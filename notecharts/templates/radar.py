from typing import Union, List
from ..widget import Chart
from ..palette import PaletteName, Palette
from .utils import PaletteOptions, _extract_columns_dict, _deep_update

class Radar(Chart):
    """Pre-built modern Radar Chart.

    Radar charts are ideal for displaying multivariate data on a 2D chart.
    Each series represents a different entity with values across multiple dimensions.

    Args:
        series_data (dict): Mapping of series names to lists of values.
                            e.g. {"Player A": [80, 90, 70], "Player B": [85, 80, 95]}
                            If dataframe is provided, map series names to column names.
        dimensions (list[str]): Names of the radar axes. e.g. ["Speed", "Power", "Agility"]
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
        dataframe (optional): A pandas DataFrame to extract series_data from.
        font (str, optional): Font family to use for the chart. Defaults to None.
        **kwargs: Forwarded to the base Chart class.
    """

    def __init__(
        self,
        series_data,
        dimensions,
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
            series_data = _extract_columns_dict(dataframe, series_data)
        
        n_series = len(series_data) if isinstance(series_data, dict) else 1

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

        if font is not None:
            base_options["textStyle"] = {"fontFamily": font}

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