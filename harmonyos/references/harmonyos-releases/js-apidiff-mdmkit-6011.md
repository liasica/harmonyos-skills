---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-6011
title: MDM Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Beta1引入的API > MDM Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:59+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:4625fe97a5d06ea0c5ed4a26adedee56dbb1bb1bf0ea62b1e4b01f93ce5471ac
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：applicationManager；  API声明：function addDisallowedRunningBundlesSync(admin: Want, appIds: Array<string>, accountId?: number): void;  差异内容：NA | 类名：applicationManager；  API声明：function addDisallowedRunningBundlesSync(admin: Want, appIds: Array<string>, accountId?: number): void;  差异内容：9200010 | api/@ohos.enterprise.applicationManager.d.ts |
| 新增错误码 | 类名：restrictions；  API声明：function setDisallowedPolicy(admin: Want, feature: string, disallow: boolean): void;  差异内容：NA | 类名：restrictions；  API声明：function setDisallowedPolicy(admin: Want, feature: string, disallow: boolean): void;  差异内容：9200013 | api/@ohos.enterprise.restrictions.d.ts |
| 函数变更 | 类名：restrictions；  API声明：function getDisallowedPolicy(admin: Want, feature: string): boolean;  差异内容：admin: Want | 类名：restrictions；  API声明：function getDisallowedPolicy(admin: Want | null, feature: string): boolean;  差异内容：admin: Want | null | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function addAllowedRunningBundles(admin: Want, appIdentifiers: Array<string>, accountId: number): void;  差异内容：function addAllowedRunningBundles(admin: Want, appIdentifiers: Array<string>, accountId: number): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function removeAllowedRunningBundles(admin: Want, appIdentifiers: Array<string>, accountId: number): void;  差异内容：function removeAllowedRunningBundles(admin: Want, appIdentifiers: Array<string>, accountId: number): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager；  API声明：function getAllowedRunningBundles(admin: Want, accountId: number): Array<string>;  差异内容：function getAllowedRunningBundles(admin: Want, accountId: number): Array<string>; | api/@ohos.enterprise.applicationManager.d.ts |
