---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-hover
title: 悬浮事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 交互响应事件 > 悬浮事件
category: harmonyos-references
scraped_at: 2026-04-29T13:51:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dc64ee035c8c837f3f7f6e46eef8ac9ad588e970c132992f62eee68a32d390d2
---

光标滑动或手写笔在屏幕上悬浮移动扫过组件时触发。

说明

* 从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 目前支持通过外接鼠标以及触控板触发。部分手写笔（当前在华为智慧屏MateTV、MateTV Pro中使用灵犀手写笔时无法响应悬浮事件）不支持悬浮事件，具体取决于硬件能力。

## onHover

PhonePC/2in1TabletTVWearable

onHover(event: (isHover: boolean, event: HoverEvent) => void): T

鼠标或手写笔进入或退出组件时，触发hover事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (isHover: boolean, event: [HoverEvent](ts-universal-events-hover.md#hoverevent10对象说明)) => void | 是 | 鼠标的状态信息。  event表示设置阻塞事件冒泡属性，并获取鼠标或手写笔悬浮的位置坐标，从API version 11开始支持。  isHover表示鼠标或手写笔是否悬浮在组件上，进入时为true， 离开时为false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## onHoverMove15+

PhonePC/2in1TabletTVWearable

onHoverMove(event: Callback<HoverEvent>): T

手写笔悬浮于组件上方时触发悬浮移动事件。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Callback<[HoverEvent](ts-universal-events-hover.md#hoverevent10对象说明)> | 是 | 设置阻塞事件冒泡属性，并获取手写笔悬浮的位置坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## HoverEvent10+对象说明

PhonePC/2in1TabletTVWearable

继承于[BaseEvent](ts-gesture-customize-judge.md#baseevent8)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x15+ | number | 否 | 是 | 鼠标光标或手写笔位置在当前组件为基准的[组件坐标系](../harmonyos-guides/arkui-glossary.md#组件坐标系)中的X坐标。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| y15+ | number | 否 | 是 | 鼠标光标或手写笔位置在当前组件为基准的[组件坐标系](../harmonyos-guides/arkui-glossary.md#组件坐标系)中的Y坐标。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| windowX15+ | number | 否 | 是 | 鼠标光标或手写笔位置在当前应用窗口坐标系中的X坐标。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| windowY15+ | number | 否 | 是 | 鼠标光标或手写笔位置在当前应用窗口坐标系中的Y坐标。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| displayX15+ | number | 否 | 是 | 鼠标光标或手写笔位置在当前应用屏幕坐标系中的X坐标。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| displayY15+ | number | 否 | 是 | 鼠标光标或手写笔位置在当前应用屏幕坐标系中的Y坐标。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| stopPropagation | () => void | 否 | 否 | 阻塞[事件冒泡](../harmonyos-guides/arkts-interaction-basic-principles.md#事件冒泡)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| globalDisplayX20+ | number | 否 | 是 | 鼠标光标或手写笔位置在[全局坐标系](../harmonyos-guides/window-terminology.md#全局坐标系)中的X坐标。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| globalDisplayY20+ | number | 否 | 是 | 鼠标光标或手写笔位置在[全局坐标系](../harmonyos-guides/window-terminology.md#全局坐标系)中的Y坐标。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（使用onHover）

该示例通过按钮设置了悬浮事件[onHover](ts-universal-events-hover.md#onhover)，鼠标悬浮可触发该事件修改按钮颜色。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct HoverEventExample {
5. @State hoverText: string = 'no hover';
6. @State color: Color = Color.Blue;

8. build() {
9. Column({ space: 20 }) {
10. Button(this.hoverText, { type: ButtonType.Capsule })
11. .width(180).height(80)
12. .backgroundColor(this.color)
13. .onHover((isHover: boolean, event: HoverEvent) => {
14. // 通过onHover事件动态修改按钮在是否有鼠标或手写笔悬浮时的文本内容与背景颜色
15. // 通过event.sourceTool区分设备是鼠标还是手写笔
16. if (isHover) {
17. if (event.sourceTool == SourceTool.Pen) {
18. this.hoverText = 'pen hover';
19. this.color = Color.Pink;
20. } else if (event.sourceTool == SourceTool.MOUSE) {
21. this.hoverText = 'mouse hover';
22. this.color = Color.Red;
23. }
24. } else {
25. this.hoverText = 'no hover';
26. this.color = Color.Blue;
27. }
28. })
29. }.padding({ top: 30 }).width('100%')
30. }
31. }
```

示意图：

未悬浮时的文本内容与背景颜色：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/38inCwr4TjGMWh4b0-PtMA/zh-cn_image_0000002589245801.png?HW-CC-KV=V1&HW-CC-Date=20260429T055107Z&HW-CC-Expire=86400&HW-CC-Sign=BF9C7C2D2846392AAF8B781FB04EC8FCC01BB0D72EE1DBF57A438FEB5E997B14)

手写笔悬浮时改变文本内容与背景颜色：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/qpTPVpKrQsqvh0ZFootY3A/zh-cn_image_0000002558765992.png?HW-CC-KV=V1&HW-CC-Date=20260429T055107Z&HW-CC-Expire=86400&HW-CC-Sign=E704EDDC795A16C92EC2A2E979B267E0CA40205A52315AE98F0EF3CD14E713E1)

### 示例2（使用onHoverMove）

从API version 15开始，该示例设置了按钮的[onHoverMove](ts-universal-events-hover.md#onhovermove15)事件。当手写笔悬浮在按钮时，UI界面会显示当前手写笔悬浮状的位置。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct OnHoverMoveEventExample {
5. @State hoverMoveText: string = '';

7. build() {
8. Column({ space: 20 }) {
9. Button('onHoverMove', { type: ButtonType.Capsule })
10. .width(180).height(80)
11. .onHoverMove((event: HoverEvent) => {
12. this.hoverMoveText = 'onHoverMove:\nXY = (' + event.x + ', ' + event.y + ')' +
13. '\nwindowXY = (' + event.windowX + ', ' + event.windowY + ')' +
14. '\ndisplayXY = (' + event.displayX + ', ' + event.displayY + ')';
15. })

17. Text(this.hoverMoveText)
18. }.padding({ top: 30 }).width('100%')
19. }
20. }
```

示意图：

手写笔悬浮在Button组件上时，UI不断刷新笔尖的位置信息：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/RWItx-vBRy-byt7hf4oHhg/zh-cn_image_0000002558606334.png?HW-CC-KV=V1&HW-CC-Date=20260429T055107Z&HW-CC-Expire=86400&HW-CC-Sign=B502D0A5FE84FD609BD8A00514F16C72E458CC86ACB4A2A9B7F5EA365C8178ED)
