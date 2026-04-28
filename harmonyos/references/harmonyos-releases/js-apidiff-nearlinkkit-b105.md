---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-nearlinkkit-b105
title: NearLink Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > OS平台能力 > API变更清单 > HarmonyOS 5.0.1(13) Beta3引入的API > NearLink Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:05+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:22bb9e9c40897bda5d74b6403aab96b25b4e30b2151795209aa3d60480c15d6d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace advertising  差异内容： declare namespace advertising | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising；  API声明：function startAdvertising(advertisingParams: AdvertisingParams): Promise<number>;  差异内容：function startAdvertising(advertisingParams: AdvertisingParams): Promise<number>; | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising；  API声明：function stopAdvertising(advertisingId: number): Promise<void>;  差异内容：function stopAdvertising(advertisingId: number): Promise<void>; | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising；  API声明：function on(type: 'advertisingStateChange', callback: Callback<AdvertisingStateChangeInfo>): void;  差异内容：function on(type: 'advertisingStateChange', callback: Callback<AdvertisingStateChangeInfo>): void; | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising；  API声明：function off(type: 'advertisingStateChange', callback?: Callback<AdvertisingStateChangeInfo>): void;  差异内容：function off(type: 'advertisingStateChange', callback?: Callback<AdvertisingStateChangeInfo>): void; | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising；  API声明： interface AdvertisingParams  差异内容： interface AdvertisingParams | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingParams；  API声明：advertisingSettings: AdvertisingSettings;  差异内容：advertisingSettings: AdvertisingSettings; | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingParams；  API声明：advertisingData: AdvertisingData;  差异内容：advertisingData: AdvertisingData; | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising；  API声明： interface AdvertisingSettings  差异内容： interface AdvertisingSettings | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingSettings；  API声明：interval?: number;  差异内容：interval?: number; | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingSettings；  API声明：power?: TxPowerMode;  差异内容：power?: TxPowerMode; | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingSettings；  API声明：isConnectable?: boolean;  差异内容：isConnectable?: boolean; | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising；  API声明： interface AdvertisingData  差异内容： interface AdvertisingData | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingData；  API声明：serviceUuids?: Array<string>;  差异内容：serviceUuids?: Array<string>; | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingData；  API声明：manufacturerData?: Array<ManufacturerData>;  差异内容：manufacturerData?: Array<ManufacturerData>; | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingData；  API声明：serviceData?: Array<ServiceData>;  差异内容：serviceData?: Array<ServiceData>; | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingData；  API声明：includeDeviceName?: boolean;  差异内容：includeDeviceName?: boolean; | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising；  API声明： interface ManufacturerData  差异内容： interface ManufacturerData | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：ManufacturerData；  API声明：manufacturerId: number;  差异内容：manufacturerId: number; | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：ManufacturerData；  API声明：manufacturerData: ArrayBuffer;  差异内容：manufacturerData: ArrayBuffer; | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising；  API声明： interface ServiceData  差异内容： interface ServiceData | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：ServiceData；  API声明：serviceUuid: string;  差异内容：serviceUuid: string; | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：ServiceData；  API声明：serviceData: ArrayBuffer;  差异内容：serviceData: ArrayBuffer; | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising；  API声明： enum TxPowerMode  差异内容： enum TxPowerMode | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：TxPowerMode；  API声明：ADV\_TX\_POWER\_LOW = 1  差异内容：ADV\_TX\_POWER\_LOW = 1 | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：TxPowerMode；  API声明：ADV\_TX\_POWER\_MEDIUM = 2  差异内容：ADV\_TX\_POWER\_MEDIUM = 2 | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：TxPowerMode；  API声明：ADV\_TX\_POWER\_HIGH = 3  差异内容：ADV\_TX\_POWER\_HIGH = 3 | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising；  API声明： interface AdvertisingStateChangeInfo  差异内容： interface AdvertisingStateChangeInfo | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingStateChangeInfo；  API声明：advertisingId: number;  差异内容：advertisingId: number; | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingStateChangeInfo；  API声明：state: AdvertisingState;  差异内容：state: AdvertisingState; | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising；  API声明： enum AdvertisingState  差异内容： enum AdvertisingState | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingState；  API声明：STARTED = 1  差异内容：STARTED = 1 | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingState；  API声明：STOPPED = 2  差异内容：STOPPED = 2 | api/@hms.nearlink.advertising.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace constant  差异内容： declare namespace constant | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：constant；  API声明： export enum PairingState  差异内容： export enum PairingState | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：PairingState；  API声明：PAIRING\_STATE\_NONE = 1  差异内容：PAIRING\_STATE\_NONE = 1 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：PairingState；  API声明：PAIRING\_STATE\_PAIRING = 2  差异内容：PAIRING\_STATE\_PAIRING = 2 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：PairingState；  API声明：PAIRING\_STATE\_PAIRED = 3  差异内容：PAIRING\_STATE\_PAIRED = 3 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：constant；  API声明： export enum ConnectionState  差异内容： export enum ConnectionState | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：ConnectionState；  API声明：STATE\_CONNECTING = 0  差异内容：STATE\_CONNECTING = 0 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：ConnectionState；  API声明：STATE\_CONNECTED = 1  差异内容：STATE\_CONNECTED = 1 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：ConnectionState；  API声明：STATE\_DISCONNECTING = 2  差异内容：STATE\_DISCONNECTING = 2 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：ConnectionState；  API声明：STATE\_DISCONNECTED = 3  差异内容：STATE\_DISCONNECTED = 3 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：constant；  API声明： export enum DeviceClass  差异内容： export enum DeviceClass | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_UNCATEGORIZED = 0x000100  差异内容：DEVICE\_UNCATEGORIZED = 0x000100 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_PHONE = 0x000200  差异内容：DEVICE\_PHONE = 0x000200 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_SMARTPHONE = 0x000201  差异内容：DEVICE\_SMARTPHONE = 0x000201 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_COMPUTER = 0x000300  差异内容：DEVICE\_COMPUTER = 0x000300 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_LAPTOP = 0x000301  差异内容：DEVICE\_LAPTOP = 0x000301 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_TABLET = 0x000302  差异内容：DEVICE\_TABLET = 0x000302 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_ALL\_IN\_ONE\_COMPUTER = 0x000303  差异内容：DEVICE\_ALL\_IN\_ONE\_COMPUTER = 0x000303 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_MINI\_PC = 0x000304  差异内容：DEVICE\_MINI\_PC = 0x000304 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_WATCH = 0x000400  差异内容：DEVICE\_WATCH = 0x000400 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_SMART\_WATCH = 0x000401  差异内容：DEVICE\_SMART\_WATCH = 0x000401 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_HUMAN\_INTERFACE = 0x000500  差异内容：DEVICE\_HUMAN\_INTERFACE = 0x000500 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_KEYBOARD = 0x000501  差异内容：DEVICE\_KEYBOARD = 0x000501 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_MOUSE = 0x000502  差异内容：DEVICE\_MOUSE = 0x000502 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_HANDLE = 0x000503  差异内容：DEVICE\_HANDLE = 0x000503 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_STYLUS = 0x000504  差异内容：DEVICE\_STYLUS = 0x000504 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_TOUCHPAD = 0x000505  差异内容：DEVICE\_TOUCHPAD = 0x000505 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_AUDIO\_PLAYBACK = 0x000600  差异内容：DEVICE\_AUDIO\_PLAYBACK = 0x000600 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_SMART\_SPEAKER = 0x000601  差异内容：DEVICE\_SMART\_SPEAKER = 0x000601 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_ECHO\_WALL = 0x000602  差异内容：DEVICE\_ECHO\_WALL = 0x000602 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_AUDIO\_CAPTURE = 0x000700  差异内容：DEVICE\_AUDIO\_CAPTURE = 0x000700 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_KARAOKE\_MICROPHONE = 0x000701  差异内容：DEVICE\_KARAOKE\_MICROPHONE = 0x000701 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_LAPEL\_MICROPHONE = 0x000702  差异内容：DEVICE\_LAPEL\_MICROPHONE = 0x000702 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_WEARABLE\_AUDIO = 0x000800  差异内容：DEVICE\_WEARABLE\_AUDIO = 0x000800 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_IN\_EAR\_EARPHONE = 0x000801  差异内容：DEVICE\_IN\_EAR\_EARPHONE = 0x000801 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_HEADSET = 0x000802  差异内容：DEVICE\_HEADSET = 0x000802 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_OVER\_EAR\_HEADPHONE = 0x000803  差异内容：DEVICE\_OVER\_EAR\_HEADPHONE = 0x000803 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_NECKBAND\_EARPHONE = 0x000804  差异内容：DEVICE\_NECKBAND\_EARPHONE = 0x000804 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_PERSONAL\_CARE = 0x000900  差异内容：DEVICE\_PERSONAL\_CARE = 0x000900 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_INTELLIGENT\_TOOTHBRUSH = 0x000901  差异内容：DEVICE\_INTELLIGENT\_TOOTHBRUSH = 0x000901 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_SMART\_CUP = 0x000902  差异内容：DEVICE\_SMART\_CUP = 0x000902 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_INTELLIGENT\_SHAVER = 0x000903  差异内容：DEVICE\_INTELLIGENT\_SHAVER = 0x000903 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_HVAC = 0x000A00  差异内容：DEVICE\_HVAC = 0x000A00 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_AIR\_PURIFIER = 0x000A01  差异内容：DEVICE\_AIR\_PURIFIER = 0x000A01 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_HUMIDIFIER = 0x000A02  差异内容：DEVICE\_HUMIDIFIER = 0x000A02 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_AIR\_CIRCULATION\_FAN = 0x000A03  差异内容：DEVICE\_AIR\_CIRCULATION\_FAN = 0x000A03 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_ELECTRIC\_RIDE = 0x000B00  差异内容：DEVICE\_ELECTRIC\_RIDE = 0x000B00 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_ELECTRIC\_SCOOTER = 0x000B01  差异内容：DEVICE\_ELECTRIC\_SCOOTER = 0x000B01 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_ELECTRIC\_BICYCLE = 0x000B02  差异内容：DEVICE\_ELECTRIC\_BICYCLE = 0x000B02 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_LIGHT\_FITTING = 0x000C00  差异内容：DEVICE\_LIGHT\_FITTING = 0x000C00 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_SMART\_TABLE\_LAMP = 0x000C01  差异内容：DEVICE\_SMART\_TABLE\_LAMP = 0x000C01 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_REMOTE\_CONTROL = 0x000D00  差异内容：DEVICE\_REMOTE\_CONTROL = 0x000D00 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_TV\_REMOTE\_CONTROL = 0x000D01  差异内容：DEVICE\_TV\_REMOTE\_CONTROL = 0x000D01 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_IMAGING = 0x000E00  差异内容：DEVICE\_IMAGING = 0x000E00 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_SMART\_TV = 0x000E01  差异内容：DEVICE\_SMART\_TV = 0x000E01 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_IP\_CAMERA = 0x000E02  差异内容：DEVICE\_IP\_CAMERA = 0x000E02 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_SCREEN\_CASTER = 0x000E03  差异内容：DEVICE\_SCREEN\_CASTER = 0x000E03 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_NETWORKING = 0x000F00  差异内容：DEVICE\_NETWORKING = 0x000F00 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_IOT\_GATEWAY = 0x000F01  差异内容：DEVICE\_IOT\_GATEWAY = 0x000F01 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_ACCESS\_CONTROL = 0x001000  差异内容：DEVICE\_ACCESS\_CONTROL = 0x001000 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_INTELLIGENT\_LOCK = 0x001001  差异内容：DEVICE\_INTELLIGENT\_LOCK = 0x001001 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：DEVICE\_SMART\_KEY = 0x001002  差异内容：DEVICE\_SMART\_KEY = 0x001002 | api/@hms.nearlink.constant.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace manager  差异内容： declare namespace manager | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager；  API声明：type PairingState = constant.PairingState;  差异内容：type PairingState = constant.PairingState; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager；  API声明：type ConnectionState = constant.ConnectionState;  差异内容：type ConnectionState = constant.ConnectionState; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager；  API声明：function getState(): NearlinkState;  差异内容：function getState(): NearlinkState; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager；  API声明：function getLocalName(): string;  差异内容：function getLocalName(): string; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager；  API声明：function on(type: 'stateChange', callback: Callback<NearlinkState>): void;  差异内容：function on(type: 'stateChange', callback: Callback<NearlinkState>): void; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager；  API声明：function off(type: 'stateChange', callback?: Callback<NearlinkState>): void;  差异内容：function off(type: 'stateChange', callback?: Callback<NearlinkState>): void; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager；  API声明：function on(type: 'pairingStateChange', callback: Callback<PairingStateParam>): void;  差异内容：function on(type: 'pairingStateChange', callback: Callback<PairingStateParam>): void; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager；  API声明：function off(type: 'pairingStateChange', callback?: Callback<PairingStateParam>): void;  差异内容：function off(type: 'pairingStateChange', callback?: Callback<PairingStateParam>): void; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager；  API声明：function on(type: 'connectionStateChange', callback: Callback<ConnectionStateParam>): void;  差异内容：function on(type: 'connectionStateChange', callback: Callback<ConnectionStateParam>): void; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager；  API声明：function off(type: 'connectionStateChange', callback?: Callback<ConnectionStateParam>): void;  差异内容：function off(type: 'connectionStateChange', callback?: Callback<ConnectionStateParam>): void; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager；  API声明： enum NearlinkState  差异内容： enum NearlinkState | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：NearlinkState；  API声明：STATE\_TURNING\_ON = 0  差异内容：STATE\_TURNING\_ON = 0 | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：NearlinkState；  API声明：STATE\_ON = 1  差异内容：STATE\_ON = 1 | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：NearlinkState；  API声明：STATE\_TURNING\_OFF = 2  差异内容：STATE\_TURNING\_OFF = 2 | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：NearlinkState；  API声明：STATE\_OFF = 3  差异内容：STATE\_OFF = 3 | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager；  API声明： interface PairingStateParam  差异内容： interface PairingStateParam | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：PairingStateParam；  API声明：address: string;  差异内容：address: string; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：PairingStateParam；  API声明：preState: PairingState;  差异内容：preState: PairingState; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：PairingStateParam；  API声明：state: PairingState;  差异内容：state: PairingState; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：PairingStateParam；  API声明：reason: PairingReason;  差异内容：reason: PairingReason; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager；  API声明： enum PairingReason  差异内容： enum PairingReason | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：PairingReason；  API声明：PAIRING\_REASON\_SUCCESS = 0  差异内容：PAIRING\_REASON\_SUCCESS = 0 | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：PairingReason；  API声明：PAIRING\_REASON\_FAILURE = 1  差异内容：PAIRING\_REASON\_FAILURE = 1 | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager；  API声明： interface PairingRequestParam  差异内容： interface PairingRequestParam | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：PairingRequestParam；  API声明：address: string;  差异内容：address: string; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：PairingRequestParam；  API声明：passkey: string;  差异内容：passkey: string; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：PairingRequestParam；  API声明：pairingType: PairingType;  差异内容：pairingType: PairingType; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager；  API声明： enum PairingType  差异内容： enum PairingType | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：PairingType；  API声明：NO\_PASSKEY\_CONFIRMATION = 0  差异内容：NO\_PASSKEY\_CONFIRMATION = 0 | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager；  API声明： interface ConnectionStateParam  差异内容： interface ConnectionStateParam | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：ConnectionStateParam；  API声明：address: string;  差异内容：address: string; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：ConnectionStateParam；  API声明：preState: ConnectionState;  差异内容：preState: ConnectionState; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：ConnectionStateParam；  API声明：state: ConnectionState;  差异内容：state: ConnectionState; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：ConnectionStateParam；  API声明：connectionReason: ConnectionReason;  差异内容：connectionReason: ConnectionReason; | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager；  API声明： enum ConnectionReason  差异内容： enum ConnectionReason | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：ConnectionReason；  API声明：CONNECTION\_SUCCESS = 0  差异内容：CONNECTION\_SUCCESS = 0 | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：ConnectionReason；  API声明：CONNECTION\_FAILURE = 1  差异内容：CONNECTION\_FAILURE = 1 | api/@hms.nearlink.manager.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace remoteDevice  差异内容： declare namespace remoteDevice | api/@hms.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice；  API声明：type PairingState = constant.PairingState;  差异内容：type PairingState = constant.PairingState; | api/@hms.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice；  API声明：type ConnectionState = constant.ConnectionState;  差异内容：type ConnectionState = constant.ConnectionState; | api/@hms.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice；  API声明：type DeviceClass = constant.DeviceClass;  差异内容：type DeviceClass = constant.DeviceClass; | api/@hms.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice；  API声明：function createRemoteDevice(address: string): RemoteDevice;  差异内容：function createRemoteDevice(address: string): RemoteDevice; | api/@hms.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice；  API声明： interface RemoteDevice  差异内容： interface RemoteDevice | api/@hms.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：RemoteDevice；  API声明：getPairingState(): PairingState;  差异内容：getPairingState(): PairingState; | api/@hms.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：RemoteDevice；  API声明：getDeviceName(): string;  差异内容：getDeviceName(): string; | api/@hms.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：RemoteDevice；  API声明：getDeviceClass(): DeviceClass;  差异内容：getDeviceClass(): DeviceClass; | api/@hms.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：RemoteDevice；  API声明：getConnectionState(): ConnectionState;  差异内容：getConnectionState(): ConnectionState; | api/@hms.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace scan  差异内容： declare namespace scan | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：scan；  API声明：function startScan(filters: Array<ScanFilters>, options?: ScanOptions): Promise<void>;  差异内容：function startScan(filters: Array<ScanFilters>, options?: ScanOptions): Promise<void>; | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：scan；  API声明：function stopScan(): Promise<void>;  差异内容：function stopScan(): Promise<void>; | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：scan；  API声明：function on(type: 'deviceFound', callback: Callback<Array<ScanResults>>): void;  差异内容：function on(type: 'deviceFound', callback: Callback<Array<ScanResults>>): void; | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：scan；  API声明：function off(type: 'deviceFound', callback?: Callback<Array<ScanResults>>): void;  差异内容：function off(type: 'deviceFound', callback?: Callback<Array<ScanResults>>): void; | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：scan；  API声明： interface ScanResults  差异内容： interface ScanResults | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanResults；  API声明：address: string;  差异内容：address: string; | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanResults；  API声明：rssi: number;  差异内容：rssi: number; | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanResults；  API声明：data: ArrayBuffer;  差异内容：data: ArrayBuffer; | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanResults；  API声明：deviceName: string;  差异内容：deviceName: string; | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanResults；  API声明：isConnectable: boolean;  差异内容：isConnectable: boolean; | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：scan；  API声明： interface ScanFilters  差异内容： interface ScanFilters | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanFilters；  API声明：address?: string;  差异内容：address?: string; | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanFilters；  API声明：deviceName?: string;  差异内容：deviceName?: string; | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanFilters；  API声明：manufacturerId?: number;  差异内容：manufacturerId?: number; | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanFilters；  API声明：manufacturerData?: ArrayBuffer;  差异内容：manufacturerData?: ArrayBuffer; | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanFilters；  API声明：manufacturerDataMask?: ArrayBuffer;  差异内容：manufacturerDataMask?: ArrayBuffer; | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：scan；  API声明： interface ScanOptions  差异内容： interface ScanOptions | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanOptions；  API声明：scanMode?: ScanMode;  差异内容：scanMode?: ScanMode; | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanOptions；  API声明：duration?: number;  差异内容：duration?: number; | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：scan；  API声明： enum ScanMode  差异内容： enum ScanMode | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanMode；  API声明：SCAN\_MODE\_LOW\_POWER = 0  差异内容：SCAN\_MODE\_LOW\_POWER = 0 | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanMode；  API声明：SCAN\_MODE\_BALANCED = 1  差异内容：SCAN\_MODE\_BALANCED = 1 | api/@hms.nearlink.scan.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace ssap  差异内容： declare namespace ssap | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap；  API声明：type ConnectionState = constant.ConnectionState;  差异内容：type ConnectionState = constant.ConnectionState; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap；  API声明：function createClient(address: string): Client;  差异内容：function createClient(address: string): Client; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap；  API声明：function createServer(): Server;  差异内容：function createServer(): Server; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap；  API声明： interface Client  差异内容： interface Client | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client；  API声明：connect(): Promise<void>;  差异内容：connect(): Promise<void>; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client；  API声明：disconnect(): Promise<void>;  差异内容：disconnect(): Promise<void>; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client；  API声明：close(): void;  差异内容：close(): void; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client；  API声明：getServices(): Promise<Array<Service>>;  差异内容：getServices(): Promise<Array<Service>>; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client；  API声明：readProperty(property: Property): Promise<Property>;  差异内容：readProperty(property: Property): Promise<Property>; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client；  API声明：writeProperty(property: Property, writeType: PropertyWriteType): Promise<void>;  差异内容：writeProperty(property: Property, writeType: PropertyWriteType): Promise<void>; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client；  API声明：setPropertyNotification(property: Property, enable: boolean): Promise<void>;  差异内容：setPropertyNotification(property: Property, enable: boolean): Promise<void>; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client；  API声明：requestMtuSize(mtu: number): Promise<void>;  差异内容：requestMtuSize(mtu: number): Promise<void>; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client；  API声明：on(type: 'propertyChange', callback: Callback<Property>): void;  差异内容：on(type: 'propertyChange', callback: Callback<Property>): void; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client；  API声明：off(type: 'propertyChange', callback?: Callback<Property>): void;  差异内容：off(type: 'propertyChange', callback?: Callback<Property>): void; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client；  API声明：on(type: 'connectionStateChange', callback: Callback<ConnectionChangeState>): void;  差异内容：on(type: 'connectionStateChange', callback: Callback<ConnectionChangeState>): void; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client；  API声明：off(type: 'connectionStateChange', callback?: Callback<ConnectionChangeState>): void;  差异内容：off(type: 'connectionStateChange', callback?: Callback<ConnectionChangeState>): void; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client；  API声明：on(type: 'mtuChange', callback: Callback<number>): void;  差异内容：on(type: 'mtuChange', callback: Callback<number>): void; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client；  API声明：off(type: 'mtuChange', callback?: Callback<number>): void;  差异内容：off(type: 'mtuChange', callback?: Callback<number>): void; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap；  API声明： interface Server  差异内容： interface Server | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server；  API声明：addService(service: Service): void;  差异内容：addService(service: Service): void; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server；  API声明：removeService(serviceUuid: string): void;  差异内容：removeService(serviceUuid: string): void; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server；  API声明：close(): void;  差异内容：close(): void; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server；  API声明：notifyPropertyChanged(address: string, property: Property): Promise<void>;  差异内容：notifyPropertyChanged(address: string, property: Property): Promise<void>; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server；  API声明：sendResponse(response: ServerResponse): void;  差异内容：sendResponse(response: ServerResponse): void; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server；  API声明：on(type: 'connectionStateChange', callback: Callback<ConnectionChangeState>): void;  差异内容：on(type: 'connectionStateChange', callback: Callback<ConnectionChangeState>): void; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server；  API声明：off(type: 'connectionStateChange', callback?: Callback<ConnectionChangeState>): void;  差异内容：off(type: 'connectionStateChange', callback?: Callback<ConnectionChangeState>): void; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server；  API声明：on(type: 'propertyRead', callback: Callback<PropertyReadRequest>): void;  差异内容：on(type: 'propertyRead', callback: Callback<PropertyReadRequest>): void; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server；  API声明：off(type: 'propertyRead', callback?: Callback<PropertyReadRequest>): void;  差异内容：off(type: 'propertyRead', callback?: Callback<PropertyReadRequest>): void; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server；  API声明：on(type: 'propertyWrite', callback: Callback<PropertyWriteRequest>): void;  差异内容：on(type: 'propertyWrite', callback: Callback<PropertyWriteRequest>): void; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server；  API声明：off(type: 'propertyWrite', callback?: Callback<PropertyWriteRequest>): void;  差异内容：off(type: 'propertyWrite', callback?: Callback<PropertyWriteRequest>): void; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server；  API声明：on(type: 'mtuChange', callback: Callback<number>): void;  差异内容：on(type: 'mtuChange', callback: Callback<number>): void; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server；  API声明：off(type: 'mtuChange', callback?: Callback<number>): void;  差异内容：off(type: 'mtuChange', callback?: Callback<number>): void; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap；  API声明： interface Service  差异内容： interface Service | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Service；  API声明：serviceUuid: string;  差异内容：serviceUuid: string; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Service；  API声明：properties: Array<Property>;  差异内容：properties: Array<Property>; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap；  API声明： interface Property  差异内容： interface Property | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Property；  API声明：serviceUuid: string;  差异内容：serviceUuid: string; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Property；  API声明：propertyUuid: string;  差异内容：propertyUuid: string; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Property；  API声明：value: ArrayBuffer;  差异内容：value: ArrayBuffer; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Property；  API声明：descriptors?: Array<PropertyDescriptor>;  差异内容：descriptors?: Array<PropertyDescriptor>; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Property；  API声明：operation?: number;  差异内容：operation?: number; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap；  API声明： interface PropertyDescriptor  差异内容： interface PropertyDescriptor | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyDescriptor；  API声明：serviceUuid: string;  差异内容：serviceUuid: string; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyDescriptor；  API声明：propertyUuid: string;  差异内容：propertyUuid: string; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyDescriptor；  API声明：value: ArrayBuffer;  差异内容：value: ArrayBuffer; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyDescriptor；  API声明：descriptorType: PropertyDescriptorType;  差异内容：descriptorType: PropertyDescriptorType; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyDescriptor；  API声明：isWriteable?: boolean;  差异内容：isWriteable?: boolean; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap；  API声明： interface PropertyReadRequest  差异内容： interface PropertyReadRequest | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyReadRequest；  API声明：address: string;  差异内容：address: string; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyReadRequest；  API声明：serviceUuid: string;  差异内容：serviceUuid: string; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyReadRequest；  API声明：propertyUuid: string;  差异内容：propertyUuid: string; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyReadRequest；  API声明：requestId: number;  差异内容：requestId: number; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap；  API声明： interface PropertyWriteRequest  差异内容： interface PropertyWriteRequest | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyWriteRequest；  API声明：address: string;  差异内容：address: string; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyWriteRequest；  API声明：serviceUuid: string;  差异内容：serviceUuid: string; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyWriteRequest；  API声明：propertyUuid: string;  差异内容：propertyUuid: string; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyWriteRequest；  API声明：value: ArrayBuffer;  差异内容：value: ArrayBuffer; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyWriteRequest；  API声明：requestId: number;  差异内容：requestId: number; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyWriteRequest；  API声明：writeType: PropertyWriteType;  差异内容：writeType: PropertyWriteType; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap；  API声明： interface ServerResponse  差异内容： interface ServerResponse | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ServerResponse；  API声明：address: string;  差异内容：address: string; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ServerResponse；  API声明：requestId: number;  差异内容：requestId: number; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ServerResponse；  API声明：value: ArrayBuffer;  差异内容：value: ArrayBuffer; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap；  API声明： interface ConnectionChangeState  差异内容： interface ConnectionChangeState | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ConnectionChangeState；  API声明：address: string;  差异内容：address: string; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ConnectionChangeState；  API声明：state: ConnectionState;  差异内容：state: ConnectionState; | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap；  API声明： enum PropertyDescriptorType  差异内容： enum PropertyDescriptorType | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyDescriptorType；  API声明：PROPERTY = 1  差异内容：PROPERTY = 1 | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyDescriptorType；  API声明：CLIENT\_PROPERTY\_CONFIG = 2  差异内容：CLIENT\_PROPERTY\_CONFIG = 2 | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyDescriptorType；  API声明：SERVER\_PROPERTY\_CONFIG = 3  差异内容：SERVER\_PROPERTY\_CONFIG = 3 | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyDescriptorType；  API声明：PROPERTY\_FORMAT = 4  差异内容：PROPERTY\_FORMAT = 4 | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyDescriptorType；  API声明：TYPE\_VENDOR = 255  差异内容：TYPE\_VENDOR = 255 | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap；  API声明： enum Operation  差异内容： enum Operation | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Operation；  API声明：READABLE = 0x01  差异内容：READABLE = 0x01 | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Operation；  API声明：WRITE\_NO\_RESPONSE = 0x02  差异内容：WRITE\_NO\_RESPONSE = 0x02 | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Operation；  API声明：WRITE\_WITH\_RESPONSE = 0x04  差异内容：WRITE\_WITH\_RESPONSE = 0x04 | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Operation；  API声明：NOTIFY = 0x08  差异内容：NOTIFY = 0x08 | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap；  API声明： enum PropertyWriteType  差异内容： enum PropertyWriteType | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyWriteType；  API声明：WRITE = 1  差异内容：WRITE = 1 | api/@hms.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyWriteType；  API声明：WRITE\_NO\_RESPONSE = 2  差异内容：WRITE\_NO\_RESPONSE = 2 | api/@hms.nearlink.ssap.d.ts |
