---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-6012
title: ArkWeb
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Release引入的API > ArkWeb
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:52+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:034113af4fe81e7bb0b64f1526453f3fdf8863110540a144921a53dd23267369
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：ThreatType；  API声明：THREAT\_NONE = 4  差异内容：THREAT\_NONE = 4 | component/web.d.ts |
| 新增API | NA | 类名：ThreatType；  API声明：THREAT\_UNPROCESSED = 5  差异内容：THREAT\_UNPROCESSED = 5 | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：onSafeBrowsingCheckFinish(callback: OnSafeBrowsingCheckResultCallback): WebAttribute;  差异内容：onSafeBrowsingCheckFinish(callback: OnSafeBrowsingCheckResultCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：webview；  API声明：class PrefetchOptions  差异内容：class PrefetchOptions | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：PrefetchOptions；  API声明：minTimeBetweenPrefetchesMs: number;  差异内容：minTimeBetweenPrefetchesMs: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：PrefetchOptions；  API声明：ignoreCacheControlNoStore: boolean;  差异内容：ignoreCacheControlNoStore: boolean; | api/@ohos.web.webview.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：WebviewController；  API声明：prefetchPage(url: string, additionalHeaders?: Array<WebHeader>): void;  差异内容：prefetchPage(url: string, additionalHeaders?: Array<WebHeader>): void; | 类名：WebviewController；  API声明：prefetchPage(url: string, additionalHeaders?: Array<WebHeader>, prefetchOptions?: PrefetchOptions): void;  差异内容：prefetchPage(url: string, additionalHeaders?: Array<WebHeader>, prefetchOptions?: PrefetchOptions): void; | api/@ohos.web.webview.d.ts |
