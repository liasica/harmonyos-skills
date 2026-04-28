---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-performanceanalysiskit-5111
title: Performance Analysis Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > Performance Analysis Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:56+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:1e9a2b5bacb12c0b4fce9facd1fea60782fe1ebd2896ec1b310dc89725fb1b78
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：hidebug；  API声明：function dumpJsRawHeapData(needGC?: boolean): Promise<string>;  差异内容：401 | 类名：hidebug；  API声明：function dumpJsRawHeapData(needGC?: boolean): Promise<string>;  差异内容：NA | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hiTraceMeter；  API声明：function traceByValue(level: HiTraceOutputLevel, name: string, count: number): void;  差异内容：function traceByValue(level: HiTraceOutputLevel, name: string, count: number): void; | api/@ohos.hiTraceMeter.d.ts |
| 新增API | NA | 类名：hiTraceMeter；  API声明：enum HiTraceOutputLevel  差异内容：enum HiTraceOutputLevel | api/@ohos.hiTraceMeter.d.ts |
| 新增API | NA | 类名：HiTraceOutputLevel；  API声明：DEBUG = 0  差异内容：DEBUG = 0 | api/@ohos.hiTraceMeter.d.ts |
| 新增API | NA | 类名：HiTraceOutputLevel；  API声明：INFO = 1  差异内容：INFO = 1 | api/@ohos.hiTraceMeter.d.ts |
| 新增API | NA | 类名：HiTraceOutputLevel；  API声明：CRITICAL = 2  差异内容：CRITICAL = 2 | api/@ohos.hiTraceMeter.d.ts |
| 新增API | NA | 类名：HiTraceOutputLevel；  API声明：COMMERCIAL = 3  差异内容：COMMERCIAL = 3 | api/@ohos.hiTraceMeter.d.ts |
| 新增API | NA | 类名：HiTraceOutputLevel；  API声明：MAX = COMMERCIAL  差异内容：MAX = COMMERCIAL | api/@ohos.hiTraceMeter.d.ts |
| 新增API | NA | 类名：hiTraceMeter；  API声明：function startSyncTrace(level: HiTraceOutputLevel, name: string, customArgs?: string): void;  差异内容：function startSyncTrace(level: HiTraceOutputLevel, name: string, customArgs?: string): void; | api/@ohos.hiTraceMeter.d.ts |
| 新增API | NA | 类名：hiTraceMeter；  API声明：function finishSyncTrace(level: HiTraceOutputLevel): void;  差异内容：function finishSyncTrace(level: HiTraceOutputLevel): void; | api/@ohos.hiTraceMeter.d.ts |
| 新增API | NA | 类名：hiTraceMeter；  API声明：function startAsyncTrace(level: HiTraceOutputLevel, name: string, taskId: number, customCategory: string, customArgs?: string): void;  差异内容：function startAsyncTrace(level: HiTraceOutputLevel, name: string, taskId: number, customCategory: string, customArgs?: string): void; | api/@ohos.hiTraceMeter.d.ts |
| 新增API | NA | 类名：hiTraceMeter；  API声明：function finishAsyncTrace(level: HiTraceOutputLevel, name: string, taskId: number): void;  差异内容：function finishAsyncTrace(level: HiTraceOutputLevel, name: string, taskId: number): void; | api/@ohos.hiTraceMeter.d.ts |
| 新增API | NA | 类名：hiTraceMeter；  API声明：function isTraceEnabled(): boolean;  差异内容：function isTraceEnabled(): boolean; | api/@ohos.hiTraceMeter.d.ts |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：declare namespace hiTraceMeter  差异内容：NA | 类名：global；  API声明：declare namespace hiTraceMeter  差异内容：atomicservice | api/@ohos.hiTraceMeter.d.ts |
| API从不支持元服务到支持元服务 | 类名：hiTraceMeter；  API声明：function startTrace(name: string, taskId: number): void;  差异内容：NA | 类名：hiTraceMeter；  API声明：function startTrace(name: string, taskId: number): void;  差异内容：atomicservice | api/@ohos.hiTraceMeter.d.ts |
| API从不支持元服务到支持元服务 | 类名：hiTraceMeter；  API声明：function finishTrace(name: string, taskId: number): void;  差异内容：NA | 类名：hiTraceMeter；  API声明：function finishTrace(name: string, taskId: number): void;  差异内容：atomicservice | api/@ohos.hiTraceMeter.d.ts |
| API从不支持元服务到支持元服务 | 类名：hiTraceMeter；  API声明：function traceByValue(name: string, count: number): void;  差异内容：NA | 类名：hiTraceMeter；  API声明：function traceByValue(name: string, count: number): void;  差异内容：atomicservice | api/@ohos.hiTraceMeter.d.ts |
