---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-gameservicekit-6002
title: Game Service Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > Game Service Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:29+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:97d3312cceb447e548be5566d5558522ba5a0935bc316c057a2a5d716f7d58f6
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：interface BindParameters  差异内容：interface BindParameters | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：BindParameters；  API声明：deviceId: string;  差异内容：deviceId: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：BindParameters；  API声明：networkId: string;  差异内容：networkId: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：interface NearbyGameDevice  差异内容：interface NearbyGameDevice | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：NearbyGameDevice；  API声明：deviceName: string;  差异内容：deviceName: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：NearbyGameDevice；  API声明：deviceId: string;  差异内容：deviceId: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：NearbyGameDevice；  API声明：networkId: string;  差异内容：networkId: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：interface DiscoveryResult  差异内容：interface DiscoveryResult | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：DiscoveryResult；  API声明：nearbyGameDevices: Array<NearbyGameDevice>;  差异内容：nearbyGameDevices: Array<NearbyGameDevice>; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：enum Mode  差异内容：enum Mode | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：Mode；  API声明：API = 1  差异内容：API = 1 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：Mode；  API声明：KNOCK = 2  差异内容：KNOCK = 2 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：NearbyTransferErrorCode；  API声明：INVALID\_PARAMETER = 1018300008  差异内容：INVALID\_PARAMETER = 1018300008 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：function on(type: 'discovery', callback: Callback<DiscoveryResult>): void;  差异内容：function on(type: 'discovery', callback: Callback<DiscoveryResult>): void; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：function off(type: 'discovery', callback?: Callback<DiscoveryResult>): void;  差异内容：function off(type: 'discovery', callback?: Callback<DiscoveryResult>): void; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：function discoveryNearbyGame(): Promise<void>;  差异内容：function discoveryNearbyGame(): Promise<void>; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer；  API声明：function bindNearbyGame(bindParameters: BindParameters): Promise<void>;  差异内容：function bindNearbyGame(bindParameters: BindParameters): Promise<void>; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CreateParameters；  API声明：mode?: Mode;  差异内容：mode?: Mode; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
