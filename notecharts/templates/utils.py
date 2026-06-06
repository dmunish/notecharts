from typing import Union, Optional, List, Literal
from typing import TypedDict
from ..palette import PaletteName


class PaletteOptions(TypedDict, total=False):
    """Options dictionary for palette generation.
    
    The 'palette' key is required. All other keys are optional.
    
    Attributes:
        palette: The palette name (PaletteName) or a list of color strings.
        format: Color format - 'hex', 'hsv', 'rgb', or 'rgba'. Defaults to 'hex'.
        value: Adjust the value (brightness) of colors. Optional.
        saturation: Adjust saturation of colors. Optional.
        alpha: Opacity value (0-1). Defaults to 1.0.
    """
    palette: Union[PaletteName, str, List[str]]
    format: Literal["hex", "hsv", "rgb", "rgba"]
    value: Optional[float]
    saturation: Optional[float]
    alpha: float


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
