---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common
title: 选择器（Picker）公共接口
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 按钮与选择 > 选择器（Picker）公共接口
category: harmonyos-references
scraped_at: 2026-04-28T08:01:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:caaeda3226ca3a755433efa572e60a0cef25a5ba0b827d093916e8b2c622811b
---

选择器组件公共接口。

说明

从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## PickerTextStyle对象说明

PhonePC/2in1TabletTVWearable

选择器组件的文本样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 文本颜色。 |
| font | [Font](ts-types.md#font) | 否 | 是 | 文本样式。 |

## PickerDialogButtonStyle12+对象说明

PhonePC/2in1TabletTVWearable

选择器弹窗的按钮样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ButtonType](ts-basic-components-button.md#buttontype枚举说明) | 否 | 是 | 按钮显示样式。 |
| style | [ButtonStyleMode](ts-basic-components-button.md#buttonstylemode11枚举说明) | 否 | 是 | 按钮的样式和重要程度。 |
| role | [ButtonRole](ts-basic-components-button.md#buttonrole12枚举说明) | 否 | 是 | Button组件的角色。 |
| fontSize | [Length](ts-types.md#length) | 否 | 是 | 文本显示字号。 |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 文本显示颜色。 |
| fontWeight | [FontWeight](ts-appendix-enums.md#fontweight) | number | string | 否 | 是 | 文本的字体粗细。number类型取值[100, 900]，取值间隔为100，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如"200"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。 |
| fontStyle | [FontStyle](ts-appendix-enums.md#fontstyle) | 否 | 是 | 文本的字体样式。 |
| fontFamily | [Resource](ts-types.md#resource) | string | 否 | 是 | 字体列表。默认字体'HarmonyOS Sans'，当前支持'HarmonyOS Sans'字体和[注册自定义字体](js-apis-font.md)。 |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 按钮背景色。 |
| borderRadius | [Length](ts-types.md#length) | [BorderRadiuses](ts-types.md#borderradiuses9) | 否 | 是 | 圆角半径。 |
| primary | boolean | 否 | 是 | 弹出弹窗后，未使用Tab键切换焦点时，Enter键是否默认由该按钮响应。  true：弹出弹窗后，未使用Tab键切换焦点时，按下Enter键会触发该按钮绑定的事件。  false：弹出弹窗后，未使用Tab键切换焦点时，按下Enter键不会触发该按钮绑定的事件。  默认值：false |

## DateRange19+对象说明

PhonePC/2in1TabletTVWearable

日期区间，用于描述起止日期区间。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | Date | 否 | 是 | 设置日期区间的开始日期。 |
| end | Date | 否 | 是 | 设置日期区间的结束日期。 |
