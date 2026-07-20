from __future__ import annotations

import json
import uuid


class JSCode:
    """Wraps a raw JavaScript string to be inserted unquoted into ECharts options."""

    def __init__(self, js: str) -> None:
        self.js = js

    def __repr__(self) -> str:
        return f'JSCode({self.js!r})'


class _EChartsEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('default', self.default)
        super().__init__(*args, **kwargs)
        self.placeholders: dict[str, str] = {}

    def default(self, obj):
        if isinstance(obj, JSCode):
            placeholder = f'__JS_{uuid.uuid4().hex}__'
            self.placeholders[placeholder] = obj.js
            return placeholder
        return super().default(obj)


def serialize_options(options: dict) -> str:
    encoder = _EChartsEncoder()
    result = encoder.encode(options)
    for placeholder, js_code in encoder.placeholders.items():
        result = result.replace(f'"{placeholder}"', js_code)
    return result
