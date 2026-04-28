---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/text-measure-c
title: 文本测量（C/C++）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 文本 > 文本测量 > 文本测量（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3c16677959b2b9444f8a044d67ad41fbb3dd14df4c8311ef48aae55c7f304a03
---

## 场景介绍

文本测量指的是在图形绘制中，对文本的尺寸和布局进行评估，计算文本在给定字体和样式下占用的空间（例如宽度、高度和其他相关信息）的过程。文本测量用于文本排版、布局、渲染以及调整文本显示的位置和大小等场景，便于更精准地控制与调整界面的布局和呈现，以达到设计预期。

当前主要支持以下方面的文本测量能力：

* **文本宽度**：测量给定文本在特定字体、大小和样式下的水平长度。
* **文本高度**：测量给定文本的垂直高度，通常涉及字体的上升线、下降线等。
* **行间距**：测量多行文本之间的垂直距离，通常与字体的行距相关。
* **字符间距**：测量单个字符之间的水平距离，通常与字形和字体设计有关。

## 接口说明

文本测量中常用接口如下表所示，详细接口说明参考[drawing\_text\_typography.h](../harmonyos-references/capi-drawing-text-typography-h.md)。

| 接口名 | 描述 |
| --- | --- |
| double OH\_Drawing\_TypographyGetLongestLine(OH\_Drawing\_Typography\*) | 获取最长行的宽度，建议实际使用时将返回值向上取整。 |
| double OH\_Drawing\_TypographyGetLongestLineWithIndent(OH\_Drawing\_Typography\*) | 获取最长行的宽度（该宽度包含当前行缩进的宽度），建议实际使用时将返回值向上取整。 |
| size\_t OH\_Drawing\_TypographyGetLineCount (OH\_Drawing\_Typography\* ) | 获取文本行数。 |
| OH\_Drawing\_LineMetrics\* OH\_Drawing\_TypographyGetLineMetrics (OH\_Drawing\_Typography\* ) | 获取段落行的度量信息。包含行的高度、宽度、起始坐标等信息。 |
| double OH\_Drawing\_TextStyleGetLetterSpacing (OH\_Drawing\_TextStyle \*) | 获取文本的字符间距。 |

## 开发步骤

1. 在工程的src/main/cpp/CMakeLists.txt文件中添加以下lib。

   ```
   1. libnative_drawing.so
   ```
2. 导入依赖的相关头文件。

   ```
   1. #include <native_drawing/drawing_font_collection.h>
   2. #include <native_drawing/drawing_text_typography.h>
   3. #include <native_drawing/drawing_text_declaration.h>
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKTextMeasurement/entry/src/main/cpp/samples/sample_bitmap.cpp#L17-L21)
3. 创建段落生成器ParagraphBuilder，并设置段落样式。

   ```
   1. // 创建文本样式，并设置字体大小为50
   2. OH_Drawing_SetTextStyleColor(myTextStyle, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
   3. OH_Drawing_SetTextStyleFontSize(myTextStyle, 50.0);
   4. // 创建一个段落样式对象，以设置排版风格
   5. OH_Drawing_TypographyStyle *typographyStyle = OH_Drawing_CreateTypographyStyle();
   6. // 设置段落样式的对齐方式为左对齐
   7. OH_Drawing_SetTypographyTextAlign(typographyStyle, TEXT_ALIGN_LEFT);
   8. // 创建一个段落生成器
   9. OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typographyStyle, fontCollection);
   10. // 在段落生成器中设置文本样式
   11. OH_Drawing_TypographyHandlerPushTextStyle(handler, myTextStyle);
   12. // 在段落生成器中添加文本内容
   13. const char *text = "排版测量的文字度量信息";
   14. OH_Drawing_TypographyHandlerAddText(handler, text);
   15. // 通过段落生成器生成段落
   16. OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKTextMeasurement/entry/src/main/cpp/samples/sample_bitmap.cpp#L173-L190)
4. 调用排版接口并设置段落排版宽度，对段落进行塑型排版。

   ```
   1. // 对段落进行塑形排版，设置排版宽度为maxWidth
   2. OH_Drawing_TypographyLayout(typography, maxWidth);
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKTextMeasurement/entry/src/main/cpp/samples/sample_bitmap.cpp#L194-L197)
5. 调用段落测量信息获取接口，获取指定数据。

   ```
   1. // case1: 获取排版后最长行行宽
   2. double longestLine = OH_Drawing_TypographyGetLongestLine(typography);
   3. DRAWING_LOGI("第%{public}d行 longestLine: %{public}f", longestLine);

   5. // case2:获取排版后段落行数
   6. size_t lineCnt = OH_Drawing_TypographyGetLineCount(typography);
   7. DRAWING_LOGI("lineCnt: %{public}zu", lineCnt);

   9. // case3:获取段落每行的度量信息
   10. OH_Drawing_LineMetrics *lineMetrics = OH_Drawing_TypographyGetLineMetrics(typography);
   11. int lineMetricsSize = OH_Drawing_LineMetricsGetSize(lineMetrics);
   12. for (int i = 0; i < lineMetricsSize; ++i) {
   13. // lineMetrics为经过排版测量的文字度量信息
   14. double curLineAscender = -lineMetrics[i].ascender;
   15. double curLineWidth = lineMetrics[i].width;
   16. DRAWING_LOGI("第%{public}d行 lineMetrics ascender: %{public}f", i + 1, curLineAscender);
   17. DRAWING_LOGI("第%{public}d行 lineMetrics width: %{public}f", i + 1, curLineWidth);
   18. }

   20. // case4:获取段落最长行宽度与带缩进最长行行宽
   21. double longestLineWithIndent = OH_Drawing_TypographyGetLongestLineWithIndent(typography);
   22. DRAWING_LOGI("longestLineWithIndent: %{public}f", longestLineWithIndent);

   24. OH_Drawing_Font_Metrics fontMetrics;
   25. // 获取文本字体属性
   26. bool result = OH_Drawing_TextStyleGetFontMetrics(typography, myTextStyle, &fontMetrics);
   27. DRAWING_LOGI("result: %{public}zu, fontMetrics ascent: %{public}f" , result, fontMetrics.ascent);
   28. // 获取排版对象的指定行位置信息，该接口需要在OH_Drawing_TypographyLayout接口调用之后调用
   29. OH_Drawing_LineMetrics lineMetric;
   30. OH_Drawing_TypographyGetLineMetricsAt(typography, 0, &lineMetric);
   31. DRAWING_LOGI("第1行 lineMetrics ascender: %{public}f", -lineMetric.ascender);
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKTextMeasurement/entry/src/main/cpp/samples/sample_bitmap.cpp#L200-L232)
