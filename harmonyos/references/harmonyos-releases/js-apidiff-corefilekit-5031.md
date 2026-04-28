---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corefilekit-5031
title: Core File Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta1引入的API > Core File Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:41+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:b132c74001cc4e878c0861ea2d593ad466401ece113c273558a763d3b5dba502
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace keyManager  差异内容： declare namespace keyManager | api/@ohos.file.keyManager.d.ts |
| 新增API | NA | 类名：global；  API声明： export class AtomicFile  差异内容： export class AtomicFile | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：AtomicFile；  API声明：getBaseFile(): File;  差异内容：getBaseFile(): File; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：AtomicFile；  API声明：openRead(): ReadStream;  差异内容：openRead(): ReadStream; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：AtomicFile；  API声明：readFully(): ArrayBuffer;  差异内容：readFully(): ArrayBuffer; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：AtomicFile；  API声明：startWrite(): WriteStream;  差异内容：startWrite(): WriteStream; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：AtomicFile；  API声明：finishWrite(): void;  差异内容：finishWrite(): void; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：AtomicFile；  API声明：failWrite(): void;  差异内容：failWrite(): void; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：AtomicFile；  API声明：delete(): void;  差异内容：delete(): void; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：Stat；  API声明：readonly atimeNs?: bigint;  差异内容：readonly atimeNs?: bigint; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：Stat；  API声明：readonly mtimeNs?: bigint;  差异内容：readonly mtimeNs?: bigint; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：Stat；  API声明：readonly ctimeNs?: bigint;  差异内容：readonly ctimeNs?: bigint; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：storageStatistics；  API声明：function getTotalSize(callback: AsyncCallback<number>): void;  差异内容：function getTotalSize(callback: AsyncCallback<number>): void; | api/@ohos.file.storageStatistics.d.ts |
| 新增API | NA | 类名：storageStatistics；  API声明：function getTotalSize(): Promise<number>;  差异内容：function getTotalSize(): Promise<number>; | api/@ohos.file.storageStatistics.d.ts |
| 新增API | NA | 类名：storageStatistics；  API声明：function getTotalSizeSync(): number;  差异内容：function getTotalSizeSync(): number; | api/@ohos.file.storageStatistics.d.ts |
| 新增API | NA | 类名：storageStatistics；  API声明：function getFreeSize(callback: AsyncCallback<number>): void;  差异内容：function getFreeSize(callback: AsyncCallback<number>): void; | api/@ohos.file.storageStatistics.d.ts |
| 新增API | NA | 类名：storageStatistics；  API声明：function getFreeSize(): Promise<number>;  差异内容：function getFreeSize(): Promise<number>; | api/@ohos.file.storageStatistics.d.ts |
| 新增API | NA | 类名：storageStatistics；  API声明：function getFreeSizeSync(): number;  差异内容：function getFreeSizeSync(): number; | api/@ohos.file.storageStatistics.d.ts |
