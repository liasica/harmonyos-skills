---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-notificationkit-7002
title: Notification Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Notification Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:caff63567739d3ada04f4d28c1cb905705d9c902ad2eeb46682f11d1cff43075
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：notificationManager；  API声明：function isDistributedEnabled(callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：notificationManager；  API声明：function isDistributedEnabled(callback: AsyncCallback<boolean>): void;  差异内容：26.0.0 | api/@ohos.notificationManager.d.ts |
| API废弃版本变更 | 类名：notificationManager；  API声明：function isDistributedEnabled(): Promise<boolean>;  差异内容：NA | 类名：notificationManager；  API声明：function isDistributedEnabled(): Promise<boolean>;  差异内容：26.0.0 | api/@ohos.notificationManager.d.ts |
| 新增错误码 | 类名：notificationManager；  API声明：function publish(request: NotificationRequest, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：notificationManager；  API声明：function publish(request: NotificationRequest, callback: AsyncCallback<void>): void;  差异内容：1600029 | api/@ohos.notificationManager.d.ts |
| 新增错误码 | 类名：notificationManager；  API声明：function publish(request: NotificationRequest): Promise<void>;  差异内容：NA | 类名：notificationManager；  API声明：function publish(request: NotificationRequest): Promise<void>;  差异内容：1600029 | api/@ohos.notificationManager.d.ts |
| 新增错误码 | 类名：notificationManager；  API声明：function isDistributedEnabled(callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：notificationManager；  API声明：function isDistributedEnabled(callback: AsyncCallback<boolean>): void;  差异内容：801 | api/@ohos.notificationManager.d.ts |
| 新增错误码 | 类名：notificationManager；  API声明：function isDistributedEnabled(): Promise<boolean>;  差异内容：NA | 类名：notificationManager；  API声明：function isDistributedEnabled(): Promise<boolean>;  差异内容：801 | api/@ohos.notificationManager.d.ts |
