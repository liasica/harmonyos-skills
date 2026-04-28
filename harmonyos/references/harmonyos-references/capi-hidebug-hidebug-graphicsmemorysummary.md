---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-graphicsmemorysummary
title: HiDebug_GraphicsMemorySummary
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiDebug_GraphicsMemorySummary
category: harmonyos-references
scraped_at: 2026-04-28T08:11:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3f8309e1c86acce5cda4d64a3bf1fd0ccca93da30152afb05b79510ab9ae597f
---

```
1. typedef struct HiDebug_GraphicsMemorySummary {...} HiDebug_GraphicsMemorySummary
```

## 概述

PhonePC/2in1TabletTVWearable

应用图形显存占用详情的结构定义。

**起始版本：** 21

**相关模块：** [HiDebug](capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](capi-hidebug-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t gl | gl内存大小，RenderService渲染进程加载所需资源占用的内存，例如图片、纹理等，以KB为单位。 |
| uint32\_t graph | graph内存大小，进程统计的DMA内存占用，包括直接通过接口申请的DMA buffer和通过allocator\_host申请的DMA buffer，以KB为单位。 |
