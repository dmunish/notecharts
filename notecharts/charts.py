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

def _deep_update(d, u):
    """Recursively update dictionary d with u."""
    for k, v in u.items():
        if isinstance(v, dict) and k in d and isinstance(d[k], dict):
            _deep_update(d[k], v)
        else:
            d[k] = v


class Bar(Chart):
    """Pre-built Bar Chart."""
    def __init__(self, data, x, y, title=None, custom_options=None, **kwargs):
        formatted_data = _format_data(data)
        y_list = y if isinstance(y, list) else [y]
        
        series = []
        for y_col in y_list:
            series_config = {
                "type": "bar",
                "encode": {"x": x, "y": y_col},
                "name": str(y_col),
                "animationDuration": 1500,
                "animationEasing": "cubicOut"
            }
            series.append(series_config)

        options = {
            "title": {
                "text": title,
                "left": "center",
                "top": 10,
                "textStyle": {"fontWeight": "normal"}
            },
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {"type": "shadow"},
                "backgroundColor": "rgba(255, 255, 255, 0.9)",
                "borderColor": "#eee",
                "borderWidth": 1,
                "textStyle": {"color": "#333"}
            },
            "dataZoom": {"type": JSCode("'inside'")},
            "legend": {"bottom": 10, "type": "scroll"},
            "grid": {"left": "5%", "right": "5%", "bottom": "15%", "top": "15%", "containLabel": True},
            "dataset": {"source": formatted_data},
            "xAxis": {"type": "category"},
            "yAxis": {"type": "value", "splitLine": {"lineStyle": {"type": "dashed", "color": "#f0f0f0"}}},
            "series": series
        }
        
        if custom_options:
            _deep_update(options, custom_options)
            
        super().__init__(options)


class Line(Chart):
    """Pre-built Line Chart."""
    def __init__(self, data, x, y, title=None, theme="light", width="99%", height="500px", 
                 smooth=True, area=False, stacked=False, custom_options=None, **kwargs):
        formatted_data = _format_data(data)
        y_list = y if isinstance(y, list) else [y]

        series = []
        for y_col in y_list:
            series_config = {
                "type": "line",
                "encode": {"x": x, "y": y_col},
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
            series.append(series_config)
            
        options = {
            "title": {
                "text": title,
                "left": "center",
                "top": 10,
                "textStyle": {"fontWeight": "normal"}
            },
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {"type": "shadow"},
                "backgroundColor": "rgba(255, 255, 255, 0.9)",
                "borderColor": "#eee",
                "borderWidth": 1,
                "textStyle": {"color": "#333"}
            },
            "dataZoom": {"type": JSCode("'inside'")},
            "legend": {"bottom": 10, "type": "scroll"},
            "grid": {"left": "5%", "right": "5%", "bottom": "15%", "top": "15%", "containLabel": True},
            "dataset": {"source": formatted_data},
            "xAxis": {"type": "category", "boundaryGap": False},
            "yAxis": {"type": "value", "splitLine": {"lineStyle": {"type": "dashed", "color": "#f0f0f0"}}},
            "series": series
        }
        
        if custom_options:
            _deep_update(options, custom_options)
            
        super().__init__(options, width=width, height=height, theme=theme)


class Scatter(Chart):
    """Pre-built Scatter Chart."""
    def __init__(self, data, x, y, title=None, theme="light", width="99%", height="500px", 
                 symbol_size=10, custom_options=None, **kwargs):
        formatted_data = _format_data(data)
        y_list = y if isinstance(y, list) else [y]

        series = []
        for y_col in y_list:
            series_config = {
                "type": "scatter",
                "encode": {"x": x, "y": y_col},
                "name": str(y_col),
                "symbolSize": symbol_size,
                "itemStyle": {"opacity": 0.8}
            }
            series.append(series_config)

        options = {
            "title": {
                "text": title,
                "left": "center",
                "top": 10,
                "textStyle": {"fontWeight": "normal"}
            },
            "tooltip": {
                "trigger": "item",
                "axisPointer": {"type": "cross"},
                "backgroundColor": "rgba(255, 255, 255, 0.9)",
                "borderColor": "#eee",
                "borderWidth": 1,
                "textStyle": {"color": "#333"}
            },
            "dataZoom": {"type": JSCode("'inside'")},
            "legend": {"bottom": 10, "type": "scroll"},
            "grid": {"left": "5%", "right": "5%", "bottom": "15%", "top": "15%", "containLabel": True},
            "dataset": {"source": formatted_data},
            "xAxis": {
                "type": "value",
                "splitLine": {"show": True, "lineStyle": {"type": "dashed", "color": "#f0f0f0"}},
                "scale": True
            },
            "yAxis": {
                "type": "value",
                "splitLine": {"lineStyle": {"type": "dashed", "color": "#f0f0f0"}},
                "scale": True
            },
            "series": series
        }
        
        if custom_options:
            _deep_update(options, custom_options)
            
        super().__init__(options, width=width, height=height, theme=theme)