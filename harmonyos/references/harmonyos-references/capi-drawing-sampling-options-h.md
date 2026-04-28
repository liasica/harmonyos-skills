---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-sampling-options-h
title: drawing_sampling_options.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_sampling_options.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:59+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1449812fcc033900ac5aca99a389121a7942f985d74e35187165b496fc415bd8
---

## 概述

PhonePC/2in1TabletTVWearable

文件中定义了与采样相关的功能函数。用于图片或者纹理等图像的采样。

**引用文件：** <native\_drawing/drawing\_sampling\_options.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_FilterMode](capi-drawing-sampling-options-h.md#oh_drawing_filtermode) | OH\_Drawing\_FilterMode | 过滤模式枚举。 |
| [OH\_Drawing\_MipmapMode](capi-drawing-sampling-options-h.md#oh_drawing_mipmapmode) | OH\_Drawing\_MipmapMode | 多级渐远纹理模式枚举。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_SamplingOptions\* OH\_Drawing\_SamplingOptionsCreate(OH\_Drawing\_FilterMode filterMode,OH\_Drawing\_MipmapMode mipmapMode)](capi-drawing-sampling-options-h.md#oh_drawing_samplingoptionscreate) | 创建一个采样选项对象。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  mipmapMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [OH\_Drawing\_SamplingOptions\* OH\_Drawing\_SamplingOptionsCopy(OH\_Drawing\_SamplingOptions\* samplingOptions)](capi-drawing-sampling-options-h.md#oh_drawing_samplingoptionscopy) | 创建一个采样选项对象副本[OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)，用于拷贝一个已有采样选项对象。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  samplingOptions为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_SamplingOptionsDestroy(OH\_Drawing\_SamplingOptions\* samplingOptions)](capi-drawing-sampling-options-h.md#oh_drawing_samplingoptionsdestroy) | 销毁采样选项对象并回收该对象占有内存。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_FilterMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_FilterMode
```

**描述**

过滤模式枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| FILTER\_MODE\_NEAREST | 邻近过滤模式。 |
| FILTER\_MODE\_LINEAR | 线性过滤模式。 |

### OH\_Drawing\_MipmapMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_MipmapMode
```

**描述**

多级渐远纹理模式枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| MIPMAP\_MODE\_NONE | 忽略多级渐远纹理级别。 |
| MIPMAP\_MODE\_NEAREST | 邻近多级渐远级别采样。 |
| MIPMAP\_MODE\_LINEAR | 两个邻近多级渐远纹理之间，线性插值采样。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_SamplingOptionsCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_SamplingOptions* OH_Drawing_SamplingOptionsCreate(OH_Drawing_FilterMode filterMode,OH_Drawing_MipmapMode mipmapMode)
```

**描述**

创建一个采样选项对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

mipmapMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FilterMode](capi-drawing-sampling-options-h.md#oh_drawing_filtermode) filterMode | 过滤采样模式[OH\_Drawing\_FilterMode](capi-drawing-sampling-options-h.md#oh_drawing_filtermode)。 |
| [OH\_Drawing\_MipmapMode](capi-drawing-sampling-options-h.md#oh_drawing_mipmapmode) mipmapMode | 多级渐远纹理采样模式[OH\_Drawing\_MipmapMode](capi-drawing-sampling-options-h.md#oh_drawing_mipmapmode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)\* | 函数会返回一个指针，指针指向创建的采样选项对象[OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)。 |

### OH\_Drawing\_SamplingOptionsCopy()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_SamplingOptions* OH_Drawing_SamplingOptionsCopy(OH_Drawing_SamplingOptions* samplingOptions)
```

**描述**

创建一个采样选项对象副本[OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)，用于拷贝一个已有采样选项对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

samplingOptions为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)\* samplingOptions | 指向采样选项对象[OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_Drawing\_SamplingOptions\* | 函数会返回一个指针，指针指向创建的采样选项对象副本[OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)。如果对象返回NULL，表示创建失败；可能的原因是可用内存为空，或者是samplingOptions为NULL。 |

### OH\_Drawing\_SamplingOptionsDestroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_SamplingOptionsDestroy(OH_Drawing_SamplingOptions* samplingOptions)
```

**描述**

销毁采样选项对象并回收该对象占有内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)\* samplingOptions | 指向采样选项对象[OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)的指针。 |
