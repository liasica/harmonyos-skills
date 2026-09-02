---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-performanceanalysiskit-6111
title: Performance Analysis Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > Performance Analysis Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:08+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:3c8a655594494d0a2023abc51e0eb4e939c25c60b18b01db4dd142dcb5dd2f23
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：jsLeakWatcher；  API声明：function dump(filePath: string): Array<string>;  差异内容：401 | 类名：jsLeakWatcher；  API声明：function dump(filePath: string): Array<string>;  差异内容：NA | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function dumpJsHeapData(filename: string, needClean: boolean): void;  差异内容：function dumpJsHeapData(filename: string, needClean: boolean): void; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function dumpJsRawHeapData(needGC: boolean, needClean: boolean): Promise<string>;  差异内容：function dumpJsRawHeapData(needGC: boolean, needClean: boolean): Promise<string>; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：interface RequestTraceConfig  差异内容：interface RequestTraceConfig | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：RequestTraceConfig；  API声明：identifier: string;  差异内容：identifier: string; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：RequestTraceConfig；  API声明：bufferSizeKb: number;  差异内容：bufferSizeKb: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：RequestTraceConfig；  API声明：durationMs: number;  差异内容：durationMs: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：RequestTraceConfig；  API声明：reserved: number;  差异内容：reserved: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function requestTrace(config: RequestTraceConfig): Promise<string>;  差异内容：function requestTrace(config: RequestTraceConfig): Promise<string>; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function setProcDumpInSharedOOM(enable: boolean): void;  差异内容：function setProcDumpInSharedOOM(enable: boolean): void; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：interface RssInfo  差异内容：interface RssInfo | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：RssInfo；  API声明：rss: bigint;  差异内容：rss: bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：RssInfo；  API声明：swapRss: bigint;  差异内容：swapRss: bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function getRssInfo(): RssInfo;  差异内容：function getRssInfo(): RssInfo; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：jsLeakWatcher；  API声明：export declare enum MonitorObjectType  差异内容：export declare enum MonitorObjectType | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：MonitorObjectType；  API声明：ALL = -1  差异内容：ALL = -1 | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：MonitorObjectType；  API声明：CUSTOM\_COMPONENT = 1 << 0  差异内容：CUSTOM\_COMPONENT = 1 << 0 | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：MonitorObjectType；  API声明：WINDOW = 1 << 1  差异内容：WINDOW = 1 << 1 | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：MonitorObjectType；  API声明：NODE\_CONTAINER = 1 << 2  差异内容：NODE\_CONTAINER = 1 << 2 | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：MonitorObjectType；  API声明：X\_COMPONENT = 1 << 3  差异内容：X\_COMPONENT = 1 << 3 | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：MonitorObjectType；  API声明：ABILITY = 1 << 4  差异内容：ABILITY = 1 << 4 | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：jsLeakWatcher；  API声明：interface LeakWatcherConfig  差异内容：interface LeakWatcherConfig | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：LeakWatcherConfig；  API声明：monitorObjectTypes: MonitorObjectType;  差异内容：monitorObjectTypes: MonitorObjectType; | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：LeakWatcherConfig；  API声明：objectUniqueIDs?: Array<number>;  差异内容：objectUniqueIDs?: Array<number>; | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：LeakWatcherConfig；  API声明：checkInterval?: number;  差异内容：checkInterval?: number; | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：LeakWatcherConfig；  API声明：fgLeakCountThreshold?: number;  差异内容：fgLeakCountThreshold?: number; | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：LeakWatcherConfig；  API声明：bgLeakCountThreshold?: number;  差异内容：bgLeakCountThreshold?: number; | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：LeakWatcherConfig；  API声明：maxStoredHeapDumps?: number;  差异内容：maxStoredHeapDumps?: number; | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：LeakWatcherConfig；  API声明：dumpHeapWaitTimeMs?: number;  差异内容：dumpHeapWaitTimeMs?: number; | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：LeakWatcherConfig；  API声明：exclusionList?: Array<string>;  差异内容：exclusionList?: Array<string>; | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：interface AppCrashPolicy  差异内容：interface AppCrashPolicy | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：AppCrashPolicy；  API声明：pageSwitchLogEnable?: boolean;  差异内容：pageSwitchLogEnable?: boolean; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：interface AppFreezePolicy  差异内容：interface AppFreezePolicy | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：AppFreezePolicy；  API声明：pageSwitchLogEnable?: boolean;  差异内容：pageSwitchLogEnable?: boolean; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：interface ResourceOverlimitPolicy  差异内容：interface ResourceOverlimitPolicy | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：ResourceOverlimitPolicy；  API声明：pageSwitchLogEnable?: boolean;  差异内容：pageSwitchLogEnable?: boolean; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：interface AddressSanitizerPolicy  差异内容：interface AddressSanitizerPolicy | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：AddressSanitizerPolicy；  API声明：pageSwitchLogEnable?: boolean;  差异内容：pageSwitchLogEnable?: boolean; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：EventPolicy；  API声明：appCrashPolicy?: AppCrashPolicy;  差异内容：appCrashPolicy?: AppCrashPolicy; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：EventPolicy；  API声明：appFreezePolicy?: AppFreezePolicy;  差异内容：appFreezePolicy?: AppFreezePolicy; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：EventPolicy；  API声明：resourceOverlimitPolicy?: ResourceOverlimitPolicy;  差异内容：resourceOverlimitPolicy?: ResourceOverlimitPolicy; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：EventPolicy；  API声明：addressSanitizerPolicy?: AddressSanitizerPolicy;  差异内容：addressSanitizerPolicy?: AddressSanitizerPolicy; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
