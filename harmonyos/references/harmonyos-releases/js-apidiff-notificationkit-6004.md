---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-notificationkit-6004
title: Notification Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta5引入的API > Notification Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:10+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:dc29890f39837a6d5e7a7436634ddff1cd6d4b73119ab5b2672ea2c223a55a8b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：NotificationSlot；  API声明：level?: notification.SlotLevel;  差异内容：NA | 类名：NotificationSlot；  API声明：level?: notification.SlotLevel;  差异内容：20 | api/notification/notificationSlot.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：NotificationSlot；  API声明：notificationLevel?: notificationManager.SlotLevel;  差异内容：notificationLevel?: notificationManager.SlotLevel; | api/notification/notificationSlot.d.ts |
