---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-performanceanalysiskit-6021
title: Performance Analysis Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:48+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:056473719c1526220365c9315ca036e5c6fc688176b4e07959b19326d4143ad4
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：hiTraceMeter；  API声明：type TraceEventListener = (traceStatus: boolean) => void;  差异内容：type TraceEventListener = (traceStatus: boolean) => void; | api/@ohos.hiTraceMeter.d.ts |
| 新增API | NA | 类名：hiTraceMeter；  API声明：function registerTraceListener(callback: TraceEventListener): number;  差异内容：function registerTraceListener(callback: TraceEventListener): number; | api/@ohos.hiTraceMeter.d.ts |
| 新增API | NA | 类名：hiTraceMeter；  API声明：function unregisterTraceListener(index: number): number;  差异内容：function unregisterTraceListener(index: number): number; | api/@ohos.hiTraceMeter.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：interface MainThreadJankPolicy  差异内容：interface MainThreadJankPolicy | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：MainThreadJankPolicy；  API声明：logType?: number;  差异内容：logType?: number; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：MainThreadJankPolicy；  API声明：ignoreStartupTime?: number;  差异内容：ignoreStartupTime?: number; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：MainThreadJankPolicy；  API声明：sampleInterval?: number;  差异内容：sampleInterval?: number; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：MainThreadJankPolicy；  API声明：sampleCount?: number;  差异内容：sampleCount?: number; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：MainThreadJankPolicy；  API声明：reportTimesPerApp?: number;  差异内容：reportTimesPerApp?: number; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：MainThreadJankPolicy；  API声明：autoStopSampling?: boolean;  差异内容：autoStopSampling?: boolean; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：interface CpuUsageHighPolicy  差异内容：interface CpuUsageHighPolicy | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：CpuUsageHighPolicy；  API声明：foregroundLoadThreshold?: number;  差异内容：foregroundLoadThreshold?: number; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：CpuUsageHighPolicy；  API声明：backgroundLoadThreshold?: number;  差异内容：backgroundLoadThreshold?: number; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：CpuUsageHighPolicy；  API声明：threadLoadThreshold?: number;  差异内容：threadLoadThreshold?: number; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：CpuUsageHighPolicy；  API声明：perfLogCaptureCount?: number;  差异内容：perfLogCaptureCount?: number; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：CpuUsageHighPolicy；  API声明：threadLoadInterval?: number;  差异内容：threadLoadInterval?: number; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：interface EventPolicy  差异内容：interface EventPolicy | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：EventPolicy；  API声明：mainThreadJankPolicy?: MainThreadJankPolicy;  差异内容：mainThreadJankPolicy?: MainThreadJankPolicy; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：EventPolicy；  API声明：cpuUsageHighPolicy?: CpuUsageHighPolicy;  差异内容：cpuUsageHighPolicy?: CpuUsageHighPolicy; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：function configEventPolicy(policy: EventPolicy): Promise<void>;  差异内容：function configEventPolicy(policy: EventPolicy): Promise<void>; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
