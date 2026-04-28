---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-b035
title: ArkWeb
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta3引入的API > ArkWeb
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:29+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a3f14328573b90960bf1937ddde2f6deafa3c1393475204ca7ae1d6058791f78
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：WebviewController；  API声明：registerJavaScriptProxy(object: object, name: string, methodList: Array<string>, asyncMethodList?: Array<string>): void;  差异内容：NA | 类名：WebviewController；  API声明：registerJavaScriptProxy(object: object, name: string, methodList: Array<string>, asyncMethodList?: Array<string>, permission?: string): void;  差异内容：permission?: string | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController；  API声明：static enableBackForwardCache(features: BackForwardCacheSupportedFeatures): void;  差异内容：static enableBackForwardCache(features: BackForwardCacheSupportedFeatures): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController；  API声明：setBackForwardCacheOptions(options: BackForwardCacheOptions): void;  差异内容：setBackForwardCacheOptions(options: BackForwardCacheOptions): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明： class BackForwardCacheSupportedFeatures  差异内容： class BackForwardCacheSupportedFeatures | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BackForwardCacheSupportedFeatures；  API声明：nativeEmbed: boolean;  差异内容：nativeEmbed: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BackForwardCacheSupportedFeatures；  API声明：mediaTakeOver: boolean;  差异内容：mediaTakeOver: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明： class BackForwardCacheOptions  差异内容： class BackForwardCacheOptions | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BackForwardCacheOptions；  API声明：size: number;  差异内容：size: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BackForwardCacheOptions；  API声明：timeToLive: number;  差异内容：timeToLive: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebOptions；  API声明：sharedRenderProcessToken?: string;  差异内容：sharedRenderProcessToken?: string; | component/web.d.ts |
| 新增API | NA | 类名：JavaScriptProxy；  API声明：permission?: string;  差异内容：permission?: string; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum WebKeyboardAvoidMode  差异内容： declare enum WebKeyboardAvoidMode | component/web.d.ts |
| 新增API | NA | 类名：WebKeyboardAvoidMode；  API声明：RESIZE\_VISUAL = 0  差异内容：RESIZE\_VISUAL = 0 | component/web.d.ts |
| 新增API | NA | 类名：WebKeyboardAvoidMode；  API声明：RESIZE\_CONTENT = 1  差异内容：RESIZE\_CONTENT = 1 | component/web.d.ts |
| 新增API | NA | 类名：WebKeyboardAvoidMode；  API声明：OVERLAYS\_CONTENT = 2  差异内容：OVERLAYS\_CONTENT = 2 | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：keyboardAvoidMode(mode: WebKeyboardAvoidMode): WebAttribute;  差异内容：keyboardAvoidMode(mode: WebKeyboardAvoidMode): WebAttribute; | component/web.d.ts |
| 删除API | 类名：WebviewController；  API声明：static enableBackForwardCache(features: BackForwardCacheSupportedFeatures): void;  差异内容：static enableBackForwardCache(features: BackForwardCacheSupportedFeatures): void; | NA | api/@ohos.web.webview.d.ts |
| 删除API | 类名：WebviewController；  API声明：setBackForwardCacheOptions(options: BackForwardCacheOptions): void;  差异内容：setBackForwardCacheOptions(options: BackForwardCacheOptions): void; | NA | api/@ohos.web.webview.d.ts |
| 删除API | 类名：webview；  API声明： class BackForwardCacheSupportedFeatures  差异内容： class BackForwardCacheSupportedFeatures | NA | api/@ohos.web.webview.d.ts |
| 删除API | 类名：BackForwardCacheSupportedFeatures；  API声明：nativeEmbed: boolean;  差异内容：nativeEmbed: boolean; | NA | api/@ohos.web.webview.d.ts |
| 删除API | 类名：BackForwardCacheSupportedFeatures；  API声明：mediaTakeOver: boolean;  差异内容：mediaTakeOver: boolean; | NA | api/@ohos.web.webview.d.ts |
| 删除API | 类名：webview；  API声明： class BackForwardCacheOptions  差异内容： class BackForwardCacheOptions | NA | api/@ohos.web.webview.d.ts |
| 删除API | 类名：BackForwardCacheOptions；  API声明：size: number;  差异内容：size: number; | NA | api/@ohos.web.webview.d.ts |
| 删除API | 类名：BackForwardCacheOptions；  API声明：timeToLive: number;  差异内容：timeToLive: number; | NA | api/@ohos.web.webview.d.ts |
| 删除API | 类名：WebAttribute；  API声明：forceDisplayScrollBar(enabled: boolean): WebAttribute;  差异内容：forceDisplayScrollBar(enabled: boolean): WebAttribute; | NA | component/web.d.ts |
