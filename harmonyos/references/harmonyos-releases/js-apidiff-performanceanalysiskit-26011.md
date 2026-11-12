---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-performanceanalysiskit-26011
title: Performance Analysis Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Performance Analysis Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:54+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:3c89d2cccec59bbf5d8753b2a98f477e8ab7deae6adf779c473f54274f2c2459
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：ThreadCpuUsage；  API声明：threadName?: string;  差异内容：threadName?: string; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function getAppRunningUniqueId(): string;  差异内容：function getAppRunningUniqueId(): string; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：class ExternalLogManager  差异内容：class ExternalLogManager | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：ExternalLogManager；  API声明：onCapacityReached(container: ExternalLogContainer): void;  差异内容：onCapacityReached(container: ExternalLogContainer): void; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：class ExternalLogContainer  差异内容：class ExternalLogContainer | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：ExternalLogContainer；  API声明：getAllLogs(): Set<ExternalLogWrapper>;  差异内容：getAllLogs(): Set<ExternalLogWrapper>; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：ExternalLogContainer；  API声明：getAllLogFiles(): Set<string>;  差异内容：getAllLogFiles(): Set<string>; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：ExternalLogContainer；  API声明：getLogFilesOfSysEvent(event: string): Set<string>;  差异内容：getLogFilesOfSysEvent(event: string): Set<string>; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：ExternalLogContainer；  API声明：getLogFilesGeneratedAfter(timePoint: number): Set<string>;  差异内容：getLogFilesGeneratedAfter(timePoint: number): Set<string>; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：ExternalLogContainer；  API声明：getLogFilesGeneratedBefore(timePoint: number): Set<string>;  差异内容：getLogFilesGeneratedBefore(timePoint: number): Set<string>; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：ExternalLogContainer；  API声明：getLogFilesLargerThan(sizeKb: number): Set<string>;  差异内容：getLogFilesLargerThan(sizeKb: number): Set<string>; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：ExternalLogContainer；  API声明：getLogFilesSmallerThan(sizeKb: number): Set<string>;  差异内容：getLogFilesSmallerThan(sizeKb: number): Set<string>; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：ExternalLogContainer；  API声明：getLogNumber(): number;  差异内容：getLogNumber(): number; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：ExternalLogContainer；  API声明：getFirstGeneratedLogFiles(num: number): Set<string>;  差异内容：getFirstGeneratedLogFiles(num: number): Set<string>; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：class ExternalLogWrapper  差异内容：class ExternalLogWrapper | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：ExternalLogWrapper；  API声明：getFilePath(): string;  差异内容：getFilePath(): string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：ExternalLogWrapper；  API声明：getGenerationTime(): number;  差异内容：getGenerationTime(): number; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：ExternalLogWrapper；  API声明：getSizeInKb(): number;  差异内容：getSizeInKb(): number; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：ExternalLogWrapper；  API声明：getSysEvent(): string;  差异内容：getSysEvent(): string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：function registerExternalLogManager(logMngr: ExternalLogManager): void;  差异内容：function registerExternalLogManager(logMngr: ExternalLogManager): void; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：function isExternalLogManagerRegistered(): boolean;  差异内容：function isExternalLogManagerRegistered(): boolean; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
