<p align="center">
  <img src="https://github.com/dmunish/notecharts/blob/main/assets/notecharts-banner.png?raw=true" height=100% width=auto />
</p>

[![PyPI](https://img.shields.io/pypi/v/notecharts.svg?style=for-the-badge)](https://pypi.org/project/notecharts)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**notecharts** (note-charts or not-echarts) is designed for web-quality, interactive charts in Jupyter notebooks through Apache ECharts. It faithfully brings the full power of ECharts' declarative JSON-like API directly into Python notebooks, with a few notable enhancements.

## Why notecharts?

If you've done data visualization in Python before, you've likely encountered these standard tools:
- **matplotlib:** Excellent for publication-quality static charts, but lacks out-of-the-box interactivity.
- **plotly.py:** Great for interactive charts, but can require extensive configuration to achieve a polished, modern aesthetic or smooth animations.

Apache ECharts is an incredibly powerful web plotting library. While there have been previous attempts to bring it to Jupyter, they often come with trade-offs:
- **pyecharts:** Powerful, but introduces a deep "Pythonic" abstraction. This deviates from the official ECharts API, making it difficult to translate JavaScript examples from the docs into Python.
- **ipecharts:** Provides widget integration, but can have inconsistent interactivity and currently lacks support for environments like Google Colab.

**notecharts** bridges this gap. It provides a thin layer that allows you to write ECharts options exactly as they appear in the official docs, while handling the heavy lifting of library loading, font injection, dynamic palettes, and serialization.

| Force Directed Graph | Multi-Line |
|:---:|:---:|
| [![Force Directed Graph](https://github.com/dmunish/notecharts/blob/main/assets/force-directed-graph.png?raw=true)](https://github.com/dmunish/notecharts/blob/main/examples/force-directed-graph.ipynb) | [![Multi-Line](https://github.com/dmunish/notecharts/blob/main/assets/line.png?raw=true)](https://github.com/dmunish/notecharts/blob/main/examples/line-bar.ipynb) |
| **Geo/Map** | **3D Scatter** |
| [![Map](https://github.com/dmunish/notecharts/blob/main/assets/geo.png?raw=true)](https://github.com/dmunish/notecharts/blob/main/examples/geo.ipynb) | [![Scatter 3D](https://github.com/dmunish/notecharts/blob/main/assets/scatter-3d.png?raw=true)](https://github.com/dmunish/notecharts/blob/main/examples/scatter-3D.ipynb) |

Click on the images above to view code for making them.

## Key Features

- **Declarative API:** Pass a dictionary, get a chart. No complex class hierarchies to learn.
- **`JSCode` Support:** Inject raw JavaScript functions for formatters, tooltips, and custom processing logic.
- **Font Injection:** Automatically detect font declarations in your config, fetch the corresponding fonts (if available) from Google Fonts.
- **Rich Color Palettes:** Access 196 professionally-designed customizable color palettes from [Palettable](https://jiffyclub.github.io/palettable/), or make your own through interpolation.
- **Pre-built Charts:** Includes pre-built primitives like `Bar`, `Line`, `Scatter`, and `Radar` with beautiful defaults.
- **Environment Agnostic:** Works seamlessly in VS Code, JupyterLab, and Google Colab.
- **Compression:** Compresses the data and config objects so the notebook doesn't balloon in size.

## Installation

```bash
pip install notecharts
```

## Usage

### Full Control
Complete control over every aspect of the chart, through a beautiful, declarative API. If you can find an example on the [ECharts Gallery](https://echarts.apache.org/examples/en/index.html), you can run it in `notecharts`.

```python
from notecharts import Chart, JSCode, Palette

options = {
    "title": {"text": "Bar Chart"},
    "textStyle": {"fontFamily": "Josefin Sans"},    # Automatically loaded from Google Fonts
    "xAxis": {"data": ["Mon", "Tue", "Wed", "Thurs", "Fri"]},
    "yAxis": {},
    "tooltip": {
        "trigger": "axis",
        "formatter": JSCode("function(params) { return params[0].name + ': $' + params[0].value; }")
    },
    "legend": {},
    "series": [
        {
            "name": "Sales",
            "type": "bar",
            "data": [120, 150, 200, 180, 220]
        },
        {
            "name": "Expenses",
            "type": "bar",
            "data": [80, 100, 120, 110, 140]
        },
        {
            "name": "Profit",
            "type": "bar",
            "data": [40, 50, 80, 70, 80]
        }
    ],
    "color": Palette("Plasma", 3)   # Load n colors from any palette,
                                    # or create your own palette through interpolation,
                                    # like Palette(["#003566", "#ffc300"], 5)
}

Chart(options, width="60%").display()
```

### Primitives
Use the pre-configured classes for common visualizations, and optionally override any default styling of the class.

```python
from notecharts import Line

Line(
    x=["Mon", "Tue", "Wed", "Thu", "Fri"],
    y={
        "Product A": [120, 200, 150, 220, 280],
        "Product B": [180, 160, 200, 240, 290],
        "Product C": [160, 120, 140, 190, 250]
    },
    title="Weekly Sales",
    palette="agGrnYl",
    width="650px",
    font="Elms Sans",
    options= {
        "legend": {"itemGap": 25} # Override class defaults
    }
).display()
```

#### With DataFrames

All pre-built charts support direct DataFrame integration without manual column extraction:

```python
import pandas as pd
from notecharts import Bar

df = pd.DataFrame({
    'day': ['Mon','Tue', 'Wed', 'Thu', 'Fri'],
    'product_a': [120, 200, 150, 220, 280],
    'product_b': [180, 160, 200, 240, 290],
    'product_c': [160, 120, 140, 190, 250]
})

Bar(
    dataframe = df,
    x = 'day',
    y = {'Product A': 'product_a', 'Product B': 'product_b', 'Product C': 'product_c'},
    width = "650px",
    font = "Josefin Sans",
    palette = {
        "palette": "Plasma",
        "saturation": 0.75          # Customize the palette
    }
).display()
```

## Disclaimer

- **Security:** Use of `JSCode` allows for arbitrary JavaScript execution in the browser/notebook context. Always ensure you are passing trusted code and data to your charts.
- **Connectivity:** This library is lightweight because it fetches the ECharts, ECharts-GL and fflate (for data decompression) minified code from `cdn.jsdelivr.net` at runtime, so an active internet connection is required to render charts for the first time. It is then cached in the browser/IDE context and subsequent renders can work offline.

## License & Attribution

- **notecharts** is licensed under the [MIT License](LICENSE).
- **Apache ECharts**: This library is a wrapper for [Apache ECharts](https://echarts.apache.org/en/index.html) which is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). 
- Apache ECharts, ECharts, Apache, the Apache feather, and the Apache ECharts project logo are either registered trademarks or trademarks of the Apache Software Foundation.
- Part of the [![Featured on Awesome README](https://awesome.re/badge-flat.svg)](https://github.com/matiassingers/awesome-readme) project.

## References
See the [ECharts gallery](https://echarts.apache.org/examples/en/index.html) for bespoke examples, or the [official docs](https://echarts.apache.org/en/option.html) for an in-depth explanation of features and how to use them.
