---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-data-values-h
title: oh_data_values.h
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 头文件 > oh_data_values.h
category: harmonyos-references
scraped_at: 2026-04-28T07:59:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:672587f7c903a3d95f609123aa9b7c7829be51e37a84174585e2b26b266d4290
---

## 概述

PhonePC/2in1TabletTVWearable

提供与多条数据值相关的函数和枚举。

**引用文件：** <database/data/oh\_data\_values.h>

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
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) | OH\_Data\_Values | 定义OH\_Data\_Values结构类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Data\_Values \*OH\_Values\_Create(void)](capi-oh-data-values-h.md#oh_values_create) | 创建[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例，用于储存多条键值对数据。 |
| [int OH\_Values\_Destroy(OH\_Data\_Values \*values)](capi-oh-data-values-h.md#oh_values_destroy) | 销毁[OH\_Data\_Values](capi-rdb-oh-data-values.md)对象。 |
| [int OH\_Values\_Put(OH\_Data\_Values \*values, const OH\_Data\_Value \*val)](capi-oh-data-values-h.md#oh_values_put) | 添加OH\_Data\_Value类型数据给OH\_Data\_Values对象。 |
| [int OH\_Values\_PutNull(OH\_Data\_Values \*values)](capi-oh-data-values-h.md#oh_values_putnull) | 添加空数据给OH\_Data\_Values对象。 |
| [int OH\_Values\_PutInt(OH\_Data\_Values \*values, int64\_t val)](capi-oh-data-values-h.md#oh_values_putint) | 添加整型数据给OH\_Data\_Values对象。 |
| [int OH\_Values\_PutReal(OH\_Data\_Values \*values, double val)](capi-oh-data-values-h.md#oh_values_putreal) | 添加REAL类型数据给OH\_Data\_Values对象。 |
| [int OH\_Values\_PutText(OH\_Data\_Values \*values, const char \*val)](capi-oh-data-values-h.md#oh_values_puttext) | 添加字符串类型数据给OH\_Data\_Values对象。 |
| [int OH\_Values\_PutBlob(OH\_Data\_Values \*values, const unsigned char \*val, size\_t length)](capi-oh-data-values-h.md#oh_values_putblob) | 添加BLOB类型数据给OH\_Data\_Values对象。 |
| [int OH\_Values\_PutAsset(OH\_Data\_Values \*values, const Data\_Asset \*val)](capi-oh-data-values-h.md#oh_values_putasset) | 添加ASSET类型数据给OH\_Data\_Values对象。 |
| [int OH\_Values\_PutAssets(OH\_Data\_Values \*values, const Data\_Asset \* const \* val, size\_t length)](capi-oh-data-values-h.md#oh_values_putassets) | 添加ASSETS类型数据给OH\_Data\_Values对象。 |
| [int OH\_Values\_PutFloatVector(OH\_Data\_Values \*values, const float \*val, size\_t length)](capi-oh-data-values-h.md#oh_values_putfloatvector) | 添加float数组类型数据给OH\_Data\_Values对象。 |
| [int OH\_Values\_PutUnlimitedInt(OH\_Data\_Values \*values, int sign, const uint64\_t \*trueForm, size\_t length)](capi-oh-data-values-h.md#oh_values_putunlimitedint) | 添加任意长度的整型数组数据给OH\_Data\_Values对象。 |
| [int OH\_Values\_Count(OH\_Data\_Values \*values, size\_t \*count)](capi-oh-data-values-h.md#oh_values_count) | 获取数据个数。 |
| [int OH\_Values\_GetType(OH\_Data\_Values \*values, int index, OH\_ColumnType \*type)](capi-oh-data-values-h.md#oh_values_gettype) | 获取数据类型。 |
| [int OH\_Values\_Get(OH\_Data\_Values \*values, int index, OH\_Data\_Value \*\*val)](capi-oh-data-values-h.md#oh_values_get) | 获取OH\_Data\_Value类型数据。 |
| [int OH\_Values\_IsNull(OH\_Data\_Values \*values, int index, bool \*val)](capi-oh-data-values-h.md#oh_values_isnull) | 检查数据是否为空。 |
| [int OH\_Values\_GetInt(OH\_Data\_Values \*values, int index, int64\_t \*val)](capi-oh-data-values-h.md#oh_values_getint) | 获取整型数据。 |
| [int OH\_Values\_GetReal(OH\_Data\_Values \*values, int index, double \*val)](capi-oh-data-values-h.md#oh_values_getreal) | 获取REAL类型数据。 |
| [int OH\_Values\_GetText(OH\_Data\_Values \*values, int index, const char \*\*val)](capi-oh-data-values-h.md#oh_values_gettext) | 获取字符串类型数据。 |
| [int OH\_Values\_GetBlob(OH\_Data\_Values \*values, int index, const uint8\_t \*\*val, size\_t \*length)](capi-oh-data-values-h.md#oh_values_getblob) | 获取BLOB类型数据。 |
| [int OH\_Values\_GetAsset(OH\_Data\_Values \*values, int index, Data\_Asset \*val)](capi-oh-data-values-h.md#oh_values_getasset) | 获取ASSET类型数据。 |
| [int OH\_Values\_GetAssetsCount(OH\_Data\_Values \*values, int index, size\_t \*length)](capi-oh-data-values-h.md#oh_values_getassetscount) | 获取ASSETS类型数据的大小。 |
| [int OH\_Values\_GetAssets(OH\_Data\_Values \*values, int index, Data\_Asset \*\*val, size\_t inLen, size\_t \*outLen)](capi-oh-data-values-h.md#oh_values_getassets) | 获取ASSETS类型数据。 |
| [int OH\_Values\_GetFloatVectorCount(OH\_Data\_Values \*values, int index, size\_t \*length)](capi-oh-data-values-h.md#oh_values_getfloatvectorcount) | 获取float数组类型数据的大小。 |
| [int OH\_Values\_GetFloatVector(OH\_Data\_Values \*values, int index, float \*val, size\_t inLen, size\_t \*outLen)](capi-oh-data-values-h.md#oh_values_getfloatvector) | 获取float数组类型数据。 |
| [int OH\_Values\_GetUnlimitedIntBand(OH\_Data\_Values \*values, int index, size\_t \*length)](capi-oh-data-values-h.md#oh_values_getunlimitedintband) | 获取任意长度的整型数据的大小。 |
| [int OH\_Values\_GetUnlimitedInt(OH\_Data\_Values \*values, int index, int \*sign, uint64\_t \*trueForm, size\_t inLen,size\_t \*outLen)](capi-oh-data-values-h.md#oh_values_getunlimitedint) | 获取任意长度的整型数据。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Values\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_Data_Values *OH_Values_Create(void)
```

**描述**

创建[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例，用于储存多条键值对数据。

**起始版本：** 18

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) | 执行成功时返回指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针，否则返回nullptr。  使用完成后，必须通过[OH\_Values\_Destroy](capi-oh-data-values-h.md#oh_values_destroy)接口释放内存。 |

### OH\_Values\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_Destroy(OH_Data_Values *values)
```

**描述**

销毁[OH\_Data\_Values](capi-rdb-oh-data-values.md)对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Values\_Put()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_Put(OH_Data_Values *values, const OH_Data_Value *val)
```

**描述**

添加OH\_Data\_Value类型数据给OH\_Data\_Values对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| const [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*val | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Values\_PutNull()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_PutNull(OH_Data_Values *values)
```

**描述**

添加空数据给OH\_Data\_Values对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Values\_PutInt()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_PutInt(OH_Data_Values *values, int64_t val)
```

**描述**

添加整型数据给OH\_Data\_Values对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| int64\_t val | 表示整型数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Values\_PutReal()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_PutReal(OH_Data_Values *values, double val)
```

**描述**

添加REAL类型数据给OH\_Data\_Values对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| double val | 表示REAL类型数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Values\_PutText()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_PutText(OH_Data_Values *values, const char *val)
```

**描述**

添加字符串类型数据给OH\_Data\_Values对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| const char \*val | 表示字符串类型数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Values\_PutBlob()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_PutBlob(OH_Data_Values *values, const unsigned char *val, size_t length)
```

**描述**

添加BLOB类型数据给OH\_Data\_Values对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| const unsigned char \*val | 表示BLOB类型数据。 |
| size\_t length | 该参数为输入参数，表示开发者传入的BLOB类型数据的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Values\_PutAsset()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_PutAsset(OH_Data_Values *values, const Data_Asset *val)
```

**描述**

添加ASSET类型数据给OH\_Data\_Values对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| const [Data\_Asset](capi-rdb-data-asset.md) \*val | 表示指向[Data\_Asset](capi-rdb-data-asset.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Values\_PutAssets()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_PutAssets(OH_Data_Values *values, const Data_Asset * const * val, size_t length)
```

**描述**

添加ASSETS类型数据给OH\_Data\_Values对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| const [Data\_Asset](capi-rdb-data-asset.md) \* const \* val | 表示指向[Data\_Asset](capi-rdb-data-asset.md)对象的指针。 |
| size\_t length | 该参数为输入参数，表示开发者传入的[Data\_Asset](capi-rdb-data-asset.md)对象数组元素的个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Values\_PutFloatVector()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_PutFloatVector(OH_Data_Values *values, const float *val, size_t length)
```

**描述**

添加float数组类型数据给OH\_Data\_Values对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| const float \*val | 表示指向float数组对象的指针。 |
| size\_t length | 该参数为输入参数，表示开发者传入的float数组的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Values\_PutUnlimitedInt()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_PutUnlimitedInt(OH_Data_Values *values, int sign, const uint64_t *trueForm, size_t length)
```

**描述**

添加任意长度的整型数组数据给OH\_Data\_Values对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| int sign | 表示正负数，0表示正整数，1表示负整数。 |
| const uint64\_t \*trueForm | 表示指向整型数组的指针。 |
| size\_t length | 该参数为输入参数，表示开发者传入的整型数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Values\_Count()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_Count(OH_Data_Values *values, size_t *count)
```

**描述**

获取数据个数。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| size\_t \*count | 一个输出参数，表示values中数据的个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Values\_GetType()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_GetType(OH_Data_Values *values, int index, OH_ColumnType *type)
```

**描述**

获取数据类型。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| [OH\_ColumnType](capi-oh-data-value-h.md#oh_columntype) \*type | 一个输出参数，表示数据类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Values\_Get()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_Get(OH_Data_Values *values, int index, OH_Data_Value **val)
```

**描述**

获取OH\_Data\_Value类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*\*val | 一个输出参数，表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。  无需申请内存和释放内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Values\_IsNull()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_IsNull(OH_Data_Values *values, int index, bool *val)
```

**描述**

检查数据是否为空。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| bool \*val | 一个输出参数，true表示空，false表示不为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Values\_GetInt()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_GetInt(OH_Data_Values *values, int index, int64_t *val)
```

**描述**

获取整型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| int64\_t \*val | 一个输出参数，表示指向整型数据的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |

### OH\_Values\_GetReal()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_GetReal(OH_Data_Values *values, int index, double *val)
```

**描述**

获取REAL类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| double \*val | 一个输出参数，表示指向REAL类型数据的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |

### OH\_Values\_GetText()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_GetText(OH_Data_Values *values, int index, const char **val)
```

**描述**

获取字符串类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| const char \*\*val | 一个输出参数，表示指向字符串类型数据的指针。  无需申请内存和释放内存。  val的生命周期遵循values中index的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |

### OH\_Values\_GetBlob()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_GetBlob(OH_Data_Values *values, int index, const uint8_t **val, size_t *length)
```

**描述**

获取BLOB类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| const uint8\_t \*\*val | 一个输出参数，表示指向BLOB类型数据的指针。  无需申请内存和释放内存。  val的生命周期遵循values中index的值。 |
| size\_t \*length | 该参数为输出参数，表示BLOB类型数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |

### OH\_Values\_GetAsset()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_GetAsset(OH_Data_Values *values, int index, Data_Asset *val)
```

**描述**

获取ASSET类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| [Data\_Asset](capi-rdb-data-asset.md) \*val | 表示指向[Data\_Asset](capi-rdb-data-asset.md)对象的指针。  需要申请数据内存。  此函数仅填充数据，否则执行失败。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |

### OH\_Values\_GetAssetsCount()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_GetAssetsCount(OH_Data_Values *values, int index, size_t *length)
```

**描述**

获取ASSETS类型数据的大小。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| size\_t \*length | 该参数为输出参数，表示ASSETS类型数据的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |

### OH\_Values\_GetAssets()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_GetAssets(OH_Data_Values *values, int index, Data_Asset **val, size_t inLen, size_t *outLen)
```

**描述**

获取ASSETS类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| [Data\_Asset](capi-rdb-data-asset.md) \*\*val | 表示指向[Data\_Asset](capi-rdb-data-asset.md)对象的指针。  使用时需要申请数据内存。  此函数仅填充数据，否则执行失败。 |
| size\_t inLen | 表示val的大小。可以通过[OH\_Values\_GetAssetsCount](capi-oh-data-values-h.md#oh_values_getassetscount)获取。 |
| size\_t \*outLen | 一个输出参数，表示实际获取的数据大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |

### OH\_Values\_GetFloatVectorCount()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_GetFloatVectorCount(OH_Data_Values *values, int index, size_t *length)
```

**描述**

获取float数组类型数据的大小。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| size\_t \*length | 该参数为输出参数，表示float数组类型数据的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |

### OH\_Values\_GetFloatVector()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_GetFloatVector(OH_Data_Values *values, int index, float *val, size_t inLen, size_t *outLen)
```

**描述**

获取float数组类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| float \*val | 表示指向float数组的指针。  需要申请数据内存。  此函数仅填充数据，否则执行失败。 |
| size\_t inLen | 表示val的大小。可以通过[OH\_Values\_GetFloatVectorCount](capi-oh-data-values-h.md#oh_values_getfloatvectorcount)获取。 |
| size\_t \*outLen | 一个输出参数，表示实际获取的数据大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |

### OH\_Values\_GetUnlimitedIntBand()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_GetUnlimitedIntBand(OH_Data_Values *values, int index, size_t *length)
```

**描述**

获取任意长度的整型数据的大小。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| size\_t \*length | 该参数为输出参数，表示整型数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |

### OH\_Values\_GetUnlimitedInt()

PhonePC/2in1TabletTVWearable

```
1. int OH_Values_GetUnlimitedInt(OH_Data_Values *values, int index, int *sign, uint64_t *trueForm, size_t inLen, size_t *outLen)
```

**描述**

获取任意长度的整型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Values](capi-rdb-oh-data-values.md) \*values | 表示指向[OH\_Data\_Values](capi-rdb-oh-data-values.md)实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| int \*sign | 一个输出参数，表示正负数，0表示正整数，1表示负整数。 |
| uint64\_t \*trueForm | 表示指向整型数组的指针。  需要申请数据内存。  此函数仅填充数据，否则执行失败。 |
| size\_t inLen | 表示trueForm的大小。可以通过[OH\_Values\_GetUnlimitedIntBand](capi-oh-data-values-h.md#oh_values_getunlimitedintband)获取。 |
| size\_t \*outLen | 一个输出参数，表示实际获取的数据大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |
