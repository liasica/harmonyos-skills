---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-chipgroup
title: ChipGroup
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > ChipGroup
category: harmonyos-references
scraped_at: 2026-04-28T08:02:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1545825304a9403d0a757c536522b7b467196b8757e72573326967df6df15399
---

ChipGroup组件提供操作块群组，用于文件或资源内容的分类等场景。

说明

该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ChipSize, ChipGroup } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## ChipGroup

PhonePC/2in1TabletTVWearable

```
1. ChipGroup({
2. items: ChipGroupItemOptions[],
3. itemStyle?: ChipItemStyle,
4. selectedIndexes?: Array<number>,
5. multiple?: boolean,
6. chipGroupSpace?: ChipGroupSpaceOptions,
7. chipGroupPadding?: ChipGroupPaddingOptions,
8. onChange?: Callback<Array<number>>,
9. suffix?: Callback<void>
10. })
```

**装饰器类型：**@Component

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| items | [ChipGroupItemOptions[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-chipgroup#chipgroupitemoptions) | 是 | @Require @Prop | 每个Chip的特定属性，参考[ChipGroupItemOptions[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-chipgroup#chipgroupitemoptions)类型。  若为undefined时，ChipGroup默认为空。 |
| itemStyle | [ChipItemStyle](ohos-arkui-advanced-chipgroup.md#chipitemstyle) | 否 | @Prop | Chip的style属性，如颜色，大小等，参考[ChipItemStyle](ohos-arkui-advanced-chipgroup.md#chipitemstyle)类型。  默认值：  { size: ChipSize.NORMAL, backgroundColor: $r('sys.color.ohos\_id\_color\_button\_normal'), fontColor: $r('sys.color.ohos\_id\_color\_text\_primary'), selectedFontColor: $r('sys.color.ohos\_id\_color\_text\_primary\_contrary'), selectedBackgroundColor: $r('sys.color.ohos\_id\_color\_emphasize') }  值为undefined时，按默认值处理。 |
| selectedIndexes | Array<number> | 否 | @Prop | 被选中Chip的索引。  默认值：[0]  值为undefined时，按默认值处理。 |
| multiple | boolean | 否 | @Prop | 是否选中多个Chip。  true：支持多个Chip选中；false：仅支持单个Chip选中。  默认值：false  值为undefined时，按默认值处理。 |
| chipGroupSpace | [ChipGroupSpaceOptions](ohos-arkui-advanced-chipgroup.md#chipgroupspaceoptions) | 否 | @Prop | 左右内边距及Chip之间间距。参考[ChipGroupSpaceOptions](ohos-arkui-advanced-chipgroup.md#chipgroupspaceoptions)类型。  默认值：{ itemSpace: 8, startSpace: 16, endSpace: 16 }  单位：vp  值为undefined时，按默认值处理。 |
| chipGroupPadding | [ChipGroupPaddingOptions](ohos-arkui-advanced-chipgroup.md#chipgrouppaddingoptions) | 否 | @Prop | 设置ChipGroup的上下内边距，以控制整体高度。类型为[ChipGroupPaddingOptions](ohos-arkui-advanced-chipgroup.md#chipgrouppaddingoptions)。  默认值：{ top: 14, bottom: 14 }  单位：vp  值为undefined时，按默认值处理。 |
| onChange | Callback<Array<number>> | 否 | - | Chip状态改变时的回调方法。  若为undefined，表示解绑事件。 |
| suffix | Callback<void> | 否 | @BuilderParam | 支持开发者自定义builder，如需在组件最右侧显示自定义内容可配置suffix属性，使用属性suffix需引用[IconGroupSuffix](ohos-arkui-advanced-chipgroup.md#icongroupsuffix)接口。  默认不传入时，没有suffix。  值为undefined时，没有suffix。 |

说明

1. 针对selectedIndexes和multiple接口，当multiple等于false时，如果没有传入selectedIndexes，默认是第一个Chip被选中，如果传入的selectedIndexes有一个以上的元素时，默认第一个索引的Chip被选中。
2. 使用suffix接口时，需引入IconGroupSuffix接口，若不传入，suffix将为空。
3. 图标填充色（fillColor和activedFillColor）的设置应与字体颜色（fontColor）保持一致。如果需要设置不同的颜色，可以在传入[ChipGroupSpaceOptions](#chipgroupspaceoptions)时使用prefixSymbol。

## ChipGroupItemOptions

PhonePC/2in1TabletTVWearable

ChipGroupItemOptions定义每个Chip的非通用属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| prefixIcon | [IconOptions](ohos-arkui-advanced-chipgroup.md#iconoptions) | 否 | 是 | 前缀Image图标属性。  默认值：没有前缀Image图标。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| prefixSymbol | [ChipSymbolGlyphOptions](ohos-arkui-advanced-chip.md#chipsymbolglyphoptions12) | 否 | 是 | 前缀SymbolGlyph图标属性。  默认值：没有前缀SymbolGlyph图标。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| label | [LabelOptions](ohos-arkui-advanced-chipgroup.md#labeloptions) | 否 | 否 | 文本属性。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| suffixIcon(deprecated) | [IconOptions](ohos-arkui-advanced-chipgroup.md#iconoptions) | 否 | 是 | 后缀Image图标属性。  默认值：不显示后缀Image图标。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **说明：** 从API version 12开始支持，从API version 14开始废弃，建议使用suffixImageIcon替代。 |
| suffixSymbol | [ChipSymbolGlyphOptions](ohos-arkui-advanced-chip.md#chipsymbolglyphoptions12) | 否 | 是 | 后缀SymbolGlyph图标属性。  默认值：不显示后缀SymbolGlyph图标。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| allowClose | boolean | 否 | 是 | 删除图标是否显示。  false表示删除图标不显示，true表示删除图标显示。  默认值：false  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| suffixImageIcon14+ | [SuffixImageIconOptions](ohos-arkui-advanced-chipgroup.md#suffiximageiconoptions14) | 否 | 是 | 后缀Image图标属性。  默认值：不显示后缀Image图标。  值为undefined时，按默认值处理。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| suffixSymbolOptions14+ | [ChipSuffixSymbolGlyphOptions](ohos-arkui-advanced-chip.md#chipsuffixsymbolglyphoptions14) | 否 | 是 | 后缀Symbol图标属性。  默认值：后缀Symbol图标无功能。  值为undefined时，按默认值处理。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| closeOptions14+ | [CloseOptions](ohos-arkui-advanced-chip.md#closeoptions14) | 否 | 是 | 默认删除图标的无障碍朗读功能属性。  值为undefined时，按默认值处理。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| accessibilityDescription14+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | ChipGroup中Chip项的无障碍描述。此描述用于向用户详细解释ChipGroup中Chip项，开发人员应为ChipGroup中Chip项的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的结果。特别是当这些结果无法仅从ChipGroup中Chip项的属性和无障碍文本中直接获知时。如果ChipGroup中Chip项同时具备文本属性和无障碍说明属性，当ChipGroup中Chip项被选中时，系统将首先播报ChipGroup中Chip项的文本属性，随后播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| accessibilityLevel14+ | string | 否 | 是 | ChipGroup中Chip项无障碍重要性。用于控制ChipGroup中Chip项是否可被无障碍辅助服务所识别。  支持的值为:  "auto"：ChipGroup中Chip项会转换为“yes”。  "yes"：ChipGroup中Chip项可被无障碍辅助服务所识别。  "no"：ChipGroup中Chip项不可被无障碍辅助服务所识别。  "no-hide-descendants"：ChipGroup中Chip项及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"  值为undefined时，按默认值处理。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |

说明

当传入suffixIcon参数时，allowClose不生效；未传入suffixIcon参数时，allowClose决定是否显示移除图标。

## ChipItemStyle

PhonePC/2in1TabletTVWearable

ChipItemStyle定义了Chip的共通属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size | [ChipSize](ohos-arkui-advanced-chip.md#chipsize) | [SizeOptions](ts-types.md#sizeoptions) | 否 | 是 | Chip尺寸，使用时需要从Chip组件引入ChipSize类型。  默认值：ChipSize.NORMAL或{ height: 0, width: 0 }  为undefined时，使用默认值。 |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | Chip背景颜色。  默认值：$r('sys.color.ohos\_id\_color\_button\_normal')  为undefined时，backgroundColor走默认值。 |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | Chip文字颜色。  默认值：$r('sys.color.ohos\_id\_color\_text\_primary')  为undefined时，fontColor走默认值。 |
| selectedFontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | Chip激活时的文字颜色。  默认值：$r('sys.color.ohos\_id\_color\_text\_primary\_contrary')  为undefined时，selectedFontColor走默认值。 |
| selectedBackgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | Chip激活时的背景颜色。  默认值：$r('sys.color.ohos\_id\_color\_emphasize')  为undefined时，selectedBackgroundColor走默认值。 |

说明

1. 操作块的大小有两种类型，一种是ChipSize，提供NORMAL和SMALL两种尺寸供选择；另一种是SizeOptions。
2. backgroundColor、selectedBackgroundColor传入undefined时，显示默认背景颜色，传入非法值时，背景色透明。

## ChipGroupSpaceOptions

PhonePC/2in1TabletTVWearable

ChipGroupSpaceOptions 定义了ChipGroup左右内边距，以及Chip与Chip之间的间距。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| itemSpace | string | number | 否 | 是 | Chip与Chip之间的间距（不支持百分比）。  取值范围：  number类型: ≥ 0 的数值（如：0、8、16、24.5）。  string类型: 单位为fp|vp|px|lpx且数值部分 ≥ 0 的字符串（如："8vp"、"16fp"、"12px"、"10lpx"）。  不支持: 负数、百分比单位、无效字符串格式。  默认值：8  单位：vp  为undefined时，itemSpace采取默认值。 |
| startSpace | [Length](ts-types.md#length) | 否 | 是 | 左侧内边距（不支持百分比）。  默认值：16  单位：vp  为undefined时，startSpace取默认值。 |
| endSpace | [Length](ts-types.md#length) | 否 | 是 | 右侧内边距（不支持百分比）。  默认值：16  单位：vp  如果为undefined，则使用默认值。 |

## ChipGroupPaddingOptions

PhonePC/2in1TabletTVWearable

ChipGroupPaddingOptions定义了ChipGroup的上下内边距，用于控制其整体高度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| top | [Length](ts-types.md#length) | 否 | 否 | ChipGroup的上方内边距（不支持百分比）。  默认值：14  单位：vp  为undefined时，top取默认值。 |
| bottom | [Length](ts-types.md#length) | 否 | 否 | ChipGroup的下方内边距（不支持百分比）。  默认值：14  单位：vp  为undefined时，bottom取默认值。 |

## SuffixImageIconOptions14+

PhonePC/2in1TabletTVWearable

后缀图标选项的类型。

继承自[IconOptions](ohos-arkui-advanced-chipgroup.md#iconoptions)。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| action | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 后缀图标响应事件。  值为undefined时，无后缀图标响应事件。 |
| accessibilityText | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 后缀图标的无障碍文本属性。用于为用户进一步说明后缀图标，开发人员可为后缀图标的该属性设置相对较详细的解释文本，帮助用户理解将要执行的操作。如帮助用户理解将要执行的操作可能导致什么后果，尤其是当这些后果无法从后缀图标本身属性与无障碍文本中了解到时。若后缀图标既拥有文本属性又拥有无障碍说明属性，则后缀图标被选中时，先播报后缀图标的文本属性，再播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。 |
| accessibilityDescription | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 后缀图标的无障碍描述。此描述用于向用户详细解释后缀图标，开发人员应为后缀图标的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从后缀图标的属性和无障碍文本中直接获知时。如果后缀图标同时具备文本属性和无障碍说明属性，当后缀图标被选中时，系统将首先播报后缀图标的文本属性，随后播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。 |
| accessibilityLevel | string | 否 | 是 | 后缀图标无障碍重要性。用于控制后缀图标是否可被无障碍辅助服务所识别。  支持的值为:  "auto"：后缀图标存在action时转化为“yes”，不存在action时，转化为“no”。  "yes"：后缀图标可被无障碍辅助服务所识别。  "no"：后缀图标不可被无障碍辅助服务所识别。  "no-hide-descendants"：后缀图标及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"  值为undefined时，按默认值处理。 |

## SymbolItemOptions14+

PhonePC/2in1TabletTVWearable

ChipGroup的尾部图标选项类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| symbol | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 否 | 尾部图标的SymbolGlyphModifier配置对象，用于设置图标的显示样式、渲染模式等。 |
| action | [VoidCallback](ts-types.md#voidcallback12) | 否 | 否 | 尾部图标响应事件。 |
| accessibilityText | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 尾部图标的无障碍文本属性。用于为用户进一步说明尾部图标，开发人员可为尾部图标的该属性设置相对较详细的解释文本，帮助用户理解将要执行的操作。如帮助用户理解将要执行的操作可能导致什么后果，尤其是当这些后果无法从尾部图标本身属性与无障碍文本中了解到时。若尾部图标既拥有文本属性又拥有无障碍说明属性，则尾部图标被选中时，先播报尾部图标的文本属性，再播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。 |
| accessibilityDescription | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 尾部图标的无障碍描述。此描述用于向用户详细解释尾部图标，开发人员应为尾部图标的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从尾部图标的属性和无障碍文本中直接获知时。如果尾部图标同时具备文本属性和无障碍说明属性，当尾部图标被选中时，系统将首先播报尾部图标的文本属性，随后播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。 |
| accessibilityLevel | string | 否 | 是 | 尾部图标无障碍重要性。用于控制尾部图标是否可被无障碍辅助服务所识别。  支持的值为:  "auto"：尾部图标转化为“yes”。  "yes"：尾部图标可被无障碍辅助服务所识别。  "no"：尾部图标不可被无障碍辅助服务所识别。  "no-hide-descendants"：尾部图标及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"。  值为undefined时，按默认值处理。 |

## IconGroupSuffix

PhonePC/2in1TabletTVWearable

```
1. IconGroupSuffix({items: Array<IconItemOptions | SymbolGlyphModifier | SymbolItemOptions>})
```

**装饰器类型：**@Component

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| items | Array<[IconItemOptions](ohos-arkui-advanced-chipgroup.md#iconitemoptions) | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) |  [SymbolItemOptions](ohos-arkui-advanced-chipgroup.md#symbolitemoptions14)> | 是 | @Require @Prop | 尾部区域显示的自定义项数组，支持IconItemOptions（Image图标）、SymbolGlyphModifier（Symbol图标）或SymbolItemOptions（Symbol图标配置）类型。 |

说明

传参SymbolGlyphModifier时，不支持使用symbolEffect修改动效类型和[effectStrategy](ts-basic-components-symbolglyph.md#effectstrategy)设置动效。

## IconItemOptions

PhonePC/2in1TabletTVWearable

定义了尾部builder接口，针对背板大小及颜色设置限制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [IconOptions](ohos-arkui-advanced-chipgroup.md#iconoptions) | 否 | 否 | 自定义Builder icon。  Chip大小是ChipSize.SMALL时，suffix默认值：{width: 16,height: 16}。  Chip大小是ChipSize.NORMAL时，suffix默认值：{width: 24,height: 24}。  如果想动态修改size，那么必须在引入[IconGroupSuffix](ohos-arkui-advanced-chipgroup.md#icongroupsuffix)时，使用[SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier)类型。  值为undefined时，按默认值处理。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| action | Callback<void> | 否 | 否 | 自定义Builder items 的Callback  为undefined时，表示解绑事件。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| accessibilityText14+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 尾部图标无障碍文本属性。用于为用户进一步说明尾部图标，开发人员可为尾部图标的该属性设置相对较详细的解释文本，帮助用户理解将要执行的操作。如帮助用户理解将要执行的操作可能导致什么后果，尤其是当这些后果无法从尾部图标本身属性与无障碍文本中了解到时。若尾部图标既拥有文本属性又拥有无障碍说明属性，则尾部图标被选中时，先播报尾部图标的文本属性，再播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| accessibilityDescription14+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 尾部图标无障碍描述。此描述用于向用户详细解释尾部图标，开发人员应为尾部图标的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从尾部图标的属性和无障碍文本中直接获知时。如果尾部图标同时具备文本属性和无障碍说明属性，当尾部图标被选中时，系统将首先播报尾部图标的文本属性，随后播报无障碍说明属性的内容。  默认值：空字符串。  值为undefined时，按默认值处理。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| accessibilityLevel14+ | string | 否 | 是 | 尾部图标无障碍重要性。用于控制尾部图标是否可被无障碍辅助服务所识别。  支持的值为:  "auto"：尾部图标转化为“yes”。  "yes"：尾部图标可被无障碍辅助服务所识别。  "no"：尾部图标不可被无障碍辅助服务所识别。  "no-hide-descendants"：尾部图标及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"  值为undefined时，按默认值处理。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |

## IconOptions

PhonePC/2in1TabletTVWearable

IconOptions定义图标的共通属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| src | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 图标图片或图片地址引用请参考[Image](ts-basic-components-image.md#image-1)。 |
| size | [SizeOptions](ts-types.md#sizeoptions) | 否 | 是 | 图标大小，不支持百分比。  默认值：undefined |

## LabelOptions

PhonePC/2in1TabletTVWearable

Label定义图标属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | string | 否 | 否 | 文本属性 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（无最右侧的builder）

该示例实现了在没有最右侧builder时的效果。

```
1. import { ChipSize, ChipGroup } from '@kit.ArkUI';

3. @Entry
4. @Preview
5. @Component
6. struct Index {
7. @State selected_index: Array<number> = [0, 1, 2, 3, 4, 5, 6];

9. build() {
10. Column() {
11. ChipGroup({
12. // items内每个对象设置的都是每个Chip的特定属性。
13. items: [
14. {
15. // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
16. prefixIcon: { src: $r('app.media.icon') },
17. label: { text: '操作块1' },
18. suffixIcon: { src: $r('sys.media.ohos_ic_public_cut') },
19. allowClose: false
20. },
21. {
22. prefixIcon: { src: $r('sys.media.ohos_ic_public_copy') },
23. label: { text: '操作块2' },
24. allowClose: true
25. },
26. {
27. prefixIcon: { src: $r('sys.media.ohos_ic_public_clock') },
28. label: { text: '操作块3' },
29. allowClose: true
30. },
31. {
32. prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') },
33. label: { text: '操作块4' },
34. allowClose: true
35. },
36. {
37. prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_mirror') },
38. label: { text: '操作块5' },
39. allowClose: true
40. },
41. {
42. prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') },
43. label: { text: '操作块6' },
44. allowClose: true
45. },
46. ],
47. // 设置Chip的style属性。
48. itemStyle: {
49. size: ChipSize.SMALL,
50. backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
51. fontColor: $r('sys.color.ohos_id_color_text_primary'),
52. selectedBackgroundColor: $r('sys.color.ohos_id_color_emphasize'),
53. selectedFontColor: $r('sys.color.ohos_id_color_text_primary_contrary'),
54. },
55. selectedIndexes: this.selected_index,
56. multiple: false,
57. chipGroupSpace: { itemSpace: 8, endSpace: 0 },
58. chipGroupPadding: { top: 10, bottom: 10 },
59. onChange: (activatedChipsIndex: Array<number>) => {
60. console.info('chips on clicked, activated index ' + activatedChipsIndex);
61. },
62. })
63. }
64. }
65. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/zbjiyZuzRMKOyZzaBSgztw/zh-cn_image_0000002552800448.png?HW-CC-KV=V1&HW-CC-Date=20260428T000233Z&HW-CC-Expire=86400&HW-CC-Sign=7A203E9C0B30889BCFF2C878F2FFDE473310C31C950868D3099EF08A3E6AEF03)

### 示例2（有最右侧的builder）

通过配置suffix实现最右侧的自定义组件效果。

```
1. import { ChipSize, ChipGroup, IconGroupSuffix } from '@kit.ArkUI';

3. @Entry
4. @Preview
5. @Component
6. struct Index {
7. @State selected_index: Array<number> = [0, 1, 2, 3, 4, 5, 6];
8. @State selected_state: boolean = true;

10. @LocalBuilder
11. ChipGroupSuffix(): void {
12. // 开发者通过引用IconGroupSuffix，实现组件最右侧的自定义组件效果。
13. IconGroupSuffix({
14. items: [{
15. icon: { src: $r('sys.media.ohos_ic_public_search_filled'), size: { width: 36, height: 36 } },
16. action: () => {
17. if (this.selected_state == false) {
18. this.selected_index = [0, 1, 2, 3, 4, 5, 6];
19. this.selected_state = true;
20. } else {
21. this.selected_index = [];
22. this.selected_state = false;
23. }
24. }
25. }
26. ]
27. })
28. }

30. build() {
31. Column() {
32. ChipGroup({
33. // items内每个对象设置的都是每个Chip的特定属性。
34. items: [
35. {
36. // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
37. prefixIcon: { src: $r('app.media.icon') },
38. label: { text: '操作块1' },
39. suffixIcon: { src: $r('sys.media.ohos_ic_public_cut') },
40. allowClose: false
41. },
42. {
43. prefixIcon: { src: $r('sys.media.ohos_ic_public_copy') },
44. label: { text: '操作块2' },
45. allowClose: true
46. },
47. {
48. prefixIcon: { src: $r('sys.media.ohos_ic_public_clock') },
49. label: { text: '操作块3' },
50. allowClose: true
51. },
52. {
53. prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') },
54. label: { text: '操作块4' },
55. allowClose: true
56. },
57. {
58. prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_mirror') },
59. label: { text: '操作块5' },
60. allowClose: true
61. },
62. {
63. prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') },
64. label: { text: '操作块6' },
65. allowClose: true
66. },
67. ],
68. // 设置Chip的style属性。
69. itemStyle: {
70. size: ChipSize.NORMAL,
71. backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
72. fontColor: $r('sys.color.ohos_id_color_text_primary'),
73. selectedBackgroundColor: $r('sys.color.ohos_id_color_emphasize'),
74. selectedFontColor: $r('sys.color.ohos_id_color_text_primary_contrary'),
75. },
76. selectedIndexes: this.selected_index,
77. multiple: true,
78. chipGroupSpace: { itemSpace: 8, endSpace: 0 },
79. chipGroupPadding: { top: 10, bottom: 10 },
80. onChange: (activatedChipsIndex: Array<number>) => {
81. console.info('chips on clicked, activated index ' + activatedChipsIndex);
82. },
83. // 自定义builder，在组件最右侧显示自定义的内容。
84. suffix: this.ChipGroupSuffix
85. })
86. }
87. }
88. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/kEsfP3G8TViaYlzQ7dK6Lw/zh-cn_image_0000002583440143.png?HW-CC-KV=V1&HW-CC-Date=20260428T000233Z&HW-CC-Expire=86400&HW-CC-Sign=2198DB7A843072FDEC2221D7C889F9C022427FE8D167E16DCF670A98F7AA8EED)

### 示例3（设置Symbol类型图标）

该示例实现了IconGroupSuffix和ChipGroup传入SymbolGlyph资源。

```
1. import { ChipSize, ChipGroup, IconGroupSuffix, SymbolGlyphModifier } from '@kit.ArkUI';

3. @Entry
4. @Preview
5. @Component
6. struct Index {
7. @State selected_index: Array<number> = [0, 1, 2, 3, 4, 5, 6];
8. @State selected_state: boolean = true;
9. @State prefixModifierNormal: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_star'));
10. @State prefixModifierActivated: SymbolGlyphModifier =
11. new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontColor([Color.Red]);
12. @State suffixModifierNormal: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_wifi'));
13. @State suffixModifierActivated: SymbolGlyphModifier =
14. new SymbolGlyphModifier($r('sys.symbol.ohos_wifi')).fontColor([Color.Red]);

16. @LocalBuilder
17. ChipGroupSuffix(): void {
18. // 开发者通过引用IconGroupSuffix，实现组件最右侧的自定义组件效果。
19. IconGroupSuffix({
20. items: [
21. new SymbolGlyphModifier($r('sys.symbol.magnifyingglass'))
22. .onClick(() => {
23. if (this.selected_state == false) {
24. this.selected_index = [0, 1, 2, 3, 4, 5, 6];
25. this.selected_state = true;
26. } else {
27. this.selected_index = [];
28. this.selected_state = false;
29. }
30. })
31. ]
32. })
33. }

35. build() {
36. Column() {
37. ChipGroup({
38. // items内每个对象设置的都是每个Chip的特定属性。
39. items: [
40. {
41. prefixSymbol: { normal: this.prefixModifierNormal, activated: this.prefixModifierActivated },
42. label: { text: '操作块1' },
43. suffixSymbol: { normal: this.suffixModifierNormal, activated: this.suffixModifierActivated },
44. allowClose: false,
45. },
46. {
47. prefixSymbol: { normal: this.prefixModifierNormal, activated: this.prefixModifierActivated },
48. label: { text: '操作块2' },
49. allowClose: true,
50. },
51. {
52. prefixIcon: { src: $r('sys.media.ohos_ic_public_clock') },
53. label: { text: '操作块3' },
54. allowClose: true,
55. },
56. {
57. prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') },
58. label: { text: '操作块4' },
59. allowClose: true,
60. },
61. {
62. prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_mirror') },
63. label: { text: '操作块5' },
64. allowClose: true,
65. },
66. {
67. prefixIcon: { src: $r('sys.media.ohos_ic_public_cast_stream') },
68. label: { text: '操作块6' },
69. allowClose: true,
70. },
71. ],
72. // 设置Chip的style属性。
73. itemStyle: {
74. size: ChipSize.NORMAL,
75. backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
76. fontColor: $r('sys.color.ohos_id_color_text_primary'),
77. selectedBackgroundColor: $r('sys.color.ohos_id_color_emphasize'),
78. selectedFontColor: $r('sys.color.ohos_id_color_text_primary_contrary'),
79. },
80. selectedIndexes: this.selected_index,
81. multiple: true,
82. chipGroupSpace: { itemSpace: 8, endSpace: 0 },
83. chipGroupPadding: { top: 10, bottom: 10 },
84. onChange: (activatedChipsIndex: Array<number>) => {
85. console.info('chips on clicked, activated index ' + activatedChipsIndex);
86. },
87. // 自定义builder，在组件最右侧显示自定义的内容。
88. suffix: this.ChipGroupSuffix
89. })
90. }
91. }
92. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/kJXgjkkxQ0eQ0Iq-TTgfBQ/zh-cn_image_0000002552960098.png?HW-CC-KV=V1&HW-CC-Date=20260428T000233Z&HW-CC-Expire=86400&HW-CC-Sign=9B7CDF5281BF2DA48F6F0818D91717989048210EE2BAFCFBA79CB46FF1151938)

### 示例4（单选时无障碍朗读）

该示例实现ChipGroup在单选模式下，有后缀区域和无后缀区域的屏幕朗读功能，具体播报内容为accessibilityText属性中的内容。

```
1. import { ChipGroup, IconGroupSuffix, SymbolGlyphModifier } from '@kit.ArkUI';

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
53. export struct ChipGroupExample2 {
54. @LocalBuilder
55. Suffix() {
56. IconGroupSuffix({
57. items: [
58. {
59. icon: { src: $r('sys.media.ohos_ic_public_more'), },
60. accessibilityText: '更多', // 播报“更多，按钮，新手提醒”
61. accessibilityDescription: '新手提醒',
62. action: () => {
63. this.getUIContext().getPromptAction().showToast({
64. message: '更多按钮被点击！'
65. });
66. }
67. },
68. {
69. symbol: new SymbolGlyphModifier($r('sys.symbol.more')),
70. accessibilityText: '更多', // 播报“更多，按钮，新手提醒”
71. accessibilityDescription: '新手提醒',
72. action: () => {
73. this.getUIContext().getPromptAction().showToast({
74. message: '更多按钮被点击！'
75. });
76. }
77. },
78. {
79. icon: { src: $r('sys.media.ohos_ic_public_more'), },
80. accessibilityText: '更多', // accessibilityLevel属性设置为“no”时，accessibilityText属性和accessibilityDescription属性无效
81. accessibilityDescription: '新手提醒',
82. accessibilityLevel: 'no',
83. action: () => {
84. this.getUIContext().getPromptAction().showToast({
85. message: '更多按钮被点击！'
86. });
87. }
88. }
89. ]
90. })
91. }

93. build() {
94. NavDestination() {
95. Scroll() {
96. Column({ space: 12 }) {
97. SectionGroup({ title: '可用的' }) {
98. SectionItem({ title: '单选 无后缀区域' }) {
99. ChipGroup({
100. items: [
101. {
102. prefixIcon: {
103. src: $r('app.media.startIcon')
104. },
105. label: { text: '选项1' },
106. suffixImageIcon: {
107. src: $r('sys.media.save_button_picture'),
108. accessibilityText: '保存', // 播报“保存，按钮”
109. action: () => {
110. this.getUIContext().getPromptAction().showToast({
111. message: '后缀图标被点击！'
112. });
113. },
114. }
115. },
116. {
117. label: { text: '选项2' },
118. suffixSymbol: {
119. normal: new SymbolGlyphModifier($r('sys.symbol.save')),
120. activated: new SymbolGlyphModifier($r('sys.symbol.save'))
121. },
122. suffixSymbolOptions: {
123. normalAccessibility: {
124. accessibilityText: '保存' // 播报“保存，按钮”
125. },
126. action: () => {
127. this.getUIContext().getPromptAction().showToast({
128. message: '后缀图标被点击！'
129. });
130. }
131. }
132. },
133. {
134. label: { text: '选项3' },
135. suffixIcon: { src: $r('sys.media.save_button_picture'), }
136. },
137. { label: { text: '选项4' } },
138. { label: { text: '选项5' } },
139. { label: { text: '选项6' } },
140. { label: { text: '选项7' } },
141. { label: { text: '选项8' } },
142. { label: { text: '选项9' } },
143. ]
144. })
145. }

147. SectionItem({ title: '单选 有后缀区域' }) {
148. ChipGroup({
149. items: [
150. { label: { text: '选项1' } },
151. { label: { text: '选项2' } },
152. { label: { text: '选项3' } },
153. { label: { text: '选项4' } },
154. { label: { text: '选项5' } },
155. { label: { text: '选项6' } },
156. { label: { text: '选项7' } },
157. { label: { text: '选项8' } },
158. { label: { text: '选项9' } },
159. ],
160. suffix: this.Suffix,
161. })
162. }
163. }
164. }
165. }
166. .padding({
167. top: 8,
168. bottom: 8,
169. left: 16,
170. right: 16,
171. })
172. }
173. .title('基础用法')
174. .backgroundColor('#F1F3F5')
175. }
176. }
```

### 示例5（多选时无障碍朗读）

该示例实现了ChipGroup在多选模式下，有后缀区域和无后缀区域的屏幕朗读功能，具体播报内容为accessibilityText属性中的内容。

```
1. import { ChipGroup, IconGroupSuffix, SymbolGlyphModifier } from '@kit.ArkUI';

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
53. export struct ChipGroupExample2 {
54. @LocalBuilder
55. Suffix() {
56. IconGroupSuffix({
57. items: [
58. {
59. icon: { src: $r('sys.media.ohos_ic_public_more'), },
60. accessibilityText: '更多', // 播报“更多，按钮，新手提醒”
61. accessibilityDescription: '新手提醒',
62. action: () => {
63. this.getUIContext().getPromptAction().showToast({
64. message: '更多按钮被点击！'
65. });
66. }
67. },
68. {
69. symbol: new SymbolGlyphModifier($r('sys.symbol.more')),
70. accessibilityText: '更多', // 播报“更多，按钮，新手提醒”
71. accessibilityDescription: '新手提醒',
72. action: () => {
73. this.getUIContext().getPromptAction().showToast({
74. message: '更多按钮被点击！'
75. });
76. }
77. },
78. {
79. icon: { src: $r('sys.media.ohos_ic_public_more'), },
80. accessibilityText: '更多', // accessibilityLevel属性设置为“no”时，accessibilityText属性和accessibilityDescription属性无效
81. accessibilityDescription: '新手提醒',
82. accessibilityLevel: 'no',
83. action: () => {
84. this.getUIContext().getPromptAction().showToast({
85. message: '更多按钮被点击！'
86. });
87. }
88. }
89. ]
90. })
91. }

93. build() {
94. NavDestination() {
95. Scroll() {
96. Column({ space: 12 }) {
97. SectionGroup({ title: '可用的' }) {
98. SectionItem({ title: '多选 无后缀区域' }) {
99. ChipGroup({
100. items: [
101. { label: { text: '选项1' } },
102. { label: { text: '选项2' } },
103. { label: { text: '选项3' } },
104. { label: { text: '选项4' } },
105. { label: { text: '选项5' } },
106. { label: { text: '选项6' } },
107. { label: { text: '选项7' } },
108. { label: { text: '选项8' } },
109. { label: { text: '选项9' } },
110. ],
111. multiple: true
112. })
113. }

115. SectionItem({ title: '多选 有后缀区域' }) {
116. ChipGroup({
117. items: [
118. { label: { text: '选项1' } },
119. { label: { text: '选项2' } },
120. { label: { text: '选项3' } },
121. { label: { text: '选项4' } },
122. { label: { text: '选项5' } },
123. { label: { text: '选项6' } },
124. { label: { text: '选项7' } },
125. { label: { text: '选项8' } },
126. { label: { text: '选项9' } },
127. ],
128. suffix: this.Suffix,
129. multiple: true,
130. })
131. }
132. }
133. }
134. }
135. .padding({
136. top: 8,
137. bottom: 8,
138. left: 16,
139. right: 16,
140. })
141. }
142. .title('基础用法')
143. .backgroundColor('#F1F3F5')
144. }
145. }
```
