import copy
import json
import requests
import urllib.parse
import uuid
from pathlib import Path
from typing import Literal, get_args

from IPython.display import HTML, Image, display

from ._codec import PackedPayload, extract_columnar, pack_and_compress, compress_maps
from ._fonts import discover_fonts
from ._serialize import JSCode, serialize_options
from .option import Option

__all__ = ['Chart', 'JSCode', 'Mode', 'Renderer', 'Theme']

RENDERER_URL = 'https://notecharts--notecharts-renderer-renderer-render.modal.run'
Renderer = Literal['canvas', 'svg']
Theme = Literal['light', 'dark']
Mode = Literal['interactive', 'static']

_HTML_TEMPLATE_FILE = Path(__file__).parent / 'chart.html'
with open(_HTML_TEMPLATE_FILE, encoding='utf-8') as _f:
    _HTML_TEMPLATE = _f.read()


def _validate_param(value: str, allowed: type, name: str) -> str:
    norm = value.strip().lower()
    if norm not in get_args(allowed):
        raise ValueError(
            f'Invalid {name} {norm!r}. Supported: {", ".join(get_args(allowed))}.'
        )
    return norm


class Chart:

    def __init__(
        self,
        options: Option,
        mode: Literal['interactive', 'static'] = 'interactive',
        width: str = '99%',
        height: str = '500px',
        renderer: Literal['canvas', 'svg'] = 'canvas',
        theme: Literal['light', 'dark'] = 'light',
        devicePixelRatio: int = 1,
        maps: dict | None = None,
        compress: bool = True,
    ):
        """
        Render an Apache ECharts figure in a Jupyter notebook.

        Google Fonts are auto-loaded for any ``fontFamily`` value found inside
        *options*.  GeoJSON maps can be registered via the *maps* parameter.

        Args:
            options: The ECharts option dictionary.
            mode: ``"interactive"`` (default) or ``"static"``.
            width: CSS width of the chart container.  Default ``"99%"``.
            height: CSS height of the chart container.  Default ``"500px"``.
            renderer: ``"canvas"`` (default) or ``"svg"``.
            theme: ``"light"`` (default) or ``"dark"``.
            devicePixelRatio: Pixel ratio for canvas rendering.  Default ``1``.
            maps: Map name → GeoJSON data.  Default ``None``.
            compress: Compress the option payload.  Default ``True``.

        Raises:
            TypeError: *options* is not a dict, or *maps* is not dict/None.
            ValueError: *renderer*, *theme*, or *mode* has an invalid value.
        """
        if not isinstance(options, dict):
            raise TypeError(
                f'Chart options must be a dictionary, got {type(options).__name__}.'
            )
        if maps is not None and not isinstance(maps, dict):
            raise TypeError(
                f'Chart maps must be a dictionary or None, got {type(maps).__name__}.'
            )

        self.mode = _validate_param(mode, Mode, 'mode')
        self.renderer = _validate_param(renderer, Renderer, 'renderer')
        self.theme = _validate_param(theme, Theme, 'theme')
        self.devicePixelRatio = int(devicePixelRatio)
        self.options = options
        self.maps = maps or {}
        self.width = width.strip() if isinstance(width, str) else str(width)
        self.height = height.strip() if isinstance(height, str) else str(height)
        self.compress = compress

        if self.theme == 'light' and 'backgroundColor' not in self.options:
            self.options['backgroundColor'] = 'white'
        self.fonts = list(discover_fonts(self.options, JSCode))

    def _make_chart_html(self, chart_id: str | None = None) -> str:
        if chart_id is None:
            chart_id = f'echart_{uuid.uuid4().hex}'

        if self.compress:
            self._compress_payload()
        else:
            self._plain_payload()

        font_link = self._build_font_link()

        return (_HTML_TEMPLATE
            .replace('__FONT_LINK__', font_link)
            .replace('__CHART_ID__', chart_id)
            .replace('__WIDTH__', self.width)
            .replace('__HEIGHT__', self.height)
            .replace('__THEME__', self.theme)
            .replace('__RENDERER__', self.renderer)
            .replace('__DEVICE_PIXEL_RATIO__', str(self.devicePixelRatio))
            .replace('__OPTIONS_DATA__', self._options_js_code)
            .replace('__COMPRESS_FORMAT__', self._compress_format)
            .replace('__HAS_MAPS__', _bool_js(self.maps))
            .replace('__MAPS_DATA__', self._maps_code)
            .replace('__MAPS_COMPRESSED__', _bool_js(self._maps_compressed))
            .replace('__HAS_FONTS__', _bool_js(self.fonts))
            .replace('__MODE__', self.mode)
        )

    def _compress_payload(self) -> None:
        working = copy.deepcopy(self.options)
        skeleton, blob = extract_columnar(working)
        options_json = serialize_options(skeleton)
        payload = pack_and_compress(options_json, blob)
        self._options_js_code = payload.options_js_code
        self._compress_format = payload.compress_format
        self._maps_compressed = False

        if self.maps:
            maps_json = json.dumps(self.maps)
            self._maps_code, self._maps_compressed = compress_maps(maps_json)
        else:
            self._maps_code = '{}'

    def _plain_payload(self) -> None:
        self._options_js_code = serialize_options(self.options)
        self._compress_format = 'none'
        self._maps_code = json.dumps(self.maps) if self.maps else '{}'
        self._maps_compressed = False

    def _build_font_link(self) -> str:
        if not self.fonts:
            return ''
        base = 'https://fonts.googleapis.com/css2'
        params = {'family': self.fonts, 'display': 'swap'}
        qs = urllib.parse.urlencode(params, doseq=True)
        return f'<link href="{base}?{qs}" rel="stylesheet">'

    def display(self) -> None:
        if self.mode == 'static':
            self._display_static()
        else:
            display(HTML(self._make_chart_html()))

    def _display_static(self) -> None:
        if _contains_jscode(self.options):
            raise ValueError('mode="static" does not support JSCode options.')
        response = requests.post(
            RENDERER_URL,
            json={
                'options': self.options,
                'maps': self.maps,
                'width': self.width,
                'height': self.height,
                'renderer': self.renderer,
                'theme': self.theme,
                'devicePixelRatio': self.devicePixelRatio,
            },
            timeout=20,
        )
        response.raise_for_status()
        display(Image(data=response.content, format='png'))

    def _repr_html_(self) -> str:
        if self.mode == 'static':
            raise RuntimeError("mode='static' must be rendered with Chart.display().")
        return self._make_chart_html()


def _bool_js(value) -> str:
    return 'true' if value else 'false'


def _contains_jscode(value) -> bool:
    if isinstance(value, JSCode):
        return True
    if isinstance(value, dict):
        return any(_contains_jscode(item) for item in value.values())
    if isinstance(value, list):
        return any(_contains_jscode(item) for item in value)
    return False