from typing import TypedDict, Any, List, Union, Literal

class AngleaxisAxislabelTextstyle(TypedDict, total=False):
    color: str
    fontSize: int | float


class AngleaxisAxislabel(TypedDict, total=False):
    formatter: Any
    inside: bool
    interval: int | float
    margin: int | float
    show: bool
    textStyle: AngleaxisAxislabelTextstyle


class AngleaxisAxislineLinestyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class AngleaxisAxisline(TypedDict, total=False):
    lineStyle: AngleaxisAxislineLinestyle
    show: bool


class AngleaxisAxistickLinestyle(TypedDict, total=False):
    color: str
    shadowColor: str
    type: Literal['solid', 'dashed', 'dotted']


class AngleaxisAxistick(TypedDict, total=False):
    inside: bool
    interval: int | float
    length: int | float
    lineStyle: AngleaxisAxistickLinestyle
    show: bool


class AngleaxisDataTextstyle(TypedDict, total=False):
    baseline: Literal['top', 'middle', 'bottom']
    color: str
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class AngleaxisData(TypedDict, total=False):
    textStyle: AngleaxisDataTextstyle
    value: Any


class AngleaxisSplitareaAreastyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class AngleaxisSplitarea(TypedDict, total=False):
    areaStyle: AngleaxisSplitareaAreastyle
    interval: int | float
    show: bool


class AngleaxisSplitlineLinestyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    type: Literal['solid', 'dashed', 'dotted']


class AngleaxisSplitline(TypedDict, total=False):
    interval: int | float
    lineStyle: AngleaxisSplitlineLinestyle
    show: bool


class Angleaxis(TypedDict, total=False):
    axisLabel: AngleaxisAxislabel
    axisLine: AngleaxisAxisline
    axisTick: AngleaxisAxistick
    boundaryGap: int | float
    clockwise: bool
    data: AngleaxisData
    interval: int | float
    max: int | float
    min: int | float
    polarIndex: int | float
    scale: bool
    splitArea: AngleaxisSplitarea
    splitLine: AngleaxisSplitline
    splitNumber: Any
    startAngle: Any
    type: Literal['value', 'category', 'time', 'log']


class Animation(TypedDict, total=False):
    pass


class Animationduration(TypedDict, total=False):
    pass


class Animationdurationupdate(TypedDict, total=False):
    pass


class Animationeasing(TypedDict, total=False):
    pass


class Animationeasingupdate(TypedDict, total=False):
    pass


class Backgroundcolor(TypedDict, total=False):
    pass


Color = list[str]


class Datazoom(TypedDict, total=False):
    pass


class DatazoomInside(TypedDict, total=False):
    angleAxisIndex: int | float
    end: Any
    endValue: Any
    filterMode: Literal['filter', 'weakFilter', 'empty', 'none']
    orient: Literal['horizontal', 'vertical']
    radiusAxisIndex: int | float
    start: Any
    startValue: Any
    throttle: Any
    type: Literal['inside']
    xAxisIndex: int | float
    yAxisIndex: int | float
    zoomLock: int | float


class DatazoomSliderTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class DatazoomSlider(TypedDict, total=False):
    angleAxisIndex: int | float
    backgroundColor: str
    bottom: Any
    dataBackgroundColor: str
    end: Any
    endValue: Any
    fillerColor: str
    filterMode: Literal['filter', 'weakFilter', 'empty', 'none']
    handleColor: str
    handleSize: int | float
    labelFormatter: Any
    labelPrecision: int | float
    left: Any
    orient: Literal['horizontal', 'vertical']
    radiusAxisIndex: int | float
    realtime: bool
    right: Any
    show: bool
    showDataShadow: bool
    showDetail: bool
    start: Any
    startValue: Any
    textStyle: DatazoomSliderTextstyle
    throttle: Any
    top: Any
    type: Literal['slider']
    xAxisIndex: int | float
    yAxisIndex: int | float
    z: int | float
    zlevel: int | float
    zoomLock: int | float


class GeoItemstyleEmphasis(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class GeoItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class GeoItemstyle(TypedDict, total=False):
    bottom: Any
    emphasis: GeoItemstyleEmphasis
    left: Any
    normal: GeoItemstyleNormal
    right: Any
    top: Any
    z: int | float
    zlevel: int | float


class GeoLabelEmphasisTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class GeoLabelEmphasis(TypedDict, total=False):
    show: bool
    textStyle: GeoLabelEmphasisTextstyle


class GeoLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class GeoLabelNormal(TypedDict, total=False):
    show: bool
    textStyle: GeoLabelNormalTextstyle


class GeoLabel(TypedDict, total=False):
    emphasis: GeoLabelEmphasis
    normal: GeoLabelNormal


class Geo(TypedDict, total=False):
    bottom: Any
    itemStyle: GeoItemstyle
    label: GeoLabel
    left: Any
    map: str
    right: Any
    roam: bool
    show: bool
    top: Any
    z: int | float
    zlevel: int | float


class Grid(TypedDict, total=False):
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    bottom: Any
    containLabel: bool
    height: int | float
    left: Any
    right: Any
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    show: bool
    top: Any
    width: int | float
    z: int | float
    zlevel: int | float


class LegendData(TypedDict, total=False):
    icon: Any
    name: str
    textStyle: Any


class LegendTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class Legend(TypedDict, total=False):
    align: Literal['left', 'center', 'right', 'auto']
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    bottom: Any
    data: LegendData
    formatter: Any
    height: int | float
    itemGap: int | float
    itemHeight: int | float
    itemWidth: int | float
    left: Any
    orient: Literal['horizontal', 'vertical']
    padding: Any
    right: Any
    selected: Any
    selectedMode: Literal['multiple', 'single', 'series'] | bool
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    show: bool
    textStyle: LegendTextstyle
    top: Any
    width: int | float
    z: int | float
    zlevel: int | float


class ParallelParallelaxisdefaultAxislabelTextstyle(TypedDict, total=False):
    color: str
    fontStyle: Literal['normal', 'italic', 'oblique']


class ParallelParallelaxisdefaultAxislabel(TypedDict, total=False):
    formatter: Any
    inside: bool
    margin: int | float
    rotate: int | float
    show: bool
    textStyle: ParallelParallelaxisdefaultAxislabelTextstyle


class ParallelParallelaxisdefaultAxislineLinestyle(TypedDict, total=False):
    color: str
    shadowBlur: int | float
    type: Literal['solid', 'dashed', 'dotted']


class ParallelParallelaxisdefaultAxisline(TypedDict, total=False):
    lineStyle: ParallelParallelaxisdefaultAxislineLinestyle
    show: bool


class ParallelParallelaxisdefaultAxistickLinestyle(TypedDict, total=False):
    color: str
    type: Literal['solid', 'dashed', 'dotted']


class ParallelParallelaxisdefaultAxistick(TypedDict, total=False):
    inside: bool
    interval: int | float
    length: int | float
    lineStyle: ParallelParallelaxisdefaultAxistickLinestyle
    show: bool


class ParallelParallelaxisdefaultDataTextstyle(TypedDict, total=False):
    align: Literal['left', 'center', 'right', 'auto']
    baseline: Literal['top', 'middle', 'bottom']
    color: str
    fontStyle: Literal['normal', 'italic', 'oblique']


class ParallelParallelaxisdefaultData(TypedDict, total=False):
    textStyle: ParallelParallelaxisdefaultDataTextstyle
    value: Any


class ParallelParallelaxisdefaultNametextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']


class ParallelParallelaxisdefault(TypedDict, total=False):
    axisLabel: ParallelParallelaxisdefaultAxislabel
    axisLine: ParallelParallelaxisdefaultAxisline
    axisTick: ParallelParallelaxisdefaultAxistick
    boundaryGap: int | float
    data: ParallelParallelaxisdefaultData
    interval: int | float
    inverse: bool
    max: int | float
    min: int | float
    name: str
    nameGap: int | float
    nameLocation: Literal['start', 'middle', 'end']
    nameTextStyle: ParallelParallelaxisdefaultNametextstyle
    scale: bool
    splitNumber: Any
    type: Literal['value', 'category', 'time', 'log']


class Parallel(TypedDict, total=False):
    bottom: Any
    height: int | float
    layout: Literal['horizontal', 'vertical']
    left: Any
    parallelAxisDefault: ParallelParallelaxisdefault
    right: Any
    top: Any
    width: int | float
    z: int | float
    zlevel: int | float


class ParallelaxisAreaselectstyle(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    width: int | float


class ParallelaxisAxislabelTextstyle(TypedDict, total=False):
    color: str
    fontSize: int | float


class ParallelaxisAxislabel(TypedDict, total=False):
    formatter: Any
    inside: bool
    interval: int | float
    margin: int | float
    rotate: int | float
    show: bool
    textStyle: ParallelaxisAxislabelTextstyle


class ParallelaxisAxislineLinestyle(TypedDict, total=False):
    color: str


class ParallelaxisAxisline(TypedDict, total=False):
    lineStyle: ParallelaxisAxislineLinestyle
    show: bool


class ParallelaxisAxistickLinestyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class ParallelaxisAxistick(TypedDict, total=False):
    inside: bool
    interval: int | float
    lineStyle: ParallelaxisAxistickLinestyle


class ParallelaxisDataTextstyle(TypedDict, total=False):
    align: Literal['left', 'center', 'right', 'auto']
    baseline: Literal['top', 'middle', 'bottom']
    color: str


class ParallelaxisData(TypedDict, total=False):
    textStyle: ParallelaxisDataTextstyle
    value: Any


class ParallelaxisNametextstyle(TypedDict, total=False):
    color: str


class Parallelaxis(TypedDict, total=False):
    areaSelectStyle: ParallelaxisAreaselectstyle
    axisLabel: ParallelaxisAxislabel
    axisLine: ParallelaxisAxisline
    axisTick: ParallelaxisAxistick
    boundaryGap: int | float
    data: ParallelaxisData
    dim: Any
    interval: int | float
    inverse: bool
    max: int | float
    min: int | float
    name: str
    nameGap: int | float
    nameLocation: Literal['start', 'middle', 'end']
    nameTextStyle: ParallelaxisNametextstyle
    parallelIndex: int | float
    scale: bool
    splitNumber: Any
    type: Literal['value', 'category', 'time', 'log']


class Polar(TypedDict, total=False):
    center: list | dict
    radius: list | dict
    z: int | float
    zlevel: int | float


class RadiusaxisAxislabelTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class RadiusaxisAxislabel(TypedDict, total=False):
    formatter: Any
    inside: bool
    interval: int | float
    margin: int | float
    rotate: int | float
    show: bool
    textStyle: RadiusaxisAxislabelTextstyle


class RadiusaxisAxislineLinestyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class RadiusaxisAxisline(TypedDict, total=False):
    lineStyle: RadiusaxisAxislineLinestyle
    show: bool


class RadiusaxisAxistickLinestyle(TypedDict, total=False):
    color: str
    type: Literal['solid', 'dashed', 'dotted']


class RadiusaxisAxistick(TypedDict, total=False):
    inside: bool
    interval: int | float
    length: int | float
    lineStyle: RadiusaxisAxistickLinestyle
    show: bool


class RadiusaxisDataTextstyle(TypedDict, total=False):
    baseline: Literal['top', 'middle', 'bottom']
    color: str


class RadiusaxisData(TypedDict, total=False):
    textStyle: RadiusaxisDataTextstyle
    value: Any


class RadiusaxisNametextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class RadiusaxisSplitareaAreastyle(TypedDict, total=False):
    color: str
    shadowColor: str


class RadiusaxisSplitarea(TypedDict, total=False):
    areaStyle: RadiusaxisSplitareaAreastyle
    interval: int | float
    show: bool


class RadiusaxisSplitlineLinestyle(TypedDict, total=False):
    color: str
    shadowBlur: int | float
    shadowColor: str
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class RadiusaxisSplitline(TypedDict, total=False):
    interval: int | float
    lineStyle: RadiusaxisSplitlineLinestyle
    show: bool


class Radiusaxis(TypedDict, total=False):
    axisLabel: RadiusaxisAxislabel
    axisLine: RadiusaxisAxisline
    axisTick: RadiusaxisAxistick
    boundaryGap: int | float
    data: RadiusaxisData
    interval: int | float
    inverse: bool
    max: int | float
    min: int | float
    name: str
    nameGap: int | float
    nameLocation: Literal['start', 'middle', 'end']
    nameTextStyle: RadiusaxisNametextstyle
    polarIndex: int | float
    scale: bool
    splitArea: RadiusaxisSplitarea
    splitLine: RadiusaxisSplitline
    splitNumber: Any
    type: Literal['value', 'category', 'time', 'log']


class Series(TypedDict, total=False):
    pass


class SeriesBarDataItemstyleEmphasis(TypedDict, total=False):
    barBorderColor: str
    barBorderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesBarDataItemstyleNormal(TypedDict, total=False):
    barBorderColor: str
    barBorderRadius: list | dict
    barBorderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesBarDataItemstyle(TypedDict, total=False):
    emphasis: SeriesBarDataItemstyleEmphasis
    normal: SeriesBarDataItemstyleNormal


class SeriesBarDataLabelEmphasisTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesBarDataLabelEmphasis(TypedDict, total=False):
    position: str
    show: bool
    textStyle: SeriesBarDataLabelEmphasisTextstyle


class SeriesBarDataLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesBarDataLabelNormal(TypedDict, total=False):
    position: str
    show: bool
    textStyle: SeriesBarDataLabelNormalTextstyle


class SeriesBarDataLabel(TypedDict, total=False):
    emphasis: SeriesBarDataLabelEmphasis
    normal: SeriesBarDataLabelNormal


class SeriesBarData(TypedDict, total=False):
    itemStyle: SeriesBarDataItemstyle
    label: SeriesBarDataLabel
    value: Any


class SeriesBarItemstyleEmphasis(TypedDict, total=False):
    barBorderColor: str
    barBorderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesBarItemstyleNormal(TypedDict, total=False):
    barBorderColor: str
    barBorderRadius: list | dict
    barBorderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesBarItemstyle(TypedDict, total=False):
    emphasis: SeriesBarItemstyleEmphasis
    normal: SeriesBarItemstyleNormal


class SeriesBarLabelEmphasisTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesBarLabelEmphasis(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesBarLabelEmphasisTextstyle


class SeriesBarLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesBarLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesBarLabelNormalTextstyle


class SeriesBarLabel(TypedDict, total=False):
    emphasis: SeriesBarLabelEmphasis
    normal: SeriesBarLabelNormal


class SeriesBarMarklineDataItemLabelEmphasis(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool


class SeriesBarMarklineDataItemLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool


class SeriesBarMarklineDataItemLabel(TypedDict, total=False):
    emphasis: SeriesBarMarklineDataItemLabelEmphasis
    normal: SeriesBarMarklineDataItemLabelNormal


class SeriesBarMarklineDataItemLinestyleEmphasis(TypedDict, total=False):
    color: str
    shadowBlur: int | float


class SeriesBarMarklineDataItemLinestyleNormal(TypedDict, total=False):
    color: str
    curveness: int | float
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesBarMarklineDataItemLinestyle(TypedDict, total=False):
    emphasis: SeriesBarMarklineDataItemLinestyleEmphasis
    normal: SeriesBarMarklineDataItemLinestyleNormal


class SeriesBarMarklineDataItem(TypedDict, total=False):
    coord: str
    label: SeriesBarMarklineDataItemLabel
    lineStyle: SeriesBarMarklineDataItemLinestyle
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    type: Literal['min', 'max', 'average']
    value: Any
    valueDim: Any
    valueIndex: int | float
    x: Any
    y: Any


class SeriesBarMarklineLabelEmphasis(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool


class SeriesBarMarklineLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool


class SeriesBarMarklineLabel(TypedDict, total=False):
    emphasis: SeriesBarMarklineLabelEmphasis
    normal: SeriesBarMarklineLabelNormal


class SeriesBarMarklineLinestyleEmphasis(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesBarMarklineLinestyleNormal(TypedDict, total=False):
    color: str
    curveness: int | float
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesBarMarklineLinestyle(TypedDict, total=False):
    emphasis: SeriesBarMarklineLinestyleEmphasis
    normal: SeriesBarMarklineLinestyleNormal


class SeriesBarMarkline(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    data: List[SeriesBarMarklineDataItem]
    label: SeriesBarMarklineLabel
    lineStyle: SeriesBarMarklineLinestyle
    precision: int | float
    symbol: str
    symbolSize: int | float


class SeriesBarMarkpointDataItemstyleEmphasis(TypedDict, total=False):
    color: str
    shadowBlur: int | float
    shadowOffsetX: int | float


class SeriesBarMarkpointDataItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float


class SeriesBarMarkpointDataItemstyle(TypedDict, total=False):
    emphasis: SeriesBarMarkpointDataItemstyleEmphasis
    normal: SeriesBarMarkpointDataItemstyleNormal


class SeriesBarMarkpointDataLabelEmphasisTextstyle(TypedDict, total=False):
    color: str


class SeriesBarMarkpointDataLabelEmphasis(TypedDict, total=False):
    position: str
    show: bool
    textStyle: SeriesBarMarkpointDataLabelEmphasisTextstyle


class SeriesBarMarkpointDataLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']


class SeriesBarMarkpointDataLabelNormal(TypedDict, total=False):
    position: str
    show: bool
    textStyle: SeriesBarMarkpointDataLabelNormalTextstyle


class SeriesBarMarkpointDataLabel(TypedDict, total=False):
    emphasis: SeriesBarMarkpointDataLabelEmphasis
    normal: SeriesBarMarkpointDataLabelNormal


class SeriesBarMarkpointData(TypedDict, total=False):
    coord: str
    itemStyle: SeriesBarMarkpointDataItemstyle
    label: SeriesBarMarkpointDataLabel
    name: str
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    type: Literal['min', 'max', 'average']
    value: Any
    valueDim: Any
    valueIndex: int | float
    x: Any
    y: Any


class SeriesBarMarkpointItemstyleEmphasis(TypedDict, total=False):
    color: str
    shadowBlur: int | float


class SeriesBarMarkpointItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesBarMarkpointItemstyle(TypedDict, total=False):
    emphasis: SeriesBarMarkpointItemstyleEmphasis
    normal: SeriesBarMarkpointItemstyleNormal


class SeriesBarMarkpointLabelEmphasisTextstyle(TypedDict, total=False):
    color: str
    fontSize: int | float


class SeriesBarMarkpointLabelEmphasis(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesBarMarkpointLabelEmphasisTextstyle


class SeriesBarMarkpointLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontSize: int | float


class SeriesBarMarkpointLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesBarMarkpointLabelNormalTextstyle


class SeriesBarMarkpointLabel(TypedDict, total=False):
    emphasis: SeriesBarMarkpointLabelEmphasis
    normal: SeriesBarMarkpointLabelNormal


class SeriesBarMarkpoint(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    data: SeriesBarMarkpointData
    itemStyle: SeriesBarMarkpointItemstyle
    label: SeriesBarMarkpointLabel
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float


class SeriesBar(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    barCategoryGap: int | float
    barGap: int | float
    barMaxWidth: int | float
    barMinHeight: int | float
    barWidth: int | float
    coordinateSystem: str
    data: SeriesBarData
    itemStyle: SeriesBarItemstyle
    label: SeriesBarLabel
    legendHoverLink: Any
    markLine: SeriesBarMarkline
    markPoint: SeriesBarMarkpoint
    name: str
    stack: str
    type: Literal['bar']
    xAxisIndex: int | float
    yAxisIndex: int | float
    z: int | float
    zlevel: int | float


class SeriesBoxplotDataItemstyle(TypedDict, total=False):
    shadowBlur: int | float


class SeriesBoxplotData(TypedDict, total=False):
    itemStyle: SeriesBoxplotDataItemstyle
    name: str
    value: Any


class SeriesBoxplotItemstyleEmphasis(TypedDict, total=False):
    color: str
    shadowOffsetX: int | float


class SeriesBoxplotItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesBoxplotItemstyle(TypedDict, total=False):
    emphasis: SeriesBoxplotItemstyleEmphasis
    normal: SeriesBoxplotItemstyleNormal


class SeriesBoxplotMarklineDataItemLabelEmphasis(TypedDict, total=False):
    formatter: Any


class SeriesBoxplotMarklineDataItemLabelNormal(TypedDict, total=False):
    position: str


class SeriesBoxplotMarklineDataItemLabel(TypedDict, total=False):
    emphasis: SeriesBoxplotMarklineDataItemLabelEmphasis
    normal: SeriesBoxplotMarklineDataItemLabelNormal


class SeriesBoxplotMarklineDataItem(TypedDict, total=False):
    label: SeriesBoxplotMarklineDataItemLabel


class SeriesBoxplotMarklineLabelEmphasis(TypedDict, total=False):
    formatter: Any


class SeriesBoxplotMarklineLabelNormal(TypedDict, total=False):
    position: str


class SeriesBoxplotMarklineLabel(TypedDict, total=False):
    emphasis: SeriesBoxplotMarklineLabelEmphasis
    normal: SeriesBoxplotMarklineLabelNormal


class SeriesBoxplotMarklineLinestyleNormal(TypedDict, total=False):
    curveness: int | float
    type: Literal['solid', 'dashed', 'dotted']


class SeriesBoxplotMarklineLinestyle(TypedDict, total=False):
    normal: SeriesBoxplotMarklineLinestyleNormal


class SeriesBoxplotMarkline(TypedDict, total=False):
    data: List[SeriesBoxplotMarklineDataItem]
    label: SeriesBoxplotMarklineLabel
    lineStyle: SeriesBoxplotMarklineLinestyle
    symbol: str
    symbolSize: int | float


class SeriesBoxplotMarkpointDataLabelNormal(TypedDict, total=False):
    position: str


class SeriesBoxplotMarkpointDataLabel(TypedDict, total=False):
    normal: SeriesBoxplotMarkpointDataLabelNormal


class SeriesBoxplotMarkpointData(TypedDict, total=False):
    coord: str
    label: SeriesBoxplotMarkpointDataLabel
    valueDim: Any
    valueIndex: int | float


class SeriesBoxplotMarkpointLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontStyle: Literal['normal', 'italic', 'oblique']


class SeriesBoxplotMarkpointLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesBoxplotMarkpointLabelNormalTextstyle


class SeriesBoxplotMarkpointLabel(TypedDict, total=False):
    normal: SeriesBoxplotMarkpointLabelNormal


class SeriesBoxplotMarkpoint(TypedDict, total=False):
    data: SeriesBoxplotMarkpointData
    label: SeriesBoxplotMarkpointLabel
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float


class SeriesBoxplot(TypedDict, total=False):
    animationDuration: bool
    animationEasing: str
    boxWidth: int | float
    coordinateSystem: str
    data: SeriesBoxplotData
    hoverAnimation: bool
    itemStyle: SeriesBoxplotItemstyle
    layout: Any
    legendHoverLink: Any
    markLine: SeriesBoxplotMarkline
    markPoint: SeriesBoxplotMarkpoint
    name: str
    type: Literal['boxplot']
    xAxisIndex: int | float
    yAxisIndex: int | float
    z: int | float


class SeriesCandlestickDataItemstyle(TypedDict, total=False):
    borderColor: str
    borderColor0: str
    borderWidth: int | float
    color: str
    color0: str
    emphasis: Any
    normal: Any
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesCandlestickData(TypedDict, total=False):
    itemStyle: SeriesCandlestickDataItemstyle
    name: str
    value: Any


class SeriesCandlestickItemstyleEmphasis(TypedDict, total=False):
    borderColor: str
    color: str
    color0: str


class SeriesCandlestickItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderColor0: str
    borderWidth: int | float
    color: str
    color0: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesCandlestickItemstyle(TypedDict, total=False):
    emphasis: SeriesCandlestickItemstyleEmphasis
    normal: SeriesCandlestickItemstyleNormal


class SeriesCandlestickMarklineDataItemLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str


class SeriesCandlestickMarklineDataItemLabel(TypedDict, total=False):
    normal: SeriesCandlestickMarklineDataItemLabelNormal


class SeriesCandlestickMarklineDataItem(TypedDict, total=False):
    coord: str
    label: SeriesCandlestickMarklineDataItemLabel
    lineStyle: Any
    symbol: str
    value: Any
    valueDim: Any
    valueIndex: int | float
    x: Any
    y: Any


class SeriesCandlestickMarklineLabelEmphasis(TypedDict, total=False):
    formatter: Any


class SeriesCandlestickMarklineLabelNormal(TypedDict, total=False):
    position: str
    show: bool


class SeriesCandlestickMarklineLabel(TypedDict, total=False):
    emphasis: SeriesCandlestickMarklineLabelEmphasis
    normal: SeriesCandlestickMarklineLabelNormal


class SeriesCandlestickMarklineLinestyleNormal(TypedDict, total=False):
    type: Literal['solid', 'dashed', 'dotted']


class SeriesCandlestickMarklineLinestyle(TypedDict, total=False):
    normal: SeriesCandlestickMarklineLinestyleNormal


class SeriesCandlestickMarkline(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationEasingUpdate: str
    data: List[SeriesCandlestickMarklineDataItem]
    label: SeriesCandlestickMarklineLabel
    lineStyle: SeriesCandlestickMarklineLinestyle
    precision: int | float
    symbol: str
    symbolSize: int | float


class SeriesCandlestickMarkpointDataItemstyle(TypedDict, total=False):
    normal: Any


class SeriesCandlestickMarkpointDataLabelNormal(TypedDict, total=False):
    position: str
    show: bool
    textStyle: Any


class SeriesCandlestickMarkpointDataLabel(TypedDict, total=False):
    normal: SeriesCandlestickMarkpointDataLabelNormal


class SeriesCandlestickMarkpointData(TypedDict, total=False):
    coord: str
    itemStyle: SeriesCandlestickMarkpointDataItemstyle
    label: SeriesCandlestickMarkpointDataLabel
    name: str
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    value: Any
    valueIndex: int | float
    x: Any
    y: Any


class SeriesCandlestickMarkpointItemstyleNormal(TypedDict, total=False):
    color: str


class SeriesCandlestickMarkpointItemstyle(TypedDict, total=False):
    emphasis: Any
    normal: SeriesCandlestickMarkpointItemstyleNormal


class SeriesCandlestickMarkpointLabelEmphasis(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: Any


class SeriesCandlestickMarkpointLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontSize: int | float
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesCandlestickMarkpointLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesCandlestickMarkpointLabelNormalTextstyle


class SeriesCandlestickMarkpointLabel(TypedDict, total=False):
    emphasis: SeriesCandlestickMarkpointLabelEmphasis
    normal: SeriesCandlestickMarkpointLabelNormal


class SeriesCandlestickMarkpoint(TypedDict, total=False):
    animation: bool
    animationDurationUpdate: bool
    data: SeriesCandlestickMarkpointData
    itemStyle: SeriesCandlestickMarkpointItemstyle
    label: SeriesCandlestickMarkpointLabel
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float


class SeriesCandlestick(TypedDict, total=False):
    animationDuration: bool
    animationEasing: str
    coordinateSystem: str
    data: SeriesCandlestickData
    hoverAnimation: bool
    itemStyle: SeriesCandlestickItemstyle
    layout: Any
    legendHoverLink: Any
    markLine: SeriesCandlestickMarkline
    markPoint: SeriesCandlestickMarkpoint
    name: str
    type: Literal['candlestick']
    xAxisIndex: int | float
    yAxisIndex: int | float
    z: int | float
    zlevel: int | float


class SeriesEffectscatterDataItemstyleEmphasis(TypedDict, total=False):
    color: str
    opacity: int | float


class SeriesEffectscatterDataItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesEffectscatterDataItemstyle(TypedDict, total=False):
    emphasis: SeriesEffectscatterDataItemstyleEmphasis
    normal: SeriesEffectscatterDataItemstyleNormal


class SeriesEffectscatterDataLabelEmphasis(TypedDict, total=False):
    show: bool


class SeriesEffectscatterDataLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']


class SeriesEffectscatterDataLabelNormal(TypedDict, total=False):
    position: str
    show: bool
    textStyle: SeriesEffectscatterDataLabelNormalTextstyle


class SeriesEffectscatterDataLabel(TypedDict, total=False):
    emphasis: SeriesEffectscatterDataLabelEmphasis
    normal: SeriesEffectscatterDataLabelNormal


class SeriesEffectscatterData(TypedDict, total=False):
    itemStyle: SeriesEffectscatterDataItemstyle
    label: SeriesEffectscatterDataLabel
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float


class SeriesEffectscatterItemstyleEmphasis(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    opacity: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesEffectscatterItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesEffectscatterItemstyle(TypedDict, total=False):
    emphasis: SeriesEffectscatterItemstyleEmphasis
    normal: SeriesEffectscatterItemstyleNormal


class SeriesEffectscatterLabelEmphasis(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool


class SeriesEffectscatterLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesEffectscatterLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesEffectscatterLabelNormalTextstyle


class SeriesEffectscatterLabel(TypedDict, total=False):
    emphasis: SeriesEffectscatterLabelEmphasis
    normal: SeriesEffectscatterLabelNormal


class SeriesEffectscatterMarklineDataItem(TypedDict, total=False):
    symbol: str
    symbolSize: int | float


class SeriesEffectscatterMarklineLabelEmphasis(TypedDict, total=False):
    formatter: Any


class SeriesEffectscatterMarklineLabel(TypedDict, total=False):
    emphasis: SeriesEffectscatterMarklineLabelEmphasis


class SeriesEffectscatterMarklineLinestyleNormal(TypedDict, total=False):
    curveness: int | float
    width: int | float


class SeriesEffectscatterMarklineLinestyle(TypedDict, total=False):
    normal: SeriesEffectscatterMarklineLinestyleNormal


class SeriesEffectscatterMarkline(TypedDict, total=False):
    data: List[SeriesEffectscatterMarklineDataItem]
    label: SeriesEffectscatterMarklineLabel
    lineStyle: SeriesEffectscatterMarklineLinestyle
    precision: int | float
    symbol: str
    symbolSize: int | float


class SeriesEffectscatterMarkpointDataLabelEmphasis(TypedDict, total=False):
    show: bool
    textStyle: Any


class SeriesEffectscatterMarkpointDataLabel(TypedDict, total=False):
    emphasis: SeriesEffectscatterMarkpointDataLabelEmphasis


class SeriesEffectscatterMarkpointData(TypedDict, total=False):
    coord: str
    label: SeriesEffectscatterMarkpointDataLabel
    name: str
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    type: Literal['min', 'max', 'average']
    value: Any
    valueIndex: int | float
    x: Any
    y: Any


class SeriesEffectscatterMarkpointItemstyleNormal(TypedDict, total=False):
    borderWidth: int | float


class SeriesEffectscatterMarkpointItemstyle(TypedDict, total=False):
    emphasis: Any
    normal: SeriesEffectscatterMarkpointItemstyleNormal


class SeriesEffectscatterMarkpointLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool


class SeriesEffectscatterMarkpointLabel(TypedDict, total=False):
    emphasis: Any
    normal: SeriesEffectscatterMarkpointLabelNormal


class SeriesEffectscatterMarkpoint(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    data: SeriesEffectscatterMarkpointData
    itemStyle: SeriesEffectscatterMarkpointItemstyle
    label: SeriesEffectscatterMarkpointLabel
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float


class SeriesEffectscatterRippleeffect(TypedDict, total=False):
    brushType: Literal['fill', 'stroke']
    period: int | float
    scale: bool


class SeriesEffectscatter(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    coordinateSystem: str
    data: SeriesEffectscatterData
    effectType: Literal['ripple']
    geoIndex: int | float
    itemStyle: SeriesEffectscatterItemstyle
    label: SeriesEffectscatterLabel
    legendHoverLink: Any
    markLine: SeriesEffectscatterMarkline
    markPoint: SeriesEffectscatterMarkpoint
    name: str
    polarIndex: int | float
    rippleEffect: SeriesEffectscatterRippleeffect
    showEffectOn: bool
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    type: Literal['effectScatter']
    xAxisIndex: int | float
    yAxisIndex: int | float
    z: int | float
    zlevel: int | float


class SeriesFunnelDataItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str


class SeriesFunnelDataItemstyle(TypedDict, total=False):
    normal: SeriesFunnelDataItemstyleNormal


class SeriesFunnelDataLabelEmphasis(TypedDict, total=False):
    show: bool


class SeriesFunnelDataLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesFunnelDataLabelNormal(TypedDict, total=False):
    position: str
    show: bool
    textStyle: SeriesFunnelDataLabelNormalTextstyle


class SeriesFunnelDataLabel(TypedDict, total=False):
    emphasis: SeriesFunnelDataLabelEmphasis
    normal: SeriesFunnelDataLabelNormal


class SeriesFunnelDataLabellineNormalLinestyle(TypedDict, total=False):
    opacity: int | float
    width: int | float


class SeriesFunnelDataLabellineNormal(TypedDict, total=False):
    length: int | float
    lineStyle: SeriesFunnelDataLabellineNormalLinestyle
    show: bool


class SeriesFunnelDataLabelline(TypedDict, total=False):
    normal: SeriesFunnelDataLabellineNormal


class SeriesFunnelData(TypedDict, total=False):
    itemStyle: SeriesFunnelDataItemstyle
    label: SeriesFunnelDataLabel
    labelLine: SeriesFunnelDataLabelline
    name: str
    value: Any


class SeriesFunnelItemstyleEmphasis(TypedDict, total=False):
    color: str
    opacity: int | float


class SeriesFunnelItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesFunnelItemstyle(TypedDict, total=False):
    emphasis: SeriesFunnelItemstyleEmphasis
    normal: SeriesFunnelItemstyleNormal


class SeriesFunnelLabelEmphasis(TypedDict, total=False):
    formatter: Any
    show: bool


class SeriesFunnelLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']


class SeriesFunnelLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesFunnelLabelNormalTextstyle


class SeriesFunnelLabel(TypedDict, total=False):
    emphasis: SeriesFunnelLabelEmphasis
    normal: SeriesFunnelLabelNormal


class SeriesFunnelLabellineEmphasis(TypedDict, total=False):
    show: bool


class SeriesFunnelLabellineNormalLinestyle(TypedDict, total=False):
    color: str
    shadowBlur: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesFunnelLabellineNormal(TypedDict, total=False):
    length: int | float
    lineStyle: SeriesFunnelLabellineNormalLinestyle
    show: bool


class SeriesFunnelLabelline(TypedDict, total=False):
    emphasis: SeriesFunnelLabellineEmphasis
    normal: SeriesFunnelLabellineNormal


class SeriesFunnelMarklineDataItemLabelEmphasis(TypedDict, total=False):
    formatter: Any


class SeriesFunnelMarklineDataItemLabel(TypedDict, total=False):
    emphasis: SeriesFunnelMarklineDataItemLabelEmphasis


class SeriesFunnelMarklineDataItem(TypedDict, total=False):
    label: SeriesFunnelMarklineDataItemLabel
    symbol: str
    x: Any


class SeriesFunnelMarkline(TypedDict, total=False):
    data: List[SeriesFunnelMarklineDataItem]
    label: Any
    symbol: str
    symbolSize: int | float


class SeriesFunnelMarkpointData(TypedDict, total=False):
    itemStyle: Any
    symbol: str
    symbolRotate: int | float


class SeriesFunnelMarkpointItemstyleNormal(TypedDict, total=False):
    color: str


class SeriesFunnelMarkpointItemstyle(TypedDict, total=False):
    normal: SeriesFunnelMarkpointItemstyleNormal


class SeriesFunnelMarkpointLabelNormal(TypedDict, total=False):
    position: str


class SeriesFunnelMarkpointLabel(TypedDict, total=False):
    normal: SeriesFunnelMarkpointLabelNormal


class SeriesFunnelMarkpoint(TypedDict, total=False):
    data: SeriesFunnelMarkpointData
    itemStyle: SeriesFunnelMarkpointItemstyle
    label: SeriesFunnelMarkpointLabel
    symbol: str
    symbolRotate: int | float


class SeriesFunnel(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    data: SeriesFunnelData
    funnelAlign: Literal['left', 'right', 'center']
    gap: int | float
    itemStyle: SeriesFunnelItemstyle
    label: SeriesFunnelLabel
    labelLine: SeriesFunnelLabelline
    legendHoverLink: Any
    markLine: SeriesFunnelMarkline
    markPoint: SeriesFunnelMarkpoint
    max: int | float
    maxSize: int | float
    min: int | float
    minSize: int | float
    name: str
    sort: str
    type: Literal['funnel']


class SeriesGaugeAxislabelTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesGaugeAxislabel(TypedDict, total=False):
    color: str
    formatter: Any
    show: bool
    textStyle: SeriesGaugeAxislabelTextstyle


class SeriesGaugeAxislineLinestyleWidth(TypedDict, total=False):
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesGaugeAxislineLinestyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    width: SeriesGaugeAxislineLinestyleWidth


class SeriesGaugeAxisline(TypedDict, total=False):
    lineStyle: SeriesGaugeAxislineLinestyle
    show: bool


class SeriesGaugeAxistickLinestyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesGaugeAxistick(TypedDict, total=False):
    length: int | float
    lineStyle: SeriesGaugeAxistickLinestyle
    show: bool
    splitNumber: Any


class SeriesGaugeDetailTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesGaugeDetail(TypedDict, total=False):
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    height: int | float
    offsetCenter: int | float
    show: bool
    textStyle: SeriesGaugeDetailTextstyle
    width: int | float


class SeriesGaugeItemstyleEmphasis(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesGaugeItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesGaugeItemstyle(TypedDict, total=False):
    emphasis: SeriesGaugeItemstyleEmphasis
    normal: SeriesGaugeItemstyleNormal


class SeriesGaugeMarklineDataItemLabelEmphasis(TypedDict, total=False):
    formatter: Any


class SeriesGaugeMarklineDataItemLabelNormal(TypedDict, total=False):
    formatter: Any


class SeriesGaugeMarklineDataItemLabel(TypedDict, total=False):
    emphasis: SeriesGaugeMarklineDataItemLabelEmphasis
    normal: SeriesGaugeMarklineDataItemLabelNormal


class SeriesGaugeMarklineDataItemLinestyleNormal(TypedDict, total=False):
    color: str


class SeriesGaugeMarklineDataItemLinestyle(TypedDict, total=False):
    normal: SeriesGaugeMarklineDataItemLinestyleNormal


class SeriesGaugeMarklineDataItem(TypedDict, total=False):
    label: SeriesGaugeMarklineDataItemLabel
    lineStyle: SeriesGaugeMarklineDataItemLinestyle
    value: Any
    y: Any


class SeriesGaugeMarklineLabelEmphasis(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool


class SeriesGaugeMarklineLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str


class SeriesGaugeMarklineLabel(TypedDict, total=False):
    emphasis: SeriesGaugeMarklineLabelEmphasis
    normal: SeriesGaugeMarklineLabelNormal


class SeriesGaugeMarklineLinestyleNormal(TypedDict, total=False):
    color: str


class SeriesGaugeMarklineLinestyle(TypedDict, total=False):
    emphasis: Any
    normal: SeriesGaugeMarklineLinestyleNormal


class SeriesGaugeMarkline(TypedDict, total=False):
    data: List[SeriesGaugeMarklineDataItem]
    label: SeriesGaugeMarklineLabel
    lineStyle: SeriesGaugeMarklineLinestyle
    precision: int | float
    symbol: str
    symbolSize: int | float


class SeriesGaugeMarkpointDataItemstyleEmphasis(TypedDict, total=False):
    borderWidth: int | float


class SeriesGaugeMarkpointDataItemstyle(TypedDict, total=False):
    emphasis: SeriesGaugeMarkpointDataItemstyleEmphasis
    normal: Any


class SeriesGaugeMarkpointDataLabelNormal(TypedDict, total=False):
    position: str


class SeriesGaugeMarkpointDataLabel(TypedDict, total=False):
    emphasis: Any
    normal: SeriesGaugeMarkpointDataLabelNormal


class SeriesGaugeMarkpointData(TypedDict, total=False):
    itemStyle: SeriesGaugeMarkpointDataItemstyle
    label: SeriesGaugeMarkpointDataLabel
    name: str
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    value: Any
    x: Any
    y: Any


class SeriesGaugeMarkpointItemstyleEmphasis(TypedDict, total=False):
    opacity: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesGaugeMarkpointItemstyle(TypedDict, total=False):
    emphasis: SeriesGaugeMarkpointItemstyleEmphasis


class SeriesGaugeMarkpointLabelEmphasis(TypedDict, total=False):
    formatter: Any
    position: str


class SeriesGaugeMarkpointLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontSize: int | float


class SeriesGaugeMarkpointLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesGaugeMarkpointLabelNormalTextstyle


class SeriesGaugeMarkpointLabel(TypedDict, total=False):
    emphasis: SeriesGaugeMarkpointLabelEmphasis
    normal: SeriesGaugeMarkpointLabelNormal


class SeriesGaugeMarkpoint(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    data: SeriesGaugeMarkpointData
    itemStyle: SeriesGaugeMarkpointItemstyle
    label: SeriesGaugeMarkpointLabel
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float


class SeriesGaugePointer(TypedDict, total=False):
    length: int | float
    show: bool
    width: int | float


class SeriesGaugeSplitlineLinestyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesGaugeSplitline(TypedDict, total=False):
    length: int | float
    lineStyle: SeriesGaugeSplitlineLinestyle
    show: bool


class SeriesGaugeTitleTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesGaugeTitle(TypedDict, total=False):
    offsetCenter: int | float
    show: bool
    textStyle: SeriesGaugeTitleTextstyle


class SeriesGauge(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    axisLabel: SeriesGaugeAxislabel
    axisLine: SeriesGaugeAxisline
    axisTick: SeriesGaugeAxistick
    clockwise: bool
    detail: SeriesGaugeDetail
    endAngle: Any
    itemStyle: SeriesGaugeItemstyle
    markLine: SeriesGaugeMarkline
    markPoint: SeriesGaugeMarkpoint
    max: int | float
    min: int | float
    name: str
    pointer: SeriesGaugePointer
    radius: list | dict
    splitLine: SeriesGaugeSplitline
    splitNumber: Any
    startAngle: Any
    title: SeriesGaugeTitle
    type: Literal['gauge']


class SeriesGraphCategoriesItemstyleEmphasis(TypedDict, total=False):
    color: str


class SeriesGraphCategoriesItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetY: int | float


class SeriesGraphCategoriesItemstyle(TypedDict, total=False):
    emphasis: SeriesGraphCategoriesItemstyleEmphasis
    normal: SeriesGraphCategoriesItemstyleNormal


class SeriesGraphCategoriesLabelNormal(TypedDict, total=False):
    formatter: Any


class SeriesGraphCategoriesLabel(TypedDict, total=False):
    normal: SeriesGraphCategoriesLabelNormal


class SeriesGraphCategories(TypedDict, total=False):
    itemStyle: SeriesGraphCategoriesItemstyle
    label: SeriesGraphCategoriesLabel
    name: str
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float


class SeriesGraphDataItemstyleEmphasis(TypedDict, total=False):
    borderColor: str
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesGraphDataItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesGraphDataItemstyle(TypedDict, total=False):
    emphasis: SeriesGraphDataItemstyleEmphasis
    normal: SeriesGraphDataItemstyleNormal


class SeriesGraphDataLabelEmphasis(TypedDict, total=False):
    position: str
    show: bool
    textStyle: Any


class SeriesGraphDataLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesGraphDataLabelNormal(TypedDict, total=False):
    position: str
    show: bool
    textStyle: SeriesGraphDataLabelNormalTextstyle


class SeriesGraphDataLabel(TypedDict, total=False):
    emphasis: SeriesGraphDataLabelEmphasis
    normal: SeriesGraphDataLabelNormal


class SeriesGraphData(TypedDict, total=False):
    category: Any
    itemStyle: SeriesGraphDataItemstyle
    label: SeriesGraphDataLabel
    name: str
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    value: Any


class SeriesGraphForce(TypedDict, total=False):
    edgeLength: int | float
    gravity: Any
    initLayout: Any
    layoutAnimation: bool
    repulsion: Any


class SeriesGraphItemstyleEmphasis(TypedDict, total=False):
    borderWidth: int | float
    color: str
    shadowOffsetY: int | float


class SeriesGraphItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesGraphItemstyle(TypedDict, total=False):
    emphasis: SeriesGraphItemstyleEmphasis
    normal: SeriesGraphItemstyleNormal


class SeriesGraphLabelEmphasisTextstyle(TypedDict, total=False):
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesGraphLabelEmphasis(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesGraphLabelEmphasisTextstyle


class SeriesGraphLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesGraphLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesGraphLabelNormalTextstyle


class SeriesGraphLabel(TypedDict, total=False):
    emphasis: SeriesGraphLabelEmphasis
    normal: SeriesGraphLabelNormal


class SeriesGraphLinestyleEmphasis(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesGraphLinestyleNormal(TypedDict, total=False):
    color: str
    curveness: int | float
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesGraphLinestyle(TypedDict, total=False):
    emphasis: SeriesGraphLinestyleEmphasis
    normal: SeriesGraphLinestyleNormal


class SeriesGraphLinksLinestyleEmphasis(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesGraphLinksLinestyleNormal(TypedDict, total=False):
    color: str
    curveness: int | float
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesGraphLinksLinestyle(TypedDict, total=False):
    emphasis: SeriesGraphLinksLinestyleEmphasis
    normal: SeriesGraphLinksLinestyleNormal


class SeriesGraphLinks(TypedDict, total=False):
    lineStyle: SeriesGraphLinksLinestyle
    source: Any
    target: Any


class SeriesGraphMarklineDataItemLabelEmphasis(TypedDict, total=False):
    formatter: Any
    position: str


class SeriesGraphMarklineDataItemLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str


class SeriesGraphMarklineDataItemLabel(TypedDict, total=False):
    emphasis: SeriesGraphMarklineDataItemLabelEmphasis
    normal: SeriesGraphMarklineDataItemLabelNormal


class SeriesGraphMarklineDataItemLinestyleNormal(TypedDict, total=False):
    type: Literal['solid', 'dashed', 'dotted']


class SeriesGraphMarklineDataItemLinestyle(TypedDict, total=False):
    normal: SeriesGraphMarklineDataItemLinestyleNormal


class SeriesGraphMarklineDataItem(TypedDict, total=False):
    label: SeriesGraphMarklineDataItemLabel
    lineStyle: SeriesGraphMarklineDataItemLinestyle
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    value: Any
    x: Any
    y: Any


class SeriesGraphMarklineLabelEmphasis(TypedDict, total=False):
    formatter: Any


class SeriesGraphMarklineLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool


class SeriesGraphMarklineLabel(TypedDict, total=False):
    emphasis: SeriesGraphMarklineLabelEmphasis
    normal: SeriesGraphMarklineLabelNormal


class SeriesGraphMarklineLinestyleEmphasis(TypedDict, total=False):
    shadowBlur: int | float
    type: Literal['solid', 'dashed', 'dotted']


class SeriesGraphMarklineLinestyleNormal(TypedDict, total=False):
    color: str
    curveness: int | float
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesGraphMarklineLinestyle(TypedDict, total=False):
    emphasis: SeriesGraphMarklineLinestyleEmphasis
    normal: SeriesGraphMarklineLinestyleNormal


class SeriesGraphMarkline(TypedDict, total=False):
    animation: bool
    animationEasing: str
    data: List[SeriesGraphMarklineDataItem]
    label: SeriesGraphMarklineLabel
    lineStyle: SeriesGraphMarklineLinestyle
    precision: int | float
    symbol: str
    symbolSize: int | float


class SeriesGraphMarkpointDataItemstyleNormal(TypedDict, total=False):
    color: str


class SeriesGraphMarkpointDataItemstyle(TypedDict, total=False):
    normal: SeriesGraphMarkpointDataItemstyleNormal


class SeriesGraphMarkpointDataLabelEmphasisTextstyle(TypedDict, total=False):
    fontFamily: str


class SeriesGraphMarkpointDataLabelEmphasis(TypedDict, total=False):
    textStyle: SeriesGraphMarkpointDataLabelEmphasisTextstyle


class SeriesGraphMarkpointDataLabelNormal(TypedDict, total=False):
    position: str
    show: bool
    textStyle: Any


class SeriesGraphMarkpointDataLabel(TypedDict, total=False):
    emphasis: SeriesGraphMarkpointDataLabelEmphasis
    normal: SeriesGraphMarkpointDataLabelNormal


class SeriesGraphMarkpointData(TypedDict, total=False):
    itemStyle: SeriesGraphMarkpointDataItemstyle
    label: SeriesGraphMarkpointDataLabel
    name: str
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    value: Any
    x: Any
    y: Any


class SeriesGraphMarkpointItemstyleEmphasis(TypedDict, total=False):
    color: str


class SeriesGraphMarkpointItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesGraphMarkpointItemstyle(TypedDict, total=False):
    emphasis: SeriesGraphMarkpointItemstyleEmphasis
    normal: SeriesGraphMarkpointItemstyleNormal


class SeriesGraphMarkpointLabelEmphasis(TypedDict, total=False):
    formatter: Any


class SeriesGraphMarkpointLabelNormalTextstyle(TypedDict, total=False):
    color: str


class SeriesGraphMarkpointLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesGraphMarkpointLabelNormalTextstyle


class SeriesGraphMarkpointLabel(TypedDict, total=False):
    emphasis: SeriesGraphMarkpointLabelEmphasis
    normal: SeriesGraphMarkpointLabelNormal


class SeriesGraphMarkpoint(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    data: SeriesGraphMarkpointData
    itemStyle: SeriesGraphMarkpointItemstyle
    label: SeriesGraphMarkpointLabel
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float


class SeriesGraph(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    bottom: Any
    categories: SeriesGraphCategories
    color: str
    data: SeriesGraphData
    edges: Any
    force: SeriesGraphForce
    height: int | float
    hoverAnimation: bool
    itemStyle: SeriesGraphItemstyle
    label: SeriesGraphLabel
    layout: Any
    left: Any
    legendHoverLink: Any
    lineStyle: SeriesGraphLinestyle
    links: SeriesGraphLinks
    markLine: SeriesGraphMarkline
    markPoint: SeriesGraphMarkpoint
    name: str
    nodeScaleRatio: bool
    nodes: Any
    right: Any
    roam: bool
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    top: Any
    type: Literal['graph']
    width: int | float
    z: int | float
    zlevel: int | float


class SeriesHeatmapDataItemstyleEmphasis(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesHeatmapDataItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float


class SeriesHeatmapDataItemstyle(TypedDict, total=False):
    emphasis: SeriesHeatmapDataItemstyleEmphasis
    normal: SeriesHeatmapDataItemstyleNormal


class SeriesHeatmapDataLabelEmphasis(TypedDict, total=False):
    position: str
    show: bool
    textStyle: Any


class SeriesHeatmapDataLabelNormalTextstyle(TypedDict, total=False):
    color: str


class SeriesHeatmapDataLabelNormal(TypedDict, total=False):
    position: str
    show: bool
    textStyle: SeriesHeatmapDataLabelNormalTextstyle


class SeriesHeatmapDataLabel(TypedDict, total=False):
    emphasis: SeriesHeatmapDataLabelEmphasis
    normal: SeriesHeatmapDataLabelNormal


class SeriesHeatmapData(TypedDict, total=False):
    itemStyle: SeriesHeatmapDataItemstyle
    label: SeriesHeatmapDataLabel
    name: str
    value: Any


class SeriesHeatmapMarkline(TypedDict, total=False):
    symbolSize: int | float


class SeriesHeatmapMarkpoint(TypedDict, total=False):
    itemStyle: Any
    symbolRotate: int | float


class SeriesHeatmap(TypedDict, total=False):
    blurSize: int | float
    coordinateSystem: str
    data: SeriesHeatmapData
    geoIndex: int | float
    markLine: SeriesHeatmapMarkline
    markPoint: SeriesHeatmapMarkpoint
    name: str
    type: Literal['heatmap']
    xAxisIndex: int | float
    yAxisIndex: int | float


class SeriesLineAreastyleEmphasis(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesLineAreastyleNormal(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesLineAreastyle(TypedDict, total=False):
    emphasis: SeriesLineAreastyleEmphasis
    normal: SeriesLineAreastyleNormal


class SeriesLineDataItemstyleEmphasis(TypedDict, total=False):
    barBorderColor: str
    barBorderWidth: int | float
    color: str
    opacity: int | float
    shadowColor: str
    shadowOffsetX: int | float


class SeriesLineDataItemstyleNormal(TypedDict, total=False):
    barBorderColor: str
    barBorderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesLineDataItemstyle(TypedDict, total=False):
    emphasis: SeriesLineDataItemstyleEmphasis
    normal: SeriesLineDataItemstyleNormal


class SeriesLineDataLabelEmphasisTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesLineDataLabelEmphasis(TypedDict, total=False):
    position: str
    show: bool
    textStyle: SeriesLineDataLabelEmphasisTextstyle


class SeriesLineDataLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesLineDataLabelNormal(TypedDict, total=False):
    position: str
    show: bool
    textStyle: SeriesLineDataLabelNormalTextstyle


class SeriesLineDataLabel(TypedDict, total=False):
    emphasis: SeriesLineDataLabelEmphasis
    normal: SeriesLineDataLabelNormal


class SeriesLineData(TypedDict, total=False):
    itemStyle: SeriesLineDataItemstyle
    label: SeriesLineDataLabel
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    value: Any


class SeriesLineItemstyleEmphasis(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesLineItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesLineItemstyle(TypedDict, total=False):
    emphasis: SeriesLineItemstyleEmphasis
    normal: SeriesLineItemstyleNormal


class SeriesLineLabelEmphasisTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesLineLabelEmphasis(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesLineLabelEmphasisTextstyle


class SeriesLineLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesLineLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesLineLabelNormalTextstyle


class SeriesLineLabel(TypedDict, total=False):
    emphasis: SeriesLineLabelEmphasis
    normal: SeriesLineLabelNormal


class SeriesLineLinestyleEmphasis(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesLineLinestyleNormal(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesLineLinestyle(TypedDict, total=False):
    emphasis: SeriesLineLinestyleEmphasis
    normal: SeriesLineLinestyleNormal


class SeriesLineMarklineDataItemLabelEmphasis(TypedDict, total=False):
    formatter: Any


class SeriesLineMarklineDataItemLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool


class SeriesLineMarklineDataItemLabel(TypedDict, total=False):
    emphasis: SeriesLineMarklineDataItemLabelEmphasis
    normal: SeriesLineMarklineDataItemLabelNormal


class SeriesLineMarklineDataItemLinestyleEmphasis(TypedDict, total=False):
    color: str
    curveness: int | float
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesLineMarklineDataItemLinestyleNormal(TypedDict, total=False):
    color: str
    curveness: int | float
    shadowBlur: int | float
    shadowOffsetX: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesLineMarklineDataItemLinestyle(TypedDict, total=False):
    emphasis: SeriesLineMarklineDataItemLinestyleEmphasis
    normal: SeriesLineMarklineDataItemLinestyleNormal


class SeriesLineMarklineDataItem(TypedDict, total=False):
    coord: str
    label: SeriesLineMarklineDataItemLabel
    lineStyle: SeriesLineMarklineDataItemLinestyle
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    type: Literal['min', 'max', 'average']
    value: Any
    valueDim: Any
    valueIndex: int | float
    x: Any
    y: Any


class SeriesLineMarklineLabelEmphasis(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool


class SeriesLineMarklineLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool


class SeriesLineMarklineLabel(TypedDict, total=False):
    emphasis: SeriesLineMarklineLabelEmphasis
    normal: SeriesLineMarklineLabelNormal


class SeriesLineMarklineLinestyleEmphasis(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesLineMarklineLinestyleNormal(TypedDict, total=False):
    color: str
    curveness: int | float
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesLineMarklineLinestyle(TypedDict, total=False):
    emphasis: SeriesLineMarklineLinestyleEmphasis
    normal: SeriesLineMarklineLinestyleNormal


class SeriesLineMarkline(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    data: List[SeriesLineMarklineDataItem]
    label: SeriesLineMarklineLabel
    lineStyle: SeriesLineMarklineLinestyle
    precision: int | float
    symbol: str
    symbolSize: int | float


class SeriesLineMarkpointDataItemstyleEmphasis(TypedDict, total=False):
    borderColor: str
    color: str


class SeriesLineMarkpointDataItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesLineMarkpointDataItemstyle(TypedDict, total=False):
    emphasis: SeriesLineMarkpointDataItemstyleEmphasis
    normal: SeriesLineMarkpointDataItemstyleNormal


class SeriesLineMarkpointDataLabelEmphasisTextstyle(TypedDict, total=False):
    color: str


class SeriesLineMarkpointDataLabelEmphasis(TypedDict, total=False):
    position: str
    show: bool
    textStyle: SeriesLineMarkpointDataLabelEmphasisTextstyle


class SeriesLineMarkpointDataLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesLineMarkpointDataLabelNormal(TypedDict, total=False):
    position: str
    show: bool
    textStyle: SeriesLineMarkpointDataLabelNormalTextstyle


class SeriesLineMarkpointDataLabel(TypedDict, total=False):
    emphasis: SeriesLineMarkpointDataLabelEmphasis
    normal: SeriesLineMarkpointDataLabelNormal


class SeriesLineMarkpointData(TypedDict, total=False):
    coord: str
    itemStyle: SeriesLineMarkpointDataItemstyle
    label: SeriesLineMarkpointDataLabel
    name: str
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    type: Literal['min', 'max', 'average']
    value: Any
    valueDim: Any
    valueIndex: int | float
    x: Any
    y: Any


class SeriesLineMarkpointItemstyleEmphasis(TypedDict, total=False):
    borderColor: str
    color: str


class SeriesLineMarkpointItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesLineMarkpointItemstyle(TypedDict, total=False):
    emphasis: SeriesLineMarkpointItemstyleEmphasis
    normal: SeriesLineMarkpointItemstyleNormal


class SeriesLineMarkpointLabelEmphasisTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesLineMarkpointLabelEmphasis(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesLineMarkpointLabelEmphasisTextstyle


class SeriesLineMarkpointLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesLineMarkpointLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesLineMarkpointLabelNormalTextstyle


class SeriesLineMarkpointLabel(TypedDict, total=False):
    emphasis: SeriesLineMarkpointLabelEmphasis
    normal: SeriesLineMarkpointLabelNormal


class SeriesLineMarkpoint(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    data: SeriesLineMarkpointData
    itemStyle: SeriesLineMarkpointItemstyle
    label: SeriesLineMarkpointLabel
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float


class SeriesLine(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    areaStyle: SeriesLineAreastyle
    clipOverflow: Any
    coordinateSystem: str
    data: SeriesLineData
    hoverAnimation: bool
    itemStyle: SeriesLineItemstyle
    label: SeriesLineLabel
    legendHoverLink: Any
    lineStyle: SeriesLineLinestyle
    markLine: SeriesLineMarkline
    markPoint: SeriesLineMarkpoint
    name: str
    polarIndex: int | float
    showAllSymbol: bool
    showSymbol: bool
    smooth: Any
    smoothMonotone: Literal['x', 'y']
    stack: str
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    type: Literal['line']
    xAxisIndex: int | float
    yAxisIndex: int | float
    z: int | float
    zlevel: int | float


class SeriesLinesDataItemLinestyleEmphasis(TypedDict, total=False):
    curveness: int | float


class SeriesLinesDataItemLinestyleNormal(TypedDict, total=False):
    curveness: int | float
    opacity: int | float
    shadowBlur: int | float
    width: int | float


class SeriesLinesDataItemLinestyle(TypedDict, total=False):
    emphasis: SeriesLinesDataItemLinestyleEmphasis
    normal: SeriesLinesDataItemLinestyleNormal


class SeriesLinesDataItem(TypedDict, total=False):
    coord: str
    lineStyle: SeriesLinesDataItemLinestyle
    name: str
    value: Any


class SeriesLinesEffect(TypedDict, total=False):
    color: str
    period: int | float
    show: bool
    symbol: str
    symbolSize: int | float
    trailLength: int | float


class SeriesLinesLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool


class SeriesLinesLabel(TypedDict, total=False):
    normal: SeriesLinesLabelNormal


class SeriesLinesLinestyleEmphasis(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']


class SeriesLinesLinestyleNormal(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesLinesLinestyle(TypedDict, total=False):
    emphasis: SeriesLinesLinestyleEmphasis
    normal: SeriesLinesLinestyleNormal


class SeriesLinesMarklineDataItemLabelNormal(TypedDict, total=False):
    position: str


class SeriesLinesMarklineDataItemLabel(TypedDict, total=False):
    normal: SeriesLinesMarklineDataItemLabelNormal


class SeriesLinesMarklineDataItemLinestyle(TypedDict, total=False):
    emphasis: Any
    normal: Any


class SeriesLinesMarklineDataItem(TypedDict, total=False):
    label: SeriesLinesMarklineDataItemLabel
    lineStyle: SeriesLinesMarklineDataItemLinestyle
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    value: Any
    x: Any
    y: Any


class SeriesLinesMarklineLabelEmphasis(TypedDict, total=False):
    formatter: Any


class SeriesLinesMarklineLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str


class SeriesLinesMarklineLabel(TypedDict, total=False):
    emphasis: SeriesLinesMarklineLabelEmphasis
    normal: SeriesLinesMarklineLabelNormal


class SeriesLinesMarklineLinestyleEmphasis(TypedDict, total=False):
    color: str


class SeriesLinesMarklineLinestyleNormal(TypedDict, total=False):
    color: str
    curveness: int | float
    shadowBlur: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesLinesMarklineLinestyle(TypedDict, total=False):
    emphasis: SeriesLinesMarklineLinestyleEmphasis
    normal: SeriesLinesMarklineLinestyleNormal


class SeriesLinesMarkline(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    data: List[SeriesLinesMarklineDataItem]
    label: SeriesLinesMarklineLabel
    lineStyle: SeriesLinesMarklineLinestyle
    precision: int | float
    symbol: str
    symbolSize: int | float


class SeriesLinesMarkpointDataItemstyle(TypedDict, total=False):
    normal: Any


class SeriesLinesMarkpointDataLabelNormal(TypedDict, total=False):
    position: str


class SeriesLinesMarkpointDataLabel(TypedDict, total=False):
    normal: SeriesLinesMarkpointDataLabelNormal


class SeriesLinesMarkpointData(TypedDict, total=False):
    itemStyle: SeriesLinesMarkpointDataItemstyle
    label: SeriesLinesMarkpointDataLabel
    name: str
    symbolRotate: int | float
    symbolSize: int | float
    x: Any
    y: Any


class SeriesLinesMarkpointItemstyleEmphasis(TypedDict, total=False):
    opacity: int | float


class SeriesLinesMarkpointItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str


class SeriesLinesMarkpointItemstyle(TypedDict, total=False):
    emphasis: SeriesLinesMarkpointItemstyleEmphasis
    normal: SeriesLinesMarkpointItemstyleNormal


class SeriesLinesMarkpointLabelEmphasis(TypedDict, total=False):
    formatter: Any


class SeriesLinesMarkpointLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesLinesMarkpointLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesLinesMarkpointLabelNormalTextstyle


class SeriesLinesMarkpointLabel(TypedDict, total=False):
    emphasis: SeriesLinesMarkpointLabelEmphasis
    normal: SeriesLinesMarkpointLabelNormal


class SeriesLinesMarkpoint(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    data: SeriesLinesMarkpointData
    itemStyle: SeriesLinesMarkpointItemstyle
    label: SeriesLinesMarkpointLabel
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float


class SeriesLines(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    coordinateSystem: str
    data: List[SeriesLinesDataItem]
    effect: SeriesLinesEffect
    geoIndex: int | float
    label: SeriesLinesLabel
    lineStyle: SeriesLinesLinestyle
    markLine: SeriesLinesMarkline
    markPoint: SeriesLinesMarkpoint
    name: str
    type: Literal['lines']
    xAxisIndex: int | float
    yAxisIndex: int | float
    z: int | float
    zlevel: int | float


class SeriesMapData(TypedDict, total=False):
    name: str
    value: Any


class SeriesMapItemstyleEmphasis(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesMapItemstyleNormal(TypedDict, total=False):
    areaColor: str
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesMapItemstyle(TypedDict, total=False):
    bottom: Any
    emphasis: SeriesMapItemstyleEmphasis
    left: Any
    normal: SeriesMapItemstyleNormal
    right: Any
    top: Any
    z: int | float
    zlevel: int | float


class SeriesMapLabelEmphasisTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesMapLabelEmphasis(TypedDict, total=False):
    show: bool
    textStyle: SeriesMapLabelEmphasisTextstyle


class SeriesMapLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesMapLabelNormal(TypedDict, total=False):
    show: bool
    textStyle: SeriesMapLabelNormalTextstyle


class SeriesMapLabel(TypedDict, total=False):
    emphasis: SeriesMapLabelEmphasis
    normal: SeriesMapLabelNormal


class SeriesMap(TypedDict, total=False):
    bottom: Any
    data: SeriesMapData
    itemStyle: SeriesMapItemstyle
    label: SeriesMapLabel
    left: Any
    map: str
    mapValueCalculation: str
    name: str
    right: Any
    roam: bool
    selectedMode: Literal['multiple', 'single', 'series'] | bool
    showLegendSymbol: bool
    top: Any
    type: Literal['map']
    z: int | float
    zlevel: int | float


class SeriesParallelDataLinestyle(TypedDict, total=False):
    color: str
    emphasis: Any
    normal: Any
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesParallelData(TypedDict, total=False):
    lineStyle: SeriesParallelDataLinestyle
    name: str
    value: Any


class SeriesParallelLinestyleEmphasis(TypedDict, total=False):
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    type: Literal['solid', 'dashed', 'dotted']


class SeriesParallelLinestyleNormal(TypedDict, total=False):
    color: str
    width: int | float


class SeriesParallelLinestyle(TypedDict, total=False):
    emphasis: SeriesParallelLinestyleEmphasis
    normal: SeriesParallelLinestyleNormal


class SeriesParallel(TypedDict, total=False):
    activeOpacity: int | float
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    coordinateSystem: str
    data: SeriesParallelData
    inactiveOpacity: int | float
    lineStyle: SeriesParallelLinestyle
    name: str
    parallelIndex: int | float
    type: Literal['parallel']


class SeriesPieDataItemstyleEmphasis(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesPieDataItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesPieDataItemstyle(TypedDict, total=False):
    emphasis: SeriesPieDataItemstyleEmphasis
    normal: SeriesPieDataItemstyleNormal


class SeriesPieDataLabelEmphasisTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesPieDataLabelEmphasis(TypedDict, total=False):
    show: bool
    textStyle: SeriesPieDataLabelEmphasisTextstyle


class SeriesPieDataLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesPieDataLabelNormal(TypedDict, total=False):
    position: str
    show: bool
    textStyle: SeriesPieDataLabelNormalTextstyle


class SeriesPieDataLabel(TypedDict, total=False):
    emphasis: SeriesPieDataLabelEmphasis
    normal: SeriesPieDataLabelNormal


class SeriesPieDataLabellineEmphasisLinestyle(TypedDict, total=False):
    color: str


class SeriesPieDataLabellineEmphasis(TypedDict, total=False):
    lineStyle: SeriesPieDataLabellineEmphasisLinestyle
    show: bool


class SeriesPieDataLabellineNormalLinestyle(TypedDict, total=False):
    color: str
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesPieDataLabellineNormal(TypedDict, total=False):
    length: int | float
    length2: int | float
    lineStyle: SeriesPieDataLabellineNormalLinestyle
    show: bool
    smooth: Any


class SeriesPieDataLabelline(TypedDict, total=False):
    emphasis: SeriesPieDataLabellineEmphasis
    normal: SeriesPieDataLabellineNormal


class SeriesPieData(TypedDict, total=False):
    itemStyle: SeriesPieDataItemstyle
    label: SeriesPieDataLabel
    labelLine: SeriesPieDataLabelline
    name: str
    selected: Any
    value: Any


class SeriesPieItemstyleEmphasis(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesPieItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesPieItemstyle(TypedDict, total=False):
    emphasis: SeriesPieItemstyleEmphasis
    normal: SeriesPieItemstyleNormal


class SeriesPieLabelEmphasisTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesPieLabelEmphasis(TypedDict, total=False):
    formatter: Any
    show: bool
    textStyle: SeriesPieLabelEmphasisTextstyle


class SeriesPieLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesPieLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesPieLabelNormalTextstyle


class SeriesPieLabel(TypedDict, total=False):
    emphasis: SeriesPieLabelEmphasis
    normal: SeriesPieLabelNormal


class SeriesPieLabellineEmphasisLinestyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesPieLabellineEmphasis(TypedDict, total=False):
    lineStyle: SeriesPieLabellineEmphasisLinestyle
    show: bool


class SeriesPieLabellineNormalLinestyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesPieLabellineNormal(TypedDict, total=False):
    length: int | float
    length2: int | float
    lineStyle: SeriesPieLabellineNormalLinestyle
    show: bool
    smooth: Any


class SeriesPieLabelline(TypedDict, total=False):
    emphasis: SeriesPieLabellineEmphasis
    normal: SeriesPieLabellineNormal


class SeriesPieMarklineDataItemLabelEmphasis(TypedDict, total=False):
    formatter: Any


class SeriesPieMarklineDataItemLabelNormal(TypedDict, total=False):
    formatter: Any


class SeriesPieMarklineDataItemLabel(TypedDict, total=False):
    emphasis: SeriesPieMarklineDataItemLabelEmphasis
    normal: SeriesPieMarklineDataItemLabelNormal


class SeriesPieMarklineDataItemLinestyleNormal(TypedDict, total=False):
    color: str


class SeriesPieMarklineDataItemLinestyle(TypedDict, total=False):
    normal: SeriesPieMarklineDataItemLinestyleNormal


class SeriesPieMarklineDataItem(TypedDict, total=False):
    label: SeriesPieMarklineDataItemLabel
    lineStyle: SeriesPieMarklineDataItemLinestyle
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    value: Any
    x: Any
    y: Any


class SeriesPieMarklineLabelEmphasis(TypedDict, total=False):
    formatter: Any


class SeriesPieMarklineLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool


class SeriesPieMarklineLabel(TypedDict, total=False):
    emphasis: SeriesPieMarklineLabelEmphasis
    normal: SeriesPieMarklineLabelNormal


class SeriesPieMarklineLinestyleEmphasis(TypedDict, total=False):
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']


class SeriesPieMarklineLinestyleNormal(TypedDict, total=False):
    color: str


class SeriesPieMarklineLinestyle(TypedDict, total=False):
    emphasis: SeriesPieMarklineLinestyleEmphasis
    normal: SeriesPieMarklineLinestyleNormal


class SeriesPieMarkline(TypedDict, total=False):
    animation: bool
    animationEasingUpdate: str
    data: List[SeriesPieMarklineDataItem]
    label: SeriesPieMarklineLabel
    lineStyle: SeriesPieMarklineLinestyle
    precision: int | float
    symbol: str
    symbolSize: int | float


class SeriesPieMarkpointDataItemstyleEmphasis(TypedDict, total=False):
    color: str


class SeriesPieMarkpointDataItemstyleNormal(TypedDict, total=False):
    color: str


class SeriesPieMarkpointDataItemstyle(TypedDict, total=False):
    emphasis: SeriesPieMarkpointDataItemstyleEmphasis
    normal: SeriesPieMarkpointDataItemstyleNormal


class SeriesPieMarkpointDataLabelNormal(TypedDict, total=False):
    position: str
    show: bool
    textStyle: Any


class SeriesPieMarkpointDataLabel(TypedDict, total=False):
    normal: SeriesPieMarkpointDataLabelNormal


class SeriesPieMarkpointData(TypedDict, total=False):
    itemStyle: SeriesPieMarkpointDataItemstyle
    label: SeriesPieMarkpointDataLabel
    name: str
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    value: Any
    x: Any
    y: Any


class SeriesPieMarkpointItemstyleNormal(TypedDict, total=False):
    color: str


class SeriesPieMarkpointItemstyle(TypedDict, total=False):
    normal: SeriesPieMarkpointItemstyleNormal


class SeriesPieMarkpointLabelEmphasis(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool


class SeriesPieMarkpointLabelNormalTextstyle(TypedDict, total=False):
    color: str


class SeriesPieMarkpointLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesPieMarkpointLabelNormalTextstyle


class SeriesPieMarkpointLabel(TypedDict, total=False):
    emphasis: SeriesPieMarkpointLabelEmphasis
    normal: SeriesPieMarkpointLabelNormal


class SeriesPieMarkpoint(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    data: SeriesPieMarkpointData
    itemStyle: SeriesPieMarkpointItemstyle
    label: SeriesPieMarkpointLabel
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float


class SeriesPie(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    avoidLabelOverlap: bool
    center: list | dict
    clockwise: bool
    data: SeriesPieData
    hoverAnimation: bool
    itemStyle: SeriesPieItemstyle
    label: SeriesPieLabel
    labelLine: SeriesPieLabelline
    legendHoverLink: Any
    markLine: SeriesPieMarkline
    markPoint: SeriesPieMarkpoint
    minAngle: int | float
    name: str
    radius: list | dict
    roseType: Literal['radius', 'area']
    selectedMode: Literal['multiple', 'single', 'series'] | bool
    selectedOffset: int | float
    startAngle: Any
    type: Literal['pie']
    z: int | float
    zlevel: int | float


class SeriesSankeyDataItemstyleEmphasis(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesSankeyDataItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesSankeyDataItemstyle(TypedDict, total=False):
    emphasis: SeriesSankeyDataItemstyleEmphasis
    normal: SeriesSankeyDataItemstyleNormal


class SeriesSankeyDataLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontStyle: Literal['normal', 'italic', 'oblique']


class SeriesSankeyDataLabelNormal(TypedDict, total=False):
    position: str
    show: bool
    textStyle: SeriesSankeyDataLabelNormalTextstyle


class SeriesSankeyDataLabel(TypedDict, total=False):
    normal: SeriesSankeyDataLabelNormal


class SeriesSankeyData(TypedDict, total=False):
    itemStyle: SeriesSankeyDataItemstyle
    label: SeriesSankeyDataLabel
    name: str
    value: Any


class SeriesSankeyItemstyleEmphasis(TypedDict, total=False):
    borderColor: str
    color: str


class SeriesSankeyItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesSankeyItemstyle(TypedDict, total=False):
    emphasis: SeriesSankeyItemstyleEmphasis
    normal: SeriesSankeyItemstyleNormal


class SeriesSankeyLabelNormalTextstyle(TypedDict, total=False):
    color: str


class SeriesSankeyLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesSankeyLabelNormalTextstyle


class SeriesSankeyLabel(TypedDict, total=False):
    emphasis: Any
    normal: SeriesSankeyLabelNormal


class SeriesSankeyLinestyleEmphasis(TypedDict, total=False):
    color: str


class SeriesSankeyLinestyleNormal(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str


class SeriesSankeyLinestyle(TypedDict, total=False):
    emphasis: SeriesSankeyLinestyleEmphasis
    normal: SeriesSankeyLinestyleNormal


class SeriesSankeyLinksLinestyleEmphasis(TypedDict, total=False):
    color: str
    curveness: int | float
    opacity: int | float
    shadowBlur: int | float


class SeriesSankeyLinksLinestyleNormal(TypedDict, total=False):
    color: str
    curveness: int | float
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesSankeyLinksLinestyle(TypedDict, total=False):
    emphasis: SeriesSankeyLinksLinestyleEmphasis
    normal: SeriesSankeyLinksLinestyleNormal


class SeriesSankeyLinks(TypedDict, total=False):
    lineStyle: SeriesSankeyLinksLinestyle
    source: Any
    target: Any
    value: Any


class SeriesSankey(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    bottom: Any
    data: SeriesSankeyData
    edges: Any
    height: int | float
    itemStyle: SeriesSankeyItemstyle
    label: SeriesSankeyLabel
    layoutIterations: Any
    left: Any
    lineStyle: SeriesSankeyLinestyle
    links: SeriesSankeyLinks
    nodeGap: int | float
    nodeWidth: int | float
    nodes: Any
    right: Any
    top: Any
    type: Literal['sankey']
    width: int | float
    z: int | float
    zlevel: int | float


class SeriesScatterDataItemstyleEmphasis(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str


class SeriesScatterDataItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesScatterDataItemstyle(TypedDict, total=False):
    emphasis: SeriesScatterDataItemstyleEmphasis
    normal: SeriesScatterDataItemstyleNormal


class SeriesScatterDataLabelEmphasis(TypedDict, total=False):
    position: str
    show: bool


class SeriesScatterDataLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesScatterDataLabelNormal(TypedDict, total=False):
    position: str
    show: bool
    textStyle: SeriesScatterDataLabelNormalTextstyle


class SeriesScatterDataLabel(TypedDict, total=False):
    emphasis: SeriesScatterDataLabelEmphasis
    normal: SeriesScatterDataLabelNormal


class SeriesScatterData(TypedDict, total=False):
    itemStyle: SeriesScatterDataItemstyle
    label: SeriesScatterDataLabel
    name: str
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    value: Any


class SeriesScatterItemstyleEmphasis(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetY: int | float


class SeriesScatterItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesScatterItemstyle(TypedDict, total=False):
    emphasis: SeriesScatterItemstyleEmphasis
    normal: SeriesScatterItemstyleNormal


class SeriesScatterLabelEmphasisTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesScatterLabelEmphasis(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesScatterLabelEmphasisTextstyle


class SeriesScatterLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesScatterLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesScatterLabelNormalTextstyle


class SeriesScatterLabel(TypedDict, total=False):
    emphasis: SeriesScatterLabelEmphasis
    normal: SeriesScatterLabelNormal


class SeriesScatterMarklineDataItemLabelEmphasis(TypedDict, total=False):
    formatter: Any


class SeriesScatterMarklineDataItemLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool


class SeriesScatterMarklineDataItemLabel(TypedDict, total=False):
    emphasis: SeriesScatterMarklineDataItemLabelEmphasis
    normal: SeriesScatterMarklineDataItemLabelNormal


class SeriesScatterMarklineDataItemLinestyleNormal(TypedDict, total=False):
    color: str
    curveness: int | float
    type: Literal['solid', 'dashed', 'dotted']


class SeriesScatterMarklineDataItemLinestyle(TypedDict, total=False):
    normal: SeriesScatterMarklineDataItemLinestyleNormal


class SeriesScatterMarklineDataItem(TypedDict, total=False):
    coord: str
    label: SeriesScatterMarklineDataItemLabel
    lineStyle: SeriesScatterMarklineDataItemLinestyle
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    type: Literal['min', 'max', 'average']
    value: Any
    valueIndex: int | float
    x: Any
    y: Any


class SeriesScatterMarklineLabelEmphasis(TypedDict, total=False):
    formatter: Any


class SeriesScatterMarklineLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool


class SeriesScatterMarklineLabel(TypedDict, total=False):
    emphasis: SeriesScatterMarklineLabelEmphasis
    normal: SeriesScatterMarklineLabelNormal


class SeriesScatterMarklineLinestyleEmphasis(TypedDict, total=False):
    color: str
    opacity: int | float
    type: Literal['solid', 'dashed', 'dotted']


class SeriesScatterMarklineLinestyleNormal(TypedDict, total=False):
    color: str
    curveness: int | float
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class SeriesScatterMarklineLinestyle(TypedDict, total=False):
    emphasis: SeriesScatterMarklineLinestyleEmphasis
    normal: SeriesScatterMarklineLinestyleNormal


class SeriesScatterMarkline(TypedDict, total=False):
    animation: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    data: List[SeriesScatterMarklineDataItem]
    label: SeriesScatterMarklineLabel
    lineStyle: SeriesScatterMarklineLinestyle
    precision: int | float
    symbol: str
    symbolSize: int | float


class SeriesScatterMarkpointDataItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str


class SeriesScatterMarkpointDataItemstyle(TypedDict, total=False):
    normal: SeriesScatterMarkpointDataItemstyleNormal


class SeriesScatterMarkpointDataLabel(TypedDict, total=False):
    emphasis: Any
    normal: Any


class SeriesScatterMarkpointData(TypedDict, total=False):
    coord: str
    itemStyle: SeriesScatterMarkpointDataItemstyle
    label: SeriesScatterMarkpointDataLabel
    name: str
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    type: Literal['min', 'max', 'average']
    value: Any
    valueDim: Any
    valueIndex: int | float
    x: Any
    y: Any


class SeriesScatterMarkpointItemstyleEmphasis(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesScatterMarkpointItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesScatterMarkpointItemstyle(TypedDict, total=False):
    emphasis: SeriesScatterMarkpointItemstyleEmphasis
    normal: SeriesScatterMarkpointItemstyleNormal


class SeriesScatterMarkpointLabelNormalTextstyle(TypedDict, total=False):
    color: str


class SeriesScatterMarkpointLabelNormal(TypedDict, total=False):
    formatter: Any
    position: str
    show: bool
    textStyle: SeriesScatterMarkpointLabelNormalTextstyle


class SeriesScatterMarkpointLabel(TypedDict, total=False):
    emphasis: Any
    normal: SeriesScatterMarkpointLabelNormal


class SeriesScatterMarkpoint(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    data: SeriesScatterMarkpointData
    itemStyle: SeriesScatterMarkpointItemstyle
    label: SeriesScatterMarkpointLabel
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float


class SeriesScatter(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    coordinateSystem: str
    data: SeriesScatterData
    geoIndex: int | float
    hoverAnimation: bool
    itemStyle: SeriesScatterItemstyle
    label: SeriesScatterLabel
    large: Any
    largeThreshold: Any
    legendHoverLink: Any
    markLine: SeriesScatterMarkline
    markPoint: SeriesScatterMarkpoint
    name: str
    polarIndex: int | float
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    type: Literal['scatter']
    xAxisIndex: int | float
    yAxisIndex: int | float
    z: int | float
    zlevel: int | float


class SeriesTreemapBreadcrumbItemstyleEmphasis(TypedDict, total=False):
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class SeriesTreemapBreadcrumbItemstyleNormal(TypedDict, total=False):
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    textStyle: Any


class SeriesTreemapBreadcrumbItemstyle(TypedDict, total=False):
    emphasis: SeriesTreemapBreadcrumbItemstyleEmphasis
    normal: SeriesTreemapBreadcrumbItemstyleNormal


class SeriesTreemapBreadcrumb(TypedDict, total=False):
    bottom: Any
    emptyItemWidth: int | float
    height: int | float
    itemStyle: SeriesTreemapBreadcrumbItemstyle
    left: Any
    show: bool


class SeriesTreemapDataItemstyle(TypedDict, total=False):
    normal: Any


class SeriesTreemapDataLabelNormal(TypedDict, total=False):
    position: str
    show: bool


class SeriesTreemapDataLabel(TypedDict, total=False):
    emphasis: Any
    normal: SeriesTreemapDataLabelNormal


class SeriesTreemapData(TypedDict, total=False):
    children: Any
    childrenVisibleMin: int | float
    color: str
    colorAlpha: str
    colorMappingBy: str
    colorSaturation: str
    id: Any
    itemStyle: SeriesTreemapDataItemstyle
    label: SeriesTreemapDataLabel
    link: Any
    name: str
    target: Any
    value: Any
    visibleMin: int | float
    visualDimension: Any


class SeriesTreemapItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderColorSaturation: str
    borderWidth: int | float
    color: str
    colorAlpha: str
    colorSaturation: str
    gapWidth: int | float


class SeriesTreemapItemstyle(TypedDict, total=False):
    emphasis: Any
    normal: SeriesTreemapItemstyleNormal


class SeriesTreemapLabelEmphasisTextstyle(TypedDict, total=False):
    align: Literal['left', 'center', 'right', 'auto']


class SeriesTreemapLabelEmphasis(TypedDict, total=False):
    position: str
    show: bool
    textStyle: SeriesTreemapLabelEmphasisTextstyle


class SeriesTreemapLabelNormalTextstyle(TypedDict, total=False):
    align: Literal['left', 'center', 'right', 'auto']
    baseline: Literal['top', 'middle', 'bottom']
    color: str
    ellipsis: Any
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesTreemapLabelNormal(TypedDict, total=False):
    position: str
    show: bool
    textStyle: SeriesTreemapLabelNormalTextstyle


class SeriesTreemapLabel(TypedDict, total=False):
    emphasis: SeriesTreemapLabelEmphasis
    normal: SeriesTreemapLabelNormal


class SeriesTreemapLevelsItemstyleEmphasis(TypedDict, total=False):
    borderColorSaturation: str
    borderWidth: int | float
    color: str
    colorAlpha: str
    gapWidth: int | float


class SeriesTreemapLevelsItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderColorSaturation: str
    borderWidth: int | float
    color: str
    colorAlpha: str
    colorSaturation: str
    gapWidth: int | float


class SeriesTreemapLevelsItemstyle(TypedDict, total=False):
    emphasis: SeriesTreemapLevelsItemstyleEmphasis
    normal: SeriesTreemapLevelsItemstyleNormal


class SeriesTreemapLevelsLabelEmphasisTextstyle(TypedDict, total=False):
    baseline: Literal['top', 'middle', 'bottom']
    ellipsis: Any
    fontStyle: Literal['normal', 'italic', 'oblique']


class SeriesTreemapLevelsLabelEmphasis(TypedDict, total=False):
    position: str
    show: bool
    textStyle: SeriesTreemapLevelsLabelEmphasisTextstyle


class SeriesTreemapLevelsLabelNormalTextstyle(TypedDict, total=False):
    align: Literal['left', 'center', 'right', 'auto']
    baseline: Literal['top', 'middle', 'bottom']
    color: str
    ellipsis: Any
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class SeriesTreemapLevelsLabelNormal(TypedDict, total=False):
    position: str
    show: bool
    textStyle: SeriesTreemapLevelsLabelNormalTextstyle


class SeriesTreemapLevelsLabel(TypedDict, total=False):
    emphasis: SeriesTreemapLevelsLabelEmphasis
    normal: SeriesTreemapLevelsLabelNormal


class SeriesTreemapLevels(TypedDict, total=False):
    childrenVisibleMin: int | float
    color: str
    colorAlpha: str
    colorMappingBy: str
    colorSaturation: str
    itemStyle: SeriesTreemapLevelsItemstyle
    label: SeriesTreemapLevelsLabel
    visibleMin: int | float
    visualDimension: Any


class SeriesTreemap(TypedDict, total=False):
    animationDuration: bool
    animationEasing: str
    bottom: Any
    breadcrumb: SeriesTreemapBreadcrumb
    childrenVisibleMin: int | float
    color: str
    colorAlpha: str
    colorMappingBy: str
    colorSaturation: str
    data: SeriesTreemapData
    height: int | float
    itemStyle: SeriesTreemapItemstyle
    label: SeriesTreemapLabel
    left: Any
    levels: SeriesTreemapLevels
    nodeClick: Any
    right: Any
    roam: bool
    squareRatio: Any
    top: Any
    type: Literal['treemap']
    visibleMin: int | float
    visualDimension: Any
    width: int | float
    z: int | float
    zlevel: int | float
    zoomToNodeRatio: int | float


class Textstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class TimelineCheckpointstyle(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationEasing: str
    borderColor: str
    borderWidth: int | float
    color: str
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float


class TimelineControlstyleEmphasis(TypedDict, total=False):
    color: str


class TimelineControlstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str


class TimelineControlstyle(TypedDict, total=False):
    emphasis: TimelineControlstyleEmphasis
    itemGap: int | float
    itemSize: int | float
    nextIcon: Any
    normal: TimelineControlstyleNormal
    playIcon: Any
    position: str
    prevIcon: Any
    show: bool
    showNextBtn: bool
    showPlayBtn: bool
    showPrevBtn: bool
    stopIcon: Any


class TimelineItemstyleEmphasis(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowColor: str


class TimelineItemstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class TimelineItemstyle(TypedDict, total=False):
    emphasis: TimelineItemstyleEmphasis
    normal: TimelineItemstyleNormal


class TimelineLabelEmphasisTextstyle(TypedDict, total=False):
    color: str


class TimelineLabelEmphasis(TypedDict, total=False):
    formatter: Any
    rotate: int | float
    show: bool
    textStyle: TimelineLabelEmphasisTextstyle


class TimelineLabelNormalTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class TimelineLabelNormal(TypedDict, total=False):
    formatter: Any
    interval: int | float
    rotate: int | float
    show: bool
    textStyle: TimelineLabelNormalTextstyle


class TimelineLabel(TypedDict, total=False):
    emphasis: TimelineLabelEmphasis
    normal: TimelineLabelNormal
    position: str


class TimelineLinestyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    show: bool
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class Timeline(TypedDict, total=False):
    autoPlay: Any
    axisType: Literal['category', 'time', 'value']
    bottom: Any
    checkpointStyle: TimelineCheckpointstyle
    controlPosition: Literal['left', 'right']
    controlStyle: TimelineControlstyle
    currentIndex: int | float
    data: list | dict
    inverse: bool
    itemStyle: TimelineItemstyle
    label: TimelineLabel
    left: Any
    lineStyle: TimelineLinestyle
    loop: Any
    orient: Literal['horizontal', 'vertical']
    padding: Any
    playInterval: int | float
    realtime: bool
    rewind: Any
    right: Any
    show: bool
    symbol: str
    symbolOffset: int | float
    symbolRotate: int | float
    symbolSize: int | float
    top: Any
    type: Literal['number', 'time']
    z: int | float
    zlevel: int | float


class TitleSubtextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class TitleTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class Title(TypedDict, total=False):
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    bottom: Any
    itemGap: int | float
    left: Any
    link: Any
    padding: Any
    right: Any
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    show: bool
    sublink: Any
    subtarget: Any
    subtext: Any
    subtextStyle: TitleSubtextstyle
    target: Any
    text: Any
    textStyle: TitleTextstyle
    top: Any
    z: int | float
    zlevel: int | float


class ToolboxFeatureDataviewIconstyleEmphasis(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class ToolboxFeatureDataviewIconstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class ToolboxFeatureDataviewIconstyle(TypedDict, total=False):
    emphasis: ToolboxFeatureDataviewIconstyleEmphasis
    normal: ToolboxFeatureDataviewIconstyleNormal


class ToolboxFeatureDataview(TypedDict, total=False):
    backgroundColor: str
    buttonColor: str
    buttonTextColor: str
    icon: Any
    iconStyle: ToolboxFeatureDataviewIconstyle
    lang: Any
    readOnly: Any
    show: bool
    textColor: str
    textareaBorderColor: str
    textareaColor: str
    title: Any


class ToolboxFeatureDatazoomIcon(TypedDict, total=False):
    back: Any
    zoom: int | float


class ToolboxFeatureDatazoomIconstyleEmphasis(TypedDict, total=False):
    color: str


class ToolboxFeatureDatazoomIconstyleNormal(TypedDict, total=False):
    borderColor: str
    color: str
    shadowBlur: int | float


class ToolboxFeatureDatazoomIconstyle(TypedDict, total=False):
    emphasis: ToolboxFeatureDatazoomIconstyleEmphasis
    normal: ToolboxFeatureDatazoomIconstyleNormal


class ToolboxFeatureDatazoomTitle(TypedDict, total=False):
    back: Any
    zoom: int | float


class ToolboxFeatureDatazoom(TypedDict, total=False):
    icon: ToolboxFeatureDatazoomIcon
    iconStyle: ToolboxFeatureDatazoomIconstyle
    show: bool
    title: ToolboxFeatureDatazoomTitle
    xAxisIndex: int | float
    yAxisIndex: int | float


class ToolboxFeatureMagictypeIcon(TypedDict, total=False):
    bar: Any
    line: Any
    stack: str
    tiled: Any


class ToolboxFeatureMagictypeIconstyleEmphasis(TypedDict, total=False):
    borderColor: str
    opacity: int | float
    shadowBlur: int | float


class ToolboxFeatureMagictypeIconstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float


class ToolboxFeatureMagictypeIconstyle(TypedDict, total=False):
    emphasis: ToolboxFeatureMagictypeIconstyleEmphasis
    normal: ToolboxFeatureMagictypeIconstyleNormal


class ToolboxFeatureMagictypeOption(TypedDict, total=False):
    bar: Any
    line: Any
    stack: str
    tiled: Any


class ToolboxFeatureMagictypeSeriesindex(TypedDict, total=False):
    bar: Any
    line: Any
    stack: str
    tiled: Any


class ToolboxFeatureMagictypeTitle(TypedDict, total=False):
    bar: Any
    line: Any
    stack: str
    tiled: Any


class ToolboxFeatureMagictype(TypedDict, total=False):
    icon: ToolboxFeatureMagictypeIcon
    iconStyle: ToolboxFeatureMagictypeIconstyle
    option: ToolboxFeatureMagictypeOption
    seriesIndex: ToolboxFeatureMagictypeSeriesindex
    show: bool
    title: ToolboxFeatureMagictypeTitle
    type: Literal['line', 'bar', 'stack', 'tiled']


class ToolboxFeatureRestoreIconstyleEmphasis(TypedDict, total=False):
    borderColor: str
    color: str
    shadowBlur: int | float


class ToolboxFeatureRestoreIconstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class ToolboxFeatureRestoreIconstyle(TypedDict, total=False):
    emphasis: ToolboxFeatureRestoreIconstyleEmphasis
    normal: ToolboxFeatureRestoreIconstyleNormal


class ToolboxFeatureRestore(TypedDict, total=False):
    icon: Any
    iconStyle: ToolboxFeatureRestoreIconstyle
    show: bool
    title: Any


class ToolboxFeatureSaveasimageIconstyleEmphasis(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class ToolboxFeatureSaveasimageIconstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class ToolboxFeatureSaveasimageIconstyle(TypedDict, total=False):
    emphasis: ToolboxFeatureSaveasimageIconstyleEmphasis
    normal: ToolboxFeatureSaveasimageIconstyleNormal


class ToolboxFeatureSaveasimage(TypedDict, total=False):
    backgroundColor: str
    excludeComponents: Any
    icon: Any
    iconStyle: ToolboxFeatureSaveasimageIconstyle
    name: str
    pixelRatio: Any
    show: bool
    title: Any
    type: Literal['png', 'jpeg', 'gif', 'svg', 'auto']


class ToolboxFeature(TypedDict, total=False):
    dataView: ToolboxFeatureDataview
    dataZoom: ToolboxFeatureDatazoom
    magicType: ToolboxFeatureMagictype
    restore: ToolboxFeatureRestore
    saveAsImage: ToolboxFeatureSaveasimage


class ToolboxIconstyleEmphasis(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class ToolboxIconstyleNormal(TypedDict, total=False):
    borderColor: str
    borderWidth: int | float
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class ToolboxIconstyle(TypedDict, total=False):
    emphasis: ToolboxIconstyleEmphasis
    normal: ToolboxIconstyleNormal


class Toolbox(TypedDict, total=False):
    bottom: Any
    feature: ToolboxFeature
    height: int | float
    iconStyle: ToolboxIconstyle
    itemGap: int | float
    itemSize: int | float
    left: Any
    orient: Literal['horizontal', 'vertical']
    right: Any
    show: bool
    showTitle: bool
    top: Any
    width: int | float
    z: int | float
    zlevel: int | float


class TooltipAxispointerCrossstyleTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class TooltipAxispointerCrossstyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    textStyle: TooltipAxispointerCrossstyleTextstyle
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class TooltipAxispointerLinestyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class TooltipAxispointerShadowstyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class TooltipAxispointer(TypedDict, total=False):
    animation: bool
    animationDuration: bool
    animationDurationUpdate: bool
    animationEasing: str
    animationEasingUpdate: str
    axis: Any
    crossStyle: TooltipAxispointerCrossstyle
    lineStyle: TooltipAxispointerLinestyle
    shadowStyle: TooltipAxispointerShadowstyle
    type: Literal['line', 'shadow', 'cross', 'none']


class TooltipTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class Tooltip(TypedDict, total=False):
    alwaysShowContent: bool
    axisPointer: TooltipAxispointer
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    enterable: Any
    formatter: Any
    hideDelay: Any
    padding: Any
    position: str
    show: bool
    showContent: bool
    textStyle: TooltipTextstyle
    transitionDuration: Any
    trigger: Literal['item', 'axis', 'none']
    triggerOn: Literal['mousemove', 'click', 'none', 'mousemove|click']


class Visualmap(TypedDict, total=False):
    pass


class VisualmapContinuousTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class VisualmapContinuous(TypedDict, total=False):
    align: Literal["auto", "left", "right"]
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    bottom: Any
    calculable: Any
    color: str | list[str]
    dimension: Any
    formatter: Any
    handlePosition: Literal['left', 'right']
    inRange: Any
    inverse: bool
    itemHeight: int | float
    itemWidth: int | float
    left: Any
    max: int | float
    min: int | float
    orient: Literal['horizontal', 'vertical']
    outOfRange: Any
    padding: Any
    precision: int | float
    realtime: bool
    right: Any
    seriesIndex: int | float
    show: bool
    text: Any
    textGap: int | float
    textStyle: VisualmapContinuousTextstyle
    top: Any
    type: Literal['continuous']
    z: int | float
    zlevel: int | float


class VisualmapPiecewiseTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class VisualmapPiecewise(TypedDict, total=False):
    align: Literal["auto", "left", "right"]
    backgroundColor: str
    borderColor: str
    borderWidth: int | float
    bottom: Any
    categories: Any
    color: str
    dimension: Any
    formatter: Any
    inRange: Any
    inverse: bool
    itemGap: int | float
    itemHeight: int | float
    itemSymbol: str
    itemWidth: int | float
    left: Any
    max: int | float
    min: int | float
    orient: Literal['horizontal', 'vertical']
    outOfRange: Any
    padding: Any
    pieces: Any
    precision: int | float
    right: Any
    selectedMode: Literal['multiple', 'single', 'series'] | bool
    seriesIndex: int | float
    show: bool
    splitNumber: Any
    text: Any
    textGap: int | float
    textStyle: VisualmapPiecewiseTextstyle
    top: Any
    type: Literal['piecewise']
    z: int | float
    zlevel: int | float


class XaxisAxislabelTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class XaxisAxislabel(TypedDict, total=False):
    formatter: Any
    inside: bool
    interval: int | float
    margin: int | float
    rotate: int | float
    show: bool
    textStyle: XaxisAxislabelTextstyle


class XaxisAxislineLinestyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class XaxisAxisline(TypedDict, total=False):
    lineStyle: XaxisAxislineLinestyle
    onZero: int | float
    show: bool


class XaxisAxistickLinestyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class XaxisAxistick(TypedDict, total=False):
    inside: bool
    interval: int | float
    length: int | float
    lineStyle: XaxisAxistickLinestyle
    show: bool


class XaxisDataTextstyle(TypedDict, total=False):
    align: Literal['left', 'center', 'right', 'auto']
    baseline: Literal['top', 'middle', 'bottom']
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class XaxisData(TypedDict, total=False):
    textStyle: XaxisDataTextstyle
    value: Any


class XaxisNametextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class XaxisSplitareaAreastyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class XaxisSplitarea(TypedDict, total=False):
    areaStyle: XaxisSplitareaAreastyle
    interval: int | float
    show: bool


class XaxisSplitlineLinestyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class XaxisSplitline(TypedDict, total=False):
    interval: int | float
    lineStyle: XaxisSplitlineLinestyle
    show: bool


class Xaxis(TypedDict, total=False):
    axisLabel: XaxisAxislabel
    axisLine: XaxisAxisline
    axisTick: XaxisAxistick
    boundaryGap: int | float
    data: XaxisData
    gridIndex: int | float
    interval: int | float
    inverse: bool
    max: int | float
    min: int | float
    name: str
    nameGap: int | float
    nameLocation: Literal['start', 'middle', 'end']
    nameTextStyle: XaxisNametextstyle
    position: str
    scale: bool
    splitArea: XaxisSplitarea
    splitLine: XaxisSplitline
    splitNumber: Any
    type: Literal['value', 'category', 'time', 'log']


class YaxisAxislabelTextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class YaxisAxislabel(TypedDict, total=False):
    formatter: Any
    inside: bool
    interval: int | float
    margin: int | float
    rotate: int | float
    show: bool
    textStyle: YaxisAxislabelTextstyle


class YaxisAxislineLinestyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class YaxisAxisline(TypedDict, total=False):
    lineStyle: YaxisAxislineLinestyle
    onZero: int | float
    show: bool


class YaxisAxistickLinestyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class YaxisAxistick(TypedDict, total=False):
    inside: bool
    interval: int | float
    length: int | float
    lineStyle: YaxisAxistickLinestyle
    show: bool


class YaxisDataTextstyle(TypedDict, total=False):
    align: Literal['left', 'center', 'right', 'auto']
    baseline: Literal['top', 'middle', 'bottom']
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class YaxisData(TypedDict, total=False):
    textStyle: YaxisDataTextstyle
    value: Any


class YaxisNametextstyle(TypedDict, total=False):
    color: str
    fontFamily: str
    fontSize: int | float
    fontStyle: Literal['normal', 'italic', 'oblique']
    fontWeight: Literal['normal', 'bold', 'bolder', 'lighter']


class YaxisSplitareaAreastyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float


class YaxisSplitarea(TypedDict, total=False):
    areaStyle: YaxisSplitareaAreastyle
    interval: int | float
    show: bool


class YaxisSplitlineLinestyle(TypedDict, total=False):
    color: str
    opacity: int | float
    shadowBlur: int | float
    shadowColor: str
    shadowOffsetX: int | float
    shadowOffsetY: int | float
    type: Literal['solid', 'dashed', 'dotted']
    width: int | float


class YaxisSplitline(TypedDict, total=False):
    interval: int | float
    lineStyle: YaxisSplitlineLinestyle
    show: bool


class Yaxis(TypedDict, total=False):
    axisLabel: YaxisAxislabel
    axisLine: YaxisAxisline
    axisTick: YaxisAxistick
    boundaryGap: int | float
    data: YaxisData
    gridIndex: int | float
    interval: int | float
    inverse: bool
    max: int | float
    min: int | float
    name: str
    nameGap: int | float
    nameLocation: Literal['start', 'middle', 'end']
    nameTextStyle: YaxisNametextstyle
    position: str
    scale: bool
    splitArea: YaxisSplitarea
    splitLine: YaxisSplitline
    splitNumber: Any
    type: Literal['value', 'category', 'time', 'log']


class Option(TypedDict, total=False):
    dataZoom: Union[DatazoomInside, DatazoomSlider] | List[Union[DatazoomInside, DatazoomSlider]]
    series: List[Union[SeriesBar, SeriesBoxplot, SeriesCandlestick, SeriesEffectscatter, SeriesFunnel, SeriesGauge, SeriesGraph, SeriesHeatmap, SeriesLine, SeriesLines, SeriesMap, SeriesParallel, SeriesPie, SeriesSankey, SeriesScatter, SeriesTreemap]]
    visualMap: Union[VisualmapContinuous, VisualmapPiecewise] | List[Union[VisualmapContinuous, VisualmapPiecewise]]
    angleaxis: Angleaxis
    angleaxisaxislabel: AngleaxisAxislabel
    angleaxisaxislabeltextstyle: AngleaxisAxislabelTextstyle
    angleaxisaxisline: AngleaxisAxisline
    angleaxisaxislinelinestyle: AngleaxisAxislineLinestyle
    angleaxisaxistick: AngleaxisAxistick
    angleaxisaxisticklinestyle: AngleaxisAxistickLinestyle
    angleaxisdata: AngleaxisData
    angleaxisdatatextstyle: AngleaxisDataTextstyle
    angleaxissplitarea: AngleaxisSplitarea
    angleaxissplitareaareastyle: AngleaxisSplitareaAreastyle
    angleaxissplitline: AngleaxisSplitline
    angleaxissplitlinelinestyle: AngleaxisSplitlineLinestyle
    animation: Animation
    animationduration: Animationduration
    animationdurationupdate: Animationdurationupdate
    animationeasing: Animationeasing
    animationeasingupdate: Animationeasingupdate
    backgroundcolor: Backgroundcolor
    color: Color
    geo: Geo
    geoitemstyle: GeoItemstyle
    geoitemstyleemphasis: GeoItemstyleEmphasis
    geoitemstylenormal: GeoItemstyleNormal
    geolabel: GeoLabel
    geolabelemphasis: GeoLabelEmphasis
    geolabelemphasistextstyle: GeoLabelEmphasisTextstyle
    geolabelnormal: GeoLabelNormal
    geolabelnormaltextstyle: GeoLabelNormalTextstyle
    grid: Grid
    legend: Legend
    legenddata: LegendData
    legendtextstyle: LegendTextstyle
    parallel: Parallel
    parallelparallelaxisdefault: ParallelParallelaxisdefault
    parallelparallelaxisdefaultaxislabel: ParallelParallelaxisdefaultAxislabel
    parallelparallelaxisdefaultaxislabeltextstyle: ParallelParallelaxisdefaultAxislabelTextstyle
    parallelparallelaxisdefaultaxisline: ParallelParallelaxisdefaultAxisline
    parallelparallelaxisdefaultaxislinelinestyle: ParallelParallelaxisdefaultAxislineLinestyle
    parallelparallelaxisdefaultaxistick: ParallelParallelaxisdefaultAxistick
    parallelparallelaxisdefaultaxisticklinestyle: ParallelParallelaxisdefaultAxistickLinestyle
    parallelparallelaxisdefaultdata: ParallelParallelaxisdefaultData
    parallelparallelaxisdefaultdatatextstyle: ParallelParallelaxisdefaultDataTextstyle
    parallelparallelaxisdefaultnametextstyle: ParallelParallelaxisdefaultNametextstyle
    parallelaxis: Parallelaxis
    parallelaxisareaselectstyle: ParallelaxisAreaselectstyle
    parallelaxisaxislabel: ParallelaxisAxislabel
    parallelaxisaxislabeltextstyle: ParallelaxisAxislabelTextstyle
    parallelaxisaxisline: ParallelaxisAxisline
    parallelaxisaxislinelinestyle: ParallelaxisAxislineLinestyle
    parallelaxisaxistick: ParallelaxisAxistick
    parallelaxisaxisticklinestyle: ParallelaxisAxistickLinestyle
    parallelaxisdata: ParallelaxisData
    parallelaxisdatatextstyle: ParallelaxisDataTextstyle
    parallelaxisnametextstyle: ParallelaxisNametextstyle
    polar: Polar
    radiusaxis: Radiusaxis
    radiusaxisaxislabel: RadiusaxisAxislabel
    radiusaxisaxislabeltextstyle: RadiusaxisAxislabelTextstyle
    radiusaxisaxisline: RadiusaxisAxisline
    radiusaxisaxislinelinestyle: RadiusaxisAxislineLinestyle
    radiusaxisaxistick: RadiusaxisAxistick
    radiusaxisaxisticklinestyle: RadiusaxisAxistickLinestyle
    radiusaxisdata: RadiusaxisData
    radiusaxisdatatextstyle: RadiusaxisDataTextstyle
    radiusaxisnametextstyle: RadiusaxisNametextstyle
    radiusaxissplitarea: RadiusaxisSplitarea
    radiusaxissplitareaareastyle: RadiusaxisSplitareaAreastyle
    radiusaxissplitline: RadiusaxisSplitline
    radiusaxissplitlinelinestyle: RadiusaxisSplitlineLinestyle
    textstyle: Textstyle
    timeline: Timeline
    timelinecheckpointstyle: TimelineCheckpointstyle
    timelinecontrolstyle: TimelineControlstyle
    timelinecontrolstyleemphasis: TimelineControlstyleEmphasis
    timelinecontrolstylenormal: TimelineControlstyleNormal
    timelineitemstyle: TimelineItemstyle
    timelineitemstyleemphasis: TimelineItemstyleEmphasis
    timelineitemstylenormal: TimelineItemstyleNormal
    timelinelabel: TimelineLabel
    timelinelabelemphasis: TimelineLabelEmphasis
    timelinelabelemphasistextstyle: TimelineLabelEmphasisTextstyle
    timelinelabelnormal: TimelineLabelNormal
    timelinelabelnormaltextstyle: TimelineLabelNormalTextstyle
    timelinelinestyle: TimelineLinestyle
    title: Title
    titlesubtextstyle: TitleSubtextstyle
    titletextstyle: TitleTextstyle
    toolbox: Toolbox
    toolboxfeature: ToolboxFeature
    toolboxfeaturedataview: ToolboxFeatureDataview
    toolboxfeaturedataviewiconstyle: ToolboxFeatureDataviewIconstyle
    toolboxfeaturedataviewiconstyleemphasis: ToolboxFeatureDataviewIconstyleEmphasis
    toolboxfeaturedataviewiconstylenormal: ToolboxFeatureDataviewIconstyleNormal
    toolboxfeaturedatazoom: ToolboxFeatureDatazoom
    toolboxfeaturedatazoomicon: ToolboxFeatureDatazoomIcon
    toolboxfeaturedatazoomiconstyle: ToolboxFeatureDatazoomIconstyle
    toolboxfeaturedatazoomiconstyleemphasis: ToolboxFeatureDatazoomIconstyleEmphasis
    toolboxfeaturedatazoomiconstylenormal: ToolboxFeatureDatazoomIconstyleNormal
    toolboxfeaturedatazoomtitle: ToolboxFeatureDatazoomTitle
    toolboxfeaturemagictype: ToolboxFeatureMagictype
    toolboxfeaturemagictypeicon: ToolboxFeatureMagictypeIcon
    toolboxfeaturemagictypeiconstyle: ToolboxFeatureMagictypeIconstyle
    toolboxfeaturemagictypeiconstyleemphasis: ToolboxFeatureMagictypeIconstyleEmphasis
    toolboxfeaturemagictypeiconstylenormal: ToolboxFeatureMagictypeIconstyleNormal
    toolboxfeaturemagictypeoption: ToolboxFeatureMagictypeOption
    toolboxfeaturemagictypeseriesindex: ToolboxFeatureMagictypeSeriesindex
    toolboxfeaturemagictypetitle: ToolboxFeatureMagictypeTitle
    toolboxfeaturerestore: ToolboxFeatureRestore
    toolboxfeaturerestoreiconstyle: ToolboxFeatureRestoreIconstyle
    toolboxfeaturerestoreiconstyleemphasis: ToolboxFeatureRestoreIconstyleEmphasis
    toolboxfeaturerestoreiconstylenormal: ToolboxFeatureRestoreIconstyleNormal
    toolboxfeaturesaveasimage: ToolboxFeatureSaveasimage
    toolboxfeaturesaveasimageiconstyle: ToolboxFeatureSaveasimageIconstyle
    toolboxfeaturesaveasimageiconstyleemphasis: ToolboxFeatureSaveasimageIconstyleEmphasis
    toolboxfeaturesaveasimageiconstylenormal: ToolboxFeatureSaveasimageIconstyleNormal
    toolboxiconstyle: ToolboxIconstyle
    toolboxiconstyleemphasis: ToolboxIconstyleEmphasis
    toolboxiconstylenormal: ToolboxIconstyleNormal
    tooltip: Tooltip
    tooltipaxispointer: TooltipAxispointer
    tooltipaxispointercrossstyle: TooltipAxispointerCrossstyle
    tooltipaxispointercrossstyletextstyle: TooltipAxispointerCrossstyleTextstyle
    tooltipaxispointerlinestyle: TooltipAxispointerLinestyle
    tooltipaxispointershadowstyle: TooltipAxispointerShadowstyle
    tooltiptextstyle: TooltipTextstyle
    xaxis: Xaxis
    xaxisaxislabel: XaxisAxislabel
    xaxisaxislabeltextstyle: XaxisAxislabelTextstyle
    xaxisaxisline: XaxisAxisline
    xaxisaxislinelinestyle: XaxisAxislineLinestyle
    xaxisaxistick: XaxisAxistick
    xaxisaxisticklinestyle: XaxisAxistickLinestyle
    xaxisdata: XaxisData
    xaxisdatatextstyle: XaxisDataTextstyle
    xaxisnametextstyle: XaxisNametextstyle
    xaxissplitarea: XaxisSplitarea
    xaxissplitareaareastyle: XaxisSplitareaAreastyle
    xaxissplitline: XaxisSplitline
    xaxissplitlinelinestyle: XaxisSplitlineLinestyle
    yaxis: Yaxis
    yaxisaxislabel: YaxisAxislabel
    yaxisaxislabeltextstyle: YaxisAxislabelTextstyle
    yaxisaxisline: YaxisAxisline
    yaxisaxislinelinestyle: YaxisAxislineLinestyle
    yaxisaxistick: YaxisAxistick
    yaxisaxisticklinestyle: YaxisAxistickLinestyle
    yaxisdata: YaxisData
    yaxisdatatextstyle: YaxisDataTextstyle
    yaxisnametextstyle: YaxisNametextstyle
    yaxissplitarea: YaxisSplitarea
    yaxissplitareaareastyle: YaxisSplitareaAreastyle
    yaxissplitline: YaxisSplitline
    yaxissplitlinelinestyle: YaxisSplitlineLinestyle