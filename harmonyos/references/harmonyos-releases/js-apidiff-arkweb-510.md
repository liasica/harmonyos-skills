---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-510
title: ArkWeb
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > ArkWeb
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:03+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:de0e1ea946247d17931c903f2f35f0eeafc79b68c1ffe27d6a4eda843e05e21f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：WebviewController；  API声明：getHitTest(): WebHitTestType;  差异内容：NA | 类名：WebviewController；  API声明：getHitTest(): WebHitTestType;  差异内容：18 | api/@ohos.web.webview.d.ts |
| API废弃版本变更 | 类名：WebviewController；  API声明：getHitTestValue(): HitTestValue;  差异内容：NA | 类名：WebviewController；  API声明：getHitTestValue(): HitTestValue;  差异内容：18 | api/@ohos.web.webview.d.ts |
| 新增错误码 | 类名：WebviewController；  API声明：static clearIntelligentTrackingPreventionBypassingList(): void;  差异内容：NA | 类名：WebviewController；  API声明：static clearIntelligentTrackingPreventionBypassingList(): void;  差异内容：801 | api/@ohos.web.webview.d.ts |
| 新增错误码 | 类名：WebviewController；  API声明：isAdsBlockEnabled(): boolean;  差异内容：NA | 类名：WebviewController；  API声明：isAdsBlockEnabled(): boolean;  差异内容：801 | api/@ohos.web.webview.d.ts |
| 新增错误码 | 类名：WebviewController；  API声明：isAdsBlockEnabledForCurPage(): boolean;  差异内容：NA | 类名：WebviewController；  API声明：isAdsBlockEnabledForCurPage(): boolean;  差异内容：801 | api/@ohos.web.webview.d.ts |
| 新增错误码 | 类名：AdsBlockManager；  API声明：static clearAdsBlockDisallowedList(): void;  差异内容：NA | 类名：AdsBlockManager；  API声明：static clearAdsBlockDisallowedList(): void;  差异内容：801 | api/@ohos.web.webview.d.ts |
| 新增错误码 | 类名：AdsBlockManager；  API声明：static clearAdsBlockAllowedList(): void;  差异内容：NA | 类名：AdsBlockManager；  API声明：static clearAdsBlockAllowedList(): void;  差异内容：801 | api/@ohos.web.webview.d.ts |
| 新增错误码 | 类名：WebviewController；  API声明：enableIntelligentTrackingPrevention(enable: boolean): void;  差异内容：NA | 类名：WebviewController；  API声明：enableIntelligentTrackingPrevention(enable: boolean): void;  差异内容：801 | api/@ohos.web.webview.d.ts |
| 新增错误码 | 类名：WebviewController；  API声明：isIntelligentTrackingPreventionEnabled(): boolean;  差异内容：NA | 类名：WebviewController；  API声明：isIntelligentTrackingPreventionEnabled(): boolean;  差异内容：801 | api/@ohos.web.webview.d.ts |
| 新增错误码 | 类名：WebviewController；  API声明：static addIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void;  差异内容：NA | 类名：WebviewController；  API声明：static addIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void;  差异内容：801 | api/@ohos.web.webview.d.ts |
| 新增错误码 | 类名：WebviewController；  API声明：static removeIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void;  差异内容：NA | 类名：WebviewController；  API声明：static removeIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void;  差异内容：801 | api/@ohos.web.webview.d.ts |
| 新增错误码 | 类名：WebviewController；  API声明：enableAdsBlock(enable: boolean): void;  差异内容：NA | 类名：WebviewController；  API声明：enableAdsBlock(enable: boolean): void;  差异内容：801 | api/@ohos.web.webview.d.ts |
| 新增错误码 | 类名：AdsBlockManager；  API声明：static setAdsBlockRules(rulesFile: string, replace: boolean): void;  差异内容：NA | 类名：AdsBlockManager；  API声明：static setAdsBlockRules(rulesFile: string, replace: boolean): void;  差异内容：801 | api/@ohos.web.webview.d.ts |
| 新增错误码 | 类名：AdsBlockManager；  API声明：static addAdsBlockDisallowedList(domainSuffixes: Array<string>): void;  差异内容：NA | 类名：AdsBlockManager；  API声明：static addAdsBlockDisallowedList(domainSuffixes: Array<string>): void;  差异内容：801 | api/@ohos.web.webview.d.ts |
| 新增错误码 | 类名：AdsBlockManager；  API声明：static addAdsBlockAllowedList(domainSuffixes: Array<string>): void;  差异内容：NA | 类名：AdsBlockManager；  API声明：static addAdsBlockAllowedList(domainSuffixes: Array<string>): void;  差异内容：801 | api/@ohos.web.webview.d.ts |
| 新增错误码 | 类名：AdsBlockManager；  API声明：static removeAdsBlockDisallowedList(domainSuffixes: Array<string>): void;  差异内容：NA | 类名：AdsBlockManager；  API声明：static removeAdsBlockDisallowedList(domainSuffixes: Array<string>): void;  差异内容：801 | api/@ohos.web.webview.d.ts |
| 新增错误码 | 类名：AdsBlockManager；  API声明：static removeAdsBlockAllowedList(domainSuffixes: Array<string>): void;  差异内容：NA | 类名：AdsBlockManager；  API声明：static removeAdsBlockAllowedList(domainSuffixes: Array<string>): void;  差异内容：801 | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：static removeAllCache(clearRom: boolean): void;  差异内容：static removeAllCache(clearRom: boolean): void; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：getLastHitTest(): HitTestValue;  差异内容：getLastHitTest(): HitTestValue; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：FileSelectorParam；  API声明：getMimeTypes(): Array<string>;  差异内容：getMimeTypes(): Array<string>; | component/web.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebAttribute；  API声明：enableFollowSystemFontWeight(follow: boolean): WebAttribute;  差异内容：enableFollowSystemFontWeight(follow: boolean): WebAttribute; | component/web.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebAttribute；  API声明：enableWebAVSession(enabled: boolean): WebAttribute;  差异内容：enableWebAVSession(enabled: boolean): WebAttribute; | component/web.d.ts |
