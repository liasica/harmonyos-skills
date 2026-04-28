---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-backgroundtaskskit-6011
title: Background Tasks Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Beta1引入的API > Background Tasks Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:56+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:952258f50f7ea311f30836c8b57dbb641e2b8176a17c5623187b478f8bdd61ac
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API模型切换 | 类名：global；  API声明：declare class WorkSchedulerExtensionAbility  差异内容：NA | 类名：global；  API声明：declare class WorkSchedulerExtensionAbility  差异内容：stagemodelonly | api/@ohos.WorkSchedulerExtensionAbility.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：function startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>;  差异内容：function startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：function updateBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>;  差异内容：function updateBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：function stopBackgroundRunning(context: Context, continuousTaskId: number): Promise<void>;  差异内容：function stopBackgroundRunning(context: Context, continuousTaskId: number): Promise<void>; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：export class ContinuousTaskRequest  差异内容：export class ContinuousTaskRequest | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskRequest；  API声明：backgroundTaskModes: BackgroundTaskMode[];  差异内容：backgroundTaskModes: BackgroundTaskMode[]; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskRequest；  API声明：backgroundTaskSubmodes: BackgroundTaskSubmode[];  差异内容：backgroundTaskSubmodes: BackgroundTaskSubmode[]; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskRequest；  API声明：wantAgent: WantAgent;  差异内容：wantAgent: WantAgent; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskRequest；  API声明：combinedTaskNotification?: boolean;  差异内容：combinedTaskNotification?: boolean; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskRequest；  API声明：continuousTaskId?: number;  差异内容：continuousTaskId?: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskRequest；  API声明：isModeSupported(): boolean;  差异内容：isModeSupported(): boolean; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：export enum BackgroundTaskMode  差异内容：export enum BackgroundTaskMode | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode；  API声明：MODE\_DATA\_TRANSFER = 1  差异内容：MODE\_DATA\_TRANSFER = 1 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode；  API声明：MODE\_AUDIO\_PLAYBACK = 2  差异内容：MODE\_AUDIO\_PLAYBACK = 2 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode；  API声明：MODE\_AUDIO\_RECORDING = 3  差异内容：MODE\_AUDIO\_RECORDING = 3 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode；  API声明：MODE\_LOCATION = 4  差异内容：MODE\_LOCATION = 4 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode；  API声明：MODE\_BLUETOOTH\_INTERACTION = 5  差异内容：MODE\_BLUETOOTH\_INTERACTION = 5 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode；  API声明：MODE\_MULTI\_DEVICE\_CONNECTION = 6  差异内容：MODE\_MULTI\_DEVICE\_CONNECTION = 6 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode；  API声明：MODE\_VOIP = 8  差异内容：MODE\_VOIP = 8 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode；  API声明：MODE\_TASK\_KEEPING = 9  差异内容：MODE\_TASK\_KEEPING = 9 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：export enum BackgroundTaskSubmode  差异内容：export enum BackgroundTaskSubmode | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode；  API声明：SUBMODE\_CAR\_KEY\_NORMAL\_NOTIFICATION = 1  差异内容：SUBMODE\_CAR\_KEY\_NORMAL\_NOTIFICATION = 1 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode；  API声明：SUBMODE\_NORMAL\_NOTIFICATION = 2  差异内容：SUBMODE\_NORMAL\_NOTIFICATION = 2 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode；  API声明：SUBMODE\_LIVE\_VIEW\_NOTIFICATION = 3  差异内容：SUBMODE\_LIVE\_VIEW\_NOTIFICATION = 3 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
