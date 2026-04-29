---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-rotationgesture
title: RotationGesture
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 手势处理 > 基础手势 > RotationGesture
category: harmonyos-references
scraped_at: 2026-04-29T13:51:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b16aeb38a2a0c1313e3d701d1e0100f5d130d9177c35d98f92bb5f01feda2e65
---

用于触发旋转手势，最少需要2指，最多5指，最小改变度数为1度。该手势不支持通过触控板双指旋转操作触发。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 接口

PhonePC/2in1TabletTVWearable

### RotationGesture

PhonePC/2in1TabletTVWearable

RotationGesture(value?: { fingers?: number; angle?: number })

继承自[GestureInterface<T>](ts-gesture-common.md#gestureinterfacet11)，设置旋转手势事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | { fingers?: number; angle?: number } | 否 | 设置旋转手势事件参数。  - fingers：触发旋转手势所需的最少手指数， 最小为2指，最大为5指。  默认值：2  取值范围：[2, 5]。当设置的值小于2或大于5时，会被转化为默认值。  触发手势时手指数量可以多于fingers参数值，但仅最先落下的两指参与手势计算。  - angle：触发旋转手势所需的最小角度变化，单位为deg。  默认值：1  **说明：**  当改变度数的值小于等于0或大于360时，会被转化为默认值。 |

### RotationGesture15+

PhonePC/2in1TabletTVWearable

RotationGesture(options?: RotationGestureHandlerOptions)

设置旋转手势事件。与[RotationGesture](ts-basic-gestures-rotationgesture.md#rotationgesture-1)相比，options参数新增了isFingerCountLimited参数，表示是否检查触摸屏幕的手指数量。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RotationGestureHandlerOptions](ts-gesturehandler.md#rotationgesturehandleroptions) | 否 | 旋转手势处理器配置参数。 |

## 事件

PhonePC/2in1TabletTVWearable

说明

在[GestureEvent](ts-gesture-common.md#gestureevent对象说明)的fingerList元素中，手指索引编号与位置相对应，即fingerList[index]的id为index。对于先按下但未参与当前手势触发的手指，fingerList中对应的位置为空。建议优先使用fingerInfos。

### onActionStart

PhonePC/2in1TabletTVWearable

onActionStart(event: (event: GestureEvent) => void)

Rotation手势识别成功后触发的回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [GestureEvent](ts-gesture-common.md#gestureevent对象说明)) => void | 是 | 手势事件回调函数。 |

### onActionUpdate

PhonePC/2in1TabletTVWearable

onActionUpdate(event: (event: GestureEvent) => void)

Rotation手势移动过程中触发的回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [GestureEvent](ts-gesture-common.md#gestureevent对象说明)) => void | 是 | 手势事件回调函数。 |

### onActionEnd

PhonePC/2in1TabletTVWearable

onActionEnd(event: (event: GestureEvent) => void)

Rotation手势识别成功，当抬起最后一根满足手势触发条件的手指后触发的回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [GestureEvent](ts-gesture-common.md#gestureevent对象说明)) => void | 是 | 手势事件回调函数。 |

### onActionCancel

PhonePC/2in1TabletTVWearable

onActionCancel(event: () => void)

Rotation手势识别成功，接收到触摸取消事件触发的回调。该回调不返回手势事件信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 手势事件回调函数。 |

### onActionCancel18+

PhonePC/2in1TabletTVWearable

onActionCancel(event: Callback<GestureEvent>)

Rotation手势识别成功，接收到触摸取消事件触发的回调。与[onActionCancel](ts-basic-gestures-rotationgesture.md#onactioncancel)相比，该回调返回手势事件信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Callback<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 手势事件回调函数。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例通过配置RotationGesture实现了双指旋转手势的识别。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RotationGestureExample {
5. @State angle: number = 0;
6. @State rotateValue: number = 0;

8. build() {
9. Column() {
10. Column() {
11. Text('RotationGesture angle:' + this.angle)
12. }
13. .height(200)
14. .width(300)
15. .padding(20)
16. .border({ width: 3 })
17. .margin(80)
18. .rotate({ angle: this.angle })
19. // 双指旋转触发该手势事件
20. .gesture(
21. RotationGesture()
22. .onActionStart((event: GestureEvent) => {
23. console.info('Rotation start')
24. })
25. .onActionUpdate((event: GestureEvent) => {
26. if (event) {
27. this.angle = this.rotateValue + event.angle
28. }
29. })
30. .onActionEnd((event: GestureEvent) => {
31. this.rotateValue = this.angle
32. console.info('Rotation end')
33. })
34. )
35. }.width('100%')
36. }
37. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/dRnoNfuFRaqq_iKb9DMWzA/zh-cn_image_0000002558766106.png?HW-CC-KV=V1&HW-CC-Date=20260429T055134Z&HW-CC-Expire=86400&HW-CC-Sign=66025C2D84967C80E10F4D30F88144E09628C1F5F7DDF84F0E07A4B491DFD72D)
