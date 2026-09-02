---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-values-bucket-h
title: oh_values_bucket.h
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 头文件 > oh_values_bucket.h
category: harmonyos-references
scraped_at: 2026-09-02T15:00:42+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c97dae79794bd0dd0f078243c5e377b34626c46912ca04923b3455cb2b88a7f5
---

## 概述

用于存储键值对的类型。

**引用文件：** <database/rdb/oh\_values\_bucket.h>

**库：** libnative\_rdb\_ndk.z.so

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 10

**相关模块：** [RDB](capi-rdb.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_VBucket](capi-rdb-oh-vbucket.md) | OH\_VBucket | 用于存储键值对的类型。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [int OH\_VBucket\_PutAsset(OH\_VBucket \*bucket, const char \*field, Data\_Asset \*value)](capi-oh-values-bucket-h.md#oh_vbucket_putasset) | 将[Data\_Asset](capi-rdb-data-asset.md) 类型的对象放入给定列名的[OH\_VBucket](capi-rdb-oh-vbucket.md)对象中。 |
| [int OH\_VBucket\_PutAssets(OH\_VBucket \*bucket, const char \*field, Data\_Asset \*\*value, uint32\_t count)](capi-oh-values-bucket-h.md#oh_vbucket_putassets) | 将[Data\_Asset](capi-rdb-data-asset.md) 类型的对象数组放入给定列名的[OH\_VBucket](capi-rdb-oh-vbucket.md)对象中。 |
| [int OH\_VBucket\_PutFloatVector(OH\_VBucket \*bucket, const char \*field, const float \*vec, size\_t len)](capi-oh-values-bucket-h.md#oh_vbucket_putfloatvector) | 将float数组类型对象放入给定列名的[OH\_VBucket](capi-rdb-oh-vbucket.md)对象中。 |
| [int OH\_VBucket\_PutUnlimitedInt(OH\_VBucket \*bucket, const char \*field, int sign, const uint64\_t \*trueForm, size\_t len)](capi-oh-values-bucket-h.md#oh_vbucket_putunlimitedint) | 将任意长度的整数类型对象放入给定列名的[OH\_VBucket](capi-rdb-oh-vbucket.md)对象中。 |

## 函数说明

### OH\_VBucket\_PutAsset()

```c
int OH_VBucket_PutAsset(OH_VBucket *bucket, const char *field, Data_Asset *value)
```

**描述**

将[Data\_Asset](capi-rdb-data-asset.md) 类型的对象放入给定列名的[OH\_VBucket](capi-rdb-oh-vbucket.md)对象中。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VBucket](capi-rdb-oh-vbucket.md) \*bucket | 表示指向[OH\_VBucket](capi-rdb-oh-vbucket.md)实例的指针。 |
| const char \*field | 数据库表中的列名，不能为空。 |
| [Data\_Asset](capi-rdb-data-asset.md) \*value | 数据库表中指定列名对应的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。  RDB\_OK 表示成功。  RDB\_E\_INVALID\_ARGS 表示无效参数。详细信息请参阅[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。 |

### OH\_VBucket\_PutAssets()

```c
int OH_VBucket_PutAssets(OH_VBucket *bucket, const char *field, Data_Asset **value, uint32_t count)
```

**描述**

将[Data\_Asset](capi-rdb-data-asset.md) 类型的对象数组放入给定列名的[OH\_VBucket](capi-rdb-oh-vbucket.md)对象中。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VBucket](capi-rdb-oh-vbucket.md) \*bucket | 表示指向[OH\_VBucket](capi-rdb-oh-vbucket.md)实例的指针。 |
| const char \*field | 数据库表中的列名，不能为空。 |
| [Data\_Asset](capi-rdb-data-asset.md) \*\*value | 数据库表中指定列名对应的值。 |
| uint32\_t count | 表示传入的[Data\_Asset](capi-rdb-data-asset.md)对象数组元素的个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。  RDB\_OK 表示成功。  RDB\_E\_INVALID\_ARGS 表示无效参数。详细信息请参阅[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。 |

**参考：**

[OH\_VBucket](capi-rdb-oh-vbucket.md)

### OH\_VBucket\_PutFloatVector()

```c
int OH_VBucket_PutFloatVector(OH_VBucket *bucket, const char *field, const float *vec, size_t len)
```

**描述**

将float数组类型对象放入给定列名的[OH\_VBucket](capi-rdb-oh-vbucket.md)对象中。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VBucket](capi-rdb-oh-vbucket.md) \*bucket | 表示指向[OH\_VBucket](capi-rdb-oh-vbucket.md)实例的指针。 |
| const char \*field | 数据库表中的列名，不能为空。 |
| const float \*vec | 表示指向float数组的指针。 |
| size\_t len | 表示float数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。  RDB\_OK 表示成功。  RDB\_E\_INVALID\_ARGS 表示无效参数。详细信息请参阅[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。 |

**参考：**

[OH\_VBucket](capi-rdb-oh-vbucket.md)

### OH\_VBucket\_PutUnlimitedInt()

```c
int OH_VBucket_PutUnlimitedInt(OH_VBucket *bucket, const char *field, int sign, const uint64_t *trueForm, size_t len)
```

**描述**

将任意长度的整数类型对象放入给定列名的[OH\_VBucket](capi-rdb-oh-vbucket.md)对象中。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VBucket](capi-rdb-oh-vbucket.md) \*bucket | 表示指向[OH\_VBucket](capi-rdb-oh-vbucket.md)实例的指针。 |
| const char \*field | 数据库表中的列名，不能为空。 |
| int sign | 表示整数类型对象是正数还是负数，0表示正数，1表示负数。 |
| const uint64\_t \*trueForm | 表示指向整数类型数组的指针。 |
| size\_t len | 表示整数数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。  RDB\_OK 表示成功。  RDB\_E\_INVALID\_ARGS 表示无效参数。详细信息请参阅[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。 |
