---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-buffer-handle-h
title: buffer_handle.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > buffer_handle.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a6a5fb7a5b8e1369fbebb9b9ea9bd5e6d1d4a001f796adfe7b940f5f1aa564d6
---

## 概述

定义NativeWindow模块使用的BufferHandle的结构体。

**引用文件：** <native\_window/buffer\_handle.h>

**库：** libnative\_window.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**相关模块：** [NativeWindow](capi-nativewindow.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [BufferHandle](capi-nativewindow-bufferhandle.md) | BufferHandle | 缓冲区句柄，用于对缓冲区的信息传递和获取。句柄包含了缓冲区的文件描述符、尺寸、格式、用途、虚拟地址、共享内存键、物理地址、自定义数据。 |
