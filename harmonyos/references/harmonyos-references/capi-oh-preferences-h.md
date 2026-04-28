---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-preferences-h
title: oh_preferences.h
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 头文件 > oh_preferences.h
category: harmonyos-references
scraped_at: 2026-04-28T07:59:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:eea26dc3d6637f3268a287a64b76eab920aeeeececf143e495e840d66c6d2a80
---

## 概述

PhonePC/2in1TabletTVWearable

提供访问Preferences对象的接口与数据结构。

**引用文件：** <database/preferences/oh\_preferences.h>

**库：** libohpreferences.so

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 13

**相关模块：** [Preferences](capi-preferences.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Preferences](capi-preferences-oh-preferences.md) | OH\_Preferences | 定义Preferences对象类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_PreferencesDataObserver)(void \*context, const OH\_PreferencesPair \*pairs, uint32\_t count)](capi-oh-preferences-h.md#oh_preferencesdataobserver) | OH\_PreferencesDataObserver | 定义数据变更触发的回调函数类型。 |
| [OH\_Preferences \*OH\_Preferences\_Open(OH\_PreferencesOption \*option, int \*errCode)](capi-oh-preferences-h.md#oh_preferences_open) | - | 打开一个Preferences实例对象并创建指向它的指针。  当不再需要使用指针时，请使用[OH\_Preferences\_Close](capi-oh-preferences-h.md#oh_preferences_close)关闭实例对象。 |
| [int OH\_Preferences\_Close(OH\_Preferences \*preference)](capi-oh-preferences-h.md#oh_preferences_close) | - | 关闭一个Preferences实例对象。 |
| [int OH\_Preferences\_GetInt(OH\_Preferences \*preference, const char \*key, int \*value)](capi-oh-preferences-h.md#oh_preferences_getint) | - | 获取Preferences实例对象中Key对应的整型值。 |
| [int OH\_Preferences\_GetBool(OH\_Preferences \*preference, const char \*key, bool \*value)](capi-oh-preferences-h.md#oh_preferences_getbool) | - | 获取Preferences实例对象中Key对应的布尔值。 |
| [int OH\_Preferences\_GetString(OH\_Preferences \*preference, const char \*key, char \*\*value, uint32\_t \*valueLen)](capi-oh-preferences-h.md#oh_preferences_getstring) | - | 获取Preferences实例对象中Key对应的字符串。 |
| [void OH\_Preferences\_FreeString(char \*string)](capi-oh-preferences-h.md#oh_preferences_freestring) | - | 释放从Preferences实例对象中获取的字符串。 |
| [int OH\_Preferences\_SetInt(OH\_Preferences \*preference, const char \*key, int value)](capi-oh-preferences-h.md#oh_preferences_setint) | - | 根据Key设置Preferences实例对象中的整型值。 |
| [int OH\_Preferences\_SetBool(OH\_Preferences \*preference, const char \*key, bool value)](capi-oh-preferences-h.md#oh_preferences_setbool) | - | 根据Key设置Preferences实例对象中的布尔值。 |
| [int OH\_Preferences\_SetString(OH\_Preferences \*preference, const char \*key, const char \*value)](capi-oh-preferences-h.md#oh_preferences_setstring) | - | 根据Key设置Preferences实例对象中的字符串。 |
| [int OH\_Preferences\_Delete(OH\_Preferences \*preference, const char \*key)](capi-oh-preferences-h.md#oh_preferences_delete) | - | 在Preferences实例对象中删除Key对应的KV数据。 |
| [int OH\_Preferences\_RegisterDataObserver(OH\_Preferences \*preference, void \*context,OH\_PreferencesDataObserver observer, const char \*keys[], uint32\_t keyCount)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-preferences-h#oh_preferences_registerdataobserver) | - | 对选取的Key注册数据变更订阅。订阅的Key的值发生变更后，在调用OH\_Preferences\_Close()后触发回调。 |
| [int OH\_Preferences\_UnregisterDataObserver(OH\_Preferences \*preference, void \*context,OH\_PreferencesDataObserver observer, const char \*keys[], uint32\_t keyCount)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-preferences-h#oh_preferences_unregisterdataobserver) | - | 取消注册选取Key的数据变更订阅。 |
| [int OH\_Preferences\_IsStorageTypeSupported(Preferences\_StorageType type, bool \*isSupported)](capi-oh-preferences-h.md#oh_preferences_isstoragetypesupported) | - | 校验当前平台是否支持对应存储模式。 |
| [int OH\_Preferences\_DeletePreferences(OH\_PreferencesOption \*option)](capi-oh-preferences-h.md#oh_preferences_deletepreferences) | - | 删除指定的Preferences对象。 |
| [int OH\_Preferences\_SetValue(OH\_Preferences \*preference, const char \*key, OH\_PreferencesValue \*value)](capi-oh-preferences-h.md#oh_preferences_setvalue) | - | 在Preferences对象中设置值[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)。 |
| [int OH\_Preferences\_GetValue(OH\_Preferences \*preference, const char \*key, OH\_PreferencesValue \*\*value)](capi-oh-preferences-h.md#oh_preferences_getvalue) | - | 根据给定的Key获取Preferences对象中的值。 |
| [int OH\_Preferences\_GetAll(OH\_Preferences \*preference, OH\_PreferencesPair \*\*pairs, uint32\_t \*count)](capi-oh-preferences-h.md#oh_preferences_getall) | - | 获取Preferences对象中的所有值。 |
| [bool OH\_Preferences\_HasKey(OH\_Preferences \*preference, const char \*key)](capi-oh-preferences-h.md#oh_preferences_haskey) | - | 检查Preferences对象是否包含与指定Key匹配的KV数据，若包含则返回true，否则返回false。 |
| [int OH\_Preferences\_Flush(OH\_Preferences \*preference)](capi-oh-preferences-h.md#oh_preferences_flush) | - | 将[OH\_Preferences](capi-preferences-oh-preferences.md)对象的缓存保存到xml文件中。 |
| [int OH\_Preferences\_ClearCache(OH\_Preferences \*preference)](capi-oh-preferences-h.md#oh_preferences_clearcache) | - | 清除[OH\_Preferences](capi-preferences-oh-preferences.md)对象缓存中的所有值。 |
| [int OH\_Preferences\_RegisterMultiProcessDataObserver(OH\_Preferences \*preference, void \*context, OH\_PreferencesDataObserver observer)](capi-oh-preferences-h.md#oh_preferences_registermultiprocessdataobserver) | - | 为Preferences对象注册一个多进程数据观察者。 |
| [int OH\_Preferences\_UnregisterMultiProcessDataObserver(OH\_Preferences \*preference, void \*context, OH\_PreferencesDataObserver observer)](capi-oh-preferences-h.md#oh_preferences_unregistermultiprocessdataobserver) | - | 取消注册Preferences对象的多进程数据观察者。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_PreferencesDataObserver()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_PreferencesDataObserver)(void *context, const OH_PreferencesPair *pairs, uint32_t count)
```

**描述**

定义数据变更触发的回调函数类型。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void \*context | 应用上下文的指针。 |
| const [OH\_PreferencesPair](capi-preferences-oh-preferencespair.md) \*pairs | 发生变更的KV数据的指针。 |
| uint32\_t count | 发生变更的KV数据的数量。 |

### OH\_Preferences\_Open()

PhonePC/2in1TabletTVWearable

```
1. OH_Preferences *OH_Preferences_Open(OH_PreferencesOption *option, int *errCode)
```

**描述**

打开一个Preferences实例对象并创建指向它的指针。

当不再需要使用指针时，请使用[OH\_Preferences\_Close](capi-oh-preferences-h.md#oh_preferences_close)关闭实例对象。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PreferencesOption](capi-preferences-oh-preferencesoption.md) \*option | 指向Preferences配置选项[OH\_PreferencesOption](capi-preferences-oh-preferencesoption.md)的指针。 |
| int \*errCode | 该参数作为出参使用，表示指向返回错误码的指针，详见[OH\_Preferences\_ErrCode](capi-oh-preferences-err-code-h.md#oh_preferences_errcode)。  若错误码为PREFERENCES\_OK，表示操作成功。  若错误码为PREFERENCES\_ERROR\_INVALID\_PARAM，表示参数不合法。  若错误码为PREFERENCES\_ERROR\_NOT\_SUPPORTED，表示系统能力不支持。  若错误码为PREFERENCES\_ERROR\_DELETE\_FILE，表示删除文件失败。  若错误码为PREFERENCES\_ERROR\_STORAGE，表示存储异常。  若错误码为PREFERENCES\_ERROR\_MALLOC，表示内存分配失败。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Preferences](capi-preferences-oh-preferences.md) | 当操作成功时，返回指向打开的Preferences对象[OH\_Preferences](capi-preferences-oh-preferences.md)实例对象的指针，失败返回空指针。 |

### OH\_Preferences\_Close()

PhonePC/2in1TabletTVWearable

```
1. int OH_Preferences_Close(OH_Preferences *preference)
```

**描述**

关闭一个Preferences实例对象。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Preferences](capi-preferences-oh-preferences.md) \*preference | 指向需要关闭的Preferences[OH\_Preferences](capi-preferences-oh-preferences.md)实例对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码，详见[OH\_Preferences\_ErrCode](capi-oh-preferences-err-code-h.md#oh_preferences_errcode)。  若错误码为PREFERENCES\_OK，表示操作成功。  若错误码为PREFERENCES\_ERROR\_INVALID\_PARAM，表示参数不合法。  若错误码为PREFERENCES\_ERROR\_STORAGE，表示存储异常。  若错误码为PREFERENCES\_ERROR\_MALLOC，表示内存分配失败。 |

### OH\_Preferences\_GetInt()

PhonePC/2in1TabletTVWearable

```
1. int OH_Preferences_GetInt(OH_Preferences *preference, const char *key, int *value)
```

**描述**

获取Preferences实例对象中Key对应的整型值。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Preferences](capi-preferences-oh-preferences.md) \*preference | 指向目标Preferences[OH\_Preferences](capi-preferences-oh-preferences.md)实例对象的指针。 |
| const char \*key | 需要获取的Key的指针。 |
| int \*value | 该参数作为出参使用，表示指向获取到的整型值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码为PREFERENCES\_OK，表示操作成功。  若错误码为PREFERENCES\_ERROR\_INVALID\_PARAM，表示参数不合法。  若错误码为PREFERENCES\_ERROR\_STORAGE，表示存储异常。  若错误码为PREFERENCES\_ERROR\_MALLOC，表示内存分配失败。  若错误码为PREFERENCES\_ERROR\_KEY\_NOT\_FOUND，表示查询的Key不存在。 |

### OH\_Preferences\_GetBool()

PhonePC/2in1TabletTVWearable

```
1. int OH_Preferences_GetBool(OH_Preferences *preference, const char *key, bool *value)
```

**描述**

获取Preferences实例对象中Key对应的布尔值。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Preferences](capi-preferences-oh-preferences.md) \*preference | 指向目标Preferences[OH\_Preferences](capi-preferences-oh-preferences.md)实例对象的指针。 |
| const char \*key | 需要获取的Key的指针。 |
| bool \*value | 该参数作为出参使用，表示指向获取到的布尔值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码为PREFERENCES\_OK，表示操作成功。  若错误码为PREFERENCES\_ERROR\_INVALID\_PARAM，表示参数不合法。  若错误码为PREFERENCES\_ERROR\_STORAGE，表示存储异常。  若错误码为PREFERENCES\_ERROR\_MALLOC，表示内存分配失败。  若错误码为PREFERENCES\_ERROR\_KEY\_NOT\_FOUND，表示查询的key不存在。 |

### OH\_Preferences\_GetString()

PhonePC/2in1TabletTVWearable

```
1. int OH_Preferences_GetString(OH_Preferences *preference, const char *key, char **value, uint32_t *valueLen)
```

**描述**

获取Preferences实例对象中Key对应的字符串。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Preferences](capi-preferences-oh-preferences.md) \*preference | 指向目标Preferences[OH\_Preferences](capi-preferences-oh-preferences.md)实例对象的指针。 |
| const char \*key | 需要获取的Key的指针。 |
| char \*\*value | 该参数作为出参使用，表示指向获取到的字符串的二级指针，使用完毕后需要调用释放函数[OH\_Preferences\_FreeString](capi-oh-preferences-h.md#oh_preferences_freestring)释放内存。 |
| uint32\_t \*valueLen | 该参数作为出参使用，表示获取到的字符串长度的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码为PREFERENCES\_OK，表示操作成功。  若错误码为PREFERENCES\_ERROR\_INVALID\_PARAM，表示参数不合法。  若错误码为PREFERENCES\_ERROR\_STORAGE，表示存储异常。  若错误码为PREFERENCES\_ERROR\_MALLOC，表示内存分配失败。  若错误码为PREFERENCES\_ERROR\_KEY\_NOT\_FOUND，表示查询的Key不存在。 |

### OH\_Preferences\_FreeString()

PhonePC/2in1TabletTVWearable

```
1. void OH_Preferences_FreeString(char *string)
```

**描述**

释放从Preferences实例对象中获取的字符串。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*string | 需要释放的字符串指针。 |

### OH\_Preferences\_SetInt()

PhonePC/2in1TabletTVWearable

```
1. int OH_Preferences_SetInt(OH_Preferences *preference, const char *key, int value)
```

**描述**

根据Key设置Preferences实例对象中的整型值。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Preferences](capi-preferences-oh-preferences.md) \*preference | 指向目标Preferences[OH\_Preferences](capi-preferences-oh-preferences.md)实例对象的指针。 |
| const char \*key | 指向需要设置的Key的指针。 |
| int value | 需要设置的整型值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码为PREFERENCES\_OK，表示操作成功。  若错误码为PREFERENCES\_ERROR\_INVALID\_PARAM，表示参数不合法。  若错误码为PREFERENCES\_ERROR\_STORAGE，表示存储异常。  若错误码为PREFERENCES\_ERROR\_MALLOC，表示内存分配失败。 |

### OH\_Preferences\_SetBool()

PhonePC/2in1TabletTVWearable

```
1. int OH_Preferences_SetBool(OH_Preferences *preference, const char *key, bool value)
```

**描述**

根据Key设置Preferences实例对象中的布尔值。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Preferences](capi-preferences-oh-preferences.md) \*preference | 指向目标Preferences[OH\_Preferences](capi-preferences-oh-preferences.md)实例对象的指针。 |
| const char \*key | 指向需要设置的Key的指针。 |
| bool value | 需要设置的布尔值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码为PREFERENCES\_OK，表示操作成功。  若错误码为PREFERENCES\_ERROR\_INVALID\_PARAM，表示参数不合法。  若错误码为PREFERENCES\_ERROR\_STORAGE，表示存储异常。  若错误码为PREFERENCES\_ERROR\_MALLOC，表示内存分配失败。 |

### OH\_Preferences\_SetString()

PhonePC/2in1TabletTVWearable

```
1. int OH_Preferences_SetString(OH_Preferences *preference, const char *key, const char *value)
```

**描述**

根据Key设置Preferences实例对象中的字符串。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Preferences](capi-preferences-oh-preferences.md) \*preference | 指向目标Preferences[OH\_Preferences](capi-preferences-oh-preferences.md)实例对象的指针。 |
| const char \*key | 指向需要设置的Key的指针。 |
| const char \*value | 指向需要设置的字符串指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码为PREFERENCES\_OK，表示操作成功。  若错误码为PREFERENCES\_ERROR\_INVALID\_PARAM，表示参数不合法。  若错误码为PREFERENCES\_ERROR\_STORAGE，表示存储异常。  若错误码为PREFERENCES\_ERROR\_MALLOC，表示内存分配失败。 |

### OH\_Preferences\_Delete()

PhonePC/2in1TabletTVWearable

```
1. int OH_Preferences_Delete(OH_Preferences *preference, const char *key)
```

**描述**

在Preferences实例对象中删除Key对应的KV数据。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Preferences](capi-preferences-oh-preferences.md) \*preference | 指向目标Preferences[OH\_Preferences](capi-preferences-oh-preferences.md)实例对象的指针。 |
| const char \*key | 指向需要删除的Key的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码为PREFERENCES\_OK，表示操作成功。  若错误码为PREFERENCES\_ERROR\_INVALID\_PARAM，表示参数不合法。  若错误码为PREFERENCES\_ERROR\_STORAGE，表示存储异常。  若错误码为PREFERENCES\_ERROR\_MALLOC，表示内存分配失败。 |

### OH\_Preferences\_RegisterDataObserver()

PhonePC/2in1TabletTVWearable

```
1. int OH_Preferences_RegisterDataObserver(OH_Preferences *preference, void *context,OH_PreferencesDataObserver observer, const char *keys[], uint32_t keyCount)
```

**描述**

对选取的Key注册数据变更订阅。订阅的Key的值发生变更后，在调用OH\_Preferences\_Close()后触发回调。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Preferences](capi-preferences-oh-preferences.md) \*preference | 指向目标Preferences[OH\_Preferences](capi-preferences-oh-preferences.md)实例对象的指针。 |
| void \*context | 应用上下文的指针。 |
| [OH\_PreferencesDataObserver](capi-oh-preferences-h.md#oh_preferencesdataobserver) observer | 订阅数据变更关联的回调函数[OH\_PreferencesDataObserver](capi-oh-preferences-h.md#oh_preferencesdataobserver)。 |
| const char \*keys[] | 需要订阅的Key数组。 |
| uint32\_t keyCount | 需要订阅的Key的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码为PREFERENCES\_OK，表示操作成功。  若错误码为PREFERENCES\_ERROR\_INVALID\_PARAM，表示参数不合法。  若错误码为PREFERENCES\_ERROR\_STORAGE，表示存储异常。  若错误码为PREFERENCES\_ERROR\_MALLOC，表示内存分配失败。  若错误码为PREFERENCES\_ERROR\_GET\_DATAOBSMGRCLIENT，表示获取数据变更订阅服务失败。 |

### OH\_Preferences\_UnregisterDataObserver()

PhonePC/2in1TabletTVWearable

```
1. int OH_Preferences_UnregisterDataObserver(OH_Preferences *preference, void *context,OH_PreferencesDataObserver observer, const char *keys[], uint32_t keyCount)
```

**描述**

取消注册选取Key的数据变更订阅。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Preferences](capi-preferences-oh-preferences.md) \*preference | 指向目标Preferences[OH\_Preferences](capi-preferences-oh-preferences.md)实例对象的指针。 |
| void \*context | 应用上下文的指针。 |
| [OH\_PreferencesDataObserver](capi-oh-preferences-h.md#oh_preferencesdataobserver) observer | 订阅数据变更关联的回调函数[OH\_PreferencesDataObserver](capi-oh-preferences-h.md#oh_preferencesdataobserver)。 |
| const char \*keys[] | 需要取消订阅的Key数组。 |
| uint32\_t keyCount | 需要取消订阅的Key的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码为PREFERENCES\_OK，表示操作成功。  若错误码为PREFERENCES\_ERROR\_INVALID\_PARAM，表示参数不合法。  若错误码为PREFERENCES\_ERROR\_STORAGE，表示存储异常。  若错误码为PREFERENCES\_ERROR\_MALLOC，表示内存分配失败。 |

### OH\_Preferences\_IsStorageTypeSupported()

PhonePC/2in1TabletTVWearable

```
1. int OH_Preferences_IsStorageTypeSupported(Preferences_StorageType type, bool *isSupported)
```

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Preferences\_StorageType](capi-oh-preferences-option-h.md#preferences_storagetype) type | 要校验是否支持的存储模式。 |
| bool \*isSupported | 校验结果的指针，作为出参使用。true表示当前平台支持当前校验的存储模式，false表示当前平台不支持当前校验的存储模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回接口操作执行的状态码。  PREFERENCES\_OK，表示操作成功。  PREFERENCES\_ERROR\_INVALID\_PARAM，表示参数不合法。 |

### OH\_Preferences\_DeletePreferences()

PhonePC/2in1TabletTVWearable

```
1. int OH_Preferences_DeletePreferences(OH_PreferencesOption *option)
```

**描述**

删除指定的Preferences对象。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PreferencesOption](capi-preferences-oh-preferencesoption.md) \*option | 指向Preferences配置选项[OH\_PreferencesOption](capi-preferences-oh-preferencesoption.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码为PREFERENCES\_OK，表示操作成功。  若错误码为PREFERENCES\_ERROR\_INVALID\_PARAM，表示参数不合法。  若错误码为PREFERENCES\_ERROR\_NOT\_SUPPORTED，表示系统能力不支持。  若错误码为PREFERENCES\_ERROR\_DELETE\_FILE，表示删除文件失败。 |

### OH\_Preferences\_SetValue()

PhonePC/2in1TabletTVWearable

```
1. int OH_Preferences_SetValue(OH_Preferences *preference, const char *key, OH_PreferencesValue *value)
```

**描述**

在Preferences对象中设置值[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Preferences](capi-preferences-oh-preferences.md) \*preference | 指向目标[OH\_Preferences](capi-preferences-oh-preferences.md)实例的指针。 |
| const char \*key | 指向需要设置的Key的指针。 |
| [OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*value | 指向需要设置的[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |

### OH\_Preferences\_GetValue()

PhonePC/2in1TabletTVWearable

```
1. int OH_Preferences_GetValue(OH_Preferences *preference, const char *key, OH_PreferencesValue **value)
```

**描述**

根据给定的Key获取Preferences对象中的值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Preferences](capi-preferences-oh-preferences.md) \*preference | 指向目标[OH\_Preferences](capi-preferences-oh-preferences.md)实例的指针。 |
| const char \*key | 指向需要获取值的Key的指针。 |
| [OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*\*value | 指向获取到的[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)值的二级指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。  若错误码PREFERENCES\_ERROR\_KEY\_NOT\_FOUND表示查询的Key不存在。 |

### OH\_Preferences\_GetAll()

PhonePC/2in1TabletTVWearable

```
1. int OH_Preferences_GetAll(OH_Preferences *preference, OH_PreferencesPair **pairs, uint32_t *count)
```

**描述**

获取Preferences对象中的所有值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Preferences](capi-preferences-oh-preferences.md) \*preference | 指向目标[OH\_Preferences](capi-preferences-oh-preferences.md)实例的指针。 |
| [OH\_PreferencesPair](capi-preferences-oh-preferencespair.md) \*\*pairs | 指向要获取的KV数据的指针。当不再需要此KV数据时，用户需要调用[OH\_Preferences\_FreeString](capi-oh-preferences-h.md#oh_preferences_freestring)释放内存。 |
| uint32\_t \*count | 指向获取到的所有值的数量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。  若错误码PREFERENCES\_ERROR\_KEY\_NOT\_FOUND表示查询的Key不存在。 |

### OH\_Preferences\_HasKey()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Preferences_HasKey(OH_Preferences *preference, const char *key)
```

**描述**

检查Preferences对象是否包含与指定Key匹配的KV数据，若包含则返回true，否则返回false。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Preferences](capi-preferences-oh-preferences.md) \*preference | 指向目标[OH\_Preferences](capi-preferences-oh-preferences.md)实例的指针。 |
| const char \*key | 指向需要检查的Key的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回true则表示Preferences对象包含与指定Key匹配的KV数据，否则返回false。 |

### OH\_Preferences\_Flush()

PhonePC/2in1TabletTVWearable

```
1. int OH_Preferences_Flush(OH_Preferences *preference)
```

**描述**

将[OH\_Preferences](capi-preferences-oh-preferences.md)对象的缓存保存到xml文件中。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Preferences](capi-preferences-oh-preferences.md) \*preference | 指向目标[OH\_Preferences](capi-preferences-oh-preferences.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_NOT\_SUPPORTED表示系统能力不支持。 |

### OH\_Preferences\_ClearCache()

PhonePC/2in1TabletTVWearable

```
1. int OH_Preferences_ClearCache(OH_Preferences *preference)
```

**描述**

清除[OH\_Preferences](capi-preferences-oh-preferences.md)对象缓存中的所有值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Preferences](capi-preferences-oh-preferences.md) \*preference | 指向目标[OH\_Preferences](capi-preferences-oh-preferences.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_NOT\_SUPPORTED表示系统能力不支持。 |

### OH\_Preferences\_RegisterMultiProcessDataObserver()

PhonePC/2in1TabletTVWearable

```
1. int OH_Preferences_RegisterMultiProcessDataObserver(OH_Preferences *preference, void *context, OH_PreferencesDataObserver observer)
```

**描述**

为Preferences对象注册一个多进程数据观察者。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Preferences](capi-preferences-oh-preferences.md) \*preference | 指向目标[OH\_Preferences](capi-preferences-oh-preferences.md)实例的指针。 |
| void \*context | 指向数据观察者上下文的指针。 |
| [OH\_PreferencesDataObserver](capi-oh-preferences-h.md#oh_preferencesdataobserver) observer | 要注册的[OH\_PreferencesDataObserver](capi-oh-preferences-h.md#oh_preferencesdataobserver)回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。  若错误码PREFERENCES\_ERROR\_GET\_DATAOBSMGRCLIENT表示获取数据变更订阅服务失败。 |

### OH\_Preferences\_UnregisterMultiProcessDataObserver()

PhonePC/2in1TabletTVWearable

```
1. int OH_Preferences_UnregisterMultiProcessDataObserver(OH_Preferences *preference, void *context, OH_PreferencesDataObserver observer)
```

**描述**

取消注册Preferences对象的多进程数据观察者。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Preferences](capi-preferences-oh-preferences.md) \*preference | 指向目标[OH\_Preferences](capi-preferences-oh-preferences.md)实例的指针。 |
| void \*context | 指向数据观察者上下文的指针。 |
| [OH\_PreferencesDataObserver](capi-oh-preferences-h.md#oh_preferencesdataobserver) observer | 要取消注册的[OH\_PreferencesDataObserver](capi-oh-preferences-h.md#oh_preferencesdataobserver)回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |
