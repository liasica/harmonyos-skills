---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationextensioncontent
title: NotificationExtensionContent
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > ArkTS API > notification > NotificationExtensionContent
category: harmonyos-references
scraped_at: 2026-09-02T15:03:00+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:73552643dfe1dc6beb19af4f28733caad65c4f971a473ee634f09e2b782ee96e
---

通知扩展内容。

**说明** 

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## NotificationExtensionContent

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 通知标题。  不可为空字符串，大小不超过1024字节，超出部分会被截断。 |
| text | string | 否 | 否 | 通知正文内容。  不可为空字符串，大小不超过3072字节，超出部分会被截断。 |
