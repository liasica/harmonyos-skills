---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-rdb-transaction-h
title: oh_rdb_transaction.h
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 头文件 > oh_rdb_transaction.h
category: harmonyos-references
scraped_at: 2026-04-28T07:59:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4c046d9f432c6ba74188e2acd09490b28addf8e12b13ba522e6ebdc10bc7beac
---

## 概述

PhonePC/2in1TabletTVWearable

提供与数据库事务相关的函数和枚举。

**引用文件：** <database/rdb/oh\_rdb\_transaction.h>

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
| [OH\_RDB\_TransOptions](capi-rdb-oh-rdb-transoptions.md) | OH\_RDB\_TransOptions | 定义[OH\_RDB\_TransOptions](capi-rdb-oh-rdb-transoptions.md)结构类型。 |
| [OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md) | OH\_Rdb\_Transaction | 定义[OH\_RDB\_TransOptions](capi-rdb-oh-rdb-transoptions.md)结构类型。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_RDB\_TransType](capi-oh-rdb-transaction-h.md#oh_rdb_transtype) | OH\_RDB\_TransType | 表示关系型数据库事务类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_RDB\_TransOptions \*OH\_RdbTrans\_CreateOptions(void)](capi-oh-rdb-transaction-h.md#oh_rdbtrans_createoptions) | 创建事务配置对象。 |
| [int OH\_RdbTrans\_DestroyOptions(OH\_RDB\_TransOptions \*options)](capi-oh-rdb-transaction-h.md#oh_rdbtrans_destroyoptions) | 销毁事务配置对象。 |
| [int OH\_RdbTransOption\_SetType(OH\_RDB\_TransOptions \*options, OH\_RDB\_TransType type)](capi-oh-rdb-transaction-h.md#oh_rdbtransoption_settype) | 设置关系型数据库事务类型。 |
| [int OH\_RdbTrans\_Commit(OH\_Rdb\_Transaction \*trans)](capi-oh-rdb-transaction-h.md#oh_rdbtrans_commit) | 提交事务。 |
| [int OH\_RdbTrans\_Rollback(OH\_Rdb\_Transaction \*trans)](capi-oh-rdb-transaction-h.md#oh_rdbtrans_rollback) | 回滚事务。 |
| [int OH\_RdbTrans\_Insert(OH\_Rdb\_Transaction \*trans, const char \*table, const OH\_VBucket \*row, int64\_t \*rowId)](capi-oh-rdb-transaction-h.md#oh_rdbtrans_insert) | 将一行数据插入到目标表中。 |
| [int OH\_RdbTrans\_InsertWithConflictResolution(OH\_Rdb\_Transaction \*trans, const char \*table, const OH\_VBucket \*row,Rdb\_ConflictResolution resolution, int64\_t \*rowId)](capi-oh-rdb-transaction-h.md#oh_rdbtrans_insertwithconflictresolution) | 将一行数据插入到目标表中，支持冲突解决。 |
| [int OH\_RdbTrans\_BatchInsert(OH\_Rdb\_Transaction \*trans, const char \*table, const OH\_Data\_VBuckets \*rows,Rdb\_ConflictResolution resolution, int64\_t \*changes)](capi-oh-rdb-transaction-h.md#oh_rdbtrans_batchinsert) | 将一组数据批量插入到目标表中。 |
| [int OH\_RdbTrans\_Update(OH\_Rdb\_Transaction \*trans, const OH\_VBucket \*row, const OH\_Predicates \*predicates,int64\_t \*changes)](capi-oh-rdb-transaction-h.md#oh_rdbtrans_update) | 根据指定的条件更新数据库中的数据。 |
| [int OH\_RdbTrans\_UpdateWithConflictResolution(OH\_Rdb\_Transaction \*trans, const OH\_VBucket \*row,const OH\_Predicates \*predicates, Rdb\_ConflictResolution resolution, int64\_t \*changes)](capi-oh-rdb-transaction-h.md#oh_rdbtrans_updatewithconflictresolution) | 根据指定条件更新数据库中的数据，并支持冲突解决。 |
| [int OH\_RdbTrans\_Delete(OH\_Rdb\_Transaction \*trans, const OH\_Predicates \*predicates, int64\_t \*changes)](capi-oh-rdb-transaction-h.md#oh_rdbtrans_delete) | 根据指定条件从数据库中删除数据。 |
| [OH\_Cursor \*OH\_RdbTrans\_Query(OH\_Rdb\_Transaction \*trans, const OH\_Predicates \*predicates, const char \*columns[],int len)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-rdb-transaction-h#oh_rdbtrans_query) | 根据指定的条件查询数据库中的数据。 |
| [OH\_Cursor \*OH\_RdbTrans\_QuerySql(OH\_Rdb\_Transaction \*trans, const char \*sql, const OH\_Data\_Values \*args)](capi-oh-rdb-transaction-h.md#oh_rdbtrans_querysql) | 根据SQL语句查询数据库中的数据。 |
| [int OH\_RdbTrans\_Execute(OH\_Rdb\_Transaction \*trans, const char \*sql, const OH\_Data\_Values \*args, OH\_Data\_Value \*\*result)](capi-oh-rdb-transaction-h.md#oh_rdbtrans_execute) | 执行包含指定参数的SQL语句。 |
| [int OH\_RdbTrans\_Destroy(OH\_Rdb\_Transaction \*trans)](capi-oh-rdb-transaction-h.md#oh_rdbtrans_destroy) | 销毁事务对象。 |
| [OH\_Cursor \*OH\_RdbTrans\_QueryWithoutRowCount(OH\_Rdb\_Transaction \*trans, const OH\_Predicates \*predicates, const char \* const columns[], int len)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-rdb-transaction-h#oh_rdbtrans_querywithoutrowcount) | 根据指定的条件查询数据库中的数据，不计算行数。 |
| [OH\_Cursor \*OH\_RdbTrans\_QuerySqlWithoutRowCount(OH\_Rdb\_Transaction \*trans, const char \*sql, const OH\_Data\_Values \*args)](capi-oh-rdb-transaction-h.md#oh_rdbtrans_querysqlwithoutrowcount) | 根据SQL语句查询数据库中的数据，不计算行数。 |
| [int OH\_RdbTrans\_BatchInsertWithReturning(OH\_Rdb\_Transaction \*trans, const char \*table, const OH\_Data\_VBuckets \*rows, Rdb\_ConflictResolution resolution, OH\_RDB\_ReturningContext \*context)](capi-oh-rdb-transaction-h.md#oh_rdbtrans_batchinsertwithreturning) | 将批量数据插入目标表，并将变更信息输出到上下文中。 |
| [int OH\_RdbTrans\_UpdateWithReturning(OH\_Rdb\_Transaction \*trans, OH\_VBucket \*row, OH\_Predicates \*predicates, Rdb\_ConflictResolution resolution, OH\_RDB\_ReturningContext \*context)](capi-oh-rdb-transaction-h.md#oh_rdbtrans_updatewithreturning) | 根据指定条件更新数据库中的数据并输出更改信息到上下文。 |
| [int OH\_RdbTrans\_DeleteWithReturning(OH\_Rdb\_Transaction \*trans, OH\_Predicates \*predicates, OH\_RDB\_ReturningContext \*context)](capi-oh-rdb-transaction-h.md#oh_rdbtrans_deletewithreturning) | 根据指定条件从数据库中删除数据并输出更改信息到上下文。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_RDB\_TransType

PhonePC/2in1TabletTVWearable

```
1. enum OH_RDB_TransType
```

**描述**

表示关系型数据库事务类型。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| RDB\_TRANS\_DEFERRED = 0 | 在首次访问数据库之前，事务默认设置不会启动。 |
| RDB\_TRANS\_IMMEDIATE | 数据库连接立即开始新的写入，而无需等待写入语句。 |
| RDB\_TRANS\_EXCLUSIVE | 与RDB\_TRANS\_IMMEDIATE类型相似，写事务会立即启动。  RDB\_TRANS\_EXCLUSIVE和RDB\_TRANS\_IMMEDIATE类型在WAL模式下相同，但在其他日志模式下，RDB\_TRANS\_EXCLUSIVE会阻止其他数据库连接在事务进行时读取数据库。 |
| RDB\_TRANS\_BUTT | RDB事务类型的最大值。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_RdbTrans\_CreateOptions()

PhonePC/2in1TabletTVWearable

```
1. OH_RDB_TransOptions *OH_RdbTrans_CreateOptions(void)
```

**描述**

创建事务配置对象。

**起始版本：** 18

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_RDB\_TransOptions](capi-rdb-oh-rdb-transoptions.md) | 执行成功时返回指向[OH\_RDB\_TransOptions](capi-rdb-oh-rdb-transoptions.md)实例的指针。否则返回nullptr。  使用完成后，必须通过[OH\_RdbTrans\_DestroyOptions](capi-oh-rdb-transaction-h.md#oh_rdbtrans_destroyoptions)接口释放内存。 |

### OH\_RdbTrans\_DestroyOptions()

PhonePC/2in1TabletTVWearable

```
1. int OH_RdbTrans_DestroyOptions(OH_RDB_TransOptions *options)
```

**描述**

销毁事务配置对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_RDB\_TransOptions](capi-rdb-oh-rdb-transoptions.md) \*options | 指向[OH\_RDB\_TransOptions](capi-rdb-oh-rdb-transoptions.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_RdbTransOption\_SetType()

PhonePC/2in1TabletTVWearable

```
1. int OH_RdbTransOption_SetType(OH_RDB_TransOptions *options, OH_RDB_TransType type)
```

**描述**

设置关系型数据库事务类型。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_RDB\_TransOptions](capi-rdb-oh-rdb-transoptions.md) \*options | 指向[OH\_RDB\_TransOptions](capi-rdb-oh-rdb-transoptions.md)实例的指针。 |
| [OH\_RDB\_TransType](capi-oh-rdb-transaction-h.md#oh_rdb_transtype) type | 表示关系型数据库事务类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_RdbTrans\_Commit()

PhonePC/2in1TabletTVWearable

```
1. int OH_RdbTrans_Commit(OH_Rdb_Transaction *trans)
```

**描述**

提交事务。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md) \*trans | 指向[OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  返回RDB\_OK表示成功。  返回RDB\_E\_ERROR表示数据库常见错误。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_ALREADY\_CLOSED表示数据库已经关闭。  返回RDB\_E\_SQLITE\_FULL表示SQLite错误码：数据库已满。  返回RDB\_E\_SQLITE\_CORRUPT表示数据库损坏。  返回RDB\_E\_SQLITE\_PERM表示SQLite错误码：访问权限被拒绝。  返回RDB\_E\_SQLITE\_BUSY表示SQLite错误码：数据库文件被锁定。  返回RDB\_E\_SQLITE\_NOMEM表示SQLite错误码：数据库内存不足。  返回RDB\_E\_SQLITE\_READONLY表示SQLite错误码：尝试写入只读数据库。  返回RDB\_E\_SQLITE\_IOERR表示SQLite错误码：磁盘I/O错误。 |

### OH\_RdbTrans\_Rollback()

PhonePC/2in1TabletTVWearable

```
1. int OH_RdbTrans_Rollback(OH_Rdb_Transaction *trans)
```

**描述**

回滚事务。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md) \*trans | 指向[OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  返回RDB\_OK表示成功。  返回RDB\_E\_ERROR表示数据库常见错误。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_ALREADY\_CLOSED表示数据库已经关闭。  返回RDB\_E\_SQLITE\_FULL表示SQLite错误码：数据库已满。  返回RDB\_E\_SQLITE\_CORRUPT表示数据库损坏。  返回RDB\_E\_SQLITE\_PERM表示SQLite错误码：访问权限被拒绝。  返回RDB\_E\_SQLITE\_BUSY表示SQLite错误码：数据库文件被锁定。  返回RDB\_E\_SQLITE\_NOMEM表示SQLite错误码：数据库内存不足。  返回RDB\_E\_SQLITE\_READONLY表示SQLite错误码：尝试写入只读数据库。  返回RDB\_E\_SQLITE\_IOERR表示SQLite错误码：磁盘I/O错误。 |

### OH\_RdbTrans\_Insert()

PhonePC/2in1TabletTVWearable

```
1. int OH_RdbTrans_Insert(OH_Rdb_Transaction *trans, const char *table, const OH_VBucket *row, int64_t *rowId)
```

**描述**

将一行数据插入到目标表中。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md) \*trans | 指向[OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md)实例的指针。 |
| const char \*table | 要插入的目标表名。 |
| const [OH\_VBucket](capi-rdb-oh-vbucket.md) \*row | 要插入到表中的数据行。 |
| int64\_t \*rowId | 输出参数，表示插入后返回的行号。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  返回RDB\_OK表示成功。  返回RDB\_E\_ERROR表示数据库常见错误。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_ALREADY\_CLOSED表示数据库已经关闭。  返回RDB\_E\_WAL\_SIZE\_OVER\_LIMIT表示WAL日志文件大小超过默认值。  返回RDB\_E\_SQLITE\_FULL表示SQLite错误码：数据库已满。  返回RDB\_E\_SQLITE\_CORRUPT表示数据库损坏。  返回RDB\_E\_SQLITE\_PERM表示SQLite错误码：访问权限被拒绝。  返回RDB\_E\_SQLITE\_BUSY表示SQLite错误码：数据库文件被锁定。  返回RDB\_E\_SQLITE\_LOCKED表示SQLite错误码：数据库中的表被锁定。  返回RDB\_E\_SQLITE\_NOMEM表示SQLite错误码：数据库内存不足。  返回RDB\_E\_SQLITE\_READONLY表示SQLite错误码：尝试写入只读数据库。  返回RDB\_E\_SQLITE\_IOERR表示SQLite错误码：磁盘I/O错误。  返回RDB\_E\_SQLITE\_TOO\_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。  返回RDB\_E\_SQLITE\_MISMATCH表示SQLite错误码：数据类型不匹配。 |

### OH\_RdbTrans\_InsertWithConflictResolution()

PhonePC/2in1TabletTVWearable

```
1. int OH_RdbTrans_InsertWithConflictResolution(OH_Rdb_Transaction *trans, const char *table, const OH_VBucket *row,Rdb_ConflictResolution resolution, int64_t *rowId)
```

**描述**

将一行数据插入到目标表中，支持冲突解决。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md) \*trans | 指向[OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md)实例的指针。 |
| const char \*table | 要插入的目标表名。 |
| const [OH\_VBucket](capi-rdb-oh-vbucket.md) \*row | 表示要插入到表中的数据。 |
| [Rdb\_ConflictResolution](capi-oh-rdb-types-h.md#rdb_conflictresolution) resolution | 表示发生冲突时的解决策略。 |
| int64\_t \*rowId | 输出参数，表示插入成功后返回的行号。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  返回RDB\_OK表示成功。  返回RDB\_E\_ERROR表示数据库常见错误。  返回RDB\_E\_INVALID\_ARGS表示输入参数无效。  返回RDB\_E\_ALREADY\_CLOSED表示数据库已关闭。  返回RDB\_E\_WAL\_SIZE\_OVER\_LIMIT表示WAL日志文件大小超过默认值。  返回RDB\_E\_SQLITE\_FULL表示SQLite错误码：数据库已满。  返回RDB\_E\_SQLITE\_CORRUPT表示数据库损坏。  返回RDB\_E\_SQLITE\_PERM表示SQLite错误码：访问权限被拒绝。  返回RDB\_E\_SQLITE\_BUSY表示SQLite错误码：数据库文件被锁定。  返回RDB\_E\_SQLITE\_LOCKED表示SQLite错误码：数据库中的表被锁定。  返回RDB\_E\_SQLITE\_NOMEM表示SQLite错误码：数据库内存不足。  返回RDB\_E\_SQLITE\_READONLY表示SQLite错误码：尝试写入只读数据库。  返回RDB\_E\_SQLITE\_IOERR表示SQLite错误码：磁盘I/O错误。  返回RDB\_E\_SQLITE\_TOO\_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。  返回RDB\_E\_SQLITE\_MISMATCH表示SQLite错误码：数据类型不匹配。  返回RDB\_E\_SQLITE\_CONSTRAINT表示SQLite错误码：违反约束导致操作中止。 |

### OH\_RdbTrans\_BatchInsert()

PhonePC/2in1TabletTVWearable

```
1. int OH_RdbTrans_BatchInsert(OH_Rdb_Transaction *trans, const char *table, const OH_Data_VBuckets *rows, Rdb_ConflictResolution resolution, int64_t *changes)
```

**描述**

将一组数据批量插入到目标表中。

单次插入参数的最大数量限制为32766，超出上限会返回RDB\_E\_INVALID\_ARGS错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276\*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md) \*trans | 指向[OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md)实例的指针。 |
| const char \*table | 要插入的目标表名。 |
| const [OH\_Data\_VBuckets](capi-rdb-oh-data-vbuckets.md) \*rows | 表示要插入到表中的一组数据。 |
| [Rdb\_ConflictResolution](capi-oh-rdb-types-h.md#rdb_conflictresolution) resolution | 表示发生冲突时的解决策略。 |
| int64\_t \*changes | 输出参数，表示插入成功的次数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  返回RDB\_OK表示成功。  返回RDB\_E\_ERROR表示数据库常见错误。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_ALREADY\_CLOSED表示数据库已经关闭。  返回RDB\_E\_WAL\_SIZE\_OVER\_LIMIT表示WAL日志文件大小超过默认值。  返回RDB\_E\_SQLITE\_FULL表示SQLite错误码：数据库已满。  返回RDB\_E\_SQLITE\_CORRUPT表示数据库损坏。  返回RDB\_E\_SQLITE\_PERM表示SQLite错误码：访问权限被拒绝。  返回RDB\_E\_SQLITE\_BUSY表示SQLite错误码：数据库文件被锁定。  返回RDB\_E\_SQLITE\_LOCKED表示SQLite错误码：数据库中的表被锁定。  返回RDB\_E\_SQLITE\_NOMEM表示SQLite错误码：数据库内存不足。  返回RDB\_E\_SQLITE\_READONLY表示SQLite错误码：尝试写入只读数据库。  返回RDB\_E\_SQLITE\_IOERR表示SQLite错误码：磁盘I/O错误。  返回RDB\_E\_SQLITE\_TOO\_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。  返回RDB\_E\_SQLITE\_MISMATCH表示SQLite错误码：数据类型不匹配。  返回RDB\_E\_SQLITE\_CONSTRAINT表示SQLite错误码：SQLite约束。 |

### OH\_RdbTrans\_Update()

PhonePC/2in1TabletTVWearable

```
1. int OH_RdbTrans_Update(OH_Rdb_Transaction *trans, const OH_VBucket *row, const OH_Predicates *predicates, int64_t *changes)
```

**描述**

根据指定的条件更新数据库中的数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md) \*trans | 指向[OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md)实例的指针。 |
| const [OH\_VBucket](capi-rdb-oh-vbucket.md) \*row | 表示要更新到表中的数据行。 |
| const [OH\_Predicates](capi-rdb-oh-predicates.md) \*predicates | 表示[OH\_Predicates](capi-rdb-oh-predicates.md)指定的更新条件。 |
| int64\_t \*changes | 输出参数，表示更新成功的次数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  返回RDB\_OK表示成功。  返回RDB\_E\_ERROR表示数据库常见错误。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_ALREADY\_CLOSED表示数据库已经关闭。  返回RDB\_E\_WAL\_SIZE\_OVER\_LIMIT表示WAL日志文件大小超过默认值。  返回RDB\_E\_SQLITE\_FULL表示SQLite错误码：数据库已满。  返回RDB\_E\_SQLITE\_CORRUPT表示数据库损坏。  返回RDB\_E\_SQLITE\_PERM表示SQLite错误码：访问权限被拒绝。  返回RDB\_E\_SQLITE\_BUSY表示SQLite错误码：数据库文件被锁定。  返回RDB\_E\_SQLITE\_LOCKED表示SQLite错误码：数据库中的表被锁定。  返回RDB\_E\_SQLITE\_NOMEM表示SQLite错误码：数据库内存不足。  返回RDB\_E\_SQLITE\_READONLY表示SQLite错误码：尝试写入只读数据库。  返回RDB\_E\_SQLITE\_IOERR表示SQLite错误码：磁盘I/O错误。  返回RDB\_E\_SQLITE\_TOO\_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。  返回RDB\_E\_SQLITE\_MISMATCH表示SQLite错误码：数据类型不匹配。 |

### OH\_RdbTrans\_UpdateWithConflictResolution()

PhonePC/2in1TabletTVWearable

```
1. int OH_RdbTrans_UpdateWithConflictResolution(OH_Rdb_Transaction *trans, const OH_VBucket *row,const OH_Predicates *predicates, Rdb_ConflictResolution resolution, int64_t *changes)
```

**描述**

根据指定条件更新数据库中的数据，并支持冲突解决。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md) \*trans | 指向[OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md)实例的指针。 |
| const [OH\_VBucket](capi-rdb-oh-vbucket.md) \*row | 表示要更新到表中的数据。 |
| const [OH\_Predicates](capi-rdb-oh-predicates.md) \*predicates | 表示[OH\_Predicates](capi-rdb-oh-predicates.md)指定的更新条件。 |
| [Rdb\_ConflictResolution](capi-oh-rdb-types-h.md#rdb_conflictresolution) resolution | 表示发生冲突时的解决策略。 |
| int64\_t \*changes | 输出参数，表示更新成功的行数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  返回RDB\_OK表示成功。  返回RDB\_E\_ERROR表示数据库常见错误。  返回RDB\_E\_INVALID\_ARGS表示输入参数无效。  返回RDB\_E\_ALREADY\_CLOSED表示数据库已关闭。  返回RDB\_E\_WAL\_SIZE\_OVER\_LIMIT表示WAL日志文件大小超过默认值。  返回RDB\_E\_SQLITE\_FULL表示SQLite错误码：数据库已满。  返回RDB\_E\_SQLITE\_CORRUPT表示数据库损坏。  返回RDB\_E\_SQLITE\_PERM表示SQLite错误码：访问权限被拒绝。  返回RDB\_E\_SQLITE\_BUSY表示SQLite错误码：数据库文件被锁定。  返回RDB\_E\_SQLITE\_LOCKED表示SQLite错误码：数据库中的表被锁定。  返回RDB\_E\_SQLITE\_NOMEM表示SQLite错误码：数据库内存不足。  返回RDB\_E\_SQLITE\_READONLY表示SQLite错误码：尝试写入只读数据库。  返回RDB\_E\_SQLITE\_IOERR表示SQLite错误码：磁盘I/O错误。  返回RDB\_E\_SQLITE\_TOO\_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。  返回RDB\_E\_SQLITE\_MISMATCH表示SQLite错误码：数据类型不匹配。  返回RDB\_E\_SQLITE\_CONSTRAINT表示SQLite错误码：违反约束导致操作中止。 |

### OH\_RdbTrans\_Delete()

PhonePC/2in1TabletTVWearable

```
1. int OH_RdbTrans_Delete(OH_Rdb_Transaction *trans, const OH_Predicates *predicates, int64_t *changes)
```

**描述**

根据指定条件从数据库中删除数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md) \*trans | 指向[OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md)实例的指针。 |
| const [OH\_Predicates](capi-rdb-oh-predicates.md) \*predicates | 表示[OH\_Predicates](capi-rdb-oh-predicates.md)指定的删除条件。 |
| int64\_t \*changes | 表示删除成功的次数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  返回RDB\_OK表示成功。  返回RDB\_E\_ERROR表示数据库常见错误。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_ALREADY\_CLOSED表示数据库已经关闭。  返回RDB\_E\_WAL\_SIZE\_OVER\_LIMIT表示WAL日志文件大小超过默认值。  返回RDB\_E\_SQLITE\_FULL表示SQLite错误码：数据库已满。  返回RDB\_E\_SQLITE\_CORRUPT表示数据库损坏。  返回RDB\_E\_SQLITE\_PERM表示SQLite错误码：访问权限被拒绝。  返回RDB\_E\_SQLITE\_BUSY表示SQLite错误码：数据库文件被锁定。  返回RDB\_E\_SQLITE\_LOCKED表示SQLite错误码：数据库中的表被锁定。  返回RDB\_E\_SQLITE\_NOMEM表示SQLite错误码：数据库内存不足。  返回RDB\_E\_SQLITE\_READONLY表示SQLite错误码：尝试写入只读数据库。  返回RDB\_E\_SQLITE\_IOERR表示SQLite错误码：磁盘I/O错误。  返回RDB\_E\_SQLITE\_TOO\_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。  返回RDB\_E\_SQLITE\_MISMATCH表示SQLite错误码：数据类型不匹配。 |

### OH\_RdbTrans\_Query()

PhonePC/2in1TabletTVWearable

```
1. OH_Cursor *OH_RdbTrans_Query(OH_Rdb_Transaction *trans, const OH_Predicates *predicates, const char *columns[], int len)
```

**描述**

根据指定的条件查询数据库中的数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md) \*trans | 指向[OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md)实例的指针。 |
| const [OH\_Predicates](capi-rdb-oh-predicates.md) \*predicates | 表示[OH\_Predicates](capi-rdb-oh-predicates.md)指定的查询条件。 |
| const char \*columns[] | 表示要查询的列，如果传入空值，则查询适用于所有列。 |
| int len | 表示列中元素的个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Cursor](capi-rdb-oh-cursor.md) | 如果执行成功，则返回指向[OH\_Cursor](capi-rdb-oh-cursor.md)实例的指针。如果数据库已关闭或数据库没有响应，则返回空。 |

### OH\_RdbTrans\_QuerySql()

PhonePC/2in1TabletTVWearable

```
1. OH_Cursor *OH_RdbTrans_QuerySql(OH_Rdb_Transaction *trans, const char *sql, const OH_Data_Values *args)
```

**描述**

根据SQL语句查询数据库中的数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md) \*trans | 指向[OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md)实例的指针。 |
| const char \*sql | 表示要执行的SQL语句。 |
| const [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*args | 指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Cursor](capi-rdb-oh-cursor.md) | 如果执行成功，则返回指向[OH\_Cursor](capi-rdb-oh-cursor.md)实例的指针。如果数据库已关闭或数据库没有响应，则返回空。 |

### OH\_RdbTrans\_Execute()

PhonePC/2in1TabletTVWearable

```
1. int OH_RdbTrans_Execute(OH_Rdb_Transaction *trans, const char *sql, const OH_Data_Values *args, OH_Data_Value **result)
```

**描述**

执行包含指定参数的SQL语句。

不支持开头包含注释的语句。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md) \*trans | 指向[OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md)实例的指针。 |
| const char \*sql | 表示要执行的SQL语句。 |
| const [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*args | SQL语句中包含的参数。 |
| OH\_Data\_Value \*\*result | 执行成功时指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。使用完成后，必须通过[OH\_Value\_Destroy](capi-oh-data-value-h.md#oh_value_destroy)接口释放内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  返回RDB\_OK表示成功。  返回RDB\_E\_ERROR表示数据库常见错误。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_ALREADY\_CLOSED表示数据库已经关闭。  返回RDB\_E\_WAL\_SIZE\_OVER\_LIMIT表示WAL日志文件大小超过默认值。  返回RDB\_E\_SQLITE\_FULL表示SQLite错误码：数据库已满。  返回RDB\_E\_SQLITE\_CORRUPT表示数据库损坏。  返回RDB\_E\_SQLITE\_PERM表示SQLite错误码：访问权限被拒绝。  返回RDB\_E\_SQLITE\_BUSY表示SQLite错误码：数据库文件被锁定。  返回RDB\_E\_SQLITE\_LOCKED表示SQLite错误码：数据库中的表被锁定。  返回RDB\_E\_SQLITE\_NOMEM表示SQLite错误码：数据库内存不足。  返回RDB\_E\_SQLITE\_READONLY表示SQLite错误码：尝试写入只读数据库。  返回RDB\_E\_SQLITE\_IOERR表示SQLite错误码：磁盘I/O错误。  返回RDB\_E\_SQLITE\_TOO\_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。  返回RDB\_E\_SQLITE\_MISMATCH表示SQLite错误码：数据类型不匹配。 |

### OH\_RdbTrans\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. int OH_RdbTrans_Destroy(OH_Rdb_Transaction *trans)
```

**描述**

销毁事务对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md) \*trans | 指向[OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_RdbTrans\_QueryWithoutRowCount()

PhonePC/2in1TabletTVWearable

```
1. OH_Cursor *OH_RdbTrans_QueryWithoutRowCount(OH_Rdb_Transaction *trans, const OH_Predicates *predicates, const char * const columns[], int len)
```

**描述**

根据指定的条件查询数据库中的数据，不计算行数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md) \*trans | 指向[OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md)实例的指针。 |
| [const OH\_Predicates](capi-rdb-oh-predicates.md) \*predicates | [OH\_Predicates](capi-rdb-oh-predicates.md)指定的查询条件。 |
| const char \* const columns[] | 要查询的列，如果传入空值，则查询所有列。 |
| int len | 传入的columns数组的长度。若len大于columns数组的实际长度，则会访问越界。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Cursor \*](capi-rdb-oh-cursor.md) | 如果执行成功，则返回指向[OH\_Cursor](capi-rdb-oh-cursor.md)实例的指针。如果数据库已关闭或数据库没有响应，则返回nullptr。 |

### OH\_RdbTrans\_QuerySqlWithoutRowCount()

PhonePC/2in1TabletTVWearable

```
1. OH_Cursor *OH_RdbTrans_QuerySqlWithoutRowCount(OH_Rdb_Transaction *trans, const char *sql, const OH_Data_Values *args)
```

**描述**

根据SQL语句查询数据库中的数据，不计算行数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md) \*trans | 指向[OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md)实例的指针。 |
| const char \*sql | 要执行的SQL语句。 |
| [const OH\_Data\_Values](capi-rdb-oh-data-values.md) \*args | 指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Cursor \*](capi-rdb-oh-cursor.md) | 如果执行成功，则返回指向[OH\_Cursor](capi-rdb-oh-cursor.md)实例的指针。如果数据库已关闭或数据库没有响应，则返回nullptr。 |

### OH\_RdbTrans\_BatchInsertWithReturning()

PhonePC/2in1TabletTVWearable

```
1. int OH_RdbTrans_BatchInsertWithReturning(OH_Rdb_Transaction *trans, const char *table, const OH_Data_VBuckets *rows, Rdb_ConflictResolution resolution, OH_RDB_ReturningContext *context)
```

**描述**

将批量数据插入目标表，并将变更信息输出到上下文中。

一次最多可以插入32766个参数。如果参数数量超过上限，则返回错误代码RDB\_E\_INVALID\_ARGS。

参数数量计算方式为插入数据条数乘以插入数据时所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10则最多可以插入3276条数据（3276\*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md) \*trans | 指向[OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md)实例的指针。 |
| const char \*table | 要插入的目标表名。 |
| [const OH\_Data\_VBuckets](capi-rdb-oh-data-vbuckets.md) \*rows | 要插入到表中的行数据。 |
| [Rdb\_ConflictResolution](capi-oh-rdb-types-h.md#rdb_conflictresolution) resolution | 发生冲突时的解决策略[Rdb\_ConflictResolution](capi-oh-rdb-types-h.md#rdb_conflictresolution)，不建议使用RDB\_CONFLICT\_FAIL，因为失败时会抛异常，  无法正常获取实际的变更数据。 |
| [OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md) \*context | 指向[OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  返回RDB\_OK表示执行成功。  返回RDB\_E\_INVALID\_ARGS表示输入参数无效。  返回RDB\_E\_WAL\_SIZE\_OVER\_LIMIT表示WAL文件大小超过默认限制。  返回RDB\_E\_NOT\_SUPPORTED表示不支持的操作。  返回RDB\_E\_DATABASE\_BUSY表示数据库忙。  返回RDB\_E\_ALREADY\_CLOSED表示数据库已关闭。  返回RDB\_E\_SQLITE\_FULL表示SQLite错误：数据库已满。  返回RDB\_E\_SQLITE\_CORRUPT表示数据库损坏。  返回RDB\_E\_SQLITE\_BUSY表示SQLite错误：数据库文件被锁定。  返回RDB\_E\_SQLITE\_LOCKED表示SQLite错误：数据库中的表被锁定。  返回RDB\_E\_SQLITE\_IOERR表示SQLite错误：发生某种磁盘I/O错误。  返回RDB\_E\_SQLITE\_TOO\_BIG表示SQLite错误：TEXT或BLOB超出大小限制。  返回RDB\_E\_SQLITE\_MISMATCH表示SQLite错误：数据类型不匹配。  返回RDB\_E\_SQLITE\_CONSTRAINT表示SQLite错误：由于违反约束而中止。  返回RDB\_E\_SQLITE\_ERROR表示SQLite错误。可能原因：语法错误，例如表或列不存在。  具体错误码可参考[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。 |

### OH\_RdbTrans\_UpdateWithReturning()

PhonePC/2in1TabletTVWearable

```
1. int OH_RdbTrans_UpdateWithReturning(OH_Rdb_Transaction *trans, OH_VBucket *row, OH_Predicates *predicates, Rdb_ConflictResolution resolution, OH_RDB_ReturningContext *context)
```

**描述**

根据指定条件更新数据库中的数据并输出更改信息到上下文。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md) \*trans | 指向[OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md)实例的指针。 |
| [OH\_VBucket](capi-rdb-oh-vbucket.md) \*row | 要更新到表中的行数据。 |
| [OH\_Predicates](capi-rdb-oh-predicates.md) \*predicates | 指向[OH\_Predicates](capi-rdb-oh-predicates.md)实例的指针。 |
| [Rdb\_ConflictResolution](capi-oh-rdb-types-h.md#rdb_conflictresolution) resolution | 发生冲突时的解决策略Rdb\_ConflictResolution，不建议使用RDB\_CONFLICT\_FAIL，因为失败时会抛异常，  无法正常获取实际的变更数据。 |
| [OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md) \*context | 指向[OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  返回RDB\_OK表示执行成功。  返回RDB\_E\_INVALID\_ARGS表示输入参数无效。  返回RDB\_E\_WAL\_SIZE\_OVER\_LIMIT表示WAL文件大小超过默认限制。  返回RDB\_E\_NOT\_SUPPORTED表示不支持的操作。  返回RDB\_E\_EMPTY\_VALUES\_BUCKET表示值桶为空。  返回RDB\_E\_DATABASE\_BUSY表示数据库忙。  返回RDB\_E\_ALREADY\_CLOSED表示数据库已关闭。  返回RDB\_E\_SQLITE\_FULL表示SQLite错误：数据库已满。  返回RDB\_E\_SQLITE\_CORRUPT表示数据库损坏。  返回RDB\_E\_SQLITE\_BUSY表示SQLite错误：数据库文件被锁定。  返回RDB\_E\_SQLITE\_LOCKED表示SQLite错误：数据库中的表被锁定。  返回RDB\_E\_SQLITE\_IOERR表示SQLite错误：发生某种磁盘I/O错误。  返回RDB\_E\_SQLITE\_TOO\_BIG表示SQLite错误：TEXT或BLOB超出大小限制。  返回RDB\_E\_SQLITE\_MISMATCH表示SQLite错误：数据类型不匹配。  返回RDB\_E\_SQLITE\_CONSTRAINT表示SQLite错误：由于违反约束而中止。  返回RDB\_E\_SQLITE\_ERROR表示SQLite错误。可能原因：语法错误，例如表或列不存在。  具体错误码可参考[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。 |

### OH\_RdbTrans\_DeleteWithReturning()

PhonePC/2in1TabletTVWearable

```
1. int OH_RdbTrans_DeleteWithReturning(OH_Rdb_Transaction *trans, OH_Predicates *predicates, OH_RDB_ReturningContext *context)
```

**描述**

根据指定条件从数据库中删除数据并输出更改信息到上下文。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md) \*trans | 指向[OH\_Rdb\_Transaction](capi-rdb-oh-rdb-transaction.md)实例的指针。 |
| [OH\_Predicates](capi-rdb-oh-predicates.md) \*predicates | 指向[OH\_Predicates](capi-rdb-oh-predicates.md)实例的指针。 |
| [OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md) \*context | 指向[OH\_RDB\_ReturningContext](capi-rdb-oh-rdb-returningcontext.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  返回RDB\_OK表示执行成功。  返回RDB\_E\_INVALID\_ARGS表示输入参数无效。  返回RDB\_E\_WAL\_SIZE\_OVER\_LIMIT表示WAL文件大小超过默认限制。  返回RDB\_E\_NOT\_SUPPORTED表示不支持的操作。  返回RDB\_E\_DATABASE\_BUSY表示数据库忙。  返回RDB\_E\_ALREADY\_CLOSED表示数据库已关闭。  返回RDB\_E\_SQLITE\_FULL表示SQLite错误：数据库已满。  返回RDB\_E\_SQLITE\_CORRUPT表示数据库损坏。  返回RDB\_E\_SQLITE\_BUSY表示SQLite错误：数据库文件被锁定。  返回RDB\_E\_SQLITE\_LOCKED表示SQLite错误：数据库中的表被锁定。  返回RDB\_E\_SQLITE\_IOERR表示SQLite错误：发生某种磁盘I/O错误。  返回RDB\_E\_SQLITE\_TOO\_BIG表示SQLite错误：TEXT或BLOB超出大小限制。  返回RDB\_E\_SQLITE\_MISMATCH表示SQLite错误：数据类型不匹配。  返回RDB\_E\_SQLITE\_ERROR表示SQLite错误。可能原因：语法错误，例如表或列不存在。  具体错误码可参考[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。 |
