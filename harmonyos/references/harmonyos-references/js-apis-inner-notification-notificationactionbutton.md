---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationactionbutton
title: NotificationActionButton
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > ArkTS API > notification > NotificationActionButton
category: harmonyos-references
scraped_at: 2026-09-02T15:03:00+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0042d63db3cb6792d8578227375a5a607eba958a59570471214eca3dd50d06f8
---

NotificationActionButton模块定义了通知中显示的操作按钮，用于在[NotificationRequest](js-apis-inner-notification-notificationrequest.md#notificationrequest-1)中添加交互式操作按钮，让用户通过点击按钮触发WantAgent动作。当开发者需要在通知中提供交互式操作按钮（如"回复"、"标记已读"等）时使用此模块。

**说明** 

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## NotificationActionButton

**系统能力：** SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 按钮标题，显示在通知的操作按钮上。字符串长度不超过202字节，超出部分会被截断。不可为空字符串。 |
| wantAgent | [WantAgent](js-apis-app-ability-wantagent.md) | 否 | 否 | 点击按钮时触发的WantAgent，封装了应用的行为意图。用户点击按钮后，系统将按WantAgent指定的方式执行动作（如跳转至指定UIAbility或发送公共事件）。 |
| extras | { [key: string]: any } | 否 | 是 | 按钮扩展信息。默认为空。用于存储按钮的自定义扩展数据，应用可按需添加任意键值对信息，如按钮的特定标识、附加数据等。 |
| userInput8+ | [NotificationUserInput](js-apis-inner-notification-notificationuserinput.md) | 否 | 是 | 用户输入对象实例，默认为空。表示用户输入时的标识。 |
