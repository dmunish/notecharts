(function() {

    // ── wait for the div to exist in the DOM ──────────────────────────
    function waitForDom(id, cb) {
        var dom = document.getElementById(id);
        if (dom) { cb(dom); return; }
        var observer = new MutationObserver(function() {
            var el = document.getElementById(id);
            if (el) { observer.disconnect(); cb(el); }
        });
        observer.observe(document.body || document.documentElement, {
            childList: true, subtree: true
        });
        var attempts = 0;
        var poll = setInterval(function() {
            var el = document.getElementById(id);
            if (el) { clearInterval(poll); observer.disconnect(); cb(el); return; }
            if (++attempts > 100) {
                clearInterval(poll); observer.disconnect();
                console.error('ECharts wrapper: #__CHART_ID__ never appeared in DOM');
            }
        }, 100);
    }

    // ── Decompress and parse options ────────────────────────────────

    function decodeZ85(str) {
        var alpha = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-:+=^!/*?&<>()[]{}@%$#';
        var table = {};
        for (var i = 0; i < 85; i++) table[alpha[i]] = i;

        var pad = (5 - str.length % 5) % 5;
        for (var i = 0; i < pad; i++) str += '\0';

        var outLen = Math.floor(str.length / 5) * 4 - pad;
        var out = new Uint8Array(outLen);
        var oi = 0;
        for (var i = 0; i < str.length; i += 5) {
            var n = ((((table[str[i]] * 85 + table[str[i+1]]) * 85
                     + table[str[i+2]]) * 85 + table[str[i+3]]) * 85
                     + table[str[i+4]]);
            if (oi < outLen) out[oi++] = (n >>> 24) & 255;
            if (oi < outLen) out[oi++] = (n >>> 16) & 255;
            if (oi < outLen) out[oi++] = (n >>> 8) & 255;
            if (oi < outLen) out[oi++] = n & 255;
        }
        return out;
    }

    function readVarint(bytes, offset) {
        var result = 0, factor = 1;
        while (true) {
            var b = bytes[offset++];
            result += (b & 0x7f) * factor;
            if (!(b & 0x80)) break;
            factor *= 128;
        }
        return { value: (result >>> 1) ^ (-(result & 1)), offset: offset };
    }

    function decodeColumnarTable(bytes, offset, ncols, nrows, format, keys) {
        var columns = [];
        for (var c = 0; c < ncols; c++) {
            var type = bytes[offset++];
            var col = [];
            if (type === 0) {
                var r = readVarint(bytes, offset);
                col.push(r.value); offset = r.offset;
                for (var i = 1; i < nrows; i++) {
                    r = readVarint(bytes, offset);
                    col.push(col[i - 1] + r.value);
                    offset = r.offset;
                }
            } else if (type === 1) {
                var slice = bytes.slice(offset, offset + nrows * 8);
                var view = new DataView(slice.buffer);
                for (var i = 0; i < nrows; i++) {
                    col.push(view.getFloat64(i * 8, true));
                }
                offset += nrows * 8;
            } else if (type === 2) {
                var nstrings = bytes[offset] | (bytes[offset + 1] << 8);
                offset += 2;
                var strings = [];
                for (var i = 0; i < nstrings; i++) {
                    var slen = bytes[offset] | (bytes[offset + 1] << 8);
                    offset += 2;
                    strings.push(new TextDecoder().decode(
                        bytes.slice(offset, offset + slen)));
                    offset += slen;
                }
                for (var i = 0; i < nrows; i++) {
                    var rr = readVarint(bytes, offset);
                    col.push(strings[rr.value]);
                    offset = rr.offset;
                }
            }
            columns.push(col);
        }

        var rows = [];
        if (format === 2) {
            for (var r = 0; r < nrows; r++) {
                var row = {};
                for (var c = 0; c < ncols; c++) {
                    row[keys[c]] = columns[c][r];
                }
                rows.push(row);
            }
        } else {
            for (var r = 0; r < nrows; r++) {
                var row = [];
                for (var c = 0; c < ncols; c++) {
                    row.push(columns[c][r]);
                }
                rows.push(row);
            }
        }
        return { rows: rows, offset: offset };
    }

    function rehydrateColumnar(obj, blob) {
        if (!blob || blob.length === 0) return;
        var nTables = blob[0] | (blob[1] << 8);
        var tables = [];
        for (var i = 0; i < nTables; i++) {
            var off = 2 + i * 4;
            var dataStart = blob[off] | (blob[off + 1] << 8)
                          | (blob[off + 2] << 16) | (blob[off + 3] << 24);
            var format = blob[dataStart];
            var pos = dataStart + 1;
            var ncols = blob[pos++];
            var keys = [];
            if (format === 2) {
                for (var k = 0; k < ncols; k++) {
                    var klen = blob[pos] | (blob[pos + 1] << 8);
                    pos += 2;
                    keys.push(new TextDecoder().decode(blob.slice(pos, pos + klen)));
                    pos += klen;
                }
            }
            var nrows = blob[pos] | (blob[pos + 1] << 8)
                      | (blob[pos + 2] << 16) | (blob[pos + 3] << 24);
            var result = decodeColumnarTable(blob, pos + 4, ncols, nrows, format, keys);
            tables.push(result.rows);
        }
        var re = /^@@C(\d+)@@$/;
        function walk(o) {
            if (Array.isArray(o)) {
                for (var j = 0; j < o.length; j++) walk(o[j]);
            } else if (o && typeof o === 'object') {
                var keys = Object.keys(o);
                for (var k = 0; k < keys.length; k++) {
                    var v = o[keys[k]];
                    if (typeof v === 'string') {
                        var m = v.match(re);
                        if (m) {
                            var idx = parseInt(m[1], 10);
                            if (idx < tables.length) o[keys[k]] = tables[idx];
                        }
                    } else {
                        walk(v);
                    }
                }
            }
        }
        walk(obj);
    }

    function parseOptions(rawOptions, format, fzstd) {
        var finalOptions;
        try {
            if (format === 'none') {
                finalOptions = rawOptions;
            } else if (format === 'z85' || format === 'columnar') {
                if (!fzstd) {
                    console.error('ECharts wrapper: fzstd not available');
                    return null;
                }
                var bytes = decodeZ85(rawOptions);
                var decompressed = fzstd.decompress(bytes);
                if (format === 'columnar') {
                    var jsonLen = decompressed[0] | (decompressed[1] << 8)
                                | (decompressed[2] << 16) | (decompressed[3] << 24);
                    var jsonBytes = decompressed.slice(4, 4 + jsonLen);
                    var blob = decompressed.slice(4 + jsonLen);
                    var optionsString = new TextDecoder().decode(jsonBytes);
                    finalOptions = new Function('return ' + optionsString)();
                    rehydrateColumnar(finalOptions, blob);
                } else {
                    var optionsString = new TextDecoder().decode(decompressed);
                    finalOptions = new Function('return ' + optionsString)();
                }
            } else {
                console.error('ECharts wrapper: unknown compress format:', format);
                return null;
            }
            return finalOptions;
        } catch (e) {
            console.error('ECharts wrapper: Error parsing options:', e);
            console.error('  format:', format);
            console.error('  fzstd available:', !!fzstd);
            if (e.stack) console.error('  Stack:', e.stack);
            return null;
        }
    }

    // ── chart init ─────
    function initChart(ec, fzstd) {
        waitForDom('__CHART_ID__', function(dom) {
            var chart = ec.init(dom, '__THEME__', {
                renderer: '__RENDERER__', devicePixelRatio: __DEVICE_PIXEL_RATIO__
            });

            var rawOptions = __OPTIONS_DATA__;
            var format = '__COMPRESS_FORMAT__';
            var options = parseOptions(rawOptions, format, fzstd);

            if (!options) {
                console.error('ECharts wrapper: Failed to parse options');
                return;
            }

            // Register maps if provided
            if (__HAS_MAPS__) {
                if (__MAPS_COMPRESSED__) {
                    var mapBytes = decodeZ85(__MAPS_DATA__);
                    var mapDecompressed = fzstd.decompress(mapBytes);
                    var maps = new Function('return ' + new TextDecoder().decode(mapDecompressed))();
                } else {
                    var maps = __MAPS_DATA__;
                }
                Object.entries(maps).forEach(function([name, data]) {
                    ec.registerMap(name, data);
                });
            }
            
            chart.setOption(options);

            if ('__MODE__' === 'image') {
                setTimeout(function () {
                    try {
                        var dataURL = chart.getDataURL({
                            type: 'png',
                            pixelRatio: __DEVICE_PIXEL_RATIO__ || 1,
                            backgroundColor: (options && options.backgroundColor) || '#fff'
                        });
                        var img = document.createElement('img');
                        img.src = dataURL;
                        img.style.width = dom.style.width || '100%';
                        img.style.height = 'auto';
                        img.style.maxWidth = '100%';
                        dom.parentNode.replaceChild(img, dom);
                        chart.dispose();
                    } catch (e) {
                        console.error('ECharts wrapper: image capture failed', e);
                    }
                }, 10);
            } else {
                window.addEventListener('resize', function () { chart.resize(); });
            }
        });
    }

    // ── Check if echarts and fzstd are already loaded ─────────────────
    function modulesReady(cb) {
        var needsFzstd = '__COMPRESS_FORMAT__' !== 'none' || __MAPS_COMPRESSED__;

        if (typeof window.echarts !== 'undefined') {
            if (needsFzstd && typeof window.fzstd === 'undefined') {
                return false;
            }
            cb(window.echarts, window.fzstd);
            return;
        }
        if (typeof require !== 'undefined' && typeof require.config === 'function') {
            if (require.defined && (require.defined('echarts') || require.defined('echarts-gl'))) {
                if (needsFzstd) {
                    if (typeof window.fzstd === 'undefined') {
                        return false;
                    }
                    require(['echarts'], function(ec) {
                        cb(ec, window.fzstd);
                    });
                    return;
                } else {
                    require(['echarts'], function(ec) {
                        cb(ec, undefined);
                    });
                    return;
                }
            }
        }
        return false;
    }

    // ── plain <script> loader (Colab / plain Jupyter) ─────────────────
    function loadScript(url, cb) {
        var s = document.createElement('script');
        s.src = url;
        s.onload = cb;
        s.onerror = function() { console.error('ECharts wrapper: failed to load ' + url); };
        document.head.appendChild(s);
    }

    function loadViaScript() {
        var needsFzstd = '__COMPRESS_FORMAT__' !== 'none' || __MAPS_COMPRESSED__;
        if (typeof window.echarts !== 'undefined') {
            if (needsFzstd && typeof window.fzstd === 'undefined') {
                loadScript('https://cdn.jsdelivr.net/npm/fzstd@0.1.1/umd/index.js', function() {
                    initChart(window.echarts, window.fzstd);
                });
            } else {
                initChart(window.echarts, window.fzstd || undefined);
            }
            return;
        }
        loadScript('https://cdn.jsdelivr.net/npm/echarts@6.1.0/dist/echarts.min.js', function() {
            loadScript('https://cdn.jsdelivr.net/npm/echarts-gl@2.1.0/dist/echarts-gl.min.js', function() {
                if (needsFzstd && typeof window.fzstd === 'undefined') {
                    loadScript('https://cdn.jsdelivr.net/npm/fzstd@0.1.1/umd/index.js', function() {
                        initChart(window.echarts, window.fzstd);
                    });
                } else {
                    initChart(window.echarts, window.fzstd || undefined);
                }
            });
        });
    }

    // ── RequireJS loader (VS Code webview) ────────────────────────────
    function loadViaRequire() {
        var needsFzstd = '__COMPRESS_FORMAT__' !== 'none' || __MAPS_COMPRESSED__;
        var paths = {
            'echarts': 'https://cdn.jsdelivr.net/npm/echarts@6.1.0/dist/echarts.min',
            'echarts-gl': 'https://cdn.jsdelivr.net/npm/echarts-gl@2.1.0/dist/echarts-gl.min'
        };

        require.config({ paths: paths });

        function doLoadEcharts() {
            require(['echarts'], function(ec) {
                require(['echarts-gl'], function() {
                    initChart(ec, window.fzstd);
                });
            }, function(err) {
                console.error('ECharts wrapper: RequireJS failed to load echarts modules:', err);
            });
        }

        if (needsFzstd && typeof window.fzstd === 'undefined') {
            fetch('https://cdn.jsdelivr.net/npm/fzstd@0.1.1/umd/index.js')
                .then(function(res) { return res.text(); })
                .then(function(text) {
                    var wrapper = new Function('module', 'exports', 'define', text);
                    wrapper(undefined, undefined, undefined);
                    doLoadEcharts();
                })
                .catch(function(err) {
                    console.error('ECharts wrapper: Failed to fetch fzstd:', err);
                });
        } else {
            doLoadEcharts();
        }
    }

    // ── font gate → then load echarts ─────────────────────────────────
    function loadEchartsAndInit() {
        if (modulesReady(initChart) !== false) {
            return;
        }
        if (typeof require !== 'undefined' && typeof require.config === 'function') {
            loadViaRequire();
        } else {
            loadViaScript();
        }
    }

    if (__HAS_FONTS__) {
        if (document.fonts && document.fonts.ready) {
            document.fonts.ready.then(loadEchartsAndInit);
        } else {
            loadEchartsAndInit();
        }
    } else {
        loadEchartsAndInit();
    }
})();
