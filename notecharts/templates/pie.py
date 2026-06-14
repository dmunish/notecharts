from typing import Union, List, Dict, Any
from ..chart import Chart
from ..palette import PaletteName, Palette
from .utils import PaletteOptions, _extract_column, _apply_styling
from ..option import Option

class Pie(Chart):
    """Pre-built modern Pie Chart with neon glows and solid legend indicators.

    Creates a 2D pie chart from separate names and data values, or from a dataframe.
    Automatically splits complex palettes into color-offset variations to maintain 
    consistent multi-layered radial linear gradients and glows.

    Args:
        data (dict or DataFrame, optional): A dict of name-value pairs, or a DataFrame
            with columns for names and values. Defaults to None.
        name (list or str, optional): List of category names, or column name in the
            DataFrame containing labels. Defaults to None.
        value (list or str, optional): List of data values, or column name in the
            DataFrame containing values. Defaults to None.
        title (str, optional): Chart title. Defaults to None.
        palette (str, PaletteName, PaletteOptions dict, or list of colors, optional):
            Color palette specification. Can be:
            
            - A palette name string (e.g., "Plasma", "Cube1") to generate colors automatically.
            - A PaletteOptions dict with 'palette' key plus optional parameters (format, value,
              saturation, alpha, reverse) for advanced color generation.
            - A list of color strings for direct color specification.
            
            Defaults to None (uses default colors).
        width (str, optional): CSS width. Defaults to "99%".
        height (str, optional): CSS height. Defaults to "500px".
        renderer (str, optional): 'canvas' or 'svg'. Defaults to "canvas".
        theme (str, optional): 'light' or 'dark'. Defaults to "light".
        options (dict, optional): ECharts options to merge/override.
        font (str, optional): Font family to use for the chart. Defaults to None.
        **kwargs: Forwarded to the base Chart class.
    """

    def __init__(
        self,
        data: Union[Dict[str, Any], Any] = None,
        name: Union[List[str], str, None] = None,
        value: Union[List[Any], str, None] = None,
        title: str = None,
        palette: Union[PaletteName, str, PaletteOptions, List[str], None] = None,
        width: str = "99%",
        height: str = "500px",
        renderer: str = "canvas",
        theme: str = "light",
        options: Option = None,
        font: str = None,
        **kwargs
    ):
        # 1. Parse input: dict, DataFrame, or separate name+value lists
        if isinstance(data, dict):
            raw_pairs = [{"name": str(k), "value": v} for k, v in data.items()]
        elif hasattr(data, 'columns') and hasattr(data, '__getitem__'):
            values = _extract_column(data, value)
            labels = _extract_column(data, name) if name else [f"Item {i}" for i in range(len(values))]
            raw_pairs = [{"name": str(n), "value": v} for n, v in zip(labels, values)]
        else:
            labels = name if name else [f"Item {i}" for i in range(len(value))]
            raw_pairs = [{"name": str(n), "value": v} for n, v in zip(labels, value)]

        n_slices = len(raw_pairs)

        # 2. Resolve palette — generate 3 color variants for gradients and glows
        if palette is None:
            color_1 = color_2 = glow_col = None
        else:
            if isinstance(palette, dict):
                pk = palette.copy()
                pal = pk.pop("palette")
            else:
                pal = palette
                pk = {}
            
            if theme == "dark":
                color_1 = Palette(pal, n_slices, value="+0.3", **pk)
                color_2 = Palette(pal, n_slices, value="-0.3", saturation="-0.1", **pk)
                glow_col = Palette(pal, n_slices, value="-0.2", alpha=0.8, **pk)
            else:
                color_1 = Palette(pal, n_slices, value="+0.7", **pk)
                color_2 = Palette(pal, n_slices, saturation="-0.1", **pk)
                glow_col = Palette(pal, n_slices, value="-0.2", alpha=0.8, **pk)

        # 3. Assemble structural arrays
        pie_data = []
        legend_data = []

        for i, item in enumerate(raw_pairs):
            pie_opts = {
                "name": item["name"],
                "value": item["value"],
                "itemStyle": {"borderRadius": 10},
            }

            if color_1 is not None:
                pie_opts["itemStyle"]["color"] = {
                    "type": "linear",
                    "x": 0,
                    "y": 0,
                    "x2": 1,
                    "y2": 1,
                    "colorStops": [
                        {"offset": 0, "color": color_1[i % len(color_1)]},
                        {"offset": 1, "color": color_2[i % len(color_2)]},
                    ],
                }
                pie_opts["labelLine"] = {
                    "lineStyle": {"width": 2, "color": color_1[i % len(color_1)]}
                }

                if theme == "dark":
                    pie_opts["itemStyle"].update({"shadowBlur": 25, "shadowColor": glow_col[i % len(glow_col)]})

            pie_data.append(pie_opts)

            if color_1 is not None:
                legend_data.append({"name": item["name"], "itemStyle": {"color": color_1[i % len(color_1)]}})
            else:
                legend_data.append({"name": item["name"]})

        # 4. Standard Base configuration settings
        base_options: Option = {
            "tooltip": {
                "trigger": "item",
                "formatter": "{b} : {c} ({d}%)",
                "textStyle": {"fontSize": 14},
                "axisPointer": {"type": "shadow"},
                "borderWidth": 0,
                "padding": [14, 18],
                "shadowBlur": 10,
                "shadowColor": "rgba(0, 0, 0, 0.4)",
                "shadowOffsetX": 0,
                "shadowOffsetY": 4,
                "extraCssText": "border-radius: 12px;",
            },
            "legend": {
                "data": legend_data,
                "bottom": "5%",
                "icon": "circle",
                "itemGap": 20,
                "itemWidth": 20,
                "type": "scroll"
            },
            "toolbox": {
                "feature": {
                    "restore": {},
                    "saveAsImage": {
                        "name": title if title else "Chart",
                        "pixelRatio": 3
                    }
                }
            },
            "series": [
                {
                    "name": title if title else "Data Proportion",
                    "type": "pie",
                    "radius": "60%",
                    "data": pie_data,
                    "animationDuration": 1000,
                    "animationEasing": "cubicOut",
                }
            ]
        }

        # 5. Dynamic text parameters
        _apply_styling(base_options, title=title, font=font, options=options)

        if title is None:
            base_options["series"][0]["center"] = ["50%", "45%"]

        super().__init__(
            options=base_options,
            width=width,
            height=height,
            renderer=renderer,
            theme=theme,
            **kwargs
        )