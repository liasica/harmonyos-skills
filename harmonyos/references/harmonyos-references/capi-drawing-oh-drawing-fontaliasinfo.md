---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontaliasinfo
title: OH_Drawing_FontAliasInfo
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_FontAliasInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c5649b9dfcca56130d44807766fb49d20d36a809ac9be5ee9cadae40d40bfa3d
---

```c
typedef struct OH_Drawing_FontAliasInfo {...} OH_Drawing_FontAliasInfo
```

## 概述

别名字体信息结构体。

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_text\_typography.h](capi-drawing-text-typography-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char\* familyName | 字体家族名。 |
| int weight | 字体字重值，当字重值大于0时，表示此字体集只包含所指定字重的字体，当字重值等于0时，表示此字体集包含所有字体。 |
