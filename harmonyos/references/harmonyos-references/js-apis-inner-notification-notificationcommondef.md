---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationcommondef
title: NotificationCommonDef
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > ArkTS API > notification > NotificationCommonDef
category: harmonyos-references
scraped_at: 2026-09-02T15:03:00+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cec352206aa119091c6127924b06c3de94f6f4c4641297abeab6a50571a48192
---

NotificationCommonDef中定义了通知相关接口中使用的通用数据结构。

**说明** 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## BundleOption

描述BundleOption信息，即应用的包信息。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundle | string | 否 | 否 | 应用的包名。 |
| uid | number | 否 | 是 | 应用的UID。从[ApplicationInfo](js-apis-bundlemanager-applicationinfo.md#applicationinfo-1)获取，默认为0。 应用分身场景下，此参数为必填项。 |

## GrantedBundleInfo22+

描述已授权的包信息。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 应用的包名。 |
| appIndex | number | 是 | 否 | 应用的分身索引标识，仅在分身应用中生效。从[ApplicationInfo](js-apis-bundlemanager-applicationinfo.md#applicationinfo-1)中appIndex获取。 |
| appName | string | 是 | 是 | 应用的名称。从[ApplicationInfo](js-apis-bundlemanager-applicationinfo.md#applicationinfo-1)中label获取。 |

## UserGrantSetting

描述用户授权的设置信息。

**起始版本**：26.0.0

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| userGrantEnabled | boolean | 是 | 否 | “允许获取本机通知”的开关状态。 true：表示功能已启用；false：表示功能未启用。 |
| grantedBundleInfos | Array<[GrantedBundleInfo](js-apis-inner-notification-notificationcommondef.md#grantedbundleinfo22)> | 是 | 是 | “已获取的本机通知”通知开关开启的应用列表。 |
