---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-settings
title: 绑定手势方法
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 手势处理 > 绑定手势 > 绑定手势方法
category: harmonyos-references
scraped_at: 2026-04-28T08:01:19+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:56c51c17a732af2ab619a9a2ae8836098165cca804c73b8eddfd50b9439c9504
---

为组件绑定不同类型的手势事件，并设置事件的响应方法。

说明

* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 可以通过gesture、priorityGesture和parallelGesture给组件绑定手势识别，手势识别成功后可以通过事件回调通知组件。可以通过[触摸热区](ts-universal-attributes-touch-target.md)指定可识别手势的区域。gesture、priorityGesture和parallelGesture当前不支持使用三目运算符（条件? 表达式1 : 表达式2）切换手势绑定。

## gesture

PhonePC/2in1TabletTVWearable

gesture(gesture: GestureType, mask?: GestureMask): T

绑定手势。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| gesture | [GestureType](ts-gesture-common.md#gesturetype) | 是 | 绑定的手势类型。 |
| mask | [GestureMask](ts-gesture-common.md#gesturemask枚举说明) | 否 | 事件响应设置。  默认值：GestureMask.Normal |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## priorityGesture

PhonePC/2in1TabletTVWearable

priorityGesture(gesture: GestureType, mask?: GestureMask): T

绑定优先识别手势。

1. 默认情况下，子组件优先识别通过gesture绑定的手势，当父组件配置priorityGesture时，父组件优先识别priorityGesture绑定的手势。
2. 绑定长按手势时，设置触发长按的最短时间小的组件会优先响应，会忽略priorityGesture设置。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| gesture | [GestureType](ts-gesture-common.md#gesturetype) | 是 | 绑定的手势对象。 |
| mask | [GestureMask](ts-gesture-common.md#gesturemask枚举说明) | 否 | 事件响应设置。  默认值：GestureMask.Normal |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## parallelGesture

PhonePC/2in1TabletTVWearable

parallelGesture(gesture: GestureType, mask?: GestureMask): T

绑定可与子组件手势同时触发的手势。手势事件为非冒泡事件。父组件设置parallelGesture时，父子组件相同的手势事件都可以触发，实现类似冒泡效果。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| gesture | [GestureType](ts-gesture-common.md#gesturetype) | 是 | 绑定的手势对象。 |
| mask | [GestureMask](ts-gesture-common.md#gesturemask枚举说明) | 否 | 事件响应设置。  默认值：GestureMask.Normal |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## SourceType枚举说明8+

PhonePC/2in1TabletTVWearable

定义输入源对应的设备类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Unknown | 0 | 未知输入源。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Mouse | 1 | 鼠标。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| TouchScreen | 2 | 触摸屏。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| KEY22+ | 4 | 按键。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| JOYSTICK22+ | 5 | 手柄。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |

## SourceTool枚举说明9+

PhonePC/2in1TabletTVWearable

定义输入源对应的工具类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Unknown | 0 | 未知输入源。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Finger | 1 | 手指输入。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Pen | 2 | 手写笔输入。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| MOUSE12+ | 7 | 鼠标输入。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| TOUCHPAD12+ | 9 | 触控板输入。触控板单指输入被视为鼠标输入操作。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| JOYSTICK12+ | 10 | 手柄输入。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（父组件优先识别手势和父子组件同时触发手势）

该示例通过配置priorityGesture和parallelGesture分别实现了父组件优先识别手势和父子组件同时触发手势。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct GestureSettingsExample {
5. @State priorityTestValue: string = ''
6. @State parallelTestValue: string = ''

8. build() {
9. Column() {
10. Column() {
11. Text('TapGesture:' + this.priorityTestValue).fontSize(28)
12. .gesture(
13. TapGesture()
14. .onAction((event: GestureEvent) => {
15. this.priorityTestValue += '\nText'
16. }))
17. }
18. .height(200)
19. .width(250)
20. .padding(20)
21. .margin(20)
22. .border({ width: 3 })
23. // 设置为priorityGesture时，点击文本会忽略Text组件的TapGesture手势事件，优先识别父组件Column的TapGesture手势事件
24. .priorityGesture(
25. TapGesture()
26. .onAction((event: GestureEvent) => {
27. this.priorityTestValue += '\nColumn'
28. }), GestureMask.IgnoreInternal)

30. Column() {
31. Text('TapGesture:' + this.parallelTestValue).fontSize(28)
32. .gesture(
33. TapGesture()
34. .onAction((event: GestureEvent) => {
35. this.parallelTestValue += '\nText'
36. }))
37. }
38. .height(200)
39. .width(250)
40. .padding(20)
41. .margin(20)
42. .border({ width: 3 })
43. // 设置为parallelGesture时，点击文本会同时触发子组件Text与父组件Column的TapGesture手势事件
44. .parallelGesture(
45. TapGesture()
46. .onAction((event: GestureEvent) => {
47. this.parallelTestValue += '\nColumn'
48. }), GestureMask.Normal)
49. }
50. }
51. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/ooOhRqVNSJ-UCFFTurnxVQ/zh-cn_image_0000002583439625.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000118Z&HW-CC-Expire=86400&HW-CC-Sign=0FD905D849604AFAF7BBAFC0E7CDE74AC4BF672578A5B24F29FD07BD280E4F23)

### 示例2（实时监测参与滑动手势的有效触点数量）

该示例通过配置fingerInfos实时监测参与滑动手势的有效触点数量。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PanGestureWithFingerCount {
5. @State offsetX: number = 0
6. @State offsetY: number = 0
7. @State positionX: number = 0
8. @State positionY: number = 0
9. @State fingerCount: number = 0 // 用于记录参与手势的触点数量
10. private panOption: PanGestureOptions = new PanGestureOptions({
11. direction: PanDirection.All,
12. fingers: 1
13. })

15. build() {
16. Column() {
17. // 显示当前有效触点数量
18. Text(`触点数量: ${this.fingerCount}`)
19. .fontSize(20)
20. .margin(10)

22. Column() {
23. Text('PanGesture offset:\nX: ' + this.offsetX + '\n' + 'Y: ' + this.offsetY)
24. }
25. .height(200)
26. .width(300)
27. .padding(20)
28. .border({ width: 3 })
29. .margin(50)
30. .translate({ x: this.offsetX, y: this.offsetY, z: 0 })
31. .gesture(
32. PanGesture(this.panOption)
33. .onActionStart((event: GestureEvent) => {
34. console.info('Pan start')
35. this.fingerCount = event.fingerInfos?.length || 0 // 记录触点数量
36. })
37. .onActionUpdate((event: GestureEvent) => {
38. if (event) {
39. console.info(`fingerInfos ${JSON.stringify(event.fingerInfos)}`)
40. this.offsetX = this.positionX + event.offsetX
41. this.offsetY = this.positionY + event.offsetY
42. this.fingerCount = event.fingerInfos?.length || 0 // 更新触点数量，记录下参与当前手势的有效触点的数量
43. }
44. })
45. .onActionEnd((event: GestureEvent) => {
46. this.positionX = this.offsetX
47. this.positionY = this.offsetY
48. this.fingerCount = 0 // 触点离开触摸区域后归零
49. console.info('Pan end')
50. })
51. .onActionCancel(() => {
52. this.fingerCount = 0 // 手势取消后归零
53. })
54. )

56. Button('切换为双指滑动')
57. .onClick(() => {
58. this.panOption.setFingers(2)
59. })
60. }
61. }
62. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/Q-PFEke4SfugVlWvmqcD3g/zh-cn_image_0000002552959580.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000118Z&HW-CC-Expire=86400&HW-CC-Sign=807F72B3622386D11429DF774A4D468256463C728EF5E650AA1F3EB22EA95737)
