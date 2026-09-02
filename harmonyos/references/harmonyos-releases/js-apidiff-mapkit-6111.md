---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mapkit-6111
title: Map Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > Map Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:c70fd92d2f4fc19f8987cb1f123652ee4788e09154d9d325b0b91f7b85728959
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：MapEventManager；  API声明：onMarkerLongClick(callback: Callback<Marker>): void;  差异内容：onMarkerLongClick(callback: Callback<Marker>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager；  API声明：offMarkerLongClick(callback?: Callback<Marker>): void;  差异内容：offMarkerLongClick(callback?: Callback<Marker>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager；  API声明：onPoiLongClick(callback: Callback<mapCommon.Poi>): void;  差异内容：onPoiLongClick(callback: Callback<mapCommon.Poi>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager；  API声明：offPoiLongClick(callback?: Callback<mapCommon.Poi>): void;  差异内容：offPoiLongClick(callback?: Callback<mapCommon.Poi>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MarkerOptions；  API声明：annotationBackgroundColor?: number;  差异内容：annotationBackgroundColor?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TileOverlayOptions；  API声明：tileDataReuse?: number[];  差异内容：tileDataReuse?: number[]; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：petalMaps；  API声明：function openMapOfflineDataManagement(context: common.Context, offlineDataParams: OfflineDataParams): Promise<void>;  差异内容：function openMapOfflineDataManagement(context: common.Context, offlineDataParams: OfflineDataParams): Promise<void>; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：PoiDetailParams；  API声明：destinationAddress?: string;  差异内容：destinationAddress?: string; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：petalMaps；  API声明：interface OfflineDataParams  差异内容：interface OfflineDataParams | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：OfflineDataParams；  API声明：scenarios: string;  差异内容：scenarios: string; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：OfflineDataParams；  API声明：recommendedRegionIds?: string[];  差异内容：recommendedRegionIds?: string[]; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：DistrictSelectOptions；  API声明：maxAdminLevel?: number;  差异内容：maxAdminLevel?: number; | api/@hms.core.map.sceneMap.d.ts |
| 新增API | NA | 类名：Site；  API声明：reliability?: number;  差异内容：reliability?: number; | api/@hms.core.map.site.d.ts |
