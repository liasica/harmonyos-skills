---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-cursor-h
title: oh_cursor.h
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 头文件 > oh_cursor.h
category: harmonyos-references
scraped_at: 2026-04-28T07:59:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9f892af50805b0bdaae682c6bb3856f2a19caf125ba6ed14cb3f12c5acdfc1a1
---

## 概述

PhonePC/2in1TabletTVWearable

提供通过查询数据库生成的数据库结果集的访问方法。结果集是指用户调用关系型数据库查询接口之后返回的结果集合，提供了多种灵活的数据访问方式，以便用户获取各项数据。

**引用文件：** <database/rdb/oh\_cursor.h>

**库：** libnative\_rdb\_ndk.z.so

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 10

**相关模块：** [RDB](capi-rdb.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Cursor](capi-rdb-oh-cursor.md) | OH\_Cursor | 提供通过查询数据库生成的数据库结果集的访问方法。结果集是指用户调用关系型数据库查询接口之后返回的结果集合，提供了多种灵活的数据访问方式，以便用户获取各项数据。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int OH\_Cursor\_GetFloatVectorCount(OH\_Cursor \*cursor, int32\_t columnIndex, size\_t \*length)](capi-oh-cursor-h.md#oh_cursor_getfloatvectorcount) | 获取当前行中指定列的浮点数数组大小。 |
| [int OH\_Cursor\_GetFloatVector(OH\_Cursor \*cursor, int32\_t columnIndex, float \*val, size\_t inLen, size\_t \*outLen)](capi-oh-cursor-h.md#oh_cursor_getfloatvector) | 以浮点数数组的形式获取当前行中指定列的值。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Cursor\_GetFloatVectorCount()

PhonePC/2in1TabletTVWearable

```
1. int OH_Cursor_GetFloatVectorCount(OH_Cursor *cursor, int32_t columnIndex, size_t *length)
```

**描述**

获取当前行中指定列的浮点数数组大小。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Cursor](capi-rdb-oh-cursor.md) \*cursor | 表示指向[OH\_Cursor](capi-rdb-oh-cursor.md)实例的指针。 |
| int32\_t columnIndex | 表示结果集中指定列的索引，索引值从0开始。 |
| size\_t \*length | 该参数是输出参数，结果集中指定列的浮点数数组大小会写入该变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  返回RDB\_OK表示成功。  返回RDB\_E\_ERROR表示数据库常见错误。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_SQLITE\_CORRUPT表示数据库损坏。  返回RDB\_E\_STEP\_RESULT\_CLOSED表示查询到的结果集已经关闭。  返回RDB\_E\_ALREADY\_CLOSED表示数据库已经关闭。  返回RDB\_E\_SQLITE\_PERM表示SQLite错误: 访问权限被拒绝。  返回RDB\_E\_SQLITE\_BUSY表示SQLite错误: 数据库文件被锁定。  返回RDB\_E\_SQLITE\_LOCKED表示SQLite错误码：数据库中的表被锁定。  返回RDB\_E\_SQLITE\_NOMEM表示SQLite错误: 数据库内存不足。  返回RDB\_E\_SQLITE\_IOERR表示SQLite错误: 磁盘I/O错误。  返回RDB\_E\_SQLITE\_TOO\_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。  返回RDB\_E\_SQLITE\_MISMATCH表示SQLite错误码：数据类型不匹配。 |

### OH\_Cursor\_GetFloatVector()

PhonePC/2in1TabletTVWearable

```
1. int OH_Cursor_GetFloatVector(OH_Cursor *cursor, int32_t columnIndex, float *val, size_t inLen, size_t *outLen)
```

**描述**

以浮点数数组的形式获取当前行中指定列的值。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Cursor](capi-rdb-oh-cursor.md) \*cursor | 表示指向[OH\_Cursor](capi-rdb-oh-cursor.md)实例的指针。 |
| int32\_t columnIndex | 表示结果集中指定列的索引，索引值从0开始。 |
| float \*val | 该参数是输出参数，结果集中指定列的值会以浮点数数组形式写入该变量，调用者需要申请数组内存。 |
| size\_t inLen | 表示申请的浮点数数组大小。 |
| size\_t \*outLen | 该参数是输出参数，表示实际浮点数数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  返回RDB\_OK表示成功。  返回RDB\_E\_ERROR表示数据库常见错误。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_SQLITE\_CORRUPT表示数据库损坏。  返回RDB\_E\_STEP\_RESULT\_CLOSED表示查询到的结果集已经关闭。  返回RDB\_E\_ALREADY\_CLOSED表示数据库已经关闭。  返回RDB\_E\_SQLITE\_PERM表示SQLite错误: 访问权限被拒绝。  返回RDB\_E\_SQLITE\_BUSY表示SQLite错误: 数据库文件被锁定。  返回RDB\_E\_SQLITE\_LOCKED表示SQLite错误码：数据库中的表被锁定。  返回RDB\_E\_SQLITE\_NOMEM表示SQLite错误: 数据库内存不足。  返回RDB\_E\_SQLITE\_IOERR表示SQLite错误: 磁盘I/O错误。  返回RDB\_E\_SQLITE\_TOO\_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。  返回RDB\_E\_SQLITE\_MISMATCH表示SQLite错误码：数据类型不匹配。 |
