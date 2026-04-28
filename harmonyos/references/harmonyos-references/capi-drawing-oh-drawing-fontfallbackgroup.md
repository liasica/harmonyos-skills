---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontfallbackgroup
title: OH_Drawing_FontFallbackGroup
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_FontFallbackGroup
category: harmonyos-references
scraped_at: 2026-04-28T08:15:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:df8e278dd28d9cac8e1ec7d217d7662e7a4d431ff8b168c4cb603fd5d5d6bd07
---

```
1. typedef struct OH_Drawing_FontFallbackGroup {...} OH_Drawing_FontFallbackGroup
```

## 概述

PhonePC/2in1TabletTVWearable

备用字体集信息结构体。

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_text\_typography.h](capi-drawing-text-typography-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char\* groupName | 备用字体集所对应的字体集名称，如果值为空，表示可以使用备用字体集列表集所有的字体。 |
| size\_t fallbackInfoSize | 备用字体集数量。 |
| [OH\_Drawing\_FontFallbackInfo](capi-drawing-oh-drawing-fontfallbackinfo.md)\* fallbackInfoSet | 备用字体字体集列表。 |
