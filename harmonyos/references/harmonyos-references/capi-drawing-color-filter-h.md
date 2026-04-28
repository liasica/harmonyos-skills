---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-color-filter-h
title: drawing_color_filter.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_color_filter.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:02444044bea188cb7bd67351e7a9e4c27b8dc3de09f1dc2094c5c929681e7a40
---

## 概述

PhonePC/2in1TabletTVWearable

声明与绘图模块中的颜色滤波器对象相关的函数。

**引用文件：** <native\_drawing/drawing\_color\_filter.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateBlendMode(uint32\_t color, OH\_Drawing\_BlendMode blendMode)](capi-drawing-color-filter-h.md#oh_drawing_colorfiltercreateblendmode) | 创建具有混合模式的颜色滤波器。 |
| [OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateCompose(OH\_Drawing\_ColorFilter\* outerColorFilter,OH\_Drawing\_ColorFilter\* innerColorFilter)](capi-drawing-color-filter-h.md#oh_drawing_colorfiltercreatecompose) | 将两个颜色滤波器合成一个新的颜色滤波器。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  outerColorFilter、innerColorFilter任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateMatrix(const float matrix[20])](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-color-filter-h#oh_drawing_colorfiltercreatematrix) | 创建具有5x4颜色矩阵的颜色滤波器。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  matrix为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateLinearToSrgbGamma(void)](capi-drawing-color-filter-h.md#oh_drawing_colorfiltercreatelineartosrgbgamma) | 创建一个从线性颜色空间转换到SRGB颜色空间的颜色滤波器。 |
| [OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateSrgbGammaToLinear(void)](capi-drawing-color-filter-h.md#oh_drawing_colorfiltercreatesrgbgammatolinear) | 创建颜色滤波器将RGB颜色通道应用于SRGB的伽玛曲线。 |
| [OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateLuma(void)](capi-drawing-color-filter-h.md#oh_drawing_colorfiltercreateluma) | 创建一个颜色滤波器将其输入的亮度值乘以透明度通道，并将红色、绿色和蓝色通道设置为零。 |
| [OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateLighting(uint32\_t mulColor, uint32\_t addColor)](capi-drawing-color-filter-h.md#oh_drawing_colorfiltercreatelighting) | 创建一个光照颜色滤波器，此滤波器会将RGB通道的颜色值乘以一种颜色值并加上另一种颜色值，计算结果会被限制在0到255范围内。 |
| [void OH\_Drawing\_ColorFilterDestroy(OH\_Drawing\_ColorFilter\* colorFilter)](capi-drawing-color-filter-h.md#oh_drawing_colorfilterdestroy) | 销毁颜色滤波器对象，并回收该对象占用的内存。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_ColorFilterCreateBlendMode()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateBlendMode(uint32_t color, OH_Drawing_BlendMode blendMode)
```

**描述**

创建具有混合模式的颜色滤波器。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t color | 表示颜色，是一个32位（ARGB）变量。 |
| [OH\_Drawing\_BlendMode](capi-drawing-types-h.md#oh_drawing_blendmode) blendMode | 表示混合模式。支持可选的混合模式具体可见[OH\_Drawing\_BlendMode](capi-drawing-types-h.md#oh_drawing_blendmode)枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md)\* | 返回创建的颜色滤波器对象的指针。 |

### OH\_Drawing\_ColorFilterCreateCompose()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateCompose(OH_Drawing_ColorFilter* outerColorFilter,OH_Drawing_ColorFilter* innerColorFilter)
```

**描述**

将两个颜色滤波器合成一个新的颜色滤波器。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

outerColorFilter、innerColorFilter任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md)\* outerColorFilter | 指向颜色滤波器对象一的指针。 |
| [OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md)\* innerColorFilter | 指向颜色滤波器对象二的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md)\* | 返回创建的颜色滤波器对象的指针。 |

### OH\_Drawing\_ColorFilterCreateMatrix()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateMatrix(const float matrix[20])
```

**描述**

创建具有5x4颜色矩阵的颜色滤波器。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| matrix | 表示矩阵，以长度为20的浮点数组表示。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md)\* | 返回创建的颜色滤波器对象的指针。 |

### OH\_Drawing\_ColorFilterCreateLinearToSrgbGamma()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateLinearToSrgbGamma(void)
```

**描述**

创建一个从线性颜色空间转换到SRGB颜色空间的颜色滤波器。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md)\* | 返回创建的颜色滤波器对象的指针。 |

### OH\_Drawing\_ColorFilterCreateSrgbGammaToLinear()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateSrgbGammaToLinear(void)
```

**描述**

创建颜色滤波器将RGB颜色通道应用于SRGB的伽玛曲线。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md)\* | 返回创建的颜色滤波器对象的指针。 |

### OH\_Drawing\_ColorFilterCreateLuma()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateLuma(void)
```

**描述**

创建一个颜色滤波器将其输入的亮度值乘以透明度通道，并将红色、绿色和蓝色通道设置为零。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md)\* | 返回创建的颜色滤波器对象的指针。 |

### OH\_Drawing\_ColorFilterCreateLighting()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateLighting(uint32_t mulColor, uint32_t addColor)
```

**描述**

创建一个光照颜色滤波器，此滤波器会将RGB通道的颜色值乘以一种颜色值并加上另一种颜色值，计算结果会被限制在0到255范围内。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t mulColor | 用来乘法运算的颜色值。 |
| uint32\_t addColor | 用来加法运算的颜色值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md)\* | 返回创建的颜色滤波器对象的指针。 |

### OH\_Drawing\_ColorFilterDestroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_ColorFilterDestroy(OH_Drawing_ColorFilter* colorFilter)
```

**描述**

销毁颜色滤波器对象，并回收该对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md)\* colorFilter | 表示指向颜色滤波器对象的指针。 |
