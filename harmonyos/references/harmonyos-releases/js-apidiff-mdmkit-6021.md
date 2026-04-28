---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-6021
title: MDM Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:47+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:03d6b5793c6bbf37ad39c9469af226f701cffc4bf6675fe1c0908c0e322e8f12
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace common  差异内容：declare namespace common | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：common；  API声明：export interface ApplicationInstance  差异内容：export interface ApplicationInstance | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ApplicationInstance；  API声明：appIdentifier: string;  差异内容：appIdentifier: string; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ApplicationInstance；  API声明：accountId: number;  差异内容：accountId: number; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ApplicationInstance；  API声明：appIndex: number;  差异内容：appIndex: number; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：common；  API声明：export enum ManagedPolicy  差异内容：export enum ManagedPolicy | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ManagedPolicy；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ManagedPolicy；  API声明：DISALLOW = 1  差异内容：DISALLOW = 1 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：ManagedPolicy；  API声明：FORCE\_OPEN = 2  差异内容：FORCE\_OPEN = 2 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：common；  API声明：export interface InstallationResult  差异内容：export interface InstallationResult | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：InstallationResult；  API声明：result: Result;  差异内容：result: Result; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：InstallationResult；  API声明：message: string;  差异内容：message: string; | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：common；  API声明：export enum Result  差异内容：export enum Result | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：Result；  API声明：SUCCESS = 0  差异内容：SUCCESS = 0 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：Result；  API声明：FAIL = -1  差异内容：FAIL = -1 | api/@ohos.enterprise.common.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function addUserNonStopApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void;  差异内容：function addUserNonStopApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function removeUserNonStopApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void;  差异内容：function removeUserNonStopApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function getUserNonStopApps(admin: Want): Array<common.ApplicationInstance>;  差异内容：function getUserNonStopApps(admin: Want): Array<common.ApplicationInstance>; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function addFreezeExemptedApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void;  差异内容：function addFreezeExemptedApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function removeFreezeExemptedApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void;  差异内容：function removeFreezeExemptedApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function getFreezeExemptedApps(admin: Want): Array<common.ApplicationInstance>;  差异内容：function getFreezeExemptedApps(admin: Want): Array<common.ApplicationInstance>; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：function installMarketApps(admin: Want, bundleNames: Array<string>): void;  差异内容：function installMarketApps(admin: Want, bundleNames: Array<string>): void; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：EnterpriseAdminExtensionAbility；  API声明：onMarketAppInstallResult(bundleName: string, result: common.InstallationResult): void;  差异内容：onMarketAppInstallResult(bundleName: string, result: common.InstallationResult): void; | api/@ohos.enterprise.EnterpriseAdminExtensionAbility.d.ts |
| 新增API | NA | 类名：FirewallRule；  API声明：family?: number;  差异内容：family?: number; | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：DomainFilterRule；  API声明：family?: number;  差异内容：family?: number; | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function setExternalSourceExtensionsPolicy(admin: Want, policy: common.ManagedPolicy): void;  差异内容：function setExternalSourceExtensionsPolicy(admin: Want, policy: common.ManagedPolicy): void; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function getExternalSourceExtensionsPolicy(admin: Want): common.ManagedPolicy;  差异内容：function getExternalSourceExtensionsPolicy(admin: Want): common.ManagedPolicy; | api/@ohos.enterprise.securityManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.enterprise.common.d.ts  差异内容：MDMKit | api/@ohos.enterprise.common.d.ts |
