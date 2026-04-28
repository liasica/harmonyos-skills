---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mapkit-5111
title: Map Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > Map Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:55+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:dc3b1897d2cd77828bc9a7872cb5c2b27ffa365725ae1efad4b9bd1c43248c8f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：map；  API声明：interface IndoorMapInfo  差异内容：interface IndoorMapInfo | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：IndoorMapInfo；  API声明：buildingId: string;  差异内容：buildingId: string; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：IndoorMapInfo；  API声明：floorNames: string[];  差异内容：floorNames: string[]; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：IndoorMapInfo；  API声明：floorOrders: number[];  差异内容：floorOrders: number[]; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：IndoorMapInfo；  API声明：currentFloorName: string;  差异内容：currentFloorName: string; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：LogoAlignment；  API声明：TOP\_CENTER = 4  差异内容：TOP\_CENTER = 4 | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：LogoAlignment；  API声明：BOTTOM\_CENTER = 5  差异内容：BOTTOM\_CENTER = 5 | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明：enum ScaleUnit  差异内容：enum ScaleUnit | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：ScaleUnit；  API声明：METRIC\_UNIT = 0  差异内容：METRIC\_UNIT = 0 | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：ScaleUnit；  API声明：IMPERIAL\_UNIT = 1  差异内容：IMPERIAL\_UNIT = 1 | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TransitMode；  API声明：BUS = 'bus'  差异内容：BUS = 'bus' | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitMode；  API声明：SUBWAY = 'subway'  差异内容：SUBWAY = 'subway' | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：function getTransitRoutes(context: common.Context, params: TransitRouteParams): Promise<TransitRouteResult>;  差异内容：function getTransitRoutes(context: common.Context, params: TransitRouteParams): Promise<TransitRouteResult>; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：interface TransitRouteParams  差异内容：interface TransitRouteParams | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitRouteParams；  API声明：origin: RouteCoordinate;  差异内容：origin: RouteCoordinate; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitRouteParams；  API声明：destination: RouteCoordinate;  差异内容：destination: RouteCoordinate; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitRouteParams；  API声明：departureTime?: number;  差异内容：departureTime?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitRouteParams；  API声明：preference?: number;  差异内容：preference?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：enum TransitMode  差异内容：enum TransitMode | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：interface TransitRouteResult  差异内容：interface TransitRouteResult | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitRouteResult；  API声明：routes?: TransitRoute[];  差异内容：routes?: TransitRoute[]; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：interface TransitRoute  差异内容：interface TransitRoute | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitRoute；  API声明：id: string;  差异内容：id: string; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitRoute；  API声明：sections: TransitRouteSection[];  差异内容：sections: TransitRouteSection[]; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitRoute；  API声明：busSortInfo?: BusSortInfo;  差异内容：busSortInfo?: BusSortInfo; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：interface BusSortInfo  差异内容：interface BusSortInfo | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：BusSortInfo；  API声明：totalCost?: number;  差异内容：totalCost?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：BusSortInfo；  API声明：walkLength?: number;  差异内容：walkLength?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：BusSortInfo；  API声明：transferNum?: number;  差异内容：transferNum?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：BusSortInfo；  API声明：fee?: number;  差异内容：fee?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：BusSortInfo；  API声明：score?: number;  差异内容：score?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：BusSortInfo；  API声明：routeId?: string;  差异内容：routeId?: string; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：BusSortInfo；  API声明：currency?: string;  差异内容：currency?: string; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：BusSortInfo；  API声明：arrivalTime?: number;  差异内容：arrivalTime?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：BusSortInfo；  API声明：routeDesc?: number;  差异内容：routeDesc?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：interface TransitRouteSection  差异内容：interface TransitRouteSection | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitRouteSection；  API声明：type: string;  差异内容：type: string; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitRouteSection；  API声明：pedestrianSection?: PedestrianSection;  差异内容：pedestrianSection?: PedestrianSection; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitRouteSection；  API声明：transitSection?: TransitSection;  差异内容：transitSection?: TransitSection; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：interface PedestrianSection  差异内容：interface PedestrianSection | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：PedestrianSection；  API声明：id: string;  差异内容：id: string; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：PedestrianSection；  API声明：type: string;  差异内容：type: string; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：PedestrianSection；  API声明：arrival: PedestrianDepartureArrival;  差异内容：arrival: PedestrianDepartureArrival; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：PedestrianSection；  API声明：departure: PedestrianDepartureArrival;  差异内容：departure: PedestrianDepartureArrival; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：PedestrianSection；  API声明：language?: string;  差异内容：language?: string; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：PedestrianSection；  API声明：passthrough?: Passthrough[];  差异内容：passthrough?: Passthrough[]; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：PedestrianSection；  API声明：polyline?: mapCommon.LatLng[];  差异内容：polyline?: mapCommon.LatLng[]; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：PedestrianSection；  API声明：travelSummary?: BaseSummary;  差异内容：travelSummary?: BaseSummary; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：interface PedestrianDepartureArrival  差异内容：interface PedestrianDepartureArrival | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：PedestrianDepartureArrival；  API声明：place: Place;  差异内容：place: Place; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：PedestrianDepartureArrival；  API声明：time?: number;  差异内容：time?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：interface Passthrough  差异内容：interface Passthrough | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：Passthrough；  API声明：place: Place;  差异内容：place: Place; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：Passthrough；  API声明：offset?: number;  差异内容：offset?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：interface Place  差异内容：interface Place | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：Place；  API声明：location: mapCommon.LatLng;  差异内容：location: mapCommon.LatLng; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：Place；  API声明：type: string;  差异内容：type: string; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：Place；  API声明：name?: string;  差异内容：name?: string; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：interface BaseSummary  差异内容：interface BaseSummary | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：BaseSummary；  API声明：duration: number;  差异内容：duration: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：BaseSummary；  API声明：length: number;  差异内容：length: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：BaseSummary；  API声明：waitTime?: number;  差异内容：waitTime?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：interface TransitSection  差异内容：interface TransitSection | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitSection；  API声明：id: string;  差异内容：id: string; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitSection；  API声明：type: string;  差异内容：type: string; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitSection；  API声明：arrival: TransitArrival;  差异内容：arrival: TransitArrival; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitSection；  API声明：departure: TransitDeparture;  差异内容：departure: TransitDeparture; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitSection；  API声明：intermediateStops?: TransitStop[];  差异内容：intermediateStops?: TransitStop[]; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitSection；  API声明：language?: string;  差异内容：language?: string; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitSection；  API声明：passthrough?: Passthrough[];  差异内容：passthrough?: Passthrough[]; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitSection；  API声明：polyline?: mapCommon.LatLng[];  差异内容：polyline?: mapCommon.LatLng[]; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitSection；  API声明：transport?: TransitTransport;  差异内容：transport?: TransitTransport; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitSection；  API声明：travelSummary?: BaseSummary;  差异内容：travelSummary?: BaseSummary; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitSection；  API声明：extraTransitSection?: ExtraTransitSection[];  差异内容：extraTransitSection?: ExtraTransitSection[]; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitSection；  API声明：sectionDesc?: number;  差异内容：sectionDesc?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitSection；  API声明：firstVehicleHour?: number;  差异内容：firstVehicleHour?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitSection；  API声明：finalVehicleHour?: number;  差异内容：finalVehicleHour?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitSection；  API声明：stopOffset?: number;  差异内容：stopOffset?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：interface TransitArrival  差异内容：interface TransitArrival | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitArrival；  API声明：place: Place;  差异内容：place: Place; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitArrival；  API声明：delay?: number;  差异内容：delay?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitArrival；  API声明：time?: number;  差异内容：time?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitArrival；  API声明：exit?: TransitEntranceExit;  差异内容：exit?: TransitEntranceExit; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：interface TransitDeparture  差异内容：interface TransitDeparture | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitDeparture；  API声明：place: Place;  差异内容：place: Place; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitDeparture；  API声明：delay?: number;  差异内容：delay?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitDeparture；  API声明：time?: number;  差异内容：time?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitDeparture；  API声明：entrance?: TransitEntranceExit;  差异内容：entrance?: TransitEntranceExit; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：interface TransitEntranceExit  差异内容：interface TransitEntranceExit | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitEntranceExit；  API声明：name: string;  差异内容：name: string; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitEntranceExit；  API声明：location: mapCommon.LatLng;  差异内容：location: mapCommon.LatLng; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：interface TransitStop  差异内容：interface TransitStop | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitStop；  API声明：departure: TransitDeparture;  差异内容：departure: TransitDeparture; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitStop；  API声明：duration?: number;  差异内容：duration?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：interface TransitTransport  差异内容：interface TransitTransport | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitTransport；  API声明：mode: TransitMode;  差异内容：mode: TransitMode; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitTransport；  API声明：category?: string;  差异内容：category?: string; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitTransport；  API声明：color?: string;  差异内容：color?: string; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitTransport；  API声明：headsign?: string;  差异内容：headsign?: string; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitTransport；  API声明：name?: string;  差异内容：name?: string; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：TransitTransport；  API声明：textColor?: string;  差异内容：textColor?: string; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：navi；  API声明：interface ExtraTransitSection  差异内容：interface ExtraTransitSection | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：ExtraTransitSection；  API声明：intermediateStops: TransitStop[];  差异内容：intermediateStops: TransitStop[]; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：ExtraTransitSection；  API声明：polyline: mapCommon.LatLng[];  差异内容：polyline: mapCommon.LatLng[]; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：ExtraTransitSection；  API声明：transport: TransitTransport;  差异内容：transport: TransitTransport; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：ExtraTransitSection；  API声明：travelSummary: BaseSummary;  差异内容：travelSummary: BaseSummary; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：ExtraTransitSection；  API声明：firstVehicleHour?: number;  差异内容：firstVehicleHour?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：ExtraTransitSection；  API声明：finalVehicleHour?: number;  差异内容：finalVehicleHour?: number; | api/@hms.core.map.navi.d.ts |
| 新增API | NA | 类名：ExtraTransitSection；  API声明：stopOffset?: number;  差异内容：stopOffset?: number; | api/@hms.core.map.navi.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：MapComponentController；  API声明：setIndoorMapEnabled(enabled: boolean): void;  差异内容：setIndoorMapEnabled(enabled: boolean): void; | api/@hms.core.map.map.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：MapComponentController；  API声明：isIndoorMapEnabled(): boolean;  差异内容：isIndoorMapEnabled(): boolean; | api/@hms.core.map.map.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：MapComponentController；  API声明：switchIndoorMapFloor(buildingId: string, floorName: string): void;  差异内容：switchIndoorMapFloor(buildingId: string, floorName: string): void; | api/@hms.core.map.map.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Marker；  API声明：setAnnotationVisible(visible: boolean): void;  差异内容：setAnnotationVisible(visible: boolean): void; | api/@hms.core.map.map.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Marker；  API声明：isAnnotationVisible(): boolean;  差异内容：isAnnotationVisible(): boolean; | api/@hms.core.map.map.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：MapEventManager；  API声明：on(type: 'indoorMapEnter', callback: Callback<IndoorMapInfo>): void;  差异内容：on(type: 'indoorMapEnter', callback: Callback<IndoorMapInfo>): void; | api/@hms.core.map.map.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：MapEventManager；  API声明：off(type: 'indoorMapEnter', callback?: Callback<IndoorMapInfo>): void;  差异内容：off(type: 'indoorMapEnter', callback?: Callback<IndoorMapInfo>): void; | api/@hms.core.map.map.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：MapEventManager；  API声明：on(type: 'indoorMapExit', callback: Callback<void>): void;  差异内容：on(type: 'indoorMapExit', callback: Callback<void>): void; | api/@hms.core.map.map.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：MapEventManager；  API声明：off(type: 'indoorMapExit', callback?: Callback<void>): void;  差异内容：off(type: 'indoorMapExit', callback?: Callback<void>): void; | api/@hms.core.map.map.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：MapOptions；  API声明：scaleUnit?: ScaleUnit;  差异内容：scaleUnit?: ScaleUnit; | api/@hms.core.map.mapCommon.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：MapOptions；  API声明：indoorMapEnabled?: boolean;  差异内容：indoorMapEnabled?: boolean; | api/@hms.core.map.mapCommon.d.ts |
