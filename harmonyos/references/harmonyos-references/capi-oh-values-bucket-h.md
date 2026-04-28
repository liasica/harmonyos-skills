---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-values-bucket-h
title: oh_values_bucket.h
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 头文件 > oh_values_bucket.h
category: harmonyos-references
scraped_at: 2026-04-28T07:59:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:55abe43d99efb144ccc12dbbd9046ccf77edf7b1a6cbb1416f3d2a7b03bab3a1
---

## 概述

PhonePC/2in1TabletTVWearable

用于存储键值对的类型。

**引用文件：** <database/rdb/oh\_values\_bucket.h>

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
| [OH\_VBucket](capi-rdb-oh-vbucket.md) | OH\_VBucket | 用于存储键值对的类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int OH\_VBucket\_PutAsset(OH\_VBucket \*bucket, const char \*field, Data\_Asset \*value)](capi-oh-values-bucket-h.md#oh_vbucket_putasset) | 将[Data\_Asset](capi-rdb-data-asset.md) 类型的对象放入给定列名的[OH\_VBucket](capi-rdb-oh-vbucket.md)对象中。 |
| [int OH\_VBucket\_PutAssets(OH\_VBucket \*bucket, const char \*field, Data\_Asset \*\*value, uint32\_t count)](capi-oh-values-bucket-h.md#oh_vbucket_putassets) | 将[Data\_Asset](capi-rdb-data-asset.md) 类型的对象数组放入给定列名的[OH\_VBucket](capi-rdb-oh-vbucket.md)对象中。 |
| [int OH\_VBucket\_PutFloatVector(OH\_VBucket \*bucket, const char \*field, const float \*vec, size\_t len)](capi-oh-values-bucket-h.md#oh_vbucket_putfloatvector) | 将float数组类型对象放入给定列名的[OH\_VBucket](capi-rdb-oh-vbucket.md)对象中。 |
| [int OH\_VBucket\_PutUnlimitedInt(OH\_VBucket \*bucket, const char \*field, int sign, const uint64\_t \*trueForm, size\_t len)](capi-oh-values-bucket-h.md#oh_vbucket_putunlimitedint) | 将任意长度的整数类型对象放入给定列名的[OH\_VBucket](capi-rdb-oh-vbucket.md)对象中。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_VBucket\_PutAsset()

PhonePC/2in1TabletTVWearable

```
1. int OH_VBucket_PutAsset(OH_VBucket *bucket, const char *field, Data_Asset *value)
```

**描述**

将[Data\_Asset](capi-rdb-data-asset.md) 类型的对象放入给定列名的[OH\_VBucket](capi-rdb-oh-vbucket.md)对象中。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VBucket](capi-rdb-oh-vbucket.md) \*bucket | 表示指向[OH\_VBucket](capi-rdb-oh-vbucket.md)实例的指针。 |
| const char \*field | 数据库表中的列名。 |
| [Data\_Asset](capi-rdb-data-asset.md) \*value | 数据库表中指定列名对应的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。  RDB\_OK 表示成功。  RDB\_E\_INVALID\_ARGS 表示无效参数。 |

### OH\_VBucket\_PutAssets()

PhonePC/2in1TabletTVWearable

```
1. int OH_VBucket_PutAssets(OH_VBucket *bucket, const char *field, Data_Asset **value, uint32_t count)
```

**描述**

将[Data\_Asset](capi-rdb-data-asset.md) 类型的对象数组放入给定列名的[OH\_VBucket](capi-rdb-oh-vbucket.md)对象中。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VBucket](capi-rdb-oh-vbucket.md) \*bucket | 表示指向[OH\_VBucket](capi-rdb-oh-vbucket.md)实例的指针。 |
| const char \*field | 数据库表中的列名。 |
| [Data\_Asset](capi-rdb-data-asset.md) \*\*value | 数据库表中指定列名对应的值。 |
| uint32\_t count | 表示传入的[Data\_Asset](capi-rdb-data-asset.md)对象数组元素的个数. |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。  RDB\_OK 表示成功。  RDB\_E\_INVALID\_ARGS 表示无效参数。 |

**参考：**

OH\_VBucket

### OH\_VBucket\_PutFloatVector()

PhonePC/2in1TabletTVWearable

```
1. int OH_VBucket_PutFloatVector(OH_VBucket *bucket, const char *field, const float *vec, size_t len)
```

**描述**

将float数组类型对象放入给定列名的[OH\_VBucket](capi-rdb-oh-vbucket.md)对象中。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VBucket](capi-rdb-oh-vbucket.md) \*bucket | 表示指向[OH\_VBucket](capi-rdb-oh-vbucket.md)实例的指针。 |
| const char \*field | 数据库表中的列名。 |
| const float \*vec | 表示指向float数组的指针。 |
| size\_t len | 表示float数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。  RDB\_OK 表示成功。  RDB\_E\_INVALID\_ARGS 表示无效参数。 |

**参考：**

OH\_VBucket

### OH\_VBucket\_PutUnlimitedInt()

PhonePC/2in1TabletTVWearable

```
1. int OH_VBucket_PutUnlimitedInt(OH_VBucket *bucket, const char *field, int sign, const uint64_t *trueForm, size_t len)
```

**描述**

将任意长度的整数类型对象放入给定列名的[OH\_VBucket](capi-rdb-oh-vbucket.md)对象中。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VBucket](capi-rdb-oh-vbucket.md) \*bucket | 表示指向[OH\_VBucket](capi-rdb-oh-vbucket.md)实例的指针。 |
| const char \*field | 数据库表中的列名。 |
| int sign | 表示整数类型对象是正数还是负数，0表示正数，1表示负数。 |
| const uint64\_t \*trueForm | 表示指向整数类型数组的指针。 |
| size\_t len | 表示整数数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。  RDB\_OK 表示成功。  RDB\_E\_INVALID\_ARGS 表示无效参数。 |
