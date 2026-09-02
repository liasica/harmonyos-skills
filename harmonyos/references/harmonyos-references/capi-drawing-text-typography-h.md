---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h
title: drawing_text_typography.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_text_typography.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:342a2c5d27669784c400168c6a3373668115946164761697f927533fc4e3255b
---

## 概述

定义绘制模块中排版相关的函数。

**引用文件：** <native\_drawing/drawing\_text\_typography.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_PlaceholderSpan](capi-drawing-oh-drawing-placeholderspan.md) | OH\_Drawing\_PlaceholderSpan | 用于描述占位符的结构体。 |
| [OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md) | OH\_Drawing\_FontDescriptor | 描述系统字体详细信息的结构体。 |
| [OH\_Drawing\_LineMetrics](capi-drawing-oh-drawing-linemetrics.md) | OH\_Drawing\_LineMetrics | 文字行位置信息。 |
| [OH\_Drawing\_FontFallbackInfo](capi-drawing-oh-drawing-fontfallbackinfo.md) | OH\_Drawing\_FontFallbackInfo | 备用字体信息结构体。 |
| [OH\_Drawing\_FontFallbackGroup](capi-drawing-oh-drawing-fontfallbackgroup.md) | OH\_Drawing\_FontFallbackGroup | 备用字体集信息结构体。 |
| [OH\_Drawing\_FontAdjustInfo](capi-drawing-oh-drawing-fontadjustinfo.md) | OH\_Drawing\_FontAdjustInfo | 字重映射信息结构体。 |
| [OH\_Drawing\_FontAliasInfo](capi-drawing-oh-drawing-fontaliasinfo.md) | OH\_Drawing\_FontAliasInfo | 别名字体信息结构体。 |
| [OH\_Drawing\_FontGenericInfo](capi-drawing-oh-drawing-fontgenericinfo.md) | OH\_Drawing\_FontGenericInfo | 系统所支持的通用字体集信息结构体。 |
| [OH\_Drawing\_FontConfigInfo](capi-drawing-oh-drawing-fontconfiginfo.md) | OH\_Drawing\_FontConfigInfo | 系统字体配置信息结构体。 |
| [OH\_Drawing\_FontStyleStruct](capi-drawing-oh-drawing-fontstylestruct.md) | OH\_Drawing\_FontStyleStruct | 定义字体样式信息的结构体。 |
| [OH\_Drawing\_FontFeature](capi-drawing-oh-drawing-fontfeature.md) | OH\_Drawing\_FontFeature | 描述文本字体特征结构体。 |
| [OH\_Drawing\_StrutStyle](capi-drawing-oh-drawing-strutstyle.md) | OH\_Drawing\_StrutStyle | 用于描述支柱样式的结构体。支柱样式用于控制绘制文本时行之间的间距、基线对齐方式以及其他与行高相关的属性。 |
| [OH\_Drawing\_RectSize](capi-drawing-oh-drawing-rectsize.md) | OH\_Drawing\_RectSize | 定义文本矩形结构体。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_TextDirection](capi-drawing-text-typography-h.md#oh_drawing_textdirection) | - | 文字方向。 |
| [OH\_Drawing\_TextAlign](capi-drawing-text-typography-h.md#oh_drawing_textalign) | - | 文字对齐方式。 |
| [OH\_Drawing\_FontWeight](capi-drawing-text-typography-h.md#oh_drawing_fontweight) | - | 字重。 |
| [OH\_Drawing\_TextBaseline](capi-drawing-text-typography-h.md#oh_drawing_textbaseline) | - | 基线位置。 |
| [OH\_Drawing\_TextDecoration](capi-drawing-text-typography-h.md#oh_drawing_textdecoration) | - | 文本装饰。 |
| [OH\_Drawing\_FontStyle](capi-drawing-text-typography-h.md#oh_drawing_fontstyle) | - | 区分字体是否为斜体。 |
| [OH\_Drawing\_PlaceholderVerticalAlignment](capi-drawing-text-typography-h.md#oh_drawing_placeholderverticalalignment) | OH\_Drawing\_PlaceholderVerticalAlignment | 占位符垂直对齐枚举。 |
| [OH\_Drawing\_TextDecorationStyle](capi-drawing-text-typography-h.md#oh_drawing_textdecorationstyle) | OH\_Drawing\_TextDecorationStyle | 文本装饰样式枚举。 |
| [OH\_Drawing\_EllipsisModal](capi-drawing-text-typography-h.md#oh_drawing_ellipsismodal) | OH\_Drawing\_EllipsisModal | 省略号样式枚举。 |
| [OH\_Drawing\_BreakStrategy](capi-drawing-text-typography-h.md#oh_drawing_breakstrategy) | OH\_Drawing\_BreakStrategy | 文本的中断策略枚举。 |
| [OH\_Drawing\_WordBreakType](capi-drawing-text-typography-h.md#oh_drawing_wordbreaktype) | OH\_Drawing\_WordBreakType | 单词的断词方式枚举。 |
| [OH\_Drawing\_RectHeightStyle](capi-drawing-text-typography-h.md#oh_drawing_rectheightstyle) | OH\_Drawing\_RectHeightStyle | 矩形框高度样式枚举。 |
| [OH\_Drawing\_RectWidthStyle](capi-drawing-text-typography-h.md#oh_drawing_rectwidthstyle) | OH\_Drawing\_RectWidthStyle | 矩形框宽度样式枚举。 |
| [OH\_Drawing\_TextBadgeType](capi-drawing-text-typography-h.md#oh_drawing_textbadgetype) | OH\_Drawing\_TextBadgeType | 上下标样式枚举。 |
| [OH\_Drawing\_FontConfigInfoErrorCode](capi-drawing-text-typography-h.md#oh_drawing_fontconfiginfoerrorcode) | - | 系统字体配置信息列表错误码枚举。 |
| [OH\_Drawing\_FontWidth](capi-drawing-text-typography-h.md#oh_drawing_fontwidth) | - | 字体宽度的枚举。 |
| [OH\_Drawing\_TextHeightBehavior](capi-drawing-text-typography-h.md#oh_drawing_textheightbehavior) | - | 文本高度修饰符模式枚举。 |
| [OH\_Drawing\_TextStyleType](capi-drawing-text-typography-h.md#oh_drawing_textstyletype) | - | 文本样式类型枚举。 |
| [OH\_Drawing\_TextVerticalAlignment](capi-drawing-text-typography-h.md#oh_drawing_textverticalalignment) | OH\_Drawing\_TextVerticalAlignment | 垂直对齐方式枚举。 |
| [OH\_Drawing\_LineHeightStyle](capi-drawing-text-typography-h.md#oh_drawing_lineheightstyle) | OH\_Drawing\_LineHeightStyle | 行高缩放基数样式枚举。默认样式为TEXT\_LINE\_HEIGHT\_BY\_FONT\_SIZE。 |
| [OH\_Drawing\_TextStyleAttributeId](capi-drawing-text-typography-h.md#oh_drawing_textstyleattributeid) | OH\_Drawing\_TextStyleAttributeId | 文本样式属性枚举。 |
| [OH\_Drawing\_TypographyStyleAttributeId](capi-drawing-text-typography-h.md#oh_drawing_typographystyleattributeid) | OH\_Drawing\_TypographyStyleAttributeId | 排版样式属性枚举。  针对排版样式和文本样式中的共有属性，建议优先使用文本样式属性（可由[OH\_Drawing\_TextStyleAttributeId](capi-drawing-text-typography-h.md#oh_drawing_textstyleattributeid)获取）。 |
| [OH\_Drawing\_TypographyAttributeId](capi-drawing-text-typography-h.md#oh_drawing_typographyattributeid) | OH\_Drawing\_TypographyAttributeId | 排版属性枚举。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle\* OH\_Drawing\_CreateTypographyStyle(void)](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle) | 创建指向OH\_Drawing\_TypographyStyle对象的指针。不再需要[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)时，请使用[OH\_Drawing\_DestroyTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_destroytypographystyle)接口释放该对象的指针。 |
| [void OH\_Drawing\_DestroyTypographyStyle(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_destroytypographystyle) | 释放被OH\_Drawing\_TypographyStyle对象占据的内存。 |
| [void OH\_Drawing\_SetTypographyTextDirection(OH\_Drawing\_TypographyStyle\* style, int direction)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextdirection) | 设置指定排版样式中的文本方向。 |
| [void OH\_Drawing\_SetTypographyTextAlign(OH\_Drawing\_TypographyStyle\* style, int align)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextalign) | 设置文本对齐方式。 |
| [int OH\_Drawing\_TypographyGetEffectiveAlignment(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographygeteffectivealignment) | 获取文字对齐方式。 |
| [void OH\_Drawing\_SetTypographyTextMaxLines(OH\_Drawing\_TypographyStyle\* style, int lineNumber)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextmaxlines) | 设置文本最大行数。 |
| [OH\_Drawing\_TextStyle\* OH\_Drawing\_CreateTextStyle(void)](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle) | 创建指向OH\_Drawing\_TextStyle对象的指针。 |
| [OH\_Drawing\_TextStyle\* OH\_Drawing\_TypographyGetTextStyle(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographygettextstyle) | 获取指定排版样式中设置的默认文本样式。 |
| [void OH\_Drawing\_DestroyTextStyle(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_destroytextstyle) | 释放被OH\_Drawing\_TextStyle对象占据的内存。 |
| [void OH\_Drawing\_SetTextStyleColor(OH\_Drawing\_TextStyle\* style, uint32\_t color)](capi-drawing-text-typography-h.md#oh_drawing_settextstylecolor) | 设置文本颜色。 |
| [void OH\_Drawing\_SetTextStyleFontSize(OH\_Drawing\_TextStyle\* style, double fontSize)](capi-drawing-text-typography-h.md#oh_drawing_settextstylefontsize) | 设置字号。 |
| [void OH\_Drawing\_SetTextStyleFontWeight(OH\_Drawing\_TextStyle\* style, int fontWeight)](capi-drawing-text-typography-h.md#oh_drawing_settextstylefontweight) | 设置字重。在HarmonyOS 6.1.1之前，仅系统字体中的可变字体支持字重调节；从HarmonyOS 6.1.1开始，系统字体与三方注册字体中的可变字体均支持字重调节。非可变字体设置字重值小于semi-bold时字体粗细无变化，设置字重值大于等于semi-bold时可能会触发伪加粗效果。 |
| [void OH\_Drawing\_SetTextStyleBaseLine(OH\_Drawing\_TextStyle\* style, int baseline)](capi-drawing-text-typography-h.md#oh_drawing_settextstylebaseline) | 设置文本样式的字体基线位置。 |
| [void OH\_Drawing\_SetTextStyleDecoration(OH\_Drawing\_TextStyle\* style, int decoration)](capi-drawing-text-typography-h.md#oh_drawing_settextstyledecoration) | 设置指定文本样式中的装饰线类型，只能设置一个装饰线类型，添加多个需要使用[OH\_Drawing\_AddTextStyleDecoration](capi-drawing-text-typography-h.md#oh_drawing_addtextstyledecoration)。 |
| [void OH\_Drawing\_AddTextStyleDecoration(OH\_Drawing\_TextStyle\* style, int decoration)](capi-drawing-text-typography-h.md#oh_drawing_addtextstyledecoration) | 新增指定装饰线，可同时显示多种装饰线。 |
| [void OH\_Drawing\_RemoveTextStyleDecoration(OH\_Drawing\_TextStyle\* style, int decoration)](capi-drawing-text-typography-h.md#oh_drawing_removetextstyledecoration) | 删除指定装饰线。 |
| [void OH\_Drawing\_SetTextStyleDecorationColor(OH\_Drawing\_TextStyle\* style, uint32\_t color)](capi-drawing-text-typography-h.md#oh_drawing_settextstyledecorationcolor) | 设置指定文本样式中的装饰线颜色。如果不调用该接口或者设置color为0时，装饰线颜色跟随文本颜色。 |
| [void OH\_Drawing\_SetTextStyleFontHeight(OH\_Drawing\_TextStyle\* style, double fontHeight)](capi-drawing-text-typography-h.md#oh_drawing_settextstylefontheight) | 设置行高，按当前字体大小的倍数进行设置。 |
| [void OH\_Drawing\_SetTextStyleFontFamilies(OH\_Drawing\_TextStyle\* style, int fontFamiliesNumber, const char\* fontFamilies[])](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_settextstylefontfamilies) | 设置指定文本样式的字体家族类型。 |
| [void OH\_Drawing\_SetTextStyleFontStyle(OH\_Drawing\_TextStyle\* style, int fontStyle)](capi-drawing-text-typography-h.md#oh_drawing_settextstylefontstyle) | 为指定文本样式设置字体样式。 |
| [void OH\_Drawing\_SetTextStyleLocale(OH\_Drawing\_TextStyle\* style, const char\* locale)](capi-drawing-text-typography-h.md#oh_drawing_settextstylelocale) | 设置文本语言环境。 |
| [void OH\_Drawing\_SetTextStyleForegroundBrush(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Brush\* foregroundBrush)](capi-drawing-text-typography-h.md#oh_drawing_settextstyleforegroundbrush) | 设置指定文本样式中的前景色画刷。 |
| [void OH\_Drawing\_TextStyleGetForegroundBrush(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Brush\* foregroundBrush)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetforegroundbrush) | 获取已设置的前景色画刷。 |
| [void OH\_Drawing\_SetTextStyleForegroundPen(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Pen\* foregroundPen)](capi-drawing-text-typography-h.md#oh_drawing_settextstyleforegroundpen) | 设置指定文本样式中的前景色画笔。 |
| [void OH\_Drawing\_TextStyleGetForegroundPen(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Pen\* foregroundPen)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetforegroundpen) | 获取已设置的前景色画笔。 |
| [void OH\_Drawing\_SetTextStyleBackgroundBrush(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Brush\* backgroundBrush)](capi-drawing-text-typography-h.md#oh_drawing_settextstylebackgroundbrush) | 设置指定文本样式中的背景色画刷。 |
| [void OH\_Drawing\_TextStyleGetBackgroundBrush(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Brush\* backgroundBrush)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetbackgroundbrush) | 获取已设置的背景色画刷。 |
| [void OH\_Drawing\_SetTextStyleBackgroundPen(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Pen\* backgroundPen)](capi-drawing-text-typography-h.md#oh_drawing_settextstylebackgroundpen) | 设置指定文本样式中的背景色画笔。 |
| [void OH\_Drawing\_TextStyleGetBackgroundPen(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Pen\* backgroundPen)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetbackgroundpen) | 获取已设置的背景色画笔。 |
| [OH\_Drawing\_TypographyCreate\* OH\_Drawing\_CreateTypographyHandler(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_FontCollection\* fontCollection)](capi-drawing-text-typography-h.md#oh_drawing_createtypographyhandler) | 创建指向OH\_Drawing\_TypographyCreate对象的指针。不再需要[OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)时，请使用[OH\_Drawing\_DestroyTypographyHandler](capi-drawing-text-typography-h.md#oh_drawing_destroytypographyhandler)接口释放该对象的指针。建议优先使用[OH\_Drawing\_CreateSharedFontCollection](capi-drawing-font-collection-h.md#oh_drawing_createsharedfontcollection)函数创建[OH\_Drawing\_FontCollection](capi-drawing-oh-drawing-fontcollection.md)对象。 |
| [void OH\_Drawing\_DestroyTypographyHandler(OH\_Drawing\_TypographyCreate\* handler)](capi-drawing-text-typography-h.md#oh_drawing_destroytypographyhandler) | 释放被OH\_Drawing\_TypographyCreate对象占据的内存。 |
| [void OH\_Drawing\_TypographyHandlerPushTextStyle(OH\_Drawing\_TypographyCreate\* handler, OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographyhandlerpushtextstyle) | 将指定文本样式压入文本样式栈，后续添加的文本总是会使用栈顶的文本样式。 |
| [void OH\_Drawing\_TypographyHandlerAddText(OH\_Drawing\_TypographyCreate\* handler, const char\* text)](capi-drawing-text-typography-h.md#oh_drawing_typographyhandleraddtext) | 设置文本内容。 |
| [void OH\_Drawing\_TypographyHandlerPopTextStyle(OH\_Drawing\_TypographyCreate\* handler)](capi-drawing-text-typography-h.md#oh_drawing_typographyhandlerpoptextstyle) | 从文本样式栈中弹出栈顶文本样式。 |
| [OH\_Drawing\_Typography\* OH\_Drawing\_CreateTypography(OH\_Drawing\_TypographyCreate\* handler)](capi-drawing-text-typography-h.md#oh_drawing_createtypography) | 创建指向OH\_Drawing\_Typography对象的指针。不再需要[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)时，请使用[OH\_Drawing\_DestroyTypography](capi-drawing-text-typography-h.md#oh_drawing_destroytypography)接口释放该对象的指针。 |
| [void OH\_Drawing\_DestroyTypography(OH\_Drawing\_Typography\* typography)](capi-drawing-text-typography-h.md#oh_drawing_destroytypography) | 释放OH\_Drawing\_Typography对象占据的内存。 |
| [void OH\_Drawing\_TypographyLayout(OH\_Drawing\_Typography\* typography, double maxWidth)](capi-drawing-text-typography-h.md#oh_drawing_typographylayout) | 对文本内容进行排版布局计算。 |
| [void OH\_Drawing\_TypographyPaint(OH\_Drawing\_Typography\* typography, OH\_Drawing\_Canvas\* canvas, double positionX, double positionY)](capi-drawing-text-typography-h.md#oh_drawing_typographypaint) | 在指定位置绘制文本，从左上角开始绘制，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用并生效之后调用。 |
| [void OH\_Drawing\_TypographyPaintOnPath(OH\_Drawing\_Typography\* typography, OH\_Drawing\_Canvas\* canvas,OH\_Drawing\_Path\* path, double hOffset, double vOffset)](capi-drawing-text-typography-h.md#oh_drawing_typographypaintonpath) | 沿指定路径绘制文本。建议搭配[OH\_Drawing\_SetTypographyTextMaxLines](capi-drawing-text-typography-h.md#oh_drawing_settypographytextmaxlines)接口设置最大行为1行，避免因文本宽度超过排版宽度出现跨行重叠问题。 |
| [double OH\_Drawing\_TypographyGetMaxWidth(OH\_Drawing\_Typography\* typography)](capi-drawing-text-typography-h.md#oh_drawing_typographygetmaxwidth) | 获取用户设置的排版宽度，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。 |
| [double OH\_Drawing\_TypographyGetHeight(OH\_Drawing\_Typography\* typography)](capi-drawing-text-typography-h.md#oh_drawing_typographygetheight) | 获取排版对象整体的高度，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。 |
| [double OH\_Drawing\_TypographyGetLongestLine(OH\_Drawing\_Typography\* typography)](capi-drawing-text-typography-h.md#oh_drawing_typographygetlongestline) | 获取排版对象最长行的宽度，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用，建议实际使用时将返回值向上取整。当文本内容为空时，返回0.0。 |
| [double OH\_Drawing\_TypographyGetLongestLineWithIndent(OH\_Drawing\_Typography\* typography)](capi-drawing-text-typography-h.md#oh_drawing_typographygetlongestlinewithindent) | 获取排版对象最长行的宽度（该宽度包含当前行缩进的宽度），该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用，建议实际使用时将返回值向上取整。当文本内容为空时，返回0.0。 |
| [double OH\_Drawing\_TypographyGetMinIntrinsicWidth(OH\_Drawing\_Typography\* typography)](capi-drawing-text-typography-h.md#oh_drawing_typographygetminintrinsicwidth) | 获取排版对象的最小固有宽度，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。 |
| [double OH\_Drawing\_TypographyGetMaxIntrinsicWidth(OH\_Drawing\_Typography\* typography)](capi-drawing-text-typography-h.md#oh_drawing_typographygetmaxintrinsicwidth) | 获取排版对象的最大固有宽度，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。 |
| [double OH\_Drawing\_TypographyGetAlphabeticBaseline(OH\_Drawing\_Typography\* typography)](capi-drawing-text-typography-h.md#oh_drawing_typographygetalphabeticbaseline) | 获取排版对象字母文字基线，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。 |
| [double OH\_Drawing\_TypographyGetIdeographicBaseline(OH\_Drawing\_Typography\* typography)](capi-drawing-text-typography-h.md#oh_drawing_typographygetideographicbaseline) | 获取排版对象表意文字基线，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。 |
| [void OH\_Drawing\_TypographyHandlerAddPlaceholder(OH\_Drawing\_TypographyCreate\* handler,OH\_Drawing\_PlaceholderSpan\* span)](capi-drawing-text-typography-h.md#oh_drawing_typographyhandleraddplaceholder) | 设置占位符。 |
| [bool OH\_Drawing\_TypographyDidExceedMaxLines(OH\_Drawing\_Typography\* typography)](capi-drawing-text-typography-h.md#oh_drawing_typographydidexceedmaxlines) | 获取排版对象中文本是否超过最大行，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用，如果没有通过[OH\_Drawing\_SetTypographyTextMaxLines](capi-drawing-text-typography-h.md#oh_drawing_settypographytextmaxlines)接口设置最大行，则返回false。 |
| [OH\_Drawing\_TextBox\* OH\_Drawing\_TypographyGetRectsForRange(OH\_Drawing\_Typography\* typography,size\_t start, size\_t end, OH\_Drawing\_RectHeightStyle heightStyle, OH\_Drawing\_RectWidthStyle widthStyle)](capi-drawing-text-typography-h.md#oh_drawing_typographygetrectsforrange) | 获取排版对象中指定范围内的文本框，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。不再需要[OH\_Drawing\_TextBox](capi-drawing-oh-drawing-textbox.md)时，请使用[OH\_Drawing\_TypographyDestroyTextBox](capi-drawing-text-typography-h.md#oh_drawing_typographydestroytextbox)接口释放该对象的指针。 |
| [OH\_Drawing\_TextBox\* OH\_Drawing\_TypographyGetRectsForPlaceholders(OH\_Drawing\_Typography\* typography)](capi-drawing-text-typography-h.md#oh_drawing_typographygetrectsforplaceholders) | 获取排版对象中占位符的文本框，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。不再需要[OH\_Drawing\_TextBox](capi-drawing-oh-drawing-textbox.md)时，请使用[OH\_Drawing\_TypographyDestroyTextBox](capi-drawing-text-typography-h.md#oh_drawing_typographydestroytextbox)接口释放该对象的指针。 |
| [float OH\_Drawing\_GetLeftFromTextBox(OH\_Drawing\_TextBox\* textbox, int index)](capi-drawing-text-typography-h.md#oh_drawing_getleftfromtextbox) | 获取文本框左侧位置。 |
| [float OH\_Drawing\_GetRightFromTextBox(OH\_Drawing\_TextBox\* textbox, int index)](capi-drawing-text-typography-h.md#oh_drawing_getrightfromtextbox) | 获取文本框右侧位置。 |
| [float OH\_Drawing\_GetTopFromTextBox(OH\_Drawing\_TextBox\* textbox, int index)](capi-drawing-text-typography-h.md#oh_drawing_gettopfromtextbox) | 获取文本框顶部位置。 |
| [float OH\_Drawing\_GetBottomFromTextBox(OH\_Drawing\_TextBox\* textbox, int index)](capi-drawing-text-typography-h.md#oh_drawing_getbottomfromtextbox) | 获取文本框底部位置。 |
| [int OH\_Drawing\_GetTextDirectionFromTextBox(OH\_Drawing\_TextBox\* textbox, int index)](capi-drawing-text-typography-h.md#oh_drawing_gettextdirectionfromtextbox) | 获取文本框方向。 |
| [size\_t OH\_Drawing\_GetSizeOfTextBox(OH\_Drawing\_TextBox\* textBox)](capi-drawing-text-typography-h.md#oh_drawing_getsizeoftextbox) | 获取文本框数量大小。 |
| [OH\_Drawing\_PositionAndAffinity\* OH\_Drawing\_TypographyGetGlyphPositionAtCoordinate(OH\_Drawing\_Typography\* typography,double dx, double dy)](capi-drawing-text-typography-h.md#oh_drawing_typographygetglyphpositionatcoordinate) | 获取坐标处文本的索引位置和亲和性。 |
| [OH\_Drawing\_PositionAndAffinity\* OH\_Drawing\_TypographyGetGlyphPositionAtCoordinateWithCluster(OH\_Drawing\_Typography\* typography, double dx, double dy)](capi-drawing-text-typography-h.md#oh_drawing_typographygetglyphpositionatcoordinatewithcluster) | 获取坐标处文本所属字符簇的索引位置和亲和性，字符簇指一个或多个字符组成的整体。 |
| [size\_t OH\_Drawing\_GetPositionFromPositionAndAffinity(OH\_Drawing\_PositionAndAffinity\* positionAndAffinity)](capi-drawing-text-typography-h.md#oh_drawing_getpositionfrompositionandaffinity) | 获取OH\_Drawing\_PositionAndAffinity对象的位置属性。 |
| [int OH\_Drawing\_GetAffinityFromPositionAndAffinity(OH\_Drawing\_PositionAndAffinity\* positionAndAffinity)](capi-drawing-text-typography-h.md#oh_drawing_getaffinityfrompositionandaffinity) | 获取OH\_Drawing\_PositionAndAffinity对象的亲和性，根据亲和性可判断字体会靠近前方文本还是后方文本。 |
| [OH\_Drawing\_Range\* OH\_Drawing\_TypographyGetWordBoundary(OH\_Drawing\_Typography\* typography, size\_t offset)](capi-drawing-text-typography-h.md#oh_drawing_typographygetwordboundary) | 获取排版对象中单词的边界。 |
| [size\_t OH\_Drawing\_GetStartFromRange(OH\_Drawing\_Range\* range)](capi-drawing-text-typography-h.md#oh_drawing_getstartfromrange) | 获取OH\_Drawing\_Range对象开始位置。 |
| [size\_t OH\_Drawing\_GetEndFromRange(OH\_Drawing\_Range\* range)](capi-drawing-text-typography-h.md#oh_drawing_getendfromrange) | 获取OH\_Drawing\_Range对象结束位置。 |
| [size\_t OH\_Drawing\_TypographyGetLineCount(OH\_Drawing\_Typography\* typography)](capi-drawing-text-typography-h.md#oh_drawing_typographygetlinecount) | 获取排版对象中文本行数，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。 |
| [void OH\_Drawing\_SetTextStyleDecorationStyle(OH\_Drawing\_TextStyle\* style, int decorationStyle)](capi-drawing-text-typography-h.md#oh_drawing_settextstyledecorationstyle) | 设置指定文本样式中的装饰线样式。 |
| [void OH\_Drawing\_SetTextStyleDecorationThicknessScale(OH\_Drawing\_TextStyle\* style, double decorationThicknessScale)](capi-drawing-text-typography-h.md#oh_drawing_settextstyledecorationthicknessscale) | 设置文本装饰线的粗细缩放比例。 |
| [void OH\_Drawing\_SetTextStyleLetterSpacing(OH\_Drawing\_TextStyle\* style, double letterSpacing)](capi-drawing-text-typography-h.md#oh_drawing_settextstyleletterspacing) | 设置文本的字符间距。 |
| [void OH\_Drawing\_SetTextStyleWordSpacing(OH\_Drawing\_TextStyle\* style, double wordSpacing)](capi-drawing-text-typography-h.md#oh_drawing_settextstylewordspacing) | 设置文本的单词间距。 |
| [void OH\_Drawing\_SetTextStyleHalfLeading(OH\_Drawing\_TextStyle\* style, bool halfLeading)](capi-drawing-text-typography-h.md#oh_drawing_settextstylehalfleading) | 设置文本为一半行间距。 |
| [void OH\_Drawing\_SetTextStyleEllipsis(OH\_Drawing\_TextStyle\* style, const char\* ellipsis)](capi-drawing-text-typography-h.md#oh_drawing_settextstyleellipsis) | 设置文本的省略号内容。 |
| [void OH\_Drawing\_SetTextStyleEllipsisModal(OH\_Drawing\_TextStyle\* style, int ellipsisModal)](capi-drawing-text-typography-h.md#oh_drawing_settextstyleellipsismodal) | 设置文本的省略号样式。 |
| [void OH\_Drawing\_SetTypographyTextBreakStrategy(OH\_Drawing\_TypographyStyle\* style, int breakStrategy)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextbreakstrategy) | 设置文本的中断策略。 |
| [void OH\_Drawing\_SetTypographyTextWordBreakType(OH\_Drawing\_TypographyStyle\* style, int wordBreakType)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextwordbreaktype) | 设置单词的断词方式。 |
| [void OH\_Drawing\_SetTypographyTextEllipsisModal(OH\_Drawing\_TypographyStyle\* style, int ellipsisModal)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextellipsismodal) | 设置文本的省略模式。 |
| [void OH\_Drawing\_SetTypographyTextEllipsis(OH\_Drawing\_TypographyStyle\* style, const char\* ellipsis)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextellipsis) | 设置排版样式省略号文本。 |
| [double OH\_Drawing\_TypographyGetLineHeight(OH\_Drawing\_Typography\* typography, int lineNumber)](capi-drawing-text-typography-h.md#oh_drawing_typographygetlineheight) | 获取排版对象中指定行的行高，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。 |
| [double OH\_Drawing\_TypographyGetLineWidth(OH\_Drawing\_Typography\* typography, int lineNumber)](capi-drawing-text-typography-h.md#oh_drawing_typographygetlinewidth) | 获取指定行的行宽，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。 |
| [void OH\_Drawing\_SetTypographyTextSplitRatio(OH\_Drawing\_TypographyStyle\* style, float textSplitRatio)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextsplitratio) | 设置文本划分比率。 |
| [bool OH\_Drawing\_TypographyIsLineUnlimited(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographyislineunlimited) | 获取文本是否有最大行数限制。 |
| [bool OH\_Drawing\_TypographyIsEllipsized(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographyisellipsized) | 获取指定排版样式是否配置省略号。 |
| [void OH\_Drawing\_SetTypographyTextLocale(OH\_Drawing\_TypographyStyle\* style, const char\* locale)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextlocale) | 设置指定排版样式的语言环境。 |
| [bool OH\_Drawing\_TextStyleGetFontMetrics(OH\_Drawing\_Typography\* typography,OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Font\_Metrics\* fontmetrics)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetfontmetrics) | 从排版对象中获取字体属性。 |
| [void OH\_Drawing\_SetTypographyTextStyle(OH\_Drawing\_TypographyStyle\* handler, OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextstyle) | 设置排版样式。 |
| [OH\_Drawing\_FontDescriptor\* OH\_Drawing\_CreateFontDescriptor(void)](capi-drawing-text-typography-h.md#oh_drawing_createfontdescriptor) | 构造字体描述对象，用于描述系统字体详细信息。 |
| [void OH\_Drawing\_DestroyFontDescriptor(OH\_Drawing\_FontDescriptor\* descriptor)](capi-drawing-text-typography-h.md#oh_drawing_destroyfontdescriptor) | 释放字体描述对象占用的内存。 |
| [OH\_Drawing\_FontParser\* OH\_Drawing\_CreateFontParser(void)](capi-drawing-text-typography-h.md#oh_drawing_createfontparser) | 构造字体解析对象，用于解析系统字体。 |
| [void OH\_Drawing\_DestroyFontParser(OH\_Drawing\_FontParser\* parser)](capi-drawing-text-typography-h.md#oh_drawing_destroyfontparser) | 释放字体解析对象占用的内存。 |
| [char\*\* OH\_Drawing\_FontParserGetSystemFontList(OH\_Drawing\_FontParser\* fontParser, size\_t\* num)](capi-drawing-text-typography-h.md#oh_drawing_fontparsergetsystemfontlist) | 获取系统字体名称列表，此接口仅在Phone、PC/2in1设备上支持。 |
| [void OH\_Drawing\_DestroySystemFontList(char\*\* fontList, size\_t num)](capi-drawing-text-typography-h.md#oh_drawing_destroysystemfontlist) | 释放系统字体名称列表占用的内存。 |
| [OH\_Drawing\_FontDescriptor\* OH\_Drawing\_FontParserGetFontByName(OH\_Drawing\_FontParser\* fontParser, const char\* name)](capi-drawing-text-typography-h.md#oh_drawing_fontparsergetfontbyname) | 根据传入的系统字体名称获取系统字体的相关信息。仅在Phone、PC/2in1设备上支持，其他设备上调用返回nullptr。 |
| [OH\_Drawing\_LineMetrics\* OH\_Drawing\_TypographyGetLineMetrics(OH\_Drawing\_Typography\* typography)](capi-drawing-text-typography-h.md#oh_drawing_typographygetlinemetrics) | 获取排版对象的行位置信息，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。不再需要[OH\_Drawing\_LineMetrics](capi-drawing-oh-drawing-linemetrics.md)时，请使用[OH\_Drawing\_DestroyLineMetrics](capi-drawing-text-typography-h.md#oh_drawing_destroylinemetrics)接口释放该对象的指针。 |
| [size\_t OH\_Drawing\_LineMetricsGetSize(OH\_Drawing\_LineMetrics\* lineMetrics)](capi-drawing-text-typography-h.md#oh_drawing_linemetricsgetsize) | 获取行数量。 |
| [void OH\_Drawing\_DestroyLineMetrics(OH\_Drawing\_LineMetrics\* lineMetrics)](capi-drawing-text-typography-h.md#oh_drawing_destroylinemetrics) | 释放行位置信息对象占用的内存。 |
| [bool OH\_Drawing\_TypographyGetLineMetricsAt(OH\_Drawing\_Typography\* typography, int lineNumber, OH\_Drawing\_LineMetrics\* lineMetric)](capi-drawing-text-typography-h.md#oh_drawing_typographygetlinemetricsat) | 获取排版对象的指定行位置信息，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。 |
| [bool OH\_Drawing\_TypographyGetLineInfo(OH\_Drawing\_Typography\* typography, int lineNumber, bool oneLine,bool includeWhitespace, OH\_Drawing\_LineMetrics\* drawingLineMetrics)](capi-drawing-text-typography-h.md#oh_drawing_typographygetlineinfo) | 获取排版对象中指定行的位置信息或指定行第一个字符的位置信息，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。 |
| [void OH\_Drawing\_SetTypographyTextFontWeight(OH\_Drawing\_TypographyStyle\* style, int weight)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextfontweight) | 设置排版样式默认字重。在HarmonyOS 6.1.1之前，仅系统字体中的可变字体支持字重调节；从HarmonyOS 6.1.1开始，系统字体与三方注册字体中的可变字体均支持字重调节。非可变字体设置字重值小于semi-bold时字体粗细无变化，设置字重值大于等于semi-bold时可能会触发伪加粗效果。 |
| [void OH\_Drawing\_SetTypographyTextFontStyle(OH\_Drawing\_TypographyStyle\* style, int fontStyle)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextfontstyle) | 设置排版样式默认的字体样式。 |
| [void OH\_Drawing\_SetTypographyTextFontFamily(OH\_Drawing\_TypographyStyle\* style, const char\* fontFamily)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextfontfamily) | 设置字体家族的名称。 |
| [void OH\_Drawing\_SetTypographyTextFontSize(OH\_Drawing\_TypographyStyle\* style, double fontSize)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextfontsize) | 设置文本排版字号。 |
| [void OH\_Drawing\_SetTypographyTextFontHeight(OH\_Drawing\_TypographyStyle\* style, double fontHeight)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextfontheight) | 设置文本排版字体高度。 |
| [void OH\_Drawing\_SetTypographyTextHalfLeading(OH\_Drawing\_TypographyStyle\* style, bool halfLeading)](capi-drawing-text-typography-h.md#oh_drawing_settypographytexthalfleading) | 设置文本排版是否为一半行间距。 |
| [void OH\_Drawing\_SetTypographyTextUseLineStyle(OH\_Drawing\_TypographyStyle\* style, bool useLineStyle)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextuselinestyle) | 设置文本排版是否启用行样式。 |
| [void OH\_Drawing\_SetTypographyTextLineStyleFontWeight(OH\_Drawing\_TypographyStyle\* style, int weight)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextlinestylefontweight) | 设置排版样式中支柱样式的文本样式字重。在HarmonyOS 6.1.1之前，仅系统字体中的可变字体支持字重调节；从HarmonyOS 6.1.1开始，系统字体与三方注册字体中的可变字体均支持字重调节。非可变字体设置字重值小于semi-bold时字体粗细无变化，设置字重值大于等于semi-bold时可能会触发伪加粗效果。 |
| [void OH\_Drawing\_SetTypographyTextLineStyleFontStyle(OH\_Drawing\_TypographyStyle\* style, int fontStyle)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextlinestylefontstyle) | 设置文本排版样式中支柱样式的字体样式。 |
| [void OH\_Drawing\_SetTypographyTextLineStyleFontFamilies(OH\_Drawing\_TypographyStyle\* style, int fontFamiliesNumber, const char\* fontFamilies[])](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_settypographytextlinestylefontfamilies) | 设置文本排版行样式字体家族。 |
| [void OH\_Drawing\_SetTypographyTextLineStyleFontSize(OH\_Drawing\_TypographyStyle\* style, double lineStyleFontSize)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextlinestylefontsize) | 设置文本排版行样式字号。 |
| [void OH\_Drawing\_SetTypographyTextLineStyleFontHeight(OH\_Drawing\_TypographyStyle\* style, double lineStyleFontHeight)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextlinestylefontheight) | 设置文本排版行样式字体高度。 |
| [void OH\_Drawing\_SetTypographyTextLineStyleHalfLeading(OH\_Drawing\_TypographyStyle\* style, bool lineStyleHalfLeading)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextlinestylehalfleading) | 设置文本排版行样式是否为一半行间距。 |
| [void OH\_Drawing\_SetTypographyTextLineStyleSpacingScale(OH\_Drawing\_TypographyStyle\* style, double spacingScale)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextlinestylespacingscale) | 设置文本排版行样式间距比例。 |
| [void OH\_Drawing\_SetTypographyTextLineStyleOnly(OH\_Drawing\_TypographyStyle\* style, bool lineStyleOnly)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextlinestyleonly) | 设置文本排版是否仅启用行样式。 |
| [OH\_Drawing\_TextShadow\* OH\_Drawing\_CreateTextShadow(void)](capi-drawing-text-typography-h.md#oh_drawing_createtextshadow) | 创建指向文本阴影对象的指针。不再需要[OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)时，请使用[OH\_Drawing\_DestroyTextShadow](capi-drawing-text-typography-h.md#oh_drawing_destroytextshadow)接口释放该对象的指针。 |
| [void OH\_Drawing\_DestroyTextShadow(OH\_Drawing\_TextShadow\* shadow)](capi-drawing-text-typography-h.md#oh_drawing_destroytextshadow) | 释放被文本阴影对象占据的内存。 |
| [OH\_Drawing\_TextShadow\* OH\_Drawing\_TextStyleGetShadows(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetshadows) | 获取文本阴影容器。不再需要[OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)时，请使用[OH\_Drawing\_DestroyTextShadows](capi-drawing-text-typography-h.md#oh_drawing_destroytextshadows)接口释放该对象的指针。 |
| [int OH\_Drawing\_TextStyleGetShadowCount(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetshadowcount) | 获取文本阴影容器的大小。 |
| [void OH\_Drawing\_TextStyleAddShadow(OH\_Drawing\_TextStyle\* style, const OH\_Drawing\_TextShadow\* shadow)](capi-drawing-text-typography-h.md#oh_drawing_textstyleaddshadow) | 文本阴影容器中添加文本阴影元素。 |
| [void OH\_Drawing\_TextStyleClearShadows(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_textstyleclearshadows) | 清除文本阴影容器中的所有元素。 |
| [OH\_Drawing\_TextShadow\* OH\_Drawing\_TextStyleGetShadowWithIndex(OH\_Drawing\_TextStyle\* style, int index)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetshadowwithindex) | 根据下标获取文本阴影容器中的元素。 |
| [void OH\_Drawing\_TypographySetIndents(OH\_Drawing\_Typography\* typography, int indentsNumber, const float indents[])](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_typographysetindents) | 设置文本的排版缩进，不调用此接口默认文本无缩进。 |
| [float OH\_Drawing\_TypographyGetIndentsWithIndex(OH\_Drawing\_Typography\* typography, int index)](capi-drawing-text-typography-h.md#oh_drawing_typographygetindentswithindex) | 根据行索引获取排版对象缩进容器中的元素，行索引从0开始。 |
| [OH\_Drawing\_Range\* OH\_Drawing\_TypographyGetLineTextRange(OH\_Drawing\_Typography\* typography, int lineNumber, bool includeSpaces)](capi-drawing-text-typography-h.md#oh_drawing_typographygetlinetextrange) | 获取排版对象中行的边界，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。该接口只能获取已有行的边界，即输入行索引从0开始，最大行索引为[OH\_Drawing\_TypographyGetLineCount](capi-drawing-text-typography-h.md#oh_drawing_typographygetlinecount) - 1。 |
| [void OH\_Drawing\_DestroyTextShadows(OH\_Drawing\_TextShadow\* shadow)](capi-drawing-text-typography-h.md#oh_drawing_destroytextshadows) | 释放由被文本阴影对象OH\_Drawing\_TextShadow构成的vector占据的内存。 |
| [OH\_Drawing\_FontConfigInfo\* OH\_Drawing\_GetSystemFontConfigInfo(OH\_Drawing\_FontConfigInfoErrorCode\* errorCode)](capi-drawing-text-typography-h.md#oh_drawing_getsystemfontconfiginfo) | 获取系统字体配置信息。 |
| [void OH\_Drawing\_DestroySystemFontConfigInfo(OH\_Drawing\_FontConfigInfo\* drawFontCfgInfo)](capi-drawing-text-typography-h.md#oh_drawing_destroysystemfontconfiginfo) | 释放系统字体配置信息占用的内存。 |
| [void OH\_Drawing\_SetTextStyleFontStyleStruct(OH\_Drawing\_TextStyle\* drawingTextStyle,OH\_Drawing\_FontStyleStruct fontStyle)](capi-drawing-text-typography-h.md#oh_drawing_settextstylefontstylestruct) | 设置文本样式中的字体样式，包括字体字重、字体宽度和字体斜度。 |
| [void OH\_Drawing\_SetTextStyleBadgeType(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextBadgeType textBadgeType)](capi-drawing-text-typography-h.md#oh_drawing_settextstylebadgetype) | 设置文本排版时是否启用上标或下标。未调用此接口时，默认不启用。 |
| [OH\_Drawing\_FontStyleStruct OH\_Drawing\_TextStyleGetFontStyleStruct(OH\_Drawing\_TextStyle\* drawingTextStyle)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetfontstylestruct) | 获取文本样式中的字体样式，包括字体字重、字体宽度和字体斜度。 |
| [void OH\_Drawing\_SetTypographyStyleFontStyleStruct(OH\_Drawing\_TypographyStyle\* drawingStyle,OH\_Drawing\_FontStyleStruct fontStyle)](capi-drawing-text-typography-h.md#oh_drawing_settypographystylefontstylestruct) | 设置排版样式中默认文本样式的字体样式，包括字体字重、字体宽度和字体斜度。 |
| [OH\_Drawing\_FontStyleStruct OH\_Drawing\_TypographyStyleGetFontStyleStruct(OH\_Drawing\_TypographyStyle\* drawingStyle)](capi-drawing-text-typography-h.md#oh_drawing_typographystylegetfontstylestruct) | 获取排版样式中默认文本样式的字体样式，包括字体字重、字体宽度和字体斜度。 |
| [void OH\_Drawing\_TextStyleSetBackgroundRect(OH\_Drawing\_TextStyle\* style,const OH\_Drawing\_RectStyle\_Info\* rectStyleInfo, int styleId)](capi-drawing-text-typography-h.md#oh_drawing_textstylesetbackgroundrect) | 设置文本背景矩形框和样式id。样式id仅当背景框为圆角矩形时有效。 |
| [void OH\_Drawing\_TypographyHandlerAddSymbol(OH\_Drawing\_TypographyCreate\* handler, uint32\_t symbol)](capi-drawing-text-typography-h.md#oh_drawing_typographyhandleraddsymbol) | 设置排版创建过程中的符号。 |
| [void OH\_Drawing\_TextStyleAddFontFeature(OH\_Drawing\_TextStyle\* style, const char\* tag, int value)](capi-drawing-text-typography-h.md#oh_drawing_textstyleaddfontfeature) | 设置文本样式中指定字体特征是否启用。 |
| [void OH\_Drawing\_TextStyleAddFontVariation(OH\_Drawing\_TextStyle\* style, const char\* axis, const float value)](capi-drawing-text-typography-h.md#oh_drawing_textstyleaddfontvariation) | 添加可变字体属性。对应的字体文件（.ttf文件）需要支持可变调节，此接口才能生效。当对应的字体不支持可变调节时，此接口调用不生效。 |
| [OH\_Drawing\_FontFeature\* OH\_Drawing\_TextStyleGetFontFeatures(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetfontfeatures) | 获取指定文本样式的字体特征map容器中所有内容。 |
| [void OH\_Drawing\_TextStyleDestroyFontFeatures(OH\_Drawing\_FontFeature\* fontFeature, size\_t fontFeatureSize)](capi-drawing-text-typography-h.md#oh_drawing_textstyledestroyfontfeatures) | 释放存放字体特征所有内容的结构体数组所占用的空间。 |
| [size\_t OH\_Drawing\_TextStyleGetFontFeatureSize(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetfontfeaturesize) | 获取指定文本样式中字体特征map容器的大小。 |
| [void OH\_Drawing\_TextStyleClearFontFeature(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_textstyleclearfontfeature) | 清除指定文本样式的字体特征map容器中所有内容。 |
| [double OH\_Drawing\_TextStyleGetBaselineShift(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetbaselineshift) | 获取指定文本样式的基线偏移。 |
| [void OH\_Drawing\_TextStyleSetBaselineShift(OH\_Drawing\_TextStyle\* style, double lineShift)](capi-drawing-text-typography-h.md#oh_drawing_textstylesetbaselineshift) | 设置文本样式基线偏移。 |
| [void OH\_Drawing\_TypographyTextSetHeightBehavior(OH\_Drawing\_TypographyStyle\* style,OH\_Drawing\_TextHeightBehavior heightMode)](capi-drawing-text-typography-h.md#oh_drawing_typographytextsetheightbehavior) | 设置文本高度修饰符模式。 |
| [OH\_Drawing\_TextHeightBehavior OH\_Drawing\_TypographyTextGetHeightBehavior(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographytextgetheightbehavior) | 获取文本高度修饰符模式。 |
| [OH\_Drawing\_Font\_Metrics\* OH\_Drawing\_TypographyGetLineFontMetrics(OH\_Drawing\_Typography\* typography,size\_t lineNumber, size\_t\* fontMetricsSize)](capi-drawing-text-typography-h.md#oh_drawing_typographygetlinefontmetrics) | 从排版对象中目标行获取所有字体度量信息，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用，否则会返回空指针。不再需要[OH\_Drawing\_Font\_Metrics](capi-drawing-oh-drawing-font-metrics.md)时，请使用[OH\_Drawing\_TypographyDestroyLineFontMetrics](capi-drawing-text-typography-h.md#oh_drawing_typographydestroylinefontmetrics)接口释放该对象的指针。 |
| [void OH\_Drawing\_TypographyDestroyLineFontMetrics(OH\_Drawing\_Font\_Metrics\* lineFontMetric)](capi-drawing-text-typography-h.md#oh_drawing_typographydestroylinefontmetrics) | 释放指定行所有字体度量结构体集合所占用的所有空间。 |
| [bool OH\_Drawing\_TextStyleIsEqual(const OH\_Drawing\_TextStyle\* style, const OH\_Drawing\_TextStyle\* comparedStyle)](capi-drawing-text-typography-h.md#oh_drawing_textstyleisequal) | 判断两个文本样式对象是否相等，字宽属性不参与对比。 |
| [bool OH\_Drawing\_TextStyleIsEqualByFont(const OH\_Drawing\_TextStyle\* style, const OH\_Drawing\_TextStyle\* comparedStyle)](capi-drawing-text-typography-h.md#oh_drawing_textstyleisequalbyfont) | 判断两个文本样式对象的字体样式属性是否相等。 |
| [bool OH\_Drawing\_TextStyleIsAttributeMatched(const OH\_Drawing\_TextStyle\* style,const OH\_Drawing\_TextStyle\* comparedStyle, OH\_Drawing\_TextStyleType textStyleType)](capi-drawing-text-typography-h.md#oh_drawing_textstyleisattributematched) | 判断两个文本样式对象是否有一样的字体样式类型。 |
| [void OH\_Drawing\_TextStyleSetPlaceholder(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_textstylesetplaceholder) | 设置占位符。 |
| [bool OH\_Drawing\_TextStyleIsPlaceholder(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_textstyleisplaceholder) | 返回是否有设置文本占位符。 |
| [OH\_Drawing\_TextAlign OH\_Drawing\_TypographyStyleGetEffectiveAlignment(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographystylegeteffectivealignment) | 获取文本对齐模式。 |
| [bool OH\_Drawing\_TypographyStyleIsHintEnabled(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographystyleishintenabled) | 获取文本是否启用字形轮廓自动调整，字形轮廓自动调整用于在渲染小字号文本时改善其可读性和外观。 |
| [void OH\_Drawing\_SetTypographyStyleTextStrutStyle(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_StrutStyle\* strutstyle)](capi-drawing-text-typography-h.md#oh_drawing_settypographystyletextstrutstyle) | 设置文本支柱样式。 |
| [OH\_Drawing\_StrutStyle\* OH\_Drawing\_TypographyStyleGetStrutStyle(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographystylegetstrutstyle) | 获取文本支柱样式。 |
| [void OH\_Drawing\_TypographyStyleDestroyStrutStyle(OH\_Drawing\_StrutStyle\* strutstyle)](capi-drawing-text-typography-h.md#oh_drawing_typographystyledestroystrutstyle) | 释放被支柱样式对象占据的内存。 |
| [bool OH\_Drawing\_TypographyStyleStrutStyleEquals(OH\_Drawing\_StrutStyle\* from, OH\_Drawing\_StrutStyle\* to)](capi-drawing-text-typography-h.md#oh_drawing_typographystylestrutstyleequals) | 判断支柱样式结构体是否相同。 |
| [void OH\_Drawing\_TypographyStyleSetHintsEnabled(OH\_Drawing\_TypographyStyle\* style, bool hintsEnabled)](capi-drawing-text-typography-h.md#oh_drawing_typographystylesethintsenabled) | 设置文本是否启用字形轮廓自动调整，字形轮廓自动调整用于在渲染小字号文本时改善其可读性和外观。 |
| [void OH\_Drawing\_TypographyMarkDirty(OH\_Drawing\_Typography\* typography)](capi-drawing-text-typography-h.md#oh_drawing_typographymarkdirty) | 将排版标记为脏数据，用于初始化排版状态。调用排版对象的属性获取接口前，需先调用[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口进行排版布局。 |
| [int32\_t OH\_Drawing\_TypographyGetUnresolvedGlyphsCount(OH\_Drawing\_Typography\* typography)](capi-drawing-text-typography-h.md#oh_drawing_typographygetunresolvedglyphscount) | 获取文本中尚未解析的字形的数量，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用并生效之后调用。 |
| [void OH\_Drawing\_TypographyUpdateFontSize(OH\_Drawing\_Typography\* typography, size\_t from, size\_t to, float fontSize)](capi-drawing-text-typography-h.md#oh_drawing_typographyupdatefontsize) | 更新排版对象中的字体大小。 |
| [void OH\_Drawing\_TypographyUpdateFontColor(OH\_Drawing\_Typography\* typography, uint32\_t color)](capi-drawing-text-typography-h.md#oh_drawing_typographyupdatefontcolor) | 更新排版对象中的字体颜色。如果当前装饰线未设置颜色，使用该接口也会同时更新装饰线的颜色。使用该接口更新字体颜色属性后，可直接使用[OH\_Drawing\_TypographyPaint](capi-drawing-text-typography-h.md#oh_drawing_typographypaint)进行绘制生效。 |
| [void OH\_Drawing\_TypographyUpdateDecoration(OH\_Drawing\_Typography\* typography, OH\_Drawing\_TextDecoration decoration)](capi-drawing-text-typography-h.md#oh_drawing_typographyupdatedecoration) | 更新排版对象中的文本装饰线类型。使用该接口更新文本装饰线类型属性后，可直接使用[OH\_Drawing\_TypographyPaint](capi-drawing-text-typography-h.md#oh_drawing_typographypaint)进行绘制生效。 |
| [void OH\_Drawing\_TypographyUpdateDecorationThicknessScale(OH\_Drawing\_Typography\* typography,double decorationThicknessScale)](capi-drawing-text-typography-h.md#oh_drawing_typographyupdatedecorationthicknessscale) | 更新排版对象中的文本装饰线的粗细缩放比例。使用该接口更新文本装饰线粗细缩放比例属性后，可直接使用[OH\_Drawing\_TypographyPaint](capi-drawing-text-typography-h.md#oh_drawing_typographypaint)进行绘制生效。 |
| [void OH\_Drawing\_TypographyUpdateDecorationStyle(OH\_Drawing\_Typography\* typography,OH\_Drawing\_TextDecorationStyle decorationStyle)](capi-drawing-text-typography-h.md#oh_drawing_typographyupdatedecorationstyle) | 更新排版对象中的文本装饰线样式。使用该接口更新文本装饰线样式属性后，可直接使用[OH\_Drawing\_TypographyPaint](capi-drawing-text-typography-h.md#oh_drawing_typographypaint)进行绘制生效。 |
| [bool OH\_Drawing\_TypographyTextGetLineStyle(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographytextgetlinestyle) | 获取文本排版是否启用行样式。 |
| [OH\_Drawing\_FontWeight OH\_Drawing\_TypographyTextlineStyleGetFontWeight(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographytextlinestylegetfontweight) | 获取文本排版行样式字重。 |
| [OH\_Drawing\_FontStyle OH\_Drawing\_TypographyTextlineStyleGetFontStyle(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographytextlinestylegetfontstyle) | 获取文本排版样式中支柱样式的字体样式。 |
| [char\*\* OH\_Drawing\_TypographyTextlineStyleGetFontFamilies(OH\_Drawing\_TypographyStyle\* style, size\_t\* num)](capi-drawing-text-typography-h.md#oh_drawing_typographytextlinestylegetfontfamilies) | 获取文本排版行样式字体家族名。 |
| [void OH\_Drawing\_TypographyTextlineStyleDestroyFontFamilies(char\*\* fontFamilies, size\_t fontFamiliesNum)](capi-drawing-text-typography-h.md#oh_drawing_typographytextlinestyledestroyfontfamilies) | 释放字体家族占用的内存。 |
| [double OH\_Drawing\_TypographyTextlineStyleGetFontSize(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographytextlinestylegetfontsize) | 获取文本排版行样式字号。 |
| [double OH\_Drawing\_TypographyTextlineStyleGetHeightScale(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographytextlinestylegetheightscale) | 获取文本排版行样式的行高缩放系数。 |
| [bool OH\_Drawing\_TypographyTextlineStyleGetHeightOnly(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographytextlinestylegetheightonly) | 获取字体渲染过程中计算字体块高度相关参数的方法。 |
| [bool OH\_Drawing\_TypographyTextlineStyleGetHalfLeading(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographytextlinestylegethalfleading) | 获取文本排版行样式是否为一半行间距。 |
| [double OH\_Drawing\_TypographyTextlineStyleGetSpacingScale(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographytextlinestylegetspacingscale) | 获取文本排版行样式间距比例。 |
| [bool OH\_Drawing\_TypographyTextlineGetStyleOnly(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographytextlinegetstyleonly) | 获取文本排版是否仅启用行样式。 |
| [OH\_Drawing\_TextAlign OH\_Drawing\_TypographyGetTextAlign(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographygettextalign) | 获取文本对齐方式。 |
| [OH\_Drawing\_TextDirection OH\_Drawing\_TypographyGetTextDirection(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographygettextdirection) | 获取指定排版样式中的文本方向。 |
| [size\_t OH\_Drawing\_TypographyGetTextMaxLines(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographygettextmaxlines) | 获取文本的最大行数。 |
| [char\* OH\_Drawing\_TypographyGetTextEllipsis(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_typographygettextellipsis) | 获取指定排版样式设置的省略号文本。 |
| [void OH\_Drawing\_TypographyDestroyEllipsis(char\* ellipsis)](capi-drawing-text-typography-h.md#oh_drawing_typographydestroyellipsis) | 释放省略号文本占用的内存。 |
| [bool OH\_Drawing\_TypographyStyleEquals(OH\_Drawing\_TypographyStyle\* from, OH\_Drawing\_TypographyStyle\* to)](capi-drawing-text-typography-h.md#oh_drawing_typographystyleequals) | 判断排版样式是否相同，当前文本高度修饰符模式[OH\_Drawing\_TextHeightBehavior](capi-drawing-text-typography-h.md#oh_drawing_textheightbehavior)没有被纳入比较。 |
| [uint32\_t OH\_Drawing\_TextStyleGetColor(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetcolor) | 获取文本颜色。 |
| [OH\_Drawing\_TextDecorationStyle OH\_Drawing\_TextStyleGetDecorationStyle(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetdecorationstyle) | 获取文本装饰样式。 |
| [OH\_Drawing\_FontWeight OH\_Drawing\_TextStyleGetFontWeight(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetfontweight) | 获取字重。 |
| [OH\_Drawing\_FontStyle OH\_Drawing\_TextStyleGetFontStyle(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetfontstyle) | 获取指定文本样式的字体样式。 |
| [OH\_Drawing\_TextBaseline OH\_Drawing\_TextStyleGetBaseline(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetbaseline) | 获取指定文本样式的字体基线位置。 |
| [char\*\* OH\_Drawing\_TextStyleGetFontFamilies(OH\_Drawing\_TextStyle\* style, size\_t\* num)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetfontfamilies) | 获取字体家族名称列表。 |
| [void OH\_Drawing\_TextStyleDestroyFontFamilies(char\*\* fontFamilies, size\_t num)](capi-drawing-text-typography-h.md#oh_drawing_textstyledestroyfontfamilies) | 释放长度为num的字体家族名称列表占用的内存。 |
| [double OH\_Drawing\_TextStyleGetFontSize(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetfontsize) | 获取指定文本样式字号。 |
| [double OH\_Drawing\_TextStyleGetLetterSpacing(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetletterspacing) | 获取指定文本样式的字符间距。 |
| [double OH\_Drawing\_TextStyleGetWordSpacing(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetwordspacing) | 获取指定文本样式的单词间距。 |
| [double OH\_Drawing\_TextStyleGetFontHeight(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetfontheight) | 获取指定文本样式行高缩放系数。 |
| [bool OH\_Drawing\_TextStyleGetHalfLeading(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_textstylegethalfleading) | 获取指定文本样式一半行间距开关状态。 |
| [const char\* OH\_Drawing\_TextStyleGetLocale(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_textstylegetlocale) | 获取语言环境。 |
| [void OH\_Drawing\_TypographyDestroyTextBox(OH\_Drawing\_TextBox\* textBox)](capi-drawing-text-typography-h.md#oh_drawing_typographydestroytextbox) | 释放文本框占用的内存。 |
| [void OH\_Drawing\_SetTextShadow(OH\_Drawing\_TextShadow\* shadow, uint32\_t color, OH\_Drawing\_Point\* offset,double blurRadius)](capi-drawing-text-typography-h.md#oh_drawing_settextshadow) | 设置文本阴影对象的参数。 |
| [OH\_Drawing\_TextTab\* OH\_Drawing\_CreateTextTab(OH\_Drawing\_TextAlign alignment, float location)](capi-drawing-text-typography-h.md#oh_drawing_createtexttab) | 创建文本制表符对象。 |
| [void OH\_Drawing\_DestroyTextTab(OH\_Drawing\_TextTab\* tab)](capi-drawing-text-typography-h.md#oh_drawing_destroytexttab) | 释放文本制表符对象占据的内存。 |
| [OH\_Drawing\_TextAlign OH\_Drawing\_GetTextTabAlignment(OH\_Drawing\_TextTab\* tab)](capi-drawing-text-typography-h.md#oh_drawing_gettexttabalignment) | 获取文本制表符对象的对齐方式。 |
| [float OH\_Drawing\_GetTextTabLocation(OH\_Drawing\_TextTab\* tab)](capi-drawing-text-typography-h.md#oh_drawing_gettexttablocation) | 获取文本制表符的位置。 |
| [void OH\_Drawing\_SetTypographyTextTab(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TextTab\* tab)](capi-drawing-text-typography-h.md#oh_drawing_settypographytexttab) | 设置文本制表符对齐方式及位置。当设置了文本对齐方式或者省略号风格时制表符不生效，当制表符位置小于1.0时为替换成空格的效果。 |
| [size\_t OH\_Drawing\_GetDrawingArraySize(OH\_Drawing\_Array\* drawingArray)](capi-drawing-text-typography-h.md#oh_drawing_getdrawingarraysize) | 获取传入类型为对象数组[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)中的对象个数。 |
| [void OH\_Drawing\_SetTypographyTextTrailingSpaceOptimized(OH\_Drawing\_TypographyStyle\* style, bool trailingSpaceOptimized)](capi-drawing-text-typography-h.md#oh_drawing_settypographytexttrailingspaceoptimized) | 设置文本排版时行尾空格是否参与对齐计算。 |
| [void OH\_Drawing\_TypographyHandlerAddEncodedText(OH\_Drawing\_TypographyCreate\* handler, const void\* text,size\_t byteLength, OH\_Drawing\_TextEncoding textEncodingType)](capi-drawing-text-typography-h.md#oh_drawing_typographyhandleraddencodedtext) | 添加指定编码的文本。 |
| [void OH\_Drawing\_SetTypographyTextAutoSpace(OH\_Drawing\_TypographyStyle\* style, bool enableAutoSpace)](capi-drawing-text-typography-h.md#oh_drawing_settypographytextautospace) | 设置文本排版时是否启用自动间距。  默认不启用自动间距，一旦启用则会自动调整CJK（中文字符、日文字符、韩文字符）与西文（拉丁字母、西里尔字母、希腊字母）、CJK与数字、CJK与版权符号、版权符号与数字、版权符号与西文之间的间距。 |
| [void OH\_Drawing\_TypographyUpdateDecorationColor(OH\_Drawing\_Typography\* typography, uint32\_t color)](capi-drawing-text-typography-h.md#oh_drawing_typographyupdatedecorationcolor) | 更新排版对象中的文本装饰线颜色。  使用该接口更新文本装饰线颜色属性后，可直接使用[OH\_Drawing\_TypographyPaint](capi-drawing-text-typography-h.md#oh_drawing_typographypaint)进行绘制生效。 |
| [void OH\_Drawing\_SetTypographyVerticalAlignment(OH\_Drawing\_TypographyStyle\* style,OH\_Drawing\_TextVerticalAlignment align)](capi-drawing-text-typography-h.md#oh_drawing_settypographyverticalalignment) | 设置文本垂直对齐方式。 |
| [OH\_Drawing\_TypographyStyle\* OH\_Drawing\_CopyTypographyStyle(OH\_Drawing\_TypographyStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_copytypographystyle) | 创建一个段落样式的对象副本，用于拷贝一个已有的段落样式对象。 |
| [OH\_Drawing\_TextStyle\* OH\_Drawing\_CopyTextStyle(OH\_Drawing\_TextStyle\* style)](capi-drawing-text-typography-h.md#oh_drawing_copytextstyle) | 创建一个文本样式的对象副本，用于拷贝一个已有的文本样式对象。 |
| [OH\_Drawing\_TextShadow\* OH\_Drawing\_CopyTextShadow(OH\_Drawing\_TextShadow\* shadow)](capi-drawing-text-typography-h.md#oh_drawing_copytextshadow) | 创建一个文本阴影的对象副本，用于拷贝一个已有的文本阴影对象。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTextStyleAttributeDouble(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id, double value)](capi-drawing-text-typography-h.md#oh_drawing_settextstyleattributedouble) | 设置double类型文本样式的属性。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetTextStyleAttributeDouble(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id, double\* value)](capi-drawing-text-typography-h.md#oh_drawing_gettextstyleattributedouble) | 获取double类型文本样式的属性。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTextStyleAttributeInt(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id, int value)](capi-drawing-text-typography-h.md#oh_drawing_settextstyleattributeint) | 设置int类型文本样式的属性。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetTextStyleAttributeInt(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id, int\* value)](capi-drawing-text-typography-h.md#oh_drawing_gettextstyleattributeint) | 获取int类型文本样式的属性。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTypographyStyleAttributeDouble(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TypographyStyleAttributeId id, double value)](capi-drawing-text-typography-h.md#oh_drawing_settypographystyleattributedouble) | 设置double类型排版样式的属性。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetTypographyStyleAttributeDouble(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TypographyStyleAttributeId id, double\* value)](capi-drawing-text-typography-h.md#oh_drawing_gettypographystyleattributedouble) | 获取double类型排版样式的属性。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTypographyStyleAttributeInt(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TypographyStyleAttributeId id, int value)](capi-drawing-text-typography-h.md#oh_drawing_settypographystyleattributeint) | 设置int类型排版样式的属性。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetTypographyStyleAttributeInt(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TypographyStyleAttributeId id, int\* value)](capi-drawing-text-typography-h.md#oh_drawing_gettypographystyleattributeint) | 获取int类型排版样式的属性。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTypographyStyleAttributeBool(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TypographyStyleAttributeId id, bool value)](capi-drawing-text-typography-h.md#oh_drawing_settypographystyleattributebool) | 设置bool类型排版样式的属性。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetTypographyStyleAttributeBool(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TypographyStyleAttributeId id, bool\* value)](capi-drawing-text-typography-h.md#oh_drawing_gettypographystyleattributebool) | 获取bool类型排版样式的属性。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTypographyStyleAttributeDoubleArray(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TypographyStyleAttributeId id, double\* arrayValue, size\_t arrayLength)](capi-drawing-text-typography-h.md#oh_drawing_settypographystyleattributedoublearray) | 设置浮点数数组类型排版样式的属性。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetTypographyStyleAttributeDoubleArray(const OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TypographyStyleAttributeId id, double\*\* arrayValue, size\_t\* arrayLength)](capi-drawing-text-typography-h.md#oh_drawing_gettypographystyleattributedoublearray) | 获取浮点数数组类型排版样式的属性。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTypographyAttributeBool(OH\_Drawing\_Typography\* typography, OH\_Drawing\_TypographyAttributeId id, bool value)](capi-drawing-text-typography-h.md#oh_drawing_settypographyattributebool) | 设置bool类型的排版属性。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetTypographyAttributeBool(const OH\_Drawing\_Typography\* typography, OH\_Drawing\_TypographyAttributeId id, bool\* value)](capi-drawing-text-typography-h.md#oh_drawing_gettypographyattributebool) | 获取bool类型排版的属性。 |
| [void OH\_Drawing\_DestroyPositionAndAffinity(OH\_Drawing\_PositionAndAffinity\* positionAndAffinity)](capi-drawing-text-typography-h.md#oh_drawing_destroypositionandaffinity) | 释放[OH\_Drawing\_PositionAndAffinity](capi-drawing-oh-drawing-positionandaffinity.md)对象持有的内存。 |
| [OH\_Drawing\_Range\* OH\_Drawing\_TypographyGetCharacterRangeForGlyphRangeWithBuffer(OH\_Drawing\_Typography\* typography, size\_t glyphRangeStart, size\_t glyphRangeEnd, OH\_Drawing\_Range\*\* actualGlyphRange, OH\_Drawing\_TextEncoding textEncodingType)](capi-drawing-text-typography-h.md#oh_drawing_typographygetcharacterrangeforglyphrangewithbuffer) | 获取指定字形范围对应的字符范围。 |
| [OH\_Drawing\_PositionAndAffinity\* OH\_Drawing\_TypographyGetCharacterPositionAtCoordinateWithBuffer(OH\_Drawing\_Typography\* typography, double dx, double dy, OH\_Drawing\_TextEncoding textEncodingType)](capi-drawing-text-typography-h.md#oh_drawing_typographygetcharacterpositionatcoordinatewithbuffer) | 获取与指定坐标最接近的字符位置信息。 |
| [OH\_Drawing\_Range\* OH\_Drawing\_TypographyGetGlyphRangeForCharacterRangeWithBuffer(OH\_Drawing\_Typography\* typography, size\_t characterRangeStart, size\_t characterRangeEnd, OH\_Drawing\_Range\*\* actualCharacterRange, OH\_Drawing\_TextEncoding textEncodingType)](capi-drawing-text-typography-h.md#oh_drawing_typographygetglyphrangeforcharacterrangewithbuffer) | 获取指定字符范围对应的字形范围。 |
| [void OH\_Drawing\_ReleaseRangeBuffer(OH\_Drawing\_Range\* range)](capi-drawing-text-typography-h.md#oh_drawing_releaserangebuffer) | 释放[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象占用的内存。 |
| [OH\_Drawing\_RectSize OH\_Drawing\_TypographyLayoutWithConstraintsWithBuffer(OH\_Drawing\_Typography\* typography, OH\_Drawing\_RectSize constraintsRect, OH\_Drawing\_Array\*\* fitStrRangeArr, size\_t\* fitStrRangeArrayLen)](capi-drawing-text-typography-h.md#oh_drawing_typographylayoutwithconstraintswithbuffer) | 在约束矩形内布局文本。 |
| [OH\_Drawing\_Range\* OH\_Drawing\_GetRangeByArrayIndex(OH\_Drawing\_Array\* array, size\_t index)](capi-drawing-text-typography-h.md#oh_drawing_getrangebyarrayindex) | 根据数组索引获取指向OH\_Drawing\_Range对象的指针。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_ReleaseArrayBuffer(OH\_Drawing\_Array\* array)](capi-drawing-text-typography-h.md#oh_drawing_releasearraybuffer) | 释放[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)对象占用的内存。 |
| [void OH\_Drawing\_TextStyleAddFontVariationWithNormalization(OH\_Drawing\_TextStyle\* style, const char\* axis, const float normalizedValue)](capi-drawing-text-typography-h.md#oh_drawing_textstyleaddfontvariationwithnormalization) | 添加归一化后的可变字体属性。对应的字体文件（.ttf文件）需要支持可变调节，此接口才能生效。 |

## 枚举类型说明

### OH\_Drawing\_TextDirection

```c
enum OH_Drawing_TextDirection
```

**描述**

文字方向。

**起始版本：** 8

| 枚举项 | 描述 |
| --- | --- |
| TEXT\_DIRECTION\_RTL | 方向：从右到左。 |
| TEXT\_DIRECTION\_LTR | 方向：从左到右。 |

### OH\_Drawing\_TextAlign

```c
enum OH_Drawing_TextAlign
```

**描述**

文字对齐方式。

**起始版本：** 8

| 枚举项 | 描述 |
| --- | --- |
| TEXT\_ALIGN\_LEFT | 左对齐。 |
| TEXT\_ALIGN\_RIGHT | 右对齐。 |
| TEXT\_ALIGN\_CENTER | 居中对齐。 |
| TEXT\_ALIGN\_JUSTIFY | 两端对齐，即紧靠左和右边缘，中间单词空隙由空格填充，最后一行除外。 |
| TEXT\_ALIGN\_START | 当OH\_Drawing\_TextDirection是TEXT\_DIRECTION\_LTR时，TEXT\_ALIGN\_START和TEXT\_ALIGN\_LEFT相同；  类似地，当OH\_Drawing\_TextDirection是TEXT\_DIRECTION\_RTL时，TEXT\_ALIGN\_START和TEXT\_ALIGN\_RIGHT相同。 |
| TEXT\_ALIGN\_END | 当OH\_Drawing\_TextDirection是TEXT\_DIRECTION\_LTR时，TEXT\_ALIGN\_END和TEXT\_ALIGN\_RIGHT相同；  类似地，当OH\_Drawing\_TextDirection是TEXT\_DIRECTION\_RTL时，TEXT\_ALIGN\_END和TEXT\_ALIGN\_LEFT相同。 |

### OH\_Drawing\_FontWeight

```c
enum OH_Drawing_FontWeight
```

**描述**

字重。

**起始版本：** 8

| 枚举项 | 描述 |
| --- | --- |
| FONT\_WEIGHT\_100 | 字重为thin。 |
| FONT\_WEIGHT\_200 | 字重为extra-light。 |
| FONT\_WEIGHT\_300 | 字重为light。 |
| FONT\_WEIGHT\_400 | 字重为normal/regular。 |
| FONT\_WEIGHT\_500 | 字重为medium。 |
| FONT\_WEIGHT\_600 | 字重为semi-bold。 |
| FONT\_WEIGHT\_700 | 字重为bold。 |
| FONT\_WEIGHT\_800 | 字重为extra-bold。 |
| FONT\_WEIGHT\_900 | 字重为black。 |

### OH\_Drawing\_TextBaseline

```c
enum OH_Drawing_TextBaseline
```

**描述**

基线位置。

**起始版本：** 8

| 枚举项 | 描述 |
| --- | --- |
| TEXT\_BASELINE\_ALPHABETIC | 用于表音文字，基线在中间偏下的位置。 |
| TEXT\_BASELINE\_IDEOGRAPHIC | 用于表意文字，基线位于底部。 |

### OH\_Drawing\_TextDecoration

```c
enum OH_Drawing_TextDecoration
```

**描述**

文本装饰。

**起始版本：** 8

| 枚举项 | 描述 |
| --- | --- |
| TEXT\_DECORATION\_NONE = 0x0 | 无装饰。 |
| TEXT\_DECORATION\_UNDERLINE = 0x1 | 下划线。 |
| TEXT\_DECORATION\_OVERLINE = 0x2 | 上划线。 |
| TEXT\_DECORATION\_LINE\_THROUGH = 0x4 | 删除线。 |

### OH\_Drawing\_FontStyle

```c
enum OH_Drawing_FontStyle
```

**描述**

字体样式，包括非斜体、斜体和倾斜字体。

**起始版本：** 8

| 枚举项 | 描述 |
| --- | --- |
| FONT\_STYLE\_NORMAL | 非斜体。 |
| FONT\_STYLE\_ITALIC | 斜体。 |
| FONT\_STYLE\_OBLIQUE | 倾斜字体。 |

### OH\_Drawing\_PlaceholderVerticalAlignment

```c
enum OH_Drawing_PlaceholderVerticalAlignment
```

**描述**

占位符垂直对齐枚举。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| ALIGNMENT\_OFFSET\_AT\_BASELINE | 偏移于基线对齐。 |
| ALIGNMENT\_ABOVE\_BASELINE | 高于基线对齐。 |
| ALIGNMENT\_BELOW\_BASELINE | 低于基线对齐。 |
| ALIGNMENT\_TOP\_OF\_ROW\_BOX | 行框顶部对齐。 |
| ALIGNMENT\_BOTTOM\_OF\_ROW\_BOX | 行框底部对齐。 |
| ALIGNMENT\_CENTER\_OF\_ROW\_BOX | 行框中心对齐。 |
| ALIGNMENT\_FOLLOW\_PARAGRAPH | 跟随文本垂直对齐方式。  **起始版本：** 20 |

### OH\_Drawing\_TextVerticalAlignment

```c
enum OH_Drawing_TextVerticalAlignment
```

**描述**

垂直对齐方式枚举。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| TEXT\_VERTICAL\_ALIGNMENT\_BASELINE | 基线对齐。 |
| TEXT\_VERTICAL\_ALIGNMENT\_BOTTOM | 底部对齐。 |
| TEXT\_VERTICAL\_ALIGNMENT\_CENTER | 居中对齐。 |
| TEXT\_VERTICAL\_ALIGNMENT\_TOP | 顶部对齐。 |

### OH\_Drawing\_TextDecorationStyle

```c
enum OH_Drawing_TextDecorationStyle
```

**描述**

文本装饰样式枚举。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| TEXT\_DECORATION\_STYLE\_SOLID | 实心样式。 |
| TEXT\_DECORATION\_STYLE\_DOUBLE | 双重样式。 |
| TEXT\_DECORATION\_STYLE\_DOTTED | 圆点样式。 |
| TEXT\_DECORATION\_STYLE\_DASHED | 虚线样式。 |
| TEXT\_DECORATION\_STYLE\_WAVY | 波浪样式。 |

### OH\_Drawing\_EllipsisModal

```c
enum OH_Drawing_EllipsisModal
```

**描述**

省略号样式枚举。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| ELLIPSIS\_MODAL\_HEAD = 0 | 头部省略号模式，即省略号位置出现在行首。该枚举值仅在使用[OH\_Drawing\_SetTypographyTextMaxLines](capi-drawing-text-typography-h.md#oh_drawing_settypographytextmaxlines)接口设置文本最大行数为1时有效。 |
| ELLIPSIS\_MODAL\_MIDDLE = 1 | 中部省略号模式，即省略号位置出现在行的中间。该枚举值仅在使用[OH\_Drawing\_SetTypographyTextMaxLines](capi-drawing-text-typography-h.md#oh_drawing_settypographytextmaxlines)接口设置文本最大行数为1时有效。 |
| ELLIPSIS\_MODAL\_TAIL = 2 | 尾部省略号模式，即省略号位置出现在行的尾部。该枚举值在使用[OH\_Drawing\_SetTypographyTextMaxLines](capi-drawing-text-typography-h.md#oh_drawing_settypographytextmaxlines)接口设置文本最大行数为任何值时均有效。 |
| ELLIPSIS\_MODAL\_MULTILINE\_HEAD = 3 | 头部省略号模式，即省略号位置出现在行首。该枚举值在使用[OH\_Drawing\_SetTypographyTextMaxLines](capi-drawing-text-typography-h.md#oh_drawing_settypographytextmaxlines)接口设置文本最大行数为任何值时均有效。  **起始版本：** 24 |
| ELLIPSIS\_MODAL\_MULTILINE\_MIDDLE = 4 | 中间省略号模式，即省略号位置出现在行的中间。该枚举值在使用[OH\_Drawing\_SetTypographyTextMaxLines](capi-drawing-text-typography-h.md#oh_drawing_settypographytextmaxlines)接口设置文本最大行数为任何值时均有效。  **起始版本：** 24 |

### OH\_Drawing\_BreakStrategy

```c
enum OH_Drawing_BreakStrategy
```

**描述**

文本的中断策略枚举。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| BREAK\_STRATEGY\_GREEDY = 0 | 贪心策略，换行时尽可能填满每一行。 |
| BREAK\_STRATEGY\_HIGH\_QUALITY = 1 | 高质量策略，换行时优先考虑文本的连续性。 |
| BREAK\_STRATEGY\_BALANCED = 2 | 平衡策略，换行时在单词边界换行。 |

### OH\_Drawing\_WordBreakType

```c
enum OH_Drawing_WordBreakType
```

**描述**

单词的断词方式枚举。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| WORD\_BREAK\_TYPE\_NORMAL = 0 | 常规方式。 |
| WORD\_BREAK\_TYPE\_BREAK\_ALL = 1 | 全部中断方式。 |
| WORD\_BREAK\_TYPE\_BREAK\_WORD = 2 | 单词中断方式。 |
| WORD\_BREAK\_TYPE\_BREAK\_HYPHEN = 3 | 每行末尾单词尝试通过连字符"-"进行断行，若无法添加连字符"-"，则跟WORD\_BREAK\_TYPE\_BREAK\_WORD保持一致。  **起始版本：** 18 |

### OH\_Drawing\_RectHeightStyle

```c
enum OH_Drawing_RectHeightStyle
```

**描述**

矩形框高度样式枚举。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| RECT\_HEIGHT\_STYLE\_TIGHT | 紧密样式，文本框高度紧贴文本内容边界。 |
| RECT\_HEIGHT\_STYLE\_MAX | 最大样式，文本框高度取所有行中的最大高度。 |
| RECT\_HEIGHT\_STYLE\_INCLUDELINESPACEMIDDLE | 包含行间距中间样式，文本框高度包含行间距的中间部分。 |
| RECT\_HEIGHT\_STYLE\_INCLUDELINESPACETOP | 包含行间距顶部样式，文本框高度包含行间距的顶部部分。 |
| RECT\_HEIGHT\_STYLE\_INCLUDELINESPACEBOTTOM | 包含行间距底部样式，文本框高度包含行间距的底部部分。 |
| RECT\_HEIGHT\_STYLE\_STRUCT | 结构样式，使用支柱样式（StrutStyle）决定文本框高度。 |

### OH\_Drawing\_RectWidthStyle

```c
enum OH_Drawing_RectWidthStyle
```

**描述**

矩形框宽度样式枚举。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| RECT\_WIDTH\_STYLE\_TIGHT | 紧密样式，文本框宽度紧密贴合文本内容。 |
| RECT\_WIDTH\_STYLE\_MAX | 最大样式，扩展宽度以匹配所有行中最宽的矩形。 |

### OH\_Drawing\_TextBadgeType

```c
enum OH_Drawing_TextBadgeType
```

**描述**

上下标样式枚举。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| TEXT\_BADGE\_NONE | 不启用上标或下标。 |
| TEXT\_SUPERSCRIPT | 启用上标。 |
| TEXT\_SUBSCRIPT | 启用下标。 |

### OH\_Drawing\_FontConfigInfoErrorCode

```c
enum OH_Drawing_FontConfigInfoErrorCode
```

**描述**

系统字体配置信息列表错误码枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| SUCCESS\_FONT\_CONFIG\_INFO = 0 | 获取系统字体配置信息列表成功。 |
| ERROR\_FONT\_CONFIG\_INFO\_UNKNOWN = 1 | 未知错误。 |
| ERROR\_FONT\_CONFIG\_INFO\_PARSE\_FILE = 2 | 解析系统配置文件失败。 |
| ERROR\_FONT\_CONFIG\_INFO\_ALLOC\_MEMORY = 3 | 申请内存失败。 |
| ERROR\_FONT\_CONFIG\_INFO\_COPY\_STRING\_DATA = 4 | 拷贝字符串数据失败。 |

### OH\_Drawing\_FontWidth

```c
enum OH_Drawing_FontWidth
```

**描述**

字体宽度的枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| FONT\_WIDTH\_ULTRA\_CONDENSED = 1 | 表示超窄的字宽。 |
| FONT\_WIDTH\_EXTRA\_CONDENSED = 2 | 表示特窄的字宽。 |
| FONT\_WIDTH\_CONDENSED = 3 | 表示窄的字宽。 |
| FONT\_WIDTH\_SEMI\_CONDENSED = 4 | 表示半窄的字宽。 |
| FONT\_WIDTH\_NORMAL = 5 | 表示常规的字宽。 |
| FONT\_WIDTH\_SEMI\_EXPANDED = 6 | 表示半宽的字宽。 |
| FONT\_WIDTH\_EXPANDED = 7 | 表示宽的字宽。 |
| FONT\_WIDTH\_EXTRA\_EXPANDED = 8 | 表示特宽的字宽。 |
| FONT\_WIDTH\_ULTRA\_EXPANDED = 9 | 表示超宽的字宽。 |

### OH\_Drawing\_TextHeightBehavior

```c
enum OH_Drawing_TextHeightBehavior
```

**描述**

文本高度修饰符模式枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| TEXT\_HEIGHT\_ALL = 0x0 | 段落中第一行顶部和段落中最后一行底部[OH\_Drawing\_SetTextStyleFontHeight](capi-drawing-text-typography-h.md#oh_drawing_settextstylefontheight)设置的高度生效。 |
| TEXT\_HEIGHT\_DISABLE\_FIRST\_ASCENT = 0x1 | 禁止段落中第一行顶部[OH\_Drawing\_SetTextStyleFontHeight](capi-drawing-text-typography-h.md#oh_drawing_settextstylefontheight)设置的高度生效。 |
| TEXT\_HEIGHT\_DISABLE\_LAST\_ASCENT = 0x2 | 禁止段落中最后一行底部[OH\_Drawing\_SetTextStyleFontHeight](capi-drawing-text-typography-h.md#oh_drawing_settextstylefontheight)设置的高度生效。 |
| TEXT\_HEIGHT\_DISABLE\_ALL = 0x1 | 0x2 | 禁止段落中第一行顶部和段落中最后一行底部[OH\_Drawing\_SetTextStyleFontHeight](capi-drawing-text-typography-h.md#oh_drawing_settextstylefontheight)设置的高度生效。 |

### OH\_Drawing\_TextStyleType

```c
enum OH_Drawing_TextStyleType
```

**描述**

文本样式类型枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| TEXT\_STYLE\_NONE | 无文本样式。 |
| TEXT\_STYLE\_ALL\_ATTRIBUTES | 所有文本样式。 |
| TEXT\_STYLE\_FONT | 字体样式。 |
| TEXT\_STYLE\_FOREGROUND | 文本前景样式。 |
| TEXT\_STYLE\_BACKGROUND | 文本背景样式。 |
| TEXT\_STYLE\_SHADOW | 文本阴影样式。 |
| TEXT\_STYLE\_DECORATIONS | 文本装饰样式。 |
| TEXT\_STYLE\_LETTER\_SPACING | 文本字符间距样式。 |
| TEXT\_STYLE\_WORD\_SPACING | 文本单词间距样式。 |

### OH\_Drawing\_LineHeightStyle

```c
enum OH_Drawing_LineHeightStyle
```

**描述**

行高缩放基数样式枚举。默认样式为TEXT\_LINE\_HEIGHT\_BY\_FONT\_SIZE。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| TEXT\_LINE\_HEIGHT\_BY\_FONT\_SIZE = 0 | 以字号大小作为缩放基数。  行高计算公式：FontSize \* FontHeight。  FontSize可由[OH\_Drawing\_TextStyleGetFontSize](capi-drawing-text-typography-h.md#oh_drawing_textstylegetfontsize)接口获取。  FontHeight可由[OH\_Drawing\_TextStyleGetFontHeight](capi-drawing-text-typography-h.md#oh_drawing_textstylegetfontheight)接口获取。 |
| TEXT\_LINE\_HEIGHT\_BY\_FONT\_HEIGHT = 1 | 以字形高度作为缩放基数。  行高计算公式：字形高度 \* FontHeight。  字形高度由文本经过字体文件塑形得到。  FontHeight（可由[OH\_Drawing\_TextStyleGetFontHeight](capi-drawing-text-typography-h.md#oh_drawing_textstylegetfontheight)获取）。 |

### OH\_Drawing\_TextStyleAttributeId

```c
enum OH_Drawing_TextStyleAttributeId
```

**描述**

文本样式属性枚举。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| TEXT\_STYLE\_ATTR\_D\_LINE\_HEIGHT\_MAXIMUM = 0 | 行高上限。  若同时开启行高缩放，当FontHeight（可由[OH\_Drawing\_TextStyleGetFontHeight](capi-drawing-text-typography-h.md#oh_drawing_textstylegetfontheight)接口获取）大于0时行高上限才生效。  取值范围为单精度浮点数正数部分，默认值为单精度浮点数上限。 |
| TEXT\_STYLE\_ATTR\_D\_LINE\_HEIGHT\_MINIMUM = 1 | 行高下限。  若同时开启行高缩放，当FontHeight（可由[OH\_Drawing\_TextStyleGetFontHeight](capi-drawing-text-typography-h.md#oh_drawing_textstylegetfontheight)接口获取）大于0时行高下限才生效。  取值范围为单精度浮点数非负部分，默认值为0。 |
| TEXT\_STYLE\_ATTR\_I\_LINE\_HEIGHT\_STYLE = 2 | 行高缩放基数样式。具体行高缩放基数样式可见[OH\_Drawing\_LineHeightStyle](capi-drawing-text-typography-h.md#oh_drawing_lineheightstyle)。 |
| TEXT\_STYLE\_ATTR\_I\_FONT\_WIDTH = 3 | 字宽。 |
| TEXT\_STYLE\_ATTR\_I\_FONT\_EDGING = 4 | 字体边缘处理方式。默认为抗锯齿，具体字体边缘处理方式可见[OH\_Drawing\_FontEdging](capi-drawing-font-h.md#oh_drawing_fontedging)。  **起始版本：** 24 |

### OH\_Drawing\_TypographyStyleAttributeId

```c
enum OH_Drawing_TypographyStyleAttributeId
```

**描述**

排版样式属性枚举。

针对排版样式和文本样式中的共有属性，建议优先使用文本样式属性（可由[OH\_Drawing\_TextStyleAttributeId](capi-drawing-text-typography-h.md#oh_drawing_textstyleattributeid)获取）。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| TYPOGRAPHY\_STYLE\_ATTR\_D\_LINE\_HEIGHT\_MAXIMUM = 0 | 行高上限。  若同时开启行高缩放，当FontHeight（可由[OH\_Drawing\_TextStyleGetFontHeight](capi-drawing-text-typography-h.md#oh_drawing_textstylegetfontheight)接口获取）大于0时行高上限才生效。  取值范围为单精度浮点数正数部分。 |
| TYPOGRAPHY\_STYLE\_ATTR\_D\_LINE\_HEIGHT\_MINIMUM = 1 | 行高下限。  若同时开启行高缩放，当FontHeight（可由[OH\_Drawing\_TextStyleGetFontHeight](capi-drawing-text-typography-h.md#oh_drawing_textstylegetfontheight)接口获取）大于0时行高下限才生效。  取值范围为单精度浮点数非负部分，默认值为0。 |
| TYPOGRAPHY\_STYLE\_ATTR\_D\_LINE\_SPACING = 2 | 行间距。  lineSpacing不受行高上下限的限制。  尾行默认添加行间距。  可通过[OH\_Drawing\_TypographyTextSetHeightBehavior](capi-drawing-text-typography-h.md#oh_drawing_typographytextsetheightbehavior)接口设置textHeightBehavior为DISABLE\_LAST\_ASCENT禁用尾行行间距。  默认值为0。 |
| TYPOGRAPHY\_STYLE\_ATTR\_I\_LINE\_HEIGHT\_STYLE = 3 | 行高缩放基数样式。具体行高缩放基数样式可见[OH\_Drawing\_LineHeightStyle](capi-drawing-text-typography-h.md#oh_drawing_lineheightstyle)。 |
| TYPOGRAPHY\_STYLE\_ATTR\_I\_FONT\_WIDTH = 4 | 字宽。 |
| TYPOGRAPHY\_STYLE\_ATTR\_B\_COMPRESS\_HEAD\_PUNCTUATION = 5 | 设置文本排版时是否启用行首标点压缩。  **说明：**  1. 需要字体文件支持[OH\_Drawing\_FontFeature](capi-drawing-oh-drawing-fontfeature.md)中的"ss08"特性，否则无法压缩。  2. 在行首标点压缩范围内的标点才在本特性作用范围内。  **起始版本：** 23 |
| TYPOGRAPHY\_STYLE\_ATTR\_B\_INCLUDE\_FONT\_PADDING = 6 | 设置文本排版时是否启用字体内部的padding。  **起始版本：** 23 |
| TYPOGRAPHY\_STYLE\_ATTR\_B\_FALLBACK\_LINE\_SPACING = 7 | 设置文本排版时是否启用行间距回退机制。  **起始版本：** 23 |
| TYPOGRAPHY\_STYLE\_ATTR\_I\_ELLIPSIS\_MODAL = 8 | 省略号样式。具体省略号样式可见[OH\_Drawing\_EllipsisModal](capi-drawing-text-typography-h.md#oh_drawing_ellipsismodal)。  **起始版本：** 24 |
| TYPOGRAPHY\_STYLE\_ATTR\_DA\_LINE\_HEAD\_INDENT = 9 | 行首缩进数组。  缩进数组值需全部大于等于0，数组中每个元素代表一行缩进值，当实际文本行数超过缩进数组个数时，超过行的缩进为数组最后一个值。  **起始版本：** 26.0.0 |
| TYPOGRAPHY\_STYLE\_ATTR\_D\_FIRST\_LINE\_HEAD\_INDENT = 10 | 段落首行缩进。缩进值需大于等于0。  **起始版本：** 26.0.0 |
| TYPOGRAPHY\_STYLE\_ATTR\_DA\_LINE\_TAIL\_INDENT = 11 | 行尾缩进数组。  缩进数组值需全部大于等于0，数组中每个元素代表一行缩进值，当实际文本行数超过缩进数组个数时，超过行的缩进为数组最后一个值。  **起始版本：** 26.0.0 |

### OH\_Drawing\_TypographyAttributeId

```c
enum OH_Drawing_TypographyAttributeId
```

**描述**

排版属性枚举。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| TYPOGRAPHY\_ATTR\_B\_FORCE\_REUSE\_RASTER\_RESULT = 0 | 是否强制复用光栅化结果。设置后，在下次调用[OH\_Drawing\_TypographyPaint](capi-drawing-text-typography-h.md#oh_drawing_typographypaint)绘制时生效。  true表示强制复用光栅化结果，false表示允许更新光栅化结果，默认值为false。 |

## 函数说明

### OH\_Drawing\_CreateTypographyStyle()

```c
OH_Drawing_TypographyStyle* OH_Drawing_CreateTypographyStyle(void)
```

**描述**

创建指向OH\_Drawing\_TypographyStyle对象的指针。不再需要[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)时，请使用[OH\_Drawing\_DestroyTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_destroytypographystyle)接口释放该对象的指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* | 指向创建的[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)对象的指针。 |

### OH\_Drawing\_DestroyTypographyStyle()

```c
void OH_Drawing_DestroyTypographyStyle(OH_Drawing_TypographyStyle* style)
```

**描述**

释放被OH\_Drawing\_TypographyStyle对象占据的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)对象的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

### OH\_Drawing\_SetTypographyTextDirection()

```c
void OH_Drawing_SetTypographyTextDirection(OH_Drawing_TypographyStyle* style, int direction)
```

**描述**

设置指定排版样式中的文本方向。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| int direction | 设置文本方向，设置0为从右到左，设置1或其他值为从左到右，具体可见[OH\_Drawing\_TextDirection](capi-drawing-text-typography-h.md#oh_drawing_textdirection)枚举。 |

### OH\_Drawing\_SetTypographyTextAlign()

```c
void OH_Drawing_SetTypographyTextAlign(OH_Drawing_TypographyStyle* style, int align)
```

**描述**

设置文本对齐方式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| int align | 设置文本对齐方式，设置1为右对齐，设置2为居中对齐，设置3为两端对齐，设置4为与文字方向相同，设置5为文字方向相反，设置0或其它为左对齐，具体可见[OH\_Drawing\_TextAlign](capi-drawing-text-typography-h.md#oh_drawing_textalign)枚举。 |

### OH\_Drawing\_TypographyGetEffectiveAlignment()

```c
int OH_Drawing_TypographyGetEffectiveAlignment(OH_Drawing_TypographyStyle* style)
```

**描述**

获取文字对齐方式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**废弃版本：** 18

**替代接口：** [OH\_Drawing\_TypographyStyleGetEffectiveAlignment](capi-drawing-text-typography-h.md#oh_drawing_typographystylegeteffectivealignment)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)对象的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回文字对齐方式。 |

### OH\_Drawing\_SetTypographyTextMaxLines()

```c
void OH_Drawing_SetTypographyTextMaxLines(OH_Drawing_TypographyStyle* style, int lineNumber)
```

**描述**

设置文本最大行数。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| int lineNumber | 最大行数，整数。传入0或负数时不显示文字。 |

### OH\_Drawing\_CreateTextStyle()

```c
OH_Drawing_TextStyle* OH_Drawing_CreateTextStyle(void)
```

**描述**

创建指向OH\_Drawing\_TextStyle对象的指针。不再需要[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)时，请使用[OH\_Drawing\_DestroyTextStyle](capi-drawing-text-typography-h.md#oh_drawing_destroytextstyle)接口释放该对象的指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* | 指向创建的[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)对象的指针。 |

### OH\_Drawing\_TypographyGetTextStyle()

```c
OH_Drawing_TextStyle* OH_Drawing_TypographyGetTextStyle(OH_Drawing_TypographyStyle* style)
```

**描述**

获取指定排版样式中设置的默认文本样式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)对象的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* | 返回指向文本样式[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，不再需要时，请使用[OH\_Drawing\_DestroyTextStyle](capi-drawing-text-typography-h.md#oh_drawing_destroytextstyle)释放该对象指针。 |

### OH\_Drawing\_DestroyTextStyle()

```c
void OH_Drawing_DestroyTextStyle(OH_Drawing_TextStyle* style)
```

**描述**

释放被OH\_Drawing\_TextStyle对象占据的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

### OH\_Drawing\_SetTextStyleColor()

```c
void OH_Drawing_SetTextStyleColor(OH_Drawing_TextStyle* style, uint32_t color)
```

**描述**

设置文本颜色。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| uint32\_t color | 文本颜色，使用ARGB格式，例如入参为0xFFFF0000表示不透明红色。 |

### OH\_Drawing\_SetTextStyleFontSize()

```c
void OH_Drawing_SetTextStyleFontSize(OH_Drawing_TextStyle* style, double fontSize)
```

**描述**

设置字号。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| double fontSize | 字号，单位为物理像素px。 |

### OH\_Drawing\_SetTextStyleFontWeight()

```c
void OH_Drawing_SetTextStyleFontWeight(OH_Drawing_TextStyle* style, int fontWeight)
```

**描述**

设置字重。在HarmonyOS 6.1.1之前，仅系统字体中的可变字体支持字重调节；从HarmonyOS 6.1.1开始，系统字体与三方注册字体中的可变字体均支持字重调节。非可变字体设置字重值小于semi-bold时字体粗细无变化，设置字重值大于等于semi-bold时可能会触发伪加粗效果。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| int fontWeight | 设置字重，设置0字重为thin，设置1字重为extra-light，设置2字重为light，设置4字重为medium，设置5字重为semi-bold，  设置6字重为bold，设置7字重为extra-bold，设置8字重为black，设置3或其它字重为normal/regular，具体可见[OH\_Drawing\_FontWeight](capi-drawing-text-typography-h.md#oh_drawing_fontweight)枚举。 |

### OH\_Drawing\_SetTextStyleBaseLine()

```c
void OH_Drawing_SetTextStyleBaseLine(OH_Drawing_TextStyle* style, int baseline)
```

**描述**

设置文本样式的字体基线位置。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| int baseline | 设置字体基线位置，设置1基线位于底部，设置0或其它基线在中间偏下的位置，具体可见[OH\_Drawing\_TextBaseline](capi-drawing-text-typography-h.md#oh_drawing_textbaseline)枚举。 |

### OH\_Drawing\_SetTextStyleDecoration()

```c
void OH_Drawing_SetTextStyleDecoration(OH_Drawing_TextStyle* style, int decoration)
```

**描述**

设置指定文本样式中的装饰线类型，只能设置一个装饰线类型，添加多个需要使用[OH\_Drawing\_AddTextStyleDecoration](capi-drawing-text-typography-h.md#oh_drawing_addtextstyledecoration)。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| int decoration | 设置装饰，设置1为下划线，设置2为上划线，设置4为删除线，设置0或其它为无装饰，具体可见[OH\_Drawing\_TextDecoration](capi-drawing-text-typography-h.md#oh_drawing_textdecoration)枚举。 |

### OH\_Drawing\_AddTextStyleDecoration()

```c
void OH_Drawing_AddTextStyleDecoration(OH_Drawing_TextStyle* style, int decoration)
```

**描述**

新增指定装饰，可同时显示多种装饰线。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| int decoration | 要新增的装饰。设置1为新增下划线，设置2为新增上划线，设置4为新增删除线。可通过位或操作一次新增多种装饰线。  设置非[OH\_Drawing\_TextDecoration](capi-drawing-text-typography-h.md#oh_drawing_textdecoration)枚举的装饰样式则保持原有装饰。 |

### OH\_Drawing\_RemoveTextStyleDecoration()

```c
void OH_Drawing_RemoveTextStyleDecoration(OH_Drawing_TextStyle* style, int decoration)
```

**描述**

删除指定装饰。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| int decoration | 要删除的装饰。应该与现有的装饰相匹配，设置1为删除下划线，设置2为删除上划线，设置4为删除删除线，可通过位或操作一次删除多种装饰线。  设置非[OH\_Drawing\_TextDecoration](capi-drawing-text-typography-h.md#oh_drawing_textdecoration)枚举的装饰样式则保持原有装饰。 |

### OH\_Drawing\_SetTextStyleDecorationColor()

```c
void OH_Drawing_SetTextStyleDecorationColor(OH_Drawing_TextStyle* style, uint32_t color)
```

**描述**

设置指定文本样式中的装饰线颜色。如果不调用该接口或者设置color为0时，装饰线颜色跟随文本颜色。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| uint32\_t color | 装饰线颜色，使用ARGB格式，例如入参为0xFFFF0000表示不透明红色。如果不调用该接口或者设置color为0时，装饰线颜色跟随文本颜色。 |

### OH\_Drawing\_SetTextStyleFontHeight()

```c
void OH_Drawing_SetTextStyleFontHeight(OH_Drawing_TextStyle* style, double fontHeight)
```

**描述**

设置行高，按当前字体大小的倍数进行设置。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| double fontHeight | 当前字体大小的倍数。 |

### OH\_Drawing\_SetTextStyleFontFamilies()

```c
void OH_Drawing_SetTextStyleFontFamilies(OH_Drawing_TextStyle* style, int fontFamiliesNumber, const char* fontFamilies[])
```

**描述**

设置指定文本样式的字体家族类型。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| int fontFamiliesNumber | 字体名称数量，禁止填入负数。 |
| fontFamilies | 指向字体家族类型的指针。 |

### OH\_Drawing\_SetTextStyleFontStyle()

```c
void OH_Drawing_SetTextStyleFontStyle(OH_Drawing_TextStyle* style, int fontStyle)
```

**描述**

为指定文本样式设置字体样式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| int fontStyle | 设置字体样式，设置1为斜体，设置2为倾斜字体，设置0或其它为非斜体，具体可见[OH\_Drawing\_FontStyle](capi-drawing-text-typography-h.md#oh_drawing_fontstyle)枚举。 |

### OH\_Drawing\_SetTextStyleLocale()

```c
void OH_Drawing_SetTextStyleLocale(OH_Drawing_TextStyle* style, const char* locale)
```

**描述**

设置文本语言环境。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| const char\* locale | 语言类型，数据类型为指向char的指针。格式参考BCP 47语言标签标准，如'en'代表英文，'zh-Hans'代表简体中文，'zh-Hant'代表繁体中文。未指定时默认locale为'zh-Hans'。 |

### OH\_Drawing\_SetTextStyleForegroundBrush()

```c
void OH_Drawing_SetTextStyleForegroundBrush(OH_Drawing_TextStyle* style, OH_Drawing_Brush* foregroundBrush)
```

**描述**

设置指定文本样式中的前景色画刷。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* foregroundBrush | 指向画刷[OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)对象的指针，由[OH\_Drawing\_BrushCreate](capi-drawing-brush-h.md#oh_drawing_brushcreate)获取。 |

### OH\_Drawing\_TextStyleGetForegroundBrush()

```c
void OH_Drawing_TextStyleGetForegroundBrush(OH_Drawing_TextStyle* style, OH_Drawing_Brush* foregroundBrush)
```

**描述**

返回设置的前景色画刷。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* foregroundBrush | 指向画刷[OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)对象的指针，由[OH\_Drawing\_BrushCreate](capi-drawing-brush-h.md#oh_drawing_brushcreate)获取。 |

### OH\_Drawing\_SetTextStyleForegroundPen()

```c
void OH_Drawing_SetTextStyleForegroundPen(OH_Drawing_TextStyle* style, OH_Drawing_Pen* foregroundPen)
```

**描述**

设置指定文本样式中的前景色画笔。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* foregroundPen | 指向画笔[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)对象的指针，由[OH\_Drawing\_PenCreate](capi-drawing-pen-h.md#oh_drawing_pencreate)获取。 |

### OH\_Drawing\_TextStyleGetForegroundPen()

```c
void OH_Drawing_TextStyleGetForegroundPen(OH_Drawing_TextStyle* style, OH_Drawing_Pen* foregroundPen)
```

**描述**

返回设置的前景色画笔。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* foregroundPen | 指向画笔[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)对象的指针，由[OH\_Drawing\_PenCreate](capi-drawing-pen-h.md#oh_drawing_pencreate)获取。 |

### OH\_Drawing\_SetTextStyleBackgroundBrush()

```c
void OH_Drawing_SetTextStyleBackgroundBrush(OH_Drawing_TextStyle* style, OH_Drawing_Brush* backgroundBrush)
```

**描述**

设置指定文本样式中的背景色画刷。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* backgroundBrush | 指向画刷[OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)对象的指针，由[OH\_Drawing\_BrushCreate](capi-drawing-brush-h.md#oh_drawing_brushcreate)获取。 |

### OH\_Drawing\_TextStyleGetBackgroundBrush()

```c
void OH_Drawing_TextStyleGetBackgroundBrush(OH_Drawing_TextStyle* style, OH_Drawing_Brush* backgroundBrush)
```

**描述**

返回设置的背景色画刷。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* backgroundBrush | 指向画刷[OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)对象的指针，由[OH\_Drawing\_BrushCreate](capi-drawing-brush-h.md#oh_drawing_brushcreate)获取。 |

### OH\_Drawing\_SetTextStyleBackgroundPen()

```c
void OH_Drawing_SetTextStyleBackgroundPen(OH_Drawing_TextStyle* style, OH_Drawing_Pen* backgroundPen)
```

**描述**

设置指定文本样式中的背景色画笔。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* backgroundPen | 指向画笔[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)对象的指针，由[OH\_Drawing\_PenCreate](capi-drawing-pen-h.md#oh_drawing_pencreate)获取。 |

### OH\_Drawing\_TextStyleGetBackgroundPen()

```c
void OH_Drawing_TextStyleGetBackgroundPen(OH_Drawing_TextStyle* style, OH_Drawing_Pen* backgroundPen)
```

**描述**

返回设置的背景色画笔。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* backgroundPen | 指向画笔[OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)对象的指针，由[OH\_Drawing\_PenCreate](capi-drawing-pen-h.md#oh_drawing_pencreate)获取。 |

### OH\_Drawing\_CreateTypographyHandler()

```c
OH_Drawing_TypographyCreate* OH_Drawing_CreateTypographyHandler(OH_Drawing_TypographyStyle* style, OH_Drawing_FontCollection* fontCollection)
```

**描述**

创建指向OH\_Drawing\_TypographyCreate对象的指针。不再需要[OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)时，请使用[OH\_Drawing\_DestroyTypographyHandler](capi-drawing-text-typography-h.md#oh_drawing_destroytypographyhandler)接口释放该对象的指针。建议优先使用[OH\_Drawing\_CreateSharedFontCollection](capi-drawing-font-collection-h.md#oh_drawing_createsharedfontcollection)函数创建[OH\_Drawing\_FontCollection](capi-drawing-oh-drawing-fontcollection.md)对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| [OH\_Drawing\_FontCollection](capi-drawing-oh-drawing-fontcollection.md)\* fontCollection | 指向字体集对象[OH\_Drawing\_FontCollection](capi-drawing-oh-drawing-fontcollection.md)的指针，由[OH\_Drawing\_CreateFontCollection](capi-drawing-font-collection-h.md#oh_drawing_createfontcollection)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)\* | 指向新创建的OH\_Drawing\_TypographyCreate对象的指针。 |

### OH\_Drawing\_DestroyTypographyHandler()

```c
void OH_Drawing_DestroyTypographyHandler(OH_Drawing_TypographyCreate* handler)
```

**描述**

释放被OH\_Drawing\_TypographyCreate对象占据的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)\* handler | 指向[OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)对象的指针，由[OH\_Drawing\_CreateTypographyHandler](capi-drawing-text-typography-h.md#oh_drawing_createtypographyhandler)获取。 |

### OH\_Drawing\_TypographyHandlerPushTextStyle()

```c
void OH_Drawing_TypographyHandlerPushTextStyle(OH_Drawing_TypographyCreate* handler, OH_Drawing_TextStyle* style)
```

**描述**

将指定文本样式压入文本样式栈，后续添加的文本总是会使用栈顶的文本样式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)\* handler | 指向[OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)对象的指针，由[OH\_Drawing\_CreateTypographyHandler](capi-drawing-text-typography-h.md#oh_drawing_createtypographyhandler)获取。 |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

### OH\_Drawing\_TypographyHandlerAddText()

```c
void OH_Drawing_TypographyHandlerAddText(OH_Drawing_TypographyCreate* handler, const char* text)
```

**描述**

设置文本内容。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)\* handler | 指向[OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)对象的指针，由[OH\_Drawing\_CreateTypographyHandler](capi-drawing-text-typography-h.md#oh_drawing_createtypographyhandler)获取。 |
| const char\* text | 指向文本内容的指针。 |

### OH\_Drawing\_TypographyHandlerPopTextStyle()

```c
void OH_Drawing_TypographyHandlerPopTextStyle(OH_Drawing_TypographyCreate* handler)
```

**描述**

从文本样式栈中弹出栈顶文本样式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)\* handler | 指向[OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)对象的指针，由[OH\_Drawing\_CreateTypographyHandler](capi-drawing-text-typography-h.md#oh_drawing_createtypographyhandler)获取。 |

### OH\_Drawing\_CreateTypography()

```c
OH_Drawing_Typography* OH_Drawing_CreateTypography(OH_Drawing_TypographyCreate* handler)
```

**描述**

创建指向OH\_Drawing\_Typography对象的指针。不再需要[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)时，请使用[OH\_Drawing\_DestroyTypography](capi-drawing-text-typography-h.md#oh_drawing_destroytypography)接口释放该对象的指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)\* handler | 指向[OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)对象的指针，由[OH\_Drawing\_CreateTypographyHandler](capi-drawing-text-typography-h.md#oh_drawing_createtypographyhandler)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* | 指向OH\_Drawing\_Typography对象的指针。 |

### OH\_Drawing\_DestroyTypography()

```c
void OH_Drawing_DestroyTypography(OH_Drawing_Typography* typography)
```

**描述**

释放OH\_Drawing\_Typography对象占据的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向排版对象[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |

### OH\_Drawing\_TypographyLayout()

```c
void OH_Drawing_TypographyLayout(OH_Drawing_Typography* typography, double maxWidth)
```

**描述**

对排版对象进行布局计算，根据指定的最大宽度对文本进行换行。调用该接口后，排版对象的各项属性才可被正确获取。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向排版对象[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| double maxWidth | 文本排版的单行最大宽度，单位为物理像素px。取值应大于0。 |

### OH\_Drawing\_TypographyPaint()

```c
void OH_Drawing_TypographyPaint(OH_Drawing_Typography* typography, OH_Drawing_Canvas* canvas, double positionX, double positionY)
```

**描述**

在指定位置绘制文本，从左上角开始绘制，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用并生效之后调用。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向OH\_Drawing\_Canvas对象的指针，由[OH\_Drawing\_CanvasCreate](capi-drawing-canvas-h.md#oh_drawing_canvascreate)获取。 |
| double positionX | 文本绘制起始位置的水平坐标（即文本区域左上角的x坐标），单位为物理像素px。以画布左上角为坐标原点，向右为正方向。 |
| double positionY | 文本绘制起始位置的垂直坐标（即文本区域左上角的y坐标），单位为物理像素px。以画布左上角为坐标原点，向下为正方向。 |

### OH\_Drawing\_TypographyPaintOnPath()

```c
void OH_Drawing_TypographyPaintOnPath(OH_Drawing_Typography* typography, OH_Drawing_Canvas* canvas,OH_Drawing_Path* path, double hOffset, double vOffset)
```

**描述**

沿指定路径绘制文本，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用并生效之后调用。建议搭配[OH\_Drawing\_SetTypographyTextMaxLines](capi-drawing-text-typography-h.md#oh_drawing_settypographytextmaxlines)接口设置最大行为1行，避免因文本宽度超过排版宽度出现跨行重叠问题。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向OH\_Drawing\_Canvas对象的指针，由[OH\_Drawing\_CanvasCreate](capi-drawing-canvas-h.md#oh_drawing_canvascreate)获取。 |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向OH\_Drawing\_Path对象的指针，由[OH\_Drawing\_PathCreate](capi-drawing-path-h.md#oh_drawing_pathcreate)获取。 |
| double hOffset | 水平偏移量，单位为物理像素px。文本沿路径的水平偏移（X 轴），向右为正，向左为负。 |
| double vOffset | 垂直偏移量，单位为物理像素px。文本沿路径的垂直偏移（Y 轴），向下为正，向上为负。 |

### OH\_Drawing\_TypographyGetMaxWidth()

```c
double OH_Drawing_TypographyGetMaxWidth(OH_Drawing_Typography* typography)
```

**描述**

获取用户设置的排版宽度，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回最大宽度，单位为物理像素px。 |

### OH\_Drawing\_TypographyGetHeight()

```c
double OH_Drawing_TypographyGetHeight(OH_Drawing_Typography* typography)
```

**描述**

获取排版对象整体的高度，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回高度，单位为物理像素px。 |

### OH\_Drawing\_TypographyGetLongestLine()

```c
double OH_Drawing_TypographyGetLongestLine(OH_Drawing_Typography* typography)
```

**描述**

获取排版对象最长行的宽度，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用，建议实际使用时将返回值向上取整。当文本内容为空时，返回0.0。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回最长行的宽度，单位为物理像素px。 |

### OH\_Drawing\_TypographyGetLongestLineWithIndent()

```c
double OH_Drawing_TypographyGetLongestLineWithIndent(OH_Drawing_Typography* typography)
```

**描述**

获取排版对象最长行的宽度（该宽度包含当前行缩进的宽度），该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用，建议实际使用时将返回值向上取整。当文本内容为空时，返回0.0。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回最长行的宽度（该宽度包含当前行缩进的宽度），单位为物理像素px。 |

### OH\_Drawing\_TypographyGetMinIntrinsicWidth()

```c
double OH_Drawing_TypographyGetMinIntrinsicWidth(OH_Drawing_Typography* typography)
```

**描述**

获取排版对象的最小固有宽度，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回最小固有宽度，单位为物理像素px。 |

### OH\_Drawing\_TypographyGetMaxIntrinsicWidth()

```c
double OH_Drawing_TypographyGetMaxIntrinsicWidth(OH_Drawing_Typography* typography)
```

**描述**

获取排版对象的最大固有宽度，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回最大固有宽度，单位为物理像素px。 |

### OH\_Drawing\_TypographyGetAlphabeticBaseline()

```c
double OH_Drawing_TypographyGetAlphabeticBaseline(OH_Drawing_Typography* typography)
```

**描述**

获取排版对象的字母基线位置，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回字母文字基线，单位为物理像素px。 |

### OH\_Drawing\_TypographyGetIdeographicBaseline()

```c
double OH_Drawing_TypographyGetIdeographicBaseline(OH_Drawing_Typography* typography)
```

**描述**

获取排版对象的表意文字基线位置，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回表意文字基线，单位为物理像素px。 |

### OH\_Drawing\_TypographyHandlerAddPlaceholder()

```c
void OH_Drawing_TypographyHandlerAddPlaceholder(OH_Drawing_TypographyCreate* handler,OH_Drawing_PlaceholderSpan* span)
```

**描述**

设置占位符。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)\* handler | 指向[OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)对象的指针，由[OH\_Drawing\_CreateTypographyHandler](capi-drawing-text-typography-h.md#oh_drawing_createtypographyhandler)获取。 |
| [OH\_Drawing\_PlaceholderSpan](capi-drawing-oh-drawing-placeholderspan.md)\* span | 指向[OH\_Drawing\_PlaceholderSpan](capi-drawing-oh-drawing-placeholderspan.md)对象的指针。 |

### OH\_Drawing\_TypographyDidExceedMaxLines()

```c
bool OH_Drawing_TypographyDidExceedMaxLines(OH_Drawing_Typography* typography)
```

**描述**

获取排版对象中文本是否超过最大行，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用，如果没有通过[OH\_Drawing\_SetTypographyTextMaxLines](capi-drawing-text-typography-h.md#oh_drawing_settypographytextmaxlines)接口设置最大行，则返回false。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回文本是否超过最大行，true表示超过，false表示未超过。 |

### OH\_Drawing\_TypographyGetRectsForRange()

```c
OH_Drawing_TextBox* OH_Drawing_TypographyGetRectsForRange(OH_Drawing_Typography* typography,size_t start, size_t end, OH_Drawing_RectHeightStyle heightStyle, OH_Drawing_RectWidthStyle widthStyle)
```

**描述**

获取排版对象中指定范围内的文本框，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。不再需要[OH\_Drawing\_TextBox](capi-drawing-oh-drawing-textbox.md)时，请使用[OH\_Drawing\_TypographyDestroyTextBox](capi-drawing-text-typography-h.md#oh_drawing_typographydestroytextbox)接口释放该对象的指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| size\_t start | 开始位置，取值范围为[0, 文本长度]，按UTF-16代码单元计数。需小于end，否则返回空。 |
| size\_t end | 结束位置，取值范围为[0, 文本长度]，按UTF-16代码单元计数。超出文本长度时按文本长度处理；为0时返回空。 |
| [OH\_Drawing\_RectHeightStyle](capi-drawing-text-typography-h.md#oh_drawing_rectheightstyle) heightStyle | 设置高度样式，支持可选的高度样式具体可见[OH\_Drawing\_RectHeightStyle](capi-drawing-text-typography-h.md#oh_drawing_rectheightstyle)枚举。 |
| [OH\_Drawing\_RectWidthStyle](capi-drawing-text-typography-h.md#oh_drawing_rectwidthstyle) widthStyle | 设置宽度样式，支持可选的宽度样式具体可见[OH\_Drawing\_RectWidthStyle](capi-drawing-text-typography-h.md#oh_drawing_rectwidthstyle)枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_Drawing\_TextBox\* | 返回指定范围内的文本框，具体可见[OH\_Drawing\_TextBox](capi-drawing-oh-drawing-textbox.md)结构体。 |

### OH\_Drawing\_TypographyGetRectsForPlaceholders()

```c
OH_Drawing_TextBox* OH_Drawing_TypographyGetRectsForPlaceholders(OH_Drawing_Typography* typography)
```

**描述**

获取排版对象中占位符的文本框，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。不再需要[OH\_Drawing\_TextBox](capi-drawing-oh-drawing-textbox.md)时，请使用[OH\_Drawing\_TypographyDestroyTextBox](capi-drawing-text-typography-h.md#oh_drawing_typographydestroytextbox)接口释放该对象的指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextBox](capi-drawing-oh-drawing-textbox.md)\* | 返回占位符的文本框，返回类型为[OH\_Drawing\_TextBox](capi-drawing-oh-drawing-textbox.md)结构体。 |

### OH\_Drawing\_GetLeftFromTextBox()

```c
float OH_Drawing_GetLeftFromTextBox(OH_Drawing_TextBox* textbox, int index)
```

**描述**

获取文本框左侧位置。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextBox](capi-drawing-oh-drawing-textbox.md)\* textbox | 指向OH\_Drawing\_TextBox对象的指针，由[OH\_Drawing\_TypographyGetRectsForRange](capi-drawing-text-typography-h.md#oh_drawing_typographygetrectsforrange)或[OH\_Drawing\_TypographyGetRectsForPlaceholders](capi-drawing-text-typography-h.md#oh_drawing_typographygetrectsforplaceholders)获取。 |
| int index | 文本框的索引，取值范围为[0, 文本框数量-1]，文本框数量可通过[OH\_Drawing\_GetSizeOfTextBox](capi-drawing-text-typography-h.md#oh_drawing_getsizeoftextbox)获取。超出范围时返回0.0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回文本框左侧位置，单位为物理像素px。 |

### OH\_Drawing\_GetRightFromTextBox()

```c
float OH_Drawing_GetRightFromTextBox(OH_Drawing_TextBox* textbox, int index)
```

**描述**

获取文本框右侧位置。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextBox](capi-drawing-oh-drawing-textbox.md)\* textbox | 指向OH\_Drawing\_TextBox对象的指针，由[OH\_Drawing\_TypographyGetRectsForRange](capi-drawing-text-typography-h.md#oh_drawing_typographygetrectsforrange)或[OH\_Drawing\_TypographyGetRectsForPlaceholders](capi-drawing-text-typography-h.md#oh_drawing_typographygetrectsforplaceholders)获取。 |
| int index | 文本框的索引，取值范围为[0, 文本框数量-1]，文本框数量可通过[OH\_Drawing\_GetSizeOfTextBox](capi-drawing-text-typography-h.md#oh_drawing_getsizeoftextbox)获取。超出范围时返回0.0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回文本框右侧位置，单位为物理像素px。 |

### OH\_Drawing\_GetTopFromTextBox()

```c
float OH_Drawing_GetTopFromTextBox(OH_Drawing_TextBox* textbox, int index)
```

**描述**

获取文本框顶部位置。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextBox](capi-drawing-oh-drawing-textbox.md)\* textbox | 指向OH\_Drawing\_TextBox对象的指针，由[OH\_Drawing\_TypographyGetRectsForRange](capi-drawing-text-typography-h.md#oh_drawing_typographygetrectsforrange)或[OH\_Drawing\_TypographyGetRectsForPlaceholders](capi-drawing-text-typography-h.md#oh_drawing_typographygetrectsforplaceholders)获取。 |
| int index | 文本框的索引，取值范围为[0, 文本框数量-1]，文本框数量可通过[OH\_Drawing\_GetSizeOfTextBox](capi-drawing-text-typography-h.md#oh_drawing_getsizeoftextbox)获取。超出范围时返回0.0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回文本框顶部位置，单位为物理像素px。 |

### OH\_Drawing\_GetBottomFromTextBox()

```c
float OH_Drawing_GetBottomFromTextBox(OH_Drawing_TextBox* textbox, int index)
```

**描述**

获取文本框底部位置。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextBox](capi-drawing-oh-drawing-textbox.md)\* textbox | 指向OH\_Drawing\_TextBox对象的指针，由[OH\_Drawing\_TypographyGetRectsForRange](capi-drawing-text-typography-h.md#oh_drawing_typographygetrectsforrange)或[OH\_Drawing\_TypographyGetRectsForPlaceholders](capi-drawing-text-typography-h.md#oh_drawing_typographygetrectsforplaceholders)获取。 |
| int index | 文本框的索引，取值范围为[0, 文本框数量-1]，文本框数量可通过[OH\_Drawing\_GetSizeOfTextBox](capi-drawing-text-typography-h.md#oh_drawing_getsizeoftextbox)获取。超出范围时返回0.0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回文本框底部位置，单位为物理像素px。 |

### OH\_Drawing\_GetTextDirectionFromTextBox()

```c
int OH_Drawing_GetTextDirectionFromTextBox(OH_Drawing_TextBox* textbox, int index)
```

**描述**

获取文本框方向。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextBox](capi-drawing-oh-drawing-textbox.md)\* textbox | 指向[OH\_Drawing\_TextBox](capi-drawing-oh-drawing-textbox.md)对象的指针，由[OH\_Drawing\_TypographyGetRectsForRange](capi-drawing-text-typography-h.md#oh_drawing_typographygetrectsforrange)或[OH\_Drawing\_TypographyGetRectsForPlaceholders](capi-drawing-text-typography-h.md#oh_drawing_typographygetrectsforplaceholders)获取。 |
| int index | 文本框的索引，取值范围为[0, 文本框数量-1]，文本框数量可通过[OH\_Drawing\_GetSizeOfTextBox](capi-drawing-text-typography-h.md#oh_drawing_getsizeoftextbox)获取。超出范围时返回0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回文本框方向，1表示LTR，0表示RTL或入参异常。 |

### OH\_Drawing\_GetSizeOfTextBox()

```c
size_t OH_Drawing_GetSizeOfTextBox(OH_Drawing_TextBox* textBox)
```

**描述**

获取文本框的数量。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextBox](capi-drawing-oh-drawing-textbox.md)\* textBox | 指向OH\_Drawing\_TextBox对象的指针，由[OH\_Drawing\_TypographyGetRectsForRange](capi-drawing-text-typography-h.md#oh_drawing_typographygetrectsforrange)或[OH\_Drawing\_TypographyGetRectsForPlaceholders](capi-drawing-text-typography-h.md#oh_drawing_typographygetrectsforplaceholders)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| size\_t | 返回文本框数量大小。 |

### OH\_Drawing\_TypographyGetGlyphPositionAtCoordinate()

```c
OH_Drawing_PositionAndAffinity* OH_Drawing_TypographyGetGlyphPositionAtCoordinate(OH_Drawing_Typography* typography,double dx, double dy)
```

**描述**

获取坐标处文本的索引位置和亲和性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**废弃版本：** 18

**替代接口：** [OH\_Drawing\_TypographyGetGlyphPositionAtCoordinateWithCluster](capi-drawing-text-typography-h.md#oh_drawing_typographygetglyphpositionatcoordinatewithcluster)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| double dx | 光标的x坐标。 |
| double dy | 光标的y坐标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_PositionAndAffinity](capi-drawing-oh-drawing-positionandaffinity.md)\* | 返回坐标处字体的索引位置和亲和性，返回类型为[OH\_Drawing\_PositionAndAffinity](capi-drawing-oh-drawing-positionandaffinity.md)结构体。 |

### OH\_Drawing\_TypographyGetGlyphPositionAtCoordinateWithCluster()

```c
OH_Drawing_PositionAndAffinity* OH_Drawing_TypographyGetGlyphPositionAtCoordinateWithCluster(OH_Drawing_Typography* typography, double dx, double dy)
```

**描述**

获取坐标处文本所属字符簇的索引位置和亲和性，字符簇指一个或多个字符组成的整体。不再需要[OH\_Drawing\_PositionAndAffinity](capi-drawing-oh-drawing-positionandaffinity.md)时，请使用[OH\_Drawing\_DestroyPositionAndAffinity](capi-drawing-text-typography-h.md#oh_drawing_destroypositionandaffinity)接口释放该对象的指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| double dx | 光标的x坐标，单位为px。 |
| double dy | 光标的y坐标，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_PositionAndAffinity](capi-drawing-oh-drawing-positionandaffinity.md)\* | 返回坐标处指定类型字体的索引位置和亲和性，返回类型为[OH\_Drawing\_PositionAndAffinity](capi-drawing-oh-drawing-positionandaffinity.md)结构体。 |

### OH\_Drawing\_GetPositionFromPositionAndAffinity()

```c
size_t OH_Drawing_GetPositionFromPositionAndAffinity(OH_Drawing_PositionAndAffinity* positionAndAffinity)
```

**描述**

获取OH\_Drawing\_PositionAndAffinity对象的位置属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_PositionAndAffinity](capi-drawing-oh-drawing-positionandaffinity.md)\* positionAndAffinity | 指向OH\_Drawing\_PositionAndAffinity对象的指针，由[OH\_Drawing\_TypographyGetGlyphPositionAtCoordinateWithCluster](capi-drawing-text-typography-h.md#oh_drawing_typographygetglyphpositionatcoordinatewithcluster)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| size\_t | 返回OH\_Drawing\_PositionAndAffinity对象的位置属性。 |

### OH\_Drawing\_GetAffinityFromPositionAndAffinity()

```c
int OH_Drawing_GetAffinityFromPositionAndAffinity(OH_Drawing_PositionAndAffinity* positionAndAffinity)
```

**描述**

获取OH\_Drawing\_PositionAndAffinity对象的亲和性，根据亲和性可判断字体会靠近前方文本还是后方文本。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_PositionAndAffinity](capi-drawing-oh-drawing-positionandaffinity.md)\* positionAndAffinity | 指向OH\_Drawing\_PositionAndAffinity对象的指针，由[OH\_Drawing\_TypographyGetGlyphPositionAtCoordinateWithCluster](capi-drawing-text-typography-h.md#oh_drawing_typographygetglyphpositionatcoordinatewithcluster)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回OH\_Drawing\_PositionAndAffinity对象的亲和性，1表示亲和后方文字，0表示亲和前方文字或入参异常。 |

### OH\_Drawing\_TypographyGetWordBoundary()

```c
OH_Drawing_Range* OH_Drawing_TypographyGetWordBoundary(OH_Drawing_Typography* typography, size_t offset)
```

**描述**

获取排版对象中单词的边界。不再需要[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)时，请使用[OH\_Drawing\_ReleaseRangeBuffer](capi-drawing-text-typography-h.md#oh_drawing_releaserangebuffer)接口释放该对象的指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| size\_t offset | 单词索引，取值范围为[0, n-1]，n为文本长度。超出范围时返回默认值或抛出异常。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)\* | 返回单词边界，返回类型为[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)结构体。 |

### OH\_Drawing\_GetStartFromRange()

```c
size_t OH_Drawing_GetStartFromRange(OH_Drawing_Range* range)
```

**描述**

获取OH\_Drawing\_Range对象开始位置。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)\* range | 指向OH\_Drawing\_Range对象的指针，由[OH\_Drawing\_TypographyGetWordBoundary](capi-drawing-text-typography-h.md#oh_drawing_typographygetwordboundary)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| size\_t | 返回OH\_Drawing\_Range对象开始位置。 |

### OH\_Drawing\_GetEndFromRange()

```c
size_t OH_Drawing_GetEndFromRange(OH_Drawing_Range* range)
```

**描述**

获取OH\_Drawing\_Range对象结束位置。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)\* range | 指向OH\_Drawing\_Range对象的指针，由[OH\_Drawing\_TypographyGetWordBoundary](capi-drawing-text-typography-h.md#oh_drawing_typographygetwordboundary)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| size\_t | 返回OH\_Drawing\_Range对象结束位置。 |

### OH\_Drawing\_TypographyGetLineCount()

```c
size_t OH_Drawing_TypographyGetLineCount(OH_Drawing_Typography* typography)
```

**描述**

获取排版对象中文本行数，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| size\_t | 返回行数。 |

### OH\_Drawing\_SetTextStyleDecorationStyle()

```c
void OH_Drawing_SetTextStyleDecorationStyle(OH_Drawing_TextStyle* style, int decorationStyle)
```

**描述**

设置指定文本样式中的装饰线样式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| int decorationStyle | 设置的文本装饰样式，支持可选的装饰样式具体可见[OH\_Drawing\_TextDecorationStyle](capi-drawing-text-typography-h.md#oh_drawing_textdecorationstyle)枚举。 |

### OH\_Drawing\_SetTextStyleDecorationThicknessScale()

```c
void OH_Drawing_SetTextStyleDecorationThicknessScale(OH_Drawing_TextStyle* style, double decorationThicknessScale)
```

**描述**

设置文本装饰线的粗细缩放比例。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| double decorationThicknessScale | 粗细缩放比例。默认值为1，如果设置的粗细缩放比例小于等于0，不会绘制装饰线。 |

### OH\_Drawing\_SetTextStyleLetterSpacing()

```c
void OH_Drawing_SetTextStyleLetterSpacing(OH_Drawing_TextStyle* style, double letterSpacing)
```

**描述**

设置文本的字符间距。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| double letterSpacing | 间距大小，正值增大间距，负值减小间距，默认值为0，单位为px。 |

### OH\_Drawing\_SetTextStyleWordSpacing()

```c
void OH_Drawing_SetTextStyleWordSpacing(OH_Drawing_TextStyle* style, double wordSpacing)
```

**描述**

设置文本的单词间距。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| double wordSpacing | 间距大小，正值增大间距，负值减小间距，默认值为0，单位为px。 |

### OH\_Drawing\_SetTextStyleHalfLeading()

```c
void OH_Drawing_SetTextStyleHalfLeading(OH_Drawing_TextStyle* style, bool halfLeading)
```

**描述**

设置文本为一半行间距。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| bool halfLeading | 设置一半行间距是否生效。true表示生效，false表示不生效。 |

### OH\_Drawing\_SetTextStyleEllipsis()

```c
void OH_Drawing_SetTextStyleEllipsis(OH_Drawing_TextStyle* style, const char* ellipsis)
```

**描述**

设置文本的省略号内容。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**废弃版本：** 18

**替代接口：** [OH\_Drawing\_SetTypographyTextEllipsis](capi-drawing-text-typography-h.md#oh_drawing_settypographytextellipsis)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| const char\* ellipsis | 设置省略号内容，数据类型为指向char的指针。 |

### OH\_Drawing\_SetTextStyleEllipsisModal()

```c
void OH_Drawing_SetTextStyleEllipsisModal(OH_Drawing_TextStyle* style, int ellipsisModal)
```

**描述**

设置文本的省略号样式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**废弃版本：** 18

**替代接口：** [OH\_Drawing\_SetTypographyTextEllipsisModal](capi-drawing-text-typography-h.md#oh_drawing_settypographytextellipsismodal)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| int ellipsisModal | 设置省略号样式，可选的省略号样式具体可见[OH\_Drawing\_EllipsisModal](capi-drawing-text-typography-h.md#oh_drawing_ellipsismodal)枚举。 |

### OH\_Drawing\_SetTypographyTextBreakStrategy()

```c
void OH_Drawing_SetTypographyTextBreakStrategy(OH_Drawing_TypographyStyle* style, int breakStrategy)
```

**描述**

设置文本的中断策略。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| int breakStrategy | 设置中断策略，支持可选的中断策略具体可见[OH\_Drawing\_BreakStrategy](capi-drawing-text-typography-h.md#oh_drawing_breakstrategy)枚举。 |

### OH\_Drawing\_SetTypographyTextWordBreakType()

```c
void OH_Drawing_SetTypographyTextWordBreakType(OH_Drawing_TypographyStyle* style, int wordBreakType)
```

**描述**

设置单词的断词方式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| int wordBreakType | 设置断词方式，支持可选的断词方式样式具体可见[OH\_Drawing\_WordBreakType](capi-drawing-text-typography-h.md#oh_drawing_wordbreaktype)枚举。 |

### OH\_Drawing\_SetTypographyTextEllipsisModal()

```c
void OH_Drawing_SetTypographyTextEllipsisModal(OH_Drawing_TypographyStyle* style, int ellipsisModal)
```

**描述**

设置文本的省略模式。

该接口仅支持省略号样式为ELLIPSIS\_MODAL\_HEAD、ELLIPSIS\_MODAL\_MIDDLE、ELLIPSIS\_MODAL\_TAIL，具体可见[OH\_Drawing\_EllipsisModal](capi-drawing-text-typography-h.md#oh_drawing_ellipsismodal)枚举。

**说明** 

从API version 24开始，推荐使用[OH\_Drawing\_SetTypographyStyleAttributeInt](capi-drawing-text-typography-h.md#oh_drawing_settypographystyleattributeint)接口设置省略号样式，以支持更多省略号样式的枚举值。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向OH\_Drawing\_TypographyStyle对象的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| int ellipsisModal | 设置省略号样式，可选的省略号样式具体可见[OH\_Drawing\_EllipsisModal](capi-drawing-text-typography-h.md#oh_drawing_ellipsismodal)枚举。 |

### OH\_Drawing\_SetTypographyTextEllipsis()

```c
void OH_Drawing_SetTypographyTextEllipsis(OH_Drawing_TypographyStyle* style, const char* ellipsis)
```

**描述**

设置排版样式省略号文本。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| const char\* ellipsis | 省略号文本。 |

### OH\_Drawing\_TypographyGetLineHeight()

```c
double OH_Drawing_TypographyGetLineHeight(OH_Drawing_Typography* typography, int lineNumber)
```

**描述**

获取排版对象中指定行的行高，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| int lineNumber | 要获取行号的索引，从0开始，最大为[OH\_Drawing\_TypographyGetLineCount](capi-drawing-text-typography-h.md#oh_drawing_typographygetlinecount) - 1。超出范围时返回0.0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回指定行的行高，单位为物理像素px。 |

### OH\_Drawing\_TypographyGetLineWidth()

```c
double OH_Drawing_TypographyGetLineWidth(OH_Drawing_Typography* typography, int lineNumber)
```

**描述**

获取指定行的行宽，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| int lineNumber | 要获取行号的索引，从0开始，最大为[OH\_Drawing\_TypographyGetLineCount](capi-drawing-text-typography-h.md#oh_drawing_typographygetlinecount) - 1。超出范围时返回0.0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回指定行的行宽，单位为物理像素px。 |

### OH\_Drawing\_SetTypographyTextSplitRatio()

```c
void OH_Drawing_SetTypographyTextSplitRatio(OH_Drawing_TypographyStyle* style, float textSplitRatio)
```

**描述**

设置文本划分比率，用于点击定位字符时，确定光标在一个字形内的归属位置。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| float textSplitRatio | 文本划分比率，取值范围为[0, 1]，默认值为0.5。用于点击坐标映射到字符位置时，在一个字形内决定归到当前字符还是下一字符的划分阈值；值越大越偏向当前字符，值越小越偏向下一字符。 |

### OH\_Drawing\_TypographyIsLineUnlimited()

```c
bool OH_Drawing_TypographyIsLineUnlimited(OH_Drawing_TypographyStyle* style)
```

**描述**

获取文本是否有最大行数限制。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向文本风格[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回文本是否有最大行数限制，true表示无最大行数限制，false表示有最大行数限制。 |

### OH\_Drawing\_TypographyIsEllipsized()

```c
bool OH_Drawing_TypographyIsEllipsized(OH_Drawing_TypographyStyle* style)
```

**描述**

获取指定排版样式是否配置省略号。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回指定排版样式是否配置省略号，true表示已配置省略号，false表示没有配置省略号。 |

### OH\_Drawing\_SetTypographyTextLocale()

```c
void OH_Drawing_SetTypographyTextLocale(OH_Drawing_TypographyStyle* style, const char* locale)
```

**描述**

设置指定排版样式的语言环境。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| const char\* locale | 语言环境，数据类型为指向char的指针。格式参考BCP 47语言标签标准，如'en'代表英文，'zh-Hans'代表简体中文，'zh-Hant'代表繁体中文。未指定时默认locale为'zh-Hans'。 |

### OH\_Drawing\_TextStyleGetFontMetrics()

```c
bool OH_Drawing_TextStyleGetFontMetrics(OH_Drawing_Typography* typography,OH_Drawing_TextStyle* style, OH_Drawing_Font_Metrics* fontmetrics)
```

**描述**

获取文本字体属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向文本对象[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| [OH\_Drawing\_Font\_Metrics](capi-drawing-oh-drawing-font-metrics.md)\* fontmetrics | 指向字体属性对象[OH\_Drawing\_Font\_Metrics](capi-drawing-oh-drawing-font-metrics.md)的指针，由[OH\_Drawing\_Font\_Metrics](capi-drawing-oh-drawing-font-metrics.md)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 是否获取到字体属性。true表示获取到字体属性，false表示未获取到字体属性。 |

### OH\_Drawing\_SetTypographyTextStyle()

```c
void OH_Drawing_SetTypographyTextStyle(OH_Drawing_TypographyStyle* handler, OH_Drawing_TextStyle* style)
```

**描述**

设置排版样式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* handler | 指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

### OH\_Drawing\_CreateFontDescriptor()

```c
OH_Drawing_FontDescriptor* OH_Drawing_CreateFontDescriptor(void)
```

**描述**

构造字体描述对象，用于描述系统字体详细信息。不再需要[OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)时，请使用[OH\_Drawing\_DestroyFontDescriptor](capi-drawing-text-typography-h.md#oh_drawing_destroyfontdescriptor)接口释放该对象的指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)\* | 返回指向已创建的字体描述对象[OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)的指针。 |

### OH\_Drawing\_DestroyFontDescriptor()

```c
void OH_Drawing_DestroyFontDescriptor(OH_Drawing_FontDescriptor* descriptor)
```

**描述**

释放字体描述对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)\* descriptor | 指向字体描述对象[OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)的指针，由[OH\_Drawing\_CreateFontDescriptor](capi-drawing-text-typography-h.md#oh_drawing_createfontdescriptor)获取。 |

### OH\_Drawing\_CreateFontParser()

```c
OH_Drawing_FontParser* OH_Drawing_CreateFontParser(void)
```

**描述**

构造字体解析对象，用于解析系统字体。不再需要[OH\_Drawing\_FontParser](capi-drawing-oh-drawing-fontparser.md)时，请使用[OH\_Drawing\_DestroyFontParser](capi-drawing-text-typography-h.md#oh_drawing_destroyfontparser)接口释放该对象的指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontParser](capi-drawing-oh-drawing-fontparser.md)\* | 返回指向已创建的字体解析对象[OH\_Drawing\_FontParser](capi-drawing-oh-drawing-fontparser.md)的指针。 |

### OH\_Drawing\_DestroyFontParser()

```c
void OH_Drawing_DestroyFontParser(OH_Drawing_FontParser* parser)
```

**描述**

释放字体解析对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontParser](capi-drawing-oh-drawing-fontparser.md)\* parser | 指向字体解析对象[OH\_Drawing\_FontParser](capi-drawing-oh-drawing-fontparser.md)的指针，由[OH\_Drawing\_CreateFontParser](capi-drawing-text-typography-h.md#oh_drawing_createfontparser)获取。 |

### OH\_Drawing\_FontParserGetSystemFontList()

```c
char** OH_Drawing_FontParserGetSystemFontList(OH_Drawing_FontParser* fontParser, size_t* num)
```

**描述**

获取系统字体名称列表。不再需要该列表时，请使用[OH\_Drawing\_DestroySystemFontList](capi-drawing-text-typography-h.md#oh_drawing_destroysystemfontlist)释放内存。此接口仅在Phone、PC/2in1设备上支持。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontParser](capi-drawing-oh-drawing-fontparser.md)\* fontParser | 指向字体解析对象[OH\_Drawing\_FontParser](capi-drawing-oh-drawing-fontparser.md)的指针，由[OH\_Drawing\_CreateFontParser](capi-drawing-text-typography-h.md#oh_drawing_createfontparser)获取。 |
| size\_t\* num | 返回获取到的系统字体名称数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| char\*\* | 返回获取到的系统字体列表。 |

### OH\_Drawing\_DestroySystemFontList()

```c
void OH_Drawing_DestroySystemFontList(char** fontList, size_t num)
```

**描述**

释放系统字体名称列表占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\*\* fontList | 指向系统字体名称列表的指针。 |
| size\_t num | 系统字体名称列表的数量。 |

### OH\_Drawing\_FontParserGetFontByName()

```c
OH_Drawing_FontDescriptor* OH_Drawing_FontParserGetFontByName(OH_Drawing_FontParser* fontParser, const char* name)
```

**描述**

根据传入的系统字体名称获取系统字体的相关信息。此接口仅在Phone、PC/2in1设备上支持。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontParser](capi-drawing-oh-drawing-fontparser.md)\* fontParser | 指向字体解析对象[OH\_Drawing\_FontParser](capi-drawing-oh-drawing-fontparser.md)的指针，由[OH\_Drawing\_CreateFontParser](capi-drawing-text-typography-h.md#oh_drawing_createfontparser)获取。 |
| const char\* name | 系统字体名，有效的系统字体名称可通过[OH\_Drawing\_FontParserGetSystemFontList](capi-drawing-text-typography-h.md#oh_drawing_fontparsergetsystemfontlist)接口获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_Drawing\_FontDescriptor\* | 返回系统字体描述对象，不再需要时，请使用[OH\_Drawing\_DestroyFontDescriptor](capi-drawing-text-typography-h.md#oh_drawing_destroyfontdescriptor)释放该对象指针。 |

### OH\_Drawing\_TypographyGetLineMetrics()

```c
OH_Drawing_LineMetrics* OH_Drawing_TypographyGetLineMetrics(OH_Drawing_Typography* typography)
```

**描述**

获取排版对象的行位置信息，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。不再需要[OH\_Drawing\_LineMetrics](capi-drawing-oh-drawing-linemetrics.md)时，请使用[OH\_Drawing\_DestroyLineMetrics](capi-drawing-text-typography-h.md#oh_drawing_destroylinemetrics)接口释放该对象的指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向文本对象[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_LineMetrics](capi-drawing-oh-drawing-linemetrics.md)\* | 返回指向行位置信息对象[OH\_Drawing\_LineMetrics](capi-drawing-oh-drawing-linemetrics.md)的指针。 |

### OH\_Drawing\_LineMetricsGetSize()

```c
size_t OH_Drawing_LineMetricsGetSize(OH_Drawing_LineMetrics* lineMetrics)
```

**描述**

获取行数量。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_LineMetrics](capi-drawing-oh-drawing-linemetrics.md)\* lineMetrics | 指向行位置信息对象[OH\_Drawing\_LineMetrics](capi-drawing-oh-drawing-linemetrics.md)的指针，由[OH\_Drawing\_LineMetrics](capi-drawing-oh-drawing-linemetrics.md)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| size\_t | 返回行数量。 |

### OH\_Drawing\_DestroyLineMetrics()

```c
void OH_Drawing_DestroyLineMetrics(OH_Drawing_LineMetrics* lineMetrics)
```

**描述**

释放行位置信息对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_LineMetrics](capi-drawing-oh-drawing-linemetrics.md)\* lineMetrics | 指向行位置信息对象[OH\_Drawing\_LineMetrics](capi-drawing-oh-drawing-linemetrics.md)的指针，由[OH\_Drawing\_LineMetrics](capi-drawing-oh-drawing-linemetrics.md)获取。 |

### OH\_Drawing\_TypographyGetLineMetricsAt()

```c
bool OH_Drawing_TypographyGetLineMetricsAt(OH_Drawing_Typography* typography, int lineNumber, OH_Drawing_LineMetrics* lineMetric)
```

**描述**

获取排版对象的指定行位置信息，具体参见[OH\_Drawing\_LineMetrics](capi-drawing-oh-drawing-linemetrics.md)结构体，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向文本对象[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| int lineNumber | 要获取行号的索引，从0开始，最大为[OH\_Drawing\_TypographyGetLineCount](capi-drawing-text-typography-h.md#oh_drawing_typographygetlinecount) - 1。超出范围时返回false。 |
| [OH\_Drawing\_LineMetrics](capi-drawing-oh-drawing-linemetrics.md)\* lineMetric | 指向行位置信息对象[OH\_Drawing\_LineMetrics](capi-drawing-oh-drawing-linemetrics.md)的指针，作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 行位置信息对象是否成功获取。true表示成功获取，false表示未成功获取。 |

### OH\_Drawing\_TypographyGetLineInfo()

```c
bool OH_Drawing_TypographyGetLineInfo(OH_Drawing_Typography* typography, int lineNumber, bool oneLine,bool includeWhitespace, OH_Drawing_LineMetrics* drawingLineMetrics)
```

**描述**

获取排版对象中指定行的位置信息或指定行第一个字符的位置信息，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向文本对象[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| int lineNumber | 要获取行号的索引，从0开始，最大为[OH\_Drawing\_TypographyGetLineCount](capi-drawing-text-typography-h.md#oh_drawing_typographygetlinecount) - 1。超出范围时返回false。 |
| bool oneLine | true为获取整行的位置信息，false为获取第一个字符的位置信息。 |
| bool includeWhitespace | 文字宽度是否包含空白符。true表示包含空白符，false表示不包含空白符。 |
| [OH\_Drawing\_LineMetrics](capi-drawing-oh-drawing-linemetrics.md)\* drawingLineMetrics | 指向行位置信息对象[OH\_Drawing\_LineMetrics](capi-drawing-oh-drawing-linemetrics.md)的指针，由[OH\_Drawing\_LineMetrics](capi-drawing-oh-drawing-linemetrics.md)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 指定行的行位置信息或第一个字符的位置信息是否成功获取，true表示成功获取，false表示未成功获取。 |

### OH\_Drawing\_SetTypographyTextFontWeight()

```c
void OH_Drawing_SetTypographyTextFontWeight(OH_Drawing_TypographyStyle* style, int weight)
```

**描述**

设置排版样式默认字重。在HarmonyOS 6.1.1之前，仅系统字体中的可变字体支持字重调节；从HarmonyOS 6.1.1开始，系统字体与三方注册字体中的可变字体均支持字重调节。非可变字体设置字重值小于semi-bold时字体粗细无变化，设置字重值大于等于semi-bold时可能会触发伪加粗效果。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| int weight | 设置字重，设置0字重为thin，设置1字重为extra-light，设置2字重为light，设置4字重为medium，设置5字重为semi-bold，  设置6字重为bold，设置7字重为extra-bold，设置8字重为black，设置3或其它字重为normal/regular，具体可见[OH\_Drawing\_FontWeight](capi-drawing-text-typography-h.md#oh_drawing_fontweight)枚举。 |

### OH\_Drawing\_SetTypographyTextFontStyle()

```c
void OH_Drawing_SetTypographyTextFontStyle(OH_Drawing_TypographyStyle* style, int fontStyle)
```

**描述**

设置排版样式默认的字体样式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| int fontStyle | 设置字体样式，设置1为斜体，设置0或其它为非斜体，具体可见[OH\_Drawing\_FontStyle](capi-drawing-text-typography-h.md#oh_drawing_fontstyle)枚举。 |

### OH\_Drawing\_SetTypographyTextFontFamily()

```c
void OH_Drawing_SetTypographyTextFontFamily(OH_Drawing_TypographyStyle* style, const char* fontFamily)
```

**描述**

设置字体家族的名称。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| const char\* fontFamily | 字体家族的名称，数据类型为指向char的指针。 |

### OH\_Drawing\_SetTypographyTextFontSize()

```c
void OH_Drawing_SetTypographyTextFontSize(OH_Drawing_TypographyStyle* style, double fontSize)
```

**描述**

设置文本排版字号。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| double fontSize | 字号（大于0），单位为px。 |

### OH\_Drawing\_SetTypographyTextFontHeight()

```c
void OH_Drawing_SetTypographyTextFontHeight(OH_Drawing_TypographyStyle* style, double fontHeight)
```

**描述**

设置文本排版字体高度，按当前字体大小的倍数进行设置。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| double fontHeight | 字体高度, 当前字体大小的倍数。取值小于0时按0处理。 |

### OH\_Drawing\_SetTypographyTextHalfLeading()

```c
void OH_Drawing_SetTypographyTextHalfLeading(OH_Drawing_TypographyStyle* style, bool halfLeading)
```

**描述**

设置文本排版是否为一半行间距。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| bool halfLeading | 设置一半行间距是否生效，true表示生效，false表示不生效。 |

### OH\_Drawing\_SetTypographyTextUseLineStyle()

```c
void OH_Drawing_SetTypographyTextUseLineStyle(OH_Drawing_TypographyStyle* style, bool useLineStyle)
```

**描述**

设置文本排版是否启用行样式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| bool useLineStyle | 设置行样式是否启用，true表示启用，false表示不启用。 |

### OH\_Drawing\_SetTypographyTextLineStyleFontWeight()

```c
void OH_Drawing_SetTypographyTextLineStyleFontWeight(OH_Drawing_TypographyStyle* style, int weight)
```

**描述**

设置排版样式中支柱样式的文本样式字重。在HarmonyOS 6.1.1之前，仅系统字体中的可变字体支持字重调节；从HarmonyOS 6.1.1开始，系统字体与三方注册字体中的可变字体均支持字重调节。非可变字体设置字重值小于semi-bold时字体粗细无变化，设置字重值大于等于semi-bold时可能会触发伪加粗效果。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| int weight | 设置字重，设置0字重为thin，设置1字重为extra-light，设置2字重为light，设置4字重为medium，设置5字重为semi-bold，设置6字重为bold，设置7字重为extra-bold，设置8字重为black，设置3或其它字重为normal/regular，具体可见[OH\_Drawing\_FontWeight](capi-drawing-text-typography-h.md#oh_drawing_fontweight)枚举。 |

### OH\_Drawing\_SetTypographyTextLineStyleFontStyle()

```c
void OH_Drawing_SetTypographyTextLineStyleFontStyle(OH_Drawing_TypographyStyle* style, int fontStyle)
```

**描述**

设置文本排版样式中支柱样式的字体样式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| int fontStyle | 设置字体样式，设置1为斜体，设置0或其它为非斜体，具体可见[OH\_Drawing\_FontStyle](capi-drawing-text-typography-h.md#oh_drawing_fontstyle)枚举。 |

### OH\_Drawing\_SetTypographyTextLineStyleFontFamilies()

```c
void OH_Drawing_SetTypographyTextLineStyleFontFamilies(OH_Drawing_TypographyStyle* style, int fontFamiliesNumber, const char* fontFamilies[])
```

**描述**

设置文本排版行样式字体家族。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| int fontFamiliesNumber | 字体名称数量，禁止填入负数。 |
| fontFamilies | 指向字体家族类型数组的指针。 |

### OH\_Drawing\_SetTypographyTextLineStyleFontSize()

```c
void OH_Drawing_SetTypographyTextLineStyleFontSize(OH_Drawing_TypographyStyle* style, double lineStyleFontSize)
```

**描述**

设置文本排版行样式字号。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| double lineStyleFontSize | 字号（大于0），单位为物理像素px。 |

### OH\_Drawing\_SetTypographyTextLineStyleFontHeight()

```c
void OH_Drawing_SetTypographyTextLineStyleFontHeight(OH_Drawing_TypographyStyle* style, double lineStyleFontHeight)
```

**描述**

设置文本排版行样式字体高度，按当前字体大小的倍数进行设置。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| double lineStyleFontHeight | 字体高度，取值应大于0。 |

### OH\_Drawing\_SetTypographyTextLineStyleHalfLeading()

```c
void OH_Drawing_SetTypographyTextLineStyleHalfLeading(OH_Drawing_TypographyStyle* style, bool lineStyleHalfLeading)
```

**描述**

设置文本排版行样式是否为一半行间距。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| bool lineStyleHalfLeading | 设置一半行间距是否生效。true表示生效，false表示不生效。 |

### OH\_Drawing\_SetTypographyTextLineStyleSpacingScale()

```c
void OH_Drawing_SetTypographyTextLineStyleSpacingScale(OH_Drawing_TypographyStyle* style, double spacingScale)
```

**描述**

设置文本排版行样式间距比例。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| double spacingScale | 行样式间距比例，用于缩放行间距，值大于1.0增大行间距，值小于1.0减小行间距,1.0表示原始间距。 |

### OH\_Drawing\_SetTypographyTextLineStyleOnly()

```c
void OH_Drawing_SetTypographyTextLineStyleOnly(OH_Drawing_TypographyStyle* style, bool lineStyleOnly)
```

**描述**

设置文本排版是否仅启用行样式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| bool lineStyleOnly | 设置仅启用行样式是否生效。true表示生效，false表示不生效。 |

### OH\_Drawing\_CreateTextShadow()

```c
OH_Drawing_TextShadow* OH_Drawing_CreateTextShadow(void)
```

**描述**

创建指向文本阴影对象的指针。不再需要[OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)时，请使用[OH\_Drawing\_DestroyTextShadow](capi-drawing-text-typography-h.md#oh_drawing_destroytextshadow)接口释放该对象的指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)\* | 指向创建的文本阴影对象。 |

### OH\_Drawing\_DestroyTextShadow()

```c
void OH_Drawing_DestroyTextShadow(OH_Drawing_TextShadow* shadow)
```

**描述**

释放被文本阴影对象占据的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)\* shadow | 指向文本阴影对象[OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)的指针，由[OH\_Drawing\_CreateTextShadow](capi-drawing-text-typography-h.md#oh_drawing_createtextshadow)获取。 |

### OH\_Drawing\_TextStyleGetShadows()

```c
OH_Drawing_TextShadow* OH_Drawing_TextStyleGetShadows(OH_Drawing_TextStyle* style)
```

**描述**

获取文本阴影容器。不再需要[OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)时，请使用[OH\_Drawing\_DestroyTextShadows](capi-drawing-text-typography-h.md#oh_drawing_destroytextshadows)接口释放该对象的指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)\* | 返回指向文本阴影容器[OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)的指针。 |

### OH\_Drawing\_TextStyleGetShadowCount()

```c
int OH_Drawing_TextStyleGetShadowCount(OH_Drawing_TextStyle* style)
```

**描述**

获取文本阴影容器的大小。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回文本阴影容器的大小。 |

### OH\_Drawing\_TextStyleAddShadow()

```c
void OH_Drawing_TextStyleAddShadow(OH_Drawing_TextStyle* style, const OH_Drawing_TextShadow* shadow)
```

**描述**

文本阴影容器中添加文本阴影元素。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| const [OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)\* shadow | 指向文本阴影对象[OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)的指针，由[OH\_Drawing\_CreateTextShadow](capi-drawing-text-typography-h.md#oh_drawing_createtextshadow)获取。 |

### OH\_Drawing\_TextStyleClearShadows()

```c
void OH_Drawing_TextStyleClearShadows(OH_Drawing_TextStyle* style)
```

**描述**

清除文本阴影容器中的所有元素。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

### OH\_Drawing\_TextStyleGetShadowWithIndex()

```c
OH_Drawing_TextShadow* OH_Drawing_TextStyleGetShadowWithIndex(OH_Drawing_TextStyle* style, int index)
```

**描述**

根据下标获取文本阴影容器中的元素。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| int index | 下标索引，取值范围为[0, 阴影数量-1]，阴影数量可通过[OH\_Drawing\_TextStyleGetShadowCount](capi-drawing-text-typography-h.md#oh_drawing_textstylegetshadowcount)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)\* | 返回指向文本阴影对象[OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)的指针。 |

### OH\_Drawing\_TypographySetIndents()

```c
void OH_Drawing_TypographySetIndents(OH_Drawing_Typography* typography, int indentsNumber, const float indents[])
```

**描述**

设置文本的排版缩进，不调用此接口默认文本无缩进。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向排版对象[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| int indentsNumber | 为段落设置的缩进数量。该值应小于或等于 indents 数组的长度，以避免访问数组越界导致的显示异常。 |
| indents | 指向浮点类型数组的指针，每个数组元素表示一个缩进宽度，单位为物理像素（px）。在应用[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)接口时，需要先声明并初始化该浮点数组。 |

### OH\_Drawing\_TypographyGetIndentsWithIndex()

```c
float OH_Drawing_TypographyGetIndentsWithIndex(OH_Drawing_Typography* typography, int index)
```

**描述**

根据行索引获取排版对象缩进容器中的元素，行索引从0开始。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向文本对象[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| int index | 缩进值的下标索引。index小于0时返回0.0。index大于等于缩进值数量时返回最后一个缩进值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回索引对应的元素值。 |

### OH\_Drawing\_TypographyGetLineTextRange()

```c
OH_Drawing_Range* OH_Drawing_TypographyGetLineTextRange(OH_Drawing_Typography* typography, int lineNumber, bool includeSpaces)
```

**描述**

获取排版对象中行的边界，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用。该接口只能获取已有行的边界，即输入行索引从0开始，最大行索引为[OH\_Drawing\_TypographyGetLineCount](capi-drawing-text-typography-h.md#oh_drawing_typographygetlinecount) - 1。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向文本对象[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| int lineNumber | 行索引 |
| bool includeSpaces | 设置返回的边界是否包含空格，true为包含空格，false为不包含空格。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)\* | 返回指向行边界对象的指针[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)。如果输入的行索引是非法的行索引，则返回的边界范围的start和end都为0。 |

### OH\_Drawing\_DestroyTextShadows()

```c
void OH_Drawing_DestroyTextShadows(OH_Drawing_TextShadow* shadow)
```

**描述**

释放由被文本阴影对象OH\_Drawing\_TextShadow构成的vector占据的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)\* shadow | 指向文本阴影对象[OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)的指针，由[OH\_Drawing\_CreateTextShadow](capi-drawing-text-typography-h.md#oh_drawing_createtextshadow)获取。 |

### OH\_Drawing\_GetSystemFontConfigInfo()

```c
OH_Drawing_FontConfigInfo* OH_Drawing_GetSystemFontConfigInfo(OH_Drawing_FontConfigInfoErrorCode* errorCode)
```

**描述**

获取系统字体配置信息。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontConfigInfoErrorCode](capi-drawing-text-typography-h.md#oh_drawing_fontconfiginfoerrorcode)\* errorCode | 错误码，具体可见[OH\_Drawing\_FontConfigInfoErrorCode](capi-drawing-text-typography-h.md#oh_drawing_fontconfiginfoerrorcode)枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontConfigInfo](capi-drawing-oh-drawing-fontconfiginfo.md)\* | 返回系统字体配置信息的指针，不再需要时，请使用[OH\_Drawing\_DestroySystemFontConfigInfo](capi-drawing-text-typography-h.md#oh_drawing_destroysystemfontconfiginfo)释放该对象指针。 |

### OH\_Drawing\_DestroySystemFontConfigInfo()

```c
void OH_Drawing_DestroySystemFontConfigInfo(OH_Drawing_FontConfigInfo* drawFontCfgInfo)
```

**描述**

释放系统字体配置信息占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontConfigInfo](capi-drawing-oh-drawing-fontconfiginfo.md)\* drawFontCfgInfo | 指向系统字体配置信息[OH\_Drawing\_FontConfigInfo](capi-drawing-oh-drawing-fontconfiginfo.md)的指针，由[OH\_Drawing\_GetSystemFontConfigInfo](capi-drawing-text-typography-h.md#oh_drawing_getsystemfontconfiginfo)获取。 |

### OH\_Drawing\_SetTextStyleFontStyleStruct()

```c
void OH_Drawing_SetTextStyleFontStyleStruct(OH_Drawing_TextStyle* drawingTextStyle,OH_Drawing_FontStyleStruct fontStyle)
```

**描述**

设置文本样式中的字体样式，包括字体字重、字体宽度和字体斜度。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* drawingTextStyle | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| [OH\_Drawing\_FontStyleStruct](capi-drawing-oh-drawing-fontstylestruct.md) fontStyle | 字体样式对象，包括字体字重、字体宽度和字体斜度信息。 |

### OH\_Drawing\_SetTextStyleBadgeType()

```c
void OH_Drawing_SetTextStyleBadgeType(OH_Drawing_TextStyle* style, OH_Drawing_TextBadgeType textBadgeType)
```

**描述**

设置文本排版时是否启用上标或下标。未调用此接口时，默认不启用。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 表示指向[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| [OH\_Drawing\_TextBadgeType](capi-drawing-text-typography-h.md#oh_drawing_textbadgetype) textBadgeType | 设置文本排版时是否启用上标或下标。TEXT\_SUPERSCRIPT表示启用上标，TEXT\_SUBSCRIPT表示启用下标，默认值为TEXT\_BADGE\_NONE表示不启用。 |

### OH\_Drawing\_TextStyleGetFontStyleStruct()

```c
OH_Drawing_FontStyleStruct OH_Drawing_TextStyleGetFontStyleStruct(OH_Drawing_TextStyle* drawingTextStyle)
```

**描述**

获取文本样式中的字体样式，包括字体字重、字体宽度和字体斜度。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* drawingTextStyle | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontStyleStruct](capi-drawing-oh-drawing-fontstylestruct.md) | 返回获取到的字体样式对象。 |

### OH\_Drawing\_SetTypographyStyleFontStyleStruct()

```c
void OH_Drawing_SetTypographyStyleFontStyleStruct(OH_Drawing_TypographyStyle* drawingStyle,OH_Drawing_FontStyleStruct fontStyle)
```

**描述**

设置排版样式中默认文本样式的字体样式，包括字体字重、字体宽度和字体斜度。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* drawingStyle | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| [OH\_Drawing\_FontStyleStruct](capi-drawing-oh-drawing-fontstylestruct.md) fontStyle | 字体样式对象，包括字体字重、字体宽度和字体斜度信息。 |

### OH\_Drawing\_TypographyStyleGetFontStyleStruct()

```c
OH_Drawing_FontStyleStruct OH_Drawing_TypographyStyleGetFontStyleStruct(OH_Drawing_TypographyStyle* drawingStyle)
```

**描述**

获取排版样式中默认文本样式的字体样式，包括字体字重、字体宽度和字体斜度。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* drawingStyle | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontStyleStruct](capi-drawing-oh-drawing-fontstylestruct.md) | 返回获取到的字体样式对象，包括字体字重、字体宽度和字体斜度信息。 |

### OH\_Drawing\_TextStyleSetBackgroundRect()

```c
void OH_Drawing_TextStyleSetBackgroundRect(OH_Drawing_TextStyle* style,const OH_Drawing_RectStyle_Info* rectStyleInfo, int styleId)
```

**描述**

设置文本背景矩形框和样式id。样式id仅当背景框为圆角矩形时有效。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| const [OH\_Drawing\_RectStyle\_Info](capi-drawing-oh-drawing-rectstyle-info.md)\* rectStyleInfo | 指向[OH\_Drawing\_RectStyle\_Info](capi-drawing-oh-drawing-rectstyle-info.md)对象的指针。 |
| int styleId | 要设置的样式id，仅当背景框为圆角矩形时有效。文本处理时会被划分为多个分段，每个分段都有自己的TextStyle，id标识着这个分段将被绘制于第几个背景矩形框中。  若一行中每个分段的id全为0，表示所有分段绘制在同一个圆角矩形背景框中；若一行中的id为0, 1，则id为0的分段绘制在一个圆角矩形背景框内，id为1的分段绘制在另一个圆角矩形背景框内，以此类推。 |

### OH\_Drawing\_TypographyHandlerAddSymbol()

```c
void OH_Drawing_TypographyHandlerAddSymbol(OH_Drawing_TypographyCreate* handler, uint32_t symbol)
```

**描述**

设置排版创建过程中的符号。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)\* handler | 指向[OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)对象的指针，由[OH\_Drawing\_CreateTypographyHandler](capi-drawing-text-typography-h.md#oh_drawing_createtypographyhandler)获取。 |
| uint32\_t symbol | 设置的symbol码位值，详见[主题图标库](https://developer.huawei.com/consumer/cn/design/harmonyos-symbol/)列表视图下的unicode值。 |

### OH\_Drawing\_TextStyleAddFontFeature()

```c
void OH_Drawing_TextStyleAddFontFeature(OH_Drawing_TextStyle* style, const char* tag, int value)
```

**描述**

设置文本样式中指定字体特征是否启用。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| const char\* tag | 指向字体特征键值对中关键字所标识的字符串。 |
| int value | 要设置的字体特征键值对的值。 |

### OH\_Drawing\_TextStyleAddFontVariation()

```c
void OH_Drawing_TextStyleAddFontVariation(OH_Drawing_TextStyle* style, const char* axis, const float value)
```

**描述**

添加可变字体属性。对应的字体文件（.ttf文件）需要支持可变调节，此接口才能生效。当对应的字体不支持可变调节时，此接口调用不生效。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| const char\* axis | 可变字体属性键值对中的键。目前仅支持'wght'，表示字重属性。 |
| const float value | 设置的可变字体属性键值对的值。目前默认字体下字重属性支持的取值范围为[0,900]。 |

### OH\_Drawing\_TextStyleGetFontFeatures()

```c
OH_Drawing_FontFeature* OH_Drawing_TextStyleGetFontFeatures(OH_Drawing_TextStyle* style)
```

**描述**

获取指定文本样式的字体特征map容器中所有内容。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontFeature](capi-drawing-oh-drawing-fontfeature.md)\* | 要获取的字体特征容器的所有内容，指向存放容器所有键值对的一个结构体数组。 |

### OH\_Drawing\_TextStyleDestroyFontFeatures()

```c
void OH_Drawing_TextStyleDestroyFontFeatures(OH_Drawing_FontFeature* fontFeature, size_t fontFeatureSize)
```

**描述**

释放存放字体特征所有内容的结构体数组所占用的空间。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontFeature](capi-drawing-oh-drawing-fontfeature.md)\* fontFeature | 指向存放容器所有键值对的结构体数组指针，由[OH\_Drawing\_TextStyleGetFontFeatures](capi-drawing-text-typography-h.md#oh_drawing_textstylegetfontfeatures)获取。 |
| size\_t fontFeatureSize | 存放容器所有键值对的结构体数组的大小。 |

### OH\_Drawing\_TextStyleGetFontFeatureSize()

```c
size_t OH_Drawing_TextStyleGetFontFeatureSize(OH_Drawing_TextStyle* style)
```

**描述**

获取指定文本样式中字体特征map容器的大小。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| size\_t | 字体特征map容器的大小。 |

### OH\_Drawing\_TextStyleClearFontFeature()

```c
void OH_Drawing_TextStyleClearFontFeature(OH_Drawing_TextStyle* style)
```

**描述**

清除指定文本样式的字体特征map容器中所有内容。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

### OH\_Drawing\_TextStyleGetBaselineShift()

```c
double OH_Drawing_TextStyleGetBaselineShift(OH_Drawing_TextStyle* style)
```

**描述**

获取指定文本样式的基线偏移。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 基线偏移的值，单位为物理像素px。 |

### OH\_Drawing\_TextStyleSetBaselineShift()

```c
void OH_Drawing_TextStyleSetBaselineShift(OH_Drawing_TextStyle* style, double lineShift)
```

**描述**

设置文本样式基线偏移。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| double lineShift | 文本的基线偏移量，正值向上偏移，负值向下偏移，单位为px。 |

### OH\_Drawing\_TypographyTextSetHeightBehavior()

```c
void OH_Drawing_TypographyTextSetHeightBehavior(OH_Drawing_TypographyStyle* style,OH_Drawing_TextHeightBehavior heightMode)
```

**描述**

设置文本高度修饰符模式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| [OH\_Drawing\_TextHeightBehavior](capi-drawing-text-typography-h.md#oh_drawing_textheightbehavior) heightMode | 文本高度修饰符模式，为[OH\_Drawing\_TextHeightBehavior](capi-drawing-text-typography-h.md#oh_drawing_textheightbehavior)类型的枚举值。 |

### OH\_Drawing\_TypographyTextGetHeightBehavior()

```c
OH_Drawing_TextHeightBehavior OH_Drawing_TypographyTextGetHeightBehavior(OH_Drawing_TypographyStyle* style)
```

**描述**

获取文本高度修饰符模式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextHeightBehavior](capi-drawing-text-typography-h.md#oh_drawing_textheightbehavior) | 返回文本高度修饰符模式，为[OH\_Drawing\_TextHeightBehavior](capi-drawing-text-typography-h.md#oh_drawing_textheightbehavior)类型的枚举值。 |

### OH\_Drawing\_TypographyGetLineFontMetrics()

```c
OH_Drawing_Font_Metrics* OH_Drawing_TypographyGetLineFontMetrics(OH_Drawing_Typography* typography,size_t lineNumber, size_t* fontMetricsSize)
```

**描述**

从排版对象中目标行获取所有字体度量信息，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用之后调用，否则会返回空指针。不再需要[OH\_Drawing\_Font\_Metrics](capi-drawing-oh-drawing-font-metrics.md)时，请使用[OH\_Drawing\_TypographyDestroyLineFontMetrics](capi-drawing-text-typography-h.md#oh_drawing_typographydestroylinefontmetrics)接口释放该对象的指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向文本对象[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| size\_t lineNumber | 指定行数，取值为整数，最小有效值为1，最大行取决于文本输入后字体引擎解析出来的行数，若输入值大于最大行会返回错误值并打印错误消息。 |
| size\_t\* fontMetricsSize | 指示从当前行返回的字体度量结构的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Font\_Metrics](capi-drawing-oh-drawing-font-metrics.md)\* | 返回当前行的所有字体度量信息。 |

### OH\_Drawing\_TypographyDestroyLineFontMetrics()

```c
void OH_Drawing_TypographyDestroyLineFontMetrics(OH_Drawing_Font_Metrics* lineFontMetric)
```

**描述**

释放指定行所有字体度量结构体集合所占用的所有空间。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Font\_Metrics](capi-drawing-oh-drawing-font-metrics.md)\* lineFontMetric | 指示要释放空间的指定行所有字体度量结构体集合的第一个地址。 |

### OH\_Drawing\_TextStyleIsEqual()

```c
bool OH_Drawing_TextStyleIsEqual(const OH_Drawing_TextStyle* style, const OH_Drawing_TextStyle* comparedStyle)
```

**描述**

判断两个文本样式对象是否相等，字宽属性不参与对比。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 比较的文本样式对象。 |
| const [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* comparedStyle | 比较的文本样式对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回两个文本样式对象是否相等。true表示相等，false表示不相等。 |

### OH\_Drawing\_TextStyleIsEqualByFont()

```c
bool OH_Drawing_TextStyleIsEqualByFont(const OH_Drawing_TextStyle* style, const OH_Drawing_TextStyle* comparedStyle)
```

**描述**

判断两个文本样式对象的字体样式属性是否相等。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 比较的文本样式对象。 |
| const [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* comparedStyle | 比较的文本样式对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回两个文本样式对象的字体样式属性是否相等的结果。true表示字体样式属性相等，false表示不相等。 |

### OH\_Drawing\_TextStyleIsAttributeMatched()

```c
bool OH_Drawing_TextStyleIsAttributeMatched(const OH_Drawing_TextStyle* style,const OH_Drawing_TextStyle* comparedStyle, OH_Drawing_TextStyleType textStyleType)
```

**描述**

判断两个文本样式对象是否有一样的字体样式类型。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 比较的文本样式对象。 |
| const [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* comparedStyle | 比较的文本样式对象。 |
| [OH\_Drawing\_TextStyleType](capi-drawing-text-typography-h.md#oh_drawing_textstyletype) textStyleType | 文本样式类型枚举[OH\_Drawing\_TextStyleType](capi-drawing-text-typography-h.md#oh_drawing_textstyletype)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回两个TextStyle对象是否有对应的文本样式类型一样的结果。true表示其文本样式类型一样，false表示不一样。 |

### OH\_Drawing\_TextStyleSetPlaceholder()

```c
void OH_Drawing_TextStyleSetPlaceholder(OH_Drawing_TextStyle* style)
```

**描述**

设置占位符。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

### OH\_Drawing\_TextStyleIsPlaceholder()

```c
bool OH_Drawing_TextStyleIsPlaceholder(OH_Drawing_TextStyle* style)
```

**描述**

返回是否有设置文本占位符。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回是否有设置文本占位符。true表示有设置文本占位符，false表示未设置文本占位符。 |

### OH\_Drawing\_TypographyStyleGetEffectiveAlignment()

```c
OH_Drawing_TextAlign OH_Drawing_TypographyStyleGetEffectiveAlignment(OH_Drawing_TypographyStyle* style)
```

**描述**

获取文本对齐模式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextAlign](capi-drawing-text-typography-h.md#oh_drawing_textalign) | 返回文本对齐模式的枚举值[OH\_Drawing\_TextAlign](capi-drawing-text-typography-h.md#oh_drawing_textalign)。 |

### OH\_Drawing\_TypographyStyleIsHintEnabled()

```c
bool OH_Drawing_TypographyStyleIsHintEnabled(OH_Drawing_TypographyStyle* style)
```

**描述**

获取文本是否启用字形轮廓自动调整，字形轮廓自动调整用于在渲染小字号文本时改善其可读性和外观。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回文本是否启用字形轮廓自动调整。true表示启用，false表示不启用。 |

### OH\_Drawing\_SetTypographyStyleTextStrutStyle()

```c
void OH_Drawing_SetTypographyStyleTextStrutStyle(OH_Drawing_TypographyStyle* style, OH_Drawing_StrutStyle* strutstyle)
```

**描述**

设置文本支柱样式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| [OH\_Drawing\_StrutStyle](capi-drawing-oh-drawing-strutstyle.md)\* strutstyle | 指向支柱样式对象[OH\_Drawing\_StrutStyle](capi-drawing-oh-drawing-strutstyle.md)的指针，由[OH\_Drawing\_TypographyStyleGetStrutStyle](capi-drawing-text-typography-h.md#oh_drawing_typographystylegetstrutstyle)获取。 |

### OH\_Drawing\_TypographyStyleGetStrutStyle()

```c
OH_Drawing_StrutStyle* OH_Drawing_TypographyStyleGetStrutStyle(OH_Drawing_TypographyStyle* style)
```

**描述**

获取文本支柱样式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_StrutStyle](capi-drawing-oh-drawing-strutstyle.md)\* | 返回指向支柱样式对象[OH\_Drawing\_StrutStyle](capi-drawing-oh-drawing-strutstyle.md)的指针。 |

### OH\_Drawing\_TypographyStyleDestroyStrutStyle()

```c
void OH_Drawing_TypographyStyleDestroyStrutStyle(OH_Drawing_StrutStyle* strutstyle)
```

**描述**

释放被支柱样式对象占据的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_StrutStyle](capi-drawing-oh-drawing-strutstyle.md)\* strutstyle | 指向支柱样式对象[OH\_Drawing\_StrutStyle](capi-drawing-oh-drawing-strutstyle.md)的指针，由[OH\_Drawing\_TypographyStyleGetStrutStyle](capi-drawing-text-typography-h.md#oh_drawing_typographystylegetstrutstyle)获取。 |

### OH\_Drawing\_TypographyStyleStrutStyleEquals()

```c
bool OH_Drawing_TypographyStyleStrutStyleEquals(OH_Drawing_StrutStyle* from, OH_Drawing_StrutStyle* to)
```

**描述**

判断支柱样式结构体是否相同。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_StrutStyle](capi-drawing-oh-drawing-strutstyle.md)\* from | 被比较的支柱样式结构体。 |
| [OH\_Drawing\_StrutStyle](capi-drawing-oh-drawing-strutstyle.md)\* to | 用于比较的支柱样式结构体。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回支柱样式结构体是否相同。true表示相同，false表示不相同。 |

### OH\_Drawing\_TypographyStyleSetHintsEnabled()

```c
void OH_Drawing_TypographyStyleSetHintsEnabled(OH_Drawing_TypographyStyle* style, bool hintsEnabled)
```

**描述**

设置文本是否启用字形轮廓自动调整，字形轮廓自动调整用于在渲染小字号文本时改善其可读性和外观。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| bool hintsEnabled | 是否启用字形轮廓自动调整。true表示启用，false表示不启用。 |

### OH\_Drawing\_TypographyMarkDirty()

```c
void OH_Drawing_TypographyMarkDirty(OH_Drawing_Typography* typography)
```

**描述**

将排版标记为脏数据，用于初始化排版状态。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 表示指向文本[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |

### OH\_Drawing\_TypographyGetUnresolvedGlyphsCount()

```c
int32_t OH_Drawing_TypographyGetUnresolvedGlyphsCount(OH_Drawing_Typography* typography)
```

**描述**

获取文本中尚未解析的字形的数量，该接口需要在[OH\_Drawing\_TypographyLayout](capi-drawing-text-typography-h.md#oh_drawing_typographylayout)接口调用并生效之后调用。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 表示指向文本[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回文本中尚未解析的字形的数量。 |

### OH\_Drawing\_TypographyUpdateFontSize()

```c
void OH_Drawing_TypographyUpdateFontSize(OH_Drawing_Typography* typography, size_t from, size_t to, float fontSize)
```

**描述**

更新排版对象中的字体大小。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 表示指向排版对象[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| size\_t from | 保留字段，暂未使用。 |
| size\_t to | 保留字段，暂未使用。 |
| float fontSize | 表示更新后的字体大小，取值需大于0，单位为px。 |

### OH\_Drawing\_TypographyUpdateFontColor()

```c
void OH_Drawing_TypographyUpdateFontColor(OH_Drawing_Typography* typography, uint32_t color)
```

**描述**

更新排版对象中的字体颜色。如果当前装饰线未设置颜色，使用该接口也会同时更新装饰线的颜色。使用该接口更新字体颜色属性后，可直接使用[OH\_Drawing\_TypographyPaint](capi-drawing-text-typography-h.md#oh_drawing_typographypaint)进行绘制生效。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 表示指向排版对象[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| uint32\_t color | 表示更新后的字体颜色。 |

### OH\_Drawing\_TypographyUpdateDecoration()

```c
void OH_Drawing_TypographyUpdateDecoration(OH_Drawing_Typography* typography, OH_Drawing_TextDecoration decoration)
```

**描述**

更新排版对象中的文本装饰线类型。使用该接口更新文本装饰线类型属性后，可直接使用[OH\_Drawing\_TypographyPaint](capi-drawing-text-typography-h.md#oh_drawing_typographypaint)进行绘制生效。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 表示指向排版对象[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| [OH\_Drawing\_TextDecoration](capi-drawing-text-typography-h.md#oh_drawing_textdecoration) decoration | 表示更新后的装饰线类型，具体可见[OH\_Drawing\_TextDecoration](capi-drawing-text-typography-h.md#oh_drawing_textdecoration)枚举。可通过位或操作一次设置多种装饰线类型。设置非[OH\_Drawing\_TextDecoration](capi-drawing-text-typography-h.md#oh_drawing_textdecoration)枚举的装饰样式则保持原有装饰线类型。 |

### OH\_Drawing\_TypographyUpdateDecorationThicknessScale()

```c
void OH_Drawing_TypographyUpdateDecorationThicknessScale(OH_Drawing_Typography* typography,double decorationThicknessScale)
```

**描述**

更新排版对象中的文本装饰线的粗细缩放比例。使用该接口更新文本装饰线粗细缩放比例属性后，可直接使用[OH\_Drawing\_TypographyPaint](capi-drawing-text-typography-h.md#oh_drawing_typographypaint)进行绘制生效。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 表示指向排版对象[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| double decorationThicknessScale | 表示更新后的文本装饰线的粗细缩放比例。装饰线的粗细会随着这个比例变大而变粗，如果更新的粗细缩放比例小于等于0，那么就不会绘制装饰线。 |

### OH\_Drawing\_TypographyUpdateDecorationStyle()

```c
void OH_Drawing_TypographyUpdateDecorationStyle(OH_Drawing_Typography* typography,OH_Drawing_TextDecorationStyle decorationStyle)
```

**描述**

更新排版对象中的文本装饰线样式。使用该接口更新文本装饰线样式属性后，可直接使用[OH\_Drawing\_TypographyPaint](capi-drawing-text-typography-h.md#oh_drawing_typographypaint)进行绘制生效。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 表示指向排版对象[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| [OH\_Drawing\_TextDecorationStyle](capi-drawing-text-typography-h.md#oh_drawing_textdecorationstyle) decorationStyle | 表示更新后的文本装饰线样式，支持可选的装饰样式具体可见[OH\_Drawing\_TextDecorationStyle](capi-drawing-text-typography-h.md#oh_drawing_textdecorationstyle)枚举。 |

### OH\_Drawing\_TypographyTextGetLineStyle()

```c
bool OH_Drawing_TypographyTextGetLineStyle(OH_Drawing_TypographyStyle* style)
```

**描述**

获取文本排版是否启用行样式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 表示指向[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)对象的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回行样式是否启用的结果。true表示启用，false表示不启用。 |

### OH\_Drawing\_TypographyTextlineStyleGetFontWeight()

```c
OH_Drawing_FontWeight OH_Drawing_TypographyTextlineStyleGetFontWeight(OH_Drawing_TypographyStyle* style)
```

**描述**

获取文本排版行样式字重。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 表示指向[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)对象的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontWeight](capi-drawing-text-typography-h.md#oh_drawing_fontweight) | 返回文本排版行样式字重。  0字重为thin，1字重为extra-light，2字重为light，4字重为medium，5字重为semi-bold，6字重为bold，7字重为extra-bold，8字重为black，3或其它字重为normal/regular，具体可见[OH\_Drawing\_FontWeight](capi-drawing-text-typography-h.md#oh_drawing_fontweight)枚举。 |

### OH\_Drawing\_TypographyTextlineStyleGetFontStyle()

```c
OH_Drawing_FontStyle OH_Drawing_TypographyTextlineStyleGetFontStyle(OH_Drawing_TypographyStyle* style)
```

**描述**

获取文本排版样式中支柱样式的字体样式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 表示指向[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)对象的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontStyle](capi-drawing-text-typography-h.md#oh_drawing_fontstyle) | 返回文本排版样式中支柱样式的字体样式。1为斜体，0或其它为非斜体，具体可见[OH\_Drawing\_FontStyle](capi-drawing-text-typography-h.md#oh_drawing_fontstyle)枚举。 |

### OH\_Drawing\_TypographyTextlineStyleGetFontFamilies()

```c
char** OH_Drawing_TypographyTextlineStyleGetFontFamilies(OH_Drawing_TypographyStyle* style, size_t* num)
```

**描述**

获取文本排版行样式字体家族名。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 表示指向[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)对象的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| size\_t\* num | 指向字体名称数量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| char\*\* | 返回文本排版行样式字体家族名。 |

### OH\_Drawing\_TypographyTextlineStyleDestroyFontFamilies()

```c
void OH_Drawing_TypographyTextlineStyleDestroyFontFamilies(char** fontFamilies, size_t fontFamiliesNum)
```

**描述**

释放字体家族名称列表占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\*\* fontFamilies | 表示指向字体家族的指针。 |
| size\_t fontFamiliesNum | 字体名称的数量。 |

### OH\_Drawing\_TypographyTextlineStyleGetFontSize()

```c
double OH_Drawing_TypographyTextlineStyleGetFontSize(OH_Drawing_TypographyStyle* style)
```

**描述**

获取文本排版行样式字号。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 表示指向[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)对象的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回文本排版行样式字号。 |

### OH\_Drawing\_TypographyTextlineStyleGetHeightScale()

```c
double OH_Drawing_TypographyTextlineStyleGetHeightScale(OH_Drawing_TypographyStyle* style)
```

**描述**

获取文本排版行样式的行高缩放系数。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 表示指向[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)对象的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回文本排版行样式的行高缩放系数。 |

### OH\_Drawing\_TypographyTextlineStyleGetHeightOnly()

```c
bool OH_Drawing_TypographyTextlineStyleGetHeightOnly(OH_Drawing_TypographyStyle* style)
```

**描述**

获取字体渲染过程中计算字体块高度相关参数的方法。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 表示指向[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)对象的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回计算字体块高度相关参数的方法。true表示以字号为准计算，false表示以行距计算。 |

### OH\_Drawing\_TypographyTextlineStyleGetHalfLeading()

```c
bool OH_Drawing_TypographyTextlineStyleGetHalfLeading(OH_Drawing_TypographyStyle* style)
```

**描述**

获取文本排版行样式是否为一半行间距。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 表示指向[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)对象的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 文本排版行样式是否为一半行间距，true表示是一半行间距，false表示不是。 |

### OH\_Drawing\_TypographyTextlineStyleGetSpacingScale()

```c
double OH_Drawing_TypographyTextlineStyleGetSpacingScale(OH_Drawing_TypographyStyle* style)
```

**描述**

获取文本排版行样式间距比例。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 表示指向[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)对象的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回文本排版行样式间距比例。 |

### OH\_Drawing\_TypographyTextlineGetStyleOnly()

```c
bool OH_Drawing_TypographyTextlineGetStyleOnly(OH_Drawing_TypographyStyle* style)
```

**描述**

获取文本排版是否仅启用行样式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 表示指向[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)对象的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回文本排版是否仅启用行样式。true表示启用，false表示不启用。 |

### OH\_Drawing\_TypographyGetTextAlign()

```c
OH_Drawing_TextAlign OH_Drawing_TypographyGetTextAlign(OH_Drawing_TypographyStyle* style)
```

**描述**

获取文本对齐方式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 表示指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextAlign](capi-drawing-text-typography-h.md#oh_drawing_textalign) | 返回文本对齐方式。1为右对齐，2为居中对齐，3为两端对齐，4为与文字方向相同，5为文字方向相反，0或其它为左对齐，具体可见[OH\_Drawing\_TextAlign](capi-drawing-text-typography-h.md#oh_drawing_textalign)枚举。 |

### OH\_Drawing\_TypographyGetTextDirection()

```c
OH_Drawing_TextDirection OH_Drawing_TypographyGetTextDirection(OH_Drawing_TypographyStyle* style)
```

**描述**

获取指定排版样式中的文本方向。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 表示指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextDirection](capi-drawing-text-typography-h.md#oh_drawing_textdirection) | 返回文本方向。0为从右到左，1为从左到右，具体可见[OH\_Drawing\_TextDirection](capi-drawing-text-typography-h.md#oh_drawing_textdirection)枚举。 |

### OH\_Drawing\_TypographyGetTextMaxLines()

```c
size_t OH_Drawing_TypographyGetTextMaxLines(OH_Drawing_TypographyStyle* style)
```

**描述**

获取文本的最大行数。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 表示指向排版样式[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| size\_t | 返回结果为文本最大行数。 |

### OH\_Drawing\_TypographyGetTextEllipsis()

```c
char* OH_Drawing_TypographyGetTextEllipsis(OH_Drawing_TypographyStyle* style)
```

**描述**

获取指定排版样式设置的省略号文本。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 表示指向[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)对象的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| char\* | 返回设置的省略号文本，不再需要时，使用[OH\_Drawing\_TypographyDestroyEllipsis](capi-drawing-text-typography-h.md#oh_drawing_typographydestroyellipsis)释放文本占用内存。 |

### OH\_Drawing\_TypographyDestroyEllipsis()

```c
void OH_Drawing_TypographyDestroyEllipsis(char* ellipsis)
```

**描述**

释放省略号文本占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\* ellipsis | 表示指向省略号文本的指针。 |

### OH\_Drawing\_TypographyStyleEquals()

```c
bool OH_Drawing_TypographyStyleEquals(OH_Drawing_TypographyStyle* from, OH_Drawing_TypographyStyle* to)
```

**描述**

判断排版样式是否相同，当前文本高度修饰符模式[OH\_Drawing\_TextHeightBehavior](capi-drawing-text-typography-h.md#oh_drawing_textheightbehavior)没有被纳入比较。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* from | 被比较的排版样式。 |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* to | 用于比较的排版样式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回排版样式是否相同。true表示相同，false表示不相同。 |

### OH\_Drawing\_TextStyleGetColor()

```c
uint32_t OH_Drawing_TextStyleGetColor(OH_Drawing_TextStyle* style)
```

**描述**

获取文本颜色。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 返回文本颜色。 |

### OH\_Drawing\_TextStyleGetDecorationStyle()

```c
OH_Drawing_TextDecorationStyle OH_Drawing_TextStyleGetDecorationStyle(OH_Drawing_TextStyle* style)
```

**描述**

获取文本装饰样式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextDecorationStyle](capi-drawing-text-typography-h.md#oh_drawing_textdecorationstyle) | 返回文本装饰样式，具体可见[OH\_Drawing\_TextDecorationStyle](capi-drawing-text-typography-h.md#oh_drawing_textdecorationstyle)枚举。 |

### OH\_Drawing\_TextStyleGetFontWeight()

```c
OH_Drawing_FontWeight OH_Drawing_TextStyleGetFontWeight(OH_Drawing_TextStyle* style)
```

**描述**

获取字重。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontWeight](capi-drawing-text-typography-h.md#oh_drawing_fontweight) | 返回字重，具体可见[OH\_Drawing\_FontWeight](capi-drawing-text-typography-h.md#oh_drawing_fontweight)枚举。 |

### OH\_Drawing\_TextStyleGetFontStyle()

```c
OH_Drawing_FontStyle OH_Drawing_TextStyleGetFontStyle(OH_Drawing_TextStyle* style)
```

**描述**

获取指定文本样式的字体样式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向字体样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontStyle](capi-drawing-text-typography-h.md#oh_drawing_fontstyle) | 返回字体样式，具体可见[OH\_Drawing\_FontStyle](capi-drawing-text-typography-h.md#oh_drawing_fontstyle)枚举。 |

### OH\_Drawing\_TextStyleGetBaseline()

```c
OH_Drawing_TextBaseline OH_Drawing_TextStyleGetBaseline(OH_Drawing_TextStyle* style)
```

**描述**

获取指定文本样式的字体基线位置。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextBaseline](capi-drawing-text-typography-h.md#oh_drawing_textbaseline) | 返回字体基线位置，具体可见[OH\_Drawing\_TextBaseline](capi-drawing-text-typography-h.md#oh_drawing_textbaseline)枚举。 |

### OH\_Drawing\_TextStyleGetFontFamilies()

```c
char** OH_Drawing_TextStyleGetFontFamilies(OH_Drawing_TextStyle* style, size_t* num)
```

**描述**

获取字体家族名称列表。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| size\_t\* num | 指向字体名称数量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| char\*\* | 返回获取到的字体家族名称列表。 |

### OH\_Drawing\_TextStyleDestroyFontFamilies()

```c
void OH_Drawing_TextStyleDestroyFontFamilies(char** fontFamilies, size_t num)
```

**描述**

释放长度为num的字体家族名称列表占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\*\* fontFamilies | 指向字体家族名称列表的指针。 |
| size\_t num | 字体家族名称列表的长度。 |

### OH\_Drawing\_TextStyleGetFontSize()

```c
double OH_Drawing_TextStyleGetFontSize(OH_Drawing_TextStyle* style)
```

**描述**

获取指定文本样式字号。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回字号。 |

### OH\_Drawing\_TextStyleGetLetterSpacing()

```c
double OH_Drawing_TextStyleGetLetterSpacing(OH_Drawing_TextStyle* style)
```

**描述**

获取指定文本样式的字符间距。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回字符间距大小。 |

### OH\_Drawing\_TextStyleGetWordSpacing()

```c
double OH_Drawing_TextStyleGetWordSpacing(OH_Drawing_TextStyle* style)
```

**描述**

获取指定文本样式的单词间距。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回单词间距大小。 |

### OH\_Drawing\_TextStyleGetFontHeight()

```c
double OH_Drawing_TextStyleGetFontHeight(OH_Drawing_TextStyle* style)
```

**描述**

获取指定文本样式行高缩放系数。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回行高缩放系数。 |

### OH\_Drawing\_TextStyleGetHalfLeading()

```c
bool OH_Drawing_TextStyleGetHalfLeading(OH_Drawing_TextStyle* style)
```

**描述**

获取指定文本样式一半行间距开关状态。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回当前文本样式一半行间距的开关状态。true表示开启一半行间距，false表示未开启一半行间距。 |

### OH\_Drawing\_TextStyleGetLocale()

```c
const char* OH_Drawing_TextStyleGetLocale(OH_Drawing_TextStyle* style)
```

**描述**

获取语言环境。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 返回语言环境，数据类型为指向char对象的指针。语言环境格式为：语言-国家。如zh-CN表示中文（中国），en-US表示英语（美国）等。具体参考BCP 47语言标签标准。 |

### OH\_Drawing\_TypographyDestroyTextBox()

```c
void OH_Drawing_TypographyDestroyTextBox(OH_Drawing_TextBox* textBox)
```

**描述**

释放文本框占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextBox](capi-drawing-oh-drawing-textbox.md)\* textBox | 指向文本框对象[OH\_Drawing\_TextBox](capi-drawing-oh-drawing-textbox.md)的指针。 |

### OH\_Drawing\_SetTextShadow()

```c
void OH_Drawing_SetTextShadow(OH_Drawing_TextShadow* shadow, uint32_t color, OH_Drawing_Point* offset,double blurRadius)
```

**描述**

设置文本阴影对象的参数。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)\* shadow | 指向文本阴影对象[OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)的指针，由[OH\_Drawing\_CreateTextShadow](capi-drawing-text-typography-h.md#oh_drawing_createtextshadow)获取。 |
| uint32\_t color | 文本阴影的颜色，例如入参为0xAABBCCDD，AA代表透明度，BB代表红色分量的值，CC代表绿色分量的值，DD代表蓝色分量的值。 |
| [OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md)\* offset | 指向坐标点对象[OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md)的指针，文本阴影基于当前文本的偏移位置。 |
| double blurRadius | 模糊半径，浮点数，没有单位，值为0.0时表示没有模糊效果。 |

### OH\_Drawing\_CreateTextTab()

```c
OH_Drawing_TextTab* OH_Drawing_CreateTextTab(OH_Drawing_TextAlign alignment, float location)
```

**描述**

创建文本制表符对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextAlign](capi-drawing-text-typography-h.md#oh_drawing_textalign) alignment | 制表符之后的文本对齐方式。1为右对齐，2为居中对齐，0或其它为左对齐。 |
| float location | 文本制表符之后的文本对齐的位置，相对于当前文本起始位置的偏移。单位为物理像素px，最小值为1.0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextTab](capi-drawing-oh-drawing-texttab.md)\* | 返回指向文本制表符对象的指针。如果返回空指针，表示创建失败。失败的原因可能为没有可用的内存。 |

### OH\_Drawing\_DestroyTextTab()

```c
void OH_Drawing_DestroyTextTab(OH_Drawing_TextTab* tab)
```

**描述**

释放文本制表符对象占据的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextTab](capi-drawing-oh-drawing-texttab.md)\* tab | 指向文本制表符对象的指针。 |

### OH\_Drawing\_GetTextTabAlignment()

```c
OH_Drawing_TextAlign OH_Drawing_GetTextTabAlignment(OH_Drawing_TextTab* tab)
```

**描述**

获取文本制表符对象的对齐方式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextTab](capi-drawing-oh-drawing-texttab.md)\* tab | 指向文本制表符对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextAlign](capi-drawing-text-typography-h.md#oh_drawing_textalign) | 返回文本对齐方式。1为右对齐，2为居中对齐，0或其它为左对齐。 |

### OH\_Drawing\_GetTextTabLocation()

```c
float OH_Drawing_GetTextTabLocation(OH_Drawing_TextTab* tab)
```

**描述**

获取文本制表符的位置。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextTab](capi-drawing-oh-drawing-texttab.md)\* tab | 指向文本制表符对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 返回文本制表符对象的位置，单位为物理像素px。 |

### OH\_Drawing\_SetTypographyTextTab()

```c
void OH_Drawing_SetTypographyTextTab(OH_Drawing_TypographyStyle* style, OH_Drawing_TextTab* tab)
```

**描述**

设置文本制表符对齐方式及位置。当设置了文本对齐方式或者省略号风格时制表符不生效，当制表符位置小于1.0时为替换成空格的效果。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针。 |
| [OH\_Drawing\_TextTab](capi-drawing-oh-drawing-texttab.md)\* tab | 指向文本制表符对象的指针。 |

### OH\_Drawing\_GetDrawingArraySize()

```c
size_t OH_Drawing_GetDrawingArraySize(OH_Drawing_Array* drawingArray)
```

**描述**

获取传入类型为对象数组[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)中的对象个数。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)\* drawingArray | 指向对象数组[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| size\_t | 数组中的对象个数。 |

### OH\_Drawing\_SetTypographyTextTrailingSpaceOptimized()

```c
void OH_Drawing_SetTypographyTextTrailingSpaceOptimized(OH_Drawing_TypographyStyle* style, bool trailingSpaceOptimized)
```

**描述**

设置文本排版时行尾空格是否参与对齐计算。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向文本风格对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针。 |
| bool trailingSpaceOptimized | 设置文本排版时行尾空格是否参与对齐计算。true表示行尾空格不参与计算，false表示行尾空格参与计算，默认值为false。文本居中对齐场景下推荐设置为true。 |

### OH\_Drawing\_TypographyHandlerAddEncodedText()

```c
void OH_Drawing_TypographyHandlerAddEncodedText(OH_Drawing_TypographyCreate* handler, const void* text,size_t byteLength, OH_Drawing_TextEncoding textEncodingType)
```

**描述**

添加指定编码的文本。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)\* handler | 指向[OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)对象的指针，由[OH\_Drawing\_CreateTypographyHandler](capi-drawing-text-typography-h.md#oh_drawing_createtypographyhandler)获取。 |
| const void\* text | 指向文本内容的指针。 |
| size\_t byteLength | 文本的字节长度。 |
| [OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding) textEncodingType | 文本的编码类型，为[OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding)类型的枚举值。只支持TEXT\_ENCODING\_UTF8, TEXT\_ENCODING\_UTF16, TEXT\_ENCODING\_UTF32。 |

### OH\_Drawing\_SetTypographyTextAutoSpace()

```c
void OH_Drawing_SetTypographyTextAutoSpace(OH_Drawing_TypographyStyle* style, bool enableAutoSpace)
```

**描述**

设置文本排版时是否启用自动间距。

默认不启用自动间距，一旦启用则会自动调整CJK（中文字符、日文字符、韩文字符）与西文（拉丁字母、西里尔字母、希腊字母）、CJK与数字、CJK与版权符号、版权符号与数字、版权符号与西文之间的间距。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 表示指向[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)对象的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| bool enableAutoSpace | 设置文本排版时是否启用自动间距。true表示启用自动间距，false表示不启用自动间距，默认值为false。 |

### OH\_Drawing\_TypographyUpdateDecorationColor()

```c
void OH_Drawing_TypographyUpdateDecorationColor(OH_Drawing_Typography* typography, uint32_t color)
```

**描述**

更新排版对象中的文本装饰线颜色。

使用该接口更新文本装饰线颜色属性后，可直接使用[OH\_Drawing\_TypographyPaint](capi-drawing-text-typography-h.md#oh_drawing_typographypaint)进行绘制生效。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 表示指向排版对象[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| uint32\_t color | 表示更新后的文本装饰线颜色。 |

### OH\_Drawing\_SetTypographyVerticalAlignment()

```c
void OH_Drawing_SetTypographyVerticalAlignment(OH_Drawing_TypographyStyle* style,OH_Drawing_TextVerticalAlignment align)
```

**描述**

设置文本垂直对齐方式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 表示指向[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)对象的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| [OH\_Drawing\_TextVerticalAlignment](capi-drawing-text-typography-h.md#oh_drawing_textverticalalignment) align | 设置文本垂直对齐方式。默认为基线对齐，其余对齐方式见[OH\_Drawing\_TextVerticalAlignment](capi-drawing-text-typography-h.md#oh_drawing_textverticalalignment)。 |

### OH\_Drawing\_CopyTypographyStyle()

```c
OH_Drawing_TypographyStyle* OH_Drawing_CopyTypographyStyle(OH_Drawing_TypographyStyle* style)
```

**描述**

创建一个段落样式的对象副本，用于拷贝一个已有的段落样式对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向被拷贝对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* | 返回拷贝的[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)对象指针。如果返回空指针，表示创建失败；可能的原因是无可用内存，或者style为空指针。不再需要时，请使用[OH\_Drawing\_DestroyTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_destroytypographystyle)释放该对象指针。 |

### OH\_Drawing\_CopyTextStyle()

```c
OH_Drawing_TextStyle* OH_Drawing_CopyTextStyle(OH_Drawing_TextStyle* style)
```

**描述**

创建一个文本样式的对象副本，用于拷贝一个已有的文本样式对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向被拷贝对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* | 返回拷贝的[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)对象指针。如果返回空指针，表示创建失败；可能的原因是无可用内存，或者style为空指针。不再需要时，请使用[OH\_Drawing\_DestroyTextStyle](capi-drawing-text-typography-h.md#oh_drawing_destroytextstyle)释放该对象指针。 |

### OH\_Drawing\_CopyTextShadow()

```c
OH_Drawing_TextShadow* OH_Drawing_CopyTextShadow(OH_Drawing_TextShadow* shadow)
```

**描述**

创建一个文本阴影的对象副本，用于拷贝一个已有的文本阴影对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)\* shadow | 指向被拷贝对象[OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)\* | 返回拷贝的[OH\_Drawing\_TextShadow](capi-drawing-oh-drawing-textshadow.md)对象指针。如果返回空指针，表示创建失败；可能的原因是无可用内存，或者shadow为空指针。不再需要时，请使用[OH\_Drawing\_DestroyTextShadow](capi-drawing-text-typography-h.md#oh_drawing_destroytextshadow)释放该对象指针。 |

### OH\_Drawing\_SetTextStyleAttributeDouble()

```c
OH_Drawing_ErrorCode OH_Drawing_SetTextStyleAttributeDouble(OH_Drawing_TextStyle* style, OH_Drawing_TextStyleAttributeId id, double value)
```

**描述**

设置double类型文本样式的属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针。 |
| [OH\_Drawing\_TextStyleAttributeId](capi-drawing-text-typography-h.md#oh_drawing_textstyleattributeid) id | 文本样式属性id。 |
| double value | 文本样式属性值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数style为空指针。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。 |

### OH\_Drawing\_GetTextStyleAttributeDouble()

```c
OH_Drawing_ErrorCode OH_Drawing_GetTextStyleAttributeDouble(OH_Drawing_TextStyle* style, OH_Drawing_TextStyleAttributeId id, double* value)
```

**描述**

获取double类型文本样式的属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针。 |
| [OH\_Drawing\_TextStyleAttributeId](capi-drawing-text-typography-h.md#oh_drawing_textstyleattributeid) id | 文本样式属性id。 |
| double\* value | 指向double类型属性的指针。作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数style为空指针。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。 |

### OH\_Drawing\_SetTextStyleAttributeInt()

```c
OH_Drawing_ErrorCode OH_Drawing_SetTextStyleAttributeInt(OH_Drawing_TextStyle* style, OH_Drawing_TextStyleAttributeId id, int value)
```

**描述**

设置int类型文本样式的属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针。 |
| [OH\_Drawing\_TextStyleAttributeId](capi-drawing-text-typography-h.md#oh_drawing_textstyleattributeid) id | 文本样式属性id。 |
| int value | 待设置属性值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数style为空指针。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。  返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE，表示传入的value超出待设置属性取值范围。 |

### OH\_Drawing\_GetTextStyleAttributeInt()

```c
OH_Drawing_ErrorCode OH_Drawing_GetTextStyleAttributeInt(OH_Drawing_TextStyle* style, OH_Drawing_TextStyleAttributeId id, int* value)
```

**描述**

获取int类型文本样式的属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向文本样式对象[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)的指针。 |
| [OH\_Drawing\_TextStyleAttributeId](capi-drawing-text-typography-h.md#oh_drawing_textstyleattributeid) id | 文本样式属性id。 |
| int\* value | 指向int类型属性的指针。作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数style为空指针。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。 |

### OH\_Drawing\_SetTypographyStyleAttributeDouble()

```c
OH_Drawing_ErrorCode OH_Drawing_SetTypographyStyleAttributeDouble(OH_Drawing_TypographyStyle* style, OH_Drawing_TypographyStyleAttributeId id, double value)
```

**描述**

设置double类型排版样式的属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针。 |
| [OH\_Drawing\_TypographyStyleAttributeId](capi-drawing-text-typography-h.md#oh_drawing_typographystyleattributeid) id | 排版样式属性id。 |
| double value | 待设置属性值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数style为空指针。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。 |

### OH\_Drawing\_GetTypographyStyleAttributeDouble()

```c
OH_Drawing_ErrorCode OH_Drawing_GetTypographyStyleAttributeDouble(OH_Drawing_TypographyStyle* style, OH_Drawing_TypographyStyleAttributeId id, double* value)
```

**描述**

获取double类型排版样式的属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针。 |
| [OH\_Drawing\_TypographyStyleAttributeId](capi-drawing-text-typography-h.md#oh_drawing_typographystyleattributeid) id | 排版样式属性id。 |
| double\* value | 指向double类型属性的指针。作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数style为空指针。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。 |

### OH\_Drawing\_SetTypographyStyleAttributeInt()

```c
OH_Drawing_ErrorCode OH_Drawing_SetTypographyStyleAttributeInt(OH_Drawing_TypographyStyle* style, OH_Drawing_TypographyStyleAttributeId id, int value)
```

**描述**

设置int类型排版样式的属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针。 |
| [OH\_Drawing\_TypographyStyleAttributeId](capi-drawing-text-typography-h.md#oh_drawing_typographystyleattributeid) id | 排版样式属性id。 |
| int value | 待设置属性值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数style为空指针。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。  返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE，表示传入的value超出待设置属性取值范围。 |

### OH\_Drawing\_GetTypographyStyleAttributeInt()

```c
OH_Drawing_ErrorCode OH_Drawing_GetTypographyStyleAttributeInt(OH_Drawing_TypographyStyle* style, OH_Drawing_TypographyStyleAttributeId id, int* value)
```

**描述**

获取int类型排版样式的属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针。 |
| [OH\_Drawing\_TypographyStyleAttributeId](capi-drawing-text-typography-h.md#oh_drawing_typographystyleattributeid) id | 排版样式属性id。 |
| int\* value | 指向int类型属性的指针。作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数style为空指针。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。 |

### OH\_Drawing\_SetTypographyStyleAttributeBool()

```c
OH_Drawing_ErrorCode OH_Drawing_SetTypographyStyleAttributeBool(OH_Drawing_TypographyStyle* style, OH_Drawing_TypographyStyleAttributeId id, bool value)
```

**描述**

设置bool类型排版样式的属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针。 |
| [OH\_Drawing\_TypographyStyleAttributeId](capi-drawing-text-typography-h.md#oh_drawing_typographystyleattributeid) id | 排版样式属性id。 |
| bool value | 待设置属性值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示参数style为空指针。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。 |

### OH\_Drawing\_GetTypographyStyleAttributeBool()

```c
OH_Drawing_ErrorCode OH_Drawing_GetTypographyStyleAttributeBool(OH_Drawing_TypographyStyle* style, OH_Drawing_TypographyStyleAttributeId id, bool* value)
```

**描述**

获取bool类型排版样式的属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针。 |
| [OH\_Drawing\_TypographyStyleAttributeId](capi-drawing-text-typography-h.md#oh_drawing_typographystyleattributeid) id | 排版样式属性id。 |
| bool\* value | 指向bool类型属性的指针。作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示参数style或者value为空指针。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。 |

### OH\_Drawing\_SetTypographyStyleAttributeDoubleArray()

```c
OH_Drawing_ErrorCode OH_Drawing_SetTypographyStyleAttributeDoubleArray(OH_Drawing_TypographyStyle* style, OH_Drawing_TypographyStyleAttributeId id, double* arrayValue, size_t arrayLength)
```

**描述**

设置浮点数数组类型排版样式的属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针。 |
| [OH\_Drawing\_TypographyStyleAttributeId](capi-drawing-text-typography-h.md#oh_drawing_typographystyleattributeid) id | 排版样式属性id。 |
| double\* arrayValue | 指向浮点数数组的指针。 |
| size\_t arrayLength | 指向浮点数数组的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示参数style或者arrayValue为空指针或arrayLength为0。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。 |

### OH\_Drawing\_GetTypographyStyleAttributeDoubleArray()

```c
OH_Drawing_ErrorCode OH_Drawing_GetTypographyStyleAttributeDoubleArray(const OH_Drawing_TypographyStyle* style, OH_Drawing_TypographyStyleAttributeId id, double** arrayValue, size_t* arrayLength)
```

**描述**

获取浮点数数组类型排版样式的属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向排版样式对象[OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)的指针。 |
| [OH\_Drawing\_TypographyStyleAttributeId](capi-drawing-text-typography-h.md#oh_drawing_typographystyleattributeid) id | 排版样式属性id。 |
| double\*\* arrayValue | 指向浮点数数组的指针。作为出参使用。 |
| size\_t\* arrayLength | 指向浮点数数组的长度。作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示参数style或者arrayValue为空指针或arrayLength为0。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。 |

### OH\_Drawing\_SetTypographyAttributeBool()

```c
OH_Drawing_ErrorCode OH_Drawing_SetTypographyAttributeBool(OH_Drawing_Typography* typography, OH_Drawing_TypographyAttributeId id, bool value)
```

**描述**

设置bool类型的排版属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向排版对象[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| [OH\_Drawing\_TypographyAttributeId](capi-drawing-text-typography-h.md#oh_drawing_typographyattributeid) id | 排版属性id，指定要设置的bool类型属性。 |
| bool value | 要设置的bool值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示参数typography为空指针。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。 |

### OH\_Drawing\_GetTypographyAttributeBool()

```c
OH_Drawing_ErrorCode OH_Drawing_GetTypographyAttributeBool(const OH_Drawing_Typography* typography, OH_Drawing_TypographyAttributeId id, bool* value)
```

**描述**

获取bool类型排版的属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向排版对象[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| [OH\_Drawing\_TypographyAttributeId](capi-drawing-text-typography-h.md#oh_drawing_typographyattributeid) id | 排版样式属性id。 |
| bool\* value | 指向bool类型属性的指针。作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示参数typography或value为空指针。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。 |

### OH\_Drawing\_DestroyPositionAndAffinity()

```c
void OH_Drawing_DestroyPositionAndAffinity(OH_Drawing_PositionAndAffinity* positionAndAffinity)
```

**描述**

释放[OH\_Drawing\_PositionAndAffinity](capi-drawing-oh-drawing-positionandaffinity.md)对象持有的内存。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_PositionAndAffinity](capi-drawing-oh-drawing-positionandaffinity.md)\* positionAndAffinity | 指向[OH\_Drawing\_PositionAndAffinity](capi-drawing-oh-drawing-positionandaffinity.md)对象的指针。 |

### OH\_Drawing\_TypographyGetCharacterRangeForGlyphRangeWithBuffer()

```c
OH_Drawing_Range* OH_Drawing_TypographyGetCharacterRangeForGlyphRangeWithBuffer(OH_Drawing_Typography* typography, size_t glyphRangeStart, size_t glyphRangeEnd, OH_Drawing_Range** actualGlyphRange, OH_Drawing_TextEncoding textEncodingType)
```

**描述**

获取指定字形范围对应的字符范围。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| size\_t glyphRangeStart | 表示字形范围的开始位置。 |
| size\_t glyphRangeEnd | 表示字形范围的结束位置。 |
| [OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)\*\* actualGlyphRange | 返回实际的字形范围，表示指向[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)的二级指针，作为出参使用。  当请求的字形范围只包含复杂字形序列的一部分时，该参数返回对应的完整字形范围。  例如：连字、组合表情等可能由多个原子字形组成，必须作为整体处理。  如果该参数为NULL，将不返回实际字形范围，表示调用者不关心实际字形范围信息。  使用后需通过[OH\_Drawing\_ReleaseRangeBuffer](capi-drawing-text-typography-h.md#oh_drawing_releaserangebuffer)接口释放该对象。 |
| [OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding) textEncodingType | 表示文本编码类型[OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding)。  当前仅支持UTF-8和UTF-16编码类型。  对于UTF-8编码，返回的字符范围表示字节范围。  对于UTF-16编码，返回的字符范围表示UTF-16代码单元范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Range\*](capi-drawing-oh-drawing-range.md) | 返回表示字符范围的[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象指针，当不再需要该对象时，请使用[OH\_Drawing\_ReleaseRangeBuffer](capi-drawing-text-typography-h.md#oh_drawing_releaserangebuffer)接口释放。 |

### OH\_Drawing\_TypographyGetCharacterPositionAtCoordinateWithBuffer()

```c
OH_Drawing_PositionAndAffinity* OH_Drawing_TypographyGetCharacterPositionAtCoordinateWithBuffer(OH_Drawing_Typography* typography, double dx, double dy, OH_Drawing_TextEncoding textEncodingType)
```

**描述**

获取与指定坐标最接近的字符位置信息。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| double dx | 文本排版区域内的水平坐标，单位为物理像素（px）。  相对于文本排版区域左上角的x偏移量，向右为正方向。  支持浮点数，可取负值（表示在文本区域左侧）。  坐标超出文本区域范围时，将返回最近的字符位置。可通过触摸事件或点击事件获取。 |
| double dy | 文本排版区域内的垂直坐标，单位为物理像素（px）。  相对于文本排版区域左上角的y偏移量，向下为正方向。  支持浮点数，可取负值（表示在文本区域上方）。  坐标超出文本区域范围时，将返回最近的字符位置。可通过触摸事件或点击事件获取。 |
| [OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding) textEncodingType | 表示文本编码类型[OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding)。  当前仅支持UTF-8和UTF-16编码类型。  对于UTF-8编码，返回的位置表示字节偏移量；对于UTF-16编码，返回的位置表示UTF-16代码单元偏移量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_PositionAndAffinity\*](capi-drawing-oh-drawing-positionandaffinity.md) | 返回坐标处的字符索引位置和亲和性，返回类型为[OH\_Drawing\_PositionAndAffinity](capi-drawing-oh-drawing-positionandaffinity.md)结构体。  当不再需要该对象时，请使用[OH\_Drawing\_DestroyPositionAndAffinity](capi-drawing-text-typography-h.md#oh_drawing_destroypositionandaffinity)接口释放。 |

### OH\_Drawing\_TypographyGetGlyphRangeForCharacterRangeWithBuffer()

```c
OH_Drawing_Range* OH_Drawing_TypographyGetGlyphRangeForCharacterRangeWithBuffer(OH_Drawing_Typography* typography, size_t characterRangeStart, size_t characterRangeEnd, OH_Drawing_Range** actualCharacterRange, OH_Drawing_TextEncoding textEncodingType)
```

**描述**

获取指定字符范围对应的字形范围。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向OH\_Drawing\_Typography对象的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| size\_t characterRangeStart | 表示字符范围的开始位置。 |
| size\_t characterRangeEnd | 表示字符范围的结束位置。 |
| [OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)\*\* actualCharacterRange | 返回实际的字符范围，表示指向[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)的二级指针，作为出参使用。  当请求的字符范围只包含组合字符序列的一部分时，该参数返回对应的完整字符范围。  例如：基础字符加变音符号的组合字符，必须作为整体处理。  如果该参数为NULL，将不返回实际字符范围，表示调用者不关心实际字符范围信息。  使用后需通过[OH\_Drawing\_ReleaseRangeBuffer](capi-drawing-text-typography-h.md#oh_drawing_releaserangebuffer)接口释放该对象。 |
| [OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding) textEncodingType | 表示文本编码类型[OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding)。  当前仅支持UTF-8和UTF-16编码类型。  对于UTF-8编码，输入字符范围应解释为字节范围；对于UTF-16编码，输入字符范围应解释为UTF-16代码单元范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Range\*](capi-drawing-oh-drawing-range.md) | 返回表示字形范围的[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象指针，当不再需要该对象时，请使用[OH\_Drawing\_ReleaseRangeBuffer](capi-drawing-text-typography-h.md#oh_drawing_releaserangebuffer)接口释放。 |

### OH\_Drawing\_ReleaseRangeBuffer()

```c
void OH_Drawing_ReleaseRangeBuffer(OH_Drawing_Range* range)
```

**描述**

释放[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象占用的内存。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)\* range | 表示指向[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象的指针。 |

### OH\_Drawing\_TypographyLayoutWithConstraintsWithBuffer()

```c
OH_Drawing_RectSize OH_Drawing_TypographyLayoutWithConstraintsWithBuffer(OH_Drawing_Typography* typography, OH_Drawing_RectSize constraintsRect, OH_Drawing_Array** fitStrRangeArr, size_t* fitStrRangeArrayLen)
```

**描述**

在约束矩形内布局文本。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* typography | 指向文本对象[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)的指针，由[OH\_Drawing\_CreateTypography](capi-drawing-text-typography-h.md#oh_drawing_createtypography)获取。 |
| [OH\_Drawing\_RectSize](capi-drawing-oh-drawing-rectsize.md) constraintsRect | 约束布局的高度和宽度。 |
| [OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)\*\* fitStrRangeArr | 作为出参，包含实际容纳的段落文本的字符范围。指向数组对象[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)的指针。  通过[OH\_Drawing\_ReleaseArrayBuffer](capi-drawing-text-typography-h.md#oh_drawing_releasearraybuffer)释放内存。 |
| size\_t\* fitStrRangeArrayLen | 作为出参，容纳的字符串数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_RectSize](capi-drawing-oh-drawing-rectsize.md) | 返回布局后的实际文本尺寸，包含宽度和高度信息。 |

### OH\_Drawing\_GetRangeByArrayIndex()

```c
OH_Drawing_Range* OH_Drawing_GetRangeByArrayIndex(OH_Drawing_Array* array, size_t index)
```

**描述**

根据数组索引获取指向OH\_Drawing\_Range对象的指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)\* array | 指向数组对象[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)的指针。 |
| size\_t index | 目标[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象在数组中的索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Range\*](capi-drawing-oh-drawing-range.md) | 返回指向OH\_Drawing\_Range对象的指针。 |

### OH\_Drawing\_ReleaseArrayBuffer()

```c
OH_Drawing_ErrorCode OH_Drawing_ReleaseArrayBuffer(OH_Drawing_Array* array)
```

**描述**

释放[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)\* array | 指向数组对象[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)的指针。  支持的数组类型：  字体全名数组，通过[OH\_Drawing\_GetSystemFontFullNamesByType](capi-drawing-text-font-descriptor-h.md#oh_drawing_getsystemfontfullnamesbytype)获取。  文本行数组，通过[OH\_Drawing\_TypographyGetTextLines](capi-drawing-text-line-h.md#oh_drawing_typographygettextlines)获取。  字符串索引数组，通过[OH\_Drawing\_GetRunStringIndices](capi-drawing-text-run-h.md#oh_drawing_getrunstringindices)获取。  矩形数组，通过[OH\_Drawing\_RectCreateArray](capi-drawing-rect-h.md#oh_drawing_rectcreatearray)获取。  字体描述符数组，通过[OH\_Drawing\_GetFontFullDescriptorsFromStream](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontfulldescriptorsfromstream)或[OH\_Drawing\_GetFontFullDescriptorsFromPath](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontfulldescriptorsfrompath)获取。  文本范围数组，通过[OH\_Drawing\_TypographyLayoutWithConstraintsWithBuffer](capi-drawing-text-typography-h.md#oh_drawing_typographylayoutwithconstraintswithbuffer)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS表示操作成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER表示array为空指针或类型不支持。 |

### OH\_Drawing\_TextStyleAddFontVariationWithNormalization()

```c
void OH_Drawing_TextStyleAddFontVariationWithNormalization(OH_Drawing_TextStyle* style, const char* axis, const float normalizedValue)
```

**描述**

添加归一化后的可变字体属性。对应的字体文件（.ttf文件）需要支持可变调节，此接口才能生效。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向OH\_Drawing\_TextStyle对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)获取。 |
| const char\* axis | 可变字体属性键值对中的键。 |
| const float normalizedValue | 设置的可变字体属性键值对的值。归一化取值范围为[-1,1]，映射字体文件中配置的最小值到最大值范围，0表示字体文件中配置的默认值。 |
