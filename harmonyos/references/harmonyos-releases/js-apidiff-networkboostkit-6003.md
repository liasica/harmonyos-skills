---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkboostkit-6003
title: Network Boost Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Network Boost Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:20+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:6f88916f8460dbf956c9da97d65a88ade8721e4ea834e51f39324951e3065bce
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 自定义类型变更 | 类名：netQuality；  API声明：type ServiceType = 'default' | 'background' | 'realtimeVoice' | 'realtimeVideo' | 'callSignaling' | 'realtimeGame' | 'normalGame' | 'shortVideo' | 'longVideo' | 'livestreamingAnchor' | 'livestreamingWatcher' | 'download' | 'upload' | 'browser';  差异内容：'default' | 'background' | 'realtimeVoice' | 'realtimeVideo' | 'callSignaling' | 'realtimeGame' | 'normalGame' | 'shortVideo' | 'longVideo' | 'livestreamingAnchor' | 'livestreamingWatcher' | 'download' | 'upload' | 'browser' | 类名：netQuality；  API声明：type ServiceType = 'default' | 'background' | 'realtimeVoice' | 'realtimeVideo' | 'callSignaling' | 'realtimeGame' | 'normalGame' | 'shortVideo' | 'longVideo' | 'livestreamingAnchor' | 'livestreamingWatcher' | 'download' | 'upload' | 'browser' | 'transaction' | 'shopping' | 'detection' | 'cloudService' | 'voiceConference' | 'videoConference' | 'audio' | 'navigation' | 'seckillService' | 'login';  差异内容：'default' | 'background' | 'realtimeVoice' | 'realtimeVideo' | 'callSignaling' | 'realtimeGame' | 'normalGame' | 'shortVideo' | 'longVideo' | 'livestreamingAnchor' | 'livestreamingWatcher' | 'download' | 'upload' | 'browser' | 'transaction' | 'shopping' | 'detection' | 'cloudService' | 'voiceConference' | 'videoConference' | 'audio' | 'navigation' | 'seckillService' | 'login' | api/@hms.networkboost.netquality.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace netBoost  差异内容：declare namespace netBoost | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：netBoost；  API声明：function setSceneDesc(sceneDesc: SceneDesc): void;  差异内容：function setSceneDesc(sceneDesc: SceneDesc): void; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：netBoost；  API声明：interface SceneDesc  差异内容：interface SceneDesc | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：SceneDesc；  API声明：scene: netQuality.ServiceType;  差异内容：scene: netQuality.ServiceType; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：SceneDesc；  API声明：sceneEvent: SceneEvent;  差异内容：sceneEvent: SceneEvent; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：SceneDesc；  API声明：startTime?: number;  差异内容：startTime?: number; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：SceneDesc；  API声明：duration?: number;  差异内容：duration?: number; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：netBoost；  API声明：enum SceneEvent  差异内容：enum SceneEvent | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：SceneEvent；  API声明：SCENE\_EVENT\_ENTER = 0  差异内容：SCENE\_EVENT\_ENTER = 0 | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：SceneEvent；  API声明：SCENE\_EVENT\_UPDATE = 1  差异内容：SCENE\_EVENT\_UPDATE = 1 | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：SceneEvent；  API声明：SCENE\_EVENT\_LEAVE = 2  差异内容：SCENE\_EVENT\_LEAVE = 2 | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：netHandover；  API声明：function getMultiPathQuotaStats(): MultiPathQuota;  差异内容：function getMultiPathQuotaStats(): MultiPathQuota; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover；  API声明：function requestMultiPath(callback: Callback<MultiPathRequestResult>): void;  差异内容：function requestMultiPath(callback: Callback<MultiPathRequestResult>): void; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover；  API声明：function releaseMultiPath(): void;  差异内容：function releaseMultiPath(): void; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover；  API声明：function on(type: 'multiPathStateChange', callback: Callback<MultiPathStateInfo>): void;  差异内容：function on(type: 'multiPathStateChange', callback: Callback<MultiPathStateInfo>): void; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover；  API声明：function off(type: 'multiPathStateChange', callback?: Callback<MultiPathStateInfo>): void;  差异内容：function off(type: 'multiPathStateChange', callback?: Callback<MultiPathStateInfo>): void; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover；  API声明：function on(type: 'multiPathRecommendation', callback: Callback<MultiPathRecommendationInfo>): void;  差异内容：function on(type: 'multiPathRecommendation', callback: Callback<MultiPathRecommendationInfo>): void; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover；  API声明：function off(type: 'multiPathRecommendation', callback?: Callback<MultiPathRecommendationInfo>): void;  差异内容：function off(type: 'multiPathRecommendation', callback?: Callback<MultiPathRecommendationInfo>): void; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover；  API声明：interface MultiPathQuotaInfo  差异内容：interface MultiPathQuotaInfo | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathQuotaInfo；  API声明：count: number;  差异内容：count: number; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathQuotaInfo；  API声明：duration: number;  差异内容：duration: number; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover；  API声明：interface MultiPathQuota  差异内容：interface MultiPathQuota | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathQuota；  API声明：readonly used: MultiPathQuotaInfo;  差异内容：readonly used: MultiPathQuotaInfo; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathQuota；  API声明：readonly remaining: MultiPathQuotaInfo;  差异内容：readonly remaining: MultiPathQuotaInfo; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover；  API声明：interface MultiPathRecommendationInfo  差异内容：interface MultiPathRecommendationInfo | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathRecommendationInfo；  API声明：action: MultiPathAction;  差异内容：action: MultiPathAction; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover；  API声明：interface MultiPathRequestResult  差异内容：interface MultiPathRequestResult | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathRequestResult；  API声明：result: MultiPathErrorResult;  差异内容：result: MultiPathErrorResult; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover；  API声明：interface MultiPathStateInfo  差异内容：interface MultiPathStateInfo | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathStateInfo；  API声明：multiPathState: MultiPathState;  差异内容：multiPathState: MultiPathState; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathStateInfo；  API声明：cause: MultiPathChangeCause;  差异内容：cause: MultiPathChangeCause; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathStateInfo；  API声明：netHandle: connection.NetHandle;  差异内容：netHandle: connection.NetHandle; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathStateInfo；  API声明：pathState: PathState;  差异内容：pathState: PathState; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathStateInfo；  API声明：pathType: netQuality.PathType;  差异内容：pathType: netQuality.PathType; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover；  API声明：enum PathState  差异内容：enum PathState | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：PathState；  API声明：PATH\_IDLE = 0  差异内容：PATH\_IDLE = 0 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：PathState；  API声明：PATH\_CONNECTED = 1  差异内容：PATH\_CONNECTED = 1 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：PathState；  API声明：PATH\_SUSPENDED = 2  差异内容：PATH\_SUSPENDED = 2 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover；  API声明：enum MultiPathState  差异内容：enum MultiPathState | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathState；  API声明：MULTIPATH\_IDLE = 0  差异内容：MULTIPATH\_IDLE = 0 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathState；  API声明：MULTIPATH\_CREATING = 1  差异内容：MULTIPATH\_CREATING = 1 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathState；  API声明：MULTIPATH\_CREATED = 2  差异内容：MULTIPATH\_CREATED = 2 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathState；  API声明：MULTIPATH\_RELEASING = 3  差异内容：MULTIPATH\_RELEASING = 3 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover；  API声明：enum MultiPathErrorResult  差异内容：enum MultiPathErrorResult | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathErrorResult；  API声明：MULTIPATH\_ERROR\_NONE = 0  差异内容：MULTIPATH\_ERROR\_NONE = 0 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathErrorResult；  API声明：MULTIPATH\_ERROR\_NETWORK\_REFUSED = 1  差异内容：MULTIPATH\_ERROR\_NETWORK\_REFUSED = 1 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathErrorResult；  API声明：MULTIPATH\_ERROR\_TIMEOUT = 2  差异内容：MULTIPATH\_ERROR\_TIMEOUT = 2 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathErrorResult；  API声明：MULTIPATH\_ERROR\_LOCAL = 3  差异内容：MULTIPATH\_ERROR\_LOCAL = 3 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover；  API声明：enum MultiPathChangeCause  差异内容：enum MultiPathChangeCause | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathChangeCause；  API声明：MULTIPATH\_CHANGE\_CAUSE\_REQUEST\_NORMAL = 0  差异内容：MULTIPATH\_CHANGE\_CAUSE\_REQUEST\_NORMAL = 0 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathChangeCause；  API声明：MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_NORMAL = 50  差异内容：MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_NORMAL = 50 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathChangeCause；  API声明：MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_NETWORK = 51  差异内容：MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_NETWORK = 51 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathChangeCause；  API声明：MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_USER\_REFUSED = 52  差异内容：MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_USER\_REFUSED = 52 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathChangeCause；  API声明：MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_NO\_QUOTA = 53  差异内容：MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_NO\_QUOTA = 53 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathChangeCause；  API声明：MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_POWER\_CONSUMPTION = 54  差异内容：MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_POWER\_CONSUMPTION = 54 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathChangeCause；  API声明：MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_INSUFFICIENT\_TRAFFIC = 55  差异内容：MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_INSUFFICIENT\_TRAFFIC = 55 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathChangeCause；  API声明：MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_CONFLICT = 56  差异内容：MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_CONFLICT = 56 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathChangeCause；  API声明：MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_SYS\_FUSING = 57  差异内容：MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_SYS\_FUSING = 57 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathChangeCause；  API声明：MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_SYS\_DEFAULT = 99  差异内容：MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_SYS\_DEFAULT = 99 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathChangeCause；  API声明：MULTIPATH\_CHANGE\_CAUSE\_SUSPEND\_ENTER = 100  差异内容：MULTIPATH\_CHANGE\_CAUSE\_SUSPEND\_ENTER = 100 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathChangeCause；  API声明：MULTIPATH\_CHANGE\_CAUSE\_SUSPEND\_LEAVE = 101  差异内容：MULTIPATH\_CHANGE\_CAUSE\_SUSPEND\_LEAVE = 101 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathChangeCause；  API声明：MULTIPATH\_CHANGE\_CAUSE\_CONN\_PROPERTIES\_UPDATE = 102  差异内容：MULTIPATH\_CHANGE\_CAUSE\_CONN\_PROPERTIES\_UPDATE = 102 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover；  API声明：enum MultiPathAction  差异内容：enum MultiPathAction | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathAction；  API声明：MULTIPATH\_ACTION\_REQUEST = 0  差异内容：MULTIPATH\_ACTION\_REQUEST = 0 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：MultiPathAction；  API声明：MULTIPATH\_ACTION\_RELEASE = 1  差异内容：MULTIPATH\_ACTION\_RELEASE = 1 | api/@hms.networkboost.handover.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.networkboost.netBoost.d.ts  差异内容：NetworkBoostKit | api/@hms.networkboost.netBoost.d.ts |
