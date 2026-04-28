---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontaliasinfo
title: OH_Drawing_FontAliasInfo
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_FontAliasInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:15:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:91f5bb3d8fce0b556fcce13075920115ab4a2f5c9a2d10397510b9b0a65e2719
---

```
1. typedef struct OH_Drawing_FontAliasInfo {...} OH_Drawing_FontAliasInfo
```

## 概述

PhonePC/2in1TabletTVWearable

别名字体信息结构体。

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_text\_typography.h](capi-drawing-text-typography-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char\* familyName | 字体家族名。 |
| int weight | 字体字重值，当字重值大于0时，表示此字体集只包含所指定weight的字体，当字重值等于0时，表示此字体集包含所有字体。 |
