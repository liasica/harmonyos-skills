---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll
title: Scroll
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 滚动与滑动 > Scroll
category: harmonyos-references
scraped_at: 2026-04-28T08:01:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:423c5f48fe89c7e7417fa11928e618d8c6badfd6877db8f5480ce64352664aaa
---

可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。

说明

* 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件嵌套List子组件滚动时，若List不设置宽高，则默认全部加载，在对性能有要求的场景下建议指定List的宽高，最佳实践请参考[懒加载优化性能-Scroll嵌套List导致按需加载失效](../best-practices/bpta-lazyforeach-optimization.md#section6296154115367)。
* 该组件滚动的前提是主轴方向大小小于内容大小。
* Scroll组件[通用属性clip](ts-universal-attributes-sharp-clipping.md#clip12)的默认值为true。
* Scroll组件的高度超出屏幕显示范围时，可以通过设置通用属性[layoutWeight](ts-universal-attributes-size.md#layoutweight)让Scroll高度适应主轴的剩余空间。
* 手指触摸屏幕时，会停止当前触摸范围内所有滚动组件的滚动动画（[scrollTo](ts-container-scroll.md#scrollto)和[scrollToIndex](ts-container-scroll.md#scrolltoindex)接口触发的滚动动画除外），包括边缘回弹动画。
* 组件内部已绑定手势实现跟手滚动等功能，需要增加自定义手势操作时请参考[手势拦截增强](ts-gesture-blocking-enhancement.md)进行处理。

## 子组件

PhonePC/2in1TabletTVWearable

支持单个子组件。

从API version 21开始，Scroll单个子组件的宽高最大为16777216px；API version 20及之前，Scroll单个子组件的宽高最大为1000000px。子组件超出该大小可能导致滚动或显示异常。

## 接口

PhonePC/2in1TabletTVWearable

Scroll(scroller?: Scroller)

创建Scroll滚动容器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scroller | [Scroller](ts-container-scroll.md#scroller) | 否 | 可滚动组件的控制器。用于与可滚动组件进行绑定。  **说明：**  不允许和其他滚动类组件，如：[ArcList](ts-container-arclist.md)、[List](ts-container-list.md)、[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)和[WaterFlow](ts-container-waterflow.md)绑定同一个滚动控制对象。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)和[滚动组件通用属性](ts-container-scrollable-common.md#属性)外，还支持以下属性：

### scrollable

PhonePC/2in1TabletTVWearable

scrollable(value: ScrollDirection)

设置滚动方向。该值被修改后会重置滚动偏移量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScrollDirection](ts-container-scroll.md#scrolldirection枚举说明) | 是 | 滚动方向。  默认值：ScrollDirection.Vertical |

当滚动方向设置为[ScrollDirection.FREE](ts-container-scroll.md#scrolldirection枚举说明)时，Scroll组件仅支持部分能力，见[自由滚动模式下支持的能力](ts-container-scroll.md#scrolldirection枚举说明)。

### scrollBar

PhonePC/2in1TabletTVWearable

scrollBar(barState: BarState)

设置滚动条状态。如果容器组件无法滚动，则滚动条不显示。如果容器组件的子组件大小为无穷大，则滚动条不支持拖动和伴随滚动。

从API version 10开始，当滚动组件存在圆角时，为避免滚动条被圆角截断，滚动条会自动计算距顶部和底部的避让距离。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| barState | [BarState](ts-appendix-enums.md#barstate) | 是 | 滚动条状态。  默认值：BarState.Auto |

### scrollBarColor

PhonePC/2in1TabletTVWearable

scrollBarColor(color: Color | number | string)

设置滚动条的颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Color](ts-appendix-enums.md#color) | number | string | 是 | 滚动条的颜色。  默认值：'#66182431'  number为HEX格式颜色，支持rgb或者argb，示例：0xffffff。  string为rgb或者argb格式颜色，示例：'#ffffff'。 |

### scrollBarColor22+

PhonePC/2in1TabletTVWearable

scrollBarColor(color: Color | number | string | Resource)

设置滚动条的颜色。与[scrollBarColor](ts-container-scroll.md#scrollbarcolor)相比，color参数开始支持Resource类型。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Color](ts-appendix-enums.md#color) | number | string | [Resource](ts-types.md#resource) | 是 | 滚动条的颜色。  默认值：'#66182431'  number为HEX格式颜色，支持rgb或者argb，示例：0xffffff。string为rgb或者argb格式颜色，示例：'#ffffff'。 |

### scrollBarWidth

PhonePC/2in1TabletTVWearable

scrollBarWidth(value: number | string)

设置滚动条的宽度，不支持百分比设置。宽度设置后，滚动条正常状态和按压状态宽度均为滚动条的宽度值。如果滚动条的宽度超过Scroll组件主轴方向的高度，则滚动条的宽度会变为默认值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 滚动条的宽度。  默认值：4  单位：vp  取值范围：设置为小于0的值时，按默认值处理。设置为0时，不显示滚动条。 |

### scrollSnap10+

PhonePC/2in1TabletTVWearable

scrollSnap(value: ScrollSnapOptions)

设置Scroll组件的限位滚动模式。

限位动画期间[onWillScroll](ts-container-scroll.md#onwillscroll12)事件上报的滚动操作来源类型为ScrollSource.FLING。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScrollSnapOptions](ts-container-scroll.md#scrollsnapoptions10对象说明) | 是 | Scroll组件的限位滚动模式。 |

### edgeEffect

PhonePC/2in1TabletTVWearable

edgeEffect(edgeEffect: EdgeEffect, options?: EdgeEffectOptions)

设置边缘滑动效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| edgeEffect | [EdgeEffect](ts-appendix-enums.md#edgeeffect) | 是 | Scroll组件的边缘滑动效果，支持弹簧效果和阴影效果。  默认值：EdgeEffect.None |
| options11+ | [EdgeEffectOptions](ts-container-scrollable-common.md#edgeeffectoptions11对象说明) | 否 | 组件内容大小小于组件自身时，是否开启滑动效果。设置为{ alwaysEnabled: true }会开启滑动效果，{ alwaysEnabled: false }不开启。  默认值：{ alwaysEnabled: true } |

### enableScrollInteraction10+

PhonePC/2in1TabletTVWearable

enableScrollInteraction(value: boolean)

设置是否支持滚动手势。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否支持滚动手势。设置为true时可以通过手指或者鼠标滚动，设置为false时无法通过手指或者鼠标滚动，但不影响控制器[Scroller](ts-container-scroll.md#scroller)的滚动接口。  默认值：true |

说明

组件无法通过鼠标按下拖动操作进行滚动。

### nestedScroll10+

PhonePC/2in1TabletTVWearable

nestedScroll(value: NestedScrollOptions)

设置前后两个方向的嵌套滚动模式，实现与父组件的滚动联动。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NestedScrollOptions](ts-container-scrollable-common.md#nestedscrolloptions10对象说明) | 是 | 嵌套滚动选项。  默认值：{ scrollForward: NestedScrollMode.SELF\_ONLY, scrollBackward: NestedScrollMode.SELF\_ONLY }  Scroll设置[enablePaging](ts-container-scroll.md#enablepaging11)或者[scrollSnap](ts-container-scroll.md#scrollsnap10)，并同时设置父组件优先的嵌套滚动时，嵌套滚动不生效。 |

### friction10+

PhonePC/2in1TabletTVWearable

friction(value: number | Resource)

设置摩擦系数，手动划动滚动区域时生效，仅影响惯性滚动过程，对惯性滚动过程中的链式效果有间接影响。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [Resource](ts-types.md#resource) | 是 | 摩擦系数。  默认值：非可穿戴设备为0.6，可穿戴设备为0.9。  从API version 11开始，非可穿戴设备默认值为0.7。  从API version 12开始，非可穿戴设备默认值为0.75。  取值范围：(0, +∞)，设置为小于等于0的值时，按默认值处理。 |

### enablePaging11+

PhonePC/2in1TabletTVWearable

enablePaging(value: boolean)

设置是否支持划动翻页。如果同时设置了划动翻页enablePaging和限位滚动scrollSnap，则scrollSnap优先生效，enablePaging不生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否支持划动翻页。设置为true支持滑动翻页，false不支持。  默认值：false |

### initialOffset12+

PhonePC/2in1TabletTVWearable

initialOffset(value: OffsetOptions)

设置初始滚动偏移量。只在首次布局时生效，后续动态修改该属性值不生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [OffsetOptions](ts-container-scroll.md#offsetoptions12对象说明) | 是 | 当输入的大小为百分比时，初始滚动偏移量为Scroll组件主轴方向大小与百分比数值之积。 |

### maxZoomScale20+

PhonePC/2in1TabletTVWearable

maxZoomScale(scale: number)

设置Scroll组件内容的最大手势缩放比例。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | number | 是 | Scroll组件内容的最大手势缩放比例。  默认值：1  取值范围：(0, +∞)，小于或等于0时按默认值1处理。 |

### minZoomScale20+

PhonePC/2in1TabletTVWearable

minZoomScale(scale: number)

设置Scroll组件内容的最小手势缩放比例。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | number | 是 | Scroll组件内容的最小手势缩放比例。  默认值：1  取值范围：(0, maxZoomScale]，小于或等于0时按默认值1处理，大于maxZoomScale时按maxZoomScale处理。 |

说明

当maxZoomScale和minZoomScale不同时为1时，Scroll组件会启用缩放手势。

### zoomScale20+

PhonePC/2in1TabletTVWearable

zoomScale(scale: number)

设置Scroll组件内容的缩放比例。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | number | 是 | 设置Scroll组件内容的缩放比例，该参数支持[!!](../harmonyos-guides/arkts-new-binding.md)双向绑定变量。  默认值：1  取值范围：(0, +∞)，小于或等于0时按默认值1处理。 |

### enableBouncesZoom20+

PhonePC/2in1TabletTVWearable

enableBouncesZoom(enable: boolean)

启用过缩放回弹效果。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 启用过缩放回弹效果。设置为true表示启用该效果，设置为false表示禁用该效果。  默认值：true |

## ScrollDirection枚举说明

PhonePC/2in1TabletTVWearable

滚动方向枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Vertical | 0 | 仅支持竖直方向滚动。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Horizontal | 1 | 仅支持水平方向滚动。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Free(deprecated) | 2 | 支持竖直或水平方向滚动。  **说明：** 从API version 7开始支持，从API version 9开始废弃，建议使用FREE替代。FREE枚举值从API version 20开始支持。 |
| None | 3 | 不可滚动。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| FREE20+ | 4 | 自由滚动。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

FREE（自由滚动）模式下支持的能力：

| **支持的属性** | **支持的事件** | **支持的[Scroller](ts-container-scroll.md#scroller)接口** |
| --- | --- | --- |
| [scrollBar](ts-container-scroll.md#scrollbar) | [onWillScroll](ts-container-scroll.md#onwillscroll12) | [scrollTo](ts-container-scroll.md#scrollto) |
| [scrollBarColor](ts-container-scroll.md#scrollbarcolor) | [onDidScroll](ts-container-scroll.md#ondidscroll12) | [scrollEdge](ts-container-scroll.md#scrolledge) |
| [scrollBarWidth](ts-container-scroll.md#scrollbarwidth) | [onScrollEdge](ts-container-scroll.md#onscrolledge) | [scrollPage](ts-container-scroll.md#scrollpage9) |
| [scrollBarMargin](ts-container-scrollable-common.md#scrollbarmargin20) | [onScrollStart](ts-container-scroll.md#onscrollstart9) | [currentOffset](ts-container-scroll.md#currentoffset) |
| [edgeEffect](ts-container-scroll.md#edgeeffect) | [onScrollStop](ts-container-scroll.md#onscrollstop9) | [offset](ts-container-scroll.md#offset23) |
| [enableScrollInteraction](ts-container-scroll.md#enablescrollinteraction10) | - | [scrollBy](ts-container-scroll.md#scrollby9) |
| [friction](ts-container-scroll.md#friction10) | - | [getItemRect](ts-container-scroll.md#getitemrect11) |
| [clipContent](ts-container-scrollable-common.md#clipcontent14) | - | - |
| [initialOffset](ts-container-scroll.md#initialoffset12) | - | - |
| [scrollable](ts-container-scroll.md#scrollable) | - | - |

说明

* edgeEffect属性仅支持Spring和None边缘滑动效果。
* onWillScroll回调仅支持在跟手滑动阶段重载偏移量。
* onScrollEdge回调只在到达边缘时触发一次，回弹后不会重复触发。
* 在抛滑动画过程中切换边缘模式不会打断动画。

## ScrollSnapOptions10+对象说明

PhonePC/2in1TabletTVWearable

限位滚动模式对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| snapAlign | [ScrollSnapAlign](ts-container-list.md#scrollsnapalign10枚举说明) | 否 | 否 | 设置Scroll组件限位滚动时的对齐方式。  **说明：**  1.该属性默认值为ScrollSnapAlign.NONE。 |
| snapPagination | [Dimension](ts-types.md#dimension10) | Array<Dimension> | 否 | 是 | 设置Scroll组件限位滚动时的分页点。  **说明：**  1.当属性为Dimension时，Dimension表示每页的大小，系统按照该大小进行分页。  2.当属性为Array<Dimension>时，每个Dimension表示分页点，系统按照分页点进行分页。每个Dimension的范围为[0,可滑动距离]。  3.当该属性不填或者Dimension为小于等于0的输入时，按异常值，无限位滚动处理。当该属性值为Array<Dimension>数组时，数组中的数值必须为单调递增。  4.当输入为百分比时，实际的大小为Scroll组件的视口与百分比数值之积。 |
| enableSnapToStart | boolean | 否 | 是 | 在Scroll组件限位滚动模式下，该属性设置为true后，不允许Scroll在开头和第一页间自由滑动，该属性设置为false后，允许Scroll在开头和第一页间自由滑动。  **说明：**  1.该属性值默认为true。  2.该属性仅当snapPagination属性为Array<Dimension>时生效，不支持Dimension。 |
| enableSnapToEnd | boolean | 否 | 是 | 在Scroll组件限位滚动模式下，该属性设置为true后，不允许Scroll在最后一页和末尾间自由滑动，该属性设置为false后，允许Scroll在最后一页和末尾间自由滑动。  **说明：**  1.该属性值默认为true。  2.该属性仅当snapPagination属性为Array<Dimension>时生效，不支持Dimension。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)和[滚动组件通用事件](ts-container-scrollable-common.md#事件)外，还支持以下事件：

说明

不支持滚动组件通用事件中的[onWillScroll](ts-container-scrollable-common.md#onwillscroll12)、[onDidScroll](ts-container-scrollable-common.md#ondidscroll12)事件。

### onScrollFrameBegin9+

PhonePC/2in1TabletTVWearable

onScrollFrameBegin(event: OnScrollFrameBeginCallback)

该接口回调时，事件参数传入即将发生的滚动量，事件处理函数中可根据应用场景计算实际需要的滚动量并作为事件处理函数的返回值返回，Scroll将按照返回值的实际滚动量进行滚动。

支持[offsetRemain](ts-container-scroll.md#onscrollframebeginhandlerresult18对象说明)为负值。

若通过onScrollFrameBegin事件和[scrollBy](ts-container-scroll.md#scrollby9)方法实现容器嵌套滚动，需设置子滚动节点的[EdgeEffect](ts-container-scroll.md#edgeeffect)为None。如Scroll嵌套List滚动时，List组件的[edgeEffect](ts-container-list.md#edgeeffect)属性需设置为EdgeEffect.None，否则抛滑List，会触发List的边缘回弹动画，导致嵌套滚动失效。

满足以下任一条件时触发该事件：

1. 用户交互（如手指滑动、键鼠操作等）触发滚动。
2. Scroll惯性滚动。
3. 调用[fling](ts-container-scroll.md#fling12)接口触发滚动。

不触发该事件的条件：

1. 调用除[fling](ts-container-scroll.md#fling12)接口外的其他滚动控制接口。
2. 越界回弹。
3. 拖动滚动条。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [OnScrollFrameBeginCallback](ts-container-scroll.md#onscrollframebegincallback18) | 是 | 每帧滚动开始回调函数。 |

### onScroll(deprecated)

PhonePC/2in1TabletTVWearable

onScroll(event: (xOffset: number, yOffset: number) => void)

滚动事件回调，返回滚动时水平、竖直方向偏移量，单位vp。

触发该事件的条件：

1、滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。

2、通过滚动控制器API接口调用。

3、越界回弹。

说明

从API version 7开始支持，从API version 12开始废弃，建议使用[onWillScroll](ts-container-scroll.md#onwillscroll12)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| xOffset | number | 是 | 相对于上一帧水平方向的偏移量，Scroll中的内容向左滚动时偏移量为正，向右滚动时偏移量为负。  单位vp。 |
| yOffset | number | 是 | 相对于上一帧竖直方向的偏移量，Scroll中的内容向上滚动时偏移量为正，向下滚动时偏移量为负。  单位vp。 |

### onWillScroll12+

PhonePC/2in1TabletTVWearable

onWillScroll(handler: ScrollOnWillScrollCallback)

滚动事件回调，Scroll滚动前触发。

回调当前帧将要滚动的偏移量和当前滚动状态和滚动操作来源，其中回调的偏移量为计算得到的将要滚动的偏移量值，并非最终实际滚动偏移。可以通过该回调返回值指定Scroll将要滚动的偏移。

触发该事件的条件：

1、滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。

2、通过滚动控制器API接口调用。

3、越界回弹。

说明

滚动事件的回调函数在滚动过程中会被频繁触发，因此应避免在该回调函数中执行耗时操作，以防止应用出现卡顿和丢帧的问题。最佳实践请参考[主线程耗时操作优化指导-高频回调场景](../best-practices/bpta-time-optimization-of-the-main-thread.md#section10112623611)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [ScrollOnWillScrollCallback](ts-container-scroll.md#scrollonwillscrollcallback12) | 是 | Scroll滚动前触发的回调。 |

### onDidScroll12+

PhonePC/2in1TabletTVWearable

onDidScroll(handler: ScrollOnScrollCallback)

滚动事件回调，Scroll滚动时触发。

返回当前帧滚动的偏移量和当前滚动状态。

触发该事件的条件：

1、滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。

2、通过滚动控制器API接口调用。

3、越界回弹。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [ScrollOnScrollCallback](ts-container-scroll.md#scrollonscrollcallback12) | 是 | Scroll滚动时触发的回调。 |

### onScrollEdge

PhonePC/2in1TabletTVWearable

onScrollEdge(event: OnScrollEdgeCallback)

滚动到边缘事件回调。

触发该事件的条件：

1、滚动组件滚动到边缘时触发，支持键鼠操作等其他触发滚动的输入设置。

2、通过滚动控制器API接口调用。

3、越界回弹。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [OnScrollEdgeCallback](ts-container-scroll.md#onscrolledgecallback18) | 是 | 滚动到的边缘位置。  当Scroll设置为水平方向滚动时，上报[Edge.Center](ts-appendix-enums.md#edge)表示水平方向起始位置，上报[Edge.Baseline](ts-appendix-enums.md#edge)表示水平方向末尾位置。由于[Edge.Center](ts-appendix-enums.md#edge)和[Edge.Baseline](ts-appendix-enums.md#edge)枚举值已经废弃，推荐使用[onReachStart](ts-container-scrollable-common.md#onreachstart11)、[onReachEnd](ts-container-scrollable-common.md#onreachend11)事件监听是否滚动到边界。 |

### onScrollEnd(deprecated)

PhonePC/2in1TabletTVWearable

onScrollEnd(event: () => void)

滚动停止事件回调。

触发该事件的条件：

1、滚动组件触发滚动后停止，支持键鼠操作等其他触发滚动的输入设置。

2、通过滚动控制器API接口调用后停止，带过渡动效。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[onScrollStop](ts-container-scroll.md#onscrollstop9)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 滚动停止事件回调。 |

### onScrollStart9+

PhonePC/2in1TabletTVWearable

onScrollStart(event: VoidCallback)

滚动开始时触发。手指拖动Scroll或拖动Scroll的滚动条触发的滚动开始时，会触发该事件。使用[Scroller](ts-container-scroll.md#scroller)滚动控制器触发的带动画的滚动，动画开始时会触发该事件。

触发该事件的条件：

1、滚动组件开始滚动时触发，支持键鼠操作等其他触发滚动的输入设置。

2、通过滚动控制器API接口调用后开始，带过渡动效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](ts-types.md#voidcallback12) | 是 | 滚动开始回调。 |

### onScrollStop9+

PhonePC/2in1TabletTVWearable

onScrollStop(event: VoidCallback)

滚动停止时触发。手拖动Scroll或拖动Scroll的滚动条触发的滚动，手离开屏幕后滚动停止时会触发该事件。使用[Scroller](ts-container-scroll.md#scroller)滚动控制器触发的带动画的滚动，动画停止时会触发该事件。

触发该事件的条件：

1、滚动组件触发滚动后停止，支持键鼠操作等其他触发滚动的输入设置。

2、通过滚动控制器API接口调用后开始，带过渡动效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](ts-types.md#voidcallback12) | 是 | 滚动停止回调。 |

### onDidZoom20+

PhonePC/2in1TabletTVWearable

onDidZoom(event: ScrollOnDidZoomCallback)

每帧缩放完成时触发。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ScrollOnDidZoomCallback](ts-container-scroll.md#scrollondidzoomcallback20) | 是 | 每帧缩放完成时回调。 |

### onZoomStart20+

PhonePC/2in1TabletTVWearable

onZoomStart(event: VoidCallback)

手势缩放开始触发。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](ts-types.md#voidcallback12) | 是 | 缩放开始回调。 |

### onZoomStop20+

PhonePC/2in1TabletTVWearable

onZoomStop(event: VoidCallback)

手势缩放停止时触发。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](ts-types.md#voidcallback12) | 是 | 缩放停止回调。 |

## ScrollOnScrollCallback12+

PhonePC/2in1TabletTVWearable

type ScrollOnScrollCallback = (xOffset: number, yOffset: number, scrollState: ScrollState) => void

Scroll滚动时触发的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| xOffset | number | 是 | 相对于上一帧水平方向的偏移量，Scroll中的内容向左滚动时偏移量为正，向右滚动时偏移量为负。  单位vp。 |
| yOffset | number | 是 | 相对于上一帧竖直方向的偏移量，Scroll中的内容向上滚动时偏移量为正，向下滚动时偏移量为负。  单位vp。 |
| scrollState | [ScrollState](ts-container-list.md#scrollstate枚举说明) | 是 | 当前滚动状态。 |

说明

若通过[onScrollFrameBegin](ts-container-scroll.md#onscrollframebegin9)事件和[scrollBy](ts-container-scroll.md#scrollby9)方法实现容器嵌套滚动，需设置子滚动节点的EdgeEffect为None。如Scroll嵌套List滚动时，List组件的[edgeEffect](ts-container-list.md#edgeeffect)属性需设置为EdgeEffect.None。

## ScrollOnWillScrollCallback12+

PhonePC/2in1TabletTVWearable

type ScrollOnWillScrollCallback = (xOffset: number, yOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => void | OffsetResult

Scroll滚动前触发的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| xOffset | number | 是 | 相对于上一帧水平方向的偏移量，Scroll中的内容向左滚动时偏移量为正，向右滚动时偏移量为负。  单位vp。 |
| yOffset | number | 是 | 相对于上一帧竖直方向的偏移量，Scroll中的内容向上滚动时偏移量为正，向下滚动时偏移量为负。  单位vp。 |
| scrollState | [ScrollState](ts-container-list.md#scrollstate枚举说明) | 是 | 当前滚动状态。 |
| scrollSource | [ScrollSource](ts-appendix-enums.md#scrollsource12) | 是 | 当前滚动操作的来源。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| void | [OffsetResult](ts-container-scroll.md#offsetresult11对象说明) | 返回OffsetResult时按照开发者指定的偏移量滚动；不返回时按回调参数(xOffset, yOffset)滚动。 |

## OnScrollEdgeCallback18+

PhonePC/2in1TabletTVWearable

type OnScrollEdgeCallback = (side: Edge) => void

滚动到边缘时触发的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| side | [Edge](ts-appendix-enums.md#edge) | 是 | 滚动到的边缘位置。 |

## OnScrollFrameBeginCallback18+

PhonePC/2in1TabletTVWearable

type OnScrollFrameBeginCallback = (offset: number, state: ScrollState) => OnScrollFrameBeginHandlerResult;

Scroll每帧滚动前触发的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 即将发生的滑动量，单位vp。 |
| state | [ScrollState](ts-container-list.md#scrollstate枚举说明) | 是 | 当前滑动状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [OnScrollFrameBeginHandlerResult](ts-container-scroll.md#onscrollframebeginhandlerresult18对象说明) | 返回实际滑动量。 |

## OnScrollFrameBeginHandlerResult18+对象说明

PhonePC/2in1TabletTVWearable

[OnScrollFrameBeginCallback](ts-container-scroll.md#onscrollframebegincallback18)返回的实际相对上一帧滚动偏移量。

说明

为规范匿名对象的定义，API version 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offsetRemain9+ | number | 否 | 否 | 实际相对上一帧的滚动偏移量。  单位vp。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## ScrollOnDidZoomCallback20+

PhonePC/2in1TabletTVWearable

type ScrollOnDidZoomCallback = (scale: number) => void

Scroll每帧缩放完成时触发的回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | number | 是 | 当前缩放倍数。 |

## Scroller

PhonePC/2in1TabletTVWearable

可滚动容器组件的控制器，可以将此组件绑定至容器组件，然后通过它控制容器组件的滚动。同一个控制器不可以控制多个容器组件，目前支持绑定到ArcList、ArcScrollBar、List、Scroll、ScrollBar、Grid、WaterFlow上。

说明

1、Scroller控制器与滚动容器组件的绑定发生在组件创建阶段。

2、Scroller控制器与滚动容器组件绑定后才可以正常调用Scroller方法，否则根据调用接口不同会不生效或者抛异常。

3、以[aboutToAppear](ts-custom-component-lifecycle.md#abouttoappear)为例，aboutToAppear在创建自定义组件的新实例后，在执行其build()方法之前执行。因此如果滚动组件在自定义组件build内，在该自定义组件aboutToAppear执行时，内部滚动组件还没有创建，是不能正常调用上述Scroller方法的。

4、以[onAppear](ts-universal-events-show-hide.md#onappear)为例，组件挂载显示后触发此回调。因此在滚动组件的onAppear回调执行时，滚动组件已经创建并已经和Scroller绑定成功，是可以正常调用Scroller方法的。

### 导入对象

```
1. scroller: Scroller = new Scroller();
```

### constructor

PhonePC/2in1TabletTVWearable

constructor()

Scroller的构造函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### scrollTo

PhonePC/2in1TabletTVWearable

scrollTo(options: ScrollOptions)

滑动到指定位置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ScrollOptions](ts-container-scroll.md#scrolloptions18对象说明) | 是 | 滑动到指定位置的参数。 |

说明

ScrollTo动画速度大于200vp/s时，滚动组件区域内的组件不响应点击事件。

### scrollEdge

PhonePC/2in1TabletTVWearable

scrollEdge(value: Edge, options?: ScrollEdgeOptions)

滚动到容器边缘，不区分滚动轴方向，Edge.Top和Edge.Start表现相同，Edge.Bottom和Edge.End表现相同。

Scroll组件默认有动画，Grid、List、WaterFlow组件默认无动画。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Edge](ts-appendix-enums.md#edge) | 是 | 滚动到的边缘位置。 |
| options12+ | [ScrollEdgeOptions](ts-container-scroll.md#scrolledgeoptions12对象说明) | 否 | 设置滚动到边缘位置的模式。 |

### fling12+

PhonePC/2in1TabletTVWearable

fling(velocity: number): void

滚动类组件根据传入的初始速度进行惯性滚动。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| velocity | number | 是 | 惯性滚动的初始速度值。单位：vp/s  **说明：**  velocity值设置为0，视为异常值，本次滚动不生效。如果值为正数，则向顶部滚动；如果值为负数，则向底部滚动。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[滚动类组件错误码](errorcode-scroll.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

### scrollPage9+

PhonePC/2in1TabletTVWearable

scrollPage(value: ScrollPageOptions)

滚动到下一页或者上一页。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScrollPageOptions](ts-container-scroll.md#scrollpageoptions14对象说明) | 是 | 设置翻页模式。 |

### scrollPage(deprecated)

PhonePC/2in1TabletTVWearable

scrollPage(value: { next: boolean, direction?: Axis })

滚动到下一页或者上一页。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[scrollPage9+](ts-container-scroll.md#scrollpage9)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| next | boolean | 是 | 是否向下翻页。true表示向下翻页，false表示向上翻页。 |
| direction | [Axis](ts-appendix-enums.md#axis) | 否 | 设置滚动方向为水平或竖直方向。 |

### currentOffset

PhonePC/2in1TabletTVWearable

currentOffset(): OffsetResult

获取当前的滚动总偏移量。

说明

1. 当Scroller没有和组件绑定时，该接口会返回undefined，但是接口中没有声明，推荐使用[offset](ts-container-scroll.md#offset23)函数。
2. Grid、List、WaterFlow组件有懒加载机制，组件内容没有加载并布局完成时，内容总偏移量通过估算得到，估算结果可能会有误差。其中List组件可以通过[childrenMainSize](ts-container-list.md#childrenmainsize12)属性解决估算不准确的问题，Grid与WaterFlow估算不准暂无解决方案。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [OffsetResult11+](ts-container-scroll.md#offsetresult11对象说明) | 返回当前的滚动总偏移量。 |

### offset23+

PhonePC/2in1TabletTVWearable

offset(): OffsetResult | undefined

获取当前的滚动总偏移量。除接口声明有undefined以外，其他与[currentOffset](ts-container-scroll.md#currentoffset)接口保持一致。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [OffsetResult](ts-container-scroll.md#offsetresult11对象说明) | undefined | 返回当前的滚动总偏移量。当Scroller没有和组件绑定时，该接口会返回undefined。 |

### scrollToIndex

PhonePC/2in1TabletTVWearable

scrollToIndex(value: number, smooth?: boolean, align?: ScrollAlign, options?: ScrollToIndexOptions)

滑动到指定Index，支持设置滑动额外偏移量。

开启smooth动效时，会对经过的所有item进行加载和布局计算，当大量加载item时会导致性能问题，建议先调用scrollToIndex不带动画跳转到目标附近位置，再调用scrollToIndex带动画滚动到目标位置。

说明

1.仅支持ArcList、Grid、List、WaterFlow组件。

2.在[LazyForEach](ts-rendering-control-lazyforeach.md)、[ForEach](ts-rendering-control-foreach.md)、[Repeat](ts-rendering-control-repeat.md)刷新数据源时，需确保在数据刷新完成之后再调用此接口。

3.从API version 11开始，在List中支持[contentStartOffset](ts-container-list.md#contentstartoffset11)和[contentEndOffset](ts-container-list.md#contentendoffset11)。从API version 22开始，在Grid和Waterflow组件中支持设置[contentStartOffset](ts-container-scrollable-common.md#contentstartoffset22)和[contentEndOffset](ts-container-scrollable-common.md#contentendoffset22)。

* 当滚动容器组件设置contentStartOffset时，如果ScrollAlign设置为START，滚动结束时，指定item首部会与滚动容器组件contentStartOffset处对齐。
* 当滚动容器组件设置contentEndOffset时，如果ScrollAlign设置为END，滚动结束时，指定item尾部会与滚动容器组件contentEndOffset处对齐。
* 当滚动容器组件设置contentStartOffset或contentEndOffset时，如果ScrollAlign设置为AUTO，且指定item完全处于显示区内，不做调整；否则依照滚动距离最短的原则，将指定item首部与滚动组件contentStartOffset处对齐，或指定item尾部与滚动组件contentEndOffset处对齐，使指定item完全显示。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 要滑动到的目标元素在当前容器中的索引值。  **说明：**  value值设置成负值或者大于当前容器子组件的最大索引值，视为异常值，本次跳转不生效。 |
| smooth | boolean | 否 | 设置滑动到列表项在列表中的索引值时是否有动效，true表示有动效，false表示没有动效。  默认值：false。 |
| align | [ScrollAlign](ts-container-scroll.md#scrollalign10枚举说明) | 否 | 指定滑动到的元素与当前容器的对齐方式。  List中的默认值为：ScrollAlign.START。Grid中默认值为：ScrollAlign.AUTO。WaterFlow中的默认值为：ScrollAlign.START。  **说明：**  仅List、Grid、WaterFlow组件支持该参数。 |
| options12+ | [ScrollToIndexOptions](ts-container-scroll.md#scrolltoindexoptions12对象说明) | 否 | 设置滑动到指定Index的选项，如额外偏移量。  默认值：0，单位：vp。 |

### scrollBy9+

PhonePC/2in1TabletTVWearable

scrollBy(dx: Length, dy: Length)

滑动指定距离。

说明

支持ArcList、Scroll、List、Grid、WaterFlow组件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dx | [Length](ts-types.md#length) | 是 | 水平方向滚动距离，不支持百分比形式。  取值范围：(-∞, +∞) |
| dy | [Length](ts-types.md#length) | 是 | 竖直方向滚动距离，不支持百分比形式。  取值范围：(-∞, +∞) |

### isAtEnd10+

PhonePC/2in1TabletTVWearable

isAtEnd(): boolean

查询组件是否滚动到底部。

说明

支持ArcList、Scroll、List、Grid、WaterFlow组件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示组件已经滚动到底部，false表示组件还没滚动到底部。 |

### getItemRect11+

PhonePC/2in1TabletTVWearable

getItemRect(index: number): RectResult

获取子组件的大小及相对容器组件的位置。

说明

支持ArcList、Scroll、List、Grid、WaterFlow组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 子组件的索引值。 |

说明

* index必须是当前显示区域显示的子组件的索引值，否则视为非法值。
* 非法值返回的大小和位置均为0。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RectResult](ts-universal-attributes-on-child-touch-test.md#rectresult) | 子组件的大小和相对于组件的位置。  单位：vp。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[滚动类组件错误码](errorcode-scroll.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

### getItemIndex14+

PhonePC/2in1TabletTVWearable

getItemIndex(x: number, y: number): number

通过坐标获取子组件的索引。

说明

支持List、Grid、WaterFlow组件。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | x轴坐标，单位为vp。 |
| y | number | 是 | y轴坐标，单位为vp。 |

说明

非法值返回的索引为-1。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回子组件的索引。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[滚动类组件错误码](errorcode-scroll.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

### contentSize22+

PhonePC/2in1TabletTVWearable

contentSize(): SizeResult

获取滚动组件内容总大小。

说明

* Grid、List、WaterFlow和Scroll组件主轴方向内容大小为所有子组件布局后的总大小，交叉轴方向内容大小为组件自身交叉轴方向大小减去padding和border后的大小。
* Grid、List、WaterFlow组件有懒加载机制，该接口依赖已布局的子节点进行估算。如果组件内容没有布局完成且子组件高度不一致，估算结果可能会有误差，需要开发者去适配，比如List组件可以通过childrenMainSize属性解决估算不准问题。
* 如果应用动态增删子节点，则需要应用动态获取内容总大小，来保证接口获取结果的即时性。
* 当Scroll组件设置scrollable为ScrollDirection.FREE自由滚动模式时，获取到的内容总大小为子组件缩放后的总大小。
* 当Scroll组件设置scrollable为ScrollDirection.None不可滚动时，获取到的内容总大小为0。
* 当Grid组件同时设置columnsTemplate和rowsTemplate，或columnsTemplate和rowsTemplate都不设置时即为不可滚动场景，此时获取到的内容总大小高度为0，宽度为Grid组件内容区宽度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SizeResult](ts-custom-component-layout.md#sizeresult10) | 滚动组件内容总大小，包括内容宽度和高度。  单位：vp |

**错误码**：

以下错误码详细介绍请参考[滚动类组件错误码](errorcode-scroll.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100004 | Controller not bound to a component. |

## OffsetResult11+对象说明

PhonePC/2in1TabletTVWearable

滑动偏移量对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| xOffset | number | 否 | 否 | 水平滑动偏移。  返回值单位为vp。 |
| yOffset | number | 否 | 否 | 竖直滑动偏移。  返回值单位为vp。 |

## ScrollAnimationOptions12+对象说明

PhonePC/2in1TabletTVWearable

自定义滚动动效的参数选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 否 | 是 | 设置滚动时长。  默认值：1000  单位：毫秒  **说明：**  设置为小于0的值时，按默认值显示。 |
| curve | [Curve](ts-appendix-enums.md#curve) | [ICurve](js-apis-curve.md#icurve9) | 否 | 是 | 设置滚动曲线。  默认值：Curve.Ease |
| canOverScroll | boolean | 否 | 是 | 设置滚动动画滚动到边界后，是否转换成越界回弹动画。  默认值：false  **说明：**  仅在设置为true，且组件的edgeEffect设置为[EdgeEffect.Spring](ts-appendix-enums.md#edgeeffect)时，使用动画滚动到边界会转换为越界回弹动画，设置为false时，滚动到边界会直接停止动画，不会转换为越界回弹动画。  从API version 20开始，如果[ScrollOptions](ts-container-scroll.md#scrolloptions18对象说明)中的canOverScroll设置为true，表示滚动可以停留在过界位置，滚动动画过界后不会转换为回弹动画。 |

## ScrollAlign10+枚举说明

PhonePC/2in1TabletTVWearable

对齐方式枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| START | 0 | 首部对齐。指定item首部与滚动容器组件首部对齐。 |
| CENTER | 1 | 居中对齐。指定item主轴方向居中对齐于滚动容器组件。 |
| END | 2 | 尾部对齐。指定item尾部与滚动容器组件尾部对齐。 |
| AUTO | 3 | 自动对齐。  若指定item完全处于显示区，不做调整。否则依照滑动距离最短的原则，将指定item首部对齐或尾部对齐于滚动容器组件，使指定item完全处于显示区。 |

## ScrollToIndexOptions12+对象说明

PhonePC/2in1TabletTVWearable

滑动到指定Index的参数选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| extraOffset | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 滑动到指定Index的额外偏移量。如果值为正数，则向底部额外偏移；如果值为负数，则向顶部额外偏移。 |

## ScrollPageOptions14+对象说明

PhonePC/2in1TabletTVWearable

翻页模式的参数选项。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| next | boolean | 否 | 否 | 是否向下翻页。true表示向下翻页，false表示向上翻页。 |
| animation | boolean | 否 | 是 | 是否开启翻页动画效果。true有动画，false无动画。  默认值：false。 |

## OffsetOptions12+对象说明

PhonePC/2in1TabletTVWearable

初始滚动偏移量的参数选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| xOffset | [Dimension](ts-types.md#dimension10) | 否 | 是 | 水平滚动偏移。  默认值：0 |
| yOffset | [Dimension](ts-types.md#dimension10) | 否 | 是 | 垂直滚动偏移。  默认值：0 |

## ScrollEdgeOptions12+对象说明

PhonePC/2in1TabletTVWearable

滚动到边缘位置的参数选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| velocity | number | 否 | 是 | 设置滚动到容器边缘的固定速度。如果设置小于等于0的值，参数不生效。  默认值：0  单位： vp/s |

## ScrollOptions18+对象说明

PhonePC/2in1TabletTVWearable

滚动到指定位置的参数选项。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| xOffset10+ | number | string | 否 | 否 | 水平滚动总偏移量。  **说明：**  该参数值不支持设置百分比。  仅滚动轴为x轴时生效。  取值范围：当值小于0时，不带动画的滚动，按0处理。带动画的滚动，默认滚动到起始位置后停止，可通过设置animation参数，使滚动在越界时启动回弹动画。  参数类型为number时单位为vp。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| yOffset10+ | number | string | 否 | 否 | 垂直滚动总偏移量。  **说明：**  该参数值不支持设置百分比。  仅滚动轴为y轴时生效。  取值范围：当值小于0时，不带动画的滚动，按0处理。带动画的滚动，默认滚动到起始位置后停止，可通过设置animation参数，使滚动在越界时启动回弹动画。  参数类型为number时单位为vp。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| animation10+ | [ScrollAnimationOptions](ts-container-scroll.md#scrollanimationoptions12对象说明) | boolean | 否 | 是 | 动画配置。  - ScrollAnimationOptions: 自定义滚动动效。  - boolean: 使能默认弹簧动效。  默认值：  ScrollAnimationOptions: { duration: 1000, curve: Curve.Ease, canOverScroll: false }  boolean: false  **说明：**  当前List、Scroll、Grid、WaterFlow均支持boolean类型和ICurve曲线。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| canOverScroll20+ | boolean | 否 | 是 | 滚动目标位置是否可以超出边界停留。仅当组件的edgeEffect设置为EdgeEffect.Spring时，滚动能够越界停留。  设置为true时滚动可以在过界后停留，设置为false时滚动无法在过界后停留。  默认值：false  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## UIScrollEvent19+

PhonePC/2in1TabletTVWearable

frameNode中[getEvent('Scroll')](js-apis-arkui-framenode.md#geteventscroll19)方法的返回值，可用于给Scroll节点设置滚动事件。

UIScrollEvent继承于[UIScrollableCommonEvent](ts-container-scrollable-common.md#uiscrollablecommonevent19)。

### setOnWillScroll19+

PhonePC/2in1TabletTVWearable

setOnWillScroll(callback: ScrollOnWillScrollCallback | undefined): void

设置[onWillScroll](ts-container-scroll.md#onwillscroll12)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ScrollOnWillScrollCallback](ts-container-scroll.md#scrollonwillscrollcallback12) | undefined | 是 | onWillScroll事件的回调函数。 |

### setOnDidScroll19+

PhonePC/2in1TabletTVWearable

setOnDidScroll(callback: ScrollOnScrollCallback | undefined): void

设置[onDidScroll](ts-container-scroll.md#ondidscroll12)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ScrollOnScrollCallback](ts-container-scroll.md#scrollonscrollcallback12) | undefined | 是 | onDidScroll事件的回调函数。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置scroller控制器）

该示例展示了Scroll组件部分属性和scroller控制器的使用。

```
1. // xxx.ets
2. import { curves } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct ScrollExample {
7. scroller: Scroller = new Scroller();
8. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

10. build() {
11. Stack({ alignContent: Alignment.TopStart }) {
12. Scroll(this.scroller) {
13. Column() {
14. ForEach(this.arr, (item: number) => {
15. Text(item.toString())
16. .width('90%')
17. .height(150)
18. .backgroundColor(0xFFFFFF)
19. .borderRadius(15)
20. .fontSize(16)
21. .textAlign(TextAlign.Center)
22. .margin({ top: 10 })
23. }, (item: number) => item.toString())
24. }.width('100%')
25. }
26. .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
27. .scrollBar(BarState.On) // 滚动条常驻显示
28. .scrollBarColor(Color.Gray) // 滚动条颜色
29. .scrollBarWidth(10) // 滚动条宽度
30. .friction(0.6)
31. .edgeEffect(EdgeEffect.None)
32. .onWillScroll((xOffset: number, yOffset: number, scrollState: ScrollState) => {
33. console.info(xOffset + ' ' + yOffset);
34. })
35. .onScrollEdge((side: Edge) => {
36. console.info('To the edge');
37. })
38. .onScrollStop(() => {
39. console.info('Scroll Stop');
40. })

42. Button('scroll 150')
43. .height('5%')
44. .onClick(() => { // 点击后下滑指定距离150.0vp
45. this.scroller.scrollBy(0, 150);
46. })
47. .margin({ top: 10, left: 20 })
48. Button('scroll 100')
49. .height('5%')
50. .onClick(() => { // 点击后滑动到指定位置，即下滑100.0vp的距离
51. const yOffset: number = this.scroller.currentOffset().yOffset;
52. this.scroller.scrollTo({ xOffset: 0, yOffset: yOffset + 100 });
53. })
54. .margin({ top: 60, left: 20 })
55. Button('scroll 100')
56. .height('5%')
57. .onClick(() => { // 点击后滑动到指定位置，即下滑100.0vp的距离，滑动过程配置有动画
58. let curve = curves.interpolatingSpring(10, 1, 228, 30); // 创建一个弹簧曲线
59. const yOffset: number = this.scroller.currentOffset().yOffset;
60. this.scroller.scrollTo({ xOffset: 0, yOffset: yOffset + 100, animation: { duration: 1000, curve: curve } });
61. })
62. .margin({ top: 110, left: 20 })
63. Button('back top')
64. .height('5%')
65. .onClick(() => { // 点击后回到顶部
66. this.scroller.scrollEdge(Edge.Top);
67. })
68. .margin({ top: 160, left: 20 })
69. Button('next page')
70. .height('5%')
71. .onClick(() => { // 点击后滑到下一页
72. this.scroller.scrollPage({ next: true ,animation: true });
73. })
74. .margin({ top: 210, left: 20 })
75. Button('fling -3000')
76. .height('5%')
77. .onClick(() => { // 点击后触发初始速度为-3000vp/s的惯性滚动
78. this.scroller.fling(-3000);
79. })
80. .margin({ top: 260, left: 20 })
81. Button('scroll to bottom 700')
82. .height('5%')
83. .onClick(() => { // 点击后滑到下边缘，速度值是700vp/s
84. this.scroller.scrollEdge(Edge.Bottom, { velocity: 700 });
85. })
86. .margin({ top: 310, left: 20 })
87. }.width('100%').height('100%').backgroundColor(0xDCDCDC)
88. }
89. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/1kV2ZZ-dRQyaGn7UrcH4-A/zh-cn_image_0000002552799984.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000128Z&HW-CC-Expire=86400&HW-CC-Sign=DD2B7617C31B4A3DC46E938DCF2ABD79D84DABC57901BFEEB73B984EADC562D7)

### 示例2（嵌套滚动实现方式一）

该示例使用onScrollFrameBegin事件实现了内层List组件和外层Scroll组件的嵌套滚动。

```
1. import { LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct NestedScroll {
6. @State listPosition: number = 0; // 0代表滚动到List顶部，1代表中间值，2代表滚动到List底部。
7. private arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
8. private scrollerForScroll: Scroller = new Scroller();
9. private scrollerForList: Scroller = new Scroller();

11. build() {
12. Flex() {
13. Scroll(this.scrollerForScroll) {
14. Column() {
15. Text('Scroll Area')
16. .width('100%')
17. .height('40%')
18. .backgroundColor(0X330000FF)
19. .fontSize(16)
20. .textAlign(TextAlign.Center)
21. .onClick(() => {
22. this.scrollerForList.scrollToIndex(5, false, ScrollAlign.START, { extraOffset: LengthMetrics.vp(5) });
23. })

25. List({ space: 20, scroller: this.scrollerForList }) {
26. ForEach(this.arr, (item: number) => {
27. ListItem() {
28. Text('ListItem' + item)
29. .width('100%')
30. .height('100%')
31. .borderRadius(15)
32. .fontSize(16)
33. .textAlign(TextAlign.Center)
34. .backgroundColor(Color.White)
35. }.width('100%').height(100)
36. }, (item: string) => item)
37. }
38. .width('100%')
39. .height('50%')
40. .edgeEffect(EdgeEffect.None)
41. .friction(0.6)
42. .onReachStart(() => {
43. this.listPosition = 0;
44. })
45. .onReachEnd(() => {
46. this.listPosition = 2;
47. })
48. .onScrollFrameBegin((offset: number) => {
49. if ((this.listPosition == 0 && offset <= 0) || (this.listPosition == 2 && offset >= 0)) {
50. this.scrollerForScroll.scrollBy(0, offset);
51. return { offsetRemain: 0 };
52. }
53. this.listPosition = 1;
54. return { offsetRemain: offset };
55. })

57. Text('Scroll Area')
58. .width('100%')
59. .height('40%')
60. .backgroundColor(0X330000FF)
61. .fontSize(16)
62. .textAlign(TextAlign.Center)
63. }
64. }
65. .width('100%').height('100%')
66. }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding(20)
67. }
68. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/WZ7nTyHVQg6ijKMRXsmjjA/zh-cn_image_0000002583439679.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000128Z&HW-CC-Expire=86400&HW-CC-Sign=B24F964C7CACFDF18E5CE127ABBCA9D0B2103E9E960C021B6391CF8AE46D7389)

### 示例3（嵌套滚动实现方式二）

该示例使用[nestedScroll](ts-container-scroll.md#nestedscroll10)属性实现了内层List组件和外层Scroll组件的嵌套滚动。

```
1. @Entry
2. @Component
3. struct StickyNestedScroll {
4. @State arr: number[] = [];

6. @Styles
7. listCard() {
8. .backgroundColor(Color.White)
9. .height(72)
10. .width('100%')
11. .borderRadius(12)
12. }

14. build() {
15. Scroll() {
16. Column() {
17. Text('Scroll Area')
18. .width('100%')
19. .height('40%')
20. .backgroundColor('#0080DC')
21. .textAlign(TextAlign.Center)
22. Tabs({ barPosition: BarPosition.Start }) {
23. TabContent() {
24. List({ space: 10 }) {
25. ForEach(this.arr, (item: number) => {
26. ListItem() {
27. Text('item' + item)
28. .fontSize(16)
29. }.listCard()
30. }, (item: number) => item.toString())
31. }.width('100%')
32. .edgeEffect(EdgeEffect.Spring)
33. .nestedScroll({
34. scrollForward: NestedScrollMode.PARENT_FIRST,
35. scrollBackward: NestedScrollMode.SELF_FIRST
36. })
37. }.tabBar('Tab1')

39. TabContent() {
40. }.tabBar('Tab2')
41. }
42. .vertical(false)
43. .height('100%')
44. }.width('100%')
45. }
46. .edgeEffect(EdgeEffect.Spring)
47. .friction(0.6)
48. .backgroundColor('#DCDCDC')
49. .scrollBar(BarState.Off)
50. .width('100%')
51. .height('100%')
52. }

54. aboutToAppear() {
55. for (let i = 0; i < 30; i++) {
56. this.arr.push(i);
57. }
58. }
59. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/sxL3sknCSxalo_Hl5VuILQ/zh-cn_image_0000002552959634.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000128Z&HW-CC-Expire=86400&HW-CC-Sign=210297D67EC6CE7442764FB776079AF96BE2DE867996BFED9D774B6A37B80DF8)

### 示例4（嵌套滚动父组件向子组件传递滚动）

该示例使用[enableScrollInteraction](ts-container-scroll.md#enablescrollinteraction10)属性和[onScrollFrameBegin](ts-container-scroll.md#onscrollframebegin9)事件实现了父组件向子组件传递滚动。

```
1. @Entry
2. @Component
3. struct NestedScroll {
4. private headerHeight: number = 0;
5. private arr: number[] = [];
6. private scrollerForParent: Scroller = new Scroller();
7. private scrollerForChild: Scroller = new Scroller();

9. aboutToAppear(): void {
10. for (let i = 0; i < 10; i++) {
11. this.arr.push(i);
12. }
13. }

15. build() {
16. Scroll(this.scrollerForParent) {
17. Column() {
18. Text('Scroll Area')
19. .width('100%')
20. .height('40%')
21. .backgroundColor(0X330000FF)
22. .fontSize(16)
23. .textAlign(TextAlign.Center)
24. .onClick(() => {
25. this.scrollerForChild.scrollToIndex(5);
26. })
27. .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
28. this.headerHeight = newValue.height! as number;
29. })
30. List({ space: 20, scroller: this.scrollerForChild }) {
31. ForEach(this.arr, (item: number) => {
32. ListItem() {
33. Text('ListItem' + item)
34. .width('100%')
35. .height('100%')
36. .borderRadius(15)
37. .fontSize(16)
38. .textAlign(TextAlign.Center)
39. .backgroundColor(Color.White)
40. }.width('100%').height(100)
41. }, (item: number) => item.toString())
42. }
43. .width('100%')
44. .height('100%')
45. .edgeEffect(EdgeEffect.None)
46. .scrollBar(BarState.Off)
47. .enableScrollInteraction(false)

49. Text('Scroll Area')
50. .width('100%')
51. .height('40%')
52. .backgroundColor(0X330000FF)
53. .fontSize(16)
54. .textAlign(TextAlign.Center)
55. }
56. }
57. .scrollBar(BarState.Off)
58. .edgeEffect(EdgeEffect.Spring)
59. .onScrollFrameBegin((offset: number, state: ScrollState) => {
60. let retOffset = offset;
61. let currOffset = this.scrollerForParent.currentOffset().yOffset;
62. let newOffset = currOffset + offset;
63. if (offset > 0) {
64. if (this.scrollerForChild.isAtEnd()) {
65. return { offsetRemain: offset };
66. }
67. if (newOffset > this.headerHeight) {
68. retOffset = this.headerHeight - currOffset;
69. }
70. this.scrollerForChild.scrollBy(0, offset - retOffset);
71. } else {
72. if (this.scrollerForChild.currentOffset().yOffset <= 0) {
73. return { offsetRemain: offset };
74. }
75. if (newOffset < this.headerHeight) {
76. retOffset = this.headerHeight - currOffset;
77. }
78. this.scrollerForChild.scrollBy(0, offset - retOffset);
79. }
80. return { offsetRemain: retOffset };
81. })
82. .width('100%')
83. .height('100%')
84. .backgroundColor(0xDCDCDC)
85. }
86. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/-eCmxm2uTY-tQk1kpwGI0g/zh-cn_image_0000002583479635.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000128Z&HW-CC-Expire=86400&HW-CC-Sign=5DA26B465D272D3B6F5250CF622D3DEEA9038F63DD57A36A57873EC3FCA821FB)

### 示例5（设置限位滚动）

该示例实现了Scroll组件的限位滚动。

```
1. @Entry
2. @Component
3. struct Index {
4. scroller: Scroller = new Scroller();
5. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
6. build() {
7. Scroll(this.scroller) {
8. Column() {
9. ForEach(this.arr, (item: number) => {
10. Text(item.toString())
11. .width('90%')
12. .height(200)
13. .backgroundColor(0xFFFFFF)
14. .borderWidth(1)
15. .borderColor(Color.Black)
16. .borderRadius(15)
17. .fontSize(16)
18. .textAlign(TextAlign.Center)
19. }, (item: number) => item.toString())
20. }.width('100%').backgroundColor(0xDCDCDC)
21. }
22. .backgroundColor(Color.Yellow)
23. .height('100%')
24. .edgeEffect(EdgeEffect.Spring)
25. .scrollSnap({snapAlign:ScrollSnapAlign.START, snapPagination:400, enableSnapToStart:true, enableSnapToEnd:true})
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/nCnAT6_dS1SuVKA34tEU7A/zh-cn_image_0000002552799986.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000128Z&HW-CC-Expire=86400&HW-CC-Sign=65A7C6025E308759597F1F61B728B93552BE163A1B959A419E224F8A7BD11088)

### 示例6（获取子组件索引）

该示例展示了如何获得List组件的子组件索引。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ListExample {
5. private arr: number[] = [];
6. private scroller: ListScroller = new ListScroller();
7. @State listSpace: number = 10;
8. @State listChildrenSize: ChildrenMainSize = new ChildrenMainSize(100);
9. @State listIndex: number = -1;
10. @State itemBackgroundColorArr: boolean[] = [false];
11. aboutToAppear(){
12. // 初始化数据源。
13. for (let i = 0; i < 10; i++) {
14. this.arr.push(i);
15. }
16. this.listChildrenSize.splice(0, 5, [100, 100, 100, 100, 100]);
17. }
18. build() {
19. Column() {
20. List({ space: this.listSpace, initialIndex: 4, scroller: this.scroller }) {
21. ForEach(this.arr, (item: number) => {
22. ListItem() {
23. Text('item-' + item)
24. .height( item < 5 ? 100 : this.listChildrenSize.childDefaultSize)
25. .width('90%')
26. .fontSize(16)
27. .textAlign(TextAlign.Center)
28. .borderRadius(10)
29. .backgroundColor( this.itemBackgroundColorArr[item] ? 0x68B4FF: 0xFFFFFF)
30. }
31. }, (item: number) => item.toString())
32. }
33. .backgroundColor(Color.Gray)
34. .layoutWeight(1)
35. .scrollBar(BarState.On)
36. .childrenMainSize(this.listChildrenSize)
37. .alignListItem(ListItemAlign.Center)
38. .gesture(
39. PanGesture()
40. .onActionUpdate((event: GestureEvent) => {
41. if (event.fingerList[0] != undefined && event.fingerList[0].localX != undefined && event.fingerList[0].localY != undefined) {
42. this.listIndex = this.scroller.getItemIndex(event.fingerList[0].localX, event.fingerList[0].localY);
43. this.itemBackgroundColorArr[this.listIndex] = true;
44. }
45. })
46. )
47. .gesture(
48. TapGesture({ count: 1 })
49. .onAction((event: GestureEvent) => {
50. if (event) {
51. this.itemBackgroundColorArr.splice(0,this.itemBackgroundColorArr.length);
52. }
53. })
54. )

56. Text('您当前位置Item索引为：'+ this.listIndex)
57. .fontColor(Color.Red)
58. .height(50)
59. }
60. }
61. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/PfxQ381KQGG9FNQNg3Md3A/zh-cn_image_0000002583439681.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000128Z&HW-CC-Expire=86400&HW-CC-Sign=6BA913F2DB62D6FF89FA32B493A6555DAA41995ACDA3C11E22BDEB164D3C76AB)

### 示例7（设置边缘渐隐）

该示例实现了Scroll组件开启边缘渐隐效果并设置边缘渐隐长度。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';
3. @Entry
4. @Component
5. struct ScrollExample {
6. scroller: Scroller = new Scroller();
7. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

9. build() {
10. Stack({ alignContent: Alignment.TopStart }) {
11. Scroll(this.scroller) {
12. Column() {
13. ForEach(this.arr, (item: number) => {
14. Text(item.toString())
15. .width('90%')
16. .height(150)
17. .backgroundColor(0xFFFFFF)
18. .borderRadius(15)
19. .fontSize(16)
20. .textAlign(TextAlign.Center)
21. .margin({ top: 10 })
22. }, (item: string) => item)
23. }.width('100%')
24. }
25. .fadingEdge(true,{fadingEdgeLength:LengthMetrics.vp(80)})

29. }.width('100%').height('100%').backgroundColor(0xDCDCDC)
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/tV6MprVPRLO-hLyMmydMjw/zh-cn_image_0000002552959636.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000128Z&HW-CC-Expire=86400&HW-CC-Sign=CA0B8521D0D4444D0092EE919429F6EC6653CB8E6CD3A30A7036A67B7748BC4A)

### 示例8（单边边缘效果）

该示例通过[edgeEffect](ts-container-scroll.md#edgeeffect)接口，实现了Scroll组件设置单边边缘效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ScrollExample {
5. scroller: Scroller = new Scroller();
6. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

8. build() {
9. Stack({ alignContent: Alignment.TopStart }) {
10. Scroll(this.scroller) {
11. Column() {
12. ForEach(this.arr, (item: number) => {
13. Text(item.toString())
14. .width('90%')
15. .height(150)
16. .backgroundColor(0xFFFFFF)
17. .borderRadius(15)
18. .fontSize(16)
19. .textAlign(TextAlign.Center)
20. .margin({ top: 10 })
21. }, (item: string) => item)
22. }.width('100%')
23. }
24. .edgeEffect(EdgeEffect.Spring,{alwaysEnabled:true,effectEdge:EffectEdge.START})
25. }.width('100%').height('100%').backgroundColor(0xDCDCDC)
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/RkRIE0z1Smq1yajKTryGiQ/zh-cn_image_0000002583479637.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000128Z&HW-CC-Expire=86400&HW-CC-Sign=8ABF79AC59E5E2D9147CA0A6611303347EC36A6348AD5CAF907A4A567AB245BE)

### 示例9（划动翻页效果）

该示例通过[enablePaging](ts-container-scroll.md#enablepaging11)接口，实现了Scroll组件滑动翻页效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct EnablePagingExample {
5. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

7. build() {
8. Stack({ alignContent: Alignment.Center }) {
9. Scroll() {
10. Column() {
11. ForEach(this.arr, (item: number) => {
12. Text(item.toString())
13. .width('100%')
14. .height('100%')
15. .borderRadius(15)
16. .fontSize(16)
17. .textAlign(TextAlign.Center)
18. .backgroundColor(0xFFFFFF)
19. }, (item: number) => item.toString())
20. }
21. }.width('90%').height('90%')
22. .enablePaging(true)
23. }.width('100%').height('100%').backgroundColor(0xDCDCDC)
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/hIIWqR1QR8GMIXdZXHaXSA/zh-cn_image_0000002552799988.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000128Z&HW-CC-Expire=86400&HW-CC-Sign=94901C336B7328EDE4FB1E2A5AE1B469E24B65A8C2B83696C881E34BA97039BE)

### 示例10（设置过界停留）

该示例通过[scrollTo](ts-container-scroll.md#scrollto)接口，实现了Scroll组件设置过界停留效果。

```
1. // xxx.ets
2. import { curves } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct StickyNestedScroll {
7. scroller: Scroller = new Scroller;

9. build() {
10. Column() {
11. Row() {
12. Button('有动画scrollTo').onClick(() => {
13. let curve = curves.interpolatingSpring(0.5, 5, 10, 15) // 创建一个弹簧曲线
14. const yOffset: number = this.scroller.currentOffset().yOffset;
15. this.scroller.scrollTo({
16. xOffset: 0,
17. yOffset: yOffset - 100,
18. animation: { duration: 1000, curve: curve, canOverScroll: true },
19. canOverScroll: true
20. })
21. }).margin({ top: 10 })
22. Button('无动画scrollTo').onClick(() => {
23. const yOffset: number = this.scroller.currentOffset().yOffset;
24. this.scroller.scrollTo({
25. xOffset: 0,
26. yOffset: yOffset - 100,
27. animation: false,
28. canOverScroll: true
29. })
30. }).margin({ top: 10, left: 20 })
31. }.margin({ bottom: 20 })

33. Scroll(this.scroller) {
34. Column() {
35. Text('Scroll Area')
36. .width('100%')
37. .height('100%')
38. .backgroundColor('#0080DC')
39. .textAlign(TextAlign.Center)
40. }
41. .width('100%')
42. .height('100%')
43. }
44. .scrollable(ScrollDirection.Vertical)
45. .edgeEffect(EdgeEffect.Spring) // 设置边缘效果
46. .fadingEdge(false) // 关闭边缘渐隐效果
47. .scrollBar(BarState.Auto)
48. .friction(undefined)
49. .backgroundColor('#DCDCDC')
50. .width('100%')
51. .height('50%')
52. }
53. }
54. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/jwEINkDtThy1YxbHty-78w/zh-cn_image_0000002583439683.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000128Z&HW-CC-Expire=86400&HW-CC-Sign=D63333C893652100F289989E2638EBBFA9B677D2E0DFCC11CA20B39F08DC8745)

### 示例11（自由滚动和缩放）

从API version 20开始，该示例实现了Scroll组件自由滚动和缩放效果。

```
1. @Entry
2. @Component
3. struct ScrollZoomExample {
4. @State currScale:number = 1;
5. build() {
6. Column() {
7. Scroll() {
8. Image($r('app.media.image1')) // 'app.media.image1'仅作示例，请替换实际图片。
9. }
10. .height(400)
11. .scrollable(ScrollDirection.FREE)
12. .minZoomScale(1)
13. .maxZoomScale(2)
14. .zoomScale(this.currScale!!)
15. .enableBouncesZoom(true)
16. .onDidZoom((scale: number) => {
17. console.info(`onDidZoom:${scale}`);
18. })
19. .onZoomStart(() => {
20. console.info('onZoomStart');
21. })
22. .onZoomStop(() => {
23. console.info('onZoomStop');
24. })
25. }.width('100%').height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/DHQvcI6xSmK1KDBjDVAIBA/zh-cn_image_0000002552959638.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000128Z&HW-CC-Expire=86400&HW-CC-Sign=A88378D77EA5348AFA07424215754D709C22A98FAF90509E965DA7B18E259018)

### 示例12（获取内容总大小）

从API version 22 开始，该示例实现了获取内容总大小的功能。

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. @Entry
4. @Component
5. struct ScrollExample1 {
6. scroller: Scroller = new Scroller();
7. private arr: number[] = []

9. aboutToAppear() {
10. for (let j = 0; j < 10; j++) {
11. this.arr.push(j);
12. }
13. }

15. @State contentWidth: number = -1;
16. @State contentHeight: number = -1;

18. build() {
19. Column() {
20. Text('设置scroller控制器和ForEach')
21. Row() {
22. // 点击按钮来调用contentSize函数获取内容尺寸
23. Button('GetContentSize')
24. .onClick(() => {
25. // Scroller未绑定组件时会抛异常，需要加上try catch保护
26. try {
27. // 通过调用contentSize函数获取内容尺寸的宽度值
28. this.contentWidth = this.scroller.contentSize().width;
29. // 通过调用contentSize函数获取内容尺寸的高度值
30. this.contentHeight = this.scroller.contentSize().height;
31. } catch (error) {
32. let err: BusinessError = error as BusinessError;
33. console.error(`Failed to get contentSize of the grid, code=${err.code}, message=${err.message}`);
34. }
35. })
36. // 将获取到的内容尺寸信息通过文本进行呈现
37. Text('Width：' + this.contentWidth + '，Height：' + this.contentHeight)
38. .fontColor(Color.Red)
39. .height(50)
40. }

42. Stack({ alignContent: Alignment.TopStart }) {
43. Scroll(this.scroller) {
44. Column() {
45. ForEach(this.arr, (item: number) => {
46. Text(item.toString())
47. .width('90%')
48. .height(150)
49. .backgroundColor(0xFFFFFF)
50. .borderRadius(15)
51. .fontSize(16)
52. .textAlign(TextAlign.Center)
53. .margin({ top: 10 })
54. }, (item: number) => item.toString())
55. }.width('100%')
56. }
57. .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
58. .scrollBar(BarState.On) // 滚动条常驻显示
59. .scrollBarColor(Color.Gray) // 滚动条颜色
60. .scrollBarWidth(10) // 滚动条宽度
61. .friction(0.6)
62. .edgeEffect(EdgeEffect.None)
63. }.width('100%').height('100%').backgroundColor(0xDCDCDC)
64. }
65. }
66. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/VPG8uyaKQVivLAyM9YSzQg/zh-cn_image_0000002583479639.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000128Z&HW-CC-Expire=86400&HW-CC-Sign=930C6507313C33FAFA8EEDBEE3C3CC921F9FC3C9D442C41998900BD0EAE1528A)

### 示例13（设置滚动事件）

该示例通过FrameNode中的[getEvent('Scroll')](js-apis-arkui-framenode.md#geteventscroll19)获取[UIScrollEvent](ts-container-scroll.md#uiscrollevent19)，并为Scroll设置滚动事件回调，用于事件监听方因无法直接修改页面代码而无法使用声明式接口设置回调的场景。

从API version 19开始，新增UIScrollEvent接口。

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. class MyNodeController extends NodeController {
4. public rootNode: FrameNode | null = null;

6. makeNode(uiContext: UIContext): FrameNode | null {
7. this.rootNode = new FrameNode(uiContext);
8. this.rootNode.commonAttribute.width(100);
9. return this.rootNode;
10. }

12. addCommonEvent(frameNode: FrameNode) {
13. // 获取Scroll事件
14. let scrollEvent: UIScrollEvent | undefined = typeNode.getEvent(frameNode, 'Scroll');

16. // 设置OnWillScroll事件
17. scrollEvent?.setOnWillScroll((xOffset: number, yOffset: number, scrollState: ScrollState,
18. scrollSource: ScrollSource) => {
19. console.info('onWillScroll xOffset = ${xOffset}, yOffset = ${yOffset}, scrollState = ${scrollState}, scrollSource = ${scrollSource}');
20. });

22. // 设置OnDidScroll事件
23. scrollEvent?.setOnDidScroll((scrollOffset: number, scrollState: ScrollState) => {
24. console.info('onDidScroll scrollOffset = ${scrollOffset}, scrollState = ${scrollState}');
25. });

27. // 设置OnReachStart事件
28. scrollEvent?.setOnReachStart(() => {
29. console.info('onReachStart');
30. });

32. // 设置OnReachEnd事件
33. scrollEvent?.setOnReachEnd(() => {
34. console.info('onReachEnd');
35. });

37. // 设置OnScrollStart事件
38. scrollEvent?.setOnScrollStart(() => {
39. console.info('onScrollStart');
40. });

42. // 设置OnScrollStop事件
43. scrollEvent?.setOnScrollStop(() => {
44. console.info('onScrollStop');
45. });

47. // 设置OnScrollFrameBegin事件
48. scrollEvent?.setOnScrollFrameBegin((offset: number, state: ScrollState) => {
49. console.info('onScrollFrameBegin offset = ${offset}, state = ${state}');
50. return undefined;
51. });
52. }
53. }

55. @Entry
56. @Component
57. struct Index {
58. @State index: number = 0;
59. private myNodeController: MyNodeController = new MyNodeController();
60. @State numbers: string[] = [];

62. aboutToAppear() {
63. for (let i = 0; i < 30; i++) {
64. this.numbers.push('${i+1}');
65. }
66. }

68. build() {
69. Column() {
70. Button('add CommonEvent to Scroll')
71. .onClick(() => {
72. this.myNodeController!.addCommonEvent(this.myNodeController!.rootNode!.getParent()!.getPreviousSibling()!)
73. })
74. Scroll() {
75. Column() {
76. ForEach(this.numbers, (day: string, index: number) => {
77. Column() {
78. Text(day)
79. .fontSize(16)
80. .backgroundColor(0xF9CF93)
81. .width('90%')
82. .height(80)
83. .textAlign(TextAlign.Center)
84. .margin({ top: 10 })
85. }
86. .width('100%')
87. .justifyContent(FlexAlign.Center)
88. .alignItems(HorizontalAlign.Center)
89. }, (day: string, index: number) => index.toString() + day)
90. }
91. }
92. .scrollable(ScrollDirection.Vertical)
93. .edgeEffect(EdgeEffect.Spring)
94. .width('90%')
95. .backgroundColor(0xFAEEE0)
96. .height(300)
97. NodeContainer(this.myNodeController)
98. }
99. }
100. }
```
