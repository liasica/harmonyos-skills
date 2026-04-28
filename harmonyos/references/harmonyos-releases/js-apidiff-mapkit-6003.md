---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mapkit-6003
title: Map Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Map Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:19+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:82690df193e93a412c07d82bc1cce51c0276a64d6e00fb8ed6344182c9f95899
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：MapComponentController；  API声明：addMarker(options: mapCommon.MarkerOptions): Promise<Marker>;  差异内容：NA | 类名：MapComponentController；  API声明：addMarker(options: mapCommon.MarkerOptions): Promise<Marker>;  差异内容：1002601005 | api/@hms.core.map.map.d.ts |
| 删除错误码 | 类名：MapComponentController；  API声明：addTileOverlay(params: mapCommon.TileOverlayParams): TileOverlay;  差异内容：401 | 类名：MapComponentController；  API声明：addTileOverlay(params: mapCommon.TileOverlayParams | mapCommon.TileOverlayOptions): TileOverlay;  差异内容：NA | api/@hms.core.map.map.d.ts |
| 函数变更 | 类名：MapComponentController；  API声明：addTileOverlay(params: mapCommon.TileOverlayParams): TileOverlay;  差异内容：params: mapCommon.TileOverlayParams | 类名：MapComponentController；  API声明：addTileOverlay(params: mapCommon.TileOverlayParams | mapCommon.TileOverlayOptions): TileOverlay;  差异内容：params: mapCommon.TileOverlayParams | mapCommon.TileOverlayOptions | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：map；  API声明：interface Heatmap  差异内容：interface Heatmap | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Heatmap；  API声明：setData(data: mapCommon.WeightedLatLng[]): void;  差异内容：setData(data: mapCommon.WeightedLatLng[]): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Heatmap；  API声明：getData(): mapCommon.WeightedLatLng[];  差异内容：getData(): mapCommon.WeightedLatLng[]; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Heatmap；  API声明：setColor(color: Record<number, number>): void;  差异内容：setColor(color: Record<number, number>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Heatmap；  API声明：getColor(): Record<number, number>;  差异内容：getColor(): Record<number, number>; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Heatmap；  API声明：setIntensity(intensity: number | Record<number, number>): void;  差异内容：setIntensity(intensity: number | Record<number, number>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Heatmap；  API声明：getIntensity(): number | Record<number, number>;  差异内容：getIntensity(): number | Record<number, number>; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Heatmap；  API声明：setOpacity(opacity: number | Record<number, number>): void;  差异内容：setOpacity(opacity: number | Record<number, number>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Heatmap；  API声明：getOpacity(): number | Record<number, number>;  差异内容：getOpacity(): number | Record<number, number>; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Heatmap；  API声明：setRadius(radius: number | Record<number, number>): void;  差异内容：setRadius(radius: number | Record<number, number>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Heatmap；  API声明：getRadius(): number | Record<number, number>;  差异内容：getRadius(): number | Record<number, number>; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Heatmap；  API声明：setRadiusUnit(radiusUnit: mapCommon.RadiusUnit): void;  差异内容：setRadiusUnit(radiusUnit: mapCommon.RadiusUnit): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Heatmap；  API声明：getRadiusUnit(): mapCommon.RadiusUnit;  差异内容：getRadiusUnit(): mapCommon.RadiusUnit; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Heatmap；  API声明：setVisible(visible: boolean): void;  差异内容：setVisible(visible: boolean): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Heatmap；  API声明：isVisible(): boolean;  差异内容：isVisible(): boolean; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Heatmap；  API声明：remove(): void;  差异内容：remove(): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：map；  API声明：interface MvtOverlay  差异内容：interface MvtOverlay | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MvtOverlay；  API声明：addLayers(layers: mapCommon.MvtLayer[]): void;  差异内容：addLayers(layers: mapCommon.MvtLayer[]): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MvtOverlay；  API声明：removeLayers(layerIds: string[]): void;  差异内容：removeLayers(layerIds: string[]): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MvtOverlay；  API声明：changeLayers(addedLayers: mapCommon.MvtLayer[], removedLayerIds: string[]): void;  差异内容：changeLayers(addedLayers: mapCommon.MvtLayer[], removedLayerIds: string[]): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：map；  API声明：interface FlowFieldOverlay  差异内容：interface FlowFieldOverlay | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：FlowFieldOverlay；  API声明：setStyle(style: mapCommon.ParticleStyle): void;  差异内容：setStyle(style: mapCommon.ParticleStyle): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：FlowFieldOverlay；  API声明：getStyle(): mapCommon.ParticleStyle;  差异内容：getStyle(): mapCommon.ParticleStyle; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：map；  API声明：interface MassPointOverlay  差异内容：interface MassPointOverlay | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MassPointOverlay；  API声明：getId(): string;  差异内容：getId(): string; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MassPointOverlay；  API声明：setItems(items: mapCommon.MassPointItem[]): void;  差异内容：setItems(items: mapCommon.MassPointItem[]): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MassPointOverlay；  API声明：getItems(): mapCommon.MassPointItem[];  差异内容：getItems(): mapCommon.MassPointItem[]; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MassPointOverlay；  API声明：setAnchorU(anchorU: number): void;  差异内容：setAnchorU(anchorU: number): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MassPointOverlay；  API声明：getAnchorU(): number;  差异内容：getAnchorU(): number; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MassPointOverlay；  API声明：setAnchorV(anchorV: number): void;  差异内容：setAnchorV(anchorV: number): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MassPointOverlay；  API声明：getAnchorV(): number;  差异内容：getAnchorV(): number; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MassPointOverlay；  API声明：setVisible(visible: boolean): void;  差异内容：setVisible(visible: boolean): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MassPointOverlay；  API声明：isVisible(): boolean;  差异内容：isVisible(): boolean; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MassPointOverlay；  API声明：remove(): void;  差异内容：remove(): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：map；  API声明：type MassPointOverlayCallback = (massPointOverlay: MassPointOverlay, massPointItem: mapCommon.MassPointItem) => void;  差异内容：type MassPointOverlayCallback = (massPointOverlay: MassPointOverlay, massPointItem: mapCommon.MassPointItem) => void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MyLocationDisplayType；  API声明：TRACK\_ROTATE = 4  差异内容：TRACK\_ROTATE = 4 | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明：interface TileOverlayOptions  差异内容：interface TileOverlayOptions | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TileOverlayOptions；  API声明：tileUrl?: string;  差异内容：tileUrl?: string; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TileOverlayOptions；  API声明：tileProvider?: TileProvider;  差异内容：tileProvider?: TileProvider; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TileOverlayOptions；  API声明：transparency?: number;  差异内容：transparency?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TileOverlayOptions；  API声明：fadeIn?: boolean;  差异内容：fadeIn?: boolean; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TileOverlayOptions；  API声明：diskCacheEnabled?: boolean;  差异内容：diskCacheEnabled?: boolean; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TileOverlayOptions；  API声明：diskCacheSize?: number;  差异内容：diskCacheSize?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TileOverlayOptions；  API声明：diskCachePath?: string;  差异内容：diskCachePath?: string; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明：interface HeatmapParams  差异内容：interface HeatmapParams | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：HeatmapParams；  API声明：id: string;  差异内容：id: string; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：HeatmapParams；  API声明：data: WeightedLatLng[];  差异内容：data: WeightedLatLng[]; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：HeatmapParams；  API声明：color?: Record<number, number>;  差异内容：color?: Record<number, number>; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：HeatmapParams；  API声明：intensity?: number | Record<number, number>;  差异内容：intensity?: number | Record<number, number>; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：HeatmapParams；  API声明：opacity?: number | Record<number, number>;  差异内容：opacity?: number | Record<number, number>; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：HeatmapParams；  API声明：radius?: number | Record<number, number>;  差异内容：radius?: number | Record<number, number>; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：HeatmapParams；  API声明：radiusUnit?: RadiusUnit;  差异内容：radiusUnit?: RadiusUnit; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：HeatmapParams；  API声明：visible?: boolean;  差异内容：visible?: boolean; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明：enum RadiusUnit  差异内容：enum RadiusUnit | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：RadiusUnit；  API声明：PIXEL\_UNIT = 0  差异内容：PIXEL\_UNIT = 0 | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：RadiusUnit；  API声明：METER\_UNIT = 1  差异内容：METER\_UNIT = 1 | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明：interface WeightedLatLng  差异内容：interface WeightedLatLng | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：WeightedLatLng；  API声明：point: LatLng;  差异内容：point: LatLng; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：WeightedLatLng；  API声明：intensity?: number;  差异内容：intensity?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明：type TileProvider = (x: number, y: number, z: number) => Promise<ArrayBuffer>;  差异内容：type TileProvider = (x: number, y: number, z: number) => Promise<ArrayBuffer>; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明：interface MvtOverlayParams  差异内容：interface MvtOverlayParams | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MvtOverlayParams；  API声明：source: MvtSource;  差异内容：source: MvtSource; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MvtOverlayParams；  API声明：layers: MvtLayer[];  差异内容：layers: MvtLayer[]; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明：interface MvtSource  差异内容：interface MvtSource | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MvtSource；  API声明：tileUrl?: string;  差异内容：tileUrl?: string; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MvtSource；  API声明：tileProvider?: TileProvider;  差异内容：tileProvider?: TileProvider; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MvtSource；  API声明：minZoom?: number;  差异内容：minZoom?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MvtSource；  API声明：maxZoom?: number;  差异内容：maxZoom?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明：interface MvtLayer  差异内容：interface MvtLayer | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MvtLayer；  API声明：id: string;  差异内容：id: string; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MvtLayer；  API声明：type: MvtLayerType;  差异内容：type: MvtLayerType; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MvtLayer；  API声明：sourceLayer: string;  差异内容：sourceLayer: string; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MvtLayer；  API声明：paint?: MvtPaint;  差异内容：paint?: MvtPaint; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明：interface MvtPaint  差异内容：interface MvtPaint | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MvtPaint；  API声明：fillColor?: number | Expression;  差异内容：fillColor?: number | Expression; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MvtPaint；  API声明：fillOpacity?: number | Expression;  差异内容：fillOpacity?: number | Expression; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明：enum MvtLayerType  差异内容：enum MvtLayerType | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MvtLayerType；  API声明：FILL = 'fill'  差异内容：FILL = 'fill' | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明：interface Expression  差异内容：interface Expression | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：Expression；  API声明：operator: Operator;  差异内容：operator: Operator; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：Expression；  API声明：args: string | string[] | Expression[];  差异内容：args: string | string[] | Expression[]; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明：enum Operator  差异内容：enum Operator | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：Operator；  API声明：GET = 'get'  差异内容：GET = 'get' | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明：interface FlowFieldOverlayParams  差异内容：interface FlowFieldOverlayParams | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：FlowFieldOverlayParams；  API声明：data: string;  差异内容：data: string; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：FlowFieldOverlayParams；  API声明：style?: ParticleStyle;  差异内容：style?: ParticleStyle; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明：interface ParticleStyle  差异内容：interface ParticleStyle | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：ParticleStyle；  API声明：count?: number;  差异内容：count?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：ParticleStyle；  API声明：color?: number;  差异内容：color?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：ParticleStyle；  API声明：maxSpeed?: number;  差异内容：maxSpeed?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：ParticleStyle；  API声明：speedFactor?: number;  差异内容：speedFactor?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明：interface MassPointItem  差异内容：interface MassPointItem | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MassPointItem；  API声明：itemId: string;  差异内容：itemId: string; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MassPointItem；  API声明：position: LatLng;  差异内容：position: LatLng; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MassPointItem；  API声明：title?: string;  差异内容：title?: string; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MassPointItem；  API声明：snippet?: string;  差异内容：snippet?: string; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon；  API声明：interface MassPointOverlayParams  差异内容：interface MassPointOverlayParams | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MassPointOverlayParams；  API声明：id: string;  差异内容：id: string; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MassPointOverlayParams；  API声明：items: MassPointItem[];  差异内容：items: MassPointItem[]; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MassPointOverlayParams；  API声明：icon: ResourceStr | image.PixelMap;  差异内容：icon: ResourceStr | image.PixelMap; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MassPointOverlayParams；  API声明：anchorU?: number;  差异内容：anchorU?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MassPointOverlayParams；  API声明：anchorV?: number;  差异内容：anchorV?: number; | api/@hms.core.map.mapCommon.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：MapComponentController；  API声明：addHeatmap(params: mapCommon.HeatmapParams): Promise<Heatmap>;  差异内容：addHeatmap(params: mapCommon.HeatmapParams): Promise<Heatmap>; | api/@hms.core.map.map.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：MapComponentController；  API声明：addMvtOverlay(params: mapCommon.MvtOverlayParams): MvtOverlay;  差异内容：addMvtOverlay(params: mapCommon.MvtOverlayParams): MvtOverlay; | api/@hms.core.map.map.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：MapComponentController；  API声明：setFramePerSecond(fps: number): void;  差异内容：setFramePerSecond(fps: number): void; | api/@hms.core.map.map.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：MapComponentController；  API声明：addFlowFieldOverlay(params: mapCommon.FlowFieldOverlayParams): Promise<FlowFieldOverlay>;  差异内容：addFlowFieldOverlay(params: mapCommon.FlowFieldOverlayParams): Promise<FlowFieldOverlay>; | api/@hms.core.map.map.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：MapComponentController；  API声明：addMassPointOverlay(params: mapCommon.MassPointOverlayParams): Promise<MassPointOverlay>;  差异内容：addMassPointOverlay(params: mapCommon.MassPointOverlayParams): Promise<MassPointOverlay>; | api/@hms.core.map.map.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：MapComponentController；  API声明：setLanguage(language: string): void;  差异内容：setLanguage(language: string): void; | api/@hms.core.map.map.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：MapComponentController；  API声明：getLanguage(): string;  差异内容：getLanguage(): string; | api/@hms.core.map.map.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：MapComponentController；  API声明：setSphereEnabled(enabled: boolean): void;  差异内容：setSphereEnabled(enabled: boolean): void; | 类名：MapComponentController；  API声明：setSphereEnabled(enabled: boolean, animateDuration: number): void;  差异内容：setSphereEnabled(enabled: boolean, animateDuration: number): void; | api/@hms.core.map.map.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Marker；  API声明：setIconBuilder(iconBuilder: CustomBuilder): Promise<void>;  差异内容：setIconBuilder(iconBuilder: CustomBuilder): Promise<void>; | api/@hms.core.map.map.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：MapEventManager；  API声明：on(type: 'massPointOverlayClick', callback: MassPointOverlayCallback): void;  差异内容：on(type: 'massPointOverlayClick', callback: MassPointOverlayCallback): void; | api/@hms.core.map.map.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：MapEventManager；  API声明：off(type: 'massPointOverlayClick', callback?: MassPointOverlayCallback): void;  差异内容：off(type: 'massPointOverlayClick', callback?: MassPointOverlayCallback): void; | api/@hms.core.map.map.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：TileOverlay；  API声明：clearDiskCache(): Promise<void>;  差异内容：clearDiskCache(): Promise<void>; | api/@hms.core.map.map.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：MapOptions；  API声明：language?: string;  差异内容：language?: string; | api/@hms.core.map.mapCommon.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：MarkerOptions；  API声明：iconBuilder?: CustomBuilder;  差异内容：iconBuilder?: CustomBuilder; | api/@hms.core.map.mapCommon.d.ts |
