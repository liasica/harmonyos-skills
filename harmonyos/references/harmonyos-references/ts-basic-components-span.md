---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span
title: Span
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 文本与输入 > Span
category: harmonyos-references
scraped_at: 2026-09-05T06:17:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:eb56edb1c9e476a70b05fefd587f5ea313020a2559f1d8f0372296a2336dca1d
---

作为[Text](ts-basic-components-text.md)、[ContainerSpan](ts-basic-components-containerspan.md)组件的子组件，用于显示行内文本，支持对文本的字体、颜色、大小等样式进行细粒度设置。适用于在同一行文本中混合显示不同样式的场景，如不同字体颜色的文本、添加装饰线或阴影效果等。

**说明** 

* 该组件从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 该组件从API version 10开始支持继承父组件Text的属性，即如果子组件未设置属性且父组件设置属性，则继承父组件设置的属性。支持继承的属性仅包括：fontColor、fontSize、fontStyle、fontWeight、decoration、letterSpacing、textCase、fontFamily、textShadow。
* 支持[通用属性](ts-component-general-attributes.md)中的[无障碍属性](ts-universal-attributes-accessibility.md)（[accessibilityText](ts-universal-attributes-accessibility.md#accessibilitytext)）、[组件标识](ts-universal-attributes-component-id.md)（[id](ts-universal-attributes-component-id.md#id)、[key](ts-universal-attributes-component-id.md#key12)）和[禁用反色能力](ts-allow-force-dark.md)（[allowForceDark](ts-allow-force-dark.md#allowforcedark)），不支持其他通用属性。若需设置其他通用属性，应使用[Text](ts-basic-components-text.md)进行设置，或改用[属性字符串](ts-universal-styled-string.md)中的[CustomSpan](ts-universal-styled-string.md#customspan)自行绘制。
* [accessibilityText](ts-universal-attributes-accessibility.md#accessibilitytext)仅在Span设置了[onClick](ts-universal-events-click.md#onclick)事件时生效，配置的文本只会体现在无障碍服务识别到的内嵌链接弹窗中。直接播报时，仍播报Span的内容，不会替换为accessibilityText配置的文本。
* [通用事件](ts-component-general-events.md)只支持点击事件[onClick](ts-universal-events-click.md#onclick)和悬浮事件[onHover](ts-universal-events-hover.md#onhover)。

## 子组件

无

## 接口

Span(value: string | Resource)

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [Resource](ts-types.md#resource) | 是 | 文本内容。 |

## 属性

属性继承自[BaseSpan](ts-basic-components-span.md#basespan)。

### decoration

decoration(value: DecorationStyleInterface)

设置文本装饰线样式及其颜色。未通过该接口设置时，默认装饰线类型为TextDecorationType.None（无装饰线），颜色为Color.Black（黑色），样式为TextDecorationStyle.SOLID（实线）。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [DecorationStyleInterface12+](ts-universal-styled-string.md#decorationstyleinterface) | 是 | 文本装饰线样式对象。  **说明：**  style参数不支持卡片能力。 |

**说明** 

当文字的下边缘轮廓与装饰线位置相交时，会触发下划线避让规则，下划线将在这些字符处避让文字。常见“gjyqp”等英文字符。

当文本装饰线的颜色设置为Color.Transparent时，装饰线颜色设置为跟随每行第一个字的字体颜色。当文本装饰线的颜色设置为透明色16进制对应值“#00FFFFFF”时，装饰线颜色设置为透明色。

### letterSpacing

letterSpacing(value: number | ResourceStr)

设置文本字符间距。取值小于0，字符聚集重叠，取值大于0且随着数值变大，字符间距越来越大，稀疏分布。适用于标题排版、标签文字等需要调整字符紧凑度或稀疏度的场景。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [ResourceStr](ts-types.md#resourcestr) | 是 | 文本字符间距。  单位：[fp](ts-pixel-units.md#基本像素单位)  从API version 20开始，支持[Resource](ts-types.md#resource)类型。 |

### textCase

textCase(value: TextCase)

设置文本大小写。未通过该接口设置时，默认文本大小写为TextCase.Normal（正常大小写）。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TextCase](ts-appendix-enums.md#textcase) | 是 | 文本大小写。 |

### fontColor

fontColor(value: ResourceColor)

设置字体颜色。未通过该接口设置时，默认字体颜色为'#FF182431'（深灰色），Wearable设备上默认为'#C5FFFFFF'（白色，不透明度约为77%）。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 字体颜色。 |

### fontSize

fontSize(value: number | string | Resource)

设置字体大小。未通过该接口设置时，默认字体大小为16fp，Wearable设备上默认为15fp。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](ts-types.md#resource) | 是 | 字体大小。fontSize为number类型时，使用fp单位。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"，不支持设置百分比字符串。  从API version 20开始，支持[Resource](ts-types.md#resource)类型。 |

### fontStyle

fontStyle(value: FontStyle)

设置字体样式。未通过该接口设置时，默认字体样式为FontStyle.Normal（正常样式）。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FontStyle](ts-appendix-enums.md#fontstyle) | 是 | 字体样式。 |

### fontWeight

fontWeight(value: number | FontWeight | ResourceStr)

设置文本的字体粗细，设置过大可能会在不同字体下有截断。未通过该接口设置时，默认字体粗细为FontWeight.Normal（正常粗细，对应数值400）。

**说明** 

当同时设置[fontVariations属性](ts-basic-components-span.md#fontvariations)时，fontVariations属性的优先级更高。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [FontWeight](ts-appendix-enums.md#fontweight) | [ResourceStr](ts-types.md#resourcestr) | 是 | 文本的字体粗细。  number类型取值[100, 900]，取值间隔为100，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular”、“medium”，分别对应FontWeight中相应的枚举值。设置过大可能会在不同字体下有截断。传入超出取值范围或不符合间隔要求的值时取默认值。  从API version 20开始，支持[Resource](ts-types.md#resource)类型。 |

### fontWeight24+

fontWeight(weight: number | FontWeight | ResourceStr, fontWeightConfigs?: FontWeightConfigs)

设置文本的字体粗细。未通过该接口设置时，默认字体粗细为FontWeight.Normal（正常粗细，对应数值400）。

**说明** 

当同时设置fontVariations属性时，fontVariations属性的优先级更高。

**卡片能力：** 从API version 24开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| weight | number | [FontWeight](ts-appendix-enums.md#fontweight) | [ResourceStr](ts-types.md#resourcestr) | 是 | 文本的字体粗细。  number类型取值[100, 900]，取值间隔为100，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular”、“medium”，分别对应FontWeight中相应的枚举值。设置过大可能会在不同字体下有截断。  传入超出取值范围的值时取默认值。传入不符合间隔要求的值时，若设置fontWeightConfigs的enableVariableFontWeight为true，使用传入值；若设置为false，使用默认值。 |
| fontWeightConfigs | [FontWeightConfigs](ts-text-common.md#fontweightconfigs24对象说明) | 否 | 字体粗细配置对象，用于配置可变字体字重等选项。默认值继承[FontWeightConfigs](ts-text-common.md#fontweightconfigs24对象说明)。 |

### fontFamily

fontFamily(value: string | Resource)

设置字体列表。未通过该接口设置时，默认字体为'HarmonyOS Sans'。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [Resource](ts-types.md#resource) | 是 | 字体列表。  使用多个字体时，请用逗号','分隔，字体的优先级按顺序生效。例如：'Arial,HarmonyOS Sans'。 |

**说明** 

可以使用[loadFontSync](js-apis-graphics-text.md#loadfontsync)注册自定义字体。

### lineHeight10+

lineHeight(value: Length)

设置文本行高。未通过该接口设置时，默认由系统根据字体大小自动计算行高。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 文本行高。  number类型时单位为fp。设置string类型时，支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"，不支持设置百分比字符串。 |

### font10+

font(value: Font)

设置文本样式。包括字体大小、字体粗细、字体族和字体风格。

**说明** 

fontWeight设置过大可能会在不同字体下有截断。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](ts-types.md#font) | 是 | 文本样式，包括字体大小、字体粗细、字体族和字体风格。 |

### font24+

font(value: Font, fontConfigs?: FontConfigs)

设置文本样式。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](ts-types.md#font) | 是 | 文本样式，包括字体大小、字体粗细、字体族和字体风格。 |
| fontConfigs | [FontConfigs](ts-text-common.md#fontconfigs24对象说明) | 否 | 字体配置，用于自定义字体渲染行为（如配置可变字体属性）。当需要对字体进行高级配置时传入此参数，不传入时继承[FontConfigs](ts-text-common.md#fontconfigs24对象说明)的默认配置。 |

### textShadow11+

textShadow(value: ShadowOptions | Array<ShadowOptions>)

设置文字阴影效果。该接口支持以数组形式入参，实现多重文字阴影。不支持fill字段，不支持智能取色模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明) | Array<[ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明)> | 是 | 文字阴影效果。可设置阴影的模糊半径(radius)、颜色(color)、偏移距离(offsetX/offsetY)等参数，支持数组形式实现多重阴影。 |

### fontVariations

fontVariations(fontVariations: Array<FontVariation>)

设置可变字体的属性，适用于需要动态调整字体粗细、宽度等可变维度参数的场景。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fontVariations | Array<[FontVariation](js-apis-graphics-text.md#fontvariation)> | 是 | 可变字体的属性数组，每个数组元素包含axis（属性轴名称）和value（属性值）两个字段。fontVariations属性的优先级高于[fontWeight](ts-basic-components-span.md#fontweight24)。 |

## 事件

通用事件支持[点击事件onClick](ts-universal-events-click.md#onclick)、[悬浮事件onHover](ts-universal-events-hover.md#onhover)。

**说明** 

由于Span组件无尺寸信息，因此点击事件返回的ClickEvent对象的target属性无效。

## BaseSpan

定义BaseSpan基础类，包含Span的通用属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

### textBackgroundStyle11+

textBackgroundStyle(style: TextBackgroundStyle): T

设置文本背景样式。作为[ContainerSpan](ts-basic-components-containerspan.md)的子组件时可继承该属性值，优先使用自身的设置。未通过该接口设置时，默认背景颜色为Color.Transparent（透明），圆角弧度为0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [TextBackgroundStyle](ts-basic-components-span.md#textbackgroundstyle11对象说明) | 是 | 文本背景样式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前Span的属性对象。 |

### baselineOffset12+

baselineOffset(value: LengthMetrics): T

设置Span基线的偏移量，适用于上下标排版、混合字号文本对齐微调等场景。此属性与父组件的baselineOffset是共存的。未通过该接口设置时，默认偏移量为0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 是 | 设置Span基线的偏移量，设置该值为百分比时，按默认值显示。  正数内容向上偏移，负数向下偏移。  在ImageSpan中，设置为非0时，[verticalAlign](ts-basic-components-imagespan.md#verticalalign)将固定为ImageSpanAlignment.BASELINE对齐；设置为0时，要使基线对齐策略生效，需同时设置[verticalAlign](ts-basic-components-imagespan.md#verticalalign)为ImageSpanAlignment.BASELINE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前Span的属性对象，用于链式调用。 |

## TextBackgroundStyle11+对象说明

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 文本背景色。默认为透明，无背景色。 |
| radius | [Dimension](ts-types.md#dimension10) | [BorderRadiuses](ts-types.md#borderradiuses9) | 否 | 是 | 文本背景圆角。默认无圆角。 |

## 示例

### 示例1（设置文本样式）

该示例展示了设置不同样式的文本效果以及Span配置点击事件。

```ts
// xxx.ets
@Entry
@Component
struct SpanExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
      Text('Basic Usage').fontSize(9).fontColor(0xCCCCCC)
      Text() {
        Span('In Line')
        Span(' Component')
        Span(' !')
      }

      Text() {
        Span('This is the Span component').fontSize(12).textCase(TextCase.Normal)
          .decoration({ type: TextDecorationType.None, color: Color.Red })
          .fontFamily('HarmonyOS Sans')
      }.margin({ top: 12 })

      // 文本横线添加
      Text('Text Decoration').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('I am Underline-WAVY-span')
          .decoration({ type: TextDecorationType.Underline, color: Color.Red, style: TextDecorationStyle.WAVY })
          .fontSize(12)
      }

      Text() {
        Span('I am LineThrough-DOTTED-span')
          .decoration({ type: TextDecorationType.LineThrough, color: Color.Red, style: TextDecorationStyle.DOTTED })
          .fontSize(12)
      }

      Text() {
        Span('I am Overline-DASHED-span')
          .decoration({ type: TextDecorationType.Overline, color: Color.Red, style: TextDecorationStyle.DASHED })
          .fontSize(12)
      }

      // 文本字符间距
      Text('LetterSpacing').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('span letter spacing')
          .letterSpacing(0)
          .fontSize(12)
      }

      Text() {
        Span('span letter spacing')
          .letterSpacing(-2)
          .fontSize(12)
      }

      Text() {
        Span('span letter spacing')
          .letterSpacing(3)
          .fontSize(12)
      }

      // 文本大小写展示设置
      Text('Text Case').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('I am Lower-span').fontSize(12)
          .textCase(TextCase.LowerCase)
          .decoration({ type: TextDecorationType.None })
      }

      Text() {
        Span('I am Upper-span').fontSize(12)
          .textCase(TextCase.UpperCase)
          .decoration({ type: TextDecorationType.None })
      }

      // 文本字体样式设置
      Text('FontStyle').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('I am FontStyle-Normal').fontSize(12)
          .fontStyle(FontStyle.Normal)
      }

      Text() {
        Span('I am FontStyle-Italic').fontSize(12)
          .fontStyle(FontStyle.Italic)
      }

      // 文本字体粗细设置
      Text('FontWeight').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('I am FontWeight-Lighter').fontSize(12)
          .fontWeight(FontWeight.Lighter)
      }

      Text() {
        Span('I am FontWeight-Bold').fontSize(12)
          .fontWeight(FontWeight.Bold)
      }

      // 文本行高设置
      Text('LineHeight').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('I am lineHeight default\n').fontSize(12)
          .fontWeight(FontWeight.Lighter)
        Span('I am lineHeight 30').fontSize(12)
          .lineHeight(30)
      }
      .backgroundColor(Color.Gray)

      // 文本样式设置
      Text('Font').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('span font 12 Bolder Italic')
          .font({
            size: 12,
            weight: FontWeight.Bolder,
            style: FontStyle.Italic,
            family: "HarmonyOS Sans"
          })
      }

      // 文本字体配置设置。从API version 24开始新增支持fontConfigs属性。
      Text('Font with FontConfigs').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('span font with configs')
          .font({
            size: 14,
            weight: 550,
            style: FontStyle.Normal,
            family: "HarmonyOS Sans"
          }, {
            fontWeightConfigs: {
              enableVariableFontWeight: true
            }
          })
      }

      // 文本字体粗细配置设置。从API version 24开始新增支持fontWeightConfigs属性。
      Text('FontWeight with FontWeightConfigs').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('span fontWeight 850 with configs')
          .fontWeight(850, {
            enableVariableFontWeight: true,
            enableDeviceFontWeightCategory: false
          })
      }
      Text() {
        Span('span fontWeight 600 with configs')
          .fontWeight(600, {
            enableVariableFontWeight: false,
            enableDeviceFontWeightCategory: true
          })
      }

      // span点击事件设置
      Text('span click event').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
      Text() {
        Span('Span default ').fontSize(12)
        Span('Span click')
          .onClick((event) => {
            console.info("span onClick")
          })
      }
    }.width('100%').padding({ left: 35, right: 35, top: 35 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/Wvg90iMGRGGof5SWix3inw/zh-cn_image_0000002742005179.png)

### 示例2（设置文本阴影）

从API version 11开始，该示例通过[textShadow](ts-basic-components-span.md#textshadow11)属性展示了文本设置阴影的效果。

```ts
// xxx.ets
@Entry
@Component
struct SpanExample {
  @State textShadows: ShadowOptions | Array<ShadowOptions> = [{
    radius: 10,
    color: Color.Red,
    offsetX: 10,
    offsetY: 0
  }, {
    radius: 10,
    color: Color.Orange,
    offsetX: 20,
    offsetY: 0
  },
    {
      radius: 10,
      color: Color.Yellow,
      offsetX: 30,
      offsetY: 0
    }, {
      radius: 10,
      color: Color.Green,
      offsetX: 40,
      offsetY: 0
    },
    {
      radius: 10,
      color: Color.Blue,
      offsetX: 100,
      offsetY: 0
    }]

  build() {
    Column({ space: 8 }) {
      Text() {
        Span('123456789').fontSize(50).textShadow(this.textShadows).fontColor(Color.Pink)
      }

      Text() {
        Span('123456789') // span can inherit text shadow & font size from outer text
      }.fontSize(50).textShadow(this.textShadows).fontColor(Color.Pink)
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/j2e-150UR46EvSE-PrcYbA/zh-cn_image_0000002712406190.png)

### 示例3（设置背景样式）

从API version 11开始，该示例通过[textBackgroundStyle](ts-basic-components-span.md#textbackgroundstyle11)属性展示了文本设置背景样式的效果。

```ts
// xxx.ets
@Component
@Entry
struct SpanExample {
  build() {
    Column() {
      Text() {
        Span('   Hello World !   ')
          .fontSize('20fp')
          .textBackgroundStyle({ color: '#7F007DFF', radius: '5vp' })
          .fontColor(Color.White)
      }
    }.width('100%').margin({ bottom: '5vp' }).alignItems(HorizontalAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/y8WgfA2FRY6rwm4CjKzl4w/zh-cn_image_0000002742125139.png)

### 示例4（设置文本基线偏移量）

从API version 12开始，该示例通过[baselineOffset](ts-basic-components-span.md#baselineoffset12)属性展示了文本设置不同基线偏移量的效果。

```ts
// xxx.ets
import { LengthUnit, LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct SpanExample {
  build() {
    Row() {
      Column() {
        Text() {
          Span('SpanOne')
            .fontSize(10)
            .baselineOffset(new LengthMetrics(20, LengthUnit.VP))
          Span('SpanTwo')
            .fontSize(10)
            .baselineOffset(new LengthMetrics(0, LengthUnit.VP))
          // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
          ImageSpan($r("app.media.sky"))
            .width('80px')
            .baselineOffset(new LengthMetrics(-20, LengthUnit.VP))
        }
        .backgroundColor('#7F007DFF')
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/YLeSgoGwRhW6a6UlIplhFw/zh-cn_image_0000002712246232.png)

### 示例5（设置文本可变字体的属性）

该示例通过[fontVariations](ts-basic-components-span.md#fontvariations)属性设置可变字体的属性。

从API版本26.0.0开始，新增[fontVariations](ts-basic-components-span.md#fontvariations)接口。

```ts
// xxx.ets
@Entry
@Component
struct SpanExample {
  @State weightValue: number = 400;

  build() {
    Column() {
      Text() {
        Span('Hello World !')
          // wght代表可变字体的字重属性
          .fontVariations([{ axis: 'wght', value: this.weightValue }])
      }

      Button('字重: ' + this.weightValue)
        .margin(10)
        .onClick(() => {
          this.weightValue += 100;
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/1tQzzJ3bQEWPa-buMJwTow/zh-cn_image_0000002712246156.gif)
