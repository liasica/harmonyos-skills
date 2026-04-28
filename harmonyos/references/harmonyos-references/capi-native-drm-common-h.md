---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h
title: native_drm_common.h
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > C API > 头文件 > native_drm_common.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ec8aaf3eb49cf0061104c46816431c0a16648f0ada7832fa1e9f77deea1b5490
---

## 概述

PhonePC/2in1TabletTVWearable

定义DRM数据类型。

**引用文件：** <multimedia/drm\_framework/native\_drm\_common.h>

**库：** libnative\_drm.so

**系统能力：** SystemCapability.Multimedia.Drm.Core

**起始版本：** 11

**相关模块：** [Drm](capi-drm.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [DRM\_MediaKeyRequestInfo](capi-drm-drm-mediakeyrequestinfo.md) | DRM\_MediaKeyRequestInfo | 媒体密钥请求信息。 |
| [DRM\_MediaKeyRequest](capi-drm-drm-mediakeyrequest.md) | DRM\_MediaKeyRequest | 媒体密钥请求。 |
| [DRM\_Statistics](capi-drm-drm-statistics.md) | DRM\_Statistics | MediaKeySystem的度量信息。 |
| [DRM\_OfflineMediakeyIdArray](capi-drm-drm-offlinemediakeyidarray.md) | DRM\_OfflineMediakeyIdArray | 离线媒体密钥ID数组。 |
| [DRM\_KeysInfo](capi-drm-drm-keysinfo.md) | DRM\_KeysInfo | 媒体密钥信息。 |
| [DRM\_MediaKeyStatus](capi-drm-drm-mediakeystatus.md) | DRM\_MediaKeyStatus | 媒体密钥状态。 |
| [DRM\_PsshInfo](capi-drm-drm-psshinfo.md) | DRM\_PsshInfo | DRM内容保护系统专用头（Protection System Specific Header）信息。 |
| [DRM\_MediaKeySystemInfo](capi-drm-drm-mediakeysysteminfo.md) | DRM\_MediaKeySystemInfo | 加密媒体内容的DRM信息。 |
| [DRM\_MediaKeySystemDescription](capi-drm-drm-mediakeysystemdescription.md) | DRM\_MediaKeySystemDescription | DRM解决方案名称及其UUID的列表。 |
| [MediaKeySystem](capi-drm-mediakeysystem.md) | MediaKeySystem | MediaKeySystem结构。 |
| [MediaKeySession](capi-drm-mediakeysession.md) | MediaKeySession | MediaKeySession结构。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [DRM\_EventType](capi-native-drm-common-h.md#drm_eventtype) | DRM\_EventType | 监听事件类型。 |
| [DRM\_ContentProtectionLevel](capi-native-drm-common-h.md#drm_contentprotectionlevel) | DRM\_ContentProtectionLevel | 内容保护级别。 |
| [DRM\_MediaKeyType](capi-native-drm-common-h.md#drm_mediakeytype) | DRM\_MediaKeyType | 媒体密钥类型。 |
| [DRM\_MediaKeyRequestType](capi-native-drm-common-h.md#drm_mediakeyrequesttype) | DRM\_MediaKeyRequestType | 媒体密钥请求类型。 |
| [DRM\_OfflineMediaKeyStatus](capi-native-drm-common-h.md#drm_offlinemediakeystatus) | DRM\_OfflineMediaKeyStatus | 离线媒体密钥状态。 |
| [DRM\_CertificateStatus](capi-native-drm-common-h.md#drm_certificatestatus) | DRM\_CertificateStatus | 设备DRM证书状态。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*DRM\_MediaKeySystemInfoCallback)(DRM\_MediaKeySystemInfo \*mediaKeySystemInfo)](capi-native-drm-common-h.md#drm_mediakeysysteminfocallback) | DRM\_MediaKeySystemInfoCallback | 应用为从媒体源获取DRM信息而设置的回调。 |

### 宏定义

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_COUNT 16 | 媒体密钥请求可选数据的最大数量。  **起始版本：** 11 |
| MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_NAME\_LEN 64 | 媒体密钥请求可选数据名称的最大长度。  **起始版本：** 11 |
| MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_DATA\_LEN 128 | 媒体密钥请求可选数据的最大长度。  **起始版本：** 11 |
| MAX\_INIT\_DATA\_LEN 2048 | 媒体密钥请求初始化数据的最大长度。  **起始版本：** 11 |
| MAX\_MIMETYPE\_LEN 64 | 媒体mimetype的最大长度。  **起始版本：** 11 |
| MAX\_MEDIA\_KEY\_REQUEST\_DATA\_LEN 8192 | 媒体密钥请求数据的最大长度。  **起始版本：** 11 |
| MAX\_DEFAULT\_URL\_LEN 2048 | URL最大长度。  **起始版本：** 11 |
| MAX\_STATISTICS\_COUNT 10 | 度量记录的最大数量。  **起始版本：** 11 |
| MAX\_STATISTICS\_NAME\_LEN 64 | 度量记录名称的最大长度。  **起始版本：** 11 |
| MAX\_STATISTICS\_BUFFER\_LEN 256 | 度量记录缓冲区的最大长度。  **起始版本：** 11 |
| MAX\_OFFLINE\_MEDIA\_KEY\_ID\_COUNT 512 | 离线媒体密钥标识的最大数量。  **起始版本：** 11 |
| MAX\_OFFLINE\_MEDIA\_KEY\_ID\_LEN 64 | 离线媒体密钥标识的最大长度。  **起始版本：** 11 |
| MAX\_KEY\_INFO\_COUNT 64 | 密钥信息的最大数量。  **起始版本：** 11 |
| MAX\_KEY\_ID\_LEN 16 | 密钥标识的最大长度。  **起始版本：** 11 |
| MAX\_KEY\_STATUS\_VALUE\_LEN 128 | 密钥状态值的最大长度。  **起始版本：** 11 |
| MAX\_MEDIA\_KEY\_STATUS\_COUNT 64 | 媒体密钥状态的最大数量。  **起始版本：** 11 |
| MAX\_MEDIA\_KEY\_STATUS\_NAME\_LEN 64 | 媒体密钥状态名称的最大长度。  **起始版本：** 11 |
| MAX\_MEDIA\_KEY\_STATUS\_VALUE\_LEN 256 | 媒体密钥状态值的最大长度。  **起始版本：** 11 |
| DRM\_UUID\_LEN 16 | DRM解决方案的UUID长度。  **起始版本：** 11 |
| MAX\_PSSH\_DATA\_LEN 2048 | PSSH（Protected System Specific Header）信息的最大长度。  **起始版本：** 11 |
| MAX\_PSSH\_INFO\_COUNT 8 | PSSH（Protected System Specific Header）信息的最大数量。  **起始版本：** 11 |
| MAX\_MEDIA\_KEY\_SYSTEM\_NAME\_LEN 128 | MediaKeySystem名称的最大长度。  **起始版本：** 12 |
| MAX\_MEDIA\_KEY\_SYSTEM\_NUM 8 | MediaKeySystem的最大数量。  **起始版本：** 12 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### DRM\_EventType

PhonePC/2in1TabletTVWearable

```
1. enum DRM_EventType
```

**描述**

监听事件类型。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| EVENT\_DRM\_BASE = 200 | DRM基础事件。 |
| EVENT\_PROVISION\_REQUIRED = 201 | 设备证书请求事件。 |
| EVENT\_KEY\_REQUIRED = 202 | 密钥请求事件。 |
| EVENT\_KEY\_EXPIRED = 203 | 密钥过期事件。 |
| EVENT\_VENDOR\_DEFINED = 204 | DRM解决方案自定义事件。 |
| EVENT\_EXPIRATION\_UPDATE = 206 | 密钥过期更新事件。 |

### DRM\_ContentProtectionLevel

PhonePC/2in1TabletTVWearable

```
1. enum DRM_ContentProtectionLevel
```

**描述**

内容保护级别。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| CONTENT\_PROTECTION\_LEVEL\_UNKNOWN = 0 | 未知级别。 |
| CONTENT\_PROTECTION\_LEVEL\_SW\_CRYPTO | 软件安全级别。 |
| CONTENT\_PROTECTION\_LEVEL\_HW\_CRYPTO | 硬件安全级别。 |
| CONTENT\_PROTECTION\_LEVEL\_ENHANCED\_HW\_CRYPTO | 硬件增强级别。 |
| CONTENT\_PROTECTION\_LEVEL\_MAX | 最大安全级别。 |

### DRM\_MediaKeyType

PhonePC/2in1TabletTVWearable

```
1. enum DRM_MediaKeyType
```

**描述**

媒体密钥类型。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| MEDIA\_KEY\_TYPE\_OFFLINE = 0 | 离线。 |
| MEDIA\_KEY\_TYPE\_ONLINE | 在线。 |

### DRM\_MediaKeyRequestType

PhonePC/2in1TabletTVWearable

```
1. enum DRM_MediaKeyRequestType
```

**描述**

媒体密钥请求类型。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| MEDIA\_KEY\_REQUEST\_TYPE\_UNKNOWN = 0 | 未知请求类型。 |
| MEDIA\_KEY\_REQUEST\_TYPE\_INITIAL | 初始化请求。 |
| MEDIA\_KEY\_REQUEST\_TYPE\_RENEWAL | 续订请求。 |
| MEDIA\_KEY\_REQUEST\_TYPE\_RELEASE | 释放请求。 |
| MEDIA\_KEY\_REQUEST\_TYPE\_NONE | 无请求。 |
| MEDIA\_KEY\_REQUEST\_TYPE\_UPDATE | 更新请求。 |

### DRM\_OfflineMediaKeyStatus

PhonePC/2in1TabletTVWearable

```
1. enum DRM_OfflineMediaKeyStatus
```

**描述**

离线媒体密钥状态。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| OFFLINE\_MEDIA\_KEY\_STATUS\_UNKNOWN = 0 | 未知状态。 |
| OFFLINE\_MEDIA\_KEY\_STATUS\_USABLE | 可用状态。 |
| OFFLINE\_MEDIA\_KEY\_STATUS\_INACTIVE | 失活状态。 |

### DRM\_CertificateStatus

PhonePC/2in1TabletTVWearable

```
1. enum DRM_CertificateStatus
```

**描述**

设备DRM证书状态。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| CERT\_STATUS\_PROVISIONED = 0 | 设备已安装设备DRM证书。 |
| CERT\_STATUS\_NOT\_PROVISIONED | 设备未安装设备DRM证书或证书状态异常。 |
| CERT\_STATUS\_EXPIRED | 设备DRM证书过期。 |
| CERT\_STATUS\_INVALID | 设备DRM证书无效。 |
| CERT\_STATUS\_UNAVAILABLE | 设备DRM证书不可用。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### DRM\_MediaKeySystemInfoCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*DRM_MediaKeySystemInfoCallback)(DRM_MediaKeySystemInfo *mediaKeySystemInfo)
```

**描述**

应用为从媒体源获取DRM信息而设置的回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [DRM\_MediaKeySystemInfo](capi-drm-drm-mediakeysysteminfo.md) \*mediaKeySystemInfo | 从媒体源获取的DRM信息。 |
