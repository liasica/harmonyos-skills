---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-healthservicekit-510
title: Health Service Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Health Service Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:09+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:4eb1c66a8f6786db065643e7b641458d01be40bea323649fccc48481cf1a2689
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：healthStore；  API声明：function syncAll(): Promise<void>;  差异内容：function syncAll(): Promise<void>; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthStore；  API声明：function on(type: 'serviceDie', callback: Callback<void>): void;  差异内容：function on(type: 'serviceDie', callback: Callback<void>): void; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthStore；  API声明：function off(type: 'serviceDie', callback?: Callback<void>): void;  差异内容：function off(type: 'serviceDie', callback?: Callback<void>): void; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthDataTypes；  API声明：const HEART\_RATE\_VARIABILITY: healthStore.DataType;  差异内容：const HEART\_RATE\_VARIABILITY: healthStore.DataType; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthDataTypes；  API声明：const EMOTION: healthStore.DataType;  差异内容：const EMOTION: healthStore.DataType; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthFields；  API声明：type HeartRateVariability = {  /\*\*  \* heart rate variability, value must be (0, 200].  \*  \* @type { number }  \* @syscap SystemCapability.Health.HealthStore  \* @since 5.1.0(18)  \*/  heartRateVariabilityRMSSD: number;  };  差异内容：type HeartRateVariability = {  /\*\*  \* heart rate variability, value must be (0, 200].  \*  \* @type { number }  \* @syscap SystemCapability.Health.HealthStore  \* @since 5.1.0(18)  \*/  heartRateVariabilityRMSSD: number;  }; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthFields；  API声明：type Emotion = {  /\*\*  \* current emotional state, value must be [0, 100).  \*  \* @type { number }  \* @syscap SystemCapability.Health.HealthStore  \* @since 5.1.0(18)  \*/  emotionStatus: number;  };  差异内容：type Emotion = {  /\*\*  \* current emotional state, value must be [0, 100).  \*  \* @type { number }  \* @syscap SystemCapability.Health.HealthStore  \* @since 5.1.0(18)  \*/  emotionStatus: number;  }; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthModels；  API声明：type HeartRateVariability = healthStore.SamplePoint<healthFields.HeartRateVariability>;  差异内容：type HeartRateVariability = healthStore.SamplePoint<healthFields.HeartRateVariability>; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthModels；  API声明：type Emotion = healthStore.SamplePoint<healthFields.Emotion>;  差异内容：type Emotion = healthStore.SamplePoint<healthFields.Emotion>; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：samplePointHelper；  API声明：namespace heartRateVariability  差异内容：namespace heartRateVariability | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：heartRateVariability；  API声明：const DATA\_TYPE: healthStore.DataType;  差异内容：const DATA\_TYPE: healthStore.DataType; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：heartRateVariability；  API声明：type Model = healthModels.HeartRateVariability;  差异内容：type Model = healthModels.HeartRateVariability; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：heartRateVariability；  API声明：type Fields = healthFields.HeartRateVariability;  差异内容：type Fields = healthFields.HeartRateVariability; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：samplePointHelper；  API声明：namespace emotion  差异内容：namespace emotion | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：emotion；  API声明：const DATA\_TYPE: healthStore.DataType;  差异内容：const DATA\_TYPE: healthStore.DataType; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：emotion；  API声明：type Model = healthModels.Emotion;  差异内容：type Model = healthModels.Emotion; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：emotion；  API声明：type Fields = healthFields.Emotion;  差异内容：type Fields = healthFields.Emotion; | api/@hms.health.store.d.ts |
| 新增API | NA | 类名：healthService；  API声明：interface SampleEvent  差异内容：interface SampleEvent | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：SampleEvent；  API声明：eventId: number;  差异内容：eventId: number; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：SampleEvent；  API声明：eventLevel: number;  差异内容：eventLevel: number; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：SampleEvent；  API声明：eventData: string;  差异内容：eventData: string; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：SampleEvent；  API声明：srcPkgName?: string;  差异内容：srcPkgName?: string; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：SampleEvent；  API声明：destPkgName?: string;  差异内容：destPkgName?: string; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：healthService；  API声明：interface SampleReal  差异内容：interface SampleReal | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：SampleReal；  API声明：dataType: healthStore.DataType;  差异内容：dataType: healthStore.DataType; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：SampleReal；  API声明：time: number;  差异内容：time: number; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：SampleReal；  API声明：fields: Pick<K, keyof K>;  差异内容：fields: Pick<K, keyof K>; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：SampleReal；  API声明：deviceUniqueId?: string;  差异内容：deviceUniqueId?: string; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：type ConfigType = number | string | boolean;  差异内容：type ConfigType = number | string | boolean; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：interface WorkoutConfig  差异内容：interface WorkoutConfig | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：WorkoutConfig；  API声明：linkageType: LinkageType;  差异内容：linkageType: LinkageType; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：WorkoutConfig；  API声明：sportType: number;  差异内容：sportType: number; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：WorkoutConfig；  API声明：activityGoals?: Goal[];  差异内容：activityGoals?: Goal[]; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：WorkoutConfig；  API声明：extensionConfig?: Record<string, ConfigType>;  差异内容：extensionConfig?: Record<string, ConfigType>; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：interface Goal  差异内容：interface Goal | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：Goal；  API声明：type: number;  差异内容：type: number; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：Goal；  API声明：value: number;  差异内容：value: number; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：function config(workoutConfig: WorkoutConfig): Promise<void>;  差异内容：function config(workoutConfig: WorkoutConfig): Promise<void>; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：function start(): Promise<StartResult>;  差异内容：function start(): Promise<StartResult>; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：function pause(): Promise<void>;  差异内容：function pause(): Promise<void>; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：function resume(): Promise<void>;  差异内容：function resume(): Promise<void>; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：function stop(): Promise<void>;  差异内容：function stop(): Promise<void>; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：function onData(dataType: undefined, listener: Callback<SampleReal[]>): Promise<void>;  差异内容：function onData(dataType: undefined, listener: Callback<SampleReal[]>): Promise<void>; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：function onData(dataType: healthStore.DataType, listener: Callback<SampleReal[]>): Promise<void>;  差异内容：function onData(dataType: healthStore.DataType, listener: Callback<SampleReal[]>): Promise<void>; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：function offData(dataType: undefined, listener: Callback<SampleReal[]>): Promise<void>;  差异内容：function offData(dataType: undefined, listener: Callback<SampleReal[]>): Promise<void>; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：function offData(dataType: healthStore.DataType, listener: Callback<SampleReal[]>): Promise<void>;  差异内容：function offData(dataType: healthStore.DataType, listener: Callback<SampleReal[]>): Promise<void>; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：function sendData(sampleReal: SampleReal[]): Promise<void>;  差异内容：function sendData(sampleReal: SampleReal[]): Promise<void>; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：function onEvent(event: "  ", listener: Callback<SampleEvent>): Promise<void>;  差异内容：function onEvent(event: " ", listener: Callback<SampleEvent>): Promise<void>; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：function offEvent(event: "  ", listener: Callback<SampleEvent>): Promise<void>;  差异内容：function offEvent(event: " ", listener: Callback<SampleEvent>): Promise<void>; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：function sendEvent(event: SampleEvent): Promise<void>;  差异内容：function sendEvent(event: SampleEvent): Promise<void>; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：enum StartCode  差异内容：enum StartCode | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：StartCode；  API声明：SUCCESS = 0  差异内容：SUCCESS = 0 | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：StartCode；  API声明：WORKOUT\_WORKING = 1  差异内容：WORKOUT\_WORKING = 1 | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：StartCode；  API声明：NO\_SUPPORTED\_DEVICE = 2  差异内容：NO\_SUPPORTED\_DEVICE = 2 | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：StartCode；  API声明：DEVICE\_BUSY = 3  差异内容：DEVICE\_BUSY = 3 | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：interface StartResult  差异内容：interface StartResult | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：StartResult；  API声明：startCode: StartCode;  差异内容：startCode: StartCode; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：StartResult；  API声明：deviceState: DeviceState[];  差异内容：deviceState: DeviceState[]; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：interface DeviceState  差异内容：interface DeviceState | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：DeviceState；  API声明：deviceId: string;  差异内容：deviceId: string; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：DeviceState；  API声明：deviceName?: string;  差异内容：deviceName?: string; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：DeviceState；  API声明：state: number;  差异内容：state: number; | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：enum LinkageType  差异内容：enum LinkageType | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：LinkageType；  API声明：COURSE\_LINK = 0  差异内容：COURSE\_LINK = 0 | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：LinkageType；  API声明：ACTIVITY\_LINK = 1  差异内容：ACTIVITY\_LINK = 1 | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：workout；  API声明：enum TargetType  差异内容：enum TargetType | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：TargetType；  API声明：NONE = 0  差异内容：NONE = 0 | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：TargetType；  API声明：DISTANCE = 1  差异内容：DISTANCE = 1 | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：TargetType；  API声明：CALORIE = 2  差异内容：CALORIE = 2 | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：TargetType；  API声明：TIME = 3  差异内容：TIME = 3 | api/@hms.health.service.d.ts |
| 新增API | NA | 类名：TargetType；  API声明：SKIPPING\_TIMES = 4  差异内容：SKIPPING\_TIMES = 4 | api/@hms.health.service.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：AuthorizationRequest；  API声明：scopes?: string[];  差异内容：scopes?: string[]; | api/@hms.health.store.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：AuthorizationResponse；  API声明：scopes?: string[];  差异内容：scopes?: string[]; | api/@hms.health.store.d.ts |
