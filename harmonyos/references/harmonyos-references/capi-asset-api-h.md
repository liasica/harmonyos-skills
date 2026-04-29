---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-asset-api-h
title: asset_api.h
breadcrumb: API参考 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > C API > 头文件 > asset_api.h
category: harmonyos-references
scraped_at: 2026-04-29T13:57:17+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:3b589929521cc6df585ab67330be16a6025d376241aac24b8748da59dd7b8bce
---

## 概述

PhonePC/2in1TabletTVWearable

声明用于访问关键资产的接口。

**引用文件：** <asset/asset\_api.h>

**库：** libasset\_ndk.z.so

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 11

**相关模块：** [AssetApi](capi-assetapi.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int32\_t OH\_Asset\_Add(const Asset\_Attr \*attributes, uint32\_t attrCnt)](capi-asset-api-h.md#oh_asset_add) | 新增一条关键资产。  如果要设置[Asset\_Tag](capi-asset-type-h.md#asset_tag).ASSET\_TAG\_IS\_PERSISTENT属性，需要申请ohos.permission.STORE\_PERSISTENT\_DATA权限，申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。 |
| [int32\_t OH\_Asset\_Remove(const Asset\_Attr \*query, uint32\_t queryCnt)](capi-asset-api-h.md#oh_asset_remove) | 删除符合条件的一条或多条关键资产。 |
| [int32\_t OH\_Asset\_Update(const Asset\_Attr \*query, uint32\_t queryCnt, const Asset\_Attr \*attributesToUpdate, uint32\_t updateCnt)](capi-asset-api-h.md#oh_asset_update) | 更新符合条件的一条关键资产。 |
| [int32\_t OH\_Asset\_PreQuery(const Asset\_Attr \*query, uint32\_t queryCnt, Asset\_Blob \*challenge)](capi-asset-api-h.md#oh_asset_prequery) | 查询的预处理，用于需要用户认证的关键资产。 |
| [int32\_t OH\_Asset\_Query(const Asset\_Attr \*query, uint32\_t queryCnt, Asset\_ResultSet \*resultSet)](capi-asset-api-h.md#oh_asset_query) | 查询一条或多条符合条件的关键资产。 |
| [int32\_t OH\_Asset\_PostQuery(const Asset\_Attr \*handle, uint32\_t handleCnt)](capi-asset-api-h.md#oh_asset_postquery) | 查询的后置处理，用于需要用户认证的关键资产。 |
| [int32\_t OH\_Asset\_QuerySyncResult(const Asset\_Attr \*query, uint32\_t queryCnt, Asset\_SyncResult \*syncResult)](capi-asset-api-h.md#oh_asset_querysyncresult) | 查询关键资产的同步结果。 |
| [Asset\_Attr \*OH\_Asset\_ParseAttr(const Asset\_Result \*result, Asset\_Tag tag)](capi-asset-api-h.md#oh_asset_parseattr) | 解析查询结果，并获取指定的属性值。 |
| [void OH\_Asset\_FreeBlob(Asset\_Blob \*blob)](capi-asset-api-h.md#oh_asset_freeblob) | 释放挑战值所占用的内存。 |
| [void OH\_Asset\_FreeResultSet(Asset\_ResultSet \*resultSet)](capi-asset-api-h.md#oh_asset_freeresultset) | 释放查询结果所占用的内存。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Asset\_Add()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Asset_Add(const Asset_Attr *attributes, uint32_t attrCnt)
```

**描述**

新增一条关键资产。

如果要设置[Asset\_Tag](capi-asset-type-h.md#asset_tag).ASSET\_TAG\_IS\_PERSISTENT属性，需要申请ohos.permission.STORE\_PERSISTENT\_DATA权限，申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Asset\_Attr](capi-assettype-asset-attr.md) \*attributes | 待新增关键资产的属性集合。 |
| uint32\_t attrCnt | 待新增关键资产的属性数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [Asset\_ResultCode](capi-asset-type-h.md#asset_resultcode):  ASSET\_SUCCESS = 0：操作成功。  ASSET\_PERMISSION\_DENIED = 201：调用方不是一个系统应用。  ASSET\_INVALID\_ARGUMENT = 401：参数错误。 可能原因:  1. 必选参数未指定。  2. 参数类型错误。  3. 参数校验失败。  ASSET\_SERVICE\_UNAVAILABLE = 24000001：关键资产服务不可用。  ASSET\_DUPLICATED = 24000003：关键资产已存在。  ASSET\_STATUS\_MISMATCH = 24000005：锁屏状态不匹配。  ASSET\_OUT\_OF\_MEMORY = 24000006：系统内存不足。  ASSET\_DATA\_CORRUPTED = 24000007：关键资产损坏。  ASSET\_DATABASE\_ERROR = 24000008：数据库操作失败。  ASSET\_CRYPTO\_ERROR = 24000009：算法库操作失败。  ASSET\_IPC\_ERROR = 24000010：进程通信错误。  ASSET\_BMS\_ERROR = 24000011：包管理服务异常。  ASSET\_ACCOUNT\_ERROR = 24000012：账号系统服务异常。  ASSET\_ACCESS\_TOKEN\_ERROR = 24000013：访问控制服务异常。  ASSET\_FILE\_OPERATION\_ERROR = 24000014：文件操作失败。  ASSET\_GET\_SYSTEM\_TIME\_ERROR = 24000015：获取系统时间失败。 |

### OH\_Asset\_Remove()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Asset_Remove(const Asset_Attr *query, uint32_t queryCnt)
```

**描述**

删除符合条件的一条或多条关键资产。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Asset\_Attr](capi-assettype-asset-attr.md) \*query | 待删除关键资产的搜索条件。 |
| uint32\_t queryCnt | 待删除关键资产搜索条件的个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [Asset\_ResultCode](capi-asset-type-h.md#asset_resultcode):  ASSET\_SUCCESS = 0：操作成功。  ASSET\_INVALID\_ARGUMENT = 401：参数错误。 可能原因:  1. 参数类型错误。  2. 参数校验失败。  ASSET\_SERVICE\_UNAVAILABLE = 24000001：关键资产服务不可用。  ASSET\_NOT\_FOUND = 24000002：未找到关键资产。  ASSET\_OUT\_OF\_MEMORY = 24000006：系统内存不足。  ASSET\_DATA\_CORRUPTED = 24000007：关键资产损坏。  ASSET\_DATABASE\_ERROR = 24000008：数据库操作失败。  ASSET\_IPC\_ERROR = 24000010：进程通信错误。  ASSET\_BMS\_ERROR = 24000011：包管理服务异常。  ASSET\_ACCOUNT\_ERROR = 24000012：账号系统服务异常。  ASSET\_ACCESS\_TOKEN\_ERROR = 24000013：访问控制服务异常。  ASSET\_GET\_SYSTEM\_TIME\_ERROR = 24000015：获取系统时间失败。 |

### OH\_Asset\_Update()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Asset_Update(const Asset_Attr *query, uint32_t queryCnt,const Asset_Attr *attributesToUpdate, uint32_t updateCnt)
```

**描述**

更新符合条件的一条关键资产。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Asset\_Attr](capi-assettype-asset-attr.md) \*query | 待更新关键资产的搜索条件。 |
| uint32\_t queryCnt | 待更新关键资产搜索条件的个数。 |
| const [Asset\_Attr](capi-assettype-asset-attr.md) \*attributesToUpdate | 待更新关键资产的属性集合。 |
| uint32\_t updateCnt | 待更新关键资产的属性数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [Asset\_ResultCode](capi-asset-type-h.md#asset_resultcode):  ASSET\_SUCCESS = 0：操作成功。  ASSET\_INVALID\_ARGUMENT = 401：参数错误。 可能原因:  1. 必选参数未指定。  2. 参数类型错误。  3. 参数校验失败。  ASSET\_SERVICE\_UNAVAILABLE = 24000001：关键资产服务不可用。  ASSET\_NOT\_FOUND = 24000002：未找到关键资产。  ASSET\_STATUS\_MISMATCH = 24000005：锁屏状态不匹配。  ASSET\_OUT\_OF\_MEMORY = 24000006：系统内存不足。  ASSET\_DATA\_CORRUPTED = 24000007：关键资产损坏。  ASSET\_DATABASE\_ERROR = 24000008：数据库操作失败。  ASSET\_CRYPTO\_ERROR = 24000009：算法库操作失败。  ASSET\_IPC\_ERROR = 24000010：进程通信错误。  ASSET\_BMS\_ERROR = 24000011：包管理服务异常。  ASSET\_ACCOUNT\_ERROR = 24000012：账号系统服务异常。  ASSET\_ACCESS\_TOKEN\_ERROR = 24000013：访问控制服务异常。  ASSET\_GET\_SYSTEM\_TIME\_ERROR = 24000015：获取系统时间失败。 |

### OH\_Asset\_PreQuery()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Asset_PreQuery(const Asset_Attr *query, uint32_t queryCnt, Asset_Blob *challenge)
```

**描述**

查询的预处理，用于需要用户认证的关键资产。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Asset\_Attr](capi-assettype-asset-attr.md) \*query | 关键资产的查询条件。 |
| uint32\_t queryCnt | 关键资产查询条件的个数。 |
| [Asset\_Blob](capi-assettype-asset-blob.md) \*challenge | 挑战值，在后续调用[OH\_Asset\_Query](capi-asset-api-h.md#oh_asset_query)时使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [Asset\_ResultCode](capi-asset-type-h.md#asset_resultcode):  ASSET\_SUCCESS = 0：操作成功。  ASSET\_INVALID\_ARGUMENT = 401：参数错误。 可能原因:  1. 参数类型错误。  2. 参数校验失败。  ASSET\_SERVICE\_UNAVAILABLE = 24000001：关键资产服务不可用。  ASSET\_NOT\_FOUND = 24000002：未找到关键资产。  ASSET\_STATUS\_MISMATCH = 24000005：锁屏状态不匹配。  ASSET\_OUT\_OF\_MEMORY = 24000006：系统内存不足。  ASSET\_DATA\_CORRUPTED = 24000007：关键资产损坏。  ASSET\_DATABASE\_ERROR = 24000008：数据库操作失败。  ASSET\_CRYPTO\_ERROR = 24000009：算法库操作失败。  ASSET\_IPC\_ERROR = 24000010：进程通信错误。  ASSET\_BMS\_ERROR = 24000011：包管理服务异常。  ASSET\_ACCOUNT\_ERROR = 24000012：账号系统服务异常。  ASSET\_ACCESS\_TOKEN\_ERROR = 24000013：访问控制服务异常。  ASSET\_LIMIT\_EXCEEDED = 24000016：缓存数量超限。  ASSET\_UNSUPPORTED = 24000017：该子功能不支持。 |

### OH\_Asset\_Query()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Asset_Query(const Asset_Attr *query, uint32_t queryCnt, Asset_ResultSet *resultSet)
```

**描述**

查询一条或多条符合条件的关键资产。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Asset\_Attr](capi-assettype-asset-attr.md) \*query | 关键资产的查询条件。 |
| uint32\_t queryCnt | 关键资产查询条件的个数。 |
| [Asset\_ResultSet](capi-assettype-asset-resultset.md) \*resultSet | 查询结果列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [Asset\_ResultCode](capi-asset-type-h.md#asset_resultcode):  ASSET\_SUCCESS = 0：操作成功。  ASSET\_INVALID\_ARGUMENT = 401：参数错误。 可能原因:  1. 参数类型错误。  2. 参数校验失败。  ASSET\_SERVICE\_UNAVAILABLE = 24000001：关键资产服务不可用。  ASSET\_NOT\_FOUND = 24000002：未找到关键资产。  ASSET\_ACCESS\_DENIED = 24000004：访问被拒绝。  ASSET\_STATUS\_MISMATCH = 24000005：锁屏状态不匹配。  ASSET\_OUT\_OF\_MEMORY = 24000006：系统内存不足。  ASSET\_DATA\_CORRUPTED = 24000007：关键资产损坏。  ASSET\_DATABASE\_ERROR = 24000008：数据库操作失败。  ASSET\_CRYPTO\_ERROR = 24000009：算法库操作失败。  ASSET\_IPC\_ERROR = 24000010：进程通信错误。  ASSET\_BMS\_ERROR = 24000011：包管理服务异常。  ASSET\_ACCOUNT\_ERROR = 24000012：账号系统服务异常。  ASSET\_ACCESS\_TOKEN\_ERROR = 24000013：访问控制服务异常。  ASSET\_UNSUPPORTED = 24000017：该子功能不支持。 |

### OH\_Asset\_PostQuery()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Asset_PostQuery(const Asset_Attr *handle, uint32_t handleCnt)
```

**描述**

查询的后置处理，用于需要用户认证的关键资产。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Asset\_Attr](capi-assettype-asset-attr.md) \*handle | 待处理的查询句柄，当前包含[OH\_Asset\_PreQuery](capi-asset-api-h.md#oh_asset_prequery)执行成功返回的挑战值。 |
| uint32\_t handleCnt | 句柄属性集合中元素的个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [Asset\_ResultCode](capi-asset-type-h.md#asset_resultcode):  ASSET\_SUCCESS = 0：操作成功。  ASSET\_INVALID\_ARGUMENT = 401：参数错误。 可能原因:  1. 必选参数未指定。  2. 参数类型错误。  3. 参数校验失败。  ASSET\_SERVICE\_UNAVAILABLE = 24000001：关键资产服务不可用。  ASSET\_OUT\_OF\_MEMORY = 24000006：系统内存不足。  ASSET\_IPC\_ERROR = 24000010：进程通信错误。  ASSET\_BMS\_ERROR = 24000011：包管理服务异常。  ASSET\_ACCOUNT\_ERROR = 24000012：账号系统服务异常。  ASSET\_ACCESS\_TOKEN\_ERROR = 24000013：访问控制服务异常。 |

### OH\_Asset\_QuerySyncResult()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Asset_QuerySyncResult(const Asset_Attr *query, uint32_t queryCnt, Asset_SyncResult *syncResult)
```

**描述**

查询关键资产的同步结果。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Asset\_Attr](capi-assettype-asset-attr.md) \*query | 关键资产同步结果的查询条件。 |
| uint32\_t queryCnt | 关键资产同步结果的查询条件个数。 |
| [Asset\_SyncResult](capi-assettype-asset-syncresult.md) \*syncResult | 查询到的关键资产同步结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [Asset\_ResultCode](capi-asset-type-h.md#asset_resultcode)：  ASSET\_SUCCESS = 0：操作成功。  ASSET\_SERVICE\_UNAVAILABLE = 24000001：关键资产服务不可用。  ASSET\_OUT\_OF\_MEMORY = 24000006：系统内存不足。  ASSET\_IPC\_ERROR = 24000010：进程通信错误。  ASSET\_BMS\_ERROR = 24000011：包管理服务异常。  ASSET\_ACCOUNT\_ERROR = 24000012：账号系统服务异常。  ASSET\_ACCESS\_TOKEN\_ERROR = 24000013：访问控制服务异常。  ASSET\_FILE\_OPERATION\_ERROR = 24000014：文件操作失败。  ASSET\_PARAM\_VERIFICATION\_FAILED = 24000018：参数校验失败。 |

### OH\_Asset\_ParseAttr()

PhonePC/2in1TabletTVWearable

```
1. Asset_Attr *OH_Asset_ParseAttr(const Asset_Result *result, Asset_Tag tag)
```

**描述**

解析查询结果，并获取指定的属性值。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Asset\_Result](capi-assettype-asset-result.md) \*result | 从[OH\_Asset\_Query](capi-asset-api-h.md#oh_asset_query)中获取的查询结果。 |
| [Asset\_Tag](capi-asset-type-h.md#asset_tag) tag | 待获取的属性标签。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Asset\_Attr](capi-assettype-asset-attr.md) | 如果操作成功，则以Asset\_Attr的形式返回属性，该属性不需要业务进行释放；否则返回NULL。 |

### OH\_Asset\_FreeBlob()

PhonePC/2in1TabletTVWearable

```
1. void OH_Asset_FreeBlob(Asset_Blob *blob)
```

**描述**

释放挑战值所占用的内存。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Asset\_Blob](capi-assettype-asset-blob.md) \*blob | 从[OH\_Asset\_PreQuery](capi-asset-api-h.md#oh_asset_prequery)获取的挑战值。 |

### OH\_Asset\_FreeResultSet()

PhonePC/2in1TabletTVWearable

```
1. void OH_Asset_FreeResultSet(Asset_ResultSet *resultSet)
```

**描述**

释放查询结果所占用的内存。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Asset\_ResultSet](capi-assettype-asset-resultset.md) \*resultSet | 从[OH\_Asset\_Query](capi-asset-api-h.md#oh_asset_query)得到的查询结果列表。 |
