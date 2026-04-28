---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-touch
title: 触摸事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 基础输入事件 > 触摸事件
category: harmonyos-references
scraped_at: 2026-04-28T08:00:53+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:a3c34734f3f6630b442eeebea6f11d174b01d695433facc2e17bed8d270e1471
---

由手指、手写笔或鼠标左键在组件上按下、滑动或抬起时触发。

说明

* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 事件分发可参考[事件交互流程](../harmonyos-guides/arkts-interaction-basic-principles.md#事件交互流程)，手势事件处理流程可参考[多层级手势事件](../harmonyos-guides/arkts-gesture-events-multi-level-gesture.md)。
* 如需绑定手势事件可参考[绑定手势方法](ts-gesture-settings.md)。

## onTouch

PhonePC/2in1TabletTVWearable

onTouch(event: (event: TouchEvent) => void): T

手指触摸动作触发该回调。触摸事件默认[冒泡](../harmonyos-guides/arkts-interaction-basic-principles.md#事件冒泡)，会被多个组件消费，如果需阻止冒泡，可参考[TouchEvent](ts-universal-events-touch.md#touchevent对象说明)的stopPropagation方法。鼠标左键按下时，对应的事件也会转换成触摸事件并触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [TouchEvent](ts-universal-events-touch.md#touchevent对象说明)) => void | 是 | 获得TouchEvent对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## TouchEvent对象说明

PhonePC/2in1TabletTVWearable

继承于[BaseEvent](ts-gesture-customize-judge.md#baseevent8)。在非事件注入场景下，changedTouches是按屏幕刷新率重采样的点，而touches是按器件刷新率上报的点，因此changedTouches与touches的数据可能不同。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [TouchType](ts-appendix-enums.md#touchtype) | 否 | 否 | 触摸事件的类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| touches | [TouchObject](ts-universal-events-touch.md#touchobject)[] | 否 | 否 | 全部屏幕触点（多指）的信息，每个元素代表一个触点。在使用该属性时，需要校验是否为空。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| changedTouches | [TouchObject](ts-universal-events-touch.md#touchobject)[] | 否 | 否 | 发生变化而产生事件的手指信息。在使用该属性时，需要校验是否为空。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| stopPropagation | () => void | 否 | 否 | 阻塞[事件冒泡](../harmonyos-guides/arkts-interaction-basic-principles.md#事件冒泡)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| preventDefault12+ | () => void | 否 | 否 | 阻止默认事件。  **说明：** 该接口仅支持部分组件使用，当前支持组件：[Hyperlink](ts-container-hyperlink.md)，不支持的组件在使用时会抛出异常。暂不支持异步调用和提供Modifier接口。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

**错误码：**

以下错误码的详细介绍请参见[交互事件错误码](errorcode-event.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100017 | Component does not support prevent function. |

### getHistoricalPoints10+

PhonePC/2in1TabletTVWearable

getHistoricalPoints(): Array<HistoricalPoint>

获取当前帧的所有历史点。不同设备每帧的触摸事件频率不同，且该接口仅能在[TouchEvent](ts-universal-events-touch.md#touchevent对象说明)中调用，用于获取触发[onTouch](ts-universal-events-touch.md#ontouch)时当前帧历史点的相关信息。[onTouch](ts-universal-events-touch.md#ontouch)一帧通常只会调用一次，如果当前帧收到的[TouchEvent](ts-universal-events-touch.md#touchevent对象说明)数目大于1，会将该帧最后一个点通过[onTouch](ts-universal-events-touch.md#ontouch)返回，其余点作为历史点。如果多指在同一帧上报事件，可能触发多次onTouch。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[HistoricalPoint](ts-universal-events-touch.md#historicalpoint10对象说明)> | 由历史点组成的数组。 |

## TouchObject

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [TouchType](ts-appendix-enums.md#touchtype) | 否 | 否 | 触摸事件的类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| id | number | 否 | 否 | 手指唯一标识符。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| x | number | 否 | 否 | 触摸点在事件响应组件为基准的[组件坐标系](../harmonyos-guides/arkui-glossary.md#组件坐标系)中的X坐标。  单位：vp  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| y | number | 否 | 否 | 触摸点在事件响应组件为基准的[组件坐标系](../harmonyos-guides/arkui-glossary.md#组件坐标系)中的Y坐标。  单位：vp  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| windowX10+ | number | 否 | 否 | 触摸点在当前应用窗口坐标系中的X坐标。  单位：vp  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| windowY10+ | number | 否 | 否 | 触摸点在当前应用窗口坐标系中的Y坐标。  单位：vp  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| displayX10+ | number | 否 | 否 | 触摸点在当前应用屏幕坐标系中的X坐标。  单位：vp  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| displayY10+ | number | 否 | 否 | 触摸点在当前应用屏幕坐标系中的Y坐标。  单位：vp  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| screenX(deprecated) | number | 否 | 否 | 触摸点在当前应用窗口坐标系中的X坐标。  单位：vp  **说明：** 从API version 7开始支持，从API version 10开始废弃，建议使用windowX替代。 |
| screenY(deprecated) | number | 否 | 否 | 触摸点在当前应用窗口坐标系中的Y坐标。  单位：vp  **说明：** 从API version 7开始支持，从API version 10开始废弃，建议使用windowY替代。 |
| pressedTime15+ | number | 否 | 是 | 当前手指按下的时间。  单位：ns  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| pressure15+ | number | 否 | 是 | 当前手指按压的压力值。  取值范围：[0,65535)，压力越大，值越大。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| width15+ | number | 否 | 是 | 当前手指按压区域的宽度。  单位：vp  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| height15+ | number | 否 | 是 | 当前手指按压区域的高度。  单位：vp  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| hand15+ | [InteractionHand](ts-appendix-enums.md#interactionhand15) | 否 | 是 | 表示事件是由左手点击还是右手点击触发。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| globalDisplayX20+ | number | 否 | 是 | 触摸点在[全局坐标系](../harmonyos-guides/window-terminology.md#全局坐标系)中的X坐标。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| globalDisplayY20+ | number | 否 | 是 | 触摸点在[全局坐标系](../harmonyos-guides/window-terminology.md#全局坐标系)中的Y坐标。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## HistoricalPoint10+对象说明

PhonePC/2in1TabletTVWearable

历史点信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| touchObject | [TouchObject](ts-universal-events-touch.md#touchobject) | 否 | 否 | 历史点对应触摸事件的基础信息。 |
| size | number | 否 | 否 | 历史点对应触摸事件中手指与屏幕的触摸区域大小。  默认值：0 |
| force | number | 否 | 否 | 历史点对应触摸事件的压力大小。  默认值：0  取值范围：[0,65535)，压力越大，值越大。 |
| timestamp | number | 否 | 否 | 历史点对应触摸事件的时间戳，表示触发事件时距离系统启动的时间间隔。  单位：ns |

## 示例

PhonePC/2in1TabletTVWearable

该示例中，按钮设置触摸事件，在点击按钮时可获取事件的相关参数。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TouchExample {
5. @State text: string = '';
6. @State eventType: string = '';

8. build() {
9. Column() {
10. Button('Touch').height(40).width(100)
11. .onTouch((event?: TouchEvent) => {
12. if (event && event.sourceTool === SourceTool.Finger) {
13. if (event.type === TouchType.Down) {
14. this.eventType = 'Down';
15. }
16. if (event.type === TouchType.Up) {
17. this.eventType = 'Up';
18. }
19. if (event.type === TouchType.Move) {
20. this.eventType = 'Move';
21. }
22. // 1.手指按住屏幕同时点击Home键返回桌面，此时会触发Cancel
23. // 2.折叠屏手机，应用在按住屏幕的情况下折叠手机切换到外屏，此时会触发Cancel
24. if (event.type === TouchType.Cancel) {
25. this.eventType = 'Cancel';
26. }
27. if (event.touches) {
28. this.text = 'TouchType:' + this.eventType
29. + '\nDistance between touch point and touch element:'
30. + '\n  x: ' + event.touches[0].x + '\n  y: ' + event.touches[0].y
31. + '\n  width: ' + event.touches[0].width + '\n  height: ' + event.touches[0].height
32. + '\n  pressedTime: ' + event.touches[0].pressedTime
33. + '\n  pressure: ' + event.touches[0].pressure
34. + '\nComponent globalPos:'
35. + '\n  x: ' + event.target.area.globalPosition.x + '\n  y: ' + event.target.area.globalPosition.y
36. + '\n  width: ' + event.target.area.width + '\n  height: ' + event.target.area.height
37. + '\ntargetDisplayId: ' + event.targetDisplayId;
38. }
39. }
40. })
41. Button('Touch').height(50).width(200).margin(20)
42. .onTouch((event?: TouchEvent) => {
43. if (event) {
44. if (event.type === TouchType.Down) {
45. this.eventType = 'Down';
46. }
47. if (event.type === TouchType.Up) {
48. this.eventType = 'Up';
49. }
50. if (event.type === TouchType.Move) {
51. this.eventType = 'Move';
52. }
53. // 1.手指按住屏幕同时点击Home键返回桌面，此时会触发Cancel
54. // 2.折叠屏手机，应用在按住屏幕的情况下折叠手机切换到外屏，此时会触发Cancel
55. if (event.type === TouchType.Cancel) {
56. this.eventType = 'Cancel';
57. }
58. if (event.touches) {
59. this.text = 'TouchType:' + this.eventType
60. + '\nDistance between touch point and touch element:'
61. + '\n  x: ' + event.touches[0].x + '\n  y: ' + event.touches[0].y
62. + '\n  width: ' + event.touches[0].width + '\n  height: ' + event.touches[0].height
63. + '\n  pressedTime: ' + event.touches[0].pressedTime
64. + '\n  pressure: ' + event.touches[0].pressure
65. + '\nComponent globalPos:'
66. + '\n  x: ' + event.target.area.globalPosition.x + '\n  y: ' + event.target.area.globalPosition.y
67. + '\n  width: ' + event.target.area.width + '\n  height: ' + event.target.area.height
68. + '\ntargetDisplayId: ' + event.targetDisplayId;
69. }
70. }
71. })
72. Text(this.text)
73. }.width('100%').padding(30)
74. }
75. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/zFLbtVjqQJ2_hzXucWdxvw/zh-cn_image_0000002552959462.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000052Z&HW-CC-Expire=86400&HW-CC-Sign=1A5C108E3E274538ADAFC3FCCA188FCCBEF1469D1370BD0161CDEC3F1A7746DD)
