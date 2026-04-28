---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-5032
title: ArkWeb
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta2引入的API > ArkWeb
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:33+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d6da07cc5e13b2a807f34e2f02585b36cf72fb9c697f73a38708a26277567f76
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：webview；  API声明： enum ProxySchemeFilter  差异内容： enum ProxySchemeFilter | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ProxySchemeFilter；  API声明：MATCH\_ALL\_SCHEMES = 0  差异内容：MATCH\_ALL\_SCHEMES = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ProxySchemeFilter；  API声明：MATCH\_HTTP = 1  差异内容：MATCH\_HTTP = 1 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ProxySchemeFilter；  API声明：MATCH\_HTTPS = 2  差异内容：MATCH\_HTTPS = 2 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明： class ProxyConfig  差异内容： class ProxyConfig | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ProxyConfig；  API声明：insertBypassRule(bypassRule: string): void;  差异内容：insertBypassRule(bypassRule: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ProxyConfig；  API声明：insertDirectRule(schemeFilter?: ProxySchemeFilter): void;  差异内容：insertDirectRule(schemeFilter?: ProxySchemeFilter): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ProxyConfig；  API声明：insertProxyRule(proxyRule: string, schemeFilter?: ProxySchemeFilter): void;  差异内容：insertProxyRule(proxyRule: string, schemeFilter?: ProxySchemeFilter): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ProxyConfig；  API声明：bypassHostnamesWithoutPeriod(): void;  差异内容：bypassHostnamesWithoutPeriod(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ProxyConfig；  API声明：clearImplicitRules(): void;  差异内容：clearImplicitRules(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ProxyConfig；  API声明：enableReverseBypass(reverse: boolean): void;  差异内容：enableReverseBypass(reverse: boolean): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ProxyConfig；  API声明：getBypassRules(): Array<string>;  差异内容：getBypassRules(): Array<string>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ProxyConfig；  API声明：getProxyRules(): Array<ProxyRule>;  差异内容：getProxyRules(): Array<ProxyRule>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ProxyConfig；  API声明：isReverseBypassEnabled(): boolean;  差异内容：isReverseBypassEnabled(): boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明： class ProxyRule  差异内容： class ProxyRule | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ProxyRule；  API声明：getSchemeFilter(): ProxySchemeFilter;  差异内容：getSchemeFilter(): ProxySchemeFilter; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ProxyRule；  API声明：getUrl(): string;  差异内容：getUrl(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明：type OnProxyConfigChangeCallback = () => void;  差异内容：type OnProxyConfigChangeCallback = () => void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明： class ProxyController  差异内容： class ProxyController | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ProxyController；  API声明：static applyProxyOverride(proxyConfig: ProxyConfig, callback: OnProxyConfigChangeCallback): void;  差异内容：static applyProxyOverride(proxyConfig: ProxyConfig, callback: OnProxyConfigChangeCallback): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ProxyController；  API声明：static removeProxyOverride(callback: OnProxyConfigChangeCallback): void;  差异内容：static removeProxyOverride(callback: OnProxyConfigChangeCallback): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：OnSslErrorEventReceiveEvent；  API声明：certChainData?: Array<Uint8Array>;  差异内容：certChainData?: Array<Uint8Array>; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：optimizeParserBudget(optimizeParserBudget: boolean): WebAttribute;  差异内容：optimizeParserBudget(optimizeParserBudget: boolean): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：runJavaScriptOnDocumentStart(scripts: Array<ScriptItem>): WebAttribute;  差异内容：runJavaScriptOnDocumentStart(scripts: Array<ScriptItem>): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：runJavaScriptOnDocumentEnd(scripts: Array<ScriptItem>): WebAttribute;  差异内容：runJavaScriptOnDocumentEnd(scripts: Array<ScriptItem>): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：runJavaScriptOnHeadEnd(scripts: Array<ScriptItem>): WebAttribute;  差异内容：runJavaScriptOnHeadEnd(scripts: Array<ScriptItem>): WebAttribute; | component/web.d.ts |
