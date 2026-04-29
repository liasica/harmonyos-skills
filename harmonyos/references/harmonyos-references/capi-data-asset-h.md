---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-data-asset-h
title: data_asset.h
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 头文件 > data_asset.h
category: harmonyos-references
scraped_at: 2026-04-29T13:49:41+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:c996e5d09cd2ae67d386324c5b1bb3fe96dbbb4bba19285c5eb45dc959b07947
---

## 概述

PhonePC/2in1TabletTVWearable

提供资产类型数据结构。

资产是指一种可以在数据管理中使用的数据结构，可以存储及查询一个文件的名称、绝对路径、相对路径、创建时间、修改时间、状态、占用空间等属性。

**引用文件：** <database/data/data\_asset.h>

**库：** libnative\_rdb\_ndk.z.so

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 11

**相关模块：** [RDB](capi-rdb.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Data\_Asset](capi-rdb-data-asset.md) | Data\_Asset | 表示资产附件类型的数据。  提供资产附件的信息。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Data\_AssetStatus](capi-data-asset-h.md#data_assetstatus) | Data\_AssetStatus | 资产状态值类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int OH\_Data\_Asset\_SetName(Data\_Asset \*asset, const char \*name)](capi-data-asset-h.md#oh_data_asset_setname) | 设置资产类型数据的名称。 |
| [int OH\_Data\_Asset\_SetUri(Data\_Asset \*asset, const char \*uri)](capi-data-asset-h.md#oh_data_asset_seturi) | 设置资产类型数据在系统里的绝对路径，即URI。 |
| [int OH\_Data\_Asset\_SetPath(Data\_Asset \*asset, const char \*path)](capi-data-asset-h.md#oh_data_asset_setpath) | 设置资产类型数据在应用沙箱里的相对路径。 |
| [int OH\_Data\_Asset\_SetCreateTime(Data\_Asset \*asset, int64\_t createTime)](capi-data-asset-h.md#oh_data_asset_setcreatetime) | 设置资产类型数据创建的时间。 |
| [int OH\_Data\_Asset\_SetModifyTime(Data\_Asset \*asset, int64\_t modifyTime)](capi-data-asset-h.md#oh_data_asset_setmodifytime) | 设置资产类型数据最后修改的时间。 |
| [int OH\_Data\_Asset\_SetSize(Data\_Asset \*asset, size\_t size)](capi-data-asset-h.md#oh_data_asset_setsize) | 设置资产类型数据占用空间的大小。 |
| [int OH\_Data\_Asset\_SetStatus(Data\_Asset \*asset, Data\_AssetStatus status)](capi-data-asset-h.md#oh_data_asset_setstatus) | 设置资产类型数据的状态码。 |
| [int OH\_Data\_Asset\_GetName(Data\_Asset \*asset, char \*name, size\_t \*length)](capi-data-asset-h.md#oh_data_asset_getname) | 获取资产类型数据的名称。 |
| [int OH\_Data\_Asset\_GetUri(Data\_Asset \*asset, char \*uri, size\_t \*length)](capi-data-asset-h.md#oh_data_asset_geturi) | 获取资产类型数据的绝对路径。 |
| [int OH\_Data\_Asset\_GetPath(Data\_Asset \*asset, char \*path, size\_t \*length)](capi-data-asset-h.md#oh_data_asset_getpath) | 获取资产类型数据的相对路径。 |
| [int OH\_Data\_Asset\_GetCreateTime(Data\_Asset \*asset, int64\_t \*createTime)](capi-data-asset-h.md#oh_data_asset_getcreatetime) | 获取资产类型数据的创建时间。 |
| [int OH\_Data\_Asset\_GetModifyTime(Data\_Asset \*asset, int64\_t \*modifyTime)](capi-data-asset-h.md#oh_data_asset_getmodifytime) | 获取资产类型数据的最后修改的时间。 |
| [int OH\_Data\_Asset\_GetSize(Data\_Asset \*asset, size\_t \*size)](capi-data-asset-h.md#oh_data_asset_getsize) | 获取资产类型数据占用空间的大小。 |
| [int OH\_Data\_Asset\_GetStatus(Data\_Asset \*asset, Data\_AssetStatus \*status)](capi-data-asset-h.md#oh_data_asset_getstatus) | 获取资产类型数据的状态码。 |
| [Data\_Asset \*OH\_Data\_Asset\_CreateOne(void)](capi-data-asset-h.md#oh_data_asset_createone) | 创建一个[Data\_Asset](capi-rdb-data-asset.md)类型实例。 |
| [int OH\_Data\_Asset\_DestroyOne(Data\_Asset \*asset)](capi-data-asset-h.md#oh_data_asset_destroyone) | 销毁[Data\_Asset](capi-rdb-data-asset.md) 对象并回收该对象占用的内存。 |
| [Data\_Asset \*\*OH\_Data\_Asset\_CreateMultiple(uint32\_t count)](capi-data-asset-h.md#oh_data_asset_createmultiple) | 创建指定数量的[Data\_Asset](capi-rdb-data-asset.md)类型实例。 |
| [int OH\_Data\_Asset\_DestroyMultiple(Data\_Asset \*\*assets, uint32\_t count)](capi-data-asset-h.md#oh_data_asset_destroymultiple) | 销毁多个[Data\_Asset](capi-rdb-data-asset.md) 对象并回收该对象占用的内存。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### Data\_AssetStatus

PhonePC/2in1TabletTVWearable

```
1. enum Data_AssetStatus
```

**描述**

资产状态值类型。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| ASSET\_NULL = 0 | 表示资产为空。 |
| ASSET\_NORMAL | 表示资产状态正常。 |
| ASSET\_INSERT | 表示资产需要插入到云端。 |
| ASSET\_UPDATE | 表示资产需要更新到云端。 |
| ASSET\_DELETE | 表示资产需要在云端删除。 |
| ASSET\_ABNORMAL | 表示资产状态异常。 |
| ASSET\_DOWNLOADING | 表示资产正在下载到本地设备。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Data\_Asset\_SetName()

PhonePC/2in1TabletTVWearable

```
1. int OH_Data_Asset_SetName(Data_Asset *asset, const char *name)
```

**描述**

设置资产类型数据的名称。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Data\_Asset](capi-rdb-data-asset.md) \*asset | 表示指向[Data\_Asset](capi-rdb-data-asset.md)实例的指针。 |
| const char \*name | 表示要设置的名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回特定的错误码值。详细信息可以查看[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Data\_Asset\_SetUri()

PhonePC/2in1TabletTVWearable

```
1. int OH_Data_Asset_SetUri(Data_Asset *asset, const char *uri)
```

**描述**

设置资产类型数据在系统里的绝对路径，即URI。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Data\_Asset](capi-rdb-data-asset.md) \*asset | 表示指向[Data\_Asset](capi-rdb-data-asset.md)实例的指针。 |
| const char \*uri | 表示要设置的URI。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回特定的错误码值。详细信息可以查看[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Data\_Asset\_SetPath()

PhonePC/2in1TabletTVWearable

```
1. int OH_Data_Asset_SetPath(Data_Asset *asset, const char *path)
```

**描述**

设置资产类型数据在应用沙箱里的相对路径。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Data\_Asset](capi-rdb-data-asset.md) \*asset | 表示指向[Data\_Asset](capi-rdb-data-asset.md)实例的指针。 |
| const char \*path | 表示要设置的相对路径。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回特定的错误码值。详细信息可以查看[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Data\_Asset\_SetCreateTime()

PhonePC/2in1TabletTVWearable

```
1. int OH_Data_Asset_SetCreateTime(Data_Asset *asset, int64_t createTime)
```

**描述**

设置资产类型数据创建的时间。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Data\_Asset](capi-rdb-data-asset.md) \*asset | 表示指向[Data\_Asset](capi-rdb-data-asset.md)实例的指针。 |
| int64\_t createTime | 表示要设置的创建时间。无特定单位。开发者可自行指定。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回特定的错误码值。详细信息可以查看[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Data\_Asset\_SetModifyTime()

PhonePC/2in1TabletTVWearable

```
1. int OH_Data_Asset_SetModifyTime(Data_Asset *asset, int64_t modifyTime)
```

**描述**

设置资产类型数据最后修改的时间。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Data\_Asset](capi-rdb-data-asset.md) \*asset | 表示指向[Data\_Asset](capi-rdb-data-asset.md)实例的指针。 |
| int64\_t modifyTime | 表示要设置的最后修改的时间。无特定单位。开发者可自行指定。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回特定的错误码值。详细信息可以查看[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Data\_Asset\_SetSize()

PhonePC/2in1TabletTVWearable

```
1. int OH_Data_Asset_SetSize(Data_Asset *asset, size_t size)
```

**描述**

设置资产类型数据占用空间的大小。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Data\_Asset](capi-rdb-data-asset.md) \*asset | 表示指向[Data\_Asset](capi-rdb-data-asset.md)实例的指针。 |
| size\_t size | 表示要设置的占用空间的大小（单位为字节（Byte），取值为非负整数）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回特定的错误码值。详细信息可以查看[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Data\_Asset\_SetStatus()

PhonePC/2in1TabletTVWearable

```
1. int OH_Data_Asset_SetStatus(Data_Asset *asset, Data_AssetStatus status)
```

**描述**

设置资产类型数据的状态码。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Data\_Asset](capi-rdb-data-asset.md) \*asset | 表示指向[Data\_Asset](capi-rdb-data-asset.md)实例的指针。 |
| [Data\_AssetStatus](capi-data-asset-h.md#data_assetstatus) status | 表示需要设置的状态码。详细信息可以查看[Data\_AssetStatus](capi-data-asset-h.md#data_assetstatus)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回特定的错误码值。详细信息可以查看[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Data\_Asset\_GetName()

PhonePC/2in1TabletTVWearable

```
1. int OH_Data_Asset_GetName(Data_Asset *asset, char *name, size_t *length)
```

**描述**

获取资产类型数据的名称。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Data\_Asset](capi-rdb-data-asset.md) \*asset | 表示指向[Data\_Asset](capi-rdb-data-asset.md)实例的指针。 |
| char \*name | 该参数是输出参数，资产类型数据的名称会以字符串形式写入该变量。 |
| size\_t \*length | 表示name的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回特定的错误码值。详细信息可以查看[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。  返回RDB\_ERR表示函数执行异常。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Data\_Asset\_GetUri()

PhonePC/2in1TabletTVWearable

```
1. int OH_Data_Asset_GetUri(Data_Asset *asset, char *uri, size_t *length)
```

**描述**

获取资产类型数据的绝对路径。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Data\_Asset](capi-rdb-data-asset.md) \*asset | 表示指向[Data\_Asset](capi-rdb-data-asset.md)实例的指针。 |
| char \*uri | 参数是输出参数，资产类型数据的绝对路径会以字符串形式写入该变量。 |
| size\_t \*length | 表示uri的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回特定的错误码值。详细信息可以查看[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。  返回RDB\_ERR表示函数执行异常。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Data\_Asset\_GetPath()

PhonePC/2in1TabletTVWearable

```
1. int OH_Data_Asset_GetPath(Data_Asset *asset, char *path, size_t *length)
```

**描述**

获取资产类型数据的相对路径。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Data\_Asset](capi-rdb-data-asset.md) \*asset | 表示指向[Data\_Asset](capi-rdb-data-asset.md)实例的指针。 |
| char \*path | 参数是输出参数，资产类型数据的相对路径会以字符串形式写入该变量。 |
| size\_t \*length | 表示path的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回特定的错误码值。详细信息可以查看[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。  返回RDB\_ERR表示函数执行异常。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Data\_Asset\_GetCreateTime()

PhonePC/2in1TabletTVWearable

```
1. int OH_Data_Asset_GetCreateTime(Data_Asset *asset, int64_t *createTime)
```

**描述**

获取资产类型数据的创建时间。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Data\_Asset](capi-rdb-data-asset.md) \*asset | 表示指向[Data\_Asset](capi-rdb-data-asset.md)实例的指针。 |
| int64\_t \*createTime | 参数是输出参数，资产类型数据的创建时间会以int64\_t形式写入该变量。无特定单位。开发者可自行指定。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回特定的错误码值。详细信息可以查看[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。  返回RDB\_ERR表示函数执行异常。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

**参考：**

Data\_Asset

### OH\_Data\_Asset\_GetModifyTime()

PhonePC/2in1TabletTVWearable

```
1. int OH_Data_Asset_GetModifyTime(Data_Asset *asset, int64_t *modifyTime)
```

**描述**

获取资产类型数据的最后修改的时间。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Data\_Asset](capi-rdb-data-asset.md) \*asset | 表示指向[Data\_Asset](capi-rdb-data-asset.md)实例的指针。 |
| int64\_t \*modifyTime | 参数是输出参数，资产类型数据的最后修改时间会以int64\_t形式写入该变量。无特定单位。开发者可自行指定。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回特定的错误码值。详细信息可以查看[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。  返回RDB\_ERR表示函数执行异常。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Data\_Asset\_GetSize()

PhonePC/2in1TabletTVWearable

```
1. int OH_Data_Asset_GetSize(Data_Asset *asset, size_t *size)
```

**描述**

获取资产类型数据占用空间的大小。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Data\_Asset](capi-rdb-data-asset.md) \*asset | 表示指向[Data\_Asset](capi-rdb-data-asset.md)实例的指针。 |
| size\_t \*size | 参数是输出参数，资产类型数据的占用空间大小会以size\_t形式写入该变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回特定的错误码值。详细信息可以查看[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。  返回RDB\_ERR表示函数执行异常。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Data\_Asset\_GetStatus()

PhonePC/2in1TabletTVWearable

```
1. int OH_Data_Asset_GetStatus(Data_Asset *asset, Data_AssetStatus *status)
```

**描述**

获取资产类型数据的状态码。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Data\_Asset](capi-rdb-data-asset.md) \*asset | 表示指向[Data\_Asset](capi-rdb-data-asset.md)实例的指针。 |
| [Data\_AssetStatus](capi-data-asset-h.md#data_assetstatus) \*status | 参数是输出参数，资产类型数据的状态码会以[Data\_AssetStatus](capi-data-asset-h.md#data_assetstatus)形式写入该变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回特定的错误码值。详细信息可以查看[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。  返回RDB\_OK表示成功。  返回RDB\_E\_INVALID\_ARGS表示无效参数。 |

### OH\_Data\_Asset\_CreateOne()

PhonePC/2in1TabletTVWearable

```
1. Data_Asset *OH_Data_Asset_CreateOne(void)
```

**描述**

创建一个[Data\_Asset](capi-rdb-data-asset.md)类型实例。

**起始版本：** 11

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Data\_Asset](capi-rdb-data-asset.md) | 创建成功则返回一个指向[Data\_Asset](capi-rdb-data-asset.md)结构体实例的指针，否则返回NULL。  使用完成后，必须通过[OH\_Data\_Asset\_DestroyOne](capi-data-asset-h.md#oh_data_asset_destroyone)接口释放内存。 |

### OH\_Data\_Asset\_DestroyOne()

PhonePC/2in1TabletTVWearable

```
1. int OH_Data_Asset_DestroyOne(Data_Asset *asset)
```

**描述**

销毁[Data\_Asset](capi-rdb-data-asset.md) 对象并回收该对象占用的内存。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Data\_Asset](capi-rdb-data-asset.md) \*asset | 表示指向[Data\_Asset](capi-rdb-data-asset.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，成功时返回RDB\_OK，出错时返回对应的错误码。详细信息可以查看[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。 |

### OH\_Data\_Asset\_CreateMultiple()

PhonePC/2in1TabletTVWearable

```
1. Data_Asset **OH_Data_Asset_CreateMultiple(uint32_t count)
```

**描述**

创建指定数量的[Data\_Asset](capi-rdb-data-asset.md)类型实例。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t count | 代表创建的资产类型数据的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Data\_Asset](capi-rdb-data-asset.md) | 创建成功则返回一个指向[Data\_Asset](capi-rdb-data-asset.md)结构体实例的指针，否则返回NULL。  使用完成后，必须通过[OH\_Data\_Asset\_DestroyMultiple](capi-data-asset-h.md#oh_data_asset_destroymultiple)接口释放内存。 |

### OH\_Data\_Asset\_DestroyMultiple()

PhonePC/2in1TabletTVWearable

```
1. int OH_Data_Asset_DestroyMultiple(Data_Asset **assets, uint32_t count)
```

**描述**

销毁多个[Data\_Asset](capi-rdb-data-asset.md) 对象并回收该对象占用的内存。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Data\_Asset](capi-rdb-data-asset.md) \*\*assets | 表示指向[Data\_Asset](capi-rdb-data-asset.md)实例的指针。 |
| uint32\_t count | 代表需要销毁的[Data\_Asset](capi-rdb-data-asset.md)类型对象的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，成功时返回RDB\_OK，出错时返回对应的错误码。详细信息可以查看[OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode)。 |
