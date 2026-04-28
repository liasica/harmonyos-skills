---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-effect-filter-h
title: image_effect_filter.h
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 头文件 > image_effect_filter.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4f6ae141e5715f1ebff79d2b49d3351233e74a923730db4a674297cf201326be
---

## 概述

PhonePC/2in1TabletTV

声明滤镜相关接口。

开发者可以通过滤镜的接口快速实现基本的效果处理，也可以将滤镜添加到效果器中，组合成滤镜链串联执行。系统提供了如“亮度”、“裁剪”等基本的效果处理滤镜。

**引用文件：** <multimedia/image\_effect/image\_effect\_filter.h>

**库：** libimage\_effect.so

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**相关模块：** [ImageEffect](capi-imageeffect.md)

## 汇总

PhonePC/2in1TabletTV

### 结构体

PhonePC/2in1TabletTV

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ImageEffect\_DataValue](capi-imageeffect-imageeffect-datavalue.md) | ImageEffect\_DataValue | 数据值联合体。 |
| [ImageEffect\_Any](capi-imageeffect-imageeffect-any.md) | ImageEffect\_Any | 参数结构体。 |
| [ImageEffect\_FilterNames](capi-imageeffect-imageeffect-filternames.md) | ImageEffect\_FilterNames | 滤镜名信息。 |
| [ImageEffect\_FilterDelegate](capi-imageeffect-imageeffect-filterdelegate.md) | ImageEffect\_FilterDelegate | 自定义滤镜回调函数结构体。 |
| [ImageEffect\_Region](capi-imageeffect-imageeffect-region.md) | ImageEffect\_Region | 图像区域结构体。 |
| [ImageEffect\_Size](capi-imageeffect-imageeffect-size.md) | ImageEffect\_Size | 图像尺寸结构体。 |
| [OH\_EffectFilter](capi-imageeffect-oh-effectfilter.md) | OH\_EffectFilter | 定义滤镜结构类型。 |
| [OH\_EffectFilterInfo](capi-imageeffect-oh-effectfilterinfo.md) | OH\_EffectFilterInfo | 定义滤镜信息结构体。 |
| [OH\_EffectBufferInfo](capi-imageeffect-oh-effectbufferinfo.md) | OH\_EffectBufferInfo | 定义图像信息。 |

### 枚举

PhonePC/2in1TabletTV

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ImageEffect\_DataType](capi-image-effect-filter-h.md#imageeffect_datatype) | ImageEffect\_DataType | 数据类型枚举值。 |
| [ImageEffect\_Format](capi-image-effect-filter-h.md#imageeffect_format) | ImageEffect\_Format | 像素格式枚举值。 |
| [ImageEffect\_BufferType](capi-image-effect-filter-h.md#imageeffect_buffertype) | ImageEffect\_BufferType | 内存类型枚举值。 |

### 宏定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| OH\_EFFECT\_BRIGHTNESS\_FILTER "Brightness" | 亮度滤镜，对应的参数为OH\_EFFECT\_FILTER\_INTENSITY\_KEY，参数类型为[EFFECT\_DATA\_TYPE\_FLOAT](capi-image-effect-filter-h.md#imageeffect_datatype)。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.ImageEffect.Core |
| OH\_EFFECT\_CONTRAST\_FILTER "Contrast" | 对比度滤镜，对应的参数为OH\_EFFECT\_FILTER\_INTENSITY\_KEY，参数类型为[EFFECT\_DATA\_TYPE\_FLOAT](capi-image-effect-filter-h.md#imageeffect_datatype)。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.ImageEffect.Core |
| OH\_EFFECT\_CROP\_FILTER "Crop" | 裁剪滤镜，对应的参数为OH\_EFFECT\_FILTER\_REGION\_KEY，参数类型为[EFFECT\_DATA\_TYPE\_PTR](capi-image-effect-filter-h.md#imageeffect_datatype)，参数值为结构体 [ImageEffect\_Region](capi-imageeffect-imageeffect-region.md)。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.ImageEffect.Core |
| OH\_EFFECT\_FILTER\_INTENSITY\_KEY "FilterIntensity" | 强度参数。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.ImageEffect.Core |
| OH\_EFFECT\_FILTER\_REGION\_KEY "FilterRegion" | 图像区域参数。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.ImageEffect.Core |

### 函数

PhonePC/2in1TabletTV

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_EffectFilterInfo \*OH\_EffectFilterInfo\_Create()](capi-image-effect-filter-h.md#oh_effectfilterinfo_create) | - | 创建OH\_EffectFilterInfo实例，调用[OH\_EffectFilterInfo\_Release](capi-image-effect-filter-h.md#oh_effectfilterinfo_release)进行资源释放。 |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_SetFilterName(OH\_EffectFilterInfo \*info, const char \*name)](capi-image-effect-filter-h.md#oh_effectfilterinfo_setfiltername) | - | 设置滤镜名。 |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_GetFilterName(OH\_EffectFilterInfo \*info, char \*\*name)](capi-image-effect-filter-h.md#oh_effectfilterinfo_getfiltername) | - | 获取滤镜名。 |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_SetSupportedBufferTypes(OH\_EffectFilterInfo \*info, uint32\_t size, ImageEffect\_BufferType \*bufferTypeArray)](capi-image-effect-filter-h.md#oh_effectfilterinfo_setsupportedbuffertypes) | - | 设置滤镜所支持的内存类型。 |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_GetSupportedBufferTypes(OH\_EffectFilterInfo \*info, uint32\_t \*size, ImageEffect\_BufferType \*\*bufferTypeArray)](capi-image-effect-filter-h.md#oh_effectfilterinfo_getsupportedbuffertypes) | - | 获取滤镜所支持的内存类型。 |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_SetSupportedFormats(OH\_EffectFilterInfo \*info, uint32\_t size, ImageEffect\_Format \*formatArray)](capi-image-effect-filter-h.md#oh_effectfilterinfo_setsupportedformats) | - | 设置滤镜所支持的像素格式。 |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_GetSupportedFormats(OH\_EffectFilterInfo \*info, uint32\_t \*size, ImageEffect\_Format \*\*formatArray)](capi-image-effect-filter-h.md#oh_effectfilterinfo_getsupportedformats) | - | 获取滤镜所支持的像素格式。 |
| [ImageEffect\_ErrorCode OH\_EffectFilterInfo\_Release(OH\_EffectFilterInfo \*info)](capi-image-effect-filter-h.md#oh_effectfilterinfo_release) | - | 销毁OH\_EffectFilterInfo实例。 |
| [OH\_EffectBufferInfo \*OH\_EffectBufferInfo\_Create()](capi-image-effect-filter-h.md#oh_effectbufferinfo_create) | - | 创建OH\_EffectBufferInfo实例，调用[OH\_EffectBufferInfo\_Release](capi-image-effect-filter-h.md#oh_effectbufferinfo_release)进行资源释放。 |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetAddr(OH\_EffectBufferInfo \*info, void \*addr)](capi-image-effect-filter-h.md#oh_effectbufferinfo_setaddr) | - | 设置图像内存地址。 |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetAddr(OH\_EffectBufferInfo \*info, void \*\*addr)](capi-image-effect-filter-h.md#oh_effectbufferinfo_getaddr) | - | 获取图像内存地址。 |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetWidth(OH\_EffectBufferInfo \*info, int32\_t width)](capi-image-effect-filter-h.md#oh_effectbufferinfo_setwidth) | - | 设置图像宽度。 |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetWidth(OH\_EffectBufferInfo \*info, int32\_t \*width)](capi-image-effect-filter-h.md#oh_effectbufferinfo_getwidth) | - | 获取图像宽度。 |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetHeight(OH\_EffectBufferInfo \*info, int32\_t height)](capi-image-effect-filter-h.md#oh_effectbufferinfo_setheight) | - | 设置图像高度。 |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetHeight(OH\_EffectBufferInfo \*info, int32\_t \*height)](capi-image-effect-filter-h.md#oh_effectbufferinfo_getheight) | - | 获取图像高度。 |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetRowSize(OH\_EffectBufferInfo \*info, int32\_t rowSize)](capi-image-effect-filter-h.md#oh_effectbufferinfo_setrowsize) | - | 设置图像每一行的字节数。 |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetRowSize(OH\_EffectBufferInfo \*info, int32\_t \*rowSize)](capi-image-effect-filter-h.md#oh_effectbufferinfo_getrowsize) | - | 获取图像每一行的字节数。 |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetEffectFormat(OH\_EffectBufferInfo \*info, ImageEffect\_Format format)](capi-image-effect-filter-h.md#oh_effectbufferinfo_seteffectformat) | - | 设置图像的像素格式。 |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetEffectFormat(OH\_EffectBufferInfo \*info, ImageEffect\_Format \*format)](capi-image-effect-filter-h.md#oh_effectbufferinfo_geteffectformat) | - | 获取图像的像素格式。 |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetTextureId(OH\_EffectBufferInfo \*info, int32\_t textureId)](capi-image-effect-filter-h.md#oh_effectbufferinfo_settextureid) | - | 设置OH\_EffectBufferInfo的图像的textureId。 |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetTextureId(OH\_EffectBufferInfo \*info, int32\_t \*textureId)](capi-image-effect-filter-h.md#oh_effectbufferinfo_gettextureid) | - | 从OH\_EffectBufferInfo中获取图像的textureId。 |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_Release(OH\_EffectBufferInfo \*info)](capi-image-effect-filter-h.md#oh_effectbufferinfo_release) | - | 销毁OH\_EffectBufferInfo实例。 |
| [typedef bool (\*OH\_EffectFilterDelegate\_SetValue)(OH\_EffectFilter \*filter, const char \*key, const ImageEffect\_Any \*value)](capi-image-effect-filter-h.md#oh_effectfilterdelegate_setvalue) | OH\_EffectFilterDelegate\_SetValue | 自定义滤镜设置参数的回调函数，用于开发者校验参数及参数值。 |
| [typedef void (\*OH\_EffectFilterDelegate\_PushData)(OH\_EffectFilter \*filter, OH\_EffectBufferInfo \*info)](capi-image-effect-filter-h.md#oh_effectfilterdelegate_pushdata) | OH\_EffectFilterDelegate\_PushData | 自定义滤镜传递图像信息到下一级滤镜的函数指针。需要在[OH\_EffectFilterDelegate\_Render](capi-image-effect-filter-h.md#oh_effectfilterdelegate_render)的回调中主动调用该函数指针。 |
| [typedef bool (\*OH\_EffectFilterDelegate\_Render)(OH\_EffectFilter \*filter, OH\_EffectBufferInfo \*info, OH\_EffectFilterDelegate\_PushData pushData)](capi-image-effect-filter-h.md#oh_effectfilterdelegate_render) | OH\_EffectFilterDelegate\_Render | 自定义滤镜渲染图像的回调函数。 |
| [typedef bool (\*OH\_EffectFilterDelegate\_Save)(OH\_EffectFilter \*filter, char \*\*info)](capi-image-effect-filter-h.md#oh_effectfilterdelegate_save) | OH\_EffectFilterDelegate\_Save | 自定义滤镜序列化的回调函数，按照JSON格式进行滤镜序列化处理。 |
| [typedef OH\_EffectFilter \*(\*OH\_EffectFilterDelegate\_Restore)(const char \*info)](capi-image-effect-filter-h.md#oh_effectfilterdelegate_restore) | OH\_EffectFilterDelegate\_Restore | 自定义滤镜反序列化的回调函数。 |
| [OH\_EffectFilter \*OH\_EffectFilter\_Create(const char \*name)](capi-image-effect-filter-h.md#oh_effectfilter_create) | - | 创建OH\_EffectFilter实例，调用[OH\_EffectFilter\_Release](capi-image-effect-filter-h.md#oh_effectfilter_release)进行资源释放。 |
| [ImageEffect\_ErrorCode OH\_EffectFilter\_SetValue(OH\_EffectFilter \*filter, const char \*key, const ImageEffect\_Any \*value)](capi-image-effect-filter-h.md#oh_effectfilter_setvalue) | - | 设置滤镜参数。 |
| [ImageEffect\_ErrorCode OH\_EffectFilter\_GetValue(OH\_EffectFilter \*filter, const char \*key, ImageEffect\_Any \*value)](capi-image-effect-filter-h.md#oh_effectfilter_getvalue) | - | 获取滤镜参数。 |
| [ImageEffect\_ErrorCode OH\_EffectFilter\_Register(const OH\_EffectFilterInfo \*info, const ImageEffect\_FilterDelegate \*delegate)](capi-image-effect-filter-h.md#oh_effectfilter_register) | - | 注册自定义滤镜。 |
| [ImageEffect\_FilterNames \*OH\_EffectFilter\_LookupFilters(const char \*key)](capi-image-effect-filter-h.md#oh_effectfilter_lookupfilters) | - | 查询满足条件的滤镜。 |
| [void OH\_EffectFilter\_ReleaseFilterNames()](capi-image-effect-filter-h.md#oh_effectfilter_releasefilternames) | - | 释放滤镜名内存资源。 |
| [ImageEffect\_ErrorCode OH\_EffectFilter\_LookupFilterInfo(const char \*name, OH\_EffectFilterInfo \*info)](capi-image-effect-filter-h.md#oh_effectfilter_lookupfilterinfo) | - | 查询滤镜信息。 |
| [ImageEffect\_ErrorCode OH\_EffectFilter\_Render(OH\_EffectFilter \*filter, OH\_PixelmapNative \*inputPixelmap, OH\_PixelmapNative \*outputPixelmap)](capi-image-effect-filter-h.md#oh_effectfilter_render) | - | 执行图像渲染。 |
| [ImageEffect\_ErrorCode OH\_EffectFilter\_RenderWithTextureId(OH\_EffectFilter \*filter, int32\_t inputTextureId, int32\_t outputTextureId, int32\_t colorSpace)](capi-image-effect-filter-h.md#oh_effectfilter_renderwithtextureid) | - | 使用纹理标识渲染滤镜效果。该函数不支持相同的输入和输出图像。 |
| [ImageEffect\_ErrorCode OH\_EffectFilter\_Release(OH\_EffectFilter \*filter)](capi-image-effect-filter-h.md#oh_effectfilter_release) | - | 销毁OH\_EffectFilter实例。 |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_SetTimestamp(OH\_EffectBufferInfo \*info, int64\_t timestamp)](capi-image-effect-filter-h.md#oh_effectbufferinfo_settimestamp) | - | 设置滤镜时间戳。 |
| [ImageEffect\_ErrorCode OH\_EffectBufferInfo\_GetTimestamp(OH\_EffectBufferInfo \*info, int64\_t \*timestamp)](capi-image-effect-filter-h.md#oh_effectbufferinfo_gettimestamp) | - | 获取滤镜时间戳。 |

## 枚举类型说明

PhonePC/2in1TabletTV

### ImageEffect\_DataType

PhonePC/2in1TabletTV

```
1. enum ImageEffect_DataType
```

**描述**

数据类型枚举值。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| EFFECT\_DATA\_TYPE\_UNKNOWN = 0 | 未定义类型。 |
| EFFECT\_DATA\_TYPE\_INT32 = 1 | 整形。 |
| EFFECT\_DATA\_TYPE\_FLOAT = 2 | 单精度浮点型。 |
| EFFECT\_DATA\_TYPE\_DOUBLE = 3 | 双精度浮点型。 |
| EFFECT\_DATA\_TYPE\_CHAR = 4 | 字节类型。 |
| EFFECT\_DATA\_TYPE\_LONG = 5 | 长整型。 |
| EFFECT\_DATA\_TYPE\_BOOL = 6 | 布尔类型。 |
| EFFECT\_DATA\_TYPE\_PTR = 7 | 指针类型。 |

### ImageEffect\_Format

PhonePC/2in1TabletTV

```
1. enum ImageEffect_Format
```

**描述**

像素格式枚举值。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| EFFECT\_PIXEL\_FORMAT\_UNKNOWN = 0 | 未定义类型。 |
| EFFECT\_PIXEL\_FORMAT\_RGBA8888 = 1 | RGBA8888类型。 |
| EFFECT\_PIXEL\_FORMAT\_NV21 = 2 | NV21类型。 |
| EFFECT\_PIXEL\_FORMAT\_NV12 = 3 | NV12类型。 |
| EFFECT\_PIXEL\_FORMAT\_RGBA1010102 = 4 | 10bit RGBA类型。 |
| EFFECT\_PIXEL\_FORMAT\_YCBCR\_P010 = 5 | 10bit YCBCR420类型。 |
| EFFECT\_PIXEL\_FORMAT\_YCRCB\_P010 = 6 | 10bit YCRCB420类型。 |

### ImageEffect\_BufferType

PhonePC/2in1TabletTV

```
1. enum ImageEffect_BufferType
```

**描述**

内存类型枚举值。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| EFFECT\_BUFFER\_TYPE\_UNKNOWN = 0 | 未定义类型。 |
| EFFECT\_BUFFER\_TYPE\_PIXEL = 1 | 像素图类型。 |
| EFFECT\_BUFFER\_TYPE\_TEXTURE = 2 | 纹理类型。 |

## 函数说明

PhonePC/2in1TabletTV

### OH\_EffectFilterInfo\_Create()

PhonePC/2in1TabletTV

```
1. OH_EffectFilterInfo *OH_EffectFilterInfo_Create()
```

**描述**

创建OH\_EffectFilterInfo实例，调用[OH\_EffectFilterInfo\_Release](capi-image-effect-filter-h.md#oh_effectfilterinfo_release)进行资源释放。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_EffectFilterInfo](capi-imageeffect-oh-effectfilterinfo.md) \* | 返回一个指向OH\_EffectFilterInfo实例的指针，创建失败时返回空指针。 |

### OH\_EffectFilterInfo\_SetFilterName()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectFilterInfo_SetFilterName(OH_EffectFilterInfo *info, const char *name)
```

**描述**

设置滤镜名。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectFilterInfo](capi-imageeffect-oh-effectfilterinfo.md) \*info | 滤镜信息指针。 |
| const char \*name | 滤镜名，例如：OH\_EFFECT\_BRIGHTNESS\_FILTER。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectFilterInfo\_GetFilterName()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectFilterInfo_GetFilterName(OH_EffectFilterInfo *info, char **name)
```

**描述**

获取滤镜名。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectFilterInfo](capi-imageeffect-oh-effectfilterinfo.md) \*info | 滤镜信息指针。 |
| char \*\*name | 指向char数组的指针，返回滤镜名。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectFilterInfo\_SetSupportedBufferTypes()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectFilterInfo_SetSupportedBufferTypes(OH_EffectFilterInfo *info, uint32_t size, ImageEffect_BufferType *bufferTypeArray)
```

**描述**

设置滤镜所支持的内存类型。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectFilterInfo](capi-imageeffect-oh-effectfilterinfo.md) \*info | 滤镜信息指针。 |
| uint32\_t size | 滤镜所支持内存类型[ImageEffect\_BufferType](capi-image-effect-filter-h.md#imageeffect_buffertype)个数。 |
| [ImageEffect\_BufferType](capi-image-effect-filter-h.md#imageeffect_buffertype) \*bufferTypeArray | 滤镜所支持内存类型[ImageEffect\_BufferType](capi-image-effect-filter-h.md#imageeffect_buffertype)数组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectFilterInfo\_GetSupportedBufferTypes()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectFilterInfo_GetSupportedBufferTypes(OH_EffectFilterInfo *info, uint32_t *size, ImageEffect_BufferType **bufferTypeArray)
```

**描述**

获取滤镜所支持的内存类型。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectFilterInfo](capi-imageeffect-oh-effectfilterinfo.md) \*info | 滤镜信息指针。 |
| uint32\_t \*size | 滤镜所支持内存类型[ImageEffect\_BufferType](capi-image-effect-filter-h.md#imageeffect_buffertype)个数。 |
| [ImageEffect\_BufferType](capi-image-effect-filter-h.md#imageeffect_buffertype) \*\*bufferTypeArray | 滤镜所支持内存类型[ImageEffect\_BufferType](capi-image-effect-filter-h.md#imageeffect_buffertype)数组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectFilterInfo\_SetSupportedFormats()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectFilterInfo_SetSupportedFormats(OH_EffectFilterInfo *info, uint32_t size, ImageEffect_Format *formatArray)
```

**描述**

设置滤镜所支持的像素格式。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectFilterInfo](capi-imageeffect-oh-effectfilterinfo.md) \*info | 滤镜信息指针。 |
| uint32\_t size | 滤镜所支持像素格式[ImageEffect\_Format](capi-image-effect-filter-h.md#imageeffect_format)个数。 |
| [ImageEffect\_Format](capi-image-effect-filter-h.md#imageeffect_format) \*formatArray | 滤镜所支持像素格式[ImageEffect\_Format](capi-image-effect-filter-h.md#imageeffect_format)数组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectFilterInfo\_GetSupportedFormats()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectFilterInfo_GetSupportedFormats(OH_EffectFilterInfo *info, uint32_t *size, ImageEffect_Format **formatArray)
```

**描述**

获取滤镜所支持的像素格式。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectFilterInfo](capi-imageeffect-oh-effectfilterinfo.md) \*info | 滤镜信息指针。 |
| uint32\_t \*size | 滤镜所支持像素格式[ImageEffect\_Format](capi-image-effect-filter-h.md#imageeffect_format)个数。 |
| [ImageEffect\_Format](capi-image-effect-filter-h.md#imageeffect_format) \*\*formatArray | 滤镜所支持像素格式[ImageEffect\_Format](capi-image-effect-filter-h.md#imageeffect_format)数组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectFilterInfo\_Release()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectFilterInfo_Release(OH_EffectFilterInfo *info)
```

**描述**

销毁OH\_EffectFilterInfo实例。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectFilterInfo](capi-imageeffect-oh-effectfilterinfo.md) \*info | 滤镜信息指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectBufferInfo\_Create()

PhonePC/2in1TabletTV

```
1. OH_EffectBufferInfo *OH_EffectBufferInfo_Create()
```

**描述**

创建OH\_EffectBufferInfo实例，调用[OH\_EffectBufferInfo\_Release](capi-image-effect-filter-h.md#oh_effectbufferinfo_release)进行资源释放。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_EffectBufferInfo](capi-imageeffect-oh-effectbufferinfo.md) \* | 返回一个指向OH\_EffectBufferInfo实例的指针，创建失败时返回空指针。 |

### OH\_EffectBufferInfo\_SetAddr()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectBufferInfo_SetAddr(OH_EffectBufferInfo *info, void *addr)
```

**描述**

设置图像内存地址。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectBufferInfo](capi-imageeffect-oh-effectbufferinfo.md) \*info | 图像信息指针。 |
| void \*addr | 图像虚拟内存地址。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectBufferInfo\_GetAddr()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectBufferInfo_GetAddr(OH_EffectBufferInfo *info, void **addr)
```

**描述**

获取图像内存地址。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectBufferInfo](capi-imageeffect-oh-effectbufferinfo.md) \*info | 图像信息指针。 |
| void \*\*addr | 图像虚拟内存地址。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectBufferInfo\_SetWidth()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectBufferInfo_SetWidth(OH_EffectBufferInfo *info, int32_t width)
```

**描述**

设置图像宽度。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectBufferInfo](capi-imageeffect-oh-effectbufferinfo.md) \*info | 图像信息指针。 |
| int32\_t width | 图像宽度，单位：像素。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectBufferInfo\_GetWidth()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectBufferInfo_GetWidth(OH_EffectBufferInfo *info, int32_t *width)
```

**描述**

获取图像宽度。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectBufferInfo](capi-imageeffect-oh-effectbufferinfo.md) \*info | 图像信息指针。 |
| int32\_t \*width | 图像宽度，单位：像素。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectBufferInfo\_SetHeight()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectBufferInfo_SetHeight(OH_EffectBufferInfo *info, int32_t height)
```

**描述**

设置图像高度。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectBufferInfo](capi-imageeffect-oh-effectbufferinfo.md) \*info | 图像信息指针。 |
| int32\_t height | 图像高度，单位：像素。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectBufferInfo\_GetHeight()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectBufferInfo_GetHeight(OH_EffectBufferInfo *info, int32_t *height)
```

**描述**

获取图像高度。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectBufferInfo](capi-imageeffect-oh-effectbufferinfo.md) \*info | 图像信息指针。 |
| int32\_t \*height | 图像高度，单位：像素。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectBufferInfo\_SetRowSize()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectBufferInfo_SetRowSize(OH_EffectBufferInfo *info, int32_t rowSize)
```

**描述**

设置图像每一行的字节数。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectBufferInfo](capi-imageeffect-oh-effectbufferinfo.md) \*info | 图像信息指针。 |
| int32\_t rowSize | 图像每一行的字节数，单位：字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectBufferInfo\_GetRowSize()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectBufferInfo_GetRowSize(OH_EffectBufferInfo *info, int32_t *rowSize)
```

**描述**

获取图像每一行的字节数。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectBufferInfo](capi-imageeffect-oh-effectbufferinfo.md) \*info | 图像信息指针。 |
| int32\_t \*rowSize | 图像每一行的字节数，单位：字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectBufferInfo\_SetEffectFormat()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectBufferInfo_SetEffectFormat(OH_EffectBufferInfo *info, ImageEffect_Format format)
```

**描述**

设置图像的像素格式。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectBufferInfo](capi-imageeffect-oh-effectbufferinfo.md) \*info | 图像信息指针。 |
| [ImageEffect\_Format](capi-image-effect-filter-h.md#imageeffect_format) format | 图像像素格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectBufferInfo\_GetEffectFormat()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectBufferInfo_GetEffectFormat(OH_EffectBufferInfo *info, ImageEffect_Format *format)
```

**描述**

获取图像的像素格式。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectBufferInfo](capi-imageeffect-oh-effectbufferinfo.md) \*info | 图像信息指针。 |
| [ImageEffect\_Format](capi-image-effect-filter-h.md#imageeffect_format) \*format | 图像像素格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectBufferInfo\_SetTextureId()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectBufferInfo_SetTextureId(OH_EffectBufferInfo *info, int32_t textureId)
```

**描述**

设置OH\_EffectBufferInfo的图像的textureId。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectBufferInfo](capi-imageeffect-oh-effectbufferinfo.md) \*info | OH\_EffectBufferInfo结构体实例指针。 |
| int32\_t textureId | 图像纹理标识。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：参数缺失。 |

### OH\_EffectBufferInfo\_GetTextureId()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectBufferInfo_GetTextureId(OH_EffectBufferInfo *info, int32_t *textureId)
```

**描述**

从OH\_EffectBufferInfo中获取图像的textureId。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectBufferInfo](capi-imageeffect-oh-effectbufferinfo.md) \*info | OH\_EffectBufferInfo结构体实例指针。 |
| int32\_t \*textureId | 图像纹理标识。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：参数缺失。 |

### OH\_EffectBufferInfo\_Release()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectBufferInfo_Release(OH_EffectBufferInfo *info)
```

**描述**

销毁OH\_EffectBufferInfo实例。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectBufferInfo](capi-imageeffect-oh-effectbufferinfo.md) \*info | 图像信息指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectFilterDelegate\_SetValue()

PhonePC/2in1TabletTV

```
1. typedef bool (*OH_EffectFilterDelegate_SetValue)(OH_EffectFilter *filter, const char *key, const ImageEffect_Any *value)
```

**描述**

自定义滤镜设置参数的回调函数，用于开发者校验参数及参数值。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectFilter](capi-imageeffect-oh-effectfilter.md) \*filter | 滤镜指针。 |
| const char \*key | 滤镜参数。 |
| [const ImageEffect\_Any](capi-imageeffect-imageeffect-any.md) \*value | 滤镜参数值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 参数有效时返回true，否则返回false。 |

### OH\_EffectFilterDelegate\_PushData()

PhonePC/2in1TabletTV

```
1. typedef void (*OH_EffectFilterDelegate_PushData)(OH_EffectFilter *filter, OH_EffectBufferInfo *info)
```

**描述**

自定义滤镜传递图像信息到下一级滤镜的函数指针。需要在[OH\_EffectFilterDelegate\_Render](capi-image-effect-filter-h.md#oh_effectfilterdelegate_render)的回调中主动调用该函数指针。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectFilter](capi-imageeffect-oh-effectfilter.md) \*filter | 滤镜指针。 |
| [OH\_EffectBufferInfo](capi-imageeffect-oh-effectbufferinfo.md) \*info | 图像信息OH\_EffectBufferInfo指针。 |

### OH\_EffectFilterDelegate\_Render()

PhonePC/2in1TabletTV

```
1. typedef bool (*OH_EffectFilterDelegate_Render)(OH_EffectFilter *filter, OH_EffectBufferInfo *info, OH_EffectFilterDelegate_PushData pushData)
```

**描述**

自定义滤镜渲染图像的回调函数。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectFilter](capi-imageeffect-oh-effectfilter.md) \*filter | 滤镜指针。 |
| [OH\_EffectBufferInfo](capi-imageeffect-oh-effectbufferinfo.md) \*info | 图像信息OH\_EffectBufferInfo指针。 |
| [OH\_EffectFilterDelegate\_PushData](capi-image-effect-filter-h.md#oh_effectfilterdelegate_pushdata) pushData | 自定义滤镜传递图像信息到下一级滤镜的函数指针OH\_EffectFilterDelegate\_PushData。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 执行成功时返回true，否则返回false。 |

### OH\_EffectFilterDelegate\_Save()

PhonePC/2in1TabletTV

```
1. typedef bool (*OH_EffectFilterDelegate_Save)(OH_EffectFilter *filter, char **info)
```

**描述**

自定义滤镜序列化的回调函数，按照JSON格式进行滤镜序列化处理。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectFilter](capi-imageeffect-oh-effectfilter.md) \*filter | 滤镜指针。 |
| char \*\*info | 指向char数组的指针，返回序列化JSON字符串。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 执行成功时返回true，否则返回false。 |

### OH\_EffectFilterDelegate\_Restore()

PhonePC/2in1TabletTV

```
1. typedef OH_EffectFilter *(*OH_EffectFilterDelegate_Restore)(const char *info)
```

**描述**

自定义滤镜反序列化的回调函数。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*info | 序列化JSON字符串。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_EffectFilter](capi-imageeffect-oh-effectfilter.md) \* | 执行成功时返回OH\_EffectFilter实例，否则返回空指针。 |

### OH\_EffectFilter\_Create()

PhonePC/2in1TabletTV

```
1. OH_EffectFilter *OH_EffectFilter_Create(const char *name)
```

**描述**

创建OH\_EffectFilter实例，调用[OH\_EffectFilter\_Release](capi-image-effect-filter-h.md#oh_effectfilter_release)进行资源释放。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*name | 滤镜名，例如：OH\_EFFECT\_BRIGHTNESS\_FILTER。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_EffectFilter](capi-imageeffect-oh-effectfilter.md) \* | 返回一个指向OH\_EffectFilter实例的指针，创建失败时返回空指针。 |

### OH\_EffectFilter\_SetValue()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectFilter_SetValue(OH_EffectFilter *filter, const char *key, const ImageEffect_Any *value)
```

**描述**

设置滤镜参数。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectFilter](capi-imageeffect-oh-effectfilter.md) \*filter | 滤镜指针。 |
| const char \*key | 滤镜参数，例如：OH\_EFFECT\_FILTER\_INTENSITY\_KEY。 |
| [const ImageEffect\_Any](capi-imageeffect-imageeffect-any.md) \*value | 滤镜参数值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。  EFFECT\_KEY\_ERROR：参数无效。  EFFECT\_PARAM\_ERROR：参数值无效。 |

### OH\_EffectFilter\_GetValue()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectFilter_GetValue(OH_EffectFilter *filter, const char *key, ImageEffect_Any *value)
```

**描述**

获取滤镜参数。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectFilter](capi-imageeffect-oh-effectfilter.md) \*filter | 滤镜指针。 |
| const char \*key | 滤镜参数，例如：OH\_EFFECT\_FILTER\_INTENSITY\_KEY。 |
| [ImageEffect\_Any](capi-imageeffect-imageeffect-any.md) \*value | 滤镜参数值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。  EFFECT\_KEY\_ERROR：参数无效。 |

### OH\_EffectFilter\_Register()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectFilter_Register(const OH_EffectFilterInfo *info, const ImageEffect_FilterDelegate *delegate)
```

**描述**

注册自定义滤镜。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_EffectFilterInfo](capi-imageeffect-oh-effectfilterinfo.md) \*info | 滤镜信息指针OH\_EffectFilterInfo。 |
| [const ImageEffect\_FilterDelegate](capi-imageeffect-imageeffect-filterdelegate.md) \*delegate | 自定义滤镜回调函数ImageEffect\_FilterDelegate。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectFilter\_LookupFilters()

PhonePC/2in1TabletTV

```
1. ImageEffect_FilterNames *OH_EffectFilter_LookupFilters(const char *key)
```

**描述**

查询满足条件的滤镜。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*key | 查询条件，可根据“Default”关键词查询所有的滤镜。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_FilterNames](capi-imageeffect-imageeffect-filternames.md) \* | 滤镜名列表。 |

### OH\_EffectFilter\_ReleaseFilterNames()

PhonePC/2in1TabletTV

```
1. void OH_EffectFilter_ReleaseFilterNames()
```

**描述**

释放滤镜名内存资源。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

### OH\_EffectFilter\_LookupFilterInfo()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectFilter_LookupFilterInfo(const char *name, OH_EffectFilterInfo *info)
```

**描述**

查询滤镜信息。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*name | 滤镜名。 |
| [OH\_EffectFilterInfo](capi-imageeffect-oh-effectfilterinfo.md) \*info | 滤镜信息指针OH\_EffectFilterInfo。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针或其他无效值。 |

### OH\_EffectFilter\_Render()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectFilter_Render(OH_EffectFilter *filter, OH_PixelmapNative *inputPixelmap, OH_PixelmapNative *outputPixelmap)
```

**描述**

执行图像渲染。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectFilter](capi-imageeffect-oh-effectfilter.md) \*filter | 滤镜指针。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*inputPixelmap | 输入图像。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*outputPixelmap | 输出图像。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectFilter\_RenderWithTextureId()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectFilter_RenderWithTextureId(OH_EffectFilter *filter, int32_t inputTextureId, int32_t outputTextureId, int32_t colorSpace)
```

**描述**

使用纹理标识渲染滤镜效果。该函数不支持相同的输入和输出图像。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectFilter](capi-imageeffect-oh-effectfilter.md) \*filter | OH\_EffectFilter结构体实例指针。 |
| int32\_t inputTextureId | 输入纹理标识。输入的纹理标识必须是有效的且绑定了GL\_TEXTURE\_2D类型的纹理。 |
| int32\_t outputTextureId | 输出纹理标识，输入纹理标识必须是一个有效的纹理。  如果纹理标识未被绑定纹理图片，纹理标识会自动绑定GL\_TEXTURE\_2D类型；  如果纹理标识已经被绑定纹理且尺寸不合适，结果可能会被裁剪或部分填充到此纹理上。 |
| int32\_t colorSpace | 图片对应的色彩空间。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：参数缺失。 |

### OH\_EffectFilter\_Release()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectFilter_Release(OH_EffectFilter *filter)
```

**描述**

销毁OH\_EffectFilter实例。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectFilter](capi-imageeffect-oh-effectfilter.md) \*filter | 滤镜指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectBufferInfo\_SetTimestamp()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectBufferInfo_SetTimestamp(OH_EffectBufferInfo *info, int64_t timestamp)
```

**描述**

设置滤镜时间戳。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectBufferInfo](capi-imageeffect-oh-effectbufferinfo.md) \*info | 图像信息指针。 |
| int64\_t timestamp | 图像帧数据的时间戳。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |

### OH\_EffectBufferInfo\_GetTimestamp()

PhonePC/2in1TabletTV

```
1. ImageEffect_ErrorCode OH_EffectBufferInfo_GetTimestamp(OH_EffectBufferInfo *info, int64_t *timestamp)
```

**描述**

获取滤镜时间戳。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_EffectBufferInfo](capi-imageeffect-oh-effectbufferinfo.md) \*info | 图像信息指针。 |
| int64\_t \*timestamp | 图像帧数据的时间戳。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ImageEffect\_ErrorCode](capi-image-effect-errors-h.md#imageeffect_errorcode) | EFFECT\_SUCCESS：方法调用成功。  EFFECT\_ERROR\_PARAM\_INVALID：入参为空指针。 |
