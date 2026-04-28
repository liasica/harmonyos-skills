---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-security-components-pastebutton
title: PasteButton
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 安全 > PasteButton
category: harmonyos-references
scraped_at: 2026-04-28T08:02:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2bafc0beb215b7d0f29937804fc7b20ff244bf8a401932779a018801117a4d5c
---

安全控件的粘贴控件。用户点击粘贴控件，应用可以临时获取读取剪贴板权限。

说明

该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 接口

PhonePC/2in1TabletTVWearable

### PasteButton

PhonePC/2in1TabletTVWearable

PasteButton()

默认创建带有图标、文本、背景的粘贴控件。

为避免因控件样式不合法而导致授权失败，请开发者先了解安全控件样式的[约束与限制](../harmonyos-guides/security-component-overview.md#约束与限制)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### PasteButton

PhonePC/2in1TabletTVWearable

PasteButton(options: PasteButtonOptions)

创建包含指定元素的粘贴控件。

为避免因控件样式不合法而导致授权失败，请开发者先了解安全控件样式的[约束与限制](../harmonyos-guides/security-component-overview.md#约束与限制)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [PasteButtonOptions](ts-security-components-pastebutton.md#pastebuttonoptions) | 是 | 创建包含指定元素的粘贴控件。  默认值：  {  icon: PasteIconStyle.LINES,  text: PasteDescription.PASTE,  buttonType: ButtonType.Capsule  } |

## PasteButtonOptions

PhonePC/2in1TabletTVWearable

用于指定粘贴控件的图标、文本等指定元素。

说明

* icon或text需至少传入一个。
* 如果icon、text都不传入，PasteButton中的options参数不生效，创建的PasteButton为默认样式。

  + PasteIconStyle默认样式为LINES。
  + PasteDescription默认样式为PASTE。
  + ButtonType默认样式为Capsule。
* icon、text和buttonType不支持动态修改。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [PasteIconStyle](ts-security-components-pastebutton.md#pasteiconstyle枚举说明) | 否 | 是 | 设置粘贴控件的图标风格。  不传入该参数表示没有图标。 |
| text | [PasteDescription](ts-security-components-pastebutton.md#pastedescription枚举说明) | 否 | 是 | 设置粘贴控件的文本描述。  不传入该参数表示没有文字描述。 |
| buttonType | [ButtonType](ts-securitycomponent-attributes.md#buttontype枚举说明) | 否 | 是 | 设置粘贴控件的背景样式。  不传入该参数，系统默认提供Capsule类型按钮。 |

## 属性

PhonePC/2in1TabletTVWearable

不支持通用属性，仅继承[安全控件通用属性](ts-securitycomponent-attributes.md)。

## PasteIconStyle枚举说明

PhonePC/2in1TabletTVWearable

粘贴控件的图标风格。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LINES | 0 | 粘贴控件展示线条样式图标。 |

## PasteDescription枚举说明

PhonePC/2in1TabletTVWearable

粘贴控件的文本描述。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PASTE | 0 | 粘贴控件的文字描述为“粘贴”。 |

## PasteButtonOnClickResult枚举说明

PhonePC/2in1TabletTVWearable

粘贴控件点击后的授权结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 粘贴控件点击后权限授权成功。 |
| TEMPORARY\_AUTHORIZATION\_FAILED | 1 | 粘贴控件点击后权限授权失败。 |

## PasteButtonCallback18+

PhonePC/2in1TabletTVWearable

type PasteButtonCallback = (event: ClickEvent, result: PasteButtonOnClickResult, error?: BusinessError<void>) => void

点击粘贴控件触发该回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ClickEvent](ts-universal-events-click.md#clickevent) | 是 | 见ClickEvent对象说明。 |
| result | [PasteButtonOnClickResult](ts-security-components-pastebutton.md#pastebuttononclickresult枚举说明) | 是 | 剪贴板权限的授权结果，授权后可以读取当前剪贴板内容。 |
| error | [BusinessError<void>](js-apis-base.md#businesserror) | 否 | 点击按钮时的错误码和错误信息。  错误码0表示点击粘贴控件授权成功。  错误码1表示系统内部错误。  错误码2表示属性设置错误，包括但不限于：  1. 字体或图标设置过小。  2. 字体或图标与背托颜色相近。  3. 字体或图标颜色过于透明。  4. padding为负值。  5. 按钮被其他组件或窗口遮挡。  6. 文本超出背托范围。  7. 按钮超出窗口或屏幕。  8. 按钮整体尺寸过大。  9. 按钮文本被截断，显示不全。  10. 相关属性设置影响安全控件显示。 |

## 事件

PhonePC/2in1TabletTVWearable

不支持通用事件，仅支持以下事件：

### onClick

PhonePC/2in1TabletTVWearable

onClick(event: PasteButtonCallback)

点击动作触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [PasteButtonCallback](ts-security-components-pastebutton.md#pastebuttoncallback18) | 是 | 见PasteButtonCallback。  在API10-17时，参数类型为：(event: [ClickEvent](ts-universal-events-click.md#clickevent), result: [PasteButtonOnClickResult](ts-security-components-pastebutton.md#pastebuttononclickresult枚举说明)) => void。  从API18开始，变更为PasteButtonCallback。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. // xxx.ets
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. handlePasteButtonClick: PasteButtonCallback =
8. (event: ClickEvent, result: PasteButtonOnClickResult, error?: BusinessError<void>) => {
9. if (result === PasteButtonOnClickResult.SUCCESS) {
10. console.info("success");
11. } else {
12. console.error("errCode: " + error?.code);
13. console.error("errMessage: " + error?.message);
14. }
15. };

17. build() {
18. Row() {
19. Column({ space: 10 }) {
20. // 默认参数下，图标、文字、背景都存在。
21. PasteButton().onClick(this.handlePasteButtonClick)
22. // 传入参数即表示元素存在，不传入的参数表示元素不存在，如果不传入buttonType，会默认添加ButtonType.Capsule配置，显示图标+背景。
23. PasteButton({ icon: PasteIconStyle.LINES })
24. // 只显示图标+背景，如果设置背景色高八位的α值低于0x1a，则会被系统强制调整为0xff。
25. PasteButton({ icon: PasteIconStyle.LINES, buttonType: ButtonType.Capsule })
26. .backgroundColor(0x10007dff)
27. // 图标、文字、背景都存在，如果设置背景色高八位的α值低于0x1a，则会被系统强制调整为0xff。
28. PasteButton({ icon: PasteIconStyle.LINES, text: PasteDescription.PASTE, buttonType: ButtonType.Capsule })
29. // 图标、文字、背景都存在，如果设置宽度小于当前属性组合下允许的最小宽度时，宽度仍为设置值，此时按钮文本信息会自动换行，以保证安全控件显示的完整性。
30. PasteButton({ icon: PasteIconStyle.LINES, text: PasteDescription.PASTE, buttonType: ButtonType.Capsule })
31. .fontSize(16)
32. .width(30)
33. // 图标、文字、背景都存在，如果设置宽度小于当前属性组合下允许的最小宽度时，宽度仍为设置值，此时按钮文本信息会自动换行，以保证安全控件显示的完整性。
34. PasteButton({ icon: PasteIconStyle.LINES, text: PasteDescription.PASTE, buttonType: ButtonType.Capsule })
35. .fontSize(16)
36. .size({ width: 30, height: 30 })
37. // 图标、文字、背景都存在，如果设置宽度小于当前属性组合下允许的最小宽度时，宽度仍为设置值，此时按钮文本信息会自动换行，以保证安全控件显示的完整性。
38. PasteButton({ icon: PasteIconStyle.LINES, text: PasteDescription.PASTE, buttonType: ButtonType.Capsule })
39. .fontSize(16)
40. .constraintSize({
41. minWidth: 0,
42. maxWidth: 30,
43. minHeight: 0,
44. maxHeight: 30
45. })
46. }.width('100%')
47. }.height('100%')
48. }
49. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/qRN7OtJWQde6i6GFByN3bw/zh-cn_image_0000002583440121.png?HW-CC-KV=V1&HW-CC-Date=20260428T000224Z&HW-CC-Expire=86400&HW-CC-Sign=731E3AF7337DACD62D2FCA252FB68DD4C4420D15894F4A6EDFA483CB002E3212)
