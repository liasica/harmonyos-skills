---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-select
title: Select
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 按钮与选择 > Select
category: harmonyos-references
scraped_at: 2026-04-29T13:52:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fc361b02b3417d9faaea68c9cfb6a547fbb8fbb5775692c0c4d89e13f21dccbb
---

提供下拉选择菜单，让用户在多个选项间选择。

说明

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

Select(options: Array<SelectOption>)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | Array<[SelectOption](ts-basic-components-select.md#selectoption对象说明)> | 是 | 设置下拉选项。 |

## SelectOption对象说明

PhonePC/2in1TabletTVWearable

下拉菜单项的信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 下拉选项内容。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| icon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 下拉选项图片。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| symbolIcon12+ | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md) | 否 | 是 | 下拉选项Symbol图片。  symbolIcon优先级高于icon。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### selected

PhonePC/2in1TabletTVWearable

selected(value: number | Resource)

设置下拉菜单初始选项的索引，第一项的索引为0。当不设置selected属性或设置为异常值时，默认选中值为-1，菜单项不选中；当设置为undefined、null时，选中第一项。

从API version 10开始，该属性支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。

从API version 18开始，该属性支持[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [Resource](ts-types.md#resource)11+ | 是 | 下拉菜单初始选项的索引，索引值从0开始。 |

### selected18+

PhonePC/2in1TabletTVWearable

selected(numCount: Optional<number | Resource>)

设置下拉菜单初始选项的索引，第一项的索引为0。当不设置selected属性或设置异常值时，默认选择值为-1，菜单项不选中；当设置为undefined、null时，选中第一项。

该属性支持[$$](../harmonyos-guides/arkts-two-way-sync.md)、[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| numCount | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number | [Resource](ts-types.md#resource)> | 是 | 下拉菜单初始选项的索引。  当numCount的值为undefined时，选中第一项。 |

### value

PhonePC/2in1TabletTVWearable

value(value: ResourceStr)

设置下拉按钮的文本内容。选中菜单项后，按钮文本将自动更新为选中的菜单项文本。

从API version 10开始，该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。

从API version 18开始，该参数支持[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr)11+ | 是 | 下拉按钮本身的文本内容。  **说明：** 文本长度大于列宽时，文本被截断。 |

### value18+

PhonePC/2in1TabletTVWearable

value(resStr: Optional<ResourceStr>)

设置下拉按钮的文本内容。选中菜单项后，按钮文本将自动更新为选中的菜单项文本。与[value](ts-basic-components-select.md#value)相比，resStr参数新增了对undefined类型的支持。

该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)、[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resStr | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ResourceStr](ts-types.md#resourcestr)> | 是 | 下拉按钮本身的文本内容。  当resStr的值为undefined时维持上次取值。 |

### controlSize12+

PhonePC/2in1TabletTVWearable

controlSize(value: ControlSize)

设置Select组件的尺寸。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ControlSize](ts-basic-components-button.md#controlsize11枚举说明)11+ | 是 | Select组件的尺寸。  默认值：ControlSize.NORMAL |

controlSize、width、height接口作用优先级：

1）如果开发者只设置了width和height，当文字大小设置为较大的值时，文字会超出组件大小，超出的部分以省略号的方式显示；

2）如果开发者只设置了controlSize，没有设置width和height，组件宽高自适应文字，文字不超出组件，并设置最小宽度minWidth和最小高度minHeight；

3）如果同时设置了controlSize、width、height接口，width和height设置的值生效，但如果width和height设置的值小于controlSize设置的最小宽度minWidth和最小高度minHeight，width和height设置的值不生效，宽高仍保持controlSize设置的最小宽度minWidth和最小高度minHeight。

### controlSize18+

PhonePC/2in1TabletTVWearable

controlSize(size: Optional<ControlSize>)

设置Select组件的尺寸。与[controlSize](ts-basic-components-select.md#controlsize12)12+相比，size参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ControlSize](ts-basic-components-button.md#controlsize11枚举说明)> | 是 | Select组件的尺寸。  当size的值为undefined时，默认值为ControlSize.NORMAL。 |

controlSize、width、height接口作用优先级：

1）如果开发者只设置了width和height，当文字大小设置的是比较大的值的时候，文字超出组件大小，超出的部分以省略号的方式显示；

2）如果开发者只设置了controlSize，没有设置width和height，组件宽高自适应文字，文字不超出组件，并设置最小宽度minWidth和最小高度minHeight；

3）如果controlSize、width、height接口都设置了，width和height设置的值生效，但如果width和height设置的值小于controlSize设置的最小宽度minWidth和最小高度minHeight，width和height设置的值不生效，宽高仍保持controlSize设置的最小宽度minWidth和最小高度minHeight。

### menuItemContentModifier12+

PhonePC/2in1TabletTVWearable

menuItemContentModifier(modifier: ContentModifier<MenuItemConfiguration>)

定制Select下拉菜单项内容区的方法。在应用了menuItemContentModifier后，下拉菜单的内容将完全由开发者自定义，此时为Select组件设置的分割线、选项颜色及下拉菜单的字体颜色等属性将不再生效。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](ts-universal-attributes-content-modifier.md#contentmodifiert)[<MenuItemConfiguration>](ts-basic-components-select.md#menuitemconfiguration12对象说明) | 是 | 在Select组件上，定制下拉菜单项内容区的方法。  modifier：内容修改器，开发者需要自定义class实现ContentModifier接口。 |

### menuItemContentModifier18+

PhonePC/2in1TabletTVWearable

menuItemContentModifier(modifier: Optional<ContentModifier<MenuItemConfiguration>>)

定制Select下拉菜单项内容区的方法。与[menuItemContentModifier](ts-basic-components-select.md#menuitemcontentmodifier12)12+相比，modifier参数新增了对undefined类型的支持。在应用了menuItemContentModifier后，下拉菜单的内容将完全由开发者自定义，此时为Select组件设置的分割线、选项颜色及下拉菜单的字体颜色等属性将不再生效。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ContentModifier](ts-universal-attributes-content-modifier.md#contentmodifiert)[<MenuItemConfiguration>](ts-basic-components-select.md#menuitemconfiguration12对象说明)> | 是 | 在Select组件上，定制下拉菜单项内容区的方法。  modifier：内容修改器，开发者需要自定义class实现ContentModifier接口。  当modifier的值为undefined时，不使用内容修改器。 |

### divider12+

PhonePC/2in1TabletTVWearable

divider(options: Optional<DividerOptions> | null)

设置分割线样式，不设置该属性则按“默认值”展示分割线。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[DividerOptions](ts-basic-components-textpicker.md#divideroptions12对象说明)> | null | 是 | 1.设置DividerOptions，则按设置的样式显示分割线。  默认值：  {  strokeWidth: '1px' ,  color: '#33182431'  }  2.设置为null时，不显示分割线。  3.strokeWidth设置过宽时，会覆盖文字。分割线会从每一个Item底部开始，同时向上向下画分割线。  4.startMargin和endMargin的默认值与不设置divider属性时的分割线样式保持一致。startMargin和endMargin的和与optionWidth的值相等时，不显示分割线。 startMargin和endMargin的和超过optionWidth的值时，按照默认样式显示分割线。 |

### dividerStyle19+

PhonePC/2in1TabletTVWearable

dividerStyle(style: Optional<DividerStyleOptions>)

设置分割线样式，不设置该属性则按“默认值”展示分割线。该属性与divider互斥，按调用顺序生效。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[DividerStyleOptions](ts-types.md#dividerstyleoptions12)> | 是 | 1.设置DividerOptions，则按设置的样式显示分割线。  默认值：  {  strokeWidth: '1px' ,  color: '#33182431'  }  2.设置为null或undefined时，展示默认分割线。  3.当mode为FLOAT\_ABOVE\_MENU时，strokeWidth设置过宽时，会覆盖文字。分割线会从每一个Item底部开始，同时向上向下画分割线。当mode为EMBEDDED\_IN\_MENU时，分割线在Menu中展开，独立占用高度。  4.startMargin和endMargin的默认值与不设置divider属性时的分割线样式保持一致。startMargin和endMargin的和与optionWidth的值相等时，不显示分割线。startMargin和endMargin的和超过optionWidth的值时，按照默认样式显示分割线。 |

### font

PhonePC/2in1TabletTVWearable

font(value: Font)

设置下拉按钮本身的文本样式。当size为0时，文本不显示，当size为负值时，文本的size按照默认值显示。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](ts-types.md#font) | 是 | 下拉按钮本身的文本样式。  API version 11及以前默认值：  {  size: $r('sys.float.ohos\_id\_text\_size\_button1'),  weight: FontWeight.Medium  }  API version 12以后，如果设置controlSize的值为：controlSize.SMALL，size默认值是$r('sys.float.ohos\_id\_text\_size\_button2')，否则为$r('sys.float.ohos\_id\_text\_size\_button1')。 |

### font18+

PhonePC/2in1TabletTVWearable

font(selectFont: Optional<Font>)

设置下拉按钮本身的文本样式。当size为0时，文本不显示，当size为负值时，文本的size按照默认值显示。与[font](ts-basic-components-select.md#font)相比，selectFont参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectFont | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Font](ts-types.md#font)> | 是 | 下拉按钮本身的文本样式。  如果设置controlSize的值为：controlSize.SMALL，size默认值是$r('sys.float.ohos\_id\_text\_size\_button2')，否则为$r('sys.float.ohos\_id\_text\_size\_button1')。  当selectFont的值为undefined时，恢复为系统文本样式。 |

### fontColor

PhonePC/2in1TabletTVWearable

fontColor(value: ResourceColor)

设置下拉按钮本身的文本颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 下拉按钮本身的文本颜色。  默认值：$r('sys.color.ohos\_id\_color\_text\_primary')混合$r('sys.color.ohos\_id\_alpha\_content\_primary')的透明度。 |

### fontColor18+

PhonePC/2in1TabletTVWearable

fontColor(resColor: Optional<ResourceColor>)

设置下拉按钮本身的文本颜色。与[fontColor](ts-basic-components-select.md#fontcolor)相比，resColor参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resColor | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ResourceColor](ts-types.md#resourcecolor)> | 是 | 下拉按钮本身的文本颜色。  当resColor的值为undefined时，默认值：$r('sys.color.ohos\_id\_color\_text\_primary')混合$r('sys.color.ohos\_id\_alpha\_content\_primary')的透明度。  当value的值为undefined时，维持上次取值。 |

### selectedOptionBgColor

PhonePC/2in1TabletTVWearable

selectedOptionBgColor(value: ResourceColor)

设置下拉菜单选中项的背景色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 下拉菜单选中项的背景色。  默认值：$r('sys.color.ohos\_id\_color\_component\_activated')混合$r('sys.color.ohos\_id\_alpha\_highlight\_bg')的透明度。 |

### selectedOptionBgColor18+

PhonePC/2in1TabletTVWearable

selectedOptionBgColor(resColor: Optional<ResourceColor>)

设置下拉菜单选中项的背景色。与[selectedOptionBgColor](ts-basic-components-select.md#selectedoptionbgcolor)相比，resColor参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resColor | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ResourceColor](ts-types.md#resourcecolor)> | 是 | 下拉菜单选中项的背景色。  当resColor的值为undefined时，默认值：$r('sys.color.ohos\_id\_color\_component\_activated')混合$r('sys.color.ohos\_id\_alpha\_highlight\_bg')的透明度。 |

### selectedOptionFont

PhonePC/2in1TabletTVWearable

selectedOptionFont(value: Font)

设置下拉菜单选中项的文本样式。当size为0的时候，文本不显示，当size为负值的时候，文本的size按照默认值显示。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](ts-types.md#font) | 是 | 下拉菜单选中项的文本样式。  默认值：  {  size: $r('sys.float.ohos\_id\_text\_size\_body1'),  weight: FontWeight.Regular  } |

### selectedOptionFont18+

PhonePC/2in1TabletTVWearable

selectedOptionFont(selectFont: Optional<Font>)

设置下拉菜单选中项的文本样式。当size为0的时候，文本不显示，当size为负值的时候，文本的size按照默认值显示。与[selectedOptionFont](ts-basic-components-select.md#selectedoptionfont)相比，selectFont参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectFont | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Font](ts-types.md#font)> | 是 | 下拉菜单选中项的文本样式。  当selectFont的值为undefined时，默认值：  {  size: $r('sys.float.ohos\_id\_text\_size\_body1'),  weight: FontWeight.Regular  } |

### selectedOptionFontColor

PhonePC/2in1TabletTVWearable

selectedOptionFontColor(value: ResourceColor)

设置下拉菜单选中项的文本颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 下拉菜单选中项的文本颜色。  默认值：$r('sys.color.ohos\_id\_color\_text\_primary\_activated') |

### selectedOptionFontColor18+

PhonePC/2in1TabletTVWearable

selectedOptionFontColor(resColor: Optional<ResourceColor>)

设置下拉菜单选中项的文本颜色。与[selectedOptionFontColor](ts-basic-components-select.md#selectedoptionfontcolor)相比，resColor参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resColor | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ResourceColor](ts-types.md#resourcecolor)> | 是 | 下拉菜单选中项的文本颜色。  当resColor的值为undefined时，默认值为$r('sys.color.ohos\_id\_color\_text\_primary\_activated')。 |

### optionBgColor

PhonePC/2in1TabletTVWearable

optionBgColor(value: ResourceColor)

设置下拉菜单项的背景色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 下拉菜单项的背景色。  默认值：  API version 11之前，默认值为Color.White。  API version 11及之后，默认值为Color.Transparent。 |

### optionBgColor18+

PhonePC/2in1TabletTVWearable

optionBgColor(resColor: Optional<ResourceColor>)

设置下拉菜单项的背景色。与[optionBgColor](ts-basic-components-select.md#optionbgcolor)相比，resColor参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resColor | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ResourceColor](ts-types.md#resourcecolor)> | 是 | 下拉菜单项的背景色。  当resColor的值为undefined时，下拉菜单项的背景色为Color.White。 |

### optionFont

PhonePC/2in1TabletTVWearable

optionFont(value: Font)

设置下拉菜单项的文本样式。当size为0的时候，文本不显示，当size为负值的时候，文本的size按照默认值显示。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](ts-types.md#font) | 是 | 下拉菜单项的文本样式。  默认值：  {  size: $r('sys.float.ohos\_id\_text\_size\_body1'),  weight: FontWeight.Regular  } |

### optionFont18+

PhonePC/2in1TabletTVWearable

optionFont(selectFont: Optional<Font>)

设置下拉菜单项的文本样式。当size为0的时候，文本不显示，当size为负值的时候，文本的size按照默认值显示。

与[optionFont](ts-basic-components-select.md#optionfont)相比，selectFont参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectFont | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Font](ts-types.md#font)> | 是 | 下拉菜单项的文本样式。  当selectFont的值为undefined时，默认值：  {  size: $r('sys.float.ohos\_id\_text\_size\_body1'),  weight: FontWeight.Regular  } |

### optionFontColor

PhonePC/2in1TabletTVWearable

optionFontColor(value: ResourceColor)

设置下拉菜单项的文本颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 下拉菜单项的文本颜色。  默认值：$r('sys.color.ohos\_id\_color\_text\_primary') |

### optionFontColor18+

PhonePC/2in1TabletTVWearable

optionFontColor(resColor: Optional<ResourceColor>)

设置下拉菜单项的文本颜色。与[optionFontColor](ts-basic-components-select.md#optionfontcolor)相比，resColor参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resColor | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ResourceColor](ts-types.md#resourcecolor)> | 是 | 下拉菜单项的文本颜色。  当resColor的值为undefined时，默认值：$r('sys.color.ohos\_id\_color\_text\_primary') |

### space10+

PhonePC/2in1TabletTVWearable

space(value: Length)

设置下拉菜单项的文本与箭头的间距。不支持设置百分比。将间距设置为null、undefined，或者小于等于8的值时，取默认值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 下拉菜单项的文本与箭头的间距。  默认值：8  **说明：** 设置string类型时，不支持百分比。 |

### space18+

PhonePC/2in1TabletTVWearable

space(spaceLength: Optional<Length>)

设置下拉菜单项的文本与箭头的间距。不支持设置百分比。设置为null、undefined，或者小于等于8的值，取默认值。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| spaceLength | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Length](ts-types.md#length)> | 是 | 下拉菜单项的文本与箭头之间的间距。  当spaceLength的值为undefined时，默认值：8 |

### arrowPosition10+

PhonePC/2in1TabletTVWearable

arrowPosition(value: ArrowPosition)

设置下拉菜单项的文本与箭头之间的对齐方式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ArrowPosition](ts-basic-components-select.md#arrowposition10枚举说明) | 是 | 下拉菜单项的文本与箭头之间的对齐方式。  默认值：ArrowPosition.END |

### arrowPosition18+

PhonePC/2in1TabletTVWearable

arrowPosition(position: Optional<ArrowPosition>)

设置下拉菜单项的文本与箭头之间的对齐方式。与[arrowPosition](ts-basic-components-select.md#arrowposition10)相比，position参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ArrowPosition](ts-basic-components-select.md#arrowposition10枚举说明)> | 是 | 下拉菜单项的文本与箭头之间的对齐方式。  当position的值为undefined时，默认值：ArrowPosition.END |

### menuAlign10+

PhonePC/2in1TabletTVWearable

menuAlign(alignType: MenuAlignType, offset?: Offset)

设置下拉按钮与下拉菜单间的对齐方式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignType | [MenuAlignType](ts-basic-components-select.md#menualigntype10枚举说明) | 是 | 对齐方式类型。  默认值：MenuAlignType.START |
| offset | [Offset](ts-types.md#offset) | 否 | 按照对齐类型对齐后，下拉菜单相对下拉按钮的偏移量。  默认值：{dx: 0, dy: 0} |

### menuAlign18+

PhonePC/2in1TabletTVWearable

menuAlign(alignType: Optional<MenuAlignType>, offset?: Offset)

设置下拉按钮与下拉菜单间的对齐方式。与[menuAlign](ts-basic-components-select.md#menualign10)10+相比，alignType参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignType | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[MenuAlignType](ts-basic-components-select.md#menualigntype10枚举说明)> | 是 | 对齐方式类型。  当alignType的值为undefined时，默认值：MenuAlignType.START |
| offset | [Offset](ts-types.md#offset) | 否 | 按照对齐类型对齐后，下拉菜单相对下拉按钮的偏移量。  默认值：{dx: 0, dy: 0} |

### optionWidth11+

PhonePC/2in1TabletTVWearable

optionWidth(value: Dimension | OptionWidthMode )

设置下拉菜单项的宽度，不支持设置百分比。OptionWidthMode类型为枚举类型，OptionWidthMode决定下拉菜单是否继承下拉按钮宽度。

当设置为异常值或小于最小宽度56vp时，属性无效，菜单项宽度设为默认值，即2栅格。

Select组件距屏幕边缘的左右间距为16vp，建议将组件本身及菜单项的宽度设置为小于等于calc(100% - 32vp)的值，以避免下拉菜单弹出时发生偏移。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | [OptionWidthMode](ts-appendix-enums.md#optionwidthmode11) | 是 | 下拉菜单项的宽度。 |

### optionWidth18+

PhonePC/2in1TabletTVWearable

optionWidth(width: Optional<Dimension | OptionWidthMode> )

设置下拉菜单项的宽度，不支持设置百分比。OptionWidthMode类型为枚举类型，OptionWidthMode决定下拉菜单是否继承下拉按钮宽度。与[optionWidth](ts-basic-components-select.md#optionwidth11)11+相比，width参数新增了对undefined类型的支持。

当设置为异常值或小于最小宽度56vp时，属性无效，菜单项宽度设为默认值，即2栅格。

Select组件距屏幕边缘的左右间距为16vp，建议将组件本身及菜单项的宽度设置为小于等于calc(100% - 32vp)的值，以避免下拉菜单弹出时发生偏移。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Dimension](ts-types.md#dimension10) | [OptionWidthMode](ts-appendix-enums.md#optionwidthmode11)> | 是 | 下拉菜单项的宽度。  当width的值为undefined时，属性无效，菜单项宽度设为默认值，即2栅格。 |

### optionHeight11+

PhonePC/2in1TabletTVWearable

optionHeight(value: Dimension)

设置下拉菜单显示的最大高度，不支持设置百分比。默认最大高度是屏幕可用高度的80%，设置的菜单最大高度不能超过默认最大高度。

当设置为异常值或零时，属性不生效。

如果下拉菜单所有选项的实际高度没有设定的高度大，下拉菜单的高度按实际高度显示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | 是 | 下拉菜单显示的最大高度。 |

### optionHeight18+

PhonePC/2in1TabletTVWearable

optionHeight(height: Optional<Dimension>)

设置下拉菜单显示的最大高度，不支持设置百分比。默认最大高度是屏幕可用高度的80%，设置的菜单最大高度不能超过默认最大高度。与[optionHeight](ts-basic-components-select.md#optionheight11)11+相比，height参数新增了对undefined类型的支持。

当设置为异常值或零时，属性不生效。

如果下拉菜单所有选项的实际高度小于设定的高度，下拉菜单的高度按实际高度显示。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| height | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Dimension](ts-types.md#dimension10)> | 是 | 下拉菜单显示的最大高度。  当height的值为undefined时，属性不生效，下拉菜单最大高度设为默认值，即下拉菜单最大高度默认值为屏幕可用高度的80%。 |

### menuBackgroundColor11+

PhonePC/2in1TabletTVWearable

menuBackgroundColor(value: ResourceColor)

设置下拉菜单的背景色。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 下拉菜单的背景色。  默认值：  API version 11之前，默认值为$r('sys.color.ohos\_id\_color\_card\_bg')。  API version 11及之后，默认值为Color.Transparent。 |

### menuBackgroundColor18+

PhonePC/2in1TabletTVWearable

menuBackgroundColor(resColor: Optional<ResourceColor>)

设置下拉菜单的背景色。与[menuBackgroundColor](ts-basic-components-select.md#menubackgroundcolor11)11+相比，resColor参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resColor | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ResourceColor](ts-types.md#resourcecolor)> | 是 | 下拉菜单的背景色。  当resColor的值为undefined时，默认值为Color.Transparent。 |

### menuBackgroundBlurStyle11+

PhonePC/2in1TabletTVWearable

menuBackgroundBlurStyle(value: BlurStyle)

设置下拉菜单的背景模糊材质。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 是 | 下拉菜单的背景模糊材质。  默认值：BlurStyle.COMPONENT\_ULTRA\_THICK |

### menuBackgroundBlurStyle18+

PhonePC/2in1TabletTVWearable

menuBackgroundBlurStyle(style: Optional<BlurStyle>)

设置下拉菜单的背景模糊材质。与[menuBackgroundBlurStyle](ts-basic-components-select.md#menubackgroundblurstyle11)11+相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[BlurStyle](ts-universal-attributes-background.md#blurstyle9)> | 是 | 下拉菜单的背景模糊材质。  当style的值为undefined时，默认值：BlurStyle.COMPONENT\_ULTRA\_THICK |

### avoidance19+

PhonePC/2in1TabletTVWearable

avoidance(mode: AvoidanceMode)

设置下拉菜单的避让模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [AvoidanceMode](ts-basic-components-select.md#avoidancemode19枚举说明) | 是 | 设置下拉菜单的避让模式。  默认值：AvoidanceMode.COVER\_TARGET |

### menuOutline20+

PhonePC/2in1TabletTVWearable

menuOutline(outline: MenuOutlineOptions)

设置下拉菜单框的外描边样式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| outline | [MenuOutlineOptions](ts-basic-components-select.md#menuoutlineoptions20对象说明) | 是 | 下拉菜单框的外描边样式。 |

### showDefaultSelectedIcon20+

PhonePC/2in1TabletTVWearable

showDefaultSelectedIcon(show: boolean)

设置是否显示默认选择的图标。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| show | boolean | 是 | 是否显示默认选定的图标。  true：显示默认选择的图标；false：不显示默认选择的图标，通过突出显示背景色来表示选中。  默认值：false  当show为true时，若设置了selectedOptionBgColor选中项的背景色时，则同时显示选中项的背景色和默认选定的图标；若未通过selectedOptionBgColor设置选中项的背景色时，不突出显示背景色，只显示默认选定的图标。 |

### textModifier20+

PhonePC/2in1TabletTVWearable

textModifier(modifier: Optional<[TextModifier](ts-universal-attributes-attribute-modifier.md)>)

定制Select按钮文本样式的方法，在应用了textModifier之后，Select按钮的文本样式将完全由开发者自定义。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[TextModifier](ts-universal-attributes-attribute-modifier.md)> | 是 | 在Select组件上，定制按钮文本样式的方法。  当modifier的值为undefined时，不自定义文本样式。 |

### arrowModifier20+

PhonePC/2in1TabletTVWearable

arrowModifier(modifier: Optional<SymbolGlyphModifier>)

定制Select按钮下拉箭头图标样式的方法，在应用arrowModifier之后，Select按钮下拉箭头的图标样式将完全由开发者自定义。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md)> | 是 | 在Select组件上，定制Select按钮下拉箭头图标样式的方法。  当modifier的值为undefined时，不自定义下拉箭头图标样式。 |

### optionTextModifier20+

PhonePC/2in1TabletTVWearable

optionTextModifier(modifier: Optional<[TextModifier](ts-universal-attributes-attribute-modifier.md)>)

定制Select下拉菜单未选中项文本样式的方法，在应用optionTextModifier之后，下拉菜单未选中项的文本样式将完全由开发者自定义。

如果[optionFont](ts-basic-components-select.md#optionfont)与optionTextModifier的Font属性同时设置，则优先使用[optionFont](ts-basic-components-select.md#optionfont)设置下拉菜单未选中项的文本样式；[optionFont](ts-basic-components-select.md#optionfont)中缺省的属性将设置为对应的默认值。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[TextModifier](ts-universal-attributes-attribute-modifier.md)> | 是 | 在Select组件上，定制Select下拉菜单未选中项样式的方法。  当modifier的值为undefined时，不自定义下拉菜单未选中项的文本样式。 |

### selectedOptionTextModifier20+

PhonePC/2in1TabletTVWearable

selectedOptionTextModifier(modifier: Optional<[TextModifier](ts-universal-attributes-attribute-modifier.md)>)

定制Select下拉菜单选中项文本样式的方法，在应用selectedOptionTextModifier之后，下拉菜单选中项的文本样式将完全由开发者自定义。

如果[selectedOptionFont](ts-basic-components-select.md#selectedoptionfont)与selectedOptionTextModifier的Font属性同时设置，则优先使用[selectedOptionFont](ts-basic-components-select.md#selectedoptionfont)设置下拉菜单选中项的文本样式；若未设置[selectedOptionFont](ts-basic-components-select.md#selectedoptionfont)，则优先使用[optionFont](ts-basic-components-select.md#optionfont)设置下拉菜单选中项的文本样式。其中[selectedOptionFont](ts-basic-components-select.md#selectedoptionfont)或者[optionFont](ts-basic-components-select.md#optionfont)缺省的属性将设置为对应的默认值。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[TextModifier](ts-universal-attributes-attribute-modifier.md)> | 是 | 设置下拉菜单项选中项的文本样式。  开发者可以根据需要管理和维护文本的样式进行设置。  当modifier的值为undefined时，不自定义下拉菜单项选中项的文本样式。 |

### showInSubWindow20+

PhonePC/2in1TabletTVWearable

showInSubWindow(showInSubWindow:Optional<boolean>)

设置下拉菜单是否显示在子窗中。未通过该接口设置时，下拉菜单默认不显示在子窗中。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 在PC/2in1设备中可生效，在其他设备类型中不生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| showInSubWindow | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 设置下拉菜单是否显示在子窗中。  true代表下拉菜单显示在子窗中。  false代表下拉菜单不显示在子窗中。 |

### keyboardAvoidMode23+

PhonePC/2in1TabletTVWearable

keyboardAvoidMode(mode:Optional<MenuKeyboardAvoidMode>)

设置下拉菜单是否避让软键盘。未通过该接口设置时，默认不避让软键盘。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[MenuKeyboardAvoidMode](ts-universal-attributes-menu.md#menukeyboardavoidmode23枚举说明)> | 是 | 设置下拉菜单是否避让软键盘。取值为undefined时，按照MenuKeyboardAvoidMode.NONE处理，不避让软键盘。 |

### minKeyboardAvoidDistance23+

PhonePC/2in1TabletTVWearable

minKeyboardAvoidDistance(distance:Optional<LengthMetrics>)

设置Select的菜单避让软键盘的最小距离。未通过该接口设置，最小距离默认为8vp。仅当[keyboardAvoidMode](ts-basic-components-select.md#keyboardavoidmode23)设置为避让软键盘时生效。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| distance | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)> | 是 | 设置下拉菜单避让软键盘的最小距离。设置为负数、undefined时，按照8vp处理。 |

## ArrowPosition10+枚举说明

PhonePC/2in1TabletTVWearable

箭头的位置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| END | 0 | 文字在前，箭头在后。 |
| START | 1 | 箭头在前，文字在后。 |

## MenuAlignType10+枚举说明

PhonePC/2in1TabletTVWearable

下拉菜单的对齐方式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| START | 0 | 按照语言方向起始端对齐。 |
| CENTER | 1 | 居中对齐。 |
| END | 2 | 按照语言方向末端对齐。 |

## AvoidanceMode19+枚举说明

PhonePC/2in1TabletTVWearable

下拉菜单避让模式的枚举选项。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 说明 |
| --- | --- |
| COVER\_TARGET | 目标组件下方无足够空间时，覆盖目标组件。 |
| AVOID\_AROUND\_TARGET | 目标组件四周无足够空间时，在最大空间处压缩显示（可滚动）。 |

## MenuItemConfiguration12+对象说明

PhonePC/2in1TabletTVWearable

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](ts-universal-attributes-content-modifier.md#commonconfigurationt)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 下拉菜单项的文本内容。  **说明：**  当文本字符的长度超过菜单项文本区域的宽度时，文本将会被截断。 |
| icon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 下拉菜单项的图片内容。  **说明：**  string格式可用于加载网络图片和本地图片。 |
| symbolIcon | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md) | 否 | 是 | 下拉选项Symbol图片内容。 |
| selected | boolean | 否 | 否 | 下拉菜单项是否被选中。值为true表示选中，值为false表示未选中。  默认值：false |
| index | number | 否 | 否 | 下拉菜单项的索引，索引值从0开始。 |
| triggerSelect | (index: number, value: string) :void | 否 | 否 | 下拉菜单选中某一项的回调函数。  index：选中菜单项的索引。  value：选中菜单项的文本。  **说明：**  index会赋值给事件[onSelect](ts-basic-components-select.md#onselect)回调中的索引参数； value会返回给Select组件显示，同时会赋值给事件[onSelect](ts-basic-components-select.md#onselect)回调中的文本参数。 |

## MenuOutlineOptions20+对象说明

PhonePC/2in1TabletTVWearable

下拉菜单框的外描边参数对象。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | [Dimension](ts-types.md#dimension10) | [EdgeOutlineWidths](ts-types.md#edgeoutlinewidths11对象说明) | 否 | 是 | 设置外描边宽度，不支持百分比。  默认值：0 |
| color | [ResourceColor](ts-types.md#resourcecolor) | [EdgeColors](ts-types.md#edgecolors9) | 否 | 是 | 设置外描边颜色。  默认值：#19ffffff |

## 事件

PhonePC/2in1TabletTVWearable

### onSelect

PhonePC/2in1TabletTVWearable

onSelect(callback: (index: number, value: string) => void)

下拉菜单选中某一项时，会触发回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 选中项的索引，索引值从0开始。 |
| value | string | 是 | 选中项的值。 |

### onSelect18+

PhonePC/2in1TabletTVWearable

onSelect(callback: Optional<OnSelectCallback> )

下拉菜单选中某一项时，会触发回调。与[onSelect](ts-basic-components-select.md#onselect)相比，callback参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[OnSelectCallback](ts-basic-components-select.md#onselectcallback18)> | 是 | 下拉菜单选中某一项的回调。  当callback的值为undefined时，不使用回调函数。 |

## OnSelectCallback18+

PhonePC/2in1TabletTVWearable

type OnSelectCallback = (index: number, selectStr: string) => void

下拉菜单选中某一项时触发的回调函数类型定义。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 选中项的索引，索引值从0开始。 |
| selectStr | string | 是 | 选中项的值。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置下拉菜单）

该示例通过配置[SelectOption](ts-basic-components-select.md#selectoption对象说明)实现下拉菜单，并从API version 19开始通过设置[avoidance](ts-basic-components-select.md#avoidance19)属性实现菜单的避让方式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SelectExample {
5. @State text: string = "TTTTT";
6. @State index: number = 2;
7. @State space: number = 8;
8. @State arrowPosition: ArrowPosition = ArrowPosition.END;

10. build() {
11. Column() {
12. // $r('app.media.selection')需要替换为开发者所需的图像资源文件。
13. Select([{ value: 'aaa', icon: $r("app.media.selection") },
14. { value: 'bbb', icon: $r("app.media.selection") },
15. { value: 'ccc', icon: $r("app.media.selection") },
16. { value: 'ddd', icon: $r("app.media.selection") }])
17. .selected(this.index)
18. .value(this.text)
19. .font({ size: 16, weight: 500 })
20. .fontColor('#182431')
21. .selectedOptionFont({ size: 16, weight: 400 })
22. .optionFont({ size: 16, weight: 400 })
23. .space(this.space)
24. .arrowPosition(this.arrowPosition)
25. .menuAlign(MenuAlignType.START, { dx: 0, dy: 0 })
26. .optionWidth(200)
27. .optionHeight(300)
28. .onSelect((index: number, text?: string | undefined) => {
29. console.info('Select:' + index);
30. this.index = index;
31. if (text) {
32. this.text = text;
33. }
34. })
35. .avoidance(AvoidanceMode.COVER_TARGET);
36. }.width('100%')
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/5tOV2bcETBivDu-6_bNw5Q/zh-cn_image_0000002558766244.png?HW-CC-KV=V1&HW-CC-Date=20260429T055200Z&HW-CC-Expire=86400&HW-CC-Sign=1DBFA41216DF51B52FD7B33E2D23EC7B6C96BEE7991D7A712852475C53FC6362)

### 示例2（设置symbol类型图标）

该示例实现了一个下拉菜单中图片为Symbol的Select组件，并从API version 19开始通过设置[avoidance](ts-basic-components-select.md#avoidance19)属性实现菜单的避让方式。

```
1. // xxx.ets
2. import { SymbolGlyphModifier } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct SelectExample {
7. @State text: string = "TTTTT";
8. @State index: number = 2;
9. @State space: number = 8;
10. @State arrowPosition: ArrowPosition = ArrowPosition.END;
11. @State symbolModifier1: SymbolGlyphModifier =
12. new SymbolGlyphModifier($r('sys.symbol.ohos_wifi')).fontColor([Color.Green]);
13. @State symbolModifier2: SymbolGlyphModifier =
14. new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontColor([Color.Red]);
15. @State symbolModifier3: SymbolGlyphModifier =
16. new SymbolGlyphModifier($r('sys.symbol.ohos_trash')).fontColor([Color.Gray]);
17. @State symbolModifier4: SymbolGlyphModifier =
18. new SymbolGlyphModifier($r('sys.symbol.exposure')).fontColor([Color.Gray]);

20. build() {
21. Column() {
22. Select([{ value: 'aaa', symbolIcon: this.symbolModifier1 },
23. { value: 'bbb', symbolIcon: this.symbolModifier2 },
24. { value: 'ccc', symbolIcon: this.symbolModifier3 },
25. { value: 'ddd', symbolIcon: this.symbolModifier4 }])
26. .selected(this.index)
27. .value(this.text)
28. .font({ size: 16, weight: 500 })
29. .fontColor('#182431')
30. .selectedOptionFont({ size: 16, weight: 400 })
31. .optionFont({ size: 16, weight: 400 })
32. .space(this.space)
33. .arrowPosition(this.arrowPosition)
34. .menuAlign(MenuAlignType.START, { dx: 0, dy: 0 })
35. .onSelect((index: number, text?: string | undefined) => {
36. console.info('Select:' + index);
37. this.index = index;
38. if (text) {
39. this.text = text;
40. }
41. })
42. .avoidance(AvoidanceMode.COVER_TARGET);
43. }.width('100%')
44. }
45. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/CT2Mvbu7SweGCsf9wgHmEg/zh-cn_image_0000002558606586.png?HW-CC-KV=V1&HW-CC-Date=20260429T055200Z&HW-CC-Expire=86400&HW-CC-Sign=2BD3FD02A6EE600C8F5F12F0292B36363DFEB8F10019165745A99987671C317C)

### 示例3（自定义下拉菜单）

该示例实现了一个自定义下拉菜选项的Select组件。自定义下拉菜单选项样式为“文本 + Symbol图片 + 空白间隔 + 文本 + 绘制三角形”，点击菜单选项后Select组件显示菜单选项的文本内容。

```
1. import { SymbolGlyphModifier } from '@kit.ArkUI';

3. class MyMenuItemContentModifier implements ContentModifier<MenuItemConfiguration> {
4. modifierText: string = "";

6. constructor(text: string) {
7. this.modifierText = text;
8. }

10. applyContent(): WrappedBuilder<[MenuItemConfiguration]> {
11. return wrapBuilder(MenuItemBuilder);
12. }
13. }

15. @Builder
16. function MenuItemBuilder(configuration: MenuItemConfiguration) {
17. Row() {
18. Text(configuration.value)
19. Blank()
20. if (configuration.symbolIcon) {
21. SymbolGlyph().attributeModifier(configuration.symbolIcon).fontSize(24)
22. } else if (configuration.icon) {
23. Image(configuration.icon).size({ width: 24, height: 24 })
24. }
25. Blank(30)
26. Text((configuration.contentModifier as MyMenuItemContentModifier).modifierText)
27. Blank(30)
28. Path()
29. .width('100px')
30. .height('150px')
31. .commands('M40 0 L80 100 L0 100 Z')
32. .fillOpacity(0)
33. .stroke(Color.Black)
34. .strokeWidth(3)
35. }
36. .onClick(() => {
37. configuration.triggerSelect(configuration.index, configuration.value.valueOf().toString());
38. })
39. }

41. @Entry
42. @Component
43. struct SelectExample {
44. @State text: string = "Content Modifier Select";
45. @State symbolModifier1: SymbolGlyphModifier =
46. new SymbolGlyphModifier($r('sys.symbol.ohos_trash')).fontColor([Color.Gray]);
47. @State symbolModifier2: SymbolGlyphModifier =
48. new SymbolGlyphModifier($r('sys.symbol.exposure')).fontColor([Color.Gray]);

50. build() {
51. Column() {
52. Row() {
53. // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
54. Select([{ value: 'item1', icon: $r('app.media.icon'), symbolIcon: this.symbolModifier1 },
55. { value: 'item1', icon: $r('app.media.icon'), symbolIcon: this.symbolModifier2 }])
56. .value(this.text)
57. .onSelect((index: number, text?: string) => {
58. console.info('Select index:' + index);
59. console.info('Select text:' + text);
60. })
61. .menuItemContentModifier(new MyMenuItemContentModifier("Content Modifier"))

63. }.alignItems(VerticalAlign.Center).height('50%')
64. }
65. }
66. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/tp-hphd7SbaUw9SAYbSzCw/zh-cn_image_0000002589326113.png?HW-CC-KV=V1&HW-CC-Date=20260429T055200Z&HW-CC-Expire=86400&HW-CC-Sign=10FEFF86FA682E13ACF7867114C0E14245897ADEA48F532B08E5BEF7014BB423)

### 示例4（设置分割线样式）

该示例通过配置divider的DividerOptions类型实现分割线样式的下拉菜单，并从API version 19开始通过设置[avoidance](ts-basic-components-select.md#avoidance19)属性实现菜单的避让方式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SelectExample {
5. @State text: string = "TTTTT";
6. @State index: number = -1;
7. @State arrowPosition: ArrowPosition = ArrowPosition.END;

9. build() {
10. Column() {
11. // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
12. Select([{ value: 'aaa', icon: $r("app.media.icon") },
13. { value: 'bbb', icon: $r("app.media.icon") },
14. { value: 'ccc', icon: $r("app.media.icon") },
15. { value: 'ddd', icon: $r("app.media.icon") }])
16. .selected(this.index)
17. .value(this.text)
18. .font({ size: 16, weight: 500 })
19. .fontColor('#182431')
20. .selectedOptionFont({ size: 16, weight: 400 })
21. .optionFont({ size: 16, weight: 400 })
22. .arrowPosition(this.arrowPosition)
23. .menuAlign(MenuAlignType.START, { dx: 0, dy: 0 })
24. .optionWidth(200)
25. .optionHeight(300)
26. .divider({
27. strokeWidth: 5,
28. color: Color.Blue,
29. startMargin: 10,
30. endMargin: 10
31. })
32. .onSelect((index: number, text?: string | undefined) => {
33. console.info('Select:' + index);
34. this.index = index;
35. if (text) {
36. this.text = text;
37. }
38. })
39. .avoidance(AvoidanceMode.COVER_TARGET);
40. }.width('100%')
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/eq-LDIJFS_e6WO8xQWICKg/zh-cn_image_0000002589246055.png?HW-CC-KV=V1&HW-CC-Date=20260429T055200Z&HW-CC-Expire=86400&HW-CC-Sign=9DB149774940C2E764DEEED1DC74F8425861BAFF89116E4A05CCEFEDC551E4FF)

### 示例5（设置无分割线样式）

该示例通过配置divider为null实现无分割线样式的下拉菜单，并从API version 19开始通过设置[avoidance](ts-basic-components-select.md#avoidance19)属性实现菜单的避让方式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SelectExample {
5. @State text: string = "TTTTT";
6. @State index: number = -1;
7. @State arrowPosition: ArrowPosition = ArrowPosition.END;

9. build() {
10. Column() {
11. // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
12. Select([{ value: 'aaa', icon: $r("app.media.icon") },
13. { value: 'bbb', icon: $r("app.media.icon") },
14. { value: 'ccc', icon: $r("app.media.icon") },
15. { value: 'ddd', icon: $r("app.media.icon") }])
16. .selected(this.index)
17. .value(this.text)
18. .font({ size: 16, weight: 500 })
19. .fontColor('#182431')
20. .selectedOptionFont({ size: 16, weight: 400 })
21. .optionFont({ size: 16, weight: 400 })
22. .arrowPosition(this.arrowPosition)
23. .menuAlign(MenuAlignType.START, { dx: 0, dy: 0 })
24. .optionWidth(200)
25. .optionHeight(300)
26. .divider(null)
27. .onSelect((index: number, text?: string | undefined) => {
28. console.info('Select:' + index);
29. this.index = index;
30. if (text) {
31. this.text = text;
32. }
33. })
34. .avoidance(AvoidanceMode.COVER_TARGET);
35. }.width('100%')
36. }
37. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/SfMjAnBARG6uO1mtkujbcw/zh-cn_image_0000002558766246.png?HW-CC-KV=V1&HW-CC-Date=20260429T055200Z&HW-CC-Expire=86400&HW-CC-Sign=26D8C90948BB3EFAD9FD9FE84890BA968A5C4B7149913825FD586761F9477747)

### 示例6（设置Select中文本和箭头样式）

从API version 20开始，该示例通过[textModifier](ts-basic-components-select.md#textmodifier20)和[arrowModifier](ts-basic-components-select.md#arrowmodifier20)属性设置文本以及箭头样式。

```
1. import { TextModifier, SymbolGlyphModifier } from "@kit.ArkUI";

3. @Entry
4. @Component
5. struct SelectExample {
6. @State text: string = "TTTTTTTTTT".repeat(3);
7. @State index: number = 2;
8. textModifier: TextModifier = new TextModifier();
9. symbolGlyphModifier: SymbolGlyphModifier = new SymbolGlyphModifier();

11. aboutToAppear(): void {
12. this.textModifier
13. .maxLines(2)
14. .fontSize(18)
15. .textAlign(TextAlign.Center)
16. .fontColor('#333333')
17. .fontWeight(FontWeight.Medium)
18. .textOverflow({overflow:TextOverflow.Clip})

20. this.symbolGlyphModifier
21. .fontSize(25)
22. .fontColor(['#999999'])
23. }

25. build() {
26. Column() {
27. Select([
28. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
29. { value: 'A very long option text that should be truncated nicely'.repeat(3), icon: $r("app.media.startIcon") },
30. { value: 'Option B', icon: $r("app.media.startIcon") },
31. { value: 'Option C', icon: $r("app.media.startIcon") },
32. { value: 'Option D', icon: $r("app.media.startIcon") }
33. ])
34. .selected(this.index)
35. .value(this.text)
36. .textModifier(this.textModifier)
37. .arrowModifier(this.symbolGlyphModifier)
38. .onSelect((index: number, text?: string) => {
39. console.info('Select:' + index);
40. this.index = index;
41. if (text) {
42. this.text = text;
43. }
44. })
45. .margin({ top: 20,left:30 })
46. .borderRadius(12)
47. .width(200)
48. .padding(9)
49. .backgroundColor(Color.White)
50. .shadow({ radius: 10, color: '#888888', offsetX: 0, offsetY: 10 })
51. }
52. .alignItems(HorizontalAlign.Start)
53. .padding(10)
54. .backgroundColor('#F0F2F5')
55. .width('100%')
56. .height('100%')
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/F3cqRTNVRvGypWRXebMzMA/zh-cn_image_0000002558606588.png?HW-CC-KV=V1&HW-CC-Date=20260429T055200Z&HW-CC-Expire=86400&HW-CC-Sign=475C8FEFB228ED289D61C23FE80AB6C0F0922E807FED02986151102F0FACFB16)

### 示例7（设置Select下拉菜单选中和非选中项文本样式）

从API version 20开始，该示例通过[optionTextModifier](ts-basic-components-select.md#optiontextmodifier20)和[selectedOptionTextModifier](ts-basic-components-select.md#selectedoptiontextmodifier20)属性设置下拉菜单选中和非选中项文本样式。

```
1. import { TextModifier } from "@kit.ArkUI";

3. @Entry
4. @Component
5. struct SelectExample {
6. @State text: string = "TTTTTTTTTT".repeat(3);
7. @State index: number = 2;
8. optionTextModifier: TextModifier = new TextModifier();
9. selectedOptionTextModifier: TextModifier = new TextModifier();
10. aboutToAppear(): void {
11. this.optionTextModifier
12. .maxLines(1)
13. .fontSize(16)
14. .textAlign(TextAlign.Start)
15. .fontColor('#666666')
16. .fontWeight(FontWeight.Normal)
17. .width(200)

19. this.selectedOptionTextModifier
20. .maxLines(1)
21. .fontSize(18)
22. .textAlign(TextAlign.Start)
23. .fontColor('#007BFF')
24. .fontWeight(FontWeight.Bold)
25. .width(200)
26. }

28. build() {
29. Column() {
30. Select([
31. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
32. { value: 'A very long option text that should be truncated nicely'.repeat(3), icon: $r("app.media.startIcon") },
33. { value: 'Option B', icon: $r("app.media.startIcon") },
34. { value: 'Option C', icon: $r("app.media.startIcon") },
35. { value: 'Option D', icon: $r("app.media.startIcon") }
36. ])
37. .selected(this.index)
38. .value(this.text)
39. .onSelect((index: number, text?: string) => {
40. console.info('Select:' + index);
41. this.index = index;
42. if (text) {
43. this.text = text;
44. }
45. })
46. .optionTextModifier(this.optionTextModifier)
47. .selectedOptionTextModifier(this.selectedOptionTextModifier)
48. .margin({ top: 20,left:30 })
49. .borderRadius(12)
50. .width(200)
51. .padding(9)
52. .backgroundColor(Color.White)
53. .shadow({ radius: 10, color: '#888888', offsetX: 0, offsetY: 10 })
54. }
55. .alignItems(HorizontalAlign.Start)
56. .padding(10)
57. .backgroundColor('#F0F2F5')
58. .width('100%')
59. .height('100%')
60. }
61. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/xRp2sj_KTk-w0E9-_fC7Hg/zh-cn_image_0000002589326115.png?HW-CC-KV=V1&HW-CC-Date=20260429T055200Z&HW-CC-Expire=86400&HW-CC-Sign=87869AD33EAB1F88AB6C401BD43E75DE0FB7225ACE8A6F8EA28FB6B8B383ABBD)

### 示例8（设置分割线模式）

从API version 19开始，该示例通过配置[DividerStyleOptions](ts-types.md#dividerstyleoptions12)的mode属性设置分割线模式。

```
1. import { LengthMetrics } from '@kit.ArkUI'

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. RelativeContainer() {
8. Select([{ value: "SelectItem" }, { value: "SelectItem" }, { value: "SelectItem" },])
9. .value("请选择")
10. .dividerStyle({
11. strokeWidth: LengthMetrics.vp(5),
12. color: '#d5d5d5',
13. mode: DividerMode.EMBEDDED_IN_MENU
14. })
15. }
16. .height('100%')
17. .width('100%')
18. }
19. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/Q1iO4yzNQYmcL8aJiu5WNw/zh-cn_image_0000002589246057.png?HW-CC-KV=V1&HW-CC-Date=20260429T055200Z&HW-CC-Expire=86400&HW-CC-Sign=63EC8334969E0F272E5B2DA2614CFF9CBCE0EE6B82FAD425558B2F632ECC367B)

### 示例9（设置Select下拉菜单外描边样式）

从API version 20开始该示例通过配置menuOutline的width和color属性设置下拉菜单外描边样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SelectExample {
5. @State text: string = "TTTTT";
6. @State index: number = -1;
7. @State arrowPosition: ArrowPosition = ArrowPosition.END;

9. build() {
10. Column() {
11. Select([{ value: 'aaa' },
12. { value: 'bbb' },
13. { value: 'ccc' },
14. { value: 'ddd' }])
15. .selected(this.index)
16. .value(this.text)
17. .font({ size: 16, weight: 500 })
18. .fontColor('#182431')
19. .selectedOptionFont({ size: 16, weight: 400 })
20. .optionFont({ size: 16, weight: 400 })
21. .arrowPosition(this.arrowPosition)
22. .menuAlign(MenuAlignType.START, { dx: 0, dy: 0 })
23. .optionWidth(200)
24. .optionHeight(300)
25. .menuOutline({
26. width: '5vp',
27. color: Color.Blue
28. })
29. .onSelect((index: number, text?: string | undefined) => {
30. console.info('Select:' + index);
31. this.index = index;
32. if (text) {
33. this.text = text;
34. }
35. })
36. }
37. .width('100%')
38. .height('100%')
39. .backgroundColor('#F0F2F5')
40. }
41. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/w-Gq0ltXQeCSf2Gen0FeQg/zh-cn_image_0000002558766248.png?HW-CC-KV=V1&HW-CC-Date=20260429T055200Z&HW-CC-Expire=86400&HW-CC-Sign=C5A91C4B1C5B54A7325E96A1F4DF121C1B9A308375DA5023F2D7F1C07FDD71C1)

### 示例10（设置Select的弹出菜单避让软键盘）

该示例通过调用[keyboardAvoidMode](ts-basic-components-select.md#keyboardavoidmode23)和[minKeyboardAvoidDistance](ts-basic-components-select.md#minkeyboardavoiddistance23)接口，实现下拉菜单避让软键盘并自定义避让软键盘的最小距离。

从API version 23开始，新增keyboardAvoidMode、minKeyboardAvoidDistance接口。

```
1. import { inputMethod } from '@kit.IMEKit';
2. import { LengthMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Index {
7. private inputController: inputMethod.InputMethodController = inputMethod.getController();

9. build() {
10. RelativeContainer() {
11. Select([{ value: 'SelectOption' },
12. { value: 'SelectOption' },
13. { value: 'SelectOption' },
14. { value: 'SelectOption' },
15. { value: 'SelectOption' }])
16. .value('Click Show Options')
17. .alignRules({
18. center: { anchor: '__container__', align: VerticalAlign.Center },
19. middle: { anchor: '__container__', align: HorizontalAlign.Center },
20. })
21. .keyboardAvoidMode(MenuKeyboardAvoidMode.TRANSLATE_AND_RESIZE)
22. .minKeyboardAvoidDistance(LengthMetrics.vp(20))
23. .onClick(() => {
24. setTimeout(() => {
25. this.attachAndListener()
26. }, 2000)
27. })
28. }
29. .height('100%')
30. .width('100%')
31. }

33. async attachAndListener() {
34. focusControl.requestFocus('Index')
35. try {
36. await this.inputController.attach(true, {
37. inputAttribute: {
38. textInputType: inputMethod.TextInputType.TEXT,
39. enterKeyType: inputMethod.EnterKeyType.SEARCH
40. }
41. })
42. } catch (err) {
43. console.error('Fail to attach')
44. }
45. }
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/Hq_xNd8yTEiSRf344NQ3Mw/zh-cn_image_0000002558606590.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055200Z&HW-CC-Expire=86400&HW-CC-Sign=FA65CE2D03A4208FD15D36F81083823C8375B2EE01B6E8EBD3C9EBC75485C561)
