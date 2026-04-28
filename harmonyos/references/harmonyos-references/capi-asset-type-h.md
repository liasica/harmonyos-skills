---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-asset-type-h
title: asset_type.h
breadcrumb: API参考 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > C API > 头文件 > asset_type.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:491e012d5b3e64d864e606f9ef67a29370af07de78c6d022ad7af4ccf5818763
---

## 概述

PhonePC/2in1TabletTVWearable

定义关键资产存储服务中通用的枚举值、数据结构和错误码。

**引用文件：** <asset/asset\_type.h>

**库：** libasset\_ndk.z.so

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 11

**相关模块：** [AssetType](capi-assettype.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Asset\_Blob](capi-assettype-asset-blob.md) | Asset\_Blob | 二进制数组类型，即不定长的字节数组。 |
| [Asset\_Value](capi-assettype-asset-value.md) | Asset\_Value | 关键资产属性内容。 |
| [Asset\_Attr](capi-assettype-asset-attr.md) | Asset\_Attr | 关键资产属性。 |
| [Asset\_Result](capi-assettype-asset-result.md) | Asset\_Result | 关键资产查询结果，用于定义一条关键资产。 |
| [Asset\_ResultSet](capi-assettype-asset-resultset.md) | Asset\_ResultSet | 关键资产查询结果集合，用于定义多条关键资产。 |
| [Asset\_SyncResult](capi-assettype-asset-syncresult.md) | Asset\_SyncResult | 关键资产同步结果。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Asset\_TagType](capi-asset-type-h.md#asset_tagtype) | Asset\_TagType | 关键资产属性的类型定义。 |
| [Asset\_Tag](capi-asset-type-h.md#asset_tag) | Asset\_Tag | 关键资产属性的名称。 |
| [Asset\_ResultCode](capi-asset-type-h.md#asset_resultcode) | Asset\_ResultCode | 调用ASSET返回的结果码。 |
| [Asset\_Accessibility](capi-asset-type-h.md#asset_accessibility) | Asset\_Accessibility | 基于锁屏状态的访问控制类型。 |
| [Asset\_AuthType](capi-asset-type-h.md#asset_authtype) | Asset\_AuthType | 关键资产支持的用户认证类型。 |
| [Asset\_SyncType](capi-asset-type-h.md#asset_synctype) | Asset\_SyncType | 关键资产支持的同步类型。 |
| [Asset\_WrapType](capi-asset-type-h.md#asset_wraptype) | Asset\_WrapType | 关键资产支持的加密导入导出类型。 |
| [Asset\_ConflictResolution](capi-asset-type-h.md#asset_conflictresolution) | Asset\_ConflictResolution | 新增关键资产时的冲突（如：别名相同）处理策略。 |
| [Asset\_ReturnType](capi-asset-type-h.md#asset_returntype) | Asset\_ReturnType | 关键资产查询返回的结果类型。 |
| [Asset\_OperationType](capi-asset-type-h.md#asset_operationtype) | Asset\_OperationType | 附属的操作类型。 |

### 宏定义

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| ASSET\_TAG\_TYPE\_MASK (0xF << 28) | 用于获取关键资产属性类型的掩码。  **起始版本：** 11 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### Asset\_TagType

PhonePC/2in1TabletTVWearable

```
1. enum Asset_TagType
```

**描述**

关键资产属性的类型定义。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| ASSET\_TYPE\_BOOL = 0x1 << 28 | 标识关键资产属性的类型是bool。 |
| ASSET\_TYPE\_NUMBER = 0x2 << 28 | 标识关键资产属性的类型是uint32\_t。 |
| ASSET\_TYPE\_BYTES = 0x3 << 28 | 标识关键资产属性的类型是byte数组。 |

### Asset\_Tag

PhonePC/2in1TabletTVWearable

```
1. enum Asset_Tag
```

**描述**

关键资产属性的名称。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| ASSET\_TAG\_SECRET = ASSET\_TYPE\_BYTES | 0x01 | 表示用户敏感数据，如口令、令牌等，其值为bytes类型。 |
| ASSET\_TAG\_ALIAS = ASSET\_TYPE\_BYTES | 0x02 | 表示一个关键资产的标识，其值为bytes类型。 |
| ASSET\_TAG\_ACCESSIBILITY = ASSET\_TYPE\_NUMBER | 0x03 | 表示关键资产何时可访问，其值为uint32\_t类型。 |
| ASSET\_TAG\_REQUIRE\_PASSWORD\_SET = ASSET\_TYPE\_BOOL | 0x04 | 表示关键资产是否在设备是否设置了锁屏密码时可用，其值为bool类型。 |
| ASSET\_TAG\_AUTH\_TYPE = ASSET\_TYPE\_NUMBER | 0x05 | 表示关键资产需要的用户认证类型，其值为uint32\_t类型。 |
| ASSET\_TAG\_AUTH\_VALIDITY\_PERIOD = ASSET\_TYPE\_NUMBER | 0x06 | 表示用户认证的有效时间，其值为uint32\_t类型，单位为秒。 |
| ASSET\_TAG\_AUTH\_CHALLENGE = ASSET\_TYPE\_BYTES | 0x07 | 表示认证时防重放用的挑战值，其值为bytes类型。 |
| ASSET\_TAG\_AUTH\_TOKEN = ASSET\_TYPE\_BYTES | 0x08 | 表示用户认证后获取到的认证令牌，其值为bytes类型。 |
| ASSET\_TAG\_SYNC\_TYPE = ASSET\_TYPE\_NUMBER | 0x10 | 表示关键资产的同步类型，其值为uint32\_t类型。 |
| ASSET\_TAG\_IS\_PERSISTENT = ASSET\_TYPE\_BOOL | 0x11 | 表示关键资产是否需持久化存储，其值为bool类型。  在调用OH\_Asset\_Add函数时传入该属性需要校验权限ohos.permission.STORE\_PERSISTENT\_DATA。 |
| ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_1 = ASSET\_TYPE\_BYTES | 0x20 | 表示一个用户可自定义传入的字段，该字段不可被更新，其值为bytes类型。 |
| ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_2 = ASSET\_TYPE\_BYTES | 0x21 | 表示一个用户可自定义传入的字段，该字段不可被更新，其值为bytes类型。 |
| ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_3 = ASSET\_TYPE\_BYTES | 0x22 | 表示一个用户可自定义传入的字段，该字段不可被更新，其值为bytes类型。 |
| ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_4 = ASSET\_TYPE\_BYTES | 0x23 | 表示一个用户可自定义传入的字段，该字段不可被更新，其值为bytes类型。 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1 = ASSET\_TYPE\_BYTES | 0x30 | 表示一个用户可自定义传入的字段，该字段可被更新，其值为bytes类型。 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_2 = ASSET\_TYPE\_BYTES | 0x31 | 表示一个用户可自定义传入的字段，该字段可被更新，其值为bytes类型。 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_3 = ASSET\_TYPE\_BYTES | 0x32 | 表示一个用户可自定义传入的字段，该字段可被更新，其值为bytes类型。 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_4 = ASSET\_TYPE\_BYTES | 0x33 | 表示一个用户可自定义传入的字段，该字段可被更新，其值为bytes类型。 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_1 = ASSET\_TYPE\_BYTES | 0x34 | 表示一个用户可自定义传入的字段，该字段可被更新，该项信息不会进行同步，其值为bytes类型。  **起始版本：** 12 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_2 = ASSET\_TYPE\_BYTES | 0x35 | 表示一个用户可自定义传入的字段，该字段可被更新，该项信息不会进行同步，其值为bytes类型。  **起始版本：** 12 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_3 = ASSET\_TYPE\_BYTES | 0x36 | 表示一个用户可自定义传入的字段，该字段可被更新，该项信息不会进行同步，其值为bytes类型。  **起始版本：** 12 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_4 = ASSET\_TYPE\_BYTES | 0x37 | 表示一个用户可自定义传入的字段，该字段可被更新，该项信息不会进行同步，其值为bytes类型。  **起始版本：** 12 |
| ASSET\_TAG\_RETURN\_TYPE = ASSET\_TYPE\_NUMBER | 0x40 | 表示查询关键资产时的返回类型，其值为uint32\_t类型。 |
| ASSET\_TAG\_RETURN\_LIMIT = ASSET\_TYPE\_NUMBER | 0x41 | 表示查询关键资产时的最大返回数量，其值为uint32\_t类型。 |
| ASSET\_TAG\_RETURN\_OFFSET = ASSET\_TYPE\_NUMBER | 0x42 | 表示查询关键资产时的偏移量，其值为uint32\_t类型。 |
| ASSET\_TAG\_RETURN\_ORDERED\_BY = ASSET\_TYPE\_NUMBER | 0x43 | 表示查询关键资产时的排序依据，其值为uint32\_t类型。 |
| ASSET\_TAG\_CONFLICT\_RESOLUTION = ASSET\_TYPE\_NUMBER | 0x44 | 表示增加关键资产时的冲突处理策略，其值为uint32\_t类型。 |
| ASSET\_TAG\_UPDATE\_TIME = ASSET\_TYPE\_BYTES | 0x45 | 表示关键资产的更新时间（时间戳形式），其值为bytes类型。  **起始版本：** 12 |
| ASSET\_TAG\_OPERATION\_TYPE = ASSET\_TYPE\_NUMBER | 0x46 | 表示附加的操作类型，其值为uint32\_t类型。  **起始版本：** 12 |
| ASSET\_TAG\_REQUIRE\_ATTR\_ENCRYPTED = ASSET\_TYPE\_BOOL | 0x47 | 表示是否加密业务自定义附属信息，其值为bool类型。  **起始版本：** 14 |
| ASSET\_TAG\_GROUP\_ID = ASSET\_TYPE\_BYTES | 0x48 | 表示关键资产所属群组，其值为bytes类型。  **起始版本：** 18 |
| ASSET\_TAG\_WRAP\_TYPE = ASSET\_TYPE\_NUMBER | 0x49 | 表示关键资产支持的加密导入导出类型，其值为uint32\_t类型。  **起始版本：** 18 |

### Asset\_ResultCode

PhonePC/2in1TabletTVWearable

```
1. enum Asset_ResultCode
```

**描述**

调用ASSET返回的结果码。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| ASSET\_SUCCESS = 0 | 表示操作成功。 |
| ASSET\_PERMISSION\_DENIED = 201 | 表示调用者没有权限。 |
| ASSET\_INVALID\_ARGUMENT = 401 | 表示参数错误。 |
| ASSET\_SERVICE\_UNAVAILABLE = 24000001 | 表示关键资产服务不可用。 |
| ASSET\_NOT\_FOUND = 24000002 | 表示未找到关键资产。 |
| ASSET\_DUPLICATED = 24000003 | 表示关键资产已存在。 |
| ASSET\_ACCESS\_DENIED = 24000004 | 表示访问被拒绝。 |
| ASSET\_STATUS\_MISMATCH = 24000005 | 表示锁屏状态不匹配。 |
| ASSET\_OUT\_OF\_MEMORY = 24000006 | 表示系统内存不足。 |
| ASSET\_DATA\_CORRUPTED = 24000007 | 表示关键资产损坏。 |
| ASSET\_DATABASE\_ERROR = 24000008 | 表示数据库操作失败。 |
| ASSET\_CRYPTO\_ERROR = 24000009 | 表示算法库操作失败。 |
| ASSET\_IPC\_ERROR = 24000010 | 表示进程通信错误。 |
| ASSET\_BMS\_ERROR = 24000011 | 表示包管理服务异常。 |
| ASSET\_ACCOUNT\_ERROR = 24000012 | 表示账号系统服务异常。 |
| ASSET\_ACCESS\_TOKEN\_ERROR = 24000013 | 表示访问控制服务异常。 |
| ASSET\_FILE\_OPERATION\_ERROR = 24000014 | 表示文件操作失败。 |
| ASSET\_GET\_SYSTEM\_TIME\_ERROR = 24000015 | 表示获取系统时间失败。 |
| ASSET\_LIMIT\_EXCEEDED = 24000016 | 表示缓存数量超限。 |
| ASSET\_UNSUPPORTED = 24000017 | 表示该子功能不支持。 |
| ASSET\_PARAM\_VERIFICATION\_FAILED = 24000018 | 表示参数校验失败。  **起始版本：** 20 |

### Asset\_Accessibility

PhonePC/2in1TabletTVWearable

```
1. enum Asset_Accessibility
```

**描述**

基于锁屏状态的访问控制类型。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| ASSET\_ACCESSIBILITY\_DEVICE\_POWERED\_ON = 0 | 开机后可访问。 |
| ASSET\_ACCESSIBILITY\_DEVICE\_FIRST\_UNLOCKED = 1 | 首次解锁后可访问。 |
| ASSET\_ACCESSIBILITY\_DEVICE\_UNLOCKED = 2 | 解锁时可访问。 |

### Asset\_AuthType

PhonePC/2in1TabletTVWearable

```
1. enum Asset_AuthType
```

**描述**

关键资产支持的用户认证类型。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| ASSET\_AUTH\_TYPE\_NONE = 0x00 | 访问关键资产前无需用户认证。 |
| ASSET\_AUTH\_TYPE\_ANY = 0xFF | 任意一种用户认证方式（PIN码、人脸、指纹等）通过后，均可访问关键资产。 |

### Asset\_SyncType

PhonePC/2in1TabletTVWearable

```
1. enum Asset_SyncType
```

**描述**

关键资产支持的同步类型。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| ASSET\_SYNC\_TYPE\_NEVER = 0 | 不允许同步关键资产。 |
| ASSET\_SYNC\_TYPE\_THIS\_DEVICE = 1 << 0 | 只在本设备进行同步，如仅在本设备还原的备份场景。 |
| ASSET\_SYNC\_TYPE\_TRUSTED\_DEVICE = 1 << 1 | 只在可信设备间进行同步，如克隆场景。 |
| ASSET\_SYNC\_TYPE\_TRUSTED\_ACCOUNT = 1 << 2 | 只在登录可信账号的设备间进行同步，如云同步场景。  **起始版本：** 12 |

### Asset\_WrapType

PhonePC/2in1TabletTVWearable

```
1. enum Asset_WrapType
```

**描述**

关键资产支持的加密导入导出类型。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| ASSET\_WRAP\_TYPE\_NEVER = 0 | 不允许加密导入导出关键资产。 |
| ASSET\_WRAP\_TYPE\_TRUSTED\_ACCOUNT = 1 | 只在登录可信账号的设备进行加密导入导出关键资产。 |

### Asset\_ConflictResolution

PhonePC/2in1TabletTVWearable

```
1. enum Asset_ConflictResolution
```

**描述**

新增关键资产时的冲突（如：别名相同）处理策略。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| ASSET\_CONFLICT\_OVERWRITE = 0 | 覆盖原本的关键资产。 |
| ASSET\_CONFLICT\_THROW\_ERROR = 1 | 抛出异常，由业务进行后续处理。 |

### Asset\_ReturnType

PhonePC/2in1TabletTVWearable

```
1. enum Asset_ReturnType
```

**描述**

关键资产查询返回的结果类型。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| ASSET\_RETURN\_ALL = 0 | 返回关键资产明文及属性。 |
| ASSET\_RETURN\_ATTRIBUTES = 1 | 返回关键资产属性，不含关键资产明文。 |

### Asset\_OperationType

PhonePC/2in1TabletTVWearable

```
1. enum Asset_OperationType
```

**描述**

附属的操作类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ASSET\_NEED\_SYNC = 0 | 需要进行同步操作。 |
| ASSET\_NEED\_LOGOUT = 1 | 需要进行登出操作。 |
