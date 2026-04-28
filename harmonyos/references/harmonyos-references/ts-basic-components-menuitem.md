---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-menuitem
title: MenuItem
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 菜单 > MenuItem
category: harmonyos-references
scraped_at: 2026-04-28T08:02:15+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:8a79276487244d67070490c23e9ccc9074f1b3286bf0af011686e279bbecbd46
---

用来展示菜单中具体的菜单选项。

说明

该组件从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

MenuItem(value?: MenuItemOptions | CustomBuilder)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [MenuItemOptions](ts-basic-components-menuitem.md#menuitemoptions对象说明) | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 包含设置MenuItem的各项信息。 如果不传该参数，则创建空的MenuItem对象。 |

## MenuItemOptions对象说明

PhonePC/2in1TabletTVWearable

Menu中具体item菜单项信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| startIcon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | MenuItem的起始图标。不支持Symbol图标。使用Symbol图标时，须使用symbolStartIcon。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| content | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | MenuItem的内容。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| endIcon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | MenuItem的末尾图标。不支持Symbol图标。使用Symbol图标时，须使用symbolEndIcon。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| labelInfo | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | MenuItem结束的标签信息，如快捷方式Ctrl+C等。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| builder | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 是 | 用于构建二级菜单。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| symbolStartIcon12+ | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md) | 否 | 是 | MenuItem起始的Symbol图标。配置该项时，原先startIcon图标不显示。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| symbolEndIcon12+ | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md) | 否 | 是 | MenuItem末尾的Symbol图标。配置该项时，原先endIcon图标不显示。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### selected

PhonePC/2in1TabletTVWearable

selected(value: boolean)

设置菜单项是否选中。

从API version 10开始，该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。

从API version 18开始，该参数支持[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 菜单项是否选中。  true：菜单项被选中；false：菜单项不被选中。  默认值：false |

### selectIcon

PhonePC/2in1TabletTVWearable

selectIcon(value: boolean | ResourceStr | SymbolGlyphModifier)

设置当菜单项被选中时，是否显示被选中的图标。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | [ResourceStr](ts-types.md#resourcestr)10+| [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md)12+ | 是 | 菜单项被选中时，是否显示被选中的图标。  true：显示默认的对勾图标；false：不显示图标。  ResourceStr：显示指定的图标。  SymbolGlyphModifier：显示指定的HMSymbol图标。  默认值：false |

### contentFont10+

PhonePC/2in1TabletTVWearable

contentFont(value: Font)

设置菜单项中内容信息的字体样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](ts-types.md#font) | 是 | 菜单项中内容信息的字体样式。 |

### contentFontColor10+

PhonePC/2in1TabletTVWearable

contentFontColor(value: ResourceColor)

设置菜单项中内容信息的字体颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 菜单项中内容信息的字体颜色。  默认值：'#E5000000' |

### labelFont10+

PhonePC/2in1TabletTVWearable

labelFont(value: Font)

设置菜单项中标签信息的字体样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](ts-types.md#font) | 是 | 菜单项中标签信息的字体样式。 |

### labelFontColor10+

PhonePC/2in1TabletTVWearable

labelFontColor(value: ResourceColor)

设置菜单项中标签信息的字体颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 菜单项中标签信息的字体颜色。  默认值：'#99000000' |

## 事件

PhonePC/2in1TabletTVWearable

### onChange

PhonePC/2in1TabletTVWearable

onChange(callback: (selected: boolean) => void)

当选中状态发生变化时，触发该回调。只有手动触发且MenuItem状态改变时才会触发onChange回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selected | boolean | 是 | 选中状态发生变化时，触发该回调。  true：未选中切换为选中；false：选中切换为未选中。 |

## 示例

PhonePC/2in1TabletTVWearable

详见[Menu组件示例](ts-basic-components-menu.md#示例)。
