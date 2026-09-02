---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-7003
title: ArkWeb
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Release引入的API > ArkWeb
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3396b0d7949e17752ba6b5b590e52690f7e5d7d24c8cb7c4c3caff997f5d5d9f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：WebviewController；  API声明：getSubframeErrorPageEnabled(): boolean;  差异内容：getSubframeErrorPageEnabled(): boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：enableMediaNetworkProxy(enabled: boolean): WebAttribute;  差异内容：enableMediaNetworkProxy(enabled: boolean): WebAttribute; | component/web.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：WebCookieManager；  API声明：static fetchCookieSync(url: string, incognito?: boolean): string;  差异内容：static fetchCookieSync(url: string, incognito?: boolean): string; | 类名：WebCookieManager；  API声明：static fetchCookieSync(url: string, incognito?: boolean, includePartitionedCookies?: boolean): string;  差异内容：static fetchCookieSync(url: string, incognito?: boolean, includePartitionedCookies?: boolean): string; | api/@ohos.web.webview.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：WebviewController；  API声明：setErrorPageEnabled(enable: boolean): void;  差异内容：setErrorPageEnabled(enable: boolean): void; | 类名：WebviewController；  API声明：setErrorPageEnabled(enable: boolean, includeSubframe: boolean): void;  差异内容：setErrorPageEnabled(enable: boolean, includeSubframe: boolean): void; | api/@ohos.web.webview.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围不是包含关系 | 类名：WebCookieManager；  API声明：static fetchCookie(url: string, callback: AsyncCallback<string>): void;  差异内容：static fetchCookie(url: string, callback: AsyncCallback<string>): void; | 类名：WebCookieManager；  API声明：static fetchCookie(url: string, incognito: boolean, includePartitionedCookies: boolean): Promise<string>;  差异内容：static fetchCookie(url: string, incognito: boolean, includePartitionedCookies: boolean): Promise<string>; | api/@ohos.web.webview.d.ts |
