---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-placeholderspan
title: OH_Drawing_PlaceholderSpan
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_PlaceholderSpan
category: harmonyos-references
scraped_at: 2026-09-02T15:02:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6177c400d1df0cee58199ec69798645928dd58c0c197f65c79b020fb7001fb71
---

```c
typedef struct {...} OH_Drawing_PlaceholderSpan
```

## 概述

用于描述占位符跨度的结构体。

**起始版本：** 11

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_text\_typography.h](capi-drawing-text-typography-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| double width | 占位符宽度。 |
| double height | 占位符高度。 |
| [OH\_Drawing\_PlaceholderVerticalAlignment](capi-drawing-text-typography-h.md#oh_drawing_placeholderverticalalignment) alignment | 占位符对齐方式。 |
| [OH\_Drawing\_TextBaseline](capi-drawing-text-typography-h.md#oh_drawing_textbaseline) baseline | 占位符基线。 |
| double baselineOffset | 占位符基线偏移。 |
