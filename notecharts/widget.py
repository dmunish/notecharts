import json
import uuid
import urllib.parse
from IPython.display import display, HTML


class JSCode:
    """Wrap a raw JavaScript string so it is inserted unquoted into the option object."""
    def __init__(self, js: str):
        self.js = js

    def __repr__(self):
        return f"JSCode({self.js!r})"


class _EChartsEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.placeholders = {}

    def default(self, obj):
        if isinstance(obj, JSCode):
            placeholder = f"__JS_{uuid.uuid4().hex}__"
            self.placeholders[placeholder] = obj.js
            return placeholder
        return super().default(obj)


class Chart:
    """
    Render Apache ECharts directly in a Jupyter notebook from a Python 'options' dict.

    Features:
      - Automatic Google Fonts loading from any 'fontFamily' value found
        inside the options dictionary (deep search).
      - Global font setting via `textStyle.fontFamily` at the root level.

    Args:
        options (dict): The ECharts option dictionary.
        width (str): CSS width of the chart container.
        height (str): CSS height of the chart container.
        renderer (str): 'canvas' or 'svg'.
        theme (str): 'light' or 'dark'.

    Raises:
        ValueError: If an unsupported `renderer` or `theme` is provided.
        TypeError: If `options` is not a dictionary.
    """

    # Generic CSS font families that should not be loaded from Google Fonts
    _GENERIC_FONTS = {
        "serif", "sans-serif", "monospace", "cursive", "fantasy",
        "system-ui", "ui-serif", "ui-sans-serif", "ui-monospace",
        "ui-rounded", "math", "emoji", "fangsong",
        "inherit", "initial", "unset"
    }

    def __init__(
        self,
        options: dict,
        width: str = "99%",
        height: str = "500px",
        renderer: str = "canvas",
        theme: str = "light",
    ):
        if not isinstance(options, dict):
            raise TypeError(
                f"Chart options must be a dictionary, got {type(options).__name__}."
            )
        self.options = options
        self.width = width.strip() if isinstance(width, str) else str(width)
        self.height = height.strip() if isinstance(height, str) else str(height)

        self.renderer = renderer.lower().strip()
        if self.renderer not in ["canvas", "svg"]:
            raise ValueError(
                f"Invalid renderer '{self.renderer}'. Supported: 'canvas', 'svg'."
            )

        self.theme = theme.lower().strip()
        if self.theme not in ["light", "dark"]:
            raise ValueError(
                f"Invalid theme '{self.theme}'. Supported: 'light', 'dark'."
            )

        if self.theme == "light" and "backgroundColor" not in self.options:
            self.options["backgroundColor"] = "white"

        # Discover all custom font families from the options dict
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

    # ------------------------------------------------------------------
    # HTML generation
    # ------------------------------------------------------------------
    def _make_chart_html(self, chart_id=None) -> str:
        if chart_id is None:
            chart_id = f"echart_{uuid.uuid4().hex}"
        options_js = self._serialise_options()

        font_link = ""
        if self.fonts:
            base_url = "https://fonts.googleapis.com/css2"
            params = {"family": self.fonts, "display": "swap"}
            query_string = urllib.parse.urlencode(params, doseq=True)
            font_link = f'<link href="{base_url}?{query_string}" rel="stylesheet">'

        has_fonts = "true" if self.fonts else "false"

        return f"""
        {font_link}
        <div id="{chart_id}" style="width:{self.width};height:{self.height};"></div>
        <script>
        (function() {{
            var EC_URL = 'https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js';
            var GL_URL = 'https://cdn.jsdelivr.net/npm/echarts-gl/dist/echarts-gl.min.js';

            // ── wait for the div to exist in the DOM ──────────────────────────
            function waitForDom(id, cb) {{
                var dom = document.getElementById(id);
                if (dom) {{ cb(dom); return; }}
                var observer = new MutationObserver(function() {{
                    var el = document.getElementById(id);
                    if (el) {{ observer.disconnect(); cb(el); }}
                }});
                observer.observe(document.body || document.documentElement, {{
                    childList: true, subtree: true
                }});
                var attempts = 0;
                var poll = setInterval(function() {{
                    var el = document.getElementById(id);
                    if (el) {{ clearInterval(poll); observer.disconnect(); cb(el); return; }}
                    if (++attempts > 100) {{
                        clearInterval(poll); observer.disconnect();
                        console.error('ECharts wrapper: #{chart_id} never appeared in DOM');
                    }}
                }}, 100);
            }}

            function initChart() {{
                waitForDom('{chart_id}', function(dom) {{
                    var chart = echarts.init(dom, '{self.theme}', {{
                        renderer: '{self.renderer}', devicePixelRatio: 3
                    }});
                    chart.setOption({options_js});
                    window.addEventListener('resize', function() {{ chart.resize(); }});
                }});
            }}

            function loadScript(url, cb) {{
                var s = document.createElement('script');
                s.src = url;
                s.onload = cb;
                s.onerror = function() {{ console.error('ECharts wrapper: failed to load ' + url); }};
                document.head.appendChild(s);
            }}

            function loadEchartsAndInit() {{
                if (typeof echarts === 'undefined') {{
                    loadScript(EC_URL, function() {{
                        if (typeof echarts._glLoaded === 'undefined') {{
                            echarts._glLoaded = true;
                            loadScript(GL_URL, initChart);
                        }} else {{
                            initChart();
                        }}
                    }});
                }} else {{
                    if (typeof echarts._glLoaded === 'undefined') {{
                        echarts._glLoaded = true;
                        loadScript(GL_URL, initChart);
                    }} else {{
                        initChart();
                    }}
                }}
            }}

            if ({has_fonts}) {{
                if (document.fonts && document.fonts.ready) {{
                    document.fonts.ready.then(loadEchartsAndInit);
                }} else {{
                    loadEchartsAndInit();
                }}
            }} else {{
                loadEchartsAndInit();
            }}
        }})();
        </script>
        """

    # ------------------------------------------------------------------
    # Display
    # ------------------------------------------------------------------
    def display(self):
        display(HTML(self._make_chart_html()))

    def _repr_html_(self):
        return self._make_chart_html()