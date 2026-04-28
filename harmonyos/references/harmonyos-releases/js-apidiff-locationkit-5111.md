---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-locationkit-5111
title: Location Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > Location Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:54+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:7e79f6fba389cb1e45841412221c6eaae1e3ef3bc2b216527402f0d2d549e676
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：geoLocationManager；  API声明：export interface Poi  差异内容：export interface Poi | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：Poi；  API声明：id: string;  差异内容：id: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：Poi；  API声明：confidence: number;  差异内容：confidence: number; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：Poi；  API声明：name: string;  差异内容：name: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：Poi；  API声明：latitude: number;  差异内容：latitude: number; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：Poi；  API声明：longitude: number;  差异内容：longitude: number; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：Poi；  API声明：administrativeArea: string;  差异内容：administrativeArea: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：Poi；  API声明：subAdministrativeArea: string;  差异内容：subAdministrativeArea: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：Poi；  API声明：locality: string;  差异内容：locality: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：Poi；  API声明：subLocality: string;  差异内容：subLocality: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：Poi；  API声明：address: string;  差异内容：address: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager；  API声明：export interface PoiInfo  差异内容：export interface PoiInfo | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：PoiInfo；  API声明：poiArray: Array<Poi>;  差异内容：poiArray: Array<Poi>; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：PoiInfo；  API声明：timestamp: number;  差异内容：timestamp: number; | api/@ohos.geoLocationManager.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ContinuousLocationRequest；  API声明：needPoi?: boolean;  差异内容：needPoi?: boolean; | api/@ohos.geoLocationManager.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：SingleLocationRequest；  API声明：needPoi?: boolean;  差异内容：needPoi?: boolean; | api/@ohos.geoLocationManager.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Location；  API声明：poi?: PoiInfo;  差异内容：poi?: PoiInfo; | api/@ohos.geoLocationManager.d.ts |
