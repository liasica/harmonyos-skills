---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h
title: styled_string.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > styled_string.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e938a9403ef666a800006aa22dbcaf9962e1ae14a82657d61e37936f41da60a4
---

## 概述

在Native侧定义[ArkUI\_NodeType](capi-native-node-h.md#arkui_nodetype)为ARKUI\_NODE\_TEXT的组件的文本样式和文本布局管理器。提供丰富的文本样式设置能力，包括字体样式（字体颜色、大小、粗细、风格）、文本装饰线、文本阴影、基线偏移、字符间距、行高、行间距等；支持图片、超链接、自定义绘制等特殊内容嵌入；提供段落级别的布局管理，包括对齐方式、缩进、段落间距等；支持文本手势交互能力，如点击、长按、触摸事件。适用于需要丰富文本样式展示、复杂文本布局、图文混排、文本交互等场景。

**引用文件：** <arkui/styled\_string.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [StyledStringSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/StyledStringSample)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_StyledString](capi-arkui-nativemodule-arkui-styledstring.md) | ArkUI\_StyledString | 定义文本组件支持的样式化字符串数据对象，支持为文本内容设置多种样式属性，适用于需要在Native侧构建和管理富文本展示的场景。 |
| [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md) | OH\_ArkUI\_SpanStyle | 定义属性字符串样式对象。  可以通过[OH\_ArkUI\_SpanStyle\_Create](capi-styled-string-h.md#oh_arkui_spanstyle_create)接口创建对应的属性字符串样式对象。  可以通过[OH\_ArkUI\_SpanStyle\_Destroy](capi-styled-string-h.md#oh_arkui_spanstyle_destroy)接口销毁属性字符串样式对象。  对象创建后通过[OH\_ArkUI\_SpanStyle\_SetStart](capi-styled-string-h.md#oh_arkui_spanstyle_setstart)和[OH\_ArkUI\_SpanStyle\_SetLength](capi-styled-string-h.md#oh_arkui_spanstyle_setlength)指定样式作用的范围。  对象创建后通过OH\_ArkUI\_SpanStyle\_SetXXXStyle系列接口设置生效的具体样式，例如通过[OH\_ArkUI\_SpanStyle\_SetTextStyle](capi-styled-string-h.md#oh_arkui_spanstyle_settextstyle)设置字体样式效果。 |
| [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md) | OH\_ArkUI\_ImageAttachment | 定义图片样式对象。  可以通过[OH\_ArkUI\_ImageAttachment\_Create](capi-styled-string-h.md#oh_arkui_imageattachment_create)接口创建对应的图片样式对象。  可以通过[OH\_ArkUI\_ImageAttachment\_Destroy](capi-styled-string-h.md#oh_arkui_imageattachment_destroy)接口销毁图片样式对象。  对象创建后通过OH\_ArkUI\_ImageAttachment\_SetXXX系列接口设置生效的具体样式，例如通过[OH\_ArkUI\_ImageAttachment\_SetPixelMap](capi-styled-string-h.md#oh_arkui_imageattachment_setpixelmap)设置图片源。 |
| [OH\_ArkUI\_CustomSpan](capi-arkui-nativemodule-oh-arkui-customspan.md) | OH\_ArkUI\_CustomSpan | 定义自定义绘制Span。  可以通过[OH\_ArkUI\_CustomSpan\_Create](capi-styled-string-h.md#oh_arkui_customspan_create)接口创建对应的自定义绘制Span对象。  可以通过[OH\_ArkUI\_CustomSpan\_Destroy](capi-styled-string-h.md#oh_arkui_customspan_destroy)接口销毁自定义绘制Span对象。  对象创建后通过[OH\_ArkUI\_CustomSpan\_RegisterOnMeasureCallback](capi-styled-string-h.md#oh_arkui_customspan_registeronmeasurecallback)和[OH\_ArkUI\_CustomSpan\_RegisterOnDrawCallback](capi-styled-string-h.md#oh_arkui_customspan_registerondrawcallback)接口注册绘制回调函数。 |
| [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md) | OH\_ArkUI\_TextStyle | 定义文本字体样式。  可以通过[OH\_ArkUI\_TextStyle\_Create](capi-styled-string-h.md#oh_arkui_textstyle_create)接口创建对应的文本字体样式对象。  可以通过[OH\_ArkUI\_TextStyle\_Destroy](capi-styled-string-h.md#oh_arkui_textstyle_destroy)接口销毁文本字体样式对象。  对象创建后通过OH\_ArkUI\_TextStyle\_SetXXX系列接口设置生效的具体样式，例如通过[OH\_ArkUI\_TextStyle\_SetFontColor](capi-styled-string-h.md#oh_arkui_textstyle_setfontcolor)设置字体颜色。 |
| [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md) | OH\_ArkUI\_ParagraphStyle | 定义段落样式。  可以通过[OH\_ArkUI\_ParagraphStyle\_Create](capi-styled-string-h.md#oh_arkui_paragraphstyle_create)接口创建对应的段落样式对象。  可以通过[OH\_ArkUI\_ParagraphStyle\_Destroy](capi-styled-string-h.md#oh_arkui_paragraphstyle_destroy)接口销毁段落样式对象。  对象创建后通过OH\_ArkUI\_ParagraphStyle\_SetXXX系列接口设置生效的具体样式，例如通过[OH\_ArkUI\_ParagraphStyle\_SetTextAlign](capi-styled-string-h.md#oh_arkui_paragraphstyle_settextalign)设置文本对齐方式。 |
| [OH\_ArkUI\_GestureStyle](capi-arkui-nativemodule-oh-arkui-gesturestyle.md) | OH\_ArkUI\_GestureStyle | 定义事件手势样式。  可以通过[OH\_ArkUI\_GestureStyle\_Create](capi-styled-string-h.md#oh_arkui_gesturestyle_create)接口创建对应的事件手势样式对象。  可以通过[OH\_ArkUI\_GestureStyle\_Destroy](capi-styled-string-h.md#oh_arkui_gesturestyle_destroy)接口销毁事件手势样式对象。  对象创建后通过OH\_ArkUI\_GestureStyle\_RegisterOnXXXCallback系列接口注册具体的事件回调，例如通过[OH\_ArkUI\_GestureStyle\_RegisterOnClickCallback](capi-styled-string-h.md#oh_arkui_gesturestyle_registeronclickcallback)注册点击事件回调。 |
| [OH\_ArkUI\_TextShadowStyle](capi-arkui-nativemodule-oh-arkui-textshadowstyle.md) | OH\_ArkUI\_TextShadowStyle | 定义文本阴影样式。  可以通过[OH\_ArkUI\_TextShadowStyle\_Create](capi-styled-string-h.md#oh_arkui_textshadowstyle_create)接口创建对应的文本阴影样式对象。  可以通过[OH\_ArkUI\_TextShadowStyle\_Destroy](capi-styled-string-h.md#oh_arkui_textshadowstyle_destroy)接口销毁文本阴影样式对象。  对象创建后通过[OH\_ArkUI\_TextShadowStyle\_SetTextShadow](capi-styled-string-h.md#oh_arkui_textshadowstyle_settextshadow)接口设置生效的具体样式。 |
| [OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md) | OH\_ArkUI\_DecorationStyle | 定义文本装饰线样式。  可以通过[OH\_ArkUI\_DecorationStyle\_Create](capi-styled-string-h.md#oh_arkui_decorationstyle_create)接口创建对应的文本装饰线样式对象。  可以通过[OH\_ArkUI\_DecorationStyle\_Destroy](capi-styled-string-h.md#oh_arkui_decorationstyle_destroy)接口销毁文本装饰线样式对象。  对象创建后通过OH\_ArkUI\_DecorationStyle\_SetXXX系列接口设置生效的具体样式，例如通过[OH\_ArkUI\_DecorationStyle\_SetTextDecorationType](capi-styled-string-h.md#oh_arkui_decorationstyle_settextdecorationtype)设置装饰线类型。 |
| [OH\_ArkUI\_BaselineOffsetStyle](capi-arkui-nativemodule-oh-arkui-baselineoffsetstyle.md) | OH\_ArkUI\_BaselineOffsetStyle | 定义基线偏移量样式。  可以通过[OH\_ArkUI\_BaselineOffsetStyle\_Create](capi-styled-string-h.md#oh_arkui_baselineoffsetstyle_create)接口创建对应的基线偏移量样式对象。  可以通过[OH\_ArkUI\_BaselineOffsetStyle\_Destroy](capi-styled-string-h.md#oh_arkui_baselineoffsetstyle_destroy)接口销毁基线偏移量样式对象。  对象创建后通过[OH\_ArkUI\_BaselineOffsetStyle\_SetBaselineOffset](capi-styled-string-h.md#oh_arkui_baselineoffsetstyle_setbaselineoffset)接口设置具体的基线偏移量值。 |
| [OH\_ArkUI\_LetterSpacingStyle](capi-arkui-nativemodule-oh-arkui-letterspacingstyle.md) | OH\_ArkUI\_LetterSpacingStyle | 定义字符间距样式。  可以通过[OH\_ArkUI\_LetterSpacingStyle\_Create](capi-styled-string-h.md#oh_arkui_letterspacingstyle_create)接口创建对应的字符间距样式对象。  可以通过[OH\_ArkUI\_LetterSpacingStyle\_Destroy](capi-styled-string-h.md#oh_arkui_letterspacingstyle_destroy)接口销毁字符间距样式对象。  对象创建后通过[OH\_ArkUI\_LetterSpacingStyle\_SetLetterSpacing](capi-styled-string-h.md#oh_arkui_letterspacingstyle_setletterspacing)接口设置具体的字符间距值。 |
| [OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md) | OH\_ArkUI\_LineHeightStyle | 定义行高样式。  可以通过[OH\_ArkUI\_LineHeightStyle\_Create](capi-styled-string-h.md#oh_arkui_lineheightstyle_create)接口创建对应的行高样式对象。  可以通过[OH\_ArkUI\_LineHeightStyle\_Destroy](capi-styled-string-h.md#oh_arkui_lineheightstyle_destroy)接口销毁行高样式对象。  对象创建后可以通过[OH\_ArkUI\_LineHeightStyle\_SetLineHeight](capi-styled-string-h.md#oh_arkui_lineheightstyle_setlineheight)接口设置具体的固定行高值。  从API版本26.0.0开始，[OH\_ArkUI\_LineHeightStyle\_SetLineHeightMultiple](capi-styled-string-h.md#oh_arkui_lineheightstyle_setlineheightmultiple)接口设置具体的行高倍数值。 |
| [OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md) | OH\_ArkUI\_LineSpacingStyle | 定义行间距样式。  可以通过[OH\_ArkUI\_LineSpacingStyle\_Create](capi-styled-string-h.md#oh_arkui_linespacingstyle_create)接口创建对应的行间距样式对象。  可以通过[OH\_ArkUI\_LineSpacingStyle\_Destroy](capi-styled-string-h.md#oh_arkui_linespacingstyle_destroy)接口销毁行间距样式对象。  对象创建后可以通过[OH\_ArkUI\_LineSpacingStyle\_SetLineSpacing](capi-styled-string-h.md#oh_arkui_linespacingstyle_setlinespacing)接口设置具体的行间距值。  可以通过[OH\_ArkUI\_LineSpacingStyle\_SetOnlyBetweenLines](capi-styled-string-h.md#oh_arkui_linespacingstyle_setonlybetweenlines)接口设置行间距是否只在行间生效。 |
| [OH\_ArkUI\_UrlStyle](capi-arkui-nativemodule-oh-arkui-urlstyle.md) | OH\_ArkUI\_UrlStyle | 定义超链接样式。  可以通过[OH\_ArkUI\_UrlStyle\_Create](capi-styled-string-h.md#oh_arkui_urlstyle_create)接口创建对应的超链接样式对象。  可以通过[OH\_ArkUI\_UrlStyle\_Destroy](capi-styled-string-h.md#oh_arkui_urlstyle_destroy)接口销毁超链接样式对象。  对象创建后通过[OH\_ArkUI\_UrlStyle\_SetUrl](capi-styled-string-h.md#oh_arkui_urlstyle_seturl)接口设置链接地址。 |
| [OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md) | OH\_ArkUI\_BackgroundColorStyle | 定义背景颜色样式。  可以通过[OH\_ArkUI\_BackgroundColorStyle\_Create](capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_create)接口创建对应的背景颜色样式对象。  可以通过[OH\_ArkUI\_BackgroundColorStyle\_Destroy](capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_destroy)接口销毁背景颜色样式对象。  对象创建后通过[OH\_ArkUI\_BackgroundColorStyle\_SetColor](capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_setcolor)和[OH\_ArkUI\_BackgroundColorStyle\_SetRadius](capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_setradius)接口设置背景颜色和圆角。 |
| [OH\_ArkUI\_UserDataSpan](capi-arkui-nativemodule-oh-arkui-userdataspan.md) | OH\_ArkUI\_UserDataSpan | 定义用户数据Span样式。  可以通过[OH\_ArkUI\_UserDataSpan\_Create](capi-styled-string-h.md#oh_arkui_userdataspan_create)接口创建对应的用户数据Span样式对象。  可以通过[OH\_ArkUI\_UserDataSpan\_Destroy](capi-styled-string-h.md#oh_arkui_userdataspan_destroy)接口销毁用户数据Span样式对象。  对象创建后通过[OH\_ArkUI\_UserDataSpan\_SetUserData](capi-styled-string-h.md#oh_arkui_userdataspan_setuserdata)接口绑定用户数据。 |
| [OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md) | OH\_ArkUI\_LeadingMarginSpanDrawInfo | 定义段落缩进的自定义绘制信息。  可以通过[OH\_ArkUI\_LeadingMarginSpanDrawInfo\_Create](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_create)接口创建对应的段落缩进的自定义绘制信息对象。  可以通过[OH\_ArkUI\_LeadingMarginSpanDrawInfo\_Destroy](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_destroy)接口销毁段落缩进的自定义绘制信息对象。  对象用于在[OH\_ArkUI\_ParagraphStyle\_RegisterOnDrawLeadingMarginCallback](capi-styled-string-h.md#oh_arkui_paragraphstyle_registerondrawleadingmargincallback)注册的回调函数中，提供当前行的绘制上下文信息。 |
| [ArkUI\_TextLayoutManager](capi-arkui-nativemodule-arkui-textlayoutmanager.md) | ArkUI\_TextLayoutManager | 定义文本布局管理器对象，用于对文本进行布局处理，适用于需要精细控制文本显示和排版效果的场景，可帮助开发者实现自定义的文本布局需求。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_ArkUI\_StyledStringKey](capi-styled-string-h.md#oh_arkui_styledstringkey) | OH\_ArkUI\_StyledStringKey | 属性字符串的样式类型枚举。 |
| [OH\_ArkUI\_SuperscriptStyle](capi-styled-string-h.md#oh_arkui_superscriptstyle) | OH\_ArkUI\_SuperscriptStyle | 定义文本上下角标样式枚举。 |
| [OH\_ArkUI\_TextEncoding](capi-styled-string-h.md#oh_arkui_textencoding) | OH\_ArkUI\_TextEncoding | 文本布局查询接口支持的文本编码类型。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_StyledString\* OH\_ArkUI\_StyledString\_Create(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_FontCollection\* collection)](capi-styled-string-h.md#oh_arkui_styledstring_create) | 创建指向ArkUI\_StyledString对象的指针。 |
| [void OH\_ArkUI\_StyledString\_Destroy(ArkUI\_StyledString\* handle)](capi-styled-string-h.md#oh_arkui_styledstring_destroy) | 释放ArkUI\_StyledString对象占用的内存。 |
| [void OH\_ArkUI\_StyledString\_PushTextStyle(ArkUI\_StyledString\* handle, OH\_Drawing\_TextStyle\* style)](capi-styled-string-h.md#oh_arkui_styledstring_pushtextstyle) | 将新的排版风格设置到当前格式化字符串样式栈顶。 |
| [void OH\_ArkUI\_StyledString\_AddText(ArkUI\_StyledString\* handle, const char\* content)](capi-styled-string-h.md#oh_arkui_styledstring_addtext) | 基于当前格式化字符串样式添加对应的文本内容。 |
| [void OH\_ArkUI\_StyledString\_PopTextStyle(ArkUI\_StyledString\* handle)](capi-styled-string-h.md#oh_arkui_styledstring_poptextstyle) | 将当前格式化字符串对象中栈顶样式出栈。 |
| [OH\_Drawing\_Typography\* OH\_ArkUI\_StyledString\_CreateTypography(ArkUI\_StyledString\* handle)](capi-styled-string-h.md#oh_arkui_styledstring_createtypography) | 基于格式化字符串对象创建指向[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)对象的指针，用于提前进行文本测算排版。[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)对象的生命周期由应用管理，当应用销毁该对象时，应同步调用[NODE\_TEXT\_CONTENT\_WITH\_STYLED\_STRING](capi-native-node-h-nodeattributetype-text.md#node_text_content_with_styled_string)对应的reset方法进行置空，避免野指针崩溃风险。 |
| [void OH\_ArkUI\_StyledString\_AddPlaceholder(ArkUI\_StyledString\* handle, OH\_Drawing\_PlaceholderSpan\* placeholder)](capi-styled-string-h.md#oh_arkui_styledstring_addplaceholder) | 向格式化字符串中添加占位符。 |
| [ArkUI\_StyledString\_Descriptor\* OH\_ArkUI\_StyledString\_Descriptor\_Create(void)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_create) | 创建属性字符串数据对象。 |
| [void OH\_ArkUI\_StyledString\_Descriptor\_Destroy(ArkUI\_StyledString\_Descriptor\* descriptor)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_destroy) | 释放[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象占用的内存。 |
| [int32\_t OH\_ArkUI\_UnmarshallStyledStringDescriptor(uint8\_t\* buffer, size\_t bufferSize, ArkUI\_StyledString\_Descriptor\* descriptor)](capi-styled-string-h.md#oh_arkui_unmarshallstyledstringdescriptor) | 将包含属性字符串信息的字节数组反序列化为属性字符串。 |
| [int32\_t OH\_ArkUI\_MarshallStyledStringDescriptor(uint8\_t\* buffer, size\_t bufferSize, ArkUI\_StyledString\_Descriptor\* descriptor, size\_t\* resultSize)](capi-styled-string-h.md#oh_arkui_marshallstyledstringdescriptor) | 将属性字符串信息序列化为字节数组。 |
| [const char\* OH\_ArkUI\_ConvertToHtml(ArkUI\_StyledString\_Descriptor\* descriptor)](capi-styled-string-h.md#oh_arkui_converttohtml) | 将属性字符串信息转换成HTML。 |
| [ArkUI\_StyledString\_Descriptor\* OH\_ArkUI\_StyledString\_Descriptor\_CreateWithString(const char\* value, const OH\_ArkUI\_SpanStyle\*\* styles, int32\_t length)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_createwithstring) | 创建纯文本内容类型的[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象。 |
| [ArkUI\_StyledString\_Descriptor\* OH\_ArkUI\_StyledString\_Descriptor\_CreateWithImageAttachment(const OH\_ArkUI\_ImageAttachment\* value)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_createwithimageattachment) | 创建图片内容类型的[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象。 |
| [ArkUI\_StyledString\_Descriptor\* OH\_ArkUI\_StyledString\_Descriptor\_CreateWithCustomSpan(const OH\_ArkUI\_CustomSpan\* value)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_createwithcustomspan) | 创建自定义绘制Span内容类型的[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_StyledString\_Descriptor\_GetLength(const ArkUI\_StyledString\_Descriptor\* descriptor, int32\_t\* length)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_getlength) | 获取属性字符串的字符长度。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_StyledString\_Descriptor\_GetString(const ArkUI\_StyledString\_Descriptor\* descriptor, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_getstring) | 获取属性字符串的文本内容。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_StyledString\_Descriptor\_IsEqual(const ArkUI\_StyledString\_Descriptor\* firstDescriptor, const ArkUI\_StyledString\_Descriptor\* secondDescriptor, bool\* isEqual)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_isequal) | 判断两个属性字符串是否相同。当属性字符串的文本及样式均一致，视为相同。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_StyledString\_Descriptor\_SubStyledString(const ArkUI\_StyledString\_Descriptor\* descriptor, ArkUI\_StyledString\_Descriptor\* subDescriptor, uint32\_t start, uint32\_t length)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_substyledstring) | 获取属性字符串的子属性字符串。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_StyledString\_Descriptor\_GetStyles(const ArkUI\_StyledString\_Descriptor\* descriptor, uint32\_t start, uint32\_t length, OH\_ArkUI\_StyledStringKey styledKey, OH\_ArkUI\_SpanStyle\*\* styles, uint32\_t stylesSize, uint32\_t\* writeLength)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_getstyles) | 获取属性字符串指定范围内的样式集合。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_StyledString\_Descriptor\_FromHtml(ArkUI\_StyledString\_Descriptor\* descriptor, const char\* html)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_fromhtml) | 将HTML格式字符串转换成属性字符串。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_StyledString\_Descriptor\_ReplaceString(ArkUI\_StyledString\_Descriptor\* descriptor, uint32\_t start, uint32\_t length, const char\* string)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_replacestring) | 替换属性字符串指定范围的文本。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_StyledString\_Descriptor\_InsertString(ArkUI\_StyledString\_Descriptor\* descriptor, uint32\_t start, const char\* string)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_insertstring) | 在属性字符串的指定位置插入文本。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_StyledString\_Descriptor\_RemoveString(ArkUI\_StyledString\_Descriptor\* descriptor, uint32\_t start, uint32\_t length)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_removestring) | 移除属性字符串指定范围的文本。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_StyledString\_Descriptor\_ReplaceStyle(ArkUI\_StyledString\_Descriptor\* descriptor, const OH\_ArkUI\_SpanStyle\* spanStyle)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_replacestyle) | 替换属性字符串指定范围内的样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_StyledString\_Descriptor\_SetStyle(ArkUI\_StyledString\_Descriptor\* descriptor, const OH\_ArkUI\_SpanStyle\* spanStyle)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_setstyle) | 为属性字符串指定范围设置新样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_StyledString\_Descriptor\_RemoveStyle(ArkUI\_StyledString\_Descriptor\* descriptor, uint32\_t start, uint32\_t length, OH\_ArkUI\_StyledStringKey styledKey)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_removestyle) | 清除属性字符串指定范围内的指定类型样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_StyledString\_Descriptor\_ClearStyles(ArkUI\_StyledString\_Descriptor\* descriptor)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_clearstyles) | 清除属性字符串对象的所有样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_StyledString\_Descriptor\_ReplaceStyledString(ArkUI\_StyledString\_Descriptor\* descriptor, uint32\_t start, uint32\_t length, const ArkUI\_StyledString\_Descriptor\* other)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_replacestyledstring) | 替换指定范围的属性字符串。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_StyledString\_Descriptor\_InsertStyledString(ArkUI\_StyledString\_Descriptor\* descriptor, uint32\_t start, const ArkUI\_StyledString\_Descriptor\* other)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_insertstyledstring) | 在属性字符串的指定位置插入新的属性字符串。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_StyledString\_Descriptor\_AppendStyledString(ArkUI\_StyledString\_Descriptor\* descriptor, const ArkUI\_StyledString\_Descriptor\* other)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_appendstyledstring) | 在属性字符串的末尾追加新的属性字符串。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_StyledString\_Descriptor\_InvalidateCustomSpan(const ArkUI\_StyledString\_Descriptor\* descriptor)](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_invalidatecustomspan) | 主动刷新属性字符串中的自定义绘制Span。 |
| [OH\_ArkUI\_TextStyle\* OH\_ArkUI\_TextStyle\_Create()](capi-styled-string-h.md#oh_arkui_textstyle_create) | 创建[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象。 |
| [void OH\_ArkUI\_TextStyle\_Destroy(OH\_ArkUI\_TextStyle\* textStyle)](capi-styled-string-h.md#oh_arkui_textstyle_destroy) | 释放[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象占用的内存。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextStyle\_SetFontColor(OH\_ArkUI\_TextStyle\* textStyle, uint32\_t fontColor)](capi-styled-string-h.md#oh_arkui_textstyle_setfontcolor) | 设置文本字体样式中的字体颜色。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextStyle\_GetFontColor(const OH\_ArkUI\_TextStyle\* textStyle, uint32\_t\* fontColor)](capi-styled-string-h.md#oh_arkui_textstyle_getfontcolor) | 获取文本字体样式中的字体颜色。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextStyle\_SetFontFamily(OH\_ArkUI\_TextStyle\* textStyle, const char\* fontFamily)](capi-styled-string-h.md#oh_arkui_textstyle_setfontfamily) | 设置文本字体样式中的字体族。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextStyle\_GetFontFamily(const OH\_ArkUI\_TextStyle\* textStyle, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](capi-styled-string-h.md#oh_arkui_textstyle_getfontfamily) | 获取文本字体样式中的字体族。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextStyle\_SetFontSize(OH\_ArkUI\_TextStyle\* textStyle, float fontSize)](capi-styled-string-h.md#oh_arkui_textstyle_setfontsize) | 设置文本字体样式中的字体大小。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextStyle\_GetFontSize(const OH\_ArkUI\_TextStyle\* textStyle, float\* fontSize)](capi-styled-string-h.md#oh_arkui_textstyle_getfontsize) | 获取文本字体样式中的字体大小。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextStyle\_SetFontWeight(OH\_ArkUI\_TextStyle\* textStyle, uint32\_t fontWeight)](capi-styled-string-h.md#oh_arkui_textstyle_setfontweight) | 设置文本字体样式中的字体粗细。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextStyle\_GetFontWeight(const OH\_ArkUI\_TextStyle\* textStyle, uint32\_t\* fontWeight)](capi-styled-string-h.md#oh_arkui_textstyle_getfontweight) | 获取文本字体样式中的字体粗细。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextStyle\_SetFontStyle(OH\_ArkUI\_TextStyle\* textStyle, ArkUI\_FontStyle fontStyle)](capi-styled-string-h.md#oh_arkui_textstyle_setfontstyle) | 设置文本字体样式中的字体风格。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextStyle\_GetFontStyle(const OH\_ArkUI\_TextStyle\* textStyle, ArkUI\_FontStyle\* fontStyle)](capi-styled-string-h.md#oh_arkui_textstyle_getfontstyle) | 获取文本字体样式中的字体风格。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextStyle\_SetStrokeWidth(OH\_ArkUI\_TextStyle\* textStyle, float strokeWidth)](capi-styled-string-h.md#oh_arkui_textstyle_setstrokewidth) | 设置文本字体样式中的描边宽度。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextStyle\_GetStrokeWidth(const OH\_ArkUI\_TextStyle\* textStyle, float\* strokeWidth)](capi-styled-string-h.md#oh_arkui_textstyle_getstrokewidth) | 获取文本字体样式中的描边宽度。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextStyle\_SetStrokeColor(OH\_ArkUI\_TextStyle\* textStyle, uint32\_t strokeColor)](capi-styled-string-h.md#oh_arkui_textstyle_setstrokecolor) | 设置文本字体样式中的描边颜色。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextStyle\_GetStrokeColor(const OH\_ArkUI\_TextStyle\* textStyle, uint32\_t\* strokeColor)](capi-styled-string-h.md#oh_arkui_textstyle_getstrokecolor) | 获取文本字体样式中的描边颜色。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextStyle\_SetSuperscript(OH\_ArkUI\_TextStyle\* textStyle, OH\_ArkUI\_SuperscriptStyle superscript)](capi-styled-string-h.md#oh_arkui_textstyle_setsuperscript) | 设置文本字体样式中的上下标样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextStyle\_GetSuperscript(const OH\_ArkUI\_TextStyle\* textStyle, OH\_ArkUI\_SuperscriptStyle\* superscript)](capi-styled-string-h.md#oh_arkui_textstyle_getsuperscript) | 获取文本字体样式中的上下标样式。 |
| [OH\_ArkUI\_SpanStyle\* OH\_ArkUI\_SpanStyle\_Create()](capi-styled-string-h.md#oh_arkui_spanstyle_create) | 创建[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象。 |
| [void OH\_ArkUI\_SpanStyle\_Destroy(OH\_ArkUI\_SpanStyle\* spanStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_destroy) | 释放[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象占用的内存。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_GetStyledKey(const OH\_ArkUI\_SpanStyle\* spanStyle, OH\_ArkUI\_StyledStringKey\* styledKey)](capi-styled-string-h.md#oh_arkui_spanstyle_getstyledkey) | 获取属性字符串样式对象的样式类型。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_SetStart(OH\_ArkUI\_SpanStyle\* spanStyle, int32\_t start)](capi-styled-string-h.md#oh_arkui_spanstyle_setstart) | 设置属性字符串样式对象的起始位置。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_GetStart(const OH\_ArkUI\_SpanStyle\* spanStyle, int32\_t\* start)](capi-styled-string-h.md#oh_arkui_spanstyle_getstart) | 获取属性字符串样式对象的起始位置。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_SetLength(OH\_ArkUI\_SpanStyle\* spanStyle, int32\_t length)](capi-styled-string-h.md#oh_arkui_spanstyle_setlength) | 设置属性字符串样式对象的长度。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_GetLength(const OH\_ArkUI\_SpanStyle\* spanStyle, int32\_t\* length)](capi-styled-string-h.md#oh_arkui_spanstyle_getlength) | 获取属性字符串样式对象的长度。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_SetTextStyle(OH\_ArkUI\_SpanStyle\* spanStyle, const OH\_ArkUI\_TextStyle\* textStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_settextstyle) | 设置属性字符串样式对象的文本字体样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_GetTextStyle(const OH\_ArkUI\_SpanStyle\* spanStyle, OH\_ArkUI\_TextStyle\* textStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_gettextstyle) | 获取属性字符串样式对象的文本字体样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_SetParagraphStyle(OH\_ArkUI\_SpanStyle\* spanStyle, const OH\_ArkUI\_ParagraphStyle\* paragraphStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_setparagraphstyle) | 设置属性字符串样式对象的段落样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_GetParagraphStyle(const OH\_ArkUI\_SpanStyle\* spanStyle, OH\_ArkUI\_ParagraphStyle\* paragraphStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_getparagraphstyle) | 获取属性字符串样式对象的段落样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_SetGestureStyle(OH\_ArkUI\_SpanStyle\* spanStyle, const OH\_ArkUI\_GestureStyle\* gestureStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_setgesturestyle) | 设置属性字符串样式对象的事件手势样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_GetGestureStyle(const OH\_ArkUI\_SpanStyle\* spanStyle, OH\_ArkUI\_GestureStyle\* gestureStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_getgesturestyle) | 获取属性字符串样式对象的事件手势样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_SetTextShadowStyle(OH\_ArkUI\_SpanStyle\* spanStyle, const OH\_ArkUI\_TextShadowStyle\* textShadowStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_settextshadowstyle) | 设置属性字符串样式对象的文本阴影样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_GetTextShadowStyle(const OH\_ArkUI\_SpanStyle\* spanStyle, OH\_ArkUI\_TextShadowStyle\* textShadowStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_gettextshadowstyle) | 获取属性字符串样式对象的文本阴影样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_SetDecorationStyle(OH\_ArkUI\_SpanStyle\* spanStyle, const OH\_ArkUI\_DecorationStyle\* decorationStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_setdecorationstyle) | 设置属性字符串样式对象的文本装饰线样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_GetDecorationStyle(const OH\_ArkUI\_SpanStyle\* spanStyle, OH\_ArkUI\_DecorationStyle\* decorationStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_getdecorationstyle) | 获取属性字符串样式对象的文本装饰线样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_SetBaselineOffsetStyle(OH\_ArkUI\_SpanStyle\* spanStyle, const OH\_ArkUI\_BaselineOffsetStyle\* baselineOffsetStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_setbaselineoffsetstyle) | 设置属性字符串样式对象的基线偏移量样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_GetBaselineOffsetStyle(const OH\_ArkUI\_SpanStyle\* spanStyle, OH\_ArkUI\_BaselineOffsetStyle\* baselineOffsetStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_getbaselineoffsetstyle) | 获取属性字符串样式对象的基线偏移量样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_SetLetterSpacingStyle(OH\_ArkUI\_SpanStyle\* spanStyle, const OH\_ArkUI\_LetterSpacingStyle\* letterSpacingStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_setletterspacingstyle) | 设置属性字符串样式对象的字符间距样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_GetLetterSpacingStyle(const OH\_ArkUI\_SpanStyle\* spanStyle, OH\_ArkUI\_LetterSpacingStyle\* letterSpacingStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_getletterspacingstyle) | 获取属性字符串样式对象的字符间距样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_SetLineHeightStyle(OH\_ArkUI\_SpanStyle\* spanStyle, const OH\_ArkUI\_LineHeightStyle\* lineHeightStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_setlineheightstyle) | 设置属性字符串样式对象的行高样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_GetLineHeightStyle(const OH\_ArkUI\_SpanStyle\* spanStyle, OH\_ArkUI\_LineHeightStyle\* lineHeightStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_getlineheightstyle) | 获取属性字符串样式对象的行高样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_SetUrlStyle(OH\_ArkUI\_SpanStyle\* spanStyle, const OH\_ArkUI\_UrlStyle\* urlStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_seturlstyle) | 设置属性字符串样式对象的超链接样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_GetUrlStyle(const OH\_ArkUI\_SpanStyle\* spanStyle, OH\_ArkUI\_UrlStyle\* urlStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_geturlstyle) | 获取属性字符串样式对象的超链接样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_SetBackgroundColorStyle(OH\_ArkUI\_SpanStyle\* spanStyle, const OH\_ArkUI\_BackgroundColorStyle\* backgroundColorStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_setbackgroundcolorstyle) | 设置属性字符串样式对象的背景颜色样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_GetBackgroundColorStyle(const OH\_ArkUI\_SpanStyle\* spanStyle, OH\_ArkUI\_BackgroundColorStyle\* backgroundColorStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_getbackgroundcolorstyle) | 获取属性字符串样式对象的背景颜色样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_SetUserDataSpan(OH\_ArkUI\_SpanStyle\* spanStyle, const OH\_ArkUI\_UserDataSpan\* userDataSpan)](capi-styled-string-h.md#oh_arkui_spanstyle_setuserdataspan) | 设置属性字符串样式对象的用户数据Span样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_GetUserDataSpan(const OH\_ArkUI\_SpanStyle\* spanStyle, OH\_ArkUI\_UserDataSpan\* userDataSpan)](capi-styled-string-h.md#oh_arkui_spanstyle_getuserdataspan) | 获取属性字符串样式对象的用户数据Span样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_SetCustomSpan(OH\_ArkUI\_SpanStyle\* spanStyle, const OH\_ArkUI\_CustomSpan\* customSpan)](capi-styled-string-h.md#oh_arkui_spanstyle_setcustomspan) | 设置属性字符串样式对象的自定义绘制Span样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_GetCustomSpan(const OH\_ArkUI\_SpanStyle\* spanStyle, OH\_ArkUI\_CustomSpan\* customSpan)](capi-styled-string-h.md#oh_arkui_spanstyle_getcustomspan) | 获取属性字符串样式对象的自定义绘制Span样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_SetImageAttachment(OH\_ArkUI\_SpanStyle\* spanStyle, const OH\_ArkUI\_ImageAttachment\* imageAttachment)](capi-styled-string-h.md#oh_arkui_spanstyle_setimageattachment) | 设置属性字符串样式对象的图片样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_GetImageAttachment(const OH\_ArkUI\_SpanStyle\* spanStyle, OH\_ArkUI\_ImageAttachment\* imageAttachment)](capi-styled-string-h.md#oh_arkui_spanstyle_getimageattachment) | 获取属性字符串样式对象的图片样式。 |
| [OH\_ArkUI\_LeadingMarginSpanDrawInfo\* OH\_ArkUI\_LeadingMarginSpanDrawInfo\_Create()](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_create) | 创建[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象。 |
| [void OH\_ArkUI\_LeadingMarginSpanDrawInfo\_Destroy(OH\_ArkUI\_LeadingMarginSpanDrawInfo\* drawInfo)](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_destroy) | 释放[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象占用的内存。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LeadingMarginSpanDrawInfo\_SetX(OH\_ArkUI\_LeadingMarginSpanDrawInfo\* drawInfo, float x)](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_setx) | 设置段落缩进的自定义绘制信息对象中当前行相对于组件的水平偏移。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LeadingMarginSpanDrawInfo\_GetX(const OH\_ArkUI\_LeadingMarginSpanDrawInfo\* drawInfo, float\* x)](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_getx) | 获取段落缩进的自定义绘制信息对象中当前行相对于组件的水平偏移。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LeadingMarginSpanDrawInfo\_SetTop(OH\_ArkUI\_LeadingMarginSpanDrawInfo\* drawInfo, float top)](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_settop) | 设置段落缩进的自定义绘制信息对象中行顶与组件上边缘的距离。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LeadingMarginSpanDrawInfo\_GetTop(const OH\_ArkUI\_LeadingMarginSpanDrawInfo\* drawInfo, float\* top)](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_gettop) | 获取段落缩进的自定义绘制信息对象中行顶与组件上边缘的距离。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LeadingMarginSpanDrawInfo\_SetBottom(OH\_ArkUI\_LeadingMarginSpanDrawInfo\* drawInfo, float bottom)](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_setbottom) | 设置段落缩进的自定义绘制信息对象中行底与组件上边缘的距离。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LeadingMarginSpanDrawInfo\_GetBottom(const OH\_ArkUI\_LeadingMarginSpanDrawInfo\* drawInfo, float\* bottom)](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_getbottom) | 获取段落缩进的自定义绘制信息对象中行底与组件上边缘的距离。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LeadingMarginSpanDrawInfo\_SetBaseline(OH\_ArkUI\_LeadingMarginSpanDrawInfo\* drawInfo, float baseline)](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_setbaseline) | 设置段落缩进的自定义绘制信息对象中当前行的基线与组件上边缘的距离。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LeadingMarginSpanDrawInfo\_GetBaseline(const OH\_ArkUI\_LeadingMarginSpanDrawInfo\* drawInfo, float\* baseline)](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_getbaseline) | 获取段落缩进的自定义绘制信息对象中当前行的基线与组件上边缘的距离。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LeadingMarginSpanDrawInfo\_SetTextDirection(OH\_ArkUI\_LeadingMarginSpanDrawInfo\* drawInfo, ArkUI\_TextDirection direction)](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_settextdirection) | 设置段落缩进的自定义绘制信息对象中文本内容的方向。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LeadingMarginSpanDrawInfo\_GetTextDirection(const OH\_ArkUI\_LeadingMarginSpanDrawInfo\* drawInfo, ArkUI\_TextDirection\* direction)](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_gettextdirection) | 获取段落缩进的自定义绘制信息对象中文本内容的方向。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LeadingMarginSpanDrawInfo\_SetStart(OH\_ArkUI\_LeadingMarginSpanDrawInfo\* drawInfo, uint32\_t start)](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_setstart) | 设置段落缩进的自定义绘制信息对象中当前行的起始索引。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LeadingMarginSpanDrawInfo\_GetStart(const OH\_ArkUI\_LeadingMarginSpanDrawInfo\* drawInfo, uint32\_t\* start)](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_getstart) | 获取段落缩进的自定义绘制信息对象中当前行的起始索引。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LeadingMarginSpanDrawInfo\_SetEnd(OH\_ArkUI\_LeadingMarginSpanDrawInfo\* drawInfo, uint32\_t end)](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_setend) | 设置段落缩进的自定义绘制信息对象中当前行的结束索引。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LeadingMarginSpanDrawInfo\_GetEnd(const OH\_ArkUI\_LeadingMarginSpanDrawInfo\* drawInfo, uint32\_t\* end)](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_getend) | 获取段落缩进的自定义绘制信息对象中当前行的结束索引。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LeadingMarginSpanDrawInfo\_SetFirst(OH\_ArkUI\_LeadingMarginSpanDrawInfo\* drawInfo, bool first)](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_setfirst) | 设置段落缩进的自定义绘制信息对象中当前行是否为段落的首行。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LeadingMarginSpanDrawInfo\_GetFirst(const OH\_ArkUI\_LeadingMarginSpanDrawInfo\* drawInfo, bool\* first)](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_getfirst) | 获取段落缩进的自定义绘制信息对象中当前行是否为段落的首行。 |
| [OH\_ArkUI\_ParagraphStyle\* OH\_ArkUI\_ParagraphStyle\_Create()](capi-styled-string-h.md#oh_arkui_paragraphstyle_create) | 创建[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象。 |
| [void OH\_ArkUI\_ParagraphStyle\_Destroy(OH\_ArkUI\_ParagraphStyle\* paragraphStyle)](capi-styled-string-h.md#oh_arkui_paragraphstyle_destroy) | 释放[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象占用的内存。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_SetTextAlign(OH\_ArkUI\_ParagraphStyle\* paragraphStyle, ArkUI\_TextAlignment align)](capi-styled-string-h.md#oh_arkui_paragraphstyle_settextalign) | 设置段落样式中的水平方向的文本对齐方式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_GetTextAlign(const OH\_ArkUI\_ParagraphStyle\* paragraphStyle, ArkUI\_TextAlignment\* align)](capi-styled-string-h.md#oh_arkui_paragraphstyle_gettextalign) | 获取段落样式中的水平方向的文本对齐方式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_SetTextIndent(OH\_ArkUI\_ParagraphStyle\* paragraphStyle, float textIndent)](capi-styled-string-h.md#oh_arkui_paragraphstyle_settextindent) | 设置段落样式中的首行文本缩进。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_GetTextIndent(const OH\_ArkUI\_ParagraphStyle\* paragraphStyle, float\* textIndent)](capi-styled-string-h.md#oh_arkui_paragraphstyle_gettextindent) | 获取段落样式中的首行文本缩进。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_SetMaxLines(OH\_ArkUI\_ParagraphStyle\* paragraphStyle, int32\_t maxLines)](capi-styled-string-h.md#oh_arkui_paragraphstyle_setmaxlines) | 设置段落样式中的最大行数。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_GetMaxLines(const OH\_ArkUI\_ParagraphStyle\* paragraphStyle, int32\_t\* maxLines)](capi-styled-string-h.md#oh_arkui_paragraphstyle_getmaxlines) | 获取段落样式中的最大行数。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_SetOverflow(OH\_ArkUI\_ParagraphStyle\* paragraphStyle, ArkUI\_TextOverflow overflow)](capi-styled-string-h.md#oh_arkui_paragraphstyle_setoverflow) | 设置段落样式中的段落超长时的显示方式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_GetOverflow(const OH\_ArkUI\_ParagraphStyle\* paragraphStyle, ArkUI\_TextOverflow\* overflow)](capi-styled-string-h.md#oh_arkui_paragraphstyle_getoverflow) | 获取段落样式中的段落超长时的显示方式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_SetWordBreak(OH\_ArkUI\_ParagraphStyle\* paragraphStyle, ArkUI\_WordBreak wordBreak)](capi-styled-string-h.md#oh_arkui_paragraphstyle_setwordbreak) | 设置段落样式中的断行规则。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_GetWordBreak(const OH\_ArkUI\_ParagraphStyle\* paragraphStyle, ArkUI\_WordBreak\* wordBreak)](capi-styled-string-h.md#oh_arkui_paragraphstyle_getwordbreak) | 获取段落样式中的断行规则。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_SetLeadingMarginPixelMap(OH\_ArkUI\_ParagraphStyle\* paragraphStyle, struct OH\_PixelmapNative\* pixelmap)](capi-styled-string-h.md#oh_arkui_paragraphstyle_setleadingmarginpixelmap) | 设置段落样式中的段落缩进的像素图。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_GetLeadingMarginPixelMap(const OH\_ArkUI\_ParagraphStyle\* paragraphStyle, struct OH\_PixelmapNative\*\* pixelmap)](capi-styled-string-h.md#oh_arkui_paragraphstyle_getleadingmarginpixelmap) | 获取段落样式中的段落缩进的像素图。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_SetLeadingMarginWidth(OH\_ArkUI\_ParagraphStyle\* paragraphStyle, uint32\_t width)](capi-styled-string-h.md#oh_arkui_paragraphstyle_setleadingmarginwidth) | 设置段落样式中的段落缩进宽度。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_GetLeadingMarginWidth(const OH\_ArkUI\_ParagraphStyle\* paragraphStyle, uint32\_t\* width)](capi-styled-string-h.md#oh_arkui_paragraphstyle_getleadingmarginwidth) | 获取段落样式中的段落缩进宽度。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_SetLeadingMarginHeight(OH\_ArkUI\_ParagraphStyle\* paragraphStyle, uint32\_t height)](capi-styled-string-h.md#oh_arkui_paragraphstyle_setleadingmarginheight) | 设置段落样式中的段落缩进高度。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_GetLeadingMarginHeight(const OH\_ArkUI\_ParagraphStyle\* paragraphStyle, uint32\_t\* height)](capi-styled-string-h.md#oh_arkui_paragraphstyle_getleadingmarginheight) | 获取段落样式中的段落缩进高度。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_SetParagraphSpacing(OH\_ArkUI\_ParagraphStyle\* paragraphStyle, uint32\_t paragraphSpacing)](capi-styled-string-h.md#oh_arkui_paragraphstyle_setparagraphspacing) | 设置段落样式中的段落间距。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_GetParagraphSpacing(const OH\_ArkUI\_ParagraphStyle\* paragraphStyle, uint32\_t\* paragraphSpacing)](capi-styled-string-h.md#oh_arkui_paragraphstyle_getparagraphspacing) | 获取段落样式中的段落间距。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_SetTextVerticalAlign(OH\_ArkUI\_ParagraphStyle\* paragraphStyle, ArkUI\_TextVerticalAlignment verticalAlignment)](capi-styled-string-h.md#oh_arkui_paragraphstyle_settextverticalalign) | 设置段落样式中的垂直方向的文本对齐方式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_GetTextVerticalAlign(const OH\_ArkUI\_ParagraphStyle\* paragraphStyle, ArkUI\_TextVerticalAlignment\* verticalAlignment)](capi-styled-string-h.md#oh_arkui_paragraphstyle_gettextverticalalign) | 获取段落样式中的垂直方向的文本对齐方式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_RegisterOnDrawLeadingMarginCallback(OH\_ArkUI\_ParagraphStyle\* paragraphStyle, void(\*onDraw)(ArkUI\_DrawContext\* context, OH\_ArkUI\_LeadingMarginSpanDrawInfo\* drawInfo))](capi-styled-string-h.md#oh_arkui_paragraphstyle_registerondrawleadingmargincallback) | 注册段落样式中绘制段落缩进时触发的回调函数。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_RegisterOnGetLeadingMarginCallback(OH\_ArkUI\_ParagraphStyle\* paragraphStyle, float(\*leadingMargin)())](capi-styled-string-h.md#oh_arkui_paragraphstyle_registerongetleadingmargincallback) | 设置段落样式中获取段落缩进距离时触发的回调函数。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_SetTextDirection(OH\_ArkUI\_ParagraphStyle\* paragraphStyle, ArkUI\_TextDirection textDirection)](capi-styled-string-h.md#oh_arkui_paragraphstyle_settextdirection) | 设置段落样式中的文本方向。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_GetTextDirection(const OH\_ArkUI\_ParagraphStyle\* paragraphStyle, ArkUI\_TextDirection\* textDirection)](capi-styled-string-h.md#oh_arkui_paragraphstyle_gettextdirection) | 获取段落样式中的文本方向。 |
| [OH\_ArkUI\_GestureStyle\* OH\_ArkUI\_GestureStyle\_Create()](capi-styled-string-h.md#oh_arkui_gesturestyle_create) | 创建[OH\_ArkUI\_GestureStyle](capi-arkui-nativemodule-oh-arkui-gesturestyle.md)对象。 |
| [void OH\_ArkUI\_GestureStyle\_Destroy(OH\_ArkUI\_GestureStyle\* gestureStyle)](capi-styled-string-h.md#oh_arkui_gesturestyle_destroy) | 释放[OH\_ArkUI\_GestureStyle](capi-arkui-nativemodule-oh-arkui-gesturestyle.md)对象占用的内存。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_GestureStyle\_RegisterOnClickCallback(OH\_ArkUI\_GestureStyle\* gestureStyle, void(\*onClick)(ArkUI\_NodeEvent\*))](capi-styled-string-h.md#oh_arkui_gesturestyle_registeronclickcallback) | 注册事件手势样式中的点击事件回调。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_GestureStyle\_RegisterOnLongPressCallback(OH\_ArkUI\_GestureStyle\* gestureStyle, void(\*onLongPress)(ArkUI\_GestureEvent\*))](capi-styled-string-h.md#oh_arkui_gesturestyle_registeronlongpresscallback) | 注册事件手势样式中的长按事件回调。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_GestureStyle\_RegisterOnTouchCallback(OH\_ArkUI\_GestureStyle\* gestureStyle, void(\*onTouch)(ArkUI\_NodeEvent\*))](capi-styled-string-h.md#oh_arkui_gesturestyle_registerontouchcallback) | 注册事件手势样式中的触摸事件回调。 |
| [OH\_ArkUI\_TextShadowStyle\* OH\_ArkUI\_TextShadowStyle\_Create()](capi-styled-string-h.md#oh_arkui_textshadowstyle_create) | 创建[OH\_ArkUI\_TextShadowStyle](capi-arkui-nativemodule-oh-arkui-textshadowstyle.md)对象。 |
| [void OH\_ArkUI\_TextShadowStyle\_Destroy(OH\_ArkUI\_TextShadowStyle\* textShadowStyle)](capi-styled-string-h.md#oh_arkui_textshadowstyle_destroy) | 释放[OH\_ArkUI\_TextShadowStyle](capi-arkui-nativemodule-oh-arkui-textshadowstyle.md)对象占用的内存。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextShadowStyle\_SetTextShadow(OH\_ArkUI\_TextShadowStyle\* textShadowStyle, const OH\_ArkUI\_ShadowOptions\*\* options, uint32\_t length)](capi-styled-string-h.md#oh_arkui_textshadowstyle_settextshadow) | 设置文本阴影样式的文本阴影选项。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextShadowStyle\_GetTextShadow(const OH\_ArkUI\_TextShadowStyle\* textShadowStyle, OH\_ArkUI\_ShadowOptions\*\* shadowOptions, uint32\_t shadowOptionsSize, uint32\_t\* writeLength)](capi-styled-string-h.md#oh_arkui_textshadowstyle_gettextshadow) | 获取文本阴影样式的文本阴影选项。 |
| [OH\_ArkUI\_DecorationStyle\* OH\_ArkUI\_DecorationStyle\_Create()](capi-styled-string-h.md#oh_arkui_decorationstyle_create) | 创建[OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)对象。 |
| [void OH\_ArkUI\_DecorationStyle\_Destroy(OH\_ArkUI\_DecorationStyle\* decorationStyle)](capi-styled-string-h.md#oh_arkui_decorationstyle_destroy) | 释放[OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)对象占用的内存。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_DecorationStyle\_SetTextDecorationType(OH\_ArkUI\_DecorationStyle\* decorationStyle, ArkUI\_TextDecorationType type)](capi-styled-string-h.md#oh_arkui_decorationstyle_settextdecorationtype) | 设置文本装饰线样式的装饰线类型。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_DecorationStyle\_GetTextDecorationType(const OH\_ArkUI\_DecorationStyle\* decorationStyle, ArkUI\_TextDecorationType\* type)](capi-styled-string-h.md#oh_arkui_decorationstyle_gettextdecorationtype) | 获取文本装饰线样式的装饰线类型。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_DecorationStyle\_SetColor(OH\_ArkUI\_DecorationStyle\* decorationStyle, uint32\_t color)](capi-styled-string-h.md#oh_arkui_decorationstyle_setcolor) | 设置文本装饰线样式的装饰线颜色。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_DecorationStyle\_GetColor(const OH\_ArkUI\_DecorationStyle\* decorationStyle, uint32\_t\* color)](capi-styled-string-h.md#oh_arkui_decorationstyle_getcolor) | 获取文本装饰线样式的装饰线颜色。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_DecorationStyle\_SetTextDecorationStyle(OH\_ArkUI\_DecorationStyle\* decorationStyle, ArkUI\_TextDecorationStyle style)](capi-styled-string-h.md#oh_arkui_decorationstyle_settextdecorationstyle) | 设置文本装饰线样式的装饰线样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_DecorationStyle\_GetTextDecorationStyle(const OH\_ArkUI\_DecorationStyle\* decorationStyle, ArkUI\_TextDecorationStyle\* style)](capi-styled-string-h.md#oh_arkui_decorationstyle_gettextdecorationstyle) | 获取文本装饰线样式的装饰线样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_DecorationStyle\_SetThicknessScale(OH\_ArkUI\_DecorationStyle\* decorationStyle, float thicknessScale)](capi-styled-string-h.md#oh_arkui_decorationstyle_setthicknessscale) | 设置文本装饰线样式的装饰线的粗细缩放比例。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_DecorationStyle\_GetThicknessScale(const OH\_ArkUI\_DecorationStyle\* decorationStyle, float\* thicknessScale)](capi-styled-string-h.md#oh_arkui_decorationstyle_getthicknessscale) | 获取文本装饰线样式的装饰线的粗细缩放比例。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_DecorationStyle\_SetEnableMultiType(OH\_ArkUI\_DecorationStyle\* decorationStyle, bool enableMultiType)](capi-styled-string-h.md#oh_arkui_decorationstyle_setenablemultitype) | 设置文本装饰线样式中是否开启多装饰线显示。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_DecorationStyle\_GetEnableMultiType(const OH\_ArkUI\_DecorationStyle\* decorationStyle, bool\* enableMultiType)](capi-styled-string-h.md#oh_arkui_decorationstyle_getenablemultitype) | 获取文本装饰线样式中是否开启多装饰线显示。 |
| [OH\_ArkUI\_BaselineOffsetStyle\* OH\_ArkUI\_BaselineOffsetStyle\_Create()](capi-styled-string-h.md#oh_arkui_baselineoffsetstyle_create) | 创建[OH\_ArkUI\_BaselineOffsetStyle](capi-arkui-nativemodule-oh-arkui-baselineoffsetstyle.md)对象。 |
| [void OH\_ArkUI\_BaselineOffsetStyle\_Destroy(OH\_ArkUI\_BaselineOffsetStyle\* baselineOffsetStyle)](capi-styled-string-h.md#oh_arkui_baselineoffsetstyle_destroy) | 释放[OH\_ArkUI\_BaselineOffsetStyle](capi-arkui-nativemodule-oh-arkui-baselineoffsetstyle.md)对象占用的内存。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_BaselineOffsetStyle\_SetBaselineOffset(OH\_ArkUI\_BaselineOffsetStyle\* baselineOffsetStyle, float baselineOffset)](capi-styled-string-h.md#oh_arkui_baselineoffsetstyle_setbaselineoffset) | 设置基线偏移量。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_BaselineOffsetStyle\_GetBaselineOffset(const OH\_ArkUI\_BaselineOffsetStyle\* baselineOffsetStyle, float\* baselineOffset)](capi-styled-string-h.md#oh_arkui_baselineoffsetstyle_getbaselineoffset) | 获取基线偏移量。 |
| [OH\_ArkUI\_LetterSpacingStyle\* OH\_ArkUI\_LetterSpacingStyle\_Create()](capi-styled-string-h.md#oh_arkui_letterspacingstyle_create) | 创建[OH\_ArkUI\_LetterSpacingStyle](capi-arkui-nativemodule-oh-arkui-letterspacingstyle.md)对象。 |
| [void OH\_ArkUI\_LetterSpacingStyle\_Destroy(OH\_ArkUI\_LetterSpacingStyle\* letterSpacingStyle)](capi-styled-string-h.md#oh_arkui_letterspacingstyle_destroy) | 释放[OH\_ArkUI\_LetterSpacingStyle](capi-arkui-nativemodule-oh-arkui-letterspacingstyle.md)对象占用的内存。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LetterSpacingStyle\_SetLetterSpacing(OH\_ArkUI\_LetterSpacingStyle\* letterSpacingStyle, float letterSpacing)](capi-styled-string-h.md#oh_arkui_letterspacingstyle_setletterspacing) | 设置字符间距。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LetterSpacingStyle\_GetLetterSpacing(const OH\_ArkUI\_LetterSpacingStyle\* letterSpacingStyle, float\* letterSpacing)](capi-styled-string-h.md#oh_arkui_letterspacingstyle_getletterspacing) | 获取字符间距。 |
| [OH\_ArkUI\_LineHeightStyle\* OH\_ArkUI\_LineHeightStyle\_Create()](capi-styled-string-h.md#oh_arkui_lineheightstyle_create) | 创建[OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md)对象。 |
| [void OH\_ArkUI\_LineHeightStyle\_Destroy(OH\_ArkUI\_LineHeightStyle\* lineHeightStyle)](capi-styled-string-h.md#oh_arkui_lineheightstyle_destroy) | 释放[OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md)对象占用的内存。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LineHeightStyle\_SetLineHeight(OH\_ArkUI\_LineHeightStyle\* lineHeightStyle, float lineHeight)](capi-styled-string-h.md#oh_arkui_lineheightstyle_setlineheight) | 设置文本行高。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LineHeightStyle\_GetLineHeight(const OH\_ArkUI\_LineHeightStyle\* lineHeightStyle, float\* lineHeight)](capi-styled-string-h.md#oh_arkui_lineheightstyle_getlineheight) | 获取文本行高。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LineHeightStyle\_SetLineHeightMultiple(OH\_ArkUI\_LineHeightStyle\* lineHeightStyle, float lineHeightMultiple)](capi-styled-string-h.md#oh_arkui_lineheightstyle_setlineheightmultiple) | 设置行高样式的行高倍数。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LineHeightStyle\_GetLineHeightMultiple(const OH\_ArkUI\_LineHeightStyle\* lineHeightStyle, float\* lineHeightMultiple)](capi-styled-string-h.md#oh_arkui_lineheightstyle_getlineheightmultiple) | 获取行高样式的行高倍数。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_SetLineSpacingStyle(OH\_ArkUI\_SpanStyle\* spanStyle, const OH\_ArkUI\_LineSpacingStyle\* lineSpacingStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_setlinespacingstyle) | 设置属性字符串样式对象的行间距样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_SpanStyle\_GetLineSpacingStyle(const OH\_ArkUI\_SpanStyle\* spanStyle, OH\_ArkUI\_LineSpacingStyle\* lineSpacingStyle)](capi-styled-string-h.md#oh_arkui_spanstyle_getlinespacingstyle) | 获取属性字符串样式对象的行间距样式。 |
| [OH\_ArkUI\_LineSpacingStyle\* OH\_ArkUI\_LineSpacingStyle\_Create()](capi-styled-string-h.md#oh_arkui_linespacingstyle_create) | 创建[OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)对象。 |
| [void OH\_ArkUI\_LineSpacingStyle\_Destroy(OH\_ArkUI\_LineSpacingStyle\* lineSpacingStyle)](capi-styled-string-h.md#oh_arkui_linespacingstyle_destroy) | 释放[OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)对象占用的内存。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LineSpacingStyle\_SetLineSpacing(OH\_ArkUI\_LineSpacingStyle\* lineSpacingStyle, float lineSpacing)](capi-styled-string-h.md#oh_arkui_linespacingstyle_setlinespacing) | 设置行间距。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LineSpacingStyle\_GetLineSpacing(const OH\_ArkUI\_LineSpacingStyle\* lineSpacingStyle, float\* lineSpacing)](capi-styled-string-h.md#oh_arkui_linespacingstyle_getlinespacing) | 获取行间距。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LineSpacingStyle\_SetOnlyBetweenLines(OH\_ArkUI\_LineSpacingStyle\* lineSpacingStyle, bool onlyBetweenLines)](capi-styled-string-h.md#oh_arkui_linespacingstyle_setonlybetweenlines) | 设置行间距是否只在行间生效。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_LineSpacingStyle\_GetOnlyBetweenLines(const OH\_ArkUI\_LineSpacingStyle\* lineSpacingStyle, bool\* onlyBetweenLines)](capi-styled-string-h.md#oh_arkui_linespacingstyle_getonlybetweenlines) | 获取行间距是否只在行间生效。 |
| [OH\_ArkUI\_BackgroundColorStyle\* OH\_ArkUI\_BackgroundColorStyle\_Create()](capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_create) | 创建[OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md)对象。 |
| [void OH\_ArkUI\_BackgroundColorStyle\_Destroy(OH\_ArkUI\_BackgroundColorStyle\* style)](capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_destroy) | 释放[OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md)对象占用的内存。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_BackgroundColorStyle\_SetColor(OH\_ArkUI\_BackgroundColorStyle\* style, uint32\_t color)](capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_setcolor) | 设置背景颜色样式的背景色。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_BackgroundColorStyle\_GetColor(const OH\_ArkUI\_BackgroundColorStyle\* style, uint32\_t\* color)](capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_getcolor) | 获取背景颜色样式的背景色。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_BackgroundColorStyle\_SetRadius(OH\_ArkUI\_BackgroundColorStyle\* style, float topLeft, float topRight, float bottomLeft, float bottomRight)](capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_setradius) | 设置背景颜色样式的背景圆角。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_BackgroundColorStyle\_GetRadius(const OH\_ArkUI\_BackgroundColorStyle\* style, float\* topLeft, float\* topRight, float\* bottomLeft, float\* bottomRight)](capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_getradius) | 获取背景颜色样式的背景圆角。 |
| [OH\_ArkUI\_UrlStyle\* OH\_ArkUI\_UrlStyle\_Create()](capi-styled-string-h.md#oh_arkui_urlstyle_create) | 创建[OH\_ArkUI\_UrlStyle](capi-arkui-nativemodule-oh-arkui-urlstyle.md)对象。 |
| [void OH\_ArkUI\_UrlStyle\_Destroy(OH\_ArkUI\_UrlStyle\* style)](capi-styled-string-h.md#oh_arkui_urlstyle_destroy) | 释放[OH\_ArkUI\_UrlStyle](capi-arkui-nativemodule-oh-arkui-urlstyle.md)对象占用的内存。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_UrlStyle\_SetUrl(OH\_ArkUI\_UrlStyle\* style, const char\* url)](capi-styled-string-h.md#oh_arkui_urlstyle_seturl) | 设置超链接样式的超链接内容。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_UrlStyle\_GetUrl(const OH\_ArkUI\_UrlStyle\* style, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](capi-styled-string-h.md#oh_arkui_urlstyle_geturl) | 获取超链接样式的超链接内容。 |
| [OH\_ArkUI\_UserDataSpan\* OH\_ArkUI\_UserDataSpan\_Create()](capi-styled-string-h.md#oh_arkui_userdataspan_create) | 创建[OH\_ArkUI\_UserDataSpan](capi-arkui-nativemodule-oh-arkui-userdataspan.md)对象。 |
| [void OH\_ArkUI\_UserDataSpan\_Destroy(OH\_ArkUI\_UserDataSpan\* userDataSpan)](capi-styled-string-h.md#oh_arkui_userdataspan_destroy) | 释放[OH\_ArkUI\_UserDataSpan](capi-arkui-nativemodule-oh-arkui-userdataspan.md)对象占用的内存。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_UserDataSpan\_SetUserData(OH\_ArkUI\_UserDataSpan\* userDataSpan, void\* userData)](capi-styled-string-h.md#oh_arkui_userdataspan_setuserdata) | 设置用户数据Span样式中的用户数据。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_UserDataSpan\_GetUserData(const OH\_ArkUI\_UserDataSpan\* userDataSpan, void\*\* userData)](capi-styled-string-h.md#oh_arkui_userdataspan_getuserdata) | 获取用户数据Span样式中的用户数据。 |
| [OH\_ArkUI\_CustomSpan\* OH\_ArkUI\_CustomSpan\_Create()](capi-styled-string-h.md#oh_arkui_customspan_create) | 创建[OH\_ArkUI\_CustomSpan](capi-arkui-nativemodule-oh-arkui-customspan.md)对象。 |
| [void OH\_ArkUI\_CustomSpan\_Destroy(OH\_ArkUI\_CustomSpan\* customSpan)](capi-styled-string-h.md#oh_arkui_customspan_destroy) | 释放[OH\_ArkUI\_CustomSpan](capi-arkui-nativemodule-oh-arkui-customspan.md)对象占用的内存。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_CustomSpan\_RegisterOnMeasureCallback(OH\_ArkUI\_CustomSpan\* customSpan, ArkUI\_CustomSpanMetrics\*(\*onMeasure)(float))](capi-styled-string-h.md#oh_arkui_customspan_registeronmeasurecallback) | 注册自定义绘制Span获取尺寸大小时的回调函数。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_CustomSpan\_RegisterOnDrawCallback(OH\_ArkUI\_CustomSpan\* customSpan, void(\*onDraw)(ArkUI\_DrawContext\*, ArkUI\_CustomSpanDrawInfo\*))](capi-styled-string-h.md#oh_arkui_customspan_registerondrawcallback) | 注册自定义绘制Span绘制时的回调函数。 |
| [OH\_ArkUI\_ImageAttachment\* OH\_ArkUI\_ImageAttachment\_Create()](capi-styled-string-h.md#oh_arkui_imageattachment_create) | 创建[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象。 |
| [void OH\_ArkUI\_ImageAttachment\_Destroy(OH\_ArkUI\_ImageAttachment\* imageAttachment)](capi-styled-string-h.md#oh_arkui_imageattachment_destroy) | 释放[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象占用的内存。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_SetPixelMap(OH\_ArkUI\_ImageAttachment\* imageAttachment, struct OH\_PixelmapNative\* pixelmap)](capi-styled-string-h.md#oh_arkui_imageattachment_setpixelmap) | 设置图片样式中的图片数据源。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_GetPixelMap(const OH\_ArkUI\_ImageAttachment\* imageAttachment, struct OH\_PixelmapNative\*\* pixelmap)](capi-styled-string-h.md#oh_arkui_imageattachment_getpixelmap) | 获取图片样式中的图片数据源。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_SetResource(OH\_ArkUI\_ImageAttachment\* imageAttachment, const char\* resource)](capi-styled-string-h.md#oh_arkui_imageattachment_setresource) | 设置图片样式中的图片资源地址。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_GetResource(const OH\_ArkUI\_ImageAttachment\* imageAttachment, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](capi-styled-string-h.md#oh_arkui_imageattachment_getresource) | 获取图片样式中的图片资源地址。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_SetSizeWidth(OH\_ArkUI\_ImageAttachment\* imageAttachment, float width)](capi-styled-string-h.md#oh_arkui_imageattachment_setsizewidth) | 设置图片样式中的图片宽度。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_GetSizeWidth(const OH\_ArkUI\_ImageAttachment\* imageAttachment, float\* width)](capi-styled-string-h.md#oh_arkui_imageattachment_getsizewidth) | 获取图片样式中的图片宽度。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_SetSizeHeight(OH\_ArkUI\_ImageAttachment\* imageAttachment, float height)](capi-styled-string-h.md#oh_arkui_imageattachment_setsizeheight) | 设置图片样式中的图片高度。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_GetSizeHeight(const OH\_ArkUI\_ImageAttachment\* imageAttachment, float\* height)](capi-styled-string-h.md#oh_arkui_imageattachment_getsizeheight) | 获取图片样式中的图片高度。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_SetVerticalAlign(OH\_ArkUI\_ImageAttachment\* imageAttachment, ArkUI\_ImageSpanAlignment verticalAlign)](capi-styled-string-h.md#oh_arkui_imageattachment_setverticalalign) | 设置图片样式中的图片对齐方式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_GetVerticalAlign(const OH\_ArkUI\_ImageAttachment\* imageAttachment, ArkUI\_ImageSpanAlignment\* verticalAlign)](capi-styled-string-h.md#oh_arkui_imageattachment_getverticalalign) | 获取图片样式中的图片对齐方式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_SetObjectFit(OH\_ArkUI\_ImageAttachment\* imageAttachment, ArkUI\_ObjectFit objectFit)](capi-styled-string-h.md#oh_arkui_imageattachment_setobjectfit) | 设置图片样式中的图片缩放类型。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_GetObjectFit(const OH\_ArkUI\_ImageAttachment\* imageAttachment, ArkUI\_ObjectFit\* objectFit)](capi-styled-string-h.md#oh_arkui_imageattachment_getobjectfit) | 获取图片样式中的图片缩放类型。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_SetMargin(OH\_ArkUI\_ImageAttachment\* imageAttachment, ArkUI\_Margin margin)](capi-styled-string-h.md#oh_arkui_imageattachment_setmargin) | 设置图片样式中的图片外边距。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_GetMargin(const OH\_ArkUI\_ImageAttachment\* imageAttachment, ArkUI\_Margin\* margin)](capi-styled-string-h.md#oh_arkui_imageattachment_getmargin) | 获取图片样式中的图片外边距。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_SetPadding(OH\_ArkUI\_ImageAttachment\* imageAttachment, ArkUI\_Margin padding)](capi-styled-string-h.md#oh_arkui_imageattachment_setpadding) | 设置图片样式中的图片内边距。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_GetPadding(const OH\_ArkUI\_ImageAttachment\* imageAttachment, ArkUI\_Margin\* padding)](capi-styled-string-h.md#oh_arkui_imageattachment_getpadding) | 获取图片样式中的图片内边距。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_SetBorderRadiuses(OH\_ArkUI\_ImageAttachment\* imageAttachment, float topLeft, float topRight, float bottomLeft, float bottomRight)](capi-styled-string-h.md#oh_arkui_imageattachment_setborderradiuses) | 设置图片样式中的图片圆角。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_GetBorderRadiuses(const OH\_ArkUI\_ImageAttachment\* imageAttachment, float\* topLeft, float\* topRight, float\* bottomLeft, float\* bottomRight)](capi-styled-string-h.md#oh_arkui_imageattachment_getborderradiuses) | 获取图片样式中的图片圆角。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_SetColorFilter(OH\_ArkUI\_ImageAttachment\* imageAttachment, const float\* colorFilter, uint32\_t size)](capi-styled-string-h.md#oh_arkui_imageattachment_setcolorfilter) | 设置图片样式中的图片颜色过滤器。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_GetColorFilter(const OH\_ArkUI\_ImageAttachment\* imageAttachment, float\*\* colorFilter, uint32\_t colorFilterSize, uint32\_t\* writeLength)](capi-styled-string-h.md#oh_arkui_imageattachment_getcolorfilter) | 获取图片样式中的图片颜色过滤器。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_SetDrawingColorFilter(OH\_ArkUI\_ImageAttachment\* imageAttachment, const OH\_Drawing\_ColorFilter\* drawingColorFilter)](capi-styled-string-h.md#oh_arkui_imageattachment_setdrawingcolorfilter) | 设置图片样式中的图片颜色滤镜。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_GetDrawingColorFilter(const OH\_ArkUI\_ImageAttachment\* imageAttachment, OH\_Drawing\_ColorFilter\* drawingColorFilter)](capi-styled-string-h.md#oh_arkui_imageattachment_getdrawingcolorfilter) | 获取图片样式中的图片颜色滤镜。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_SetSyncLoad(OH\_ArkUI\_ImageAttachment\* imageAttachment, bool syncLoad)](capi-styled-string-h.md#oh_arkui_imageattachment_setsyncload) | 设置图片样式中是否同步加载图片。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_GetSyncLoad(const OH\_ArkUI\_ImageAttachment\* imageAttachment, bool\* syncLoad)](capi-styled-string-h.md#oh_arkui_imageattachment_getsyncload) | 获取图片样式中是否同步加载图片。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_SetSupportSvg(OH\_ArkUI\_ImageAttachment\* imageAttachment, bool supportSvg)](capi-styled-string-h.md#oh_arkui_imageattachment_setsupportsvg) | 设置图片样式中是否开启SVG标签解析能力增强功能，开启后支持解析扩展SVG标签及属性。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ImageAttachment\_GetSupportSvg(const OH\_ArkUI\_ImageAttachment\* imageAttachment, bool\* supportSvg)](capi-styled-string-h.md#oh_arkui_imageattachment_getsupportsvg) | 获取图片样式中是否开启SVG标签解析能力增强功能。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextEditorChangeEvent\_GetRangeBefore(const OH\_ArkUI\_TextEditorChangeEvent\* event, uint32\_t\* start, uint32\_t\* end)](capi-styled-string-h.md#oh_arkui_texteditorchangeevent_getrangebefore) | 获取文本变化信息中待被替换的原文本的范围。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextEditorChangeEvent\_GetReplacementStyledString(const OH\_ArkUI\_TextEditorChangeEvent\* event, ArkUI\_StyledString\_Descriptor\* descriptor)](capi-styled-string-h.md#oh_arkui_texteditorchangeevent_getreplacementstyledstring) | 获取文本变化信息中的用于替换的属性字符串。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextEditorChangeEvent\_GetPreviewStyledString(const OH\_ArkUI\_TextEditorChangeEvent\* event, ArkUI\_StyledString\_Descriptor\* descriptor)](capi-styled-string-h.md#oh_arkui_texteditorchangeevent_getpreviewstyledstring) | 获取文本变化信息中的预览内容属性字符串。 |
| [void OH\_ArkUI\_TextLayoutManager\_Dispose(ArkUI\_TextLayoutManager\* layoutManager)](capi-styled-string-h.md#oh_arkui_textlayoutmanager_dispose) | 释放文本布局管理器对象占用的内存。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetLineCount(ArkUI\_TextLayoutManager\* layoutManager, int32\_t\* outLineCount)](capi-styled-string-h.md#oh_arkui_textlayoutmanager_getlinecount) | 获取文本行数。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetRectsForRange(ArkUI\_TextLayoutManager\* layoutManager, int32\_t start, int32\_t end, OH\_Drawing\_RectWidthStyle widthStyle, OH\_Drawing\_RectHeightStyle heightStyle, OH\_Drawing\_TextBox\*\* outTextBoxes)](capi-styled-string-h.md#oh_arkui_textlayoutmanager_getrectsforrange) | 获取给定的矩形区域宽度样式以及高度样式的规格下，文本中任意区间范围内的字符或占位符所占的绘制区域信息。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetGlyphPositionAtCoordinate(ArkUI\_TextLayoutManager\* layoutManager, double dx, double dy, OH\_Drawing\_PositionAndAffinity\*\* outPos)](capi-styled-string-h.md#oh_arkui_textlayoutmanager_getglyphpositionatcoordinate) | 获取距离给定坐标最近的字形的位置信息。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetLineMetrics(ArkUI\_TextLayoutManager\* layoutManager, int32\_t lineNumber, OH\_Drawing\_LineMetrics\* outMetrics)](capi-styled-string-h.md#oh_arkui_textlayoutmanager_getlinemetrics) | 获取指定行的行信息、文本样式信息、以及字体属性信息。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetCharacterPositionAtCoordinate(ArkUI\_TextLayoutManager\* layoutManager, double dx, double dy, OH\_Drawing\_PositionAndAffinity\*\* outPos)](capi-styled-string-h.md#oh_arkui_textlayoutmanager_getcharacterpositionatcoordinate) | 获取距离指定坐标最近的字符的位置信息。与OH\_ArkUI\_TextLayoutManager\_GetGlyphPositionAtCoordinate的区别：此方法返回字符级别的位置信息，适用于文本编辑、光标定位等基于字符编码的场景；而GetGlyphPositionAtCoordinate返回字形级别的位置信息，适用于渲染相关的精确定位场景。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetGlyphRangeForCharacterRange(ArkUI\_TextLayoutManager\* layoutManager, OH\_Drawing\_Range\* charRange, OH\_Drawing\_Range\*\* outGlyphRange, OH\_Drawing\_Range\*\* outActualCharRange)](capi-styled-string-h.md#oh_arkui_textlayoutmanager_getglyphrangeforcharacterrange) | 获取由指定字符范围所生成的字形范围。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetCharacterRangeForGlyphRange(ArkUI\_TextLayoutManager\* layoutManager, OH\_Drawing\_Range\* glyphRange, OH\_Drawing\_Range\*\* outCharRange, OH\_Drawing\_Range\*\* outActualGlyphRange)](capi-styled-string-h.md#oh_arkui_textlayoutmanager_getcharacterrangeforglyphrange) | 获取由指定字形范围所生成的字符范围。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetCharacterPositionAtCoordinateWithEncoding(ArkUI\_TextLayoutManager\* layoutManager, double dx, double dy, OH\_ArkUI\_TextEncoding encoding, OH\_Drawing\_PositionAndAffinity\*\* outPos)](capi-styled-string-h.md#oh_arkui_textlayoutmanager_getcharacterpositionatcoordinatewithencoding) | 根据指定编码类型，获取距离指定坐标最近的字符位置信息。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetGlyphRangeForCharacterRangeWithEncoding(ArkUI\_TextLayoutManager\* layoutManager, OH\_Drawing\_Range\* charRange, OH\_ArkUI\_TextEncoding encoding, OH\_Drawing\_Range\*\* outGlyphRange, OH\_Drawing\_Range\*\* outActualCharRange)](capi-styled-string-h.md#oh_arkui_textlayoutmanager_getglyphrangeforcharacterrangewithencoding) | 根据指定编码类型和文本字符范围，获取字形范围以及实际的字符范围。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_TextLayoutManager\_GetCharacterRangeForGlyphRangeWithEncoding(ArkUI\_TextLayoutManager\* layoutManager, OH\_Drawing\_Range\* glyphRange, OH\_ArkUI\_TextEncoding encoding, OH\_Drawing\_Range\*\* outCharRange, OH\_Drawing\_Range\*\* outActualGlyphRange)](capi-styled-string-h.md#oh_arkui_textlayoutmanager_getcharacterrangeforglyphrangewithencoding) | 根据指定编码类型和文本字形范围，获取字符范围以及实际的字形范围。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_SetLinearGradient(OH\_ArkUI\_ParagraphStyle\* paragraphStyle, const OH\_ArkUI\_LinearGradientOptions\* linearGradient)](capi-styled-string-h.md#oh_arkui_paragraphstyle_setlineargradient) | 设置段落样式的线性渐变。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_GetLinearGradient(const OH\_ArkUI\_ParagraphStyle\* paragraphStyle, OH\_ArkUI\_LinearGradientOptions\* linearGradient)](capi-styled-string-h.md#oh_arkui_paragraphstyle_getlineargradient) | 获取段落样式的线性渐变。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_SetRadialGradient(OH\_ArkUI\_ParagraphStyle\* paragraphStyle, const OH\_ArkUI\_RadialGradientOptions\* radialGradient)](capi-styled-string-h.md#oh_arkui_paragraphstyle_setradialgradient) | 设置段落样式的径向渐变。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_GetRadialGradient(const OH\_ArkUI\_ParagraphStyle\* paragraphStyle, OH\_ArkUI\_RadialGradientOptions\* radialGradient)](capi-styled-string-h.md#oh_arkui_paragraphstyle_getradialgradient) | 获取段落样式的径向渐变。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_SetTailIndents(OH\_ArkUI\_ParagraphStyle\* paragraphStyle, const float\* tailIndents, uint32\_t size)](capi-styled-string-h.md#oh_arkui_paragraphstyle_settailindents) | 设置段落样式的尾部缩进。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ParagraphStyle\_GetTailIndents(const OH\_ArkUI\_ParagraphStyle\* paragraphStyle, float\*\* tailIndents, uint32\_t tailIndentsSize, uint32\_t\* writeLength)](capi-styled-string-h.md#oh_arkui_paragraphstyle_gettailindents) | 获取段落样式的尾部缩进。 |

## 枚举类型说明

### OH\_ArkUI\_StyledStringKey

```c
enum OH_ArkUI_StyledStringKey
```

**描述**

属性字符串的样式类型枚举。

**起始版本：** 24

| 枚举项 | 描述 |
| --- | --- |
| OH\_ARKUI\_STYLEDSTRINGKEY\_UNSPECIFIED = -1 | 未指定样式。 |
| OH\_ARKUI\_STYLEDSTRINGKEY\_FONT = 0 | 文本字体样式。 |
| OH\_ARKUI\_STYLEDSTRINGKEY\_DECORATION = 1 | 文本装饰线样式。 |
| OH\_ARKUI\_STYLEDSTRINGKEY\_BASELINE\_OFFSET = 2 | 文本基线偏移量样式。 |
| OH\_ARKUI\_STYLEDSTRINGKEY\_LETTER\_SPACING = 3 | 文本字符间距样式。 |
| OH\_ARKUI\_STYLEDSTRINGKEY\_TEXT\_SHADOW = 4 | 文本阴影样式。 |
| OH\_ARKUI\_STYLEDSTRINGKEY\_LINE\_HEIGHT = 5 | 文本行高样式。 |
| OH\_ARKUI\_STYLEDSTRINGKEY\_BACKGROUND\_COLOR = 6 | 文本背景颜色样式。 |
| OH\_ARKUI\_STYLEDSTRINGKEY\_URL = 7 | 超链接样式。 |
| OH\_ARKUI\_STYLEDSTRINGKEY\_LINE\_SPACING = 8 | 文本行间距样式。**起始版本：** 26.0.0 |
| OH\_ARKUI\_STYLEDSTRINGKEY\_GESTURE = 100 | 事件手势样式。 |
| OH\_ARKUI\_STYLEDSTRINGKEY\_PARAGRAPH\_STYLE = 200 | 文本段落样式。 |
| OH\_ARKUI\_STYLEDSTRINGKEY\_IMAGE = 300 | 图片样式。 |
| OH\_ARKUI\_STYLEDSTRINGKEY\_CUSTOM\_SPAN = 400 | 自定义绘制Span样式。 |
| OH\_ARKUI\_STYLEDSTRINGKEY\_USER\_DATA = 500 | 用户数据Span样式。 |

### OH\_ArkUI\_SuperscriptStyle

```c
enum OH_ArkUI_SuperscriptStyle
```

**描述**

定义文本上下角标样式枚举。

**起始版本：** 24

| 枚举项 | 描述 |
| --- | --- |
| OH\_ARKUI\_SUPERSCRIPTSTYLE\_NORMAL = 0 | 普通文本样式，适用于不需要上下标效果的常规文本场景。 |
| OH\_ARKUI\_SUPERSCRIPTSTYLE\_SUPERSCRIPT = 1 | 上标文本样式，适用于数学公式中的指数表示（如x²）或脚注引用标记等场景。 |
| OH\_ARKUI\_SUPERSCRIPTSTYLE\_SUBSCRIPT = 2 | 下标文本样式，适用于化学式中的元素下标表示（如H₂O）或数学变量下标等场景。 |

### OH\_ArkUI\_TextEncoding

```c
enum OH_ArkUI_TextEncoding
```

**描述**

文本布局查询接口支持的文本编码类型。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| OH\_ARKUI\_TEXT\_ENCODING\_UTF8 = 0 | UTF-8编码。字符位置或字符范围按UTF-8字节偏移量计算。 |
| OH\_ARKUI\_TEXT\_ENCODING\_UTF16 = 1 | UTF-16编码。字符位置或字符范围按UTF-16码元偏移量计算。 |

## 函数说明

### OH\_ArkUI\_StyledString\_Create()

```c
ArkUI_StyledString* OH_ArkUI_StyledString_Create(OH_Drawing_TypographyStyle* style, OH_Drawing_FontCollection* collection)
```

**描述**

创建指向ArkUI\_StyledString对象的指针。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_StyledString\_Destroy](capi-styled-string-h.md#oh_arkui_styledstring_destroy)销毁它。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyStyle](capi-drawing-oh-drawing-typographystyle.md)\* style | 指向OH\_Drawing\_TypographyStyle的指针，由[OH\_Drawing\_CreateTypographyStyle](capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle)获取。 |
| [OH\_Drawing\_FontCollection](capi-drawing-oh-drawing-fontcollection.md)\* collection | 指向OH\_Drawing\_FontCollection的指针，由[OH\_Drawing\_CreateFontCollection](capi-drawing-font-collection-h.md#oh_drawing_createfontcollection)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_StyledString](capi-arkui-nativemodule-arkui-styledstring.md)\* | 创建指向ArkUI\_StyledString对象的指针。如果返回空指针，表示创建失败，可能原因包括地址空间已满或参数异常（如style、collection为空指针）。 |

### OH\_ArkUI\_StyledString\_Destroy()

```c
void OH_ArkUI_StyledString_Destroy(ArkUI_StyledString* handle)
```

**描述**

释放ArkUI\_StyledString对象占用的内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_StyledString](capi-arkui-nativemodule-arkui-styledstring.md)\* handle | 指向ArkUI\_StyledString对象的指针。 |

### OH\_ArkUI\_StyledString\_PushTextStyle()

```c
void OH_ArkUI_StyledString_PushTextStyle(ArkUI_StyledString* handle, OH_Drawing_TextStyle* style)
```

**描述**

将新的排版风格设置到当前格式化字符串样式栈顶。

**说明** 

调用此方法压入的样式，必须在使用完毕后调用[OH\_ArkUI\_StyledString\_PopTextStyle](capi-styled-string-h.md#oh_arkui_styledstring_poptextstyle)将其出栈。未出栈的样式会持续影响后续添加的文本排版。典型使用流程：PushTextStyle → AddText → PopTextStyle。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_StyledString](capi-arkui-nativemodule-arkui-styledstring.md)\* handle | 指向ArkUI\_StyledString对象的指针。 |
| [OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)\* style | 指向[OH\_Drawing\_TextStyle](capi-drawing-oh-drawing-textstyle.md)对象的指针，由[OH\_Drawing\_CreateTextStyle](capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)创建获取。 |

### OH\_ArkUI\_StyledString\_AddText()

```c
void OH_ArkUI_StyledString_AddText(ArkUI_StyledString* handle, const char* content)
```

**描述**

基于当前格式化字符串样式添加对应的文本内容。所添加的文本将使用当前栈顶的排版样式，该样式由[OH\_ArkUI\_StyledString\_PushTextStyle](capi-styled-string-h.md#oh_arkui_styledstring_pushtextstyle)压入。当栈顶样式通过[OH\_ArkUI\_StyledString\_PopTextStyle](capi-styled-string-h.md#oh_arkui_styledstring_poptextstyle)出栈后，后续添加的文本将使用新的栈顶样式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_StyledString](capi-arkui-nativemodule-arkui-styledstring.md)\* handle | 指向ArkUI\_StyledString对象的指针。 |
| const char\* content | 指向文本内容的指针。 |

### OH\_ArkUI\_StyledString\_PopTextStyle()

```c
void OH_ArkUI_StyledString_PopTextStyle(ArkUI_StyledString* handle)
```

**描述**

将当前格式化字符串对象中栈顶样式出栈。

**说明** 

此方法必须在[OH\_ArkUI\_StyledString\_PushTextStyle](capi-styled-string-h.md#oh_arkui_styledstring_pushtextstyle)之后调用，用于将之前压入的样式从栈中移除。对空栈调用此方法不产生效果。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_StyledString](capi-arkui-nativemodule-arkui-styledstring.md)\* handle | 指向ArkUI\_StyledString对象的指针。 |

### OH\_ArkUI\_StyledString\_CreateTypography()

```c
OH_Drawing_Typography* OH_ArkUI_StyledString_CreateTypography(ArkUI_StyledString* handle)
```

**描述**

基于格式化字符串对象创建指向[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)对象的指针，用于提前进行文本测算排版。

**说明** 

[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)对象的生命周期由应用管理，当应用销毁该对象时，应同步调用[NODE\_TEXT\_CONTENT\_WITH\_STYLED\_STRING](capi-native-node-h-nodeattributetype-text.md#node_text_content_with_styled_string)对应的reset方法进行置空，避免野指针崩溃风险。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_StyledString](capi-arkui-nativemodule-arkui-styledstring.md)\* handle | 指向ArkUI\_StyledString对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)\* | 指向OH\_Drawing\_Typography对象的指针。如果对象返回空指针，表示创建失败，失败的原因是handle参数为空指针。 |

### OH\_ArkUI\_StyledString\_AddPlaceholder()

```c
void OH_ArkUI_StyledString_AddPlaceholder(ArkUI_StyledString* handle, OH_Drawing_PlaceholderSpan* placeholder)
```

**描述**

添加占位符，用于在格式化字符串中预留指定宽高的空白区域或嵌入自定义内容。其尺寸等信息由[OH\_Drawing\_PlaceholderSpan](capi-drawing-oh-drawing-placeholderspan.md)指定。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_StyledString](capi-arkui-nativemodule-arkui-styledstring.md)\* handle | 指向ArkUI\_StyledString对象的指针。 |
| [OH\_Drawing\_PlaceholderSpan](capi-drawing-oh-drawing-placeholderspan.md)\* placeholder | 指向OH\_Drawing\_PlaceholderSpan对象的指针。 |

### OH\_ArkUI\_StyledString\_Descriptor\_Create()

```c
ArkUI_StyledString_Descriptor* OH_ArkUI_StyledString_Descriptor_Create(void)
```

**描述**

创建属性字符串数据对象。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_StyledString\_Descriptor\_Destroy](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_destroy)销毁它。

**起始版本：** 14

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* | 指向ArkUI\_StyledString\_Descriptor对象的指针，用于存储属性字符串的文本和样式信息。 |

### OH\_ArkUI\_StyledString\_Descriptor\_Destroy()

```c
void OH_ArkUI_StyledString_Descriptor_Destroy(ArkUI_StyledString_Descriptor* descriptor)
```

**描述**

释放ArkUI\_StyledString\_Descriptor对象占用的内存。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向ArkUI\_StyledString\_Descriptor对象的指针。 |

### OH\_ArkUI\_UnmarshallStyledStringDescriptor()

```c
int32_t OH_ArkUI_UnmarshallStyledStringDescriptor(uint8_t* buffer, size_t bufferSize, ArkUI_StyledString_Descriptor* descriptor)
```

**描述**

将包含属性字符串信息的字节数组反序列化为属性字符串。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint8\_t\* buffer | 待反序列化的字节数组。 |
| size\_t bufferSize | 字节数组长度。 |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向ArkUI\_StyledString\_Descriptor对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常，可能原因包括传入参数为空指针或参数值不在有效范围内，请检查参数是否有效。 |

### OH\_ArkUI\_MarshallStyledStringDescriptor()

```c
int32_t OH_ArkUI_MarshallStyledStringDescriptor(uint8_t* buffer, size_t bufferSize, ArkUI_StyledString_Descriptor* descriptor, size_t* resultSize)
```

**描述**

将属性字符串信息序列化为字节数组。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint8\_t\* buffer | 字节数组，用于存储属性字符串序列化后的数据。 |
| size\_t bufferSize | 字节数组长度。 |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向ArkUI\_StyledString\_Descriptor对象的指针。 |
| size\_t\* resultSize | 属性字符串转换后的字节数组实际长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常，可能原因包括传入参数为空指针或参数值不在有效范围内，请检查参数是否有效。  [ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 属性字符串无效，可能原因包括属性字符串对象已被销毁或未正确创建，请确保使用有效的属性字符串对象。 |

### OH\_ArkUI\_ConvertToHtml()

```c
const char* OH_ArkUI_ConvertToHtml(ArkUI_StyledString_Descriptor* descriptor)
```

**描述**

将属性字符串信息转换成HTML。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向ArkUI\_StyledString\_Descriptor对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | HTML。该指针由内部管理，在[OH\_ArkUI\_StyledString\_Descriptor\_Destroy()](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_destroy)时释放。 |

### OH\_ArkUI\_StyledString\_Descriptor\_CreateWithString()

```c
ArkUI_StyledString_Descriptor* OH_ArkUI_StyledString_Descriptor_CreateWithString(const char* value, const OH_ArkUI_SpanStyle** styles, int32_t length)
```

**描述**

创建纯文本内容类型的[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_StyledString\_Descriptor\_Destroy](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_destroy)销毁它。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* value | 属性字符串的纯文本内容。 |
| const [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\*\* styles | 属性字符串的样式集合，指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象数组的指针。数组中每个OH\_ArkUI\_SpanStyle对象需先调用[OH\_ArkUI\_SpanStyle\_SetStart](capi-styled-string-h.md#oh_arkui_spanstyle_setstart)和[OH\_ArkUI\_SpanStyle\_SetLength](capi-styled-string-h.md#oh_arkui_spanstyle_setlength)设置样式作用的范围。 |
| int32\_t length | 样式对象数组的数量。取值范围[0, +∞)，需与传入的styles指针所指向的数组实际长度一致。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* | 指向创建的[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。  如果结果为空指针，表示创建失败，失败的原因是传入参数为空指针或参数值无效。 |

### OH\_ArkUI\_StyledString\_Descriptor\_CreateWithImageAttachment()

```c
ArkUI_StyledString_Descriptor* OH_ArkUI_StyledString_Descriptor_CreateWithImageAttachment(const OH_ArkUI_ImageAttachment* value)
```

**描述**

创建图片内容类型的[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_StyledString\_Descriptor\_Destroy](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_destroy)销毁它。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* value | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* | 指向创建的[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。  如果结果为空指针，表示创建失败，失败的原因是传入参数为空指针或参数值无效。 |

### OH\_ArkUI\_StyledString\_Descriptor\_CreateWithCustomSpan()

```c
ArkUI_StyledString_Descriptor* OH_ArkUI_StyledString_Descriptor_CreateWithCustomSpan(const OH_ArkUI_CustomSpan* value)
```

**描述**

创建自定义绘制Span内容类型的[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_StyledString\_Descriptor\_Destroy](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_destroy)销毁它。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_CustomSpan](capi-arkui-nativemodule-oh-arkui-customspan.md)\* value | 指向[OH\_ArkUI\_CustomSpan](capi-arkui-nativemodule-oh-arkui-customspan.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* | 指向创建的[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。  如果结果为空指针，表示创建失败，失败的原因是传入参数为空指针或参数值无效。 |

### OH\_ArkUI\_StyledString\_Descriptor\_GetLength()

```c
ArkUI_ErrorCode OH_ArkUI_StyledString_Descriptor_GetLength(const ArkUI_StyledString_Descriptor* descriptor, int32_t* length)
```

**描述**

获取属性字符串的字符长度。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |
| int32\_t\* length | 输出参数，用于接收属性字符串的字符长度结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常，可能原因包括descriptor为空指针或length为空指针，请检查参数是否有效。  [ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 属性字符串无效，可能原因包括属性字符串对象已被销毁或未正确创建，请确保使用有效的属性字符串对象。 |

### OH\_ArkUI\_StyledString\_Descriptor\_GetString()

```c
ArkUI_ErrorCode OH_ArkUI_StyledString_Descriptor_GetString(const ArkUI_StyledString_Descriptor* descriptor, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取属性字符串的文本内容。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |
| char\* buffer | 文本内容写入内存的缓冲区，内存空间需由开发者分配。 |
| int32\_t bufferSize | 缓冲区大小。 |
| int32\_t\* writeLength | 返回值为[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时表示实际写入缓冲区的长度。  返回值为[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时表示字符串完整写入缓冲区所需要的最小长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常，可能原因包括descriptor为空指针、buffer为空指针或writeLength为空指针，请检查参数是否有效。  [ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 属性字符串无效，可能原因包括属性字符串对象已被销毁或未正确创建，请确保使用有效的属性字符串对象。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 缓冲区大小不足，当提供的bufferSize小于实际需要写入的数据长度时返回此错误码。处理步骤：通过writeLength参数获取所需最小缓冲区大小，重新分配足够大小的缓冲区后再次调用。 |

### OH\_ArkUI\_StyledString\_Descriptor\_IsEqual()

```c
ArkUI_ErrorCode OH_ArkUI_StyledString_Descriptor_IsEqual(const ArkUI_StyledString_Descriptor* firstDescriptor, const ArkUI_StyledString_Descriptor* secondDescriptor, bool* isEqual)
```

**描述**

判断两个属性字符串是否相同。当属性字符串的文本及样式均一致，视为相同。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* firstDescriptor | 指向[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |
| const [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* secondDescriptor | 指向另一个[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |
| bool\* isEqual | 两个属性字符串是否相同。true表示相同；false表示不相同。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 属性字符串无效。 |

### OH\_ArkUI\_StyledString\_Descriptor\_SubStyledString()

```c
ArkUI_ErrorCode OH_ArkUI_StyledString_Descriptor_SubStyledString(const ArkUI_StyledString_Descriptor* descriptor, ArkUI_StyledString_Descriptor* subDescriptor, uint32_t start, uint32_t length)
```

**描述**

获取属性字符串的子属性字符串。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* subDescriptor | 指向[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)子属性字符串对象的指针。 |
| uint32\_t start | 子属性字符串的起始位置。取值范围[0, 属性字符串的字符长度]，超出范围时返回ARKUI\_ERROR\_CODE\_PARAM\_INVALID。 |
| uint32\_t length | 子属性字符串的字符长度。取值范围[0, 属性字符串的字符长度与参数start的差值]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 属性字符串无效。 |

### OH\_ArkUI\_StyledString\_Descriptor\_GetStyles()

```c
ArkUI_ErrorCode OH_ArkUI_StyledString_Descriptor_GetStyles(const ArkUI_StyledString_Descriptor* descriptor, uint32_t start, uint32_t length, OH_ArkUI_StyledStringKey styledKey, OH_ArkUI_SpanStyle** styles, uint32_t stylesSize, uint32_t* writeLength)
```

**描述**

获取属性字符串指定范围内的样式集合。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |
| uint32\_t start | 指定范围的起始位置。取值范围[0, 属性字符串的字符长度]。 |
| uint32\_t length | 指定范围的长度。取值范围[0, 属性字符串的字符长度与参数start的差值]。 |
| [OH\_ArkUI\_StyledStringKey](capi-styled-string-h.md#oh_arkui_styledstringkey) styledKey | 需要获取的指定样式类型，取值为[OH\_ArkUI\_StyledStringKey](capi-styled-string-h.md#oh_arkui_styledstringkey)中的枚举。 |
| [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\*\* styles | 指向样式对象数组的缓冲区指针。 |
| uint32\_t stylesSize | 样式对象数组的缓冲区大小。 |
| uint32\_t\* writeLength | 属性字符串中获取到的样式对象的数组的实际大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 属性字符串无效。 |

### OH\_ArkUI\_StyledString\_Descriptor\_FromHtml()

```c
ArkUI_ErrorCode OH_ArkUI_StyledString_Descriptor_FromHtml(ArkUI_StyledString_Descriptor* descriptor, const char* html)
```

**描述**

将HTML格式字符串转换成属性字符串。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |
| const char\* html | 待转换为属性字符串的HTML格式字符串，当前支持转换的HTML标签范围：<p>、<span>、<img>、<br>、<strong>、<b>、<a>、<i>、<em>、<s>、<u>、<del>、<sup>、<sub>、<cite>、<dfn>、<small>、<h1>、<h2>、<h3>、<h4>、<h5>、<h6>、<ol>、<ul>、<li>。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 属性字符串无效。 |

### OH\_ArkUI\_StyledString\_Descriptor\_ReplaceString()

```c
ArkUI_ErrorCode OH_ArkUI_StyledString_Descriptor_ReplaceString(ArkUI_StyledString_Descriptor* descriptor, uint32_t start, uint32_t length, const char* string)
```

**描述**

替换属性字符串指定范围的文本。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |
| uint32\_t start | 指定范围的起始位置。取值范围[0, 属性字符串的字符长度]。 |
| uint32\_t length | 指定范围的长度。取值范围[0, 属性字符串的字符长度与参数start的差值]。 |
| const char\* string | 替换的新文本内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 属性字符串无效。 |

### OH\_ArkUI\_StyledString\_Descriptor\_InsertString()

```c
ArkUI_ErrorCode OH_ArkUI_StyledString_Descriptor_InsertString(ArkUI_StyledString_Descriptor* descriptor, uint32_t start, const char* string)
```

**描述**

在属性字符串的指定位置插入文本。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |
| uint32\_t start | 插入位置。取值范围[0, 属性字符串的字符长度]。 |
| const char\* string | 插入的新文本内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 属性字符串无效。 |

### OH\_ArkUI\_StyledString\_Descriptor\_RemoveString()

```c
ArkUI_ErrorCode OH_ArkUI_StyledString_Descriptor_RemoveString(ArkUI_StyledString_Descriptor* descriptor, uint32_t start, uint32_t length)
```

**描述**

移除属性字符串指定范围的文本。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |
| uint32\_t start | 指定范围的起始位置。取值范围[0, 属性字符串的字符长度]。 |
| uint32\_t length | 指定范围的字符长度。取值范围[0, 属性字符串的字符长度与参数start的差值]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 属性字符串无效。 |

### OH\_ArkUI\_StyledString\_Descriptor\_ReplaceStyle()

```c
ArkUI_ErrorCode OH_ArkUI_StyledString_Descriptor_ReplaceStyle(ArkUI_StyledString_Descriptor* descriptor, const OH_ArkUI_SpanStyle* spanStyle)
```

**描述**

替换属性字符串指定范围内的样式。与[OH\_ArkUI\_StyledString\_Descriptor\_SetStyle](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_setstyle)的区别：ReplaceStyle会清除指定范围内所有类型的已有样式后设置新样式；SetStyle为指定范围设置样式，只替换同类型的已有样式，不影响其他类型的样式。建议需要完全替换已有样式时使用ReplaceStyle，需要叠加设置样式时使用SetStyle。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |
| const [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。  需先调用[OH\_ArkUI\_SpanStyle\_SetStart](capi-styled-string-h.md#oh_arkui_spanstyle_setstart)和[OH\_ArkUI\_SpanStyle\_SetLength](capi-styled-string-h.md#oh_arkui_spanstyle_setlength)在该对象中设置目标范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 属性字符串无效。 |

### OH\_ArkUI\_StyledString\_Descriptor\_SetStyle()

```c
ArkUI_ErrorCode OH_ArkUI_StyledString_Descriptor_SetStyle(ArkUI_StyledString_Descriptor* descriptor, const OH_ArkUI_SpanStyle* spanStyle)
```

**描述**

为属性字符串指定范围设置新样式。与[OH\_ArkUI\_StyledString\_Descriptor\_ReplaceStyle](capi-styled-string-h.md#oh_arkui_styledstring_descriptor_replacestyle)的区别：SetStyle为指定范围设置样式，只替换同类型的已有样式，不影响其他类型的样式，适用于叠加设置样式的场景；ReplaceStyle会清除指定范围内所有类型的已有样式后设置新样式，适用于完全替换已有样式的场景。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |
| const [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。需先调用[OH\_ArkUI\_SpanStyle\_SetStart](capi-styled-string-h.md#oh_arkui_spanstyle_setstart)和[OH\_ArkUI\_SpanStyle\_SetLength](capi-styled-string-h.md#oh_arkui_spanstyle_setlength)在该对象中设置目标范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 属性字符串无效。 |

### OH\_ArkUI\_StyledString\_Descriptor\_RemoveStyle()

```c
ArkUI_ErrorCode OH_ArkUI_StyledString_Descriptor_RemoveStyle(ArkUI_StyledString_Descriptor* descriptor, uint32_t start, uint32_t length, OH_ArkUI_StyledStringKey styledKey)
```

**描述**

清除属性字符串指定范围内的指定类型样式。

**说明** 

被清除后属性样式取TextEditor组件对应类型属性的默认值（如清除TextStyle后取TextEditor的字体默认样式）。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |
| uint32\_t start | 指定范围的起始位置。取值范围[0, 属性字符串的字符长度]。 |
| uint32\_t length | 指定范围的长度。取值范围[0, 属性字符串的字符长度与参数start的差值]。 |
| [OH\_ArkUI\_StyledStringKey](capi-styled-string-h.md#oh_arkui_styledstringkey) styledKey | 样式类型枚举值，取值为[OH\_ArkUI\_StyledStringKey](capi-styled-string-h.md#oh_arkui_styledstringkey)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 属性字符串无效。 |

### OH\_ArkUI\_StyledString\_Descriptor\_ClearStyles()

```c
ArkUI_ErrorCode OH_ArkUI_StyledString_Descriptor_ClearStyles(ArkUI_StyledString_Descriptor* descriptor)
```

**描述**

清除属性字符串对象的所有样式。

**说明** 

被清除后属性样式取TextEditor组件对应类型属性的默认值（如清除TextStyle后取TextEditor的字体默认样式）。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 属性字符串无效。 |

### OH\_ArkUI\_StyledString\_Descriptor\_ReplaceStyledString()

```c
ArkUI_ErrorCode OH_ArkUI_StyledString_Descriptor_ReplaceStyledString(ArkUI_StyledString_Descriptor* descriptor, uint32_t start, uint32_t length, const ArkUI_StyledString_Descriptor* other)
```

**描述**

替换指定范围的属性字符串。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |
| uint32\_t start | 指定范围的起始位置。取值范围[0, 属性字符串的字符长度]。 |
| uint32\_t length | 指定范围的长度。取值范围[0, 属性字符串的字符长度与参数start的差值]。 |
| const [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* other | 指向新的[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 属性字符串无效。 |

### OH\_ArkUI\_StyledString\_Descriptor\_InsertStyledString()

```c
ArkUI_ErrorCode OH_ArkUI_StyledString_Descriptor_InsertStyledString(ArkUI_StyledString_Descriptor* descriptor, uint32_t start, const ArkUI_StyledString_Descriptor* other)
```

**描述**

在属性字符串的指定位置插入新的属性字符串。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |
| uint32\_t start | 插入位置。取值范围[0, 属性字符串的字符长度]。 |
| const [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* other | 指向新的[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 属性字符串无效。 |

### OH\_ArkUI\_StyledString\_Descriptor\_AppendStyledString()

```c
ArkUI_ErrorCode OH_ArkUI_StyledString_Descriptor_AppendStyledString(ArkUI_StyledString_Descriptor* descriptor, const ArkUI_StyledString_Descriptor* other)
```

**描述**

在属性字符串的末尾追加新的属性字符串。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |
| const [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* other | 指向新的[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 属性字符串无效。 |

### OH\_ArkUI\_StyledString\_Descriptor\_InvalidateCustomSpan()

```c
ArkUI_ErrorCode OH_ArkUI_StyledString_Descriptor_InvalidateCustomSpan(const ArkUI_StyledString_Descriptor* descriptor)
```

**描述**

主动刷新属性字符串中的自定义绘制Span。

**说明** 

调用该接口会立即触发通过[OH\_ArkUI\_CustomSpan\_RegisterOnDrawCallback](capi-styled-string-h.md#oh_arkui_customspan_registerondrawcallback)注册在自定义绘制Span上的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 属性字符串无效。 |

### OH\_ArkUI\_TextStyle\_Create()

```c
OH_ArkUI_TextStyle* OH_ArkUI_TextStyle_Create()
```

**描述**

创建[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_TextStyle\_Destroy](capi-styled-string-h.md#oh_arkui_textstyle_destroy)销毁它。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)\* | 指向[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象的指针，用于定义文本字体样式。 |

### OH\_ArkUI\_TextStyle\_Destroy()

```c
void OH_ArkUI_TextStyle_Destroy(OH_ArkUI_TextStyle* textStyle)
```

**描述**

释放[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象占用的内存。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)\* textStyle | 指向[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象的指针。 |

### OH\_ArkUI\_TextStyle\_SetFontColor()

```c
ArkUI_ErrorCode OH_ArkUI_TextStyle_SetFontColor(OH_ArkUI_TextStyle* textStyle, uint32_t fontColor)
```

**描述**

设置文本字体样式中的字体颜色。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)\* textStyle | 指向[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象的指针。 |
| uint32\_t fontColor | 字体颜色，0xARGB格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextStyle\_GetFontColor()

```c
ArkUI_ErrorCode OH_ArkUI_TextStyle_GetFontColor(const OH_ArkUI_TextStyle* textStyle, uint32_t* fontColor)
```

**描述**

获取文本字体样式中的字体颜色。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)\* textStyle | 指向[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象的指针。 |
| uint32\_t\* fontColor | 字体颜色，0xARGB格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextStyle\_SetFontFamily()

```c
ArkUI_ErrorCode OH_ArkUI_TextStyle_SetFontFamily(OH_ArkUI_TextStyle* textStyle, const char* fontFamily)
```

**描述**

设置文本字体样式中的字体族。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)\* textStyle | 指向[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象的指针。 |
| const char\* fontFamily | 字体族。存放待设置的字体名称，不同字体名称通过逗号拼接。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextStyle\_GetFontFamily()

```c
ArkUI_ErrorCode OH_ArkUI_TextStyle_GetFontFamily(const OH_ArkUI_TextStyle* textStyle, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取文本字体样式中的字体族。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)\* textStyle | 指向[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象的指针。 |
| char\* buffer | 字体族内容写入内存的缓冲区，内存空间需由开发者分配。 |
| int32\_t bufferSize | 缓冲区最多可写入的字符的数量。 |
| int32\_t\* writeLength | 返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时，表示实际写入缓冲区的字符串长度。  返回[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时，表示字符串完整写入缓冲区所需要的最小长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 缓冲区大小不足，当提供的bufferSize小于实际需要写入的数据长度时返回此错误码。处理步骤：通过writeLength参数获取所需最小缓冲区大小，重新分配足够大小的缓冲区后再次调用。 |

### OH\_ArkUI\_TextStyle\_SetFontSize()

```c
ArkUI_ErrorCode OH_ArkUI_TextStyle_SetFontSize(OH_ArkUI_TextStyle* textStyle, float fontSize)
```

**描述**

设置文本字体样式中的字体大小。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)\* textStyle | 指向[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象的指针。 |
| float fontSize | 字体大小，单位为vp。取值范围[0, +∞)。传入负数时使用默认字体大小。默认值为16vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextStyle\_GetFontSize()

```c
ArkUI_ErrorCode OH_ArkUI_TextStyle_GetFontSize(const OH_ArkUI_TextStyle* textStyle, float* fontSize)
```

**描述**

获取文本字体样式中的字体大小。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)\* textStyle | 指向[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象的指针。 |
| float\* fontSize | 字体大小，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextStyle\_SetFontWeight()

```c
ArkUI_ErrorCode OH_ArkUI_TextStyle_SetFontWeight(OH_ArkUI_TextStyle* textStyle, uint32_t fontWeight)
```

**描述**

设置文本字体样式中的字体粗细。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)\* textStyle | 指向[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象的指针。 |
| uint32\_t fontWeight | 字体粗细。取值为[ArkUI\_FontWeight](capi-text-h.md#arkui_fontweight)中的枚举值，默认值为ARKUI\_FONT\_WEIGHT\_W400。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextStyle\_GetFontWeight()

```c
ArkUI_ErrorCode OH_ArkUI_TextStyle_GetFontWeight(const OH_ArkUI_TextStyle* textStyle, uint32_t* fontWeight)
```

**描述**

获取文本字体样式中的字体粗细。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)\* textStyle | 指向[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象的指针。 |
| uint32\_t\* fontWeight | 字体粗细。取值为[ArkUI\_FontWeight](capi-text-h.md#arkui_fontweight)中的枚举值，默认值为ARKUI\_FONT\_WEIGHT\_W400。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextStyle\_SetFontStyle()

```c
ArkUI_ErrorCode OH_ArkUI_TextStyle_SetFontStyle(OH_ArkUI_TextStyle* textStyle, ArkUI_FontStyle fontStyle)
```

**描述**

设置文本字体样式中的字体风格。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)\* textStyle | 指向[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象的指针。 |
| [ArkUI\_FontStyle](capi-text-h.md#arkui_fontstyle) fontStyle | 字体风格。取值为[ArkUI\_FontStyle](capi-text-h.md#arkui_fontstyle)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextStyle\_GetFontStyle()

```c
ArkUI_ErrorCode OH_ArkUI_TextStyle_GetFontStyle(const OH_ArkUI_TextStyle* textStyle, ArkUI_FontStyle* fontStyle)
```

**描述**

获取文本字体样式中的字体风格。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)\* textStyle | 指向[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象的指针。 |
| [ArkUI\_FontStyle](capi-text-h.md#arkui_fontstyle)\* fontStyle | 字体风格。取值为[ArkUI\_FontStyle](capi-text-h.md#arkui_fontstyle)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextStyle\_SetStrokeWidth()

```c
ArkUI_ErrorCode OH_ArkUI_TextStyle_SetStrokeWidth(OH_ArkUI_TextStyle* textStyle, float strokeWidth)
```

**描述**

设置文本字体样式中的描边宽度。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)\* textStyle | 指向[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象的指针。 |
| float strokeWidth | 描边宽度，取值范围(-∞, +∞)，单位为vp。值小于0时为实体字，大于0时为轮廓字，等于0时无描边效果。默认值：0vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextStyle\_GetStrokeWidth()

```c
ArkUI_ErrorCode OH_ArkUI_TextStyle_GetStrokeWidth(const OH_ArkUI_TextStyle* textStyle, float* strokeWidth)
```

**描述**

获取文本字体样式中的描边宽度。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)\* textStyle | 指向[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象的指针。 |
| float\* strokeWidth | 描边宽度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextStyle\_SetStrokeColor()

```c
ArkUI_ErrorCode OH_ArkUI_TextStyle_SetStrokeColor(OH_ArkUI_TextStyle* textStyle, uint32_t strokeColor)
```

**描述**

设置文本字体样式中的描边颜色。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)\* textStyle | 指向[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象的指针。 |
| uint32\_t strokeColor | 描边颜色，0xARGB格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextStyle\_GetStrokeColor()

```c
ArkUI_ErrorCode OH_ArkUI_TextStyle_GetStrokeColor(const OH_ArkUI_TextStyle* textStyle, uint32_t* strokeColor)
```

**描述**

获取文本字体样式中的描边颜色。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)\* textStyle | 指向[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象的指针。 |
| uint32\_t\* strokeColor | 描边颜色，0xARGB格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextStyle\_SetSuperscript()

```c
ArkUI_ErrorCode OH_ArkUI_TextStyle_SetSuperscript(OH_ArkUI_TextStyle* textStyle, OH_ArkUI_SuperscriptStyle superscript)
```

**描述**

设置文本字体样式中的上下标样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)\* textStyle | 指向[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象的指针。 |
| [OH\_ArkUI\_SuperscriptStyle](capi-styled-string-h.md#oh_arkui_superscriptstyle) superscript | 上下标样式。取值为[OH\_ArkUI\_SuperscriptStyle](capi-styled-string-h.md#oh_arkui_superscriptstyle)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextStyle\_GetSuperscript()

```c
ArkUI_ErrorCode OH_ArkUI_TextStyle_GetSuperscript(const OH_ArkUI_TextStyle* textStyle, OH_ArkUI_SuperscriptStyle* superscript)
```

**描述**

获取文本字体样式中的上下标样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)\* textStyle | 指向[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象的指针。 |
| [OH\_ArkUI\_SuperscriptStyle](capi-styled-string-h.md#oh_arkui_superscriptstyle)\* superscript | 上下标样式。取值为[OH\_ArkUI\_SuperscriptStyle](capi-styled-string-h.md#oh_arkui_superscriptstyle)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_Create()

```c
OH_ArkUI_SpanStyle* OH_ArkUI_SpanStyle_Create()
```

**描述**

创建[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_SpanStyle\_Destroy](capi-styled-string-h.md#oh_arkui_spanstyle_destroy)销毁它。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针，用于设置属性字符串样式的作用范围和具体样式。 |

### OH\_ArkUI\_SpanStyle\_Destroy()

```c
void OH_ArkUI_SpanStyle_Destroy(OH_ArkUI_SpanStyle* spanStyle)
```

**描述**

释放[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象占用的内存。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |

### OH\_ArkUI\_SpanStyle\_GetStyledKey()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_GetStyledKey(const OH_ArkUI_SpanStyle* spanStyle, OH_ArkUI_StyledStringKey* styledKey)
```

**描述**

获取属性字符串样式对象的样式类型。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| [OH\_ArkUI\_StyledStringKey](capi-styled-string-h.md#oh_arkui_styledstringkey)\* styledKey | 样式类型的枚举值。取值为[OH\_ArkUI\_StyledStringKey](capi-styled-string-h.md#oh_arkui_styledstringkey)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_SetStart()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_SetStart(OH_ArkUI_SpanStyle* spanStyle, int32_t start)
```

**描述**

设置属性字符串样式对象的起始位置。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| int32\_t start | 属性字符串样式对象的起始位置，需与[OH\_ArkUI\_SpanStyle\_SetLength](capi-styled-string-h.md#oh_arkui_spanstyle_setlength)配合使用以指定样式作用的范围。取值范围[0, 属性字符串的长度]，超出范围时按0处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_GetStart()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_GetStart(const OH_ArkUI_SpanStyle* spanStyle, int32_t* start)
```

**描述**

获取属性字符串样式对象的起始位置。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| int32\_t\* start | 属性字符串样式对象的起始位置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_SetLength()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_SetLength(OH_ArkUI_SpanStyle* spanStyle, int32_t length)
```

**描述**

设置属性字符串样式对象的长度。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| int32\_t length | 属性字符串样式对象的长度，需与[OH\_ArkUI\_SpanStyle\_SetStart](capi-styled-string-h.md#oh_arkui_spanstyle_setstart)配合使用以指定样式作用的范围。取值范围[0, 属性字符串的长度与参数start的差值]。当length的值小于0或超出字符串长度与start的差值时，按字符串长度与start的差值处理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_GetLength()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_GetLength(const OH_ArkUI_SpanStyle* spanStyle, int32_t* length)
```

**描述**

获取属性字符串样式对象的长度。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| int32\_t\* length | 属性字符串样式对象的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_SetTextStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_SetTextStyle(OH_ArkUI_SpanStyle* spanStyle, const OH_ArkUI_TextStyle* textStyle)
```

**描述**

设置属性字符串样式对象的文本字体样式。

**说明** 

此操作会替换[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象中已设置的其他类型样式。一个SpanStyle对象只能持有一种类型的样式，设置新类型样式后，之前已设置的其他类型样式（如已设置的GestureStyle、ParagraphStyle等）将被清除。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| const [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)\* textStyle | 指向[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_GetTextStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_GetTextStyle(const OH_ArkUI_SpanStyle* spanStyle, OH_ArkUI_TextStyle* textStyle)
```

**描述**

获取属性字符串样式对象的文本字体样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| [OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)\* textStyle | 指向[OH\_ArkUI\_TextStyle](capi-arkui-nativemodule-oh-arkui-textstyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_SetParagraphStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_SetParagraphStyle(OH_ArkUI_SpanStyle* spanStyle, const OH_ArkUI_ParagraphStyle* paragraphStyle)
```

**描述**

设置属性字符串样式对象的段落样式。

**说明** 

* 此操作会替换[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象中已设置的其他类型样式。一个SpanStyle对象只能持有一种类型的样式，设置新类型样式后，之前已设置的其他类型样式（如已设置的TextStyle、GestureStyle等）将被清除。
* 每个段落的段落样式按首个占位设置的段落样式生效，未设置时，段落按被绑定组件的段落样式生效。
* 在API版本26.0.0之前，如果属性字符串段落内首个占位为OH\_ArkUI\_CustomSpan或OH\_ArkUI\_ImageAttachment时，设置在该段落上的段落样式不生效。从API版本26.0.0开始，设置段落样式生效。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| const [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_GetParagraphStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_GetParagraphStyle(const OH_ArkUI_SpanStyle* spanStyle, OH_ArkUI_ParagraphStyle* paragraphStyle)
```

**描述**

获取属性字符串样式对象的段落样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_SetGestureStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_SetGestureStyle(OH_ArkUI_SpanStyle* spanStyle, const OH_ArkUI_GestureStyle* gestureStyle)
```

**描述**

设置属性字符串样式对象的事件手势样式。

**说明** 

此操作会替换[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象中已设置的其他类型样式。一个SpanStyle对象只能持有一种类型的样式，设置新类型样式后，之前已设置的其他类型样式（如已设置的TextStyle、ParagraphStyle等）将被清除。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| const [OH\_ArkUI\_GestureStyle](capi-arkui-nativemodule-oh-arkui-gesturestyle.md)\* gestureStyle | 指向[OH\_ArkUI\_GestureStyle](capi-arkui-nativemodule-oh-arkui-gesturestyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_GetGestureStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_GetGestureStyle(const OH_ArkUI_SpanStyle* spanStyle, OH_ArkUI_GestureStyle* gestureStyle)
```

**描述**

获取属性字符串样式对象的事件手势样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| [OH\_ArkUI\_GestureStyle](capi-arkui-nativemodule-oh-arkui-gesturestyle.md)\* gestureStyle | 指向[OH\_ArkUI\_GestureStyle](capi-arkui-nativemodule-oh-arkui-gesturestyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_SetTextShadowStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_SetTextShadowStyle(OH_ArkUI_SpanStyle* spanStyle, const OH_ArkUI_TextShadowStyle* textShadowStyle)
```

**描述**

设置属性字符串样式对象的文本阴影样式。

**说明** 

此操作会替换[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象中已设置的其他类型样式。一个SpanStyle对象只能持有一种类型的样式，设置新类型样式后，之前已设置的其他类型样式（如已设置的GestureStyle、ParagraphStyle等）将被清除。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| const [OH\_ArkUI\_TextShadowStyle](capi-arkui-nativemodule-oh-arkui-textshadowstyle.md)\* textShadowStyle | 指向[OH\_ArkUI\_TextShadowStyle](capi-arkui-nativemodule-oh-arkui-textshadowstyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_GetTextShadowStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_GetTextShadowStyle(const OH_ArkUI_SpanStyle* spanStyle, OH_ArkUI_TextShadowStyle* textShadowStyle)
```

**描述**

获取属性字符串样式对象的文本阴影样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| [OH\_ArkUI\_TextShadowStyle](capi-arkui-nativemodule-oh-arkui-textshadowstyle.md)\* textShadowStyle | 指向[OH\_ArkUI\_TextShadowStyle](capi-arkui-nativemodule-oh-arkui-textshadowstyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_SetDecorationStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_SetDecorationStyle(OH_ArkUI_SpanStyle* spanStyle, const OH_ArkUI_DecorationStyle* decorationStyle)
```

**描述**

设置属性字符串样式对象的文本装饰线样式。

**说明** 

此操作会替换[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象中已设置的其他类型样式。一个SpanStyle对象只能持有一种类型的样式，设置新类型样式后，之前已设置的其他类型样式（如已设置的GestureStyle、ParagraphStyle等）将被清除。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| const [OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)\* decorationStyle | 指向[OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_GetDecorationStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_GetDecorationStyle(const OH_ArkUI_SpanStyle* spanStyle, OH_ArkUI_DecorationStyle* decorationStyle)
```

**描述**

获取属性字符串样式对象的文本装饰线样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| [OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)\* decorationStyle | 指向[OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_SetBaselineOffsetStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_SetBaselineOffsetStyle(OH_ArkUI_SpanStyle* spanStyle, const OH_ArkUI_BaselineOffsetStyle* baselineOffsetStyle)
```

**描述**

设置属性字符串样式对象的基线偏移量样式。

**说明** 

此操作会替换[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象中已设置的其他类型样式。一个SpanStyle对象只能持有一种类型的样式，设置新类型样式后，之前已设置的其他类型样式（如已设置的GestureStyle、ParagraphStyle等）将被清除。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| const [OH\_ArkUI\_BaselineOffsetStyle](capi-arkui-nativemodule-oh-arkui-baselineoffsetstyle.md)\* baselineOffsetStyle | 指向[OH\_ArkUI\_BaselineOffsetStyle](capi-arkui-nativemodule-oh-arkui-baselineoffsetstyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_GetBaselineOffsetStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_GetBaselineOffsetStyle(const OH_ArkUI_SpanStyle* spanStyle, OH_ArkUI_BaselineOffsetStyle* baselineOffsetStyle)
```

**描述**

获取属性字符串样式对象的基线偏移量样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| [OH\_ArkUI\_BaselineOffsetStyle](capi-arkui-nativemodule-oh-arkui-baselineoffsetstyle.md)\* baselineOffsetStyle | 指向[OH\_ArkUI\_BaselineOffsetStyle](capi-arkui-nativemodule-oh-arkui-baselineoffsetstyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_SetLetterSpacingStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_SetLetterSpacingStyle(OH_ArkUI_SpanStyle* spanStyle, const OH_ArkUI_LetterSpacingStyle* letterSpacingStyle)
```

**描述**

设置属性字符串样式对象的字符间距样式。

**说明** 

此操作会替换[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象中已设置的其他类型样式。一个SpanStyle对象只能持有一种类型的样式，设置新类型样式后，之前已设置的其他类型样式（如已设置的GestureStyle、ParagraphStyle等）将被清除。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| const [OH\_ArkUI\_LetterSpacingStyle](capi-arkui-nativemodule-oh-arkui-letterspacingstyle.md)\* letterSpacingStyle | 指向[OH\_ArkUI\_LetterSpacingStyle](capi-arkui-nativemodule-oh-arkui-letterspacingstyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_GetLetterSpacingStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_GetLetterSpacingStyle(const OH_ArkUI_SpanStyle* spanStyle, OH_ArkUI_LetterSpacingStyle* letterSpacingStyle)
```

**描述**

获取属性字符串样式对象的字符间距样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| [OH\_ArkUI\_LetterSpacingStyle](capi-arkui-nativemodule-oh-arkui-letterspacingstyle.md)\* letterSpacingStyle | 指向[OH\_ArkUI\_LetterSpacingStyle](capi-arkui-nativemodule-oh-arkui-letterspacingstyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_SetLineHeightStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_SetLineHeightStyle(OH_ArkUI_SpanStyle* spanStyle, const OH_ArkUI_LineHeightStyle* lineHeightStyle)
```

**描述**

设置属性字符串样式对象的行高样式。

**说明** 

此操作会替换[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象中已设置的其他类型样式。一个SpanStyle对象只能持有一种类型的样式，设置新类型样式后，之前已设置的其他类型样式（如已设置的GestureStyle、ParagraphStyle等）将被清除。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| const [OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md)\* lineHeightStyle | 指向[OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_GetLineHeightStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_GetLineHeightStyle(const OH_ArkUI_SpanStyle* spanStyle, OH_ArkUI_LineHeightStyle* lineHeightStyle)
```

**描述**

获取属性字符串样式对象的行高样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| [OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md)\* lineHeightStyle | 指向[OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_SetUrlStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_SetUrlStyle(OH_ArkUI_SpanStyle* spanStyle, const OH_ArkUI_UrlStyle* urlStyle)
```

**描述**

设置属性字符串样式对象的超链接样式。

**说明** 

此操作会替换[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象中已设置的其他类型样式。一个SpanStyle对象只能持有一种类型的样式，设置新类型样式后，之前已设置的其他类型样式（如已设置的GestureStyle、ParagraphStyle等）将被清除。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| const [OH\_ArkUI\_UrlStyle](capi-arkui-nativemodule-oh-arkui-urlstyle.md)\* urlStyle | 指向[OH\_ArkUI\_UrlStyle](capi-arkui-nativemodule-oh-arkui-urlstyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_GetUrlStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_GetUrlStyle(const OH_ArkUI_SpanStyle* spanStyle, OH_ArkUI_UrlStyle* urlStyle)
```

**描述**

获取属性字符串样式对象的超链接样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| [OH\_ArkUI\_UrlStyle](capi-arkui-nativemodule-oh-arkui-urlstyle.md)\* urlStyle | 指向[OH\_ArkUI\_UrlStyle](capi-arkui-nativemodule-oh-arkui-urlstyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_SetBackgroundColorStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_SetBackgroundColorStyle(OH_ArkUI_SpanStyle* spanStyle, const OH_ArkUI_BackgroundColorStyle* backgroundColorStyle)
```

**描述**

设置属性字符串样式对象的背景颜色样式。

**说明** 

此操作会替换[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象中已设置的其他类型样式。一个SpanStyle对象只能持有一种类型的样式，设置新类型样式后，之前已设置的其他类型样式（如已设置的GestureStyle、ParagraphStyle等）将被清除。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| const [OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md)\* backgroundColorStyle | 指向[OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_GetBackgroundColorStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_GetBackgroundColorStyle(const OH_ArkUI_SpanStyle* spanStyle, OH_ArkUI_BackgroundColorStyle* backgroundColorStyle)
```

**描述**

获取属性字符串样式对象的背景颜色样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| [OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md)\* backgroundColorStyle | 指向[OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_SetUserDataSpan()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_SetUserDataSpan(OH_ArkUI_SpanStyle* spanStyle, const OH_ArkUI_UserDataSpan* userDataSpan)
```

**描述**

设置属性字符串样式对象的用户数据Span样式。

**说明** 

此操作会替换[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象中已设置的其他类型样式。一个SpanStyle对象只能持有一种类型的样式，设置新类型样式后，之前已设置的其他类型样式（如已设置的GestureStyle、ParagraphStyle等）将被清除。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| const [OH\_ArkUI\_UserDataSpan](capi-arkui-nativemodule-oh-arkui-userdataspan.md)\* userDataSpan | 指向[OH\_ArkUI\_UserDataSpan](capi-arkui-nativemodule-oh-arkui-userdataspan.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_GetUserDataSpan()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_GetUserDataSpan(const OH_ArkUI_SpanStyle* spanStyle, OH_ArkUI_UserDataSpan* userDataSpan)
```

**描述**

获取属性字符串样式对象的用户数据Span样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| [OH\_ArkUI\_UserDataSpan](capi-arkui-nativemodule-oh-arkui-userdataspan.md)\* userDataSpan | 指向[OH\_ArkUI\_UserDataSpan](capi-arkui-nativemodule-oh-arkui-userdataspan.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_SetCustomSpan()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_SetCustomSpan(OH_ArkUI_SpanStyle* spanStyle, const OH_ArkUI_CustomSpan* customSpan)
```

**描述**

设置属性字符串样式对象的自定义绘制Span样式。

**说明** 

此操作会替换[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象中已设置的其他类型样式。一个SpanStyle对象只能持有一种类型的样式，设置新类型样式后，之前已设置的其他类型样式（如已设置的GestureStyle、ParagraphStyle等）将被清除。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| const [OH\_ArkUI\_CustomSpan](capi-arkui-nativemodule-oh-arkui-customspan.md)\* customSpan | 指向[OH\_ArkUI\_CustomSpan](capi-arkui-nativemodule-oh-arkui-customspan.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_GetCustomSpan()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_GetCustomSpan(const OH_ArkUI_SpanStyle* spanStyle, OH_ArkUI_CustomSpan* customSpan)
```

**描述**

获取属性字符串样式对象的自定义绘制Span样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| [OH\_ArkUI\_CustomSpan](capi-arkui-nativemodule-oh-arkui-customspan.md)\* customSpan | 指向[OH\_ArkUI\_CustomSpan](capi-arkui-nativemodule-oh-arkui-customspan.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_SetImageAttachment()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_SetImageAttachment(OH_ArkUI_SpanStyle* spanStyle, const OH_ArkUI_ImageAttachment* imageAttachment)
```

**描述**

设置属性字符串样式对象的图片样式。

**说明** 

此操作会替换[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象中已设置的其他类型样式。一个SpanStyle对象只能持有一种类型的样式，设置新类型样式后，之前已设置的其他类型样式（如已设置的GestureStyle、ParagraphStyle等）将被清除。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| const [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_GetImageAttachment()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_GetImageAttachment(const OH_ArkUI_SpanStyle* spanStyle, OH_ArkUI_ImageAttachment* imageAttachment)
```

**描述**

获取属性字符串样式对象的图片样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LeadingMarginSpanDrawInfo\_Create()

```c
OH_ArkUI_LeadingMarginSpanDrawInfo* OH_ArkUI_LeadingMarginSpanDrawInfo_Create()
```

**描述**

创建[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_LeadingMarginSpanDrawInfo\_Destroy](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_destroy)销毁它。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)\* | 指向[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象的指针，用于定义段落缩进的自定义绘制信息。 |

### OH\_ArkUI\_LeadingMarginSpanDrawInfo\_Destroy()

```c
void OH_ArkUI_LeadingMarginSpanDrawInfo_Destroy(OH_ArkUI_LeadingMarginSpanDrawInfo* drawInfo)
```

**描述**

释放[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象占用的内存。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)\* drawInfo | 指向[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象的指针。 |

### OH\_ArkUI\_LeadingMarginSpanDrawInfo\_SetX()

```c
ArkUI_ErrorCode OH_ArkUI_LeadingMarginSpanDrawInfo_SetX(OH_ArkUI_LeadingMarginSpanDrawInfo* drawInfo, float x)
```

**描述**

设置段落缩进的自定义绘制信息对象中当前行相对于组件的水平偏移。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)\* drawInfo | 指向[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象的指针。 |
| float x | 当前行相对于组件的水平偏移，单位px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LeadingMarginSpanDrawInfo\_GetX()

```c
ArkUI_ErrorCode OH_ArkUI_LeadingMarginSpanDrawInfo_GetX(const OH_ArkUI_LeadingMarginSpanDrawInfo* drawInfo, float* x)
```

**描述**

获取段落缩进的自定义绘制信息对象中当前行相对于组件的水平偏移。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)\* drawInfo | 指向[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象的指针。 |
| float\* x | 当前行相对于组件的水平偏移，单位px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LeadingMarginSpanDrawInfo\_SetTop()

```c
ArkUI_ErrorCode OH_ArkUI_LeadingMarginSpanDrawInfo_SetTop(OH_ArkUI_LeadingMarginSpanDrawInfo* drawInfo, float top)
```

**描述**

设置段落缩进的自定义绘制信息对象中行顶与组件上边缘的距离。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)\* drawInfo | 指向[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象的指针。 |
| float top | 行顶与组件上边缘的距离，单位px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LeadingMarginSpanDrawInfo\_GetTop()

```c
ArkUI_ErrorCode OH_ArkUI_LeadingMarginSpanDrawInfo_GetTop(const OH_ArkUI_LeadingMarginSpanDrawInfo* drawInfo, float* top)
```

**描述**

获取段落缩进的自定义绘制信息对象中行顶与组件上边缘的距离。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)\* drawInfo | 指向[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象的指针。 |
| float\* top | 行顶与组件上边缘的距离，单位px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LeadingMarginSpanDrawInfo\_SetBottom()

```c
ArkUI_ErrorCode OH_ArkUI_LeadingMarginSpanDrawInfo_SetBottom(OH_ArkUI_LeadingMarginSpanDrawInfo* drawInfo, float bottom)
```

**描述**

设置段落缩进的自定义绘制信息对象中行底与组件上边缘的距离。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)\* drawInfo | 指向[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象的指针。 |
| float bottom | 行底与组件上边缘的距离，单位px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LeadingMarginSpanDrawInfo\_GetBottom()

```c
ArkUI_ErrorCode OH_ArkUI_LeadingMarginSpanDrawInfo_GetBottom(const OH_ArkUI_LeadingMarginSpanDrawInfo* drawInfo, float* bottom)
```

**描述**

获取段落缩进的自定义绘制信息对象中行底与组件上边缘的距离。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)\* drawInfo | 指向[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象的指针。 |
| float\* bottom | 行底与组件上边缘的距离，单位px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LeadingMarginSpanDrawInfo\_SetBaseline()

```c
ArkUI_ErrorCode OH_ArkUI_LeadingMarginSpanDrawInfo_SetBaseline(OH_ArkUI_LeadingMarginSpanDrawInfo* drawInfo, float baseline)
```

**描述**

设置段落缩进的自定义绘制信息对象中当前行的基线与组件上边缘的距离。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)\* drawInfo | 指向[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象的指针。 |
| float baseline | 当前行的基线与组件上边缘的距离，单位px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LeadingMarginSpanDrawInfo\_GetBaseline()

```c
ArkUI_ErrorCode OH_ArkUI_LeadingMarginSpanDrawInfo_GetBaseline(const OH_ArkUI_LeadingMarginSpanDrawInfo* drawInfo, float* baseline)
```

**描述**

获取段落缩进的自定义绘制信息对象中当前行的基线与组件上边缘的距离。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)\* drawInfo | 指向[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象的指针。 |
| float\* baseline | 当前行的基线与组件上边缘的距离，单位px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LeadingMarginSpanDrawInfo\_SetTextDirection()

```c
ArkUI_ErrorCode OH_ArkUI_LeadingMarginSpanDrawInfo_SetTextDirection(OH_ArkUI_LeadingMarginSpanDrawInfo* drawInfo, ArkUI_TextDirection direction)
```

**描述**

设置段落缩进的自定义绘制信息对象中文本内容的方向。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)\* drawInfo | 指向[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象的指针。 |
| [ArkUI\_TextDirection](capi-text-common-h.md#arkui_textdirection) direction | 文本内容的方向。取值为[ArkUI\_TextDirection](capi-text-common-h.md#arkui_textdirection)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LeadingMarginSpanDrawInfo\_GetTextDirection()

```c
ArkUI_ErrorCode OH_ArkUI_LeadingMarginSpanDrawInfo_GetTextDirection(const OH_ArkUI_LeadingMarginSpanDrawInfo* drawInfo, ArkUI_TextDirection* direction)
```

**描述**

获取段落缩进的自定义绘制信息对象中文本内容的方向。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)\* drawInfo | 指向[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象的指针。 |
| [ArkUI\_TextDirection](capi-text-common-h.md#arkui_textdirection)\* direction | 文本内容的方向。取值为[ArkUI\_TextDirection](capi-text-common-h.md#arkui_textdirection)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LeadingMarginSpanDrawInfo\_SetStart()

```c
ArkUI_ErrorCode OH_ArkUI_LeadingMarginSpanDrawInfo_SetStart(OH_ArkUI_LeadingMarginSpanDrawInfo* drawInfo, uint32_t start)
```

**描述**

设置段落缩进的自定义绘制信息对象中当前行的起始索引。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)\* drawInfo | 指向[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象的指针。 |
| uint32\_t start | 当前行的起始索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LeadingMarginSpanDrawInfo\_GetStart()

```c
ArkUI_ErrorCode OH_ArkUI_LeadingMarginSpanDrawInfo_GetStart(const OH_ArkUI_LeadingMarginSpanDrawInfo* drawInfo, uint32_t* start)
```

**描述**

获取段落缩进的自定义绘制信息对象中当前行的起始索引。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)\* drawInfo | 指向[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象的指针。 |
| uint32\_t\* start | 当前行的起始索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LeadingMarginSpanDrawInfo\_SetEnd()

```c
ArkUI_ErrorCode OH_ArkUI_LeadingMarginSpanDrawInfo_SetEnd(OH_ArkUI_LeadingMarginSpanDrawInfo* drawInfo, uint32_t end)
```

**描述**

设置段落缩进的自定义绘制信息对象中当前行的结束索引。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)\* drawInfo | 指向[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象的指针。 |
| uint32\_t end | 当前行的结束索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LeadingMarginSpanDrawInfo\_GetEnd()

```c
ArkUI_ErrorCode OH_ArkUI_LeadingMarginSpanDrawInfo_GetEnd(const OH_ArkUI_LeadingMarginSpanDrawInfo* drawInfo, uint32_t* end)
```

**描述**

获取段落缩进的自定义绘制信息对象中当前行的结束索引。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)\* drawInfo | 指向[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象的指针。 |
| uint32\_t\* end | 当前行的结束索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LeadingMarginSpanDrawInfo\_SetFirst()

```c
ArkUI_ErrorCode OH_ArkUI_LeadingMarginSpanDrawInfo_SetFirst(OH_ArkUI_LeadingMarginSpanDrawInfo* drawInfo, bool first)
```

**描述**

设置段落缩进的自定义绘制信息对象中当前行是否为段落的首行。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)\* drawInfo | 指向[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象的指针。 |
| bool first | 当前行是否为段落的首行。true表示首行；false表示非首行。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LeadingMarginSpanDrawInfo\_GetFirst()

```c
ArkUI_ErrorCode OH_ArkUI_LeadingMarginSpanDrawInfo_GetFirst(const OH_ArkUI_LeadingMarginSpanDrawInfo* drawInfo, bool* first)
```

**描述**

获取段落缩进的自定义绘制信息对象中当前行是否为段落的首行。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)\* drawInfo | 指向[OH\_ArkUI\_LeadingMarginSpanDrawInfo](capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo.md)对象的指针。 |
| bool\* first | 当前行是否为段落的首行。true表示首行；false表示非首行。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_Create()

```c
OH_ArkUI_ParagraphStyle* OH_ArkUI_ParagraphStyle_Create()
```

**描述**

创建[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_ParagraphStyle\_Destroy](capi-styled-string-h.md#oh_arkui_paragraphstyle_destroy)销毁它。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针，用于定义段落样式。 |

### OH\_ArkUI\_ParagraphStyle\_Destroy()

```c
void OH_ArkUI_ParagraphStyle_Destroy(OH_ArkUI_ParagraphStyle* paragraphStyle)
```

**描述**

释放[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象占用的内存。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |

### OH\_ArkUI\_ParagraphStyle\_SetTextAlign()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_SetTextAlign(OH_ArkUI_ParagraphStyle* paragraphStyle, ArkUI_TextAlignment align)
```

**描述**

设置段落样式中的水平方向的文本对齐方式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| [ArkUI\_TextAlignment](capi-text-common-h.md#arkui_textalignment) align | 水平方向的文本对齐方式。取值为[ArkUI\_TextAlignment](capi-text-common-h.md#arkui_textalignment)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_GetTextAlign()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_GetTextAlign(const OH_ArkUI_ParagraphStyle* paragraphStyle, ArkUI_TextAlignment* align)
```

**描述**

获取段落样式中的水平方向的文本对齐方式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| [ArkUI\_TextAlignment](capi-text-common-h.md#arkui_textalignment)\* align | 水平方向的文本对齐方式。取值为[ArkUI\_TextAlignment](capi-text-common-h.md#arkui_textalignment)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_SetTextIndent()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_SetTextIndent(OH_ArkUI_ParagraphStyle* paragraphStyle, float textIndent)
```

**描述**

设置段落样式中的首行文本缩进。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| float textIndent | 首行缩进值，单位为vp。取值范围：[0, +∞)。传入负数时使用默认值0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_GetTextIndent()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_GetTextIndent(const OH_ArkUI_ParagraphStyle* paragraphStyle, float* textIndent)
```

**描述**

获取段落样式中的首行文本缩进。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| float\* textIndent | 首行缩进值，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_SetMaxLines()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_SetMaxLines(OH_ArkUI_ParagraphStyle* paragraphStyle, int32_t maxLines)
```

**描述**

设置段落样式中的最大行数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| int32\_t maxLines | 最大行数。取值范围[0, +∞)。传入负数时不限制。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_GetMaxLines()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_GetMaxLines(const OH_ArkUI_ParagraphStyle* paragraphStyle, int32_t* maxLines)
```

**描述**

获取段落样式中的最大行数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| int32\_t\* maxLines | 最大行数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_SetOverflow()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_SetOverflow(OH_ArkUI_ParagraphStyle* paragraphStyle, ArkUI_TextOverflow overflow)
```

**描述**

设置段落样式中的段落超长时的显示方式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| [ArkUI\_TextOverflow](capi-text-common-h.md#arkui_textoverflow) overflow | 段落超长时的显示方式。取值为[ArkUI\_TextOverflow](capi-text-common-h.md#arkui_textoverflow)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_GetOverflow()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_GetOverflow(const OH_ArkUI_ParagraphStyle* paragraphStyle, ArkUI_TextOverflow* overflow)
```

**描述**

获取段落样式中的段落超长时的显示方式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| [ArkUI\_TextOverflow](capi-text-common-h.md#arkui_textoverflow)\* overflow | 段落超长时的显示方式。取值为[ArkUI\_TextOverflow](capi-text-common-h.md#arkui_textoverflow)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_SetWordBreak()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_SetWordBreak(OH_ArkUI_ParagraphStyle* paragraphStyle, ArkUI_WordBreak wordBreak)
```

**描述**

设置段落样式中的断行规则。不同断行策略适用于不同场景，具体请参考[ArkUI\_WordBreak](capi-text-common-h.md#arkui_wordbreak)枚举值。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| [ArkUI\_WordBreak](capi-text-common-h.md#arkui_wordbreak) wordBreak | 断行规则。取值为[ArkUI\_WordBreak](capi-text-common-h.md#arkui_wordbreak)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_GetWordBreak()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_GetWordBreak(const OH_ArkUI_ParagraphStyle* paragraphStyle, ArkUI_WordBreak* wordBreak)
```

**描述**

获取段落样式中的断行规则。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| [ArkUI\_WordBreak](capi-text-common-h.md#arkui_wordbreak)\* wordBreak | 断行规则。取值为[ArkUI\_WordBreak](capi-text-common-h.md#arkui_wordbreak)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_SetLeadingMarginPixelMap()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_SetLeadingMarginPixelMap(OH_ArkUI_ParagraphStyle* paragraphStyle, struct OH_PixelmapNative* pixelmap)
```

**描述**

设置段落样式中的段落缩进的像素图。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| struct [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\* pixelmap | 段落缩进的像素图。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_GetLeadingMarginPixelMap()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_GetLeadingMarginPixelMap(const OH_ArkUI_ParagraphStyle* paragraphStyle, struct OH_PixelmapNative** pixelmap)
```

**描述**

获取段落样式中的段落缩进的像素图。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| struct [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\*\* pixelmap | 段落缩进的像素图。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_SetLeadingMarginWidth()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_SetLeadingMarginWidth(OH_ArkUI_ParagraphStyle* paragraphStyle, uint32_t width)
```

**描述**

设置段落样式中的段落缩进宽度。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| uint32\_t width | 段落缩进宽度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_GetLeadingMarginWidth()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_GetLeadingMarginWidth(const OH_ArkUI_ParagraphStyle* paragraphStyle, uint32_t* width)
```

**描述**

获取段落样式中的段落缩进宽度。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| uint32\_t\* width | 段落缩进宽度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_SetLeadingMarginHeight()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_SetLeadingMarginHeight(OH_ArkUI_ParagraphStyle* paragraphStyle, uint32_t height)
```

**描述**

设置段落样式中的段落缩进高度。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| uint32\_t height | 段落缩进高度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_GetLeadingMarginHeight()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_GetLeadingMarginHeight(const OH_ArkUI_ParagraphStyle* paragraphStyle, uint32_t* height)
```

**描述**

获取段落样式中的段落缩进高度。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| uint32\_t\* height | 段落缩进高度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_SetParagraphSpacing()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_SetParagraphSpacing(OH_ArkUI_ParagraphStyle* paragraphStyle, uint32_t paragraphSpacing)
```

**描述**

设置段落样式中的段落间距。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| uint32\_t paragraphSpacing | 段落间距，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_GetParagraphSpacing()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_GetParagraphSpacing(const OH_ArkUI_ParagraphStyle* paragraphStyle, uint32_t* paragraphSpacing)
```

**描述**

获取段落样式中的段落间距。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| uint32\_t\* paragraphSpacing | 段落间距，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_SetTextVerticalAlign()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_SetTextVerticalAlign(OH_ArkUI_ParagraphStyle* paragraphStyle, ArkUI_TextVerticalAlignment verticalAlignment)
```

**描述**

设置段落样式中的垂直方向的文本对齐方式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| [ArkUI\_TextVerticalAlignment](capi-text-common-h.md#arkui_textverticalalignment) verticalAlignment | 垂直方向的文本对齐方式。取值为[ArkUI\_TextVerticalAlignment](capi-text-common-h.md#arkui_textverticalalignment)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_GetTextVerticalAlign()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_GetTextVerticalAlign(const OH_ArkUI_ParagraphStyle* paragraphStyle, ArkUI_TextVerticalAlignment* verticalAlignment)
```

**描述**

获取段落样式中的垂直方向的文本对齐方式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| [ArkUI\_TextVerticalAlignment](capi-text-common-h.md#arkui_textverticalalignment)\* verticalAlignment | 垂直方向的文本对齐方式。取值为[ArkUI\_TextVerticalAlignment](capi-text-common-h.md#arkui_textverticalalignment)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_RegisterOnDrawLeadingMarginCallback()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_RegisterOnDrawLeadingMarginCallback(OH_ArkUI_ParagraphStyle* paragraphStyle, void(*onDraw)(ArkUI_DrawContext* context, OH_ArkUI_LeadingMarginSpanDrawInfo* drawInfo))
```

**描述**

注册段落样式中绘制段落缩进时触发的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| void(\*onDraw)(ArkUI\_DrawContext\* context, OH\_ArkUI\_LeadingMarginSpanDrawInfo\* drawInfo) | 绘制段落缩进时触发的回调函数。回调参数：context为图形绘制上下文，drawInfo为段落缩进的自定义绘制信息对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_RegisterOnGetLeadingMarginCallback()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_RegisterOnGetLeadingMarginCallback(OH_ArkUI_ParagraphStyle* paragraphStyle, float(*leadingMargin)())
```

**描述**

设置段落样式中获取段落缩进距离时触发的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| float(\*leadingMargin)() | 获取段落缩进距离时触发的回调函数。回调返回值表示段落缩进距离，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_SetTextDirection()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_SetTextDirection(OH_ArkUI_ParagraphStyle* paragraphStyle, ArkUI_TextDirection textDirection)
```

**描述**

设置段落样式中的文本方向。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| [ArkUI\_TextDirection](capi-text-common-h.md#arkui_textdirection) textDirection | 文本方向。取值为[ArkUI\_TextDirection](capi-text-common-h.md#arkui_textdirection)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_GetTextDirection()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_GetTextDirection(const OH_ArkUI_ParagraphStyle* paragraphStyle, ArkUI_TextDirection* textDirection)
```

**描述**

获取段落样式中的文本方向。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| [ArkUI\_TextDirection](capi-text-common-h.md#arkui_textdirection)\* textDirection | 文本方向。取值为[ArkUI\_TextDirection](capi-text-common-h.md#arkui_textdirection)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_GestureStyle\_Create()

```c
OH_ArkUI_GestureStyle* OH_ArkUI_GestureStyle_Create()
```

**描述**

创建[OH\_ArkUI\_GestureStyle](capi-arkui-nativemodule-oh-arkui-gesturestyle.md)对象。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_GestureStyle\_Destroy](capi-styled-string-h.md#oh_arkui_gesturestyle_destroy)销毁它。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_GestureStyle](capi-arkui-nativemodule-oh-arkui-gesturestyle.md)\* | 指向[OH\_ArkUI\_GestureStyle](capi-arkui-nativemodule-oh-arkui-gesturestyle.md)对象的指针，用于定义事件手势样式。 |

### OH\_ArkUI\_GestureStyle\_Destroy()

```c
void OH_ArkUI_GestureStyle_Destroy(OH_ArkUI_GestureStyle* gestureStyle)
```

**描述**

释放[OH\_ArkUI\_GestureStyle](capi-arkui-nativemodule-oh-arkui-gesturestyle.md)对象占用的内存。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_GestureStyle](capi-arkui-nativemodule-oh-arkui-gesturestyle.md)\* gestureStyle | 指向[OH\_ArkUI\_GestureStyle](capi-arkui-nativemodule-oh-arkui-gesturestyle.md)对象的指针。 |

### OH\_ArkUI\_GestureStyle\_RegisterOnClickCallback()

```c
ArkUI_ErrorCode OH_ArkUI_GestureStyle_RegisterOnClickCallback(OH_ArkUI_GestureStyle* gestureStyle, void(*onClick)(ArkUI_NodeEvent*))
```

**描述**

注册事件手势样式中的点击事件回调。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_GestureStyle](capi-arkui-nativemodule-oh-arkui-gesturestyle.md)\* gestureStyle | 指向[OH\_ArkUI\_GestureStyle](capi-arkui-nativemodule-oh-arkui-gesturestyle.md)对象的指针。 |
| void(\*onClick)(ArkUI\_NodeEvent\*) | 点击事件的回调函数。回调参数：event为节点事件对象，包含点击事件的相关信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_GestureStyle\_RegisterOnLongPressCallback()

```c
ArkUI_ErrorCode OH_ArkUI_GestureStyle_RegisterOnLongPressCallback(OH_ArkUI_GestureStyle* gestureStyle, void(*onLongPress)(ArkUI_GestureEvent*))
```

**描述**

注册事件手势样式中的长按事件回调。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_GestureStyle](capi-arkui-nativemodule-oh-arkui-gesturestyle.md)\* gestureStyle | 指向[OH\_ArkUI\_GestureStyle](capi-arkui-nativemodule-oh-arkui-gesturestyle.md)对象的指针。 |
| void(\*onLongPress)(ArkUI\_GestureEvent\*) | 长按事件的回调函数。回调参数：event为手势事件对象，包含长按事件的相关信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_GestureStyle\_RegisterOnTouchCallback()

```c
ArkUI_ErrorCode OH_ArkUI_GestureStyle_RegisterOnTouchCallback(OH_ArkUI_GestureStyle* gestureStyle, void(*onTouch)(ArkUI_NodeEvent*))
```

**描述**

注册事件手势样式中的触摸事件回调。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_GestureStyle](capi-arkui-nativemodule-oh-arkui-gesturestyle.md)\* gestureStyle | 指向[OH\_ArkUI\_GestureStyle](capi-arkui-nativemodule-oh-arkui-gesturestyle.md)对象的指针。 |
| void(\*onTouch)(ArkUI\_NodeEvent\*) | 触摸事件的回调函数。回调参数：event为节点事件对象，包含触摸事件的相关信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextShadowStyle\_Create()

```c
OH_ArkUI_TextShadowStyle* OH_ArkUI_TextShadowStyle_Create()
```

**描述**

创建[OH\_ArkUI\_TextShadowStyle](capi-arkui-nativemodule-oh-arkui-textshadowstyle.md)对象。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_TextShadowStyle\_Destroy](capi-styled-string-h.md#oh_arkui_textshadowstyle_destroy)销毁它。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_TextShadowStyle](capi-arkui-nativemodule-oh-arkui-textshadowstyle.md)\* | 指向[OH\_ArkUI\_TextShadowStyle](capi-arkui-nativemodule-oh-arkui-textshadowstyle.md)对象的指针，用于定义文本阴影样式。 |

### OH\_ArkUI\_TextShadowStyle\_Destroy()

```c
void OH_ArkUI_TextShadowStyle_Destroy(OH_ArkUI_TextShadowStyle* textShadowStyle)
```

**描述**

释放[OH\_ArkUI\_TextShadowStyle](capi-arkui-nativemodule-oh-arkui-textshadowstyle.md)对象占用的内存。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_TextShadowStyle](capi-arkui-nativemodule-oh-arkui-textshadowstyle.md)\* textShadowStyle | 指向[OH\_ArkUI\_TextShadowStyle](capi-arkui-nativemodule-oh-arkui-textshadowstyle.md)对象的指针。 |

### OH\_ArkUI\_TextShadowStyle\_SetTextShadow()

```c
ArkUI_ErrorCode OH_ArkUI_TextShadowStyle_SetTextShadow(OH_ArkUI_TextShadowStyle* textShadowStyle, const OH_ArkUI_ShadowOptions** options, uint32_t length)
```

**描述**

设置文本阴影样式的文本阴影选项。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_TextShadowStyle](capi-arkui-nativemodule-oh-arkui-textshadowstyle.md)\* textShadowStyle | 指向[OH\_ArkUI\_TextShadowStyle](capi-arkui-nativemodule-oh-arkui-textshadowstyle.md)对象的指针。 |
| const [OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)\*\* options | 文本阴影选项，指向[OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)对象数组的指针。 |
| uint32\_t length | 文本阴影选项数组元素的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextShadowStyle\_GetTextShadow()

```c
ArkUI_ErrorCode OH_ArkUI_TextShadowStyle_GetTextShadow(const OH_ArkUI_TextShadowStyle* textShadowStyle, OH_ArkUI_ShadowOptions** shadowOptions, uint32_t shadowOptionsSize, uint32_t* writeLength)
```

**描述**

获取文本阴影样式的文本阴影选项。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_TextShadowStyle](capi-arkui-nativemodule-oh-arkui-textshadowstyle.md)\* textShadowStyle | 指向[OH\_ArkUI\_TextShadowStyle](capi-arkui-nativemodule-oh-arkui-textshadowstyle.md)对象的指针。 |
| [OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)\*\* shadowOptions | 文本阴影选项，指向[OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)对象数组的指针。 |
| uint32\_t shadowOptionsSize | 阴影选项的缓冲区大小。 |
| uint32\_t\* writeLength | 文本阴影样式中实际的文本阴影选项数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DecorationStyle\_Create()

```c
OH_ArkUI_DecorationStyle* OH_ArkUI_DecorationStyle_Create()
```

**描述**

创建[OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)对象。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_DecorationStyle\_Destroy](capi-styled-string-h.md#oh_arkui_decorationstyle_destroy)销毁它。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)\* | 指向[OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)对象的指针，用于定义文本装饰线样式。 |

### OH\_ArkUI\_DecorationStyle\_Destroy()

```c
void OH_ArkUI_DecorationStyle_Destroy(OH_ArkUI_DecorationStyle* decorationStyle)
```

**描述**

释放[OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)对象占用的内存。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)\* decorationStyle | 指向[OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)对象的指针。 |

### OH\_ArkUI\_DecorationStyle\_SetTextDecorationType()

```c
ArkUI_ErrorCode OH_ArkUI_DecorationStyle_SetTextDecorationType(OH_ArkUI_DecorationStyle* decorationStyle, ArkUI_TextDecorationType type)
```

**描述**

设置文本装饰线样式的装饰线类型。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)\* decorationStyle | 指向[OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)对象的指针。 |
| [ArkUI\_TextDecorationType](capi-text-common-h.md#arkui_textdecorationtype) type | 装饰线类型。取值为[ArkUI\_TextDecorationType](capi-text-common-h.md#arkui_textdecorationtype)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DecorationStyle\_GetTextDecorationType()

```c
ArkUI_ErrorCode OH_ArkUI_DecorationStyle_GetTextDecorationType(const OH_ArkUI_DecorationStyle* decorationStyle, ArkUI_TextDecorationType* type)
```

**描述**

获取文本装饰线样式的装饰线类型。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)\* decorationStyle | 指向[OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)对象的指针。 |
| [ArkUI\_TextDecorationType](capi-text-common-h.md#arkui_textdecorationtype)\* type | 装饰线类型。取值为[ArkUI\_TextDecorationType](capi-text-common-h.md#arkui_textdecorationtype)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DecorationStyle\_SetColor()

```c
ArkUI_ErrorCode OH_ArkUI_DecorationStyle_SetColor(OH_ArkUI_DecorationStyle* decorationStyle, uint32_t color)
```

**描述**

设置文本装饰线样式的装饰线颜色。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)\* decorationStyle | 指向[OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)对象的指针。 |
| uint32\_t color | 装饰线颜色，0xARGB格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DecorationStyle\_GetColor()

```c
ArkUI_ErrorCode OH_ArkUI_DecorationStyle_GetColor(const OH_ArkUI_DecorationStyle* decorationStyle, uint32_t* color)
```

**描述**

获取文本装饰线样式的装饰线颜色。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)\* decorationStyle | 指向[OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)对象的指针。 |
| uint32\_t\* color | 装饰线颜色，0xARGB格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DecorationStyle\_SetTextDecorationStyle()

```c
ArkUI_ErrorCode OH_ArkUI_DecorationStyle_SetTextDecorationStyle(OH_ArkUI_DecorationStyle* decorationStyle, ArkUI_TextDecorationStyle style)
```

**描述**

设置文本装饰线样式的装饰线样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)\* decorationStyle | 指向[OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)对象的指针。 |
| [ArkUI\_TextDecorationStyle](capi-text-common-h.md#arkui_textdecorationstyle) style | 装饰线样式。取值为[ArkUI\_TextDecorationStyle](capi-text-common-h.md#arkui_textdecorationstyle)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DecorationStyle\_GetTextDecorationStyle()

```c
ArkUI_ErrorCode OH_ArkUI_DecorationStyle_GetTextDecorationStyle(const OH_ArkUI_DecorationStyle* decorationStyle, ArkUI_TextDecorationStyle* style)
```

**描述**

获取文本装饰线样式的装饰线样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)\* decorationStyle | 指向[OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)对象的指针。 |
| [ArkUI\_TextDecorationStyle](capi-text-common-h.md#arkui_textdecorationstyle)\* style | 装饰线样式。取值为[ArkUI\_TextDecorationStyle](capi-text-common-h.md#arkui_textdecorationstyle)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DecorationStyle\_SetThicknessScale()

```c
ArkUI_ErrorCode OH_ArkUI_DecorationStyle_SetThicknessScale(OH_ArkUI_DecorationStyle* decorationStyle, float thicknessScale)
```

**描述**

设置文本装饰线样式的装饰线的粗细缩放比例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)\* decorationStyle | 指向[OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)对象的指针。 |
| float thicknessScale | 装饰线的粗细缩放比例。取值范围为[0, +∞)。传入负数时不生效。默认值：1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DecorationStyle\_GetThicknessScale()

```c
ArkUI_ErrorCode OH_ArkUI_DecorationStyle_GetThicknessScale(const OH_ArkUI_DecorationStyle* decorationStyle, float* thicknessScale)
```

**描述**

获取文本装饰线样式的装饰线的粗细缩放比例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)\* decorationStyle | 指向[OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)对象的指针。 |
| float\* thicknessScale | 装饰线的粗细缩放比例。取值范围为[0, +∞)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DecorationStyle\_SetEnableMultiType()

```c
ArkUI_ErrorCode OH_ArkUI_DecorationStyle_SetEnableMultiType(OH_ArkUI_DecorationStyle* decorationStyle, bool enableMultiType)
```

**描述**

设置文本装饰线样式中是否开启多装饰线显示。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)\* decorationStyle | 指向[OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)对象的指针。 |
| bool enableMultiType | 是否开启多装饰线显示。传入true时开启多装饰线显示，允许同时显示多种类型的装饰线（如同时显示下划线和删除线），适用于需要复合装饰效果的场景；传入false时不开启，仅显示单一类型装饰线，适用于只需要一种装饰线的场景。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DecorationStyle\_GetEnableMultiType()

```c
ArkUI_ErrorCode OH_ArkUI_DecorationStyle_GetEnableMultiType(const OH_ArkUI_DecorationStyle* decorationStyle, bool* enableMultiType)
```

**描述**

获取文本装饰线样式中是否开启多装饰线显示。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)\* decorationStyle | 指向[OH\_ArkUI\_DecorationStyle](capi-arkui-nativemodule-oh-arkui-decorationstyle.md)对象的指针。 |
| bool\* enableMultiType | 是否开启多装饰线显示。true表示开启，false表示关闭。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_BaselineOffsetStyle\_Create()

```c
OH_ArkUI_BaselineOffsetStyle* OH_ArkUI_BaselineOffsetStyle_Create()
```

**描述**

创建[OH\_ArkUI\_BaselineOffsetStyle](capi-arkui-nativemodule-oh-arkui-baselineoffsetstyle.md)对象。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_BaselineOffsetStyle\_Destroy](capi-styled-string-h.md#oh_arkui_baselineoffsetstyle_destroy)销毁它。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_BaselineOffsetStyle](capi-arkui-nativemodule-oh-arkui-baselineoffsetstyle.md)\* | 指向[OH\_ArkUI\_BaselineOffsetStyle](capi-arkui-nativemodule-oh-arkui-baselineoffsetstyle.md)对象的指针，用于定义基线偏移量样式。 |

### OH\_ArkUI\_BaselineOffsetStyle\_Destroy()

```c
void OH_ArkUI_BaselineOffsetStyle_Destroy(OH_ArkUI_BaselineOffsetStyle* baselineOffsetStyle)
```

**描述**

释放[OH\_ArkUI\_BaselineOffsetStyle](capi-arkui-nativemodule-oh-arkui-baselineoffsetstyle.md)对象占用的内存。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_BaselineOffsetStyle](capi-arkui-nativemodule-oh-arkui-baselineoffsetstyle.md)\* baselineOffsetStyle | 指向[OH\_ArkUI\_BaselineOffsetStyle](capi-arkui-nativemodule-oh-arkui-baselineoffsetstyle.md)对象的指针。 |

### OH\_ArkUI\_BaselineOffsetStyle\_SetBaselineOffset()

```c
ArkUI_ErrorCode OH_ArkUI_BaselineOffsetStyle_SetBaselineOffset(OH_ArkUI_BaselineOffsetStyle* baselineOffsetStyle, float baselineOffset)
```

**描述**

设置基线偏移量。适用于需要调整文本基线位置的场景，例如上下角标定位、行内图标与文字垂直对齐等。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_BaselineOffsetStyle](capi-arkui-nativemodule-oh-arkui-baselineoffsetstyle.md)\* baselineOffsetStyle | 指向[OH\_ArkUI\_BaselineOffsetStyle](capi-arkui-nativemodule-oh-arkui-baselineoffsetstyle.md)对象的指针。 |
| float baselineOffset | 基线偏移量，单位为vp。取值范围(-∞, +∞)。正值与负值分别对应不同的偏移方向，0表示无偏移。具体方向效果需结合上下角标等场景确定。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_BaselineOffsetStyle\_GetBaselineOffset()

```c
ArkUI_ErrorCode OH_ArkUI_BaselineOffsetStyle_GetBaselineOffset(const OH_ArkUI_BaselineOffsetStyle* baselineOffsetStyle, float* baselineOffset)
```

**描述**

获取基线偏移量。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_BaselineOffsetStyle](capi-arkui-nativemodule-oh-arkui-baselineoffsetstyle.md)\* baselineOffsetStyle | 指向[OH\_ArkUI\_BaselineOffsetStyle](capi-arkui-nativemodule-oh-arkui-baselineoffsetstyle.md)对象的指针。 |
| float\* baselineOffset | 基线偏移量，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LetterSpacingStyle\_Create()

```c
OH_ArkUI_LetterSpacingStyle* OH_ArkUI_LetterSpacingStyle_Create()
```

**描述**

创建[OH\_ArkUI\_LetterSpacingStyle](capi-arkui-nativemodule-oh-arkui-letterspacingstyle.md)对象。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_LetterSpacingStyle\_Destroy](capi-styled-string-h.md#oh_arkui_letterspacingstyle_destroy)销毁它。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_LetterSpacingStyle](capi-arkui-nativemodule-oh-arkui-letterspacingstyle.md)\* | 指向[OH\_ArkUI\_LetterSpacingStyle](capi-arkui-nativemodule-oh-arkui-letterspacingstyle.md)对象的指针，用于定义字符间距样式。 |

### OH\_ArkUI\_LetterSpacingStyle\_Destroy()

```c
void OH_ArkUI_LetterSpacingStyle_Destroy(OH_ArkUI_LetterSpacingStyle* letterSpacingStyle)
```

**描述**

释放[OH\_ArkUI\_LetterSpacingStyle](capi-arkui-nativemodule-oh-arkui-letterspacingstyle.md)对象占用的内存。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_LetterSpacingStyle](capi-arkui-nativemodule-oh-arkui-letterspacingstyle.md)\* letterSpacingStyle | 指向[OH\_ArkUI\_LetterSpacingStyle](capi-arkui-nativemodule-oh-arkui-letterspacingstyle.md)对象的指针。 |

### OH\_ArkUI\_LetterSpacingStyle\_SetLetterSpacing()

```c
ArkUI_ErrorCode OH_ArkUI_LetterSpacingStyle_SetLetterSpacing(OH_ArkUI_LetterSpacingStyle* letterSpacingStyle, float letterSpacing)
```

**描述**

设置字符间距。适用于需要调整文字间距的场景，例如标题加宽间距提升可读性、紧凑排版缩小间距等。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_LetterSpacingStyle](capi-arkui-nativemodule-oh-arkui-letterspacingstyle.md)\* letterSpacingStyle | 指向[OH\_ArkUI\_LetterSpacingStyle](capi-arkui-nativemodule-oh-arkui-letterspacingstyle.md)对象的指针。 |
| float letterSpacing | 字符间距值，单位为vp。取值范围(-∞, +∞)。正值表示加宽字符间距，负值表示缩小字符间距，0表示使用默认间距。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LetterSpacingStyle\_GetLetterSpacing()

```c
ArkUI_ErrorCode OH_ArkUI_LetterSpacingStyle_GetLetterSpacing(const OH_ArkUI_LetterSpacingStyle* letterSpacingStyle, float* letterSpacing)
```

**描述**

获取字符间距。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_LetterSpacingStyle](capi-arkui-nativemodule-oh-arkui-letterspacingstyle.md)\* letterSpacingStyle | 指向[OH\_ArkUI\_LetterSpacingStyle](capi-arkui-nativemodule-oh-arkui-letterspacingstyle.md)对象的指针。 |
| float\* letterSpacing | 字符间距值，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LineHeightStyle\_Create()

```c
OH_ArkUI_LineHeightStyle* OH_ArkUI_LineHeightStyle_Create()
```

**描述**

创建[OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md)对象。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_LineHeightStyle\_Destroy](capi-styled-string-h.md#oh_arkui_lineheightstyle_destroy)销毁它。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md)\* | 指向[OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md)对象的指针，用于定义行高样式。 |

### OH\_ArkUI\_LineHeightStyle\_Destroy()

```c
void OH_ArkUI_LineHeightStyle_Destroy(OH_ArkUI_LineHeightStyle* lineHeightStyle)
```

**描述**

释放[OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md)对象占用的内存。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md)\* lineHeightStyle | 指向[OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md)对象的指针。 |

### OH\_ArkUI\_LineHeightStyle\_SetLineHeight()

```c
ArkUI_ErrorCode OH_ArkUI_LineHeightStyle_SetLineHeight(OH_ArkUI_LineHeightStyle* lineHeightStyle, float lineHeight)
```

**描述**

设置文本行高。

**说明** 

与[OH\_ArkUI\_LineHeightStyle\_SetLineHeightMultiple](capi-styled-string-h.md#oh_arkui_lineheightstyle_setlineheightmultiple)同时设置时，仅lineHeightMultiple生效，lineHeight不生效。lineHeightMultiple小于0时不生效，此时使用lineHeight设置行高。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md)\* lineHeightStyle | 指向[OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md)对象的指针。 |
| float lineHeight | 固定行高值，单位为vp。与[OH\_ArkUI\_LineHeightStyle\_SetLineHeightMultiple](capi-styled-string-h.md#oh_arkui_lineheightstyle_setlineheightmultiple)同时设置时，仅lineHeightMultiple生效，lineHeight不生效，lineHeightMultiple小于0时不生效，此时使用lineHeight设置行高。取值范围(-∞, +∞)，负值表示自适应字体大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LineHeightStyle\_GetLineHeight()

```c
ArkUI_ErrorCode OH_ArkUI_LineHeightStyle_GetLineHeight(const OH_ArkUI_LineHeightStyle* lineHeightStyle, float* lineHeight)
```

**描述**

获取文本行高。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md)\* lineHeightStyle | 指向[OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md)对象的指针。 |
| float\* lineHeight | 固定行高值，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LineHeightStyle\_SetLineHeightMultiple()

```c
ArkUI_ErrorCode OH_ArkUI_LineHeightStyle_SetLineHeightMultiple(OH_ArkUI_LineHeightStyle* lineHeightStyle, float lineHeightMultiple)
```

**描述**

设置行高样式的行高倍数。

**说明** 

* lineHeightMultiple与lineHeight或[OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)同时设置时，仅lineHeightMultiple生效，行高为该行最高字体高度与倍数的乘积。
* lineHeightMultiple小于0时不生效，使用lineHeight和[OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)设置行高和行间距。
* lineHeight可以通过[OH\_ArkUI\_LineHeightStyle\_SetLineHeight()](capi-styled-string-h.md#oh_arkui_lineheightstyle_setlineheight)接口设置。
* lineHeightMultiple等于0时等效于设置为1。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md)\* lineHeightStyle | 指向[OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md)对象的指针。 |
| float lineHeightMultiple | 行高倍数。取值范围为[0, +∞)。传入负数时不生效，传入0时等效于设置为1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LineHeightStyle\_GetLineHeightMultiple()

```c
ArkUI_ErrorCode OH_ArkUI_LineHeightStyle_GetLineHeightMultiple(const OH_ArkUI_LineHeightStyle* lineHeightStyle, float* lineHeightMultiple)
```

**描述**

获取行高样式的行高倍数。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md)\* lineHeightStyle | 指向[OH\_ArkUI\_LineHeightStyle](capi-arkui-nativemodule-oh-arkui-lineheightstyle.md)对象的指针。 |
| float\* lineHeightMultiple | 行高倍数。取值范围为[0, +∞)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_SetLineSpacingStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_SetLineSpacingStyle(OH_ArkUI_SpanStyle* spanStyle, const OH_ArkUI_LineSpacingStyle* lineSpacingStyle)
```

**描述**

设置属性字符串样式对象的行间距样式。

**说明** 

此操作会替换[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象中已设置的其他类型样式。一个SpanStyle对象只能持有一种类型的样式，设置新类型样式后，之前已设置的其他类型样式（如已设置的GestureStyle、ParagraphStyle等）将被清除。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| const [OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)\* lineSpacingStyle | 指向[OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SpanStyle\_GetLineSpacingStyle()

```c
ArkUI_ErrorCode OH_ArkUI_SpanStyle_GetLineSpacingStyle(const OH_ArkUI_SpanStyle* spanStyle, OH_ArkUI_LineSpacingStyle* lineSpacingStyle)
```

**描述**

获取属性字符串样式对象的行间距样式。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)\* spanStyle | 指向[OH\_ArkUI\_SpanStyle](capi-arkui-nativemodule-oh-arkui-spanstyle.md)对象的指针。 |
| [OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)\* lineSpacingStyle | 指向[OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)对象的指针，用于定义行间距样式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LineSpacingStyle\_Create()

```c
OH_ArkUI_LineSpacingStyle* OH_ArkUI_LineSpacingStyle_Create()
```

**描述**

创建[OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)对象。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_LineSpacingStyle\_Destroy](capi-styled-string-h.md#oh_arkui_linespacingstyle_destroy)销毁它。

**起始版本：** 26.0.0

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)\* | 指向[OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)对象的指针，用于定义行间距样式。 |

### OH\_ArkUI\_LineSpacingStyle\_Destroy()

```c
void OH_ArkUI_LineSpacingStyle_Destroy(OH_ArkUI_LineSpacingStyle* lineSpacingStyle)
```

**描述**

释放[OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)对象占用的内存。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)\* lineSpacingStyle | 指向[OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)对象的指针。 |

### OH\_ArkUI\_LineSpacingStyle\_SetLineSpacing()

```c
ArkUI_ErrorCode OH_ArkUI_LineSpacingStyle_SetLineSpacing(OH_ArkUI_LineSpacingStyle* lineSpacingStyle, float lineSpacing)
```

**描述**

设置行间距。

**说明** 

与[OH\_ArkUI\_LineHeightStyle\_SetLineHeightMultiple](capi-styled-string-h.md#oh_arkui_lineheightstyle_setlineheightmultiple)同时设置时，仅lineHeightMultiple生效，行间距不生效。lineHeightMultiple小于0时不生效，此时行间距正常生效。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)\* lineSpacingStyle | 指向[OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)对象的指针。 |
| float lineSpacing | 行间距值，单位为vp。取值范围(-∞, +∞)。与[OH\_ArkUI\_LineHeightStyle\_SetLineHeightMultiple](capi-styled-string-h.md#oh_arkui_lineheightstyle_setlineheightmultiple)同时设置时，仅lineHeightMultiple生效，行间距不生效。lineHeightMultiple小于0时不生效，此时行间距正常生效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LineSpacingStyle\_GetLineSpacing()

```c
ArkUI_ErrorCode OH_ArkUI_LineSpacingStyle_GetLineSpacing(const OH_ArkUI_LineSpacingStyle* lineSpacingStyle, float* lineSpacing)
```

**描述**

获取行间距。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)\* lineSpacingStyle | 指向[OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)对象的指针。 |
| float\* lineSpacing | 行间距值，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LineSpacingStyle\_SetOnlyBetweenLines()

```c
ArkUI_ErrorCode OH_ArkUI_LineSpacingStyle_SetOnlyBetweenLines(OH_ArkUI_LineSpacingStyle* lineSpacingStyle, bool onlyBetweenLines)
```

**描述**

设置行间距是否只在行间生效。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)\* lineSpacingStyle | 指向[OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)对象的指针。 |
| bool onlyBetweenLines | 行间距是否只在行间生效。true表示仅在行与行之间添加间距，首行上方、尾行下方无额外间距，false表示所有行之间、首行上方、尾行下方均添加完整行间距。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_LineSpacingStyle\_GetOnlyBetweenLines()

```c
ArkUI_ErrorCode OH_ArkUI_LineSpacingStyle_GetOnlyBetweenLines(const OH_ArkUI_LineSpacingStyle* lineSpacingStyle, bool* onlyBetweenLines)
```

**描述**

获取行间距是否只在行间生效。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)\* lineSpacingStyle | 指向[OH\_ArkUI\_LineSpacingStyle](capi-arkui-nativemodule-oh-arkui-linespacingstyle.md)对象的指针。 |
| bool\* onlyBetweenLines | 行间距是否只在行间生效。true表示仅在行与行之间添加间距，首行上方、尾行下方无额外间距，false表示所有行之间、首行上方、尾行下方均添加完整行间距。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_BackgroundColorStyle\_Create()

```c
OH_ArkUI_BackgroundColorStyle* OH_ArkUI_BackgroundColorStyle_Create()
```

**描述**

创建[OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md)对象。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_BackgroundColorStyle\_Destroy](capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_destroy)销毁它。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md)\* | 指向[OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md)对象的指针，用于定义背景颜色样式。 |

### OH\_ArkUI\_BackgroundColorStyle\_Destroy()

```c
void OH_ArkUI_BackgroundColorStyle_Destroy(OH_ArkUI_BackgroundColorStyle* style)
```

**描述**

释放[OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md)对象占用的内存。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md)\* style | 指向[OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md)对象的指针。 |

### OH\_ArkUI\_BackgroundColorStyle\_SetColor()

```c
ArkUI_ErrorCode OH_ArkUI_BackgroundColorStyle_SetColor(OH_ArkUI_BackgroundColorStyle* style, uint32_t color)
```

**描述**

设置背景颜色样式的背景色。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md)\* style | 指向[OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md)对象的指针。 |
| uint32\_t color | 背景颜色，0xARGB格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_BackgroundColorStyle\_GetColor()

```c
ArkUI_ErrorCode OH_ArkUI_BackgroundColorStyle_GetColor(const OH_ArkUI_BackgroundColorStyle* style, uint32_t* color)
```

**描述**

获取背景颜色样式的背景色。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md)\* style | 指向[OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md)对象的指针。 |
| uint32\_t\* color | 背景颜色，0xARGB格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_BackgroundColorStyle\_SetRadius()

```c
ArkUI_ErrorCode OH_ArkUI_BackgroundColorStyle_SetRadius(OH_ArkUI_BackgroundColorStyle* style, float topLeft, float topRight, float bottomLeft, float bottomRight)
```

**描述**

设置背景颜色样式的背景圆角。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md)\* style | 指向[OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md)对象的指针。 |
| float topLeft | 左上角圆角半径，单位为vp。取值范围：[0, +∞)。传入负数时使用默认值0。 |
| float topRight | 右上角圆角半径，单位为vp。取值范围：[0, +∞)。传入负数时使用默认值0。 |
| float bottomLeft | 左下角圆角半径，单位为vp。取值范围：[0, +∞)。传入负数时使用默认值0。 |
| float bottomRight | 右下角圆角半径，单位为vp。取值范围：[0, +∞)。传入负数时使用默认值0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_BackgroundColorStyle\_GetRadius()

```c
ArkUI_ErrorCode OH_ArkUI_BackgroundColorStyle_GetRadius(const OH_ArkUI_BackgroundColorStyle* style, float* topLeft, float* topRight, float* bottomLeft, float* bottomRight)
```

**描述**

获取背景颜色样式的背景圆角。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md)\* style | 指向[OH\_ArkUI\_BackgroundColorStyle](capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle.md)对象的指针。 |
| float\* topLeft | 左上角圆角半径，单位为vp。 |
| float\* topRight | 右上角圆角半径，单位为vp。 |
| float\* bottomLeft | 左下角圆角半径，单位为vp。 |
| float\* bottomRight | 右下角圆角半径，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_UrlStyle\_Create()

```c
OH_ArkUI_UrlStyle* OH_ArkUI_UrlStyle_Create()
```

**描述**

创建[OH\_ArkUI\_UrlStyle](capi-arkui-nativemodule-oh-arkui-urlstyle.md)对象。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_UrlStyle\_Destroy](capi-styled-string-h.md#oh_arkui_urlstyle_destroy)销毁它。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_UrlStyle](capi-arkui-nativemodule-oh-arkui-urlstyle.md)\* | 指向[OH\_ArkUI\_UrlStyle](capi-arkui-nativemodule-oh-arkui-urlstyle.md)对象的指针，用于定义超链接样式。 |

### OH\_ArkUI\_UrlStyle\_Destroy()

```c
void OH_ArkUI_UrlStyle_Destroy(OH_ArkUI_UrlStyle* style)
```

**描述**

释放[OH\_ArkUI\_UrlStyle](capi-arkui-nativemodule-oh-arkui-urlstyle.md)对象占用的内存。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_UrlStyle](capi-arkui-nativemodule-oh-arkui-urlstyle.md)\* style | 指向[OH\_ArkUI\_UrlStyle](capi-arkui-nativemodule-oh-arkui-urlstyle.md)对象的指针。 |

### OH\_ArkUI\_UrlStyle\_SetUrl()

```c
ArkUI_ErrorCode OH_ArkUI_UrlStyle_SetUrl(OH_ArkUI_UrlStyle* style, const char* url)
```

**描述**

设置超链接样式的超链接内容。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_UrlStyle](capi-arkui-nativemodule-oh-arkui-urlstyle.md)\* style | 指向[OH\_ArkUI\_UrlStyle](capi-arkui-nativemodule-oh-arkui-urlstyle.md)对象的指针。 |
| const char\* url | 超链接内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_UrlStyle\_GetUrl()

```c
ArkUI_ErrorCode OH_ArkUI_UrlStyle_GetUrl(const OH_ArkUI_UrlStyle* style, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取超链接样式的超链接内容。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_UrlStyle](capi-arkui-nativemodule-oh-arkui-urlstyle.md)\* style | 指向[OH\_ArkUI\_UrlStyle](capi-arkui-nativemodule-oh-arkui-urlstyle.md)对象的指针。 |
| char\* buffer | 超链接内容写入内存的缓冲区，内存空间需由开发者分配。 |
| int32\_t bufferSize | 缓冲区最多可写入的字符的数量。 |
| int32\_t\* writeLength | 返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时，表示实际写入缓冲区的字符的数量。  返回[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时，表示字符串完整写入缓冲区所需要的最小长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 缓冲区大小不足，可通过writeLength参数获取所需最小缓冲区大小，重新分配足够大小的缓冲区后再次调用。 |

### OH\_ArkUI\_UserDataSpan\_Create()

```c
OH_ArkUI_UserDataSpan* OH_ArkUI_UserDataSpan_Create()
```

**描述**

创建[OH\_ArkUI\_UserDataSpan](capi-arkui-nativemodule-oh-arkui-userdataspan.md)对象。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_UserDataSpan\_Destroy](capi-styled-string-h.md#oh_arkui_userdataspan_destroy)销毁它。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_UserDataSpan](capi-arkui-nativemodule-oh-arkui-userdataspan.md)\* | 指向[OH\_ArkUI\_UserDataSpan](capi-arkui-nativemodule-oh-arkui-userdataspan.md)对象的指针，用于定义用户数据Span样式。 |

### OH\_ArkUI\_UserDataSpan\_Destroy()

```c
void OH_ArkUI_UserDataSpan_Destroy(OH_ArkUI_UserDataSpan* userDataSpan)
```

**描述**

释放[OH\_ArkUI\_UserDataSpan](capi-arkui-nativemodule-oh-arkui-userdataspan.md)对象占用的内存。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_UserDataSpan](capi-arkui-nativemodule-oh-arkui-userdataspan.md)\* userDataSpan | 指向[OH\_ArkUI\_UserDataSpan](capi-arkui-nativemodule-oh-arkui-userdataspan.md)对象的指针。 |

### OH\_ArkUI\_UserDataSpan\_SetUserData()

```c
ArkUI_ErrorCode OH_ArkUI_UserDataSpan_SetUserData(OH_ArkUI_UserDataSpan* userDataSpan, void* userData)
```

**描述**

设置用户数据Span样式中的用户数据。

**说明** 

该接口允许开发者将任意类型的自定义数据关联到当前的样式对象上。用于在属性字符串中存储用户数据。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_UserDataSpan](capi-arkui-nativemodule-oh-arkui-userdataspan.md)\* userDataSpan | 指向[OH\_ArkUI\_UserDataSpan](capi-arkui-nativemodule-oh-arkui-userdataspan.md)对象的指针。 |
| void\* userData | 用户数据，生命周期需由开发者自行管理。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_UserDataSpan\_GetUserData()

```c
ArkUI_ErrorCode OH_ArkUI_UserDataSpan_GetUserData(const OH_ArkUI_UserDataSpan* userDataSpan, void** userData)
```

**描述**

获取用户数据Span样式中的用户数据。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_UserDataSpan](capi-arkui-nativemodule-oh-arkui-userdataspan.md)\* userDataSpan | 指向[OH\_ArkUI\_UserDataSpan](capi-arkui-nativemodule-oh-arkui-userdataspan.md)对象的指针。 |
| void\*\* userData | 用户数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomSpan\_Create()

```c
OH_ArkUI_CustomSpan* OH_ArkUI_CustomSpan_Create()
```

**描述**

创建[OH\_ArkUI\_CustomSpan](capi-arkui-nativemodule-oh-arkui-customspan.md)对象。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_CustomSpan\_Destroy](capi-styled-string-h.md#oh_arkui_customspan_destroy)销毁它。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_CustomSpan](capi-arkui-nativemodule-oh-arkui-customspan.md)\* | 指向[OH\_ArkUI\_CustomSpan](capi-arkui-nativemodule-oh-arkui-customspan.md)对象的指针，用于定义自定义绘制Span。 |

### OH\_ArkUI\_CustomSpan\_Destroy()

```c
void OH_ArkUI_CustomSpan_Destroy(OH_ArkUI_CustomSpan* customSpan)
```

**描述**

释放[OH\_ArkUI\_CustomSpan](capi-arkui-nativemodule-oh-arkui-customspan.md)对象占用的内存。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_CustomSpan](capi-arkui-nativemodule-oh-arkui-customspan.md)\* customSpan | 指向[OH\_ArkUI\_CustomSpan](capi-arkui-nativemodule-oh-arkui-customspan.md)对象的指针。 |

### OH\_ArkUI\_CustomSpan\_RegisterOnMeasureCallback()

```c
ArkUI_ErrorCode OH_ArkUI_CustomSpan_RegisterOnMeasureCallback(OH_ArkUI_CustomSpan* customSpan, ArkUI_CustomSpanMetrics*(*onMeasure)(float))
```

**描述**

设置自定义绘制Span获取尺寸大小时的回调函数。适用于在文本中嵌入自定义内容（如自定义图标、内联控件、特殊表情等）时，需要根据内容计算占用尺寸的场景。回调返回的尺寸将影响该Span在文本排版中的占位大小。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_CustomSpan](capi-arkui-nativemodule-oh-arkui-customspan.md)\* customSpan | 指向[OH\_ArkUI\_CustomSpan](capi-arkui-nativemodule-oh-arkui-customspan.md)对象的指针。 |
| ArkUI\_CustomSpanMetrics\*(\*onMeasure)(float) | 获取尺寸大小的回调函数。fontSize为组件中的文本字体大小，单位为fp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CustomSpan\_RegisterOnDrawCallback()

```c
ArkUI_ErrorCode OH_ArkUI_CustomSpan_RegisterOnDrawCallback(OH_ArkUI_CustomSpan* customSpan, void(*onDraw)(ArkUI_DrawContext*, ArkUI_CustomSpanDrawInfo*))
```

**描述**

注册自定义绘制Span绘制时的回调函数。适用于需要绘制非标准文本内容的场景，例如在文本中绘制自定义图标、装饰图形、特殊标记等。通过该回调，开发者可以使用图形绘制上下文实现任意自定义绘制效果。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_CustomSpan](capi-arkui-nativemodule-oh-arkui-customspan.md)\* customSpan | 指向[OH\_ArkUI\_CustomSpan](capi-arkui-nativemodule-oh-arkui-customspan.md)对象的指针。 |
| void(\*onDraw)(ArkUI\_DrawContext\*, ArkUI\_CustomSpanDrawInfo\*) | 绘制时的回调函数。回调参数：context为图形绘制上下文，drawInfo为自定义绘制Span的绘制信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_Create()

```c
OH_ArkUI_ImageAttachment* OH_ArkUI_ImageAttachment_Create()
```

**描述**

创建[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象。

**说明** 

当该对象不再使用时，调用[OH\_ArkUI\_ImageAttachment\_Destroy](capi-styled-string-h.md#oh_arkui_imageattachment_destroy)销毁它。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针，用于定义图片样式对象。 |

### OH\_ArkUI\_ImageAttachment\_Destroy()

```c
void OH_ArkUI_ImageAttachment_Destroy(OH_ArkUI_ImageAttachment* imageAttachment)
```

**描述**

释放[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象占用的内存。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |

### OH\_ArkUI\_ImageAttachment\_SetPixelMap()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_SetPixelMap(OH_ArkUI_ImageAttachment* imageAttachment, struct OH_PixelmapNative* pixelmap)
```

**描述**

设置图片样式中的图片数据源。

**说明** 

与[OH\_ArkUI\_ImageAttachment\_SetResource](capi-styled-string-h.md#oh_arkui_imageattachment_setresource)同时设置时，后设置的生效。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| struct [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\* pixelmap | 图片数据源。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_GetPixelMap()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_GetPixelMap(const OH_ArkUI_ImageAttachment* imageAttachment, struct OH_PixelmapNative** pixelmap)
```

**描述**

获取图片样式中的图片数据源。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| struct [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\*\* pixelmap | 图片数据源。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_SetResource()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_SetResource(OH_ArkUI_ImageAttachment* imageAttachment, const char* resource)
```

**描述**

设置图片样式中的图片资源地址。

**说明** 

与[OH\_ArkUI\_ImageAttachment\_SetPixelMap](capi-styled-string-h.md#oh_arkui_imageattachment_setpixelmap)同时设置时，后设置的生效。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| const char\* resource | 图片资源地址。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_GetResource()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_GetResource(const OH_ArkUI_ImageAttachment* imageAttachment, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取图片样式中的图片资源地址。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| char\* buffer | 图片资源地址字符串写入内存的缓冲区，内存空间需由开发者分配。 |
| int32\_t bufferSize | 缓冲区大小。 |
| int32\_t\* writeLength | 返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时，表示实际写入缓冲区的字符串长度。  返回[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时，表示字符串完整写入缓冲区所需要的最小长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 缓冲区大小不足。 |

### OH\_ArkUI\_ImageAttachment\_SetSizeWidth()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_SetSizeWidth(OH_ArkUI_ImageAttachment* imageAttachment, float width)
```

**描述**

设置图片样式中的图片宽度。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| float width | 图片宽度，单位为vp。取值范围：[0, +∞)。默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_GetSizeWidth()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_GetSizeWidth(const OH_ArkUI_ImageAttachment* imageAttachment, float* width)
```

**描述**

获取图片样式中的图片宽度。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| float\* width | 图片宽度，单位为vp。取值范围：[0, +∞)。默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_SetSizeHeight()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_SetSizeHeight(OH_ArkUI_ImageAttachment* imageAttachment, float height)
```

**描述**

设置图片样式中的图片高度。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| float height | 图片高度，单位为vp。取值范围：[0, +∞)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_GetSizeHeight()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_GetSizeHeight(const OH_ArkUI_ImageAttachment* imageAttachment, float* height)
```

**描述**

获取图片样式中的图片高度。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| float\* height | 图片高度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_SetVerticalAlign()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_SetVerticalAlign(OH_ArkUI_ImageAttachment* imageAttachment, ArkUI_ImageSpanAlignment verticalAlign)
```

**描述**

设置图片样式中的图片对齐方式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| [ArkUI\_ImageSpanAlignment](capi-image-span-h.md#arkui_imagespanalignment) verticalAlign | 图片对齐方式。取值为[ArkUI\_ImageSpanAlignment](capi-image-span-h.md#arkui_imagespanalignment)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_GetVerticalAlign()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_GetVerticalAlign(const OH_ArkUI_ImageAttachment* imageAttachment, ArkUI_ImageSpanAlignment* verticalAlign)
```

**描述**

获取图片样式中的图片对齐方式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| [ArkUI\_ImageSpanAlignment](capi-image-span-h.md#arkui_imagespanalignment)\* verticalAlign | 图片对齐方式。取值为[ArkUI\_ImageSpanAlignment](capi-image-span-h.md#arkui_imagespanalignment)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_SetObjectFit()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_SetObjectFit(OH_ArkUI_ImageAttachment* imageAttachment, ArkUI_ObjectFit objectFit)
```

**描述**

设置图片样式中的图片缩放类型。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| [ArkUI\_ObjectFit](capi-image-h.md#arkui_objectfit) objectFit | 图片缩放类型。取值为[ArkUI\_ObjectFit](capi-image-h.md#arkui_objectfit)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_GetObjectFit()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_GetObjectFit(const OH_ArkUI_ImageAttachment* imageAttachment, ArkUI_ObjectFit* objectFit)
```

**描述**

获取图片样式中的图片缩放类型。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| [ArkUI\_ObjectFit](capi-image-h.md#arkui_objectfit)\* objectFit | 图片缩放类型。取值为[ArkUI\_ObjectFit](capi-image-h.md#arkui_objectfit)中的枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_SetMargin()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_SetMargin(OH_ArkUI_ImageAttachment* imageAttachment, ArkUI_Margin margin)
```

**描述**

设置图片样式中的图片外边距。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| [ArkUI\_Margin](capi-arkui-nativemodule-arkui-margin.md) margin | 图片外边距，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_GetMargin()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_GetMargin(const OH_ArkUI_ImageAttachment* imageAttachment, ArkUI_Margin* margin)
```

**描述**

获取图片样式中的图片外边距。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| [ArkUI\_Margin](capi-arkui-nativemodule-arkui-margin.md)\* margin | 图片外边距，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_SetPadding()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_SetPadding(OH_ArkUI_ImageAttachment* imageAttachment, ArkUI_Margin padding)
```

**描述**

设置图片样式中的图片内边距。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| [ArkUI\_Margin](capi-arkui-nativemodule-arkui-margin.md) padding | 图片内边距，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_GetPadding()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_GetPadding(const OH_ArkUI_ImageAttachment* imageAttachment, ArkUI_Margin* padding)
```

**描述**

获取图片样式中的图片内边距。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| [ArkUI\_Margin](capi-arkui-nativemodule-arkui-margin.md)\* padding | 图片内边距，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_SetBorderRadiuses()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_SetBorderRadiuses(OH_ArkUI_ImageAttachment* imageAttachment, float topLeft, float topRight, float bottomLeft, float bottomRight)
```

**描述**

设置图片样式中的图片圆角。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| float topLeft | 左上角圆角半径，单位为vp。取值范围：[0, +∞)。传入负数时使用默认值0。 |
| float topRight | 右上角圆角半径，单位为vp。取值范围：[0, +∞)。传入负数时使用默认值0。 |
| float bottomLeft | 左下角圆角半径，单位为vp。取值范围：[0, +∞)。传入负数时使用默认值0。 |
| float bottomRight | 右下角圆角半径，单位为vp。取值范围：[0, +∞)。传入负数时使用默认值0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_GetBorderRadiuses()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_GetBorderRadiuses(const OH_ArkUI_ImageAttachment* imageAttachment, float* topLeft, float* topRight, float* bottomLeft, float* bottomRight)
```

**描述**

获取图片样式中的图片圆角。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| float\* topLeft | 左上角圆角半径，单位为vp。取值范围[0, +∞)。 |
| float\* topRight | 右上角圆角半径，单位为vp。取值范围[0, +∞)。 |
| float\* bottomLeft | 左下角圆角半径，单位为vp。取值范围[0, +∞)。 |
| float\* bottomRight | 右下角圆角半径，单位为vp。取值范围[0, +∞)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_SetColorFilter()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_SetColorFilter(OH_ArkUI_ImageAttachment* imageAttachment, const float* colorFilter, uint32_t size)
```

**描述**

设置图片样式中的图片颜色过滤器。

**说明** 

与[OH\_ArkUI\_ImageAttachment\_SetDrawingColorFilter](capi-styled-string-h.md#oh_arkui_imageattachment_setdrawingcolorfilter)同时设置时，后设置的生效。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| const float\* colorFilter | 图片颜色过滤器，float类型数组，包含颜色矩阵变换系数，用于对图片进行颜色变换，数组长度由参数size指定。 |
| uint32\_t size | 颜色过滤器数组的元素数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_GetColorFilter()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_GetColorFilter(const OH_ArkUI_ImageAttachment* imageAttachment, float** colorFilter, uint32_t colorFilterSize, uint32_t* writeLength)
```

**描述**

获取图片样式中的图片颜色过滤器。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| float\*\* colorFilter | 图片颜色过滤器写入内存的缓冲区，内存空间需由开发者分配。 |
| uint32\_t colorFilterSize | 缓冲区大小。 |
| uint32\_t\* writeLength | 图片颜色过滤器数组的实际大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 缓冲区大小不足。 |

### OH\_ArkUI\_ImageAttachment\_SetDrawingColorFilter()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_SetDrawingColorFilter(OH_ArkUI_ImageAttachment* imageAttachment, const OH_Drawing_ColorFilter* drawingColorFilter)
```

**描述**

设置图片样式中的图片颜色滤镜。

**说明** 

与[OH\_ArkUI\_ImageAttachment\_SetColorFilter](capi-styled-string-h.md#oh_arkui_imageattachment_setcolorfilter)同时设置时，后设置的生效。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| const [OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md)\* drawingColorFilter | 图片颜色滤镜。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_GetDrawingColorFilter()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_GetDrawingColorFilter(const OH_ArkUI_ImageAttachment* imageAttachment, OH_Drawing_ColorFilter* drawingColorFilter)
```

**描述**

获取图片样式中的图片颜色滤镜。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| [OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md)\* drawingColorFilter | 图片颜色滤镜。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_SetSyncLoad()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_SetSyncLoad(OH_ArkUI_ImageAttachment* imageAttachment, bool syncLoad)
```

**描述**

设置图片样式中是否同步加载图片。

**说明** 

此属性仅在通过[OH\_ArkUI\_ImageAttachment\_SetResource](capi-styled-string-h.md#oh_arkui_imageattachment_setresource)设置图片源为资源地址时生效。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| bool syncLoad | 是否同步加载图片。true表示同步加载，同步加载时阻塞UI线程，不会显示占位图；false表示异步加载。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_GetSyncLoad()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_GetSyncLoad(const OH_ArkUI_ImageAttachment* imageAttachment, bool* syncLoad)
```

**描述**

获取图片样式中是否同步加载图片。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| bool\* syncLoad | 是否同步加载图片。true表示同步加载；false表示异步加载。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_SetSupportSvg()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_SetSupportSvg(OH_ArkUI_ImageAttachment* imageAttachment, bool supportSvg)
```

**描述**

设置图片样式中是否开启SVG标签解析能力增强功能。开启后可解析更丰富的SVG标签及属性，提升SVG图片的渲染兼容性。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| bool supportSvg | 是否开启SVG标签解析能力增强功能。true表示开启；false表示不开启。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ImageAttachment\_GetSupportSvg()

```c
ArkUI_ErrorCode OH_ArkUI_ImageAttachment_GetSupportSvg(const OH_ArkUI_ImageAttachment* imageAttachment, bool* supportSvg)
```

**描述**

获取图片样式中是否开启SVG标签解析能力增强功能。开启后可解析更丰富的SVG标签及属性，提升SVG图片的渲染兼容性。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)\* imageAttachment | 指向[OH\_ArkUI\_ImageAttachment](capi-arkui-nativemodule-oh-arkui-imageattachment.md)对象的指针。 |
| bool\* supportSvg | 是否开启SVG标签解析能力增强功能。true表示开启；false表示未开启。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextEditorChangeEvent\_GetRangeBefore()

```c
ArkUI_ErrorCode OH_ArkUI_TextEditorChangeEvent_GetRangeBefore(const OH_ArkUI_TextEditorChangeEvent* event, uint32_t* start, uint32_t* end)
```

**描述**

获取文本变化信息中待被替换的原文本的范围。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH\_ArkUI\_TextEditorChangeEvent\* event | 指向[OH\_ArkUI\_TextEditorChangeEvent](capi-arkui-nativemodule-oh-arkui-texteditorchangeevent.md)对象的指针。 |
| uint32\_t\* start | 待替换内容范围的起始索引。 |
| uint32\_t\* end | 待替换内容范围的结束索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextEditorChangeEvent\_GetReplacementStyledString()

```c
ArkUI_ErrorCode OH_ArkUI_TextEditorChangeEvent_GetReplacementStyledString(const OH_ArkUI_TextEditorChangeEvent* event, ArkUI_StyledString_Descriptor* descriptor)
```

**描述**

获取文本变化信息中的用于替换的属性字符串。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH\_ArkUI\_TextEditorChangeEvent\* event | 指向[OH\_ArkUI\_TextEditorChangeEvent](capi-arkui-nativemodule-oh-arkui-texteditorchangeevent.md)对象的指针。 |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextEditorChangeEvent\_GetPreviewStyledString()

```c
ArkUI_ErrorCode OH_ArkUI_TextEditorChangeEvent_GetPreviewStyledString(const OH_ArkUI_TextEditorChangeEvent* event, ArkUI_StyledString_Descriptor* descriptor)
```

**描述**

获取文本变化信息中的预览内容属性字符串。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH\_ArkUI\_TextEditorChangeEvent\* event | 指向[OH\_ArkUI\_TextEditorChangeEvent](capi-arkui-nativemodule-oh-arkui-texteditorchangeevent.md)对象的指针。 |
| [ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)\* descriptor | 指向[ArkUI\_StyledString\_Descriptor](capi-arkui-nativemodule-arkui-styledstring-descriptor.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextLayoutManager\_Dispose()

```c
void OH_ArkUI_TextLayoutManager_Dispose(ArkUI_TextLayoutManager* layoutManager)
```

**描述**

释放文本布局管理器对象占用的内存。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextLayoutManager](capi-arkui-nativemodule-arkui-textlayoutmanager.md)\* layoutManager | 指向ArkUI\_TextLayoutManager对象的指针。 |

### OH\_ArkUI\_TextLayoutManager\_GetLineCount()

```c
ArkUI_ErrorCode OH_ArkUI_TextLayoutManager_GetLineCount(ArkUI_TextLayoutManager* layoutManager, int32_t* outLineCount)
```

**描述**

获取文本行数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextLayoutManager](capi-arkui-nativemodule-arkui-textlayoutmanager.md)\* layoutManager | 指向ArkUI\_TextLayoutManager对象的指针。 |
| int32\_t\* outLineCount | 文本行数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextLayoutManager\_GetRectsForRange()

```c
ArkUI_ErrorCode OH_ArkUI_TextLayoutManager_GetRectsForRange(ArkUI_TextLayoutManager* layoutManager, int32_t start, int32_t end, OH_Drawing_RectWidthStyle widthStyle, OH_Drawing_RectHeightStyle heightStyle, OH_Drawing_TextBox** outTextBoxes)
```

**描述**

获取给定的矩形区域宽度样式以及高度样式的规格下，文本中任意区间范围内的字符或占位符所占的绘制区域信息。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextLayoutManager](capi-arkui-nativemodule-arkui-textlayoutmanager.md)\* layoutManager | 指向ArkUI\_TextLayoutManager对象的指针。 |
| int32\_t start | 起始位置索引，start取值需要大于等于0，否则会返回参数异常。 |
| int32\_t end | 结束位置索引，end取值需要大于等于start，否则会返回参数异常。 |
| [OH\_Drawing\_RectWidthStyle](capi-drawing-text-typography-h.md#oh_drawing_rectwidthstyle) widthStyle | 矩形区域宽度样式。 |
| [OH\_Drawing\_RectHeightStyle](capi-drawing-text-typography-h.md#oh_drawing_rectheightstyle) heightStyle | 矩形区域高度样式。 |
| [OH\_Drawing\_TextBox](capi-drawing-oh-drawing-textbox.md)\*\* outTextBoxes | 指向OH\_Drawing\_TextBox对象的二级指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextLayoutManager\_GetGlyphPositionAtCoordinate()

```c
ArkUI_ErrorCode OH_ArkUI_TextLayoutManager_GetGlyphPositionAtCoordinate(ArkUI_TextLayoutManager* layoutManager, double dx, double dy, OH_Drawing_PositionAndAffinity** outPos)
```

**描述**

获取距离给定坐标最近的字符位置信息。返回的位置索引为UTF-16字符偏移量而非字形偏移量。字形(glyph)为渲染视觉单位，与字符(character)可能存在多对多映射关系。例如文本为“世界Hello”，其字形索引范围为[0, 7]，对应的UTF-8字符索引范围为[0, 11]，UTF-16字符索引范围为[0, 7]。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextLayoutManager](capi-arkui-nativemodule-arkui-textlayoutmanager.md)\* layoutManager | 指向ArkUI\_TextLayoutManager对象的指针。 |
| double dx | 相对于控件的x坐标，单位为px。 |
| double dy | 相对于控件的y坐标，单位为px。 |
| [OH\_Drawing\_PositionAndAffinity](capi-drawing-oh-drawing-positionandaffinity.md)\*\* outPos | 指向OH\_Drawing\_PositionAndAffinity对象的二级指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextLayoutManager\_GetLineMetrics()

```c
ArkUI_ErrorCode OH_ArkUI_TextLayoutManager_GetLineMetrics(ArkUI_TextLayoutManager* layoutManager, int32_t lineNumber, OH_Drawing_LineMetrics* outMetrics)
```

**描述**

获取指定行的行信息、文本样式信息、以及字体属性信息。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextLayoutManager](capi-arkui-nativemodule-arkui-textlayoutmanager.md)\* layoutManager | 指向ArkUI\_TextLayoutManager对象的指针。 |
| int32\_t lineNumber | 指定行的行号索引，行号索引从0开始计数，lineNumber小于0或大于等于文本行数时会返回参数异常。 |
| [OH\_Drawing\_LineMetrics](capi-drawing-oh-drawing-linemetrics.md)\* outMetrics | 指向OH\_Drawing\_LineMetrics对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextLayoutManager\_GetCharacterPositionAtCoordinate()

```c
ArkUI_ErrorCode OH_ArkUI_TextLayoutManager_GetCharacterPositionAtCoordinate(ArkUI_TextLayoutManager* layoutManager, double dx, double dy, OH_Drawing_PositionAndAffinity** outPos)
```

**描述**

获取距离指定坐标最近的字符的位置信息。

与OH\_ArkUI\_TextLayoutManager\_GetGlyphPositionAtCoordinate的区别：此方法返回字符级别的位置信息，适用于文本编辑、光标定位等基于字符编码的场景；而GetGlyphPositionAtCoordinate返回字形级别的位置信息，适用于渲染相关的精确定位场景。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextLayoutManager](capi-arkui-nativemodule-arkui-textlayoutmanager.md)\* layoutManager | 指向[ArkUI\_TextLayoutManager](capi-arkui-nativemodule-arkui-textlayoutmanager.md)对象的指针。 |
| double dx | 相对于控件的x坐标，单位为px。 |
| double dy | 相对于控件的y坐标，单位为px。 |
| [OH\_Drawing\_PositionAndAffinity](capi-drawing-oh-drawing-positionandaffinity.md)\*\* outPos | 指向[OH\_Drawing\_PositionAndAffinity](capi-drawing-oh-drawing-positionandaffinity.md)对象的二级指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextLayoutManager\_GetGlyphRangeForCharacterRange()

```c
ArkUI_ErrorCode OH_ArkUI_TextLayoutManager_GetGlyphRangeForCharacterRange(ArkUI_TextLayoutManager* layoutManager, OH_Drawing_Range* charRange, OH_Drawing_Range** outGlyphRange,
OH_Drawing_Range** outActualCharRange);
```

**描述**

获取由指定字符索引范围所生成的字形索引范围以及实际的字符索引范围。例如文本为“世界Hello”，其中文本“世”的字形索引范围为[0, 1]，一个汉字占三个字符，所以其对应的字符索引范围为[0, 3]。如果指定的字符索引范围是[0, 1]，但无法解析出三分之一个汉字，所以实际的字符索引范围是[0, 3]。outGlyphRange、outActualCharRange返回的[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象在使用完成后，需通过[OH\_Drawing\_ReleaseRangeBuffer](capi-drawing-text-typography-h.md#oh_drawing_releaserangebuffer)释放。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextLayoutManager](capi-arkui-nativemodule-arkui-textlayoutmanager.md)\* layoutManager | 指向[ArkUI\_TextLayoutManager](capi-arkui-nativemodule-arkui-textlayoutmanager.md)对象的指针。 |
| [OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)\* charRange | 指向[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象的指针，表示字符索引范围。 |
| [OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)\*\* outGlyphRange | 指向[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象的二级指针，表示字形索引范围。 |
| [OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)\*\* outActualCharRange | 指向[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象的二级指针，表示实际的字符索引范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextLayoutManager\_GetCharacterRangeForGlyphRange()

```c
ArkUI_ErrorCode OH_ArkUI_TextLayoutManager_GetCharacterRangeForGlyphRange(ArkUI_TextLayoutManager* layoutManager, OH_Drawing_Range* glyphRange, OH_Drawing_Range** outCharRange,
OH_Drawing_Range** outActualGlyphRange)
```

**描述**

获取由指定字形索引范围所生成的字符索引范围以及实际的字形索引范围。例如文本为“世界Hello”，其字形索引范围为[0, 7]，一个汉字占三个字符，所以其对应的字符索引范围为[0, 11]。如果指定的索引范围是[0, 11]，但字形一共只有7个，所以实际的字形索引范围是[0, 7]。outCharRange、outActualGlyphRange返回的[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象在使用完成后，需通过[OH\_Drawing\_ReleaseRangeBuffer](capi-drawing-text-typography-h.md#oh_drawing_releaserangebuffer)释放。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextLayoutManager](capi-arkui-nativemodule-arkui-textlayoutmanager.md)\* layoutManager | 指向[ArkUI\_TextLayoutManager](capi-arkui-nativemodule-arkui-textlayoutmanager.md)对象的指针。 |
| [OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)\* glyphRange | 指向[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象的指针，表示字形索引范围。 |
| [OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)\*\* outCharRange | 指向[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象的二级指针，表示字符索引范围。 |
| [OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)\*\* outActualGlyphRange | 指向[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象的二级指针，表示实际的字形索引范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextLayoutManager\_GetCharacterPositionAtCoordinateWithEncoding()

```c
ArkUI_ErrorCode OH_ArkUI_TextLayoutManager_GetCharacterPositionAtCoordinateWithEncoding(ArkUI_TextLayoutManager* layoutManager, double dx, double dy, OH_ArkUI_TextEncoding encoding, OH_Drawing_PositionAndAffinity** outPos)
```

**描述**

根据指定编码类型，获取距离指定坐标最近的字符位置信息。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextLayoutManager](capi-arkui-nativemodule-arkui-textlayoutmanager.md)\* layoutManager | 指向[ArkUI\_TextLayoutManager](capi-arkui-nativemodule-arkui-textlayoutmanager.md)对象的指针。 |
| double dx | 相对于控件的x坐标，单位为px。 |
| double dy | 相对于控件的y坐标，单位为px。 |
| [OH\_ArkUI\_TextEncoding](capi-styled-string-h.md#oh_arkui_textencoding) encoding | 字符位置使用的编码类型。 |
| [OH\_Drawing\_PositionAndAffinity](capi-drawing-oh-drawing-positionandaffinity.md)\*\* outPos | 指向[OH\_Drawing\_PositionAndAffinity](capi-drawing-oh-drawing-positionandaffinity.md)对象的二级指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextLayoutManager\_GetGlyphRangeForCharacterRangeWithEncoding()

```c
ArkUI_ErrorCode OH_ArkUI_TextLayoutManager_GetGlyphRangeForCharacterRangeWithEncoding(ArkUI_TextLayoutManager* layoutManager, OH_Drawing_Range* charRange, OH_ArkUI_TextEncoding encoding,
OH_Drawing_Range** outGlyphRange, OH_Drawing_Range** outActualCharRange)
```

**描述**

根据指定编码类型和文本字符范围，获取字形范围以及实际的字符范围。

**说明** 

outGlyphRange、outActualCharRange返回的[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象在使用完成后，需通过[OH\_Drawing\_ReleaseRangeBuffer](capi-drawing-text-typography-h.md#oh_drawing_releaserangebuffer)释放。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextLayoutManager](capi-arkui-nativemodule-arkui-textlayoutmanager.md)\* layoutManager | 指向[ArkUI\_TextLayoutManager](capi-arkui-nativemodule-arkui-textlayoutmanager.md)对象的指针。 |
| [OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)\* charRange | 指向[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象的指针，表示字符索引范围。 |
| [OH\_ArkUI\_TextEncoding](capi-styled-string-h.md#oh_arkui_textencoding) encoding | 字符索引范围使用的编码类型。 |
| [OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)\*\* outGlyphRange | 指向[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象的二级指针，表示字形索引范围。 |
| [OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)\*\* outActualCharRange | 指向[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象的二级指针，表示实际的字符索引范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_TextLayoutManager\_GetCharacterRangeForGlyphRangeWithEncoding()

```c
ArkUI_ErrorCode OH_ArkUI_TextLayoutManager_GetCharacterRangeForGlyphRangeWithEncoding(ArkUI_TextLayoutManager* layoutManager, OH_Drawing_Range* glyphRange, OH_ArkUI_TextEncoding encoding,
OH_Drawing_Range** outCharRange, OH_Drawing_Range** outActualGlyphRange)
```

**描述**

根据指定编码类型和文本字形范围，获取字符范围以及实际的字形范围。

**说明** 

outCharRange、outActualGlyphRange返回的[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象在使用完成后，需通过[OH\_Drawing\_ReleaseRangeBuffer](capi-drawing-text-typography-h.md#oh_drawing_releaserangebuffer)释放。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextLayoutManager](capi-arkui-nativemodule-arkui-textlayoutmanager.md)\* layoutManager | 指向[ArkUI\_TextLayoutManager](capi-arkui-nativemodule-arkui-textlayoutmanager.md)对象的指针。 |
| [OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)\* glyphRange | 指向[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象的指针，表示字形索引范围。 |
| [OH\_ArkUI\_TextEncoding](capi-styled-string-h.md#oh_arkui_textencoding) encoding | 字符索引范围使用的编码类型。 |
| [OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)\*\* outCharRange | 指向[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象的二级指针，表示字符索引范围。 |
| [OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)\*\* outActualGlyphRange | 指向[OH\_Drawing\_Range](capi-drawing-oh-drawing-range.md)对象的二级指针，表示实际的字形索引范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_SetLinearGradient()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_SetLinearGradient(OH_ArkUI_ParagraphStyle* paragraphStyle, const OH_ArkUI_LinearGradientOptions* linearGradient)
```

**描述**

设置段落样式的线性渐变。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| const [OH\_ArkUI\_LinearGradientOptions](capi-arkui-nativemodule-oh-arkui-lineargradientoptions.md)\* linearGradient | 指向[OH\_ArkUI\_LinearGradientOptions](capi-arkui-nativemodule-oh-arkui-lineargradientoptions.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_GetLinearGradient()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_GetLinearGradient(const OH_ArkUI_ParagraphStyle* paragraphStyle, OH_ArkUI_LinearGradientOptions* linearGradient)
```

**描述**

获取段落样式的线性渐变。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| [OH\_ArkUI\_LinearGradientOptions](capi-arkui-nativemodule-oh-arkui-lineargradientoptions.md)\* linearGradient | 指向[OH\_ArkUI\_LinearGradientOptions](capi-arkui-nativemodule-oh-arkui-lineargradientoptions.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_SetRadialGradient()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_SetRadialGradient(OH_ArkUI_ParagraphStyle* paragraphStyle, const OH_ArkUI_RadialGradientOptions* radialGradient)
```

**描述**

设置段落样式的径向渐变。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| const [OH\_ArkUI\_RadialGradientOptions](capi-arkui-nativemodule-oh-arkui-radialgradientoptions.md)\* radialGradient | 指向[OH\_ArkUI\_RadialGradientOptions](capi-arkui-nativemodule-oh-arkui-radialgradientoptions.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_GetRadialGradient()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_GetRadialGradient(const OH_ArkUI_ParagraphStyle* paragraphStyle, OH_ArkUI_RadialGradientOptions* radialGradient)
```

**描述**

获取段落样式的径向渐变。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| [OH\_ArkUI\_RadialGradientOptions](capi-arkui-nativemodule-oh-arkui-radialgradientoptions.md)\* radialGradient | 指向[OH\_ArkUI\_RadialGradientOptions](capi-arkui-nativemodule-oh-arkui-radialgradientoptions.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_SetTailIndents()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_SetTailIndents(OH_ArkUI_ParagraphStyle* paragraphStyle, const float* tailIndents, uint32_t size)
```

**描述**

设置段落样式的尾部缩进。

**说明** 

所有输入指针参数必须由调用者负责分配、管理和释放。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| const float\* tailIndents | 尾部缩进值数组。单位：fp。取值范围：[0, +∞)。其有效长度由size指定。若size等于1，则所有文本行使用相同的尾部缩进值tailIndents[0]；若size大于1，则第i行（从0开始计数）使用tailIndents[i]作为尾部缩进值。当文本行数超过size时，超出部分的行将复用tailIndents[size - 1]的值做缩进。 |
| uint32\_t size | tailIndents数组中有效尾部缩进值的个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ParagraphStyle\_GetTailIndents()

```c
ArkUI_ErrorCode OH_ArkUI_ParagraphStyle_GetTailIndents(const OH_ArkUI_ParagraphStyle* paragraphStyle, float** tailIndents, uint32_t tailIndentsSize, uint32_t* writeLength)
```

**描述**

获取段落样式的尾部缩进。

**说明** 

所有输入指针参数必须由调用者负责分配、管理和释放。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)\* paragraphStyle | 指向[OH\_ArkUI\_ParagraphStyle](capi-arkui-nativemodule-oh-arkui-paragraphstyle.md)对象的指针。 |
| float\*\* tailIndents | 尾部缩进值，单位为fp。 |
| uint32\_t tailIndentsSize | tailIndents缓冲区大小。 |
| uint32\_t\* writeLength | 实际写入缓冲区的尾部缩进值个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 缓冲区长度小于最小缓冲区长度。 |
