---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-cursor
title: 鼠标光标控制
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 交互属性 > 鼠标光标控制
category: harmonyos-references
scraped_at: 2026-04-29T13:51:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:df8adf5f1f33991d57720b938e5f897bafbd0c44c41de4989a694f1cd73748ac
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/leje5rNtQB257NaUqxqjng/zh-cn_image_0000002558606408.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055125Z&HW-CC-Expire=86400&HW-CC-Sign=B87478650C58AC835FFDF93E5C2D03EBDCED360FDD778F72A4077515D3D9798F)

当鼠标悬浮在绿色区域时，显示：向东箭头光标样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/rqrMKARORgSNzPkbXmBiHg/zh-cn_image_0000002589325935.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055125Z&HW-CC-Expire=86400&HW-CC-Sign=B3EF9E725F2D729F2B988B14ED15D8D2BCDF76C49BB8454DA7A168EF20B1EB42)
