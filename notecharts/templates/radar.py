from typing import Union, List, Dict, Any
from ..chart import Chart
from ..palette import PaletteName, Palette
from .utils import PaletteOptions, _apply_styling
from ..option import Option

class Radar(Chart):
    """Pre-built modern Radar Chart with subtle linear gradients and rounded tooltips.

    Args:
        data (dict, list of dicts, or DataFrame, optional): Dataset containing keys/columns 
            for indicators and data series values.
        indicators (list of dicts or list of str, optional): Radar dimensions, e.g.,
            [{"name": "A", "max": 100}, {"name": "B", "max": 150}] or just names if auto-scaled.
        metrics (list of str, optional): If passing a DataFrame, these are the columns
            to use as axes for the radar indicators.
        series_names (list of str, optional): Custom names for each mapped data series line.
        title (str, optional): Chart title. Defaults to None.
        palette (str, PaletteName, PaletteOptions dict, or list, optional):
            Color palette specification parsed through the Palette generator layer.
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
        data: Any = None,
        indicators: Union[List[Dict[str, Any]], List[str], None] = None,
        metrics: List[str] = None,
        series_names: List[str] = None,
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
        # 1. Standardize and Extract Multi-Series Radar Input Arrays
        parsed_series = []  # List of tuples: (series_name, value_list)
        resolved_indicators = []

        # Handle DataFrames (using duck typing for compatibility with any DataFrame-like object)
        if hasattr(data, 'columns') and hasattr(data, '__getitem__'):
            target_metrics = metrics if metrics else [col for col in data.columns if col != data.columns[0]]
            
            # Determine indicators from metrics
            if indicators and isinstance(indicators[0], dict):
                resolved_indicators = indicators
            else:
                for m in target_metrics:
                    max_val = float(data[m].max()) * 1.1 if not data[m].empty else 100
                    resolved_indicators.append({"name": m, "max": round(max_val) if max_val > 0 else 100})

            # Check if rows or columns represent distinct target series lines
            if series_names:
                for i, name in enumerate(series_names):
                    if i < len(data):
                        row_vals = [data.at[i, m] for m in target_metrics]
                        parsed_series.append((str(name), row_vals))
            else:
                # Default fallback fallback to indexing
                for idx, row in data.iterrows():
                    name = str(row.iloc[0]) if len(data.columns) > len(target_metrics) else f"Series {idx + 1}"
                    row_vals = [row[m] for m in target_metrics]
                    parsed_series.append((name, row_vals))

        # Handle dictionaries or native structures
        elif isinstance(data, dict):
            # Format: {"Primary Weights": [4600, 13000, ...], "Secondary Weights": [...]}
            for name, vals in data.items():
                parsed_series.append((str(name), vals))
            resolved_indicators = indicators if indicators else []
            
        else:
            # Fallback to direct series arrays passing
            if isinstance(data, list) and len(data) > 0 and isinstance(data[0], tuple):
                parsed_series = data
            elif data is not None:
                name = series_names[0] if series_names else "Data Series"
                parsed_series = [(name, data)]
            resolved_indicators = indicators if indicators else []

        # Normalize simple list-of-string indicators
        if resolved_indicators and isinstance(resolved_indicators[0], str):
            resolved_indicators = [{"name": ind, "max": 100} for ind in resolved_indicators]

        n_series = len(parsed_series)
        legend_names = [item[0] for item in parsed_series]

        # 2. Resolve Color Gradients and Alpha Variations via Palette Layer
        if palette is None:
            color_base = color_transparent = None
        else:
            if isinstance(palette, dict):
                pk = palette.copy()
                pal = pk.pop("palette")
            else:
                pal = palette
                pk = {}

            color_base = Palette(pal, n_series, **pk)
            color_transparent = Palette(pal, n_series, alpha=0, value="-0.5", **pk)

        # 3. Assemble Core Series Configurations
        series_list = []
        for i, (name, values) in enumerate(parsed_series):
            series_entry = {
                "name": name,
                "type": "radar",
                "symbol": "circle",
                "symbolSize": 10,
                "data": [
                    {
                        "value": values,
                        "name": name
                    }
                ],
                # "emphasis": {
                #     "lineStyle": {
                #         "width": 3
                #     }
                # }
            }

            # Inject procedural styling if a dynamic palette is present
            if color_base is not None:
                base_c = color_base[i % len(color_base)]
                trans_c = color_transparent[i % len(color_transparent)]
                
                series_entry["itemStyle"] = {"color": base_c, "shadowBlur": 10, "shadowColor": base_c}
                series_entry["lineStyle"] = {"color": base_c, "width": 2}
                series_entry["areaStyle"] = {
                    "opacity": 0.8,
                    "color": {
                        "type": "linear",
                        "x": 0, "y": 0, "x2": 1, "y2": 1,
                        "colorStops": [
                            {"offset": 0, "color": base_c},
                            {"offset": 1, "color": trans_c}
                        ]
                    }
                }
            series_list.append(series_entry)

        # 4. Standardized Base Options Framework
        base_options: Option = {
            "tooltip": {
                "trigger": "item",
                "borderWidth": 0,
                "padding": [14, 18],
                "shadowBlur": 10,
                "shadowColor": "rgba(0, 0, 0, 0.12)",
                "extraCssText": "border-radius: 12px;",
            },
            "legend": {
                "data": legend_names,
                "bottom": 20,
                "type": "scroll",
                "icon": "circle",
                "itemGap": 25,
                "itemWidth": 20,
                "textStyle": {"fontSize": 13}
            },
            "radar": {
                "radius": "60%",
                "center": ["50%", "55%"],
                "startAngle": 90,
                "triggerEvent": True,
                "shape": "polygon",
                "indicator": resolved_indicators
            },
            "animationEasing": "quinticOut",
            "animationDuration": 900,
            "series": series_list
        }

        # 5. Overrides, Layout Adjustments, and Structural Title Interpolations
        _apply_styling(base_options, title=title, font=font, options=options)

        # Reposition title configurations seamlessly to match target layout blueprint
        if "title" in base_options:
            if title:  # Keep specific styling defaults intact unless handled natively
                base_options["title"].update({
                    "top": 24,
                    "left": "center"
                })
                if "textStyle" in base_options["title"]:
                    base_options["title"]["textStyle"].update({"fontSize": 22, "fontWeight": 400})

        super().__init__(
            options=base_options,
            width=width,
            height=height,
            renderer=renderer,
            theme=theme,
            **kwargs
        )