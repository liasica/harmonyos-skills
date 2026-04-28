---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-rdb-types-h
title: oh_rdb_types.h
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 头文件 > oh_rdb_types.h
category: harmonyos-references
scraped_at: 2026-04-28T07:59:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6eeba2499b1fc2c0ea05c73f4fd505e62a39ac5223c6800733b7f683af1f40aa
---

## 概述

PhonePC/2in1TabletTVWearable

提供与数据值相关的类型定义。

**引用文件：** <database/rdb/oh\_rdb\_types.h>

**库：** libnative\_rdb\_ndk.z.so

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 18

**相关模块：** [RDB](capi-rdb.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md) | OH\_RDB\_ReturningContext | returning相关接口的上下文。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Rdb\_ConflictResolution](capi-oh-rdb-types-h.md#rdb_conflictresolution) | Rdb\_ConflictResolution | 表示冲突解决策略的枚举。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_RDB\_ReturningContext \*OH\_RDB\_CreateReturningContext(void)](capi-oh-rdb-types-h.md#oh_rdb_createreturningcontext) | 创建[OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md)的实例对象。 |
| [void OH\_RDB\_DestroyReturningContext(OH\_RDB\_ReturningContext \*context)](capi-oh-rdb-types-h.md#oh_rdb_destroyreturningcontext) | 销毁[OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md)实例对象。 |
| [int OH\_RDB\_SetReturningFields(OH\_RDB\_ReturningContext \*context, const char \*const fields[], int32\_t len)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-rdb-types-h#oh_rdb_setreturningfields) | 设置结果集中返回的字段。 |
| [int OH\_RDB\_SetMaxReturningCount(OH\_RDB\_ReturningContext \*context, int32\_t count)](capi-oh-rdb-types-h.md#oh_rdb_setmaxreturningcount) | 设置返回结果集的最大行数量。 |
| [OH\_Cursor \*OH\_RDB\_GetReturningValues(OH\_RDB\_ReturningContext \*context)](capi-oh-rdb-types-h.md#oh_rdb_getreturningvalues) | 获取数据变化的游标，默认包含1024条。 |
| [int64\_t OH\_RDB\_GetChangedCount(OH\_RDB\_ReturningContext \*context)](capi-oh-rdb-types-h.md#oh_rdb_getchangedcount) | 获取受此操作影响的数据行的数量。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### Rdb\_ConflictResolution

PhonePC/2in1TabletTVWearable

```
1. enum Rdb_ConflictResolution
```

**描述**

表示冲突解决策略的枚举。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| RDB\_CONFLICT\_NONE = 1 | 发生冲突时不执行任何操作。 |
| RDB\_CONFLICT\_ROLLBACK | 发生冲突时抛错误码，同时回滚本次事务。 |
| RDB\_CONFLICT\_ABORT | 发生冲突时抛错误码，同时回滚本次修改。 |
| RDB\_CONFLICT\_FAIL | 发生冲突时抛错误码，不回滚冲突前的修改同时终止本次修改。 |
| RDB\_CONFLICT\_IGNORE | 发生冲突时忽略冲突的数据，继续执行后续修改。 |
| RDB\_CONFLICT\_REPLACE | 发生冲突时，尝试删除后插入，如果还是冲突则等同于RDB\_CONFLICT\_ABORT。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_RDB\_CreateReturningContext()

PhonePC/2in1TabletTVWearable

```
1. OH_RDB_ReturningContext *OH_RDB_CreateReturningContext(void)
```

**描述**

创建[OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md)的实例对象。

**起始版本：** 23

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_RDB\_ReturningContext \*](capi-rdb-oh-rdb-returningcontext.md) | 执行成功时返回指向[OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md)实例的指针。  否则返回nullptr。使用完成后必须通过[OH\_RDB\_DestroyReturningContext](capi-oh-rdb-types-h.md#oh_rdb_destroyreturningcontext)接口释放内存。 |

### OH\_RDB\_DestroyReturningContext()

PhonePC/2in1TabletTVWearable

```
1. void OH_RDB_DestroyReturningContext(OH_RDB_ReturningContext *context)
```

**描述**

销毁[OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md)实例对象。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md) \*context | 指向[OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md)实例的指针。 |

### OH\_RDB\_SetReturningFields()

PhonePC/2in1TabletTVWearable

```
1. int OH_RDB_SetReturningFields(OH_RDB_ReturningContext *context, const char *const fields[], int32_t len)
```

**描述**

设置结果集中返回的字段。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md) \*context | 指向[OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md)实例的指针。 |
| const char \*const fields[] | 要返回的列名。 |
| int32\_t len | 字段长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  执行成功返回RDB\_OK。  输入参数无效返回RDB\_E\_INVALID\_ARGS。 |

### OH\_RDB\_SetMaxReturningCount()

PhonePC/2in1TabletTVWearable

```
1. int OH_RDB_SetMaxReturningCount(OH_RDB_ReturningContext *context, int32_t count)
```

**描述**

设置返回结果集的最大行数量。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md) \*context | 指向[OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md)实例的指针。 |
| int32\_t count | 表示返回结果集的最大条目数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  执行成功返回RDB\_OK。  输入参数无效返回RDB\_E\_INVALID\_ARGS。 |

### OH\_RDB\_GetReturningValues()

PhonePC/2in1TabletTVWearable

```
1. OH_Cursor *OH_RDB_GetReturningValues(OH_RDB_ReturningContext *context)
```

**描述**

获取数据变化的游标，默认包含1024条。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md) \*context | 指向[OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_Cursor \* | 返回指向[OH\_Cursor](capi-rdb-oh-cursor.md)结构体实例的指针。  如果获取游标失败，则返回nullptr。使用[OH\_RDB\_DestroyReturningContext](capi-oh-rdb-types-h.md#oh_rdb_destroyreturningcontext)接口释放内存时会销毁游标，无需单独释放。 |

### OH\_RDB\_GetChangedCount()

PhonePC/2in1TabletTVWearable

```
1. int64_t OH_RDB_GetChangedCount(OH_RDB_ReturningContext *context)
```

**描述**

获取受此操作影响的数据行的数量。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md) \*context | 指向[OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int64\_t | 返回已更改的条目数，如果获取变更失败则返回-1。 |
