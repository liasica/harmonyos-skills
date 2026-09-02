---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-rectstyle-info
title: OH_Drawing_RectStyle_Info
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_RectStyle_Info
category: harmonyos-references
scraped_at: 2026-09-02T15:02:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:46d181d5613fb7a9d5ae4967194e41ecb313e0d974c251e7014fd99e0dbde621
---

```c
typedef struct {...} OH_Drawing_RectStyle_Info
```

## 概述

定义矩形框样式结构体。

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_types.h](capi-drawing-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t color | 矩形框的颜色。 |
| double leftTopRadius | 矩形框的左上半径。 |
| double rightTopRadius | 矩形框的右上半径。 |
| double rightBottomRadius | 矩形框的右下半径。 |
| double leftBottomRadius | 矩形框的左下半径。 |
