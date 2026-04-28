---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mapkit-5032
title: Map Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta2引入的API > Map Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:37+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:f3065e6a8b2bf7feeb9d1657d972e6c545d94adac7192a153e3b61a13d4fd347
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace petalMaps  差异内容： declare namespace petalMaps | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：petalMaps；  API声明：function openMapHomePage(context: common.Context): Promise<void>;  差异内容：function openMapHomePage(context: common.Context): Promise<void>; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：petalMaps；  API声明：function openMapPoiDetail(context: common.Context, poiDetailParams: PoiDetailParams): Promise<void>;  差异内容：function openMapPoiDetail(context: common.Context, poiDetailParams: PoiDetailParams): Promise<void>; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：petalMaps；  API声明：function openMapTextSearch(context: common.Context, textSearchParams: TextSearchParams): Promise<void>;  差异内容：function openMapTextSearch(context: common.Context, textSearchParams: TextSearchParams): Promise<void>; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：petalMaps；  API声明：function openMapRoutePlan(context: common.Context, routePlanParams: RoutePlanParams): Promise<void>;  差异内容：function openMapRoutePlan(context: common.Context, routePlanParams: RoutePlanParams): Promise<void>; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：petalMaps；  API声明：function openMapNavi(context: common.Context, naviParams: NaviParams): Promise<void>;  差异内容：function openMapNavi(context: common.Context, naviParams: NaviParams): Promise<void>; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：petalMaps；  API声明： interface PoiDetailParams  差异内容： interface PoiDetailParams | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：PoiDetailParams；  API声明：destinationPosition: mapCommon.LatLng;  差异内容：destinationPosition: mapCommon.LatLng; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：PoiDetailParams；  API声明：destinationName?: string;  差异内容：destinationName?: string; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：PoiDetailParams；  API声明：destinationPoiId?: string;  差异内容：destinationPoiId?: string; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：petalMaps；  API声明： interface TextSearchParams  差异内容： interface TextSearchParams | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：TextSearchParams；  API声明：destinationName?: string;  差异内容：destinationName?: string; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：petalMaps；  API声明： interface RoutePlanParams  差异内容： interface RoutePlanParams | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：RoutePlanParams；  API声明：originPosition?: mapCommon.LatLng;  差异内容：originPosition?: mapCommon.LatLng; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：RoutePlanParams；  API声明：originName?: string;  差异内容：originName?: string; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：RoutePlanParams；  API声明：originPoiId?: string;  差异内容：originPoiId?: string; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：RoutePlanParams；  API声明：destinationPosition: mapCommon.LatLng;  差异内容：destinationPosition: mapCommon.LatLng; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：RoutePlanParams；  API声明：destinationName?: string;  差异内容：destinationName?: string; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：RoutePlanParams；  API声明：destinationPoiId?: string;  差异内容：destinationPoiId?: string; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：RoutePlanParams；  API声明：vehicleType?: VehicleType;  差异内容：vehicleType?: VehicleType; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：petalMaps；  API声明： interface NaviParams  差异内容： interface NaviParams | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：NaviParams；  API声明：destinationPosition: mapCommon.LatLng;  差异内容：destinationPosition: mapCommon.LatLng; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：NaviParams；  API声明：destinationName?: string;  差异内容：destinationName?: string; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：NaviParams；  API声明：destinationPoiId?: string;  差异内容：destinationPoiId?: string; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：NaviParams；  API声明：vehicleType?: VehicleType;  差异内容：vehicleType?: VehicleType; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：petalMaps；  API声明： enum VehicleType  差异内容： enum VehicleType | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：VehicleType；  API声明：DRIVING = 0  差异内容：DRIVING = 0 | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：VehicleType；  API声明：WALKING = 1  差异内容：WALKING = 1 | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：VehicleType；  API声明：CYCLING = 2  差异内容：CYCLING = 2 | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：MapPolyline；  API声明：setCustomTexture(customTexture: ResourceStr | image.PixelMap, isTextureMappingUsed: boolean): Promise<void>;  差异内容：setCustomTexture(customTexture: ResourceStr | image.PixelMap, isTextureMappingUsed: boolean): Promise<void>; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapComponentController；  API声明：addTileOverlay(params: mapCommon.TileOverlayParams): TileOverlay;  差异内容：addTileOverlay(params: mapCommon.TileOverlayParams): TileOverlay; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapComponentController；  API声明：getLogoScale(): number;  差异内容：getLogoScale(): number; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapComponentController；  API声明：isSphereEnabled(): boolean;  差异内容：isSphereEnabled(): boolean; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapComponentController；  API声明：setSphereEnabled(enabled: boolean): void;  差异内容：setSphereEnabled(enabled: boolean): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapComponentController；  API声明：setLogoScale(logoScale: number): void;  差异内容：setLogoScale(logoScale: number): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapPolyline；  API声明：setCustomTextureIndexes(customTextureIndexes: number[]): Promise<void>;  差异内容：setCustomTextureIndexes(customTextureIndexes: number[]): Promise<void>; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：ClusterOverlay；  API声明：on(type: 'markerClusterClick', callback: Callback<MarkerClusterInfo>): void;  差异内容：on(type: 'markerClusterClick', callback: Callback<MarkerClusterInfo>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：ClusterOverlay；  API声明：off(type: 'markerClusterClick', callback?: Callback<MarkerClusterInfo>): void;  差异内容：off(type: 'markerClusterClick', callback?: Callback<MarkerClusterInfo>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：map；  API声明： interface MarkerClusterInfo  差异内容： interface MarkerClusterInfo | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MarkerClusterInfo；  API声明：marker: Marker;  差异内容：marker: Marker; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MarkerClusterInfo；  API声明：clusterItems: Array<mapCommon.ClusterItem>;  差异内容：clusterItems: Array<mapCommon.ClusterItem>; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：map；  API声明： interface TileOverlay  差异内容： interface TileOverlay | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：TileOverlay；  API声明：setTransparency(transparency: number): void;  差异内容：setTransparency(transparency: number): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：TileOverlay；  API声明：clearTileCache(): void;  差异内容：clearTileCache(): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：TileOverlay；  API声明：setFadeIn(fadeIn: boolean): void;  差异内容：setFadeIn(fadeIn: boolean): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：TileOverlay；  API声明：getTransparency(): number;  差异内容：getTransparency(): number; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：TileOverlay；  API声明：getFadeIn(): boolean;  差异内容：getFadeIn(): boolean; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapOptions；  API声明：sphereEnabled?: boolean;  差异内容：sphereEnabled?: boolean; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MapOptions；  API声明：logoScale?: number;  差异内容：logoScale?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MarkerOptions；  API声明：collisionRule?: CollisionRule;  差异内容：collisionRule?: CollisionRule; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MarkerOptions；  API声明：annotations?: Array<Text>;  差异内容：annotations?: Array<Text>; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MarkerOptions；  API声明：showIcon?: boolean;  差异内容：showIcon?: boolean; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MarkerOptions；  API声明：annotationPosition?: TextPosition;  差异内容：annotationPosition?: TextPosition; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MapPolylineOptions；  API声明：customTextures?: Array<ResourceStr | image.PixelMap>;  差异内容：customTextures?: Array<ResourceStr | image.PixelMap>; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MapPolylineOptions；  API声明：customTextureIndexes?: Array<number>;  差异内容：customTextureIndexes?: Array<number>; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MapPolylineOptions；  API声明：isTextureMappingUsed?: boolean;  差异内容：isTextureMappingUsed?: boolean; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明： interface TileOverlayParams  差异内容： interface TileOverlayParams | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TileOverlayParams；  API声明：tileUrl: string;  差异内容：tileUrl: string; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TileOverlayParams；  API声明：transparency?: number;  差异内容：transparency?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TileOverlayParams；  API声明：fadeIn?: boolean;  差异内容：fadeIn?: boolean; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：LocationQueryOptions；  API声明：themeColor?: CustomColors;  差异内容：themeColor?: CustomColors; | api/@hms.core.map.sceneMap.d.ts |
| 新增API | NA | 类名：LocationQueryOptions；  API声明：cancelCallback?: Callback<void>;  差异内容：cancelCallback?: Callback<void>; | api/@hms.core.map.sceneMap.d.ts |
| 新增API | NA | 类名：LocationChoosingOptions；  API声明：themeColor?: CustomColors;  差异内容：themeColor?: CustomColors; | api/@hms.core.map.sceneMap.d.ts |
| 新增API | NA | 类名：LocationChoosingOptions；  API声明：cancelCallback?: Callback<void>;  差异内容：cancelCallback?: Callback<void>; | api/@hms.core.map.sceneMap.d.ts |
| 新增API | NA | 类名：DistrictSelectOptions；  API声明：themeColor?: CustomColors;  差异内容：themeColor?: CustomColors; | api/@hms.core.map.sceneMap.d.ts |
| 新增API | NA | 类名：DistrictSelectOptions；  API声明：subWindowEnabled?: boolean;  差异内容：subWindowEnabled?: boolean; | api/@hms.core.map.sceneMap.d.ts |
| 新增API | NA | 类名：DistrictSelectOptions；  API声明：cancelCallback?: Callback<void>;  差异内容：cancelCallback?: Callback<void>; | api/@hms.core.map.sceneMap.d.ts |
| kit变更 | NA | MapKit | api/@hms.core.map.petalMaps.d.ts |
