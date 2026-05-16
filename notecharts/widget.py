import json
import uuid
import urllib.parse
import base64
import zlib
from IPython.display import display, HTML

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
        super().__init__(*args, **kwargs)
        self.placeholders = {}

    def default(self, obj):
        if isinstance(obj, JSCode):
            placeholder = f"__JS_{uuid.uuid4().hex}__"
            self.placeholders[placeholder] = obj.js
            return placeholder
        return super().default(obj)


class Chart:
    """Renders Apache ECharts directly in a Jupyter notebook from a Python 'options' dict.

    Features include automatic Google Fonts loading from any 'fontFamily' value found
    inside the options dictionary and global font setting via `textStyle.fontFamily`.
    Supports registering GeoJSON maps for map-type charts.

    Attributes:
        options (dict): The ECharts option dictionary.
        maps (dict): Dictionary mapping map names to GeoJSON data.
        width (str): CSS width of the chart container.
        height (str): CSS height of the chart container.
        renderer (str): The renderer type ('canvas' or 'svg').
        theme (str): The chart theme ('light' or 'dark').
        devicePixelRatio (str): The pixel ratio at which to render when using Canvas. Default is 1.
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
        devicePixelRatio = 1,
        maps: dict = None,
        compress: bool = True
    ):
        """Initializes the Chart with options and display settings.

        Args:
            options (dict): The ECharts option dictionary.
            width (str, optional): CSS width. Defaults to "99%".
            height (str, optional): CSS height. Defaults to "500px".
            renderer (str, optional): 'canvas' or 'svg'. Defaults to "canvas".
            theme (str, optional): 'light' or 'dark'. Defaults to "light".
            devicePixelRatio(int, optional): The pixel ratio at which to render when using Canvas. Default is 1.
            maps (dict, optional): Dictionary mapping map names to GeoJSON data. Defaults to None.
            compress (bool, optional): Whether to compress options using zlib. Defaults to True.

        Raises:
            TypeError: If options is not a dictionary or maps is not a dictionary/None.
            ValueError: If renderer or theme is invalid.
        """
        if not isinstance(options, dict):
            raise TypeError(
                f"Chart options must be a dictionary, got {type(options).__name__}."
            )
        
        if maps is not None and not isinstance(maps, dict):
            raise TypeError(
                f"Chart maps must be a dictionary or None, got {type(maps).__name__}."
            )
        
        self.options = options
        self.maps = maps or {}
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
        
        self.devicePixelRatio = int(devicePixelRatio)

        if self.theme == "light" and "backgroundColor" not in self.options:
            self.options["backgroundColor"] = "white"

        self.compress = compress

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

        return f"""
        {font_link}
        <div id="{chart_id}" style="width:{self.width};height:{self.height};"></div>
        <script>
        (function() {{

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

            // ── Decompress and parse options ────────────────────────────────
            function parseOptions(rawOptions, isCompressed, fflate) {{
                var finalOptions;
                try {{
                    if (isCompressed) {{
                        if (!fflate) {{
                            console.error('ECharts wrapper: fflate library not available for decompression. Available:', typeof window.fflate);
                            return null;
                        }}
                        if (!fflate.unzlibSync) {{
                            console.error('ECharts wrapper: fflate.unzlibSync not available');
                            return null;
                        }}
                        // Decode base64 to Uint8Array
                        var binaryString = window.atob(rawOptions);
                        var len = binaryString.length;
                        var bytes = new Uint8Array(len);
                        for (var i = 0; i < len; i++) {{
                            bytes[i] = binaryString.charCodeAt(i);
                        }}
                        // Decompress using fflate
                        var decompressed = fflate.unzlibSync(bytes);
                        // Convert bytes to string
                        var decoder = new TextDecoder();
                        var optionsString = decoder.decode(decompressed);
                        // Parse as JavaScript object (supports JSCode functions)
                        finalOptions = new Function('return ' + optionsString)();
                    }} else {{
                        // Uncompressed: rawOptions is already a dynamically evaluated JS object literal
                        finalOptions = rawOptions;
                    }}
                    return finalOptions;
                }} catch (e) {{
                    console.error('ECharts wrapper: Error parsing options:', e);
                    console.error('  isCompressed:', isCompressed);
                    console.error('  fflate available:', !!fflate);
                    if (e.stack) {{
                        console.error('  Stack:', e.stack);
                    }}
                    return null;
                }}
            }}

            // ── chart init ─────
            function initChart(ec, fflate) {{
                waitForDom('{chart_id}', function(dom) {{
                    var chart = ec.init(dom, '{self.theme}', {{
                        renderer: '{self.renderer}', devicePixelRatio: {self.devicePixelRatio}
                    }});
                    
                    // Parse the options (handles both compressed and uncompressed)
                    var rawOptions = {options_js_code};
                    var isCompressed = {is_compressed_js};
                    var options = parseOptions(rawOptions, isCompressed, fflate);
                    
                    if (!options) {{
                        console.error('ECharts wrapper: Failed to parse options');
                        return;
                    }}
                    
                    // Register maps if provided
                    if ({has_maps}) {{
                        var maps = {maps_json};
                        Object.entries(maps).forEach(function([name, data]) {{
                            ec.registerMap(name, data);
                        }});
                    }}
                    
                    chart.setOption(options);
                    window.addEventListener('resize', function() {{ chart.resize(); }});
                }});
            }}

            // ── Check if echarts and fflate are already loaded ─────────────────
            function modulesReady(cb) {{
                var needsFflate = {is_compressed_js};
                
                if (typeof window.echarts !== 'undefined') {{
                    if (needsFflate && typeof window.fflate === 'undefined') {{
                        return false; // Still need fflate
                    }}
                    cb(window.echarts, window.fflate);
                    return;
                }}
                if (typeof require !== 'undefined' && typeof require.config === 'function') {{
                    if (require.defined && (require.defined('echarts') || require.defined('echarts-gl'))) {{
                        if (needsFflate) {{
                            if (typeof window.fflate === 'undefined') {{
                                return false; // Force fallback to loaders
                            }}
                            require(['echarts'], function(ec) {{
                                cb(ec, window.fflate);
                            }});
                            return;
                        }} else {{
                            require(['echarts'], function(ec) {{
                                cb(ec, undefined);
                            }});
                            return;
                        }}
                    }}
                }}
                // Not loaded yet, fall through to load it
                return false;
            }}

            // ── plain <script> loader (Colab / plain Jupyter) ─────────────────
            function loadScript(url, cb) {{
                var s = document.createElement('script');
                s.src = url;
                s.onload = cb;
                s.onerror = function() {{ console.error('ECharts wrapper: failed to load ' + url); }};
                document.head.appendChild(s);
            }}

            function loadViaScript() {{
                // Skip if already loaded globally
                if (typeof window.echarts !== 'undefined') {{
                    // Check if fflate is needed
                    var needsFflate = {is_compressed_js};
                    if (needsFflate && typeof window.fflate === 'undefined') {{
                        loadScript('https://cdn.jsdelivr.net/npm/fflate@0.8.3/umd/index.js', function() {{
                            initChart(window.echarts, window.fflate);
                        }});
                    }} else {{
                        initChart(window.echarts, window.fflate || undefined);
                    }}
                    return;
                }}
                loadScript('https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js', function() {{
                    loadScript('https://cdn.jsdelivr.net/npm/echarts-gl/dist/echarts-gl.min.js', function() {{
                        var needsFflate = {is_compressed_js};
                        if (needsFflate && typeof window.fflate === 'undefined') {{
                            loadScript('https://cdn.jsdelivr.net/npm/fflate@0.8.3/umd/index.js', function() {{
                                initChart(window.echarts, window.fflate);
                            }});
                        }} else {{
                            initChart(window.echarts, window.fflate || undefined);
                        }}
                    }});
                }});
            }}

            // ── RequireJS loader (VS Code webview) ────────────────────────────
            function loadViaRequire() {{
                var needsFflate = {is_compressed_js};
                var paths = {{
                    'echarts': 'https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min',
                    'echarts-gl': 'https://cdn.jsdelivr.net/npm/echarts-gl/dist/echarts-gl.min'
                }};
                
                require.config({{ paths: paths }});
                
                function doLoadEcharts() {{
                    require(['echarts'], function(ec) {{
                        require(['echarts-gl'], function() {{
                            initChart(ec, window.fflate);
                        }});
                    }}, function(err) {{
                        console.error('ECharts wrapper: RequireJS failed to load echarts modules:', err);
                    }});
                }}

                if (needsFflate && typeof window.fflate === 'undefined') {{
                    // Fetch fflate and execute it while shadowing module/exports/define
                    // to prevent UMD loader conflicts with RequireJS in VS Code webviews
                    fetch('https://cdn.jsdelivr.net/npm/fflate@0.8.2/umd/index.js')
                        .then(function(res) {{ return res.text(); }})
                        .then(function(text) {{
                            var wrapper = new Function('module', 'exports', 'define', text);
                            wrapper(undefined, undefined, undefined);
                            doLoadEcharts();
                        }})
                        .catch(function(err) {{
                            console.error('ECharts wrapper: Failed to fetch fflate:', err);
                        }});
                }} else {{
                    doLoadEcharts();
                }}
            }}

            // ── font gate → then load echarts ─────────────────────────────────
            function loadEchartsAndInit() {{
                // First check if already available
                if (modulesReady(initChart) !== false) {{
                    return;
                }}
                // Not available, load it
                if (typeof require !== 'undefined' && typeof require.config === 'function') {{
                    loadViaRequire();
                }} else {{
                    loadViaScript();
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