---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-xcomponent
title: ArkUI_NodeAttributeType（XComponent组件相关属性）
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_node.h > ArkUI_NodeAttributeType（XComponent组件相关属性）
category: harmonyos-references
scraped_at: 2026-04-29T13:54:16+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:ec7cab6e578d57bc111569974e8f54a50683c8d713bdd577eae10d902648f0d7
---

```
1. enum ArkUI_NodeAttributeType
```

## 概述

定义ArkUI在Native侧可以设置的XComponent组件相关属性集合。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)

## NODE\_XCOMPONENT\_ID

```
1. NODE_XCOMPONENT_ID = MAX_NODE_SCOPE_NUM * ARKUI_NODE_XCOMPONENT = 12000
```

XComponent组件ID属性，支持属性设置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | ID的内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | ID的内容。 |

## NODE\_XCOMPONENT\_TYPE

```
1. NODE_XCOMPONENT_TYPE = 12001
```

XComponent组件的类型，仅支持属性获取接口。

XComponent组件的类型需要在组件创建时通过[ArkUI\_NodeType](capi-native-node-h.md#arkui_nodetype)中的ARKUI\_NODE\_XCOMPONENT或者ARKUI\_NODE\_XCOMPONENT\_TEXTURE明确，不允许后续修改。

使用[setAttribute](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setattribute)接口尝试修改XComponent组件的类型时会发生绘制内容异常。

作为属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | XComponent组件的类型，参数类型为[ArkUI\_XComponentType](capi-native-type-h.md#arkui_xcomponenttype)。 |

## NODE\_XCOMPONENT\_SURFACE\_SIZE

```
1. NODE_XCOMPONENT_SURFACE_SIZE = 12002
```

XComponent组件的宽高，仅支持属性获取接口。

使用[setAttribute](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setattribute)接口尝试修改XComponent组件的宽高时设置不会生效。

作为属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 宽数值，单位为px。 |
| .value[1].u32 | 高数值，单位为px。 |

## NODE\_XCOMPONENT\_SURFACE\_RECT

```
1. NODE_XCOMPONENT_SURFACE_RECT = 12003
```

设置XComponent组件持有Surface的显示区域，支持属性设置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | Surface显示区域相对于XComponent组件左上角的x轴坐标，单位为px。 |
| .value[1].i32 | Surface显示区域相对于XComponent组件左上角的y轴坐标，单位为px。 |
| .value[2].i32 | Surface显示区域的宽度，单位为px。 |
| .value[3].i32 | Surface显示区域的高度，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | Surface显示区域相对于XComponent组件左上角的x轴坐标，单位为px。 |
| .value[1].i32 | Surface显示区域相对于XComponent组件左上角的y轴坐标，单位为px。 |
| .value[2].i32 | Surface显示区域的宽度，单位为px。 |
| .value[3].i32 | Surface显示区域的高度，单位为px。 |

## NODE\_XCOMPONENT\_ENABLE\_ANALYZER

```
1. NODE_XCOMPONENT_ENABLE_ANALYZER = 12004
```

设置XComponent组件是否支持图像分析，支持属性设置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否支持图像分析，1表示支持图像分析，0表示不支持图像分析，默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否支持图像分析，1表示支持图像分析，0表示不支持图像分析，默认值：0。 |
