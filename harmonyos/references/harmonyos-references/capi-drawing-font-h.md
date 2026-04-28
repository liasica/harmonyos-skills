---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-font-h
title: drawing_font.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_font.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:42db18a0d90e9fd57bc84964516c8946d4e88853053a93bf639b37e7018193e9
---

## 概述

PhonePC/2in1TabletTVWearable

文件中定义了与字体相关的功能函数。

**引用文件：** <native\_drawing/drawing\_font.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_Font\_Metrics](capi-drawing-oh-drawing-font-metrics.md) | OH\_Drawing\_Font\_Metrics | 定义字体度量信息的结构体。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_FontHinting](capi-drawing-font-h.md#oh_drawing_fonthinting) | OH\_Drawing\_FontHinting | 字型轮廓效果类型枚举。 |
| [OH\_Drawing\_FontEdging](capi-drawing-font-h.md#oh_drawing_fontedging) | OH\_Drawing\_FontEdging | 字型边缘效果类型枚举。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontGetSpacing(const OH\_Drawing\_Font\* font, float\* spacing)](capi-drawing-font-h.md#oh_drawing_fontgetspacing) | 用于获取推荐的字型行间距。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontGetPos(const OH\_Drawing\_Font\* font, const uint16\_t\* glyphs, int count,const OH\_Drawing\_Point\* origin, OH\_Drawing\_Point2D\* points)](capi-drawing-font-h.md#oh_drawing_fontgetpos) | 用于从指定的原点开始，获取每个字形的相对位置。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontGetWidthsBounds(const OH\_Drawing\_Font\* font, const uint16\_t\* glyphs, int count,const OH\_Drawing\_Brush\* brush, const OH\_Drawing\_Pen\* pen, float\* widths, OH\_Drawing\_Array\* bounds)](capi-drawing-font-h.md#oh_drawing_fontgetwidthsbounds) | 用于获取字形数组中每个字形的宽度和边界框。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontMeasureTextWithBrushOrPen(const OH\_Drawing\_Font\* font, const void\* text,size\_t byteLength, OH\_Drawing\_TextEncoding encoding, const OH\_Drawing\_Brush\* brush, const OH\_Drawing\_Pen\* pen,OH\_Drawing\_Rect\* bounds, float\* textWidth)](capi-drawing-font-h.md#oh_drawing_fontmeasuretextwithbrushorpen) | 使用画刷或画笔获取文本的宽度和边界框。 |
| [OH\_Drawing\_Font\* OH\_Drawing\_FontCreate(void)](capi-drawing-font-h.md#oh_drawing_fontcreate) | 用于创建一个字型对象。 |
| [void OH\_Drawing\_FontSetBaselineSnap(OH\_Drawing\_Font\* font, bool baselineSnap)](capi-drawing-font-h.md#oh_drawing_fontsetbaselinesnap) | 当前画布矩阵轴对齐时，将字型基线设置为是否与像素对齐。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [bool OH\_Drawing\_FontIsBaselineSnap(const OH\_Drawing\_Font\* font)](capi-drawing-font-h.md#oh_drawing_fontisbaselinesnap) | 当前画布矩阵轴对齐时，获取字型基线是否与像素对齐。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_FontSetSubpixel(OH\_Drawing\_Font\* font, bool isSubpixel)](capi-drawing-font-h.md#oh_drawing_fontsetsubpixel) | 设置字型是否使用次像素渲染。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [bool OH\_Drawing\_FontIsSubpixel(const OH\_Drawing\_Font\* font)](capi-drawing-font-h.md#oh_drawing_fontissubpixel) | 获取字型是否使用次像素渲染。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_FontSetForceAutoHinting(OH\_Drawing\_Font\* font, bool isForceAutoHinting)](capi-drawing-font-h.md#oh_drawing_fontsetforceautohinting) | 用于设置是否自动调整字型轮廓。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [bool OH\_Drawing\_FontIsForceAutoHinting(const OH\_Drawing\_Font\* font)](capi-drawing-font-h.md#oh_drawing_fontisforceautohinting) | 获取字型轮廓是否自动调整。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_FontSetTypeface(OH\_Drawing\_Font\* font, OH\_Drawing\_Typeface\* typeface)](capi-drawing-font-h.md#oh_drawing_fontsettypeface) | 用于给字型设置字体。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_FontGetTypeface(OH\_Drawing\_Font\* font)](capi-drawing-font-h.md#oh_drawing_fontgettypeface) | 获取字体对象。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_FontSetTextSize(OH\_Drawing\_Font\* font, float textSize)](capi-drawing-font-h.md#oh_drawing_fontsettextsize) | 用于给字型对象设置文字大小。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [float OH\_Drawing\_FontGetTextSize(const OH\_Drawing\_Font\* font)](capi-drawing-font-h.md#oh_drawing_fontgettextsize) | 获取字型对象的文字大小。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [int OH\_Drawing\_FontCountText(OH\_Drawing\_Font\* font, const void\* text, size\_t byteLength,OH\_Drawing\_TextEncoding encoding)](capi-drawing-font-h.md#oh_drawing_fontcounttext) | 获取文本所表示的字符数量。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font、text任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [uint32\_t OH\_Drawing\_FontTextToGlyphs(const OH\_Drawing\_Font\* font, const void\* text, uint32\_t byteLength,OH\_Drawing\_TextEncoding encoding, uint16\_t\* glyphs, int maxGlyphCount)](capi-drawing-font-h.md#oh_drawing_fonttexttoglyphs) | 用于将文本转换为字形索引。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font、text、glyphs任意一个为NULL或者byteLength等于0或者maxGlyphCount小于等于0时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_FontGetWidths(const OH\_Drawing\_Font\* font, const uint16\_t\* glyphs, int count, float\* widths)](capi-drawing-font-h.md#oh_drawing_fontgetwidths) | 用于获取字符串中每个字符的宽度。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font、glyphs、widths任意一个为NULL或者count小于等于0时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontMeasureSingleCharacter(const OH\_Drawing\_Font\* font, const char\* str,float\* textWidth)](capi-drawing-font-h.md#oh_drawing_fontmeasuresinglecharacter) | 用于测量单个字符的宽度。当前字型中的字体不支持待测量字符时，退化到使用系统字体测量字符宽度。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontMeasureText(const OH\_Drawing\_Font\* font, const void\* text, size\_t byteLength,OH\_Drawing\_TextEncoding encoding, OH\_Drawing\_Rect\* bounds, float\* textWidth)](capi-drawing-font-h.md#oh_drawing_fontmeasuretext) | 用于获取文本的宽度和边界框。 |
| [void OH\_Drawing\_FontSetLinearText(OH\_Drawing\_Font\* font, bool isLinearText)](capi-drawing-font-h.md#oh_drawing_fontsetlineartext) | 用于设置线性可缩放字型。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [bool OH\_Drawing\_FontIsLinearText(const OH\_Drawing\_Font\* font)](capi-drawing-font-h.md#oh_drawing_fontislineartext) | 获取字型对象是否使用线性缩放。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_FontSetTextSkewX(OH\_Drawing\_Font\* font, float skewX)](capi-drawing-font-h.md#oh_drawing_fontsettextskewx) | 用于给字型设置文本倾斜。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [float OH\_Drawing\_FontGetTextSkewX(const OH\_Drawing\_Font\* font)](capi-drawing-font-h.md#oh_drawing_fontgettextskewx) | 获取字型文本在x轴上的倾斜度。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_FontSetFakeBoldText(OH\_Drawing\_Font\* font, bool isFakeBoldText)](capi-drawing-font-h.md#oh_drawing_fontsetfakeboldtext) | 用于设置增加描边宽度以近似粗体字体效果。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [bool OH\_Drawing\_FontIsFakeBoldText(const OH\_Drawing\_Font\* font)](capi-drawing-font-h.md#oh_drawing_fontisfakeboldtext) | 获取是否增加笔画宽度以接近粗体字体。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_FontSetScaleX(OH\_Drawing\_Font\* font, float scaleX)](capi-drawing-font-h.md#oh_drawing_fontsetscalex) | 用于设置字型在x轴上的缩放比例。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [float OH\_Drawing\_FontGetScaleX(const OH\_Drawing\_Font\* font)](capi-drawing-font-h.md#oh_drawing_fontgetscalex) | 获取字型在x轴上的缩放比例。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_FontSetHinting(OH\_Drawing\_Font\* font, OH\_Drawing\_FontHinting fontHinting)](capi-drawing-font-h.md#oh_drawing_fontsethinting) | 用于设置字型轮廓效果。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  fontHinting不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [OH\_Drawing\_FontHinting OH\_Drawing\_FontGetHinting(const OH\_Drawing\_Font\* font)](capi-drawing-font-h.md#oh_drawing_fontgethinting) | 获取字型轮廓效果枚举类型。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_FontSetEmbeddedBitmaps(OH\_Drawing\_Font\* font, bool isEmbeddedBitmaps)](capi-drawing-font-h.md#oh_drawing_fontsetembeddedbitmaps) | 用于设置字型是否转换成位图处理。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [bool OH\_Drawing\_FontIsEmbeddedBitmaps(const OH\_Drawing\_Font\* font)](capi-drawing-font-h.md#oh_drawing_fontisembeddedbitmaps) | 获取字型是否转换成位图处理。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_FontSetEdging(OH\_Drawing\_Font\* font, OH\_Drawing\_FontEdging fontEdging)](capi-drawing-font-h.md#oh_drawing_fontsetedging) | 用于设置字型边缘效果。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  fontEdging不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [OH\_Drawing\_FontEdging OH\_Drawing\_FontGetEdging(const OH\_Drawing\_Font\* font)](capi-drawing-font-h.md#oh_drawing_fontgetedging) | 获取字型边缘效果。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_FontDestroy(OH\_Drawing\_Font\* font)](capi-drawing-font-h.md#oh_drawing_fontdestroy) | 用于销毁字型对象并回收该对象占有的内存。 |
| [float OH\_Drawing\_FontGetMetrics(OH\_Drawing\_Font\* font, OH\_Drawing\_Font\_Metrics\* fontMetrics)](capi-drawing-font-h.md#oh_drawing_fontgetmetrics) | 获取字体度量信息。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  font、fontMetrics任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontGetBounds(const OH\_Drawing\_Font\* font, const uint16\_t\* glyphs, uint32\_t count,OH\_Drawing\_Array\* bounds)](capi-drawing-font-h.md#oh_drawing_fontgetbounds) | 获取字型指定字形索引的矩形边界。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontGetPathForGlyph(const OH\_Drawing\_Font\* font, uint16\_t glyph,OH\_Drawing\_Path\* path)](capi-drawing-font-h.md#oh_drawing_fontgetpathforglyph) | 获取字型指定字形索引的轮廓。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontGetTextPath(const OH\_Drawing\_Font\* font, const void\* text, size\_t byteLength,OH\_Drawing\_TextEncoding encoding, float x, float y, OH\_Drawing\_Path\* path)](capi-drawing-font-h.md#oh_drawing_fontgettextpath) | 获取文字轮廓路径。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontSetThemeFontFollowed(OH\_Drawing\_Font\* font, bool followed)](capi-drawing-font-h.md#oh_drawing_fontsetthemefontfollowed) | 设置字型中的字体是否跟随主题字体。设置跟随主题字体后，若系统启用主题字体并且字型未被设置字体，字型会使用该主题字体。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontIsThemeFontFollowed(const OH\_Drawing\_Font\* font, bool\* followed)](capi-drawing-font-h.md#oh_drawing_fontisthemefontfollowed) | 获取字型中的字体是否跟随主题字体。默认不跟随主题字体。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontMeasureSingleCharacterWithFeatures(const OH\_Drawing\_Font\* font, const char\* str,const OH\_Drawing\_FontFeatures\* fontFeatures, float\* textWidth)](capi-drawing-font-h.md#oh_drawing_fontmeasuresinglecharacterwithfeatures) | 用于测量单个字符的宽度，字符带有字体特征。当前字型中的字体不支持待测量字符时，退化到使用系统字体测量字符宽度。 |
| [OH\_Drawing\_FontFeatures\* OH\_Drawing\_FontFeaturesCreate(void)](capi-drawing-font-h.md#oh_drawing_fontfeaturescreate) | 用于创建一个字体特征容器对象。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontFeaturesAddFeature(OH\_Drawing\_FontFeatures\* fontFeatures,const char\* name, float value)](capi-drawing-font-h.md#oh_drawing_fontfeaturesaddfeature) | 向字体特征容器对象中添加一个字体特征。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontFeaturesDestroy(OH\_Drawing\_FontFeatures\* fontFeatures)](capi-drawing-font-h.md#oh_drawing_fontfeaturesdestroy) | 用于销毁字体特征容器对象并回收该对象占有的内存。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_FontHinting

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_FontHinting
```

**描述**

字型轮廓效果类型枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| FONT\_HINTING\_NONE | 不修改字型轮廓。 |
| FONT\_HINTING\_SLIGHT | 最小限度修改字型轮廓以改善对比度。 |
| FONT\_HINTING\_NORMAL | 修改字型轮廓以提高对比度。 |
| FONT\_HINTING\_FULL | 修改字型轮廓以获得最大对比度。 |

### OH\_Drawing\_FontEdging

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_FontEdging
```

**描述**

字型边缘效果类型枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| FONT\_EDGING\_ALIAS | 无抗锯齿处理。 |
| FONT\_EDGING\_ANTI\_ALIAS | 使用抗锯齿来平滑字型边缘。 |
| FONT\_EDGING\_SUBPIXEL\_ANTI\_ALIAS | 使用次像素级别的抗锯齿来平滑字型边缘，可以获得更加平滑的字型渲染效果。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_FontMeasureSingleCharacterWithFeatures()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_FontMeasureSingleCharacterWithFeatures(const OH_Drawing_Font* font, const char* str, const OH_Drawing_FontFeatures* fontFeatures, float* textWidth)
```

**描述**

用于测量单个字符的宽度，字符带有字体特征。当前字型中的字体不支持待测量字符时，退化到使用系统字体测量字符宽度。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| const char\* str | 待测量的单个字符。可以传入字符串，但只会以UTF-8编码解析并测量字符串中的首个字符。 |
| [const OH\_Drawing\_FontFeatures](capi-drawing-oh-drawing-fontfeatures.md)\* fontFeatures | 指向字体特征容器对象[OH\_Drawing\_FontFeatures](capi-drawing-oh-drawing-fontfeatures.md)的指针。容器中未加入任何字体特征时使用TTF(TrueType Font)文件中预设的字体特征。 |
| float\* textWidth | 用于存储得到的字符宽度，作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数font、str、fontFeatures或者textWidth任意一个为空指针或者str的长度为0。 |

### OH\_Drawing\_FontFeaturesCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_FontFeatures* OH_Drawing_FontFeaturesCreate(void)
```

**描述**

用于创建一个字体特征容器对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontFeatures](capi-drawing-oh-drawing-fontfeatures.md)\* | 函数会返回一个指针，指向创建的字体特征容器对象[OH\_Drawing\_FontFeatures](capi-drawing-oh-drawing-fontfeatures.md)。  如果返回的对象指针为空，则表示字体特征容器对象创建失败。失败的原因可能为：没有可用的内存。 |

### OH\_Drawing\_FontFeaturesAddFeature()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_FontFeaturesAddFeature(OH_Drawing_FontFeatures* fontFeatures, const char* name, float value)
```

**描述**

向字体特征容器对象中添加一个字体特征。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontFeatures](capi-drawing-oh-drawing-fontfeatures.md)\* fontFeatures | 指向字体特征容器对象[OH\_Drawing\_FontFeatures](capi-drawing-oh-drawing-fontfeatures.md)的指针。 |
| const char\* name | 字体特征的名称。常见的字体特征名称包含liga、frac、case等，需要对应的ttf文件支持才能生效。 |
| float value | 字体特征的数值。建议通过字体查看工具或查阅字体文档，确定具体的有效取值范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数fontFeatures或name为空指针。 |

### OH\_Drawing\_FontFeaturesDestroy()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_FontFeaturesDestroy(OH_Drawing_FontFeatures* fontFeatures)
```

**描述**

用于销毁字体特征容器对象并回收该对象占有的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontFeatures](capi-drawing-oh-drawing-fontfeatures.md)\* fontFeatures | 指向字体特征容器对象[OH\_Drawing\_FontFeatures](capi-drawing-oh-drawing-fontfeatures.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数fontFeatures为空指针。 |

### OH\_Drawing\_FontMeasureTextWithBrushOrPen()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_FontMeasureTextWithBrushOrPen(const OH_Drawing_Font* font, const void* text,size_t byteLength, OH_Drawing_TextEncoding encoding, const OH_Drawing_Brush* brush, const OH_Drawing_Pen* pen,OH_Drawing_Rect* bounds, float* textWidth)
```

**描述**

使用画刷或画笔获取文本的宽度和边界框。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH\_Drawing\_Font\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| const void\* text | 指向文本的指针。 |
| size\_t byteLength | 表示以字节为单位的文本长度。 |
| [OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding) encoding | 文本编码类型。 |
| const OH\_Drawing\_Brush\* brush | 指向画刷对象[OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)的指针。 |
| const OH\_Drawing\_Pen\* pen | 指向画笔对象[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)的指针。 |
| OH\_Drawing\_Rect\* bounds | 用于承载获取的边界框，可以为NULL。 |
| float\* textWidth | 表示文本宽度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行操作码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数font、text、textWidth至少有一个为空，或者byteLength为0，或者brush和pen同时存在。 |

### OH\_Drawing\_FontGetWidthsBounds()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_FontGetWidthsBounds(const OH_Drawing_Font* font, const uint16_t* glyphs, int count,const OH_Drawing_Brush* brush, const OH_Drawing_Pen* pen, float* widths, OH_Drawing_Array* bounds)
```

**描述**

用于获取字形数组中每个字形的宽度和边界框。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH\_Drawing\_Font\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| const uint16\_t\* glyphs | 字形索引存储首地址。 |
| int count | 字形索引的数量，大小与glyphs数组大小保持一致。 |
| const OH\_Drawing\_Brush\* brush | 指向画刷对象[OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)的指针。 |
| const OH\_Drawing\_Pen\* pen | 指向画笔对象[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)的指针。 |
| float\* widths | 字形宽度存储首地址，用于存储得到的字形宽度，作为返回值返回给调用者。 |
| OH\_Drawing\_Array\* bounds | 字形边界框存储首地址，用于存储得到的字形边界框。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行操作码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数font、glyphs至少有一个为空，或者count不大于0，或者brush和pen同时存在，或者widths和bounds同时为空。 |

### OH\_Drawing\_FontGetPos()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_FontGetPos(const OH_Drawing_Font* font, const uint16_t* glyphs, int count,const OH_Drawing_Point* origin, OH_Drawing_Point2D* points)
```

**描述**

用于从指定的原点开始，获取每个字形的相对位置。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH\_Drawing\_Font\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| const uint16\_t\* glyphs | 字形索引存储首地址。 |
| int count | 字形索引的数量，大小与glyphs数组大小保持一致。 |
| const OH\_Drawing\_Point\* origin | 指向第一个字形的位置，可以为NULL，为NULL默认从(0, 0)开始。 |
| [OH\_Drawing\_Point2D](capi-drawing-oh-drawing-point2d.md)\* points | 字形相对位置存储首地址，用于存储得到的字形相对位置，作为返回值返回给调用者。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行操作码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数font、glyphs、points至少有一个为空，或者count不大于0。 |

### OH\_Drawing\_FontGetSpacing()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_FontGetSpacing(const OH_Drawing_Font* font, float* spacing)
```

**描述**

用于获取推荐的字型行间距。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH\_Drawing\_Font\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| float\* spacing | 推荐的字型行间距，作为返回值返回给调用者。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行操作码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数font、spacing至少有一个为空。 |

### OH\_Drawing\_FontCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Font* OH_Drawing_FontCreate(void)
```

**描述**

用于创建一个字型对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* | 函数会返回一个指针，指针指向创建的字型对象。 |

### OH\_Drawing\_FontSetBaselineSnap()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FontSetBaselineSnap(OH_Drawing_Font* font, bool baselineSnap)
```

**描述**

当前画布矩阵轴对齐时，将字型基线设置为是否与像素对齐。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| bool baselineSnap | 指示字型基线是否和像素对齐。true表示对齐，false表示不对齐。 |

### OH\_Drawing\_FontIsBaselineSnap()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Drawing_FontIsBaselineSnap(const OH_Drawing_Font* font)
```

**描述**

当前画布矩阵轴对齐时，获取字型基线是否与像素对齐。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回字型基线是否与像素对齐。true为对齐，false为没有对齐。 |

### OH\_Drawing\_FontSetSubpixel()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FontSetSubpixel(OH_Drawing_Font* font, bool isSubpixel)
```

**描述**

设置字型是否使用次像素渲染。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| bool isSubpixel | 字型是否使用次像素渲染。true为使用，false为不使用。 |

### OH\_Drawing\_FontIsSubpixel()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Drawing_FontIsSubpixel(const OH_Drawing_Font* font)
```

**描述**

获取字型是否使用次像素渲染。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回字型是否使用次像素渲染。true为使用，false为不使用。 |

### OH\_Drawing\_FontSetForceAutoHinting()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FontSetForceAutoHinting(OH_Drawing_Font* font, bool isForceAutoHinting)
```

**描述**

用于设置是否自动调整字型轮廓。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| bool isForceAutoHinting | 是否自动调整字型轮廓。true为自动调整，false为不自动调整。 |

### OH\_Drawing\_FontIsForceAutoHinting()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Drawing_FontIsForceAutoHinting(const OH_Drawing_Font* font)
```

**描述**

获取字型轮廓是否自动调整。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回字型轮廓是否自动调整。true为自动调整，false为不自动调整。 |

### OH\_Drawing\_FontSetTypeface()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FontSetTypeface(OH_Drawing_Font* font, OH_Drawing_Typeface* typeface)
```

**描述**

用于给字型设置字体。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象的指针。 |
| [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* typeface | 指向字体对象的指针，为NULL会使用系统默认字体对象。 |

### OH\_Drawing\_FontGetTypeface()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Typeface* OH_Drawing_FontGetTypeface(OH_Drawing_Font* font)
```

**描述**

获取字体对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* | OH\_Drawing\_Typeface 函数返回一个指针，指向字体对象[OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)。 |

### OH\_Drawing\_FontSetTextSize()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FontSetTextSize(OH_Drawing_Font* font, float textSize)
```

**描述**

用于给字型对象设置文字大小。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象的指针。 |
| float textSize | 文字大小，该参数为浮点数，为负数时字体大小会被置为0。字体大小为0时，绘制的文字不会显示。 |

### OH\_Drawing\_FontGetTextSize()

PhonePC/2in1TabletTVWearable

```
1. float OH_Drawing_FontGetTextSize(const OH_Drawing_Font* font)
```

**描述**

获取字型对象的文字大小。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回一个浮点数，表示文字大小。 |

### OH\_Drawing\_FontCountText()

PhonePC/2in1TabletTVWearable

```
1. int OH_Drawing_FontCountText(OH_Drawing_Font* font, const void* text, size_t byteLength,OH_Drawing_TextEncoding encoding)
```

**描述**

获取文本所表示的字符数量。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font、text任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| const void\* text | 文本存储首地址。 |
| size\_t byteLength | 文本长度，单位为字节。 |
| [OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding) encoding | 文本编码类型[OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回文本所表示的字符数量，整数。 |

### OH\_Drawing\_FontTextToGlyphs()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_Drawing_FontTextToGlyphs(const OH_Drawing_Font* font, const void* text, uint32_t byteLength,OH_Drawing_TextEncoding encoding, uint16_t* glyphs, int maxGlyphCount)
```

**描述**

用于将文本转换为字形索引。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font、text、glyphs任意一个为NULL或者byteLength等于0或者maxGlyphCount小于等于0时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| const void\* text | 文本存储首地址。 |
| uint32\_t byteLength | 文本长度，单位为字节。 |
| [OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding) encoding | 文本编码类型[OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding)。 |
| uint16\_t\* glyphs | 字形索引存储首地址，用于存储得到的字形索引。 |
| int maxGlyphCount | 文本所表示的最大字符数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 返回字形索引数量。 |

### OH\_Drawing\_FontGetWidths()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FontGetWidths(const OH_Drawing_Font* font, const uint16_t* glyphs, int count, float* widths)
```

**描述**

用于获取字符串中每个字符的宽度。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font、glyphs、widths任意一个为NULL或者count小于等于0时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| const uint16\_t\* glyphs | 字形索引存储首地址。 |
| int count | 字形索引的数量。 |
| float\* widths | 字形宽度存储首地址，用于存储得到的字形宽度。 |

### OH\_Drawing\_FontMeasureSingleCharacter()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_FontMeasureSingleCharacter(const OH_Drawing_Font* font, const char* str,float* textWidth)
```

**描述**

用于测量单个字符的宽度。当前字型中的字体不支持待测量字符时，退化到使用系统字体测量字符宽度。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| const char\* str | 待测量的单个字符。可以传入字符串，但只会以UTF-8编码解析并测量字符串中的首个字符。 |
| float\* textWidth | 用于存储得到的字符宽度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数font、str、textWidth任意一个为NULL或者str的长度为0。 |

### OH\_Drawing\_FontMeasureText()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_FontMeasureText(const OH_Drawing_Font* font, const void* text, size_t byteLength,OH_Drawing_TextEncoding encoding, OH_Drawing_Rect* bounds, float* textWidth)
```

**描述**

用于获取文本的宽度和边界框。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| const void\* text | 指向文本的指针。 |
| size\_t byteLength | 表示以字节为单位的文本长度。 |
| [OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding) encoding | 文本编码类型。 |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* bounds | 用于承载获取的边界框，可以为NULL。 |
| float\* textWidth | 表示文本宽度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数font，text，textWidth至少有一个为空，或者byteLength为0。 |

### OH\_Drawing\_FontSetLinearText()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FontSetLinearText(OH_Drawing_Font* font, bool isLinearText)
```

**描述**

用于设置线性可缩放字型。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象的指针。 |
| bool isLinearText | 真为使能线性可缩放字型，假为不使能。 |

### OH\_Drawing\_FontIsLinearText()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Drawing_FontIsLinearText(const OH_Drawing_Font* font)
```

**描述**

获取字型对象是否使用线性缩放。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回字型对象是否使用线性缩放，true为使用，false为不使用。 |

### OH\_Drawing\_FontSetTextSkewX()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FontSetTextSkewX(OH_Drawing_Font* font, float skewX)
```

**描述**

用于给字型设置文本倾斜。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象的指针。 |
| float skewX | 轴相对于Y轴的倾斜度。 |

### OH\_Drawing\_FontGetTextSkewX()

PhonePC/2in1TabletTVWearable

```
1. float OH_Drawing_FontGetTextSkewX(const OH_Drawing_Font* font)
```

**描述**

获取字型文本在x轴上的倾斜度。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回一个浮点数，表示x轴上的文本倾斜度。 |

### OH\_Drawing\_FontSetFakeBoldText()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FontSetFakeBoldText(OH_Drawing_Font* font, bool isFakeBoldText)
```

**描述**

用于设置增加描边宽度以近似粗体字体效果。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象的指针。 |
| bool isFakeBoldText | 真为使能增加描边宽度，假为不使能。 |

### OH\_Drawing\_FontIsFakeBoldText()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Drawing_FontIsFakeBoldText(const OH_Drawing_Font* font)
```

**描述**

获取是否增加笔画宽度以接近粗体字体。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回是否增加笔画宽度以接近粗体字体。true为增加，false为不增加。 |

### OH\_Drawing\_FontSetScaleX()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FontSetScaleX(OH_Drawing_Font* font, float scaleX)
```

**描述**

用于设置字型在x轴上的缩放比例。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| float scaleX | 文本在x轴上的缩放比例。 |

### OH\_Drawing\_FontGetScaleX()

PhonePC/2in1TabletTVWearable

```
1. float OH_Drawing_FontGetScaleX(const OH_Drawing_Font* font)
```

**描述**

获取字型在x轴上的缩放比例。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回文本在x轴上的缩放比例。 |

### OH\_Drawing\_FontSetHinting()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FontSetHinting(OH_Drawing_Font* font, OH_Drawing_FontHinting fontHinting)
```

**描述**

用于设置字型轮廓效果。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

fontHinting不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| [OH\_Drawing\_FontHinting](capi-drawing-font-h.md#oh_drawing_fonthinting) fontHinting | 字型轮廓枚举类型[OH\_Drawing\_FontHinting](capi-drawing-font-h.md#oh_drawing_fonthinting)。 |

### OH\_Drawing\_FontGetHinting()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_FontHinting OH_Drawing_FontGetHinting(const OH_Drawing_Font* font)
```

**描述**

获取字型轮廓效果枚举类型。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontHinting](capi-drawing-font-h.md#oh_drawing_fonthinting) | OH\_Drawing\_FontHinting 返回字型轮廓效果枚举类型[OH\_Drawing\_FontHinting](capi-drawing-font-h.md#oh_drawing_fonthinting)。 |

### OH\_Drawing\_FontSetEmbeddedBitmaps()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FontSetEmbeddedBitmaps(OH_Drawing_Font* font, bool isEmbeddedBitmaps)
```

**描述**

用于设置字型是否转换成位图处理。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| bool isEmbeddedBitmaps | 设置字型是否转换成位图处理，true表示转换成位图处理，false表示不转换成位图处理。 |

### OH\_Drawing\_FontIsEmbeddedBitmaps()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Drawing_FontIsEmbeddedBitmaps(const OH_Drawing_Font* font)
```

**描述**

获取字型是否转换成位图处理。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回字型是否转换成位图处理，true表示转换成位图处理，false表示不转换成位图处理。 |

### OH\_Drawing\_FontSetEdging()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FontSetEdging(OH_Drawing_Font* font, OH_Drawing_FontEdging fontEdging)
```

**描述**

用于设置字型边缘效果。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

fontEdging不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| [OH\_Drawing\_FontEdging](capi-drawing-font-h.md#oh_drawing_fontedging) fontEdging | 字型边缘效果。 |

### OH\_Drawing\_FontGetEdging()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_FontEdging OH_Drawing_FontGetEdging(const OH_Drawing_Font* font)
```

**描述**

获取字型边缘效果。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontEdging](capi-drawing-font-h.md#oh_drawing_fontedging) | 返回字型边缘效果。 |

### OH\_Drawing\_FontDestroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FontDestroy(OH_Drawing_Font* font)
```

**描述**

用于销毁字型对象并回收该对象占有的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象的指针。 |

### OH\_Drawing\_FontGetMetrics()

PhonePC/2in1TabletTVWearable

```
1. float OH_Drawing_FontGetMetrics(OH_Drawing_Font* font, OH_Drawing_Font_Metrics* fontMetrics)
```

**描述**

获取字体度量信息。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

font、fontMetrics任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| [OH\_Drawing\_Font\_Metrics](capi-drawing-oh-drawing-font-metrics.md)\* fontMetrics | 指向字体度量信息对象[OH\_Drawing\_Font\_Metrics](capi-drawing-oh-drawing-font-metrics.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 函数返回一个浮点数变量，表示建议的行间距。 |

### OH\_Drawing\_FontGetBounds()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_FontGetBounds(const OH_Drawing_Font* font, const uint16_t* glyphs, uint32_t count,OH_Drawing_Array* bounds)
```

**描述**

获取字型指定字形索引的矩形边界。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| const uint16\_t\* glyphs | 字形索引数组。 |
| uint32\_t count | 字形数组的长度。 |
| [OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)\* bounds | 矩形边界数组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数font、glyphs或bounds为空，或者count为零。 |

### OH\_Drawing\_FontGetPathForGlyph()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_FontGetPathForGlyph(const OH_Drawing_Font* font, uint16_t glyph,OH_Drawing_Path* path)
```

**描述**

获取字型指定字形索引的轮廓。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| uint16\_t glyph | 指定的字形索引。 |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针, 用于存储得到的字形路径。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数font或者path为空， 或者指定glyph不存在。 |

### OH\_Drawing\_FontGetTextPath()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_FontGetTextPath(const OH_Drawing_Font* font, const void* text, size_t byteLength,OH_Drawing_TextEncoding encoding, float x, float y, OH_Drawing_Path* path)
```

**描述**

获取文字轮廓路径。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指示字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| const void\* text | 指示要获取轮廓路径的文本字符串。 |
| size\_t byteLength | 指示要获取对应文本路径的字节长度，如果此字节长度大于text字符串的字节长度，会发生未定义行为。 |
| [OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding) encoding | 指示文本编码格式，支持 UTF-8、UTF-16、UTF-32，以及字形索引，具体类型格式可见[OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding)。 |
| float x | 指示文本在绘图区域内以原点为起始位置的X坐标。 |
| float y | 指示文本在绘图区域内以原点为起始位置的Y坐标。 |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 返回获取到的文字轮廓路径对象，作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 返回错误代码。  如果操作成功，则返回 [OH\_DRAWING\_SUCCESS](capi-drawing-error-code-h.md#oh_drawing_errorcode)。  如果 font、text 或 path 中的任何一个为空指针，则返回 [OH\_DRAWING\_ERROR\_INVALID\_PARAMETER](capi-drawing-error-code-h.md#oh_drawing_errorcode)。 |

### OH\_Drawing\_FontSetThemeFontFollowed()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_FontSetThemeFontFollowed(OH_Drawing_Font* font, bool followed)
```

**描述**

设置字型中的字体是否跟随主题字体。设置跟随主题字体后，若系统启用主题字体并且字型未被设置字体，字型会使用该主题字体。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指示字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| bool followed | 字型中的字体是否跟随主题字体，true表示跟随主题字体，false表示不跟随主题字体。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数font为空。 |

### OH\_Drawing\_FontIsThemeFontFollowed()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_FontIsThemeFontFollowed(const OH_Drawing_Font* font, bool* followed)
```

**描述**

获取字型中的字体是否跟随主题字体。默认不跟随主题字体。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指示字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| bool\* followed | 返回字型中的字体是否跟随主题字体的结果，true表示跟随主题字体，false表示不跟随主题字体。作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数font或者followed其中一个为空。 |
