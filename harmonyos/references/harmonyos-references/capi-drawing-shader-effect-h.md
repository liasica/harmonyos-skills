---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-shader-effect-h
title: drawing_shader_effect.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_shader_effect.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:59+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:a97de715799d13999ad511949af226da9ec1a5c3aa51eb029574c2ef49cf687e
---

## 概述

PhonePC/2in1TabletTVWearable

声明与绘图模块中的着色器对象相关的函数。

**引用文件：** <native\_drawing/drawing\_shader\_effect.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode) | OH\_Drawing\_TileMode | 着色器效果平铺模式的枚举。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateColorShader(const uint32\_t color)](capi-drawing-shader-effect-h.md#oh_drawing_shadereffectcreatecolorshader) | 创建具有单一颜色的着色器。 |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateLinearGradient(const OH\_Drawing\_Point\* startPt,const OH\_Drawing\_Point\* endPt, const uint32\_t\* colors,const float\* pos, uint32\_t size, OH\_Drawing\_TileMode tileMode)](capi-drawing-shader-effect-h.md#oh_drawing_shadereffectcreatelineargradient) | 创建着色器，在两个指定点之间生成线性渐变。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  startPt、endPt、colors任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  tileMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateLinearGradientWithLocalMatrix(const OH\_Drawing\_Point2D\* startPt, const OH\_Drawing\_Point2D\* endPt, const uint32\_t\* colors, const float\* pos,uint32\_t size, OH\_Drawing\_TileMode tileMode, const OH\_Drawing\_Matrix\* matrix)](capi-drawing-shader-effect-h.md#oh_drawing_shadereffectcreatelineargradientwithlocalmatrix) | 创建着色器，在两个指定点之间生成线性渐变。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  startPt、endPt、colors任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  tileMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateRadialGradient(const OH\_Drawing\_Point\* centerPt, float radius,const uint32\_t\* colors, const float\* pos, uint32\_t size, OH\_Drawing\_TileMode tileMode)](capi-drawing-shader-effect-h.md#oh_drawing_shadereffectcreateradialgradient) | 创建着色器，在给定圆心和半径的情况下生成径向渐变。  从起点到终点颜色从内到外进行圆形渐变（从中间向外拉）被称为径向渐变。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  centerPt、colors任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  tileMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateRadialGradientWithLocalMatrix(const OH\_Drawing\_Point2D\* centerPt, float radius, const uint32\_t\* colors, const float\* pos, uint32\_t size,OH\_Drawing\_TileMode tileMode, const OH\_Drawing\_Matrix\* matrix)](capi-drawing-shader-effect-h.md#oh_drawing_shadereffectcreateradialgradientwithlocalmatrix) | 创建着色器，在给定圆心和半径的情况下生成径向渐变。  从起点到终点颜色从内到外进行圆形渐变（从中间向外拉）被称为径向渐变。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  centerPt、colors任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  tileMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateSweepGradientWithLocalMatrix(const OH\_Drawing\_Point\* centerPt,const uint32\_t\* colors, const float\* pos, uint32\_t size, OH\_Drawing\_TileMode tileMode, const OH\_Drawing\_Matrix\* matrix)](capi-drawing-shader-effect-h.md#oh_drawing_shadereffectcreatesweepgradientwithlocalmatrix) | 创建着色器，在给定中心的情况下结合矩阵变换生成扇形渐变。  颜色从0°到360°渐变被称为扇形渐变。 |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateSweepGradient(const OH\_Drawing\_Point\* centerPt,const uint32\_t\* colors, const float\* pos, uint32\_t size, OH\_Drawing\_TileMode tileMode)](capi-drawing-shader-effect-h.md#oh_drawing_shadereffectcreatesweepgradient) | 创建着色器，在给定中心的情况下生成扇形渐变。  颜色从0°到360°渐变被称为扇形渐变。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  centerPt、colors任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  tileMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateImageShader(OH\_Drawing\_Image\* image,OH\_Drawing\_TileMode tileX, OH\_Drawing\_TileMode tileY, const OH\_Drawing\_SamplingOptions\* samplingOptions,const OH\_Drawing\_Matrix\* matrix)](capi-drawing-shader-effect-h.md#oh_drawing_shadereffectcreateimageshader) | 创建图像着色器。此接口不建议用于录制类型的画布，会影响性能。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  image、samplingOptions任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  tileX、tileY任意一个不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateTwoPointConicalGradient(const OH\_Drawing\_Point2D\* startPt,float startRadius, const OH\_Drawing\_Point2D\* endPt, float endRadius, const uint32\_t\* colors, const float\* pos,uint32\_t size, OH\_Drawing\_TileMode tileMode, const OH\_Drawing\_Matrix\* matrix)](capi-drawing-shader-effect-h.md#oh_drawing_shadereffectcreatetwopointconicalgradient) | 创建着色器，在给定两个圆之间生成渐变。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  startPt、endPt、colors任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  tileMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateCompose(OH\_Drawing\_ShaderEffect\* dst,OH\_Drawing\_ShaderEffect\* src, OH\_Drawing\_BlendMode mode)](capi-drawing-shader-effect-h.md#oh_drawing_shadereffectcreatecompose) | 按照指定的混合模式对两个着色器进行叠加，生成一个新的着色器。 |
| [void OH\_Drawing\_ShaderEffectDestroy(OH\_Drawing\_ShaderEffect\* shaderEffect)](capi-drawing-shader-effect-h.md#oh_drawing_shadereffectdestroy) | 销毁着色器对象，并收回该对象占用的内存。 |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreatePixelMapShader(OH\_Drawing\_PixelMap\* pixelMap,OH\_Drawing\_TileMode tileX, OH\_Drawing\_TileMode tileY, const OH\_Drawing\_SamplingOptions\* samplingOptions,const OH\_Drawing\_Matrix\* matrix)](capi-drawing-shader-effect-h.md#oh_drawing_shadereffectcreatepixelmapshader) | 创建像素图着色器。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_TileMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_TileMode
```

**描述**

着色器效果平铺模式的枚举。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| CLAMP | 如果着色器效果超出其原始边界，则复制边缘颜色。 |
| REPEAT | 在水平和垂直方向上重复着色器效果图像。 |
| MIRROR | 水平和垂直重复着色器效果图像，交替镜像。 |
| DECAL | 只在原始区域内绘制，其他地方返回透明黑色。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_ShaderEffectCreatePixelMapShader()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ShaderEffect* OH_Drawing_ShaderEffectCreatePixelMapShader(OH_Drawing_PixelMap* pixelMap,OH_Drawing_TileMode tileX, OH_Drawing_TileMode tileY, const OH_Drawing_SamplingOptions* samplingOptions,const OH_Drawing_Matrix* matrix)
```

**描述**

创建像素图着色器。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_PixelMap](capi-drawing-oh-drawing-pixelmap.md)\* pixelMap | 指向像素图[OH\_Drawing\_PixelMap](capi-drawing-oh-drawing-pixelmap.md)的指针。 |
| [OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode) tileX | 水平方向着色器效果平铺模式类型，支持可选的具体模式可见[OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode)枚举。 |
| [OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode) tileY | 垂直方向着色器效果平铺模式类型，支持可选的具体模式可见[OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode)枚举。 |
| [const OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)\* samplingOptions | 指向采样选项对象[OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)的指针。 |
| [const OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)\* matrix | 指向矩阵对象[OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)的指针。如果矩阵指针为空，默认传入单位矩阵。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_Drawing\_ShaderEffect\* | 返回创建的着色器对象的指针。 |

### OH\_Drawing\_ShaderEffectCreateColorShader()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ShaderEffect* OH_Drawing_ShaderEffectCreateColorShader(const uint32_t color)
```

**描述**

创建具有单一颜色的着色器。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const uint32\_t color | 表示着色器的ARGB格式颜色，该参数为32位无符号整数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)\* | 函数会返回一个指针，指针指向创建的着色器对象[OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)。如果对象返回NULL，表示创建失败；可能的原因是可用内存为空。 |

### OH\_Drawing\_ShaderEffectCreateLinearGradient()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ShaderEffect* OH_Drawing_ShaderEffectCreateLinearGradient(const OH_Drawing_Point* startPt,const OH_Drawing_Point* endPt, const uint32_t* colors,const float* pos, uint32_t size, OH_Drawing_TileMode tileMode)
```

**描述**

创建着色器，在两个指定点之间生成线性渐变。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

startPt、endPt、colors任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

tileMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md)\* startPt | 表示渐变的起点。 |
| const [OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md)\* endPt | 表示渐变的终点。 |
| const uint32\_t\* colors | 表示在两个点之间分布的颜色。 |
| const float\* pos | 表示colors中每个对应颜色的相对位置，数组长度需和colors保持一致。如果pos为NULL，颜色均匀分布在起点和终点之间。 |
| uint32\_t size | 表示颜色数组的长度（即元素个数），范围为[0, 256]，长度为0时，表示无渐变效果。 |
| [OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode) tileMode | 着色器效果平铺模式类型，支持可选的具体模式可见[OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode)枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)\* | 返回创建的着色器对象的指针。 |

### OH\_Drawing\_ShaderEffectCreateLinearGradientWithLocalMatrix()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ShaderEffect* OH_Drawing_ShaderEffectCreateLinearGradientWithLocalMatrix(const OH_Drawing_Point2D* startPt, const OH_Drawing_Point2D* endPt, const uint32_t* colors, const float* pos,uint32_t size, OH_Drawing_TileMode tileMode, const OH_Drawing_Matrix* matrix)
```

**描述**

创建着色器，在两个指定点之间生成线性渐变。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

startPt、endPt、colors任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

tileMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Point2D](capi-drawing-oh-drawing-point2d.md)\* startPt | 表示渐变的起点。 |
| const [OH\_Drawing\_Point2D](capi-drawing-oh-drawing-point2d.md)\* endPt | 表示渐变的终点。 |
| const uint32\_t\* colors | 表示在两个点之间分布的颜色。 |
| const float\* pos | 表示colors中每个对应颜色的相对位置，数组长度需和colors保持一致。如果pos为NULL，颜色均匀分布在起点和终点之间。 |
| uint32\_t size | 表示颜色数组的长度（即元素个数），范围为[0, 256]，长度为0时，表示无渐变效果。 |
| [OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode) tileMode | 着色器效果平铺模式类型，支持可选的具体模式可见[OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode)枚举。 |
| const [OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)\* matrix | 表示作用于着色器上的矩阵变换，如果matrix是NULL, 默认是一个单位矩阵。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)\* | 函数会返回一个指针，指针指向创建的着色器对象[OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)。如果对象返回NULL，表示创建失败；可能的原因是可用内存为空，或者是startPt、endPt、colors至少一个为NULL。 |

### OH\_Drawing\_ShaderEffectCreateRadialGradient()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ShaderEffect* OH_Drawing_ShaderEffectCreateRadialGradient(const OH_Drawing_Point* centerPt, float radius,const uint32_t* colors, const float* pos, uint32_t size, OH_Drawing_TileMode tileMode)
```

**描述**

创建着色器，在给定圆心和半径的情况下生成径向渐变。

从起点到终点颜色从内到外进行圆形渐变（从中间向外拉）被称为径向渐变。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

centerPt、colors任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

tileMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md)\* centerPt | 表示渐变的圆心。 |
| float radius | 表示渐变的半径，需为非负数。 |
| const uint32\_t\* colors | 表示在径向上分布的颜色。 |
| const float\* pos | 表示colors中每个对应颜色的相对位置，数组长度需和colors保持一致。如果pos为NULL，颜色均匀分布在径向上。 |
| uint32\_t size | 表示颜色数组的长度（即元素个数），范围为[0, 256]，长度为0时，表示无渐变效果。 |
| [OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode) tileMode | 着色器效果平铺模式类型，支持可选的具体模式可见[OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode)枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)\* | 返回创建的着色器对象的指针。 |

### OH\_Drawing\_ShaderEffectCreateRadialGradientWithLocalMatrix()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ShaderEffect* OH_Drawing_ShaderEffectCreateRadialGradientWithLocalMatrix(const OH_Drawing_Point2D* centerPt, float radius, const uint32_t* colors, const float* pos, uint32_t size,OH_Drawing_TileMode tileMode, const OH_Drawing_Matrix* matrix)
```

**描述**

创建着色器，在给定圆心和半径的情况下生成径向渐变。

从起点到终点颜色从内到外进行圆形渐变（从中间向外拉）被称为径向渐变。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

centerPt、colors任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

tileMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Point2D](capi-drawing-oh-drawing-point2d.md)\* centerPt | 表示渐变的圆心。 |
| float radius | 表示渐变的半径。 |
| const uint32\_t\* colors | 表示在径向上分布的颜色。 |
| const float\* pos | 表示colors中每个对应颜色的相对位置，数组长度需和colors保持一致。如果pos为NULL，颜色均匀分布在径向上。 |
| uint32\_t size | 表示颜色数组的长度（即元素个数），范围为[0, 256]，长度为0时，表示无渐变效果。 |
| [OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode) tileMode | 着色器效果平铺模式类型，支持可选的具体模式可见[OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode)枚举。 |
| const [OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)\* matrix | 表示作用于着色器上的矩阵变换，如果matrix是NULL, 默认是一个单位矩阵。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)\* | 函数会返回一个指针，指针指向创建的着色器对象[OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)。如果对象返回NULL，表示创建失败；可能的原因是可用内存为空，或者是centerPt、colors至少一个为NULL。 |

### OH\_Drawing\_ShaderEffectCreateSweepGradientWithLocalMatrix()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ShaderEffect* OH_Drawing_ShaderEffectCreateSweepGradientWithLocalMatrix(const OH_Drawing_Point* centerPt,const uint32_t* colors, const float* pos, uint32_t size, OH_Drawing_TileMode tileMode, const OH_Drawing_Matrix* matrix)
```

**描述**

创建着色器，在给定中心的情况下结合矩阵变换生成扇形渐变。

颜色从0°到360°渐变被称为扇形渐变。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md)\* centerPt | 表示渐变的圆心。 |
| const uint32\_t\* colors | 表示在两个点之间分布的颜色。 |
| const float\* pos | 表示colors中每个对应颜色的相对位置，数组长度需和colors保持一致。如果pos为NULL，颜色均匀分布在0°和360°之间。 |
| uint32\_t size | 表示颜色数组的长度（即元素个数），范围为[0, 256]，长度为0时，表示无渐变效果。 |
| [OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode) tileMode | 着色器效果平铺模式类型，支持可选的具体模式可见[OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode)枚举。 |
| const [OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)\* matrix | 表示作用于着色器上的矩阵变换，如果matrix是NULL, 默认是一个单位矩阵。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)\* | 函数会返回一个指针，指针指向创建的着色器对象[OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)。  存在以下任意一种情况时，会返回空指针：1.可用内存为空；2.centerPt、colors任意为空；3.tileMode超出枚举范围。 |

### OH\_Drawing\_ShaderEffectCreateSweepGradient()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ShaderEffect* OH_Drawing_ShaderEffectCreateSweepGradient(const OH_Drawing_Point* centerPt,const uint32_t* colors, const float* pos, uint32_t size, OH_Drawing_TileMode tileMode)
```

**描述**

创建着色器，在给定中心的情况下生成扇形渐变。

颜色从0°到360°渐变被称为扇形渐变。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

centerPt、colors任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

tileMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md)\* centerPt | 表示渐变的圆心。 |
| const uint32\_t\* colors | 表示在两个点之间分布的颜色。 |
| const float\* pos | 表示colors中每个对应颜色的相对位置，数组长度需和colors保持一致。如果pos为NULL，颜色均匀分布在0°和360°之间。 |
| uint32\_t size | 表示颜色数组的长度（即元素个数），范围为[0, 256]，长度为0时，表示无渐变效果。 |
| [OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode) tileMode | 着色器效果平铺模式类型，支持可选的具体模式可见[OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode)枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)\* | 函数会返回一个指针，指针指向创建的着色器对象[OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)。  存在以下任意一种情况时，会返回空指针：1.可用内存为空；2.centerPt、colors任意为空；3.tileMode超出枚举范围。 |

### OH\_Drawing\_ShaderEffectCreateImageShader()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ShaderEffect* OH_Drawing_ShaderEffectCreateImageShader(OH_Drawing_Image* image,OH_Drawing_TileMode tileX, OH_Drawing_TileMode tileY, const OH_Drawing_SamplingOptions* samplingOptions,const OH_Drawing_Matrix* matrix)
```

**描述**

创建图像着色器。此接口不建议用于录制类型的画布，会影响性能。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

image、samplingOptions任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

tileX、tileY任意一个不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Image](capi-drawing-oh-drawing-image.md)\* image | 指向图片对象[OH\_Drawing\_Image](capi-drawing-oh-drawing-image.md)的指针。 |
| [OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode) tileX | 水平方向着色器效果平铺模式类型，支持可选的具体模式可见[OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode)枚举。 |
| [OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode) tileY | 垂直方向着色器效果平铺模式类型，支持可选的具体模式可见[OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode)枚举。 |
| const [OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)\* samplingOptions | 指向采样选项对象[OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)的指针。 |
| const [OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)\* matrix | 指向矩阵对象[OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)的指针。如果矩阵指针为空，默认传入单位矩阵。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)\* | 函数会返回一个指针，指针指向创建的着色器对象[OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)。  存在以下任意一种情况时，会返回空指针：1.可用内存为空；2.image、samplingOptions任意为空；3.tileX、tileY超出枚举范围。 |

### OH\_Drawing\_ShaderEffectCreateTwoPointConicalGradient()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ShaderEffect* OH_Drawing_ShaderEffectCreateTwoPointConicalGradient(const OH_Drawing_Point2D* startPt,float startRadius, const OH_Drawing_Point2D* endPt, float endRadius, const uint32_t* colors, const float* pos,uint32_t size, OH_Drawing_TileMode tileMode, const OH_Drawing_Matrix* matrix)
```

**描述**

创建着色器，在给定两个圆之间生成渐变。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

startPt、endPt、colors任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

tileMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Point2D](capi-drawing-oh-drawing-point2d.md)\* startPt | 表示渐变的起点圆心。 |
| float startRadius | 表示渐变的起点半径，需为非负数。 |
| const [OH\_Drawing\_Point2D](capi-drawing-oh-drawing-point2d.md)\* endPt | 表示渐变的终点圆心。 |
| float endRadius | 表示渐变的终点半径，需为非负数。 |
| const uint32\_t\* colors | 表示在两个圆之间分布的颜色。 |
| const float\* pos | 表示colors中每个对应颜色的相对位置，数组长度需和colors保持一致。如果pos为NULL，颜色均匀分布在两个圆之间。 |
| uint32\_t size | 表示颜色数组的长度（即元素个数），范围为[0, 256]，长度为0时，表示无渐变效果。 |
| [OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode) tileMode | 着色器效果平铺模式类型，支持可选的具体模式可见[OH\_Drawing\_TileMode](capi-drawing-shader-effect-h.md#oh_drawing_tilemode)枚举。 |
| const [OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)\* matrix | 表示作用于着色器上的矩阵变换，如果matrix是NULL, 默认是一个单位矩阵。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)\* | 函数会返回一个指针，指针指向创建的着色器对象[OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)。如果对象返回NULL，表示创建失败；可能的原因是：1.可用内存为空；2.startPt、endPt、colors任意为空；3.tileMode超出枚举范围。 |

### OH\_Drawing\_ShaderEffectCreateCompose()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ShaderEffect* OH_Drawing_ShaderEffectCreateCompose(OH_Drawing_ShaderEffect* dst,OH_Drawing_ShaderEffect* src, OH_Drawing_BlendMode mode)
```

**描述**

按照指定的混合模式对两个着色器进行叠加，生成一个新的着色器。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)\* dst | 在混合模式中作为目标色的着色器。 |
| [OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)\* src | 在混合模式中作为源色的着色器。 |
| [OH\_Drawing\_BlendMode](capi-drawing-types-h.md#oh_drawing_blendmode) mode | 混合模式[OH\_Drawing\_BlendMode](capi-drawing-types-h.md#oh_drawing_blendmode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)\* | 函数会返回一个指针，指针指向创建的着色器对象[OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)。  当可用内存为空，或者是dst、src任意一个为空，或mode超出枚举范围时，结果返回NULL，表示创建失败。 |

### OH\_Drawing\_ShaderEffectDestroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_ShaderEffectDestroy(OH_Drawing_ShaderEffect* shaderEffect)
```

**描述**

销毁着色器对象，并收回该对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md)\* shaderEffect | 表示指向着色器对象的指针。 |
