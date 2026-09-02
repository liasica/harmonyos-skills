---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-gpucontextoptions
title: OH_Drawing_GpuContextOptions
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_GpuContextOptions
category: harmonyos-references
scraped_at: 2026-09-02T15:02:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f216c5ae3ca09fe286ec9849641c1efe795124e75147e15e9f07ad858b0e5de2
---

```c
typedef struct {...} OH_Drawing_GpuContextOptions
```

## 概述

定义有关图形处理器上下文的选项。

**起始版本：** 12

**废弃版本：** 18

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_gpu\_context.h](capi-drawing-gpu-context-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| bool allowPathMaskCaching | 用于控制是否启用路径蒙版缓存，如果为true，则允许缓存路径蒙版纹理，如果为false，则不允许。 |
