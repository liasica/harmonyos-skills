---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-visible-area-change-event
title: 组件可见区域变化事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 组件变化事件 > 组件可见区域变化事件
category: harmonyos-references
scraped_at: 2026-04-28T08:00:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:15b56531becdde3509ffa01f4dbd502bffc347b8927928c138fdbc977c31847a
---

组件可见区域变化事件是组件在屏幕中的显示区域面积变化时触发的事件，提供了判断组件是否完全或部分显示在屏幕中的能力，适用于广告曝光埋点之类的场景。

说明

从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## onVisibleAreaChange

PhonePC/2in1TabletTVWearable

onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback): T

组件可见区域变化时触发该回调。开发指导及常见问题请参考[感知组件可见性](../harmonyos-guides/arkts-manage-components-visibility.md)指南。

说明

* 从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。
* 仅提供自身节点相对于所有祖先节点（直到window边界）的相对裁切面积与自身面积的比值及其变化趋势。
* 不支持兄弟组件对自身节点的遮挡计算，不支持所有祖先的兄弟节点对自身节点的遮挡计算，不支持窗口遮挡计算，不支持组件旋转计算，如[Stack](ts-container-stack.md)、[Z序控制](ts-universal-attributes-z-order.md)、[rotate](ts-universal-attributes-transformation.md#rotate)等。
* 不支持非挂树节点的可见面积变化计算。例如，预加载的节点、通过[overlay](ts-universal-attributes-overlay.md#overlay)能力挂载的自定义节点。
* 不支持[scale](ts-universal-attributes-transformation.md#scale)属性，如果想要支持[scale](ts-universal-attributes-transformation.md#scale)，则需使用[onVisibleAreaChange22+](ts-universal-component-visible-area-change-event.md#onvisibleareachange22)，将measureFromViewport设置为true。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ratios | Array<number> | 是 | 阈值数组。其中，每个阈值代表组件可见面积（即组件在屏幕显示区的面积，只计算父组件内的面积，超出父组件部分不会计算）与组件自身面积的比值。当组件可见面积与自身面积的比值接近阈值时，均会触发该回调。每个阈值的取值范围为[0.0, 1.0]，如果开发者设置的阈值小于0.0，则实际取值为0.0；如果设置的阈值大于1.0，则实际取值为1.0。  **说明：**  当数值接近边界0和1时，将会按照误差不超过0.001的规则进行舍入。例如，0.9997会被近似为1。 |
| event | [VisibleAreaChangeCallback](ts-universal-component-visible-area-change-event.md#visibleareachangecallback12) | 是 | 组件可见区域变化事件的回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## onVisibleAreaChange22+

PhonePC/2in1TabletTVWearable

onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback, measureFromViewport: boolean): T

组件可见区域变化时触发该回调。可以通过measureFromViewport设置可见区域计算模式。开发指导及常见问题请参考[感知组件可见性](../harmonyos-guides/arkts-manage-components-visibility.md)指南。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ratios | Array<number> | 是 | 阈值数组。其中，每个阈值代表组件可见面积与组件自身面积的比值。当组件可见面积与自身面积的比值接近阈值时，均会触发该回调。每个阈值的取值范围为[0.0, 1.0]，如果开发者设置的阈值小于0.0，则实际取值为0.0；如果设置的阈值大于1.0，则实际取值为1.0。  **说明：**  当数值接近边界0和1时，将会按照误差不超过0.001的规则进行舍入。例如，0.9997会被近似为1。 |
| event | [VisibleAreaChangeCallback](ts-universal-component-visible-area-change-event.md#visibleareachangecallback12) | 是 | 组件可见区域变化事件的回调。 |
| measureFromViewport | boolean | 是 | 设置可见区域计算模式。  当measureFromViewport设置为true时，系统在计算该组件的可见区域时，会考虑父组件的[clip](ts-universal-attributes-sharp-clipping.md#clip12) 属性设置。如果父组件的[clip](ts-universal-attributes-sharp-clipping.md#clip12)为false，则认为其内的子组件可以超出其区域进行显示，因此超出父组件的区域也将被视为可见区域纳入计算；如果父组件的[clip](ts-universal-attributes-sharp-clipping.md#clip12)设置为true，则组件超出父组件的区域会被裁剪，无法显示，因此会被视为不可见区域进行计算。而当measureFromViewport设置为false时，则不考虑[clip](ts-universal-attributes-sharp-clipping.md#clip12)的影响，直接将组件超出父组件的部分视为不可见区域。  measureFromViewport设置为true时，祖先节点设置[scale](ts-universal-attributes-transformation.md#scale)属性，组件可见比例会被正确计算。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

说明

* 仅提供自身节点相对于所有祖先节点（直到window边界）的相对裁切面积与自身面积的比值及其变化趋势。
* 不支持兄弟组件对自身节点的遮挡计算，不支持所有祖先的兄弟节点对自身节点的遮挡计算，不支持窗口遮挡计算，不支持组件旋转计算，如[Stack](ts-container-stack.md)、[Z序控制](ts-universal-attributes-z-order.md)、[rotate](ts-universal-attributes-transformation.md#rotate)等。
* 不支持非挂树节点的可见面积变化计算。例如，预加载的节点、通过[overlay](ts-universal-attributes-overlay.md#overlay)能力挂载的自定义节点。

## onVisibleAreaApproximateChange17+

PhonePC/2in1TabletTVWearable

onVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback | undefined): T

设置onVisibleAreaApproximateChange事件的回调参数，限制它的执行间隔。

说明

从API version 23开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [VisibleAreaEventOptions](ts-universal-component-visible-area-change-event.md#visibleareaeventoptions12) | 是 | 可见区域变化相关的参数。 |
| event | [VisibleAreaChangeCallback](ts-universal-component-visible-area-change-event.md#visibleareachangecallback12) | undefined | 是 | onVisibleAreaChange事件的回调函数。当组件可见面积与自身面积的比值接近options中设置的阈值时触发该回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

说明

* 此接口与[onVisibleAreaChange](ts-universal-component-visible-area-change-event.md#onvisibleareachange)接口存在如下差异：onVisibleAreaChange在每一帧都会进行可见区域比例的计算，如果注册节点太多，系统功耗存在劣化。而此接口降低了可见区域比例计算的频度，计算间隔由[VisibleAreaEventOptions](ts-universal-component-visible-area-change-event.md#visibleareaeventoptions12)的expectedUpdateInterval参数决定。
* 当前接口的可见区域回调阈值默认包含0。例如，开发者设置回调阈值为[0.5]，实际生效的阈值为[0.0, 0.5]。
* 从API version 18开始，支持在自定义组件中调用该接口。
* 不支持[scale](ts-universal-attributes-transformation.md#scale)属性，如果想要支持[scale](ts-universal-attributes-transformation.md#scale)，则需将[VisibleAreaEventOptions](ts-universal-component-visible-area-change-event.md#visibleareaeventoptions12)的measureFromViewport设置为true。
* 从API version 21开始，返回值类型由void改为T。

## VisibleAreaEventOptions12+

PhonePC/2in1TabletTVWearable

关于区域变化相关的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ratios | Array<number> | 否 | 否 | 阈值数组。其中，每个阈值代表组件可见面积（即组件在屏幕显示区的面积，只计算父组件内的面积，超出父组件部分不会计算）与组件自身面积的比值。每个阈值的取值范围为[0.0, 1.0]，如果开发者设置的阈值小于0.0，则实际取值为0.0；如果设置的阈值大于1.0，则实际取值为1.0。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| expectedUpdateInterval | number | 否 | 是 | 定义了开发者期望的计算间隔，单位为ms。当该字段小于100或为NaN时，默认取值为100；当该字段大于2^31-1时，默认取值为2^31-1。  默认值：1000  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| measureFromViewport22+ | boolean | 否 | 是 | 设置可见区域计算模式。  当measureFromViewport设置为true时，系统在计算该组件的可见区域时，会考虑父组件的[clip](ts-universal-attributes-sharp-clipping.md#clip12) 属性设置。如果父组件的[clip](ts-universal-attributes-sharp-clipping.md#clip12)为false，则认为其内的子组件可以超出其区域进行显示，因此超出父组件的区域也将被视为可见区域纳入计算；如果父组件的[clip](ts-universal-attributes-sharp-clipping.md#clip12)设置为true，则组件超出父组件的区域会被裁剪，无法显示，因此会被视为不可见区域进行计算。而当measureFromViewport设置为false时，则不考虑[clip](ts-universal-attributes-sharp-clipping.md#clip12)的影响，直接将组件超出父组件的部分视为不可见区域。  默认值：false  measureFromViewport设置为true时，祖先节点设置[scale](ts-universal-attributes-transformation.md#scale)属性，组件可见比例会被正确计算。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |

## VisibleAreaChangeCallback12+

PhonePC/2in1TabletTVWearable

type VisibleAreaChangeCallback = (isExpanding: boolean, currentRatio: number) => void

组件可见区域变化事件的回调类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isExpanding | boolean | 是 | 视组件的可见面积与自身面积的比值与上一次回调相比的情况而定，比值变大为true，比值变小为false。 |
| currentRatio | number | 是 | 触发回调时，组件可见面积与自身面积的比值。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1 (使用onVisibleAreaChange来监听区域变化)

该示例对组件设置[onVisibleAreaChange](ts-universal-component-visible-area-change-event.md#onvisibleareachange)事件，当组件完全显示或者完全消失时触发回调。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ScrollExample {
5. scroller: Scroller = new Scroller()
6. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
7. @State testTextStr: string = 'test'
8. @State testRowStr: string = 'test'

10. build() {
11. Column() {
12. Column() {
13. Text(this.testTextStr)
14. .fontSize(20)

16. Text(this.testRowStr)
17. .fontSize(20)
18. }
19. .height(100)
20. .backgroundColor(Color.Gray)
21. .opacity(0.3)

23. Scroll(this.scroller) {
24. Column() {
25. Text("Test Text Visible Change")
26. .fontSize(20)
27. .height(200)
28. .margin({ top: 50, bottom: 20 })
29. .backgroundColor(Color.Green)
30. // 通过设置ratios为[0.0, 1.0]，实现当组件完全显示或完全消失在屏幕中时触发回调。
31. .onVisibleAreaChange([0.0, 1.0], (isExpanding: boolean, currentRatio: number) => {
32. console.info(`Test Text isExpanding: ${isExpanding}, currentRatio: ${currentRatio}`)
33. if (isExpanding && currentRatio >= 1.0) {
34. console.info(`Test Text is fully visible. currentRatio: ${currentRatio}`)
35. this.testTextStr = 'Test Text is fully visible'
36. }

38. if (!isExpanding && currentRatio <= 0.0) {
39. console.info('Test Text is completely invisible.')
40. this.testTextStr = 'Test Text is completely invisible'
41. }
42. })

44. Row() {
45. Text('Test Row Visible Change')
46. .fontSize(20)
47. .margin({ bottom: 20 })

49. }
50. .height(200)
51. .backgroundColor(Color.Yellow)
52. .onVisibleAreaChange([0.0, 1.0], (isExpanding: boolean, currentRatio: number) => {
53. console.info(`Test Text isExpanding: ${isExpanding}, currentRatio: ${currentRatio}`)
54. if (isExpanding && currentRatio >= 1.0) {
55. console.info('Test Row is fully visible.')
56. this.testRowStr = 'Test Row is fully visible'
57. }

59. if (!isExpanding && currentRatio <= 0.0) {
60. console.info('Test Row is completely invisible.')
61. this.testRowStr = 'Test Row is completely invisible'
62. }
63. })

65. ForEach(this.arr, (item: number) => {
66. Text(item.toString())
67. .width('90%')
68. .height(150)
69. .backgroundColor(0xFFFFFF)
70. .borderRadius(15)
71. .fontSize(16)
72. .textAlign(TextAlign.Center)
73. .margin({ top: 10 })
74. }, (item: number) => (item.toString()))

76. }.width('100%')
77. }
78. .backgroundColor(0x317aff)
79. .scrollable(ScrollDirection.Vertical)
80. .scrollBar(BarState.On)
81. .scrollBarColor(Color.Gray)
82. .scrollBarWidth(10)
83. .onWillScroll((xOffset: number, yOffset: number, scrollState: ScrollState) => {
84. console.info(`${xOffset} ${yOffset}`)
85. })
86. .onScrollEdge((side: Edge) => {
87. console.info('To the edge')
88. })
89. .onScrollStop(() => {
90. console.info('Scroll Stop')
91. })

93. }.width('100%').height('100%').backgroundColor(0xDCDCDC)
94. }
95. }
```

### 示例2 (使用onVisibleAreaApproximateChange来监听区域变化)

从API version 17开始，该示例对组件设置[onVisibleAreaApproximateChange](ts-universal-component-visible-area-change-event.md#onvisibleareaapproximatechange17)事件，当组件完全显示或者完全消失时触发回调。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ScrollExample {
5. scroller: Scroller = new Scroller()
6. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
7. @State testTextStr: string = 'test'
8. @State testRowStr: string = 'test'

10. build() {
11. Column() {
12. Column() {
13. Text(this.testTextStr)
14. .fontSize(20)

16. Text(this.testRowStr)
17. .fontSize(20)
18. }
19. .height(100)
20. .backgroundColor(Color.Gray)
21. .opacity(0.3)

23. Scroll(this.scroller) {
24. Column() {
25. Text("Test Text Visible Change")
26. .fontSize(20)
27. .height(200)
28. .margin({ top: 50, bottom: 20 })
29. .backgroundColor(Color.Green)
30. // 通过设置ratios为[0.0, 1.0]，实现当组件完全显示或完全消失在屏幕中时触发回调。
31. .onVisibleAreaApproximateChange({ ratios: [0.0, 1.0], expectedUpdateInterval: 1000 },
32. (isExpanding: boolean, currentRatio: number) => {
33. console.info(`Test Text isExpanding: ${isExpanding}, currentRatio: ${currentRatio}`)
34. if (isExpanding && currentRatio >= 1.0) {
35. console.info(`Test Text is fully visible. currentRatio: ${currentRatio}`)
36. this.testTextStr = 'Test Text is fully visible'
37. }

39. if (!isExpanding && currentRatio <= 0.0) {
40. console.info('Test Text is completely invisible.')
41. this.testTextStr = 'Test Text is completely invisible'
42. }
43. })

45. Row() {
46. Text('Test Row Visible Change')
47. .fontSize(20)
48. .margin({ bottom: 20 })

50. }
51. .height(200)
52. .backgroundColor(Color.Yellow)
53. .onVisibleAreaChange([0.0, 1.0], (isExpanding: boolean, currentRatio: number) => {
54. console.info(`Test Text isExpanding: ${isExpanding}, currentRatio: ${currentRatio}`)
55. if (isExpanding && currentRatio >= 1.0) {
56. console.info('Test Row is fully visible.')
57. this.testRowStr = 'Test Row is fully visible'
58. }

60. if (!isExpanding && currentRatio <= 0.0) {
61. console.info('Test Row is completely invisible.')
62. this.testRowStr = 'Test Row is completely invisible'
63. }
64. })

66. ForEach(this.arr, (item: number) => {
67. Text(item.toString())
68. .width('90%')
69. .height(150)
70. .backgroundColor(0xFFFFFF)
71. .borderRadius(15)
72. .fontSize(16)
73. .textAlign(TextAlign.Center)
74. .margin({ top: 10 })
75. }, (item: number) => (item.toString()))

77. }.width('100%')
78. }
79. .backgroundColor(0x317aff)
80. .scrollable(ScrollDirection.Vertical)
81. .scrollBar(BarState.On)
82. .scrollBarColor(Color.Gray)
83. .scrollBarWidth(10)
84. .onWillScroll((xOffset: number, yOffset: number, scrollState: ScrollState) => {
85. console.info(`${xOffset} ${yOffset}`)
86. })
87. .onScrollEdge((side: Edge) => {
88. console.info('To the edge')
89. })
90. .onScrollStop(() => {
91. console.info('Scroll Stop')
92. })

94. }.width('100%').height('100%').backgroundColor(0xDCDCDC)
95. }
96. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/VhovQO5XSbOa-WpYqkzs0w/zh-cn_image_0000002552799826.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000058Z&HW-CC-Expire=86400&HW-CC-Sign=968A67406B335D5377E50CA2E0F077E4D81C5F9EC19B8F6431F43715A873E30A)

### 示例3 (设置measureFromViewport子组件超出父组件显示)

从API version 22开始，该示例展示onVisibleAreaChange事件设置measureFromViewport参数效果对比，主要差异体现在回调返回值组件可见比例（currentRatio）的不同，设置measureFromViewport为true时，返回的组件可见比例（currentRatio）更符合实际效果。该示例在不同设备上currentRatio会有微小差异。

```
1. @Entry
2. @Component
3. struct OnVisibleAreaChangeSample {
4. @State ratio1: number = 0.0;
5. @State ratio2: number = 0.0;
6. @State ratio3: number = 0.0;

8. build() {
9. Column() {
10. Text(`onVisibleChange1 with measureFromViewport \nratio: ${this.ratio1}`)
11. Column() {
12. Row() {
13. Row() {

15. }
16. .backgroundColor(Color.Blue)
17. .height(120)
18. .width(120)
19. .offset({ x: 0, y: 60 })
20. // measureFromViewport设置为true，父组件未设置clip(true)，超出父组件的区域被视为可见区域。
21. .onVisibleAreaApproximateChange({
22. ratios: [0.0, 1.0],
23. expectedUpdateInterval: 500,
24. measureFromViewport: true
25. }, (isExpanding: boolean, currentRatio: number) => {
26. console.info(`onVisibleAreaApproximateChange1 isExpanding: ${isExpanding} currentRatio: ${currentRatio}`)
27. })
28. .onVisibleAreaChange([0.0, 1.0], (isExpanding: boolean, currentRatio: number) => {
29. this.ratio1 = currentRatio
30. }, true)
31. }
32. .backgroundColor(Color.Pink)
33. .height(120)
34. .width(120)
35. }
36. .padding(5)
37. .borderWidth(1)
38. .height(200)
39. .width(200)

41. Text(`onVisibleChange2 without measureFromViewport \nratio: ${this.ratio2}`)
42. Column() {
43. Row() {
44. Row() {

46. }
47. .backgroundColor(Color.Blue)
48. .height(120)
49. .width(120)
50. .offset({ x: 0, y: 60 })
51. // 不设置measureFromViewport，measureFromViewport默认为false，父组件未设置clip(true)，超出父组件的区域被视为不可见区域。
52. .onVisibleAreaApproximateChange({ ratios: [0.0, 1.0], expectedUpdateInterval: 500 },
53. (isExpanding: boolean, currentRatio: number) => {
54. console.info(`onVisibleAreaApproximateChange2 isExpanding: ${isExpanding} currentRatio: ${currentRatio}`)
55. })
56. .onVisibleAreaChange([0.0, 1.0], (isExpanding: boolean, currentRatio: number) => {
57. this.ratio2 = currentRatio
58. })
59. }
60. .backgroundColor(Color.Pink)
61. .height(120)
62. .width(120)
63. }
64. .padding(5)
65. .borderWidth(1)
66. .height(200)
67. .width(200)

69. Text(`parent set clip(true) onVisibleChange3 with measureFromViewport \nratio: ${this.ratio3}`)
70. Column() {
71. Row() {
72. Row() {

74. }
75. .backgroundColor(Color.Blue)
76. .height(120)
77. .width(120)
78. .offset({ x: 0, y: 60 })
79. // measureFromViewport设置为true，父组件设置clip(true)，超出父组件的区域被视为不可见区域。
80. .onVisibleAreaApproximateChange({
81. ratios: [0.0, 1.0],
82. expectedUpdateInterval: 500,
83. measureFromViewport: true
84. }, (isExpanding: boolean, currentRatio: number) => {
85. console.info(`onVisibleAreaApproximateChange3 isExpanding: ${isExpanding} currentRatio: ${currentRatio}`)
86. })
87. .onVisibleAreaChange([0.0, 1.0], (isExpanding: boolean, currentRatio: number) => {
88. this.ratio3 = currentRatio
89. }, true)
90. }
91. .clip(true)
92. .backgroundColor(Color.Pink)
93. .height(120)
94. .width(120)
95. }
96. .padding(5)
97. .borderWidth(1)
98. .height(200)
99. .width(200)
100. }
101. .height('100%')
102. .width('100%')
103. }
104. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/gafWvamhThyznhSPnF2jog/zh-cn_image_0000002583439521.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000058Z&HW-CC-Expire=86400&HW-CC-Sign=69C81032CC9E7629B9BBA58C15CE6E0D01DCB0C734331A3FE91C95F5822D1166)
