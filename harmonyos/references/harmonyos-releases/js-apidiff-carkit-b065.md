---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-carkit-b065
title: Car Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > Car Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:16+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:55e880ea37af5b3202a2874e798794519b71fb0a02ca322119a8d63b8d760942
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace smartMobility  差异内容： declare namespace smartMobility | api/@hms.carService.smartMobility.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace smartMobilityCommon  差异内容： declare namespace smartMobilityCommon | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：smartMobilityCommon；  API声明：function getSmartMobilityAwareness(): SmartMobilityAwareness;  差异内容：function getSmartMobilityAwareness(): SmartMobilityAwareness; | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：smartMobilityCommon；  API声明： class SmartMobilityAwareness  差异内容： class SmartMobilityAwareness | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：SmartMobilityAwareness；  API声明：on(type: 'smartMobilityStatus', smartMobilityTypes: SmartMobilityType[], callback: Callback<SmartMobilityInfo>): void;  差异内容：on(type: 'smartMobilityStatus', smartMobilityTypes: SmartMobilityType[], callback: Callback<SmartMobilityInfo>): void; | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：SmartMobilityAwareness；  API声明：off(type: 'smartMobilityStatus', smartMobilityTypes: SmartMobilityType[], callback?: Callback<SmartMobilityInfo>): void;  差异内容：off(type: 'smartMobilityStatus', smartMobilityTypes: SmartMobilityType[], callback?: Callback<SmartMobilityInfo>): void; | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：SmartMobilityAwareness；  API声明：on(type: 'smartMobilityEvent', smartMobilityTypes: SmartMobilityType[], callback: Callback<SmartMobilityEvent>): void;  差异内容：on(type: 'smartMobilityEvent', smartMobilityTypes: SmartMobilityType[], callback: Callback<SmartMobilityEvent>): void; | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：SmartMobilityAwareness；  API声明：off(type: 'smartMobilityEvent', smartMobilityTypes: SmartMobilityType[], callback?: Callback<SmartMobilityEvent>): void;  差异内容：off(type: 'smartMobilityEvent', smartMobilityTypes: SmartMobilityType[], callback?: Callback<SmartMobilityEvent>): void; | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：SmartMobilityAwareness；  API声明：getSmartMobilityStatus(type: SmartMobilityType): SmartMobilityInfo;  差异内容：getSmartMobilityStatus(type: SmartMobilityType): SmartMobilityInfo; | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：SmartMobilityAwareness；  API声明：getSmartMobilityEvent(type: SmartMobilityType, eventName: string): SmartMobilityEvent;  差异内容：getSmartMobilityEvent(type: SmartMobilityType, eventName: string): SmartMobilityEvent; | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：smartMobilityCommon；  API声明： interface SmartMobilityInfo  差异内容： interface SmartMobilityInfo | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：SmartMobilityInfo；  API声明：status: SmartMobilityStatus;  差异内容：status: SmartMobilityStatus; | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：SmartMobilityInfo；  API声明：type: SmartMobilityType;  差异内容：type: SmartMobilityType; | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：SmartMobilityInfo；  API声明：data: Record<string, Object>;  差异内容：data: Record<string, Object>; | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：smartMobilityCommon；  API声明： interface SmartMobilityEvent  差异内容： interface SmartMobilityEvent | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：SmartMobilityEvent；  API声明：eventName: string;  差异内容：eventName: string; | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：SmartMobilityEvent；  API声明：type: SmartMobilityType;  差异内容：type: SmartMobilityType; | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：SmartMobilityEvent；  API声明：data: Record<string, Object>;  差异内容：data: Record<string, Object>; | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：smartMobilityCommon；  API声明： enum SmartMobilityStatus  差异内容： enum SmartMobilityStatus | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：SmartMobilityStatus；  API声明：IDLE = 0  差异内容：IDLE = 0 | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：SmartMobilityStatus；  API声明：RUNNING = 1  差异内容：RUNNING = 1 | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：smartMobilityCommon；  API声明： enum SmartMobilityType  差异内容： enum SmartMobilityType | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：SmartMobilityType；  API声明：HICAR = 0  差异内容：HICAR = 0 | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：SmartMobilityType；  API声明：SUPER\_LAUNCHER = 1  差异内容：SUPER\_LAUNCHER = 1 | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：SmartMobilityType；  API声明：CAR\_HOP = 2  差异内容：CAR\_HOP = 2 | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增API | NA | 类名：NavigationMetadata；  API声明：customData?: Record<string, Object>;  差异内容：customData?: Record<string, Object>; | api/@hms.carService.navigationInfoMgr.d.ts |
