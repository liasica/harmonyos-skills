---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-6011
title: Connectivity Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Beta1引入的API > Connectivity Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:57+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:bfec035c5164fc0975fa79fd47f0f8e47115eb646bc2548dfa929a5355c5ef4e
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace common  差异内容：declare namespace common | api/@ohos.bluetooth.common.d.ts |
| 新增API | NA | 类名：common；  API声明：export interface BluetoothAddress  差异内容：export interface BluetoothAddress | api/@ohos.bluetooth.common.d.ts |
| 新增API | NA | 类名：BluetoothAddress；  API声明：address: string;  差异内容：address: string; | api/@ohos.bluetooth.common.d.ts |
| 新增API | NA | 类名：BluetoothAddress；  API声明：addressType: BluetoothAddressType;  差异内容：addressType: BluetoothAddressType; | api/@ohos.bluetooth.common.d.ts |
| 新增API | NA | 类名：common；  API声明：export enum BluetoothAddressType  差异内容：export enum BluetoothAddressType | api/@ohos.bluetooth.common.d.ts |
| 新增API | NA | 类名：BluetoothAddressType；  API声明：VIRTUAL = 1  差异内容：VIRTUAL = 1 | api/@ohos.bluetooth.common.d.ts |
| 新增API | NA | 类名：BluetoothAddressType；  API声明：REAL = 2  差异内容：REAL = 2 | api/@ohos.bluetooth.common.d.ts |
| 新增API | NA | 类名：ble；  API声明：function getConnectedBLEDevices(profile: BleProfile): Array<string>;  差异内容：function getConnectedBLEDevices(profile: BleProfile): Array<string>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：enum BleProfile  差异内容：enum BleProfile | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BleProfile；  API声明：GATT = 1  差异内容：GATT = 1 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BleProfile；  API声明：GATT\_CLIENT = 2  差异内容：GATT\_CLIENT = 2 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BleProfile；  API声明：GATT\_SERVER = 3  差异内容：GATT\_SERVER = 3 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：connection；  API声明：function pairDevice(deviceId: BluetoothAddress): Promise<void>;  差异内容：function pairDevice(deviceId: BluetoothAddress): Promise<void>; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：type BluetoothAddress = common.BluetoothAddress;  差异内容：type BluetoothAddress = common.BluetoothAddress; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：function startScan(): void;  差异内容：function startScan(): void; | api/@ohos.wifiManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.bluetooth.common.d.ts  差异内容：ConnectivityKit | api/@ohos.bluetooth.common.d.ts |
