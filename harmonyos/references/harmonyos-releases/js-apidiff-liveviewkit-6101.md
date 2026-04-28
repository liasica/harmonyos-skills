---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-liveviewkit-6101
title: Live View Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Live View Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5491a889fd5821e86942e9fc0ed40c8ce602df98d33815195196d4e2fb71bced
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：liveViewManager；  API声明：function startLiveViewByTrigger(liveView: LiveView, trigger: Trigger): Promise<LiveViewResult>;  差异内容：function startLiveViewByTrigger(liveView: LiveView, trigger: Trigger): Promise<LiveViewResult>; | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：liveViewManager；  API声明：function stopLiveViewByTrigger(liveView: LiveView, trigger: Trigger): Promise<LiveViewResult>;  差异内容：function stopLiveViewByTrigger(liveView: LiveView, trigger: Trigger): Promise<LiveViewResult>; | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：liveViewManager；  API声明：function isGeofenceTriggerEnabled(): Promise<boolean>;  差异内容：function isGeofenceTriggerEnabled(): Promise<boolean>; | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：liveViewManager；  API声明：export interface Trigger  差异内容：export interface Trigger | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：Trigger；  API声明：type: TriggerType;  差异内容：type: TriggerType; | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：Trigger；  API声明：condition: Geofence;  差异内容：condition: Geofence; | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：Trigger；  API声明：displayTime?: number;  差异内容：displayTime?: number; | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：liveViewManager；  API声明：export interface Geofence  差异内容：export interface Geofence | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：Geofence；  API声明：coordinateSystemType: CoordinateSystemType;  差异内容：coordinateSystemType: CoordinateSystemType; | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：Geofence；  API声明：longitude: number;  差异内容：longitude: number; | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：Geofence；  API声明：latitude: number;  差异内容：latitude: number; | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：Geofence；  API声明：radius: number;  差异内容：radius: number; | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：Geofence；  API声明：monitorEvent: MonitorEvent;  差异内容：monitorEvent: MonitorEvent; | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：Geofence；  API声明：delayTime?: number;  差异内容：delayTime?: number; | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：liveViewManager；  API声明：export enum TriggerType  差异内容：export enum TriggerType | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：TriggerType；  API声明：TRIGGER\_TYPE\_GEOFENCE = 1  差异内容：TRIGGER\_TYPE\_GEOFENCE = 1 | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：liveViewManager；  API声明：export enum CoordinateSystemType  差异内容：export enum CoordinateSystemType | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：CoordinateSystemType；  API声明：COORDINATE\_TYPE\_WGS84 = 1  差异内容：COORDINATE\_TYPE\_WGS84 = 1 | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：CoordinateSystemType；  API声明：COORDINATE\_TYPE\_GCJ02 = 2  差异内容：COORDINATE\_TYPE\_GCJ02 = 2 | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：liveViewManager；  API声明：export enum MonitorEvent  差异内容：export enum MonitorEvent | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：MonitorEvent；  API声明：MONITOR\_TYPE\_ENTRY = 1  差异内容：MONITOR\_TYPE\_ENTRY = 1 | api/@hms.core.liveview.liveViewManager.d.ts |
| 新增API | NA | 类名：MonitorEvent；  API声明：MONITOR\_TYPE\_LEAVE = 2  差异内容：MONITOR\_TYPE\_LEAVE = 2 | api/@hms.core.liveview.liveViewManager.d.ts |
