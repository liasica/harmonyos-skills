---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-image
title: ArkUI_NodeAttributeType（图类组件相关属性）
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_node.h > ArkUI_NodeAttributeType（图类组件相关属性）
category: harmonyos-references
scraped_at: 2026-04-29T13:54:16+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:9da9a5a86043fd667fec865aeaf6b74b5e4d208b23679e42974e78de319f3c21
---

```
1. enum ArkUI_NodeAttributeType
```

## 概述

定义ArkUI在Native侧可以设置的图类组件相关属性样式集合，包含Image和ImageAnimator组件属性设置。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)

## NODE\_IMAGE\_SRC

```
1. NODE_IMAGE_SRC = MAX_NODE_SCOPE_NUM * ARKUI_NODE_IMAGE = 4000
```

[image](ts-basic-components-image.md)组件设置图片地址属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 表示image组件地址。 |
| .object | 表示 PixelMap 图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)；  .object参数和.string参数二选一，不可同时设置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 表示image组件地址。 |
| .object | 表示 PixelMap 图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)。 |

## NODE\_IMAGE\_OBJECT\_FIT

```
1. NODE_IMAGE_OBJECT_FIT = 4001
```

图片填充效果属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示图片填充效果，取[ArkUI\_ObjectFit](capi-native-type-h.md#arkui_objectfit)枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示图片填充效果，取[ArkUI\_ObjectFit](capi-native-type-h.md#arkui_objectfit)枚举值。 |

## NODE\_IMAGE\_INTERPOLATION

```
1. NODE_IMAGE_INTERPOLATION = 4002
```

图片插值效果属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示插值效果，取[ArkUI\_ImageInterpolation](capi-native-type-h.md#arkui_imageinterpolation)枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示插值效果，取[ArkUI\_ImageInterpolation](capi-native-type-h.md#arkui_imageinterpolation)枚举值。 |

## NODE\_IMAGE\_OBJECT\_REPEAT

```
1. NODE_IMAGE_OBJECT_REPEAT = 4003
```

图片重复样式属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示图片重复样式，取[ArkUI\_ImageRepeat](capi-native-type-h.md#arkui_imagerepeat)枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示图片重复样式，取[ArkUI\_ImageRepeat](capi-native-type-h.md#arkui_imagerepeat)枚举值。 |

## NODE\_IMAGE\_COLOR\_FILTER

```
1. NODE_IMAGE_COLOR_FILTER = 4004
```

图片滤镜效果属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 ~ .value[19].f32 | 表示滤镜矩阵数组。 |
| .size | 表示滤镜数组大小 5x4。 |
| .object | 颜色滤波器指针，参数类型为OH\_Drawing\_ColorFilter。  .object和.size参数只能二选一，不可同时设置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 ~ .value[19].f32 | 表示滤镜矩阵数组。 |
| .size | 表示滤镜数组大小 5x4。 |
| .object | 颜色滤波器指针，参数类型为OH\_Drawing\_ColorFilter。 |

## NODE\_IMAGE\_AUTO\_RESIZE

```
1. NODE_IMAGE_AUTO_RESIZE = 4005
```

图源自动缩放属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示是否缩放布尔值，默认值：false。false表示关闭图源自动缩放，true表示开启图源自动缩放。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示是否缩放布尔值。 |

## NODE\_IMAGE\_ALT

```
1. NODE_IMAGE_ALT = 4006
```

占位图地址属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 表示image组件占位图地址。 |
| .object | 表示 PixelMap 图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)；  .object参数和.string参数二选一，不可同时设置，不支持网络图片。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 表示image组件占位图地址。 |
| .object | 表示 PixelMap 图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)。 |

## NODE\_IMAGE\_DRAGGABLE

```
1. NODE_IMAGE_DRAGGABLE = 4007
```

图片拖拽效果属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示是否支持拖拽，设置为true表示支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示是否支持拖拽。 |

## NODE\_IMAGE\_RENDER\_MODE

```
1. NODE_IMAGE_RENDER_MODE = 4008
```

图片渲染模式属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_ImageRenderMode](capi-native-type-h.md#arkui_imagerendermode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_ImageRenderMode](capi-native-type-h.md#arkui_imagerendermode)。 |

## NODE\_IMAGE\_FIT\_ORIGINAL\_SIZE

```
1. NODE_IMAGE_FIT_ORIGINAL_SIZE = 4009
```

设置图片的显示尺寸是否跟随图源尺寸，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置图片的显示尺寸是否跟随图源尺寸，1表示跟随，0表示不跟随，默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 1表示图片的显示尺寸跟随图源尺寸，0表示图片的显示尺寸不跟随图源尺寸。 |

## NODE\_IMAGE\_FILL\_COLOR

```
1. NODE_IMAGE_FILL_COLOR = 4010
```

设置填充颜色，设置后填充颜色会覆盖在图片上，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 填充色数值，0xargb格式，形如 0xFFFF0000 表示红色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 填充色数值，0xargb格式。 |

## NODE\_IMAGE\_RESIZABLE

```
1. NODE_IMAGE_RESIZABLE = 4011
```

设置图像拉伸时，可调整大小的图像选项。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 图片左部拉伸时，保持不变距离。单位vp。 |
| .value[1].f32 | 图片上部拉伸时，保持不变距离。单位vp。 |
| .value[2].f32 | 图片右部拉伸时，保持不变距离。单位vp。 |
| .value[3].f32 | 图片下部拉伸时，保持不变距离。单位vp。与NODE\_IMAGE\_ANTIALIASED一起使用时，NODE\_IMAGE\_ANTIALIASED属性设置不生效。 |
| .object | 参数类型为[OH\_Drawing\_Lattice](capi-drawing-oh-drawing-lattice.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 图片左部拉伸时，保持不变距离。单位vp。 |
| .value[1].f32 | 图片上部拉伸时，保持不变距离。单位vp。 |
| .value[2].f32 | 图片右部拉伸时，保持不变距离。单位vp。 |
| .value[3].f32 | 图片下部拉伸时，保持不变距离。单位vp。 |
| .object | 参数类型为[OH\_Drawing\_Lattice](capi-drawing-oh-drawing-lattice.md)。 |

## NODE\_IMAGE\_SYNC\_LOAD

```
1. NODE_IMAGE_SYNC_LOAD = 4012
```

图源同步加载属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示是否同步，默认值：false。false表示异步加载图片，true表示同步加载图片。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示是否同步。 |

## NODE\_IMAGE\_SOURCE\_SIZE

```
1. NODE_IMAGE_SOURCE_SIZE = 4013
```

设置图片解码尺寸，仅在目标尺寸小于图源尺寸时生效。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示图片解码的宽，单位px。 |
| .value[1].i32 | 表示图片解码的高，单位px。当任意参数小于等于0时，属性设置失败并返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode)函数参数异常。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示图片解码的宽，单位px。 |
| .value[1].i32 | 表示图片解码的高，单位px。 |

## NODE\_IMAGE\_IMAGE\_MATRIX

```
1. NODE_IMAGE_IMAGE_MATRIX = 4014
```

设置图片的变换矩阵属性。支持属性设置，属性重置和属性获取接口。支持使用浮点数或矩阵对象实现仿射图像变换。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0...15].f32 | 4x4矩阵通过长度为16的浮点数数组来表示。当参数个数小于16，属性设置失败并返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode)函数参数异常；当参数个数大于16，只取前16个数据。 |
| .object | 参数类型为ArkUI\_Matrix4。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0...15].f32 | 4x4矩阵通过长度为16的浮点数数组来表示。 |
| .object | 参数类型为ArkUI\_Matrix4。 |

## NODE\_IMAGE\_MATCH\_TEXT\_DIRECTION

```
1. NODE_IMAGE_MATCH_TEXT_DIRECTION = 4015
```

设置图片是否跟随系统语言方向，在RTL语言环境下显示镜像翻转显示效果。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 图片是否跟随系统语言方向，默认值为false。false表示图片不跟随系统语言方向，true表示图片跟随系统语言方向。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 图片是否跟随系统语言方向。false表示图片不跟随系统语言方向，true表示图片跟随系统语言方向。 |

## NODE\_IMAGE\_COPY\_OPTION

```
1. NODE_IMAGE_COPY_OPTION = 4016
```

设置图片的拷贝方式。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 支持图片拷贝的方式[ArkUI\_CopyOptions](capi-native-type-h.md#arkui_copyoptions)，默认值为ARKUI\_COPY\_OPTIONS\_NONE。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 支持图片拷贝的方式[ArkUI\_CopyOptions](capi-native-type-h.md#arkui_copyoptions)。 |

## NODE\_IMAGE\_ENABLE\_ANALYZER

```
1. NODE_IMAGE_ENABLE_ANALYZER = 4017
```

设置组件支持AI分析，当前支持主体识别、文字识别和对象查找等功能。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否为图片开启AI分析，默认值为false。false表示组件不支持AI分析，true表示组件支持AI分析。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否为图片开启AI分析。false表示组件不支持AI分析，true表示组件支持AI分析。 |

## NODE\_IMAGE\_DYNAMIC\_RANGE\_MODE

```
1. NODE_IMAGE_DYNAMIC_RANGE_MODE = 4018
```

定义图片显示动态范围属性，指定图像渲染的动态范围模式（例如：SDR/HDR）。支持设置、重置和获取接口，用于匹配显示设备能力，确保图像明暗与色彩的准确呈现。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 动态范围类型[ArkUI\_DynamicRangeMode](capi-native-type-h.md#arkui_dynamicrangemode)，默认值为ARKUI\_DYNAMIC\_RANGE\_MODE\_STANDARD。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 动态范围类型[ArkUI\_DynamicRangeMode](capi-native-type-h.md#arkui_dynamicrangemode)。 |

## NODE\_IMAGE\_HDR\_BRIGHTNESS

```
1. NODE_IMAGE_HDR_BRIGHTNESS = 4019
```

定义图片HDR模式下的亮度属性，用于控制高动态范围显示的亮度参数。支持设置、重置和获取接口，确保HDR图像亮部与暗部细节的精准呈现。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 可设置的亮度值，取值范围[0, 1]。小于0和大于1.0时取1。0表示图片按照SDR亮度显示，1表示图片按照当前允许的最高HDR亮度显示。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 可设置的亮度值，取值范围[0, 1]。 |

## NODE\_IMAGE\_ORIENTATION

```
1. NODE_IMAGE_ORIENTATION = 4020
```

设置图像内容的显示方向。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 期望的图像内容显示方向[ArkUI\_Orientation](capi-native-type-h.md#arkui_imagerotateorientation)，默认值为ARKUI\_ORIENTATION\_UP。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 期望的图像内容显示方向[ArkUI\_Orientation](capi-native-type-h.md#arkui_imagerotateorientation)。 |

## NODE\_IMAGE\_SUPPORT\_SVG2

```
1. NODE_IMAGE_SUPPORT_SVG2 = 4021
```

通过启用SVG新解析能力开关设置SVG解析功能支持的范围，支持属性设置，属性重置，属性获取接口。Image组件创建后，不支持动态修改该属性的值。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否启用SVG新解析能力开关。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否启用SVG新解析能力开关。 |

## NODE\_IMAGE\_CONTENT\_TRANSITION

```
1. NODE_IMAGE_CONTENT_TRANSITION = 4022
```

设置图像变化时的转场动效，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 自定义转场动效，参数类型[ArkUI\_ContentTransitionEffect](i-arkui-nativemodule-arkui-contenttransitioneffect.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 自定义转场动效，参数类型[ArkUI\_ContentTransitionEffect](i-arkui-nativemodule-arkui-contenttransitioneffect.md)。 |

## NODE\_IMAGE\_ALT\_PLACEHOLDER

```
1. NODE_IMAGE_ALT_PLACEHOLDER  = 4023
```

支持加载过程中的占位图的配置，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 表示image组件加载过程中的占位图地址。 |
| .object | 表示PixelMap图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)；  .object参数和.string参数二选一，不可同时设置，不支持网络图片。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 表示image组件加载过程中的占位图地址。 |
| .object | 表示PixelMap图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)。 |

## NODE\_IMAGE\_ALT\_ERROR

```
1. NODE_IMAGE_ALT_ERROR  = 4024
```

支持加载失败时的占位图的配置，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 表示image组件加载失败时的占位图地址。 |
| .object | 表示PixelMap图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)；  .object参数和.string参数二选一，不可同时设置，不支持网络图片。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 表示image组件加载失败时的占位图地址。 |
| .object | 表示PixelMap图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)。 |

## NODE\_IMAGE\_ANTIALIASED

```
1. NODE_IMAGE_ANTIALIASED = 4025
```

支持设置位图图片边缘抗锯齿的配置，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示是否开启位图图片边缘抗锯齿，默认值：false。false表示不开启抗锯齿，true表示开启抗锯齿。与NODE\_IMAGE\_RESIZABLE一起使用时，该属性不生效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示是否开启位图图片边缘抗锯齿。false表示不开启抗锯齿，true表示开启抗锯齿。 |

## NODE\_IMAGE\_ANIMATOR\_IMAGES

```
1. NODE_IMAGE_ANIMATOR_IMAGES = ARKUI_NODE_IMAGE_ANIMATOR * MAX_NODE_SCOPE_NUM = 19000
```

设置帧动画组件的图片帧信息集合。不支持动态更新。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .size | 图片帧的数量。 |
| .object | 图片帧数组，参数类型为[ArkUI\_ImageAnimatorFrameInfo](pi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)数组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .size | 图片帧的数量。 |
| .object | 图片帧数组，参数类型为[ArkUI\_ImageAnimatorFrameInfo](pi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)数组。 |

## NODE\_IMAGE\_ANIMATOR\_STATE

```
1. NODE_IMAGE_ANIMATOR_STATE = 19001
```

控制帧动画组件的播放状态。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 控制动画的播放状态，参数类型为[ArkUI\_AnimationStatus](capi-native-type-h.md#arkui_animationstatus)，默认值为初始状态。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 控制动画的播放状态，参数类型为[ArkUI\_AnimationStatus](capi-native-type-h.md#arkui_animationstatus)。 |

## NODE\_IMAGE\_ANIMATOR\_DURATION

```
1. NODE_IMAGE_ANIMATOR_DURATION = 19002
```

设置帧动画的播放时长，当数组中任意一帧图片单独设置了duration属性后，该属性设置无效。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 播放时长，单位为毫秒，默认值1000。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 播放时长，单位为毫秒，默认值1000。 |

## NODE\_IMAGE\_ANIMATOR\_REVERSE

```
1. NODE_IMAGE_ANIMATOR_REVERSE = 19003
```

设置帧动画的播放方向。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 播放方向，0表示从第一张图片播放到最后一张，1表示从最后一张图片播放到第一张，默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 播放方向，0表示从第一张图片播放到最后一张，1表示从最后一张图片播放到第一张。 |

## NODE\_IMAGE\_ANIMATOR\_FIXED\_SIZE

```
1. NODE_IMAGE_ANIMATOR_FIXED_SIZE = 19004
```

设置图片大小是否固定为组件大小。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置图片大小是否固定为组件大小，1表示图片大小与组件大小一致。0表示每一张图片的width、height、top和left都要单独设置，默认值为1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 设置图片大小是否固定为组件大小，1表示图片大小与组件大小一致。0表示每一张图片的width、height、top和left都要单独设置。 |

## NODE\_IMAGE\_ANIMATOR\_FILL\_MODE

```
1. NODE_IMAGE_ANIMATOR_FILL_MODE = 19005
```

设置帧动画在当前播放方向下，动画开始前和结束后的状态。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 当前播放方向下，动画开始前和结束后的状态，参数类型为[ArkUI\_AnimationFillMode](capi-native-type-h.md#arkui_animationfillmode)，默认值为ARKUI\_ANIMATION\_FILL\_MODE\_FORWARDS。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 当前播放方向下，动画开始前和结束后的状态，参数类型为[ArkUI\_AnimationFillMode](capi-native-type-h.md#arkui_animationfillmode)。 |

## NODE\_IMAGE\_ANIMATOR\_ITERATION

```
1. NODE_IMAGE_ANIMATOR_ITERATION = 19006
```

设置帧动画的播放次数。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 播放次数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 播放次数。 |
