---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-animator
title: ArkUI_NodeAttributeType（动效、视效相关属性）
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_node.h > ArkUI_NodeAttributeType（动效、视效相关属性）
category: harmonyos-references
scraped_at: 2026-04-29T13:54:13+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:36f3e50a0f7573538e7e8fd2d86bbeb8d2f17ffc17e24be7bbdc0c413b4f9501
---

```
1. enum ArkUI_NodeAttributeType
```

## 概述

定义ArkUI在Native侧可以设置的动效、视效相关属性样式集合，包含图形变换、渐变、阴影、模糊和转场等属性设置。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)

## NODE\_TRANSLATE

```
1. NODE_TRANSLATE = 8
```

设置组件平移，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | x轴移动距离，单位vp，默认值0。 |
| .value[1].f32 | y轴移动距离，单位vp，默认值0。 |
| .value[2].f32 | z轴移动距离，单位vp，默认值0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | x轴移动距离，单位vp。 |
| .value[1].f32 | y轴移动距离，单位vp。 |
| .value[2].f32 | z轴移动距离，单位vp。 |

## NODE\_SCALE

```
1. NODE_SCALE = 9
```

设置组件缩放，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | x轴的缩放系数，默认值1。 |
| .value[1].f32 | y轴的缩放系数，默认值1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | x轴的缩放系数。 |
| .value[1].f32 | y轴的缩放系数。 |

## NODE\_ROTATE

```
1. NODE_ROTATE = 10
```

设置组件旋转，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 旋转轴向量x坐标，默认值0。 |
| .value[1].f32 | 旋转轴向量y坐标，默认值0。 |
| .value[2].f32 | 旋转轴向量z坐标，默认值0。 |
| .value[3].f32 | 旋转角度，默认值0。 |
| .value[4].f32 | 视距，即视点到z=0平面的距离，单位vp，默认值0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 旋转轴向量x坐标。 |
| .value[1].f32 | 旋转轴向量y坐标。 |
| .value[2].f32 | 旋转轴向量z坐标。 |
| .value[3].f32 | 旋转角度。 |
| .value[4].f32 | 视距，即视点到z=0平面的距离，单位vp。 |

## NODE\_BRIGHTNESS

```
1. NODE_BRIGHTNESS = 11
```

设置组件高光效果，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 亮度值，默认值1.0，推荐取值范围[0, 2.0]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 亮度值。 |

## NODE\_SATURATION

```
1. NODE_SATURATION = 12
```

设置组件饱和度效果，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 饱和度值，默认值1.0，推荐取值范围[0, 50.0)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 饱和度值。 |

## NODE\_BLUR

```
1. NODE_BLUR = 13
```

设置组件内容模糊效果，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 模糊半径，模糊半径越大越模糊，为0时不模糊，小于0时按0处理且不会返回错误码。单位vp，默认值0.0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 模糊半径，模糊半径越大越模糊，为0时不模糊。单位vp。 |

## NODE\_LINEAR\_GRADIENT

```
1. NODE_LINEAR_GRADIENT = 14
```

设置组件颜色渐变效果，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 线性渐变的起始角度，当[ArkUI\_LinearGradientDirection](capi-native-type-h.md#arkui_lineargradientdirection)为ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM时，angle属性生效，否则按direction为主要布局方式。0点方向顺时针旋转为正向角度，默认值：180。 |
| .value[1].i32 | 线性渐变的方向，设置除ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM的线性渐变方向后，angle不生效。数据类型[ArkUI\_LinearGradientDirection](capi-native-type-h.md#arkui_lineargradientdirection)。 |
| .value[2].i32 | 为渐变的颜色重复着色，默认值 false。 |
| .object | 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过： |
| colors | 渐变色颜色。 |
| stops | 渐变位置。 |
| size | 颜色个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 线性渐变的起始角度。当为ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM时，angle为设置值，其他情况均为默认值。 |
| .value[1].i32 | 线性渐变的方向。 |
| .value[2].i32 | 为渐变的颜色重复着色。 |
| .object | 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过： |
| colors | 渐变色颜色。 |
| stops | 渐变位置。 |
| size | 颜色个数。 |

## NODE\_OPACITY

```
1. NODE_OPACITY = 16
```

透明度属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 透明度数值，默认值为1，取值范围为0到1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 透明度数值，取值范围为0到1。 |

## NODE\_Z\_INDEX

```
1. NODE_Z_INDEX = 21
```

组件的堆叠顺序属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 堆叠顺序数值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 堆叠顺序数值。 |

## NODE\_VISIBILITY

```
1. NODE_VISIBILITY = 22
```

组件是否可见属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 控制当前组件显示或隐藏，参数类型[ArkUI\_Visibility](capi-native-type-h.md#arkui_visibility)，默认值为ARKUI\_VISIBILITY\_VISIBLE。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 控制当前组件显示或隐藏，参数类型[ArkUI\_Visibility](capi-native-type-h.md#arkui_visibility)，默认值为ARKUI\_VISIBILITY\_VISIBLE。 |

## NODE\_CLIP

```
1. NODE_CLIP = 23
```

组件进行裁剪、遮罩处理属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 控制是否对子组件超出当前组件范围外的区域进行裁剪，0表示不裁切，1表示裁切。默认为不裁切。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 控制是否对子组件超出当前组件范围外的区域进行裁剪，0表示不裁切，1表示裁切。 |

## NODE\_CLIP\_SHAPE

```
1. NODE_CLIP_SHAPE = 24
```

组件上指定形状的裁剪，支持属性设置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

1.rect类型：

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 裁剪类型，参数类型ArkUI\_ClipType，ARKUI\_CLIP\_TYPE\_RECTANGLE。 |
| .value[1].f32 | 矩形宽度，单位为vp。 |
| .value[2].f32 | 矩形高度，单位为vp。 |
| .value[3].f32 | 矩形圆角宽度，单位为vp。 |
| .value[4].f32 | 矩形圆角高度，单位为vp。 |
| .value[5]?.f32 | 矩形形状的左上圆角半径，单位为vp。 |
| .value[6]?.f32 | 矩形形状的左下圆角半径，单位为vp。 |
| .value[7]?.f32 | 矩形形状的右上圆角半径，单位为vp。 |
| .value[8]?.f32 | 矩形形状的右下圆角半径，单位为vp。 |
| .object | 参数类型为ArkUI\_RenderNodeClipOption，矩形形状的坐标偏移量，在仅传入.object参数时生效。 |

2.circle类型：

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 裁剪类型，参数类型ArkUI\_ClipType，ARKUI\_CLIP\_TYPE\_CIRCLE。 |
| .value[1].f32 | 圆形宽度，单位为vp。 |
| .value[2].f32 | 圆形高度，单位为vp。 |
| .object | 参数类型为ArkUI\_RenderNodeClipOption，圆形坐标偏移量，在仅传入.object参数时生效。 |

3.ellipse类型：

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 裁剪类型，参数类型ArkUI\_ClipType，ARKUI\_CLIP\_TYPE\_ELLIPSE。 |
| .value[1].f32 | 椭圆形宽度，单位为vp。 |
| .value[2].f32 | 椭圆形高度，单位为vp。 |
| .object | 参数类型为ArkUI\_RenderNodeClipOption，椭圆形坐标偏移量，在仅传入.object参数时生效。 |

4.path类型：

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 裁剪类型，参数类型ArkUI\_ClipType，ARKUI\_CLIP\_TYPE\_PATH。 |
| .value[1].f32 | 路径宽度，单位为vp。 |
| .value[2].f32 | 路径高度，单位为vp。 |
| .string | 路径绘制的命令字符串。 |
| .object | 参数类型为ArkUI\_RenderNodeClipOption，路径绘制的命令，在仅传入.object参数时生效。 |

**返回：**

1.rect类型：

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 裁剪类型，参数类型ArkUI\_ClipType，ARKUI\_CLIP\_TYPE\_RECTANGLE。 |
| .value[1].f32 | 矩形宽度，单位为vp。 |
| .value[2].f32 | 矩形高度，单位为vp。 |
| .value[3].f32 | 矩形圆角宽度，单位为vp。 |
| .value[4].f32 | 矩形圆角高度，单位为vp。 |
| .value[5]?.f32 | 矩形形状的左上圆角半径，单位为vp。 |
| .value[6]?.f32 | 矩形形状的左下圆角半径，单位为vp。 |
| .value[7]?.f32 | 矩形形状的右上圆角半径，单位为vp。 |
| .value[8]?.f32 | 矩形形状的右下圆角半径，单位为vp。 |
| .value[9]?.f32 | 矩形形状的横坐标偏移，单位为vp。 |
| .value[10]?.f32 | 矩形形状的纵坐标偏移，单位为vp。 |

2.circle类型：

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 裁剪类型，参数类型ArkUI\_ClipType，ARKUI\_CLIP\_TYPE\_CIRCLE。 |
| .value[1].f32 | 圆形宽度，单位为vp。 |
| .value[2].f32 | 圆形高度，单位为vp。 |
| .value[3]?.f32 | 圆形横坐标偏移，单位为vp。 |
| .value[4]?.f32 | 圆形纵坐标偏移，单位为vp。 |

3.ellipse类型：

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 裁剪类型，参数类型ArkUI\_ClipType，ARKUI\_CLIP\_TYPE\_ELLIPSE。 |
| .value[1].f32 | 椭圆形宽度，单位为vp。 |
| .value[2].f32 | 椭圆形高度，单位为vp。 |
| .value[3]?.f32 | 椭圆形横坐标偏移，单位为vp。 |
| .value[4]?.f32 | 椭圆形纵坐标偏移，单位为vp。 |

4.path类型：

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 裁剪类型，参数类型ArkUI\_ClipType，ARKUI\_CLIP\_TYPE\_PATH。 |
| .value[1].f32 | 路径宽度，单位为vp。 |
| .value[2].f32 | 路径高度，单位为vp。 |
| .string | 路径绘制的命令字符串。 |

## NODE\_TRANSFORM

```
1. NODE_TRANSFORM = 25
```

矩阵变换功能，可对图形进行平移、旋转和缩放等，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0...15].f32 | 16个浮点数。此时[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)中的size取值不应为0。 |
| .object | 是指向ArkUI\_Matrix4的指针，此时[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)中的size取值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0...15].f32 | 16个浮点数字。 |

## NODE\_SHADOW

```
1. NODE_SHADOW = 28
```

阴影效果属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置当前组件阴影效果，参数类型[ArkUI\_ShadowStyle](capi-native-type-h.md#arkui_shadowstyle)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 设置当前组件阴影效果，参数类型[ArkUI\_ShadowStyle](capi-native-type-h.md#arkui_shadowstyle)。 |

## NODE\_CUSTOM\_SHADOW

```
1. NODE_CUSTOM_SHADOW = 29
```

自定义阴影效果，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0]?.f32 | 阴影模糊半径，单位为px。 |
| .value[1]?.i32 | 是否开启智能取色，0代表不开启，1代表开启，默认不开启。 |
| .value[2]?.f32 | 阴影X轴偏移量，单位为px。 |
| .value[3]?.f32 | 阴影Y轴偏移量，单位为px。 |
| .value[4]?.i32 | 阴影类型[ArkUI\_ShadowType](capi-native-type-h.md#arkui_shadowtype)，默认值为ARKUI\_SHADOW\_TYPE\_COLOR。 |
| .value[5]?.u32 | 阴影颜色，0xargb格式，形如 0xFFFF0000 表示红色。 |
| .value[6]?.u32 | 阴影是否内部填充，0表示不填充，1表示填充。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 阴影模糊半径，单位为px。 |
| .value[1].i32 | 是否开启智能取色。 |
| .value[2].f32 | 阴影X轴偏移量，单位为px。 |
| .value[3].f32 | 阴影Y轴偏移量，单位为px。 |
| .value[4].i32 | 阴影类型[ArkUI\_ShadowType](capi-native-type-h.md#arkui_shadowtype)，默认值为ARKUI\_SHADOW\_TYPE\_COLOR。 |
| .value[5].u32 | 阴影颜色，0xargb格式，形如 0xFFFF0000 表示红色。 |
| .value[6].u32 | 阴影是否内部填充，0表示不填充，1表示填充。 |

## NODE\_BACKGROUND\_BLUR\_STYLE

```
1. NODE_BACKGROUND_BLUR_STYLE = 32
```

背景和内容之间的模糊属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示模糊类型，取[ArkUI\_BlurStyle](capi-native-type-h.md#arkui_blurstyle)枚举值。 |
| .value[1]?.i32 | 表示深浅色模式，取[ArkUI\_ColorMode](capi-native-type-h.md#arkui_colormode)枚举值。 |
| .value[2]?.i32 | 表示取色模式，取[ArkUI\_AdaptiveColor](capi-native-type-h.md#arkui_adaptivecolor)枚举值。 |
| .value[3]?.f32 | 表示模糊效果程度，取[0.0,1.0]范围内的值。 |
| .value[4]?.f32 | 表示灰阶模糊起始边界。 |
| .value[5]?.f32 | 表示灰阶模糊终点边界。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示模糊类型，取[ArkUI\_BlurStyle](capi-native-type-h.md#arkui_blurstyle)枚举值。 |
| .value[1].i32 | 表示深浅色模式，取[ArkUI\_ColorMode](capi-native-type-h.md#arkui_colormode)枚举值。 |
| .value[2].i32 | 表示取色模式，取[ArkUI\_AdaptiveColor](capi-native-type-h.md#arkui_adaptivecolor)枚举值。 |
| .value[3].f32 | 表示模糊效果程度，取[0.0,1.0]范围内的值。 |
| .value[4].f32 | 表示灰阶模糊起始边界。 |
| .value[5].f32 | 表示灰阶模糊终点边界。 |

## NODE\_TRANSFORM\_CENTER

```
1. NODE_TRANSFORM_CENTER = 33
```

图形变换和转场的中心点属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

注：如果设置坐标百分比位置，属性获取方法返回计算后的以vp为单位的值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0]?.f32 | 表示中心点X轴坐标值，单位为vp。 |
| .value[1]?.f32 | 表示中心点Y轴坐标，单位为vp。 |
| .value[2]?.f32 | 表示中心点Z轴坐标，单位为vp。 |
| .value[3]?.f32 | 表示中心点X轴坐标的百分比位置，如0.2表示百分之20的位置，该属性覆盖value[0].f32，默认值:0.5f。 |
| .value[4]?.f32 | 表示中心点Y轴坐标的百分比位置，如0.2表示百分之20的位置，该属性覆盖value[1].f32，默认值:0.5f。 |
| .value[5]?.f32 | 表示中心点Z轴坐标的百分比位置，如0.2表示百分之20的位置，该属性覆盖value[2].f32，默认值:0.0f。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 表示中心点X轴坐标，单位为vp。 |
| .value[1].f32 | 表示中心点Y轴坐标，单位为vp。 |
| .value[2].f32 | 表示中心点Z轴坐标，单位为vp。 |

## NODE\_MOTION\_PATH

```
1. NODE_MOTION_PATH = 111
```

设置组件的运动路径属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 指向路径动画的运动路径配置项的指针；参数类型为[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 指向路径动画的运动路径配置项的指针；参数类型为[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)。 |

## NODE\_OPACITY\_TRANSITION

```
1. NODE_OPACITY_TRANSITION = 34
```

转场时的透明度效果属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 表示起终点的透明度值。 |
| .value[1].i32 | 表示动画时长，单位ms。 |
| .value[2].i32 | 表示动画曲线类型，取[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)枚举值。 |
| .value[3]?.i32 | 表示动画延迟时长，单位ms。 |
| .value[4]?.i32 | 表示动画播放次数。 |
| .value[5]?.i32 | 表示动画播放模式，取[ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode)枚举值。 |
| .value[6]?.f32 | 表示动画播放速度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 表示起终点的透明度值。 |
| .value[1].i32 | 表示动画时长，单位ms。 |
| .value[2].i32 | 表示动画曲线类型，取[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)枚举值。 |
| .value[3].i32 | 表示动画延迟时长，单位ms。 |
| .value[4].i32 | 表示动画播放次数。 |
| .value[5].i32 | 表示动画播放模式，取[ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode)枚举值。 |
| .value[6].f32 | 表示动画播放速度。 |

## NODE\_ROTATE\_TRANSITION

```
1. NODE_ROTATE_TRANSITION = 35
```

转场时的旋转效果属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 表示横向旋转分量。 |
| .value[1].f32 | 表示纵向的旋转分量。 |
| .value[2].f32 | 表示竖向的旋转分量。 |
| .value[3].f32 | 表示角度。 |
| .value[4].f32 | 表示视距，默认值：0.0f。 |
| .value[5].i32 | 表示动画时长，单位ms。 |
| .value[6].i32 | 表示动画曲线类型，取[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)枚举值。 |
| .value[7]?.i32 | 表示动画延迟时长，单位ms。 |
| .value[8]?.i32 | 表示动画播放次数。 |
| .value[9]?.i32 | 表示动画播放模式，取[ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode)枚举值。 |
| .value[10]?.f32 | 表示动画播放速度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 表示横向旋转分量。 |
| .value[1].f32 | 表示纵向的旋转分量。 |
| .value[2].f32 | 表示竖向的旋转分量。 |
| .value[3].f32 | 表示角度。 |
| .value[4].f32 | 表示视距。 |
| .value[5].i32 | 表示动画时长，单位ms。 |
| .value[6].i32 | 表示动画曲线类型，取[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)枚举值。 |
| .value[7].i32 | 表示动画延迟时长，单位ms。 |
| .value[8].i32 | 表示动画播放次数。 |
| .value[9].i32 | 表示动画播放模式，取[ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode)枚举值。 |
| .value[10].f32 | 表示动画播放速度。 |

## NODE\_SCALE\_TRANSITION

```
1. NODE_SCALE_TRANSITION = 36
```

转场时的缩放效果属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 横向放大倍数。 |
| .value[1].f32 | 纵向放大倍数。 |
| .value[2].f32 | 竖向放大倍数。 |
| .value[3].i32 | 表示动画时长，单位ms。 |
| .value[4].i32 | 表示动画曲线类型，取[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)枚举值。 |
| .value[5]?.i32 | 表示动画延迟时长，单位ms。 |
| .value[6]?.i32 | 表示动画播放次数。 |
| .value[7]?.i32 | 表示动画播放模式，取[ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode)枚举值。 |
| .value[8]?.f32 | 表示动画播放速度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 横向放大倍数。 |
| .value[1].f32 | 纵向放大倍数。 |
| .value[2].f32 | 竖向放大倍数。 |
| .value[3].i32 | 表示动画时长，单位ms。 |
| .value[4].i32 | 表示动画曲线类型，取[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)枚举值。 |
| .value[5].i32 | 表示动画延迟时长，单位ms。 |
| .value[6].i32 | 表示动画播放次数。 |
| .value[7].i32 | 表示动画播放模式，取[ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode)枚举值。 |
| .value[8].f32 | 表示动画播放速度。 |

## NODE\_TRANSLATE\_TRANSITION

```
1. NODE_TRANSLATE_TRANSITION = 37
```

转场时的平移效果属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 表示横向平移距离值，单位为vp。默认值为0.0vp。 |
| .value[1].f32 | 表示纵向平移距离值，单位为vp。默认值为0.0vp。 |
| .value[2].f32 | 表示竖向平移距离值，单位为vp。默认值为0.0vp。 |
| .value[3].i32 | 表示动画时长，单位ms。 |
| .value[4].i32 | 表示动画曲线类型，取[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)枚举值。 |
| .value[5]?.i32 | 表示动画延迟时长，单位ms。 |
| .value[6]?.i32 | 表示动画播放次数。 |
| .value[7]?.i32 | 表示动画播放模式，取[ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode)枚举值。 |
| .value[8]?.f32 | 表示动画播放速度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 表示横向平移距离值，单位为vp。 |
| .value[1].f32 | 表示纵向平移距离值，单位为vp。 |
| .value[2].f32 | 表示竖向平移距离值，单位为vp。 |
| .value[3].i32 | 表示动画时长，单位ms。 |
| .value[4].i32 | 表示动画曲线类型，取[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)枚举值。 |
| .value[5].i32 | 表示动画延迟时长，单位ms。 |
| .value[6].i32 | 表示动画播放次数。 |
| .value[7].i32 | 表示动画播放模式，取[ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode)枚举值。 |
| .value[8].f32 | 表示动画播放速度。 |

## NODE\_MOVE\_TRANSITION

```
1. NODE_MOVE_TRANSITION = 38
```

转场时从屏幕边缘滑入和滑出的效果属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_TransitionEdge](capi-native-type-h.md#arkui_transitionedge)。 |
| .value[1].i32 | 表示动画时长，单位ms。 |
| .value[2].i32 | 表示动画曲线类型，取[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)枚举值。 |
| .value[3]?.i32 | 表示动画延迟时长，单位ms。 |
| .value[4]?.i32 | 表示动画播放次数。 |
| .value[5]?.i32 | 表示动画播放模式，取[ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode)枚举值。 |
| .value[6]?.f32 | 表示动画播放速度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_TransitionEdge](capi-native-type-h.md#arkui_transitionedge)。 |
| .value[1].i32 | 表示动画时长，单位ms。 |
| .value[2].i32 | 表示动画曲线类型，取[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)枚举值。 |
| .value[3].i32 | 表示动画延迟时长，单位ms。 |
| .value[4].i32 | 表示动画播放次数。 |
| .value[5].i32 | 表示动画播放模式，取[ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode)枚举值。 |
| .value[6].f32 | 表示动画播放速度。 |

## NODE\_SWEEP\_GRADIENT

```
1. NODE_SWEEP_GRADIENT = 43
```

角度渐变效果，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0]?.f32 | 为角度渐变的中心点，即相对于当前组件左上角的坐标,X轴坐标。 |
| .value[1]?.f32 | 为角度渐变的中心点，即相对于当前组件左上角的坐标,Y轴坐标。 |
| .value[2]?.f32 | 角度渐变的起点，默认值0。 |
| .value[3]?.f32 | 角度渐变的终点，默认值0。 |
| .value[4]?.f32 | 角度渐变的旋转角度，默认值0。 |
| .value[5]?.i32 | 为渐变的颜色重复着色，0表示不重复着色，1表示重复着色。 |
| .object | 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过： |
| colors | 渐变色颜色。 |
| stops | 渐变位置。 |
| size | 颜色个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 为角度渐变的中心点，即相对于当前组件左上角的坐标,X轴坐标。 |
| .value[1].f32 | 为角度渐变的中心点，即相对于当前组件左上角的坐标,Y轴坐标。 |
| .value[2].f32 | 角度渐变的起点，默认值0。 |
| .value[3].f32 | 角度渐变的终点，默认值0。 |
| .value[4].f32 | 角度渐变的旋转角度，默认值0。 |
| .value[5].i32 | 为渐变的颜色重复着色，0表示不重复着色，1表示重复着色。 |
| .object | 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过： |
| colors | 渐变色颜色。 |
| stops | 渐变位置。 |
| size | 颜色个数。 |

## NODE\_RADIAL\_GRADIENT

```
1. NODE_RADIAL_GRADIENT = 44
```

径向渐变渐变效果，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0]?.f32 | 为径向渐变的中心点，即相对于当前组件左上角的坐标,X轴坐标。 |
| .value[1]?.f32 | 为径向渐变的中心点，即相对于当前组件左上角的坐标,Y轴坐标。 |
| .value[2]?.f32 | 径向渐变的半径，默认值0。 |
| .value[3]?.i32 | 为渐变的颜色重复着色，0表示不重复着色，1表示重复着色。 |
| .object | 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过： |
| colors | 渐变色颜色。 |
| stops | 渐变位置。 |
| size | 颜色个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 为径向渐变的中心点，即相对于当前组件左上角的坐标,X轴坐标。 |
| .value[1].f32 | 为径向渐变的中心点，即相对于当前组件左上角的坐标,Y轴坐标。 |
| .value[2].f32 | 径向渐变的半径，默认值0。 |
| .value[3].i32 | 为渐变的颜色重复着色，0表示不重复着色，1表示重复着色。 |
| .object | 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过： |
| colors | 渐变色颜色。 |
| stops | 渐变位置。 |
| size | 颜色个数。 |

## NODE\_MASK

```
1. NODE_MASK = 45
```

组件上加上指定形状的遮罩，支持属性设置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| 1.rect类型 | .value[0].u32：填充颜色，0xargb类型；  .value[1].u32：描边颜色，0xargb类型；  .value[2].f32：描边宽度，单位为vp；  .value[3].i32：遮罩类型，参数类型[ArkUI\_MaskType](capi-native-type-h.md#arkui_masktype)，遮罩类型枚举值为ARKUI\_MASK\_TYPE\_RECTANGLE；  .value[4].f32：矩形宽度，单位为vp；  .value[5].f32：矩形高度，单位为vp；  .value[6].f32：矩形圆角宽度，单位为vp；  .value[7].f32：矩形圆角高度，单位为vp；  .value[8]?.f32：矩形形状的左上圆角半径，单位为vp；  .value[9]?.f32：矩形形状的左下圆角半径，单位为vp；  .value[10]?.f32：矩形形状的右上圆角半径，单位为vp；  .value[11]?.f32：矩形形状的右下圆角半径，单位为vp。 |
| 2.circle类型 | .value[0].u32：填充颜色，0xargb类型；  .value[1].u32：描边颜色，0xargb类型；  .value[2].f32：描边宽度，单位为vp；  .value[3].i32：遮罩类型，参数类型[ArkUI\_MaskType](capi-native-type-h.md#arkui_masktype)，遮罩类型枚举值为ARKUI\_MASK\_TYPE\_CIRCLE；  .value[4].f32：圆形宽度，单位为vp；  .value[5].f32：圆形高度，单位为vp。 |
| 3.ellipse类型 | .value[0].u32：填充颜色，0xargb类型；  .value[1].u32：描边颜色，0xargb类型；  .value[2].f32：描边宽度，单位为vp；  .value[3].i32：遮罩类型，参数类型[ArkUI\_MaskType](capi-native-type-h.md#arkui_masktype)，遮罩类型枚举值为ARKUI\_MASK\_TYPE\_ELLIPSE；  .value[4].f32：椭圆形宽度，单位为vp；  .value[5].f32：椭圆形高度，单位为vp。 |
| 4.path类型 | .value[0].u32：填充颜色，0xargb类型；  .value[1].u32：描边颜色，0xargb类型；  .value[2].f32：描边宽度，单位为vp；  .value[3].i32：遮罩类型，参数类型[ArkUI\_MaskType](capi-native-type-h.md#arkui_masktype)，遮罩类型枚举值为ARKUI\_MASK\_TYPE\_PATH；  .value[4].f32：路径宽度，单位为vp；  .value[5].f32：路径高度，单位为vp；  .string：路径绘制的命令字符串。 |
| 5.progress类型 | .value[0].i32：遮罩类型，参数类型[ArkUI\_MaskType](capi-native-type-h.md#arkui_masktype)，遮罩类型枚举值为ARKUI\_MASK\_TYPE\_PROGRESS；  .value[1].f32：进度遮罩的当前值；  .value[2].f32：进度遮罩的最大值；  .value[3].u32：进度遮罩的颜色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| 1.rect类型 | .value[0].u32：填充颜色，0xargb类型；  .value[1].u32：描边颜色，0xargb类型；  .value[2].f32：描边宽度，单位为vp；  .value[3].i32：遮罩类型；  .value[4].f32：矩形宽度，单位为vp；  .value[5].f32：矩形高度，单位为vp；  .value[6].f32：矩形圆角宽度，单位为vp；  .value[7].f32：矩形圆角高度，单位为vp；  .value[8]?.f32：矩形形状的左上圆角半径，单位为vp；  .value[9]?.f32：矩形形状的左下圆角半径，单位为vp；  .value[10]?.f32：矩形形状的右上圆角半径，单位为vp；  .value[11]?.f32：矩形形状的右下圆角半径，单位为vp。 |
| 2.circle类型 | .value[0].u32：填充颜色，0xargb类型；  .value[1].u32：描边颜色，0xargb类型；  .value[2].f32：描边宽度，单位为vp；  .value[3].i32：遮罩类型；  .value[4].f32：圆形宽度，单位为vp；  .value[5].f32：圆形高度，单位为vp。 |
| 3.ellipse类型 | .value[0].u32：填充颜色，0xargb类型；  .value[1].u32：描边颜色，0xargb类型；  .value[2].f32：描边宽度，单位为vp；  .value[3].i32：遮罩类型；  .value[4].f32：椭圆形宽度，单位为vp；  .value[5].f32：椭圆形高度，单位为vp。 |
| 4.path类型 | .value[0].u32：填充颜色，0xargb类型；  .value[1].u32：描边颜色，0xargb类型；  .value[2].f32：描边宽度，单位为vp；  .value[3].i32：遮罩类型；  .value[4].f32：路径宽度，单位为vp；  .value[5].f32：路径高度，单位为vp；  .string：路径绘制的命令字符串。 |
| 5.progress类型 | .value[0].i32：遮罩类型；  .value[1].f32：进度遮罩的当前值；  .value[2].f32：进度遮罩的最大值；  .value[3].u32：进度遮罩的颜色。 |

## NODE\_BLEND\_MODE

```
1. NODE_BLEND_MODE = 46
```

当前控件背景与子节点内容进行混合，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 控制当前组件的混合模式类型，参数类型[ArkUI\_BlendMode](capi-native-type-h.md#arkui_blendmode)，默认值为ARKUI\_BLEND\_MODE\_NONE。 |
| .value[1]?.i32 | blendMode实现方式是否离屏，参数类型[ArkUI\_BlendApplyType](capi-native-type-h.md#arkui_blendapplytype)，默认值为BLEND\_APPLY\_TYPE\_FAST。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 控制当前组件的混合模式类型，参数类型[ArkUI\_BlendMode](capi-native-type-h.md#arkui_blendmode)，默认值为ARKUI\_BLEND\_MODE\_NONE。 |
| .value[1].i32 | blendMode实现方式是否离屏，参数类型[ArkUI\_BlendApplyType](capi-native-type-h.md#arkui_blendapplytype)，默认值为BLEND\_APPLY\_TYPE\_FAST。 |

## NODE\_GRAY\_SCALE

```
1. NODE_GRAY_SCALE = 49
```

灰度效果属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 灰度转换比例，范围0-1之间，默认值为0，比如0.5指按照50%进行灰度处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 灰度转换比例，范围0-1之间。 |

## NODE\_INVERT

```
1. NODE_INVERT = 50
```

反转输入的图像比例属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 图像反转比例，范围0-1之间，默认值为0，比如0.5指按照50%进行反转处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 图像反转比例，范围0-1之间。 |

## NODE\_SEPIA

```
1. NODE_SEPIA = 51
```

图像转换为深褐色比例属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 图像转换为深褐色比例，范围0-1之间，默认值为0，比如0.5指按照50%进行深褐色处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 图像转换为深褐色比例，范围0-1之间。 |

## NODE\_CONTRAST

```
1. NODE_CONTRAST = 52
```

对比度属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 对比度，等于1时为原图，越大则对比度越高，默认值为1，取值范围：[0, 10)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 对比度，取值范围：[0, 10)。 |

## NODE\_FOREGROUND\_COLOR

```
1. NODE_FOREGROUND_COLOR = 53
```

前景颜色属性，支持属性设置和属性获取接口。属性重置接口无效果。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xargb类型，如0xFFFF0000表示红色，默认值为0xFF000000。 |
| .value[0].i32 | 颜色数值枚举ArkUI\_ColoringStrategy。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xargb类型。 |

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

## NODE\_GEOMETRY\_TRANSITION

```
1. NODE_GEOMETRY_TRANSITION = 75
```

组件内隐式共享元素转场，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0]?.i32 | 参数类型为1或者0。共享元素绑定的2个组件，针对出场元素未进行删除时是否要继续参与共享元素动画，默认为false，不参与保持原始位置不动。 |
| .string | 用于设置绑定关系，id置""清除绑定关系避免参与共享行为，id可更换重新建立绑定关系。同一个id只能有两个组件绑定且是in/out不同类型角色，不能多个组件绑定同一个id。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 参数类型为1或者0。共享元素绑定的2个组件，针对出场元素未进行删除时是否要继续参与共享元素动画，默认未false，不参与保持原始位置不动。 |
| .string | 用于设置绑定关系，id置""清除绑定关系避免参与共享行为，id可更换重新建立绑定关系。同一个id只能有两个组件绑定且是in/out不同类型角色，不能多个组件绑定同一个id。 |

## NODE\_RENDER\_FIT

```
1. NODE_RENDER_FIT = 77
```

设置宽高动画过程中的组件内容填充方式，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 内容填充方式，使用[ArkUI\_RenderFit](capi-native-type-h.md#arkui_renderfit)枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 内容填充方式，使用[ArkUI\_RenderFit](capi-native-type-h.md#arkui_renderfit)枚举值。 |

## NODE\_OUTLINE\_COLOR

```
1. NODE_OUTLINE_COLOR = 78
```

外描边颜色属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 统一设置四条边的边框颜色，使用0xargb表示，如0xFFFF11FF。 |
| .value[0].u32 | 设置上侧边框颜色，使用0xargb表示，如0xFFFF11FF。 |
| .value[1].u32 | 设置右侧边框颜色，使用0xargb表示，如0xFFFF11FF。 |
| .value[2].u32 | 设置下侧边框颜色，使用0xargb表示，如0xFFFF11FF。 |
| .value[3].u32 | 设置左侧边框颜色，使用0xargb表示，如0xFFFF11FF。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 设置上侧边框颜色，使用0xargb表示，如0xFFFF11FF。 |
| .value[1].u32 | 设置右侧边框颜色，使用0xargb表示，如0xFFFF11FF。 |
| .value[2].u32 | 设置下侧边框颜色，使用0xargb表示，如0xFFFF11FF。 |
| .value[3].u32 | 设置左侧边框颜色，使用0xargb表示，如0xFFFF11FF。 |

## NODE\_COLOR\_BLEND

```
1. NODE_COLOR_BLEND = 81
```

为组件添加颜色叠加效果，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 叠加的颜色，使用0xargb表示，默认值为0x00000000。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 叠加的颜色，使用0xargb表示，如0xFFFF11FF。 |

## NODE\_FOREGROUND\_BLUR\_STYLE

```
1. NODE_FOREGROUND_BLUR_STYLE = 82
```

为当前组件提供内容模糊能力，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示内容模糊样式，取[ArkUI\_BlurStyle](capi-native-type-h.md#arkui_blurstyle)枚举值。 |
| .value[1]?.i32 | 表示内容模糊效果使用的深浅色模式，取[ArkUI\_ColorMode](capi-native-type-h.md#arkui_colormode)枚举值。 |
| .value[2]?.i32 | 表示内容模糊效果使用的取色模式，取[ArkUI\_AdaptiveColor](capi-native-type-h.md#arkui_adaptivecolor)枚举值。 |
| .value[3]?.f32 | 表示模糊效果程度，取[0.0,1.0]范围内的值。 |
| .value[4]?.i32 | 表示灰阶模糊参数，对黑色的提亮程度，取值范围为[0,127]。 |
| .value[5]?.i32 | 表示灰阶模糊参数，对白色的压暗程度，取值范围为[0,127]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示内容模糊样式，取[ArkUI\_BlurStyle](capi-native-type-h.md#arkui_blurstyle)枚举值。 |
| .value[1].i32 | 表示内容模糊效果使用的深浅色模式，取[ArkUI\_ColorMode](capi-native-type-h.md#arkui_colormode)枚举值。 |
| .value[2].i32 | 表示内容模糊效果使用的取色模式，取[ArkUI\_AdaptiveColor](capi-native-type-h.md#arkui_adaptivecolor)枚举值。 |
| .value[3].f32 | 表示模糊效果程度，取[0.0,1.0]范围内的值。 |
| .value[4].i32 | 表示灰阶模糊参数，对黑色的提亮程度，取值范围为[0,127]。 |
| .value[5].i32 | 表示灰阶模糊参数，对白色的压暗程度，取值范围为[0,127]。 |

## NODE\_TRANSITION

```
1. NODE_TRANSITION = 94
```

定义组件插入和删除时显示过渡动效，支持属性设置，属性获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 参数类型为[ArkUI\_TransitionEffect](capi-arkui-nativemodule-arkui-transitioneffect.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 参数类型为[ArkUI\_TransitionEffect](capi-arkui-nativemodule-arkui-transitioneffect.md)。 |

## NODE\_BACKDROP\_BLUR

```
1. NODE_BACKDROP_BLUR = 99
```

设置背景模糊效果，支持属性设置，属性重置和属性获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 表示背景模糊半径，取值范围[0,+∞)。单位px，默认值0.0。 |
| .value[1]?.f32 | 表示灰阶模糊参数，对黑色的提亮程度，取值范围为[0,127]。 |
| .value[2]?.f32 | 表示灰阶模糊参数，对白色的压暗程度，取值范围为[0,127]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 表示背景模糊半径，取值范围[0,+∞)。单位px。 |
| .value[1].f32 | 表示灰阶模糊参数，对黑色的提亮程度，取值范围为[0,127]。 |
| .value[2].f32 | 表示灰阶模糊参数，对白色的压暗程度，取值范围为[0,127]。 |

## NODE\_BACKGROUND\_IMAGE\_RESIZABLE\_WITH\_SLICE

```
1. NODE_BACKGROUND_IMAGE_RESIZABLE_WITH_SLICE = 100
```

设置背景图在拉伸时可调整大小的属性，支持属性设置，属性重置和属性获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 图片左部拉伸时，图片的像素值保持不变，单位为vp。 |
| .value[1].f32 | 图片顶部拉伸时，图片的像素值保持不变，单位为vp。 |
| .value[2].f32 | 图片右部拉伸时，图片的像素值保持不变，单位为vp。 |
| .value[3].f32 | 图片底部拉伸时，图片的像素值保持不变，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 图片左部拉伸时，图片的像素值保持不变，单位为vp。 |
| .value[1].f32 | 图片顶部拉伸时，图片的像素值保持不变，单位为vp。 |
| .value[2].f32 | 图片右部拉伸时，图片的像素值保持不变，单位为vp。 |
| .value[3].f32 | 图片底部拉伸时，图片的像素值保持不变，单位为vp。 |

## NODE\_TRANSLATE\_WITH\_PERCENT

```
1. NODE_TRANSLATE_WITH_PERCENT = 103
```

设置组件平移，支持百分比形式的平移入参，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | x轴移动距离，默认单位为百分比，除非value[3]存在且value[3]为0时单位为vp，默认值0。 |
| .value[1].f32 | y轴移动距离，默认单位为百分比，除非value[4]存在且value[4]为0时单位为vp，默认值0。 |
| .value[2].f32 | z轴移动距离，单位vp，默认值0。 |
| .value[3]?.i32 | x轴移动距离是否为百分比形式指定，取值范围：0或1。为1时表示以百分比形式指定，例如value[0].f32=0.1且value[3].i32=1时表示x方向平移10%。默认值1。 |
| .value[4]?.i32 | y轴移动距离是否为百分比形式指定，取值范围：0或1。为1时表示以百分比形式指定，例如value[1].f32=0.1且value[4].i32=1时表示y方向平移10%，默认值1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | x轴移动距离，单位取决于value[3]。 |
| .value[1].f32 | y轴移动距离，单位取决于value[4]。 |
| .value[2].f32 | z轴移动距离，单位vp。 |
| .value[3].i32 | x轴移动距离的单位是否为百分比，当value[3].i32为0时x轴移动距离单位为vp，当value[3].i32为1时x轴移动距离单位为百分比。 |
| .value[4].i32 | y轴移动距离的单位是否为百分比，当value[4].i32为0时y轴移动距离单位为vp，当value[4].i32为1时y轴移动距离单位为百分比。 |

## NODE\_ROTATE\_ANGLE

```
1. NODE_ROTATE_ANGLE = 104
```

设置组件旋转，支持各轴旋转角属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | x轴方向旋转角度，默认值0。 |
| .value[1].f32 | y轴方向旋转角度，默认值0。 |
| .value[2].f32 | z轴方向旋转角度，默认值0。 |
| .value[3].f32 | 视距，即视点到z=0平面的距离，单位px，默认值0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | x轴方向旋转角度，默认值0。 |
| .value[1].f32 | y轴方向旋转角度，默认值0。 |
| .value[2].f32 | z轴方向旋转角度，默认值0。 |
| .value[3].f32 | 视距，即视点到z=0平面的距离，单位px，默认值0。 |

## NODE\_PIXEL\_ROUND

```
1. NODE_PIXEL_ROUND = 109
```

设置组件的像素取整策略，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 组件的像素取整策略；参数类型为[ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 组件的像素取整策略；参数类型为[ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)。 |
