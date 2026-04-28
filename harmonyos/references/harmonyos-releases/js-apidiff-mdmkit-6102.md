---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-6102
title: MDM Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta2引入的变更 > MDM Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3801d2a4d3e12a79a8880ad708121141c83a0f0975d697bdf38560fbb5967e51
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：restrictions；  API声明：function setDisallowedPolicy(admin: Want, feature: string, disallow: boolean): void;  差异内容：ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS | 类名：restrictions；  API声明：function setDisallowedPolicy(admin: Want, feature: string, disallow: boolean): void;  差异内容：ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS or ohos.permission.ENTERPRISE\_MANAGE\_NETWORK | api/@ohos.enterprise.restrictions.d.ts |
| 权限变更 | 类名：restrictions；  API声明：function getDisallowedPolicy(admin: Want | null, feature: string): boolean;  差异内容：ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS | 类名：restrictions；  API声明：function getDisallowedPolicy(admin: Want | null, feature: string): boolean;  差异内容：ohos.permission.ENTERPRISE\_MANAGE\_RESTRICTIONS or ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS or ohos.permission.ENTERPRISE\_MANAGE\_NETWORK | api/@ohos.enterprise.restrictions.d.ts |
| 删除API | 类名：securityManager；  API声明：function installEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, fd: number, accountId: number): void;  差异内容：function installEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, fd: number, accountId: number): void; | NA | api/@ohos.enterprise.securityManager.d.ts |
| 删除API | 类名：securityManager；  API声明：function uninstallEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, accountId: number): void;  差异内容：function uninstallEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, accountId: number): void; | NA | api/@ohos.enterprise.securityManager.d.ts |
