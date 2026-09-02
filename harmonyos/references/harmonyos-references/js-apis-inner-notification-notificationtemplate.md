---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationtemplate
title: NotificationTemplate
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > ArkTS API > notification > NotificationTemplate
category: harmonyos-references
scraped_at: 2026-09-02T15:03:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cdd9a831ab336b07c2e966c2cd7da09b4b4e167150b682a4128052a43f876ebb
---

通知模板。用于指定通知所使用的模板类型。

**说明** 

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

提供预定义模板支持。允许应用开发者使用系统预定义的通知模板，只需提供模板名称和相应的数据，系统会自动渲染出符合规范的通知样式。

使用场景：当前仅支持上传下载场景。

## NotificationTemplate

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 模板名称。当前仅支持表示下载进度的进度条通知模板，取值为'downloadTemplate'。字符串长度不超过202字节，超出部分会被截断。不可为空字符串。 |
| data | Record<string, Object> | 否 | 否 | 模板数据。  - title: 表示下载标题。必填字段，值为字符串类型。  - fileName: 表示下载文件名。必填字段，值为字符串类型。  - progressValue: 表示下载进度，值为数值类型。建议取值范围为0~100，表示百分比进度。当progressValue取值小于或等于0时，进度为0；当其取值大于或等于100时，进度环消失，代表下载完成。 |
