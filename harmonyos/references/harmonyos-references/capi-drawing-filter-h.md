---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-filter-h
title: drawing_filter.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_filter.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:53+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:597d5e92c529e6ec63515b30fc3d7dcb86daead10611e4def7b1d37159ae8e3a
---

## 概述

PhonePC/2in1TabletTVWearable

声明与绘图模块中的滤波器对象相关的函数。

**引用文件：** <native\_drawing/drawing\_filter.h>

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
| [OH\_Drawing\_Filter\* OH\_Drawing\_FilterCreate(void)](capi-drawing-filter-h.md#oh_drawing_filtercreate) | 创建一个滤波器对象。 |
| [void OH\_Drawing\_FilterSetImageFilter(OH\_Drawing\_Filter\* filter, OH\_Drawing\_ImageFilter\* imageFilter)](capi-drawing-filter-h.md#oh_drawing_filtersetimagefilter) | 为滤波器对象设置图像滤波器对象。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  filter为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_FilterSetMaskFilter(OH\_Drawing\_Filter\* filter, OH\_Drawing\_MaskFilter\* maskFilter)](capi-drawing-filter-h.md#oh_drawing_filtersetmaskfilter) | 为滤波器对象设置蒙版滤波器对象。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  filter为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_FilterSetColorFilter(OH\_Drawing\_Filter\* filter, OH\_Drawing\_ColorFilter\* colorFilter)](capi-drawing-filter-h.md#oh_drawing_filtersetcolorfilter) | 为滤波器对象设置颜色滤波器对象。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  filter为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_FilterGetColorFilter(OH\_Drawing\_Filter\* filter, OH\_Drawing\_ColorFilter\* colorFilter)](capi-drawing-filter-h.md#oh_drawing_filtergetcolorfilter) | 从滤波器对象获取颜色滤波器对象。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  filter、colorFilter任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_FilterDestroy(OH\_Drawing\_Filter\* filter)](capi-drawing-filter-h.md#oh_drawing_filterdestroy) | 销毁滤波器对象，并收回该对象占用的内存。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_FilterCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Filter* OH_Drawing_FilterCreate(void)
```

**描述**

创建一个滤波器对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)\* | 返回创建的滤波器对象的指针。 |

### OH\_Drawing\_FilterSetImageFilter()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FilterSetImageFilter(OH_Drawing_Filter* filter, OH_Drawing_ImageFilter* imageFilter)
```

**描述**

为滤波器对象设置图像滤波器对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

filter为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)\* filter | 指示指向滤波器对象[OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)的指针。 |
| [OH\_Drawing\_ImageFilter](capi-drawing-oh-drawing-imagefilter.md)\* imageFilter | 指示指向图像滤波器[OH\_Drawing\_ImageFilter](capi-drawing-oh-drawing-imagefilter.md)对象的指针，为NULL表示清空滤波器对象中的图像滤波器效果。 |

### OH\_Drawing\_FilterSetMaskFilter()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FilterSetMaskFilter(OH_Drawing_Filter* filter, OH_Drawing_MaskFilter* maskFilter)
```

**描述**

为滤波器对象设置蒙版滤波器对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

filter为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)\* filter | 指示指向滤波器对象[OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)的指针。 |
| [OH\_Drawing\_MaskFilter](capi-drawing-oh-drawing-maskfilter.md)\* maskFilter | 指示指向蒙版滤波器对象[OH\_Drawing\_MaskFilter](capi-drawing-oh-drawing-maskfilter.md)的指针，为NULL表示清空滤波器对象中的蒙版滤波器效果。 |

### OH\_Drawing\_FilterSetColorFilter()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FilterSetColorFilter(OH_Drawing_Filter* filter, OH_Drawing_ColorFilter* colorFilter)
```

**描述**

为滤波器对象设置颜色滤波器对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

filter为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)\* filter | 指示指向滤波器对象[OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)的指针。 |
| [OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md)\* colorFilter | 指示指向颜色滤波器对象[OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md)的指针，为NULL表示清空滤波器对象中的颜色滤波器效果。 |

### OH\_Drawing\_FilterGetColorFilter()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FilterGetColorFilter(OH_Drawing_Filter* filter, OH_Drawing_ColorFilter* colorFilter)
```

**描述**

从滤波器对象获取颜色滤波器对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

filter、colorFilter任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)\* filter | 指示指向滤波器对象[OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)的指针。 |
| [OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md)\* colorFilter | 指示指向颜色滤波器对象[OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md)的指针。 |

### OH\_Drawing\_FilterDestroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FilterDestroy(OH_Drawing_Filter* filter)
```

**描述**

销毁滤波器对象，并收回该对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)\* filter | 指示指向滤波器对象[OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md)的指针。 |
