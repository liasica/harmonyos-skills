---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontfallbackgroup
title: OH_Drawing_FontFallbackGroup
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_FontFallbackGroup
category: harmonyos-references
scraped_at: 2026-09-02T15:02:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f6e6b7672e2d2f6a340d10b7990b5ad1cfb605f45bec817e90f1564696697f98
---

```c
typedef struct OH_Drawing_FontFallbackGroup {...} OH_Drawing_FontFallbackGroup
```

## 概述

备用字体集信息结构体。

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_text\_typography.h](capi-drawing-text-typography-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char\* groupName | 备用字体集所对应的字体集名称，如果值为空，表示可以使用备用字体集列表中所有的字体。 |
| size\_t fallbackInfoSize | 备用字体集数量。 |
| [OH\_Drawing\_FontFallbackInfo](capi-drawing-oh-drawing-fontfallbackinfo.md)\* fallbackInfoSet | 备用字体集列表。 |
