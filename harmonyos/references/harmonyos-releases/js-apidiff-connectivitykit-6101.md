---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-6101
title: Connectivity Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Connectivity Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:58d733d63b2afb4b188d5671d4cbda027d873180e1bc01ef4d3268e7af623e7d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：ble；  API声明：function startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | 类名：ble；  API声明：function startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH or (ohos.permission.ACCESS\_BLUETOOTH and ohos.permission.MANAGE\_BLUETOOTH\_ADVERTISER\_NAME) | api/@ohos.bluetooth.ble.d.ts |
| 权限变更 | 类名：ble；  API声明：function startAdvertising(advertisingParams: AdvertisingParams, callback: AsyncCallback<number>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | 类名：ble；  API声明：function startAdvertising(advertisingParams: AdvertisingParams, callback: AsyncCallback<number>): void;  差异内容：ohos.permission.ACCESS\_BLUETOOTH or (ohos.permission.ACCESS\_BLUETOOTH and ohos.permission.MANAGE\_BLUETOOTH\_ADVERTISER\_NAME) | api/@ohos.bluetooth.ble.d.ts |
| 权限变更 | 类名：ble；  API声明：function startAdvertising(advertisingParams: AdvertisingParams): Promise<number>;  差异内容：ohos.permission.ACCESS\_BLUETOOTH | 类名：ble；  API声明：function startAdvertising(advertisingParams: AdvertisingParams): Promise<number>;  差异内容：ohos.permission.ACCESS\_BLUETOOTH or (ohos.permission.ACCESS\_BLUETOOTH and ohos.permission.MANAGE\_BLUETOOTH\_ADVERTISER\_NAME) | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace partnerAgent  差异内容：declare namespace partnerAgent | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：partnerAgent；  API声明：function isPartnerAgentSupported(): boolean;  差异内容：function isPartnerAgentSupported(): boolean; | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：partnerAgent；  API声明：function bindDevice(deviceAddress: PartnerDeviceAddress, deviceCapability: DeviceCapability, businessCapability: BusinessCapability, partnerAgentExtensionAbilityName: string): Promise<void>;  差异内容：function bindDevice(deviceAddress: PartnerDeviceAddress, deviceCapability: DeviceCapability, businessCapability: BusinessCapability, partnerAgentExtensionAbilityName: string): Promise<void>; | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：partnerAgent；  API声明：function unbindDevice(deviceAddress: PartnerDeviceAddress): Promise<void>;  差异内容：function unbindDevice(deviceAddress: PartnerDeviceAddress): Promise<void>; | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：partnerAgent；  API声明：function isDeviceBound(deviceAddress: PartnerDeviceAddress): boolean;  差异内容：function isDeviceBound(deviceAddress: PartnerDeviceAddress): boolean; | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：partnerAgent；  API声明：function getBoundDevices(): PartnerDeviceAddress[];  差异内容：function getBoundDevices(): PartnerDeviceAddress[]; | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：partnerAgent；  API声明：function isDeviceControlEnabled(deviceAddress: PartnerDeviceAddress): boolean;  差异内容：function isDeviceControlEnabled(deviceAddress: PartnerDeviceAddress): boolean; | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：partnerAgent；  API声明：interface DeviceCapability  差异内容：interface DeviceCapability | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：DeviceCapability；  API声明：supportBR?: boolean;  差异内容：supportBR?: boolean; | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：DeviceCapability；  API声明：supportBleAdvertiser?: boolean;  差异内容：supportBleAdvertiser?: boolean; | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：partnerAgent；  API声明：interface BusinessCapability  差异内容：interface BusinessCapability | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：BusinessCapability；  API声明：supportMediaControl?: boolean;  差异内容：supportMediaControl?: boolean; | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：BusinessCapability；  API声明：supportTelephonyControl?: boolean;  差异内容：supportTelephonyControl?: boolean; | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：partnerAgent；  API声明：export interface PartnerDeviceAddress  差异内容：export interface PartnerDeviceAddress | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：PartnerDeviceAddress；  API声明：bluetoothAddress?: common.BluetoothAddress;  差异内容：bluetoothAddress?: common.BluetoothAddress; | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：partnerAgent；  API声明：export enum PartnerAgentExtensionAbilityDestroyReason  差异内容：export enum PartnerAgentExtensionAbilityDestroyReason | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：PartnerAgentExtensionAbilityDestroyReason；  API声明：UNKNOWN\_REASON = 0  差异内容：UNKNOWN\_REASON = 0 | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：PartnerAgentExtensionAbilityDestroyReason；  API声明：USER\_CLOSED\_ABILITY = 1  差异内容：USER\_CLOSED\_ABILITY = 1 | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：PartnerAgentExtensionAbilityDestroyReason；  API声明：DEVICE\_UNPAIRED = 2  差异内容：DEVICE\_UNPAIRED = 2 | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：PartnerAgentExtensionAbilityDestroyReason；  API声明：DEVICE\_LOST = 3  差异内容：DEVICE\_LOST = 3 | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：PartnerAgentExtensionAbilityDestroyReason；  API声明：BLUETOOTH\_DISABLED = 4  差异内容：BLUETOOTH\_DISABLED = 4 | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增API | NA | 类名：global；  API声明：type PartnerDeviceAddress = partnerAgent.PartnerDeviceAddress;  差异内容：type PartnerDeviceAddress = partnerAgent.PartnerDeviceAddress; | api/@ohos.FusionConnectivity.PartnerAgentExtensionAbility.d.ts |
| 新增API | NA | 类名：global；  API声明：type PartnerAgentExtensionAbilityDestroyReason = partnerAgent.PartnerAgentExtensionAbilityDestroyReason;  差异内容：type PartnerAgentExtensionAbilityDestroyReason = partnerAgent.PartnerAgentExtensionAbilityDestroyReason; | api/@ohos.FusionConnectivity.PartnerAgentExtensionAbility.d.ts |
| 新增API | NA | 类名：global；  API声明：export default class PartnerAgentExtensionAbility  差异内容：export default class PartnerAgentExtensionAbility | api/@ohos.FusionConnectivity.PartnerAgentExtensionAbility.d.ts |
| 新增API | NA | 类名：PartnerAgentExtensionAbility；  API声明：context: PartnerAgentExtensionContext;  差异内容：context: PartnerAgentExtensionContext; | api/@ohos.FusionConnectivity.PartnerAgentExtensionAbility.d.ts |
| 新增API | NA | 类名：PartnerAgentExtensionAbility；  API声明：onDestroyWithReason(reason: PartnerAgentExtensionAbilityDestroyReason): void;  差异内容：onDestroyWithReason(reason: PartnerAgentExtensionAbilityDestroyReason): void; | api/@ohos.FusionConnectivity.PartnerAgentExtensionAbility.d.ts |
| 新增API | NA | 类名：PartnerAgentExtensionAbility；  API声明：onDeviceDiscovered(deviceAddress: PartnerDeviceAddress): void;  差异内容：onDeviceDiscovered(deviceAddress: PartnerDeviceAddress): void; | api/@ohos.FusionConnectivity.PartnerAgentExtensionAbility.d.ts |
| 新增API | NA | 类名：global；  API声明：export default class PartnerAgentExtensionContext  差异内容：export default class PartnerAgentExtensionContext | api/@ohos.FusionConnectivity.PartnerAgentExtensionContext.d.ts |
| 新增API | NA | 类名：ble；  API声明：type BluetoothAddress = common.BluetoothAddress;  差异内容：type BluetoothAddress = common.BluetoothAddress; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：readPhy(deviceId: string): Promise<PhyValue>;  差异内容：readPhy(deviceId: string): Promise<PhyValue>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：setPhy(deviceId: string, phyValue: PhyValue): Promise<void>;  差异内容：setPhy(deviceId: string, phyValue: PhyValue): Promise<void>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：onBlePhyUpdate(callback: Callback<PhyValue>): void;  差异内容：onBlePhyUpdate(callback: Callback<PhyValue>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer；  API声明：offBlePhyUpdate(callback?: Callback<PhyValue>): void;  差异内容：offBlePhyUpdate(callback?: Callback<PhyValue>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：readPhy(): Promise<PhyValue>;  差异内容：readPhy(): Promise<PhyValue>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：setPhy(phyValue: PhyValue): Promise<void>;  差异内容：setPhy(phyValue: PhyValue): Promise<void>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：onBlePhyUpdate(callback: Callback<PhyValue>): void;  差异内容：onBlePhyUpdate(callback: Callback<PhyValue>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice；  API声明：offBlePhyUpdate(callback?: Callback<PhyValue>): void;  差异内容：offBlePhyUpdate(callback?: Callback<PhyValue>): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanResult；  API声明：address?: BluetoothAddress;  差异内容：address?: BluetoothAddress; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：AdvertiseData；  API声明：advertiseName?: string;  差异内容：advertiseName?: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanFilter；  API声明：address?: BluetoothAddress;  差异内容：address?: BluetoothAddress; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanFilter；  API声明：rssiThreshold?: number;  差异内容：rssiThreshold?: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：enum BlePhy  差异内容：enum BlePhy | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BlePhy；  API声明：BLE\_PHY\_1M = 1  差异内容：BLE\_PHY\_1M = 1 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BlePhy；  API声明：BLE\_PHY\_2M = 2  差异内容：BLE\_PHY\_2M = 2 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BlePhy；  API声明：BLE\_PHY\_CODED = 3  差异内容：BLE\_PHY\_CODED = 3 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：enum CodedPhyMode  差异内容：enum CodedPhyMode | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：CodedPhyMode；  API声明：BLE\_PHY\_CODED\_S2 = 1  差异内容：BLE\_PHY\_CODED\_S2 = 1 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：CodedPhyMode；  API声明：BLE\_PHY\_CODED\_S8 = 2  差异内容：BLE\_PHY\_CODED\_S8 = 2 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble；  API声明：interface PhyValue  差异内容：interface PhyValue | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：PhyValue；  API声明：txPhy: BlePhy;  差异内容：txPhy: BlePhy; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：PhyValue；  API声明：rxPhy: BlePhy;  差异内容：rxPhy: BlePhy; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：PhyValue；  API声明：phyMode?: CodedPhyMode;  差异内容：phyMode?: CodedPhyMode; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BluetoothAddress；  API声明：rawAddressType?: BluetoothRawAddressType;  差异内容：rawAddressType?: BluetoothRawAddressType; | api/@ohos.bluetooth.common.d.ts |
| 新增API | NA | 类名：common；  API声明：export enum BluetoothRawAddressType  差异内容：export enum BluetoothRawAddressType | api/@ohos.bluetooth.common.d.ts |
| 新增API | NA | 类名：BluetoothRawAddressType；  API声明：PUBLIC = 0  差异内容：PUBLIC = 0 | api/@ohos.bluetooth.common.d.ts |
| 新增API | NA | 类名：BluetoothRawAddressType；  API声明：RANDOM = 1  差异内容：RANDOM = 1 | api/@ohos.bluetooth.common.d.ts |
| 新增API | NA | 类名：connection；  API声明：function onScanModeChange(callback: Callback<ScanMode>): void;  差异内容：function onScanModeChange(callback: Callback<ScanMode>): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function offScanModeChange(callback?: Callback<ScanMode>): void;  差异内容：function offScanModeChange(callback?: Callback<ScanMode>): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：hid；  API声明：type BluetoothAddress = common.BluetoothAddress;  差异内容：type BluetoothAddress = common.BluetoothAddress; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：hid；  API声明：function createHidDeviceProfile(): HidDeviceProfile;  差异内容：function createHidDeviceProfile(): HidDeviceProfile; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：hid；  API声明：interface HidDeviceProfile  差异内容：interface HidDeviceProfile | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceProfile；  API声明：registerHidDevice(sdp: HidDeviceSdp, inQos: HidDeviceQos, outQos: HidDeviceQos, callback: Callback<boolean>): void;  差异内容：registerHidDevice(sdp: HidDeviceSdp, inQos: HidDeviceQos, outQos: HidDeviceQos, callback: Callback<boolean>): void; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceProfile；  API声明：unregisterHidDevice(): void;  差异内容：unregisterHidDevice(): void; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceProfile；  API声明：connect(deviceId: BluetoothAddress): void;  差异内容：connect(deviceId: BluetoothAddress): void; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceProfile；  API声明：disconnect(): void;  差异内容：disconnect(): void; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceProfile；  API声明：sendReport(id: number, reportData: Uint8Array): void;  差异内容：sendReport(id: number, reportData: Uint8Array): void; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceProfile；  API声明：replyReport(type: ReportType, id: number, reportData: Uint8Array): void;  差异内容：replyReport(type: ReportType, id: number, reportData: Uint8Array): void; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceProfile；  API声明：reportError(error: ErrorReason): void;  差异内容：reportError(error: ErrorReason): void; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceProfile；  API声明：onGetReport(callback: Callback<GetReportData>): void;  差异内容：onGetReport(callback: Callback<GetReportData>): void; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceProfile；  API声明：offGetReport(callback?: Callback<GetReportData>): void;  差异内容：offGetReport(callback?: Callback<GetReportData>): void; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceProfile；  API声明：onSetReport(callback: Callback<SetReportData>): void;  差异内容：onSetReport(callback: Callback<SetReportData>): void; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceProfile；  API声明：offSetReport(callback?: Callback<SetReportData>): void;  差异内容：offSetReport(callback?: Callback<SetReportData>): void; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceProfile；  API声明：onInterruptDataReceived(callback: Callback<InterruptData>): void;  差异内容：onInterruptDataReceived(callback: Callback<InterruptData>): void; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceProfile；  API声明：offInterruptDataReceived(callback?: Callback<InterruptData>): void;  差异内容：offInterruptDataReceived(callback?: Callback<InterruptData>): void; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceProfile；  API声明：onSetProtocol(callback: Callback<ProtocolData>): void;  差异内容：onSetProtocol(callback: Callback<ProtocolData>): void; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceProfile；  API声明：offSetProtocol(callback?: Callback<ProtocolData>): void;  差异内容：offSetProtocol(callback?: Callback<ProtocolData>): void; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceProfile；  API声明：onVirtualCableUnplug(callback: Callback<void>): void;  差异内容：onVirtualCableUnplug(callback: Callback<void>): void; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceProfile；  API声明：offVirtualCableUnplug(callback?: Callback<void>): void;  差异内容：offVirtualCableUnplug(callback?: Callback<void>): void; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：hid；  API声明：interface HidDeviceSdp  差异内容：interface HidDeviceSdp | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceSdp；  API声明：name: string;  差异内容：name: string; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceSdp；  API声明：description: string;  差异内容：description: string; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceSdp；  API声明：provider: string;  差异内容：provider: string; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceSdp；  API声明：subclass: Subclass;  差异内容：subclass: Subclass; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceSdp；  API声明：descriptors: Uint8Array;  差异内容：descriptors: Uint8Array; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：hid；  API声明：interface HidDeviceQos  差异内容：interface HidDeviceQos | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceQos；  API声明：serviceType?: ServiceType;  差异内容：serviceType?: ServiceType; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceQos；  API声明：tokenRate?: number;  差异内容：tokenRate?: number; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceQos；  API声明：tokenBucketSize?: number;  差异内容：tokenBucketSize?: number; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceQos；  API声明：peakBandwidth?: number;  差异内容：peakBandwidth?: number; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceQos；  API声明：latency?: number;  差异内容：latency?: number; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：HidDeviceQos；  API声明：delayVariation?: number;  差异内容：delayVariation?: number; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：hid；  API声明：interface GetReportData  差异内容：interface GetReportData | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：GetReportData；  API声明：type: ReportType;  差异内容：type: ReportType; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：GetReportData；  API声明：id: number;  差异内容：id: number; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：GetReportData；  API声明：bufferSize: number;  差异内容：bufferSize: number; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：hid；  API声明：interface SetReportData  差异内容：interface SetReportData | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：SetReportData；  API声明：type: ReportType;  差异内容：type: ReportType; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：SetReportData；  API声明：id: number;  差异内容：id: number; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：SetReportData；  API声明：data: Uint8Array;  差异内容：data: Uint8Array; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：hid；  API声明：interface InterruptData  差异内容：interface InterruptData | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：InterruptData；  API声明：id: number;  差异内容：id: number; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：InterruptData；  API声明：data: Uint8Array;  差异内容：data: Uint8Array; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：hid；  API声明：interface ProtocolData  差异内容：interface ProtocolData | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：ProtocolData；  API声明：protocol: ProtocolType;  差异内容：protocol: ProtocolType; | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：hid；  API声明：enum Subclass  差异内容：enum Subclass | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：Subclass；  API声明：SUBCLASS\_UNCATEGORIZED = 0  差异内容：SUBCLASS\_UNCATEGORIZED = 0 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：Subclass；  API声明：SUBCLASS\_JOYSTICK = 1  差异内容：SUBCLASS\_JOYSTICK = 1 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：Subclass；  API声明：SUBCLASS\_GAMEPAD = 2  差异内容：SUBCLASS\_GAMEPAD = 2 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：Subclass；  API声明：SUBCLASS\_REMOTE\_CONTROL = 3  差异内容：SUBCLASS\_REMOTE\_CONTROL = 3 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：Subclass；  API声明：SUBCLASS\_SENSING\_DEVICE = 4  差异内容：SUBCLASS\_SENSING\_DEVICE = 4 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：Subclass；  API声明：SUBCLASS\_DIGITIZER\_TABLET = 5  差异内容：SUBCLASS\_DIGITIZER\_TABLET = 5 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：Subclass；  API声明：SUBCLASS\_CARD\_READER = 6  差异内容：SUBCLASS\_CARD\_READER = 6 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：Subclass；  API声明：SUBCLASS\_KEYBOARD = 64  差异内容：SUBCLASS\_KEYBOARD = 64 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：Subclass；  API声明：SUBCLASS\_MOUSE = 128  差异内容：SUBCLASS\_MOUSE = 128 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：Subclass；  API声明：SUBCLASS\_COMBO = 192  差异内容：SUBCLASS\_COMBO = 192 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：hid；  API声明：enum ReportType  差异内容：enum ReportType | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：ReportType；  API声明：REPORT\_TYPE\_INPUT = 1  差异内容：REPORT\_TYPE\_INPUT = 1 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：ReportType；  API声明：REPORT\_TYPE\_OUTPUT = 2  差异内容：REPORT\_TYPE\_OUTPUT = 2 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：ReportType；  API声明：REPORT\_TYPE\_FEATURE = 3  差异内容：REPORT\_TYPE\_FEATURE = 3 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：hid；  API声明：enum ServiceType  差异内容：enum ServiceType | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：ServiceType；  API声明：SERVICE\_NO\_TRAFFIC = 0  差异内容：SERVICE\_NO\_TRAFFIC = 0 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：ServiceType；  API声明：SERVICE\_BEST\_EFFORT = 1  差异内容：SERVICE\_BEST\_EFFORT = 1 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：ServiceType；  API声明：SERVICE\_GUARANTEED = 2  差异内容：SERVICE\_GUARANTEED = 2 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：hid；  API声明：enum ErrorReason  差异内容：enum ErrorReason | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：ErrorReason；  API声明：RSP\_SUCCESS = 0  差异内容：RSP\_SUCCESS = 0 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：ErrorReason；  API声明：RSP\_NOT\_READY = 1  差异内容：RSP\_NOT\_READY = 1 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：ErrorReason；  API声明：RSP\_INVALID\_REPORT\_ID = 2  差异内容：RSP\_INVALID\_REPORT\_ID = 2 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：ErrorReason；  API声明：RSP\_UNSUPPORTED\_REQ = 3  差异内容：RSP\_UNSUPPORTED\_REQ = 3 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：ErrorReason；  API声明：RSP\_INVALID\_PARAM = 4  差异内容：RSP\_INVALID\_PARAM = 4 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：ErrorReason；  API声明：RSP\_UNKNOWN = 14  差异内容：RSP\_UNKNOWN = 14 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：hid；  API声明：enum ProtocolType  差异内容：enum ProtocolType | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：ProtocolType；  API声明：PROTOCOL\_BOOT\_MODE = 0  差异内容：PROTOCOL\_BOOT\_MODE = 0 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：ProtocolType；  API声明：PROTOCOL\_REPORT\_MODE = 1  差异内容：PROTOCOL\_REPORT\_MODE = 1 | api/@ohos.bluetooth.hid.d.ts |
| 新增API | NA | 类名：WifiP2PConfig；  API声明：goFreq?: number;  差异内容：goFreq?: number; | api/@ohos.wifiManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.FusionConnectivity.partnerAgent.d.ts  差异内容：ConnectivityKit | api/@ohos.FusionConnectivity.partnerAgent.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.FusionConnectivity.PartnerAgentExtensionAbility.d.ts  差异内容：ConnectivityKit | api/@ohos.FusionConnectivity.PartnerAgentExtensionAbility.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.FusionConnectivity.PartnerAgentExtensionContext.d.ts  差异内容：ConnectivityKit | api/@ohos.FusionConnectivity.PartnerAgentExtensionContext.d.ts |
