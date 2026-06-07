from __future__ import annotations
from typing import Any, Callable, Literal
from typing_extensions import TypedDict

class AngleAxisAxisLabelOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    inside: bool
    margin: int | float
    formatter: str | Callable[..., Any]
    showMinLabel: bool
    showMaxLabel: bool
    hideOverlap: bool
    customValues: Any
    color: str | list[str] | Callable[..., Any]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: AngleAxisAxisLabelRichOpts
    richInheritPlainLabel: bool

class AngleAxisAxisLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class AngleAxisAxisLineLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class AngleAxisAxisLineOpts(TypedDict, total=False):
    show: bool
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: AngleAxisAxisLineLineStyleOpts

class AngleAxisAxisPointerHandleOpts(TypedDict, total=False):
    show: bool
    icon: Any
    size: int | float
    margin: int | float
    color: str
    throttle: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class AngleAxisAxisPointerLabelOpts(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: str | Callable[..., Any]
    margin: int | float
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    padding: str
    backgroundColor: str
    borderColor: str
    borderWidth: str
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class AngleAxisAxisPointerLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class AngleAxisAxisPointerOpts(TypedDict, total=False):
    show: bool
    type: Literal["line", "shadow", "none"]
    snap: bool
    z: int | float
    label: AngleAxisAxisPointerLabelOpts
    lineStyle: AngleAxisAxisPointerLineStyleOpts
    shadowStyle: AngleAxisAxisPointerShadowStyleOpts
    triggerEmphasis: bool
    triggerTooltip: bool
    value: int | float
    status: Literal["show", "hide"]
    handle: AngleAxisAxisPointerHandleOpts

class AngleAxisAxisPointerShadowStyleOpts(TypedDict, total=False):
    color: str | list[str]
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class AngleAxisAxisTickLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class AngleAxisAxisTickOpts(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: int | float | Callable[..., Any]
    inside: bool
    length: int | float
    lineStyle: AngleAxisAxisTickLineStyleOpts
    customValues: Any

class AngleAxisDataItemOpts(TypedDict, total=False):
    value: str
    textStyle: AngleAxisDataItemTextStyleOpts

class AngleAxisDataItemTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: AngleAxisDataItemTextStyleRichOpts
    richInheritPlainLabel: bool

class AngleAxisDataItemTextStyleRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class AngleAxisMinorSplitLineLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class AngleAxisMinorSplitLineOpts(TypedDict, total=False):
    show: bool
    lineStyle: AngleAxisMinorSplitLineLineStyleOpts

class AngleAxisMinorTickLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class AngleAxisMinorTickOpts(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: AngleAxisMinorTickLineStyleOpts

class AngleAxisOpts(TypedDict, total=False):
    id: str
    polarIndex: int | float
    startAngle: int | float
    endAngle: int | float
    clockwise: bool
    type: str
    boundaryGap: bool
    containShape: bool
    min: str | int | float | Callable[..., Any]
    max: str | int | float | Callable[..., Any]
    dataMin: int | float
    dataMax: int | float
    scale: bool
    splitNumber: int | float
    minInterval: int | float
    maxInterval: int | float
    interval: int | float
    logBase: int | float
    startValue: int | float
    silent: bool
    triggerEvent: bool
    axisLine: AngleAxisAxisLineOpts
    axisTick: AngleAxisAxisTickOpts
    minorTick: AngleAxisMinorTickOpts
    axisLabel: AngleAxisAxisLabelOpts
    splitLine: AngleAxisSplitLineOpts
    minorSplitLine: AngleAxisMinorSplitLineOpts
    splitArea: AngleAxisSplitAreaOpts
    data: list[AngleAxisDataItemOpts]
    axisPointer: AngleAxisAxisPointerOpts
    tooltip: AngleAxisTooltipOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: int | float | Callable[..., Any]
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: int | float | Callable[..., Any]
    animationDurationUpdate: int | float | Callable[..., Any]
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: int | float | Callable[..., Any]
    zlevel: int | float
    z: int | float

class AngleAxisSplitAreaAreaStyleOpts(TypedDict, total=False):
    color: Any
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class AngleAxisSplitAreaOpts(TypedDict, total=False):
    interval: int | float | Callable[..., Any]
    show: bool
    areaStyle: AngleAxisSplitAreaAreaStyleOpts

class AngleAxisSplitLineLineStyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class AngleAxisSplitLineOpts(TypedDict, total=False):
    show: bool
    showMinLine: bool
    showMaxLine: bool
    interval: int | float | Callable[..., Any]
    lineStyle: AngleAxisSplitLineLineStyleOpts

class AngleAxisTooltipOpts(TypedDict, total=False):
    show: bool
    position: str
    formatter: str | Callable[..., Any]
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: AngleAxisTooltipTextStyleOpts
    extraCssText: str

class AngleAxisTooltipTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str

class AriaDecalDecalsOpts(TypedDict, total=False):
    symbol: str
    symbolSize: int | float
    symbolKeepAspect: bool
    color: str
    backgroundColor: str
    dashArrayX: int | float
    dashArrayY: int | float
    rotation: int | float
    maxTileWidth: int | float
    maxTileHeight: int | float

class AriaDecalOpts(TypedDict, total=False):
    show: bool
    decals: AriaDecalDecalsOpts

class AriaLabelDataOpts(TypedDict, total=False):
    maxCount: int | float
    allData: str
    partialData: str
    withName: str
    withoutName: str
    excludeDimensionId: Any
    separator: AriaLabelDataSeparatorOpts

class AriaLabelDataSeparatorOpts(TypedDict, total=False):
    middle: str
    end: str

class AriaLabelGeneralOpts(TypedDict, total=False):
    withTitle: str
    withoutTitle: str

class AriaLabelOpts(TypedDict, total=False):
    enabled: bool
    description: str
    general: AriaLabelGeneralOpts
    series: AriaLabelSeriesOpts
    data: AriaLabelDataOpts

class AriaLabelSeriesMultipleOpts(TypedDict, total=False):
    prefix: str
    withName: str
    withoutName: str
    separator: AriaLabelSeriesMultipleSeparatorOpts

class AriaLabelSeriesMultipleSeparatorOpts(TypedDict, total=False):
    middle: str
    end: str

class AriaLabelSeriesOpts(TypedDict, total=False):
    maxCount: int | float
    single: AriaLabelSeriesSingleOpts
    multiple: AriaLabelSeriesMultipleOpts

class AriaLabelSeriesSingleOpts(TypedDict, total=False):
    prefix: str
    withName: str
    withoutName: str

class AriaOpts(TypedDict, total=False):
    enabled: bool
    label: AriaLabelOpts
    decal: AriaDecalOpts

class AxisPointerHandleOpts(TypedDict, total=False):
    show: bool
    icon: Any
    size: int | float
    margin: int | float
    color: str
    throttle: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class AxisPointerLabelOpts(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: str | Callable[..., Any]
    margin: int | float
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    padding: str
    backgroundColor: str
    borderColor: str
    borderWidth: str
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class AxisPointerLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class AxisPointerOpts(TypedDict, total=False):
    id: str
    show: bool
    type: Literal["line", "shadow", "none"]
    snap: bool
    z: int | float
    label: AxisPointerLabelOpts
    lineStyle: AxisPointerLineStyleOpts
    shadowStyle: AxisPointerShadowStyleOpts
    triggerEmphasis: bool
    triggerTooltip: bool
    value: int | float
    status: Literal["show", "hide"]
    handle: AxisPointerHandleOpts
    link: Any
    triggerOn: Literal["mousemove", "click", "none"]

class AxisPointerShadowStyleOpts(TypedDict, total=False):
    color: str | list[str]
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class BrushOpts(TypedDict, total=False):
    id: str
    toolbox: Any
    brushLink: str
    seriesIndex: str | int | float
    geoIndex: str | int | float
    xAxisIndex: str | int | float
    yAxisIndex: str | int | float
    brushType: str
    brushMode: str
    transformable: bool
    brushStyle: dict[str, Any]
    throttleType: str
    throttleDelay: int | float
    removeOnClick: bool
    inBrush: dict[str, Any]
    outOfBrush: dict[str, Any]
    z: int | float

class CalendarDayLabelOpts(TypedDict, total=False):
    show: bool
    firstDay: int | float
    margin: int | float
    position: Literal["start", "end"]
    nameMap: Literal["EN", "ZH"]
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: CalendarDayLabelRichOpts
    richInheritPlainLabel: bool
    silent: bool

class CalendarDayLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class CalendarItemStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class CalendarMonthLabelOpts(TypedDict, total=False):
    show: bool
    align: Literal["left", "center", "right"]
    margin: int | float
    position: Literal["start", "end"]
    nameMap: Literal["EN", "ZH"]
    formatter: str | Callable[..., Any]
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: CalendarMonthLabelRichOpts
    richInheritPlainLabel: bool
    silent: bool

class CalendarMonthLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class CalendarOpts(TypedDict, total=False):
    id: str
    zlevel: int | float
    z: int | float
    left: str | int | float
    top: str | int | float
    right: str | int | float
    bottom: str | int | float
    width: str | int | float
    height: str | int | float
    range: str | int | float
    cellSize: int | float
    orient: Literal["horizontal", "vertical"]
    splitLine: CalendarSplitLineOpts
    itemStyle: CalendarItemStyleOpts
    dayLabel: CalendarDayLabelOpts
    monthLabel: CalendarMonthLabelOpts
    yearLabel: CalendarYearLabelOpts
    silent: bool

class CalendarSplitLineLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class CalendarSplitLineOpts(TypedDict, total=False):
    show: bool
    lineStyle: CalendarSplitLineLineStyleOpts

class CalendarYearLabelOpts(TypedDict, total=False):
    show: bool
    margin: int | float
    position: Literal["top", "bottom", "left", "right"]
    formatter: str | Callable[..., Any]
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: CalendarYearLabelRichOpts
    richInheritPlainLabel: bool
    silent: bool

class CalendarYearLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class DatasetOpts(TypedDict, total=False):
    id: str
    source: dict[str, Any]
    dimensions: Any
    sourceHeader: int | float | bool
    transform: Any
    fromDatasetIndex: int | float
    fromDatasetId: str
    fromTransformResult: int | float

class Geo3DColorMaterialOpts(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float

class Geo3DEmphasisItemStyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float

class Geo3DEmphasisLabelOpts(TypedDict, total=False):
    show: bool
    distance: int | float
    formatter: str | Callable[..., Any]
    textStyle: Geo3DEmphasisLabelTextStyleOpts

class Geo3DEmphasisLabelTextStyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Geo3DEmphasisOpts(TypedDict, total=False):
    label: Geo3DEmphasisLabelOpts
    itemStyle: Geo3DEmphasisItemStyleOpts

class Geo3DGroundPlaneOpts(TypedDict, total=False):
    show: bool
    color: str

class Geo3DItemStyleOpts(TypedDict, total=False):
    color: str | Callable[..., Any]
    opacity: int | float
    borderWidth: int | float
    borderColor: str

class Geo3DLabelOpts(TypedDict, total=False):
    show: bool
    distance: int | float
    formatter: str | Callable[..., Any]
    textStyle: Geo3DLabelTextStyleOpts

class Geo3DLabelTextStyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Geo3DLambertMaterialOpts(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float

class Geo3DLightAmbientCubemapOpts(TypedDict, total=False):
    texture: str
    diffuseIntensity: int | float
    specularIntensity: int | float

class Geo3DLightAmbientOpts(TypedDict, total=False):
    color: str
    intensity: int | float

class Geo3DLightMainOpts(TypedDict, total=False):
    color: str
    intensity: int | float
    shadow: bool
    shadowQuality: str
    alpha: int | float
    beta: int | float

class Geo3DLightOpts(TypedDict, total=False):
    main: Geo3DLightMainOpts
    ambient: Geo3DLightAmbientOpts
    ambientCubemap: Geo3DLightAmbientCubemapOpts

class Geo3DOpts(TypedDict, total=False):
    show: bool
    map: str
    boxWidth: int | float
    boxHeight: int | float
    boxDepth: int | float
    regionHeight: int | float
    environment: str
    groundPlane: Geo3DGroundPlaneOpts
    instancing: bool
    label: Geo3DLabelOpts
    itemStyle: Geo3DItemStyleOpts
    emphasis: Geo3DEmphasisOpts
    regions: list[Geo3DRegionsItemOpts]
    shading: str
    realisticMaterial: Geo3DRealisticMaterialOpts
    lambertMaterial: Geo3DLambertMaterialOpts
    colorMaterial: Geo3DColorMaterialOpts
    light: Geo3DLightOpts
    postEffect: Geo3DPostEffectOpts
    temporalSuperSampling: Geo3DTemporalSuperSamplingOpts
    viewControl: Geo3DViewControlOpts
    zlevel: int | float
    left: str | int | float
    top: str | int | float
    right: str | int | float
    bottom: str | int | float
    width: str | int | float
    height: str | int | float

class Geo3DPostEffectBloomOpts(TypedDict, total=False):
    enable: bool
    bloomIntensity: int | float

class Geo3DPostEffectColorCorrectionOpts(TypedDict, total=False):
    enable: bool
    lookupTexture: str
    exposure: int | float
    brightness: int | float
    contrast: int | float
    saturation: int | float

class Geo3DPostEffectDepthOfFieldOpts(TypedDict, total=False):
    enable: bool
    focalDistance: bool
    focalRange: bool
    fstop: int | float
    blurRadius: int | float

class Geo3DPostEffectFxaaOpts(TypedDict, total=False):
    enable: bool

class Geo3DPostEffectOpts(TypedDict, total=False):
    enable: bool
    bloom: Geo3DPostEffectBloomOpts
    depthOfField: Geo3DPostEffectDepthOfFieldOpts
    screenSpaceAmbientOcclusion: dict[str, Any]
    SSAO: Geo3DPostEffectSsaoOpts
    colorCorrection: Geo3DPostEffectColorCorrectionOpts
    FXAA: Geo3DPostEffectFxaaOpts

class Geo3DPostEffectSsaoOpts(TypedDict, total=False):
    enable: bool
    quality: str
    radius: int | float
    intensity: int | float

class Geo3DRealisticMaterialOpts(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float
    roughness: str | int | float
    metalness: str | int | float
    roughnessAdjust: int | float
    metalnessAdjust: int | float
    normalTexture: str

class Geo3DRegionsItemEmphasisItemStyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    borderWidth: int | float
    borderColor: str

class Geo3DRegionsItemEmphasisLabelOpts(TypedDict, total=False):
    show: bool
    distance: int | float
    formatter: str | Callable[..., Any]
    textStyle: Geo3DRegionsItemEmphasisLabelTextStyleOpts

class Geo3DRegionsItemEmphasisLabelTextStyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Geo3DRegionsItemEmphasisOpts(TypedDict, total=False):
    itemStyle: Geo3DRegionsItemEmphasisItemStyleOpts
    label: Geo3DRegionsItemEmphasisLabelOpts

class Geo3DRegionsItemItemStyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    borderWidth: int | float
    borderColor: str

class Geo3DRegionsItemLabelOpts(TypedDict, total=False):
    show: bool
    distance: int | float
    formatter: str | Callable[..., Any]
    textStyle: Geo3DRegionsItemLabelTextStyleOpts

class Geo3DRegionsItemLabelTextStyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Geo3DRegionsItemOpts(TypedDict, total=False):
    name: str
    regionHeight: int | float
    itemStyle: Geo3DRegionsItemItemStyleOpts
    label: Geo3DRegionsItemLabelOpts
    emphasis: Geo3DRegionsItemEmphasisOpts

class Geo3DTemporalSuperSamplingOpts(TypedDict, total=False):
    enable: bool

class Geo3DViewControlOpts(TypedDict, total=False):
    projection: str
    autoRotate: bool
    autoRotateDirection: str
    autoRotateSpeed: int | float
    autoRotateAfterStill: int | float
    damping: int | float
    rotateSensitivity: int | float
    zoomSensitivity: int | float
    panSensitivity: int | float
    panMouseButton: str
    rotateMouseButton: str
    distance: int | float
    minDistance: int | float
    maxDistance: int | float
    orthographicSize: int | float
    maxOrthographicSize: int | float
    minOrthographicSize: int | float
    alpha: int | float
    beta: int | float
    center: Any
    minAlpha: int | float
    maxAlpha: int | float
    minBeta: int | float
    maxBeta: int | float
    animation: bool
    animationDurationUpdate: int | float
    animationEasingUpdate: str

class GeoBlurItemStyleOpts(TypedDict, total=False):
    areaColor: str | list[str]
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class GeoBlurLabelOpts(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: str | Callable[..., Any]
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: GeoBlurLabelRichOpts
    richInheritPlainLabel: bool

class GeoBlurLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class GeoBlurOpts(TypedDict, total=False):
    label: GeoBlurLabelOpts
    itemStyle: GeoBlurItemStyleOpts

class GeoEmphasisItemStyleOpts(TypedDict, total=False):
    areaColor: str | list[str]
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class GeoEmphasisLabelOpts(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: str | Callable[..., Any]
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: GeoEmphasisLabelRichOpts
    richInheritPlainLabel: bool

class GeoEmphasisLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class GeoEmphasisOpts(TypedDict, total=False):
    disabled: bool
    focus: str
    label: GeoEmphasisLabelOpts
    itemStyle: GeoEmphasisItemStyleOpts

class GeoItemStyleOpts(TypedDict, total=False):
    areaColor: str | list[str]
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class GeoLabelOpts(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: str | Callable[..., Any]
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: GeoLabelRichOpts
    richInheritPlainLabel: bool

class GeoLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class GeoOpts(TypedDict, total=False):
    id: str
    show: bool
    map: str
    projection: GeoProjectionOpts
    center: Any
    zoom: int | float
    scaleLimit: GeoScaleLimitOpts
    roam: Literal["true", "false", "scale", "move"]
    roamTrigger: str
    aspectScale: int | float
    boundingCoords: Any
    nameMap: dict[str, Any]
    nameProperty: str
    selectedMode: str | bool
    label: GeoLabelOpts
    itemStyle: GeoItemStyleOpts
    emphasis: GeoEmphasisOpts
    select: GeoSelectOpts
    blur: GeoBlurOpts
    zlevel: int | float
    z: int | float
    left: str | int | float
    top: str | int | float
    right: str | int | float
    bottom: str | int | float
    width: str | int | float
    height: str | int | float
    layoutCenter: Any
    layoutSize: str | int | float
    preserveAspect: str | bool
    preserveAspectAlign: Literal["left", "right", "center"]
    preserveAspectVerticalAlign: Literal["top", "bottom", "middle"]
    clip: bool
    coordinateSystem: str
    coordinateSystemUsage: str
    coord: str | int | float
    calendarIndex: int | float
    calendarId: int | float
    matrixIndex: int | float
    matrixId: int | float
    regions: list[GeoRegionsItemOpts]
    silent: bool
    tooltip: GeoTooltipOpts

class GeoProjectionOpts(TypedDict, total=False):
    project: Callable[..., Any]
    unproject: Callable[..., Any]
    stream: Callable[..., Any]

class GeoRegionsItemBlurItemStyleOpts(TypedDict, total=False):
    areaColor: str | list[str]
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class GeoRegionsItemBlurLabelOpts(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: str | Callable[..., Any]
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: GeoRegionsItemBlurLabelRichOpts
    richInheritPlainLabel: bool

class GeoRegionsItemBlurLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class GeoRegionsItemBlurOpts(TypedDict, total=False):
    itemStyle: GeoRegionsItemBlurItemStyleOpts
    label: GeoRegionsItemBlurLabelOpts

class GeoRegionsItemEmphasisItemStyleOpts(TypedDict, total=False):
    areaColor: str | list[str]
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class GeoRegionsItemEmphasisLabelOpts(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: str | Callable[..., Any]
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: GeoRegionsItemEmphasisLabelRichOpts
    richInheritPlainLabel: bool

class GeoRegionsItemEmphasisLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class GeoRegionsItemEmphasisOpts(TypedDict, total=False):
    itemStyle: GeoRegionsItemEmphasisItemStyleOpts
    label: GeoRegionsItemEmphasisLabelOpts

class GeoRegionsItemItemStyleOpts(TypedDict, total=False):
    areaColor: str | list[str]
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class GeoRegionsItemLabelOpts(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: str | Callable[..., Any]
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: GeoRegionsItemLabelRichOpts
    richInheritPlainLabel: bool

class GeoRegionsItemLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class GeoRegionsItemOpts(TypedDict, total=False):
    name: str
    selected: bool
    itemStyle: GeoRegionsItemItemStyleOpts
    label: GeoRegionsItemLabelOpts
    emphasis: GeoRegionsItemEmphasisOpts
    select: GeoRegionsItemSelectOpts
    blur: GeoRegionsItemBlurOpts
    tooltip: GeoRegionsItemTooltipOpts
    silent: bool

class GeoRegionsItemSelectItemStyleOpts(TypedDict, total=False):
    areaColor: str | list[str]
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class GeoRegionsItemSelectLabelOpts(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: str | Callable[..., Any]
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: GeoRegionsItemSelectLabelRichOpts
    richInheritPlainLabel: bool

class GeoRegionsItemSelectLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class GeoRegionsItemSelectOpts(TypedDict, total=False):
    itemStyle: GeoRegionsItemSelectItemStyleOpts
    label: GeoRegionsItemSelectLabelOpts

class GeoRegionsItemTooltipOpts(TypedDict, total=False):
    show: bool
    position: str
    formatter: str | Callable[..., Any]
    valueFormatter: str
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: GeoRegionsItemTooltipTextStyleOpts
    extraCssText: str

class GeoRegionsItemTooltipTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str

class GeoScaleLimitOpts(TypedDict, total=False):
    min: int | float
    max: int | float

class GeoSelectItemStyleOpts(TypedDict, total=False):
    areaColor: str | list[str]
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class GeoSelectLabelOpts(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: str | Callable[..., Any]
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: GeoSelectLabelRichOpts
    richInheritPlainLabel: bool

class GeoSelectLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class GeoSelectOpts(TypedDict, total=False):
    disabled: bool
    label: GeoSelectLabelOpts
    itemStyle: GeoSelectItemStyleOpts

class GeoTooltipOpts(TypedDict, total=False):
    show: bool
    position: str
    formatter: str | Callable[..., Any]
    valueFormatter: str
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: GeoTooltipTextStyleOpts
    extraCssText: str

class GeoTooltipTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str

class GlobeAtmosphereOpts(TypedDict, total=False):
    show: bool
    offset: int | float
    color: str
    glowPower: int | float
    innerGlowPower: int | float

class GlobeColorMaterialOpts(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float

class GlobeLambertMaterialOpts(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float

class GlobeLayersItemOpts(TypedDict, total=False):
    show: bool
    type: str
    name: str
    blendTo: str
    intensity: int | float
    shading: str
    distance: int | float
    texture: str

class GlobeLightAmbientCubemapOpts(TypedDict, total=False):
    texture: str
    diffuseIntensity: int | float
    specularIntensity: int | float

class GlobeLightAmbientOpts(TypedDict, total=False):
    color: str
    intensity: int | float

class GlobeLightMainOpts(TypedDict, total=False):
    color: str
    intensity: int | float
    shadow: bool
    shadowQuality: str
    alpha: int | float
    beta: int | float
    time: Any

class GlobeLightOpts(TypedDict, total=False):
    main: GlobeLightMainOpts
    ambient: GlobeLightAmbientOpts
    ambientCubemap: GlobeLightAmbientCubemapOpts

class GlobeOpts(TypedDict, total=False):
    show: bool
    zlevel: int | float
    left: str | int | float
    top: str | int | float
    right: str | int | float
    bottom: str | int | float
    width: str | int | float
    height: str | int | float
    globeRadius: int | float
    globeOuterRadius: int | float
    environment: str
    baseTexture: str
    heightTexture: str
    displacementTexture: str
    displacementScale: int | float
    displacementQuality: str
    shading: str
    realisticMaterial: GlobeRealisticMaterialOpts
    lambertMaterial: GlobeLambertMaterialOpts
    colorMaterial: GlobeColorMaterialOpts
    light: GlobeLightOpts
    atmosphere: GlobeAtmosphereOpts
    postEffect: GlobePostEffectOpts
    temporalSuperSampling: GlobeTemporalSuperSamplingOpts
    viewControl: GlobeViewControlOpts
    layers: list[GlobeLayersItemOpts]

class GlobePostEffectBloomOpts(TypedDict, total=False):
    enable: bool
    bloomIntensity: int | float

class GlobePostEffectColorCorrectionOpts(TypedDict, total=False):
    enable: bool
    lookupTexture: str
    exposure: int | float
    brightness: int | float
    contrast: int | float
    saturation: int | float

class GlobePostEffectDepthOfFieldOpts(TypedDict, total=False):
    enable: bool
    focalDistance: bool
    focalRange: bool
    fstop: int | float
    blurRadius: int | float

class GlobePostEffectFxaaOpts(TypedDict, total=False):
    enable: bool

class GlobePostEffectOpts(TypedDict, total=False):
    enable: bool
    bloom: GlobePostEffectBloomOpts
    depthOfField: GlobePostEffectDepthOfFieldOpts
    screenSpaceAmbientOcclusion: dict[str, Any]
    SSAO: GlobePostEffectSsaoOpts
    colorCorrection: GlobePostEffectColorCorrectionOpts
    FXAA: GlobePostEffectFxaaOpts

class GlobePostEffectSsaoOpts(TypedDict, total=False):
    enable: bool
    quality: str
    radius: int | float
    intensity: int | float

class GlobeRealisticMaterialOpts(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float
    roughness: str | int | float
    metalness: str | int | float
    roughnessAdjust: int | float
    metalnessAdjust: int | float
    normalTexture: str

class GlobeTemporalSuperSamplingOpts(TypedDict, total=False):
    enable: bool

class GlobeViewControlOpts(TypedDict, total=False):
    projection: str
    autoRotate: bool
    autoRotateDirection: str
    autoRotateSpeed: int | float
    autoRotateAfterStill: int | float
    damping: int | float
    rotateSensitivity: int | float
    zoomSensitivity: int | float
    panSensitivity: int | float
    panMouseButton: str
    rotateMouseButton: str
    distance: int | float
    minDistance: int | float
    maxDistance: int | float
    orthographicSize: int | float
    maxOrthographicSize: int | float
    minOrthographicSize: int | float
    alpha: int | float
    beta: int | float
    center: Any
    minAlpha: int | float
    maxAlpha: int | float
    minBeta: int | float
    maxBeta: int | float
    animation: bool
    animationDurationUpdate: int | float
    animationEasingUpdate: str
    targetCoord: Any

class GraphicOpts(TypedDict, total=False):
    id: str
    elements: Any

class Grid3DAxisLabelOpts(TypedDict, total=False):
    show: bool
    margin: int | float
    interval: int | float | Callable[..., Any]
    formatter: str | Callable[..., Any]
    textStyle: Grid3DAxisLabelTextStyleOpts

class Grid3DAxisLabelTextStyleOpts(TypedDict, total=False):
    color: str | list[str] | Callable[..., Any]
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Grid3DAxisLineLineStyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Grid3DAxisLineOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    lineStyle: Grid3DAxisLineLineStyleOpts

class Grid3DAxisPointerLabelOpts(TypedDict, total=False):
    show: bool
    formatter: Callable[..., Any]
    margin: int | float
    textStyle: Grid3DAxisPointerLabelTextStyleOpts

class Grid3DAxisPointerLabelTextStyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Grid3DAxisPointerLineStyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Grid3DAxisPointerOpts(TypedDict, total=False):
    show: bool
    lineStyle: Grid3DAxisPointerLineStyleOpts
    label: Grid3DAxisPointerLabelOpts

class Grid3DAxisTickLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    opacity: int | float
    width: int | float

class Grid3DAxisTickOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    length: int | float
    lineStyle: Grid3DAxisTickLineStyleOpts

class Grid3DLightAmbientCubemapOpts(TypedDict, total=False):
    texture: str
    diffuseIntensity: int | float
    specularIntensity: int | float

class Grid3DLightAmbientOpts(TypedDict, total=False):
    color: str
    intensity: int | float

class Grid3DLightMainOpts(TypedDict, total=False):
    color: str
    intensity: int | float
    shadow: bool
    shadowQuality: str
    alpha: int | float
    beta: int | float

class Grid3DLightOpts(TypedDict, total=False):
    main: Grid3DLightMainOpts
    ambient: Grid3DLightAmbientOpts
    ambientCubemap: Grid3DLightAmbientCubemapOpts

class Grid3DOpts(TypedDict, total=False):
    show: bool
    boxWidth: int | float
    boxHeight: int | float
    boxDepth: int | float
    axisLine: Grid3DAxisLineOpts
    axisLabel: Grid3DAxisLabelOpts
    axisTick: Grid3DAxisTickOpts
    splitLine: Grid3DSplitLineOpts
    splitArea: Grid3DSplitAreaOpts
    axisPointer: Grid3DAxisPointerOpts
    environment: str
    light: Grid3DLightOpts
    postEffect: Grid3DPostEffectOpts
    temporalSuperSampling: Grid3DTemporalSuperSamplingOpts
    viewControl: Grid3DViewControlOpts
    zlevel: int | float
    left: str | int | float
    top: str | int | float
    right: str | int | float
    bottom: str | int | float
    width: str | int | float
    height: str | int | float

class Grid3DPostEffectBloomOpts(TypedDict, total=False):
    enable: bool
    bloomIntensity: int | float

class Grid3DPostEffectColorCorrectionOpts(TypedDict, total=False):
    enable: bool
    lookupTexture: str
    exposure: int | float
    brightness: int | float
    contrast: int | float
    saturation: int | float

class Grid3DPostEffectDepthOfFieldOpts(TypedDict, total=False):
    enable: bool
    focalDistance: bool
    focalRange: bool
    fstop: int | float
    blurRadius: int | float

class Grid3DPostEffectFxaaOpts(TypedDict, total=False):
    enable: bool

class Grid3DPostEffectOpts(TypedDict, total=False):
    enable: bool
    bloom: Grid3DPostEffectBloomOpts
    depthOfField: Grid3DPostEffectDepthOfFieldOpts
    screenSpaceAmbientOcclusion: dict[str, Any]
    SSAO: Grid3DPostEffectSsaoOpts
    colorCorrection: Grid3DPostEffectColorCorrectionOpts
    FXAA: Grid3DPostEffectFxaaOpts

class Grid3DPostEffectSsaoOpts(TypedDict, total=False):
    enable: bool
    quality: str
    radius: int | float
    intensity: int | float

class Grid3DSplitAreaAreaStyleOpts(TypedDict, total=False):
    color: Any

class Grid3DSplitAreaOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    areaStyle: Grid3DSplitAreaAreaStyleOpts

class Grid3DSplitLineLineStyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Grid3DSplitLineOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    lineStyle: Grid3DSplitLineLineStyleOpts

class Grid3DTemporalSuperSamplingOpts(TypedDict, total=False):
    enable: bool

class Grid3DViewControlOpts(TypedDict, total=False):
    projection: str
    autoRotate: bool
    autoRotateDirection: str
    autoRotateSpeed: int | float
    autoRotateAfterStill: int | float
    damping: int | float
    rotateSensitivity: int | float
    zoomSensitivity: int | float
    panSensitivity: int | float
    panMouseButton: str
    rotateMouseButton: str
    distance: int | float
    minDistance: int | float
    maxDistance: int | float
    orthographicSize: int | float
    maxOrthographicSize: int | float
    minOrthographicSize: int | float
    alpha: int | float
    beta: int | float
    center: Any
    minAlpha: int | float
    maxAlpha: int | float
    minBeta: int | float
    maxBeta: int | float
    animation: bool
    animationDurationUpdate: int | float
    animationEasingUpdate: str

class GridOpts(TypedDict, total=False):
    id: str
    show: bool
    zlevel: int | float
    z: int | float
    left: str | int | float
    top: str | int | float
    right: str | int | float
    bottom: str | int | float
    width: str | int | float
    height: str | int | float
    containLabel: bool
    outerBoundsMode: str
    outerBounds: GridOuterBoundsOpts
    outerBoundsContain: bool
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    tooltip: GridTooltipOpts
    coordinateSystem: str
    coordinateSystemUsage: str
    coord: str | int | float
    calendarIndex: int | float
    calendarId: int | float
    matrixIndex: int | float
    matrixId: int | float

class GridOuterBoundsOpts(TypedDict, total=False):
    left: str | int | float
    top: str | int | float
    right: str | int | float
    bottom: str | int | float
    width: str | int | float
    height: str | int | float

class GridTooltipAxisPointerCrossStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class GridTooltipAxisPointerLabelOpts(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: str | Callable[..., Any]
    margin: int | float
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    padding: str
    backgroundColor: str
    borderColor: str
    borderWidth: str
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class GridTooltipAxisPointerLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class GridTooltipAxisPointerOpts(TypedDict, total=False):
    type: Literal["none", "line", "shadow", "cross"]
    axis: str
    snap: bool
    z: int | float
    label: GridTooltipAxisPointerLabelOpts
    lineStyle: GridTooltipAxisPointerLineStyleOpts
    shadowStyle: GridTooltipAxisPointerShadowStyleOpts
    crossStyle: GridTooltipAxisPointerCrossStyleOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: int | float | Callable[..., Any]
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: int | float | Callable[..., Any]
    animationDurationUpdate: int | float | Callable[..., Any]
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: int | float | Callable[..., Any]

class GridTooltipAxisPointerShadowStyleOpts(TypedDict, total=False):
    color: str | list[str]
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class GridTooltipOpts(TypedDict, total=False):
    show: bool
    trigger: Literal["item", "axis", "none"]
    axisPointer: GridTooltipAxisPointerOpts
    position: str
    formatter: str | Callable[..., Any]
    valueFormatter: str
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: GridTooltipTextStyleOpts
    extraCssText: str

class GridTooltipTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str

class LegendDataItemItemStyleDecalOpts(TypedDict, total=False):
    symbol: str
    symbolSize: int | float
    symbolKeepAspect: bool
    color: str
    backgroundColor: str
    dashArrayX: int | float
    dashArrayY: int | float
    rotation: int | float
    maxTileWidth: int | float
    maxTileHeight: int | float

class LegendDataItemItemStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    decal: LegendDataItemItemStyleDecalOpts

class LegendDataItemLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    inactiveColor: str | list[str]
    inactiveWidth: int | float

class LegendDataItemOpts(TypedDict, total=False):
    name: str
    icon: str
    itemStyle: LegendDataItemItemStyleOpts
    lineStyle: LegendDataItemLineStyleOpts
    inactiveColor: str | list[str]
    inactiveBorderColor: str | list[str]
    inactiveBorderWidth: str | int | float
    symbolRotate: str | int | float
    textStyle: LegendDataItemTextStyleOpts

class LegendDataItemTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str

class LegendEmphasisOpts(TypedDict, total=False):
    selectorLabel: LegendEmphasisSelectorLabelOpts

class LegendEmphasisSelectorLabelOpts(TypedDict, total=False):
    show: bool
    distance: int | float
    rotate: int | float
    offset: Any
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: LegendEmphasisSelectorLabelRichOpts
    richInheritPlainLabel: bool

class LegendEmphasisSelectorLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class LegendItemStyleDecalOpts(TypedDict, total=False):
    symbol: str
    symbolSize: int | float
    symbolKeepAspect: bool
    color: str
    backgroundColor: str
    dashArrayX: int | float
    dashArrayY: int | float
    rotation: int | float
    maxTileWidth: int | float
    maxTileHeight: int | float

class LegendItemStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    decal: LegendItemStyleDecalOpts

class LegendLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    inactiveColor: str | list[str]
    inactiveWidth: int | float

class LegendOpts(TypedDict, total=False):
    type: Literal["plain", "scroll"]
    id: str
    show: bool
    zlevel: int | float
    z: int | float
    left: str | int | float
    top: str | int | float
    right: str | int | float
    bottom: str | int | float
    width: str | int | float
    height: str | int | float
    coordinateSystem: str
    coordinateSystemUsage: str
    coord: str | int | float
    calendarIndex: int | float
    calendarId: int | float
    matrixIndex: int | float
    matrixId: int | float
    orient: Literal["vertical", "horizontal"]
    align: Literal["auto", "left", "right"]
    padding: int | float
    itemGap: int | float
    itemWidth: int | float
    itemHeight: int | float
    itemStyle: LegendItemStyleOpts
    lineStyle: LegendLineStyleOpts
    symbolRotate: str | int | float
    formatter: str | Callable[..., Any]
    selectedMode: str | bool
    inactiveColor: str | list[str]
    inactiveBorderColor: str | list[str]
    inactiveBorderWidth: str | int | float
    selected: dict[str, Any]
    textStyle: LegendTextStyleOpts
    tooltip: dict[str, Any]
    icon: str
    data: list[LegendDataItemOpts]
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderRadius: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    scrollDataIndex: int | float
    pageButtonItemGap: int | float
    pageButtonGap: int | float
    pageButtonPosition: str
    pageFormatter: str | Callable[..., Any]
    pageIcons: LegendPageIconsOpts
    pageIconColor: str
    pageIconInactiveColor: str
    pageIconSize: int | float
    pageTextStyle: LegendPageTextStyleOpts
    animation: bool
    animationDurationUpdate: int | float
    emphasis: LegendEmphasisOpts
    selector: bool
    selectorLabel: LegendSelectorLabelOpts
    selectorPosition: Literal["auto", "start", "end"]
    selectorItemGap: int | float
    selectorButtonGap: int | float
    triggerEvent: bool

class LegendPageIconsOpts(TypedDict, total=False):
    horizontal: Any
    vertical: Any

class LegendPageTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str

class LegendSelectorLabelOpts(TypedDict, total=False):
    show: bool
    distance: int | float
    rotate: int | float
    offset: Any
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: LegendSelectorLabelRichOpts
    richInheritPlainLabel: bool

class LegendSelectorLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class LegendTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: LegendTextStyleRichOpts
    richInheritPlainLabel: bool

class LegendTextStyleRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class Mapbox3DColorMaterialOpts(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float

class Mapbox3DLambertMaterialOpts(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float

class Mapbox3DLightAmbientCubemapOpts(TypedDict, total=False):
    texture: str
    diffuseIntensity: int | float
    specularIntensity: int | float

class Mapbox3DLightAmbientOpts(TypedDict, total=False):
    color: str
    intensity: int | float

class Mapbox3DLightMainOpts(TypedDict, total=False):
    color: str
    intensity: int | float
    shadow: bool
    shadowQuality: str
    alpha: int | float
    beta: int | float

class Mapbox3DLightOpts(TypedDict, total=False):
    main: Mapbox3DLightMainOpts
    ambient: Mapbox3DLightAmbientOpts
    ambientCubemap: Mapbox3DLightAmbientCubemapOpts

class Mapbox3DOpts(TypedDict, total=False):
    style: str | dict[str, Any]
    center: Any
    zoom: int | float
    bearing: int | float
    pitch: int | float
    altitudeScale: int | float
    shading: str
    realisticMaterial: Mapbox3DRealisticMaterialOpts
    lambertMaterial: Mapbox3DLambertMaterialOpts
    colorMaterial: Mapbox3DColorMaterialOpts
    light: Mapbox3DLightOpts
    postEffect: Mapbox3DPostEffectOpts
    temporalSuperSampling: Mapbox3DTemporalSuperSamplingOpts

class Mapbox3DPostEffectBloomOpts(TypedDict, total=False):
    enable: bool
    bloomIntensity: int | float

class Mapbox3DPostEffectColorCorrectionOpts(TypedDict, total=False):
    enable: bool
    lookupTexture: str
    exposure: int | float
    brightness: int | float
    contrast: int | float
    saturation: int | float

class Mapbox3DPostEffectDepthOfFieldOpts(TypedDict, total=False):
    enable: bool
    focalDistance: bool
    focalRange: bool
    fstop: int | float
    blurRadius: int | float

class Mapbox3DPostEffectFxaaOpts(TypedDict, total=False):
    enable: bool

class Mapbox3DPostEffectOpts(TypedDict, total=False):
    enable: bool
    bloom: Mapbox3DPostEffectBloomOpts
    depthOfField: Mapbox3DPostEffectDepthOfFieldOpts
    screenSpaceAmbientOcclusion: dict[str, Any]
    SSAO: Mapbox3DPostEffectSsaoOpts
    colorCorrection: Mapbox3DPostEffectColorCorrectionOpts
    FXAA: Mapbox3DPostEffectFxaaOpts

class Mapbox3DPostEffectSsaoOpts(TypedDict, total=False):
    enable: bool
    quality: str
    radius: int | float
    intensity: int | float

class Mapbox3DRealisticMaterialOpts(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float
    roughness: str | int | float
    metalness: str | int | float
    roughnessAdjust: int | float
    metalnessAdjust: int | float
    normalTexture: str

class Mapbox3DTemporalSuperSamplingOpts(TypedDict, total=False):
    enable: bool

class MatrixBackgroundStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class MatrixBodyDataItemOpts(TypedDict, total=False):
    coord: Any
    coordClamp: bool
    mergeCells: bool
    value: str | int | float

class MatrixBodyItemStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class MatrixBodyLabelOpts(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: str | Callable[..., Any]
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: MatrixBodyLabelRichOpts
    richInheritPlainLabel: bool

class MatrixBodyLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class MatrixBodyOpts(TypedDict, total=False):
    data: list[MatrixBodyDataItemOpts]
    label: MatrixBodyLabelOpts
    itemStyle: MatrixBodyItemStyleOpts
    silent: bool
    cursor: str
    z2: int | float

class MatrixCornerDataItemOpts(TypedDict, total=False):
    coord: Any
    coordClamp: bool
    mergeCells: bool
    value: str | int | float

class MatrixCornerItemStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class MatrixCornerLabelOpts(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: str | Callable[..., Any]
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: MatrixCornerLabelRichOpts
    richInheritPlainLabel: bool

class MatrixCornerLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class MatrixCornerOpts(TypedDict, total=False):
    data: list[MatrixCornerDataItemOpts]
    label: MatrixCornerLabelOpts
    itemStyle: MatrixCornerItemStyleOpts
    silent: bool
    cursor: str
    z2: int | float

class MatrixOpts(TypedDict, total=False):
    id: str
    zlevel: int | float
    z: int | float
    left: str | int | float
    top: str | int | float
    right: str | int | float
    bottom: str | int | float
    width: str | int | float
    height: str | int | float
    x: MatrixXOpts
    y: MatrixYOpts
    body: MatrixBodyOpts
    corner: MatrixCornerOpts
    backgroundStyle: MatrixBackgroundStyleOpts
    borderZ2: int | float
    tooltip: dict[str, Any]
    triggerEvent: bool

class MatrixXDataItemOpts(TypedDict, total=False):
    value: str | int | float
    children: Any
    size: int | float

class MatrixXDividerLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class MatrixXItemStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class MatrixXLabelOpts(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: str | Callable[..., Any]
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: MatrixXLabelRichOpts
    richInheritPlainLabel: bool

class MatrixXLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class MatrixXLevelsItemOpts(TypedDict, total=False):
    levelSize: str | int | float

class MatrixXOpts(TypedDict, total=False):
    show: bool
    data: list[MatrixXDataItemOpts]
    length: int | float
    label: MatrixXLabelOpts
    itemStyle: MatrixXItemStyleOpts
    silent: bool
    cursor: str
    z2: int | float
    levelSize: str | int | float
    levels: list[MatrixXLevelsItemOpts]
    dividerLineStyle: MatrixXDividerLineStyleOpts

class MatrixYDataItemOpts(TypedDict, total=False):
    value: str | int | float
    children: Any
    size: int | float

class MatrixYDividerLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class MatrixYItemStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class MatrixYLabelOpts(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: str | Callable[..., Any]
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: MatrixYLabelRichOpts
    richInheritPlainLabel: bool

class MatrixYLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class MatrixYLevelsItemOpts(TypedDict, total=False):
    levelSize: str | int | float

class MatrixYOpts(TypedDict, total=False):
    show: bool
    data: list[MatrixYDataItemOpts]
    length: int | float
    label: MatrixYLabelOpts
    itemStyle: MatrixYItemStyleOpts
    silent: bool
    cursor: str
    z2: int | float
    levelSize: str | int | float
    levels: list[MatrixYLevelsItemOpts]
    dividerLineStyle: MatrixYDividerLineStyleOpts

class ParallelAxisAreaSelectStyleOpts(TypedDict, total=False):
    width: int | float
    borderWidth: int | float
    borderColor: str | list[str]
    color: str | list[str]
    opacity: int | float

class ParallelAxisAxisLabelOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    inside: bool
    rotate: int | float
    margin: int | float
    formatter: str | Callable[..., Any]
    showMinLabel: bool
    showMaxLabel: bool
    hideOverlap: bool
    customValues: Any
    color: str | list[str] | Callable[..., Any]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: ParallelAxisAxisLabelRichOpts
    richInheritPlainLabel: bool

class ParallelAxisAxisLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class ParallelAxisAxisLineLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class ParallelAxisAxisLineOpts(TypedDict, total=False):
    show: bool
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: ParallelAxisAxisLineLineStyleOpts

class ParallelAxisAxisTickLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class ParallelAxisAxisTickOpts(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: int | float | Callable[..., Any]
    inside: bool
    length: int | float
    lineStyle: ParallelAxisAxisTickLineStyleOpts
    customValues: Any

class ParallelAxisDataItemOpts(TypedDict, total=False):
    value: str
    textStyle: ParallelAxisDataItemTextStyleOpts

class ParallelAxisDataItemTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: ParallelAxisDataItemTextStyleRichOpts
    richInheritPlainLabel: bool

class ParallelAxisDataItemTextStyleRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class ParallelAxisMinorTickLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class ParallelAxisMinorTickOpts(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: ParallelAxisMinorTickLineStyleOpts

class ParallelAxisNameTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: ParallelAxisNameTextStyleRichOpts
    richInheritPlainLabel: bool

class ParallelAxisNameTextStyleRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class ParallelAxisNameTruncateOpts(TypedDict, total=False):
    maxWidth: int | float
    ellipsis: str

class ParallelAxisOpts(TypedDict, total=False):
    id: str
    dim: int | float
    parallelIndex: int | float
    realtime: bool
    areaSelectStyle: ParallelAxisAreaSelectStyleOpts
    type: str
    name: str
    nameLocation: Literal["start", "middle", "end"]
    nameTextStyle: ParallelAxisNameTextStyleOpts
    nameGap: int | float
    nameRotate: int | float
    nameTruncate: ParallelAxisNameTruncateOpts
    inverse: bool
    boundaryGap: bool
    containShape: bool
    min: str | int | float | Callable[..., Any]
    max: str | int | float | Callable[..., Any]
    dataMin: int | float
    dataMax: int | float
    scale: bool
    splitNumber: int | float
    minInterval: int | float
    maxInterval: int | float
    interval: int | float
    logBase: int | float
    startValue: int | float
    silent: bool
    triggerEvent: bool
    axisLine: ParallelAxisAxisLineOpts
    axisTick: ParallelAxisAxisTickOpts
    minorTick: ParallelAxisMinorTickOpts
    axisLabel: ParallelAxisAxisLabelOpts
    data: list[ParallelAxisDataItemOpts]
    tooltip: ParallelAxisTooltipOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: int | float | Callable[..., Any]
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: int | float | Callable[..., Any]
    animationDurationUpdate: int | float | Callable[..., Any]
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: int | float | Callable[..., Any]

class ParallelAxisTooltipOpts(TypedDict, total=False):
    show: bool
    position: str
    formatter: str | Callable[..., Any]
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: ParallelAxisTooltipTextStyleOpts
    extraCssText: str

class ParallelAxisTooltipTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str

class ParallelOpts(TypedDict, total=False):
    id: str
    zlevel: int | float
    z: int | float
    left: str | int | float
    top: str | int | float
    right: str | int | float
    bottom: str | int | float
    width: str | int | float
    height: str | int | float
    coordinateSystem: str
    coordinateSystemUsage: str
    coord: str | int | float
    calendarIndex: int | float
    calendarId: int | float
    matrixIndex: int | float
    matrixId: int | float
    layout: Literal["horizontal", "vertical"]
    axisExpandable: bool
    axisExpandCenter: int | float
    axisExpandCount: int | float
    axisExpandWidth: int | float
    axisExpandTriggerOn: Literal["click", "mousemove"]
    parallelAxisDefault: ParallelParallelAxisDefaultOpts

class ParallelParallelAxisDefaultAxisLabelOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    inside: bool
    rotate: int | float
    margin: int | float
    formatter: str | Callable[..., Any]
    showMinLabel: bool
    showMaxLabel: bool
    hideOverlap: bool
    customValues: Any
    color: str | list[str] | Callable[..., Any]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: ParallelParallelAxisDefaultAxisLabelRichOpts
    richInheritPlainLabel: bool

class ParallelParallelAxisDefaultAxisLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class ParallelParallelAxisDefaultAxisLineLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class ParallelParallelAxisDefaultAxisLineOpts(TypedDict, total=False):
    show: bool
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: ParallelParallelAxisDefaultAxisLineLineStyleOpts

class ParallelParallelAxisDefaultAxisTickLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class ParallelParallelAxisDefaultAxisTickOpts(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: int | float | Callable[..., Any]
    inside: bool
    length: int | float
    lineStyle: ParallelParallelAxisDefaultAxisTickLineStyleOpts
    customValues: Any

class ParallelParallelAxisDefaultDataItemOpts(TypedDict, total=False):
    value: str
    textStyle: ParallelParallelAxisDefaultDataItemTextStyleOpts

class ParallelParallelAxisDefaultDataItemTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: ParallelParallelAxisDefaultDataItemTextStyleRichOpts
    richInheritPlainLabel: bool

class ParallelParallelAxisDefaultDataItemTextStyleRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class ParallelParallelAxisDefaultMinorTickLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class ParallelParallelAxisDefaultMinorTickOpts(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: ParallelParallelAxisDefaultMinorTickLineStyleOpts

class ParallelParallelAxisDefaultNameTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: ParallelParallelAxisDefaultNameTextStyleRichOpts
    richInheritPlainLabel: bool

class ParallelParallelAxisDefaultNameTextStyleRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class ParallelParallelAxisDefaultNameTruncateOpts(TypedDict, total=False):
    maxWidth: int | float
    ellipsis: str

class ParallelParallelAxisDefaultOpts(TypedDict, total=False):
    type: str
    name: str
    nameLocation: Literal["start", "middle", "end"]
    nameTextStyle: ParallelParallelAxisDefaultNameTextStyleOpts
    nameGap: int | float
    nameRotate: int | float
    nameTruncate: ParallelParallelAxisDefaultNameTruncateOpts
    inverse: bool
    boundaryGap: bool
    containShape: bool
    min: str | int | float | Callable[..., Any]
    max: str | int | float | Callable[..., Any]
    dataMin: int | float
    dataMax: int | float
    scale: bool
    splitNumber: int | float
    minInterval: int | float
    maxInterval: int | float
    interval: int | float
    logBase: int | float
    startValue: int | float
    silent: bool
    triggerEvent: bool
    axisLine: ParallelParallelAxisDefaultAxisLineOpts
    axisTick: ParallelParallelAxisDefaultAxisTickOpts
    minorTick: ParallelParallelAxisDefaultMinorTickOpts
    axisLabel: ParallelParallelAxisDefaultAxisLabelOpts
    data: list[ParallelParallelAxisDefaultDataItemOpts]
    tooltip: ParallelParallelAxisDefaultTooltipOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: int | float | Callable[..., Any]
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: int | float | Callable[..., Any]
    animationDurationUpdate: int | float | Callable[..., Any]
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: int | float | Callable[..., Any]

class ParallelParallelAxisDefaultTooltipOpts(TypedDict, total=False):
    show: bool
    position: str
    formatter: str | Callable[..., Any]
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: ParallelParallelAxisDefaultTooltipTextStyleOpts
    extraCssText: str

class ParallelParallelAxisDefaultTooltipTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str

class PolarOpts(TypedDict, total=False):
    id: str
    zlevel: int | float
    z: int | float
    center: Any
    radius: str | int | float
    coordinateSystem: str
    coordinateSystemUsage: str
    coord: str | int | float
    calendarIndex: int | float
    calendarId: int | float
    matrixIndex: int | float
    matrixId: int | float
    tooltip: PolarTooltipOpts

class PolarTooltipAxisPointerCrossStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class PolarTooltipAxisPointerLabelOpts(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: str | Callable[..., Any]
    margin: int | float
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    padding: str
    backgroundColor: str
    borderColor: str
    borderWidth: str
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class PolarTooltipAxisPointerLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class PolarTooltipAxisPointerOpts(TypedDict, total=False):
    type: Literal["none", "line", "shadow", "cross"]
    axis: str
    snap: bool
    z: int | float
    label: PolarTooltipAxisPointerLabelOpts
    lineStyle: PolarTooltipAxisPointerLineStyleOpts
    shadowStyle: PolarTooltipAxisPointerShadowStyleOpts
    crossStyle: PolarTooltipAxisPointerCrossStyleOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: int | float | Callable[..., Any]
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: int | float | Callable[..., Any]
    animationDurationUpdate: int | float | Callable[..., Any]
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: int | float | Callable[..., Any]

class PolarTooltipAxisPointerShadowStyleOpts(TypedDict, total=False):
    color: str | list[str]
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class PolarTooltipOpts(TypedDict, total=False):
    show: bool
    trigger: Literal["item", "axis", "none"]
    axisPointer: PolarTooltipAxisPointerOpts
    position: str
    formatter: str | Callable[..., Any]
    valueFormatter: str
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: PolarTooltipTextStyleOpts
    extraCssText: str

class PolarTooltipTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str

class RadarAxisLabelOpts(TypedDict, total=False):
    show: bool
    rotate: int | float
    margin: int | float
    formatter: str | Callable[..., Any]
    showMinLabel: bool
    showMaxLabel: bool
    hideOverlap: bool
    customValues: Any
    color: str | list[str] | Callable[..., Any]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: RadarAxisLabelRichOpts
    richInheritPlainLabel: bool

class RadarAxisLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class RadarAxisLineLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class RadarAxisLineOpts(TypedDict, total=False):
    show: bool
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: RadarAxisLineLineStyleOpts

class RadarAxisNameOpts(TypedDict, total=False):
    show: bool
    formatter: str | Callable[..., Any]
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: RadarAxisNameRichOpts
    richInheritPlainLabel: bool

class RadarAxisNameRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class RadarAxisTickLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class RadarAxisTickOpts(TypedDict, total=False):
    show: bool
    length: int | float
    lineStyle: RadarAxisTickLineStyleOpts
    customValues: Any

class RadarIndicatorItemOpts(TypedDict, total=False):
    name: str
    max: int | float
    min: int | float
    color: str

class RadarOpts(TypedDict, total=False):
    id: str
    zlevel: int | float
    z: int | float
    center: Any
    radius: str | int | float
    coordinateSystem: str
    coordinateSystemUsage: str
    coord: str | int | float
    calendarIndex: int | float
    calendarId: int | float
    matrixIndex: int | float
    matrixId: int | float
    clockwise: bool
    startAngle: int | float
    axisName: RadarAxisNameOpts
    axisNameGap: int | float
    splitNumber: int | float
    shape: Literal["polygon", "circle"]
    scale: bool
    silent: bool
    triggerEvent: bool
    axisLine: RadarAxisLineOpts
    axisTick: RadarAxisTickOpts
    axisLabel: RadarAxisLabelOpts
    splitLine: RadarSplitLineOpts
    splitArea: RadarSplitAreaOpts
    indicator: list[RadarIndicatorItemOpts]

class RadarSplitAreaAreaStyleOpts(TypedDict, total=False):
    color: Any
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class RadarSplitAreaOpts(TypedDict, total=False):
    show: bool
    areaStyle: RadarSplitAreaAreaStyleOpts

class RadarSplitLineLineStyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class RadarSplitLineOpts(TypedDict, total=False):
    show: bool
    showMinLine: bool
    showMaxLine: bool
    lineStyle: RadarSplitLineLineStyleOpts

class RadiusAxisAxisLabelOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    inside: bool
    rotate: int | float
    margin: int | float
    formatter: str | Callable[..., Any]
    showMinLabel: bool
    showMaxLabel: bool
    hideOverlap: bool
    customValues: Any
    color: str | list[str] | Callable[..., Any]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: RadiusAxisAxisLabelRichOpts
    richInheritPlainLabel: bool

class RadiusAxisAxisLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class RadiusAxisAxisLineLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class RadiusAxisAxisLineOpts(TypedDict, total=False):
    show: bool
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: RadiusAxisAxisLineLineStyleOpts

class RadiusAxisAxisPointerHandleOpts(TypedDict, total=False):
    show: bool
    icon: Any
    size: int | float
    margin: int | float
    color: str
    throttle: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class RadiusAxisAxisPointerLabelOpts(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: str | Callable[..., Any]
    margin: int | float
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    padding: str
    backgroundColor: str
    borderColor: str
    borderWidth: str
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class RadiusAxisAxisPointerLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class RadiusAxisAxisPointerOpts(TypedDict, total=False):
    show: bool
    type: Literal["line", "shadow", "none"]
    snap: bool
    z: int | float
    label: RadiusAxisAxisPointerLabelOpts
    lineStyle: RadiusAxisAxisPointerLineStyleOpts
    shadowStyle: RadiusAxisAxisPointerShadowStyleOpts
    triggerEmphasis: bool
    triggerTooltip: bool
    value: int | float
    status: Literal["show", "hide"]
    handle: RadiusAxisAxisPointerHandleOpts

class RadiusAxisAxisPointerShadowStyleOpts(TypedDict, total=False):
    color: str | list[str]
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class RadiusAxisAxisTickLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class RadiusAxisAxisTickOpts(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: int | float | Callable[..., Any]
    inside: bool
    length: int | float
    lineStyle: RadiusAxisAxisTickLineStyleOpts
    customValues: Any

class RadiusAxisDataItemOpts(TypedDict, total=False):
    value: str
    textStyle: RadiusAxisDataItemTextStyleOpts

class RadiusAxisDataItemTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: RadiusAxisDataItemTextStyleRichOpts
    richInheritPlainLabel: bool

class RadiusAxisDataItemTextStyleRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class RadiusAxisMinorSplitLineLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class RadiusAxisMinorSplitLineOpts(TypedDict, total=False):
    show: bool
    lineStyle: RadiusAxisMinorSplitLineLineStyleOpts

class RadiusAxisMinorTickLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class RadiusAxisMinorTickOpts(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: RadiusAxisMinorTickLineStyleOpts

class RadiusAxisNameTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: RadiusAxisNameTextStyleRichOpts
    richInheritPlainLabel: bool

class RadiusAxisNameTextStyleRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class RadiusAxisNameTruncateOpts(TypedDict, total=False):
    maxWidth: int | float
    ellipsis: str

class RadiusAxisOpts(TypedDict, total=False):
    id: str
    polarIndex: int | float
    type: str
    name: str
    nameLocation: Literal["start", "middle", "end"]
    nameTextStyle: RadiusAxisNameTextStyleOpts
    nameGap: int | float
    nameRotate: int | float
    nameTruncate: RadiusAxisNameTruncateOpts
    inverse: bool
    boundaryGap: bool
    containShape: bool
    min: str | int | float | Callable[..., Any]
    max: str | int | float | Callable[..., Any]
    dataMin: int | float
    dataMax: int | float
    scale: bool
    splitNumber: int | float
    minInterval: int | float
    maxInterval: int | float
    interval: int | float
    logBase: int | float
    startValue: int | float
    silent: bool
    triggerEvent: bool
    axisLine: RadiusAxisAxisLineOpts
    axisTick: RadiusAxisAxisTickOpts
    minorTick: RadiusAxisMinorTickOpts
    axisLabel: RadiusAxisAxisLabelOpts
    splitLine: RadiusAxisSplitLineOpts
    minorSplitLine: RadiusAxisMinorSplitLineOpts
    splitArea: RadiusAxisSplitAreaOpts
    data: list[RadiusAxisDataItemOpts]
    axisPointer: RadiusAxisAxisPointerOpts
    tooltip: RadiusAxisTooltipOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: int | float | Callable[..., Any]
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: int | float | Callable[..., Any]
    animationDurationUpdate: int | float | Callable[..., Any]
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: int | float | Callable[..., Any]
    zlevel: int | float
    z: int | float

class RadiusAxisSplitAreaAreaStyleOpts(TypedDict, total=False):
    color: Any
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class RadiusAxisSplitAreaOpts(TypedDict, total=False):
    interval: int | float | Callable[..., Any]
    show: bool
    areaStyle: RadiusAxisSplitAreaAreaStyleOpts

class RadiusAxisSplitLineLineStyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class RadiusAxisSplitLineOpts(TypedDict, total=False):
    show: bool
    showMinLine: bool
    showMaxLine: bool
    interval: int | float | Callable[..., Any]
    lineStyle: RadiusAxisSplitLineLineStyleOpts

class RadiusAxisTooltipOpts(TypedDict, total=False):
    show: bool
    position: str
    formatter: str | Callable[..., Any]
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: RadiusAxisTooltipTextStyleOpts
    extraCssText: str

class RadiusAxisTooltipTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str

class SingleAxisAxisLabelOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    inside: bool
    rotate: int | float
    margin: int | float
    formatter: str | Callable[..., Any]
    showMinLabel: bool
    showMaxLabel: bool
    hideOverlap: bool
    customValues: Any
    color: str | list[str] | Callable[..., Any]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: SingleAxisAxisLabelRichOpts
    richInheritPlainLabel: bool

class SingleAxisAxisLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class SingleAxisAxisLineLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class SingleAxisAxisLineOpts(TypedDict, total=False):
    show: bool
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: SingleAxisAxisLineLineStyleOpts

class SingleAxisAxisPointerHandleOpts(TypedDict, total=False):
    show: bool
    icon: Any
    size: int | float
    margin: int | float
    color: str
    throttle: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class SingleAxisAxisPointerLabelOpts(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: str | Callable[..., Any]
    margin: int | float
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    padding: str
    backgroundColor: str
    borderColor: str
    borderWidth: str
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class SingleAxisAxisPointerLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class SingleAxisAxisPointerOpts(TypedDict, total=False):
    show: bool
    type: Literal["line", "shadow", "none"]
    snap: bool
    z: int | float
    label: SingleAxisAxisPointerLabelOpts
    lineStyle: SingleAxisAxisPointerLineStyleOpts
    shadowStyle: SingleAxisAxisPointerShadowStyleOpts
    triggerEmphasis: bool
    triggerTooltip: bool
    value: int | float
    status: Literal["show", "hide"]
    handle: SingleAxisAxisPointerHandleOpts

class SingleAxisAxisPointerShadowStyleOpts(TypedDict, total=False):
    color: str | list[str]
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class SingleAxisAxisTickLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class SingleAxisAxisTickOpts(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: int | float | Callable[..., Any]
    inside: bool
    length: int | float
    lineStyle: SingleAxisAxisTickLineStyleOpts
    customValues: Any

class SingleAxisDataItemOpts(TypedDict, total=False):
    value: str
    textStyle: SingleAxisDataItemTextStyleOpts

class SingleAxisDataItemTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: SingleAxisDataItemTextStyleRichOpts
    richInheritPlainLabel: bool

class SingleAxisDataItemTextStyleRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class SingleAxisMinorSplitLineLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class SingleAxisMinorSplitLineOpts(TypedDict, total=False):
    show: bool
    lineStyle: SingleAxisMinorSplitLineLineStyleOpts

class SingleAxisMinorTickLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class SingleAxisMinorTickOpts(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: SingleAxisMinorTickLineStyleOpts

class SingleAxisNameTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: SingleAxisNameTextStyleRichOpts
    richInheritPlainLabel: bool

class SingleAxisNameTextStyleRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class SingleAxisNameTruncateOpts(TypedDict, total=False):
    maxWidth: int | float
    ellipsis: str

class SingleAxisOpts(TypedDict, total=False):
    id: str
    zlevel: int | float
    z: int | float
    left: str | int | float
    top: str | int | float
    right: str | int | float
    bottom: str | int | float
    width: str | int | float
    height: str | int | float
    orient: str
    type: str
    name: str
    nameLocation: Literal["start", "middle", "end"]
    nameTextStyle: SingleAxisNameTextStyleOpts
    nameGap: int | float
    nameRotate: int | float
    nameTruncate: SingleAxisNameTruncateOpts
    inverse: bool
    boundaryGap: bool
    containShape: bool
    min: str | int | float | Callable[..., Any]
    max: str | int | float | Callable[..., Any]
    dataMin: int | float
    dataMax: int | float
    scale: bool
    splitNumber: int | float
    minInterval: int | float
    maxInterval: int | float
    interval: int | float
    logBase: int | float
    startValue: int | float
    silent: bool
    triggerEvent: bool
    axisLine: SingleAxisAxisLineOpts
    axisTick: SingleAxisAxisTickOpts
    minorTick: SingleAxisMinorTickOpts
    axisLabel: SingleAxisAxisLabelOpts
    splitLine: SingleAxisSplitLineOpts
    minorSplitLine: SingleAxisMinorSplitLineOpts
    splitArea: SingleAxisSplitAreaOpts
    data: list[SingleAxisDataItemOpts]
    axisPointer: SingleAxisAxisPointerOpts
    tooltip: SingleAxisTooltipOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: int | float | Callable[..., Any]
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: int | float | Callable[..., Any]
    animationDurationUpdate: int | float | Callable[..., Any]
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: int | float | Callable[..., Any]

class SingleAxisSplitAreaAreaStyleOpts(TypedDict, total=False):
    color: Any
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class SingleAxisSplitAreaOpts(TypedDict, total=False):
    interval: int | float | Callable[..., Any]
    show: bool
    areaStyle: SingleAxisSplitAreaAreaStyleOpts

class SingleAxisSplitLineLineStyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class SingleAxisSplitLineOpts(TypedDict, total=False):
    show: bool
    showMinLine: bool
    showMaxLine: bool
    interval: int | float | Callable[..., Any]
    lineStyle: SingleAxisSplitLineLineStyleOpts

class SingleAxisTooltipAxisPointerCrossStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class SingleAxisTooltipAxisPointerLabelOpts(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: str | Callable[..., Any]
    margin: int | float
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    padding: str
    backgroundColor: str
    borderColor: str
    borderWidth: str
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class SingleAxisTooltipAxisPointerLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class SingleAxisTooltipAxisPointerOpts(TypedDict, total=False):
    type: Literal["none", "line", "shadow", "cross"]
    axis: str
    snap: bool
    z: int | float
    label: SingleAxisTooltipAxisPointerLabelOpts
    lineStyle: SingleAxisTooltipAxisPointerLineStyleOpts
    shadowStyle: SingleAxisTooltipAxisPointerShadowStyleOpts
    crossStyle: SingleAxisTooltipAxisPointerCrossStyleOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: int | float | Callable[..., Any]
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: int | float | Callable[..., Any]
    animationDurationUpdate: int | float | Callable[..., Any]
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: int | float | Callable[..., Any]

class SingleAxisTooltipAxisPointerShadowStyleOpts(TypedDict, total=False):
    color: str | list[str]
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class SingleAxisTooltipOpts(TypedDict, total=False):
    show: bool
    trigger: Literal["item", "axis", "none"]
    axisPointer: SingleAxisTooltipAxisPointerOpts
    position: str
    formatter: str | Callable[..., Any]
    valueFormatter: str
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: SingleAxisTooltipTextStyleOpts
    extraCssText: str

class SingleAxisTooltipTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str

class StateAnimationOpts(TypedDict, total=False):
    duration: int | float
    easing: str

class TextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str

class ThumbnailItemStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class ThumbnailOpts(TypedDict, total=False):
    id: str
    show: bool
    zlevel: int | float
    z: int | float
    left: str | int | float
    top: str | int | float
    right: str | int | float
    bottom: str | int | float
    width: str | int | float
    height: str | int | float
    coordinateSystem: str
    coordinateSystemUsage: str
    coord: str | int | float
    calendarIndex: int | float
    calendarId: int | float
    matrixIndex: int | float
    matrixId: int | float
    itemStyle: ThumbnailItemStyleOpts
    windowStyle: ThumbnailWindowStyleOpts
    seriesIndex: int | float
    seriesId: str | int | float

class ThumbnailWindowStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class TimelineCheckpointStyleOpts(TypedDict, total=False):
    symbol: str
    symbolSize: int | float
    symbolRotate: int | float
    symbolKeepAspect: bool
    symbolOffset: Any
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    animation: bool
    animationDuration: int | float
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]

class TimelineControlStyleOpts(TypedDict, total=False):
    show: bool
    showPlayBtn: bool
    showPrevBtn: bool
    showNextBtn: bool
    itemSize: int | float
    itemGap: int | float
    position: Literal["left", "right", "top", "bottom"]
    playIcon: str
    stopIcon: str
    prevIcon: str
    nextIcon: str
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class TimelineEmphasisItemStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class TimelineEmphasisLabelOpts(TypedDict, total=False):
    show: bool
    interval: str | int | float
    rotate: Any
    formatter: str | Callable[..., Any]
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: TimelineEmphasisLabelRichOpts
    richInheritPlainLabel: bool

class TimelineEmphasisLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class TimelineEmphasisOpts(TypedDict, total=False):
    label: TimelineEmphasisLabelOpts
    itemStyle: TimelineEmphasisItemStyleOpts
    checkpointStyle: dict[str, Any]
    controlStyle: dict[str, Any]

class TimelineItemStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class TimelineLabelOpts(TypedDict, total=False):
    position: Literal["auto", "left", "right", "top", "bottom"]
    show: bool
    interval: str | int | float
    rotate: Any
    formatter: str | Callable[..., Any]
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: TimelineLabelRichOpts
    richInheritPlainLabel: bool

class TimelineLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class TimelineLineStyleOpts(TypedDict, total=False):
    show: bool
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class TimelineOpts(TypedDict, total=False):
    show: bool
    type: str
    axisType: str
    currentIndex: int | float
    autoPlay: bool
    rewind: bool
    loop: bool
    playInterval: int | float
    realtime: bool
    replaceMerge: str
    controlPosition: Literal["left", "right"]
    zlevel: int | float
    z: int | float
    left: str | int | float
    top: str | int | float
    right: str | int | float
    bottom: str | int | float
    coordinateSystem: str
    coordinateSystemUsage: str
    coord: str | int | float
    calendarIndex: int | float
    calendarId: int | float
    matrixIndex: int | float
    matrixId: int | float
    padding: int | float
    orient: Literal["horizontal", "vertical"]
    inverse: bool
    symbol: str
    symbolSize: int | float
    symbolRotate: int | float
    symbolKeepAspect: bool
    symbolOffset: Any
    lineStyle: TimelineLineStyleOpts
    label: TimelineLabelOpts
    itemStyle: TimelineItemStyleOpts
    checkpointStyle: TimelineCheckpointStyleOpts
    controlStyle: TimelineControlStyleOpts
    progress: TimelineProgressOpts
    emphasis: TimelineEmphasisOpts
    data: Any

class TimelineProgressItemStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class TimelineProgressLabelOpts(TypedDict, total=False):
    show: bool
    interval: str | int | float
    rotate: Any
    formatter: str | Callable[..., Any]
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: TimelineProgressLabelRichOpts
    richInheritPlainLabel: bool

class TimelineProgressLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class TimelineProgressLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class TimelineProgressOpts(TypedDict, total=False):
    lineStyle: TimelineProgressLineStyleOpts
    itemStyle: TimelineProgressItemStyleOpts
    label: TimelineProgressLabelOpts

class TitleOpts(TypedDict, total=False):
    id: str
    show: bool
    text: str
    link: str
    target: str
    textStyle: TitleTextStyleOpts
    subtext: str
    sublink: str
    subtarget: str
    subtextStyle: TitleSubtextStyleOpts
    textAlign: Literal["auto", "left", "center", "right"]
    textVerticalAlign: Literal["auto", "top", "middle", "bottom"]
    triggerEvent: bool
    padding: int | float
    itemGap: int | float
    zlevel: int | float
    z: int | float
    left: str | int | float
    top: str | int | float
    right: str | int | float
    bottom: str | int | float
    coordinateSystem: str
    coordinateSystemUsage: str
    coord: str | int | float
    calendarIndex: int | float
    calendarId: int | float
    matrixIndex: int | float
    matrixId: int | float
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderRadius: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class TitleSubtextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: TitleSubtextStyleRichOpts
    richInheritPlainLabel: bool

class TitleSubtextStyleRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class TitleTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: TitleTextStyleRichOpts
    richInheritPlainLabel: bool

class TitleTextStyleRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class ToolboxEmphasisIconStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    textPosition: str
    textFill: str
    textAlign: Literal["left", "center", "right"]
    textBackgroundColor: str
    textBorderRadius: int | float
    textPadding: int | float

class ToolboxEmphasisOpts(TypedDict, total=False):
    iconStyle: ToolboxEmphasisIconStyleOpts

class ToolboxFeatureBrushIconOpts(TypedDict, total=False):
    rect: str
    polygon: str
    lineX: str
    lineY: str
    keep: str
    clear: str

class ToolboxFeatureBrushOpts(TypedDict, total=False):
    type: Any
    icon: ToolboxFeatureBrushIconOpts
    title: ToolboxFeatureBrushTitleOpts

class ToolboxFeatureBrushTitleOpts(TypedDict, total=False):
    rect: str
    polygon: str
    lineX: str
    lineY: str
    keep: str
    clear: str

class ToolboxFeatureDataViewEmphasisIconStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    textPosition: str
    textFill: str
    textAlign: Literal["left", "center", "right"]
    textBackgroundColor: str
    textBorderRadius: int | float
    textPadding: int | float

class ToolboxFeatureDataViewEmphasisOpts(TypedDict, total=False):
    iconStyle: ToolboxFeatureDataViewEmphasisIconStyleOpts

class ToolboxFeatureDataViewIconStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class ToolboxFeatureDataViewOpts(TypedDict, total=False):
    show: bool
    title: str
    icon: str
    iconStyle: ToolboxFeatureDataViewIconStyleOpts
    emphasis: ToolboxFeatureDataViewEmphasisOpts
    readOnly: bool
    optionToContent: Callable[..., Any]
    contentToOption: Callable[..., Any]
    lang: Any
    backgroundColor: str
    textareaColor: str
    textareaBorderColor: str
    textColor: str
    buttonColor: str
    buttonTextColor: str

class ToolboxFeatureDataZoomBrushStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class ToolboxFeatureDataZoomEmphasisIconStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    textPosition: str
    textFill: str
    textAlign: Literal["left", "center", "right"]
    textBackgroundColor: str
    textBorderRadius: int | float
    textPadding: int | float

class ToolboxFeatureDataZoomEmphasisOpts(TypedDict, total=False):
    iconStyle: ToolboxFeatureDataZoomEmphasisIconStyleOpts

class ToolboxFeatureDataZoomIconOpts(TypedDict, total=False):
    zoom: str
    back: str

class ToolboxFeatureDataZoomIconStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class ToolboxFeatureDataZoomOpts(TypedDict, total=False):
    show: bool
    title: ToolboxFeatureDataZoomTitleOpts
    icon: ToolboxFeatureDataZoomIconOpts
    iconStyle: ToolboxFeatureDataZoomIconStyleOpts
    emphasis: ToolboxFeatureDataZoomEmphasisOpts
    filterMode: str
    xAxisIndex: int | float | bool
    yAxisIndex: int | float | bool
    brushStyle: ToolboxFeatureDataZoomBrushStyleOpts

class ToolboxFeatureDataZoomTitleOpts(TypedDict, total=False):
    zoom: str
    back: str

class ToolboxFeatureMagicTypeEmphasisIconStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    textPosition: str
    textFill: str
    textAlign: Literal["left", "center", "right"]
    textBackgroundColor: str
    textBorderRadius: int | float
    textPadding: int | float

class ToolboxFeatureMagicTypeEmphasisOpts(TypedDict, total=False):
    iconStyle: ToolboxFeatureMagicTypeEmphasisIconStyleOpts

class ToolboxFeatureMagicTypeIconOpts(TypedDict, total=False):
    line: str
    bar: str
    stack: str

class ToolboxFeatureMagicTypeIconStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class ToolboxFeatureMagicTypeOptionOpts(TypedDict, total=False):
    line: dict[str, Any]
    bar: dict[str, Any]
    stack: dict[str, Any]

class ToolboxFeatureMagicTypeOpts(TypedDict, total=False):
    show: bool
    type: Any
    title: ToolboxFeatureMagicTypeTitleOpts
    icon: ToolboxFeatureMagicTypeIconOpts
    iconStyle: ToolboxFeatureMagicTypeIconStyleOpts
    emphasis: ToolboxFeatureMagicTypeEmphasisOpts
    option: ToolboxFeatureMagicTypeOptionOpts
    seriesIndex: ToolboxFeatureMagicTypeSeriesIndexOpts

class ToolboxFeatureMagicTypeSeriesIndexOpts(TypedDict, total=False):
    line: Any
    bar: Any

class ToolboxFeatureMagicTypeTitleOpts(TypedDict, total=False):
    line: str
    bar: str
    stack: str
    tiled: str

class ToolboxFeatureOpts(TypedDict, total=False):
    saveAsImage: ToolboxFeatureSaveAsImageOpts
    restore: ToolboxFeatureRestoreOpts
    dataView: ToolboxFeatureDataViewOpts
    dataZoom: ToolboxFeatureDataZoomOpts
    magicType: ToolboxFeatureMagicTypeOpts
    brush: ToolboxFeatureBrushOpts

class ToolboxFeatureRestoreEmphasisIconStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    textPosition: str
    textFill: str
    textAlign: Literal["left", "center", "right"]
    textBackgroundColor: str
    textBorderRadius: int | float
    textPadding: int | float

class ToolboxFeatureRestoreEmphasisOpts(TypedDict, total=False):
    iconStyle: ToolboxFeatureRestoreEmphasisIconStyleOpts

class ToolboxFeatureRestoreIconStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class ToolboxFeatureRestoreOpts(TypedDict, total=False):
    show: bool
    title: str
    icon: str
    iconStyle: ToolboxFeatureRestoreIconStyleOpts
    emphasis: ToolboxFeatureRestoreEmphasisOpts

class ToolboxFeatureSaveAsImageEmphasisIconStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    textPosition: str
    textFill: str
    textAlign: Literal["left", "center", "right"]
    textBackgroundColor: str
    textBorderRadius: int | float
    textPadding: int | float

class ToolboxFeatureSaveAsImageEmphasisOpts(TypedDict, total=False):
    iconStyle: ToolboxFeatureSaveAsImageEmphasisIconStyleOpts

class ToolboxFeatureSaveAsImageIconStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class ToolboxFeatureSaveAsImageOpts(TypedDict, total=False):
    type: Literal["png", "jpg"]
    name: str
    backgroundColor: str | list[str]
    connectedBackgroundColor: str | list[str]
    excludeComponents: Any
    show: bool
    title: str
    icon: str
    iconStyle: ToolboxFeatureSaveAsImageIconStyleOpts
    emphasis: ToolboxFeatureSaveAsImageEmphasisOpts
    pixelRatio: int | float

class ToolboxIconStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class ToolboxOpts(TypedDict, total=False):
    id: str
    show: bool
    orient: Literal["vertical", "horizontal"]
    itemSize: int | float
    itemGap: int | float
    showTitle: bool
    feature: ToolboxFeatureOpts
    iconStyle: ToolboxIconStyleOpts
    emphasis: ToolboxEmphasisOpts
    zlevel: int | float
    z: int | float
    left: str | int | float
    top: str | int | float
    right: str | int | float
    bottom: str | int | float
    width: str | int | float
    height: str | int | float
    coordinateSystem: str
    coordinateSystemUsage: str
    coord: str | int | float
    calendarIndex: int | float
    calendarId: int | float
    matrixIndex: int | float
    matrixId: int | float
    tooltip: dict[str, Any]

class TooltipAxisPointerCrossStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class TooltipAxisPointerLabelOpts(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: str | Callable[..., Any]
    margin: int | float
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    padding: str
    backgroundColor: str
    borderColor: str
    borderWidth: str
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class TooltipAxisPointerLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class TooltipAxisPointerOpts(TypedDict, total=False):
    type: Literal["none", "line", "shadow", "cross"]
    axis: str
    snap: bool
    z: int | float
    label: TooltipAxisPointerLabelOpts
    lineStyle: TooltipAxisPointerLineStyleOpts
    shadowStyle: TooltipAxisPointerShadowStyleOpts
    crossStyle: TooltipAxisPointerCrossStyleOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: int | float | Callable[..., Any]
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: int | float | Callable[..., Any]
    animationDurationUpdate: int | float | Callable[..., Any]
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: int | float | Callable[..., Any]

class TooltipAxisPointerShadowStyleOpts(TypedDict, total=False):
    color: str | list[str]
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class TooltipOpts(TypedDict, total=False):
    show: bool
    trigger: Literal["item", "axis", "none"]
    axisPointer: TooltipAxisPointerOpts
    showContent: bool
    alwaysShowContent: bool
    triggerOn: Literal["mousemove", "click"]
    showDelay: int | float
    hideDelay: int | float
    enterable: bool
    renderMode: Literal["html", "richText"]
    confine: bool
    appendToBody: bool
    appendTo: str | Callable[..., Any]
    className: str
    transitionDuration: int | float
    displayTransition: bool
    position: str
    formatter: str | Callable[..., Any]
    valueFormatter: str
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: TooltipTextStyleOpts
    extraCssText: str
    order: Literal["seriesAsc", "seriesDesc", "valueAsc", "valueDesc"]

class TooltipTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str

class XAxis3DAxisLabelOpts(TypedDict, total=False):
    show: bool
    margin: int | float
    interval: int | float | Callable[..., Any]
    formatter: str | Callable[..., Any]
    textStyle: XAxis3DAxisLabelTextStyleOpts

class XAxis3DAxisLabelTextStyleOpts(TypedDict, total=False):
    color: str | list[str] | Callable[..., Any]
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class XAxis3DAxisLineLineStyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class XAxis3DAxisLineOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    lineStyle: XAxis3DAxisLineLineStyleOpts

class XAxis3DAxisPointerLabelOpts(TypedDict, total=False):
    show: bool
    formatter: Callable[..., Any]
    margin: int | float
    textStyle: XAxis3DAxisPointerLabelTextStyleOpts

class XAxis3DAxisPointerLabelTextStyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class XAxis3DAxisPointerLineStyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class XAxis3DAxisPointerOpts(TypedDict, total=False):
    show: bool
    lineStyle: XAxis3DAxisPointerLineStyleOpts
    label: XAxis3DAxisPointerLabelOpts

class XAxis3DAxisTickLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    opacity: int | float
    width: int | float

class XAxis3DAxisTickOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    length: int | float
    lineStyle: XAxis3DAxisTickLineStyleOpts

class XAxis3DDataItemOpts(TypedDict, total=False):
    value: str
    textStyle: XAxis3DDataItemTextStyleOpts

class XAxis3DDataItemTextStyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class XAxis3DNameTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class XAxis3DOpts(TypedDict, total=False):
    show: bool
    name: str
    grid3DIndex: int | float
    nameTextStyle: XAxis3DNameTextStyleOpts
    nameGap: int | float
    type: str
    min: str | int | float
    max: str | int | float
    scale: bool
    splitNumber: int | float
    minInterval: int | float
    interval: int | float
    logBase: int | float
    data: list[XAxis3DDataItemOpts]
    axisLine: XAxis3DAxisLineOpts
    axisLabel: XAxis3DAxisLabelOpts
    axisTick: XAxis3DAxisTickOpts
    splitLine: XAxis3DSplitLineOpts
    splitArea: XAxis3DSplitAreaOpts
    axisPointer: XAxis3DAxisPointerOpts

class XAxis3DSplitAreaAreaStyleOpts(TypedDict, total=False):
    color: Any

class XAxis3DSplitAreaOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    areaStyle: XAxis3DSplitAreaAreaStyleOpts

class XAxis3DSplitLineLineStyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class XAxis3DSplitLineOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    lineStyle: XAxis3DSplitLineLineStyleOpts

class XAxisAxisLabelOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    inside: bool
    rotate: int | float
    margin: int | float
    formatter: str | Callable[..., Any]
    showMinLabel: bool
    showMaxLabel: bool
    alignMinLabel: str
    alignMaxLabel: str
    hideOverlap: bool
    customValues: Any
    color: str | list[str] | Callable[..., Any]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: XAxisAxisLabelRichOpts
    richInheritPlainLabel: bool

class XAxisAxisLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class XAxisAxisLineLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class XAxisAxisLineOpts(TypedDict, total=False):
    show: bool
    onZero: Literal["auto", "true", "false"]
    onZeroAxisIndex: int | float
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: XAxisAxisLineLineStyleOpts

class XAxisAxisPointerHandleOpts(TypedDict, total=False):
    show: bool
    icon: Any
    size: int | float
    margin: int | float
    color: str
    throttle: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class XAxisAxisPointerLabelOpts(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: str | Callable[..., Any]
    margin: int | float
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    padding: str
    backgroundColor: str
    borderColor: str
    borderWidth: str
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class XAxisAxisPointerLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class XAxisAxisPointerOpts(TypedDict, total=False):
    show: bool
    type: Literal["line", "shadow", "none"]
    snap: bool
    z: int | float
    label: XAxisAxisPointerLabelOpts
    lineStyle: XAxisAxisPointerLineStyleOpts
    shadowStyle: XAxisAxisPointerShadowStyleOpts
    triggerEmphasis: bool
    triggerTooltip: bool
    value: int | float
    status: Literal["show", "hide"]
    handle: XAxisAxisPointerHandleOpts

class XAxisAxisPointerShadowStyleOpts(TypedDict, total=False):
    color: str | list[str]
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class XAxisAxisTickLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class XAxisAxisTickOpts(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: int | float | Callable[..., Any]
    inside: bool
    length: int | float
    lineStyle: XAxisAxisTickLineStyleOpts
    customValues: Any

class XAxisBreakAreaItemStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class XAxisBreakAreaOpts(TypedDict, total=False):
    show: bool
    itemStyle: XAxisBreakAreaItemStyleOpts
    zigzagAmplitude: int | float
    zigzagMinSpan: int | float
    zigzagMaxSpan: int | float
    zigzagZ: int | float
    expandOnClick: bool

class XAxisBreakLabelLayoutOpts(TypedDict, total=False):
    moveOverlap: str | bool

class XAxisBreaksItemOpts(TypedDict, total=False):
    start: str | int | float
    end: str | int | float
    gap: str | int | float
    isExpanded: bool

class XAxisDataItemOpts(TypedDict, total=False):
    value: str
    textStyle: XAxisDataItemTextStyleOpts

class XAxisDataItemTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: XAxisDataItemTextStyleRichOpts
    richInheritPlainLabel: bool

class XAxisDataItemTextStyleRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class XAxisMinorSplitLineLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class XAxisMinorSplitLineOpts(TypedDict, total=False):
    show: bool
    lineStyle: XAxisMinorSplitLineLineStyleOpts

class XAxisMinorTickLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class XAxisMinorTickOpts(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: XAxisMinorTickLineStyleOpts

class XAxisNameTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: XAxisNameTextStyleRichOpts
    richInheritPlainLabel: bool

class XAxisNameTextStyleRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class XAxisNameTruncateOpts(TypedDict, total=False):
    maxWidth: int | float
    ellipsis: str

class XAxisOpts(TypedDict, total=False):
    id: str
    show: bool
    gridIndex: int | float
    alignTicks: bool
    position: Literal["top", "bottom"]
    offset: int | float
    type: str
    name: str
    nameLocation: Literal["start", "middle", "end"]
    nameTextStyle: XAxisNameTextStyleOpts
    nameGap: int | float
    nameRotate: int | float
    nameTruncate: XAxisNameTruncateOpts
    nameMoveOverlap: bool
    inverse: bool
    boundaryGap: bool
    containShape: bool
    min: str | int | float | Callable[..., Any]
    max: str | int | float | Callable[..., Any]
    dataMin: int | float
    dataMax: int | float
    scale: bool
    splitNumber: int | float
    minInterval: int | float
    maxInterval: int | float
    interval: int | float
    logBase: int | float
    startValue: int | float
    silent: bool
    triggerEvent: bool
    jitter: int | float
    jitterOverlap: bool
    jitterMargin: int | float
    breaks: list[XAxisBreaksItemOpts]
    breakArea: XAxisBreakAreaOpts
    breakLabelLayout: XAxisBreakLabelLayoutOpts
    axisLine: XAxisAxisLineOpts
    axisTick: XAxisAxisTickOpts
    minorTick: XAxisMinorTickOpts
    axisLabel: XAxisAxisLabelOpts
    splitLine: XAxisSplitLineOpts
    minorSplitLine: XAxisMinorSplitLineOpts
    splitArea: XAxisSplitAreaOpts
    data: list[XAxisDataItemOpts]
    axisPointer: XAxisAxisPointerOpts
    tooltip: XAxisTooltipOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: int | float | Callable[..., Any]
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: int | float | Callable[..., Any]
    animationDurationUpdate: int | float | Callable[..., Any]
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: int | float | Callable[..., Any]
    zlevel: int | float
    z: int | float

class XAxisSplitAreaAreaStyleOpts(TypedDict, total=False):
    color: Any
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class XAxisSplitAreaOpts(TypedDict, total=False):
    interval: int | float | Callable[..., Any]
    show: bool
    areaStyle: XAxisSplitAreaAreaStyleOpts

class XAxisSplitLineLineStyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class XAxisSplitLineOpts(TypedDict, total=False):
    show: bool
    showMinLine: bool
    showMaxLine: bool
    interval: int | float | Callable[..., Any]
    lineStyle: XAxisSplitLineLineStyleOpts

class XAxisTooltipOpts(TypedDict, total=False):
    show: bool
    position: str
    formatter: str | Callable[..., Any]
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: XAxisTooltipTextStyleOpts
    extraCssText: str

class XAxisTooltipTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str

class YAxis3DAxisLabelOpts(TypedDict, total=False):
    show: bool
    margin: int | float
    interval: int | float | Callable[..., Any]
    formatter: str | Callable[..., Any]
    textStyle: YAxis3DAxisLabelTextStyleOpts

class YAxis3DAxisLabelTextStyleOpts(TypedDict, total=False):
    color: str | list[str] | Callable[..., Any]
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class YAxis3DAxisLineLineStyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class YAxis3DAxisLineOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    lineStyle: YAxis3DAxisLineLineStyleOpts

class YAxis3DAxisPointerLabelOpts(TypedDict, total=False):
    show: bool
    formatter: Callable[..., Any]
    margin: int | float
    textStyle: YAxis3DAxisPointerLabelTextStyleOpts

class YAxis3DAxisPointerLabelTextStyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class YAxis3DAxisPointerLineStyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class YAxis3DAxisPointerOpts(TypedDict, total=False):
    show: bool
    lineStyle: YAxis3DAxisPointerLineStyleOpts
    label: YAxis3DAxisPointerLabelOpts

class YAxis3DAxisTickLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    opacity: int | float
    width: int | float

class YAxis3DAxisTickOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    length: int | float
    lineStyle: YAxis3DAxisTickLineStyleOpts

class YAxis3DDataItemOpts(TypedDict, total=False):
    value: str
    textStyle: YAxis3DDataItemTextStyleOpts

class YAxis3DDataItemTextStyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class YAxis3DNameTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class YAxis3DOpts(TypedDict, total=False):
    show: bool
    name: str
    grid3DIndex: int | float
    nameTextStyle: YAxis3DNameTextStyleOpts
    nameGap: int | float
    type: str
    min: str | int | float
    max: str | int | float
    scale: bool
    splitNumber: int | float
    minInterval: int | float
    interval: int | float
    logBase: int | float
    data: list[YAxis3DDataItemOpts]
    axisLine: YAxis3DAxisLineOpts
    axisLabel: YAxis3DAxisLabelOpts
    axisTick: YAxis3DAxisTickOpts
    splitLine: YAxis3DSplitLineOpts
    splitArea: YAxis3DSplitAreaOpts
    axisPointer: YAxis3DAxisPointerOpts

class YAxis3DSplitAreaAreaStyleOpts(TypedDict, total=False):
    color: Any

class YAxis3DSplitAreaOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    areaStyle: YAxis3DSplitAreaAreaStyleOpts

class YAxis3DSplitLineLineStyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class YAxis3DSplitLineOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    lineStyle: YAxis3DSplitLineLineStyleOpts

class YAxisAxisLabelOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    inside: bool
    rotate: int | float
    margin: int | float
    formatter: str | Callable[..., Any]
    showMinLabel: bool
    showMaxLabel: bool
    verticalAlignMinLabel: str
    verticalAlignMaxLabel: str
    hideOverlap: bool
    customValues: Any
    color: str | list[str] | Callable[..., Any]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: YAxisAxisLabelRichOpts
    richInheritPlainLabel: bool

class YAxisAxisLabelRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class YAxisAxisLineLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class YAxisAxisLineOpts(TypedDict, total=False):
    show: bool
    onZero: Literal["auto", "true", "false"]
    onZeroAxisIndex: int | float
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: YAxisAxisLineLineStyleOpts

class YAxisAxisPointerHandleOpts(TypedDict, total=False):
    show: bool
    icon: Any
    size: int | float
    margin: int | float
    color: str
    throttle: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class YAxisAxisPointerLabelOpts(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: str | Callable[..., Any]
    margin: int | float
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    padding: str
    backgroundColor: str
    borderColor: str
    borderWidth: str
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class YAxisAxisPointerLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class YAxisAxisPointerOpts(TypedDict, total=False):
    show: bool
    type: Literal["line", "shadow", "none"]
    snap: bool
    z: int | float
    label: YAxisAxisPointerLabelOpts
    lineStyle: YAxisAxisPointerLineStyleOpts
    shadowStyle: YAxisAxisPointerShadowStyleOpts
    triggerEmphasis: bool
    triggerTooltip: bool
    value: int | float
    status: Literal["show", "hide"]
    handle: YAxisAxisPointerHandleOpts

class YAxisAxisPointerShadowStyleOpts(TypedDict, total=False):
    color: str | list[str]
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class YAxisAxisTickLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class YAxisAxisTickOpts(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: int | float | Callable[..., Any]
    inside: bool
    length: int | float
    lineStyle: YAxisAxisTickLineStyleOpts
    customValues: Any

class YAxisBreakAreaItemStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderCap: Literal["butt", "round", "square"]
    borderJoin: Literal["bevel", "round", "miter"]
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class YAxisBreakAreaOpts(TypedDict, total=False):
    show: bool
    itemStyle: YAxisBreakAreaItemStyleOpts
    zigzagAmplitude: int | float
    zigzagMinSpan: int | float
    zigzagMaxSpan: int | float
    zigzagZ: int | float
    expandOnClick: bool

class YAxisBreakLabelLayoutOpts(TypedDict, total=False):
    moveOverlap: str | bool

class YAxisBreaksItemOpts(TypedDict, total=False):
    start: str | int | float
    end: str | int | float
    gap: str | int | float
    isExpanded: bool

class YAxisDataItemOpts(TypedDict, total=False):
    value: str
    textStyle: YAxisDataItemTextStyleOpts

class YAxisDataItemTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: YAxisDataItemTextStyleRichOpts
    richInheritPlainLabel: bool

class YAxisDataItemTextStyleRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class YAxisMinorSplitLineLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class YAxisMinorSplitLineOpts(TypedDict, total=False):
    show: bool
    lineStyle: YAxisMinorSplitLineLineStyleOpts

class YAxisMinorTickLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class YAxisMinorTickOpts(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: YAxisMinorTickLineStyleOpts

class YAxisNameTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str
    rich: YAxisNameTextStyleRichOpts
    richInheritPlainLabel: bool

class YAxisNameTextStyleRichStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    align: Literal["left", "center", "right"]
    verticalAlign: Literal["top", "middle", "bottom"]
    lineHeight: int | float
    backgroundColor: str | dict[str, Any]
    borderColor: str | list[str]
    borderWidth: int | float
    borderType: Literal["solid", "dashed", "dotted"]
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str | list[str]
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

class YAxisNameTruncateOpts(TypedDict, total=False):
    maxWidth: int | float
    ellipsis: str

class YAxisOpts(TypedDict, total=False):
    id: str
    show: bool
    gridIndex: int | float
    alignTicks: bool
    position: Literal["left", "right"]
    offset: int | float
    type: str
    name: str
    nameLocation: Literal["start", "middle", "end"]
    nameTextStyle: YAxisNameTextStyleOpts
    nameGap: int | float
    nameRotate: int | float
    nameTruncate: YAxisNameTruncateOpts
    nameMoveOverlap: bool
    inverse: bool
    boundaryGap: bool
    containShape: bool
    min: str | int | float | Callable[..., Any]
    max: str | int | float | Callable[..., Any]
    dataMin: int | float
    dataMax: int | float
    scale: bool
    splitNumber: int | float
    minInterval: int | float
    maxInterval: int | float
    interval: int | float
    logBase: int | float
    startValue: int | float
    silent: bool
    triggerEvent: bool
    jitter: int | float
    jitterOverlap: bool
    jitterMargin: int | float
    breaks: list[YAxisBreaksItemOpts]
    breakArea: YAxisBreakAreaOpts
    breakLabelLayout: YAxisBreakLabelLayoutOpts
    axisLine: YAxisAxisLineOpts
    axisTick: YAxisAxisTickOpts
    minorTick: YAxisMinorTickOpts
    axisLabel: YAxisAxisLabelOpts
    splitLine: YAxisSplitLineOpts
    minorSplitLine: YAxisMinorSplitLineOpts
    splitArea: YAxisSplitAreaOpts
    data: list[YAxisDataItemOpts]
    axisPointer: YAxisAxisPointerOpts
    tooltip: YAxisTooltipOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: int | float | Callable[..., Any]
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: int | float | Callable[..., Any]
    animationDurationUpdate: int | float | Callable[..., Any]
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: int | float | Callable[..., Any]
    zlevel: int | float
    z: int | float

class YAxisSplitAreaAreaStyleOpts(TypedDict, total=False):
    color: Any
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class YAxisSplitAreaOpts(TypedDict, total=False):
    interval: int | float | Callable[..., Any]
    show: bool
    areaStyle: YAxisSplitAreaAreaStyleOpts

class YAxisSplitLineLineStyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: Literal["solid", "dashed", "dotted"]
    dashOffset: int | float
    cap: Literal["butt", "round", "square"]
    join: Literal["bevel", "round", "miter"]
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class YAxisSplitLineOpts(TypedDict, total=False):
    show: bool
    showMinLine: bool
    showMaxLine: bool
    interval: int | float | Callable[..., Any]
    lineStyle: YAxisSplitLineLineStyleOpts

class YAxisTooltipOpts(TypedDict, total=False):
    show: bool
    position: str
    formatter: str | Callable[..., Any]
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: YAxisTooltipTextStyleOpts
    extraCssText: str

class YAxisTooltipTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    fontStyle: Literal["normal", "italic", "oblique"]
    fontWeight: Literal["normal", "bold", "bolder", "lighter"]
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str | list[str]
    textBorderWidth: int | float
    textBorderType: Literal["solid", "dashed", "dotted"]
    textBorderDashOffset: int | float
    textShadowColor: str | list[str]
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: Literal["truncate", "break", "breakAll"]
    ellipsis: str

class ZAxis3DAxisLabelOpts(TypedDict, total=False):
    show: bool
    margin: int | float
    interval: int | float | Callable[..., Any]
    formatter: str | Callable[..., Any]
    textStyle: ZAxis3DAxisLabelTextStyleOpts

class ZAxis3DAxisLabelTextStyleOpts(TypedDict, total=False):
    color: str | list[str] | Callable[..., Any]
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class ZAxis3DAxisLineLineStyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class ZAxis3DAxisLineOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    lineStyle: ZAxis3DAxisLineLineStyleOpts

class ZAxis3DAxisPointerLabelOpts(TypedDict, total=False):
    show: bool
    formatter: Callable[..., Any]
    margin: int | float
    textStyle: ZAxis3DAxisPointerLabelTextStyleOpts

class ZAxis3DAxisPointerLabelTextStyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class ZAxis3DAxisPointerLineStyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class ZAxis3DAxisPointerOpts(TypedDict, total=False):
    show: bool
    lineStyle: ZAxis3DAxisPointerLineStyleOpts
    label: ZAxis3DAxisPointerLabelOpts

class ZAxis3DAxisTickLineStyleOpts(TypedDict, total=False):
    color: str | list[str]
    opacity: int | float
    width: int | float

class ZAxis3DAxisTickOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    length: int | float
    lineStyle: ZAxis3DAxisTickLineStyleOpts

class ZAxis3DDataItemOpts(TypedDict, total=False):
    value: str
    textStyle: ZAxis3DDataItemTextStyleOpts

class ZAxis3DDataItemTextStyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class ZAxis3DNameTextStyleOpts(TypedDict, total=False):
    color: str | list[str]
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class ZAxis3DOpts(TypedDict, total=False):
    show: bool
    name: str
    grid3DIndex: int | float
    nameTextStyle: ZAxis3DNameTextStyleOpts
    nameGap: int | float
    type: str
    min: str | int | float
    max: str | int | float
    scale: bool
    splitNumber: int | float
    minInterval: int | float
    interval: int | float
    logBase: int | float
    data: list[ZAxis3DDataItemOpts]
    axisLine: ZAxis3DAxisLineOpts
    axisLabel: ZAxis3DAxisLabelOpts
    axisTick: ZAxis3DAxisTickOpts
    splitLine: ZAxis3DSplitLineOpts
    splitArea: ZAxis3DSplitAreaOpts
    axisPointer: ZAxis3DAxisPointerOpts

class ZAxis3DSplitAreaAreaStyleOpts(TypedDict, total=False):
    color: Any

class ZAxis3DSplitAreaOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    areaStyle: ZAxis3DSplitAreaAreaStyleOpts

class ZAxis3DSplitLineLineStyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class ZAxis3DSplitLineOpts(TypedDict, total=False):
    show: bool
    interval: int | float | Callable[..., Any]
    lineStyle: ZAxis3DSplitLineLineStyleOpts

AngleAxisAxisLabelRichOpts = dict[str, AngleAxisAxisLabelRichStyleOpts]
AngleAxisDataItemTextStyleRichOpts = dict[str, AngleAxisDataItemTextStyleRichStyleOpts]
CalendarDayLabelRichOpts = dict[str, CalendarDayLabelRichStyleOpts]
CalendarMonthLabelRichOpts = dict[str, CalendarMonthLabelRichStyleOpts]
CalendarYearLabelRichOpts = dict[str, CalendarYearLabelRichStyleOpts]
GeoBlurLabelRichOpts = dict[str, GeoBlurLabelRichStyleOpts]
GeoEmphasisLabelRichOpts = dict[str, GeoEmphasisLabelRichStyleOpts]
GeoLabelRichOpts = dict[str, GeoLabelRichStyleOpts]
GeoRegionsItemBlurLabelRichOpts = dict[str, GeoRegionsItemBlurLabelRichStyleOpts]
GeoRegionsItemEmphasisLabelRichOpts = dict[str, GeoRegionsItemEmphasisLabelRichStyleOpts]
GeoRegionsItemLabelRichOpts = dict[str, GeoRegionsItemLabelRichStyleOpts]
GeoRegionsItemSelectLabelRichOpts = dict[str, GeoRegionsItemSelectLabelRichStyleOpts]
GeoSelectLabelRichOpts = dict[str, GeoSelectLabelRichStyleOpts]
LegendEmphasisSelectorLabelRichOpts = dict[str, LegendEmphasisSelectorLabelRichStyleOpts]
LegendSelectorLabelRichOpts = dict[str, LegendSelectorLabelRichStyleOpts]
LegendTextStyleRichOpts = dict[str, LegendTextStyleRichStyleOpts]
MatrixBodyLabelRichOpts = dict[str, MatrixBodyLabelRichStyleOpts]
MatrixCornerLabelRichOpts = dict[str, MatrixCornerLabelRichStyleOpts]
MatrixXLabelRichOpts = dict[str, MatrixXLabelRichStyleOpts]
MatrixYLabelRichOpts = dict[str, MatrixYLabelRichStyleOpts]
ParallelAxisAxisLabelRichOpts = dict[str, ParallelAxisAxisLabelRichStyleOpts]
ParallelAxisDataItemTextStyleRichOpts = dict[str, ParallelAxisDataItemTextStyleRichStyleOpts]
ParallelAxisNameTextStyleRichOpts = dict[str, ParallelAxisNameTextStyleRichStyleOpts]
ParallelParallelAxisDefaultAxisLabelRichOpts = dict[str, ParallelParallelAxisDefaultAxisLabelRichStyleOpts]
ParallelParallelAxisDefaultDataItemTextStyleRichOpts = dict[str, ParallelParallelAxisDefaultDataItemTextStyleRichStyleOpts]
ParallelParallelAxisDefaultNameTextStyleRichOpts = dict[str, ParallelParallelAxisDefaultNameTextStyleRichStyleOpts]
RadarAxisLabelRichOpts = dict[str, RadarAxisLabelRichStyleOpts]
RadarAxisNameRichOpts = dict[str, RadarAxisNameRichStyleOpts]
RadiusAxisAxisLabelRichOpts = dict[str, RadiusAxisAxisLabelRichStyleOpts]
RadiusAxisDataItemTextStyleRichOpts = dict[str, RadiusAxisDataItemTextStyleRichStyleOpts]
RadiusAxisNameTextStyleRichOpts = dict[str, RadiusAxisNameTextStyleRichStyleOpts]
SingleAxisAxisLabelRichOpts = dict[str, SingleAxisAxisLabelRichStyleOpts]
SingleAxisDataItemTextStyleRichOpts = dict[str, SingleAxisDataItemTextStyleRichStyleOpts]
SingleAxisNameTextStyleRichOpts = dict[str, SingleAxisNameTextStyleRichStyleOpts]
TimelineEmphasisLabelRichOpts = dict[str, TimelineEmphasisLabelRichStyleOpts]
TimelineLabelRichOpts = dict[str, TimelineLabelRichStyleOpts]
TimelineProgressLabelRichOpts = dict[str, TimelineProgressLabelRichStyleOpts]
TitleSubtextStyleRichOpts = dict[str, TitleSubtextStyleRichStyleOpts]
TitleTextStyleRichOpts = dict[str, TitleTextStyleRichStyleOpts]
XAxisAxisLabelRichOpts = dict[str, XAxisAxisLabelRichStyleOpts]
XAxisDataItemTextStyleRichOpts = dict[str, XAxisDataItemTextStyleRichStyleOpts]
XAxisNameTextStyleRichOpts = dict[str, XAxisNameTextStyleRichStyleOpts]
YAxisAxisLabelRichOpts = dict[str, YAxisAxisLabelRichStyleOpts]
YAxisDataItemTextStyleRichOpts = dict[str, YAxisDataItemTextStyleRichStyleOpts]
YAxisNameTextStyleRichOpts = dict[str, YAxisNameTextStyleRichStyleOpts]

class Option(TypedDict, total=False):
    angleAxis: AngleAxisOpts
    animation: dict[str, Any]
    animationDelay: dict[str, Any]
    animationDelayUpdate: dict[str, Any]
    animationDuration: dict[str, Any]
    animationDurationUpdate: dict[str, Any]
    animationEasing: dict[str, Any]
    animationEasingUpdate: dict[str, Any]
    animationThreshold: dict[str, Any]
    aria: AriaOpts
    axisPointer: AxisPointerOpts
    backgroundColor: dict[str, Any]
    blendMode: dict[str, Any]
    brush: BrushOpts
    calendar: CalendarOpts
    color: dict[str, Any]
    darkMode: dict[str, Any]
    dataZoom: dict[str, Any]
    dataset: DatasetOpts
    geo3D: Geo3DOpts
    geo: GeoOpts
    globe: GlobeOpts
    graphic: GraphicOpts
    grid3D: Grid3DOpts
    grid: GridOpts
    hoverLayerThreshold: dict[str, Any]
    legend: LegendOpts
    mapbox3D: Mapbox3DOpts
    matrix: MatrixOpts
    media: dict[str, Any]
    options: dict[str, Any]
    parallel: ParallelOpts
    parallelAxis: ParallelAxisOpts
    polar: PolarOpts
    radar: RadarOpts
    radiusAxis: RadiusAxisOpts
    richInheritPlainLabel: dict[str, Any]
    series: dict[str, Any]
    singleAxis: SingleAxisOpts
    stateAnimation: StateAnimationOpts
    textStyle: TextStyleOpts
    thumbnail: ThumbnailOpts
    timeline: TimelineOpts
    title: TitleOpts
    toolbox: ToolboxOpts
    tooltip: TooltipOpts
    useUTC: dict[str, Any]
    visualMap: dict[str, Any]
    xAxis3D: XAxis3DOpts
    xAxis: XAxisOpts
    yAxis3D: YAxis3DOpts
    yAxis: YAxisOpts
    zAxis3D: ZAxis3DOpts