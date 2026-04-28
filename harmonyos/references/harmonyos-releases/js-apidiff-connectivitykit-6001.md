---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-6001
title: Connectivity Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > Connectivity Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:38+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a5a9ceb98f0c58d43c78bed420ced616bd5ed125b11bc35e31014d8c2bf92788
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：ble；  API声明：function startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void;  差异内容：NA | 类名：ble；  API声明：function startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void;  差异内容：2900010,2902054 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：ble；  API声明：function startAdvertising(advertisingParams: AdvertisingParams, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：ble；  API声明：function startAdvertising(advertisingParams: AdvertisingParams, callback: AsyncCallback<number>): void;  差异内容：2900010,2902054 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：ble；  API声明：function startAdvertising(advertisingParams: AdvertisingParams): Promise<number>;  差异内容：NA | 类名：ble；  API声明：function startAdvertising(advertisingParams: AdvertisingParams): Promise<number>;  差异内容：2900010,2902054 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：ble；  API声明：function stopAdvertising(advertisingId: number, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：ble；  API声明：function stopAdvertising(advertisingId: number, callback: AsyncCallback<void>): void;  差异内容：2902055 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：ble；  API声明：function stopAdvertising(advertisingId: number): Promise<void>;  差异内容：NA | 类名：ble；  API声明：function stopAdvertising(advertisingId: number): Promise<void>;  差异内容：2902055 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：ble；  API声明：function enableAdvertising(advertisingEnableParams: AdvertisingEnableParams, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：ble；  API声明：function enableAdvertising(advertisingEnableParams: AdvertisingEnableParams, callback: AsyncCallback<void>): void;  差异内容：2902055 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：ble；  API声明：function enableAdvertising(advertisingEnableParams: AdvertisingEnableParams): Promise<void>;  差异内容：NA | 类名：ble；  API声明：function enableAdvertising(advertisingEnableParams: AdvertisingEnableParams): Promise<void>;  差异内容：2902055 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：ble；  API声明：function disableAdvertising(advertisingDisableParams: AdvertisingDisableParams, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：ble；  API声明：function disableAdvertising(advertisingDisableParams: AdvertisingDisableParams, callback: AsyncCallback<void>): void;  差异内容：2902055 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：ble；  API声明：function disableAdvertising(advertisingDisableParams: AdvertisingDisableParams): Promise<void>;  差异内容：NA | 类名：ble；  API声明：function disableAdvertising(advertisingDisableParams: AdvertisingDisableParams): Promise<void>;  差异内容：2902055 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：GattClientDevice；  API声明：readCharacteristicValue(characteristic: BLECharacteristic, callback: AsyncCallback<BLECharacteristic>): void;  差异内容：NA | 类名：GattClientDevice；  API声明：readCharacteristicValue(characteristic: BLECharacteristic, callback: AsyncCallback<BLECharacteristic>): void;  差异内容：2900011,2901003,2901004,2901005,2901006,2901007 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：GattClientDevice；  API声明：readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>;  差异内容：NA | 类名：GattClientDevice；  API声明：readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>;  差异内容：2900011,2901003,2901004,2901005,2901006,2901007 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：GattClientDevice；  API声明：readDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<BLEDescriptor>): void;  差异内容：NA | 类名：GattClientDevice；  API声明：readDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<BLEDescriptor>): void;  差异内容：2900011,2901003,2901004,2901005,2901006,2901007 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：GattClientDevice；  API声明：readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>;  差异内容：NA | 类名：GattClientDevice；  API声明：readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>;  差异内容：2900011,2901003,2901004,2901005,2901006,2901007 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：GattClientDevice；  API声明：writeCharacteristicValue(characteristic: BLECharacteristic, writeType: GattWriteType, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：GattClientDevice；  API声明：writeCharacteristicValue(characteristic: BLECharacteristic, writeType: GattWriteType, callback: AsyncCallback<void>): void;  差异内容：2900011,2901003,2901004,2901005,2901006,2901007 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：GattClientDevice；  API声明：writeCharacteristicValue(characteristic: BLECharacteristic, writeType: GattWriteType): Promise<void>;  差异内容：NA | 类名：GattClientDevice；  API声明：writeCharacteristicValue(characteristic: BLECharacteristic, writeType: GattWriteType): Promise<void>;  差异内容：2900011,2901003,2901004,2901005,2901006,2901007 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：GattClientDevice；  API声明：writeDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：GattClientDevice；  API声明：writeDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<void>): void;  差异内容：2900011,2901003,2901004,2901005,2901006,2901007 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：GattClientDevice；  API声明：writeDescriptorValue(descriptor: BLEDescriptor): Promise<void>;  差异内容：NA | 类名：GattClientDevice；  API声明：writeDescriptorValue(descriptor: BLEDescriptor): Promise<void>;  差异内容：2900011,2901003,2901004,2901005,2901006,2901007 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：GattClientDevice；  API声明：getRssiValue(callback: AsyncCallback<number>): void;  差异内容：NA | 类名：GattClientDevice；  API声明：getRssiValue(callback: AsyncCallback<number>): void;  差异内容：2900011,2901003 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：GattClientDevice；  API声明：getRssiValue(): Promise<number>;  差异内容：NA | 类名：GattClientDevice；  API声明：getRssiValue(): Promise<number>;  差异内容：2900011,2901003 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：GattClientDevice；  API声明：setCharacteristicChangeNotification(characteristic: BLECharacteristic, enable: boolean, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：GattClientDevice；  API声明：setCharacteristicChangeNotification(characteristic: BLECharacteristic, enable: boolean, callback: AsyncCallback<void>): void;  差异内容：2900011,2901003 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：GattClientDevice；  API声明：setCharacteristicChangeNotification(characteristic: BLECharacteristic, enable: boolean): Promise<void>;  差异内容：NA | 类名：GattClientDevice；  API声明：setCharacteristicChangeNotification(characteristic: BLECharacteristic, enable: boolean): Promise<void>;  差异内容：2900011,2901003 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：GattClientDevice；  API声明：setCharacteristicChangeIndication(characteristic: BLECharacteristic, enable: boolean, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：GattClientDevice；  API声明：setCharacteristicChangeIndication(characteristic: BLECharacteristic, enable: boolean, callback: AsyncCallback<void>): void;  差异内容：2900011,2901003 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：GattClientDevice；  API声明：setCharacteristicChangeIndication(characteristic: BLECharacteristic, enable: boolean): Promise<void>;  差异内容：NA | 类名：GattClientDevice；  API声明：setCharacteristicChangeIndication(characteristic: BLECharacteristic, enable: boolean): Promise<void>;  差异内容：2900011,2901003 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanReportMode；  API声明：BATCH = 2  差异内容：BATCH = 2 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanReportType；  API声明：ON\_BATCH = 3  差异内容：ON\_BATCH = 3 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：interface GattPermissions  差异内容：interface GattPermissions | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattPermissions；  API声明：read?: boolean;  差异内容：read?: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattPermissions；  API声明：readEncrypted?: boolean;  差异内容：readEncrypted?: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattPermissions；  API声明：readEncryptedMitm?: boolean;  差异内容：readEncryptedMitm?: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattPermissions；  API声明：write?: boolean;  差异内容：write?: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattPermissions；  API声明：writeEncrypted?: boolean;  差异内容：writeEncrypted?: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattPermissions；  API声明：writeEncryptedMitm?: boolean;  差异内容：writeEncryptedMitm?: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattPermissions；  API声明：writeSigned?: boolean;  差异内容：writeSigned?: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattPermissions；  API声明：writeSignedMitm?: boolean;  差异内容：writeSignedMitm?: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：function connectToCandidateConfigWithUserAction(networkId: number): Promise<void>;  差异内容：function connectToCandidateConfigWithUserAction(networkId: number): Promise<void>; | api/@ohos.wifiManager.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：BLECharacteristic；  API声明：permissions?: GattPermissions;  差异内容：permissions?: GattPermissions; | api/@ohos.bluetooth.ble.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：BLEDescriptor；  API声明：permissions?: GattPermissions;  差异内容：permissions?: GattPermissions; | api/@ohos.bluetooth.ble.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：GattProperties；  API声明：broadcast?: boolean;  差异内容：broadcast?: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：GattProperties；  API声明：authenticatedSignedWrite?: boolean;  差异内容：authenticatedSignedWrite?: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：GattProperties；  API声明：extendedProperties?: boolean;  差异内容：extendedProperties?: boolean; | api/@ohos.bluetooth.ble.d.ts |
