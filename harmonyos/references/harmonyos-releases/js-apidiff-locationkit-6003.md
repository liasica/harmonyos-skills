---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-locationkit-6003
title: Location Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Location Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:19+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:c9877cddac733bf4ea284d6201d45a0850445ef1f0ac7ca452ee20e8230e339b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：geoLocationManager；  API声明：function addBeaconFence(fenceRequest: BeaconFenceRequest): Promise<number>;  差异内容：function addBeaconFence(fenceRequest: BeaconFenceRequest): Promise<number>; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：function removeBeaconFence(beaconFence?: BeaconFence): Promise<void>;  差异内容：function removeBeaconFence(beaconFence?: BeaconFence): Promise<void>; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：function isBeaconFenceSupported(): boolean;  差异内容：function isBeaconFenceSupported(): boolean; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：export interface BeaconManufactureData  差异内容：export interface BeaconManufactureData | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BeaconManufactureData；  API声明：manufactureId: number;  差异内容：manufactureId: number; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BeaconManufactureData；  API声明：manufactureData: ArrayBuffer;  差异内容：manufactureData: ArrayBuffer; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BeaconManufactureData；  API声明：manufactureDataMask: ArrayBuffer;  差异内容：manufactureDataMask: ArrayBuffer; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：export interface BeaconFence  差异内容：export interface BeaconFence | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BeaconFence；  API声明：identifier: string;  差异内容：identifier: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BeaconFence；  API声明：beaconFenceInfoType: BeaconFenceInfoType;  差异内容：beaconFenceInfoType: BeaconFenceInfoType; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BeaconFence；  API声明：manufactureData?: BeaconManufactureData;  差异内容：manufactureData?: BeaconManufactureData; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：export interface BeaconFenceRequest  差异内容：export interface BeaconFenceRequest | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BeaconFenceRequest；  API声明：beacon: BeaconFence;  差异内容：beacon: BeaconFence; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BeaconFenceRequest；  API声明：transitionCallback?: Callback<GeofenceTransition>;  差异内容：transitionCallback?: Callback<GeofenceTransition>; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BeaconFenceRequest；  API声明：fenceExtensionAbilityName?: string;  差异内容：fenceExtensionAbilityName?: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：export enum BeaconFenceInfoType  差异内容：export enum BeaconFenceInfoType | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BeaconFenceInfoType；  API声明：BEACON\_MANUFACTURE\_DATA = 1  差异内容：BEACON\_MANUFACTURE\_DATA = 1 | api/@ohos.geoLocationManager.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：GeofenceTransition；  API声明：beaconFence?: BeaconFence;  差异内容：beaconFence?: BeaconFence; | api/@ohos.geoLocationManager.d.ts |
