---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-26011
title: MDM Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > MDM Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:54+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f204900cfd122b3a3600a993ddf83c4f6c670b4bf459b5b70f7a132374b3e809
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：DomainAccountPolicy；  API声明：supportUKeyAuthentication?: boolean;  差异内容：supportUKeyAuthentication?: boolean; | api/@ohos.enterprise.accountManager.d.ts |
| 新增API | NA | 类名：adminManager；  API声明：function getAdminInfos(): Array<AdminInfo>;  差异内容：function getAdminInfos(): Array<AdminInfo>; | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：adminManager；  API声明：function isSelfSuperAdmin(): boolean;  差异内容：function isSelfSuperAdmin(): boolean; | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：adminManager；  API声明：export interface AdminInfo  差异内容：export interface AdminInfo | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：AdminInfo；  API声明：type: AdminType;  差异内容：type: AdminType; | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：AdminInfo；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：AdminInfo；  API声明：abilityName: string;  差异内容：abilityName: string; | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：interface FormInfo  差异内容：interface FormInfo | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：FormInfo；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：FormInfo；  API声明：moduleName: string;  差异内容：moduleName: string; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：FormInfo；  API声明：abilityName: string;  差异内容：abilityName: string; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：FormInfo；  API声明：name: string;  差异内容：name: string; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：FormInfo；  API声明：dimension: formInfo.FormDimension;  差异内容：dimension: formInfo.FormDimension; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：enum StandbyResourceType  差异内容：enum StandbyResourceType | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：StandbyResourceType；  API声明：NETWORK = 1  差异内容：NETWORK = 1 | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function publishFormToDesktop(formInfo: FormInfo): string;  差异内容：function publishFormToDesktop(formInfo: FormInfo): string; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function requestExemptionResource(resourceType: StandbyResourceType, bundleName: string, duration: number): void;  差异内容：function requestExemptionResource(resourceType: StandbyResourceType, bundleName: string, duration: number): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function releaseExemptionResource(resourceType: StandbyResourceType, bundleName: string): void;  差异内容：function releaseExemptionResource(resourceType: StandbyResourceType, bundleName: string): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：common；  API声明：export enum DiskType  差异内容：export enum DiskType | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：DiskType；  API声明：SD\_CARD = 1  差异内容：SD\_CARD = 1 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：DiskType；  API声明：USB\_FLASH = 2  差异内容：USB\_FLASH = 2 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：DiskType；  API声明：CD\_DVD\_BD = 3  差异内容：CD\_DVD\_BD = 3 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：common；  API声明：export interface ExternalStorageDeviceInfo  差异内容：export interface ExternalStorageDeviceInfo | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ExternalStorageDeviceInfo；  API声明：type: DiskType;  差异内容：type: DiskType; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ExternalStorageDeviceInfo；  API声明：devicePath: string;  差异内容：devicePath: string; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ExternalStorageDeviceInfo；  API声明：volumeId: string;  差异内容：volumeId: string; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ExternalStorageDeviceInfo；  API声明：mountStatus: boolean;  差异内容：mountStatus: boolean; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ExternalStorageDeviceInfo；  API声明：vendorId: number;  差异内容：vendorId: number; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ExternalStorageDeviceInfo；  API声明：productId: number;  差异内容：productId: number; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ExternalStorageDeviceInfo；  API声明：serial: string;  差异内容：serial: string; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：common；  API声明：export enum ManagedFeature  差异内容：export enum ManagedFeature | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ManagedFeature；  API声明：LOCAL\_HOTA\_DOMAIN = 0  差异内容：LOCAL\_HOTA\_DOMAIN = 0 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ManagedFeature；  API声明：USER\_EXTEND\_CREDENTIAL = 1  差异内容：USER\_EXTEND\_CREDENTIAL = 1 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ManagedFeature；  API声明：DEVICE\_SECURITY\_LEVEL = 2  差异内容：DEVICE\_SECURITY\_LEVEL = 2 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ManagedFeature；  API声明：PRINTER\_IP\_ADDRESS\_POLICY = 3  差异内容：PRINTER\_IP\_ADDRESS\_POLICY = 3 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ManagedFeature；  API声明：OPTICAL\_DISC\_DRIVE\_BURN = 4  差异内容：OPTICAL\_DISC\_DRIVE\_BURN = 4 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ManagedFeature；  API声明：EXACT\_TIMER = 5  差异内容：EXACT\_TIMER = 5 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ManagedFeature；  API声明：EXEMPTION\_RESOURCE = 6  差异内容：EXEMPTION\_RESOURCE = 6 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ManagedFeature；  API声明：X\_KEY = 7  差异内容：X\_KEY = 7 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ManagedFeature；  API声明：SYSTEM\_ROLLBACK = 8  差异内容：SYSTEM\_ROLLBACK = 8 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ManagedFeature；  API声明：SUPER\_PRIVACY = 9  差异内容：SUPER\_PRIVACY = 9 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：common；  API声明：function isFeatureSupported(feature: ManagedFeature): boolean;  差异内容：function isFeatureSupported(feature: ManagedFeature): boolean; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：common；  API声明：export enum QueryPolicy  差异内容：export enum QueryPolicy | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：QueryPolicy；  API声明：SELF = 0  差异内容：SELF = 0 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：QueryPolicy；  API声明：ALL = 1  差异内容：ALL = 1 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：EnterpriseAdminExtensionAbility；  API声明：onUnmountExternalStorageDevice(deviceInfo: common.ExternalStorageDeviceInfo): void;  差异内容：onUnmountExternalStorageDevice(deviceInfo: common.ExternalStorageDeviceInfo): void; | api/@ohos.enterprise.EnterpriseAdminExtensionAbility.d.ts |
| 新增API | NA | 类名：FeatureForDevice；  API声明：X\_KEY = 1  差异内容：X\_KEY = 1 | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：FeatureForDevice；  API声明：PACKET\_FILTERING = 3  差异内容：PACKET\_FILTERING = 3 | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：FeatureForDevice；  API声明：SUDO = 4  差异内容：SUDO = 4 | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：FeatureForDevice；  API声明：SYSTEM\_ROLLBACK = 51  差异内容：SYSTEM\_ROLLBACK = 51 | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：FeatureForDevice；  API声明：SATA\_ODD\_BURN = 52  差异内容：SATA\_ODD\_BURN = 52 | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：FeatureForDevice；  API声明：SUPER\_PRIVACY = 53  差异内容：SUPER\_PRIVACY = 53 | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：export interface AddCredentialInfo  差异内容：export interface AddCredentialInfo | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：AddCredentialInfo；  API声明：pluginInfo: string;  差异内容：pluginInfo: string; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：AddCredentialInfo；  API声明：authToken?: Uint8Array;  差异内容：authToken?: Uint8Array; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：export interface RemoveCredentialInfo  差异内容：export interface RemoveCredentialInfo | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：RemoveCredentialInfo；  API声明：credentialId: Uint8Array;  差异内容：credentialId: Uint8Array; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：RemoveCredentialInfo；  API声明：authToken?: Uint8Array;  差异内容：authToken?: Uint8Array; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：export interface UserExtCredentialInfo  差异内容：export interface UserExtCredentialInfo | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：UserExtCredentialInfo；  API声明：credentialId: Uint8Array;  差异内容：credentialId: Uint8Array; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：UserExtCredentialInfo；  API声明：pluginInfo: string;  差异内容：pluginInfo: string; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：export enum DeviceSecurityLevelPolicy  差异内容：export enum DeviceSecurityLevelPolicy | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：DeviceSecurityLevelPolicy；  API声明：DEFAULT\_ENFORCED = 0  差异内容：DEFAULT\_ENFORCED = 0 | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：DeviceSecurityLevelPolicy；  API声明：ALLOW\_BALANCED = 1  差异内容：ALLOW\_BALANCED = 1 | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：DeviceSecurityLevelPolicy；  API声明：ALLOW\_FLEXIBLE = 2  差异内容：ALLOW\_FLEXIBLE = 2 | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function setDeviceSecurityLevelPolicy(level: DeviceSecurityLevelPolicy): void;  差异内容：function setDeviceSecurityLevelPolicy(level: DeviceSecurityLevelPolicy): void; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function getDeviceSecurityLevelPolicy(): DeviceSecurityLevelPolicy;  差异内容：function getDeviceSecurityLevelPolicy(): DeviceSecurityLevelPolicy; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function openSession(accountId: number): Promise<Uint8Array>;  差异内容：function openSession(accountId: number): Promise<Uint8Array>; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function closeSession(accountId: number): void;  差异内容：function closeSession(accountId: number): void; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function addUserExtendCredential(info: AddCredentialInfo, accountId: number): Promise<Uint8Array>;  差异内容：function addUserExtendCredential(info: AddCredentialInfo, accountId: number): Promise<Uint8Array>; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function removeUserExtendCredential(info: RemoveCredentialInfo, accountId: number): void;  差异内容：function removeUserExtendCredential(info: RemoveCredentialInfo, accountId: number): void; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function getUserExtendCredential(accountId: number): Promise<UserExtCredentialInfo[]>;  差异内容：function getUserExtendCredential(accountId: number): Promise<UserExtCredentialInfo[]>; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function setUnlockPolicy(policy: UnlockPolicy, accountId: number): void;  差异内容：function setUnlockPolicy(policy: UnlockPolicy, accountId: number): void; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function getUnlockPolicy(accountId: number): UnlockPolicy;  差异内容：function getUnlockPolicy(accountId: number): UnlockPolicy; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：export enum UnlockPolicy  差异内容：export enum UnlockPolicy | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：UnlockPolicy；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：UnlockPolicy；  API声明：EXTENDED\_AUTH\_ONLY = 1  差异内容：EXTENDED\_AUTH\_ONLY = 1 | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：UnlockPolicy；  API声明：EXTENDED\_AUTH\_REQUIRED = 2  差异内容：EXTENDED\_AUTH\_REQUIRED = 2 | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function setWeakPinEnable(isEnable: boolean, fd?: number): void;  差异内容：function setWeakPinEnable(isEnable: boolean, fd?: number): void; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function isWeakPinEnabled(): boolean;  差异内容：function isWeakPinEnabled(): boolean; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：class ExactTimerConfig  差异内容：class ExactTimerConfig | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：ExactTimerConfig；  API声明：name: string;  差异内容：name: string; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：ExactTimerConfig；  API声明：repeat: boolean;  差异内容：repeat: boolean; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：ExactTimerConfig；  API声明：interval: number;  差异内容：interval: number; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：ExactTimerConfig；  API声明：callback(): void;  差异内容：callback(): void; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function createExactTimer(config: ExactTimerConfig): Promise<number>;  差异内容：function createExactTimer(config: ExactTimerConfig): Promise<number>; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function startExactTimer(timer: number, triggerTime: number): Promise<void>;  差异内容：function startExactTimer(timer: number, triggerTime: number): Promise<void>; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function stopExactTimer(timer: number): Promise<void>;  差异内容：function stopExactTimer(timer: number): Promise<void>; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function destroyExactTimer(timer: number): Promise<void>;  差异内容：function destroyExactTimer(timer: number): Promise<void>; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function addAllowedPrinterIPAddressesForDevice(ipAddresses: Array<string>): void;  差异内容：function addAllowedPrinterIPAddressesForDevice(ipAddresses: Array<string>): void; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function removeAllowedPrinterIPAddressesForDevice(ipAddresses: Array<string>): void;  差异内容：function removeAllowedPrinterIPAddressesForDevice(ipAddresses: Array<string>): void; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function getAllowedPrinterIPAddressesForDevice(queryPolicy?: common.QueryPolicy): Array<string>;  差异内容：function getAllowedPrinterIPAddressesForDevice(queryPolicy?: common.QueryPolicy): Array<string>; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function addAllowedPrinterIPAddressesForAccount(ipAddresses: Array<string>): void;  差异内容：function addAllowedPrinterIPAddressesForAccount(ipAddresses: Array<string>): void; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function removeAllowedPrinterIPAddressesForAccount(ipAddresses: Array<string>): void;  差异内容：function removeAllowedPrinterIPAddressesForAccount(ipAddresses: Array<string>): void; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function getAllowedPrinterIPAddressesForAccount(queryPolicy?: common.QueryPolicy): Array<string>;  差异内容：function getAllowedPrinterIPAddressesForAccount(queryPolicy?: common.QueryPolicy): Array<string>; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function setLocalHotaDomain(domain: string): void;  差异内容：function setLocalHotaDomain(domain: string): void; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function getLocalHotaDomain(): string;  差异内容：function getLocalHotaDomain(): string; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：export interface UsbDevice  差异内容：export interface UsbDevice | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：UsbDevice；  API声明：vendorId: number;  差异内容：vendorId: number; | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：UsbDevice；  API声明：productId: number;  差异内容：productId: number; | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：UsbDevice；  API声明：serial?: string;  差异内容：serial?: string; | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：export enum MountPolicy  差异内容：export enum MountPolicy | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：MountPolicy；  API声明：MOUNT\_READ\_WRITE = 0  差异内容：MOUNT\_READ\_WRITE = 0 | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：MountPolicy；  API声明：MOUNT\_READ\_ONLY = 1  差异内容：MOUNT\_READ\_ONLY = 1 | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：MountPolicy；  API声明：UNMOUNT = 2  差异内容：UNMOUNT = 2 | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function getUsbSerialNumber(busNum: number, devAddress: number): string;  差异内容：function getUsbSerialNumber(busNum: number, devAddress: number): string; | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function addAllowedOpticalDiscDriveBurnUsbDevices(usbDevices: Array<UsbDevice>): Promise<void>;  差异内容：function addAllowedOpticalDiscDriveBurnUsbDevices(usbDevices: Array<UsbDevice>): Promise<void>; | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function removeAllowedOpticalDiscDriveBurnUsbDevices(usbDevices: Array<UsbDevice>): Promise<void>;  差异内容：function removeAllowedOpticalDiscDriveBurnUsbDevices(usbDevices: Array<UsbDevice>): Promise<void>; | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function getAllowedOpticalDiscDriveBurnUsbDevices(queryPolicy?: common.QueryPolicy): Promise<Array<UsbDevice>>;  差异内容：function getAllowedOpticalDiscDriveBurnUsbDevices(queryPolicy?: common.QueryPolicy): Promise<Array<UsbDevice>>; | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function setExternalStorageInterceptEnable(enable: boolean): void;  差异内容：function setExternalStorageInterceptEnable(enable: boolean): void; | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function isExternalStorageInterceptEnable(queryPolicy?: common.QueryPolicy): boolean;  差异内容：function isExternalStorageInterceptEnable(queryPolicy?: common.QueryPolicy): boolean; | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function setExternalStorageDeviceMountPolicy(volumeId: string, policy: MountPolicy): void;  差异内容：function setExternalStorageDeviceMountPolicy(volumeId: string, policy: MountPolicy): void; | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function getExternalStorageDeviceInfos(): Array<common.ExternalStorageDeviceInfo>;  差异内容：function getExternalStorageDeviceInfos(): Array<common.ExternalStorageDeviceInfo>; | api/@ohos.enterprise.usbManager.d.ts |
