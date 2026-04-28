---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-b031
title: Connectivity Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Connectivity Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:37+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:18a1ee5de14946007044f108ad2086e090766390bde03fb4af1c9558cff0b275
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：connection；  API声明：function setLocalName(name: string): void;  差异内容：NA | 类名：connection；  API声明：function setLocalName(name: string): void;  差异内容：12 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function getRemoteProfileUuids(deviceId: string, callback: AsyncCallback<Array<ProfileUuids>>): void;  差异内容：function getRemoteProfileUuids(deviceId: string, callback: AsyncCallback<Array<ProfileUuids>>): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function getRemoteProfileUuids(deviceId: string): Promise<Array<ProfileUuids>>;  差异内容：function getRemoteProfileUuids(deviceId: string): Promise<Array<ProfileUuids>>; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：WifiDeviceConfig；  API声明：wapiConfig?: WifiWapiConfig;  差异内容：wapiConfig?: WifiWapiConfig; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明： interface WifiWapiConfig  差异内容： interface WifiWapiConfig | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiWapiConfig；  API声明：wapiPskType: WapiPskType;  差异内容：wapiPskType: WapiPskType; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiWapiConfig；  API声明：wapiAsCert: string;  差异内容：wapiAsCert: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiWapiConfig；  API声明：wapiUserCert: string;  差异内容：wapiUserCert: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明： enum WapiPskType  差异内容： enum WapiPskType | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WapiPskType；  API声明：WAPI\_PSK\_ASCII = 0  差异内容：WAPI\_PSK\_ASCII = 0 | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WapiPskType；  API声明：WAPI\_PSK\_HEX = 1  差异内容：WAPI\_PSK\_HEX = 1 | api/@ohos.wifiManager.d.ts |
