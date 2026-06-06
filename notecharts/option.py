from __future__ import annotations
from typing import Any, Callable
from typing_extensions import TypedDict

class Title_textstyle_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Title_textstyle_richOpts = dict[str, Title_textstyle_rich_styleOpts]

class Title_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Title_textstyle_richOpts
    richInheritPlainLabel: bool

class Title_subtextstyle_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Title_subtextstyle_richOpts = dict[str, Title_subtextstyle_rich_styleOpts]

class Title_subtextstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Title_subtextstyle_richOpts
    richInheritPlainLabel: bool

class TitleOpts(TypedDict, total=False):
    id: str
    show: bool
    text: str
    link: str
    target: str
    textStyle: Title_textstyleOpts
    subtext: str
    sublink: str
    subtarget: str
    subtextStyle: Title_subtextstyleOpts
    textAlign: str
    textVerticalAlign: str
    triggerEvent: bool
    padding: int | float
    itemGap: int | float
    zlevel: int | float
    z: int | float
    left: int | float | str
    top: int | float | str
    right: int | float | str
    bottom: int | float | str
    coordinateSystem: str
    coordinateSystemUsage: str
    coord: str | int | float
    calendarIndex: int | float
    calendarId: int | float
    matrixIndex: int | float
    matrixId: int | float
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    borderRadius: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class Legend_itemstyle_decalOpts(TypedDict, total=False):
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

class Legend_itemstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    decal: Legend_itemstyle_decalOpts

class Legend_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    inactiveColor: str
    inactiveWidth: int | float

class Legend_textstyle_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Legend_textstyle_richOpts = dict[str, Legend_textstyle_rich_styleOpts]

class Legend_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Legend_textstyle_richOpts
    richInheritPlainLabel: bool

class Legend_data_item_itemstyle_decalOpts(TypedDict, total=False):
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

class Legend_data_item_itemstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    decal: Legend_data_item_itemstyle_decalOpts

class Legend_data_item_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    inactiveColor: str
    inactiveWidth: int | float

class Legend_data_item_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str

class Legend_data_itemOpts(TypedDict, total=False):
    name: str
    icon: str
    itemStyle: Legend_data_item_itemstyleOpts
    lineStyle: Legend_data_item_linestyleOpts
    inactiveColor: str
    inactiveBorderColor: str
    inactiveBorderWidth: str | int | float
    symbolRotate: str | int | float
    textStyle: Legend_data_item_textstyleOpts

class Legend_pageiconsOpts(TypedDict, total=False):
    horizontal: Any
    vertical: Any

class Legend_pagetextstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str

class Legend_emphasis_selectorlabel_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Legend_emphasis_selectorlabel_richOpts = dict[str, Legend_emphasis_selectorlabel_rich_styleOpts]

class Legend_emphasis_selectorlabelOpts(TypedDict, total=False):
    show: bool
    distance: int | float
    rotate: int | float
    offset: Any
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Legend_emphasis_selectorlabel_richOpts
    richInheritPlainLabel: bool

class Legend_emphasisOpts(TypedDict, total=False):
    selectorLabel: Legend_emphasis_selectorlabelOpts

class Legend_selectorlabel_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Legend_selectorlabel_richOpts = dict[str, Legend_selectorlabel_rich_styleOpts]

class Legend_selectorlabelOpts(TypedDict, total=False):
    show: bool
    distance: int | float
    rotate: int | float
    offset: Any
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Legend_selectorlabel_richOpts
    richInheritPlainLabel: bool

class LegendOpts(TypedDict, total=False):
    type: str
    id: str
    show: bool
    zlevel: int | float
    z: int | float
    left: int | float | str
    top: int | float | str
    right: int | float | str
    bottom: int | float | str
    width: int | float | str
    height: int | float | str
    coordinateSystem: str
    coordinateSystemUsage: str
    coord: str | int | float
    calendarIndex: int | float
    calendarId: int | float
    matrixIndex: int | float
    matrixId: int | float
    orient: str
    align: str
    padding: int | float
    itemGap: int | float
    itemWidth: int | float
    itemHeight: int | float
    itemStyle: Legend_itemstyleOpts
    lineStyle: Legend_linestyleOpts
    symbolRotate: str | int | float
    formatter: Callable[..., Any] | str
    selectedMode: str | bool
    inactiveColor: str
    inactiveBorderColor: str
    inactiveBorderWidth: str | int | float
    selected: dict[str, Any]
    textStyle: Legend_textstyleOpts
    tooltip: dict[str, Any]
    icon: str
    data: list[Legend_data_itemOpts]
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    borderRadius: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    scrollDataIndex: int | float
    pageButtonItemGap: int | float
    pageButtonGap: int | float
    pageButtonPosition: str
    pageFormatter: Callable[..., Any] | str
    pageIcons: Legend_pageiconsOpts
    pageIconColor: str
    pageIconInactiveColor: str
    pageIconSize: int | float
    pageTextStyle: Legend_pagetextstyleOpts
    animation: bool
    animationDurationUpdate: int | float
    emphasis: Legend_emphasisOpts
    selector: bool
    selectorLabel: Legend_selectorlabelOpts
    selectorPosition: str
    selectorItemGap: int | float
    selectorButtonGap: int | float
    triggerEvent: bool

class Grid_outerboundsOpts(TypedDict, total=False):
    left: int | float | str
    top: int | float | str
    right: int | float | str
    bottom: int | float | str
    width: int | float | str
    height: int | float | str

class Grid_tooltip_axispointer_labelOpts(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: Callable[..., Any] | str
    margin: int | float
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    padding: str
    backgroundColor: str
    borderColor: str
    borderWidth: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class Grid_tooltip_axispointer_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Grid_tooltip_axispointer_shadowstyleOpts(TypedDict, total=False):
    color: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Grid_tooltip_axispointer_crossstyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Grid_tooltip_axispointerOpts(TypedDict, total=False):
    type: str
    axis: str
    snap: bool
    z: int | float
    label: Grid_tooltip_axispointer_labelOpts
    lineStyle: Grid_tooltip_axispointer_linestyleOpts
    shadowStyle: Grid_tooltip_axispointer_shadowstyleOpts
    crossStyle: Grid_tooltip_axispointer_crossstyleOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: str
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: str
    animationDelayUpdate: Callable[..., Any] | int | float

class Grid_tooltip_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str

class Grid_tooltipOpts(TypedDict, total=False):
    show: bool
    trigger: str
    axisPointer: Grid_tooltip_axispointerOpts
    position: str
    formatter: Callable[..., Any] | str
    valueFormatter: str
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    padding: int | float
    textStyle: Grid_tooltip_textstyleOpts
    extraCssText: str

class GridOpts(TypedDict, total=False):
    id: str
    show: bool
    zlevel: int | float
    z: int | float
    left: int | float | str
    top: int | float | str
    right: int | float | str
    bottom: int | float | str
    width: int | float | str
    height: int | float | str
    containLabel: bool
    outerBoundsMode: str
    outerBounds: Grid_outerboundsOpts
    outerBoundsContain: bool
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    tooltip: Grid_tooltipOpts
    coordinateSystem: str
    coordinateSystemUsage: str
    coord: str | int | float
    calendarIndex: int | float
    calendarId: int | float
    matrixIndex: int | float
    matrixId: int | float

class Xaxis_nametextstyle_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Xaxis_nametextstyle_richOpts = dict[str, Xaxis_nametextstyle_rich_styleOpts]

class Xaxis_nametextstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Xaxis_nametextstyle_richOpts
    richInheritPlainLabel: bool

class Xaxis_nametruncateOpts(TypedDict, total=False):
    maxWidth: int | float
    ellipsis: str

class Xaxis_breaks_itemOpts(TypedDict, total=False):
    start: int | float | str
    end: int | float | str
    gap: str | int | float
    isExpanded: bool

class Xaxis_breakarea_itemstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Xaxis_breakareaOpts(TypedDict, total=False):
    show: bool
    itemStyle: Xaxis_breakarea_itemstyleOpts
    zigzagAmplitude: int | float
    zigzagMinSpan: int | float
    zigzagMaxSpan: int | float
    zigzagZ: int | float
    expandOnClick: bool

class Xaxis_breaklabellayoutOpts(TypedDict, total=False):
    moveOverlap: str | bool

class Xaxis_axisline_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Xaxis_axislineOpts(TypedDict, total=False):
    show: bool
    onZero: str | bool
    onZeroAxisIndex: int | float
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: Xaxis_axisline_linestyleOpts

class Xaxis_axistick_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Xaxis_axistickOpts(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    length: int | float
    lineStyle: Xaxis_axistick_linestyleOpts
    customValues: Any

class Xaxis_minortick_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Xaxis_minortickOpts(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: Xaxis_minortick_linestyleOpts

class Xaxis_axislabel_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Xaxis_axislabel_richOpts = dict[str, Xaxis_axislabel_rich_styleOpts]

class Xaxis_axislabelOpts(TypedDict, total=False):
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
    color: Callable[..., Any] | str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Xaxis_axislabel_richOpts
    richInheritPlainLabel: bool

class Xaxis_splitline_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Xaxis_splitlineOpts(TypedDict, total=False):
    show: bool
    showMinLine: bool
    showMaxLine: bool
    interval: Callable[..., Any] | int | float
    lineStyle: Xaxis_splitline_linestyleOpts

class Xaxis_minorsplitline_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Xaxis_minorsplitlineOpts(TypedDict, total=False):
    show: bool
    lineStyle: Xaxis_minorsplitline_linestyleOpts

class Xaxis_splitarea_areastyleOpts(TypedDict, total=False):
    color: Any
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Xaxis_splitareaOpts(TypedDict, total=False):
    interval: Callable[..., Any] | int | float
    show: bool
    areaStyle: Xaxis_splitarea_areastyleOpts

class Xaxis_data_item_textstyle_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Xaxis_data_item_textstyle_richOpts = dict[str, Xaxis_data_item_textstyle_rich_styleOpts]

class Xaxis_data_item_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Xaxis_data_item_textstyle_richOpts
    richInheritPlainLabel: bool

class Xaxis_data_itemOpts(TypedDict, total=False):
    value: str
    textStyle: Xaxis_data_item_textstyleOpts

class Xaxis_axispointer_labelOpts(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: Callable[..., Any] | str
    margin: int | float
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    padding: str
    backgroundColor: str
    borderColor: str
    borderWidth: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class Xaxis_axispointer_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Xaxis_axispointer_shadowstyleOpts(TypedDict, total=False):
    color: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Xaxis_axispointer_handleOpts(TypedDict, total=False):
    show: bool
    icon: Any
    size: int | float
    margin: int | float
    color: str
    throttle: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class Xaxis_axispointerOpts(TypedDict, total=False):
    show: bool
    type: str
    snap: bool
    z: int | float
    label: Xaxis_axispointer_labelOpts
    lineStyle: Xaxis_axispointer_linestyleOpts
    shadowStyle: Xaxis_axispointer_shadowstyleOpts
    triggerEmphasis: bool
    triggerTooltip: bool
    value: int | float
    status: bool
    handle: Xaxis_axispointer_handleOpts

class Xaxis_tooltip_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str

class Xaxis_tooltipOpts(TypedDict, total=False):
    show: bool
    position: str
    formatter: Callable[..., Any] | str
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    padding: int | float
    textStyle: Xaxis_tooltip_textstyleOpts
    extraCssText: str

class XaxisOpts(TypedDict, total=False):
    id: str
    show: bool
    gridIndex: int | float
    alignTicks: bool
    position: str
    offset: int | float
    type: str
    name: str
    nameLocation: str
    nameTextStyle: Xaxis_nametextstyleOpts
    nameGap: int | float
    nameRotate: int | float
    nameTruncate: Xaxis_nametruncateOpts
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
    breaks: list[Xaxis_breaks_itemOpts]
    breakArea: Xaxis_breakareaOpts
    breakLabelLayout: Xaxis_breaklabellayoutOpts
    axisLine: Xaxis_axislineOpts
    axisTick: Xaxis_axistickOpts
    minorTick: Xaxis_minortickOpts
    axisLabel: Xaxis_axislabelOpts
    splitLine: Xaxis_splitlineOpts
    minorSplitLine: Xaxis_minorsplitlineOpts
    splitArea: Xaxis_splitareaOpts
    data: list[Xaxis_data_itemOpts]
    axisPointer: Xaxis_axispointerOpts
    tooltip: Xaxis_tooltipOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: str
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: str
    animationDelayUpdate: Callable[..., Any] | int | float
    zlevel: int | float
    z: int | float

class Yaxis_nametextstyle_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Yaxis_nametextstyle_richOpts = dict[str, Yaxis_nametextstyle_rich_styleOpts]

class Yaxis_nametextstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Yaxis_nametextstyle_richOpts
    richInheritPlainLabel: bool

class Yaxis_nametruncateOpts(TypedDict, total=False):
    maxWidth: int | float
    ellipsis: str

class Yaxis_breaks_itemOpts(TypedDict, total=False):
    start: int | float | str
    end: int | float | str
    gap: str | int | float
    isExpanded: bool

class Yaxis_breakarea_itemstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Yaxis_breakareaOpts(TypedDict, total=False):
    show: bool
    itemStyle: Yaxis_breakarea_itemstyleOpts
    zigzagAmplitude: int | float
    zigzagMinSpan: int | float
    zigzagMaxSpan: int | float
    zigzagZ: int | float
    expandOnClick: bool

class Yaxis_breaklabellayoutOpts(TypedDict, total=False):
    moveOverlap: str | bool

class Yaxis_axisline_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Yaxis_axislineOpts(TypedDict, total=False):
    show: bool
    onZero: str | bool
    onZeroAxisIndex: int | float
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: Yaxis_axisline_linestyleOpts

class Yaxis_axistick_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Yaxis_axistickOpts(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    length: int | float
    lineStyle: Yaxis_axistick_linestyleOpts
    customValues: Any

class Yaxis_minortick_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Yaxis_minortickOpts(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: Yaxis_minortick_linestyleOpts

class Yaxis_axislabel_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Yaxis_axislabel_richOpts = dict[str, Yaxis_axislabel_rich_styleOpts]

class Yaxis_axislabelOpts(TypedDict, total=False):
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
    color: Callable[..., Any] | str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Yaxis_axislabel_richOpts
    richInheritPlainLabel: bool

class Yaxis_splitline_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Yaxis_splitlineOpts(TypedDict, total=False):
    show: bool
    showMinLine: bool
    showMaxLine: bool
    interval: Callable[..., Any] | int | float
    lineStyle: Yaxis_splitline_linestyleOpts

class Yaxis_minorsplitline_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Yaxis_minorsplitlineOpts(TypedDict, total=False):
    show: bool
    lineStyle: Yaxis_minorsplitline_linestyleOpts

class Yaxis_splitarea_areastyleOpts(TypedDict, total=False):
    color: Any
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Yaxis_splitareaOpts(TypedDict, total=False):
    interval: Callable[..., Any] | int | float
    show: bool
    areaStyle: Yaxis_splitarea_areastyleOpts

class Yaxis_data_item_textstyle_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Yaxis_data_item_textstyle_richOpts = dict[str, Yaxis_data_item_textstyle_rich_styleOpts]

class Yaxis_data_item_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Yaxis_data_item_textstyle_richOpts
    richInheritPlainLabel: bool

class Yaxis_data_itemOpts(TypedDict, total=False):
    value: str
    textStyle: Yaxis_data_item_textstyleOpts

class Yaxis_axispointer_labelOpts(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: Callable[..., Any] | str
    margin: int | float
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    padding: str
    backgroundColor: str
    borderColor: str
    borderWidth: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class Yaxis_axispointer_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Yaxis_axispointer_shadowstyleOpts(TypedDict, total=False):
    color: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Yaxis_axispointer_handleOpts(TypedDict, total=False):
    show: bool
    icon: Any
    size: int | float
    margin: int | float
    color: str
    throttle: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class Yaxis_axispointerOpts(TypedDict, total=False):
    show: bool
    type: str
    snap: bool
    z: int | float
    label: Yaxis_axispointer_labelOpts
    lineStyle: Yaxis_axispointer_linestyleOpts
    shadowStyle: Yaxis_axispointer_shadowstyleOpts
    triggerEmphasis: bool
    triggerTooltip: bool
    value: int | float
    status: bool
    handle: Yaxis_axispointer_handleOpts

class Yaxis_tooltip_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str

class Yaxis_tooltipOpts(TypedDict, total=False):
    show: bool
    position: str
    formatter: Callable[..., Any] | str
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    padding: int | float
    textStyle: Yaxis_tooltip_textstyleOpts
    extraCssText: str

class YaxisOpts(TypedDict, total=False):
    id: str
    show: bool
    gridIndex: int | float
    alignTicks: bool
    position: str
    offset: int | float
    type: str
    name: str
    nameLocation: str
    nameTextStyle: Yaxis_nametextstyleOpts
    nameGap: int | float
    nameRotate: int | float
    nameTruncate: Yaxis_nametruncateOpts
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
    breaks: list[Yaxis_breaks_itemOpts]
    breakArea: Yaxis_breakareaOpts
    breakLabelLayout: Yaxis_breaklabellayoutOpts
    axisLine: Yaxis_axislineOpts
    axisTick: Yaxis_axistickOpts
    minorTick: Yaxis_minortickOpts
    axisLabel: Yaxis_axislabelOpts
    splitLine: Yaxis_splitlineOpts
    minorSplitLine: Yaxis_minorsplitlineOpts
    splitArea: Yaxis_splitareaOpts
    data: list[Yaxis_data_itemOpts]
    axisPointer: Yaxis_axispointerOpts
    tooltip: Yaxis_tooltipOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: str
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: str
    animationDelayUpdate: Callable[..., Any] | int | float
    zlevel: int | float
    z: int | float

class Polar_tooltip_axispointer_labelOpts(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: Callable[..., Any] | str
    margin: int | float
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    padding: str
    backgroundColor: str
    borderColor: str
    borderWidth: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class Polar_tooltip_axispointer_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Polar_tooltip_axispointer_shadowstyleOpts(TypedDict, total=False):
    color: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Polar_tooltip_axispointer_crossstyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Polar_tooltip_axispointerOpts(TypedDict, total=False):
    type: str
    axis: str
    snap: bool
    z: int | float
    label: Polar_tooltip_axispointer_labelOpts
    lineStyle: Polar_tooltip_axispointer_linestyleOpts
    shadowStyle: Polar_tooltip_axispointer_shadowstyleOpts
    crossStyle: Polar_tooltip_axispointer_crossstyleOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: str
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: str
    animationDelayUpdate: Callable[..., Any] | int | float

class Polar_tooltip_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str

class Polar_tooltipOpts(TypedDict, total=False):
    show: bool
    trigger: str
    axisPointer: Polar_tooltip_axispointerOpts
    position: str
    formatter: Callable[..., Any] | str
    valueFormatter: str
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    padding: int | float
    textStyle: Polar_tooltip_textstyleOpts
    extraCssText: str

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
    tooltip: Polar_tooltipOpts

class Radiusaxis_nametextstyle_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Radiusaxis_nametextstyle_richOpts = dict[str, Radiusaxis_nametextstyle_rich_styleOpts]

class Radiusaxis_nametextstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Radiusaxis_nametextstyle_richOpts
    richInheritPlainLabel: bool

class Radiusaxis_nametruncateOpts(TypedDict, total=False):
    maxWidth: int | float
    ellipsis: str

class Radiusaxis_axisline_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Radiusaxis_axislineOpts(TypedDict, total=False):
    show: bool
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: Radiusaxis_axisline_linestyleOpts

class Radiusaxis_axistick_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Radiusaxis_axistickOpts(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    length: int | float
    lineStyle: Radiusaxis_axistick_linestyleOpts
    customValues: Any

class Radiusaxis_minortick_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Radiusaxis_minortickOpts(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: Radiusaxis_minortick_linestyleOpts

class Radiusaxis_axislabel_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Radiusaxis_axislabel_richOpts = dict[str, Radiusaxis_axislabel_rich_styleOpts]

class Radiusaxis_axislabelOpts(TypedDict, total=False):
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
    color: Callable[..., Any] | str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Radiusaxis_axislabel_richOpts
    richInheritPlainLabel: bool

class Radiusaxis_splitline_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Radiusaxis_splitlineOpts(TypedDict, total=False):
    show: bool
    showMinLine: bool
    showMaxLine: bool
    interval: Callable[..., Any] | int | float
    lineStyle: Radiusaxis_splitline_linestyleOpts

class Radiusaxis_minorsplitline_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Radiusaxis_minorsplitlineOpts(TypedDict, total=False):
    show: bool
    lineStyle: Radiusaxis_minorsplitline_linestyleOpts

class Radiusaxis_splitarea_areastyleOpts(TypedDict, total=False):
    color: Any
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Radiusaxis_splitareaOpts(TypedDict, total=False):
    interval: Callable[..., Any] | int | float
    show: bool
    areaStyle: Radiusaxis_splitarea_areastyleOpts

class Radiusaxis_data_item_textstyle_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Radiusaxis_data_item_textstyle_richOpts = dict[str, Radiusaxis_data_item_textstyle_rich_styleOpts]

class Radiusaxis_data_item_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Radiusaxis_data_item_textstyle_richOpts
    richInheritPlainLabel: bool

class Radiusaxis_data_itemOpts(TypedDict, total=False):
    value: str
    textStyle: Radiusaxis_data_item_textstyleOpts

class Radiusaxis_axispointer_labelOpts(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: Callable[..., Any] | str
    margin: int | float
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    padding: str
    backgroundColor: str
    borderColor: str
    borderWidth: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class Radiusaxis_axispointer_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Radiusaxis_axispointer_shadowstyleOpts(TypedDict, total=False):
    color: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Radiusaxis_axispointer_handleOpts(TypedDict, total=False):
    show: bool
    icon: Any
    size: int | float
    margin: int | float
    color: str
    throttle: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class Radiusaxis_axispointerOpts(TypedDict, total=False):
    show: bool
    type: str
    snap: bool
    z: int | float
    label: Radiusaxis_axispointer_labelOpts
    lineStyle: Radiusaxis_axispointer_linestyleOpts
    shadowStyle: Radiusaxis_axispointer_shadowstyleOpts
    triggerEmphasis: bool
    triggerTooltip: bool
    value: int | float
    status: bool
    handle: Radiusaxis_axispointer_handleOpts

class Radiusaxis_tooltip_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str

class Radiusaxis_tooltipOpts(TypedDict, total=False):
    show: bool
    position: str
    formatter: Callable[..., Any] | str
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    padding: int | float
    textStyle: Radiusaxis_tooltip_textstyleOpts
    extraCssText: str

class RadiusaxisOpts(TypedDict, total=False):
    id: str
    polarIndex: int | float
    type: str
    name: str
    nameLocation: str
    nameTextStyle: Radiusaxis_nametextstyleOpts
    nameGap: int | float
    nameRotate: int | float
    nameTruncate: Radiusaxis_nametruncateOpts
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
    axisLine: Radiusaxis_axislineOpts
    axisTick: Radiusaxis_axistickOpts
    minorTick: Radiusaxis_minortickOpts
    axisLabel: Radiusaxis_axislabelOpts
    splitLine: Radiusaxis_splitlineOpts
    minorSplitLine: Radiusaxis_minorsplitlineOpts
    splitArea: Radiusaxis_splitareaOpts
    data: list[Radiusaxis_data_itemOpts]
    axisPointer: Radiusaxis_axispointerOpts
    tooltip: Radiusaxis_tooltipOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: str
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: str
    animationDelayUpdate: Callable[..., Any] | int | float
    zlevel: int | float
    z: int | float

class Angleaxis_axisline_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Angleaxis_axislineOpts(TypedDict, total=False):
    show: bool
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: Angleaxis_axisline_linestyleOpts

class Angleaxis_axistick_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Angleaxis_axistickOpts(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    length: int | float
    lineStyle: Angleaxis_axistick_linestyleOpts
    customValues: Any

class Angleaxis_minortick_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Angleaxis_minortickOpts(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: Angleaxis_minortick_linestyleOpts

class Angleaxis_axislabel_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Angleaxis_axislabel_richOpts = dict[str, Angleaxis_axislabel_rich_styleOpts]

class Angleaxis_axislabelOpts(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    margin: int | float
    formatter: Callable[..., Any] | str
    showMinLabel: bool
    showMaxLabel: bool
    hideOverlap: bool
    customValues: Any
    color: Callable[..., Any] | str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Angleaxis_axislabel_richOpts
    richInheritPlainLabel: bool

class Angleaxis_splitline_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Angleaxis_splitlineOpts(TypedDict, total=False):
    show: bool
    showMinLine: bool
    showMaxLine: bool
    interval: Callable[..., Any] | int | float
    lineStyle: Angleaxis_splitline_linestyleOpts

class Angleaxis_minorsplitline_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Angleaxis_minorsplitlineOpts(TypedDict, total=False):
    show: bool
    lineStyle: Angleaxis_minorsplitline_linestyleOpts

class Angleaxis_splitarea_areastyleOpts(TypedDict, total=False):
    color: Any
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Angleaxis_splitareaOpts(TypedDict, total=False):
    interval: Callable[..., Any] | int | float
    show: bool
    areaStyle: Angleaxis_splitarea_areastyleOpts

class Angleaxis_data_item_textstyle_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Angleaxis_data_item_textstyle_richOpts = dict[str, Angleaxis_data_item_textstyle_rich_styleOpts]

class Angleaxis_data_item_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Angleaxis_data_item_textstyle_richOpts
    richInheritPlainLabel: bool

class Angleaxis_data_itemOpts(TypedDict, total=False):
    value: str
    textStyle: Angleaxis_data_item_textstyleOpts

class Angleaxis_axispointer_labelOpts(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: Callable[..., Any] | str
    margin: int | float
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    padding: str
    backgroundColor: str
    borderColor: str
    borderWidth: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class Angleaxis_axispointer_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Angleaxis_axispointer_shadowstyleOpts(TypedDict, total=False):
    color: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Angleaxis_axispointer_handleOpts(TypedDict, total=False):
    show: bool
    icon: Any
    size: int | float
    margin: int | float
    color: str
    throttle: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class Angleaxis_axispointerOpts(TypedDict, total=False):
    show: bool
    type: str
    snap: bool
    z: int | float
    label: Angleaxis_axispointer_labelOpts
    lineStyle: Angleaxis_axispointer_linestyleOpts
    shadowStyle: Angleaxis_axispointer_shadowstyleOpts
    triggerEmphasis: bool
    triggerTooltip: bool
    value: int | float
    status: bool
    handle: Angleaxis_axispointer_handleOpts

class Angleaxis_tooltip_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str

class Angleaxis_tooltipOpts(TypedDict, total=False):
    show: bool
    position: str
    formatter: Callable[..., Any] | str
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    padding: int | float
    textStyle: Angleaxis_tooltip_textstyleOpts
    extraCssText: str

class AngleaxisOpts(TypedDict, total=False):
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
    axisLine: Angleaxis_axislineOpts
    axisTick: Angleaxis_axistickOpts
    minorTick: Angleaxis_minortickOpts
    axisLabel: Angleaxis_axislabelOpts
    splitLine: Angleaxis_splitlineOpts
    minorSplitLine: Angleaxis_minorsplitlineOpts
    splitArea: Angleaxis_splitareaOpts
    data: list[Angleaxis_data_itemOpts]
    axisPointer: Angleaxis_axispointerOpts
    tooltip: Angleaxis_tooltipOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: str
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: str
    animationDelayUpdate: Callable[..., Any] | int | float
    zlevel: int | float
    z: int | float

class Radar_axisname_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Radar_axisname_richOpts = dict[str, Radar_axisname_rich_styleOpts]

class Radar_axisnameOpts(TypedDict, total=False):
    show: bool
    formatter: Callable[..., Any] | str
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Radar_axisname_richOpts
    richInheritPlainLabel: bool

class Radar_axisline_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Radar_axislineOpts(TypedDict, total=False):
    show: bool
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: Radar_axisline_linestyleOpts

class Radar_axistick_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Radar_axistickOpts(TypedDict, total=False):
    show: bool
    length: int | float
    lineStyle: Radar_axistick_linestyleOpts
    customValues: Any

class Radar_axislabel_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Radar_axislabel_richOpts = dict[str, Radar_axislabel_rich_styleOpts]

class Radar_axislabelOpts(TypedDict, total=False):
    show: bool
    rotate: int | float
    margin: int | float
    formatter: Callable[..., Any] | str
    showMinLabel: bool
    showMaxLabel: bool
    hideOverlap: bool
    customValues: Any
    color: Callable[..., Any] | str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Radar_axislabel_richOpts
    richInheritPlainLabel: bool

class Radar_splitline_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Radar_splitlineOpts(TypedDict, total=False):
    show: bool
    showMinLine: bool
    showMaxLine: bool
    lineStyle: Radar_splitline_linestyleOpts

class Radar_splitarea_areastyleOpts(TypedDict, total=False):
    color: Any
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Radar_splitareaOpts(TypedDict, total=False):
    show: bool
    areaStyle: Radar_splitarea_areastyleOpts

class Radar_indicator_itemOpts(TypedDict, total=False):
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
    axisName: Radar_axisnameOpts
    axisNameGap: int | float
    splitNumber: int | float
    shape: str
    scale: bool
    silent: bool
    triggerEvent: bool
    axisLine: Radar_axislineOpts
    axisTick: Radar_axistickOpts
    axisLabel: Radar_axislabelOpts
    splitLine: Radar_splitlineOpts
    splitArea: Radar_splitareaOpts
    indicator: list[Radar_indicator_itemOpts]

class Tooltip_axispointer_labelOpts(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: Callable[..., Any] | str
    margin: int | float
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    padding: str
    backgroundColor: str
    borderColor: str
    borderWidth: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class Tooltip_axispointer_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Tooltip_axispointer_shadowstyleOpts(TypedDict, total=False):
    color: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Tooltip_axispointer_crossstyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Tooltip_axispointerOpts(TypedDict, total=False):
    type: str
    axis: str
    snap: bool
    z: int | float
    label: Tooltip_axispointer_labelOpts
    lineStyle: Tooltip_axispointer_linestyleOpts
    shadowStyle: Tooltip_axispointer_shadowstyleOpts
    crossStyle: Tooltip_axispointer_crossstyleOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: str
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: str
    animationDelayUpdate: Callable[..., Any] | int | float

class Tooltip_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str

class TooltipOpts(TypedDict, total=False):
    show: bool
    trigger: str
    axisPointer: Tooltip_axispointerOpts
    showContent: bool
    alwaysShowContent: bool
    triggerOn: str
    showDelay: int | float
    hideDelay: int | float
    enterable: bool
    renderMode: str
    confine: bool
    appendToBody: bool
    appendTo: Callable[..., Any] | str
    className: str
    transitionDuration: int | float
    displayTransition: bool
    position: str
    formatter: Callable[..., Any] | str
    valueFormatter: str
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    padding: int | float
    textStyle: Tooltip_textstyleOpts
    extraCssText: str
    order: str

class Axispointer_labelOpts(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: Callable[..., Any] | str
    margin: int | float
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    padding: str
    backgroundColor: str
    borderColor: str
    borderWidth: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class Axispointer_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Axispointer_shadowstyleOpts(TypedDict, total=False):
    color: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Axispointer_handleOpts(TypedDict, total=False):
    show: bool
    icon: Any
    size: int | float
    margin: int | float
    color: str
    throttle: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class AxispointerOpts(TypedDict, total=False):
    id: str
    show: bool
    type: str
    snap: bool
    z: int | float
    label: Axispointer_labelOpts
    lineStyle: Axispointer_linestyleOpts
    shadowStyle: Axispointer_shadowstyleOpts
    triggerEmphasis: bool
    triggerTooltip: bool
    value: int | float
    status: bool
    handle: Axispointer_handleOpts
    link: Any
    triggerOn: str

class Toolbox_feature_saveasimage_iconstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Toolbox_feature_saveasimage_emphasis_iconstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    textPosition: str
    textFill: str
    textAlign: str
    textBackgroundColor: str
    textBorderRadius: int | float
    textPadding: int | float

class Toolbox_feature_saveasimage_emphasisOpts(TypedDict, total=False):
    iconStyle: Toolbox_feature_saveasimage_emphasis_iconstyleOpts

class Toolbox_feature_saveasimageOpts(TypedDict, total=False):
    type: str
    name: str
    backgroundColor: str
    connectedBackgroundColor: str
    excludeComponents: Any
    show: bool
    title: str
    icon: str
    iconStyle: Toolbox_feature_saveasimage_iconstyleOpts
    emphasis: Toolbox_feature_saveasimage_emphasisOpts
    pixelRatio: int | float

class Toolbox_feature_restore_iconstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Toolbox_feature_restore_emphasis_iconstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    textPosition: str
    textFill: str
    textAlign: str
    textBackgroundColor: str
    textBorderRadius: int | float
    textPadding: int | float

class Toolbox_feature_restore_emphasisOpts(TypedDict, total=False):
    iconStyle: Toolbox_feature_restore_emphasis_iconstyleOpts

class Toolbox_feature_restoreOpts(TypedDict, total=False):
    show: bool
    title: str
    icon: str
    iconStyle: Toolbox_feature_restore_iconstyleOpts
    emphasis: Toolbox_feature_restore_emphasisOpts

class Toolbox_feature_dataview_iconstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Toolbox_feature_dataview_emphasis_iconstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    textPosition: str
    textFill: str
    textAlign: str
    textBackgroundColor: str
    textBorderRadius: int | float
    textPadding: int | float

class Toolbox_feature_dataview_emphasisOpts(TypedDict, total=False):
    iconStyle: Toolbox_feature_dataview_emphasis_iconstyleOpts

class Toolbox_feature_dataviewOpts(TypedDict, total=False):
    show: bool
    title: str
    icon: str
    iconStyle: Toolbox_feature_dataview_iconstyleOpts
    emphasis: Toolbox_feature_dataview_emphasisOpts
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

class Toolbox_feature_datazoom_titleOpts(TypedDict, total=False):
    zoom: str
    back: str

class Toolbox_feature_datazoom_iconOpts(TypedDict, total=False):
    zoom: str
    back: str

class Toolbox_feature_datazoom_iconstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Toolbox_feature_datazoom_emphasis_iconstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    textPosition: str
    textFill: str
    textAlign: str
    textBackgroundColor: str
    textBorderRadius: int | float
    textPadding: int | float

class Toolbox_feature_datazoom_emphasisOpts(TypedDict, total=False):
    iconStyle: Toolbox_feature_datazoom_emphasis_iconstyleOpts

class Toolbox_feature_datazoom_brushstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Toolbox_feature_datazoomOpts(TypedDict, total=False):
    show: bool
    title: Toolbox_feature_datazoom_titleOpts
    icon: Toolbox_feature_datazoom_iconOpts
    iconStyle: Toolbox_feature_datazoom_iconstyleOpts
    emphasis: Toolbox_feature_datazoom_emphasisOpts
    filterMode: str
    xAxisIndex: int | float | bool
    yAxisIndex: int | float | bool
    brushStyle: Toolbox_feature_datazoom_brushstyleOpts

class Toolbox_feature_magictype_titleOpts(TypedDict, total=False):
    line: str
    bar: str
    stack: str
    tiled: str

class Toolbox_feature_magictype_iconOpts(TypedDict, total=False):
    line: str
    bar: str
    stack: str

class Toolbox_feature_magictype_iconstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Toolbox_feature_magictype_emphasis_iconstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    textPosition: str
    textFill: str
    textAlign: str
    textBackgroundColor: str
    textBorderRadius: int | float
    textPadding: int | float

class Toolbox_feature_magictype_emphasisOpts(TypedDict, total=False):
    iconStyle: Toolbox_feature_magictype_emphasis_iconstyleOpts

class Toolbox_feature_magictype_optionOpts(TypedDict, total=False):
    line: dict[str, Any]
    bar: dict[str, Any]
    stack: dict[str, Any]

class Toolbox_feature_magictype_seriesindexOpts(TypedDict, total=False):
    line: Any
    bar: Any

class Toolbox_feature_magictypeOpts(TypedDict, total=False):
    show: bool
    type: Any
    title: Toolbox_feature_magictype_titleOpts
    icon: Toolbox_feature_magictype_iconOpts
    iconStyle: Toolbox_feature_magictype_iconstyleOpts
    emphasis: Toolbox_feature_magictype_emphasisOpts
    option: Toolbox_feature_magictype_optionOpts
    seriesIndex: Toolbox_feature_magictype_seriesindexOpts

class Toolbox_feature_brush_iconOpts(TypedDict, total=False):
    rect: str
    polygon: str
    lineX: str
    lineY: str
    keep: str
    clear: str

class Toolbox_feature_brush_titleOpts(TypedDict, total=False):
    rect: str
    polygon: str
    lineX: str
    lineY: str
    keep: str
    clear: str

class Toolbox_feature_brushOpts(TypedDict, total=False):
    type: Any
    icon: Toolbox_feature_brush_iconOpts
    title: Toolbox_feature_brush_titleOpts

class Toolbox_featureOpts(TypedDict, total=False):
    saveAsImage: Toolbox_feature_saveasimageOpts
    restore: Toolbox_feature_restoreOpts
    dataView: Toolbox_feature_dataviewOpts
    dataZoom: Toolbox_feature_datazoomOpts
    magicType: Toolbox_feature_magictypeOpts
    brush: Toolbox_feature_brushOpts

class Toolbox_iconstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Toolbox_emphasis_iconstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    textPosition: str
    textFill: str
    textAlign: str
    textBackgroundColor: str
    textBorderRadius: int | float
    textPadding: int | float

class Toolbox_emphasisOpts(TypedDict, total=False):
    iconStyle: Toolbox_emphasis_iconstyleOpts

class ToolboxOpts(TypedDict, total=False):
    id: str
    show: bool
    orient: str
    itemSize: int | float
    itemGap: int | float
    showTitle: bool
    feature: Toolbox_featureOpts
    iconStyle: Toolbox_iconstyleOpts
    emphasis: Toolbox_emphasisOpts
    zlevel: int | float
    z: int | float
    left: int | float | str
    top: int | float | str
    right: int | float | str
    bottom: int | float | str
    width: int | float | str
    height: int | float | str
    coordinateSystem: str
    coordinateSystemUsage: str
    coord: str | int | float
    calendarIndex: int | float
    calendarId: int | float
    matrixIndex: int | float
    matrixId: int | float
    tooltip: dict[str, Any]

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

class Geo_projectionOpts(TypedDict, total=False):
    project: Callable[..., Any]
    unproject: Callable[..., Any]
    stream: Callable[..., Any]

class Geo_scalelimitOpts(TypedDict, total=False):
    min: int | float
    max: int | float

class Geo_label_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Geo_label_richOpts = dict[str, Geo_label_rich_styleOpts]

class Geo_labelOpts(TypedDict, total=False):
    show: bool
    position: str
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Geo_label_richOpts
    richInheritPlainLabel: bool

class Geo_itemstyleOpts(TypedDict, total=False):
    areaColor: str
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Geo_emphasis_label_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Geo_emphasis_label_richOpts = dict[str, Geo_emphasis_label_rich_styleOpts]

class Geo_emphasis_labelOpts(TypedDict, total=False):
    show: bool
    position: str
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Geo_emphasis_label_richOpts
    richInheritPlainLabel: bool

class Geo_emphasis_itemstyleOpts(TypedDict, total=False):
    areaColor: str
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Geo_emphasisOpts(TypedDict, total=False):
    disabled: bool
    focus: str
    label: Geo_emphasis_labelOpts
    itemStyle: Geo_emphasis_itemstyleOpts

class Geo_select_label_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Geo_select_label_richOpts = dict[str, Geo_select_label_rich_styleOpts]

class Geo_select_labelOpts(TypedDict, total=False):
    show: bool
    position: str
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Geo_select_label_richOpts
    richInheritPlainLabel: bool

class Geo_select_itemstyleOpts(TypedDict, total=False):
    areaColor: str
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Geo_selectOpts(TypedDict, total=False):
    disabled: bool
    label: Geo_select_labelOpts
    itemStyle: Geo_select_itemstyleOpts

class Geo_blur_label_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Geo_blur_label_richOpts = dict[str, Geo_blur_label_rich_styleOpts]

class Geo_blur_labelOpts(TypedDict, total=False):
    show: bool
    position: str
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Geo_blur_label_richOpts
    richInheritPlainLabel: bool

class Geo_blur_itemstyleOpts(TypedDict, total=False):
    areaColor: str
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Geo_blurOpts(TypedDict, total=False):
    label: Geo_blur_labelOpts
    itemStyle: Geo_blur_itemstyleOpts

class Geo_regions_item_itemstyleOpts(TypedDict, total=False):
    areaColor: str
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Geo_regions_item_label_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Geo_regions_item_label_richOpts = dict[str, Geo_regions_item_label_rich_styleOpts]

class Geo_regions_item_labelOpts(TypedDict, total=False):
    show: bool
    position: str
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Geo_regions_item_label_richOpts
    richInheritPlainLabel: bool

class Geo_regions_item_emphasis_itemstyleOpts(TypedDict, total=False):
    areaColor: str
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Geo_regions_item_emphasis_label_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Geo_regions_item_emphasis_label_richOpts = dict[str, Geo_regions_item_emphasis_label_rich_styleOpts]

class Geo_regions_item_emphasis_labelOpts(TypedDict, total=False):
    show: bool
    position: str
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Geo_regions_item_emphasis_label_richOpts
    richInheritPlainLabel: bool

class Geo_regions_item_emphasisOpts(TypedDict, total=False):
    itemStyle: Geo_regions_item_emphasis_itemstyleOpts
    label: Geo_regions_item_emphasis_labelOpts

class Geo_regions_item_select_itemstyleOpts(TypedDict, total=False):
    areaColor: str
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Geo_regions_item_select_label_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Geo_regions_item_select_label_richOpts = dict[str, Geo_regions_item_select_label_rich_styleOpts]

class Geo_regions_item_select_labelOpts(TypedDict, total=False):
    show: bool
    position: str
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Geo_regions_item_select_label_richOpts
    richInheritPlainLabel: bool

class Geo_regions_item_selectOpts(TypedDict, total=False):
    itemStyle: Geo_regions_item_select_itemstyleOpts
    label: Geo_regions_item_select_labelOpts

class Geo_regions_item_blur_itemstyleOpts(TypedDict, total=False):
    areaColor: str
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Geo_regions_item_blur_label_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Geo_regions_item_blur_label_richOpts = dict[str, Geo_regions_item_blur_label_rich_styleOpts]

class Geo_regions_item_blur_labelOpts(TypedDict, total=False):
    show: bool
    position: str
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Geo_regions_item_blur_label_richOpts
    richInheritPlainLabel: bool

class Geo_regions_item_blurOpts(TypedDict, total=False):
    itemStyle: Geo_regions_item_blur_itemstyleOpts
    label: Geo_regions_item_blur_labelOpts

class Geo_regions_item_tooltip_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str

class Geo_regions_item_tooltipOpts(TypedDict, total=False):
    show: bool
    position: str
    formatter: Callable[..., Any] | str
    valueFormatter: str
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    padding: int | float
    textStyle: Geo_regions_item_tooltip_textstyleOpts
    extraCssText: str

class Geo_regions_itemOpts(TypedDict, total=False):
    name: str
    selected: bool
    itemStyle: Geo_regions_item_itemstyleOpts
    label: Geo_regions_item_labelOpts
    emphasis: Geo_regions_item_emphasisOpts
    select: Geo_regions_item_selectOpts
    blur: Geo_regions_item_blurOpts
    tooltip: Geo_regions_item_tooltipOpts
    silent: bool

class Geo_tooltip_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str

class Geo_tooltipOpts(TypedDict, total=False):
    show: bool
    position: str
    formatter: Callable[..., Any] | str
    valueFormatter: str
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    padding: int | float
    textStyle: Geo_tooltip_textstyleOpts
    extraCssText: str

class GeoOpts(TypedDict, total=False):
    id: str
    show: bool
    map: str
    projection: Geo_projectionOpts
    center: Any
    zoom: int | float
    scaleLimit: Geo_scalelimitOpts
    roam: str | bool
    roamTrigger: str
    aspectScale: int | float
    boundingCoords: Any
    nameMap: dict[str, Any]
    nameProperty: str
    selectedMode: str | bool
    label: Geo_labelOpts
    itemStyle: Geo_itemstyleOpts
    emphasis: Geo_emphasisOpts
    select: Geo_selectOpts
    blur: Geo_blurOpts
    zlevel: int | float
    z: int | float
    left: int | float | str
    top: int | float | str
    right: int | float | str
    bottom: int | float | str
    width: int | float | str
    height: int | float | str
    layoutCenter: Any
    layoutSize: str | int | float
    preserveAspect: str | bool
    preserveAspectAlign: str
    preserveAspectVerticalAlign: str
    clip: bool
    coordinateSystem: str
    coordinateSystemUsage: str
    coord: str | int | float
    calendarIndex: int | float
    calendarId: int | float
    matrixIndex: int | float
    matrixId: int | float
    regions: list[Geo_regions_itemOpts]
    silent: bool
    tooltip: Geo_tooltipOpts

class Parallel_parallelaxisdefault_nametextstyle_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Parallel_parallelaxisdefault_nametextstyle_richOpts = dict[str, Parallel_parallelaxisdefault_nametextstyle_rich_styleOpts]

class Parallel_parallelaxisdefault_nametextstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Parallel_parallelaxisdefault_nametextstyle_richOpts
    richInheritPlainLabel: bool

class Parallel_parallelaxisdefault_nametruncateOpts(TypedDict, total=False):
    maxWidth: int | float
    ellipsis: str

class Parallel_parallelaxisdefault_axisline_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Parallel_parallelaxisdefault_axislineOpts(TypedDict, total=False):
    show: bool
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: Parallel_parallelaxisdefault_axisline_linestyleOpts

class Parallel_parallelaxisdefault_axistick_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Parallel_parallelaxisdefault_axistickOpts(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    length: int | float
    lineStyle: Parallel_parallelaxisdefault_axistick_linestyleOpts
    customValues: Any

class Parallel_parallelaxisdefault_minortick_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Parallel_parallelaxisdefault_minortickOpts(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: Parallel_parallelaxisdefault_minortick_linestyleOpts

class Parallel_parallelaxisdefault_axislabel_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Parallel_parallelaxisdefault_axislabel_richOpts = dict[str, Parallel_parallelaxisdefault_axislabel_rich_styleOpts]

class Parallel_parallelaxisdefault_axislabelOpts(TypedDict, total=False):
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
    color: Callable[..., Any] | str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Parallel_parallelaxisdefault_axislabel_richOpts
    richInheritPlainLabel: bool

class Parallel_parallelaxisdefault_data_item_textstyle_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Parallel_parallelaxisdefault_data_item_textstyle_richOpts = dict[str, Parallel_parallelaxisdefault_data_item_textstyle_rich_styleOpts]

class Parallel_parallelaxisdefault_data_item_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Parallel_parallelaxisdefault_data_item_textstyle_richOpts
    richInheritPlainLabel: bool

class Parallel_parallelaxisdefault_data_itemOpts(TypedDict, total=False):
    value: str
    textStyle: Parallel_parallelaxisdefault_data_item_textstyleOpts

class Parallel_parallelaxisdefault_tooltip_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str

class Parallel_parallelaxisdefault_tooltipOpts(TypedDict, total=False):
    show: bool
    position: str
    formatter: Callable[..., Any] | str
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    padding: int | float
    textStyle: Parallel_parallelaxisdefault_tooltip_textstyleOpts
    extraCssText: str

class Parallel_parallelaxisdefaultOpts(TypedDict, total=False):
    type: str
    name: str
    nameLocation: str
    nameTextStyle: Parallel_parallelaxisdefault_nametextstyleOpts
    nameGap: int | float
    nameRotate: int | float
    nameTruncate: Parallel_parallelaxisdefault_nametruncateOpts
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
    axisLine: Parallel_parallelaxisdefault_axislineOpts
    axisTick: Parallel_parallelaxisdefault_axistickOpts
    minorTick: Parallel_parallelaxisdefault_minortickOpts
    axisLabel: Parallel_parallelaxisdefault_axislabelOpts
    data: list[Parallel_parallelaxisdefault_data_itemOpts]
    tooltip: Parallel_parallelaxisdefault_tooltipOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: str
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: str
    animationDelayUpdate: Callable[..., Any] | int | float

class ParallelOpts(TypedDict, total=False):
    id: str
    zlevel: int | float
    z: int | float
    left: int | float | str
    top: int | float | str
    right: int | float | str
    bottom: int | float | str
    width: int | float | str
    height: int | float | str
    coordinateSystem: str
    coordinateSystemUsage: str
    coord: str | int | float
    calendarIndex: int | float
    calendarId: int | float
    matrixIndex: int | float
    matrixId: int | float
    layout: str
    axisExpandable: bool
    axisExpandCenter: int | float
    axisExpandCount: int | float
    axisExpandWidth: int | float
    axisExpandTriggerOn: str
    parallelAxisDefault: Parallel_parallelaxisdefaultOpts

class Parallelaxis_areaselectstyleOpts(TypedDict, total=False):
    width: int | float
    borderWidth: int | float
    borderColor: str
    color: str
    opacity: int | float

class Parallelaxis_nametextstyle_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Parallelaxis_nametextstyle_richOpts = dict[str, Parallelaxis_nametextstyle_rich_styleOpts]

class Parallelaxis_nametextstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Parallelaxis_nametextstyle_richOpts
    richInheritPlainLabel: bool

class Parallelaxis_nametruncateOpts(TypedDict, total=False):
    maxWidth: int | float
    ellipsis: str

class Parallelaxis_axisline_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Parallelaxis_axislineOpts(TypedDict, total=False):
    show: bool
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: Parallelaxis_axisline_linestyleOpts

class Parallelaxis_axistick_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Parallelaxis_axistickOpts(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    length: int | float
    lineStyle: Parallelaxis_axistick_linestyleOpts
    customValues: Any

class Parallelaxis_minortick_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Parallelaxis_minortickOpts(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: Parallelaxis_minortick_linestyleOpts

class Parallelaxis_axislabel_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Parallelaxis_axislabel_richOpts = dict[str, Parallelaxis_axislabel_rich_styleOpts]

class Parallelaxis_axislabelOpts(TypedDict, total=False):
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
    color: Callable[..., Any] | str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Parallelaxis_axislabel_richOpts
    richInheritPlainLabel: bool

class Parallelaxis_data_item_textstyle_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Parallelaxis_data_item_textstyle_richOpts = dict[str, Parallelaxis_data_item_textstyle_rich_styleOpts]

class Parallelaxis_data_item_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Parallelaxis_data_item_textstyle_richOpts
    richInheritPlainLabel: bool

class Parallelaxis_data_itemOpts(TypedDict, total=False):
    value: str
    textStyle: Parallelaxis_data_item_textstyleOpts

class Parallelaxis_tooltip_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str

class Parallelaxis_tooltipOpts(TypedDict, total=False):
    show: bool
    position: str
    formatter: Callable[..., Any] | str
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    padding: int | float
    textStyle: Parallelaxis_tooltip_textstyleOpts
    extraCssText: str

class ParallelaxisOpts(TypedDict, total=False):
    id: str
    dim: int | float
    parallelIndex: int | float
    realtime: bool
    areaSelectStyle: Parallelaxis_areaselectstyleOpts
    type: str
    name: str
    nameLocation: str
    nameTextStyle: Parallelaxis_nametextstyleOpts
    nameGap: int | float
    nameRotate: int | float
    nameTruncate: Parallelaxis_nametruncateOpts
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
    axisLine: Parallelaxis_axislineOpts
    axisTick: Parallelaxis_axistickOpts
    minorTick: Parallelaxis_minortickOpts
    axisLabel: Parallelaxis_axislabelOpts
    data: list[Parallelaxis_data_itemOpts]
    tooltip: Parallelaxis_tooltipOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: str
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: str
    animationDelayUpdate: Callable[..., Any] | int | float

class Singleaxis_nametextstyle_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Singleaxis_nametextstyle_richOpts = dict[str, Singleaxis_nametextstyle_rich_styleOpts]

class Singleaxis_nametextstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Singleaxis_nametextstyle_richOpts
    richInheritPlainLabel: bool

class Singleaxis_nametruncateOpts(TypedDict, total=False):
    maxWidth: int | float
    ellipsis: str

class Singleaxis_axisline_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Singleaxis_axislineOpts(TypedDict, total=False):
    show: bool
    symbol: str
    symbolSize: Any
    symbolOffset: int | float
    lineStyle: Singleaxis_axisline_linestyleOpts

class Singleaxis_axistick_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Singleaxis_axistickOpts(TypedDict, total=False):
    show: bool
    alignWithLabel: bool
    interval: Callable[..., Any] | int | float
    inside: bool
    length: int | float
    lineStyle: Singleaxis_axistick_linestyleOpts
    customValues: Any

class Singleaxis_minortick_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Singleaxis_minortickOpts(TypedDict, total=False):
    show: bool
    splitNumber: int | float
    length: int | float
    lineStyle: Singleaxis_minortick_linestyleOpts

class Singleaxis_axislabel_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Singleaxis_axislabel_richOpts = dict[str, Singleaxis_axislabel_rich_styleOpts]

class Singleaxis_axislabelOpts(TypedDict, total=False):
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
    color: Callable[..., Any] | str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Singleaxis_axislabel_richOpts
    richInheritPlainLabel: bool

class Singleaxis_splitline_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Singleaxis_splitlineOpts(TypedDict, total=False):
    show: bool
    showMinLine: bool
    showMaxLine: bool
    interval: Callable[..., Any] | int | float
    lineStyle: Singleaxis_splitline_linestyleOpts

class Singleaxis_minorsplitline_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Singleaxis_minorsplitlineOpts(TypedDict, total=False):
    show: bool
    lineStyle: Singleaxis_minorsplitline_linestyleOpts

class Singleaxis_splitarea_areastyleOpts(TypedDict, total=False):
    color: Any
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Singleaxis_splitareaOpts(TypedDict, total=False):
    interval: Callable[..., Any] | int | float
    show: bool
    areaStyle: Singleaxis_splitarea_areastyleOpts

class Singleaxis_data_item_textstyle_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Singleaxis_data_item_textstyle_richOpts = dict[str, Singleaxis_data_item_textstyle_rich_styleOpts]

class Singleaxis_data_item_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Singleaxis_data_item_textstyle_richOpts
    richInheritPlainLabel: bool

class Singleaxis_data_itemOpts(TypedDict, total=False):
    value: str
    textStyle: Singleaxis_data_item_textstyleOpts

class Singleaxis_axispointer_labelOpts(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: Callable[..., Any] | str
    margin: int | float
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    padding: str
    backgroundColor: str
    borderColor: str
    borderWidth: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class Singleaxis_axispointer_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Singleaxis_axispointer_shadowstyleOpts(TypedDict, total=False):
    color: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Singleaxis_axispointer_handleOpts(TypedDict, total=False):
    show: bool
    icon: Any
    size: int | float
    margin: int | float
    color: str
    throttle: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class Singleaxis_axispointerOpts(TypedDict, total=False):
    show: bool
    type: str
    snap: bool
    z: int | float
    label: Singleaxis_axispointer_labelOpts
    lineStyle: Singleaxis_axispointer_linestyleOpts
    shadowStyle: Singleaxis_axispointer_shadowstyleOpts
    triggerEmphasis: bool
    triggerTooltip: bool
    value: int | float
    status: bool
    handle: Singleaxis_axispointer_handleOpts

class Singleaxis_tooltip_axispointer_labelOpts(TypedDict, total=False):
    show: bool
    precision: str | int | float
    formatter: Callable[..., Any] | str
    margin: int | float
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    padding: str
    backgroundColor: str
    borderColor: str
    borderWidth: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float

class Singleaxis_tooltip_axispointer_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Singleaxis_tooltip_axispointer_shadowstyleOpts(TypedDict, total=False):
    color: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Singleaxis_tooltip_axispointer_crossstyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Singleaxis_tooltip_axispointerOpts(TypedDict, total=False):
    type: str
    axis: str
    snap: bool
    z: int | float
    label: Singleaxis_tooltip_axispointer_labelOpts
    lineStyle: Singleaxis_tooltip_axispointer_linestyleOpts
    shadowStyle: Singleaxis_tooltip_axispointer_shadowstyleOpts
    crossStyle: Singleaxis_tooltip_axispointer_crossstyleOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: str
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: str
    animationDelayUpdate: Callable[..., Any] | int | float

class Singleaxis_tooltip_textstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str

class Singleaxis_tooltipOpts(TypedDict, total=False):
    show: bool
    trigger: str
    axisPointer: Singleaxis_tooltip_axispointerOpts
    position: str
    formatter: Callable[..., Any] | str
    valueFormatter: str
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    padding: int | float
    textStyle: Singleaxis_tooltip_textstyleOpts
    extraCssText: str

class SingleaxisOpts(TypedDict, total=False):
    id: str
    zlevel: int | float
    z: int | float
    left: int | float | str
    top: int | float | str
    right: int | float | str
    bottom: int | float | str
    width: int | float | str
    height: int | float | str
    orient: str
    type: str
    name: str
    nameLocation: str
    nameTextStyle: Singleaxis_nametextstyleOpts
    nameGap: int | float
    nameRotate: int | float
    nameTruncate: Singleaxis_nametruncateOpts
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
    axisLine: Singleaxis_axislineOpts
    axisTick: Singleaxis_axistickOpts
    minorTick: Singleaxis_minortickOpts
    axisLabel: Singleaxis_axislabelOpts
    splitLine: Singleaxis_splitlineOpts
    minorSplitLine: Singleaxis_minorsplitlineOpts
    splitArea: Singleaxis_splitareaOpts
    data: list[Singleaxis_data_itemOpts]
    axisPointer: Singleaxis_axispointerOpts
    tooltip: Singleaxis_tooltipOpts
    animation: bool
    animationThreshold: int | float
    animationDuration: Callable[..., Any] | int | float
    animationEasing: str
    animationDelay: Callable[..., Any] | int | float
    animationDurationUpdate: Callable[..., Any] | int | float
    animationEasingUpdate: str
    animationDelayUpdate: Callable[..., Any] | int | float

class Timeline_linestyleOpts(TypedDict, total=False):
    show: bool
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Timeline_label_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Timeline_label_richOpts = dict[str, Timeline_label_rich_styleOpts]

class Timeline_labelOpts(TypedDict, total=False):
    position: int | float | str
    show: bool
    interval: int | float | str
    rotate: Any
    formatter: Callable[..., Any] | str
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Timeline_label_richOpts
    richInheritPlainLabel: bool

class Timeline_itemstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Timeline_checkpointstyleOpts(TypedDict, total=False):
    symbol: str
    symbolSize: int | float
    symbolRotate: int | float
    symbolKeepAspect: bool
    symbolOffset: Any
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float
    animation: bool
    animationDuration: int | float
    animationEasing: str

class Timeline_controlstyleOpts(TypedDict, total=False):
    show: bool
    showPlayBtn: bool
    showPrevBtn: bool
    showNextBtn: bool
    itemSize: int | float
    itemGap: int | float
    position: str
    playIcon: str
    stopIcon: str
    prevIcon: str
    nextIcon: str
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Timeline_progress_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Timeline_progress_itemstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Timeline_progress_label_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Timeline_progress_label_richOpts = dict[str, Timeline_progress_label_rich_styleOpts]

class Timeline_progress_labelOpts(TypedDict, total=False):
    show: bool
    interval: int | float | str
    rotate: Any
    formatter: Callable[..., Any] | str
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Timeline_progress_label_richOpts
    richInheritPlainLabel: bool

class Timeline_progressOpts(TypedDict, total=False):
    lineStyle: Timeline_progress_linestyleOpts
    itemStyle: Timeline_progress_itemstyleOpts
    label: Timeline_progress_labelOpts

class Timeline_emphasis_label_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Timeline_emphasis_label_richOpts = dict[str, Timeline_emphasis_label_rich_styleOpts]

class Timeline_emphasis_labelOpts(TypedDict, total=False):
    show: bool
    interval: int | float | str
    rotate: Any
    formatter: Callable[..., Any] | str
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Timeline_emphasis_label_richOpts
    richInheritPlainLabel: bool

class Timeline_emphasis_itemstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Timeline_emphasisOpts(TypedDict, total=False):
    label: Timeline_emphasis_labelOpts
    itemStyle: Timeline_emphasis_itemstyleOpts
    checkpointStyle: dict[str, Any]
    controlStyle: dict[str, Any]

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
    controlPosition: str
    zlevel: int | float
    z: int | float
    left: int | float | str
    top: int | float | str
    right: int | float | str
    bottom: int | float | str
    coordinateSystem: str
    coordinateSystemUsage: str
    coord: str | int | float
    calendarIndex: int | float
    calendarId: int | float
    matrixIndex: int | float
    matrixId: int | float
    padding: int | float
    orient: str
    inverse: bool
    symbol: str
    symbolSize: int | float
    symbolRotate: int | float
    symbolKeepAspect: bool
    symbolOffset: Any
    lineStyle: Timeline_linestyleOpts
    label: Timeline_labelOpts
    itemStyle: Timeline_itemstyleOpts
    checkpointStyle: Timeline_checkpointstyleOpts
    controlStyle: Timeline_controlstyleOpts
    progress: Timeline_progressOpts
    emphasis: Timeline_emphasisOpts
    data: Any

class GraphicOpts(TypedDict, total=False):
    id: str
    elements: Any

class Calendar_splitline_linestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Calendar_splitlineOpts(TypedDict, total=False):
    show: bool
    lineStyle: Calendar_splitline_linestyleOpts

class Calendar_itemstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Calendar_daylabel_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Calendar_daylabel_richOpts = dict[str, Calendar_daylabel_rich_styleOpts]

class Calendar_daylabelOpts(TypedDict, total=False):
    show: bool
    firstDay: int | float
    margin: int | float
    position: str
    nameMap: str
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Calendar_daylabel_richOpts
    richInheritPlainLabel: bool
    silent: bool

class Calendar_monthlabel_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Calendar_monthlabel_richOpts = dict[str, Calendar_monthlabel_rich_styleOpts]

class Calendar_monthlabelOpts(TypedDict, total=False):
    show: bool
    align: str
    margin: int | float
    position: str
    nameMap: str
    formatter: Callable[..., Any] | str
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Calendar_monthlabel_richOpts
    richInheritPlainLabel: bool
    silent: bool

class Calendar_yearlabel_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Calendar_yearlabel_richOpts = dict[str, Calendar_yearlabel_rich_styleOpts]

class Calendar_yearlabelOpts(TypedDict, total=False):
    show: bool
    margin: int | float
    position: str
    formatter: Callable[..., Any] | str
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Calendar_yearlabel_richOpts
    richInheritPlainLabel: bool
    silent: bool

class CalendarOpts(TypedDict, total=False):
    id: str
    zlevel: int | float
    z: int | float
    left: int | float | str
    top: int | float | str
    right: int | float | str
    bottom: int | float | str
    width: str | int | float
    height: str | int | float
    range: str | int | float
    cellSize: int | float
    orient: str
    splitLine: Calendar_splitlineOpts
    itemStyle: Calendar_itemstyleOpts
    dayLabel: Calendar_daylabelOpts
    monthLabel: Calendar_monthlabelOpts
    yearLabel: Calendar_yearlabelOpts
    silent: bool

class Matrix_x_data_itemOpts(TypedDict, total=False):
    value: int | float | str
    children: Any
    size: int | float

class Matrix_x_label_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Matrix_x_label_richOpts = dict[str, Matrix_x_label_rich_styleOpts]

class Matrix_x_labelOpts(TypedDict, total=False):
    show: bool
    position: str
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Matrix_x_label_richOpts
    richInheritPlainLabel: bool

class Matrix_x_itemstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Matrix_x_levels_itemOpts(TypedDict, total=False):
    levelSize: str | int | float

class Matrix_x_dividerlinestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Matrix_xOpts(TypedDict, total=False):
    show: bool
    data: list[Matrix_x_data_itemOpts]
    length: int | float
    label: Matrix_x_labelOpts
    itemStyle: Matrix_x_itemstyleOpts
    silent: bool
    cursor: str
    z2: int | float
    levelSize: str | int | float
    levels: list[Matrix_x_levels_itemOpts]
    dividerLineStyle: Matrix_x_dividerlinestyleOpts

class Matrix_y_data_itemOpts(TypedDict, total=False):
    value: int | float | str
    children: Any
    size: int | float

class Matrix_y_label_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Matrix_y_label_richOpts = dict[str, Matrix_y_label_rich_styleOpts]

class Matrix_y_labelOpts(TypedDict, total=False):
    show: bool
    position: str
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Matrix_y_label_richOpts
    richInheritPlainLabel: bool

class Matrix_y_itemstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Matrix_y_levels_itemOpts(TypedDict, total=False):
    levelSize: str | int | float

class Matrix_y_dividerlinestyleOpts(TypedDict, total=False):
    color: str
    width: int | float
    type: int | float | str
    dashOffset: int | float
    cap: str
    join: str
    miterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Matrix_yOpts(TypedDict, total=False):
    show: bool
    data: list[Matrix_y_data_itemOpts]
    length: int | float
    label: Matrix_y_labelOpts
    itemStyle: Matrix_y_itemstyleOpts
    silent: bool
    cursor: str
    z2: int | float
    levelSize: str | int | float
    levels: list[Matrix_y_levels_itemOpts]
    dividerLineStyle: Matrix_y_dividerlinestyleOpts

class Matrix_body_data_itemOpts(TypedDict, total=False):
    coord: Any
    coordClamp: bool
    mergeCells: bool
    value: int | float | str

class Matrix_body_label_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Matrix_body_label_richOpts = dict[str, Matrix_body_label_rich_styleOpts]

class Matrix_body_labelOpts(TypedDict, total=False):
    show: bool
    position: str
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Matrix_body_label_richOpts
    richInheritPlainLabel: bool

class Matrix_body_itemstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Matrix_bodyOpts(TypedDict, total=False):
    data: list[Matrix_body_data_itemOpts]
    label: Matrix_body_labelOpts
    itemStyle: Matrix_body_itemstyleOpts
    silent: bool
    cursor: str
    z2: int | float

class Matrix_corner_data_itemOpts(TypedDict, total=False):
    coord: Any
    coordClamp: bool
    mergeCells: bool
    value: int | float | str

class Matrix_corner_label_rich_styleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: str | int | float
    height: str | int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float

Matrix_corner_label_richOpts = dict[str, Matrix_corner_label_rich_styleOpts]

class Matrix_corner_labelOpts(TypedDict, total=False):
    show: bool
    position: str
    distance: int | float
    rotate: int | float
    offset: Any
    formatter: Callable[..., Any] | str
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    align: str
    verticalAlign: str
    lineHeight: int | float
    backgroundColor: dict[str, Any] | str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderRadius: int | float
    padding: int | float
    shadowColor: str
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str
    rich: Matrix_corner_label_richOpts
    richInheritPlainLabel: bool

class Matrix_corner_itemstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Matrix_cornerOpts(TypedDict, total=False):
    data: list[Matrix_corner_data_itemOpts]
    label: Matrix_corner_labelOpts
    itemStyle: Matrix_corner_itemstyleOpts
    silent: bool
    cursor: str
    z2: int | float

class Matrix_backgroundstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class MatrixOpts(TypedDict, total=False):
    id: str
    zlevel: int | float
    z: int | float
    left: int | float | str
    top: int | float | str
    right: int | float | str
    bottom: int | float | str
    width: int | float | str
    height: int | float | str
    x: Matrix_xOpts
    y: Matrix_yOpts
    body: Matrix_bodyOpts
    corner: Matrix_cornerOpts
    backgroundStyle: Matrix_backgroundstyleOpts
    borderZ2: int | float
    tooltip: dict[str, Any]
    triggerEvent: bool

class Thumbnail_itemstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class Thumbnail_windowstyleOpts(TypedDict, total=False):
    color: str
    borderColor: str
    borderWidth: int | float
    borderType: int | float | str
    borderDashOffset: int | float
    borderCap: str
    borderJoin: str
    borderMiterLimit: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    opacity: int | float

class ThumbnailOpts(TypedDict, total=False):
    id: str
    show: bool
    zlevel: int | float
    z: int | float
    left: int | float | str
    top: int | float | str
    right: int | float | str
    bottom: int | float | str
    width: int | float | str
    height: int | float | str
    coordinateSystem: str
    coordinateSystemUsage: str
    coord: str | int | float
    calendarIndex: int | float
    calendarId: int | float
    matrixIndex: int | float
    matrixId: int | float
    itemStyle: Thumbnail_itemstyleOpts
    windowStyle: Thumbnail_windowstyleOpts
    seriesIndex: int | float
    seriesId: int | float | str

class DatasetOpts(TypedDict, total=False):
    id: str
    source: dict[str, Any]
    dimensions: Any
    sourceHeader: int | float | bool
    transform: Any
    fromDatasetIndex: int | float
    fromDatasetId: str
    fromTransformResult: int | float

class Aria_label_generalOpts(TypedDict, total=False):
    withTitle: str
    withoutTitle: str

class Aria_label_series_singleOpts(TypedDict, total=False):
    prefix: str
    withName: str
    withoutName: str

class Aria_label_series_multiple_separatorOpts(TypedDict, total=False):
    middle: str
    end: str

class Aria_label_series_multipleOpts(TypedDict, total=False):
    prefix: str
    withName: str
    withoutName: str
    separator: Aria_label_series_multiple_separatorOpts

class Aria_label_seriesOpts(TypedDict, total=False):
    maxCount: int | float
    single: Aria_label_series_singleOpts
    multiple: Aria_label_series_multipleOpts

class Aria_label_data_separatorOpts(TypedDict, total=False):
    middle: str
    end: str

class Aria_label_dataOpts(TypedDict, total=False):
    maxCount: int | float
    allData: str
    partialData: str
    withName: str
    withoutName: str
    excludeDimensionId: Any
    separator: Aria_label_data_separatorOpts

class Aria_labelOpts(TypedDict, total=False):
    enabled: bool
    description: str
    general: Aria_label_generalOpts
    series: Aria_label_seriesOpts
    data: Aria_label_dataOpts

class Aria_decal_decalsOpts(TypedDict, total=False):
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

class Aria_decalOpts(TypedDict, total=False):
    show: bool
    decals: Aria_decal_decalsOpts

class AriaOpts(TypedDict, total=False):
    enabled: bool
    label: Aria_labelOpts
    decal: Aria_decalOpts

class TextstyleOpts(TypedDict, total=False):
    color: str
    fontStyle: str
    fontWeight: int | float | str
    fontFamily: str
    fontSize: int | float
    lineHeight: int | float
    width: int | float
    height: int | float
    textBorderColor: str
    textBorderWidth: int | float
    textBorderType: int | float | str
    textBorderDashOffset: int | float
    textShadowColor: str
    textShadowBlur: int | float
    textShadowOffsetX: int | float
    textShadowOffsetY: int | float
    overflow: str
    ellipsis: str

class StateanimationOpts(TypedDict, total=False):
    duration: int | float
    easing: str

class Globe_realisticmaterialOpts(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float
    roughness: str | int | float
    metalness: str | int | float
    roughnessAdjust: int | float
    metalnessAdjust: int | float
    normalTexture: str

class Globe_lambertmaterialOpts(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float

class Globe_colormaterialOpts(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float

class Globe_light_mainOpts(TypedDict, total=False):
    color: str
    intensity: int | float
    shadow: bool
    shadowQuality: str
    alpha: int | float
    beta: int | float
    time: Any

class Globe_light_ambientOpts(TypedDict, total=False):
    color: str
    intensity: int | float

class Globe_light_ambientcubemapOpts(TypedDict, total=False):
    texture: str
    diffuseIntensity: int | float
    specularIntensity: int | float

class Globe_lightOpts(TypedDict, total=False):
    main: Globe_light_mainOpts
    ambient: Globe_light_ambientOpts
    ambientCubemap: Globe_light_ambientcubemapOpts

class Globe_atmosphereOpts(TypedDict, total=False):
    show: bool
    offset: int | float
    color: str
    glowPower: int | float
    innerGlowPower: int | float

class Globe_posteffect_bloomOpts(TypedDict, total=False):
    enable: bool
    bloomIntensity: int | float

class Globe_posteffect_depthoffieldOpts(TypedDict, total=False):
    enable: bool
    focalDistance: bool
    focalRange: bool
    fstop: int | float
    blurRadius: int | float

class Globe_posteffect_ssaoOpts(TypedDict, total=False):
    enable: bool
    quality: str
    radius: int | float
    intensity: int | float

class Globe_posteffect_colorcorrectionOpts(TypedDict, total=False):
    enable: bool
    lookupTexture: str
    exposure: int | float
    brightness: int | float
    contrast: int | float
    saturation: int | float

class Globe_posteffect_fxaaOpts(TypedDict, total=False):
    enable: bool

class Globe_posteffectOpts(TypedDict, total=False):
    enable: bool
    bloom: Globe_posteffect_bloomOpts
    depthOfField: Globe_posteffect_depthoffieldOpts
    screenSpaceAmbientOcclusion: dict[str, Any]
    SSAO: Globe_posteffect_ssaoOpts
    colorCorrection: Globe_posteffect_colorcorrectionOpts
    FXAA: Globe_posteffect_fxaaOpts

class Globe_temporalsupersamplingOpts(TypedDict, total=False):
    enable: bool

class Globe_viewcontrolOpts(TypedDict, total=False):
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

class Globe_layers_itemOpts(TypedDict, total=False):
    show: bool
    type: str
    name: str
    blendTo: str
    intensity: int | float
    shading: str
    distance: int | float
    texture: str

class GlobeOpts(TypedDict, total=False):
    show: bool
    zlevel: int | float
    left: int | float | str
    top: int | float | str
    right: int | float | str
    bottom: int | float | str
    width: int | float | str
    height: int | float | str
    globeRadius: int | float
    globeOuterRadius: int | float
    environment: str
    baseTexture: str
    heightTexture: str
    displacementTexture: str
    displacementScale: int | float
    displacementQuality: str
    shading: str
    realisticMaterial: Globe_realisticmaterialOpts
    lambertMaterial: Globe_lambertmaterialOpts
    colorMaterial: Globe_colormaterialOpts
    light: Globe_lightOpts
    atmosphere: Globe_atmosphereOpts
    postEffect: Globe_posteffectOpts
    temporalSuperSampling: Globe_temporalsupersamplingOpts
    viewControl: Globe_viewcontrolOpts
    layers: list[Globe_layers_itemOpts]

class Geo3d_groundplaneOpts(TypedDict, total=False):
    show: bool
    color: str

class Geo3d_label_textstyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Geo3d_labelOpts(TypedDict, total=False):
    show: bool
    distance: int | float
    formatter: Callable[..., Any] | str
    textStyle: Geo3d_label_textstyleOpts

class Geo3d_itemstyleOpts(TypedDict, total=False):
    color: Callable[..., Any] | str
    opacity: int | float
    borderWidth: int | float
    borderColor: str

class Geo3d_emphasis_label_textstyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Geo3d_emphasis_labelOpts(TypedDict, total=False):
    show: bool
    distance: int | float
    formatter: Callable[..., Any] | str
    textStyle: Geo3d_emphasis_label_textstyleOpts

class Geo3d_emphasis_itemstyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float

class Geo3d_emphasisOpts(TypedDict, total=False):
    label: Geo3d_emphasis_labelOpts
    itemStyle: Geo3d_emphasis_itemstyleOpts

class Geo3d_regions_item_itemstyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    borderWidth: int | float
    borderColor: str

class Geo3d_regions_item_label_textstyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Geo3d_regions_item_labelOpts(TypedDict, total=False):
    show: bool
    distance: int | float
    formatter: Callable[..., Any] | str
    textStyle: Geo3d_regions_item_label_textstyleOpts

class Geo3d_regions_item_emphasis_itemstyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    borderWidth: int | float
    borderColor: str

class Geo3d_regions_item_emphasis_label_textstyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Geo3d_regions_item_emphasis_labelOpts(TypedDict, total=False):
    show: bool
    distance: int | float
    formatter: Callable[..., Any] | str
    textStyle: Geo3d_regions_item_emphasis_label_textstyleOpts

class Geo3d_regions_item_emphasisOpts(TypedDict, total=False):
    itemStyle: Geo3d_regions_item_emphasis_itemstyleOpts
    label: Geo3d_regions_item_emphasis_labelOpts

class Geo3d_regions_itemOpts(TypedDict, total=False):
    name: str
    regionHeight: int | float
    itemStyle: Geo3d_regions_item_itemstyleOpts
    label: Geo3d_regions_item_labelOpts
    emphasis: Geo3d_regions_item_emphasisOpts

class Geo3d_realisticmaterialOpts(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float
    roughness: str | int | float
    metalness: str | int | float
    roughnessAdjust: int | float
    metalnessAdjust: int | float
    normalTexture: str

class Geo3d_lambertmaterialOpts(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float

class Geo3d_colormaterialOpts(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float

class Geo3d_light_mainOpts(TypedDict, total=False):
    color: str
    intensity: int | float
    shadow: bool
    shadowQuality: str
    alpha: int | float
    beta: int | float

class Geo3d_light_ambientOpts(TypedDict, total=False):
    color: str
    intensity: int | float

class Geo3d_light_ambientcubemapOpts(TypedDict, total=False):
    texture: str
    diffuseIntensity: int | float
    specularIntensity: int | float

class Geo3d_lightOpts(TypedDict, total=False):
    main: Geo3d_light_mainOpts
    ambient: Geo3d_light_ambientOpts
    ambientCubemap: Geo3d_light_ambientcubemapOpts

class Geo3d_posteffect_bloomOpts(TypedDict, total=False):
    enable: bool
    bloomIntensity: int | float

class Geo3d_posteffect_depthoffieldOpts(TypedDict, total=False):
    enable: bool
    focalDistance: bool
    focalRange: bool
    fstop: int | float
    blurRadius: int | float

class Geo3d_posteffect_ssaoOpts(TypedDict, total=False):
    enable: bool
    quality: str
    radius: int | float
    intensity: int | float

class Geo3d_posteffect_colorcorrectionOpts(TypedDict, total=False):
    enable: bool
    lookupTexture: str
    exposure: int | float
    brightness: int | float
    contrast: int | float
    saturation: int | float

class Geo3d_posteffect_fxaaOpts(TypedDict, total=False):
    enable: bool

class Geo3d_posteffectOpts(TypedDict, total=False):
    enable: bool
    bloom: Geo3d_posteffect_bloomOpts
    depthOfField: Geo3d_posteffect_depthoffieldOpts
    screenSpaceAmbientOcclusion: dict[str, Any]
    SSAO: Geo3d_posteffect_ssaoOpts
    colorCorrection: Geo3d_posteffect_colorcorrectionOpts
    FXAA: Geo3d_posteffect_fxaaOpts

class Geo3d_temporalsupersamplingOpts(TypedDict, total=False):
    enable: bool

class Geo3d_viewcontrolOpts(TypedDict, total=False):
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

class Geo3dOpts(TypedDict, total=False):
    show: bool
    map: str
    boxWidth: int | float
    boxHeight: int | float
    boxDepth: int | float
    regionHeight: int | float
    environment: str
    groundPlane: Geo3d_groundplaneOpts
    instancing: bool
    label: Geo3d_labelOpts
    itemStyle: Geo3d_itemstyleOpts
    emphasis: Geo3d_emphasisOpts
    regions: list[Geo3d_regions_itemOpts]
    shading: str
    realisticMaterial: Geo3d_realisticmaterialOpts
    lambertMaterial: Geo3d_lambertmaterialOpts
    colorMaterial: Geo3d_colormaterialOpts
    light: Geo3d_lightOpts
    postEffect: Geo3d_posteffectOpts
    temporalSuperSampling: Geo3d_temporalsupersamplingOpts
    viewControl: Geo3d_viewcontrolOpts
    zlevel: int | float
    left: int | float | str
    top: int | float | str
    right: int | float | str
    bottom: int | float | str
    width: int | float | str
    height: int | float | str

class Mapbox3d_realisticmaterialOpts(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float
    roughness: str | int | float
    metalness: str | int | float
    roughnessAdjust: int | float
    metalnessAdjust: int | float
    normalTexture: str

class Mapbox3d_lambertmaterialOpts(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float

class Mapbox3d_colormaterialOpts(TypedDict, total=False):
    detailTexture: str
    textureTiling: int | float
    textureOffset: int | float

class Mapbox3d_light_mainOpts(TypedDict, total=False):
    color: str
    intensity: int | float
    shadow: bool
    shadowQuality: str
    alpha: int | float
    beta: int | float

class Mapbox3d_light_ambientOpts(TypedDict, total=False):
    color: str
    intensity: int | float

class Mapbox3d_light_ambientcubemapOpts(TypedDict, total=False):
    texture: str
    diffuseIntensity: int | float
    specularIntensity: int | float

class Mapbox3d_lightOpts(TypedDict, total=False):
    main: Mapbox3d_light_mainOpts
    ambient: Mapbox3d_light_ambientOpts
    ambientCubemap: Mapbox3d_light_ambientcubemapOpts

class Mapbox3d_posteffect_bloomOpts(TypedDict, total=False):
    enable: bool
    bloomIntensity: int | float

class Mapbox3d_posteffect_depthoffieldOpts(TypedDict, total=False):
    enable: bool
    focalDistance: bool
    focalRange: bool
    fstop: int | float
    blurRadius: int | float

class Mapbox3d_posteffect_ssaoOpts(TypedDict, total=False):
    enable: bool
    quality: str
    radius: int | float
    intensity: int | float

class Mapbox3d_posteffect_colorcorrectionOpts(TypedDict, total=False):
    enable: bool
    lookupTexture: str
    exposure: int | float
    brightness: int | float
    contrast: int | float
    saturation: int | float

class Mapbox3d_posteffect_fxaaOpts(TypedDict, total=False):
    enable: bool

class Mapbox3d_posteffectOpts(TypedDict, total=False):
    enable: bool
    bloom: Mapbox3d_posteffect_bloomOpts
    depthOfField: Mapbox3d_posteffect_depthoffieldOpts
    screenSpaceAmbientOcclusion: dict[str, Any]
    SSAO: Mapbox3d_posteffect_ssaoOpts
    colorCorrection: Mapbox3d_posteffect_colorcorrectionOpts
    FXAA: Mapbox3d_posteffect_fxaaOpts

class Mapbox3d_temporalsupersamplingOpts(TypedDict, total=False):
    enable: bool

class Mapbox3dOpts(TypedDict, total=False):
    style: dict[str, Any] | str
    center: Any
    zoom: int | float
    bearing: int | float
    pitch: int | float
    altitudeScale: int | float
    shading: str
    realisticMaterial: Mapbox3d_realisticmaterialOpts
    lambertMaterial: Mapbox3d_lambertmaterialOpts
    colorMaterial: Mapbox3d_colormaterialOpts
    light: Mapbox3d_lightOpts
    postEffect: Mapbox3d_posteffectOpts
    temporalSuperSampling: Mapbox3d_temporalsupersamplingOpts

class Grid3d_axisline_linestyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Grid3d_axislineOpts(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    lineStyle: Grid3d_axisline_linestyleOpts

class Grid3d_axislabel_textstyleOpts(TypedDict, total=False):
    color: Callable[..., Any] | str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Grid3d_axislabelOpts(TypedDict, total=False):
    show: bool
    margin: int | float
    interval: Callable[..., Any] | int | float
    formatter: Callable[..., Any] | str
    textStyle: Grid3d_axislabel_textstyleOpts

class Grid3d_axistick_linestyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Grid3d_axistickOpts(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    length: int | float
    lineStyle: Grid3d_axistick_linestyleOpts

class Grid3d_splitline_linestyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Grid3d_splitlineOpts(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    lineStyle: Grid3d_splitline_linestyleOpts

class Grid3d_splitarea_areastyleOpts(TypedDict, total=False):
    color: Any

class Grid3d_splitareaOpts(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    areaStyle: Grid3d_splitarea_areastyleOpts

class Grid3d_axispointer_linestyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Grid3d_axispointer_label_textstyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Grid3d_axispointer_labelOpts(TypedDict, total=False):
    show: bool
    formatter: Callable[..., Any]
    margin: int | float
    textStyle: Grid3d_axispointer_label_textstyleOpts

class Grid3d_axispointerOpts(TypedDict, total=False):
    show: bool
    lineStyle: Grid3d_axispointer_linestyleOpts
    label: Grid3d_axispointer_labelOpts

class Grid3d_light_mainOpts(TypedDict, total=False):
    color: str
    intensity: int | float
    shadow: bool
    shadowQuality: str
    alpha: int | float
    beta: int | float

class Grid3d_light_ambientOpts(TypedDict, total=False):
    color: str
    intensity: int | float

class Grid3d_light_ambientcubemapOpts(TypedDict, total=False):
    texture: str
    diffuseIntensity: int | float
    specularIntensity: int | float

class Grid3d_lightOpts(TypedDict, total=False):
    main: Grid3d_light_mainOpts
    ambient: Grid3d_light_ambientOpts
    ambientCubemap: Grid3d_light_ambientcubemapOpts

class Grid3d_posteffect_bloomOpts(TypedDict, total=False):
    enable: bool
    bloomIntensity: int | float

class Grid3d_posteffect_depthoffieldOpts(TypedDict, total=False):
    enable: bool
    focalDistance: bool
    focalRange: bool
    fstop: int | float
    blurRadius: int | float

class Grid3d_posteffect_ssaoOpts(TypedDict, total=False):
    enable: bool
    quality: str
    radius: int | float
    intensity: int | float

class Grid3d_posteffect_colorcorrectionOpts(TypedDict, total=False):
    enable: bool
    lookupTexture: str
    exposure: int | float
    brightness: int | float
    contrast: int | float
    saturation: int | float

class Grid3d_posteffect_fxaaOpts(TypedDict, total=False):
    enable: bool

class Grid3d_posteffectOpts(TypedDict, total=False):
    enable: bool
    bloom: Grid3d_posteffect_bloomOpts
    depthOfField: Grid3d_posteffect_depthoffieldOpts
    screenSpaceAmbientOcclusion: dict[str, Any]
    SSAO: Grid3d_posteffect_ssaoOpts
    colorCorrection: Grid3d_posteffect_colorcorrectionOpts
    FXAA: Grid3d_posteffect_fxaaOpts

class Grid3d_temporalsupersamplingOpts(TypedDict, total=False):
    enable: bool

class Grid3d_viewcontrolOpts(TypedDict, total=False):
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

class Grid3dOpts(TypedDict, total=False):
    show: bool
    boxWidth: int | float
    boxHeight: int | float
    boxDepth: int | float
    axisLine: Grid3d_axislineOpts
    axisLabel: Grid3d_axislabelOpts
    axisTick: Grid3d_axistickOpts
    splitLine: Grid3d_splitlineOpts
    splitArea: Grid3d_splitareaOpts
    axisPointer: Grid3d_axispointerOpts
    environment: str
    light: Grid3d_lightOpts
    postEffect: Grid3d_posteffectOpts
    temporalSuperSampling: Grid3d_temporalsupersamplingOpts
    viewControl: Grid3d_viewcontrolOpts
    zlevel: int | float
    left: int | float | str
    top: int | float | str
    right: int | float | str
    bottom: int | float | str
    width: int | float | str
    height: int | float | str

class Xaxis3d_nametextstyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Xaxis3d_data_item_textstyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Xaxis3d_data_itemOpts(TypedDict, total=False):
    value: str
    textStyle: Xaxis3d_data_item_textstyleOpts

class Xaxis3d_axisline_linestyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Xaxis3d_axislineOpts(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    lineStyle: Xaxis3d_axisline_linestyleOpts

class Xaxis3d_axislabel_textstyleOpts(TypedDict, total=False):
    color: Callable[..., Any] | str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Xaxis3d_axislabelOpts(TypedDict, total=False):
    show: bool
    margin: int | float
    interval: Callable[..., Any] | int | float
    formatter: Callable[..., Any] | str
    textStyle: Xaxis3d_axislabel_textstyleOpts

class Xaxis3d_axistick_linestyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Xaxis3d_axistickOpts(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    length: int | float
    lineStyle: Xaxis3d_axistick_linestyleOpts

class Xaxis3d_splitline_linestyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Xaxis3d_splitlineOpts(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    lineStyle: Xaxis3d_splitline_linestyleOpts

class Xaxis3d_splitarea_areastyleOpts(TypedDict, total=False):
    color: Any

class Xaxis3d_splitareaOpts(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    areaStyle: Xaxis3d_splitarea_areastyleOpts

class Xaxis3d_axispointer_linestyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Xaxis3d_axispointer_label_textstyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Xaxis3d_axispointer_labelOpts(TypedDict, total=False):
    show: bool
    formatter: Callable[..., Any]
    margin: int | float
    textStyle: Xaxis3d_axispointer_label_textstyleOpts

class Xaxis3d_axispointerOpts(TypedDict, total=False):
    show: bool
    lineStyle: Xaxis3d_axispointer_linestyleOpts
    label: Xaxis3d_axispointer_labelOpts

class Xaxis3dOpts(TypedDict, total=False):
    show: bool
    name: str
    grid3DIndex: int | float
    nameTextStyle: Xaxis3d_nametextstyleOpts
    nameGap: int | float
    type: str
    min: str | int | float
    max: str | int | float
    scale: bool
    splitNumber: int | float
    minInterval: int | float
    interval: int | float
    logBase: int | float
    data: list[Xaxis3d_data_itemOpts]
    axisLine: Xaxis3d_axislineOpts
    axisLabel: Xaxis3d_axislabelOpts
    axisTick: Xaxis3d_axistickOpts
    splitLine: Xaxis3d_splitlineOpts
    splitArea: Xaxis3d_splitareaOpts
    axisPointer: Xaxis3d_axispointerOpts

class Yaxis3d_nametextstyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Yaxis3d_data_item_textstyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Yaxis3d_data_itemOpts(TypedDict, total=False):
    value: str
    textStyle: Yaxis3d_data_item_textstyleOpts

class Yaxis3d_axisline_linestyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Yaxis3d_axislineOpts(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    lineStyle: Yaxis3d_axisline_linestyleOpts

class Yaxis3d_axislabel_textstyleOpts(TypedDict, total=False):
    color: Callable[..., Any] | str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Yaxis3d_axislabelOpts(TypedDict, total=False):
    show: bool
    margin: int | float
    interval: Callable[..., Any] | int | float
    formatter: Callable[..., Any] | str
    textStyle: Yaxis3d_axislabel_textstyleOpts

class Yaxis3d_axistick_linestyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Yaxis3d_axistickOpts(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    length: int | float
    lineStyle: Yaxis3d_axistick_linestyleOpts

class Yaxis3d_splitline_linestyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Yaxis3d_splitlineOpts(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    lineStyle: Yaxis3d_splitline_linestyleOpts

class Yaxis3d_splitarea_areastyleOpts(TypedDict, total=False):
    color: Any

class Yaxis3d_splitareaOpts(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    areaStyle: Yaxis3d_splitarea_areastyleOpts

class Yaxis3d_axispointer_linestyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Yaxis3d_axispointer_label_textstyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Yaxis3d_axispointer_labelOpts(TypedDict, total=False):
    show: bool
    formatter: Callable[..., Any]
    margin: int | float
    textStyle: Yaxis3d_axispointer_label_textstyleOpts

class Yaxis3d_axispointerOpts(TypedDict, total=False):
    show: bool
    lineStyle: Yaxis3d_axispointer_linestyleOpts
    label: Yaxis3d_axispointer_labelOpts

class Yaxis3dOpts(TypedDict, total=False):
    show: bool
    name: str
    grid3DIndex: int | float
    nameTextStyle: Yaxis3d_nametextstyleOpts
    nameGap: int | float
    type: str
    min: str | int | float
    max: str | int | float
    scale: bool
    splitNumber: int | float
    minInterval: int | float
    interval: int | float
    logBase: int | float
    data: list[Yaxis3d_data_itemOpts]
    axisLine: Yaxis3d_axislineOpts
    axisLabel: Yaxis3d_axislabelOpts
    axisTick: Yaxis3d_axistickOpts
    splitLine: Yaxis3d_splitlineOpts
    splitArea: Yaxis3d_splitareaOpts
    axisPointer: Yaxis3d_axispointerOpts

class Zaxis3d_nametextstyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Zaxis3d_data_item_textstyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Zaxis3d_data_itemOpts(TypedDict, total=False):
    value: str
    textStyle: Zaxis3d_data_item_textstyleOpts

class Zaxis3d_axisline_linestyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Zaxis3d_axislineOpts(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    lineStyle: Zaxis3d_axisline_linestyleOpts

class Zaxis3d_axislabel_textstyleOpts(TypedDict, total=False):
    color: Callable[..., Any] | str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Zaxis3d_axislabelOpts(TypedDict, total=False):
    show: bool
    margin: int | float
    interval: Callable[..., Any] | int | float
    formatter: Callable[..., Any] | str
    textStyle: Zaxis3d_axislabel_textstyleOpts

class Zaxis3d_axistick_linestyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Zaxis3d_axistickOpts(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    length: int | float
    lineStyle: Zaxis3d_axistick_linestyleOpts

class Zaxis3d_splitline_linestyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Zaxis3d_splitlineOpts(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    lineStyle: Zaxis3d_splitline_linestyleOpts

class Zaxis3d_splitarea_areastyleOpts(TypedDict, total=False):
    color: Any

class Zaxis3d_splitareaOpts(TypedDict, total=False):
    show: bool
    interval: Callable[..., Any] | int | float
    areaStyle: Zaxis3d_splitarea_areastyleOpts

class Zaxis3d_axispointer_linestyleOpts(TypedDict, total=False):
    color: str
    opacity: int | float
    width: int | float

class Zaxis3d_axispointer_label_textstyleOpts(TypedDict, total=False):
    color: str
    borderWidth: int | float
    borderColor: str
    fontFamily: str
    fontSize: int | float
    fontWeight: str

class Zaxis3d_axispointer_labelOpts(TypedDict, total=False):
    show: bool
    formatter: Callable[..., Any]
    margin: int | float
    textStyle: Zaxis3d_axispointer_label_textstyleOpts

class Zaxis3d_axispointerOpts(TypedDict, total=False):
    show: bool
    lineStyle: Zaxis3d_axispointer_linestyleOpts
    label: Zaxis3d_axispointer_labelOpts

class Zaxis3dOpts(TypedDict, total=False):
    show: bool
    name: str
    grid3DIndex: int | float
    nameTextStyle: Zaxis3d_nametextstyleOpts
    nameGap: int | float
    type: str
    min: str | int | float
    max: str | int | float
    scale: bool
    splitNumber: int | float
    minInterval: int | float
    interval: int | float
    logBase: int | float
    data: list[Zaxis3d_data_itemOpts]
    axisLine: Zaxis3d_axislineOpts
    axisLabel: Zaxis3d_axislabelOpts
    axisTick: Zaxis3d_axistickOpts
    splitLine: Zaxis3d_splitlineOpts
    splitArea: Zaxis3d_splitareaOpts
    axisPointer: Zaxis3d_axispointerOpts

class Option(TypedDict, total=False):
    angleAxis: AngleaxisOpts
    animation: dict[str, Any]
    animationDelay: dict[str, Any]
    animationDelayUpdate: dict[str, Any]
    animationDuration: dict[str, Any]
    animationDurationUpdate: dict[str, Any]
    animationEasing: dict[str, Any]
    animationEasingUpdate: dict[str, Any]
    animationThreshold: dict[str, Any]
    aria: AriaOpts
    axisPointer: AxispointerOpts
    backgroundColor: dict[str, Any]
    blendMode: dict[str, Any]
    brush: BrushOpts
    calendar: CalendarOpts
    color: dict[str, Any]
    darkMode: dict[str, Any]
    dataZoom: dict[str, Any]
    dataset: DatasetOpts
    geo3D: Geo3dOpts
    geo: GeoOpts
    globe: GlobeOpts
    graphic: GraphicOpts
    grid3D: Grid3dOpts
    grid: GridOpts
    hoverLayerThreshold: dict[str, Any]
    legend: LegendOpts
    mapbox3D: Mapbox3dOpts
    matrix: MatrixOpts
    media: dict[str, Any]
    options: dict[str, Any]
    parallel: ParallelOpts
    parallelAxis: ParallelaxisOpts
    polar: PolarOpts
    radar: RadarOpts
    radiusAxis: RadiusaxisOpts
    richInheritPlainLabel: dict[str, Any]
    series: dict[str, Any]
    singleAxis: SingleaxisOpts
    stateAnimation: StateanimationOpts
    textStyle: TextstyleOpts
    thumbnail: ThumbnailOpts
    timeline: TimelineOpts
    title: TitleOpts
    toolbox: ToolboxOpts
    tooltip: TooltipOpts
    useUTC: dict[str, Any]
    visualMap: dict[str, Any]
    xAxis3D: Xaxis3dOpts
    xAxis: XaxisOpts
    yAxis3D: Yaxis3dOpts
    yAxis: YaxisOpts
    zAxis3D: Zaxis3dOpts