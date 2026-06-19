from typing import Union, List
from ..chart import Chart
from ..palette import PaletteName
from ..option import Option
from .utils import PaletteOptions, _resolve_palette, _apply_styling, _extract_column

class Scatter(Chart):
    """Pre-built modern Scatter Plot.

    Creates a 2D or 3D scatter plot depending on whether z is provided.
    Automatically determines n_colors based on the number of series.

    Args:
        x (list or str): X-axis data, or column name if dataframe is provided.
        y (list or str): Y-axis data, or column name if dataframe is provided.
        z (list or str, optional): Z-axis data for 3D scatter, or column name if dataframe is provided. Defaults to None.
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
        dataframe (optional): A pandas DataFrame to extract x, y, z from.
        font (str, optional): Font family to use for the chart. Defaults to None.
        **kwargs: Forwarded to the base Chart class.
    """

    def __init__(
        self,
        x,
        y,
        z=None,
        title=None,
        palette: Union[PaletteName, str, PaletteOptions, List[str], None] = None,
        width="99%",
        height="500px",
        renderer="canvas",
        theme="light",
        options:Option=None,
        dataframe=None,
        font=None,
        **kwargs
    ):
        # Extract columns from dataframe if provided
        if dataframe is not None and hasattr(dataframe, 'columns') and hasattr(dataframe, '__getitem__'):
            x = _extract_column(dataframe, x)
            y = _extract_column(dataframe, y)
            if z is not None:
                z = _extract_column(dataframe, z)
        
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

        colors = _resolve_palette(palette, 1)

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

        _apply_styling(base_options, title=title, colors=colors, font=font, options=options)

        super().__init__(
            options=base_options,
            width=width,
            height=height,
            renderer=renderer,
            theme=theme,
            **kwargs
        )