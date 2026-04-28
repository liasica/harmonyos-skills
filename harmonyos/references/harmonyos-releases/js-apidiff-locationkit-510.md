---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-locationkit-510
title: Location Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Location Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:10+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:22ef938a8823b982bce8490c28fe3215e44045ce3c6422a295291d69ca090cb6
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API模型切换 | 类名：global；  API声明：export default class FenceExtensionAbility  差异内容：NA | 类名：global；  API声明：export default class FenceExtensionAbility  差异内容：stagemodelonly | api/@ohos.app.ability.FenceExtensionAbility.d.ts |
| API模型切换 | 类名：FenceExtensionAbility；  API声明：context: FenceExtensionContext;  差异内容：NA | 类名：FenceExtensionAbility；  API声明：context: FenceExtensionContext;  差异内容：stagemodelonly | api/@ohos.app.ability.FenceExtensionAbility.d.ts |
| API模型切换 | 类名：FenceExtensionAbility；  API声明：onFenceStatusChange(transition: geoLocationManager.GeofenceTransition, additions: Record<string, string>): void;  差异内容：NA | 类名：FenceExtensionAbility；  API声明：onFenceStatusChange(transition: geoLocationManager.GeofenceTransition, additions: Record<string, string>): void;  差异内容：stagemodelonly | api/@ohos.app.ability.FenceExtensionAbility.d.ts |
| API模型切换 | 类名：FenceExtensionAbility；  API声明：onDestroy(): void;  差异内容：NA | 类名：FenceExtensionAbility；  API声明：onDestroy(): void;  差异内容：stagemodelonly | api/@ohos.app.ability.FenceExtensionAbility.d.ts |
| API模型切换 | 类名：global；  API声明：export default class FenceExtensionContext  差异内容：NA | 类名：global；  API声明：export default class FenceExtensionContext  差异内容：stagemodelonly | api/@ohos.app.ability.FenceExtensionContext.d.ts |
| 删除错误码 | 类名：geoLocationManager；  API声明：function on(type: 'locationChange', request: LocationRequest | ContinuousLocationRequest, callback: Callback<Location>): void;  差异内容：3301200 | 类名：geoLocationManager；  API声明：function on(type: 'locationChange', request: LocationRequest | ContinuousLocationRequest, callback: Callback<Location>): void;  差异内容：NA | api/@ohos.geoLocationManager.d.ts |
| 删除错误码 | 类名：geoLocationManager；  API声明：function off(type: 'locationChange', callback?: Callback<Location>): void;  差异内容：3301100,3301200 | 类名：geoLocationManager；  API声明：function off(type: 'locationChange', callback?: Callback<Location>): void;  差异内容：NA | api/@ohos.geoLocationManager.d.ts |
| 删除错误码 | 类名：geoLocationManager；  API声明：function on(type: 'cachedGnssLocationsChange', request: CachedGnssLocationsRequest, callback: Callback<Array<Location>>): void;  差异内容：3301200 | 类名：geoLocationManager；  API声明：function on(type: 'cachedGnssLocationsChange', request: CachedGnssLocationsRequest, callback: Callback<Array<Location>>): void;  差异内容：NA | api/@ohos.geoLocationManager.d.ts |
| 删除错误码 | 类名：geoLocationManager；  API声明：function off(type: 'cachedGnssLocationsChange', callback?: Callback<Array<Location>>): void;  差异内容：3301200 | 类名：geoLocationManager；  API声明：function off(type: 'cachedGnssLocationsChange', callback?: Callback<Array<Location>>): void;  差异内容：NA | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：export enum SportsType  差异内容：export enum SportsType | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：SportsType；  API声明：RUNNING = 1  差异内容：RUNNING = 1 | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：SportsType；  API声明：WALKING  差异内容：WALKING | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：SportsType；  API声明：CYCLING  差异内容：CYCLING | api/@ohos.geoLocationManager.d.ts |
