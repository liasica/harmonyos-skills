---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-pen-h
title: drawing_pen.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_pen.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fa99467eace231651380c76f3cc236d5c33386464f71e2c3eab19250de69ae2a
---

## 概述

PhonePC/2in1TabletTVWearable

文件中定义了与画笔相关的功能函数。

**相关示例：** [Drawing API示例(C/C++)](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKAPIDrawing)

**引用文件：** <native\_drawing/drawing\_pen.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_NativeColorSpaceManager](nativecolorspacemanager-oh-nativecolorspacemanager.md) | OH\_NativeColorSpaceManager | 声明色域管理对象，提供获取色域基础属性的能力。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_PenLineCapStyle](capi-drawing-pen-h.md#oh_drawing_penlinecapstyle) | OH\_Drawing\_PenLineCapStyle | 枚举集合定义了画笔笔帽的样式，即画笔在绘制线段时，在线段头尾端点的样式。 |
| [OH\_Drawing\_PenLineJoinStyle](capi-drawing-pen-h.md#oh_drawing_penlinejoinstyle) | OH\_Drawing\_PenLineJoinStyle | 枚举集合定义了线条转角的样式，即画笔在绘制折线段时，在折线转角处的样式。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen\* OH\_Drawing\_PenCreate(void)](capi-drawing-pen-h.md#oh_drawing_pencreate) | 用于创建一个画笔对象。 |
| [OH\_Drawing\_Pen\* OH\_Drawing\_PenCopy(OH\_Drawing\_Pen\* pen)](capi-drawing-pen-h.md#oh_drawing_pencopy) | 创建一个画笔对象副本[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)，用于拷贝一个已有画笔对象。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PenDestroy(OH\_Drawing\_Pen\* pen)](capi-drawing-pen-h.md#oh_drawing_pendestroy) | 用于销毁画笔对象并回收该对象占有的内存。 |
| [bool OH\_Drawing\_PenIsAntiAlias(const OH\_Drawing\_Pen\* pen)](capi-drawing-pen-h.md#oh_drawing_penisantialias) | 用于获取画笔是否设置抗锯齿属性，如果为真则说明画笔会启用抗锯齿功能，在绘制图形时会对图形的边缘像素进行半透明的模糊处理。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PenSetAntiAlias(OH\_Drawing\_Pen\* pen, bool antiAlias)](capi-drawing-pen-h.md#oh_drawing_pensetantialias) | 用于设置画笔的抗锯齿属性，设置为真则画笔在绘制图形时会对图形的边缘像素进行半透明的模糊处理。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [uint32\_t OH\_Drawing\_PenGetColor(const OH\_Drawing\_Pen\* pen)](capi-drawing-pen-h.md#oh_drawing_pengetcolor) | 用于获取画笔的颜色属性，颜色属性描述了画笔绘制图形轮廓时使用的颜色，用一个32位（ARGB）的变量表示。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PenSetColor(OH\_Drawing\_Pen\* pen, uint32\_t color)](capi-drawing-pen-h.md#oh_drawing_pensetcolor) | 用于设置画笔的颜色属性，颜色属性描述了画笔绘制图形轮廓时使用的颜色，用一个32位（ARGB）的变量表示。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [uint8\_t OH\_Drawing\_PenGetAlpha(const OH\_Drawing\_Pen\* pen)](capi-drawing-pen-h.md#oh_drawing_pengetalpha) | 获取画笔的透明度值。画笔在勾勒图形时透明通道会使用该值。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PenSetAlpha(OH\_Drawing\_Pen\* pen, uint8\_t alpha)](capi-drawing-pen-h.md#oh_drawing_pensetalpha) | 为画笔设置透明度值。画笔在勾勒图形时透明通道会使用该值。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [float OH\_Drawing\_PenGetWidth(const OH\_Drawing\_Pen\* pen)](capi-drawing-pen-h.md#oh_drawing_pengetwidth) | 用于获取画笔的厚度属性，厚度属性描述了画笔绘制图形轮廓的宽度。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PenSetWidth(OH\_Drawing\_Pen\* pen, float width)](capi-drawing-pen-h.md#oh_drawing_pensetwidth) | 用于设置画笔的厚度属性，厚度属性描述了画笔绘制图形轮廓的宽度。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [float OH\_Drawing\_PenGetMiterLimit(const OH\_Drawing\_Pen\* pen)](capi-drawing-pen-h.md#oh_drawing_pengetmiterlimit) | 用于获取折线尖角的限制值，当画笔绘制一条折线，转角类型设置为尖角时，那么此时该属性用于限制出现尖角的长度范围，如果超出则平角显示，不超出依然为尖角。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PenSetMiterLimit(OH\_Drawing\_Pen\* pen, float miter)](capi-drawing-pen-h.md#oh_drawing_pensetmiterlimit) | 用于设置折线尖角的限制值，当画笔绘制一条折线，转角类型设置为尖角时，那么此时该属性用于限制出现尖角的长度范围，如果超出则平角显示，不超出依然为尖角。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_PenLineCapStyle OH\_Drawing\_PenGetCap(const OH\_Drawing\_Pen\* pen)](capi-drawing-pen-h.md#oh_drawing_pengetcap) | 用于获取画笔笔帽的样式。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PenSetCap(OH\_Drawing\_Pen\* pen, OH\_Drawing\_PenLineCapStyle capStyle)](capi-drawing-pen-h.md#oh_drawing_pensetcap) | 用于设置画笔笔帽样式。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  capStyle不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [OH\_Drawing\_PenLineJoinStyle OH\_Drawing\_PenGetJoin(const OH\_Drawing\_Pen\* pen)](capi-drawing-pen-h.md#oh_drawing_pengetjoin) | 用于获取画笔绘制折线转角的样式。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PenSetJoin(OH\_Drawing\_Pen\* pen, OH\_Drawing\_PenLineJoinStyle joinStyle)](capi-drawing-pen-h.md#oh_drawing_pensetjoin) | 用于设置画笔绘制转角的样式。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  joinStyle不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [void OH\_Drawing\_PenSetShaderEffect(OH\_Drawing\_Pen\* pen, OH\_Drawing\_ShaderEffect\* shaderEffect)](capi-drawing-pen-h.md#oh_drawing_pensetshadereffect) | 设置画笔着色器效果。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PenSetShadowLayer(OH\_Drawing\_Pen\* pen, OH\_Drawing\_ShadowLayer\* shadowLayer)](capi-drawing-pen-h.md#oh_drawing_pensetshadowlayer) | 设置画笔阴影层效果，设置的阴影层效果当前仅在绘制文字时生效。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PenSetPathEffect(OH\_Drawing\_Pen\* pen, OH\_Drawing\_PathEffect\* pathEffect)](capi-drawing-pen-h.md#oh_drawing_pensetpatheffect) | 设置画笔路径效果。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PenSetFilter(OH\_Drawing\_Pen\* pen, OH\_Drawing\_Filter\* filter)](capi-drawing-pen-h.md#oh_drawing_pensetfilter) | 设置画笔滤波器。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PenGetFilter(OH\_Drawing\_Pen\* pen, OH\_Drawing\_Filter\* filter)](capi-drawing-pen-h.md#oh_drawing_pengetfilter) | 从画笔获取滤波器[OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)。滤波器是一个容器，可以承载蒙版滤波器和颜色滤波器。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen、filter任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PenSetBlendMode(OH\_Drawing\_Pen\* pen, OH\_Drawing\_BlendMode blendMode)](capi-drawing-pen-h.md#oh_drawing_pensetblendmode) | 为画笔设置一个混合器，该混合器实现了指定的混合模式枚举。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  blendMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [bool OH\_Drawing\_PenGetFillPath(OH\_Drawing\_Pen\* pen, const OH\_Drawing\_Path\* src, OH\_Drawing\_Path\* dst,const OH\_Drawing\_Rect\* rect, const OH\_Drawing\_Matrix\* matrix)](capi-drawing-pen-h.md#oh_drawing_pengetfillpath) | 获取使用画笔绘制的源路径轮廓，并用目标路径表示。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen、src、dst任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PenReset(OH\_Drawing\_Pen\* pen)](capi-drawing-pen-h.md#oh_drawing_penreset) | 将画笔重置至初始值。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PenSetColor4f(OH\_Drawing\_Pen\* pen, float a, float r, float g, float b,OH\_NativeColorSpaceManager\* colorSpaceManager)](capi-drawing-pen-h.md#oh_drawing_pensetcolor4f) | 用于设置画笔的颜色属性，颜色属性描述了画笔绘制图形轮廓时使用的颜色。  颜色采用浮点数表示的ARGB格式，色彩空间由[OH\_NativeColorSpaceManager](nativecolorspacemanager-oh-nativecolorspacemanager.md)指定。  如果colorSpaceManager为nullptr，使用SRGB（基于IEC 61966-2.1：1999的标准红绿蓝色彩空间）色彩空间作为默认值。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PenGetAlphaFloat(OH\_Drawing\_Pen\* pen, float\* a)](capi-drawing-pen-h.md#oh_drawing_pengetalphafloat) | 获取画笔颜色的透明度值。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PenGetRedFloat(OH\_Drawing\_Pen\* pen, float\* r)](capi-drawing-pen-h.md#oh_drawing_pengetredfloat) | 获取画笔颜色的红色分量。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PenGetGreenFloat(OH\_Drawing\_Pen\* pen, float\* g)](capi-drawing-pen-h.md#oh_drawing_pengetgreenfloat) | 获取画笔颜色的绿色分量。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PenGetBlueFloat(OH\_Drawing\_Pen\* pen, float\* b)](capi-drawing-pen-h.md#oh_drawing_pengetbluefloat) | 获取画笔颜色的蓝色分量。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_PenLineCapStyle

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_PenLineCapStyle
```

**描述**

枚举集合定义了画笔笔帽的样式，即画笔在绘制线段时，在线段头尾端点的样式。

**起始版本：** 8

| 枚举项 | 描述 |
| --- | --- |
| LINE\_FLAT\_CAP | 没有笔帽样式，线条头尾端点处横切。 |
| LINE\_SQUARE\_CAP | 笔帽的样式为方框，线条的头尾端点处多出一个方框，方框宽度和线段一样宽，高度是线段厚度的一半。 |
| LINE\_ROUND\_CAP | 笔帽的样式为圆弧，线条的头尾端点处多出一个半圆弧，半圆的直径与线段厚度一致。 |

### OH\_Drawing\_PenLineJoinStyle

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_PenLineJoinStyle
```

**描述**

枚举集合定义了线条转角的样式，即画笔在绘制折线段时，在折线转角处的样式。

**起始版本：** 8

| 枚举项 | 描述 |
| --- | --- |
| LINE\_MITER\_JOIN | 转角类型为尖角，如果折线角度比较小，则尖角会很长，需要使用限制值（miter limit）进行限制。 |
| LINE\_ROUND\_JOIN | 转角类型为圆头。 |
| LINE\_BEVEL\_JOIN | 转角类型为平头。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_PenCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Pen* OH_Drawing_PenCreate(void)
```

**描述**

用于创建一个画笔对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* | 函数会返回一个指针，指针指向创建的画笔对象。 |

### OH\_Drawing\_PenCopy()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Pen* OH_Drawing_PenCopy(OH_Drawing_Pen* pen)
```

**描述**

创建一个画笔对象副本[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)，用于拷贝一个已有画笔对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* | 函数会返回一个指针，指针指向创建的画笔对象副本[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)。如果对象返回NULL，表示创建失败；可能的原因是可用内存为空，或者是pen为NULL。 |

### OH\_Drawing\_PenDestroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PenDestroy(OH_Drawing_Pen* pen)
```

**描述**

用于销毁画笔对象并回收该对象占有的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象的指针。 |

### OH\_Drawing\_PenIsAntiAlias()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Drawing_PenIsAntiAlias(const OH_Drawing_Pen* pen)
```

**描述**

用于获取画笔是否设置抗锯齿属性，如果为真则说明画笔会启用抗锯齿功能，在绘制图形时会对图形的边缘像素进行半透明的模糊处理。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 函数返回画笔对象是否设置抗锯齿属性，返回真则设置了抗锯齿，返回假则没有设置抗锯齿。 |

### OH\_Drawing\_PenSetAntiAlias()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PenSetAntiAlias(OH_Drawing_Pen* pen, bool antiAlias)
```

**描述**

用于设置画笔的抗锯齿属性，设置为真则画笔在绘制图形时会对图形的边缘像素进行半透明的模糊处理。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象的指针。 |
| bool antiAlias | 真为抗锯齿，假则不做抗锯齿处理。 |

### OH\_Drawing\_PenGetColor()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_Drawing_PenGetColor(const OH_Drawing_Pen* pen)
```

**描述**

用于获取画笔的颜色属性，颜色属性描述了画笔绘制图形轮廓时使用的颜色，用一个32位（ARGB）的变量表示。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 函数返回一个描述颜色的32位（ARGB）变量。 |

### OH\_Drawing\_PenSetColor()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PenSetColor(OH_Drawing_Pen* pen, uint32_t color)
```

**描述**

用于设置画笔的颜色属性，颜色属性描述了画笔绘制图形轮廓时使用的颜色，用一个32位（ARGB）的变量表示。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象的指针。 |
| uint32\_t color | 描述颜色的32位（ARGB）变量。 |

### OH\_Drawing\_PenGetAlpha()

PhonePC/2in1TabletTVWearable

```
1. uint8_t OH_Drawing_PenGetAlpha(const OH_Drawing_Pen* pen)
```

**描述**

获取画笔的透明度值。画笔在勾勒图形时透明通道会使用该值。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 表示指向画笔对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint8\_t | 返回一个8比特的值表示透明度。 |

### OH\_Drawing\_PenSetAlpha()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PenSetAlpha(OH_Drawing_Pen* pen, uint8_t alpha)
```

**描述**

为画笔设置透明度值。画笔在勾勒图形时透明通道会使用该值。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 表示指向画笔对象的指针。 |
| uint8\_t alpha | 表示要设置的透明度值，是一个8比特的变量。 |

### OH\_Drawing\_PenGetWidth()

PhonePC/2in1TabletTVWearable

```
1. float OH_Drawing_PenGetWidth(const OH_Drawing_Pen* pen)
```

**描述**

用于获取画笔的厚度属性，厚度属性描述了画笔绘制图形轮廓的宽度。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 函数返回画笔的厚度。 |

### OH\_Drawing\_PenSetWidth()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PenSetWidth(OH_Drawing_Pen* pen, float width)
```

**描述**

用于设置画笔的厚度属性，厚度属性描述了画笔绘制图形轮廓的宽度。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象的指针。 |
| float width | 描述画笔厚度的变量。 |

### OH\_Drawing\_PenGetMiterLimit()

PhonePC/2in1TabletTVWearable

```
1. float OH_Drawing_PenGetMiterLimit(const OH_Drawing_Pen* pen)
```

**描述**

用于获取折线尖角的限制值，当画笔绘制一条折线，转角类型设置为尖角时，那么此时该属性用于限制出现尖角的长度范围，如果超出则平角显示，不超出依然为尖角。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 函数返回尖角的限制值。 |

### OH\_Drawing\_PenSetMiterLimit()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PenSetMiterLimit(OH_Drawing_Pen* pen, float miter)
```

**描述**

用于设置折线尖角的限制值，当画笔绘制一条折线，转角类型设置为尖角时，那么此时该属性用于限制出现尖角的长度范围，如果超出则平角显示，不超出依然为尖角。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象的指针。 |
| float miter | 描述尖角限制值的变量。 |

### OH\_Drawing\_PenGetCap()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_PenLineCapStyle OH_Drawing_PenGetCap(const OH_Drawing_Pen* pen)
```

**描述**

用于获取画笔笔帽的样式。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_PenLineCapStyle](capi-drawing-pen-h.md#oh_drawing_penlinecapstyle) | 函数返回画笔笔帽样式。 |

### OH\_Drawing\_PenSetCap()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PenSetCap(OH_Drawing_Pen* pen, OH_Drawing_PenLineCapStyle capStyle)
```

**描述**

用于设置画笔笔帽样式。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

capStyle不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象的指针。 |
| [OH\_Drawing\_PenLineCapStyle](capi-drawing-pen-h.md#oh_drawing_penlinecapstyle) capStyle | 描述画笔笔帽样式的变量。 |

### OH\_Drawing\_PenGetJoin()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_PenLineJoinStyle OH_Drawing_PenGetJoin(const OH_Drawing_Pen* pen)
```

**描述**

用于获取画笔绘制折线转角的样式。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_PenLineJoinStyle](capi-drawing-pen-h.md#oh_drawing_penlinejoinstyle) | 函数返回折线转角的样式。 |

### OH\_Drawing\_PenSetJoin()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PenSetJoin(OH_Drawing_Pen* pen, OH_Drawing_PenLineJoinStyle joinStyle)
```

**描述**

用于设置画笔绘制转角的样式。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

joinStyle不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象的指针。 |
| [OH\_Drawing\_PenLineJoinStyle](capi-drawing-pen-h.md#oh_drawing_penlinejoinstyle) joinStyle | 折线转角样式。 |

### OH\_Drawing\_PenSetShaderEffect()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PenSetShaderEffect(OH_Drawing_Pen* pen, OH_Drawing_ShaderEffect* shaderEffect)
```

**描述**

设置画笔着色器效果。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)的指针。 |
| [OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)\* shaderEffect | 指向着色器对象[OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)的指针，为NULL表示清空着色器效果。 |

### OH\_Drawing\_PenSetShadowLayer()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PenSetShadowLayer(OH_Drawing_Pen* pen, OH_Drawing_ShadowLayer* shadowLayer)
```

**描述**

设置画笔阴影层效果，设置的阴影层效果当前仅在绘制文字时生效。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)的指针。 |
| [OH\_Drawing\_ShadowLayer](capi-drawing-oh-drawing-shadowlayer.md)\* shadowLayer | 指向阴影层对象[OH\_Drawing\_ShadowLayer](capi-drawing-oh-drawing-shadowlayer.md)的指针，为NULL表示清空阴影层效果。 |

### OH\_Drawing\_PenSetPathEffect()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PenSetPathEffect(OH_Drawing_Pen* pen, OH_Drawing_PathEffect* pathEffect)
```

**描述**

设置画笔路径效果。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)的指针。 |
| [OH\_Drawing\_PathEffect](capi-drawing-oh-drawing-patheffect.md)\* pathEffect | 指向路径效果对象[OH\_Drawing\_PathEffect](capi-drawing-oh-drawing-patheffect.md)的指针，为NULL表示清空路径效果。 |

### OH\_Drawing\_PenSetFilter()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PenSetFilter(OH_Drawing_Pen* pen, OH_Drawing_Filter* filter)
```

**描述**

设置画笔滤波器。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)的指针。 |
| [OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)\* filter | 指向滤波器[OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)的指针，为NULL表示清空画笔滤波器。 |

### OH\_Drawing\_PenGetFilter()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PenGetFilter(OH_Drawing_Pen* pen, OH_Drawing_Filter* filter)
```

**描述**

从画笔获取滤波器[OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)。滤波器是一个容器，可以承载蒙版滤波器和颜色滤波器。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen、filter任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)的指针。 |
| [OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)\* filter | 指向滤波器对象[OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)的指针。 |

### OH\_Drawing\_PenSetBlendMode()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PenSetBlendMode(OH_Drawing_Pen* pen, OH_Drawing_BlendMode blendMode)
```

**描述**

为画笔设置一个混合器，该混合器实现了指定的混合模式枚举。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

blendMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)的指针。 |
| [OH\_Drawing\_BlendMode](capi-drawing-types-h.md#oh_drawing_blendmode) blendMode | 混合模式枚举类型[OH\_Drawing\_BlendMode](capi-drawing-types-h.md#oh_drawing_blendmode)。 |

### OH\_Drawing\_PenGetFillPath()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Drawing_PenGetFillPath(OH_Drawing_Pen* pen, const OH_Drawing_Path* src, OH_Drawing_Path* dst,const OH_Drawing_Rect* rect, const OH_Drawing_Matrix* matrix)
```

**描述**

获取使用画笔绘制的源路径轮廓，并用目标路径表示。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen、src、dst任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)的指针。 |
| const [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* src | 指向源路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* dst | 指向目标路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象[OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)的指针，推荐使用NULL。 |
| const [OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)\* matrix | 指向矩阵对象[OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)的指针，推荐使用NULL, 默认是一个单位矩阵。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 获取目标路径是否成功。true表示获取成功，false表示获取失败。 |

### OH\_Drawing\_PenReset()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PenReset(OH_Drawing_Pen* pen)
```

**描述**

将画笔重置至初始值。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)的指针。 |

### OH\_Drawing\_PenSetColor4f()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_PenSetColor4f(OH_Drawing_Pen* pen, float a, float r, float g, float b,OH_NativeColorSpaceManager* colorSpaceManager)
```

**描述**

用于设置画笔的颜色属性，颜色属性描述了画笔绘制图形轮廓时使用的颜色。

颜色采用浮点数表示的ARGB格式，色彩空间由[OH\_NativeColorSpaceManager](nativecolorspacemanager-oh-nativecolorspacemanager.md)指定。

如果colorSpaceManager为nullptr，使用SRGB（基于IEC 61966-2.1：1999的标准红绿蓝色彩空间）色彩空间作为默认值。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_Drawing\_Pen\* pen | 表示指向[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)对象的指针。 |
| float a | 表示颜色中的透明度值，用0.0 ~ 1.0之间的浮点数表示，大于1.0时，取1.0，小于0.0时，取0.0。 |
| float r | 表示颜色中的红色分量，用0.0 ~ 1.0之间的浮点数表示，大于1.0时，取1.0，小于0.0时，取0.0。 |
| float g | 表示颜色中的绿色分量，用0.0 ~ 1.0之间的浮点数表示，大于1.0时，取1.0，小于0.0时，取0.0。 |
| float b | 表示颜色中的蓝色分量，用0.0 ~ 1.0之间的浮点数表示，大于1.0时，取1.0，小于0.0时，取0.0。 |
| [OH\_NativeColorSpaceManager](nativecolorspacemanager-oh-nativecolorspacemanager.md)\* colorSpaceManager | 表示指向[OH\_NativeColorSpaceManager](nativecolorspacemanager-oh-nativecolorspacemanager.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数pen为NULL。 |

### OH\_Drawing\_PenGetAlphaFloat()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_PenGetAlphaFloat(OH_Drawing_Pen* pen, float* a)
```

**描述**

获取画笔颜色的透明度值。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 表示指向[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)对象的指针。 |
| float\* a | 表示颜色中的透明度，范围为0.0 ~ 1.0的浮点数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数pen或a为NULL。 |

### OH\_Drawing\_PenGetRedFloat()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_PenGetRedFloat(OH_Drawing_Pen* pen, float* r)
```

**描述**

获取画笔颜色的红色分量。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 表示指向[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)对象的指针。 |
| float\* r | 表示颜色中的红色分量，范围为0.0 ~ 1.0的浮点数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数pen或r为NULL。 |

### OH\_Drawing\_PenGetGreenFloat()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_PenGetGreenFloat(OH_Drawing_Pen* pen, float* g)
```

**描述**

获取画笔颜色的绿色分量。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 表示指向[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)对象的指针。 |
| float\* g | 表示颜色中的绿色分量，范围为0.0 ~ 1.0的浮点数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数pen或g为NULL。 |

### OH\_Drawing\_PenGetBlueFloat()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_PenGetBlueFloat(OH_Drawing_Pen* pen, float* b)
```

**描述**

获取画笔颜色的蓝色分量。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 表示指向[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)对象的指针。 |
| float\* b | 表示颜色中的蓝色分量，范围为0.0 ~ 1.0的浮点数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数pen或b为NULL。 |
