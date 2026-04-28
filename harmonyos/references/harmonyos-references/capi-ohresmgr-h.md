---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohresmgr-h
title: ohresmgr.h
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 头文件 > ohresmgr.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:32+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:147fd5e43fd6cff9254c6dbb80787a9fb4a513d4ce1bed0df927dd6c2d397b86
---

## 概述

PhonePC/2in1TabletTVWearable

提供资源管理native侧获取资源的能力。

**引用文件：** <resourcemanager/ohresmgr.h>

**库：** libohresmgr.so

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**相关模块：** [resourcemanager](capi-resourcemanager.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaBase64(const NativeResourceManager \*mgr, uint32\_t resId, char \*\*resultValue, uint64\_t \*resultLen, uint32\_t density = 0)](capi-ohresmgr-h.md#oh_resourcemanager_getmediabase64) | 通过指定资源ID，获取屏幕密度对应的media资源的Base64码。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaBase64Data(const NativeResourceManager \*mgr, uint32\_t resId, char \*\*resultValue, uint64\_t \*resultLen, uint32\_t density)](capi-ohresmgr-h.md#oh_resourcemanager_getmediabase64data) | 通过指定资源ID，获取屏幕密度对应的media资源的Base64码。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaBase64ByName(const NativeResourceManager \*mgr, const char \*resName, char \*\*resultValue, uint64\_t \*resultLen, uint32\_t density = 0)](capi-ohresmgr-h.md#oh_resourcemanager_getmediabase64byname) | 通过指定资源名称，获取屏幕密度对应的media资源的Base64码。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaBase64DataByName(const NativeResourceManager \*mgr, const char \*resName, char \*\*resultValue, uint64\_t \*resultLen, uint32\_t density)](capi-ohresmgr-h.md#oh_resourcemanager_getmediabase64databyname) | 通过指定资源名称，获取屏幕密度对应的media资源的Base64码。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMedia(const NativeResourceManager \*mgr, uint32\_t resId, uint8\_t \*\*resultValue, uint64\_t \*resultLen, uint32\_t density = 0)](capi-ohresmgr-h.md#oh_resourcemanager_getmedia) | 通过指定资源ID，获取屏幕密度对应的media资源的内容。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaData(const NativeResourceManager \*mgr, uint32\_t resId, uint8\_t \*\*resultValue, uint64\_t \*resultLen, uint32\_t density)](capi-ohresmgr-h.md#oh_resourcemanager_getmediadata) | 通过指定资源ID，获取屏幕密度对应的media资源的内容。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaByName(const NativeResourceManager \*mgr, const char \*resName, uint8\_t \*\*resultValue, uint64\_t \*resultLen, uint32\_t density = 0)](capi-ohresmgr-h.md#oh_resourcemanager_getmediabyname) | 通过指定资源名称，获取屏幕密度对应的media资源的内容。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaDataByName(const NativeResourceManager \*mgr, const char \*resName, uint8\_t \*\*resultValue, uint64\_t \*resultLen, uint32\_t density)](capi-ohresmgr-h.md#oh_resourcemanager_getmediadatabyname) | 通过指定资源名称，获取屏幕密度对应的media资源的内容。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetDrawableDescriptor(const NativeResourceManager \*mgr, uint32\_t resId, ArkUI\_DrawableDescriptor \*\*drawableDescriptor, uint32\_t density = 0, uint32\_t type = 0)](capi-ohresmgr-h.md#oh_resourcemanager_getdrawabledescriptor) | 通过指定资源Id，获取屏幕密度对应的图标资源的DrawableDescriptor。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetDrawableDescriptorData(const NativeResourceManager \*mgr, uint32\_t resId, ArkUI\_DrawableDescriptor \*\*drawableDescriptor, uint32\_t density, uint32\_t type)](capi-ohresmgr-h.md#oh_resourcemanager_getdrawabledescriptordata) | 通过指定资源Id，获取屏幕密度对应的图标资源的DrawableDescriptor。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetDrawableDescriptorByName(const NativeResourceManager \*mgr, const char \*resName, ArkUI\_DrawableDescriptor \*\*drawableDescriptor, uint32\_t density = 0, uint32\_t type = 0)](capi-ohresmgr-h.md#oh_resourcemanager_getdrawabledescriptorbyname) | 通过指定资源名称，获取屏幕密度对应的图标资源的DrawableDescriptor。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetDrawableDescriptorDataByName(const NativeResourceManager \*mgr, const char \*resName, ArkUI\_DrawableDescriptor \*\*drawableDescriptor, uint32\_t density, uint32\_t type)](capi-ohresmgr-h.md#oh_resourcemanager_getdrawabledescriptordatabyname) | 通过指定资源名称，获取屏幕密度对应的图标资源的DrawableDescriptor。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetSymbol(const NativeResourceManager \*mgr, uint32\_t resId, uint32\_t \*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getsymbol) | 通过指定资源ID，获取对应的symbol资源。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetSymbolByName(const NativeResourceManager \*mgr, const char \*resName, uint32\_t \*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getsymbolbyname) | 通过指定资源名称，获取对应的symbol资源。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetLocales(const NativeResourceManager \*mgr, char \*\*\*resultValue, uint32\_t \*resultLen, bool includeSystem = false)](capi-ohresmgr-h.md#oh_resourcemanager_getlocales) | 获取语言列表。使用此接口后，需要调用OH\_ResourceManager\_ReleaseStringArray()方法来释放locales的内存。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetLocalesData(const NativeResourceManager \*mgr, char \*\*\*resultValue, uint32\_t \*resultLen, bool includeSystem)](capi-ohresmgr-h.md#oh_resourcemanager_getlocalesdata) | 获取语言列表。使用此接口后，需要调用OH\_ResourceManager\_ReleaseStringArray()方法来释放locales的内存。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetConfiguration(const NativeResourceManager \*mgr, ResourceManager\_Configuration \*configuration)](capi-ohresmgr-h.md#oh_resourcemanager_getconfiguration) | 获取设备配置。使用此接口后，需要调用[OH\_ResourceManager\_ReleaseConfiguration](capi-ohresmgr-h.md#oh_resourcemanager_releaseconfiguration)方法来释放内存。如果使用malloc创建ResourceManager\_Configuration对象，还需要调用free()方法来释放它。(API20废弃) |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetResourceConfiguration(const NativeResourceManager \*mgr, ResourceManager\_Configuration \*configuration)](capi-ohresmgr-h.md#oh_resourcemanager_getresourceconfiguration) | 获取设备配置。使用此接口后，需要调用[OH\_ResourceManager\_ReleaseConfiguration](capi-ohresmgr-h.md#oh_resourcemanager_releaseconfiguration)方法来释放内存。如果使用malloc创建ResourceManager\_Configuration对象，还需要调用free()方法来释放它。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_ReleaseConfiguration(ResourceManager\_Configuration \*configuration)](capi-ohresmgr-h.md#oh_resourcemanager_releaseconfiguration) | 释放[OH\_ResourceManager\_GetConfiguration](capi-ohresmgr-h.md#oh_resourcemanager_getconfiguration)和[OH\_ResourceManager\_GetResourceConfiguration](capi-ohresmgr-h.md#oh_resourcemanager_getresourceconfiguration)方法申请的内存。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetString(const NativeResourceManager \*mgr, uint32\_t resId, char \*\*resultValue, ...)](capi-ohresmgr-h.md#oh_resourcemanager_getstring) | 通过指定资源ID，获取对应的string资源。获取普通string资源使用OH\_ResourceManager\_GetString(mgr, resId, resultValue)接口。获取带有%d、%s、%f占位符的格式化资源使用OH\_ResourceManager\_GetString(mgr, resId, resultValue, 10, "format", 10.10)接口。使用此接口后，需要调用free()方法来释放字符串的内存。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetStringByName(const NativeResourceManager \*mgr, const char \*resName, char \*\*resultValue, ...)](capi-ohresmgr-h.md#oh_resourcemanager_getstringbyname) | 通过指定资源名称，获取对应的string资源。获取普通string资源使用OH\_ResourceManager\_GetString(mgr, resName, resultValue)接口。获取带有%d、%s、%f占位符的格式化资源使用OH\_ResourceManager\_GetString(mgr, resName, resultValue, 10, "format", 10.10)接口。使用此接口后，需要调用free()方法来释放字符串的内存。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetStringArray(const NativeResourceManager \*mgr, uint32\_t resId, char \*\*\*resultValue, uint32\_t \*resultLen)](capi-ohresmgr-h.md#oh_resourcemanager_getstringarray) | 通过指定资源ID，获取字符串数组。使用此接口后，需要调用OH\_ResourceManager\_ReleaseStringArray()接口来释放字符串数组内存。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetStringArrayByName(const NativeResourceManager \*mgr, const char \*resName, char \*\*\*resultValue, uint32\_t \*resultLen)](capi-ohresmgr-h.md#oh_resourcemanager_getstringarraybyname) | 通过指定资源名称，获取字符串数组。使用此接口后，需要调用OH\_ResourceManager\_ReleaseStringArray()接口来释放字符串数组内存。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_ReleaseStringArray(char \*\*\*resValue, uint32\_t len)](capi-ohresmgr-h.md#oh_resourcemanager_releasestringarray) | 释放字符串数组内存。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetPluralString(const NativeResourceManager \*mgr, uint32\_t resId, uint32\_t num, char \*\*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getpluralstring) | 通过指定资源ID，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。(API18废弃) |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetPluralStringByName(const NativeResourceManager \*mgr, const char \*resName, uint32\_t num, char \*\*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getpluralstringbyname) | 通过指定资源名称，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。(API18废弃) |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetIntPluralString(const NativeResourceManager \*mgr, uint32\_t resId, uint32\_t num, char \*\*resultValue, ...)](capi-ohresmgr-h.md#oh_resourcemanager_getintpluralstring) | 通过指定资源ID，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetDoublePluralString(const NativeResourceManager \*mgr, uint32\_t resId, double num, char \*\*resultValue, ...)](capi-ohresmgr-h.md#oh_resourcemanager_getdoublepluralstring) | 通过指定资源ID，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetIntPluralStringByName(const NativeResourceManager \*mgr, const char \*resName, uint32\_t num, char \*\*resultValue, ...)](capi-ohresmgr-h.md#oh_resourcemanager_getintpluralstringbyname) | 通过指定资源名称，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetDoublePluralStringByName(const NativeResourceManager \*mgr, const char \*resName, double num, char \*\*resultValue, ...)](capi-ohresmgr-h.md#oh_resourcemanager_getdoublepluralstringbyname) | 通过指定资源名称，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetColor(const NativeResourceManager \*mgr, uint32\_t resId, uint32\_t \*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getcolor) | 通过指定资源ID，获取对应的颜色值。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetColorByName(const NativeResourceManager \*mgr, const char \*resName, uint32\_t \*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getcolorbyname) | 通过指定资源ID，获取对应的颜色值。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetInt(const NativeResourceManager \*mgr, uint32\_t resId, int \*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getint) | 通过指定资源ID，获取对应的int值。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetIntByName(const NativeResourceManager \*mgr, const char \*resName, int \*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getintbyname) | 通过指定资源名称，获取对应的int值。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetFloat(const NativeResourceManager \*mgr, uint32\_t resId, float \*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getfloat) | 通过指定资源ID，获取对应的float值。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetFloatByName(const NativeResourceManager \*mgr, const char \*resName, float \*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getfloatbyname) | 通过指定资源名称，获取对应的float值。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetBool(const NativeResourceManager \*mgr, uint32\_t resId, bool \*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getbool) | 通过指定资源ID，获取对应的bool值。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetBoolByName(const NativeResourceManager \*mgr, const char \*resName, bool \*resultValue)](capi-ohresmgr-h.md#oh_resourcemanager_getboolbyname) | 通过指定资源名称，获取对应的bool值。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_AddResource(const NativeResourceManager \*mgr, const char \*path)](capi-ohresmgr-h.md#oh_resourcemanager_addresource) | 在应用程序运行时添加overlay资源。 |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_RemoveResource(const NativeResourceManager \*mgr, const char \*path)](capi-ohresmgr-h.md#oh_resourcemanager_removeresource) | 在应用程序运行时删除overlay资源。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_ResourceManager\_GetMediaBase64()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetMediaBase64(const NativeResourceManager *mgr, uint32_t resId, char **resultValue, uint64_t *resultLen, uint32_t density = 0)
```

**描述**

通过指定资源ID，获取屏幕密度对应的media资源的Base64码。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| uint32\_t resId | 资源ID。 |
| uint32\_t density | 可选参数，取值范围参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)，默认值为0，表示使用当前系统dpi的密度。 |
| char \*\*resultValue | 写入resultValue的结果。 |
| uint64\_t \*resultLen | 写入resultLen的media长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001001 - 无效的资源ID。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_GetMediaBase64Data()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetMediaBase64Data(const NativeResourceManager *mgr, uint32_t resId, char **resultValue, uint64_t *resultLen, uint32_t density)
```

**描述**

通过指定资源ID，获取屏幕密度对应的media资源的Base64码。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| uint32\_t resId | 资源ID。 |
| char \*\*resultValue | 写入resultValue的结果。 |
| uint64\_t \*resultLen | 写入resultLen的media长度。 |
| uint32\_t density | 可选参数，取值范围参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)，值为0表示使用当前系统dpi的密度。如果不需要此属性，请将此参数设置为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001001 - 无效的资源ID。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_GetMediaBase64ByName()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetMediaBase64ByName(const NativeResourceManager *mgr, const char *resName, char **resultValue, uint64_t *resultLen, uint32_t density = 0)
```

**描述**

通过指定资源名称，获取屏幕密度对应的media资源的Base64码。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*resName | 资源名称。 |
| char \*\*resultValue | 写入resultValue的结果。 |
| uint64\_t \*resultLen | 写入resultLen的media长度。 |
| uint32\_t density | 可选参数，取值范围参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)，默认值为0，表示使用当前系统dpi的密度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001003 - 无效的资源名称。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_GetMediaBase64DataByName()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetMediaBase64DataByName(const NativeResourceManager *mgr, const char *resName, char **resultValue, uint64_t *resultLen, uint32_t density)
```

**描述**

通过指定资源名称，获取屏幕密度对应的media资源的Base64码。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*resName | 资源名称。 |
| char \*\*resultValue | 写入resultValue的结果。 |
| uint64\_t \*resultLen | 写入resultLen的media长度。 |
| uint32\_t density | 可选参数，取值范围参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)，值为0表示使用当前系统dpi的密度。如果不需要此属性，请将此参数设置为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001003 - 无效的资源名称。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_GetMedia()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetMedia(const NativeResourceManager *mgr, uint32_t resId, uint8_t **resultValue, uint64_t *resultLen, uint32_t density = 0)
```

**描述**

通过指定资源ID，获取屏幕密度对应的media资源的内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| uint32\_t resId | 资源ID。 |
| uint32\_t density | 可选参数，取值范围参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)，默认值为0，表示使用当前系统dpi的密度。 |
| uint8\_t \*\*resultValue | 写入resultValue的结果。 |
| uint64\_t \*resultLen | 写入resultLen的media长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001001 - 无效的资源ID。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_GetMediaData()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetMediaData(const NativeResourceManager *mgr, uint32_t resId, uint8_t **resultValue, uint64_t *resultLen, uint32_t density)
```

**描述**

通过指定资源ID，获取屏幕密度对应的media资源的内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| uint32\_t resId | 资源ID。 |
| uint8\_t \*\*resultValue | 写入resultValue的结果。 |
| uint64\_t \*resultLen | 写入resultLen的media长度。 |
| uint32\_t density | 可选参数，取值范围参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)，值为0表示使用当前系统dpi的密度。如果不需要此属性，请将此参数设置为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001001 - 无效的资源ID。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_GetMediaByName()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetMediaByName(const NativeResourceManager *mgr, const char *resName, uint8_t **resultValue, uint64_t *resultLen, uint32_t density = 0)
```

**描述**

通过指定资源名称，获取屏幕密度对应的media资源的内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*resName | 资源名称。 |
| uint32\_t density | 可选参数，取值范围参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)，默认值为0，表示使用当前系统dpi的密度。 |
| uint8\_t \*\*resultValue | 写入resultValue的结果。 |
| uint64\_t \*resultLen | 写入resultLen的media长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001003 - 无效的资源名称。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_GetMediaDataByName()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetMediaDataByName(const NativeResourceManager *mgr, const char *resName, uint8_t **resultValue, uint64_t *resultLen, uint32_t density)
```

**描述**

通过指定资源名称，获取屏幕密度对应的media资源的内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*resName | 资源名称。 |
| uint8\_t \*\*resultValue | 写入resultValue的结果。 |
| uint64\_t \*resultLen | 写入resultLen的media长度。 |
| uint32\_t density | 可选参数，取值范围参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)，值为0表示使用当前系统dpi的密度。如果不需要此属性，请将此参数设置为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001003 - 无效的资源名称。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_GetDrawableDescriptor()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetDrawableDescriptor(const NativeResourceManager *mgr, uint32_t resId, ArkUI_DrawableDescriptor **drawableDescriptor, uint32_t density = 0, uint32_t type = 0)
```

**描述**

通过指定资源Id，获取屏幕密度对应的图标资源的DrawableDescriptor。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| uint32\_t | 资源ID。 |
| uint32\_t density | 可选参数，取值范围参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)，默认值为0，表示使用当前系统dpi的密度。 |
| uint32\_t type | 可选参数，表示图标类型，0表示自身图标，1表示主题图标。 |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md) \*\*drawableDescriptor | 写入drawableDescriptor的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001001 - 无效的资源ID。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。 |

### OH\_ResourceManager\_GetDrawableDescriptorData()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetDrawableDescriptorData(const NativeResourceManager *mgr, uint32_t resId, ArkUI_DrawableDescriptor **drawableDescriptor, uint32_t density, uint32_t type)
```

**描述**

通过指定资源Id，获取屏幕密度对应的图标资源的DrawableDescriptor。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| uint32\_t resId | 资源ID。 |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md) \*\*drawableDescriptor | 写入drawableDescriptor的结果。 |
| uint32\_t density | 可选参数，取值范围参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)，值为0表示使用当前系统dpi的密度。如果不需要此属性，请将此参数设置为0。 |
| uint32\_t type | 可选参数，表示图标类型，0表示自身图标，1表示主题图标。如果该属性不是必需的，请将该参数设为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001001 - 无效的资源ID。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。 |

### OH\_ResourceManager\_GetDrawableDescriptorByName()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetDrawableDescriptorByName(const NativeResourceManager *mgr, const char *resName, ArkUI_DrawableDescriptor **drawableDescriptor, uint32_t density = 0, uint32_t type = 0)
```

**描述**

通过指定资源名称，获取屏幕密度对应的图标资源的DrawableDescriptor。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*resName | 资源名称。 |
| uint32\_t density | 可选参数，取值范围参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)，默认值为0，表示使用当前系统dpi的密度。 |
| uint32\_t type | 可选参数，表示图标类型，0表示自身图标，1表示主题图标，2表示动态图标。 |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md) \*\*drawableDescriptor | 写入drawableDescriptor的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001003 - 无效的资源名称。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。 |

### OH\_ResourceManager\_GetDrawableDescriptorDataByName()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetDrawableDescriptorDataByName(const NativeResourceManager *mgr, const char *resName, ArkUI_DrawableDescriptor **drawableDescriptor, uint32_t density, uint32_t type)
```

**描述**

通过指定资源名称，获取屏幕密度对应的图标资源的DrawableDescriptor。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*resName | 资源名称。 |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md) \*\*drawableDescriptor | 写入drawableDescriptor的结果。 |
| uint32\_t density | 可选参数，取值范围参考[ScreenDensity](capi-resmgr-common-h.md#screendensity)，值为0表示使用当前系统dpi的密度。如果不需要此属性，请将此参数设置为0。 |
| uint32\_t type | 可选参数，表示图标类型，0表示自身图标，1表示主题图标。如果该属性不是必需的，请将该参数设为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001003 - 无效的资源名称。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。 |

### OH\_ResourceManager\_GetSymbol()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetSymbol(const NativeResourceManager *mgr, uint32_t resId, uint32_t *resultValue)
```

**描述**

通过指定资源ID，获取对应的symbol资源。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| uint32\_t resId | 资源ID。 |
| uint32\_t \*resultValue | 写入resultValue的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001001 - 无效的资源ID。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。  [ERROR\_CODE\_RES\_REF\_TOO\_MUCH](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001006 - 资源被循环引用。 |

### OH\_ResourceManager\_GetSymbolByName()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetSymbolByName(const NativeResourceManager *mgr, const char *resName, uint32_t *resultValue)
```

**描述**

通过指定资源名称，获取对应的symbol资源。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*resName | 资源名称。 |
| uint32\_t \*resultValue | 写入resultValue的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001003 - 无效的资源名称。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。  [ERROR\_CODE\_RES\_REF\_TOO\_MUCH](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001006 - 资源被循环引用。 |

### OH\_ResourceManager\_GetLocales()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetLocales(const NativeResourceManager *mgr, char ***resultValue, uint32_t *resultLen, bool includeSystem = false)
```

**描述**

获取语言列表。使用此接口后，需要调用OH\_ResourceManager\_ReleaseStringArray()方法来释放locales的内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| char \*\*\*resultValue | 写入resultValue的结果。 |
| uint32\_t \*resultLen | 写入resultLen的locales长度。 |
| bool includeSystem | 是否包含系统资源，默认值为false，当只有系统资源查询locales列表时它不起作用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_GetLocalesData()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetLocalesData(const NativeResourceManager *mgr, char ***resultValue, uint32_t *resultLen, bool includeSystem)
```

**描述**

获取语言列表。使用此接口后，需要调用OH\_ResourceManager\_ReleaseStringArray()方法来释放locales的内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| char \*\*\*resultValue | 写入resultValue的结果。 |
| uint32\_t \*resultLen | 写入resultLen的locales长度。 |
| bool includeSystem | 是否包含系统资源，如果不需要此属性，请将此参数设置为 false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_GetConfiguration()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetConfiguration(const NativeResourceManager *mgr, ResourceManager_Configuration *configuration)
```

**描述**

获取设备配置。使用此接口后，需要调用[OH\_ResourceManager\_ReleaseConfiguration](capi-ohresmgr-h.md#oh_resourcemanager_releaseconfiguration)方法来释放内存。如果使用malloc创建ResourceManager\_Configuration对象，还需要调用free()方法来释放它。

**起始版本：** 12

**废弃版本：** 20

**替代接口：** [OH\_ResourceManager\_GetResourceConfiguration](capi-ohresmgr-h.md#oh_resourcemanager_getresourceconfiguration)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| [ResourceManager\_Configuration](capi-resourcemanager-resourcemanager-configuration.md) \*configuration | 写入获取的设备配置。其中configuration.screenDensity的返回值为设备DPI除以160取整后的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_SYSTEM\_RES\_MANAGER\_GET\_FAILED](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001009 - 无法访问系统资源。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_GetResourceConfiguration()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetResourceConfiguration(const NativeResourceManager *mgr, ResourceManager_Configuration *configuration)
```

**描述**

获取设备配置。使用此接口后，需要调用[OH\_ResourceManager\_ReleaseConfiguration](capi-ohresmgr-h.md#oh_resourcemanager_releaseconfiguration)方法来释放内存。如果使用malloc创建ResourceManager\_Configuration对象，还需要调用free()方法来释放它。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| [ResourceManager\_Configuration](capi-resourcemanager-resourcemanager-configuration.md) \*configuration | 写入获取的设备配置。其中configuration.screenDensity的返回值为设备DPI。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_SYSTEM\_RES\_MANAGER\_GET\_FAILED](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001009 - 无法访问系统资源。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_ReleaseConfiguration()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_ReleaseConfiguration(ResourceManager_Configuration *configuration)
```

**描述**

释放[OH\_ResourceManager\_GetConfiguration](capi-ohresmgr-h.md#oh_resourcemanager_getconfiguration)和[OH\_ResourceManager\_GetResourceConfiguration](capi-ohresmgr-h.md#oh_resourcemanager_getresourceconfiguration)方法申请的内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ResourceManager\_Configuration](capi-resourcemanager-resourcemanager-configuration.md) \*configuration | 需要释放内存的configuration对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。 |

### OH\_ResourceManager\_GetString()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetString(const NativeResourceManager *mgr, uint32_t resId, char **resultValue, ...)
```

**描述**

通过指定资源ID，获取对应的string资源。获取普通string资源使用OH\_ResourceManager\_GetString(mgr, resId, resultValue)接口。获取带有%d、%s、%f占位符的格式化资源使用OH\_ResourceManager\_GetString(mgr, resId, resultValue, 10, "format", 10.10)接口。使用此接口后，需要调用free()方法来释放字符串的内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| uint32\_t resId | 资源ID。 |
| char \*\*resultValue | 写入resultValue的结果。 |
| ... | 格式化字符串资源参数，可变参数，支持const char\*、int、float类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001001 - 无效的资源ID。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。  [ERROR\_CODE\_RES\_REF\_TOO\_MUCH](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001006 - 资源被循环引用。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_GetStringByName()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetStringByName(const NativeResourceManager *mgr, const char *resName, char **resultValue, ...)
```

**描述**

通过指定资源名称，获取对应的string资源。获取普通string资源使用OH\_ResourceManager\_GetString(mgr, resName, resultValue)接口。获取带有%d、%s、%f占位符的格式化资源使用OH\_ResourceManager\_GetString(mgr, resName, resultValue, 10, "format", 10.10)接口。使用此接口后，需要调用free()方法来释放字符串的内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*resName | 资源名称。 |
| char \*\*resultValue | 写入resultValue的结果。 |
| ... | 格式化字符串资源参数，可变参数，支持const char\*、int、float类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001003 - 无效的资源名称。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。  [ERROR\_CODE\_RES\_REF\_TOO\_MUCH](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001006 - 资源被循环引用。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_GetStringArray()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetStringArray(const NativeResourceManager *mgr, uint32_t resId, char ***resultValue, uint32_t *resultLen)
```

**描述**

通过指定资源ID，获取字符串数组。使用此接口后，需要调用OH\_ResourceManager\_ReleaseStringArray()接口来释放字符串数组内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| uint32\_t resId | 资源ID。 |
| char \*\*\*resultValue | 写入resultValue的结果。 |
| uint32\_t \*resultLen | 写入resultLen的StringArray长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001001 - 无效的资源ID。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。  [ERROR\_CODE\_RES\_REF\_TOO\_MUCH](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001006 - 资源被循环引用。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_GetStringArrayByName()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetStringArrayByName(const NativeResourceManager *mgr, const char *resName, char ***resultValue, uint32_t *resultLen)
```

**描述**

通过指定资源名称，获取字符串数组。使用此接口后，需要调用OH\_ResourceManager\_ReleaseStringArray()接口来释放字符串数组内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*resName | 资源名称。 |
| char \*\*\*resultValue | 写入resultValue的结果。 |
| uint32\_t \*resultLen | 写入resultLen的StringArray长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001003 - 无效的资源名称。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。  [ERROR\_CODE\_RES\_REF\_TOO\_MUCH](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001006 - 资源被循环引用。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_ReleaseStringArray()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_ReleaseStringArray(char ***resValue, uint32_t len)
```

**描述**

释放字符串数组内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*\*\*resValue | 需要释放的字符串数组。 |
| uint32\_t len | 字符串数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。 |

### OH\_ResourceManager\_GetPluralString()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetPluralString(const NativeResourceManager *mgr, uint32_t resId, uint32_t num, char **resultValue)
```

**描述**

通过指定资源ID，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。

**起始版本：** 12

**废弃版本：** 18

**替代接口：** [OH\_ResourceManager\_GetIntPluralString](capi-ohresmgr-h.md#oh_resourcemanager_getintpluralstring)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| uint32\_t resId | 资源ID。 |
| uint32\_t num | 数量值。 |
| char \*\*resultValue | 写入resultValue的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001001 - 无效的资源ID。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。  [ERROR\_CODE\_RES\_REF\_TOO\_MUCH](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001006 - 资源被循环引用。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_GetPluralStringByName()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetPluralStringByName(const NativeResourceManager *mgr, const char *resName, uint32_t num, char **resultValue)
```

**描述**

通过指定资源名称，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。

**起始版本：** 12

**废弃版本：** 18

**替代接口：** [OH\_ResourceManager\_GetIntPluralStringByName](capi-ohresmgr-h.md#oh_resourcemanager_getintpluralstringbyname)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*resName | 资源名称。 |
| uint32\_t num | 数量值。 |
| char \*\*resultValue | 写入resultValue的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001003 - 无效的资源名称。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。  [ERROR\_CODE\_RES\_REF\_TOO\_MUCH](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001006 - 资源被循环引用。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_GetIntPluralString()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetIntPluralString(const NativeResourceManager *mgr, uint32_t resId, uint32_t num, char **resultValue, ...)
```

**描述**

通过指定资源ID，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| uint32\_t resId | 资源ID。 |
| uint32\_t num | 数量值（整数）。根据当前语言的复数规则获取该数量值对应的字符串数字。 |
| char \*\*resultValue | 写入resultValue的结果。 |
| ... | 格式化字符串资源参数，可变参数，支持const char\*、int、float类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001001 - 无效的资源ID。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。  [ERROR\_CODE\_RES\_REF\_TOO\_MUCH](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001006 - 资源被循环引用。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_GetDoublePluralString()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetDoublePluralString(const NativeResourceManager *mgr, uint32_t resId, double num, char **resultValue, ...)
```

**描述**

通过指定资源ID，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| uint32\_t resId | 资源ID。 |
| double num | 数量值（浮点数）。根据当前语言的复数规则获取该数量值对应的字符串数字。 |
| char \*\*resultValue | 写入resultValue的结果。 |
| ... | 格式化字符串资源参数，可变参数，支持const char\*、int、float类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001001 - 无效的资源ID。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。  [ERROR\_CODE\_RES\_REF\_TOO\_MUCH](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001006 - 资源被循环引用。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_GetIntPluralStringByName()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetIntPluralStringByName(const NativeResourceManager *mgr, const char *resName, uint32_t num, char **resultValue, ...)
```

**描述**

通过指定资源名称，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*resName | 资源名称。 |
| uint32\_t num | 数量值（整数）。根据当前语言的复数规则获取该数量值对应的字符串数字。 |
| char \*\*resultValue | 写入resultValue的结果。 |
| ... | 格式化字符串资源参数，可变参数，支持const char\*、int、float类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001003 - 无效的资源名称。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。  [ERROR\_CODE\_RES\_REF\_TOO\_MUCH](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001006 - 资源被循环引用。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_GetDoublePluralStringByName()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetDoublePluralStringByName(const NativeResourceManager *mgr, const char *resName, double num, char **resultValue, ...)
```

**描述**

通过指定资源名称，获取对应的单复数字符串。使用此接口后，需要调用free()方法来释放字符串的内存。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*resName | 资源名称。 |
| double num | 数量值（浮点数）。根据当前语言的复数规则获取该数量值对应的字符串数字。 |
| char \*\*resultValue | 写入resultValue的结果。 |
| ... | 格式化字符串资源参数，可变参数，支持const char\*、int、float类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001003 - 无效的资源名称。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。  [ERROR\_CODE\_RES\_REF\_TOO\_MUCH](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001006 - 资源被循环引用。  [ERROR\_CODE\_OUT\_OF\_MEMORY](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001100 - 内存溢出。 |

### OH\_ResourceManager\_GetColor()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetColor(const NativeResourceManager *mgr, uint32_t resId, uint32_t *resultValue)
```

**描述**

通过指定资源ID，获取对应的颜色值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| uint32\_t resId | 资源ID。 |
| uint32\_t \*resultValue | 写入resultValue的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001001 - 无效的资源ID。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。  [ERROR\_CODE\_RES\_REF\_TOO\_MUCH](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001006 - 资源被循环引用。 |

### OH\_ResourceManager\_GetColorByName()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetColorByName(const NativeResourceManager *mgr, const char *resName, uint32_t *resultValue)
```

**描述**

通过指定资源ID，获取对应的颜色值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*resName | 资源名称。 |
| uint32\_t \*resultValue | 写入resultValue的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001003 - 无效的资源名称。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。  [ERROR\_CODE\_RES\_REF\_TOO\_MUCH](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001006 - 资源被循环引用。 |

### OH\_ResourceManager\_GetInt()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetInt(const NativeResourceManager *mgr, uint32_t resId, int *resultValue)
```

**描述**

通过指定资源ID，获取对应的int值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| uint32\_t resId | 资源ID。 |
| int \*resultValue | 写入resultValue的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001001 - 无效的资源ID。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。  [ERROR\_CODE\_RES\_REF\_TOO\_MUCH](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001006 - 资源被循环引用。 |

### OH\_ResourceManager\_GetIntByName()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetIntByName(const NativeResourceManager *mgr, const char *resName, int *resultValue)
```

**描述**

通过指定资源名称，获取对应的int值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*resName | 资源名称。 |
| int \*resultValue | 写入resultValue的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001003 - 无效的资源名称。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。  [ERROR\_CODE\_RES\_REF\_TOO\_MUCH](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001006 - 资源被循环引用。 |

### OH\_ResourceManager\_GetFloat()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetFloat(const NativeResourceManager *mgr, uint32_t resId, float *resultValue)
```

**描述**

通过指定资源ID，获取对应的float值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| uint32\_t resId | 资源ID。 |
| float \*resultValue | 写入resultValue的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001001 - 无效的资源ID。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。  [ERROR\_CODE\_RES\_REF\_TOO\_MUCH](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001006 - 资源被循环引用。 |

### OH\_ResourceManager\_GetFloatByName()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetFloatByName(const NativeResourceManager *mgr, const char *resName, float *resultValue)
```

**描述**

通过指定资源名称，获取对应的float值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*resName | 资源名称。 |
| float \*resultValue | 写入resultValue的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001003 - 无效的资源名称。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。  [ERROR\_CODE\_RES\_REF\_TOO\_MUCH](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001006 - 资源被循环引用。 |

### OH\_ResourceManager\_GetBool()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetBool(const NativeResourceManager *mgr, uint32_t resId, bool *resultValue)
```

**描述**

通过指定资源ID，获取对应的bool值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| uint32\_t resId | 资源ID。 |
| bool \*resultValue | 写入resultValue的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001001 - 无效的资源ID。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001002 - 没有根据资源ID找到匹配的资源。  [ERROR\_CODE\_RES\_REF\_TOO\_MUCH](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001006 - 资源被循环引用。 |

### OH\_ResourceManager\_GetBoolByName()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_GetBoolByName(const NativeResourceManager *mgr, const char *resName, bool *resultValue)
```

**描述**

通过指定资源名称，获取对应的bool值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*resName | 资源名称。 |
| bool \*resultValue | 写入resultValue的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_RES\_ID\_NOT\_FOUND](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001003 - 无效的资源名称。  [ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001004 - 没有根据资源名称找到匹配的资源。  [ERROR\_CODE\_RES\_REF\_TOO\_MUCH](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001006 - 资源被循环引用。 |

### OH\_ResourceManager\_AddResource()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_AddResource(const NativeResourceManager *mgr, const char *path)
```

**描述**

在应用程序运行时添加overlay资源。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*path | 资源路径。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_OVERLAY\_RES\_PATH\_INVALID](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001010 - 无效的资源路径. |

### OH\_ResourceManager\_RemoveResource()

PhonePC/2in1TabletTVWearable

```
1. ResourceManager_ErrorCode OH_ResourceManager_RemoveResource(const NativeResourceManager *mgr, const char *path)
```

**描述**

在应用程序运行时删除overlay资源。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const NativeResourceManager](capi-rawfile-nativeresourcemanager.md) \*mgr | 指向[NativeResourceManager](capi-rawfile-nativeresourcemanager.md)的指针，此指针通过[OH\_ResourceManager\_InitNativeResourceManager](capi-raw-file-manager-h.md#oh_resourcemanager_initnativeresourcemanager)方法获取。 |
| const char \*path | 资源路径。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager\_ErrorCode](capi-resmgr-common-h.md#resourcemanager_errorcode) | [SUCCESS](capi-resmgr-common-h.md#resourcemanager_errorcode) 0 - 成功。  [ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](capi-resmgr-common-h.md#resourcemanager_errorcode) 401 - 输入参数无效。可能的原因：1.参数类型不正确；2.参数验证失败。  [ERROR\_CODE\_OVERLAY\_RES\_PATH\_INVALID](capi-resmgr-common-h.md#resourcemanager_errorcode) 9001010 - 无效的资源路径. |
