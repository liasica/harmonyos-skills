---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/text-faqs
title: 文本开发常见问题
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 文本 > 文本开发常见问题
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bb4c2b45b3d6fc545ce52ad25936f7ccb9a5013b2ac57dbe84b8a1939ca5d49f
---

## 如何对找不到字形的字符进行显示优化

目前对于找不到字形的字符默认显示为空白，可能让用户感到困惑。

系统提供开关，开启后，未找到字形的字符会显示为豆腐块。

* 在ArkTS环境中，可以使用setTextUndefinedGlyphDisplay接口开启开关，找不到字形的字符会强制显示为豆腐块。

  ```ts
  import { text } from "@kit.ArkGraphics2D";

  text.setTextUndefinedGlyphDisplay(text.TextUndefinedGlyphDisplay.USE_TOFU);
  ```
* 在C/C++环境中，可以使用OH\_Drawing\_SetTextUndefinedGlyphDisplay接口开启开关，找不到字形的字符会强制显示为豆腐块。

  ```c
  #include "drawing/drawing_text_global.h"

  OH_Drawing_SetTextUndefinedGlyphDisplay(TEXT_NO_GLYPH_USE_TOFU);
  ```

上述两个接口控制同一个开关，使用其一即可。

以"\uffffHello World\uffff"文本为例，其中\uffff表示一个找不到字形的字符。

对比效果如下：

| 是否开启显示优化 | 示意效果 |
| --- | --- |
| 未开启 |  |
| 开启 |  |
