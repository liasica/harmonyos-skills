---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-nearlinkkit-510
title: NearLink Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > NearLink Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:766c21d923146331a28b91b2ef5620e893022bfcfd2f7b0a7cf0c0e654f131df
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace dataTransfer  差异内容：declare namespace dataTransfer | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer；  API声明：type ConnectionState = constant.ConnectionState;  差异内容：type ConnectionState = constant.ConnectionState; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer；  API声明：function createPort(uuid: string): void;  差异内容：function createPort(uuid: string): void; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer；  API声明：function destroyPort(uuid: string): void;  差异内容：function destroyPort(uuid: string): void; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer；  API声明：function connect(params: ConnectionParams): Promise<void>;  差异内容：function connect(params: ConnectionParams): Promise<void>; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer；  API声明：function disconnect(params: ConnectionParams): Promise<void>;  差异内容：function disconnect(params: ConnectionParams): Promise<void>; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer；  API声明：function on(type: 'connectionStateChanged', callback: Callback<ConnectionResult>): void;  差异内容：function on(type: 'connectionStateChanged', callback: Callback<ConnectionResult>): void; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer；  API声明：function off(type: 'connectionStateChanged', callback?: Callback<ConnectionResult>): void;  差异内容：function off(type: 'connectionStateChanged', callback?: Callback<ConnectionResult>): void; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer；  API声明：function getConnectionState(params: ConnectionStateParams): ConnectionState;  差异内容：function getConnectionState(params: ConnectionStateParams): ConnectionState; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer；  API声明：function writeData(params: DataParams): Promise<void>;  差异内容：function writeData(params: DataParams): Promise<void>; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer；  API声明：function on(type: 'readData', callback: Callback<DataParams>): void;  差异内容：function on(type: 'readData', callback: Callback<DataParams>): void; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer；  API声明：function off(type: 'readData', callback?: Callback<DataParams>): void;  差异内容：function off(type: 'readData', callback?: Callback<DataParams>): void; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer；  API声明：interface ConnectionParams  差异内容：interface ConnectionParams | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：ConnectionParams；  API声明：address: string;  差异内容：address: string; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：ConnectionParams；  API声明：uuid: string;  差异内容：uuid: string; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：ConnectionParams；  API声明：mtu?: number;  差异内容：mtu?: number; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：ConnectionParams；  API声明：transferMode?: TransferMode;  差异内容：transferMode?: TransferMode; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer；  API声明：interface DataParams  差异内容：interface DataParams | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：DataParams；  API声明：address: string;  差异内容：address: string; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：DataParams；  API声明：uuid: string;  差异内容：uuid: string; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：DataParams；  API声明：data: ArrayBuffer;  差异内容：data: ArrayBuffer; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer；  API声明：interface ConnectionResult  差异内容：interface ConnectionResult | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：ConnectionResult；  API声明：address: string;  差异内容：address: string; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：ConnectionResult；  API声明：uuid: string;  差异内容：uuid: string; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：ConnectionResult；  API声明：mtu: number;  差异内容：mtu: number; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：ConnectionResult；  API声明：state: ConnectionState;  差异内容：state: ConnectionState; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer；  API声明：interface ConnectionStateParams  差异内容：interface ConnectionStateParams | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：ConnectionStateParams；  API声明：address: string;  差异内容：address: string; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：ConnectionStateParams；  API声明：uuid: string;  差异内容：uuid: string; | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer；  API声明：enum TransferMode  差异内容：enum TransferMode | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：TransferMode；  API声明：BASIC = 0  差异内容：BASIC = 0 | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：TransferMode；  API声明：RELIABLE = 1  差异内容：RELIABLE = 1 | api/@hms.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_VEHICLE\_KEY = 0x001003  差异内容：DEVICE\_VEHICLE\_KEY = 0x001003 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_VEHICLE\_LOCK = 0x001004  差异内容：DEVICE\_VEHICLE\_LOCK = 0x001004 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：constant；  API声明：export enum AcbState  差异内容：export enum AcbState | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：AcbState；  API声明：DISCONNECTED = 0  差异内容：DISCONNECTED = 0 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：AcbState；  API声明：CONNECTED = 1  差异内容：CONNECTED = 1 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：AcbState；  API声明：ENCRYPTED = 2  差异内容：ENCRYPTED = 2 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：manager；  API声明：type AcbState = constant.AcbState;  差异内容：type AcbState = constant.AcbState; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager；  API声明：function on(type: 'acbStateChange', callback: Callback<AcbStateParam>): void;  差异内容：function on(type: 'acbStateChange', callback: Callback<AcbStateParam>): void; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager；  API声明：function off(type: 'acbStateChange', callback?: Callback<AcbStateParam>): void;  差异内容：function off(type: 'acbStateChange', callback?: Callback<AcbStateParam>): void; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：PairingReason；  API声明：PAIRING\_REASON\_PROFILE\_UNSUPPORTED = 2  差异内容：PAIRING\_REASON\_PROFILE\_UNSUPPORTED = 2 | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：PairingReason；  API声明：PAIRING\_REASON\_EXCEED\_ACB\_MAX = 3  差异内容：PAIRING\_REASON\_EXCEED\_ACB\_MAX = 3 | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：PairingReason；  API声明：PAIRING\_REASON\_REMOTE\_CANCELED = 4  差异内容：PAIRING\_REASON\_REMOTE\_CANCELED = 4 | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：PairingReason；  API声明：PAIRING\_REASON\_LOCAL\_CANCELED = 5  差异内容：PAIRING\_REASON\_LOCAL\_CANCELED = 5 | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：PairingType；  API声明：PAIRING\_TYPE\_PASSCODE = 1  差异内容：PAIRING\_TYPE\_PASSCODE = 1 | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：PairingType；  API声明：PAIRING\_TYPE\_NUMBER\_COMPARE = 2  差异内容：PAIRING\_TYPE\_NUMBER\_COMPARE = 2 | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager；  API声明：interface AcbStateParam  差异内容：interface AcbStateParam | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：AcbStateParam；  API声明：address: string;  差异内容：address: string; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：AcbStateParam；  API声明：state: AcbState;  差异内容：state: AcbState; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：remoteDevice；  API声明：type AcbState = constant.AcbState;  差异内容：type AcbState = constant.AcbState; | api/@hms.nearlink.remoteDevice.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.nearlink.dataTransfer.d.ts  差异内容：NearLinkKit | api/@hms.nearlink.dataTransfer.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：RemoteDevice；  API声明：startPairing(): Promise<void>;  差异内容：startPairing(): Promise<void>; | api/@hms.nearlink.remoteDevice.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：RemoteDevice；  API声明：getAcbState(): AcbState;  差异内容：getAcbState(): AcbState; | api/@hms.nearlink.remoteDevice.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ScanResults；  API声明：deviceClass?: constant.DeviceClass;  差异内容：deviceClass?: constant.DeviceClass; | api/@hms.nearlink.scan.d.ts |
