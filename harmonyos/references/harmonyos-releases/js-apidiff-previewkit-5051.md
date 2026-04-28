---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-previewkit-5051
title: Preview Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.5(17) > OS平台能力 > API变更清单 > Preview Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:20+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:908552419361366b611d429d2b4656bb24da2798803957e2a4ca04d5efafb6ed
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace openFileBoost  差异内容：declare namespace openFileBoost | api/@hms.pcService.openFileBoost.d.ts |
| 新增API | NA | 类名：openFileBoost；  API声明：export enum FilePreloadState  差异内容：export enum FilePreloadState | api/@hms.pcService.openFileBoost.d.ts |
| 新增API | NA | 类名：FilePreloadState；  API声明：NOT\_PRELOADED = 0  差异内容：NOT\_PRELOADED = 0 | api/@hms.pcService.openFileBoost.d.ts |
| 新增API | NA | 类名：FilePreloadState；  API声明：PRELOADING = 1  差异内容：PRELOADING = 1 | api/@hms.pcService.openFileBoost.d.ts |
| 新增API | NA | 类名：FilePreloadState；  API声明：PRELOADED = 2  差异内容：PRELOADED = 2 | api/@hms.pcService.openFileBoost.d.ts |
| 新增API | NA | 类名：openFileBoost；  API声明：export interface FilePreloadStatusInfo  差异内容：export interface FilePreloadStatusInfo | api/@hms.pcService.openFileBoost.d.ts |
| 新增API | NA | 类名：FilePreloadStatusInfo；  API声明：sandboxPath: string;  差异内容：sandboxPath: string; | api/@hms.pcService.openFileBoost.d.ts |
| 新增API | NA | 类名：FilePreloadStatusInfo；  API声明：progress: number;  差异内容：progress: number; | api/@hms.pcService.openFileBoost.d.ts |
| 新增API | NA | 类名：FilePreloadStatusInfo；  API声明：state: FilePreloadState;  差异内容：state: FilePreloadState; | api/@hms.pcService.openFileBoost.d.ts |
| 新增API | NA | 类名：openFileBoost；  API声明：function on(type: 'filePreloadStateChanged', callback: Callback<FilePreloadStatusInfo>): void;  差异内容：function on(type: 'filePreloadStateChanged', callback: Callback<FilePreloadStatusInfo>): void; | api/@hms.pcService.openFileBoost.d.ts |
| 新增API | NA | 类名：openFileBoost；  API声明：function off(type: 'filePreloadStateChanged', callback?: Callback<FilePreloadStatusInfo>): void;  差异内容：function off(type: 'filePreloadStateChanged', callback?: Callback<FilePreloadStatusInfo>): void; | api/@hms.pcService.openFileBoost.d.ts |
| 新增API | NA | 类名：openFileBoost；  API声明：function addFile(file: string): void;  差异内容：function addFile(file: string): void; | api/@hms.pcService.openFileBoost.d.ts |
| 新增API | NA | 类名：openFileBoost；  API声明：function removeFile(file: string): void;  差异内容：function removeFile(file: string): void; | api/@hms.pcService.openFileBoost.d.ts |
| 新增API | NA | 类名：openFileBoost；  API声明：function queryFilePreloadStatusInfo(file: string): FilePreloadStatusInfo;  差异内容：function queryFilePreloadStatusInfo(file: string): FilePreloadStatusInfo; | api/@hms.pcService.openFileBoost.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.pcService.openFileBoost.d.ts  差异内容：PreviewKit | api/@hms.pcService.openFileBoost.d.ts |
