---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-string
title: OH_Drawing_String
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_String
category: harmonyos-references
scraped_at: 2026-09-02T15:02:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:206e3b104c72a2c832265c22938e35fedbc482fb31df3ebf33a8fd6b0aa7d272
---

```c
typedef struct {...} OH_Drawing_String
```

## 概述

采用UTF-16编码的字符串信息结构体。

**起始版本：** 14

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_types.h](capi-drawing-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t\* strData | 指向包含UTF-16编码的字节数组的指针。 |
| uint32\_t strLen | strData指向的字符串的实际长度，单位为字节。 |
