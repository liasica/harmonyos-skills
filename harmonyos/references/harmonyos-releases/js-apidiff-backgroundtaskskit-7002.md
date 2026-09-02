---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-backgroundtaskskit-7002
title: Background Tasks Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Background Tasks Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:03+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:dc2f756d0072656c8c9d4f9039061f120e06616ddfb5ba34012c77a16ed04aea
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：ContinuousTaskRequest；  API声明：requestAuthFromUserByDialog(context: Context, callback: Callback<UserAuthResult>): void;  差异内容：requestAuthFromUserByDialog(context: Context, callback: Callback<UserAuthResult>): void; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskRequest；  API声明：checkSpecialScenarioAuthResult(context: Context): Promise<UserAuthResult>;  差异内容：checkSpecialScenarioAuthResult(context: Context): Promise<UserAuthResult>; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：reminderAgentManager；  API声明：export enum TimeZoneType  差异内容：export enum TimeZoneType | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：TimeZoneType；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：TimeZoneType；  API声明：FIXED\_TIME\_ZONE = 1  差异内容：FIXED\_TIME\_ZONE = 1 | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：TimeZoneType；  API声明：SYSTEM\_TIME\_ZONE = 2  差异内容：SYSTEM\_TIME\_ZONE = 2 | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：reminderAgentManager；  API声明：interface NotificationRequestProxy  差异内容：interface NotificationRequestProxy | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：NotificationRequestProxy；  API声明：appMessageId?: string;  差异内容：appMessageId?: string; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：NotificationRequestProxy；  API声明：isAlertOnce?: boolean;  差异内容：isAlertOnce?: boolean; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：ReminderRequest；  API声明：fixedTimeZone?: TimeZoneType;  差异内容：fixedTimeZone?: TimeZoneType; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：ReminderRequest；  API声明：notificationRequestProxy?: NotificationRequestProxy;  差异内容：notificationRequestProxy?: NotificationRequestProxy; | api/@ohos.reminderAgentManager.d.ts |
| 删除API | 类名：ContinuousTaskDetailedCancelReason；  API声明：SYSTEM\_CANCEL\_AUDIO\_PLAYBACK\_NOT\_USE\_AVSESSION = 5  差异内容：SYSTEM\_CANCEL\_AUDIO\_PLAYBACK\_NOT\_USE\_AVSESSION = 5 | NA | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
