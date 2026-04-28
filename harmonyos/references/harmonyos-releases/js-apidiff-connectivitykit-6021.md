---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-6021
title: Connectivity Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > Connectivity Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:44+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:064d41364684a40d38d8e85beff21e66d7061a2e90132dca582fc8c7aa74efa8
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：GattClientDevice；  API声明：getRssiValue(callback: AsyncCallback<number>): void;  差异内容：2900011 | 类名：GattClientDevice；  API声明：getRssiValue(callback: AsyncCallback<number>): void;  差异内容：NA | api/@ohos.bluetooth.ble.d.ts |
| 删除错误码 | 类名：GattClientDevice；  API声明：getRssiValue(): Promise<number>;  差异内容：2900011 | 类名：GattClientDevice；  API声明：getRssiValue(): Promise<number>;  差异内容：NA | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：getService(serviceUuid: string): GattService;  差异内容：getService(serviceUuid: string): GattService; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：getServices(): GattService[];  差异内容：getServices(): GattService[]; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：getConnectedState(deviceId: string): ProfileConnectionState;  差异内容：getConnectedState(deviceId: string): ProfileConnectionState; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：getConnectedState(): ProfileConnectionState;  差异内容：getConnectedState(): ProfileConnectionState; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：updateConnectionParam(param: ConnectionParam): Promise<void>;  差异内容：updateConnectionParam(param: ConnectionParam): Promise<void>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：on(type: 'serviceChange', callback: Callback<void>): void;  差异内容：on(type: 'serviceChange', callback: Callback<void>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：off(type: 'serviceChange', callback?: Callback<void>): void;  差异内容：off(type: 'serviceChange', callback?: Callback<void>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanResult；  API声明：advertiseFlags?: number;  差异内容：advertiseFlags?: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanResult；  API声明：manufacturerDataMap?: Map<number, Uint8Array>;  差异内容：manufacturerDataMap?: Map<number, Uint8Array>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanResult；  API声明：serviceDataMap?: Map<string, Uint8Array>;  差异内容：serviceDataMap?: Map<string, Uint8Array>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanResult；  API声明：serviceUuids?: string[];  差异内容：serviceUuids?: string[]; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanResult；  API声明：txPowerLevel?: number;  差异内容：txPowerLevel?: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanResult；  API声明：advertisingDataMap?: Map<number, Uint8Array>;  差异内容：advertisingDataMap?: Map<number, Uint8Array>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：enum ConnectionParam  差异内容：enum ConnectionParam | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ConnectionParam；  API声明：LOW\_POWER = 1  差异内容：LOW\_POWER = 1 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ConnectionParam；  API声明：BALANCED = 2  差异内容：BALANCED = 2 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ConnectionParam；  API声明：HIGH = 3  差异内容：HIGH = 3 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：access；  API声明：function convertUuid(uuid: string): string;  差异内容：function convertUuid(uuid: string): string; | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：socket；  API声明：function getMaxReceiveDataSize(clientSocket: number): number;  差异内容：function getMaxReceiveDataSize(clientSocket: number): number; | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：socket；  API声明：function getMaxTransmitDataSize(clientSocket: number): number;  差异内容：function getMaxTransmitDataSize(clientSocket: number): number; | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：socket；  API声明：function isConnected(clientSocket: number): boolean;  差异内容：function isConnected(clientSocket: number): boolean; | api/@ohos.bluetooth.socket.d.ts |
