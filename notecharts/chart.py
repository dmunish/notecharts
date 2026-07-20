import json
import struct
import uuid
import urllib.parse
import copy
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


# ── Z85 encoding (4 bytes → 5 chars, 25% overhead vs base64's 33%) ────
_Z85_ENC = b'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-:+=^!/*?&<>()[]{}@%$#'


def _z85_encode(data: bytes) -> str:
    chars = []
    for i in range(0, len(data), 4):
        chunk = data[i:i + 4]
        pad = 4 - len(chunk)
        if pad:
            chunk = chunk + b'\0' * pad
        n = int.from_bytes(chunk, 'big')
        for j in range(4, -1, -1):
            chars.append(chr(_Z85_ENC[(n // (85 ** j)) % 85]))
    extra = (4 - len(data) % 4) % 4
    return ''.join(chars[:len(chars) - extra])


# ── Columnar-binary helpers ────────────────────────────────────────────

def _zigzag(n: int) -> int:
    return (n << 1) ^ (n >> 63)


def _write_varint(buf: bytearray, value: int) -> None:
    zig = _zigzag(value)
    while zig > 0x7f:
        buf.append((zig & 0x7f) | 0x80)
        zig >>= 7
    buf.append(zig & 0x7f)


def _is_columnar_candidate(data) -> bool:
    if not isinstance(data, list) or len(data) < 4:
        return False
    if all(isinstance(x, (int, float)) for x in data):
        return True
    if isinstance(data[0], list) and data[0] and isinstance(data[0][0], (int, float)):
        if all(isinstance(r, list) and len(r) == len(data[0]) for r in data):
            return True
    if isinstance(data[0], dict):
        keys = list(data[0].keys())
        return all(isinstance(item, dict) and all(k in item for k in keys)
                   for item in data)
    return False


def _extract_columnar(options: dict) -> tuple[dict, bytes]:
    tables = []

    def _walk(obj):
        if isinstance(obj, dict):
            for key in ('data', 'source'):
                if key in obj and _is_columnar_candidate(obj[key]):
                    idx = len(tables)
                    tables.append(obj[key])
                    obj[key] = f'@@C{idx}@@'
            for v in obj.values():
                _walk(v)
        elif isinstance(obj, list):
            for item in obj:
                _walk(item)

    _walk(options)
    if not tables:
        return options, b''

    blob = bytearray()
    blob.extend(struct.pack('<H', len(tables)))
    offset = 2 + 4 * len(tables)
    for t in tables:
        buf = _encode_table(t)
        blob.extend(struct.pack('<I', offset))
        offset += len(buf)
    for t in tables:
        blob.extend(_encode_table(t))
    return options, bytes(blob)


def _encode_table(data: list) -> bytearray:
    buf = bytearray()
    if all(isinstance(x, (int, float)) for x in data):
        buf.append(0)
        columns = [data]
    elif isinstance(data[0], list):
        buf.append(1)
        ncols = len(data[0])
        columns = [[data[r][c] for r in range(len(data))] for c in range(ncols)]
    elif isinstance(data[0], dict):
        buf.append(2)
        keys = list(data[0].keys())
        columns = [[item[k] for item in data] for k in keys]
    else:
        return bytearray()

    buf.extend(struct.pack('<B', len(columns)))
    
    if buf[0] == 2:
        for k in keys:
            encoded = k.encode('utf-8')
            buf.extend(struct.pack('<H', len(encoded)))
            buf.extend(encoded)
    
    buf.extend(struct.pack('<I', len(columns[0])))

    for col in columns:
        if all(not isinstance(x, (int, float)) or isinstance(x, bool) for x in col):
            buf.append(2)
            _encode_string_column(buf, [str(x) for x in col])
        elif all(isinstance(x, int) or (isinstance(x, float) and x == int(x))
                 for x in col):
            buf.append(0)
            _encode_int_column(buf, [int(x) for x in col])
        else:
            buf.append(1)
            _encode_float_column(buf, [float(x) for x in col])
    return buf


def _encode_int_column(buf: bytearray, values: list[int]) -> None:
    _write_varint(buf, values[0])
    for i in range(1, len(values)):
        _write_varint(buf, values[i] - values[i - 1])


def _encode_float_column(buf: bytearray, values: list[float]) -> None:
    for v in values:
        buf.extend(struct.pack('<d', v))


def _encode_string_column(buf: bytearray, values: list[str]) -> None:
    unique = {}
    for v in values:
        if v not in unique:
            unique[v] = len(unique)
    strings = list(unique.keys())
    buf.extend(struct.pack('<H', len(strings)))
    for s in strings:
        encoded = s.encode('utf-8')
        buf.extend(struct.pack('<H', len(encoded)))
        buf.extend(encoded)
    for v in values:
        _write_varint(buf, unique[v])


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
    def _serialise_options(self, obj=None) -> str:
        if obj is None:
            obj = self.options
        encoder = _EChartsEncoder()
        json_str = encoder.encode(obj)
        for placeholder, js_code in encoder.placeholders.items():
            json_str = json_str.replace(f'"{placeholder}"', js_code)
        return json_str

    # ------------------------------------------------------------------
    # HTML generation
    # ------------------------------------------------------------------
    def _make_chart_html(self, chart_id=None) -> str:
        if chart_id is None:
            chart_id = f"echart_{uuid.uuid4().hex}"

        if self.compress:
            working_options = copy.deepcopy(self.options)
            skeleton, columnar_blob = _extract_columnar(working_options)
            options_json = self._serialise_options(skeleton)

            if columnar_blob:
                packed = struct.pack('<I', len(options_json)) + \
                         options_json.encode('utf-8') + columnar_blob
                compressed = zlib.compress(packed, level=6)
                options_js_code = f"'{_z85_encode(compressed)}'"
                compress_format = 'columnar'
            else:
                compressed = zlib.compress(options_json.encode('utf-8'), level=6)
                options_js_code = f"'{_z85_encode(compressed)}'"
                compress_format = 'z85'

            if self.maps:
                maps_raw = json.dumps(self.maps)
                maps_compressed = zlib.compress(maps_raw.encode('utf-8'), level=6)
                maps_json = f"'{_z85_encode(maps_compressed)}'"
                maps_compressed_flag = "true"
            else:
                maps_json = "{}"
                maps_compressed_flag = "false"
        else:
            options_json = self._serialise_options()
            options_js_code = options_json
            compress_format = 'none'
            maps_json = json.dumps(self.maps) if self.maps else "{}"
            maps_compressed_flag = "false"

        font_link = ""
        if self.fonts:
            base_url = "https://fonts.googleapis.com/css2"
            params = {"family": self.fonts, "display": "swap"}
            query_string = urllib.parse.urlencode(params, doseq=True)
            font_link = f'<link href="{base_url}?{query_string}" rel="stylesheet">'

        has_fonts = "true" if self.fonts else "false"
        has_maps = "true" if self.maps else "false"

        js_code = (_JS_TEMPLATE
            .replace('__CHART_ID__', chart_id)
            .replace('__THEME__', self.theme)
            .replace('__RENDERER__', self.renderer)
            .replace('__DEVICE_PIXEL_RATIO__', str(self.devicePixelRatio))
            .replace('__OPTIONS_DATA__', options_js_code)
            .replace('__COMPRESS_FORMAT__', compress_format)
            .replace('__HAS_MAPS__', has_maps)
            .replace('__MAPS_DATA__', maps_json)
            .replace('__MAPS_COMPRESSED__', maps_compressed_flag)
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