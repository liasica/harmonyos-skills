---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-surface-h
title: drawing_surface.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_surface.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:39b07b1d23705ce5e3570f2152d87d1d379124087c1385465bba013b22823472
---

## 概述

本文件定义了与surface相关的功能函数，包括surface的创建、销毁和使用等。surface对象用于管理画布绘制的内容，支持通过图形处理器上下文创建离屏surface和与屏幕窗口绑定的surface。

本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**引用文件：** <native\_drawing/drawing\_surface.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_Surface\* OH\_Drawing\_SurfaceCreateFromGpuContext(OH\_Drawing\_GpuContext\* gpuContext, bool flag, OH\_Drawing\_Image\_Info imageInfo)](capi-drawing-surface-h.md#oh_drawing_surfacecreatefromgpucontext) | 使用图形处理器上下文创建离屏surface对象，用于管理画布绘制的内容。若需将绘制内容上屏显示（配合[OH\_Drawing\_SurfaceFlush](capi-drawing-surface-h.md#oh_drawing_surfaceflush)使用），请改用[OH\_Drawing\_SurfaceCreateOnScreen](capi-drawing-surface-h.md#oh_drawing_surfacecreateonscreen)创建与屏幕窗口绑定的surface对象。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  gpuContext为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_Surface\* OH\_Drawing\_SurfaceCreateOnScreen(OH\_Drawing\_GpuContext\* gpuContext, OH\_Drawing\_Image\_Info imageInfo, void\* window)](capi-drawing-surface-h.md#oh_drawing_surfacecreateonscreen) | 使用图形处理器上下文创建一个与屏幕窗口绑定的surface对象，用于管理画布绘制的内容。若不需要上屏显示，请改用[OH\_Drawing\_SurfaceCreateFromGpuContext](capi-drawing-surface-h.md#oh_drawing_surfacecreatefromgpucontext)创建离屏surface对象。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  gpuContext或window为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。  imageInfo的宽高和window的宽高需保持一致，否则对象创建失败。 |
| [OH\_Drawing\_Canvas\* OH\_Drawing\_SurfaceGetCanvas(OH\_Drawing\_Surface\* surface)](capi-drawing-surface-h.md#oh_drawing_surfacegetcanvas) | 通过surface对象获取画布对象。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  surface为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SurfaceFlush(OH\_Drawing\_Surface\* surface)](capi-drawing-surface-h.md#oh_drawing_surfaceflush) | 将surface对象上的画布绘制内容提交给图形处理器处理，完成绘制内容上屏显示。 |
| [void OH\_Drawing\_SurfaceDestroy(OH\_Drawing\_Surface\* surface)](capi-drawing-surface-h.md#oh_drawing_surfacedestroy) | 销毁surface对象并回收该对象占用的内存。调用本接口销毁surface对象后，通过[OH\_Drawing\_SurfaceGetCanvas](capi-drawing-surface-h.md#oh_drawing_surfacegetcanvas)获取的画布对象不应再使用，其生命周期由surface对象管理。 |

## 函数说明

### OH\_Drawing\_SurfaceCreateFromGpuContext()

```c
OH_Drawing_Surface* OH_Drawing_SurfaceCreateFromGpuContext(OH_Drawing_GpuContext* gpuContext, bool flag, OH_Drawing_Image_Info imageInfo)
```

**描述**

使用图形处理器上下文创建离屏surface对象，用于管理画布绘制的内容。若需将绘制内容上屏显示（配合[OH\_Drawing\_SurfaceFlush](capi-drawing-surface-h.md#oh_drawing_surfaceflush)使用），请改用[OH\_Drawing\_SurfaceCreateOnScreen](capi-drawing-surface-h.md#oh_drawing_surfacecreateonscreen)创建与屏幕窗口绑定的surface对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

gpuContext为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_GpuContext](capi-drawing-oh-drawing-gpucontext.md)\* gpuContext | 指向图形处理器上下文对象[OH\_Drawing\_GpuContext](capi-drawing-oh-drawing-gpucontext.md)的指针。 |
| bool flag | 用于控制内存分配是否计入缓存预算。true则计入缓存预算，false则不计入缓存预算。缓存预算为图形处理器缓存可使用的内存上限，计入预算的内存分配会占用缓存额度。当需要将绘制内容纳入缓存管理以提升性能时，flag设置为true；当绘制内容为临时数据、不需要长期缓存时，flag设置为false。 |
| [OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md) imageInfo | 图像信息[OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md)结构体，用于指定所创建surface的图像宽度、高度、颜色类型和透明度类型等属性。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Surface](capi-drawing-oh-drawing-surface.md)\* | 返回指向创建的surface对象[OH\_Drawing\_Surface](capi-drawing-oh-drawing-surface.md)的指针。 |

### OH\_Drawing\_SurfaceCreateOnScreen()

```c
OH_Drawing_Surface* OH_Drawing_SurfaceCreateOnScreen(OH_Drawing_GpuContext* gpuContext, OH_Drawing_Image_Info imageInfo, void* window)
```

**描述**

使用图形处理器上下文创建一个与屏幕窗口绑定的surface对象，用于管理画布绘制的内容。若不需要上屏显示，请改用[OH\_Drawing\_SurfaceCreateFromGpuContext](capi-drawing-surface-h.md#oh_drawing_surfacecreatefromgpucontext)创建离屏surface对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

gpuContext或window为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

imageInfo的宽高和window的宽高需保持一致，否则对象创建失败。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 16

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_GpuContext](capi-drawing-oh-drawing-gpucontext.md)\* gpuContext | 指向图形处理器上下文对象[OH\_Drawing\_GpuContext](capi-drawing-oh-drawing-gpucontext.md)的指针。 |
| [OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md) imageInfo | 图像信息[OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md)结构体，用于指定所创建surface的图像宽度、高度、颜色类型和透明度类型等属性。 |
| void\* window | 指向屏幕窗口对象（OHNativeWindow）的指针，实际应传入OHNativeWindow\*类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Surface](capi-drawing-oh-drawing-surface.md)\* | 返回指向创建的surface对象[OH\_Drawing\_Surface](capi-drawing-oh-drawing-surface.md)的指针。 |

### OH\_Drawing\_SurfaceGetCanvas()

```c
OH_Drawing_Canvas* OH_Drawing_SurfaceGetCanvas(OH_Drawing_Surface* surface)
```

**描述**

通过surface对象获取画布对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

surface为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Surface](capi-drawing-oh-drawing-surface.md)\* surface | 指向已创建的surface对象的指针[OH\_Drawing\_Surface](capi-drawing-oh-drawing-surface.md)，用于从中获取画布对象。该surface对象可由[OH\_Drawing\_SurfaceCreateFromGpuContext](capi-drawing-surface-h.md#oh_drawing_surfacecreatefromgpucontext)或[OH\_Drawing\_SurfaceCreateOnScreen](capi-drawing-surface-h.md#oh_drawing_surfacecreateonscreen)创建。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* | 返回指向获取的画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。返回的指针不需要由调用者管理，其生命周期由对应的surface对象管理。调用[OH\_Drawing\_SurfaceDestroy](capi-drawing-surface-h.md#oh_drawing_surfacedestroy)销毁surface对象后，不应再使用该画布对象。 |

### OH\_Drawing\_SurfaceFlush()

```c
OH_Drawing_ErrorCode OH_Drawing_SurfaceFlush(OH_Drawing_Surface* surface)
```

**描述**

将surface对象上的画布绘制内容提交给图形处理器处理，完成绘制内容上屏显示。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 16

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Surface](capi-drawing-oh-drawing-surface.md)\* surface | 指向创建的surface对象的指针[OH\_Drawing\_Surface](capi-drawing-oh-drawing-surface.md)。该surface对象必须由[OH\_Drawing\_SurfaceCreateOnScreen](capi-drawing-surface-h.md#oh_drawing_surfacecreateonscreen)创建，否则该接口调用不会将绘制内容上屏显示。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数surface为NULL。 |

### OH\_Drawing\_SurfaceDestroy()

```c
void OH_Drawing_SurfaceDestroy(OH_Drawing_Surface* surface)
```

**描述**

销毁surface对象并回收该对象占用的内存。调用本接口销毁surface对象后，通过[OH\_Drawing\_SurfaceGetCanvas](capi-drawing-surface-h.md#oh_drawing_surfacegetcanvas)获取的画布对象不应再使用，其生命周期由surface对象管理。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Surface](capi-drawing-oh-drawing-surface.md)\* surface | 指向待销毁的surface对象的指针[OH\_Drawing\_Surface](capi-drawing-oh-drawing-surface.md)。该surface对象可由[OH\_Drawing\_SurfaceCreateFromGpuContext](capi-drawing-surface-h.md#oh_drawing_surfacecreatefromgpucontext)或[OH\_Drawing\_SurfaceCreateOnScreen](capi-drawing-surface-h.md#oh_drawing_surfacecreateonscreen)创建，销毁后该指针不应再被使用。 |
