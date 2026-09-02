---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-performanceanalysiskit-7002
title: Performance Analysis Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Performance Analysis Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:3d56475cf0aa21e7de59ebfbdbed9ee3627bad1c8f259e3a91eb1c458fc473c5
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：hilog；  API声明：function setOutputType(type: OutputType): OutputType;  差异内容：function setOutputType(type: OutputType): OutputType; | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：hilog；  API声明：function setOutputTypeByDomainID(type: OutputType, domainIDs: Array<number>, isExclude: boolean): OutputType;  差异内容：function setOutputTypeByDomainID(type: OutputType, domainIDs: Array<number>, isExclude: boolean): OutputType; | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：hilog；  API声明：function getOutputType(): OutputType;  差异内容：function getOutputType(): OutputType; | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：hilog；  API声明：function getOutputDir(): string;  差异内容：function getOutputDir(): string; | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：hilog；  API声明：function clean(): void;  差异内容：function clean(): void; | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：hilog；  API声明：function flush(): void;  差异内容：function flush(): void; | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：hilog；  API声明：function getLogFile(latestSeconds: number): Array<string>;  差异内容：function getLogFile(latestSeconds: number): Array<string>; | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：hilog；  API声明：enum OutputType  差异内容：enum OutputType | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：OutputType；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：OutputType；  API声明：CONSOLE\_ONLY = 0  差异内容：CONSOLE\_ONLY = 0 | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：OutputType；  API声明：PRIVATE\_SANDBOX\_ONLY = 1  差异内容：PRIVATE\_SANDBOX\_ONLY = 1 | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：OutputType；  API声明：SHARE\_SANDBOX\_ONLY = 2  差异内容：SHARE\_SANDBOX\_ONLY = 2 | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：OutputType；  API声明：PRIVATE\_SANDBOX\_WITH\_CONSOLE = 3  差异内容：PRIVATE\_SANDBOX\_WITH\_CONSOLE = 3 | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：OutputType；  API声明：SHARE\_SANDBOX\_WITH\_CONSOLE = 4  差异内容：SHARE\_SANDBOX\_WITH\_CONSOLE = 4 | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：AppCrashPolicy；  API声明：collectMinidump?: boolean;  差异内容：collectMinidump?: boolean; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：ResourceOverlimitPolicy；  API声明：useRefinedLogFileName?: boolean;  差异内容：useRefinedLogFileName?: boolean; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
