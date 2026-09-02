---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/textblock-drawing-c
title: 字块绘制（C/C++）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 图形绘制与显示 > 图元绘制 > 字块绘制（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:49+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:f3726e52532f60fb40abb7a54dae260c928a3651af66ad0c3d8938f7a1d8f109
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
* 指向OH\_Drawing\_Font字体对象的指针。OH\_Drawing\_Font用于设置和获取字体的各种属性，如字体大小、文本样式、字体对齐方式、字体渲染方式、字体描边方式等，详细的API介绍请参考[drawing\_font.h](../harmonyos-references/capi-drawing-font-h.md)。
* 文本编码方式。

简单示例和示意图如下所示：

```
// 创建字体对象
OH_Drawing_Font *font = OH_Drawing_FontCreate();
// 设置字体大小
OH_Drawing_FontSetTextSize(font, value100_);
// 需要绘制的文字
const char *str = "Hello world";
// 创建字块对象
OH_Drawing_TextBlob *textBlob =
    OH_Drawing_TextBlobCreateFromString(str, font, TEXT_ENCODING_UTF8);
// 绘制字块
OH_Drawing_CanvasDrawTextBlob(canvas, textBlob, value200_, value800_);
// 释放字块对象
OH_Drawing_TextBlobDestroy(textBlob);
// 释放字体对象
OH_Drawing_FontDestroy(font);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/nasQKMgKSFy7NxZDFDyVmQ/zh-cn_image_0000002736313769.jpg)

## 文字描边

基于基本的字块绘制，还可以通过画笔实现文字描边效果，描边效果的更多介绍请参考[描边效果](basic-drawing-effect-c.md#描边效果)。

以下以英文文字描边和中文文字描边给出示例和指导。

### 英文文字描边

英文文字描边的简要示例和示意图如下：

```
// 创建画笔
OH_Drawing_Pen *pen = OH_Drawing_PenCreate();
// 设置抗锯齿
OH_Drawing_PenSetAntiAlias(pen, true);
// 设置描边颜色
OH_Drawing_PenSetColor(pen, OH_Drawing_ColorSetArgb(RGBA_MAX, RGBA_MAX, RGBA_MIN, RGBA_MIN));
// 设置描边线宽为3
OH_Drawing_PenSetWidth(pen, 3);
// 设置画笔描边效果
OH_Drawing_CanvasAttachPen(canvas, pen);
// 创建字型对象
OH_Drawing_Font *font = OH_Drawing_FontCreate();
// 设置字体大小
OH_Drawing_FontSetTextSize(font, value150_);
const char *str = "Hello world";
// 创建字块对象
OH_Drawing_TextBlob *textBlob =
    OH_Drawing_TextBlobCreateFromString(str, font, TEXT_ENCODING_UTF8);
// 绘制字块
OH_Drawing_CanvasDrawTextBlob(canvas, textBlob, value200_, value800_);
// 去除描边效果
OH_Drawing_CanvasDetachPen(canvas);
// 销毁各类对象
OH_Drawing_TextBlobDestroy(textBlob);
OH_Drawing_FontDestroy(font);
OH_Drawing_PenDestroy(pen);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/6lovNYoCTlCR0xI4Mkht0g/zh-cn_image_0000002706674726.jpg)

### 中文文字描边

首先需要通过画笔描边，然后需要调用画刷填充内部颜色，去除字体中间的杂质和重叠部分，实现中文文字描边效果。

中文文字描边的简要示例和示意图如下：

```
// 创建画刷
OH_Drawing_Brush *brush = OH_Drawing_BrushCreate();
// 创建画笔
OH_Drawing_Pen *pen = OH_Drawing_PenCreate();
// 设置画刷抗锯齿
OH_Drawing_BrushSetAntiAlias(brush, true);
// 设置画刷填充颜色
OH_Drawing_BrushSetColor(brush, OH_Drawing_ColorSetArgb(0xFF, 0xFF, 0xFF, 0xFF));
// 设置画笔抗锯齿
OH_Drawing_PenSetAntiAlias(pen, true);
// 设置描边线宽为3
OH_Drawing_PenSetWidth(pen, 3);
// 设置画笔描边颜色
OH_Drawing_PenSetColor(pen, OH_Drawing_ColorSetArgb(0xFF, 0xFF, 0x00, 0x00));
// 设置画笔描边效果
OH_Drawing_CanvasAttachPen(canvas, pen);
// 创建字型对象
OH_Drawing_Font *font = OH_Drawing_FontCreate();
// 设置字体大小
OH_Drawing_FontSetTextSize(font, value150_);
const char *str = "你好";
// 创建字块对象
OH_Drawing_TextBlob *textBlob =
    OH_Drawing_TextBlobCreateFromString(str, font, TEXT_ENCODING_UTF8);
// 绘制字块
OH_Drawing_CanvasDrawTextBlob(canvas, textBlob, value200_, value800_);
// 去除描边效果
OH_Drawing_CanvasDetachPen(canvas);
// 设置画刷填充效果
OH_Drawing_CanvasAttachBrush(canvas, brush);
OH_Drawing_CanvasDrawTextBlob(canvas, textBlob, value200_, value800_);
// 去除画布中的画刷
OH_Drawing_CanvasDetachBrush(canvas);

// 销毁各类对象
OH_Drawing_TextBlobDestroy(textBlob);
OH_Drawing_FontDestroy(font);
OH_Drawing_PenDestroy(pen);
OH_Drawing_BrushDestroy(brush);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/JAL7n7sBS-O14kzXDEpWJQ/zh-cn_image_0000002736433815.png)

## 文字渐变

基于基本字块绘制，还可以通过着色器实现文字渐变的效果，着色器的更多介绍请参考[着色器效果](complex-drawing-effect-c.md#着色器效果)。

以下为文字添加了线性渐变着色器效果的简要示例和示意图：

```
// 开始点
OH_Drawing_Point *startPt = OH_Drawing_PointCreate(value100_, value100_);
// 结束点
OH_Drawing_Point *endPt = OH_Drawing_PointCreate(value900_, value900_);
// 颜色数组
uint32_t colors[] = {0xFFFFFF00, 0xFFFF0000, 0xFF0000FF};
// 相对位置数组
float pos[] = {0.0f, 0.5f, 1.0f};
// 创建线性渐变着色器效果
OH_Drawing_ShaderEffect *colorShaderEffect =
    OH_Drawing_ShaderEffectCreateLinearGradient(startPt, endPt, colors, pos, 3, CLAMP);
// 创建画刷对象
OH_Drawing_Brush *brush = OH_Drawing_BrushCreate();
// 基于画刷设置着色器效果
OH_Drawing_BrushSetShaderEffect(brush, colorShaderEffect);
// 设置画刷填充效果
OH_Drawing_CanvasAttachBrush(canvas, brush);
// 创建字型对象
OH_Drawing_Font *font = OH_Drawing_FontCreate();
// 设置字体大小
OH_Drawing_FontSetTextSize(font, value150_);
const char *str = "Hello world";
// 创建字块对象
OH_Drawing_TextBlob *textBlob =
    OH_Drawing_TextBlobCreateFromString(str, font, TEXT_ENCODING_UTF8);
// 绘制字块
OH_Drawing_CanvasDrawTextBlob(canvas, textBlob, value200_, value800_);
// 取消填充效果
OH_Drawing_CanvasDetachBrush(canvas);
// 销毁各类对象
OH_Drawing_TextBlobDestroy(textBlob);
OH_Drawing_FontDestroy(font);
OH_Drawing_BrushDestroy(brush);
OH_Drawing_ShaderEffectDestroy(colorShaderEffect);
OH_Drawing_PointDestroy(startPt);
OH_Drawing_PointDestroy(endPt);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/vVdaH3DGSuq-BoaFiY1bCw/zh-cn_image_0000002706834664.jpg)

## 主题字体

主题字体，特指系统**主题应用**中能使用的字体，属于一种特殊的自定义字体。如需涉及文本测量和布局排版相关内容，可参考[使用主题字体（C/C++）](theme-font-c.md)。

设置跟随主题字体的示例代码和效果图如下：

```
// 创建字型对象
OH_Drawing_Font *font = OH_Drawing_FontCreate();
// 设置文字大小
OH_Drawing_FontSetTextSize(font, value100_);
// 设置跟随主题字体
OH_Drawing_FontSetThemeFontFollowed(font, true);
// 需要绘制的文字
const char *str = "Hello World";
// 创建字块对象
OH_Drawing_TextBlob *textBlob =
    OH_Drawing_TextBlobCreateFromString(str, font, TEXT_ENCODING_UTF8);
// 绘制字块
OH_Drawing_CanvasDrawTextBlob(canvas, textBlob, value200_, value800_);
// 释放字块对象
OH_Drawing_TextBlobDestroy(textBlob);
// 释放字型对象
OH_Drawing_FontDestroy(font);
```

| 未跟随主题字体的效果图 | 跟随主题字体的效果图（不同主题字体显示效果不同，此处仅示意） |
| --- | --- |
|  |  |

**说明** 

需要在应用入口文件（默认工程中为EntryAbility.ets）中重写onConfigurationUpdate函数，以响应切换主题字体的操作，确保切换后页面能够及时刷新并生效。具体实现可参考[使用主题字体（C/C++）](theme-font-c.md)。

## 单字绘制

单字绘制是图形渲染中针对文本渲染的一种精细化控制技术。相比字块绘制，其核心优势在于能够利用字体退化机制，在当前字体无法显示某字符时，自动退化到使用系统字体绘制字符，提升对特殊字符的兼容性，避免字符缺失。同时，单字绘制支持逐字符配置字体特征（如连字、替代字形），满足复杂排版需求，增强用户体验。详细API说明请见[drawing\_canvas.h](../harmonyos-references/capi-drawing-canvas-h.md#oh_drawing_canvasdrawsinglecharacter)。

基础场景：绘制无字体特征的字符。

对于无需字体特征的常规文本渲染场景，可以使用OH\_Drawing\_CanvasDrawSingleCharacter绘制单个字符，使用OH\_Drawing\_FontMeasureSingleCharacter测量单个字符的宽度，示例代码和效果图如下：

```
// 创建字型对象
OH_Drawing_Font *font = OH_Drawing_FontCreate();
// 设置文字大小
OH_Drawing_FontSetTextSize(font, value100_);
float startX = 100;
float startY = 100;
int strLen = 5;
const char* str = "Hello";
for (int i = 0; i < strLen; ++i) {
    // 单字绘制
    OH_Drawing_CanvasDrawSingleCharacter(canvas, &str[i], font, startX, startY);
    float textWidth = 0.f;
    // 测量单个字符的宽度
    OH_Drawing_FontMeasureSingleCharacter(font, &str[i], &textWidth);
    startX += textWidth;
}
// 释放字型对象
OH_Drawing_FontDestroy(font);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/n4bacl3TR1avWkv5QZP10w/zh-cn_image_0000002706834658.jpg)

进阶场景：绘制带字体特征的字符。

对于需要字体特征的文本渲染场景，可以使用OH\_Drawing\_CanvasDrawSingleCharacterWithFeatures绘制单个字符，使用OH\_Drawing\_FontMeasureSingleCharacterWithFeatures测量单个字符的宽度，示例代码和效果图如下：

```
// 创建字型对象
OH_Drawing_Font *font = OH_Drawing_FontCreate();
// 设置文字大小
OH_Drawing_FontSetTextSize(font, value100_);
// 创建字体特征对象
OH_Drawing_FontFeatures* features = OH_Drawing_FontFeaturesCreate();
OH_Drawing_FontFeaturesAddFeature(features, "frac", 1);
float startX = 100;
float startY = 100;
int strLen = 5;
const char* str = "a2+b2";
for (int i = 0; i < strLen; ++i) {
    // 单字绘制
    OH_Drawing_CanvasDrawSingleCharacterWithFeatures(canvas, &str[i], font, startX, startY, features);
    float textWidth = 0.f;
    // 测量单个字符的宽度
    OH_Drawing_FontMeasureSingleCharacterWithFeatures(font, &str[i], features, &textWidth);
    startX += textWidth;
}
// 释放字体特征对象
OH_Drawing_FontFeaturesDestroy(features);
// 释放字型对象
OH_Drawing_FontDestroy(font);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/lsx24uSuQ4CwPKIVE1Y5Zw/zh-cn_image_0000002736313765.png)

**说明** 

如果 OH\_Drawing\_CanvasDrawSingleCharacterWithFeatures 与 OH\_Drawing\_FontMeasureSingleCharacter 混合使用，或者 OH\_Drawing\_CanvasDrawSingleCharacter 与 OH\_Drawing\_FontMeasureSingleCharacterWithFeatures 混合使用，字体绘制可能会重叠。

## 示例代码

* [图形绘制（C/C++）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKGraphicsDraw)
