---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-on-child-touch-test
title: 自定义事件分发
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 交互事件分发控制 > 自定义事件分发
category: harmonyos-references
scraped_at: 2026-04-29T13:51:08+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bdf770bf608becede6197a9c34b136eda53c63c3cd96bbfbe4a7159c0c6a666c
---

在处理触屏事件时，ArkUI会在触屏事件触发前进行按压点和组件区域的[触摸测试](../harmonyos-guides/arkts-interaction-basic-principles.md#触摸测试)，收集需要响应触屏事件的组件，再基于触摸测试结果分发相应的触屏事件。在父节点，可以通过onChildTouchTest决定子节点的触摸测试方式，影响子组件的触摸测试，从而影响后续的触屏事件分发。具体影响参考[TouchTestStrategy](ts-universal-attributes-on-child-touch-test.md#touchteststrategy11枚举说明)枚举说明。

说明

* 从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* onClick和旋转、捏合手势经过自定义事件分发后，可能会因为未命中触摸热区导致事件不响应。

## onChildTouchTest11+

PhonePC/2in1TabletTVWearable

onChildTouchTest(event: (value: Array<TouchTestInfo>) => TouchResult): T

当前组件通过设置回调，可自定义触摸测试并控制触摸测试中的子节点行为。

说明

* 子节点信息数组中仅包含命名节点的信息，即开发者通过id属性设置了id的节点。
* 从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (value: Array<[TouchTestInfo>](ts-universal-attributes-on-child-touch-test.md#touchtestinfo11)) => TouchResult | 是 | 触摸事件信息。value的值为包含子节点信息的数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## TouchTestInfo11+

PhonePC/2in1TabletTVWearable

当前屏幕触点所在组件的坐标系、id和尺寸相关信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| windowX | number | 否 | 否 | 按压点相对于窗口左上角的x轴坐标。  单位：vp |
| windowY | number | 否 | 否 | 按压点相对于窗口左上角的y轴坐标。  单位：vp |
| parentX | number | 否 | 否 | 按压点相对于父组件左上角的x轴坐标。  单位：vp |
| parentY | number | 否 | 否 | 按压点相对于父组件左上角的y轴坐标。  单位：vp |
| x | number | 否 | 否 | 按压点相对于子组件左上角的x轴坐标。  单位：vp |
| y | number | 否 | 否 | 按压点相对于子组件左上角的y轴坐标。  单位：vp |
| rect | [RectResult](ts-universal-attributes-on-child-touch-test.md#rectresult) | 否 | 否 | 子组件的位置和宽高。 |
| [id](ts-universal-attributes-component-id.md#id) | string | 否 | 否 | 子组件的唯一标识。 |

## RectResult

PhonePC/2in1TabletTVWearable

位置和尺寸类型，用于描述组件的位置和宽高。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 水平方向横坐标。  单位：vp |
| y | number | 否 | 否 | 竖直方向纵坐标。  单位：vp |
| width | number | 否 | 否 | 内容宽度大小。  单位：vp |
| height | number | 否 | 否 | 内容高度大小。  单位：vp |

## TouchResult11+

PhonePC/2in1TabletTVWearable

自定义事件分发结果，开发者通过返回结果来影响事件分发。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| strategy | [TouchTestStrategy](ts-universal-attributes-on-child-touch-test.md#touchteststrategy11枚举说明) | 否 | 否 | 事件派发策略。 |
| id | string | 否 | 是 | 子组件的唯一标识。  当strategy为TouchTestStrategy.DEFAULT时，id是可选的；当strategy是TouchTestStrategy.FORWARD\_COMPETITION或TouchTestStrategy.FORWARD时，id是必需的（如果没有返回id，则当成TouchTestStrategy.DEFAULT处理）。 |

## TouchTestStrategy11+枚举说明

PhonePC/2in1TabletTVWearable

事件派发策略。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 自定义分发不产生影响，系统按当前节点命中状态分发事件。 |
| FORWARD\_COMPETITION | 1 | 应用指定分发事件到某个子节点，其他兄弟节点是否分发事件交由系统决定。 |
| FORWARD | 2 | 应用指定分发事件到某个子节点，系统不再分发事件到其他兄弟节点。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置事件派发策略为FORWARD\_COMPETITION）

该示例点击List下方空白区域后拖动，可使List滑动。点击Button按钮时，Button会响应onClick事件。

```
1. // xxx.ets
2. import { PromptAction } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct ListExample {
7. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
8. promptAction: PromptAction = this.getUIContext().getPromptAction();
9. @State text: string = 'Button'

11. build() {
12. Column() {
13. List({ space: 12, initialIndex: 0 }) {
14. ForEach(this.arr, (item: number) => {
15. ListItem() {
16. Text('Item ' + item)
17. .width('100%')
18. .height(56)
19. .fontSize(16)
20. .textAlign(TextAlign.Start)
21. }.borderRadius(24)
22. .backgroundColor(Color.White)
23. .padding({ left: 12, right: 12 })
24. }, (item: number) => item.toString())
25. }
26. .listDirection(Axis.Vertical)
27. .scrollBar(BarState.Off)
28. .edgeEffect(EdgeEffect.Spring)
29. .onScrollIndex((start: number, end: number) => {
30. console.info(`first ${start}`)
31. console.info(`last ${end}`)
32. })
33. .onDidScroll((scrollOffset: number, scrollState: ScrollState) => {
34. console.info(`onScroll scrollState = ScrollState ${scrollState.toString()}, scrollOffset = ${scrollOffset}`)
35. })
36. .width('100%')
37. .height('65%')
38. .id('MyList')

40. Button(this.text)
41. .width(312)
42. .height(40)
43. .id('MyButton')
44. .fontSize(16)
45. .fontWeight(FontWeight.Medium)
46. .margin({ top: 80 })
47. .onClick(() => {
48. this.text = 'click the button'
49. this.promptAction.showToast({ message: 'you click the button.', duration: 3000 })
50. })
51. }
52. .width('100%')
53. .height('100%')
54. .backgroundColor(0xF1F3F5)
55. .justifyContent(FlexAlign.End)
56. .padding({ left: 12, right: 12, bottom: 24 })
57. .onChildTouchTest((touchInfo) => {
58. for (let info of touchInfo) {
59. if (info.id == 'MyList') {
60. return { id: info.id, strategy: TouchTestStrategy.FORWARD_COMPETITION }
61. }
62. }
63. return { strategy: TouchTestStrategy.DEFAULT }
64. })
65. }
66. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/H876hI8zTciu955VDYAbnA/zh-cn_image_0000002558765994.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055107Z&HW-CC-Expire=86400&HW-CC-Sign=AE69CD87D8452D9C581CBC867144AD40D7340A447E85AEF0ABF53F84BBE74BE5)

### 示例2（设置事件派发策略为FORWARD）

点击List下方空白区域后拖动，可以滑动List。点击Button按钮时，Button不会响应onClick事件。

```
1. // xxx.ets
2. import { PromptAction } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct ListExample {
7. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
8. promptAction: PromptAction = this.getUIContext().getPromptAction();
9. @State text: string = 'Button'

11. build() {
12. Column() {
13. List({ space: 12, initialIndex: 0 }) {
14. ForEach(this.arr, (item: number) => {
15. ListItem() {
16. Text('Item ' + item)
17. .width('100%')
18. .height(56)
19. .fontSize(16)
20. .textAlign(TextAlign.Start)
21. }.borderRadius(24)
22. .backgroundColor(Color.White)
23. .padding({ left: 12, right: 12 })
24. }, (item: number) => item.toString())
25. }
26. .listDirection(Axis.Vertical)
27. .scrollBar(BarState.Off)
28. .edgeEffect(EdgeEffect.Spring)
29. .onScrollIndex((start: number, end: number) => {
30. console.info(`first ${start}`)
31. console.info(`last ${end}`)
32. })
33. .onDidScroll((scrollOffset: number, scrollState: ScrollState) => {
34. console.info(`onScroll scrollState = ScrollState ${scrollState.toString()}, scrollOffset = ${scrollOffset}`)
35. })
36. .width('100%')
37. .height('65%')
38. .id('MyList')

40. Button(this.text)
41. .width(312)
42. .height(40)
43. .id('MyButton')
44. .fontSize(16)
45. .fontWeight(FontWeight.Medium)
46. .margin({ top: 80 })
47. .onClick(() => {
48. this.text = 'click the button'
49. this.promptAction.showToast({ message: 'you click the button.', duration: 3000 })
50. })
51. }
52. .width('100%')
53. .height('100%')
54. .backgroundColor(0xF1F3F5)
55. .justifyContent(FlexAlign.End)
56. .padding({ left: 12, right: 12, bottom: 24 })
57. .onChildTouchTest((touchInfo) => {
58. for (let info of touchInfo) {
59. if (info.id == 'MyList') {
60. return { id: info.id, strategy: TouchTestStrategy.FORWARD }
61. }
62. }
63. return { strategy: TouchTestStrategy.DEFAULT }
64. })
65. }
66. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/JOsvndPFQCmZObtm4OFzEA/zh-cn_image_0000002558606336.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055107Z&HW-CC-Expire=86400&HW-CC-Sign=B364DF0C021006AF1A5391A7948926DFBA7A299B8711E871E29472EAE86A0658)

### 示例3（设置事件派发策略为DEFAULT）

点击List下方空白区域后拖动，List不会滑动。点击Button按钮时，Button会响应onClick事件。

```
1. // xxx.ets
2. import { PromptAction } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct ListExample {
7. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
8. promptAction: PromptAction = this.getUIContext().getPromptAction();
9. @State text: string = 'Button'

11. build() {
12. Column() {
13. List({ space: 12, initialIndex: 0 }) {
14. ForEach(this.arr, (item: number) => {
15. ListItem() {
16. Text('Item ' + item)
17. .width('100%')
18. .height(56)
19. .fontSize(16)
20. .textAlign(TextAlign.Start)
21. }.borderRadius(24)
22. .backgroundColor(Color.White)
23. .padding({ left: 12, right: 12 })
24. }, (item: number) => item.toString())
25. }
26. .listDirection(Axis.Vertical)
27. .scrollBar(BarState.Off)
28. .edgeEffect(EdgeEffect.Spring)
29. .onScrollIndex((start: number, end: number) => {
30. console.info(`first ${start}`)
31. console.info(`last ${end}`)
32. })
33. .onDidScroll((scrollOffset: number, scrollState: ScrollState) => {
34. console.info(`onScroll scrollState = ScrollState ${scrollState.toString()}, scrollOffset = ${scrollOffset}`)
35. })
36. .width('100%')
37. .height('65%')
38. .id('MyList')

40. Button(this.text)
41. .width(312)
42. .height(40)
43. .id('MyButton')
44. .fontSize(16)
45. .fontWeight(FontWeight.Medium)
46. .margin({ top: 80 })
47. .onClick(() => {
48. this.text = 'click the button'
49. this.promptAction.showToast({ message: 'you click the button.', duration: 3000 })
50. })
51. }
52. .width('100%')
53. .height('100%')
54. .backgroundColor(0xF1F3F5)
55. .justifyContent(FlexAlign.End)
56. .padding({ left: 12, right: 12, bottom: 24 })
57. .onChildTouchTest((touchInfo) => {
58. return { strategy: TouchTestStrategy.DEFAULT }
59. })
60. }
61. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/Ygr8xUcJSGur0KTHOBtiKQ/zh-cn_image_0000002589325863.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055107Z&HW-CC-Expire=86400&HW-CC-Sign=741DD0CC362D26A71BEC1FF78A92AE9E9C034AB26C923E3D9DB80C837B128238)
