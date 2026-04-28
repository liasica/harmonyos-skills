---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist
title: ArcList
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 滚动与滑动 > ArcList
category: harmonyos-references
scraped_at: 2026-04-28T08:01:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8666b6082279285e6386e23f9f3614203fdce6b406b84ce7c78c9ac01fd74bf9
---

弧形列表包含一系列列表项。适合连续、多行呈现同类数据，例如图片和文本。

说明

* 该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件支持在Phone、PC/2in1、Tablet、TV、Wearable设备上使用。API version 22及以前版本，在Phone、PC/2in1、Tablet、TV上使用会编译告警，但可以正常运行。

## 导入模块

PhonePC/2in1TabletTVWearable

说明

* ArcListAttribute是用于配置ArcList组件属性的关键接口。API version 21及之前版本，导入ArcList组件后需要开发者手动导入ArcListAttribute，否则会编译报错。从API version 22开始，编译工具链识别到导入ArcList组件后，会自动导入ArcListAttribute，无需开发者手动导入ArcListAttribute。
* 如果开发者手动导入ArcListAttribute，DevEco Studio会显示置灰，API version 21及之前版本删除会编译报错，从API version 22开始，删除对功能无影响。

API version 21及之前版本：

```
1. import { ArcList, ArcListAttribute } from '@kit.ArkUI';
```

API version 22及之后版本：

```
1. import { ArcList } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

仅支持[ArcListItem](ts-container-arclistitem.md)子组件。

说明

ArcList的子组件索引值计算规则：

* 按子组件的顺序依次递增。
* [if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)语句中，只有条件成立的分支内的子组件会参与索引值计算，条件不成立的分支内子组件不计算索引值。
* [ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)/[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)语句中，会计算展开所有子节点索引值。
* [if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)、[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)和[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)发生变化以后，会更新子节点索引值。
* ArcList子组件[visibility](ts-universal-attributes-visibility.md#visibility)属性设置为Hidden或None依然会计算索引值。

## 接口

PhonePC/2in1TabletTVWearable

ArcList(options?: ArkListOptions)

创建弧形列表实例，传入弧形列表配置项参数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ArkListOptions](ts-container-arclist.md#arklistoptions) | 否 | 为ArcList提供可选参数。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### digitalCrownSensitivity

PhonePC/2in1TabletTVWearable

digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>)

设置表冠响应事件灵敏度。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sensitivity | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[CrownSensitivity](ts-appendix-enums.md#crownsensitivity18)> | 是 | 表冠响应灵敏度。  默认值：CrownSensitivity.MEDIUM，响应速度适中。 |

### space

PhonePC/2in1TabletTVWearable

space(space: Optional<LengthMetrics>)

设置列表子项之间的距离。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| space | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)> | 是 | 列表子项之间的间距。  默认值：LengthMetrics.vp(0)  ArcList子组件的[visibility](ts-universal-attributes-visibility.md#visibility)属性设置为None时不显示，但该子组件上下的space还会生效。 |

### scrollBar

PhonePC/2in1TabletTVWearable

scrollBar(status: Optional<BarState>)

设置滚动条状态。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| status | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[BarState](ts-appendix-enums.md#barstate)> | 是 | 滚动条状态。  默认值：BarState.Auto |

### cachedCount

PhonePC/2in1TabletTVWearable

cachedCount(count: Optional<number>)

设置列表中ArcListItem的预加载数量，懒加载场景只会预加载ArcList显示区域外上下各cachedCount行的ArcListItem，非懒加载场景会全部加载。懒加载、非懒加载都只布局ArcList显示区域+ArcList显示区域外上下各cachedCount行的ArcListItem。

ArcList设置cachedCount后，显示区域外上下各会预加载并布局cachedCount行ArcListItem。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | ArcListItem的预加载数量。  默认值：根据屏幕内显示的节点个数设置，最大值为16。  取值范围：[0, +∞) |

### chainAnimation

PhonePC/2in1TabletTVWearable

chainAnimation(enable: Optional<boolean>)

设置当前ArcList是否启用链式联动动效，开启后列表滑动以及顶部和底部拖拽时会有链式联动的效果。

链式联动效果：ArcList内的ArcListItem间隔一定距离，在基本的滑动交互行为下，主动对象驱动从动对象进行联动，驱动效果遵循弹簧物理动效。

链式动效生效需要满足前提条件：ArcList边缘效果为[EdgeEffect.Spring](ts-appendix-enums.md#edgeeffect)类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否启用链式联动动效。  默认值：false，不启用链式联动。true，启用链式联动。 |

### enableScrollInteraction

PhonePC/2in1TabletTVWearable

enableScrollInteraction(enable: Optional<boolean>)

设置是否支持滚动手势。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否支持滚动手势。设置为true时可以通过手指或者鼠标滚动，设置为false时无法通过手指或者鼠标滚动，但不影响控制器[Scroller](ts-container-scroll.md#scroller)的滚动接口。  默认值：true |

### fadingEdge

PhonePC/2in1TabletTVWearable

fadingEdge(enable: Optional<boolean>)

设置是否开启边缘渐隐效果。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | fadingEdge生效时，会覆盖原组件的.overlay()属性。  fadingEdge生效时，建议不在该组件上设置background相关属性，会影响渐隐的显示效果。  fadingEdge生效时，组件会裁剪到边界，设置组件的[clip](ts-universal-attributes-sharp-clipping.md#clip12)属性为false不生效。  设置为true时开启边缘渐隐效果，设置为false时不开启边缘渐隐效果。  默认值：false |

### friction

PhonePC/2in1TabletTVWearable

friction(friction: Optional<number>)

设置摩擦系数，手动划动滚动区域时生效，仅影响惯性滚动过程。设置为小于等于0的值时，按默认值处理。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| friction | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 摩擦系数。  默认值：0.8  取值范围：(0, +∞) |

### scrollBarWidth

PhonePC/2in1TabletTVWearable

scrollBarWidth(width: Optional<LengthMetrics>)

设置滚动条的宽度。宽度设置后，滚动条按压状态宽度为设置的宽度值。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)> | 是 | 滚动条的宽度。  默认值：LengthMetrics.vp(24)  最小值：LengthMetrics.vp(4)  单位：vp |

### scrollBarColor

PhonePC/2in1TabletTVWearable

scrollBarColor(color: Optional<ColorMetrics>)

设置滚动条的颜色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ColorMetrics](js-apis-arkui-graphics.md#colormetrics12)> | 是 | 设置滚动条颜色。  默认值：ColorMetrics.numeric(0xA9FFFFFF) |

### flingSpeedLimit

PhonePC/2in1TabletTVWearable

flingSpeedLimit(speed: Optional<number>)

限制跟手滑动结束后，惯性滚动动效开始时的最大初始速度。设置为小于等于0的值时，按默认值处理。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speed | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 惯性滚动动效开始时的最大初始速度。  默认值：9000  单位：vp/s  取值范围：(0, +∞) |

### childrenMainSize

PhonePC/2in1TabletTVWearable

childrenMainSize(size: Optional<ChildrenMainSize>)

设置ArcList组件的子组件在主轴方向的大小信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ChildrenMainSize](ts-container-scrollable-common.md#childrenmainsize12对象说明)> | 是 | 通过[ChildrenMainSize](ts-container-scrollable-common.md#childrenmainsize12对象说明)对象向ArcList组件精确提供所有子组件在主轴方向的大小信息，能够确保ArcList组件在子组件主轴尺寸不统一、子组件的增删变动、以及使用[scrollToIndex](ts-container-scroll.md#scrolltoindex)等场景时，仍能保持其滑动位置的准确性。进而保证了[scrollTo](ts-container-scroll.md#scrollto)能够精准跳转至指定位置，[currentOffset](ts-container-scroll.md#currentoffset)或[offset](ts-container-scroll.md#offset23)准确反映当前的滑动位置，且内置滚动条能够实现平滑移动，避免任何跳跃或突变，从API version 23开始，新增offset接口。  **说明：**  提供的主轴方向大小必须与子组件实际在主轴方向的大小一致，子组件在主轴方向大小发生变化或进行增删操作时，必须通过调用ChildrenMainSize对象的方法来及时通知ArcList组件。 |

## 事件

PhonePC/2in1TabletTVWearable

### onScrollIndex

PhonePC/2in1TabletTVWearable

onScrollIndex(handler: Optional<ArcScrollIndexHandler>)

当子组件划入或划出ArcList的显示区域时，将触发此事件。在ArcList初始化时，此事件会被触发一次。当ArcList显示区域内的首个或末个子组件的索引值发生变化，或是显示区域中心的子组件发生变动时，同样会触发此事件。

ArcList的边缘效果为弹簧效果时，在ArcList划动到边缘继续划动和松手回弹过程不会触发onScrollIndex事件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ArcScrollIndexHandler](ts-container-arclist.md#arcscrollindexhandler)> | 是 | 有子组件划入或划出ArcList显示区域时触发该回调。 |

### onReachStart

PhonePC/2in1TabletTVWearable

onReachStart(handler: Optional<VoidCallback>)

列表到达起始位置时触发。

当ArcList进行初始化时，若[initialIndex](ts-container-arclist.md#arklistoptions)设定为0，将触发一次事件。当ArcList滚动至起始位置，亦会触发一次事件。在ArcList的边缘效果设置为弹簧效果时，滑动经过起始位置时会触发一次事件，而在回弹返回起始位置时，将再次触发一次事件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[VoidCallback](ts-types.md#voidcallback12)> | 是 | 列表到达起始位置时触发。 |

### onReachEnd

PhonePC/2in1TabletTVWearable

onReachEnd(handler: Optional<VoidCallback>)

列表到达末尾位置时触发。

ArcList边缘效果为弹簧效果时，划动经过末尾位置时触发一次该事件，回弹回末尾位置时再触发一次该事件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[VoidCallback](ts-types.md#voidcallback12)> | 是 | 列表到达末尾位置时触发。 |

### onScrollStart

PhonePC/2in1TabletTVWearable

onScrollStart(handler: Optional<VoidCallback>)

列表滑动开始时触发。手指拖动列表或列表的滚动条触发的滑动开始时，会触发该事件。使用[Scroller](ts-container-scroll.md#scroller)滑动控制器触发的带动画的滑动，动画开始时会触发该事件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[VoidCallback](ts-types.md#voidcallback12)> | 是 | 列表滑动开始时触发。 |

### onScrollStop

PhonePC/2in1TabletTVWearable

onScrollStop(handler: Optional<VoidCallback>)

列表滑动停止时触发。手指拖动列表或列表的滚动条触发的滑动，手指离开屏幕后滑动停止时会触发该事件。使用[Scroller](ts-container-scroll.md#scroller)滑动控制器触发的带动画的滑动，动画停止会触发该事件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[VoidCallback](ts-types.md#voidcallback12)> | 是 | 列表滑动停止时触发。 |

### onWillScroll

PhonePC/2in1TabletTVWearable

onWillScroll(handler: Optional<OnWillScrollCallback>)

列表滑动时每帧开始前触发，返回当前帧将要滑动的偏移量和当前滑动状态。返回的偏移量为计算得到的将要滑动的偏移量值，并非最终实际滑动偏移。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[OnWillScrollCallback](ts-container-scrollable-common.md#onwillscrollcallback12)> | 是 | 列表滑动时每帧开始前触发的回调。 |

说明

调用[scrollEdge](ts-container-scroll.md#scrolledge)和不带动画的[scrollToIndex](ts-container-scroll.md#scrolltoindex)时，不触发onWillScroll。

### onDidScroll

PhonePC/2in1TabletTVWearable

onDidScroll(handler: Optional<OnScrollCallback>)

列表滑动时触发，返回当前帧滑动的偏移量和当前滑动状态。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[OnScrollCallback](ts-container-scrollable-common.md#onscrollcallback12)> | 是 | 列表滑动时触发的回调。 |

## ArkListOptions

PhonePC/2in1TabletTVWearable

包含创建ArcList组件的基础参数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| initialIndex | number | 否 | 是 | 设置当前ArcList初次加载时视窗起始位置显示的item的索引值。  默认值：0  **说明：**  设置为负数或超过了当前ArcList最后一个item的索引值时视为无效取值，无效取值按默认值显示。 |
| scroller | [Scroller](ts-container-scroll.md#scroller) | 否 | 是 | 可滚动组件的控制器。与ArcList绑定后，可以通过它控制ArcList的滚动。  **说明：**  不允许和其他滚动类组件，如：[ArcList](ts-container-arclist.md)、[List](ts-container-list.md)、[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)和[WaterFlow](ts-container-waterflow.md)绑定同一个滚动控制对象。 |
| header | [ComponentContent](js-apis-arkui-componentcontent.md) | 否 | 是 | 支持标题设置。 |

## ArcScrollIndexHandler

PhonePC/2in1TabletTVWearable

type ArcScrollIndexHandler = (start: number, end: number, center: number) => void

有子组件划入或划出ArcList显示区域时触发的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | ArcList显示区域内第一个子组件的索引值。 |
| end | number | 是 | ArcList显示区域内最后一个子组件的索引值。 |
| center | number | 是 | ArcList显示区域内中间位置子组件的索引值。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例增加了ArcList支持标题栏设置的效果，子项自动缩放显示。

```
1. // xxx.ets
2. import { ComponentContent, LengthMetrics } from '@kit.ArkUI';
3. import { UIContext, CircleShape } from '@kit.ArkUI';
4. // 从API version 22开始，无需手动导入ArcListAttribute和ArcListItemAttribute。具体请参考ArcList、ArcListItem的导入模块说明。
5. import { ArcList, ArcListItem, ArcListAttribute, ArcListItemAttribute } from '@kit.ArkUI';

7. @Builder
8. function buildText() {
9. Column() {
10. Text('header')
11. .fontSize('60px')
12. .fontWeight(FontWeight.Bold)
13. .fontColor(Color.Black)
14. }.margin(0)
15. }

17. @Entry
18. @Component
19. struct Index {
20. @State  private numItems: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

22. private watchSize: string = '466px'; // Wearable默认宽高：466*466
23. private listSize: string = '414px'; // item宽度

25. context: UIContext = this.getUIContext();
26. tabBar1: ComponentContent<Object> = new ComponentContent(this.context, wrapBuilder(buildText));

28. @Builder
29. buildList2() {
30. Stack() {
31. Column() {
32. }
33. .justifyContent(FlexAlign.Center)
34. .width(this.watchSize)
35. .height(this.watchSize)
36. .clipShape(new CircleShape({ width: '100%', height: '100%' }))
37. .backgroundColor(Color.White)

39. ArcList({ initialIndex: 0, header: this.tabBar1 }) {
40. ForEach(this.numItems, (item: number, index: number) => {
41. ArcListItem() {
42. Button('' + item, { type: ButtonType.Capsule })
43. .width(this.listSize)
44. .height('100px')
45. .fontSize('40px')
46. .focusable(true)
47. .focusOnTouch(true)
48. .backgroundColor(0x17A98D)
49. }.align(Alignment.Center)
50. }, (item: number, index: number) => (item + index).toString())
51. }
52. .space(LengthMetrics.px(10))
53. .borderRadius(this.watchSize)
54. .focusable(true)
55. .focusOnTouch(true)
56. .defaultFocus(true)
57. }
58. .align(Alignment.Center)
59. .width(this.watchSize)
60. .height(this.watchSize)
61. .border({color: Color.Black, width: 1})
62. .borderRadius(this.watchSize)
63. }

65. build() {
66. Column() {
67. this.buildList2()
68. }
69. .width('100%')
70. .height('100%')
71. .alignItems(HorizontalAlign.Center)
72. .justifyContent(FlexAlign.Center)
73. }
74. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/CYfnRfWeRPuirLglav3nhw/zh-cn_image_0000002583479619.png?HW-CC-KV=V1&HW-CC-Date=20260428T000127Z&HW-CC-Expire=86400&HW-CC-Sign=CEFBAD40FC1B877BDFB3C9A94CEEAFF434A5A2E3759D3E69538AE96D00B39D91)
