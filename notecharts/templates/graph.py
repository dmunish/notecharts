from typing import Union, List, Dict, Any, Optional
from ..chart import Chart
from ..palette import PaletteName, Palette
from .utils import PaletteOptions, _apply_styling


class Graph(Chart):
    """Pre-built Force-Directed Graph.

    Creates an interactive force-directed graph from nodes and links,
    with automatic symbol sizing and palette-driven category colors.

    Args:
        nodes (list of dict): Node objects, each with 'id', 'name', 'value' (optional,
            determines symbolSize), and 'category' (optional, index or name).
        links (list of dict): Link objects with 'source' and 'target' node ids.
        categories (list, optional): Category names/objects. If omitted, inferred
            from nodes. Defaults to None.
        title (str, optional): Chart title. Defaults to None.
        palette (str, PaletteName, PaletteOptions dict, or list of colors, optional):
            Color palette for categories. Defaults to None (ECharts defaults).
        width (str, optional): CSS width. Defaults to "99%".
        height (str, optional): CSS height. Defaults to "500px".
        renderer (str, optional): 'canvas' or 'svg'. Defaults to "canvas".
        theme (str, optional): 'light' or 'dark'. Defaults to "light".
        options (dict, optional): ECharts options to merge/override.
        font (str, optional): Font family. Defaults to None.
        **kwargs: Forwarded to the base Chart class.
    """

    def __init__(
        self,
        nodes: List[Dict[str, Any]],
        links: List[Dict[str, Any]],
        categories: Optional[List] = None,
        title: str = None,
        palette: Union[PaletteName, str, PaletteOptions, List[str], None] = None,
        width: str = "99%",
        height: str = "500px",
        renderer: str = "canvas",
        theme: str = "light",
        options: Optional[Dict] = None,
        font: str = None,
        **kwargs
    ):
        # Infer categories from nodes if not provided
        if categories is None:
            seen = set()
            categories = []
            for n in nodes:
                cat = n.get("category")
                if cat is not None and cat not in seen:
                    seen.add(cat)
                    categories.append(cat)

        # Generate category colors from palette
        n_cats = len(categories)
        if palette is not None and n_cats > 0:
            if isinstance(palette, dict):
                pk = palette.copy()
                pal = pk.pop("palette")
            else:
                pal = palette
                pk = {}
            cat_fill = Palette(pal, n_cats, **pk)
            cat_border = Palette(pal, n_cats, value=0.75, saturation=0.4, **pk)
        else:
            cat_fill = cat_border = None

        # Apply colors to categories
        for i, cat in enumerate(categories):
            if isinstance(cat, dict):
                if cat_fill is not None:
                    cat["itemStyle"] = {
                        "color": cat_fill[i],
                        "borderColor": cat_border[i],
                        "borderWidth": 3,
                    }
            else:
                categories[i] = {
                    "name": str(cat),
                }
                if cat_fill is not None:
                    categories[i]["itemStyle"] = {
                        "color": cat_fill[i],
                        "borderColor": cat_border[i],
                        "borderWidth": 3,
                    }

        # Scale node values to symbolSize
        values = [n.get("value", 0) or 0 for n in nodes if n.get("value") is not None]
        if values:
            vmin, vmax = min(values), max(values)
            vrange = vmax - vmin if vmax > vmin else 1
            for node in nodes:
                val = node.get("value", 0) or 0
                normalized = (val - vmin) / vrange
                node["symbolSize"] = 6 + normalized * 16

        base_options = {
            "tooltip": {"show": False},
            "toolbox": {
                "feature": {
                    "restore": {},
                    "saveAsImage": {"name": title if title else "Graph", "pixelRatio": 3},
                }
            },
            "series": [
                {
                    "name": title if title else "Graph",
                    "type": "graph",
                    "layout": "force",
                    "data": nodes,
                    "links": links,
                    "categories": categories,
                    "roam": True,
                    "draggable": True,
                    "label": {"show": False, "position": "right", "fontSize": 11},
                    "lineStyle": {"width": 0.5, "opacity": 0.6},
                    "force": {
                        "repulsion": 200,
                        "gravity": 0.1,
                        "edgeLength": [100, 300],
                        "friction": 0.2,
                    },
                    "animationDuration": 1000,
                    "animationEasing": "cubicOut",
                }
            ],
        }

        _apply_styling(base_options, title=title, font=font, options=options)

        super().__init__(
            options=base_options,
            width=width,
            height=height,
            renderer=renderer,
            theme=theme,
            **kwargs
        )
