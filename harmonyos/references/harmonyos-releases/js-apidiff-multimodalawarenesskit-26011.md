---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-multimodalawarenesskit-26011
title: Multimodal Awareness Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Multimodal Awareness Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:53+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:c2db485e3a047564b5b061a5c66dd848b0fa2069c21329b6c5cedfcce068147c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace carAwareness  差异内容：declare namespace carAwareness | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：carAwareness；  API声明：enum Capability  差异内容：enum Capability | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：Capability；  API声明：SPATIAL\_MOTION = 'SpatialMotion'  差异内容：SPATIAL\_MOTION = 'SpatialMotion' | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：Capability；  API声明：REALTIME\_WEATHER = 'RealTimeWeather'  差异内容：REALTIME\_WEATHER = 'RealTimeWeather' | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：Capability；  API声明：REFUELING = 'Refueling'  差异内容：REFUELING = 'Refueling' | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：carAwareness；  API声明：export interface SpatialMotionInfo  差异内容：export interface SpatialMotionInfo | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：SpatialMotionInfo；  API声明：timestamp: number;  差异内容：timestamp: number; | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：SpatialMotionInfo；  API声明：pointX: number;  差异内容：pointX: number; | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：SpatialMotionInfo；  API声明：pointY: number;  差异内容：pointY: number; | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：SpatialMotionInfo；  API声明：event: number;  差异内容：event: number; | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：carAwareness；  API声明：function onSpatialMotion(callback: Callback<SpatialMotionInfo>): void;  差异内容：function onSpatialMotion(callback: Callback<SpatialMotionInfo>): void; | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：carAwareness；  API声明：function offSpatialMotion(callback?: Callback<SpatialMotionInfo>): void;  差异内容：function offSpatialMotion(callback?: Callback<SpatialMotionInfo>): void; | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：carAwareness；  API声明：export interface RealTimeWeatherInfo  差异内容：export interface RealTimeWeatherInfo | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：RealTimeWeatherInfo；  API声明：timestamp: number;  差异内容：timestamp: number; | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：RealTimeWeatherInfo；  API声明：weather: number;  差异内容：weather: number; | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：carAwareness；  API声明：function onRealTimeWeather(callback: Callback<RealTimeWeatherInfo>): void;  差异内容：function onRealTimeWeather(callback: Callback<RealTimeWeatherInfo>): void; | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：carAwareness；  API声明：function offRealTimeWeather(callback?: Callback<RealTimeWeatherInfo>): void;  差异内容：function offRealTimeWeather(callback?: Callback<RealTimeWeatherInfo>): void; | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：carAwareness；  API声明：export interface RefuelingInfo  差异内容：export interface RefuelingInfo | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：RefuelingInfo；  API声明：timestamp: number;  差异内容：timestamp: number; | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：RefuelingInfo；  API声明：status: number;  差异内容：status: number; | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：carAwareness；  API声明：function onRefueling(callback: Callback<RefuelingInfo>): void;  差异内容：function onRefueling(callback: Callback<RefuelingInfo>): void; | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：carAwareness；  API声明：function offRefueling(callback?: Callback<RefuelingInfo>): void;  差异内容：function offRefueling(callback?: Callback<RefuelingInfo>): void; | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增API | NA | 类名：carAwareness；  API声明：function getAllCapabilityList(): Promise<Capability[]>;  差异内容：function getAllCapabilityList(): Promise<Capability[]>; | api/@ohos.multimodalAwareness.carAwareness.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.multimodalAwareness.carAwareness.d.ts  差异内容：MultimodalAwarenessKit | api/@ohos.multimodalAwareness.carAwareness.d.ts |
