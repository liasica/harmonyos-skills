---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-scrollbar
title: ScrollBar
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 滚动与滑动 > ScrollBar
category: harmonyos-references
scraped_at: 2026-04-29T13:51:49+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:f3372fcad7f420eb2cb6a15dc56822d62e17bbe5fe62213ccbc95078ed7f283e
---

滚动条组件ScrollBar，用于配合可滚动组件使用，如[ArcList](ts-container-arclist.md)、[List](ts-container-list.md)、[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)、[WaterFlow](ts-container-waterflow.md)。

说明

* 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* ScrollBar主轴方向不设置大小时，采用父组件[布局约束](js-apis-arkui-framenode.md#layoutconstraint12)中的maxSize作为主轴方向大小。如果ScrollBar的父组件存在可滚动组件，如[ArcList](ts-container-arclist.md)、[List](ts-container-list.md)、[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)、[WaterFlow](ts-container-waterflow.md)，建议设置ScrollBar主轴方向大小，否则ScrollBar主轴方向大小可能为无穷大。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含单个子组件。

## 接口

PhonePC/2in1TabletTVWearable

ScrollBar(value: ScrollBarOptions)

创建滚动条组件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScrollBarOptions](ts-basic-components-scrollbar.md#scrollbaroptions对象说明) | 是 | 滚动条组件参数。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### enableNestedScroll14+

PhonePC/2in1TabletTVWearable

enableNestedScroll(enabled: Optional<boolean>)

设置滚动条是否嵌套滚动。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否执行嵌套滚动。设置为true执行嵌套滚动，设置为false不嵌套滚动。  默认值：false |

说明

滚动条使能嵌套滚动时，滚动条的滚动偏移量会先发送给绑定的内层滚动组件，内层滚动组件再根据设置的嵌套滚动优先级依次传递给外层父滚动组件。

WaterFlow组件的布局模式为移动窗口式（[WaterFlowLayoutMode.SLIDING\_WINDOW](ts-container-waterflow.md#waterflowlayoutmode12枚举说明)）时，不支持嵌套滚动。

设置嵌套滚动模式为[PARALLEL](ts-appendix-enums.md#nestedscrollmode10)时，父子组件同时滚动，需要开发者在[onScrollFrameBegin](ts-container-scroll.md#onscrollframebegin9)中按照所需逻辑，自行设置父子组件滚动顺序。

### scrollBarColor20+

PhonePC/2in1TabletTVWearable

scrollBarColor(color: Optional<ColorMetrics>)

设置滚动条滑块的颜色，仅滚动条不放置子组件时生效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ColorMetrics](js-apis-arkui-graphics.md#colormetrics12)> | 是 | 滚动条的颜色。  默认值：ColorMetrics.numeric(0x66182431) |

## ScrollBarOptions对象说明

PhonePC/2in1TabletTVWearable

滚动条组件参数。

说明

* ScrollBar组件负责定义可滚动区域的行为样式，ScrollBar的子节点负责定义滚动条的行为样式。
* 滚动条组件与可滚动组件通过Scroller进行绑定，且只有当两者方向相同时，才能联动，ScrollBar与可滚动组件仅支持一对一绑定。
* 从API version 12开始，ScrollBar组件没有子节点时，支持显示默认样式的滚动条。
* ScrollBar组件的显隐是通过BarState设置，组件内部会自动根据BarState设置调整opacity来控制显隐，因此ScrollBar组件设置[opacity](ts-universal-attributes-opacity.md#opacity18)属性不生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scroller | [Scroller](ts-container-scroll.md#scroller) | 否 | 否 | 可滚动组件的控制器。用于与可滚动组件进行绑定。 |
| direction | [ScrollBarDirection](ts-basic-components-scrollbar.md#scrollbardirection枚举说明) | 否 | 是 | 滚动条的方向，控制可滚动组件对应方向的滚动。  默认值：ScrollBarDirection.Vertical |
| state | [BarState](ts-appendix-enums.md#barstate) | 否 | 是 | 滚动条状态。  默认值：BarState.Auto |

## ScrollBarDirection枚举说明

PhonePC/2in1TabletTVWearable

滚动条方向枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Vertical | 0 | 纵向滚动条。 |
| Horizontal | 1 | 横向滚动条。 |

## 示例1（设置子节点）

PhonePC/2in1TabletTVWearable

该示例为ScrollBar组件有子节点时的滚动条样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ScrollBarExample {
5. private scroller: Scroller = new Scroller();
6. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];

8. build() {
9. Column() {
10. Stack({ alignContent: Alignment.End }) {
11. Scroll(this.scroller) {
12. Flex({ direction: FlexDirection.Column }) {
13. ForEach(this.arr, (item: number) => {
14. Row() {
15. Text(item.toString())
16. .width('80%')
17. .height(60)
18. .backgroundColor('#3366CC')
19. .borderRadius(15)
20. .fontSize(16)
21. .textAlign(TextAlign.Center)
22. .margin({ top: 5 })
23. }
24. }, (item: number) => item.toString())
25. }.margin({ right: 15 })
26. }
27. .width('90%')
28. .scrollBar(BarState.Off)
29. .scrollable(ScrollDirection.Vertical)

31. ScrollBar({ scroller: this.scroller, direction: ScrollBarDirection.Vertical, state: BarState.Auto }) {
32. Text()
33. .width(20)
34. .height(100)
35. .borderRadius(10)
36. .backgroundColor('#C0C0C0')
37. }.width(20).backgroundColor('#ededed')
38. }
39. }
40. }
41. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/Fhb1gYr6RI2Td5z6X1C6PQ/zh-cn_image_0000002558766174.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055146Z&HW-CC-Expire=86400&HW-CC-Sign=B1E31A98BB2884B3F3E836AC1CBC4315C9AF6F7D26C3A9E23BD27DC0075585B1)

## 示例2（不设置子节点）

PhonePC/2in1TabletTVWearable

该示例为ScrollBar组件没有子节点时的滚动条样式。从API version 20开始，可通过[scrollBarColor](ts-basic-components-scrollbar.md#scrollbarcolor20)设置滚动条颜色。

```
1. import { ColorMetrics } from '@kit.ArkUI'

3. @Entry
4. @Component
5. struct ScrollBarExample {
6. private scroller: Scroller = new Scroller();
7. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
8. @State scrollBarColor: ColorMetrics = ColorMetrics.rgba(24, 35, 48, 0.4);

10. build() {
11. Column() {
12. Stack({ alignContent: Alignment.End }) {
13. Scroll(this.scroller) {
14. Flex({ direction: FlexDirection.Column }) {
15. ForEach(this.arr, (item: number) => {
16. Row() {
17. Text(item.toString())
18. .width('80%')
19. .height(60)
20. .backgroundColor('#3366CC')
21. .borderRadius(15)
22. .fontSize(16)
23. .textAlign(TextAlign.Center)
24. .margin({ top: 5 })
25. }
26. }, (item: number) => item.toString())
27. }.margin({ right: 15 })
28. }
29. .width('90%')
30. .scrollBar(BarState.Off)
31. .scrollable(ScrollDirection.Vertical)

33. ScrollBar({ scroller: this.scroller, direction: ScrollBarDirection.Vertical, state: BarState.Auto })
34. .scrollBarColor(this.scrollBarColor)
35. }
36. }
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/zL9R4d7fRDS7cTRWHDYqRQ/zh-cn_image_0000002558606516.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055146Z&HW-CC-Expire=86400&HW-CC-Sign=62C505F4AD38BDF21EE14687F508EE674BBC65A4CAE88EA2C5B552F202AA862B)

## 示例3（支持嵌套滚动）

PhonePC/2in1TabletTVWearable

从API version 20开始，该示例通过[enableNestedScroll](ts-basic-components-scrollbar.md#enablenestedscroll14)属性使ScrollBar组件支持嵌套滚动。

```
1. import { ColorMetrics } from '@kit.ArkUI'

3. @Entry
4. @Component
5. struct StickyNestedScroll {
6. listScroller: Scroller = new Scroller();
7. @State array: number[] = [];
8. @State scrollBarColor: ColorMetrics = ColorMetrics.rgba(24, 35, 48, 0.4);

10. @Styles
11. listCard() {
12. .backgroundColor(Color.White)
13. .height(72)
14. .width('100%')
15. .borderRadius(12)
16. }

18. build() {
19. Stack() {
20. Scroll() {
21. Column() {
22. Text('Scroll Area')
23. .width('100%')
24. .height('40%')
25. .backgroundColor('#0080DC')
26. .textAlign(TextAlign.Center)
27. List({ space: 10, scroller: this.listScroller }) {
28. ForEach(this.array, (item: number) => {
29. ListItem() {
30. Text('item' + item)
31. .fontSize(16)
32. }
33. .listCard()
34. }, (item: number) => item.toString())
35. }
36. .scrollBar(BarState.Off)
37. .nestedScroll({
38. scrollForward: NestedScrollMode.PARENT_FIRST,
39. scrollBackward: NestedScrollMode.SELF_FIRST
40. })
41. .height('100%')
42. }
43. .width('100%')
44. }
45. .edgeEffect(EdgeEffect.Spring)
46. .backgroundColor('#DCDCDC')
47. .scrollBar(BarState.Off)
48. .width('100%')
49. .height('100%')

51. ScrollBar({ scroller: this.listScroller })
52. .position({ right: 0 })
53. .enableNestedScroll(true)
54. .scrollBarColor(this.scrollBarColor)
55. }
56. }

58. aboutToAppear() {
59. for (let i = 0; i < 15; i++) {
60. this.array.push(i);
61. }
62. }
63. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/Gt1_70owSI2NW3n5e8CexQ/zh-cn_image_0000002589326043.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055146Z&HW-CC-Expire=86400&HW-CC-Sign=37FAD537EAA9F5E499ABD831B1D6D2FE57B32A56E3B4F39B094C9BF420A2BA0A)
