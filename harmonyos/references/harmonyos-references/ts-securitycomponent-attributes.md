---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-securitycomponent-attributes
title: 安全控件通用属性
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 安全 > 安全控件通用属性
category: harmonyos-references
scraped_at: 2026-04-28T08:02:25+08:00
doc_updated_at: 2026-04-03
content_hash: sha256:bc2370ca15eddaff3bf2cd9355ba89ca57caceb8378b05a20d9bb7f2054e9313
---

安全控件的基础属性，用于设置安全控件通用的属性。

说明

该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## iconSize

PhonePC/2in1TabletTVWearable

iconSize(value: Dimension): T

设置安全控件图标的尺寸。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | 是 | 安全控件上图标的尺寸。  默认值：16vp。  不支持设置百分比字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## layoutDirection

PhonePC/2in1TabletTVWearable

layoutDirection(value: SecurityComponentLayoutDirection): T

设置安全控件图标和文字分布的方向。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SecurityComponentLayoutDirection](ts-securitycomponent-attributes.md#securitycomponentlayoutdirection枚举说明) | 是 | 安全控件上图标和文字分布的方向。  默认值：SecurityComponentLayoutDirection.HORIZONTAL。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## position

PhonePC/2in1TabletTVWearable

position(value: Position): T

设置绝对定位，设置安全控件的左上角相对于父容器左上角的偏移位置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Position](ts-types.md#position) | 是 | 安全控件的左上角相对于父容器左上角的偏移位置。  **异常情况说明**：  1.当入参为异常值（如入参不符合Position定义等）、入参为Position类型但x和y均为异常值（如undefined或其他与格式要求不符的字符串等）时，该属性不生效；  2.当入参的Position中，x和y有且仅有一个异常值时，值异常的属性会被置为0。如输入{x: 0, y: 'a'}，最终效果按{x: 0, y: 0}显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## markAnchor

PhonePC/2in1TabletTVWearable

markAnchor(value: Position): T

设置安全控件在位置定位时的锚点，以控件左上角作为基准点进行偏移。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Position](ts-types.md#position) | 是 | 安全控件在位置定位时的锚点，以控件左上角作为基准点进行偏移。通常配合position和offset属性使用，单独使用时，效果类似offset。  无默认值，设置异常值时该属性不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## offset

PhonePC/2in1TabletTVWearable

offset(value: Position | Edges | LocalizedEdges): T

设置安全控件相对于自身布局位置的坐标偏移。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Position](ts-types.md#position) | [Edges12+](ts-types.md#edges12) | [LocalizedEdges12+](ts-types.md#localizededges12) | 是 | 安全控件相对于自身布局位置的坐标偏移。设置此属性不会影响父容器的布局，仅在绘制过程中调整位置。  无默认值，设置异常值时该属性不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## fontSize

PhonePC/2in1TabletTVWearable

fontSize(value: Dimension): T

设置安全控件文字的尺寸。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | 是 | 安全控件上文字的尺寸。  默认值：16fp。  不支持设置百分比字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## fontStyle

PhonePC/2in1TabletTVWearable

fontStyle(value: FontStyle): T

设置安全控件文字的样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FontStyle](ts-appendix-enums.md#fontstyle) | 是 | 安全控件上文字的样式。  默认值：FontStyle.Normal。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## fontWeight

PhonePC/2in1TabletTVWearable

fontWeight(value: number | FontWeight | string | Resource): T

设置安全控件文字粗细。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [FontWeight](ts-appendix-enums.md#fontweight) | string | [Resource](ts-types.md#resource)20+ | 是 | 安全控件上文字粗细。  number类型取值[100, 900]，取值间隔为100，取值越大，字体越粗。  string类型支持使用数字字符串（如'400'），以及FontWeight中的枚举值对应的字符串（如'bold'、'bolder'、'lighter'、'regular'、'medium'）。  从API version 20开始，支持Resource类型。Resource类型仅支持'integer'和'string'，当类型为'integer'时，取值参考前述number类型；当类型为'string'时，取值参考前述string类型。  如果控件未设置fontWeight，文字粗细将默认设置为FontWeight.Medium；如果value入参为非法值，文字粗细将被设置为FontWeight.Normal。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## fontFamily

PhonePC/2in1TabletTVWearable

fontFamily(value: string | Resource): T

设置安全控件文字的字体。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [Resource](ts-types.md#resource) | 是 | 安全控件上文字的字体。  默认字体：'HarmonyOS Sans'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## fontColor

PhonePC/2in1TabletTVWearable

fontColor(value: ResourceColor): T

设置安全控件文字的颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 安全控件上文字的颜色。  默认值：$r('sys.color.font\_on\_primary')。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## iconColor

PhonePC/2in1TabletTVWearable

iconColor(value: ResourceColor): T

设置安全控件图标的颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 安全控件上图标的颜色。  默认值：$r('sys.color.icon\_on\_primary')。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## backgroundColor

PhonePC/2in1TabletTVWearable

backgroundColor(value: ResourceColor): T

设置安全控件的背景颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 安全控件的背景颜色。安全控件按钮背景色高八位的α值低于0x1a（例如0x1800ff00）时，安全控件按钮背景色高八位的α值会被系统强制调整为0xff。  默认值：$r('sys.color.icon\_emphasize')。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## borderStyle

PhonePC/2in1TabletTVWearable

borderStyle(value: BorderStyle): T

设置安全控件的边框的样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BorderStyle](ts-appendix-enums.md#borderstyle) | 是 | 安全控件的边框的样式。  默认不设置边框样式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## borderWidth

PhonePC/2in1TabletTVWearable

borderWidth(value: Dimension): T

设置安全控件的边框宽度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | 是 | 安全控件的边框宽度。  默认不设置边框宽度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## borderColor

PhonePC/2in1TabletTVWearable

borderColor(value: ResourceColor): T

设置安全控件的边框颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 安全控件的边框颜色。  默认不设置边框颜色。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## borderRadius

PhonePC/2in1TabletTVWearable

borderRadius(value: Dimension): T

设置安全控件的边框圆角半径。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | 是 | 安全控件的边框圆角半径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## borderRadius15+

PhonePC/2in1TabletTVWearable

borderRadius(radius: Dimension | BorderRadiuses): T

设置安全控件的边框圆角半径，支持分别设置四个圆角的半径。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | [Dimension](ts-types.md#dimension10) | [BorderRadiuses](ts-types.md#borderradiuses9) | 是 | 安全控件的边框圆角半径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## padding

PhonePC/2in1TabletTVWearable

padding(value: Padding | Dimension): T

设置安全控件的内边距。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Padding](ts-types.md#padding) | [Dimension](ts-types.md#dimension10) | 是 | 安全控件的内边距。  默认值：上下8vp，左右16vp。  **说明**：本参数不支持设置百分比字符串数据类型。若设置百分比字符串，则对应内边距显示为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## align15+

PhonePC/2in1TabletTVWearable

align(alignType: Alignment): T

设置安全控件图标文本的对齐方式。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignType | [Alignment](ts-appendix-enums.md#alignment) | 是 | 安全控件图标文本的对齐方式。图标文本作为整体在控件背托范围内进行对齐，UX显示受[padding](ts-securitycomponent-attributes.md#padding)影响，在padding生效的基础上进行指定方式对齐。  默认值：Alignment.Center。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## textIconSpace

PhonePC/2in1TabletTVWearable

textIconSpace(value: Dimension): T

设置安全控件中图标和文字的间距。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | 是 | 安全控件中图标和文字的间距。  默认值：4vp。  **说明**：本参数不支持设置百分比字符串数据类型，若设置百分比字符串，则图标和文字的间距显示为0；从API 14开始，若设置值为负值，则使用默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## width11+

PhonePC/2in1TabletTVWearable

width(value: Length): T

设置安全控件自身的宽度，缺省时将根据元素内容自适配宽度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 安全控件自身的宽度，缺省时将根据元素内容自适配宽度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## height11+

PhonePC/2in1TabletTVWearable

height(value: Length): T

设置安全控件自身的高度，缺省时将根据元素内容自适配高度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 安全控件自身的高度，缺省时将根据元素内容自适配高度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## size11+

PhonePC/2in1TabletTVWearable

size(value: SizeOptions): T

设置宽高尺寸，缺省时将根据元素内容自适配高宽尺寸。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SizeOptions](ts-types.md#sizeoptions) | 是 | 宽高尺寸，缺省时将根据元素内容自适配高宽尺寸。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## constraintSize11+

PhonePC/2in1TabletTVWearable

constraintSize(value: ConstraintSizeOptions): T

设置约束尺寸，组件布局时限制尺寸范围。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ConstraintSizeOptions](ts-types.md#constraintsizeoptions) | 是 | 约束尺寸，组件布局时，进行尺寸范围限制。未显式指定单位时，单位为vp。constraintSize的优先级高于Width和Height。取值结果参考[constraintSize取值对width/height影响](ts-universal-attributes-size.md#constraintsize)。  默认值：  {  minWidth: 0,  maxWidth: Infinity,  minHeight: 0,  maxHeight: Infinity  }。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## alignRules15+

PhonePC/2in1TabletTVWearable

alignRules(alignRule: AlignRuleOption): T

指定设置在相对容器中子组件的对齐规则，仅当父容器为[RelativeContainer](ts-container-relativecontainer.md)时生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignRule | [AlignRuleOption](ts-universal-attributes-location.md#alignruleoption9对象说明) | 是 | 指定设置在相对容器中子组件的对齐规则。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## alignRules15+

PhonePC/2in1TabletTVWearable

alignRules(alignRule: LocalizedAlignRuleOptions): T

指定设置在相对容器中子组件的对齐规则，仅当父容器为[RelativeContainer](ts-container-relativecontainer.md)时生效。该方法水平方向上以start和end分别替代上述[alignRules](ts-securitycomponent-attributes.md#alignrules15)的left和right，以便在RTL模式下能镜像显示，建议使用该方法指定设置在相对容器中子组件的对齐规则。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignRule | [LocalizedAlignRuleOptions](ts-universal-attributes-location.md#localizedalignruleoptions12对象说明) | 是 | 指定设置在相对容器中子组件的对齐规则。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## id15+

PhonePC/2in1TabletTVWearable

id(description: string): T

组件的唯一标识，唯一性由使用者保证。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| description | string | 是 | 组件的唯一标识，唯一性由使用者保证。  默认值：''。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## chainMode15+

PhonePC/2in1TabletTVWearable

chainMode(direction: Axis, style: ChainStyle): T

指定以该组件为链头所构成的链的参数，仅当父容器为[RelativeContainer](ts-container-relativecontainer.md)时生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| direction | [Axis](ts-appendix-enums.md#axis) | 是 | 链的方向。 |
| style | [ChainStyle](ts-universal-attributes-location.md#chainstyle12) | 是 | 链的样式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## minFontScale18+

PhonePC/2in1TabletTVWearable

minFontScale(scale: number | Resource): T

设置文本最小的字体缩小倍数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | number | [Resource](ts-types.md#resource) | 是 | 文本最小的字体缩小倍数。  取值范围：[0, 1]。  **说明：**  设置的值小于0时，按值为0处理，即缩小不受限制；设置的值大于1，按值为1处理，即缩小不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## maxFontScale18+

PhonePC/2in1TabletTVWearable

maxFontScale(scale: number | Resource): T

设置文本最大的字体放大倍数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | number | [Resource](ts-types.md#resource) | 是 | 文本最大的字体放大倍数。  取值范围：[1, +∞)。  **说明：**  设置的值小于1时，按值为1处理，异常值默认不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## minFontSize18+

PhonePC/2in1TabletTVWearable

minFontSize(minSize: number | string | Resource): T

设置文本最小显示字号。

* 配合[maxFontSize](ts-securitycomponent-attributes.md#maxfontsize18)以及[maxLines](ts-securitycomponent-attributes.md#maxlines18)或布局大小限制使用，可实现自适应字号，单独设置不生效。
* minFontSize小于或等于0时，自适应字号不生效。
* 自适应字号生效时，fontSize设置不生效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| minSize | number | string | [Resource](ts-types.md#resource) | 是 | 文本最小显示字号。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## maxFontSize18+

PhonePC/2in1TabletTVWearable

maxFontSize(maxSize: number | string | Resource): T

设置文本最大显示字号。

* 配合[minFontSize](ts-securitycomponent-attributes.md#minfontsize18)以及[maxLines](ts-securitycomponent-attributes.md#maxlines18)或布局大小限制使用，可实现自适应字号，单独设置不生效。
* 当自适应字号生效时，设置的fontSize将不生效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxSize | number | string | [Resource](ts-types.md#resource) | 是 | 文本最大显示字号。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## maxLines18+

PhonePC/2in1TabletTVWearable

maxLines(line: number | Resource): T

设置文本的最大行数。默认情况下，文本自动换行，指定此属性后，文本的最大显示行数不会超过指定值。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| line | number | [Resource](ts-types.md#resource)20+ | 是 | 文本的最大行数。  number类型入参的取值范围：[1, +∞)。从API version 20开始，支持Resource类型。Resource类型仅支持'integer'，取值范围为[1, +∞)。  **说明：**  设置的值小于1时，按默认值1000000处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## heightAdaptivePolicy18+

PhonePC/2in1TabletTVWearable

heightAdaptivePolicy(policy: TextHeightAdaptivePolicy): T

设置文本自适应高度的方式。

通过文本自适应高度实现文本大小自适应。

安全控件文本以[maxFontSize](ts-securitycomponent-attributes.md#maxfontsize18)的值进行布局，如果可以完整显示文本，则无需进行自适应调节，该接口设置不生效，否则按指定文本自适应高度的方式进行调节，具体自适应调节规格如下：

当设置为TextHeightAdaptivePolicy.MAX\_LINES\_FIRST时，优先使用[maxLines](ts-securitycomponent-attributes.md#maxlines18)属性来调整文本高度。如果使用maxLines属性的布局大小超过了布局约束，则尝试在[minFontSize](ts-securitycomponent-attributes.md#minfontsize18)和[maxFontSize](ts-securitycomponent-attributes.md#maxfontsize18)的范围内缩小字体以显示更多文本，如果此时仍不能完整显示文本信息，安全控件会自适应调整高度以使得文本完整显示。

当设置为TextHeightAdaptivePolicy.MIN\_FONT\_SIZE\_FIRST时，优先使用[minFontSize](ts-securitycomponent-attributes.md#minfontsize18)属性来调整文本高度。如果使用minFontSize属性可以将文本布局在一行中，则尝试在minFontSize和[maxFontSize](ts-securitycomponent-attributes.md#maxfontsize18)的范围内增大字体并使用最大可能的字体大小；如果使用minFontSize属性无法将文本布局在一行中，则尝试使用[maxLines](ts-securitycomponent-attributes.md#maxlines18)属性进行布局，如果此时仍不能完整显示文本信息，安全控件会自适应调整高度以使得文本完整显示。

当设置为TextHeightAdaptivePolicy.LAYOUT\_CONSTRAINT\_FIRST时，优先使用布局约束来调整文本高度。如果布局大小超过布局约束，则尝试在[minFontSize](ts-securitycomponent-attributes.md#minfontsize18)和[maxFontSize](ts-securitycomponent-attributes.md#maxfontsize18)的范围内缩小字体以满足布局约束。如果将字体大小缩小到minFontSize后，布局大小仍然超过布局约束，则删除超过布局约束的行；如果设置了[maxLines](ts-securitycomponent-attributes.md#maxlines18)属性，布局后行数不超过maxlines值（可能存在横向截断）；如果未设置maxlines属性值，布局后的行数不限制。

安全控件文本未完全显示时，点击不授权。

具体效果请见[示例](ts-securitycomponent-attributes.md#示例3)。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policy | [TextHeightAdaptivePolicy](ts-appendix-enums.md#textheightadaptivepolicy10) | 是 | 文本自适应高度的方式。  默认值：TextHeightAdaptivePolicy.MAX\_LINES\_FIRST。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## enabled18+

PhonePC/2in1TabletTVWearable

enabled(respond: boolean): T

设置安全控件是否可交互。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| respond | boolean | 是 | 值为true表示组件可交互，响应点击等操作。  值为false表示组件不可交互，不响应点击等操作。  默认值：true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## focusBox22+

PhonePC/2in1TabletTVWearable

focusBox(style: FocusBoxStyle): T

设置安全控件系统焦点框样式。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [FocusBoxStyle](ts-universal-attributes-focus.md#focusboxstyle12对象说明) | 是 | 设置安全控件系统焦点框样式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回安全控件的属性。 |

## SecurityComponentLayoutDirection枚举说明

PhonePC/2in1TabletTVWearable

安全控件上图标和文字的排列方向。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HORIZONTAL | 0 | 安全控件上图标和文字分布的方向为水平排列。 |
| VERTICAL | 1 | 安全控件上图标和文字分布的方向为垂直排列。 |

## ButtonType枚举说明

PhonePC/2in1TabletTVWearable

按钮类型。

不同的按钮类型将影响属性[borderRadius（边框圆角半径）](ts-securitycomponent-attributes.md#borderradius)的设置效果。影响如下：

* 当按钮类型为Capsule时，borderRadius设置不生效，按钮圆角半径始终为宽、高中较小值的一半。
* 当按钮类型为Circle时，borderRadius设置不生效：
  + 若同时设置了宽和高，按钮圆角半径为宽高中较小值的一半；
  + 若只设置宽、高中的一个，按钮圆角半径为所设宽或所设高值的一半；
  + 若未设置宽高或borderRadius的值为负数，按钮圆角半径将根据具体布局确定。
* 当按钮类型为Normal时，按钮圆角半径可通过borderRadius设置，圆角大小受组件尺寸限制，最小值为0，最大值为组件宽高中较小值的一半。
* 当按钮类型为ROUNDED\_RECTANGLE时，若不设置borderRadius，圆角矩形按钮的圆角半径大小保持默认值20vp不变，不随按钮高度变化而变化。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Normal | 0 | 普通按钮（默认不带圆角）。 |
| Capsule | 1 | 胶囊型按钮（圆角半径默认为高度的一半）。 |
| Circle | 2 | 圆形按钮。 |
| ROUNDED\_RECTANGLE16+ | 8 | 圆角矩形按钮（默认值：圆角半径大小20vp）。 |

## 示例

PhonePC/2in1TabletTVWearable

说明

为避免控件样式不合法导致授权失败，请开发者先了解安全控件样式的[约束与限制](../harmonyos-guides/security-component-overview.md#约束与限制)。

### 示例1

设置SecurityComponent的基础属性，生成一个保存控件。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Row() {
6. Column({ space: 5 }) {
7. // 生成一个保存控件，并设置它的SecurityComponent属性。
8. SaveButton()
9. .fontSize(35)
10. .fontColor(Color.White)
11. .iconSize(30)
12. .layoutDirection(SecurityComponentLayoutDirection.HORIZONTAL)
13. .borderWidth(1)
14. .borderStyle(BorderStyle.Dashed)
15. .borderColor(Color.Blue)
16. .borderRadius(20)
17. .fontWeight(100)
18. .iconColor(Color.White)
19. .padding({
20. left: 50,
21. top: 50,
22. bottom: 50,
23. right: 50
24. })
25. .textIconSpace(20)
26. .backgroundColor(0x3282f6)
27. SaveButton().size({ width: 200, height: 100 })
28. SaveButton()
29. .size({ width: 200, height: 100 })
30. .align(Alignment.Start)
31. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD, buttonType: ButtonType.Normal })
32. .size({ width: 150, height: 80 })
33. .borderRadius({
34. topLeft: 20,
35. topRight: 25,
36. bottomRight: 30,
37. bottomLeft: 35
38. })
39. SaveButton().constraintSize({ maxWidth: 60 })
40. }.width('100%')
41. }.height('100%')
42. }
43. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/tD6L60fDTn6cOyTm6tAbOQ/zh-cn_image_0000002583440119.png?HW-CC-KV=V1&HW-CC-Date=20260428T000224Z&HW-CC-Expire=86400&HW-CC-Sign=CDDDC985D2F03E31212C0549EBBC509839A96B54BD0B3738ED1C6C43139450E8)

### 示例2

以容器和容器内组件作为锚点进行布局。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Row() {
6. RelativeContainer() {
7. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD, buttonType: ButtonType.Normal })
8. .width(100)
9. .height(100)
10. .backgroundColor('#A3CF62')
11. .alignRules({
12. top: { anchor: '__container__', align: VerticalAlign.Top },
13. left: { anchor: '__container__', align: HorizontalAlign.Start }
14. })
15. .id('row1')

17. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD, buttonType: ButtonType.Normal })
18. .width(100)
19. .height(100)
20. .backgroundColor('#00AE9D')
21. .alignRules({
22. top: { anchor: '__container__', align: VerticalAlign.Top },
23. right: { anchor: '__container__', align: HorizontalAlign.End }
24. })
25. .id('row2')

27. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD, buttonType: ButtonType.Normal })
28. .height(100)
29. .backgroundColor('#0A59F7')
30. .alignRules({
31. top: { anchor: 'row1', align: VerticalAlign.Bottom },
32. left: { anchor: 'row1', align: HorizontalAlign.End },
33. right: { anchor: 'row2', align: HorizontalAlign.Start }
34. })
35. .id('row3')

37. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD, buttonType: ButtonType.Normal })
38. .backgroundColor('#2CA9E0')
39. .alignRules({
40. top: { anchor: 'row3', align: VerticalAlign.Bottom },
41. bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
42. left: { anchor: '__container__', align: HorizontalAlign.Start },
43. right: { anchor: 'row1', align: HorizontalAlign.End }
44. })
45. .id('row4')

47. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD, buttonType: ButtonType.Normal })
48. .backgroundColor('#30C9F7')
49. .alignRules({
50. top: { anchor: 'row3', align: VerticalAlign.Bottom },
51. bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
52. left: { anchor: 'row2', align: HorizontalAlign.Start },
53. right: { anchor: '__container__', align: HorizontalAlign.End }
54. })
55. .id('row5')
56. }
57. .width(300).height(300)
58. .margin({ left: 50 })
59. .border({ width: 2, color: '#6699FF' })
60. }
61. .height('100%')
62. }
63. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/BSUc65N6Sci56vSxpgjRcQ/zh-cn_image_0000002552960074.png?HW-CC-KV=V1&HW-CC-Date=20260428T000224Z&HW-CC-Expire=86400&HW-CC-Sign=1D56A582ADC96937C47D4DBC0F49BB49367A8C4D39E77246BFA55B6F16122130)

### 示例3

安全控件文本高度自适应。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Column() {
6. Scroll() {
7. Column({ space: 10 }) {
8. Column({ space: 10 }) {
9. Row() {
10. Text('FontSize = 20，图例：').fontSize(20)
11. Text('快速保存图片').fontSize(20).fontColor(Color.Blue)
12. }.width('100%')

14. Row() {
15. Text('FontSize = 10，图例：').fontSize(20)
16. Text('快速保存图片').fontSize(10).fontColor(Color.Blue)
17. }.width('100%')
18. }.width('100%')

20. Flex({ wrap: FlexWrap.Wrap }) {
21. Column() {
22. Row() {
23. Text('heightAdaptivePolicy = MIN_FONT_SIZE_FIRST').fontSize(16).fontWeight(FontWeight.Bold)
24. }
25. }.height(40)

27. Column() {
28. Column({ space: 10 }) {
29. Row() {
30. Text('无需自适应调节')
31. }.width('90%')

33. // 当前布局无需调整即可完整显示文本，文本无需自适应调节。
34. SaveButton({
35. text: SaveDescription.QUICK_SAVE_TO_GALLERY, buttonType: ButtonType.Normal
36. })
37. .maxFontSize(20)
38. .minFontSize(10)
39. .maxLines(6)
40. .heightAdaptivePolicy(TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST)
41. .width(120)
42. .height(20)
43. .padding(0)
44. .borderRadius(10)
45. }
46. }.width('50%').height(90).backgroundColor(0x10000000)

48. Column() {
49. Column({ space: 10 }) {
50. Row() {
51. Text('优先减少字号')
52. }.width('90%')

54. // 当前布局无法完整显示文字，优先缩小fontSize，缩小后可以一行显示。
55. SaveButton({
56. text: SaveDescription.QUICK_SAVE_TO_GALLERY, buttonType: ButtonType.Normal
57. })
58. .maxFontSize(20)
59. .minFontSize(10)
60. .maxLines(6)
61. .heightAdaptivePolicy(TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST)
62. .width(60)
63. .height(20)
64. .padding(0)
65. .borderRadius(10)
66. }
67. }.width('50%').height(90).backgroundColor(0x30000000)

69. Column() {
70. Column({ space: 10 }) {
71. Row() {
72. Text('先减小字号，再换行')
73. }.width('90%')

75. // 当前布局无法完整显示文字，优先缩小fontSize，缩小后仍然无法完整显示，尝试使用maxLines属性换行布局。
76. // 由于高度不足以完整显示，自动调整高度使文本完整显示。
77. SaveButton({
78. text: SaveDescription.QUICK_SAVE_TO_GALLERY, buttonType: ButtonType.Normal
79. })
80. .maxFontSize(20)
81. .minFontSize(10)
82. .maxLines(6)
83. .heightAdaptivePolicy(TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST)
84. .width(20)
85. .height(20)
86. .padding(0)
87. .borderRadius(10)
88. }
89. }.width('50%').height(90).backgroundColor(0x30000000)

91. Column() {
92. Column({ space: 10 }) {
93. Row() {
94. Text('减小字号+换行，文字被截断')
95. }.width('90%')

97. // 当前布局无法完整显示文字，优先缩小fontSize，缩小后仍然无法完整显示，尝试使用maxLines属性换行布局。
98. // 由于maxlines属性为3，只能显示三行，所以文字被截断。
99. // 由于高度不足以完整显示，自动调整高度使文本完整显示。
100. SaveButton({
101. text: SaveDescription.QUICK_SAVE_TO_GALLERY, buttonType: ButtonType.Normal
102. })
103. .maxFontSize(20)
104. .minFontSize(10)
105. .maxLines(3)
106. .heightAdaptivePolicy(TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST)
107. .width(10)
108. .height(20)
109. .padding(0)
110. .borderRadius(10)
111. }
112. }.width('50%').height(90).backgroundColor(0x10000000)
113. }.width('100%')

115. Flex({ wrap: FlexWrap.Wrap }) {
116. Column() {
117. Row() {
118. Text('heightAdaptivePolicy = MAX_LINES_FIRST').fontSize(16).fontWeight(FontWeight.Bold)
119. }
120. }.height(40)

122. Column() {
123. Column({ space: 10 }) {
124. Row() {
125. Text('无需自适应调节')
126. }.width('90%')

128. // 当前布局无需调整即可完整显示文本，文本无需自适应调节。
129. SaveButton({
130. text: SaveDescription.QUICK_SAVE_TO_GALLERY, buttonType: ButtonType.Normal
131. })
132. .maxFontSize(20)
133. .minFontSize(10)
134. .maxLines(6)
135. .heightAdaptivePolicy(TextHeightAdaptivePolicy.MAX_LINES_FIRST)
136. .width(120)
137. .height(20)
138. .padding(0)
139. .borderRadius(10)
140. }
141. }.width('50%').height(90).backgroundColor(0x10000000)

143. Column() {
144. Column({ space: 10 }) {
145. Row() {
146. Text('优先换行')
147. }.width('90%')

149. // 当前布局无法完整显示文字，优先使用maxlines属性换行布局，换行后可以完整显示。
150. // 由于高度不足以完整显示，自动调整高度使文本完整显示。
151. SaveButton({
152. text: SaveDescription.QUICK_SAVE_TO_GALLERY, buttonType: ButtonType.Normal
153. })
154. .maxFontSize(20)
155. .minFontSize(10)
156. .maxLines(6)
157. .heightAdaptivePolicy(TextHeightAdaptivePolicy.MAX_LINES_FIRST)
158. .width(60)
159. .height(20)
160. .padding(0)
161. .borderRadius(10)
162. }
163. }.width('50%').height(90).backgroundColor(0x30000000)

165. Column() {
166. Column({ space: 10 }) {
167. Row() {
168. Text('先换行，再减小字号')
169. }.width('90%')

171. // 当前布局无法完整显示文字，优先使用maxlines属性换行布局，换行后仍然无法完整显示，缩小fontSize尝试布局，缩小字体后可以完整显示。
172. // 由于高度不足以完整显示，自动调整高度使文本完整显示。
173. SaveButton({
174. text: SaveDescription.QUICK_SAVE_TO_GALLERY, buttonType: ButtonType.Normal
175. })
176. .maxFontSize(20)
177. .minFontSize(10)
178. .maxLines(3)
179. .heightAdaptivePolicy(TextHeightAdaptivePolicy.MAX_LINES_FIRST)
180. .width(20)
181. .height(20)
182. .padding(0)
183. .borderRadius(10)
184. }
185. }.width('50%').height(90).backgroundColor(0x30000000)

187. Column() {
188. Column({ space: 10 }) {
189. Row() {
190. Text('换行+减小字号，文字被截断')
191. }.width('90%')

193. // 当前布局无法完整显示文字，优先使用maxlines属性换行布局，换行后仍然无法完整显示，缩小fontSize尝试布局。
194. // 由于minFontSize属性为10，每行只能显示一个字，所以文字被截断。
195. // 由于高度不足以完整显示，自动调整高度使文本完整显示。
196. SaveButton({
197. text: SaveDescription.QUICK_SAVE_TO_GALLERY, buttonType: ButtonType.Normal
198. })
199. .maxFontSize(20)
200. .minFontSize(10)
201. .maxLines(3)
202. .heightAdaptivePolicy(TextHeightAdaptivePolicy.MAX_LINES_FIRST)
203. .width(10)
204. .height(20)
205. .padding(0)
206. .borderRadius(10)
207. }
208. }.width('50%').height(90).backgroundColor(0x10000000)
209. }.width('100%')

211. Flex({ wrap: FlexWrap.Wrap }) {

213. Column() {
214. Row() {
215. Text('heightAdaptivePolicy = LAYOUT_CONSTRAINT_FIRST').fontSize(16).fontWeight(FontWeight.Bold)
216. }
217. }.height(40)

219. Column() {
220. Column({ space: 10 }) {
221. Row() {
222. Text('无需自适应调节')
223. }.width('90%')

225. // 当前布局无需调整即可完整显示文本，文本无需自适应调节。
226. SaveButton({
227. text: SaveDescription.QUICK_SAVE_TO_GALLERY, buttonType: ButtonType.Normal
228. })
229. .maxFontSize(20)
230. .minFontSize(10)
231. .maxLines(6)
232. .heightAdaptivePolicy(TextHeightAdaptivePolicy.LAYOUT_CONSTRAINT_FIRST)
233. .width(120)
234. .height(20)
235. .padding(0)
236. .borderRadius(10)
237. }
238. }.width('50%').height(90).backgroundColor(0x10000000)

240. Column() {
241. Column({ space: 10 }) {
242. Row() {
243. Text('不改变布局约束，优先减小字号')
244. }.width('90%')

246. // 当前布局无法完整显示文字，优先缩小fontSize，缩小后可以一行显示。
247. SaveButton({
248. text: SaveDescription.QUICK_SAVE_TO_GALLERY, buttonType: ButtonType.Normal
249. })
250. .maxFontSize(20)
251. .minFontSize(10)
252. .maxLines(6)
253. .heightAdaptivePolicy(TextHeightAdaptivePolicy.LAYOUT_CONSTRAINT_FIRST)
254. .width(60)
255. .height(20)
256. .padding(0)
257. .borderRadius(10)
258. }
259. }.width('50%').height(90).backgroundColor(0x30000000)

261. Column() {
262. Column({ space: 10 }) {
263. Row() {
264. Text('不改变布局约束，先减小字号再换行')
265. }.width('90%')

267. // 当前布局无法完整显示文字，优先缩小fontSize，缩小后无法完整显示，使用maxlines属性进行换行布局。布局后可以完整显示。
268. // LAYOUT_CONSTRAINT_FIRST模式下安全控件高度不支持自适应调整。
269. SaveButton({
270. text: SaveDescription.QUICK_SAVE_TO_GALLERY, buttonType: ButtonType.Normal
271. })
272. .maxFontSize(20)
273. .minFontSize(10)
274. .maxLines(6)
275. .heightAdaptivePolicy(TextHeightAdaptivePolicy.LAYOUT_CONSTRAINT_FIRST)
276. .width(20)
277. .height(40)
278. .padding(0)
279. .borderRadius(10)
280. }
281. }.width('50%').height(90).backgroundColor(0x30000000)

283. Column() {
284. Column({ space: 10 }) {
285. Row() {
286. Text(`Maxlines不够\n文字被截断`)
287. }.width('90%')

289. // 当前布局无法完整显示文字，优先缩小fontSize，缩小后无法完整显示，但由于height只能显示一行，所以文字被截断。
290. // LAYOUT_CONSTRAINT_FIRST模式下安全控件高度不支持自适应调整。
291. SaveButton({
292. text: SaveDescription.QUICK_SAVE_TO_GALLERY, buttonType: ButtonType.Normal
293. })
294. .maxFontSize(20)
295. .minFontSize(10)
296. .maxLines(2)
297. .heightAdaptivePolicy(TextHeightAdaptivePolicy.LAYOUT_CONSTRAINT_FIRST)
298. .width(20)
299. .height(40)
300. .padding(0)
301. .borderRadius(10)
302. }
303. }.width('25%').height(90).backgroundColor(0x10000000)

305. Column() {
306. Column({ space: 10 }) {
307. Row() {
308. Text(`高度不够\n文字被截断`)
309. }.width('90%')

311. // 当前布局无法完整显示文字，优先缩小fontSize，缩小后无法完整显示，但由于height只能显示一行，所以文字被截断。
312. // LAYOUT_CONSTRAINT_FIRST模式下安全控件高度不支持自适应调整。
313. SaveButton({
314. text: SaveDescription.QUICK_SAVE_TO_GALLERY, buttonType: ButtonType.Normal
315. })
316. .maxFontSize(20)
317. .minFontSize(10)
318. .maxLines(6)
319. .heightAdaptivePolicy(TextHeightAdaptivePolicy.LAYOUT_CONSTRAINT_FIRST)
320. .width(20)
321. .height(20)
322. .padding(0)
323. .borderRadius(10)
324. }
325. }.width('25%').height(90).backgroundColor(0x20000000)
326. }.width('100%')

328. }.width('100%')
329. }.width('100%').margin({ top: 10, left: 10, right: 10 })
330. }
331. }
332. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/WPVwrZ2LS_qzrGIJYoehJg/zh-cn_image_0000002583480075.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000224Z&HW-CC-Expire=86400&HW-CC-Sign=6CD1779574BEB2303EDE3A8935A2E27CFF66FB65F139F7CBDE00A74B2364C4C5)

### 示例4

设置安全控件系统焦点框样式。

```
1. import { ColorMetrics, LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Row() {
8. Column({ space: 30 }) {
9. Column({ space: 15 }) {
10. Text('不设置focusBox属性的默认安全控件')
11. SaveButton()
12. }

14. Column({ space: 15 }) {
15. Text('紧贴安全控件的黑色焦点框')
16. SaveButton()
17. .focusBox({
18. margin: new LengthMetrics(0),
19. strokeColor: ColorMetrics.rgba(0, 0, 0),
20. })
21. }

23. Column({ space: 15 }) {
24. Text('较大的红色焦点框')
25. SaveButton()
26. .focusBox({
27. margin: new LengthMetrics(10),
28. strokeColor: ColorMetrics.rgba(255, 0, 0),
29. strokeWidth: LengthMetrics.px(10)
30. })
31. }

33. Column({ space: 15 }) {
34. Text('矩形安全控件')
35. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD, buttonType: ButtonType.Normal })
36. .focusBox({
37. margin: new LengthMetrics(10),
38. strokeColor: ColorMetrics.rgba(255, 0, 0),
39. strokeWidth: LengthMetrics.px(10)
40. })
41. }

43. Column({ space: 15 }) {
44. Text('圆形安全控件')
45. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD, buttonType: ButtonType.Circle })
46. .focusBox({
47. margin: new LengthMetrics(10),
48. strokeColor: ColorMetrics.rgba(255, 0, 0),
49. strokeWidth: LengthMetrics.px(10)
50. })
51. }
52. }
53. .width('100%')
54. }
55. .height('100%')
56. }
57. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/hnio7eOCSY2WVlLevZeaLA/zh-cn_image_0000002552800426.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000224Z&HW-CC-Expire=86400&HW-CC-Sign=7D71E0799FCE64F977101C357AA9B5FA2C8201A8CB535B4CE88234607DA0E674)
