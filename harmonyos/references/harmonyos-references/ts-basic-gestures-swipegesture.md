---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-swipegesture
title: SwipeGesture
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 手势处理 > 基础手势 > SwipeGesture
category: harmonyos-references
scraped_at: 2026-04-28T08:01:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:cdde603e15a5ace2373d50ea39171568be7123516d75e84dbbabb27199dbeaff
---

用于触发快滑手势，滑动速度需大于速度阈值，默认最小速度为100vp/s。

说明

从API version 8开始支持。后续版本如有新增内容，将采用上角标单独标记该内容的起始版本。

## 接口

PhonePC/2in1TabletTVWearable

### SwipeGesture

PhonePC/2in1TabletTVWearable

SwipeGesture(value?: { fingers?: number; direction?: SwipeDirection; speed?: number })

继承自[GestureInterface<T>](ts-gesture-common.md#gestureinterfacet11)，设置快滑手势事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | { fingers?: number; direction?: SwipeDirection; speed?: number } | 否 | 设置快滑事件参数。  - fingers：触发快滑的最少手指数。  默认值：1  取值范围：[1, 10]  - direction：触发快滑手势的滑动方向。  默认值：SwipeDirection.All  - speed：识别快滑的最小速度。  默认值：100VP/s  取值范围：(0, +∞)  **说明：**  当滑动速度的值小于等于0时，会被转化为默认值。 |

### SwipeGesture15+

PhonePC/2in1TabletTVWearable

SwipeGesture(options?: SwipeGestureHandlerOptions)

设置快滑手势事件。与[SwipeGesture](ts-basic-gestures-swipegesture.md#swipegesture-1)相比，options参数新增了isFingerCountLimited，表示是否检查触摸屏幕的手指数量。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SwipeGestureHandlerOptions](ts-gesturehandler.md#swipegesturehandleroptions) | 否 | 快滑事件处理器配置参数。 |

## SwipeDirection枚举说明

PhonePC/2in1TabletTVWearable

定义滑动手势的触发方向。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| All | - | 所有方向。 |
| Horizontal | - | 水平方向，手指滑动方向与x轴夹角小于45度时触发。 |
| Vertical | - | 竖直方向，手指滑动方向与y轴夹角小于45度时触发。 |
| None | - | 任何方向均不可触发。 |

## 事件

PhonePC/2in1TabletTVWearable

说明

在[GestureEvent](ts-gesture-common.md#gestureevent对象说明)的fingerList元素中，手指索引编号与位置相对应，即fingerList[index]的id为index。对于先按下但未参与当前手势触发的手指，fingerList中对应的位置为空。建议开发者优先使用fingerInfos。

### onAction

PhonePC/2in1TabletTVWearable

onAction(event: (event: GestureEvent) => void)

Swipe手势识别成功时触发回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [GestureEvent](ts-gesture-common.md#gestureevent对象说明)) => void | 是 | 手势事件回调函数。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例展示了如何实现快滑手势的识别。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SwipeGestureExample {
5. @State rotateAngle: number = 0;
6. @State speed: number = 1;

8. build() {
9. Column() {
10. Column() {
11. Text("SwipeGesture speed\n" + this.speed)
12. Text("SwipeGesture angle\n" + this.rotateAngle)
13. }
14. .border({ width: 3 })
15. .width(300)
16. .height(200)
17. .margin(100)
18. .rotate({ angle: this.rotateAngle })
19. // 单指竖直方向快滑时触发该事件
20. .gesture(
21. SwipeGesture({ direction: SwipeDirection.Vertical })
22. .onAction((event: GestureEvent) => {
23. if (event) {
24. this.speed = event.speed
25. this.rotateAngle = event.angle
26. }
27. })
28. )
29. }.width('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/NqTcYdDWThyok0cyjHIzgA/zh-cn_image_0000002583479585.png?HW-CC-KV=V1&HW-CC-Date=20260428T000121Z&HW-CC-Expire=86400&HW-CC-Sign=FBBB0FBA929633B66C1B87FDBA17B8AA49B0C50DA429B6B320F9D1C1162601E0)
