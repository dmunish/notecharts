<p align="center">
  <img src="https://github.com/dmunish/notecharts/blob/main/assets/notecharts-banner.png?raw=true" height=400 width="auto" />
</p>

[![PyPI version](https://img.shields.io/pypi/v/notecharts.svg?style=flat-square)](https://pypi.org/project/notecharts/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

**notecharts** (note-charts or not-echarts) is an ultra-lightweight, zero-config wrapper for Apache ECharts in Jupyter environments. It faithfully brings the full power of ECharts' declarative JSON-like API directly into Python notebooks, with a couple enhancements.

## Why notecharts?

If you've used ECharts in Python before, you likely encountered two extremes:
- **pyecharts:** Powerful, but wraps the API in a deep "Pythonic" abstraction that often deviates from the official ECharts documentation, making it hard to translate JS examples to Python.
- **ipecharts:** Often lacks the interactivity or ease of use, API is buggy or unclear sometimes.

**notecharts** bridges this gap. It provides a thin layer that allows you to write ECharts options exactly as they appear in the official docs, while handling the heavy lifting of library loading, font injection, and serialization.

| Force Directed Graph | Multi-Line |
|:---:|:---:|
| ![Force Directed Graph](https://github.com/dmunish/notecharts/blob/main/assets/force-directed-graph.png?raw=true) | ![Multi-Line](https://github.com/dmunish/notecharts/blob/main/assets/line.png?raw=true) |
| **Geo/Map** | **3D Scatter** |
| ![Map](https://github.com/dmunish/notecharts/blob/main/assets/geo.png?raw=true) | ![Scatter 3D](https://github.com/dmunish/notecharts/blob/main/assets/scatter-3d.png?raw=true) |

## Key Features

- **Declarative API:** Pass a dictionary, get a chart. No complex class hierarchies to learn.
- **`JSCode` Support:** Inject raw JavaScript functions for formatters, tooltips, and custom logic.
- **Smart Font Discovery:** Automatically detect `fontFamily` declarations in your options fetch the corresponding fonts (if available) from Google Fonts.
- **Rich Color Palettes:** Access ~200 professionally-designed color palettes from [Palettable](https://jiffyclub.github.io/palettable/).
- **Pre-built Modern Charts:** Includes high-level classes like `Bar`, `Line`, `Scatter`, and `Radar` with beautiful defaults.
- **Environment Agnostic:** Works seamlessly in VS Code, JupyterLab, and Google Colab.

## Installation

```bash
pip install notecharts
```

## Usage

### The Declarative Way
If you can find an example on the [ECharts Gallery](https://echarts.apache.org/examples/en/index.html), you can run it in `notecharts`.

```python
from notecharts import Chart, JSCode

options = {
    "title": {"text": "Basic Chart"},
    "xAxis": {"data": ["Mon", "Tue", "Wed", "Thu", "Fri"]},
    "yAxis": {},
    "series": [{
        "type": "bar",
        "data": [23, 24, 18, 25, 27], # or any other list from outside the object
        "label": {
            "show": True,
            "formatter": JSCode("function(p) { return p.value + ' units'; }")
        }
    }],
    "color": "Viridis",  # Reference a palette by name from Palettable
    "textStyle": {
        "fontFamily": "Inter"  # Automatically load fonts from Google Fonts
    }
}

Chart(options, width = "60%", renderer = "svg").display()
```

### The Quick Way (Pre-built Charts)
Use the pre-configured classes for common visualizations with sensible defaults.

```python
from notecharts import Bar

# Simple chart with default colors
Bar(
    x=["Mon", "Tue", "Wed"],
    y={"Sales": [150, 230, 224]},
    title="Weekly Sales"
).display()
```

With a Palettable palette:

```python
# Use a named palette from Palettable
Bar(
    x=["Mon", "Tue", "Wed"],
    y={"Sales": [150, 230, 224], "Expenses": [100, 120, 140]},
    title="Weekly Sales",
    colors="Set2",  # Any palette name from the Available Palettes list
    theme="dark"
).display()
```

Or with custom colors:

```python
# Use your own color array
Bar(
    x=["Mon", "Tue", "Wed"],
    y={"Sales": [150, 230, 224]},
    colors=["#FF6B6B", "#4ECDC4"],
    title="Weekly Sales"
).display()
```

## Disclaimer

- **Security:** Use of `JSCode` allows for arbitrary JavaScript execution in the browser/notebook context. Always ensure you are passing trusted code and data to your charts.
- **Connectivity:** This library is ultra-lightweight because it does not ship with the ECharts binaries. It fetches them from `cdn.jsdelivr.net` at runtime, so an active internet connection is required to render charts if the libraries are not already cached.

## License & Attribution

- **notecharts** is licensed under the [MIT License](LICENSE).
- **Apache ECharts**: This library is a wrapper for [Apache ECharts](https://echarts.apache.org/en/index.html) which is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). 
  - *Apache ECharts, ECharts, Apache, the Apache feather, and the Apache ECharts project logo are either registered trademarks or trademarks of the Apache Software Foundation.*

## References
See the [ECharts gallery](https://echarts.apache.org/examples/en/index.html) for bespoke examples, or the [official docs](https://echarts.apache.org/en/option.html) for an in-depth explanation of features and how to use them.