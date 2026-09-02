---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-predicates-h
title: oh_predicates.h
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 头文件 > oh_predicates.h
category: harmonyos-references
scraped_at: 2026-09-02T15:00:42+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e78a281aef7e8851a7620ad73f996d9e7cae511363ca7ef84f13169930c79003
---

## 概述

表示关系型数据库（RDB）的谓词。

**引用文件：** <database/rdb/oh\_predicates.h>

**库：** libnative\_rdb\_ndk.z.so

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 10

**相关模块：** [RDB](capi-rdb.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Predicates](capi-rdb-oh-predicates.md) | OH\_Predicates | 表示谓词。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_OrderType](capi-oh-predicates-h.md#oh_ordertype) | OH\_OrderType | 排序方式。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [int OH\_Predicates\_NotLike(OH\_Predicates \*predicates, const char \*field, const char \*pattern)](capi-oh-predicates-h.md#oh_predicates_notlike) | 设置OH\_Predicates以匹配数据类型为字符串且值不类似于指定值的字段。  此方法类似于SQL语句中的“Not Like”。 |
| [int OH\_Predicates\_Glob(OH\_Predicates \*predicates, const char \*field, const char \*pattern)](capi-oh-predicates-h.md#oh_predicates_glob) | 设置OH\_Predicates以匹配指定字段（数据类型为字符串）且值包含通配符的字段。  与“Like”方法不同，此方法的输入参数区分大小写。 |
| [int OH\_Predicates\_NotGlob(OH\_Predicates \*predicates, const char \*field, const char \*pattern)](capi-oh-predicates-h.md#oh_predicates_notglob) | 设置OH\_Predicates以不匹配指定字段（数据类型为字符串）且值包含通配符的字段。  与“Not Like”方法不同，此方法的输入参数区分大小写。 |
| [int OH\_Predicates\_Having(OH\_Predicates \*predicates, const char \*conditions, const OH\_Data\_Values \*values)](capi-oh-predicates-h.md#oh_predicates_having) | 设置OH\_Predicates以指定条件来过滤分组结果，这些结果将出现在最终结果中。 |

## 枚举类型说明

### OH\_OrderType

```c
enum OH_OrderType
```

**描述**

排序方式。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| ASC = 0 | 升序排列。 |
| DESC = 1 | 降序排列。 |

## 函数说明

### OH\_Predicates\_NotLike()

```c
int OH_Predicates_NotLike(OH_Predicates *predicates, const char *field, const char *pattern)
```

**描述**

设置OH\_Predicates以匹配数据类型为字符串且值不类似于指定值的字段。

此方法类似于SQL语句中的“Not Like”。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Predicates](capi-rdb-oh-predicates.md) \*predicates | 表示指向[OH\_Predicates](capi-rdb-oh-predicates.md)实例的指针，不能为空。 |
| const char \*field | 表示数据库表中的列名，不能为空。 |
| const char \*pattern | 表示要比较的指定值，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。  RDB\_OK 表示成功。  RDB\_E\_INVALID\_ARGS 表示无效参数。详细信息请参阅[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。 |

### OH\_Predicates\_Glob()

```c
int OH_Predicates_Glob(OH_Predicates *predicates, const char *field, const char *pattern)
```

**描述**

设置OH\_Predicates以匹配指定字段（数据类型为字符串）且值包含通配符的字段。

与“Like”方法不同，此方法的输入参数区分大小写。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Predicates](capi-rdb-oh-predicates.md) \*predicates | 表示指向[OH\_Predicates](capi-rdb-oh-predicates.md)实例的指针，不能为空。 |
| const char \*field | 表示数据库表中的列名，不能为空。 |
| const char \*pattern | 表示与谓词匹配的值，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。  RDB\_OK 表示成功。  RDB\_E\_INVALID\_ARGS 表示无效参数。详细信息请参阅[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。 |

### OH\_Predicates\_NotGlob()

```c
int OH_Predicates_NotGlob(OH_Predicates *predicates, const char *field, const char *pattern)
```

**描述**

设置OH\_Predicates以不匹配指定字段（数据类型为字符串）且值包含通配符的字段。

与“Not Like”方法不同，此方法的输入参数区分大小写。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Predicates](capi-rdb-oh-predicates.md) \*predicates | 表示指向[OH\_Predicates](capi-rdb-oh-predicates.md)实例的指针，不能为空。 |
| const char \*field | 表示数据库表中的列名，不能为空。 |
| const char \*pattern | 表示要比较的指定值，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。  RDB\_OK 表示成功。  RDB\_E\_INVALID\_ARGS 表示无效参数。详细信息请参阅[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。 |

### OH\_Predicates\_Having()

```c
int OH_Predicates_Having(OH_Predicates *predicates, const char *conditions, const OH_Data_Values *values)
```

**描述**

设置OH\_Predicates以指定条件来过滤分组结果，这些结果将出现在最终结果中。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Predicates](capi-rdb-oh-predicates.md) \*predicates | 表示指向[OH\_Predicates](capi-rdb-oh-predicates.md)实例的指针，不能为空。 |
| const char \*conditions | 表示having子句中的过滤条件，不能为空且不能为空字符串。 |
| const [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。  RDB\_OK 表示成功。  RDB\_E\_INVALID\_ARGS 表示无效参数。详细信息请参阅[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。 |
