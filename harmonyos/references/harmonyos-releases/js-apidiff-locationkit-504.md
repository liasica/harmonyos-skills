---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-locationkit-504
title: Location Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.4(16) > OS平台能力 > API变更清单 > Location Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:27+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:3fc768cc59e793d5eeb22c93f45e98c871cfc43074ed7b1bdf997fcb0058b01f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：geoLocationManager；  API声明：function on(type: 'bluetoothScanResultChange', callback: Callback<BluetoothScanResult>): void;  差异内容：function on(type: 'bluetoothScanResultChange', callback: Callback<BluetoothScanResult>): void; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：function off(type: 'bluetoothScanResultChange', callback?: Callback<BluetoothScanResult>): void;  差异内容：function off(type: 'bluetoothScanResultChange', callback?: Callback<BluetoothScanResult>): void; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明： export interface BluetoothScanResult  差异内容： export interface BluetoothScanResult | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BluetoothScanResult；  API声明：deviceId: string;  差异内容：deviceId: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BluetoothScanResult；  API声明：rssi: number;  差异内容：rssi: number; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BluetoothScanResult；  API声明：data?: ArrayBuffer;  差异内容：data?: ArrayBuffer; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BluetoothScanResult；  API声明：deviceName: string;  差异内容：deviceName: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BluetoothScanResult；  API声明：connectable: boolean;  差异内容：connectable: boolean; | api/@ohos.geoLocationManager.d.ts |
