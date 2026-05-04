"""Pre-built chart classes for common visualization patterns."""

from typing import Union
from .widget import Chart, JSCode, PaletteName


def _deep_update(d, u):
    """Recursively updates a dictionary.

    Args:
        d (dict): The dictionary to update.
        u (dict): The update dictionary.
    """
    for k, v in u.items():
        if isinstance(v, dict) and k in d and isinstance(d[k], dict):
            _deep_update(d[k], v)
        else:
            d[k] = v


class Bar(Chart):
    """Pre-built modern Bar Chart.

    Creates a 2D bar chart from x-axis categories and one or more y-series.
    Automatically determines n_colors based on the number of series.

    Args:
        x (list): X-axis categories (labels).
        y (dict): Mapping of series names to data lists, e.g. {"Sales": [10, 20, 30]}.
        title (str, optional): Chart title. Defaults to None.
        colors (list or str, optional): Optional list of colors, or the name of a palette. Defaults to None.
        width (str, optional): CSS width. Defaults to "99%".
        height (str, optional): CSS height. Defaults to "500px".
        renderer (str, optional): 'canvas' or 'svg'. Defaults to "canvas".
        theme (str, optional): 'light' or 'dark'. Defaults to "light".
        options (dict, optional): ECharts options to merge/override.
        **kwargs: Forwarded to the base Chart class.
    """

    def __init__(
        self,
        x,
        y,
        title=None,
        colors: Union[list, PaletteName, str] = None,
        width="99%",
        height="500px",
        renderer="canvas",
        theme="light",
        options=None,
        **kwargs
    ):
        n_series = len(y) if isinstance(y, dict) else 1

        # Build series array from y dict
        series = []
        for series_name, data in (y.items() if isinstance(y, dict) else [(None, y)]):
            series.append({
                "type": "bar",
                "name": str(series_name) if series_name else "value",
                "data": data,
                "itemStyle": {
                    "borderRadius": [6, 6, 0, 0],
                },
                "animationDuration": 1200,
                "animationEasing": "cubicOut",
            })

        # Build base options
        base_options = {
            "xAxis": {
                "type": "category",
                "data": x,
                "axisLine": {"show": False},
                "axisTick": {"show": False},
                "axisLabel": {"fontSize": 12},
            },
            "yAxis": {
                "type": "value",
                "splitLine": {"lineStyle": {"type": "dashed"}},
                "axisLabel": {"fontSize": 12},
            },
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {"type": "shadow"},
                "borderWidth": 0,
                "padding": [14, 18],
                "shadowBlur": 10,
                "shadowColor": "rgba(0, 0, 0, 0.4)",
                "shadowOffsetX": 0,
                "shadowOffsetY": 4,
                "extraCssText": "border-radius: 12px;",
            },
            "toolbox": {
                "feature": {
                    "restore": {},
                    "magicType": {"type": ["line", "stack"]},
                    "saveAsImage": {"name": title if title else "Chart"},
                }
            },
            "dataZoom": {"type": JSCode("'inside'")},
            "legend": {
                "bottom": 20,
                "type": "scroll",
                "icon": "roundRect",
                "textStyle": {"fontSize": 13},
            },
            "grid": {
                "left": "5%",
                "right": "5%",
                "bottom": "18%",
                "top": "18%",
                "containLabel": True,
            },
            "series": series,
        }

        if title is not None:
            base_options["title"] = {
                "text": title,
                "left": "center",
                "top": 24,
                "textStyle": {"fontSize": 22, "fontWeight": 600},
            }

        if colors is not None:
            base_options["color"] = colors

        # Merge user options
        if options:
            _deep_update(base_options, options)

        super().__init__(
            options=base_options,
            width=width,
            height=height,
            renderer=renderer,
            theme=theme,
            **kwargs
        )


class Line(Chart):
    """Pre-built modern Line Chart.

    Creates a line chart with optional area fill and smooth interpolation.
    Automatically determines n_colors based on the number of series.

    Args:
        x (list): X-axis categories (labels).
        y (dict): Mapping of series names to data lists.
        title (str, optional): Chart title. Defaults to None.
        colors (list or str, optional): Optional list of colors, or the name of a palette. Defaults to None.
        width (str, optional): CSS width. Defaults to "99%".
        height (str, optional): CSS height. Defaults to "500px".
        renderer (str, optional): 'canvas' or 'svg'. Defaults to "canvas".
        theme (str, optional): 'light' or 'dark'. Defaults to "light".
        options (dict, optional): ECharts options to merge/override.
        **kwargs: Forwarded to the base Chart class.
    """

    def __init__(
        self,
        x,
        y,
        title=None,
        colors: Union[list, PaletteName, str] = None,
        width="99%",
        height="500px",
        renderer="canvas",
        theme="light",
        options=None,
        **kwargs
    ):
        # Build series array from y dict
        series = []
        for series_name, data in (y.items() if isinstance(y, dict) else [(None, y)]):
            ser = {
                "type": "line",
                "name": str(series_name) if series_name else "value",
                "data": data,
                "smooth": False,
                "symbol": "circle",
                "symbolSize": 8,
                "lineStyle": {"width": 3},
                "animationDuration": 1000,
                "animationEasing": "cubicOut",
            }
            series.append(ser)

        base_options = {
            "xAxis": {
                "type": "category",
                "data": x,
                "axisLine": {"show": False},
                "axisTick": {"show": False},
                "axisLabel": {"fontSize": 12},
            },
            "yAxis": {
                "type": "value",
                "splitLine": {"lineStyle": {"type": "dashed"}},
                "axisLabel": {"fontSize": 12},
            },
            "tooltip": {
                "trigger": "axis",
                "borderWidth": 0,
                "padding": [14, 18],
                "shadowBlur": 10,
                "shadowColor": "rgba(0, 0, 0, 0.12)",
                "extraCssText": "border-radius: 12px;",
            },
            "toolbox": {
                "feature": {
                    "restore": {},
                    "magicType": {"type": ["bar", "stack"]},
                    "saveAsImage": {"name": title if title else "Chart", "pixelRatio": 3},
                }
            },
            "dataZoom": {"type": JSCode("'inside'")},
            "legend": {
                "bottom": 20,
                "type": "scroll",
                "icon": "circle",
                "textStyle": {"fontSize": 13},
            },
            "grid": {
                "left": "5%",
                "right": "5%",
                "bottom": "18%",
                "top": "18%",
                "containLabel": True,
            },
            "series": series,
        }

        if title is not None:
            base_options["title"] = {
                "text": title,
                "left": "center",
                "top": 24,
                "textStyle": {"fontSize": 22, "fontWeight": 600},
            }

        if colors is not None:
            base_options["color"] = colors

        if options:
            _deep_update(base_options, options)

        super().__init__(
            options=base_options,
            width=width,
            height=height,
            renderer=renderer,
            theme=theme,
            **kwargs
        )


class Scatter(Chart):
    """Pre-built modern Scatter Plot.

    Creates a 2D or 3D scatter plot depending on whether z is provided.
    Automatically determines n_colors based on the number of series.

    Args:
        x (list): X-axis data.
        y (list): Y-axis data.
        z (list, optional): Z-axis data for 3D scatter. Defaults to None.
        title (str, optional): Chart title. Defaults to None.
        colors (list or str, optional): Optional list of colors, or the name of a palette. Defaults to None.
        width (str, optional): CSS width. Defaults to "99%".
        height (str, optional): CSS height. Defaults to "500px".
        renderer (str, optional): 'canvas' or 'svg'. Defaults to "canvas".
        theme (str, optional): 'light' or 'dark'. Defaults to "light".
        options (dict, optional): ECharts options to merge/override.
        **kwargs: Forwarded to the base Chart class.
    """

    def __init__(
        self,
        x,
        y,
        z=None,
        title=None,
        colors: Union[list, PaletteName, str] = None,
        width="99%",
        height="500px",
        renderer="canvas",
        theme="light",
        options=None,
        **kwargs
    ):
        is_3d = z is not None

        # Build data points
        if is_3d:
            data = [[x[i], y[i], z[i]] for i in range(len(x))]
        else:
            data = [[x[i], y[i]] for i in range(len(x))]

        series = [{
            "type": "scatter3D" if is_3d else "scatter",
            "name": "data",
            "data": data,
            "symbolSize": 10,
            "animationDuration": 1000,
            "animationEasing": "cubicOut",
        }]

        base_options = {
            "tooltip": {
                "trigger": "item",
                "borderWidth": 0,
                "padding": [14, 18],
                "shadowBlur": 10,
                "shadowColor": "rgba(0, 0, 0, 0.12)",
                "extraCssText": "border-radius: 12px;",
            },
            "toolbox": {
                "feature": {
                    "restore": {},
                    "saveAsImage": {"name": title if title else "Chart", "pixelRatio": 3},
                }
            },
            "series": series,
        }

        if is_3d:
            base_options.update({
                "grid3D": {"boxWidth": 100, "boxDepth": 100, "boxHeight": 100},
                "xAxis3D": {"type": "value"},
                "yAxis3D": {"type": "value"},
                "zAxis3D": {"type": "value"},
            })
        else:
            base_options.update({
                "xAxis": {"type": "value", "splitLine": {"lineStyle": {"type": "dashed"}}},
                "yAxis": {"type": "value", "splitLine": {"lineStyle": {"type": "dashed"}}},
                "grid": {
                    "left": "5%",
                    "right": "5%",
                    "bottom": "15%",
                    "top": "15%",
                    "containLabel": True,
                },
            })

        if title is not None:
            base_options["title"] = {
                "text": title,
                "left": "center",
                "top": 24,
                "textStyle": {"fontSize": 22, "fontWeight": 600},
            }

        if colors is not None:
            base_options["color"] = colors

        if options:
            _deep_update(base_options, options)

        super().__init__(
            options=base_options,
            width=width,
            height=height,
            renderer=renderer,
            theme=theme,
            **kwargs
        )


class Radar(Chart):
    """Pre-built modern Radar Chart.

    Radar charts are ideal for displaying multivariate data on a 2D chart.
    Each series represents a different entity with values across multiple dimensions.

    Args:
        series_data (dict): Mapping of series names to lists of values.
                            e.g. {"Player A": [80, 90, 70], "Player B": [85, 80, 95]}
        dimensions (list[str]): Names of the radar axes. e.g. ["Speed", "Power", "Agility"]
        title (str, optional): Chart title. Defaults to None.
        colors (list or str, optional): Optional list of colors, or the name of a palette. Defaults to None.
        width (str, optional): CSS width. Defaults to "99%".
        height (str, optional): CSS height. Defaults to "500px".
        renderer (str, optional): 'canvas' or 'svg'. Defaults to "canvas".
        theme (str, optional): 'light' or 'dark'. Defaults to "light".
        options (dict, optional): ECharts options to merge/override.
        **kwargs: Forwarded to the base Chart class.
    """

    def __init__(
        self,
        series_data,
        dimensions,
        title=None,
        colors: Union[list, PaletteName, str] = None,
        width="99%",
        height="500px",
        renderer="canvas",
        theme="light",
        options=None,
        **kwargs
    ):
        # Build radar axes
        radar_config = {
            "indicator": [{"name": dim} for dim in dimensions],
            "splitNumber": 4,
            "name": {"textStyle": {"color": "#666"}},
            "splitLine": {"lineStyle": {"color": ["#eee", "#ddd", "#ccc", "#bbb", "#aaa"]}},
            "splitArea": {"areaStyle": {"color": ["rgba(0,0,0,0.01)", "rgba(0,0,0,0.02)"]}},
        }

        # Build series from series_data dict
        series = []
        for series_name, values in series_data.items():
            series.append({
                "name": str(series_name),
                "value": values,
                "areaStyle": {"opacity": 0.3},
                "animationDuration": 1000,
                "animationEasing": "cubicOut",
            })

        base_options = {
            "radar": radar_config,
            "series": [{"type": "radar", "data": series}],
            "tooltip": {
                "trigger": "item",
                "borderWidth": 0,
                "padding": [14, 18],
                "shadowBlur": 10,
                "shadowColor": "rgba(0, 0, 0, 0.12)",
                "extraCssText": "border-radius: 12px;",
            },
            "legend": {
                "bottom": 20,
                "type": "scroll",
                "icon": "circle",
                "textStyle": {"fontSize": 13},
            },
        }

        if title is not None:
            base_options["title"] = {
                "text": title,
                "left": "center",
                "top": 24,
                "textStyle": {"fontSize": 22, "fontWeight": 600},
            }

        if colors is not None:
            base_options["color"] = colors

        if options:
            _deep_update(base_options, options)

        super().__init__(
            options=base_options,
            width=width,
            height=height,
            renderer=renderer,
            theme=theme,
            **kwargs
        )