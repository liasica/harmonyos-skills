---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/text-custom-arkts
title: 自定义文本绘制与显示（ArkTS）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 文本 > 文本绘制与显示 > 自定义文本绘制与显示（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6b3ddbb0c33e60111e4ee19cf4d24819defbc0d704560ee7f2575d36af7ddbde
---

在复杂的文本排版场景中，当系统提供的标准文本组件无法满足特定的视觉或交互需求时，开发者可以利用ArkGraphics 2D提供的底层文本绘制能力，通过直接控制画布（Canvas）和文本样式，实现对文本外观、布局的精细控制。这种能力适用于需要高度定制化文本渲染效果的场景，例如艺术字体、复杂的富文本编排或特殊的动态文字效果。

字体引擎作为图形系统中的核心组件，负责将字符代码转换为可视化的字形，并精确计算每个字形的布局和位置，为自定义文本绘制提供底层支持。通过文本测量接口，开发者可以获取文本的精确尺寸，这是实现精准布局（如居中显示）的基础。

## 文本塑形

### 场景介绍

文本塑形是字体引擎提供的一项关键能力，它允许开发者不经过系统默认的文本排版流程，直接获取文本的底层字形信息（如宽度、方向等测量信息）。这使得开发者能够基于这些原始数据，实现完全自定义的排版逻辑、绘制操作以及断行策略。

这种能力适用于以下场景：

* 自定义富文本渲染：例如在社交媒体、新闻客户端等应用中，需要实现图文混排、多样式文本混合显示。
* 跨平台一致性排版需求应用：确保文本在不同平台或设备上呈现一致的视觉效果。
* 精细化排版管理：如实现艺术排版、动态文字布局等系统标准文本组件难以达到的效果。

### 接口说明

文本塑形中常用接口如下表所示，详细接口说明参考[@ohos.graphics.text (文本模块)](../harmonyos-references/js-apis-graphics-text.md#paragraph)和[@ohos.graphics.drawing (drawing TextBlob)](../harmonyos-references/arkts-apis-graphics-drawing-textblob.md)。

| 接口名 | 描述 |
| --- | --- |
| buildLineTypeset(): LineTypeset | 构建行排版器。 |
| createLine(startIndex: number, count: number): TextLine | 根据指定的排版区间生成文本行对象。 |
| getGlyphRuns(): Array<Run> | 获取文本行的排版单元数组。 |
| getGlyphs(): Array<number> | 获取该排版单元中每个字符的字形序号。 |
| getFont(): drawing.Font | 获取排版单元的字体属性对象。 |
| getAdvances(range: Range): Array<common2D.Point> | 获取该排版单元指定范围内每个字形的字形宽度数组。 |
| static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob | 基于RunBuffer信息创建TextBlob对象。 |
| static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob | 基于RunBuffer信息创建TextBlob对象。 |
| drawTextBlob(blob: TextBlob, x: number, y: number): void | 绘制一段文字。若构造blob的字体不支持待绘制字符，则该部分字符无法绘制。 |

### 开发步骤

从API version 18开始，支持获取文字塑形结果能力。从API version 20开始，支持获取文字排版方向和文字字形宽度。关键代码如下：

1. 导入依赖的相关模块。

   ```
   1. import { text } from '@kit.ArkGraphics2D'
   2. import { drawing } from '@kit.ArkGraphics2D'
   3. import { common2D } from '@kit.ArkGraphics2D'
   ```
2. 创建段落样式，并使用构造段落生成器ParagraphBuilder生成段落实例。

   ```
   1. let myTextStyle: text.TextStyle = {
   2. // 文本大小
   3. fontSize: 60
   4. };
   5. let myParagraphStyle: text.ParagraphStyle = {
   6. textStyle: myTextStyle,
   7. };
   8. let fontCollection = text.FontCollection.getGlobalInstance();
   9. let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
   ```

   [IndependentShaping.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/shape/IndependentShaping.ets#L52-L62)
3. 添加文本内容。

   ```
   1. paragraphBuilder.addText('Hello World');
   ```

   [IndependentShaping.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/shape/IndependentShaping.ets#L65-L67)
4. 创建行对象。获取行中所有文字的塑形结果。

   使用createLine()方法创建一个单行对象，通过行对象getGlyphRuns()方法获取相同样式的文字单元。

   ```
   1. // 生成行
   2. let lineTypeSet: text.LineTypeset = paragraphBuilder.buildLineTypeset()
   3. let textLine: text.TextLine = lineTypeSet.createLine(0, 11);

   5. // 获取塑形结果
   6. let runs: text.Run[] = textLine.getGlyphRuns();
   ```

   [IndependentShaping.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/shape/IndependentShaping.ets#L69-L76)
5. 该步骤是文本塑形流程中的自定义绘制环节。通过调用getGlyphs()方法获取文本中每个字符对应的字形序号，再结合getFont()方法获取的字体对象，即可唯一确定每个字形的具体图形信息。

   从 API version 20 开始，新增的getAdvances()方法能够返回一个数组，其中包含了每个字形在绘制时建议占用的宽度和高度。依赖这些精确的测量数据，开发者可以自由地计算并定义每个字形的绘制位置，从而实现复杂的文本布局效果，如自定义字符间距、垂直偏移或特殊排版。

   ```
   1. let x: number = 0;
   2. let y: number = 0;
   3. for (let index = 0; index < runs.length; index++) {
   4. const run = runs[index];
   5. // 绘制字形
   6. let glyphs: number[] = run.getGlyphs();
   7. let font: drawing.Font = run.getFont();
   8. let advances: common2D.Point[] = run.getAdvances({ start: 0, end: 0 });

   10. // 创建字形buffer，通过drawing接口进行字形独立绘制
   11. let runBuffer: drawing.TextBlobRunBuffer[] = [];
   12. for (let i = 0; i < glyphs.length; i++) {
   13. runBuffer.push({ glyph: glyphs[i], positionX: x, positionY: y });
   14. x += advances[i].x + 10;
   15. y += advances[i].y + 30;
   16. }
   17. let textBlob: drawing.TextBlob = drawing.TextBlob.makeFromRunBuffer(runBuffer, font, null);
   18. // 自定义绘制一串具有相同属性的一系列连续字形
   19. canvas.drawTextBlob(textBlob, 20, 100);
   20. }
   ```

   [IndependentShaping.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ComplexTextDrawing/entry/src/main/ets/pages/shape/IndependentShaping.ets#L78-L99)

效果展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/WV1c_QyTQkia5UBKC3-8tQ/zh-cn_image_0000002589325059.png?HW-CC-KV=V1&HW-CC-Date=20260429T053615Z&HW-CC-Expire=86400&HW-CC-Sign=D16BA79047529789B47C5456B439555D23DBB7B755F1AC251384723D56FC2084)
