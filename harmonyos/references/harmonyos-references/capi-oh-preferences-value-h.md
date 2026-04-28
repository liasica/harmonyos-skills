---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-preferences-value-h
title: oh_preferences_value.h
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 头文件 > oh_preferences_value.h
category: harmonyos-references
scraped_at: 2026-04-28T07:59:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:decf81bf11f867b5a0a564601d6631e7954d1f21cba6ed8b81f265f1383758bc
---

## 概述

PhonePC/2in1TabletTVWearable

提供访问Preferences值（PreferencesValue）对象的接口、枚举类型与数据结构。

**引用文件：** <database/preferences/oh\_preferences\_value.h>

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
| [OH\_PreferencesPair](capi-preferences-oh-preferencespair.md) | OH\_PreferencesPair | 定义Preferences使用的KV数据对象类型。 |
| [OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) | OH\_PreferencesValue | 定义PreferencesValue对象类型。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Preference\_ValueType](capi-oh-preferences-value-h.md#preference_valuetype) | Preference\_ValueType | 定义PreferencesValue的数据类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [const char \*OH\_PreferencesPair\_GetKey(const OH\_PreferencesPair \*pairs, uint32\_t index)](capi-oh-preferences-value-h.md#oh_preferencespair_getkey) | 获取KV数据中索引对应数据的键。 |
| [const OH\_PreferencesValue \*OH\_PreferencesPair\_GetPreferencesValue(const OH\_PreferencesPair \*pairs, uint32\_t index)](capi-oh-preferences-value-h.md#oh_preferencespair_getpreferencesvalue) | 获取KV数据数组中索引对应的值。 |
| [Preference\_ValueType OH\_PreferencesValue\_GetValueType(const OH\_PreferencesValue \*object)](capi-oh-preferences-value-h.md#oh_preferencesvalue_getvaluetype) | 获取PreferencesValue对象的数据类型。 |
| [int OH\_PreferencesValue\_GetInt(const OH\_PreferencesValue \*object, int \*value)](capi-oh-preferences-value-h.md#oh_preferencesvalue_getint) | 从PreferencesValue对象[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)中获取一个整型值。 |
| [int OH\_PreferencesValue\_GetBool(const OH\_PreferencesValue \*object, bool \*value)](capi-oh-preferences-value-h.md#oh_preferencesvalue_getbool) | 从PreferencesValue对象[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)中获取一个布尔值。 |
| [int OH\_PreferencesValue\_GetString(const OH\_PreferencesValue \*object, char \*\*value, uint32\_t \*valueLen)](capi-oh-preferences-value-h.md#oh_preferencesvalue_getstring) | 从PreferencesValue对象[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)中获取字符串。 |
| [void OH\_PreferencesPair\_Destroy(OH\_PreferencesPair \*pairs, uint32\_t count)](capi-oh-preferences-value-h.md#oh_preferencespair_destroy) | 销毁一个[OH\_PreferencesPair](capi-preferences-oh-preferencespair.md)实例。 |
| [OH\_PreferencesValue\* OH\_PreferencesValue\_Create(void)](capi-oh-preferences-value-h.md#oh_preferencesvalue_create) | 创建一个[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例。 |
| [void OH\_PreferencesValue\_Destroy(OH\_PreferencesValue \*value)](capi-oh-preferences-value-h.md#oh_preferencesvalue_destroy) | 销毁一个[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例。 |
| [int OH\_PreferencesValue\_SetInt(const OH\_PreferencesValue \*object, int value)](capi-oh-preferences-value-h.md#oh_preferencesvalue_setint) | 为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置整型值。 |
| [int OH\_PreferencesValue\_SetBool(const OH\_PreferencesValue \*object, bool value)](capi-oh-preferences-value-h.md#oh_preferencesvalue_setbool) | 为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置布尔值。 |
| [int OH\_PreferencesValue\_SetString(const OH\_PreferencesValue \*object, const char \*value)](capi-oh-preferences-value-h.md#oh_preferencesvalue_setstring) | 为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置字符串值。 |
| [int OH\_PreferencesValue\_SetInt64(const OH\_PreferencesValue \*object, int64\_t value)](capi-oh-preferences-value-h.md#oh_preferencesvalue_setint64) | 为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置int64值。 |
| [int OH\_PreferencesValue\_GetInt64(const OH\_PreferencesValue \*object, int64\_t \*value)](capi-oh-preferences-value-h.md#oh_preferencesvalue_getint64) | 获取[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的int64值。 |
| [int OH\_PreferencesValue\_SetDouble(const OH\_PreferencesValue \*object, double value)](capi-oh-preferences-value-h.md#oh_preferencesvalue_setdouble) | 为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置double值。 |
| [int OH\_PreferencesValue\_GetDouble(const OH\_PreferencesValue \*object, double \*value)](capi-oh-preferences-value-h.md#oh_preferencesvalue_getdouble) | 获取[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的double值。 |
| [int OH\_PreferencesValue\_SetIntArray(const OH\_PreferencesValue \*object, const int \*value, uint32\_t count)](capi-oh-preferences-value-h.md#oh_preferencesvalue_setintarray) | 为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置整型数组值。 |
| [int OH\_PreferencesValue\_GetIntArray(const OH\_PreferencesValue \*object, int \*\*value, uint32\_t \*count)](capi-oh-preferences-value-h.md#oh_preferencesvalue_getintarray) | 获取[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的整型数组值。 |
| [int OH\_PreferencesValue\_SetBoolArray(const OH\_PreferencesValue \*object, const bool \*value, uint32\_t count)](capi-oh-preferences-value-h.md#oh_preferencesvalue_setboolarray) | 为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置布尔数组值。 |
| [int OH\_PreferencesValue\_GetBoolArray(const OH\_PreferencesValue \*object, bool \*\*value, uint32\_t \*count)](capi-oh-preferences-value-h.md#oh_preferencesvalue_getboolarray) | 获取[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的布尔数组值。 |
| [int OH\_PreferencesValue\_SetStringArray(const OH\_PreferencesValue \*object, const char \*\*value, uint32\_t count)](capi-oh-preferences-value-h.md#oh_preferencesvalue_setstringarray) | 为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置字符串数组值。 |
| [int OH\_PreferencesValue\_GetStringArray(const OH\_PreferencesValue \*object, char \*\*\*value, uint32\_t \*count)](capi-oh-preferences-value-h.md#oh_preferencesvalue_getstringarray) | 获取[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的字符串数组值。 |
| [int OH\_PreferencesValue\_SetInt64Array(const OH\_PreferencesValue \*object, const int64\_t \*value, uint32\_t count)](capi-oh-preferences-value-h.md#oh_preferencesvalue_setint64array) | 为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置int64数组值。 |
| [int OH\_PreferencesValue\_GetInt64Array(const OH\_PreferencesValue \*object, int64\_t \*\*value, uint32\_t \*count)](capi-oh-preferences-value-h.md#oh_preferencesvalue_getint64array) | 获取[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的int64数组值。 |
| [int OH\_PreferencesValue\_SetDoubleArray(const OH\_PreferencesValue \*object, const double \*value, uint32\_t count)](capi-oh-preferences-value-h.md#oh_preferencesvalue_setdoublearray) | 为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置double数组值。 |
| [int OH\_PreferencesValue\_GetDoubleArray(const OH\_PreferencesValue \*object, double \*\*value, uint32\_t \*count)](capi-oh-preferences-value-h.md#oh_preferencesvalue_getdoublearray) | 获取[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的double数组值。 |
| [int OH\_PreferencesValue\_SetBlob(const OH\_PreferencesValue \*object, const uint8\_t \*value, uint32\_t count)](capi-oh-preferences-value-h.md#oh_preferencesvalue_setblob) | 为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置二进制值。 |
| [int OH\_PreferencesValue\_GetBlob(const OH\_PreferencesValue \*object, uint8\_t \*\*value, uint32\_t \*count)](capi-oh-preferences-value-h.md#oh_preferencesvalue_getblob) | 获取[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的二进制值。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### Preference\_ValueType

PhonePC/2in1TabletTVWearable

```
1. enum Preference_ValueType
```

**描述**

定义PreferencesValue的数据类型。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| PREFERENCE\_TYPE\_NULL = 0 | 空类型。 |
| PREFERENCE\_TYPE\_INT | 整型类型。 |
| PREFERENCE\_TYPE\_BOOL | 布尔类型。 |
| PREFERENCE\_TYPE\_STRING | 字符串类型。 |
| PREFERENCE\_TYPE\_INT64 | 64位整型类型。  **起始版本：** 23 |
| PREFERENCE\_TYPE\_DOUBLE | 浮点型类型。  **起始版本：** 23 |
| PREFERENCE\_TYPE\_INT\_ARRAY | 整型数组。  **起始版本：** 23 |
| PREFERENCE\_TYPE\_BOOL\_ARRAY | 布尔数组。  **起始版本：** 23 |
| PREFERENCE\_TYPE\_STRING\_ARRAY | 字符串数组。  **起始版本：** 23 |
| PREFERENCE\_TYPE\_INT64\_ARRAY | 64位整型数组。  **起始版本：** 23 |
| PREFERENCE\_TYPE\_DOUBLE\_ARRAY | 浮点型数组。  **起始版本：** 23 |
| PREFERENCE\_TYPE\_BLOB | 二进制数据。  **起始版本：** 23 |
| PREFERENCE\_TYPE\_BUTT | 结束类型。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_PreferencesPair\_GetKey()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_PreferencesPair_GetKey(const OH_PreferencesPair *pairs, uint32_t index)
```

**描述**

获取KV数据中索引对应数据的键。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_PreferencesPair](capi-preferences-oh-preferencespair.md) \*pairs | 目标KV数据[OH\_PreferencesPair](capi-preferences-oh-preferencespair.md)的指针。 |
| uint32\_t index | 目标KV数据[OH\_PreferencesPair](capi-preferences-oh-preferencespair.md)的索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char \* | 如果操作成功，返回获取到的键的指针。操作失败或传参不合法返回空指针。 |

### OH\_PreferencesPair\_GetPreferencesValue()

PhonePC/2in1TabletTVWearable

```
1. const OH_PreferencesValue *OH_PreferencesPair_GetPreferencesValue(const OH_PreferencesPair *pairs, uint32_t index)
```

**描述**

获取KV数据数组中索引对应的值。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_PreferencesPair](capi-preferences-oh-preferencespair.md) \*pairs | 目标KV数据[OH\_PreferencesPair](capi-preferences-oh-preferencespair.md)的指针。 |
| uint32\_t index | 目标KV数据[OH\_PreferencesPair](capi-preferences-oh-preferencespair.md)的索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const [OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) | 如果操作成功，返回获取到的值对象的指针。操作失败或传参不合法返回空指针。 |

### OH\_PreferencesValue\_GetValueType()

PhonePC/2in1TabletTVWearable

```
1. Preference_ValueType OH_PreferencesValue_GetValueType(const OH_PreferencesValue *object)
```

**描述**

获取PreferencesValue对象的数据类型。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 对象[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Preference\_ValueType](capi-oh-preferences-value-h.md#preference_valuetype) | 返回获取到的数据类型枚举。若返回数据类型枚举为PREFERENCE\_TYPE\_NULL，代表传参不合法。 |

### OH\_PreferencesValue\_GetInt()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_GetInt(const OH_PreferencesValue *object, int *value)
```

**描述**

从PreferencesValue对象[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)中获取一个整型值。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 对象[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)的指针。 |
| int \*value | 该参数作为出参使用，表示指向获取到的整型值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码为PREFERENCES\_OK，表示操作成功。  若错误码为PREFERENCES\_ERROR\_INVALID\_PARAM，表示参数不合法。  若错误码为PREFERENCES\_ERROR\_STORAGE，表示存储异常。  若错误码为PREFERENCES\_ERROR\_MALLOC，表示内存分配失败。 |

### OH\_PreferencesValue\_GetBool()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_GetBool(const OH_PreferencesValue *object, bool *value)
```

**描述**

从PreferencesValue对象[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)中获取一个布尔值。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 对象[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)的指针。 |
| bool \*value | 该参数作为出参使用，表示指向获取到的布尔值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码为PREFERENCES\_OK，表示操作成功。  若错误码为PREFERENCES\_ERROR\_INVALID\_PARAM，表示参数不合法。  若错误码为PREFERENCES\_ERROR\_STORAGE，表示存储异常。  若错误码为PREFERENCES\_ERROR\_MALLOC，表示内存分配失败。 |

### OH\_PreferencesValue\_GetString()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_GetString(const OH_PreferencesValue *object, char **value, uint32_t *valueLen)
```

**描述**

从PreferencesValue对象[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)中获取字符串。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 对象[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)的指针。 |
| char \*\*value | 该参数作为出参使用，表示指向获取到的字符串的二级指针，使用完毕后需要调用释放函数[OH\_Preferences\_FreeString](capi-oh-preferences-h.md#oh_preferences_freestring)释放内存。 |
| uint32\_t \*valueLen | 该参数作为出参使用，表示指向获取到的字符串长度的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码为PREFERENCES\_OK，表示操作成功。  若错误码为PREFERENCES\_ERROR\_INVALID\_PARAM，表示参数不合法。  若错误码为PREFERENCES\_ERROR\_STORAGE，表示存储异常。  若错误码为PREFERENCES\_ERROR\_MALLOC，表示内存分配失败。 |

### OH\_PreferencesPair\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_PreferencesPair_Destroy(OH_PreferencesPair *pairs, uint32_t count)
```

**描述**

销毁一个[OH\_PreferencesPair](capi-preferences-oh-preferencespair.md)实例。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PreferencesPair](capi-preferences-oh-preferencespair.md) \*pairs | 指向目标[OH\_PreferencesPair](capi-preferences-oh-preferencespair.md)实例的指针。 |
| uint32\_t count | 需要销毁的KV数组大小。 |

### OH\_PreferencesValue\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_PreferencesValue* OH_PreferencesValue_Create(void)
```

**描述**

创建一个[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例。

**起始版本：** 23

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_PreferencesValue\*](capi-preferences-oh-preferencesvalue.md) | 如果操作成功，返回指向[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)值对象的指针，否则返回nullptr。 |

### OH\_PreferencesValue\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_PreferencesValue_Destroy(OH_PreferencesValue *value)
```

**描述**

销毁一个[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*value | 指向目标[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的指针。 |

### OH\_PreferencesValue\_SetInt()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_SetInt(const OH_PreferencesValue *object, int value)
```

**描述**

为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置整型值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 指向目标[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的指针。 |
| int value | 需要设置的整型值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |

### OH\_PreferencesValue\_SetBool()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_SetBool(const OH_PreferencesValue *object, bool value)
```

**描述**

为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置布尔值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 指向目标[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的指针。 |
| bool value | 需要设置的布尔值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |

### OH\_PreferencesValue\_SetString()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_SetString(const OH_PreferencesValue *object, const char *value)
```

**描述**

为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置字符串值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 指向目标[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的指针。 |
| const char \*value | 需要设置的字符串值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |

### OH\_PreferencesValue\_SetInt64()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_SetInt64(const OH_PreferencesValue *object, int64_t value)
```

**描述**

为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置int64值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 指向目标[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的指针。 |
| int64\_t value | 需要设置的int64值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |

### OH\_PreferencesValue\_GetInt64()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_GetInt64(const OH_PreferencesValue *object, int64_t *value)
```

**描述**

获取[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的int64值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 指向目标[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的指针。 |
| int64\_t \*value | 指向获取到的int64值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |

### OH\_PreferencesValue\_SetDouble()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_SetDouble(const OH_PreferencesValue *object, double value)
```

**描述**

为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置double值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 指向目标[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的指针。 |
| double value | 需要设置的double值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |

### OH\_PreferencesValue\_GetDouble()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_GetDouble(const OH_PreferencesValue *object, double *value)
```

**描述**

获取[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的double值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 指向目标[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的指针。 |
| double \*value | 指向获取到的double值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |

### OH\_PreferencesValue\_SetIntArray()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_SetIntArray(const OH_PreferencesValue *object, const int *value, uint32_t count)
```

**描述**

为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置整型数组值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 指向目标[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的指针。 |
| const int \*value | 需要设置的整型数组值。 |
| uint32\_t count | 指向需要设置的数组大小的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |

### OH\_PreferencesValue\_GetIntArray()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_GetIntArray(const OH_PreferencesValue *object, int **value, uint32_t *count)
```

**描述**

获取[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的整型数组值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 指向目标[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的指针。 |
| int \*\*value | 指向获取到的整型数组值的二级指针。 |
| uint32\_t \*count | 指向获取到的数组大小的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |

### OH\_PreferencesValue\_SetBoolArray()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_SetBoolArray(const OH_PreferencesValue *object, const bool *value, uint32_t count)
```

**描述**

为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置布尔数组值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 指向目标[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的指针。 |
| const bool \*value | 需要设置的布尔数组值。 |
| uint32\_t count | 指向需要设置的数组大小的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |

### OH\_PreferencesValue\_GetBoolArray()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_GetBoolArray(const OH_PreferencesValue *object, bool **value, uint32_t *count)
```

**描述**

获取[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的布尔数组值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 指向目标[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的指针。 |
| bool \*\*value | 指向获取到的布尔数组值的二级指针。 |
| uint32\_t \*count | 指向获取到的数组大小的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |

### OH\_PreferencesValue\_SetStringArray()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_SetStringArray(const OH_PreferencesValue *object, const char **value, uint32_t count)
```

**描述**

为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置字符串数组值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 指向目标[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的指针。 |
| const char \*\*value | 需要设置的字符串数组值。 |
| uint32\_t count | 指向需要设置的数组大小的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |

### OH\_PreferencesValue\_GetStringArray()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_GetStringArray(const OH_PreferencesValue *object, char ***value, uint32_t *count)
```

**描述**

获取[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的字符串数组值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 指向目标[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的指针。 |
| char \*\*\*value | 指向获取到的字符串数组值的二级指针。 |
| uint32\_t \*count | 指向获取到的数组大小的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |

### OH\_PreferencesValue\_SetInt64Array()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_SetInt64Array(const OH_PreferencesValue *object, const int64_t *value, uint32_t count)
```

**描述**

为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置int64数组值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 指向目标[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的指针。 |
| const int64\_t \*value | 需要设置的int64数组值。 |
| uint32\_t count | 指向需要设置的数组大小的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |

### OH\_PreferencesValue\_GetInt64Array()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_GetInt64Array(const OH_PreferencesValue *object, int64_t **value, uint32_t *count)
```

**描述**

获取[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的int64数组值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 指向目标[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的指针。 |
| int64\_t \*\*value | 指向获取到的int64数组值的二级指针。 |
| uint32\_t \*count | 指向获取到的数组大小的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |

### OH\_PreferencesValue\_SetDoubleArray()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_SetDoubleArray(const OH_PreferencesValue *object, const double *value, uint32_t count)
```

**描述**

为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置double数组值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 指向目标[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的指针。 |
| const double \*value | 需要设置的double数组值。 |
| uint32\_t count | 指向需要设置的数组大小的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |

### OH\_PreferencesValue\_GetDoubleArray()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_GetDoubleArray(const OH_PreferencesValue *object, double **value, uint32_t *count)
```

**描述**

获取[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的double数组值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 指向目标[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的指针。 |
| double \*\*value | 指向获取到的double数组值的二级指针。 |
| uint32\_t \*count | 指向获取到的数组大小的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |

### OH\_PreferencesValue\_SetBlob()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_SetBlob(const OH_PreferencesValue *object, const uint8_t *value, uint32_t count)
```

**描述**

为[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例设置二进制值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 指向目标[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的指针。 |
| const uint8\_t \*value | 需要设置的二进制值。 |
| uint32\_t count | 指向需要设置的二进制大小的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |

### OH\_PreferencesValue\_GetBlob()

PhonePC/2in1TabletTVWearable

```
1. int OH_PreferencesValue_GetBlob(const OH_PreferencesValue *object, uint8_t **value, uint32_t *count)
```

**描述**

获取[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的二进制值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md) \*object | 指向目标[OH\_PreferencesValue](capi-preferences-oh-preferencesvalue.md)实例的指针。 |
| uint8\_t \*\*value | 指向获取到的二进制值的二级指针。 |
| uint32\_t \*count | 指向获取到的二进制大小的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES\_OK表示操作成功。  若错误码PREFERENCES\_ERROR\_INVALID\_PARAM表示参数不合法。  若错误码PREFERENCES\_ERROR\_STORAGE表示存储异常。  若错误码PREFERENCES\_ERROR\_MALLOC表示内存分配失败。 |
