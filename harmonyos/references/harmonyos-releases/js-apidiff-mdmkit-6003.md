---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-6003
title: MDM Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > MDM Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:19+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:daae4fd25e99c85d2fd435ec34e292be53902482becc40a0a1941f12b7830579
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：adminManager；  API声明：function disableAdmin(admin: Want, userId?: number): Promise<void>;  差异内容：401 | 类名：adminManager；  API声明：function disableAdmin(admin: Want, userId?: number): Promise<void>;  差异内容：NA | api/@ohos.enterprise.adminManager.d.ts |
| 删除错误码 | 类名：restrictions；  API声明：function setDisallowedPolicyForAccount(admin: Want, feature: string, disallow: boolean, accountId: number): void;  差异内容：401 | 类名：restrictions；  API声明：function setDisallowedPolicyForAccount(admin: Want, feature: string, disallow: boolean, accountId: number): void;  差异内容：NA | api/@ohos.enterprise.restrictions.d.ts |
| 删除错误码 | 类名：restrictions；  API声明：function getDisallowedPolicyForAccount(admin: Want, feature: string, accountId: number): boolean;  差异内容：401 | 类名：restrictions；  API声明：function getDisallowedPolicyForAccount(admin: Want | null, feature: string, accountId: number): boolean;  差异内容：NA | api/@ohos.enterprise.restrictions.d.ts |
| 权限变更 | 类名：adminManager；  API声明：function disableAdmin(admin: Want, userId?: number): Promise<void>;  差异内容：ohos.permission.MANAGE\_ENTERPRISE\_DEVICE\_ADMIN | 类名：adminManager；  API声明：function disableAdmin(admin: Want, userId?: number): Promise<void>;  差异内容：ohos.permission.MANAGE\_ENTERPRISE\_DEVICE\_ADMIN or ohos.permission.START\_PROVISIONING\_MESSAGE | api/@ohos.enterprise.adminManager.d.ts |
| 函数变更 | 类名：restrictions；  API声明：function getDisallowedPolicyForAccount(admin: Want, feature: string, accountId: number): boolean;  差异内容：admin: Want | 类名：restrictions；  API声明：function getDisallowedPolicyForAccount(admin: Want | null, feature: string, accountId: number): boolean;  差异内容：admin: Want | null | api/@ohos.enterprise.restrictions.d.ts |
| 函数变更 | 类名：applicationManager；  API声明：function setAllowedKioskApps(admin: Want, bundleNames: Array<string>): void;  差异内容：admin: Want, bundleNames: Array<string> | 类名：applicationManager；  API声明：function setAllowedKioskApps(admin: Want, appIdentifiers: Array<string>): void;  差异内容：admin: Want, appIdentifiers: Array<string> | api/@ohos.enterprise.applicationManager.d.ts |
| 函数变更 | 类名：applicationManager；  API声明：function isAppKioskAllowed(bundleName: string): boolean;  差异内容：bundleName: string | 类名：applicationManager；  API声明：function isAppKioskAllowed(appIdentifier: string): boolean;  差异内容：appIdentifier: string | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：adminManager；  API声明：export enum Policy  差异内容：export enum Policy | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：Policy；  API声明：BLOCK\_LIST = 0  差异内容：BLOCK\_LIST = 0 | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：Policy；  API声明：TRUST\_LIST = 1  差异内容：TRUST\_LIST = 1 | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：adminManager；  API声明：function isByodAdmin(admin: Want): boolean;  差异内容：function isByodAdmin(admin: Want): boolean; | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function addAutoStartApps(admin: Want, autoStartApps: Array<Want>, accountId: number, disallowModify: boolean): void;  差异内容：function addAutoStartApps(admin: Want, autoStartApps: Array<Want>, accountId: number, disallowModify: boolean): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function removeAutoStartApps(admin: Want, autoStartApps: Array<Want>, accountId: number): void;  差异内容：function removeAutoStartApps(admin: Want, autoStartApps: Array<Want>, accountId: number): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function getAutoStartApps(admin: Want, accountId: number): Array<Want>;  差异内容：function getAutoStartApps(admin: Want, accountId: number): Array<Want>; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function addKeepAliveApps(admin: Want, bundleNames: Array<string>, accountId: number, disallowModify: boolean): void;  差异内容：function addKeepAliveApps(admin: Want, bundleNames: Array<string>, accountId: number, disallowModify: boolean): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：enum KioskFeature  差异内容：enum KioskFeature | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：KioskFeature；  API声明：ALLOW\_NOTIFICATION\_CENTER = 1  差异内容：ALLOW\_NOTIFICATION\_CENTER = 1 | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：KioskFeature；  API声明：ALLOW\_CONTROL\_CENTER = 2  差异内容：ALLOW\_CONTROL\_CENTER = 2 | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function isModifyAutoStartAppsDisallowed(admin: Want, autoStartApp: Want, accountId: number): boolean;  差异内容：function isModifyAutoStartAppsDisallowed(admin: Want, autoStartApp: Want, accountId: number): boolean; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function isModifyKeepAliveAppsDisallowed(admin: Want, accountId: number, bundleName: string): boolean;  差异内容：function isModifyKeepAliveAppsDisallowed(admin: Want, accountId: number, bundleName: string): boolean; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function setKioskFeatures(admin: Want, features: Array<KioskFeature>): void;  差异内容：function setKioskFeatures(admin: Want, features: Array<KioskFeature>): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：restrictions；  API声明：function getUserRestricted(admin: Want, settingsItem: string): boolean;  差异内容：function getUserRestricted(admin: Want, settingsItem: string): boolean; | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：Protocol；  API声明：OPP = 2  差异内容：OPP = 2 | api/@ohos.enterprise.bluetoothManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：function addInstallationAllowedAppDistributionTypes(admin: Want, appDistributionTypes: Array<AppDistributionType>): void;  差异内容：function addInstallationAllowedAppDistributionTypes(admin: Want, appDistributionTypes: Array<AppDistributionType>): void; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：function removeInstallationAllowedAppDistributionTypes(admin: Want, appDistributionTypes: Array<AppDistributionType>): void;  差异内容：function removeInstallationAllowedAppDistributionTypes(admin: Want, appDistributionTypes: Array<AppDistributionType>): void; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：function getInstallationAllowedAppDistributionTypes(admin: Want): Array<AppDistributionType>;  差异内容：function getInstallationAllowedAppDistributionTypes(admin: Want): Array<AppDistributionType>; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：enum AppDistributionType  差异内容：enum AppDistributionType | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：AppDistributionType；  API声明：APP\_GALLERY = 1  差异内容：APP\_GALLERY = 1 | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：AppDistributionType；  API声明：ENTERPRISE = 2  差异内容：ENTERPRISE = 2 | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：AppDistributionType；  API声明：ENTERPRISE\_NORMAL = 3  差异内容：ENTERPRISE\_NORMAL = 3 | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：AppDistributionType；  API声明：ENTERPRISE\_MDM = 4  差异内容：ENTERPRISE\_MDM = 4 | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：AppDistributionType；  API声明：INTERNALTESTING = 5  差异内容：INTERNALTESTING = 5 | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：AppDistributionType；  API声明：CROWDTESTING = 6  差异内容：CROWDTESTING = 6 | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：deviceSettings；  API声明：function setHomeWallpaper(admin: Want, fd: number): Promise<void>;  差异内容：function setHomeWallpaper(admin: Want, fd: number): Promise<void>; | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：deviceSettings；  API声明：function setUnlockWallpaper(admin: Want, fd: number): Promise<void>;  差异内容：function setUnlockWallpaper(admin: Want, fd: number): Promise<void>; | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：export interface ApplicationInstance  差异内容：export interface ApplicationInstance | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：ApplicationInstance；  API声明：appIdentifier: string;  差异内容：appIdentifier: string; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：ApplicationInstance；  API声明：accountId: number;  差异内容：accountId: number; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：ApplicationInstance；  API声明：appIndex: number;  差异内容：appIndex: number; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function setPermissionManagedState(admin: Want, applicationInstance: ApplicationInstance, permissions: Array<string>, managedState: PermissionManagedState): void;  差异内容：function setPermissionManagedState(admin: Want, applicationInstance: ApplicationInstance, permissions: Array<string>, managedState: PermissionManagedState): void; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function getPermissionManagedState(admin: Want, applicationInstance: ApplicationInstance, permission: string): PermissionManagedState;  差异内容：function getPermissionManagedState(admin: Want, applicationInstance: ApplicationInstance, permission: string): PermissionManagedState; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：export enum PermissionManagedState  差异内容：export enum PermissionManagedState | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：PermissionManagedState；  API声明：DEFAULT = 1  差异内容：DEFAULT = 1 | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：PermissionManagedState；  API声明：GRANTED = 0  差异内容：GRANTED = 0 | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：PermissionManagedState；  API声明：DENIED = -1  差异内容：DENIED = -1 | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function setAutoUnlockAfterReboot(admin: Want, isAllowed: boolean): void;  差异内容：function setAutoUnlockAfterReboot(admin: Want, isAllowed: boolean): void; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function getAutoUnlockAfterReboot(admin: Want): boolean;  差异内容：function getAutoUnlockAfterReboot(admin: Want): boolean; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function setInstallLocalEnterpriseAppEnabled(admin: Want, isEnable: boolean): void;  差异内容：function setInstallLocalEnterpriseAppEnabled(admin: Want, isEnable: boolean): void; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function getInstallLocalEnterpriseAppEnabled(admin: Want): boolean;  差异内容：function getInstallLocalEnterpriseAppEnabled(admin: Want): boolean; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：enum NearLinkProtocol  差异内容：enum NearLinkProtocol | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：NearLinkProtocol；  API声明：SSAP = 0  差异内容：SSAP = 0 | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：NearLinkProtocol；  API声明：DATA\_TRANSFER = 1  差异内容：DATA\_TRANSFER = 1 | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function addDisallowedNearLinkProtocols(admin: Want, protocols: Array<NearLinkProtocol>, accountId: number): void;  差异内容：function addDisallowedNearLinkProtocols(admin: Want, protocols: Array<NearLinkProtocol>, accountId: number): void; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function removeDisallowedNearLinkProtocols(admin: Want, protocols: Array<NearLinkProtocol>, accountId: number): void;  差异内容：function removeDisallowedNearLinkProtocols(admin: Want, protocols: Array<NearLinkProtocol>, accountId: number): void; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function getDisallowedNearLinkProtocols(admin: Want, accountId: number): Array<NearLinkProtocol>;  差异内容：function getDisallowedNearLinkProtocols(admin: Want, accountId: number): Array<NearLinkProtocol>; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：telephonyManager；  API声明：function addOutgoingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void;  差异内容：function addOutgoingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void; | api/@ohos.enterprise.telephonyManager.d.ts |
| 新增API | NA | 类名：telephonyManager；  API声明：function removeOutgoingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void;  差异内容：function removeOutgoingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void; | api/@ohos.enterprise.telephonyManager.d.ts |
| 新增API | NA | 类名：telephonyManager；  API声明：function getOutgoingCallPolicyNumbers(admin: Want, policy: adminManager.Policy): Array<string>;  差异内容：function getOutgoingCallPolicyNumbers(admin: Want, policy: adminManager.Policy): Array<string>; | api/@ohos.enterprise.telephonyManager.d.ts |
| 新增API | NA | 类名：telephonyManager；  API声明：function addIncomingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void;  差异内容：function addIncomingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void; | api/@ohos.enterprise.telephonyManager.d.ts |
| 新增API | NA | 类名：telephonyManager；  API声明：function removeIncomingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void;  差异内容：function removeIncomingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void; | api/@ohos.enterprise.telephonyManager.d.ts |
| 新增API | NA | 类名：telephonyManager；  API声明：function getIncomingCallPolicyNumbers(admin: Want, policy: adminManager.Policy): Array<string>;  差异内容：function getIncomingCallPolicyNumbers(admin: Want, policy: adminManager.Policy): Array<string>; | api/@ohos.enterprise.telephonyManager.d.ts |
