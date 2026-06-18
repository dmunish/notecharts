from .chart import Chart, JSCode
from .palette import Palette, render_palette
from .option import Option

from .templates.bar import Bar
from .templates.line import Line
from .templates.radar import Radar
from .templates.scatter import Scatter
from .templates.pie import Pie

__version__ = "0.5.0"
__all__ = ["Chart", "JSCode", "Palette", "Option", "Bar", "Line", "Scatter", "Radar", "Pie", "render_palette"]