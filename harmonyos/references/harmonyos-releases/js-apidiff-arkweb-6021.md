---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-6021
title: ArkWeb
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > ArkWeb
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:42+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:eeb0aaec73080a6f72c12433b9ab6faac2e6e9d30f348cfef685a7a72de830b8
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：WebviewController；  API声明：static prefetchResource(request: RequestInfo, additionalHeaders?: Array<WebHeader>, cacheKey?: string, cacheValidTime?: number): void;  差异内容：401 | 类名：WebviewController；  API声明：static prefetchResource(request: RequestInfo, additionalHeaders?: Array<WebHeader>, cacheKey?: string, cacheValidTime?: number): void;  差异内容：NA | api/@ohos.web.webview.d.ts |
| 删除错误码 | 类名：WebviewController；  API声明：injectOfflineResources(resourceMaps: Array<OfflineResourceMap>): void;  差异内容：401 | 类名：WebviewController；  API声明：injectOfflineResources(resourceMaps: Array<OfflineResourceMap>): void;  差异内容：NA | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCookieManager；  API声明：static setLazyInitializeWebEngine(lazy: boolean): void;  差异内容：static setLazyInitializeWebEngine(lazy: boolean): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：JsMessageExt；  API声明：getErrorDescription(): string | null;  差异内容：getErrorDescription(): string | null; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明：enum WebSoftKeyboardBehaviorMode  差异内容：enum WebSoftKeyboardBehaviorMode | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSoftKeyboardBehaviorMode；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSoftKeyboardBehaviorMode；  API声明：DISABLE\_AUTO\_KEYBOARD\_ON\_ACTIVE = 1  差异内容：DISABLE\_AUTO\_KEYBOARD\_ON\_ACTIVE = 1 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController；  API声明：setSoftKeyboardBehaviorMode(mode: WebSoftKeyboardBehaviorMode): void;  差异内容：setSoftKeyboardBehaviorMode(mode: WebSoftKeyboardBehaviorMode): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：global；  API声明：type OnVerifyPinCallback = (verifyPinEvent: VerifyPinEvent) => void;  差异内容：type OnVerifyPinCallback = (verifyPinEvent: VerifyPinEvent) => void; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum WebRotateEffect  差异内容：declare enum WebRotateEffect | component/web.d.ts |
| 新增API | NA | 类名：WebRotateEffect；  API声明：TOPLEFT\_EFFECT = 0  差异内容：TOPLEFT\_EFFECT = 0 | component/web.d.ts |
| 新增API | NA | 类名：WebRotateEffect；  API声明：RESIZE\_COVER\_EFFECT = 1  差异内容：RESIZE\_COVER\_EFFECT = 1 | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class VerifyPinHandler  差异内容：declare class VerifyPinHandler | component/web.d.ts |
| 新增API | NA | 类名：VerifyPinHandler；  API声明：confirm(result: PinVerifyResult): void;  差异内容：confirm(result: PinVerifyResult): void; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum ContextMenuDataMediaType  差异内容：declare enum ContextMenuDataMediaType | component/web.d.ts |
| 新增API | NA | 类名：ContextMenuDataMediaType；  API声明：NONE = 0  差异内容：NONE = 0 | component/web.d.ts |
| 新增API | NA | 类名：ContextMenuDataMediaType；  API声明：IMAGE = 1  差异内容：IMAGE = 1 | component/web.d.ts |
| 新增API | NA | 类名：ContextMenuDataMediaType；  API声明：VIDEO = 2  差异内容：VIDEO = 2 | component/web.d.ts |
| 新增API | NA | 类名：ContextMenuDataMediaType；  API声明：AUDIO = 3  差异内容：AUDIO = 3 | component/web.d.ts |
| 新增API | NA | 类名：ContextMenuDataMediaType；  API声明：CANVAS = 4  差异内容：CANVAS = 4 | component/web.d.ts |
| 新增API | NA | 类名：WebContextMenuParam；  API声明：getContextMenuMediaType(): ContextMenuDataMediaType;  差异内容：getContextMenuMediaType(): ContextMenuDataMediaType; | component/web.d.ts |
| 新增API | NA | 类名：WebOptions；  API声明：emulateTouchFromMouseEvent?: boolean;  差异内容：emulateTouchFromMouseEvent?: boolean; | component/web.d.ts |
| 新增API | NA | 类名：OnRefreshAccessedHistoryEvent；  API声明：isMainFrame?: boolean;  差异内容：isMainFrame?: boolean; | component/web.d.ts |
| 新增API | NA | 类名：WebKeyboardAvoidMode；  API声明：RETURN\_TO\_UICONTEXT = 3  差异内容：RETURN\_TO\_UICONTEXT = 3 | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface BlankScreenDetails  差异内容：declare interface BlankScreenDetails | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenDetails；  API声明：detectedContentfulNodesCount?: number;  差异内容：detectedContentfulNodesCount?: number; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum DetectedBlankScreenReason  差异内容：declare enum DetectedBlankScreenReason | component/web.d.ts |
| 新增API | NA | 类名：DetectedBlankScreenReason；  API声明：NO\_CONTENTFUL\_NODES = 0  差异内容：NO\_CONTENTFUL\_NODES = 0 | component/web.d.ts |
| 新增API | NA | 类名：DetectedBlankScreenReason；  API声明：SUB\_THRESHOLD\_CONTENTFUL\_NODES = 1  差异内容：SUB\_THRESHOLD\_CONTENTFUL\_NODES = 1 | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface BlankScreenDetectionEventInfo  差异内容：declare interface BlankScreenDetectionEventInfo | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenDetectionEventInfo；  API声明：url: string;  差异内容：url: string; | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenDetectionEventInfo；  API声明：blankScreenReason: DetectedBlankScreenReason;  差异内容：blankScreenReason: DetectedBlankScreenReason; | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenDetectionEventInfo；  API声明：blankScreenDetails?: BlankScreenDetails;  差异内容：blankScreenDetails?: BlankScreenDetails; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：type OnDetectBlankScreenCallback = (event: BlankScreenDetectionEventInfo) => void;  差异内容：type OnDetectBlankScreenCallback = (event: BlankScreenDetectionEventInfo) => void; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum BlankScreenDetectionMethod  差异内容：declare enum BlankScreenDetectionMethod | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenDetectionMethod；  API声明：DETECTION\_CONTENTFUL\_NODES\_SEVENTEEN = 0  差异内容：DETECTION\_CONTENTFUL\_NODES\_SEVENTEEN = 0 | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface BlankScreenDetectionConfig  差异内容：declare interface BlankScreenDetectionConfig | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenDetectionConfig；  API声明：enable: boolean;  差异内容：enable: boolean; | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenDetectionConfig；  API声明：detectionTiming?: number[];  差异内容：detectionTiming?: number[]; | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenDetectionConfig；  API声明：detectionMethods?: BlankScreenDetectionMethod[];  差异内容：detectionMethods?: BlankScreenDetectionMethod[]; | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenDetectionConfig；  API声明：contentfulNodesCountThreshold?: number;  差异内容：contentfulNodesCountThreshold?: number; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：rotateRenderEffect(effect: WebRotateEffect): WebAttribute;  差异内容：rotateRenderEffect(effect: WebRotateEffect): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：onVerifyPin(callback: OnVerifyPinCallback): WebAttribute;  差异内容：onVerifyPin(callback: OnVerifyPinCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：zoomControlAccess(zoomControlAccess: boolean): WebAttribute;  差异内容：zoomControlAccess(zoomControlAccess: boolean): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：backToTop(backToTop: boolean): WebAttribute;  差异内容：backToTop(backToTop: boolean): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：onDetectedBlankScreen(callback: OnDetectBlankScreenCallback): WebAttribute;  差异内容：onDetectedBlankScreen(callback: OnDetectBlankScreenCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：blankScreenDetectionConfig(detectConfig: BlankScreenDetectionConfig): WebAttribute;  差异内容：blankScreenDetectionConfig(detectConfig: BlankScreenDetectionConfig): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：enableSelectedDataDetector(enable: boolean): WebAttribute;  差异内容：enableSelectedDataDetector(enable: boolean): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface VerifyPinEvent  差异内容：declare interface VerifyPinEvent | component/web.d.ts |
| 新增API | NA | 类名：VerifyPinEvent；  API声明：handler: VerifyPinHandler;  差异内容：handler: VerifyPinHandler; | component/web.d.ts |
| 新增API | NA | 类名：VerifyPinEvent；  API声明：identity: string;  差异内容：identity: string; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum PinVerifyResult  差异内容：declare enum PinVerifyResult | component/web.d.ts |
| 新增API | NA | 类名：PinVerifyResult；  API声明：PIN\_VERIFICATION\_SUCCESS = 0  差异内容：PIN\_VERIFICATION\_SUCCESS = 0 | component/web.d.ts |
| 新增API | NA | 类名：PinVerifyResult；  API声明：PIN\_VERIFICATION\_FAILED = 1  差异内容：PIN\_VERIFICATION\_FAILED = 1 | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum CredentialType  差异内容：declare enum CredentialType | component/web.d.ts |
| 新增API | NA | 类名：CredentialType；  API声明：CREDENTIAL\_USER = 2  差异内容：CREDENTIAL\_USER = 2 | component/web.d.ts |
| 新增API | NA | 类名：CredentialType；  API声明：CREDENTIAL\_APP = 3  差异内容：CREDENTIAL\_APP = 3 | component/web.d.ts |
| 新增API | NA | 类名：CredentialType；  API声明：CREDENTIAL\_UKEY = 4  差异内容：CREDENTIAL\_UKEY = 4 | component/web.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：ClientAuthenticationHandler；  API声明：confirm(authUri: string): void;  差异内容：confirm(authUri: string): void; | 类名：ClientAuthenticationHandler；  API声明：confirm(identity: string, credentialTypeOrCertChainFile: CredentialType | string): void;  差异内容：confirm(identity: string, credentialTypeOrCertChainFile: CredentialType | string): void; | component/web.d.ts |
