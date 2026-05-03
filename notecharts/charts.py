import random
import colorsys
from .widget import Chart, JSCode

def _format_data(data):
    """Formats the input data for ECharts.

    Args:
        data (list-of-lists, list-of-dicts, or DataFrame): The input data.

    Returns:
        list: The formatted data.
    """
    if hasattr(data, "to_dict") and hasattr(data, "columns"):
        return data.to_dict(orient="records")
    return data

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

def _get_harmony_hues(base_hue, harmony):
    """Returns a list of hue angles for the given harmony scheme.

    Args:
        base_hue (float): Base hue angle (0-360).
        harmony (str): Harmony scheme Name. One of 'monochromatic', 'complementary',
            'triadic', 'tetradic', 'split-complementary', or 'analogous'.

    Returns:
        list[float]: List of hue angles.
    """
    base = base_hue % 360
    if harmony == "monochromatic":
        return [base]
    elif harmony == "complementary":
        return [base, (base + 180) % 360]
    elif harmony == "triadic":
        return [base, (base + 120) % 360, (base + 240) % 360]
    elif harmony == "tetradic":
        return [base, (base + 90) % 360, (base + 180) % 360, (base + 270) % 360]
    elif harmony == "split-complementary":
        return [base, (base + 150) % 360, (base + 210) % 360]
    elif harmony == "analogous":
        return [(base - 30) % 360, base, (base + 30) % 360]
    else:
        return [base]

def _hsv_palette(n_colors, color_theme="pastel", base_hue=None, chart_theme="light", harmony="auto"):
    """Generates a cohesive HEX color palette based on HSV values and harmonies.

    Args:
        n_colors (int): Number of colors to generate.
        color_theme (str, optional): Preset saturation/value ('pastel', 'neon', 'professional').
            Defaults to "pastel".
        base_hue (float, optional): Seed hue (0-360). Defaults to None.
        chart_theme (str, optional): 'light' or 'dark' background context. Defaults to "light".
        harmony (str, optional): Color harmony scheme or 'auto'. Defaults to "auto".

    Returns:
        list[str]: List of HEX color strings.

    Raises:
        ValueError: If color_theme is unknown.
    """
    if n_colors <= 0:
        return []

    if chart_theme == "dark":
        presets = {
            "pastel":       (0.25, 0.90),
            "neon":         (0.80, 0.95),
            "professional": (0.45, 0.80),
        }
    else:
        presets = {
            "pastel":       (0.40, 0.80),
            "neon":         (0.75, 1.00),
            "professional": (0.50, 0.75),
        }
    if color_theme not in presets:
        raise ValueError(f"Unknown color_theme '{color_theme}'. Choose from {list(presets.keys())}.")
    sat, val = presets[color_theme]

    if base_hue is None:
        random.seed(42)
        base_hue = random.random() * 360

    # Auto-select harmony based on number of colors
    if harmony == "auto":
        if n_colors == 1:
            harmony = "monochromatic"
        elif n_colors == 2:
            harmony = "complementary"
        elif n_colors == 3:
            harmony = "triadic"
        elif n_colors == 4:
            harmony = "tetradic"
        elif n_colors == 5:
            harmony = "split-complementary"
        else:
            harmony = "tetradic"

    base_hues = _get_harmony_hues(base_hue, harmony)
    colors = []
    for i in range(n_colors):
        if i < len(base_hues):
            hue = base_hues[i]
            s = sat
            v = val
        else:
            # Generate variants by cycling through base hues and subtly altering sat/val
            cycle = (i - len(base_hues)) // len(base_hues)
            idx = (i - len(base_hues)) % len(base_hues)
            hue = base_hues[idx]
            # Alternate between slightly desaturated/lighter and slightly darkened
            if cycle % 2 == 0:
                s = sat * 0.85
                v = min(1.0, val * 1.15)
            else:
                s = sat * 1.0
                v = max(0.0, val * 0.85)
        rgb = colorsys.hsv_to_rgb(hue / 360.0, s, v)
        hex_color = "#{:02x}{:02x}{:02x}".format(
            int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)
        )
        colors.append(hex_color)
    return colors

class Bar(Chart):
    """Pre-built modern Bar Chart.

    Notecharts' Bar integration handles automatic layout, tooltips, and themes.
    """

    def __init__(
        self,
        data,
        x,
        y,
        title=None,
        width="99%",
        height="500px",
        renderer="canvas",
        theme="light",
        custom_options=None,
        user_colors=None,
        **kwargs
    ):
        """Initializes a Bar Chart.

        Args:
            data (list-of-lists, list-of-dicts, or DataFrame): The source data.
            x (str): Column name for the x-axis.
            y (str or list[str]): Column name(s) for the y-axis.
            title (str, optional): Chart title. Defaults to None.
            width (str, optional): CSS width. Defaults to "99%".
            height (str, optional): CSS height. Defaults to "500px".
            renderer (str, optional): 'canvas' or 'svg'. Defaults to "canvas".
            theme (str, optional): 'light' or 'dark'. Defaults to "light".
            custom_options (dict, optional): Extra options to merge into the ECharts dict.
            user_colors (list[str], optional): List of hex colors. Defaults to None.
            **kwargs: Forwarded to the base Chart class.
        """
        formatted_data = _format_data(data)
        y_cols = y if isinstance(y, list) else [y]

        series = []
        for y_col in y_cols:
            series.append({
                "type": "bar",
                "encode": {"x": x, "y": y_col},
                "name": str(y_col),
                "itemStyle": {
                    "borderRadius": [6, 6, 0, 0],
                },
                "animationDuration": 1200,
                "animationEasing": "cubicOut",
            })

        # Use user-provided colors if given, else auto-generate harmonious palette
        if user_colors is not None:
            palette = user_colors
        else:
            palette = _hsv_palette(len(y_cols), color_theme="neon", chart_theme=theme, harmony="auto")

        options = {
            "color": palette,
            "title": {
                "text": title,
                "left": "center",
                "top": 24,
                "textStyle": {
                    "fontSize": 22,
                    "fontWeight": 600,
                },
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
                "extraCssText": "border-radius: 12px;"
            },
            "toolbox": {
                "feature": {
                    "restore": {},
                    "magicType": {
                        "type": ["line", "stack"]
                    },
                    "saveAsImage": {
                        "name": title if title else "Chart"
                    }
                }
            },
            "dataZoom": {
                "type": JSCode("'inside'")
            },
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
            "xAxis": {
                "type": "category",
                "axisLine": {"show": False},
                "axisTick": {"show": False},
                "axisLabel": {"fontSize": 12},
            },
            "yAxis": {
                "type": "value",
                "splitLine": {
                    "lineStyle": {
                        "type": "dashed",
                    }
                },
                "axisLabel": {"fontSize": 12},
            },
            "dataset": {"source": formatted_data},
            "series": series,
        }

        if title is None:
            del options["title"]

        if custom_options:
            _deep_update(options, custom_options)

        super().__init__(
            options=options,
            width=width,
            height=height,
            renderer=renderer,
            theme=theme,
            **kwargs
        )

class Line(Chart):
    """Pre-built modern Line Chart.

    Supports smooth lines, area fill, and automatic color palettes.
    """

    def __init__(
        self,
        data,
        x,
        y,
        title=None,
        area=True,
        smooth=True,
        width="99%",
        height="500px",
        renderer="canvas",
        theme="light",
        custom_options=None,
        user_colors=None,
        **kwargs
    ):
        """Initializes a Line Chart.

        Args:
            data (list-of-lists, list-of-dicts, or DataFrame): The source data.
            x (str): Column name for the x-axis.
            y (str or list[str]): Column name(s) for the y-axis.
            title (str, optional): Chart title. Defaults to None.
            area (bool, optional): Whether to show area fill. Defaults to True.
            smooth (bool, optional): Whether to smooth the line. Defaults to True.
            width (str, optional): CSS width. Defaults to "99%".
            height (str, optional): CSS height. Defaults to "500px".
            renderer (str, optional): 'canvas' or 'svg'. Defaults to "canvas".
            theme (str, optional): 'light' or 'dark'. Defaults to "light".
            custom_options (dict, optional): Extra options to merge into the ECharts dict.
            user_colors (list[str], optional): List of hex colors. Defaults to None.
            **kwargs: Forwarded to the base Chart class.
        """
        formatted_data = _format_data(data)
        y_cols = y if isinstance(y, list) else [y]

        if user_colors is not None:
            palette = user_colors
        else:
            palette = _hsv_palette(len(y_cols), color_theme="neon", chart_theme=theme, harmony="auto")

        series = []
        for i, y_col in enumerate(y_cols):
            color = palette[i % len(palette)]
            ser = {
                "type": "line",
                "encode": {"x": x, "y": y_col},
                "name": str(y_col),
                "smooth": smooth,
                "symbol": "circle",
                "symbolSize": 8,
                "lineStyle": {"width": 3},
                "animationDuration": 1000,
                "animationEasing": "cubicOut",
            }
            if area:
                ser["areaStyle"] = {
                    "color": {
                        "type": "linear",
                        "x": 0, "y": 0, "x2": 0, "y2": 1,
                        "colorStops": [
                            {"offset": 0, "color": f"{color}40"},
                            {"offset": 1, "color": f"{color}00"}
                        ]
                    }
                }
            series.append(ser)

        options = {
            "color": palette,
            "title": {
                "text": title,
                "left": "center",
                "top": 24,
                "textStyle": {"fontSize": 22, "fontWeight": 600},
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
                    "saveAsImage": {
                        "name": title if title else "Chart",
                        "pixelRatio": 3
                    },
                    "dataZoom": {}
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
            "xAxis": {
                "type": "category",
                "axisLine": {"show": False},
                "axisTick": {"show": False},
                "axisLabel": {"fontSize": 12},
            },
            "yAxis": {
                "type": "value",
                "splitLine": {"lineStyle": {"type": "dashed"}},
                "axisLabel": {"fontSize": 12},
            },
            "dataset": {"source": formatted_data},
            "series": series,
        }

        if title is None:
            del options["title"]

        if custom_options:
            _deep_update(options, custom_options)

        super().__init__(
            options=options,
            width=width,
            height=height,
            renderer=renderer,
            theme=theme,
            **kwargs
        )

class Scatter(Chart):
    """Pre-built modern Scatter Plot.
    
    Optimized for high-density visualizations with clear tooltips.
    """

    def __init__(
        self,
        data,
        x,
        y,
        title=None,
        name_col=None,
        width="99%",
        height="500px",
        renderer="canvas",
        theme="light",
        custom_options=None,
        user_colors=None,
        **kwargs
    ):
        """Initializes a Scatter Plot.

        Args:
            data (list-of-lists, list-of-dicts, or DataFrame): The source data.
            x (str): Column name for the x-axis.
            y (str or list[str]): Column name(s) for the y-axis.
            title (str, optional): Chart title. Defaults to None.
            name_col (str, optional): Column name for series names. Defaults to None.
            width (str, optional): CSS width. Defaults to "99%".
            height (str, optional): CSS height. Defaults to "500px".
            renderer (str, optional): 'canvas' or 'svg'. Defaults to "canvas".
            theme (str, optional): 'light' or 'dark'. Defaults to "light".
            custom_options (dict, optional): Extra options to merge into the ECharts dict.
            user_colors (list[str], optional): List of hex colors. Defaults to None.
            **kwargs: Forwarded to the base Chart class.
        """
        formatted_data = _format_data(data)
        y_cols = y if isinstance(y, list) else [y]

        series = []
        for y_col in y_cols:
            series.append({
                "type": "scatter",
                "encode": {"x": x, "y": y_col},
                "name": str(y_col),
                "symbolSize": 14,
                "animationDuration": 1000,
                "animationEasing": "cubicOut",
            })

        if user_colors is not None:
            palette = user_colors
        else:
            palette = _hsv_palette(len(y_cols), color_theme="neon", chart_theme=theme, harmony="auto")

        options = {
            "color": palette,
            "title": {
                "text": title,
                "left": "center",
                "top": 24,
                "textStyle": {"fontSize": 22, "fontWeight": 600},
            },
            "tooltip": {
                "trigger": "item",
                "borderWidth": 0,
                "padding": [14, 18],
                "shadowBlur": 10,
                "shadowColor": "rgba(0, 0, 0, 0.12)",
                "extraCssText": "border-radius: 12px;",
                "formatter": JSCode(
                    f"""function(params) {{
                        var row = params.data;
                        var lines = [];
                        var nameVal = '{name_col}' ? row['{name_col}'] : null;
                        if (nameVal !== undefined && nameVal !== null) {{
                            lines.push('<strong>' + nameVal + '</strong>');
                        }}
                        var val, display;
                        for (var key in row) {{
                            if (row.hasOwnProperty(key) && key !== '{name_col}') {{
                                val = row[key];
                                display = (typeof val === 'number') ? val.toFixed(3) : val;
                                lines.push(key + ': ' + display);
                            }}
                        }}
                        return lines.join('<br/>');
                    }}"""
                )
            },
            "toolbox": {
                "feature": {
                    "restore": {},
                    "saveAsImage": {
                        "name": title if title else "Chart",
                        "pixelRatio": 3
                    },
                    "dataZoom": {}
                }
            },
            "dataZoom": {
                "type": JSCode("'inside'")
            },
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
            "xAxis": {
                "type": "value",
                "splitLine": {"lineStyle": {"type": "dashed"}},
                "axisLabel": {"fontSize": 12},
            },
            "yAxis": {
                "type": "value",
                "splitLine": {"lineStyle": {"type": "dashed"}},
                "axisLabel": {"fontSize": 12},
            },
            "dataset": {"source": formatted_data},
            "series": series,
        }

        if title is None:
            del options["title"]

        if custom_options:
            _deep_update(options, custom_options)

        super().__init__(
            options=options,
            width=width,
            height=height,
            renderer=renderer,
            theme=theme,
            **kwargs
        )

class Radar(Chart):
    """Pre-built modern Radar Chart.

    Radar charts are ideal for displaying multivariate data on a 2D chart.
    """

    def __init__(
        self,
        data,
        name_col,
        dimensions,
        title=None,
        width="99%",
        height="500px",
        renderer="canvas",
        theme="light",
        custom_options=None,
        user_colors=None,
        **kwargs
    ):
        """Initializes a Radar Chart.

        Args:
            data (list-of-lists, list-of-dicts, or DataFrame): The source data.
            name_col (str): Column that identifies each series (e.g., 'player').
            dimensions (list[str]): Column names for the radar axes (e.g., ['speed', 'power']).
            title (str, optional): Chart title. Defaults to None.
            width (str, optional): CSS width. Defaults to "99%".
            height (str, optional): CSS height. Defaults to "500px".
            renderer (str, optional): 'canvas' or 'svg'. Defaults to "canvas".
            theme (str, optional): 'light' or 'dark'. Defaults to "light".
            custom_options (dict, optional): Extra options to merge into the ECharts dict.
            user_colors (list[str], optional): List of hex colors. Defaults to None.
            **kwargs: Forwarded to the base Chart class.
        """
        formatted_data = _format_data(data)

        # Group data by series name
        series_map = {}
        for row in formatted_data:
            name = row[name_col]
            series_map.setdefault(name, []).append(row)

        # Compute max per dimension for indicator range
        dim_max = {d: 0 for d in dimensions}
        for row in formatted_data:
            for d in dimensions:
                if row[d] > dim_max[d]:
                    dim_max[d] = row[d]

        indicators = [{"name": d, "max": dim_max[d]} for d in dimensions]

        # Build series list
        series = []
        for idx, (name, rows) in enumerate(series_map.items()):
            row = rows[0]
            values = [row[d] for d in dimensions]
            series.append({
                "type": "radar",
                "data": [{"value": values, "name": str(name)}],
                "areaStyle": {"opacity": 0.2},
                "symbol": "circle",
                "symbolSize": 6,
                "lineStyle": {"width": 2},
            })

        if user_colors is not None:
            palette = user_colors
        else:
            palette = _hsv_palette(len(series), color_theme="neon", chart_theme=theme, harmony="auto")

        options = {
            "color": palette,
            "title": {
                "text": title,
                "left": "center",
                "top": 24,
                "textStyle": {"fontSize": 22, "fontWeight": 600},
            },
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
                    "saveAsImage": {
                        "name": title if title else "Chart",
                        "pixelRatio": 3
                    },
                }
            },
            "legend": {
                "bottom": 20,
                "type": "scroll",
                "icon": "circle",
                "textStyle": {"fontSize": 13},
            },
            "radar": {
                "indicator": indicators,
                "splitArea": {
                    "areaStyle": {
                        "color": ["rgba(0,0,0,0.02)", "rgba(0,0,0,0.04)"]
                    }
                },
                "axisLine": {"lineStyle": {"color": "rgba(0,0,0,0.1)"}},
                "splitLine": {"lineStyle": {"color": "rgba(0,0,0,0.1)"}},
            },
            "series": series,
        }

        if title is None:
            del options["title"]

        if custom_options:
            _deep_update(options, custom_options)

        super().__init__(
            options=options,
            width=width,
            height=height,
            renderer=renderer,
            theme=theme,
            **kwargs
        )