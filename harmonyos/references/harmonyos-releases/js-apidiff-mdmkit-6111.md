---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-6111
title: MDM Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > MDM Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:c7245b660f0796aab8b5ee014b61862e18b7e90497952300eb50a6bb79d5490b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：ManagedEvent；  API声明：MANAGED\_EVENT\_STARTUP\_GUIDE\_COMPLETED = 8  差异内容：MANAGED\_EVENT\_STARTUP\_GUIDE\_COMPLETED = 8 | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：ManagedEvent；  API声明：MANAGED\_EVENT\_BOOT\_COMPLETED = 9  差异内容：MANAGED\_EVENT\_BOOT\_COMPLETED = 9 | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：KioskFeature；  API声明：ALLOW\_GESTURE\_CONTROL = 3  差异内容：ALLOW\_GESTURE\_CONTROL = 3 | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：KioskFeature；  API声明：ALLOW\_SIDE\_DOCK = 4  差异内容：ALLOW\_SIDE\_DOCK = 4 | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：interface DockInfo  差异内容：interface DockInfo | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：DockInfo；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：DockInfo；  API声明：abilityName: string;  差异内容：abilityName: string; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：DockInfo；  API声明：index: number;  差异内容：index: number; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function addDockApp(admin: Want, bundleName: string, abilityName: string, index?: number): void;  差异内容：function addDockApp(admin: Want, bundleName: string, abilityName: string, index?: number): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function removeDockApp(admin: Want, bundleName: string, abilityName: string): void;  差异内容：function removeDockApp(admin: Want, bundleName: string, abilityName: string): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function getDockApps(admin: Want): Array<DockInfo>;  差异内容：function getDockApps(admin: Want): Array<DockInfo>; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：common；  API声明：export enum StartupScene  差异内容：export enum StartupScene | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：StartupScene；  API声明：USER\_SETUP = 0  差异内容：USER\_SETUP = 0 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：StartupScene；  API声明：OTA = 1  差异内容：OTA = 1 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：StartupScene；  API声明：DEVICE\_PROVISION = 2  差异内容：DEVICE\_PROVISION = 2 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：deviceSettings；  API声明：enum SettingsItem  差异内容：enum SettingsItem | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsItem；  API声明：FLOATING\_NAVIGATION = 1  差异内容：FLOATING\_NAVIGATION = 1 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：deviceSettings；  API声明：function setValueForAccount(admin: Want, item: SettingsItem, accountId: number, value: string): void;  差异内容：function setValueForAccount(admin: Want, item: SettingsItem, accountId: number, value: string): void; | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：deviceSettings；  API声明：function getValueForAccount(admin: Want, item: SettingsItem, accountId: number): string;  差异内容：function getValueForAccount(admin: Want, item: SettingsItem, accountId: number): string; | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：EnterpriseAdminExtensionAbility；  API声明：onStartupGuideCompleted(scene: common.StartupScene): void;  差异内容：onStartupGuideCompleted(scene: common.StartupScene): void; | api/@ohos.enterprise.EnterpriseAdminExtensionAbility.d.ts |
| 新增API | NA | 类名：EnterpriseAdminExtensionAbility；  API声明：onDeviceBootCompleted(): void;  差异内容：onDeviceBootCompleted(): void; | api/@ohos.enterprise.EnterpriseAdminExtensionAbility.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function installEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, fd: number, accountId: number): void;  差异内容：function installEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, fd: number, accountId: number): void; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function uninstallEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, accountId: number): void;  差异内容：function uninstallEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, accountId: number): void; | api/@ohos.enterprise.securityManager.d.ts |
