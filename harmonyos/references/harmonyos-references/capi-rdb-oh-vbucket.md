---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-vbucket
title: OH_VBucket
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > OH_VBucket
category: harmonyos-references
scraped_at: 2026-04-28T07:59:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b83c46d4ae8e12f4fccac4cdbefa2daa1144d21a1ee4cbfb19abc7519bb40d38
---

```
1. typedef struct {...} OH_VBucket
```

## 概述

PhonePC/2in1TabletTVWearable

用于存储键值对的类型。

**起始版本：** 10

**相关模块：** [RDB](capi-rdb.md)

**所在头文件：** [oh\_values\_bucket.h](capi-oh-values-bucket-h.md)

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int64\_t id | OH\_VBucket结构体的唯一标识符。 |
| uint16\_t capability | 表示结构体的存储键值对的数量。 |

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int (\*putText)(OH\_VBucket \*bucket, const char \*field, const char \*value)](capi-rdb-oh-vbucket.md#puttext) | 将char\*值放入给定列名的OH\_VBucket对象中。 |
| [int (\*putInt64)(OH\_VBucket \*bucket, const char \*field, int64\_t value)](capi-rdb-oh-vbucket.md#putint64) | 将int64\_t值放入给定列名的OH\_VBucket对象中。 |
| [int (\*putReal)(OH\_VBucket \*bucket, const char \*field, double value)](capi-rdb-oh-vbucket.md#putreal) | 将double值放入给定列名的OH\_VBucket对象中。 |
| [int (\*putBlob)(OH\_VBucket \*bucket, const char \*field, const uint8\_t \*value, uint32\_t size)](capi-rdb-oh-vbucket.md#putblob) | 将const uint8\_t \*值放入给定列名的OH\_VBucket对象中。 |
| [int (\*putNull)(OH\_VBucket \*bucket, const char \*field)](capi-rdb-oh-vbucket.md#putnull) | 将NULL值放入给定列名的OH\_VBucket对象中。 |
| [int (\*clear)(OH\_VBucket \*bucket)](capi-rdb-oh-vbucket.md#clear) | 清空OH\_VBucket对象。 |
| [int (\*destroy)(OH\_VBucket \*bucket)](capi-rdb-oh-vbucket.md#destroy) | 销毁OH\_VBucket对象，并回收该对象占用的内存。 |

### 成员函数说明

PhonePC/2in1TabletTVWearable

### putText()

PhonePC/2in1TabletTVWearable

```
1. int (*putText)(OH_VBucket *bucket, const char *field, const char *value)
```

**描述**

将char\*值放入给定列名的OH\_VBucket对象中。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_VBucket \*bucket | 表示指向OH\_VBucket实例的指针。 |
| const char \*field | 数据库表中的列名 |
| const char \*value | 数据库表中指定列名对应的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

### putInt64()

PhonePC/2in1TabletTVWearable

```
1. int (*putInt64)(OH_VBucket *bucket, const char *field, int64_t value)
```

**描述**

将int64\_t值放入给定列名的OH\_VBucket对象中。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_VBucket \*bucket | 表示指向OH\_VBucket实例的指针。 |
| const char \*field | 数据库表中的列名 |
| int64\_t value | 数据库表中指定列名对应的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

### putReal()

PhonePC/2in1TabletTVWearable

```
1. int (*putReal)(OH_VBucket *bucket, const char *field, double value)
```

**描述**

将double值放入给定列名的OH\_VBucket对象中。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_VBucket \*bucket | 表示指向OH\_VBucket实例的指针。 |
| const char \*field | 数据库表中的列名 |
| double value | 数据库表中指定列名对应的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

### putBlob()

PhonePC/2in1TabletTVWearable

```
1. int (*putBlob)(OH_VBucket *bucket, const char *field, const uint8_t *value, uint32_t size)
```

**描述**

将const uint8\_t \*值放入给定列名的OH\_VBucket对象中。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_VBucket \*bucket | 表示指向OH\_VBucket实例的指针。 |
| const char \*field | 数据库表中的列名 |
| const uint8\_t \*value | 数据库表中指定列名对应的值。 |
| uint32\_t size | 表示value的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

### putNull()

PhonePC/2in1TabletTVWearable

```
1. int (*putNull)(OH_VBucket *bucket, const char *field)
```

**描述**

将NULL值放入给定列名的OH\_VBucket对象中。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_VBucket \*bucket | 表示指向OH\_VBucket实例的指针。 |
| const char \*field | 数据库表中的列名 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

### clear()

PhonePC/2in1TabletTVWearable

```
1. int (*clear)(OH_VBucket *bucket)
```

**描述**

清空[OH\_VBucket](capi-rdb-oh-vbucket.md)对象。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_VBucket \*bucket | 表示指向OH\_VBucket实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

### destroy()

PhonePC/2in1TabletTVWearable

```
1. int (*destroy)(OH_VBucket *bucket)
```

**描述**

销毁[OH\_VBucket](capi-rdb-oh-vbucket.md)对象，并回收该对象占用的内存。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_VBucket \*bucket | 表示指向OH\_VBucket实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |
