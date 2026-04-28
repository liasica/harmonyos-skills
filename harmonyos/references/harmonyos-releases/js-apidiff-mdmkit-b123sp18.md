---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-b123sp18
title: MDM Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > API变更清单 > MDM Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:52+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:4b25739636d8dff9c1d903144146ae861741f47feeba52f35e8e5e89cf057947
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：EnterpriseAdminExtensionAbility；  API声明：onBundleAdded(bundleName: string, accountId: number): void;  差异内容：onBundleAdded(bundleName: string, accountId: number): void; | api/@ohos.enterprise.EnterpriseAdminExtensionAbility.d.ts |
| 新增API | NA | 类名：EnterpriseAdminExtensionAbility；  API声明：onBundleRemoved(bundleName: string, accountId: number): void;  差异内容：onBundleRemoved(bundleName: string, accountId: number): void; | api/@ohos.enterprise.EnterpriseAdminExtensionAbility.d.ts |
| 新增API | NA | 类名：adminManager；  API声明：function setDelegatedPolicies(admin: Want, bundleName: string, policies: Array<string>): void;  差异内容：function setDelegatedPolicies(admin: Want, bundleName: string, policies: Array<string>): void; | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：adminManager；  API声明：function getDelegatedPolicies(admin: Want, bundleName: string): Array<string>;  差异内容：function getDelegatedPolicies(admin: Want, bundleName: string): Array<string>; | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：adminManager；  API声明：function getDelegatedBundleNames(admin: Want, policy: string): Array<string>;  差异内容：function getDelegatedBundleNames(admin: Want, policy: string): Array<string>; | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function addKeepAliveApps(admin: Want, bundleNames: Array<string>, accountId: number): void;  差异内容：function addKeepAliveApps(admin: Want, bundleNames: Array<string>, accountId: number): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function removeKeepAliveApps(admin: Want, bundleNames: Array<string>, accountId: number): void;  差异内容：function removeKeepAliveApps(admin: Want, bundleNames: Array<string>, accountId: number): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function getKeepAliveApps(admin: Want, accountId: number): Array<string>;  差异内容：function getKeepAliveApps(admin: Want, accountId: number): Array<string>; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：restrictions；  API声明：function setDisallowedPolicyForAccount(admin: Want, feature: string, disallow: boolean, accountId: number): void;  差异内容：function setDisallowedPolicyForAccount(admin: Want, feature: string, disallow: boolean, accountId: number): void; | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：restrictions；  API声明：function getDisallowedPolicyForAccount(admin: Want, feature: string, accountId: number): boolean;  差异内容：function getDisallowedPolicyForAccount(admin: Want, feature: string, accountId: number): boolean; | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：restrictions；  API声明：function addDisallowedListForAccount(admin: Want, feature: string, list: Array<string>, accountId: number): void;  差异内容：function addDisallowedListForAccount(admin: Want, feature: string, list: Array<string>, accountId: number): void; | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：restrictions；  API声明：function removeDisallowedListForAccount(admin: Want, feature: string, list: Array<string>, accountId: number): void;  差异内容：function removeDisallowedListForAccount(admin: Want, feature: string, list: Array<string>, accountId: number): void; | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：restrictions；  API声明：function getDisallowedListForAccount(admin: Want, feature: string, accountId: number): Array<string>;  差异内容：function getDisallowedListForAccount(admin: Want, feature: string, accountId: number): Array<string>; | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function setWatermarkImage(admin: Want, bundleName: string, source: string | image.PixelMap, accountId: number): void;  差异内容：function setWatermarkImage(admin: Want, bundleName: string, source: string | image.PixelMap, accountId: number): void; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：securityManager；  API声明：function cancelWatermarkImage(admin: Want, bundleName: string, accountId: number): void;  差异内容：function cancelWatermarkImage(admin: Want, bundleName: string, accountId: number): void; | api/@ohos.enterprise.securityManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明： enum Descriptor  差异内容： enum Descriptor | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：Descriptor；  API声明：INTERFACE = 0  差异内容：INTERFACE = 0 | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：Descriptor；  API声明：DEVICE = 1  差异内容：DEVICE = 1 | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明： export interface UsbDeviceType  差异内容： export interface UsbDeviceType | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：UsbDeviceType；  API声明：baseClass: number;  差异内容：baseClass: number; | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：UsbDeviceType；  API声明：subClass: number;  差异内容：subClass: number; | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：UsbDeviceType；  API声明：protocol: number;  差异内容：protocol: number; | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：UsbDeviceType；  API声明：descriptor: Descriptor;  差异内容：descriptor: Descriptor; | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function addDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void;  差异内容：function addDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void; | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function removeDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void;  差异内容：function removeDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void; | api/@ohos.enterprise.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function getDisallowedUsbDevices(admin: Want): Array<UsbDeviceType>;  差异内容：function getDisallowedUsbDevices(admin: Want): Array<UsbDeviceType>; | api/@ohos.enterprise.usbManager.d.ts |
