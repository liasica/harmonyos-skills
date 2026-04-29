---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-chip
title: Chip
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > Chip
category: harmonyos-references
scraped_at: 2026-04-29T13:52:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:853cf40bdbe2ecfc14e97aa4c6e59a85f8fdbb433735377fe0167564ec5dfe6e
---

Chip用于搜索框历史记录、邮件发送列表等场景。

说明

该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { Chip, ChipOptions, ChipSize } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## Chip

PhonePC/2in1TabletTVWearable

Chip(options:ChipOptions): void

**装饰器类型：**@Builder

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常， 异常信息中提示接口未定义，在其他设备中可正常调用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ChipOptions](ohos-arkui-advanced-chip.md#chipoptions) | 是 | 定义Chip组件的参数。 |

## ChipOptions

PhonePC/2in1TabletTVWearable

ChipOptions定义Chip的样式及具体式样参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size | [ChipSize](ohos-arkui-advanced-chip.md#chipsize) | [SizeOptions](ts-types.md#sizeoptions) | 否 | 是 | Chip尺寸。  默认值：ChipSize.NORMAL  SizeOptions类型参数不支持百分比设置，异常值按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **说明**：[适老化](../harmonyos-guides/arkui-support-for-aging-adaptation.md)在size指定具体宽高时不生效，size设置为{ height: 0, width: 0 }除外。 |
| enabled | boolean | 否 | 是 | Chip是否可选中。  默认值：true。  true：操作块可选中；false：操作块不可选中。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| activated12+ | boolean | 否 | 是 | Chip是否为激活态。  默认值：false。  true：操作块为激活态；false：操作块为非激活态。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| prefixIcon | [PrefixIconOptions](ohos-arkui-advanced-chip.md#prefixiconoptions) | 否 | 是 | 前缀图标属性。  默认值：不显示前缀图标。  值为undefined时，按默认值处理。  prefixIcon和prefixSymbol同时设置时，显示prefixSymbol的效果，prefixIcon无效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| prefixSymbol12+ | [ChipSymbolGlyphOptions](ohos-arkui-advanced-chip.md#chipsymbolglyphoptions12) | 否 | 是 | 前缀图标属性，symbol类型。  默认值：不显示前缀图标。  值为undefined时，按默认值处理。  prefixIcon和prefixSymbol同时设置时，显示prefixSymbol的效果，prefixIcon无效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| label | [LabelOptions](ohos-arkui-advanced-chip.md#labeloptions) | 否 | 否 | 文本属性。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| suffixIcon | [SuffixIconOptions](ohos-arkui-advanced-chip.md#suffixiconoptions) | 否 | 是 | 后缀图标属性。  默认值：不显示后缀图标。  值为undefined时，按默认值处理。  suffixIcon和suffixSymbol同时设置时，显示suffixSymbol的效果，suffixIcon无效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| suffixSymbol12+ | [ChipSymbolGlyphOptions](ohos-arkui-advanced-chip.md#chipsymbolglyphoptions12) | 否 | 是 | 后缀图标属性，symbol类型。  默认值：不显示后缀图标。  值为undefined时，按默认值处理。  suffixIcon和suffixSymbol同时设置时，显示suffixSymbol的效果，suffixIcon无效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| suffixSymbolOptions14+ | [ChipSuffixSymbolGlyphOptions](ohos-arkui-advanced-chip.md#chipsuffixsymbolglyphoptions14) | 否 | 是 | symbol类型后缀图标属性的无障碍朗读功能属性。  默认值：不显示后缀图标。  值为undefined时，按默认值处理。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | Chip背景颜色。  默认值：$r('sys.color.ohos\_id\_color\_button\_normal')。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| activatedBackgroundColor12+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | Chip激活时的背景颜色。  默认值：$r('sys.color.ohos\_id\_color\_emphasize')。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| borderRadius | [Dimension](ts-types.md#dimension10) | 否 | 是 | Chip背景圆角半径大小，不支持百分比。  默认值：$r('sys.float.ohos\_id\_corner\_radius\_button')。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| allowClose | boolean | 否 | 是 | 关闭图标是否显示。  默认值：true  true：删除图标显示；false：删除图标不显示。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onClose | ()=>void | 否 | 是 | 默认关闭图标点击事件。  值为undefined时，关闭图标点击事件。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onClicked12+ | Callback<void> | 否 | 是 | Chip点击事件。  值为undefined时，Chip不能被点击。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| direction12+ | [Direction](ts-appendix-enums.md#direction) | 否 | 是 | 布局方向。  默认值：Direction.Auto。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| closeOptions14+ | [CloseOptions](ohos-arkui-advanced-chip.md#closeoptions14) | 否 | 是 | 默认关闭图标的无障碍朗读功能属性。  值为undefined时，按默认值处理。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| accessibilityDescription14+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | Chip组件的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的结果。特别是当这些结果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| accessibilityLevel14+ | string | 否 | 是 | Chip组件无障碍重要性。用于控制后缀图标是否可被无障碍辅助服务所识别。  支持的值为:  "auto"：当前组件会转化为"yes"。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"。  值为undefined时，按默认值处理。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| accessibilitySelectedType14+ | [AccessibilitySelectedType](ohos-arkui-advanced-chip.md#accessibilityselectedtype14) | 否 | 是 | Chip组件选中态类型。  默认值：当设置了activated属性但未指定accessibilitySelectedType时，默认使用CHECKED类型。当未设置activated属性时，默认使用CLICKED类型。  值为undefined时，按默认值处理。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| maxFontScale23+ | number | [Resource](ts-types.md#resource) | 否 | 是 | Chip组件文本与图标的最大的字体缩放倍数。  取值范围：[1, +∞)  设置的值小于1时，按值为1处理。异常值默认不生效。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| minFontScale23+ | number | [Resource](ts-types.md#resource) | 否 | 是 | Chip组件文本与图标的最小的字体缩放倍数。  取值范围：[0, 1]  设置的值小于0时，按值为0处理。设置的值大于1时，按值为1处理。异常值默认不生效。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| padding23+ | [LocalizedPadding](ts-types.md#localizedpadding12) | 否 | 是 | Chip组件的内边距。  默认值：  - size为ChipSize.SMALL并且activated为true时，默认值：{ start: LengthMetrics.resource('sys.float.chip\_activated\_small\_text\_padding'), end: LengthMetrics.resource('sys.float.chip\_activated\_small\_text\_padding'), top: LengthMetrics.vp(4), bottom: LengthMetrics.vp(4)}  - size为ChipSize.SMALL并且activated为false时，默认值：{ start: LengthMetrics.resource('sys.float.chip\_small\_text\_padding'), end: LengthMetrics.resource('sys.float.chip\_small\_text\_padding'), top: LengthMetrics.vp(4), bottom: LengthMetrics.vp(4)}  - size不为ChipSize.SMALL并且activated为true时，默认值：{ start: LengthMetrics.resource('sys.float.chip\_activated\_normal\_text\_padding'), end: LengthMetrics.resource('sys.float.chip\_activated\_normal\_text\_padding'), top: LengthMetrics.vp(4), bottom: LengthMetrics.vp(4)}  - size不为ChipSize.SMALL并且activated为false时，默认值：{ start: LengthMetrics.resource('sys.float.chip\_normal\_text\_padding'), end: LengthMetrics.resource('sys.float.chip\_normal\_text\_padding'), top: LengthMetrics.vp(4), bottom: LengthMetrics.vp(4)}  值为undefined时，按默认值处理。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| fontSize23+ | [Dimension](ts-types.md#dimension10) | 否 | 是 | 统一设置Chip组件的文本与图标的字体大小，不支持百分比。  该fontSize的优先级低于prefixSymbol、label、suffixSymbol和closeOptions中的fontSize属性。  默认值：  - size为ChipSize.SMALL时，文本默认值：$r('sys.float.chip\_small\_font\_size')；图标默认值：$r('sys.float.chip\_small\_icon\_size')  - 其他情况下，文本默认值：$r('sys.float.chip\_normal\_font\_size')；图标默认值：$r('sys.float.chip\_normal\_icon\_size')  值为undefined时，按默认值处理。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

说明

1. 当suffixSymbol有传入参数时，suffixIcon和allowClose不生效；当suffixSymbol没有传入参数而suffixIcon有传入参数时，allowClose不生效；当suffixSymbol和suffixIcon都没有传入参数时，allowClose决定是否显示删除图标。
2. backgroundColor和activatedBackgroundColor赋值为undefined时，显示默认背景颜色；赋值为非法值时，背景颜色透明。
3. prefixSymbol/suffixSymbol的fontColor默认值为：normalFontColor: [$r('sys.color.ohos\_id\_color\_primary')]、activatedFontColor: [$r('sys.color.ohos\_id\_color\_text\_primary\_contrary')]。fontColor默认值为16。
4. prefixIcon的fillColor默认值为：$r('sys.color.ohos\_id\_color\_secondary')，suffixIcon的fillColor默认值为：$r('sys.color.ohos\_id\_color\_primary')。fillColor对颜色的解析与Image组件保持一致。
5. prefixIcon和suffixIcon的activatedFillColor默认值均为：$r('sys.color.ohos\_id\_color\_text\_primary\_contrary')。activatedFillColor对颜色的解析与Image组件保持一致。

## ChipSize

PhonePC/2in1TabletTVWearable

ChipSize是Chip可指定的尺寸类型，如普通型Chip。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | "NORMAL" | normal尺寸操作块。 |
| SMALL | "SMALL" | small尺寸操作块。 |

## AccessibilitySelectedType14+

PhonePC/2in1TabletTVWearable

AccessibilitySelectedType是Chip可指定的选中态类型，用于控制无障碍服务如何向用户传达组件的选中状态。不同的选中态类型提供了不同的语义和用户体验。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CLICKED | 0 | 单击型。组件不向无障碍服务报告任何选中状态，仅作为可单击组件使用。适用于执行某个操作但不保持状态的场景，如普通按钮。 |
| CHECKED | 1 | 复选型。组件通过 [accessibilityChecked](ts-universal-attributes-accessibility.md#accessibilitychecked13) 属性向无障碍服务报告选中状态。适用于多选场景，如标签筛选、属性选择等。 |
| SELECTED | 2 | 单选型。组件通过 [accessibilitySelected](ts-universal-attributes-accessibility.md#accessibilityselected13) 属性向无障碍服务报告选中状态。适用于表示当前选中项的场景，如导航栏标签、单选列表项等。 |

## IconCommonOptions

PhonePC/2in1TabletTVWearable

IconCommonOptions定义图标的共通属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| src | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 图标图片或图片地址引用。 |
| size | [SizeOptions](ts-types.md#sizeoptions) | 否 | 是 | 图标大小，不支持百分比。  默认值：  - 当ChipOptions.size为ChipSize.SMALL时，默认值为：{width: $r('sys.float.chip\_small\_icon\_size'), height: $r('sys.float.chip\_small\_icon\_size')}  - 当ChipOptions.size为ChipSize.NORMAL时，默认值为：{width: $r('sys.float.chip\_normal\_icon\_size'), height: $r('sys.float.chip\_normal\_icon\_size')}  单位：vp  值为undefined时，按默认值处理。 |
| fillColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 图标填充颜色。  默认值：$r('sys.color.chip\_usually\_icon\_color')  值为undefined时，按默认值处理。 |
| activatedFillColor12+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 操作块激活时图标填充颜色。  默认值：$r('sys.color.chip\_active\_icon\_color')  值为undefined时，按默认值处理。 |

说明

仅在图片格式为SVG时，fillColor和activatedFillColor属性才生效。

## PrefixIconOptions

PhonePC/2in1TabletTVWearable

PrefixIconOptions定义前缀图标的属性。

继承于[IconCommonOptions](ohos-arkui-advanced-chip.md#iconcommonoptions)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

## SuffixIconOptions

PhonePC/2in1TabletTVWearable

SuffixIconOptions定义后缀图标的属性。

继承于[IconCommonOptions](ohos-arkui-advanced-chip.md#iconcommonoptions)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| action | () => void | 否 | 是 | 后缀图标设定事件。  值为undefined时，不设定后缀图标事件。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| accessibilityText14+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 后缀图标无障碍文本属性。当后缀图标不包含文本属性时，屏幕朗读选中后缀图标时不播报，使用者无法清楚地知道当前是否选中了后缀图标。为了解决此场景，开发人员可为不包含文字信息的后缀图标设置无障碍文本，当屏幕朗读选中后缀图标时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己是否选中了后缀图标。  默认值：‘ ’  值为undefined时，按默认值处理。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| accessibilityDescription14+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 后缀图标的无障碍描述。此描述用于向用户详细解释后缀图标，开发人员应为后缀图标的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从后缀图标的属性和无障碍文本中直接获知时。如果后缀图标同时具备文本属性和无障碍说明属性，当后缀图标被选中时，系统将首先播报后缀图标的文本属性，随后播报无障碍说明属性的内容。  默认值：‘ ’  值为undefined时，按默认值处理。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| accessibilityLevel14+ | string | 否 | 是 | 后缀图标的无障碍重要性。用于控制后缀图标是否可被无障碍辅助服务识别。  支持的值为:  "auto"：当前组件存在action时转化为"yes"，不存在action时，转化为"no"。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"。  值为undefined时，按默认值处理。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |

## AccessibilityOptions14+

PhonePC/2in1TabletTVWearable

后缀图标的无障碍朗读功能属性。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| accessibilityText | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 无障碍文本属性。当组件无文本属性时，屏幕朗读选中此组件不会播报，导致使用者无法清楚了解当前选中的组件。开发人员可为此类组件设置无障碍文本，屏幕朗读时将播报该文本，帮助使用者明确选中了什么组件。  默认值：‘ ’  值为undefined时，按默认值处理。 |
| accessibilityDescription | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 无障碍描述。此描述用于向用户详细解释当前组件，开发人员应提供详尽的文本说明，以协助用户理解即将执行的操作及其后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。  默认值：‘ ’  值为undefined时，按默认值处理。 |
| accessibilityLevel | string | 否 | 是 | 无障碍重要性。用于控制组件是否可被无障碍辅助服务识别。  支持的值为:  "auto"：当前组件会转换为"yes"。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"。  值为undefined时，按默认值处理。 |

## ChipSuffixSymbolGlyphOptions14+

PhonePC/2in1TabletTVWearable

symbol类型后缀图标属性的无障碍朗读功能属性类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| action | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 后缀图标设定事件。  默认值：undefined |
| normalAccessibility | [AccessibilityOptions](ohos-arkui-advanced-chip.md#accessibilityoptions14) | 否 | 是 | 非激活态无障碍朗读功能属性。  默认值：undefined |
| activatedAccessibility | [AccessibilityOptions](ohos-arkui-advanced-chip.md#accessibilityoptions14) | 否 | 是 | 激活态无障碍朗读功能属性。  默认值：undefined |

## ChipSymbolGlyphOptions12+

PhonePC/2in1TabletTVWearable

ChipSymbolGlyphOptions定义前缀图标和后缀图标的属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| normal | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | 非激活时图标设定。  默认值：不显示前缀图标或后缀图标  值为undefined时，按默认值处理。 |
| activated | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | 激活时图标设定。  默认值：不显示前缀图标或后缀图标  值为undefined时，按默认值处理。 |

说明

不支持使用[SymbolEffect](ts-basic-components-symbolglyph.md#symboleffect12对象说明)修改动效类型及effectStrategy设置动效。

## LabelOptions

PhonePC/2in1TabletTVWearable

LabelOptions定义文本属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | string | 否 | 否 | 文本文字内容。 |
| fontSize | [Dimension](ts-types.md#dimension10) | 否 | 是 | 文字字号，不支持百分比。  默认值：$r('sys.float.ohos\_id\_text\_size\_button2')  值为undefined时，按默认值处理。 |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 文字颜色。  默认值：$r('sys.color.ohos\_id\_color\_text\_primary')  值为undefined时，按默认值处理。 |
| activatedFontColor12+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 操作块激活时的文字颜色。  默认值：$r('sys.color.ohos\_id\_color\_text\_primary\_contrary')  值为undefined时，按默认值处理。 |
| fontFamily | string | 否 | 是 | 文字字体。  默认值："HarmonyOS Sans"  值为undefined时，按默认值处理。 |
| labelMargin | [LabelMarginOptions](ohos-arkui-advanced-chip.md#labelmarginoptions) | 否 | 是 | 文本与左右侧图标之间间距。  默认值：  size为ChipSize.SMALL时，默认值：{ left: 4, right: 4 }  size为ChipSize.NORMAL时，默认值：{ left: 6, right: 6 }  单位：vp  值为undefined时，按默认值处理。 |
| localizedLabelMargin12+ | [LocalizedLabelMarginOptions](ohos-arkui-advanced-chip.md#localizedlabelmarginoptions12) | 否 | 是 | 本地化文本与左右侧图标之间间距。  默认值：  size为ChipSize.SMALL时，默认值：  { start: LengthMetrics.resource($r('sys.float.chip\_small\_text\_margin')), end: LengthMetrics.resource($r('sys.float.chip\_small\_text\_margin')) }  size为ChipSize.NORMAL时，默认值：  { start: LengthMetrics.resource($r('sys.float.chip\_normal\_text\_margin')), end: LengthMetrics.resource($r('sys.float.chip\_normal\_text\_margin')) }  值为undefined时，按默认值处理。 |

## CloseOptions14+

PhonePC/2in1TabletTVWearable

CloseOptions用于定义Chip组件默认的关闭图标功能属性，包括无障碍功能属性，其中accessibilityText默认为"删除"。

继承于[AccessibilityOptions](ohos-arkui-advanced-chip.md#accessibilityoptions14)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontSize23+ | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置Chip组件默认关闭图标的大小，不支持百分比。  默认值：  size为ChipSize.SMALL时，默认值：$r('sys.float.chip\_small\_font\_size')  其他情况默认值：$r('sys.float.chip\_normal\_font\_size')  值为undefined时，按默认值处理。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## LabelMarginOptions

PhonePC/2in1TabletTVWearable

LabelMarginOptions用于定义文本与左右侧图标之间间距。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | [Dimension](ts-types.md#dimension10) | 否 | 是 | 文本与左侧图标之间间距，不支持百分比。  默认值：  size为ChipSize.SMALL时，left默认值：4  size为ChipSize.NORMAL时，left默认值：6  单位：vp  超出取值范围按默认值处理。  取值范围：[0, +∞) |
| right | [Dimension](ts-types.md#dimension10) | 否 | 是 | 文本与右侧图标之间间距，不支持百分比。  默认值：  size为ChipSize.SMALL时，right默认值：4  size为ChipSize.NORMAL时，right默认值：6  单位：vp  超出取值范围按默认值处理。  取值范围：[0, +∞) |

## LocalizedLabelMarginOptions12+

PhonePC/2in1TabletTVWearable

LocalizedLabelMarginOptions用于定义本地化文本与左右侧图标之间间距。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 文本与左侧图标之间间距，不支持百分比。  默认值：  size为ChipSize.SMALL时，start默认值:  LengthMetrics.resource($r('sys.float.chip\_small\_text\_margin'))  size为ChipSize.NORMAL时，start默认值：  LengthMetrics.resource($r('sys.float.chip\_normal\_text\_margin'))  值为undefined时，按默认值处理。 |
| end | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 文本与右侧图标之间间距，不支持百分比。  默认值：  size为ChipSize.SMALL时，end默认值：  LengthMetrics.resource($r('sys.float.chip\_small\_text\_margin'))  size为ChipSize.NORMAL时，end默认值:  LengthMetrics.resource($r('sys.float.chip\_normal\_text\_margin'))  值为undefined时，按默认值处理。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（自定义后缀图标）

通过配置suffixIcon实现自定义操作块的后缀图标。

```
1. import { Chip, ChipSize, LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Column({ space: 10 }) {
8. Chip({
9. // 设置前缀图标属性。
10. prefixIcon: {
11. // 'app.media.chips'仅作示例，请替换为实际使用图片。
12. src: $r('app.media.chips'),
13. size: { width: 16, height: 16 },
14. fillColor: Color.Red
15. },
16. // 设置文本属性。
17. label: {
18. text: '操作块',
19. fontSize: 12,
20. fontColor: Color.Blue,
21. fontFamily: 'HarmonyOS Sans',
22. labelMargin: { left: 20, right: 30 }
23. },
24. // 设置后缀图标属性。
25. suffixIcon: {
26. // 'app.media.close'仅作示例，请替换为实际使用图片。
27. src: $r('app.media.close'),
28. size: { width: 16, height: 16 },
29. fillColor: Color.Red
30. },
31. size: ChipSize.NORMAL,
32. allowClose: false,
33. enabled: true,
34. backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
35. borderRadius: $r('sys.float.ohos_id_corner_radius_button'),
36. minFontScale: 0.2,
37. maxFontScale: 2,
38. padding: {
39. start: LengthMetrics.vp(20),
40. end: LengthMetrics.vp(20)
41. },
42. fontSize: 12
43. })
44. }
45. }
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/rmtkePsPQLO8WqHyebD4eQ/zh-cn_image_0000002558766620.png?HW-CC-KV=V1&HW-CC-Date=20260429T055256Z&HW-CC-Expire=86400&HW-CC-Sign=FF4CA55C221F6242BD1409ECF315D94D9BE377E342B40C06EEA286745C8AFA82)

### 示例2（设置默认后缀图标）

配置allowClose为true，显示后缀移除图标。

```
1. import { Chip, ChipSize, LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Column({ space: 10 }) {
8. Chip({
9. // 设置前缀图标属性。
10. prefixIcon: {
11. // 'app.media.chips'仅作示例，请替换为实际使用图片。
12. src: $r('app.media.chips'),
13. size: { width: 16, height: 16 },
14. fillColor: Color.Blue
15. },
16. // 设置文本属性。
17. label: {
18. text: '操作块',
19. fontSize: 12,
20. fontColor: Color.Blue,
21. fontFamily: 'HarmonyOS Sans',
22. labelMargin: { left: 20, right: 30 }
23. },
24. size: ChipSize.NORMAL,
25. allowClose: true,
26. closeOptions: {fontSize: 12},
27. enabled: true,
28. backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
29. borderRadius: $r('sys.float.ohos_id_corner_radius_button'),
30. minFontScale: 0.2,
31. maxFontScale: 2,
32. padding: {
33. start: LengthMetrics.vp(20),
34. end: LengthMetrics.vp(20)
35. },
36. fontSize: 12
37. })
38. }
39. }
40. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/v0vaNeFpR4a7fmsC-hZr2A/zh-cn_image_0000002558606960.png?HW-CC-KV=V1&HW-CC-Date=20260429T055256Z&HW-CC-Expire=86400&HW-CC-Sign=ADEE6D83EC2DC6A6F912F89EDB0C8EE6B0801EBABC6790860C8F6028DA54DA97)

### 示例3（不显示后缀图标）

配置allowClose为false，隐藏后缀移除图标。

```
1. import { Chip, ChipSize, LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Column({ space: 10 }) {
8. Chip({
9. // 设置前缀图标属性。
10. prefixIcon: {
11. // 'app.media.chips'仅作示例，请替换为实际使用图片。
12. src: $r('app.media.chips'),
13. size: { width: 16, height: 16 },
14. fillColor: Color.Blue
15. },
16. // 设置文本属性。
17. label: {
18. text: '操作块',
19. fontSize: 12,
20. fontColor: Color.Blue,
21. fontFamily: 'HarmonyOS Sans',
22. labelMargin: { left: 20, right: 30 }
23. },
24. size: ChipSize.SMALL,
25. allowClose: false,
26. enabled: true,
27. backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
28. borderRadius: $r('sys.float.ohos_id_corner_radius_button'),
29. onClose: () => {
30. console.info('chip on close');
31. },
32. minFontScale: 0.2,
33. maxFontScale: 2,
34. padding: {
35. start: LengthMetrics.vp(20),
36. end: LengthMetrics.vp(20)
37. },
38. fontSize: 12
39. })
40. }
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/W7MyWaRBRcCdrWOlFM505w/zh-cn_image_0000002589326487.png?HW-CC-KV=V1&HW-CC-Date=20260429T055256Z&HW-CC-Expire=86400&HW-CC-Sign=09897BE6B15CC32F91018FC0A8B55EADE059B5191414802A00612A8D544E116D)

### 示例4（激活态操作块）

该示例通过配置activated实现激活态操作块。

```
1. import { Chip, ChipSize } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State isActivated: boolean = false;

8. build() {
9. Column({ space: 10 }) {
10. Chip({
11. // 设置前缀图标属性。
12. prefixIcon: {
13. // 'app.media.chips'仅作示例，请替换为实际使用图片。
14. src: $r('app.media.chips'),
15. size: { width: 16, height: 16 },
16. fillColor: Color.Blue,
17. activatedFillColor: $r('sys.color.ohos_id_color_text_primary_contrary')
18. },
19. // 设置文本属性。
20. label: {
21. text: '操作块',
22. fontSize: 12,
23. fontColor: Color.Blue,
24. activatedFontColor: $r('sys.color.ohos_id_color_text_primary_contrary'),
25. fontFamily: 'HarmonyOS Sans',
26. labelMargin: { left: 20, right: 30 }
27. },
28. size: ChipSize.NORMAL,
29. allowClose: true,
30. enabled: true,
31. activated: this.isActivated,
32. backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
33. activatedBackgroundColor: $r('sys.color.ohos_id_color_emphasize'),
34. borderRadius: $r('sys.float.ohos_id_corner_radius_button'),
35. onClose: () => {
36. console.info('chip on close');
37. },
38. onClicked: () => {
39. console.info('chip on clicked');
40. }
41. })
42. // 点击“改变激活状态”，用于控制操作块的激活与关闭。
43. Button('改变激活状态')
44. .onClick(() => {
45. this.isActivated = !this.isActivated;
46. })
47. }
48. }
49. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/7cpGpCTQSuiLRxLwi1dfJQ/zh-cn_image_0000002589246429.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055256Z&HW-CC-Expire=86400&HW-CC-Sign=AFBDE2A943E4282A765CF7DBFCC1A9DF5E435481F6757371C9C8C1DF4A74A08A)

### 示例5（设置symbol类型图标）

Chip组件的前缀图标使用symbol类型资源展示。

```
1. import { Chip, ChipSize, SymbolGlyphModifier } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State isActivated: boolean = false;

8. build() {
9. Column({ space: 10 }) {
10. Chip({
11. // 设置前缀图标属性，symbol类型。
12. prefixSymbol: {
13. normal: new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontSize(16).fontColor([Color.Green]),
14. activated: new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontSize(16).fontColor([Color.Red]),
15. },
16. // 设置文本属性。
17. label: {
18. text: '操作块',
19. fontSize: 12,
20. fontColor: Color.Blue,
21. activatedFontColor: $r('sys.color.ohos_id_color_text_primary_contrary'),
22. fontFamily: 'HarmonyOS Sans',
23. labelMargin: { left: 20, right: 30 },
24. },
25. size: ChipSize.NORMAL,
26. allowClose: true,
27. enabled: true,
28. activated: this.isActivated,
29. backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
30. activatedBackgroundColor: $r('sys.color.ohos_id_color_emphasize'),
31. borderRadius: $r('sys.float.ohos_id_corner_radius_button'),
32. onClose: () => {
33. console.info('chip on close');
34. },
35. onClicked: () => {
36. console.info('chip on clicked');
37. }
38. })

40. Button('改变激活状态')
41. .onClick(() => {
42. this.isActivated = !this.isActivated;
43. })
44. }
45. }
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/xXKc8ldHSRq255Ig7X9ppg/zh-cn_image_0000002558766622.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055256Z&HW-CC-Expire=86400&HW-CC-Sign=2A0E5137D54C01630AE9CD8B372098A15E16625EBF3D94F82C7469C8A1C61043)

### 示例6（设置镜像效果）

配置direction实现Chip布局镜像化展示。

```
1. import { Chip, ChipSize, LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct ChipPage {
6. build() {
7. Column() {
8. Chip({
9. direction: Direction.Rtl,
10. // 设置前缀图标属性。
11. prefixIcon: {
12. // 'app.media.chips'仅作示例，请替换为实际使用图片。
13. src: $r('app.media.chips'),
14. size: { width: 16, height: 16 },
15. fillColor: Color.Red,
16. },
17. // 设置文本属性。
18. label: {
19. text: '操作块',
20. fontSize: 12,
21. fontColor: Color.Blue,
22. fontFamily: 'HarmonyOS Sans',
23. localizedLabelMargin: { start: LengthMetrics.vp(20), end: LengthMetrics.vp(20) },
24. },
25. // 设置后缀图标属性。
26. suffixIcon: {
27. // 'app.media.close'仅作示例，请替换为实际使用图片。
28. src: $r('app.media.close'),
29. size: { width: 16, height: 16 },
30. fillColor: Color.Red,
31. },
32. size: ChipSize.NORMAL,
33. allowClose: false,
34. enabled: true,
35. backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
36. borderRadius: $r('sys.float.ohos_id_corner_radius_button')
37. })
38. }
39. .justifyContent(FlexAlign.Center)
40. .width('100%')
41. .height('100%')
42. }
43. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/9KRM23GwTLKrZAbz7zOYxA/zh-cn_image_0000002558606962.png?HW-CC-KV=V1&HW-CC-Date=20260429T055256Z&HW-CC-Expire=86400&HW-CC-Sign=90CBE93BDED0855E78C6CA77A1807F340C5E0551E07EE3FA2ED1F9F11CDAFB7A)

### 示例7（Image类型无障碍朗读）

该示例代码实现Chip组件Image类型后缀图标的无障碍朗读功能，点击后缀图标播报“图标，按钮，新手提醒”。

```
1. import { Chip } from '@kit.ArkUI';

3. @Builder
4. function DefaultFunction(): void {
5. }

7. @Component
8. struct SectionGroup {
9. @Prop
10. @Require
11. title: ResourceStr;
12. @BuilderParam
13. @Require
14. content: () => void = DefaultFunction;

16. build() {
17. Column({ space: 4 }) {
18. Text(this.title)
19. .fontColor('#FF666666')
20. .fontSize(12)
21. Column({ space: 8 }) {
22. this.content()
23. }
24. }
25. .alignItems(HorizontalAlign.Start)
26. .width('100%')
27. }
28. }

30. @Component
31. struct SectionItem {
32. @Prop
33. @Require
34. title: ResourceStr;
35. @BuilderParam
36. @Require
37. content: () => void = DefaultFunction;

39. build() {
40. Column({ space: 12 }) {
41. Text(this.title)
42. this.content()
43. }
44. .backgroundColor('#FFFFFFFF')
45. .borderRadius(12)
46. .padding(12)
47. .width('100%')
48. }
49. }

51. @Entry
52. @Component
53. struct ChipExample2 {
54. @State activated: boolean = false;

56. build() {
57. NavDestination() {
58. Scroll() {
59. SectionGroup({ title: '后缀图标播报' }) {
60. SectionItem({ title: '自定义播报' }) {
61. Chip({
62. label: { text: '操作块' },
63. suffixIcon: {
64. src: $r('sys.media.ohos_ic_public_cut'),
65. accessibilityText: '图标', // 播报“图标，按钮，新手提醒”
66. accessibilityDescription: '新手提醒',
67. action: () => {
68. this.getUIContext().getPromptAction().showToast({
69. message: '后缀图标被点击！'
70. });
71. }
72. },
73. onClicked: () => {
74. this.getUIContext().getPromptAction().showToast({
75. message: '操作块被点击！'
76. });
77. }
78. })
79. }
80. }
81. }
82. }
83. }
84. }
```

### 示例8（symbol类型无障碍朗读）

该示例代码实现Chip组件symbol类型后缀图标的无障碍朗读功能，点击后缀图标播报“音乐，按钮，新手提醒”。

```
1. import { Chip, SymbolGlyphModifier } from '@kit.ArkUI';

3. @Builder
4. function DefaultFunction(): void {
5. }

7. @Component
8. struct SectionGroup {
9. @Prop
10. @Require
11. title: ResourceStr;
12. @BuilderParam
13. @Require
14. content: () => void = DefaultFunction;

16. build() {
17. Column({ space: 4 }) {
18. Text(this.title)
19. .fontColor('#FF666666')
20. .fontSize(12)
21. Column({ space: 8 }) {
22. this.content()
23. }
24. }
25. .alignItems(HorizontalAlign.Start)
26. .width('100%')
27. }
28. }

30. @Component
31. struct SectionItem {
32. @Prop
33. @Require
34. title: ResourceStr;
35. @BuilderParam
36. @Require
37. content: () => void = DefaultFunction;

39. build() {
40. Column({ space: 12 }) {
41. Text(this.title)
42. this.content()
43. }
44. .backgroundColor('#FFFFFFFF')
45. .borderRadius(12)
46. .padding(12)
47. .width('100%')
48. }
49. }

51. @Entry
52. @Component
53. struct ChipExample2 {
54. @State activated: boolean = false;

56. build() {
57. NavDestination() {
58. Scroll() {
59. SectionGroup({ title: '后缀Symbol播报' }) {
60. SectionItem({ title: 'activatedAccessibility' }) {
61. Chip({
62. label: { text: '操作块' },
63. activated: true,
64. suffixSymbol: {
65. activated: new SymbolGlyphModifier($r('sys.symbol.media_sound'))
66. .fontSize(72),
67. },
68. suffixSymbolOptions: {
69. activatedAccessibility: {
70. accessibilityText: '音乐', // 播报“音乐，按钮，新手提醒”
71. accessibilityDescription: '新手提醒'
72. },
73. action: () => {
74. this.getUIContext().getPromptAction().showToast({
75. message: '后缀Symbol被点击！'
76. });
77. }
78. },
79. onClicked: () => {
80. this.getUIContext().getPromptAction().showToast({
81. message: '操作块被点击！'
82. });
83. }
84. })
85. }

87. SectionItem({ title: 'normalAccessibility' }) {
88. Chip({
89. label: { text: '操作块' },
90. suffixSymbol: {
91. normal: new SymbolGlyphModifier($r('sys.symbol.media_sound'))
92. .fontSize(72),
93. },
94. suffixSymbolOptions: {
95. normalAccessibility: {
96. accessibilityText: '音乐', // 播报“音乐，按钮，新手提醒”
97. accessibilityDescription: '新手提醒'
98. },
99. action: () => {
100. this.getUIContext().getPromptAction().showToast({
101. message: '后缀Symbol被点击！'
102. });
103. }
104. },
105. onClicked: () => {
106. this.getUIContext().getPromptAction().showToast({
107. message: '操作块被点击！'
108. });
109. }
110. })
111. }
112. }
113. }
114. }
115. .padding({
116. top: 8,
117. bottom: 8,
118. left: 16,
119. right: 16,
120. })
121. }
122. }
```

### 示例9（Chip组件无障碍朗读）

示例展示Chip组件的无障碍属性设置，包括不同的accessibilitySelectedType类型和各种无障碍属性。

```
1. import { AccessibilitySelectedType, Chip, ChipSize } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct ChipAccessibilityExample {
6. @State clickedChipActivated: boolean = false;
7. @State checkedChipActivated: boolean = false;
8. @State selectedChipActivated: boolean = false;

10. build() {
11. Column({ space: 20 }) {
12. Text('Chip组件无障碍属性示例').fontSize(20).fontWeight(FontWeight.Bold)

14. // 点击型Chip - CLICKED类型
15. Chip({
16. label: { text: '点击型Chip' },
17. prefixIcon: {
18. src: $r('sys.media.ohos_app_icon'),
19. fillColor: Color.Blue
20. },
21. size: ChipSize.NORMAL,
22. accessibilitySelectedType: AccessibilitySelectedType.CLICKED, // 点击型
23. accessibilityDescription: '这是一个点击型Chip', // 整体无障碍描述
24. accessibilityLevel: 'yes', // 确保可被无障碍服务识别
25. closeOptions: {
26. accessibilityDescription: '删除此Chip，此操作无法撤销' // 为删除按钮提供详细说明
27. },
28. activated: this.clickedChipActivated,
29. onClicked: () => {
30. this.clickedChipActivated = !this.clickedChipActivated;
31. this.getUIContext().getPromptAction().showToast({ message: '点击型Chip被点击' });
32. },
33. onClose: () => {
34. this.getUIContext().getPromptAction().showToast({ message: '点击型Chip的关闭按钮被点击' });
35. }
36. })

38. // 复选型Chip - CHECKED类型
39. Chip({
40. label: { text: '复选型Chip' },
41. prefixIcon: {
42. src: $r('sys.media.ohos_app_icon'),
43. fillColor: Color.Green
44. },
45. size: ChipSize.NORMAL,
46. accessibilitySelectedType: AccessibilitySelectedType.CHECKED, // 复选型
47. accessibilityDescription: '这是一个复选型Chip', // 整体无障碍描述
48. activated: this.checkedChipActivated,
49. onClicked: () => {
50. this.checkedChipActivated = !this.checkedChipActivated;
51. this.getUIContext().getPromptAction().showToast({
52. message: this.checkedChipActivated ? '复选型Chip被选中' : '复选型Chip被取消选中'
53. });
54. }
55. })

57. // 单选型Chip - SELECTED类型
58. Chip({
59. label: { text: '单选型Chip' },
60. prefixIcon: {
61. src: $r('sys.media.ohos_app_icon'),
62. fillColor: Color.Red
63. },
64. size: ChipSize.NORMAL,
65. accessibilitySelectedType: AccessibilitySelectedType.SELECTED, // 单选型
66. accessibilityDescription: '这是一个单选型Chip', // 整体无障碍描述
67. activated: this.selectedChipActivated,
68. onClicked: () => {
69. this.selectedChipActivated = !this.selectedChipActivated;
70. this.getUIContext().getPromptAction().showToast({
71. message: this.selectedChipActivated ? '单选型Chip被选中' : '单选型Chip被取消选中'
72. });
73. }
74. })

76. // 无障碍级别设置示例
77. Chip({
78. label: { text: '无障碍级别为no' },
79. size: ChipSize.NORMAL,
80. accessibilityLevel: 'no', // 此Chip不能被无障碍服务识别
81. closeOptions: {
82. accessibilityLevel: 'no'
83. },
84. backgroundColor: '#CCCCCC',
85. onClicked: () => {
86. this.getUIContext().getPromptAction().showToast({ message: '此Chip无法被无障碍服务识别' });
87. }
88. })
89. }
90. .width('100%')
91. .padding(16)
92. }
93. }
```
