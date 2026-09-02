---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-previewkit-7001
title: Preview Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Preview Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:06+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:cc19d01cd3548fccc37b2e837fac1d9304da178e0b69a3df64a635ea6b6d5d4a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：global；  API声明：declare namespace openFileBoost  差异内容：NA | 类名：global；  API声明：declare namespace openFileBoost  差异内容：26.0.0 | api/@hms.pcService.openFileBoost.d.ts |
| API废弃版本变更 | 类名：openFileBoost；  API声明：export enum FilePreloadState  差异内容：NA | 类名：openFileBoost；  API声明：export enum FilePreloadState  差异内容：26.0.0 | api/@hms.pcService.openFileBoost.d.ts |
| API废弃版本变更 | 类名：FilePreloadState；  API声明：NOT\_PRELOADED = 0  差异内容：NA | 类名：FilePreloadState；  API声明：NOT\_PRELOADED = 0  差异内容：26.0.0 | api/@hms.pcService.openFileBoost.d.ts |
| API废弃版本变更 | 类名：FilePreloadState；  API声明：PRELOADING = 1  差异内容：NA | 类名：FilePreloadState；  API声明：PRELOADING = 1  差异内容：26.0.0 | api/@hms.pcService.openFileBoost.d.ts |
| API废弃版本变更 | 类名：FilePreloadState；  API声明：PRELOADED = 2  差异内容：NA | 类名：FilePreloadState；  API声明：PRELOADED = 2  差异内容：26.0.0 | api/@hms.pcService.openFileBoost.d.ts |
| API废弃版本变更 | 类名：openFileBoost；  API声明：export interface FilePreloadStatusInfo  差异内容：NA | 类名：openFileBoost；  API声明：export interface FilePreloadStatusInfo  差异内容：26.0.0 | api/@hms.pcService.openFileBoost.d.ts |
| API废弃版本变更 | 类名：FilePreloadStatusInfo；  API声明：sandboxPath: string;  差异内容：NA | 类名：FilePreloadStatusInfo；  API声明：sandboxPath: string;  差异内容：26.0.0 | api/@hms.pcService.openFileBoost.d.ts |
| API废弃版本变更 | 类名：FilePreloadStatusInfo；  API声明：progress: number;  差异内容：NA | 类名：FilePreloadStatusInfo；  API声明：progress: number;  差异内容：26.0.0 | api/@hms.pcService.openFileBoost.d.ts |
| API废弃版本变更 | 类名：FilePreloadStatusInfo；  API声明：state: FilePreloadState;  差异内容：NA | 类名：FilePreloadStatusInfo；  API声明：state: FilePreloadState;  差异内容：26.0.0 | api/@hms.pcService.openFileBoost.d.ts |
| API废弃版本变更 | 类名：openFileBoost；  API声明：function on(type: 'filePreloadStateChanged', callback: Callback<FilePreloadStatusInfo>): void;  差异内容：NA | 类名：openFileBoost；  API声明：function on(type: 'filePreloadStateChanged', callback: Callback<FilePreloadStatusInfo>): void;  差异内容：26.0.0 | api/@hms.pcService.openFileBoost.d.ts |
| API废弃版本变更 | 类名：openFileBoost；  API声明：function off(type: 'filePreloadStateChanged', callback?: Callback<FilePreloadStatusInfo>): void;  差异内容：NA | 类名：openFileBoost；  API声明：function off(type: 'filePreloadStateChanged', callback?: Callback<FilePreloadStatusInfo>): void;  差异内容：26.0.0 | api/@hms.pcService.openFileBoost.d.ts |
| API废弃版本变更 | 类名：openFileBoost；  API声明：function addFile(file: string): void;  差异内容：NA | 类名：openFileBoost；  API声明：function addFile(file: string): void;  差异内容：26.0.0 | api/@hms.pcService.openFileBoost.d.ts |
| API废弃版本变更 | 类名：openFileBoost；  API声明：function removeFile(file: string): void;  差异内容：NA | 类名：openFileBoost；  API声明：function removeFile(file: string): void;  差异内容：26.0.0 | api/@hms.pcService.openFileBoost.d.ts |
| API废弃版本变更 | 类名：openFileBoost；  API声明：function queryFilePreloadStatusInfo(file: string): FilePreloadStatusInfo;  差异内容：NA | 类名：openFileBoost；  API声明：function queryFilePreloadStatusInfo(file: string): FilePreloadStatusInfo;  差异内容：26.0.0 | api/@hms.pcService.openFileBoost.d.ts |
