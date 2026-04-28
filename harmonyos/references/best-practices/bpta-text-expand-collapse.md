---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-text-expand-collapse
title: 文本展开折叠
breadcrumb: 最佳实践 > 布局与弹窗 > 文本展开折叠
category: best-practices
scraped_at: 2026-04-28T08:19:43+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:1a7d3ac4c9fd9a5bd61b8be456edec563323b12e661f72c76ddbb5d67b2bc282
---

## 概述

列表中的博文、评论等复合型内容组件，在文本行数超过预设阈值时，触发“展开”“收起”的功能。内容收起时，如果有用“图片”展示“表情”的功能场景，由于图片出现的位置和大小都不固定，在收起展开时，截止到文字结尾的位置不好判断。

本文将介绍解决这一问题的基本逻辑和解决方案，帮助开发者使用系统自带模块，更简洁的解决问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/E-Jl-BERRFqu4gXjKHoqGA/zh-cn_image_0000002340609309.png?HW-CC-KV=V1&HW-CC-Date=20260428T001941Z&HW-CC-Expire=86400&HW-CC-Sign=C4D7867B6FD8C17931CB736C3E253DD1596A275C47C866515EA49F16EA0B464C "点击放大")

## 纯文本展开折叠

### 场景描述

在示例列表中显示纯文本展开和收起功能，文本与按钮的显示变化。

1. 文本中只有文字。
2. 超出2行要能显示"...展开"，展开后显示收起。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/FX9akniKT4iVo_uw7QPLzQ/zh-cn_image_0000002306649880.png?HW-CC-KV=V1&HW-CC-Date=20260428T001941Z&HW-CC-Expire=86400&HW-CC-Sign=591211DC5DC86747E57018A4B608E4FFA6D8CD998CDB0648ABAC9B521B358C2D "点击放大")

### 实现原理

需要计算出“...”前最后一个文字的索引和显示行高，以确定“收起”“展开”按钮的位置，其原理如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/RRiZ7W9TTnqOX4EaAfbohA/zh-cn_image_0000002306490160.png?HW-CC-KV=V1&HW-CC-Date=20260428T001941Z&HW-CC-Expire=86400&HW-CC-Sign=2AF87F468513163AC2AA240E3300F1AD398DC4D06D93AA2A8C2DFEEE606D8E59 "点击放大")

计算文本高度，结合按钮和“...”的宽度，计算收起文本最后一个文字的坐标，换算为对应内容索引，截断显示相应的内容。

分别添加“收起”“展开”按钮及交互，进行文本截断内容和全部内容展示的切换。

本示例使用measureTextSize()方法判断文字的高度，API20新增[getParagraphs20+](../harmonyos-references/arkts-apis-uicontext-measureutils.md#getparagraphs20)方法测算文本。getParagraphs()方法代码量更少，更直观的获取显示行数。

### 开发步骤

1. 计算原始文本高度。

   使用[measureTextSize()](../harmonyos-references/arkts-apis-uicontext-measureutils.md#measuretextsize12)方法来判断总体文字的高度。

   ```
   1. getIsExpanded() {
   2. let titleSize: SizeOptions = this.uiContext.getMeasureUtils().measureTextSize({
   3. textContent: this.textSectionAttribute.title, //The text content is calculated
   4. lineHeight: this.textSectionAttribute.lineHeight,
   5. constraintWidth: this.textSectionAttribute.constraintWidth, //The text layout width is calculated
   6. fontSize: this.textSectionAttribute.fontSize //The text font size is calculated
   7. });
   8. let height = this.getUIContext().px2vp(Number(titleSize.height));
   9. if (height <= this.textSectionAttribute.lineHeight * 2) {
   10. this.textModifier.needProcess = false;
   11. this.textModifier.title = this.textSectionAttribute.title;
   12. return;
   13. } else {
   14. this.textModifier.needProcess = true;
   15. }
   16. if (this.expanded) {
   17. this.collapseText();
   18. } else {
   19. this.expandText();
   20. }
   21. }
   ```

   [TextExpandView.ets](https://gitcode.com/harmonyos_samples/TextExpand/blob/master/entry/src/main/ets/view/TextExpandView.ets#L60-L81)
2. 计算文本收起高度（示例代码与步骤3同源）。

   使用measureTextSize()方法来判断两行文字的高度，当前为两行文字的高度。

   ```
   1. const minLinesTextSize: SizeOptions = uiContext?.getMeasureUtils().measureTextSize({
   2. textContent: text,
   3. fontSize: fontSize,
   4. maxLines: maxLines,
   5. wordBreak: WordBreak.BREAK_ALL,
   6. constraintWidth: textWidth
   7. });
   8. const minHeight: Length | undefined = minLinesTextSize.height;
   ```
3. 获取收起文本，显示收起展开按钮。

   减少接收文字字符数。当接收文字高度小于指定行数高度时，使文字显示两行收起。

   ```
   1. public static getShortText(textSectionAttribute: TextSectionAttribute, lastSpan: string): string {
   2. let text = TextUtils.getStringFromResource(textSectionAttribute.title);
   3. const minLinesTextSize: SizeOptions | undefined = uiContext?.getMeasureUtils().measureTextSize({
   4. textContent: text,
   5. fontSize: textSectionAttribute.fontSize,
   6. maxLines: textSectionAttribute.maxLines,
   7. wordBreak: WordBreak.BREAK_ALL,
   8. constraintWidth: textSectionAttribute.constraintWidth
   9. });
   10. const minHeight: Length | undefined = minLinesTextSize?.height;
   11. if (minHeight === undefined) {
   12. return '';
   13. }
   14. // Use the dichotomy to find strings that are exactly two lines in length
   15. let textStr: string[] = Array.from(text); //Split the string to avoid special characters and inconsistent sizes
   16. let leftCursor: number = 0;
   17. let rightCursor: number = textStr.length;
   18. let cursor: number = Math.floor(rightCursor / 2);
   19. let tempTitle: string = '';
   20. while (true) {
   21. tempTitle = text.substring(0, cursor) + suffix + lastSpan;
   22. const currentLinesTextSize: SizeOptions | undefined = uiContext?.getMeasureUtils().measureTextSize({
   23. textContent: tempTitle,
   24. fontSize: textSectionAttribute.fontSize,
   25. wordBreak: WordBreak.BREAK_ALL,
   26. constraintWidth: textSectionAttribute.constraintWidth
   27. });
   28. const currentLineHeight: Length | undefined = currentLinesTextSize?.height;
   29. if (currentLineHeight === undefined) {
   30. return '';
   31. }
   32. if (currentLineHeight > minHeight) {
   33. // The current character has exceeded two lines, continue to look to the left
   34. rightCursor = cursor;
   35. cursor = leftCursor + Math.floor((cursor - leftCursor) / 2);
   36. } else {
   37. // The current character is less than two lines, it may be OK, but you still need to look to the right
   38. leftCursor = cursor;
   39. cursor += Math.floor((rightCursor - cursor) / 2);
   40. }
   41. if (Math.abs(rightCursor - leftCursor) <= 1) {
   42. // The two pointers basically coincide, which means that they have been found
   43. break;
   44. }
   45. }
   46. return text.substring(0, cursor) + suffix;
   47. }
   ```

   [TextUtils.ets](https://gitcode.com/harmonyos_samples/TextExpand/blob/master/entry/src/main/ets/utils/TextUtils.ets#L33-L80)

## 富文本展开折叠

### 场景描述

在示例列表中显示富文本展开和收起功能，文本与按钮的显示变化。

1. 文本中存在表情。
2. 文本中文字存在不同颜色、字号。
3. 超出3行要能显示"...展开"，展开后显示收起。
4. 关键字有超链接功能。

当前展示内容需要针对整个文本做截断并最终显示...和"展开"字眼，例如图片中的文本就比较长，需要在"潮声与你"的位置截断。该场景由于文本中有图片和不同字号的限制，使得计算截断文本的位置比较困难。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/tMdf2v9sTRCEZ4FpdUknqA/zh-cn_image_0000002340489169.png?HW-CC-KV=V1&HW-CC-Date=20260428T001941Z&HW-CC-Expire=86400&HW-CC-Sign=13C330AF7903720C2E81C020D14688BBAC93A318D98BBD81725CAA711129C9CE "点击放大")

### 实现原理

需要计算出“...”前最后一个文字的索引和显示行高，以确定“收起”“展开”按钮的位置，其原理如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/xLyARxQARq6c9tbvg62slw/zh-cn_image_0000002340609313.png?HW-CC-KV=V1&HW-CC-Date=20260428T001941Z&HW-CC-Expire=86400&HW-CC-Sign=408022789CF3A5B3D4E0156026047BA122748E91CC4B0D073D66848A1568E11A "点击放大")

使用排版，计算实际需要收起内容的高度，结合按钮和“...”的宽度，计算收起文本最后一个文字的坐标，换算为对应内容索引，截断显示相应的内容。

分别添加“收起”“展开”按钮及交互，进行文本截断内容和全部内容展示的切换。

### 开发步骤

1. 引用[graphics.text](../harmonyos-references/js-apis-graphics-text.md)解析文本、确定内容大小。

   设置文本解析规则，解析字符串。例如，图片显示位置、大小、文本显示位置、文本颜色、文本字号。
2. 设置段落排版。

   创建ParagraphBuilder，初始化文本样式，指定文本大小和文本颜色。注意文本大小这里是传的px，需要用fp2px转换一下（转换时需要考虑字体设置的最大缩放比例和系统字体缩放比例，即选择min(sysFontScale，maxCustomFontScale)）。

   ```
   1. let myTextStyle: text.TextStyle = {
   2. fontSize: uiContext?.fp2px(fontSize)
   3. };

   5. let myParagraphStyle: text.ParagraphStyle = {
   6. textStyle: myTextStyle,
   7. align: text.TextAlign.START,
   8. maxLines: 300, // Just specify a large enough number of rows
   9. breakStrategy: text.BreakStrategy.GREEDY,
   10. wordBreak: text.WordBreak.BREAK_WORD
   11. };

   13. let fontCollection = new text.FontCollection();
   14. let paragraphGraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
   ```

   [TextUtils.ets](https://gitcode.com/harmonyos_samples/TextExpand/blob/master/entry/src/main/ets/utils/TextUtils.ets#L113-L126)
3. 添加占位符，指定样式。

   根据第一步骤解析出来的内容，如果是图片的话，就用addPlaceholder()，添加一张图片占位符，需要指定这张图片的大小（单位px），旁边的文字排版方式，文字基线位置等信息。

   ```
   1. paragraphGraphBuilder.addPlaceholder({
   2. width: item.imgWidth,
   3. height: item.imgHeight,
   4. align: text.PlaceholderAlignment.BOTTOM_OF_ROW_BOX,
   5. baseline: text.TextBaseline.IDEOGRAPHIC,
   6. baselineOffset: 0
   7. });
   ```

   [TextUtils.ets](https://gitcode.com/harmonyos_samples/TextExpand/blob/master/entry/src/main/ets/utils/TextUtils.ets#L139-L145)

   如果是文字的话，就使用addText()，添加一段文本，添加这段文本之前可以重新通过pushStyle()方法指定这段文本的字体大小和颜色。

   ```
   1. paragraphGraphBuilder.pushStyle({
   2. fontSize: fontSize,
   3. });
   4. paragraphGraphBuilder.addText(item.content);
   ```

   [TextUtils.ets](https://gitcode.com/harmonyos_samples/TextExpand/blob/master/entry/src/main/ets/utils/TextUtils.ets#L151-L154)

   如果需要使用之前的文本样式，可以通过popStyle()把当前样式pop出去。

   上面添加的文字大小和图片占位符的大小要同Text控件展示的时候的大小一致，否则会导致计算不准确。
4. 预排版。

   全部添加完成之后，使用paragraph的layoutSync()方法预先排版，传递的大小单位也为px。这个layoutSync()传递宽度要同展示的时候的Text文本宽度一致，否则计算出来的和展示的时候肯定不一致。

   ```
   1. let paragraph = paragraphGraphBuilder.build();
   2. paragraph.layoutSync(textMaxWidth);
   ```

   [TextUtils.ets](https://gitcode.com/harmonyos_samples/TextExpand/blob/master/entry/src/main/ets/utils/TextUtils.ets#L164-L165)
5. 计算截断坐标。

   计算三个点之前的最后一个文字的坐标。设这个字符变量为lastWord。经过paragraph的排版之后，就可以得到这段文本真实的渲染数据了。先通过paragraph.getLineCount()，计算出来一共排版了多少行，如果超过了自己要设定的行数，或者getLineCount()的行数和自己设定的maxLine一致，但是最后一行的宽度+之前计算出来的widthMore，超过了第四步骤设定的最大宽度，则说明需要截断。

   计算lastWord文字的Y坐标，通过getLineHeight()获取每一行的高度加起来，其中最后一行高度需要加一半的高度。

   ```
   1. for (let i = 0; i < textSectionAttribute.maxLines; i++) {
   2. y += i === textSectionAttribute.maxLines - 1 ? paragraph.getLineHeight(i) / 2 : paragraph.getLineHeight(i);
   3. }
   ```

   [TextUtils.ets](https://gitcode.com/harmonyos_samples/TextExpand/blob/master/entry/src/main/ets/utils/TextUtils.ets#L195-L197)
6. 计算lastWord的X坐标。

   ```
   1. if (paragraph.getLineWidth(textSectionAttribute.maxLines - 1) + Number(widthMore) >
   2. textSectionAttribute.constraintWidth) {
   3. x = textSectionAttribute.constraintWidth - Number(widthMore);
   4. } else {
   5. x = paragraph.getLineWidth(textSectionAttribute.maxLines - 1)
   6. }
   ```

   [TextUtils.ets](https://gitcode.com/harmonyos_samples/TextExpand/blob/master/entry/src/main/ets/utils/TextUtils.ets#L201-L206)
7. 转换坐标对应索引。

   计算lastWord的展示索引位置。拿到lastWord的x与y坐标之后，通过getGlyphPositionAtCoordinate()拿到这个坐标的文字所在段落的索引，这个就是最终文字展示的索引。

   ```
   1. // The conversion coordinates correspond to the index
   2. let positionWithAffinity = paragraph.getGlyphPositionAtCoordinate(x, y);
   3. let index = 0;
   4. if (positionWithAffinity.affinity === text.Affinity.UPSTREAM) {
   5. index = positionWithAffinity.position;
   6. } else {
   7. index = positionWithAffinity.position + 1;
   8. }
   ```

   [TextUtils.ets](https://gitcode.com/harmonyos_samples/TextExpand/blob/master/entry/src/main/ets/utils/TextUtils.ets#L210-L217)
8. 添加“展开”“收起”按钮。

   显示展开按钮时使用上面获取的shortContentArray数组数据来渲染，完全展示的时候使用RichTextModel里的textArray数组数据来渲染。判断两种情况分别显示按钮。

   ```
   1. if (this.textModifier.needProcess && !this.textModifier.exceedOneLine) {
   2. Span(this.lastSpanAttribute.content[0])
   3. .fontColor(this.lastSpanAttribute.color)
   4. } else if (this.textModifier.exceedOneLine) {
   5. Span(this.lastSpanAttribute.content[1])
   6. .fontColor(this.lastSpanAttribute.color)
   7. }
   ```

   [RichTextExpandView.ets](https://gitcode.com/harmonyos_samples/TextExpand/blob/master/entry/src/main/ets/view/RichTextExpandView.ets#L106-L112)

## 示例代码

* [实现富文本收起展开功能](https://gitcode.com/harmonyos_samples/TextExpand)
