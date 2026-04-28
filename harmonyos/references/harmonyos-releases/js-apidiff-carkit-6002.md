---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-carkit-6002
title: Car Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > Car Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:27+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:96bcedca5ca415cfc0ca1e0b20ac48e86714e9bb00eb05e5d6c830dbc5b6aeff
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：navigationInfoMgr；  API声明：function getNavigationController(): NavigationController;  差异内容：NA | 类名：navigationInfoMgr；  API声明：function getNavigationController(): NavigationController;  差异内容：801 | api/@hms.carService.navigationInfoMgr.d.ts |
| 新增错误码 | 类名：NavigationController；  API声明：updateNavigationStatus(navigationStatus: NavigationStatus): void;  差异内容：NA | 类名：NavigationController；  API声明：updateNavigationStatus(navigationStatus: NavigationStatus): void;  差异内容：1003810001,1003810002,801 | api/@hms.carService.navigationInfoMgr.d.ts |
| 新增错误码 | 类名：NavigationController；  API声明：updateNavigationMetadata(navigationMetadata: NavigationMetadata): void;  差异内容：NA | 类名：NavigationController；  API声明：updateNavigationMetadata(navigationMetadata: NavigationMetadata): void;  差异内容：1003810001,1003810002,801 | api/@hms.carService.navigationInfoMgr.d.ts |
| 新增错误码 | 类名：NavigationController；  API声明：registerSystemNavigationListener(listener: SystemNavigationListener): void;  差异内容：NA | 类名：NavigationController；  API声明：registerSystemNavigationListener(listener: SystemNavigationListener): void;  差异内容：1003810001,801 | api/@hms.carService.navigationInfoMgr.d.ts |
| 新增错误码 | 类名：NavigationController；  API声明：unregisterSystemNavigationListener(): void;  差异内容：NA | 类名：NavigationController；  API声明：unregisterSystemNavigationListener(): void;  差异内容：801 | api/@hms.carService.navigationInfoMgr.d.ts |
| 新增错误码 | 类名：smartMobilityCommon；  API声明：function getSmartMobilityAwareness(): SmartMobilityAwareness;  差异内容：NA | 类名：smartMobilityCommon；  API声明：function getSmartMobilityAwareness(): SmartMobilityAwareness;  差异内容：801 | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增错误码 | 类名：SmartMobilityAwareness；  API声明：on(type: 'smartMobilityStatus', smartMobilityTypes: SmartMobilityType[], callback: Callback<SmartMobilityInfo>): void;  差异内容：NA | 类名：SmartMobilityAwareness；  API声明：on(type: 'smartMobilityStatus', smartMobilityTypes: SmartMobilityType[], callback: Callback<SmartMobilityInfo>): void;  差异内容：801 | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增错误码 | 类名：SmartMobilityAwareness；  API声明：off(type: 'smartMobilityStatus', smartMobilityTypes: SmartMobilityType[], callback?: Callback<SmartMobilityInfo>): void;  差异内容：NA | 类名：SmartMobilityAwareness；  API声明：off(type: 'smartMobilityStatus', smartMobilityTypes: SmartMobilityType[], callback?: Callback<SmartMobilityInfo>): void;  差异内容：801 | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增错误码 | 类名：SmartMobilityAwareness；  API声明：on(type: 'smartMobilityEvent', smartMobilityTypes: SmartMobilityType[], callback: Callback<SmartMobilityEvent>): void;  差异内容：NA | 类名：SmartMobilityAwareness；  API声明：on(type: 'smartMobilityEvent', smartMobilityTypes: SmartMobilityType[], callback: Callback<SmartMobilityEvent>): void;  差异内容：801 | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增错误码 | 类名：SmartMobilityAwareness；  API声明：off(type: 'smartMobilityEvent', smartMobilityTypes: SmartMobilityType[], callback?: Callback<SmartMobilityEvent>): void;  差异内容：NA | 类名：SmartMobilityAwareness；  API声明：off(type: 'smartMobilityEvent', smartMobilityTypes: SmartMobilityType[], callback?: Callback<SmartMobilityEvent>): void;  差异内容：801 | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增错误码 | 类名：SmartMobilityAwareness；  API声明：getSmartMobilityStatus(type: SmartMobilityType): SmartMobilityInfo;  差异内容：NA | 类名：SmartMobilityAwareness；  API声明：getSmartMobilityStatus(type: SmartMobilityType): SmartMobilityInfo;  差异内容：801 | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增错误码 | 类名：SmartMobilityAwareness；  API声明：getSmartMobilityEvent(type: SmartMobilityType, eventName: string): SmartMobilityEvent;  差异内容：NA | 类名：SmartMobilityAwareness；  API声明：getSmartMobilityEvent(type: SmartMobilityType, eventName: string): SmartMobilityEvent;  差异内容：801 | api/@hms.carService.smartMobilityCommon.d.ts |
