---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-memory-stream-h
title: drawing_memory_stream.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_memory_stream.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9d5df2128823cca5cffb363705070025370c12527df18ca6134a30c250545d26
---

## 概述

文件中定义了与内存流相关的功能函数，支持基于内存数据创建和销毁内存流对象。内存流支持数据拷贝或直接引用两种访问方式。

本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**引用文件：** <native\_drawing/drawing\_memory\_stream.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_MemoryStream\* OH\_Drawing\_MemoryStreamCreate(const void\* data, size\_t length, bool copyData)](capi-drawing-memory-stream-h.md#oh_drawing_memorystreamcreate) | 创建一个内存流对象，用于将内存中的数据封装为流，可作为数据源供图形处理接口（如图像解码）等后续绘制接口使用。创建的内存流对象使用完毕后，需要调用[OH\_Drawing\_MemoryStreamDestroy()](capi-drawing-memory-stream-h.md#oh_drawing_memorystreamdestroy)销毁并回收内存。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  data为NULL或者length等于0时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_MemoryStreamDestroy(OH\_Drawing\_MemoryStream\* memoryStream)](capi-drawing-memory-stream-h.md#oh_drawing_memorystreamdestroy) | 销毁由[OH\_Drawing\_MemoryStreamCreate()](capi-drawing-memory-stream-h.md#oh_drawing_memorystreamcreate)创建的内存流对象并回收该对象占用的内存。 |

## 函数说明

### OH\_Drawing\_MemoryStreamCreate()

```c
OH_Drawing_MemoryStream* OH_Drawing_MemoryStreamCreate(const void* data, size_t length, bool copyData)
```

**描述**

创建一个内存流对象，用于将内存中的数据封装为流，可作为数据源供图形处理接口（如图像解码）等后续绘制接口使用。创建的内存流对象使用完毕后，需要调用[OH\_Drawing\_MemoryStreamDestroy()](capi-drawing-memory-stream-h.md#oh_drawing_memorystreamdestroy)销毁并回收内存。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

data为NULL或者length等于0时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const void\* data | 要创建内存流的数据缓冲区，数据为二进制字节流，长度由length参数指定，单位为字节。data不能为NULL，为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。当copyData为false时，调用者还需确保data指向的数据在内存流对象生命周期内保持有效。 |
| size\_t length | 数据段长度，单位为字节，取值必须大于0。为0时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| bool copyData | 是否拷贝数据。true表示内存流对象会拷贝一份数据段数据，false表示内存流对象直接使用数据段数据，不拷贝。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_MemoryStream](capi-drawing-oh-drawing-memorystream.md)\* | 指向创建的内存流对象[OH\_Drawing\_MemoryStream](capi-drawing-oh-drawing-memorystream.md)的指针，可作为数据源传递给后续图形处理接口（如图像解码）使用。 |

### OH\_Drawing\_MemoryStreamDestroy()

```c
void OH_Drawing_MemoryStreamDestroy(OH_Drawing_MemoryStream* memoryStream)
```

**描述**

销毁由[OH\_Drawing\_MemoryStreamCreate()](capi-drawing-memory-stream-h.md#oh_drawing_memorystreamcreate)创建的内存流对象并回收该对象占用的内存。销毁后不应再访问内存流对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_MemoryStream](capi-drawing-oh-drawing-memorystream.md)\* memoryStream | 指向内存流对象[OH\_Drawing\_MemoryStream](capi-drawing-oh-drawing-memorystream.md)的指针。 |
