from typing import Union, List
from ..chart import Chart
from ..palette import PaletteName, Palette
from .utils import PaletteOptions, _extract_column, _extract_columns_dict, _apply_styling

class Line(Chart):
    """Pre-built modern Line Chart.

    Creates a line chart with optional area fill and smooth interpolation.
    Automatically determines n_colors based on the number of series.

    Args:
        x (list or str): X-axis categories (labels), or column name if dataframe is provided.
        y (dict): Mapping of series names to data lists.
                  If dataframe is provided, map series names to column names.
        title (str, optional): Chart title. Defaults to None.
        palette (str, PaletteName, PaletteOptions dict, or list of colors, optional):
            Color palette specification. Can be:
            
            - A palette name string (e.g., "Viridis", "Set2") to generate colors automatically.
            - A PaletteOptions dict with 'palette' key plus optional parameters (format, value,
              saturation, alpha, shuffle) for advanced color generation.
            - A list of color strings for direct color specification.
            
            Defaults to None (uses default colors).
        width (str, optional): CSS width. Defaults to "99%".
        height (str, optional): CSS height. Defaults to "500px".
        renderer (str, optional): 'canvas' or 'svg'. Defaults to "canvas".
        theme (str, optional): 'light' or 'dark'. Defaults to "light".
        options (dict, optional): ECharts options to merge/override.
        dataframe (optional): A pandas DataFrame to extract x and y from.
        font (str, optional): Font family to use for the chart. Defaults to None.
        **kwargs: Forwarded to the base Chart class.
    """

    def __init__(
        self,
        x,
        y,
        title=None,
        palette: Union[PaletteName, str, PaletteOptions, List[str], None] = None,
        width="99%",
        height="500px",
        renderer="canvas",
        theme="light",
        options=None,
        dataframe=None,
        font=None,
        **kwargs
    ):
        n_series = len(y) if isinstance(y, dict) else 1

        # Generate colors from palette parameter
        colors = None
        grad_top = None
        grad_bottom = None
        if palette is not None:
            if isinstance(palette, dict):
                palette_dict = palette.copy()
                palette_name = palette_dict.pop("palette")
                colors = Palette(palette_name, n_series, **palette_dict)
                grad_top = Palette(palette_name, n_series, alpha=max(palette_dict.get("alpha", 1) - 0.7, 0))
                grad_bottom = Palette(palette_name, n_series, alpha=0.0)

            elif isinstance(palette, str):
                colors = Palette(palette, n_series)
                grad_top = Palette(palette, n_series, alpha=0.7)
                grad_bottom = Palette(palette, n_series, alpha=0.0)

            elif isinstance(palette, list):
                colors = Palette(palette, n_series)
                grad_top = Palette(palette, n_series, alpha=0.7)
                grad_bottom = Palette(palette, n_series, alpha=0.0)

        # Extract columns from dataframe if provided
        if dataframe is not None and hasattr(dataframe, 'columns') and hasattr(dataframe, '__getitem__'):
            x = _extract_column(dataframe, x)
            y = _extract_columns_dict(dataframe, y)
        

        # Build series array from y dict
        series = []
        for i, (series_name, data) in enumerate(y.items() if isinstance(y, dict) else [(None, y)]):
            ser = {
                "type": "line",
                "name": str(series_name) if series_name else "value",
                "data": data,
                "smooth": True,
                "symbol": "circle",
                "symbolSize": 8,
                "lineStyle": {"width": 3},
                "animationDuration": 1000,
                "animationEasing": "cubicOut",
            }

            if grad_top is not None:
                ser["areaStyle"] = {
                    "color": {
                        "type": "linear",
                        "x": 0, "y": 0, "x2": 0, "y2": 1,
                        "colorStops": [
                            {"offset": 0, "color": grad_top[i]},
                            {"offset": 1, "color": grad_bottom[i]}
                        ]
                    },
                    "opacity": 0.0 if theme=='light' else 0.5
                }

            series.append(ser)

        base_options = {
            "xAxis": {
                "type": "category",
                "data": x,
                "axisLine": {"show": False},
                "axisTick": {"show": False},
                "axisLabel": {"fontSize": 12, "margin": 15},
            },
            "yAxis": {
                "type": "value",
                "splitLine": {"lineStyle": {"type": "dashed"}},
                "axisLabel": {"fontSize": 12, "margin": 15},
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
            "dataZoom": {"type": "inside"},
            "legend": {
                "bottom": 20,
                "type": "scroll",
                "icon": "circle",
                "textStyle": {"fontSize": 13},
                "itemGap": 35,
                "itemWidth": 20
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

        _apply_styling(base_options, title=title, colors=colors, font=font, options=options)

        super().__init__(
            options=base_options,
            width=width,
            height=height,
            renderer=renderer,
            theme=theme,
            **kwargs
        )