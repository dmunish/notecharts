from .chart import Chart, JSCode
from .palette import Palette
from .option import Option

from .templates.bar import Bar
from .templates.line import Line
from .templates.radar import Radar
from .templates.scatter import Scatter
from .templates.pie import Pie
from .templates.graph import Graph

__version__ = "0.4.0"
__all__ = ["Chart", "JSCode", "Palette", "Option", "Bar", "Line", "Scatter", "Radar", "Pie", "Graph"]