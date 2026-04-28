---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-distributedservicekit-510
title: Distributed Service Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Distributed Service Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:09+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:cfdaf1d8e0cece22b77ebc8a685aee9fbfa5fe220c812a5c404ff7a845d3a4cc
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：distributedDeviceManager；  API声明：function releaseDeviceManager(deviceManager: DeviceManager): void;  差异内容：201 | 类名：distributedDeviceManager；  API声明：function releaseDeviceManager(deviceManager: DeviceManager): void;  差异内容：NA | api/@ohos.distributedDeviceManager.d.ts |
| 删除错误码 | 类名：DeviceManager；  API声明：getAvailableDeviceListSync(): Array<DeviceBasicInfo>;  差异内容：401 | 类名：DeviceManager；  API声明：getAvailableDeviceListSync(): Array<DeviceBasicInfo>;  差异内容：NA | api/@ohos.distributedDeviceManager.d.ts |
| 删除错误码 | 类名：DeviceManager；  API声明：stopDiscovering(): void;  差异内容：11600104,401 | 类名：DeviceManager；  API声明：stopDiscovering(): void;  差异内容：NA | api/@ohos.distributedDeviceManager.d.ts |
| 权限变更 | 类名：distributedDeviceManager；  API声明：function releaseDeviceManager(deviceManager: DeviceManager): void;  差异内容：ohos.permission.DISTRIBUTED\_DATASYNC | 类名：distributedDeviceManager；  API声明：function releaseDeviceManager(deviceManager: DeviceManager): void;  差异内容：NA | api/@ohos.distributedDeviceManager.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace abilityConnectionManager  差异内容：declare namespace abilityConnectionManager | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：interface PeerInfo  差异内容：interface PeerInfo | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：PeerInfo；  API声明：deviceId: string;  差异内容：deviceId: string; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：PeerInfo；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：PeerInfo；  API声明：moduleName: string;  差异内容：moduleName: string; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：PeerInfo；  API声明：abilityName: string;  差异内容：abilityName: string; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：PeerInfo；  API声明：serviceName?: string;  差异内容：serviceName?: string; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：interface ConnectOptions  差异内容：interface ConnectOptions | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectOptions；  API声明：needSendData?: boolean;  差异内容：needSendData?: boolean; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectOptions；  API声明：startOptions?: StartOptionParams;  差异内容：startOptions?: StartOptionParams; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectOptions；  API声明：parameters?: Record<string, string>;  差异内容：parameters?: Record<string, string>; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：interface ConnectResult  差异内容：interface ConnectResult | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectResult；  API声明：isConnected: boolean;  差异内容：isConnected: boolean; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectResult；  API声明：errorCode?: ConnectErrorCode;  差异内容：errorCode?: ConnectErrorCode; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectResult；  API声明：reason?: string;  差异内容：reason?: string; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：export enum ConnectErrorCode  差异内容：export enum ConnectErrorCode | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectErrorCode；  API声明：CONNECTED\_SESSION\_EXISTS = 0  差异内容：CONNECTED\_SESSION\_EXISTS = 0 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectErrorCode；  API声明：PEER\_APP\_REJECTED = 1  差异内容：PEER\_APP\_REJECTED = 1 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectErrorCode；  API声明：LOCAL\_WIFI\_NOT\_OPEN = 2  差异内容：LOCAL\_WIFI\_NOT\_OPEN = 2 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectErrorCode；  API声明：PEER\_WIFI\_NOT\_OPEN = 3  差异内容：PEER\_WIFI\_NOT\_OPEN = 3 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectErrorCode；  API声明：PEER\_ABILITY\_NO\_ONCOLLABORATE = 4  差异内容：PEER\_ABILITY\_NO\_ONCOLLABORATE = 4 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：ConnectErrorCode；  API声明：SYSTEM\_INTERNAL\_ERROR = 5  差异内容：SYSTEM\_INTERNAL\_ERROR = 5 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：export enum StartOptionParams  差异内容：export enum StartOptionParams | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：StartOptionParams；  API声明：START\_IN\_FOREGROUND = 0  差异内容：START\_IN\_FOREGROUND = 0 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：interface EventCallbackInfo  差异内容：interface EventCallbackInfo | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：EventCallbackInfo；  API声明：sessionId: number;  差异内容：sessionId: number; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：EventCallbackInfo；  API声明：eventType: string;  差异内容：eventType: string; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：EventCallbackInfo；  API声明：reason?: DisconnectReason;  差异内容：reason?: DisconnectReason; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：EventCallbackInfo；  API声明：msg?: string;  差异内容：msg?: string; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：EventCallbackInfo；  API声明：data?: ArrayBuffer;  差异内容：data?: ArrayBuffer; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：interface CollaborateEventInfo  差异内容：interface CollaborateEventInfo | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：CollaborateEventInfo；  API声明：sessionId: number;  差异内容：sessionId: number; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：CollaborateEventInfo；  API声明：eventType: CollaborateEventType;  差异内容：eventType: CollaborateEventType; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：CollaborateEventInfo；  API声明：eventMsg?: string;  差异内容：eventMsg?: string; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：enum CollaborateEventType  差异内容：enum CollaborateEventType | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：CollaborateEventType；  API声明：SEND\_FAILURE = 0  差异内容：SEND\_FAILURE = 0 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：CollaborateEventType；  API声明：COLOR\_SPACE\_CONVERSION\_FAILURE = 1  差异内容：COLOR\_SPACE\_CONVERSION\_FAILURE = 1 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：enum DisconnectReason  差异内容：enum DisconnectReason | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：DisconnectReason；  API声明：PEER\_APP\_CLOSE\_COLLABORATION = 0  差异内容：PEER\_APP\_CLOSE\_COLLABORATION = 0 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：DisconnectReason；  API声明：PEER\_APP\_EXIT = 1  差异内容：PEER\_APP\_EXIT = 1 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：DisconnectReason；  API声明：NETWORK\_DISCONNECTED = 2  差异内容：NETWORK\_DISCONNECTED = 2 | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：function on(type: 'connect', sessionId: number, callback: Callback<EventCallbackInfo>): void;  差异内容：function on(type: 'connect', sessionId: number, callback: Callback<EventCallbackInfo>): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：function off(type: 'connect', sessionId: number, callback?: Callback<EventCallbackInfo>): void;  差异内容：function off(type: 'connect', sessionId: number, callback?: Callback<EventCallbackInfo>): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：function on(type: 'disconnect', sessionId: number, callback: Callback<EventCallbackInfo>): void;  差异内容：function on(type: 'disconnect', sessionId: number, callback: Callback<EventCallbackInfo>): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：function off(type: 'disconnect', sessionId: number, callback?: Callback<EventCallbackInfo>): void;  差异内容：function off(type: 'disconnect', sessionId: number, callback?: Callback<EventCallbackInfo>): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：function on(type: 'receiveMessage', sessionId: number, callback: Callback<EventCallbackInfo>): void;  差异内容：function on(type: 'receiveMessage', sessionId: number, callback: Callback<EventCallbackInfo>): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：function off(type: 'receiveMessage', sessionId: number, callback?: Callback<EventCallbackInfo>): void;  差异内容：function off(type: 'receiveMessage', sessionId: number, callback?: Callback<EventCallbackInfo>): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：function on(type: 'receiveData', sessionId: number, callback: Callback<EventCallbackInfo>): void;  差异内容：function on(type: 'receiveData', sessionId: number, callback: Callback<EventCallbackInfo>): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：function off(type: 'receiveData', sessionId: number, callback?: Callback<EventCallbackInfo>): void;  差异内容：function off(type: 'receiveData', sessionId: number, callback?: Callback<EventCallbackInfo>): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：function createAbilityConnectionSession(serviceName: string, context: Context, peerInfo: PeerInfo, connectOptions: ConnectOptions): number;  差异内容：function createAbilityConnectionSession(serviceName: string, context: Context, peerInfo: PeerInfo, connectOptions: ConnectOptions): number; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：function destroyAbilityConnectionSession(sessionId: number): void;  差异内容：function destroyAbilityConnectionSession(sessionId: number): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：function getPeerInfoById(sessionId: number): PeerInfo | undefined;  差异内容：function getPeerInfoById(sessionId: number): PeerInfo | undefined; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：function connect(sessionId: number): Promise<ConnectResult>;  差异内容：function connect(sessionId: number): Promise<ConnectResult>; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：function disconnect(sessionId: number): void;  差异内容：function disconnect(sessionId: number): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：function acceptConnect(sessionId: number, token: string): Promise<void>;  差异内容：function acceptConnect(sessionId: number, token: string): Promise<void>; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：function reject(token: string, reason: string): void;  差异内容：function reject(token: string, reason: string): void; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：function sendMessage(sessionId: number, msg: string): Promise<void>;  差异内容：function sendMessage(sessionId: number, msg: string): Promise<void>; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：function sendData(sessionId: number, data: ArrayBuffer): Promise<void>;  差异内容：function sendData(sessionId: number, data: ArrayBuffer): Promise<void>; | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：export enum CollaborationKeys  差异内容：export enum CollaborationKeys | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：CollaborationKeys；  API声明：PEER\_INFO = 'ohos.collaboration.key.peerInfo'  差异内容：PEER\_INFO = 'ohos.collaboration.key.peerInfo' | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：CollaborationKeys；  API声明：CONNECT\_OPTIONS = 'ohos.collaboration.key.connectOptions'  差异内容：CONNECT\_OPTIONS = 'ohos.collaboration.key.connectOptions' | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：CollaborationKeys；  API声明：COLLABORATE\_TYPE = 'ohos.collaboration.key.abilityCollaborateType'  差异内容：COLLABORATE\_TYPE = 'ohos.collaboration.key.abilityCollaborateType' | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：abilityConnectionManager；  API声明：export enum CollaborationValues  差异内容：export enum CollaborationValues | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：CollaborationValues；  API声明：ABILITY\_COLLABORATION\_TYPE\_DEFAULT = 'ohos.collaboration.value.abilityCollab'  差异内容：ABILITY\_COLLABORATION\_TYPE\_DEFAULT = 'ohos.collaboration.value.abilityCollab' | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增API | NA | 类名：CollaborationValues；  API声明：ABILITY\_COLLABORATION\_TYPE\_CONNECT\_PROXY = 'ohos.collaboration.value.connectProxy'  差异内容：ABILITY\_COLLABORATION\_TYPE\_CONNECT\_PROXY = 'ohos.collaboration.value.connectProxy' | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.distributedsched.abilityConnectionManager.d.ts  差异内容：DistributedServiceKit | api/@ohos.distributedsched.abilityConnectionManager.d.ts |
