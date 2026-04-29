---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-native-node-h-nodeattributetype-layoutcomponent
title: ArkUI_NodeAttributeType（布局类组件相关属性）
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_node.h > ArkUI_NodeAttributeType（布局类组件相关属性）
category: harmonyos-references
scraped_at: 2026-04-29T13:54:12+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:1eb34ea34fb3008250bc2d5f9b0eb4f8bf3b6647fc903a46fc9e90227206fabb
---

```
1. enum ArkUI_NodeAttributeType
```

## 概述

定义ArkUI在Native侧可以设置的布局类组件相关属性集合。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)

## NODE\_STACK\_ALIGN\_CONTENT

```
1. NODE_STACK_ALIGN_CONTENT = MAX_NODE_SCOPE_NUM * ARKUI_NODE_STACK = 1000000
```

设置子组件在容器内的对齐方式，支持属性设置，属性重置和属性获取接口。该属性与通用属性NODE\_ALIGNMENT同时设置时，后设置的属性生效。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 对齐方式，数据类型[ArkUI\_Alignment](capi-native-type-h.md#arkui_alignment)，默认值ARKUI\_ALIGNMENT\_CENTER。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 对齐方式，数据类型[ArkUI\_Alignment](capi-native-type-h.md#arkui_alignment)。 |

## NODE\_COLUMN\_ALIGN\_ITEMS

```
1. NODE_COLUMN_ALIGN_ITEMS = MAX_NODE_SCOPE_NUM * ARKUI_NODE_COLUMN = 1006000
```

设置Column子组件在水平方向上的对齐格式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 子组件在水平方向上的对齐格式，数据类型[ArkUI\_HorizontalAlignment](capi-native-type-h.md#arkui_horizontalalignment)，默认值ARKUI\_HORIZONTAL\_ALIGNMENT\_CENTER。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 子组件在水平方向上的对齐格式，数据类型[ArkUI\_HorizontalAlignment](capi-native-type-h.md#arkui_horizontalalignment)。 |

## NODE\_COLUMN\_JUSTIFY\_CONTENT

```
1. NODE_COLUMN_JUSTIFY_CONTENT = 1006001
```

设置Column子组件在垂直方向上的对齐格式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 子组件在垂直方向上的对齐格式，数据类型[ArkUI\_FlexAlignment](capi-native-type-h.md#arkui_flexalignment)，默认值ARKUI\_FLEX\_ALIGNMENT\_START。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 子组件在垂直方向上的对齐格式，数据类型[ArkUI\_FlexAlignment](capi-native-type-h.md#arkui_flexalignment)。 |

## NODE\_LINEAR\_LAYOUT\_SPACE

```
1. NODE_LINEAR_LAYOUT_SPACE = 1006002
```

设置Column或Row子组件的间距，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 子组件之间的间距，单位vp，默认值：0。  取值范围：[0, +∞)。  设置异常值时，按默认值显示。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 子组件之间的间距，单位vp。 |

## NODE\_LINEAR\_LAYOUT\_REVERSE

```
1. NODE_LINEAR_LAYOUT_REVERSE = 1006003
```

设置Column或Row中沿主轴方向的子组件排列是否反向，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 主轴方向的子组件排列是否反向，默认值：false。值为true时，子组件在垂直方向上反转排列。值为false时，子组件在垂直方向上正序排列。  设置异常值时，按默认值显示。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 主轴方向的子组件排列是否反向。 |

## NODE\_ROW\_ALIGN\_ITEMS

```
1. NODE_ROW_ALIGN_ITEMS = MAX_NODE_SCOPE_NUM * ARKUI_NODE_ROW = 1007000
```

设置Row子组件在垂直方向上的对齐格式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 子组件在垂直方向上的对齐格式，数据类型[ArkUI\_VerticalAlignment](capi-native-type-h.md#arkui_verticalalignment)，默认值ARKUI\_VERTICAL\_ALIGNMENT\_CENTER。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 子组件在垂直方向上的对齐格式，数据类型[ArkUI\_VerticalAlignment](capi-native-type-h.md#arkui_verticalalignment)。 |

## NODE\_ROW\_JUSTIFY\_CONTENT

```
1. NODE_ROW_JUSTIFY_CONTENT = 1007001
```

设置Row子组件在水平方向上的对齐格式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 子组件在水平方向上的对齐格式，数据类型[ArkUI\_FlexAlignment](capi-native-type-h.md#arkui_flexalignment)，默认值ARKUI\_FLEX\_ALIGNMENT\_START。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 子组件在水平方向上的对齐格式，数据类型[ArkUI\_FlexAlignment](capi-native-type-h.md#arkui_flexalignment)。 |

## NODE\_FLEX\_OPTION

```
1. NODE_FLEX_OPTION = MAX_NODE_SCOPE_NUM * ARKUI_NODE_FLEX = 1008000
```

设置Flex属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0]?.i32 | 子组件在Flex容器上排列的方向[ArkUI\_FlexDirection](capi-native-type-h.md#arkui_flexdirection)，默认值为ARKUI\_FLEX\_DIRECTION\_ROW。 |
| .value[1]?.i32 | 排列规则[ArkUI\_FlexWrap](capi-native-type-h.md#arkui_flexwrap)，默认值为ARKUI\_FLEX\_WRAP\_NO\_WRAP。 |
| .value[2]?.i32 | 主轴上的对齐格式[ArkUI\_FlexAlignment](capi-native-type-h.md#arkui_flexalignment)，默认值为ARKUI\_FLEX\_ALIGNMENT\_START。 |
| .value[3]?.i32 | 交叉轴上的对齐格式[ArkUI\_ItemAlignment](capi-native-type-h.md#arkui_itemalignment)，默认值为ARKUI\_ITEM\_ALIGNMENT\_START。 |
| .value[4]?.i32 | 交叉轴中有额外的空间时，多行内容的对齐方式[ArkUI\_FlexAlignment](capi-native-type-h.md#arkui_flexalignment)，默认值为ARKUI\_FLEX\_ALIGNMENT\_START。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 子组件在Flex容器上排列的方向的枚举值。 |
| .value[1].i32 | 排列规则的枚举值。 |
| .value[2].i32 | 主轴上的对齐格式的枚举值。 |
| .value[3].i32 | 交叉轴上的对齐格式的枚举值。 |
| .value[4].i32 | 交叉轴中有额外的空间时，多行内容的对齐方式的枚举值。 |

## NODE\_FLEX\_SPACE

```
1. NODE_FLEX_SPACE = 1008001
```

设置Flex容器内子组件的间距，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | Flex容器主轴方向的间距，单位vp，默认值：0。  取值范围：[0, +∞)。  设置异常值时，按默认值显示。 |
| .value[1].f32 | Flex容器交叉轴方向的间距，单位vp，默认值：0。  取值范围：[0, +∞)。  设置异常值时，按默认值显示。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | Flex容器主轴方向的间距，单位vp。 |
| .value[1].f32 | Flex容器交叉轴方向的间距，单位vp。 |

## NODE\_RELATIVE\_CONTAINER\_GUIDE\_LINE

```
1. NODE_RELATIVE_CONTAINER_GUIDE_LINE = MAX_NODE_SCOPE_NUM * ARKUI_NODE_RELATIVE_CONTAINER = 1012000
```

设置RelativeContainer容器内的辅助线，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | RelativeContainer容器内的辅助线，参数类型为[ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | RelativeContainer容器内的辅助线，参数类型为[ArkUI\_GuidelineOption](capi-arkui-nativemodule-arkui-guidelineoption.md)。 |

## NODE\_RELATIVE\_CONTAINER\_BARRIER

```
1. NODE_RELATIVE_CONTAINER_BARRIER = 1012001
```

设置RelativeContainer容器内的屏障，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | RelativeContainer容器内的屏障，参数类型为[ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | RelativeContainer容器内的屏障，参数类型为[ArkUI\_BarrierOption](capi-arkui-nativemodule-arkui-barrieroption.md)。 |
