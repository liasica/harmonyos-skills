---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-7001
title: MDM Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > MDM Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:06+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:ad25a237cea11fb50c27ba649da7ec21824bc63e0ba337c4dc2185baea73b62a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：usbManager；  API声明：function setUsbStorageDeviceAccessPolicy(admin: Want, usbPolicy: UsbPolicy): void;  差异内容：ohos.permission.ENTERPRISE\_MANAGE\_USB | 类名：usbManager；  API声明：function setUsbStorageDeviceAccessPolicy(admin: Want, usbPolicy: UsbPolicy): void;  差异内容：ohos.permission.ENTERPRISE\_MANAGE\_USB or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS | api/@ohos.enterprise.usbManager.d.ts |
| 权限变更 | 类名：usbManager；  API声明：function getUsbStorageDeviceAccessPolicy(admin: Want): UsbPolicy;  差异内容：ohos.permission.ENTERPRISE\_MANAGE\_USB | 类名：usbManager；  API声明：function getUsbStorageDeviceAccessPolicy(admin: Want): UsbPolicy;  差异内容：ohos.permission.ENTERPRISE\_MANAGE\_USB or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：bluetoothManager；  API声明：function addDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array<Protocol>, policy: TransferPolicy): void;  差异内容：function addDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array<Protocol>, policy: TransferPolicy): void; | api/@ohos.enterprise.bluetoothManager.d.ts |
| 新增API | NA | 类名：bluetoothManager；  API声明：function removeDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array<Protocol>, policy: TransferPolicy): void;  差异内容：function removeDisallowedBluetoothProtocols(admin: Want, accountId: number, protocols: Array<Protocol>, policy: TransferPolicy): void; | api/@ohos.enterprise.bluetoothManager.d.ts |
| 新增API | NA | 类名：bluetoothManager；  API声明：function getDisallowedBluetoothProtocols(admin: Want | null, accountId: number, policy: TransferPolicy): Array<Protocol>;  差异内容：function getDisallowedBluetoothProtocols(admin: Want | null, accountId: number, policy: TransferPolicy): Array<Protocol>; | api/@ohos.enterprise.bluetoothManager.d.ts |
| 新增API | NA | 类名：bluetoothManager；  API声明：export enum TransferPolicy  差异内容：export enum TransferPolicy | api/@ohos.enterprise.bluetoothManager.d.ts |
| 新增API | NA | 类名：TransferPolicy；  API声明：SEND\_ONLY = 0  差异内容：SEND\_ONLY = 0 | api/@ohos.enterprise.bluetoothManager.d.ts |
| 新增API | NA | 类名：TransferPolicy；  API声明：RECEIVE\_ONLY = 1  差异内容：RECEIVE\_ONLY = 1 | api/@ohos.enterprise.bluetoothManager.d.ts |
| 新增API | NA | 类名：TransferPolicy；  API声明：RECEIVE\_SEND = 2  差异内容：RECEIVE\_SEND = 2 | api/@ohos.enterprise.bluetoothManager.d.ts |
| 新增API | NA | 类名：restrictions；  API声明：function setDisallowedPolicyForAccount(admin: Want, feature: FeatureForAccount, disallow: boolean, accountId: number): void;  差异内容：function setDisallowedPolicyForAccount(admin: Want, feature: FeatureForAccount, disallow: boolean, accountId: number): void; | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：restrictions；  API声明：function getDisallowedPolicyForAccount(admin: Want | null, feature: FeatureForAccount, accountId: number): boolean;  差异内容：function getDisallowedPolicyForAccount(admin: Want | null, feature: FeatureForAccount, accountId: number): boolean; | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：FeatureForDevice；  API声明：LOCAL\_INPUT = 2  差异内容：LOCAL\_INPUT = 2 | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：FeatureForDevice；  API声明：CORE\_DUMP = 6  差异内容：CORE\_DUMP = 6 | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：FeatureForDevice；  API声明：DISK\_ERASURE = 8  差异内容：DISK\_ERASURE = 8 | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：restrictions；  API声明：enum FeatureForAccount  差异内容：enum FeatureForAccount | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：FeatureForAccount；  API声明：MULTI\_WINDOW = 0  差异内容：MULTI\_WINDOW = 0 | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：FeatureForAccount；  API声明：SUPER\_HUB = 2  差异内容：SUPER\_HUB = 2 | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：ManagedEvent；  API声明：MANAGED\_EVENT\_BUNDLE\_UPDATED = 10  差异内容：MANAGED\_EVENT\_BUNDLE\_UPDATED = 10 | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：ManagedEvent；  API声明：MANAGED\_EVENT\_POLICIES\_CHANGED = 11  差异内容：MANAGED\_EVENT\_POLICIES\_CHANGED = 11 | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：interface BundleStatsInfo  差异内容：interface BundleStatsInfo | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：BundleStatsInfo；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：BundleStatsInfo；  API声明：appIndex: number;  差异内容：appIndex: number; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：BundleStatsInfo；  API声明：abilityInFgTotalTime: number;  差异内容：abilityInFgTotalTime: number; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function addAllowedNotificationBundles(admin: Want, bundleNames: Array<string>, accountId: number): void;  差异内容：function addAllowedNotificationBundles(admin: Want, bundleNames: Array<string>, accountId: number): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function removeAllowedNotificationBundles(admin: Want, bundleNames: Array<string>, accountId: number): void;  差异内容：function removeAllowedNotificationBundles(admin: Want, bundleNames: Array<string>, accountId: number): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function getAllowedNotificationBundles(admin: Want | null, accountId: number): Array<string>;  差异内容：function getAllowedNotificationBundles(admin: Want | null, accountId: number): Array<string>; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function queryTrafficStats(admin: Want, bundleName: string, appIndex: number, accountId: number, networkInfo: statistics.NetworkInfo): Promise<statistics.NetStatsInfo>;  差异内容：function queryTrafficStats(admin: Want, bundleName: string, appIndex: number, accountId: number, networkInfo: statistics.NetworkInfo): Promise<statistics.NetStatsInfo>; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function queryBundleStatsInfos(admin: Want, startTime: number, endTime: number, accountId: number): Array<BundleStatsInfo>;  差异内容：function queryBundleStatsInfos(admin: Want, startTime: number, endTime: number, accountId: number): Array<BundleStatsInfo>; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function addHideLauncherIcon(admin: Want, bundleNames: Array<string>): void;  差异内容：function addHideLauncherIcon(admin: Want, bundleNames: Array<string>): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function removeHideLauncherIcon(admin: Want, bundleNames: Array<string>): void;  差异内容：function removeHideLauncherIcon(admin: Want, bundleNames: Array<string>): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function getHideLauncherIcon(admin: Want | null): Array<string>;  差异内容：function getHideLauncherIcon(admin: Want | null): Array<string>; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：interface BundleStorageStats  差异内容：interface BundleStorageStats | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleStorageStats；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleStorageStats；  API声明：appSize: number;  差异内容：appSize: number; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleStorageStats；  API声明：dataSize: number;  差异内容：dataSize: number; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：function getInstalledBundleStorageStats(admin: Want, bundleNames: Array<string>, accountId: number): Promise<Array<BundleStorageStats>>;  差异内容：function getInstalledBundleStorageStats(admin: Want, bundleNames: Array<string>, accountId: number): Promise<Array<BundleStorageStats>>; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：common；  API声明：export interface PolicyChangedEvent  差异内容：export interface PolicyChangedEvent | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：PolicyChangedEvent；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：PolicyChangedEvent；  API声明：functionName: string;  差异内容：functionName: string; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：PolicyChangedEvent；  API声明：parameters: string;  差异内容：parameters: string; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：PolicyChangedEvent；  API声明：time: number;  差异内容：time: number; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：deviceSettings；  API声明：enum SwitchKey  差异内容：enum SwitchKey | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SwitchKey；  API声明：NEARLINK = 0  差异内容：NEARLINK = 0 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SwitchKey；  API声明：BLUETOOTH = 1  差异内容：BLUETOOTH = 1 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SwitchKey；  API声明：WIFI = 2  差异内容：WIFI = 2 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SwitchKey；  API声明：NFC = 3  差异内容：NFC = 3 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：deviceSettings；  API声明：enum SwitchStatus  差异内容：enum SwitchStatus | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SwitchStatus；  API声明：ON = 0  差异内容：ON = 0 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SwitchStatus；  API声明：OFF = 1  差异内容：OFF = 1 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SwitchStatus；  API声明：FORCE\_ON = 2  差异内容：FORCE\_ON = 2 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：deviceSettings；  API声明：function setSwitchStatus(admin: Want, key: SwitchKey, status: SwitchStatus): void;  差异内容：function setSwitchStatus(admin: Want, key: SwitchKey, status: SwitchStatus): void; | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：EnterpriseAdminExtensionAbility；  API声明：onBundleUpdated(bundleName: string, accountId: number): void;  差异内容：onBundleUpdated(bundleName: string, accountId: number): void; | api/@ohos.enterprise.EnterpriseAdminExtensionAbility.d.ts |
| 新增API | NA | 类名：EnterpriseAdminExtensionAbility；  API声明：onAdminPolicyChanged(event: common.PolicyChangedEvent): void;  差异内容：onAdminPolicyChanged(event: common.PolicyChangedEvent): void; | api/@ohos.enterprise.EnterpriseAdminExtensionAbility.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function setScreenLockDisabledForAccount(admin: Want, disable: boolean): void;  差异内容：function setScreenLockDisabledForAccount(admin: Want, disable: boolean): void; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function isScreenLockDisabledForAccount(admin: Want): boolean;  差异内容：function isScreenLockDisabledForAccount(admin: Want): boolean; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function setScreenWatermarkImage(admin: Want, pixelMap: image.PixelMap): void;  差异内容：function setScreenWatermarkImage(admin: Want, pixelMap: image.PixelMap): void; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function cancelScreenWatermarkImage(admin: Want): void;  差异内容：function cancelScreenWatermarkImage(admin: Want): void; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：telephonyManager；  API声明：function activeSim(admin: Want, slotId: number): void;  差异内容：function activeSim(admin: Want, slotId: number): void; | api/@ohos.enterprise.telephonyManager.d.ts |
| 新增API | NA | 类名：telephonyManager；  API声明：function deactiveSim(admin: Want, slotId: number): void;  差异内容：function deactiveSim(admin: Want, slotId: number): void; | api/@ohos.enterprise.telephonyManager.d.ts |
| 新增API | NA | 类名：telephonyManager；  API声明：function setDefaultData(admin: Want, slotId: number): void;  差异内容：function setDefaultData(admin: Want, slotId: number): void; | api/@ohos.enterprise.telephonyManager.d.ts |
| 新增API | NA | 类名：telephonyManager；  API声明：function getDefaultData(admin: Want): number;  差异内容：function getDefaultData(admin: Want): number; | api/@ohos.enterprise.telephonyManager.d.ts |
