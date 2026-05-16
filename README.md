<p align="center">
  <img src="https://github.com/dmunish/notecharts/blob/main/assets/notecharts-banner.png?raw=true" height=400 width="auto" />
</p>

[![PyPI](https://img.shields.io/pypi/v/notecharts.svg?style=for-the-badge)](https://pypi.org/project/notecharts)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**notecharts** (note-charts or not-echarts) is designed for web-quality, interactive charts in Jupyter notebooks through Apache ECharts. It faithfully brings the full power of ECharts' declarative JSON-like API directly into Python notebooks, with a couple enhancements.

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

Click the charts to view how to create them.

## Key Features

- **Declarative API:** Pass a dictionary, get a chart. No complex class hierarchies to learn.
- **`JSCode` Support:** Inject raw JavaScript functions for formatters, tooltips, and custom processing logic.
- **Font Injection:** Automatically detect font declarations in your config, fetch the corresponding fonts (if available) from Google Fonts.
- **Rich Color Palettes:** Access 196 professionally-designed color palettes from [Palettable](https://jiffyclub.github.io/palettable/) and customize them.
- **Pre-built Charts:** Includes pre-built primitives like `Bar`, `Line`, `Scatter`, and `Radar` with beautiful defaults.
- **Environment Agnostic:** Works seamlessly in VS Code, JupyterLab, and Google Colab.

## Installation

```bash
pip install notecharts
```

## Usage

### The Declarative Way
If you can find an example on the [ECharts Gallery](https://echarts.apache.org/examples/en/index.html), you can run it in `notecharts`.

```python
from notecharts import Chart, JSCode, Palette

options = {
    "title": {"text": "Bar Chart"},
    "textStyle": {"fontFamily": "Josefin Sans"},  # Automatically loaded from Google Fonts
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
    "color": Palette("Plasma", 3),  # Load the Plasma palette with 3 colors
}

Chart(options, width="60%").display()
```

### The Quick Way
Use the pre-configured classes for common visualizations with sensible defaults and automatic palette generation.

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
    options= { # Override class defaults
        "textStyle": {"fontFamily": "Josefin Sans"}, 
    }
).display()
```

With palette options:

```python
from notecharts import Bar

Bar(
    x=["Jan", "Feb", "Mar", "Apr"],
    y={
        "Sales": [150, 230, 224, 310],
        "Expenses": [120, 150, 180, 210]
    },
    title="Revenue vs Expenses",
    palette={
        "palette": "BluYl",
        "saturation": 0.5,  # Adjust saturation
    },
    theme="dark",
    width="650px"
).display()
```

## Disclaimer

- **Security:** Use of `JSCode` allows for arbitrary JavaScript execution in the browser/notebook context. Always ensure you are passing trusted code and data to your charts.
- **Connectivity:** This library is ultra-lightweight because it does not ship with the ECharts binaries. It fetches them from `cdn.jsdelivr.net` at runtime, so an active internet connection is required to render charts if the libraries are not already cached.

## License & Attribution

- **notecharts** is licensed under the [MIT License](LICENSE).
- **Apache ECharts**: This library is a wrapper for [Apache ECharts](https://echarts.apache.org/en/index.html) which is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). 
- Apache ECharts, ECharts, Apache, the Apache feather, and the Apache ECharts project logo are either registered trademarks or trademarks of the Apache Software Foundation.
- Part of the [![Featured on Awesome README](https://awesome.re/badge-flat.svg)](https://github.com/matiassingers/awesome-readme) project.

## References
See the [ECharts gallery](https://echarts.apache.org/examples/en/index.html) for bespoke examples, or the [official docs](https://echarts.apache.org/en/option.html) for an in-depth explanation of features and how to use them.
