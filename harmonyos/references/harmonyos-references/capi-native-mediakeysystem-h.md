---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-mediakeysystem-h
title: native_mediakeysystem.h
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 头文件 > native_mediakeysystem.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0a50bd2a554bfec5cb538b43eb93863fdf27c746c06cf2d8ee30b388e304654b
---

## 概述

PhonePC/2in1TabletTVWearable

定义Drm MediaKeySystem API。提供以下功能：

查询是否支持特定的drm、创建媒体密钥会话、获取和设置配置、获取统计信息、获取内容保护级别、生成提供请求、处理提供响应、事件监听、获取内容防护级别、管理离线媒体密钥等。

**引用文件：** <multimedia/drm\_framework/native\_mediakeysystem.h>

**库：** libnative\_drm.so

**系统能力：** SystemCapability.Multimedia.Drm.Core

**起始版本：** 11

**相关模块：** [Drm](capi-drm.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef Drm\_ErrCode (\*MediaKeySystem\_Callback)(DRM\_EventType eventType, uint8\_t \*info, int32\_t infoLen, char \*extra)](capi-native-mediakeysystem-h.md#mediakeysystem_callback) | MediaKeySystem\_Callback | MediaKeySystem事件触发时将调用的回调，不返回MediaKeySystem实例，适用于单个MediaKeySystem场景。 |
| [typedef Drm\_ErrCode (\*OH\_MediaKeySystem\_Callback)(MediaKeySystem \*mediaKeySystem, DRM\_EventType eventType, uint8\_t \*info, int32\_t infoLen, char \*extra)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_callback) | OH\_MediaKeySystem\_Callback | MediaKeySystem事件触发时将调用的回调，返回MediaKeySystem实例，适用于多个MediaKeySystem场景。 |
| [Drm\_ErrCode OH\_MediaKeySystem\_SetCallback(MediaKeySystem \*mediaKeySystem, OH\_MediaKeySystem\_Callback callback)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_setcallback) | - | 设置MediaKeySystem事件回调。 |
| [Drm\_ErrCode OH\_MediaKeySystem\_GetMediaKeySystems(DRM\_MediaKeySystemDescription \*descs, uint32\_t \*count)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_getmediakeysystems) | - | 获取设备支持的DRM解决方案的名称和唯一标识的列表。 |
| [bool OH\_MediaKeySystem\_IsSupported(const char \*name)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_issupported) | - | 查询设备是否支持对应的DRM解决方案。 |
| [bool OH\_MediaKeySystem\_IsSupported2(const char \*name, const char \*mimeType)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_issupported2) | - | 查询设备是否支持对应的DRM解决方案名称及媒体类型。 |
| [bool OH\_MediaKeySystem\_IsSupported3(const char \*name, const char \*mimeType, DRM\_ContentProtectionLevel contentProtectionLevel)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_issupported3) | - | 查询设备是否支持对应的DRM解决方案、媒体类型、内容保护级别。 |
| [Drm\_ErrCode OH\_MediaKeySystem\_Create(const char \*name, MediaKeySystem \*\*mediaKeySystem)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_create) | - | 创建MediaKeySystem实例。 |
| [Drm\_ErrCode OH\_MediaKeySystem\_SetConfigurationString(MediaKeySystem \*mediaKeySystem, const char \*configName, const char \*value)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_setconfigurationstring) | - | 设置字符串类型的配置属性。 |
| [Drm\_ErrCode OH\_MediaKeySystem\_GetConfigurationString(MediaKeySystem \*mediaKeySystem, const char \*configName, char \*value, int32\_t valueLen)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_getconfigurationstring) | - | 获取字符串类型配置属性值。 |
| [Drm\_ErrCode OH\_MediaKeySystem\_SetConfigurationByteArray(MediaKeySystem \*mediaKeySystem, const char \*configName, uint8\_t \*value, int32\_t valueLen)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_setconfigurationbytearray) | - | 设置字符数组类型的配置属性值。 |
| [Drm\_ErrCode OH\_MediaKeySystem\_GetConfigurationByteArray(MediaKeySystem \*mediaKeySystem, const char \*configName, uint8\_t \*value, int32\_t \*valueLen)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_getconfigurationbytearray) | - | 获取字符数组类型配置属性值。 |
| [Drm\_ErrCode OH\_MediaKeySystem\_GetStatistics(MediaKeySystem \*mediaKeySystem, DRM\_Statistics \*statistics)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_getstatistics) | - | 获取度量记录。 |
| [Drm\_ErrCode OH\_MediaKeySystem\_GetMaxContentProtectionLevel(MediaKeySystem \*mediaKeySystem, DRM\_ContentProtectionLevel \*contentProtectionLevel)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_getmaxcontentprotectionlevel) | - | 获取设备支持的最大内容保护级别。 |
| [Drm\_ErrCode OH\_MediaKeySystem\_SetMediaKeySystemCallback(MediaKeySystem \*mediaKeySystem, MediaKeySystem\_Callback callback)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_setmediakeysystemcallback) | - | 设置MediaKeySystem事件回调。 |
| [Drm\_ErrCode OH\_MediaKeySystem\_CreateMediaKeySession(MediaKeySystem \*mediaKeySystem, DRM\_ContentProtectionLevel \*level, MediaKeySession \*\*mediaKeySession)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_createmediakeysession) | - | 创建MediaKeySession会话实例。 |
| [Drm\_ErrCode OH\_MediaKeySystem\_GenerateKeySystemRequest(MediaKeySystem \*mediaKeySystem, uint8\_t \*request, int32\_t \*requestLen, char \*defaultUrl, int32\_t defaultUrlLen)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_generatekeysystemrequest) | - | 生成设备DRM证书请求。 |
| [Drm\_ErrCode OH\_MediaKeySystem\_ProcessKeySystemResponse(MediaKeySystem \*mediaKeySystem, uint8\_t \*response, int32\_t responseLen)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_processkeysystemresponse) | - | 处理设备DRM证书请求响应。 |
| [Drm\_ErrCode OH\_MediaKeySystem\_GetOfflineMediaKeyIds(MediaKeySystem \*mediaKeySystem, DRM\_OfflineMediakeyIdArray \*offlineMediaKeyIds)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_getofflinemediakeyids) | - | 获取离线媒体密钥标识列表，媒体密钥标识用于对离线媒体密钥的管理。 |
| [Drm\_ErrCode OH\_MediaKeySystem\_GetOfflineMediaKeyStatus(MediaKeySystem \*mediaKeySystem, uint8\_t \*offlineMediaKeyId, int32\_t offlineMediaKeyIdLen, DRM\_OfflineMediaKeyStatus \*status)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_getofflinemediakeystatus) | - | 获取离线媒体密钥状态。 |
| [Drm\_ErrCode OH\_MediaKeySystem\_ClearOfflineMediaKeys(MediaKeySystem \*mediaKeySystem, uint8\_t \*offlineMediaKeyId, int32\_t offlineMediaKeyIdLen)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_clearofflinemediakeys) | - | 按id清除离线媒体密钥。 |
| [Drm\_ErrCode OH\_MediaKeySystem\_GetCertificateStatus(MediaKeySystem \*mediaKeySystem, DRM\_CertificateStatus \*certStatus)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_getcertificatestatus) | - | 获取设备DRM证书状态。 |
| [Drm\_ErrCode OH\_MediaKeySystem\_Destroy(MediaKeySystem \*mediaKeySystem)](capi-native-mediakeysystem-h.md#oh_mediakeysystem_destroy) | - | 销毁MediaKeySystem实例。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### MediaKeySystem\_Callback()

PhonePC/2in1TabletTVWearable

```
1. typedef  Drm_ErrCode (*MediaKeySystem_Callback)(DRM_EventType eventType, uint8_t *info,int32_t infoLen, char *extra)
```

**描述**

MediaKeySystem事件触发时将调用的回调，不返回MediaKeySystem实例，适用于单个MediaKeySystem场景。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [DRM\_EventType](capi-native-drm-common-h.md#drm_eventtype) eventType | 事件类型。 |
| uint8\_t \*info | 事件信息。 |
| int32\_t infoLen | 事件信息长度。 |
| char \*extra | 增量信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Drm\_ErrCode](capi-native-drm-err-h.md#drm_errcode) | DRM\_ERR\_OK：执行成功。  DRM\_ERR\_INVALID\_VAL：输入参数无效。 |

### OH\_MediaKeySystem\_Callback()

PhonePC/2in1TabletTVWearable

```
1. typedef Drm_ErrCode (*OH_MediaKeySystem_Callback)(MediaKeySystem *mediaKeySystem, DRM_EventType eventType,uint8_t *info, int32_t infoLen, char *extra)
```

**描述**

MediaKeySystem事件触发时将调用的回调，返回MediaKeySystem实例，适用于多个MediaKeySystem场景。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [MediaKeySystem](capi-drm-mediakeysystem.md) \*mediaKeySystem | MediaKeySystem实例。 |
| [DRM\_EventType](capi-native-drm-common-h.md#drm_eventtype) eventType | 事件类型。 |
| uint8\_t \*info | 事件信息。 |
| int32\_t infoLen | 事件信息长度。 |
| char \*extra | 增量信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Drm\_ErrCode](capi-native-drm-err-h.md#drm_errcode) | DRM\_ERR\_OK：执行成功。  DRM\_ERR\_INVALID\_VAL：输入参数无效。 |

### OH\_MediaKeySystem\_SetCallback()

PhonePC/2in1TabletTVWearable

```
1. Drm_ErrCode OH_MediaKeySystem_SetCallback(MediaKeySystem *mediaKeySystem, OH_MediaKeySystem_Callback callback)
```

**描述**

设置MediaKeySystem事件回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [MediaKeySystem](capi-drm-mediakeysystem.md) \*mediaKeySystem | MediaKeySystem实例。 |
| [OH\_MediaKeySystem\_Callback](capi-native-mediakeysystem-h.md#oh_mediakeysystem_callback) callback | 回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Drm\_ErrCode](capi-native-drm-err-h.md#drm_errcode) | DRM\_ERR\_OK：执行成功。  DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySystem为空指针或无效。 |

### OH\_MediaKeySystem\_GetMediaKeySystems()

PhonePC/2in1TabletTVWearable

```
1. Drm_ErrCode OH_MediaKeySystem_GetMediaKeySystems(DRM_MediaKeySystemDescription *descs, uint32_t *count)
```

**描述**

获取设备支持的DRM解决方案的名称和唯一标识的列表。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [DRM\_MediaKeySystemDescription](capi-drm-drm-mediakeysystemdescription.md) \*descs | DRM解决方案名称和唯一标识的列表。 |
| uint32\_t \*count | DRM解决方案名称和唯一标识的列表长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Drm\_ErrCode](capi-native-drm-err-h.md#drm_errcode) | DRM\_ERR\_OK：执行成功。  DRM\_ERR\_INVALID\_VAL：可能原因：  1.输入参数descs为空指针或输入参数count为空指针。  2.输入参数descs长度不足。  DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。 |

### OH\_MediaKeySystem\_IsSupported()

PhonePC/2in1TabletTVWearable

```
1. bool OH_MediaKeySystem_IsSupported(const char *name)
```

**描述**

查询设备是否支持对应的DRM解决方案。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*name | DRM解决方案名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 表示是否支持指定DRM解决方案。true表示支持，false表示不支持。 |

### OH\_MediaKeySystem\_IsSupported2()

PhonePC/2in1TabletTVWearable

```
1. bool OH_MediaKeySystem_IsSupported2(const char *name, const char *mimeType)
```

**描述**

查询设备是否支持对应的DRM解决方案名称及媒体类型。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*name | DRM解决方案名称。 |
| const char \*mimeType | 媒体类型，支持的媒体类型取决于DRM解决方案，如：video/avc、video/hev。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 表示是否支持指定DRM解决方案及媒体类型。true表示支持，false表示不支持。 |

### OH\_MediaKeySystem\_IsSupported3()

PhonePC/2in1TabletTVWearable

```
1. bool OH_MediaKeySystem_IsSupported3(const char *name, const char *mimeType,DRM_ContentProtectionLevel contentProtectionLevel)
```

**描述**

查询设备是否支持对应的DRM解决方案、媒体类型、内容保护级别。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*name | DRM解决方案名称。 |
| const char \*mimeType | 媒体类型，支持的媒体类型取决于DRM解决方案，如：video/avc、video/hev。 |
| [DRM\_ContentProtectionLevel](capi-native-drm-common-h.md#drm_contentprotectionlevel) contentProtectionLevel | 内容保护级别。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 表示是否支持指定DRM解决方案，媒体类型以及内容保护级别。true表示支持，false表示不支持。 |

### OH\_MediaKeySystem\_Create()

PhonePC/2in1TabletTVWearable

```
1. Drm_ErrCode OH_MediaKeySystem_Create(const char *name, MediaKeySystem **mediaKeySystem)
```

**描述**

创建MediaKeySystem实例。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*name | DRM解决方案名称。 |
| [MediaKeySystem](capi-drm-mediakeysystem.md) \*\*mediaKeySystem | MediaKeySystem实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Drm\_ErrCode](capi-native-drm-err-h.md#drm_errcode) | DRM\_ERR\_OK：执行成功。  DRM\_ERR\_INVALID\_VAL：可能原因：  1.输入参数name为空指针或长度为0。  2.输入参数mediaKeySystem为空指针。  DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。  DRM\_ERR\_SERVICE\_DIED：服务死亡。  DRM\_ERR\_MAX\_SYSTEM\_NUM\_REACHED：已创建的MediaKeySystem数量达到最大限制(64个)。 |

### OH\_MediaKeySystem\_SetConfigurationString()

PhonePC/2in1TabletTVWearable

```
1. Drm_ErrCode OH_MediaKeySystem_SetConfigurationString(MediaKeySystem *mediaKeySystem,const char *configName, const char *value)
```

**描述**

设置字符串类型的配置属性。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [MediaKeySystem](capi-drm-mediakeysystem.md) \*mediaKeySystem | MediaKeySystem实例。 |
| const char \*configName | 字符串类型配置属性名，不能为空，具体支持的属性名由设备上DRM解决方案决定。 |
| const char \*value | 字符串类型配置属性值，不能为空，具体支持的属性值由设备上DRM解决方案决定。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Drm\_ErrCode](capi-native-drm-err-h.md#drm_errcode) | DRM\_ERR\_OK：执行成功。  DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySystem为空指针或无效，输入参数configName为空指针，或输入参数value为空指针。 |

### OH\_MediaKeySystem\_GetConfigurationString()

PhonePC/2in1TabletTVWearable

```
1. Drm_ErrCode OH_MediaKeySystem_GetConfigurationString(MediaKeySystem *mediaKeySystem,const char *configName, char *value, int32_t valueLen)
```

**描述**

获取字符串类型配置属性值。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [MediaKeySystem](capi-drm-mediakeysystem.md) \*mediaKeySystem | MediaKeySystem实例。 |
| const char \*configName | 字符串类型配置名。 |
| char \*value | 字符串类型配置值。 |
| int32\_t valueLen | 字符串类型配置值长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Drm\_ErrCode](capi-native-drm-err-h.md#drm_errcode) | DRM\_ERR\_OK：执行成功。  DRM\_ERR\_NO\_MEMORY：内存不足，内存分配失败。  DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySystem为空指针或无效，输入参数configName为空指针，或输入参数value为空指针。  DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。 |

### OH\_MediaKeySystem\_SetConfigurationByteArray()

PhonePC/2in1TabletTVWearable

```
1. Drm_ErrCode OH_MediaKeySystem_SetConfigurationByteArray(MediaKeySystem *mediaKeySystem,const char *configName, uint8_t *value, int32_t valueLen)
```

**描述**

设置字符数组类型的配置属性值。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [MediaKeySystem](capi-drm-mediakeysystem.md) \*mediaKeySystem | MediaKeySystem实例。 |
| const char \*configName | 字符数组类型配置属性名，不能为空，具体支持的属性名由设备上DRM解决方案决定。 |
| uint8\_t \*value | 字符数组类型配置属性值，不能为空，具体支持的属性值由设备上DRM解决方案决定。 |
| int32\_t valueLen | 字符数组类型配置属性值长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Drm\_ErrCode](capi-native-drm-err-h.md#drm_errcode) | DRM\_ERR\_OK：执行成功。  DRM\_ERR\_NO\_MEMORY：内存不足，内存分配失败。  DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySystem为空指针或无效，输入参数configName为空指针，或输入参数value为空指针。  DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。 |

### OH\_MediaKeySystem\_GetConfigurationByteArray()

PhonePC/2in1TabletTVWearable

```
1. Drm_ErrCode OH_MediaKeySystem_GetConfigurationByteArray(MediaKeySystem *mediaKeySystem,const char *configName, uint8_t *value, int32_t *valueLen)
```

**描述**

获取字符数组类型配置属性值。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [MediaKeySystem](capi-drm-mediakeysystem.md) \*mediaKeySystem | MediaKeySystem实例。 |
| const char \*configName | 字符数组类型配置属性名称，不能为空，具体支持的属性名由设备上DRM解决方案决定。 |
| uint8\_t \*value | 字符数组类型配置属性。 |
| int32\_t \*valueLen | 字符数组类型配置属性长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Drm\_ErrCode](capi-native-drm-err-h.md#drm_errcode) | DRM\_ERR\_OK：执行成功。  DRM\_ERR\_NO\_MEMORY：内存不足，内存分配失败。  DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySystem为空指针或无效，输入参数configName为空指针，输入参数value为空指针，或valueLen为空指针。  DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。 |

### OH\_MediaKeySystem\_GetStatistics()

PhonePC/2in1TabletTVWearable

```
1. Drm_ErrCode OH_MediaKeySystem_GetStatistics(MediaKeySystem *mediaKeySystem, DRM_Statistics *statistics)
```

**描述**

获取度量记录。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [MediaKeySystem](capi-drm-mediakeysystem.md) \*mediaKeySystem | MediaKeySystem实例。 |
| [DRM\_Statistics](capi-drm-drm-statistics.md) \*statistics | 度量记录。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Drm\_ErrCode](capi-native-drm-err-h.md#drm_errcode) | DRM\_ERR\_OK：执行成功。  DRM\_ERR\_NO\_MEMORY：内存不足，内存分配失败。  DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySystem为空指针或无效，或输入参数statistics为空指针。  DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。 |

### OH\_MediaKeySystem\_GetMaxContentProtectionLevel()

PhonePC/2in1TabletTVWearable

```
1. Drm_ErrCode OH_MediaKeySystem_GetMaxContentProtectionLevel(MediaKeySystem *mediaKeySystem,DRM_ContentProtectionLevel *contentProtectionLevel)
```

**描述**

获取设备支持的最大内容保护级别。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [MediaKeySystem](capi-drm-mediakeysystem.md) \*mediaKeySystem | MediaKeySystem实例。 |
| [DRM\_ContentProtectionLevel](capi-native-drm-common-h.md#drm_contentprotectionlevel) \*contentProtectionLevel | 内容保护级别。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Drm\_ErrCode](capi-native-drm-err-h.md#drm_errcode) | DRM\_ERR\_OK：执行成功。  DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySystem为空指针或无效，或输入参数contentProtectionLevel为空指针。  DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。 |

### OH\_MediaKeySystem\_SetMediaKeySystemCallback()

PhonePC/2in1TabletTVWearable

```
1. Drm_ErrCode OH_MediaKeySystem_SetMediaKeySystemCallback(MediaKeySystem *mediaKeySystem,MediaKeySystem_Callback callback)
```

**描述**

设置MediaKeySystem事件回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [MediaKeySystem](capi-drm-mediakeysystem.md) \*mediaKeySystem | MediaKeySystem实例。 |
| [MediaKeySystem\_Callback](capi-native-mediakeysystem-h.md#mediakeysystem_callback) callback | 回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Drm\_ErrCode](capi-native-drm-err-h.md#drm_errcode) | DRM\_ERR\_OK：执行成功。  DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySystem为空指针或无效。 |

### OH\_MediaKeySystem\_CreateMediaKeySession()

PhonePC/2in1TabletTVWearable

```
1. Drm_ErrCode OH_MediaKeySystem_CreateMediaKeySession(MediaKeySystem *mediaKeySystem,DRM_ContentProtectionLevel *level, MediaKeySession **mediaKeySession)
```

**描述**

创建MediaKeySession会话实例。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [MediaKeySystem](capi-drm-mediakeysystem.md) \*mediaKeySystem | MediaKeySystem实例。 |
| [DRM\_ContentProtectionLevel](capi-native-drm-common-h.md#drm_contentprotectionlevel) \*level | 内容保护级别。 |
| [MediaKeySession](capi-drm-mediakeysession.md) \*\*mediaKeySession | MediaKeySession实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Drm\_ErrCode](capi-native-drm-err-h.md#drm_errcode) | DRM\_ERR\_OK：执行成功。  DRM\_ERR\_NO\_MEMORY：内存不足，内存分配失败。  DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySystem为空指针或无效，或输入参数level超出合理范围，或mediaKeySession为空指针。  DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。  DRM\_ERR\_SERVICE\_DIED：服务死亡。  DRM\_ERR\_MAX\_SESSION\_NUM\_REACHED：当前MediaKeySystem已创建的MediaKeySession数量达到最大限制(64个)。 |

### OH\_MediaKeySystem\_GenerateKeySystemRequest()

PhonePC/2in1TabletTVWearable

```
1. Drm_ErrCode OH_MediaKeySystem_GenerateKeySystemRequest(MediaKeySystem *mediaKeySystem, uint8_t *request,int32_t *requestLen, char *defaultUrl, int32_t defaultUrlLen)
```

**描述**

生成设备DRM证书请求。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [MediaKeySystem](capi-drm-mediakeysystem.md) \*mediaKeySystem | MediaKeySystem实例。 |
| uint8\_t \*request | 设备DRM证书请求。 |
| int32\_t \*requestLen | 设备DRM证书请求的长度。 |
| char \*defaultUrl | 设备DRM证书服务的URL。 |
| int32\_t defaultUrlLen | 设备DRM证书服务的URL长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Drm\_ErrCode](capi-native-drm-err-h.md#drm_errcode) | DRM\_ERR\_OK：执行成功。  DRM\_ERR\_NO\_MEMORY：内存不足，内存分配失败。  DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySystem为空指针或无效，或其它指针类型输入参数为空指针。  DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。 |

### OH\_MediaKeySystem\_ProcessKeySystemResponse()

PhonePC/2in1TabletTVWearable

```
1. Drm_ErrCode OH_MediaKeySystem_ProcessKeySystemResponse(MediaKeySystem *mediaKeySystem,uint8_t *response, int32_t responseLen)
```

**描述**

处理设备DRM证书请求响应。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [MediaKeySystem](capi-drm-mediakeysystem.md) \*mediaKeySystem | MediaKeySystem实例。 |
| uint8\_t \*response | 设备DRM证书请求响应。 |
| int32\_t responseLen | 设备DRM证书请求响应长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Drm\_ErrCode](capi-native-drm-err-h.md#drm_errcode) | DRM\_ERR\_OK：执行成功。  DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySystem为空指针或无效，或输入参数response为空指针。  DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。 |

### OH\_MediaKeySystem\_GetOfflineMediaKeyIds()

PhonePC/2in1TabletTVWearable

```
1. Drm_ErrCode OH_MediaKeySystem_GetOfflineMediaKeyIds(MediaKeySystem *mediaKeySystem,DRM_OfflineMediakeyIdArray *offlineMediaKeyIds)
```

**描述**

获取离线媒体密钥标识列表，媒体密钥标识用于对离线媒体密钥的管理。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [MediaKeySystem](capi-drm-mediakeysystem.md) \*mediaKeySystem | MediaKeySystem实例。 |
| [DRM\_OfflineMediakeyIdArray](capi-drm-drm-offlinemediakeyidarray.md) \*offlineMediaKeyIds | 离线媒体密钥的媒体密钥标识列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Drm\_ErrCode](capi-native-drm-err-h.md#drm_errcode) | DRM\_ERR\_OK：执行成功。  DRM\_ERR\_NO\_MEMORY：内存不足，内存分配失败。  DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySystem为空指针或无效，或输入参数offlineMediaKeyIds为空指针。  DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。 |

### OH\_MediaKeySystem\_GetOfflineMediaKeyStatus()

PhonePC/2in1TabletTVWearable

```
1. Drm_ErrCode OH_MediaKeySystem_GetOfflineMediaKeyStatus(MediaKeySystem *mediaKeySystem,uint8_t *offlineMediaKeyId, int32_t offlineMediaKeyIdLen, DRM_OfflineMediaKeyStatus *status)
```

**描述**

获取离线媒体密钥状态。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [MediaKeySystem](capi-drm-mediakeysystem.md) \*mediaKeySystem | MediaKeySystem实例。 |
| uint8\_t \*offlineMediaKeyId | 离线媒体密钥标识。 |
| int32\_t offlineMediaKeyIdLen | 离线媒体密钥标识长度。 |
| [DRM\_OfflineMediaKeyStatus](capi-native-drm-common-h.md#drm_offlinemediakeystatus) \*status | 媒体密钥状态。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Drm\_ErrCode](capi-native-drm-err-h.md#drm_errcode) | DRM\_ERR\_OK：执行成功。  DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySystem为空指针或无效，或其它指针类型输入参数为空指针。  DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。 |

### OH\_MediaKeySystem\_ClearOfflineMediaKeys()

PhonePC/2in1TabletTVWearable

```
1. Drm_ErrCode OH_MediaKeySystem_ClearOfflineMediaKeys(MediaKeySystem *mediaKeySystem,uint8_t *offlineMediaKeyId, int32_t offlineMediaKeyIdLen)
```

**描述**

按id清除离线媒体密钥。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [MediaKeySystem](capi-drm-mediakeysystem.md) \*mediaKeySystem | MediaKeySystem实例。 |
| uint8\_t \*offlineMediaKeyId | 离线媒体密钥标识。 |
| int32\_t offlineMediaKeyIdLen | 离线媒体密钥标识长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Drm\_ErrCode](capi-native-drm-err-h.md#drm_errcode) | DRM\_ERR\_OK：执行成功。  DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySystem为空指针或无效，或输入参数offlineMediaKeyId为空指针。  DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。 |

### OH\_MediaKeySystem\_GetCertificateStatus()

PhonePC/2in1TabletTVWearable

```
1. Drm_ErrCode OH_MediaKeySystem_GetCertificateStatus(MediaKeySystem *mediaKeySystem,DRM_CertificateStatus *certStatus)
```

**描述**

获取设备DRM证书状态。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [MediaKeySystem](capi-drm-mediakeysystem.md) \*mediaKeySystem | MediaKeySystem实例。 |
| [DRM\_CertificateStatus](capi-native-drm-common-h.md#drm_certificatestatus) \*certStatus | 设备DRM证书状态值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Drm\_ErrCode](capi-native-drm-err-h.md#drm_errcode) | DRM\_ERR\_OK：执行成功。  DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySystem为空指针或无效，或输入参数certStatus为空指针。  DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。 |

### OH\_MediaKeySystem\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. Drm_ErrCode OH_MediaKeySystem_Destroy(MediaKeySystem *mediaKeySystem)
```

**描述**

销毁MediaKeySystem实例。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [MediaKeySystem](capi-drm-mediakeysystem.md) \*mediaKeySystem | MediaKeySystem实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Drm\_ErrCode](capi-native-drm-err-h.md#drm_errcode) | DRM\_ERR\_OK：执行成功。  DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySystem为空指针或无效。  DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。 |
