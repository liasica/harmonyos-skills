---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notificationextensionsubscriptioninfo
title: NotificationExtensionSubscriptionInfo
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > ArkTS API > notification > NotificationExtensionSubscriptionInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:03:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b947da3e78d6f239a3cd4935b40f480025ed0c49f485b5ccbe6fae7fe0d8dbd4
---

用于描述通知扩展订阅的信息。

**说明** 

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## NotificationExtensionSubscriptionInfo

**系统能力：** SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [notificationExtensionSubscription.SubscribeType](js-apis-notificationextensionsubscription.md#subscribetype) | 否 | 否 | 订阅的类型，指定通知扩展的订阅方式。当前仅支持SubscribeType.BLUETOOTH，表示通过蓝牙订阅通知。 |
| addr | string | 否 | 否 | 表示设备的唯一标识符。当type为SubscribeType.BLUETOOTH时，指定对应的蓝牙设备地址。例如："11:22:33:AA:BB:FF" |
