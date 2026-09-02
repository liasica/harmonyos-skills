---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-backgroundtaskskit-7001
title: Background Tasks Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Background Tasks Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:05+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:e848146fda2f97df68adcd8fcdfa6efac2ffe75d26cdcb76650f6cd923f7f568
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：backgroundTaskManager；  API声明：function stopBackgroundRunning(context: Context, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：backgroundTaskManager；  API声明：function stopBackgroundRunning(context: Context, callback: AsyncCallback<void>): void;  差异内容：201 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增错误码 | 类名：backgroundTaskManager；  API声明：function stopBackgroundRunning(context: Context): Promise<void>;  差异内容：NA | 类名：backgroundTaskManager；  API声明：function stopBackgroundRunning(context: Context): Promise<void>;  差异内容：201 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskCancelInfo；  API声明：detailedReason?: ContinuousTaskDetailedCancelReason;  差异内容：detailedReason?: ContinuousTaskDetailedCancelReason; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendInfo；  API声明：suspendMessage?: SuspendMessage;  差异内容：suspendMessage?: SuspendMessage; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：interface SuspendMessage  差异内容：interface SuspendMessage | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：SuspendMessage；  API声明：message: string;  差异内容：message: string; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：SuspendMessage；  API声明：reason: ContinuousTaskSuspendReason;  差异内容：reason: ContinuousTaskSuspendReason; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode；  API声明：MODE\_NEARLINK = 14  差异内容：MODE\_NEARLINK = 14 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：export enum ContinuousTaskDetailedCancelReason  差异内容：export enum ContinuousTaskDetailedCancelReason | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason；  API声明：USER\_CANCEL\_REMOVE\_NOTIFICATION = 3  差异内容：USER\_CANCEL\_REMOVE\_NOTIFICATION = 3 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason；  API声明：SYSTEM\_CANCEL\_DATA\_TRANSFER\_LOW\_SPEED = 4  差异内容：SYSTEM\_CANCEL\_DATA\_TRANSFER\_LOW\_SPEED = 4 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason；  API声明：SYSTEM\_CANCEL\_AUDIO\_PLAYBACK\_NOT\_USE\_AVSESSION = 5  差异内容：SYSTEM\_CANCEL\_AUDIO\_PLAYBACK\_NOT\_USE\_AVSESSION = 5 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason；  API声明：SYSTEM\_CANCEL\_AUDIO\_PLAYBACK\_NOT\_RUNNING = 6  差异内容：SYSTEM\_CANCEL\_AUDIO\_PLAYBACK\_NOT\_RUNNING = 6 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason；  API声明：SYSTEM\_CANCEL\_AUDIO\_RECORDING\_NOT\_RUNNING = 7  差异内容：SYSTEM\_CANCEL\_AUDIO\_RECORDING\_NOT\_RUNNING = 7 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason；  API声明：SYSTEM\_CANCEL\_NOT\_USE\_LOCATION = 8  差异内容：SYSTEM\_CANCEL\_NOT\_USE\_LOCATION = 8 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason；  API声明：SYSTEM\_CANCEL\_NOT\_USE\_BLUETOOTH = 9  差异内容：SYSTEM\_CANCEL\_NOT\_USE\_BLUETOOTH = 9 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason；  API声明：SYSTEM\_CANCEL\_NOT\_USE\_MULTI\_DEVICE = 10  差异内容：SYSTEM\_CANCEL\_NOT\_USE\_MULTI\_DEVICE = 10 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason；  API声明：SYSTEM\_CANCEL\_USE\_ILLEGALLY = 11  差异内容：SYSTEM\_CANCEL\_USE\_ILLEGALLY = 11 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason；  API声明：SYSTEM\_CANCEL\_DATA\_TRANSFER\_NOT\_UPDATE = 12  差异内容：SYSTEM\_CANCEL\_DATA\_TRANSFER\_NOT\_UPDATE = 12 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason；  API声明：SYSTEM\_CANCEL\_VOIP\_NOT\_RUNNING = 13  差异内容：SYSTEM\_CANCEL\_VOIP\_NOT\_RUNNING = 13 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason；  API声明：SYSTEM\_CANCEL\_USER\_UNAUTHORIZED = 14  差异内容：SYSTEM\_CANCEL\_USER\_UNAUTHORIZED = 14 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason；  API声明：SYSTEM\_SUSPEND\_VOIP\_NOT\_USED = 13  差异内容：SYSTEM\_SUSPEND\_VOIP\_NOT\_USED = 13 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason；  API声明：SYSTEM\_SUSPEND\_BLUETOOTH\_DATA\_NOT\_EXIST = 14  差异内容：SYSTEM\_SUSPEND\_BLUETOOTH\_DATA\_NOT\_EXIST = 14 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason；  API声明：SYSTEM\_SUSPEND\_POSITION\_NOT\_MOVED = 15  差异内容：SYSTEM\_SUSPEND\_POSITION\_NOT\_MOVED = 15 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason；  API声明：SYSTEM\_SUSPEND\_AUDIO\_PLAYBACK\_MUTE = 16  差异内容：SYSTEM\_SUSPEND\_AUDIO\_PLAYBACK\_MUTE = 16 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason；  API声明：SYSTEM\_SUSPEND\_NEARLINK\_NOT\_USED = 17  差异内容：SYSTEM\_SUSPEND\_NEARLINK\_NOT\_USED = 17 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason；  API声明：SYSTEM\_SUSPEND\_NEARLINK\_DATA\_NOT\_EXIST = 18  差异内容：SYSTEM\_SUSPEND\_NEARLINK\_DATA\_NOT\_EXIST = 18 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason；  API声明：SYSTEM\_SUSPEND\_USER\_UNAUTHORIZED = 19  差异内容：SYSTEM\_SUSPEND\_USER\_UNAUTHORIZED = 19 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ReminderRequestTimer；  API声明：repeatInterval?: number;  差异内容：repeatInterval?: number; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：ReminderRequestTimer；  API声明：repeatCount?: number;  差异内容：repeatCount?: number; | api/@ohos.reminderAgentManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：backgroundTaskManager；  API声明：export class ContinuousTaskRequest  差异内容：NA | 类名：backgroundTaskManager；  API声明：export class ContinuousTaskRequest  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：ContinuousTaskRequest；  API声明：get backgroundTaskModes(): BackgroundTaskMode[];  差异内容：NA | 类名：ContinuousTaskRequest；  API声明：get backgroundTaskModes(): BackgroundTaskMode[];  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：ContinuousTaskRequest；  API声明：get backgroundTaskSubmodes(): BackgroundTaskSubmode[];  差异内容：NA | 类名：ContinuousTaskRequest；  API声明：get backgroundTaskSubmodes(): BackgroundTaskSubmode[];  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：ContinuousTaskRequest；  API声明：get wantAgent(): WantAgent;  差异内容：NA | 类名：ContinuousTaskRequest；  API声明：get wantAgent(): WantAgent;  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：ContinuousTaskRequest；  API声明：combinedTaskNotification?: boolean;  差异内容：NA | 类名：ContinuousTaskRequest；  API声明：combinedTaskNotification?: boolean;  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：ContinuousTaskRequest；  API声明：continuousTaskId?: number;  差异内容：NA | 类名：ContinuousTaskRequest；  API声明：continuousTaskId?: number;  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：ContinuousTaskRequest；  API声明：isModeSupported(): boolean;  差异内容：NA | 类名：ContinuousTaskRequest；  API声明：isModeSupported(): boolean;  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：ContinuousTaskNotification；  API声明：continuousTaskId?: number;  差异内容：NA | 类名：ContinuousTaskNotification；  API声明：continuousTaskId?: number;  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：backgroundTaskManager；  API声明：function startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>;  差异内容：NA | 类名：backgroundTaskManager；  API声明：function startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>;  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：backgroundTaskManager；  API声明：function updateBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>;  差异内容：NA | 类名：backgroundTaskManager；  API声明：function updateBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>;  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：backgroundTaskManager；  API声明：function stopBackgroundRunning(context: Context, continuousTaskId: number): Promise<void>;  差异内容：NA | 类名：backgroundTaskManager；  API声明：function stopBackgroundRunning(context: Context, continuousTaskId: number): Promise<void>;  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：BackgroundMode；  API声明：LOCATION = 4  差异内容：NA | 类名：BackgroundMode；  API声明：LOCATION = 4  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：backgroundTaskManager；  API声明：export enum BackgroundTaskMode  差异内容：NA | 类名：backgroundTaskManager；  API声明：export enum BackgroundTaskMode  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：BackgroundTaskMode；  API声明：MODE\_AUDIO\_PLAYBACK = 2  差异内容：NA | 类名：BackgroundTaskMode；  API声明：MODE\_AUDIO\_PLAYBACK = 2  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：BackgroundTaskMode；  API声明：MODE\_LOCATION = 4  差异内容：NA | 类名：BackgroundTaskMode；  API声明：MODE\_LOCATION = 4  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：BackgroundTaskMode；  API声明：MODE\_MULTI\_DEVICE\_CONNECTION = 6  差异内容：NA | 类名：BackgroundTaskMode；  API声明：MODE\_MULTI\_DEVICE\_CONNECTION = 6  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：BackgroundTaskMode；  API声明：MODE\_AV\_PLAYBACK\_AND\_RECORD = 12  差异内容：NA | 类名：BackgroundTaskMode；  API声明：MODE\_AV\_PLAYBACK\_AND\_RECORD = 12  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：backgroundTaskManager；  API声明：export enum BackgroundTaskSubmode  差异内容：NA | 类名：backgroundTaskManager；  API声明：export enum BackgroundTaskSubmode  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：BackgroundTaskSubmode；  API声明：SUBMODE\_NORMAL\_NOTIFICATION = 2  差异内容：NA | 类名：BackgroundTaskSubmode；  API声明：SUBMODE\_NORMAL\_NOTIFICATION = 2  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：BackgroundTaskSubmode；  API声明：SUBMODE\_AUDIO\_PLAYBACK\_NORMAL\_NOTIFICATION = 4  差异内容：NA | 类名：BackgroundTaskSubmode；  API声明：SUBMODE\_AUDIO\_PLAYBACK\_NORMAL\_NOTIFICATION = 4  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：BackgroundTaskSubmode；  API声明：SUBMODE\_AVSESSION\_AUDIO\_PLAYBACK = 5  差异内容：NA | 类名：BackgroundTaskSubmode；  API声明：SUBMODE\_AVSESSION\_AUDIO\_PLAYBACK = 5  差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
