---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-font-descriptor-h
title: drawing_text_font_descriptor.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_text_font_descriptor.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:03236cce0de2a887acf4efad17a60c383dd3622abe499db716bd3fc1cd0fec36
---

## 概述

定义了字体信息的相关接口，比如获取字体信息、查找和匹配指定字体、读取字体描述符属性以及获取字体的Unicode码和字体数量等。

**引用文件：** <native\_drawing/drawing\_text\_font\_descriptor.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 14

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_FontVariationInstanceCoordinate](capi-drawing-oh-drawing-fontvariationinstancecoordinate.md) | OH\_Drawing\_FontVariationInstanceCoordinate | 可变字体属性键值对。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_SystemFontType](capi-drawing-text-font-descriptor-h.md#oh_drawing_systemfonttype) | OH\_Drawing\_SystemFontType | 字体类型的枚举。 |
| [OH\_Drawing\_FontFullDescriptorAttributeId](capi-drawing-text-font-descriptor-h.md#oh_drawing_fontfulldescriptorattributeid) | OH\_Drawing\_FontFullDescriptorAttributeId | 字体描述符属性的枚举。不同类型的字体描述符属性，请使用对应类型的接口获取属性。如字体描述符属性FULL\_DESCRIPTOR\_ATTR\_I\_WEIGHT为int类型，需使用[OH\_Drawing\_GetFontFullDescriptorAttributeInt](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontfulldescriptorattributeint)接口获取其属性值。 |
| [OH\_Drawing\_FontVariationAxisAttributeId](capi-drawing-text-font-descriptor-h.md#oh_drawing_fontvariationaxisattributeid) | OH\_Drawing\_FontVariationAxisAttributeId | 字体可变轴属性的枚举。 |
| [OH\_Drawing\_FontVariationInstanceAttributeId](capi-drawing-text-font-descriptor-h.md#oh_drawing_fontvariationinstanceattributeid) | OH\_Drawing\_FontVariationInstanceAttributeId | 字体可变实例属性的枚举。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontDescriptor\* OH\_Drawing\_MatchFontDescriptors(OH\_Drawing\_FontDescriptor\* desc, size\_t\* num)](capi-drawing-text-font-descriptor-h.md#oh_drawing_matchfontdescriptors) | 获取与指定字体描述符匹配的所有系统字体描述符，其中[OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)的path字段不作为有效的匹配字段，其余字段不是默认值时生效。  如果参数desc的所有字段都是默认值，则获取所有系统字体描述符。  如果匹配失败，返回NULL。不再需要[OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)时，请使用[OH\_Drawing\_DestroyFontDescriptors](capi-drawing-text-font-descriptor-h.md#oh_drawing_destroyfontdescriptors)接口释放该对象的指针。 |
| [void OH\_Drawing\_DestroyFontDescriptors(OH\_Drawing\_FontDescriptor\* descriptors, size\_t num)](capi-drawing-text-font-descriptor-h.md#oh_drawing_destroyfontdescriptors) | 释放字体描述符[OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)数组。 |
| [OH\_Drawing\_FontDescriptor\* OH\_Drawing\_GetFontDescriptorByFullName(const OH\_Drawing\_String\* fullName, OH\_Drawing\_SystemFontType fontType)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontdescriptorbyfullname) | 根据字体名称和字体类型获取指定的字体描述符，支持系统字体、风格字体和用户已安装字体，如果获取失败则返回NULL。  字体描述符是描述字体特征的一种数据结构，它包含了定义字体外观和属性的详细信息。 |
| [OH\_Drawing\_Array\* OH\_Drawing\_GetSystemFontFullNamesByType(OH\_Drawing\_SystemFontType fontType)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getsystemfontfullnamesbytype) | 根据字体类型获取对应字体的字体名称数组。 |
| [const OH\_Drawing\_String\* OH\_Drawing\_GetSystemFontFullNameByIndex(OH\_Drawing\_Array\* fullNameArray, size\_t index)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getsystemfontfullnamebyindex) | 在字体名称数组中通过索引获取对应位置的字体名称，如果索引超出范围或数组无效，则返回NULL。 |
| [void OH\_Drawing\_DestroySystemFontFullNames(OH\_Drawing\_Array\* fullNameArray)](capi-drawing-text-font-descriptor-h.md#oh_drawing_destroysystemfontfullnames) | 释放通过字体类型获取的对应字体的字体名称数组占用的内存。 |
| [OH\_Drawing\_Array\* OH\_Drawing\_GetFontFullDescriptorsFromStream(const void\* data, size\_t size)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontfulldescriptorsfromstream) | 根据原始二进制数据获取字体描述符数组。 |
| [OH\_Drawing\_Array\* OH\_Drawing\_GetFontFullDescriptorsFromPath(const char\* path)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontfulldescriptorsfrompath) | 根据字体文件路径获取字体描述符数组。 |
| [const OH\_Drawing\_FontFullDescriptor\* OH\_Drawing\_GetFontFullDescriptorByIndex(OH\_Drawing\_Array\* descriptorArray, size\_t index)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontfulldescriptorbyindex) | 在字体描述符数组中通过索引获取对应的字体描述符。 |
| [void OH\_Drawing\_DestroyFontFullDescriptors(OH\_Drawing\_Array\* descriptorArray)](capi-drawing-text-font-descriptor-h.md#oh_drawing_destroyfontfulldescriptors) | 释放字体描述符数组占用的内存。 |
| [void OH\_Drawing\_DestroyFontFullDescriptor(const OH\_Drawing\_FontFullDescriptor\* descriptor)](capi-drawing-text-font-descriptor-h.md#oh_drawing_destroyfontfulldescriptor) | 释放字体描述符指针占用的内存。本函数可用于释放由[OH\_Drawing\_GetFontFullDescriptorByFullName](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontfulldescriptorbyfullname)接口获取的字体描述符指针。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetFontFullDescriptorAttributeInt(const OH\_Drawing\_FontFullDescriptor\* descriptor, OH\_Drawing\_FontFullDescriptorAttributeId id, int\* value)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontfulldescriptorattributeint) | 获取int类型字体描述符的属性。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetFontFullDescriptorAttributeBool(const OH\_Drawing\_FontFullDescriptor\* descriptor, OH\_Drawing\_FontFullDescriptorAttributeId id, bool\* value)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontfulldescriptorattributebool) | 获取bool类型字体描述符的属性。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetFontFullDescriptorAttributeString(const OH\_Drawing\_FontFullDescriptor\* descriptor, OH\_Drawing\_FontFullDescriptorAttributeId id, OH\_Drawing\_String\* str)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontfulldescriptorattributestring) | 获取[OH\_Drawing\_String](capi-drawing-oh-drawing-string.md)类型字体描述符的属性。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetFontUnicodeArrayFromFile(const char\* fontSrc, uint32\_t index, int32\_t\*\* unicodeArray, int32\_t\* arrayLength)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontunicodearrayfromfile) | 从字体文件中获取unicode码数组。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetFontUnicodeArrayFromBuffer(uint8\_t\* fontBuffer, size\_t length, uint32\_t index, int32\_t\*\* unicodeArray, int32\_t\* arrayLength)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontunicodearrayfrombuffer) | 从字体字节流缓存中获取unicode码数组。 |
| [uint32\_t OH\_Drawing\_GetFontCountFromFile(const char\* fontSrc)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontcountfromfile) | 获取字体文件中包含的字体数量。 |
| [uint32\_t OH\_Drawing\_GetFontCountFromBuffer(uint8\_t\* fontBuffer, size\_t length)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontcountfrombuffer) | 获取字体缓存数据中包含的字体数量。 |
| [OH\_Drawing\_String\* OH\_Drawing\_GetFontPathsByType(OH\_Drawing\_SystemFontType fontType, size\_t\* pathCount)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontpathsbytype) | 获取指定字体类型的所有字体文件路径。 |
| [OH\_Drawing\_Array\* OH\_Drawing\_GetFontFullDescriptorAttributeArray(const OH\_Drawing\_FontFullDescriptor\* descriptor, OH\_Drawing\_FontFullDescriptorAttributeId id)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontfulldescriptorattributearray) | 获取字体描述符的对象数组属性。 |
| [OH\_Drawing\_FontVariationAxis\* OH\_Drawing\_GetFontVariationAxisByIndex(OH\_Drawing\_Array\* array, size\_t index)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontvariationaxisbyindex) | 在字体可变轴数组中通过索引获取对应的字体可变轴。 |
| [void OH\_Drawing\_DestroyFontVariationAxis(OH\_Drawing\_Array\* fontVariaAxisArray)](capi-drawing-text-font-descriptor-h.md#oh_drawing_destroyfontvariationaxis) | 释放字体可变轴数组占用的内存。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetFontVariationAxisAttributeDouble(OH\_Drawing\_FontVariationAxis\* variationAxis, OH\_Drawing\_FontVariationAxisAttributeId id, double \*value)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontvariationaxisattributedouble) | 获取double类型字体可变轴的属性。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetFontVariationAxisAttributeInt(OH\_Drawing\_FontVariationAxis\* variationAxis, OH\_Drawing\_FontVariationAxisAttributeId id, int \*value)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontvariationaxisattributeint) | 获取int类型字体可变轴的属性。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetFontVariationAxisAttributeStr(OH\_Drawing\_FontVariationAxis\* variationAxis, OH\_Drawing\_FontVariationAxisAttributeId id, OH\_Drawing\_String \*str)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontvariationaxisattributestr) | 获取[OH\_Drawing\_String](capi-drawing-oh-drawing-string.md)类型字体可变轴的属性。 |
| [OH\_Drawing\_FontVariationInstance\* OH\_Drawing\_GetFontVariationInstanceByIndex(OH\_Drawing\_Array\* array, size\_t index)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontvariationinstancebyindex) | 在字体可变实例数组中通过索引获取对应的字体可变实例。 |
| [void OH\_Drawing\_DestroyFontVariationInstance(OH\_Drawing\_Array\* fontVariaAxisInstance)](capi-drawing-text-font-descriptor-h.md#oh_drawing_destroyfontvariationinstance) | 释放字体可变实例数组占用的内存。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetFontVariationInstanceAttributeStr(OH\_Drawing\_FontVariationInstance\* variationInstance, OH\_Drawing\_FontVariationInstanceAttributeId id, OH\_Drawing\_String\* str)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontvariationinstanceattributestr) | 获取[OH\_Drawing\_String](capi-drawing-oh-drawing-string.md)类型字体可变实例的属性。 |
| [OH\_Drawing\_FontVariationInstanceCoordinate\* OH\_Drawing\_GetFontVariationInstanceCoordinate(OH\_Drawing\_FontVariationInstance\* variationInstance, size\_t\* arrayLength)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontvariationinstancecoordinate) | 获取字体可变实例的可变字体属性对象。 |
| [const OH\_Drawing\_FontFullDescriptor\* OH\_Drawing\_GetFontFullDescriptorByFullName(const OH\_Drawing\_String\* fullName, OH\_Drawing\_SystemFontType fontType)](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontfulldescriptorbyfullname) | 根据字体名称和字体类型获取字体完整描述符对象。 |

## 枚举类型说明

### OH\_Drawing\_SystemFontType

```c
enum OH_Drawing_SystemFontType
```

**描述**

字体类型的枚举。

**起始版本：** 14

| 枚举项 | 描述 |
| --- | --- |
| ALL = 1 << 0 | 所有字体类型。 |
| GENERIC = 1 << 1 | 系统字体类型。 |
| STYLISH = 1 << 2 | 风格字体类型。 |
| INSTALLED = 1 << 3 | 用户已安装字体类型。 |
| CUSTOMIZED = 1 << 4 | 自定义字体类型。  **起始版本：** 18 |

### OH\_Drawing\_FontFullDescriptorAttributeId

```c
enum OH_Drawing_FontFullDescriptorAttributeId
```

**描述**

字体描述符属性的枚举。不同类型的字体描述符属性，请使用对应类型的接口获取属性。如字体描述符属性FULL\_DESCRIPTOR\_ATTR\_I\_WEIGHT为int类型，需使用[OH\_Drawing\_GetFontFullDescriptorAttributeInt](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontfulldescriptorattributeint)接口获取其属性值。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| FULL\_DESCRIPTOR\_ATTR\_S\_PATH = 0 | 字体文件的路径，[OH\_Drawing\_String](capi-drawing-oh-drawing-string.md)类型。 |
| FULL\_DESCRIPTOR\_ATTR\_S\_POSTSCRIPT\_NAME = 1 | 唯一标识字体的名称，[OH\_Drawing\_String](capi-drawing-oh-drawing-string.md)类型。 |
| FULL\_DESCRIPTOR\_ATTR\_S\_FULL\_NAME = 2 | 字体的名称，[OH\_Drawing\_String](capi-drawing-oh-drawing-string.md)类型。 |
| FULL\_DESCRIPTOR\_ATTR\_S\_FAMILY\_NAME = 3 | 字体家族的名称，[OH\_Drawing\_String](capi-drawing-oh-drawing-string.md)类型。 |
| FULL\_DESCRIPTOR\_ATTR\_S\_SUB\_FAMILY\_NAME = 4 | 子字体家族的名称，[OH\_Drawing\_String](capi-drawing-oh-drawing-string.md)类型。 |
| FULL\_DESCRIPTOR\_ATTR\_I\_WEIGHT = 5 | 字体的字重，int类型。 |
| FULL\_DESCRIPTOR\_ATTR\_I\_WIDTH = 6 | 字体的宽窄风格属性，int类型。 |
| FULL\_DESCRIPTOR\_ATTR\_I\_ITALIC = 7 | 字体是否倾斜，int类型。1表示字体倾斜，0表示字体非倾斜。 |
| FULL\_DESCRIPTOR\_ATTR\_B\_MONO = 8 | 字体是否等宽，bool类型。true表示字体等宽，false表示字体非等宽。 |
| FULL\_DESCRIPTOR\_ATTR\_B\_SYMBOLIC = 9 | 字体是否支持符号字体，bool类型。true表示支持符号字体，false表示不支持符号字体。 |
| FULL\_DESCRIPTOR\_ATTR\_S\_LOCAL\_POSTSCRIPT\_NAME = 10 | 根据系统语言配置提取字体唯一标识的名称。  **起始版本：** 23 |
| FULL\_DESCRIPTOR\_ATTR\_S\_LOCAL\_FULL\_NAME = 11 | 根据系统语言配置提取字体全名。  **起始版本：** 23 |
| FULL\_DESCRIPTOR\_ATTR\_S\_LOCAL\_FAMILY\_NAME = 12 | 根据系统语言配置提取字体家族名称。  **起始版本：** 23 |
| FULL\_DESCRIPTOR\_ATTR\_S\_LOCAL\_SUB\_FAMILY\_NAME = 13 | 根据系统语言配置提取子字体家族名称。  **起始版本：** 23 |
| FULL\_DESCRIPTOR\_ATTR\_S\_VERSION = 14 | 字体版本。  **起始版本：** 23 |
| FULL\_DESCRIPTOR\_ATTR\_S\_MANUFACTURE = 15 | 字体制造商信息。  **起始版本：** 23 |
| FULL\_DESCRIPTOR\_ATTR\_S\_COPYRIGHT = 16 | 字体版权信息。  **起始版本：** 23 |
| FULL\_DESCRIPTOR\_ATTR\_S\_TRADEMARK = 17 | 字体商标信息。  **起始版本：** 23 |
| FULL\_DESCRIPTOR\_ATTR\_S\_LICENSE = 18 | 字体许可证信息。  **起始版本：** 23 |
| FULL\_DESCRIPTOR\_ATTR\_O\_VARIATION\_AXIS = 19 | 字体可变轴数组。  **起始版本：** 24 |
| FULL\_DESCRIPTOR\_ATTR\_O\_VARIATION\_INSTANCE = 20 | 字体可变实例数组。  **起始版本：** 24 |
| FULL\_DESCRIPTOR\_ATTR\_I\_INDEX = 21 | 字体索引。  **起始版本：** 23 |

### OH\_Drawing\_FontVariationAxisAttributeId

```c
enum OH_Drawing_FontVariationAxisAttributeId
```

**描述**

字体可变轴属性的枚举。

**起始版本：** 24

| 枚举项 | 描述 |
| --- | --- |
| FONT\_VARIATION\_AXIS\_ATTR\_S\_KEY = 0 | 字体可变轴的关键字标识。 |
| FONT\_VARIATION\_AXIS\_ATTR\_D\_MIN\_VALUE = 1 | 字体可变轴的最小值。 |
| FONT\_VARIATION\_AXIS\_ATTR\_D\_MAX\_VALUE = 2 | 字体可变轴的最大值。 |
| FONT\_VARIATION\_AXIS\_ATTR\_D\_DEFAULT\_VALUE = 3 | 字体可变轴的默认值。 |
| FONT\_VARIATION\_AXIS\_ATTR\_I\_FLAGS = 4 | 字体可变轴的标志位。值为0时表示该轴对用户可见，值为1时表示该轴应隐藏。 |
| FONT\_VARIATION\_AXIS\_ATTR\_S\_NAME = 5 | 字体可变轴的英文名称。 |
| FONT\_VARIATION\_AXIS\_ATTR\_S\_LOCAL\_NAME = 6 | 字体可变轴的本地化名称。 |

### OH\_Drawing\_FontVariationInstanceAttributeId

```c
enum OH_Drawing_FontVariationInstanceAttributeId
```

**描述**

字体可变实例属性的枚举。

**起始版本：** 24

| 枚举项 | 描述 |
| --- | --- |
| FONT\_VARIATION\_INSTANCE\_ATTR\_S\_NAME = 0 | 字体可变实例的英文名称。 |
| FONT\_VARIATION\_INSTANCE\_ATTR\_S\_LOCAL\_NAME = 1 | 字体可变实例的本地化名称。 |

## 函数说明

### OH\_Drawing\_MatchFontDescriptors()

```c
OH_Drawing_FontDescriptor* OH_Drawing_MatchFontDescriptors(OH_Drawing_FontDescriptor* desc, size_t* num)
```

**描述**

获取与指定字体描述符匹配的所有系统字体描述符，其中[OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)的path字段不作为有效的匹配字段，其余字段不是默认值时生效。

如果参数desc的所有字段都是默认值，则获取所有系统字体描述符。

如果匹配失败，返回NULL。不再需要[OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)时，请使用[OH\_Drawing\_DestroyFontDescriptors](capi-drawing-text-font-descriptor-h.md#oh_drawing_destroyfontdescriptors)接口释放该对象的指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)\* desc | 指向字体描述符[OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)对象的指针。  建议使用[OH\_Drawing\_CreateFontDescriptor](capi-drawing-text-typography-h.md#oh_drawing_createfontdescriptor)获得有效的[OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)实例。  如果自己创建[OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)实例，请确保不用于匹配的字段是默认值。 |
| size\_t\* num | 出参，用于接收返回值数组的成员个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)\* | [OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)数组，释放时请使用[OH\_Drawing\_DestroyFontDescriptors](capi-drawing-text-font-descriptor-h.md#oh_drawing_destroyfontdescriptors)。 |

### OH\_Drawing\_DestroyFontDescriptors()

```c
void OH_Drawing_DestroyFontDescriptors(OH_Drawing_FontDescriptor* descriptors, size_t num)
```

**描述**

释放字体描述符[OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)数组。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)\* descriptors | 需要释放的字体描述符[OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)数组指针。 |
| size\_t num | [OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)数组的成员个数。 |

### OH\_Drawing\_GetFontDescriptorByFullName()

```c
OH_Drawing_FontDescriptor* OH_Drawing_GetFontDescriptorByFullName(const OH_Drawing_String* fullName, OH_Drawing_SystemFontType fontType)
```

**描述**

根据字体名称和字体类型获取指定的字体描述符，支持系统字体、风格字体和用户已安装字体，如果获取失败则返回NULL。

字体描述符是描述字体特征的一种数据结构，它包含了定义字体外观和属性的详细信息。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_String](capi-drawing-oh-drawing-string.md)\* fullName | 表示指向字体名称字符串[OH\_Drawing\_String](capi-drawing-oh-drawing-string.md)的指针。 |
| [OH\_Drawing\_SystemFontType](capi-drawing-text-font-descriptor-h.md#oh_drawing_systemfonttype) fontType | 表示字体类型的枚举值[OH\_Drawing\_SystemFontType](capi-drawing-text-font-descriptor-h.md#oh_drawing_systemfonttype)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)\* | 指向字体描述符对象[OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)的指针，不再需要[OH\_Drawing\_FontDescriptor](capi-drawing-oh-drawing-fontdescriptor.md)时，请使用[OH\_Drawing\_DestroyFontDescriptor](capi-drawing-text-typography-h.md#oh_drawing_destroyfontdescriptor)接口释放该对象的指针。 |

### OH\_Drawing\_GetSystemFontFullNamesByType()

```c
OH_Drawing_Array* OH_Drawing_GetSystemFontFullNamesByType(OH_Drawing_SystemFontType fontType)
```

**描述**

根据字体类型获取对应字体的字体名称数组。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_SystemFontType](capi-drawing-text-font-descriptor-h.md#oh_drawing_systemfonttype) fontType | 表示字体类型的枚举值[OH\_Drawing\_SystemFontType](capi-drawing-text-font-descriptor-h.md#oh_drawing_systemfonttype)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)\* | 返回对应字体类型的字体名称数组[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)的指针，不再需要[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)时，请使用[OH\_Drawing\_DestroySystemFontFullNames](capi-drawing-text-font-descriptor-h.md#oh_drawing_destroysystemfontfullnames)接口释放该对象的指针。 |

### OH\_Drawing\_GetSystemFontFullNameByIndex()

```c
const OH_Drawing_String* OH_Drawing_GetSystemFontFullNameByIndex(OH_Drawing_Array* fullNameArray, size_t index)
```

**描述**

在字体名称数组中通过索引获取对应位置的字体名称，如果索引超出范围或数组无效，则返回NULL。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)\* fullNameArray | 表示字体名称数组[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)的指针。 |
| size\_t index | 数组的索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const [OH\_Drawing\_String](capi-drawing-oh-drawing-string.md)\* | 返回对应索引的字体名称[OH\_Drawing\_String](capi-drawing-oh-drawing-string.md)的指针。 |

### OH\_Drawing\_DestroySystemFontFullNames()

```c
void OH_Drawing_DestroySystemFontFullNames(OH_Drawing_Array* fullNameArray)
```

**描述**

释放通过字体类型获取的对应字体的字体名称数组占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)\* fullNameArray | 表示字体名称数组[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)的指针。 |

### OH\_Drawing\_GetFontFullDescriptorsFromStream()

```c
OH_Drawing_Array* OH_Drawing_GetFontFullDescriptorsFromStream(const void* data, size_t size)
```

**描述**

根据原始二进制数据获取字体描述符数组。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const void\* data | 指向原始二进制字体数据缓冲区的指针。 |
| size\_t size | 以字节为单位的字体数据缓冲区的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Array\*](capi-drawing-oh-drawing-array.md) | 返回指向对应字体文件的字体描述符数组[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)的指针，不再需要OH\_Drawing\_Array时，请使用[OH\_Drawing\_DestroyFontFullDescriptors](capi-drawing-text-font-descriptor-h.md#oh_drawing_destroyfontfulldescriptors)接口释放该对象的指针。  如果因数据格式无效或解析错误导致操作失败，返回NULL。 |

### OH\_Drawing\_GetFontFullDescriptorsFromPath()

```c
OH_Drawing_Array* OH_Drawing_GetFontFullDescriptorsFromPath(const char* path)
```

**描述**

根据字体文件路径获取字体描述符数组。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* path | 需要查询的字体文件的路径。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Array\*](capi-drawing-oh-drawing-array.md) | 返回指向对应字体文件的字体描述符数组[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)的指针，不再需要OH\_Drawing\_Array时，请使用[OH\_Drawing\_DestroyFontFullDescriptors](capi-drawing-text-font-descriptor-h.md#oh_drawing_destroyfontfulldescriptors)接口释放该对象的指针。  如果字体文件未找到、字体文件路径无效、字体文件无权限或者文件非字体格式，返回NULL。 |

### OH\_Drawing\_GetFontFullDescriptorByIndex()

```c
const OH_Drawing_FontFullDescriptor* OH_Drawing_GetFontFullDescriptorByIndex(OH_Drawing_Array* descriptorArray, size_t index)
```

**描述**

在字体描述符数组中通过索引获取对应的字体描述符。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)\* descriptorArray | 表示指向字体描述符数组[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)的指针。 |
| size\_t index | 数组的索引，索引值从0开始。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const [OH\_Drawing\_FontFullDescriptor](capi-drawing-oh-drawing-fontfulldescriptor.md)\* | 返回指向指定索引处字体描述符对象[OH\_Drawing\_FontFullDescriptor](capi-drawing-oh-drawing-fontfulldescriptor.md)的指针。  如果索引超出范围或数组无效，则返回NULL。 |

### OH\_Drawing\_DestroyFontFullDescriptors()

```c
void OH_Drawing_DestroyFontFullDescriptors(OH_Drawing_Array* descriptorArray)
```

**描述**

释放字体描述符数组占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)\* descriptorArray | 表示指向字体描述符数组[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)的指针。 |

### OH\_Drawing\_DestroyFontFullDescriptor()

```c
void OH_Drawing_DestroyFontFullDescriptor(const OH_Drawing_FontFullDescriptor* descriptor)
```

**描述**

释放字体描述符指针占用的内存。本函数可用于释放由[OH\_Drawing\_GetFontFullDescriptorByFullName](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontfulldescriptorbyfullname)接口获取的字体描述符指针。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_Drawing\_FontFullDescriptor](capi-drawing-oh-drawing-fontfulldescriptor.md)\* descriptor | 表示指向字体描述符对象[OH\_Drawing\_FontFullDescriptor](capi-drawing-oh-drawing-fontfulldescriptor.md)的指针。 |

### OH\_Drawing\_GetFontFullDescriptorAttributeInt()

```c
OH_Drawing_ErrorCode OH_Drawing_GetFontFullDescriptorAttributeInt(const OH_Drawing_FontFullDescriptor* descriptor, OH_Drawing_FontFullDescriptorAttributeId id, int* value)
```

**描述**

获取int类型字体描述符的属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_FontFullDescriptor](capi-drawing-oh-drawing-fontfulldescriptor.md)\* descriptor | 指向字体描述符对象[OH\_Drawing\_FontFullDescriptor](capi-drawing-oh-drawing-fontfulldescriptor.md)的指针。 |
| [OH\_Drawing\_FontFullDescriptorAttributeId](capi-drawing-text-font-descriptor-h.md#oh_drawing_fontfulldescriptorattributeid) id | 字体描述符属性id。从[OH\_Drawing\_FontFullDescriptorAttributeId](capi-drawing-text-font-descriptor-h.md#oh_drawing_fontfulldescriptorattributeid)中可获取字体描述符属性。 |
| int\* value | 指向int类型属性的指针。作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示参数descriptor或者value为空指针。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。 |

### OH\_Drawing\_GetFontFullDescriptorAttributeBool()

```c
OH_Drawing_ErrorCode OH_Drawing_GetFontFullDescriptorAttributeBool(const OH_Drawing_FontFullDescriptor* descriptor, OH_Drawing_FontFullDescriptorAttributeId id, bool* value)
```

**描述**

获取bool类型字体描述符的属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_FontFullDescriptor](capi-drawing-oh-drawing-fontfulldescriptor.md)\* descriptor | 指向字体描述符对象[OH\_Drawing\_FontFullDescriptor](capi-drawing-oh-drawing-fontfulldescriptor.md)的指针。 |
| [OH\_Drawing\_FontFullDescriptorAttributeId](capi-drawing-text-font-descriptor-h.md#oh_drawing_fontfulldescriptorattributeid) id | 字体描述符属性id。从[OH\_Drawing\_FontFullDescriptorAttributeId](capi-drawing-text-font-descriptor-h.md#oh_drawing_fontfulldescriptorattributeid)中可获取字体描述符属性。 |
| bool\* value | 指向bool类型属性的指针。作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示参数descriptor或者value为空指针。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。 |

### OH\_Drawing\_GetFontFullDescriptorAttributeString()

```c
OH_Drawing_ErrorCode OH_Drawing_GetFontFullDescriptorAttributeString(const OH_Drawing_FontFullDescriptor* descriptor, OH_Drawing_FontFullDescriptorAttributeId id, OH_Drawing_String* str)
```

**描述**

获取[OH\_Drawing\_String](capi-drawing-oh-drawing-string.md)类型字体描述符的属性。

**说明** 

如果不再需要OH\_Drawing\_String，调用方需要手动释放OH\_Drawing\_String结构体内部的strData成员。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_FontFullDescriptor](capi-drawing-oh-drawing-fontfulldescriptor.md)\* descriptor | 指向字体描述符对象[OH\_Drawing\_FontFullDescriptor](capi-drawing-oh-drawing-fontfulldescriptor.md)的指针。 |
| [OH\_Drawing\_FontFullDescriptorAttributeId](capi-drawing-text-font-descriptor-h.md#oh_drawing_fontfulldescriptorattributeid) id | 字体描述符属性id。从[OH\_Drawing\_FontFullDescriptorAttributeId](capi-drawing-text-font-descriptor-h.md#oh_drawing_fontfulldescriptorattributeid)中可获取字体描述符属性。 |
| [OH\_Drawing\_String](capi-drawing-oh-drawing-string.md)\* str | 指向OH\_Drawing\_String类型属性的指针。作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示参数descriptor或者str为空指针。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。 |

### OH\_Drawing\_GetFontUnicodeArrayFromFile()

```c
OH_Drawing_ErrorCode OH_Drawing_GetFontUnicodeArrayFromFile(const char* fontSrc, uint32_t index, int32_t** unicodeArray, int32_t* arrayLength)
```

**描述**

从字体文件中获取unicode码数组。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* fontSrc | 字体文件路径。 |
| uint32\_t index | ttc/otc文件中字体的索引，取值范围为[0, 字体数量-1]，非ttc/otc文件需设置为0。 |
| int32\_t\*\* unicodeArray | 出参，用于接收unicode码数组，当不需要时，使用free()释放。 |
| int32\_t\* arrayLength | 出参，用于接收unicode码数组的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示传入字体路径非法、传入非字体文件或参数unicodeArray、arrayLength为NULL。 |

### OH\_Drawing\_GetFontUnicodeArrayFromBuffer()

```c
OH_Drawing_ErrorCode OH_Drawing_GetFontUnicodeArrayFromBuffer(uint8_t* fontBuffer, size_t length, uint32_t index, int32_t** unicodeArray, int32_t* arrayLength)
```

**描述**

从字体字节流缓存中获取unicode码数组。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint8\_t\* fontBuffer | 字体文件数据。 |
| size\_t length | 字体文件数据长度。 |
| uint32\_t index | ttc/otc文件中字体的索引，取值范围为[0, 字体数量-1]，非ttc/otc文件需设置为0。 |
| int32\_t\*\* unicodeArray | 出参，用于接收unicode码数组，当不需要时，使用free()释放。 |
| int32\_t\* arrayLength | 出参，用于接收unicode码数组的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示缓存数据非法或缓存数据不是字体文件数据或参数unicodeArray、arrayLength为NULL。 |

### OH\_Drawing\_GetFontCountFromFile()

```c
uint32_t OH_Drawing_GetFontCountFromFile(const char* fontSrc)
```

**描述**

获取字体文件中包含的字体数量。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* fontSrc | 字体文件路径。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 字体数量。 |

### OH\_Drawing\_GetFontCountFromBuffer()

```c
uint32_t OH_Drawing_GetFontCountFromBuffer(uint8_t* fontBuffer, size_t length)
```

**描述**

获取字体缓存数据中包含的字体数量。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint8\_t\* fontBuffer | 字体缓存数据。 |
| size\_t length | 字体数据长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 字体数量。 |

### OH\_Drawing\_GetFontPathsByType()

```c
OH_Drawing_String* OH_Drawing_GetFontPathsByType(OH_Drawing_SystemFontType fontType, size_t* pathCount)
```

**描述**

获取指定字体类型的所有字体文件路径。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_SystemFontType](capi-drawing-text-font-descriptor-h.md#oh_drawing_systemfonttype) fontType | 系统字体类型对象 [OH\_Drawing\_SystemFontType](capi-drawing-text-font-descriptor-h.md#oh_drawing_systemfonttype) 的枚举。 |
| size\_t\* pathCount | 出参，用于接收返回的字体路径列表的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_String\*](capi-drawing-oh-drawing-string.md) | 返回字体路径列表。不再需要时，请使用free释放该对象指针以及每个OH\_Drawing\_String对象内部持有的指针。 |

### OH\_Drawing\_GetFontFullDescriptorAttributeArray()

```c
OH_Drawing_Array* OH_Drawing_GetFontFullDescriptorAttributeArray(const OH_Drawing_FontFullDescriptor* descriptor, OH_Drawing_FontFullDescriptorAttributeId id)
```

**描述**

获取字体描述符的对象数组属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_Drawing\_FontFullDescriptor](capi-drawing-oh-drawing-fontfulldescriptor.md)\* descriptor | 指向字体描述符对象[OH\_Drawing\_FontFullDescriptor](capi-drawing-oh-drawing-fontfulldescriptor.md)的指针。 |
| [OH\_Drawing\_FontFullDescriptorAttributeId](capi-drawing-text-font-descriptor-h.md#oh_drawing_fontfulldescriptorattributeid) id | 字体描述符属性id。从[OH\_Drawing\_FontFullDescriptorAttributeId](capi-drawing-text-font-descriptor-h.md#oh_drawing_fontfulldescriptorattributeid)中可获取字体描述符属性。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Array\*](capi-drawing-oh-drawing-array.md) | 返回对象数组，获取失败时返回NULL。当id为FULL\_DESCRIPTOR\_ATTR\_O\_VARIATION\_AXIS时，不再需要时请使用[OH\_Drawing\_DestroyFontVariationAxis](capi-drawing-text-font-descriptor-h.md#oh_drawing_destroyfontvariationaxis)接口释放；当id为FULL\_DESCRIPTOR\_ATTR\_O\_VARIATION\_INSTANCE时，不再需要时请使用[OH\_Drawing\_DestroyFontVariationInstance](capi-drawing-text-font-descriptor-h.md#oh_drawing_destroyfontvariationinstance)接口释放。 |

### OH\_Drawing\_GetFontVariationAxisByIndex()

```c
OH_Drawing_FontVariationAxis* OH_Drawing_GetFontVariationAxisByIndex(OH_Drawing_Array* array, size_t index)
```

**描述**

在字体可变轴数组中通过索引获取对应的字体可变轴。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)\* array | 指向字体可变轴数组[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)的指针，通过[OH\_Drawing\_GetFontFullDescriptorAttributeArray](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontfulldescriptorattributearray)获取。 |
| size\_t index | 数组的索引，索引值从0开始。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontVariationAxis\*](capi-drawing-oh-drawing-fontvariationaxis.md) | 返回指向指定索引处字体可变轴对象[OH\_Drawing\_FontVariationAxis](capi-drawing-oh-drawing-fontvariationaxis.md)的指针。  如果索引超出范围或数组无效，则返回NULL。 |

### OH\_Drawing\_DestroyFontVariationAxis()

```c
void OH_Drawing_DestroyFontVariationAxis(OH_Drawing_Array* fontVariaAxisArray)
```

**描述**

释放字体可变轴数组占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)\* fontVariaAxisArray | 指向字体可变轴数组对象[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)的指针。 |

### OH\_Drawing\_GetFontVariationAxisAttributeDouble()

```c
OH_Drawing_ErrorCode OH_Drawing_GetFontVariationAxisAttributeDouble(OH_Drawing_FontVariationAxis* variationAxis, OH_Drawing_FontVariationAxisAttributeId id, double *value)
```

**描述**

获取double类型字体可变轴的属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontVariationAxis](capi-drawing-oh-drawing-fontvariationaxis.md)\* variationAxis | 指向字体可变轴对象[OH\_Drawing\_FontVariationAxis](capi-drawing-oh-drawing-fontvariationaxis.md)的指针。 |
| [OH\_Drawing\_FontVariationAxisAttributeId](capi-drawing-text-font-descriptor-h.md#oh_drawing_fontvariationaxisattributeid) id | 字体可变轴属性id。从[OH\_Drawing\_FontVariationAxisAttributeId](capi-drawing-text-font-descriptor-h.md#oh_drawing_fontvariationaxisattributeid)中可获取字体可变轴的属性。 |
| double \*value | 指向double类型属性的指针。作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示参数variationAxis或者value为空指针。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。 |

### OH\_Drawing\_GetFontVariationAxisAttributeInt()

```c
OH_Drawing_ErrorCode OH_Drawing_GetFontVariationAxisAttributeInt(OH_Drawing_FontVariationAxis* variationAxis, OH_Drawing_FontVariationAxisAttributeId id, int *value)
```

**描述**

获取int类型字体可变轴的属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontVariationAxis](capi-drawing-oh-drawing-fontvariationaxis.md)\* variationAxis | 指向字体可变轴对象[OH\_Drawing\_FontVariationAxis](capi-drawing-oh-drawing-fontvariationaxis.md)的指针。 |
| [OH\_Drawing\_FontVariationAxisAttributeId](capi-drawing-text-font-descriptor-h.md#oh_drawing_fontvariationaxisattributeid) id | 字体可变轴属性id。从[OH\_Drawing\_FontVariationAxisAttributeId](capi-drawing-text-font-descriptor-h.md#oh_drawing_fontvariationaxisattributeid)中可获取字体可变轴的属性。 |
| int \*value | 指向int类型属性的指针。作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示参数variationAxis或者value为空指针。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。 |

### OH\_Drawing\_GetFontVariationAxisAttributeStr()

```c
OH_Drawing_ErrorCode OH_Drawing_GetFontVariationAxisAttributeStr(OH_Drawing_FontVariationAxis* variationAxis, OH_Drawing_FontVariationAxisAttributeId id, OH_Drawing_String *str)
```

**描述**

获取[OH\_Drawing\_String](capi-drawing-oh-drawing-string.md)类型字体可变轴的属性。

**说明** 

如果不再需要OH\_Drawing\_String，调用方需要手动释放OH\_Drawing\_String结构体内部的strData成员。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontVariationAxis](capi-drawing-oh-drawing-fontvariationaxis.md)\* variationAxis | 指向字体可变轴对象[OH\_Drawing\_FontVariationAxis](capi-drawing-oh-drawing-fontvariationaxis.md)的指针。 |
| [OH\_Drawing\_FontVariationAxisAttributeId](capi-drawing-text-font-descriptor-h.md#oh_drawing_fontvariationaxisattributeid) id | 字体可变轴属性id。从[OH\_Drawing\_FontVariationAxisAttributeId](capi-drawing-text-font-descriptor-h.md#oh_drawing_fontvariationaxisattributeid)中可获取字体可变轴的属性。 |
| [OH\_Drawing\_String](capi-drawing-oh-drawing-string.md) \*str | 指向OH\_Drawing\_String类型属性的指针。作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示参数variationAxis或者str为空指针。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。 |

### OH\_Drawing\_GetFontVariationInstanceByIndex()

```c
OH_Drawing_FontVariationInstance* OH_Drawing_GetFontVariationInstanceByIndex(OH_Drawing_Array* array, size_t index)
```

**描述**

在字体可变实例数组中通过索引获取对应的字体可变实例。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)\* array | 指向字体可变实例数组[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)的指针。通过[OH\_Drawing\_GetFontFullDescriptorAttributeArray](capi-drawing-text-font-descriptor-h.md#oh_drawing_getfontfulldescriptorattributearray)获取。 |
| size\_t index | 数组的索引，索引值从0开始。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontVariationInstance\*](capi-drawing-oh-drawing-fontvariationinstance.md) | 返回指向指定索引处字体可变实例对象[OH\_Drawing\_FontVariationInstance](capi-drawing-oh-drawing-fontvariationinstance.md)的指针。  如果索引超出范围或数组无效，则返回NULL。 |

### OH\_Drawing\_DestroyFontVariationInstance()

```c
void OH_Drawing_DestroyFontVariationInstance(OH_Drawing_Array* fontVariaAxisInstance)
```

**描述**

释放字体可变实例数组占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)\* fontVariaAxisInstance | 指向字体可变实例数组对象[OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md)的指针。 |

### OH\_Drawing\_GetFontVariationInstanceAttributeStr()

```c
OH_Drawing_ErrorCode OH_Drawing_GetFontVariationInstanceAttributeStr(OH_Drawing_FontVariationInstance* variationInstance, OH_Drawing_FontVariationInstanceAttributeId id, OH_Drawing_String* str)
```

**描述**

获取[OH\_Drawing\_String](capi-drawing-oh-drawing-string.md)类型字体可变实例的属性。

**说明** 

如果不再需要OH\_Drawing\_String，调用方需要手动释放OH\_Drawing\_String结构体内部的strData成员。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontVariationInstance](capi-drawing-oh-drawing-fontvariationinstance.md)\* variationInstance | 指向字体可变实例对象[OH\_Drawing\_FontVariationInstance](capi-drawing-oh-drawing-fontvariationinstance.md)的指针。 |
| [OH\_Drawing\_FontVariationInstanceAttributeId](capi-drawing-text-font-descriptor-h.md#oh_drawing_fontvariationinstanceattributeid) id | 字体可变实例属性id。从[OH\_Drawing\_FontVariationInstanceAttributeId](capi-drawing-text-font-descriptor-h.md#oh_drawing_fontvariationinstanceattributeid)中可获取字体可变实例属性。 |
| [OH\_Drawing\_String](capi-drawing-oh-drawing-string.md)\* str | 指向OH\_Drawing\_String类型属性的指针。作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示参数variationInstance或者str为空指针。  返回OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH，表示传入属性id与调用函数不匹配。 |

### OH\_Drawing\_GetFontVariationInstanceCoordinate()

```c
OH_Drawing_FontVariationInstanceCoordinate* OH_Drawing_GetFontVariationInstanceCoordinate(OH_Drawing_FontVariationInstance* variationInstance, size_t* arrayLength)
```

**描述**

获取字体可变实例的可变字体属性对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontVariationInstance](capi-drawing-oh-drawing-fontvariationinstance.md)\* variationInstance | 指向字体可变实例的指针。 |
| size\_t\* arrayLength | 指向OH\_Drawing\_FontVariationInstanceCoordinate列表长度的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontVariationInstanceCoordinate\*](capi-drawing-oh-drawing-fontvariationinstancecoordinate.md) | 返回指向可变字体属性列表的指针，若variationInstance无效则返回NULL。 |

### OH\_Drawing\_GetFontFullDescriptorByFullName()

```c
const OH_Drawing_FontFullDescriptor* OH_Drawing_GetFontFullDescriptorByFullName(const OH_Drawing_String* fullName, OH_Drawing_SystemFontType fontType)
```

**描述**

根据字体名称和字体类型获取字体完整描述符对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_Drawing\_String](capi-drawing-oh-drawing-string.md)\* fullName | 指向字体名称对象[OH\_Drawing\_String](capi-drawing-oh-drawing-string.md)的指针。 |
| [OH\_Drawing\_SystemFontType](capi-drawing-text-font-descriptor-h.md#oh_drawing_systemfonttype) fontType | 系统字体类型对象[OH\_Drawing\_SystemFontType](capi-drawing-text-font-descriptor-h.md#oh_drawing_systemfonttype)的枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [const OH\_Drawing\_FontFullDescriptor\*](capi-drawing-oh-drawing-fontfulldescriptor.md) | 返回指向字体完整描述符对象[OH\_Drawing\_FontFullDescriptor](capi-drawing-oh-drawing-fontfulldescriptor.md)的指针。不再需要OH\_Drawing\_FontFullDescriptor时，请使用[OH\_Drawing\_DestroyFontFullDescriptor](capi-drawing-text-font-descriptor-h.md#oh_drawing_destroyfontfulldescriptor)接口释放该对象的指针。 |
