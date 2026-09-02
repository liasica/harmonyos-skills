---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-penkit-7002
title: Pen Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Pen Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-08-04
content_hash: sha256:c246ad8ea9c625ea60dd98af97d1269f9eb8f6019b0fc83de4df2075b40a73fa
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：PickedColorInfo；  API声明：brightness?: number;  差异内容：brightness?: number; | api/@hms.officeservice.imageFeaturePicker.d.ts |
| 新增API | NA | 类名：imageFeaturePicker；  API声明：function pickHdrForResult(x?: number, y?: number): Promise<PickedColorInfo>;  差异内容：function pickHdrForResult(x?: number, y?: number): Promise<PickedColorInfo>; | api/@hms.officeservice.imageFeaturePicker.d.ts |
| 新增API | NA | 类名：imageFeaturePicker；  API声明：function pickHdrForResult(x?: number, y?: number, showValue?: boolean): Promise<PickedColorInfo>;  差异内容：function pickHdrForResult(x?: number, y?: number, showValue?: boolean): Promise<PickedColorInfo>; | api/@hms.officeservice.imageFeaturePicker.d.ts |
| 新增API | NA | 类名：stylusInteraction；  API声明：function isSensorSupported(): boolean;  差异内容：function isSensorSupported(): boolean; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction；  API声明：function onAccelerometer(receiver: Callback<AccelerometerEvent>): void;  差异内容：function onAccelerometer(receiver: Callback<AccelerometerEvent>): void; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction；  API声明：function offAccelerometer(receiver?: Callback<AccelerometerEvent>): void;  差异内容：function offAccelerometer(receiver?: Callback<AccelerometerEvent>): void; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction；  API声明：interface AccelerometerData  差异内容：interface AccelerometerData | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：AccelerometerData；  API声明：x: number;  差异内容：x: number; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：AccelerometerData；  API声明：y: number;  差异内容：y: number; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：AccelerometerData；  API声明：z: number;  差异内容：z: number; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction；  API声明：interface AccelerometerEvent  差异内容：interface AccelerometerEvent | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：AccelerometerEvent；  API声明：accelerometerData: AccelerometerData[];  差异内容：accelerometerData: AccelerometerData[]; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：AccelerometerEvent；  API声明：timestamp: number;  差异内容：timestamp: number; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction；  API声明：function onGyroscope(receiver: Callback<GyroscopeEvent>): void;  差异内容：function onGyroscope(receiver: Callback<GyroscopeEvent>): void; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction；  API声明：function offGyroscope(receiver?: Callback<GyroscopeEvent>): void;  差异内容：function offGyroscope(receiver?: Callback<GyroscopeEvent>): void; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction；  API声明：interface GyroscopeData  差异内容：interface GyroscopeData | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：GyroscopeData；  API声明：x: number;  差异内容：x: number; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：GyroscopeData；  API声明：y: number;  差异内容：y: number; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：GyroscopeData；  API声明：z: number;  差异内容：z: number; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction；  API声明：interface GyroscopeEvent  差异内容：interface GyroscopeEvent | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：GyroscopeEvent；  API声明：gyroscopeData: GyroscopeData[];  差异内容：gyroscopeData: GyroscopeData[]; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：GyroscopeEvent；  API声明：timestamp: number;  差异内容：timestamp: number; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction；  API声明：function onSensor(receiver: Callback<SensorEvent>): void;  差异内容：function onSensor(receiver: Callback<SensorEvent>): void; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction；  API声明：function offSensor(receiver?: Callback<SensorEvent>): void;  差异内容：function offSensor(receiver?: Callback<SensorEvent>): void; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction；  API声明：interface SensorData  差异内容：interface SensorData | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：SensorData；  API声明：accelerometerData: AccelerometerData;  差异内容：accelerometerData: AccelerometerData; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：SensorData；  API声明：gyroscopeData: GyroscopeData;  差异内容：gyroscopeData: GyroscopeData; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：stylusInteraction；  API声明：interface SensorEvent  差异内容：interface SensorEvent | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：SensorEvent；  API声明：sensorData: SensorData[];  差异内容：sensorData: SensorData[]; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：SensorEvent；  API声明：timestamp: number;  差异内容：timestamp: number; | api/@hms.officeservice.stylusInteraction.d.ts |
| 新增API | NA | 类名：global；  API声明：export class StylusFrameBoost  差异内容：export class StylusFrameBoost | api/@hms.stylus.handwrite.d.ts |
| 新增API | NA | 类名：StylusFrameBoost；  API声明：forceRefreshOneFrame(action: number): number;  差异内容：forceRefreshOneFrame(action: number): number; | api/@hms.stylus.handwrite.d.ts |
| 新增API | NA | 类名：HandwriteComponent；  API声明：hiddenTools?: HiddenConfig;  差异内容：hiddenTools?: HiddenConfig; | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export enum HiddenToolType  差异内容：export enum HiddenToolType | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：HiddenToolType；  API声明：PEN = 1  差异内容：PEN = 1 | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：HiddenToolType；  API声明：PENCIL = 3  差异内容：PENCIL = 3 | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：HiddenToolType；  API声明：MARKER = 4  差异内容：MARKER = 4 | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：HiddenToolType；  API声明：HIGHLIGHTER\_BRUSH = 5  差异内容：HIGHLIGHTER\_BRUSH = 5 | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：HiddenToolType；  API声明：MOSAIC = 7  差异内容：MOSAIC = 7 | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：HiddenToolType；  API声明：LASSO = 1048576  差异内容：LASSO = 1048576 | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：HiddenToolType；  API声明：LASER = 3145728  差异内容：LASER = 3145728 | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：HiddenToolType；  API声明：GRAPHICS\_TOOLS = 4194304  差异内容：GRAPHICS\_TOOLS = 4194304 | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface HiddenConfig  差异内容：export interface HiddenConfig | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：HiddenConfig；  API声明：hiddenOptionalTools?: HiddenToolType[];  差异内容：hiddenOptionalTools?: HiddenToolType[]; | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：HiddenConfig；  API声明：hiddenArcBox?: boolean;  差异内容：hiddenArcBox?: boolean; | api/@hms.stylus.HandwriteComponent.d.ets |
