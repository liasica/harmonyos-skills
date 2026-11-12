---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/textblock-drawing-arkts
title: 字块绘制（ArkTS）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 图形绘制与显示 > 图元绘制 > 字块绘制（ArkTS）
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:efbac01005617a5ae16bd61614350fa6cd89d8d596afc49addc30048c9a22d35
---

## 场景介绍

字块（TextBlob）是指文本的集合。无论是单个的文字还是大块的文本，都可以通过字块来绘制。

除了基本的字块绘制之外，还可以给文字添加各种绘制效果。常见的字块绘制场景包括[文字描边](textblock-drawing-arkts.md#文字描边)、[文字渐变](textblock-drawing-arkts.md#文字渐变)、[字体回退](textblock-drawing-arkts.md#字体回退)等，更多效果请见[绘制效果](drawing-effect-overview.md)。

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

```typescript
// 创建字型对象
const font = new drawing.Font();
// 设置字体大小
font.setSize(100);
// 创建字块对象
const textBlob = drawing.TextBlob.makeFromString('Hello world', font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
// 绘制字块
canvas.drawTextBlob(textBlob, VALUE_200, VALUE_300);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/9PjSDVmoQ0K7Y4s4T4QPDA/zh-cn_image_0000002786519954.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5BF1D042DCB69FE39B7D0249B9FFB2D6E3974F4B97A7C78715B3E160F25F1F9)

## 文字描边

基于基本的字块绘制，还可以通过画笔实现文字描边效果，描边效果的更多介绍请参考[描边效果](basic-drawing-effect-arkts.md#描边效果)。

以下以英文文字描边和中文文字描边给出示例和指导。

### 英文文字描边

英文文字描边的简要示例和示意图如下：

```typescript
// 创建画笔
let pen = new drawing.Pen();
// 设置抗锯齿
pen.setAntiAlias(true);
// 设置描边线宽
pen.setStrokeWidth(3.0);
// 设置描边颜色
pen.setColor(0xFF, 0xFF, 0x00, 0x00);
// 创建字型对象
const font = new drawing.Font();
// 设置字体大小
font.setSize(100);
// 添加画笔描边效果
canvas.attachPen(pen);
// 创建字块对象
const textBlob = drawing.TextBlob.makeFromString('Hello world', font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
// 绘制字块
canvas.drawTextBlob(textBlob, VALUE_200, VALUE_300);
// 去除描边效果
canvas.detachPen();
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/Ek21FJrTRaaeYKyFkTbh_w/zh-cn_image_0000002786360026.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=658B2EEEA582BF42A63E7243DACA1DCB3FD153A415764FA8F7474DAC185333D5)

### 中文文字描边

首先需要通过画笔描边，然后需要调用画刷填充内部颜色，去除字体中间的杂质和重叠部分，实现中文文字描边效果。

中文文字描边的简要示例和示意图如下：

```typescript
// 创建画刷
let brush = new drawing.Brush();
// 创建画笔
let pen = new drawing.Pen();
// 设置抗锯齿
brush.setAntiAlias(true);
// 设置填充颜色
brush.setColor(0xFF, 0xFF, 0xFF, 0xFF);

pen.setAntiAlias(true);
// 设置描边线宽
pen.setStrokeWidth(3.0);
// 设置描边颜色
pen.setColor(0xFF, 0xFF, 0x00, 0x00);

// 创建字型对象
const font = new drawing.Font();
// 设置字体大小
font.setSize(100);
// 添加画笔描边效果
canvas.attachPen(pen);
// 创建字块对象
const textBlob = drawing.TextBlob.makeFromString(STROKE_SAMPLE, font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
// 绘制字块
canvas.drawTextBlob(textBlob, VALUE_200,  VALUE_300);
// 去除描边效果
canvas.detachPen();

canvas.attachBrush(brush);
canvas.drawTextBlob(textBlob, VALUE_200, VALUE_300);
canvas.detachBrush();
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/I4tR0ehIRN6xuEztCe__oQ/zh-cn_image_0000002815559447.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=6880AF09D31886F252147E1C3C555A33463285FF2FEB2C1974BD72A7F81F9C69)

## 文字渐变

基于基本字块绘制，还可以通过着色器实现文字渐变的效果，着色器的更多介绍请参考[着色器效果](complex-drawing-effect-arkts.md#着色器效果)。

以下为文字添加了线性渐变着色器效果的简要示例和示意图：

```typescript
let startPt: common2D.Point = { x: VALUE_100, y: VALUE_100 };
let endPt: common2D.Point = { x: VALUE_900, y: VALUE_900 };
let colors = [0xFFFFFF00, 0xFFFF0000, 0xFF0000FF];
// 创建线性渐变着色器
let shaderEffect = drawing.ShaderEffect.createLinearGradient(startPt, endPt, colors, drawing.TileMode.CLAMP);
// 创建画刷
let brush = new drawing.Brush();
// 设置着色器
brush.setShaderEffect(shaderEffect);
// 添加画刷填充效果
canvas.attachBrush(brush);
// 创建字型
const font = new drawing.Font();
// 设置字体大小
font.setSize(VALUE_200);
// 创建字块
const textBlob = drawing.TextBlob.makeFromString('Hello world', font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
// 绘制字块
canvas.drawTextBlob(textBlob, VALUE_100, VALUE_300);
// 去除填充效果
canvas.detachBrush();
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/21BylubFSuyAmG8rmg1_Yg/zh-cn_image_0000002815399531.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=122471AD0DC41C0FBA2440E372E112B76299A657EE79EFC5390EA860BF5369B0)

## 主题字体

主题字体，特指系统**主题应用**中能使用的字体，属于一种特殊的自定义字体。如需涉及文本测量和布局排版相关内容，可参考[使用主题字体（ArkTS）](theme-font-arkts.md)。

设置跟随主题字体的示例代码和效果图如下：

```typescript
// 创建字型对象
const font = new drawing.Font();
// 设置文字大小
font.setSize(100);
// 设置跟随主题字体
font.setThemeFontFollowed(true);
// 创建字块对象
const textBlob = drawing.TextBlob.makeFromString('Hello World', font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
// 绘制字块
canvas.drawTextBlob(textBlob, VALUE_200, VALUE_300);
```

| 未跟随主题字体的效果图 | 跟随主题字体的效果图（不同主题字体显示效果不同，此处仅示意） |
| --- | --- |
|  |  |

**说明** 

需要在应用入口文件（默认工程中为EntryAbility.ets）中复写onConfigurationUpdate函数，以响应切换主题字体的操作，确保切换后页面能够及时刷新并生效。具体实现可参考[使用主题字体（ArkTS）](theme-font-arkts.md)。

## 单字绘制

单字绘制是图形渲染中针对文本渲染的一种精细化控制技术。相比字块绘制，其核心优势在于能够利用字体退化机制，在当前字体无法显示某字符时，自动退化到使用系统字体绘制字符，提升对特殊字符的兼容性，避免字符缺失。同时，单字绘制支持逐字符配置字体特征（如连字、替代字形），满足复杂排版需求，增强用户体验。详细API说明请见[drawSingleCharacter](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#drawsinglecharacter12)。

基础场景：绘制无字体特征的字符。

对于无需字体特征的常规文本渲染场景，可以使用drawSingleCharacter绘制单个字符，使用measureSingleCharacter测量单个字符的宽度，示例代码和效果图如下：

```typescript
// 创建字型对象
const font = new drawing.Font();
// 设置文字大小
font.setSize(100);
let startX = 100;
let startY = 100;
let text = ['H', 'e', 'l', 'l', 'o'];
for (let s of text) {
  // 单字绘制
  canvas.drawSingleCharacter(s, font, startX, startY);
  // 测量单个字符的宽度
  let textWidth = font.measureSingleCharacter(s);
  startX += textWidth;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/4hb-_scMRzmYDJb0rhJcbQ/zh-cn_image_0000002815559449.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=D950D60B0F2BE1C5725B4610BCA02939BCD885D5277E8612DEB83009A076BF9F)

进阶场景：绘制带字体特征的字符。

对于需要字体特征的文本渲染场景，可以使用drawSingleCharacterWithFeatures绘制单个字符，使用measureSingleCharacterWithFeatures测量单个字符的宽度，示例代码和效果图如下：

```typescript
// 创建字型对象
const font = new drawing.Font();
// 设置文字大小
font.setSize(100);
let startX = 100;
let startY = 100;
let text = ['a', '2', '+', 'b', '2'];
// 创建字体特征对象数组
let fontFeatures: drawing.FontFeature[] = [{name: 'frac', value: 1}];
for (let s of text) {
  // 单字绘制
  canvas.drawSingleCharacterWithFeatures(s, font, startX, startY, fontFeatures);
  // 测量单个字符的宽度
  let textWidth = font.measureSingleCharacterWithFeatures(s, fontFeatures);
  startX += textWidth;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/IoGr0vRnQJ2Peo6OC8mj_A/zh-cn_image_0000002815399533.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=45EED56F494AD86C0621D5EB3000B8D2748AE4A943383298EEFF690DEB7FCFC6)

**说明** 

如果 drawSingleCharacterWithFeatures 与 measureSingleCharacter 混合使用，或者 drawSingleCharacter 与 measureSingleCharacterWithFeatures 混合使用，字体绘制可能会重叠。

## 字体回退

在实际开发中，开发者指定的字体未必能覆盖文本中的全部字符，例如一个仅包含拉丁字符的字体无法显示中文、阿拉伯文等字符。此时若直接使用该字体绘制文本，不在字体覆盖范围内的字符将无法正常显示。字体回退（Font Fallback）能力可以自动从系统字体中查找能够支持这些字符的字体进行显示，从而兼顾字体风格统一与文本的完整呈现，开发者无需自行判断字符覆盖范围，也无需为不同语言单独指定字体。若系统字体中仍无支持某字符的字体，则该字符依旧无法正常显示。

当需要注意字符覆盖范围、或需要在一段文本中混用多种语言时，即可使用本节介绍的支持字体回退的接口。[单字绘制](textblock-drawing-arkts.md#单字绘制)也具备字体回退能力，适用于逐字符渲染场景；本节介绍的是字块创建、字形转换与文本宽度测量场景下的字体回退接口。详细的API介绍请参考[TextBlob](../harmonyos-references/arkts-apis-graphics-drawing-textblob.md)和[Font](../harmonyos-references/arkts-apis-graphics-drawing-font.md)。

**说明** 

从API版本26.0.1开始，新增字体回退功能。

### 字块绘制支持字体回退

当指定的字体无法覆盖文本中的所有字符时，可以使用支持字体回退的字块创建接口[makeFromStringWithFallback()](../harmonyos-references/arkts-apis-graphics-drawing-textblob.md#makefromstringwithfallback)或[makeFromPosTextWithFallback()](../harmonyos-references/arkts-apis-graphics-drawing-textblob.md#makefrompostextwithfallback)。接口会自动为不支持的字符查找系统回退字体，并按字体将文本分组，生成一组字块对象。绘制时，需将所有字块绘制在同一坐标原点，即可完整呈现整段文本。

主要实现步骤如下：创建字型对象并设置字体 → 准备文本 → 调用回退接口获取字块数组 → 遍历数组，在同一原点绘制每个字块。

使用[makeFromStringWithFallback()](../harmonyos-references/arkts-apis-graphics-drawing-textblob.md#makefromstringwithfallback)接口从字符串创建支持字体回退的字块数组并绘制的示例代码如下：

```typescript
// 创建字型对象
const font = new drawing.Font();
// 创建字体对象
const myTypeface = drawing.Typeface.makeFromFile('/system/fonts/NotoSansArmenian[wdth,wght].ttf');
// 为字型设置字体
font.setTypeface(myTypeface);
// 设置字体大小
font.setSize(VALUE_100);
// 创建支持字体回退的字块数组
const textBlobs = drawing.TextBlob.makeFromStringWithFallback('Hello世界', font);
// 遍历字块数组并绘制，每个TextBlob绘制在相同原点
for (let textBlob of textBlobs) {
  canvas.drawTextBlob(textBlob, VALUE_200, VALUE_300);
}
```

| 使用不回退接口makeFromString()的效果图 | 使用回退接口makeFromStringWithFallback()的效果图 |
| --- | --- |
|  |  |

使用[makeFromPosTextWithFallback()](../harmonyos-references/arkts-apis-graphics-drawing-textblob.md#makefrompostextwithfallback)接口从文本和坐标点数组创建支持字体回退的字块数组并绘制的示例代码如下：

```typescript
// 创建字型对象
const font = new drawing.Font();
// 创建字体对象
const myTypeface = drawing.Typeface.makeFromFile('/system/fonts/NotoSansArmenian[wdth,wght].ttf');
// 为字型设置字体
font.setTypeface(myTypeface);
// 设置字体大小
font.setSize(VALUE_100);
// 需要绘制的文本
const text = 'Hello世界';
// 获取glyph数量
const glyphCount = font.countText(text);
// 为每个字符指定坐标位置
let points: common2D.Point[] = [];
let xOffset = 0;
for (let i = 0; i < glyphCount; i++) {
  points.push({ x: VALUE_200 + xOffset, y: VALUE_300 });
  xOffset += 60;
}
// 创建支持字体回退的字块数组
const textBlobs = drawing.TextBlob.makeFromPosTextWithFallback(text, glyphCount, points, font);
// 遍历字块数组并绘制
for (let textBlob of textBlobs) {
  canvas.drawTextBlob(textBlob, 0, 0);
}
```

| 使用不回退接口makeFromPosText()的效果图 | 使用回退接口makeFromPosTextWithFallback()的效果图 |
| --- | --- |
|  |  |

### 字形转换与文本宽度测量支持字体回退

当需要将文本转换为字形，或测量文本在字体回退后的实际宽度时，可以使用Font提供的支持字体回退的字形转换接口[textToGlyphsWithFallback()](../harmonyos-references/arkts-apis-graphics-drawing-font.md#texttoglyphswithfallback)和文本宽度测量接口[measureTextWithFallback()](../harmonyos-references/arkts-apis-graphics-drawing-font.md#measuretextwithfallback)。

使用[textToGlyphsWithFallback()](../harmonyos-references/arkts-apis-graphics-drawing-font.md#texttoglyphswithfallback)将文本转换为字形信息（转换时自动按回退字体分组），再逐组设置对应字体、根据字形宽度计算位置，最后通过[drawGlyphs()](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#drawglyphs)绘制。示例代码如下：

```typescript
// 创建字型对象
const font = new drawing.Font();
// 创建字体对象
const myTypeface = drawing.Typeface.makeFromFile('/system/fonts/NotoSansArmenian[wdth,wght].ttf');
// 为字型设置字体
font.setTypeface(myTypeface);
// 设置字体大小
font.setSize(VALUE_100);
// 需要转换的文本
const text = 'Hello世界';
// 获取glyph数量
const glyphCount = font.countText(text);
// 将文本转换为glyph索引，支持字体回退
const fallbackInfos = font.textToGlyphsWithFallback(text, glyphCount);
// 使用drawGlyphs按回退字体分组绘制字形
let xOffset = 0;
// 遍历回退信息，每个元素包含相同typeface的glyph ID数组
for (let info of fallbackInfos) {
  // info.typeface为匹配的字体
  // info.glyphIds为该字体对应的glyph ID数组
  font.setTypeface(info.typeface);
  let positions: common2D.Point[] = [];
  let glyphWidths = font.getWidths(info.glyphIds);
  for (let j = 0; j < info.glyphIds.length; j++) {
    positions.push({ x: VALUE_200 + xOffset, y: VALUE_300 });
    xOffset += glyphWidths[j];
  }
  canvas.drawGlyphs(info.glyphIds, 0, positions, 0, info.glyphIds.length, font);
}
```

| 使用不回退接口textToGlyphs()的效果图 | 使用回退接口textToGlyphsWithFallback()的效果图 |
| --- | --- |
|  |  |

使用[measureTextWithFallback()](../harmonyos-references/arkts-apis-graphics-drawing-font.md#measuretextwithfallback)接口测量文本在字体回退后实际宽度的示例代码如下：

```typescript
// 创建字型对象
const font = new drawing.Font();
// 创建字体对象
const myTypeface = drawing.Typeface.makeFromFile('/system/fonts/NotoSansArmenian[wdth,wght].ttf');
// 为字型设置字体
font.setTypeface(myTypeface);
// 设置字体大小
font.setSize(VALUE_100);
// 需要测量的文本
const text = 'Hello世界';
// 测量文本宽度，支持字体回退
const textWidth = font.measureTextWithFallback(text, drawing.TextEncoding.TEXT_ENCODING_UTF8);
console.info('textWidth: ' + textWidth);
```

## 示例代码

* [图形绘制（ArkTS）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/ArkTSGraphicsDraw)
