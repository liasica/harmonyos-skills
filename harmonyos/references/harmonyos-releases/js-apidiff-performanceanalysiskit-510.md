---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-performanceanalysiskit-510
title: Performance Analysis Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Performance Analysis Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:13+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:0f0a8214ed06fd04eda76557f7d36ebbc72bfcf223676ace0fc772b68784e1e2
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：global；  API声明：declare namespace FaultLogger  差异内容：NA | 类名：global；  API声明：declare namespace FaultLogger  差异内容：18 | api/@ohos.faultLogger.d.ts |
| API废弃版本变更 | 类名：FaultLogger；  API声明：enum FaultType  差异内容：NA | 类名：FaultLogger；  API声明：enum FaultType  差异内容：18 | api/@ohos.faultLogger.d.ts |
| API废弃版本变更 | 类名：FaultType；  API声明：NO\_SPECIFIC = 0  差异内容：NA | 类名：FaultType；  API声明：NO\_SPECIFIC = 0  差异内容：18 | api/@ohos.faultLogger.d.ts |
| API废弃版本变更 | 类名：FaultType；  API声明：CPP\_CRASH = 2  差异内容：NA | 类名：FaultType；  API声明：CPP\_CRASH = 2  差异内容：18 | api/@ohos.faultLogger.d.ts |
| API废弃版本变更 | 类名：FaultType；  API声明：JS\_CRASH = 3  差异内容：NA | 类名：FaultType；  API声明：JS\_CRASH = 3  差异内容：18 | api/@ohos.faultLogger.d.ts |
| API废弃版本变更 | 类名：FaultType；  API声明：APP\_FREEZE = 4  差异内容：NA | 类名：FaultType；  API声明：APP\_FREEZE = 4  差异内容：18 | api/@ohos.faultLogger.d.ts |
| API废弃版本变更 | 类名：FaultLogger；  API声明：function query(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>>): void;  差异内容：NA | 类名：FaultLogger；  API声明：function query(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>>): void;  差异内容：18 | api/@ohos.faultLogger.d.ts |
| API废弃版本变更 | 类名：FaultLogger；  API声明：function query(faultType: FaultType): Promise<Array<FaultLogInfo>>;  差异内容：NA | 类名：FaultLogger；  API声明：function query(faultType: FaultType): Promise<Array<FaultLogInfo>>;  差异内容：18 | api/@ohos.faultLogger.d.ts |
| API废弃版本变更 | 类名：FaultLogger；  API声明：interface FaultLogInfo  差异内容：NA | 类名：FaultLogger；  API声明：interface FaultLogInfo  差异内容：18 | api/@ohos.faultLogger.d.ts |
| API废弃版本变更 | 类名：FaultLogInfo；  API声明：pid: number;  差异内容：NA | 类名：FaultLogInfo；  API声明：pid: number;  差异内容：18 | api/@ohos.faultLogger.d.ts |
| API废弃版本变更 | 类名：FaultLogInfo；  API声明：uid: number;  差异内容：NA | 类名：FaultLogInfo；  API声明：uid: number;  差异内容：18 | api/@ohos.faultLogger.d.ts |
| API废弃版本变更 | 类名：FaultLogInfo；  API声明：type: FaultType;  差异内容：NA | 类名：FaultLogInfo；  API声明：type: FaultType;  差异内容：18 | api/@ohos.faultLogger.d.ts |
| API废弃版本变更 | 类名：FaultLogInfo；  API声明：timestamp: number;  差异内容：NA | 类名：FaultLogInfo；  API声明：timestamp: number;  差异内容：18 | api/@ohos.faultLogger.d.ts |
| API废弃版本变更 | 类名：FaultLogInfo；  API声明：reason: string;  差异内容：NA | 类名：FaultLogInfo；  API声明：reason: string;  差异内容：18 | api/@ohos.faultLogger.d.ts |
| API废弃版本变更 | 类名：FaultLogInfo；  API声明：module: string;  差异内容：NA | 类名：FaultLogInfo；  API声明：module: string;  差异内容：18 | api/@ohos.faultLogger.d.ts |
| API废弃版本变更 | 类名：FaultLogInfo；  API声明：summary: string;  差异内容：NA | 类名：FaultLogInfo；  API声明：summary: string;  差异内容：18 | api/@ohos.faultLogger.d.ts |
| API废弃版本变更 | 类名：FaultLogInfo；  API声明：fullLog: string;  差异内容：NA | 类名：FaultLogInfo；  API声明：fullLog: string;  差异内容：18 | api/@ohos.faultLogger.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function dumpJsRawHeapData(needGC?: boolean): Promise<string>;  差异内容：function dumpJsRawHeapData(needGC?: boolean): Promise<string>; | api/@ohos.hidebug.d.ts |
