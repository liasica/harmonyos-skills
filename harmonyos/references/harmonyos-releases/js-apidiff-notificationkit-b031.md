---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-notificationkit-b031
title: Notification Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Notification Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:42+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:0396c18ce4bd9218e6ae6c78bf38c5af01cfd48ab37d3fcc321e4a8e6bd7bbae
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：notificationManager；  API声明：function requestEnableNotification(callback: AsyncCallback<void>): void;  差异内容：NA | 类名：notificationManager；  API声明：function requestEnableNotification(callback: AsyncCallback<void>): void;  差异内容：12 | api/@ohos.notificationManager.d.ts |
| API废弃版本变更 | 类名：notificationManager；  API声明：function requestEnableNotification(): Promise<void>;  差异内容：NA | 类名：notificationManager；  API声明：function requestEnableNotification(): Promise<void>;  差异内容：12 | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：notificationManager；  API声明：function isNotificationEnabledSync(): boolean;  差异内容：function isNotificationEnabledSync(): boolean; | api/@ohos.notificationManager.d.ts |
