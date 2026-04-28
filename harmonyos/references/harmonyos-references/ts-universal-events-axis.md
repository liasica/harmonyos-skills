---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-axis
title: 轴事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 基础输入事件 > 轴事件
category: harmonyos-references
scraped_at: 2026-04-28T08:00:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5c7968f07e169f5276cfa88216d3222dee173ea454c9f0ba44d23a1fa88378af
---

轴事件是指当鼠标或触控板等带指针输入设备的指针位于组件区域内时，因操作滚轮或触控板双指沿特定方向（轴）滑动时触发的事件。“轴”指二维坐标系中的方向，分为水平（X轴）和垂直（Y轴）。

说明

本模块首批接口从API version 17开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## onAxisEvent

PhonePC/2in1TabletTVWearable

onAxisEvent(event: Callback<AxisEvent>): T

鼠标滚轮滚动或触控板双指轻触滑动、双指捏合时触发该回调。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Callback<[AxisEvent](ts-universal-events-axis.md#axisevent)> | 是 | 获得[AxisEvent](ts-universal-events-axis.md#axisevent)对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## AxisEvent

PhonePC/2in1TabletTVWearable

轴事件的对象说明，继承于[BaseEvent](ts-gesture-customize-judge.md#baseevent8)。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| action | [AxisAction](ts-appendix-enums.md#axisaction17) | 否 | 否 | 轴事件的动作类型。  **元服务API：** 从API version 17开始，该接口支持在元服务中使用。 |
| x | number | 否 | 否 | 鼠标光标在被点击元素为基准的[组件坐标系](../harmonyos-guides/arkui-glossary.md#组件坐标系)中的X坐标。  单位：vp  **元服务API：** 从API version 17开始，该接口支持在元服务中使用。 |
| y | number | 否 | 否 | 鼠标光标在被点击元素为基准的[组件坐标系](../harmonyos-guides/arkui-glossary.md#组件坐标系)中的Y坐标。  单位：vp  **元服务API：** 从API version 17开始，该接口支持在元服务中使用。 |
| windowX | number | 否 | 否 | 鼠标光标在当前应用窗口坐标系中的X坐标。  单位：vp  **元服务API：** 从API version 17开始，该接口支持在元服务中使用。 |
| windowY | number | 否 | 否 | 鼠标光标在当前应用窗口坐标系中的Y坐标。  单位：vp  **元服务API：** 从API version 17开始，该接口支持在元服务中使用。 |
| displayX | number | 否 | 否 | 鼠标光标在当前应用屏幕坐标系中的X坐标。  单位：vp  **元服务API：** 从API version 17开始，该接口支持在元服务中使用。 |
| displayY | number | 否 | 否 | 鼠标光标在当前应用屏幕坐标系中的Y坐标。  单位：vp  **元服务API：** 从API version 17开始，该接口支持在元服务中使用。 |
| scrollStep | number | 否 | 是 | 鼠标轴滚动步长配置。  **说明：** 仅支持鼠标滚轮，取值范围：[0~65535]  **元服务API：** 从API version 17开始，该接口支持在元服务中使用。 |
| propagation | Callback<void> | 否 | 否 | 激活[事件冒泡](../harmonyos-guides/arkts-interaction-basic-principles.md#事件冒泡)。  **元服务API：** 从API version 17开始，该接口支持在元服务中使用。 |
| globalDisplayX20+ | number | 否 | 是 | 鼠标光标在[全局坐标系](../harmonyos-guides/window-terminology.md#全局坐标系)中的X坐标。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| globalDisplayY20+ | number | 否 | 是 | 鼠标光标在[全局坐标系](../harmonyos-guides/window-terminology.md#全局坐标系)中的Y坐标。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

### getHorizontalAxisValue

PhonePC/2in1TabletTVWearable

getHorizontalAxisValue(): number

获取此次轴事件的水平轴值。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 水平轴值。  单位：vp |

### getVerticalAxisValue

PhonePC/2in1TabletTVWearable

getVerticalAxisValue(): number

获取此次轴事件的垂直轴值。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 垂直轴值。  单位：vp |

### getPinchAxisScaleValue21+

PhonePC/2in1TabletTVWearable

getPinchAxisScaleValue(): number

返回此次轴事件双指缩放的比例。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 双指缩放比例。  **说明：** 缩放比例指的是触控板双指缩放事件触发过程中双指当前的距离与双指最初按下时的距离的比值。  默认值：0  取值范围：[0, +∞) |

### hasAxis22+

PhonePC/2in1TabletTVWearable

hasAxis(axisType: AxisType): boolean

检测此轴事件是否包含指定的轴类型。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| axisType | [AxisType](ts-appendix-enums.md#axistype22) | 是 | 轴事件的轴类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 此轴事件是否包含指定的轴类型。  true：包含指定的轴类型；false：不包含指定的轴类型。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例中，对按钮设置轴事件，通过滚动鼠标滚轮可获取轴事件的相关参数。从API version 21开始，该示例通过[axisPinch](ts-gesture-customize-judge.md#属性)和[getPinchAxisScaleValue](ts-universal-events-axis.md#getpinchaxisscalevalue21)获取双指缩放比例；从API version 22开始，该示例通过[hasAxis](ts-universal-events-axis.md#hasaxis22)判断轴事件是否包含指定的轴类型。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct AxisEventExample {
5. @State text: string = ''

7. build() {
8. Column() {
9. Row({ space: 20 }) {
10. Button('AxisEvent').width(100).height(40)
11. .onAxisEvent((event?: AxisEvent) => {
12. if (event) {
13. this.text =
14. 'AxisEvent:' + '\n  action:' + event.action + '\n  displayX:' + event.displayX + '\n  displayY:' +
15. event.displayY + '\n  windowX:' + event.windowX + '\n  windowY:' + event.windowY + '\n  x:' + event.x +
16. '\n  y:' + event.y + '\n VerticalAxisValue:' + event.getVerticalAxisValue() +
17. '\n HorizontalAxisValue:' + event.getHorizontalAxisValue() + '\n axisPinch:' + event.axisPinch +
18. '\n PinchAxisScaleValue:' + event.getPinchAxisScaleValue() +
19. '\n HasAxis:' + event.hasAxis(AxisType.VERTICAL_AXIS);
20. }
21. })
22. }.margin(20)

24. Text(this.text).margin(15)
25. }.width('100%')
26. }
27. }
```

鼠标滚轮滚动时：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/KsjQ0Qg6R0GE6XsLF-sr4A/zh-cn_image_0000002552799814.png?HW-CC-KV=V1&HW-CC-Date=20260428T000052Z&HW-CC-Expire=86400&HW-CC-Sign=BA0A57FD14E6346DB876A0BB9137B755257FE7C741619BD93E463E74A5496FB1)
