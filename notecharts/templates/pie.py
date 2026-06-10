from typing import Union, List, Dict, Any
from ..chart import Chart
from ..palette import PaletteName, Palette
from .utils import PaletteOptions, _extract_column, _deep_update
from ..option import Option

class Pie(Chart):
    """Pre-built modern Pie Chart with neon glows and solid legend indicators.

    Creates a 2D pie chart from separate names and data values, or from a dataframe.
    Automatically splits complex palettes into color-offset variations to maintain 
    consistent multi-layered radial linear gradients and glows.

    Args:
        data (dict or str): Mapping of names to data values, e.g. {"A": 10000, "B": 6700}.
                           If dataframe is provided, pass the column name for values.
        names (list or str, optional): If dataframe is provided, pass the column name containing labels.
                                       Otherwise, defaults to None (keys extracted from data dict).
        title (str, optional): Chart title. Defaults to None.
        palette (str, PaletteName, PaletteOptions dict, or list of colors, optional):
            Color palette specification. Can be:
            
            - A palette name string (e.g., "Plasma", "Cube1") to generate colors automatically.
            - A PaletteOptions dict with 'palette' key plus optional parameters (format, value,
              saturation, alpha, shuffle) for advanced color generation.
            - A list of color strings for direct color specification.
            
            Defaults to None (uses default colors).
        width (str, optional): CSS width. Defaults to "99%".
        height (str, optional): CSS height. Defaults to "500px".
        renderer (str, optional): 'canvas' or 'svg'. Defaults to "canvas".
        theme (str, optional): 'light' or 'dark'. Defaults to "light".
        options (dict, optional): ECharts options to merge/override.
        dataframe (optional): A pandas DataFrame to extract names and values from.
        font (str, optional): Font family to use for the chart. Defaults to None.
        **kwargs: Forwarded to the base Chart class.
    """

    def __init__(
        self,
        data: Union[Dict[str, Any], str, List[Any]],
        names: Union[List[str], str, None] = None,
        title: str = None,
        palette: Union[PaletteName, str, PaletteOptions, List[str], None] = None,
        width: str = "99%",
        height: str = "500px",
        renderer: str = "canvas",
        theme: str = "light",
        options: Option = None,
        dataframe: Any = None,
        font: str = None,
        **kwargs
    ):
        # 1. Parse Dataframe sources if passed matching package helper paradigms
        if dataframe is not None and hasattr(dataframe, 'columns') and hasattr(dataframe, '__getitem__'):
            values_list = _extract_column(dataframe, data)
            names_list = _extract_column(dataframe, names) if names else [f"Item {i}" for i in range(len(values_list))]
            raw_pairs = [{"name": str(n), "value": v} for n, v in zip(names_list, values_list)]
        else:
            if isinstance(data, dict):
                raw_pairs = [{"name": str(k), "value": v} for k, v in data.items()]
            else:
                # Fallback to separate zip lists if dict structure wasn't used natively
                labels = names if names else [f"Item {i}" for i in range(len(data))]
                raw_pairs = [{"name": str(n), "value": v} for n, v in zip(labels, data)]

        n_slices = len(raw_pairs)

        # 2. Extract Palette rules mirroring package requirements
        palette_name = "Plasma"  # Match default package standard choice
        palette_kwargs = {}
        
        if palette is not None:
            if isinstance(palette, dict):
                palette_kwargs = palette.copy()
                palette_name = palette_kwargs.pop("palette")
            elif isinstance(palette, str):
                palette_name = palette
            elif isinstance(palette, list):
                palette_name = None
                color_1 = palette
                # Generate variations manually if string hex arrays are bound directly
                color_2 = palette
                glow_col = palette

        # Build structural offset layers securely from notecharts Palettes
        if palette_name is not None:
            c1_kwargs = {"value": "+0.3", **palette_kwargs} if palette_kwargs else {"value": "+0.7"}
            c2_kwargs = {"value": "-0.3", "saturation": "-0.1", **palette_kwargs} if palette_kwargs else {"value": "-0.1", "saturation": "-0.1"}
            glow_kwargs = {"value": "-0.2", "alpha": 0.8, **palette_kwargs} if palette_kwargs else {"value": "-0.2", "alpha": 0.8}
            
            color_1 = Palette(palette_name, n_slices, **c1_kwargs)
            color_2 = Palette(palette_name, n_slices, **c2_kwargs)
            glow_col = Palette(palette_name, n_slices, **glow_kwargs)

        # 3. Assemble structural arrays
        pie_data = []
        legend_data = []

        for i, item in enumerate(raw_pairs):
            pie_opts = {
                "name": item["name"],
                "value": item["value"],
                "itemStyle": {
                    "borderRadius": 10,
                    "color": {
                        "type": "linear",
                        "x": 0,
                        "y": 0,
                        "x2": 1,
                        "y2": 1,
                        "colorStops": [
                            {"offset": 0, "color": color_1[i % len(color_1)]},
                            {"offset": 1, "color": color_2[i % len(color_2)]}
                        ]
                    }
                },
                "labelLine": {
                    "lineStyle": {
                        "width": 2,
                        "color": color_1[i % len(color_1)]
                    }
                }
            }
            
            if theme == "dark":
                pie_opts["itemStyle"].update({"shadowBlur": 25, "shadowColor": glow_col[i % len(glow_col)]})

            pie_data.append(pie_opts)
            
            legend_data.append({
                "name": item["name"],
                "itemStyle": {
                    "color": color_1[i % len(color_1)]
                }
            })

        # 4. Standard Base configuration settings
        base_options = {
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
                    "saveAsImage": {
                        "name": title if title else "PieChart",
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
        if title is not None:
            base_options["title"] = {
                "text": title,
                "left": "center",
                "top": 24,
                "textStyle": {"fontSize": 22, "fontWeight": 600},
            }

        if title is None:
            base_options["series"][0]["center"] = ["50%", "45%"]

        if font is not None:
            base_options["textStyle"] = {"fontFamily": font}

        # Recursive deep dictionary overrides for structural changes
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