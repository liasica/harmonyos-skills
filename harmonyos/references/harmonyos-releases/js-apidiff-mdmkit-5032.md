---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-5032
title: MDM Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta2引入的API > MDM Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:38+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:5964d3c0cef4aec2c559c9ba6a0c0b9a2bd442e975784a7c473b1a694dded37c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：browser；  API声明：function setManagedBrowserPolicy(admin: Want, bundleName: string, policyName: string, policyValue: string): void;  差异内容：function setManagedBrowserPolicy(admin: Want, bundleName: string, policyName: string, policyValue: string): void; | api/@ohos.enterprise.browser.d.ts |
| 新增API | NA | 类名：browser；  API声明：function getManagedBrowserPolicy(admin: Want, bundleName: string): ArrayBuffer;  差异内容：function getManagedBrowserPolicy(admin: Want, bundleName: string): ArrayBuffer; | api/@ohos.enterprise.browser.d.ts |
| 新增API | NA | 类名：browser；  API声明：function getSelfManagedBrowserPolicyVersion(): string;  差异内容：function getSelfManagedBrowserPolicyVersion(): string; | api/@ohos.enterprise.browser.d.ts |
| 新增API | NA | 类名：browser；  API声明：function getSelfManagedBrowserPolicy(): ArrayBuffer;  差异内容：function getSelfManagedBrowserPolicy(): ArrayBuffer; | api/@ohos.enterprise.browser.d.ts |
| 新增API | NA | 类名：Direction；  API声明：FORWARD = 2  差异内容：FORWARD = 2 | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：Action；  API声明：REJECT = 2  差异内容：REJECT = 2 | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：DomainFilterRule；  API声明：direction?: Direction;  差异内容：direction?: Direction; | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：networkManager；  API声明：function setGlobalProxyForAccount(admin: Want, httpProxy: connection.HttpProxy, accountId: number): void;  差异内容：function setGlobalProxyForAccount(admin: Want, httpProxy: connection.HttpProxy, accountId: number): void; | api/@ohos.enterprise.networkManager.d.ts |
| 新增API | NA | 类名：networkManager；  API声明：function getGlobalProxyForAccount(admin: Want, accountId: number): connection.HttpProxy;  差异内容：function getGlobalProxyForAccount(admin: Want, accountId: number): connection.HttpProxy; | api/@ohos.enterprise.networkManager.d.ts |
