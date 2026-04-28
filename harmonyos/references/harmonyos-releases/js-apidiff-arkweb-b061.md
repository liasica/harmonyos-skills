---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-b061
title: ArkWeb
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta6引入的API > ArkWeb
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:23+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:fe2dd51b04aa21f84ebe7b1e7936b73e1bc7b46ec1805cfd72488e9e4591c88f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：WebviewController；  API声明：static enableBackForwardCache(features: BackForwardCacheSupportedFeatures): void;  差异内容：static enableBackForwardCache(features: BackForwardCacheSupportedFeatures): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController；  API声明：setBackForwardCacheOptions(options: BackForwardCacheOptions): void;  差异内容：setBackForwardCacheOptions(options: BackForwardCacheOptions): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明： enum SuspendType  差异内容： enum SuspendType | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SuspendType；  API声明：ENTER\_BACK\_FORWARD\_CACHE = 0  差异内容：ENTER\_BACK\_FORWARD\_CACHE = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SuspendType；  API声明：ENTER\_BACKGROUND  差异内容：ENTER\_BACKGROUND | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SuspendType；  API声明：AUTO\_CLEANUP  差异内容：AUTO\_CLEANUP | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerBridge；  API声明：resumePlayer?(): void;  差异内容：resumePlayer?(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerBridge；  API声明：suspendPlayer?(type: SuspendType): void;  差异内容：suspendPlayer?(type: SuspendType): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明： class BackForwardCacheSupportedFeatures  差异内容： class BackForwardCacheSupportedFeatures | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BackForwardCacheSupportedFeatures；  API声明：nativeEmbed: boolean;  差异内容：nativeEmbed: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BackForwardCacheSupportedFeatures；  API声明：mediaTakeOver: boolean;  差异内容：mediaTakeOver: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明： class BackForwardCacheOptions  差异内容： class BackForwardCacheOptions | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BackForwardCacheOptions；  API声明：size: number;  差异内容：size: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BackForwardCacheOptions；  API声明：timeToLive: number;  差异内容：timeToLive: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeEmbedStatus；  API声明：ENTER\_BFCACHE = 3  差异内容：ENTER\_BFCACHE = 3 | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedStatus；  API声明：LEAVE\_BFCACHE = 4  差异内容：LEAVE\_BFCACHE = 4 | component/web.d.ts |
