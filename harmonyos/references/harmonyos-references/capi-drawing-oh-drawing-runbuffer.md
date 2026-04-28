---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-runbuffer
title: OH_Drawing_RunBuffer
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_RunBuffer
category: harmonyos-references
scraped_at: 2026-04-28T08:15:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7e4b9d9aecb0d25940cf8d7a609c1bf255eb8f8f77bf6fb39f51aa7f6f15550d
---

```
1. typedef struct {...} OH_Drawing_RunBuffer
```

## 概述

PhonePC/2in1TabletTVWearable

结构体用于描述一块内存，描述文字和位置信息。

**起始版本：** 11

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_text\_blob.h](capi-drawing-text-blob-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint16\_t\* glyphs | 存储文字索引。 |
| float\* pos | 存储文字的位置。 |
| char\* utf8text | 存储文字UTF-8编码。 |
| uint32\_t\* clusters | 存储文字簇UTF-8编码（簇指的是集合）。 |
