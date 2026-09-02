---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-7001
title: Connectivity Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Connectivity Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:05+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:1b3b2bcb47cbbb62b9b826b9559aff36adb03030b990c571966f12a1c782bc1b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：connection；  API声明：function disconnectAllowedProfiles(deviceId: string): Promise<void>;  差异内容：function disconnectAllowedProfiles(deviceId: string): Promise<void>; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function onAclStateChange(callback: Callback<AclStateResult>): void;  差异内容：function onAclStateChange(callback: Callback<AclStateResult>): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function offAclStateChange(callback?: Callback<AclStateResult>): void;  差异内容：function offAclStateChange(callback?: Callback<AclStateResult>): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：interface AclStateResult  差异内容：interface AclStateResult | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：AclStateResult；  API声明：deviceId: string;  差异内容：deviceId: string; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：AclStateResult；  API声明：state: AclState;  差异内容：state: AclState; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：export enum AclState  差异内容：export enum AclState | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：AclState；  API声明：STATE\_CONNECTED = 0  差异内容：STATE\_CONNECTED = 0 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：AclState；  API声明：STATE\_DISCONNECTED = 1  差异内容：STATE\_DISCONNECTED = 1 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：function connectToCandidateConfig(settings: ConnectSettings): Promise<void>;  差异内容：function connectToCandidateConfig(settings: ConnectSettings): Promise<void>; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：enum WifiCapability  差异内容：enum WifiCapability | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiCapability；  API声明：WIFI\_AUTO\_ENABLE = 0  差异内容：WIFI\_AUTO\_ENABLE = 0 | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：interface ConnectSettings  差异内容：interface ConnectSettings | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：ConnectSettings；  API声明：networkId: number;  差异内容：networkId: number; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：ConnectSettings；  API声明：withUserAction?: boolean;  差异内容：withUserAction?: boolean; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：ConnectSettings；  API声明：userActionTimeout?: number;  差异内容：userActionTimeout?: number; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：ConnectSettings；  API声明：addNetworkToSystem?: boolean;  差异内容：addNetworkToSystem?: boolean; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：access；  API声明：function isBluetoothSupported(): boolean;  差异内容：function isBluetoothSupported(): boolean; | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：removeAllServices(): void;  差异内容：removeAllServices(): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertiseSetting；  API声明：isExtended?: boolean;  差异内容：isExtended?: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanOptions；  API声明：isExtended?: boolean;  差异内容：isExtended?: boolean; | api/@ohos.bluetooth.ble.d.ts |
