---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-locationkit-7002
title: Location Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Location Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:0cd2d5825baff267b87a0aeb266ab344668f81200d885fc6bb9fd83f83a0f0df
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：geoLocationManager；  API声明：function on(type: 'locationChange', request: LocationRequest | ContinuousLocationRequest, callback: Callback<Location>): void;  差异内容：NA | 类名：geoLocationManager；  API声明：function on(type: 'locationChange', request: LocationRequest | ContinuousLocationRequest, callback: Callback<Location>): void;  差异内容：3301200 | api/@ohos.geoLocationManager.d.ts |
| 新增错误码 | 类名：geoLocationManager；  API声明：function off(type: 'locationChange', callback?: Callback<Location>): void;  差异内容：NA | 类名：geoLocationManager；  API声明：function off(type: 'locationChange', callback?: Callback<Location>): void;  差异内容：3301100,3301200 | api/@ohos.geoLocationManager.d.ts |
| 新增错误码 | 类名：geoLocationManager；  API声明：function on(type: 'cachedGnssLocationsChange', request: CachedGnssLocationsRequest, callback: Callback<Array<Location>>): void;  差异内容：NA | 类名：geoLocationManager；  API声明：function on(type: 'cachedGnssLocationsChange', request: CachedGnssLocationsRequest, callback: Callback<Array<Location>>): void;  差异内容：3301200 | api/@ohos.geoLocationManager.d.ts |
| 新增错误码 | 类名：geoLocationManager；  API声明：function off(type: 'cachedGnssLocationsChange', callback?: Callback<Array<Location>>): void;  差异内容：NA | 类名：geoLocationManager；  API声明：function off(type: 'cachedGnssLocationsChange', callback?: Callback<Array<Location>>): void;  差异内容：3301200 | api/@ohos.geoLocationManager.d.ts |
| 删除错误码 | 类名：geoLocationManager；  API声明：function off(type: 'locationChange', callback?: Callback<Location>): void;  差异内容：401 | 类名：geoLocationManager；  API声明：function off(type: 'locationChange', callback?: Callback<Location>): void;  差异内容：NA | api/@ohos.geoLocationManager.d.ts |
| 权限变更 | 类名：geoLocationManager；  API声明：function off(type: 'locationChange', callback?: Callback<Location>): void;  差异内容：ohos.permission.APPROXIMATELY\_LOCATION | 类名：geoLocationManager；  API声明：function off(type: 'locationChange', callback?: Callback<Location>): void;  差异内容：ohos.permission.APPROXIMATELY\_LOCATION [since 9 - 24] | api/@ohos.geoLocationManager.d.ts |
| 权限变更 | 类名：geoLocationManager；  API声明：function off(type: 'gnssFenceStatusChange', request: GeofenceRequest, want: WantAgent): void;  差异内容：ohos.permission.APPROXIMATELY\_LOCATION | 类名：geoLocationManager；  API声明：function off(type: 'gnssFenceStatusChange', request: GeofenceRequest, want: WantAgent): void;  差异内容：ohos.permission.APPROXIMATELY\_LOCATION [since 9 - 24] | api/@ohos.geoLocationManager.d.ts |
| 权限变更 | 类名：geoLocationManager；  API声明：function removeGnssGeofence(geofenceId: number): Promise<void>;  差异内容：ohos.permission.LOCATION and ohos.permission.APPROXIMATELY\_LOCATION | 类名：geoLocationManager；  API声明：function removeGnssGeofence(geofenceId: number): Promise<void>;  差异内容：ohos.permission.LOCATION and ohos.permission.APPROXIMATELY\_LOCATION [since 12 - 24] | api/@ohos.geoLocationManager.d.ts |
| 权限变更 | 类名：geoLocationManager；  API声明：function removeBeaconFence(beaconFence?: BeaconFence): Promise<void>;  差异内容：ohos.permission.LOCATION and ohos.permission.APPROXIMATELY\_LOCATION | 类名：geoLocationManager；  API声明：function removeBeaconFence(beaconFence?: BeaconFence): Promise<void>;  差异内容：ohos.permission.LOCATION and ohos.permission.APPROXIMATELY\_LOCATION [since 20 - 24] | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：function onLocationChange(request: LocationRequest | ContinuousLocationRequest, callback: Callback<Location>): void;  差异内容：function onLocationChange(request: LocationRequest | ContinuousLocationRequest, callback: Callback<Location>): void; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：function offLocationChange(callback?: Callback<Location>): void;  差异内容：function offLocationChange(callback?: Callback<Location>): void; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：function getCurrentDistrict(params?: DistrictRequestParams): Promise<DistrictInfo>;  差异内容：function getCurrentDistrict(params?: DistrictRequestParams): Promise<DistrictInfo>; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：function startBluetoothSearch(request: BluetoothSearchRequestParams, callback: Callback<BluetoothScanResult>): void;  差异内容：function startBluetoothSearch(request: BluetoothSearchRequestParams, callback: Callback<BluetoothScanResult>): void; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：function stopBluetoothSearch(callback?: Callback<BluetoothScanResult>): void;  差异内容：function stopBluetoothSearch(callback?: Callback<BluetoothScanResult>): void; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：function getPostProcessingTrack(sportsType: SportsType): Promise<Array<Location>>;  差异内容：function getPostProcessingTrack(sportsType: SportsType): Promise<Array<Location>>; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：export interface BluetoothSearchRequestParams  差异内容：export interface BluetoothSearchRequestParams | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BluetoothSearchRequestParams；  API声明：deviceIdArray: Array<string>;  差异内容：deviceIdArray: Array<string>; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BluetoothSearchRequestParams；  API声明：rssiThreshold?: number;  差异内容：rssiThreshold?: number; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：interface DistrictInfo  差异内容：interface DistrictInfo | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：DistrictInfo；  API声明：locale?: string;  差异内容：locale?: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：DistrictInfo；  API声明：countryCode?: string;  差异内容：countryCode?: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：DistrictInfo；  API声明：countryName?: string;  差异内容：countryName?: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：DistrictInfo；  API声明：administrativeArea?: string;  差异内容：administrativeArea?: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：DistrictInfo；  API声明：subAdministrativeArea?: string;  差异内容：subAdministrativeArea?: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：DistrictInfo；  API声明：locality?: string;  差异内容：locality?: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：DistrictInfo；  API声明：subLocality?: string;  差异内容：subLocality?: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：export interface DistrictRequestParams  差异内容：export interface DistrictRequestParams | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：DistrictRequestParams；  API声明：locale?: string;  差异内容：locale?: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：DistrictRequestParams；  API声明：timeoutMs?: number;  差异内容：timeoutMs?: number; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：ContinuousLocationRequest；  API声明：sportsType?: SportsType;  差异内容：sportsType?: SportsType; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：Location；  API声明：isFromMock?: boolean;  差异内容：isFromMock?: boolean; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：SportsType；  API声明：SKIING = 4  差异内容：SKIING = 4 | api/@ohos.geoLocationManager.d.ts |
