---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-performanceanalysiskit-7001
title: Performance Analysis Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Performance Analysis Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:06+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:f3d119a5410070b174407a6ebdf47191fa1c67a29127ce4076b6fa8715fc4a67
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace hiRetrieval  差异内容：declare namespace hiRetrieval | api/@ohos.hiviewdfx.hiRetrieval.d.ts |
| 新增API | NA | 类名：hiRetrieval；  API声明：interface HiRetrievalConfig  差异内容：interface HiRetrievalConfig | api/@ohos.hiviewdfx.hiRetrieval.d.ts |
| 新增API | NA | 类名：HiRetrievalConfig；  API声明：userType: string;  差异内容：userType: string; | api/@ohos.hiviewdfx.hiRetrieval.d.ts |
| 新增API | NA | 类名：HiRetrievalConfig；  API声明：deviceType: string;  差异内容：deviceType: string; | api/@ohos.hiviewdfx.hiRetrieval.d.ts |
| 新增API | NA | 类名：HiRetrievalConfig；  API声明：deviceModel: string;  差异内容：deviceModel: string; | api/@ohos.hiviewdfx.hiRetrieval.d.ts |
| 新增API | NA | 类名：hiRetrieval；  API声明：function init(): void;  差异内容：function init(): void; | api/@ohos.hiviewdfx.hiRetrieval.d.ts |
| 新增API | NA | 类名：hiRetrieval；  API声明：function participate(config: HiRetrievalConfig): void;  差异内容：function participate(config: HiRetrievalConfig): void; | api/@ohos.hiviewdfx.hiRetrieval.d.ts |
| 新增API | NA | 类名：hiRetrieval；  API声明：function quit(): void;  差异内容：function quit(): void; | api/@ohos.hiviewdfx.hiRetrieval.d.ts |
| 新增API | NA | 类名：hiRetrieval；  API声明：function isParticipant(): boolean;  差异内容：function isParticipant(): boolean; | api/@ohos.hiviewdfx.hiRetrieval.d.ts |
| 新增API | NA | 类名：hiRetrieval；  API声明：function getLastParticipationTimestamp(): number;  差异内容：function getLastParticipationTimestamp(): number; | api/@ohos.hiviewdfx.hiRetrieval.d.ts |
| 新增API | NA | 类名：hiRetrieval；  API声明：function run(): void;  差异内容：function run(): void; | api/@ohos.hiviewdfx.hiRetrieval.d.ts |
| 新增API | NA | 类名：hiRetrieval；  API声明：function getCurrentConfig(): HiRetrievalConfig;  差异内容：function getCurrentConfig(): HiRetrievalConfig; | api/@ohos.hiviewdfx.hiRetrieval.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function dumpJsRawHeapData(needGC: boolean, needClean: boolean, processDump: boolean): Promise<Array<string>>;  差异内容：function dumpJsRawHeapData(needGC: boolean, needClean: boolean, processDump: boolean): Promise<Array<string>>; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hichecker；  API声明：const RULE\_THREAD\_CHECK\_NETWORK\_USAGE = 2n;  差异内容：const RULE\_THREAD\_CHECK\_NETWORK\_USAGE = 2n; | api/@ohos.hichecker.d.ts |
| 新增API | NA | 类名：event；  API声明：const appFreezeWarning: string;  差异内容：const appFreezeWarning: string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：AppCrashPolicy；  API声明：extendPcLrPrinting?: boolean;  差异内容：extendPcLrPrinting?: boolean; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：AppCrashPolicy；  API声明：logFileCutoffSzBytes?: number;  差异内容：logFileCutoffSzBytes?: number; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：AppCrashPolicy；  API声明：simplifyVmaPrinting?: boolean;  差异内容：simplifyVmaPrinting?: boolean; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：ResourceOverlimitPolicy；  API声明：jsHeapLogtype?: string;  差异内容：jsHeapLogtype?: string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.hiviewdfx.hiRetrieval.d.ts  差异内容：PerformanceAnalysisKit | api/@ohos.hiviewdfx.hiRetrieval.d.ts |
