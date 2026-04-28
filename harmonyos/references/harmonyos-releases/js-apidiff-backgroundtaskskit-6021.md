---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-backgroundtaskskit-6021
title: Background Tasks Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > Background Tasks Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:43+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a4b6477337ca6a99a566d5e5dfd35cbb4c4963d0b79639347cae3955aab34855
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：ContinuousTaskRequest；  API声明：requestAuthFromUser(context: Context, callback: Callback<UserAuthResult>): void;  差异内容：requestAuthFromUser(context: Context, callback: Callback<UserAuthResult>): void; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskRequest；  API声明：checkSpecialScenarioAuth(context: Context): Promise<UserAuthResult>;  差异内容：checkSpecialScenarioAuth(context: Context): Promise<UserAuthResult>; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode；  API声明：MODE\_AV\_PLAYBACK\_AND\_RECORD = 12  差异内容：MODE\_AV\_PLAYBACK\_AND\_RECORD = 12 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode；  API声明：MODE\_SPECIAL\_SCENARIO\_PROCESSING = 13  差异内容：MODE\_SPECIAL\_SCENARIO\_PROCESSING = 13 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode；  API声明：SUBMODE\_AUDIO\_PLAYBACK\_NORMAL\_NOTIFICATION = 4  差异内容：SUBMODE\_AUDIO\_PLAYBACK\_NORMAL\_NOTIFICATION = 4 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode；  API声明：SUBMODE\_AVSESSION\_AUDIO\_PLAYBACK = 5  差异内容：SUBMODE\_AVSESSION\_AUDIO\_PLAYBACK = 5 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode；  API声明：SUBMODE\_AUDIO\_RECORD\_NORMAL\_NOTIFICATION = 6  差异内容：SUBMODE\_AUDIO\_RECORD\_NORMAL\_NOTIFICATION = 6 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode；  API声明：SUBMODE\_SCREEN\_RECORD\_NORMAL\_NOTIFICATION = 7  差异内容：SUBMODE\_SCREEN\_RECORD\_NORMAL\_NOTIFICATION = 7 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode；  API声明：SUBMODE\_VOICE\_CHAT\_NORMAL\_NOTIFICATION = 8  差异内容：SUBMODE\_VOICE\_CHAT\_NORMAL\_NOTIFICATION = 8 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode；  API声明：SUBMODE\_MEDIA\_PROCESS\_NORMAL\_NOTIFICATION = 9  差异内容：SUBMODE\_MEDIA\_PROCESS\_NORMAL\_NOTIFICATION = 9 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode；  API声明：SUBMODE\_VIDEO\_BROADCAST\_NORMAL\_NOTIFICATION = 10  差异内容：SUBMODE\_VIDEO\_BROADCAST\_NORMAL\_NOTIFICATION = 10 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：export enum UserAuthResult  差异内容：export enum UserAuthResult | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：UserAuthResult；  API声明：NOT\_SUPPORTED = 0  差异内容：NOT\_SUPPORTED = 0 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：UserAuthResult；  API声明：NOT\_DETERMINED = 1  差异内容：NOT\_DETERMINED = 1 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：UserAuthResult；  API声明：DENIED = 2  差异内容：DENIED = 2 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：UserAuthResult；  API声明：GRANTED\_ONCE = 3  差异内容：GRANTED\_ONCE = 3 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：UserAuthResult；  API声明：GRANTED\_ALWAYS = 4  差异内容：GRANTED\_ALWAYS = 4 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：WorkInfo；  API声明：earliestStartTime?: number;  差异内容：earliestStartTime?: number; | api/@ohos.resourceschedule.workScheduler.d.ts |
