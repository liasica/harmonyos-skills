---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-click
title: 点击事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 交互响应事件 > 点击事件
category: harmonyos-references
scraped_at: 2026-04-29T13:51:09+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:9f3e83c2ea4f92d4c879abe2e7fc311c919f4fec84af6c0a38733f520bbd3840
---

组件被点击时触发的事件。

说明

* 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 点击事件遵循[触摸事件](ts-universal-events-touch.md)分发流程，触摸事件支持屏蔽、透传等自定义行为。
* 事件分发可参考[事件交互流程](../harmonyos-guides/arkts-interaction-basic-principles.md#事件交互流程)，手势事件处理流程可参考[多层级手势事件](../harmonyos-guides/arkts-gesture-events-multi-level-gesture.md)。
* 当该点击事件由键盘或者手柄触发时，不会触发[onGestureJudgeBegin](ts-gesture-customize-judge.md#ongesturejudgebegin)，[onGestureRecognizerJudgeBegin](ts-gesture-blocking-enhancement.md#ongesturerecognizerjudgebegin)和[willClick](arkts-apis-uicontext-uiobserver.md#onwillclick12)的回调。

## onClick12+

PhonePC/2in1TabletTVWearable

onClick(event: Callback<ClickEvent>, distanceThreshold: number): T

点击动作触发该回调。

当触发点击事件的设备类型为键盘或手柄时，事件的[SourceTool](ts-gesture-settings.md#sourcetool枚举说明9)值为Unknown，事件的[SourceType](ts-gesture-settings.md#sourcetype枚举说明8)值为KEY，JOYSTICK。

新增distanceThreshold参数，设置点击手势移动阈值。手指移动超出阈值时，点击手势识别失败。

对于无手指移动距离限制的点击场景，建议使用原有接口。若需限制点击时手指移动范围，建议使用该接口。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

说明

* 从API version 12开始，在使用卡片能力时，存在以下限制：

  1. 如果手指按下的持续时间超过800ms，不能触发点击事件。
  2. 如果手指按下后移动位移超过20px，不能触发点击事件。
* 该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Callback<[ClickEvent](ts-universal-events-click.md#clickevent)> | 是 | 点击事件的回调函数。 |
| distanceThreshold | number | 是 | 点击事件移动阈值。当设置的值小于等于0时，会被转化为默认值。  默认值：2^31-1  单位：vp  **说明：**  当手指的移动距离超出开发者预设的移动阈值时，点击识别失败。如果初始化为默认阈值时，手指移动超过组件热区范围，点击识别失败。 |

说明

如果执行滑动操作，但滑动距离未超过点击事件移动阈值，并且抬手时手指在组件热区范围内，也会触发点击事件。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## onClick

PhonePC/2in1TabletTVWearable

onClick(event: (event: ClickEvent) => void): T

点击动作触发该回调。

触发点击事件的设备类型为键盘或手柄时，事件的SourceTool值为Unknown，事件的[SourceType](ts-gesture-settings.md#sourcetype枚举说明8)值为KEY，JOYSTICK。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

说明

从API version 9开始，使用卡片能力时存在以下限制：

1. 如果手指按下的持续时间超过800ms，不能触发点击事件。
2. 如果手指按下后移动位移超过20px，不能触发点击事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [ClickEvent](ts-universal-events-click.md#clickevent)) => void | 是 | 点击事件的回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## ClickEvent

PhonePC/2in1TabletTVWearable

继承于[BaseEvent](ts-gesture-customize-judge.md#baseevent8)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 点击位置在被点击元素为基准的[组件坐标系](../harmonyos-guides/arkui-glossary.md#组件坐标系)中的X坐标。onClick的[distanceThreshold](ts-universal-events-click.md#onclick12)设置后，点击位置为抬手点。触发事件的是键盘或手柄时，点击位置为被点击元素的中心点。  单位：vp  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| y | number | 否 | 否 | 点击位置在被点击元素为基准的[组件坐标系](../harmonyos-guides/arkui-glossary.md#组件坐标系)中的Y坐标。onClick的distanceThreshold设置后，点击位置为抬手点。触发事件的是键盘或手柄时，点击位置为被点击元素的中心点。  单位：vp  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| windowX10+ | number | 否 | 否 | 点击位置在当前应用窗口坐标系中的X坐标。onClick的distanceThreshold设置后，点击位置为抬手点。  单位：vp  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| windowY10+ | number | 否 | 否 | 点击位置在当前应用窗口坐标系中的Y坐标。onClick的distanceThreshold设置后，点击位置为抬手点。  单位：vp  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| displayX10+ | number | 否 | 否 | 点击位置在当前应用屏幕坐标系中的X坐标。  单位：vp  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| displayY10+ | number | 否 | 否 | 点击位置在当前应用屏幕坐标系中的Y坐标。  单位：vp  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| screenX(deprecated) | number | 否 | 否 | 点击位置在当前应用窗口坐标系中的X坐标。  单位：vp  **说明：** 从API version 7开始支持，从API version 10开始废弃，建议使用windowX替代。 |
| screenY(deprecated) | number | 否 | 否 | 点击位置在当前应用窗口坐标系中的Y坐标。  单位：vp  **说明：** 从API version 7开始支持，从API version 10开始废弃，建议使用windowY替代。 |
| preventDefault12+ | () => void | 否 | 否 | 阻止默认事件。  **说明：** 该接口仅支持部分组件使用，当前支持组件：RichEditor、Hyperlink，不支持的组件使用时会抛出异常。暂不支持异步调用和提供Modifier接口。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| hand15+ | [InteractionHand](ts-appendix-enums.md#interactionhand15) | 否 | 是 | 表示事件是由左手点击还是右手点击触发。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| globalDisplayX20+ | number | 否 | 是 | 点击位置在[全局坐标系](../harmonyos-guides/window-terminology.md#全局坐标系)中的X坐标。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| globalDisplayY20+ | number | 否 | 是 | 点击位置在[全局坐标系](../harmonyos-guides/window-terminology.md#全局坐标系)中的Y坐标。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

**错误码：**

以下错误码的详细介绍请参见[交互事件错误码](errorcode-event.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100017 | Component does not support prevent function. |

## EventTarget8+

PhonePC/2in1TabletTVWearable

[BaseEvent](ts-gesture-customize-judge.md#baseevent8)中参数target的类型。

触发事件的元素对象的显示区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| area | [Area](ts-types.md#area8) | 否 | 否 | 目标元素的区域信息。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| id15+ | string | 否 | 是 | 开发者设置的节点[id](ts-universal-attributes-component-id.md#id)。默认值：undefined  **卡片能力：** 从API version 15开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例通过按钮设置点击事件，点击按钮可获取点击事件的相关参数。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ClickExample {
5. @State text: string = '';

7. build() {
8. Column() {
9. Row({ space: 20 }) {
10. Button('Click1').width(100).height(40).id('click1')
11. .onClick((event?: ClickEvent) => {
12. if (event) {
13. this.text =
14. `Click Point:\n  windowX:${event.windowX}\n  windowY:${event.windowY}\n  x:${event.x}\n  y:${event.y}\n target:\n  component globalPos:(${event.target.area.globalPosition.x},${event.target.area.globalPosition.y})\n  width:${event.target.area.width}\n  height:${event.target.area.height}\n  id:${event.target.id}\ntargetDisplayId:${event.targetDisplayId}\ntimestamp${event.timestamp}`
15. }
16. }, 20)
17. Button('Click2').width(200).height(50).id('click2')
18. .onClick((event?: ClickEvent) => {
19. if (event) {
20. this.text =
21. `Click Point:\n  windowX:${event.windowX}\n  windowY:${event.windowY}\n  x:${event.x}\n  y:${event.y}\n target:\n  component globalPos:(${event.target.area.globalPosition.x},${event.target.area.globalPosition.y})\n  width:${event.target.area.width}\n  height:${event.target.area.height}\n  id:${event.target.id}\ntargetDisplayId:${event.targetDisplayId}\ntimestamp${event.timestamp}`
22. }
23. }, 20)
24. }.margin(20)

26. Text(this.text).margin(15)
27. }.width('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/fCInChibTTiFn5XjhI4rtQ/zh-cn_image_0000002589245797.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055107Z&HW-CC-Expire=86400&HW-CC-Sign=FAD2E750EC64B50D31F7189CC4B1C711712249BEFBFCDA030DA6D255E8A7C754)
