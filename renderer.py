from __future__ import annotations

import asyncio
import base64
import urllib.parse
from contextlib import asynccontextmanager
from typing import Any

import modal
from fastapi import FastAPI, HTTPException, Response

APP_NAME = "render"
LOCAL_URL = "http://127.0.0.1:8000/render"
WIDTH = 700
HEIGHT = 500
CONTEXT_POOL_SIZE = 2
RENDER_TIMEOUT_SECONDS = 15

app = modal.App(APP_NAME)

image = (
    modal.Image.debian_slim(python_version="3.11")
    .apt_install("libglib2.0-0", "libnss3", "libnspr4", "libatk1.0-0", "libatk-bridge2.0-0", "libdbus-1-3", "libdrm2", "libxcb1", "libxkbcommon0", "libxcomposite1", "libxdamage1", "libxfixes3", "libxrandr2", "libgbm1", "libasound2")
    .pip_install("fastapi[standard]", "playwright")
    .run_commands("playwright install chromium --with-deps")
)

_GENERIC_FONTS = {
    'serif', 'sans-serif', 'monospace', 'cursive', 'fantasy',
    'system-ui', 'ui-serif', 'ui-sans-serif', 'ui-monospace',
    'ui-rounded', 'math', 'emoji', 'fangsong',
    'inherit', 'initial', 'unset',
}


def _discover_fonts(obj: Any, found: set[str] | None = None) -> set[str]:
    if found is None:
        found = set()
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == 'fontFamily':
                for name in str(value).split(','):
                    name = name.strip().strip("'\"")
                    if name and name.lower() not in _GENERIC_FONTS:
                        found.add(name)
            else:
                _discover_fonts(value, found)
    elif isinstance(obj, list):
        for item in obj:
            _discover_fonts(item, found)
    return found


def _font_link(options: dict[str, Any]) -> str:
    fonts = sorted(_discover_fonts(options))
    if not fonts:
        return ''
    params = {'family': fonts, 'display': 'swap'}
    qs = urllib.parse.urlencode(params, doseq=True)
    return f'<link href="https://fonts.googleapis.com/css2?{qs}" rel="stylesheet">'


def chart_html(
        options: dict[str, Any],
        width: int,
        height: int,
        device_pixel_ratio: int,
        theme: str,
) -> str:
    return f"""
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
    <script src="https://cdn.jsdelivr.net/npm/echarts@6.1.0/dist/echarts.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/echarts-gl@2.1.0/dist/echarts-gl.min.js"></script>
    {_font_link(options)}
    <style>html, body {{ margin: 0; }} #chart {{ width: {width}; height: {height}; }}</style>
</head>
<body>
  <div id="chart"></div>
</body>
</html>
"""


class BrowserPool:
    def __init__(self, size: int) -> None:
        self.size = size
        self.playwright = None
        self.browser = None
        self.contexts: asyncio.Queue = asyncio.Queue()

    async def start(self) -> None:
        from playwright.async_api import async_playwright

        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch()
        for _ in range(self.size):
            await self.contexts.put(await self.browser.new_context())

    async def close(self) -> None:
        while not self.contexts.empty():
            await self.contexts.get().close()
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()

    @asynccontextmanager
    async def checkout(self):
        context = await self.contexts.get()
        try:
            yield context
        finally:
            await self.contexts.put(context)

    async def render(self, request: dict[str, Any]) -> bytes:
        options = request["options"]
        width = request.get("width", f"{WIDTH}px")
        height = request.get("height", f"{HEIGHT}px")
        device_pixel_ratio = request.get("devicePixelRatio", 1)
        theme = request.get("theme", "light")
        async with self.checkout() as context:
            page = await context.new_page()
            try:
                page.set_default_timeout(RENDER_TIMEOUT_SECONDS * 1000)
                await page.set_content(
                    chart_html(options, width, height, device_pixel_ratio, theme),
                    wait_until="load",
                )
                await page.wait_for_function(
                    "typeof echarts !== 'undefined'",
                    timeout=RENDER_TIMEOUT_SECONDS * 1000,
                )
                fonts = sorted(_discover_fonts(options))
                data_url = await page.evaluate(
                    """
                    async ({options, maps, theme, devicePixelRatio, fonts}) => {
                        await Promise.all(fonts.map(font => document.fonts.load(
                            `16px "${font}"`
                        )));
                        await document.fonts.ready;
                        const chart = echarts.init(
                            document.getElementById('chart'),
                            theme,
                            {devicePixelRatio}
                        );
                        Object.entries(maps || {}).forEach(([name, data]) => {
                            echarts.registerMap(name, data);
                        });
                        const rendered = new Promise(resolve => chart.on('finished', resolve));
                        chart.setOption(options);
                        await rendered;
                        await new Promise(requestAnimationFrame);
                        chart.resize();
                        const dataURL = chart.getDataURL({
                            type: 'png',
                            pixelRatio: devicePixelRatio,
                            backgroundColor: options.backgroundColor || '#fff'
                        });
                        chart.dispose();
                        return dataURL;
                    }
                    """,
                    {
                        **request,
                        "fonts": fonts,
                    },
                )
                return base64.b64decode(data_url.split(",", 1)[1])
            finally:
                await page.close()


@app.cls(
    image=image,
    timeout=RENDER_TIMEOUT_SECONDS + 10,
    min_containers=1,
    max_containers=2,
)
@modal.concurrent(max_inputs=CONTEXT_POOL_SIZE)
class Renderer:
    @modal.enter()
    async def start(self) -> None:
        self.pool = BrowserPool(CONTEXT_POOL_SIZE)
        await self.pool.start()

    @modal.exit()
    async def stop(self) -> None:
        await self.pool.close()

    @modal.fastapi_endpoint(method="POST", label="r")
    async def render(self, request: dict[str, Any]) -> Response:
        if not isinstance(request, dict) or not isinstance(request.get("options"), dict):
            raise HTTPException(status_code=400, detail="request.options must be a JSON object")
        try:
            image = await asyncio.wait_for(
                self.pool.render(request),
                timeout=RENDER_TIMEOUT_SECONDS,
            )
        except asyncio.TimeoutError as exc:
            raise HTTPException(status_code=504, detail="chart rendering timed out") from exc
        return Response(content=image, media_type="image/png")


def create_local_app() -> FastAPI:
    pool = BrowserPool(CONTEXT_POOL_SIZE)
    @asynccontextmanager
    async def lifespan(_api: FastAPI):
        await pool.start()
        try:
            yield
        finally:
            await pool.close()

    api = FastAPI(lifespan=lifespan)

    @api.post("/render")
    async def render_local(request: dict[str, Any]) -> Response:
        if not isinstance(request, dict) or not isinstance(request.get("options"), dict):
            raise HTTPException(status_code=400, detail="request.options must be a JSON object")
        try:
            image = await asyncio.wait_for(
                pool.render(request),
                timeout=RENDER_TIMEOUT_SECONDS,
            )
        except asyncio.TimeoutError as exc:
            raise HTTPException(status_code=504, detail="chart rendering timed out") from exc
        return Response(content=image, media_type="image/png")

    return api


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(create_local_app(), host="127.0.0.1", port=8000)