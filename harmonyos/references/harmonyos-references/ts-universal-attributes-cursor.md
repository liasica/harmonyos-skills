---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-cursor
title: 鼠标光标控制
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 交互属性 > 鼠标光标控制
category: harmonyos-references
scraped_at: 2026-04-28T08:01:12+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0cef747177aa00070373f82c7457cab8d92e57dc8a6550d34038f316a20f2ffd
---

控制鼠标光标的显示样式。

说明

从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## cursorControl

PhonePC/2in1TabletTVWearable

### setCursor

PhonePC/2in1TabletTVWearable

setCursor(value: PointerStyle): void

方法语句中可使用的全局接口，调用该接口可更改当前的鼠标光标样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PointerStyle](ts-universal-attributes-cursor.md#pointerstyle) | 是 | 设置的鼠标样式。 |

### restoreDefault

PhonePC/2in1TabletTVWearable

restoreDefault(): void

方法语句中可使用的全局接口，调用此接口可将鼠标光标恢复成默认箭头样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## PointerStyle

PhonePC/2in1TabletTVWearable

type PointerStyle = pointer.PointerStyle

光标样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [pointer.PointerStyle](js-apis-pointer.md#pointerstyle) | 光标样式。 |

说明

直接使用cursorControl可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题，建议使用getUIContext()获取[UIContext](arkts-apis-uicontext-uicontext.md)实例，并使用[getCursorController](arkts-apis-uicontext-uicontext.md#getcursorcontroller12)获取绑定实例的cursorControl。

## 示例

PhonePC/2in1TabletTVWearable

该示例通过setCursor实现了鼠标光标样式的更改。

```
1. // xxx.ets
2. import { pointer } from '@kit.InputKit';

4. @Entry
5. @Component
6. struct CursorControlExample {
7. @State text: string = '';
8. controller: TextInputController = new TextInputController()

10. build() {
11. Column() {
12. Row()
13. .height(200)
14. .width(200)
15. .backgroundColor(Color.Green)
16. .position({ x: 60, y: 70 })
17. .onHover((flag) => {
18. if (flag) {
19. // 建议使用this.getUIContext().getCursorController().setCursor()
20. cursorControl.setCursor(pointer.PointerStyle.EAST)
21. } else {
22. // 建议使用this.getUIContext().getCursorController().restoreDefault()
23. cursorControl.restoreDefault()
24. }
25. })
26. Row()
27. .height(200)
28. .width(200)
29. .backgroundColor(Color.Blue)
30. .position({ x: 130, y: 120 })
31. .onHover((flag) => {
32. if (flag) {
33. // 建议使用this.getUIContext().getCursorController().setCursor()
34. cursorControl.setCursor(pointer.PointerStyle.WEST)
35. } else {
36. // 建议使用this.getUIContext().getCursorController().restoreDefault()
37. cursorControl.restoreDefault()
38. }
39. })
40. }.width('100%')
41. }
42. }
```

示意图：

当鼠标悬浮在蓝色区域时，显示：向西箭头光标样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/NOEnm68oR-a9YpJFy2Hc7g/zh-cn_image_0000002583479545.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=50AD722588981930692C28DD2F37445BAC6FD01B6FE83D6FDC6E7B93D39F9802)

当鼠标悬浮在绿色区域时，显示：向东箭头光标样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/LosbMxgyRVW7SMO0uHulTQ/zh-cn_image_0000002552799896.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000112Z&HW-CC-Expire=86400&HW-CC-Sign=356B318E4C1ECBC8079C3D1F163F807ECA27E4E361383EC36A792942D5EBEA69)
