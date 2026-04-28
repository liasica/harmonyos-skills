---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-6002
title: ArkWeb
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > ArkWeb
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:25+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:eb50c689084756233e2e9ea33b0fd95f713397fb2b6c32adde94554b53a7751a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：webview；  API声明：enum WebBlanklessErrorCode  差异内容：enum WebBlanklessErrorCode | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebBlanklessErrorCode；  API声明：SUCCESS = 0  差异内容：SUCCESS = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebBlanklessErrorCode；  API声明：ERR\_UNKNOWN = -1  差异内容：ERR\_UNKNOWN = -1 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebBlanklessErrorCode；  API声明：ERR\_INVALID\_PARAM = -2  差异内容：ERR\_INVALID\_PARAM = -2 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebBlanklessErrorCode；  API声明：ERR\_CONTROLLER\_NOT\_INITED = -3  差异内容：ERR\_CONTROLLER\_NOT\_INITED = -3 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebBlanklessErrorCode；  API声明：ERR\_KEY\_NOT\_MATCH = -4  差异内容：ERR\_KEY\_NOT\_MATCH = -4 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebBlanklessErrorCode；  API声明：ERR\_SIGNIFICANT\_CHANGE = -5  差异内容：ERR\_SIGNIFICANT\_CHANGE = -5 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明：interface BlanklessInfo  差异内容：interface BlanklessInfo | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BlanklessInfo；  API声明：errCode: WebBlanklessErrorCode;  差异内容：errCode: WebBlanklessErrorCode; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BlanklessInfo；  API声明：similarity: number;  差异内容：similarity: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BlanklessInfo；  API声明：loadingTime: number;  差异内容：loadingTime: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：global；  API声明：type MouseInfoCallback = (event: NativeEmbedMouseInfo) => void;  差异内容：type MouseInfoCallback = (event: NativeEmbedMouseInfo) => void; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface NativeEmbedMouseInfo  差异内容：declare interface NativeEmbedMouseInfo | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedMouseInfo；  API声明：embedId?: string;  差异内容：embedId?: string; | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedMouseInfo；  API声明：mouseEvent?: MouseEvent;  差异内容：mouseEvent?: MouseEvent; | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedMouseInfo；  API声明：result?: EventResult;  差异内容：result?: EventResult; | component/web.d.ts |
| 新增API | NA | 类名：WebElementType；  API声明：LINK = 2  差异内容：LINK = 2 | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum AudioSessionType  差异内容：declare enum AudioSessionType | component/web.d.ts |
| 新增API | NA | 类名：AudioSessionType；  API声明：AMBIENT = 3  差异内容：AMBIENT = 3 | component/web.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：getBlanklessInfoWithKey(key: string): BlanklessInfo;  差异内容：getBlanklessInfoWithKey(key: string): BlanklessInfo; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：setBlanklessLoadingWithKey(key: string, is\_start: boolean): WebBlanklessErrorCode;  差异内容：setBlanklessLoadingWithKey(key: string, is\_start: boolean): WebBlanklessErrorCode; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：static clearBlanklessLoadingCache(keys?: Array<string>): void;  差异内容：static clearBlanklessLoadingCache(keys?: Array<string>): void; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：static setBlanklessLoadingCacheCapacity(capacity: number): number;  差异内容：static setBlanklessLoadingCacheCapacity(capacity: number): number; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：getProgress(): number;  差异内容：getProgress(): number; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：EventResult；  API声明：setMouseEventResult(result: boolean, stopPropagation?: boolean): void;  差异内容：setMouseEventResult(result: boolean, stopPropagation?: boolean): void; | component/web.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebAttribute；  API声明：onNativeEmbedMouseEvent(callback: MouseInfoCallback): WebAttribute;  差异内容：onNativeEmbedMouseEvent(callback: MouseInfoCallback): WebAttribute; | component/web.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：SslErrorHandler；  API声明：handleCancel(): void;  差异内容：handleCancel(): void; | 类名：SslErrorHandler；  API声明：handleCancel(abortLoading: boolean): void;  差异内容：handleCancel(abortLoading: boolean): void; | component/web.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：WebMediaOptions；  API声明：audioSessionType?: AudioSessionType;  差异内容：audioSessionType?: AudioSessionType; | component/web.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：OnTitleReceiveEvent；  API声明：isRealTitle?: boolean;  差异内容：isRealTitle?: boolean; | component/web.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：SslErrorEvent；  API声明：certChainData?: Array<Uint8Array>;  差异内容：certChainData?: Array<Uint8Array>; | component/web.d.ts |
