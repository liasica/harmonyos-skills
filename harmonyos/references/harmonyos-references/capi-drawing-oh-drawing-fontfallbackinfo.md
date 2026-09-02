---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontfallbackinfo
title: OH_Drawing_FontFallbackInfo
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_FontFallbackInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8b7a9d953758613579405ecd114a7d3450e810006d6af0b5016af20c3a5a06bd
---

```c
typedef struct OH_Drawing_FontFallbackInfo {...} OH_Drawing_FontFallbackInfo
```

## 概述

备用字体信息结构体。

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_text\_typography.h](capi-drawing-text-typography-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char\* language | 字体集所支持的语言类型，语言格式为bcp47。 |
| char\* familyName | 字体家族名。 |
