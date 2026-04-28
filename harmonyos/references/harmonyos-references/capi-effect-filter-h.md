---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-effect-filter-h
title: effect_filter.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > effect_filter.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:05+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6dd4cb4af89a22ad3b38e569c9251940e70090392d5ba1ff3b8a9fa2f9666766
---

## 概述

PhonePC/2in1TabletTVWearable

声明滤镜效果的接口。

**引用文件：** <native\_effect/effect\_filter.h>

**库：** libnative\_effect.so

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**相关模块：** [effectKit](capi-effectkit.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [EffectErrorCode OH\_Filter\_CreateEffect(OH\_PixelmapNative\* pixelmap, OH\_Filter\*\* filter)](capi-effect-filter-h.md#oh_filter_createeffect) | 创建一个OH\_Filter对象。 |
| [EffectErrorCode OH\_Filter\_Release(OH\_Filter\* filter)](capi-effect-filter-h.md#oh_filter_release) | 释放OH\_Filter对象。 |
| [EffectErrorCode OH\_Filter\_Blur(OH\_Filter\* filter, float radius)](capi-effect-filter-h.md#oh_filter_blur) | 创建一个毛玻璃滤镜效果，然后添加到滤镜里面。 |
| [EffectErrorCode OH\_Filter\_BlurWithTileMode(OH\_Filter\* filter, float radius, EffectTileMode tileMode)](capi-effect-filter-h.md#oh_filter_blurwithtilemode) | 创建一个毛玻璃滤镜效果，然后添加到滤镜里面，支持着色器效果平铺模式选择。 |
| [EffectErrorCode OH\_Filter\_Brighten(OH\_Filter\* filter, float brightness)](capi-effect-filter-h.md#oh_filter_brighten) | 创建一个提亮效果并且添加到滤镜中。 |
| [EffectErrorCode OH\_Filter\_GrayScale(OH\_Filter\* filter)](capi-effect-filter-h.md#oh_filter_grayscale) | 创建一个灰度效果并且添加到滤镜中。 |
| [EffectErrorCode OH\_Filter\_Invert(OH\_Filter\* filter)](capi-effect-filter-h.md#oh_filter_invert) | 创建一个反色效果并且添加到滤镜中。 |
| [EffectErrorCode OH\_Filter\_SetColorMatrix(OH\_Filter\* filter, OH\_Filter\_ColorMatrix\* matrix)](capi-effect-filter-h.md#oh_filter_setcolormatrix) | 通过矩阵创建一个自定义的效果并且添加到滤镜中。 |
| [EffectErrorCode OH\_Filter\_GetEffectPixelMap(OH\_Filter\* filter, OH\_PixelmapNative\*\* pixelmap)](capi-effect-filter-h.md#oh_filter_geteffectpixelmap) | 获取滤镜生成的位图。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Filter\_CreateEffect()

PhonePC/2in1TabletTVWearable

```
1. EffectErrorCode OH_Filter_CreateEffect(OH_PixelmapNative* pixelmap, OH_Filter** filter)
```

**描述**

创建一个OH\_Filter对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-drawing-oh-pixelmapnative.md)\* pixelmap | 创建滤镜的位图。 |
| [OH\_Filter](capi-effectkit-oh-filter.md)\*\* filter | 用来接收滤镜的二级指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [EffectErrorCode](capi-effect-types-h.md#effecterrorcode) | 返回结果参见状态码[EffectErrorCode](capi-effect-types-h.md#effecterrorcode)。 |

### OH\_Filter\_Release()

PhonePC/2in1TabletTVWearable

```
1. EffectErrorCode OH_Filter_Release(OH_Filter* filter)
```

**描述**

释放OH\_Filter对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Filter](capi-effectkit-oh-filter.md)\* filter | 被释放的对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [EffectErrorCode](capi-effect-types-h.md#effecterrorcode) | 返回结果参见状态码[EffectErrorCode](capi-effect-types-h.md#effecterrorcode)。 |

### OH\_Filter\_Blur()

PhonePC/2in1TabletTVWearable

```
1. EffectErrorCode OH_Filter_Blur(OH_Filter* filter, float radius)
```

**描述**

创建一个毛玻璃滤镜效果，然后添加到滤镜里面。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Filter](capi-effectkit-oh-filter.md)\* filter | 滤镜指针。 |
| float radius | 毛玻璃效果的模糊半径，单位为像素。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [EffectErrorCode](capi-effect-types-h.md#effecterrorcode) | 返回结果参见状态码[EffectErrorCode](capi-effect-types-h.md#effecterrorcode)。 |

### OH\_Filter\_BlurWithTileMode()

PhonePC/2in1TabletTVWearable

```
1. EffectErrorCode OH_Filter_BlurWithTileMode(OH_Filter* filter, float radius, EffectTileMode tileMode)
```

**描述**

创建一个毛玻璃滤镜效果，然后添加到滤镜里面，支持着色器效果平铺模式选择。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Filter](capi-effectkit-oh-filter.md)\* filter | 滤镜指针。 |
| float radius | 毛玻璃效果的模糊半径，单位为像素。 |
| [EffectTileMode](capi-effect-types-h.md#effecttilemode) tileMode | 着色器效果平铺模式，支持可选的具体模式可见[EffectTileMode](capi-effect-types-h.md#effecttilemode)枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [EffectErrorCode](capi-effect-types-h.md#effecterrorcode) | 返回结果参见状态码[EffectErrorCode](capi-effect-types-h.md#effecterrorcode)。  操作成功则返回EFFECT\_SUCCESS。  无效参数则返回EFFECT\_BAD\_PARAMETER。 |

### OH\_Filter\_Brighten()

PhonePC/2in1TabletTVWearable

```
1. EffectErrorCode OH_Filter_Brighten(OH_Filter* filter, float brightness)
```

**描述**

创建一个提亮效果并且添加到滤镜中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Filter](capi-effectkit-oh-filter.md)\* filter | 滤镜指针。 |
| float brightness | 提亮效果的亮度值，取值范围在0-1之间，取值为0时图像保持不变，取值为1时图像全白。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [EffectErrorCode](capi-effect-types-h.md#effecterrorcode) | 返回结果参见状态码[EffectErrorCode](capi-effect-types-h.md#effecterrorcode)。 |

### OH\_Filter\_GrayScale()

PhonePC/2in1TabletTVWearable

```
1. EffectErrorCode OH_Filter_GrayScale(OH_Filter* filter)
```

**描述**

创建一个灰度效果并且添加到滤镜中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Filter](capi-effectkit-oh-filter.md)\* filter | 滤镜指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [EffectErrorCode](capi-effect-types-h.md#effecterrorcode) | 返回结果参见状态码[EffectErrorCode](capi-effect-types-h.md#effecterrorcode)。 |

### OH\_Filter\_Invert()

PhonePC/2in1TabletTVWearable

```
1. EffectErrorCode OH_Filter_Invert(OH_Filter* filter)
```

**描述**

创建一个反色效果并且添加到滤镜中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Filter](capi-effectkit-oh-filter.md)\* filter | 滤镜指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [EffectErrorCode](capi-effect-types-h.md#effecterrorcode) | 返回结果参见状态码[EffectErrorCode](capi-effect-types-h.md#effecterrorcode)。 |

### OH\_Filter\_SetColorMatrix()

PhonePC/2in1TabletTVWearable

```
1. EffectErrorCode OH_Filter_SetColorMatrix(OH_Filter* filter, OH_Filter_ColorMatrix* matrix)
```

**描述**

通过矩阵创建一个自定义的效果并且添加到滤镜中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Filter](capi-effectkit-oh-filter.md)\* filter | 滤镜指针。 |
| [OH\_Filter\_ColorMatrix](capi-effectkit-oh-filter-colormatrix.md)\* matrix | 用来创建滤镜的自定义矩阵[OH\_Filter\_ColorMatrix](capi-effectkit-oh-filter-colormatrix.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [EffectErrorCode](capi-effect-types-h.md#effecterrorcode) | 返回结果参见状态码[EffectErrorCode](capi-effect-types-h.md#effecterrorcode)。 |

### OH\_Filter\_GetEffectPixelMap()

PhonePC/2in1TabletTVWearable

```
1. EffectErrorCode OH_Filter_GetEffectPixelMap(OH_Filter* filter, OH_PixelmapNative** pixelmap)
```

**描述**

获取滤镜生成的位图。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Filter](capi-effectkit-oh-filter.md)\* filter | 用来创建位图的滤镜指针。 |
| [OH\_PixelmapNative](capi-drawing-oh-pixelmapnative.md)\*\* pixelmap | 用来接收位图的二级指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [EffectErrorCode](capi-effect-types-h.md#effecterrorcode) | 返回结果参见状态码[EffectErrorCode](capi-effect-types-h.md#effecterrorcode)。 |
