---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-6101
title: MDM Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > MDM Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6ac2e4582a523c6b51dff3564d318088c18310e2e0f2304b7f44da167512401d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：adminManager；  API声明：function disableAdmin(admin: Want, userId?: number): Promise<void>;  差异内容：ohos.permission.MANAGE\_ENTERPRISE\_DEVICE\_ADMIN or ohos.permission.START\_PROVISIONING\_MESSAGE | 类名：adminManager；  API声明：function disableAdmin(admin: Want, userId?: number): Promise<void>;  差异内容：ohos.permission.MANAGE\_ENTERPRISE\_DEVICE\_ADMIN or ohos.permission.START\_PROVISIONING\_MESSAGE or ohos.permission.ENTERPRISE\_DEACTIVATE\_DEVICE\_ADMIN | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class EnterpriseAdminExtensionContext  差异内容：declare class EnterpriseAdminExtensionContext | api/application/EnterpriseAdminExtensionContext.d.ts |
| 新增API | NA | 类名：EnterpriseAdminExtensionContext；  API声明：startAbilityByAdmin(admin: Want, want: Want): Promise<void>;  差异内容：startAbilityByAdmin(admin: Want, want: Want): Promise<void>; | api/application/EnterpriseAdminExtensionContext.d.ts |
| 新增API | NA | 类名：adminManager；  API声明：function enableDeviceAdmin(admin: Want): Promise<void>;  差异内容：function enableDeviceAdmin(admin: Want): Promise<void>; | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：adminManager；  API声明：function disableDeviceAdmin(admin: Want): Promise<void>;  差异内容：function disableDeviceAdmin(admin: Want): Promise<void>; | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：function getInstalledBundleList(admin: Want, accountId: number, bundleInfoGetFlag: number): Promise<Array<BundleInfo>>;  差异内容：function getInstalledBundleList(admin: Want, accountId: number, bundleInfoGetFlag: number): Promise<Array<BundleInfo>>; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：export enum BundleInfoGetFlag  差异内容：export enum BundleInfoGetFlag | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleInfoGetFlag；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleInfoGetFlag；  API声明：WITH\_APPLICATION\_INFO = 1 << 0  差异内容：WITH\_APPLICATION\_INFO = 1 << 0 | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleInfoGetFlag；  API声明：WITH\_SIGNATURE\_INFO = 1 << 1  差异内容：WITH\_SIGNATURE\_INFO = 1 << 1 | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleInfoGetFlag；  API声明：WITH\_APPLICATION\_ICON\_INFO = 1 << 2  差异内容：WITH\_APPLICATION\_ICON\_INFO = 1 << 2 | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly iconData: string;  差异内容：readonly iconData: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function setAbilityDisabled(admin: Want, bundleName: string, accountId: number, abilityName: string, isDisabled: boolean): void;  差异内容：function setAbilityDisabled(admin: Want, bundleName: string, accountId: number, abilityName: string, isDisabled: boolean): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function isAbilityDisabled(admin: Want, bundleName: string, accountId: number, abilityName: string): boolean;  差异内容：function isAbilityDisabled(admin: Want, bundleName: string, accountId: number, abilityName: string): boolean; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：common；  API声明：export type EnterpriseAdminExtensionContext = \_EnterpriseAdminExtensionContext.default;  差异内容：export type EnterpriseAdminExtensionContext = \_EnterpriseAdminExtensionContext.default; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：EnterpriseAdminExtensionAbility；  API声明：context: EnterpriseAdminExtensionContext;  差异内容：context: EnterpriseAdminExtensionContext; | api/@ohos.enterprise.EnterpriseAdminExtensionAbility.d.ts |
| 新增API | NA | 类名：EnterpriseAdminExtensionAbility；  API声明：onDeviceAdminEnabled(bundleName: string): void;  差异内容：onDeviceAdminEnabled(bundleName: string): void; | api/@ohos.enterprise.EnterpriseAdminExtensionAbility.d.ts |
| 新增API | NA | 类名：EnterpriseAdminExtensionAbility；  API声明：onDeviceAdminDisabled(bundleName: string): void;  差异内容：onDeviceAdminDisabled(bundleName: string): void; | api/@ohos.enterprise.EnterpriseAdminExtensionAbility.d.ts |
| 新增API | NA | 类名：EnterpriseAdminExtensionAbility；  API声明：onLogCollected(result: common.Result): void;  差异内容：onLogCollected(result: common.Result): void; | api/@ohos.enterprise.EnterpriseAdminExtensionAbility.d.ts |
| 新增API | NA | 类名：EnterpriseAdminExtensionAbility；  API声明：onKeyEvent(keyEvent: systemManager.KeyEvent): void;  差异内容：onKeyEvent(keyEvent: systemManager.KeyEvent): void; | api/@ohos.enterprise.EnterpriseAdminExtensionAbility.d.ts |
| 新增API | NA | 类名：networkManager；  API声明：enum LogType  差异内容：enum LogType | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：LogType；  API声明：NFLOG = 0  差异内容：NFLOG = 0 | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：FirewallRule；  API声明：logType?: LogType;  差异内容：logType?: LogType; | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：DomainFilterRule；  API声明：logType?: LogType;  差异内容：logType?: LogType; | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：networkManager；  API声明：enum IpSetMode  差异内容：enum IpSetMode | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：IpSetMode；  API声明：STATIC = 0  差异内容：STATIC = 0 | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：IpSetMode；  API声明：DHCP = 1  差异内容：DHCP = 1 | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：networkManager；  API声明：interface InterfaceConfig  差异内容：interface InterfaceConfig | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：InterfaceConfig；  API声明：ipSetMode: IpSetMode;  差异内容：ipSetMode: IpSetMode; | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：InterfaceConfig；  API声明：ipAddress?: string;  差异内容：ipAddress?: string; | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：InterfaceConfig；  API声明：gateway?: string;  差异内容：gateway?: string; | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：InterfaceConfig；  API声明：netMask?: string;  差异内容：netMask?: string; | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：InterfaceConfig；  API声明：dnsServers?: string;  差异内容：dnsServers?: string; | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：networkManager；  API声明：function setEthernetConfig(admin: Want, networkInterface: string, config: InterfaceConfig): void;  差异内容：function setEthernetConfig(admin: Want, networkInterface: string, config: InterfaceConfig): void; | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：restrictions；  API声明：function setUserRestrictionForAccount(admin: Want, settingsItem: string, accountId: number, restricted: boolean): void;  差异内容：function setUserRestrictionForAccount(admin: Want, settingsItem: string, accountId: number, restricted: boolean): void; | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：restrictions；  API声明：function getUserRestrictedForAccount(admin: Want | null, settingsItem: string, accountId: number): boolean;  差异内容：function getUserRestrictedForAccount(admin: Want | null, settingsItem: string, accountId: number): boolean; | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function installEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, fd: number, accountId: number): void;  差异内容：function installEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, fd: number, accountId: number): void; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function uninstallEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, accountId: number): void;  差异内容：function uninstallEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, accountId: number): void; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function addKeyEventPolicies(admin: Want, keyPolicies: Array<KeyEventPolicy>): void;  差异内容：function addKeyEventPolicies(admin: Want, keyPolicies: Array<KeyEventPolicy>): void; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function removeKeyEventPolicies(admin: Want, keyCodes: Array<KeyCode>): void;  差异内容：function removeKeyEventPolicies(admin: Want, keyCodes: Array<KeyCode>): void; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function getKeyEventPolicies(admin: Want): Array<KeyEventPolicy>;  差异内容：function getKeyEventPolicies(admin: Want): Array<KeyEventPolicy>; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：interface KeyEventPolicy  差异内容：interface KeyEventPolicy | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：KeyEventPolicy；  API声明：keyCode: KeyCode;  差异内容：keyCode: KeyCode; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：KeyEventPolicy；  API声明：keyPolicy: KeyPolicy;  差异内容：keyPolicy: KeyPolicy; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：enum KeyCode  差异内容：enum KeyCode | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：POWER = 0  差异内容：POWER = 0 | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：VOLUME\_UP = 1  差异内容：VOLUME\_UP = 1 | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：VOLUME\_DOWN = 2  差异内容：VOLUME\_DOWN = 2 | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：BACK = 3  差异内容：BACK = 3 | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：HOME = 4  差异内容：HOME = 4 | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：RECENT = 5  差异内容：RECENT = 5 | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：enum KeyPolicy  差异内容：enum KeyPolicy | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：KeyPolicy；  API声明：INTERCEPTION = 0  差异内容：INTERCEPTION = 0 | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：KeyPolicy；  API声明：CUSTOM = 1  差异内容：CUSTOM = 1 | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：interface KeyEvent  差异内容：interface KeyEvent | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：KeyEvent；  API声明：keyCode: KeyCode;  差异内容：keyCode: KeyCode; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：KeyEvent；  API声明：keyAction: KeyAction;  差异内容：keyAction: KeyAction; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：KeyEvent；  API声明：actionTime: number;  差异内容：actionTime: number; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：KeyEvent；  API声明：keyItems: Array<KeyItem>;  差异内容：keyItems: Array<KeyItem>; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：enum KeyAction  差异内容：enum KeyAction | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：KeyAction；  API声明：UNKNOWN = -1  差异内容：UNKNOWN = -1 | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：KeyAction；  API声明：DOWN = 0  差异内容：DOWN = 0 | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：KeyAction；  API声明：UP = 1  差异内容：UP = 1 | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：interface KeyItem  差异内容：interface KeyItem | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：KeyItem；  API声明：keyCode: KeyCode;  差异内容：keyCode: KeyCode; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：KeyItem；  API声明：pressed: boolean;  差异内容：pressed: boolean; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：KeyItem；  API声明：downTime: number;  差异内容：downTime: number; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function startCollectLog(admin: Want): Promise<void>;  差异内容：function startCollectLog(admin: Want): Promise<void>; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function finishLogCollected(admin: Want): void;  差异内容：function finishLogCollected(admin: Want): void; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：telephonyManager；  API声明：function hangupCalling(admin: Want): void;  差异内容：function hangupCalling(admin: Want): void; | api/@ohos.enterprise.telephonyManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\application\EnterpriseAdminExtensionContext.d.ts  差异内容：MDMKit | api/application/EnterpriseAdminExtensionContext.d.ts |
