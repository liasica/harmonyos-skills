---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-text
title: ArkUI_NodeAttributeType（文本显示类组件相关属性）
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_node.h > ArkUI_NodeAttributeType（文本显示类组件相关属性）
category: harmonyos-references
scraped_at: 2026-04-29T13:54:15+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:0b6b339c6c680e014200820f2f4328e830e914c27b8b520e801631dd128e9971
---

```
1. enum ArkUI_NodeAttributeType
```

## 概述

定义ArkUI在Native侧可以设置的文本显示类组件相关属性样式集合，包含Text、Span、ImageSpan等组件属性设置。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)

## NODE\_TEXT\_CONTENT

```
1. NODE_TEXT_CONTENT = MAX_NODE_SCOPE_NUM * ARKUI_NODE_TEXT = 1000
```

Text组件设置文本内容属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 表示文本内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 表示文本内容。 |

## NODE\_FONT\_COLOR

```
1. NODE_FONT_COLOR = 1001
```

组件字体颜色属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 字体颜色数值，0xargb格式，形如 0xFFFF0000 表示红色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 字体颜色数值，0xargb格式。 |

## NODE\_FONT\_SIZE

```
1. NODE_FONT_SIZE = 1002
```

组件字体大小属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 字体大小数值，单位为fp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 字体大小数值，单位为fp。 |

## NODE\_FONT\_STYLE

```
1. NODE_FONT_STYLE = 1003
```

组件字体样式属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 字体样式[ArkUI\_FontStyle](capi-native-type-h.md#arkui_fontstyle)，默认值为ARKUI\_FONT\_STYLE\_NORMAL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 字体样式[ArkUI\_FontStyle](capi-native-type-h.md#arkui_fontstyle)。 |

## NODE\_FONT\_WEIGHT

```
1. NODE_FONT_WEIGHT = 1004
```

组件字体粗细属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 字体粗细样式[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)，默认值为ARKUI\_FONT\_WEIGHT\_NORMAL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 字体粗细样式[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)。 |

## NODE\_TEXT\_LINE\_HEIGHT

```
1. NODE_TEXT_LINE_HEIGHT = 1005
```

文本行高属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 表示lineHeight值，单位为fp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 表示lineHeight值，单位为fp。 |

## NODE\_TEXT\_DECORATION

```
1. NODE_TEXT_DECORATION = 1006
```

文本装饰线样式及其颜色属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 文本装饰线类型[ArkUI\_TextDecorationType](capi-native-type-h.md#arkui_textdecorationtype)，默认值为ARKUI\_TEXT\_DECORATION\_TYPE\_NONE。 |
| .value[1]?.u32 | 可选值，装饰线颜色，0xargb格式，形如 0xFFFF0000 表示红色。 |
| .value[2]?.i32 | 文本装饰线样式[ArkUI\_TextDecorationStyle](capi-native-type-h.md#arkui_textdecorationstyle)。 |
| .value[3]?.f32 | 可选值，文本装饰线粗细比例，默认值：1.0，取值范围：[0, +∞)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 文本装饰线类型[ArkUI\_TextDecorationType](capi-native-type-h.md#arkui_textdecorationtype)。 |
| .value[1].u32 | 装饰线颜色，0xargb格式。 |
| .value[2].i32 | 文本装饰线样式[ArkUI\_TextDecorationStyle](capi-native-type-h.md#arkui_textdecorationstyle)。 |
| .value[3].f32 | 文本装饰线粗细比例。 |

## NODE\_TEXT\_CASE

```
1. NODE_TEXT_CASE = 1007
```

文本大小写属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示文本大小写类型[ArkUI\_TextCase](capi-native-type-h.md#arkui_textcase)，默认值为ARKUI\_TEXT\_CASE\_NORMAL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示文本大小写类型[ArkUI\_TextCase](capi-native-type-h.md#arkui_textcase)。 |

## NODE\_TEXT\_LETTER\_SPACING

```
1. NODE_TEXT_LETTER_SPACING = 1008
```

文本字符间距属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 表示字符间距值，单位为fp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 表示字符间距值，单位为fp。 |

## NODE\_TEXT\_MAX\_LINES

```
1. NODE_TEXT_MAX_LINES = 1009
```

文本最大行数属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示最大行数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示最大行数。 |

## NODE\_TEXT\_ALIGN

```
1. NODE_TEXT_ALIGN = 1010
```

文本水平对齐方式, 支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示文本水平对齐方式，取[ArkUI\_TextAlignment](capi-native-type-h.md#arkui_textalignment)枚举值。默认值为ARKUI\_TEXT\_ALIGNMENT\_START。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示文本水平对齐方式，取[ArkUI\_TextAlignment](capi-native-type-h.md#arkui_textalignment)枚举值。 |

## NODE\_TEXT\_OVERFLOW

```
1. NODE_TEXT_OVERFLOW = 1011
```

文本超长时的显示方式属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示文本超长时的显示方式[ArkUI\_TextOverflow](capi-native-type-h.md#arkui_textoverflow)。默认值为ARKUI\_TEXT\_OVERFLOW\_NONE。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示文本超长时的显示方式。[ArkUI\_TextOverflow](capi-native-type-h.md#arkui_textoverflow)。 |

## NODE\_FONT\_FAMILY

```
1. NODE_FONT_FAMILY = 1012
```

Text字体列表属性，支持属性设置，属性重置和属性获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 字体字符串，多个用,分隔。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 字体字符串，多个用,分隔。 |

## NODE\_TEXT\_COPY\_OPTION

```
1. NODE_TEXT_COPY_OPTION = 1013
```

文本复制粘贴属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 复制粘贴方式[ArkUI\_CopyOptions](capi-native-type-h.md#arkui_copyoptions)，默认值为ARKUI\_COPY\_OPTIONS\_NONE。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 复制粘贴方式[ArkUI\_CopyOptions](capi-native-type-h.md#arkui_copyoptions)。 |

## NODE\_TEXT\_BASELINE\_OFFSET

```
1. NODE_TEXT_BASELINE_OFFSET = 1014
```

文本基线的偏移量属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 偏移量数值，单位为fp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 偏移量数值，单位为fp。 |

## NODE\_TEXT\_TEXT\_SHADOW

```
1. NODE_TEXT_TEXT_SHADOW = 1015
```

文字阴影效果属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 阴影模糊半径，单位为vp。 |
| .value[1].i32 | 阴影类型[ArkUI\_ShadowType](capi-native-type-h.md#arkui_shadowtype)，默认值为ARKUI\_SHADOW\_TYPE\_COLOR。 |
| .value[2].u32 | 阴影颜色，0xargb格式，形如 0xFFFF0000 表示红色。 |
| .value[3].f32 | 阴影X轴偏移量，单位为vp。 |
| .value[4].f32 | 阴影Y轴偏移量，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 阴影模糊半径，单位为vp。 |
| .value[1].i32 | 阴影类型[ArkUI\_ShadowType](capi-native-type-h.md#arkui_shadowtype)。 |
| .value[2].u32 | 阴影颜色，0xargb格式。 |
| .value[3].f32 | 阴影X轴偏移量，单位为vp。 |
| .value[4].f32 | 阴影Y轴偏移量，单位为vp。 |

## NODE\_TEXT\_MIN\_FONT\_SIZE

```
1. NODE_TEXT_MIN_FONT_SIZE = 1016
```

Text最小显示字号，支持属性设置，属性重置和属性获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 文本最小显示字号，单位为fp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 文本最小显示字号，单位为fp。 |

## NODE\_TEXT\_MAX\_FONT\_SIZE

```
1. NODE_TEXT_MAX_FONT_SIZE = 1017
```

Text最大显示字号，支持属性设置，属性重置和属性获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 文本最大显示字号，单位为fp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 文本最大显示字号，单位为fp。 |

## NODE\_TEXT\_FONT

```
1. NODE_TEXT_FONT = 1018
```

Text样式，支持属性设置，属性重置和属性获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string? | 可选值 字体列表，使用多个字体，使用','进行分割。 |
| .value[0].f32 | 文本尺寸，单位为fp。 |
| .value[1]?.i32 | 可选值，文本的字体粗细，参数类型[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)。默认值为ARKUI\_FONT\_WEIGHT\_NORMAL。 |
| .value[2]?.i32 | 可选值，字体样式，参数类型[ArkUI\_FontStyle](capi-native-type-h.md#arkui_fontstyle)。默认值为ARKUI\_FONT\_STYLE\_NORMAL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 字体列表，使用多个字体，使用','进行分割。 |
| .value[0].f32 | 文本尺寸，单位为fp。 |
| .value[1].i32 | 文本的字体粗细，参数类型[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)。默认值为ARKUI\_FONT\_WEIGHT\_NORMAL。 |
| .value[2].i32 | 字体样式，参数类型[ArkUI\_FontStyle](capi-native-type-h.md#arkui_fontstyle)。默认值为ARKUI\_FONT\_STYLE\_NORMAL。 |

## NODE\_TEXT\_HEIGHT\_ADAPTIVE\_POLICY

```
1. NODE_TEXT_HEIGHT_ADAPTIVE_POLICY = 1019
```

Text自适应高度的方式，支持属性设置，属性重置和属性获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_TextHeightAdaptivePolicy](capi-native-type-h.md#arkui_textheightadaptivepolicy)。默认值为ARKUI\_TEXT\_HEIGHT\_ADAPTIVE\_POLICY\_MAX\_LINES\_FIRST。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_TextHeightAdaptivePolicy](capi-native-type-h.md#arkui_textheightadaptivepolicy)。 |

## NODE\_TEXT\_INDENT

```
1. NODE_TEXT_INDENT = 1020
```

文本首行缩进属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 表示首行缩进值，单位为fp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 表示首行缩进值，单位为vp。 |

## NODE\_TEXT\_WORD\_BREAK

```
1. NODE_TEXT_WORD_BREAK = 1021
```

文本断行规则属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_WordBreak](capi-native-type-h.md#arkui_wordbreak)。默认值为ARKUI\_WORD\_BREAK\_BREAK\_WORD。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_WordBreak](capi-native-type-h.md#arkui_wordbreak)。 |

## NODE\_TEXT\_ELLIPSIS\_MODE

```
1. NODE_TEXT_ELLIPSIS_MODE = 1022
```

设置文本省略位置，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_EllipsisMode](capi-native-type-h.md#arkui_ellipsismode)。默认值为ARKUI\_ELLIPSIS\_MODE\_END。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_EllipsisMode](capi-native-type-h.md#arkui_ellipsismode)。 |

## NODE\_TEXT\_LINE\_SPACING

```
1. NODE_TEXT_LINE_SPACING = 1023
```

文本行间距属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 表示lineSpacing值，单位为fp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 表示lineSpacing值，单位为fp。 |

## NODE\_FONT\_FEATURE

```
1. NODE_FONT_FEATURE = 1024
```

设置文本特性效果，设置NODE\_FONT\_FEATURE属性，NODE\_FONT\_FEATURE是 OpenType 字体的高级排版能力，如支持连字、数字等宽等特性，一般用在自定义字体中，其能力需要字体本身支持，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 符合文本特性格式的字符串，格式为normal | <feature-tag-value>。  <feature-tag-value>的格式为：<string> [ <integer> | on | off ]。  <feature-tag-value>的个数可以有多个，中间用','隔开，例如，使用等宽数字的输入格式为：ss01 on。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 表示文本特性的内容，多个文本特性之间使用逗号分隔。 |

## NODE\_TEXT\_ENABLE\_DATA\_DETECTOR

```
1. NODE_TEXT_ENABLE_DATA_DETECTOR = 1025
```

设置使能文本识别。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 使能文本识别，默认值false，true表示文本可实体识别，false表示不可识别。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 使能文本识别。 |

## NODE\_TEXT\_ENABLE\_DATA\_DETECTOR\_CONFIG

```
1. NODE_TEXT_ENABLE_DATA_DETECTOR_CONFIG = 1026
```

设置文本识别配置。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0...].i32 | 实体类型数组，参数类型[ArkUI\_TextDataDetectorType](capi-native-type-h.md#arkui_textdatadetectortype)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0...].i32 | 实体类型数组，参数类型[ArkUI\_TextDataDetectorType](capi-native-type-h.md#arkui_textdatadetectortype)。 |

## NODE\_TEXT\_SELECTED\_BACKGROUND\_COLOR

```
1. NODE_TEXT_SELECTED_BACKGROUND_COLOR = 1027
```

文本选中时的背景色属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xargb格式，形如 0xFFFF0000 表示红色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xargb格式。 |

## NODE\_TEXT\_CONTENT\_WITH\_STYLED\_STRING

```
1. NODE_TEXT_CONTENT_WITH_STYLED_STRING = 1028
```

Text组件使用格式化字符串对象设置文本内容属性，支持属性设置，属性重置，属性获取接口。配置自定义[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)对象到Text组件，会跳过文本控件的布局测算阶段，需要注意：

1、需要保证OH\_ArkUI\_StyledString对象、OH\_Drawing\_Typography对象的生命周期跟随Text组件生命周期，Text组件析构时重置OH\_ArkUI\_StyledString对象，否则会导致应用出现空指针崩溃。

2、保证OH\_Drawing\_TypographyLayout方法调用时序在Text组件的布局测算之前。

3、释放OH\_ArkUI\_StyledString对象、OH\_Drawing\_Typography对象时，需要同步调用Text组件的reset方法，否则会导致应用出现空指针崩溃。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 表示 ArkUI\_StyledString 格式化字符串数据，参数类型为[ArkUI\_StyledString](capi-arkui-nativemodule-arkui-styledstring.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 表示 ArkUI\_StyledString 格式化字符串数据，参数类型为[ArkUI\_StyledString](capi-arkui-nativemodule-arkui-styledstring.md)。 |

## NODE\_TEXT\_HALF\_LEADING

```
1. NODE_TEXT_HALF_LEADING = 1029
```

Text组件设置文本纵向居中显示。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 文本是否纵向居中显示，默认值false。  true表示文本是纵向居中显示，false表示文本不是纵向居中显示。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 文本是否纵向居中显示。 |

## NODE\_IMMUTABLE\_FONT\_WEIGHT

```
1. NODE_IMMUTABLE_FONT_WEIGHT = 1030
```

组件字体粗细属性，支持属性设置，属性重置和属性获取接口。通过此接口设置的粗细属性不会跟随系统字体粗细变化。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 字体粗细样式[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)，默认值为ARKUI\_FONT\_WEIGHT\_NORMAL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 字体粗细样式[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)。 |

## NODE\_TEXT\_LINE\_COUNT

```
1. NODE_TEXT_LINE_COUNT = 1031
```

文本行数属性，支持属性获取接口。

作为属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示文本行数。 |

## NODE\_TEXT\_OPTIMIZE\_TRAILING\_SPACE

```
1. NODE_TEXT_OPTIMIZE_TRAILING_SPACE = 1032
```

设置文本排版时是否优化每行结尾的空格，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置文本排版时是否优化每行结尾的空格，默认值为false。  true表示设置文本排版时优化每行结尾的空格，false表示不优化。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 文本排版时是否优化每行结尾的空格。 |

## NODE\_TEXT\_LINEAR\_GRADIENT

```
1. NODE_TEXT_LINEAR_GRADIENT = 1033
```

设置文本线性渐变效果，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 线性渐变的起始角度。当direction属性设置为ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM时，angle属性生效；否则，以direction属性为主要布局方式。0点方向顺时针旋转为正向角度，默认值：180。 |
| .value[1].i32 | 线性渐变的方向[ArkUI\_LinearGradientDirection](capi-native-type-h.md#arkui_lineargradientdirection)。设置除ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM之外的线性渐变方向后，angle不生效。默认值：ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_LEFT\_BOTTOM。 |
| .value[2].i32 | 为渐变的颜色重复着色，false表示不重复着色，true表示重复着色。默认值：false。 |
| .object | 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过。 |
| colors | 渐变色颜色数组，数组元素为0xargb格式，形如0xFFFF0000表示红色。 |
| stops | stops表示指定颜色所处位置的数组，数组元素取值范围为[0,1.0]，0表示需要设置渐变色的容器的开始处，1.0表示容器的结尾处。想要实现多个颜色渐变效果时，数组元素建议递增设置，如后一个数组元素比前一个数组元素小的话，按照等于前一个数组元素的值处理。 |
| size | 颜色个数，若小于colors数组长度则仅生效前size个颜色，不建议设置大于colors数组长度或小于等于0的值以及异常值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 线性渐变的起始角度。当为ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM时，angle为设置值，其他情况均为默认值0。 |
| .value[1].i32 | 线性渐变的方向[ArkUI\_LinearGradientDirection](capi-native-type-h.md#arkui_lineargradientdirection)。 |
| .value[2].i32 | 为渐变的颜色重复着色，0表示不重复着色，1表示重复着色。默认值：0。 |
| .object | 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过： |
| colors | 渐变色颜色数组，数组元素为0xargb格式，形如0xFFFF0000表示红色。 |
| stops | stops表示指定颜色所处位置的数组，数组元素取值范围为[0,1.0]，0表示需要设置渐变色的容器的开始处，1.0表示容器的结尾处。 |
| size | 生效后渐变色的颜色个数。 |

## NODE\_TEXT\_RADIAL\_GRADIENT

```
1. NODE_TEXT_RADIAL_GRADIENT = 1034
```

设置文本径向渐变渐变效果，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0]?.f32 | 为径向渐变的中心点，即相对于当前文本框左上角的X轴坐标。 |
| .value[1]?.f32 | 为径向渐变的中心点，即相对于当前文本框左上角的Y轴坐标。文本框左上角的坐标为[0,0]。 |
| .value[2]?.f32 | 径向渐变的半径，默认值0。 |
| .value[3]?.i32 | 为渐变的颜色重复着色，false表示不重复着色，true表示重复着色。默认值：false。 |
| .object | 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过： |
| colors | 渐变色颜色数组，数组元素为0xargb格式，形如0xFFFF0000表示红色。 |
| stops | stops表示指定颜色所处位置的数组，数组元素取值范围为[0,1.0]，0表示需要设置渐变色的容器的开始处，1.0表示容器的结尾处。想要实现多个颜色渐变效果时，数组元素建议递增设置，如后一个数组元素比前一个数组元素小的话，按照等于前一个数组元素的值处理。 |
| size | 颜色个数，若小于colors数组长度则仅生效前size个颜色，不建议设置大于colors数组长度或小于等于0的值以及异常值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0]?.f32 | 为径向渐变的中心点，即相对于当前文本框左上角的X轴坐标。 |
| .value[1]?.f32 | 为径向渐变的中心点，即相对于当前文本框左上角的Y轴坐标。文本框左上角的坐标为[0,0]。 |
| .value[2]?.f32 | 径向渐变的半径，默认值0。 |
| .value[3]?.i32 | 为渐变的颜色重复着色，0表示不重复着色，1表示重复着色。默认值：0。 |
| .object | 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过： |
| colors | 渐变色颜色数组，数组元素为0xargb格式，形如0xFFFF0000表示红色。 |
| stops | stops表示指定颜色所处位置的数组，数组元素取值范围为[0,1.0]，0表示需要设置渐变色的容器的开始处，1.0表示容器的结尾处。 |
| size | 生效后渐变色的颜色个数。 |

## NODE\_TEXT\_VERTICAL\_ALIGN

```
1. NODE_TEXT_VERTICAL_ALIGN = 1035
```

设置文本内容垂直对齐方式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 文本内容垂直对齐方式[ArkUI\_TextVerticalAlignment](capi-native-type-h.md#arkui_textverticalalignment)，默认值：ARKUI\_TEXT\_VERTICAL\_ALIGNMENT\_BASELINE。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 文本内容垂直对齐方式[ArkUI\_TextVerticalAlignment](capi-native-type-h.md#arkui_textverticalalignment)。 |

## NODE\_TEXT\_CONTENT\_ALIGN

```
1. NODE_TEXT_CONTENT_ALIGN = 1036
```

设置文本内容区垂直对齐方式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 文本内容区垂直对齐方式[ArkUI\_TextContentAlign](capi-native-type-h.md#arkui_textcontentalign)，默认值：ARKUI\_TEXT\_CONTENT\_ALIGN\_CENTER。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 文本内容区垂直对齐方式[ArkUI\_TextContentAlign](capi-native-type-h.md#arkui_textcontentalign)。 |

## NODE\_TEXT\_MIN\_LINES

```
1. NODE_TEXT_MIN_LINES = 1037
```

文本最小行数属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示文本最小行数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示文本最小行数。 |

## NODE\_TEXT\_ENABLE\_SELECTED\_DATA\_DETECTOR

```
1. NODE_TEXT_ENABLE_SELECTED_DATA_DETECTOR = 1038
```

开启选中词文本识别。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 开启选中词文本识别，true表示开启识别，false表示关闭识别。默认值：true。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否开启选中词文本识别。 |

## NODE\_TEXT\_MIN\_LINE\_HEIGHT

```
1. NODE_TEXT_MIN_LINE_HEIGHT = 1040
```

设置文本最小行高，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 文本最小行高，默认值：0。单位为fp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 文本最小行高。单位为fp。 |

## NODE\_TEXT\_MAX\_LINE\_HEIGHT

```
1. NODE_TEXT_MAX_LINE_HEIGHT = 1041
```

设置文本最大行高，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 文本最大行高，默认值：0，表示最大行高不受限制。单位为fp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 文本最大行高。单位为fp。 |

## NODE\_TEXT\_LINE\_HEIGHT\_MULTIPLE

```
1. NODE_TEXT_LINE_HEIGHT_MULTIPLE = 1042
```

设置倍数行高模式的倍数值，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 倍数行高模式的倍数值，默认值：0，表示使用默认行高高度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 倍数行高模式的倍数值。 |

## NODE\_TEXT\_LAYOUT\_MANAGER

```
1. NODE_TEXT_LAYOUT_MANAGER = 1043
```

文本布局管理器，支持属性获取接口。

作为属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 文本布局管理器对象，参数类型为[ArkUI\_LayoutManager](capi-arkui-nativemodule-arkui-textlayoutmanager.md)。 |

## NODE\_TEXT\_EDIT\_MENU\_OPTIONS

```
1. NODE_TEXT_EDIT_MENU_OPTIONS = 1044
```

文本菜单扩展项，支持属性设置接口。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 文本菜单扩展项配置数据，参数类型为[ArkUI\_TextEditMenuOptions](capi-arkui-nativemodule-arkui-texteditmenuoptions.md)。 |

## NODE\_TEXT\_BIND\_SELECTION\_MENU

```
1. NODE_TEXT_BIND_SELECTION_MENU = 1045
```

自定义文本选择菜单，支持属性设置接口。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 自定义文本选择菜单配置数据，参数类型为[ArkUI\_TextSelectionMenuOptions](-arkui-nativemodule-arkui-textselectionmenuoptions.md)。 |

## NODE\_TEXT\_TEXT\_SELECTION

```
1. NODE_TEXT_TEXT_SELECTION = 1046
```

设置文本选择区域，设置后选中区域将被高亮显示，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 文本选择的起始位置。 |
| .value[1].i32 | 文本选择的结束位置。 |
| .object | 选择选项。参数类型为[ArkUI\_SelectionOptions](capi-arkui-nativemodule-arkui-selectionoptions.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 文本选择的起始位置。 |
| .value[1].i32 | 文本选择的结束位置。 |
| .object | 选择选项。参数类型为[ArkUI\_SelectionOptions](capi-arkui-nativemodule-arkui-selectionoptions.md)。 |

## NODE\_TEXT\_COMPRESS\_LEADING\_PUNCTUATION

```
1. NODE_TEXT_COMPRESS_LEADING_PUNCTUATION = 1048
```

文本行首标点压缩开关，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否打开行首标点压缩开关。  true表示开启行首标点压缩，false表示关闭行首标点压缩。默认值false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否打开行首标点压缩开关。 |

## NODE\_TEXT\_INCLUDE\_FONT\_PADDING

```
1. NODE_TEXT_INCLUDE_FONT_PADDING = 1049
```

设置是否在首行和尾行增加间距以避免文字截断。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置是否在首行和尾行增加间距以避免文字截断。true表示开启增加间距，false表示关闭增加间距。默认值：false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否在首行和尾行增加间距。true表示增加间距，false表示不增加间距。 |

## NODE\_TEXT\_FALLBACK\_LINE\_SPACING

```
1. NODE_TEXT_FALLBACK_LINE_SPACING = 1050
```

针对多行文字叠加，支持行高基于文字实际高度自适应。此接口仅当行高小于文字实际高度时生效。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 支持行高基于文字实际高度自适应。true表示开启自适应，false表示关闭自适应。默认值：false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否开启行高基于文字实际高度自适应。true表示开启自适应，false表示关闭自适应。 |

## NODE\_TEXT\_MARQUEE\_OPTIONS

```
1. NODE_TEXT_MARQUEE_OPTIONS = 1051
```

文本跑马灯模式配置项，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 文本跑马灯模式配置，参数类型为[ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 文本跑马灯模式配置，参数类型为[ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)。 |

## NODE\_TEXT\_DIRECTION

```
1. NODE_TEXT_DIRECTION = 1052
```

文本排版方向。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示文本的排版方向，取[ArkUI\_TextDirection](capi-native-type-h.md#arkui_textdirection)枚举值。默认值为ARKUI\_TEXT\_DIRECTION\_DEFAULT。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示文本的排版方向，对应取值及含义请参考[ArkUI\_TextDirection](capi-native-type-h.md#arkui_textdirection)枚举值。 |

## NODE\_TEXT\_SELECTED\_DRAG\_PREVIEW\_STYLE

```
1. NODE_TEXT_SELECTED_DRAG_PREVIEW_STYLE = 1053
```

用于设置文本选中状态下的拖拽预览样式。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 文本选中状态下的拖拽预览样式。参数类型为[ArkUI\_SelectedDragPreviewStyle](ui-nativemodule-arkui-textselecteddragpreviewstyle.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 文本选中状态下的拖拽预览样式。参数类型为[ArkUI\_SelectedDragPreviewStyle](ui-nativemodule-arkui-textselecteddragpreviewstyle.md)。 |

## NODE\_SPAN\_CONTENT

```
1. NODE_SPAN_CONTENT = MAX_NODE_SCOPE_NUM * ARKUI_NODE_SPAN = 2000
```

文本内容属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 表示[span](ts-basic-components-span.md)的文本内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 表示span的文本内容。 |

## NODE\_SPAN\_TEXT\_BACKGROUND\_STYLE

```
1. NODE_SPAN_TEXT_BACKGROUND_STYLE = 2001
```

文本背景色属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 表示文本背景颜色，0xargb格式，形如0xFFFF0000 表示红色。  第二个参数为文本背景圆角设置，支持如下两种设置方式：  - .value[1].f32：四个方向的圆角半径统一设置，单位为vp。  - .value[1].f32：设置左上角圆角半径，单位为vp。 |
| .value[2].f32 | 设置右上角圆角半径，单位为vp。 |
| .value[3].f32 | 设置左下角圆角半径，单位为vp。 |
| .value[4].f32 | 设置右下角圆角半径，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 文本背景颜色，0xargb格式。 |
| .value[1].f32 | 左上角圆角半径，单位为vp。 |
| .value[2].f32 | 右上角圆角半径，单位为vp。 |
| .value[3].f32 | 左下角圆角半径，单位为vp。 |
| .value[4].f32 | 右下角圆角半径，单位为vp。 |

## NODE\_SPAN\_BASELINE\_OFFSET

```
1. NODE_SPAN_BASELINE_OFFSET = 2002
```

文本基线的偏移量属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 偏移量数值，单位为fp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 偏移量数值，单位为fp。 |

## NODE\_IMAGE\_SPAN\_SRC

```
1. NODE_IMAGE_SPAN_SRC = MAX_NODE_SCOPE_NUM * ARKUI_NODE_IMAGE_SPAN = 3000
```

imageSpan组件图片地址属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 表示imageSpan的图片地址。 |
| .object | 表示 PixelMap 图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)。  .object参数和.string参数二选一，不可同时设置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 表示imageSpan的图片地址。 |
| .object | 表示 PixelMap 图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)。 |

## NODE\_IMAGE\_SPAN\_VERTICAL\_ALIGNMENT

```
1. NODE_IMAGE_SPAN_VERTICAL_ALIGNMENT = 3001
```

图片基于文本的对齐方式属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示图片基于文本的对齐方式，取[ArkUI\_ImageSpanAlignment](capi-native-type-h.md#arkui_imagespanalignment)枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示图片基于文本的对齐方式，取[ArkUI\_ImageSpanAlignment](capi-native-type-h.md#arkui_imagespanalignment)枚举值。 |

## NODE\_IMAGE\_SPAN\_ALT

```
1. NODE_IMAGE_SPAN_ALT = 3002
```

imageSpan组件占位图地址属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 表示image组件占位图地址(不支持gif类型图源)。 |
| .object | 表示 PixelMap 图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)；  .object参数和.string参数二选一，不可同时设置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 表示image组件占位图地址。 |
| .object | 表示 PixelMap 图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)。 |

## NODE\_IMAGE\_SPAN\_BASELINE\_OFFSET

```
1. NODE_IMAGE_SPAN_BASELINE_OFFSET = 3003
```

imageSpan组件的基线偏移量属性，支持属性设置，属性重置和属性获取接口。偏移量数值为正数时向上偏移，负数时向下偏移，默认值0，单位为fp。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 偏移量数值，单位为fp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 偏移量数值，单位为fp。 |

## NODE\_IMAGE\_SPAN\_COLOR\_FILTER

```
1. NODE_IMAGE_SPAN_COLOR_FILTER = 3004
```

图片滤镜效果属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 ~ .value[19].f32 | 表示滤镜矩阵数组。 |
| .size | 表示滤镜数组大小为5x4。 |
| .object | 颜色滤波器指针，参数类型为[OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md)。  .object和.size参数只能二选一，不可同时设置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 ~ .value[19].f32 | 表示滤镜矩阵数组。 |
| .size | 表示滤镜数组大小为5x4。 |
| .object | 颜色滤波器指针，参数类型为[OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md)。 |

## NODE\_IMAGE\_SPAN\_SUPPORT\_SVG2

```
1. NODE_IMAGE_SPAN_SUPPORT_SVG2 = 3005
```

通过启用SVG新解析能力开关设置SVG解析功能支持的范围，支持属性设置，属性重置，属性获取接口。ImageSpan组件创建后，不支持动态修改该属性的值。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否启用SVG新解析能力开关。true：支持SVG解析新能力；false：保持原有SVG解析能力。  默认值：false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否启用SVG新解析能力开关。 |
