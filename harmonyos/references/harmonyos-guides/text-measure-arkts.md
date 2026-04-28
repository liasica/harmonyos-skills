---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/text-measure-arkts
title: 文本测量（ArkTS）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 文本 > 文本测量 > 文本测量（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:422839b667be05ea1a4f7ca686b7851ea417634f687602d614418d2d31beba1d
---

## 场景介绍

文本测量指的是在图形绘制中，对文本的尺寸和布局进行评估，计算文本在给定字体和样式下占用的空间（例如宽度、高度和其他相关信息）的过程。文本测量用于文本排版、布局、渲染以及调整文本显示的位置和大小等场景，便于更精准地控制与调整界面的布局和呈现，以达到设计预期。

当前主要支持以下方面的文本测量能力：

* **文本宽度**：测量给定文本在特定字体、大小和样式下的水平长度。
* **文本高度**：测量给定文本的垂直高度，通常涉及文本的上升线、下降线等。
* **行间距**：测量多行文本之间的垂直距离，通常与文本的行距相关。
* **字符间距**：测量单个字符之间的水平距离，通常与字形和字体设计有关。

## 接口说明

文本测量中常用接口如下表所示，详细接口说明参考[@ohos.graphics.text (文本模块)](../harmonyos-references/js-apis-graphics-text.md#paragraph)。

| 接口名 | 描述 |
| --- | --- |
| getLongestLine(): number | 获取当前段落最长行的宽度，建议实际使用时将返回值向上取整。 |
| getLongestLineWithIndent(): number | 获取当前段落最长行的宽度（该宽度包含当前行缩进的宽度），建议实际使用时将返回值向上取整。 |
| getTextLines(): Array<TextLine> | 获取当前段落文本行对象数组。 |
| getLineMetrics(): Array<LineMetrics> | 获取段落所有行的度量信息。包含行的高度、宽度、起始坐标等信息。 |
| getLineMetrics(lineNumber: number): LineMetrics | undefined | 获取段落指定行的度量信息。包含行的高度、宽度、起始坐标等信息。超出当前段落排版后最大行数后返回undefined。 |

## 开发步骤

1. 导入依赖的相关模块。

   ```
   1. import { text } from '@kit.ArkGraphics2D';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/TextMetrics/entry/src/main/ets/pages/Index.ets#L19-L21)
2. 创建段落样式，并使用构造段落生成器ParagraphBuilder生成段落实例。

   ```
   1. // 设置文本样式
   2. let myTextStyle: text.TextStyle = {
   3. color: {
   4. alpha: 255,
   5. red: 255,
   6. green: 0,
   7. blue: 0
   8. },
   9. fontSize: 100
   10. };
   11. // 创建一个段落样式对象，以设置排版风格
   12. let myParagraphStyle: text.ParagraphStyle = {
   13. textStyle: myTextStyle,
   14. wordBreak: text.WordBreak.NORMAL
   15. };
   16. // 创建一个段落生成器
   17. let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, new text.FontCollection());
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/TextMetrics/entry/src/main/ets/pages/Index.ets#L28-L46)
3. 设置文本样式，添加文本内容，并生成段落文本用于后续文本的绘制显示。

   ```
   1. // 在段落生成器中设置文本样式
   2. paragraphBuilder.pushStyle(myTextStyle);
   3. // 在段落生成器中设置文本内容
   4. paragraphBuilder.addText("文本测量测试");
   5. // 通过段落生成器生成段落
   6. let paragraph = paragraphBuilder.build();
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/TextMetrics/entry/src/main/ets/pages/Index.ets#L47-L54)
4. 调用测量相关接口，获取指定的测量信息。

   ```
   1. // 对段落进行塑形排版，设置排版宽度为1000
   2. paragraph.layoutSync(1000);
   3. // case1: 获取排版后最长行行宽
   4. let longestLineWidth = paragraph.getLongestLine();
   5. console.info("longestLineWidth = " + longestLineWidth);

   7. // case2: 获取排版后最长行行宽(包含缩进)
   8. let longestLineWithIndentWidth = paragraph.getLongestLineWithIndent();
   9. console.info("longestLineWithIndentWidth = " + longestLineWithIndentWidth);

   11. // case3: 获取排版后所有行对象
   12. let textLines = paragraph.getTextLines();
   13. for (let index = 0; index < textLines.length; index++) {
   14. const textline = textLines[index];
   15. let curLineRange = textline.getTextRange();
   16. let curLineGlyCnt = textline.getGlyphCount();
   17. console.info("MetricsMSG: 第" + (index + 1) + "行 TextRange start: " + curLineRange.start + " TextRange end: " + curLineRange.end);
   18. console.info("MetricsMSG: 第" + (index + 1) + "行字形数量为: " + curLineGlyCnt);
   19. }

   21. // case4: 获取排版后指定行对应的度量信息
   22. let lineCnt = paragraph.getLineCount();
   23. for (let index = 0; index < lineCnt; index++) {
   24. let lineMetrics = paragraph.getLineMetrics(index);
   25. if (lineMetrics) {
   26. console.info("MetricsMSG: 第" + (index + 1) + "行 lineMetrics width: " + lineMetrics.width);
   27. console.info("MetricsMSG: 第" + (index + 1) + "行 lineMetrics start index: " + lineMetrics.startIndex + ", end index: " +
   28. lineMetrics.endIndex);
   29. }
   30. }

   32. // case5: 获取排版后所有行度量信息数组
   33. let allLineMetrics = paragraph.getLineMetrics();
   34. console.info("MetricsMSG: 第1行 lineMetrics width: " + allLineMetrics[0].width);
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/TextMetrics/entry/src/main/ets/pages/Index.ets#L55-L90)
