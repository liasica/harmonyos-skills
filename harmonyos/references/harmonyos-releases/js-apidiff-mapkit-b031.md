---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mapkit-b031
title: Map Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Map Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:41+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:8f015039cd6dd8f945c0ab43cb497880a8a1df71f931c34035785b78fcc208e2
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：sceneMap；  API声明：function queryLocation(context: common.UIAbilityContext, options: LocationQueryOptions): Promise<void>;  差异内容：1002600001,1002600002,1002600003,1002600004,1002600012,401 | 类名：sceneMap；  API声明：function queryLocation(context: common.UIAbilityContext, options: LocationQueryOptions): Promise<void>;  差异内容：1002600001,1002600002,1002600003,1002600004,401 | api/@hms.core.map.sceneMap.d.ts |
| 错误码变更 | 类名：sceneMap；  API声明：function selectDistrict(context: common.Context, options: DistrictSelectOptions): Promise<DistrictSelectResult>;  差异内容：1002600001,1002600002,1002600003,1002600004,401 | 类名：sceneMap；  API声明：function selectDistrict(context: common.Context, options: DistrictSelectOptions): Promise<DistrictSelectResult>;  差异内容：1002600001,1002600002,1002600003,1002600004,1002600012,401 | api/@hms.core.map.sceneMap.d.ts |
| 函数变更 | 类名：ClusterOverlay；  API声明：off(type: 'clusterClick', callback: Callback<void>): void;  差异内容：callback: Callback<void> | 类名：ClusterOverlay；  API声明：off(type: 'clusterClick', callback?: Callback<void>): void;  差异内容：callback?: Callback<void> | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapComponentController；  API声明：addBuildingOverlay(params: mapCommon.BuildingOverlayParams): Promise<BuildingOverlay>;  差异内容：addBuildingOverlay(params: mapCommon.BuildingOverlayParams): Promise<BuildingOverlay>; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapComponentController；  API声明：addTraceOverlay(params: mapCommon.TraceOverlayParams, markers?: Array<Marker>): Promise<TraceOverlay>;  差异内容：addTraceOverlay(params: mapCommon.TraceOverlayParams, markers?: Array<Marker>): Promise<TraceOverlay>; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapComponentController；  API声明：show(): void;  差异内容：show(): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapComponentController；  API声明：hide(): void;  差异内容：hide(): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：map；  API声明： interface BuildingOverlay  差异内容： interface BuildingOverlay | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：BuildingOverlay；  API声明：getId(): string;  差异内容：getId(): string; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：BuildingOverlay；  API声明：remove(): void;  差异内容：remove(): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：BuildingOverlay；  API声明：setSideVisible(visible: boolean): void;  差异内容：setSideVisible(visible: boolean): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：BuildingOverlay；  API声明：setFloorVisible(visible: boolean): void;  差异内容：setFloorVisible(visible: boolean): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：BuildingOverlay；  API声明：setFloorBottomHeight(height: number): void;  差异内容：setFloorBottomHeight(height: number): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：map；  API声明： interface TraceOverlay  差异内容： interface TraceOverlay | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：TraceOverlay；  API声明：getId(): string;  差异内容：getId(): string; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：TraceOverlay；  API声明：remove(): void;  差异内容：remove(): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：TraceOverlay；  API声明：pause(): void;  差异内容：pause(): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：TraceOverlay；  API声明：resume(): void;  差异内容：resume(): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：navi；  API声明：function getDrivingMatrix(context: common.Context, params: DrivingMatrixParams): Promise<MatrixResult>;  差异内容：function getDrivingMatrix(context: common.Context, params: DrivingMatrixParams): Promise<MatrixResult>; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：function getWalkingMatrix(context: common.Context, params: MatrixParams): Promise<MatrixResult>;  差异内容：function getWalkingMatrix(context: common.Context, params: MatrixParams): Promise<MatrixResult>; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：function getCyclingMatrix(context: common.Context, params: MatrixParams): Promise<MatrixResult>;  差异内容：function getCyclingMatrix(context: common.Context, params: MatrixParams): Promise<MatrixResult>; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：function snapToRoads(context: common.Context, params: SnapToRoadsParams): Promise<SnapToRoadsResult>;  差异内容：function snapToRoads(context: common.Context, params: SnapToRoadsParams): Promise<SnapToRoadsResult>; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：site；  API声明：function nearbySearch(context: common.Context, nearbySearchParams: NearbySearchParams): Promise<NearbySearchResult>;  差异内容：function nearbySearch(context: common.Context, nearbySearchParams: NearbySearchParams): Promise<NearbySearchResult>; | api/@hms.core.map.site.d.ts |
| 新增API | NA | 类名：site；  API声明：function queryAutoComplete(context: common.Context, queryAutoCompleteParams: QueryAutoCompleteParams): Promise<QueryAutoCompleteResult>;  差异内容：function queryAutoComplete(context: common.Context, queryAutoCompleteParams: QueryAutoCompleteParams): Promise<QueryAutoCompleteResult>; | api/@hms.core.map.site.d.ts |
| 新增API | NA | 类名：site；  API声明：function searchById(context: common.Context, searchByIdParams: SearchByIdParams): Promise<SearchByIdResult>;  差异内容：function searchById(context: common.Context, searchByIdParams: SearchByIdParams): Promise<SearchByIdResult>; | api/@hms.core.map.site.d.ts |
| 新增API | NA | 类名：site；  API声明：function geocode(context: common.Context, geocodeParams: GeocodeParams): Promise<GeocodeResult>;  差异内容：function geocode(context: common.Context, geocodeParams: GeocodeParams): Promise<GeocodeResult>; | api/@hms.core.map.site.d.ts |
| 新增API | NA | 类名：site；  API声明：function reverseGeocode(context: common.Context, reverseGeocodeParams: ReverseGeocodeParams): Promise<ReverseGeocodeResult>;  差异内容：function reverseGeocode(context: common.Context, reverseGeocodeParams: ReverseGeocodeParams): Promise<ReverseGeocodeResult>; | api/@hms.core.map.site.d.ts |
| 新增API | NA | 类名：ReverseGeocodeParams；  API声明：isNearbyAoi?: boolean;  差异内容：isNearbyAoi?: boolean; | api/@hms.core.map.site.d.ts |
| 新增API | NA | 类名：ReverseGeocodeParams；  API声明：sortRule?: SortRule;  差异内容：sortRule?: SortRule; | api/@hms.core.map.site.d.ts |
| 新增API | NA | 类名：Aoi；  API声明：direction?: string;  差异内容：direction?: string; | api/@hms.core.map.site.d.ts |
| 新增API | NA | 类名：staticMap；  API声明：function getMapImage(context: common.Context, options: StaticMapOptions): Promise<image.PixelMap>;  差异内容：function getMapImage(context: common.Context, options: StaticMapOptions): Promise<image.PixelMap>; | api/@hms.core.map.staticMap.d.ts |
| 新增API | NA | 类名：PointAnnotationParams；  API声明：textPosition?: TextPosition;  差异内容：textPosition?: TextPosition; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明： interface BuildingOverlayParams  差异内容： interface BuildingOverlayParams | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：BuildingOverlayParams；  API声明：points: Array<LatLng>;  差异内容：points: Array<LatLng>; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：BuildingOverlayParams；  API声明：totalHeight: number;  差异内容：totalHeight: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：BuildingOverlayParams；  API声明：floorBottomHeight: number;  差异内容：floorBottomHeight: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：BuildingOverlayParams；  API声明：topFaceColor?: number;  差异内容：topFaceColor?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：BuildingOverlayParams；  API声明：sideFaceColor?: number;  差异内容：sideFaceColor?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：BuildingOverlayParams；  API声明：floorColor?: number;  差异内容：floorColor?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：BuildingOverlayParams；  API声明：showLevel?: number;  差异内容：showLevel?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：BuildingOverlayParams；  API声明：animationDuration?: number;  差异内容：animationDuration?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：BuildingOverlayParams；  API声明：sideTexture?: BuildingTexture;  差异内容：sideTexture?: BuildingTexture; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：BuildingOverlayParams；  API声明：floorTexture?: BuildingTexture;  差异内容：floorTexture?: BuildingTexture; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明： interface BuildingTexture  差异内容： interface BuildingTexture | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：BuildingTexture；  API声明：image: ResourceStr | image.PixelMap;  差异内容：image: ResourceStr | image.PixelMap; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：BuildingTexture；  API声明：width?: number;  差异内容：width?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：BuildingTexture；  API声明：height?: number;  差异内容：height?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明： interface TraceOverlayParams  差异内容： interface TraceOverlayParams | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TraceOverlayParams；  API声明：points: Array<LatLng>;  差异内容：points: Array<LatLng>; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TraceOverlayParams；  API声明：width?: number;  差异内容：width?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TraceOverlayParams；  API声明：color?: number;  差异内容：color?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TraceOverlayParams；  API声明：isMapMoving?: boolean;  差异内容：isMapMoving?: boolean; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TraceOverlayParams；  API声明：animationDuration?: number;  差异内容：animationDuration?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TraceOverlayParams；  API声明：animationCallback?: Callback<number>;  差异内容：animationCallback?: Callback<number>; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明： enum TextPosition  差异内容： enum TextPosition | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TextPosition；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TextPosition；  API声明：TOP = 1  差异内容：TOP = 1 | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TextPosition；  API声明：BOTTOM = 2  差异内容：BOTTOM = 2 | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TextPosition；  API声明：LEFT = 3  差异内容：LEFT = 3 | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TextPosition；  API声明：RIGHT = 4  差异内容：RIGHT = 4 | api/@hms.core.map.mapCommon.d.ts |
