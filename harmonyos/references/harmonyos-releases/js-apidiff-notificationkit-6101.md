---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-notificationkit-6101
title: Notification Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Notification Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a2bbecb386b476447586758ca831cbcc85478532ab587d60a8c272b44ffc9d10
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：notificationManager；  API声明：function isGeofenceEnabled(): Promise<boolean>;  差异内容：function isGeofenceEnabled(): Promise<boolean>; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：notificationManager；  API声明：export enum PriorityNotificationType  差异内容：export enum PriorityNotificationType | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：PriorityNotificationType；  API声明：OTHER = 'OTHER'  差异内容：OTHER = 'OTHER' | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：PriorityNotificationType；  API声明：PRIMARY\_CONTACT = 'PRIMARY\_CONTACT'  差异内容：PRIMARY\_CONTACT = 'PRIMARY\_CONTACT' | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：PriorityNotificationType；  API声明：AT\_ME = 'AT\_ME'  差异内容：AT\_ME = 'AT\_ME' | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：PriorityNotificationType；  API声明：URGENT\_MESSAGE = 'URGENT\_MESSAGE'  差异内容：URGENT\_MESSAGE = 'URGENT\_MESSAGE' | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：PriorityNotificationType；  API声明：SCHEDULE\_REMINDER = 'SCHEDULE\_REMINDER'  差异内容：SCHEDULE\_REMINDER = 'SCHEDULE\_REMINDER' | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：NotificationFlags；  API声明：bannerEnabled?: NotificationFlagStatus;  差异内容：bannerEnabled?: NotificationFlagStatus; | api/notification/notificationFlags.d.ts |
| 新增API | NA | 类名：NotificationFlags；  API声明：lockScreenEnabled?: NotificationFlagStatus;  差异内容：lockScreenEnabled?: NotificationFlagStatus; | api/notification/notificationFlags.d.ts |
| 新增API | NA | 类名：NotificationRequest；  API声明：priorityNotificationType?: notificationManager.PriorityNotificationType;  差异内容：priorityNotificationType?: notificationManager.PriorityNotificationType; | api/notification/notificationRequest.d.ts |
| 新增API | NA | 类名：NotificationRequest；  API声明：overlayIcon?: image.PixelMap;  差异内容：overlayIcon?: image.PixelMap; | api/notification/notificationRequest.d.ts |
