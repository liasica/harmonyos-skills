---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-longpressgesture
title: LongPressGesture
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 手势处理 > 基础手势 > LongPressGesture
category: harmonyos-references
scraped_at: 2026-04-29T13:51:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9424da64b255646e8270ad8c8c069dc356733b3599129b70d83185c20cba7ce5
---

用于触发长按手势事件，触发长按手势的最少手指数为1，默认最短长按时间为500毫秒。可配置duration参数控制最短长按时长。

说明

* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 从API version 18开始，部分设备会优先响应系统的双指长按手势，导致应用的双指长按手势不生效。

## 接口

PhonePC/2in1TabletTVWearable

### LongPressGesture

PhonePC/2in1TabletTVWearable

LongPressGesture(value?: { fingers?: number; repeat?: boolean; duration?: number })

创建长按手势对象。继承自[GestureInterface<T>](ts-gesture-common.md#gestureinterfacet11)。

当组件默认支持可拖拽时，如Text、TextInput、TextArea、HyperLink、Image和RichEditor等组件。长按手势与拖拽会出现冲突，事件优先级如下：

当长按触发时间小于500毫秒时，系统优先响应长按事件而非拖拽事件。

当长按触发时间达到或超过500毫秒时，系统优先响应拖拽事件而非长按事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | { fingers?: number; repeat?: boolean; duration?: number } | 否 | 设置长按手势参数。  - fingers：触发长按的最少手指数，最小值为1， 最大值为10。  默认值：1  - repeat：是否连续触发事件回调。true表示连续触发事件回调，false表示不连续触发事件回调。  默认值：false  - duration：触发长按的最短时间，单位为毫秒（ms）。  默认值：500 |

### LongPressGesture15+

PhonePC/2in1TabletTVWearable

LongPressGesture(options?: LongPressGestureHandlerOptions)

创建长按手势对象。与[LongPressGesture](ts-basic-gestures-longpressgesture.md#longpressgesture-1)相比，options参数新增了对isFingerCountLimited参数，表示是否检查触摸屏幕的手指数量。

当组件默认支持可拖拽时，如Text、TextInput、TextArea、HyperLink、Image和RichEditor等组件。长按手势与拖拽会出现冲突，事件优先级如下：

当长按触发时间小于500毫秒时，系统优先响应长按事件而非拖拽事件。

当长按触发时间达到或超过500毫秒时，系统优先响应拖拽事件而非长按事件。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [LongPressGestureHandlerOptions](ts-gesturehandler.md#longpressgesturehandleroptions) | 否 | 长按手势处理器配置参数。 |

## 事件

PhonePC/2in1TabletTVWearable

说明

* 在[GestureEvent](ts-gesture-common.md#gestureevent对象说明)的fingerList元素中，手指索引编号与位置相对应，即fingerList[index]的id为index。对于先按下但未参与当前手势触发的手指，fingerList中对应的位置为空。建议优先使用fingerInfos。
* 长按手势触发后，[GestureEvent](ts-gesture-common.md#gestureevent对象说明)中fingerList和fingerInfo的信息仅在有手指按下时才会更新，手指抬起时不会更新。

### onAction

PhonePC/2in1TabletTVWearable

onAction(event: (event: GestureEvent) => void)

设置长按手势识别成功回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [GestureEvent](ts-gesture-common.md#gestureevent对象说明)) => void | 是 | 长按手势识别成功回调函数。 |

### onActionEnd

PhonePC/2in1TabletTVWearable

onActionEnd(event: (event: GestureEvent) => void)

设置长按手势结束回调。长按手势识别成功后，最后一根手指抬起时触发回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [GestureEvent](ts-gesture-common.md#gestureevent对象说明)) => void | 是 | 长按手势结束回调函数。 |

### onActionCancel

PhonePC/2in1TabletTVWearable

onActionCancel(event: () => void)

设置长按手势取消回调。长按手势识别成功后，接收到触摸取消事件时触发回调。不返回手势事件信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 长按手势取消回调函数。 |

### onActionCancel18+

PhonePC/2in1TabletTVWearable

onActionCancel(event: Callback<GestureEvent>)

设置长按手势取消回调。长按手势识别成功后，接收到触摸取消事件时触发回调。返回手势事件信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Callback<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 长按手势取消回调函数。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例通过LongPressGesture实现了长按手势的识别。从API version 22开始，支持通过[LongPressGestureHandlerOptions](ts-gesturehandler.md#longpressgesturehandleroptions)的allowableMovement属性设置识别手势的最大移动距离。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LongPressGestureExample {
5. @State count: number = 0;

7. build() {
8. Column() {
9. Text('LongPress onAction:' + this.count).fontSize(28)
10. // 单指长按文本触发该手势事件
11. .gesture(
12. // 设置长按手势识别器识别的手势的最大移动距离为200px
13. LongPressGesture({ repeat: true, allowableMovement: 200 })
14. // 由于repeat设置为true，长按动作存在时会连续触发，触发间隔为duration（默认值500ms）
15. .onAction((event: GestureEvent) => {
16. if (event && event.repeat) {
17. this.count++
18. }
19. })
20. // 长按动作一结束触发
21. .onActionEnd((event: GestureEvent) => {
22. this.count = 0
23. })
24. )
25. }
26. .height(200)
27. .width(300)
28. .padding(20)
29. .border({ width: 3 })
30. .margin(30)
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/IrFDUyHlRsSUnFA56dUOJQ/zh-cn_image_0000002589245913.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055134Z&HW-CC-Expire=86400&HW-CC-Sign=ED502AB90DCE5D83F457BCD130EB54F87DC4F867EFA7C673420E393DB617FC75)
