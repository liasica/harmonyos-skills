---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/textblock-drawing-arkts
title: 字块绘制（ArkTS）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 图形绘制与显示 > 图元绘制 > 字块绘制（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7ca295430f558ff22821c0c27a482bc00b56d73c80acdaa18ffa99b1efacfc9d
---

## 场景介绍

字块（TextBlob）是指文本的集合。无论是单个的文字还是大块的文本，都可以通过字块来绘制。

除了基本的字块绘制之外，还可以给文字添加各种绘制效果。常见的字块绘制场景包括[文字描边](textblock-drawing-arkts.md#文字描边)、[文字渐变](textblock-drawing-arkts.md#文字渐变)等，更多效果请见[绘制效果](drawing-effect-overview.md)。

本节不涉及文本测量和布局排版相关内容，如需在开发中处理此类文本绘制需求，可参考[文本开发概述](text-overview.md)，该文档系统讲解了排版策略与相关使用指导。

## 基本字块绘制

Canvas通过drawTextBlob()来绘制字块。函数接受三个参数：TextBlob字块对象，以及文字基线左端点的x坐标和y坐标。

画布Canvas对象具体可见[画布的获取与绘制结果的显示（ArkTS）](canvas-get-result-draw-arkts.md)。

字块对象可以通过多种方式创建得到，详细的字块创建方式和接口使用请参考[TextBlob](../harmonyos-references/arkts-apis-graphics-drawing-textblob.md)。

此处以使用makeFromString()接口创建字块为例，接口接受3个参数，分别为：

* 需要显示的字符串text。
* font字型对象。其中font用于设置和获取字体的各种属性，如字体大小、文本样式、字体对齐方式、字体渲染方式、字体描边方式等，详细的API介绍请参考[Font](../harmonyos-references/arkts-apis-graphics-drawing-font.md)。
* 文本编码方式。当前支持的文本编码方式如下：

  + TEXT\_ENCODING\_UTF8：使用1个字节表示UTF-8或ASCII；
  + TEXT\_ENCODING\_UTF16：使用2个字节表示大部分unicode；
  + TEXT\_ENCODING\_UTF32：使用4个字节表示全部unicode；
  + TEXT\_ENCODING\_GLYPH\_ID：使用2个字节表示glyph index。

基本效果的示例代码和效果图如下：

```
1. // 创建字型对象
2. const font = new drawing.Font();
3. // 设置字体大小
4. font.setSize(100);
5. // 创建字块对象
6. const textBlob = drawing.TextBlob.makeFromString('Hello world', font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
7. // 绘制字块
8. canvas.drawTextBlob(textBlob, VALUE_200, VALUE_300);
```

[TextBlockDrawing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/TextBlockDrawing.ets#L22-L31)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/RiKpPgxWQd-ZFIlSLaLBMQ/zh-cn_image_0000002583438705.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234711Z&HW-CC-Expire=86400&HW-CC-Sign=D5929F8561988E5BD8D42EDBB683343A9084773DC528050AED46C71A6EC4624F)

## 文字描边

基于基本的字块绘制，还可以通过画笔实现文字描边效果，描边效果的更多介绍请参考[描边效果](basic-drawing-effect-arkts.md#描边效果)。

以下以英文文字描边和中文文字描边给出示例和指导。

### 英文文字描边

英文文字描边的简要示例和示意图如下：

```
1. // 创建画笔
2. let pen = new drawing.Pen();
3. // 设置抗锯齿
4. pen.setAntiAlias(true);
5. // 设置描边线宽
6. pen.setStrokeWidth(3.0);
7. // 设置描边颜色
8. pen.setColor(0xFF, 0xFF, 0x00, 0x00);
9. // 创建字型对象
10. const font = new drawing.Font();
11. // 设置字体大小
12. font.setSize(100);
13. // 添加画笔描边效果
14. canvas.attachPen(pen);
15. // 创建字块对象
16. const textBlob = drawing.TextBlob.makeFromString('Hello world', font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
17. // 绘制字块
18. canvas.drawTextBlob(textBlob, VALUE_200, VALUE_300);
19. // 去除描边效果
20. canvas.detachPen();
```

[TextBlockDrawing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/TextBlockDrawing.ets#L35-L56)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/h53cyQvYTnumUr2hweSiPw/zh-cn_image_0000002552958660.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234711Z&HW-CC-Expire=86400&HW-CC-Sign=71BB2C41C83CEB1704A84AD923B301F20F136440C86AFD37381D62944762FF48)

### 中文文字描边

首先需要通过画笔描边，然后需要调用画刷填充内部颜色，去除字体中间的杂质和重叠部分，实现中文文字描边效果。

中文文字描边的简要示例和示意图如下：

```
1. // 创建画刷
2. let brush = new drawing.Brush();
3. // 创建画笔
4. let pen = new drawing.Pen();
5. // 设置抗锯齿
6. brush.setAntiAlias(true);
7. // 设置描边颜色
8. brush.setColor(0xFF, 0xFF, 0xFF, 0xFF);

10. pen.setAntiAlias(true);
11. // 设置描边线宽
12. pen.setStrokeWidth(3.0);
13. // 设置描边颜色
14. pen.setColor(0xFF, 0xFF, 0x00, 0x00);

16. // 创建字型对象
17. const font = new drawing.Font();
18. // 设置字体大小
19. font.setSize(100);
20. // 添加画笔描边效果
21. canvas.attachPen(pen);
22. // 创建字块对象
23. const textBlob = drawing.TextBlob.makeFromString(STROKE_SAMPLE, font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
24. // 绘制字块
25. canvas.drawTextBlob(textBlob, VALUE_200,  VALUE_300);
26. // 去除描边效果
27. canvas.detachPen();

29. canvas.attachBrush(brush);
30. canvas.drawTextBlob(textBlob, VALUE_200, VALUE_300);
31. canvas.detachBrush();
```

[TextBlockDrawing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/TextBlockDrawing.ets#L60-L93)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/g3dJT8saQiK3VKZSnRASbg/zh-cn_image_0000002583478661.png?HW-CC-KV=V1&HW-CC-Date=20260427T234711Z&HW-CC-Expire=86400&HW-CC-Sign=2DBF64012B6ECBDF28DAD9978CD81D7340ACD8E068BBA69EA2B4346C1DB73AEF)

## 文字渐变

基于基本字块绘制，还可以通过着色器实现文字渐变的效果，着色器的更多介绍请参考[着色器效果](complex-drawing-effect-arkts.md#着色器效果)。

以下为文字添加了线性渐变着色器效果的简要示例和示意图：

```
1. let startPt: common2D.Point = { x: VALUE_100, y: VALUE_100 };
2. let endPt: common2D.Point = { x: VALUE_900, y: VALUE_900 };
3. let colors = [0xFFFFFF00, 0xFFFF0000, 0xFF0000FF];
4. // 创建线性渐变着色器
5. let shaderEffect = drawing.ShaderEffect.createLinearGradient(startPt, endPt, colors, drawing.TileMode.CLAMP);
6. // 创建画刷
7. let brush = new drawing.Brush();
8. // 设置着色器
9. brush.setShaderEffect(shaderEffect);
10. // 添加画刷填充效果
11. canvas.attachBrush(brush);
12. // 创建字型
13. const font = new drawing.Font();
14. // 设置字体大小
15. font.setSize(VALUE_200);
16. // 创建字块
17. const textBlob = drawing.TextBlob.makeFromString('Hello world', font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
18. // 绘制字块
19. canvas.drawTextBlob(textBlob, VALUE_100, VALUE_300);
20. // 去除填充效果
21. canvas.detachBrush();
```

[TextBlockDrawing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/TextBlockDrawing.ets#L97-L119)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/SKWRljt8TqyzFgKZ5H_TVQ/zh-cn_image_0000002552799012.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234711Z&HW-CC-Expire=86400&HW-CC-Sign=CEC444608FBFCA7DF94ED78DBD59697F06E9E177EC83AEC972FC0E378BBA98E7)

## 主题字体

主题字体，特指系统**主题应用**中能使用的字体，属于一种特殊的自定义字体。如需涉及文本测量和布局排版相关内容，可参考[使用主题字体（ArkTS）](theme-font-arkts.md)。

设置跟随主题字体的示例代码和效果图如下：

```
1. // 创建线性渐变着色器
2. const font = new drawing.Font();
3. // 设置文字大小
4. font.setSize(100);
5. // 设置跟随主题字体
6. font.setThemeFontFollowed(true);
7. // 创建字块对象
8. const textBlob = drawing.TextBlob.makeFromString('Hello World', font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
9. // 绘制字块
10. canvas.drawTextBlob(textBlob, VALUE_200, VALUE_300);
```

[TextBlockDrawing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/TextBlockDrawing.ets#L123-L134)

| 未跟随主题字体的效果图 | 跟随主题字体的效果图（不同主题字体显示效果不同，此处仅示意） |
| --- | --- |
|  |  |

说明

需要在应用入口文件（默认工程中为EntryAbility.ets）中复写onConfigurationUpdate函数，以响应切换主题字体的操作，确保切换后页面能够及时刷新并生效。具体实现可参考[使用主题字体（ArkTS）](theme-font-arkts.md)。

## 单字绘制

单字绘制是图形渲染中针对文本渲染的一种精细化控制技术。相比字块绘制，其核心优势在于能够利用字体退化机制，在当前字体无法显示某字符时，自动退化到使用系统字体绘制字符，提升对特殊字符的兼容性，避免字符缺失。同时，单字绘制支持逐字符配置字体特征（如连字、替代字形），满足复杂排版需求，增强用户体验。详细API说明请见[drawing.Canvas](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#drawsinglecharacter12)。

基础场景：绘制无字体特征的字符。

对于无需字体特征的常规文本渲染场景，可以使用drawSingleCharacter绘制单个字符，使用measureSingleCharacter测量单个字符的宽度，示例代码和效果图如下：

```
1. // 创建字型对象
2. const font = new drawing.Font();
3. // 设置文字大小
4. font.setSize(100);
5. let startX = 100;
6. let startY = 100;
7. let text = ['H', 'e', 'l', 'l', 'o'];
8. for (let s of text) {
9. // 单字绘制
10. canvas.drawSingleCharacter(s, font, startX, startY);
11. // 测量单个字符的宽度
12. let textWidth = font.measureSingleCharacter(s);
13. startX += textWidth;
14. }
```

[TextBlockDrawing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/TextBlockDrawing.ets#L138-L153)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/APguuIaNRuS6btQtZgmQBA/zh-cn_image_0000002583478663.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234711Z&HW-CC-Expire=86400&HW-CC-Sign=8C49F707D85998B1EEECDF5BFD850B5F506E58817A5BA1F5571FB28CDC5898CC)

进阶场景：绘制带字体特征的字符。

对于需要字体特征的文本渲染场景，可以使用drawSingleCharacterWithFeatures绘制单个字符，使用measureSingleCharacterWithFeatures测量单个字符的宽度，示例代码和效果图如下：

```
1. // 创建字型对象
2. const font = new drawing.Font();
3. // 设置文字大小
4. font.setSize(100);
5. let startX = 100;
6. let startY = 100;
7. let text = ['a', '2', '+', 'b', '2'];
8. // 创建字体特征对象数组
9. let fontFeatures: drawing.FontFeature[] = [{name: 'frac', value: 1}];
10. for (let s of text) {
11. // 单字绘制
12. canvas.drawSingleCharacterWithFeatures(s, font, startX, startY, fontFeatures);
13. // 测量单个字符的宽度
14. let textWidth = font.measureSingleCharacterWithFeatures(s, fontFeatures);
15. startX += textWidth;
16. }
```

[TextBlockDrawing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/TextBlockDrawing.ets#L157-L174)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/ZT5hrsP0RlCjUTAWQuIj9A/zh-cn_image_0000002552799014.png?HW-CC-KV=V1&HW-CC-Date=20260427T234711Z&HW-CC-Expire=86400&HW-CC-Sign=62B235D2C354B75FC28F0998139F6404ED4B113879B073635A4AA0814B5430D1)

说明

如果 drawSingleCharacterWithFeatures 与 measureSingleCharacter 混合使用，或者 drawSingleCharacter 与 measureSingleCharacterWithFeatures 混合使用，字体绘制可能会重叠。

## 示例代码

* [图形绘制（ArkTS）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/ArkTSGraphicsDraw)
