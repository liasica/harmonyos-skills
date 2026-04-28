---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-6101
title: ArkWeb
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > ArkWeb
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:892a2170221b51f57ac298359bd7787d00140e020bdd47e7b1b3910680301598
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：global；  API声明：declare class WebCookie  差异内容：NA | 类名：global；  API声明：declare class WebCookie  差异内容：23 | component/web.d.ts |
| 函数变更 | 类名：WebAttribute；  API声明：enableNativeEmbedMode(mode: boolean): WebAttribute;  差异内容：mode: boolean | 类名：WebAttribute；  API声明：enableNativeEmbedMode(enabled: boolean): WebAttribute;  差异内容：enabled: boolean | component/web.d.ts |
| 函数变更 | 类名：WebviewController；  API声明：registerJavaScriptProxy(object: object, name: string, methodList: Array<string>, asyncMethodList?: Array<string>, permission?: string): void;  差异内容：object: object, name: string, methodList: Array<string>, asyncMethodList?: Array<string>, permission?: string | 类名：WebviewController；  API声明：registerJavaScriptProxy(jsObject: object, name: string, methodList: Array<string>, asyncMethodList?: Array<string>, permission?: string): void;  差异内容：jsObject: object, name: string, methodList: Array<string>, asyncMethodList?: Array<string>, permission?: string | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：global；  API声明：type OnCameraCaptureStateChangeCallback = (event: CameraCaptureStateChangeInfo) => void;  差异内容：type OnCameraCaptureStateChangeCallback = (event: CameraCaptureStateChangeInfo) => void; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：type OnMicrophoneCaptureStateChangeCallback = (event: MicrophoneCaptureStateChangeInfo) => void;  差异内容：type OnMicrophoneCaptureStateChangeCallback = (event: MicrophoneCaptureStateChangeInfo) => void; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum ConsoleMessageSource  差异内容：declare enum ConsoleMessageSource | component/web.d.ts |
| 新增API | NA | 类名：ConsoleMessageSource；  API声明：XML = 0  差异内容：XML = 0 | component/web.d.ts |
| 新增API | NA | 类名：ConsoleMessageSource；  API声明：JAVASCRIPT = 1  差异内容：JAVASCRIPT = 1 | component/web.d.ts |
| 新增API | NA | 类名：ConsoleMessageSource；  API声明：NETWORK = 2  差异内容：NETWORK = 2 | component/web.d.ts |
| 新增API | NA | 类名：ConsoleMessageSource；  API声明：CONSOLE\_API = 3  差异内容：CONSOLE\_API = 3 | component/web.d.ts |
| 新增API | NA | 类名：ConsoleMessageSource；  API声明：STORAGE = 4  差异内容：STORAGE = 4 | component/web.d.ts |
| 新增API | NA | 类名：ConsoleMessageSource；  API声明：RENDERING = 5  差异内容：RENDERING = 5 | component/web.d.ts |
| 新增API | NA | 类名：ConsoleMessageSource；  API声明：SECURITY = 6  差异内容：SECURITY = 6 | component/web.d.ts |
| 新增API | NA | 类名：ConsoleMessageSource；  API声明：OTHER = 7  差异内容：OTHER = 7 | component/web.d.ts |
| 新增API | NA | 类名：ConsoleMessageSource；  API声明：DEPRECATION = 8  差异内容：DEPRECATION = 8 | component/web.d.ts |
| 新增API | NA | 类名：ConsoleMessageSource；  API声明：WORKER = 9  差异内容：WORKER = 9 | component/web.d.ts |
| 新增API | NA | 类名：ConsoleMessageSource；  API声明：VIOLATION = 10  差异内容：VIOLATION = 10 | component/web.d.ts |
| 新增API | NA | 类名：ConsoleMessageSource；  API声明：INTERVENTION = 11  差异内容：INTERVENTION = 11 | component/web.d.ts |
| 新增API | NA | 类名：ConsoleMessageSource；  API声明：RECOMMENDATION = 12  差异内容：RECOMMENDATION = 12 | component/web.d.ts |
| 新增API | NA | 类名：FileSelectorParam；  API声明：getSuggestedName(): string;  差异内容：getSuggestedName(): string; | component/web.d.ts |
| 新增API | NA | 类名：FileSelectorParam；  API声明：getDefaultPath(): string;  差异内容：getDefaultPath(): string; | component/web.d.ts |
| 新增API | NA | 类名：FileSelectorParam；  API声明：getDescriptions(): Array<string>;  差异内容：getDescriptions(): Array<string>; | component/web.d.ts |
| 新增API | NA | 类名：FileSelectorParam；  API声明：isAcceptAllOptionExcluded(): boolean;  差异内容：isAcceptAllOptionExcluded(): boolean; | component/web.d.ts |
| 新增API | NA | 类名：FileSelectorParam；  API声明：getAcceptableFileTypes(): Array<Array<AcceptableFileType>>;  差异内容：getAcceptableFileTypes(): Array<Array<AcceptableFileType>>; | component/web.d.ts |
| 新增API | NA | 类名：WebContextMenuResult；  API声明：requestPasswordAutoFill(): void;  差异内容：requestPasswordAutoFill(): void; | component/web.d.ts |
| 新增API | NA | 类名：ConsoleMessage；  API声明：getSource(): ConsoleMessageSource;  差异内容：getSource(): ConsoleMessageSource; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface UrlRegexRule  差异内容：declare interface UrlRegexRule | component/web.d.ts |
| 新增API | NA | 类名：UrlRegexRule；  API声明：secondLevelDomain: string;  差异内容：secondLevelDomain: string; | component/web.d.ts |
| 新增API | NA | 类名：UrlRegexRule；  API声明：rule: string;  差异内容：rule: string; | component/web.d.ts |
| 新增API | NA | 类名：ScriptItem；  API声明：urlRegexRules?: Array<UrlRegexRule>;  差异内容：urlRegexRules?: Array<UrlRegexRule>; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum NavigationPolicy  差异内容：declare enum NavigationPolicy | component/web.d.ts |
| 新增API | NA | 类名：NavigationPolicy；  API声明：NEW\_POPUP = 0  差异内容：NEW\_POPUP = 0 | component/web.d.ts |
| 新增API | NA | 类名：NavigationPolicy；  API声明：NEW\_WINDOW = 1  差异内容：NEW\_WINDOW = 1 | component/web.d.ts |
| 新增API | NA | 类名：NavigationPolicy；  API声明：NEW\_BACKGROUND\_TAB = 2  差异内容：NEW\_BACKGROUND\_TAB = 2 | component/web.d.ts |
| 新增API | NA | 类名：NavigationPolicy；  API声明：NEW\_FOREGROUND\_TAB = 3  差异内容：NEW\_FOREGROUND\_TAB = 3 | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface WindowFeatures  差异内容：declare interface WindowFeatures | component/web.d.ts |
| 新增API | NA | 类名：WindowFeatures；  API声明：height: number;  差异内容：height: number; | component/web.d.ts |
| 新增API | NA | 类名：WindowFeatures；  API声明：width: number;  差异内容：width: number; | component/web.d.ts |
| 新增API | NA | 类名：WindowFeatures；  API声明：x: number;  差异内容：x: number; | component/web.d.ts |
| 新增API | NA | 类名：WindowFeatures；  API声明：y: number;  差异内容：y: number; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface OnWindowNewExtEvent  差异内容：declare interface OnWindowNewExtEvent | component/web.d.ts |
| 新增API | NA | 类名：OnWindowNewExtEvent；  API声明：isAlert: boolean;  差异内容：isAlert: boolean; | component/web.d.ts |
| 新增API | NA | 类名：OnWindowNewExtEvent；  API声明：isUserTrigger: boolean;  差异内容：isUserTrigger: boolean; | component/web.d.ts |
| 新增API | NA | 类名：OnWindowNewExtEvent；  API声明：targetUrl: string;  差异内容：targetUrl: string; | component/web.d.ts |
| 新增API | NA | 类名：OnWindowNewExtEvent；  API声明：handler: ControllerHandler;  差异内容：handler: ControllerHandler; | component/web.d.ts |
| 新增API | NA | 类名：OnWindowNewExtEvent；  API声明：windowFeatures: WindowFeatures;  差异内容：windowFeatures: WindowFeatures; | component/web.d.ts |
| 新增API | NA | 类名：OnWindowNewExtEvent；  API声明：navigationPolicy: NavigationPolicy;  差异内容：navigationPolicy: NavigationPolicy; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：type TextSelectionChangeCallback = (selectionText: string) => void;  差异内容：type TextSelectionChangeCallback = (selectionText: string) => void; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface FirstScreenPaint  差异内容：declare interface FirstScreenPaint | component/web.d.ts |
| 新增API | NA | 类名：FirstScreenPaint；  API声明：url: string;  差异内容：url: string; | component/web.d.ts |
| 新增API | NA | 类名：FirstScreenPaint；  API声明：navigationStartTime: number;  差异内容：navigationStartTime: number; | component/web.d.ts |
| 新增API | NA | 类名：FirstScreenPaint；  API声明：firstScreenPaintTime: number;  差异内容：firstScreenPaintTime: number; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：type OnFirstScreenPaintCallback = (firstScreenPaint: FirstScreenPaint) => void;  差异内容：type OnFirstScreenPaintCallback = (firstScreenPaint: FirstScreenPaint) => void; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：onWindowNewExt(callback: Callback<OnWindowNewExtEvent>): WebAttribute;  差异内容：onWindowNewExt(callback: Callback<OnWindowNewExtEvent>): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：onFirstScreenPaint(callback: OnFirstScreenPaintCallback): WebAttribute;  差异内容：onFirstScreenPaint(callback: OnFirstScreenPaintCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：enableAutoFill(value: boolean): WebAttribute;  差异内容：enableAutoFill(value: boolean): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：onTextSelectionChange(callback: TextSelectionChangeCallback): WebAttribute;  差异内容：onTextSelectionChange(callback: TextSelectionChangeCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：enableImageAnalyzer(enable: boolean): WebAttribute;  差异内容：enableImageAnalyzer(enable: boolean): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：onCameraCaptureStateChange(callback: OnCameraCaptureStateChangeCallback): WebAttribute;  差异内容：onCameraCaptureStateChange(callback: OnCameraCaptureStateChangeCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：onMicrophoneCaptureStateChange(callback: OnMicrophoneCaptureStateChangeCallback): WebAttribute;  差异内容：onMicrophoneCaptureStateChange(callback: OnMicrophoneCaptureStateChangeCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface AcceptableFileType  差异内容：declare interface AcceptableFileType | component/web.d.ts |
| 新增API | NA | 类名：AcceptableFileType；  API声明：mimeType: string;  差异内容：mimeType: string; | component/web.d.ts |
| 新增API | NA | 类名：AcceptableFileType；  API声明：acceptableType: Array<string>;  差异内容：acceptableType: Array<string>; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface CameraCaptureStateChangeInfo  差异内容：declare interface CameraCaptureStateChangeInfo | component/web.d.ts |
| 新增API | NA | 类名：CameraCaptureStateChangeInfo；  API声明：originalState: CameraCaptureState;  差异内容：originalState: CameraCaptureState; | component/web.d.ts |
| 新增API | NA | 类名：CameraCaptureStateChangeInfo；  API声明：newState: CameraCaptureState;  差异内容：newState: CameraCaptureState; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum CameraCaptureState  差异内容：declare enum CameraCaptureState | component/web.d.ts |
| 新增API | NA | 类名：CameraCaptureState；  API声明：NONE = 0  差异内容：NONE = 0 | component/web.d.ts |
| 新增API | NA | 类名：CameraCaptureState；  API声明：PAUSED = 1  差异内容：PAUSED = 1 | component/web.d.ts |
| 新增API | NA | 类名：CameraCaptureState；  API声明：ACTIVE = 2  差异内容：ACTIVE = 2 | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface MicrophoneCaptureStateChangeInfo  差异内容：declare interface MicrophoneCaptureStateChangeInfo | component/web.d.ts |
| 新增API | NA | 类名：MicrophoneCaptureStateChangeInfo；  API声明：originalState: MicrophoneCaptureState;  差异内容：originalState: MicrophoneCaptureState; | component/web.d.ts |
| 新增API | NA | 类名：MicrophoneCaptureStateChangeInfo；  API声明：newState: MicrophoneCaptureState;  差异内容：newState: MicrophoneCaptureState; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum MicrophoneCaptureState  差异内容：declare enum MicrophoneCaptureState | component/web.d.ts |
| 新增API | NA | 类名：MicrophoneCaptureState；  API声明：NONE = 0  差异内容：NONE = 0 | component/web.d.ts |
| 新增API | NA | 类名：MicrophoneCaptureState；  API声明：PAUSED = 1  差异内容：PAUSED = 1 | component/web.d.ts |
| 新增API | NA | 类名：MicrophoneCaptureState；  API声明：ACTIVE = 2  差异内容：ACTIVE = 2 | component/web.d.ts |
| 新增API | NA | 类名：ArkWebEngineVersion；  API声明：ARKWEB\_EVERGREEN = 99999  差异内容：ARKWEB\_EVERGREEN = 99999 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCookieManager；  API声明：static fetchAllCookies(incognito: boolean): Promise<Array<WebHttpCookie>>;  差异内容：static fetchAllCookies(incognito: boolean): Promise<Array<WebHttpCookie>>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebBlanklessErrorCode；  API声明：ERR\_DURATION\_OUT\_OF\_RANGE = -6  差异内容：ERR\_DURATION\_OUT\_OF\_RANGE = -6 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebBlanklessErrorCode；  API声明：ERR\_EXPIRATION\_TIME\_OUT\_OF\_RANGE = -7  差异内容：ERR\_EXPIRATION\_TIME\_OUT\_OF\_RANGE = -7 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明：enum BlanklessFrameInterpolationState  差异内容：enum BlanklessFrameInterpolationState | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BlanklessFrameInterpolationState；  API声明：FRAME\_INTERPOLATION\_SUCCEEDED = 0  差异内容：FRAME\_INTERPOLATION\_SUCCEEDED = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BlanklessFrameInterpolationState；  API声明：FRAME\_INTERPOLATION\_FAILED = 1  差异内容：FRAME\_INTERPOLATION\_FAILED = 1 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BlanklessFrameInterpolationState；  API声明：FRAME\_INTERPOLATION\_REMOVED = 2  差异内容：FRAME\_INTERPOLATION\_REMOVED = 2 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明：interface BlanklessFrameInterpolationInfo  差异内容：interface BlanklessFrameInterpolationInfo | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BlanklessFrameInterpolationInfo；  API声明：key: string;  差异内容：key: string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BlanklessFrameInterpolationInfo；  API声明：state: BlanklessFrameInterpolationState;  差异内容：state: BlanklessFrameInterpolationState; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BlanklessFrameInterpolationInfo；  API声明：timestamp: number;  差异内容：timestamp: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BlanklessFrameInterpolationInfo；  API声明：reason: string;  差异内容：reason: string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明：interface BlanklessLoadingParam  差异内容：interface BlanklessLoadingParam | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BlanklessLoadingParam；  API声明：enable: boolean;  差异内容：enable: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BlanklessLoadingParam；  API声明：duration?: number;  差异内容：duration?: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BlanklessLoadingParam；  API声明：expirationTime?: number;  差异内容：expirationTime?: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BlanklessLoadingParam；  API声明：callback?: Callback<BlanklessFrameInterpolationInfo>;  差异内容：callback?: Callback<BlanklessFrameInterpolationInfo>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController；  API声明：static isActiveWebEngineEvergreen(): boolean;  差异内容：static isActiveWebEngineEvergreen(): boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController；  API声明：setBlanklessLoadingWithParams(key: string, param: BlanklessLoadingParam): WebBlanklessErrorCode;  差异内容：setBlanklessLoadingWithParams(key: string, param: BlanklessLoadingParam): WebBlanklessErrorCode; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController；  API声明：static setScrollbarMode(scrollbarMode: ScrollbarMode): void;  差异内容：static setScrollbarMode(scrollbarMode: ScrollbarMode): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController；  API声明：resumeMicrophone(): void;  差异内容：resumeMicrophone(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController；  API声明：pauseMicrophone(): void;  差异内容：pauseMicrophone(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController；  API声明：stopMicrophone(): void;  差异内容：stopMicrophone(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明：enum ScrollbarMode  差异内容：enum ScrollbarMode | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ScrollbarMode；  API声明：OVERLAY\_LAYOUT\_SCROLLBAR = 0  差异内容：OVERLAY\_LAYOUT\_SCROLLBAR = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ScrollbarMode；  API声明：FORCE\_DISPLAY\_SCROLLBAR = 1  差异内容：FORCE\_DISPLAY\_SCROLLBAR = 1 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明：enum WebHttpCookieSameSitePolicy  差异内容：enum WebHttpCookieSameSitePolicy | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebHttpCookieSameSitePolicy；  API声明：NONE = 0  差异内容：NONE = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebHttpCookieSameSitePolicy；  API声明：LAX = 1  差异内容：LAX = 1 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebHttpCookieSameSitePolicy；  API声明：STRICT = 2  差异内容：STRICT = 2 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明：interface WebHttpCookie  差异内容：interface WebHttpCookie | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebHttpCookie；  API声明：samesitePolicy: WebHttpCookieSameSitePolicy;  差异内容：samesitePolicy: WebHttpCookieSameSitePolicy; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebHttpCookie；  API声明：expiresDate: string;  差异内容：expiresDate: string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebHttpCookie；  API声明：name: string;  差异内容：name: string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebHttpCookie；  API声明：isSessionCookie: boolean;  差异内容：isSessionCookie: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebHttpCookie；  API声明：value: string;  差异内容：value: string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebHttpCookie；  API声明：path: string;  差异内容：path: string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebHttpCookie；  API声明：isHttpOnly: boolean;  差异内容：isHttpOnly: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebHttpCookie；  API声明：isSecure: boolean;  差异内容：isSecure: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebHttpCookie；  API声明：domain: string;  差异内容：domain: string; | api/@ohos.web.webview.d.ts |
| 新增kit | 类名：global；  API声明：component\web.d.ts  差异内容：NA | 类名：global；  API声明：component\web.d.ts  差异内容：ArkWeb | component/web.d.ts |
