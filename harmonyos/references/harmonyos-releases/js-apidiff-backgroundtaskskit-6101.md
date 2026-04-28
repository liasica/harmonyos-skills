---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-backgroundtaskskit-6101
title: Background Tasks Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Background Tasks Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1f99ad39a91e172f46dcd2e3628db401ca4e4db7727df6daee835b4f61ebd7a2
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：reminderAgentManager；  API声明：function cancelReminderOnDisplay(reminderId: number): Promise<void>;  差异内容：function cancelReminderOnDisplay(reminderId: number): Promise<void>; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：reminderAgentManager；  API声明：function subscribeReminderState(callback: Callback<Array<ReminderState>>): Promise<void>;  差异内容：function subscribeReminderState(callback: Callback<Array<ReminderState>>): Promise<void>; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：reminderAgentManager；  API声明：function unsubscribeReminderState(callback?: Callback<Array<ReminderState>>): Promise<void>;  差异内容：function unsubscribeReminderState(callback?: Callback<Array<ReminderState>>): Promise<void>; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：RingChannel；  API声明：RING\_CHANNEL\_NOTIFICATION = 2  差异内容：RING\_CHANNEL\_NOTIFICATION = 2 | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：reminderAgentManager；  API声明：interface ReminderState  差异内容：interface ReminderState | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：ReminderState；  API声明：reminderId: number;  差异内容：reminderId: number; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：ReminderState；  API声明：buttonType: ActionButtonType;  差异内容：buttonType: ActionButtonType; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：ReminderState；  API声明：isMessageResent: boolean;  差异内容：isMessageResent: boolean; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：backgroundProcessManager；  API声明：function getPowerSaveMode(pid: number): Promise<PowerSaveMode>;  差异内容：function getPowerSaveMode(pid: number): Promise<PowerSaveMode>; | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo；  API声明：bundleName?: string;  差异内容：bundleName?: string; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo；  API声明：appIndex?: number;  差异内容：appIndex?: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode；  API声明：SUBMODE\_WORK\_OUT\_NORMAL\_NOTIFICATION = 11  差异内容：SUBMODE\_WORK\_OUT\_NORMAL\_NOTIFICATION = 11 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
