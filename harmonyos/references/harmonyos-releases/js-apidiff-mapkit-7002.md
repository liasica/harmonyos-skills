---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mapkit-7002
title: Map Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Map Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:3c49ce4080a9af91bf233bc22751c126bb888d34da740730f61d7a89d3fd895a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：MapPolyline；  API声明：setCustomTextureIndexes(customTextureIndexes: number[]): Promise<void>;  差异内容：401 | 类名：MapPolyline；  API声明：setCustomTextureIndexes(customTextureIndexes: number[]): Promise<void>;  差异内容：NA | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace offlineMapData  差异内容：declare namespace offlineMapData | api/@hms.core.map.offlineMapData.d.ts |
| 新增API | NA | 类名：offlineMapData；  API声明：function getRecommendedCityIdsByLatLngs(context: common.Context, latlngs: mapCommon.LatLng[]): Promise<string[]>;  差异内容：function getRecommendedCityIdsByLatLngs(context: common.Context, latlngs: mapCommon.LatLng[]): Promise<string[]>; | api/@hms.core.map.offlineMapData.d.ts |
| 新增API | NA | 类名：MapComponentController；  API声明：setSphereMapEnabled(enabled: boolean, params?: mapCommon.SphereParams): Promise<void>;  差异内容：setSphereMapEnabled(enabled: boolean, params?: mapCommon.SphereParams): Promise<void>; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapComponentController；  API声明：addSignalLine(signalParams: mapCommon.MapSignalParams): Promise<MapSignalLine>;  差异内容：addSignalLine(signalParams: mapCommon.MapSignalParams): Promise<MapSignalLine>; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapComponentController；  API声明：removeSignalLineCache(signalLineId?: string): void;  差异内容：removeSignalLineCache(signalLineId?: string): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapPolyline；  API声明：addLineText(lineText: mapCommon.LineText): void;  差异内容：addLineText(lineText: mapCommon.LineText): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapPolyline；  API声明：removeLineText(): void;  差异内容：removeLineText(): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：map；  API声明：interface MapSignalLine  差异内容：interface MapSignalLine | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapSignalLine；  API声明：setColors(colors: number[]): void;  差异内容：setColors(colors: number[]): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapSignalLine；  API声明：getColors(): number[];  差异内容：getColors(): number[]; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapSignalLine；  API声明：setWidth(width: number): void;  差异内容：setWidth(width: number): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapSignalLine；  API声明：getWidth(): number;  差异内容：getWidth(): number; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MyLocationDisplayType；  API声明：MAP\_ROTATE = 5  差异内容：MAP\_ROTATE = 5 | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MyLocationDisplayType；  API声明：MAP\_ROTATE\_NO\_CENTER = 6  差异内容：MAP\_ROTATE\_NO\_CENTER = 6 | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明：interface SphereParams  差异内容：interface SphereParams | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：SphereParams；  API声明：sunLightEnabled?: boolean;  差异内容：sunLightEnabled?: boolean; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：SphereParams；  API声明：cityLightEnabled?: boolean;  差异内容：cityLightEnabled?: boolean; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：SphereParams；  API声明：animateDuration?: number;  差异内容：animateDuration?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：SphereParams；  API声明：backgroundImage?: ResourceStr | image.PixelMap;  差异内容：backgroundImage?: ResourceStr | image.PixelMap; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：SphereParams；  API声明：coverageImage?: ResourceStr | image.PixelMap;  差异内容：coverageImage?: ResourceStr | image.PixelMap; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明：interface LineText  差异内容：interface LineText | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：LineText；  API声明：lineNames: string[];  差异内容：lineNames: string[]; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：LineText；  API声明：lineNameIndexes: number[];  差异内容：lineNameIndexes: number[]; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：LineText；  API声明：nameOnRight?: boolean;  差异内容：nameOnRight?: boolean; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：LineText；  API声明：color?: number;  差异内容：color?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：LineText；  API声明：fontSize?: number;  差异内容：fontSize?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：LineText；  API声明：strokeColor?: number;  差异内容：strokeColor?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：LineText；  API声明：fontStyle?: FontStyle;  差异内容：fontStyle?: FontStyle; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明：interface MapSignalParams  差异内容：interface MapSignalParams | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MapSignalParams；  API声明：signalId: string;  差异内容：signalId: string; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MapSignalParams；  API声明：points?: LatLng[];  差异内容：points?: LatLng[]; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MapSignalParams；  API声明：colors?: number[];  差异内容：colors?: number[]; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MapSignalParams；  API声明：width?: number;  差异内容：width?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MapSignalParams；  API声明：coordinateType?: CoordinateType;  差异内容：coordinateType?: CoordinateType; | api/@hms.core.map.mapCommon.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.core.map.offlineMapData.d.ts  差异内容：MapKit | api/@hms.core.map.offlineMapData.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Projection；  API声明：fromScreenLocation(point: mapCommon.MapPoint): mapCommon.LatLng;  差异内容：fromScreenLocation(point: mapCommon.MapPoint): mapCommon.LatLng; | 类名：Projection；  API声明：fromScreenLocation(point: mapCommon.MapPoint, altitude: number): mapCommon.LatLng;  差异内容：fromScreenLocation(point: mapCommon.MapPoint, altitude: number): mapCommon.LatLng; | api/@hms.core.map.map.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Projection；  API声明：toScreenLocation(position: mapCommon.LatLng): mapCommon.MapPoint;  差异内容：toScreenLocation(position: mapCommon.LatLng): mapCommon.MapPoint; | 类名：Projection；  API声明：toScreenLocation(position: mapCommon.LatLng, altitude: number): mapCommon.MapPoint;  差异内容：toScreenLocation(position: mapCommon.LatLng, altitude: number): mapCommon.MapPoint; | api/@hms.core.map.map.d.ts |
| 修改导出符号 | 类名：global；  API声明：export type customInfoWindowCallback = (markerDelegate: map.MarkerDelegate) => void;  差异内容：export type customInfoWindowCallback = (markerDelegate: map.MarkerDelegate) => void; | 类名：global；  API声明：export { mapCommon, map, MapComponent, staticMap, site, navi, sceneMap, petalMaps, offlineMapData, customInfoWindowCallback };  差异内容：export { mapCommon, map, MapComponent, staticMap, site, navi, sceneMap, petalMaps, offlineMapData, customInfoWindowCallback }; | kits/@kit.MapKit.d.ts |
