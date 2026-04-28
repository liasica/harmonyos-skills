---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-5032
title: Connectivity Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta2引入的API > Connectivity Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:34+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:6fbc6b4b53cfac89a04c6972494c0d471b0e2a01c9ad18be83ae6467bb5cbf5a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：ble；  API声明：function createBleScanner(): BleScanner;  差异内容：function createBleScanner(): BleScanner; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface BleScanner  差异内容： interface BleScanner | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BleScanner；  API声明：startScan(filters: Array<ScanFilter>, options?: ScanOptions): Promise<void>;  差异内容：startScan(filters: Array<ScanFilter>, options?: ScanOptions): Promise<void>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BleScanner；  API声明：stopScan(): Promise<void>;  差异内容：stopScan(): Promise<void>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BleScanner；  API声明：on(type: 'BLEDeviceFind', callback: Callback<ScanReport>): void;  差异内容：on(type: 'BLEDeviceFind', callback: Callback<ScanReport>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BleScanner；  API声明：off(type: 'BLEDeviceFind', callback?: Callback<ScanReport>): void;  差异内容：off(type: 'BLEDeviceFind', callback?: Callback<ScanReport>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface ScanReport  差异内容： interface ScanReport | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanReport；  API声明：reportType: ScanReportType;  差异内容：reportType: ScanReportType; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanReport；  API声明：scanResult: Array<ScanResult>;  差异内容：scanResult: Array<ScanResult>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanOptions；  API声明：reportMode?: ScanReportMode;  差异内容：reportMode?: ScanReportMode; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： enum ScanReportMode  差异内容： enum ScanReportMode | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanReportMode；  API声明：NORMAL = 1  差异内容：NORMAL = 1 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： enum ScanReportType  差异内容： enum ScanReportType | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanReportType；  API声明：ON\_FOUND = 1  差异内容：ON\_FOUND = 1 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanReportType；  API声明：ON\_LOST = 2  差异内容：ON\_LOST = 2 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：connection；  API声明：function getLastConnectionTime(deviceId: string): Promise<number>;  差异内容：function getLastConnectionTime(deviceId: string): Promise<number>; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：function enableWifi(): void;  差异内容：function enableWifi(): void; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：function addDeviceConfig(config: WifiDeviceConfig): Promise<number>;  差异内容：function addDeviceConfig(config: WifiDeviceConfig): Promise<number>; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：function addDeviceConfig(config: WifiDeviceConfig, callback: AsyncCallback<number>): void;  差异内容：function addDeviceConfig(config: WifiDeviceConfig, callback: AsyncCallback<number>): void; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：function connectToNetwork(networkId: number): void;  差异内容：function connectToNetwork(networkId: number): void; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：function disconnect(): void;  差异内容：function disconnect(): void; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：function getDeviceMacAddress(): string[];  差异内容：function getDeviceMacAddress(): string[]; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：function getDeviceConfigs(): Array<WifiDeviceConfig>;  差异内容：function getDeviceConfigs(): Array<WifiDeviceConfig>; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：function removeDevice(id: number): void;  差异内容：function removeDevice(id: number): void; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiCategory；  API声明：WIFI7 = 4  差异内容：WIFI7 = 4 | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiCategory；  API声明：WIFI7\_PLUS = 5  差异内容：WIFI7\_PLUS = 5 | api/@ohos.wifiManager.d.ts |
