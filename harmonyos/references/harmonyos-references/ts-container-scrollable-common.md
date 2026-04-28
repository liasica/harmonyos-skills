---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scrollable-common
title: 滚动组件通用接口
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 滚动与滑动 > 滚动组件通用接口
category: harmonyos-references
scraped_at: 2026-04-28T08:01:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1b179a857be22342d48c467080eb6da6c1e4e369878d04e34a48bca1c6f8442e
---

滚动组件通用属性和事件目前只支持[List](ts-container-list.md)、[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)和[WaterFlow](ts-container-waterflow.md)组件。

说明

本模块从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 属性

PhonePC/2in1TabletTVWearable

### scrollBar11+

PhonePC/2in1TabletTVWearable

scrollBar(barState: BarState): T

设置滚动条状态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| barState | [BarState](ts-appendix-enums.md#barstate) | 是 | 滚动条状态。  默认值：List、Grid、Scroll组件默认BarState.Auto，WaterFlow组件默认BarState.Off。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### scrollBarColor11+

PhonePC/2in1TabletTVWearable

scrollBarColor(color: Color | number | string): T

设置滚动条的颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Color](ts-appendix-enums.md#color) | number | string | 是 | 滚动条的颜色。  默认值：'#182431'（40%不透明度）  number为HEX格式颜色，支持rgb或者argb，示例：0xffffff。string为rgb或者argb格式颜色，示例：'#ffffff'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### scrollBarColor22+

PhonePC/2in1TabletTVWearable

scrollBarColor(color: Color | number | string | Resource): T

设置滚动条的颜色。与[scrollBarColor11+](ts-container-scrollable-common.md#scrollbarcolor11)相比，color参数开始支持Resource类型。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Color](ts-appendix-enums.md#color) | number | string | [Resource](ts-types.md#resource) | 是 | 滚动条的颜色。  默认值：'#182431'（40%不透明度）  number为HEX格式颜色，支持rgb或者argb，示例：0xffffff。string为rgb或者argb格式颜色，示例：'#ffffff'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### scrollBarWidth11+

PhonePC/2in1TabletTVWearable

scrollBarWidth(value: number | string): T

设置滚动条的宽度，不支持百分比设置。宽度设置后，滚动条正常状态和按压状态宽度均为滚动条的宽度值。如果滚动条的宽度超过滚动组件主轴方向的高度，则滚动条的宽度会变为默认值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 滚动条的宽度。  默认值：4  单位：vp  取值范围：设置为小于0的值时，按默认值处理。设置为0时，不显示滚动条。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### edgeEffect11+

PhonePC/2in1TabletTVWearable

edgeEffect(edgeEffect: EdgeEffect, options?: EdgeEffectOptions): T

设置边缘滑动效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| edgeEffect | [EdgeEffect](ts-appendix-enums.md#edgeeffect) | 是 | 滚动组件的边缘滑动效果，支持弹簧效果和阴影效果。  默认值：Grid、Scroll、WaterFlow组件默认EdgeEffect.None，List组件默认EdgeEffect.Spring。 |
| options | [EdgeEffectOptions](ts-container-scrollable-common.md#edgeeffectoptions11对象说明) | 否 | 组件内容大小小于组件自身时是否开启滑动效果，以及设置边缘效果生效的边缘。设置为{ alwaysEnabled: true }会开启滑动效果，{ alwaysEnabled: false }不开启。  默认值：  List、Grid、WaterFlow组件默认{ alwaysEnabled: false, EffectEdge: EffectEdge.START | EffectEdge.END }，Scroll组件默认{ alwaysEnabled: true, EffectEdge: EffectEdge.START | EffectEdge.END }。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### nestedScroll11+

PhonePC/2in1TabletTVWearable

nestedScroll(value: NestedScrollOptions): T

设置前后两个方向的嵌套滚动模式，实现与父组件的滚动联动。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NestedScrollOptions](ts-container-scrollable-common.md#nestedscrolloptions10对象说明) | 是 | 嵌套滚动选项。  默认值：{ scrollForward: NestedScrollMode.SELF\_ONLY, scrollBackward: NestedScrollMode.SELF\_ONLY } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### enableScrollInteraction11+

PhonePC/2in1TabletTVWearable

enableScrollInteraction(value: boolean): T

设置是否支持滚动手势。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否支持滚动手势。设置为true时可以通过手指或者鼠标滚动，设置为false时无法通过手指或者鼠标滚动，但不影响控制器[Scroller](ts-container-scroll.md#scroller)的滚动接口。  默认值：true |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### friction11+

PhonePC/2in1TabletTVWearable

friction(value: number | Resource): T

设置摩擦系数，手动划动滚动区域时生效，仅影响惯性滚动过程，对惯性滚动过程中的链式效果有间接影响。设置为小于等于0的值时，按默认值处理。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [Resource](ts-types.md#resource) | 是 | 摩擦系数。  默认值：非wearable设备为0.6，wearable设备为0.9。  从API version 11开始，非wearable设备默认值为0.7。  从API version 12开始，非wearable设备默认值为0.75。  取值范围：(0, +∞)，设置为小于等于0的值时，按默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### flingSpeedLimit11+

PhonePC/2in1TabletTVWearable

flingSpeedLimit(speedLimit: number): T

限制跟手滑动结束后，惯性动效开始时的最大初始速度。

说明

* 惯性动效是指手指快速滑动并离开屏幕后，滚动内容继续滚动并逐渐减速停止的效果，也称为惯性滚动。
* 惯性动效触发场景包括：惯性手指快速滑动并离手时，或调用[fling](ts-container-scroll.md#fling12)方法。
* 使用鼠标滚轮、键盘方向键方式滚动，或通过[scrollTo](ts-container-scroll.md#scrollto)等方法直接滚动到指定位置，不会产生惯性动效。
* 如果惯性动效通过[fling](ts-container-scroll.md#fling12)方法触发，则flingSpeedLimit设置不生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speedLimit | number | 是 | 惯性动效开始时的最大初始速度。  默认值：9000  单位：vp/s  取值范围：(0, +∞)，设置为小于等于0的值时，按默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### fadingEdge14+

PhonePC/2in1TabletTVWearable

fadingEdge(enabled: Optional<boolean>, options?: FadingEdgeOptions): T

设置是否开启边缘渐隐效果及设置边缘渐隐长度。

说明

fadingEdge是通过设置[overlay](ts-universal-attributes-overlay.md#overlay)属性和[blendMode](ts-universal-attributes-image-effect.md#blendmode11)属性（参数值为BlendMode.SRC\_OVER，BlendApplyType.OFFSCREEN）实现的。当fadingEdge生效时，会覆盖原组件的.overlay()属性和.blendMode()属性，并将导致当前组件和其子组件需要截屏的接口无法截取到正确的画面。需要截屏的接口有：[blur](ts-universal-attributes-image-effect.md#blur)、[linearGradientBlur](ts-universal-attributes-image-effect.md#lineargradientblur12)、[brightness](ts-universal-attributes-image-effect.md#brightness)、[visualEffect](ts-universal-attributes-filter-effect.md#visualeffect)、[grayscale](ts-universal-attributes-image-effect.md#grayscale)、[saturate](ts-universal-attributes-image-effect.md#saturate)、[contrast](ts-universal-attributes-image-effect.md#contrast)、[invert](ts-universal-attributes-image-effect.md#invert)、[sepia](ts-universal-attributes-image-effect.md#sepia)、[hueRotate](ts-universal-attributes-image-effect.md#huerotate)、[colorBlend](ts-universal-attributes-image-effect.md#colorblend)、[lightUpEffect](ts-universal-attributes-image-effect.md#lightupeffect12)、[pixelStretchEffect](ts-universal-attributes-image-effect.md#pixelstretcheffect12)、[blendMode](ts-universal-attributes-image-effect.md#blendmode11)、[backgroundBrightness](ts-universal-attributes-background.md#backgroundbrightness12)。

fadingEdge生效时，建议不在设置fadingEdge属性的组件上设置[background](ts-universal-attributes-background.md#background10)相关属性，会影响渐隐的显示效果。

fadingEdge生效时，设置fadingEdge属性的组件会裁剪到边界，在该组件上设置[clip](ts-universal-attributes-sharp-clipping.md#clip12)属性为false不生效。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否开启边缘渐隐效果。设置为true时开启边缘渐隐效果，设置为false时不开启边缘渐隐效果。  默认值：false |
| options | [FadingEdgeOptions](ts-container-scrollable-common.md#fadingedgeoptions14对象说明) | 否 | 边缘渐隐参数对象。可以通过该对象定义边缘渐隐效果属性，比如设置渐隐长度。  如果设置小于0的值或undefined或者不设置则取默认值，默认长度为32vp。  如果设置的长度超过容器高度的一半时，渐隐长度取容器高度的一半。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### clipContent14+

PhonePC/2in1TabletTVWearable

clipContent(clip: ContentClipMode | RectShape): T

设置滚动容器的内容层裁剪区域。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clip | [ContentClipMode](ts-container-scrollable-common.md#contentclipmode14枚举说明) | [RectShape](js-apis-arkui-shape.md#rectshape) | 是 | 裁剪只针对滚动容器的内容，即其子节点，背景不受影响。通过RectShape传入自定义矩形区域时仅支持设置宽高和相对于组件左上角的[offset](js-apis-arkui-shape.md#offset)，不支持圆角。  默认值：Grid、Scroll的默认值为ContentClipMode.BOUNDARY，List、WaterFlow的默认值为ContentClipMode.CONTENT\_ONLY。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### backToTop15+

PhonePC/2in1TabletTVWearable

backToTop(backToTop: boolean): T

设置滚动组件是否支持点击状态栏回到顶部。

支持当前页面的滚动组件收到点击状态栏事件后，通过动画回到顶部。点击状态栏后，后台应用的滚动组件不受影响，不做回到顶部的动作。本属性不受[enableScrollInteraction](ts-container-scrollable-common.md#enablescrollinteraction11)设置的影响。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| backToTop | boolean | 是 | 设置滚动组件是否支持点击状态栏回到顶部。设置为true支持点击状态栏通过动画回到顶部，设置为false不支持点击状态栏回到顶部。  默认值：  API version 18之前：false。  API version 18及以后：滚动方向是水平方向时为false，是垂直方向时为true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### scrollBarMargin20+

PhonePC/2in1TabletTVWearable

scrollBarMargin(margin: ScrollBarMargin): T

设置滚动条的边距。边距是在滚动条避让圆角距离的基础上计算的，如果滚动条区域小于滚动条的最小长度，则不显示滚动条。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| margin | [ScrollBarMargin](ts-types.md#scrollbarmargin20对象说明) | 是 | 滚动条起始、末尾边距。  默认值：{start: LengthMetrics.vp(0), end: LengthMetrics.vp(0)} |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### digitalCrownSensitivity18+

PhonePC/2in1TabletTVWearable

digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>): T

设置表冠响应事件灵敏度。

组件收到[表冠事件](ts-universal-events-crown.md)的前提是该组件获焦，焦点控制可以通过[focusable](ts-universal-attributes-focus.md#focusable)、[defaultFocus](ts-universal-attributes-focus.md#defaultfocus9)、[focusOnTouch](ts-universal-attributes-focus.md#focusontouch9)进行管理。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sensitivity | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[CrownSensitivity](ts-appendix-enums.md#crownsensitivity18)> | 是 | 表冠响应灵敏度。  默认值：CrownSensitivity.MEDIUM，响应速度适中。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### contentStartOffset22+

PhonePC/2in1TabletTVWearable

contentStartOffset(offset: number | Resource): T

设置内容区域起始偏移量。滚动组件滚动到起始位置时，内容与组件显示区域边界保留指定距离。

contentStartOffset + contentEndOffset超过滚动组件内容区长度后contentStartOffset和contentEndOffset会置0。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | [Resource](ts-types.md#resource) | 是 | 内容区域起始偏移量。  默认值：0  单位：vp  设置异常值如负数、非数字Resource时，按默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### contentEndOffset22+

PhonePC/2in1TabletTVWearable

contentEndOffset(offset: number | Resource): T

设置内容区末尾偏移量。滚动组件滚动到末尾位置时，内容与组件显示区域边界保留指定距离。

contentStartOffset + contentEndOffset超过滚动组件内容区长度后contentStartOffset和contentEndOffset会置0。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | [Resource](ts-types.md#resource) | 是 | 内容区末尾偏移量。  默认值：0  单位：vp  设置异常值如负数、非数字Resource时，按默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

## 事件

PhonePC/2in1TabletTVWearable

### onReachStart11+

PhonePC/2in1TabletTVWearable

onReachStart(event: () => void): T

滚动组件到达起始位置时触发。

滚动组件初始化时会触发一次，滚动到起始位置时触发一次。边缘效果为弹簧效果时，划动经过起始位置时触发一次，回弹回起始位置时再触发一次。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 滚动组件到达起始位置时的回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### onReachEnd11+

PhonePC/2in1TabletTVWearable

onReachEnd(event: () => void): T

滚动组件到达末尾位置时触发。

滚动组件边缘效果为弹簧效果时，划动经过末尾位置时触发一次，回弹回末尾位置时再触发一次。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 滚动组件到达末尾位置时的回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### onScrollStart11+

PhonePC/2in1TabletTVWearable

onScrollStart(event: () => void): T

滚动开始时触发。手指拖动滚动组件或拖动滚动组件的滚动条触发的滚动开始时，会触发该事件。使用[Scroller](ts-container-scroll.md#scroller)滚动控制器触发的带动画的滚动，动画开始时会触发该事件。

触发该事件的条件：

1. 滚动组件开始滚动时触发，支持键鼠操作等其他触发滚动的输入设置。
2. 通过滚动控制器API接口调用后开始，带过渡动效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 滚动开始时的回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### onScrollStop11+

PhonePC/2in1TabletTVWearable

onScrollStop(event: () => void): T

滚动停止时触发。手拖动滚动组件或拖动滚动组件的滚动条触发的滚动，手离开屏幕后滚动停止时会触发该事件。使用[Scroller](ts-container-scroll.md#scroller)滚动控制器触发的带动画的滚动，动画停止时会触发该事件。

触发该事件的条件：

1. 滚动组件触发滚动后停止，支持键鼠操作等其他触发滚动的输入设置。
2. 通过调用带过渡动画的滚动控制器API接口，动画停止时。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 滚动停止时的回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### onWillScroll12+

PhonePC/2in1TabletTVWearable

onWillScroll(handler: Optional<OnWillScrollCallback>): T

滚动事件回调，滚动组件滚动前触发。

回调当前帧将要滚动的偏移量和当前滚动状态和滚动操作来源，其中回调的偏移量为计算得到的将要滚动的偏移量值，并非最终实际滚动偏移。可以通过该回调返回值指定滚动组件将要滚动的偏移。[Scroll](ts-container-scroll.md)组件的[onWillScroll](ts-container-scroll.md#onwillscroll12)接口的参数类型是[ScrollOnWillScrollCallback](ts-container-scroll.md#scrollonwillscrollcallback12)。

说明

* 从API version 14开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。
* 调用不带动画的[ScrollEdge](ts-container-scroll.md#scrolledge)和[ScrollToIndex](ts-container-scroll.md#scrolltoindex)时，不触发onWillScroll。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[OnWillScrollCallback](ts-container-scrollable-common.md#onwillscrollcallback12)> | 是 | 滚动组件滑动前触发的回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### onDidScroll12+

PhonePC/2in1TabletTVWearable

onDidScroll(handler: OnScrollCallback): T

滚动组件滑动时触发，返回当前帧滑动的偏移量和当前滑动状态。

说明

从API version 14开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [OnScrollCallback](ts-container-scrollable-common.md#onscrollcallback12) | 是 | 滚动组件滑动时触发的回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### onScroll(deprecated)

PhonePC/2in1TabletTVWearable

onScroll(event: (scrollOffset: number, scrollState: ScrollState) => void): T

滚动组件滑动时触发。

说明

从API version 11开始支持，从API version 12开始废弃，[List](ts-container-list.md)、[Grid](ts-container-grid.md)和[WaterFlow](ts-container-waterflow.md)组件的onScroll事件在布局之后触发，建议使用[onDidScroll](ts-container-scrollable-common.md#ondidscroll12)替代；[Scroll](ts-container-scroll.md)组件的onScroll事件在布局之前触发，建议使用[onWillScroll](ts-container-scrollable-common.md#onwillscroll12)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (scrollOffset: number, scrollState: [ScrollState](ts-container-list.md#scrollstate枚举说明)) => void | 是 | 滚动组件滑动时的回调。  scrollOffset：相对于上一帧的偏移量，滚动组件的内容向上滚动时偏移量为正，向下滚动时偏移量为负。单位vp。  scrollState：当前滑动状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### onWillStartDragging21+

PhonePC/2in1TabletTVWearable

onWillStartDragging(handler: VoidCallback): T

滚动组件开始拖动时触发。

**卡片能力：** 从API version 21开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [VoidCallback](ts-types.md#voidcallback12) | 是 | 滚动组件开始拖动时触发的回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### onWillStopDragging20+

PhonePC/2in1TabletTVWearable

onWillStopDragging(handler: OnWillStopDraggingCallback): T

滚动组件划动离手时触发，使用鼠标滚轮划动时不会触发。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [OnWillStopDraggingCallback](ts-container-scrollable-common.md#onwillstopdraggingcallback20) | 是 | 滚动组件划动离手时触发的回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### onDidStopDragging21+

PhonePC/2in1TabletTVWearable

onDidStopDragging(handler: OnDidStopDraggingCallback): T

滚动组件结束拖拽时触发。

**卡片能力：** 从API version 21开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [OnDidStopDraggingCallback](ts-container-scrollable-common.md#ondidstopdraggingcallback21) | 是 | 滚动组件结束拖动时触发的回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### onWillStartFling21+

PhonePC/2in1TabletTVWearable

onWillStartFling(handler: VoidCallback): T

滚动组件将要开始惯性动效时触发。

说明

* 如果惯性动效通过[fling](ts-container-scroll.md#fling12)方法触发，则onWillStartFling不触发。
* 惯性动效的触发场景参考[flingSpeedLimit](ts-container-scrollable-common.md#flingspeedlimit11)方法的说明。

**卡片能力：** 从API version 21开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [VoidCallback](ts-types.md#voidcallback12) | 是 | 滚动组件将要开始惯性动效时触发的回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

### onDidStopFling21+

PhonePC/2in1TabletTVWearable

onDidStopFling(handler: VoidCallback): T

滚动组件结束惯性动效后触发，进行中的惯性动效被新的滑动事件打断时不触发。

**卡片能力：** 从API version 21开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [VoidCallback](ts-types.md#voidcallback12) | 是 | 滚动组件结束惯性动效后触发的回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前滚动组件。 |

## ItemDragInfo对象说明

PhonePC/2in1TabletTVWearable

拖拽点信息对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 当前拖拽点的x坐标，单位vp。 |
| y | number | 否 | 否 | 当前拖拽点的y坐标，单位vp。 |

## NestedScrollOptions10+对象说明

PhonePC/2in1TabletTVWearable

[nestedScroll](ts-container-scrollable-common.md#nestedscroll11)属性参数对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scrollForward | [NestedScrollMode](ts-appendix-enums.md#nestedscrollmode10) | 否 | 否 | 滚动组件往末尾端滚动时的嵌套滚动选项。 |
| scrollBackward | [NestedScrollMode](ts-appendix-enums.md#nestedscrollmode10) | 否 | 否 | 滚动组件往起始端滚动时的嵌套滚动选项。 |

## EdgeEffectOptions11+对象说明

PhonePC/2in1TabletTVWearable

[edgeEffect](ts-container-scrollable-common.md#edgeeffect11)属性参数对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| alwaysEnabled | boolean | 否 | 否 | 组件内容大小小于组件自身时，设置是否开启滑动效果。设置为true开启滑动效果，设置为false关闭滑动效果。[List](ts-container-list.md)、[Grid](ts-container-grid.md)和[WaterFlow](ts-container-waterflow.md)组件默认值是false，[Scroll](ts-container-scroll.md)组件默认值是true。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| effectEdge18+ | number | 否 | 是 | 设置边缘效果生效的边缘。  如果设置[EffectEdge](ts-container-scrollable-common.md#effectedge18枚举说明).START表示只有起始边生效。如果设置[EffectEdge](ts-container-scrollable-common.md#effectedge18枚举说明).END表示只有末尾边生效。  默认值为[EffectEdge](ts-container-scrollable-common.md#effectedge18枚举说明).START | [EffectEdge](ts-container-scrollable-common.md#effectedge18枚举说明).END表示双边同时生效。当设置为其它异常值时，则默认双边同时生效。  如果需要双边都不生效，可将edgeEffect设置为EdgeEffect.None。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## FadingEdgeOptions14+对象说明

PhonePC/2in1TabletTVWearable

[fadingEdge](ts-container-scrollable-common.md#fadingedge14)属性边缘渐隐参数对象。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fadingEdgeLength | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 设置边缘渐隐长度。 |

## EditModeOptions23+对象说明

PhonePC/2in1TabletTVWearable

List/Grid组件编辑模式选项属性参数对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enableGatherSelectedItemsAnimation | boolean | 否 | 是 | 是否启用多选聚拢动画。设置true时启用聚拢动画，设置为false时关闭聚拢动画。  只有GridItem或ListItem上设置了[bindContextMenu](ts-universal-attributes-menu.md#bindcontextmenu8)且responseType设置为[ResponseType](ts-appendix-enums.md#responsetype8).LongPress、[preview](ts-universal-attributes-menu.md#contextmenuoptions10)参数设置为MenuPreviewMode.IMAGE或CustomBuilder时会显示多选聚拢动画。  如果GridItem或ListItem上设置了[拖拽事件](ts-universal-events-drag-drop.md)，是否聚拢以[dragPreviewOptions](ts-universal-attributes-drag-drop.md#dragpreviewoptions11)设置为准。  默认值：false |
| onGetPreviewBadge | [OnGetPreviewBadgeCallback](ts-container-scrollable-common.md#ongetpreviewbadgecallback23) | 否 | 是 | 即将启动多选长按聚拢动画时，触发用于获取选中数量的回调。  缺省时用Grid或List显示范围内选中item的数量作为多选长按聚拢动画后菜单预览图的角标。 |

## EffectEdge18+枚举说明

PhonePC/2in1TabletTVWearable

表示当前边缘效果要生效的边缘。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| START | 1 | 起始边生效。 |
| END | 2 | 末尾边生效。 |

## ContentClipMode14+枚举说明

PhonePC/2in1TabletTVWearable

表示滚动容器的内容裁剪模式。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

下图是组件配置了边距属性后的示意图，可理解每种枚举对应的裁剪区域。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/ROx-zxMzS_Wsf3GtnXNVFQ/zh-cn_image_0000002552800010.png?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=26C424A16A7265829C06AB7B63B1CE5C6916F9B0808CD8AB1257D510E1AB9DAE)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONTENT\_ONLY | 0 | 按内容区裁剪，对应图中的绿色区域。 |
| BOUNDARY | 1 | 按组件区域裁剪，对应图中的整个蓝色区域。 |
| SAFE\_AREA | 2 | 按组件配置的SafeArea区域裁剪，对应图中的整个黄色区域。 |

## OnWillScrollCallback12+

PhonePC/2in1TabletTVWearable

type OnWillScrollCallback = (scrollOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => void | ScrollResult

滚动组件滑动前触发的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scrollOffset | number | 是 | 相对于上一帧的偏移量，滚动组件的内容向上滚动时偏移量为正，向下滚动时偏移量为负。  单位vp。 |
| scrollState | [ScrollState](ts-container-list.md#scrollstate枚举说明) | 是 | 当前滑动状态。 |
| scrollSource | [ScrollSource](ts-appendix-enums.md#scrollsource12) | 是 | 当前滑动操作的来源。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| void | [ScrollResult](ts-container-scrollable-common.md#scrollresult12对象说明) | 返回ScrollResult时按照开发者指定的相对上一帧的偏移量滑动；不返回时按回调参数scrollOffset滑动。  取值范围：(-∞, +∞) |

## OnScrollCallback12+

PhonePC/2in1TabletTVWearable

type OnScrollCallback = (scrollOffset: number, scrollState: ScrollState) => void

滚动组件滑动时触发的回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scrollOffset | number | 是 | 相对于上一帧的偏移量，滚动组件的内容向上滚动时偏移量为正，向下滚动时偏移量为负。  单位vp。 |
| scrollState | [ScrollState](ts-container-list.md#scrollstate枚举说明) | 是 | 当前滑动状态。 |

## OnItemDragStartCallback23+

PhonePC/2in1TabletTVWearable

type OnItemDragStartCallback = (event: ItemDragInfo, itemIndex: number) => CustomBuilder

开始拖拽列表或网格元素时触发的回调。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ItemDragInfo](ts-container-scrollable-common.md#itemdraginfo对象说明) | 是 | 拖拽点的信息。 |
| itemIndex | number | 是 | 被拖拽列表元素索引值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CustomBuilder](ts-types.md#custombuilder8) | 返回CustomBuilder用于构建被拖拽元素的拖拽图。返回void表示不能拖拽。 |

## OnGetPreviewBadgeCallback23+

PhonePC/2in1TabletTVWearable

type OnGetPreviewBadgeCallback = () => boolean | number

即将启动多选长按聚拢动画时，触发用于获取选中数量的回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | number | 多选长按聚拢动画后菜单预览图是否显示选中数量角标，或需要显示的数量。  返回true表示显示选中数量角标，对应Grid或List显示范围内选中item数量；false表示不显示角标。  返回数字时默认显示角标，该数字表示角标中需要显示的数量。取值范围：[0, 231-1]，超过取值范围时按返回true处理。  返回浮点数时，向下取整。 |

## ScrollResult12+对象说明

PhonePC/2in1TabletTVWearable

[OnWillScrollCallback](ts-container-scrollable-common.md#onwillscrollcallback12)返回值对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offsetRemain | number | 否 | 否 | 将要滑动偏移量，单位vp。 |

## ChildrenMainSize12+对象说明

PhonePC/2in1TabletTVWearable

维护List组件或ListItemGroup组件的子组件在主轴方向的大小信息，仅支持一对一绑定到List组件或ListItemGroup组件。

说明

* 提供的主轴方向大小信息必须与子组件实际在主轴方向的大小一致，子组件在主轴方向大小变化或者增删子组件时都必须通过ChildrenMainSize对象方法通知List组件或ListItemGroup组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(childDefaultSize: number)

ChildrenMainSize有参构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| childDefaultSize | number | 是 | 子组件在主轴方向的默认大小。  单位：vp  **说明：**  必须是有限的非负数值，否则抛出异常。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

### childDefaultSize12+

PhonePC/2in1TabletTVWearable

set childDefaultSize(value: number)

修改子组件在主轴方向的默认大小。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 子组件在主轴方向的默认大小。  单位：vp  **说明：**  必须是有限的非负数值，否则抛出异常。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

get childDefaultSize(): number

获取子组件在主轴方向的默认大小。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 子组件在主轴方向的默认大小。  单位：vp  取值范围：[0, +∞) |

### splice12+

PhonePC/2in1TabletTVWearable

splice(start: number, deleteCount?: number, childrenSize?: Array<number>): void

批量增删改子组件在主轴方向的大小信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 从0开始计算的索引值，表示要开始修改子组件在主轴方向大小信息的位置。  **说明：**  1. 必须是有限的非负数值，否则抛出异常。  2. 非整数会被截断为整数。  3. 超过最大索引值不生效。  取值范围：[0, +∞) |
| deleteCount | number | 否 | 从start开始删除的大小信息的数量。  **说明：**  1. 必须是有限的非负数值，否则处理为0。  2. 非整数会被截断为整数。  3. start + deleteCount - 1可以超过最大索引值，会删除索引值start开始之后的所有子组件的大小信息。  默认值为+∞。  取值范围：[0, +∞) |
| childrenSize | Array<number > | 否 | 要在start位置插入的所有子组件的主轴方向的大小。  Array中各个数值单位：vp  **说明：**  1.数组中数值如果是有限的非负值，则认为是指定的大小，后续不随默认大小的变化而变化。  2. 数组中数值如果不是有限的非负值，会被处理成默认大小，后续会随默认大小的变化而变化。  默认值为空数组。  取值范围：[0, +∞) |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

说明

* 如果仅使用start参数，表示删除索引值start及之后的子组件的大小信息。
* 如果仅使用start和deleteCount参数，表示删除索引值start开始的deleteCount数量的子组件的大小信息。一般在删除子组件时使用。
* 如果使用3个参数，表示删除索引值start开始的deleteCount数量的子组件的大小信息，再在start位置插入childrenSize中所有的大小信息。一般在增加子组件或者批量更新子组件主轴方向大小的时候使用，如果仅是增加子组件，deleteCount为0，childrenSize的元素数量和增加子组件的个数应该相等；如果仅是批量更新子组件主轴方向的大小，childrenSize的元素数量应该和deleteCount相等，即为批量更新的数量。
* 如果想要通知某个子组件的大小为默认大小，childrenSize中对应的值不应该给一个有限的非负值，而应该给NaN，任意负值等能被处理成默认大小的值。

### update12+

PhonePC/2in1TabletTVWearable

update(index: number, childSize: number): void

修改指定索引值对应的子组件的主轴方向的大小信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 从0开始计算的索引值，表示要开始修改子组件在主轴方向大小信息的位置。  **说明：**  1. 必须是有限的非负数值，否则抛出异常。  2. 非整数会被截断为整数。  3. 超过最大索引值不生效。  取值范围：[0, +∞) |
| childSize | number | 是 | 要更新成的大小。  单位：vp  **说明：**  1.数值如果是有限的非负值，则认为是指定的大小，后续不随默认大小的变化而变化。  2. 数值如果不是有限的非负值，会被处理成默认大小，后续会随默认大小的变化而变化。  取值范围：[0, +∞) |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

## UIScrollableCommonEvent19+

PhonePC/2in1TabletTVWearable

用于设置滚动事件回调。

### setOnReachStart19+

PhonePC/2in1TabletTVWearable

setOnReachStart(callback: Callback<void> | undefined): void

设置[onReachStart](ts-container-scrollable-common.md#onreachstart11)事件的回调。

方法入参为undefined的时候，重置对应的事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | undefined | 是 | onReachStart事件的回调函数。 |

### setOnReachEnd19+

PhonePC/2in1TabletTVWearable

setOnReachEnd(callback: Callback<void> | undefined): void

设置[onReachEnd](ts-container-scrollable-common.md#onreachend11)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | undefined | 是 | onReachEnd事件的回调函数。 |

### setOnScrollStart19+

PhonePC/2in1TabletTVWearable

setOnScrollStart(callback: Callback<void> | undefined): void

设置[onScrollStart](ts-container-scrollable-common.md#onscrollstart11)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | undefined | 是 | onScrollStart事件的回调函数。 |

### setOnScrollStop19+

PhonePC/2in1TabletTVWearable

setOnScrollStop(callback: Callback<void> | undefined): void

设置[onScrollStop](ts-container-scrollable-common.md#onscrollstop11)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<void> | undefined | 是 | onScrollStop事件的回调函数。 |

### setOnScrollFrameBegin19+

PhonePC/2in1TabletTVWearable

setOnScrollFrameBegin(callback: OnScrollFrameBeginCallback | undefined): void

设置[onScrollFrameBegin](ts-container-scroll.md#onscrollframebegin9)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnScrollFrameBeginCallback](ts-container-scroll.md#onscrollframebegincallback18) | undefined | 是 | onScrollFrameBegin事件的回调函数。 |

## OnWillStopDraggingCallback20+

PhonePC/2in1TabletTVWearable

type OnWillStopDraggingCallback = (velocity: number) => void

滚动组件划动离手时触发的回调。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| velocity | number | 是 | 划动离手速度，滚动组件的内容向上滚动时速度为正，向下滚动时速度为负。  单位vp/s。 |

## OnDidStopDraggingCallback21+

PhonePC/2in1TabletTVWearable

type OnDidStopDraggingCallback = (willFling: boolean) => void

滚动组件在结束拖拽时触发的回调。

**卡片能力：** 从API version 21开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| willFling | boolean | 是 | 结束拖拽后是否会有惯性动效。返回true代表拖拽结束后有惯性动效，返回false代表没有惯性动效。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（支持滚动手势）

该示例通过设置[enableScrollInteraction](ts-container-scrollable-common.md#enablescrollinteraction11)属性，实现了使用手势滚动纵向列表，并在当前显示界面发生改变时回调索引。

ListDataSource说明及完整代码参考[示例1添加滚动事件](ts-container-list.md#示例1添加滚动事件)。

```
1. // xxx.ets
2. import { ListDataSource } from './ListDataSource';

4. @Entry
5. @Component
6. struct ListExample {
7. private arr: ListDataSource = new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);

9. build() {
10. Column() {
11. List({ space: 20, initialIndex: 0 }) {
12. LazyForEach(this.arr, (item: number) => {
13. ListItem() {
14. Text('' + item)
15. .width('100%')
16. .height(100)
17. .fontSize(16)
18. .textAlign(TextAlign.Center)
19. .borderRadius(10)
20. .backgroundColor(0xFFFFFF)
21. }
22. }, (item: number) => item.toString())
23. }
24. .enableScrollInteraction(true)
25. .listDirection(Axis.Vertical) // 排列方向
26. .scrollBar(BarState.Off)
27. .friction(0.6)
28. .divider({
29. strokeWidth: 2,
30. color: 0xFFFFFF,
31. startMargin: 20,
32. endMargin: 20
33. }) // 每行之间的分界线
34. .edgeEffect(EdgeEffect.Spring) // 边缘效果设置为Spring
35. .onScrollIndex((firstIndex: number, lastIndex: number, centerIndex: number) => {
36. console.info('first' + firstIndex);
37. console.info('last' + lastIndex);
38. console.info('center' + centerIndex);
39. })
40. .onScrollVisibleContentChange((start: VisibleListContentInfo, end: VisibleListContentInfo) => {
41. console.info(' start index: ' + start.index +
42. ' start item group area: ' + start.itemGroupArea +
43. ' start index in group: ' + start.itemIndexInGroup);
44. console.info(' end index: ' + end.index +
45. ' end item group area: ' + end.itemGroupArea +
46. ' end index in group: ' + end.itemIndexInGroup);
47. })
48. .onDidScroll((scrollOffset: number, scrollState: ScrollState) => {
49. console.info(`onScroll scrollState = ScrollState` + scrollState + `, scrollOffset = ` + scrollOffset);
50. })
51. .width('90%')
52. }
53. .width('100%')
54. .height('100%')
55. .backgroundColor(0xDCDCDC)
56. .padding({ top: 5 })
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/bYxvyInuQSm7U2bNI_4sMA/zh-cn_image_0000002583479605.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=EAAD068A8C6AA0ACB75C6D5F2E095BF42C96DF623273E6E26460D4A68BF04740)

### 示例2（设置边缘渐隐）

该示例通过设置[fadingEdge](ts-container-scrollable-common.md#fadingedge14)属性，实现了[List](ts-container-list.md)组件开启边缘渐隐效果并设置边缘渐隐长度。

ListDataSource说明及完整代码参考[示例1添加滚动事件](ts-container-list.md#示例1添加滚动事件)。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';
3. import { ListDataSource } from './ListDataSource';

5. @Entry
6. @Component
7. struct ListExample {
8. private arr: ListDataSource = new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]);
9. scrollerForList: Scroller = new Scroller();

11. build() {
12. Column() {

14. List({ space: 20, initialIndex: 0, scroller: this.scrollerForList }) {
15. LazyForEach(this.arr, (item: number) => {
16. ListItem() {
17. Text('' + item)
18. .width('100%')
19. .height(100)
20. .fontSize(16)
21. .textAlign(TextAlign.Center)
22. .borderRadius(10)
23. .backgroundColor(0xFFFFFF)
24. }
25. }, (item: number) => item.toString())
26. }
27. .fadingEdge(true, { fadingEdgeLength: LengthMetrics.vp(80) })
28. }
29. .width('100%')
30. .height('100%')
31. .backgroundColor(0xDCDCDC)
32. .padding({ top: 5 })
33. }
34. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/lQlI5kVlTrCHj1hX5-_R3Q/zh-cn_image_0000002583439653.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=9F25C0E904092DB8DE99C59D7B87F916ED7C37441F292C29415160F02DEDD9A2)

### 示例3（设置裁剪区域）

该示例通过设置[clipContent](ts-container-scrollable-common.md#clipcontent14)属性，改变组件的内容层裁剪区域。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct ScrollExample {
7. scroller: Scroller = new Scroller();
8. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
9. @State clipContent: ContentClipMode | RectShape | undefined = undefined;

11. build() {
12. Column() {
13. Scroll(this.scroller) {
14. Column() {
15. ForEach(this.arr, (item: number) => {
16. Text(item.toString())
17. .width(300)
18. .height(80)
19. .fontSize(20)
20. .textAlign(TextAlign.Center)
21. .backgroundColor(Color.Grey)
22. }, (item: string) => item)
23. }
24. }
25. .backgroundColor(Color.Blue)
26. .clipContent(this.clipContent)
27. .scrollBar(BarState.Off)
28. .friction(0.6)
29. .width(300)
30. .height('50%')
31. .padding(10)
32. .safeAreaPadding(LengthMetrics.vp(10))
33. .initialOffset({ yOffset: 80 })
34. .margin({ top: 20 })

36. Button('clipContent SAFE_AREA')
37. .onClick(() => {
38. this.clipContent = ContentClipMode.SAFE_AREA;
39. }).margin({ top: 30 })

41. Button('clipContent BOUNDARY')
42. .onClick(() => {
43. this.clipContent = ContentClipMode.BOUNDARY;
44. }).margin({ top: 35 })

46. Button('clipContent CONTENT_ONLY')
47. .onClick(() => {
48. this.clipContent = ContentClipMode.CONTENT_ONLY;
49. }).margin({ top: 40 })
50. }.width('100%').height('100%').backgroundColor(0xDCDCDC)
51. }
52. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/GqCpdk8zQ1SG0qp1_8c58g/zh-cn_image_0000002583439705.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=2BF6AE41A8E08237C1C82C691B96080D5FDB9A16A5D0D3A1252DF27143C83B02)

### 示例4（设置滚动条边距）

从API version 20开始，该示例通过设置[scrollBarMargin](ts-container-scrollable-common.md#scrollbarmargin20)属性，调整滚动组件的滚动条边距。

ListDataSource说明及完整代码参考[示例1添加滚动事件](ts-container-list.md#示例1添加滚动事件)。

```
1. // xxx.ets
2. import { ListDataSource } from './ListDataSource';
3. import { LengthMetrics } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct ListExample {
8. arr: ListDataSource = new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
9. @State scrollBarMargin: ScrollBarMargin = { start: LengthMetrics.vp(0), end: LengthMetrics.vp(0) };

11. build() {
12. Stack({ alignContent: Alignment.TopStart }) {
13. Column() {
14. List({ space: 20, initialIndex: 0 }) {
15. LazyForEach(this.arr, (item: number, index?: number) => {
16. ListItem() {
17. Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) {
18. Text('' + item)
19. .width('100%')
20. .height(80)
21. .fontSize(20)
22. .textAlign(TextAlign.Center)
23. .borderRadius(10)
24. .backgroundColor(Color.White)
25. .flexShrink(1)
26. }
27. }
28. }, (item: number) => item.toString())
29. }.width('90%')
30. .friction(0.6)
31. .scrollBar(BarState.On)
32. .scrollBarMargin(this.scrollBarMargin)
33. }.width('100%')

35. Button('scrollBarMargin')
36. .onClick(() => {
37. this.scrollBarMargin = { start: LengthMetrics.vp(45), end: LengthMetrics.vp(70) };
38. }).margin({ top: 5, left: 20 })

40. Button('scrollBarMargin2')
41. .onClick(() => {
42. this.scrollBarMargin = { start: LengthMetrics.vp(15), end: LengthMetrics.vp(100) };
43. }).margin({ top: 200, left: 20 })
44. }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
45. }
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/dunBPiiVR8KXeH0J5lk_3A/zh-cn_image_0000002552959660.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=8131699A96952E693A686B2603125A35EBF061EA909B4FCEAF8259B6AD5D2912)
