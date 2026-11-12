---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-backgroundtaskskit-26011
title: Background Tasks Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Background Tasks Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:53+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:dada3366e482ebd1bbaf422cca57fd0e7072952907221bd98432f43def83231b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：backgroundTaskManager；  API声明：function startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>;  差异内容：NA | 类名：backgroundTaskManager；  API声明：function startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>;  差异内容：9800008 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增错误码 | 类名：backgroundTaskManager；  API声明：function updateBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>;  差异内容：NA | 类名：backgroundTaskManager；  API声明：function updateBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>;  差异内容：9800008 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskRequest；  API声明：progressInfo?: ProgressInfo;  差异内容：progressInfo?: ProgressInfo; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：export interface ProgressInfo  差异内容：export interface ProgressInfo | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ProgressInfo；  API声明：title: string;  差异内容：title: string; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ProgressInfo；  API声明：fileName: string;  差异内容：fileName: string; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ProgressInfo；  API声明：progressValue?: number;  差异内容：progressValue?: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ProgressInfo；  API声明：isMute?: boolean;  差异内容：isMute?: boolean; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：export interface DataTransferProgress  差异内容：export interface DataTransferProgress | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：DataTransferProgress；  API声明：continuousTaskId: number;  差异内容：continuousTaskId: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：DataTransferProgress；  API声明：wantAgent?: WantAgent;  差异内容：wantAgent?: WantAgent; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：DataTransferProgress；  API声明：progressInfo: ProgressInfo;  差异内容：progressInfo: ProgressInfo; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：function startContinuousTask(context: Context, request: ContinuousTaskRequest): Promise<number>;  差异内容：function startContinuousTask(context: Context, request: ContinuousTaskRequest): Promise<number>; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：function updateDataTransferProgress(context: Context, progressInfo: DataTransferProgress): void;  差异内容：function updateDataTransferProgress(context: Context, progressInfo: DataTransferProgress): void; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode；  API声明：MODE\_USB\_CONNECTION = 16  差异内容：MODE\_USB\_CONNECTION = 16 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason；  API声明：SYSTEM\_CANCEL\_NOT\_USE\_NEARLINK = 15  差异内容：SYSTEM\_CANCEL\_NOT\_USE\_NEARLINK = 15 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason；  API声明：SYSTEM\_CANCEL\_NOT\_USE\_USB = 16  差异内容：SYSTEM\_CANCEL\_NOT\_USE\_USB = 16 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason；  API声明：SYSTEM\_SUSPEND\_USB\_NOT\_USED = 20  差异内容：SYSTEM\_SUSPEND\_USB\_NOT\_USED = 20 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
