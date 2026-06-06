from typing import Union, List
from ..chart import Chart
from ..palette import PaletteName, Palette
from .utils import PaletteOptions, _extract_column, _extract_columns_dict, _deep_update

class Bar(Chart):
    """Pre-built modern Bar Chart.

    Creates a 2D bar chart from x-axis categories and one or more y-series.
    Automatically determines n_colors based on the number of series.

    Args:
        x (list or str): X-axis categories (labels), or column name if dataframe is provided.
        y (dict): Mapping of series names to data lists, e.g. {"Sales": [10, 20, 30]}.
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
        # Extract columns from dataframe if provided
        if dataframe is not None and hasattr(dataframe, 'columns') and hasattr(dataframe, '__getitem__'):
            x = _extract_column(dataframe, x)
            y = _extract_columns_dict(dataframe, y)
        
        n_series = len(y) if isinstance(y, dict) else 1

        # Build series array from y dict
        series = []
        for series_name, data in (y.items() if isinstance(y, dict) else [(None, y)]):
            series.append({
                "type": "bar",
                "name": str(series_name) if series_name else "value",
                "data": data,
                "itemStyle": {
                    "borderRadius": [4, 4, 0, 0],
                },
                "animationDuration": 1000,
                "animationEasing": "cubicOut",
            })

        # Generate colors from palette parameter
        colors = None
        if palette is not None:
            if isinstance(palette, dict):
                # dict mode: extract palette name and pass other params to Palette()
                palette_dict = palette.copy()
                palette_name = palette_dict.pop("palette")
                colors = Palette(palette_name, n_series, **palette_dict)
            elif isinstance(palette, str):
                # str mode: palette name string
                colors = Palette(palette, n_series)
            elif isinstance(palette, list):
                # list mode: direct color specification
                colors = palette

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
                "axisLabel": {"fontSize": 12, "margin": 15},
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
                    "magicType": {
                        "type": ["line", "stack"],
                        "option": {
                            "line":{
                                "symbolSize": 10,
                                "lineStyle": {"width": 3},
                            }
                        }
                    },
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

        if title is not None:
            base_options["title"] = {
                "text": title,
                "left": "center",
                "top": 24,
                "textStyle": {"fontSize": 22, "fontWeight": 600},
            }

        if colors is not None:
            base_options["color"] = colors

        if font is not None:
            base_options["textStyle"] = {"fontFamily": font}

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

