---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-7003
title: MDM Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Release引入的API > MDM Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2bdd957eebc7db7d6ee18319b2bf2ab9aa8c95b1fa648fb7455b76a0e79b3311
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：deviceControl；  API声明：function operateDevice(admin: Want, operation: Operation, addition?: string): void;  差异内容：NA | 类名：deviceControl；  API声明：function operateDevice(admin: Want, operation: Operation, addition?: string): void;  差异内容：9201048 | api/@ohos.enterprise.deviceControl.d.ts |
| 删除错误码 | 类名：systemManager；  API声明：function isOtaUpdateNonceEnable(admin: Want): boolean;  差异内容：801 | 类名：systemManager；  API声明：function isOtaUpdateNonceEnable(admin: Want): boolean;  差异内容：NA | api/@ohos.enterprise.systemManager.d.ts |
| 权限变更 | 类名：usbManager；  API声明：function getUsbStorageDeviceAccessPolicy(admin: Want | null): UsbPolicy;  差异内容：ohos.permission.ENTERPRISE\_MANAGE\_USB or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS [since 26.0.0] | 类名：usbManager；  API声明：function getUsbStorageDeviceAccessPolicy(admin: Want | null): UsbPolicy;  差异内容：ohos.permission.ENTERPRISE\_MANAGE\_USB or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS | api/@ohos.enterprise.usbManager.d.ts |
| 函数变更 | 类名：restrictions；  API声明：function getUserRestricted(admin: Want, settingsItem: SettingsForDevice): boolean;  差异内容：admin: Want | 类名：restrictions；  API声明：function getUserRestricted(admin: Want | null, settingsItem: SettingsForDevice): boolean;  差异内容：admin: Want | null | api/@ohos.enterprise.restrictions.d.ts |
