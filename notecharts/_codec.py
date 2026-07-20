from __future__ import annotations

import struct
from dataclasses import dataclass
from typing import Any

import zstandard as zstd

# ═══════════════════════════════════════════════════════════════════════
# Z85 text encoding
# ═══════════════════════════════════════════════════════════════════════

_Z85_ENC = b'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-:+=^!/*?&<>()[]{}@%$#'


def z85_encode(data: bytes) -> str:
    chars: list[str] = []
    i = 0
    while i + 4 <= len(data):
        n = int.from_bytes(data[i : i + 4], 'big')
        for j in range(4, -1, -1):
            chars.append(chr(_Z85_ENC[(n // (85 ** j)) % 85]))
        i += 4
    rem = len(data) - i
    if rem:
        n = int.from_bytes(data[i:], 'big')
        ndigits = rem + 1
        for j in range(ndigits - 1, -1, -1):
            chars.append(chr(_Z85_ENC[(n // (85 ** j)) % 85]))
    return ''.join(chars)


# ═══════════════════════════════════════════════════════════════════════
# Columnar-binary encoding
# ═══════════════════════════════════════════════════════════════════════


def _zigzag(n: int) -> int:
    return (n << 1) ^ (n >> 63)


def _write_varint(buf: bytearray, value: int) -> None:
    zig = _zigzag(value)
    while zig > 0x7F:
        buf.append((zig & 0x7F) | 0x80)
        zig >>= 7
    buf.append(zig & 0x7F)


def _is_columnar_candidate(data: Any) -> bool:
    if not isinstance(data, list) or len(data) < 4:
        return False
    if all(isinstance(x, (int, float)) for x in data):
        return True
    if isinstance(data[0], list) and data[0] and isinstance(data[0][0], (int, float)):
        return all(isinstance(r, list) and len(r) == len(data[0]) for r in data)
    if isinstance(data[0], dict):
        keys = list(data[0].keys())
        return all(
            isinstance(item, dict) and all(k in item for k in keys)
            for item in data
        )
    return False


def extract_columnar(options: dict) -> tuple[dict, bytes]:
    tables: list[list] = []

    def _walk(obj: Any) -> None:
        if isinstance(obj, dict):
            for key in ('data', 'source'):
                if key in obj and _is_columnar_candidate(obj[key]):
                    idx = len(tables)
                    tables.append(obj[key])
                    obj[key] = f'@@C{idx}@@'
            for v in obj.values():
                _walk(v)
        elif isinstance(obj, list):
            for item in obj:
                _walk(item)

    _walk(options)
    if not tables:
        return options, b''

    blob = bytearray()
    blob.extend(struct.pack('<H', len(tables)))
    offset = 2 + 4 * len(tables)
    for t in tables:
        buf = _encode_table(t)
        blob.extend(struct.pack('<I', offset))
        offset += len(buf)
    for t in tables:
        blob.extend(_encode_table(t))
    return options, bytes(blob)


def _encode_table(data: list) -> bytearray:
    buf = bytearray()
    if all(isinstance(x, (int, float)) for x in data):
        buf.append(0)
        columns = [data]
    elif isinstance(data[0], list):
        buf.append(1)
        columns = [
            [data[r][c] for r in range(len(data))]
            for c in range(len(data[0]))
        ]
    elif isinstance(data[0], dict):
        buf.append(2)
        keys = list(data[0].keys())
        columns = [[item[k] for item in data] for k in keys]
    else:
        return bytearray()

    buf.extend(struct.pack('<B', len(columns)))
    if buf[0] == 2:
        for k in keys:
            encoded = k.encode('utf-8')
            buf.extend(struct.pack('<H', len(encoded)))
            buf.extend(encoded)
    buf.extend(struct.pack('<I', len(columns[0])))

    for col in columns:
        if all(not isinstance(x, (int, float)) or isinstance(x, bool) for x in col):
            buf.append(2)
            _encode_string_column(buf, [str(x) for x in col])
        elif all(isinstance(x, int) or (isinstance(x, float) and x == int(x)) for x in col):
            buf.append(0)
            _encode_int_column(buf, [int(x) for x in col])
        else:
            buf.append(1)
            _encode_float_column(buf, [float(x) for x in col])
    return buf


def _encode_int_column(buf: bytearray, values: list[int]) -> None:
    _write_varint(buf, values[0])
    for i in range(1, len(values)):
        _write_varint(buf, values[i] - values[i - 1])


def _encode_float_column(buf: bytearray, values: list[float]) -> None:
    for v in values:
        buf.extend(struct.pack('<d', v))


def _encode_string_column(buf: bytearray, values: list[str]) -> None:
    unique: dict[str, int] = {}
    for v in values:
        if v not in unique:
            unique[v] = len(unique)
    strings = list(unique.keys())
    buf.extend(struct.pack('<H', len(strings)))
    for s in strings:
        encoded = s.encode('utf-8')
        buf.extend(struct.pack('<H', len(encoded)))
        buf.extend(encoded)
    for v in values:
        _write_varint(buf, unique[v])


# ═══════════════════════════════════════════════════════════════════════
# Compression pipeline
# ═══════════════════════════════════════════════════════════════════════


@dataclass
class PackedPayload:
    options_js_code: str
    compress_format: str
    maps_code: str
    maps_compressed: bool


def pack_and_compress(options_json: str, columnar_blob: bytes) -> PackedPayload:
    if columnar_blob:
        packed = struct.pack('<I', len(options_json)) + options_json.encode('utf-8') + columnar_blob
        compressed = zstd.compress(packed, 6)
        return PackedPayload(
            options_js_code=f"'{z85_encode(compressed)}'",
            compress_format='columnar',
            maps_code='{}',
            maps_compressed=False,
        )
    compressed = zstd.compress(options_json.encode('utf-8'), 6)
    return PackedPayload(
        options_js_code=f"'{z85_encode(compressed)}'",
        compress_format='z85',
        maps_code='{}',
        maps_compressed=False,
    )


def compress_maps(maps_json: str) -> tuple[str, bool]:
    compressed = zstd.compress(maps_json.encode('utf-8'), 6)
    return f"'{z85_encode(compressed)}'", True
