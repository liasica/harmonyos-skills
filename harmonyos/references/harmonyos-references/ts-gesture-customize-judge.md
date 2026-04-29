---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-customize-judge
title: 自定义手势判定
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 手势处理 > 手势控制 > 自定义手势判定
category: harmonyos-references
scraped_at: 2026-04-29T13:51:37+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:7326c8264a832f4b180143e6bbc2f29c722fe51233edf3c85dc3ac2f674881ed
---

为组件提供自定义手势判定能力。开发者可根据需要，在手势识别期间，决定是否响应手势。

说明

从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## onGestureJudgeBegin

PhonePC/2in1TabletTVWearable

onGestureJudgeBegin(callback: (gestureInfo: GestureInfo, event: BaseGestureEvent) => GestureJudgeResult): T

为组件绑定自定义手势判定回调。当手势即将成功时，触发用户定义的回调获取结果。

说明

在Text组件中使用该接口时，不支持对点击事件进行自定义手势判定。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (gestureInfo: [GestureInfo](ts-gesture-common.md#gestureinfo11对象说明), event: [BaseGestureEvent](ts-gesture-common.md#basegestureevent11对象说明)) => [GestureJudgeResult](ts-gesture-common.md#gesturejudgeresult11) | 是 | 自定义手势判定回调。当手势即将成功时，触发用户定义的回调获取结果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## BaseEvent8+

PhonePC/2in1TabletTVWearable

基础事件类型。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| target | [EventTarget](ts-universal-events-click.md#eventtarget8) | 否 | 否 | 触发手势事件的元素对象。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| timestamp | number | 否 | 否 | 事件时间戳，触发事件时距离系统启动的时间间隔。  单位：ns  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| source | [SourceType](ts-gesture-settings.md#sourcetype枚举说明8) | 否 | 否 | 事件输入设备的类型。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| pressure9+ | number | 否 | 否 | 按压的压力大小。  默认值：0  取值范围：[0,1]，典型值0.913168，压感大小与数值正相关。在部分设备中，由于设备的硬件参数配置不同，可能会返回大于1的值。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| tiltX9+ | number | 否 | 否 | 手写笔在设备平面上的投影与设备平面X轴的夹角。  默认值：0  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| tiltY9+ | number | 否 | 否 | 手写笔在设备平面上的投影与设备平面Y轴的夹角。  默认值：0  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| rollAngle17+ | number | 否 | 是 | 手写笔与设备平面的夹角。  **卡片能力：** 从API version 17开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 17开始，该接口支持在元服务中使用。 |
| sourceTool9+ | [SourceTool](ts-gesture-settings.md#sourcetool枚举说明9) | 否 | 否 | 事件输入源的类型。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| axisHorizontal12+ | number | 否 | 是 | 水平轴值。  默认值：0  **说明：**  当前仅在鼠标滚轮或触控板双指滑动触发的Pan手势，或使用Ctrl+鼠标滚轮触发的Pinch手势中可以获取。  对于Shift+鼠标滚轮触发的横向滚动场景，axisHorizontal为0，滚动值体现在axisVertical中。  **卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| axisVertical12+ | number | 否 | 是 | 垂直轴值。  默认值：0  **说明：**  当前仅在鼠标滚轮或触控板双指滑动触发的Pan手势，或使用Ctrl+鼠标滚轮触发的Pinch手势中可以获取。  对于Shift+鼠标滚轮触发的横向滚动场景，滚动值体现在axisVertical中。  **卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| axisPinch21+ | number | 否 | 是 | 双指缩放比例。  默认值：0  **说明：**  仅在触控板上通过双指缩放操作触发的Pinch手势，或在轴事件中，可以获取该值；在其他场景下，获取到的将是默认值。  缩放比例是指在双指缩放事件触发过程中，双指当前距离与最初按下时距离的比值。  取值范围：[0, +∞)  **卡片能力：** 从API version 21开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |
| deviceId12+ | number | 否 | 是 | 触发当前事件的输入设备ID。  默认值：0  取值范围：[0, +∞)  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| targetDisplayId15+ | number | 否 | 是 | 事件发生的屏幕ID。  默认值：0  取值范围：[0, +∞)  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |

### getModifierKeyState12+

PhonePC/2in1TabletTVWearable

getModifierKeyState?(keys: Array<string>): boolean

获取功能键按压状态。报错信息请参考以下错误码。支持功能键'Ctrl'|'Alt'|'Shift'。

说明

此接口不支持在手写笔场景下使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keys | Array<string> | 是 | 功能键列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回功能键按压状态。当功能键均处于按压状态时返回true，否则返回false。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter verification failed. |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（自定义手势判定）

该示例通过配置[onGestureJudgeBegin](ts-gesture-customize-judge.md#ongesturejudgebegin)实现了对长按、快滑和滑动手势的自定义判定。从API version 21开始，支持通过[BaseEvent](ts-gesture-customize-judge.md#baseevent8)的axisPinch属性获取双指缩放比例。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. @State message: string = '';

7. build() {
8. Column() {
9. Row({ space: 20 }) {
10. Text(this.message).width(200).height(80).backgroundColor(Color.Pink)
11. .fontSize(25)
12. }.margin(20)
13. }
14. .width('100%')
15. .height(200)
16. .borderWidth(2)
17. .onDragStart(() => {
18. this.message = 'drag'
19. console.info("Drag start.")
20. })
21. .gesture(
22. TapGesture()
23. .tag("tap1")// 设置点击手势标志
24. .onAction(() => {
25. this.message = 'tap1'
26. })
27. )
28. .gesture(
29. LongPressGesture()
30. .tag("longPress1")// 设置长按手势标志
31. .onAction(() => {
32. this.message = 'longPress'
33. })
34. )
35. .gesture(
36. SwipeGesture()
37. .tag("swipe1")// 设置快滑手势标志
38. .onAction(() => {
39. this.message = 'swipe1'
40. })
41. )
42. .gesture(
43. PanGesture()
44. .tag("pan1")// 设置滑动手势标志
45. .onActionStart(() => {
46. this.message = 'pan1'
47. })
48. )
49. .gesture(
50. PinchGesture()
51. .tag("pinch1")// 设置捏合手势标志
52. .onActionStart(() => {
53. this.message = 'pinch1'
54. })
55. )
56. .onGestureJudgeBegin((gestureInfo: GestureInfo, event: BaseGestureEvent) => {
57. // 若该手势类型为长按手势，转换为长按手势事件
58. if (gestureInfo.type == GestureControl.GestureType.LONG_PRESS_GESTURE) {
59. let longPressEvent = event as LongPressGestureEvent;
60. console.info(`repeat ${longPressEvent.repeat}`)
61. }
62. // 若该手势类型为快滑手势，转换为快滑手势事件
63. if (gestureInfo.type == GestureControl.GestureType.SWIPE_GESTURE) {
64. let swipeEvent = event as SwipeGestureEvent;
65. console.info(`angle ${swipeEvent.angle}`)
66. }
67. // 若该手势类型为滑动手势，转换为滑动手势事件
68. if (gestureInfo.type == GestureControl.GestureType.PAN_GESTURE) {
69. let panEvent = event as PanGestureEvent;
70. console.info(`velocity ${panEvent.velocity}`)
71. }
72. // 若该手势类型为捏合手势，转换为捏合手势事件
73. if (gestureInfo.type == GestureControl.GestureType.PINCH_GESTURE) {
74. let pinchEvent = event as PinchGestureEvent;
75. console.info(`axisPinch ${pinchEvent.axisPinch}`)
76. }
77. // 自定义判定标准
78. if (gestureInfo.type == GestureControl.GestureType.DRAG) {
79. // 返回 GestureJudgeResult.REJECT 会使拖动手势失败。
80. return GestureJudgeResult.REJECT;
81. } else if (gestureInfo.tag === 'longPress1' && event.fingerList.length > 0 && event.fingerList[0].localY < 100) {
82. // 返回 GestureJudgeResult.CONTINUE 将保持系统判定。
83. return GestureJudgeResult.CONTINUE;
84. }
85. return GestureJudgeResult.CONTINUE;
86. })
87. }
88. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/I9KhgbvLSYOao_RW1hMjCQ/zh-cn_image_0000002558766108.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055136Z&HW-CC-Expire=86400&HW-CC-Sign=A4E36028EC0520B025416FC25ED9B41F9A85F80CDFB6AF189AC1203E00FDE98D)

### 示例2（自定义区域手势判定）

该示例通过配置onGestureJudgeBegin判定区域决定长按手势和拖拽是否响应。

```
1. // xxx.ets
2. import { PromptAction } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Index {
7. scroller: Scroller = new Scroller()
8. promptAction: PromptAction = this.getUIContext().getPromptAction();

10. build() {
11. Scroll(this.scroller) {
12. Column({ space: 8 }) {
13. Text("Drag 上下两层 上层绑定长按，下层绑定拖拽。先长按后平移上半区红色区域只会响应长按，先长按后平移下半区蓝色区域只会响应拖拽")
14. .width('100%')
15. .fontSize(20)
16. .fontColor('0xffdd00')
17. .backgroundColor(0xeeddaa00)
18. Stack({ alignContent: Alignment.Center }) {
19. Column() {
20. // 模拟上半区和下半区
21. Stack().width('200vp').height('100vp').backgroundColor(Color.Red)
22. Stack().width('200vp').height('100vp').backgroundColor(Color.Blue)
23. }.width('200vp').height('200vp')

25. // Stack的下半区是绑定了拖动手势的图像区域
26. Image($r('sys.media.ohos_app_icon'))
27. .draggable(true)
28. .onDragStart(() => {
29. this.promptAction.showToast({ message: "Drag 下半区蓝色区域，Image响应" })
30. })
31. .width('200vp').height('200vp')
32. // Stack的上半区是绑定了长按手势的浮动区域
33. Stack() {
34. }
35. .width('200vp')
36. .height('200vp')
37. .hitTestBehavior(HitTestMode.Transparent)
38. .onGestureJudgeBegin((gestureInfo: GestureInfo, event: BaseGestureEvent) => {
39. // 确定gestureInfo的tag标志是否有值
40. if (gestureInfo.tag) {
41. console.info(`gestureInfo tag ${gestureInfo.tag.toString()}`)
42. }
43. console.info(`gestureInfo Type ${gestureInfo.type.toString()}`);
44. console.info(`isSystemGesture ${gestureInfo.isSystemGesture}`);
45. console.info(`zqs pressure ${event.pressure}\nfingerList.length ${event.fingerList.length}\ntimeStamp ${event.timestamp}\nsourceType ${event.source.toString()}\n` +
46. `tiltX ${event.tiltX}\ntiltY ${event.tiltY}\nrollAngle ${event.rollAngle}\nsourcePool ${event.sourceTool.toString()}`);
47. // 如果是长按类型手势，判断点击的位置是否在上半区
48. if (gestureInfo.type == GestureControl.GestureType.LONG_PRESS_GESTURE) {
49. if (event.fingerList.length > 0 && event.fingerList[0].localY < 100) {
50. return GestureJudgeResult.CONTINUE
51. } else {
52. return GestureJudgeResult.REJECT
53. }
54. }
55. return GestureJudgeResult.CONTINUE
56. })
57. .gesture(GestureGroup(GestureMode.Parallel,
58. LongPressGesture()
59. .onAction((event: GestureEvent) => {
60. this.promptAction.showToast({ message: "LongPressGesture 长按上半区 红色区域，红色区域响应" })
61. })
62. .tag("tap111")
63. ))

65. }.width('100%')
66. }.width('100%')
67. }
68. }
69. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/VDcZuRwXQYuN4Q9qfvvT-A/zh-cn_image_0000002558606450.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055136Z&HW-CC-Expire=86400&HW-CC-Sign=ADEEC10F73168E5C46992A1902E5CAC5CDBFF37E5EDABFCE15DDE2B1E7A797DA)

### 示例3（实时监测参与手势的有效触点的数量及其简要信息）

该示例通过配置fingerInfos实时检测参与手势的有效触点数量、各个触点ID及其坐标

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct GestureDetectorExample {
5. @State message: string = '触摸区域'
6. @State fingerCount: number = 0
7. @State fingerDetails: string = ''

9. build() {
10. Column() {
11. // 显示信息区域
12. Column() {
13. Text(this.message)
14. .fontSize(20)
15. .fontWeight(FontWeight.Bold)

17. Text(`触点数量: ${this.fingerCount}`)
18. .fontSize(16)
19. .margin({ top: 8 })

22. Text(this.fingerDetails)
23. .fontSize(14)
24. .margin({ top: 8 })
25. }
26. .padding(10)
27. .border({ width: 1, color: Color.Gray })

29. // 手势检测区域
30. Column()
31. .width('90%')
32. .height(200)
33. .margin(20)
34. .border({ width: 2, color: Color.Black })
35. .gesture(
36. GestureGroup(GestureMode.Exclusive,
37. TapGesture()
38. .onAction(() => {
39. this.message = '单击事件'
40. }),
41. LongPressGesture()
42. .onAction(() => {
43. this.message = '长按事件'
44. }),
45. PanGesture()
46. .onActionStart(() => {
47. this.message = '拖动开始'
48. })
49. .onActionUpdate(() => {
50. this.message = '拖动中...'
51. })
52. .onActionEnd(() => {
53. this.message = '拖动结束'
54. this.fingerCount = 0
55. this.fingerDetails = ''
56. })
57. )
58. )
59. .onGestureJudgeBegin((gestureInfo: GestureInfo, event: BaseGestureEvent) => {
60. // 获取 fingerInfos 信息
61. if (event?.fingerInfos) {
62. this.fingerCount = event.fingerInfos.length
63. this.fingerDetails = event.fingerInfos.map(finger =>
64. `ID：${finger.id}: (${finger.localX.toFixed(1)}, ${finger.localY.toFixed(1)})`
65. ).join('\n')
66. console.info(`触点信息：${JSON.stringify(event.fingerInfos)}`)
67. }
68. if (this.fingerCount > 2) {
69. return GestureJudgeResult.REJECT
70. }
71. return GestureJudgeResult.CONTINUE
72. })
73. }
74. .width('100%')
75. .height('100%')
76. .padding(10)
77. }
78. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/UEXIkHAaRI25XdMBxrEHLQ/zh-cn_image_0000002589325977.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055136Z&HW-CC-Expire=86400&HW-CC-Sign=350E7F6719D0B2C5769A385A4528E3BB3CC709AEDB8E036D05B99DF8A0CF2236)
