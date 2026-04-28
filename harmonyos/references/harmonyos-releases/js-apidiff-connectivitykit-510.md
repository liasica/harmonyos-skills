---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-510
title: Connectivity Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Connectivity Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:07+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:8e37e9e50db463dbf4356a576d5d4557a23de9f228fd05166517f16c2395b691
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：HceService；  API声明：on(type: 'hceCmd', callback: AsyncCallback<number[]>): void;  差异内容：NA | 类名：HceService；  API声明：on(type: 'hceCmd', callback: AsyncCallback<number[]>): void;  差异内容：201,401,801 | api/@ohos.nfc.cardEmulation.d.ts |
| 新增错误码 | 类名：IsoDepTag；  API声明：isExtendedApduSupported(): Promise<boolean>;  差异内容：NA | 类名：IsoDepTag；  API声明：isExtendedApduSupported(): Promise<boolean>;  差异内容：3100205 | api/tag/nfctech.d.ts |
| 新增错误码 | 类名：NdefTag；  API声明：readNdef(): Promise<NdefMessage>;  差异内容：NA | 类名：NdefTag；  API声明：readNdef(): Promise<NdefMessage>;  差异内容：3100205 | api/tag/nfctech.d.ts |
| 新增错误码 | 类名：NdefTag；  API声明：writeNdef(msg: NdefMessage): Promise<void>;  差异内容：NA | 类名：NdefTag；  API声明：writeNdef(msg: NdefMessage): Promise<void>;  差异内容：3100205 | api/tag/nfctech.d.ts |
| 新增错误码 | 类名：NdefTag；  API声明：setReadOnly(): Promise<void>;  差异内容：NA | 类名：NdefTag；  API声明：setReadOnly(): Promise<void>;  差异内容：3100205 | api/tag/nfctech.d.ts |
| 新增错误码 | 类名：MifareClassicTag；  API声明：authenticateSector(sectorIndex: number, key: number[], isKeyA: boolean): Promise<void>;  差异内容：NA | 类名：MifareClassicTag；  API声明：authenticateSector(sectorIndex: number, key: number[], isKeyA: boolean): Promise<void>;  差异内容：3100205 | api/tag/nfctech.d.ts |
| 新增错误码 | 类名：MifareClassicTag；  API声明：readSingleBlock(blockIndex: number): Promise<number[]>;  差异内容：NA | 类名：MifareClassicTag；  API声明：readSingleBlock(blockIndex: number): Promise<number[]>;  差异内容：3100205 | api/tag/nfctech.d.ts |
| 新增错误码 | 类名：MifareClassicTag；  API声明：writeSingleBlock(blockIndex: number, data: number[]): Promise<void>;  差异内容：NA | 类名：MifareClassicTag；  API声明：writeSingleBlock(blockIndex: number, data: number[]): Promise<void>;  差异内容：3100205 | api/tag/nfctech.d.ts |
| 新增错误码 | 类名：MifareClassicTag；  API声明：incrementBlock(blockIndex: number, value: number): Promise<void>;  差异内容：NA | 类名：MifareClassicTag；  API声明：incrementBlock(blockIndex: number, value: number): Promise<void>;  差异内容：3100205 | api/tag/nfctech.d.ts |
| 新增错误码 | 类名：MifareClassicTag；  API声明：decrementBlock(blockIndex: number, value: number): Promise<void>;  差异内容：NA | 类名：MifareClassicTag；  API声明：decrementBlock(blockIndex: number, value: number): Promise<void>;  差异内容：3100205 | api/tag/nfctech.d.ts |
| 新增错误码 | 类名：MifareClassicTag；  API声明：transferToBlock(blockIndex: number): Promise<void>;  差异内容：NA | 类名：MifareClassicTag；  API声明：transferToBlock(blockIndex: number): Promise<void>;  差异内容：3100205 | api/tag/nfctech.d.ts |
| 新增错误码 | 类名：MifareClassicTag；  API声明：restoreFromBlock(blockIndex: number): Promise<void>;  差异内容：NA | 类名：MifareClassicTag；  API声明：restoreFromBlock(blockIndex: number): Promise<void>;  差异内容：3100205 | api/tag/nfctech.d.ts |
| 新增错误码 | 类名：MifareUltralightTag；  API声明：readMultiplePages(pageIndex: number): Promise<number[]>;  差异内容：NA | 类名：MifareUltralightTag；  API声明：readMultiplePages(pageIndex: number): Promise<number[]>;  差异内容：3100205 | api/tag/nfctech.d.ts |
| 新增错误码 | 类名：MifareUltralightTag；  API声明：writeSinglePage(pageIndex: number, data: number[]): Promise<void>;  差异内容：NA | 类名：MifareUltralightTag；  API声明：writeSinglePage(pageIndex: number, data: number[]): Promise<void>;  差异内容：3100205 | api/tag/nfctech.d.ts |
| 新增错误码 | 类名：NdefFormatableTag；  API声明：format(message: NdefMessage): Promise<void>;  差异内容：NA | 类名：NdefFormatableTag；  API声明：format(message: NdefMessage): Promise<void>;  差异内容：3100205 | api/tag/nfctech.d.ts |
| 新增错误码 | 类名：NdefFormatableTag；  API声明：formatReadOnly(message: NdefMessage): Promise<void>;  差异内容：NA | 类名：NdefFormatableTag；  API声明：formatReadOnly(message: NdefMessage): Promise<void>;  差异内容：3100205 | api/tag/nfctech.d.ts |
| 新增错误码 | 类名：TagSession；  API声明：transmit(data: number[]): Promise<number[]>;  差异内容：NA | 类名：TagSession；  API声明：transmit(data: number[]): Promise<number[]>;  差异内容：3100205 | api/tag/tagSession.d.ts |
| 删除错误码 | 类名：access；  API声明：function on(type: 'stateChange', callback: Callback<BluetoothState>): void;  差异内容：201 | 类名：access；  API声明：function on(type: 'stateChange', callback: Callback<BluetoothState>): void;  差异内容：NA | api/@ohos.bluetooth.access.d.ts |
| 删除错误码 | 类名：access；  API声明：function off(type: 'stateChange', callback?: Callback<BluetoothState>): void;  差异内容：201 | 类名：access；  API声明：function off(type: 'stateChange', callback?: Callback<BluetoothState>): void;  差异内容：NA | api/@ohos.bluetooth.access.d.ts |
| 删除错误码 | 类名：connection；  API声明：function getRemoteDeviceClass(deviceId: string): DeviceClass;  差异内容：201 | 类名：connection；  API声明：function getRemoteDeviceClass(deviceId: string): DeviceClass;  差异内容：NA | api/@ohos.bluetooth.connection.d.ts |
| 权限变更 | 类名：access；  API声明：function on(type: 'stateChange', callback: Callback<BluetoothState>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | 类名：access；  API声明：function on(type: 'stateChange', callback: Callback<BluetoothState>): void;  差异内容：NA | api/@ohos.bluetooth.access.d.ts |
| 权限变更 | 类名：access；  API声明：function off(type: 'stateChange', callback?: Callback<BluetoothState>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | 类名：access；  API声明：function off(type: 'stateChange', callback?: Callback<BluetoothState>): void;  差异内容：NA | api/@ohos.bluetooth.access.d.ts |
| 权限变更 | 类名：connection；  API声明：function getRemoteDeviceClass(deviceId: string): DeviceClass;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | 类名：connection；  API声明：function getRemoteDeviceClass(deviceId: string): DeviceClass;  差异内容：NA | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface BarcodeTag  差异内容：export interface BarcodeTag | api/tag/nfctech.d.ts |
| 新增API | NA | 类名：BarcodeTag；  API声明：getBarcode(): Promise<ArrayBuffer>;  差异内容：getBarcode(): Promise<ArrayBuffer>; | api/tag/nfctech.d.ts |
| 新增API | NA | 类名：connection；  API声明：function on(type: 'discoveryResult', callback: Callback<Array<DiscoveryResult>>): void;  差异内容：function on(type: 'discoveryResult', callback: Callback<Array<DiscoveryResult>>): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function off(type: 'discoveryResult', callback?: Callback<Array<DiscoveryResult>>): void;  差异内容：function off(type: 'discoveryResult', callback?: Callback<Array<DiscoveryResult>>): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：interface DiscoveryResult  差异内容：interface DiscoveryResult | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：DiscoveryResult；  API声明：deviceId: string;  差异内容：deviceId: string; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：DiscoveryResult；  API声明：rssi: number;  差异内容：rssi: number; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：DiscoveryResult；  API声明：deviceName: string;  差异内容：deviceName: string; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：DiscoveryResult；  API声明：deviceClass: DeviceClass;  差异内容：deviceClass: DeviceClass; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：function getMultiLinkedInfo(): Array<WifiLinkedInfo>;  差异内容：function getMultiLinkedInfo(): Array<WifiLinkedInfo>; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：function getLinkedInfoSync(): WifiLinkedInfo;  差异内容：function getLinkedInfoSync(): WifiLinkedInfo; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：enum WifiLinkType  差异内容：enum WifiLinkType | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiLinkType；  API声明：DEFAULT\_LINK = 0  差异内容：DEFAULT\_LINK = 0 | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiLinkType；  API声明：WIFI7\_SINGLE\_LINK = 1  差异内容：WIFI7\_SINGLE\_LINK = 1 | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiLinkType；  API声明：WIFI7\_MLSR = 2  差异内容：WIFI7\_MLSR = 2 | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiLinkType；  API声明：WIFI7\_EMLSR = 3  差异内容：WIFI7\_EMLSR = 3 | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiLinkType；  API声明：WIFI7\_STR = 4  差异内容：WIFI7\_STR = 4 | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：ScanReportMode；  API声明：FENCE\_SENSITIVITY\_LOW = 10  差异内容：FENCE\_SENSITIVITY\_LOW = 10 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanReportMode；  API声明：FENCE\_SENSITIVITY\_HIGH = 11  差异内容：FENCE\_SENSITIVITY\_HIGH = 11 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：socket；  API声明：function sppWriteAsync(clientSocket: number, data: ArrayBuffer): Promise<void>;  差异内容：function sppWriteAsync(clientSocket: number, data: ArrayBuffer): Promise<void>; | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：socket；  API声明：function sppReadAsync(clientSocket: number): Promise<ArrayBuffer>;  差异内容：function sppReadAsync(clientSocket: number): Promise<ArrayBuffer>; | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：tag；  API声明：const NFC\_BARCODE = 10;  差异内容：const NFC\_BARCODE = 10; | api/@ohos.nfc.tag.d.ts |
| 新增API | NA | 类名：tag；  API声明：function getBarcodeTag(tagInfo: TagInfo): BarcodeTag;  差异内容：function getBarcodeTag(tagInfo: TagInfo): BarcodeTag; | api/@ohos.nfc.tag.d.ts |
| 新增API | NA | 类名：ndef；  API声明：function makeApplicationRecord(bundleName: string): NdefRecord;  差异内容：function makeApplicationRecord(bundleName: string): NdefRecord; | api/@ohos.nfc.tag.d.ts |
| 新增API | NA | 类名：tag；  API声明：export type BarcodeTag = \_BarcodeTag;  差异内容：export type BarcodeTag = \_BarcodeTag; | api/@ohos.nfc.tag.d.ts |
| 新增API | NA | 类名：omapi；  API声明：function on(type: 'stateChanged', callback: Callback<ServiceState>): void;  差异内容：function on(type: 'stateChanged', callback: Callback<ServiceState>): void; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：omapi；  API声明：function off(type: 'stateChanged', callback?: Callback<ServiceState>): void;  差异内容：function off(type: 'stateChanged', callback?: Callback<ServiceState>): void; | api/@ohos.secureElement.d.ts |
| 起始版本有变化 | 类名：connection；  API声明：type ProfileUuids = constant.ProfileUuids;  差异内容：10 | 类名：connection；  API声明：type ProfileUuids = constant.ProfileUuids;  差异内容：12 | api/@ohos.bluetooth.connection.d.ts |
| 起始版本有变化 | 类名：connection；  API声明：function getRemoteProfileUuids(deviceId: string, callback: AsyncCallback<Array<ProfileUuids>>): void;  差异内容：10 | 类名：connection；  API声明：function getRemoteProfileUuids(deviceId: string, callback: AsyncCallback<Array<ProfileUuids>>): void;  差异内容：12 | api/@ohos.bluetooth.connection.d.ts |
| 起始版本有变化 | 类名：connection；  API声明：function getRemoteProfileUuids(deviceId: string): Promise<Array<ProfileUuids>>;  差异内容：10 | 类名：connection；  API声明：function getRemoteProfileUuids(deviceId: string): Promise<Array<ProfileUuids>>;  差异内容：12 | api/@ohos.bluetooth.connection.d.ts |
| 起始版本有变化 | 类名：connection；  API声明：function connectAllowedProfiles(deviceId: string, callback: AsyncCallback<void>): void;  差异内容：11 | 类名：connection；  API声明：function connectAllowedProfiles(deviceId: string, callback: AsyncCallback<void>): void;  差异内容：16 | api/@ohos.bluetooth.connection.d.ts |
| 起始版本有变化 | 类名：connection；  API声明：function connectAllowedProfiles(deviceId: string): Promise<void>;  差异内容：11 | 类名：connection；  API声明：function connectAllowedProfiles(deviceId: string): Promise<void>;  差异内容：16 | api/@ohos.bluetooth.connection.d.ts |
| 起始版本有变化 | 类名：constant；  API声明：export enum ProfileUuids  差异内容：10 | 类名：constant；  API声明：export enum ProfileUuids  差异内容：12 | api/@ohos.bluetooth.constant.d.ts |
| 起始版本有变化 | 类名：ProfileUuids；  API声明：PROFILE\_UUID\_HFP\_AG = '0000111F-0000-1000-8000-00805F9B34FB'  差异内容：10 | 类名：ProfileUuids；  API声明：PROFILE\_UUID\_HFP\_AG = '0000111F-0000-1000-8000-00805F9B34FB'  差异内容：12 | api/@ohos.bluetooth.constant.d.ts |
| 起始版本有变化 | 类名：ProfileUuids；  API声明：PROFILE\_UUID\_HFP\_HF = '0000111E-0000-1000-8000-00805F9B34FB'  差异内容：10 | 类名：ProfileUuids；  API声明：PROFILE\_UUID\_HFP\_HF = '0000111E-0000-1000-8000-00805F9B34FB'  差异内容：12 | api/@ohos.bluetooth.constant.d.ts |
| 起始版本有变化 | 类名：ProfileUuids；  API声明：PROFILE\_UUID\_HSP\_AG = '00001112-0000-1000-8000-00805F9B34FB'  差异内容：10 | 类名：ProfileUuids；  API声明：PROFILE\_UUID\_HSP\_AG = '00001112-0000-1000-8000-00805F9B34FB'  差异内容：12 | api/@ohos.bluetooth.constant.d.ts |
| 起始版本有变化 | 类名：ProfileUuids；  API声明：PROFILE\_UUID\_HSP\_HS = '00001108-0000-1000-8000-00805F9B34FB'  差异内容：10 | 类名：ProfileUuids；  API声明：PROFILE\_UUID\_HSP\_HS = '00001108-0000-1000-8000-00805F9B34FB'  差异内容：12 | api/@ohos.bluetooth.constant.d.ts |
| 起始版本有变化 | 类名：ProfileUuids；  API声明：PROFILE\_UUID\_A2DP\_SRC = '0000110A-0000-1000-8000-00805F9B34FB'  差异内容：10 | 类名：ProfileUuids；  API声明：PROFILE\_UUID\_A2DP\_SRC = '0000110A-0000-1000-8000-00805F9B34FB'  差异内容：12 | api/@ohos.bluetooth.constant.d.ts |
| 起始版本有变化 | 类名：ProfileUuids；  API声明：PROFILE\_UUID\_A2DP\_SINK = '0000110B-0000-1000-8000-00805F9B34FB'  差异内容：10 | 类名：ProfileUuids；  API声明：PROFILE\_UUID\_A2DP\_SINK = '0000110B-0000-1000-8000-00805F9B34FB'  差异内容：12 | api/@ohos.bluetooth.constant.d.ts |
| 起始版本有变化 | 类名：ProfileUuids；  API声明：PROFILE\_UUID\_AVRCP\_CT = '0000110E-0000-1000-8000-00805F9B34FB'  差异内容：10 | 类名：ProfileUuids；  API声明：PROFILE\_UUID\_AVRCP\_CT = '0000110E-0000-1000-8000-00805F9B34FB'  差异内容：12 | api/@ohos.bluetooth.constant.d.ts |
| 起始版本有变化 | 类名：ProfileUuids；  API声明：PROFILE\_UUID\_AVRCP\_TG = '0000110C-0000-1000-8000-00805F9B34FB'  差异内容：10 | 类名：ProfileUuids；  API声明：PROFILE\_UUID\_AVRCP\_TG = '0000110C-0000-1000-8000-00805F9B34FB'  差异内容：12 | api/@ohos.bluetooth.constant.d.ts |
| 起始版本有变化 | 类名：ProfileUuids；  API声明：PROFILE\_UUID\_HID = '00001124-0000-1000-8000-00805F9B34FB'  差异内容：10 | 类名：ProfileUuids；  API声明：PROFILE\_UUID\_HID = '00001124-0000-1000-8000-00805F9B34FB'  差异内容：12 | api/@ohos.bluetooth.constant.d.ts |
| 起始版本有变化 | 类名：ProfileUuids；  API声明：PROFILE\_UUID\_HOGP = '00001812-0000-1000-8000-00805F9B34FB'  差异内容：10 | 类名：ProfileUuids；  API声明：PROFILE\_UUID\_HOGP = '00001812-0000-1000-8000-00805F9B34FB'  差异内容：12 | api/@ohos.bluetooth.constant.d.ts |
| 起始版本有变化 | 类名：wifiManager；  API声明：function isHotspotActive(): boolean;  差异内容：9 | 类名：wifiManager；  API声明：function isHotspotActive(): boolean;  差异内容：15 | api/@ohos.wifiManager.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：HceService；  API声明：off(type: 'hceCmd', callback?: AsyncCallback<number[]>): void;  差异内容：off(type: 'hceCmd', callback?: AsyncCallback<number[]>): void; | api/@ohos.nfc.cardEmulation.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：WifiLinkedInfo；  API声明：wifiLinkType?: WifiLinkType;  差异内容：wifiLinkType?: WifiLinkType; | api/@ohos.wifiManager.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：BLECharacteristic；  API声明：characteristicValueHandle?: number;  差异内容：characteristicValueHandle?: number; | api/@ohos.bluetooth.ble.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：BLEDescriptor；  API声明：descriptorHandle?: number;  差异内容：descriptorHandle?: number; | api/@ohos.bluetooth.ble.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：AdvertiseData；  API声明：includeTxPower?: boolean;  差异内容：includeTxPower?: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增导出符号 | 类名：global；  API声明：export interface BarcodeTag  差异内容：NA | 类名：global；  API声明：  差异内容：export interface BarcodeTag | api/tag/nfctech.d.ts |
