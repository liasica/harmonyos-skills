---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationslot
title: NotificationSlot
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > ArkTS API > notification > NotificationSlot
category: harmonyos-references
scraped_at: 2026-04-28T08:17:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:549c710414459306fe83ec62a92e5a23faa37eb2c62f913936ad990a56abb40a
---

描述通知渠道，不同通知渠道对应的通知提醒方式不同。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## NotificationSlot

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type(deprecated) | [notification.SlotType](js-apis-notification.md#slottype) | 否 | 是 | 通道类型。  从API version 7开始支持，从API version 11开始废弃，建议使用notificationType替代。 |
| notificationType11+ | [notificationManager.SlotType](js-apis-notificationmanager.md#slottype) | 否 | 是 | 通道类型。 |
| level(deprecated) | [notification.SlotLevel](js-apis-notificationmanager.md#slotlevel) | 否 | 是 | 通知级别。  从API version 7开始支持，从API version 20开始废弃，建议使用notificationLevel替代。 |
| notificationLevel20+ | [notificationManager.SlotLevel](js-apis-notificationmanager.md#slotlevel) | 否 | 是 | 通知级别。 |
| desc | string | 否 | 是 | 通知渠道描述信息。 |
| badgeFlag | boolean | 否 | 是 | 是否显示角标。  - true：是。  - false：否。 |
| bypassDnd | boolean | 否 | 是 | 是否在系统中绕过免打扰模式。  - true：是。  - false：否。 |
| lockscreenVisibility | number | 否 | 是 | 在锁定屏幕上显示通知的模式。预留能力，暂不支持。 |
| vibrationEnabled | boolean | 否 | 是 | 是否可振动。  - true：是。  - false：否。 |
| sound | string | 否 | 是 | 该渠道的通知的自定义铃声文件名。该文件放在resources/rawfile目录下，支持m4a、aac、mp3、ogg、wav、flac、amr等格式。 |
| lightEnabled | boolean | 否 | 是 | 是否闪灯。  - true：是。  - false：否。 |
| lightColor | number | 否 | 是 | 通知灯颜色。预留能力，暂不支持。 |
| vibrationValues | Array<number> | 否 | 是 | 通知振动样式。预留能力，暂不支持。 |
| enabled9+ | boolean | 是 | 是 | 表示是否允许发布此通知渠道的通知。  - true：允许。  - false：禁止。 |
