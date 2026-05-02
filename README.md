# notecharts

[![PyPI version](https://img.shields.io/pypi/v/notecharts.svg?style=flat-square)](https://pypi.org/project/notecharts/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/notecharts.svg?style=flat-square)](https://pypi.org/project/notecharts/)

**notecharts** is an ultra-lightweight, zero-config wrapper for Apache ECharts in Jupyter environments. It brings the full power of ECharts' declarative JSON-like API directly into Python notebooks without the bloat.

## Why notecharts?

If you've used ECharts in Python before, you likely encountered two extremes:
- **pyecharts:** Powerful, but wraps the API in a deep "Pythonic" abstraction that often deviates from the official ECharts documentation, making it hard to translate JS examples to Python.
- **ipecharts:** Often lacks the interactivity or ease of use, API is buggy or unclear sometimes.

**notecharts** bridges this gap. It provides a thin layer that allows you to write ECharts options exactly as they appear in the official docs, while handling the heavy lifting of library loading, font injection, and serialization.

## Key Features

- **Declarative API:** Pass a dictionary, get a chart. No complex class hierarchies to learn.
- **`JSCode` Support:** Inject raw JavaScript functions for formatters, tooltips, and custom logic.
- **Smart Font Discovery:** Automatically detect `fontFamily` declarations in your options fetch the corresponding fonts (if available) from Google Fonts.
- **Pre-built Modern Charts:** Includes high-level classes like `Bar`, `Line`, `Scatter`, `Donut`, and `Radar` with beautiful default harmonies.
- **Environment Agnostic:** Works seamlessly in VS Code, JupyterLab, and Google Colab.

## Installation

```bash
pip install notecharts
```

## Usage

### The Declarative Way (Total Control)
If you can find an example on the [ECharts Gallery](https://echarts.apache.org/examples/en/index.html), you can run it in `notecharts`.

```python
from notecharts import Chart, JSCode

options = {
    "title": {"text": "Basic Chart"},
    "xAxis": {"data": ["Mon", "Tue", "Wed", "Thu", "Fri"]},
    "yAxis": {},
    "series": [{
        "type": "bar",
        "data": [23, 24, 18, 25, 27], # or any other object/variable
        "label": {
            "show": True,
            "formatter": JSCode("function(p) { return p.value + ' units'; }")
        }
    }],
    "textStyle": {
        "fontFamily": "Inter" # Automatically loaded from Google Fonts!
    }
}

Chart(options).display()
```

### The Quick Way (Pre-built Charts)
Use the pre-configured classes for common visualizations with aesthetic defaults.

```python
import pandas as pd
from notecharts import Bar

df = pd.DataFrame({                 # or a list-of-lists, list-of-dicts format
    "Day": ["Mon", "Tue", "Wed"],
    "Sales": [150, 230, 224]
})

Bar(df, x="Day", y="Sales", title="Weekly Sales", theme="dark").display()
```

## Important Considerations

- **Security:** Use of `JSCode` allows for arbitrary JavaScript execution in the browser/notebook context. Always ensure you are passing trusted code and data to your charts.
- **Connectivity:** This library is ultra-lightweight because it does not ship with the ECharts binaries. It fetches them from `cdn.jsdelivr.net` at runtime, so an active internet connection is required to render charts.

## License & Attribution

- **notecharts** is licensed under the [MIT License](LICENSE).
- **Apache ECharts**: This library is a wrapper for [Apache ECharts](https://echarts.apache.org/en/index.html) (incubating), which is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). 
  - *Apache ECharts, ECharts, Apache, the Apache feather, and the Apache ECharts project logo are either registered trademarks or trademarks of the Apache Software Foundation.*

## References
See the [ECharts gallery](https://echarts.apache.org/examples/en/index.html) for bespoke examples, or the [official docs](https://echarts.apache.org/en/option.html) for an in-depth exaplanation of the options available.