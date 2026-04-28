---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-performanceanalysiskit-6011
title: Performance Analysis Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Beta1引入的API > Performance Analysis Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:01+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:873bdc9ee79e48f800cab464f331f6bde27a5a479de750d595c9ff09ca075de8
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare class FaultLogExtensionAbility  差异内容：declare class FaultLogExtensionAbility | api/@ohos.hiviewdfx.FaultLogExtensionAbility.d.ts |
| 新增API | NA | 类名：FaultLogExtensionAbility；  API声明：context: FaultLogExtensionContext;  差异内容：context: FaultLogExtensionContext; | api/@ohos.hiviewdfx.FaultLogExtensionAbility.d.ts |
| 新增API | NA | 类名：FaultLogExtensionAbility；  API声明：onFaultReportReady(): void;  差异内容：onFaultReportReady(): void; | api/@ohos.hiviewdfx.FaultLogExtensionAbility.d.ts |
| 新增API | NA | 类名：FaultLogExtensionAbility；  API声明：onConnect(): void;  差异内容：onConnect(): void; | api/@ohos.hiviewdfx.FaultLogExtensionAbility.d.ts |
| 新增API | NA | 类名：FaultLogExtensionAbility；  API声明：onDisconnect(): void;  差异内容：onDisconnect(): void; | api/@ohos.hiviewdfx.FaultLogExtensionAbility.d.ts |
| 新增API | NA | 类名：global；  API声明：export default class FaultLogExtensionContext  差异内容：export default class FaultLogExtensionContext | api/@ohos.hiviewdfx.FaultLogExtensionContext.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function getAppVMObjectUsedSize(): bigint;  差异内容：function getAppVMObjectUsedSize(): bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：interface GraphicsMemorySummary  差异内容：interface GraphicsMemorySummary | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：GraphicsMemorySummary；  API声明：gl: number;  差异内容：gl: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：GraphicsMemorySummary；  API声明：graph: number;  差异内容：graph: number; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function getGraphicsMemorySummary(interval?: number): Promise<GraphicsMemorySummary>;  差异内容：function getGraphicsMemorySummary(interval?: number): Promise<GraphicsMemorySummary>; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hilog；  API声明：function setLogLevel(level: LogLevel, prefer: PreferStrategy): void;  差异内容：function setLogLevel(level: LogLevel, prefer: PreferStrategy): void; | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：hilog；  API声明：enum PreferStrategy  差异内容：enum PreferStrategy | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：PreferStrategy；  API声明：UNSET\_LOGLEVEL = 0  差异内容：UNSET\_LOGLEVEL = 0 | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：PreferStrategy；  API声明：PREFER\_CLOSE\_LOG = 1  差异内容：PREFER\_CLOSE\_LOG = 1 | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：PreferStrategy；  API声明：PREFER\_OPEN\_LOG = 2  差异内容：PREFER\_OPEN\_LOG = 2 | api/@ohos.hilog.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.hiviewdfx.FaultLogExtensionAbility.d.ts  差异内容：PerformanceAnalysisKit | api/@ohos.hiviewdfx.FaultLogExtensionAbility.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.hiviewdfx.FaultLogExtensionContext.d.ts  差异内容：PerformanceAnalysisKit | api/@ohos.hiviewdfx.FaultLogExtensionContext.d.ts |
