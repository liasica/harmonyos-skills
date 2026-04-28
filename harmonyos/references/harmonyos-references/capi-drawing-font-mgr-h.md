---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-font-mgr-h
title: drawing_font_mgr.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_font_mgr.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:941287e26a9fa89d2918792282850f2a8d2068dcd2ae0ed03467c6dfb2f45fa4
---

## 概述

PhonePC/2in1TabletTVWearable

文件中定义了与字体管理相关的功能函数，用于加载和匹配系统中可用的字体。

**引用文件：** <native\_drawing/drawing\_font\_mgr.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontMgr\* OH\_Drawing\_FontMgrCreate(void)](capi-drawing-font-mgr-h.md#oh_drawing_fontmgrcreate) | 创建字体管理对象，只支持管理系统字体。 |
| [void OH\_Drawing\_FontMgrDestroy(OH\_Drawing\_FontMgr\* drawingFontMgr)](capi-drawing-font-mgr-h.md#oh_drawing_fontmgrdestroy) | 释放字体管理对象占用的内存。 |
| [int OH\_Drawing\_FontMgrGetFamilyCount(OH\_Drawing\_FontMgr\* drawingFontMgr)](capi-drawing-font-mgr-h.md#oh_drawing_fontmgrgetfamilycount) | 获取字体家族的数量。 |
| [char\* OH\_Drawing\_FontMgrGetFamilyName(OH\_Drawing\_FontMgr\* drawingFontMgr, int index)](capi-drawing-font-mgr-h.md#oh_drawing_fontmgrgetfamilyname) | 由索引值获取字体家族名称。 |
| [void OH\_Drawing\_FontMgrDestroyFamilyName(char\* familyName)](capi-drawing-font-mgr-h.md#oh_drawing_fontmgrdestroyfamilyname) | 释放指定字体家族名称占用的内存。 |
| [OH\_Drawing\_FontStyleSet\* OH\_Drawing\_FontMgrCreateFontStyleSet(OH\_Drawing\_FontMgr\* drawingFontMgr, int index)](capi-drawing-font-mgr-h.md#oh_drawing_fontmgrcreatefontstyleset) | 由字体管理对象构造字体样式集对象。 |
| [void OH\_Drawing\_FontMgrDestroyFontStyleSet(OH\_Drawing\_FontStyleSet\* drawingFontStyleSet)](capi-drawing-font-mgr-h.md#oh_drawing_fontmgrdestroyfontstyleset) | 释放字体样式集对象占用的内存。 |
| [OH\_Drawing\_FontStyleSet\* OH\_Drawing\_FontMgrMatchFamily(OH\_Drawing\_FontMgr\* drawingFontMgr, const char\* familyName)](capi-drawing-font-mgr-h.md#oh_drawing_fontmgrmatchfamily) | 由指定的字体家族名称，获取字体样式集对象。 |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_FontMgrMatchFamilyStyle(OH\_Drawing\_FontMgr\* drawingFontMgr,const char\* familyName, OH\_Drawing\_FontStyleStruct fontStyle)](capi-drawing-font-mgr-h.md#oh_drawing_fontmgrmatchfamilystyle) | 根据指定的字体样式信息和字体家族名称，获取字型对象。 |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_FontMgrMatchFamilyStyleCharacter(OH\_Drawing\_FontMgr\* drawingFontMgr,const char\* familyName, OH\_Drawing\_FontStyleStruct fontStyle,const char\* bcp47[], int bcp47Count, int32\_t character)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-font-mgr-h#oh_drawing_fontmgrmatchfamilystylecharacter) | 为指定字符获取字型对象，仅在传入字体管理对象中无法找到传入UTF8字符值对应的字型对象时返回空指针。 |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_FontStyleSetCreateTypeface(OH\_Drawing\_FontStyleSet\* fontStyleSet, int index)](capi-drawing-font-mgr-h.md#oh_drawing_fontstylesetcreatetypeface) | 为指定索引获取字型对象。 |
| [OH\_Drawing\_FontStyleStruct OH\_Drawing\_FontStyleSetGetStyle(OH\_Drawing\_FontStyleSet\* fontStyleSet, int32\_t index,char\*\* styleName)](capi-drawing-font-mgr-h.md#oh_drawing_fontstylesetgetstyle) | 获取字体样式，styleName会申请内存，不再需要styleName时，请使用[OH\_Drawing\_FontStyleSetFreeStyleName](capi-drawing-font-mgr-h.md#oh_drawing_fontstylesetfreestylename)释放该对象指针。 |
| [void OH\_Drawing\_FontStyleSetFreeStyleName(char\*\* styleName)](capi-drawing-font-mgr-h.md#oh_drawing_fontstylesetfreestylename) | 释放指定字体样式名称的内存。 |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_FontStyleSetMatchStyle(OH\_Drawing\_FontStyleSet\* fontStyleSet,OH\_Drawing\_FontStyleStruct fontStyleStruct)](capi-drawing-font-mgr-h.md#oh_drawing_fontstylesetmatchstyle) | 获取最接近字体样式的字型对象。 |
| [int OH\_Drawing\_FontStyleSetCount(OH\_Drawing\_FontStyleSet\* fontStyleSet)](capi-drawing-font-mgr-h.md#oh_drawing_fontstylesetcount) | 获取字体样式集中字体的个数。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_FontMgrCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_FontMgr* OH_Drawing_FontMgrCreate(void)
```

**描述**

创建字体管理对象，只支持管理系统字体。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontMgr](capi-drawing-oh-drawing-fontmgr.md)\* | 返回指向已创建的字体管理对象[OH\_Drawing\_FontMgr](capi-drawing-oh-drawing-fontmgr.md)的指针。 |

### OH\_Drawing\_FontMgrDestroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FontMgrDestroy(OH_Drawing_FontMgr* drawingFontMgr)
```

**描述**

释放字体管理对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontMgr](capi-drawing-oh-drawing-fontmgr.md)\* drawingFontMgr | 指向字体管理对象[OH\_Drawing\_FontMgr](capi-drawing-oh-drawing-fontmgr.md)的指针，由[OH\_Drawing\_FontMgrCreate](capi-drawing-font-mgr-h.md#oh_drawing_fontmgrcreate)获取。 |

### OH\_Drawing\_FontMgrGetFamilyCount()

PhonePC/2in1TabletTVWearable

```
1. int OH_Drawing_FontMgrGetFamilyCount(OH_Drawing_FontMgr* drawingFontMgr)
```

**描述**

获取字体家族的数量。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontMgr](capi-drawing-oh-drawing-fontmgr.md)\* drawingFontMgr | 指向字体管理对象[OH\_Drawing\_FontMgr](capi-drawing-oh-drawing-fontmgr.md)的指针，由[OH\_Drawing\_FontMgrCreate](capi-drawing-font-mgr-h.md#oh_drawing_fontmgrcreate)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回字体家族的数量。 |

### OH\_Drawing\_FontMgrGetFamilyName()

PhonePC/2in1TabletTVWearable

```
1. char* OH_Drawing_FontMgrGetFamilyName(OH_Drawing_FontMgr* drawingFontMgr, int index)
```

**描述**

由索引值获取字体家族名称。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontMgr](capi-drawing-oh-drawing-fontmgr.md)\* drawingFontMgr | 指向字体管理对象[OH\_Drawing\_FontMgr](capi-drawing-oh-drawing-fontmgr.md)的指针，由[OH\_Drawing\_FontMgrCreate](capi-drawing-font-mgr-h.md#oh_drawing_fontmgrcreate)获取。 |
| int index | 用于获取对应字体家族名称的索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| char\* | 返回索引值对应的字体家族名称，不再需要时，请使用[OH\_Drawing\_FontMgrDestroyFamilyName](capi-drawing-font-mgr-h.md#oh_drawing_fontmgrdestroyfamilyname)释放该对象指针。 |

### OH\_Drawing\_FontMgrDestroyFamilyName()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FontMgrDestroyFamilyName(char* familyName)
```

**描述**

释放指定字体家族名称占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\* familyName | 指定字体家族名称数组。 |

### OH\_Drawing\_FontMgrCreateFontStyleSet()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_FontStyleSet* OH_Drawing_FontMgrCreateFontStyleSet(OH_Drawing_FontMgr* drawingFontMgr, int index)
```

**描述**

由字体管理对象构造字体样式集对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontMgr](capi-drawing-oh-drawing-fontmgr.md)\* drawingFontMgr | 指向字体管理对象[OH\_Drawing\_FontMgr](capi-drawing-oh-drawing-fontmgr.md)的指针，由[OH\_Drawing\_FontMgrCreate](capi-drawing-font-mgr-h.md#oh_drawing_fontmgrcreate)获取。 |
| int index | 用于从字体管理对象获取字体样式集对象的索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontStyleSet](capi-drawing-oh-drawing-fontstyleset.md)\* | 返回指向已创建的字体样式集对象[OH\_Drawing\_FontStyleSet](capi-drawing-oh-drawing-fontstyleset.md)的指针。 |

### OH\_Drawing\_FontMgrDestroyFontStyleSet()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FontMgrDestroyFontStyleSet(OH_Drawing_FontStyleSet* drawingFontStyleSet)
```

**描述**

释放字体样式集对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontStyleSet](capi-drawing-oh-drawing-fontstyleset.md)\* drawingFontStyleSet | 指向字体样式集对象[OH\_Drawing\_FontStyleSet](capi-drawing-oh-drawing-fontstyleset.md)的指针。 |

### OH\_Drawing\_FontMgrMatchFamily()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_FontStyleSet* OH_Drawing_FontMgrMatchFamily(OH_Drawing_FontMgr* drawingFontMgr, const char* familyName)
```

**描述**

由指定的字体家族名称，获取字体样式集对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontMgr](capi-drawing-oh-drawing-fontmgr.md)\* drawingFontMgr | 指向字体管理对象[OH\_Drawing\_FontMgr](capi-drawing-oh-drawing-fontmgr.md)的指针，由[OH\_Drawing\_FontMgrCreate](capi-drawing-font-mgr-h.md#oh_drawing_fontmgrcreate)获取。 |
| const char\* familyName | 指定的字体家族名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontStyleSet](capi-drawing-oh-drawing-fontstyleset.md)\* | 返回对应的字体样式集对象[OH\_Drawing\_FontStyleSet](capi-drawing-oh-drawing-fontstyleset.md)，不再需要时，请使用[OH\_Drawing\_FontMgrDestroyFontStyleSet](capi-drawing-font-mgr-h.md#oh_drawing_fontmgrdestroyfontstyleset)释放该对象指针。 |

### OH\_Drawing\_FontMgrMatchFamilyStyle()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Typeface* OH_Drawing_FontMgrMatchFamilyStyle(OH_Drawing_FontMgr* drawingFontMgr,const char* familyName, OH_Drawing_FontStyleStruct fontStyle)
```

**描述**

根据指定的字体样式信息和字体家族名称，获取字型对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontMgr](capi-drawing-oh-drawing-fontmgr.md)\* drawingFontMgr | 指向字体管理对象[OH\_Drawing\_FontMgr](capi-drawing-oh-drawing-fontmgr.md)的指针，由[OH\_Drawing\_FontMgrCreate](capi-drawing-font-mgr-h.md#oh_drawing_fontmgrcreate)获取。 |
| const char\* familyName | 指定的字体家族名称。 |
| [OH\_Drawing\_FontStyleStruct](capi-drawing-oh-drawing-fontstylestruct.md) fontStyle | 字体样式对象，包括字体字重、字体宽度和字体斜度信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* | 返回对应的字体样式的字型对象[OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)，不再需要时，请使用[OH\_Drawing\_TypefaceDestroy](capi-drawing-typeface-h.md#oh_drawing_typefacedestroy)释放该对象指针。 |

### OH\_Drawing\_FontMgrMatchFamilyStyleCharacter()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Typeface* OH_Drawing_FontMgrMatchFamilyStyleCharacter(OH_Drawing_FontMgr* drawingFontMgr,const char* familyName, OH_Drawing_FontStyleStruct fontStyle,const char* bcp47[], int bcp47Count, int32_t character)
```

**描述**

为指定字符获取字型对象，仅在传入字体管理对象中无法找到传入UTF8字符值对应的字型对象时返回空指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontMgr](capi-drawing-oh-drawing-fontmgr.md)\* drawingFontMgr | 指向字体管理对象[OH\_Drawing\_FontMgr](capi-drawing-oh-drawing-fontmgr.md)的指针，由[OH\_Drawing\_FontMgrCreate](capi-drawing-font-mgr-h.md#oh_drawing_fontmgrcreate)获取。 |
| const char\* familyName | 指定的字体家族名称。 |
| [OH\_Drawing\_FontStyleStruct](capi-drawing-oh-drawing-fontstylestruct.md) fontStyle | 字体样式对象，包括字体字重、字体宽度和字体斜度信息。 |
| bcp47 | 用来指示character语言编码数组，是ISO 639、15924和3166-1语言编码的组合。 |
| int bcp47Count | 参数bcp47数组大小。 |
| int32\_t character | 待匹配的UTF8字符值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* | 返回对应的字型对象[OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)。 |

### OH\_Drawing\_FontStyleSetCreateTypeface()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Typeface* OH_Drawing_FontStyleSetCreateTypeface(OH_Drawing_FontStyleSet* fontStyleSet, int index)
```

**描述**

为指定索引获取字型对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontStyleSet](capi-drawing-oh-drawing-fontstyleset.md)\* fontStyleSet | 指向字体样式集对象[OH\_Drawing\_FontStyleSet](capi-drawing-oh-drawing-fontstyleset.md)的指针。 |
| int index | 指定的字型对象的索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* | 如果成功，返回对应的字型对象[OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md); 如果失败，返回nullptr。 |

### OH\_Drawing\_FontStyleSetGetStyle()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_FontStyleStruct OH_Drawing_FontStyleSetGetStyle(OH_Drawing_FontStyleSet* fontStyleSet, int32_t index,char** styleName)
```

**描述**

获取字体样式，styleName会申请内存，不再需要styleName时，请使用[OH\_Drawing\_FontStyleSetFreeStyleName](capi-drawing-font-mgr-h.md#oh_drawing_fontstylesetfreestylename)释放该对象指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontStyleSet](capi-drawing-oh-drawing-fontstyleset.md)\* fontStyleSet | 指向字体样式集对象[OH\_Drawing\_FontStyleSet](capi-drawing-oh-drawing-fontstyleset.md)的指针。 |
| int32\_t index | 指定的字体样式的索引。 |
| char\*\* styleName | 指定字体样式名称的字符串，会申请内存，不再需要时，请使用[OH\_Drawing\_FontStyleSetFreeStyleName](capi-drawing-font-mgr-h.md#oh_drawing_fontstylesetfreestylename)释放该对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontStyleStruct](capi-drawing-oh-drawing-fontstylestruct.md) | 返回对应的字体样式。 |

### OH\_Drawing\_FontStyleSetFreeStyleName()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_FontStyleSetFreeStyleName(char** styleName)
```

**描述**

释放指定字体样式名称的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\*\* styleName | 指定字体样式名称的字符串。 |

### OH\_Drawing\_FontStyleSetMatchStyle()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Typeface* OH_Drawing_FontStyleSetMatchStyle(OH_Drawing_FontStyleSet* fontStyleSet,OH_Drawing_FontStyleStruct fontStyleStruct)
```

**描述**

获取最接近字体样式的字型对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontStyleSet](capi-drawing-oh-drawing-fontstyleset.md)\* fontStyleSet | 指向字体样式集对象[OH\_Drawing\_FontStyleSet](capi-drawing-oh-drawing-fontstyleset.md)的指针。 |
| [OH\_Drawing\_FontStyleStruct](capi-drawing-oh-drawing-fontstylestruct.md) fontStyleStruct | 字体样式对象，包括字体字重、字体宽度和字体斜度信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* | 返回对应的字型对象[OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)。 |

### OH\_Drawing\_FontStyleSetCount()

PhonePC/2in1TabletTVWearable

```
1. int OH_Drawing_FontStyleSetCount(OH_Drawing_FontStyleSet* fontStyleSet)
```

**描述**

获取字体样式集中字体的个数。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontStyleSet](capi-drawing-oh-drawing-fontstyleset.md)\* fontStyleSet | 指向字体样式集对象[OH\_Drawing\_FontStyleSet](capi-drawing-oh-drawing-fontstyleset.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回此字体样式集中字体的个数。 |
