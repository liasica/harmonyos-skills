---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-gpu-context-h
title: drawing_gpu_context.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_gpu_context.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1bf7ac451c7a4a289f19246cbb612967c9998f1dd9e4b332f6c4f795929b1c26
---

## 概述

声明与绘图模块中的图形处理器上下文对象相关的函数，用于创建、配置和销毁图形处理器上下文对象，为绘图模块提供图形处理器加速渲染所需的上下文环境。

本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**引用文件：** <native\_drawing/drawing\_gpu\_context.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_GpuContextOptions](capi-drawing-oh-drawing-gpucontextoptions.md) | OH\_Drawing\_GpuContextOptions | 定义有关图形处理器上下文的选项。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_GpuContext\* OH\_Drawing\_GpuContextCreateFromGL(OH\_Drawing\_GpuContextOptions gpuContextOptions)](capi-drawing-gpu-context-h.md#oh_drawing_gpucontextcreatefromgl) | 用于创建一个使用OpenGL作为后端接口的图形处理器上下文对象。创建的图形处理器上下文对象使用完毕后，需要调用[OH\_Drawing\_GpuContextDestroy](capi-drawing-gpu-context-h.md#oh_drawing_gpucontextdestroy)销毁并回收内存。 |
| [OH\_Drawing\_GpuContext\* OH\_Drawing\_GpuContextCreate(void)](capi-drawing-gpu-context-h.md#oh_drawing_gpucontextcreate) | 用于创建一个图形处理器上下文对象，使用的后端类型取决于运行设备。创建的图形处理器上下文对象使用完毕后，需要调用[OH\_Drawing\_GpuContextDestroy](capi-drawing-gpu-context-h.md#oh_drawing_gpucontextdestroy)销毁并回收内存。 |
| [void OH\_Drawing\_GpuContextDestroy(OH\_Drawing\_GpuContext\* gpuContext)](capi-drawing-gpu-context-h.md#oh_drawing_gpucontextdestroy) | 用于销毁图形处理器上下文对象并回收该对象占用的内存。调用后该图形处理器上下文对象指针失效，不可再次使用或重复调用。 |

## 函数说明

### OH\_Drawing\_GpuContextCreateFromGL()

```c
OH_Drawing_GpuContext* OH_Drawing_GpuContextCreateFromGL(OH_Drawing_GpuContextOptions gpuContextOptions)
```

**描述**

用于创建一个使用OpenGL作为后端接口的图形处理器上下文对象。创建的图形处理器上下文对象使用完毕后，需要调用[OH\_Drawing\_GpuContextDestroy](capi-drawing-gpu-context-h.md#oh_drawing_gpucontextdestroy)销毁并回收内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**废弃版本：** 18

**替代接口：** [OH\_Drawing\_GpuContextCreate](capi-drawing-gpu-context-h.md#oh_drawing_gpucontextcreate)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_GpuContextOptions](capi-drawing-oh-drawing-gpucontextoptions.md) gpuContextOptions | 图形处理器上下文选项[OH\_Drawing\_GpuContextOptions](capi-drawing-oh-drawing-gpucontextoptions.md)，用于配置所创建的图形处理器上下文对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_GpuContext](capi-drawing-oh-drawing-gpucontext.md)\* | 返回指向创建的图形处理器上下文对象[OH\_Drawing\_GpuContext](capi-drawing-oh-drawing-gpucontext.md)的指针。 |

### OH\_Drawing\_GpuContextCreate()

```c
OH_Drawing_GpuContext* OH_Drawing_GpuContextCreate(void)
```

**描述**

用于创建一个图形处理器上下文对象，使用的后端类型取决于运行设备。创建的图形处理器上下文对象使用完毕后，需要调用[OH\_Drawing\_GpuContextDestroy](capi-drawing-gpu-context-h.md#oh_drawing_gpucontextdestroy)销毁并回收内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 16

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_GpuContext](capi-drawing-oh-drawing-gpucontext.md)\* | 返回指向创建的图形处理器上下文对象[OH\_Drawing\_GpuContext](capi-drawing-oh-drawing-gpucontext.md)的指针。 |

### OH\_Drawing\_GpuContextDestroy()

```c
void OH_Drawing_GpuContextDestroy(OH_Drawing_GpuContext* gpuContext)
```

**描述**

用于销毁图形处理器上下文对象并回收该对象占用的内存。调用后该图形处理器上下文对象指针失效，不可再次使用或重复调用。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_GpuContext](capi-drawing-oh-drawing-gpucontext.md)\* gpuContext | 指向图形处理器上下文对象的指针。调用后该指针失效，不可再次使用，否则可能导致未定义行为或程序崩溃。 |
