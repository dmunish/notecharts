from typing import Union, Optional, List, Literal
from typing import TypedDict
from ..palette import PaletteName, Palette


class PaletteOptions(TypedDict, total=False):
    """Options dictionary for palette generation.
    
    The 'palette' key is required. All other keys are optional.
    
    Attributes:
        palette: The palette name (PaletteName) or a list of color strings.
        format: Color format - 'hex', 'hsv', 'rgb', or 'rgba'. Defaults to 'hex'.
        value: Adjust the value (brightness) of colors. Optional.
        saturation: Adjust saturation of colors. Optional.
        alpha: Opacity value (0-1). Defaults to 1.0.
        reverse: Whether to reverse color order. Defaults to False.
    """
    palette: Union[PaletteName, str, List[str]]
    format: Literal["hex", "hsv", "rgb", "rgba"]
    value: Optional[float]
    saturation: Optional[float]
    alpha: float
    reverse: bool


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


def _extract_column(df, col_name):
    """Extract single column from dataframe as list."""
    return df[col_name].tolist()


def _extract_columns_dict(df, col_dict):
    """Extract multiple columns from dataframe as dict of lists."""
    return {name: df[col].tolist() for name, col in col_dict.items()}


def _resolve_palette(palette, n):
    """Convert palette param to color list. Supports str, dict, list. Returns None if None."""
    if palette is None:
        return None
    if isinstance(palette, dict):
        p = palette.copy()
        name = p.pop("palette")
        return Palette(name, n, **p)
    if isinstance(palette, str):
        return Palette(palette, n)
    if isinstance(palette, list):
        return palette
    return None


def _apply_styling(opts, title=None, colors=None, font=None, options=None):
    """Apply common styling, deep-merge user options, and forward series-level keys."""
    if title is not None:
        opts["title"] = {
            "text": title,
            "left": "center",
            "top": 24,
            "textStyle": {"fontSize": 22, "fontWeight": 600},
        }
    if colors is not None:
        opts["color"] = colors
    if font is not None:
        opts["textStyle"] = {"fontFamily": font}
    if options:
        known_top = set(opts.keys()) - {"series"}
        _deep_update(opts, options)
        # Forward series-level options (labelLine, label, emphasis, etc.) into each series
        for s in opts.get("series", []):
            for k, v in options.items():
                if k not in known_top:
                    if isinstance(v, dict) and isinstance(s.get(k), dict):
                        s[k].update(v)
                    else:
                        s[k] = v
