---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-6112
title: MDM Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Release引入的API > MDM Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:f956c287f3e710eadd8000569294b30d7816d36c0a2ce3c6a7870870dbee26f2
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：systemManager；  API声明：function getInstallLocalEnterpriseAppEnabled(admin: Want): boolean;  差异内容：admin: Want | 类名：systemManager；  API声明：function getInstallLocalEnterpriseAppEnabled(admin: Want | null): boolean;  差异内容：admin: Want | null | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function setInstallLocalEnterpriseAppEnabledForAccount(admin: Want, isEnable: boolean, accountId: number): void;  差异内容：function setInstallLocalEnterpriseAppEnabledForAccount(admin: Want, isEnable: boolean, accountId: number): void; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function getInstallLocalEnterpriseAppEnabledForAccount(admin: Want | null, accountId: number): boolean;  差异内容：function getInstallLocalEnterpriseAppEnabledForAccount(admin: Want | null, accountId: number): boolean; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function setActivationLockDisabled(admin: Want, isDisabled: boolean, credential?: string): Promise<void>;  差异内容：function setActivationLockDisabled(admin: Want, isDisabled: boolean, credential?: string): Promise<void>; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：systemManager；  API声明：function isActivationLockDisabled(admin: Want): Promise<boolean>;  差异内容：function isActivationLockDisabled(admin: Want): Promise<boolean>; | api/@ohos.enterprise.systemManager.d.ts |
| 新增API | NA | 类名：SettingsItem；  API声明：DEVICE\_NAME = 0  差异内容：DEVICE\_NAME = 0 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：deviceSettings；  API声明：enum SettingsMenu  差异内容：enum SettingsMenu | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：ACCOUNT\_ID = 0  差异内容：ACCOUNT\_ID = 0 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：WIFI = 1  差异内容：WIFI = 1 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：WIFI\_PROXY\_SETTINGS = 2  差异内容：WIFI\_PROXY\_SETTINGS = 2 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：WIFI\_IP\_SETTINGS = 3  差异内容：WIFI\_IP\_SETTINGS = 3 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：BLUETOOTH = 4  差异内容：BLUETOOTH = 4 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：NETWORK = 5  差异内容：NETWORK = 5 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：MOBILE\_NETWORK = 6  差异内容：MOBILE\_NETWORK = 6 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：SUPER\_DEVICE = 7  差异内容：SUPER\_DEVICE = 7 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：MORE\_CONNECTIVITY\_OPTIONS = 8  差异内容：MORE\_CONNECTIVITY\_OPTIONS = 8 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：HOME\_SCREEN\_STYLE = 9  差异内容：HOME\_SCREEN\_STYLE = 9 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：DISPLAY\_BRIGHTNESS = 10  差异内容：DISPLAY\_BRIGHTNESS = 10 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：SOUND\_VIBRATION = 11  差异内容：SOUND\_VIBRATION = 11 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：NOTIFICATIONS = 12  差异内容：NOTIFICATIONS = 12 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：BIOMETRICS\_PASSWORD = 13  差异内容：BIOMETRICS\_PASSWORD = 13 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：APPS\_AND\_SERVICES = 14  差异内容：APPS\_AND\_SERVICES = 14 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：BATTERY = 15  差异内容：BATTERY = 15 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：STORAGE = 16  差异内容：STORAGE = 16 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：PRIVACY\_AND\_SECURITY = 17  差异内容：PRIVACY\_AND\_SECURITY = 17 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：DIGITAL\_BALANCE = 18  差异内容：DIGITAL\_BALANCE = 18 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：SMART\_ASSISTANT = 19  差异内容：SMART\_ASSISTANT = 19 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：ACCESSIBILITY = 20  差异内容：ACCESSIBILITY = 20 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：SYSTEM = 21  差异内容：SYSTEM = 21 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：ABOUT\_DEVICE = 22  差异内容：ABOUT\_DEVICE = 22 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：SYSTEM\_NAVIGATION = 23  差异内容：SYSTEM\_NAVIGATION = 23 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：LANGUAGE\_REGION = 24  差异内容：LANGUAGE\_REGION = 24 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：INPUT\_METHODS = 25  差异内容：INPUT\_METHODS = 25 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：DATE\_TIME = 26  差异内容：DATE\_TIME = 26 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：DATA\_CLONE = 27  差异内容：DATA\_CLONE = 27 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：BACKUP\_SETTINGS = 28  差异内容：BACKUP\_SETTINGS = 28 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：RESET = 29  差异内容：RESET = 29 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：SUPERHUB = 30  差异内容：SUPERHUB = 30 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：USER\_EXPERIENCE = 31  差异内容：USER\_EXPERIENCE = 31 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：SCREEN\_CAST = 32  差异内容：SCREEN\_CAST = 32 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：PRINTERS\_SCANNERS = 33  差异内容：PRINTERS\_SCANNERS = 33 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：MOBILE\_DATA = 34  差异内容：MOBILE\_DATA = 34 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：PERSONAL\_HOTSPOT = 35  差异内容：PERSONAL\_HOTSPOT = 35 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：SIM\_MANAGEMENT = 36  差异内容：SIM\_MANAGEMENT = 36 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：AIRPLANE\_MODE = 37  差异内容：AIRPLANE\_MODE = 37 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：MANAGE\_DATA\_USAGE = 38  差异内容：MANAGE\_DATA\_USAGE = 38 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：VPN\_SETTINGS = 39  差异内容：VPN\_SETTINGS = 39 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：TEXT\_DISPLAY\_SIZE = 40  差异内容：TEXT\_DISPLAY\_SIZE = 40 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：APP\_DUPLICATOR = 41  差异内容：APP\_DUPLICATOR = 41 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：SettingsMenu；  API声明：SEARCH = 42  差异内容：SEARCH = 42 | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：deviceSettings；  API声明：function addHiddenSettingsMenu(admin: Want, menusToHidden: Array<SettingsMenu>): void;  差异内容：function addHiddenSettingsMenu(admin: Want, menusToHidden: Array<SettingsMenu>): void; | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：deviceSettings；  API声明：function removeHiddenSettingsMenu(admin: Want, menusToHidden: Array<SettingsMenu>): void;  差异内容：function removeHiddenSettingsMenu(admin: Want, menusToHidden: Array<SettingsMenu>): void; | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：deviceSettings；  API声明：function getHiddenSettingsMenu(admin: Want): Array<SettingsMenu>;  差异内容：function getHiddenSettingsMenu(admin: Want): Array<SettingsMenu>; | api/@ohos.enterprise.deviceSettings.d.ts |
| 新增API | NA | 类名：restrictions；  API声明：enum FeatureForDevice  差异内容：enum FeatureForDevice | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：FeatureForDevice；  API声明：WIFI\_P2P = 0  差异内容：WIFI\_P2P = 0 | api/@ohos.enterprise.restrictions.d.ts |
