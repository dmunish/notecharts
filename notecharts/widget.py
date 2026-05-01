import json
import uuid
from IPython.display import display, HTML


class JSCode:
    """Wrap a raw JavaScript string so it is inserted unquoted into the option object."""
    def __init__(self, js: str):
        self.js = js

    def __repr__(self):
        return f"JSCode({self.js!r})"


class _EChartsEncoder(json.JSONEncoder):
    """Custom encoder that replaces JSCode with unique placeholders."""
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
    Render Apache ECharts directly in a Jupyter notebook from a Python dict.

    Use `JSCode` for any value that should be raw JavaScript (formatters,
    symbol size functions, linear gradients, etc.).

    Usage:
        from notecharts import Chart, JSCode

        options = {
            "tooltip": {"formatter": JSCode("function(p){ return p.value; }")},
            ...
        }
        widget = Chart(options)
        widget.display()   # or just `widget` at the end of a cell
    """

    def __init__(self, options, width="99%", height="600px", renderer = "svg", theme = "light"):
        self.options = options
        self.width = width.strip()
        self.height = height.strip()
        self.renderer = renderer.lower().strip()
        self.theme = theme.lower().strip()

        # Explicitly set default behaviour
        if self.theme == "light" and "backgroundColor" not in self.options:
            self.options["backgroundColor"] = "white"

    # ------------------------------------------------------------------
    # Serialisation
    # ------------------------------------------------------------------
    def _serialise_options(self) -> str:
        """Convert the options dict (with possible JSCode) into a JS option string."""
        encoder = _EChartsEncoder()
        json_str = encoder.encode(self.options)

        for placeholder, js_code in encoder.placeholders.items():
            json_str = json_str.replace(f'"{placeholder}"', js_code)
        return json_str

    # ------------------------------------------------------------------
    # HTML generation
    # ------------------------------------------------------------------
    def _make_chart_html(self, chart_id=None) -> str:
        """Build the <div> + <script> for a unique chart instance."""
        if chart_id is None:
            chart_id = f"echart_{uuid.uuid4().hex}"
        options_js = self._serialise_options()
        return f"""
        <div id="{chart_id}" style="width:{self.width};height:{self.height};"></div>
        <script>
        (function() {{
            if (typeof echarts === 'undefined') {{
                var script = document.createElement('script');
                script.src = 'https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js';
                script.onload = function() {{ initChart('{chart_id}'); }};
                document.head.appendChild(script);
            }} else {{
                initChart('{chart_id}');
            }}

            function initChart(id) {{
                var dom = document.getElementById(id);
                if (!dom) return;
                var chart = echarts.init(dom, '{self.theme}', {{renderer: '{self.renderer}'}});
                chart.setOption({options_js});
                window.addEventListener('resize', function() {{
                    chart.resize();
                }});
            }}
        }})();
        </script>
        """

    # ------------------------------------------------------------------
    # Display methods
    # ------------------------------------------------------------------
    def display(self):
        """Explicitly render the chart. Each call produces a new, fresh chart."""
        display(HTML(self._make_chart_html()))

    def _repr_html_(self):
        """Called by Jupyter when the object is the last expression in a cell."""
        return self._make_chart_html()