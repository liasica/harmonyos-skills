---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-performanceanalysiskit-6003
title: Performance Analysis Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Performance Analysis Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:21+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:45b7420c43cc6c9d648d1e40e59725ae37cdc3d6f5e5eb5649e9149fd8e514a6
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：hiAppEvent；  API声明：function setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void>;  差异内容：NA | 类名：hiAppEvent；  API声明：function setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void>;  差异内容：11100001,11101001,11101002,11101004,11101005 | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function getAppNativeMemInfoAsync(): Promise<NativeMemInfo>;  差异内容：function getAppNativeMemInfoAsync(): Promise<NativeMemInfo>; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function getAppNativeMemInfoWithCache(forceRefresh?: boolean): NativeMemInfo;  差异内容：function getAppNativeMemInfoWithCache(forceRefresh?: boolean): NativeMemInfo; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：enum JsRawHeapTrimLevel  差异内容：enum JsRawHeapTrimLevel | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：JsRawHeapTrimLevel；  API声明：TRIM\_LEVEL\_1 = 0  差异内容：TRIM\_LEVEL\_1 = 0 | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：JsRawHeapTrimLevel；  API声明：TRIM\_LEVEL\_2 = 1  差异内容：TRIM\_LEVEL\_2 = 1 | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function setJsRawHeapTrimLevel(level: JsRawHeapTrimLevel): void;  差异内容：function setJsRawHeapTrimLevel(level: JsRawHeapTrimLevel): void; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：jsLeakWatcher；  API声明：function enableLeakWatcher(isEnabled: boolean, configs: Array<string>, callback: Callback<Array<string>>): void;  差异内容：function enableLeakWatcher(isEnabled: boolean, configs: Array<string>, callback: Callback<Array<string>>): void; | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
