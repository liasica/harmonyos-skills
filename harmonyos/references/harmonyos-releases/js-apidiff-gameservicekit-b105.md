---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-gameservicekit-b105
title: Game Service Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > OS平台能力 > API变更清单 > HarmonyOS 5.0.1(13) Beta3引入的API > Game Service Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:03+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:11ab07ff6af71b50f2432e47c4c457ac2473e16c3b19dfbf32f53bc05d012508
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：gamePerformance；  API声明：function on(type: 'deviceStateChanged', callback: Callback<DeviceInfo>, scope: Array<DeviceInfoType>): void;  差异内容：function on(type: 'deviceStateChanged', callback: Callback<DeviceInfo>, scope: Array<DeviceInfoType>): void; | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：gamePerformance；  API声明： interface ThermalInfo  差异内容： interface ThermalInfo | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：ThermalInfo；  API声明：thermalMargin?: number;  差异内容：thermalMargin?: number; | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：ThermalInfo；  API声明：thermalTrend?: number;  差异内容：thermalTrend?: number; | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：DeviceInfo；  API声明：thermalInfo?: ThermalInfo;  差异内容：thermalInfo?: ThermalInfo; | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：gamePerformance；  API声明： enum DeviceInfoType  差异内容： enum DeviceInfoType | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：DeviceInfoType；  API声明：THERMAL = 1  差异内容：THERMAL = 1 | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：DeviceInfoType；  API声明：GPU = 2  差异内容：GPU = 2 | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：gamePerformance；  API声明： interface DeviceInfoParameter  差异内容： interface DeviceInfoParameter | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：DeviceInfoParameter；  API声明：deviceInfoType: DeviceInfoType;  差异内容：deviceInfoType: DeviceInfoType; | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：DeviceInfoParameter；  API声明：parameters?: Record<string, string>;  差异内容：parameters?: Record<string, string>; | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：gamePerformance；  API声明： enum DeviceInfoParameterKey  差异内容： enum DeviceInfoParameterKey | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：DeviceInfoParameterKey；  API声明：THERMAL\_TEMP\_LEVEL = 'tempLevel'  差异内容：THERMAL\_TEMP\_LEVEL = 'tempLevel' | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：gamePerformance；  API声明：function getDeviceInfoByScope(scope: Array<DeviceInfoParameter>): Promise<DeviceInfo>;  差异内容：function getDeviceInfoByScope(scope: Array<DeviceInfoParameter>): Promise<DeviceInfo>; | api/@hms.core.gameservice.gameperformance.d.ts |
