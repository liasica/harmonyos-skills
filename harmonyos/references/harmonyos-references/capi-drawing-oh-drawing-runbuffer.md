---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-runbuffer
title: OH_Drawing_RunBuffer
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_RunBuffer
category: harmonyos-references
scraped_at: 2026-09-02T15:02:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:915893a4923e1d269151910f784fa3344657a05cc8a07559cd530fce2c88cb50
---

```c
typedef struct {...} OH_Drawing_RunBuffer
```

## 概述

结构体用于描述一块内存，描述文字和位置信息。

**起始版本：** 11

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_text\_blob.h](capi-drawing-text-blob-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint16\_t\* glyphs | 存储字形索引。 |
| float\* pos | 存储文字的位置。单位为物理像素px。 |
| char\* utf8text | 存储文字UTF-8编码。 |
| uint32\_t\* clusters | 存储文字簇UTF-8编码（簇指的是集合）。 |
