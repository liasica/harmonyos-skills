---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontadjustinfo
title: OH_Drawing_FontAdjustInfo
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_FontAdjustInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c004a62984c49aefb0fa8d1411b6c6194e6c7fc8fe457a87c353f84fe66b4fbc
---

```c
typedef struct OH_Drawing_FontAdjustInfo {...} OH_Drawing_FontAdjustInfo
```

## 概述

字重映射信息结构体。

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_text\_typography.h](capi-drawing-text-typography-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int weight | 字体原本的字重值。 |
| int to | 字体在应用中显示的字重值。 |
