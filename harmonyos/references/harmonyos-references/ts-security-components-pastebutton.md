---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-security-components-pastebutton
title: PasteButton
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 安全 > PasteButton
category: harmonyos-references
scraped_at: 2026-09-05T06:17:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bb01314e0deb7ca37b3ba112617043113ec312ca81c4903a1799d8101989c05a
---

安全控件的粘贴控件。用户点击粘贴控件，应用可以临时获取读取剪贴板权限。

**说明** 

该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 关键Class/Interface介绍

### 核心枚举类型

* **[PasteIconStyle](ts-security-components-pastebutton.md#pasteiconstyle)：** 粘贴控件图标风格枚举，用于指定控件展示的图标风格。
* **[PasteDescription](ts-security-components-pastebutton.md#pastedescription)：** 粘贴控件文本描述枚举，用于指定控件展示的文本描述。
* **[PasteButtonOnClickResult](ts-security-components-pastebutton.md#pastebuttononclickresult)：** 粘贴控件点击结果枚举，用于表示点击后授权是否成功。

### 核心接口类型

* **[PasteButtonOptions](ts-security-components-pastebutton.md#pastebuttonoptions)：** 粘贴控件配置对象，用于指定图标、文字和按钮类型等元素属性。
* **[PasteButtonCallback](ts-security-components-pastebutton.md#pastebuttoncallback18)：** 粘贴控件点击回调类型，用于返回点击事件、授权结果和错误信息。

## 子组件

不支持。

## 接口

### PasteButton

PasteButton()

默认创建带有图标、文本、背景的粘贴控件。控件创建完成后，用户点击时系统会执行授权校验；授权成功后，应用可读取当前剪贴板内容。

为避免因控件样式不合法而导致授权失败，请开发者先了解安全控件样式的[约束与限制](../harmonyos-guides/security-component-overview.md#约束与限制)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### PasteButton

PasteButton(options: PasteButtonOptions)

创建包含指定图标、文本或按钮类型的粘贴控件。控件创建完成后，用户点击时系统会执行授权校验动作；授权成功后，应用可临时获取读取剪贴板权限。

为避免因控件样式不合法而导致授权失败，请开发者先了解安全控件样式的[约束与限制](../harmonyos-guides/security-component-overview.md#约束与限制)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [PasteButtonOptions](ts-security-components-pastebutton.md#pastebuttonoptions) | 是 | 粘贴控件的配置选项，用于指定图标、文本和按钮类型等元素属性。建议至少显式设置icon或text中的一项，以便用户清楚识别控件用途。  若icon和text都未传入，则options不生效，控件显示为默认样式：  {  icon: PasteIconStyle.LINES,  text: PasteDescription.PASTE,  buttonType: ButtonType.Capsule  } |

## PasteButtonOptions

用于设置粘贴控件的图标、文本、按钮类型等属性。

**说明** 

* 建议icon或text至少传入一个。
* 如果icon、text都不传入，PasteButton将使用默认样式创建，默认样式：

  + PasteIconStyle默认样式为LINES。
  + PasteDescription默认样式为PASTE。
  + ButtonType默认样式为Capsule。
* icon、text和buttonType不支持动态修改。这是因为安全控件的样式和属性在创建时已通过系统校验，动态修改可能导致控件样式不符合安全控件规范，从而影响授权的有效性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [PasteIconStyle](ts-security-components-pastebutton.md#pasteiconstyle) | 否 | 是 | 设置粘贴控件的图标风格。  不传入该参数表示不显示图标；若同时也不传text，控件将显示为默认样式。 |
| text | [PasteDescription](ts-security-components-pastebutton.md#pastedescription) | 否 | 是 | 设置粘贴控件的文本描述。  不传入该参数表示不显示文本描述；若同时也不传icon，控件将显示为默认样式。 |
| buttonType | [ButtonType](ts-securitycomponent-attributes.md#buttontype) | 否 | 是 | 设置粘贴控件的按钮形状。不传入该参数时默认为ButtonType.Capsule。当需要自定义按钮形状时可传入此参数。 |

## 属性

不支持通用属性，仅继承[安全控件通用属性](ts-securitycomponent-attributes.md)。

## PasteIconStyle

粘贴控件的图标风格。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LINES | 0 | 粘贴控件展示线条样式图标。 |

## PasteDescription

粘贴控件的文本描述。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PASTE | 0 | 粘贴控件的文字描述为“粘贴”。 |

## PasteButtonOnClickResult

粘贴控件点击后的授权结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 粘贴控件点击后权限授权成功。 |
| TEMPORARY\_AUTHORIZATION\_FAILED | 1 | 粘贴控件点击后权限授权失败。 |

## PasteButtonCallback18+

type PasteButtonCallback = (event: ClickEvent, result: PasteButtonOnClickResult, error?: BusinessError<void>) => void

点击粘贴控件触发该回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ClickEvent](ts-universal-events-click.md#clickevent) | 是 | 点击事件对象，包含点击的位置、时间戳、输入设备等信息。 |
| result | [PasteButtonOnClickResult](ts-security-components-pastebutton.md#pastebuttononclickresult) | 是 | 剪贴板权限的授权结果。返回SUCCESS表示已获得当前剪贴板内容的临时读取权限，可以继续执行读取操作；返回TEMPORARY\_AUTHORIZATION\_FAILED表示本次授权未成功，不应继续读取剪贴板内容。 |
| error | [BusinessError<void>](js-apis-base.md#businesserror) | 否 | 点击按钮时的错误码和错误信息。未传入时为undefined。授权结果需通过result参数判断。  错误码1表示系统内部错误。请检查系统状态后重试。  错误码2表示属性设置错误，包括但不限于：  1. 字体或图标设置过小。  2. 字体或图标与控件背景颜色相近。  3. 字体或图标颜色过于透明。  4. padding为负值。  5. 按钮被其他组件或窗口遮挡。  6. 文本超出控件背景范围。  7. 按钮超出窗口或屏幕。  8. 按钮整体尺寸过大。  9. 按钮文本被截断，显示不全。  10. 部分安全控件相关属性的设置导致控件无法正常显示。 |

## 事件

不支持通用事件，仅支持以下事件：

### onClick

onClick(event: PasteButtonCallback)

点击粘贴控件触发该回调，回调返回授权结果。授权成功后应用可临时获取读取剪贴板权限。

为避免因控件样式不合法而导致授权失败，请开发者先了解安全控件样式的[约束与限制](../harmonyos-guides/security-component-overview.md#约束与限制)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [PasteButtonCallback](ts-security-components-pastebutton.md#pastebuttoncallback18) | 是 | 点击事件的回调函数，用于处理粘贴控件点击后的授权结果。  在API version 10-17时，参数类型为(event: [ClickEvent](ts-universal-events-click.md#clickevent), result: [PasteButtonOnClickResult](ts-security-components-pastebutton.md#pastebuttononclickresult)) => void；从API version 18开始，统一使用PasteButtonCallback，可额外获取error信息。 |

## 示例

```ts
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  // 定义粘贴按钮点击回调，处理授权结果和错误信息。
  handlePasteButtonClick: PasteButtonCallback =
    (event: ClickEvent, result: PasteButtonOnClickResult, error?: BusinessError<void>) => {
      if (result === PasteButtonOnClickResult.SUCCESS) {
        console.info('success');
      } else {
        console.error('errCode: ' + error?.code);
        console.error('errMessage: ' + error?.message);
      }
    };

  build() {
    Row() {
      Column({ space: 10 }) {
        // 默认参数下，图标、文字、背景都存在。
        PasteButton().onClick(this.handlePasteButtonClick)
        // 传入参数即表示元素存在，不传入的参数表示元素不存在，如果不传入buttonType，会默认添加ButtonType.Capsule配置，显示图标+背景。
        PasteButton({ icon: PasteIconStyle.LINES })
        // 只显示图标+背景，如果设置背景色高八位的α值低于0x1a，则会被系统强制调整为0xff。
        PasteButton({ icon: PasteIconStyle.LINES, buttonType: ButtonType.Capsule })
          .backgroundColor(0x10007dff)
        // 图标、文字、背景都存在，如果设置背景色高八位的α值低于0x1a，则会被系统强制调整为0xff。
        PasteButton({ icon: PasteIconStyle.LINES, text: PasteDescription.PASTE, buttonType: ButtonType.Capsule })
        // 图标、文字、背景都存在，如果设置宽度小于当前属性组合下允许的最小宽度时，宽度仍为设置值，此时按钮文本信息会自动换行，以保证安全控件显示的完整性。
        PasteButton({ icon: PasteIconStyle.LINES, text: PasteDescription.PASTE, buttonType: ButtonType.Capsule })
          .fontSize(16)
          .width(30)
        // 图标、文字、背景都存在，如果设置宽度小于当前属性组合下允许的最小宽度时，宽度仍为设置值，此时按钮文本信息会自动换行，以保证安全控件显示的完整性。
        PasteButton({ icon: PasteIconStyle.LINES, text: PasteDescription.PASTE, buttonType: ButtonType.Capsule })
          .fontSize(16)
          .size({ width: 30, height: 30 })
        // 图标、文字、背景都存在，如果设置宽度小于当前属性组合下允许的最小宽度时，宽度仍为设置值，此时按钮文本信息会自动换行，以保证安全控件显示的完整性。
        PasteButton({ icon: PasteIconStyle.LINES, text: PasteDescription.PASTE, buttonType: ButtonType.Capsule })
          .fontSize(16)
          .constraintSize({
            minWidth: 0,
            maxWidth: 30,
            minHeight: 0,
            maxHeight: 30
          })
      }.width('100%')
    }.height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/IfOElA9tTLy4m7duLMO8kg/zh-cn_image_0000002742125397.png)
