---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-drm-e
title: Enums
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > ArkTS API > @ohos.multimedia.drm (数字版权保护) > Enums
category: harmonyos-references
scraped_at: 2026-04-28T08:12:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a1a489fa297669f42f0d66d984a0c3189e044d2f2339724e5ebceaead8b07e20
---

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## DrmErrorCode

PhonePC/2in1TabletTVWearable

枚举，错误码。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ERROR\_UNKNOWN | 24700101 | 未知错误。 |
| MAX\_SYSTEM\_NUM\_REACHED | 24700103 | MediaKeySystem实例数量超过上限（64个）。 |
| MAX\_SESSION\_NUM\_REACHED | 24700104 | MediaKeySession实例数量超过上限（64个）。 |
| SERVICE\_FATAL\_ERROR | 24700201 | DRM服务异常。 |

## PreDefinedConfigName

PhonePC/2in1TabletTVWearable

枚举，预定义的配置属性。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONFIG\_DEVICE\_VENDOR | 'vendor' | 插件厂商名，通过[getConfigurationString](arkts-apis-drm-mediakeysystem.md#getconfigurationstring)接口获取vendor对应配置值。 |
| CONFIG\_DEVICE\_VERSION | 'version' | 插件版本号，通过[getConfigurationString](arkts-apis-drm-mediakeysystem.md#getconfigurationstring)接口获取version对应配置值。 |
| CONFIG\_DEVICE\_DESCRIPTION | 'description' | 设备描述符，通过[getConfigurationString](arkts-apis-drm-mediakeysystem.md#getconfigurationstring)接口获取description对应配置值。 |
| CONFIG\_DEVICE\_ALGORITHMS | 'algorithms' | 支持的算法，通过[getConfigurationString](arkts-apis-drm-mediakeysystem.md#getconfigurationstring)接口获取algorithms对应配置值。 |
| CONFIG\_DEVICE\_UNIQUE\_ID | 'deviceUniqueId' | 设备唯一标识，通过[getConfigurationByteArray](arkts-apis-drm-mediakeysystem.md#getconfigurationbytearray)接口获取deviceUniqueId对应配置值。 |
| CONFIG\_SESSION\_MAX | 'maxSessionNum' | 设备支持的最大会话数，通过[getConfigurationString](arkts-apis-drm-mediakeysystem.md#getconfigurationstring)接口获取maxSessionNum对应配置值。 |
| CONFIG\_SESSION\_CURRENT | 'currentSessionNum' | 当前会话数量，通过[getConfigurationString](arkts-apis-drm-mediakeysystem.md#getconfigurationstring)接口获取currentSessionNum对应配置值。 |

## MediaKeyType

PhonePC/2in1TabletTVWearable

枚举，媒体密钥类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MEDIA\_KEY\_TYPE\_OFFLINE | 0 | 离线。 |
| MEDIA\_KEY\_TYPE\_ONLINE | 1 | 在线。 |

## OfflineMediaKeyStatus

PhonePC/2in1TabletTVWearable

枚举，离线媒体密钥状态。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OFFLINE\_MEDIA\_KEY\_STATUS\_UNKNOWN | 0 | 未知状态。 |
| OFFLINE\_MEDIA\_KEY\_STATUS\_USABLE | 1 | 可用状态。 |
| OFFLINE\_MEDIA\_KEY\_STATUS\_INACTIVE | 2 | 失活状态。 |

## CertificateStatus

PhonePC/2in1TabletTVWearable

枚举，设备证书状态。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CERT\_STATUS\_PROVISIONED | 0 | 设备已安装设备证书。 |
| CERT\_STATUS\_NOT\_PROVISIONED | 1 | 设备未安装设备证书。 |
| CERT\_STATUS\_EXPIRED | 2 | 设备证书过期。 |
| CERT\_STATUS\_INVALID | 3 | 设备证书无效。 |
| CERT\_STATUS\_UNAVAILABLE | 4 | 设备证书不可用。 |

## MediaKeyRequestType

PhonePC/2in1TabletTVWearable

枚举，媒体密钥请求类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MEDIA\_KEY\_REQUEST\_TYPE\_UNKNOWN | 0 | 未知请求类型。 |
| MEDIA\_KEY\_REQUEST\_TYPE\_INITIAL | 1 | 初始化请求。 |
| MEDIA\_KEY\_REQUEST\_TYPE\_RENEWAL | 2 | 续订请求。 |
| MEDIA\_KEY\_REQUEST\_TYPE\_RELEASE | 3 | 释放请求。 |
| MEDIA\_KEY\_REQUEST\_TYPE\_NONE | 4 | 无请求。 |
| MEDIA\_KEY\_REQUEST\_TYPE\_UPDATE | 5 | 更新请求。 |

## ContentProtectionLevel

PhonePC/2in1TabletTVWearable

枚举，内容保护级别。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONTENT\_PROTECTION\_LEVEL\_UNKNOWN | 0 | 未知内容保护级别。 |
| CONTENT\_PROTECTION\_LEVEL\_SW\_CRYPTO | 1 | 软件内容保护级别。 |
| CONTENT\_PROTECTION\_LEVEL\_HW\_CRYPTO | 2 | 硬件内容保护级别。 |
| CONTENT\_PROTECTION\_LEVEL\_ENHANCED\_HW | 3 | 硬件增强内容保护级别。 |
| CONTENT\_PROTECTION\_LEVEL\_MAX | 4 | 最高内容保护级别。 |
