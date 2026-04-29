---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types
title: 基础类型定义
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 公共定义 > 基础类型定义
category: harmonyos-references
scraped_at: 2026-04-29T13:53:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ee3845c198534b948966d28d3964f0f09745aca478bcf2416f721612f306c6d4
---

说明

本模块首批接口从API version 7开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

## Resource

PhonePC/2in1TabletTVWearable

资源引用类型，用于设置组件属性的值。各类资源文件，需要放入特定子目录中存储管理，资源目录的示例请参考[资源分类](../harmonyos-guides/resource-categories-and-access.md#资源分类)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

可以通过$r或者$rawfile创建Resource类型对象，不可以修改Resource中的各属性的值。

* $r('belonging.type.name')

  belonging：系统资源或者应用资源，相应的取值为'sys'和'app'；

  type：资源类型，支持'boolean'、'color'、'float'、'intarray'、'integer'、'pattern'、'plural'、'strarray'、'string'、'media'；

  name：资源名称，在资源定义时确定。
* $rawfile('filename')

  filename：工程中resources/rawfile目录下的文件名称。

说明

引用资源类型时，需确保资源类型对象内的数据类型与当前以资源类型作为参数的属性方法本身的类型一致。例如某个属性方法支持设置string | Resource，那么在使用Resource引用类型时，其数据类型也应当为string。

引用资源类型时，需确保资源类型对象用法为当前支持的用法，否则当前以资源类型作为参数的属性效果将和不设置该属性相同。

## Length

PhonePC/2in1TabletTVWearable

长度类型，用于描述尺寸单位。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| string | 需要显式指定[像素单位](ts-pixel-units.md)，如'10px'，也可设置百分比字符串，如'100%'。  **说明：**  不指定像素单位时，默认单位vp，如'10'，等同于10。 |
| number | 默认单位vp。 |
| [Resource](ts-types.md#resource) | 资源引用类型，引入系统资源或者应用资源中的尺寸。 |

## ResourceStr

PhonePC/2in1TabletTVWearable

字符串类型，用于描述字符串入参可以使用的类型。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| string | 字符串类型。 |
| [Resource](ts-types.md#resource) | 资源引用类型，引入系统资源或者应用资源中的字符串。 |

## Padding

PhonePC/2in1TabletTVWearable

内边距类型，用于描述组件不同方向的内边距。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| top | [Length](ts-types.md#length) | 否 | 是 | 上内边距，组件内元素距组件顶部的尺寸。 |
| right | [Length](ts-types.md#length) | 否 | 是 | 右内边距，组件内元素距组件右边界的尺寸。 |
| bottom | [Length](ts-types.md#length) | 否 | 是 | 下内边距，组件内元素距组件底部的尺寸。 |
| left | [Length](ts-types.md#length) | 否 | 是 | 左内边距，组件内元素距组件左边界的尺寸。 |

## LocalizedPadding12+

PhonePC/2in1TabletTVWearable

内边距类型，用于描述组件不同方向的内边距。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| top | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)12+ | 否 | 是 | 上内边距，组件内元素距组件顶部的尺寸。 |
| end | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)12+ | 否 | 是 | 右内边距，组件内元素距组件右边界的尺寸。  从右至左显示语言模式下为  左内边距，组件内元素距组件左边界的尺寸。 |
| bottom | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)12+ | 否 | 是 | 下内边距，组件内元素距组件底部的尺寸。 |
| start | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)12+ | 否 | 是 | 左内边距，组件内元素距组件左边界的尺寸。  从右至左显示语言模式下为  右内边距，组件内元素距组件右边界的尺寸。 |

## Margin

PhonePC/2in1TabletTVWearable

外边距类型，用于描述组件不同方向的外边距。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| top | [Length](ts-types.md#length) | 否 | 是 | 上外边距，组件顶部距组件外元素的尺寸。 |
| right | [Length](ts-types.md#length) | 否 | 是 | 右外边距，组件右边界距组件外元素的尺寸。 |
| bottom | [Length](ts-types.md#length) | 否 | 是 | 下外边距，组件底部距组件外元素的尺寸。 |
| left | [Length](ts-types.md#length) | 否 | 是 | 左外边距，组件左边界距组件外元素的尺寸。 |

## LocalizedMargin12+

PhonePC/2in1TabletTVWearable

外边距类型，用于描述组件不同方向的外边距。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| top | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)12+ | 否 | 是 | 上外边距，组件顶部距组件外元素的尺寸。 |
| end | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)12+ | 否 | 是 | 右外边距，组件右边界距组件外元素的尺寸。  从右至左显示语言模式下为  左外边距，组件左边界距组件外元素的尺寸。 |
| bottom | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)12+ | 否 | 是 | 下外边距，组件底部距组件外元素的尺寸。 |
| start | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)12+ | 否 | 是 | 左外边距，组件左边界距组件外元素的尺寸。  从右至左显示语言模式下为  右外边距，组件右边界距组件外元素的尺寸。 |

## EdgeWidths9+

PhonePC/2in1TabletTVWearable

边框宽度类型，用于描述组件边框不同方向的宽度。

引入该对象时，至少传入一个参数。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| top | [Length](ts-types.md#length) | 否 | 是 | 组件上边框宽度。 |
| right | [Length](ts-types.md#length) | 否 | 是 | 组件右边框宽度。 |
| bottom | [Length](ts-types.md#length) | 否 | 是 | 组件下边框宽度。 |
| left | [Length](ts-types.md#length) | 否 | 是 | 组件左边框宽度。 |

## LocalizedEdgeWidths12+

PhonePC/2in1TabletTVWearable

边框宽度类型，用于描述组件边框不同方向的宽度。

引入该对象时，至少传入一个参数。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| top | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)12+ | 否 | 是 | 组件上边框宽度。 |
| end | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)12+ | 否 | 是 | 组件右边框宽度。  从右至左显示语言模式下为组件左边框宽度。 |
| bottom | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)12+ | 否 | 是 | 组件下边框宽度。 |
| start | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)12+ | 否 | 是 | 组件左边框宽度。  从右至左显示语言模式下为组件右边框宽度。 |

## BorderRadiuses9+

PhonePC/2in1TabletTVWearable

圆角类型，用于描述组件边框圆角半径。

引用该对象时，至少传入一个参数。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| topLeft | [Length](ts-types.md#length) | 否 | 是 | 组件左上角圆角半径。 |
| topRight | [Length](ts-types.md#length) | 否 | 是 | 组件右上角圆角半径。 |
| bottomLeft | [Length](ts-types.md#length) | 否 | 是 | 组件左下角圆角半径。 |
| bottomRight | [Length](ts-types.md#length) | 否 | 是 | 组件右下角圆角半径。 |

## LocalizedBorderRadiuses12+

PhonePC/2in1TabletTVWearable

圆角类型，用于描述组件边框圆角半径。

引用该对象时，至少传入一个参数。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| topStart | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)12+ | 否 | 是 | 组件左上角圆角半径。  从右至左显示语言模式下为组件右上角圆角半径。 |
| topEnd | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)12+ | 否 | 是 | 组件右上角圆角半径。  从右至左显示语言模式下为组件左上角圆角半径。 |
| bottomStart | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)12+ | 否 | 是 | 组件左下角圆角半径。  从右至左显示语言模式下为组件右下角圆角半径。 |
| bottomEnd | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)12+ | 否 | 是 | 组件右下角圆角半径。  从右至左显示语言模式下为组件左下角圆角半径。 |

## EdgeColors9+

PhonePC/2in1TabletTVWearable

边框颜色，用于描述组件边框四条边的颜色。

引入该对象时，至少传入一个参数。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| top | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 组件上边框颜色。 |
| right | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 组件右边框颜色。 |
| bottom | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 组件下边框颜色。 |
| left | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 组件左边框颜色。 |

## LocalizedEdgeColors12+

PhonePC/2in1TabletTVWearable

边框颜色，用于描述组件边框四条边的颜色。

引入该对象时，至少传入一个参数。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| top | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 组件上边框颜色。 |
| end | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 组件右边框颜色。  从右至左显示语言模式下为组件左边框颜色。 |
| bottom | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 组件下边框颜色。 |
| start | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 组件左边框颜色。  从右至左显示语言模式下为组件右边框颜色。 |

## EdgeStyles9+

PhonePC/2in1TabletTVWearable

边框样式，用于描述组件边框四条边的样式。

引入该对象时，至少传入一个参数。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| top | [BorderStyle](ts-appendix-enums.md#borderstyle) | 否 | 是 | 组件上边框样式。 |
| right | [BorderStyle](ts-appendix-enums.md#borderstyle) | 否 | 是 | 组件右边框样式。 |
| bottom | [BorderStyle](ts-appendix-enums.md#borderstyle) | 否 | 是 | 组件下边框样式。 |
| left | [BorderStyle](ts-appendix-enums.md#borderstyle) | 否 | 是 | 组件左边框样式。 |

## Offset

PhonePC/2in1TabletTVWearable

相对布局完成位置坐标偏移量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dx | [Length](ts-types.md#length) | 否 | 否 | 水平方向偏移量。 |
| dy | [Length](ts-types.md#length) | 否 | 否 | 竖直方向偏移量。 |

## RectResult10+

PhonePC/2in1TabletTVWearable

位置和尺寸类型，用于描述组件的位置和宽高。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 水平方向横坐标。 |
| y | number | 否 | 否 | 竖直方向纵坐标。 |
| width | number | 否 | 否 | 内容宽度大小。 |
| height | number | 否 | 否 | 内容高度大小。 |

## ResourceColor

PhonePC/2in1TabletTVWearable

type ResourceColor = [Color](ts-appendix-enums.md#color) | number | string | [Resource](ts-types.md#resource)

颜色类型，用于描述资源颜色类型。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Color](ts-appendix-enums.md#color) | 颜色枚举值。 |
| number | HEX格式颜色，支持rgb或者argb。示例：0xffffff，0xffff0000。number无法识别传入位数，格式选择依据值的大小，例如0x00ffffff作rgb格式解析。 |
| string | 支持rgb、rgba或者argb的格式颜色。  rgb格式颜色示例：'#ffffff'、'rgb(255, 100, 255)'。  rgba格式颜色示例：'rgba(255, 100, 255, 0.5)'。  argb格式颜色示例：'#ff000000'。 |
| [Resource](ts-types.md#resource) | 使用引入资源的方式，引入系统资源或者应用资源中的颜色。 |

## LengthConstrain

PhonePC/2in1TabletTVWearable

长度约束，用于对组件最大、最小长度做限制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| minLength | [Length](ts-types.md#length) | 否 | 否 | 组件最小长度。 |
| maxLength | [Length](ts-types.md#length) | 否 | 否 | 组件最大长度。 |

## Font

PhonePC/2in1TabletTVWearable

设置文本样式。

说明

可以使用[loadFontSync](js-apis-graphics-text.md#loadfontsync)注册自定义字体。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size | [Length](ts-types.md#length) | 否 | 是 | 设置文本尺寸，Length为number类型时，使用fp单位。不支持设置百分比字符串。  默认值：16.0 |
| weight | [FontWeight](ts-appendix-enums.md#fontweight) | number | string | 否 | 是 | 设置文本的字体粗细，number类型取值[100, 900]，取值间隔为100，取值越大，字体越粗。  默认值：400 | FontWeight.Normal |
| family | string | [Resource](ts-types.md#resource) | 否 | 是 | 字体列表。默认字体'HarmonyOS Sans'。  使用多个字体时，请用逗号','分隔，字体的优先级按顺序生效。例如：'Arial,HarmonyOS Sans'。 |
| style | [FontStyle](ts-appendix-enums.md#fontstyle) | 否 | 是 | 设置文本的字体样式。  默认值：FontStyle.Normal |

## Area8+

PhonePC/2in1TabletTVWearable

区域类型，用于存储元素所占的区域信息。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| width | [Length](ts-types.md#length) | 目标元素的宽度。  单位：vp |
| height | [Length](ts-types.md#length) | 目标元素的高度。  单位：vp |
| position | [Position](ts-types.md#position) | 目标元素左上角在以父元素为基准的[组件坐标系](../harmonyos-guides/arkui-glossary.md#组件坐标系)中的位置。 |
| globalPosition | [Position](ts-types.md#position) | 目标元素左上角在当前窗口坐标系中的位置。 |

## Position

PhonePC/2in1TabletTVWearable

位置类型，用于表示一个坐标点。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | [Length](ts-types.md#length) | 否 | 是 | x轴坐标。  单位：vp |
| y | [Length](ts-types.md#length) | 否 | 是 | y轴坐标。  单位：vp |

## LocalizedPosition12+

PhonePC/2in1TabletTVWearable

位置类型，用于表示一个坐标点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | LTR模式时x轴相对左边坐标，RTL模式x轴相对右边坐标。 |
| top | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | y轴坐标。 |

## Edges12+

PhonePC/2in1TabletTVWearable

位置类型，表示相对四边的偏移量。同时设置top和bottom，仅top生效；同时设置left和right，仅left生效。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| top | [Dimension](ts-types.md#dimension10) | 否 | 是 | 相对顶边的偏移量。 |
| bottom | [Dimension](ts-types.md#dimension10) | 否 | 是 | 相对底边的偏移量。 |
| left | [Dimension](ts-types.md#dimension10) | 否 | 是 | 相对左边的偏移量。 |
| right | [Dimension](ts-types.md#dimension10) | 否 | 是 | 相对右边的偏移量。 |

## LocalizedEdges12+

PhonePC/2in1TabletTVWearable

位置类型，表示相对四边的偏移量。同时设置top和bottom，仅top生效；同时设置start和end，仅start生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| top | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 相对顶边的偏移量。 |
| bottom | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 相对底边的偏移量。 |
| start | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | LTR模式时相对左边的偏移量，RTL模式时相对右边的偏移量。 |
| end | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | LTR模式时相对右边的偏移量，RTL模式时相对左边的偏移量。 |

## ConstraintSizeOptions

PhonePC/2in1TabletTVWearable

约束尺寸类型，用于描述组件布局时对尺寸大小的范围限制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| minWidth | [Length](ts-types.md#length) | 否 | 是 | 元素最小宽度。 |
| maxWidth | [Length](ts-types.md#length) | 否 | 是 | 元素最大宽度。 |
| minHeight | [Length](ts-types.md#length) | 否 | 是 | 元素最小高度。 |
| maxHeight | [Length](ts-types.md#length) | 否 | 是 | 元素最大高度。 |

说明

在[Row](ts-container-row.md)、[Column](ts-container-column.md)、[RelativeContainer](ts-container-relativecontainer.md)组件中，width、height设置auto表示自适应子组件。在[TextInput](ts-basic-components-textinput.md)组件中，width设置auto表示自适应文本宽度。

## SizeOptions

PhonePC/2in1TabletTVWearable

宽高尺寸类型，用于描述组件布局时的宽高尺寸大小。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | [Length](ts-types.md#length) | 否 | 是 | 元素宽度。 |
| height | [Length](ts-types.md#length) | 否 | 是 | 元素高度。 |

## BorderOptions

PhonePC/2in1TabletTVWearable

边框属性集合，用于描述边框相关信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | [EdgeWidths](ts-types.md#edgewidths9)9+ | [Length](ts-types.md#length) | [LocalizedEdgeWidths](ts-types.md#localizededgewidths12)12+ | 否 | 是 | 设置边框宽度。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| color | [EdgeColors](ts-types.md#edgecolors9)9+ | [ResourceColor](ts-types.md#resourcecolor) | [LocalizedEdgeColors](ts-types.md#localizededgecolors12)12+ | 否 | 是 | 设置边框颜色。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| radius | [BorderRadiuses](ts-types.md#borderradiuses9)9+ | [Length](ts-types.md#length) | [LocalizedBorderRadiuses](ts-types.md#localizedborderradiuses12)12+ | 否 | 是 | 设置边框圆角半径。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| style | [EdgeStyles](ts-types.md#edgestyles9)9+ | [BorderStyle](ts-appendix-enums.md#borderstyle) | 否 | 是 | 设置边框样式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| dashGap12+ | [EdgeWidths](ts-types.md#edgewidths9) | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | [LocalizedEdgeWidths](ts-types.md#localizededgewidths12) | 否 | 是 | 设置虚线的线段间距，仅在边框样式为虚线时生效。  不支持设置百分比。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **卡片能力：** 该接口不支持在ArkTS卡片中使用。 |
| dashWidth12+ | [EdgeWidths](ts-types.md#edgewidths9) | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | [LocalizedEdgeWidths](ts-types.md#localizededgewidths12) | 否 | 是 | 设置虚线的线段长度，仅在边框样式为虚线时生效。  不支持设置百分比。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **卡片能力：** 该接口不支持在ArkTS卡片中使用。 |

## ColorFilter9+

PhonePC/2in1TabletTVWearable

创建具有4\*5矩阵的颜色过滤器。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| constructor | number[] | 是 | 创建具有4\*5矩阵的颜色过滤器，入参为[m\*n]位于m行和n列中矩阵值，矩阵是行优先的。 |

## CustomBuilder8+

PhonePC/2in1TabletTVWearable

组件属性方法参数可使用CustomBuilder类型来自定义UI描述。

| 名称 | 类型定义 | 描述 |
| --- | --- | --- |
| CustomBuilder | (() => any) | void | 生成用户自定义组件，在使用时结合[@Builder](../harmonyos-guides/arkts-builder.md)使用。 |

## CustomBuilderT<T>23+

PhonePC/2in1TabletTVWearable

type CustomBuilderT<T> = (t: T) => void

自定义UI描述，相比于CustomBuilder，本接口支持传入一个参数。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| t | T | 是 | 生成用户自定义组件，在使用时结合[@Builder](../harmonyos-guides/arkts-builder.md)使用，并允许传入一个参数。 |

## MarkStyle10+对象说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 默认值 | 描述 |
| --- | --- | --- | --- | --- | --- |
| strokeColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | Color.White | 内部图标颜色。 |
| size | [Length](ts-types.md#length) | 否 | 是 | - | 内部图标大小，单位vp。默认大小与多选框组件宽度相同。  不支持百分比形式设置。设置为非法值时，按照默认值处理。 |
| strokeWidth | [Length](ts-types.md#length) | 否 | 是 | 2 | 内部图标粗细，单位vp。不支持设置百分比。设置为非法值时，按照默认值处理。 |

## ModalTransition10+

PhonePC/2in1TabletTVWearable

全屏模态转场方式枚举类型，用于设置全屏模态转场类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 描述 |
| --- | --- |
| NONE | 全屏模态无转场动画。 |
| DEFAULT | 全屏模态上下切换动画。 |
| ALPHA | 全屏模态透明度渐变动画。 |

## OutlineOptions11+对象说明

PhonePC/2in1TabletTVWearable

外描边选项设置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | [Dimension](ts-types.md#dimension10) | [EdgeOutlineWidths](ts-types.md#edgeoutlinewidths11对象说明) | 否 | 是 | 设置外描边宽度，不支持百分比。  默认值：0，外描边效果中width为必设项，否则不显示外描边。 |
| color | [ResourceColor](ts-types.md#resourcecolor) | [EdgeColors](ts-types.md#edgecolors9) | [LocalizedEdgeColors](ts-types.md#localizededgecolors12)12+ | 否 | 是 | 设置外描边颜色。  默认值：Color.Black |
| radius | [Dimension](ts-types.md#dimension10) | [OutlineRadiuses](ts-types.md#outlineradiuses11对象说明) | 否 | 是 | 设置外描边圆角半径，不支持百分比。  默认值：0  最大生效值：组件width/2 + outlineWidth或组件height/2 + outlineWidth。 |
| style | [OutlineStyle](ts-universal-attributes-outline.md#outlinestyle枚举说明) | [EdgeOutlineStyles](ts-types.md#edgeoutlinestyles11对象说明) | 否 | 是 | 设置外描边样式。  默认值：OutlineStyle.SOLID |

## EdgeOutlineWidths11+对象说明

PhonePC/2in1TabletTVWearable

引入该对象时，至少传入一个参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | [Dimension](ts-types.md#dimension10) | 否 | 是 | 左侧外描边宽度。 |
| right | [Dimension](ts-types.md#dimension10) | 否 | 是 | 右侧外描边宽度。 |
| top | [Dimension](ts-types.md#dimension10) | 否 | 是 | 上侧外描边宽度。 |
| bottom | [Dimension](ts-types.md#dimension10) | 否 | 是 | 下侧外描边宽度。 |

## OutlineRadiuses11+对象说明

PhonePC/2in1TabletTVWearable

引用该对象时，至少传入一个参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| topLeft | [Dimension](ts-types.md#dimension10) | 否 | 是 | 左上角圆角半径。 |
| topRight | [Dimension](ts-types.md#dimension10) | 否 | 是 | 右上角圆角半径。 |
| bottomLeft | [Dimension](ts-types.md#dimension10) | 否 | 是 | 左下角圆角半径。 |
| bottomRight | [Dimension](ts-types.md#dimension10) | 否 | 是 | 右下角圆角半径。 |

## EdgeOutlineStyles11+对象说明

PhonePC/2in1TabletTVWearable

引入该对象时，至少传入一个参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | [OutlineStyle](ts-universal-attributes-outline.md#outlinestyle枚举说明) | 否 | 是 | 左侧外描边样式。 |
| right | [OutlineStyle](ts-universal-attributes-outline.md#outlinestyle枚举说明) | 否 | 是 | 右侧外描边样式。 |
| top | [OutlineStyle](ts-universal-attributes-outline.md#outlinestyle枚举说明) | 否 | 是 | 上侧外描边样式。 |
| bottom | [OutlineStyle](ts-universal-attributes-outline.md#outlinestyle枚举说明) | 否 | 是 | 下侧外描边样式。 |

## Dimension10+

PhonePC/2in1TabletTVWearable

长度类型，用于描述尺寸单位。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [PX](ts-types.md#px10) | 需要指定以px像素单位，如'10px'。 |
| [VP](ts-types.md#vp10) | 需要指定数字或vp像素单位，如10或'10vp'。 |
| [FP](ts-types.md#fp10) | 需要指定以fp像素单位，如'10fp'。 |
| [LPX](ts-types.md#lpx10) | 需要指定以lpx像素单位，如'10lpx'。 |
| [Percentage](ts-types.md#percentage10) | 需要指定以%像素单位，如'10%'。 |
| [Resource](ts-types.md#resource) | 资源引用类型，引入系统资源或者应用资源中的尺寸。 |

## PX10+

PhonePC/2in1TabletTVWearable

长度类型，用于描述以px像素单位为单位的长度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| {number}px | 需要指定以px像素单位，如'10px'。 |

## VP10+

PhonePC/2in1TabletTVWearable

长度类型，用于描述以vp像素单位为单位的长度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| {number}vp|number | 需要指定数字或vp像素单位，如10或'10vp'。 |

## FP10+

PhonePC/2in1TabletTVWearable

长度类型，用于描述以fp像素单位为单位的长度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| {number}fp | 需要指定以fp像素单位，如'10fp'。 |

## LPX10+

PhonePC/2in1TabletTVWearable

长度类型，用于描述以lpx像素单位为单位的长度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| {number}lpx | 需要指定以lpx像素单位，如'10lpx'。 |

## Percentage10+

PhonePC/2in1TabletTVWearable

长度类型，用于描述以%像素单位为单位的长度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| {number}% | 需要指定以%像素单位，如'10%'。 |

## Degree10+

PhonePC/2in1TabletTVWearable

角度类型，用于描述以deg像素单位为单位的长度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| {number}deg | 需要指定以deg像素单位，如'10deg'。 |

## TouchPoint11+

PhonePC/2in1TabletTVWearable

配置跟手点坐标，不配置时，默认居中。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型定义 | 描述 |
| --- | --- | --- |
| X | [Dimension](ts-types.md#dimension10) | 跟手点X轴坐标。 |
| Y | [Dimension](ts-types.md#dimension10) | 跟手点Y轴坐标。 |

## VoidCallback12+

PhonePC/2in1TabletTVWearable

type VoidCallback：() => void;

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## Callback12+

PhonePC/2in1TabletTVWearable

Callback<T,V = void> = (data: T) => V;

带参数的函数回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## DividerStyleOptions12+

PhonePC/2in1TabletTVWearable

分割线样式属性集合, 用于描述分割线相关信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| strokeWidth | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)12+ | 否 | 是 | 分割线的线宽。 |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 分割线的颜色。 |
| startMargin | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)12+ | 否 | 是 | 分割线与菜单侧边起始端的距离。 |
| endMargin | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)12+ | 否 | 是 | 分割线与菜单侧边结束端的距离。 |
| mode | [DividerMode](ts-appendix-enums.md#dividermode19枚举说明)19+ | 否 | 是 | 设置分割线模式。 |

## ChainWeightOptions14+对象说明

PhonePC/2in1TabletTVWearable

链中组件的布局权重。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| horizontal | number | 否 | 是 | 组件在水平方向的布局权重，设置大于0的数字时生效。  默认值：0  异常值：0 |
| vertical | number | 否 | 是 | 组件在竖直方向的布局权重，设置大于0的数字时生效。  默认值：0  异常值：0 |

## Configuration

PhonePC/2in1TabletTVWearable

数据类型。用于设置颜色模式和字体缩放倍数。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colorMode | string | 是 | 否 | 颜色模式。 |
| fontScale | number | 是 | 否 | 字体缩放。 |

## AccessibilityOptions14+对象说明

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| accessibilityPreferred | boolean | 否 | 是 | 若accessibilityPreferred设置为true，则深度遍历每个子节点时优先选择该子节点的无障碍文本accessibilityText。  若无障碍文本为空则选择本身Text文本，最终将拼接完成的文本设置给accessibilityText与Text都为空的父节点。  若accessibilityPreferred设置为false，表示不启用此功能。  默认值：false  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| stateControllerRoleType23+ | [AccessibilityRoleType](ts-universal-attributes-accessibility.md#accessibilityroletype18枚举说明) | 否 | 是 | 指定特定类型的子组件。配置[accessibilityGroup](ts-universal-attributes-accessibility.md#accessibilitygroup14)的容器组件进行无障碍聚合后，会将该特定类型的子组件的选中状态和状态播报文本作为聚合组件的状态和播报文本。从而聚合屏幕朗读下的状态播报，避免需要对子组件单独进行聚焦。  **说明：**  如果聚合组件内有多个相同类型的子组件，则以组件树上该聚合组件下的第一个查找到的子组件为控制组件。  不支持跨进程嵌入式组件内的特定类型，例如：卡片、EmbeddedUIExtension。  默认值：无指定组件  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| stateControllerId23+ | string | 否 | 是 | 指定特定[唯一标识ID](ts-universal-attributes-component-id.md#id)的子组件。配置[accessibilityGroup](ts-universal-attributes-accessibility.md#accessibilitygroup14)的容器组件进行无障碍聚合后，会将该特定标识的子组件的选中状态和状态播报文本作为聚合组件的状态和播报文本。从而聚合屏幕朗读下的状态播报，避免需要对子组件单独进行聚焦。  **说明：**  如果聚合组件内有多个相同类型的子组件，则以组件树上该聚合组件下的第一个查找到的子组件为控制组件。  如果与stateControllerRoleType同时配置，则优先匹配ID一致的组件。  不支持跨进程嵌入式组件内的特定类型，例如：卡片、EmbeddedUIExtension。  默认值：无指定组件  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| actionControllerRoleType23+ | [AccessibilityRoleType](ts-universal-attributes-accessibility.md#accessibilityroletype18枚举说明) | 否 | 是 | 指定特定类型的子组件。配置[accessibilityGroup](ts-universal-attributes-accessibility.md#accessibilitygroup14)的容器组件进行无障碍聚合后，如果触发无障碍的控制操作时，会将操作转发给该特定类型的子组件。从而聚合屏幕朗读下的点击事件，避免需要对子组件单独进行聚焦。  **说明：**  如果聚合组件内有多个相同类型的子组件，则以组件树上该聚合组件下的第一个查找到的子组件为控制组件。  当前只支持无障碍点击操作。  不支持跨进程嵌入式组件内的特定类型，例如：卡片、EmbeddedUIExtension。  默认值：无指定组件  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| actionControllerId23+ | string | 否 | 是 | 指定特定[唯一标识ID](ts-universal-attributes-component-id.md#id)的子组件。配置[accessibilityGroup](ts-universal-attributes-accessibility.md#accessibilitygroup14)的容器组件进行无障碍聚合后，如果触发无障碍的控制操作时，会将操作转发给该特定标识的子组件。从而聚合屏幕朗读下的点击事件，避免需要对子组件单独进行聚焦。  **说明：**  如果聚合组件内有多个相同类型的子组件，则以组件树上该聚合组件下的第一个查找到的子组件为控制组件。  当前只支持无障碍点击操作。  如果与actionControllerRoleType同时配置，则优先匹配ID一致的组件。  不支持跨进程嵌入式组件内的特定类型，例如：卡片、EmbeddedUIExtension。  默认值：无指定组件  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## ScrollBarMargin20+对象说明

PhonePC/2in1TabletTVWearable

滚动条边距。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 滚动条起始边距。  默认值：0，单位：vp |
| end | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 滚动条末尾边距。  默认值：0，单位：vp |

## ResponsiveFillType22+

PhonePC/2in1TabletTVWearable

type ResponsiveFillType = PresetFillType

响应式布局填充模式，用于WaterFlow、Grid、List和Swiper组件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [PresetFillType](ts-appendix-enums.md#presetfilltype22) | 为不同响应式断点规格指定列数。 |

## ItemFillPolicy22+

PhonePC/2in1TabletTVWearable

定义一个适用于WaterFlow、Grid、List和Swiper组件的响应式布局策略。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fillType | [ResponsiveFillType](ts-types.md#responsivefilltype22) | 否 | 是 | 为不同的响应式断点指定列数。默认值为BREAKPOINT\_DEFAULT。 |

## DirectionalEdgesT<T>12+

PhonePC/2in1TabletTVWearable

边缘宽度类型，用于描述组件边缘不同方向的宽度。支持全球化。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | T | 否 | 否 | 起始边缘的属性。在LTR的方向下，为左边缘，在RTL的方向下，为右边缘。 |
| end | T | 否 | 否 | 终止边缘的属性。在LTR的方向下，为右边缘，在RTL的方向下，为左边缘。 |
| top | T | 否 | 否 | 顶部边缘的属性。 |
| bottom | T | 否 | 否 | 底部边缘的属性。 |

## Bias对象说明

PhonePC/2in1TabletTVWearable

设置组件在锚点约束下的偏移参数。

以水平方向Bias为例，其值为组件到左锚点的距离 Dstart与组件到水平方向锚点间总距离 Dstart + Dend的比值。镜像语言下，Dstart为组件到右锚点的距离。下图中Dwidth表示组件宽度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/eKvt3FWuT9SVAaehuGLAsg/zh-cn_image_0000002558607008.png?HW-CC-KV=V1&HW-CC-Date=20260429T055309Z&HW-CC-Expire=86400&HW-CC-Sign=4F9B3FC61671AF7072866020D6220242F18638A0A831078274FB82D1453CEB3A)

竖直方向同理，其值为组件到上锚点的距离Dtop与组件到竖直方向锚点间总距离Dtop + Dbottom的比值。下图中Dheight表示组件高度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/kPByJW77TQGhzxSSd0e3Kw/zh-cn_image_0000002589326535.png?HW-CC-KV=V1&HW-CC-Date=20260429T055309Z&HW-CC-Expire=86400&HW-CC-Sign=BA1E3E9AA87DD296589132FF198B4D0CBC5F5B9F1D572F57D21C4A129266F774)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| horizontal | number | 否 | 是 | 水平方向上的bias值。  当子组件的width属性有正确值并且有2个水平方向的锚点时生效，设置的值必须大于等于0。  默认值： 0.5 |
| vertical | number | 否 | 是 | 垂直方向上的bias值。  当子组件的height属性有正确值并且有2个垂直方向的锚点时生效，设置的值必须大于等于0。  默认值： 0.5 |

## CacheCountInfo22+对象说明

PhonePC/2in1TabletTVWearable

缓存数量信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| minCount | number | 否 | 否 | 最小缓存数，当实际缓存数小于最小缓存数时，在滚动动画帧间空闲时隙加载缓存。  取值范围：[0, +∞)，小于0时按1处理。 |
| maxCount | number | 否 | 否 | 最大缓存数，当实际缓存数大于最大缓存数时，缓存内容会回收或释放，当UI空闲时（无动画或用户操作），会加载缓存到最大缓存数。  取值范围：[minCount, +∞)，小于minCount时按minCount处理。 |

## AccessibilityActionOptions23+对象说明

PhonePC/2in1TabletTVWearable

设置组件的无障碍操作的可选参数，用于限制或修改屏幕朗读等辅助应用发起的操作行为。仅[Slider](ts-basic-components-slider.md)组件支持使用。在其他组件使用该接口时，编译环节可正常通过，但接口功能不生效。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scrollStep | number | 否 | 是 | 无障碍手势触发的无障碍滚动操作中的组件操作步数。默认值基于组件默认值。  不支持的组件配置不生效。  当前支持组件：[slider](ts-basic-components-slider.md)，用于slider组件聚焦后通过手势上下扫动触发slider组件的滑动操作。滑动距离：scrollStep\*[step](ts-basic-components-slider.md#slideroptions对象说明)。取值范围：[1, ([max](ts-basic-components-slider.md#slideroptions对象说明) - [min](ts-basic-components-slider.md#slideroptions对象说明))/[step](ts-basic-components-slider.md#slideroptions对象说明)]，默认值为1。超出取值范围时取默认值1；在取值范围内，scrollStep为非整数时向下取整。 |
