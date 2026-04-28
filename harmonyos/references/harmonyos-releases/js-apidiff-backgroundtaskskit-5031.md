---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-backgroundtaskskit-5031
title: Background Tasks Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta1引入的API > Background Tasks Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:40+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:6457334e3df669b5c283727e9434df7fc8b535d04eb7fc32ff2f37861a4cffe3
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：ContinuousTaskNotification；  API声明：continuousTaskId?: number;  差异内容：continuousTaskId?: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明： interface ContinuousTaskCancelInfo  差异内容： interface ContinuousTaskCancelInfo | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskCancelInfo；  API声明：reason: ContinuousTaskCancelReason;  差异内容：reason: ContinuousTaskCancelReason; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskCancelInfo；  API声明：id: number;  差异内容：id: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：function on(type: 'continuousTaskCancel', callback: Callback<ContinuousTaskCancelInfo>): void;  差异内容：function on(type: 'continuousTaskCancel', callback: Callback<ContinuousTaskCancelInfo>): void; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：function off(type: 'continuousTaskCancel', callback?: Callback<ContinuousTaskCancelInfo>): void;  差异内容：function off(type: 'continuousTaskCancel', callback?: Callback<ContinuousTaskCancelInfo>): void; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明： export enum ContinuousTaskCancelReason  差异内容： export enum ContinuousTaskCancelReason | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskCancelReason；  API声明：USER\_CANCEL = 1  差异内容：USER\_CANCEL = 1 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskCancelReason；  API声明：SYSTEM\_CANCEL = 2  差异内容：SYSTEM\_CANCEL = 2 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskCancelReason；  API声明：USER\_CANCEL\_REMOVE\_NOTIFICATION = 3  差异内容：USER\_CANCEL\_REMOVE\_NOTIFICATION = 3 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskCancelReason；  API声明：SYSTEM\_CANCEL\_DATA\_TRANSFER\_LOW\_SPEED = 4  差异内容：SYSTEM\_CANCEL\_DATA\_TRANSFER\_LOW\_SPEED = 4 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskCancelReason；  API声明：SYSTEM\_CANCEL\_AUDIO\_PLAYBACK\_NOT\_USE\_AVSESSION = 5  差异内容：SYSTEM\_CANCEL\_AUDIO\_PLAYBACK\_NOT\_USE\_AVSESSION = 5 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskCancelReason；  API声明：SYSTEM\_CANCEL\_AUDIO\_PLAYBACK\_NOT\_RUNNING = 6  差异内容：SYSTEM\_CANCEL\_AUDIO\_PLAYBACK\_NOT\_RUNNING = 6 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskCancelReason；  API声明：SYSTEM\_CANCEL\_AUDIO\_RECORDING\_NOT\_RUNNING = 7  差异内容：SYSTEM\_CANCEL\_AUDIO\_RECORDING\_NOT\_RUNNING = 7 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskCancelReason；  API声明：SYSTEM\_CANCEL\_NOT\_USE\_LOCATION = 8  差异内容：SYSTEM\_CANCEL\_NOT\_USE\_LOCATION = 8 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskCancelReason；  API声明：SYSTEM\_CANCEL\_NOT\_USE\_BLUETOOTH = 9  差异内容：SYSTEM\_CANCEL\_NOT\_USE\_BLUETOOTH = 9 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskCancelReason；  API声明：SYSTEM\_CANCEL\_NOT\_USE\_MULTI\_DEVICE = 10  差异内容：SYSTEM\_CANCEL\_NOT\_USE\_MULTI\_DEVICE = 10 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskCancelReason；  API声明：SYSTEM\_CANCEL\_USE\_ILLEGALLY = 11  差异内容：SYSTEM\_CANCEL\_USE\_ILLEGALLY = 11 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
