---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/s-apis-inner-notification-notificationactionbutton
title: NotificationActionButton
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > ArkTS API > notification > NotificationActionButton
category: harmonyos-references
scraped_at: 2026-04-28T08:17:34+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:c8d5b730ebf56cfea4f1d7111db610dd5c6747777372e10d630ec6d8baef6a48
---

描述通知中显示的操作按钮。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## NotificationActionButton

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 按钮标题。字符串长度不超过200字节，超出部分会被截断；也不可为空字符串。 |
| wantAgent | [WantAgent](js-apis-app-ability-wantagent.md) | 否 | 否 | 点击按钮时触发的WantAgent。 |
| extras | { [key: string]: any } | 否 | 是 | 按钮扩展信息。预留能力，暂未支持。 |
| userInput8+ | [NotificationUserInput](js-apis-inner-notification-notificationuserinput.md) | 否 | 是 | 用户输入对象实例，默认为空。表示用户输入时的标识。 |
