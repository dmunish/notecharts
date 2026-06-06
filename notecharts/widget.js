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
    function parseOptions(rawOptions, isCompressed, fflate) {
        var finalOptions;
        try {
            if (isCompressed) {
                if (!fflate) {
                    console.error('ECharts wrapper: fflate library not available for decompression. Available:', typeof window.fflate);
                    return null;
                }
                if (!fflate.unzlibSync) {
                    console.error('ECharts wrapper: fflate.unzlibSync not available');
                    return null;
                }
                // Decode base64 to Uint8Array
                var binaryString = window.atob(rawOptions);
                var len = binaryString.length;
                var bytes = new Uint8Array(len);
                for (var i = 0; i < len; i++) {
                    bytes[i] = binaryString.charCodeAt(i);
                }
                var decompressed = fflate.unzlibSync(bytes);
                var decoder = new TextDecoder();
                var optionsString = decoder.decode(decompressed);
                finalOptions = new Function('return ' + optionsString)();
            } else {
                // Uncompressed
                finalOptions = rawOptions;
            }
            return finalOptions;
        } catch (e) {
            console.error('ECharts wrapper: Error parsing options:', e);
            console.error('  isCompressed:', isCompressed);
            console.error('  fflate available:', !!fflate);
            if (e.stack) {
                console.error('  Stack:', e.stack);
            }
            return null;
        }
    }

    // ── chart init ─────
    function initChart(ec, fflate) {
        waitForDom('__CHART_ID__', function(dom) {
            var chart = ec.init(dom, '__THEME__', {
                renderer: '__RENDERER__', devicePixelRatio: __DEVICE_PIXEL_RATIO__
            });
            
            // Parse the options (handles both compressed and uncompressed)
            var rawOptions = __OPTIONS_DATA__;
            var isCompressed = __IS_COMPRESSED__;
            var options = parseOptions(rawOptions, isCompressed, fflate);
            
            if (!options) {
                console.error('ECharts wrapper: Failed to parse options');
                return;
            }
            
            // Register maps if provided
            if (__HAS_MAPS__) {
                var maps = __MAPS_DATA__;
                Object.entries(maps).forEach(function([name, data]) {
                    ec.registerMap(name, data);
                });
            }
            
            chart.setOption(options);
            window.addEventListener('resize', function() { chart.resize(); });
        });
    }

    // ── Check if echarts and fflate are already loaded ─────────────────
    function modulesReady(cb) {
        var needsFflate = __IS_COMPRESSED__;
        
        if (typeof window.echarts !== 'undefined') {
            if (needsFflate && typeof window.fflate === 'undefined') {
                return false;
            }
            cb(window.echarts, window.fflate);
            return;
        }
        if (typeof require !== 'undefined' && typeof require.config === 'function') {
            if (require.defined && (require.defined('echarts') || require.defined('echarts-gl'))) {
                if (needsFflate) {
                    if (typeof window.fflate === 'undefined') {
                        return false;
                    }
                    require(['echarts'], function(ec) {
                        cb(ec, window.fflate);
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
        // Not loaded yet, fall through to load it
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
        if (typeof window.echarts !== 'undefined') {
            var needsFflate = __IS_COMPRESSED__;
            if (needsFflate && typeof window.fflate === 'undefined') {
                loadScript('https://cdn.jsdelivr.net/npm/fflate@0.8.3/umd/index.js', function() {
                    initChart(window.echarts, window.fflate);
                });
            } else {
                initChart(window.echarts, window.fflate || undefined);
            }
            return;
        }
        loadScript('https://cdn.jsdelivr.net/npm/echarts@6.0.0/dist/echarts.min.js', function() {
            loadScript('https://cdn.jsdelivr.net/npm/echarts-gl@2.0.9/dist/echarts-gl.min.js', function() {
                var needsFflate = __IS_COMPRESSED__;
                if (needsFflate && typeof window.fflate === 'undefined') {
                    loadScript('https://cdn.jsdelivr.net/npm/fflate@0.8.3/umd/index.js', function() {
                        initChart(window.echarts, window.fflate);
                    });
                } else {
                    initChart(window.echarts, window.fflate || undefined);
                }
            });
        });
    }

    // ── RequireJS loader (VS Code webview) ────────────────────────────
    function loadViaRequire() {
        var needsFflate = __IS_COMPRESSED__;
        var paths = {
            'echarts': 'https://cdn.jsdelivr.net/npm/echarts@6.1.0/dist/echarts.min',
            'echarts-gl': 'https://cdn.jsdelivr.net/npm/echarts-gl@2.1.0/dist/echarts-gl.min'
        };
        
        require.config({ paths: paths });
        
        function doLoadEcharts() {
            require(['echarts'], function(ec) {
                require(['echarts-gl'], function() {
                    initChart(ec, window.fflate);
                });
            }, function(err) {
                console.error('ECharts wrapper: RequireJS failed to load echarts modules:', err);
            });
        }

        if (needsFflate && typeof window.fflate === 'undefined') {
            fetch('https://cdn.jsdelivr.net/npm/fflate@0.8.2/umd/index.js')
                .then(function(res) { return res.text(); })
                .then(function(text) {
                    var wrapper = new Function('module', 'exports', 'define', text);
                    wrapper(undefined, undefined, undefined);
                    doLoadEcharts();
                })
                .catch(function(err) {
                    console.error('ECharts wrapper: Failed to fetch fflate:', err);
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
