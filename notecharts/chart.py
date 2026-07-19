import json
import uuid
import urllib.parse
import base64
import zlib
from pathlib import Path
from typing import Literal, get_args
from IPython.display import display, HTML
from .option import Option

# ── Typed parameter domains ────────────────────────────────────────────
Renderer = Literal["canvas", "svg"]
Theme    = Literal["light", "dark"]
Mode     = Literal["interactive", "image"]


def _validate_param(value: str, allowed: type, name: str) -> str:
    """Normalise *value* and raise ValueError if it is not a member of *allowed*."""
    norm = value.strip().lower()
    if norm not in get_args(allowed):
        raise ValueError(
            f"Invalid {name} {norm!r}. Supported: {', '.join(get_args(allowed))}."
        )
    return norm


# Load the JavaScript template from the bundled file
_JS_TEMPLATE_FILE = Path(__file__).parent / "chart.js"
with open(_JS_TEMPLATE_FILE, "r", encoding="utf-8") as _f:
    _JS_TEMPLATE = _f.read()


class JSCode:
    """Wraps a raw JavaScript string to be inserted unquoted into the ECharts options.

    Attributes:
        js (str): The raw JavaScript code string.
    """
    def __init__(self, js: str):
        """Initializes JSCode with the given JavaScript string.

        Args:
            js (str): The JavaScript code.
        """
        self.js = js

    def __repr__(self):
        return f"JSCode({self.js!r})"


class _EChartsEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('default', self.default)
        super().__init__(*args, **kwargs)
        self.placeholders = {}

    def default(self, obj):
        if isinstance(obj, JSCode):
            placeholder = f"__JS_{uuid.uuid4().hex}__"
            self.placeholders[placeholder] = obj.js
            return placeholder
        return super().default(obj)


class Chart:

    # Generic CSS font families that should not be loaded from Google Fonts
    _GENERIC_FONTS = {
        "serif", "sans-serif", "monospace", "cursive", "fantasy",
        "system-ui", "ui-serif", "ui-sans-serif", "ui-monospace",
        "ui-rounded", "math", "emoji", "fangsong",
        "inherit", "initial", "unset"
    }

    def __init__(
        self,
        options: Option,
        mode: str = "interactive",
        width: str = "99%",
        height: str = "500px",
        renderer: str = "canvas",
        theme: str = "light",
        devicePixelRatio: int = 1,
        maps: dict = None,
        compress: bool = True
    ):
        """Render an Apache ECharts figure in a Jupyter notebook.

        Google Fonts are auto-loaded for any ``fontFamily`` value found inside
        *options*.  GeoJSON maps can be registered via the *maps* parameter.

        Args:
            options: The ECharts option dictionary.
            mode: ``"interactive"`` (default) or ``"image"``.
            width: CSS width of the chart container.  Default ``"99%"``.
            height: CSS height of the chart container.  Default ``"500px"``.
            renderer: ``"canvas"`` (default) or ``"svg"``.
            theme: ``"light"`` (default) or ``"dark"``.
            devicePixelRatio: Pixel ratio for canvas rendering.  Default ``1``.
            maps: Map name → GeoJSON data.  Default ``None``.
            compress: Compress the option payload with zlib.  Default ``True``.

        Raises:
            TypeError: *options* is not a dict, or *maps* is not dict/None.
            ValueError: *renderer*, *theme*, or *mode* has an invalid value.
        """
        if not isinstance(options, dict):
            raise TypeError(
                f"Chart options must be a dictionary, got {type(options).__name__}."
            )
        
        if maps is not None and not isinstance(maps, dict):
            raise TypeError(
                f"Chart maps must be a dictionary or None, got {type(maps).__name__}."
            )

        self.mode              = _validate_param(mode,       Mode,     "mode")
        self.renderer          = _validate_param(renderer,   Renderer, "renderer")
        self.theme             = _validate_param(theme,      Theme,    "theme")
        self.devicePixelRatio  = int(devicePixelRatio)
        
        self.options = options
        self.maps = maps or {}
        self.width = width.strip() if isinstance(width, str) else str(width)
        self.height = height.strip() if isinstance(height, str) else str(height)

        if self.theme == "light" and "backgroundColor" not in self.options:
            self.options["backgroundColor"] = "white"

        self.compress = compress

        if self.mode == "image":
            self.options.setdefault("animation", False)

        self.fonts = list(self._discover_fonts(self.options))

    # ------------------------------------------------------------------
    # Font discovery
    # ------------------------------------------------------------------
    @classmethod
    def _extract_font_families(cls, value):
        """Return a set of non‑generic font family names from a raw value."""
        if isinstance(value, JSCode):
            return set()
        if isinstance(value, str):
            candidates = [name.strip().strip("'\"") for name in value.split(",")]
        elif isinstance(value, (list, tuple)):
            candidates = []
            for item in value:
                if isinstance(item, str):
                    candidates.extend(
                        name.strip().strip("'\"") for name in item.split(",")
                    )
        else:
            return set()

        families = set()
        for candidate in candidates:
            lower = candidate.lower()
            # Keep only non‑generic names
            if lower and lower not in cls._GENERIC_FONTS:
                families.add(candidate)
        return families

    def _discover_fonts(self, obj, found=None):
        """Recursively walk the options dict to collect font families."""
        if found is None:
            found = set()
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == "fontFamily":
                    found.update(self._extract_font_families(value))
                else:
                    self._discover_fonts(value, found)
        elif isinstance(obj, list):
            for item in obj:
                self._discover_fonts(item, found)
        return found

    # ------------------------------------------------------------------
    # Serialisation
    # ------------------------------------------------------------------
    def _serialise_options(self) -> str:
        encoder = _EChartsEncoder()
        json_str = encoder.encode(self.options)
        for placeholder, js_code in encoder.placeholders.items():
            json_str = json_str.replace(f'"{placeholder}"', js_code)
        return json_str

    def _compress_options(self, options_str: str) -> tuple:
        """Compress options string using zlib and base64 encoding.
        
        Args:
            options_str (str): The serialized options string.
            
        Returns:
            tuple: (options_data, is_compressed) where options_data is either the
                   compressed base64 string or the original string, and is_compressed
                   is a boolean flag indicating if compression was applied.
        """
        if not self.compress:
            return options_str, False
        
        try:
            # Compress the options string
            compressed = zlib.compress(options_str.encode('utf-8'), level=9)
            # Encode as base64 for safe HTML embedding
            encoded = base64.b64encode(compressed).decode('ascii')
            return encoded, True
        except Exception as e:
            # Graceful fallback on compression failure
            print(f"Warning: Compression failed ({e}), falling back to uncompressed options.")
            return options_str, False

    # ------------------------------------------------------------------
    # HTML generation
    # ------------------------------------------------------------------
    def _make_chart_html(self, chart_id=None) -> str:
        if chart_id is None:
            chart_id = f"echart_{uuid.uuid4().hex}"
        
        options_js_raw = self._serialise_options()
        options_js, is_compressed = self._compress_options(options_js_raw)
        
        # If compressed, wrap in quotes; if not, use as raw JS
        if is_compressed:
            options_js_code = f"'{options_js}'"
        else:
            options_js_code = options_js
        
        # Serialize maps to JSON
        maps_json = json.dumps(self.maps) if self.maps else "{}"

        font_link = ""
        if self.fonts:
            base_url = "https://fonts.googleapis.com/css2"
            params = {"family": self.fonts, "display": "swap"}
            query_string = urllib.parse.urlencode(params, doseq=True)
            font_link = f'<link href="{base_url}?{query_string}" rel="stylesheet">'

        has_fonts = "true" if self.fonts else "false"
        has_maps = "true" if self.maps else "false"
        is_compressed_js = "true" if is_compressed else "false"

        js_code = (_JS_TEMPLATE
            .replace('__CHART_ID__', chart_id)
            .replace('__THEME__', self.theme)
            .replace('__RENDERER__', self.renderer)
            .replace('__DEVICE_PIXEL_RATIO__', str(self.devicePixelRatio))
            .replace('__OPTIONS_DATA__', options_js_code)
            .replace('__IS_COMPRESSED__', is_compressed_js)
            .replace('__HAS_MAPS__', has_maps)
            .replace('__MAPS_DATA__', maps_json)
            .replace('__HAS_FONTS__', has_fonts)
            .replace('__MODE__', self.mode)
        )

        return f"""
        {font_link}
        <div id="{chart_id}" style="width:{self.width};height:{self.height};"></div>
        <script>
        {js_code}
        </script>
        """

    # ------------------------------------------------------------------
    # Display
    # ------------------------------------------------------------------
    def display(self):
        display(HTML(self._make_chart_html()))

    def _repr_html_(self):
        return self._make_chart_html()