---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkboostkit-7001
title: Network Boost Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Network Boost Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:06+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:8ecf9f7e2a75efa006990f2dc1322620cf6030a96d7b9b1e7d028e27812a1a7d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：netBoost；  API声明：function setDataFlowDesc(dataFlowDesc: DataFlowDesc): void;  差异内容：function setDataFlowDesc(dataFlowDesc: DataFlowDesc): void; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：netBoost；  API声明：interface DataFlowDesc  差异内容：interface DataFlowDesc | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：DataFlowDesc；  API声明：dataFlowInfo: DataFlowInfo | SocketFd;  差异内容：dataFlowInfo: DataFlowInfo | SocketFd; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：DataFlowDesc；  API声明：scene: netQuality.ServiceType;  差异内容：scene: netQuality.ServiceType; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：DataFlowDesc；  API声明：sceneEvent: SceneEvent;  差异内容：sceneEvent: SceneEvent; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：DataFlowDesc；  API声明：expectations?: ExpectedDescription;  差异内容：expectations?: ExpectedDescription; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：netBoost；  API声明：type SocketFd = number;  差异内容：type SocketFd = number; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：netBoost；  API声明：interface DataFlowInfo  差异内容：interface DataFlowInfo | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：DataFlowInfo；  API声明：protocol: ProtocolType;  差异内容：protocol: ProtocolType; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：DataFlowInfo；  API声明：local: NetAddress;  差异内容：local: NetAddress; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：DataFlowInfo；  API声明：remote: NetAddress;  差异内容：remote: NetAddress; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：netBoost；  API声明：interface ExpectedDescription  差异内容：interface ExpectedDescription | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：ExpectedDescription；  API声明：uplinkBandwidth?: number;  差异内容：uplinkBandwidth?: number; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：ExpectedDescription；  API声明：downlinkBandwidth?: number;  差异内容：downlinkBandwidth?: number; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：ExpectedDescription；  API声明：latency?: number;  差异内容：latency?: number; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：ExpectedDescription；  API声明：objectSize?: number;  差异内容：objectSize?: number; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：ExpectedDescription；  API声明：priority?: PriorityLevel;  差异内容：priority?: PriorityLevel; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：ExpectedDescription；  API声明：lowPowerMode?: boolean;  差异内容：lowPowerMode?: boolean; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：netBoost；  API声明：interface NetAddress  差异内容：interface NetAddress | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：NetAddress；  API声明：address: string;  差异内容：address: string; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：NetAddress；  API声明：port: number;  差异内容：port: number; | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：netBoost；  API声明：enum ProtocolType  差异内容：enum ProtocolType | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：ProtocolType；  API声明：PROTOCOL\_UDP = 0  差异内容：PROTOCOL\_UDP = 0 | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：ProtocolType；  API声明：PROTOCOL\_TCP = 1  差异内容：PROTOCOL\_TCP = 1 | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：netBoost；  API声明：enum PriorityLevel  差异内容：enum PriorityLevel | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：PriorityLevel；  API声明：PRIO\_NORMAL = 0  差异内容：PRIO\_NORMAL = 0 | api/@hms.networkboost.netBoost.d.ts |
| 新增API | NA | 类名：PriorityLevel；  API声明：PRIO\_HIGH = 1  差异内容：PRIO\_HIGH = 1 | api/@hms.networkboost.netBoost.d.ts |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：declare namespace netHandover  差异内容：NA | 类名：global；  API声明：declare namespace netHandover  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：netHandover；  API声明：function on(type: 'handoverChange', callback: Callback<HandoverInfo>): void;  差异内容：NA | 类名：netHandover；  API声明：function on(type: 'handoverChange', callback: Callback<HandoverInfo>): void;  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：netHandover；  API声明：function off(type: 'handoverChange', callback?: Callback<HandoverInfo>): void;  差异内容：NA | 类名：netHandover；  API声明：function off(type: 'handoverChange', callback?: Callback<HandoverInfo>): void;  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：netHandover；  API声明：function setHandoverMode(mode: HandoverMode): void;  差异内容：NA | 类名：netHandover；  API声明：function setHandoverMode(mode: HandoverMode): void;  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：netHandover；  API声明：interface HandoverInfo  差异内容：NA | 类名：netHandover；  API声明：interface HandoverInfo  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：HandoverInfo；  API声明：readonly handoverStart?: HandoverStart;  差异内容：NA | 类名：HandoverInfo；  API声明：readonly handoverStart?: HandoverStart;  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：HandoverInfo；  API声明：readonly handoverComplete?: HandoverComplete;  差异内容：NA | 类名：HandoverInfo；  API声明：readonly handoverComplete?: HandoverComplete;  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：netHandover；  API声明：interface HandoverStart  差异内容：NA | 类名：netHandover；  API声明：interface HandoverStart  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：HandoverStart；  API声明：expires: number;  差异内容：NA | 类名：HandoverStart；  API声明：expires: number;  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：HandoverStart；  API声明：dataSpeedAction: DataSpeedAction;  差异内容：NA | 类名：HandoverStart；  API声明：dataSpeedAction: DataSpeedAction;  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：netHandover；  API声明：interface DataSpeedAction  差异内容：NA | 类名：netHandover；  API声明：interface DataSpeedAction  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：DataSpeedAction；  API声明：dataSpeedSimpleAction: netQuality.DataSpeedSimpleAction;  差异内容：NA | 类名：DataSpeedAction；  API声明：dataSpeedSimpleAction: netQuality.DataSpeedSimpleAction;  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：DataSpeedAction；  API声明：linkUpBandwidth: netQuality.RateBps;  差异内容：NA | 类名：DataSpeedAction；  API声明：linkUpBandwidth: netQuality.RateBps;  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：DataSpeedAction；  API声明：linkDownBandwidth: netQuality.RateBps;  差异内容：NA | 类名：DataSpeedAction；  API声明：linkDownBandwidth: netQuality.RateBps;  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：netHandover；  API声明：interface HandoverComplete  差异内容：NA | 类名：netHandover；  API声明：interface HandoverComplete  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：HandoverComplete；  API声明：result: ErrorResult;  差异内容：NA | 类名：HandoverComplete；  API声明：result: ErrorResult;  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：HandoverComplete；  API声明：handoverContinue: boolean;  差异内容：NA | 类名：HandoverComplete；  API声明：handoverContinue: boolean;  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：HandoverComplete；  API声明：oldPathLifetime: number;  差异内容：NA | 类名：HandoverComplete；  API声明：oldPathLifetime: number;  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：HandoverComplete；  API声明：oldDataSpeedAction: DataSpeedAction;  差异内容：NA | 类名：HandoverComplete；  API声明：oldDataSpeedAction: DataSpeedAction;  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：HandoverComplete；  API声明：pathTypeChanged: boolean;  差异内容：NA | 类名：HandoverComplete；  API声明：pathTypeChanged: boolean;  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：HandoverComplete；  API声明：newNetHandle?: connection.NetHandle;  差异内容：NA | 类名：HandoverComplete；  API声明：newNetHandle?: connection.NetHandle;  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：HandoverComplete；  API声明：reEstAction: ReEstAction;  差异内容：NA | 类名：HandoverComplete；  API声明：reEstAction: ReEstAction;  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：HandoverComplete；  API声明：newDataSpeedAction: DataSpeedAction;  差异内容：NA | 类名：HandoverComplete；  API声明：newDataSpeedAction: DataSpeedAction;  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：netHandover；  API声明：enum HandoverMode  差异内容：NA | 类名：netHandover；  API声明：enum HandoverMode  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：HandoverMode；  API声明：DELEGATION = 0  差异内容：NA | 类名：HandoverMode；  API声明：DELEGATION = 0  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：HandoverMode；  API声明：DISCRETION = 1  差异内容：NA | 类名：HandoverMode；  API声明：DISCRETION = 1  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：netHandover；  API声明：enum ReEstAction  差异内容：NA | 类名：netHandover；  API声明：enum ReEstAction  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：ReEstAction；  API声明：DEFAULT = 0  差异内容：NA | 类名：ReEstAction；  API声明：DEFAULT = 0  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：ReEstAction；  API声明：QUERY\_DNS = 1  差异内容：NA | 类名：ReEstAction；  API声明：QUERY\_DNS = 1  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：ReEstAction；  API声明：CHANGE\_REMOTE\_IP = 2  差异内容：NA | 类名：ReEstAction；  API声明：CHANGE\_REMOTE\_IP = 2  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：ReEstAction；  API声明：CHANGE\_IP\_VERSION = 3  差异内容：NA | 类名：ReEstAction；  API声明：CHANGE\_IP\_VERSION = 3  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：ReEstAction；  API声明：NO\_EST = 4  差异内容：NA | 类名：ReEstAction；  API声明：NO\_EST = 4  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：netHandover；  API声明：enum ErrorResult  差异内容：NA | 类名：netHandover；  API声明：enum ErrorResult  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：ErrorResult；  API声明：ERROR\_NONE = 0  差异内容：NA | 类名：ErrorResult；  API声明：ERROR\_NONE = 0  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：ErrorResult；  API声明：ERROR\_HANDOVER\_TIMEOUT = 1  差异内容：NA | 类名：ErrorResult；  API声明：ERROR\_HANDOVER\_TIMEOUT = 1  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：ErrorResult；  API声明：ERROR\_NEW\_PATH\_ACTIVATION\_FAILED = 2  差异内容：NA | 类名：ErrorResult；  API声明：ERROR\_NEW\_PATH\_ACTIVATION\_FAILED = 2  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：ErrorResult；  API声明：ERROR\_ABORT = 3  差异内容：NA | 类名：ErrorResult；  API声明：ERROR\_ABORT = 3  差异内容：atomicservice | api/@hms.networkboost.handover.d.ts |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：declare namespace netBoost  差异内容：NA | 类名：global；  API声明：declare namespace netBoost  差异内容：atomicservice | api/@hms.networkboost.netBoost.d.ts |
| API从不支持元服务到支持元服务 | 类名：netBoost；  API声明：function setSceneDesc(sceneDesc: SceneDesc): void;  差异内容：NA | 类名：netBoost；  API声明：function setSceneDesc(sceneDesc: SceneDesc): void;  差异内容：atomicservice | api/@hms.networkboost.netBoost.d.ts |
| API从不支持元服务到支持元服务 | 类名：netBoost；  API声明：interface SceneDesc  差异内容：NA | 类名：netBoost；  API声明：interface SceneDesc  差异内容：atomicservice | api/@hms.networkboost.netBoost.d.ts |
| API从不支持元服务到支持元服务 | 类名：SceneDesc；  API声明：scene: netQuality.ServiceType;  差异内容：NA | 类名：SceneDesc；  API声明：scene: netQuality.ServiceType;  差异内容：atomicservice | api/@hms.networkboost.netBoost.d.ts |
| API从不支持元服务到支持元服务 | 类名：SceneDesc；  API声明：sceneEvent: SceneEvent;  差异内容：NA | 类名：SceneDesc；  API声明：sceneEvent: SceneEvent;  差异内容：atomicservice | api/@hms.networkboost.netBoost.d.ts |
| API从不支持元服务到支持元服务 | 类名：SceneDesc；  API声明：startTime?: number;  差异内容：NA | 类名：SceneDesc；  API声明：startTime?: number;  差异内容：atomicservice | api/@hms.networkboost.netBoost.d.ts |
| API从不支持元服务到支持元服务 | 类名：SceneDesc；  API声明：duration?: number;  差异内容：NA | 类名：SceneDesc；  API声明：duration?: number;  差异内容：atomicservice | api/@hms.networkboost.netBoost.d.ts |
| API从不支持元服务到支持元服务 | 类名：netBoost；  API声明：enum SceneEvent  差异内容：NA | 类名：netBoost；  API声明：enum SceneEvent  差异内容：atomicservice | api/@hms.networkboost.netBoost.d.ts |
| API从不支持元服务到支持元服务 | 类名：SceneEvent；  API声明：SCENE\_EVENT\_ENTER = 0  差异内容：NA | 类名：SceneEvent；  API声明：SCENE\_EVENT\_ENTER = 0  差异内容：atomicservice | api/@hms.networkboost.netBoost.d.ts |
| API从不支持元服务到支持元服务 | 类名：SceneEvent；  API声明：SCENE\_EVENT\_UPDATE = 1  差异内容：NA | 类名：SceneEvent；  API声明：SCENE\_EVENT\_UPDATE = 1  差异内容：atomicservice | api/@hms.networkboost.netBoost.d.ts |
| API从不支持元服务到支持元服务 | 类名：SceneEvent；  API声明：SCENE\_EVENT\_LEAVE = 2  差异内容：NA | 类名：SceneEvent；  API声明：SCENE\_EVENT\_LEAVE = 2  差异内容：atomicservice | api/@hms.networkboost.netBoost.d.ts |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：declare namespace netQuality  差异内容：NA | 类名：global；  API声明：declare namespace netQuality  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：function on(type: 'netQosChange', callback: Callback<Array<NetworkQos>>): void;  差异内容：NA | 类名：netQuality；  API声明：function on(type: 'netQosChange', callback: Callback<Array<NetworkQos>>): void;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：function off(type: 'netQosChange', callback?: Callback<Array<NetworkQos>>): void;  差异内容：NA | 类名：netQuality；  API声明：function off(type: 'netQosChange', callback?: Callback<Array<NetworkQos>>): void;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：function on(type: 'netSceneChange', callback: Callback<Array<NetworkScene>>): void;  差异内容：NA | 类名：netQuality；  API声明：function on(type: 'netSceneChange', callback: Callback<Array<NetworkScene>>): void;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：function off(type: 'netSceneChange', callback?: Callback<Array<NetworkScene>>): void;  差异内容：NA | 类名：netQuality；  API声明：function off(type: 'netSceneChange', callback?: Callback<Array<NetworkScene>>): void;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：function reportQoe(appQoe: AppQoe): void;  差异内容：NA | 类名：netQuality；  API声明：function reportQoe(appQoe: AppQoe): void;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：interface NetworkQos  差异内容：NA | 类名：netQuality；  API声明：interface NetworkQos  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：NetworkQos；  API声明：pathType: PathType;  差异内容：NA | 类名：NetworkQos；  API声明：pathType: PathType;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：NetworkQos；  API声明：linkUpBandwidth: RateBps;  差异内容：NA | 类名：NetworkQos；  API声明：linkUpBandwidth: RateBps;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：NetworkQos；  API声明：linkDownBandwidth: RateBps;  差异内容：NA | 类名：NetworkQos；  API声明：linkDownBandwidth: RateBps;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：NetworkQos；  API声明：linkUpRate: RateBps;  差异内容：NA | 类名：NetworkQos；  API声明：linkUpRate: RateBps;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：NetworkQos；  API声明：linkDownRate: RateBps;  差异内容：NA | 类名：NetworkQos；  API声明：linkDownRate: RateBps;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：NetworkQos；  API声明：rttMs: number;  差异内容：NA | 类名：NetworkQos；  API声明：rttMs: number;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：NetworkQos；  API声明：linkUpBufferDelayMs: number;  差异内容：NA | 类名：NetworkQos；  API声明：linkUpBufferDelayMs: number;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：NetworkQos；  API声明：linkUpBufferCongestionPercent?: number;  差异内容：NA | 类名：NetworkQos；  API声明：linkUpBufferCongestionPercent?: number;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：interface NetworkScene  差异内容：NA | 类名：netQuality；  API声明：interface NetworkScene  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：NetworkScene；  API声明：pathType: PathType;  差异内容：NA | 类名：NetworkScene；  API声明：pathType: PathType;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：NetworkScene；  API声明：scene: Scene;  差异内容：NA | 类名：NetworkScene；  API声明：scene: Scene;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：NetworkScene；  API声明：recommendedAction: RecommendedAction;  差异内容：NA | 类名：NetworkScene；  API声明：recommendedAction: RecommendedAction;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：NetworkScene；  API声明：weakSignalPrediction?: WeakSignalPrediction;  差异内容：NA | 类名：NetworkScene；  API声明：weakSignalPrediction?: WeakSignalPrediction;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：interface WeakSignalPrediction  差异内容：NA | 类名：netQuality；  API声明：interface WeakSignalPrediction  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：WeakSignalPrediction；  API声明：isLastPredictionValid: boolean;  差异内容：NA | 类名：WeakSignalPrediction；  API声明：isLastPredictionValid: boolean;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：WeakSignalPrediction；  API声明：startTime: number;  差异内容：NA | 类名：WeakSignalPrediction；  API声明：startTime: number;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：WeakSignalPrediction；  API声明：duration: number;  差异内容：NA | 类名：WeakSignalPrediction；  API声明：duration: number;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：interface AppQoe  差异内容：NA | 类名：netQuality；  API声明：interface AppQoe  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：AppQoe；  API声明：serviceType: ServiceType;  差异内容：NA | 类名：AppQoe；  API声明：serviceType: ServiceType;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：AppQoe；  API声明：qoeType: QoeType;  差异内容：NA | 类名：AppQoe；  API声明：qoeType: QoeType;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：type RateBps = number;  差异内容：NA | 类名：netQuality；  API声明：type RateBps = number;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：const BPS = 1;  差异内容：NA | 类名：netQuality；  API声明：const BPS = 1;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：const KBPS = 1000;  差异内容：NA | 类名：netQuality；  API声明：const KBPS = 1000;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：const MBPS = 1000000;  差异内容：NA | 类名：netQuality；  API声明：const MBPS = 1000000;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：const GBPS = 1000000000;  差异内容：NA | 类名：netQuality；  API声明：const GBPS = 1000000000;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：const TBPS = 1000000000000;  差异内容：NA | 类名：netQuality；  API声明：const TBPS = 1000000000000;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：type Scene = 'normal' | 'congestion' | 'frequentHandover' | 'weakSignal';  差异内容：NA | 类名：netQuality；  API声明：type Scene = 'normal' | 'congestion' | 'frequentHandover' | 'weakSignal';  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：export type DataSpeedSimpleAction = 'suspendData' | 'decreaseData' | 'increaseData' | 'keepData';  差异内容：NA | 类名：netQuality；  API声明：export type DataSpeedSimpleAction = 'suspendData' | 'decreaseData' | 'increaseData' | 'keepData';  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：type RecommendedAction = 'doCaching' | DataSpeedSimpleAction;  差异内容：NA | 类名：netQuality；  API声明：type RecommendedAction = 'doCaching' | DataSpeedSimpleAction;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：type ServiceType = 'default' | 'background' | 'realtimeVoice' | 'realtimeVideo' | 'callSignaling' | 'realtimeGame' | 'normalGame' | 'shortVideo' | 'longVideo' | 'livestreamingAnchor' | 'livestreamingWatcher' | 'download' | 'upload' | 'browser' | 'transaction' | 'shopping' | 'detection' | 'cloudService' | 'voiceConference' | 'videoConference' | 'audio' | 'navigation' | 'seckillService' | 'login';  差异内容：NA | 类名：netQuality；  API声明：type ServiceType = 'default' | 'background' | 'realtimeVoice' | 'realtimeVideo' | 'callSignaling' | 'realtimeGame' | 'normalGame' | 'shortVideo' | 'longVideo' | 'livestreamingAnchor' | 'livestreamingWatcher' | 'download' | 'upload' | 'browser' | 'transaction' | 'shopping' | 'detection' | 'cloudService' | 'voiceConference' | 'videoConference' | 'audio' | 'navigation' | 'seckillService' | 'login';  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：type BadQoeCause = 'unknown' | 'serverErr' | 'noData' | 'packetLost' | 'packetOutOfOrder' | 'highJitter' | 'highLatency';  差异内容：NA | 类名：netQuality；  API声明：type BadQoeCause = 'unknown' | 'serverErr' | 'noData' | 'packetLost' | 'packetOutOfOrder' | 'highJitter' | 'highLatency';  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：type QoeType = 'good' | BadQoeCause;  差异内容：NA | 类名：netQuality；  API声明：type QoeType = 'good' | BadQoeCause;  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：netQuality；  API声明：enum PathType  差异内容：NA | 类名：netQuality；  API声明：enum PathType  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：PathType；  API声明：CELLULAR\_PRIMARY = 0  差异内容：NA | 类名：PathType；  API声明：CELLULAR\_PRIMARY = 0  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：PathType；  API声明：CELLULAR\_SECONDARY = 1  差异内容：NA | 类名：PathType；  API声明：CELLULAR\_SECONDARY = 1  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：PathType；  API声明：WIFI\_PRIMARY = 2  差异内容：NA | 类名：PathType；  API声明：WIFI\_PRIMARY = 2  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
| API从不支持元服务到支持元服务 | 类名：PathType；  API声明：WIFI\_SECONDARY = 3  差异内容：NA | 类名：PathType；  API声明：WIFI\_SECONDARY = 3  差异内容：atomicservice | api/@hms.networkboost.netquality.d.ts |
