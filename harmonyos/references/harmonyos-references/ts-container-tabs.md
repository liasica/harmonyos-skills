---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs
title: Tabs
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 导航与切换 > Tabs
category: harmonyos-references
scraped_at: 2026-04-28T08:01:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1275f13fb79dd316aca27b61472086217e61f3dc5670acb7a89622c2eefd3389
---

通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。

说明

* 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件从API version 11开始，支持安全区域避让特性，其[expandSafeArea](ts-universal-attributes-expand-safe-area.md#expandsafearea)属性的默认值为expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])。开发者可通过重写该属性覆盖默认行为。对于API version 11之前的版本，则需配合expandSafeArea属性手动实现安全区域避让。

## 子组件

PhonePC/2in1TabletTVWearable

仅支持子组件[TabContent](ts-container-tabcontent.md)，以及渲染控制类型[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)和[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)，不建议自定义组件作为子组件。并且if/else和ForEach下也仅支持TabContent作为子组件，不建议自定义组件作为子组件。

说明

Tabs子组件的visibility属性设置为None，或者visibility属性设置为Hidden时，对应子组件不显示，但依然会在视窗内占位。

已经显示的Tabs子组件TabContent后续隐藏时不会被销毁，若需要页面懒加载和释放，可以参考[示例13](ts-container-tabs.md#示例13页面懒加载和释放)。

Tabs设置[height](ts-universal-attributes-size.md#height)为auto时，可根据子组件高度自适应高度大小。设置[width](ts-universal-attributes-size.md#width)为auto时，可根据子组件宽度自适应宽度大小。

## 接口

PhonePC/2in1TabletTVWearable

Tabs(options?: TabsOptions)

创建Tabs容器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TabsOptions](ts-container-tabs.md#tabsoptions15) | 否 | Tabs组件参数。 |

## TabsOptions15+

PhonePC/2in1TabletTVWearable

Tabs组件参数，设置Tabs的页签位置，当前显示页签的索引，Tabs控制器和TabBar的[通用属性](ts-component-general-attributes.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| barPosition7+ | [BarPosition](ts-container-tabs.md#barposition枚举说明) | 否 | 是 | 设置Tabs的页签位置。  默认值：BarPosition.Start。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| index7+ | number | 否 | 是 | 设置当前显示页签的索引。  默认值：0  **说明：**  设置为小于0的值时按默认值显示。  可选值为[0, TabContent子节点数量-1]。  直接修改index跳页时，切换动效不生效。 使用TabController的changeIndex时，默认生效切换动效，可以设置animationDuration为0关闭动画。  从API version 10开始，该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。  Tabs重建、系统资源切换（如系统字体切换、系统深浅色切换）或者组件属性变化时，会跳转到index对应的页面。若需要在上述情况下不跳转，建议使用双向绑定。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| controller7+ | [TabsController](ts-container-tabs.md#tabscontroller) | 否 | 是 | 设置Tabs控制器。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| barModifier15+ | [CommonModifier](ts-container-tabs.md#commonmodifier15) | 否 | 是 | 设置TabBar的[通用属性](ts-component-general-attributes.md)。  **说明：**  动态置为undefined时会保持当前状态不变，不会重置各通用属性。  由一个CommonModifier切换为另一个CommonModifier时，重复属性会进行覆盖，非重复属性会同时生效，不会重置前一个CommonModifier的通用属性。  Tabs的[barWidth](ts-container-tabs.md#barwidth)、[barHeight](ts-container-tabs.md#barheight)、[barBackgroundColor](ts-container-tabs.md#barbackgroundcolor10)、[barBackgroundBlurStyle](ts-container-tabs.md#barbackgroundblurstyle18)、[barBackgroundEffect](ts-container-tabs.md#barbackgroundeffect18)属性会覆盖CommonModifier的[width](ts-universal-attributes-size.md#width)、[height](ts-universal-attributes-size.md#height)、[backgroundColor](ts-universal-attributes-background.md#backgroundcolor18)、[backgroundBlurStyle](ts-universal-attributes-background.md#backgroundblurstyle18)、[backgroundEffect](ts-universal-attributes-background.md#backgroundeffect18)属性。  [align](ts-universal-attributes-location.md#align)属性仅在[BarMode.Scrollable](ts-container-tabs.md#barmode10-1)模式下生效，且Tabs为横向时还需[nonScrollableLayoutStyle](ts-container-tabs.md#scrollablebarmodeoptions10对象说明)未设置或设置为异常值时才能生效。  [TabContent](ts-container-tabcontent.md)组件的[tabBar](ts-container-tabcontent.md#tabbar18)属性为底部页签样式时不支持拖拽功能。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |

## BarPosition枚举说明

PhonePC/2in1TabletTVWearable

Tabs页签位置枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Start | 0 | vertical属性方法设置为true时，页签位于容器左侧；vertical属性方法设置为false时，页签位于容器顶部。 |
| End | 1 | vertical属性方法设置为true时，页签位于容器右侧；vertical属性方法设置为false时，页签位于容器底部。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### vertical

PhonePC/2in1TabletTVWearable

vertical(value: boolean)

设置是否为纵向Tab。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否为纵向Tab。  默认值：false，横向Tabs，为true时纵向Tabs。  当横向Tabs设置height为auto时，Tabs组件高度自适应子组件高度，即为tabBar高度+divider线宽+TabContent高度+上下padding值+上下border宽度。  当纵向Tabs设置width为auto时，Tabs组件宽度自适应子组件宽度，即为tabBar宽度+divider线宽+TabContent宽度+左右padding值+左右border宽度。  尽量保持每一个页面中的子组件尺寸大小一致，避免滑动页面时出现页面切换动画跳动现象。 |

### scrollable

PhonePC/2in1TabletTVWearable

scrollable(value: boolean)

设置是否可以通过滑动页面进行页面切换。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否可以通过滑动页面进行页面切换。  默认值：true，可以通过滑动页面进行页面切换。为false时不可滑动切换页面。 |

### barMode

PhonePC/2in1TabletTVWearable

barMode(value: BarMode, options?: ScrollableBarModeOptions)

设置TabBar布局模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BarMode](ts-container-tabs.md#barmode枚举说明) | 是 | 布局模式。  默认值：BarMode.Fixed |
| options10+ | [ScrollableBarModeOptions](ts-container-tabs.md#scrollablebarmodeoptions10对象说明) | 否 | Scrollable模式下的TabBar的布局样式。  **说明：**  仅Scrollable且水平模式下有效。 |

### barMode10+

PhonePC/2in1TabletTVWearable

barMode(value: BarMode.Fixed)

设置TabBar布局模式为BarMode.Fixed。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BarMode.Fixed](ts-container-tabs.md#barmode枚举说明) | 是 | 所有TabBar会平均分配barWidth宽度（纵向时平均分配barHeight高度）。 |

### barMode10+

PhonePC/2in1TabletTVWearable

barMode(value: BarMode.Scrollable, options: ScrollableBarModeOptions)

设置TabBar布局模式为BarMode.Scrollable。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BarMode.Scrollable](ts-container-tabs.md#barmode枚举说明) | 是 | 所有TabBar都使用实际布局宽度，超过总宽度（横向Tabs的barWidth，纵向Tabs的barHeight）后可滑动。 |
| options | [ScrollableBarModeOptions](ts-container-tabs.md#scrollablebarmodeoptions10对象说明) | 是 | Scrollable模式下的TabBar的布局样式。  **说明：**  仅水平模式下有效。 |

### barWidth

PhonePC/2in1TabletTVWearable

barWidth(value: Length)

设置TabBar的宽度值。设置为小于0或大于Tabs宽度值时，按默认值显示。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length)8+ | 是 | TabBar的宽度值。  默认值：  未设置[SubTabBarStyle](ts-container-tabcontent.md#subtabbarstyle9)和[BottomTabBarStyle](ts-container-tabcontent.md#bottomtabbarstyle9)的TabBar且vertical属性为false时，默认值为Tabs的宽度。  未设置SubTabBarStyle和BottomTabBarStyle的TabBar且vertical属性为true时，默认值为56vp。  设置SubTabBarStyle样式且vertical属性为false时，默认值为Tabs的宽度。  设置SubTabBarStyle样式且vertical属性为true时，默认值为56vp。  设置BottomTabBarStyle样式且vertical属性为true时，默认值为96vp。  设置BottomTabBarStyle样式且vertical属性为false时，默认值为Tabs的宽度。 |

### barHeight

PhonePC/2in1TabletTVWearable

barHeight(value: Length)

设置TabBar的高度值。横向Tabs可以设置height为'auto'，让TabBar自适应子组件高度。height设置为小于0或大于Tabs高度值时，按默认值显示。

API version 14之前的版本，若设置barHeight为固定值后，TabBar无法扩展底部安全区。从API version 14开始支持配合[safeAreaPadding](ts-universal-attributes-size.md#safeareapadding14)属性，当safeAreaPadding不设置bottom或者bottom设置为0时，可以实现扩展安全区。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length)8+ | 是 | TabBar的高度值。  默认值：  未设置样式或者通过CustomBuilder设置自定义样式的TabBar且vertical属性为false时，默认值为56vp。  未设置样式或者通过CustomBuilder设置自定义样式的TabBar且vertical属性为true时，默认值为Tabs的高度。  设置[SubTabBarStyle](ts-container-tabcontent.md#subtabbarstyle9)样式且vertical属性为false时，默认值为56vp。  设置SubTabBarStyle样式且vertical属性为true时，默认值为Tabs的高度。  设置[BottomTabBarStyle](ts-container-tabcontent.md#bottomtabbarstyle9)样式且vertical属性为true时，默认值为Tabs的高度。  设置BottomTabBarStyle样式且vertical属性为false时，默认值为56vp，从API version 12开始，默认值变更为48vp。 |

### barHeight20+

PhonePC/2in1TabletTVWearable

barHeight(height: Length, noMinHeightLimit: boolean)

设置TabBar的高度值。横向Tabs可以设置height为'auto'，让TabBar自适应子组件高度，并通过设置noMinHeightLimit为true让自适应高度可以小于TabBar默认高度。height设置为小于0或大于Tabs高度值时，按默认值显示。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| height | [Length](ts-types.md#length) | 是 | TabBar的高度值。  默认值：  未设置样式或者通过CustomBuilder设置自定义样式的TabBar且vertical属性为false时，默认值为56vp。  未设置样式或者通过CustomBuilder设置自定义样式的TabBar且vertical属性为true时，默认值为Tabs的高度。  设置[SubTabBarStyle](ts-container-tabcontent.md#subtabbarstyle9)样式且vertical属性为false时，默认值为56vp。  设置SubTabBarStyle样式且vertical属性为true时，默认值为Tabs的高度。  设置[BottomTabBarStyle](ts-container-tabcontent.md#bottomtabbarstyle9)样式且vertical属性为true时，默认值为Tabs的高度。  设置BottomTabBarStyle样式且vertical属性为false时，默认值为48vp。 |
| noMinHeightLimit | boolean | 是 | height设置为'auto'时，设置是否取消TabBar的最小高度限制。默认值为false。  **说明：**  值为true表示取消TabBar的最小高度限制，即TabBar的高度值可以小于默认值。  值为false表示限制TabBar的最小高度，即TabBar的最小高度值等于默认值。 |

### animationCurve20+

PhonePC/2in1TabletTVWearable

animationCurve(curve: Curve | ICurve)

设置Tabs翻页动画曲线。常用曲线参考[Curve](ts-appendix-enums.md#curve)枚举说明，也可以通过[插值计算](js-apis-curve.md)模块提供的接口创建自定义的插值曲线对象。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| curve | [Curve](ts-appendix-enums.md#curve) | [ICurve](js-apis-curve.md#icurve9) | 是 | Tabs翻页的动画曲线。  默认值：  滑动TabContent翻页时，默认值为interpolatingSpring(-1, 1, 228, 30)。  点击TabBar页签和调用TabsController的changeIndex接口翻页时，默认值为cubicBezierCurve(0.2, 0.0, 0.1, 1.0)。  设置自定义动画曲线时，滑动翻页和点击页签、调用changeIndex翻页都使用设置的动画曲线。 |

### animationDuration

PhonePC/2in1TabletTVWearable

animationDuration(value: number)

设置Tabs翻页动画时长。

animationCurve不设置时，由于滑动TabContent翻页动画曲线interpolatingSpring(-1, 1, 228, 30)时长只受曲线自身参数影响，animationDuration只能控制点击TabBar页签和调用TabsController的changeIndex接口切换TabContent的动画时长。

不受animationDuration控制的曲线可以查阅[插值计算](js-apis-curve.md)模块，比如[springMotion](js-apis-curve.md#curvesspringmotion9)、[responsiveSpringMotion](js-apis-curve.md#curvesresponsivespringmotion9)和[interpolatingSpring](js-apis-curve.md#curvesinterpolatingspring10)类型的曲线。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | Tabs翻页的动画时长。  默认值：  API version 10及以前，不设置该属性或设置为null时，默认值为0，即Tabs翻页无动画。设置为小于0或undefined时，默认值为300。  API version 11及以后，不设置该属性或设置为异常值，且设置TabBar为BottomTabBarStyle样式时，默认值为0。设置TabBar为其他样式时，默认值为300。  单位：ms  取值范围：[0, +∞) |

### animationMode12+

PhonePC/2in1TabletTVWearable

animationMode(mode: Optional<AnimationMode>)

设置点击TabBar页签或调用TabsController的changeIndex接口时切换TabContent的动画形式。

说明

此属性不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[AnimationMode](ts-container-tabs.md#animationmode12枚举说明)> | 是 | 点击TabBar页签或调用TabsController的changeIndex接口时切换TabContent的动画形式。  默认值：AnimationMode.CONTENT\_FIRST，表示在点击TabBar页签或调用TabsController的changeIndex接口切换TabContent时，先加载目标页内容，再开始切换动画。 |

### barPosition9+

PhonePC/2in1TabletTVWearable

barPosition(value: BarPosition)

设置Tabs的页签位置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BarPosition](ts-container-tabs.md#barposition枚举说明) | 是 | 设置Tabs的页签位置。  默认值：BarPosition.Start |

### divider10+

PhonePC/2in1TabletTVWearable

divider(value: DividerStyle | null)

设置区分TabBar和TabContent的分割线样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [DividerStyle](ts-container-tabs.md#dividerstyle10对象说明) | null | 是 | 分割线样式，默认不显示分割线。  DividerStyle：分割线的样式；  null：不显示分割线。 |

### fadingEdge10+

PhonePC/2in1TabletTVWearable

fadingEdge(value: boolean)

设置页签超过容器宽度时是否渐隐消失。建议配合barBackgroundColor属性一起使用，如果barBackgroundColor属性没有定义，会默认显示页签末端为白色的渐隐效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 页签超过容器宽度时是否渐隐消失。  默认值：true，页签超过容器宽度时会渐隐消失。设置为false时，页签超过容器宽度直接截断显示，不产生任何渐变效果‌。 |

### barOverlap10+

PhonePC/2in1TabletTVWearable

barOverlap(value: boolean)

设置TabBar是否背后变模糊并叠加在TabContent之上。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | TabBar是否背后变模糊并叠加在TabContent之上。当barOverlap设置为true时，TabBar背后变模糊并叠加在TabContent之上，并且TabBar默认模糊材质的BlurStyle值修改为'BlurStyle.COMPONENT\_THICK'。当barOverlap设置为false时，无模糊和叠加效果。  默认值：false |

### barBackgroundColor10+

PhonePC/2in1TabletTVWearable

barBackgroundColor(value: ResourceColor)

设置TabBar的背景颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | TabBar的背景颜色。  默认值：Color.Transparent，透明 |

### barBackgroundBlurStyle11+

PhonePC/2in1TabletTVWearable

barBackgroundBlurStyle(value: BlurStyle)

设置TabBar的背景模糊材质。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 是 | TabBar的背景模糊材质。  默认值：BlurStyle.NONE |

### barBackgroundBlurStyle18+

PhonePC/2in1TabletTVWearable

barBackgroundBlurStyle(style: BlurStyle, options: BackgroundBlurStyleOptions)

为TabBar提供一种在背景和内容之间的模糊能力，通过枚举值的方式封装了不同的模糊半径、蒙版颜色、蒙版透明度、饱和度、亮度。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 是 | 背景模糊样式。模糊样式中封装了模糊半径、蒙版颜色、蒙版透明度、饱和度、亮度五个参数。 |
| options | [BackgroundBlurStyleOptions](ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 是 | 背景模糊选项。 |

### barGridAlign10+

PhonePC/2in1TabletTVWearable

barGridAlign(value: BarGridColumnOptions)

以栅格化方式设置TabBar的可见区域。具体参见BarGridColumnOptions对象。仅水平模式下有效，[不适用于XS、XL和XXL设备](../harmonyos-guides/arkts-layout-development-grid-layout.md#栅格容器断点)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BarGridColumnOptions](ts-container-tabs.md#bargridcolumnoptions10对象说明) | 是 | 以栅格化方式设置TabBar的可见区域。 |

### edgeEffect12+

PhonePC/2in1TabletTVWearable

edgeEffect(edgeEffect: Optional<EdgeEffect>)

设置边缘回弹效果。

说明

从API version 17开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| edgeEffect | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[EdgeEffect](ts-appendix-enums.md#edgeeffect)> | 是 | 边缘滑动效果。  默认值：EdgeEffect.Spring |

### barBackgroundEffect18+

PhonePC/2in1TabletTVWearable

barBackgroundEffect(options: BackgroundEffectOptions)

设置TabBar背景属性，包含背景模糊半径，亮度，饱和度，颜色等参数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [BackgroundEffectOptions](ts-universal-attributes-background.md#backgroundeffectoptions11) | 是 | 设置TabBar背景属性包括：模糊半径，亮度，饱和度，颜色等。 |

### pageFlipMode15+

PhonePC/2in1TabletTVWearable

pageFlipMode(mode: Optional<PageFlipMode>)

设置鼠标滚轮翻页模式。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PageFlipMode](ts-appendix-enums.md#pageflipmode15)> | 是 | 鼠标滚轮翻页模式。  默认值：PageFlipMode.CONTINUOUS |

### cachedMaxCount19+

PhonePC/2in1TabletTVWearable

cachedMaxCount(count: number, mode: TabsCacheMode)

设置子组件的最大缓存个数及缓存模式。未设置该属性时默认缓存所有子组件且缓存后不会释放。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 子组件的最大缓存个数。超出范围时自动释放不再需要的子组件。  取值范围：[0, +∞)。 |
| mode | [TabsCacheMode](ts-container-tabs.md#tabscachemode19枚举说明) | 是 | 子组件的缓存模式。  默认值：TabsCacheMode.CACHE\_BOTH\_SIDE |

## DividerStyle10+对象说明

PhonePC/2in1TabletTVWearable

分割线样式对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| strokeWidth | [Length](ts-types.md#length) | 否 | 否 | 分割线的线宽（不支持百分比设置）。  默认值：0.0  单位：vp  取值范围：[0, +∞)。 |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 分割线的颜色。  默认值：#33182431 |
| startMargin | [Length](ts-types.md#length) | 否 | 是 | 分割线与侧边栏顶端的距离（不支持百分比设置）。  默认值：0.0  单位：vp  取值范围：[0, +∞)。 |
| endMargin | [Length](ts-types.md#length) | 否 | 是 | 分割线与侧边栏底端的距离（不支持百分比设置）。  默认值：0.0  单位：vp  取值范围：[0, +∞)。 |

## BarGridColumnOptions10+对象说明

PhonePC/2in1TabletTVWearable

TabBar栅格化方式设置的对象，包括栅格模式下的column边距和间隔，以及小、中、大屏下，页签占用的columns数量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| margin | [Dimension](ts-types.md#dimension10) | 否 | 是 | 栅格模式下的column边距（不支持百分比设置）。  默认值：24.0  单位：vp |
| gutter | [Dimension](ts-types.md#dimension10) | 否 | 是 | 栅格模式下的column间隔（不支持百分比设置）。  默认值：24.0  单位：vp |
| sm | number | 否 | 是 | 小屏下，页签占用的columns数量，必须是非负偶数。小屏为大于等于320vp但小于600vp。  默认值为-1，代表页签占用TabBar全部宽度。 |
| md | number | 否 | 是 | 中屏下，页签占用的columns数量，必须是非负偶数。中屏为大于等于600vp但小于800vp。  默认值为-1，代表页签占用TabBar全部宽度。 |
| lg | number | 否 | 是 | 大屏下，页签占用的columns数量，必须是非负偶数。大屏为大于等于840vp但小于1024vp。  默认值为-1，代表页签占用TabBar全部宽度。 |

## ScrollableBarModeOptions10+对象说明

PhonePC/2in1TabletTVWearable

Scrollable模式下的TabBar的布局样式对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| margin | [Dimension](ts-types.md#dimension10) | 否 | 是 | Scrollable模式下的TabBar的左右边距（不支持百分比设置）。  默认值：0.0  单位：vp  取值范围：[0, +∞)。 |
| nonScrollableLayoutStyle | [LayoutStyle](ts-container-tabs.md#layoutstyle10枚举说明) | 否 | 是 | Scrollable模式下不滚动时的页签排布方式。  默认值：LayoutStyle.ALWAYS\_CENTER |

## BarMode枚举说明

PhonePC/2in1TabletTVWearable

TabBar布局模式枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Scrollable | 0 | 每一个TabBar均使用实际布局宽度，超过总长度（横向Tabs的barWidth，纵向Tabs的barHeight）后可滑动。 |
| Fixed | 1 | 所有TabBar平均分配barWidth宽度（纵向时平均分配barHeight高度）。 |

## AnimationMode12+枚举说明

PhonePC/2in1TabletTVWearable

点击TabBar页签时切换TabContent的动画形式枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONTENT\_FIRST | 0 | 先加载目标页内容，再开始切换动画。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ACTION\_FIRST | 1 | 先开始切换动画，再加载目标页内容；生效需要同时需要满足：Tabs的height、width没有设置成auto。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NO\_ANIMATION | 2 | 关闭默认动画。调用TabsController的changeIndex接口切换TabContent时该枚举值不生效。  可以通过设置animationDuration为0实现调用TabsController的changeIndex接口时不带动画。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| CONTENT\_FIRST\_WITH\_JUMP15+ | 3 | 先加载目标页内容，再无动画跳转到目标页附近，最后有动画跳转到目标页。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| ACTION\_FIRST\_WITH\_JUMP15+ | 4 | 先无动画跳转到目标页附近，再有动画跳转到目标页，最后加载目标页内容。此项生效需要同时需要满足：Tabs的height、width没有设置成auto。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |

## LayoutStyle10+枚举说明

PhonePC/2in1TabletTVWearable

Scrollable模式下不滚动时的页签排布方式枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALWAYS\_CENTER | 0 | 当页签内容超过TabBar宽度时，TabBar可滚动。  当页签内容不超过TabBar宽度时，TabBar不可滚动，页签紧凑居中。 |
| ALWAYS\_AVERAGE\_SPLIT | 1 | 当页签内容超过TabBar宽度时，TabBar可滚动。  当页签内容不超过TabBar宽度时，TabBar不可滚动，且所有页签平均分配TabBar宽度。 |
| SPACE\_BETWEEN\_OR\_CENTER | 2 | 当页签内容超过TabBar宽度时，TabBar可滚动。  当页签内容不超过TabBar宽度但超过TabBar宽度一半时，TabBar不可滚动，页签紧凑居中。  当页签内容不超过TabBar宽度一半时，TabBar不可滚动，保证页签居中排列在TabBar宽度一半，且间距相同。 |

## CommonModifier15+

PhonePC/2in1TabletTVWearable

type CommonModifier = CommonModifier

作为Tabs组件的参数对象。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [CommonModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier) | 设置TabBar的通用属性。 |

## TabsCacheMode19+枚举说明

PhonePC/2in1TabletTVWearable

子组件的缓存模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CACHE\_BOTH\_SIDE | 0 | 缓存当前显示的子组件和其两侧的子组件。即当设置cachedMaxCount属性的count值为n时，最多缓存2n+1个子组件。 |
| CACHE\_LATEST\_SWITCHED | 1 | 缓存当前显示的子组件和最近切换过的子组件。即当设置cachedMaxCount属性的count值为n时，最多缓存n+1个子组件。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onChange

PhonePC/2in1TabletTVWearable

onChange(event: Callback<number>)

Tab页签切换后触发的事件。

满足以下任一条件，即可触发该事件：

1、滑动页面进行页面切换时，组件滑动动画结束后触发。

2、通过[控制器](ts-container-tabs.md#tabscontroller)调用[changeIndex](ts-container-tabs.md#changeindex)接口，Tab页签切换后触发。

3、动态修改[状态变量](../harmonyos-guides/arkts-state.md)构造的index属性值，Tab页签切换后触发。

4、点击TabBar页签，Tab页签切换后触发。

说明

使用自定义页签时，在onChange事件中联动可能会导致滑动页面切换后才执行页签联动，引起自定义页签切换效果延迟。建议在[onAnimationStart](ts-container-tabs.md#onanimationstart11)中监听并刷新当前索引，以确保动效能够及时触发。具体实现可参考[示例3](ts-container-tabs.md#示例3自定义页签切换联动)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<number> | 是 | 当前显示的index索引，索引从0开始计算。 |

### onTabBarClick10+

PhonePC/2in1TabletTVWearable

onTabBarClick(event: Callback<number>)

Tab页签点击后触发的事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<number> | 是 | 被点击的index索引，索引从0开始计算。 |

### onAnimationStart11+

PhonePC/2in1TabletTVWearable

onAnimationStart(handler: OnTabsAnimationStartCallback)

切换动画开始时触发该回调。当[animationDuration](ts-container-tabs.md#animationduration)为0时动画关闭且[scrollable](ts-container-tabs.md#scrollable)为false时，不触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [OnTabsAnimationStartCallback](ts-container-tabs.md#ontabsanimationstartcallback18) | 是 | 切换动画开始时触发的回调。 |

### onAnimationEnd11+

PhonePC/2in1TabletTVWearable

onAnimationEnd(handler: OnTabsAnimationEndCallback)

切换动画结束时触发该回调，包括动画过程中手势中断。当animationDuration为0时动画关闭，不触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [OnTabsAnimationEndCallback](ts-container-tabs.md#ontabsanimationendcallback18) | 是 | 切换动画结束时触发的回调。 |

### onGestureSwipe11+

PhonePC/2in1TabletTVWearable

onGestureSwipe(handler: OnTabsGestureSwipeCallback)

在页面跟手滑动过程中，逐帧触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [OnTabsGestureSwipeCallback](ts-container-tabs.md#ontabsgestureswipecallback18) | 是 | 在页面跟手滑动过程中，逐帧触发的回调。 |

### customContentTransition11+

PhonePC/2in1TabletTVWearable

customContentTransition(delegate: TabsCustomContentTransitionCallback)

自定义Tabs页面切换动画。

使用说明：

1. 当使用自定义切换动画时，Tabs组件自带的默认切换动画会被禁用，同时，页面也无法跟手滑动。
2. 当设置为undefined时，表示不使用自定义切换动画，仍然使用组件自带的默认切换动画。
3. 当前自定义切换动画不支持打断。
4. 目前自定义切换动画只支持两种场景触发：点击页签和调用TabsController.changeIndex()接口。
5. 当使用自定义切换动画时，Tabs组件支持的事件中，除了onGestureSwipe，其他事件均支持。
6. onChange和onAnimationEnd事件的触发时机需要特殊说明：如果在第一次自定义动画执行过程中，触发了第二次自定义动画，那么在开始第二次自定义动画时，就会触发第一次自定义动画的onChange和onAnimationEnd事件。
7. 当使用自定义动画时，参与动画的页面布局方式会改为Stack布局。如果开发者未主动设置相关页面的zIndex属性，那么所有页面的zIndex值是一样的，页面的渲染层级会按照在组件树上的顺序（即页面的index值顺序）确定。因此，开发者需要主动修改页面的zIndex属性，来控制页面的渲染层级。
8. 此属性不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| delegate | [TabsCustomContentTransitionCallback](ts-container-tabs.md#tabscustomcontenttransitioncallback18) | 是 | 自定义Tabs页面切换动画开始时触发的回调。 |

### onContentWillChange12+

PhonePC/2in1TabletTVWearable

onContentWillChange(handler: OnTabsContentWillChangeCallback)

自定义Tabs页面切换拦截事件能力，新页面即将显示时触发该回调。

满足以下任一条件，即可触发该事件：

1、滑动TabContent切换新页面时触发。

2、通过TabsController.changeIndex接口切换新页面时触发。

3、通过动态修改index属性值切换新页面时触发。

4、通过点击TabBar页签切换新页面时触发。

5、TabBar页签获焦后，通过键盘左右方向键等切换新页面时触发。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [OnTabsContentWillChangeCallback](ts-container-tabs.md#ontabscontentwillchangecallback18) | 是 | 自定义Tabs页面切换拦截事件能力，新页面即将显示时触发的回调。 |

### onSelected18+

PhonePC/2in1TabletTVWearable

onSelected(event: Callback<number>)

当选中元素改变时触发该回调，返回值为当前选中的元素的索引值。

满足以下任一条件，即可触发该事件：

1. 滑动离手时满足翻页阈值，开始切换动画时触发。
2. 通过[TabsController控制器](ts-container-tabs.md#tabscontroller)调用[changeIndex](ts-container-tabs.md#changeindex)接口，开始切换动画时触发。
3. 动态修改[状态变量](../harmonyos-guides/arkts-state.md)构造的index属性值后触发。
4. 通过页签处点击触发。

说明

onSelected回调中不可通过[TabsOptions](ts-container-tabs.md#tabsoptions15)的index设置当前显示页的索引，不可调用TabsController.changeIndex()方法。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<number> | 是 | 当前选中元素的索引。 |

### onUnselected18+

PhonePC/2in1TabletTVWearable

onUnselected(event: Callback<number>)

当选中元素改变时触发该回调，返回值为将要隐藏的元素的索引值。

满足以下任一条件，即可触发该事件：

1. 滑动离手时满足翻页阈值，开始切换动画时触发。
2. 通过[TabsController控制器](ts-container-tabs.md#tabscontroller)调用[changeIndex](ts-container-tabs.md#changeindex)接口，开始切换动画时触发。
3. 动态修改[状态变量](../harmonyos-guides/arkts-state.md)构造的index属性值后触发。
4. 通过页签处点击触发。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<number> | 是 | 将要隐藏元素的索引。 |

说明

onUnselected回调中不可通过TabsOptions的index设置当前显示页的索引，不可调用TabsController.changeIndex()方法。

### onContentDidScroll23+

PhonePC/2in1TabletTVWearable

onContentDidScroll(handler: OnTabsContentDidScrollCallback | undefined)

监听Tabs页面滑动事件。

在页面滑动过程中，会对视窗内所有页面逐帧触发[OnTabsContentDidScrollCallback](ts-container-tabs.md#ontabscontentdidscrollcallback23)回调。例如，当视窗内有下标为0、1的两个页面时，会每帧触发两次index值分别为0和1的回调。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [OnTabsContentDidScrollCallback](ts-container-tabs.md#ontabscontentdidscrollcallback23) | undefined | 是 | Tabs滑动时触发的回调，undefined会解绑原有回调。 |

## OnTabsAnimationStartCallback18+

PhonePC/2in1TabletTVWearable

type OnTabsAnimationStartCallback = (index: number, targetIndex: number, extraInfo: TabsAnimationEvent) => void

切换动画开始时触发的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前显示元素的索引，索引从0开始。 |
| targetIndex | number | 是 | 切换动画目标元素的索引，索引从0开始。 |
| extraInfo | [TabsAnimationEvent](ts-container-tabs.md#tabsanimationevent11对象说明) | 是 | 动画相关信息，包括主轴方向上当前显示元素和目标元素相对Tabs起始位置的位移，以及离手速度。 |

## OnTabsAnimationEndCallback18+

PhonePC/2in1TabletTVWearable

type OnTabsAnimationEndCallback = (index: number, extraInfo: TabsAnimationEvent) => void

切换动画结束时触发的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前显示元素的索引，索引从0开始。 |
| extraInfo | [TabsAnimationEvent](ts-container-tabs.md#tabsanimationevent11对象说明) | 是 | 动画相关信息，只返回主轴方向上当前显示元素相对于Tabs起始位置的位移。 |

## OnTabsGestureSwipeCallback18+

PhonePC/2in1TabletTVWearable

type OnTabsGestureSwipeCallback = (index: number, extraInfo: TabsAnimationEvent) => void

在页面跟手滑动过程中，逐帧触发的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前显示元素的索引，索引从0开始。  取值范围：[0, 索引值-1] |
| extraInfo | [TabsAnimationEvent](ts-container-tabs.md#tabsanimationevent11对象说明) | 是 | 动画相关信息，只返回主轴方向上当前显示元素相对于Tabs起始位置的位移。 |

## TabsCustomContentTransitionCallback18+

PhonePC/2in1TabletTVWearable

type TabsCustomContentTransitionCallback = (from: number, to: number) => TabContentAnimatedTransition | undefined

自定义Tabs页面切换动画开始时触发的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | number | 是 | 动画开始时，当前页面的index值，索引从0开始。  取值范围：[0, 索引值-1]，当设置的值超过索引值或小于0时无转场动画。 |
| to | number | 是 | 动画开始时，目标页面的index值，索引从0开始。  取值范围：[0, 索引值-1]，当设置的值超过索引值或小于0时无转场动画。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TabContentAnimatedTransition](ts-container-tabs.md#tabcontentanimatedtransition11) | undefined | 自定义切换动画相关信息。 |

## OnTabsContentWillChangeCallback18+

PhonePC/2in1TabletTVWearable

type OnTabsContentWillChangeCallback = (currentIndex: number, comingIndex: number) => boolean

自定义Tabs页面切换拦截事件能力，新页面即将显示时触发的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| currentIndex | number | 是 | 当前显示页面的index索引，索引从0开始计算。 |
| comingIndex | number | 是 | 将要显示的新页面的index索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当回调函数handler的返回值为true时，Tabs可以切换到新页面。  当回调函数handler的返回值为false时，Tabs无法切换到新页面，仍然显示原来页面内容。 |

## TabsAnimationEvent11+对象说明

PhonePC/2in1TabletTVWearable

Tabs组件动画相关信息集合。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| currentOffset | number | 否 | 否 | Tabs当前显示元素在主轴方向上，相对于Tabs起始位置的位移。单位vp，默认值为0。 |
| targetOffset | number | 否 | 否 | Tabs动画目标元素在主轴方向上，相对于Tabs起始位置的位移。单位vp，默认值为0。 |
| velocity | number | 否 | 否 | Tabs离手动画开始时的离手速度。单位vp/s，默认值为0。 |

## TabContentAnimatedTransition11+

PhonePC/2in1TabletTVWearable

Tabs自定义切换动画相关信息。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number | 否 | 是 | Tabs自定义切换动画超时时间。从自定义动画开始切换计时，如果到达该时间后，开发者仍未调用[TabContentTransitionProxy](ts-container-tabs.md#tabcontenttransitionproxy11)的finishTransition接口通知Tabs组件自定义动画结束，那么组件就会认为此次自定义动画已结束，直接执行后续操作。  默认值：1000  单位：ms  取值范围：[0, +∞)。 |
| transition | [Callback](ts-types.md#callback12)<[TabContentTransitionProxy](ts-container-tabs.md#tabcontenttransitionproxy11)> | 否 | 否 | 自定义切换动画具体内容。 |

## TabContentTransitionProxy11+

PhonePC/2in1TabletTVWearable

Tabs自定义切换动画执行过程中，返回给开发者的proxy对象。开发者可通过该对象获取自定义动画的起始和目标页面信息，同时，也可以通过调用该对象的finishTransition接口通知Tabs组件自定义动画已结束。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| from | number | 否 | 否 | 自定义动画起始页面对应的index值，索引从0开始。 |
| to | number | 否 | 否 | 自定义动画目标页面对应的index值，索引从0开始。 |

### finishTransition

PhonePC/2in1TabletTVWearable

finishTransition(): void

通知Tabs组件，此页面的自定义动画已结束。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## OnTabsContentDidScrollCallback23+

PhonePC/2in1TabletTVWearable

type OnTabsContentDidScrollCallback = (selectedIndex: number, index: number, position: number, mainAxisLength: number) => void

Tabs滑动时触发的回调。

说明

* 例如，当前选中的页签索引为0，从第0页切换到第1页的动画过程中，每帧都会对视窗内所有页面触发回调，当视窗内有第0页和第1页两页时，每帧会触发两次回调。其中，第一次回调的selectedIndex为0、index为0、position为当前帧第0页相对于动画开始前第0页的移动比例，mainAxisLength为主轴方向上第0页的长度。第二次回调的selectedIndex仍为0、index为1、position为当前帧第1页相对于动画开始前第0页的移动比例，mainAxisLength为主轴方向上第1页的长度。
* 若动画曲线为弹簧插值曲线，从第0页切换到第1页的动画过程中，可能会因为离手时的位置和速度，先过滑到第2页，再回弹到第1页，该过程中每帧会对视窗内第1页和第2页触发回调。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectedIndex | number | 是 | 当前选中页面的索引。例如，当前选中的页签索引为0，从第0页切换到第1页的动画过程中，每一次回调的selectedIndex都为0。 |
| index | number | 是 | 视窗内页面的索引。例如，页面滑动过程中，视窗内有第0页和第1页两页时，每帧会触发两次回调。其中，第一次回调的index为0，第二次回调的index为1。 |
| position | number | 是 | index页面相对于Tabs主轴起始位置（selectedIndex对应页面的起始位置）的移动比例。例如，一个横向Tabs中，当前选中的页签索引为0，从第0页往左切换到第1页的动画过程中，若刚好有一帧第0页和第1页分别占用视窗的30%和70%时，当前帧会触发两次回调。其中，第一次回调的position为-0.7，表示当前帧第0页在Tabs主轴起始位置的左侧，且第0页左侧位置距离Tabs主轴起始位置为视窗的70%，即第0页往左移动了视窗70%的距离。第二次回调的position为0.3，表示当前帧第1页在Tabs主轴起始位置的右侧，且第1页左侧位置距离Tabs主轴起始位置为视窗的30%，实际上第1页也是往左移动了视窗70%的距离。 |
| mainAxisLength | number | 是 | index对应页面在主轴方向上的长度，单位vp。例如，某一次回调的index为0，这一次回调的mainAxisLength为360，则表示当前帧第0页在主轴方向上的长度为360vp。横向Tabs代表的是页面宽度，竖向Tabs代表的是页面高度。 |

## TabsController

PhonePC/2in1TabletTVWearable

Tabs组件的控制器，用于控制Tabs组件进行页签切换。不支持一个TabsController控制多个Tabs组件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor

PhonePC/2in1TabletTVWearable

constructor()

TabsController的构造函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### changeIndex

PhonePC/2in1TabletTVWearable

changeIndex(value: number): void

控制Tabs切换到指定页签。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 页签在Tabs里的索引值，索引值从0开始。  **说明：**  设置小于0或大于最大数量的值时，取默认值0。 |

### preloadItems12+

PhonePC/2in1TabletTVWearable

preloadItems(indices: Optional<Array<number>>): Promise<void>

控制Tabs预加载指定子节点。调用该接口后会一次性加载所有指定的子节点，因此为了性能考虑，建议分批加载子节点。

说明

* Tabs的preloadItems需要在Tabs创建之后去调用，首次预加载推荐在Tabs的[onAppear](ts-universal-events-show-hide.md#onappear)生命周期中去控制。
* 如果TabsController对象未绑定任何Tabs组件，直接调用该接口，会抛出JS异常。因此使用该接口时，建议通过try-catch捕获异常。
* 使用preloadItems预加载标签页时，若需自定义TabBar上的显示内容，推荐使用ComponentContent实现，使用示例请参考[示例10](ts-container-tabcontent.md#示例10通过componentcontent设置tabbar)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| indices | [Optional](ts-universal-attributes-custom-property.md#optionalt)<Array<number>> | 是 | 需预加载的子节点的下标数组。  默认值：空数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 预加载完成后触发的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter invalid. Possible causes: 1. The parameter type is not Array<number>; 2. The parameter is an empty array; 3. The parameter contains an invalid index. |

### setTabBarTranslate13+

PhonePC/2in1TabletTVWearable

setTabBarTranslate(translate: TranslateOptions): void

设置TabBar的平移距离。

说明

当使用[bindTabsToScrollable](arkts-apis-uicontext-uicontext.md#bindtabstoscrollable13)或[bindTabsToNestedScrollable](arkts-apis-uicontext-uicontext.md#bindtabstonestedscrollable13)等接口绑定了Tabs组件和可滚动容器组件后，在滑动可滚动容器组件时，会触发所有与其绑定的Tabs组件的TabBar的显示和隐藏动效，调用setTabBarTranslate接口设置的TabBar平移距离会失效。因此不建议同时使用bindTabsToScrollable、bindTabsToNestedScrollable和setTabBarTranslate接口。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| translate | [TranslateOptions](ts-universal-attributes-transformation.md#translateoptions对象说明) | 是 | 设置TabBar的平移距离。 |

### setTabBarOpacity13+

PhonePC/2in1TabletTVWearable

setTabBarOpacity(opacity: number): void

设置TabBar的不透明度。

说明

当使用[bindTabsToScrollable](arkts-apis-uicontext-uicontext.md#bindtabstoscrollable13)或[bindTabsToNestedScrollable](arkts-apis-uicontext-uicontext.md#bindtabstonestedscrollable13)等接口绑定了Tabs组件和可滚动容器组件后，在滑动可滚动容器组件时，会触发所有与其绑定的Tabs组件的TabBar的显示和隐藏动效，调用setTabBarOpacity接口设置的TabBar不透明度会失效。因此不建议同时使用bindTabsToScrollable、bindTabsToNestedScrollable和setTabBarOpacity接口。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| opacity | number | 是 | 设置TabBar的不透明度，取值范围为[0.0, 1.0]，设置的值小于0.0时，按0.0处理，设置的值大于1.0时，按1.0处理。  默认值：1.0。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置TabBar的布局模式）

本示例通过barMode分别实现了页签均分布局和以实际长度布局，且展示了当页签布局长度之和超过了TabBar总长度后可滑动的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabsExample {
5. @State text: string = '文本';
6. @State barMode: BarMode = BarMode.Fixed;

8. build() {
9. Column() {
10. Row() {
11. Button('文本增加 ')
12. .width('47%')
13. .height(50)
14. .onClick((event?: ClickEvent) => {
15. this.text += '文本增加';
16. })
17. .margin({ right: '6%', bottom: '12vp' })

19. Button('文本重置')
20. .width('47%')
21. .height(50)
22. .onClick((event?: ClickEvent) => {
23. this.text = '文本';
24. })
25. .margin({ bottom: '12vp' })
26. }

28. Row() {
29. Button('BarMode.Fixed')
30. .width('47%')
31. .height(50)
32. .onClick((event?: ClickEvent) => {
33. this.barMode = BarMode.Fixed;
34. })
35. .margin({ right: '6%', bottom: '12vp' })

37. Button('BarMode.Scrollable')
38. .width('47%')
39. .height(50)
40. .onClick((event?: ClickEvent) => {
41. this.barMode = BarMode.Scrollable;
42. })
43. .margin({ bottom: '12vp' })
44. }

46. Tabs() {
47. TabContent() {
48. Column().width('100%').height('100%').backgroundColor(Color.Pink)
49. }.tabBar(SubTabBarStyle.of(this.text))

51. TabContent() {
52. Column().width('100%').height('100%').backgroundColor(Color.Green)
53. }.tabBar(SubTabBarStyle.of(this.text))

55. TabContent() {
56. Column().width('100%').height('100%').backgroundColor(Color.Blue)
57. }.tabBar(SubTabBarStyle.of(this.text))
58. }
59. .height('60%')
60. .backgroundColor(0xf1f3f5)
61. .barMode(this.barMode)
62. }
63. .width('100%')
64. .height(500)
65. .padding('24vp')
66. }
67. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/qg4WAxoQQiuqs0xgIioM6g/zh-cn_image_0000002552959676.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=3748FF50DF9B046A25D195EB11680944C5BB97BDA2027DF145865159E5B8FB01)

### 示例2（设置Scrollable模式下的TabBar的布局样式）

本示例实现了barMode的ScrollableBarModeOptions参数，该参数仅在Scrollable模式下有效。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabsExample6 {
5. private controller: TabsController = new TabsController();
6. @State scrollMargin: number = 0;
7. @State layoutStyle: LayoutStyle = LayoutStyle.ALWAYS_CENTER;
8. @State text: string = '文本';

10. build() {
11. Column() {
12. Row() {
13. Button('scrollMargin+10 ' + this.scrollMargin)
14. .width('47%')
15. .height(50)
16. .margin({ top: 5 })
17. .onClick((event?: ClickEvent) => {
18. this.scrollMargin += 10;
19. })
20. .margin({ right: '6%', bottom: '12vp' })
21. Button('scrollMargin-10 ' + this.scrollMargin)
22. .width('47%')
23. .height(50)
24. .margin({ top: 5 })
25. .onClick((event?: ClickEvent) => {
26. this.scrollMargin -= 10;
27. })
28. .margin({ bottom: '12vp' })
29. }

31. Row() {
32. Button('文本增加 ')
33. .width('47%')
34. .height(50)
35. .margin({ top: 5 })
36. .onClick((event?: ClickEvent) => {
37. this.text += '文本增加';
38. })
39. .margin({ right: '6%', bottom: '12vp' })
40. Button('文本重置')
41. .width('47%')
42. .height(50)
43. .margin({ top: 5 })
44. .onClick((event?: ClickEvent) => {
45. this.text = '文本';
46. })
47. .margin({ bottom: '12vp' })
48. }

50. Row() {
51. Button('layoutStyle.ALWAYS_CENTER')
52. .width('100%')
53. .height(50)
54. .margin({ top: 5 })
55. .fontSize(15)
56. .onClick((event?: ClickEvent) => {
57. this.layoutStyle = LayoutStyle.ALWAYS_CENTER;
58. })
59. .margin({ bottom: '12vp' })
60. }

62. Row() {
63. Button('layoutStyle.ALWAYS_AVERAGE_SPLIT')
64. .width('100%')
65. .height(50)
66. .margin({ top: 5 })
67. .fontSize(15)
68. .onClick((event?: ClickEvent) => {
69. this.layoutStyle = LayoutStyle.ALWAYS_AVERAGE_SPLIT;
70. })
71. .margin({ bottom: '12vp' })
72. }

74. Row() {
75. Button('layoutStyle.SPACE_BETWEEN_OR_CENTER')
76. .width('100%')
77. .height(50)
78. .margin({ top: 5 })
79. .fontSize(15)
80. .onClick((event?: ClickEvent) => {
81. this.layoutStyle = LayoutStyle.SPACE_BETWEEN_OR_CENTER;
82. })
83. .margin({ bottom: '12vp' })
84. }

86. Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
87. TabContent() {
88. Column().width('100%').height('100%').backgroundColor(Color.Pink)
89. }.tabBar(SubTabBarStyle.of(this.text))

91. TabContent() {
92. Column().width('100%').height('100%').backgroundColor(Color.Green)
93. }.tabBar(SubTabBarStyle.of(this.text))

95. TabContent() {
96. Column().width('100%').height('100%').backgroundColor(Color.Blue)
97. }.tabBar(SubTabBarStyle.of(this.text))
98. }
99. .animationDuration(300)
100. .height('60%')
101. .backgroundColor(0xf1f3f5)
102. .barMode(BarMode.Scrollable, { margin: this.scrollMargin, nonScrollableLayoutStyle: this.layoutStyle })
103. }
104. .width('100%')
105. .height(500)
106. .margin({ top: 5 })
107. .padding('24vp')
108. }
109. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/eraUYaZeQEOvWHSoaCqOvg/zh-cn_image_0000002583479677.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=81046901B6CF9B593A9F67E8AAD1A5978C06B9AC1719D4FA598268E42374BE16)

### 示例3（自定义页签切换联动）

本示例通过onAnimationStart、onChange实现切换时自定义tabBar和TabContent的联动。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabsExample {
5. @State fontColor: string = '#182431';
6. @State selectedFontColor: string = '#007DFF';
7. @State currentIndex: number = 0;
8. @State selectedIndex: number = 0;
9. private controller: TabsController = new TabsController();

11. @Builder tabBuilder(index: number, name: string) {
12. Column() {
13. Text(name)
14. .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
15. .fontSize(16)
16. .fontWeight(this.selectedIndex === index ? 500 : 400)
17. .lineHeight(22)
18. .margin({ top: 17, bottom: 7 })
19. Divider()
20. .strokeWidth(2)
21. .color('#007DFF')
22. .opacity(this.selectedIndex === index ? 1 : 0)
23. }.width('100%')
24. }

26. build() {
27. Column() {
28. Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
29. TabContent() {
30. Column().width('100%').height('100%').backgroundColor('#00CB87')
31. }.tabBar(this.tabBuilder(0, 'green'))

33. TabContent() {
34. Column().width('100%').height('100%').backgroundColor('#007DFF')
35. }.tabBar(this.tabBuilder(1, 'blue'))

37. TabContent() {
38. Column().width('100%').height('100%').backgroundColor('#FFBF00')
39. }.tabBar(this.tabBuilder(2, 'yellow'))

41. TabContent() {
42. Column().width('100%').height('100%').backgroundColor('#E67C92')
43. }.tabBar(this.tabBuilder(3, 'pink'))
44. }
45. .vertical(false)
46. .barMode(BarMode.Fixed)
47. .barWidth(360)
48. .barHeight(56)
49. .animationDuration(400)
50. .onChange((index: number) => {
51. // currentIndex控制TabContent显示页签
52. this.currentIndex = index;
53. this.selectedIndex = index;
54. })
55. .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
56. if (index === targetIndex) {
57. return;
58. }
59. // selectedIndex控制自定义TabBar内Image和Text颜色切换
60. this.selectedIndex = targetIndex;
61. })
62. .width(360)
63. .height(296)
64. .margin({ top: 52 })
65. .backgroundColor('#F1F3F5')
66. }.width('100%')
67. }
68. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/mqEznu4dQ2eVhguuivpAjQ/zh-cn_image_0000002552800028.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=D2A247EA6661565DCE048AB091EB460DCFB62A37A2D8CB901C53E2D78ECA9880)

### 示例4（分割线基本属性）

本示例通过divider实现了分割线各种属性的展示。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabsDivider1 {
5. private controller1: TabsController = new TabsController();
6. @State dividerColor: string = 'red';
7. @State strokeWidth: number = 2;
8. @State startMargin: number = 0;
9. @State endMargin: number = 0;
10. @State nullFlag: boolean = false;

12. build() {
13. Column() {
14. Tabs({ controller: this.controller1 }) {
15. TabContent() {
16. Column().width('100%').height('100%').backgroundColor(Color.Pink)
17. }.tabBar('pink')

19. TabContent() {
20. Column().width('100%').height('100%').backgroundColor(Color.Yellow)
21. }.tabBar('yellow')

23. TabContent() {
24. Column().width('100%').height('100%').backgroundColor(Color.Blue)
25. }.tabBar('blue')

27. TabContent() {
28. Column().width('100%').height('100%').backgroundColor(Color.Green)
29. }.tabBar('green')

31. TabContent() {
32. Column().width('100%').height('100%').backgroundColor(Color.Red)
33. }.tabBar('red')
34. }
35. .vertical(true)
36. .scrollable(true)
37. .barMode(BarMode.Fixed)
38. .barWidth(70)
39. .barHeight(200)
40. .animationDuration(400)
41. .onChange((index: number) => {
42. console.info(index.toString());
43. })
44. .height('200vp')
45. .margin({ bottom: '12vp' })
46. .divider(this.nullFlag ? null : {
47. strokeWidth: this.strokeWidth,
48. color: this.dividerColor,
49. startMargin: this.startMargin,
50. endMargin: this.endMargin
51. })

53. Button('常规Divider').width('100%').margin({ bottom: '12vp' })
54. .onClick(() => {
55. this.nullFlag = false;
56. this.strokeWidth = 2;
57. this.dividerColor = 'red';
58. this.startMargin = 0;
59. this.endMargin = 0;
60. })
61. Button('空Divider').width('100%').margin({ bottom: '12vp' })
62. .onClick(() => {
63. this.nullFlag = true;
64. })
65. Button('颜色变为蓝色').width('100%').margin({ bottom: '12vp' })
66. .onClick(() => {
67. this.dividerColor = 'blue';
68. })
69. Button('宽度增加').width('100%').margin({ bottom: '12vp' })
70. .onClick(() => {
71. this.strokeWidth += 2;
72. })
73. Button('宽度减小').width('100%').margin({ bottom: '12vp' })
74. .onClick(() => {
75. if (this.strokeWidth > 2) {
76. this.strokeWidth -= 2;
77. }
78. })
79. Button('上边距增加').width('100%').margin({ bottom: '12vp' })
80. .onClick(() => {
81. this.startMargin += 2;
82. })
83. Button('上边距减少').width('100%').margin({ bottom: '12vp' })
84. .onClick(() => {
85. if (this.startMargin > 2) {
86. this.startMargin -= 2;
87. }
88. })
89. Button('下边距增加').width('100%').margin({ bottom: '12vp' })
90. .onClick(() => {
91. this.endMargin += 2;
92. })
93. Button('下边距减少').width('100%').margin({ bottom: '12vp' })
94. .onClick(() => {
95. if (this.endMargin > 2) {
96. this.endMargin -= 2;
97. }
98. })
99. }.padding({ top: '24vp', left: '24vp', right: '24vp' })
100. }
101. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/n0LQpYHJSieIh4kr_H7Nmg/zh-cn_image_0000002583439723.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=2BE0F19769A120F0EA15F23400544709553A523C7EB52E1B5DAADF9B91F94A59)

### 示例5（设置TabBar渐隐）

本示例通过fadingEdge实现了切换子页签渐隐和不渐隐。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabsOpaque {
5. @State message: string = 'Hello World';
6. private controller: TabsController = new TabsController();
7. private controller1: TabsController = new TabsController();
8. @State selfFadingFade: boolean = true;

10. build() {
11. Column() {
12. Button('子页签设置渐隐').width('100%').margin({ bottom: '12vp' })
13. .onClick((event?: ClickEvent) => {
14. this.selfFadingFade = true;
15. })
16. Button('子页签设置不渐隐').width('100%').margin({ bottom: '12vp' })
17. .onClick((event?: ClickEvent) => {
18. this.selfFadingFade = false;
19. })
20. Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
21. TabContent() {
22. Column().width('100%').height('100%').backgroundColor(Color.Pink)
23. }.tabBar('pink')

25. TabContent() {
26. Column().width('100%').height('100%').backgroundColor(Color.Yellow)
27. }.tabBar('yellow')

29. TabContent() {
30. Column().width('100%').height('100%').backgroundColor(Color.Blue)
31. }.tabBar('blue')

33. TabContent() {
34. Column().width('100%').height('100%').backgroundColor(Color.Green)
35. }.tabBar('green')

37. TabContent() {
38. Column().width('100%').height('100%').backgroundColor(Color.Green)
39. }.tabBar('green')

41. TabContent() {
42. Column().width('100%').height('100%').backgroundColor(Color.Green)
43. }.tabBar('green')

45. TabContent() {
46. Column().width('100%').height('100%').backgroundColor(Color.Green)
47. }.tabBar('green')

49. TabContent() {
50. Column().width('100%').height('100%').backgroundColor(Color.Green)
51. }.tabBar('green')
52. }
53. .vertical(false)
54. .scrollable(true)
55. .barMode(BarMode.Scrollable)
56. .barHeight(80)
57. .animationDuration(400)
58. .onChange((index: number) => {
59. console.info(index.toString());
60. })
61. .fadingEdge(this.selfFadingFade)
62. .height('30%')
63. .width('100%')

65. Tabs({ barPosition: BarPosition.Start, controller: this.controller1 }) {
66. TabContent() {
67. Column().width('100%').height('100%').backgroundColor(Color.Pink)
68. }.tabBar('pink')

70. TabContent() {
71. Column().width('100%').height('100%').backgroundColor(Color.Yellow)
72. }.tabBar('yellow')

74. TabContent() {
75. Column().width('100%').height('100%').backgroundColor(Color.Blue)
76. }.tabBar('blue')

78. TabContent() {
79. Column().width('100%').height('100%').backgroundColor(Color.Green)
80. }.tabBar('green')

82. TabContent() {
83. Column().width('100%').height('100%').backgroundColor(Color.Green)
84. }.tabBar('green')

86. TabContent() {
87. Column().width('100%').height('100%').backgroundColor(Color.Green)
88. }.tabBar('green')
89. }
90. .vertical(true)
91. .scrollable(true)
92. .barMode(BarMode.Scrollable)
93. .barHeight(200)
94. .barWidth(80)
95. .animationDuration(400)
96. .onChange((index: number) => {
97. console.info(index.toString());
98. })
99. .fadingEdge(this.selfFadingFade)
100. .height('30%')
101. .width('100%')
102. }
103. .padding({ top: '24vp', left: '24vp', right: '24vp' })
104. }
105. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/ua4cTIsdQlqKJ6L-gZaMmA/zh-cn_image_0000002552959678.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=461B72EFB4BED4FEA971FB2F828636985852A7C1119E273F1D97850C09C2D0FC)

### 示例6（设置TabBar叠加在TabContent内容上）

本示例通过barOverlap实现了TabBar是否背后变模糊并叠加在TabContent之上。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct barHeightTest {
5. @State arr: number[] = [0, 1, 2, 3];
6. @State barOverlap: boolean = true;

8. build() {
9. Column() {
10. Text(`barOverlap ${this.barOverlap}`).fontSize(16)
11. Button('barOverlap变化').width('100%').margin({ bottom: '12vp' })
12. .onClick((event?: ClickEvent) => {
13. if (this.barOverlap) {
14. this.barOverlap = false;
15. } else {
16. this.barOverlap = true;
17. }
18. })

20. Tabs({ barPosition: BarPosition.End }) {
21. TabContent() {
22. Column() {
23. List({ space: 10 }) {
24. ForEach(this.arr, (item: number) => {
25. ListItem() {
26. Text('item' + item).width('80%').height(200).fontSize(16).textAlign(TextAlign.Center).backgroundColor('#fff8b81e')
27. }
28. }, (item: string) => item)
29. }.width('100%').height('100%')
30. .lanes(2).alignListItem(ListItemAlign.Center)
31. }.width('100%').height('100%')
32. .backgroundColor(Color.Pink)
33. }
34. .tabBar(new BottomTabBarStyle($r('sys.media.ohos_icon_mask_svg'), '测试0'))
35. }
36. .scrollable(false)
37. .height('60%')
38. .barOverlap(this.barOverlap)
39. }
40. .height(500)
41. .padding({ top: '24vp', left: '24vp', right: '24vp' })
42. }
43. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/uEFbGovBTHewmYSmkwENPA/zh-cn_image_0000002583479679.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=0E4946FFF2BF3FEFAF8F5DE0D20722536B0C5E2EA37D94500D3022DEBE0A66B9)

### 示例7（设置TabBar栅格化可见区域）

本示例通过barGridAlign实现了以栅格化方式设置TabBar的可见区域。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabsExample5 {
5. private controller: TabsController = new TabsController();
6. @State gridMargin: number = 10;
7. @State gridGutter: number = 10;
8. @State sm: number = -2;
9. @State clickedContent: string = '';

11. build() {
12. Column() {
13. Row() {
14. Button('gridMargin+10 ' + this.gridMargin)
15. .width('47%')
16. .height(50)
17. .margin({ top: 5 })
18. .onClick((event?: ClickEvent) => {
19. this.gridMargin += 10;
20. })
21. .margin({ right: '6%', bottom: '12vp' })
22. Button('gridMargin-10 ' + this.gridMargin)
23. .width('47%')
24. .height(50)
25. .margin({ top: 5 })
26. .onClick((event?: ClickEvent) => {
27. this.gridMargin -= 10;
28. })
29. .margin({ bottom: '12vp' })
30. }

32. Row() {
33. Button('gridGutter+10 ' + this.gridGutter)
34. .width('47%')
35. .height(50)
36. .margin({ top: 5 })
37. .onClick((event?: ClickEvent) => {
38. this.gridGutter += 10;
39. })
40. .margin({ right: '6%', bottom: '12vp' })
41. Button('gridGutter-10 ' + this.gridGutter)
42. .width('47%')
43. .height(50)
44. .margin({ top: 5 })
45. .onClick((event?: ClickEvent) => {
46. this.gridGutter -= 10;
47. })
48. .margin({ bottom: '12vp' })
49. }

51. Row() {
52. Button('sm+2 ' + this.sm)
53. .width('47%')
54. .height(50)
55. .margin({ top: 5 })
56. .onClick((event?: ClickEvent) => {
57. this.sm += 2;
58. })
59. .margin({ right: '6%' })
60. Button('sm-2 ' + this.sm).width('47%').height(50).margin({ top: 5 })
61. .onClick((event?: ClickEvent) => {
62. this.sm -= 2;
63. })
64. }

66. Text('点击内容:' + this.clickedContent).width('100%').height(200).margin({ top: 5 })

69. Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
70. TabContent() {
71. Column().width('100%').height('100%').backgroundColor(Color.Pink)
72. }.tabBar(BottomTabBarStyle.of($r('sys.media.ohos_app_icon'), '1'))

74. TabContent() {
75. Column().width('100%').height('100%').backgroundColor(Color.Green)
76. }.tabBar(BottomTabBarStyle.of($r('sys.media.ohos_app_icon'), '2'))

78. TabContent() {
79. Column().width('100%').height('100%').backgroundColor(Color.Blue)
80. }.tabBar(BottomTabBarStyle.of($r('sys.media.ohos_app_icon'), '3'))
81. }
82. .width('350vp')
83. .animationDuration(300)
84. .height('60%')
85. .barGridAlign({ sm: this.sm, margin: this.gridMargin, gutter: this.gridGutter })
86. .backgroundColor(0xf1f3f5)
87. .onTabBarClick((index: number) => {
88. this.clickedContent += 'now index ' + index + ' is clicked\n';
89. })
90. }
91. .width('100%')
92. .height(500)
93. .margin({ top: 5 })
94. .padding('10vp')
95. }
96. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/EjuygcPTRRmAB5FBlDt8BA/zh-cn_image_0000002552800030.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=EC4E73BEAC04177BC6A9AD6014A87099CDEC48FE743C561D1A3A5A3054350897)

### 示例8（自定义Tabs页面切换动画）

本示例通过customContentTransition实现了自定义Tabs页面的切换动画。

```
1. // xxx.ets
2. interface itemType {
3. text: string,
4. backgroundColor: Color
5. }

7. @Entry
8. @Component
9. struct TabsCustomAnimationExample {
10. @State data: itemType[] = [
11. {
12. text: 'Red',
13. backgroundColor: Color.Red
14. },
15. {
16. text: 'Yellow',
17. backgroundColor: Color.Yellow
18. },
19. {
20. text: 'Blue',
21. backgroundColor: Color.Blue
22. }];
23. @State opacityList: number[] = [];
24. @State scaleList: number[] = [];

26. private durationList: number[] = [];
27. private timeoutList: number[] = [];
28. private customContentTransition: (from: number, to: number) => TabContentAnimatedTransition = (from: number, to: number) => {
29. let tabContentAnimatedTransition = {
30. timeout: this.timeoutList[from],
31. transition: (proxy: TabContentTransitionProxy) => {
32. this.scaleList[from] = 1.0;
33. this.scaleList[to] = 0.5;
34. this.opacityList[from] = 1.0;
35. this.opacityList[to] = 0.5;
36. this.getUIContext()?.animateTo({
37. duration: this.durationList[from],
38. onFinish: () => {
39. proxy.finishTransition();
40. }
41. }, () => {
42. this.scaleList[from] = 0.5;
43. this.scaleList[to] = 1.0;
44. this.opacityList[from] = 0.5;
45. this.opacityList[to] = 1.0;
46. });
47. }
48. } as TabContentAnimatedTransition;
49. return tabContentAnimatedTransition;
50. };

52. aboutToAppear(): void {
53. let duration = 1000;
54. let timeout = 1000;
55. for (let i = 1; i <= this.data.length; i++) {
56. this.opacityList.push(1.0);
57. this.scaleList.push(1.0);
58. this.durationList.push(duration * i);
59. this.timeoutList.push(timeout * i);
60. }
61. }

63. build() {
64. Column() {
65. Tabs() {
66. ForEach(this.data, (item: itemType, index: number) => {
67. TabContent() {}
68. .tabBar(item.text)
69. .backgroundColor(item.backgroundColor)
70. // 自定义动画变化透明度、缩放页面等
71. .opacity(this.opacityList[index])
72. .scale({ x: this.scaleList[index], y: this.scaleList[index] })
73. })
74. }
75. .backgroundColor(0xf1f3f5)
76. .width('100%')
77. .height(500)
78. .customContentTransition(this.customContentTransition)
79. }
80. }
81. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/fj6JN9jJR6qgBvbsYqwmpg/zh-cn_image_0000002583439725.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=F258DD36E623A34AD601FEBEA0E64E232193951AC0159A0F0F2F556D4CA951B1)

### 示例9（页面切换拦截）

本示例通过onContentWillChange实现了自定义页面手势滑动切换拦截。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabsExample {
5. @State selectedIndex: number = 2;
6. @State currentIndex: number = 2;
7. private controller: TabsController = new TabsController();

9. @Builder tabBuilder(title: string,targetIndex: number) {
10. Column(){
11. // $r('app.media.star_fill')需要替换为开发者所需的图像资源文件
12. // $r('app.media.star')需要替换为开发者所需的图像资源文件
13. Image(this.selectedIndex === targetIndex ? $r('app.media.star_fill') : $r('app.media.star'))
14. .width(24)
15. .height(24)
16. .margin({ bottom: 4 })
17. .objectFit(ImageFit.Contain)
18. Text(title).fontColor(this.selectedIndex === targetIndex ? '#1698CE' : '#6B6B6B')
19. }.width('100%')
20. .height(50)
21. .justifyContent(FlexAlign.Center)
22. }

24. build() {
25. Column() {
26. Tabs({ barPosition: BarPosition.End, index: this.currentIndex, controller: this.controller }) {
27. TabContent() {
28. Column(){
29. Text('首页的内容')
30. }.width('100%').height('100%').backgroundColor('#00CB87').justifyContent(FlexAlign.Center)
31. }.tabBar(this.tabBuilder('首页',0))

33. TabContent() {
34. Column(){
35. Text('发现的内容')
36. }.width('100%').height('100%').backgroundColor('#007DFF').justifyContent(FlexAlign.Center)
37. }.tabBar(this.tabBuilder('发现',1))

39. TabContent() {
40. Column(){
41. Text('推荐的内容')
42. }.width('100%').height('100%').backgroundColor('#FFBF00').justifyContent(FlexAlign.Center)
43. }.tabBar(this.tabBuilder('推荐',2))

45. TabContent() {
46. Column(){
47. Text('我的内容')
48. }.width('100%').height('100%').backgroundColor('#E67C92').justifyContent(FlexAlign.Center)
49. }.tabBar(this.tabBuilder('我的',3))
50. }
51. .vertical(false)
52. .barMode(BarMode.Fixed)
53. .barWidth(360)
54. .barHeight(60)
55. .animationDuration(0)
56. .onChange((index: number) => {
57. this.currentIndex = index;
58. this.selectedIndex = index;
59. })
60. .width(360)
61. .height(600)
62. .backgroundColor('#F1F3F5')
63. .scrollable(true)
64. .onContentWillChange((currentIndex, comingIndex) => {
65. if (comingIndex == 2) {
66. return false;
67. }
68. return true;
69. })

71. Button('动态修改index').width('50%').margin({ top: 20 })
72. .onClick(()=>{
73. this.currentIndex = (this.currentIndex + 1) % 4;
74. })

76. Button('changeIndex').width('50%').margin({ top: 20 })
77. .onClick(()=>{
78. this.currentIndex = (this.currentIndex + 1) % 4;
79. this.controller.changeIndex(this.currentIndex);
80. })
81. }.width('100%')
82. }
83. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/d-65inncQvyBwiQdCNa-9w/zh-cn_image_0000002552959680.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=A92AD4A6D637657E830C96E690435C56E301C04E9A8DC63BC6C47BB20CA7247F)

### 示例10（自定义TabBar切换动画）

本示例通过onChange、onAnimationStart、onAnimationEnd、onGestureSwipe等接口实现了自定义TabBar的切换动画。

```
1. // EntryAbility.ets
2. import { Configuration, UIAbility } from '@kit.AbilityKit';
3. import { i18n } from '@kit.LocalizationKit';
4. import { CommonUtil } from '../common/CommonUtil';

6. export default class EntryAbility extends UIAbility {
7. onConfigurationUpdate(newConfig: Configuration): void {
8. // 监听系统配置变化
9. if (newConfig.language) {
10. CommonUtil.setIsRTL(i18n.isRTL(newConfig.language));
11. }
12. }
13. }
```

```
1. // CommonUtil.ets
2. export class CommonUtil {
3. private static isRTL: boolean = false;

5. public static setIsRTL(isRTL: boolean): void {
6. CommonUtil.isRTL = isRTL;
7. }

9. public static getIsRTL(): boolean {
10. return CommonUtil.isRTL;
11. }
12. }
```

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';
3. import { CommonUtil } from '../common/CommonUtil';

5. @Entry
6. @Component
7. struct TabsExample {
8. @State colorArray: [string, string][] =
9. [['green', '#00CB87'], ['blue', '#007DFF'], ['yellow', '#FFBF00'], ['pink', '#E67C92']];
10. @State currentIndex: number = 0;
11. @State animationDuration: number = 300;
12. @State indicatorLeftMargin: number = 0;
13. @State indicatorWidth: number = 0;
14. private tabsWidth: number = 0;
15. private textInfos: [number, number][] = [];
16. private isStartAnimateTo: boolean = false;

18. aboutToAppear():void {
19. for (let i = 0; i < this.colorArray.length; i++) {
20. this.textInfos.push([0, 0]);
21. }
22. }

24. @Builder
25. tabBuilder(index: number, name: string) {
26. Column() {
27. Text(name)
28. .fontSize(16)
29. .fontColor(this.currentIndex === index ? '#007DFF' : '#182431')
30. .fontWeight(this.currentIndex === index ? 500 : 400)
31. .id(index.toString())
32. .onAreaChange((oldValue: Area, newValue: Area) => {
33. this.textInfos[index] = [newValue.globalPosition.x as number, newValue.width as number];
34. if (!this.isStartAnimateTo && this.currentIndex === index && this.tabsWidth > 0) {
35. this.setIndicatorAttr(this.textInfos[this.currentIndex][0], this.textInfos[this.currentIndex][1]);
36. }
37. })
38. }.width('100%')
39. }

41. build() {
42. Stack({ alignContent: Alignment.TopStart }) {
43. Tabs({ barPosition: BarPosition.Start }) {
44. ForEach(this.colorArray, (item: [string, string], index:number) => {
45. TabContent() {
46. Column().width('100%').height('100%').backgroundColor(item[1])
47. }.tabBar(this.tabBuilder(index, item[0]))
48. })
49. }
50. .onAreaChange((oldValue: Area, newValue: Area)=> {
51. this.tabsWidth = newValue.width as number;
52. if (!this.isStartAnimateTo) {
53. this.setIndicatorAttr(this.textInfos[this.currentIndex][0], this.textInfos[this.currentIndex][1]);
54. }
55. })
56. .barWidth('100%')
57. .barHeight(56)
58. .width('100%')
59. .height(296)
60. .backgroundColor('#F1F3F5')
61. .animationDuration(this.animationDuration)
62. .onChange((index: number) => {
63. this.currentIndex = index; // 监听索引index的变化，实现页签内容的切换。
64. })
65. .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
66. // 切换动画开始时触发该回调。下划线跟着页面一起滑动，同时宽度渐变。
67. this.currentIndex = targetIndex;
68. this.startAnimateTo(this.animationDuration, this.textInfos[targetIndex][0], this.textInfos[targetIndex][1]);
69. })
70. .onAnimationEnd((index: number, event: TabsAnimationEvent) => {
71. // 切换动画结束时触发该回调。下划线动画停止。
72. let currentIndicatorInfo = this.getCurrentIndicatorInfo(index, event);
73. this.startAnimateTo(0, currentIndicatorInfo.left, currentIndicatorInfo.width);
74. })
75. .onGestureSwipe((index: number, event: TabsAnimationEvent) => {
76. // 在页面跟手滑动过程中，逐帧触发该回调。
77. let currentIndicatorInfo = this.getCurrentIndicatorInfo(index, event);
78. this.currentIndex = currentIndicatorInfo.index;
79. this.setIndicatorAttr(currentIndicatorInfo.left, currentIndicatorInfo.width);
80. })

82. Column()
83. .height(2)
84. .width(this.indicatorWidth)
85. .margin({ start: LengthMetrics.vp(this.indicatorLeftMargin), top: LengthMetrics.vp(48) })
86. .backgroundColor('#007DFF')
87. }.width('100%')
88. }

90. private getCurrentIndicatorInfo(index: number, event: TabsAnimationEvent): Record<string, number> {
91. let nextIndex = index;
92. if (index > 0 && (CommonUtil.getIsRTL() ? event.currentOffset < 0 : event.currentOffset > 0)) {
93. nextIndex--;
94. } else if (index < this.textInfos.length - 1 &&
95. (CommonUtil.getIsRTL() ? event.currentOffset > 0 : event.currentOffset < 0)) {
96. nextIndex++;
97. }
98. let indexInfo = this.textInfos[index];
99. let nextIndexInfo = this.textInfos[nextIndex];
100. let swipeRatio = Math.abs(event.currentOffset / this.tabsWidth);
101. let currentIndex = swipeRatio > 0.5 ? nextIndex : index; // 页面滑动超过一半，tabBar切换到下一页。
102. let currentLeft = indexInfo[0] + (nextIndexInfo[0] - indexInfo[0]) * swipeRatio;
103. let currentWidth = indexInfo[1] + (nextIndexInfo[1] - indexInfo[1]) * swipeRatio;
104. return { 'index': currentIndex, 'left': currentLeft, 'width': currentWidth };
105. }

107. private startAnimateTo(duration: number, leftMargin: number, width: number) {
108. this.isStartAnimateTo = true;
109. this.getUIContext()?.animateTo({
110. duration: duration, // 动画时长
111. curve: Curve.Linear, // 动画曲线
112. iterations: 1, // 播放次数
113. playMode: PlayMode.Normal, // 动画模式
114. onFinish: () => {
115. this.isStartAnimateTo = false;
116. console.info('play end');
117. }
118. }, () => {
119. this.setIndicatorAttr(leftMargin, width);
120. });
121. }

123. private setIndicatorAttr(leftMargin: number, width: number) {
124. this.indicatorWidth = width;
125. if (CommonUtil.getIsRTL()) {
126. this.indicatorLeftMargin = this.tabsWidth - leftMargin - width;
127. } else {
128. this.indicatorLeftMargin = leftMargin;
129. }
130. }
131. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/G002gfjLRnWfXvPZq-WlLg/zh-cn_image_0000002583479681.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=EEB97E9CCC75DA499807B8F1BE5CC14D216A05AA0485A8828C23495B7E6C94F9)

### 示例11（预加载子节点）

本示例通过preloadItems接口实现了预加载指定子节点。

```
1. // xxx.ets
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct TabsPreloadItems {
7. @State currentIndex: number = 1;
8. private tabsController: TabsController = new TabsController();

10. build() {
11. Column() {
12. Tabs({ index: this.currentIndex, controller: this.tabsController }) {
13. TabContent() {
14. MyComponent({ color: '#00CB87' })
15. }.tabBar(SubTabBarStyle.of('green'))

17. TabContent() {
18. MyComponent({ color: '#007DFF' })
19. }.tabBar(SubTabBarStyle.of('blue'))

21. TabContent() {
22. MyComponent({ color: '#FFBF00' })
23. }.tabBar(SubTabBarStyle.of('yellow'))

25. TabContent() {
26. MyComponent({ color: '#E67C92' })
27. }.tabBar(SubTabBarStyle.of('pink'))
28. }
29. .width(360)
30. .height(296)
31. .backgroundColor('#F1F3F5')
32. .onChange((index: number) => {
33. this.currentIndex = index;
34. })

36. Button('preload items: [0, 2, 3]')
37. .margin(5)
38. .onClick(() => {
39. // 预加载第0、2、3个子节点，提高滑动或点击切换至这些节点时的性能
40. this.tabsController.preloadItems([0, 2, 3])
41. .then(() => {
42. console.info('preloadItems success.');
43. })
44. .catch((error: BusinessError) => {
45. console.error('preloadItems failed, error code: ' + error.code + ', error message: ' + error.message);
46. })
47. })
48. }
49. }
50. }

52. @Component
53. struct MyComponent {
54. private color: string = '';

56. aboutToAppear(): void {
57. console.info('aboutToAppear backgroundColor:' + this.color);
58. }

60. aboutToDisappear(): void {
61. console.info('aboutToDisappear backgroundColor:' + this.color);
62. }

64. build() {
65. Column()
66. .width('100%')
67. .height('100%')
68. .backgroundColor(this.color)
69. }
70. }
```

### 示例12（设置TabBar平移距离和不透明度）

本示例通过setTabBarTranslate、setTabBarOpacity等接口设置了TabBar的平移距离和不透明度。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabsExample {
5. private controller: TabsController = new TabsController();

7. build() {
8. Column() {
9. Button('设置TabBar的平移距离').margin({ top: 20 })
10. .onClick(() => {
11. this.controller.setTabBarTranslate({ x: -20, y: -20 });
12. })

14. Button('设置TabBar的透明度').margin({ top: 20 })
15. .onClick(() => {
16. this.controller.setTabBarOpacity(0.5);
17. })

19. Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
20. TabContent() {
21. Column().width('100%').height('100%').backgroundColor('#00CB87')
22. }.tabBar(BottomTabBarStyle.of($r('app.media.startIcon'), 'green'))

24. TabContent() {
25. Column().width('100%').height('100%').backgroundColor('#007DFF')
26. }.tabBar(BottomTabBarStyle.of($r('app.media.startIcon'), 'blue'))

28. TabContent() {
29. Column().width('100%').height('100%').backgroundColor('#FFBF00')
30. }.tabBar(BottomTabBarStyle.of($r('app.media.startIcon'), 'yellow'))

32. TabContent() {
33. Column().width('100%').height('100%').backgroundColor('#E67C92')
34. }.tabBar(BottomTabBarStyle.of($r('app.media.startIcon'), 'pink'))
35. }
36. .width(360)
37. .height(296)
38. .margin({ top: 20 })
39. .barBackgroundColor('#F1F3F5')
40. }
41. .width('100%')
42. }
43. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/4w4Je-VZTtun7GmHj55ffg/zh-cn_image_0000002552800032.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=20CCDD23C28EE499B3D1F77FF07A2C6FBD435E7CCF22CD99714A547C1E1A4217)

### 示例13（页面懒加载和释放）

本示例通过使用自定义TabBar与Swiper配合LazyForEach实现页面懒加载和释放。

```
1. // xxx.ets
2. class MyDataSource implements IDataSource {
3. private list: number[] = [];

5. constructor(list: number[]) {
6. this.list = list;
7. }

9. totalCount(): number {
10. return this.list.length;
11. }

13. getData(index: number): number {
14. return this.list[index];
15. }

17. registerDataChangeListener(listener: DataChangeListener): void {
18. }

20. unregisterDataChangeListener() {
21. }
22. }

24. @Entry
25. @Component
26. struct TabsSwiperExample {
27. @State fontColor: string = '#182431';
28. @State selectedFontColor: string = '#007DFF';
29. @State currentIndex: number = 0;
30. private list: number[] = [];
31. private tabsController: TabsController = new TabsController();
32. private swiperController: SwiperController = new SwiperController();
33. private swiperData: MyDataSource = new MyDataSource([]);

35. aboutToAppear(): void {
36. for (let i = 0; i <= 9; i++) {
37. this.list.push(i);
38. }
39. this.swiperData = new MyDataSource(this.list);
40. }

42. @Builder tabBuilder(index: number, name: string) {
43. Column() {
44. Text(name)
45. .fontColor(this.currentIndex === index ? this.selectedFontColor : this.fontColor)
46. .fontSize(16)
47. .fontWeight(this.currentIndex === index ? 500 : 400)
48. .lineHeight(22)
49. .margin({ top: 17, bottom: 7 })
50. Divider()
51. .strokeWidth(2)
52. .color('#007DFF')
53. .opacity(this.currentIndex === index ? 1 : 0)
54. }.width('20%')
55. }

57. build() {
58. Column() {
59. Tabs({ barPosition: BarPosition.Start, controller: this.tabsController }) {
60. ForEach(this.list, (item: number) => {
61. TabContent().tabBar(this.tabBuilder(item, '页签 ' + this.list[item]))
62. })
63. }
64. .onTabBarClick((index: number) => {
65. this.currentIndex = index;
66. this.swiperController.changeIndex(index, true);
67. })
68. .barMode(BarMode.Scrollable)
69. .backgroundColor('#F1F3F5')
70. .height(56)
71. .width('100%')

73. Swiper(this.swiperController) {
74. LazyForEach(this.swiperData, (item: string) => {
75. Text(item.toString())
76. .onAppear(()=>{
77. console.info('onAppear ' + item.toString());
78. })
79. .onDisAppear(()=>{
80. console.info('onDisAppear ' + item.toString());
81. })
82. .width('100%')
83. .height('100%')
84. .backgroundColor(0xAFEEEE)
85. .textAlign(TextAlign.Center)
86. .fontSize(30)
87. }, (item: string) => item)
88. }
89. .loop(false)
90. .onChange((index: number) => {
91. this.currentIndex = index;
92. })
93. .onAnimationStart((index: number, targetIndex: number, extraInfo: SwiperAnimationEvent) => {
94. this.currentIndex = targetIndex;
95. this.tabsController.changeIndex(targetIndex);
96. })
97. }
98. }
99. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/a3DRe3w5TRmH4vr2_BNhEA/zh-cn_image_0000002583439727.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=7400555D130319B3595C400B53E1E3F1C83DD0964BDD12667818B26C0E83527D)

### 示例14（设置翻页动效）

本示例通过设置animationMode属性，实现了翻页的动效。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabsExample {
5. @State currentIndex: number = 0;
6. @State currentAnimationMode: AnimationMode = AnimationMode.CONTENT_FIRST;
7. private controller: TabsController = new TabsController();
8. private data: number[] = [];

10. aboutToAppear(): void {
11. for (let i = 0; i < 10; i++) {
12. this.data.push(i);
13. }
14. }

16. @Builder
17. tabBuilder(title: string,targetIndex: number) {
18. Column(){
19. Text(title).fontColor(this.currentIndex === targetIndex ? '#FF0000' : '#6B6B6B')
20. }.width('100%')
21. .height(50)
22. .justifyContent(FlexAlign.Center)
23. }

25. build() {
26. Column() {
27. Tabs({ barPosition: BarPosition.End, controller: this.controller, index: this.currentIndex }) {
28. ForEach(this.data, (item: string) => {
29. TabContent() {
30. Column(){
31. Text('' + item)
32. }.width('100%').height('100%').backgroundColor('#00CB87').justifyContent(FlexAlign.Center)
33. }.tabBar(this.tabBuilder('P' + item, parseInt(item)))
34. }, (item: string) => item)
35. }
36. .barWidth(360)
37. .barHeight(60)
38. .animationMode(this.currentAnimationMode)
39. .animationDuration(4000)
40. .onChange((index: number) => {
41. this.currentIndex = index;
42. })
43. .width(360)
44. .height(120)
45. .backgroundColor('#F1F3F5')

47. Text('AnimationMode:' + AnimationMode[this.currentAnimationMode])

49. Button('AnimationMode').width('50%').margin({ top: 1 }).height(25)
50. .onClick(()=>{
51. if (this.currentAnimationMode === AnimationMode.CONTENT_FIRST) {
52. this.currentAnimationMode = AnimationMode.ACTION_FIRST;
53. } else if (this.currentAnimationMode === AnimationMode.ACTION_FIRST) {
54. this.currentAnimationMode = AnimationMode.NO_ANIMATION;
55. } else if (this.currentAnimationMode === AnimationMode.NO_ANIMATION) {
56. this.currentAnimationMode = AnimationMode.CONTENT_FIRST_WITH_JUMP;
57. } else if (this.currentAnimationMode === AnimationMode.CONTENT_FIRST_WITH_JUMP) {
58. this.currentAnimationMode = AnimationMode.ACTION_FIRST_WITH_JUMP;
59. } else if (this.currentAnimationMode === AnimationMode.ACTION_FIRST_WITH_JUMP) {
60. this.currentAnimationMode = AnimationMode.CONTENT_FIRST;
61. }
62. })
63. }.width('100%')
64. }
65. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/chQN28J7RLi19GhJzjhdbQ/zh-cn_image_0000002552959682.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=28BDFFB7586B44079D0BD2BE282A05B5BACBEE9CE460DAA697876246728B0217)

### 示例15（页签超出TabBar区域显示）

该示例通过使用[TabsOptions](ts-container-tabs.md#tabsoptions15)中的barModifier设置tabBar的clip属性实现页签超出tabBar区域显示效果。

从API version 15开始，在TabsOptions中新增了barModifier接口。

```
1. // xxx.ets
2. import { CommonModifier } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct TabsBarModifierExample {
7. @State selectedIndex: number = 2;
8. @State currentIndex: number = 2;
9. @State isClip: boolean = false;
10. @State tabBarModifier: CommonModifier = new CommonModifier();
11. private controller: TabsController = new TabsController();

13. aboutToAppear(): void {
14. this.tabBarModifier.clip(this.isClip);
15. }

17. @Builder
18. tabBuilder(title: string, targetIndex: number) {
19. Column() {
20. Image($r('app.media.startIcon')).width(30).height(30)
21. Text(title).fontColor(this.selectedIndex === targetIndex ? '#1698CE' : '#6B6B6B')
22. }.width('100%')
23. .height(50)
24. .justifyContent(FlexAlign.Center)
25. .offset({ y: this.selectedIndex === targetIndex ? -15 : 0 })
26. }

28. build() {
29. Column() {
30. Tabs({
31. barPosition: BarPosition.End,
32. index: this.currentIndex,
33. controller: this.controller,
34. barModifier: this.tabBarModifier
35. }) {
36. TabContent() {
37. Column() {
38. Text('首页的内容')
39. }.width('100%').height('100%').backgroundColor('#00CB87').justifyContent(FlexAlign.Center)
40. }.tabBar(this.tabBuilder('首页', 0))

42. TabContent() {
43. Column() {
44. Text('发现的内容')
45. }.width('100%').height('100%').backgroundColor('#007DFF').justifyContent(FlexAlign.Center)
46. }.tabBar(this.tabBuilder('发现', 1))

48. TabContent() {
49. Column() {
50. Text('推荐的内容')
51. }.width('100%').height('100%').backgroundColor('#FFBF00').justifyContent(FlexAlign.Center)
52. }.tabBar(this.tabBuilder('推荐', 2))

54. TabContent() {
55. Column() {
56. Text('我的内容')
57. }.width('100%').height('100%').backgroundColor('#E67C92').justifyContent(FlexAlign.Center)
58. }.tabBar(this.tabBuilder('我的', 3))
59. }
60. .vertical(false)
61. .barMode(BarMode.Fixed)
62. .barWidth(340)
63. .barHeight(60)
64. .onChange((index: number) => {
65. this.currentIndex = index;
66. this.selectedIndex = index;
67. })
68. .width(340)
69. .height(400)
70. .backgroundColor('#F1F3F5')
71. .scrollable(true)

73. Button('isClip: ' + this.isClip)
74. .margin({ top: 30 })
75. .onClick(() => {
76. this.isClip = !this.isClip;
77. this.tabBarModifier.clip(this.isClip);
78. })
79. }.width('100%')
80. }
81. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/3WWep5yqTO2R33ooVU23eg/zh-cn_image_0000002583479683.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=F78ADFB7CD6574A3EEADB46D6EAFBB24182B41EA61F2BAF58FAA6F7AF519C357)

### 示例16（页签对齐布局）

本示例通过使用[TabsOptions](ts-container-tabs.md#tabsoptions15)中的barModifier设置tabBar的align属性实现页签对齐布局效果。

从API version 15开始，在TabsOptions中新增了barModifier接口。

```
1. // xxx.ets
2. import { CommonModifier } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct TabsBarModifierExample {
7. private controller: TabsController = new TabsController();
8. @State text: string = '文本';
9. @State isVertical: boolean = false;
10. @State tabBarModifier: CommonModifier = new CommonModifier();

12. build() {
13. Column() {
14. Row() {
15. Button('Alignment.Start ')
16. .width('47%')
17. .height(50)
18. .margin({ top: 5 })
19. .onClick((event?: ClickEvent) => {
20. this.tabBarModifier.align(Alignment.Start);
21. })
22. .margin({ right: '6%', bottom: '12vp' })
23. Button('Alignment.End')
24. .width('47%')
25. .height(50)
26. .margin({ top: 5 })
27. .onClick((event?: ClickEvent) => {
28. this.tabBarModifier.align(Alignment.End);
29. })
30. .margin({ bottom: '12vp' })
31. }

33. Row() {
34. Button('Alignment.Center')
35. .width('47%')
36. .height(50)
37. .margin({ top: 5 })
38. .onClick((event?: ClickEvent) => {
39. this.tabBarModifier.align(Alignment.Center);
40. })
41. .margin({ right: '6%', bottom: '12vp' })
42. Button('isVertical: ' + this.isVertical)
43. .width('47%')
44. .height(50)
45. .margin({ top: 5 })
46. .onClick((event?: ClickEvent) => {
47. this.isVertical = !this.isVertical;
48. })
49. .margin({ bottom: '12vp' })
50. }

52. Row() {
53. Button('Alignment.Top')
54. .width('47%')
55. .height(50)
56. .margin({ top: 5 })
57. .onClick((event?: ClickEvent) => {
58. this.tabBarModifier.align(Alignment.Top);
59. })
60. .margin({ right: '6%', bottom: '12vp' })
61. Button('Alignment.Bottom')
62. .width('47%')
63. .height(50)
64. .margin({ top: 5 })
65. .onClick((event?: ClickEvent) => {
66. this.tabBarModifier.align(Alignment.Bottom);
67. })
68. .margin({ bottom: '12vp' })
69. }

71. Tabs({ barPosition: BarPosition.End, controller: this.controller, barModifier: this.tabBarModifier }) {
72. TabContent() {
73. Column().width('100%').height('100%').backgroundColor(Color.Pink)
74. }.tabBar(SubTabBarStyle.of(this.text))

76. TabContent() {
77. Column().width('100%').height('100%').backgroundColor(Color.Green)
78. }.tabBar(SubTabBarStyle.of(this.text))

80. TabContent() {
81. Column().width('100%').height('100%').backgroundColor(Color.Blue)
82. }.tabBar(SubTabBarStyle.of(this.text))
83. }
84. .vertical(this.isVertical)
85. .height('60%')
86. .backgroundColor(0xf1f3f5)
87. .barMode(BarMode.Scrollable)
88. }
89. .width('100%')
90. .height(500)
91. .margin({ top: 5 })
92. .padding('24vp')
93. }
94. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/nwEFMtjSRIyd-8mkLssCvg/zh-cn_image_0000002552800034.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=805A71C7C0DAB8C32F5384EC9EA57AA337FAC606CABB10C662829F387D71C3C6)

### 示例17（Tabs与TabBar同步切换）

该示例通过[onSelected](ts-container-tabs.md#onselected18)接口，实现了Tabs与TabBar的同步切换。

从API version 18开始，新增了onSelected接口。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabsExample {
5. @State fontColor: string = '#182431';
6. @State selectedFontColor: string = '#007DFF';
7. @State currentIndex: number = 0;
8. @State selectedIndex: number = 0;
9. private controller: TabsController = new TabsController();

11. @Builder tabBuilder(index: number, name: string) {
12. Column() {
13. Text(name)
14. .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
15. .fontSize(16)
16. .fontWeight(this.selectedIndex === index ? 500 : 400)
17. .lineHeight(22)
18. .margin({ top: 17, bottom: 7 })
19. Divider()
20. .strokeWidth(2)
21. .color('#007DFF')
22. .opacity(this.selectedIndex === index ? 1 : 0)
23. }.width('100%')
24. }

26. build() {
27. Column() {
28. Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
29. TabContent() {
30. Column().width('100%').height('100%').backgroundColor('#00CB87')
31. }.tabBar(this.tabBuilder(0, 'green'))

33. TabContent() {
34. Column().width('100%').height('100%').backgroundColor('#007DFF')
35. }.tabBar(this.tabBuilder(1, 'blue'))

37. TabContent() {
38. Column().width('100%').height('100%').backgroundColor('#FFBF00')
39. }.tabBar(this.tabBuilder(2, 'yellow'))

41. TabContent() {
42. Column().width('100%').height('100%').backgroundColor('#E67C92')
43. }.tabBar(this.tabBuilder(3, 'pink'))
44. }
45. .vertical(false)
46. .barMode(BarMode.Fixed)
47. .barWidth(360)
48. .barHeight(56)
49. .animationDuration(400)
50. .animationMode(AnimationMode.CONTENT_FIRST)
51. .onChange((index: number) => {
52. console.info('onChange index:' + index);
53. this.currentIndex = index;
54. })
55. .onSelected((index: number) => {
56. console.info('onSelected index:' + index);
57. this.selectedIndex = index;
58. })
59. .onUnselected((index: number) => {
60. console.info('onUnselected index:' + index);
61. })
62. .width('100%')
63. .height('100%')
64. .backgroundColor('#F1F3F5')
65. }.width('100%')
66. }
67. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/I3SYkj-JR4WLihZKLODu3g/zh-cn_image_0000002583439729.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=FE7ABFB51CD76A7F454AD1A22D332FD662907D1DF55571258423FED243BC0387)

### 示例18（释放Tabs子组件）

该示例通过设置[cachedMaxCount](ts-container-tabs.md#cachedmaxcount19)属性，实现了Tabs子组件的释放。

从API version 19开始，新增了cachedMaxCount接口。

```
1. @Entry
2. @Component
3. struct TabsExample {
4. build() {
5. Tabs() {
6. TabContent() {
7. MyComponent({ color: '#00CB87' })
8. }.tabBar(SubTabBarStyle.of('green'))

10. TabContent() {
11. MyComponent({ color: '#007DFF' })
12. }.tabBar(SubTabBarStyle.of('blue'))

14. TabContent() {
15. MyComponent({ color: '#FFBF00' })
16. }.tabBar(SubTabBarStyle.of('yellow'))

18. TabContent() {
19. MyComponent({ color: '#E67C92' })
20. }.tabBar(SubTabBarStyle.of('pink'))
21. }
22. .width(360)
23. .height(296)
24. .backgroundColor('#F1F3F5')
25. .cachedMaxCount(1, TabsCacheMode.CACHE_BOTH_SIDE)
26. }
27. }

29. @Component
30. struct MyComponent {
31. private color: string = '';

33. aboutToAppear(): void {
34. console.info('aboutToAppear backgroundColor:' + this.color);
35. }

37. aboutToDisappear(): void {
38. console.info('aboutToDisappear backgroundColor:' + this.color);
39. }

41. build() {
42. Column()
43. .width('100%')
44. .height('100%')
45. .backgroundColor(this.color)
46. }
47. }
```

### 示例19（设置TabBar背景模糊效果）

该示例分别通过[barBackgroundBlurStyle](ts-container-tabs.md#barbackgroundblurstyle18)和[barBackgroundEffect](ts-container-tabs.md#barbackgroundeffect18)设置TabsBar页签栏的背景模糊样式和效果。

从API version 18开始，新增了barBackgroundBlurStyle和barBackgroundEffect接口。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabsExample {
5. build() {
6. Column() {
7. // barBackgroundBlurStyle 可以通过枚举值的方式设置模糊参数
8. Stack() {
9. Image($r('app.media.startIcon'))
10. Tabs() {
11. TabContent() {
12. Column().width('100%').height('100%').backgroundColor('#00CB87')
13. }.tabBar('green')

15. TabContent() {
16. Column().width('100%').height('100%').backgroundColor('#007DFF')
17. }.tabBar('blue')

19. TabContent() {
20. Column().width('100%').height('100%').backgroundColor('#FFBF00')
21. }.tabBar('yellow')

23. TabContent() {
24. Column().width('100%').height('100%').backgroundColor('#E67C92')
25. }.tabBar('pink')
26. }
27. .barBackgroundBlurStyle(BlurStyle.COMPONENT_THICK,
28. { colorMode: ThemeColorMode.LIGHT, adaptiveColor: AdaptiveColor.DEFAULT, scale: 1.0 })
29. }
30. .width(300)
31. .height(300)
32. .margin(10)

34. // barBackgroundEffect 可以自定义设置tabBar页签栏的模糊半径、亮度、饱和度等参数
35. Stack() {
36. Image($r('app.media.startIcon'))
37. Tabs() {
38. TabContent() {
39. Column().width('100%').height('100%').backgroundColor('#00CB87')
40. }.tabBar('green')

42. TabContent() {
43. Column().width('100%').height('100%').backgroundColor('#007DFF')
44. }.tabBar('blue')

46. TabContent() {
47. Column().width('100%').height('100%').backgroundColor('#FFBF00')
48. }.tabBar('yellow')

50. TabContent() {
51. Column().width('100%').height('100%').backgroundColor('#E67C92')
52. }.tabBar('pink')
53. }
54. .barBackgroundEffect({ radius: 20, brightness: 0.6, saturation: 15 })
55. }
56. .width(300)
57. .height(300)
58. .margin(10)
59. }
60. }
61. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/9LG2Rh5wSQmVWzR5fqGGXA/zh-cn_image_0000002552959684.png?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=B48C968D35DA56B5A023061BE8623788D8BBD00794B73491D3E82F596E8A6DEF)

### 示例20（设置边缘滑动效果）

该示例通过[edgeEffect](ts-container-tabs.md#edgeeffect12)实现了不同的边缘回弹效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabsExample {
5. @State edgeEffect: EdgeEffect = EdgeEffect.Spring;

7. build() {
8. Column() {
9. Tabs() {
10. TabContent() {
11. Column().width('100%').height('100%').backgroundColor('#00CB87')
12. }.tabBar('green')

14. TabContent() {
15. Column().width('100%').height('100%').backgroundColor('#007DFF')
16. }.tabBar('blue')

18. TabContent() {
19. Column().width('100%').height('100%').backgroundColor('#FFBF00')
20. }.tabBar('yellow')

22. TabContent() {
23. Column().width('100%').height('100%').backgroundColor('#E67C92')
24. }.tabBar('pink')
25. }
26. .width(360)
27. .height(296)
28. .margin({ top: 52 })
29. .backgroundColor('#F1F3F5')
30. .edgeEffect(this.edgeEffect)

32. Button('EdgeEffect.Spring').width('50%').margin({ top: 20 })
33. .onClick(() => {
34. this.edgeEffect = EdgeEffect.Spring;
35. })

37. Button('EdgeEffect.Fade').width('50%').margin({ top: 20 })
38. .onClick(() => {
39. this.edgeEffect = EdgeEffect.Fade;
40. })

42. Button('EdgeEffect.None').width('50%').margin({ top: 20 })
43. .onClick(() => {
44. this.edgeEffect = EdgeEffect.None;
45. })
46. }.width('100%')
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/SJzR8wY6TW2UrZla0IQBFg/zh-cn_image_0000002583479685.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=4E5D89650D83488E231C1F8A520FDAE7AB9C514F0D2F5F08B0F102EC2C3F00DB)

### 示例21（Tabs设置翻页动画曲线）

该示例展示了如何通过[animationCurve](ts-container-tabs.md#animationcurve20)接口设置Tabs翻页动画曲线，并结合animationDuration设置翻页动画的时长。

从API version 20开始，新增了animationCurve接口。

```
1. import { curves } from '@kit.ArkUI';

3. interface TabsItemType {
4. text: string,
5. backgroundColor: ResourceColor
6. }

8. @Entry
9. @Component
10. struct TabsExample {
11. private tabsController: TabsController = new TabsController();
12. private curves: (Curve | ICurve) [] = [
13. curves.interpolatingSpring(-1, 1, 328, 34),
14. curves.springCurve(10, 1, 228, 30),
15. curves.cubicBezierCurve(0.25, 0.1, 0.25, 1.0),
16. ];
17. private curveNames: string[] = [
18. 'interpolatingSpring(-1, 1, 328, 34)',
19. 'springCurve(10, 1, 228, 30)',
20. 'cubicBezierCurve(0.25, 0.1, 0.25, 1.0)'
21. ];
22. @State curveIndex: number = 0;
23. private data: TabsItemType[] = [
24. { text: '1', backgroundColor: '#004AAF' },
25. { text: '2', backgroundColor: '#2787D9' },
26. { text: '3', backgroundColor: '#D5D5D5' },
27. { text: '4', backgroundColor: '#707070' },
28. { text: '5', backgroundColor: '#F7F7F7' },
29. ];
30. @State duration: number = 0;

32. build() {
33. Column({ space: 2 }) {
34. Tabs({ controller: this.tabsController }) {
35. ForEach(this.data, (item: TabsItemType, index: number) => {
36. TabContent() {
37. }
38. .tabBar(item.text)
39. .backgroundColor(item.backgroundColor)
40. })
41. }
42. .backgroundColor(0xf1f3f5)
43. .width('100%')
44. .height(500)
45. .animationCurve(this.curves[this.curveIndex])
46. .animationDuration(this.duration)

48. Column({ space: 2 }) {
49. Text('Curve:' + this.curveNames[this.curveIndex])
50. Row({ space: 2 }) {
51. // 切换动效曲线
52. Button('++').onClick(() => {
53. this.curveIndex = (this.curveIndex + 1) % this.curves.length;
54. })
55. Button('reset').onClick(() => {
56. this.curveIndex = 0;
57. })
58. }
59. }
60. .margin({ left: '10vp' })
61. .width('100%')

63. Row({ space: 2 }) {
64. Text('Duration:' + this.duration)
65. // 增加动效时长
66. Button('+100').onClick(() => {
67. this.duration = (this.duration + 100) % 10000;
68. })
69. Button('+1000').onClick(() => {
70. this.duration = (this.duration + 1000) % 10000;
71. })
72. Button('reset').onClick(() => {
73. this.duration = 0;
74. })
75. }
76. .margin({ left: '10vp' })
77. .width('100%')
78. }
79. .margin('10vp')
80. }
81. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/C4qefOYoR3mM4rDyW0vd-Q/zh-cn_image_0000002552800036.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=5A83DFA83FBE2A34864CFD14BAEED9BE6B7D118DAE007D42FF682EF0266B956D)

### 示例22（监听Tabs页面滑动事件）

该示例展示了如何通过[onContentDidScroll](ts-container-tabs.md#oncontentdidscroll23)接口设置Tabs滑动时的回调。

从API version 23开始，新增onContentDidScroll接口。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabsDidScrollExample {
5. @State fontColor: string = '#182431';
6. @State selectedFontColor: string = '#007DFF';
7. @State currentIndex: number = 0;
8. @State selectedIndex: number = 0;
9. @State didScrollStr: string = '';
10. private controller: TabsController = new TabsController();

12. @Builder
13. tabBuilder(index: number, name: string) {
14. Column() {
15. Text(name)
16. .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
17. .fontSize(16)
18. .fontWeight(this.selectedIndex === index ? 500 : 400)
19. .lineHeight(22)
20. .margin({ top: 17, bottom: 7 })
21. Divider()
22. .strokeWidth(2)
23. .color('#007DFF')
24. .opacity(this.selectedIndex === index ? 1 : 0)
25. }.width('100%')
26. }

28. build() {
29. Column() {
30. Text('滑动页面触发回调')
31. .width("80%")
32. .fontSize(20)
33. .margin(5)
34. .textAlign(TextAlign.Center)

36. Text(this.didScrollStr)
37. .width("80%")
38. .fontSize(20)
39. .margin(5)
40. .textAlign(TextAlign.Center)

42. Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
43. TabContent() {
44. Column().width('100%').height('100%').backgroundColor('#00CB87')
45. }.tabBar(this.tabBuilder(0, 'green'))

47. TabContent() {
48. Column().width('100%').height('100%').backgroundColor('#007DFF')
49. }.tabBar(this.tabBuilder(1, 'blue'))

51. TabContent() {
52. Column().width('100%').height('100%').backgroundColor('#FFBF00')
53. }.tabBar(this.tabBuilder(2, 'yellow'))

55. TabContent() {
56. Column().width('100%').height('100%').backgroundColor('#E67C92')
57. }.tabBar(this.tabBuilder(3, 'pink'))
58. }
59. .vertical(false)
60. .barMode(BarMode.Fixed)
61. .barWidth(360)
62. .barHeight(56)
63. .animationDuration(400)
64. .onChange((index: number) => {
65. // currentIndex控制TabContent显示页签
66. this.currentIndex = index;
67. this.selectedIndex = index;
68. })
69. .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
70. if (index === targetIndex) {
71. return;
72. }
73. // selectedIndex控制自定义TabBar内Image和Text颜色切换
74. this.selectedIndex = targetIndex;
75. })
76. .width(360)
77. .height(296)
78. .margin({ top: 15 })
79. .backgroundColor('#F1F3F5')
80. .onContentDidScroll((selectedIndex: number, index: number, position: number, mainAxisLength: number) => {
81. // 监听Tabs页面滑动事件，在该回调中可以实现自定义导航点切换动画等
82. console.info("onContentDidScroll selectedIndex: " + selectedIndex + ", index: " + index + ", position: " +
83. position + ", mainAxisLength: " + mainAxisLength);
84. this.didScrollStr =
85. "onContentDidScroll selectedIndex: " + selectedIndex + ", index: " + index + ", position: " +
86. position + ", mainAxisLength: " + mainAxisLength
87. })
88. }.width('100%')
89. }
90. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/bSK5jFpHTA-cA9iB83imGg/zh-cn_image_0000002583439731.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=7738BEC52C8B871D7F7C30E45CCABEA59A19D6D9729B3EC3325D7D04E753CAB6)
