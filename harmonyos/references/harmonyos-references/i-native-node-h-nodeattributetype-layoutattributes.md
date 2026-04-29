---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-native-node-h-nodeattributetype-layoutattributes
title: ArkUI_NodeAttributeType（布局属性）
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_node.h > ArkUI_NodeAttributeType（布局属性）
category: harmonyos-references
scraped_at: 2026-04-29T13:54:12+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:b99b7eaf674994e62e49c428b2a4267e51273d6624d20e17828377b5c338ac15
---

```
1. enum ArkUI_NodeAttributeType
```

## 概述

定义ArkUI在Native侧可以设置的布局相关属性集合，包含尺寸、百分比尺寸、内外边距、边框、位置、对齐、方向、约束、Flex参数、布局规则及布局类组件相关属性设置。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)

## NODE\_WIDTH

```
1. NODE_WIDTH = 0
```

宽度属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 宽度数值，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 宽度数值，单位为vp。 |

## NODE\_HEIGHT

```
1. NODE_HEIGHT = 1
```

高度属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 高度数值，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 高度数值，单位为vp。 |

## NODE\_PADDING

```
1. NODE_PADDING = 4
```

内间距属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

1：上下左右四个位置的内间距值相等。

| 参数项 | 描述 |
| --- | --- |
| value[0].f32 | 内间距数值，单位为vp。 |

2：分别指定上下左右四个位置的内间距值。

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 上内间距数值，单位为vp，默认值为0vp。 |
| .value[1].f32 | 右内间距数值，单位为vp，默认值为0vp。 |
| .value[2].f32 | 下内间距数值，单位为vp，默认值为0vp。 |
| .value[3].f32 | 左内间距数值，单位为vp，默认值为0vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 上内间距数值，单位为vp。 |
| .value[1].f32 | 右内间距数值，单位为vp。 |
| .value[2].f32 | 下内间距数值，单位为vp。 |
| .value[3].f32 | 左内间距数值，单位为vp。 |

## NODE\_MARGIN

```
1. NODE_MARGIN = 7
```

外间距属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

1：上下左右四个位置的外间距值相等。

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 上下左右四个位置的外间距值相等时的外间距数值，单位为vp。 |

2：分别指定上下左右四个位置的外间距值。

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 上外间距数值，单位为vp，默认值为0vp。 |
| .value[1].f32 | 右外间距数值，单位为vp，默认值为0vp。 |
| .value[2].f32 | 下外间距数值，单位为vp，默认值为0vp。 |
| .value[3].f32 | 左外间距数值，单位为vp，默认值为0vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 上外间距数值，单位为vp。 |
| .value[1].f32 | 右外间距数值，单位为vp。 |
| .value[2].f32 | 下外间距数值，单位为vp。 |
| .value[3].f32 | 左外间距数值，单位为vp。 |

## NODE\_ALIGNMENT

```
1. NODE_ALIGNMENT = 15
```

设置组件内容在元素绘制区域内的对齐方式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 对齐方式，参数类型[ArkUI\_Alignment](capi-native-type-h.md#arkui_alignment)，默认值为ARKUI\_ALIGNMENT\_CENTER。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 对齐方式，参数类型[ArkUI\_Alignment](capi-native-type-h.md#arkui_alignment)。 |

## NODE\_BORDER\_WIDTH

```
1. NODE_BORDER_WIDTH = 17
```

边框宽度属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

1.统一设置四条边的边框宽度。

| 参数项 | 描述 |
| --- | --- |
| 1. .value[0].f32 | 统一设置四条边的边框宽度。 |

2.分别设置四条边的边框宽度。

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 设置上边框的边框宽度。 |
| .value[1].f32 | 设置右边框的边框宽度。 |
| .value[2].f32 | 设置下边框的边框宽度。 |
| .value[3].f32 | 设置左边框的边框宽度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 设置上边框的边框宽度。 |
| .value[1].f32 | 设置右边框的边框宽度。 |
| .value[2].f32 | 设置下边框的边框宽度。 |
| .value[3].f32 | 设置左边框的边框宽度。 |

## NODE\_BORDER\_RADIUS

```
1. NODE_BORDER_RADIUS = 18
```

边框圆角属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

1.统一设置四条边的边框圆角。

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 统一设置四条边的边框圆角。 |

2.统一设置四条边的边框圆角。

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 设置左上角圆角半径。 |
| .value[1].f32 | 设置右上角圆角半径。 |
| .value[2].f32 | 设置左下角圆角半径。 |
| .value[3].f32 | 设置右下角圆角半径。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 设置左上角圆角半径。 |
| .value[1].f32 | 设置右上角圆角半径。 |
| .value[2].f32 | 设置左下角圆角半径。 |
| .value[3].f32 | 设置右下角圆角半径。 |

## NODE\_BORDER\_COLOR

```
1. NODE_BORDER_COLOR = 19
```

边框颜色属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

1.统一设置四条边的边框颜色。

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 统一设置四条边的边框颜色，使用0xargb表示，如0xFFFF11FF。 |

2.分别设置四条边的边框颜色。

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 设置上侧边框颜色，使用0xargb表示，默认值为0xFF000000。 |
| .value[1].u32 | 设置右侧边框颜色，使用0xargb表示，默认值为0xFF000000。 |
| .value[2].u32 | 设置下侧边框颜色，使用0xargb表示，默认值为0xFF000000。 |
| .value[3].u32 | 设置左侧边框颜色，使用0xargb表示，默认值为0xFF000000。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 设置上侧边框颜色，使用0xargb表示，如0xFFFF11FF。 |
| .value[1].u32 | 设置右侧边框颜色，使用0xargb表示，如0xFFFF11FF。 |
| .value[2].u32 | 设置下侧边框颜色，使用0xargb表示，如0xFFFF11FF。 |
| .value[3].u32 | 设置左侧边框颜色，使用0xargb表示，如0xFFFF11FF。 |

## NODE\_BORDER\_STYLE

```
1. NODE_BORDER_STYLE = 20
```

边框线条样式属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

1.统一设置四条边的边框颜色。

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 统一设置四条边的边框线条样式，参数类型[ArkUI\_BorderStyle](capi-native-type-h.md#arkui_borderstyle)，默认值为ARKUI\_BORDER\_STYLE\_SOLID。 |

2.分别设置四条边的边框颜色。

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置上侧边框线条样式，参数类型[ArkUI\_BorderStyle](capi-native-type-h.md#arkui_borderstyle)，默认值为ARKUI\_BORDER\_STYLE\_SOLID。 |
| .value[1].i32 | 设置右侧边框线条样式，参数类型[ArkUI\_BorderStyle](capi-native-type-h.md#arkui_borderstyle)，默认值为ARKUI\_BORDER\_STYLE\_SOLID。 |
| .value[2].i32 | 设置下侧边框线条样式，参数类型[ArkUI\_BorderStyle](capi-native-type-h.md#arkui_borderstyle)，默认值为ARKUI\_BORDER\_STYLE\_SOLID。 |
| .value[3].i32 | 设置左侧边框线条样式，参数类型[ArkUI\_BorderStyle](capi-native-type-h.md#arkui_borderstyle)，默认值为ARKUI\_BORDER\_STYLE\_SOLID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 上侧边框线条样式对应的数值。 |
| .value[1].i32 | 右侧边框线条样式对应的数值。 |
| .value[2].i32 | 下侧边框线条样式对应的数值。 |
| .value[3].i32 | 左侧边框线条样式对应的数值。 |

## NODE\_POSITION

```
1. NODE_POSITION = 27
```

元素左上角相对于父容器左上角偏移位置，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | x轴坐标。 |
| .value[1].f32 | y轴坐标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | x轴坐标。 |
| .value[1].f32 | y轴坐标。 |

## NODE\_DIRECTION

```
1. NODE_DIRECTION = 47
```

设置容器元素内主轴方向上的布局，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 主轴方向，参数类型[ArkUI\_Direction](capi-native-type-h.md#arkui_direction)，默认值为ARKUI\_DIRECTION\_AUTO。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 主轴方向，参数类型[ArkUI\_Direction](capi-native-type-h.md#arkui_direction)。 |

## NODE\_CONSTRAINT\_SIZE

```
1. NODE_CONSTRAINT_SIZE = 48
```

约束尺寸属性，组件布局时，进行尺寸范围限制，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 最小宽度，单位为vp。 |
| .value[1].f32 | 最大宽度，单位为vp。 |
| .value[2].f32 | 最小高度，单位为vp。 |
| .value[3].f32 | 最大高度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 最小宽度，单位为vp。 |
| .value[1].f32 | 最大宽度，单位为vp。 |
| .value[2].f32 | 最小高度，单位为vp。 |
| .value[3].f32 | 最大高度，单位为vp。 |

## NODE\_OFFSET

```
1. NODE_OFFSET = 54
```

组件子元素相对组件自身的额外偏移属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | x轴偏移量，单位为vp。 |
| .value[1].f32 | y轴偏移量，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | x轴偏移量，单位为vp。 |
| .value[1].f32 | y轴偏移量，单位为vp。 |

## NODE\_MARK\_ANCHOR

```
1. NODE_MARK_ANCHOR = 55
```

组件子元素在位置定位时的锚点属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 锚点x轴坐标，单位为vp。 |
| .value[1].f32 | 锚点y轴坐标，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 锚点x轴坐标，单位为vp。 |
| .value[1].f32 | 锚点y轴坐标，单位为vp。 |

## NODE\_ALIGN\_RULES

```
1. NODE_ALIGN_RULES = 57
```

相对容器中子组件的对齐规则属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 相对容器中子组件的对齐规则，参数类型为[ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 相对容器中子组件的对齐规则，参数类型为[ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)。 |

## NODE\_ALIGN\_SELF

```
1. NODE_ALIGN_SELF = 58
```

设置子组件在父容器交叉轴的对齐格式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 子组件在父容器交叉轴上的对齐方式，参数类型[ArkUI\_ItemAlignment](capi-native-type-h.md#arkui_itemalignment)，默认值为ARKUI\_ITEM\_ALIGNMENT\_AUTO。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 子组件在父容器交叉轴上的对齐方式，参数类型[ArkUI\_ItemAlignment](capi-native-type-h.md#arkui_itemalignment)。 |

## NODE\_FLEX\_GROW

```
1. NODE_FLEX_GROW = 59
```

设置组件在父容器的剩余空间所占比例，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 组件在父容器剩余空间中所占比例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 组件在父容器剩余空间中所占比例。 |

## NODE\_FLEX\_SHRINK

```
1. NODE_FLEX_SHRINK = 60
```

设置父容器压缩尺寸分配给此属性所在组件的比例，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 父容器压缩尺寸分配给当前组件的比例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 父容器压缩尺寸分配给当前组件的比例。 |

## NODE\_FLEX\_BASIS

```
1. NODE_FLEX_BASIS = 61
```

设置组件的基准尺寸，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 组件在父容器主轴上的基准尺寸。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 组件在父容器主轴上的基准尺寸。 |

## NODE\_ASPECT\_RATIO

```
1. NODE_ASPECT_RATIO = 67
```

设置组件的宽高比，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 组件宽高比，格式为宽度/高度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 组件宽高比，格式为宽度/高度。 |

## NODE\_LAYOUT\_WEIGHT

```
1. NODE_LAYOUT_WEIGHT = 68
```

Row/Column/Flex布局下的子组件布局权重参数，支持属性设置、属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 组件在主轴上的布局权重。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 组件在主轴上的布局权重。 |

## NODE\_DISPLAY\_PRIORITY

```
1. NODE_DISPLAY_PRIORITY = 69
```

Row/Column/Flex（单行）布局下的子组件在布局容器中显示的优先级，支持属性设置，属性重置和属性获取接口。

当displayPriority大于1时，值越大优先级越高。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 组件在布局容器中的显示优先级。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 组件在布局容器中的显示优先级。 |

## NODE\_OUTLINE\_WIDTH

```
1. NODE_OUTLINE_WIDTH = 70
```

设置元素的外描边宽度，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 左侧外描边宽度，单位为vp。 |
| .value[1].f32 | 上侧外描边宽度，单位为vp。 |
| .value[2].f32 | 右侧外描边宽度，单位为vp。 |
| .value[3].f32 | 下侧外描边宽度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 左侧外描边宽度，单位为vp。 |
| .value[1].f32 | 上侧外描边宽度，单位为vp。 |
| .value[2].f32 | 右侧外描边宽度，单位为vp。 |
| .value[3].f32 | 下侧外描边宽度，单位为vp。 |

## NODE\_WIDTH\_PERCENT

```
1. NODE_WIDTH_PERCENT = 71
```

宽度属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 宽度数值，单位为百分比。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 宽度数值，单位为百分比。 |

## NODE\_HEIGHT\_PERCENT

```
1. NODE_HEIGHT_PERCENT = 72
```

高度属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 高度数值，单位为百分比。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 高度数值，单位为百分比。 |

## NODE\_PADDING\_PERCENT

```
1. NODE_PADDING_PERCENT = 73
```

内间距属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| 1. .value[0].f32 | 上下左右四个位置的内间距值相等时的内间距数值，单位为百分比。 |
| 2. .value[0].f32 | 上内间距数值，单位为百分比。 |
| .value[1].f32 | 右内间距数值，单位为百分比。 |
| .value[2].f32 | 下内间距数值，单位为百分比。 |
| .value[3].f32 | 左内间距数值，单位为百分比。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 上内间距数值，单位为百分比。 |
| .value[1].f32 | 右内间距数值，单位为百分比。 |
| .value[2].f32 | 下内间距数值，单位为百分比。 |
| .value[3].f32 | 左内间距数值，单位为百分比。 |

## NODE\_MARGIN\_PERCENT

```
1. NODE_MARGIN_PERCENT = 74
```

外间距属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| 1. .value[0].f32 | 上下左右四个位置的外间距值相等时的外间距数值，单位为百分比。 |
| 2. .value[0].f32 | 上外间距数值，单位为百分比。 |
| .value[1].f32 | 右外间距数值，单位为百分比。 |
| .value[2].f32 | 下外间距数值，单位为百分比。 |
| .value[3].f32 | 左外间距数值，单位为百分比。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 上外间距数值，单位为百分比。 |
| .value[1].f32 | 右外间距数值，单位为百分比。 |
| .value[2].f32 | 下外间距数值，单位为百分比。 |
| .value[3].f32 | 左外间距数值，单位为百分比。 |

## NODE\_RELATIVE\_LAYOUT\_CHAIN\_MODE

```
1. NODE_RELATIVE_LAYOUT_CHAIN_MODE = 76
```

指定以该组件为链头所构成的链的参数，支持属性设置、属性重置和属性获取接口。仅当父容器为RelativeContainer时生效。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 链的方向。枚举[ArkUI\_Axis](capi-native-type-h.md#arkui_axis)。 |
| .value[1].i32 | 链的样式。枚举[ArkUI\_RelativeLayoutChainStyle](capi-native-type-h.md#arkui_relativelayoutchainstyle)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 链的方向。枚举[ArkUI\_Axis](capi-native-type-h.md#arkui_axis)。 |
| .value[1].i32 | 链的样式。枚举[ArkUI\_RelativeLayoutChainStyle](capi-native-type-h.md#arkui_relativelayoutchainstyle)。 |

## NODE\_SIZE

```
1. NODE_SIZE = 79
```

设置高宽尺寸，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 宽度数值，单位为vp。 |
| .value[1].f32 | 高度数值，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 宽度数值，单位为vp。 |
| .value[1].f32 | 高度数值，单位为vp。 |

## NODE\_LAYOUT\_RECT

```
1. NODE_LAYOUT_RECT = 83
```

组件布局大小位置属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 组件x轴坐标，单位为px。 |
| .value[1].i32 | 组件y轴坐标，单位为px。 |
| .value[2].i32 | 组件宽度，单位为px。 |
| .value[3].i32 | 组件高度，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 组件x轴坐标，单位为px。 |
| .value[1].i32 | 组件y轴坐标，单位为px。 |
| .value[2].i32 | 组件宽度，单位为px。 |
| .value[3].i32 | 组件高度，单位为px。 |

## NODE\_BORDER\_WIDTH\_PERCENT

```
1. NODE_BORDER_WIDTH_PERCENT = 85
```

边框宽度属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| 1. .value[0].f32 | 统一设置四条边的边框宽度，单位为百分比。 |
| 2. .value[0].f32 | 设置上边框的边框宽度，单位为百分比。 |
| .value[1].f32 | 设置右边框的边框宽度，单位为百分比。 |
| .value[2].f32 | 设置下边框的边框宽度，单位为百分比。 |
| .value[3].f32 | 设置左边框的边框宽度，单位为百分比。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 设置上边框的边框宽度，单位为百分比。 |
| .value[1].f32 | 设置右边框的边框宽度，单位为百分比。 |
| .value[2].f32 | 设置下边框的边框宽度，单位为百分比。 |
| .value[3].f32 | 设置左边框的边框宽度，单位为百分比。 |

## NODE\_BORDER\_RADIUS\_PERCENT

```
1. NODE_BORDER_RADIUS_PERCENT = 86
```

边框圆角属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| 1. .value[0].f32 | 统一设置四条边的边框圆角半径，单位为百分比。 |
| 2. .value[0].f32 | 设置左上角圆角半径，单位为百分比。 |
| .value[1].f32 | 设置右上角圆角半径，单位为百分比。 |
| .value[2].f32 | 设置左下角圆角半径，单位为百分比。 |
| .value[3].f32 | 设置右下角圆角半径，单位为百分比。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 设置左上角圆角半径，单位为百分比。 |
| .value[1].f32 | 设置右上角圆角半径，单位为百分比。 |
| .value[2].f32 | 设置左下角圆角半径，单位为百分比。 |
| .value[3].f32 | 设置右下角圆角半径，单位为百分比。 |

## NODE\_WIDTH\_LAYOUTPOLICY

```
1. NODE_WIDTH_LAYOUTPOLICY = 105
```

设置组件宽度布局策略，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 布局策略，参数类型[ArkUI\_LayoutPolicy](capi-native-type-h.md#arkui_layoutpolicy)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 布局策略，参数类型[ArkUI\_LayoutPolicy](capi-native-type-h.md#arkui_layoutpolicy)。 |

## NODE\_HEIGHT\_LAYOUTPOLICY

```
1. NODE_HEIGHT_LAYOUTPOLICY = 106
```

设置组件高度布局策略，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 布局策略，参数类型[ArkUI\_LayoutPolicy](capi-native-type-h.md#arkui_layoutpolicy)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 布局策略，参数类型[ArkUI\_LayoutPolicy](capi-native-type-h.md#arkui_layoutpolicy)。 |

## NODE\_POSITION\_EDGES

```
1. NODE_POSITION_EDGES = 107
```

设置组件相对容器内容区边界的位置，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 组件相对容器内容区边界的位置，参数类型为[ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 组件相对容器内容区边界的位置，参数类型为[ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)。 |

## NODE\_CHAIN\_WEIGHT

```
1. NODE_CHAIN_WEIGHT = 118
```

父组件为RelativeContainer时，设置已形成链的组件的布局位置，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 组件在水平方向的布局权重，默认值：0。设置异常值时，按默认值显示。 |
| .value[1].f32 | 组件在竖直方向的布局权重，默认值：0。设置异常值时，按默认值显示。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 组件在水平方向的布局权重。 |
| .value[1].f32 | 组件在竖直方向的布局权重。 |

## NODE\_IGNORE\_LAYOUT\_SAFE\_AREA

```
1. NODE_IGNORE_LAYOUT_SAFE_AREA = 119
```

设置扩展组件布局时的安全区域，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 扩展安全区域的类型。参数类型为[ArkUI\_LayoutSafeAreaType](capi-native-type-h.md#arkui_layoutsafeareatype)，默认值：ARKUI\_LAYOUT\_SAFE\_AREA\_TYPE\_SYSTEM。设置异常值时，按默认值显示。 |
| .value[1].u32 | 扩展安全区域的方向。参数类型为[ArkUI\_LayoutSafeAreaEdge](capi-native-type-h.md#arkui_layoutsafeareaedge)，默认值：ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_ALL，例如：ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_TOP | ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_BOTTOM。设置异常值时，按默认值显示。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 扩展安全区域的类型。 |
| .value[1].u32 | 扩展安全区域的方向。 |

## NODE\_DASH\_WIDTH

```
1. NODE_DASH_WIDTH = 120
```

设置边框样式为虚线时虚线的长度，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 上边框虚线的长度，单位vp。取值范围：[0, +∞)。设置异常值时，按默认的虚线效果显示。 |
| .value[1].f32 | 右边框虚线的长度，单位vp。取值范围：[0, +∞)。设置异常值时，按默认的虚线效果显示。 |
| .value[2].f32 | 下边框虚线的长度，单位vp。取值范围：[0, +∞)。设置异常值时，按默认的虚线效果显示。 |
| .value[3].f32 | 左边框虚线的长度，单位vp。取值范围：[0, +∞)。设置异常值时，按默认的虚线效果显示。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 上边框虚线的长度，单位vp。 |
| .value[1].f32 | 右边框虚线的长度，单位vp。 |
| .value[2].f32 | 下边框虚线的长度，单位vp。 |
| .value[3].f32 | 左边框虚线的长度，单位vp。 |

## NODE\_DASH\_GAP

```
1. NODE_DASH_GAP = 121
```

设置边框样式为虚线时虚线的间隙，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 上边框虚线的间隙，单位vp。取值范围：[0, +∞)。设置异常值时，按默认的虚线效果显示。 |
| .value[1].f32 | 右边框虚线的间隙，单位vp。取值范围：[0, +∞)。设置异常值时，按默认的虚线效果显示。 |
| .value[2].f32 | 下边框虚线的间隙，单位vp。取值范围：[0, +∞)。设置异常值时，按默认的虚线效果显示。 |
| .value[3].f32 | 左边框虚线的间隙，单位vp。取值范围：[0, +∞)。设置异常值时，按默认的虚线效果显示。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 上边框虚线的间隙，单位vp。 |
| .value[1].f32 | 右边框虚线的间隙，单位vp。 |
| .value[2].f32 | 下边框虚线的间隙，单位vp。 |
| .value[3].f32 | 左边框虚线的间隙，单位vp。 |

## NODE\_LAYOUT\_GRAVITY

```
1. NODE_LAYOUT_GRAVITY = 122
```

设置Stack容器中子组件的对齐规则，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Stack容器中子组件的对齐规则。参数类型为[ArkUI\_LocalizedAlignment](capi-native-type-h.md#arkui_localizedalignment)，默认值：ARKUI\_ALIGNMENT\_CENTER。设置异常值时，按默认值显示。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Stack容器中子组件的对齐规则。参数类型为[ArkUI\_LocalizedAlignment](capi-native-type-h.md#arkui_localizedalignment)。 |

## NODE\_BORDER\_RADIUS\_TYPE

```
1. NODE_BORDER_RADIUS_TYPE = 123
```

设置组件绘制圆角的模式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 组件绘制圆角的模式。参数类型为[ArkUI\_RenderStrategy](capi-native-type-h.md#arkui_renderstrategy)，默认值：ARKUI\_RENDERSTRATEGY\_FAST。设置异常值时，按默认值显示。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 组件绘制圆角的模式。参数类型为[ArkUI\_RenderStrategy](capi-native-type-h.md#arkui_renderstrategy)。 |
