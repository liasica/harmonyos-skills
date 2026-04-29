---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-mouse-key
title: 鼠标事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 基础输入事件 > 鼠标事件
category: harmonyos-references
scraped_at: 2026-04-29T13:51:05+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:cab1346a36d221f24ddd0a2a3a18f8fa389f696b9dce5480608ef429b0dfbdf1
---

在鼠标的单个动作触发多个事件时，事件的顺序是固定的，鼠标事件默认冒泡。

说明

* 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 目前仅支持通过外接鼠标触发。

## onMouse

PhonePC/2in1TabletTVWearable

onMouse(event: (event: MouseEvent) => void): T

当前组件被鼠标按键点击时或者鼠标在组件上悬浮移动时，触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [MouseEvent](ts-universal-mouse-key.md#mouseevent对象说明)) => void | 是 | 返回触发事件时的时间戳、鼠标按键、动作、鼠标位置在整个屏幕上的坐标和相对于当前组件的坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## MouseEvent对象说明

PhonePC/2in1TabletTVWearable

继承于[BaseEvent](ts-gesture-customize-judge.md#baseevent8)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 鼠标位置在事件响应组件为基准的[组件坐标系](../harmonyos-guides/arkui-glossary.md#组件坐标系)中的X坐标。  单位：vp  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| y | number | 否 | 否 | 鼠标位置在事件响应组件为基准的[组件坐标系](../harmonyos-guides/arkui-glossary.md#组件坐标系)中的Y坐标。  单位：vp  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| button | [MouseButton](ts-appendix-enums.md#mousebutton8) | 否 | 否 | 鼠标按键。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| action | [MouseAction](ts-appendix-enums.md#mouseaction8) | 否 | 否 | 鼠标动作。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| stopPropagation | () => void | 否 | 否 | 阻塞[事件冒泡](../harmonyos-guides/arkts-interaction-basic-principles.md#事件冒泡)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| windowX10+ | number | 否 | 否 | 鼠标位置在当前应用窗口坐标系中的X坐标。  单位：vp  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| windowY10+ | number | 否 | 否 | 鼠标位置在当前应用窗口坐标系中的Y坐标。  单位：vp  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| displayX10+ | number | 否 | 否 | 鼠标位置在当前应用屏幕坐标系中的X坐标。  单位：vp  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| displayY10+ | number | 否 | 否 | 鼠标位置在当前应用屏幕坐标系中的Y坐标。  单位：vp  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| screenX(deprecated) | number | 否 | 否 | 鼠标位置在当前应用窗口坐标系中的X坐标。  单位：vp  **说明：** 从API version 8开始支持，从API version 10开始废弃，建议使用windowX替代。 |
| screenY(deprecated) | number | 否 | 否 | 鼠标位置在当前应用窗口坐标系中的Y坐标。  单位：vp  **说明：** 从API version 8开始支持，从API version 10开始废弃，建议使用windowY替代。 |
| rawDeltaX15+ | number | 否 | 是 | 鼠标设备在二维平面X轴的移动增量。其数值为鼠标硬件的原始移动数据，使用物理世界中鼠标移动的距离单位进行表示。上报数值由硬件本身决定，并非屏幕的物理/逻辑像素。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| rawDeltaY15+ | number | 否 | 是 | 鼠标设备在二维平面Y轴的移动增量。其数值为鼠标硬件的原始移动数据，使用物理世界中鼠标移动的距离单位进行表示。上报数值由硬件本身决定，并非屏幕的物理/逻辑像素。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| pressedButtons15+ | MouseButton[] | 否 | 是 | 当前按下的鼠标按键集合。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| globalDisplayX20+ | number | 否 | 是 | 鼠标位置在[全局坐标系](../harmonyos-guides/window-terminology.md#全局坐标系)中的X坐标。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| globalDisplayY20+ | number | 否 | 是 | 鼠标位置在[全局坐标系](../harmonyos-guides/window-terminology.md#全局坐标系)中的Y坐标。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例通过按钮设置了鼠标事件，通过鼠标点击按钮可以触发[onMouse](ts-universal-mouse-key.md#onmouse)事件，获取鼠标事件相关参数。从API version 15开始，可以获取鼠标事件[MouseEvent](ts-universal-mouse-key.md#mouseevent对象说明)的targetDisplayId、rawDeltaX、rawDeltaY、pressedButtons等参数。

鼠标滚轮的处理请参考[轴事件示例](ts-universal-events-axis.md#示例)。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct MouseEventExample {
5. @State hoverText: string = 'no hover';
6. @State mouseText: string = '';
7. @State action: string = '';
8. @State mouseBtn: string = '';
9. @State color: Color = Color.Blue;

11. build() {
12. Column({ space: 20 }) {
13. Button(this.hoverText)
14. .width(180)
15. .height(80)
16. .backgroundColor(this.color)
17. .fontSize(24)
18. .onHover((isHover: boolean, event: HoverEvent) => {
19. // 通过onHover事件动态修改按钮在是否有鼠标悬浮时的文本内容与背景颜色
20. if (isHover) {
21. this.hoverText = 'hover';
22. this.color = Color.Pink;
23. } else {
24. this.hoverText = 'no hover';
25. this.color = Color.Blue;
26. }
27. })
28. Button('onMouse')
29. .width(180).height(80)
30. .fontSize(24)
31. // onMouse监听鼠标事件，解析按键、动作、坐标等信息并拼接展示
32. .onMouse((event: MouseEvent): void => {
33. if (event) {
34. // 判断触发的鼠标按键类型
35. switch (event.button) {
36. case MouseButton.None:
37. this.mouseBtn = 'None';
38. break;
39. case MouseButton.Left:
40. this.mouseBtn = 'Left';
41. break;
42. case MouseButton.Right:
43. this.mouseBtn = 'Right';
44. break;
45. case MouseButton.Back:
46. this.mouseBtn = 'Back';
47. break;
48. case MouseButton.Forward:
49. this.mouseBtn = 'Forward';
50. break;
51. case MouseButton.Middle:
52. this.mouseBtn = 'Middle';
53. break;
54. }
55. // 判断触发的鼠标动作类型
56. switch (event.action) {
57. case MouseAction.Hover:
58. this.action = 'Hover';
59. break;
60. case MouseAction.Press:
61. this.action = 'Press';
62. break;
63. case MouseAction.Move:
64. this.action = 'Move';
65. break;
66. case MouseAction.Release:
67. this.action = 'Release';
68. break;
69. }
70. // 拼接鼠标事件全量信息并展示
71. this.mouseText = 'onMouse:\nButton = ' + this.mouseBtn +
72. '\nAction = ' + this.action + '\nXY=(' + event.x + ',' + event.y + ')' +
73. '\nwindowXY=(' + event.windowX + ',' + event.windowY + ')' +
74. '\ntargetDisplayId = ' + event.targetDisplayId +
75. '\nrawDeltaX = ' + event.rawDeltaX +
76. '\nrawDeltaY = ' + event.rawDeltaY +
77. '\nlength = ' + event.pressedButtons?.length;
78. }
79. })
80. Text(this.mouseText)
81. }.padding({ top: 30 }).width('100%')
82. }
83. }
```

示意图：

鼠标点击时：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/JNvN6TD5SpCRSEolGo0SXw/zh-cn_image_0000002558606326.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055103Z&HW-CC-Expire=86400&HW-CC-Sign=C7FF565AB843ED4B4E9A47BD4DCDDF1D807FF4A3BF64BA16B461655B5B7017A2)
