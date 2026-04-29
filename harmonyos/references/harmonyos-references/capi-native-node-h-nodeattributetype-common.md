---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-common
title: ArkUI_NodeAttributeType（通用属性）
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_node.h > ArkUI_NodeAttributeType（通用属性）
category: harmonyos-references
scraped_at: 2026-04-29T13:54:12+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:c46a2b65189901ea67227fd4e1c03c58101860cea5beb2bc0811212443c08f92
---

```
1. enum ArkUI_NodeAttributeType
```

## 概述

定义ArkUI在Native侧可以设置的通用属性样式集合。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)

## NODE\_WIDTH

```
1. NODE_WIDTH = 0
```

宽度属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem]格式如下。

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

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem]格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 高度数值，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 高度数值，单位为vp。 |

## NODE\_BACKGROUND\_COLOR

```
1. NODE_BACKGROUND_COLOR = 2
```

背景色属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem]格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 背景色数值，0xargb格式，形如 0xFFFF0000 表示红色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 背景色数值，0xargb格式，形如 0xFFFF0000 表示红色。 |

## NODE\_BACKGROUND\_IMAGE

```
1. NODE_BACKGROUND_IMAGE = 3
```

背景色图片属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem]格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 图片地址。API version 22及之前版本，支持网络图片资源地址、本地图片资源地址、Base64和[PixelMap](arkts-apis-image-pixelmap.md)资源，不支持[svg](js-components-svg.md)图片、gif和webp等类型的动图。 从API version 23开始，新增支持webp和gif类型的动图，显示动图第一帧，不支持其他类型的动图。 |
| .value[0]?.i32 | 可选值，repeat参数，参数类型[ArkUI\_ImageRepeat](capi-native-type-h.md#arkui_imagerepeat)，默认值为ARKUI\_IMAGE\_REPEAT\_NONE。 |
| .object | PixelMap 图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)。  .object参数和.string参数二选一，不可同时设置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 图片地址。API version 22及之前版本，支持网络图片资源地址、本地图片资源地址、Base64和PixelMap资源，不支持svg图片、gif和webp等类型的动图。 从API version 23开始，新增支持webp和gif类型的动图，显示动图第一帧，不支持其他类型的动图。 |
| .value[0].i32 | repeat参数，参数类型[ArkUI\_ImageRepeat](capi-native-type-h.md#arkui_imagerepeat)。 |
| .object | PixelMap 图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)。 |
