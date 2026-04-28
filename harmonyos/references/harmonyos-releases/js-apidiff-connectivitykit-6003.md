---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-6003
title: Connectivity Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Connectivity Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:15+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:dc71504b2ca8b0243324db17116da903b5fec4b37fed5b71a6e783e36393dbc7
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：wifiManager；  API声明：function on(type: 'hotspotStateChange', callback: Callback<number>): void;  差异内容：202 | 类名：wifiManager；  API声明：function on(type: 'hotspotStateChange', callback: Callback<number>): void;  差异内容：NA | api/@ohos.wifiManager.d.ts |
| 删除错误码 | 类名：wifiManager；  API声明：function off(type: 'hotspotStateChange', callback?: Callback<number>): void;  差异内容：202 | 类名：wifiManager；  API声明：function off(type: 'hotspotStateChange', callback?: Callback<number>): void;  差异内容：NA | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：function disableWifi(): void;  差异内容：function disableWifi(): void; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：access；  API声明：function enableBluetoothAsync(): Promise<void>;  差异内容：function enableBluetoothAsync(): Promise<void>; | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：access；  API声明：function disableBluetoothAsync(): Promise<void>;  差异内容：function disableBluetoothAsync(): Promise<void>; | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：ble；  API声明：enum GattDisconnectReason  差异内容：enum GattDisconnectReason | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattDisconnectReason；  API声明：CONN\_TIMEOUT = 1  差异内容：CONN\_TIMEOUT = 1 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattDisconnectReason；  API声明：CONN\_TERMINATE\_PEER\_USER = 2  差异内容：CONN\_TERMINATE\_PEER\_USER = 2 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattDisconnectReason；  API声明：CONN\_TERMINATE\_LOCAL\_HOST = 3  差异内容：CONN\_TERMINATE\_LOCAL\_HOST = 3 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattDisconnectReason；  API声明：CONN\_UNKNOWN = 4  差异内容：CONN\_UNKNOWN = 4 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：connection；  API声明：function getRemoteDeviceTransport(deviceId: string): BluetoothTransport;  差异内容：function getRemoteDeviceTransport(deviceId: string): BluetoothTransport; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：BluetoothTransport；  API声明：TRANSPORT\_DUAL = 2  差异内容：TRANSPORT\_DUAL = 2 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：BluetoothTransport；  API声明：TRANSPORT\_UNKNOWN = 3  差异内容：TRANSPORT\_UNKNOWN = 3 | api/@ohos.bluetooth.connection.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：BLEConnectionChangeState；  API声明：reason?: GattDisconnectReason;  差异内容：reason?: GattDisconnectReason; | api/@ohos.bluetooth.ble.d.ts |
