"""Remote rendering of chart to raster/vector bytes for ``Chart.save()``."""

from typing import Any

import requests

RENDERER_URL = 'http://127.0.0.1:8000/render'
_RENDER_TIMEOUT = 20


def render_to_bytes(
    options: dict[str, Any],
    maps: dict[str, Any],
    renderer: str,
    theme: str,
    device_pixel_ratio: int,
    width: str,
    height: str,
    format: str,
) -> bytes:
    """Render the chart to PNG/JPEG/SVG bytes via the remote renderer."""
    response = requests.post(
        RENDERER_URL,
        json={
            'options': options,
            'maps': maps,
            'width': width,
            'height': height,
            'renderer': renderer,
            'theme': theme,
            'devicePixelRatio': device_pixel_ratio,
            'format': format,
        },
        timeout=_RENDER_TIMEOUT,
    )
    response.raise_for_status()
    return response.content