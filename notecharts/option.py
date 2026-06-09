from __future__ import annotations
from typing import Any, Callable, Literal
from typing_extensions import TypedDict

class AngleAxis(TypedDict, total=False):
    id: str
    polarIndex: int | float
    startAngle: int | float
    endAngle: int | float
    clockwise: bool
    type: str
    boundaryGap: bool
    containShape: bool
    min: Callable[..., Any] | str | int | float
    max: Callable[..., Any] | str | int | float
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
    axisLine: AngleAxisAxisLine
    axisTick: AngleAxisAxisTick
    minorTick: AngleAxisMinorTick
    axisLabel: AngleAxisAxisLabel
    splitLine: AngleAxisSplitLine
    minorSplitLine: AngleAxisMinorSplitLine
    splitArea: AngleAxisSplitArea
    data: list[AngleAxisDataItem]
    axisPointer: AngleAxisAxisPointer
    tooltip: AngleAxisTooltip
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: Callable[..., Any] | int | float
    zlevel: int | float
    z: int | float

class AngleAxisAxisLabel(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    margin: int | float
    formatter: Callable[..., Any] | str
    showMinLabel: bool
    showMaxLabel: bool
    hideOverlap: bool
    customValues: Any
    color: Callable[..., Any] | str | list[str]
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
    rich: AngleAxisAxisLabelRich
    richInheritPlainLabel: bool

class AngleAxisAxisLabelRichStyle(TypedDict, total=False):
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

class AngleAxisAxisLine(TypedDict, total=False):
    show: bool
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: AngleAxisAxisLineLineStyle

class AngleAxisAxisLineLineStyle(TypedDict, total=False):
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

class AngleAxisAxisPointer(TypedDict, total=False):
    show: bool
    type: Literal["line", "shadow", "none"]
    snap: bool
    z: int | float
    label: AngleAxisAxisPointerLabel
    lineStyle: AngleAxisAxisPointerLineStyle
    shadowStyle: AngleAxisAxisPointerShadowStyle
    triggerEmphasis: bool
    triggerTooltip: bool
    value: int | float
    status: Literal["show", "hide"]
    handle: AngleAxisAxisPointerHandle

class AngleAxisAxisPointerHandle(TypedDict, total=False):
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

class AngleAxisAxisPointerLabel(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: Callable[..., Any] | str
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

class AngleAxisAxisPointerLineStyle(TypedDict, total=False):
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

class AngleAxisAxisPointerShadowStyle(TypedDict, total=False):
    color: str | list[str]
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class AngleAxisAxisTick(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    length: int | float
    lineStyle: AngleAxisAxisTickLineStyle
    customValues: Any

class AngleAxisAxisTickLineStyle(TypedDict, total=False):
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

class AngleAxisDataItem(TypedDict, total=False):
    value: str
    textStyle: AngleAxisDataItemTextStyle

class AngleAxisDataItemTextStyle(TypedDict, total=False):
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
    rich: AngleAxisDataItemTextStyleRich
    richInheritPlainLabel: bool

class AngleAxisDataItemTextStyleRichStyle(TypedDict, total=False):
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

class AngleAxisMinorSplitLine(TypedDict, total=False):
    show: bool
    lineStyle: AngleAxisMinorSplitLineLineStyle

class AngleAxisMinorSplitLineLineStyle(TypedDict, total=False):
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

class AngleAxisMinorTick(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: AngleAxisMinorTickLineStyle

class AngleAxisMinorTickLineStyle(TypedDict, total=False):
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

class AngleAxisSplitArea(TypedDict, total=False):
    interval: Callable[..., Any] | int | float
    show: bool
    areaStyle: AngleAxisSplitAreaAreaStyle

class AngleAxisSplitAreaAreaStyle(TypedDict, total=False):
    color: Any
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class AngleAxisSplitLine(TypedDict, total=False):
    show: bool
    showMinLine: bool
    showMaxLine: bool
    interval: Callable[..., Any] | int | float
    lineStyle: AngleAxisSplitLineLineStyle

class AngleAxisSplitLineLineStyle(TypedDict, total=False):
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

class AngleAxisTooltip(TypedDict, total=False):
    show: bool
    position: str
    formatter: Callable[..., Any] | str
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: AngleAxisTooltipTextStyle
    extraCssText: str

class AngleAxisTooltipTextStyle(TypedDict, total=False):
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

class Aria(TypedDict, total=False):
    enabled: bool
    label: AriaLabel
    decal: AriaDecal

class AriaDecal(TypedDict, total=False):
    show: bool
    decals: AriaDecalDecals

class AriaDecalDecals(TypedDict, total=False):
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

class AriaLabel(TypedDict, total=False):
    enabled: bool
    description: str
    general: AriaLabelGeneral
    series: AriaLabelSeries
    data: AriaLabelData

class AriaLabelData(TypedDict, total=False):
    maxCount: int | float
    allData: str
    partialData: str
    withName: str
    withoutName: str
    excludeDimensionId: Any
    separator: AriaLabelDataSeparator

class AriaLabelDataSeparator(TypedDict, total=False):
    middle: str
    end: str

class AriaLabelGeneral(TypedDict, total=False):
    withTitle: str
    withoutTitle: str

class AriaLabelSeries(TypedDict, total=False):
    maxCount: int | float
    single: AriaLabelSeriesSingle
    multiple: AriaLabelSeriesMultiple

class AriaLabelSeriesMultiple(TypedDict, total=False):
    prefix: str
    withName: str
    withoutName: str
    separator: AriaLabelSeriesMultipleSeparator

class AriaLabelSeriesMultipleSeparator(TypedDict, total=False):
    middle: str
    end: str

class AriaLabelSeriesSingle(TypedDict, total=False):
    prefix: str
    withName: str
    withoutName: str

class AxisPointer(TypedDict, total=False):
    id: str
    show: bool
    type: Literal["line", "shadow", "none"]
    snap: bool
    z: int | float
    label: AxisPointerLabel
    lineStyle: AxisPointerLineStyle
    shadowStyle: AxisPointerShadowStyle
    triggerEmphasis: bool
    triggerTooltip: bool
    value: int | float
    status: Literal["show", "hide"]
    handle: AxisPointerHandle
    link: Any
    triggerOn: Literal["mousemove", "click", "none"]

class AxisPointerHandle(TypedDict, total=False):
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

class AxisPointerLabel(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: Callable[..., Any] | str
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

class AxisPointerLineStyle(TypedDict, total=False):
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

class AxisPointerShadowStyle(TypedDict, total=False):
    color: str | list[str]
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Brush(TypedDict, total=False):
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

class Calendar(TypedDict, total=False):
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
    splitLine: CalendarSplitLine
    itemStyle: CalendarItemStyle
    dayLabel: CalendarDayLabel
    monthLabel: CalendarMonthLabel
    yearLabel: CalendarYearLabel
    silent: bool

class CalendarDayLabel(TypedDict, total=False):
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
    rich: CalendarDayLabelRich
    richInheritPlainLabel: bool
    silent: bool

class CalendarDayLabelRichStyle(TypedDict, total=False):
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

class CalendarItemStyle(TypedDict, total=False):
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

class CalendarMonthLabel(TypedDict, total=False):
    show: bool
    align: Literal["left", "center", "right"]
    margin: int | float
    position: Literal["start", "end"]
    nameMap: Literal["EN", "ZH"]
    formatter: Callable[..., Any] | str
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
    rich: CalendarMonthLabelRich
    richInheritPlainLabel: bool
    silent: bool

class CalendarMonthLabelRichStyle(TypedDict, total=False):
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

class CalendarSplitLine(TypedDict, total=False):
    show: bool
    lineStyle: CalendarSplitLineLineStyle

class CalendarSplitLineLineStyle(TypedDict, total=False):
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

class CalendarYearLabel(TypedDict, total=False):
    show: bool
    margin: int | float
    position: Literal["top", "bottom", "left", "right"]
    formatter: Callable[..., Any] | str
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
    rich: CalendarYearLabelRich
    richInheritPlainLabel: bool
    silent: bool

class CalendarYearLabelRichStyle(TypedDict, total=False):
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

class Dataset(TypedDict, total=False):
    id: str
    source: dict[str, Any]
    dimensions: Any
    sourceHeader: bool | int | float
    transform: Any
    fromDatasetIndex: int | float
    fromDatasetId: str
    fromTransformResult: int | float

class Geo(TypedDict, total=False):
    id: str
    show: bool
    map: str
    projection: GeoProjection
    center: Any
    zoom: int | float
    scaleLimit: GeoScaleLimit
    roam: Literal["true", "false", "scale", "move"]
    roamTrigger: str
    aspectScale: int | float
    boundingCoords: Any
    nameMap: dict[str, Any]
    nameProperty: str
    selectedMode: bool | str
    label: GeoLabel
    itemStyle: GeoItemStyle
    emphasis: GeoEmphasis
    select: GeoSelect
    blur: GeoBlur
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
    preserveAspect: bool | str
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
    regions: list[GeoRegionsItem]
    silent: bool
    tooltip: GeoTooltip

class Geo3D(TypedDict, total=False):
    show: bool
    map: str
    boxWidth: int | float
    boxHeight: int | float
    boxDepth: int | float
    regionHeight: int | float
    environment: str
    groundPlane: Geo3DGroundPlane
    instancing: bool
    label: Geo3DLabel
    itemStyle: Geo3DItemStyle
    emphasis: Geo3DEmphasis
    regions: list[Geo3DRegionsItem]
    shading: str
    realisticMaterial: Geo3DRealisticMaterial
    lambertMaterial: Geo3DLambertMaterial
    colorMaterial: Geo3DColorMaterial
    light: Geo3DLight
    postEffect: Geo3DPostEffect
    temporalSuperSampling: Geo3DTemporalSuperSampling
    viewControl: Geo3DViewControl
    zlevel: int | float
    left: str | int | float
    top: str | int | float
    right: str | int | float
    bottom: str | int | float
    width: str | int | float
    height: str | int | float

class Geo3DColorMaterial(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float

class Geo3DEmphasis(TypedDict, total=False):
    label: Geo3DEmphasisLabel
    itemStyle: Geo3DEmphasisItemStyle

class Geo3DEmphasisItemStyle(TypedDict, total=False):
    color: str
    opacity: int | float

class Geo3DEmphasisLabel(TypedDict, total=False):
    show: bool
    distance: int | float
    formatter: Callable[..., Any] | str
    textStyle: Geo3DEmphasisLabelTextStyle

class Geo3DEmphasisLabelTextStyle(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Geo3DGroundPlane(TypedDict, total=False):
    show: bool
    color: str

class Geo3DItemStyle(TypedDict, total=False):
    color: Callable[..., Any] | str
    opacity: int | float
    borderWidth: int | float
    borderColor: str

class Geo3DLabel(TypedDict, total=False):
    show: bool
    distance: int | float
    formatter: Callable[..., Any] | str
    textStyle: Geo3DLabelTextStyle

class Geo3DLabelTextStyle(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Geo3DLambertMaterial(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float

class Geo3DLight(TypedDict, total=False):
    main: Geo3DLightMain
    ambient: Geo3DLightAmbient
    ambientCubemap: Geo3DLightAmbientCubemap

class Geo3DLightAmbient(TypedDict, total=False):
    color: str
    intensity: int | float

class Geo3DLightAmbientCubemap(TypedDict, total=False):
    texture: str
    diffuseIntensity: int | float
    specularIntensity: int | float

class Geo3DLightMain(TypedDict, total=False):
    color: str
    intensity: int | float
    shadow: bool
    shadowQuality: str
    alpha: int | float
    beta: int | float

class Geo3DPostEffect(TypedDict, total=False):
    enable: bool
    bloom: Geo3DPostEffectBloom
    depthOfField: Geo3DPostEffectDepthOfField
    screenSpaceAmbientOcclusion: dict[str, Any]
    SSAO: Geo3DPostEffectSsao
    colorCorrection: Geo3DPostEffectColorCorrection
    FXAA: Geo3DPostEffectFxaa

class Geo3DPostEffectBloom(TypedDict, total=False):
    enable: bool
    bloomIntensity: int | float

class Geo3DPostEffectColorCorrection(TypedDict, total=False):
    enable: bool
    lookupTexture: str
    exposure: int | float
    brightness: int | float
    contrast: int | float
    saturation: int | float

class Geo3DPostEffectDepthOfField(TypedDict, total=False):
    enable: bool
    focalDistance: bool
    focalRange: bool
    fstop: int | float
    blurRadius: int | float

class Geo3DPostEffectFxaa(TypedDict, total=False):
    enable: bool

class Geo3DPostEffectSsao(TypedDict, total=False):
    enable: bool
    quality: str
    radius: int | float
    intensity: int | float

class Geo3DRealisticMaterial(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float
    roughness: str | int | float
    metalness: str | int | float
    roughnessAdjust: int | float
    metalnessAdjust: int | float
    normalTexture: str

class Geo3DRegionsItem(TypedDict, total=False):
    name: str
    regionHeight: int | float
    itemStyle: Geo3DRegionsItemItemStyle
    label: Geo3DRegionsItemLabel
    emphasis: Geo3DRegionsItemEmphasis

class Geo3DRegionsItemEmphasis(TypedDict, total=False):
    itemStyle: Geo3DRegionsItemEmphasisItemStyle
    label: Geo3DRegionsItemEmphasisLabel

class Geo3DRegionsItemEmphasisItemStyle(TypedDict, total=False):
    color: str
    opacity: int | float
    borderWidth: int | float
    borderColor: str

class Geo3DRegionsItemEmphasisLabel(TypedDict, total=False):
    show: bool
    distance: int | float
    formatter: Callable[..., Any] | str
    textStyle: Geo3DRegionsItemEmphasisLabelTextStyle

class Geo3DRegionsItemEmphasisLabelTextStyle(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Geo3DRegionsItemItemStyle(TypedDict, total=False):
    color: str
    opacity: int | float
    borderWidth: int | float
    borderColor: str

class Geo3DRegionsItemLabel(TypedDict, total=False):
    show: bool
    distance: int | float
    formatter: Callable[..., Any] | str
    textStyle: Geo3DRegionsItemLabelTextStyle

class Geo3DRegionsItemLabelTextStyle(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Geo3DTemporalSuperSampling(TypedDict, total=False):
    enable: bool

class Geo3DViewControl(TypedDict, total=False):
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

class GeoBlur(TypedDict, total=False):
    label: GeoBlurLabel
    itemStyle: GeoBlurItemStyle

class GeoBlurItemStyle(TypedDict, total=False):
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

class GeoBlurLabel(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
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
    rich: GeoBlurLabelRich
    richInheritPlainLabel: bool

class GeoBlurLabelRichStyle(TypedDict, total=False):
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

class GeoEmphasis(TypedDict, total=False):
    disabled: bool
    focus: str
    label: GeoEmphasisLabel
    itemStyle: GeoEmphasisItemStyle

class GeoEmphasisItemStyle(TypedDict, total=False):
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

class GeoEmphasisLabel(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
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
    rich: GeoEmphasisLabelRich
    richInheritPlainLabel: bool

class GeoEmphasisLabelRichStyle(TypedDict, total=False):
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

class GeoItemStyle(TypedDict, total=False):
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

class GeoLabel(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
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
    rich: GeoLabelRich
    richInheritPlainLabel: bool

class GeoLabelRichStyle(TypedDict, total=False):
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

class GeoProjection(TypedDict, total=False):
    project: Callable[..., Any]
    unproject: Callable[..., Any]
    stream: Callable[..., Any]

class GeoRegionsItem(TypedDict, total=False):
    name: str
    selected: bool
    itemStyle: GeoRegionsItemItemStyle
    label: GeoRegionsItemLabel
    emphasis: GeoRegionsItemEmphasis
    select: GeoRegionsItemSelect
    blur: GeoRegionsItemBlur
    tooltip: GeoRegionsItemTooltip
    silent: bool

class GeoRegionsItemBlur(TypedDict, total=False):
    itemStyle: GeoRegionsItemBlurItemStyle
    label: GeoRegionsItemBlurLabel

class GeoRegionsItemBlurItemStyle(TypedDict, total=False):
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

class GeoRegionsItemBlurLabel(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
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
    rich: GeoRegionsItemBlurLabelRich
    richInheritPlainLabel: bool

class GeoRegionsItemBlurLabelRichStyle(TypedDict, total=False):
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

class GeoRegionsItemEmphasis(TypedDict, total=False):
    itemStyle: GeoRegionsItemEmphasisItemStyle
    label: GeoRegionsItemEmphasisLabel

class GeoRegionsItemEmphasisItemStyle(TypedDict, total=False):
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

class GeoRegionsItemEmphasisLabel(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
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
    rich: GeoRegionsItemEmphasisLabelRich
    richInheritPlainLabel: bool

class GeoRegionsItemEmphasisLabelRichStyle(TypedDict, total=False):
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

class GeoRegionsItemItemStyle(TypedDict, total=False):
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

class GeoRegionsItemLabel(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
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
    rich: GeoRegionsItemLabelRich
    richInheritPlainLabel: bool

class GeoRegionsItemLabelRichStyle(TypedDict, total=False):
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

class GeoRegionsItemSelect(TypedDict, total=False):
    itemStyle: GeoRegionsItemSelectItemStyle
    label: GeoRegionsItemSelectLabel

class GeoRegionsItemSelectItemStyle(TypedDict, total=False):
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

class GeoRegionsItemSelectLabel(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
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
    rich: GeoRegionsItemSelectLabelRich
    richInheritPlainLabel: bool

class GeoRegionsItemSelectLabelRichStyle(TypedDict, total=False):
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

class GeoRegionsItemTooltip(TypedDict, total=False):
    show: bool
    position: str
    formatter: Callable[..., Any] | str
    valueFormatter: str
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: GeoRegionsItemTooltipTextStyle
    extraCssText: str

class GeoRegionsItemTooltipTextStyle(TypedDict, total=False):
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

class GeoScaleLimit(TypedDict, total=False):
    min: int | float
    max: int | float

class GeoSelect(TypedDict, total=False):
    disabled: bool
    label: GeoSelectLabel
    itemStyle: GeoSelectItemStyle

class GeoSelectItemStyle(TypedDict, total=False):
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

class GeoSelectLabel(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
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
    rich: GeoSelectLabelRich
    richInheritPlainLabel: bool

class GeoSelectLabelRichStyle(TypedDict, total=False):
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

class GeoTooltip(TypedDict, total=False):
    show: bool
    position: str
    formatter: Callable[..., Any] | str
    valueFormatter: str
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: GeoTooltipTextStyle
    extraCssText: str

class GeoTooltipTextStyle(TypedDict, total=False):
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

class Globe(TypedDict, total=False):
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
    realisticMaterial: GlobeRealisticMaterial
    lambertMaterial: GlobeLambertMaterial
    colorMaterial: GlobeColorMaterial
    light: GlobeLight
    atmosphere: GlobeAtmosphere
    postEffect: GlobePostEffect
    temporalSuperSampling: GlobeTemporalSuperSampling
    viewControl: GlobeViewControl
    layers: list[GlobeLayersItem]

class GlobeAtmosphere(TypedDict, total=False):
    show: bool
    offset: int | float
    color: str
    glowPower: int | float
    innerGlowPower: int | float

class GlobeColorMaterial(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float

class GlobeLambertMaterial(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float

class GlobeLayersItem(TypedDict, total=False):
    show: bool
    type: str
    name: str
    blendTo: str
    intensity: int | float
    shading: str
    distance: int | float
    texture: str

class GlobeLight(TypedDict, total=False):
    main: GlobeLightMain
    ambient: GlobeLightAmbient
    ambientCubemap: GlobeLightAmbientCubemap

class GlobeLightAmbient(TypedDict, total=False):
    color: str
    intensity: int | float

class GlobeLightAmbientCubemap(TypedDict, total=False):
    texture: str
    diffuseIntensity: int | float
    specularIntensity: int | float

class GlobeLightMain(TypedDict, total=False):
    color: str
    intensity: int | float
    shadow: bool
    shadowQuality: str
    alpha: int | float
    beta: int | float
    time: Any

class GlobePostEffect(TypedDict, total=False):
    enable: bool
    bloom: GlobePostEffectBloom
    depthOfField: GlobePostEffectDepthOfField
    screenSpaceAmbientOcclusion: dict[str, Any]
    SSAO: GlobePostEffectSsao
    colorCorrection: GlobePostEffectColorCorrection
    FXAA: GlobePostEffectFxaa

class GlobePostEffectBloom(TypedDict, total=False):
    enable: bool
    bloomIntensity: int | float

class GlobePostEffectColorCorrection(TypedDict, total=False):
    enable: bool
    lookupTexture: str
    exposure: int | float
    brightness: int | float
    contrast: int | float
    saturation: int | float

class GlobePostEffectDepthOfField(TypedDict, total=False):
    enable: bool
    focalDistance: bool
    focalRange: bool
    fstop: int | float
    blurRadius: int | float

class GlobePostEffectFxaa(TypedDict, total=False):
    enable: bool

class GlobePostEffectSsao(TypedDict, total=False):
    enable: bool
    quality: str
    radius: int | float
    intensity: int | float

class GlobeRealisticMaterial(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float
    roughness: str | int | float
    metalness: str | int | float
    roughnessAdjust: int | float
    metalnessAdjust: int | float
    normalTexture: str

class GlobeTemporalSuperSampling(TypedDict, total=False):
    enable: bool

class GlobeViewControl(TypedDict, total=False):
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

class Graphic(TypedDict, total=False):
    id: str
    elements: Any

class Grid(TypedDict, total=False):
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
    outerBounds: GridOuterBounds
    outerBoundsContain: bool
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    tooltip: GridTooltip
    coordinateSystem: str
    coordinateSystemUsage: str
    coord: str | int | float
    calendarIndex: int | float
    calendarId: int | float
    matrixIndex: int | float
    matrixId: int | float

class Grid3D(TypedDict, total=False):
    show: bool
    boxWidth: int | float
    boxHeight: int | float
    boxDepth: int | float
    axisLine: Grid3DAxisLine
    axisLabel: Grid3DAxisLabel
    axisTick: Grid3DAxisTick
    splitLine: Grid3DSplitLine
    splitArea: Grid3DSplitArea
    axisPointer: Grid3DAxisPointer
    environment: str
    light: Grid3DLight
    postEffect: Grid3DPostEffect
    temporalSuperSampling: Grid3DTemporalSuperSampling
    viewControl: Grid3DViewControl
    zlevel: int | float
    left: str | int | float
    top: str | int | float
    right: str | int | float
    bottom: str | int | float
    width: str | int | float
    height: str | int | float

class Grid3DAxisLabel(TypedDict, total=False):
    show: bool
    margin: int | float
    interval: Callable[..., Any] | int | float
    formatter: Callable[..., Any] | str
    textStyle: Grid3DAxisLabelTextStyle

class Grid3DAxisLabelTextStyle(TypedDict, total=False):
    color: Callable[..., Any] | str | list[str]
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Grid3DAxisLine(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    lineStyle: Grid3DAxisLineLineStyle

class Grid3DAxisLineLineStyle(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Grid3DAxisPointer(TypedDict, total=False):
    show: bool
    lineStyle: Grid3DAxisPointerLineStyle
    label: Grid3DAxisPointerLabel

class Grid3DAxisPointerLabel(TypedDict, total=False):
    show: bool
    formatter: Callable[..., Any]
    margin: int | float
    textStyle: Grid3DAxisPointerLabelTextStyle

class Grid3DAxisPointerLabelTextStyle(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Grid3DAxisPointerLineStyle(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Grid3DAxisTick(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    length: int | float
    lineStyle: Grid3DAxisTickLineStyle

class Grid3DAxisTickLineStyle(TypedDict, total=False):
    color: str | list[str]
    opacity: int | float
    width: int | float

class Grid3DLight(TypedDict, total=False):
    main: Grid3DLightMain
    ambient: Grid3DLightAmbient
    ambientCubemap: Grid3DLightAmbientCubemap

class Grid3DLightAmbient(TypedDict, total=False):
    color: str
    intensity: int | float

class Grid3DLightAmbientCubemap(TypedDict, total=False):
    texture: str
    diffuseIntensity: int | float
    specularIntensity: int | float

class Grid3DLightMain(TypedDict, total=False):
    color: str
    intensity: int | float
    shadow: bool
    shadowQuality: str
    alpha: int | float
    beta: int | float

class Grid3DPostEffect(TypedDict, total=False):
    enable: bool
    bloom: Grid3DPostEffectBloom
    depthOfField: Grid3DPostEffectDepthOfField
    screenSpaceAmbientOcclusion: dict[str, Any]
    SSAO: Grid3DPostEffectSsao
    colorCorrection: Grid3DPostEffectColorCorrection
    FXAA: Grid3DPostEffectFxaa

class Grid3DPostEffectBloom(TypedDict, total=False):
    enable: bool
    bloomIntensity: int | float

class Grid3DPostEffectColorCorrection(TypedDict, total=False):
    enable: bool
    lookupTexture: str
    exposure: int | float
    brightness: int | float
    contrast: int | float
    saturation: int | float

class Grid3DPostEffectDepthOfField(TypedDict, total=False):
    enable: bool
    focalDistance: bool
    focalRange: bool
    fstop: int | float
    blurRadius: int | float

class Grid3DPostEffectFxaa(TypedDict, total=False):
    enable: bool

class Grid3DPostEffectSsao(TypedDict, total=False):
    enable: bool
    quality: str
    radius: int | float
    intensity: int | float

class Grid3DSplitArea(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    areaStyle: Grid3DSplitAreaAreaStyle

class Grid3DSplitAreaAreaStyle(TypedDict, total=False):
    color: Any

class Grid3DSplitLine(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    lineStyle: Grid3DSplitLineLineStyle

class Grid3DSplitLineLineStyle(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Grid3DTemporalSuperSampling(TypedDict, total=False):
    enable: bool

class Grid3DViewControl(TypedDict, total=False):
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

class GridOuterBounds(TypedDict, total=False):
    left: str | int | float
    top: str | int | float
    right: str | int | float
    bottom: str | int | float
    width: str | int | float
    height: str | int | float

class GridTooltip(TypedDict, total=False):
    show: bool
    trigger: Literal["item", "axis", "none"]
    axisPointer: GridTooltipAxisPointer
    position: str
    formatter: Callable[..., Any] | str
    valueFormatter: str
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: GridTooltipTextStyle
    extraCssText: str

class GridTooltipAxisPointer(TypedDict, total=False):
    type: Literal["none", "line", "shadow", "cross"]
    axis: str
    snap: bool
    z: int | float
    label: GridTooltipAxisPointerLabel
    lineStyle: GridTooltipAxisPointerLineStyle
    shadowStyle: GridTooltipAxisPointerShadowStyle
    crossStyle: GridTooltipAxisPointerCrossStyle
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: Callable[..., Any] | int | float

class GridTooltipAxisPointerCrossStyle(TypedDict, total=False):
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

class GridTooltipAxisPointerLabel(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: Callable[..., Any] | str
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

class GridTooltipAxisPointerLineStyle(TypedDict, total=False):
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

class GridTooltipAxisPointerShadowStyle(TypedDict, total=False):
    color: str | list[str]
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class GridTooltipTextStyle(TypedDict, total=False):
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

class Legend(TypedDict, total=False):
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
    itemStyle: LegendItemStyle
    lineStyle: LegendLineStyle
    symbolRotate: str | int | float
    formatter: Callable[..., Any] | str
    selectedMode: bool | str
    inactiveColor: str | list[str]
    inactiveBorderColor: str | list[str]
    inactiveBorderWidth: str | int | float
    selected: dict[str, Any]
    textStyle: LegendTextStyle
    tooltip: dict[str, Any]
    icon: str
    data: list[LegendDataItem]
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
    pageFormatter: Callable[..., Any] | str
    pageIcons: LegendPageIcons
    pageIconColor: str
    pageIconInactiveColor: str
    pageIconSize: int | float
    pageTextStyle: LegendPageTextStyle
    animation: bool
    animationDurationUpdate: int | float
    emphasis: LegendEmphasis
    selector: bool
    selectorLabel: LegendSelectorLabel
    selectorPosition: Literal["auto", "start", "end"]
    selectorItemGap: int | float
    selectorButtonGap: int | float
    triggerEvent: bool

class LegendDataItem(TypedDict, total=False):
    name: str
    icon: str
    itemStyle: LegendDataItemItemStyle
    lineStyle: LegendDataItemLineStyle
    inactiveColor: str | list[str]
    inactiveBorderColor: str | list[str]
    inactiveBorderWidth: str | int | float
    symbolRotate: str | int | float
    textStyle: LegendDataItemTextStyle

class LegendDataItemItemStyle(TypedDict, total=False):
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
    decal: LegendDataItemItemStyleDecal

class LegendDataItemItemStyleDecal(TypedDict, total=False):
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

class LegendDataItemLineStyle(TypedDict, total=False):
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

class LegendDataItemTextStyle(TypedDict, total=False):
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

class LegendEmphasis(TypedDict, total=False):
    selectorLabel: LegendEmphasisSelectorLabel

class LegendEmphasisSelectorLabel(TypedDict, total=False):
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
    rich: LegendEmphasisSelectorLabelRich
    richInheritPlainLabel: bool

class LegendEmphasisSelectorLabelRichStyle(TypedDict, total=False):
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

class LegendItemStyle(TypedDict, total=False):
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
    decal: LegendItemStyleDecal

class LegendItemStyleDecal(TypedDict, total=False):
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

class LegendLineStyle(TypedDict, total=False):
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

class LegendPageIcons(TypedDict, total=False):
    horizontal: Any
    vertical: Any

class LegendPageTextStyle(TypedDict, total=False):
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

class LegendSelectorLabel(TypedDict, total=False):
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
    rich: LegendSelectorLabelRich
    richInheritPlainLabel: bool

class LegendSelectorLabelRichStyle(TypedDict, total=False):
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

class LegendTextStyle(TypedDict, total=False):
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
    rich: LegendTextStyleRich
    richInheritPlainLabel: bool

class LegendTextStyleRichStyle(TypedDict, total=False):
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

class Mapbox3D(TypedDict, total=False):
    style: str | dict[str, Any]
    center: Any
    zoom: int | float
    bearing: int | float
    pitch: int | float
    altitudeScale: int | float
    shading: str
    realisticMaterial: Mapbox3DRealisticMaterial
    lambertMaterial: Mapbox3DLambertMaterial
    colorMaterial: Mapbox3DColorMaterial
    light: Mapbox3DLight
    postEffect: Mapbox3DPostEffect
    temporalSuperSampling: Mapbox3DTemporalSuperSampling

class Mapbox3DColorMaterial(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float

class Mapbox3DLambertMaterial(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float

class Mapbox3DLight(TypedDict, total=False):
    main: Mapbox3DLightMain
    ambient: Mapbox3DLightAmbient
    ambientCubemap: Mapbox3DLightAmbientCubemap

class Mapbox3DLightAmbient(TypedDict, total=False):
    color: str
    intensity: int | float

class Mapbox3DLightAmbientCubemap(TypedDict, total=False):
    texture: str
    diffuseIntensity: int | float
    specularIntensity: int | float

class Mapbox3DLightMain(TypedDict, total=False):
    color: str
    intensity: int | float
    shadow: bool
    shadowQuality: str
    alpha: int | float
    beta: int | float

class Mapbox3DPostEffect(TypedDict, total=False):
    enable: bool
    bloom: Mapbox3DPostEffectBloom
    depthOfField: Mapbox3DPostEffectDepthOfField
    screenSpaceAmbientOcclusion: dict[str, Any]
    SSAO: Mapbox3DPostEffectSsao
    colorCorrection: Mapbox3DPostEffectColorCorrection
    FXAA: Mapbox3DPostEffectFxaa

class Mapbox3DPostEffectBloom(TypedDict, total=False):
    enable: bool
    bloomIntensity: int | float

class Mapbox3DPostEffectColorCorrection(TypedDict, total=False):
    enable: bool
    lookupTexture: str
    exposure: int | float
    brightness: int | float
    contrast: int | float
    saturation: int | float

class Mapbox3DPostEffectDepthOfField(TypedDict, total=False):
    enable: bool
    focalDistance: bool
    focalRange: bool
    fstop: int | float
    blurRadius: int | float

class Mapbox3DPostEffectFxaa(TypedDict, total=False):
    enable: bool

class Mapbox3DPostEffectSsao(TypedDict, total=False):
    enable: bool
    quality: str
    radius: int | float
    intensity: int | float

class Mapbox3DRealisticMaterial(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float
    roughness: str | int | float
    metalness: str | int | float
    roughnessAdjust: int | float
    metalnessAdjust: int | float
    normalTexture: str

class Mapbox3DTemporalSuperSampling(TypedDict, total=False):
    enable: bool

class Matrix(TypedDict, total=False):
    id: str
    zlevel: int | float
    z: int | float
    left: str | int | float
    top: str | int | float
    right: str | int | float
    bottom: str | int | float
    width: str | int | float
    height: str | int | float
    x: MatrixX
    y: MatrixY
    body: MatrixBody
    corner: MatrixCorner
    backgroundStyle: MatrixBackgroundStyle
    borderZ2: int | float
    tooltip: dict[str, Any]
    triggerEvent: bool

class MatrixBackgroundStyle(TypedDict, total=False):
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

class MatrixBody(TypedDict, total=False):
    data: list[MatrixBodyDataItem]
    label: MatrixBodyLabel
    itemStyle: MatrixBodyItemStyle
    silent: bool
    cursor: str
    z2: int | float

class MatrixBodyDataItem(TypedDict, total=False):
    coord: Any
    coordClamp: bool
    mergeCells: bool
    value: str | int | float

class MatrixBodyItemStyle(TypedDict, total=False):
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

class MatrixBodyLabel(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
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
    rich: MatrixBodyLabelRich
    richInheritPlainLabel: bool

class MatrixBodyLabelRichStyle(TypedDict, total=False):
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

class MatrixCorner(TypedDict, total=False):
    data: list[MatrixCornerDataItem]
    label: MatrixCornerLabel
    itemStyle: MatrixCornerItemStyle
    silent: bool
    cursor: str
    z2: int | float

class MatrixCornerDataItem(TypedDict, total=False):
    coord: Any
    coordClamp: bool
    mergeCells: bool
    value: str | int | float

class MatrixCornerItemStyle(TypedDict, total=False):
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

class MatrixCornerLabel(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
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
    rich: MatrixCornerLabelRich
    richInheritPlainLabel: bool

class MatrixCornerLabelRichStyle(TypedDict, total=False):
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

class MatrixX(TypedDict, total=False):
    show: bool
    data: list[MatrixXDataItem]
    length: int | float
    label: MatrixXLabel
    itemStyle: MatrixXItemStyle
    silent: bool
    cursor: str
    z2: int | float
    levelSize: str | int | float
    levels: list[MatrixXLevelsItem]
    dividerLineStyle: MatrixXDividerLineStyle

class MatrixXDataItem(TypedDict, total=False):
    value: str | int | float
    children: Any
    size: int | float

class MatrixXDividerLineStyle(TypedDict, total=False):
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

class MatrixXItemStyle(TypedDict, total=False):
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

class MatrixXLabel(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
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
    rich: MatrixXLabelRich
    richInheritPlainLabel: bool

class MatrixXLabelRichStyle(TypedDict, total=False):
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

class MatrixXLevelsItem(TypedDict, total=False):
    levelSize: str | int | float

class MatrixY(TypedDict, total=False):
    show: bool
    data: list[MatrixYDataItem]
    length: int | float
    label: MatrixYLabel
    itemStyle: MatrixYItemStyle
    silent: bool
    cursor: str
    z2: int | float
    levelSize: str | int | float
    levels: list[MatrixYLevelsItem]
    dividerLineStyle: MatrixYDividerLineStyle

class MatrixYDataItem(TypedDict, total=False):
    value: str | int | float
    children: Any
    size: int | float

class MatrixYDividerLineStyle(TypedDict, total=False):
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

class MatrixYItemStyle(TypedDict, total=False):
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

class MatrixYLabel(TypedDict, total=False):
    show: bool
    position: Literal["top", "left", "right", "bottom", "inside", "insideLeft", "insideRight", "insideTop", "insideBottom", "insideTopLeft", "insideBottomLeft", "insideTopRight", "insideBottomRight", "outside"]
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
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
    rich: MatrixYLabelRich
    richInheritPlainLabel: bool

class MatrixYLabelRichStyle(TypedDict, total=False):
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

class MatrixYLevelsItem(TypedDict, total=False):
    levelSize: str | int | float

class Parallel(TypedDict, total=False):
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
    parallelAxisDefault: ParallelParallelAxisDefault

class ParallelAxis(TypedDict, total=False):
    id: str
    dim: int | float
    parallelIndex: int | float
    realtime: bool
    areaSelectStyle: ParallelAxisAreaSelectStyle
    type: str
    name: str
    nameLocation: Literal["start", "middle", "end"]
    nameTextStyle: ParallelAxisNameTextStyle
    nameGap: int | float
    nameRotate: int | float
    nameTruncate: ParallelAxisNameTruncate
    inverse: bool
    boundaryGap: bool
    containShape: bool
    min: Callable[..., Any] | str | int | float
    max: Callable[..., Any] | str | int | float
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
    axisLine: ParallelAxisAxisLine
    axisTick: ParallelAxisAxisTick
    minorTick: ParallelAxisMinorTick
    axisLabel: ParallelAxisAxisLabel
    data: list[ParallelAxisDataItem]
    tooltip: ParallelAxisTooltip
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: Callable[..., Any] | int | float

class ParallelAxisAreaSelectStyle(TypedDict, total=False):
    width: int | float
    borderWidth: int | float
    borderColor: str | list[str]
    color: str | list[str]
    opacity: int | float

class ParallelAxisAxisLabel(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    rotate: int | float
    margin: int | float
    formatter: Callable[..., Any] | str
    showMinLabel: bool
    showMaxLabel: bool
    hideOverlap: bool
    customValues: Any
    color: Callable[..., Any] | str | list[str]
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
    rich: ParallelAxisAxisLabelRich
    richInheritPlainLabel: bool

class ParallelAxisAxisLabelRichStyle(TypedDict, total=False):
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

class ParallelAxisAxisLine(TypedDict, total=False):
    show: bool
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: ParallelAxisAxisLineLineStyle

class ParallelAxisAxisLineLineStyle(TypedDict, total=False):
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

class ParallelAxisAxisTick(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    length: int | float
    lineStyle: ParallelAxisAxisTickLineStyle
    customValues: Any

class ParallelAxisAxisTickLineStyle(TypedDict, total=False):
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

class ParallelAxisDataItem(TypedDict, total=False):
    value: str
    textStyle: ParallelAxisDataItemTextStyle

class ParallelAxisDataItemTextStyle(TypedDict, total=False):
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
    rich: ParallelAxisDataItemTextStyleRich
    richInheritPlainLabel: bool

class ParallelAxisDataItemTextStyleRichStyle(TypedDict, total=False):
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

class ParallelAxisMinorTick(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: ParallelAxisMinorTickLineStyle

class ParallelAxisMinorTickLineStyle(TypedDict, total=False):
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

class ParallelAxisNameTextStyle(TypedDict, total=False):
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
    rich: ParallelAxisNameTextStyleRich
    richInheritPlainLabel: bool

class ParallelAxisNameTextStyleRichStyle(TypedDict, total=False):
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

class ParallelAxisNameTruncate(TypedDict, total=False):
    maxWidth: int | float
    ellipsis: str

class ParallelAxisTooltip(TypedDict, total=False):
    show: bool
    position: str
    formatter: Callable[..., Any] | str
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: ParallelAxisTooltipTextStyle
    extraCssText: str

class ParallelAxisTooltipTextStyle(TypedDict, total=False):
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

class ParallelParallelAxisDefault(TypedDict, total=False):
    type: str
    name: str
    nameLocation: Literal["start", "middle", "end"]
    nameTextStyle: ParallelParallelAxisDefaultNameTextStyle
    nameGap: int | float
    nameRotate: int | float
    nameTruncate: ParallelParallelAxisDefaultNameTruncate
    inverse: bool
    boundaryGap: bool
    containShape: bool
    min: Callable[..., Any] | str | int | float
    max: Callable[..., Any] | str | int | float
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
    axisLine: ParallelParallelAxisDefaultAxisLine
    axisTick: ParallelParallelAxisDefaultAxisTick
    minorTick: ParallelParallelAxisDefaultMinorTick
    axisLabel: ParallelParallelAxisDefaultAxisLabel
    data: list[ParallelParallelAxisDefaultDataItem]
    tooltip: ParallelParallelAxisDefaultTooltip
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: Callable[..., Any] | int | float

class ParallelParallelAxisDefaultAxisLabel(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    rotate: int | float
    margin: int | float
    formatter: Callable[..., Any] | str
    showMinLabel: bool
    showMaxLabel: bool
    hideOverlap: bool
    customValues: Any
    color: Callable[..., Any] | str | list[str]
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
    rich: ParallelParallelAxisDefaultAxisLabelRich
    richInheritPlainLabel: bool

class ParallelParallelAxisDefaultAxisLabelRichStyle(TypedDict, total=False):
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

class ParallelParallelAxisDefaultAxisLine(TypedDict, total=False):
    show: bool
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: ParallelParallelAxisDefaultAxisLineLineStyle

class ParallelParallelAxisDefaultAxisLineLineStyle(TypedDict, total=False):
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

class ParallelParallelAxisDefaultAxisTick(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    length: int | float
    lineStyle: ParallelParallelAxisDefaultAxisTickLineStyle
    customValues: Any

class ParallelParallelAxisDefaultAxisTickLineStyle(TypedDict, total=False):
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

class ParallelParallelAxisDefaultDataItem(TypedDict, total=False):
    value: str
    textStyle: ParallelParallelAxisDefaultDataItemTextStyle

class ParallelParallelAxisDefaultDataItemTextStyle(TypedDict, total=False):
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
    rich: ParallelParallelAxisDefaultDataItemTextStyleRich
    richInheritPlainLabel: bool

class ParallelParallelAxisDefaultDataItemTextStyleRichStyle(TypedDict, total=False):
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

class ParallelParallelAxisDefaultMinorTick(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: ParallelParallelAxisDefaultMinorTickLineStyle

class ParallelParallelAxisDefaultMinorTickLineStyle(TypedDict, total=False):
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

class ParallelParallelAxisDefaultNameTextStyle(TypedDict, total=False):
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
    rich: ParallelParallelAxisDefaultNameTextStyleRich
    richInheritPlainLabel: bool

class ParallelParallelAxisDefaultNameTextStyleRichStyle(TypedDict, total=False):
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

class ParallelParallelAxisDefaultNameTruncate(TypedDict, total=False):
    maxWidth: int | float
    ellipsis: str

class ParallelParallelAxisDefaultTooltip(TypedDict, total=False):
    show: bool
    position: str
    formatter: Callable[..., Any] | str
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: ParallelParallelAxisDefaultTooltipTextStyle
    extraCssText: str

class ParallelParallelAxisDefaultTooltipTextStyle(TypedDict, total=False):
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

class Polar(TypedDict, total=False):
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
    tooltip: PolarTooltip

class PolarTooltip(TypedDict, total=False):
    show: bool
    trigger: Literal["item", "axis", "none"]
    axisPointer: PolarTooltipAxisPointer
    position: str
    formatter: Callable[..., Any] | str
    valueFormatter: str
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: PolarTooltipTextStyle
    extraCssText: str

class PolarTooltipAxisPointer(TypedDict, total=False):
    type: Literal["none", "line", "shadow", "cross"]
    axis: str
    snap: bool
    z: int | float
    label: PolarTooltipAxisPointerLabel
    lineStyle: PolarTooltipAxisPointerLineStyle
    shadowStyle: PolarTooltipAxisPointerShadowStyle
    crossStyle: PolarTooltipAxisPointerCrossStyle
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: Callable[..., Any] | int | float

class PolarTooltipAxisPointerCrossStyle(TypedDict, total=False):
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

class PolarTooltipAxisPointerLabel(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: Callable[..., Any] | str
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

class PolarTooltipAxisPointerLineStyle(TypedDict, total=False):
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

class PolarTooltipAxisPointerShadowStyle(TypedDict, total=False):
    color: str | list[str]
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class PolarTooltipTextStyle(TypedDict, total=False):
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

class Radar(TypedDict, total=False):
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
    axisName: RadarAxisName
    axisNameGap: int | float
    splitNumber: int | float
    shape: Literal["polygon", "circle"]
    scale: bool
    silent: bool
    triggerEvent: bool
    axisLine: RadarAxisLine
    axisTick: RadarAxisTick
    axisLabel: RadarAxisLabel
    splitLine: RadarSplitLine
    splitArea: RadarSplitArea
    indicator: list[RadarIndicatorItem]

class RadarAxisLabel(TypedDict, total=False):
    show: bool
    rotate: int | float
    margin: int | float
    formatter: Callable[..., Any] | str
    showMinLabel: bool
    showMaxLabel: bool
    hideOverlap: bool
    customValues: Any
    color: Callable[..., Any] | str | list[str]
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
    rich: RadarAxisLabelRich
    richInheritPlainLabel: bool

class RadarAxisLabelRichStyle(TypedDict, total=False):
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

class RadarAxisLine(TypedDict, total=False):
    show: bool
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: RadarAxisLineLineStyle

class RadarAxisLineLineStyle(TypedDict, total=False):
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

class RadarAxisName(TypedDict, total=False):
    show: bool
    formatter: Callable[..., Any] | str
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
    rich: RadarAxisNameRich
    richInheritPlainLabel: bool

class RadarAxisNameRichStyle(TypedDict, total=False):
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

class RadarAxisTick(TypedDict, total=False):
    show: bool
    length: int | float
    lineStyle: RadarAxisTickLineStyle
    customValues: Any

class RadarAxisTickLineStyle(TypedDict, total=False):
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

class RadarIndicatorItem(TypedDict, total=False):
    name: str
    max: int | float
    min: int | float
    color: str

class RadarSplitArea(TypedDict, total=False):
    show: bool
    areaStyle: RadarSplitAreaAreaStyle

class RadarSplitAreaAreaStyle(TypedDict, total=False):
    color: Any
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class RadarSplitLine(TypedDict, total=False):
    show: bool
    showMinLine: bool
    showMaxLine: bool
    lineStyle: RadarSplitLineLineStyle

class RadarSplitLineLineStyle(TypedDict, total=False):
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

class RadiusAxis(TypedDict, total=False):
    id: str
    polarIndex: int | float
    type: str
    name: str
    nameLocation: Literal["start", "middle", "end"]
    nameTextStyle: RadiusAxisNameTextStyle
    nameGap: int | float
    nameRotate: int | float
    nameTruncate: RadiusAxisNameTruncate
    inverse: bool
    boundaryGap: bool
    containShape: bool
    min: Callable[..., Any] | str | int | float
    max: Callable[..., Any] | str | int | float
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
    axisLine: RadiusAxisAxisLine
    axisTick: RadiusAxisAxisTick
    minorTick: RadiusAxisMinorTick
    axisLabel: RadiusAxisAxisLabel
    splitLine: RadiusAxisSplitLine
    minorSplitLine: RadiusAxisMinorSplitLine
    splitArea: RadiusAxisSplitArea
    data: list[RadiusAxisDataItem]
    axisPointer: RadiusAxisAxisPointer
    tooltip: RadiusAxisTooltip
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: Callable[..., Any] | int | float
    zlevel: int | float
    z: int | float

class RadiusAxisAxisLabel(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    rotate: int | float
    margin: int | float
    formatter: Callable[..., Any] | str
    showMinLabel: bool
    showMaxLabel: bool
    hideOverlap: bool
    customValues: Any
    color: Callable[..., Any] | str | list[str]
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
    rich: RadiusAxisAxisLabelRich
    richInheritPlainLabel: bool

class RadiusAxisAxisLabelRichStyle(TypedDict, total=False):
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

class RadiusAxisAxisLine(TypedDict, total=False):
    show: bool
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: RadiusAxisAxisLineLineStyle

class RadiusAxisAxisLineLineStyle(TypedDict, total=False):
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

class RadiusAxisAxisPointer(TypedDict, total=False):
    show: bool
    type: Literal["line", "shadow", "none"]
    snap: bool
    z: int | float
    label: RadiusAxisAxisPointerLabel
    lineStyle: RadiusAxisAxisPointerLineStyle
    shadowStyle: RadiusAxisAxisPointerShadowStyle
    triggerEmphasis: bool
    triggerTooltip: bool
    value: int | float
    status: Literal["show", "hide"]
    handle: RadiusAxisAxisPointerHandle

class RadiusAxisAxisPointerHandle(TypedDict, total=False):
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

class RadiusAxisAxisPointerLabel(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: Callable[..., Any] | str
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

class RadiusAxisAxisPointerLineStyle(TypedDict, total=False):
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

class RadiusAxisAxisPointerShadowStyle(TypedDict, total=False):
    color: str | list[str]
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class RadiusAxisAxisTick(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    length: int | float
    lineStyle: RadiusAxisAxisTickLineStyle
    customValues: Any

class RadiusAxisAxisTickLineStyle(TypedDict, total=False):
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

class RadiusAxisDataItem(TypedDict, total=False):
    value: str
    textStyle: RadiusAxisDataItemTextStyle

class RadiusAxisDataItemTextStyle(TypedDict, total=False):
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
    rich: RadiusAxisDataItemTextStyleRich
    richInheritPlainLabel: bool

class RadiusAxisDataItemTextStyleRichStyle(TypedDict, total=False):
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

class RadiusAxisMinorSplitLine(TypedDict, total=False):
    show: bool
    lineStyle: RadiusAxisMinorSplitLineLineStyle

class RadiusAxisMinorSplitLineLineStyle(TypedDict, total=False):
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

class RadiusAxisMinorTick(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: RadiusAxisMinorTickLineStyle

class RadiusAxisMinorTickLineStyle(TypedDict, total=False):
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

class RadiusAxisNameTextStyle(TypedDict, total=False):
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
    rich: RadiusAxisNameTextStyleRich
    richInheritPlainLabel: bool

class RadiusAxisNameTextStyleRichStyle(TypedDict, total=False):
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

class RadiusAxisNameTruncate(TypedDict, total=False):
    maxWidth: int | float
    ellipsis: str

class RadiusAxisSplitArea(TypedDict, total=False):
    interval: Callable[..., Any] | int | float
    show: bool
    areaStyle: RadiusAxisSplitAreaAreaStyle

class RadiusAxisSplitAreaAreaStyle(TypedDict, total=False):
    color: Any
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class RadiusAxisSplitLine(TypedDict, total=False):
    show: bool
    showMinLine: bool
    showMaxLine: bool
    interval: Callable[..., Any] | int | float
    lineStyle: RadiusAxisSplitLineLineStyle

class RadiusAxisSplitLineLineStyle(TypedDict, total=False):
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

class RadiusAxisTooltip(TypedDict, total=False):
    show: bool
    position: str
    formatter: Callable[..., Any] | str
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: RadiusAxisTooltipTextStyle
    extraCssText: str

class RadiusAxisTooltipTextStyle(TypedDict, total=False):
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

class SingleAxis(TypedDict, total=False):
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
    nameTextStyle: SingleAxisNameTextStyle
    nameGap: int | float
    nameRotate: int | float
    nameTruncate: SingleAxisNameTruncate
    inverse: bool
    boundaryGap: bool
    containShape: bool
    min: Callable[..., Any] | str | int | float
    max: Callable[..., Any] | str | int | float
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
    axisLine: SingleAxisAxisLine
    axisTick: SingleAxisAxisTick
    minorTick: SingleAxisMinorTick
    axisLabel: SingleAxisAxisLabel
    splitLine: SingleAxisSplitLine
    minorSplitLine: SingleAxisMinorSplitLine
    splitArea: SingleAxisSplitArea
    data: list[SingleAxisDataItem]
    axisPointer: SingleAxisAxisPointer
    tooltip: SingleAxisTooltip
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: Callable[..., Any] | int | float

class SingleAxisAxisLabel(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    rotate: int | float
    margin: int | float
    formatter: Callable[..., Any] | str
    showMinLabel: bool
    showMaxLabel: bool
    hideOverlap: bool
    customValues: Any
    color: Callable[..., Any] | str | list[str]
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
    rich: SingleAxisAxisLabelRich
    richInheritPlainLabel: bool

class SingleAxisAxisLabelRichStyle(TypedDict, total=False):
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

class SingleAxisAxisLine(TypedDict, total=False):
    show: bool
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: SingleAxisAxisLineLineStyle

class SingleAxisAxisLineLineStyle(TypedDict, total=False):
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

class SingleAxisAxisPointer(TypedDict, total=False):
    show: bool
    type: Literal["line", "shadow", "none"]
    snap: bool
    z: int | float
    label: SingleAxisAxisPointerLabel
    lineStyle: SingleAxisAxisPointerLineStyle
    shadowStyle: SingleAxisAxisPointerShadowStyle
    triggerEmphasis: bool
    triggerTooltip: bool
    value: int | float
    status: Literal["show", "hide"]
    handle: SingleAxisAxisPointerHandle

class SingleAxisAxisPointerHandle(TypedDict, total=False):
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

class SingleAxisAxisPointerLabel(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: Callable[..., Any] | str
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

class SingleAxisAxisPointerLineStyle(TypedDict, total=False):
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

class SingleAxisAxisPointerShadowStyle(TypedDict, total=False):
    color: str | list[str]
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class SingleAxisAxisTick(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    length: int | float
    lineStyle: SingleAxisAxisTickLineStyle
    customValues: Any

class SingleAxisAxisTickLineStyle(TypedDict, total=False):
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

class SingleAxisDataItem(TypedDict, total=False):
    value: str
    textStyle: SingleAxisDataItemTextStyle

class SingleAxisDataItemTextStyle(TypedDict, total=False):
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
    rich: SingleAxisDataItemTextStyleRich
    richInheritPlainLabel: bool

class SingleAxisDataItemTextStyleRichStyle(TypedDict, total=False):
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

class SingleAxisMinorSplitLine(TypedDict, total=False):
    show: bool
    lineStyle: SingleAxisMinorSplitLineLineStyle

class SingleAxisMinorSplitLineLineStyle(TypedDict, total=False):
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

class SingleAxisMinorTick(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: SingleAxisMinorTickLineStyle

class SingleAxisMinorTickLineStyle(TypedDict, total=False):
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

class SingleAxisNameTextStyle(TypedDict, total=False):
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
    rich: SingleAxisNameTextStyleRich
    richInheritPlainLabel: bool

class SingleAxisNameTextStyleRichStyle(TypedDict, total=False):
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

class SingleAxisNameTruncate(TypedDict, total=False):
    maxWidth: int | float
    ellipsis: str

class SingleAxisSplitArea(TypedDict, total=False):
    interval: Callable[..., Any] | int | float
    show: bool
    areaStyle: SingleAxisSplitAreaAreaStyle

class SingleAxisSplitAreaAreaStyle(TypedDict, total=False):
    color: Any
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class SingleAxisSplitLine(TypedDict, total=False):
    show: bool
    showMinLine: bool
    showMaxLine: bool
    interval: Callable[..., Any] | int | float
    lineStyle: SingleAxisSplitLineLineStyle

class SingleAxisSplitLineLineStyle(TypedDict, total=False):
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

class SingleAxisTooltip(TypedDict, total=False):
    show: bool
    trigger: Literal["item", "axis", "none"]
    axisPointer: SingleAxisTooltipAxisPointer
    position: str
    formatter: Callable[..., Any] | str
    valueFormatter: str
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: SingleAxisTooltipTextStyle
    extraCssText: str

class SingleAxisTooltipAxisPointer(TypedDict, total=False):
    type: Literal["none", "line", "shadow", "cross"]
    axis: str
    snap: bool
    z: int | float
    label: SingleAxisTooltipAxisPointerLabel
    lineStyle: SingleAxisTooltipAxisPointerLineStyle
    shadowStyle: SingleAxisTooltipAxisPointerShadowStyle
    crossStyle: SingleAxisTooltipAxisPointerCrossStyle
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: Callable[..., Any] | int | float

class SingleAxisTooltipAxisPointerCrossStyle(TypedDict, total=False):
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

class SingleAxisTooltipAxisPointerLabel(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: Callable[..., Any] | str
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

class SingleAxisTooltipAxisPointerLineStyle(TypedDict, total=False):
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

class SingleAxisTooltipAxisPointerShadowStyle(TypedDict, total=False):
    color: str | list[str]
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class SingleAxisTooltipTextStyle(TypedDict, total=False):
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

class StateAnimation(TypedDict, total=False):
    duration: int | float
    easing: str

class TextStyle(TypedDict, total=False):
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

class Thumbnail(TypedDict, total=False):
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
    itemStyle: ThumbnailItemStyle
    windowStyle: ThumbnailWindowStyle
    seriesIndex: int | float
    seriesId: str | int | float

class ThumbnailItemStyle(TypedDict, total=False):
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

class ThumbnailWindowStyle(TypedDict, total=False):
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

class Timeline(TypedDict, total=False):
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
    lineStyle: TimelineLineStyle
    label: TimelineLabel
    itemStyle: TimelineItemStyle
    checkpointStyle: TimelineCheckpointStyle
    controlStyle: TimelineControlStyle
    progress: TimelineProgress
    emphasis: TimelineEmphasis
    data: Any

class TimelineCheckpointStyle(TypedDict, total=False):
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

class TimelineControlStyle(TypedDict, total=False):
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

class TimelineEmphasis(TypedDict, total=False):
    label: TimelineEmphasisLabel
    itemStyle: TimelineEmphasisItemStyle
    checkpointStyle: dict[str, Any]
    controlStyle: dict[str, Any]

class TimelineEmphasisItemStyle(TypedDict, total=False):
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

class TimelineEmphasisLabel(TypedDict, total=False):
    show: bool
    interval: str | int | float
    rotate: Any
    formatter: Callable[..., Any] | str
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
    rich: TimelineEmphasisLabelRich
    richInheritPlainLabel: bool

class TimelineEmphasisLabelRichStyle(TypedDict, total=False):
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

class TimelineItemStyle(TypedDict, total=False):
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

class TimelineLabel(TypedDict, total=False):
    position: Literal["auto", "left", "right", "top", "bottom"]
    show: bool
    interval: str | int | float
    rotate: Any
    formatter: Callable[..., Any] | str
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
    rich: TimelineLabelRich
    richInheritPlainLabel: bool

class TimelineLabelRichStyle(TypedDict, total=False):
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

class TimelineLineStyle(TypedDict, total=False):
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

class TimelineProgress(TypedDict, total=False):
    lineStyle: TimelineProgressLineStyle
    itemStyle: TimelineProgressItemStyle
    label: TimelineProgressLabel

class TimelineProgressItemStyle(TypedDict, total=False):
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

class TimelineProgressLabel(TypedDict, total=False):
    show: bool
    interval: str | int | float
    rotate: Any
    formatter: Callable[..., Any] | str
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
    rich: TimelineProgressLabelRich
    richInheritPlainLabel: bool

class TimelineProgressLabelRichStyle(TypedDict, total=False):
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

class TimelineProgressLineStyle(TypedDict, total=False):
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

class Title(TypedDict, total=False):
    id: str
    show: bool
    text: str
    link: str
    target: str
    textStyle: TitleTextStyle
    subtext: str
    sublink: str
    subtarget: str
    subtextStyle: TitleSubtextStyle
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

class TitleSubtextStyle(TypedDict, total=False):
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
    rich: TitleSubtextStyleRich
    richInheritPlainLabel: bool

class TitleSubtextStyleRichStyle(TypedDict, total=False):
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

class TitleTextStyle(TypedDict, total=False):
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
    rich: TitleTextStyleRich
    richInheritPlainLabel: bool

class TitleTextStyleRichStyle(TypedDict, total=False):
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

class Toolbox(TypedDict, total=False):
    id: str
    show: bool
    orient: Literal["vertical", "horizontal"]
    itemSize: int | float
    itemGap: int | float
    showTitle: bool
    feature: ToolboxFeature
    iconStyle: ToolboxIconStyle
    emphasis: ToolboxEmphasis
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

class ToolboxEmphasis(TypedDict, total=False):
    iconStyle: ToolboxEmphasisIconStyle

class ToolboxEmphasisIconStyle(TypedDict, total=False):
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

class ToolboxFeature(TypedDict, total=False):
    saveAsImage: ToolboxFeatureSaveAsImage
    restore: ToolboxFeatureRestore
    dataView: ToolboxFeatureDataView
    dataZoom: ToolboxFeatureDataZoom
    magicType: ToolboxFeatureMagicType
    brush: ToolboxFeatureBrush

class ToolboxFeatureBrush(TypedDict, total=False):
    type: Any
    icon: ToolboxFeatureBrushIcon
    title: ToolboxFeatureBrushTitle

class ToolboxFeatureBrushIcon(TypedDict, total=False):
    rect: str
    polygon: str
    lineX: str
    lineY: str
    keep: str
    clear: str

class ToolboxFeatureBrushTitle(TypedDict, total=False):
    rect: str
    polygon: str
    lineX: str
    lineY: str
    keep: str
    clear: str

class ToolboxFeatureDataView(TypedDict, total=False):
    show: bool
    title: str
    icon: str
    iconStyle: ToolboxFeatureDataViewIconStyle
    emphasis: ToolboxFeatureDataViewEmphasis
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

class ToolboxFeatureDataViewEmphasis(TypedDict, total=False):
    iconStyle: ToolboxFeatureDataViewEmphasisIconStyle

class ToolboxFeatureDataViewEmphasisIconStyle(TypedDict, total=False):
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

class ToolboxFeatureDataViewIconStyle(TypedDict, total=False):
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

class ToolboxFeatureDataZoom(TypedDict, total=False):
    show: bool
    title: ToolboxFeatureDataZoomTitle
    icon: ToolboxFeatureDataZoomIcon
    iconStyle: ToolboxFeatureDataZoomIconStyle
    emphasis: ToolboxFeatureDataZoomEmphasis
    filterMode: str
    xAxisIndex: bool | int | float
    yAxisIndex: bool | int | float
    brushStyle: ToolboxFeatureDataZoomBrushStyle

class ToolboxFeatureDataZoomBrushStyle(TypedDict, total=False):
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

class ToolboxFeatureDataZoomEmphasis(TypedDict, total=False):
    iconStyle: ToolboxFeatureDataZoomEmphasisIconStyle

class ToolboxFeatureDataZoomEmphasisIconStyle(TypedDict, total=False):
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

class ToolboxFeatureDataZoomIcon(TypedDict, total=False):
    zoom: str
    back: str

class ToolboxFeatureDataZoomIconStyle(TypedDict, total=False):
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

class ToolboxFeatureDataZoomTitle(TypedDict, total=False):
    zoom: str
    back: str

class ToolboxFeatureMagicType(TypedDict, total=False):
    show: bool
    type: Any
    title: ToolboxFeatureMagicTypeTitle
    icon: ToolboxFeatureMagicTypeIcon
    iconStyle: ToolboxFeatureMagicTypeIconStyle
    emphasis: ToolboxFeatureMagicTypeEmphasis
    option: ToolboxFeatureMagicTypeOption
    seriesIndex: ToolboxFeatureMagicTypeSeriesIndex

class ToolboxFeatureMagicTypeEmphasis(TypedDict, total=False):
    iconStyle: ToolboxFeatureMagicTypeEmphasisIconStyle

class ToolboxFeatureMagicTypeEmphasisIconStyle(TypedDict, total=False):
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

class ToolboxFeatureMagicTypeIcon(TypedDict, total=False):
    line: str
    bar: str
    stack: str

class ToolboxFeatureMagicTypeIconStyle(TypedDict, total=False):
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

class ToolboxFeatureMagicTypeOption(TypedDict, total=False):
    line: dict[str, Any]
    bar: dict[str, Any]
    stack: dict[str, Any]

class ToolboxFeatureMagicTypeSeriesIndex(TypedDict, total=False):
    line: Any
    bar: Any

class ToolboxFeatureMagicTypeTitle(TypedDict, total=False):
    line: str
    bar: str
    stack: str
    tiled: str

class ToolboxFeatureRestore(TypedDict, total=False):
    show: bool
    title: str
    icon: str
    iconStyle: ToolboxFeatureRestoreIconStyle
    emphasis: ToolboxFeatureRestoreEmphasis

class ToolboxFeatureRestoreEmphasis(TypedDict, total=False):
    iconStyle: ToolboxFeatureRestoreEmphasisIconStyle

class ToolboxFeatureRestoreEmphasisIconStyle(TypedDict, total=False):
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

class ToolboxFeatureRestoreIconStyle(TypedDict, total=False):
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

class ToolboxFeatureSaveAsImage(TypedDict, total=False):
    type: Literal["png", "jpg"]
    name: str
    backgroundColor: str | list[str]
    connectedBackgroundColor: str | list[str]
    excludeComponents: Any
    show: bool
    title: str
    icon: str
    iconStyle: ToolboxFeatureSaveAsImageIconStyle
    emphasis: ToolboxFeatureSaveAsImageEmphasis
    pixelRatio: int | float

class ToolboxFeatureSaveAsImageEmphasis(TypedDict, total=False):
    iconStyle: ToolboxFeatureSaveAsImageEmphasisIconStyle

class ToolboxFeatureSaveAsImageEmphasisIconStyle(TypedDict, total=False):
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

class ToolboxFeatureSaveAsImageIconStyle(TypedDict, total=False):
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

class ToolboxIconStyle(TypedDict, total=False):
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

class Tooltip(TypedDict, total=False):
    show: bool
    trigger: Literal["item", "axis", "none"]
    axisPointer: TooltipAxisPointer
    showContent: bool
    alwaysShowContent: bool
    triggerOn: Literal["mousemove", "click"]
    showDelay: int | float
    hideDelay: int | float
    enterable: bool
    renderMode: Literal["html", "richText"]
    confine: bool
    appendToBody: bool
    appendTo: Callable[..., Any] | str
    className: str
    transitionDuration: int | float
    displayTransition: bool
    position: str
    formatter: Callable[..., Any] | str
    valueFormatter: str
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: TooltipTextStyle
    extraCssText: str
    order: Literal["seriesAsc", "seriesDesc", "valueAsc", "valueDesc"]

class TooltipAxisPointer(TypedDict, total=False):
    type: Literal["none", "line", "shadow", "cross"]
    axis: str
    snap: bool
    z: int | float
    label: TooltipAxisPointerLabel
    lineStyle: TooltipAxisPointerLineStyle
    shadowStyle: TooltipAxisPointerShadowStyle
    crossStyle: TooltipAxisPointerCrossStyle
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: Callable[..., Any] | int | float

class TooltipAxisPointerCrossStyle(TypedDict, total=False):
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

class TooltipAxisPointerLabel(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: Callable[..., Any] | str
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

class TooltipAxisPointerLineStyle(TypedDict, total=False):
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

class TooltipAxisPointerShadowStyle(TypedDict, total=False):
    color: str | list[str]
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class TooltipTextStyle(TypedDict, total=False):
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

class XAxis(TypedDict, total=False):
    id: str
    show: bool
    gridIndex: int | float
    alignTicks: bool
    position: Literal["top", "bottom"]
    offset: int | float
    type: str
    name: str
    nameLocation: Literal["start", "middle", "end"]
    nameTextStyle: XAxisNameTextStyle
    nameGap: int | float
    nameRotate: int | float
    nameTruncate: XAxisNameTruncate
    nameMoveOverlap: bool
    inverse: bool
    boundaryGap: bool
    containShape: bool
    min: Callable[..., Any] | str | int | float
    max: Callable[..., Any] | str | int | float
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
    breaks: list[XAxisBreaksItem]
    breakArea: XAxisBreakArea
    breakLabelLayout: XAxisBreakLabelLayout
    axisLine: XAxisAxisLine
    axisTick: XAxisAxisTick
    minorTick: XAxisMinorTick
    axisLabel: XAxisAxisLabel
    splitLine: XAxisSplitLine
    minorSplitLine: XAxisMinorSplitLine
    splitArea: XAxisSplitArea
    data: list[XAxisDataItem]
    axisPointer: XAxisAxisPointer
    tooltip: XAxisTooltip
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: Callable[..., Any] | int | float
    zlevel: int | float
    z: int | float

class XAxis3D(TypedDict, total=False):
    show: bool
    name: str
    grid3DIndex: int | float
    nameTextStyle: XAxis3DNameTextStyle
    nameGap: int | float
    type: str
    min: str | int | float
    max: str | int | float
    scale: bool
    splitNumber: int | float
    minInterval: int | float
    interval: int | float
    logBase: int | float
    data: list[XAxis3DDataItem]
    axisLine: XAxis3DAxisLine
    axisLabel: XAxis3DAxisLabel
    axisTick: XAxis3DAxisTick
    splitLine: XAxis3DSplitLine
    splitArea: XAxis3DSplitArea
    axisPointer: XAxis3DAxisPointer

class XAxis3DAxisLabel(TypedDict, total=False):
    show: bool
    margin: int | float
    interval: Callable[..., Any] | int | float
    formatter: Callable[..., Any] | str
    textStyle: XAxis3DAxisLabelTextStyle

class XAxis3DAxisLabelTextStyle(TypedDict, total=False):
    color: Callable[..., Any] | str | list[str]
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class XAxis3DAxisLine(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    lineStyle: XAxis3DAxisLineLineStyle

class XAxis3DAxisLineLineStyle(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class XAxis3DAxisPointer(TypedDict, total=False):
    show: bool
    lineStyle: XAxis3DAxisPointerLineStyle
    label: XAxis3DAxisPointerLabel

class XAxis3DAxisPointerLabel(TypedDict, total=False):
    show: bool
    formatter: Callable[..., Any]
    margin: int | float
    textStyle: XAxis3DAxisPointerLabelTextStyle

class XAxis3DAxisPointerLabelTextStyle(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class XAxis3DAxisPointerLineStyle(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class XAxis3DAxisTick(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    length: int | float
    lineStyle: XAxis3DAxisTickLineStyle

class XAxis3DAxisTickLineStyle(TypedDict, total=False):
    color: str | list[str]
    opacity: int | float
    width: int | float

class XAxis3DDataItem(TypedDict, total=False):
    value: str
    textStyle: XAxis3DDataItemTextStyle

class XAxis3DDataItemTextStyle(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class XAxis3DNameTextStyle(TypedDict, total=False):
    color: str | list[str]
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class XAxis3DSplitArea(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    areaStyle: XAxis3DSplitAreaAreaStyle

class XAxis3DSplitAreaAreaStyle(TypedDict, total=False):
    color: Any

class XAxis3DSplitLine(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    lineStyle: XAxis3DSplitLineLineStyle

class XAxis3DSplitLineLineStyle(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class XAxisAxisLabel(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    rotate: int | float
    margin: int | float
    formatter: Callable[..., Any] | str
    showMinLabel: bool
    showMaxLabel: bool
    alignMinLabel: str
    alignMaxLabel: str
    hideOverlap: bool
    customValues: Any
    color: Callable[..., Any] | str | list[str]
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
    rich: XAxisAxisLabelRich
    richInheritPlainLabel: bool

class XAxisAxisLabelRichStyle(TypedDict, total=False):
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

class XAxisAxisLine(TypedDict, total=False):
    show: bool
    onZero: Literal["auto", "true", "false"]
    onZeroAxisIndex: int | float
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: XAxisAxisLineLineStyle

class XAxisAxisLineLineStyle(TypedDict, total=False):
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

class XAxisAxisPointer(TypedDict, total=False):
    show: bool
    type: Literal["line", "shadow", "none"]
    snap: bool
    z: int | float
    label: XAxisAxisPointerLabel
    lineStyle: XAxisAxisPointerLineStyle
    shadowStyle: XAxisAxisPointerShadowStyle
    triggerEmphasis: bool
    triggerTooltip: bool
    value: int | float
    status: Literal["show", "hide"]
    handle: XAxisAxisPointerHandle

class XAxisAxisPointerHandle(TypedDict, total=False):
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

class XAxisAxisPointerLabel(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: Callable[..., Any] | str
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

class XAxisAxisPointerLineStyle(TypedDict, total=False):
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

class XAxisAxisPointerShadowStyle(TypedDict, total=False):
    color: str | list[str]
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class XAxisAxisTick(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    length: int | float
    lineStyle: XAxisAxisTickLineStyle
    customValues: Any

class XAxisAxisTickLineStyle(TypedDict, total=False):
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

class XAxisBreakArea(TypedDict, total=False):
    show: bool
    itemStyle: XAxisBreakAreaItemStyle
    zigzagAmplitude: int | float
    zigzagMinSpan: int | float
    zigzagMaxSpan: int | float
    zigzagZ: int | float
    expandOnClick: bool

class XAxisBreakAreaItemStyle(TypedDict, total=False):
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

class XAxisBreakLabelLayout(TypedDict, total=False):
    moveOverlap: bool | str

class XAxisBreaksItem(TypedDict, total=False):
    start: str | int | float
    end: str | int | float
    gap: str | int | float
    isExpanded: bool

class XAxisDataItem(TypedDict, total=False):
    value: str
    textStyle: XAxisDataItemTextStyle

class XAxisDataItemTextStyle(TypedDict, total=False):
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
    rich: XAxisDataItemTextStyleRich
    richInheritPlainLabel: bool

class XAxisDataItemTextStyleRichStyle(TypedDict, total=False):
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

class XAxisMinorSplitLine(TypedDict, total=False):
    show: bool
    lineStyle: XAxisMinorSplitLineLineStyle

class XAxisMinorSplitLineLineStyle(TypedDict, total=False):
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

class XAxisMinorTick(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: XAxisMinorTickLineStyle

class XAxisMinorTickLineStyle(TypedDict, total=False):
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

class XAxisNameTextStyle(TypedDict, total=False):
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
    rich: XAxisNameTextStyleRich
    richInheritPlainLabel: bool

class XAxisNameTextStyleRichStyle(TypedDict, total=False):
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

class XAxisNameTruncate(TypedDict, total=False):
    maxWidth: int | float
    ellipsis: str

class XAxisSplitArea(TypedDict, total=False):
    interval: Callable[..., Any] | int | float
    show: bool
    areaStyle: XAxisSplitAreaAreaStyle

class XAxisSplitAreaAreaStyle(TypedDict, total=False):
    color: Any
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class XAxisSplitLine(TypedDict, total=False):
    show: bool
    showMinLine: bool
    showMaxLine: bool
    interval: Callable[..., Any] | int | float
    lineStyle: XAxisSplitLineLineStyle

class XAxisSplitLineLineStyle(TypedDict, total=False):
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

class XAxisTooltip(TypedDict, total=False):
    show: bool
    position: str
    formatter: Callable[..., Any] | str
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: XAxisTooltipTextStyle
    extraCssText: str

class XAxisTooltipTextStyle(TypedDict, total=False):
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

class YAxis(TypedDict, total=False):
    id: str
    show: bool
    gridIndex: int | float
    alignTicks: bool
    position: Literal["left", "right"]
    offset: int | float
    type: str
    name: str
    nameLocation: Literal["start", "middle", "end"]
    nameTextStyle: YAxisNameTextStyle
    nameGap: int | float
    nameRotate: int | float
    nameTruncate: YAxisNameTruncate
    nameMoveOverlap: bool
    inverse: bool
    boundaryGap: bool
    containShape: bool
    min: Callable[..., Any] | str | int | float
    max: Callable[..., Any] | str | int | float
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
    breaks: list[YAxisBreaksItem]
    breakArea: YAxisBreakArea
    breakLabelLayout: YAxisBreakLabelLayout
    axisLine: YAxisAxisLine
    axisTick: YAxisAxisTick
    minorTick: YAxisMinorTick
    axisLabel: YAxisAxisLabel
    splitLine: YAxisSplitLine
    minorSplitLine: YAxisMinorSplitLine
    splitArea: YAxisSplitArea
    data: list[YAxisDataItem]
    axisPointer: YAxisAxisPointer
    tooltip: YAxisTooltip
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: Literal["linear", "quadraticIn", "quadraticOut", "quadraticInOut", "cubicIn", "cubicOut", "cubicInOut", "quarticIn", "quarticOut", "quarticInOut", "quinticIn", "quinticOut", "quinticInOut", "sinusoidalIn", "sinusoidalOut", "sinusoidalInOut", "exponentialIn", "exponentialOut", "exponentialInOut", "circularIn", "circularOut", "circularInOut", "elasticIn", "elasticOut", "elasticInOut", "backIn", "backOut", "backInOut", "bounceIn", "bounceOut", "bounceInOut"]
    animationDelayUpdate: Callable[..., Any] | int | float
    zlevel: int | float
    z: int | float

class YAxis3D(TypedDict, total=False):
    show: bool
    name: str
    grid3DIndex: int | float
    nameTextStyle: YAxis3DNameTextStyle
    nameGap: int | float
    type: str
    min: str | int | float
    max: str | int | float
    scale: bool
    splitNumber: int | float
    minInterval: int | float
    interval: int | float
    logBase: int | float
    data: list[YAxis3DDataItem]
    axisLine: YAxis3DAxisLine
    axisLabel: YAxis3DAxisLabel
    axisTick: YAxis3DAxisTick
    splitLine: YAxis3DSplitLine
    splitArea: YAxis3DSplitArea
    axisPointer: YAxis3DAxisPointer

class YAxis3DAxisLabel(TypedDict, total=False):
    show: bool
    margin: int | float
    interval: Callable[..., Any] | int | float
    formatter: Callable[..., Any] | str
    textStyle: YAxis3DAxisLabelTextStyle

class YAxis3DAxisLabelTextStyle(TypedDict, total=False):
    color: Callable[..., Any] | str | list[str]
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class YAxis3DAxisLine(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    lineStyle: YAxis3DAxisLineLineStyle

class YAxis3DAxisLineLineStyle(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class YAxis3DAxisPointer(TypedDict, total=False):
    show: bool
    lineStyle: YAxis3DAxisPointerLineStyle
    label: YAxis3DAxisPointerLabel

class YAxis3DAxisPointerLabel(TypedDict, total=False):
    show: bool
    formatter: Callable[..., Any]
    margin: int | float
    textStyle: YAxis3DAxisPointerLabelTextStyle

class YAxis3DAxisPointerLabelTextStyle(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class YAxis3DAxisPointerLineStyle(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class YAxis3DAxisTick(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    length: int | float
    lineStyle: YAxis3DAxisTickLineStyle

class YAxis3DAxisTickLineStyle(TypedDict, total=False):
    color: str | list[str]
    opacity: int | float
    width: int | float

class YAxis3DDataItem(TypedDict, total=False):
    value: str
    textStyle: YAxis3DDataItemTextStyle

class YAxis3DDataItemTextStyle(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class YAxis3DNameTextStyle(TypedDict, total=False):
    color: str | list[str]
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class YAxis3DSplitArea(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    areaStyle: YAxis3DSplitAreaAreaStyle

class YAxis3DSplitAreaAreaStyle(TypedDict, total=False):
    color: Any

class YAxis3DSplitLine(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    lineStyle: YAxis3DSplitLineLineStyle

class YAxis3DSplitLineLineStyle(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class YAxisAxisLabel(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    rotate: int | float
    margin: int | float
    formatter: Callable[..., Any] | str
    showMinLabel: bool
    showMaxLabel: bool
    verticalAlignMinLabel: str
    verticalAlignMaxLabel: str
    hideOverlap: bool
    customValues: Any
    color: Callable[..., Any] | str | list[str]
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
    rich: YAxisAxisLabelRich
    richInheritPlainLabel: bool

class YAxisAxisLabelRichStyle(TypedDict, total=False):
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

class YAxisAxisLine(TypedDict, total=False):
    show: bool
    onZero: Literal["auto", "true", "false"]
    onZeroAxisIndex: int | float
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: YAxisAxisLineLineStyle

class YAxisAxisLineLineStyle(TypedDict, total=False):
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

class YAxisAxisPointer(TypedDict, total=False):
    show: bool
    type: Literal["line", "shadow", "none"]
    snap: bool
    z: int | float
    label: YAxisAxisPointerLabel
    lineStyle: YAxisAxisPointerLineStyle
    shadowStyle: YAxisAxisPointerShadowStyle
    triggerEmphasis: bool
    triggerTooltip: bool
    value: int | float
    status: Literal["show", "hide"]
    handle: YAxisAxisPointerHandle

class YAxisAxisPointerHandle(TypedDict, total=False):
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

class YAxisAxisPointerLabel(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: Callable[..., Any] | str
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

class YAxisAxisPointerLineStyle(TypedDict, total=False):
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

class YAxisAxisPointerShadowStyle(TypedDict, total=False):
    color: str | list[str]
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class YAxisAxisTick(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    length: int | float
    lineStyle: YAxisAxisTickLineStyle
    customValues: Any

class YAxisAxisTickLineStyle(TypedDict, total=False):
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

class YAxisBreakArea(TypedDict, total=False):
    show: bool
    itemStyle: YAxisBreakAreaItemStyle
    zigzagAmplitude: int | float
    zigzagMinSpan: int | float
    zigzagMaxSpan: int | float
    zigzagZ: int | float
    expandOnClick: bool

class YAxisBreakAreaItemStyle(TypedDict, total=False):
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

class YAxisBreakLabelLayout(TypedDict, total=False):
    moveOverlap: bool | str

class YAxisBreaksItem(TypedDict, total=False):
    start: str | int | float
    end: str | int | float
    gap: str | int | float
    isExpanded: bool

class YAxisDataItem(TypedDict, total=False):
    value: str
    textStyle: YAxisDataItemTextStyle

class YAxisDataItemTextStyle(TypedDict, total=False):
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
    rich: YAxisDataItemTextStyleRich
    richInheritPlainLabel: bool

class YAxisDataItemTextStyleRichStyle(TypedDict, total=False):
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

class YAxisMinorSplitLine(TypedDict, total=False):
    show: bool
    lineStyle: YAxisMinorSplitLineLineStyle

class YAxisMinorSplitLineLineStyle(TypedDict, total=False):
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

class YAxisMinorTick(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: YAxisMinorTickLineStyle

class YAxisMinorTickLineStyle(TypedDict, total=False):
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

class YAxisNameTextStyle(TypedDict, total=False):
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
    rich: YAxisNameTextStyleRich
    richInheritPlainLabel: bool

class YAxisNameTextStyleRichStyle(TypedDict, total=False):
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

class YAxisNameTruncate(TypedDict, total=False):
    maxWidth: int | float
    ellipsis: str

class YAxisSplitArea(TypedDict, total=False):
    interval: Callable[..., Any] | int | float
    show: bool
    areaStyle: YAxisSplitAreaAreaStyle

class YAxisSplitAreaAreaStyle(TypedDict, total=False):
    color: Any
    shadowBlur: int | float
    shadowColor: str | list[str]
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class YAxisSplitLine(TypedDict, total=False):
    show: bool
    showMinLine: bool
    showMaxLine: bool
    interval: Callable[..., Any] | int | float
    lineStyle: YAxisSplitLineLineStyle

class YAxisSplitLineLineStyle(TypedDict, total=False):
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

class YAxisTooltip(TypedDict, total=False):
    show: bool
    position: str
    formatter: Callable[..., Any] | str
    backgroundColor: str | list[str]
    borderColor: str | list[str]
    borderWidth: int | float
    padding: int | float
    textStyle: YAxisTooltipTextStyle
    extraCssText: str

class YAxisTooltipTextStyle(TypedDict, total=False):
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

class ZAxis3D(TypedDict, total=False):
    show: bool
    name: str
    grid3DIndex: int | float
    nameTextStyle: ZAxis3DNameTextStyle
    nameGap: int | float
    type: str
    min: str | int | float
    max: str | int | float
    scale: bool
    splitNumber: int | float
    minInterval: int | float
    interval: int | float
    logBase: int | float
    data: list[ZAxis3DDataItem]
    axisLine: ZAxis3DAxisLine
    axisLabel: ZAxis3DAxisLabel
    axisTick: ZAxis3DAxisTick
    splitLine: ZAxis3DSplitLine
    splitArea: ZAxis3DSplitArea
    axisPointer: ZAxis3DAxisPointer

class ZAxis3DAxisLabel(TypedDict, total=False):
    show: bool
    margin: int | float
    interval: Callable[..., Any] | int | float
    formatter: Callable[..., Any] | str
    textStyle: ZAxis3DAxisLabelTextStyle

class ZAxis3DAxisLabelTextStyle(TypedDict, total=False):
    color: Callable[..., Any] | str | list[str]
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class ZAxis3DAxisLine(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    lineStyle: ZAxis3DAxisLineLineStyle

class ZAxis3DAxisLineLineStyle(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class ZAxis3DAxisPointer(TypedDict, total=False):
    show: bool
    lineStyle: ZAxis3DAxisPointerLineStyle
    label: ZAxis3DAxisPointerLabel

class ZAxis3DAxisPointerLabel(TypedDict, total=False):
    show: bool
    formatter: Callable[..., Any]
    margin: int | float
    textStyle: ZAxis3DAxisPointerLabelTextStyle

class ZAxis3DAxisPointerLabelTextStyle(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class ZAxis3DAxisPointerLineStyle(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class ZAxis3DAxisTick(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    length: int | float
    lineStyle: ZAxis3DAxisTickLineStyle

class ZAxis3DAxisTickLineStyle(TypedDict, total=False):
    color: str | list[str]
    opacity: int | float
    width: int | float

class ZAxis3DDataItem(TypedDict, total=False):
    value: str
    textStyle: ZAxis3DDataItemTextStyle

class ZAxis3DDataItemTextStyle(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class ZAxis3DNameTextStyle(TypedDict, total=False):
    color: str | list[str]
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class ZAxis3DSplitArea(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    areaStyle: ZAxis3DSplitAreaAreaStyle

class ZAxis3DSplitAreaAreaStyle(TypedDict, total=False):
    color: Any

class ZAxis3DSplitLine(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    lineStyle: ZAxis3DSplitLineLineStyle

class ZAxis3DSplitLineLineStyle(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

AngleAxisAxisLabelRich = dict[str, AngleAxisAxisLabelRichStyle]
AngleAxisDataItemTextStyleRich = dict[str, AngleAxisDataItemTextStyleRichStyle]
CalendarDayLabelRich = dict[str, CalendarDayLabelRichStyle]
CalendarMonthLabelRich = dict[str, CalendarMonthLabelRichStyle]
CalendarYearLabelRich = dict[str, CalendarYearLabelRichStyle]
GeoBlurLabelRich = dict[str, GeoBlurLabelRichStyle]
GeoEmphasisLabelRich = dict[str, GeoEmphasisLabelRichStyle]
GeoLabelRich = dict[str, GeoLabelRichStyle]
GeoRegionsItemBlurLabelRich = dict[str, GeoRegionsItemBlurLabelRichStyle]
GeoRegionsItemEmphasisLabelRich = dict[str, GeoRegionsItemEmphasisLabelRichStyle]
GeoRegionsItemLabelRich = dict[str, GeoRegionsItemLabelRichStyle]
GeoRegionsItemSelectLabelRich = dict[str, GeoRegionsItemSelectLabelRichStyle]
GeoSelectLabelRich = dict[str, GeoSelectLabelRichStyle]
LegendEmphasisSelectorLabelRich = dict[str, LegendEmphasisSelectorLabelRichStyle]
LegendSelectorLabelRich = dict[str, LegendSelectorLabelRichStyle]
LegendTextStyleRich = dict[str, LegendTextStyleRichStyle]
MatrixBodyLabelRich = dict[str, MatrixBodyLabelRichStyle]
MatrixCornerLabelRich = dict[str, MatrixCornerLabelRichStyle]
MatrixXLabelRich = dict[str, MatrixXLabelRichStyle]
MatrixYLabelRich = dict[str, MatrixYLabelRichStyle]
ParallelAxisAxisLabelRich = dict[str, ParallelAxisAxisLabelRichStyle]
ParallelAxisDataItemTextStyleRich = dict[str, ParallelAxisDataItemTextStyleRichStyle]
ParallelAxisNameTextStyleRich = dict[str, ParallelAxisNameTextStyleRichStyle]
ParallelParallelAxisDefaultAxisLabelRich = dict[str, ParallelParallelAxisDefaultAxisLabelRichStyle]
ParallelParallelAxisDefaultDataItemTextStyleRich = dict[str, ParallelParallelAxisDefaultDataItemTextStyleRichStyle]
ParallelParallelAxisDefaultNameTextStyleRich = dict[str, ParallelParallelAxisDefaultNameTextStyleRichStyle]
RadarAxisLabelRich = dict[str, RadarAxisLabelRichStyle]
RadarAxisNameRich = dict[str, RadarAxisNameRichStyle]
RadiusAxisAxisLabelRich = dict[str, RadiusAxisAxisLabelRichStyle]
RadiusAxisDataItemTextStyleRich = dict[str, RadiusAxisDataItemTextStyleRichStyle]
RadiusAxisNameTextStyleRich = dict[str, RadiusAxisNameTextStyleRichStyle]
SingleAxisAxisLabelRich = dict[str, SingleAxisAxisLabelRichStyle]
SingleAxisDataItemTextStyleRich = dict[str, SingleAxisDataItemTextStyleRichStyle]
SingleAxisNameTextStyleRich = dict[str, SingleAxisNameTextStyleRichStyle]
TimelineEmphasisLabelRich = dict[str, TimelineEmphasisLabelRichStyle]
TimelineLabelRich = dict[str, TimelineLabelRichStyle]
TimelineProgressLabelRich = dict[str, TimelineProgressLabelRichStyle]
TitleSubtextStyleRich = dict[str, TitleSubtextStyleRichStyle]
TitleTextStyleRich = dict[str, TitleTextStyleRichStyle]
XAxisAxisLabelRich = dict[str, XAxisAxisLabelRichStyle]
XAxisDataItemTextStyleRich = dict[str, XAxisDataItemTextStyleRichStyle]
XAxisNameTextStyleRich = dict[str, XAxisNameTextStyleRichStyle]
YAxisAxisLabelRich = dict[str, YAxisAxisLabelRichStyle]
YAxisDataItemTextStyleRich = dict[str, YAxisDataItemTextStyleRichStyle]
YAxisNameTextStyleRich = dict[str, YAxisNameTextStyleRichStyle]

class Option(TypedDict, total=False):
    angleAxis: AngleAxis
    animation: dict[str, Any]
    animationDelay: dict[str, Any]
    animationDelayUpdate: dict[str, Any]
    animationDuration: dict[str, Any]
    animationDurationUpdate: dict[str, Any]
    animationEasing: dict[str, Any]
    animationEasingUpdate: dict[str, Any]
    animationThreshold: dict[str, Any]
    aria: Aria
    axisPointer: AxisPointer
    backgroundColor: dict[str, Any]
    blendMode: dict[str, Any]
    brush: Brush
    calendar: Calendar
    color: dict[str, Any]
    darkMode: dict[str, Any]
    dataZoom: dict[str, Any]
    dataset: Dataset
    geo3D: Geo3D
    geo: Geo
    globe: Globe
    graphic: Graphic
    grid3D: Grid3D
    grid: Grid
    hoverLayerThreshold: dict[str, Any]
    legend: Legend
    mapbox3D: Mapbox3D
    matrix: Matrix
    media: dict[str, Any]
    options: dict[str, Any]
    parallel: Parallel
    parallelAxis: ParallelAxis
    polar: Polar
    radar: Radar
    radiusAxis: RadiusAxis
    richInheritPlainLabel: dict[str, Any]
    series: dict[str, Any]
    singleAxis: SingleAxis
    stateAnimation: StateAnimation
    textStyle: TextStyle
    thumbnail: Thumbnail
    timeline: Timeline
    title: Title
    toolbox: Toolbox
    tooltip: Tooltip
    useUTC: dict[str, Any]
    visualMap: dict[str, Any]
    xAxis3D: XAxis3D
    xAxis: XAxis
    yAxis3D: YAxis3D
    yAxis: YAxis
    zAxis3D: ZAxis3D