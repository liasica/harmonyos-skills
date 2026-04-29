---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/textblock-drawing-c
title: 字块绘制（C/C++）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 图形绘制与显示 > 图元绘制 > 字块绘制（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4789e9771abe9de4e890951888848b5fcc0a917351215e4661cdef66f5ad87be
---

## 场景介绍

字块（TextBlob）是指文本的集合。无论是单个的文字还是大块的文本，都可以通过字块来绘制。

除了基本的字块绘制之外，还可以给文字添加各种绘制效果。常见的字块绘制场景包括[文字描边](textblock-drawing-c.md#文字描边)、[文字渐变](textblock-drawing-c.md#文字渐变)等，更多效果请见[绘制效果](drawing-effect-overview.md)。

本节不涉及文本测量和布局排版相关内容，如需在开发中处理此类文本绘制需求，可参考[文本开发概述](text-overview.md)，该文档系统讲解了排版策略与相关使用指导。

## 基本字块绘制

使用OH\_Drawing\_CanvasDrawTextBlob()接口绘制字块，接口接受4个参数，分别为：画布Canvas对象、字块对象、文字基线左端点的x坐标和y坐标。

画布Canvas对象具体可见[画布的获取与绘制结果的显示（C/C++）](canvas-get-result-draw-c.md)。

字块对象可以通过多种方式创建得到，详细的字块创建方式请参考[drawing\_text\_blob.h](../harmonyos-references/capi-drawing-text-blob-h.md)。

此处以使用OH\_Drawing\_TextBlobCreateFromString()接口创建字块为例，接口接受3个参数，分别为：

* 需要显示的文本字符串内容。
* 指向OH\_Drawing\_Font字体对象的指针。OH\_Drawing\_Font用于设置和获取字体的各种属性，如字体大小、文本样式、字体对齐方式、字体渲染方式、字体描边方式等，详细的API介绍请参考[draw\_font](../harmonyos-references/capi-drawing-font-h.md)。
* 文本编码方式。

简单示例和示意图如下所示：

```
1. // 创建字体对象
2. OH_Drawing_Font *font = OH_Drawing_FontCreate();
3. // 设置字体大小
4. OH_Drawing_FontSetTextSize(font, value100_);
5. // 需要绘制的文字
6. const char *str = "Hello world";
7. // 创建字块对象
8. OH_Drawing_TextBlob *textBlob =
9. OH_Drawing_TextBlobCreateFromString(str, font, OH_Drawing_TextEncoding::TEXT_ENCODING_UTF8);
10. // 绘制字块
11. OH_Drawing_CanvasDrawTextBlob(canvas, textBlob, value200_, value800_);
12. // 释放字块对象
13. OH_Drawing_TextBlobDestroy(textBlob);
14. // 释放字体对象
15. OH_Drawing_FontDestroy(font);
```

[sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L1136-L1152)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/rkUUWUp7SJyLTHfS2-Hfrw/zh-cn_image_0000002589325037.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053610Z&HW-CC-Expire=86400&HW-CC-Sign=ED93BF8BF6B51C5EB82EA34169E3FFFA385F7177A074A05EAE6607FB50213BD5)

## 文字描边

基于基本的字块绘制，还可以通过画笔实现文字描边效果，描边效果的更多介绍请参考[描边效果](basic-drawing-effect-c.md#描边效果)。

以下以英文文字描边和中文文字描边给出示例和指导。

### 英文文字描边

英文文字描边的简要示例和示意图如下：

```
1. // 创建画笔
2. OH_Drawing_Pen *pen = OH_Drawing_PenCreate();
3. // 设置抗锯齿
4. OH_Drawing_PenSetAntiAlias(pen, true);
5. // 设置描边颜色
6. OH_Drawing_PenSetColor(pen, OH_Drawing_ColorSetArgb(RGBA_MAX, RGBA_MAX, RGBA_MIN, RGBA_MIN));
7. // 设置描边线宽为3
8. OH_Drawing_PenSetWidth(pen, 3);
9. // 设置画笔描边效果
10. OH_Drawing_CanvasAttachPen(canvas, pen);
11. // 创建字型对象
12. OH_Drawing_Font *font = OH_Drawing_FontCreate();
13. // 设置字体大小
14. OH_Drawing_FontSetTextSize(font, value150_);
15. const char *str = "Hello world";
16. // 创建字块对象
17. OH_Drawing_TextBlob *textBlob =
18. OH_Drawing_TextBlobCreateFromString(str, font, OH_Drawing_TextEncoding::TEXT_ENCODING_UTF8);
19. // 绘制字块
20. OH_Drawing_CanvasDrawTextBlob(canvas, textBlob, value200_, value800_);
21. // 去除描边效果
22. OH_Drawing_CanvasDetachPen(canvas);
23. // 销毁各类对象
24. OH_Drawing_TextBlobDestroy(textBlob);
25. OH_Drawing_FontDestroy(font);
26. OH_Drawing_PenDestroy(pen);
```

[sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L1157-L1184)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/RJK-6lrQTrmTDh4kFdccmg/zh-cn_image_0000002589244973.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053610Z&HW-CC-Expire=86400&HW-CC-Sign=B0B2D0D01963302B8A579BB227EA397C8FC4F0CB44CD0355B77A12A90E7DC763)

### 中文文字描边

首先需要通过画笔描边，然后需要调用画刷填充内部颜色，去除字体中间的杂质和重叠部分，实现中文文字描边效果。

中文文字描边的简要示例和示意图如下：

```
1. // 创建画刷
2. OH_Drawing_Brush *brush = OH_Drawing_BrushCreate();
3. // 创建画笔
4. OH_Drawing_Pen *pen = OH_Drawing_PenCreate();
5. // 设置画刷抗锯齿
6. OH_Drawing_BrushSetAntiAlias(brush, true);
7. // 设置画刷描边颜色
8. OH_Drawing_BrushSetColor(brush, OH_Drawing_ColorSetArgb(0xFF, 0xFF, 0xFF, 0xFF));
9. // 设置画笔抗锯齿
10. OH_Drawing_PenSetAntiAlias(pen, true);
11. // 设置描边线宽为3
12. OH_Drawing_PenSetWidth(pen, 3);
13. // 设置画笔描边颜色
14. OH_Drawing_PenSetColor(pen, OH_Drawing_ColorSetArgb(0xFF, 0xFF, 0x00, 0x00));
15. // 设置画笔描边效果
16. OH_Drawing_CanvasAttachPen(canvas, pen);
17. // 创建字型对象
18. OH_Drawing_Font *font = OH_Drawing_FontCreate();
19. // 设置字体大小
20. OH_Drawing_FontSetTextSize(font, value150_);
21. const char *str = "你好";
22. // 创建字块对象
23. OH_Drawing_TextBlob *textBlob =
24. OH_Drawing_TextBlobCreateFromString(str, font, OH_Drawing_TextEncoding::TEXT_ENCODING_UTF8);
25. // 绘制字块
26. OH_Drawing_CanvasDrawTextBlob(canvas, textBlob, value200_, value800_);
27. // 去除描边效果
28. OH_Drawing_CanvasDetachPen(canvas);
29. // 设置画刷描边效果
30. OH_Drawing_CanvasAttachBrush(canvas, brush);
31. OH_Drawing_CanvasDrawTextBlob(canvas, textBlob, value200_, value800_);

33. // 销毁各类对象
34. OH_Drawing_TextBlobDestroy(textBlob);
35. OH_Drawing_FontDestroy(font);
36. OH_Drawing_PenDestroy(pen);
37. OH_Drawing_BrushDestroy(brush);
```

[sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L1189-L1227)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/eNCXsb5ZRCm-FJtIzl5GnQ/zh-cn_image_0000002558765168.png?HW-CC-KV=V1&HW-CC-Date=20260429T053610Z&HW-CC-Expire=86400&HW-CC-Sign=757B7790E764AF4DB6E8FCF2C6B63412E03BA27DC578ECE734360FFA26D7ACD1)

## 文字渐变

基于基本字块绘制，还可以通过着色器实现文字渐变的效果，着色器的更多介绍请参考[着色器效果](complex-drawing-effect-c.md#着色器效果)。

以下为文字添加了线性渐变着色器效果的简要示例和示意图：

```
1. // 开始点
2. OH_Drawing_Point *startPt = OH_Drawing_PointCreate(value100_, value100_);
3. // 结束点
4. OH_Drawing_Point *endPt = OH_Drawing_PointCreate(value900_, value900_);
5. // 颜色数组
6. uint32_t colors[] = {0xFFFFFF00, 0xFFFF0000, 0xFF0000FF};
7. // 相对位置数组
8. float pos[] = {0.0f, 0.5f, 1.0f};
9. // 创建线性渐变着色器效果
10. OH_Drawing_ShaderEffect *colorShaderEffect =
11. OH_Drawing_ShaderEffectCreateLinearGradient(startPt, endPt, colors, pos, 3, OH_Drawing_TileMode::CLAMP);
12. // 创建画刷对象
13. OH_Drawing_Brush *brush = OH_Drawing_BrushCreate();
14. // 基于画刷设置着色器效果
15. OH_Drawing_BrushSetShaderEffect(brush, colorShaderEffect);
16. // 设置画刷填充效果
17. OH_Drawing_CanvasAttachBrush(canvas, brush);
18. // 创建字型对象
19. OH_Drawing_Font *font = OH_Drawing_FontCreate();
20. // 设置字体大小
21. OH_Drawing_FontSetTextSize(font, value150_);
22. const char *str = "Hello world";
23. // 创建字块对象
24. OH_Drawing_TextBlob *textBlob =
25. OH_Drawing_TextBlobCreateFromString(str, font, OH_Drawing_TextEncoding::TEXT_ENCODING_UTF8);
26. // 绘制字块
27. OH_Drawing_CanvasDrawTextBlob(canvas, textBlob, value200_, value800_);
28. // 取消填充效果
29. OH_Drawing_CanvasDetachBrush(canvas);
30. // 销毁各类对象
31. OH_Drawing_TextBlobDestroy(textBlob);
32. OH_Drawing_FontDestroy(font);
33. OH_Drawing_BrushDestroy(brush);
```

[sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L1232-L1266)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/SQjeT6aDQo6fx1AKyWQgfA/zh-cn_image_0000002558605512.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053610Z&HW-CC-Expire=86400&HW-CC-Sign=3F75E5F3247E3EF8CAC90DEA79F060BB61F1293043F5A1431BABE41F41E555AD)

## 主题字体

主题字体，特指系统**主题应用**中能使用的字体，属于一种特殊的自定义字体。如需涉及文本测量和布局排版相关内容，可参考[使用主题字体（C/C++）](theme-font-c.md)。

设置跟随主题字体的示例代码和效果图如下：

```
1. // 创建字型对象
2. OH_Drawing_Font *font = OH_Drawing_FontCreate();
3. // 设置文字大小
4. OH_Drawing_FontSetTextSize(font, value100_);
5. // 设置跟随主题字体
6. OH_Drawing_FontSetThemeFontFollowed(font, true);
7. // 需要绘制的文字
8. const char *str = "Hello World";
9. // 创建字块对象
10. OH_Drawing_TextBlob *textBlob =
11. OH_Drawing_TextBlobCreateFromString(str, font, OH_Drawing_TextEncoding::TEXT_ENCODING_UTF8);
12. // 绘制字块
13. OH_Drawing_CanvasDrawTextBlob(canvas, textBlob, value200_, value800_);
14. // 释放字块对象
15. OH_Drawing_TextBlobDestroy(textBlob);
16. // 释放字型对象
17. OH_Drawing_FontDestroy(font);
```

[sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L1271-L1289)

| 未跟随主题字体的效果图 | 跟随主题字体的效果图（不同主题字体显示效果不同，此处仅示意） |
| --- | --- |
|  |  |

说明

需要在应用入口文件（默认工程中为EntryAbility.ets）中重写onConfigurationUpdate函数，以响应切换主题字体的操作，确保切换后页面能够及时刷新并生效。具体实现可参考[使用主题字体（C/C++）](theme-font-c.md)。

## 单字绘制

单字绘制是图形渲染中针对文本渲染的一种精细化控制技术。相比字块绘制，其核心优势在于能够利用字体退化机制，在当前字体无法显示某字符时，自动退化到使用系统字体绘制字符，提升对特殊字符的兼容性，避免字符缺失。同时，单字绘制支持逐字符配置字体特征（如连字、替代字形），满足复杂排版需求，增强用户体验。详细API说明请见[drawing\_canvas.h](../harmonyos-references/capi-drawing-canvas-h.md#oh_drawing_canvasdrawsinglecharacter)。

基础场景：绘制无字体特征的字符。

对于无需字体特征的常规文本渲染场景，可以使用OH\_Drawing\_CanvasDrawSingleCharacter绘制单个字符，使用OH\_Drawing\_FontMeasureSingleCharacter测量单个字符的宽度，示例代码和效果图如下：

```
1. // 创建字型对象
2. OH_Drawing_Font *font = OH_Drawing_FontCreate();
3. // 设置文字大小
4. OH_Drawing_FontSetTextSize(font, value100_);
5. float startX = 100;
6. float startY = 100;
7. int strLen = 5;
8. const char* str = "Hello";
9. for (int i = 0; i < strLen; ++i) {
10. // 单字绘制
11. OH_Drawing_CanvasDrawSingleCharacter(canvas, &str[i], font, startX, startY);
12. float textWidth = 0.f;
13. // 测量单个字符的宽度
14. OH_Drawing_FontMeasureSingleCharacter(font, &str[i], &textWidth);
15. startX += textWidth;
16. }
17. // 释放字型对象
18. OH_Drawing_FontDestroy(font);
```

[sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L1294-L1313)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/Mu0WTaUhSmi15VG-8TmDBg/zh-cn_image_0000002558605506.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053610Z&HW-CC-Expire=86400&HW-CC-Sign=18B524CDACDFE847630C07F33ADB620194D0A9BFD2B28EDD01891306A6E45C27)

进阶场景：绘制带字体特征的字符。

对于需要字体特征的文本渲染场景，可以使用OH\_Drawing\_CanvasDrawSingleCharacterWithFeatures绘制单个字符，使用OH\_Drawing\_FontMeasureSingleCharacterWithFeatures测量单个字符的宽度，示例代码和效果图如下：

```
1. // 创建字型对象
2. OH_Drawing_Font *font = OH_Drawing_FontCreate();
3. // 设置文字大小
4. OH_Drawing_FontSetTextSize(font, value100_);
5. // 创建字体特征对象
6. OH_Drawing_FontFeatures* features = OH_Drawing_FontFeaturesCreate();
7. OH_Drawing_FontFeaturesAddFeature(features, "frac", 1);
8. float startX = 100;
9. float startY = 100;
10. int strLen = 5;
11. const char* str = "a2+b2";
12. for (int i = 0; i < strLen; ++i) {
13. // 单字绘制
14. OH_Drawing_CanvasDrawSingleCharacterWithFeatures(canvas, &str[i], font, startX, startY, features);
15. float textWidth = 0.f;
16. // 测量单个字符的宽度
17. OH_Drawing_FontMeasureSingleCharacterWithFeatures(font, &str[i], features, &textWidth);
18. startX += textWidth;
19. }
20. // 释放字体特征对象
21. OH_Drawing_FontFeaturesDestroy(features);
22. // 释放字型对象
23. OH_Drawing_FontDestroy(font);
```

[sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L1318-L1342)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/kZBIybrnSfGGFWbY5B7N-Q/zh-cn_image_0000002589325033.png?HW-CC-KV=V1&HW-CC-Date=20260429T053610Z&HW-CC-Expire=86400&HW-CC-Sign=368D9EE8F23810547043CAE8CCE516A2305DA6A22B8FE05CD71615EB0556E928)

说明

如果 OH\_Drawing\_CanvasDrawSingleCharacterWithFeatures 与 OH\_Drawing\_FontMeasureSingleCharacter 混合使用，或者 OH\_Drawing\_CanvasDrawSingleCharacter 与 OH\_Drawing\_FontMeasureSingleCharacterWithFeatures 混合使用，字体绘制可能会重叠。

## 示例代码

* [图形绘制（C/C++）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKGraphicsDraw)
