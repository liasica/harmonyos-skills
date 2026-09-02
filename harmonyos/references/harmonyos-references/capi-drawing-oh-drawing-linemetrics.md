---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-linemetrics
title: OH_Drawing_LineMetrics
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_LineMetrics
category: harmonyos-references
scraped_at: 2026-09-02T15:02:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:42890bab582c62a23c4184e42a651313b4b3f5ce184c99d7a0cede0451adcf16
---

```c
typedef struct OH_Drawing_LineMetrics {...} OH_Drawing_LineMetrics
```

## 概述

文字行位置信息。

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_text\_typography.h](capi-drawing-text-typography-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| double ascender | 文字相对于基线以上取绝对值后的高度。 |
| double descender | 文字相对于基线以下取绝对值后的高度。 |
| double capHeight | 大写字母的高度。 |
| double xHeight | 小写字母的高度。 |
| double width | 文字宽度。 |
| double height | 行高。 |
| double x | 文字左端到容器左端距离，左对齐为0，右对齐为容器宽度减去行文字宽度。 |
| double y | 文字上端到容器上端高度，第一行为0，第二行为第一行高度。 |
| size\_t startIndex | 行起始位置字符索引。 |
| size\_t endIndex | 行结束位置字符索引。 |
| [OH\_Drawing\_Font\_Metrics](capi-drawing-oh-drawing-font-metrics.md) firstCharMetrics | 第一个字的度量信息。 |
