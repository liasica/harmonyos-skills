---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-notificationkit-6111
title: Notification Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > Notification Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:08+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:30a02d67062b13396d45cb8c0e92a71e8b3637de9eee19e44b8a6d4cd4dfd83e
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：export interface NotificationParameters  差异内容：export interface NotificationParameters | api/notification/notificationRequest.d.ts |
| 新增API | NA | 类名：NotificationParameters；  API声明：wantAction?: string;  差异内容：wantAction?: string; | api/notification/notificationRequest.d.ts |
| 新增API | NA | 类名：NotificationParameters；  API声明：wantUri?: string;  差异内容：wantUri?: string; | api/notification/notificationRequest.d.ts |
| 新增API | NA | 类名：NotificationParameters；  API声明：wantParameters?: Record<string, Object>;  差异内容：wantParameters?: Record<string, Object>; | api/notification/notificationRequest.d.ts |
| 新增API | NA | 类名：notificationManager；  API声明：function getNotificationParameters(id: number, label?: string): Promise<NotificationParameters>;  差异内容：function getNotificationParameters(id: number, label?: string): Promise<NotificationParameters>; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：notificationManager；  API声明：export type NotificationParameters = \_NotificationParameters;  差异内容：export type NotificationParameters = \_NotificationParameters; | api/@ohos.notificationManager.d.ts |
