---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkboostkit-b031
title: Network Boost Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Network Boost Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:42+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:fd45318185be917cd9901c32192a7f78682612b805311192a238071b0ae7f6c0
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace netQuality  差异内容： declare namespace netQuality | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明：function on(type: 'netQosChange', callback: Callback<Array<NetworkQos>>): void;  差异内容：function on(type: 'netQosChange', callback: Callback<Array<NetworkQos>>): void; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明：function off(type: 'netQosChange', callback?: Callback<Array<NetworkQos>>): void;  差异内容：function off(type: 'netQosChange', callback?: Callback<Array<NetworkQos>>): void; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明：function on(type: 'netSceneChange', callback: Callback<Array<NetworkScene>>): void;  差异内容：function on(type: 'netSceneChange', callback: Callback<Array<NetworkScene>>): void; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明：function off(type: 'netSceneChange', callback?: Callback<Array<NetworkScene>>): void;  差异内容：function off(type: 'netSceneChange', callback?: Callback<Array<NetworkScene>>): void; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明：function reportQoe(appQoe: AppQoe): void;  差异内容：function reportQoe(appQoe: AppQoe): void; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明： interface NetworkQos  差异内容： interface NetworkQos | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：NetworkQos；  API声明：pathType: PathType;  差异内容：pathType: PathType; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：NetworkQos；  API声明：linkUpBandwidth: RateBps;  差异内容：linkUpBandwidth: RateBps; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：NetworkQos；  API声明：linkDownBandwidth: RateBps;  差异内容：linkDownBandwidth: RateBps; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：NetworkQos；  API声明：linkUpRate: RateBps;  差异内容：linkUpRate: RateBps; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：NetworkQos；  API声明：linkDownRate: RateBps;  差异内容：linkDownRate: RateBps; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：NetworkQos；  API声明：rttMs: number;  差异内容：rttMs: number; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：NetworkQos；  API声明：linkUpBufferDelayMs: number;  差异内容：linkUpBufferDelayMs: number; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：NetworkQos；  API声明：linkUpBufferCongestionPercent?: number;  差异内容：linkUpBufferCongestionPercent?: number; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明： interface NetworkScene  差异内容： interface NetworkScene | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：NetworkScene；  API声明：pathType: PathType;  差异内容：pathType: PathType; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：NetworkScene；  API声明：scene: Scene;  差异内容：scene: Scene; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：NetworkScene；  API声明：recommendedAction: RecommendedAction;  差异内容：recommendedAction: RecommendedAction; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：NetworkScene；  API声明：weakSignalPrediction?: WeakSignalPrediction;  差异内容：weakSignalPrediction?: WeakSignalPrediction; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明： interface WeakSignalPrediction  差异内容： interface WeakSignalPrediction | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：WeakSignalPrediction；  API声明：isLastPredictionValid: boolean;  差异内容：isLastPredictionValid: boolean; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：WeakSignalPrediction；  API声明：startTime: number;  差异内容：startTime: number; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：WeakSignalPrediction；  API声明：duration: number;  差异内容：duration: number; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明： interface AppQoe  差异内容： interface AppQoe | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：AppQoe；  API声明：serviceType: ServiceType;  差异内容：serviceType: ServiceType; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：AppQoe；  API声明：qoeType: QoeType;  差异内容：qoeType: QoeType; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明：type RateBps = number;  差异内容：type RateBps = number; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明：const BPS = 1;  差异内容：const BPS = 1; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明：const KBPS = 1000;  差异内容：const KBPS = 1000; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明：const MBPS = 1000000;  差异内容：const MBPS = 1000000; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明：const GBPS = 1000000000;  差异内容：const GBPS = 1000000000; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明：const TBPS = 1000000000000;  差异内容：const TBPS = 1000000000000; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明：type Scene = 'normal' | 'congestion' | 'frequentHandover' | 'weakSignal';  差异内容：type Scene = 'normal' | 'congestion' | 'frequentHandover' | 'weakSignal'; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明：export type DataSpeedSimpleAction = 'suspendData' | 'decreaseData' | 'increaseData' | 'keepData';  差异内容：export type DataSpeedSimpleAction = 'suspendData' | 'decreaseData' | 'increaseData' | 'keepData'; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明：type RecommendedAction = 'doCaching' | DataSpeedSimpleAction;  差异内容：type RecommendedAction = 'doCaching' | DataSpeedSimpleAction; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明：type ServiceType = 'default' | 'background' | 'realtimeVoice' | 'realtimeVideo' | 'callSignaling' | 'realtimeGame' | 'normalGame' | 'shortVideo' | 'longVideo' | 'livestreamingAnchor' | 'livestreamingWatcher' | 'download' | 'upload' | 'browser';  差异内容：type ServiceType = 'default' | 'background' | 'realtimeVoice' | 'realtimeVideo' | 'callSignaling' | 'realtimeGame' | 'normalGame' | 'shortVideo' | 'longVideo' | 'livestreamingAnchor' | 'livestreamingWatcher' | 'download' | 'upload' | 'browser'; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明：type BadQoeCause = 'unknown' | 'serverErr' | 'noData' | 'packetLost' | 'packetOutOfOrder' | 'highJitter' | 'highLatency';  差异内容：type BadQoeCause = 'unknown' | 'serverErr' | 'noData' | 'packetLost' | 'packetOutOfOrder' | 'highJitter' | 'highLatency'; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明：type QoeType = 'good' | BadQoeCause;  差异内容：type QoeType = 'good' | BadQoeCause; | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：netQuality；  API声明： enum PathType  差异内容： enum PathType | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：PathType；  API声明：CELLULAR\_PRIMARY = 0  差异内容：CELLULAR\_PRIMARY = 0 | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：PathType；  API声明：CELLULAR\_SECONDARY = 1  差异内容：CELLULAR\_SECONDARY = 1 | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：PathType；  API声明：WIFI\_PRIMARY = 2  差异内容：WIFI\_PRIMARY = 2 | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：PathType；  API声明：WIFI\_SECONDARY = 3  差异内容：WIFI\_SECONDARY = 3 | api/@hms.networkboost.netquality.d.ts |
