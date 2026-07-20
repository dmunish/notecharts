from __future__ import annotations

from typing import Any

_GENERIC_FONTS = {
    'serif', 'sans-serif', 'monospace', 'cursive', 'fantasy',
    'system-ui', 'ui-serif', 'ui-sans-serif', 'ui-monospace',
    'ui-rounded', 'math', 'emoji', 'fangsong',
    'inherit', 'initial', 'unset',
}


def extract_font_families(value: Any, js_code_type: type | None = None) -> set[str]:
    if js_code_type is not None and isinstance(value, js_code_type):
        return set()
    if isinstance(value, str):
        candidates = [name.strip().strip("'\"") for name in value.split(',')]
    elif isinstance(value, (list, tuple)):
        candidates = []
        for item in value:
            if isinstance(item, str):
                candidates.extend(name.strip().strip("'\"") for name in item.split(','))
    else:
        return set()
    return {
        c for c in candidates
        if c and c.lower() not in _GENERIC_FONTS
    }


def discover_fonts(obj: Any, js_code_type: type | None = None, found: set[str] | None = None) -> set[str]:
    if found is None:
        found = set()
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == 'fontFamily':
                found.update(extract_font_families(value, js_code_type))
            else:
                discover_fonts(value, js_code_type, found)
    elif isinstance(obj, list):
        for item in obj:
            discover_fonts(item, js_code_type, found)
    return found
