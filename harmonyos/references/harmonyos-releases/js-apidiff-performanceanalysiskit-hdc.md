---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-performanceanalysiskit-hdc
title: Performance Analysis Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta1引入的API > Performance Analysis Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:37:11+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:137a4cabf0f40fd6d3c07d8fb33e6ea53acbe5224c27d4bb66fcac457cb9508b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：hiAppEvent；  API声明： enum EventType  差异内容：NA | 类名：hiAppEvent；  API声明： enum EventType  差异内容：9 | api/@ohos.hiAppEvent.d.ts |
| API废弃版本变更 | 类名：EventType；  API声明：FAULT = 1  差异内容：NA | 类名：EventType；  API声明：FAULT = 1  差异内容：9 | api/@ohos.hiAppEvent.d.ts |
| API废弃版本变更 | 类名：EventType；  API声明：STATISTIC = 2  差异内容：NA | 类名：EventType；  API声明：STATISTIC = 2  差异内容：9 | api/@ohos.hiAppEvent.d.ts |
| API废弃版本变更 | 类名：EventType；  API声明：SECURITY = 3  差异内容：NA | 类名：EventType；  API声明：SECURITY = 3  差异内容：9 | api/@ohos.hiAppEvent.d.ts |
| API废弃版本变更 | 类名：EventType；  API声明：BEHAVIOR = 4  差异内容：NA | 类名：EventType；  API声明：BEHAVIOR = 4  差异内容：9 | api/@ohos.hiAppEvent.d.ts |
| API废弃版本变更 | 类名：hiAppEvent；  API声明： namespace Event  差异内容：NA | 类名：hiAppEvent；  API声明： namespace Event  差异内容：9 | api/@ohos.hiAppEvent.d.ts |
| API废弃版本变更 | 类名：Event；  API声明：const USER\_LOGIN: string;  差异内容：NA | 类名：Event；  API声明：const USER\_LOGIN: string;  差异内容：9 | api/@ohos.hiAppEvent.d.ts |
| API废弃版本变更 | 类名：Event；  API声明：const USER\_LOGOUT: string;  差异内容：NA | 类名：Event；  API声明：const USER\_LOGOUT: string;  差异内容：9 | api/@ohos.hiAppEvent.d.ts |
| API废弃版本变更 | 类名：Event；  API声明：const DISTRIBUTED\_SERVICE\_START: string;  差异内容：NA | 类名：Event；  API声明：const DISTRIBUTED\_SERVICE\_START: string;  差异内容：9 | api/@ohos.hiAppEvent.d.ts |
| API废弃版本变更 | 类名：hiAppEvent；  API声明： namespace Param  差异内容：NA | 类名：hiAppEvent；  API声明： namespace Param  差异内容：9 | api/@ohos.hiAppEvent.d.ts |
| API废弃版本变更 | 类名：Param；  API声明：const USER\_ID: string;  差异内容：NA | 类名：Param；  API声明：const USER\_ID: string;  差异内容：9 | api/@ohos.hiAppEvent.d.ts |
| API废弃版本变更 | 类名：Param；  API声明：const DISTRIBUTED\_SERVICE\_NAME: string;  差异内容：NA | 类名：Param；  API声明：const DISTRIBUTED\_SERVICE\_NAME: string;  差异内容：9 | api/@ohos.hiAppEvent.d.ts |
| API废弃版本变更 | 类名：Param；  API声明：const DISTRIBUTED\_SERVICE\_INSTANCE\_ID: string;  差异内容：NA | 类名：Param；  API声明：const DISTRIBUTED\_SERVICE\_INSTANCE\_ID: string;  差异内容：9 | api/@ohos.hiAppEvent.d.ts |
| API废弃版本变更 | 类名：hiAppEvent；  API声明：function write(eventName: string, eventType: EventType, keyValues: object): Promise<void>;  差异内容：NA | 类名：hiAppEvent；  API声明：function write(eventName: string, eventType: EventType, keyValues: object): Promise<void>;  差异内容：9 | api/@ohos.hiAppEvent.d.ts |
| API废弃版本变更 | 类名：hiAppEvent；  API声明：function write(eventName: string, eventType: EventType, keyValues: object, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：hiAppEvent；  API声明：function write(eventName: string, eventType: EventType, keyValues: object, callback: AsyncCallback<void>): void;  差异内容：9 | api/@ohos.hiAppEvent.d.ts |
| API废弃版本变更 | 类名：hiAppEvent；  API声明：function configure(config: ConfigOption): boolean;  差异内容：NA | 类名：hiAppEvent；  API声明：function configure(config: ConfigOption): boolean;  差异内容：9 | api/@ohos.hiAppEvent.d.ts |
| API废弃版本变更 | 类名：hiAppEvent；  API声明： interface ConfigOption  差异内容：NA | 类名：hiAppEvent；  API声明： interface ConfigOption  差异内容：9 | api/@ohos.hiAppEvent.d.ts |
| API废弃版本变更 | 类名：ConfigOption；  API声明：disable?: boolean;  差异内容：NA | 类名：ConfigOption；  API声明：disable?: boolean;  差异内容：9 | api/@ohos.hiAppEvent.d.ts |
| API废弃版本变更 | 类名：ConfigOption；  API声明：maxStorage?: string;  差异内容：NA | 类名：ConfigOption；  API声明：maxStorage?: string;  差异内容：9 | api/@ohos.hiAppEvent.d.ts |
| 错误码变更 | 类名：hiAppEvent；  API声明：function write(info: AppEventInfo, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：hiAppEvent；  API声明：function write(info: AppEventInfo, callback: AsyncCallback<void>): void;  差异内容：11100001,11101001,11101002,11101003,11101004,11101005,11101006,401 | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hichecker；  API声明：const RULE\_CHECK\_ARKUI\_PERFORMANCE: 17179869184n;  差异内容：const RULE\_CHECK\_ARKUI\_PERFORMANCE: 17179869184n; | api/@ohos.hichecker.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function getVss(): bigint;  差异内容：function getVss(): bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function getSystemCpuUsage(): number;  差异内容：function getSystemCpuUsage(): number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明： interface ThreadCpuUsage  差异内容： interface ThreadCpuUsage | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：ThreadCpuUsage；  API声明：threadId: number;  差异内容：threadId: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：ThreadCpuUsage；  API声明：cpuUsage: number;  差异内容：cpuUsage: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function getAppThreadCpuUsage(): ThreadCpuUsage[];  差异内容：function getAppThreadCpuUsage(): ThreadCpuUsage[]; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明： interface SystemMemInfo  差异内容： interface SystemMemInfo | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：SystemMemInfo；  API声明：totalMem: bigint;  差异内容：totalMem: bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：SystemMemInfo；  API声明：freeMem: bigint;  差异内容：freeMem: bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：SystemMemInfo；  API声明：availableMem: bigint;  差异内容：availableMem: bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function getSystemMemInfo(): SystemMemInfo;  差异内容：function getSystemMemInfo(): SystemMemInfo; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明： interface NativeMemInfo  差异内容： interface NativeMemInfo | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：NativeMemInfo；  API声明：pss: bigint;  差异内容：pss: bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：NativeMemInfo；  API声明：vss: bigint;  差异内容：vss: bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：NativeMemInfo；  API声明：rss: bigint;  差异内容：rss: bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：NativeMemInfo；  API声明：sharedDirty: bigint;  差异内容：sharedDirty: bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：NativeMemInfo；  API声明：privateDirty: bigint;  差异内容：privateDirty: bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：NativeMemInfo；  API声明：sharedClean: bigint;  差异内容：sharedClean: bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：NativeMemInfo；  API声明：privateClean: bigint;  差异内容：privateClean: bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function getAppNativeMemInfo(): NativeMemInfo;  差异内容：function getAppNativeMemInfo(): NativeMemInfo; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明： interface MemoryLimit  差异内容： interface MemoryLimit | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：MemoryLimit；  API声明：rssLimit: bigint;  差异内容：rssLimit: bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：MemoryLimit；  API声明：vssLimit: bigint;  差异内容：vssLimit: bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：MemoryLimit；  API声明：vmHeapLimit: bigint;  差异内容：vmHeapLimit: bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function getAppMemoryLimit(): MemoryLimit;  差异内容：function getAppMemoryLimit(): MemoryLimit; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明： interface VMMemoryInfo  差异内容： interface VMMemoryInfo | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：VMMemoryInfo；  API声明：totalHeap: bigint;  差异内容：totalHeap: bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：VMMemoryInfo；  API声明：heapUsed: bigint;  差异内容：heapUsed: bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：VMMemoryInfo；  API声明：allArraySize: bigint;  差异内容：allArraySize: bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function getAppVMMemoryInfo(): VMMemoryInfo;  差异内容：function getAppVMMemoryInfo(): VMMemoryInfo; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明： enum TraceFlag  差异内容： enum TraceFlag | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：TraceFlag；  API声明：MAIN\_THREAD = 1  差异内容：MAIN\_THREAD = 1 | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：TraceFlag；  API声明：ALL\_THREADS = 2  差异内容：ALL\_THREADS = 2 | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明： namespace tags  差异内容： namespace tags | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const ABILITY\_MANAGER: number;  差异内容：const ABILITY\_MANAGER: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const ARKUI: number;  差异内容：const ARKUI: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const ARK: number;  差异内容：const ARK: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const BLUETOOTH: number;  差异内容：const BLUETOOTH: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const COMMON\_LIBRARY: number;  差异内容：const COMMON\_LIBRARY: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const DISTRIBUTED\_HARDWARE\_DEVICE\_MANAGER: number;  差异内容：const DISTRIBUTED\_HARDWARE\_DEVICE\_MANAGER: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const DISTRIBUTED\_AUDIO: number;  差异内容：const DISTRIBUTED\_AUDIO: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const DISTRIBUTED\_CAMERA: number;  差异内容：const DISTRIBUTED\_CAMERA: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const DISTRIBUTED\_DATA: number;  差异内容：const DISTRIBUTED\_DATA: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const DISTRIBUTED\_HARDWARE\_FRAMEWORK: number;  差异内容：const DISTRIBUTED\_HARDWARE\_FRAMEWORK: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const DISTRIBUTED\_INPUT: number;  差异内容：const DISTRIBUTED\_INPUT: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const DISTRIBUTED\_SCREEN: number;  差异内容：const DISTRIBUTED\_SCREEN: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const DISTRIBUTED\_SCHEDULER: number;  差异内容：const DISTRIBUTED\_SCHEDULER: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const FFRT: number;  差异内容：const FFRT: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const FILE\_MANAGEMENT: number;  差异内容：const FILE\_MANAGEMENT: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const GLOBAL\_RESOURCE\_MANAGER: number;  差异内容：const GLOBAL\_RESOURCE\_MANAGER: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const GRAPHICS: number;  差异内容：const GRAPHICS: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const HDF: number;  差异内容：const HDF: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const MISC: number;  差异内容：const MISC: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const MULTIMODAL\_INPUT: number;  差异内容：const MULTIMODAL\_INPUT: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const NET: number;  差异内容：const NET: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const NOTIFICATION: number;  差异内容：const NOTIFICATION: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const NWEB: number;  差异内容：const NWEB: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const OHOS: number;  差异内容：const OHOS: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const POWER\_MANAGER: number;  差异内容：const POWER\_MANAGER: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const RPC: number;  差异内容：const RPC: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const SAMGR: number;  差异内容：const SAMGR: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const WINDOW\_MANAGER: number;  差异内容：const WINDOW\_MANAGER: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const AUDIO: number;  差异内容：const AUDIO: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const CAMERA: number;  差异内容：const CAMERA: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const IMAGE: number;  差异内容：const IMAGE: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：tags；  API声明：const MEDIA: number;  差异内容：const MEDIA: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function startAppTraceCapture(tags: number[], flag: TraceFlag, limitSize: number): string;  差异内容：function startAppTraceCapture(tags: number[], flag: TraceFlag, limitSize: number): string; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function stopAppTraceCapture(): void;  差异内容：function stopAppTraceCapture(): void; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function setAppResourceLimit(type: string, value: number, enableDebugLog: boolean): void;  差异内容：function setAppResourceLimit(type: string, value: number, enableDebugLog: boolean): void; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明： namespace domain  差异内容： namespace domain | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：domain；  API声明：const OS: string;  差异内容：const OS: string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：event；  API声明：const APP\_CRASH: string;  差异内容：const APP\_CRASH: string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：event；  API声明：const APP\_FREEZE: string;  差异内容：const APP\_FREEZE: string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：event；  API声明：const APP\_LAUNCH: string;  差异内容：const APP\_LAUNCH: string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：event；  API声明：const SCROLL\_JANK: string;  差异内容：const SCROLL\_JANK: string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：event；  API声明：const CPU\_USAGE\_HIGH: string;  差异内容：const CPU\_USAGE\_HIGH: string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：event；  API声明：const BATTERY\_USAGE: string;  差异内容：const BATTERY\_USAGE: string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：event；  API声明：const RESOURCE\_OVERLIMIT: string;  差异内容：const RESOURCE\_OVERLIMIT: string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：event；  API声明：const ADDRESS\_SANITIZER: string;  差异内容：const ADDRESS\_SANITIZER: string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：event；  API声明：const MAIN\_THREAD\_JANK: string;  差异内容：const MAIN\_THREAD\_JANK: string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：type ParamType = number | string | boolean | Array<string>;  差异内容：type ParamType = number | string | boolean | Array<string>; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：function setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void>;  差异内容：function setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void>; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：AppEventPackage；  API声明：appEventInfos: Array<AppEventInfo>;  差异内容：appEventInfos: Array<AppEventInfo>; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：AppEventPackageHolder；  API声明：setRow(size: number): void;  差异内容：setRow(size: number): void; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：AppEventFilter；  API声明：names?: string[];  差异内容：names?: string[]; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明： interface AppEventGroup  差异内容： interface AppEventGroup | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：AppEventGroup；  API声明：name: string;  差异内容：name: string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：AppEventGroup；  API声明：appEventInfos: Array<AppEventInfo>;  差异内容：appEventInfos: Array<AppEventInfo>; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：Watcher；  API声明：onReceive?: (domain: string, appEventGroups: Array<AppEventGroup>) => void;  差异内容：onReceive?: (domain: string, appEventGroups: Array<AppEventGroup>) => void; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：function setUserId(name: string, value: string): void;  差异内容：function setUserId(name: string, value: string): void; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：function getUserId(name: string): string;  差异内容：function getUserId(name: string): string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：function setUserProperty(name: string, value: string): void;  差异内容：function setUserProperty(name: string, value: string): void; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：function getUserProperty(name: string): string;  差异内容：function getUserProperty(name: string): string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明： interface AppEventReportConfig  差异内容： interface AppEventReportConfig | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：AppEventReportConfig；  API声明：domain?: string;  差异内容：domain?: string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：AppEventReportConfig；  API声明：name?: string;  差异内容：name?: string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：AppEventReportConfig；  API声明：isRealTime?: boolean;  差异内容：isRealTime?: boolean; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明： interface Processor  差异内容： interface Processor | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：Processor；  API声明：name: string;  差异内容：name: string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：Processor；  API声明：debugMode?: boolean;  差异内容：debugMode?: boolean; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：Processor；  API声明：routeInfo?: string;  差异内容：routeInfo?: string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：Processor；  API声明：appId?: string;  差异内容：appId?: string; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：Processor；  API声明：onStartReport?: boolean;  差异内容：onStartReport?: boolean; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：Processor；  API声明：onBackgroundReport?: boolean;  差异内容：onBackgroundReport?: boolean; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：Processor；  API声明：periodReport?: number;  差异内容：periodReport?: number; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：Processor；  API声明：batchReport?: number;  差异内容：batchReport?: number; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：Processor；  API声明：userIds?: string[];  差异内容：userIds?: string[]; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：Processor；  API声明：userProperties?: string[];  差异内容：userProperties?: string[]; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：Processor；  API声明：eventConfigs?: AppEventReportConfig[];  差异内容：eventConfigs?: AppEventReportConfig[]; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：Processor；  API声明：configId?: number;  差异内容：configId?: number; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：Processor；  API声明：customConfigs?: Record<string, string>;  差异内容：customConfigs?: Record<string, string>; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：function addProcessor(processor: Processor): number;  差异内容：function addProcessor(processor: Processor): number; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hiAppEvent；  API声明：function removeProcessor(id: number): void;  差异内容：function removeProcessor(id: number): void; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
