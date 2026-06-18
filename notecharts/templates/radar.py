from typing import Union, List, Dict, Any, Optional
from ..chart import Chart, JSCode
from ..palette import PaletteName, Palette
from .utils import PaletteOptions, _apply_styling
from ..option import Option


class Radar(Chart):
    """Pre-built modern Radar Chart with subtle linear gradients and rounded tooltips.

    Args:
        data (dict or DataFrame): Series data. Dict format: {"Series A": [v1, v2, ...], ...}.
            DataFrame rows become series; use `series_col` to specify the label column.
        axes (list of str or list of dicts, optional): Radar spoke definitions. Pass a list of
            column/key names for auto-scaled axes, or dicts like {"name": "Speed", "max": 120}
            for explicit control. For DataFrames, inferred automatically by excluding
            `series_col` (or the first column if `series_col` is not set).
        series_col (str, optional): DataFrame column whose values label each series.
            If omitted, row index labels are used (e.g. "Series 1").
        max_values (float, list, or dict, optional): Override auto-scaled axis maximums.
            Pass a single float to apply to all axes, a list aligned to `axes`, or a
            dict mapping axis names to their max values.
        title (str, optional): Chart title.
        palette (str, PaletteName, PaletteOptions dict, or list, optional): Color palette.
        width (str, optional): CSS width. Defaults to "99%".
        height (str, optional): CSS height. Defaults to "500px".
        renderer (str, optional): 'canvas' or 'svg'. Defaults to "canvas".
        theme (str, optional): 'light' or 'dark'. Defaults to "light".
        font (str, optional): Font family for the chart.
        options (dict, optional): ECharts options to merge/override.
        **kwargs: Forwarded to the base Chart class.
    """

    def __init__(
        self,
        data: Any = None,
        axes: Union[List[str], List[Dict[str, Any]], None] = None,
        series_col: Optional[str] = None,
        max_values: Union[float, List[float], Dict[str, float], None] = None,
        title: str = None,
        palette: Union[PaletteName, str, PaletteOptions, List[str], None] = None,
        width: str = "99%",
        height: str = "500px",
        renderer: str = "canvas",
        theme: str = "light",
        font: str = None,
        options: Option = None,
        **kwargs
    ):
        # 1. Parse Input into (name, values) pairs and resolved indicator dicts
        parsed_series, resolved_indicators = self._parse_data(data, axes, series_col, max_values)

        n_series = len(parsed_series)
        legend_names = [name for name, _ in parsed_series]

        # 2. Resolve Color Palette
        color_base = color_transparent = None
        if palette is not None:
            if isinstance(palette, dict):
                pk = palette.copy()
                pal = pk.pop("palette")
            else:
                pal, pk = palette, {}
            color_base = Palette(pal, n_series, **pk)
            color_transparent = Palette(pal, n_series, alpha=0, value="-0.5", **pk)

        # 3. Build Series Configurations
        is_light = theme == "light"
        series_list = [
            self._build_series(i, name, values, is_light, color_base, color_transparent)
            for i, (name, values) in enumerate(parsed_series)
        ]

        # 4. Assemble Base Options
        radar_center_y = "50%" if title else "42%"
        _indicator_names = [ind["name"] for ind in resolved_indicators]

        base_options: Option = {
            "tooltip": {
                "trigger": "item",
                "borderWidth": 0,
                "padding": [14, 18],
                "shadowBlur": 10,
                "shadowColor": "rgba(0, 0, 0, 0.12)",
                "extraCssText": "border-radius: 12px;",
                "formatter": JSCode(f"""
                    function(params) {{
                        var indNames = {_indicator_names};
                        var html = '<div style="font-size:15px;font-weight:600;margin-bottom:4px;">' + params.marker + ' ' + params.name + '</div>';
                        if (indNames.length > 0) {{
                            html += '<hr style="margin:4px 0 8px;border:none;border-top:1px solid rgba(0,0,0,0.08);"/>';
                            for (var i = 0; i < params.value.length; i++) {{
                                html += '<div style="display:flex;justify-content:space-between;gap:24px;font-size:13px;padding:1px 0;">';
                                html += '<span>' + indNames[i] + '</span>';
                                html += '<span style="font-weight:600;">' + Number(params.value[i]).toLocaleString() + '</span>';
                                html += '</div>';
                            }}
                        }}
                        return html;
                    }}
                """),
            },
            "legend": {
                "data": legend_names,
                "bottom": 20,
                "icon": "circle",
                "itemWidth": 20,
                "formatter": "{name}   ",
                "itemStyle": {
                    "opacity": 1
                }
            },
            "toolbox": {
                "feature": {
                    "restore": {},
                    "saveAsImage": {"pixelRatio": 3}
                }
            },
            "radar": {
                "radius": "60%",
                "center": ["50%", radar_center_y],
                "startAngle": 90,
                "triggerEvent": True,
                "shape": "polygon",
                "indicator": resolved_indicators
            },
            "animationEasing": "quinticOut",
            "animationDuration": 900,
            "series": series_list
        }

        # 5. Apply Styling Overrides and Title Layout
        _apply_styling(base_options, title=title, font=font, options=options)

        if title and "title" in base_options:
            base_options["title"].update({"top": 24, "left": "center"})
            if "textStyle" in base_options["title"]:
                base_options["title"]["textStyle"].update({"fontSize": 22, "fontWeight": 600})

        super().__init__(
            options=base_options,
            width=width,
            height=height,
            renderer=renderer,
            theme=theme,
            **kwargs
        )

    @staticmethod
    def _parse_data(data, axes, series_col, max_values):
        parsed_series = []

        if hasattr(data, "columns") and hasattr(data, "__getitem__"):
            # DataFrame: each row is a series
            exclude = {series_col} if series_col else {data.columns[0]}
            axis_names = axes if axes else [c for c in data.columns if c not in exclude]
            for idx, row in data.iterrows():
                name = str(row[series_col]) if series_col else f"Series {idx + 1}"
                parsed_series.append((name, [row[a] for a in axis_names]))
            resolved_indicators = Radar._resolve_indicators(axis_names, max_values, data=data)

        elif isinstance(data, dict):
            # Dict: {"Series Name": [values...], ...}
            axis_names = axes if axes else []
            for name, vals in data.items():
                parsed_series.append((str(name), vals))
            resolved_indicators = Radar._resolve_indicators(axis_names, max_values)

        else:
            axis_names = axes if axes else []
            resolved_indicators = Radar._resolve_indicators(axis_names, max_values)

        return parsed_series, resolved_indicators

    @staticmethod
    def _resolve_indicators(axes, max_values, data=None):
        if not axes:
            return []

        # Already fully specified as dicts — use as-is unless max_values overrides
        if axes and isinstance(axes[0], dict):
            if max_values is None:
                return axes
            axes = [a["name"] for a in axes]

        def get_max(name, i):
            if max_values is None:
                if data is not None:
                    col_max = float(data[name].max())
                    return round(col_max * 1.1) if col_max > 0 else 100
                return 100
            if isinstance(max_values, dict):
                return max_values.get(name, 100)
            if isinstance(max_values, list):
                return max_values[i] if i < len(max_values) else 100
            return float(max_values)

        return [{"name": name, "max": get_max(name, i)} for i, name in enumerate(axes)]

    @staticmethod
    def _build_series(i, name, values, is_light, color_base, color_transparent):
        entry = {
            "name": name,
            "type": "radar",
            "symbol": "circle",
            "symbolSize": 10,
            "itemStyle": {"opacity": 0},
            "data": [{"value": values, "name": name}],
            "emphasis": {
                "focus": "series",
                "lineStyle": {"width": 3, "opacity": 1},
                "itemStyle": {"opacity": 1},
                "areaStyle": {"opacity": 0.5} if is_light else {"opacity": 1.0},
            },
            "blur": {
                "lineStyle": {"width": 1, "opacity": 0.3},
                "itemStyle": {"opacity": 0},
                "areaStyle": {"opacity": 0.02} if is_light else {"opacity": 0.2},
            },
        }

        if color_base is not None:
            base_c = color_base[i % len(color_base)]
            trans_c = color_transparent[i % len(color_transparent)]
            entry["itemStyle"].update({"color": base_c})
            if not is_light:
                entry["itemStyle"].update({"shadowBlur": 10, "shadowColor": base_c})
            entry["lineStyle"] = {"color": base_c, "width": 2}
            entry["areaStyle"] = (
                {"opacity": 0.05, "color": base_c}
                if is_light else
                {
                    "opacity": 0.3,
                    "color": {
                        "type": "linear",
                        "x": 0, "y": 0, "x2": 1, "y2": 1,
                        "colorStops": [
                            {"offset": 0, "color": base_c},
                            {"offset": 1, "color": trans_c}
                        ]
                    }
                }
            )

        return entry