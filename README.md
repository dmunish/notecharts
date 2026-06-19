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

| Stacked Bar | Force Directed Graph |
|:---:|:---:|
| [![Stacked Bar](https://github.com/dmunish/notecharts/blob/main/assets/bar.png?raw=true)](https://github.com/dmunish/notecharts/blob/main/examples/line-bar.ipynb) | [![Force Directed Graph](https://github.com/dmunish/notecharts/blob/main/assets/force-directed-graph.png?raw=true)](https://github.com/dmunish/notecharts/blob/main/examples/force-directed-graph.ipynb) |
| **Geo/Map** | **3D Scatter** |
| [![Map](https://github.com/dmunish/notecharts/blob/main/assets/geo.png?raw=true)](https://github.com/dmunish/notecharts/blob/main/examples/geo.ipynb) | [![Scatter 3D](https://github.com/dmunish/notecharts/blob/main/assets/scatter-3d.png?raw=true)](https://github.com/dmunish/notecharts/blob/main/examples/scatter-3D.ipynb) |

Click the images above to view how to make them.

## Key Features

- **Declarative API:** Pass a dictionary, get a chart. No complex class hierarchies to learn.
- **Rich Color Palettes:** Browse 185 professionally-designed customizable color palettes from [Palettable](https://jiffyclub.github.io/palettable/), or make your own palettes from scratch.
- **JavaScript Support:** Inject raw JavaScript functions using `JSCode` for formatters, tooltips, and custom processing logic.
- **Code Completion:** Declare the type of the config dict as `Option` for hinting and auto-complete. 
- **Font Injection:** Automatically detect font declarations in your config, fetch the corresponding fonts (if available) from Google Fonts.
- **Templates:** Includes pre-built primitives like `Bar`, `Line`, `Scatter`, `Radar` and `Pie` with beautiful defaults.
- **Environment Agnostic:** Works seamlessly in VS Code and Google Colab.
- **Compression:** Compresses the data and config objects so the notebook doesn't balloon in size.

## Installation

```bash
pip install notecharts
```

## Usage

### Palette Browser
Use the built-in PaletteBrowser to explore available palettes, or visualize custom palettes.
```python
from notecharts import PaletteBrowser

PaletteBrowser(n=5)
```
<img src="https://github.com/dmunish/notecharts/blob/main/assets/browser.png?raw=true" alt="Palette Browser" width="100%" border="0"></img>


### Templates
Use the pre-configured temaplates for common visualizations, and optionally override any default styling of the class.

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
    palette="Spectral",
    theme="dark",
    width="650px",
    font="Elms Sans",
    options= {
        "legend": {"itemGap": 25} # Override class defaults
    }
).display()
```

#### With DataFrames

All pre-built charts support direct DataFrame integration:

```python
import pandas as pd
import random
from notecharts import Radar
 
random.seed()
 
df = pd.DataFrame({
    "Category": ["Primary", "Secondary", "Tertiary", "Quaternary"],
    "Equipment": [random.randint(4000, 6000) for _ in range(4)],
    "Materials": [random.randint(10000, 16000) for _ in range(4)],
    "Food & Beverage": [random.randint(10000, 30000) for _ in range(4)],
    "Apparel": [random.randint(10000, 40000) for _ in range(4)],
    "Tourism": [random.randint(10000, 50000) for _ in range(4)],
    "Technology": [random.randint(5000, 15000) for _ in range(4)],
})
 
Radar(
    data=df,
    series_col="Category",
    title="Radar",
    theme="dark",
    palette={
        "palette": "agSunset",
        "value": "+0.5"         # Offset-based modifications to palette
    },
    width="600px",
    font="Poppins",
).display()
```


### Full Control
Complete control over every aspect of the chart, through a beautiful, declarative API. If you can find an example on the [ECharts Gallery](https://echarts.apache.org/examples/en/index.html), you can run it in `notecharts`.

```python
from notecharts import Chart, JSCode, Palette, Option

options: Option = {
    "title": {"text": "Bar Chart"},
    "textStyle": {"fontFamily": "Josefin Sans"},    # Automatically loaded from Google Fonts
    "xAxis": {"type": "category"},
    "yAxis": {
        "axisLabel": {
            "formatter": JSCode("function(v) { return '$' + v.toLocaleString(); }")
        }
    },
    "tooltip": {
        "trigger": "axis"
    },
    "legend": {},
    "dataset": {
        "source": [
            ["Product", "Sales", "Expenses", "Profit"],
            ["Mon", 120, 80, 40],
            ["Tue", 150, 100, 50],
            ["Wed", 200, 120, 80],
            ["Thurs", 180, 110, 70],
            ["Fri", 220, 140, 80],
        ]
    },

    "series": [
        {"name": "Sales", "type": "bar"},
        {"name": "Expenses", "type": "bar"},
        {"name": "Profit", "type": "bar"}
    ],
    "color": Palette("Bamako", 3)   # Load n colors from any palette,
                                    # or create your own palette through interpolation,
                                    # like Palette(["#003566", "#ffc300"], 5)
}

Chart(options, width="700px").display()
```

## Disclaimer

- **Security:** Use of `JSCode` allows for arbitrary JavaScript execution in the browser/notebook context. Always ensure you are passing trusted code and data to your charts.
- **Connectivity:** This library is lightweight because it fetches the ECharts, ECharts-GL and fflate (for data decompression) minified code from `cdn.jsdelivr.net` at runtime, so an active internet connection is required to render charts for the first time. These are then cached in the browser/IDE context and subsequent renders can work offline.

## License & Attribution

- **notecharts** is licensed under the [MIT License](LICENSE).
- **Apache ECharts**: This library is a wrapper for [Apache ECharts](https://echarts.apache.org/en/index.html) which is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). 
- Apache ECharts, ECharts, Apache, the Apache feather, and the Apache ECharts project logo are either registered trademarks or trademarks of the Apache Software Foundation.
- Part of the [![Featured on Awesome README](https://awesome.re/badge-flat.svg)](https://github.com/matiassingers/awesome-readme) project.

## Links
- [Official Docs](https://echarts.apache.org/en/option.html)
- [ECharts Official Gallery](https://echarts.apache.org/examples/en/index.html)
- [Demo notebook on Colab](https://colab.research.google.com/drive/16kv-MJ4yuTcnSDQelMJm8QyDiaHJuEFz)
- [Community Gallery (CN)](https://www.isqqw.com/)