---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-drm-e
title: Enums
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > ArkTS API > @ohos.multimedia.drm (数字版权保护) > Enums
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0da9cd65bbd62c8b6ab38c05d6356645db0f1f37bfa1f104d8052d904ed18b74
---

**说明** 

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## DrmErrorCode

枚举，错误码。

**元服务API：** 从API版本14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ERROR\_UNKNOWN | 24700101 | 未知错误，当发生无法归类的异常时返回。建议检查输入参数是否合法、DRM服务是否正常运行。 |
| MAX\_SYSTEM\_NUM\_REACHED | 24700103 | MediaKeySystem实例数量超过上限（64个）。请调用[destroy](arkts-apis-drm-mediakeysystem.md#destroy)方法销毁不需要的MediaKeySystem实例后重试。 |
| MAX\_SESSION\_NUM\_REACHED | 24700104 | MediaKeySession实例数量超过上限（64个）。请调用[destroy](arkts-apis-drm-mediakeysession.md#destroy)方法销毁不需要的MediaKeySession实例后重试。 |
| SERVICE\_FATAL\_ERROR | 24700201 | DRM服务异常，当DRM服务发生致命错误时返回。可能原因：系统资源不足、DRM服务进程崩溃或系统异常。建议重启应用或重启设备后重试。 |

## PreDefinedConfigName

枚举，预定义的配置属性。

**元服务API：** 从API版本14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONFIG\_DEVICE\_VENDOR | 'vendor' | 插件厂商名，通过[getConfigurationString](arkts-apis-drm-mediakeysystem.md#getconfigurationstring)接口获取vendor对应配置值。 |
| CONFIG\_DEVICE\_VERSION | 'version' | 插件版本号，通过[getConfigurationString](arkts-apis-drm-mediakeysystem.md#getconfigurationstring)接口获取版本对应配置值。 |
| CONFIG\_DEVICE\_DESCRIPTION | 'description' | 设备描述，通过[getConfigurationString](arkts-apis-drm-mediakeysystem.md#getconfigurationstring)接口获取description对应配置值。 |
| CONFIG\_DEVICE\_ALGORITHMS | 'algorithms' | 支持的算法，通过[getConfigurationString](arkts-apis-drm-mediakeysystem.md#getconfigurationstring)接口获取algorithms对应配置值。 |
| CONFIG\_DEVICE\_UNIQUE\_ID | 'deviceUniqueId' | 设备唯一标识，通过[getConfigurationByteArray](arkts-apis-drm-mediakeysystem.md#getconfigurationbytearray)接口获取deviceUniqueId对应配置值。 |
| CONFIG\_SESSION\_MAX | 'maxSessionNum' | 设备支持的最大会话数，通过[getConfigurationString](arkts-apis-drm-mediakeysystem.md#getconfigurationstring)接口获取maxSessionNum对应配置值。 |
| CONFIG\_SESSION\_CURRENT | 'currentSessionNum' | 当前会话数量，通过[getConfigurationString](arkts-apis-drm-mediakeysystem.md#getconfigurationstring)接口获取currentSessionNum对应配置值。 |

## MediaKeyType

枚举，媒体密钥类型。

**元服务API：** 从API版本14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MEDIA\_KEY\_TYPE\_OFFLINE | 0 | 离线媒体密钥，用于离线播放场景。 |
| MEDIA\_KEY\_TYPE\_ONLINE | 1 | 在线媒体密钥，用于在线播放场景。 |

## OfflineMediaKeyStatus

枚举，离线媒体密钥状态。

**元服务API：** 从API版本14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OFFLINE\_MEDIA\_KEY\_STATUS\_UNKNOWN | 0 | 未知状态。 |
| OFFLINE\_MEDIA\_KEY\_STATUS\_USABLE | 1 | 可用状态。 |
| OFFLINE\_MEDIA\_KEY\_STATUS\_INACTIVE | 2 | 失活状态，可能因密钥过期或被服务端禁用导致，需要重新获取密钥。 |

## CertificateStatus

枚举，设备证书状态。

**元服务API：** 从API版本14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CERT\_STATUS\_PROVISIONED | 0 | 设备已安装设备证书。 |
| CERT\_STATUS\_NOT\_PROVISIONED | 1 | 设备未安装设备证书。 |
| CERT\_STATUS\_EXPIRED | 2 | 设备证书过期。需要重新申请设备证书。 |
| CERT\_STATUS\_INVALID | 3 | 设备证书无效。 |
| CERT\_STATUS\_UNAVAILABLE | 4 | 设备证书不可用。 |

## MediaKeyRequestType

枚举，媒体密钥请求类型。

**元服务API：** 从API版本12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MEDIA\_KEY\_REQUEST\_TYPE\_UNKNOWN | 0 | 未知请求类型。 |
| MEDIA\_KEY\_REQUEST\_TYPE\_INITIAL | 1 | 初始化请求，在首次获取媒体密钥时触发。 |
| MEDIA\_KEY\_REQUEST\_TYPE\_RENEWAL | 2 | 续订请求，在许可证即将过期或需要延长有效期时触发。 |
| MEDIA\_KEY\_REQUEST\_TYPE\_RELEASE | 3 | 释放请求，在主动释放离线密钥或关闭会话时触发，用于通知服务端释放资源。 |
| MEDIA\_KEY\_REQUEST\_TYPE\_NONE | 4 | 无请求。 |
| MEDIA\_KEY\_REQUEST\_TYPE\_UPDATE | 5 | 更新请求。 |

## ContentProtectionLevel

枚举，内容保护级别。

**元服务API：** 从API版本12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONTENT\_PROTECTION\_LEVEL\_UNKNOWN | 0 | 未知内容保护级别。 |
| CONTENT\_PROTECTION\_LEVEL\_SW\_CRYPTO | 1 | 软件内容保护级别，使用软件解密，适用于对安全性要求不高的播放场景。 |
| CONTENT\_PROTECTION\_LEVEL\_HW\_CRYPTO | 2 | 硬件内容保护级别，使用硬件解密，安全性较高，适用于大多数商业内容播放场景。 |
| CONTENT\_PROTECTION\_LEVEL\_ENHANCED\_HW | 3 | 硬件增强内容保护级别，使用硬件安全模块解密，安全性最高，适用于高价值内容播放场景。 |
| CONTENT\_PROTECTION\_LEVEL\_MAX | 4 | 最高内容保护级别。 |
