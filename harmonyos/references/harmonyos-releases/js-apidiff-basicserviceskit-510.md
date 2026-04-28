---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-510
title: Basic Services Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Basic Services Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:06+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:71fc4a9f713f27b31a741e1c27839bb315b5a909625f0ce90e14f4889116a896
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：FileSpec；  API声明：mimeType?: string;  差异内容：NA | 类名：FileSpec；  API声明：mimeType?: string;  差异内容：18 | api/@ohos.request.d.ts |
| API废弃版本变更 | 类名：usbManager；  API声明：interface USBControlParams  差异内容：NA | 类名：usbManager；  API声明：interface USBControlParams  差异内容：18 | api/@ohos.usbManager.d.ts |
| API废弃版本变更 | 类名：USBControlParams；  API声明：request: number;  差异内容：NA | 类名：USBControlParams；  API声明：request: number;  差异内容：18 | api/@ohos.usbManager.d.ts |
| API废弃版本变更 | 类名：USBControlParams；  API声明：target: USBRequestTargetType;  差异内容：NA | 类名：USBControlParams；  API声明：target: USBRequestTargetType;  差异内容：18 | api/@ohos.usbManager.d.ts |
| API废弃版本变更 | 类名：USBControlParams；  API声明：reqType: USBControlRequestType;  差异内容：NA | 类名：USBControlParams；  API声明：reqType: USBControlRequestType;  差异内容：18 | api/@ohos.usbManager.d.ts |
| API废弃版本变更 | 类名：USBControlParams；  API声明：value: number;  差异内容：NA | 类名：USBControlParams；  API声明：value: number;  差异内容：18 | api/@ohos.usbManager.d.ts |
| API废弃版本变更 | 类名：USBControlParams；  API声明：index: number;  差异内容：NA | 类名：USBControlParams；  API声明：index: number;  差异内容：18 | api/@ohos.usbManager.d.ts |
| API废弃版本变更 | 类名：USBControlParams；  API声明：data: Uint8Array;  差异内容：NA | 类名：USBControlParams；  API声明：data: Uint8Array;  差异内容：18 | api/@ohos.usbManager.d.ts |
| 新增错误码 | 类名：usbManager；  API声明：function getDevices(): Array<Readonly<USBDevice>>;  差异内容：NA | 类名：usbManager；  API声明：function getDevices(): Array<Readonly<USBDevice>>;  差异内容：801 | api/@ohos.usbManager.d.ts |
| 新增错误码 | 类名：usbManager；  API声明：function connectDevice(device: USBDevice): Readonly<USBDevicePipe>;  差异内容：NA | 类名：usbManager；  API声明：function connectDevice(device: USBDevice): Readonly<USBDevicePipe>;  差异内容：801 | api/@ohos.usbManager.d.ts |
| 新增错误码 | 类名：usbManager；  API声明：function hasRight(deviceName: string): boolean;  差异内容：NA | 类名：usbManager；  API声明：function hasRight(deviceName: string): boolean;  差异内容：801 | api/@ohos.usbManager.d.ts |
| 新增错误码 | 类名：usbManager；  API声明：function requestRight(deviceName: string): Promise<boolean>;  差异内容：NA | 类名：usbManager；  API声明：function requestRight(deviceName: string): Promise<boolean>;  差异内容：801 | api/@ohos.usbManager.d.ts |
| 新增错误码 | 类名：usbManager；  API声明：function removeRight(deviceName: string): boolean;  差异内容：NA | 类名：usbManager；  API声明：function removeRight(deviceName: string): boolean;  差异内容：801 | api/@ohos.usbManager.d.ts |
| 新增错误码 | 类名：usbManager；  API声明：function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): number;  差异内容：NA | 类名：usbManager；  API声明：function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): number;  差异内容：801 | api/@ohos.usbManager.d.ts |
| 新增错误码 | 类名：usbManager；  API声明：function releaseInterface(pipe: USBDevicePipe, iface: USBInterface): number;  差异内容：NA | 类名：usbManager；  API声明：function releaseInterface(pipe: USBDevicePipe, iface: USBInterface): number;  差异内容：801 | api/@ohos.usbManager.d.ts |
| 新增错误码 | 类名：usbManager；  API声明：function setConfiguration(pipe: USBDevicePipe, config: USBConfiguration): number;  差异内容：NA | 类名：usbManager；  API声明：function setConfiguration(pipe: USBDevicePipe, config: USBConfiguration): number;  差异内容：801 | api/@ohos.usbManager.d.ts |
| 新增错误码 | 类名：usbManager；  API声明：function setInterface(pipe: USBDevicePipe, iface: USBInterface): number;  差异内容：NA | 类名：usbManager；  API声明：function setInterface(pipe: USBDevicePipe, iface: USBInterface): number;  差异内容：801 | api/@ohos.usbManager.d.ts |
| 新增错误码 | 类名：usbManager；  API声明：function getRawDescriptor(pipe: USBDevicePipe): Uint8Array;  差异内容：NA | 类名：usbManager；  API声明：function getRawDescriptor(pipe: USBDevicePipe): Uint8Array;  差异内容：801 | api/@ohos.usbManager.d.ts |
| 新增错误码 | 类名：usbManager；  API声明：function getFileDescriptor(pipe: USBDevicePipe): number;  差异内容：NA | 类名：usbManager；  API声明：function getFileDescriptor(pipe: USBDevicePipe): number;  差异内容：801 | api/@ohos.usbManager.d.ts |
| 新增错误码 | 类名：usbManager；  API声明：function usbControlTransfer(pipe: USBDevicePipe, requestparam: USBDeviceRequestParams, timeout?: number): Promise<number>;  差异内容：NA | 类名：usbManager；  API声明：function usbControlTransfer(pipe: USBDevicePipe, requestparam: USBDeviceRequestParams, timeout?: number): Promise<number>;  差异内容：801 | api/@ohos.usbManager.d.ts |
| 新增错误码 | 类名：usbManager；  API声明：function bulkTransfer(pipe: USBDevicePipe, endpoint: USBEndpoint, buffer: Uint8Array, timeout?: number): Promise<number>;  差异内容：NA | 类名：usbManager；  API声明：function bulkTransfer(pipe: USBDevicePipe, endpoint: USBEndpoint, buffer: Uint8Array, timeout?: number): Promise<number>;  差异内容：801 | api/@ohos.usbManager.d.ts |
| 新增错误码 | 类名：usbManager；  API声明：function closePipe(pipe: USBDevicePipe): number;  差异内容：NA | 类名：usbManager；  API声明：function closePipe(pipe: USBDevicePipe): number;  差异内容：801 | api/@ohos.usbManager.d.ts |
| 新增错误码 | 类名：usbManager；  API声明：function hasAccessoryRight(accessory: USBAccessory): boolean;  差异内容：NA | 类名：usbManager；  API声明：function hasAccessoryRight(accessory: USBAccessory): boolean;  差异内容：801 | api/@ohos.usbManager.d.ts |
| 新增错误码 | 类名：usbManager；  API声明：function requestAccessoryRight(accessory: USBAccessory): Promise<boolean>;  差异内容：NA | 类名：usbManager；  API声明：function requestAccessoryRight(accessory: USBAccessory): Promise<boolean>;  差异内容：801 | api/@ohos.usbManager.d.ts |
| 新增错误码 | 类名：usbManager；  API声明：function cancelAccessoryRight(accessory: USBAccessory): void;  差异内容：NA | 类名：usbManager；  API声明：function cancelAccessoryRight(accessory: USBAccessory): void;  差异内容：801 | api/@ohos.usbManager.d.ts |
| 新增错误码 | 类名：usbManager；  API声明：function getAccessoryList(): Array<Readonly<USBAccessory>>;  差异内容：NA | 类名：usbManager；  API声明：function getAccessoryList(): Array<Readonly<USBAccessory>>;  差异内容：801 | api/@ohos.usbManager.d.ts |
| 新增错误码 | 类名：usbManager；  API声明：function openAccessory(accessory: USBAccessory): USBAccessoryHandle;  差异内容：NA | 类名：usbManager；  API声明：function openAccessory(accessory: USBAccessory): USBAccessoryHandle;  差异内容：801 | api/@ohos.usbManager.d.ts |
| 新增错误码 | 类名：usbManager；  API声明：function closeAccessory(accessoryHandle: USBAccessoryHandle): void;  差异内容：NA | 类名：usbManager；  API声明：function closeAccessory(accessoryHandle: USBAccessoryHandle): void;  差异内容：801 | api/@ohos.usbManager.d.ts |
| 删除错误码 | 类名：commonEventManager；  API声明：function publish(event: string, callback: AsyncCallback<void>): void;  差异内容：1500004 | 类名：commonEventManager；  API声明：function publish(event: string, callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.commonEventManager.d.ts |
| 删除错误码 | 类名：commonEventManager；  API声明：function publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void;  差异内容：1500004 | 类名：commonEventManager；  API声明：function publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.commonEventManager.d.ts |
| 错误码变更 | 类名：SystemPasteboard；  API声明：getData(callback: AsyncCallback<PasteData>): void;  差异内容：12900003,201,401 | 类名：SystemPasteboard；  API声明：getData(callback: AsyncCallback<PasteData>): void;  差异内容：201,27787277,401 | api/@ohos.pasteboard.d.ts |
| 错误码变更 | 类名：SystemPasteboard；  API声明：getData(): Promise<PasteData>;  差异内容：12900003,201 | 类名：SystemPasteboard；  API声明：getData(): Promise<PasteData>;  差异内容：201,27787277 | api/@ohos.pasteboard.d.ts |
| 错误码变更 | 类名：SystemPasteboard；  API声明：setData(data: PasteData, callback: AsyncCallback<void>): void;  差异内容：12900003,12900004,401 | 类名：SystemPasteboard；  API声明：setData(data: PasteData, callback: AsyncCallback<void>): void;  差异内容：27787277,27787278,401 | api/@ohos.pasteboard.d.ts |
| 错误码变更 | 类名：SystemPasteboard；  API声明：setData(data: PasteData): Promise<void>;  差异内容：12900003,12900004,401 | 类名：SystemPasteboard；  API声明：setData(data: PasteData): Promise<void>;  差异内容：27787277,27787278,401 | api/@ohos.pasteboard.d.ts |
| 错误码变更 | 类名：SystemPasteboard；  API声明：getUnifiedData(): Promise<unifiedDataChannel.UnifiedData>;  差异内容：12900003,201 | 类名：SystemPasteboard；  API声明：getUnifiedData(): Promise<unifiedDataChannel.UnifiedData>;  差异内容：201,27787277 | api/@ohos.pasteboard.d.ts |
| 错误码变更 | 类名：SystemPasteboard；  API声明：setUnifiedData(data: unifiedDataChannel.UnifiedData): Promise<void>;  差异内容：12900003,12900004,401 | 类名：SystemPasteboard；  API声明：setUnifiedData(data: unifiedDataChannel.UnifiedData): Promise<void>;  差异内容：27787277,27787278,401 | api/@ohos.pasteboard.d.ts |
| 权限变更 | 类名：settings；  API声明：function setValueSync(context: Context, name: string, value: string): boolean;  差异内容：ohos.permission.MANAGE\_SECURE\_SETTINGS | 类名：settings；  API声明：function setValueSync(context: Context, name: string, value: string): boolean;  差异内容：ohos.permission.MANAGE\_SETTINGS | api/@ohos.settings.d.ts |
| 权限变更 | 类名：settings；  API声明：function setValueSync(context: Context, name: string, value: string, domainName: string): boolean;  差异内容：ohos.permission.MANAGE\_SECURE\_SETTINGS | 类名：settings；  API声明：function setValueSync(context: Context, name: string, value: string, domainName: string): boolean;  差异内容：DEVICE\_SHARED, USER\_PROPRERTY ohos.permission.MANAGE\_SETTINGS. or [USER\_SECURE] ohos.permission.MANAGE\_SECURE\_SETTINGS. | api/@ohos.settings.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace cacheDownload  差异内容：declare namespace cacheDownload | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload；  API声明：interface CacheDownloadOptions  差异内容：interface CacheDownloadOptions | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：CacheDownloadOptions；  API声明：headers?: Record<string, string>;  差异内容：headers?: Record<string, string>; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload；  API声明：function download(url: string, options: CacheDownloadOptions);  差异内容：function download(url: string, options: CacheDownloadOptions); | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload；  API声明：function cancel(url: string);  差异内容：function cancel(url: string); | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload；  API声明：function setMemoryCacheSize(bytes: number);  差异内容：function setMemoryCacheSize(bytes: number); | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload；  API声明：function setFileCacheSize(bytes: number);  差异内容：function setFileCacheSize(bytes: number); | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：settings；  API声明：function openNetworkManagerSettings(context: Context): Promise<boolean>;  差异内容：function openNetworkManagerSettings(context: Context): Promise<boolean>; | api/@ohos.settings.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：export enum UsbTransferFlags  差异内容：export enum UsbTransferFlags | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbTransferFlags；  API声明：USB\_TRANSFER\_SHORT\_NOT\_OK = 0  差异内容：USB\_TRANSFER\_SHORT\_NOT\_OK = 0 | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbTransferFlags；  API声明：USB\_TRANSFER\_FREE\_BUFFER = 1  差异内容：USB\_TRANSFER\_FREE\_BUFFER = 1 | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbTransferFlags；  API声明：USB\_TRANSFER\_FREE\_TRANSFER = 2  差异内容：USB\_TRANSFER\_FREE\_TRANSFER = 2 | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbTransferFlags；  API声明：USB\_TRANSFER\_ADD\_ZERO\_PACKET = 3  差异内容：USB\_TRANSFER\_ADD\_ZERO\_PACKET = 3 | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：export enum UsbTransferStatus  差异内容：export enum UsbTransferStatus | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbTransferStatus；  API声明：TRANSFER\_COMPLETED = 0  差异内容：TRANSFER\_COMPLETED = 0 | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbTransferStatus；  API声明：TRANSFER\_ERROR = 1  差异内容：TRANSFER\_ERROR = 1 | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbTransferStatus；  API声明：TRANSFER\_TIMED\_OUT = 2  差异内容：TRANSFER\_TIMED\_OUT = 2 | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbTransferStatus；  API声明：TRANSFER\_CANCELED = 3  差异内容：TRANSFER\_CANCELED = 3 | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbTransferStatus；  API声明：TRANSFER\_STALL = 4  差异内容：TRANSFER\_STALL = 4 | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbTransferStatus；  API声明：TRANSFER\_NO\_DEVICE = 5  差异内容：TRANSFER\_NO\_DEVICE = 5 | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbTransferStatus；  API声明：TRANSFER\_OVERFLOW = 6  差异内容：TRANSFER\_OVERFLOW = 6 | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：export enum UsbEndpointTransferType  差异内容：export enum UsbEndpointTransferType | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbEndpointTransferType；  API声明：TRANSFER\_TYPE\_ISOCHRONOUS = 0x1  差异内容：TRANSFER\_TYPE\_ISOCHRONOUS = 0x1 | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbEndpointTransferType；  API声明：TRANSFER\_TYPE\_BULK = 0x2  差异内容：TRANSFER\_TYPE\_BULK = 0x2 | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbEndpointTransferType；  API声明：TRANSFER\_TYPE\_INTERRUPT = 0x3  差异内容：TRANSFER\_TYPE\_INTERRUPT = 0x3 | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：interface UsbIsoPacketDescriptor  差异内容：interface UsbIsoPacketDescriptor | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbIsoPacketDescriptor；  API声明：length: number;  差异内容：length: number; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbIsoPacketDescriptor；  API声明：actualLength: number;  差异内容：actualLength: number; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbIsoPacketDescriptor；  API声明：status: UsbTransferStatus;  差异内容：status: UsbTransferStatus; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：interface SubmitTransferCallback  差异内容：interface SubmitTransferCallback | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：SubmitTransferCallback；  API声明：actualLength: number;  差异内容：actualLength: number; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：SubmitTransferCallback；  API声明：status: UsbTransferStatus;  差异内容：status: UsbTransferStatus; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：SubmitTransferCallback；  API声明：isoPacketDescs: Array<Readonly<UsbIsoPacketDescriptor>>;  差异内容：isoPacketDescs: Array<Readonly<UsbIsoPacketDescriptor>>; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：interface UsbDataTransferParams  差异内容：interface UsbDataTransferParams | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbDataTransferParams；  API声明：devPipe: USBDevicePipe;  差异内容：devPipe: USBDevicePipe; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbDataTransferParams；  API声明：flags: UsbTransferFlags;  差异内容：flags: UsbTransferFlags; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbDataTransferParams；  API声明：endpoint: number;  差异内容：endpoint: number; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbDataTransferParams；  API声明：type: UsbEndpointTransferType;  差异内容：type: UsbEndpointTransferType; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbDataTransferParams；  API声明：timeout: number;  差异内容：timeout: number; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbDataTransferParams；  API声明：length: number;  差异内容：length: number; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbDataTransferParams；  API声明：callback: AsyncCallback<SubmitTransferCallback>;  差异内容：callback: AsyncCallback<SubmitTransferCallback>; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbDataTransferParams；  API声明：userData: Uint8Array;  差异内容：userData: Uint8Array; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbDataTransferParams；  API声明：buffer: Uint8Array;  差异内容：buffer: Uint8Array; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：UsbDataTransferParams；  API声明：isoPacketCount: number;  差异内容：isoPacketCount: number; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function usbSubmitTransfer(transfer: UsbDataTransferParams): void;  差异内容：function usbSubmitTransfer(transfer: UsbDataTransferParams): void; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function usbCancelTransfer(transfer: UsbDataTransferParams): void;  差异内容：function usbCancelTransfer(transfer: UsbDataTransferParams): void; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：osAccount；  API声明：class DomainAccountManager  差异内容：class DomainAccountManager | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：DomainAccountManager；  API声明：static updateAccountInfo(oldAccountInfo: DomainAccountInfo, newAccountInfo: DomainAccountInfo): Promise<void>;  差异内容：static updateAccountInfo(oldAccountInfo: DomainAccountInfo, newAccountInfo: DomainAccountInfo): Promise<void>; | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：osAccount；  API声明：interface DomainServerConfig  差异内容：interface DomainServerConfig | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：DomainServerConfig；  API声明：parameters: Record<string, Object>;  差异内容：parameters: Record<string, Object>; | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：DomainServerConfig；  API声明：id: string;  差异内容：id: string; | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：DomainServerConfig；  API声明：domain: string;  差异内容：domain: string; | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：osAccount；  API声明：class DomainServerConfigManager  差异内容：class DomainServerConfigManager | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：DomainServerConfigManager；  API声明：static addServerConfig(parameters: Record<string, Object>): Promise<DomainServerConfig>;  差异内容：static addServerConfig(parameters: Record<string, Object>): Promise<DomainServerConfig>; | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：DomainServerConfigManager；  API声明：static removeServerConfig(configId: string): Promise<void>;  差异内容：static removeServerConfig(configId: string): Promise<void>; | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：DomainServerConfigManager；  API声明：static updateServerConfig(configId: string, parameters: Record<string, Object>): Promise<DomainServerConfig>;  差异内容：static updateServerConfig(configId: string, parameters: Record<string, Object>): Promise<DomainServerConfig>; | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：DomainServerConfigManager；  API声明：static getServerConfig(configId: string): Promise<DomainServerConfig>;  差异内容：static getServerConfig(configId: string): Promise<DomainServerConfig>; | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：DomainServerConfigManager；  API声明：static getAllServerConfigs(): Promise<Array<DomainServerConfig>>;  差异内容：static getAllServerConfigs(): Promise<Array<DomainServerConfig>>; | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：DomainServerConfigManager；  API声明：static getAccountServerConfig(domainAccountInfo: DomainAccountInfo): Promise<DomainServerConfig>;  差异内容：static getAccountServerConfig(domainAccountInfo: DomainAccountInfo): Promise<DomainServerConfig>; | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：zlib；  API声明：export enum ParallelStrategy  差异内容：export enum ParallelStrategy | api/@ohos.zlib.d.ts |
| 新增API | NA | 类名：ParallelStrategy；  API声明：PARALLEL\_STRATEGY\_SEQUENTIAL = 0  差异内容：PARALLEL\_STRATEGY\_SEQUENTIAL = 0 | api/@ohos.zlib.d.ts |
| 新增API | NA | 类名：ParallelStrategy；  API声明：PARALLEL\_STRATEGY\_PARALLEL\_DECOMPRESSION = 1  差异内容：PARALLEL\_STRATEGY\_PARALLEL\_DECOMPRESSION = 1 | api/@ohos.zlib.d.ts |
| 起始版本有变化 | 类名：SystemPasteboard；  API声明：setAppShareOptions(shareOptions: ShareOption): void;  差异内容：12 | 类名：SystemPasteboard；  API声明：setAppShareOptions(shareOptions: ShareOption): void;  差异内容：14 | api/@ohos.pasteboard.d.ts |
| 起始版本有变化 | 类名：SystemPasteboard；  API声明：removeAppShareOptions(): void;  差异内容：12 | 类名：SystemPasteboard；  API声明：removeAppShareOptions(): void;  差异内容：14 | api/@ohos.pasteboard.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.request.cacheDownload.d.ts  差异内容：BasicServicesKit | api/@ohos.request.cacheDownload.d.ts |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：declare namespace settings  差异内容：NA | 类名：global；  API声明：declare namespace settings  差异内容：atomicservice | api/@ohos.settings.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：SystemPasteboard；  API声明：getChangeCount(): number;  差异内容：getChangeCount(): number; | api/@ohos.pasteboard.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Task；  API声明：setMaxSpeed(speed: number): Promise<void>;  差异内容：setMaxSpeed(speed: number): Promise<void>; | api/@ohos.request.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：FileSpec；  API声明：contentType?: string;  差异内容：contentType?: string; | api/@ohos.request.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：DomainAccountInfo；  API声明：serverConfigId?: string;  差异内容：serverConfigId?: string; | api/@ohos.account.osAccount.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Options；  API声明：parallel?: ParallelStrategy;  差异内容：parallel?: ParallelStrategy; | api/@ohos.zlib.d.ts |
