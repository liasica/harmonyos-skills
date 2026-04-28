---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/is-inner-notification-notificationextensioncontent
title: NotificationExtensionContent
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > ArkTS API > notification > NotificationExtensionContent
category: harmonyos-references
scraped_at: 2026-04-28T08:17:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7f8db27f87c54b666df31b8550a484b96b844816c84aac22afa718fc709823fe
---

通知扩展内容。

说明

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## NotificationExtensionContent

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 通知标题。不能为空且不能超过1024字节，超出内容将被截断。 |
| text | string | 否 | 否 | 通知内容。不能为空且不能超过3072字节，超出内容将被截断。 |
