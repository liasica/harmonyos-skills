---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-propertyhandlerconfigurationstruct
title: JSVM_PropertyHandlerConfigurationStruct
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_PropertyHandlerConfigurationStruct
category: harmonyos-references
scraped_at: 2026-09-02T15:03:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:aba436650e6eb45d299e9989de5dac9a572b097156e5e78d27a8badce68ba7e6
---

```c
typedef struct {...} JSVM_PropertyHandlerConfigurationStruct
```

## 概述

当执行对象的getter、setter、deleter和enumerator操作时，该结构体中对应的函数回调将会触发。

**使用场景：** 需要拦截和处理JavaScript对象属性操作的场景，实现动态属性访问控制，构建代理对象或属性监听机制。

**解决的问题：** 提供了一种机制来拦截和自定义对象的属性操作行为，允许在属性读写删除等操作时执行自定义逻辑。

**收益：** 增强对象操作的灵活性和可控性，简化属性拦截的实现逻辑。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 12

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [JSVM\_Value](capi-jsvm-jsvm-value--8h.md) namedPropertyData | 命名属性回调使用的数据。 |
| [JSVM\_Value](capi-jsvm-jsvm-value--8h.md) indexedPropertyData | 索引属性回调使用的数据。 |

### 回调函数成员

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

## 回调函数成员说明

### genericNamedPropertyGetterCallback()

```c
JSVM_Value (JSVM_CDECL* genericNamedPropertyGetterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```

**描述**

通过获取实例对象的命名属性而触发的回调函数。

### genericNamedPropertySetterCallback()

```c
JSVM_Value (JSVM_CDECL* genericNamedPropertySetterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value property,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```

**描述**

通过设置实例对象的命名属性而触发的回调函数。

### genericNamedPropertyDeleterCallback()

```c
JSVM_Value (JSVM_CDECL* genericNamedPropertyDeleterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```

**描述**

通过删除实例对象的命名属性而触发的回调函数。

### genericNamedPropertyEnumeratorCallback()

```c
JSVM_Value (JSVM_CDECL* genericNamedPropertyEnumeratorCallback)(JSVM_Env env,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```

**描述**

通过获取对象上的所有命名属性而触发的回调函数。

### genericIndexedPropertyGetterCallback()

```c
JSVM_Value (JSVM_CDECL* genericIndexedPropertyGetterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```

**描述**

通过获取实例对象的索引属性而触发的回调函数。

### genericIndexedPropertySetterCallback()

```c
JSVM_Value (JSVM_CDECL* genericIndexedPropertySetterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value property,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```

**描述**

通过设置实例对象的索引属性而触发的回调函数。

### genericIndexedPropertyDeleterCallback()

```c
JSVM_Value (JSVM_CDECL* genericIndexedPropertyDeleterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```

**描述**

通过删除实例对象的索引属性而触发的回调函数。

### genericIndexedPropertyEnumeratorCallback()

```c
JSVM_Value (JSVM_CDECL* genericIndexedPropertyEnumeratorCallback)(JSVM_Env env,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```

**描述**

通过获取对象上的所有索引属性而触发的回调函数。
