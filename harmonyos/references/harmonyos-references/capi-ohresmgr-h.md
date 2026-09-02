---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohresmgr-h
title: ohresmgr.h
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 头文件 > ohresmgr.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e0cb839779680de6b523f2ccede043d9b804c3e7410c3b2c969be20c73c73a34
---

## 概述

提供资源管理Native层获取资源的能力。

**引用文件：** <resourcemanager/ohresmgr.h>

**库：** libohresmgr.so

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**相关模块：** [resourcemanager](capi-resourcemanager.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaBase64(const NativeResourceManager \*mgr, uint32\_t resId, char \*\*resultValue, uint64\_t \*resultLen, uint32\_t density = 0)](capi-ohresmgr-h.md#oh_resourcemanager_getmediabase64) | 通过指定资源ID和屏幕密度，获取对应的media资源的Base64编码字符串。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaBase64Data(const NativeResourceManager \*mgr, uint32\_t resId, char \*\*resultValue, uint64\_t \*resultLen, uint32\_t density)](capi-ohresmgr-h.md#oh_resourcemanager_getmediabase64data) | 通过指定资源ID和屏幕密度，获取对应的media资源的Base64编码字符串。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaBase64ByName(const NativeResourceManager \*mgr, const char \*resName, char \*\*resultValue, uint64\_t \*resultLen, uint32\_t density = 0)](capi-ohresmgr-h.md#oh_resourcemanager_getmediabase64byname) | 通过指定资源名称和屏幕密度，获取对应的media资源的Base64编码字符串。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaBase64DataByName(const NativeResourceManager \*mgr, const char \*resName, char \*\*resultValue, uint64\_t \*resultLen, uint32\_t density)](capi-ohresmgr-h.md#oh_resourcemanager_getmediabase64databyname) | 通过指定资源名称和屏幕密度，获取对应的media资源的Base64编码字符串。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMedia(const NativeResourceManager \*mgr, uint32\_t resId, uint8\_t \*\*resultValue, uint64\_t \*resultLen, uint32\_t density = 0)](capi-ohresmgr-h.md#oh_resourcemanager_getmedia) | 通过指定资源ID和屏幕密度，获取对应的media资源的二进制数据。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaData(const NativeResourceManager \*mgr, uint32\_t resId, uint8\_t \*\*resultValue, uint64\_t \*resultLen, uint32\_t density)](capi-ohresmgr-h.md#oh_resourcemanager_getmediadata) | 通过指定资源ID和屏幕密度，获取对应的media资源的二进制数据。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaByName(const NativeResourceManager \*mgr, const char \*resName, uint8\_t \*\*resultValue, uint64\_t \*resultLen, uint32\_t density = 0)](capi-ohresmgr-h.md#oh_resourcemanager_getmediabyname) | 通过指定资源名称和屏幕密度，获取对应的media资源的二进制数据。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaDataByName(const NativeResourceManager \*mgr, const char \*resName, uint8\_t \*\*resultValue, uint64\_t \*resultLen, uint32\_t density)](capi-ohresmgr-h.md#oh_resourcemanager_getmediadatabyname) | 通过指定资源名称和屏幕密度，获取对应的media资源的二进制数据。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetDrawableDescriptor(const NativeResourceManager \*mgr, uint32\_t resId, ArkUI\_DrawableDescriptor \*\*drawableDescriptor, uint32\_t density = 0, uint32\_t type = 0)](capi-ohresmgr-h.md#oh_resourcemanager_getdrawabledescriptor) | 通过指定资源ID、屏幕密度、图标类型，获取图标资源对应的DrawableDescriptor对象。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetDrawableDescriptorData(const NativeResourceManager \*mgr, uint32\_t resId, ArkUI\_DrawableDescriptor \*\*drawableDescriptor, uint32\_t density, uint32\_t type)](capi-ohresmgr-h.md#oh_resourcemanager_getdrawabledescriptordata) | 通过指定资源ID、屏幕密度、图标类型，获取图标资源对应的DrawableDescriptor对象。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetDrawableDescriptorByName(const NativeResourceManager \*mgr, const char \*resName, ArkUI\_DrawableDescriptor \*\*drawableDescriptor, uint32\_t density = 0, uint32\_t type = 0)](capi-ohresmgr-h.md#oh_resourcemanager_getdrawabledescriptorbyname) | 通过指定资源名称、屏幕密度、图标类型，获取图标资源对应的DrawableDescriptor对象。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetDrawableDescriptorDataByName(const NativeResourceManager \*mgr, const char \*resName, ArkUI\_DrawableDescriptor \*\*drawableDescriptor, uint32\_t density, uint32\_t type)](capi-ohresmgr-h.md#oh_resourcemanager_getdrawabledescriptordatabyname) | 通过指定资源名称和屏幕密度，获取对应的图标资源的DrawableDescriptor对象。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetSymbol(const NativeResourceManager \*mgr, uint32\_t resId, uint32\_t \*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getsymbol) | 获取指定资源ID对应的Symbol图标的Unicode编码。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetSymbolByName(const NativeResourceManager \*mgr, const char \*resName, uint32\_t \*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getsymbolbyname) | 获取指定资源名称对应的Symbol图标的Unicode编码。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetLocales(const NativeResourceManager \*mgr, char \*\*\*resultValue, uint32\_t \*resultLen, bool includeSystem = false)](capi-ohresmgr-h.md#oh_resourcemanager_getlocales) | 获取应用支持的语言列表。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetLocalesData(const NativeResourceManager \*mgr, char \*\*\*resultValue, uint32\_t \*resultLen, bool includeSystem)](capi-ohresmgr-h.md#oh_resourcemanager_getlocalesdata) | 获取应用支持的语言列表。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetConfiguration(const NativeResourceManager \*mgr, ResourceManager\_Configuration \*configuration)](capi-ohresmgr-h.md#oh_resourcemanager_getconfiguration) | 获取设备的屏幕方向、语言区域、设备类型、屏幕密度、颜色模式等配置信息。(API20废弃) |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetResourceConfiguration(const NativeResourceManager \*mgr, ResourceManager\_Configuration \*configuration)](capi-ohresmgr-h.md#oh_resourcemanager_getresourceconfiguration) | 获取设备的屏幕方向、语言区域、设备类型、屏幕密度、颜色模式等配置信息。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_ReleaseConfiguration(ResourceManager\_Configuration \*configuration)](capi-ohresmgr-h.md#oh_resourcemanager_releaseconfiguration) | 释放[OH\_ResourceManager\_GetConfiguration](capi-ohresmgr-h.md#oh_resourcemanager_getconfiguration)或[OH\_ResourceManager\_GetResourceConfiguration](capi-ohresmgr-h.md#oh_resourcemanager_getresourceconfiguration)函数申请的内存。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetString(const NativeResourceManager \*mgr, uint32\_t resId, char \*\*resultValue, ...)](capi-ohresmgr-h.md#oh_resourcemanager_getstring) | 获取指定资源ID对应的普通字符串或格式化字符串。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetStringByName(const NativeResourceManager \*mgr, const char \*resName, char \*\*resultValue, ...)](capi-ohresmgr-h.md#oh_resourcemanager_getstringbyname) | 获取指定资源名称对应的普通字符串或格式化字符串。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetStringArray(const NativeResourceManager \*mgr, uint32\_t resId, char \*\*\*resultValue, uint32\_t \*resultLen)](capi-ohresmgr-h.md#oh_resourcemanager_getstringarray) | 获取指定资源ID对应的字符串数组。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetStringArrayByName(const NativeResourceManager \*mgr, const char \*resName, char \*\*\*resultValue, uint32\_t \*resultLen)](capi-ohresmgr-h.md#oh_resourcemanager_getstringarraybyname) | 获取指定资源名称对应的字符串数组。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_ReleaseStringArray(char \*\*\*resValue, uint32\_t len)](capi-ohresmgr-h.md#oh_resourcemanager_releasestringarray) | 释放字符串数组内存。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetPluralString(const NativeResourceManager \*mgr, uint32\_t resId, uint32\_t num, char \*\*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getpluralstring) | 获取指定资源ID对应的复数字符串。  中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。  在英语、德语等语言中，单复数类型包括基数词（如1、2、3）和序数词（如1st、2nd、3rd），本函数仅支持在基数词类型下使用。(API16废弃) |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetPluralStringByName(const NativeResourceManager \*mgr, const char \*resName, uint32\_t num, char \*\*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getpluralstringbyname) | 获取指定资源名称对应的复数字符串。  中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。  在英语、德语等语言中，单复数类型包括基数词（如1、2、3）和序数词（如1st、2nd、3rd），本函数仅支持在基数词类型下使用。(API16废弃) |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetIntPluralString(const NativeResourceManager \*mgr, uint32\_t resId, uint32\_t num, char \*\*resultValue, ...)](capi-ohresmgr-h.md#oh_resourcemanager_getintpluralstring) | 通过指定资源ID、整数数量值和可变参数，获取对应的复数字符串并进行格式化。  中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。  在英语、德语等语言中，单复数类型包括基数词（如1、2、3）和序数词（如1st、2nd、3rd），本函数仅支持在基数词类型下使用。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetIntPluralStringByName(const NativeResourceManager \*mgr, const char \*resName, uint32\_t num, char \*\*resultValue, ...)](capi-ohresmgr-h.md#oh_resourcemanager_getintpluralstringbyname) | 通过指定资源名称、整数数量值和可变参数，获取对应的复数字符串并进行格式化。  中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。  在英语、德语等语言中，单复数类型包括基数词（如1、2、3）和序数词（如1st、2nd、3rd），本函数仅支持在基数词类型下使用。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetDoublePluralString(const NativeResourceManager \*mgr, uint32\_t resId, double num, char \*\*resultValue, ...)](capi-ohresmgr-h.md#oh_resourcemanager_getdoublepluralstring) | 通过指定资源ID、浮点数数量值和可变参数，获取对应的复数字符串并进行格式化。  中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。  在英语、德语等语言中，单复数类型包括基数词（如1、2、3）和序数词（如1st、2nd、3rd），本函数仅支持在基数词类型下使用。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetDoublePluralStringByName(const NativeResourceManager \*mgr, const char \*resName, double num, char \*\*resultValue, ...)](capi-ohresmgr-h.md#oh_resourcemanager_getdoublepluralstringbyname) | 通过指定资源名称、浮点数数量值和可变参数，获取对应的复数字符串并进行格式化。  中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。  在英语、德语等语言中，单复数类型包括基数词（如1、2、3）和序数词（如1st、2nd、3rd），本函数仅支持在基数词类型下使用。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetColor(const NativeResourceManager \*mgr, uint32\_t resId, uint32\_t \*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getcolor) | 获取指定资源ID对应的颜色资源值。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetColorByName(const NativeResourceManager \*mgr, const char \*resName, uint32\_t \*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getcolorbyname) | 获取指定资源名称对应的颜色资源值。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetInt(const NativeResourceManager \*mgr, uint32\_t resId, int \*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getint) | 获取指定资源ID对应的整数资源值。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetIntByName(const NativeResourceManager \*mgr, const char \*resName, int \*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getintbyname) | 获取指定资源名称对应的整数资源值。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetFloat(const NativeResourceManager \*mgr, uint32\_t resId, float \*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getfloat) | 获取指定资源ID对应的浮点数资源值。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetFloatByName(const NativeResourceManager \*mgr, const char \*resName, float \*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getfloatbyname) | 获取指定资源名称对应的浮点数资源值。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetBool(const NativeResourceManager \*mgr, uint32\_t resId, bool \*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getbool) | 获取指定资源ID对应的布尔资源值。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetBoolByName(const NativeResourceManager \*mgr, const char \*resName, bool \*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getboolbyname) | 获取指定资源名称对应的布尔资源值。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_AddResource(const NativeResourceManager \*mgr, const char \*path)](capi-ohresmgr-h.md#oh_resourcemanager_addresource) | 在应用程序运行时，动态加载overlay资源，实现主题切换或资源覆盖。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_RemoveResource(const NativeResourceManager \*mgr, const char \*path)](capi-ohresmgr-h.md#oh_resourcemanager_removeresource) | 在应用程序运行时，移除指定的overlay资源，还原被覆盖前的资源。 |

## 函数说明

### OH\_ResourceManager\_GetMediaBase64()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetMediaBase64(const NativeResourceManager *mgr, uint32_t resId, char **resultValue, uint64_t *resultLen, uint32_t density = 0)
```

**描述**

通过指定资源ID和屏幕密度，获取对应的media资源的Base64编码字符串。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| uint32\_t resId | 输入参数。资源ID。 |
| char \*\*resultValue | 输出参数。返回Base64编码字符串指针，由malloc()分配内存，使用完后须通过free()释放。 |
| uint64\_t \*resultLen | 输出参数。返回Base64字符串长度，单位为Byte。 |
| density | 输入参数，可选。屏幕密度，取值范围请参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)。默认值为0，表示使用当前系统屏幕密度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_ID\_NOT\_FOUND，表示无效的资源ID。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID，表示根据资源ID未找到匹配的资源。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_GetMediaBase64Data()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetMediaBase64Data(const NativeResourceManager *mgr, uint32_t resId, char **resultValue, uint64_t *resultLen, uint32_t density)
```

**描述**

通过指定资源ID和屏幕密度，获取对应的media资源的Base64编码字符串。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| uint32\_t resId | 输入参数。资源ID。 |
| char \*\*resultValue | 输出参数。返回Base64编码字符串指针，由malloc()分配内存，使用完后须通过free()释放。 |
| uint64\_t \*resultLen | 输出参数。返回Base64字符串长度，单位为Byte。 |
| uint32\_t density | 输入参数。屏幕密度，取值范围请参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)。值为0表示使用当前系统屏幕密度。若不需要特定密度，请将此参数设置为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_ID\_NOT\_FOUND，表示无效的资源ID。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID，表示根据资源ID未找到匹配的资源。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_GetMediaBase64ByName()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetMediaBase64ByName(const NativeResourceManager *mgr, const char *resName, char **resultValue, uint64_t *resultLen, uint32_t density = 0)
```

**描述**

通过指定资源名称和屏幕密度，获取对应的media资源的Base64编码字符串。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| const char \*resName | 输入参数。资源名称。 |
| char \*\*resultValue | 输出参数。返回Base64编码字符串指针，由malloc()分配内存，使用完后须通过free()释放。 |
| uint64\_t \*resultLen | 输出参数。返回Base64字符串长度，单位为Byte。 |
| density | 输入参数，可选。屏幕密度，取值范围请参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)。默认值为0，表示使用当前系统屏幕密度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_NAME\_NOT\_FOUND，表示无效的资源名称。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME，表示根据资源名称未找到匹配的资源。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_GetMediaBase64DataByName()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetMediaBase64DataByName(const NativeResourceManager *mgr, const char *resName, char **resultValue, uint64_t *resultLen, uint32_t density)
```

**描述**

通过指定资源名称和屏幕密度，获取对应的media资源的Base64编码字符串。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| const char \*resName | 输入参数。资源名称。 |
| char \*\*resultValue | 输出参数。返回Base64编码字符串指针，由malloc()分配内存，使用完后须通过free()释放。 |
| uint64\_t \*resultLen | 输出参数。返回Base64字符串长度，单位为Byte。 |
| uint32\_t density | 输入参数。屏幕密度，取值范围请参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)。值为0表示使用当前系统屏幕密度。若不需要特定密度，请将此参数设置为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_NAME\_NOT\_FOUND，表示无效的资源名称。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME，表示根据资源名称未找到匹配的资源。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_GetMedia()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetMedia(const NativeResourceManager *mgr, uint32_t resId, uint8_t **resultValue, uint64_t *resultLen, uint32_t density = 0)
```

**描述**

通过指定资源ID和屏幕密度，获取对应的media资源的二进制数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| uint32\_t resId | 输入参数。资源ID。 |
| uint8\_t \*\*resultValue | 输出参数。返回媒体数据指针，由malloc()分配内存，使用完后须通过free()释放。 |
| uint64\_t \*resultLen | 输出参数。返回数据长度，单位为Byte。 |
| density | 输入参数，可选。屏幕密度，取值范围请参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)。默认值为0，表示使用当前系统屏幕密度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_ID\_NOT\_FOUND，表示无效的资源ID。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID，表示根据资源ID未找到匹配的资源。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_GetMediaData()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetMediaData(const NativeResourceManager *mgr, uint32_t resId, uint8_t **resultValue, uint64_t *resultLen, uint32_t density)
```

**描述**

通过指定资源ID和屏幕密度，获取对应的media资源的二进制数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| uint32\_t resId | 输入参数。资源ID。 |
| uint8\_t \*\*resultValue | 输出参数。返回媒体数据指针，由malloc()分配内存，使用完后须通过free()释放。 |
| uint64\_t \*resultLen | 输出参数。返回数据长度，单位为Byte。 |
| uint32\_t density | 输入参数。屏幕密度，取值范围请参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)。值为0表示使用当前系统屏幕密度。若不需要特定密度，请将此参数设置为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_ID\_NOT\_FOUND，表示无效的资源ID。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID，表示根据资源ID未找到匹配的资源。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_GetMediaByName()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetMediaByName(const NativeResourceManager *mgr, const char *resName, uint8_t **resultValue, uint64_t *resultLen, uint32_t density = 0)
```

**描述**

通过指定资源名称和屏幕密度，获取对应的media资源的二进制数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| const char \*resName | 输入参数。资源名称。 |
| uint8\_t \*\*resultValue | 输出参数。返回媒体数据指针，由malloc()分配内存，使用完后须通过free()释放。 |
| uint64\_t \*resultLen | 输出参数。返回数据长度，单位为Byte。 |
| density | 输入参数，可选。屏幕密度，取值范围请参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)。默认值为0，表示使用当前系统屏幕密度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_NAME\_NOT\_FOUND，表示无效的资源名称。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME，表示根据资源名称未找到匹配的资源。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_GetMediaDataByName()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetMediaDataByName(const NativeResourceManager *mgr, const char *resName, uint8_t **resultValue, uint64_t *resultLen, uint32_t density)
```

**描述**

通过指定资源名称和屏幕密度，获取对应的media资源的二进制数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| const char \*resName | 输入参数。资源名称。 |
| uint8\_t \*\*resultValue | 输出参数。返回媒体数据指针，由malloc()分配内存，使用完后须通过free()释放。 |
| uint64\_t \*resultLen | 输出参数。返回数据长度，单位为Byte。 |
| uint32\_t density | 输入参数。屏幕密度，取值范围请参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)。值为0表示使用当前系统屏幕密度。若不需要特定密度，请将此参数设置为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_NAME\_NOT\_FOUND，表示无效的资源名称。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME，表示根据资源名称未找到匹配的资源。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_GetDrawableDescriptor()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetDrawableDescriptor(const NativeResourceManager *mgr, uint32_t resId, ArkUI_DrawableDescriptor **drawableDescriptor, uint32_t density = 0, uint32_t type = 0)
```

**描述**

通过指定资源ID、屏幕密度、图标类型，获取图标资源对应的DrawableDescriptor对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| uint32\_t resId | 输入参数。资源ID。 |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md) \*\*drawableDescriptor | 输出参数。返回指向DrawableDescriptor对象的指针。 |
| density | 输入参数，可选。屏幕密度，取值范围请参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)。默认值为0，表示使用当前系统屏幕密度。 |
| type | 输入参数，可选。图标类型，默认值为0。  0：表示应用自身图标。  1：表示应用主题图标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_ID\_NOT\_FOUND，表示无效的资源ID。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID，表示根据资源ID未找到匹配的资源。 |

### OH\_ResourceManager\_GetDrawableDescriptorData()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetDrawableDescriptorData(const NativeResourceManager *mgr, uint32_t resId, ArkUI_DrawableDescriptor **drawableDescriptor, uint32_t density, uint32_t type)
```

**描述**

通过指定资源ID、屏幕密度、图标类型，获取图标资源对应的DrawableDescriptor对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| uint32\_t resId | 输入参数。资源ID。 |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md) \*\*drawableDescriptor | 输出参数。返回指向DrawableDescriptor对象的指针。 |
| uint32\_t density | 输入参数。屏幕密度，取值范围请参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)。值为0表示使用当前系统屏幕密度。若不需要特定密度，请将此参数设置为0。 |
| uint32\_t type | 输入参数。图标类型，若不需要特定图标类型，请将该参数设置为0。  0：表示应用自身图标。  1：表示应用主题图标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_ID\_NOT\_FOUND，表示无效的资源ID。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID，表示根据资源ID未找到匹配的资源。 |

### OH\_ResourceManager\_GetDrawableDescriptorByName()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetDrawableDescriptorByName(const NativeResourceManager *mgr, const char *resName, ArkUI_DrawableDescriptor **drawableDescriptor, uint32_t density = 0, uint32_t type = 0)
```

**描述**

通过指定资源名称、屏幕密度、图标类型，获取图标资源对应的DrawableDescriptor对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| const char \*resName | 输入参数。资源名称。 |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md) \*\*drawableDescriptor | 输出参数。返回指向DrawableDescriptor对象的指针。 |
| density | 输入参数，可选。屏幕密度，取值范围请参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)。默认值为0，表示使用当前系统屏幕密度。 |
| type | 输入参数，可选。图标类型，默认值为0。  0：表示应用自身图标。  1：表示应用主题图标。  2：表示应用动态图标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_NAME\_NOT\_FOUND，表示无效的资源名称。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME，表示根据资源名称未找到匹配的资源。 |

### OH\_ResourceManager\_GetDrawableDescriptorDataByName()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetDrawableDescriptorDataByName(const NativeResourceManager *mgr, const char *resName, ArkUI_DrawableDescriptor **drawableDescriptor, uint32_t density, uint32_t type)
```

**描述**

通过指定资源名称和屏幕密度，获取对应的图标资源的DrawableDescriptor对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| const char \*resName | 输入参数。资源名称。 |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md) \*\*drawableDescriptor | 输出参数。返回指向DrawableDescriptor对象的指针。 |
| uint32\_t density | 输入参数，屏幕密度，取值范围请参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)。值为0表示使用当前系统屏幕密度。若不需要特定密度，请将此参数设置为0。 |
| uint32\_t type | 输入参数。图标类型，若不需要特定图标类型，请将该参数设置为0。  0：表示应用自身图标。  1：表示主题图标。  2：表示动态图标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_NAME\_NOT\_FOUND，表示无效的资源名称。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME，表示根据资源名称未找到匹配的资源。 |

### OH\_ResourceManager\_GetSymbol()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetSymbol(const NativeResourceManager *mgr, uint32_t resId, uint32_t *resultValue)
```

**描述**

获取指定资源ID对应的Symbol图标的Unicode编码。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| uint32\_t resId | 输入参数。资源ID。 |
| uint32\_t \*resultValue | 输出参数。返回Symbol图标的Unicode编码。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_ID\_NOT\_FOUND，表示无效的资源ID。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID，表示根据资源ID未找到匹配的资源。  返回ERROR\_CODE\_RES\_REF\_TOO\_MUCH，表示资源存在循环引用。 |

### OH\_ResourceManager\_GetSymbolByName()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetSymbolByName(const NativeResourceManager *mgr, const char *resName, uint32_t *resultValue)
```

**描述**

获取指定资源名称对应的Symbol图标的Unicode编码。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| const char \*resName | 输入参数。资源名称。 |
| uint32\_t \*resultValue | 输出参数。返回Symbol图标的Unicode编码。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_NAME\_NOT\_FOUND，表示无效的资源名称。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME，表示根据资源名称未找到匹配的资源。  返回ERROR\_CODE\_RES\_REF\_TOO\_MUCH，表示资源存在循环引用。 |

### OH\_ResourceManager\_GetLocales()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetLocales(const NativeResourceManager *mgr, char ***resultValue, uint32_t *resultLen, bool includeSystem = false)
```

**描述**

获取应用支持的语言列表。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| char \*\*\*resultValue | 输出参数。返回指向语言列表数组的指针，由此函数分配内存，使用完后须通过[OH\_ResourceManager\_ReleaseStringArray](capi-ohresmgr-h.md#oh_resourcemanager_releasestringarray)释放。 |
| uint32\_t \*resultLen | 输出参数。返回语言列表长度。 |
| includeSystem | 输入参数，可选。表示是否包含系统资源，true表示包含系统资源，false表示不包含系统资源。默认值为false。  当使用系统资源管理对象获取语言列表时，始终返回系统资源语言列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_GetLocalesData()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetLocalesData(const NativeResourceManager *mgr, char ***resultValue, uint32_t *resultLen, bool includeSystem)
```

**描述**

获取应用支持的语言列表。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| char \*\*\*resultValue | 输出参数。返回指向语言列表数组的指针，由此函数分配内存，使用完后须通过[OH\_ResourceManager\_ReleaseStringArray](capi-ohresmgr-h.md#oh_resourcemanager_releasestringarray)释放。 |
| uint32\_t \*resultLen | 输出参数。返回语言列表长度。 |
| bool includeSystem | 输入参数。表示是否包含系统资源，true表示包含系统资源，false表示不包含系统资源。  当使用系统资源管理对象获取语言列表时，始终返回系统资源语言列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_GetConfiguration()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetConfiguration(const NativeResourceManager *mgr, ResourceManager_Configuration *configuration)
```

**描述**

获取设备的屏幕方向、语言区域、设备类型、屏幕密度、颜色模式等配置信息。

**起始版本：** 12

**废弃版本：** 20

**替代接口：** [OH\_ResourceManager\_GetResourceConfiguration](capi-ohresmgr-h.md#oh_resourcemanager_getresourceconfiguration)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| [ResourceManager\_Configuration](capi-resourcemanager-resourcemanager-configuration.md) \*configuration | 输出参数。返回设备配置信息，其中screenDensity为设备屏幕密度（dpi）除以160取整后的值。  configuration中的locale字符串由此函数分配内存，使用完后需通过[OH\_ResourceManager\_ReleaseConfiguration](capi-ohresmgr-h.md#oh_resourcemanager_releaseconfiguration)释放locale。若configuration指针由malloc()分配内存，使用完后须通过free()释放。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_SYSTEM\_RES\_MANAGER\_GET\_FAILED，表示访问系统资源失败。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_GetResourceConfiguration()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetResourceConfiguration(const NativeResourceManager *mgr, ResourceManager_Configuration *configuration)
```

**描述**

获取设备的屏幕方向、语言区域、设备类型、屏幕密度、颜色模式等配置信息。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| [ResourceManager\_Configuration](capi-resourcemanager-resourcemanager-configuration.md) \*configuration | 输出参数。返回设备配置信息，其中screenDensity的值为设备屏幕密度（dpi）。  configuration中的locale字符串由此函数分配内存，使用完后需通过[OH\_ResourceManager\_ReleaseConfiguration](capi-ohresmgr-h.md#oh_resourcemanager_releaseconfiguration)释放locale。若configuration指针由malloc()分配内存，使用完后须通过free()释放。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_SYSTEM\_RES\_MANAGER\_GET\_FAILED，表示访问系统资源失败。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_ReleaseConfiguration()

```c
ResourceManager_ErrorCode OH_ResourceManager_ReleaseConfiguration(ResourceManager_Configuration *configuration)
```

**描述**

释放[OH\_ResourceManager\_GetConfiguration](capi-ohresmgr-h.md#oh_resourcemanager_getconfiguration)或[OH\_ResourceManager\_GetResourceConfiguration](capi-ohresmgr-h.md#oh_resourcemanager_getresourceconfiguration)函数申请的内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ResourceManager\_Configuration](capi-resourcemanager-resourcemanager-configuration.md) \*configuration | 输入参数。指向需要释放内存的[ResourceManager\_Configuration](capi-resourcemanager-resourcemanager-configuration.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。 |

### OH\_ResourceManager\_GetString()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetString(const NativeResourceManager *mgr, uint32_t resId, char **resultValue, ...)
```

**描述**

获取指定资源ID对应的普通字符串或格式化字符串。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| uint32\_t resId | 输入参数。资源ID。 |
| char \*\*resultValue | 输出参数。返回字符串指针，由malloc()分配内存，使用完后须通过free()释放。 |
| ... | 输入参数，可选。表示可变参数列表，用于格式化字符串，支持const char\*、int、float三种类型。  获取普通字符串时，无需填写；获取格式化字符串时，必填，须按字符串中的占位符顺序依次传入对应类型的可变参数，参数数量、类型与字符串的占位符保持一致，如字符串包含%d、%s、%f三个占位符，调用方式为OH\_ResourceManager\_GetString(mgr, resId, resultValue, 10, "format", 10.10)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_ID\_NOT\_FOUND，表示无效的资源ID。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID，表示根据资源ID未找到匹配的资源。  返回ERROR\_CODE\_RES\_REF\_TOO\_MUCH，表示资源存在循环引用。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_GetStringByName()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetStringByName(const NativeResourceManager *mgr, const char *resName, char **resultValue, ...)
```

**描述**

获取指定资源名称对应的普通字符串或格式化字符串。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| const char \*resName | 输入参数。资源名称。 |
| char \*\*resultValue | 输出参数。返回字符串指针，由malloc()分配内存，使用完后须通过free()释放。 |
| ... | 输入参数，可选。表示可变参数列表，用于格式化字符串，支持const char\*、int、float三种类型。  获取普通字符串时，无需填写；获取格式化字符串时，必填，须按字符串中的占位符顺序依次传入对应类型的可变参数，参数数量、类型与字符串的占位符保持一致，如字符串包含%d、%s、%f三个占位符，调用方式为OH\_ResourceManager\_GetStringByName(mgr, resName, resultValue, 10, "format", 10.10)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_NAME\_NOT\_FOUND，表示无效的资源名称。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME，表示根据资源名称未找到匹配的资源。  返回ERROR\_CODE\_RES\_REF\_TOO\_MUCH，表示资源存在循环引用。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_GetStringArray()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetStringArray(const NativeResourceManager *mgr, uint32_t resId, char ***resultValue, uint32_t *resultLen)
```

**描述**

获取指定资源ID对应的字符串数组。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| uint32\_t resId | 输入参数。资源ID。 |
| char \*\*\*resultValue | 输出参数。返回字符串数组指针。由此函数分配内存，使用完后须通过[OH\_ResourceManager\_ReleaseStringArray](capi-ohresmgr-h.md#oh_resourcemanager_releasestringarray)释放。 |
| uint32\_t \*resultLen | 输出参数。返回字符串数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_ID\_NOT\_FOUND，表示无效的资源ID。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID，表示根据资源ID未找到匹配的资源。  返回ERROR\_CODE\_RES\_REF\_TOO\_MUCH，表示资源存在循环引用。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_GetStringArrayByName()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetStringArrayByName(const NativeResourceManager *mgr, const char *resName, char ***resultValue, uint32_t *resultLen)
```

**描述**

获取指定资源名称对应的字符串数组。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| const char \*resName | 输入参数。资源名称。 |
| char \*\*\*resultValue | 输出参数。返回字符串数组指针。由此函数分配内存，使用完后须通过[OH\_ResourceManager\_ReleaseStringArray](capi-ohresmgr-h.md#oh_resourcemanager_releasestringarray)释放。 |
| uint32\_t \*resultLen | 输出参数。返回字符串数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_NAME\_NOT\_FOUND，表示无效的资源名称。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME，表示根据资源名称未找到匹配的资源。  返回ERROR\_CODE\_RES\_REF\_TOO\_MUCH，表示资源存在循环引用。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_ReleaseStringArray()

```c
ResourceManager_ErrorCode OH_ResourceManager_ReleaseStringArray(char ***resValue, uint32_t len)
```

**描述**

释放字符串数组内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*\*\*resValue | 输入参数。待释放的字符串数组指针。 |
| uint32\_t len | 输入参数。字符串数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。 |

### OH\_ResourceManager\_GetPluralString()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetPluralString(const NativeResourceManager *mgr, uint32_t resId, uint32_t num, char **resultValue)
```

**描述**

获取指定资源ID对应的复数字符串。

中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

在英语、德语等语言中，单复数类型包括基数词（如1、2、3）和序数词（如1st、2nd、3rd），本函数仅支持在基数词类型下使用。

**起始版本：** 12

**废弃版本：** 16

**替代接口：** [OH\_ResourceManager\_GetIntPluralString](capi-ohresmgr-h.md#oh_resourcemanager_getintpluralstring)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| uint32\_t resId | 输入参数。资源ID。 |
| uint32\_t num | 输入参数。数量值，用于根据当前语言的复数规则获取对应的复数字符串。 |
| char \*\*resultValue | 输出参数。返回字符串指针。由malloc()分配内存，使用完后须通过free()释放。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_ID\_NOT\_FOUND，表示无效的资源ID。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID，表示根据资源ID未找到匹配的资源。  返回ERROR\_CODE\_RES\_REF\_TOO\_MUCH，表示资源存在循环引用。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_GetPluralStringByName()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetPluralStringByName(const NativeResourceManager *mgr, const char *resName, uint32_t num, char **resultValue)
```

**描述**

获取指定资源名称对应的复数字符串。

中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

在英语、德语等语言中，单复数类型包括基数词（如1、2、3）和序数词（如1st、2nd、3rd），本函数仅支持在基数词类型下使用。

**起始版本：** 12

**废弃版本：** 16

**替代接口：** [OH\_ResourceManager\_GetIntPluralStringByName](capi-ohresmgr-h.md#oh_resourcemanager_getintpluralstringbyname)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| const char \*resName | 输入参数。资源名称。 |
| uint32\_t num | 输入参数。数量值，用于根据当前语言的复数规则获取对应的复数字符串。 |
| char \*\*resultValue | 输出参数。返回字符串指针。由malloc()分配内存，使用完后须通过free()释放。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_NAME\_NOT\_FOUND，表示无效的资源名称。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME，表示根据资源名称未找到匹配的资源。  返回ERROR\_CODE\_RES\_REF\_TOO\_MUCH，表示资源存在循环引用。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_GetIntPluralString()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetIntPluralString(const NativeResourceManager *mgr, uint32_t resId, uint32_t num, char **resultValue, ...)
```

**描述**

通过指定资源ID、整数数量值和可变参数，获取对应的复数字符串并进行格式化。

中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

在英语、德语等语言中，单复数类型包括基数词（如1、2、3）和序数词（如1st、2nd、3rd），本函数仅支持在基数词类型下使用。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| uint32\_t resId | 输入参数。资源ID。 |
| uint32\_t num | 输入参数。数量值（整数），用于根据当前语言的复数规则获取对应的复数字符串。 |
| char \*\*resultValue | 输出参数。返回字符串指针。由malloc()分配内存，使用完后须通过free()释放。 |
| ... | 输入参数，可选。表示可变参数列表，用于格式化字符串，支持const char\*、int、float三种类型。  获取格式化字符串时，须按字符串中的占位符顺序依次传入对应类型的可变参数，参数数量、类型与字符串的占位符保持一致，如字符串包含%d、%s、%f三个占位符，调用方式为OH\_ResourceManager\_GetIntPluralString(mgr, resId, 10, resultValue, 10, "format", 10.10)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_ID\_NOT\_FOUND，表示无效的资源ID。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID，表示根据资源ID未找到匹配的资源。  返回ERROR\_CODE\_RES\_REF\_TOO\_MUCH，表示资源存在循环引用。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_GetIntPluralStringByName()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetIntPluralStringByName(const NativeResourceManager *mgr, const char *resName, uint32_t num, char **resultValue, ...)
```

**描述**

通过指定资源名称、整数数量值和可变参数，获取对应的复数字符串并进行格式化。

中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

在英语、德语等语言中，单复数类型包括基数词（如1、2、3）和序数词（如1st、2nd、3rd），本函数仅支持在基数词类型下使用。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| const char \*resName | 输入参数。资源名称。 |
| uint32\_t num | 输入参数。数量值（整数），用于根据当前语言的复数规则获取对应的复数字符串。 |
| char \*\*resultValue | 输出参数。返回字符串指针。由malloc()分配内存，使用完后须通过free()释放。 |
| ... | 输入参数，可选。表示可变参数列表，用于格式化字符串，支持const char\*、int、float三种类型。  获取格式化字符串时，须按字符串中的占位符顺序依次传入对应类型的可变参数，参数数量、类型与字符串的占位符保持一致，如字符串包含%d、%s、%f三个占位符，调用方式为OH\_ResourceManager\_GetIntPluralStringByName(mgr, resName, 10, resultValue, 10, "format", 10.10)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_NAME\_NOT\_FOUND，表示无效的资源名称。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME，表示根据资源名称未找到匹配的资源。  返回ERROR\_CODE\_RES\_REF\_TOO\_MUCH，表示资源存在循环引用。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_GetDoublePluralString()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetDoublePluralString(const NativeResourceManager *mgr, uint32_t resId, double num, char **resultValue, ...)
```

**描述**

通过指定资源ID、浮点数数量值和可变参数，获取对应的复数字符串并进行格式化。

中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

在英语、德语等语言中，单复数类型包括基数词（如1、2、3）和序数词（如1st、2nd、3rd），本函数仅支持在基数词类型下使用。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| uint32\_t resId | 输入参数。资源ID。 |
| double num | 输入参数。数量值（浮点数），用于根据当前语言的复数规则获取对应的复数字符串。 |
| char \*\*resultValue | 输出参数。返回字符串指针。由malloc()分配内存，使用完后须通过free()释放。 |
| ... | 输入参数，可选。表示可变参数列表，用于格式化字符串，支持const char\*、int、float三种类型。  获取格式化字符串时，须按字符串中的占位符顺序依次传入对应类型的可变参数，参数数量、类型与字符串的占位符保持一致，如字符串包含%d、%s、%f三个占位符，调用方式为OH\_ResourceManager\_GetDoublePluralString(mgr, resId, 1.1, resultValue, 10, "format", 10.10)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_ID\_NOT\_FOUND，表示无效的资源ID。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID，表示根据资源ID未找到匹配的资源。  返回ERROR\_CODE\_RES\_REF\_TOO\_MUCH，表示资源存在循环引用。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_GetDoublePluralStringByName()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetDoublePluralStringByName(const NativeResourceManager *mgr, const char *resName, double num, char **resultValue, ...)
```

**描述**

通过指定资源名称、浮点数数量值和可变参数，获取对应的复数字符串并进行格式化。

中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

在英语、德语等语言中，单复数类型包括基数词（如1、2、3）和序数词（如1st、2nd、3rd），本函数仅支持在基数词类型下使用。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| const char \*resName | 输入参数。资源名称。 |
| double num | 输入参数。数量值（浮点数），用于根据当前语言的复数规则获取对应的复数字符串。 |
| char \*\*resultValue | 输出参数。返回字符串指针。由malloc()分配内存，使用完后须通过free()释放。 |
| ... | 输入参数，可选。表示可变参数列表，用于格式化字符串，支持const char\*、int、float三种类型。  获取格式化字符串时，须按字符串中的占位符顺序依次传入对应类型的可变参数，参数数量、类型与字符串的占位符保持一致，如字符串包含%d、%s、%f三个占位符，调用方式为OH\_ResourceManager\_GetDoublePluralStringByName(mgr, resName, 1.1, resultValue, 10, "format", 10.10)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_NAME\_NOT\_FOUND，表示无效的资源名称。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME，表示根据资源名称未找到匹配的资源。  返回ERROR\_CODE\_RES\_REF\_TOO\_MUCH，表示资源存在循环引用。  返回ERROR\_CODE\_OUT\_OF\_MEMORY，表示内存溢出。 |

### OH\_ResourceManager\_GetColor()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetColor(const NativeResourceManager *mgr, uint32_t resId, uint32_t *resultValue)
```

**描述**

获取指定资源ID对应的颜色资源值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| uint32\_t resId | 输入参数。资源ID。 |
| uint32\_t \*resultValue | 输出参数。返回颜色资源值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_ID\_NOT\_FOUND，表示无效的资源ID。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID，表示根据资源ID未找到匹配的资源。  返回ERROR\_CODE\_RES\_REF\_TOO\_MUCH，表示资源存在循环引用。 |

### OH\_ResourceManager\_GetColorByName()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetColorByName(const NativeResourceManager *mgr, const char *resName, uint32_t *resultValue)
```

**描述**

获取指定资源名称对应的颜色资源值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| const char \*resName | 输入参数。资源名称。 |
| uint32\_t \*resultValue | 输出参数。返回颜色资源值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_NAME\_NOT\_FOUND，表示无效的资源名称。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME，表示根据资源名称未找到匹配的资源。  返回ERROR\_CODE\_RES\_REF\_TOO\_MUCH，表示资源存在循环引用。 |

### OH\_ResourceManager\_GetInt()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetInt(const NativeResourceManager *mgr, uint32_t resId, int *resultValue)
```

**描述**

获取指定资源ID对应的整数资源值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| uint32\_t resId | 输入参数。资源ID。 |
| int \*resultValue | 输出参数。返回整数资源值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_ID\_NOT\_FOUND，表示无效的资源ID。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID，表示根据资源ID未找到匹配的资源。  返回ERROR\_CODE\_RES\_REF\_TOO\_MUCH，表示资源存在循环引用。 |

### OH\_ResourceManager\_GetIntByName()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetIntByName(const NativeResourceManager *mgr, const char *resName, int *resultValue)
```

**描述**

获取指定资源名称对应的整数资源值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| const char \*resName | 输入参数。资源名称。 |
| int \*resultValue | 输出参数。返回整数资源值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_NAME\_NOT\_FOUND，表示无效的资源名称。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME，表示根据资源名称未找到匹配的资源。  返回ERROR\_CODE\_RES\_REF\_TOO\_MUCH，表示资源存在循环引用。 |

### OH\_ResourceManager\_GetFloat()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetFloat(const NativeResourceManager *mgr, uint32_t resId, float *resultValue)
```

**描述**

获取指定资源ID对应的浮点数资源值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| uint32\_t resId | 输入参数。资源ID。 |
| float \*resultValue | 输出参数。返回浮点数资源值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_ID\_NOT\_FOUND，表示无效的资源ID。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID，表示根据资源ID未找到匹配的资源。  返回ERROR\_CODE\_RES\_REF\_TOO\_MUCH，表示资源存在循环引用。 |

### OH\_ResourceManager\_GetFloatByName()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetFloatByName(const NativeResourceManager *mgr, const char *resName, float *resultValue)
```

**描述**

获取指定资源名称对应的浮点数资源值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| const char \*resName | 输入参数。资源名称。 |
| float \*resultValue | 输出参数。返回浮点数资源值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_NAME\_NOT\_FOUND，表示无效的资源名称。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME，表示根据资源名称未找到匹配的资源。  返回ERROR\_CODE\_RES\_REF\_TOO\_MUCH，表示资源存在循环引用。 |

### OH\_ResourceManager\_GetBool()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetBool(const NativeResourceManager *mgr, uint32_t resId, bool *resultValue)
```

**描述**

获取指定资源ID对应的布尔资源值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| uint32\_t resId | 输入参数。资源ID。 |
| bool \*resultValue | 输出参数。返回布尔资源值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_ID\_NOT\_FOUND，表示无效的资源ID。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID，表示根据资源ID未找到匹配的资源。  返回ERROR\_CODE\_RES\_REF\_TOO\_MUCH，表示资源存在循环引用。 |

### OH\_ResourceManager\_GetBoolByName()

```c
ResourceManager_ErrorCode OH_ResourceManager_GetBoolByName(const NativeResourceManager *mgr, const char *resName, bool *resultValue)
```

**描述**

获取指定资源名称对应的布尔资源值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| const char \*resName | 输入参数。资源名称。 |
| bool \*resultValue | 输出参数。返回布尔资源值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_RES\_NAME\_NOT\_FOUND，表示无效的资源名称。  返回ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME，表示根据资源名称未找到匹配的资源。  返回ERROR\_CODE\_RES\_REF\_TOO\_MUCH，表示资源存在循环引用。 |

### OH\_ResourceManager\_AddResource()

```c
ResourceManager_ErrorCode OH_ResourceManager_AddResource(const NativeResourceManager *mgr, const char *path)
```

**描述**

在应用程序运行时，动态加载overlay资源，实现主题切换或资源覆盖。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| const char \*path | 输入参数。待加载的HSP或HAP资源包的绝对路径。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_OVERLAY\_RES\_PATH\_INVALID，表示无效的overlay路径。 |

### OH\_ResourceManager\_RemoveResource()

```c
ResourceManager_ErrorCode OH_ResourceManager_RemoveResource(const NativeResourceManager *mgr, const char *path)
```

**描述**

在应用程序运行时，移除指定的overlay资源，还原被覆盖前的资源。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 输入参数。指向NativeResourceManager对象的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)函数获取。 |
| const char \*path | 输入参数。待移除的HSP或HAP资源包的绝对路径。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | 返回错误码。  返回SUCCESS，表示成功。  返回ERROR\_CODE\_INVALID\_INPUT\_PARAMETER，表示输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  返回ERROR\_CODE\_OVERLAY\_RES\_PATH\_INVALID，表示无效的overlay路径。 |
