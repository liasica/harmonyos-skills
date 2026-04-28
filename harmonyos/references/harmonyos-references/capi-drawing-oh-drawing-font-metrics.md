---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-font-metrics
title: OH_Drawing_Font_Metrics
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_Font_Metrics
category: harmonyos-references
scraped_at: 2026-04-28T08:15:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0625744f0af12b0c6faa1d0d1bc9fc55130effa666a14c1a5a84853e5e1281ae
---

```
1. typedef struct OH_Drawing_Font_Metrics {...} OH_Drawing_Font_Metrics
```

## 概述

PhonePC/2in1TabletTVWearable

定义字体度量信息的结构体。

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_font.h](capi-drawing-font-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t flags | 指示哪些度量是有效的。 |
| float top | 字符最高点到基线的最大距离。 |
| float ascent | 字符最高点到基线的推荐距离。 |
| float descent | 字符最低点到基线的推荐距离。 |
| float bottom | 字符最低点到基线的最大距离。 |
| float leading | 行间距。 |
| float avgCharWidth | 平均字符宽度，如果未知则为零。 |
| float maxCharWidth | 最大字符宽度，如果未知则为零。 |
| float xMin | 任何字形边界框原点左侧的最大范围，通常为负值；不推荐使用可变字体。 |
| float xMax | 任何字形边界框原点右侧的最大范围，通常为负值；不推荐使用可变字体。 |
| float xHeight | 小写字母的高度，如果未知则为零，通常为负数。 |
| float capHeight | 大写字母的高度，如果未知则为零，通常为负数。 |
| float underlineThickness | 下划线粗细。 |
| float underlinePosition | 表示下划线的位置，即从基线到文字下方笔画顶部的垂直距离，通常为正值。 |
| float strikeoutThickness | 删除线粗细。 |
| float strikeoutPosition | 表示删除线的位置，即从基线到文字上方笔画底部的垂直距离，通常为负值。 |
