---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-data-value-h
title: oh_data_value.h
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 头文件 > oh_data_value.h
category: harmonyos-references
scraped_at: 2026-04-28T07:59:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b93bfd2d9a1c57a64d35a94362010249c4156c282d283b02667d798a612a65be
---

## 概述

PhonePC/2in1TabletTVWearable

提供与单条数据值相关的函数和枚举。

从API version 18开始，OH\_ColumnType从oh\_cursor.h移动至此头文件呈现，对于此类型，API version 18之前即支持使用，各版本均可正常使用。

**引用文件：** <database/data/oh\_data\_value.h>

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
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) | OH\_Data\_Value | 定义[OH\_Data\_Value](capi-rdb-oh-data-value.md)结构类型。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_ColumnType](capi-oh-data-value-h.md#oh_columntype) | OH\_ColumnType | 表示列的类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Data\_Value \*OH\_Value\_Create(void)](capi-oh-data-value-h.md#oh_value_create) | 创建[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例，用于储存单条键值对数据。 |
| [int OH\_Value\_Destroy(OH\_Data\_Value \*value)](capi-oh-data-value-h.md#oh_value_destroy) | 销毁[OH\_Data\_Value](capi-rdb-oh-data-value.md)对象。 |
| [int OH\_Value\_PutNull(OH\_Data\_Value \*value)](capi-oh-data-value-h.md#oh_value_putnull) | 添加空数据。 |
| [int OH\_Value\_PutInt(OH\_Data\_Value \*value, int64\_t val)](capi-oh-data-value-h.md#oh_value_putint) | 添加整型数据。 |
| [int OH\_Value\_PutReal(OH\_Data\_Value \*value, double val)](capi-oh-data-value-h.md#oh_value_putreal) | 添加REAL类型数据。 |
| [int OH\_Value\_PutText(OH\_Data\_Value \*value, const char \*val)](capi-oh-data-value-h.md#oh_value_puttext) | 添加字符串类型数据。 |
| [int OH\_Value\_PutBlob(OH\_Data\_Value \*value, const unsigned char \*val, size\_t length)](capi-oh-data-value-h.md#oh_value_putblob) | 添加BLOB类型数据。 |
| [int OH\_Value\_PutAsset(OH\_Data\_Value \*value, const Data\_Asset \*val)](capi-oh-data-value-h.md#oh_value_putasset) | 添加ASSET类型数据。 |
| [int OH\_Value\_PutAssets(OH\_Data\_Value \*value, const Data\_Asset \* const \* val, size\_t length)](capi-oh-data-value-h.md#oh_value_putassets) | 添加ASSETS类型数据。 |
| [int OH\_Value\_PutFloatVector(OH\_Data\_Value \*value, const float \*val, size\_t length)](capi-oh-data-value-h.md#oh_value_putfloatvector) | 添加float数组类型数据。 |
| [int OH\_Value\_PutUnlimitedInt(OH\_Data\_Value \*value, int sign, const uint64\_t \*trueForm, size\_t length)](capi-oh-data-value-h.md#oh_value_putunlimitedint) | 添加任意长度的整型数组数据。 |
| [int OH\_Value\_GetType(OH\_Data\_Value \*value, OH\_ColumnType \*type)](capi-oh-data-value-h.md#oh_value_gettype) | 获取数据类型。 |
| [int OH\_Value\_IsNull(OH\_Data\_Value \*value, bool \*val)](capi-oh-data-value-h.md#oh_value_isnull) | 检查数据是否为空。 |
| [int OH\_Value\_GetInt(OH\_Data\_Value \*value, int64\_t \*val)](capi-oh-data-value-h.md#oh_value_getint) | 获取整型数据。 |
| [int OH\_Value\_GetReal(OH\_Data\_Value \*value, double \*val)](capi-oh-data-value-h.md#oh_value_getreal) | 获取REAL类型数据。 |
| [int OH\_Value\_GetText(OH\_Data\_Value \*value, const char \*\*val)](capi-oh-data-value-h.md#oh_value_gettext) | 获取字符串类型数据。 |
| [int OH\_Value\_GetBlob(OH\_Data\_Value \*value, const uint8\_t \*\*val, size\_t \*length)](capi-oh-data-value-h.md#oh_value_getblob) | 获取BLOB类型数据。 |
| [int OH\_Value\_GetAsset(OH\_Data\_Value \*value, Data\_Asset \*val)](capi-oh-data-value-h.md#oh_value_getasset) | 获取ASSET类型数据。 |
| [int OH\_Value\_GetAssetsCount(OH\_Data\_Value \*value, size\_t \*length)](capi-oh-data-value-h.md#oh_value_getassetscount) | 获取ASSETS类型数据的大小。 |
| [int OH\_Value\_GetAssets(OH\_Data\_Value \*value, Data\_Asset \*\*val, size\_t inLen, size\_t \*outLen)](capi-oh-data-value-h.md#oh_value_getassets) | 获取ASSETS类型数据。 |
| [int OH\_Value\_GetFloatVectorCount(OH\_Data\_Value \*value, size\_t \*length)](capi-oh-data-value-h.md#oh_value_getfloatvectorcount) | 获取float数组类型数据的大小。 |
| [int OH\_Value\_GetFloatVector(OH\_Data\_Value \*value, float \*val, size\_t inLen, size\_t \*outLen)](capi-oh-data-value-h.md#oh_value_getfloatvector) | 获取float数组类型数据。 |
| [int OH\_Value\_GetUnlimitedIntBand(OH\_Data\_Value \*value, size\_t \*length)](capi-oh-data-value-h.md#oh_value_getunlimitedintband) | 获取任意长度的整型数据的大小。 |
| [int OH\_Value\_GetUnlimitedInt(OH\_Data\_Value \*value, int \*sign, uint64\_t \*trueForm, size\_t inLen, size\_t \*outLen)](capi-oh-data-value-h.md#oh_value_getunlimitedint) | 获取任意长度的整型数据。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_ColumnType

PhonePC/2in1TabletTVWearable

```
1. enum OH_ColumnType
```

**描述**

表示列的类型。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| TYPE\_NULL = 0 | 表示NULL类型。 |
| TYPE\_INT64 | 表示INT64数据类型。 |
| TYPE\_REAL | 表示REAL数据类型。 |
| TYPE\_TEXT | 表示TEXT数据类型。 |
| TYPE\_BLOB | 表示BLOB数据类型。 |
| TYPE\_ASSET | 表示ASSET（资产附件）数据类型。  **起始版本：** 11 |
| TYPE\_ASSETS | 表示ASSETS（多个资产附件）数据类型。  **起始版本：** 11 |
| TYPE\_FLOAT\_VECTOR | 表示FLOAT VECTOR数据类型。  **起始版本：** 18 |
| TYPE\_UNLIMITED\_INT | 表示列类型为长度大于64位的数字。  **起始版本：** 18 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Value\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_Data_Value *OH_Value_Create(void)
```

**描述**

创建[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例，用于储存单条键值对数据。

**起始版本：** 18

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) | 执行成功时返回指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。否则返回nullptr。  使用完成后，必须通过[OH\_Value\_Destroy](capi-oh-data-value-h.md#oh_value_destroy)接口释放内存。 |

### OH\_Value\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_Destroy(OH_Data_Value *value)
```

**描述**

销毁[OH\_Data\_Value](capi-rdb-oh-data-value.md)对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Value\_PutNull()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_PutNull(OH_Data_Value *value)
```

**描述**

添加空数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Value\_PutInt()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_PutInt(OH_Data_Value *value, int64_t val)
```

**描述**

添加整型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| int64\_t val | 表示整型数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Value\_PutReal()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_PutReal(OH_Data_Value *value, double val)
```

**描述**

添加REAL类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| double val | 表示REAL类型数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Value\_PutText()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_PutText(OH_Data_Value *value, const char *val)
```

**描述**

添加字符串类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| const char \*val | 表示字符串类型数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Value\_PutBlob()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_PutBlob(OH_Data_Value *value, const unsigned char *val, size_t length)
```

**描述**

添加BLOB类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| const unsigned char \*val | 表示BLOB类型数据。 |
| size\_t length | 该参数是输入参数，表示开发者传入的BLOB类型数据的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Value\_PutAsset()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_PutAsset(OH_Data_Value *value, const Data_Asset *val)
```

**描述**

添加ASSET类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| const [Data\_Asset](capi-rdb-data-asset.md) \*val | 表示指向[Data\_Asset](capi-rdb-data-asset.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Value\_PutAssets()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_PutAssets(OH_Data_Value *value, const Data_Asset * const * val, size_t length)
```

**描述**

添加ASSETS类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| const [Data\_Asset](capi-rdb-data-asset.md) \* const \* val | 表示指向[Data\_Asset](capi-rdb-data-asset.md)对象的指针。 |
| size\_t length | 该参数是输入参数，表示开发者传入的[Data\_Asset](capi-rdb-data-asset.md)对象数组元素的个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Value\_PutFloatVector()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_PutFloatVector(OH_Data_Value *value, const float *val, size_t length)
```

**描述**

添加float数组类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| const float \*val | 表示指向float数组对象的指针。 |
| size\_t length | 该参数是输入参数，表示开发者传入的表示float数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Value\_PutUnlimitedInt()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_PutUnlimitedInt(OH_Data_Value *value, int sign, const uint64_t *trueForm, size_t length)
```

**描述**

添加任意长度的整型数组数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| int sign | 表示正负数，0表示正整数，1表示负整数。 |
| const uint64\_t \*trueForm | 表示指向整型数组的指针。 |
| size\_t length | 该参数是输入参数，表示开发者传入的表示整型数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Value\_GetType()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_GetType(OH_Data_Value *value, OH_ColumnType *type)
```

**描述**

获取数据类型。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| [OH\_ColumnType](capi-oh-data-value-h.md#oh_columntype) \*type | 一个输出参数，表示数据类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Value\_IsNull()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_IsNull(OH_Data_Value *value, bool *val)
```

**描述**

检查数据是否为空。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| bool \*val | 一个输出参数，true表示空，false表示不为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Value\_GetInt()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_GetInt(OH_Data_Value *value, int64_t *val)
```

**描述**

获取整型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| int64\_t \*val | 一个输出参数，表示指向整型数据的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |

### OH\_Value\_GetReal()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_GetReal(OH_Data_Value *value, double *val)
```

**描述**

获取REAL类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| double \*val | 一个输出参数，表示指向REAL类型数据的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |

### OH\_Value\_GetText()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_GetText(OH_Data_Value *value, const char **val)
```

**描述**

获取字符串类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| const char \*\*val | 一个输出参数，表示指向字符串类型数据的指针。  无需申请内存和释放内存。  val的生命周期遵循value中index的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |

### OH\_Value\_GetBlob()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_GetBlob(OH_Data_Value *value, const uint8_t **val, size_t *length)
```

**描述**

获取BLOB类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| const uint8\_t \*\*val | 一个输出参数，表示指向BLOB类型数据的指针。  无需申请内存和释放内存。  val的生命周期遵循value中index的值。 |
| size\_t \*length | 该参数是输出参数，表示BLOB类型数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |

### OH\_Value\_GetAsset()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_GetAsset(OH_Data_Value *value, Data_Asset *val)
```

**描述**

获取ASSET类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| [Data\_Asset](capi-rdb-data-asset.md) \*val | 表示指向[Data\_Asset](capi-rdb-data-asset.md)对象的指针。  需要申请数据内存。  此函数仅填充数据。否则执行失败。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |

### OH\_Value\_GetAssetsCount()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_GetAssetsCount(OH_Data_Value *value, size_t *length)
```

**描述**

获取ASSETS类型数据的大小。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| size\_t \*length | 该参数是输出参数，表示ASSETS类型数据的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |

### OH\_Value\_GetAssets()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_GetAssets(OH_Data_Value *value, Data_Asset **val, size_t inLen, size_t *outLen)
```

**描述**

获取ASSETS类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| [Data\_Asset](capi-rdb-data-asset.md) \*\*val | 表示指向[Data\_Asset](capi-rdb-data-asset.md)对象的指针。  需要申请数据内存。  此函数仅填充数据。否则执行失败。 |
| size\_t inLen | 表示val的大小。可以通过[OH\_Values\_GetAssetsCount](capi-oh-data-values-h.md#oh_values_getassetscount)获取。 |
| size\_t \*outLen | 一个输出参数，表示实际获取的数据大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |

### OH\_Value\_GetFloatVectorCount()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_GetFloatVectorCount(OH_Data_Value *value, size_t *length)
```

**描述**

获取float数组类型数据的大小。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| size\_t \*length | 该参数是输出参数，表示float数组类型数据的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示参数无效。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |

### OH\_Value\_GetFloatVector()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_GetFloatVector(OH_Data_Value *value, float *val, size_t inLen, size_t *outLen)
```

**描述**

获取float数组类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| float \*val | 表示指向float数组的指针。  需要申请数据内存。  此函数仅填充数据。否则执行失败。 |
| size\_t inLen | 表示val的大小。可以通过[OH\_Values\_GetFloatVectorCount](capi-oh-data-values-h.md#oh_values_getfloatvectorcount)获取。 |
| size\_t \*outLen | 一个输出参数，表示实际获取的数据大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |

### OH\_Value\_GetUnlimitedIntBand()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_GetUnlimitedIntBand(OH_Data_Value *value, size_t *length)
```

**描述**

获取任意长度的整型数据的大小。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| size\_t \*length | 该参数是输出参数，表示整型数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |

### OH\_Value\_GetUnlimitedInt()

PhonePC/2in1TabletTVWearable

```
1. int OH_Value_GetUnlimitedInt(OH_Data_Value *value, int *sign, uint64_t *trueForm, size_t inLen, size_t *outLen)
```

**描述**

获取任意长度的整型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Data\_Value](capi-rdb-oh-data-value.md) \*value | 表示指向[OH\_Data\_Value](capi-rdb-oh-data-value.md)实例的指针。 |
| int \*sign | 一个输出参数，表示正负数，0表示正整数，1表示负整数。 |
| uint64\_t \*trueForm | 表示指向整型数组的指针。  需要申请数据内存。  此函数仅填充数据。否则执行失败。 |
| size\_t inLen | 表示trueForm的大小。可以通过[OH\_Values\_GetUnlimitedIntBand](capi-oh-data-values-h.md#oh_values_getunlimitedintband)获取。 |
| size\_t \*outLen | 一个输出参数，表示实际获取的数据大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。  返回RDB\_E\_DATA\_TYPE\_NULL表示存储数据为空。  返回RDB\_E\_TYPE\_MISMATCH表示数据类型不匹配。 |
