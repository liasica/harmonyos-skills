---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corefilekit-6002
title: Core File Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > Core File Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:27+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:54f5622de70988815e2434a3e799f5ec981957b2960178d53f6831f37587dc50
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：cloudSyncManager；  API声明：enum DownloadStopReason  差异内容：enum DownloadStopReason | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：DownloadStopReason；  API声明：NO\_STOP = 0  差异内容：NO\_STOP = 0 | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：DownloadStopReason；  API声明：NETWORK\_UNAVAILABLE = 1  差异内容：NETWORK\_UNAVAILABLE = 1 | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：DownloadStopReason；  API声明：LOCAL\_STORAGE\_FULL = 2  差异内容：LOCAL\_STORAGE\_FULL = 2 | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：DownloadStopReason；  API声明：TEMPERATURE\_LIMIT = 3  差异内容：TEMPERATURE\_LIMIT = 3 | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：DownloadStopReason；  API声明：USER\_STOPPED = 4  差异内容：USER\_STOPPED = 4 | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：DownloadStopReason；  API声明：APP\_UNLOAD = 5  差异内容：APP\_UNLOAD = 5 | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：DownloadStopReason；  API声明：OTHER\_REASON = 6  差异内容：OTHER\_REASON = 6 | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：cloudSyncManager；  API声明：enum DownloadState  差异内容：enum DownloadState | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：DownloadState；  API声明：RUNNING = 0  差异内容：RUNNING = 0 | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：DownloadState；  API声明：COMPLETED = 1  差异内容：COMPLETED = 1 | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：DownloadState；  API声明：STOPPED = 2  差异内容：STOPPED = 2 | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：cloudSyncManager；  API声明：interface CloudFileInfo  差异内容：interface CloudFileInfo | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：CloudFileInfo；  API声明：cloudFileCount: number;  差异内容：cloudFileCount: number; | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：CloudFileInfo；  API声明：cloudFileTotalSize: number;  差异内容：cloudFileTotalSize: number; | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：CloudFileInfo；  API声明：localFileCount: number;  差异内容：localFileCount: number; | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：CloudFileInfo；  API声明：localFileTotalSize: number;  差异内容：localFileTotalSize: number; | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：CloudFileInfo；  API声明：bothFileCount: number;  差异内容：bothFileCount: number; | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：CloudFileInfo；  API声明：bothFileTotalSize: number;  差异内容：bothFileTotalSize: number; | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：cloudSyncManager；  API声明：class DownloadProgress  差异内容：class DownloadProgress | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：DownloadProgress；  API声明：state: DownloadState;  差异内容：state: DownloadState; | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：DownloadProgress；  API声明：successfulCount: number;  差异内容：successfulCount: number; | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：DownloadProgress；  API声明：failedCount: number;  差异内容：failedCount: number; | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：DownloadProgress；  API声明：totalCount: number;  差异内容：totalCount: number; | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：DownloadProgress；  API声明：downloadedSize: number;  差异内容：downloadedSize: number; | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：DownloadProgress；  API声明：totalSize: number;  差异内容：totalSize: number; | api/@ohos.file.cloudSyncManager.d.ts |
| 新增API | NA | 类名：DownloadProgress；  API声明：stopReason: DownloadStopReason;  差异内容：stopReason: DownloadStopReason; | api/@ohos.file.cloudSyncManager.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：BackupExtensionAbility；  API声明：onRelease(scenario: number): Promise<void>;  差异内容：onRelease(scenario: number): Promise<void>; | api/@ohos.application.BackupExtensionAbility.d.ts |
