---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationflags
title: NotificationFlags
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > ArkTS API > notification > NotificationFlags
category: harmonyos-references
scraped_at: 2026-04-28T08:17:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e7bc8333247eb589597289c48cb3f290777c74fa4ebd163e8e5f91da8f51bc9c
---

描述通知标志的实例。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## NotificationFlags

PhonePC/2in1TabletTVWearable

描述通知标志位。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| soundEnabled | [NotificationFlagStatus](js-apis-inner-notification-notificationflags.md#notificationflagstatus11) | 否 | 是 | 是否启用声音提示功能。默认值为TYPE\_NONE。从API version 23开始成为可写参数，设置时仅[TYPE\_CLOSE](js-apis-inner-notification-notificationflags.md#notificationflagstatus11)会生效。 |
| vibrationEnabled | [NotificationFlagStatus](js-apis-inner-notification-notificationflags.md#notificationflagstatus11) | 否 | 是 | 是否启用振动提醒功能。默认值为TYPE\_NONE。从API version 23开始成为可写参数，设置时仅[TYPE\_CLOSE](js-apis-inner-notification-notificationflags.md#notificationflagstatus11)会生效。 |
| bannerEnabled23+ | [NotificationFlagStatus](js-apis-inner-notification-notificationflags.md#notificationflagstatus11) | 否 | 是 | 是否启用横幅功能。默认值为TYPE\_NONE。设置时仅[TYPE\_CLOSE](js-apis-inner-notification-notificationflags.md#notificationflagstatus11)会生效。 |
| lockScreenEnabled23+ | [NotificationFlagStatus](js-apis-inner-notification-notificationflags.md#notificationflagstatus11) | 否 | 是 | 是否启用锁屏功能。默认值为TYPE\_NONE。设置时仅[TYPE\_CLOSE](js-apis-inner-notification-notificationflags.md#notificationflagstatus11)会生效。 |

## NotificationFlagStatus11+

PhonePC/2in1TabletTVWearable

描述通知标志状态。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TYPE\_NONE | 0 | 默认标志，与TYPE\_OPEN效果相同。 |
| TYPE\_OPEN | 1 | 通知标志打开。 |
| TYPE\_CLOSE | 2 | 通知标志关闭。 |
