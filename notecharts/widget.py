import json
import uuid
import urllib.parse
import importlib
from IPython.display import display, HTML
from typing import Literal

_PALETTES_MAPPING = {
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

def _sample_colors(colors, n, padding=0.1):
    """
    Interpolates 'n' colors from a list of RGB tuples via linear interpolation.

    Args:
        colors (list[tuple]): List of RGB tuples with values in [0, 1].
        n (int): Number of colors to sample.
        padding (float): Ratio to exclude from start and end of the palette. Defaults to 0.1.

    Returns:
        list[tuple]: List of n interpolated RGB tuples.
    """
    if n <= 0:
        return []
    if n == 1:
        return [colors[len(colors) // 2]]

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
            interpolated = tuple(c1[j] + (c2[j] - c1[j]) * fract for j in range(3))
            result.append(interpolated)
    return result


def _rgb_to_hex(rgb):
    """Converts an RGB tuple (floats in [0,1]) to hex string."""
    r, g, b = rgb
    return "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))


class JSCode:
    """Wraps a raw JavaScript string to be inserted unquoted into the ECharts options.

    Attributes:
        js (str): The raw JavaScript code string.
    """
    def __init__(self, js: str):
        """Initializes JSCode with the given JavaScript string.

        Args:
            js (str): The JavaScript code.
        """
        self.js = js

    def __repr__(self):
        return f"JSCode({self.js!r})"


class _EChartsEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.placeholders = {}

    def default(self, obj):
        if isinstance(obj, JSCode):
            placeholder = f"__JS_{uuid.uuid4().hex}__"
            self.placeholders[placeholder] = obj.js
            return placeholder
        return super().default(obj)


class Chart:
    """Renders Apache ECharts directly in a Jupyter notebook from a Python 'options' dict.

    Features include automatic Google Fonts loading from any 'fontFamily' value found
    inside the options dictionary and global font setting via `textStyle.fontFamily`.

    Attributes:
        options (dict): The ECharts option dictionary.
        width (str): CSS width of the chart container.
        height (str): CSS height of the chart container.
        renderer (str): The renderer type ('canvas' or 'svg').
        theme (str): The chart theme ('light' or 'dark').
        devicePixelRatio (str): The pixel ratio at which to render when using Canvas. Default is 1.
    """

    # Generic CSS font families that should not be loaded from Google Fonts
    _GENERIC_FONTS = {
        "serif", "sans-serif", "monospace", "cursive", "fantasy",
        "system-ui", "ui-serif", "ui-sans-serif", "ui-monospace",
        "ui-rounded", "math", "emoji", "fangsong",
        "inherit", "initial", "unset"
    }

    def __init__(
        self,
        options: dict,
        width: str = "99%",
        height: str = "500px",
        renderer: str = "canvas",
        theme: str = "light",
        devicePixelRatio = 1
    ):
        """Initializes the Chart with options and display settings.

        Args:
            options (dict): The ECharts option dictionary.
            width (str, optional): CSS width. Defaults to "99%".
            height (str, optional): CSS height. Defaults to "500px".
            renderer (str, optional): 'canvas' or 'svg'. Defaults to "canvas".
            theme (str, optional): 'light' or 'dark'. Defaults to "light".

        Raises:
            TypeError: If options is not a dictionary.
            ValueError: If renderer or theme is invalid.
        """
        if not isinstance(options, dict):
            raise TypeError(
                f"Chart options must be a dictionary, got {type(options).__name__}."
            )
        self.options = options
        self.width = width.strip() if isinstance(width, str) else str(width)
        self.height = height.strip() if isinstance(height, str) else str(height)

        self.renderer = renderer.lower().strip()
        if self.renderer not in ["canvas", "svg"]:
            raise ValueError(
                f"Invalid renderer '{self.renderer}'. Supported: 'canvas', 'svg'."
            )

        self.theme = theme.lower().strip()
        if self.theme not in ["light", "dark"]:
            raise ValueError(
                f"Invalid theme '{self.theme}'. Supported: 'light', 'dark'."
            )

        if self.theme == "light" and "backgroundColor" not in self.options:
            self.options["backgroundColor"] = "white"

        # Resolve palettable palettes to hex color arrays
        self._resolve_palettes(self.options)

        # Discover all custom font families from the options dict
        self.fonts = list(self._discover_fonts(self.options))

    # ------------------------------------------------------------------
    # Font discovery
    # ------------------------------------------------------------------
    @classmethod
    def _extract_font_families(cls, value):
        """Return a set of non‑generic font family names from a raw value."""
        if isinstance(value, JSCode):
            return set()
        if isinstance(value, str):
            candidates = [name.strip().strip("'\"") for name in value.split(",")]
        elif isinstance(value, (list, tuple)):
            candidates = []
            for item in value:
                if isinstance(item, str):
                    candidates.extend(
                        name.strip().strip("'\"") for name in item.split(",")
                    )
        else:
            return set()

        families = set()
        for candidate in candidates:
            lower = candidate.lower()
            # Keep only non‑generic names
            if lower and lower not in cls._GENERIC_FONTS:
                families.add(candidate)
        return families

    def _discover_fonts(self, obj, found=None):
        """Recursively walk the options dict to collect font families."""
        if found is None:
            found = set()
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == "fontFamily":
                    found.update(self._extract_font_families(value))
                else:
                    self._discover_fonts(value, found)
        elif isinstance(obj, list):
            for item in obj:
                self._discover_fonts(item, found)
        return found

    # ------------------------------------------------------------------
    # Palette resolution
    # ------------------------------------------------------------------
    def _resolve_palettes(self, obj, n_colors=None):
        """Recursively walk options to replace palette name strings with hex arrays."""
        if n_colors is None:
            n_colors = self._infer_n_colors(obj)

        self._resolve_palettes_impl(obj, n_colors)

    def _resolve_palettes_impl(self, obj, n_colors):
        """Implementation of palette resolution."""
        if isinstance(obj, dict):
            for key, value in list(obj.items()):
                if key == "color" and isinstance(value, str):
                    # Replace palette string with interpolated hex array
                    hex_palette = self._get_palette_as_hex(value, n_colors)
                    if hex_palette is not None:
                        obj[key] = hex_palette
                    elif obj is self.options:
                        del obj[key]
                else:
                    self._resolve_palettes_impl(value, n_colors)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                if isinstance(item, str):
                    # Check if this string is a known palette name
                    hex_palette = self._get_palette_as_hex(item, n_colors)
                    if hex_palette is not None:
                        obj[i] = hex_palette
                else:
                    self._resolve_palettes_impl(item, n_colors)

    def _infer_n_colors(self, obj):
        if isinstance(obj, dict):
            if "series" in obj and isinstance(obj["series"], list):
                series_list = obj["series"]
                if series_list and "categories" in series_list[0]:
                    cats = series_list[0]["categories"]
                    if isinstance(cats, list):
                        return len(cats)
                return len(series_list)   # fallback to series count
            for value in obj.values():
                n = self._infer_n_colors(value)
                if n > 0:
                    return n
        return 10

    def _get_palette_as_hex(self, palette_name, n_colors):
        """
        Resolve a palette name to a list of hex colors.

        Args:
            palette_name (str): Name of the palette or full path.
            n_colors (int): Number of colors to sample.

        Returns:
            list[str] or None: List of hex colors, or None if not a known palette.
        """
        if palette_name not in _PALETTES_MAPPING:
            return None

        module_path = _PALETTES_MAPPING[palette_name]
        parts = module_path.split(".")
        module_name = "palettable." + ".".join(parts[:-1])
        palette_obj_name = parts[-1]

        try:
            module = importlib.import_module(module_name)
            palette_obj = getattr(module, palette_obj_name)

            # Handle palette objects that have a 'colors' attribute
            if hasattr(palette_obj, "colors"):
                colors = palette_obj.colors
            else:
                # Try to treat it as a sequence-like object
                colors = list(palette_obj)

            # Normalize RGB tuples: palettable uses 0-255, we need 0-1
            normalized = [
                (c[0] / 255.0, c[1] / 255.0, c[2] / 255.0) for c in colors
            ]

            # Sample and convert to hex
            sampled = _sample_colors(normalized, n_colors)
            return [_rgb_to_hex(color) for color in sampled]
        except (ImportError, AttributeError, TypeError, IndexError):
            return None

    # ------------------------------------------------------------------
    # Serialisation
    # ------------------------------------------------------------------
    def _serialise_options(self) -> str:
        encoder = _EChartsEncoder()
        json_str = encoder.encode(self.options)
        for placeholder, js_code in encoder.placeholders.items():
            json_str = json_str.replace(f'"{placeholder}"', js_code)
        return json_str

    # ------------------------------------------------------------------
    # HTML generation
    # ------------------------------------------------------------------
    def _make_chart_html(self, chart_id=None) -> str:
        if chart_id is None:
            chart_id = f"echart_{uuid.uuid4().hex}"
        options_js = self._serialise_options()

        font_link = ""
        if self.fonts:
            base_url = "https://fonts.googleapis.com/css2"
            params = {"family": self.fonts, "display": "swap"}
            query_string = urllib.parse.urlencode(params, doseq=True)
            font_link = f'<link href="{base_url}?{query_string}" rel="stylesheet">'

        has_fonts = "true" if self.fonts else "false"

        return f"""
        {font_link}
        <div id="{chart_id}" style="width:{self.width};height:{self.height};"></div>
        <script>
        (function() {{

            // ── wait for the div to exist in the DOM ──────────────────────────
            function waitForDom(id, cb) {{
                var dom = document.getElementById(id);
                if (dom) {{ cb(dom); return; }}
                var observer = new MutationObserver(function() {{
                    var el = document.getElementById(id);
                    if (el) {{ observer.disconnect(); cb(el); }}
                }});
                observer.observe(document.body || document.documentElement, {{
                    childList: true, subtree: true
                }});
                var attempts = 0;
                var poll = setInterval(function() {{
                    var el = document.getElementById(id);
                    if (el) {{ clearInterval(poll); observer.disconnect(); cb(el); return; }}
                    if (++attempts > 100) {{
                        clearInterval(poll); observer.disconnect();
                        console.error('ECharts wrapper: #{chart_id} never appeared in DOM');
                    }}
                }}, 100);
            }}

            // ── chart init ─────
            function initChart(ec) {{
                waitForDom('{chart_id}', function(dom) {{
                    var chart = ec.init(dom, '{self.theme}', {{
                        renderer: '{self.renderer}', devicePixelRatio: {self.devicePixelRatio}
                    }});
                    chart.setOption({options_js});
                    window.addEventListener('resize', function() {{ chart.resize(); }});
                }});
            }}

            // ── plain <script> loader (Colab / plain Jupyter) ─────────────────
            function loadScript(url, cb) {{
                var s = document.createElement('script');
                s.src = url;
                s.onload = cb;
                s.onerror = function() {{ console.error('ECharts wrapper: failed to load ' + url); }};
                document.head.appendChild(s);
            }}

            function loadViaScript() {{
                loadScript('https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js', function() {{
                    loadScript('https://cdn.jsdelivr.net/npm/echarts-gl/dist/echarts-gl.min.js', function() {{
                        initChart(window.echarts);
                    }});
                }});
            }}

            // ── RequireJS loader (VS Code webview) ────────────────────────────
            function loadViaRequire() {{
                // Reset any cached failed/partial module state
                require.undef('echarts');
                require.undef('echarts-gl');
                require.config({{
                    paths: {{
                        'echarts': 'https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min',
                        'echarts-gl': 'https://cdn.jsdelivr.net/npm/echarts-gl/dist/echarts-gl.min'
                    }}
                }});
                require(['echarts'], function(ec) {{
                    require(['echarts-gl'], function() {{
                        initChart(ec);
                    }});
                }}, function(err) {{
                    console.error('ECharts wrapper: RequireJS failed to load', err);
                }});
            }}

            // ── font gate → then load echarts ─────────────────────────────────
            function loadEchartsAndInit() {{
                if (typeof require !== 'undefined' && typeof require.config === 'function') {{
                    loadViaRequire();
                }} else {{
                    loadViaScript();
                }}
            }}

            if ({has_fonts}) {{
                if (document.fonts && document.fonts.ready) {{
                    document.fonts.ready.then(loadEchartsAndInit);
                }} else {{
                    loadEchartsAndInit();
                }}
            }} else {{
                loadEchartsAndInit();
            }}
        }})();
        </script>
        """

    # ------------------------------------------------------------------
    # Display
    # ------------------------------------------------------------------
    def display(self):
        display(HTML(self._make_chart_html()))

    def _repr_html_(self):
        return self._make_chart_html()