---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationflags
title: NotificationFlags
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > ArkTS API > notification > NotificationFlags
category: harmonyos-references
scraped_at: 2026-09-02T15:03:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6ffb1f1f69042bdab5dd06a5c0ce4c71f6495e61d110532ad528de33416de7f1
---

描述[通知标志位](../harmonyos-guides/notification-glossary.md#notification-flags通知标志位)。应用可以使用NotificationFlags按需削减通知的提醒方式。

**说明** 

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## NotificationFlags

描述[通知标志位](../harmonyos-guides/notification-glossary.md#notification-flags通知标志位)。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| soundEnabled | [NotificationFlagStatus](js-apis-inner-notification-notificationflags.md#notificationflagstatus11) | 否 | 是 | 是否启用声音提示功能。默认值为TYPE\_NONE。从API version 23开始成为可写参数，设置时仅[TYPE\_CLOSE](js-apis-inner-notification-notificationflags.md#notificationflagstatus11)会生效。 |
| vibrationEnabled | [NotificationFlagStatus](js-apis-inner-notification-notificationflags.md#notificationflagstatus11) | 否 | 是 | 是否启用振动提醒功能。默认值为TYPE\_NONE。从API version 23开始成为可写参数，设置时仅[TYPE\_CLOSE](js-apis-inner-notification-notificationflags.md#notificationflagstatus11)会生效。 |
| bannerEnabled23+ | [NotificationFlagStatus](js-apis-inner-notification-notificationflags.md#notificationflagstatus11) | 否 | 是 | 是否启用横幅功能。默认值为TYPE\_NONE。设置时仅[TYPE\_CLOSE](js-apis-inner-notification-notificationflags.md#notificationflagstatus11)会生效。 |
| lockScreenEnabled23+ | [NotificationFlagStatus](js-apis-inner-notification-notificationflags.md#notificationflagstatus11) | 否 | 是 | 是否启用锁屏功能。默认值为TYPE\_NONE。设置时仅[TYPE\_CLOSE](js-apis-inner-notification-notificationflags.md#notificationflagstatus11)会生效。 |

## NotificationFlagStatus11+

描述通知标志状态。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TYPE\_NONE | 0 | 未设置标志时的默认值，与TYPE\_OPEN效果相同。 |
| TYPE\_OPEN | 1 | 通知标志打开。 |
| TYPE\_CLOSE | 2 | 通知标志关闭。 |
