import re
import importlib
from typing import Literal, Union, List, Tuple, Optional

# ============================================================================
# Palette Mapping
# ============================================================================

PALETTES_MAPPING = {
    "Accent": "colorbrewer.qualitative.Accent_7",
    "Acton": "scientific.sequential.Acton_19",
    "Algae": "cmocean.sequential.Algae_19",
    "Amp": "cmocean.sequential.Amp_19",
    "Antique": "cartocolors.qualitative.Antique_9",
    "Aquatic1": "wesanderson.Aquatic1_5",
    "Aquatic2": "wesanderson.Aquatic2_5",
    "Aquatic3": "wesanderson.Aquatic3_5",
    "ArmyRose": "cartocolors.diverging.ArmyRose_7",
    "Balance": "cmocean.diverging.Balance_19",
    "Bamako": "scientific.sequential.Bamako_19",
    "Batlow": "scientific.sequential.Batlow_19",
    "Berlin": "scientific.diverging.Berlin_19",
    "Bilbao": "scientific.sequential.Bilbao_19",
    "BluGrn": "cartocolors.sequential.BluGrn_7",
    "BluYl": "cartocolors.sequential.BluYl_7",
    "BlueDarkOrange12": "lightbartlein.diverging.BlueDarkOrange12_11",
    "BlueDarkOrange18": "lightbartlein.diverging.BlueDarkOrange18_17",
    "BlueDarkRed12": "lightbartlein.diverging.BlueDarkRed12_11",
    "BlueDarkRed18": "lightbartlein.diverging.BlueDarkRed18_17",
    "BlueGray": "lightbartlein.diverging.BlueGray_7",
    "BlueGreen": "lightbartlein.diverging.BlueGreen_13",
    "BlueGrey": "lightbartlein.diverging.BlueGrey_7",
    "BlueOrange10": "lightbartlein.diverging.BlueOrange10_9",
    "BlueOrange12": "lightbartlein.diverging.BlueOrange12_11",
    "BlueOrange8": "lightbartlein.diverging.BlueOrange8_7",
    "BlueOrangeRed": "lightbartlein.diverging.BlueOrangeRed_13",
    "BlueRed": "tableau.BlueRed_12",
    "Blues": "colorbrewer.sequential.Blues_9",
    "Blues10": "lightbartlein.sequential.Blues10_9",
    "Blues7": "lightbartlein.sequential.Blues7_7",
    "Bold": "cartocolors.qualitative.Bold_9",
    "BrBG": "colorbrewer.diverging.BrBG_11",
    "BrewerMap": "colorbrewer.BrewerMap",
    "Broc": "scientific.diverging.Broc_19",
    "BrownBlue10": "lightbartlein.diverging.BrownBlue10_9",
    "BrownBlue12": "lightbartlein.diverging.BrownBlue12_11",
    "BrwnYl": "cartocolors.sequential.BrwnYl_7",
    "BuGn": "colorbrewer.sequential.BuGn_9",
    "BuPu": "colorbrewer.sequential.BuPu_9",
    "Buda": "scientific.sequential.Buda_19",
    "Burg": "cartocolors.sequential.Burg_7",
    "BurgYl": "cartocolors.sequential.BurgYl_7",
    "CartoColorsMap": "cartocolors.cartocolorspalette.CartoColorsMap",
    "Cavalcanti": "wesanderson.Cavalcanti_5",
    "Chevalier": "wesanderson.Chevalier_4",
    "CmoceanMap": "cmocean.cmoceanpalette.CmoceanMap",
    "ColorBlind": "tableau.ColorBlind_10",
    "Cork": "scientific.diverging.Cork_19",
    "Cube1": "mycarta.Cube1_19",
    "CubeYF": "mycarta.CubeYF_19",
    "Cubehelix": "cubehelix.Cubehelix",
    "Curl": "cmocean.diverging.Curl_19",
    "Darjeeling1": "wesanderson.Darjeeling1_4",
    "Darjeeling2": "wesanderson.Darjeeling2_5",
    "Darjeeling3": "wesanderson.Darjeeling3_5",
    "Darjeeling4": "wesanderson.Darjeeling4_5",
    "Dark2": "colorbrewer.qualitative.Dark2_7",
    "DarkMint": "cartocolors.sequential.DarkMint_7",
    "Davos": "scientific.sequential.Davos_19",
    "Deep": "cmocean.sequential.Deep_19",
    "Delta": "cmocean.diverging.Delta_19",
    "Dense": "cmocean.sequential.Dense_19",
    "Devon": "scientific.sequential.Devon_19",
    "Earth": "cartocolors.diverging.Earth_7",
    "Emrld": "cartocolors.sequential.Emrld_7",
    "Fall": "cartocolors.diverging.Fall_7",
    "FantasticFox1": "wesanderson.FantasticFox1_5",
    "FantasticFox2": "wesanderson.FantasticFox2_5",
    "Geyser": "cartocolors.diverging.Geyser_7",
    "GnBu": "colorbrewer.sequential.GnBu_9",
    "GrandBudapest1": "wesanderson.GrandBudapest1_4",
    "GrandBudapest2": "wesanderson.GrandBudapest2_4",
    "GrandBudapest3": "wesanderson.GrandBudapest3_6",
    "GrandBudapest4": "wesanderson.GrandBudapest4_5",
    "GrandBudapest5": "wesanderson.GrandBudapest5_5",
    "Gray": "cmocean.sequential.Gray_19",
    "GrayC": "scientific.sequential.GrayC_19",
    "GreenMagenta": "lightbartlein.diverging.GreenMagenta_15",
    "GreenOrange": "tableau.GreenOrange_12",
    "Greens": "colorbrewer.sequential.Greens_9",
    "Greys": "colorbrewer.sequential.Greys_9",
    "Haline": "cmocean.sequential.Haline_19",
    "Hawaii": "scientific.sequential.Hawaii_19",
    "Ice": "cmocean.sequential.Ice_19",
    "Imola": "scientific.sequential.Imola_19",
    "Inferno": "matplotlib.Inferno_19",
    "IsleOfDogs1": "wesanderson.IsleOfDogs1_5",
    "IsleOfDogs2": "wesanderson.IsleOfDogs2_6",
    "IsleOfDogs3": "wesanderson.IsleOfDogs3_4",
    "LaJolla": "scientific.sequential.LaJolla_19",
    "LaPaz": "scientific.sequential.LaPaz_19",
    "LightBartleinMap": "lightbartlein.lightbartlein.LightBartleinMap",
    "LinearL": "mycarta.LinearL_19",
    "Lisbon": "scientific.diverging.Lisbon_19",
    "Magenta": "cartocolors.sequential.Magenta_7",
    "Magma": "matplotlib.Magma_19",
    "Margot1": "wesanderson.Margot1_5",
    "Margot2": "wesanderson.Margot2_4",
    "Margot3": "wesanderson.Margot3_4",
    "MatplotlibMap": "matplotlib.matplotlib.MatplotlibMap",
    "Matter": "cmocean.sequential.Matter_19",
    "Mendl": "wesanderson.Mendl_4",
    "Mint": "cartocolors.sequential.Mint_7",
    "Moonrise1": "wesanderson.Moonrise1_5",
    "Moonrise2": "wesanderson.Moonrise2_4",
    "Moonrise3": "wesanderson.Moonrise3_4",
    "Moonrise4": "wesanderson.Moonrise4_5",
    "Moonrise5": "wesanderson.Moonrise5_6",
    "Moonrise6": "wesanderson.Moonrise6_5",
    "Moonrise7": "wesanderson.Moonrise7_5",
    "MycartaMap": "mycarta.mycarta.MycartaMap",
    "Nuuk": "scientific.sequential.Nuuk_19",
    "Oleron": "scientific.sequential.Oleron_19",
    "OrRd": "colorbrewer.sequential.OrRd_9",
    "OrYel": "cartocolors.sequential.OrYel_7",
    "Oranges": "colorbrewer.sequential.Oranges_9",
    "Oslo": "scientific.sequential.Oslo_19",
    "Oxy": "cmocean.sequential.Oxy_19",
    "PRGn": "colorbrewer.diverging.PRGn_11",
    "Paired": "colorbrewer.qualitative.Paired_11",
    "Palette": "cartocolors.cartocolorspalette.Palette",
    "Pastel": "cartocolors.qualitative.Pastel_9",
    "Pastel1": "colorbrewer.qualitative.Pastel1_9",
    "Pastel2": "colorbrewer.qualitative.Pastel2_7",
    "Peach": "cartocolors.sequential.Peach_7",
    "Phase": "cmocean.sequential.Phase_19",
    "PiYG": "colorbrewer.diverging.PiYG_11",
    "PinkYl": "cartocolors.sequential.PinkYl_7",
    "Plasma": "matplotlib.Plasma_19",
    "Prism": "cartocolors.qualitative.Prism_9",
    "PuBu": "colorbrewer.sequential.PuBu_9",
    "PuBuGn": "colorbrewer.sequential.PuBuGn_9",
    "PuOr": "colorbrewer.diverging.PuOr_11",
    "PuRd": "colorbrewer.sequential.PuRd_9",
    "Purp": "cartocolors.sequential.Purp_7",
    "PurpOr": "cartocolors.sequential.PurpOr_7",
    "PurpleGray": "tableau.PurpleGray_12",
    "Purples": "colorbrewer.sequential.Purples_9",
    "RdBu": "colorbrewer.diverging.RdBu_11",
    "RdGy": "colorbrewer.diverging.RdGy_11",
    "RdPu": "colorbrewer.sequential.RdPu_9",
    "RdYlBu": "colorbrewer.diverging.RdYlBu_11",
    "RdYlGn": "colorbrewer.diverging.RdYlGn_11",
    "RedOr": "cartocolors.sequential.RedOr_7",
    "RedYellowBlue": "lightbartlein.diverging.RedYellowBlue_11",
    "Reds": "colorbrewer.sequential.Reds_9",
    "Roma": "scientific.diverging.Roma_19",
    "Royal1": "wesanderson.Royal1_4",
    "Royal2": "wesanderson.Royal2_5",
    "Royal3": "wesanderson.Royal3_5",
    "Safe": "cartocolors.qualitative.Safe_9",
    "ScientificMap": "scientific.scientific.ScientificMap",
    "Set1": "colorbrewer.qualitative.Set1_9",
    "Set2": "colorbrewer.qualitative.Set2_7",
    "Set3": "colorbrewer.qualitative.Set3_11",
    "Solar": "cmocean.sequential.Solar_19",
    "Spectral": "colorbrewer.diverging.Spectral_11",
    "Speed": "cmocean.sequential.Speed_19",
    "Sunset": "cartocolors.sequential.Sunset_7",
    "SunsetDark": "cartocolors.sequential.SunsetDark_7",
    "Tableau": "tableau.Tableau_20",
    "TableauLight": "tableau.TableauLight_10",
    "TableauMap": "tableau.tableau.TableauMap",
    "TableauMedium": "tableau.TableauMedium_10",
    "Teal": "cartocolors.sequential.Teal_7",
    "TealGrn": "cartocolors.sequential.TealGrn_7",
    "TealRose": "cartocolors.diverging.TealRose_7",
    "Tempo": "cmocean.sequential.Tempo_19",
    "Temps": "cartocolors.diverging.Temps_7",
    "Thermal": "cmocean.sequential.Thermal_19",
    "Tofino": "scientific.diverging.Tofino_19",
    "Tokyo": "scientific.sequential.Tokyo_19",
    "TrafficLight": "tableau.TrafficLight_9",
    "Tropic": "cartocolors.diverging.Tropic_7",
    "Turbid": "cmocean.sequential.Turbid_19",
    "Turku": "scientific.sequential.Turku_19",
    "Vik": "scientific.diverging.Vik_19",
    "Viridis": "matplotlib.Viridis_19",
    "Vivid": "cartocolors.qualitative.Vivid_9",
    "WesAndersonMap": "wesanderson.wesanderson.WesAndersonMap",
    "YlGn": "colorbrewer.sequential.YlGn_9",
    "YlGnBu": "colorbrewer.sequential.YlGnBu_9",
    "YlOrBr": "colorbrewer.sequential.YlOrBr_9",
    "YlOrRd": "colorbrewer.sequential.YlOrRd_9",
    "Zissou": "wesanderson.Zissou_5",
    "agGrnYl": "cartocolors.sequential.agGrnYl_7",
    "agSunset": "cartocolors.sequential.agSunset_7",
    "classic": "cubehelix.classic_16",
    "cubehelix1": "cubehelix.cubehelix1_16",
    "cubehelix2": "cubehelix.cubehelix2_16",
    "cubehelix3": "cubehelix.cubehelix3_16",
    "jim_special": "cubehelix.jim_special_16",
    "perceptual_rainbow": "cubehelix.perceptual_rainbow_16",
    "purple": "cubehelix.purple_16",
    "red": "cubehelix.red_16"
}

PaletteName = Literal[
    "Accent", "Acton", "Algae", "Amp", "Antique", "Aquatic1", "Aquatic2",
    "Aquatic3", "ArmyRose", "Balance", "Bamako", "Batlow", "Berlin", "Bilbao",
    "BluGrn", "BluYl", "BlueDarkOrange12", "BlueDarkOrange18", "BlueDarkRed12",
    "BlueDarkRed18", "BlueGray", "BlueGreen", "BlueGrey", "BlueOrange10",
    "BlueOrange12", "BlueOrange8", "BlueOrangeRed", "BlueRed", "Blues",
    "Blues10", "Blues7", "Bold", "BrBG", "BrewerMap", "Broc", "BrownBlue10",
    "BrownBlue12", "BrwnYl", "BuGn", "BuPu", "Buda", "Burg", "BurgYl",
    "CartoColorsMap", "Cavalcanti", "Chevalier", "CmoceanMap", "ColorBlind",
    "Cork", "Cube1", "CubeYF", "Cubehelix", "Curl", "Darjeeling1",
    "Darjeeling2", "Darjeeling3", "Darjeeling4", "Dark2", "DarkMint", "Davos",
    "Deep", "Delta", "Dense", "Devon", "Earth", "Emrld", "Fall",
    "FantasticFox1", "FantasticFox2", "Geyser", "GnBu", "GrandBudapest1",
    "GrandBudapest2", "GrandBudapest3", "GrandBudapest4", "GrandBudapest5",
    "Gray", "GrayC", "GreenMagenta", "GreenOrange", "Greens", "Greys",
    "Haline", "Hawaii", "Ice", "Imola", "Inferno", "IsleOfDogs1",
    "IsleOfDogs2", "IsleOfDogs3", "LaJolla", "LaPaz", "LightBartleinMap",
    "LinearL", "Lisbon", "Magenta", "Magma", "Margot1", "Margot2", "Margot3",
    "MatplotlibMap", "Matter", "Mendl", "Mint", "Moonrise1", "Moonrise2",
    "Moonrise3", "Moonrise4", "Moonrise5", "Moonrise6", "Moonrise7",
    "MycartaMap", "Nuuk", "Oleron", "OrRd", "OrYel", "Oranges", "Oslo", "Oxy",
    "PRGn", "Paired", "Palette", "Pastel", "Pastel1", "Pastel2", "Peach",
    "Phase", "PiYG", "PinkYl", "Plasma", "Prism", "PuBu", "PuBuGn", "PuOr",
    "PuRd", "Purp", "PurpOr", "PurpleGray", "Purples", "RdBu", "RdGy", "RdPu",
    "RdYlBu", "RdYlGn", "RedOr", "RedYellowBlue", "Reds", "Roma", "Royal1",
    "Royal2", "Royal3", "Safe", "ScientificMap", "Set1", "Set2", "Set3",
    "Solar", "Spectral", "Speed", "Sunset", "SunsetDark", "Tableau",
    "TableauLight", "TableauMap", "TableauMedium", "Teal", "TealGrn",
    "TealRose", "Tempo", "Temps", "Thermal", "Tofino", "Tokyo",
    "TrafficLight", "Tropic", "Turbid", "Turku", "Vik", "Viridis", "Vivid",
    "WesAndersonMap", "YlGn", "YlGnBu", "YlOrBr", "YlOrRd", "Zissou",
    "agGrnYl", "agSunset", "classic", "cubehelix1", "cubehelix2", "cubehelix3",
    "jim_special", "perceptual_rainbow", "purple", "red"
]

ColorFormat = Literal["hex", "hsv", "rgb", "rgba"]

# ============================================================================
# Color Conversion Utilities
# ============================================================================


def _rgb_to_hsv(rgb: Tuple[float, float, float]) -> Tuple[float, float, float]:
    """
    Convert RGB (0-1) to HSV (0-1).
    
    Args:
        rgb: RGB tuple with values in [0, 1].
        
    Returns:
        HSV tuple with values in [0, 1] (H: 0-1 maps to 0-360°).
    """
    r, g, b = rgb
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    delta = max_val - min_val

    # Calculate Value
    v = max_val

    # Calculate Saturation
    s = 0 if max_val == 0 else delta / max_val

    # Calculate Hue
    if delta == 0:
        h = 0
    elif max_val == r:
        h = (g - b) / delta % 6
    elif max_val == g:
        h = (b - r) / delta + 2
    else:
        h = (r - g) / delta + 4
    h = h / 6.0  # Normalize to [0, 1]

    return (h, s, v)


def _hsv_to_rgb(hsv: Tuple[float, float, float]) -> Tuple[float, float, float]:
    """
    Convert HSV (0-1) to RGB (0-1).
    
    Args:
        hsv: HSV tuple with values in [0, 1] (H: 0-1 maps to 0-360°).
        
    Returns:
        RGB tuple with values in [0, 1].
    """
    h, s, v = hsv
    h = h * 6  # Convert to [0, 6]
    c = v * s
    x = c * (1 - abs((h % 2) - 1))
    m = v - c

    if h < 1:
        r, g, b = c, x, 0
    elif h < 2:
        r, g, b = x, c, 0
    elif h < 3:
        r, g, b = 0, c, x
    elif h < 4:
        r, g, b = 0, x, c
    elif h < 5:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x

    return (r + m, g + m, b + m)


def _parse_color_string(color_str: str) -> Tuple[float, float, float]:
    """
    Parse a color string (hex, rgb, rgba, hsv) to RGB tuple (0-1).
    
    Args:
        color_str: Color string in format:
            - '#RRGGBB' or '#RRGGBBAA' (hex)
            - 'rgb(r, g, b)' (0-255)
            - 'rgba(r, g, b, a)' (0-255, 0-1)
            - 'hsv(h, s, v)' (0-360, 0-100, 0-100)
            
    Returns:
        RGB tuple with values in [0, 1]. Alpha is ignored/stripped.
        
    Raises:
        ValueError: If color string format is invalid.
    """
    color_str = color_str.strip()

    # Hex format
    if color_str.startswith("#"):
        hex_str = color_str[1:]
        if len(hex_str) not in (6, 8):
            raise ValueError(f"Invalid hex color: {color_str}. Expected #RRGGBB or #RRGGBBAA.")
        try:
            r = int(hex_str[0:2], 16) / 255.0
            g = int(hex_str[2:4], 16) / 255.0
            b = int(hex_str[4:6], 16) / 255.0
            return (r, g, b)
        except ValueError as e:
            raise ValueError(f"Invalid hex color: {color_str}.") from e

    # RGB format: rgb(r, g, b)
    rgb_match = re.match(r"rgb\(\s*(\d+(?:\.\d+)?)\s*,\s*(\d+(?:\.\d+)?)\s*,\s*(\d+(?:\.\d+)?)\s*\)", color_str)
    if rgb_match:
        r = float(rgb_match.group(1)) / 255.0
        g = float(rgb_match.group(2)) / 255.0
        b = float(rgb_match.group(3)) / 255.0
        if not (0 <= r <= 1 and 0 <= g <= 1 and 0 <= b <= 1):
            raise ValueError(f"RGB values must be in [0, 255]: {color_str}")
        return (r, g, b)

    # RGBA format: rgba(r, g, b, a)
    rgba_match = re.match(r"rgba\(\s*(\d+(?:\.\d+)?)\s*,\s*(\d+(?:\.\d+)?)\s*,\s*(\d+(?:\.\d+)?)\s*,\s*([\d.]+)\s*\)", color_str)
    if rgba_match:
        r = float(rgba_match.group(1)) / 255.0
        g = float(rgba_match.group(2)) / 255.0
        b = float(rgba_match.group(3)) / 255.0
        # Alpha is ignored for RGB output
        if not (0 <= r <= 1 and 0 <= g <= 1 and 0 <= b <= 1):
            raise ValueError(f"RGB values must be in [0, 255]: {color_str}")
        return (r, g, b)

    # HSV format: hsv(h, s, v)
    hsv_match = re.match(r"hsv\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)\s*\)", color_str)
    if hsv_match:
        h = float(hsv_match.group(1)) / 360.0  # 0-360 -> 0-1
        s = float(hsv_match.group(2)) / 100.0  # 0-100 -> 0-1
        v = float(hsv_match.group(3)) / 100.0  # 0-100 -> 0-1
        if not (0 <= h <= 1 and 0 <= s <= 1 and 0 <= v <= 1):
            raise ValueError(f"HSV values must be in valid ranges (h: 0-360, s/v: 0-100): {color_str}")
        return _hsv_to_rgb((h, s, v))

    raise ValueError(
        f"Invalid color format: {color_str}. "
        "Expected: #RRGGBB, rgb(r,g,b), rgba(r,g,b,a), or hsv(h,s,v)."
    )


def _rgb_to_hex(rgb: Tuple[float, float, float], alpha: float = 1.0) -> str:
    """
    Convert RGB tuple (0-1) to hex string.
    
    Args:
        rgb: RGB tuple with values in [0, 1].
        alpha: Alpha value in [0, 1]. If not 1, returns 8-digit hex.
        
    Returns:
        Hex color string (#RRGGBB or #RRGGBBAA).
    """
    r, g, b = rgb
    r_hex = int(round(r * 255))
    g_hex = int(round(g * 255))
    b_hex = int(round(b * 255))

    if alpha < 1.0:
        a_hex = int(round(alpha * 255))
        return f"#{r_hex:02x}{g_hex:02x}{b_hex:02x}{a_hex:02x}"
    else:
        return f"#{r_hex:02x}{g_hex:02x}{b_hex:02x}"


def _rgb_to_rgb_string(rgb: Tuple[float, float, float], alpha: float = 1.0) -> str:
    """
    Convert RGB tuple (0-1) to rgb/rgba string.
    
    Args:
        rgb: RGB tuple with values in [0, 1].
        alpha: Alpha value in [0, 1].
        
    Returns:
        RGB or RGBA string.
    """
    r, g, b = rgb
    r_val = int(round(r * 255))
    g_val = int(round(g * 255))
    b_val = int(round(b * 255))

    if alpha < 1.0:
        return f"rgba({r_val}, {g_val}, {b_val}, {alpha:.2f})"
    else:
        return f"rgb({r_val}, {g_val}, {b_val})"


def _rgb_to_hsv_string(rgb: Tuple[float, float, float]) -> str:
    """
    Convert RGB tuple (0-1) to hsv string.
    
    Args:
        rgb: RGB tuple with values in [0, 1].
        
    Returns:
        HSV string in format 'hsv(h, s, v)' with h in 0-360, s/v in 0-100.
    """
    h, s, v = _rgb_to_hsv(rgb)
    h_deg = h * 360
    s_pct = s * 100
    v_pct = v * 100
    return f"hsv({h_deg:.1f}, {s_pct:.1f}, {v_pct:.1f})"


# ============================================================================
# Palette Utilities
# ============================================================================


def _sample_colors(
    colors: List[Tuple[float, float, float]],
    n: int,
    padding: float = 0.1
) -> List[Tuple[float, float, float]]:
    """
    Interpolate n colors from a list of RGB tuples via linear interpolation.
    
    Excludes colors from the start and end of the palette via padding to avoid
    extreme values that may be less perceptually distinct.

    Args:
        colors: List of RGB tuples with values in [0, 1].
        n: Number of colors to sample.
        padding: Ratio to exclude from start and end of the palette. In range [0, 0.5).
                 Defaults to 0.1 (exclude 10% from each end).

    Returns:
        List of n interpolated RGB tuples.
        
    Raises:
        ValueError: If n is negative or if padding is invalid.
    """
    if n < 0:
        raise ValueError(f"Number of colors must be non-negative, got {n}.")
    if not (0 <= padding < 0.5):
        raise ValueError(f"Padding must be in [0, 0.5), got {padding}.")

    if n == 0:
        return []
    if n == 1:
        return [colors[len(colors) // 2]]
    if len(colors) == 0:
        raise ValueError("Cannot sample colors from an empty palette.")

    result = []
    start_pos = padding * (len(colors) - 1)
    end_pos = (1.0 - padding) * (len(colors) - 1)
    span = end_pos - start_pos

    for i in range(n):
        pos = start_pos + (i / (n - 1)) * span
        idx = int(pos)
        fract = pos - idx

        if idx >= len(colors) - 1:
            result.append(colors[-1])
        else:
            c1, c2 = colors[idx], colors[idx + 1]
            interpolated = tuple(
                c1[j] + (c2[j] - c1[j]) * fract for j in range(3)
            )
            result.append(interpolated)

    return result


def _load_palette_from_palettable(palette_name: str) -> List[Tuple[float, float, float]]:
    """
    Load a palette from the palettable library.
    
    Args:
        palette_name: Name of the palette as defined in PALETTES_MAPPING.
        
    Returns:
        List of RGB tuples (0-1) representing the palette colors.
        
    Raises:
        ValueError: If the palette is not found or cannot be loaded.
    """
    if palette_name not in PALETTES_MAPPING:
        raise ValueError(
            f"Unknown palette: {palette_name}. "
            f"Available palettes: {', '.join(sorted(PALETTES_MAPPING.keys()))}."
        )

    module_path = PALETTES_MAPPING[palette_name]
    parts = module_path.split(".")
    module_name = "palettable." + ".".join(parts[:-1])
    palette_obj_name = parts[-1]

    try:
        module = importlib.import_module(module_name)
        palette_obj = getattr(module, palette_obj_name)

        # Handle palette objects with 'colors' attribute
        if hasattr(palette_obj, "colors"):
            colors = palette_obj.colors
        else:
            # Try to treat it as a sequence
            colors = list(palette_obj)

        # Normalize RGB tuples: palettable uses 0-255, we need 0-1
        normalized = [
            (c[0] / 255.0, c[1] / 255.0, c[2] / 255.0) for c in colors
        ]
        return normalized

    except ImportError as e:
        raise ValueError(
            f"Could not import palette module '{module_name}'. "
            "Make sure palettable is installed."
        ) from e
    except (AttributeError, TypeError, IndexError) as e:
        raise ValueError(
            f"Could not load palette '{palette_name}' from palettable."
        ) from e


# ============================================================================
# Main Palette Function
# ============================================================================


def Palette(
    palette: Union[PaletteName, str, List[str]],
    n: int,
    format: ColorFormat = "hex",
    value: Optional[float] = None,
    saturation: Optional[float] = None,
    alpha: float = 1.0,
) -> List[str]:
    """
    Generate a list of colors from a palette or custom color specification.
    
    This function provides a flexible interface for working with color palettes,
    supporting both named palettes from the Palettable library and custom color
    specifications. Colors can be sampled, interpolated, and transformed in
    various ways.

    Parameters
    ----------
    palette : str or list of str
        The color palette specification. Can be:
        
        - A palette name (e.g., 'Viridis', 'Set2'). See the complete list of
          available palettes in the module documentation.
        - A single color string in format: '#RRGGBB', '#RRGGBBAA', 'rgb(r,g,b)',
          'rgba(r,g,b,a)', or 'hsv(h,s,v)'. In this case, all n colors will be
          identical.
        - A list of color strings. Colors will be interpolated between the
          provided colors to generate n distinct colors.

    n : int
        The number of distinct colors to extract from the palette.
        Must be a positive integer.

    format : {'hex', 'hsv', 'rgb', 'rgba'}, optional
        Output color format. Defaults to 'hex'.
        
        - 'hex': Hexadecimal format (#RRGGBB or #RRGGBBAA if alpha < 1)
        - 'rgb': RGB format rgb(r, g, b) with r,g,b in 0-255
        - 'rgba': RGBA format rgba(r, g, b, a) with r,g,b in 0-255, a in 0-1
        - 'hsv': HSV format hsv(h, s, v) with h in 0-360, s,v in 0-100

    value : float, optional
        Fix the brightness (value) component in HSV space to a constant.
        Must be in [0, 1]. If None, uses the original palette brightness.
        This is useful for creating uniform brightness across colors.

    saturation : float, optional
        Fix the saturation component in HSV space to a constant.
        Must be in [0, 1]. If None, uses the original palette saturation.
        This is useful for creating uniform saturation across colors.

    alpha : float, optional
        Alpha transparency value in [0, 1]. Defaults to 1.0 (opaque).
        Only applies to 'rgba' format or 'hex' format with alpha.
        Has no effect on 'rgb' or 'hsv' formats.

    Returns
    -------
    list of str
        A list of n color strings in the specified format.

    Raises
    ------
    TypeError
        If palette is not a string or list, or if n is not an integer.
    ValueError
        If n is not positive, if palette name is unknown, if color strings
        are invalid, if value/saturation/alpha are out of range, or if
        format is invalid.

    Examples
    --------
    Generate 5 colors from the Viridis palette:
    
    >>> Palette('Viridis', 5)
    ['#440154', '#31688e', '#35b779', '#fde724', '#fde724']
    
    Generate colors with fixed saturation:
    
    >>> Palette('Blues', 3, saturation=0.5)
    ['#7fa0d2', '#5a7fa9', '#355080']
    
    Interpolate between custom colors:
    
    >>> Palette(['#ff0000', '#0000ff'], 3, format='hex')
    ['#ff0000', '#7f007f', '#0000ff']
    
    Generate RGBA colors with 50% transparency:
    
    >>> Palette('Set2', 2, format='rgba', alpha=0.5)
    ['rgba(102, 194, 165, 0.50)', 'rgba(252, 141, 98, 0.50)']
    """
    # ========================================================================
    # Parameter Validation
    # ========================================================================

    # Validate n
    if not isinstance(n, int):
        raise TypeError(f"Parameter 'n' must be an integer, got {type(n).__name__}.")
    if n <= 0:
        raise ValueError(f"Parameter 'n' must be positive, got {n}.")

    # Validate format
    if format not in ("hex", "hsv", "rgb", "rgba"):
        raise ValueError(
            f"Parameter 'format' must be one of {{'hex', 'hsv', 'rgb', 'rgba'}}, "
            f"got {format!r}."
        )

    # Validate value
    if value is not None:
        if not isinstance(value, (int, float)):
            raise TypeError(f"Parameter 'value' must be a float in [0, 1], got {type(value).__name__}.")
        if not (0 <= value <= 1):
            raise ValueError(f"Parameter 'value' must be in [0, 1], got {value}.")

    # Validate saturation
    if saturation is not None:
        if not isinstance(saturation, (int, float)):
            raise TypeError(f"Parameter 'saturation' must be a float in [0, 1], got {type(saturation).__name__}.")
        if not (0 <= saturation <= 1):
            raise ValueError(f"Parameter 'saturation' must be in [0, 1], got {saturation}.")

    # Validate alpha
    if not isinstance(alpha, (int, float)):
        raise TypeError(f"Parameter 'alpha' must be a float in [0, 1], got {type(alpha).__name__}.")
    if not (0 <= alpha <= 1):
        raise ValueError(f"Parameter 'alpha' must be in [0, 1], got {alpha}.")

    # ========================================================================
    # Load/Parse Colors
    # ========================================================================

    if isinstance(palette, str):
        # Try palette name first
        if palette in PALETTES_MAPPING:
            colors_rgb = _load_palette_from_palettable(palette)
        else:
            # Try as a single color string
            try:
                single_color = _parse_color_string(palette)
                colors_rgb = [single_color]
            except ValueError as e:
                raise ValueError(
                    f"Unknown palette: {palette!r}. "
                    f"Available palettes: {', '.join(sorted(PALETTES_MAPPING.keys()))}"
                ) from e

    elif isinstance(palette, list):
        if len(palette) == 0:
            raise ValueError("Palette list cannot be empty.")
        if not all(isinstance(c, str) for c in palette):
            raise TypeError("All palette list items must be strings.")

        colors_rgb = []
        for i, color_str in enumerate(palette):
            try:
                color = _parse_color_string(color_str)
                colors_rgb.append(color)
            except ValueError as e:
                raise ValueError(
                    f"Invalid color at index {i}: {color_str!r}."
                ) from e

    else:
        raise TypeError(
            f"Parameter 'palette' must be a string or list of strings, "
            f"got {type(palette).__name__}."
        )

    # ========================================================================
    # Sample Colors
    # ========================================================================

    sampled_colors = _sample_colors(colors_rgb, n)

    # ========================================================================
    # Apply Transformations
    # ========================================================================

    if value is not None or saturation is not None:
        transformed = []
        for rgb in sampled_colors:
            h, s, v = _rgb_to_hsv(rgb)

            # Apply fixed value/saturation
            if saturation is not None:
                s = saturation
            if value is not None:
                v = value

            rgb = _hsv_to_rgb((h, s, v))
            transformed.append(rgb)

        sampled_colors = transformed

    # ========================================================================
    # Format Output
    # ========================================================================

    if format == "hex":
        return [_rgb_to_hex(rgb, alpha) for rgb in sampled_colors]
    elif format == "rgb":
        return [_rgb_to_rgb_string(rgb, alpha) for rgb in sampled_colors]
    elif format == "hsv":
        return [_rgb_to_hsv_string(rgb) for rgb in sampled_colors]
    else:  # format == "rgba"
        return [_rgb_to_rgb_string(rgb, alpha) for rgb in sampled_colors]
