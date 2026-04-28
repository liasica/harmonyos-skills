---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-accessibility-hover-event
title: 无障碍悬浮事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 无障碍相关 > 无障碍悬浮事件
category: harmonyos-references
scraped_at: 2026-04-28T08:00:57+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0f6e78c9956491e74f69eaa3af2e182f4a515ade6888761fddfb9b6af5c32d80
---

在开启无障碍模式后，Touch事件会转换为无障碍悬浮事件。

说明

* 从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 目前仅支持通过开启无障碍模式触发。

## onAccessibilityHover

PhonePC/2in1TabletTVWearable

onAccessibilityHover(callback: AccessibilityCallback): T

开启无障碍模式后，单指触摸绑定该回调的组件时触发该回调。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AccessibilityCallback](ts-universal-accessibility-hover-event.md#accessibilitycallback) | 是 | 提供开启无障碍模式后的无障碍悬浮回调事件，当开启无障碍模式后，单指触摸绑定该回调的组件时触发该回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## AccessibilityCallback

PhonePC/2in1TabletTVWearable

type AccessibilityCallback = (isHover: boolean, event: AccessibilityHoverEvent) => void

提供开启无障碍模式后的无障碍悬浮回调事件类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isHover | boolean | 是 | 表示开启无障碍模式后，手指在组件上触发由Touch事件转换成的无障碍悬浮事件，手指进入时为true，退出时为false。 |
| event | [AccessibilityHoverEvent](ts-universal-accessibility-hover-event.md#accessibilityhoverevent对象说明) | 是 | 获得AccessibilityHoverEvent对象。 |

## AccessibilityHoverEvent对象说明

PhonePC/2in1TabletTVWearable

继承于[BaseEvent](ts-gesture-customize-judge.md#baseevent8)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [AccessibilityHoverType](ts-appendix-enums.md#accessibilityhovertype12) | 否 | 否 | 无障碍悬浮动作。 |
| x | number | 否 | 否 | 手指位置相对于当前组件左上角的x轴坐标。  单位：vp |
| y | number | 否 | 否 | 手指位置相对于当前组件左上角的y轴坐标。  单位：vp |
| windowX | number | 否 | 否 | 手指位置相对于应用窗口左上角的x轴坐标。  单位：vp |
| windowY | number | 否 | 否 | 手指位置相对于应用窗口左上角的y轴坐标。  单位：vp |
| displayX | number | 否 | 否 | 手指位置相对于应用屏幕左上角的x轴坐标。  单位：vp |
| displayY | number | 否 | 否 | 手指位置相对于应用屏幕左上角的y轴坐标。  单位：vp |
| globalDisplayX20+ | number | 否 | 是 | 手指位置相对于全局屏幕的左上角的X坐标。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| globalDisplayY20+ | number | 否 | 是 | 手指位置相对于全局屏幕的左上角的Y坐标。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## onAccessibilityHoverTransparent20+

PhonePC/2in1TabletTVWearable

onAccessibilityHoverTransparent(callback: AccessibilityTransparentCallback): T

在开启朗读类辅助应用以及手指触摸在组件区域的前提下，当该组件及子组件全部没有被无障碍悬浮识别为可聚焦时，会触发该回调，并且返回无障碍悬浮事件。仅支持手指触摸。不支持如下组件在触摸位置中的场景，包括[UIExtension](js-apis-arkui-uiextension.md)、[Web](arkts-basic-components-web.md)、[XComponent](ts-basic-components-xcomponent.md)与第三方UI框架对接。在上述场景下，该回调接口无法生效。

组件无法被无障碍悬浮识别为可聚焦的主要原因包括，组件的无障碍重要性[accessibilityLevel](ts-universal-attributes-accessibility.md#accessibilitylevel)为"no"或者"no-hide-descendants"；组件无文本且未配置无障碍文本[accessibilityText](ts-universal-attributes-accessibility.md#accessibilitytext)，同时不支持点击或长按操作。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AccessibilityTransparentCallback](ts-universal-accessibility-hover-event.md#accessibilitytransparentcallback20) | 是 | 提供开启无障碍模式后未能响应的用户输入的触摸事件，当开启无障碍模式后，单指触摸未能响应无障碍悬浮事件位置时触发该回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## AccessibilityTransparentCallback20+

PhonePC/2in1TabletTVWearable

type AccessibilityTransparentCallback = (event: TouchEvent) => void

提供开启无障碍模式后未能响应的用户输入的触摸事件。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [TouchEvent](ts-universal-events-touch.md#touchevent对象说明) | 是 | 原始touch事件。  **说明：** TouchEvent对象的触摸事件的类型[TouchType](ts-appendix-enums.md#touchtype)为四种无障碍悬浮事件类型中的一种，四种无障碍悬浮事件类型为HOVER\_ENTER、HOVER\_MOVE、HOVER\_EXIT和HOVER\_CANCEL。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1 (使用onAccessibilityHover事件)

该示例主要演示通过使用onAccessibilityHover事件，对无障碍模式下的按钮进行设置。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct OnAccessibilityHoverEventExample {
5. @State hoverText: string = 'no hover';
6. @State color: Color = Color.Blue;

8. build() {
9. Column({ space: 20 }) {
10. Button(this.hoverText)
11. .width(180).height(80)
12. .backgroundColor(this.color)
13. .onAccessibilityHover((isHover: boolean, event: AccessibilityHoverEvent) => {
14. // 通过onAccessibilityHover事件动态修改按钮在是否有鼠标悬浮时的文本内容与背景颜色
15. if (isHover) {
16. this.hoverText = 'hover';
17. this.color = Color.Pink;
18. } else {
19. this.hoverText = 'no hover';
20. this.color = Color.Blue;
21. }
22. })
23. }.padding({ top: 30 }).width('100%')
24. }
25. }
```

### 示例2 (捕获无法无障碍聚焦的组件的触摸事件)

该示例代码在无障碍模式下通过onAccessibilityHoverTransparent接口捕获无法无障碍聚焦的组件的触摸事件，最后再将事件信息显示在组件下方的文本中。

从API version 20开始，新增了[onAccessibilityHoverTransparent](ts-universal-accessibility-hover-event.md#onaccessibilityhovertransparent20)入参类型为AccessibilityTransparentCallback的接口。

```
1. @Entry
2. @Component
3. struct TestExample {
4. @State text: string = '';
5. @State eventType: string = '';

7. build() {
8. Column({ space: 50 }) {
9. Column() {
10. Button("Test Button")
11. .accessibilityLevel("no")
12. }.margin({ top: 20 })

14. Text(this.text)
15. }
16. .width('100%')
17. .height('100%')
18. .onAccessibilityHoverTransparent((event?: TouchEvent) => {
19. if (event) {
20. // 手指按下触发
21. if (event.type === TouchType.HOVER_ENTER) {
22. this.eventType = 'HOVER_ENTER';
23. }
24. // 触摸移动时触发
25. if (event.type === TouchType.HOVER_MOVE) {
26. this.eventType = 'HOVER_MOVE';
27. }
28. // 抬手时触发
29. if (event.type === TouchType.HOVER_EXIT) {
30. this.eventType = 'HOVER_EXIT';
31. }
32. // 取消当前触发事件
33. if (event.type === TouchType.HOVER_CANCEL) {
34. this.eventType = 'HOVER_CANCEL';
35. }
36. this.text = 'TouchType:' + this.eventType + '\nDistance between touch point and touch element:\nx: '
37. + event.touches[0].x + '\n' + 'y: ' + event.touches[0].y + '\nComponent globalPos:('
38. + event.target.area.globalPosition.x + ',' + event.target.area.globalPosition.y + ')\nwidth:'
39. + event.target.area.width + '\nheight:' + event.target.area.height;
40. }
41. })
42. }
43. }
```
