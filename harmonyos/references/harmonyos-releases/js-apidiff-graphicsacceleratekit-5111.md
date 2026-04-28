---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-graphicsacceleratekit-5111
title: Graphics Accelerate Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > Graphics Accelerate Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:54+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:8701aeb901a9fe4171c3630f7f6b3e1001b28db38edaebab75b8d944854c151e
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：assetDownloadManager；  API声明：export enum AppDownloadStatus  差异内容：export enum AppDownloadStatus | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：AppDownloadStatus；  API声明：IN\_PROGRESS = 0  差异内容：IN\_PROGRESS = 0 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：AppDownloadStatus；  API声明：FINISH = 1  差异内容：FINISH = 1 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：export interface AppDownloadProgress  差异内容：export interface AppDownloadProgress | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：AppDownloadProgress；  API声明：totalBytesWritten: number;  差异内容：totalBytesWritten: number; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：AppDownloadProgress；  API声明：totalExpectedBytes: number;  差异内容：totalExpectedBytes: number; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：AppDownloadProgress；  API声明：totalFiles: number;  差异内容：totalFiles: number; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：AppDownloadProgress；  API声明：successCount: number;  差异内容：successCount: number; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：AppDownloadProgress；  API声明：failureCount: number;  差异内容：failureCount: number; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：AppDownloadProgress；  API声明：status: AppDownloadStatus;  差异内容：status: AppDownloadStatus; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function reportDownloadProgress(progressInfo: AppDownloadProgress): void;  差异内容：function reportDownloadProgress(progressInfo: AppDownloadProgress): void; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：AssetAccelerationExtensionAbility；  API声明：onDownloadWithAppControl(requestType: ContentRequestType, manifestUrl: string, assetAccelerationExtensionInfo: AssetAccelerationExtensionInfo): Promise<boolean>;  差异内容：onDownloadWithAppControl(requestType: ContentRequestType, manifestUrl: string, assetAccelerationExtensionInfo: AssetAccelerationExtensionInfo): Promise<boolean>; | api/@hms.gameAcceleration.AssetAccelerationExtensionAbility.d.ts |
