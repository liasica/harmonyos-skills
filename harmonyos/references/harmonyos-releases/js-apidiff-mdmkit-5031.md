---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-5031
title: MDM Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta1引入的API > MDM Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:41+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:1ddf61198745f1786c71c61a701edfbb88953e0d01e43ecb259cd4dc92ed6294
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：restrictions；  API声明：function setDisallowedPolicy(admin: Want, feature: string, disallow: boolean): void;  差异内容：ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS | 类名：restrictions；  API声明：function setDisallowedPolicy(admin: Want, feature: string, disallow: boolean): void;  差异内容：ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS | api/@ohos.enterprise.restrictions.d.ts |
| 权限变更 | 类名：restrictions；  API声明：function getDisallowedPolicy(admin: Want, feature: string): boolean;  差异内容：ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS | 类名：restrictions；  API声明：function getDisallowedPolicy(admin: Want, feature: string): boolean;  差异内容：ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：adminManager；  API声明： export enum AdminType  差异内容： export enum AdminType | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：AdminType；  API声明：ADMIN\_TYPE\_BYOD = 0x02  差异内容：ADMIN\_TYPE\_BYOD = 0x02 | api/@ohos.enterprise.adminManager.d.ts |
| 新增API | NA | 类名：adminManager；  API声明：function startAdminProvision(admin: Want, type: AdminType, context: common.Context, parameters: Record<string, string>): void;  差异内容：function startAdminProvision(admin: Want, type: AdminType, context: common.Context, parameters: Record<string, string>): void; | api/@ohos.enterprise.adminManager.d.ts |
