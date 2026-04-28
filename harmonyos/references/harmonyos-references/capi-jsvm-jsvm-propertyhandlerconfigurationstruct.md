---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-propertyhandlerconfigurationstruct
title: JSVM_PropertyHandlerConfigurationStruct
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_PropertyHandlerConfigurationStruct
category: harmonyos-references
scraped_at: 2026-04-28T08:19:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7cb6a53cdf01a0cc9ef0543a701b462062c8e122dc6edb31305110f287f68be4
---

```
1. typedef struct {...} JSVM_PropertyHandlerConfigurationStruct
```

## 概述

PhonePC/2in1TabletWearable

当执行对象的getter、setter、deleter和enumerator操作时，该结构体中对应的函数回调将会触发。

**起始版本：** 12

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

PhonePC/2in1TabletWearable

### 成员变量

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| [JSVM\_Value](capi-jsvm-jsvm-value--8h.md) namedPropertyData | 命名属性回调使用的数据。 |
| [JSVM\_Value](capi-jsvm-jsvm-value--8h.md) indexedPropertyData | 索引属性回调使用的数据。 |

### 成员函数

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| [JSVM\_Value (JSVM\_CDECL\* genericNamedPropertyGetterCallback)(JSVM\_Env env,JSVM\_Value name,JSVM\_Value thisArg,JSVM\_Value namedPropertyData)](capi-jsvm-jsvm-propertyhandlerconfigurationstruct.md#genericnamedpropertygettercallback) | 通过获取实例对象的命名属性而触发的回调函数。 |
| [JSVM\_Value (JSVM\_CDECL\* genericNamedPropertySetterCallback)(JSVM\_Env env,JSVM\_Value name,JSVM\_Value property,JSVM\_Value thisArg,JSVM\_Value namedPropertyData)](capi-jsvm-jsvm-propertyhandlerconfigurationstruct.md#genericnamedpropertysettercallback) | 通过设置实例对象的命名属性而触发的回调函数。 |
| [JSVM\_Value (JSVM\_CDECL\* genericNamedPropertyDeleterCallback)(JSVM\_Env env,JSVM\_Value name,JSVM\_Value thisArg,JSVM\_Value namedPropertyData)](capi-jsvm-jsvm-propertyhandlerconfigurationstruct.md#genericnamedpropertydeletercallback) | 通过删除实例对象的命名属性而触发的回调函数。 |
| [JSVM\_Value (JSVM\_CDECL\* genericNamedPropertyEnumeratorCallback)(JSVM\_Env env,JSVM\_Value thisArg,JSVM\_Value namedPropertyData)](capi-jsvm-jsvm-propertyhandlerconfigurationstruct.md#genericnamedpropertyenumeratorcallback) | 通过获取对象上的所有命名属性而触发的回调函数。 |
| [JSVM\_Value (JSVM\_CDECL\* genericIndexedPropertyGetterCallback)(JSVM\_Env env,JSVM\_Value index,JSVM\_Value thisArg,JSVM\_Value indexedPropertyData)](capi-jsvm-jsvm-propertyhandlerconfigurationstruct.md#genericindexedpropertygettercallback) | 通过获取实例对象的索引属性而触发的回调函数。 |
| [JSVM\_Value (JSVM\_CDECL\* genericIndexedPropertySetterCallback)(JSVM\_Env env,JSVM\_Value index,JSVM\_Value property,JSVM\_Value thisArg,JSVM\_Value indexedPropertyData)](capi-jsvm-jsvm-propertyhandlerconfigurationstruct.md#genericindexedpropertysettercallback) | 通过设置实例对象的索引属性而触发的回调函数。 |
| [JSVM\_Value (JSVM\_CDECL\* genericIndexedPropertyDeleterCallback)(JSVM\_Env env,JSVM\_Value index,JSVM\_Value thisArg,JSVM\_Value indexedPropertyData)](capi-jsvm-jsvm-propertyhandlerconfigurationstruct.md#genericindexedpropertydeletercallback) | 通过删除实例对象的索引属性而触发的回调函数。 |
| [JSVM\_Value (JSVM\_CDECL\* genericIndexedPropertyEnumeratorCallback)(JSVM\_Env env,JSVM\_Value thisArg,JSVM\_Value indexedPropertyData)](capi-jsvm-jsvm-propertyhandlerconfigurationstruct.md#genericindexedpropertyenumeratorcallback) | 通过获取对象上的所有索引属性而触发的回调函数。 |

## 成员函数说明

PhonePC/2in1TabletWearable

### genericNamedPropertyGetterCallback()

PhonePC/2in1TabletWearable

```
1. JSVM_Value (JSVM_CDECL* genericNamedPropertyGetterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```

**描述**

通过获取实例对象的命名属性而触发的回调函数。

### genericNamedPropertySetterCallback()

PhonePC/2in1TabletWearable

```
1. JSVM_Value (JSVM_CDECL* genericNamedPropertySetterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value property,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```

**描述**

通过设置实例对象的命名属性而触发的回调函数。

### genericNamedPropertyDeleterCallback()

PhonePC/2in1TabletWearable

```
1. JSVM_Value (JSVM_CDECL* genericNamedPropertyDeleterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```

**描述**

通过删除实例对象的命名属性而触发的回调函数。

### genericNamedPropertyEnumeratorCallback()

PhonePC/2in1TabletWearable

```
1. JSVM_Value (JSVM_CDECL* genericNamedPropertyEnumeratorCallback)(JSVM_Env env,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```

**描述**

通过获取对象上的所有命名属性而触发的回调函数。

### genericIndexedPropertyGetterCallback()

PhonePC/2in1TabletWearable

```
1. JSVM_Value (JSVM_CDECL* genericIndexedPropertyGetterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```

**描述**

通过获取实例对象的索引属性而触发的回调函数。

### genericIndexedPropertySetterCallback()

PhonePC/2in1TabletWearable

```
1. JSVM_Value (JSVM_CDECL* genericIndexedPropertySetterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value property,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```

**描述**

通过设置实例对象的索引属性而触发的回调函数。

### genericIndexedPropertyDeleterCallback()

PhonePC/2in1TabletWearable

```
1. JSVM_Value (JSVM_CDECL* genericIndexedPropertyDeleterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```

**描述**

通过删除实例对象的索引属性而触发的回调函数。

### genericIndexedPropertyEnumeratorCallback()

PhonePC/2in1TabletWearable

```
1. JSVM_Value (JSVM_CDECL* genericIndexedPropertyEnumeratorCallback)(JSVM_Env env,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```

**描述**

通过获取对象上的所有索引属性而触发的回调函数。
