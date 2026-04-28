---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-6003
title: ArkWeb
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > ArkWeb
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:14+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:00a5a27bac888333cbe9c90784192c0f5676f1252cb85c26d85745246b4bacad
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：webview；  API声明：enum WebDestroyMode  差异内容：enum WebDestroyMode | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDestroyMode；  API声明：NORMAL\_MODE = 0  差异内容：NORMAL\_MODE = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDestroyMode；  API声明：FAST\_MODE = 1  差异内容：FAST\_MODE = 1 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：global；  API声明：type OnOverrideErrorPageCallback = (errorPageEvent: OnErrorReceiveEvent) => string;  差异内容：type OnOverrideErrorPageCallback = (errorPageEvent: OnErrorReceiveEvent) => string; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface OnPdfScrollEvent  差异内容：declare interface OnPdfScrollEvent | component/web.d.ts |
| 新增API | NA | 类名：OnPdfScrollEvent；  API声明：url: string;  差异内容：url: string; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface OnPdfLoadEvent  差异内容：declare interface OnPdfLoadEvent | component/web.d.ts |
| 新增API | NA | 类名：OnPdfLoadEvent；  API声明：result: PdfLoadResult;  差异内容：result: PdfLoadResult; | component/web.d.ts |
| 新增API | NA | 类名：OnPdfLoadEvent；  API声明：url: string;  差异内容：url: string; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum WebBypassVsyncCondition  差异内容：declare enum WebBypassVsyncCondition | component/web.d.ts |
| 新增API | NA | 类名：WebBypassVsyncCondition；  API声明：NONE = 0  差异内容：NONE = 0 | component/web.d.ts |
| 新增API | NA | 类名：WebBypassVsyncCondition；  API声明：SCROLLBY\_FROM\_ZERO\_OFFSET = 1  差异内容：SCROLLBY\_FROM\_ZERO\_OFFSET = 1 | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum PdfLoadResult  差异内容：declare enum PdfLoadResult | component/web.d.ts |
| 新增API | NA | 类名：PdfLoadResult；  API声明：LOAD\_SUCCESS = 0  差异内容：LOAD\_SUCCESS = 0 | component/web.d.ts |
| 新增API | NA | 类名：PdfLoadResult；  API声明：PARSE\_ERROR\_FILE = 1  差异内容：PARSE\_ERROR\_FILE = 1 | component/web.d.ts |
| 新增API | NA | 类名：PdfLoadResult；  API声明：PARSE\_ERROR\_FORMAT = 2  差异内容：PARSE\_ERROR\_FORMAT = 2 | component/web.d.ts |
| 新增API | NA | 类名：PdfLoadResult；  API声明：PARSE\_ERROR\_PASSWORD = 3  差异内容：PARSE\_ERROR\_PASSWORD = 3 | component/web.d.ts |
| 新增API | NA | 类名：PdfLoadResult；  API声明：PARSE\_ERROR\_HANDLER = 4  差异内容：PARSE\_ERROR\_HANDLER = 4 | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum GestureFocusMode  差异内容：declare enum GestureFocusMode | component/web.d.ts |
| 新增API | NA | 类名：GestureFocusMode；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | component/web.d.ts |
| 新增API | NA | 类名：GestureFocusMode；  API声明：GESTURE\_TAP\_AND\_LONG\_PRESS = 1  差异内容：GESTURE\_TAP\_AND\_LONG\_PRESS = 1 | component/web.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：getPageOffset(): ScrollOffset;  差异内容：getPageOffset(): ScrollOffset; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：avoidVisibleViewportBottom(avoidHeight: number): void;  差异内容：avoidVisibleViewportBottom(avoidHeight: number): void; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：static enablePrivateNetworkAccess(enable: boolean): void;  差异内容：static enablePrivateNetworkAccess(enable: boolean): void; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：static isPrivateNetworkAccessEnabled(): boolean;  差异内容：static isPrivateNetworkAccessEnabled(): boolean; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：getErrorPageEnabled(): boolean;  差异内容：getErrorPageEnabled(): boolean; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：setErrorPageEnabled(enable: boolean): void;  差异内容：setErrorPageEnabled(enable: boolean): void; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：static setWebDestroyMode(mode: WebDestroyMode): void;  差异内容：static setWebDestroyMode(mode: WebDestroyMode): void; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebAttribute；  API声明：onOverrideErrorPage(callback: OnOverrideErrorPageCallback): WebAttribute;  差异内容：onOverrideErrorPage(callback: OnOverrideErrorPageCallback): WebAttribute; | component/web.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebAttribute；  API声明：onPdfScrollAtBottom(callback: Callback<OnPdfScrollEvent>): WebAttribute;  差异内容：onPdfScrollAtBottom(callback: Callback<OnPdfScrollEvent>): WebAttribute; | component/web.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebAttribute；  API声明：onPdfLoadEvent(callback: Callback<OnPdfLoadEvent>): WebAttribute;  差异内容：onPdfLoadEvent(callback: Callback<OnPdfLoadEvent>): WebAttribute; | component/web.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebAttribute；  API声明：bypassVsyncCondition(condition: WebBypassVsyncCondition): WebAttribute;  差异内容：bypassVsyncCondition(condition: WebBypassVsyncCondition): WebAttribute; | component/web.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebAttribute；  API声明：gestureFocusMode(mode: GestureFocusMode): WebAttribute;  差异内容：gestureFocusMode(mode: GestureFocusMode): WebAttribute; | component/web.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：WebResourceHandler；  API声明：didFail(code: WebNetErrorList): void;  差异内容：didFail(code: WebNetErrorList): void; | 类名：WebResourceHandler；  API声明：didFail(code: WebNetErrorList, completeIfNoResponse: boolean): void;  差异内容：didFail(code: WebNetErrorList, completeIfNoResponse: boolean): void; | api/@ohos.web.webview.d.ts |
