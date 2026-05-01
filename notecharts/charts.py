from .widget import Chart, JSCode

def _format_data(data):
    """
    Normalizes data into a format ECharts dataset.source accepts natively:
    list of dicts, or list of lists.
    Auto-detects pandas DataFrames and converts them.
    """
    # Check if it's a pandas DataFrame without explicitly importing pandas
    if hasattr(data, "to_dict") and hasattr(data, "columns"):
        # Convert DataFrame to list of dicts
        return data.to_dict(orient="records")
    return data

class BaseDataChart(Chart):
    """
    Base class for data-driven pre-built charts.
    """
    def __init__(self, data, x, y, title=None, theme="light", width="99%", height="500px", 
                 custom_options=None, **kwargs):
        self.data = _format_data(data)
        self.x = x
        self.y = y if isinstance(y, list) else [y]
        
        self.base_options = {
            "title": {"text": title, "left": "center", "top": 10, "textStyle": {"fontWeight": "normal"}},
            "tooltip": {
                "trigger": "axis" if self.__class__.__name__ != "Scatter" else "item",
                "axisPointer": {"type": "cross" if self.__class__.__name__ == "Scatter" else "shadow"},
                "backgroundColor": "rgba(255, 255, 255, 0.9)",
                "borderColor": "#eee",
                "borderWidth": 1,
                "textStyle": {"color": "#333"}
            },
            "dataZoom": {"type": JSCode("'inside'")},
            "legend": {"bottom": 10, "type": "scroll"},
            "grid": {"left": "5%", "right": "5%", "bottom": "15%", "top": "15%", "containLabel": True},
            "dataset": {"source": self.data},
            "xAxis": {"type": "category"},
            "yAxis": {"type": "value", "splitLine": {"lineStyle": {"type": "dashed", "color": "#f0f0f0"}}},
            "series": []
        }
        
        # Build series definition
        self._build_series(**kwargs)
        
        # Allows user to inject or override everything (e.g. customized colors, advanced axes)
        if custom_options:
            self._deep_update(self.base_options, custom_options)
            
        super().__init__(self.base_options, width=width, height=height, theme=theme)

    def _build_series(self, **kwargs):
        raise NotImplementedError("Subclasses must implement _build_series")

    def _deep_update(self, d, u):
        """Recursively update dictionary d with u."""
        for k, v in u.items():
            if isinstance(v, dict) and k in d and isinstance(d[k], dict):
                self._deep_update(d[k], v)
            else:
                d[k] = v


class Bar(BaseDataChart):
    """Pre-built Bar Chart."""
    def _build_series(self, stacked=False, rounded=True, **kwargs):
        for y_col in self.y:
            series_config = {
                "type": "bar",
                "encode": {"x": self.x, "y": y_col},
                "name": str(y_col),
                "animationDuration": 1500,
                "animationEasing": "cubicOut"
            }
            if stacked:
                series_config["stack"] = "total"
            if rounded:
                series_config["itemStyle"] = {"borderRadius": [4, 4, 0, 0]}
                
            self.base_options["series"].append(series_config)


class Line(BaseDataChart):
    """Pre-built Line Chart."""
    def _build_series(self, smooth=True, area=False, stacked=False, **kwargs):
        # Line charts usually look better with a boundary gap on the X axis set to false
        self.base_options["xAxis"]["boundaryGap"] = False

        for y_col in self.y:
            series_config = {
                "type": "line",
                "encode": {"x": self.x, "y": y_col},
                "name": str(y_col),
                "smooth": smooth,
                "symbol": "circle",
                "symbolSize": 6,
                "showSymbol": False,  # Only show points on hover for a cleaner look
            }
            if stacked:
                series_config["stack"] = "total"
            if area:
                series_config["areaStyle"] = {"opacity": 0.3}
                
            self.base_options["series"].append(series_config)


class Scatter(BaseDataChart):
    """Pre-built Scatter Chart."""
    def _build_series(self, symbol_size=10, **kwargs):
        # Scatters require both X and Y to be values (usually)
        self.base_options["xAxis"]["type"] = "value"
        self.base_options["xAxis"]["splitLine"] = {"show": True, "lineStyle": {"type": "dashed", "color": "#f0f0f0"}}
        self.base_options["xAxis"]["scale"] = True   # Don't force X axis to start at 0
        self.base_options["yAxis"]["scale"] = True   # Don't force Y axis to start at 0

        for y_col in self.y:
            series_config = {
                "type": "scatter",
                "encode": {"x": self.x, "y": y_col},
                "name": str(y_col),
                "symbolSize": symbol_size,
                "itemStyle": {"opacity": 0.8}
            }
            self.base_options["series"].append(series_config)