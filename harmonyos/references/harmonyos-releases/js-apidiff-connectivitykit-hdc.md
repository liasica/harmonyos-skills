---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-hdc
title: Connectivity Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta1引入的API > Connectivity Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:59+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:808efab372536cce121f27ec9979fa7f9415101b8908b5f4d9527f0ca10e34d7
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：bluetooth；  API声明： namespace BLE  差异内容：NA | 类名：bluetooth；  API声明： namespace BLE  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：getDeviceName(): Promise<string>;  差异内容：NA | 类名：GattClientDevice；  API声明：getDeviceName(): Promise<string>;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：getServices(): Promise<Array<GattService>>;  差异内容：NA | 类名：GattClientDevice；  API声明：getServices(): Promise<Array<GattService>>;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>;  差异内容：NA | 类名：GattClientDevice；  API声明：readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>;  差异内容：NA | 类名：GattClientDevice；  API声明：readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：getRssiValue(): Promise<number>;  差异内容：NA | 类名：GattClientDevice；  API声明：getRssiValue(): Promise<number>;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：GattService；  API声明：serviceUuid: string;  差异内容：NA | 类名：GattService；  API声明：serviceUuid: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：GattService；  API声明：isPrimary: boolean;  差异内容：NA | 类名：GattService；  API声明：isPrimary: boolean;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：GattService；  API声明：characteristics: Array<BLECharacteristic>;  差异内容：NA | 类名：GattService；  API声明：characteristics: Array<BLECharacteristic>;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：GattService；  API声明：includeServices?: Array<GattService>;  差异内容：NA | 类名：GattService；  API声明：includeServices?: Array<GattService>;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BLECharacteristic；  API声明：serviceUuid: string;  差异内容：NA | 类名：BLECharacteristic；  API声明：serviceUuid: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BLECharacteristic；  API声明：characteristicUuid: string;  差异内容：NA | 类名：BLECharacteristic；  API声明：characteristicUuid: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BLECharacteristic；  API声明：characteristicValue: ArrayBuffer;  差异内容：NA | 类名：BLECharacteristic；  API声明：characteristicValue: ArrayBuffer;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BLECharacteristic；  API声明：descriptors: Array<BLEDescriptor>;  差异内容：NA | 类名：BLECharacteristic；  API声明：descriptors: Array<BLEDescriptor>;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BLEDescriptor；  API声明：serviceUuid: string;  差异内容：NA | 类名：BLEDescriptor；  API声明：serviceUuid: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BLEDescriptor；  API声明：characteristicUuid: string;  差异内容：NA | 类名：BLEDescriptor；  API声明：characteristicUuid: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BLEDescriptor；  API声明：descriptorUuid: string;  差异内容：NA | 类名：BLEDescriptor；  API声明：descriptorUuid: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BLEDescriptor；  API声明：descriptorValue: ArrayBuffer;  差异内容：NA | 类名：BLEDescriptor；  API声明：descriptorValue: ArrayBuffer;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：NotifyCharacteristic；  API声明：serviceUuid: string;  差异内容：NA | 类名：NotifyCharacteristic；  API声明：serviceUuid: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：NotifyCharacteristic；  API声明：characteristicUuid: string;  差异内容：NA | 类名：NotifyCharacteristic；  API声明：characteristicUuid: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：NotifyCharacteristic；  API声明：characteristicValue: ArrayBuffer;  差异内容：NA | 类名：NotifyCharacteristic；  API声明：characteristicValue: ArrayBuffer;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：NotifyCharacteristic；  API声明：confirm: boolean;  差异内容：NA | 类名：NotifyCharacteristic；  API声明：confirm: boolean;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：CharacteristicReadReq；  API声明：deviceId: string;  差异内容：NA | 类名：CharacteristicReadReq；  API声明：deviceId: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：CharacteristicReadReq；  API声明：transId: number;  差异内容：NA | 类名：CharacteristicReadReq；  API声明：transId: number;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：CharacteristicReadReq；  API声明：offset: number;  差异内容：NA | 类名：CharacteristicReadReq；  API声明：offset: number;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：CharacteristicReadReq；  API声明：characteristicUuid: string;  差异内容：NA | 类名：CharacteristicReadReq；  API声明：characteristicUuid: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：CharacteristicReadReq；  API声明：serviceUuid: string;  差异内容：NA | 类名：CharacteristicReadReq；  API声明：serviceUuid: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：CharacteristicWriteReq；  API声明：deviceId: string;  差异内容：NA | 类名：CharacteristicWriteReq；  API声明：deviceId: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：CharacteristicWriteReq；  API声明：transId: number;  差异内容：NA | 类名：CharacteristicWriteReq；  API声明：transId: number;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：CharacteristicWriteReq；  API声明：offset: number;  差异内容：NA | 类名：CharacteristicWriteReq；  API声明：offset: number;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：CharacteristicWriteReq；  API声明：isPrep: boolean;  差异内容：NA | 类名：CharacteristicWriteReq；  API声明：isPrep: boolean;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：CharacteristicWriteReq；  API声明：needRsp: boolean;  差异内容：NA | 类名：CharacteristicWriteReq；  API声明：needRsp: boolean;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：CharacteristicWriteReq；  API声明：value: ArrayBuffer;  差异内容：NA | 类名：CharacteristicWriteReq；  API声明：value: ArrayBuffer;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：CharacteristicWriteReq；  API声明：characteristicUuid: string;  差异内容：NA | 类名：CharacteristicWriteReq；  API声明：characteristicUuid: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：CharacteristicWriteReq；  API声明：serviceUuid: string;  差异内容：NA | 类名：CharacteristicWriteReq；  API声明：serviceUuid: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：DescriptorReadReq；  API声明：deviceId: string;  差异内容：NA | 类名：DescriptorReadReq；  API声明：deviceId: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：DescriptorReadReq；  API声明：transId: number;  差异内容：NA | 类名：DescriptorReadReq；  API声明：transId: number;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：DescriptorReadReq；  API声明：offset: number;  差异内容：NA | 类名：DescriptorReadReq；  API声明：offset: number;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：DescriptorReadReq；  API声明：descriptorUuid: string;  差异内容：NA | 类名：DescriptorReadReq；  API声明：descriptorUuid: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：DescriptorReadReq；  API声明：characteristicUuid: string;  差异内容：NA | 类名：DescriptorReadReq；  API声明：characteristicUuid: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：DescriptorReadReq；  API声明：serviceUuid: string;  差异内容：NA | 类名：DescriptorReadReq；  API声明：serviceUuid: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：DescriptorWriteReq；  API声明：deviceId: string;  差异内容：NA | 类名：DescriptorWriteReq；  API声明：deviceId: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：DescriptorWriteReq；  API声明：transId: number;  差异内容：NA | 类名：DescriptorWriteReq；  API声明：transId: number;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：DescriptorWriteReq；  API声明：offset: number;  差异内容：NA | 类名：DescriptorWriteReq；  API声明：offset: number;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：DescriptorWriteReq；  API声明：isPrep: boolean;  差异内容：NA | 类名：DescriptorWriteReq；  API声明：isPrep: boolean;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：DescriptorWriteReq；  API声明：needRsp: boolean;  差异内容：NA | 类名：DescriptorWriteReq；  API声明：needRsp: boolean;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：DescriptorWriteReq；  API声明：value: ArrayBuffer;  差异内容：NA | 类名：DescriptorWriteReq；  API声明：value: ArrayBuffer;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：DescriptorWriteReq；  API声明：descriptorUuid: string;  差异内容：NA | 类名：DescriptorWriteReq；  API声明：descriptorUuid: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：DescriptorWriteReq；  API声明：characteristicUuid: string;  差异内容：NA | 类名：DescriptorWriteReq；  API声明：characteristicUuid: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：DescriptorWriteReq；  API声明：serviceUuid: string;  差异内容：NA | 类名：DescriptorWriteReq；  API声明：serviceUuid: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ServerResponse；  API声明：deviceId: string;  差异内容：NA | 类名：ServerResponse；  API声明：deviceId: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ServerResponse；  API声明：transId: number;  差异内容：NA | 类名：ServerResponse；  API声明：transId: number;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ServerResponse；  API声明：status: number;  差异内容：NA | 类名：ServerResponse；  API声明：status: number;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ServerResponse；  API声明：offset: number;  差异内容：NA | 类名：ServerResponse；  API声明：offset: number;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ServerResponse；  API声明：value: ArrayBuffer;  差异内容：NA | 类名：ServerResponse；  API声明：value: ArrayBuffer;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BLEConnectChangedState；  API声明：deviceId: string;  差异内容：NA | 类名：BLEConnectChangedState；  API声明：deviceId: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BLEConnectChangedState；  API声明：state: ProfileConnectionState;  差异内容：NA | 类名：BLEConnectChangedState；  API声明：state: ProfileConnectionState;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ScanResult；  API声明：deviceId: string;  差异内容：NA | 类名：ScanResult；  API声明：deviceId: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ScanResult；  API声明：rssi: number;  差异内容：NA | 类名：ScanResult；  API声明：rssi: number;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ScanResult；  API声明：data: ArrayBuffer;  差异内容：NA | 类名：ScanResult；  API声明：data: ArrayBuffer;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：AdvertiseSetting；  API声明：interval?: number;  差异内容：NA | 类名：AdvertiseSetting；  API声明：interval?: number;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：AdvertiseSetting；  API声明：txPower?: number;  差异内容：NA | 类名：AdvertiseSetting；  API声明：txPower?: number;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：AdvertiseSetting；  API声明：connectable?: boolean;  差异内容：NA | 类名：AdvertiseSetting；  API声明：connectable?: boolean;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：AdvertiseData；  API声明：serviceUuids: Array<string>;  差异内容：NA | 类名：AdvertiseData；  API声明：serviceUuids: Array<string>;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：AdvertiseData；  API声明：manufactureData: Array<ManufactureData>;  差异内容：NA | 类名：AdvertiseData；  API声明：manufactureData: Array<ManufactureData>;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：AdvertiseData；  API声明：serviceData: Array<ServiceData>;  差异内容：NA | 类名：AdvertiseData；  API声明：serviceData: Array<ServiceData>;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ManufactureData；  API声明：manufactureId: number;  差异内容：NA | 类名：ManufactureData；  API声明：manufactureId: number;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ManufactureData；  API声明：manufactureValue: ArrayBuffer;  差异内容：NA | 类名：ManufactureData；  API声明：manufactureValue: ArrayBuffer;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ServiceData；  API声明：serviceUuid: string;  差异内容：NA | 类名：ServiceData；  API声明：serviceUuid: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ServiceData；  API声明：serviceValue: ArrayBuffer;  差异内容：NA | 类名：ServiceData；  API声明：serviceValue: ArrayBuffer;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ScanFilter；  API声明：deviceId?: string;  差异内容：NA | 类名：ScanFilter；  API声明：deviceId?: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ScanFilter；  API声明：name?: string;  差异内容：NA | 类名：ScanFilter；  API声明：name?: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ScanFilter；  API声明：serviceUuid?: string;  差异内容：NA | 类名：ScanFilter；  API声明：serviceUuid?: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ScanOptions；  API声明：interval?: number;  差异内容：NA | 类名：ScanOptions；  API声明：interval?: number;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ScanOptions；  API声明：dutyMode?: ScanDuty;  差异内容：NA | 类名：ScanOptions；  API声明：dutyMode?: ScanDuty;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ScanOptions；  API声明：matchMode?: MatchMode;  差异内容：NA | 类名：ScanOptions；  API声明：matchMode?: MatchMode;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：SppOption；  API声明：uuid: string;  差异内容：NA | 类名：SppOption；  API声明：uuid: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：SppOption；  API声明：secure: boolean;  差异内容：NA | 类名：SppOption；  API声明：secure: boolean;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：SppOption；  API声明：type: SppType;  差异内容：NA | 类名：SppOption；  API声明：type: SppType;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：PinRequiredParam；  API声明：deviceId: string;  差异内容：NA | 类名：PinRequiredParam；  API声明：deviceId: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：PinRequiredParam；  API声明：pinCode: string;  差异内容：NA | 类名：PinRequiredParam；  API声明：pinCode: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：DeviceClass；  API声明：majorClass: MajorClass;  差异内容：NA | 类名：DeviceClass；  API声明：majorClass: MajorClass;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：DeviceClass；  API声明：majorMinorClass: MajorMinorClass;  差异内容：NA | 类名：DeviceClass；  API声明：majorMinorClass: MajorMinorClass;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：DeviceClass；  API声明：classOfDevice: number;  差异内容：NA | 类名：DeviceClass；  API声明：classOfDevice: number;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BondStateParam；  API声明：deviceId: string;  差异内容：NA | 类名：BondStateParam；  API声明：deviceId: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BondStateParam；  API声明：state: BondState;  差异内容：NA | 类名：BondStateParam；  API声明：state: BondState;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ScanDuty；  API声明：SCAN\_MODE\_LOW\_POWER = 0  差异内容：NA | 类名：ScanDuty；  API声明：SCAN\_MODE\_LOW\_POWER = 0  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ScanDuty；  API声明：SCAN\_MODE\_BALANCED = 1  差异内容：NA | 类名：ScanDuty；  API声明：SCAN\_MODE\_BALANCED = 1  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ScanDuty；  API声明：SCAN\_MODE\_LOW\_LATENCY = 2  差异内容：NA | 类名：ScanDuty；  API声明：SCAN\_MODE\_LOW\_LATENCY = 2  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MatchMode；  API声明：MATCH\_MODE\_AGGRESSIVE = 1  差异内容：NA | 类名：MatchMode；  API声明：MATCH\_MODE\_AGGRESSIVE = 1  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MatchMode；  API声明：MATCH\_MODE\_STICKY = 2  差异内容：NA | 类名：MatchMode；  API声明：MATCH\_MODE\_STICKY = 2  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ProfileConnectionState；  API声明：STATE\_DISCONNECTED = 0  差异内容：NA | 类名：ProfileConnectionState；  API声明：STATE\_DISCONNECTED = 0  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ProfileConnectionState；  API声明：STATE\_CONNECTING = 1  差异内容：NA | 类名：ProfileConnectionState；  API声明：STATE\_CONNECTING = 1  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ProfileConnectionState；  API声明：STATE\_CONNECTED = 2  差异内容：NA | 类名：ProfileConnectionState；  API声明：STATE\_CONNECTED = 2  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ProfileConnectionState；  API声明：STATE\_DISCONNECTING = 3  差异内容：NA | 类名：ProfileConnectionState；  API声明：STATE\_DISCONNECTING = 3  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BluetoothState；  API声明：STATE\_OFF = 0  差异内容：NA | 类名：BluetoothState；  API声明：STATE\_OFF = 0  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BluetoothState；  API声明：STATE\_TURNING\_ON = 1  差异内容：NA | 类名：BluetoothState；  API声明：STATE\_TURNING\_ON = 1  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BluetoothState；  API声明：STATE\_ON = 2  差异内容：NA | 类名：BluetoothState；  API声明：STATE\_ON = 2  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BluetoothState；  API声明：STATE\_TURNING\_OFF = 3  差异内容：NA | 类名：BluetoothState；  API声明：STATE\_TURNING\_OFF = 3  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BluetoothState；  API声明：STATE\_BLE\_TURNING\_ON = 4  差异内容：NA | 类名：BluetoothState；  API声明：STATE\_BLE\_TURNING\_ON = 4  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BluetoothState；  API声明：STATE\_BLE\_ON = 5  差异内容：NA | 类名：BluetoothState；  API声明：STATE\_BLE\_ON = 5  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BluetoothState；  API声明：STATE\_BLE\_TURNING\_OFF = 6  差异内容：NA | 类名：BluetoothState；  API声明：STATE\_BLE\_TURNING\_OFF = 6  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：SppType；  API声明：SPP\_RFCOMM  差异内容：NA | 类名：SppType；  API声明：SPP\_RFCOMM  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ScanMode；  API声明：SCAN\_MODE\_NONE = 0  差异内容：NA | 类名：ScanMode；  API声明：SCAN\_MODE\_NONE = 0  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ScanMode；  API声明：SCAN\_MODE\_CONNECTABLE = 1  差异内容：NA | 类名：ScanMode；  API声明：SCAN\_MODE\_CONNECTABLE = 1  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ScanMode；  API声明：SCAN\_MODE\_GENERAL\_DISCOVERABLE = 2  差异内容：NA | 类名：ScanMode；  API声明：SCAN\_MODE\_GENERAL\_DISCOVERABLE = 2  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ScanMode；  API声明：SCAN\_MODE\_LIMITED\_DISCOVERABLE = 3  差异内容：NA | 类名：ScanMode；  API声明：SCAN\_MODE\_LIMITED\_DISCOVERABLE = 3  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ScanMode；  API声明：SCAN\_MODE\_CONNECTABLE\_GENERAL\_DISCOVERABLE = 4  差异内容：NA | 类名：ScanMode；  API声明：SCAN\_MODE\_CONNECTABLE\_GENERAL\_DISCOVERABLE = 4  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ScanMode；  API声明：SCAN\_MODE\_CONNECTABLE\_LIMITED\_DISCOVERABLE = 5  差异内容：NA | 类名：ScanMode；  API声明：SCAN\_MODE\_CONNECTABLE\_LIMITED\_DISCOVERABLE = 5  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BondState；  API声明：BOND\_STATE\_INVALID = 0  差异内容：NA | 类名：BondState；  API声明：BOND\_STATE\_INVALID = 0  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BondState；  API声明：BOND\_STATE\_BONDING = 1  差异内容：NA | 类名：BondState；  API声明：BOND\_STATE\_BONDING = 1  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：BondState；  API声明：BOND\_STATE\_BONDED = 2  差异内容：NA | 类名：BondState；  API声明：BOND\_STATE\_BONDED = 2  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_MISC = 0x0000  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_MISC = 0x0000  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_COMPUTER = 0x0100  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_COMPUTER = 0x0100  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_PHONE = 0x0200  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_PHONE = 0x0200  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_NETWORKING = 0x0300  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_NETWORKING = 0x0300  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_AUDIO\_VIDEO = 0x0400  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_AUDIO\_VIDEO = 0x0400  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_PERIPHERAL = 0x0500  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_PERIPHERAL = 0x0500  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_IMAGING = 0x0600  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_IMAGING = 0x0600  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_WEARABLE = 0x0700  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_WEARABLE = 0x0700  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_TOY = 0x0800  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_TOY = 0x0800  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_HEALTH = 0x0900  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_HEALTH = 0x0900  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_UNCATEGORIZED = 0x1F00  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_UNCATEGORIZED = 0x1F00  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：COMPUTER\_UNCATEGORIZED = 0x0100  差异内容：NA | 类名：MajorMinorClass；  API声明：COMPUTER\_UNCATEGORIZED = 0x0100  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：COMPUTER\_DESKTOP = 0x0104  差异内容：NA | 类名：MajorMinorClass；  API声明：COMPUTER\_DESKTOP = 0x0104  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：COMPUTER\_SERVER = 0x0108  差异内容：NA | 类名：MajorMinorClass；  API声明：COMPUTER\_SERVER = 0x0108  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：COMPUTER\_LAPTOP = 0x010C  差异内容：NA | 类名：MajorMinorClass；  API声明：COMPUTER\_LAPTOP = 0x010C  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：COMPUTER\_HANDHELD\_PC\_PDA = 0x0110  差异内容：NA | 类名：MajorMinorClass；  API声明：COMPUTER\_HANDHELD\_PC\_PDA = 0x0110  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：COMPUTER\_PALM\_SIZE\_PC\_PDA = 0x0114  差异内容：NA | 类名：MajorMinorClass；  API声明：COMPUTER\_PALM\_SIZE\_PC\_PDA = 0x0114  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：COMPUTER\_WEARABLE = 0x0118  差异内容：NA | 类名：MajorMinorClass；  API声明：COMPUTER\_WEARABLE = 0x0118  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：COMPUTER\_TABLET = 0x011C  差异内容：NA | 类名：MajorMinorClass；  API声明：COMPUTER\_TABLET = 0x011C  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PHONE\_UNCATEGORIZED = 0x0200  差异内容：NA | 类名：MajorMinorClass；  API声明：PHONE\_UNCATEGORIZED = 0x0200  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PHONE\_CELLULAR = 0x0204  差异内容：NA | 类名：MajorMinorClass；  API声明：PHONE\_CELLULAR = 0x0204  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PHONE\_CORDLESS = 0x0208  差异内容：NA | 类名：MajorMinorClass；  API声明：PHONE\_CORDLESS = 0x0208  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PHONE\_SMART = 0x020C  差异内容：NA | 类名：MajorMinorClass；  API声明：PHONE\_SMART = 0x020C  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PHONE\_MODEM\_OR\_GATEWAY = 0x0210  差异内容：NA | 类名：MajorMinorClass；  API声明：PHONE\_MODEM\_OR\_GATEWAY = 0x0210  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PHONE\_ISDN = 0x0214  差异内容：NA | 类名：MajorMinorClass；  API声明：PHONE\_ISDN = 0x0214  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：NETWORK\_FULLY\_AVAILABLE = 0x0300  差异内容：NA | 类名：MajorMinorClass；  API声明：NETWORK\_FULLY\_AVAILABLE = 0x0300  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：NETWORK\_1\_TO\_17\_UTILIZED = 0x0320  差异内容：NA | 类名：MajorMinorClass；  API声明：NETWORK\_1\_TO\_17\_UTILIZED = 0x0320  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：NETWORK\_17\_TO\_33\_UTILIZED = 0x0340  差异内容：NA | 类名：MajorMinorClass；  API声明：NETWORK\_17\_TO\_33\_UTILIZED = 0x0340  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：NETWORK\_33\_TO\_50\_UTILIZED = 0x0360  差异内容：NA | 类名：MajorMinorClass；  API声明：NETWORK\_33\_TO\_50\_UTILIZED = 0x0360  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：NETWORK\_60\_TO\_67\_UTILIZED = 0x0380  差异内容：NA | 类名：MajorMinorClass；  API声明：NETWORK\_60\_TO\_67\_UTILIZED = 0x0380  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：NETWORK\_67\_TO\_83\_UTILIZED = 0x03A0  差异内容：NA | 类名：MajorMinorClass；  API声明：NETWORK\_67\_TO\_83\_UTILIZED = 0x03A0  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：NETWORK\_83\_TO\_99\_UTILIZED = 0x03C0  差异内容：NA | 类名：MajorMinorClass；  API声明：NETWORK\_83\_TO\_99\_UTILIZED = 0x03C0  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：NETWORK\_NO\_SERVICE = 0x03E0  差异内容：NA | 类名：MajorMinorClass；  API声明：NETWORK\_NO\_SERVICE = 0x03E0  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_UNCATEGORIZED = 0x0400  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_UNCATEGORIZED = 0x0400  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_WEARABLE\_HEADSET = 0x0404  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_WEARABLE\_HEADSET = 0x0404  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_HANDSFREE = 0x0408  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_HANDSFREE = 0x0408  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_MICROPHONE = 0x0410  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_MICROPHONE = 0x0410  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_LOUDSPEAKER = 0x0414  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_LOUDSPEAKER = 0x0414  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_HEADPHONES = 0x0418  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_HEADPHONES = 0x0418  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_PORTABLE\_AUDIO = 0x041C  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_PORTABLE\_AUDIO = 0x041C  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_CAR\_AUDIO = 0x0420  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_CAR\_AUDIO = 0x0420  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_SET\_TOP\_BOX = 0x0424  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_SET\_TOP\_BOX = 0x0424  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_HIFI\_AUDIO = 0x0428  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_HIFI\_AUDIO = 0x0428  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VCR = 0x042C  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VCR = 0x042C  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_CAMERA = 0x0430  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_CAMERA = 0x0430  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_CAMCORDER = 0x0434  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_CAMCORDER = 0x0434  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_MONITOR = 0x0438  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_MONITOR = 0x0438  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_DISPLAY\_AND\_LOUDSPEAKER = 0x043C  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_DISPLAY\_AND\_LOUDSPEAKER = 0x043C  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_CONFERENCING = 0x0440  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_CONFERENCING = 0x0440  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_GAMING\_TOY = 0x0448  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_GAMING\_TOY = 0x0448  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_NON\_KEYBOARD\_NON\_POINTING = 0x0500  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_NON\_KEYBOARD\_NON\_POINTING = 0x0500  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_KEYBOARD = 0x0540  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_KEYBOARD = 0x0540  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_POINTING\_DEVICE = 0x0580  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_POINTING\_DEVICE = 0x0580  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_KEYBOARD\_POINTING = 0x05C0  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_KEYBOARD\_POINTING = 0x05C0  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_UNCATEGORIZED = 0x0500  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_UNCATEGORIZED = 0x0500  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_JOYSTICK = 0x0504  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_JOYSTICK = 0x0504  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_GAMEPAD = 0x0508  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_GAMEPAD = 0x0508  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_REMOTE\_CONTROL = 0x05C0  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_REMOTE\_CONTROL = 0x05C0  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_SENSING\_DEVICE = 0x0510  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_SENSING\_DEVICE = 0x0510  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_DIGITIZER\_TABLET = 0x0514  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_DIGITIZER\_TABLET = 0x0514  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_CARD\_READER = 0x0518  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_CARD\_READER = 0x0518  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_DIGITAL\_PEN = 0x051C  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_DIGITAL\_PEN = 0x051C  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_SCANNER\_RFID = 0x0520  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_SCANNER\_RFID = 0x0520  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_GESTURAL\_INPUT = 0x0522  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_GESTURAL\_INPUT = 0x0522  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：IMAGING\_UNCATEGORIZED = 0x0600  差异内容：NA | 类名：MajorMinorClass；  API声明：IMAGING\_UNCATEGORIZED = 0x0600  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：IMAGING\_DISPLAY = 0x0610  差异内容：NA | 类名：MajorMinorClass；  API声明：IMAGING\_DISPLAY = 0x0610  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：IMAGING\_CAMERA = 0x0620  差异内容：NA | 类名：MajorMinorClass；  API声明：IMAGING\_CAMERA = 0x0620  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：IMAGING\_SCANNER = 0x0640  差异内容：NA | 类名：MajorMinorClass；  API声明：IMAGING\_SCANNER = 0x0640  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：IMAGING\_PRINTER = 0x0680  差异内容：NA | 类名：MajorMinorClass；  API声明：IMAGING\_PRINTER = 0x0680  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：WEARABLE\_UNCATEGORIZED = 0x0700  差异内容：NA | 类名：MajorMinorClass；  API声明：WEARABLE\_UNCATEGORIZED = 0x0700  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：WEARABLE\_WRIST\_WATCH = 0x0704  差异内容：NA | 类名：MajorMinorClass；  API声明：WEARABLE\_WRIST\_WATCH = 0x0704  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：WEARABLE\_PAGER = 0x0708  差异内容：NA | 类名：MajorMinorClass；  API声明：WEARABLE\_PAGER = 0x0708  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：WEARABLE\_JACKET = 0x070C  差异内容：NA | 类名：MajorMinorClass；  API声明：WEARABLE\_JACKET = 0x070C  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：WEARABLE\_HELMET = 0x0710  差异内容：NA | 类名：MajorMinorClass；  API声明：WEARABLE\_HELMET = 0x0710  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：WEARABLE\_GLASSES = 0x0714  差异内容：NA | 类名：MajorMinorClass；  API声明：WEARABLE\_GLASSES = 0x0714  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：TOY\_UNCATEGORIZED = 0x0800  差异内容：NA | 类名：MajorMinorClass；  API声明：TOY\_UNCATEGORIZED = 0x0800  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：TOY\_ROBOT = 0x0804  差异内容：NA | 类名：MajorMinorClass；  API声明：TOY\_ROBOT = 0x0804  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：TOY\_VEHICLE = 0x0808  差异内容：NA | 类名：MajorMinorClass；  API声明：TOY\_VEHICLE = 0x0808  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：TOY\_DOLL\_ACTION\_FIGURE = 0x080C  差异内容：NA | 类名：MajorMinorClass；  API声明：TOY\_DOLL\_ACTION\_FIGURE = 0x080C  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：TOY\_CONTROLLER = 0x0810  差异内容：NA | 类名：MajorMinorClass；  API声明：TOY\_CONTROLLER = 0x0810  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：TOY\_GAME = 0x0814  差异内容：NA | 类名：MajorMinorClass；  API声明：TOY\_GAME = 0x0814  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_UNCATEGORIZED = 0x0900  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_UNCATEGORIZED = 0x0900  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_BLOOD\_PRESSURE = 0x0904  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_BLOOD\_PRESSURE = 0x0904  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_THERMOMETER = 0x0908  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_THERMOMETER = 0x0908  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_WEIGHING = 0x090C  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_WEIGHING = 0x090C  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_GLUCOSE = 0x0910  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_GLUCOSE = 0x0910  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_PULSE\_OXIMETER = 0x0914  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_PULSE\_OXIMETER = 0x0914  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_PULSE\_RATE = 0x0918  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_PULSE\_RATE = 0x0918  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_DATA\_DISPLAY = 0x091C  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_DATA\_DISPLAY = 0x091C  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_STEP\_COUNTER = 0x0920  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_STEP\_COUNTER = 0x0920  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_BODY\_COMPOSITION\_ANALYZER = 0x0924  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_BODY\_COMPOSITION\_ANALYZER = 0x0924  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_PEAK\_FLOW\_MOITOR = 0x0928  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_PEAK\_FLOW\_MOITOR = 0x0928  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_MEDICATION\_MONITOR = 0x092C  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_MEDICATION\_MONITOR = 0x092C  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_KNEE\_PROSTHESIS = 0x0930  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_KNEE\_PROSTHESIS = 0x0930  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_ANKLE\_PROSTHESIS = 0x0934  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_ANKLE\_PROSTHESIS = 0x0934  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_GENERIC\_HEALTH\_MANAGER = 0x0938  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_GENERIC\_HEALTH\_MANAGER = 0x0938  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_PERSONAL\_MOBILITY\_DEVICE = 0x093C  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_PERSONAL\_MOBILITY\_DEVICE = 0x093C  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：StateChangeParam；  API声明：deviceId: string;  差异内容：NA | 类名：StateChangeParam；  API声明：deviceId: string;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：StateChangeParam；  API声明：state: ProfileConnectionState;  差异内容：NA | 类名：StateChangeParam；  API声明：state: ProfileConnectionState;  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：PlayingState；  API声明：STATE\_NOT\_PLAYING  差异内容：NA | 类名：PlayingState；  API声明：STATE\_NOT\_PLAYING  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：PlayingState；  API声明：STATE\_PLAYING  差异内容：NA | 类名：PlayingState；  API声明：STATE\_PLAYING  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ProfileId；  API声明：PROFILE\_A2DP\_SOURCE = 1  差异内容：NA | 类名：ProfileId；  API声明：PROFILE\_A2DP\_SOURCE = 1  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：ProfileId；  API声明：PROFILE\_HANDS\_FREE\_AUDIO\_GATEWAY = 4  差异内容：NA | 类名：ProfileId；  API声明：PROFILE\_HANDS\_FREE\_AUDIO\_GATEWAY = 4  差异内容：9 | api/@ohos.bluetooth.d.ts |
| API废弃版本变更 | 类名：global；  API声明： declare namespace bluetoothManager  差异内容：NA | 类名：global；  API声明： declare namespace bluetoothManager  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function getState(): BluetoothState;  差异内容：NA | 类名：bluetoothManager；  API声明：function getState(): BluetoothState;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function getBtConnectionState(): ProfileConnectionState;  差异内容：NA | 类名：bluetoothManager；  API声明：function getBtConnectionState(): ProfileConnectionState;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function pairDevice(deviceId: string): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function pairDevice(deviceId: string): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function getRemoteDeviceName(deviceId: string): string;  差异内容：NA | 类名：bluetoothManager；  API声明：function getRemoteDeviceName(deviceId: string): string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function getRemoteDeviceClass(deviceId: string): DeviceClass;  差异内容：NA | 类名：bluetoothManager；  API声明：function getRemoteDeviceClass(deviceId: string): DeviceClass;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function enableBluetooth(): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function enableBluetooth(): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function disableBluetooth(): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function disableBluetooth(): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function getLocalName(): string;  差异内容：NA | 类名：bluetoothManager；  API声明：function getLocalName(): string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function getPairedDevices(): Array<string>;  差异内容：NA | 类名：bluetoothManager；  API声明：function getPairedDevices(): Array<string>;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function getProfileConnectionState(profileId: ProfileId): ProfileConnectionState;  差异内容：NA | 类名：bluetoothManager；  API声明：function getProfileConnectionState(profileId: ProfileId): ProfileConnectionState;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function setDevicePairingConfirmation(device: string, accept: boolean): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function setDevicePairingConfirmation(device: string, accept: boolean): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function setLocalName(name: string): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function setLocalName(name: string): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function setBluetoothScanMode(mode: ScanMode, duration: number): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function setBluetoothScanMode(mode: ScanMode, duration: number): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function getBluetoothScanMode(): ScanMode;  差异内容：NA | 类名：bluetoothManager；  API声明：function getBluetoothScanMode(): ScanMode;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function startBluetoothDiscovery(): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function startBluetoothDiscovery(): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function stopBluetoothDiscovery(): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function stopBluetoothDiscovery(): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function on(type: "bluetoothDeviceFind", callback: Callback<Array<string>>): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function on(type: 'bluetoothDeviceFind', callback: Callback<Array<string>>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function off(type: "bluetoothDeviceFind", callback?: Callback<Array<string>>): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function on(type: "bondStateChange", callback: Callback<BondStateParam>): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function on(type: 'bondStateChange', callback: Callback<BondStateParam>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function off(type: "bondStateChange", callback?: Callback<BondStateParam>): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function off(type: 'bondStateChange', callback?: Callback<BondStateParam>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function on(type: "pinRequired", callback: Callback<PinRequiredParam>): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function on(type: 'pinRequired', callback: Callback<PinRequiredParam>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function off(type: "pinRequired", callback?: Callback<PinRequiredParam>): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function off(type: 'pinRequired', callback?: Callback<PinRequiredParam>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function on(type: "stateChange", callback: Callback<BluetoothState>): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function on(type: 'stateChange', callback: Callback<BluetoothState>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function off(type: "stateChange", callback?: Callback<BluetoothState>): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function off(type: 'stateChange', callback?: Callback<BluetoothState>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function sppListen(name: string, option: SppOption, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function sppListen(name: string, option: SppOption, callback: AsyncCallback<number>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function sppAccept(serverSocket: number, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function sppAccept(serverSocket: number, callback: AsyncCallback<number>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function sppConnect(device: string, option: SppOption, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function sppConnect(device: string, option: SppOption, callback: AsyncCallback<number>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function sppCloseServerSocket(socket: number): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function sppCloseServerSocket(socket: number): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function sppCloseClientSocket(socket: number): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function sppCloseClientSocket(socket: number): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function sppWrite(clientSocket: number, data: ArrayBuffer): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function sppWrite(clientSocket: number, data: ArrayBuffer): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function on(type: "sppRead", clientSocket: number, callback: Callback<ArrayBuffer>): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function on(type: 'sppRead', clientSocket: number, callback: Callback<ArrayBuffer>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function off(type: "sppRead", clientSocket: number, callback?: Callback<ArrayBuffer>): void;  差异内容：NA | 类名：bluetoothManager；  API声明：function off(type: 'sppRead', clientSocket: number, callback?: Callback<ArrayBuffer>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明：function getProfileInstance(profileId: ProfileId): A2dpSourceProfile | HandsFreeAudioGatewayProfile | HidHostProfile | PanProfile;  差异内容：NA | 类名：bluetoothManager；  API声明：function getProfileInstance(profileId: ProfileId): A2dpSourceProfile | HandsFreeAudioGatewayProfile | HidHostProfile | PanProfile;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface BaseProfile  差异内容：NA | 类名：bluetoothManager；  API声明： interface BaseProfile  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BaseProfile；  API声明：getConnectionDevices(): Array<string>;  差异内容：NA | 类名：BaseProfile；  API声明：getConnectionDevices(): Array<string>;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BaseProfile；  API声明：getDeviceState(device: string): ProfileConnectionState;  差异内容：NA | 类名：BaseProfile；  API声明：getDeviceState(device: string): ProfileConnectionState;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface A2dpSourceProfile  差异内容：NA | 类名：bluetoothManager；  API声明： interface A2dpSourceProfile  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：A2dpSourceProfile；  API声明：connect(device: string): void;  差异内容：NA | 类名：A2dpSourceProfile；  API声明：connect(device: string): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：A2dpSourceProfile；  API声明：disconnect(device: string): void;  差异内容：NA | 类名：A2dpSourceProfile；  API声明：disconnect(device: string): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：A2dpSourceProfile；  API声明：on(type: "connectionStateChange", callback: Callback<StateChangeParam>): void;  差异内容：NA | 类名：A2dpSourceProfile；  API声明：on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：A2dpSourceProfile；  API声明：off(type: "connectionStateChange", callback?: Callback<StateChangeParam>): void;  差异内容：NA | 类名：A2dpSourceProfile；  API声明：off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：A2dpSourceProfile；  API声明：getPlayingState(device: string): PlayingState;  差异内容：NA | 类名：A2dpSourceProfile；  API声明：getPlayingState(device: string): PlayingState;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface HandsFreeAudioGatewayProfile  差异内容：NA | 类名：bluetoothManager；  API声明： interface HandsFreeAudioGatewayProfile  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：HandsFreeAudioGatewayProfile；  API声明：connect(device: string): void;  差异内容：NA | 类名：HandsFreeAudioGatewayProfile；  API声明：connect(device: string): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：HandsFreeAudioGatewayProfile；  API声明：disconnect(device: string): void;  差异内容：NA | 类名：HandsFreeAudioGatewayProfile；  API声明：disconnect(device: string): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：HandsFreeAudioGatewayProfile；  API声明：on(type: "connectionStateChange", callback: Callback<StateChangeParam>): void;  差异内容：NA | 类名：HandsFreeAudioGatewayProfile；  API声明：on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：HandsFreeAudioGatewayProfile；  API声明：off(type: "connectionStateChange", callback?: Callback<StateChangeParam>): void;  差异内容：NA | 类名：HandsFreeAudioGatewayProfile；  API声明：off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface HidHostProfile  差异内容：NA | 类名：bluetoothManager；  API声明： interface HidHostProfile  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：HidHostProfile；  API声明：on(type: "connectionStateChange", callback: Callback<StateChangeParam>): void;  差异内容：NA | 类名：HidHostProfile；  API声明：on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：HidHostProfile；  API声明：off(type: "connectionStateChange", callback?: Callback<StateChangeParam>): void;  差异内容：NA | 类名：HidHostProfile；  API声明：off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface PanProfile  差异内容：NA | 类名：bluetoothManager；  API声明： interface PanProfile  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：PanProfile；  API声明：on(type: "connectionStateChange", callback: Callback<StateChangeParam>): void;  差异内容：NA | 类名：PanProfile；  API声明：on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：PanProfile；  API声明：off(type: "connectionStateChange", callback?: Callback<StateChangeParam>): void;  差异内容：NA | 类名：PanProfile；  API声明：off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： namespace BLE  差异内容：NA | 类名：bluetoothManager；  API声明： namespace BLE  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BLE；  API声明：function createGattServer(): GattServer;  差异内容：NA | 类名：BLE；  API声明：function createGattServer(): GattServer;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BLE；  API声明：function createGattClientDevice(deviceId: string): GattClientDevice;  差异内容：NA | 类名：BLE；  API声明：function createGattClientDevice(deviceId: string): GattClientDevice;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BLE；  API声明：function getConnectedBLEDevices(): Array<string>;  差异内容：NA | 类名：BLE；  API声明：function getConnectedBLEDevices(): Array<string>;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BLE；  API声明：function startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void;  差异内容：NA | 类名：BLE；  API声明：function startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BLE；  API声明：function stopBLEScan(): void;  差异内容：NA | 类名：BLE；  API声明：function stopBLEScan(): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BLE；  API声明：function on(type: "BLEDeviceFind", callback: Callback<Array<ScanResult>>): void;  差异内容：NA | 类名：BLE；  API声明：function on(type: 'BLEDeviceFind', callback: Callback<Array<ScanResult>>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BLE；  API声明：function off(type: "BLEDeviceFind", callback?: Callback<Array<ScanResult>>): void;  差异内容：NA | 类名：BLE；  API声明：function off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface GattServer  差异内容：NA | 类名：bluetoothManager；  API声明： interface GattServer  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattServer；  API声明：startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void;  差异内容：NA | 类名：GattServer；  API声明：startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattServer；  API声明：stopAdvertising(): void;  差异内容：NA | 类名：GattServer；  API声明：stopAdvertising(): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattServer；  API声明：addService(service: GattService): void;  差异内容：NA | 类名：GattServer；  API声明：addService(service: GattService): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattServer；  API声明：removeService(serviceUuid: string): void;  差异内容：NA | 类名：GattServer；  API声明：removeService(serviceUuid: string): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattServer；  API声明：close(): void;  差异内容：NA | 类名：GattServer；  API声明：close(): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattServer；  API声明：notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic): void;  差异内容：NA | 类名：GattServer；  API声明：notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattServer；  API声明：sendResponse(serverResponse: ServerResponse): void;  差异内容：NA | 类名：GattServer；  API声明：sendResponse(serverResponse: ServerResponse): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattServer；  API声明：on(type: "characteristicRead", callback: Callback<CharacteristicReadRequest>): void;  差异内容：NA | 类名：GattServer；  API声明：on(type: 'characteristicRead', callback: Callback<CharacteristicReadRequest>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattServer；  API声明：off(type: "characteristicRead", callback?: Callback<CharacteristicReadRequest>): void;  差异内容：NA | 类名：GattServer；  API声明：off(type: 'characteristicRead', callback?: Callback<CharacteristicReadRequest>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattServer；  API声明：on(type: "characteristicWrite", callback: Callback<CharacteristicWriteRequest>): void;  差异内容：NA | 类名：GattServer；  API声明：on(type: 'characteristicWrite', callback: Callback<CharacteristicWriteRequest>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattServer；  API声明：off(type: "characteristicWrite", callback?: Callback<CharacteristicWriteRequest>): void;  差异内容：NA | 类名：GattServer；  API声明：off(type: 'characteristicWrite', callback?: Callback<CharacteristicWriteRequest>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattServer；  API声明：on(type: "descriptorRead", callback: Callback<DescriptorReadRequest>): void;  差异内容：NA | 类名：GattServer；  API声明：on(type: 'descriptorRead', callback: Callback<DescriptorReadRequest>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattServer；  API声明：off(type: "descriptorRead", callback?: Callback<DescriptorReadRequest>): void;  差异内容：NA | 类名：GattServer；  API声明：off(type: 'descriptorRead', callback?: Callback<DescriptorReadRequest>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattServer；  API声明：on(type: "descriptorWrite", callback: Callback<DescriptorWriteRequest>): void;  差异内容：NA | 类名：GattServer；  API声明：on(type: 'descriptorWrite', callback: Callback<DescriptorWriteRequest>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattServer；  API声明：off(type: "descriptorWrite", callback?: Callback<DescriptorWriteRequest>): void;  差异内容：NA | 类名：GattServer；  API声明：off(type: 'descriptorWrite', callback?: Callback<DescriptorWriteRequest>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattServer；  API声明：on(type: "connectStateChange", callback: Callback<BLEConnectChangedState>): void;  差异内容：NA | 类名：GattServer；  API声明：on(type: 'connectStateChange', callback: Callback<BLEConnectChangedState>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattServer；  API声明：off(type: "connectStateChange", callback?: Callback<BLEConnectChangedState>): void;  差异内容：NA | 类名：GattServer；  API声明：off(type: 'connectStateChange', callback?: Callback<BLEConnectChangedState>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface GattClientDevice  差异内容：NA | 类名：bluetoothManager；  API声明： interface GattClientDevice  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：connect(): void;  差异内容：NA | 类名：GattClientDevice；  API声明：connect(): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：disconnect(): void;  差异内容：NA | 类名：GattClientDevice；  API声明：disconnect(): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：close(): void;  差异内容：NA | 类名：GattClientDevice；  API声明：close(): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：getDeviceName(callback: AsyncCallback<string>): void;  差异内容：NA | 类名：GattClientDevice；  API声明：getDeviceName(callback: AsyncCallback<string>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：getDeviceName(): Promise<string>;  差异内容：NA | 类名：GattClientDevice；  API声明：getDeviceName(): Promise<string>;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：getServices(callback: AsyncCallback<Array<GattService>>): void;  差异内容：NA | 类名：GattClientDevice；  API声明：getServices(callback: AsyncCallback<Array<GattService>>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：getServices(): Promise<Array<GattService>>;  差异内容：NA | 类名：GattClientDevice；  API声明：getServices(): Promise<Array<GattService>>;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：readCharacteristicValue(characteristic: BLECharacteristic, callback: AsyncCallback<BLECharacteristic>): void;  差异内容：NA | 类名：GattClientDevice；  API声明：readCharacteristicValue(characteristic: BLECharacteristic, callback: AsyncCallback<BLECharacteristic>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>;  差异内容：NA | 类名：GattClientDevice；  API声明：readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：readDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<BLEDescriptor>): void;  差异内容：NA | 类名：GattClientDevice；  API声明：readDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<BLEDescriptor>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>;  差异内容：NA | 类名：GattClientDevice；  API声明：readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：writeCharacteristicValue(characteristic: BLECharacteristic): void;  差异内容：NA | 类名：GattClientDevice；  API声明：writeCharacteristicValue(characteristic: BLECharacteristic): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：writeDescriptorValue(descriptor: BLEDescriptor): void;  差异内容：NA | 类名：GattClientDevice；  API声明：writeDescriptorValue(descriptor: BLEDescriptor): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：getRssiValue(callback: AsyncCallback<number>): void;  差异内容：NA | 类名：GattClientDevice；  API声明：getRssiValue(callback: AsyncCallback<number>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：getRssiValue(): Promise<number>;  差异内容：NA | 类名：GattClientDevice；  API声明：getRssiValue(): Promise<number>;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：setBLEMtuSize(mtu: number): void;  差异内容：NA | 类名：GattClientDevice；  API声明：setBLEMtuSize(mtu: number): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：setNotifyCharacteristicChanged(characteristic: BLECharacteristic, enable: boolean): void;  差异内容：NA | 类名：GattClientDevice；  API声明：setNotifyCharacteristicChanged(characteristic: BLECharacteristic, enable: boolean): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：on(type: "BLECharacteristicChange", callback: Callback<BLECharacteristic>): void;  差异内容：NA | 类名：GattClientDevice；  API声明：on(type: 'BLECharacteristicChange', callback: Callback<BLECharacteristic>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：off(type: "BLECharacteristicChange", callback?: Callback<BLECharacteristic>): void;  差异内容：NA | 类名：GattClientDevice；  API声明：off(type: 'BLECharacteristicChange', callback?: Callback<BLECharacteristic>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：on(type: "BLEConnectionStateChange", callback: Callback<BLEConnectChangedState>): void;  差异内容：NA | 类名：GattClientDevice；  API声明：on(type: 'BLEConnectionStateChange', callback: Callback<BLEConnectChangedState>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattClientDevice；  API声明：off(type: "BLEConnectionStateChange", callback?: Callback<BLEConnectChangedState>): void;  差异内容：NA | 类名：GattClientDevice；  API声明：off(type: 'BLEConnectionStateChange', callback?: Callback<BLEConnectChangedState>): void;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface GattService  差异内容：NA | 类名：bluetoothManager；  API声明： interface GattService  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattService；  API声明：serviceUuid: string;  差异内容：NA | 类名：GattService；  API声明：serviceUuid: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattService；  API声明：isPrimary: boolean;  差异内容：NA | 类名：GattService；  API声明：isPrimary: boolean;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattService；  API声明：characteristics: Array<BLECharacteristic>;  差异内容：NA | 类名：GattService；  API声明：characteristics: Array<BLECharacteristic>;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：GattService；  API声明：includeServices?: Array<GattService>;  差异内容：NA | 类名：GattService；  API声明：includeServices?: Array<GattService>;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface BLECharacteristic  差异内容：NA | 类名：bluetoothManager；  API声明： interface BLECharacteristic  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BLECharacteristic；  API声明：serviceUuid: string;  差异内容：NA | 类名：BLECharacteristic；  API声明：serviceUuid: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BLECharacteristic；  API声明：characteristicUuid: string;  差异内容：NA | 类名：BLECharacteristic；  API声明：characteristicUuid: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BLECharacteristic；  API声明：characteristicValue: ArrayBuffer;  差异内容：NA | 类名：BLECharacteristic；  API声明：characteristicValue: ArrayBuffer;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BLECharacteristic；  API声明：descriptors: Array<BLEDescriptor>;  差异内容：NA | 类名：BLECharacteristic；  API声明：descriptors: Array<BLEDescriptor>;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface BLEDescriptor  差异内容：NA | 类名：bluetoothManager；  API声明： interface BLEDescriptor  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BLEDescriptor；  API声明：serviceUuid: string;  差异内容：NA | 类名：BLEDescriptor；  API声明：serviceUuid: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BLEDescriptor；  API声明：characteristicUuid: string;  差异内容：NA | 类名：BLEDescriptor；  API声明：characteristicUuid: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BLEDescriptor；  API声明：descriptorUuid: string;  差异内容：NA | 类名：BLEDescriptor；  API声明：descriptorUuid: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BLEDescriptor；  API声明：descriptorValue: ArrayBuffer;  差异内容：NA | 类名：BLEDescriptor；  API声明：descriptorValue: ArrayBuffer;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface NotifyCharacteristic  差异内容：NA | 类名：bluetoothManager；  API声明： interface NotifyCharacteristic  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：NotifyCharacteristic；  API声明：serviceUuid: string;  差异内容：NA | 类名：NotifyCharacteristic；  API声明：serviceUuid: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：NotifyCharacteristic；  API声明：characteristicUuid: string;  差异内容：NA | 类名：NotifyCharacteristic；  API声明：characteristicUuid: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：NotifyCharacteristic；  API声明：characteristicValue: ArrayBuffer;  差异内容：NA | 类名：NotifyCharacteristic；  API声明：characteristicValue: ArrayBuffer;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：NotifyCharacteristic；  API声明：confirm: boolean;  差异内容：NA | 类名：NotifyCharacteristic；  API声明：confirm: boolean;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface CharacteristicReadRequest  差异内容：NA | 类名：bluetoothManager；  API声明： interface CharacteristicReadRequest  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：CharacteristicReadRequest；  API声明：deviceId: string;  差异内容：NA | 类名：CharacteristicReadRequest；  API声明：deviceId: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：CharacteristicReadRequest；  API声明：transId: number;  差异内容：NA | 类名：CharacteristicReadRequest；  API声明：transId: number;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：CharacteristicReadRequest；  API声明：offset: number;  差异内容：NA | 类名：CharacteristicReadRequest；  API声明：offset: number;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：CharacteristicReadRequest；  API声明：characteristicUuid: string;  差异内容：NA | 类名：CharacteristicReadRequest；  API声明：characteristicUuid: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：CharacteristicReadRequest；  API声明：serviceUuid: string;  差异内容：NA | 类名：CharacteristicReadRequest；  API声明：serviceUuid: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface CharacteristicWriteRequest  差异内容：NA | 类名：bluetoothManager；  API声明： interface CharacteristicWriteRequest  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：CharacteristicWriteRequest；  API声明：deviceId: string;  差异内容：NA | 类名：CharacteristicWriteRequest；  API声明：deviceId: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：CharacteristicWriteRequest；  API声明：transId: number;  差异内容：NA | 类名：CharacteristicWriteRequest；  API声明：transId: number;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：CharacteristicWriteRequest；  API声明：offset: number;  差异内容：NA | 类名：CharacteristicWriteRequest；  API声明：offset: number;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：CharacteristicWriteRequest；  API声明：isPrep: boolean;  差异内容：NA | 类名：CharacteristicWriteRequest；  API声明：isPrep: boolean;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：CharacteristicWriteRequest；  API声明：needRsp: boolean;  差异内容：NA | 类名：CharacteristicWriteRequest；  API声明：needRsp: boolean;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：CharacteristicWriteRequest；  API声明：value: ArrayBuffer;  差异内容：NA | 类名：CharacteristicWriteRequest；  API声明：value: ArrayBuffer;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：CharacteristicWriteRequest；  API声明：characteristicUuid: string;  差异内容：NA | 类名：CharacteristicWriteRequest；  API声明：characteristicUuid: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：CharacteristicWriteRequest；  API声明：serviceUuid: string;  差异内容：NA | 类名：CharacteristicWriteRequest；  API声明：serviceUuid: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface DescriptorReadRequest  差异内容：NA | 类名：bluetoothManager；  API声明： interface DescriptorReadRequest  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：DescriptorReadRequest；  API声明：deviceId: string;  差异内容：NA | 类名：DescriptorReadRequest；  API声明：deviceId: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：DescriptorReadRequest；  API声明：transId: number;  差异内容：NA | 类名：DescriptorReadRequest；  API声明：transId: number;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：DescriptorReadRequest；  API声明：offset: number;  差异内容：NA | 类名：DescriptorReadRequest；  API声明：offset: number;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：DescriptorReadRequest；  API声明：descriptorUuid: string;  差异内容：NA | 类名：DescriptorReadRequest；  API声明：descriptorUuid: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：DescriptorReadRequest；  API声明：characteristicUuid: string;  差异内容：NA | 类名：DescriptorReadRequest；  API声明：characteristicUuid: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：DescriptorReadRequest；  API声明：serviceUuid: string;  差异内容：NA | 类名：DescriptorReadRequest；  API声明：serviceUuid: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface DescriptorWriteRequest  差异内容：NA | 类名：bluetoothManager；  API声明： interface DescriptorWriteRequest  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：DescriptorWriteRequest；  API声明：deviceId: string;  差异内容：NA | 类名：DescriptorWriteRequest；  API声明：deviceId: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：DescriptorWriteRequest；  API声明：transId: number;  差异内容：NA | 类名：DescriptorWriteRequest；  API声明：transId: number;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：DescriptorWriteRequest；  API声明：offset: number;  差异内容：NA | 类名：DescriptorWriteRequest；  API声明：offset: number;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：DescriptorWriteRequest；  API声明：isPrep: boolean;  差异内容：NA | 类名：DescriptorWriteRequest；  API声明：isPrep: boolean;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：DescriptorWriteRequest；  API声明：needRsp: boolean;  差异内容：NA | 类名：DescriptorWriteRequest；  API声明：needRsp: boolean;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：DescriptorWriteRequest；  API声明：value: ArrayBuffer;  差异内容：NA | 类名：DescriptorWriteRequest；  API声明：value: ArrayBuffer;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：DescriptorWriteRequest；  API声明：descriptorUuid: string;  差异内容：NA | 类名：DescriptorWriteRequest；  API声明：descriptorUuid: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：DescriptorWriteRequest；  API声明：characteristicUuid: string;  差异内容：NA | 类名：DescriptorWriteRequest；  API声明：characteristicUuid: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：DescriptorWriteRequest；  API声明：serviceUuid: string;  差异内容：NA | 类名：DescriptorWriteRequest；  API声明：serviceUuid: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface ServerResponse  差异内容：NA | 类名：bluetoothManager；  API声明： interface ServerResponse  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ServerResponse；  API声明：deviceId: string;  差异内容：NA | 类名：ServerResponse；  API声明：deviceId: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ServerResponse；  API声明：transId: number;  差异内容：NA | 类名：ServerResponse；  API声明：transId: number;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ServerResponse；  API声明：status: number;  差异内容：NA | 类名：ServerResponse；  API声明：status: number;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ServerResponse；  API声明：offset: number;  差异内容：NA | 类名：ServerResponse；  API声明：offset: number;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ServerResponse；  API声明：value: ArrayBuffer;  差异内容：NA | 类名：ServerResponse；  API声明：value: ArrayBuffer;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface BLEConnectChangedState  差异内容：NA | 类名：bluetoothManager；  API声明： interface BLEConnectChangedState  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BLEConnectChangedState；  API声明：deviceId: string;  差异内容：NA | 类名：BLEConnectChangedState；  API声明：deviceId: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BLEConnectChangedState；  API声明：state: ProfileConnectionState;  差异内容：NA | 类名：BLEConnectChangedState；  API声明：state: ProfileConnectionState;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface ScanResult  差异内容：NA | 类名：bluetoothManager；  API声明： interface ScanResult  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanResult；  API声明：deviceId: string;  差异内容：NA | 类名：ScanResult；  API声明：deviceId: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanResult；  API声明：rssi: number;  差异内容：NA | 类名：ScanResult；  API声明：rssi: number;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanResult；  API声明：data: ArrayBuffer;  差异内容：NA | 类名：ScanResult；  API声明：data: ArrayBuffer;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface AdvertiseSetting  差异内容：NA | 类名：bluetoothManager；  API声明： interface AdvertiseSetting  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：AdvertiseSetting；  API声明：interval?: number;  差异内容：NA | 类名：AdvertiseSetting；  API声明：interval?: number;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：AdvertiseSetting；  API声明：txPower?: number;  差异内容：NA | 类名：AdvertiseSetting；  API声明：txPower?: number;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：AdvertiseSetting；  API声明：connectable?: boolean;  差异内容：NA | 类名：AdvertiseSetting；  API声明：connectable?: boolean;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface AdvertiseData  差异内容：NA | 类名：bluetoothManager；  API声明： interface AdvertiseData  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：AdvertiseData；  API声明：serviceUuids: Array<string>;  差异内容：NA | 类名：AdvertiseData；  API声明：serviceUuids: Array<string>;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：AdvertiseData；  API声明：manufactureData: Array<ManufactureData>;  差异内容：NA | 类名：AdvertiseData；  API声明：manufactureData: Array<ManufactureData>;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：AdvertiseData；  API声明：serviceData: Array<ServiceData>;  差异内容：NA | 类名：AdvertiseData；  API声明：serviceData: Array<ServiceData>;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface ManufactureData  差异内容：NA | 类名：bluetoothManager；  API声明： interface ManufactureData  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ManufactureData；  API声明：manufactureId: number;  差异内容：NA | 类名：ManufactureData；  API声明：manufactureId: number;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ManufactureData；  API声明：manufactureValue: ArrayBuffer;  差异内容：NA | 类名：ManufactureData；  API声明：manufactureValue: ArrayBuffer;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface ServiceData  差异内容：NA | 类名：bluetoothManager；  API声明： interface ServiceData  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ServiceData；  API声明：serviceUuid: string;  差异内容：NA | 类名：ServiceData；  API声明：serviceUuid: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ServiceData；  API声明：serviceValue: ArrayBuffer;  差异内容：NA | 类名：ServiceData；  API声明：serviceValue: ArrayBuffer;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface ScanFilter  差异内容：NA | 类名：bluetoothManager；  API声明： interface ScanFilter  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanFilter；  API声明：deviceId?: string;  差异内容：NA | 类名：ScanFilter；  API声明：deviceId?: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanFilter；  API声明：name?: string;  差异内容：NA | 类名：ScanFilter；  API声明：name?: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanFilter；  API声明：serviceUuid?: string;  差异内容：NA | 类名：ScanFilter；  API声明：serviceUuid?: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanFilter；  API声明：serviceUuidMask?: string;  差异内容：NA | 类名：ScanFilter；  API声明：serviceUuidMask?: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanFilter；  API声明：serviceSolicitationUuid?: string;  差异内容：NA | 类名：ScanFilter；  API声明：serviceSolicitationUuid?: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanFilter；  API声明：serviceSolicitationUuidMask?: string;  差异内容：NA | 类名：ScanFilter；  API声明：serviceSolicitationUuidMask?: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanFilter；  API声明：serviceData?: ArrayBuffer;  差异内容：NA | 类名：ScanFilter；  API声明：serviceData?: ArrayBuffer;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanFilter；  API声明：serviceDataMask?: ArrayBuffer;  差异内容：NA | 类名：ScanFilter；  API声明：serviceDataMask?: ArrayBuffer;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanFilter；  API声明：manufactureId?: number;  差异内容：NA | 类名：ScanFilter；  API声明：manufactureId?: number;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanFilter；  API声明：manufactureData?: ArrayBuffer;  差异内容：NA | 类名：ScanFilter；  API声明：manufactureData?: ArrayBuffer;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanFilter；  API声明：manufactureDataMask?: ArrayBuffer;  差异内容：NA | 类名：ScanFilter；  API声明：manufactureDataMask?: ArrayBuffer;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface ScanOptions  差异内容：NA | 类名：bluetoothManager；  API声明： interface ScanOptions  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanOptions；  API声明：interval?: number;  差异内容：NA | 类名：ScanOptions；  API声明：interval?: number;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanOptions；  API声明：dutyMode?: ScanDuty;  差异内容：NA | 类名：ScanOptions；  API声明：dutyMode?: ScanDuty;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanOptions；  API声明：matchMode?: MatchMode;  差异内容：NA | 类名：ScanOptions；  API声明：matchMode?: MatchMode;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface SppOption  差异内容：NA | 类名：bluetoothManager；  API声明： interface SppOption  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：SppOption；  API声明：uuid: string;  差异内容：NA | 类名：SppOption；  API声明：uuid: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：SppOption；  API声明：secure: boolean;  差异内容：NA | 类名：SppOption；  API声明：secure: boolean;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：SppOption；  API声明：type: SppType;  差异内容：NA | 类名：SppOption；  API声明：type: SppType;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface PinRequiredParam  差异内容：NA | 类名：bluetoothManager；  API声明： interface PinRequiredParam  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：PinRequiredParam；  API声明：deviceId: string;  差异内容：NA | 类名：PinRequiredParam；  API声明：deviceId: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：PinRequiredParam；  API声明：pinCode: string;  差异内容：NA | 类名：PinRequiredParam；  API声明：pinCode: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface DeviceClass  差异内容：NA | 类名：bluetoothManager；  API声明： interface DeviceClass  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：DeviceClass；  API声明：majorClass: MajorClass;  差异内容：NA | 类名：DeviceClass；  API声明：majorClass: MajorClass;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：DeviceClass；  API声明：majorMinorClass: MajorMinorClass;  差异内容：NA | 类名：DeviceClass；  API声明：majorMinorClass: MajorMinorClass;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：DeviceClass；  API声明：classOfDevice: number;  差异内容：NA | 类名：DeviceClass；  API声明：classOfDevice: number;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface BondStateParam  差异内容：NA | 类名：bluetoothManager；  API声明： interface BondStateParam  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BondStateParam；  API声明：deviceId: string;  差异内容：NA | 类名：BondStateParam；  API声明：deviceId: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BondStateParam；  API声明：state: BondState;  差异内容：NA | 类名：BondStateParam；  API声明：state: BondState;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： interface StateChangeParam  差异内容：NA | 类名：bluetoothManager；  API声明： interface StateChangeParam  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：StateChangeParam；  API声明：deviceId: string;  差异内容：NA | 类名：StateChangeParam；  API声明：deviceId: string;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：StateChangeParam；  API声明：state: ProfileConnectionState;  差异内容：NA | 类名：StateChangeParam；  API声明：state: ProfileConnectionState;  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： enum ScanDuty  差异内容：NA | 类名：bluetoothManager；  API声明： enum ScanDuty  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanDuty；  API声明：SCAN\_MODE\_LOW\_POWER = 0  差异内容：NA | 类名：ScanDuty；  API声明：SCAN\_MODE\_LOW\_POWER = 0  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanDuty；  API声明：SCAN\_MODE\_BALANCED = 1  差异内容：NA | 类名：ScanDuty；  API声明：SCAN\_MODE\_BALANCED = 1  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanDuty；  API声明：SCAN\_MODE\_LOW\_LATENCY = 2  差异内容：NA | 类名：ScanDuty；  API声明：SCAN\_MODE\_LOW\_LATENCY = 2  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： enum MatchMode  差异内容：NA | 类名：bluetoothManager；  API声明： enum MatchMode  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MatchMode；  API声明：MATCH\_MODE\_AGGRESSIVE = 1  差异内容：NA | 类名：MatchMode；  API声明：MATCH\_MODE\_AGGRESSIVE = 1  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MatchMode；  API声明：MATCH\_MODE\_STICKY = 2  差异内容：NA | 类名：MatchMode；  API声明：MATCH\_MODE\_STICKY = 2  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： enum ProfileConnectionState  差异内容：NA | 类名：bluetoothManager；  API声明： enum ProfileConnectionState  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ProfileConnectionState；  API声明：STATE\_DISCONNECTED = 0  差异内容：NA | 类名：ProfileConnectionState；  API声明：STATE\_DISCONNECTED = 0  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ProfileConnectionState；  API声明：STATE\_CONNECTING = 1  差异内容：NA | 类名：ProfileConnectionState；  API声明：STATE\_CONNECTING = 1  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ProfileConnectionState；  API声明：STATE\_CONNECTED = 2  差异内容：NA | 类名：ProfileConnectionState；  API声明：STATE\_CONNECTED = 2  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ProfileConnectionState；  API声明：STATE\_DISCONNECTING = 3  差异内容：NA | 类名：ProfileConnectionState；  API声明：STATE\_DISCONNECTING = 3  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： enum BluetoothState  差异内容：NA | 类名：bluetoothManager；  API声明： enum BluetoothState  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BluetoothState；  API声明：STATE\_OFF = 0  差异内容：NA | 类名：BluetoothState；  API声明：STATE\_OFF = 0  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BluetoothState；  API声明：STATE\_TURNING\_ON = 1  差异内容：NA | 类名：BluetoothState；  API声明：STATE\_TURNING\_ON = 1  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BluetoothState；  API声明：STATE\_ON = 2  差异内容：NA | 类名：BluetoothState；  API声明：STATE\_ON = 2  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BluetoothState；  API声明：STATE\_TURNING\_OFF = 3  差异内容：NA | 类名：BluetoothState；  API声明：STATE\_TURNING\_OFF = 3  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BluetoothState；  API声明：STATE\_BLE\_TURNING\_ON = 4  差异内容：NA | 类名：BluetoothState；  API声明：STATE\_BLE\_TURNING\_ON = 4  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BluetoothState；  API声明：STATE\_BLE\_ON = 5  差异内容：NA | 类名：BluetoothState；  API声明：STATE\_BLE\_ON = 5  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BluetoothState；  API声明：STATE\_BLE\_TURNING\_OFF = 6  差异内容：NA | 类名：BluetoothState；  API声明：STATE\_BLE\_TURNING\_OFF = 6  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： enum SppType  差异内容：NA | 类名：bluetoothManager；  API声明： enum SppType  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：SppType；  API声明：SPP\_RFCOMM  差异内容：NA | 类名：SppType；  API声明：SPP\_RFCOMM  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： enum ScanMode  差异内容：NA | 类名：bluetoothManager；  API声明： enum ScanMode  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanMode；  API声明：SCAN\_MODE\_NONE = 0  差异内容：NA | 类名：ScanMode；  API声明：SCAN\_MODE\_NONE = 0  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanMode；  API声明：SCAN\_MODE\_CONNECTABLE = 1  差异内容：NA | 类名：ScanMode；  API声明：SCAN\_MODE\_CONNECTABLE = 1  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanMode；  API声明：SCAN\_MODE\_GENERAL\_DISCOVERABLE = 2  差异内容：NA | 类名：ScanMode；  API声明：SCAN\_MODE\_GENERAL\_DISCOVERABLE = 2  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanMode；  API声明：SCAN\_MODE\_LIMITED\_DISCOVERABLE = 3  差异内容：NA | 类名：ScanMode；  API声明：SCAN\_MODE\_LIMITED\_DISCOVERABLE = 3  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanMode；  API声明：SCAN\_MODE\_CONNECTABLE\_GENERAL\_DISCOVERABLE = 4  差异内容：NA | 类名：ScanMode；  API声明：SCAN\_MODE\_CONNECTABLE\_GENERAL\_DISCOVERABLE = 4  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ScanMode；  API声明：SCAN\_MODE\_CONNECTABLE\_LIMITED\_DISCOVERABLE = 5  差异内容：NA | 类名：ScanMode；  API声明：SCAN\_MODE\_CONNECTABLE\_LIMITED\_DISCOVERABLE = 5  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： enum BondState  差异内容：NA | 类名：bluetoothManager；  API声明： enum BondState  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BondState；  API声明：BOND\_STATE\_INVALID = 0  差异内容：NA | 类名：BondState；  API声明：BOND\_STATE\_INVALID = 0  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BondState；  API声明：BOND\_STATE\_BONDING = 1  差异内容：NA | 类名：BondState；  API声明：BOND\_STATE\_BONDING = 1  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：BondState；  API声明：BOND\_STATE\_BONDED = 2  差异内容：NA | 类名：BondState；  API声明：BOND\_STATE\_BONDED = 2  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： enum MajorClass  差异内容：NA | 类名：bluetoothManager；  API声明： enum MajorClass  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_MISC = 0x0000  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_MISC = 0x0000  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_COMPUTER = 0x0100  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_COMPUTER = 0x0100  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_PHONE = 0x0200  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_PHONE = 0x0200  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_NETWORKING = 0x0300  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_NETWORKING = 0x0300  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_AUDIO\_VIDEO = 0x0400  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_AUDIO\_VIDEO = 0x0400  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_PERIPHERAL = 0x0500  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_PERIPHERAL = 0x0500  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_IMAGING = 0x0600  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_IMAGING = 0x0600  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_WEARABLE = 0x0700  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_WEARABLE = 0x0700  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_TOY = 0x0800  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_TOY = 0x0800  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_HEALTH = 0x0900  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_HEALTH = 0x0900  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorClass；  API声明：MAJOR\_UNCATEGORIZED = 0x1F00  差异内容：NA | 类名：MajorClass；  API声明：MAJOR\_UNCATEGORIZED = 0x1F00  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： enum MajorMinorClass  差异内容：NA | 类名：bluetoothManager；  API声明： enum MajorMinorClass  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：COMPUTER\_UNCATEGORIZED = 0x0100  差异内容：NA | 类名：MajorMinorClass；  API声明：COMPUTER\_UNCATEGORIZED = 0x0100  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：COMPUTER\_DESKTOP = 0x0104  差异内容：NA | 类名：MajorMinorClass；  API声明：COMPUTER\_DESKTOP = 0x0104  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：COMPUTER\_SERVER = 0x0108  差异内容：NA | 类名：MajorMinorClass；  API声明：COMPUTER\_SERVER = 0x0108  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：COMPUTER\_LAPTOP = 0x010C  差异内容：NA | 类名：MajorMinorClass；  API声明：COMPUTER\_LAPTOP = 0x010C  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：COMPUTER\_HANDHELD\_PC\_PDA = 0x0110  差异内容：NA | 类名：MajorMinorClass；  API声明：COMPUTER\_HANDHELD\_PC\_PDA = 0x0110  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：COMPUTER\_PALM\_SIZE\_PC\_PDA = 0x0114  差异内容：NA | 类名：MajorMinorClass；  API声明：COMPUTER\_PALM\_SIZE\_PC\_PDA = 0x0114  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：COMPUTER\_WEARABLE = 0x0118  差异内容：NA | 类名：MajorMinorClass；  API声明：COMPUTER\_WEARABLE = 0x0118  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：COMPUTER\_TABLET = 0x011C  差异内容：NA | 类名：MajorMinorClass；  API声明：COMPUTER\_TABLET = 0x011C  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PHONE\_UNCATEGORIZED = 0x0200  差异内容：NA | 类名：MajorMinorClass；  API声明：PHONE\_UNCATEGORIZED = 0x0200  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PHONE\_CELLULAR = 0x0204  差异内容：NA | 类名：MajorMinorClass；  API声明：PHONE\_CELLULAR = 0x0204  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PHONE\_CORDLESS = 0x0208  差异内容：NA | 类名：MajorMinorClass；  API声明：PHONE\_CORDLESS = 0x0208  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PHONE\_SMART = 0x020C  差异内容：NA | 类名：MajorMinorClass；  API声明：PHONE\_SMART = 0x020C  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PHONE\_MODEM\_OR\_GATEWAY = 0x0210  差异内容：NA | 类名：MajorMinorClass；  API声明：PHONE\_MODEM\_OR\_GATEWAY = 0x0210  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PHONE\_ISDN = 0x0214  差异内容：NA | 类名：MajorMinorClass；  API声明：PHONE\_ISDN = 0x0214  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：NETWORK\_FULLY\_AVAILABLE = 0x0300  差异内容：NA | 类名：MajorMinorClass；  API声明：NETWORK\_FULLY\_AVAILABLE = 0x0300  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：NETWORK\_1\_TO\_17\_UTILIZED = 0x0320  差异内容：NA | 类名：MajorMinorClass；  API声明：NETWORK\_1\_TO\_17\_UTILIZED = 0x0320  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：NETWORK\_17\_TO\_33\_UTILIZED = 0x0340  差异内容：NA | 类名：MajorMinorClass；  API声明：NETWORK\_17\_TO\_33\_UTILIZED = 0x0340  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：NETWORK\_33\_TO\_50\_UTILIZED = 0x0360  差异内容：NA | 类名：MajorMinorClass；  API声明：NETWORK\_33\_TO\_50\_UTILIZED = 0x0360  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：NETWORK\_60\_TO\_67\_UTILIZED = 0x0380  差异内容：NA | 类名：MajorMinorClass；  API声明：NETWORK\_60\_TO\_67\_UTILIZED = 0x0380  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：NETWORK\_67\_TO\_83\_UTILIZED = 0x03A0  差异内容：NA | 类名：MajorMinorClass；  API声明：NETWORK\_67\_TO\_83\_UTILIZED = 0x03A0  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：NETWORK\_83\_TO\_99\_UTILIZED = 0x03C0  差异内容：NA | 类名：MajorMinorClass；  API声明：NETWORK\_83\_TO\_99\_UTILIZED = 0x03C0  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：NETWORK\_NO\_SERVICE = 0x03E0  差异内容：NA | 类名：MajorMinorClass；  API声明：NETWORK\_NO\_SERVICE = 0x03E0  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_UNCATEGORIZED = 0x0400  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_UNCATEGORIZED = 0x0400  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_WEARABLE\_HEADSET = 0x0404  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_WEARABLE\_HEADSET = 0x0404  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_HANDSFREE = 0x0408  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_HANDSFREE = 0x0408  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_MICROPHONE = 0x0410  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_MICROPHONE = 0x0410  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_LOUDSPEAKER = 0x0414  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_LOUDSPEAKER = 0x0414  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_HEADPHONES = 0x0418  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_HEADPHONES = 0x0418  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_PORTABLE\_AUDIO = 0x041C  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_PORTABLE\_AUDIO = 0x041C  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_CAR\_AUDIO = 0x0420  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_CAR\_AUDIO = 0x0420  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_SET\_TOP\_BOX = 0x0424  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_SET\_TOP\_BOX = 0x0424  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_HIFI\_AUDIO = 0x0428  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_HIFI\_AUDIO = 0x0428  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VCR = 0x042C  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VCR = 0x042C  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_CAMERA = 0x0430  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_CAMERA = 0x0430  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_CAMCORDER = 0x0434  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_CAMCORDER = 0x0434  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_MONITOR = 0x0438  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_MONITOR = 0x0438  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_DISPLAY\_AND\_LOUDSPEAKER = 0x043C  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_DISPLAY\_AND\_LOUDSPEAKER = 0x043C  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_CONFERENCING = 0x0440  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_CONFERENCING = 0x0440  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_GAMING\_TOY = 0x0448  差异内容：NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_GAMING\_TOY = 0x0448  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_NON\_KEYBOARD\_NON\_POINTING = 0x0500  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_NON\_KEYBOARD\_NON\_POINTING = 0x0500  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_KEYBOARD = 0x0540  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_KEYBOARD = 0x0540  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_POINTING\_DEVICE = 0x0580  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_POINTING\_DEVICE = 0x0580  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_KEYBOARD\_POINTING = 0x05C0  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_KEYBOARD\_POINTING = 0x05C0  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_UNCATEGORIZED = 0x0500  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_UNCATEGORIZED = 0x0500  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_JOYSTICK = 0x0504  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_JOYSTICK = 0x0504  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_GAMEPAD = 0x0508  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_GAMEPAD = 0x0508  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_REMOTE\_CONTROL = 0x05C0  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_REMOTE\_CONTROL = 0x05C0  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_SENSING\_DEVICE = 0x0510  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_SENSING\_DEVICE = 0x0510  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_DIGITIZER\_TABLET = 0x0514  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_DIGITIZER\_TABLET = 0x0514  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_CARD\_READER = 0x0518  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_CARD\_READER = 0x0518  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_DIGITAL\_PEN = 0x051C  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_DIGITAL\_PEN = 0x051C  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_SCANNER\_RFID = 0x0520  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_SCANNER\_RFID = 0x0520  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：PERIPHERAL\_GESTURAL\_INPUT = 0x0522  差异内容：NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_GESTURAL\_INPUT = 0x0522  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：IMAGING\_UNCATEGORIZED = 0x0600  差异内容：NA | 类名：MajorMinorClass；  API声明：IMAGING\_UNCATEGORIZED = 0x0600  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：IMAGING\_DISPLAY = 0x0610  差异内容：NA | 类名：MajorMinorClass；  API声明：IMAGING\_DISPLAY = 0x0610  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：IMAGING\_CAMERA = 0x0620  差异内容：NA | 类名：MajorMinorClass；  API声明：IMAGING\_CAMERA = 0x0620  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：IMAGING\_SCANNER = 0x0640  差异内容：NA | 类名：MajorMinorClass；  API声明：IMAGING\_SCANNER = 0x0640  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：IMAGING\_PRINTER = 0x0680  差异内容：NA | 类名：MajorMinorClass；  API声明：IMAGING\_PRINTER = 0x0680  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：WEARABLE\_UNCATEGORIZED = 0x0700  差异内容：NA | 类名：MajorMinorClass；  API声明：WEARABLE\_UNCATEGORIZED = 0x0700  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：WEARABLE\_WRIST\_WATCH = 0x0704  差异内容：NA | 类名：MajorMinorClass；  API声明：WEARABLE\_WRIST\_WATCH = 0x0704  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：WEARABLE\_PAGER = 0x0708  差异内容：NA | 类名：MajorMinorClass；  API声明：WEARABLE\_PAGER = 0x0708  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：WEARABLE\_JACKET = 0x070C  差异内容：NA | 类名：MajorMinorClass；  API声明：WEARABLE\_JACKET = 0x070C  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：WEARABLE\_HELMET = 0x0710  差异内容：NA | 类名：MajorMinorClass；  API声明：WEARABLE\_HELMET = 0x0710  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：WEARABLE\_GLASSES = 0x0714  差异内容：NA | 类名：MajorMinorClass；  API声明：WEARABLE\_GLASSES = 0x0714  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：TOY\_UNCATEGORIZED = 0x0800  差异内容：NA | 类名：MajorMinorClass；  API声明：TOY\_UNCATEGORIZED = 0x0800  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：TOY\_ROBOT = 0x0804  差异内容：NA | 类名：MajorMinorClass；  API声明：TOY\_ROBOT = 0x0804  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：TOY\_VEHICLE = 0x0808  差异内容：NA | 类名：MajorMinorClass；  API声明：TOY\_VEHICLE = 0x0808  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：TOY\_DOLL\_ACTION\_FIGURE = 0x080C  差异内容：NA | 类名：MajorMinorClass；  API声明：TOY\_DOLL\_ACTION\_FIGURE = 0x080C  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：TOY\_CONTROLLER = 0x0810  差异内容：NA | 类名：MajorMinorClass；  API声明：TOY\_CONTROLLER = 0x0810  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：TOY\_GAME = 0x0814  差异内容：NA | 类名：MajorMinorClass；  API声明：TOY\_GAME = 0x0814  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_UNCATEGORIZED = 0x0900  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_UNCATEGORIZED = 0x0900  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_BLOOD\_PRESSURE = 0x0904  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_BLOOD\_PRESSURE = 0x0904  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_THERMOMETER = 0x0908  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_THERMOMETER = 0x0908  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_WEIGHING = 0x090C  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_WEIGHING = 0x090C  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_GLUCOSE = 0x0910  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_GLUCOSE = 0x0910  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_PULSE\_OXIMETER = 0x0914  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_PULSE\_OXIMETER = 0x0914  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_PULSE\_RATE = 0x0918  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_PULSE\_RATE = 0x0918  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_DATA\_DISPLAY = 0x091C  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_DATA\_DISPLAY = 0x091C  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_STEP\_COUNTER = 0x0920  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_STEP\_COUNTER = 0x0920  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_BODY\_COMPOSITION\_ANALYZER = 0x0924  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_BODY\_COMPOSITION\_ANALYZER = 0x0924  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_PEAK\_FLOW\_MONITOR = 0x0928  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_PEAK\_FLOW\_MONITOR = 0x0928  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_MEDICATION\_MONITOR = 0x092C  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_MEDICATION\_MONITOR = 0x092C  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_KNEE\_PROSTHESIS = 0x0930  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_KNEE\_PROSTHESIS = 0x0930  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_ANKLE\_PROSTHESIS = 0x0934  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_ANKLE\_PROSTHESIS = 0x0934  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_GENERIC\_HEALTH\_MANAGER = 0x0938  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_GENERIC\_HEALTH\_MANAGER = 0x0938  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：MajorMinorClass；  API声明：HEALTH\_PERSONAL\_MOBILITY\_DEVICE = 0x093C  差异内容：NA | 类名：MajorMinorClass；  API声明：HEALTH\_PERSONAL\_MOBILITY\_DEVICE = 0x093C  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： enum PlayingState  差异内容：NA | 类名：bluetoothManager；  API声明： enum PlayingState  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：PlayingState；  API声明：STATE\_NOT\_PLAYING  差异内容：NA | 类名：PlayingState；  API声明：STATE\_NOT\_PLAYING  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：PlayingState；  API声明：STATE\_PLAYING  差异内容：NA | 类名：PlayingState；  API声明：STATE\_PLAYING  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：bluetoothManager；  API声明： enum ProfileId  差异内容：NA | 类名：bluetoothManager；  API声明： enum ProfileId  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ProfileId；  API声明：PROFILE\_A2DP\_SOURCE = 1  差异内容：NA | 类名：ProfileId；  API声明：PROFILE\_A2DP\_SOURCE = 1  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ProfileId；  API声明：PROFILE\_HANDS\_FREE\_AUDIO\_GATEWAY = 4  差异内容：NA | 类名：ProfileId；  API声明：PROFILE\_HANDS\_FREE\_AUDIO\_GATEWAY = 4  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ProfileId；  API声明：PROFILE\_HID\_HOST = 6  差异内容：NA | 类名：ProfileId；  API声明：PROFILE\_HID\_HOST = 6  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：ProfileId；  API声明：PROFILE\_PAN\_NETWORK = 7  差异内容：NA | 类名：ProfileId；  API声明：PROFILE\_PAN\_NETWORK = 7  差异内容：10 | api/@ohos.bluetoothManager.d.ts |
| API废弃版本变更 | 类名：connectedTag；  API声明：function readNdefTag(callback: AsyncCallback<string>): void;  差异内容：NA | 类名：connectedTag；  API声明：function readNdefTag(callback: AsyncCallback<string>): void;  差异内容：9 | api/@ohos.connectedTag.d.ts |
| API废弃版本变更 | 类名：connectedTag；  API声明：function writeNdefTag(data: string, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：connectedTag；  API声明：function writeNdefTag(data: string, callback: AsyncCallback<void>): void;  差异内容：9 | api/@ohos.connectedTag.d.ts |
| API废弃版本变更 | 类名：FeatureType；  API声明：HCE = 0  差异内容：NA | 类名：FeatureType；  API声明：HCE = 0  差异内容：9 | api/@ohos.nfc.cardEmulation.d.ts |
| API废弃版本变更 | 类名：FeatureType；  API声明：UICC = 1  差异内容：NA | 类名：FeatureType；  API声明：UICC = 1  差异内容：9 | api/@ohos.nfc.cardEmulation.d.ts |
| API废弃版本变更 | 类名：FeatureType；  API声明：ESE = 2  差异内容：NA | 类名：FeatureType；  API声明：ESE = 2  差异内容：9 | api/@ohos.nfc.cardEmulation.d.ts |
| API废弃版本变更 | 类名：wifi；  API声明：function getScanInfos(callback: AsyncCallback<Array<WifiScanInfo>>): void;  差异内容：NA | 类名：wifi；  API声明：function getScanInfos(callback: AsyncCallback<Array<WifiScanInfo>>): void;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：wifi；  API声明：function addUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：wifi；  API声明：function addUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：wifi；  API声明：function removeUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：wifi；  API声明：function removeUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：wifi；  API声明：function getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void;  差异内容：NA | 类名：wifi；  API声明：function getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：wifi；  API声明：function getP2pLinkedInfo(callback: AsyncCallback<WifiP2pLinkedInfo>): void;  差异内容：NA | 类名：wifi；  API声明：function getP2pLinkedInfo(callback: AsyncCallback<WifiP2pLinkedInfo>): void;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：wifi；  API声明：function getCurrentGroup(callback: AsyncCallback<WifiP2pGroupInfo>): void;  差异内容：NA | 类名：wifi；  API声明：function getCurrentGroup(callback: AsyncCallback<WifiP2pGroupInfo>): void;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：wifi；  API声明：function getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice[]>): void;  差异内容：NA | 类名：wifi；  API声明：function getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice[]>): void;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiDeviceConfig；  API声明：ssid: string;  差异内容：NA | 类名：WifiDeviceConfig；  API声明：ssid: string;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiDeviceConfig；  API声明：bssid: string;  差异内容：NA | 类名：WifiDeviceConfig；  API声明：bssid: string;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiDeviceConfig；  API声明：preSharedKey: string;  差异内容：NA | 类名：WifiDeviceConfig；  API声明：preSharedKey: string;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiDeviceConfig；  API声明：isHiddenSsid: boolean;  差异内容：NA | 类名：WifiDeviceConfig；  API声明：isHiddenSsid: boolean;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiDeviceConfig；  API声明：securityType: WifiSecurityType;  差异内容：NA | 类名：WifiDeviceConfig；  API声明：securityType: WifiSecurityType;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiScanInfo；  API声明：ssid: string;  差异内容：NA | 类名：WifiScanInfo；  API声明：ssid: string;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiScanInfo；  API声明：bssid: string;  差异内容：NA | 类名：WifiScanInfo；  API声明：bssid: string;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiScanInfo；  API声明：capabilities: string;  差异内容：NA | 类名：WifiScanInfo；  API声明：capabilities: string;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiScanInfo；  API声明：securityType: WifiSecurityType;  差异内容：NA | 类名：WifiScanInfo；  API声明：securityType: WifiSecurityType;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiScanInfo；  API声明：rssi: number;  差异内容：NA | 类名：WifiScanInfo；  API声明：rssi: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiScanInfo；  API声明：band: number;  差异内容：NA | 类名：WifiScanInfo；  API声明：band: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiScanInfo；  API声明：frequency: number;  差异内容：NA | 类名：WifiScanInfo；  API声明：frequency: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiScanInfo；  API声明：channelWidth: number;  差异内容：NA | 类名：WifiScanInfo；  API声明：channelWidth: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiScanInfo；  API声明：timestamp: number;  差异内容：NA | 类名：WifiScanInfo；  API声明：timestamp: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiSecurityType；  API声明：WIFI\_SEC\_TYPE\_INVALID = 0  差异内容：NA | 类名：WifiSecurityType；  API声明：WIFI\_SEC\_TYPE\_INVALID = 0  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiSecurityType；  API声明：WIFI\_SEC\_TYPE\_OPEN = 1  差异内容：NA | 类名：WifiSecurityType；  API声明：WIFI\_SEC\_TYPE\_OPEN = 1  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiSecurityType；  API声明：WIFI\_SEC\_TYPE\_WEP = 2  差异内容：NA | 类名：WifiSecurityType；  API声明：WIFI\_SEC\_TYPE\_WEP = 2  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiSecurityType；  API声明：WIFI\_SEC\_TYPE\_PSK = 3  差异内容：NA | 类名：WifiSecurityType；  API声明：WIFI\_SEC\_TYPE\_PSK = 3  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiSecurityType；  API声明：WIFI\_SEC\_TYPE\_SAE = 4  差异内容：NA | 类名：WifiSecurityType；  API声明：WIFI\_SEC\_TYPE\_SAE = 4  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiLinkedInfo；  API声明：ssid: string;  差异内容：NA | 类名：WifiLinkedInfo；  API声明：ssid: string;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiLinkedInfo；  API声明：bssid: string;  差异内容：NA | 类名：WifiLinkedInfo；  API声明：bssid: string;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiLinkedInfo；  API声明：rssi: number;  差异内容：NA | 类名：WifiLinkedInfo；  API声明：rssi: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiLinkedInfo；  API声明：band: number;  差异内容：NA | 类名：WifiLinkedInfo；  API声明：band: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiLinkedInfo；  API声明：linkSpeed: number;  差异内容：NA | 类名：WifiLinkedInfo；  API声明：linkSpeed: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiLinkedInfo；  API声明：frequency: number;  差异内容：NA | 类名：WifiLinkedInfo；  API声明：frequency: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiLinkedInfo；  API声明：isHidden: boolean;  差异内容：NA | 类名：WifiLinkedInfo；  API声明：isHidden: boolean;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiLinkedInfo；  API声明：isRestricted: boolean;  差异内容：NA | 类名：WifiLinkedInfo；  API声明：isRestricted: boolean;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiLinkedInfo；  API声明：macAddress: string;  差异内容：NA | 类名：WifiLinkedInfo；  API声明：macAddress: string;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiLinkedInfo；  API声明：ipAddress: number;  差异内容：NA | 类名：WifiLinkedInfo；  API声明：ipAddress: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiLinkedInfo；  API声明：connState: ConnState;  差异内容：NA | 类名：WifiLinkedInfo；  API声明：connState: ConnState;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：IpInfo；  API声明：ipAddress: number;  差异内容：NA | 类名：IpInfo；  API声明：ipAddress: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：IpInfo；  API声明：gateway: number;  差异内容：NA | 类名：IpInfo；  API声明：gateway: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：IpInfo；  API声明：netmask: number;  差异内容：NA | 类名：IpInfo；  API声明：netmask: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：IpInfo；  API声明：primaryDns: number;  差异内容：NA | 类名：IpInfo；  API声明：primaryDns: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：IpInfo；  API声明：secondDns: number;  差异内容：NA | 类名：IpInfo；  API声明：secondDns: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：IpInfo；  API声明：serverIp: number;  差异内容：NA | 类名：IpInfo；  API声明：serverIp: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：IpInfo；  API声明：leaseDuration: number;  差异内容：NA | 类名：IpInfo；  API声明：leaseDuration: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：ConnState；  API声明：SCANNING  差异内容：NA | 类名：ConnState；  API声明：SCANNING  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：ConnState；  API声明：CONNECTING  差异内容：NA | 类名：ConnState；  API声明：CONNECTING  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：ConnState；  API声明：AUTHENTICATING  差异内容：NA | 类名：ConnState；  API声明：AUTHENTICATING  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：ConnState；  API声明：OBTAINING\_IPADDR  差异内容：NA | 类名：ConnState；  API声明：OBTAINING\_IPADDR  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：ConnState；  API声明：CONNECTED  差异内容：NA | 类名：ConnState；  API声明：CONNECTED  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：ConnState；  API声明：DISCONNECTING  差异内容：NA | 类名：ConnState；  API声明：DISCONNECTING  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：ConnState；  API声明：DISCONNECTED  差异内容：NA | 类名：ConnState；  API声明：DISCONNECTED  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：ConnState；  API声明：UNKNOWN  差异内容：NA | 类名：ConnState；  API声明：UNKNOWN  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2pDevice；  API声明：deviceName: string;  差异内容：NA | 类名：WifiP2pDevice；  API声明：deviceName: string;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2pDevice；  API声明：deviceAddress: string;  差异内容：NA | 类名：WifiP2pDevice；  API声明：deviceAddress: string;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2pDevice；  API声明：primaryDeviceType: string;  差异内容：NA | 类名：WifiP2pDevice；  API声明：primaryDeviceType: string;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2pDevice；  API声明：deviceStatus: P2pDeviceStatus;  差异内容：NA | 类名：WifiP2pDevice；  API声明：deviceStatus: P2pDeviceStatus;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2pDevice；  API声明：groupCapabilitys: number;  差异内容：NA | 类名：WifiP2pDevice；  API声明：groupCapabilitys: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2PConfig；  API声明：deviceAddress: string;  差异内容：NA | 类名：WifiP2PConfig；  API声明：deviceAddress: string;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2PConfig；  API声明：netId: number;  差异内容：NA | 类名：WifiP2PConfig；  API声明：netId: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2PConfig；  API声明：passphrase: string;  差异内容：NA | 类名：WifiP2PConfig；  API声明：passphrase: string;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2PConfig；  API声明：groupName: string;  差异内容：NA | 类名：WifiP2PConfig；  API声明：groupName: string;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2PConfig；  API声明：goBand: GroupOwnerBand;  差异内容：NA | 类名：WifiP2PConfig；  API声明：goBand: GroupOwnerBand;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2pGroupInfo；  API声明：isP2pGo: boolean;  差异内容：NA | 类名：WifiP2pGroupInfo；  API声明：isP2pGo: boolean;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2pGroupInfo；  API声明：ownerInfo: WifiP2pDevice;  差异内容：NA | 类名：WifiP2pGroupInfo；  API声明：ownerInfo: WifiP2pDevice;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2pGroupInfo；  API声明：passphrase: string;  差异内容：NA | 类名：WifiP2pGroupInfo；  API声明：passphrase: string;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2pGroupInfo；  API声明：interface: string;  差异内容：NA | 类名：WifiP2pGroupInfo；  API声明：interface: string;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2pGroupInfo；  API声明：groupName: string;  差异内容：NA | 类名：WifiP2pGroupInfo；  API声明：groupName: string;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2pGroupInfo；  API声明：networkId: number;  差异内容：NA | 类名：WifiP2pGroupInfo；  API声明：networkId: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2pGroupInfo；  API声明：frequency: number;  差异内容：NA | 类名：WifiP2pGroupInfo；  API声明：frequency: number;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2pGroupInfo；  API声明：clientDevices: WifiP2pDevice[];  差异内容：NA | 类名：WifiP2pGroupInfo；  API声明：clientDevices: WifiP2pDevice[];  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2pGroupInfo；  API声明：goIpAddress: string;  差异内容：NA | 类名：WifiP2pGroupInfo；  API声明：goIpAddress: string;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：P2pConnectState；  API声明：DISCONNECTED = 0  差异内容：NA | 类名：P2pConnectState；  API声明：DISCONNECTED = 0  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：P2pConnectState；  API声明：CONNECTED = 1  差异内容：NA | 类名：P2pConnectState；  API声明：CONNECTED = 1  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2pLinkedInfo；  API声明：connectState: P2pConnectState;  差异内容：NA | 类名：WifiP2pLinkedInfo；  API声明：connectState: P2pConnectState;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2pLinkedInfo；  API声明：isGroupOwner: boolean;  差异内容：NA | 类名：WifiP2pLinkedInfo；  API声明：isGroupOwner: boolean;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：WifiP2pLinkedInfo；  API声明：groupOwnerAddr: string;  差异内容：NA | 类名：WifiP2pLinkedInfo；  API声明：groupOwnerAddr: string;  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：P2pDeviceStatus；  API声明：CONNECTED = 0  差异内容：NA | 类名：P2pDeviceStatus；  API声明：CONNECTED = 0  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：P2pDeviceStatus；  API声明：INVITED = 1  差异内容：NA | 类名：P2pDeviceStatus；  API声明：INVITED = 1  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：P2pDeviceStatus；  API声明：FAILED = 2  差异内容：NA | 类名：P2pDeviceStatus；  API声明：FAILED = 2  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：P2pDeviceStatus；  API声明：AVAILABLE = 3  差异内容：NA | 类名：P2pDeviceStatus；  API声明：AVAILABLE = 3  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：P2pDeviceStatus；  API声明：UNAVAILABLE = 4  差异内容：NA | 类名：P2pDeviceStatus；  API声明：UNAVAILABLE = 4  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：GroupOwnerBand；  API声明：GO\_BAND\_AUTO = 0  差异内容：NA | 类名：GroupOwnerBand；  API声明：GO\_BAND\_AUTO = 0  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：GroupOwnerBand；  API声明：GO\_BAND\_2GHZ = 1  差异内容：NA | 类名：GroupOwnerBand；  API声明：GO\_BAND\_2GHZ = 1  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：GroupOwnerBand；  API声明：GO\_BAND\_5GHZ = 2  差异内容：NA | 类名：GroupOwnerBand；  API声明：GO\_BAND\_5GHZ = 2  差异内容：9 | api/@ohos.wifi.d.ts |
| API废弃版本变更 | 类名：wifiext；  API声明：function getSupportedPowerModel(callback: AsyncCallback<Array<PowerModel>>): void;  差异内容：NA | 类名：wifiext；  API声明：function getSupportedPowerModel(callback: AsyncCallback<Array<PowerModel>>): void;  差异内容：9 | api/@ohos.wifiext.d.ts |
| API废弃版本变更 | 类名：wifiext；  API声明：function getPowerModel(callback: AsyncCallback<PowerModel>): void;  差异内容：NA | 类名：wifiext；  API声明：function getPowerModel(callback: AsyncCallback<PowerModel>): void;  差异内容：9 | api/@ohos.wifiext.d.ts |
| API废弃版本变更 | 类名：PowerModel；  API声明：SLEEPING = 0  差异内容：NA | 类名：PowerModel；  API声明：SLEEPING = 0  差异内容：9 | api/@ohos.wifiext.d.ts |
| API废弃版本变更 | 类名：PowerModel；  API声明：GENERAL = 1  差异内容：NA | 类名：PowerModel；  API声明：GENERAL = 1  差异内容：9 | api/@ohos.wifiext.d.ts |
| API废弃版本变更 | 类名：PowerModel；  API声明：THROUGH\_WALL = 2  差异内容：NA | 类名：PowerModel；  API声明：THROUGH\_WALL = 2  差异内容：9 | api/@ohos.wifiext.d.ts |
| API废弃版本变更 | 类名：wifiManager；  API声明：function scan(): void;  差异内容：NA | 类名：wifiManager；  API声明：function scan(): void;  差异内容：10 | api/@ohos.wifiManager.d.ts |
| API废弃版本变更 | 类名：wifiManager；  API声明：function getScanResults(): Promise<Array<WifiScanInfo>>;  差异内容：NA | 类名：wifiManager；  API声明：function getScanResults(): Promise<Array<WifiScanInfo>>;  差异内容：10 | api/@ohos.wifiManager.d.ts |
| API废弃版本变更 | 类名：wifiManager；  API声明：function getScanResults(callback: AsyncCallback<Array<WifiScanInfo>>): void;  差异内容：NA | 类名：wifiManager；  API声明：function getScanResults(callback: AsyncCallback<Array<WifiScanInfo>>): void;  差异内容：10 | api/@ohos.wifiManager.d.ts |
| API废弃版本变更 | 类名：wifiManager；  API声明：function getScanResultsSync(): Array<WifiScanInfo>;  差异内容：NA | 类名：wifiManager；  API声明：function getScanResultsSync(): Array<WifiScanInfo>;  差异内容：10 | api/@ohos.wifiManager.d.ts |
| API废弃版本变更 | 类名：wifiManagerExt；  API声明：function enableHotspot(): void;  差异内容：NA | 类名：wifiManagerExt；  API声明：function enableHotspot(): void;  差异内容：10 | api/@ohos.wifiManagerExt.d.ts |
| API废弃版本变更 | 类名：wifiManagerExt；  API声明：function disableHotspot(): void;  差异内容：NA | 类名：wifiManagerExt；  API声明：function disableHotspot(): void;  差异内容：10 | api/@ohos.wifiManagerExt.d.ts |
| API废弃版本变更 | 类名：wifiManagerExt；  API声明：function setPowerMode(mode: PowerMode): void;  差异内容：NA | 类名：wifiManagerExt；  API声明：function setPowerMode(mode: PowerMode): void;  差异内容：10 | api/@ohos.wifiManagerExt.d.ts |
| API废弃版本变更 | 类名：TagSession；  API声明：sendData(data: number[], callback: AsyncCallback<number[]>): void;  差异内容：NA | 类名：TagSession；  API声明：sendData(data: number[], callback: AsyncCallback<number[]>): void;  差异内容：9 | api/tag/tagSession.d.ts |
| 错误码变更 | 类名：GattClientDevice；  API声明：getDeviceName(): Promise<string>;  差异内容：NA | 类名：GattClientDevice；  API声明：getDeviceName(): Promise<string>;  差异内容：201,2900001,2900099,401,801 | api/@ohos.bluetoothManager.d.ts |
| 错误码变更 | 类名：GattClientDevice；  API声明：getServices(): Promise<Array<GattService>>;  差异内容：NA | 类名：GattClientDevice；  API声明：getServices(): Promise<Array<GattService>>;  差异内容：201,2900001,2900099,401,801 | api/@ohos.bluetoothManager.d.ts |
| 错误码变更 | 类名：GattClientDevice；  API声明：readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>;  差异内容：NA | 类名：GattClientDevice；  API声明：readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>;  差异内容：201,2900001,2900099,2901000,401,801 | api/@ohos.bluetoothManager.d.ts |
| 错误码变更 | 类名：GattClientDevice；  API声明：readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>;  差异内容：NA | 类名：GattClientDevice；  API声明：readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>;  差异内容：201,2900001,2900099,2901000,401,801 | api/@ohos.bluetoothManager.d.ts |
| 错误码变更 | 类名：GattClientDevice；  API声明：getRssiValue(): Promise<number>;  差异内容：NA | 类名：GattClientDevice；  API声明：getRssiValue(): Promise<number>;  差异内容：201,2900099,401,801 | api/@ohos.bluetoothManager.d.ts |
| 错误码变更 | 类名：connectedTag；  API声明：function read(callback: AsyncCallback<number[]>): void;  差异内容：NA | 类名：connectedTag；  API声明：function read(callback: AsyncCallback<number[]>): void;  差异内容：201,3200101,801 | api/@ohos.connectedTag.d.ts |
| 错误码变更 | 类名：connectedTag；  API声明：function write(data: number[], callback: AsyncCallback<void>): void;  差异内容：NA | 类名：connectedTag；  API声明：function write(data: number[], callback: AsyncCallback<void>): void;  差异内容：201,3200101,401,801 | api/@ohos.connectedTag.d.ts |
| 错误码变更 | 类名：HceService；  API声明：transmit(response: number[], callback: AsyncCallback<void>): void;  差异内容：NA | 类名：HceService；  API声明：transmit(response: number[], callback: AsyncCallback<void>): void;  差异内容：201,3100301,401,801 | api/@ohos.nfc.cardEmulation.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function getScanResults(callback: AsyncCallback<Array<WifiScanInfo>>): void;  差异内容：NA | 类名：wifiManager；  API声明：function getScanResults(callback: AsyncCallback<Array<WifiScanInfo>>): void;  差异内容：201,2501000,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function addCandidateConfig(config: WifiDeviceConfig, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：wifiManager；  API声明：function addCandidateConfig(config: WifiDeviceConfig, callback: AsyncCallback<number>): void;  差异内容：201,2501000,401,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function removeCandidateConfig(networkId: number, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：wifiManager；  API声明：function removeCandidateConfig(networkId: number, callback: AsyncCallback<void>): void;  差异内容：201,2501000,401,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void;  差异内容：NA | 类名：wifiManager；  API声明：function getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void;  差异内容：201,202,2501000,2501001,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function getP2pLinkedInfo(callback: AsyncCallback<WifiP2pLinkedInfo>): void;  差异内容：NA | 类名：wifiManager；  API声明：function getP2pLinkedInfo(callback: AsyncCallback<WifiP2pLinkedInfo>): void;  差异内容：201,2801000,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function getCurrentGroup(callback: AsyncCallback<WifiP2pGroupInfo>): void;  差异内容：NA | 类名：wifiManager；  API声明：function getCurrentGroup(callback: AsyncCallback<WifiP2pGroupInfo>): void;  差异内容：201,2801000,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice[]>): void;  差异内容：NA | 类名：wifiManager；  API声明：function getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice[]>): void;  差异内容：201,2801000,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager；  API声明：function getP2pLocalDevice(callback: AsyncCallback<WifiP2pDevice>): void;  差异内容：NA | 类名：wifiManager；  API声明：function getP2pLocalDevice(callback: AsyncCallback<WifiP2pDevice>): void;  差异内容：201,2801000,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManagerExt；  API声明：function getSupportedPowerMode(callback: AsyncCallback<Array<PowerMode>>): void;  差异内容：NA | 类名：wifiManagerExt；  API声明：function getSupportedPowerMode(callback: AsyncCallback<Array<PowerMode>>): void;  差异内容：201,2701000,801 | api/@ohos.wifiManagerExt.d.ts |
| 错误码变更 | 类名：wifiManagerExt；  API声明：function getPowerMode(callback: AsyncCallback<PowerMode>): void;  差异内容：NA | 类名：wifiManagerExt；  API声明：function getPowerMode(callback: AsyncCallback<PowerMode>): void;  差异内容：201,2701000,801 | api/@ohos.wifiManagerExt.d.ts |
| 错误码变更 | 类名：IsoDepTag；  API声明：isExtendedApduSupported(callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：IsoDepTag；  API声明：isExtendedApduSupported(callback: AsyncCallback<boolean>): void;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：NdefTag；  API声明：readNdef(callback: AsyncCallback<NdefMessage>): void;  差异内容：NA | 类名：NdefTag；  API声明：readNdef(callback: AsyncCallback<NdefMessage>): void;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：NdefTag；  API声明：writeNdef(msg: NdefMessage, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：NdefTag；  API声明：writeNdef(msg: NdefMessage, callback: AsyncCallback<void>): void;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：NdefTag；  API声明：setReadOnly(callback: AsyncCallback<void>): void;  差异内容：NA | 类名：NdefTag；  API声明：setReadOnly(callback: AsyncCallback<void>): void;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：MifareClassicTag；  API声明：authenticateSector(sectorIndex: number, key: number[], isKeyA: boolean, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：MifareClassicTag；  API声明：authenticateSector(sectorIndex: number, key: number[], isKeyA: boolean, callback: AsyncCallback<void>): void;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：MifareClassicTag；  API声明：readSingleBlock(blockIndex: number, callback: AsyncCallback<number[]>): void;  差异内容：NA | 类名：MifareClassicTag；  API声明：readSingleBlock(blockIndex: number, callback: AsyncCallback<number[]>): void;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：MifareClassicTag；  API声明：writeSingleBlock(blockIndex: number, data: number[], callback: AsyncCallback<void>): void;  差异内容：NA | 类名：MifareClassicTag；  API声明：writeSingleBlock(blockIndex: number, data: number[], callback: AsyncCallback<void>): void;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：MifareClassicTag；  API声明：incrementBlock(blockIndex: number, value: number, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：MifareClassicTag；  API声明：incrementBlock(blockIndex: number, value: number, callback: AsyncCallback<void>): void;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：MifareClassicTag；  API声明：decrementBlock(blockIndex: number, value: number, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：MifareClassicTag；  API声明：decrementBlock(blockIndex: number, value: number, callback: AsyncCallback<void>): void;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：MifareClassicTag；  API声明：transferToBlock(blockIndex: number, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：MifareClassicTag；  API声明：transferToBlock(blockIndex: number, callback: AsyncCallback<void>): void;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：MifareClassicTag；  API声明：restoreFromBlock(blockIndex: number, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：MifareClassicTag；  API声明：restoreFromBlock(blockIndex: number, callback: AsyncCallback<void>): void;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：MifareUltralightTag；  API声明：readMultiplePages(pageIndex: number, callback: AsyncCallback<number[]>): void;  差异内容：NA | 类名：MifareUltralightTag；  API声明：readMultiplePages(pageIndex: number, callback: AsyncCallback<number[]>): void;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：MifareUltralightTag；  API声明：writeSinglePage(pageIndex: number, data: number[], callback: AsyncCallback<void>): void;  差异内容：NA | 类名：MifareUltralightTag；  API声明：writeSinglePage(pageIndex: number, data: number[], callback: AsyncCallback<void>): void;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：NdefFormatableTag；  API声明：format(message: NdefMessage, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：NdefFormatableTag；  API声明：format(message: NdefMessage, callback: AsyncCallback<void>): void;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：NdefFormatableTag；  API声明：formatReadOnly(message: NdefMessage, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：NdefFormatableTag；  API声明：formatReadOnly(message: NdefMessage, callback: AsyncCallback<void>): void;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：TagSession；  API声明：transmit(data: number[], callback: AsyncCallback<number[]>): void;  差异内容：NA | 类名：TagSession；  API声明：transmit(data: number[], callback: AsyncCallback<number[]>): void;  差异内容：201,3100201,3100204,401,801 | api/tag/tagSession.d.ts |
| 错误码变更 | 类名：IsoDepTag；  API声明：isExtendedApduSupported(): Promise<boolean>;  差异内容：201,3100201,401 | 类名：IsoDepTag；  API声明：isExtendedApduSupported(): Promise<boolean>;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：NdefTag；  API声明：readNdef(): Promise<NdefMessage>;  差异内容：201,3100201,401 | 类名：NdefTag；  API声明：readNdef(): Promise<NdefMessage>;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：NdefTag；  API声明：writeNdef(msg: NdefMessage): Promise<void>;  差异内容：201,3100201,401 | 类名：NdefTag；  API声明：writeNdef(msg: NdefMessage): Promise<void>;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：NdefTag；  API声明：setReadOnly(): Promise<void>;  差异内容：201,3100201,401 | 类名：NdefTag；  API声明：setReadOnly(): Promise<void>;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：MifareClassicTag；  API声明：authenticateSector(sectorIndex: number, key: number[], isKeyA: boolean): Promise<void>;  差异内容：201,3100201,401 | 类名：MifareClassicTag；  API声明：authenticateSector(sectorIndex: number, key: number[], isKeyA: boolean): Promise<void>;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：MifareClassicTag；  API声明：readSingleBlock(blockIndex: number): Promise<number[]>;  差异内容：201,3100201,401 | 类名：MifareClassicTag；  API声明：readSingleBlock(blockIndex: number): Promise<number[]>;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：MifareClassicTag；  API声明：writeSingleBlock(blockIndex: number, data: number[]): Promise<void>;  差异内容：201,3100201,401 | 类名：MifareClassicTag；  API声明：writeSingleBlock(blockIndex: number, data: number[]): Promise<void>;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：MifareClassicTag；  API声明：incrementBlock(blockIndex: number, value: number): Promise<void>;  差异内容：201,3100201,401 | 类名：MifareClassicTag；  API声明：incrementBlock(blockIndex: number, value: number): Promise<void>;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：MifareClassicTag；  API声明：decrementBlock(blockIndex: number, value: number): Promise<void>;  差异内容：201,3100201,401 | 类名：MifareClassicTag；  API声明：decrementBlock(blockIndex: number, value: number): Promise<void>;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：MifareClassicTag；  API声明：transferToBlock(blockIndex: number): Promise<void>;  差异内容：201,3100201,401 | 类名：MifareClassicTag；  API声明：transferToBlock(blockIndex: number): Promise<void>;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：MifareClassicTag；  API声明：restoreFromBlock(blockIndex: number): Promise<void>;  差异内容：201,3100201,401 | 类名：MifareClassicTag；  API声明：restoreFromBlock(blockIndex: number): Promise<void>;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：MifareUltralightTag；  API声明：readMultiplePages(pageIndex: number): Promise<number[]>;  差异内容：201,3100201,401 | 类名：MifareUltralightTag；  API声明：readMultiplePages(pageIndex: number): Promise<number[]>;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：MifareUltralightTag；  API声明：writeSinglePage(pageIndex: number, data: number[]): Promise<void>;  差异内容：201,3100201,401 | 类名：MifareUltralightTag；  API声明：writeSinglePage(pageIndex: number, data: number[]): Promise<void>;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：NdefFormatableTag；  API声明：format(message: NdefMessage): Promise<void>;  差异内容：201,3100201,401 | 类名：NdefFormatableTag；  API声明：format(message: NdefMessage): Promise<void>;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：NdefFormatableTag；  API声明：formatReadOnly(message: NdefMessage): Promise<void>;  差异内容：201,3100201,401 | 类名：NdefFormatableTag；  API声明：formatReadOnly(message: NdefMessage): Promise<void>;  差异内容：201,3100201,3100204,401 | api/tag/nfctech.d.ts |
| 错误码变更 | 类名：TagSession；  API声明：transmit(data: number[]): Promise<number[]>;  差异内容：201,3100201,401,801 | 类名：TagSession；  API声明：transmit(data: number[]): Promise<number[]>;  差异内容：201,3100201,3100204,401,801 | api/tag/tagSession.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：getDeviceName(): Promise<string>;  差异内容：NA | 类名：GattClientDevice；  API声明：getDeviceName(): Promise<string>;  差异内容：ohos.permission.USE\_BLUETOOTH | api/@ohos.bluetooth.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：getServices(): Promise<Array<GattService>>;  差异内容：NA | 类名：GattClientDevice；  API声明：getServices(): Promise<Array<GattService>>;  差异内容：ohos.permission.USE\_BLUETOOTH | api/@ohos.bluetooth.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>;  差异内容：NA | 类名：GattClientDevice；  API声明：readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>;  差异内容：ohos.permission.USE\_BLUETOOTH | api/@ohos.bluetooth.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>;  差异内容：NA | 类名：GattClientDevice；  API声明：readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>;  差异内容：ohos.permission.USE\_BLUETOOTH | api/@ohos.bluetooth.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：getRssiValue(): Promise<number>;  差异内容：NA | 类名：GattClientDevice；  API声明：getRssiValue(): Promise<number>;  差异内容：ohos.permission.USE\_BLUETOOTH | api/@ohos.bluetooth.d.ts |
| 权限变更 | 类名：A2dpSourceProfile；  API声明：on(type: "connectionStateChange", callback: Callback<StateChangeParam>): void;  差异内容：NA | 类名：A2dpSourceProfile；  API声明：on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：A2dpSourceProfile；  API声明：off(type: "connectionStateChange", callback?: Callback<StateChangeParam>): void;  差异内容：NA | 类名：A2dpSourceProfile；  API声明：off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：A2dpSourceProfile；  API声明：getPlayingState(device: string): PlayingState;  差异内容：NA | 类名：A2dpSourceProfile；  API声明：getPlayingState(device: string): PlayingState;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：HandsFreeAudioGatewayProfile；  API声明：on(type: "connectionStateChange", callback: Callback<StateChangeParam>): void;  差异内容：NA | 类名：HandsFreeAudioGatewayProfile；  API声明：on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：HandsFreeAudioGatewayProfile；  API声明：off(type: "connectionStateChange", callback?: Callback<StateChangeParam>): void;  差异内容：NA | 类名：HandsFreeAudioGatewayProfile；  API声明：off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：HidHostProfile；  API声明：on(type: "connectionStateChange", callback: Callback<StateChangeParam>): void;  差异内容：NA | 类名：HidHostProfile；  API声明：on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：HidHostProfile；  API声明：off(type: "connectionStateChange", callback?: Callback<StateChangeParam>): void;  差异内容：NA | 类名：HidHostProfile；  API声明：off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：PanProfile；  API声明：on(type: "connectionStateChange", callback: Callback<StateChangeParam>): void;  差异内容：NA | 类名：PanProfile；  API声明：on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：PanProfile；  API声明：off(type: "connectionStateChange", callback?: Callback<StateChangeParam>): void;  差异内容：NA | 类名：PanProfile；  API声明：off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：getDeviceName(): Promise<string>;  差异内容：NA | 类名：GattClientDevice；  API声明：getDeviceName(): Promise<string>;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：getServices(): Promise<Array<GattService>>;  差异内容：NA | 类名：GattClientDevice；  API声明：getServices(): Promise<Array<GattService>>;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>;  差异内容：NA | 类名：GattClientDevice；  API声明：readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>;  差异内容：NA | 类名：GattClientDevice；  API声明：readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：getRssiValue(): Promise<number>;  差异内容：NA | 类名：GattClientDevice；  API声明：getRssiValue(): Promise<number>;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：connectedTag；  API声明：function readNdefTag(callback: AsyncCallback<string>): void;  差异内容：NA | 类名：connectedTag；  API声明：function readNdefTag(callback: AsyncCallback<string>): void;  差异内容：ohos.permission.NFC\_TAG | api/@ohos.connectedTag.d.ts |
| 权限变更 | 类名：connectedTag；  API声明：function read(callback: AsyncCallback<number[]>): void;  差异内容：NA | 类名：connectedTag；  API声明：function read(callback: AsyncCallback<number[]>): void;  差异内容：ohos.permission.NFC\_TAG | api/@ohos.connectedTag.d.ts |
| 权限变更 | 类名：connectedTag；  API声明：function writeNdefTag(data: string, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：connectedTag；  API声明：function writeNdefTag(data: string, callback: AsyncCallback<void>): void;  差异内容：ohos.permission.NFC\_TAG | api/@ohos.connectedTag.d.ts |
| 权限变更 | 类名：connectedTag；  API声明：function write(data: number[], callback: AsyncCallback<void>): void;  差异内容：NA | 类名：connectedTag；  API声明：function write(data: number[], callback: AsyncCallback<void>): void;  差异内容：ohos.permission.NFC\_TAG | api/@ohos.connectedTag.d.ts |
| 权限变更 | 类名：HceService；  API声明：transmit(response: number[], callback: AsyncCallback<void>): void;  差异内容：NA | 类名：HceService；  API声明：transmit(response: number[], callback: AsyncCallback<void>): void;  差异内容：ohos.permission.NFC\_CARD\_EMULATION | api/@ohos.nfc.cardEmulation.d.ts |
| 权限变更 | 类名：TagInfo；  API声明：uid: number[];  差异内容：NA | 类名：TagInfo；  API声明：uid: number[];  差异内容：ohos.permission.NFC\_TAG | api/@ohos.nfc.tag.d.ts |
| 权限变更 | 类名：TagInfo；  API声明：technology: number[];  差异内容：NA | 类名：TagInfo；  API声明：technology: number[];  差异内容：ohos.permission.NFC\_TAG | api/@ohos.nfc.tag.d.ts |
| 权限变更 | 类名：TagInfo；  API声明：supportedProfiles: number[];  差异内容：NA | 类名：TagInfo；  API声明：supportedProfiles: number[];  差异内容：ohos.permission.NFC\_TAG | api/@ohos.nfc.tag.d.ts |
| 权限变更 | 类名：wifi；  API声明：function getScanInfos(callback: AsyncCallback<Array<WifiScanInfo>>): void;  差异内容：NA | 类名：wifi；  API声明：function getScanInfos(callback: AsyncCallback<Array<WifiScanInfo>>): void;  差异内容：ohos.permission.GET\_WIFI\_INFO and (ohos.permission.GET\_WIFI\_PEERS\_MAC or ohos.permission.LOCATION) | api/@ohos.wifi.d.ts |
| 权限变更 | 类名：wifi；  API声明：function addUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：wifi；  API声明：function addUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void;  差异内容：ohos.permission.SET\_WIFI\_INFO | api/@ohos.wifi.d.ts |
| 权限变更 | 类名：wifi；  API声明：function removeUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：wifi；  API声明：function removeUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void;  差异内容：ohos.permission.SET\_WIFI\_INFO | api/@ohos.wifi.d.ts |
| 权限变更 | 类名：wifi；  API声明：function getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void;  差异内容：NA | 类名：wifi；  API声明：function getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void;  差异内容：ohos.permission.GET\_WIFI\_INFO | api/@ohos.wifi.d.ts |
| 权限变更 | 类名：wifi；  API声明：function getP2pLinkedInfo(callback: AsyncCallback<WifiP2pLinkedInfo>): void;  差异内容：NA | 类名：wifi；  API声明：function getP2pLinkedInfo(callback: AsyncCallback<WifiP2pLinkedInfo>): void;  差异内容：ohos.permission.GET\_WIFI\_INFO | api/@ohos.wifi.d.ts |
| 权限变更 | 类名：wifi；  API声明：function getCurrentGroup(callback: AsyncCallback<WifiP2pGroupInfo>): void;  差异内容：NA | 类名：wifi；  API声明：function getCurrentGroup(callback: AsyncCallback<WifiP2pGroupInfo>): void;  差异内容：ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION | api/@ohos.wifi.d.ts |
| 权限变更 | 类名：wifi；  API声明：function getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice[]>): void;  差异内容：NA | 类名：wifi；  API声明：function getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice[]>): void;  差异内容：ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION | api/@ohos.wifi.d.ts |
| 权限变更 | 类名：wifiext；  API声明：function getSupportedPowerModel(callback: AsyncCallback<Array<PowerModel>>): void;  差异内容：NA | 类名：wifiext；  API声明：function getSupportedPowerModel(callback: AsyncCallback<Array<PowerModel>>): void;  差异内容：ohos.permission.GET\_WIFI\_INFO | api/@ohos.wifiext.d.ts |
| 权限变更 | 类名：wifiext；  API声明：function getPowerModel(callback: AsyncCallback<PowerModel>): void;  差异内容：NA | 类名：wifiext；  API声明：function getPowerModel(callback: AsyncCallback<PowerModel>): void;  差异内容：ohos.permission.GET\_WIFI\_INFO | api/@ohos.wifiext.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function getScanResults(callback: AsyncCallback<Array<WifiScanInfo>>): void;  差异内容：NA | 类名：wifiManager；  API声明：function getScanResults(callback: AsyncCallback<Array<WifiScanInfo>>): void;  差异内容：ohos.permission.GET\_WIFI\_INFO and (ohos.permission.GET\_WIFI\_PEERS\_MAC or (ohos.permission.LOCATION and ohos.permission.APPROXIMATELY\_LOCATION)) | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function addCandidateConfig(config: WifiDeviceConfig, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：wifiManager；  API声明：function addCandidateConfig(config: WifiDeviceConfig, callback: AsyncCallback<number>): void;  差异内容：ohos.permission.SET\_WIFI\_INFO | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function removeCandidateConfig(networkId: number, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：wifiManager；  API声明：function removeCandidateConfig(networkId: number, callback: AsyncCallback<void>): void;  差异内容：ohos.permission.SET\_WIFI\_INFO | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void;  差异内容：NA | 类名：wifiManager；  API声明：function getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void;  差异内容：ohos.permission.GET\_WIFI\_INFO | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function getP2pLinkedInfo(callback: AsyncCallback<WifiP2pLinkedInfo>): void;  差异内容：NA | 类名：wifiManager；  API声明：function getP2pLinkedInfo(callback: AsyncCallback<WifiP2pLinkedInfo>): void;  差异内容：ohos.permission.GET\_WIFI\_INFO | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function getCurrentGroup(callback: AsyncCallback<WifiP2pGroupInfo>): void;  差异内容：NA | 类名：wifiManager；  API声明：function getCurrentGroup(callback: AsyncCallback<WifiP2pGroupInfo>): void;  差异内容：ohos.permission.GET\_WIFI\_INFO | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice[]>): void;  差异内容：NA | 类名：wifiManager；  API声明：function getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice[]>): void;  差异内容：ohos.permission.GET\_WIFI\_INFO | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function getP2pLocalDevice(callback: AsyncCallback<WifiP2pDevice>): void;  差异内容：NA | 类名：wifiManager；  API声明：function getP2pLocalDevice(callback: AsyncCallback<WifiP2pDevice>): void;  差异内容：ohos.permission.GET\_WIFI\_INFO | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManagerExt；  API声明：function getSupportedPowerMode(callback: AsyncCallback<Array<PowerMode>>): void;  差异内容：NA | 类名：wifiManagerExt；  API声明：function getSupportedPowerMode(callback: AsyncCallback<Array<PowerMode>>): void;  差异内容：ohos.permission.GET\_WIFI\_INFO | api/@ohos.wifiManagerExt.d.ts |
| 权限变更 | 类名：wifiManagerExt；  API声明：function getPowerMode(callback: AsyncCallback<PowerMode>): void;  差异内容：NA | 类名：wifiManagerExt；  API声明：function getPowerMode(callback: AsyncCallback<PowerMode>): void;  差异内容：ohos.permission.GET\_WIFI\_INFO | api/@ohos.wifiManagerExt.d.ts |
| 权限变更 | 类名：IsoDepTag；  API声明：isExtendedApduSupported(callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：IsoDepTag；  API声明：isExtendedApduSupported(callback: AsyncCallback<boolean>): void;  差异内容：ohos.permission.NFC\_TAG | api/tag/nfctech.d.ts |
| 权限变更 | 类名：NdefTag；  API声明：readNdef(callback: AsyncCallback<NdefMessage>): void;  差异内容：NA | 类名：NdefTag；  API声明：readNdef(callback: AsyncCallback<NdefMessage>): void;  差异内容：ohos.permission.NFC\_TAG | api/tag/nfctech.d.ts |
| 权限变更 | 类名：NdefTag；  API声明：writeNdef(msg: NdefMessage, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：NdefTag；  API声明：writeNdef(msg: NdefMessage, callback: AsyncCallback<void>): void;  差异内容：ohos.permission.NFC\_TAG | api/tag/nfctech.d.ts |
| 权限变更 | 类名：NdefTag；  API声明：setReadOnly(callback: AsyncCallback<void>): void;  差异内容：NA | 类名：NdefTag；  API声明：setReadOnly(callback: AsyncCallback<void>): void;  差异内容：ohos.permission.NFC\_TAG | api/tag/nfctech.d.ts |
| 权限变更 | 类名：MifareClassicTag；  API声明：authenticateSector(sectorIndex: number, key: number[], isKeyA: boolean, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：MifareClassicTag；  API声明：authenticateSector(sectorIndex: number, key: number[], isKeyA: boolean, callback: AsyncCallback<void>): void;  差异内容：ohos.permission.NFC\_TAG | api/tag/nfctech.d.ts |
| 权限变更 | 类名：MifareClassicTag；  API声明：readSingleBlock(blockIndex: number, callback: AsyncCallback<number[]>): void;  差异内容：NA | 类名：MifareClassicTag；  API声明：readSingleBlock(blockIndex: number, callback: AsyncCallback<number[]>): void;  差异内容：ohos.permission.NFC\_TAG | api/tag/nfctech.d.ts |
| 权限变更 | 类名：MifareClassicTag；  API声明：writeSingleBlock(blockIndex: number, data: number[], callback: AsyncCallback<void>): void;  差异内容：NA | 类名：MifareClassicTag；  API声明：writeSingleBlock(blockIndex: number, data: number[], callback: AsyncCallback<void>): void;  差异内容：ohos.permission.NFC\_TAG | api/tag/nfctech.d.ts |
| 权限变更 | 类名：MifareClassicTag；  API声明：incrementBlock(blockIndex: number, value: number, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：MifareClassicTag；  API声明：incrementBlock(blockIndex: number, value: number, callback: AsyncCallback<void>): void;  差异内容：ohos.permission.NFC\_TAG | api/tag/nfctech.d.ts |
| 权限变更 | 类名：MifareClassicTag；  API声明：decrementBlock(blockIndex: number, value: number, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：MifareClassicTag；  API声明：decrementBlock(blockIndex: number, value: number, callback: AsyncCallback<void>): void;  差异内容：ohos.permission.NFC\_TAG | api/tag/nfctech.d.ts |
| 权限变更 | 类名：MifareClassicTag；  API声明：transferToBlock(blockIndex: number, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：MifareClassicTag；  API声明：transferToBlock(blockIndex: number, callback: AsyncCallback<void>): void;  差异内容：ohos.permission.NFC\_TAG | api/tag/nfctech.d.ts |
| 权限变更 | 类名：MifareClassicTag；  API声明：restoreFromBlock(blockIndex: number, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：MifareClassicTag；  API声明：restoreFromBlock(blockIndex: number, callback: AsyncCallback<void>): void;  差异内容：ohos.permission.NFC\_TAG | api/tag/nfctech.d.ts |
| 权限变更 | 类名：MifareUltralightTag；  API声明：readMultiplePages(pageIndex: number, callback: AsyncCallback<number[]>): void;  差异内容：NA | 类名：MifareUltralightTag；  API声明：readMultiplePages(pageIndex: number, callback: AsyncCallback<number[]>): void;  差异内容：ohos.permission.NFC\_TAG | api/tag/nfctech.d.ts |
| 权限变更 | 类名：MifareUltralightTag；  API声明：writeSinglePage(pageIndex: number, data: number[], callback: AsyncCallback<void>): void;  差异内容：NA | 类名：MifareUltralightTag；  API声明：writeSinglePage(pageIndex: number, data: number[], callback: AsyncCallback<void>): void;  差异内容：ohos.permission.NFC\_TAG | api/tag/nfctech.d.ts |
| 权限变更 | 类名：NdefFormatableTag；  API声明：format(message: NdefMessage, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：NdefFormatableTag；  API声明：format(message: NdefMessage, callback: AsyncCallback<void>): void;  差异内容：ohos.permission.NFC\_TAG | api/tag/nfctech.d.ts |
| 权限变更 | 类名：NdefFormatableTag；  API声明：formatReadOnly(message: NdefMessage, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：NdefFormatableTag；  API声明：formatReadOnly(message: NdefMessage, callback: AsyncCallback<void>): void;  差异内容：ohos.permission.NFC\_TAG | api/tag/nfctech.d.ts |
| 权限变更 | 类名：TagSession；  API声明：sendData(data: number[], callback: AsyncCallback<number[]>): void;  差异内容：NA | 类名：TagSession；  API声明：sendData(data: number[], callback: AsyncCallback<number[]>): void;  差异内容：ohos.permission.NFC\_TAG | api/tag/tagSession.d.ts |
| 权限变更 | 类名：TagSession；  API声明：transmit(data: number[], callback: AsyncCallback<number[]>): void;  差异内容：NA | 类名：TagSession；  API声明：transmit(data: number[], callback: AsyncCallback<number[]>): void;  差异内容：ohos.permission.NFC\_TAG | api/tag/tagSession.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function off(type: "p2pDeviceChange", callback?: Callback<WifiP2pDevice>): void;  差异内容：ohos.permission.LOCATION | 类名：wifiManager；  API声明：function off(type: 'p2pDeviceChange', callback?: Callback<WifiP2pDevice>): void;  差异内容：NA | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function off(type: "p2pPeerDeviceChange", callback?: Callback<WifiP2pDevice[]>): void;  差异内容：ohos.permission.LOCATION | 类名：wifiManager；  API声明：function off(type: 'p2pPeerDeviceChange', callback?: Callback<WifiP2pDevice[]>): void;  差异内容：NA | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function getCandidateConfigs(): Array<WifiDeviceConfig>;  差异内容：ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION | 类名：wifiManager；  API声明：function getCandidateConfigs(): Array<WifiDeviceConfig>;  差异内容：ohos.permission.GET\_WIFI\_INFO | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function getCurrentGroup(): Promise<WifiP2pGroupInfo>;  差异内容：ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION | 类名：wifiManager；  API声明：function getCurrentGroup(): Promise<WifiP2pGroupInfo>;  差异内容：ohos.permission.GET\_WIFI\_INFO | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function getP2pPeerDevices(): Promise<WifiP2pDevice[]>;  差异内容：ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION | 类名：wifiManager；  API声明：function getP2pPeerDevices(): Promise<WifiP2pDevice[]>;  差异内容：ohos.permission.GET\_WIFI\_INFO | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function getP2pLocalDevice(): Promise<WifiP2pDevice>;  差异内容：ohos.permission.GET\_WIFI\_INFO and ohos.permission.GET\_WIFI\_CONFIG | 类名：wifiManager；  API声明：function getP2pLocalDevice(): Promise<WifiP2pDevice>;  差异内容：ohos.permission.GET\_WIFI\_INFO | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function p2pConnect(config: WifiP2PConfig): void;  差异内容：ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION | 类名：wifiManager；  API声明：function p2pConnect(config: WifiP2PConfig): void;  差异内容：ohos.permission.GET\_WIFI\_INFO | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function startDiscoverDevices(): void;  差异内容：ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION | 类名：wifiManager；  API声明：function startDiscoverDevices(): void;  差异内容：ohos.permission.GET\_WIFI\_INFO | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function on(type: "p2pDeviceChange", callback: Callback<WifiP2pDevice>): void;  差异内容：ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION | 类名：wifiManager；  API声明：function on(type: 'p2pDeviceChange', callback: Callback<WifiP2pDevice>): void;  差异内容：ohos.permission.GET\_WIFI\_INFO | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function on(type: "p2pPeerDeviceChange", callback: Callback<WifiP2pDevice[]>): void;  差异内容：ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION | 类名：wifiManager；  API声明：function on(type: 'p2pPeerDeviceChange', callback: Callback<WifiP2pDevice[]>): void;  差异内容：ohos.permission.GET\_WIFI\_INFO | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function setDevicePairingConfirmation(device: string, accept: boolean): void;  差异内容：ohos.permission.MANAGE\_BLUETOOTH | 类名：bluetoothManager；  API声明：function setDevicePairingConfirmation(device: string, accept: boolean): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH and ohos.permission.MANAGE\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function scan(): void;  差异内容：ohos.permission.SET\_WIFI\_INFO and ohos.permission.LOCATION | 类名：wifiManager；  API声明：function scan(): void;  差异内容：ohos.permission.SET\_WIFI\_INFO and ohos.permission.LOCATION and ohos.permission.APPROXIMATELY\_LOCATION | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function getScanResults(): Promise<Array<WifiScanInfo>>;  差异内容：ohos.permission.GET\_WIFI\_INFO and (ohos.permission.GET\_WIFI\_PEERS\_MAC or ohos.permission.LOCATION) | 类名：wifiManager；  API声明：function getScanResults(): Promise<Array<WifiScanInfo>>;  差异内容：ohos.permission.GET\_WIFI\_INFO and (ohos.permission.GET\_WIFI\_PEERS\_MAC or (ohos.permission.LOCATION and ohos.permission.APPROXIMATELY\_LOCATION)) | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManager；  API声明：function getScanResultsSync(): Array<WifiScanInfo>;  差异内容：ohos.permission.GET\_WIFI\_INFO and (ohos.permission.GET\_WIFI\_PEERS\_MAC or ohos.permission.LOCATION) | 类名：wifiManager；  API声明：function getScanResultsSync(): Array<WifiScanInfo>;  差异内容：ohos.permission.GET\_WIFI\_INFO and (ohos.permission.GET\_WIFI\_PEERS\_MAC or (ohos.permission.LOCATION and ohos.permission.APPROXIMATELY\_LOCATION)) | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function getState(): BluetoothState;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：bluetoothManager；  API声明：function getState(): BluetoothState;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function getBtConnectionState(): ProfileConnectionState;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：bluetoothManager；  API声明：function getBtConnectionState(): ProfileConnectionState;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function pairDevice(deviceId: string): void;  差异内容：ohos.permission.DISCOVER\_BLUETOOTH | 类名：bluetoothManager；  API声明：function pairDevice(deviceId: string): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function getRemoteDeviceName(deviceId: string): string;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：bluetoothManager；  API声明：function getRemoteDeviceName(deviceId: string): string;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function getRemoteDeviceClass(deviceId: string): DeviceClass;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：bluetoothManager；  API声明：function getRemoteDeviceClass(deviceId: string): DeviceClass;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function enableBluetooth(): void;  差异内容：ohos.permission.DISCOVER\_BLUETOOTH | 类名：bluetoothManager；  API声明：function enableBluetooth(): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function disableBluetooth(): void;  差异内容：ohos.permission.DISCOVER\_BLUETOOTH | 类名：bluetoothManager；  API声明：function disableBluetooth(): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function getLocalName(): string;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：bluetoothManager；  API声明：function getLocalName(): string;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function getPairedDevices(): Array<string>;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：bluetoothManager；  API声明：function getPairedDevices(): Array<string>;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function getProfileConnectionState(profileId: ProfileId): ProfileConnectionState;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：bluetoothManager；  API声明：function getProfileConnectionState(profileId: ProfileId): ProfileConnectionState;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function setLocalName(name: string): void;  差异内容：ohos.permission.DISCOVER\_BLUETOOTH | 类名：bluetoothManager；  API声明：function setLocalName(name: string): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function setBluetoothScanMode(mode: ScanMode, duration: number): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：bluetoothManager；  API声明：function setBluetoothScanMode(mode: ScanMode, duration: number): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function getBluetoothScanMode(): ScanMode;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：bluetoothManager；  API声明：function getBluetoothScanMode(): ScanMode;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function startBluetoothDiscovery(): void;  差异内容：ohos.permission.DISCOVER\_BLUETOOTH and ohos.permission.LOCATION and ohos.permission.APPROXIMATELY\_LOCATION | 类名：bluetoothManager；  API声明：function startBluetoothDiscovery(): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function stopBluetoothDiscovery(): void;  差异内容：ohos.permission.DISCOVER\_BLUETOOTH | 类名：bluetoothManager；  API声明：function stopBluetoothDiscovery(): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function on(type: "bluetoothDeviceFind", callback: Callback<Array<string>>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：bluetoothManager；  API声明：function on(type: 'bluetoothDeviceFind', callback: Callback<Array<string>>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function off(type: "bluetoothDeviceFind", callback?: Callback<Array<string>>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：bluetoothManager；  API声明：function off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function on(type: "bondStateChange", callback: Callback<BondStateParam>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：bluetoothManager；  API声明：function on(type: 'bondStateChange', callback: Callback<BondStateParam>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function off(type: "bondStateChange", callback?: Callback<BondStateParam>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：bluetoothManager；  API声明：function off(type: 'bondStateChange', callback?: Callback<BondStateParam>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function on(type: "pinRequired", callback: Callback<PinRequiredParam>): void;  差异内容：ohos.permission.DISCOVER\_BLUETOOTH | 类名：bluetoothManager；  API声明：function on(type: 'pinRequired', callback: Callback<PinRequiredParam>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function off(type: "pinRequired", callback?: Callback<PinRequiredParam>): void;  差异内容：ohos.permission.DISCOVER\_BLUETOOTH | 类名：bluetoothManager；  API声明：function off(type: 'pinRequired', callback?: Callback<PinRequiredParam>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function on(type: "stateChange", callback: Callback<BluetoothState>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：bluetoothManager；  API声明：function on(type: 'stateChange', callback: Callback<BluetoothState>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function off(type: "stateChange", callback?: Callback<BluetoothState>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：bluetoothManager；  API声明：function off(type: 'stateChange', callback?: Callback<BluetoothState>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function sppListen(name: string, option: SppOption, callback: AsyncCallback<number>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：bluetoothManager；  API声明：function sppListen(name: string, option: SppOption, callback: AsyncCallback<number>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager；  API声明：function sppConnect(device: string, option: SppOption, callback: AsyncCallback<number>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：bluetoothManager；  API声明：function sppConnect(device: string, option: SppOption, callback: AsyncCallback<number>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：BaseProfile；  API声明：getConnectionDevices(): Array<string>;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：BaseProfile；  API声明：getConnectionDevices(): Array<string>;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：BaseProfile；  API声明：getDeviceState(device: string): ProfileConnectionState;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：BaseProfile；  API声明：getDeviceState(device: string): ProfileConnectionState;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：A2dpSourceProfile；  API声明：connect(device: string): void;  差异内容：ohos.permission.DISCOVER\_BLUETOOTH | 类名：A2dpSourceProfile；  API声明：connect(device: string): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：A2dpSourceProfile；  API声明：disconnect(device: string): void;  差异内容：ohos.permission.DISCOVER\_BLUETOOTH | 类名：A2dpSourceProfile；  API声明：disconnect(device: string): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：HandsFreeAudioGatewayProfile；  API声明：connect(device: string): void;  差异内容：ohos.permission.DISCOVER\_BLUETOOTH | 类名：HandsFreeAudioGatewayProfile；  API声明：connect(device: string): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：HandsFreeAudioGatewayProfile；  API声明：disconnect(device: string): void;  差异内容：ohos.permission.DISCOVER\_BLUETOOTH | 类名：HandsFreeAudioGatewayProfile；  API声明：disconnect(device: string): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：BLE；  API声明：function getConnectedBLEDevices(): Array<string>;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：BLE；  API声明：function getConnectedBLEDevices(): Array<string>;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：BLE；  API声明：function startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void;  差异内容：ohos.permission.DISCOVER\_BLUETOOTH and ohos.permission.MANAGE\_BLUETOOTH and ohos.permission.LOCATION and ohos.permission.APPROXIMATELY\_LOCATION | 类名：BLE；  API声明：function startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：BLE；  API声明：function stopBLEScan(): void;  差异内容：ohos.permission.DISCOVER\_BLUETOOTH | 类名：BLE；  API声明：function stopBLEScan(): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：BLE；  API声明：function on(type: "BLEDeviceFind", callback: Callback<Array<ScanResult>>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：BLE；  API声明：function on(type: 'BLEDeviceFind', callback: Callback<Array<ScanResult>>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：BLE；  API声明：function off(type: "BLEDeviceFind", callback?: Callback<Array<ScanResult>>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：BLE；  API声明：function off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer；  API声明：startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void;  差异内容：ohos.permission.DISCOVER\_BLUETOOTH | 类名：GattServer；  API声明：startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer；  API声明：stopAdvertising(): void;  差异内容：ohos.permission.DISCOVER\_BLUETOOTH | 类名：GattServer；  API声明：stopAdvertising(): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer；  API声明：addService(service: GattService): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattServer；  API声明：addService(service: GattService): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer；  API声明：removeService(serviceUuid: string): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattServer；  API声明：removeService(serviceUuid: string): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer；  API声明：close(): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattServer；  API声明：close(): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer；  API声明：notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattServer；  API声明：notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer；  API声明：sendResponse(serverResponse: ServerResponse): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattServer；  API声明：sendResponse(serverResponse: ServerResponse): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer；  API声明：on(type: "characteristicRead", callback: Callback<CharacteristicReadRequest>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattServer；  API声明：on(type: 'characteristicRead', callback: Callback<CharacteristicReadRequest>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer；  API声明：off(type: "characteristicRead", callback?: Callback<CharacteristicReadRequest>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattServer；  API声明：off(type: 'characteristicRead', callback?: Callback<CharacteristicReadRequest>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer；  API声明：on(type: "characteristicWrite", callback: Callback<CharacteristicWriteRequest>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattServer；  API声明：on(type: 'characteristicWrite', callback: Callback<CharacteristicWriteRequest>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer；  API声明：off(type: "characteristicWrite", callback?: Callback<CharacteristicWriteRequest>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattServer；  API声明：off(type: 'characteristicWrite', callback?: Callback<CharacteristicWriteRequest>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer；  API声明：on(type: "descriptorRead", callback: Callback<DescriptorReadRequest>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattServer；  API声明：on(type: 'descriptorRead', callback: Callback<DescriptorReadRequest>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer；  API声明：off(type: "descriptorRead", callback?: Callback<DescriptorReadRequest>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattServer；  API声明：off(type: 'descriptorRead', callback?: Callback<DescriptorReadRequest>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer；  API声明：on(type: "descriptorWrite", callback: Callback<DescriptorWriteRequest>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattServer；  API声明：on(type: 'descriptorWrite', callback: Callback<DescriptorWriteRequest>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer；  API声明：off(type: "descriptorWrite", callback?: Callback<DescriptorWriteRequest>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattServer；  API声明：off(type: 'descriptorWrite', callback?: Callback<DescriptorWriteRequest>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer；  API声明：on(type: "connectStateChange", callback: Callback<BLEConnectChangedState>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattServer；  API声明：on(type: 'connectStateChange', callback: Callback<BLEConnectChangedState>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer；  API声明：off(type: "connectStateChange", callback?: Callback<BLEConnectChangedState>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattServer；  API声明：off(type: 'connectStateChange', callback?: Callback<BLEConnectChangedState>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：connect(): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattClientDevice；  API声明：connect(): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：disconnect(): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattClientDevice；  API声明：disconnect(): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：close(): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattClientDevice；  API声明：close(): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：getDeviceName(callback: AsyncCallback<string>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattClientDevice；  API声明：getDeviceName(callback: AsyncCallback<string>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：getServices(callback: AsyncCallback<Array<GattService>>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattClientDevice；  API声明：getServices(callback: AsyncCallback<Array<GattService>>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：readCharacteristicValue(characteristic: BLECharacteristic, callback: AsyncCallback<BLECharacteristic>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattClientDevice；  API声明：readCharacteristicValue(characteristic: BLECharacteristic, callback: AsyncCallback<BLECharacteristic>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：readDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<BLEDescriptor>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattClientDevice；  API声明：readDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<BLEDescriptor>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：writeCharacteristicValue(characteristic: BLECharacteristic): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattClientDevice；  API声明：writeCharacteristicValue(characteristic: BLECharacteristic): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：writeDescriptorValue(descriptor: BLEDescriptor): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattClientDevice；  API声明：writeDescriptorValue(descriptor: BLEDescriptor): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：getRssiValue(callback: AsyncCallback<number>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattClientDevice；  API声明：getRssiValue(callback: AsyncCallback<number>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：setBLEMtuSize(mtu: number): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattClientDevice；  API声明：setBLEMtuSize(mtu: number): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：setNotifyCharacteristicChanged(characteristic: BLECharacteristic, enable: boolean): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattClientDevice；  API声明：setNotifyCharacteristicChanged(characteristic: BLECharacteristic, enable: boolean): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：on(type: "BLECharacteristicChange", callback: Callback<BLECharacteristic>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattClientDevice；  API声明：on(type: 'BLECharacteristicChange', callback: Callback<BLECharacteristic>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：off(type: "BLECharacteristicChange", callback?: Callback<BLECharacteristic>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattClientDevice；  API声明：off(type: 'BLECharacteristicChange', callback?: Callback<BLECharacteristic>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：on(type: "BLEConnectionStateChange", callback: Callback<BLEConnectChangedState>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattClientDevice；  API声明：on(type: 'BLEConnectionStateChange', callback: Callback<BLEConnectChangedState>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice；  API声明：off(type: "BLEConnectionStateChange", callback?: Callback<BLEConnectChangedState>): void;  差异内容：ohos.permission.USE\_BLUETOOTH | 类名：GattClientDevice；  API声明：off(type: 'BLEConnectionStateChange', callback?: Callback<BLEConnectChangedState>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：bluetooth；  API声明：function on(type: "bluetoothDeviceFind", callback: Callback<Array<string>>): void;  差异内容：type: "bluetoothDeviceFind" | 类名：bluetooth；  API声明：function on(type: 'bluetoothDeviceFind', callback: Callback<Array<string>>): void;  差异内容：type: 'bluetoothDeviceFind' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：bluetooth；  API声明：function off(type: "bluetoothDeviceFind", callback?: Callback<Array<string>>): void;  差异内容：type: "bluetoothDeviceFind" | 类名：bluetooth；  API声明：function off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void;  差异内容：type: 'bluetoothDeviceFind' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：bluetooth；  API声明：function on(type: "bondStateChange", callback: Callback<BondStateParam>): void;  差异内容：type: "bondStateChange" | 类名：bluetooth；  API声明：function on(type: 'bondStateChange', callback: Callback<BondStateParam>): void;  差异内容：type: 'bondStateChange' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：bluetooth；  API声明：function off(type: "bondStateChange", callback?: Callback<BondStateParam>): void;  差异内容：type: "bondStateChange" | 类名：bluetooth；  API声明：function off(type: 'bondStateChange', callback?: Callback<BondStateParam>): void;  差异内容：type: 'bondStateChange' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：bluetooth；  API声明：function on(type: "pinRequired", callback: Callback<PinRequiredParam>): void;  差异内容：type: "pinRequired" | 类名：bluetooth；  API声明：function on(type: 'pinRequired', callback: Callback<PinRequiredParam>): void;  差异内容：type: 'pinRequired' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：bluetooth；  API声明：function off(type: "pinRequired", callback?: Callback<PinRequiredParam>): void;  差异内容：type: "pinRequired" | 类名：bluetooth；  API声明：function off(type: 'pinRequired', callback?: Callback<PinRequiredParam>): void;  差异内容：type: 'pinRequired' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：bluetooth；  API声明：function on(type: "stateChange", callback: Callback<BluetoothState>): void;  差异内容：type: "stateChange" | 类名：bluetooth；  API声明：function on(type: 'stateChange', callback: Callback<BluetoothState>): void;  差异内容：type: 'stateChange' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：bluetooth；  API声明：function off(type: "stateChange", callback?: Callback<BluetoothState>): void;  差异内容：type: "stateChange" | 类名：bluetooth；  API声明：function off(type: 'stateChange', callback?: Callback<BluetoothState>): void;  差异内容：type: 'stateChange' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：bluetooth；  API声明：function on(type: "sppRead", clientSocket: number, callback: Callback<ArrayBuffer>): void;  差异内容：type: "sppRead" | 类名：bluetooth；  API声明：function on(type: 'sppRead', clientSocket: number, callback: Callback<ArrayBuffer>): void;  差异内容：type: 'sppRead' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：bluetooth；  API声明：function off(type: "sppRead", clientSocket: number, callback?: Callback<ArrayBuffer>): void;  差异内容：type: "sppRead" | 类名：bluetooth；  API声明：function off(type: 'sppRead', clientSocket: number, callback?: Callback<ArrayBuffer>): void;  差异内容：type: 'sppRead' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：A2dpSourceProfile；  API声明：on(type: "connectionStateChange", callback: Callback<StateChangeParam>): void;  差异内容：type: "connectionStateChange" | 类名：A2dpSourceProfile；  API声明：on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void;  差异内容：type: 'connectionStateChange' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：A2dpSourceProfile；  API声明：off(type: "connectionStateChange", callback?: Callback<StateChangeParam>): void;  差异内容：type: "connectionStateChange" | 类名：A2dpSourceProfile；  API声明：off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void;  差异内容：type: 'connectionStateChange' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：HandsFreeAudioGatewayProfile；  API声明：on(type: "connectionStateChange", callback: Callback<StateChangeParam>): void;  差异内容：type: "connectionStateChange" | 类名：HandsFreeAudioGatewayProfile；  API声明：on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void;  差异内容：type: 'connectionStateChange' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：HandsFreeAudioGatewayProfile；  API声明：off(type: "connectionStateChange", callback?: Callback<StateChangeParam>): void;  差异内容：type: "connectionStateChange" | 类名：HandsFreeAudioGatewayProfile；  API声明：off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void;  差异内容：type: 'connectionStateChange' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：BLE；  API声明：function on(type: "BLEDeviceFind", callback: Callback<Array<ScanResult>>): void;  差异内容：type: "BLEDeviceFind" | 类名：BLE；  API声明：function on(type: 'BLEDeviceFind', callback: Callback<Array<ScanResult>>): void;  差异内容：type: 'BLEDeviceFind' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：BLE；  API声明：function off(type: "BLEDeviceFind", callback?: Callback<Array<ScanResult>>): void;  差异内容：type: "BLEDeviceFind" | 类名：BLE；  API声明：function off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void;  差异内容：type: 'BLEDeviceFind' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：GattServer；  API声明：on(type: "characteristicRead", callback: Callback<CharacteristicReadReq>): void;  差异内容：type: "characteristicRead" | 类名：GattServer；  API声明：on(type: 'characteristicRead', callback: Callback<CharacteristicReadReq>): void;  差异内容：type: 'characteristicRead' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：GattServer；  API声明：off(type: "characteristicRead", callback?: Callback<CharacteristicReadReq>): void;  差异内容：type: "characteristicRead" | 类名：GattServer；  API声明：off(type: 'characteristicRead', callback?: Callback<CharacteristicReadReq>): void;  差异内容：type: 'characteristicRead' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：GattServer；  API声明：on(type: "characteristicWrite", callback: Callback<CharacteristicWriteReq>): void;  差异内容：type: "characteristicWrite" | 类名：GattServer；  API声明：on(type: 'characteristicWrite', callback: Callback<CharacteristicWriteReq>): void;  差异内容：type: 'characteristicWrite' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：GattServer；  API声明：off(type: "characteristicWrite", callback?: Callback<CharacteristicWriteReq>): void;  差异内容：type: "characteristicWrite" | 类名：GattServer；  API声明：off(type: 'characteristicWrite', callback?: Callback<CharacteristicWriteReq>): void;  差异内容：type: 'characteristicWrite' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：GattServer；  API声明：on(type: "descriptorRead", callback: Callback<DescriptorReadReq>): void;  差异内容：type: "descriptorRead" | 类名：GattServer；  API声明：on(type: 'descriptorRead', callback: Callback<DescriptorReadReq>): void;  差异内容：type: 'descriptorRead' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：GattServer；  API声明：off(type: "descriptorRead", callback?: Callback<DescriptorReadReq>): void;  差异内容：type: "descriptorRead" | 类名：GattServer；  API声明：off(type: 'descriptorRead', callback?: Callback<DescriptorReadReq>): void;  差异内容：type: 'descriptorRead' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：GattServer；  API声明：on(type: "descriptorWrite", callback: Callback<DescriptorWriteReq>): void;  差异内容：type: "descriptorWrite" | 类名：GattServer；  API声明：on(type: 'descriptorWrite', callback: Callback<DescriptorWriteReq>): void;  差异内容：type: 'descriptorWrite' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：GattServer；  API声明：off(type: "descriptorWrite", callback?: Callback<DescriptorWriteReq>): void;  差异内容：type: "descriptorWrite" | 类名：GattServer；  API声明：off(type: 'descriptorWrite', callback?: Callback<DescriptorWriteReq>): void;  差异内容：type: 'descriptorWrite' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：GattServer；  API声明：on(type: "connectStateChange", callback: Callback<BLEConnectChangedState>): void;  差异内容：type: "connectStateChange" | 类名：GattServer；  API声明：on(type: 'connectStateChange', callback: Callback<BLEConnectChangedState>): void;  差异内容：type: 'connectStateChange' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：GattServer；  API声明：off(type: "connectStateChange", callback?: Callback<BLEConnectChangedState>): void;  差异内容：type: "connectStateChange" | 类名：GattServer；  API声明：off(type: 'connectStateChange', callback?: Callback<BLEConnectChangedState>): void;  差异内容：type: 'connectStateChange' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：GattClientDevice；  API声明：on(type: "BLECharacteristicChange", callback: Callback<BLECharacteristic>): void;  差异内容：type: "BLECharacteristicChange" | 类名：GattClientDevice；  API声明：on(type: 'BLECharacteristicChange', callback: Callback<BLECharacteristic>): void;  差异内容：type: 'BLECharacteristicChange' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：GattClientDevice；  API声明：off(type: "BLECharacteristicChange", callback?: Callback<BLECharacteristic>): void;  差异内容：type: "BLECharacteristicChange" | 类名：GattClientDevice；  API声明：off(type: 'BLECharacteristicChange', callback?: Callback<BLECharacteristic>): void;  差异内容：type: 'BLECharacteristicChange' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：GattClientDevice；  API声明：on(type: "BLEConnectionStateChange", callback: Callback<BLEConnectChangedState>): void;  差异内容：type: "BLEConnectionStateChange" | 类名：GattClientDevice；  API声明：on(type: 'BLEConnectionStateChange', callback: Callback<BLEConnectChangedState>): void;  差异内容：type: 'BLEConnectionStateChange' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：GattClientDevice；  API声明：off(type: "BLEConnectionStateChange", callback?: Callback<BLEConnectChangedState>): void;  差异内容：type: "BLEConnectionStateChange" | 类名：GattClientDevice；  API声明：off(type: 'BLEConnectionStateChange', callback?: Callback<BLEConnectChangedState>): void;  差异内容：type: 'BLEConnectionStateChange' | api/@ohos.bluetooth.d.ts |
| 函数变更 | 类名：bluetoothManager；  API声明：function on(type: "bluetoothDeviceFind", callback: Callback<Array<string>>): void;  差异内容：type: "bluetoothDeviceFind" | 类名：bluetoothManager；  API声明：function on(type: 'bluetoothDeviceFind', callback: Callback<Array<string>>): void;  差异内容：type: 'bluetoothDeviceFind' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：bluetoothManager；  API声明：function off(type: "bluetoothDeviceFind", callback?: Callback<Array<string>>): void;  差异内容：type: "bluetoothDeviceFind" | 类名：bluetoothManager；  API声明：function off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void;  差异内容：type: 'bluetoothDeviceFind' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：bluetoothManager；  API声明：function on(type: "bondStateChange", callback: Callback<BondStateParam>): void;  差异内容：type: "bondStateChange" | 类名：bluetoothManager；  API声明：function on(type: 'bondStateChange', callback: Callback<BondStateParam>): void;  差异内容：type: 'bondStateChange' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：bluetoothManager；  API声明：function off(type: "bondStateChange", callback?: Callback<BondStateParam>): void;  差异内容：type: "bondStateChange" | 类名：bluetoothManager；  API声明：function off(type: 'bondStateChange', callback?: Callback<BondStateParam>): void;  差异内容：type: 'bondStateChange' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：bluetoothManager；  API声明：function on(type: "pinRequired", callback: Callback<PinRequiredParam>): void;  差异内容：type: "pinRequired" | 类名：bluetoothManager；  API声明：function on(type: 'pinRequired', callback: Callback<PinRequiredParam>): void;  差异内容：type: 'pinRequired' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：bluetoothManager；  API声明：function off(type: "pinRequired", callback?: Callback<PinRequiredParam>): void;  差异内容：type: "pinRequired" | 类名：bluetoothManager；  API声明：function off(type: 'pinRequired', callback?: Callback<PinRequiredParam>): void;  差异内容：type: 'pinRequired' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：bluetoothManager；  API声明：function on(type: "stateChange", callback: Callback<BluetoothState>): void;  差异内容：type: "stateChange" | 类名：bluetoothManager；  API声明：function on(type: 'stateChange', callback: Callback<BluetoothState>): void;  差异内容：type: 'stateChange' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：bluetoothManager；  API声明：function off(type: "stateChange", callback?: Callback<BluetoothState>): void;  差异内容：type: "stateChange" | 类名：bluetoothManager；  API声明：function off(type: 'stateChange', callback?: Callback<BluetoothState>): void;  差异内容：type: 'stateChange' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：bluetoothManager；  API声明：function on(type: "sppRead", clientSocket: number, callback: Callback<ArrayBuffer>): void;  差异内容：type: "sppRead" | 类名：bluetoothManager；  API声明：function on(type: 'sppRead', clientSocket: number, callback: Callback<ArrayBuffer>): void;  差异内容：type: 'sppRead' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：bluetoothManager；  API声明：function off(type: "sppRead", clientSocket: number, callback?: Callback<ArrayBuffer>): void;  差异内容：type: "sppRead" | 类名：bluetoothManager；  API声明：function off(type: 'sppRead', clientSocket: number, callback?: Callback<ArrayBuffer>): void;  差异内容：type: 'sppRead' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：A2dpSourceProfile；  API声明：on(type: "connectionStateChange", callback: Callback<StateChangeParam>): void;  差异内容：type: "connectionStateChange" | 类名：A2dpSourceProfile；  API声明：on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void;  差异内容：type: 'connectionStateChange' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：A2dpSourceProfile；  API声明：off(type: "connectionStateChange", callback?: Callback<StateChangeParam>): void;  差异内容：type: "connectionStateChange" | 类名：A2dpSourceProfile；  API声明：off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void;  差异内容：type: 'connectionStateChange' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：HandsFreeAudioGatewayProfile；  API声明：on(type: "connectionStateChange", callback: Callback<StateChangeParam>): void;  差异内容：type: "connectionStateChange" | 类名：HandsFreeAudioGatewayProfile；  API声明：on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void;  差异内容：type: 'connectionStateChange' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：HandsFreeAudioGatewayProfile；  API声明：off(type: "connectionStateChange", callback?: Callback<StateChangeParam>): void;  差异内容：type: "connectionStateChange" | 类名：HandsFreeAudioGatewayProfile；  API声明：off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void;  差异内容：type: 'connectionStateChange' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：HidHostProfile；  API声明：on(type: "connectionStateChange", callback: Callback<StateChangeParam>): void;  差异内容：type: "connectionStateChange" | 类名：HidHostProfile；  API声明：on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void;  差异内容：type: 'connectionStateChange' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：HidHostProfile；  API声明：off(type: "connectionStateChange", callback?: Callback<StateChangeParam>): void;  差异内容：type: "connectionStateChange" | 类名：HidHostProfile；  API声明：off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void;  差异内容：type: 'connectionStateChange' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：PanProfile；  API声明：on(type: "connectionStateChange", callback: Callback<StateChangeParam>): void;  差异内容：type: "connectionStateChange" | 类名：PanProfile；  API声明：on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void;  差异内容：type: 'connectionStateChange' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：PanProfile；  API声明：off(type: "connectionStateChange", callback?: Callback<StateChangeParam>): void;  差异内容：type: "connectionStateChange" | 类名：PanProfile；  API声明：off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void;  差异内容：type: 'connectionStateChange' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：BLE；  API声明：function on(type: "BLEDeviceFind", callback: Callback<Array<ScanResult>>): void;  差异内容：type: "BLEDeviceFind" | 类名：BLE；  API声明：function on(type: 'BLEDeviceFind', callback: Callback<Array<ScanResult>>): void;  差异内容：type: 'BLEDeviceFind' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：BLE；  API声明：function off(type: "BLEDeviceFind", callback?: Callback<Array<ScanResult>>): void;  差异内容：type: "BLEDeviceFind" | 类名：BLE；  API声明：function off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void;  差异内容：type: 'BLEDeviceFind' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：GattServer；  API声明：on(type: "characteristicRead", callback: Callback<CharacteristicReadRequest>): void;  差异内容：type: "characteristicRead" | 类名：GattServer；  API声明：on(type: 'characteristicRead', callback: Callback<CharacteristicReadRequest>): void;  差异内容：type: 'characteristicRead' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：GattServer；  API声明：off(type: "characteristicRead", callback?: Callback<CharacteristicReadRequest>): void;  差异内容：type: "characteristicRead" | 类名：GattServer；  API声明：off(type: 'characteristicRead', callback?: Callback<CharacteristicReadRequest>): void;  差异内容：type: 'characteristicRead' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：GattServer；  API声明：on(type: "characteristicWrite", callback: Callback<CharacteristicWriteRequest>): void;  差异内容：type: "characteristicWrite" | 类名：GattServer；  API声明：on(type: 'characteristicWrite', callback: Callback<CharacteristicWriteRequest>): void;  差异内容：type: 'characteristicWrite' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：GattServer；  API声明：off(type: "characteristicWrite", callback?: Callback<CharacteristicWriteRequest>): void;  差异内容：type: "characteristicWrite" | 类名：GattServer；  API声明：off(type: 'characteristicWrite', callback?: Callback<CharacteristicWriteRequest>): void;  差异内容：type: 'characteristicWrite' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：GattServer；  API声明：on(type: "descriptorRead", callback: Callback<DescriptorReadRequest>): void;  差异内容：type: "descriptorRead" | 类名：GattServer；  API声明：on(type: 'descriptorRead', callback: Callback<DescriptorReadRequest>): void;  差异内容：type: 'descriptorRead' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：GattServer；  API声明：off(type: "descriptorRead", callback?: Callback<DescriptorReadRequest>): void;  差异内容：type: "descriptorRead" | 类名：GattServer；  API声明：off(type: 'descriptorRead', callback?: Callback<DescriptorReadRequest>): void;  差异内容：type: 'descriptorRead' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：GattServer；  API声明：on(type: "descriptorWrite", callback: Callback<DescriptorWriteRequest>): void;  差异内容：type: "descriptorWrite" | 类名：GattServer；  API声明：on(type: 'descriptorWrite', callback: Callback<DescriptorWriteRequest>): void;  差异内容：type: 'descriptorWrite' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：GattServer；  API声明：off(type: "descriptorWrite", callback?: Callback<DescriptorWriteRequest>): void;  差异内容：type: "descriptorWrite" | 类名：GattServer；  API声明：off(type: 'descriptorWrite', callback?: Callback<DescriptorWriteRequest>): void;  差异内容：type: 'descriptorWrite' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：GattServer；  API声明：on(type: "connectStateChange", callback: Callback<BLEConnectChangedState>): void;  差异内容：type: "connectStateChange" | 类名：GattServer；  API声明：on(type: 'connectStateChange', callback: Callback<BLEConnectChangedState>): void;  差异内容：type: 'connectStateChange' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：GattServer；  API声明：off(type: "connectStateChange", callback?: Callback<BLEConnectChangedState>): void;  差异内容：type: "connectStateChange" | 类名：GattServer；  API声明：off(type: 'connectStateChange', callback?: Callback<BLEConnectChangedState>): void;  差异内容：type: 'connectStateChange' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：GattClientDevice；  API声明：on(type: "BLECharacteristicChange", callback: Callback<BLECharacteristic>): void;  差异内容：type: "BLECharacteristicChange" | 类名：GattClientDevice；  API声明：on(type: 'BLECharacteristicChange', callback: Callback<BLECharacteristic>): void;  差异内容：type: 'BLECharacteristicChange' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：GattClientDevice；  API声明：off(type: "BLECharacteristicChange", callback?: Callback<BLECharacteristic>): void;  差异内容：type: "BLECharacteristicChange" | 类名：GattClientDevice；  API声明：off(type: 'BLECharacteristicChange', callback?: Callback<BLECharacteristic>): void;  差异内容：type: 'BLECharacteristicChange' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：GattClientDevice；  API声明：on(type: "BLEConnectionStateChange", callback: Callback<BLEConnectChangedState>): void;  差异内容：type: "BLEConnectionStateChange" | 类名：GattClientDevice；  API声明：on(type: 'BLEConnectionStateChange', callback: Callback<BLEConnectChangedState>): void;  差异内容：type: 'BLEConnectionStateChange' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：GattClientDevice；  API声明：off(type: "BLEConnectionStateChange", callback?: Callback<BLEConnectChangedState>): void;  差异内容：type: "BLEConnectionStateChange" | 类名：GattClientDevice；  API声明：off(type: 'BLEConnectionStateChange', callback?: Callback<BLEConnectChangedState>): void;  差异内容：type: 'BLEConnectionStateChange' | api/@ohos.bluetoothManager.d.ts |
| 函数变更 | 类名：connectedTag；  API声明：function on(type: "notify", callback: Callback<number>): void;  差异内容：type: "notify" | 类名：connectedTag；  API声明：function on(type: 'notify', callback: Callback<number>): void;  差异内容：type: 'notify' | api/@ohos.connectedTag.d.ts |
| 函数变更 | 类名：connectedTag；  API声明：function off(type: "notify", callback?: Callback<number>): void;  差异内容：type: "notify" | 类名：connectedTag；  API声明：function off(type: 'notify', callback?: Callback<number>): void;  差异内容：type: 'notify' | api/@ohos.connectedTag.d.ts |
| 函数变更 | 类名：HceService；  API声明：on(type: "hceCmd", callback: AsyncCallback<number[]>): void;  差异内容：type: "hceCmd" | 类名：HceService；  API声明：on(type: 'hceCmd', callback: AsyncCallback<number[]>): void;  差异内容：type: 'hceCmd' | api/@ohos.nfc.cardEmulation.d.ts |
| 函数变更 | 类名：nfcController；  API声明：function on(type: "nfcStateChange", callback: Callback<NfcState>): void;  差异内容：type: "nfcStateChange" | 类名：nfcController；  API声明：function on(type: 'nfcStateChange', callback: Callback<NfcState>): void;  差异内容：type: 'nfcStateChange' | api/@ohos.nfc.controller.d.ts |
| 函数变更 | 类名：nfcController；  API声明：function off(type: "nfcStateChange", callback?: Callback<NfcState>): void;  差异内容：type: "nfcStateChange" | 类名：nfcController；  API声明：function off(type: 'nfcStateChange', callback?: Callback<NfcState>): void;  差异内容：type: 'nfcStateChange' | api/@ohos.nfc.controller.d.ts |
| 函数变更 | 类名：wifi；  API声明：function on(type: "wifiStateChange", callback: Callback<number>): void;  差异内容：type: "wifiStateChange" | 类名：wifi；  API声明：function on(type: 'wifiStateChange', callback: Callback<number>): void;  差异内容：type: 'wifiStateChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function off(type: "wifiStateChange", callback?: Callback<number>): void;  差异内容：type: "wifiStateChange" | 类名：wifi；  API声明：function off(type: 'wifiStateChange', callback?: Callback<number>): void;  差异内容：type: 'wifiStateChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function on(type: "wifiConnectionChange", callback: Callback<number>): void;  差异内容：type: "wifiConnectionChange" | 类名：wifi；  API声明：function on(type: 'wifiConnectionChange', callback: Callback<number>): void;  差异内容：type: 'wifiConnectionChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function off(type: "wifiConnectionChange", callback?: Callback<number>): void;  差异内容：type: "wifiConnectionChange" | 类名：wifi；  API声明：function off(type: 'wifiConnectionChange', callback?: Callback<number>): void;  差异内容：type: 'wifiConnectionChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function on(type: "wifiScanStateChange", callback: Callback<number>): void;  差异内容：type: "wifiScanStateChange" | 类名：wifi；  API声明：function on(type: 'wifiScanStateChange', callback: Callback<number>): void;  差异内容：type: 'wifiScanStateChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function off(type: "wifiScanStateChange", callback?: Callback<number>): void;  差异内容：type: "wifiScanStateChange" | 类名：wifi；  API声明：function off(type: 'wifiScanStateChange', callback?: Callback<number>): void;  差异内容：type: 'wifiScanStateChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function on(type: "wifiRssiChange", callback: Callback<number>): void;  差异内容：type: "wifiRssiChange" | 类名：wifi；  API声明：function on(type: 'wifiRssiChange', callback: Callback<number>): void;  差异内容：type: 'wifiRssiChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function off(type: "wifiRssiChange", callback?: Callback<number>): void;  差异内容：type: "wifiRssiChange" | 类名：wifi；  API声明：function off(type: 'wifiRssiChange', callback?: Callback<number>): void;  差异内容：type: 'wifiRssiChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function on(type: "hotspotStateChange", callback: Callback<number>): void;  差异内容：type: "hotspotStateChange" | 类名：wifi；  API声明：function on(type: 'hotspotStateChange', callback: Callback<number>): void;  差异内容：type: 'hotspotStateChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function off(type: "hotspotStateChange", callback?: Callback<number>): void;  差异内容：type: "hotspotStateChange" | 类名：wifi；  API声明：function off(type: 'hotspotStateChange', callback?: Callback<number>): void;  差异内容：type: 'hotspotStateChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function on(type: "p2pStateChange", callback: Callback<number>): void;  差异内容：type: "p2pStateChange" | 类名：wifi；  API声明：function on(type: 'p2pStateChange', callback: Callback<number>): void;  差异内容：type: 'p2pStateChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function off(type: "p2pStateChange", callback?: Callback<number>): void;  差异内容：type: "p2pStateChange" | 类名：wifi；  API声明：function off(type: 'p2pStateChange', callback?: Callback<number>): void;  差异内容：type: 'p2pStateChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function on(type: "p2pConnectionChange", callback: Callback<WifiP2pLinkedInfo>): void;  差异内容：type: "p2pConnectionChange" | 类名：wifi；  API声明：function on(type: 'p2pConnectionChange', callback: Callback<WifiP2pLinkedInfo>): void;  差异内容：type: 'p2pConnectionChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function off(type: "p2pConnectionChange", callback?: Callback<WifiP2pLinkedInfo>): void;  差异内容：type: "p2pConnectionChange" | 类名：wifi；  API声明：function off(type: 'p2pConnectionChange', callback?: Callback<WifiP2pLinkedInfo>): void;  差异内容：type: 'p2pConnectionChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function on(type: "p2pDeviceChange", callback: Callback<WifiP2pDevice>): void;  差异内容：type: "p2pDeviceChange" | 类名：wifi；  API声明：function on(type: 'p2pDeviceChange', callback: Callback<WifiP2pDevice>): void;  差异内容：type: 'p2pDeviceChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function off(type: "p2pDeviceChange", callback?: Callback<WifiP2pDevice>): void;  差异内容：type: "p2pDeviceChange" | 类名：wifi；  API声明：function off(type: 'p2pDeviceChange', callback?: Callback<WifiP2pDevice>): void;  差异内容：type: 'p2pDeviceChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function on(type: "p2pPeerDeviceChange", callback: Callback<WifiP2pDevice[]>): void;  差异内容：type: "p2pPeerDeviceChange" | 类名：wifi；  API声明：function on(type: 'p2pPeerDeviceChange', callback: Callback<WifiP2pDevice[]>): void;  差异内容：type: 'p2pPeerDeviceChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function off(type: "p2pPeerDeviceChange", callback?: Callback<WifiP2pDevice[]>): void;  差异内容：type: "p2pPeerDeviceChange" | 类名：wifi；  API声明：function off(type: 'p2pPeerDeviceChange', callback?: Callback<WifiP2pDevice[]>): void;  差异内容：type: 'p2pPeerDeviceChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function on(type: "p2pPersistentGroupChange", callback: Callback<void>): void;  差异内容：type: "p2pPersistentGroupChange" | 类名：wifi；  API声明：function on(type: 'p2pPersistentGroupChange', callback: Callback<void>): void;  差异内容：type: 'p2pPersistentGroupChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function off(type: "p2pPersistentGroupChange", callback?: Callback<void>): void;  差异内容：type: "p2pPersistentGroupChange" | 类名：wifi；  API声明：function off(type: 'p2pPersistentGroupChange', callback?: Callback<void>): void;  差异内容：type: 'p2pPersistentGroupChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function on(type: "p2pDiscoveryChange", callback: Callback<number>): void;  差异内容：type: "p2pDiscoveryChange" | 类名：wifi；  API声明：function on(type: 'p2pDiscoveryChange', callback: Callback<number>): void;  差异内容：type: 'p2pDiscoveryChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifi；  API声明：function off(type: "p2pDiscoveryChange", callback?: Callback<number>): void;  差异内容：type: "p2pDiscoveryChange" | 类名：wifi；  API声明：function off(type: 'p2pDiscoveryChange', callback?: Callback<number>): void;  差异内容：type: 'p2pDiscoveryChange' | api/@ohos.wifi.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function on(type: "wifiStateChange", callback: Callback<number>): void;  差异内容：type: "wifiStateChange" | 类名：wifiManager；  API声明：function on(type: 'wifiStateChange', callback: Callback<number>): void;  差异内容：type: 'wifiStateChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function off(type: "wifiStateChange", callback?: Callback<number>): void;  差异内容：type: "wifiStateChange" | 类名：wifiManager；  API声明：function off(type: 'wifiStateChange', callback?: Callback<number>): void;  差异内容：type: 'wifiStateChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function on(type: "wifiConnectionChange", callback: Callback<number>): void;  差异内容：type: "wifiConnectionChange" | 类名：wifiManager；  API声明：function on(type: 'wifiConnectionChange', callback: Callback<number>): void;  差异内容：type: 'wifiConnectionChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function off(type: "wifiConnectionChange", callback?: Callback<number>): void;  差异内容：type: "wifiConnectionChange" | 类名：wifiManager；  API声明：function off(type: 'wifiConnectionChange', callback?: Callback<number>): void;  差异内容：type: 'wifiConnectionChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function on(type: "wifiScanStateChange", callback: Callback<number>): void;  差异内容：type: "wifiScanStateChange" | 类名：wifiManager；  API声明：function on(type: 'wifiScanStateChange', callback: Callback<number>): void;  差异内容：type: 'wifiScanStateChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function off(type: "wifiScanStateChange", callback?: Callback<number>): void;  差异内容：type: "wifiScanStateChange" | 类名：wifiManager；  API声明：function off(type: 'wifiScanStateChange', callback?: Callback<number>): void;  差异内容：type: 'wifiScanStateChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function on(type: "wifiRssiChange", callback: Callback<number>): void;  差异内容：type: "wifiRssiChange" | 类名：wifiManager；  API声明：function on(type: 'wifiRssiChange', callback: Callback<number>): void;  差异内容：type: 'wifiRssiChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function off(type: "wifiRssiChange", callback?: Callback<number>): void;  差异内容：type: "wifiRssiChange" | 类名：wifiManager；  API声明：function off(type: 'wifiRssiChange', callback?: Callback<number>): void;  差异内容：type: 'wifiRssiChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function on(type: "hotspotStateChange", callback: Callback<number>): void;  差异内容：type: "hotspotStateChange" | 类名：wifiManager；  API声明：function on(type: 'hotspotStateChange', callback: Callback<number>): void;  差异内容：type: 'hotspotStateChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function off(type: "hotspotStateChange", callback?: Callback<number>): void;  差异内容：type: "hotspotStateChange" | 类名：wifiManager；  API声明：function off(type: 'hotspotStateChange', callback?: Callback<number>): void;  差异内容：type: 'hotspotStateChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function on(type: "p2pStateChange", callback: Callback<number>): void;  差异内容：type: "p2pStateChange" | 类名：wifiManager；  API声明：function on(type: 'p2pStateChange', callback: Callback<number>): void;  差异内容：type: 'p2pStateChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function off(type: "p2pStateChange", callback?: Callback<number>): void;  差异内容：type: "p2pStateChange" | 类名：wifiManager；  API声明：function off(type: 'p2pStateChange', callback?: Callback<number>): void;  差异内容：type: 'p2pStateChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function on(type: "p2pConnectionChange", callback: Callback<WifiP2pLinkedInfo>): void;  差异内容：type: "p2pConnectionChange" | 类名：wifiManager；  API声明：function on(type: 'p2pConnectionChange', callback: Callback<WifiP2pLinkedInfo>): void;  差异内容：type: 'p2pConnectionChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function off(type: "p2pConnectionChange", callback?: Callback<WifiP2pLinkedInfo>): void;  差异内容：type: "p2pConnectionChange" | 类名：wifiManager；  API声明：function off(type: 'p2pConnectionChange', callback?: Callback<WifiP2pLinkedInfo>): void;  差异内容：type: 'p2pConnectionChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function on(type: "p2pDeviceChange", callback: Callback<WifiP2pDevice>): void;  差异内容：type: "p2pDeviceChange" | 类名：wifiManager；  API声明：function on(type: 'p2pDeviceChange', callback: Callback<WifiP2pDevice>): void;  差异内容：type: 'p2pDeviceChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function off(type: "p2pDeviceChange", callback?: Callback<WifiP2pDevice>): void;  差异内容：type: "p2pDeviceChange" | 类名：wifiManager；  API声明：function off(type: 'p2pDeviceChange', callback?: Callback<WifiP2pDevice>): void;  差异内容：type: 'p2pDeviceChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function on(type: "p2pPeerDeviceChange", callback: Callback<WifiP2pDevice[]>): void;  差异内容：type: "p2pPeerDeviceChange" | 类名：wifiManager；  API声明：function on(type: 'p2pPeerDeviceChange', callback: Callback<WifiP2pDevice[]>): void;  差异内容：type: 'p2pPeerDeviceChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function off(type: "p2pPeerDeviceChange", callback?: Callback<WifiP2pDevice[]>): void;  差异内容：type: "p2pPeerDeviceChange" | 类名：wifiManager；  API声明：function off(type: 'p2pPeerDeviceChange', callback?: Callback<WifiP2pDevice[]>): void;  差异内容：type: 'p2pPeerDeviceChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function on(type: "p2pPersistentGroupChange", callback: Callback<void>): void;  差异内容：type: "p2pPersistentGroupChange" | 类名：wifiManager；  API声明：function on(type: 'p2pPersistentGroupChange', callback: Callback<void>): void;  差异内容：type: 'p2pPersistentGroupChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function off(type: "p2pPersistentGroupChange", callback?: Callback<void>): void;  差异内容：type: "p2pPersistentGroupChange" | 类名：wifiManager；  API声明：function off(type: 'p2pPersistentGroupChange', callback?: Callback<void>): void;  差异内容：type: 'p2pPersistentGroupChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function on(type: "p2pDiscoveryChange", callback: Callback<number>): void;  差异内容：type: "p2pDiscoveryChange" | 类名：wifiManager；  API声明：function on(type: 'p2pDiscoveryChange', callback: Callback<number>): void;  差异内容：type: 'p2pDiscoveryChange' | api/@ohos.wifiManager.d.ts |
| 函数变更 | 类名：wifiManager；  API声明：function off(type: "p2pDiscoveryChange", callback?: Callback<number>): void;  差异内容：type: "p2pDiscoveryChange" | 类名：wifiManager；  API声明：function off(type: 'p2pDiscoveryChange', callback?: Callback<number>): void;  差异内容：type: 'p2pDiscoveryChange' | api/@ohos.wifiManager.d.ts |
| 属性变更 | 类名：BluetoothDevice；  API声明：addrType: "public" | "random";  差异内容："public","random" | 类名：BluetoothDevice；  API声明：addrType: 'public' | 'random';  差异内容：'public','random' | api/@system.bluetooth.d.ts |
| 新增API | NA | 类名：tag；  API声明：function registerForegroundDispatch(elementName: ElementName, discTech: number[], callback: AsyncCallback<TagInfo>): void;  差异内容：function registerForegroundDispatch(elementName: ElementName, discTech: number[], callback: AsyncCallback<TagInfo>): void; | api/@ohos.nfc.tag.d.ts |
| 新增API | NA | 类名：tag；  API声明：function unregisterForegroundDispatch(elementName: ElementName): void;  差异内容：function unregisterForegroundDispatch(elementName: ElementName): void; | api/@ohos.nfc.tag.d.ts |
| 新增API | NA | 类名：tag；  API声明：function on(type: 'readerMode', elementName: ElementName, discTech: number[], callback: AsyncCallback<TagInfo>): void;  差异内容：function on(type: 'readerMode', elementName: ElementName, discTech: number[], callback: AsyncCallback<TagInfo>): void; | api/@ohos.nfc.tag.d.ts |
| 新增API | NA | 类名：tag；  API声明：function off(type: 'readerMode', elementName: ElementName, callback?: AsyncCallback<TagInfo>): void;  差异内容：function off(type: 'readerMode', elementName: ElementName, callback?: AsyncCallback<TagInfo>): void; | api/@ohos.nfc.tag.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：function getScanInfoList(): Array<WifiScanInfo>;  差异内容：function getScanInfoList(): Array<WifiScanInfo>; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：function getIpv6Info(): Ipv6Info;  差异内容：function getIpv6Info(): Ipv6Info; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：function isBandTypeSupported(bandType: WifiBandType): boolean;  差异内容：function isBandTypeSupported(bandType: WifiBandType): boolean; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：function isMeteredHotspot(): boolean;  差异内容：function isMeteredHotspot(): boolean; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明： enum DeviceAddressType  差异内容： enum DeviceAddressType | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：DeviceAddressType；  API声明：RANDOM\_DEVICE\_ADDRESS  差异内容：RANDOM\_DEVICE\_ADDRESS | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：DeviceAddressType；  API声明：REAL\_DEVICE\_ADDRESS  差异内容：REAL\_DEVICE\_ADDRESS | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明： enum EapMethod  差异内容： enum EapMethod | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：EapMethod；  API声明：EAP\_NONE  差异内容：EAP\_NONE | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：EapMethod；  API声明：EAP\_PEAP  差异内容：EAP\_PEAP | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：EapMethod；  API声明：EAP\_TLS  差异内容：EAP\_TLS | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：EapMethod；  API声明：EAP\_TTLS  差异内容：EAP\_TTLS | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：EapMethod；  API声明：EAP\_PWD  差异内容：EAP\_PWD | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：EapMethod；  API声明：EAP\_SIM  差异内容：EAP\_SIM | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：EapMethod；  API声明：EAP\_AKA  差异内容：EAP\_AKA | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：EapMethod；  API声明：EAP\_AKA\_PRIME  差异内容：EAP\_AKA\_PRIME | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：EapMethod；  API声明：EAP\_UNAUTH\_TLS  差异内容：EAP\_UNAUTH\_TLS | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明： enum Phase2Method  差异内容： enum Phase2Method | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：Phase2Method；  API声明：PHASE2\_NONE  差异内容：PHASE2\_NONE | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：Phase2Method；  API声明：PHASE2\_PAP  差异内容：PHASE2\_PAP | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：Phase2Method；  API声明：PHASE2\_MSCHAP  差异内容：PHASE2\_MSCHAP | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：Phase2Method；  API声明：PHASE2\_MSCHAPV2  差异内容：PHASE2\_MSCHAPV2 | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：Phase2Method；  API声明：PHASE2\_GTC  差异内容：PHASE2\_GTC | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：Phase2Method；  API声明：PHASE2\_SIM  差异内容：PHASE2\_SIM | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：Phase2Method；  API声明：PHASE2\_AKA  差异内容：PHASE2\_AKA | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：Phase2Method；  API声明：PHASE2\_AKA\_PRIME  差异内容：PHASE2\_AKA\_PRIME | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明： interface WifiEapConfig  差异内容： interface WifiEapConfig | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiEapConfig；  API声明：eapMethod: EapMethod;  差异内容：eapMethod: EapMethod; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiEapConfig；  API声明：phase2Method: Phase2Method;  差异内容：phase2Method: Phase2Method; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiEapConfig；  API声明：identity: string;  差异内容：identity: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiEapConfig；  API声明：anonymousIdentity: string;  差异内容：anonymousIdentity: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiEapConfig；  API声明：password: string;  差异内容：password: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiEapConfig；  API声明：caCertAlias: string;  差异内容：caCertAlias: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiEapConfig；  API声明：caPath: string;  差异内容：caPath: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiEapConfig；  API声明：clientCertAlias: string;  差异内容：clientCertAlias: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiEapConfig；  API声明：certEntry: Uint8Array;  差异内容：certEntry: Uint8Array; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiEapConfig；  API声明：certPassword: string;  差异内容：certPassword: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiEapConfig；  API声明：altSubjectMatch: string;  差异内容：altSubjectMatch: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiEapConfig；  API声明：domainSuffixMatch: string;  差异内容：domainSuffixMatch: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiEapConfig；  API声明：realm: string;  差异内容：realm: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiEapConfig；  API声明：plmn: string;  差异内容：plmn: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiEapConfig；  API声明：eapSubId: number;  差异内容：eapSubId: number; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiDeviceConfig；  API声明：bssidType?: DeviceAddressType;  差异内容：bssidType?: DeviceAddressType; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiDeviceConfig；  API声明：eapConfig?: WifiEapConfig;  差异内容：eapConfig?: WifiEapConfig; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiScanInfo；  API声明：bssidType: DeviceAddressType;  差异内容：bssidType: DeviceAddressType; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiScanInfo；  API声明：supportedWifiCategory: WifiCategory;  差异内容：supportedWifiCategory: WifiCategory; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiScanInfo；  API声明：isHiLinkNetwork: boolean;  差异内容：isHiLinkNetwork: boolean; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明： enum WifiBandType  差异内容： enum WifiBandType | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiBandType；  API声明：WIFI\_BAND\_NONE  差异内容：WIFI\_BAND\_NONE | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiBandType；  API声明：WIFI\_BAND\_2G  差异内容：WIFI\_BAND\_2G | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiBandType；  API声明：WIFI\_BAND\_5G  差异内容：WIFI\_BAND\_5G | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiBandType；  API声明：WIFI\_BAND\_6G  差异内容：WIFI\_BAND\_6G | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiBandType；  API声明：WIFI\_BAND\_60G  差异内容：WIFI\_BAND\_60G | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明： enum WifiStandard  差异内容： enum WifiStandard | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiStandard；  API声明：WIFI\_STANDARD\_UNDEFINED  差异内容：WIFI\_STANDARD\_UNDEFINED | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiStandard；  API声明：WIFI\_STANDARD\_11A  差异内容：WIFI\_STANDARD\_11A | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiStandard；  API声明：WIFI\_STANDARD\_11B  差异内容：WIFI\_STANDARD\_11B | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiStandard；  API声明：WIFI\_STANDARD\_11G  差异内容：WIFI\_STANDARD\_11G | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiStandard；  API声明：WIFI\_STANDARD\_11N  差异内容：WIFI\_STANDARD\_11N | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiStandard；  API声明：WIFI\_STANDARD\_11AC  差异内容：WIFI\_STANDARD\_11AC | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiStandard；  API声明：WIFI\_STANDARD\_11AX  差异内容：WIFI\_STANDARD\_11AX | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiStandard；  API声明：WIFI\_STANDARD\_11AD  差异内容：WIFI\_STANDARD\_11AD | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiLinkedInfo；  API声明：rxLinkSpeed: number;  差异内容：rxLinkSpeed: number; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiLinkedInfo；  API声明：maxSupportedTxLinkSpeed: number;  差异内容：maxSupportedTxLinkSpeed: number; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiLinkedInfo；  API声明：maxSupportedRxLinkSpeed: number;  差异内容：maxSupportedRxLinkSpeed: number; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiLinkedInfo；  API声明：channelWidth: WifiChannelWidth;  差异内容：channelWidth: WifiChannelWidth; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiLinkedInfo；  API声明：wifiStandard: WifiStandard;  差异内容：wifiStandard: WifiStandard; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiLinkedInfo；  API声明：supportedWifiCategory: WifiCategory;  差异内容：supportedWifiCategory: WifiCategory; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiLinkedInfo；  API声明：isHiLinkNetwork: boolean;  差异内容：isHiLinkNetwork: boolean; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明： interface Ipv6Info  差异内容： interface Ipv6Info | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：Ipv6Info；  API声明：linkIpv6Address: string;  差异内容：linkIpv6Address: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：Ipv6Info；  API声明：globalIpv6Address: string;  差异内容：globalIpv6Address: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：Ipv6Info；  API声明：randomGlobalIpv6Address: string;  差异内容：randomGlobalIpv6Address: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：Ipv6Info；  API声明：gateway: string;  差异内容：gateway: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：Ipv6Info；  API声明：netmask: string;  差异内容：netmask: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：Ipv6Info；  API声明：primaryDNS: string;  差异内容：primaryDNS: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：Ipv6Info；  API声明：secondDNS: string;  差异内容：secondDNS: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiP2pDevice；  API声明：deviceAddressType?: DeviceAddressType;  差异内容：deviceAddressType?: DeviceAddressType; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiP2PConfig；  API声明：deviceAddressType?: DeviceAddressType;  差异内容：deviceAddressType?: DeviceAddressType; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace a2dp  差异内容： declare namespace a2dp | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：a2dp；  API声明：type BaseProfile = baseProfile.BaseProfile;  差异内容：type BaseProfile = baseProfile.BaseProfile; | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：a2dp；  API声明：function createA2dpSrcProfile(): A2dpSourceProfile;  差异内容：function createA2dpSrcProfile(): A2dpSourceProfile; | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：a2dp；  API声明： interface A2dpSourceProfile  差异内容： interface A2dpSourceProfile | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：A2dpSourceProfile；  API声明：getPlayingState(deviceId: string): PlayingState;  差异内容：getPlayingState(deviceId: string): PlayingState; | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：a2dp；  API声明： interface CodecInfo  差异内容： interface CodecInfo | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecInfo；  API声明：codecType: CodecType;  差异内容：codecType: CodecType; | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecInfo；  API声明：codecBitsPerSample: CodecBitsPerSample;  差异内容：codecBitsPerSample: CodecBitsPerSample; | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecInfo；  API声明：codecChannelMode: CodecChannelMode;  差异内容：codecChannelMode: CodecChannelMode; | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecInfo；  API声明：codecSampleRate: CodecSampleRate;  差异内容：codecSampleRate: CodecSampleRate; | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：a2dp；  API声明： enum PlayingState  差异内容： enum PlayingState | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：PlayingState；  API声明：STATE\_NOT\_PLAYING  差异内容：STATE\_NOT\_PLAYING | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：PlayingState；  API声明：STATE\_PLAYING  差异内容：STATE\_PLAYING | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：a2dp；  API声明： enum CodecType  差异内容： enum CodecType | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecType；  API声明：CODEC\_TYPE\_INVALID = -1  差异内容：CODEC\_TYPE\_INVALID = -1 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecType；  API声明：CODEC\_TYPE\_SBC = 0  差异内容：CODEC\_TYPE\_SBC = 0 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecType；  API声明：CODEC\_TYPE\_AAC = 1  差异内容：CODEC\_TYPE\_AAC = 1 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecType；  API声明：CODEC\_TYPE\_L2HC = 2  差异内容：CODEC\_TYPE\_L2HC = 2 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：a2dp；  API声明： enum CodecChannelMode  差异内容： enum CodecChannelMode | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecChannelMode；  API声明：CODEC\_CHANNEL\_MODE\_NONE = 0  差异内容：CODEC\_CHANNEL\_MODE\_NONE = 0 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecChannelMode；  API声明：CODEC\_CHANNEL\_MODE\_MONO = 1  差异内容：CODEC\_CHANNEL\_MODE\_MONO = 1 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecChannelMode；  API声明：CODEC\_CHANNEL\_MODE\_STEREO = 2  差异内容：CODEC\_CHANNEL\_MODE\_STEREO = 2 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：a2dp；  API声明： enum CodecBitsPerSample  差异内容： enum CodecBitsPerSample | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecBitsPerSample；  API声明：CODEC\_BITS\_PER\_SAMPLE\_NONE = 0  差异内容：CODEC\_BITS\_PER\_SAMPLE\_NONE = 0 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecBitsPerSample；  API声明：CODEC\_BITS\_PER\_SAMPLE\_16 = 1  差异内容：CODEC\_BITS\_PER\_SAMPLE\_16 = 1 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecBitsPerSample；  API声明：CODEC\_BITS\_PER\_SAMPLE\_24 = 2  差异内容：CODEC\_BITS\_PER\_SAMPLE\_24 = 2 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecBitsPerSample；  API声明：CODEC\_BITS\_PER\_SAMPLE\_32 = 3  差异内容：CODEC\_BITS\_PER\_SAMPLE\_32 = 3 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：a2dp；  API声明： enum CodecSampleRate  差异内容： enum CodecSampleRate | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecSampleRate；  API声明：CODEC\_SAMPLE\_RATE\_NONE = 0  差异内容：CODEC\_SAMPLE\_RATE\_NONE = 0 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecSampleRate；  API声明：CODEC\_SAMPLE\_RATE\_44100 = 1  差异内容：CODEC\_SAMPLE\_RATE\_44100 = 1 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecSampleRate；  API声明：CODEC\_SAMPLE\_RATE\_48000 = 2  差异内容：CODEC\_SAMPLE\_RATE\_48000 = 2 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecSampleRate；  API声明：CODEC\_SAMPLE\_RATE\_88200 = 3  差异内容：CODEC\_SAMPLE\_RATE\_88200 = 3 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecSampleRate；  API声明：CODEC\_SAMPLE\_RATE\_96000 = 4  差异内容：CODEC\_SAMPLE\_RATE\_96000 = 4 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecSampleRate；  API声明：CODEC\_SAMPLE\_RATE\_176400 = 5  差异内容：CODEC\_SAMPLE\_RATE\_176400 = 5 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecSampleRate；  API声明：CODEC\_SAMPLE\_RATE\_192000 = 6  差异内容：CODEC\_SAMPLE\_RATE\_192000 = 6 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace access  差异内容： declare namespace access | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：access；  API声明：function enableBluetooth(): void;  差异内容：function enableBluetooth(): void; | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：access；  API声明：function disableBluetooth(): void;  差异内容：function disableBluetooth(): void; | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：access；  API声明：function getState(): BluetoothState;  差异内容：function getState(): BluetoothState; | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：access；  API声明：function on(type: 'stateChange', callback: Callback<BluetoothState>): void;  差异内容：function on(type: 'stateChange', callback: Callback<BluetoothState>): void; | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：access；  API声明：function off(type: 'stateChange', callback?: Callback<BluetoothState>): void;  差异内容：function off(type: 'stateChange', callback?: Callback<BluetoothState>): void; | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：access；  API声明： export enum BluetoothState  差异内容： export enum BluetoothState | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：BluetoothState；  API声明：STATE\_OFF = 0  差异内容：STATE\_OFF = 0 | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：BluetoothState；  API声明：STATE\_TURNING\_ON = 1  差异内容：STATE\_TURNING\_ON = 1 | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：BluetoothState；  API声明：STATE\_ON = 2  差异内容：STATE\_ON = 2 | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：BluetoothState；  API声明：STATE\_TURNING\_OFF = 3  差异内容：STATE\_TURNING\_OFF = 3 | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：BluetoothState；  API声明：STATE\_BLE\_TURNING\_ON = 4  差异内容：STATE\_BLE\_TURNING\_ON = 4 | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：BluetoothState；  API声明：STATE\_BLE\_ON = 5  差异内容：STATE\_BLE\_ON = 5 | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：BluetoothState；  API声明：STATE\_BLE\_TURNING\_OFF = 6  差异内容：STATE\_BLE\_TURNING\_OFF = 6 | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace baseProfile  差异内容： declare namespace baseProfile | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：baseProfile；  API声明：type ProfileConnectionState = constant.ProfileConnectionState;  差异内容：type ProfileConnectionState = constant.ProfileConnectionState; | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：baseProfile；  API声明： enum DisconnectCause  差异内容： enum DisconnectCause | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：DisconnectCause；  API声明：USER\_DISCONNECT = 0  差异内容：USER\_DISCONNECT = 0 | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：DisconnectCause；  API声明：CONNECT\_FROM\_KEYBOARD = 1  差异内容：CONNECT\_FROM\_KEYBOARD = 1 | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：DisconnectCause；  API声明：CONNECT\_FROM\_MOUSE = 2  差异内容：CONNECT\_FROM\_MOUSE = 2 | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：DisconnectCause；  API声明：CONNECT\_FROM\_CAR = 3  差异内容：CONNECT\_FROM\_CAR = 3 | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：DisconnectCause；  API声明：TOO\_MANY\_CONNECTED\_DEVICES = 4  差异内容：TOO\_MANY\_CONNECTED\_DEVICES = 4 | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：DisconnectCause；  API声明：CONNECT\_FAIL\_INTERNAL = 5  差异内容：CONNECT\_FAIL\_INTERNAL = 5 | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：baseProfile；  API声明： export interface StateChangeParam  差异内容： export interface StateChangeParam | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：StateChangeParam；  API声明：deviceId: string;  差异内容：deviceId: string; | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：StateChangeParam；  API声明：state: ProfileConnectionState;  差异内容：state: ProfileConnectionState; | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：StateChangeParam；  API声明：cause: DisconnectCause;  差异内容：cause: DisconnectCause; | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：baseProfile；  API声明： export interface BaseProfile  差异内容： export interface BaseProfile | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：BaseProfile；  API声明：getConnectedDevices(): Array<string>;  差异内容：getConnectedDevices(): Array<string>; | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：BaseProfile；  API声明：getConnectionState(deviceId: string): ProfileConnectionState;  差异内容：getConnectionState(deviceId: string): ProfileConnectionState; | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：BaseProfile；  API声明：on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void;  差异内容：on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void; | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：BaseProfile；  API声明：off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void;  差异内容：off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void; | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace ble  差异内容： declare namespace ble | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：type ProfileConnectionState = constant.ProfileConnectionState;  差异内容：type ProfileConnectionState = constant.ProfileConnectionState; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：function createGattServer(): GattServer;  差异内容：function createGattServer(): GattServer; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：function createGattClientDevice(deviceId: string): GattClientDevice;  差异内容：function createGattClientDevice(deviceId: string): GattClientDevice; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：function getConnectedBLEDevices(): Array<string>;  差异内容：function getConnectedBLEDevices(): Array<string>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：function startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void;  差异内容：function startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：function stopBLEScan(): void;  差异内容：function stopBLEScan(): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：function startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void;  差异内容：function startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：function startAdvertising(advertisingParams: AdvertisingParams, callback: AsyncCallback<number>): void;  差异内容：function startAdvertising(advertisingParams: AdvertisingParams, callback: AsyncCallback<number>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：function startAdvertising(advertisingParams: AdvertisingParams): Promise<number>;  差异内容：function startAdvertising(advertisingParams: AdvertisingParams): Promise<number>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：function stopAdvertising(): void;  差异内容：function stopAdvertising(): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：function stopAdvertising(advertisingId: number, callback: AsyncCallback<void>): void;  差异内容：function stopAdvertising(advertisingId: number, callback: AsyncCallback<void>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：function stopAdvertising(advertisingId: number): Promise<void>;  差异内容：function stopAdvertising(advertisingId: number): Promise<void>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：function enableAdvertising(advertisingEnableParams: AdvertisingEnableParams, callback: AsyncCallback<void>): void;  差异内容：function enableAdvertising(advertisingEnableParams: AdvertisingEnableParams, callback: AsyncCallback<void>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：function enableAdvertising(advertisingEnableParams: AdvertisingEnableParams): Promise<void>;  差异内容：function enableAdvertising(advertisingEnableParams: AdvertisingEnableParams): Promise<void>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：function disableAdvertising(advertisingDisableParams: AdvertisingDisableParams, callback: AsyncCallback<void>): void;  差异内容：function disableAdvertising(advertisingDisableParams: AdvertisingDisableParams, callback: AsyncCallback<void>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：function disableAdvertising(advertisingDisableParams: AdvertisingDisableParams): Promise<void>;  差异内容：function disableAdvertising(advertisingDisableParams: AdvertisingDisableParams): Promise<void>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：function on(type: 'advertisingStateChange', callback: Callback<AdvertisingStateChangeInfo>): void;  差异内容：function on(type: 'advertisingStateChange', callback: Callback<AdvertisingStateChangeInfo>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：function off(type: 'advertisingStateChange', callback?: Callback<AdvertisingStateChangeInfo>): void;  差异内容：function off(type: 'advertisingStateChange', callback?: Callback<AdvertisingStateChangeInfo>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：function on(type: 'BLEDeviceFind', callback: Callback<Array<ScanResult>>): void;  差异内容：function on(type: 'BLEDeviceFind', callback: Callback<Array<ScanResult>>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：function off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void;  差异内容：function off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface GattServer  差异内容： interface GattServer | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：addService(service: GattService): void;  差异内容：addService(service: GattService): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：removeService(serviceUuid: string): void;  差异内容：removeService(serviceUuid: string): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：close(): void;  差异内容：close(): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic, callback: AsyncCallback<void>): void;  差异内容：notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic, callback: AsyncCallback<void>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic): Promise<void>;  差异内容：notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic): Promise<void>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：sendResponse(serverResponse: ServerResponse): void;  差异内容：sendResponse(serverResponse: ServerResponse): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：on(type: 'characteristicRead', callback: Callback<CharacteristicReadRequest>): void;  差异内容：on(type: 'characteristicRead', callback: Callback<CharacteristicReadRequest>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：off(type: 'characteristicRead', callback?: Callback<CharacteristicReadRequest>): void;  差异内容：off(type: 'characteristicRead', callback?: Callback<CharacteristicReadRequest>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：on(type: 'characteristicWrite', callback: Callback<CharacteristicWriteRequest>): void;  差异内容：on(type: 'characteristicWrite', callback: Callback<CharacteristicWriteRequest>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：off(type: 'characteristicWrite', callback?: Callback<CharacteristicWriteRequest>): void;  差异内容：off(type: 'characteristicWrite', callback?: Callback<CharacteristicWriteRequest>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：on(type: 'descriptorRead', callback: Callback<DescriptorReadRequest>): void;  差异内容：on(type: 'descriptorRead', callback: Callback<DescriptorReadRequest>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：off(type: 'descriptorRead', callback?: Callback<DescriptorReadRequest>): void;  差异内容：off(type: 'descriptorRead', callback?: Callback<DescriptorReadRequest>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：on(type: 'descriptorWrite', callback: Callback<DescriptorWriteRequest>): void;  差异内容：on(type: 'descriptorWrite', callback: Callback<DescriptorWriteRequest>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：off(type: 'descriptorWrite', callback?: Callback<DescriptorWriteRequest>): void;  差异内容：off(type: 'descriptorWrite', callback?: Callback<DescriptorWriteRequest>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：on(type: 'connectionStateChange', callback: Callback<BLEConnectionChangeState>): void;  差异内容：on(type: 'connectionStateChange', callback: Callback<BLEConnectionChangeState>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：off(type: 'connectionStateChange', callback?: Callback<BLEConnectionChangeState>): void;  差异内容：off(type: 'connectionStateChange', callback?: Callback<BLEConnectionChangeState>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：on(type: 'BLEMtuChange', callback: Callback<number>): void;  差异内容：on(type: 'BLEMtuChange', callback: Callback<number>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：off(type: 'BLEMtuChange', callback?: Callback<number>): void;  差异内容：off(type: 'BLEMtuChange', callback?: Callback<number>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface GattClientDevice  差异内容： interface GattClientDevice | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：connect(): void;  差异内容：connect(): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：disconnect(): void;  差异内容：disconnect(): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：close(): void;  差异内容：close(): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：getDeviceName(callback: AsyncCallback<string>): void;  差异内容：getDeviceName(callback: AsyncCallback<string>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：getDeviceName(): Promise<string>;  差异内容：getDeviceName(): Promise<string>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：getServices(callback: AsyncCallback<Array<GattService>>): void;  差异内容：getServices(callback: AsyncCallback<Array<GattService>>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：getServices(): Promise<Array<GattService>>;  差异内容：getServices(): Promise<Array<GattService>>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：readCharacteristicValue(characteristic: BLECharacteristic, callback: AsyncCallback<BLECharacteristic>): void;  差异内容：readCharacteristicValue(characteristic: BLECharacteristic, callback: AsyncCallback<BLECharacteristic>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>;  差异内容：readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：readDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<BLEDescriptor>): void;  差异内容：readDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<BLEDescriptor>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>;  差异内容：readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：writeCharacteristicValue(characteristic: BLECharacteristic, writeType: GattWriteType, callback: AsyncCallback<void>): void;  差异内容：writeCharacteristicValue(characteristic: BLECharacteristic, writeType: GattWriteType, callback: AsyncCallback<void>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：writeCharacteristicValue(characteristic: BLECharacteristic, writeType: GattWriteType): Promise<void>;  差异内容：writeCharacteristicValue(characteristic: BLECharacteristic, writeType: GattWriteType): Promise<void>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：writeDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<void>): void;  差异内容：writeDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<void>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：writeDescriptorValue(descriptor: BLEDescriptor): Promise<void>;  差异内容：writeDescriptorValue(descriptor: BLEDescriptor): Promise<void>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：getRssiValue(callback: AsyncCallback<number>): void;  差异内容：getRssiValue(callback: AsyncCallback<number>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：getRssiValue(): Promise<number>;  差异内容：getRssiValue(): Promise<number>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：setBLEMtuSize(mtu: number): void;  差异内容：setBLEMtuSize(mtu: number): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：setCharacteristicChangeNotification(characteristic: BLECharacteristic, enable: boolean, callback: AsyncCallback<void>): void;  差异内容：setCharacteristicChangeNotification(characteristic: BLECharacteristic, enable: boolean, callback: AsyncCallback<void>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：setCharacteristicChangeNotification(characteristic: BLECharacteristic, enable: boolean): Promise<void>;  差异内容：setCharacteristicChangeNotification(characteristic: BLECharacteristic, enable: boolean): Promise<void>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：setCharacteristicChangeIndication(characteristic: BLECharacteristic, enable: boolean, callback: AsyncCallback<void>): void;  差异内容：setCharacteristicChangeIndication(characteristic: BLECharacteristic, enable: boolean, callback: AsyncCallback<void>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：setCharacteristicChangeIndication(characteristic: BLECharacteristic, enable: boolean): Promise<void>;  差异内容：setCharacteristicChangeIndication(characteristic: BLECharacteristic, enable: boolean): Promise<void>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：on(type: 'BLECharacteristicChange', callback: Callback<BLECharacteristic>): void;  差异内容：on(type: 'BLECharacteristicChange', callback: Callback<BLECharacteristic>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：off(type: 'BLECharacteristicChange', callback?: Callback<BLECharacteristic>): void;  差异内容：off(type: 'BLECharacteristicChange', callback?: Callback<BLECharacteristic>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：on(type: 'BLEConnectionStateChange', callback: Callback<BLEConnectionChangeState>): void;  差异内容：on(type: 'BLEConnectionStateChange', callback: Callback<BLEConnectionChangeState>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：off(type: 'BLEConnectionStateChange', callback?: Callback<BLEConnectionChangeState>): void;  差异内容：off(type: 'BLEConnectionStateChange', callback?: Callback<BLEConnectionChangeState>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：on(type: 'BLEMtuChange', callback: Callback<number>): void;  差异内容：on(type: 'BLEMtuChange', callback: Callback<number>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：off(type: 'BLEMtuChange', callback?: Callback<number>): void;  差异内容：off(type: 'BLEMtuChange', callback?: Callback<number>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface GattService  差异内容： interface GattService | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattService；  API声明：serviceUuid: string;  差异内容：serviceUuid: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattService；  API声明：isPrimary: boolean;  差异内容：isPrimary: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattService；  API声明：characteristics: Array<BLECharacteristic>;  差异内容：characteristics: Array<BLECharacteristic>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattService；  API声明：includeServices?: Array<GattService>;  差异内容：includeServices?: Array<GattService>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface BLECharacteristic  差异内容： interface BLECharacteristic | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BLECharacteristic；  API声明：serviceUuid: string;  差异内容：serviceUuid: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BLECharacteristic；  API声明：characteristicUuid: string;  差异内容：characteristicUuid: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BLECharacteristic；  API声明：characteristicValue: ArrayBuffer;  差异内容：characteristicValue: ArrayBuffer; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BLECharacteristic；  API声明：descriptors: Array<BLEDescriptor>;  差异内容：descriptors: Array<BLEDescriptor>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BLECharacteristic；  API声明：properties?: GattProperties;  差异内容：properties?: GattProperties; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface BLEDescriptor  差异内容： interface BLEDescriptor | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BLEDescriptor；  API声明：serviceUuid: string;  差异内容：serviceUuid: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BLEDescriptor；  API声明：characteristicUuid: string;  差异内容：characteristicUuid: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BLEDescriptor；  API声明：descriptorUuid: string;  差异内容：descriptorUuid: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BLEDescriptor；  API声明：descriptorValue: ArrayBuffer;  差异内容：descriptorValue: ArrayBuffer; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface NotifyCharacteristic  差异内容： interface NotifyCharacteristic | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：NotifyCharacteristic；  API声明：serviceUuid: string;  差异内容：serviceUuid: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：NotifyCharacteristic；  API声明：characteristicUuid: string;  差异内容：characteristicUuid: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：NotifyCharacteristic；  API声明：characteristicValue: ArrayBuffer;  差异内容：characteristicValue: ArrayBuffer; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：NotifyCharacteristic；  API声明：confirm: boolean;  差异内容：confirm: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface CharacteristicReadRequest  差异内容： interface CharacteristicReadRequest | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：CharacteristicReadRequest；  API声明：deviceId: string;  差异内容：deviceId: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：CharacteristicReadRequest；  API声明：transId: number;  差异内容：transId: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：CharacteristicReadRequest；  API声明：offset: number;  差异内容：offset: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：CharacteristicReadRequest；  API声明：characteristicUuid: string;  差异内容：characteristicUuid: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：CharacteristicReadRequest；  API声明：serviceUuid: string;  差异内容：serviceUuid: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface CharacteristicWriteRequest  差异内容： interface CharacteristicWriteRequest | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：CharacteristicWriteRequest；  API声明：deviceId: string;  差异内容：deviceId: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：CharacteristicWriteRequest；  API声明：transId: number;  差异内容：transId: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：CharacteristicWriteRequest；  API声明：offset: number;  差异内容：offset: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：CharacteristicWriteRequest；  API声明：isPrepared: boolean;  差异内容：isPrepared: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：CharacteristicWriteRequest；  API声明：needRsp: boolean;  差异内容：needRsp: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：CharacteristicWriteRequest；  API声明：value: ArrayBuffer;  差异内容：value: ArrayBuffer; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：CharacteristicWriteRequest；  API声明：characteristicUuid: string;  差异内容：characteristicUuid: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：CharacteristicWriteRequest；  API声明：serviceUuid: string;  差异内容：serviceUuid: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface DescriptorReadRequest  差异内容： interface DescriptorReadRequest | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：DescriptorReadRequest；  API声明：deviceId: string;  差异内容：deviceId: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：DescriptorReadRequest；  API声明：transId: number;  差异内容：transId: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：DescriptorReadRequest；  API声明：offset: number;  差异内容：offset: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：DescriptorReadRequest；  API声明：descriptorUuid: string;  差异内容：descriptorUuid: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：DescriptorReadRequest；  API声明：characteristicUuid: string;  差异内容：characteristicUuid: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：DescriptorReadRequest；  API声明：serviceUuid: string;  差异内容：serviceUuid: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface DescriptorWriteRequest  差异内容： interface DescriptorWriteRequest | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：DescriptorWriteRequest；  API声明：deviceId: string;  差异内容：deviceId: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：DescriptorWriteRequest；  API声明：transId: number;  差异内容：transId: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：DescriptorWriteRequest；  API声明：offset: number;  差异内容：offset: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：DescriptorWriteRequest；  API声明：isPrepared: boolean;  差异内容：isPrepared: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：DescriptorWriteRequest；  API声明：needRsp: boolean;  差异内容：needRsp: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：DescriptorWriteRequest；  API声明：value: ArrayBuffer;  差异内容：value: ArrayBuffer; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：DescriptorWriteRequest；  API声明：descriptorUuid: string;  差异内容：descriptorUuid: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：DescriptorWriteRequest；  API声明：characteristicUuid: string;  差异内容：characteristicUuid: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：DescriptorWriteRequest；  API声明：serviceUuid: string;  差异内容：serviceUuid: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface ServerResponse  差异内容： interface ServerResponse | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ServerResponse；  API声明：deviceId: string;  差异内容：deviceId: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ServerResponse；  API声明：transId: number;  差异内容：transId: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ServerResponse；  API声明：status: number;  差异内容：status: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ServerResponse；  API声明：offset: number;  差异内容：offset: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ServerResponse；  API声明：value: ArrayBuffer;  差异内容：value: ArrayBuffer; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface BLEConnectionChangeState  差异内容： interface BLEConnectionChangeState | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BLEConnectionChangeState；  API声明：deviceId: string;  差异内容：deviceId: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BLEConnectionChangeState；  API声明：state: ProfileConnectionState;  差异内容：state: ProfileConnectionState; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface ScanResult  差异内容： interface ScanResult | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanResult；  API声明：deviceId: string;  差异内容：deviceId: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanResult；  API声明：rssi: number;  差异内容：rssi: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanResult；  API声明：data: ArrayBuffer;  差异内容：data: ArrayBuffer; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanResult；  API声明：deviceName: string;  差异内容：deviceName: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanResult；  API声明：connectable: boolean;  差异内容：connectable: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface AdvertiseSetting  差异内容： interface AdvertiseSetting | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertiseSetting；  API声明：interval?: number;  差异内容：interval?: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertiseSetting；  API声明：txPower?: number;  差异内容：txPower?: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertiseSetting；  API声明：connectable?: boolean;  差异内容：connectable?: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface AdvertiseData  差异内容： interface AdvertiseData | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertiseData；  API声明：serviceUuids: Array<string>;  差异内容：serviceUuids: Array<string>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertiseData；  API声明：manufactureData: Array<ManufactureData>;  差异内容：manufactureData: Array<ManufactureData>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertiseData；  API声明：serviceData: Array<ServiceData>;  差异内容：serviceData: Array<ServiceData>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertiseData；  API声明：includeDeviceName?: boolean;  差异内容：includeDeviceName?: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface AdvertisingParams  差异内容： interface AdvertisingParams | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertisingParams；  API声明：advertisingSettings: AdvertiseSetting;  差异内容：advertisingSettings: AdvertiseSetting; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertisingParams；  API声明：advertisingData: AdvertiseData;  差异内容：advertisingData: AdvertiseData; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertisingParams；  API声明：advertisingResponse?: AdvertiseData;  差异内容：advertisingResponse?: AdvertiseData; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertisingParams；  API声明：duration?: number;  差异内容：duration?: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface AdvertisingEnableParams  差异内容： interface AdvertisingEnableParams | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertisingEnableParams；  API声明：advertisingId: number;  差异内容：advertisingId: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertisingEnableParams；  API声明：duration?: number;  差异内容：duration?: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface AdvertisingDisableParams  差异内容： interface AdvertisingDisableParams | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertisingDisableParams；  API声明：advertisingId: number;  差异内容：advertisingId: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface AdvertisingStateChangeInfo  差异内容： interface AdvertisingStateChangeInfo | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertisingStateChangeInfo；  API声明：advertisingId: number;  差异内容：advertisingId: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertisingStateChangeInfo；  API声明：state: AdvertisingState;  差异内容：state: AdvertisingState; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface ManufactureData  差异内容： interface ManufactureData | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ManufactureData；  API声明：manufactureId: number;  差异内容：manufactureId: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ManufactureData；  API声明：manufactureValue: ArrayBuffer;  差异内容：manufactureValue: ArrayBuffer; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface ServiceData  差异内容： interface ServiceData | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ServiceData；  API声明：serviceUuid: string;  差异内容：serviceUuid: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ServiceData；  API声明：serviceValue: ArrayBuffer;  差异内容：serviceValue: ArrayBuffer; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface ScanFilter  差异内容： interface ScanFilter | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanFilter；  API声明：deviceId?: string;  差异内容：deviceId?: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanFilter；  API声明：name?: string;  差异内容：name?: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanFilter；  API声明：serviceUuid?: string;  差异内容：serviceUuid?: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanFilter；  API声明：serviceUuidMask?: string;  差异内容：serviceUuidMask?: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanFilter；  API声明：serviceSolicitationUuid?: string;  差异内容：serviceSolicitationUuid?: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanFilter；  API声明：serviceSolicitationUuidMask?: string;  差异内容：serviceSolicitationUuidMask?: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanFilter；  API声明：serviceData?: ArrayBuffer;  差异内容：serviceData?: ArrayBuffer; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanFilter；  API声明：serviceDataMask?: ArrayBuffer;  差异内容：serviceDataMask?: ArrayBuffer; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanFilter；  API声明：manufactureId?: number;  差异内容：manufactureId?: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanFilter；  API声明：manufactureData?: ArrayBuffer;  差异内容：manufactureData?: ArrayBuffer; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanFilter；  API声明：manufactureDataMask?: ArrayBuffer;  差异内容：manufactureDataMask?: ArrayBuffer; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface ScanOptions  差异内容： interface ScanOptions | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanOptions；  API声明：interval?: number;  差异内容：interval?: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanOptions；  API声明：dutyMode?: ScanDuty;  差异内容：dutyMode?: ScanDuty; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanOptions；  API声明：matchMode?: MatchMode;  差异内容：matchMode?: MatchMode; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanOptions；  API声明：phyType?: PhyType;  差异内容：phyType?: PhyType; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： interface GattProperties  差异内容： interface GattProperties | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattProperties；  API声明：write?: boolean;  差异内容：write?: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattProperties；  API声明：writeNoResponse?: boolean;  差异内容：writeNoResponse?: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattProperties；  API声明：read?: boolean;  差异内容：read?: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattProperties；  API声明：notify?: boolean;  差异内容：notify?: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattProperties；  API声明：indicate?: boolean;  差异内容：indicate?: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： enum GattWriteType  差异内容： enum GattWriteType | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattWriteType；  API声明：WRITE = 1  差异内容：WRITE = 1 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattWriteType；  API声明：WRITE\_NO\_RESPONSE = 2  差异内容：WRITE\_NO\_RESPONSE = 2 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： enum ScanDuty  差异内容： enum ScanDuty | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanDuty；  API声明：SCAN\_MODE\_LOW\_POWER = 0  差异内容：SCAN\_MODE\_LOW\_POWER = 0 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanDuty；  API声明：SCAN\_MODE\_BALANCED = 1  差异内容：SCAN\_MODE\_BALANCED = 1 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanDuty；  API声明：SCAN\_MODE\_LOW\_LATENCY = 2  差异内容：SCAN\_MODE\_LOW\_LATENCY = 2 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： enum MatchMode  差异内容： enum MatchMode | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：MatchMode；  API声明：MATCH\_MODE\_AGGRESSIVE = 1  差异内容：MATCH\_MODE\_AGGRESSIVE = 1 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：MatchMode；  API声明：MATCH\_MODE\_STICKY = 2  差异内容：MATCH\_MODE\_STICKY = 2 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： enum AdvertisingState  差异内容： enum AdvertisingState | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertisingState；  API声明：STARTED = 1  差异内容：STARTED = 1 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertisingState；  API声明：ENABLED = 2  差异内容：ENABLED = 2 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertisingState；  API声明：DISABLED = 3  差异内容：DISABLED = 3 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertisingState；  API声明：STOPPED = 4  差异内容：STOPPED = 4 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明： enum PhyType  差异内容： enum PhyType | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：PhyType；  API声明：PHY\_LE\_1M = 1  差异内容：PHY\_LE\_1M = 1 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：PhyType；  API声明：PHY\_LE\_ALL\_SUPPORTED = 255  差异内容：PHY\_LE\_ALL\_SUPPORTED = 255 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace connection  差异内容： declare namespace connection | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：type ProfileConnectionState = constant.ProfileConnectionState;  差异内容：type ProfileConnectionState = constant.ProfileConnectionState; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：type ProfileId = constant.ProfileId;  差异内容：type ProfileId = constant.ProfileId; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：type MajorClass = constant.MajorClass;  差异内容：type MajorClass = constant.MajorClass; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：type MajorMinorClass = constant.MajorMinorClass;  差异内容：type MajorMinorClass = constant.MajorMinorClass; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function getProfileConnectionState(profileId?: ProfileId): ProfileConnectionState;  差异内容：function getProfileConnectionState(profileId?: ProfileId): ProfileConnectionState; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function pairDevice(deviceId: string, callback: AsyncCallback<void>): void;  差异内容：function pairDevice(deviceId: string, callback: AsyncCallback<void>): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function pairDevice(deviceId: string): Promise<void>;  差异内容：function pairDevice(deviceId: string): Promise<void>; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function getRemoteDeviceName(deviceId: string): string;  差异内容：function getRemoteDeviceName(deviceId: string): string; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function getRemoteDeviceClass(deviceId: string): DeviceClass;  差异内容：function getRemoteDeviceClass(deviceId: string): DeviceClass; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function getLocalName(): string;  差异内容：function getLocalName(): string; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function getPairedDevices(): Array<string>;  差异内容：function getPairedDevices(): Array<string>; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function getPairState(deviceId: string): BondState;  差异内容：function getPairState(deviceId: string): BondState; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function setDevicePairingConfirmation(deviceId: string, accept: boolean): void;  差异内容：function setDevicePairingConfirmation(deviceId: string, accept: boolean): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function setDevicePinCode(deviceId: string, code: string, callback: AsyncCallback<void>): void;  差异内容：function setDevicePinCode(deviceId: string, code: string, callback: AsyncCallback<void>): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function setDevicePinCode(deviceId: string, code: string): Promise<void>;  差异内容：function setDevicePinCode(deviceId: string, code: string): Promise<void>; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function setLocalName(name: string): void;  差异内容：function setLocalName(name: string): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function setBluetoothScanMode(mode: ScanMode, duration: number): void;  差异内容：function setBluetoothScanMode(mode: ScanMode, duration: number): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function getBluetoothScanMode(): ScanMode;  差异内容：function getBluetoothScanMode(): ScanMode; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function startBluetoothDiscovery(): void;  差异内容：function startBluetoothDiscovery(): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function stopBluetoothDiscovery(): void;  差异内容：function stopBluetoothDiscovery(): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function isBluetoothDiscovering(): boolean;  差异内容：function isBluetoothDiscovering(): boolean; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function getRemoteDeviceBatteryInfo(deviceId: string): Promise<BatteryInfo>;  差异内容：function getRemoteDeviceBatteryInfo(deviceId: string): Promise<BatteryInfo>; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function setRemoteDeviceName(deviceId: string, name: string): Promise<void>;  差异内容：function setRemoteDeviceName(deviceId: string, name: string): Promise<void>; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function on(type: 'bluetoothDeviceFind', callback: Callback<Array<string>>): void;  差异内容：function on(type: 'bluetoothDeviceFind', callback: Callback<Array<string>>): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void;  差异内容：function off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function on(type: 'bondStateChange', callback: Callback<BondStateParam>): void;  差异内容：function on(type: 'bondStateChange', callback: Callback<BondStateParam>): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function off(type: 'bondStateChange', callback?: Callback<BondStateParam>): void;  差异内容：function off(type: 'bondStateChange', callback?: Callback<BondStateParam>): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function on(type: 'pinRequired', callback: Callback<PinRequiredParam>): void;  差异内容：function on(type: 'pinRequired', callback: Callback<PinRequiredParam>): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function off(type: 'pinRequired', callback?: Callback<PinRequiredParam>): void;  差异内容：function off(type: 'pinRequired', callback?: Callback<PinRequiredParam>): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function on(type: 'batteryChange', callback: Callback<BatteryInfo>): void;  差异内容：function on(type: 'batteryChange', callback: Callback<BatteryInfo>): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function off(type: 'batteryChange', callback?: Callback<BatteryInfo>): void;  差异内容：function off(type: 'batteryChange', callback?: Callback<BatteryInfo>): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明： interface BondStateParam  差异内容： interface BondStateParam | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：BondStateParam；  API声明：deviceId: string;  差异内容：deviceId: string; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：BondStateParam；  API声明：state: BondState;  差异内容：state: BondState; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：BondStateParam；  API声明：cause: UnbondCause;  差异内容：cause: UnbondCause; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明： interface PinRequiredParam  差异内容： interface PinRequiredParam | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：PinRequiredParam；  API声明：deviceId: string;  差异内容：deviceId: string; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：PinRequiredParam；  API声明：pinCode: string;  差异内容：pinCode: string; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明： interface DeviceClass  差异内容： interface DeviceClass | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：majorClass: MajorClass;  差异内容：majorClass: MajorClass; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：majorMinorClass: MajorMinorClass;  差异内容：majorMinorClass: MajorMinorClass; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：DeviceClass；  API声明：classOfDevice: number;  差异内容：classOfDevice: number; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明： enum BluetoothTransport  差异内容： enum BluetoothTransport | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：BluetoothTransport；  API声明：TRANSPORT\_BR\_EDR = 0  差异内容：TRANSPORT\_BR\_EDR = 0 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：BluetoothTransport；  API声明：TRANSPORT\_LE = 1  差异内容：TRANSPORT\_LE = 1 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明： enum ScanMode  差异内容： enum ScanMode | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：ScanMode；  API声明：SCAN\_MODE\_NONE = 0  差异内容：SCAN\_MODE\_NONE = 0 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：ScanMode；  API声明：SCAN\_MODE\_CONNECTABLE = 1  差异内容：SCAN\_MODE\_CONNECTABLE = 1 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：ScanMode；  API声明：SCAN\_MODE\_GENERAL\_DISCOVERABLE = 2  差异内容：SCAN\_MODE\_GENERAL\_DISCOVERABLE = 2 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：ScanMode；  API声明：SCAN\_MODE\_LIMITED\_DISCOVERABLE = 3  差异内容：SCAN\_MODE\_LIMITED\_DISCOVERABLE = 3 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：ScanMode；  API声明：SCAN\_MODE\_CONNECTABLE\_GENERAL\_DISCOVERABLE = 4  差异内容：SCAN\_MODE\_CONNECTABLE\_GENERAL\_DISCOVERABLE = 4 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：ScanMode；  API声明：SCAN\_MODE\_CONNECTABLE\_LIMITED\_DISCOVERABLE = 5  差异内容：SCAN\_MODE\_CONNECTABLE\_LIMITED\_DISCOVERABLE = 5 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明： enum BondState  差异内容： enum BondState | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：BondState；  API声明：BOND\_STATE\_INVALID = 0  差异内容：BOND\_STATE\_INVALID = 0 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：BondState；  API声明：BOND\_STATE\_BONDING = 1  差异内容：BOND\_STATE\_BONDING = 1 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：BondState；  API声明：BOND\_STATE\_BONDED = 2  差异内容：BOND\_STATE\_BONDED = 2 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明： interface BatteryInfo  差异内容： interface BatteryInfo | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：BatteryInfo；  API声明：batteryLevel: number;  差异内容：batteryLevel: number; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：BatteryInfo；  API声明：leftEarBatteryLevel: number;  差异内容：leftEarBatteryLevel: number; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：BatteryInfo；  API声明：leftEarChargeState: DeviceChargeState;  差异内容：leftEarChargeState: DeviceChargeState; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：BatteryInfo；  API声明：rightEarBatteryLevel: number;  差异内容：rightEarBatteryLevel: number; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：BatteryInfo；  API声明：rightEarChargeState: DeviceChargeState;  差异内容：rightEarChargeState: DeviceChargeState; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：BatteryInfo；  API声明：boxBatteryLevel: number;  差异内容：boxBatteryLevel: number; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：BatteryInfo；  API声明：boxChargeState: DeviceChargeState;  差异内容：boxChargeState: DeviceChargeState; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明： enum DeviceChargeState  差异内容： enum DeviceChargeState | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：DeviceChargeState；  API声明：DEVICE\_NORMAL\_CHARGE\_NOT\_CHARGED = 0  差异内容：DEVICE\_NORMAL\_CHARGE\_NOT\_CHARGED = 0 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：DeviceChargeState；  API声明：DEVICE\_NORMAL\_CHARGE\_IN\_CHARGING = 1  差异内容：DEVICE\_NORMAL\_CHARGE\_IN\_CHARGING = 1 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：DeviceChargeState；  API声明：DEVICE\_SUPER\_CHARGE\_NOT\_CHARGED = 2  差异内容：DEVICE\_SUPER\_CHARGE\_NOT\_CHARGED = 2 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：DeviceChargeState；  API声明：DEVICE\_SUPER\_CHARGE\_IN\_CHARGING = 3  差异内容：DEVICE\_SUPER\_CHARGE\_IN\_CHARGING = 3 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明： enum UnbondCause  差异内容： enum UnbondCause | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：UnbondCause；  API声明：USER\_REMOVED = 0  差异内容：USER\_REMOVED = 0 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：UnbondCause；  API声明：REMOTE\_DEVICE\_DOWN = 1  差异内容：REMOTE\_DEVICE\_DOWN = 1 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：UnbondCause；  API声明：AUTH\_FAILURE = 2  差异内容：AUTH\_FAILURE = 2 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：UnbondCause；  API声明：AUTH\_REJECTED = 3  差异内容：AUTH\_REJECTED = 3 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：UnbondCause；  API声明：INTERNAL\_ERROR = 4  差异内容：INTERNAL\_ERROR = 4 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace constant  差异内容： declare namespace constant | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：constant；  API声明： export enum ProfileId  差异内容： export enum ProfileId | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：ProfileId；  API声明：PROFILE\_A2DP\_SOURCE = 1  差异内容：PROFILE\_A2DP\_SOURCE = 1 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：ProfileId；  API声明：PROFILE\_HANDSFREE\_AUDIO\_GATEWAY = 4  差异内容：PROFILE\_HANDSFREE\_AUDIO\_GATEWAY = 4 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：ProfileId；  API声明：PROFILE\_HID\_HOST = 6  差异内容：PROFILE\_HID\_HOST = 6 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：ProfileId；  API声明：PROFILE\_PAN\_NETWORK = 7  差异内容：PROFILE\_PAN\_NETWORK = 7 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：constant；  API声明： export enum ProfileConnectionState  差异内容： export enum ProfileConnectionState | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：ProfileConnectionState；  API声明：STATE\_DISCONNECTED = 0  差异内容：STATE\_DISCONNECTED = 0 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：ProfileConnectionState；  API声明：STATE\_CONNECTING = 1  差异内容：STATE\_CONNECTING = 1 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：ProfileConnectionState；  API声明：STATE\_CONNECTED = 2  差异内容：STATE\_CONNECTED = 2 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：ProfileConnectionState；  API声明：STATE\_DISCONNECTING = 3  差异内容：STATE\_DISCONNECTING = 3 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：constant；  API声明： export enum MajorClass  差异内容： export enum MajorClass | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorClass；  API声明：MAJOR\_MISC = 0x0000  差异内容：MAJOR\_MISC = 0x0000 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorClass；  API声明：MAJOR\_COMPUTER = 0x0100  差异内容：MAJOR\_COMPUTER = 0x0100 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorClass；  API声明：MAJOR\_PHONE = 0x0200  差异内容：MAJOR\_PHONE = 0x0200 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorClass；  API声明：MAJOR\_NETWORKING = 0x0300  差异内容：MAJOR\_NETWORKING = 0x0300 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorClass；  API声明：MAJOR\_AUDIO\_VIDEO = 0x0400  差异内容：MAJOR\_AUDIO\_VIDEO = 0x0400 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorClass；  API声明：MAJOR\_PERIPHERAL = 0x0500  差异内容：MAJOR\_PERIPHERAL = 0x0500 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorClass；  API声明：MAJOR\_IMAGING = 0x0600  差异内容：MAJOR\_IMAGING = 0x0600 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorClass；  API声明：MAJOR\_WEARABLE = 0x0700  差异内容：MAJOR\_WEARABLE = 0x0700 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorClass；  API声明：MAJOR\_TOY = 0x0800  差异内容：MAJOR\_TOY = 0x0800 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorClass；  API声明：MAJOR\_HEALTH = 0x0900  差异内容：MAJOR\_HEALTH = 0x0900 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorClass；  API声明：MAJOR\_UNCATEGORIZED = 0x1F00  差异内容：MAJOR\_UNCATEGORIZED = 0x1F00 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：constant；  API声明： export enum MajorMinorClass  差异内容： export enum MajorMinorClass | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：COMPUTER\_UNCATEGORIZED = 0x0100  差异内容：COMPUTER\_UNCATEGORIZED = 0x0100 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：COMPUTER\_DESKTOP = 0x0104  差异内容：COMPUTER\_DESKTOP = 0x0104 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：COMPUTER\_SERVER = 0x0108  差异内容：COMPUTER\_SERVER = 0x0108 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：COMPUTER\_LAPTOP = 0x010C  差异内容：COMPUTER\_LAPTOP = 0x010C | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：COMPUTER\_HANDHELD\_PC\_PDA = 0x0110  差异内容：COMPUTER\_HANDHELD\_PC\_PDA = 0x0110 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：COMPUTER\_PALM\_SIZE\_PC\_PDA = 0x0114  差异内容：COMPUTER\_PALM\_SIZE\_PC\_PDA = 0x0114 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：COMPUTER\_WEARABLE = 0x0118  差异内容：COMPUTER\_WEARABLE = 0x0118 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：COMPUTER\_TABLET = 0x011C  差异内容：COMPUTER\_TABLET = 0x011C | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：PHONE\_UNCATEGORIZED = 0x0200  差异内容：PHONE\_UNCATEGORIZED = 0x0200 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：PHONE\_CELLULAR = 0x0204  差异内容：PHONE\_CELLULAR = 0x0204 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：PHONE\_CORDLESS = 0x0208  差异内容：PHONE\_CORDLESS = 0x0208 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：PHONE\_SMART = 0x020C  差异内容：PHONE\_SMART = 0x020C | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：PHONE\_MODEM\_OR\_GATEWAY = 0x0210  差异内容：PHONE\_MODEM\_OR\_GATEWAY = 0x0210 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：PHONE\_ISDN = 0x0214  差异内容：PHONE\_ISDN = 0x0214 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：NETWORK\_FULLY\_AVAILABLE = 0x0300  差异内容：NETWORK\_FULLY\_AVAILABLE = 0x0300 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：NETWORK\_1\_TO\_17\_UTILIZED = 0x0320  差异内容：NETWORK\_1\_TO\_17\_UTILIZED = 0x0320 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：NETWORK\_17\_TO\_33\_UTILIZED = 0x0340  差异内容：NETWORK\_17\_TO\_33\_UTILIZED = 0x0340 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：NETWORK\_33\_TO\_50\_UTILIZED = 0x0360  差异内容：NETWORK\_33\_TO\_50\_UTILIZED = 0x0360 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：NETWORK\_60\_TO\_67\_UTILIZED = 0x0380  差异内容：NETWORK\_60\_TO\_67\_UTILIZED = 0x0380 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：NETWORK\_67\_TO\_83\_UTILIZED = 0x03A0  差异内容：NETWORK\_67\_TO\_83\_UTILIZED = 0x03A0 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：NETWORK\_83\_TO\_99\_UTILIZED = 0x03C0  差异内容：NETWORK\_83\_TO\_99\_UTILIZED = 0x03C0 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：NETWORK\_NO\_SERVICE = 0x03E0  差异内容：NETWORK\_NO\_SERVICE = 0x03E0 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_UNCATEGORIZED = 0x0400  差异内容：AUDIO\_VIDEO\_UNCATEGORIZED = 0x0400 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_WEARABLE\_HEADSET = 0x0404  差异内容：AUDIO\_VIDEO\_WEARABLE\_HEADSET = 0x0404 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_HANDSFREE = 0x0408  差异内容：AUDIO\_VIDEO\_HANDSFREE = 0x0408 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_MICROPHONE = 0x0410  差异内容：AUDIO\_VIDEO\_MICROPHONE = 0x0410 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_LOUDSPEAKER = 0x0414  差异内容：AUDIO\_VIDEO\_LOUDSPEAKER = 0x0414 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_HEADPHONES = 0x0418  差异内容：AUDIO\_VIDEO\_HEADPHONES = 0x0418 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_PORTABLE\_AUDIO = 0x041C  差异内容：AUDIO\_VIDEO\_PORTABLE\_AUDIO = 0x041C | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_CAR\_AUDIO = 0x0420  差异内容：AUDIO\_VIDEO\_CAR\_AUDIO = 0x0420 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_SET\_TOP\_BOX = 0x0424  差异内容：AUDIO\_VIDEO\_SET\_TOP\_BOX = 0x0424 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_HIFI\_AUDIO = 0x0428  差异内容：AUDIO\_VIDEO\_HIFI\_AUDIO = 0x0428 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VCR = 0x042C  差异内容：AUDIO\_VIDEO\_VCR = 0x042C | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_CAMERA = 0x0430  差异内容：AUDIO\_VIDEO\_VIDEO\_CAMERA = 0x0430 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_CAMCORDER = 0x0434  差异内容：AUDIO\_VIDEO\_CAMCORDER = 0x0434 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_MONITOR = 0x0438  差异内容：AUDIO\_VIDEO\_VIDEO\_MONITOR = 0x0438 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_DISPLAY\_AND\_LOUDSPEAKER = 0x043C  差异内容：AUDIO\_VIDEO\_VIDEO\_DISPLAY\_AND\_LOUDSPEAKER = 0x043C | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_CONFERENCING = 0x0440  差异内容：AUDIO\_VIDEO\_VIDEO\_CONFERENCING = 0x0440 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：AUDIO\_VIDEO\_VIDEO\_GAMING\_TOY = 0x0448  差异内容：AUDIO\_VIDEO\_VIDEO\_GAMING\_TOY = 0x0448 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_NON\_KEYBOARD\_NON\_POINTING = 0x0500  差异内容：PERIPHERAL\_NON\_KEYBOARD\_NON\_POINTING = 0x0500 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_KEYBOARD = 0x0540  差异内容：PERIPHERAL\_KEYBOARD = 0x0540 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_POINTING\_DEVICE = 0x0580  差异内容：PERIPHERAL\_POINTING\_DEVICE = 0x0580 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_KEYBOARD\_POINTING = 0x05C0  差异内容：PERIPHERAL\_KEYBOARD\_POINTING = 0x05C0 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_UNCATEGORIZED = 0x0500  差异内容：PERIPHERAL\_UNCATEGORIZED = 0x0500 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_JOYSTICK = 0x0504  差异内容：PERIPHERAL\_JOYSTICK = 0x0504 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_GAMEPAD = 0x0508  差异内容：PERIPHERAL\_GAMEPAD = 0x0508 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_REMOTE\_CONTROL = 0x05C0  差异内容：PERIPHERAL\_REMOTE\_CONTROL = 0x05C0 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_SENSING\_DEVICE = 0x0510  差异内容：PERIPHERAL\_SENSING\_DEVICE = 0x0510 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_DIGITIZER\_TABLET = 0x0514  差异内容：PERIPHERAL\_DIGITIZER\_TABLET = 0x0514 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_CARD\_READER = 0x0518  差异内容：PERIPHERAL\_CARD\_READER = 0x0518 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_DIGITAL\_PEN = 0x051C  差异内容：PERIPHERAL\_DIGITAL\_PEN = 0x051C | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_SCANNER\_RFID = 0x0520  差异内容：PERIPHERAL\_SCANNER\_RFID = 0x0520 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：PERIPHERAL\_GESTURAL\_INPUT = 0x0522  差异内容：PERIPHERAL\_GESTURAL\_INPUT = 0x0522 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：IMAGING\_UNCATEGORIZED = 0x0600  差异内容：IMAGING\_UNCATEGORIZED = 0x0600 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：IMAGING\_DISPLAY = 0x0610  差异内容：IMAGING\_DISPLAY = 0x0610 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：IMAGING\_CAMERA = 0x0620  差异内容：IMAGING\_CAMERA = 0x0620 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：IMAGING\_SCANNER = 0x0640  差异内容：IMAGING\_SCANNER = 0x0640 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：IMAGING\_PRINTER = 0x0680  差异内容：IMAGING\_PRINTER = 0x0680 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：WEARABLE\_UNCATEGORIZED = 0x0700  差异内容：WEARABLE\_UNCATEGORIZED = 0x0700 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：WEARABLE\_WRIST\_WATCH = 0x0704  差异内容：WEARABLE\_WRIST\_WATCH = 0x0704 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：WEARABLE\_PAGER = 0x0708  差异内容：WEARABLE\_PAGER = 0x0708 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：WEARABLE\_JACKET = 0x070C  差异内容：WEARABLE\_JACKET = 0x070C | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：WEARABLE\_HELMET = 0x0710  差异内容：WEARABLE\_HELMET = 0x0710 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：WEARABLE\_GLASSES = 0x0714  差异内容：WEARABLE\_GLASSES = 0x0714 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：TOY\_UNCATEGORIZED = 0x0800  差异内容：TOY\_UNCATEGORIZED = 0x0800 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：TOY\_ROBOT = 0x0804  差异内容：TOY\_ROBOT = 0x0804 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：TOY\_VEHICLE = 0x0808  差异内容：TOY\_VEHICLE = 0x0808 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：TOY\_DOLL\_ACTION\_FIGURE = 0x080C  差异内容：TOY\_DOLL\_ACTION\_FIGURE = 0x080C | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：TOY\_CONTROLLER = 0x0810  差异内容：TOY\_CONTROLLER = 0x0810 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：TOY\_GAME = 0x0814  差异内容：TOY\_GAME = 0x0814 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：HEALTH\_UNCATEGORIZED = 0x0900  差异内容：HEALTH\_UNCATEGORIZED = 0x0900 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：HEALTH\_BLOOD\_PRESSURE = 0x0904  差异内容：HEALTH\_BLOOD\_PRESSURE = 0x0904 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：HEALTH\_THERMOMETER = 0x0908  差异内容：HEALTH\_THERMOMETER = 0x0908 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：HEALTH\_WEIGHING = 0x090C  差异内容：HEALTH\_WEIGHING = 0x090C | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：HEALTH\_GLUCOSE = 0x0910  差异内容：HEALTH\_GLUCOSE = 0x0910 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：HEALTH\_PULSE\_OXIMETER = 0x0914  差异内容：HEALTH\_PULSE\_OXIMETER = 0x0914 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：HEALTH\_PULSE\_RATE = 0x0918  差异内容：HEALTH\_PULSE\_RATE = 0x0918 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：HEALTH\_DATA\_DISPLAY = 0x091C  差异内容：HEALTH\_DATA\_DISPLAY = 0x091C | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：HEALTH\_STEP\_COUNTER = 0x0920  差异内容：HEALTH\_STEP\_COUNTER = 0x0920 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：HEALTH\_BODY\_COMPOSITION\_ANALYZER = 0x0924  差异内容：HEALTH\_BODY\_COMPOSITION\_ANALYZER = 0x0924 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：HEALTH\_PEAK\_FLOW\_MONITOR = 0x0928  差异内容：HEALTH\_PEAK\_FLOW\_MONITOR = 0x0928 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：HEALTH\_MEDICATION\_MONITOR = 0x092C  差异内容：HEALTH\_MEDICATION\_MONITOR = 0x092C | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：HEALTH\_KNEE\_PROSTHESIS = 0x0930  差异内容：HEALTH\_KNEE\_PROSTHESIS = 0x0930 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：HEALTH\_ANKLE\_PROSTHESIS = 0x0934  差异内容：HEALTH\_ANKLE\_PROSTHESIS = 0x0934 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：HEALTH\_GENERIC\_HEALTH\_MANAGER = 0x0938  差异内容：HEALTH\_GENERIC\_HEALTH\_MANAGER = 0x0938 | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：MajorMinorClass；  API声明：HEALTH\_PERSONAL\_MOBILITY\_DEVICE = 0x093C  差异内容：HEALTH\_PERSONAL\_MOBILITY\_DEVICE = 0x093C | api/@ohos.bluetooth.constant.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace hfp  差异内容： declare namespace hfp | api/@ohos.bluetooth.hfp.d.ts |
| 新增API | NA | 类名：hfp；  API声明：type BaseProfile = baseProfile.BaseProfile;  差异内容：type BaseProfile = baseProfile.BaseProfile; | api/@ohos.bluetooth.hfp.d.ts |
| 新增API | NA | 类名：hfp；  API声明：function createHfpAgProfile(): HandsFreeAudioGatewayProfile;  差异内容：function createHfpAgProfile(): HandsFreeAudioGatewayProfile; | api/@ohos.bluetooth.hfp.d.ts |
| 新增API | NA | 类名：hfp；  API声明： interface HandsFreeAudioGatewayProfile  差异内容： interface HandsFreeAudioGatewayProfile | api/@ohos.bluetooth.hfp.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace hid  差异内容： declare namespace hid | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：hid；  API声明：type BaseProfile = baseProfile.BaseProfile;  差异内容：type BaseProfile = baseProfile.BaseProfile; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：hid；  API声明：function createHidHostProfile(): HidHostProfile;  差异内容：function createHidHostProfile(): HidHostProfile; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：hid；  API声明： interface HidHostProfile  差异内容： interface HidHostProfile | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace map  差异内容： declare namespace map | api/@ohos.bluetooth.map.d.ts |
| 新增API | NA | 类名：map；  API声明：type BaseProfile = baseProfile.BaseProfile;  差异内容：type BaseProfile = baseProfile.BaseProfile; | api/@ohos.bluetooth.map.d.ts |
| 新增API | NA | 类名：map；  API声明：function createMapMseProfile(): MapMseProfile;  差异内容：function createMapMseProfile(): MapMseProfile; | api/@ohos.bluetooth.map.d.ts |
| 新增API | NA | 类名：map；  API声明： interface MapMseProfile  差异内容： interface MapMseProfile | api/@ohos.bluetooth.map.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace pan  差异内容： declare namespace pan | api/@ohos.bluetooth.pan.d.ts |
| 新增API | NA | 类名：pan；  API声明：type BaseProfile = baseProfile.BaseProfile;  差异内容：type BaseProfile = baseProfile.BaseProfile; | api/@ohos.bluetooth.pan.d.ts |
| 新增API | NA | 类名：pan；  API声明：function createPanProfile(): PanProfile;  差异内容：function createPanProfile(): PanProfile; | api/@ohos.bluetooth.pan.d.ts |
| 新增API | NA | 类名：pan；  API声明： interface PanProfile  差异内容： interface PanProfile | api/@ohos.bluetooth.pan.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace pbap  差异内容： declare namespace pbap | api/@ohos.bluetooth.pbap.d.ts |
| 新增API | NA | 类名：pbap；  API声明：type BaseProfile = baseProfile.BaseProfile;  差异内容：type BaseProfile = baseProfile.BaseProfile; | api/@ohos.bluetooth.pbap.d.ts |
| 新增API | NA | 类名：pbap；  API声明：function createPbapServerProfile(): PbapServerProfile;  差异内容：function createPbapServerProfile(): PbapServerProfile; | api/@ohos.bluetooth.pbap.d.ts |
| 新增API | NA | 类名：pbap；  API声明： interface PbapServerProfile  差异内容： interface PbapServerProfile | api/@ohos.bluetooth.pbap.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace socket  差异内容： declare namespace socket | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：socket；  API声明：function sppListen(name: string, options: SppOptions, callback: AsyncCallback<number>): void;  差异内容：function sppListen(name: string, options: SppOptions, callback: AsyncCallback<number>): void; | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：socket；  API声明：function sppAccept(serverSocket: number, callback: AsyncCallback<number>): void;  差异内容：function sppAccept(serverSocket: number, callback: AsyncCallback<number>): void; | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：socket；  API声明：function sppConnect(deviceId: string, options: SppOptions, callback: AsyncCallback<number>): void;  差异内容：function sppConnect(deviceId: string, options: SppOptions, callback: AsyncCallback<number>): void; | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：socket；  API声明：function sppCloseServerSocket(socket: number): void;  差异内容：function sppCloseServerSocket(socket: number): void; | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：socket；  API声明：function sppCloseClientSocket(socket: number): void;  差异内容：function sppCloseClientSocket(socket: number): void; | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：socket；  API声明：function sppWrite(clientSocket: number, data: ArrayBuffer): void;  差异内容：function sppWrite(clientSocket: number, data: ArrayBuffer): void; | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：socket；  API声明：function on(type: 'sppRead', clientSocket: number, callback: Callback<ArrayBuffer>): void;  差异内容：function on(type: 'sppRead', clientSocket: number, callback: Callback<ArrayBuffer>): void; | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：socket；  API声明：function off(type: 'sppRead', clientSocket: number, callback?: Callback<ArrayBuffer>): void;  差异内容：function off(type: 'sppRead', clientSocket: number, callback?: Callback<ArrayBuffer>): void; | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：socket；  API声明： interface SppOptions  差异内容： interface SppOptions | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：SppOptions；  API声明：uuid: string;  差异内容：uuid: string; | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：SppOptions；  API声明：secure: boolean;  差异内容：secure: boolean; | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：SppOptions；  API声明：type: SppType;  差异内容：type: SppType; | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：socket；  API声明： enum SppType  差异内容： enum SppType | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：SppType；  API声明：SPP\_RFCOMM  差异内容：SPP\_RFCOMM | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace wearDetection  差异内容： declare namespace wearDetection | api/@ohos.bluetooth.wearDetection.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace omapi  差异内容： declare namespace omapi | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：omapi；  API声明：function newSEService(type: 'serviceState', callback: Callback<ServiceState>): SEService;  差异内容：function newSEService(type: 'serviceState', callback: Callback<ServiceState>): SEService; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：omapi；  API声明：function createService(): Promise<SEService>;  差异内容：function createService(): Promise<SEService>; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：omapi；  API声明： export interface SEService  差异内容： export interface SEService | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：SEService；  API声明：getReaders(): Reader[];  差异内容：getReaders(): Reader[]; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：SEService；  API声明：isConnected(): boolean;  差异内容：isConnected(): boolean; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：SEService；  API声明：shutdown(): void;  差异内容：shutdown(): void; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：SEService；  API声明：getVersion(): string;  差异内容：getVersion(): string; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：omapi；  API声明： export interface Reader  差异内容： export interface Reader | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Reader；  API声明：getName(): string;  差异内容：getName(): string; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Reader；  API声明：isSecureElementPresent(): boolean;  差异内容：isSecureElementPresent(): boolean; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Reader；  API声明：openSession(): Session;  差异内容：openSession(): Session; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Reader；  API声明：closeSessions(): void;  差异内容：closeSessions(): void; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：omapi；  API声明： export interface Session  差异内容： export interface Session | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Session；  API声明：getReader(): Reader;  差异内容：getReader(): Reader; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Session；  API声明：getATR(): number[];  差异内容：getATR(): number[]; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Session；  API声明：close(): void;  差异内容：close(): void; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Session；  API声明：isClosed(): boolean;  差异内容：isClosed(): boolean; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Session；  API声明：closeChannels(): void;  差异内容：closeChannels(): void; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Session；  API声明：openBasicChannel(aid: number[]): Promise<Channel>;  差异内容：openBasicChannel(aid: number[]): Promise<Channel>; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Session；  API声明：openBasicChannel(aid: number[], callback: AsyncCallback<Channel>): void;  差异内容：openBasicChannel(aid: number[], callback: AsyncCallback<Channel>): void; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Session；  API声明：openBasicChannel(aid: number[], p2: number): Promise<Channel>;  差异内容：openBasicChannel(aid: number[], p2: number): Promise<Channel>; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Session；  API声明：openBasicChannel(aid: number[], p2: number, callback: AsyncCallback<Channel>): void;  差异内容：openBasicChannel(aid: number[], p2: number, callback: AsyncCallback<Channel>): void; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Session；  API声明：openLogicalChannel(aid: number[]): Promise<Channel>;  差异内容：openLogicalChannel(aid: number[]): Promise<Channel>; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Session；  API声明：openLogicalChannel(aid: number[], callback: AsyncCallback<Channel>): void;  差异内容：openLogicalChannel(aid: number[], callback: AsyncCallback<Channel>): void; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Session；  API声明：openLogicalChannel(aid: number[], p2: number): Promise<Channel>;  差异内容：openLogicalChannel(aid: number[], p2: number): Promise<Channel>; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Session；  API声明：openLogicalChannel(aid: number[], p2: number, callback: AsyncCallback<Channel>): void;  差异内容：openLogicalChannel(aid: number[], p2: number, callback: AsyncCallback<Channel>): void; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：omapi；  API声明： export interface Channel  差异内容： export interface Channel | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Channel；  API声明：getSession(): Session;  差异内容：getSession(): Session; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Channel；  API声明：close(): void;  差异内容：close(): void; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Channel；  API声明：isBasicChannel(): boolean;  差异内容：isBasicChannel(): boolean; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Channel；  API声明：isClosed(): boolean;  差异内容：isClosed(): boolean; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Channel；  API声明：getSelectResponse(): number[];  差异内容：getSelectResponse(): number[]; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Channel；  API声明：transmit(command: number[]): Promise<number[]>;  差异内容：transmit(command: number[]): Promise<number[]>; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：Channel；  API声明：transmit(command: number[], callback: AsyncCallback<number[]>): void;  差异内容：transmit(command: number[], callback: AsyncCallback<number[]>): void; | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：omapi；  API声明： enum ServiceState  差异内容： enum ServiceState | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：ServiceState；  API声明：DISCONNECTED = 0  差异内容：DISCONNECTED = 0 | api/@ohos.secureElement.d.ts |
| 新增API | NA | 类名：ServiceState；  API声明：CONNECTED = 1  差异内容：CONNECTED = 1 | api/@ohos.secureElement.d.ts |
