---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-brush-h
title: drawing_brush.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_brush.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2424a6d8df7a0e8523b3c0502fa78ce1a5c87fdc7c5ee8d18b7611abd2c76be9
---

## 概述

文件中定义了与画刷相关的功能函数。

本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**相关示例：** [Drawing API示例(C/C++)](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKAPIDrawing)

**引用文件：** <native\_drawing/drawing\_brush.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_NativeColorSpaceManager](capi-nativecolorspacemanager-oh-nativecolorspacemanager.md) | OH\_NativeColorSpaceManager | 声明色彩空间管理对象，提供获取色彩空间基础属性的能力。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_Brush\* OH\_Drawing\_BrushCreate(void)](capi-drawing-brush-h.md#oh_drawing_brushcreate) | 用于创建一个画刷对象。调用本接口创建的画刷对象，在使用完毕后必须调用[OH\_Drawing\_BrushDestroy](capi-drawing-brush-h.md#oh_drawing_brushdestroy)销毁并回收内存，否则会导致内存泄漏。 |
| [OH\_Drawing\_Brush\* OH\_Drawing\_BrushCopy(OH\_Drawing\_Brush\* brush)](capi-drawing-brush-h.md#oh_drawing_brushcopy) | 拷贝一个已有画刷对象，创建其画刷对象副本[OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)。调用本接口创建的画刷对象，在使用完毕后必须调用[OH\_Drawing\_BrushDestroy](capi-drawing-brush-h.md#oh_drawing_brushdestroy)销毁并回收内存，否则会导致内存泄漏。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_BrushDestroy(OH\_Drawing\_Brush\* brush)](capi-drawing-brush-h.md#oh_drawing_brushdestroy) | 用于销毁画刷对象并回收该对象占用的内存。应与[OH\_Drawing\_BrushCreate](capi-drawing-brush-h.md#oh_drawing_brushcreate)或[OH\_Drawing\_BrushCopy](capi-drawing-brush-h.md#oh_drawing_brushcopy)配对使用，对已创建或拷贝得到的画刷对象进行释放，避免内存泄漏。 |
| [bool OH\_Drawing\_BrushIsAntiAlias(const OH\_Drawing\_Brush\* brush)](capi-drawing-brush-h.md#oh_drawing_brushisantialias) | 用于获取画刷是否设置抗锯齿属性，如果为真则说明画刷会启用抗锯齿功能，在绘制图形时会对图形的边缘像素进行半透明的模糊处理。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_BrushSetAntiAlias(OH\_Drawing\_Brush\* brush, bool antiAlias)](capi-drawing-brush-h.md#oh_drawing_brushsetantialias) | 用于设置画刷的抗锯齿属性，设置为真则画刷在绘制图形时会对图形的边缘像素进行半透明的模糊处理。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [uint32\_t OH\_Drawing\_BrushGetColor(const OH\_Drawing\_Brush\* brush)](capi-drawing-brush-h.md#oh_drawing_brushgetcolor) | 用于获取画刷的颜色属性，颜色属性描述了画刷填充图形时使用的颜色，用一个32位（ARGB）的变量表示。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_BrushSetColor(OH\_Drawing\_Brush\* brush, uint32\_t color)](capi-drawing-brush-h.md#oh_drawing_brushsetcolor) | 用于设置画刷的颜色属性，颜色属性描述了画刷填充图形时使用的颜色，用一个32位（ARGB）的变量表示。当需要色彩空间管理或高精度颜色表示时，建议优先使用[OH\_Drawing\_BrushSetColor4f](capi-drawing-brush-h.md#oh_drawing_brushsetcolor4f)。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [uint8\_t OH\_Drawing\_BrushGetAlpha(const OH\_Drawing\_Brush\* brush)](capi-drawing-brush-h.md#oh_drawing_brushgetalpha) | 用于获取画刷的透明度值。画刷在填充形状时透明通道会使用该值。当画刷颜色通过[OH\_Drawing\_BrushSetColor4f](capi-drawing-brush-h.md#oh_drawing_brushsetcolor4f)设置时，建议使用[OH\_Drawing\_BrushGetAlphaFloat](capi-drawing-brush-h.md#oh_drawing_brushgetalphafloat)获取透明度以避免精度丢失。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_BrushSetAlpha(OH\_Drawing\_Brush\* brush, uint8\_t alpha)](capi-drawing-brush-h.md#oh_drawing_brushsetalpha) | 为画刷设置透明度值。画刷在填充形状时透明通道会使用该值。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_BrushSetShaderEffect(OH\_Drawing\_Brush\* brush, OH\_Drawing\_ShaderEffect\* shaderEffect)](capi-drawing-brush-h.md#oh_drawing_brushsetshadereffect) | 为画刷设置着色器效果。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_BrushSetShadowLayer(OH\_Drawing\_Brush\* brush, OH\_Drawing\_ShadowLayer\* shadowLayer)](capi-drawing-brush-h.md#oh_drawing_brushsetshadowlayer) | 为画刷设置阴影层，设置的阴影层效果当前仅在绘制文字时生效。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_BrushSetFilter(OH\_Drawing\_Brush\* brush, OH\_Drawing\_Filter\* filter)](capi-drawing-brush-h.md#oh_drawing_brushsetfilter) | 为画刷设置滤波器[OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)。滤波器是一个容器，可以承载蒙版滤波器和颜色滤波器。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_BrushGetFilter(OH\_Drawing\_Brush\* brush, OH\_Drawing\_Filter\* filter)](capi-drawing-brush-h.md#oh_drawing_brushgetfilter) | 从画刷获取滤波器[OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)。滤波器是一个容器，可以承载蒙版滤波器和颜色滤波器。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  brush、filter任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_BrushSetBlendMode(OH\_Drawing\_Brush\* brush, OH\_Drawing\_BlendMode blendMode)](capi-drawing-brush-h.md#oh_drawing_brushsetblendmode) | 为画刷设置混合模式，通过指定的混合模式枚举决定画刷在绘制时源像素与目标像素的合成方式。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  blendMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [void OH\_Drawing\_BrushReset(OH\_Drawing\_Brush\* brush)](capi-drawing-brush-h.md#oh_drawing_brushreset) | 将画刷重置至初始状态，清空所有已设置的属性。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_BrushSetColor4f(OH\_Drawing\_Brush\* brush, float a, float r, float g, float b, OH\_NativeColorSpaceManager\* colorSpaceManager)](capi-drawing-brush-h.md#oh_drawing_brushsetcolor4f) | 设置画刷的颜色。画刷使用该颜色填充形状。  与[OH\_Drawing\_BrushSetColor](capi-drawing-brush-h.md#oh_drawing_brushsetcolor)相比，本接口使用浮点数表示ARGB分量，精度更高，并支持通过colorSpaceManager指定色彩空间；当需要色彩空间管理或高精度颜色表示时，优先使用本接口。  颜色采用浮点数表示的ARGB格式，色彩空间由[OH\_NativeColorSpaceManager](capi-nativecolorspacemanager-oh-nativecolorspacemanager.md)指定。  如果colorSpaceManager为NULL，使用sRGB（基于IEC 61966-2.1:1999的标准红绿蓝色彩空间）色彩空间作为默认值。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_BrushGetAlphaFloat(const OH\_Drawing\_Brush\* brush, float\* a)](capi-drawing-brush-h.md#oh_drawing_brushgetalphafloat) | 用于获取画刷颜色的透明度值，以浮点数形式表示。与[OH\_Drawing\_BrushGetAlpha](capi-drawing-brush-h.md#oh_drawing_brushgetalpha)相比，本接口返回浮点数表示的透明度，精度更高；当画刷颜色通过[OH\_Drawing\_BrushSetColor4f](capi-drawing-brush-h.md#oh_drawing_brushsetcolor4f)设置时，应使用本接口获取透明度以避免精度丢失。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_BrushGetRedFloat(const OH\_Drawing\_Brush\* brush, float\* r)](capi-drawing-brush-h.md#oh_drawing_brushgetredfloat) | 用于获取画刷颜色的红色分量，以浮点数形式表示。与[OH\_Drawing\_BrushGetColor](capi-drawing-brush-h.md#oh_drawing_brushgetcolor)相比，本接口以浮点数返回颜色分量，精度更高；当画刷颜色通过[OH\_Drawing\_BrushSetColor4f](capi-drawing-brush-h.md#oh_drawing_brushsetcolor4f)设置时，应使用本接口获取红色分量以避免精度丢失。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_BrushGetGreenFloat(const OH\_Drawing\_Brush\* brush, float\* g)](capi-drawing-brush-h.md#oh_drawing_brushgetgreenfloat) | 用于获取画刷颜色的绿色分量，以浮点数形式表示。与[OH\_Drawing\_BrushGetColor](capi-drawing-brush-h.md#oh_drawing_brushgetcolor)相比，本接口以浮点数返回颜色分量，精度更高；当画刷颜色通过[OH\_Drawing\_BrushSetColor4f](capi-drawing-brush-h.md#oh_drawing_brushsetcolor4f)设置时，应使用本接口获取绿色分量以避免精度丢失。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_BrushGetBlueFloat(const OH\_Drawing\_Brush\* brush, float\* b)](capi-drawing-brush-h.md#oh_drawing_brushgetbluefloat) | 用于获取画刷颜色的蓝色分量，以浮点数形式表示。与[OH\_Drawing\_BrushGetColor](capi-drawing-brush-h.md#oh_drawing_brushgetcolor)相比，本接口以浮点数返回颜色分量，精度更高；当画刷颜色通过[OH\_Drawing\_BrushSetColor4f](capi-drawing-brush-h.md#oh_drawing_brushsetcolor4f)设置时，应使用本接口获取蓝色分量以避免精度丢失。 |

## 函数说明

### OH\_Drawing\_BrushCreate()

```c
OH_Drawing_Brush* OH_Drawing_BrushCreate(void)
```

**描述**

用于创建一个画刷对象。调用本接口创建的画刷对象，在使用完毕后必须调用[OH\_Drawing\_BrushDestroy](capi-drawing-brush-h.md#oh_drawing_brushdestroy)销毁并回收内存，否则会导致内存泄漏。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* | 函数会返回一个指针，指针指向创建的画刷对象。如果返回NULL，表示创建失败；可能的原因是可用内存不足。 |

### OH\_Drawing\_BrushCopy()

```c
OH_Drawing_Brush* OH_Drawing_BrushCopy(OH_Drawing_Brush* brush)
```

**描述**

拷贝一个已有画刷对象，创建其画刷对象副本[OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)。调用本接口创建的画刷对象，在使用完毕后必须调用[OH\_Drawing\_BrushDestroy](capi-drawing-brush-h.md#oh_drawing_brushdestroy)销毁并回收内存，否则会导致内存泄漏。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 指向画刷对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* | 函数会返回一个指针，指针指向创建的画刷对象副本[OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)。如果返回NULL，表示创建失败；可能的原因是可用内存不足，或者是brush为NULL。 |

### OH\_Drawing\_BrushDestroy()

```c
void OH_Drawing_BrushDestroy(OH_Drawing_Brush* brush)
```

**描述**

用于销毁画刷对象并回收该对象占用的内存。应与[OH\_Drawing\_BrushCreate](capi-drawing-brush-h.md#oh_drawing_brushcreate)或[OH\_Drawing\_BrushCopy](capi-drawing-brush-h.md#oh_drawing_brushcopy)配对使用，对已创建或拷贝得到的画刷对象进行释放，避免内存泄漏。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 指向画刷对象的指针。 |

### OH\_Drawing\_BrushIsAntiAlias()

```c
bool OH_Drawing_BrushIsAntiAlias(const OH_Drawing_Brush* brush)
```

**描述**

用于获取画刷是否设置抗锯齿属性，如果为真则说明画刷会启用抗锯齿功能，在绘制图形时会对图形的边缘像素进行半透明的模糊处理。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 指向画刷对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 函数返回画刷对象是否设置抗锯齿属性，返回真则设置了抗锯齿，返回假则没有设置抗锯齿。 |

### OH\_Drawing\_BrushSetAntiAlias()

```c
void OH_Drawing_BrushSetAntiAlias(OH_Drawing_Brush* brush, bool antiAlias)
```

**描述**

用于设置画刷的抗锯齿属性，设置为真则画刷在绘制图形时会对图形的边缘像素进行半透明的模糊处理。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 指向画刷对象的指针。 |
| bool antiAlias | 真为抗锯齿，假则不做抗锯齿处理。 |

### OH\_Drawing\_BrushGetColor()

```c
uint32_t OH_Drawing_BrushGetColor(const OH_Drawing_Brush* brush)
```

**描述**

用于获取画刷的颜色属性，颜色属性描述了画刷填充图形时使用的颜色，用一个32位（ARGB）的变量表示。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 指向画刷对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 函数返回一个描述颜色的32位（ARGB）变量，各颜色通道取值范围为[0, 255]。 |

### OH\_Drawing\_BrushSetColor()

```c
void OH_Drawing_BrushSetColor(OH_Drawing_Brush* brush, uint32_t color)
```

**描述**

用于设置画刷的颜色属性，颜色属性描述了画刷填充图形时使用的颜色，用一个32位（ARGB）的变量表示。当需要色彩空间管理或高精度颜色表示时，建议优先使用[OH\_Drawing\_BrushSetColor4f](capi-drawing-brush-h.md#oh_drawing_brushsetcolor4f)。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 指向画刷对象的指针。 |
| uint32\_t color | 描述颜色的32位（ARGB）变量，各颜色通道取值范围为[0, 255]。 |

### OH\_Drawing\_BrushGetAlpha()

```c
uint8_t OH_Drawing_BrushGetAlpha(const OH_Drawing_Brush* brush)
```

**描述**

用于获取画刷的透明度值。画刷在填充形状时透明通道会使用该值。当画刷颜色通过[OH\_Drawing\_BrushSetColor4f](capi-drawing-brush-h.md#oh_drawing_brushsetcolor4f)设置时，建议使用[OH\_Drawing\_BrushGetAlphaFloat](capi-drawing-brush-h.md#oh_drawing_brushgetalphafloat)获取透明度以避免精度丢失。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 指向画刷对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint8\_t | 返回一个8位无符号整数，用于表示透明度值，取值范围为[0, 255]，0表示完全透明，255表示完全不透明。 |

### OH\_Drawing\_BrushSetAlpha()

```c
void OH_Drawing_BrushSetAlpha(OH_Drawing_Brush* brush, uint8_t alpha)
```

**描述**

为画刷设置透明度值。画刷在填充形状时透明通道会使用该值。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 指向画刷对象的指针。 |
| uint8\_t alpha | 表示要设置的透明度值，取值范围为[0, 255]的8位无符号整数，0表示完全透明，255表示完全不透明。 |

### OH\_Drawing\_BrushSetShaderEffect()

```c
void OH_Drawing_BrushSetShaderEffect(OH_Drawing_Brush* brush, OH_Drawing_ShaderEffect* shaderEffect)
```

**描述**

为画刷设置着色器效果。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 指向画刷对象的指针。 |
| [OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)\* shaderEffect | 表示指向着色器对象的指针，为NULL表示清空画刷的着色器效果。 |

### OH\_Drawing\_BrushSetShadowLayer()

```c
void OH_Drawing_BrushSetShadowLayer(OH_Drawing_Brush* brush, OH_Drawing_ShadowLayer* shadowLayer)
```

**描述**

为画刷设置阴影层，设置的阴影层效果当前仅在绘制文字时生效。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 指向画刷对象的指针。 |
| [OH\_Drawing\_ShadowLayer](capi-drawing-oh-drawing-shadowlayer.md)\* shadowLayer | 表示指向阴影层的指针，为NULL表示清空画刷的阴影层效果。 |

### OH\_Drawing\_BrushSetFilter()

```c
void OH_Drawing_BrushSetFilter(OH_Drawing_Brush* brush, OH_Drawing_Filter* filter)
```

**描述**

为画刷设置滤波器[OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)。滤波器是一个容器，可以承载蒙版滤波器和颜色滤波器。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 指向画刷对象的指针。 |
| [OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)\* filter | 表示指向滤波器对象的指针，为NULL表示清空画刷滤波器。 |

### OH\_Drawing\_BrushGetFilter()

```c
void OH_Drawing_BrushGetFilter(OH_Drawing_Brush* brush, OH_Drawing_Filter* filter)
```

**描述**

从画刷获取滤波器[OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)。滤波器是一个容器，可以承载蒙版滤波器和颜色滤波器。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

brush、filter任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 指向画刷对象[OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)的指针。 |
| [OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)\* filter | 表示指向滤波器对象[OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)的指针，用于接收从画刷中获取的滤波器。调用前需分配好内存，由函数写入结果。 |

### OH\_Drawing\_BrushSetBlendMode()

```c
void OH_Drawing_BrushSetBlendMode(OH_Drawing_Brush* brush, OH_Drawing_BlendMode blendMode)
```

**描述**

为画刷设置混合模式，通过指定的混合模式枚举决定画刷在绘制时源像素与目标像素的合成方式。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

blendMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 指向画刷对象[OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)的指针。 |
| [OH\_Drawing\_BlendMode](capi-drawing-types-h.md#oh_drawing_blendmode) blendMode | 要设置的混合模式，用于指定画刷在绘制时源像素与目标像素的混合方式。枚举类型[OH\_Drawing\_BlendMode](capi-drawing-types-h.md#oh_drawing_blendmode)。 |

### OH\_Drawing\_BrushReset()

```c
void OH_Drawing_BrushReset(OH_Drawing_Brush* brush)
```

**描述**

将画刷重置至初始状态，清空所有已设置的属性。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 指向画刷对象[OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)的指针。 |

### OH\_Drawing\_BrushSetColor4f()

```c
OH_Drawing_ErrorCode OH_Drawing_BrushSetColor4f(OH_Drawing_Brush* brush, float a, float r, float g, float b, OH_NativeColorSpaceManager* colorSpaceManager)
```

**描述**

设置画刷的颜色。画刷使用该颜色填充形状。

与[OH\_Drawing\_BrushSetColor](capi-drawing-brush-h.md#oh_drawing_brushsetcolor)相比，本接口使用浮点数表示ARGB分量，精度更高，并支持通过colorSpaceManager指定色彩空间；当需要色彩空间管理或高精度颜色表示时，优先使用本接口。

颜色采用浮点数表示的ARGB格式，色彩空间由[OH\_NativeColorSpaceManager](capi-nativecolorspacemanager-oh-nativecolorspacemanager.md)指定。

如果colorSpaceManager为NULL，使用sRGB（基于IEC 61966-2.1:1999的标准红绿蓝色彩空间）色彩空间作为默认值。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 表示指向[OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)对象的指针。 |
| float a | 表示颜色中的透明度值，用[0.0, 1.0]之间的浮点数表示，大于1.0时，取1.0，小于0.0时，取0.0。 |
| float r | 表示颜色中的红色分量，用[0.0, 1.0]之间的浮点数表示，大于1.0时，取1.0，小于0.0时，取0.0。 |
| float g | 表示颜色中的绿色分量，用[0.0, 1.0]之间的浮点数表示，大于1.0时，取1.0，小于0.0时，取0.0。 |
| float b | 表示颜色中的蓝色分量，用[0.0, 1.0]之间的浮点数表示，大于1.0时，取1.0，小于0.0时，取0.0。 |
| [OH\_NativeColorSpaceManager](capi-nativecolorspacemanager-oh-nativecolorspacemanager.md)\* colorSpaceManager | 表示指向[OH\_NativeColorSpaceManager](capi-nativecolorspacemanager-oh-nativecolorspacemanager.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数brush为NULL。 |

### OH\_Drawing\_BrushGetAlphaFloat()

```c
OH_Drawing_ErrorCode OH_Drawing_BrushGetAlphaFloat(const OH_Drawing_Brush* brush, float* a)
```

**描述**

用于获取画刷颜色的透明度值，以浮点数形式表示。与[OH\_Drawing\_BrushGetAlpha](capi-drawing-brush-h.md#oh_drawing_brushgetalpha)相比，本接口返回浮点数表示的透明度，精度更高；当画刷颜色通过[OH\_Drawing\_BrushSetColor4f](capi-drawing-brush-h.md#oh_drawing_brushsetcolor4f)设置时，应使用本接口获取透明度以避免精度丢失。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 表示指向[OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)对象的指针。 |
| float\* a | 表示指向浮点数的指针，用于接收画刷颜色的透明度值，取值范围为[0.0, 1.0]。调用前需确保指针指向有效内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数brush或a为NULL。 |

### OH\_Drawing\_BrushGetRedFloat()

```c
OH_Drawing_ErrorCode OH_Drawing_BrushGetRedFloat(const OH_Drawing_Brush* brush, float* r)
```

**描述**

用于获取画刷颜色的红色分量，以浮点数形式表示。与[OH\_Drawing\_BrushGetColor](capi-drawing-brush-h.md#oh_drawing_brushgetcolor)相比，本接口以浮点数返回颜色分量，精度更高；当画刷颜色通过[OH\_Drawing\_BrushSetColor4f](capi-drawing-brush-h.md#oh_drawing_brushsetcolor4f)设置时，应使用本接口获取红色分量以避免精度丢失。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 表示指向[OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)对象的指针。 |
| float\* r | 表示指向浮点数的指针，用于接收画刷颜色的红色分量值，取值范围为[0.0, 1.0]。调用前需确保指针指向有效内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数brush或r为NULL。 |

### OH\_Drawing\_BrushGetGreenFloat()

```c
OH_Drawing_ErrorCode OH_Drawing_BrushGetGreenFloat(const OH_Drawing_Brush* brush, float* g)
```

**描述**

用于获取画刷颜色的绿色分量，以浮点数形式表示。与[OH\_Drawing\_BrushGetColor](capi-drawing-brush-h.md#oh_drawing_brushgetcolor)相比，本接口以浮点数返回颜色分量，精度更高；当画刷颜色通过[OH\_Drawing\_BrushSetColor4f](capi-drawing-brush-h.md#oh_drawing_brushsetcolor4f)设置时，应使用本接口获取绿色分量以避免精度丢失。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 表示指向[OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)对象的指针。 |
| float\* g | 表示指向浮点数的指针，用于接收画刷颜色的绿色分量值，取值范围为[0.0, 1.0]。调用前需确保指针指向有效内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数brush或g为NULL。 |

### OH\_Drawing\_BrushGetBlueFloat()

```c
OH_Drawing_ErrorCode OH_Drawing_BrushGetBlueFloat(const OH_Drawing_Brush* brush, float* b)
```

**描述**

用于获取画刷颜色的蓝色分量，以浮点数形式表示。与[OH\_Drawing\_BrushGetColor](capi-drawing-brush-h.md#oh_drawing_brushgetcolor)相比，本接口以浮点数返回颜色分量，精度更高；当画刷颜色通过[OH\_Drawing\_BrushSetColor4f](capi-drawing-brush-h.md#oh_drawing_brushsetcolor4f)设置时，应使用本接口获取蓝色分量以避免精度丢失。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 表示指向[OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)对象的指针。 |
| float\* b | 表示指向浮点数的指针，用于接收画刷颜色的蓝色分量值，取值范围为[0.0, 1.0]。调用前需确保指针指向有效内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数brush或b为NULL。 |
