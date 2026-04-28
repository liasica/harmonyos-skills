---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-strutstyle
title: OH_Drawing_StrutStyle
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_StrutStyle
category: harmonyos-references
scraped_at: 2026-04-28T08:15:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e569066042b23120a544bda2b6ee38dba79a8d153c0584044fac00b407b9a78c
---

```
1. typedef struct OH_Drawing_StrutStyle {...} OH_Drawing_StrutStyle
```

## 概述

PhonePC/2in1TabletTVWearable

用于描述支柱样式的结构体。支柱样式用于控制绘制文本时行之间的间距、基线对齐方式以及其他与行高相关的属性。

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_text\_typography.h](capi-drawing-text-typography-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontWeight](capi-drawing-text-typography-h.md#oh_drawing_fontweight) weight | 计算支柱时使用的字体粗细。 |
| [OH\_Drawing\_FontStyle](capi-drawing-text-typography-h.md#oh_drawing_fontstyle) style | 计算支柱时使用的字体格式。 |
| double size | 逻辑像素中的上升加下降的大小。 |
| double heightScale | 行高缩放系数。 |
| bool heightOverride | 是否启用高度覆盖。true表示启用，false表示不启用。 |
| bool halfLeading | 半行距是否启用。true表示启用，false表示不启用。 |
| double leading | 以自定义行距应用于支柱的行距。 |
| bool forceStrutHeight | 是否所有行都将使用支柱的高度。true表示使用，false表示不使用。 |
| size\_t familiesSize | 字体家族的数量。 |
| char\*\* families | 计算支柱时使用的字体名称。 |
