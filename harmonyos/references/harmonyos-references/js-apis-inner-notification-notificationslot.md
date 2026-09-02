---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationslot
title: NotificationSlot
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > ArkTS API > notification > NotificationSlot
category: harmonyos-references
scraped_at: 2026-09-02T15:03:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:77d6fcd199edeacf44afeaa297e7ec719b3c32eb78615f51568079f3edf2d83d
---

描述[通知渠道](../harmonyos-guides/notification-glossary.md#notification-slot通知渠道)，不同通知渠道对应的[通知提醒方式](../harmonyos-guides/notification-glossary.md#notification-reminder-mode通知提醒方式)不同。

**说明** 

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## NotificationSlot

**系统能力：** SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| notificationType11+ | [notificationManager.SlotType](js-apis-notificationmanager.md#slottype) | 否 | 是 | 渠道类型。不同渠道类型的[通知提醒方式](../harmonyos-guides/notification-glossary.md#notification-reminder-mode通知提醒方式)不同。 |
| enabled9+ | boolean | 是 | 是 | 是否允许发布此[通知渠道](../harmonyos-guides/notification-glossary.md#notification-slot通知渠道)类型的通知。  - true：允许发布通知。  - false：禁止发布通知。 |
| notificationLevel20+ | [notificationManager.SlotLevel](js-apis-notificationmanager.md#slotlevel) | 否 | 是 | 通知级别，用于描述该渠道类型通知的显示优先级和提醒强度。 |
| desc | string | 否 | 是 | 通知渠道描述信息。大小不超过243字节，超出部分会被截断。 |
| badgeFlag | boolean | 否 | 是 | 是否显示角标。默认值为true。  - true：显示角标。  - false：不显示角标。 |
| bypassDnd | boolean | 否 | 是 | 是否在系统中绕过[免打扰模式](../harmonyos-guides/notification-glossary.md#do-not-disturb-mode免打扰模式)。默认值为false。  - true：绕过免打扰模式，免打扰模式下仍会提醒。  - false：不绕过免打扰模式，免打扰模式下不提醒。 |
| vibrationEnabled | boolean | 否 | 是 | 是否可振动。默认值为false。  - true：可振动。  - false：不可振动。 |
| sound | string | 否 | 是 | 该渠道的通知的[自定义铃声](../harmonyos-guides/notification-glossary.md#customized-ringtone自定义铃声)文件名。该文件放在resources/rawfile目录下，支持m4a、aac、mp3、ogg、wav、flac、amr等格式。大小不超过243字节，超出部分会被截断。 |
| lightEnabled | boolean | 否 | 是 | 是否闪灯。默认值为false。  - true：闪灯。  - false：不闪灯。 |
| type(deprecated) | [notification.SlotType](js-apis-notification.md#slottype) | 否 | 是 | 渠道类型。  从API version 7开始支持，从API version 11开始废弃，建议使用notificationType替代。 |
| level(deprecated) | [notification.SlotLevel](js-apis-notificationmanager.md#slotlevel) | 否 | 是 | 通知级别。  从API version 7开始支持，从API version 20开始废弃，建议使用notificationLevel替代。 |
| lockscreenVisibility | number | 否 | 是 | 在锁定屏幕上显示通知的模式。预留能力，暂不支持。 |
| lightColor | number | 否 | 是 | 通知灯颜色。预留能力，暂不支持。 |
| vibrationValues | Array<number> | 否 | 是 | 通知振动样式。预留能力，暂不支持。 |
