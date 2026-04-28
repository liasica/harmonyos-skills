---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-backgroundtaskskit-6001
title: Background Tasks Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > Background Tasks Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:38+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d3d20622e6d26ab562d39b2eebfef87b45c4bea6f8ebe807ff90f2a60d6da8cb
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：reminderAgentManager；  API声明：function updateReminder(reminderId: number, reminderReq: ReminderRequest): Promise<void>;  差异内容：function updateReminder(reminderId: number, reminderReq: ReminderRequest): Promise<void>; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：reminderAgentManager；  API声明：export enum RingChannel  差异内容：export enum RingChannel | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：RingChannel；  API声明：RING\_CHANNEL\_ALARM = 0  差异内容：RING\_CHANNEL\_ALARM = 0 | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：RingChannel；  API声明：RING\_CHANNEL\_MEDIA = 1  差异内容：RING\_CHANNEL\_MEDIA = 1 | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：interface TransientTaskInfo  差异内容：interface TransientTaskInfo | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：TransientTaskInfo；  API声明：remainingQuota: number;  差异内容：remainingQuota: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：TransientTaskInfo；  API声明：transientTasks: DelaySuspendInfo[];  差异内容：transientTasks: DelaySuspendInfo[]; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：interface ContinuousTaskActiveInfo  差异内容：interface ContinuousTaskActiveInfo | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskActiveInfo；  API声明：id: number;  差异内容：id: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：interface ContinuousTaskInfo  差异内容：interface ContinuousTaskInfo | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo；  API声明：abilityName: string;  差异内容：abilityName: string; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo；  API声明：uid: number;  差异内容：uid: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo；  API声明：pid: number;  差异内容：pid: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo；  API声明：isFromWebView: boolean;  差异内容：isFromWebView: boolean; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo；  API声明：backgroundModes: string[];  差异内容：backgroundModes: string[]; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo；  API声明：backgroundSubModes: string[];  差异内容：backgroundSubModes: string[]; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo；  API声明：notificationId: number;  差异内容：notificationId: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo；  API声明：continuousTaskId: number;  差异内容：continuousTaskId: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo；  API声明：abilityId: number;  差异内容：abilityId: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo；  API声明：wantAgentBundleName: string;  差异内容：wantAgentBundleName: string; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo；  API声明：wantAgentAbilityName: string;  差异内容：wantAgentAbilityName: string; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：interface ContinuousTaskSuspendInfo  差异内容：interface ContinuousTaskSuspendInfo | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendInfo；  API声明：continuousTaskId: number;  差异内容：continuousTaskId: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendInfo；  API声明：suspendState: boolean;  差异内容：suspendState: boolean; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendInfo；  API声明：suspendReason: ContinuousTaskSuspendReason;  差异内容：suspendReason: ContinuousTaskSuspendReason; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：function getTransientTaskInfo(): Promise<TransientTaskInfo>;  差异内容：function getTransientTaskInfo(): Promise<TransientTaskInfo>; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：function getAllContinuousTasks(context: Context): Promise<ContinuousTaskInfo[]>;  差异内容：function getAllContinuousTasks(context: Context): Promise<ContinuousTaskInfo[]>; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：function on(type: 'continuousTaskSuspend', callback: Callback<ContinuousTaskSuspendInfo>): void;  差异内容：function on(type: 'continuousTaskSuspend', callback: Callback<ContinuousTaskSuspendInfo>): void; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：function off(type: 'continuousTaskSuspend', callback?: Callback<ContinuousTaskSuspendInfo>): void;  差异内容：function off(type: 'continuousTaskSuspend', callback?: Callback<ContinuousTaskSuspendInfo>): void; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：function on(type: 'continuousTaskActive', callback: Callback<ContinuousTaskActiveInfo>): void;  差异内容：function on(type: 'continuousTaskActive', callback: Callback<ContinuousTaskActiveInfo>): void; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：function off(type: 'continuousTaskActive', callback?: Callback<ContinuousTaskActiveInfo>): void;  差异内容：function off(type: 'continuousTaskActive', callback?: Callback<ContinuousTaskActiveInfo>): void; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：export enum ContinuousTaskSuspendReason  差异内容：export enum ContinuousTaskSuspendReason | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason；  API声明：SYSTEM\_SUSPEND\_DATA\_TRANSFER\_LOW\_SPEED = 4  差异内容：SYSTEM\_SUSPEND\_DATA\_TRANSFER\_LOW\_SPEED = 4 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason；  API声明：SYSTEM\_SUSPEND\_AUDIO\_PLAYBACK\_NOT\_USE\_AVSESSION = 5  差异内容：SYSTEM\_SUSPEND\_AUDIO\_PLAYBACK\_NOT\_USE\_AVSESSION = 5 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason；  API声明：SYSTEM\_SUSPEND\_AUDIO\_PLAYBACK\_NOT\_RUNNING = 6  差异内容：SYSTEM\_SUSPEND\_AUDIO\_PLAYBACK\_NOT\_RUNNING = 6 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason；  API声明：SYSTEM\_SUSPEND\_AUDIO\_RECORDING\_NOT\_RUNNING = 7  差异内容：SYSTEM\_SUSPEND\_AUDIO\_RECORDING\_NOT\_RUNNING = 7 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason；  API声明：SYSTEM\_SUSPEND\_LOCATION\_NOT\_USED = 8  差异内容：SYSTEM\_SUSPEND\_LOCATION\_NOT\_USED = 8 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason；  API声明：SYSTEM\_SUSPEND\_BLUETOOTH\_NOT\_USED = 9  差异内容：SYSTEM\_SUSPEND\_BLUETOOTH\_NOT\_USED = 9 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason；  API声明：SYSTEM\_SUSPEND\_MULTI\_DEVICE\_NOT\_USED = 10  差异内容：SYSTEM\_SUSPEND\_MULTI\_DEVICE\_NOT\_USED = 10 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason；  API声明：SYSTEM\_SUSPEND\_USED\_ILLEGALLY = 11  差异内容：SYSTEM\_SUSPEND\_USED\_ILLEGALLY = 11 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason；  API声明：SYSTEM\_SUSPEND\_SYSTEM\_LOAD\_WARNING = 12  差异内容：SYSTEM\_SUSPEND\_SYSTEM\_LOAD\_WARNING = 12 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ReminderRequest；  API声明：ringChannel?: RingChannel;  差异内容：ringChannel?: RingChannel; | api/@ohos.reminderAgentManager.d.ts |
