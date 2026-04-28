---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button
title: Button
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 按钮与选择 > Button
category: harmonyos-references
scraped_at: 2026-04-28T08:01:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3774a257c0d63bde5de25fd0dbc249add5ade30808b23322f123376395c43580
---

按钮组件，可快速创建不同样式的按钮。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含单个子组件。

## 接口

PhonePC/2in1TabletTVWearable

### Button

PhonePC/2in1TabletTVWearable

Button(options: ButtonOptions)

创建可以包含单个子组件的按钮。未通过该接口设置时，则按照ButtonOptions中各参数的默认值配置。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ButtonOptions](ts-basic-components-button.md#buttonoptions对象说明) | 是 | 配置按钮的显示样式。 |

### Button

PhonePC/2in1TabletTVWearable

Button(label: ResourceStr, options?: ButtonOptions)

使用文本内容创建相应的按钮组件，此时Button无法包含子组件。

文本内容默认单行显示。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | [ResourceStr](ts-types.md#resourcestr) | 是 | 按钮文本内容。  **说明：** 当文本字符的长度超过按钮本身的宽度时，文本将会被截断。 |
| options | [ButtonOptions](ts-basic-components-button.md#buttonoptions对象说明) | 否 | 配置按钮的显示样式。  未设置时，则按照ButtonOptions中各参数的默认值配置。 |

### Button

PhonePC/2in1TabletTVWearable

Button()

创建一个空按钮。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## ButtonOptions对象说明

PhonePC/2in1TabletTVWearable

按钮的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ButtonType](ts-basic-components-button.md#buttontype枚举说明) | 否 | 是 | 按钮显示样式。  默认值：ButtonType.ROUNDED\_RECTANGLE  API version 18及之后，ButtonType的默认值修改为ButtonType.ROUNDED\_RECTANGLE。API version 18之前的版本，ButtonType的默认值为ButtonType.Capsule。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| stateEffect | boolean | 否 | 是 | 按钮按下时是否开启按压态显示效果。  true：开启按压效果；false：关闭按压效果。  默认值：true  **说明：**  当开启按压态显示效果，且开发者设置状态样式时，会基于状态样式设置完成后的背景色再进行颜色叠加。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| buttonStyle11+ | [ButtonStyleMode](ts-basic-components-button.md#buttonstylemode11枚举说明) | 否 | 是 | 按钮的样式和重要程度，根据设置枚举值的不同，系统自动会调整按钮的背景色和文字颜色。背景色和文字颜色也支持开发者通过[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)、[fontColor](ts-basic-components-button.md#fontcolor)和[role](ts-basic-components-button.md#role12)接口设置，实际显示效果以最后一次设置为准。  默认值：ButtonStyleMode.EMPHASIZED  **说明：**  按钮重要程度：强调按钮>普通按钮>文字按钮。  **卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| controlSize11+ | [ControlSize](ts-basic-components-button.md#controlsize11枚举说明) | 否 | 是 | 按钮的尺寸。  默认值：ControlSize.NORMAL  **卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| role12+ | [ButtonRole](ts-basic-components-button.md#buttonrole12枚举说明) | 否 | 是 | 按钮的角色，根据设置枚举值的不同，系统自动会调整按钮的背景色和文字颜色。背景色和文字颜色也支持开发者通过[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)、[fontColor](ts-basic-components-button.md#fontcolor)和[buttonStyle](ts-basic-components-button.md#buttonstyle11)接口设置，实际显示效果以最后一次设置为准。  默认值：ButtonRole.NORMAL  **卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### type

PhonePC/2in1TabletTVWearable

type(value: ButtonType)

设置Button样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ButtonType](ts-basic-components-button.md#buttontype枚举说明) | 是 | Button样式。  API version 18及之后，ButtonType的默认值从ButtonType.Capsule变更为ButtonType.ROUNDED\_RECTANGLE。 |

### fontSize

PhonePC/2in1TabletTVWearable

fontSize(value: Length)

设置文本显示字号。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 文本显示字号。  默认值：当controlSize为ControlSize.NORMAL时，默认值为$r('sys.float.Body\_L')。  当controlSize为ControlSize.SMALL时，默认值为$r('sys.float.Body\_S')。  **说明**：设置string类型时，不支持百分比。 |

### fontColor

PhonePC/2in1TabletTVWearable

fontColor(value: ResourceColor)

设置文本显示颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 文本显示颜色。  默认值：$r('sys.color.font\_on\_primary')，显示为白色字体。 |

### fontWeight

PhonePC/2in1TabletTVWearable

fontWeight(value: number | FontWeight | string)

设置文本的字体粗细。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [FontWeight](ts-appendix-enums.md#fontweight) | string | 是 | 文本的字体粗细，number类型取值[100, 900]，取值间隔为100，取值越大，字体越粗。  默认值：500  string类型仅支持number类型取值的字符串形式，例如'400'，以及'bold'、'bolder'、'lighter'、'regular'、'medium'，分别对应FontWeight中相应的枚举值。  当值为异常值或非法值时，字体粗细取值为400。 |

### fontStyle8+

PhonePC/2in1TabletTVWearable

fontStyle(value: FontStyle)

设置文本的字体样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FontStyle](ts-appendix-enums.md#fontstyle) | 是 | 文本的字体样式。  默认值：FontStyle.Normal |

### stateEffect

PhonePC/2in1TabletTVWearable

stateEffect(value: boolean)

设置是否开启按压态显示效果。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 按钮按下时是否开启按压态显示效果。  true：开启按压效果；false：关闭按压效果。  默认值：true |

说明

使用多态样式设置按压态时，需优先设置stateEffect为false，防止内置按压态与多态样式按压态冲突。

### fontFamily8+

PhonePC/2in1TabletTVWearable

fontFamily(value: string | Resource)

设置字体列表。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [Resource](ts-types.md#resource) | 是 | 字体列表。默认字体'HarmonyOS Sans'，当前支持'HarmonyOS Sans'字体和[注册自定义字体](js-apis-font.md)。 |

### labelStyle10+

PhonePC/2in1TabletTVWearable

labelStyle(value: LabelStyle)

设置Button组件label文本和字体的样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LabelStyle](ts-basic-components-button.md#labelstyle10对象说明) | 是 | Button组件label文本和字体的样式。 |

### buttonStyle11+

PhonePC/2in1TabletTVWearable

buttonStyle(value: ButtonStyleMode)

设置Button组件的样式和重要程度。根据设置枚举值的不同，系统自动会调整按钮的背景色和文字颜色。背景色和文字颜色也支持开发者通过[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)、[fontColor](ts-basic-components-button.md#fontcolor)和[role](ts-basic-components-button.md#role12)接口设置，实际显示效果以最后一次设置为准。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ButtonStyleMode](ts-basic-components-button.md#buttonstylemode11枚举说明) | 是 | Button组件的样式和重要程度。  默认值：ButtonStyleMode.EMPHASIZED |

### controlSize11+

PhonePC/2in1TabletTVWearable

controlSize(value: ControlSize)

设置Button组件的尺寸。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ControlSize](ts-basic-components-button.md#controlsize11枚举说明) | 是 | Button组件的尺寸。  默认值：ControlSize.NORMAL |

### role12+

PhonePC/2in1TabletTVWearable

role(value: ButtonRole)

设置Button组件的角色。根据设置枚举值的不同，系统自动会调整按钮的背景色和文字颜色。背景色和文字颜色也支持开发者通过[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)、[fontColor](ts-basic-components-button.md#fontcolor)和[buttonStyle](ts-basic-components-button.md#buttonstyle11)接口设置，实际显示效果以最后一次设置为准。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ButtonRole](ts-basic-components-button.md#buttonrole12枚举说明) | 是 | 设置Button组件的角色。  默认值：ButtonRole.NORMAL |

### contentModifier12+

PhonePC/2in1TabletTVWearable

contentModifier(modifier: ContentModifier<ButtonConfiguration>)

定制Button内容区的方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](ts-universal-attributes-content-modifier.md#contentmodifiert)<[ButtonConfiguration](ts-basic-components-button.md#buttonconfiguration12对象说明)> | 是 | 在Button组件上，定制内容区的方法。  modifier：内容修改器，开发者需要自定义class实现ContentModifier接口。 |

### minFontScale18+

PhonePC/2in1TabletTVWearable

minFontScale(scale: number | Resource)

设置文本最小的字体缩放倍数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | number | [Resource](ts-types.md#resource) | 是 | 文本最小的字体缩放倍数。  取值范围：[0, 1]  **说明：**  设置的值小于0时，按值为0处理，设置的值大于1，按值为1处理，异常值默认不生效。 |

### maxFontScale18+

PhonePC/2in1TabletTVWearable

maxFontScale(scale: number | Resource)

设置文本最大的字体缩放倍数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | number | [Resource](ts-types.md#resource) | 是 | 文本最大的字体缩放倍数。  取值范围：[1, +∞)  **说明：**  设置的值小于1时，按值为1处理，异常值默认不生效。  未设置最大缩放倍数时，圆形按钮最大缩放倍数为1倍，胶囊型按钮、普通按钮、圆角矩形按钮最大缩放倍数跟随系统设置。 |

## ButtonType枚举说明

PhonePC/2in1TabletTVWearable

按钮的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Normal | 0 | 普通按钮（默认不带圆角）。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Capsule | 1 | 胶囊型按钮（圆角默认为高度的一半）。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Circle | 2 | 圆形按钮。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| ROUNDED\_RECTANGLE15+ | 8 | 圆角矩形按钮（默认值：controlSize为NORMAL，圆角大小20vp，controlSize为SMALL，圆角大小14vp）。  **卡片能力：** 从API version 15开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |

说明

* 按钮圆角通过[通用属性borderRadius](ts-universal-attributes-border.md#borderradius)设置。
* 当按钮类型为Capsule时，borderRadius设置不生效，按钮圆角始终为宽、高中较小值的一半。
* 当按钮类型为Circle时，若同时设置了宽和高，则borderRadius不生效，且按钮半径为宽高中较小值的一半；若只设置宽、高中的一个，则borderRadius不生效，且按钮半径为所设宽或所设高值的一半；若不设置宽高，则borderRadius为按钮半径；若borderRadius的值为负，则borderRadius的值按照0处理。
* 按钮文本通过[fontSize](ts-basic-components-button.md#fontsize)、[fontColor](ts-basic-components-button.md#fontcolor)、[fontStyle](ts-basic-components-button.md#fontstyle8)、[fontFamily](ts-basic-components-button.md#fontfamily8)、[fontWeight](ts-basic-components-button.md#fontweight)进行设置。
* 设置[颜色渐变](ts-universal-attributes-gradient-color.md)需先设置[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)为透明色。
* 在不设置borderRadius时，圆角矩形按钮的圆角大小保持默认值不变。圆角大小不会随按钮高度变化而变化，和controlSize属性有关，controlSize为NORMAL时圆角大小20vp，controlSize为SMALL时圆角大小14vp。
* 设置Button的[border](ts-universal-attributes-border.md#border)时，会有默认的[borderRadius](ts-universal-attributes-border.md#borderradius)值。如果同时使用border和borderRadius，需将borderRadius放在border之后，以确保borderRadius不会被border中的默认radius覆盖。

## LabelStyle10+对象说明

PhonePC/2in1TabletTVWearable

Button组件的label文本及其字体样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| overflow | [TextOverflow](ts-appendix-enums.md#textoverflow) | 否 | 是 | 设置label文本超长时的显示方式。文本截断是按字截断。例如，英文以单词为最小单位进行截断，若需要以字母为单位进行截断，可在字母间添加零宽空格。  默认值：TextOverflow.Ellipsis  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| maxLines | number | 否 | 是 | 设置label文本的最大行数。如果指定此参数，则文本最多不会超过指定的行。如果有多余的文本，可以通过overflow来指定截断方式。  默认值：1  **说明：**  设置小于等于0的值时，按默认值处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| minFontSize | number | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置label文本最小显示字号。需配合maxFontSize以及maxLines或布局大小限制使用。  **说明：**  minFontSize小于或等于0时，自适应字号不生效。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| maxFontSize | number | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置label文本最大显示字号。需配合minFontSize以及maxLines或布局大小限制使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| heightAdaptivePolicy | [TextHeightAdaptivePolicy](ts-appendix-enums.md#textheightadaptivepolicy10) | 否 | 是 | 设置label文本自适应高度的方式。  默认值：TextHeightAdaptivePolicy.MAX\_LINES\_FIRST  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| font | [Font](ts-types.md#font) | 否 | 是 | 设置label文本字体样式。  默认值：  {  size:'16.0fp',  weight:FontWeight.Medium,  style:FontStyle.Normal,  family:'HarmonyOS Sans'  }  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| textAlign23+ | [TextAlign](ts-appendix-enums.md#textalign) | 否 | 是 | 设置label文本在水平方向上的对齐方式。当使用子节点的Text组件设置label时，此属性不生效，实际的文本对齐方式由子节点Text组件的textAlign属性决定。  Wearable设备默认值为TextAlign.Center，其他设备默认值为TextAlign.Start。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## ButtonStyleMode11+枚举说明

PhonePC/2in1TabletTVWearable

按钮的重要程度。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 普通按钮（一般界面操作）。 |
| EMPHASIZED | 1 | 强调按钮（用于强调当前操作）。 |
| TEXTUAL | 2 | 文本按钮（纯文本，无背景颜色）。 |

## ControlSize11+枚举说明

PhonePC/2in1TabletTVWearable

按钮的尺寸。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SMALL | "small" | 小尺寸按钮。 |
| NORMAL | "normal" | 正常尺寸按钮。 |

## ButtonRole12+枚举说明

PhonePC/2in1TabletTVWearable

按钮的角色。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 正常按钮。 |
| ERROR | 1 | 警示按钮。 |

## ButtonConfiguration12+对象说明

PhonePC/2in1TabletTVWearable

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](ts-universal-attributes-content-modifier.md#commonconfigurationt)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| label | string | 否 | 否 | Button的文本标签。  **说明**：当文本字符的长度超过按钮本身的宽度时，文本将会被截断。 |
| pressed | boolean | 否 | 否 | 指示是否按下Button。  true：按下；false：未按下。  默认值：false  **说明：**  此按压属性生效区域大小为原本Button组件的大小，而非build出来的新组件大小。 |
| triggerClick | [ButtonTriggerClickCallback](ts-basic-components-button.md#buttontriggerclickcallback12) | 否 | 否 | 使用builder新构建出来组件的点击事件。 |

## ButtonTriggerClickCallback12+

PhonePC/2in1TabletTVWearable

type ButtonTriggerClickCallback = (xPos: number, yPos: number) => void

定义ButtonConfiguration中使用的回调类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| xPos | number | 是 | 点击位置x的坐标。  单位：vp |
| yPos | number | 是 | 点击位置y的坐标。  单位：vp |

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置按钮的显示样式）

该示例实现了两种创建按钮的方式，包含子组件或使用文本内容创建相应的按钮。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ButtonExample {
5. build() {
6. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
7. Text('Normal button').fontSize(9).fontColor(0xCCCCCC)
8. Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
9. Button('OK', { type: ButtonType.Normal, stateEffect: true })
10. .borderRadius(8)
11. .backgroundColor(0x317aff)
12. .width(90)
13. .onClick(() => {
14. console.info('ButtonType.Normal');
15. })
16. Button({ type: ButtonType.Normal, stateEffect: true }) {
17. Row() {
18. LoadingProgress().width(20).height(20).margin({ left: 12 }).color(0xFFFFFF)
19. Text('loading').fontSize(12).fontColor(0xffffff).margin({ left: 5, right: 12 })
20. }.alignItems(VerticalAlign.Center)
21. }.borderRadius(8).backgroundColor(0x317aff).width(90).height(40)

23. Button('Disable', { type: ButtonType.Normal, stateEffect: false }).opacity(0.4)
24. .borderRadius(8).backgroundColor(0x317aff).width(90)
25. }

27. Text('Capsule button').fontSize(9).fontColor(0xCCCCCC)
28. Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
29. Button('OK', { type: ButtonType.Capsule, stateEffect: true }).backgroundColor(0x317aff).width(90)
30. Button({ type: ButtonType.Capsule, stateEffect: true }) {
31. Row() {
32. LoadingProgress().width(20).height(20).margin({ left: 12 }).color(0xFFFFFF)
33. Text('loading').fontSize(12).fontColor(0xffffff).margin({ left: 5, right: 12 })
34. }.alignItems(VerticalAlign.Center).width(90).height(40)
35. }.backgroundColor(0x317aff)

37. Button('Disable', { type: ButtonType.Capsule, stateEffect: false }).opacity(0.4)
38. .backgroundColor(0x317aff).width(90)
39. }

41. Text('Circle button').fontSize(9).fontColor(0xCCCCCC)
42. Flex({ alignItems: ItemAlign.Center, wrap: FlexWrap.Wrap }) {
43. Button({ type: ButtonType.Circle, stateEffect: true }) {
44. LoadingProgress().width(20).height(20).color(0xFFFFFF)
45. }.width(55).height(55).backgroundColor(0x317aff)

47. Button({ type: ButtonType.Circle, stateEffect: true }) {
48. LoadingProgress().width(20).height(20).color(0xFFFFFF)
49. }.width(55).height(55).margin({ left: 20 }).backgroundColor(0xF55A42)
50. }
51. }.height(400).padding({ left: 35, right: 35, top: 35 })
52. }
53. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/1yPooOl0QsC3Lpmsog1LgA/zh-cn_image_0000002552959692.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000139Z&HW-CC-Expire=86400&HW-CC-Sign=839F8FBCA3E1097EBF02C7254227D660F48E61B6818063F251EB751051A28C55)

### 示例2 （为按钮添加渲染控制）

该示例通过if/else控制按钮的显示文本。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SwipeGestureExample {
5. @State count: number = 0;

7. build() {
8. Column() {
9. Text(`${this.count}`)
10. .fontSize(30)
11. .onClick(() => {
12. this.count++;
13. })
14. if (this.count <= 0) {
15. Button('count is negative').fontSize(30).height(50)
16. } else if (this.count % 2 === 0) {
17. Button('count is even').fontSize(30).height(50)
18. } else {
19. Button('count is odd').fontSize(30).height(50)
20. }
21. }.height('100%').width('100%').justifyContent(FlexAlign.Center)
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/ruBqMgKqTr6NM6oznOEbAg/zh-cn_image_0000002583479693.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000139Z&HW-CC-Expire=86400&HW-CC-Sign=834D56036524251E3D0E507E47785AC45801E61B404EE0A7318987E71E04837E)

### 示例3 （设置按钮文本样式）

该示例通过配置labelStyle自定义按钮文本的显示样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ButtonTestDemo {
5. @State txt: string = 'overflowTextOverLengthTextOverflow.Clip';
6. @State widthShortSize: number = 205;

8. build() {
9. Row() {
10. Column() {
11. Button(this.txt)
12. .type(ButtonType.Capsule)
13. .width(this.widthShortSize)
14. .height(100)
15. .backgroundColor(0x317aff)
16. .labelStyle({ overflow: TextOverflow.Clip,
17. maxLines: 1,
18. minFontSize: 20,
19. maxFontSize: 20,
20. font: {
21. size: 20,
22. weight: FontWeight.Bolder,
23. family: 'cursive',
24. style: FontStyle.Italic
25. }
26. })
27. .fontSize(40)
28. }
29. .width('100%')
30. }
31. .height('100%')
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/ZF6gi0LEQeOxvYmH3BTKUA/zh-cn_image_0000002552800044.png?HW-CC-KV=V1&HW-CC-Date=20260428T000139Z&HW-CC-Expire=86400&HW-CC-Sign=EDDBCB015E0E3D76B9EF811F8D31C91B7D30CA30AF02AE78B87C15E93D6FC710)

### 示例4（设置不同尺寸按钮的重要程度）

该示例通过配置controlSize、buttonStyle实现不同尺寸按钮的重要程度。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ButtonExample {
5. build() {
6. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
7. Text('Normal size button').fontSize(9).fontColor(0xCCCCCC)
8. Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
9. Button('Emphasized', { buttonStyle: ButtonStyleMode.EMPHASIZED });
10. Button('Normal', { buttonStyle: ButtonStyleMode.NORMAL });
11. Button('Textual', { buttonStyle: ButtonStyleMode.TEXTUAL });
12. }

14. Text('Small size button').fontSize(9).fontColor(0xCCCCCC)
15. Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
16. Button('Emphasized', { controlSize: ControlSize.SMALL, buttonStyle: ButtonStyleMode.EMPHASIZED });
17. Button('Normal', { controlSize: ControlSize.SMALL, buttonStyle: ButtonStyleMode.NORMAL });
18. Button('Textual', { controlSize: ControlSize.SMALL, buttonStyle: ButtonStyleMode.TEXTUAL });
19. }

21. Text('Small size button').fontSize(9).fontColor(0xCCCCCC)
22. Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
23. Button('Emphasized').controlSize(ControlSize.SMALL).buttonStyle(ButtonStyleMode.EMPHASIZED);
24. Button('Normal').controlSize(ControlSize.SMALL).buttonStyle(ButtonStyleMode.NORMAL);
25. Button('Textual').controlSize(ControlSize.SMALL).buttonStyle(ButtonStyleMode.TEXTUAL);
26. }

28. }.height(400).padding({ left: 35, right: 35, top: 35 })
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/MvgeWYuQTmG8Pyt5a3T_TQ/zh-cn_image_0000002583439739.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000139Z&HW-CC-Expire=86400&HW-CC-Sign=8CDBC6A13686F7BDAF7D20C16131D8E3F1A0E484D8C0FA0EF177FCC836CA7B08)

### 示例5（设置按钮的角色）

该示例通过配置role实现按钮的角色。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ButtonExample {
5. build() {
6. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
7. Text('Role is Normal button').fontSize(9).fontColor(0xCCCCCC)
8. Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
9. Button('Emphasized', { buttonStyle: ButtonStyleMode.EMPHASIZED, role: ButtonRole.NORMAL });
10. Button('Normal', { buttonStyle: ButtonStyleMode.NORMAL, role: ButtonRole.NORMAL });
11. Button('Textual', { buttonStyle: ButtonStyleMode.TEXTUAL, role: ButtonRole.NORMAL });
12. }
13. Text('Role is Error button').fontSize(9).fontColor(0xCCCCCC)
14. Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
15. Button('Emphasized', { buttonStyle: ButtonStyleMode.EMPHASIZED, role: ButtonRole.ERROR});
16. Button('Normal', { buttonStyle: ButtonStyleMode.NORMAL, role: ButtonRole.ERROR });
17. Button('Textual', { buttonStyle: ButtonStyleMode.TEXTUAL, role: ButtonRole.ERROR });
18. }
19. }.height(200).padding({ left: 15, right: 15, top: 35 })
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/TRUaTxBRR6G7RTqwXxPU_w/zh-cn_image_0000002552959694.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000139Z&HW-CC-Expire=86400&HW-CC-Sign=D8C05761BE364BDC145E5CE50961925BF2C93F4A5447C294246072EBEE9B503F)

### 示例6（设置自定义样式按钮）

该示例实现了自定义样式的功能，自定义样式实现了一个圆圈替换原本的按钮样式。如果按压，圆圈将变成红色，标题会显示按压字样；如果没有按压，圆圈将变成黑色，标题会显示非按压字样。

```
1. class MyButtonStyle implements ContentModifier<ButtonConfiguration> {
2. x: number = 0;
3. y: number = 0;
4. selectedColor: Color = Color.Black;

6. constructor(x: number, y: number, colorType: Color) {
7. this.x = x;
8. this.y = y;
9. this.selectedColor = colorType;
10. }

12. applyContent(): WrappedBuilder<[ButtonConfiguration]> {
13. return wrapBuilder(buildButton1);
14. }
15. }

17. @Builder
18. function buildButton1(config: ButtonConfiguration) {
19. Column({ space: 30 }) {
20. Text(config.enabled ? "enabled true" : "enabled false")
21. Text('圆圈状态' + (config.pressed ? "（ 按压 ）" : "（ 非按压 ）"))
22. Text('点击位置x坐标：' + (config.enabled ? (config.contentModifier as MyButtonStyle).x : "0"))
23. Text('点击位置y坐标：' + (config.enabled ? (config.contentModifier as MyButtonStyle).y : "0"))
24. Circle({ width: 50, height: 50 })
25. .fill(config.pressed ? (config.contentModifier as MyButtonStyle).selectedColor : Color.Black)
26. .gesture(
27. TapGesture({ count: 1 }).onAction((event: GestureEvent) => {
28. config.triggerClick(event.fingerList[0].localX, event.fingerList[0].localY)
29. })).opacity(config.enabled ? 1 : 0.1)
30. }
31. }

33. @Entry
34. @Component
35. struct ButtonExample {
36. @State buttonEnabled: boolean = true;
37. @State positionX: number = 0;
38. @State positionY: number = 0;
39. @State state: boolean[] = [true, false];
40. @State index: number = 0;

42. build() {
43. Column() {
44. Button('OK')
45. .contentModifier(new MyButtonStyle(this.positionX, this.positionY, Color.Red))
46. .onClick((event) => {
47. console.info('change' + JSON.stringify(event));
48. this.positionX = event.displayX;
49. this.positionY = event.displayY;
50. }).enabled(this.buttonEnabled)
51. Row() {
52. Toggle({ type: ToggleType.Switch, isOn: true }).onChange((value: boolean) => {
53. if (value) {
54. this.buttonEnabled = true;
55. } else {
56. this.buttonEnabled = false;
57. }
58. }).margin({ left: -80 })
59. }
60. }.height('100%').width('100%').justifyContent(FlexAlign.Center)
61. }
62. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/bSzz_Ip8SXOc_9jx2adhrQ/zh-cn_image_0000002583479695.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000139Z&HW-CC-Expire=86400&HW-CC-Sign=6C55D3F186105BAE56C409604968C9ACFA66A791ED69F50B3346E7A1E8E6BBE2)

### 示例7（设置圆角矩形按钮）

该示例通过配置ButtonType.ROUNDED\_RECTANGLE创建圆角矩形按钮。

```
1. @Entry
2. @Component
3. struct ButtonExample {
4. build() {
5. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
6. Text('Rounded rectangle button with rounded corners by default.').fontSize(9).fontColor(0xCCCCCC)
7. Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
8. Button('Rounded rectangle')
9. .type(ButtonType.ROUNDED_RECTANGLE)
10. .backgroundColor(0x317aff)
11. .controlSize(ControlSize.NORMAL)
12. .width(180)
13. }
14. Text('Rounded rectangle button configured with a borderRadius of 5.').fontSize(9).fontColor(0xCCCCCC)
15. Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
16. Button('Rounded rectangle')
17. .type(ButtonType.ROUNDED_RECTANGLE)
18. .backgroundColor(0x317aff)
19. .controlSize(ControlSize.NORMAL)
20. .width(180)
21. .borderRadius(5)
22. }
23. Text('Rounded rectangle button configured extra long text.').fontSize(9).fontColor(0xCCCCCC)
24. Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
25. Button('Rounded rectangle Rounded rectangle Rounded rectangle Rounded rectangle')
26. .type(ButtonType.ROUNDED_RECTANGLE)
27. .backgroundColor(0x317aff)
28. .width(180)
29. .labelStyle({overflow:TextOverflow.Ellipsis, maxLines:3, minFontSize: 0})
30. }
31. }.height(400).padding({ left: 35, right: 35, top: 35 })
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/Zebtv7gcRr2UTenQzvD7YA/zh-cn_image_0000002552800046.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000139Z&HW-CC-Expire=86400&HW-CC-Sign=9630FB931150D85EB86BC2C1C05EE99E5869469307DDEC2217CD201C54F1D73B)

### 示例8（设置label文本水平对齐方式）

该示例通过配置[LabelStyle](ts-basic-components-button.md#labelstyle10对象说明)的textAlign，设置文本对齐方式。

从API version 23开始，新增textAlign接口。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Column(){
6. Button('helloWorld helloWorld helloWorld helloWorld helloWorld helloWorld')
7. .width(200)
8. .labelStyle({
9. textAlign: TextAlign.Center
10. })
11. }
12. .width('100%')
13. .alignItems(HorizontalAlign.Center)
14. }
15. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/aw8r7yPiRqSCNVbek0PjEQ/zh-cn_image_0000002583439741.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000139Z&HW-CC-Expire=86400&HW-CC-Sign=753C8B94D20C6375FB599C8C8052B93CE67E34C1F95B7299CAC963EB54476397)
