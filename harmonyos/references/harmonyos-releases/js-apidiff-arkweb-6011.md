---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-6011
title: ArkWeb
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Beta1引入的API > ArkWeb
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:56+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:6668f627af62816dcff034cacbb89c3f739f44d3044544e76843ea715c4dc879
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：WebviewController；  API声明：static setUserAgentForHosts(userAgent: string, hosts: Array<string>): void;  差异内容：401 | 类名：WebviewController；  API声明：static setUserAgentForHosts(userAgent: string, hosts: Array<string>): void;  差异内容：NA | api/@ohos.web.webview.d.ts |
| API废弃版本变更 | 类名：global；  API声明：declare enum HitTestType  差异内容：NA | 类名：global；  API声明：declare enum HitTestType  差异内容：21 | component/web.d.ts |
| API废弃版本变更 | 类名：HitTestType；  API声明：EditText = 0  差异内容：NA | 类名：HitTestType；  API声明：EditText = 0  差异内容：21 | component/web.d.ts |
| API废弃版本变更 | 类名：HitTestType；  API声明：Email = 1  差异内容：NA | 类名：HitTestType；  API声明：Email = 1  差异内容：21 | component/web.d.ts |
| API废弃版本变更 | 类名：HitTestType；  API声明：HttpAnchor = 2  差异内容：NA | 类名：HitTestType；  API声明：HttpAnchor = 2  差异内容：21 | component/web.d.ts |
| API废弃版本变更 | 类名：HitTestType；  API声明：HttpAnchorImg = 3  差异内容：NA | 类名：HitTestType；  API声明：HttpAnchorImg = 3  差异内容：21 | component/web.d.ts |
| API废弃版本变更 | 类名：HitTestType；  API声明：Img = 4  差异内容：NA | 类名：HitTestType；  API声明：Img = 4  差异内容：21 | component/web.d.ts |
| API废弃版本变更 | 类名：HitTestType；  API声明：Map = 5  差异内容：NA | 类名：HitTestType；  API声明：Map = 5  差异内容：21 | component/web.d.ts |
| API废弃版本变更 | 类名：HitTestType；  API声明：Phone = 6  差异内容：NA | 类名：HitTestType；  API声明：Phone = 6  差异内容：21 | component/web.d.ts |
| API废弃版本变更 | 类名：HitTestType；  API声明：Unknown = 7  差异内容：NA | 类名：HitTestType；  API声明：Unknown = 7  差异内容：21 | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：type OnNativeEmbedObjectParamChangeCallback = (event: NativeEmbedParamDataInfo) => void;  差异内容：type OnNativeEmbedObjectParamChangeCallback = (event: NativeEmbedParamDataInfo) => void; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum NativeEmbedParamStatus  差异内容：declare enum NativeEmbedParamStatus | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedParamStatus；  API声明：ADD = 0  差异内容：ADD = 0 | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedParamStatus；  API声明：UPDATE = 1  差异内容：UPDATE = 1 | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedParamStatus；  API声明：DELETE = 2  差异内容：DELETE = 2 | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface NativeEmbedParamItem  差异内容：declare interface NativeEmbedParamItem | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedParamItem；  API声明：status: NativeEmbedParamStatus;  差异内容：status: NativeEmbedParamStatus; | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedParamItem；  API声明：id: string;  差异内容：id: string; | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedParamItem；  API声明：name?: string;  差异内容：name?: string; | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedParamItem；  API声明：value?: string;  差异内容：value?: string; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface NativeEmbedParamDataInfo  差异内容：declare interface NativeEmbedParamDataInfo | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedParamDataInfo；  API声明：embedId: string;  差异内容：embedId: string; | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedParamDataInfo；  API声明：objectAttributeId?: string;  差异内容：objectAttributeId?: string; | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedParamDataInfo；  API声明：paramItems?: Array<NativeEmbedParamItem>;  差异内容：paramItems?: Array<NativeEmbedParamItem>; | component/web.d.ts |
| 新增API | NA | 类名：WebElementType；  API声明：TEXT = 3  差异内容：TEXT = 3 | component/web.d.ts |
| 新增API | NA | 类名：WebResponseType；  API声明：RIGHT\_CLICK = 2  差异内容：RIGHT\_CLICK = 2 | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface ConnectionInfo  差异内容：export interface ConnectionInfo | api/@ohos.web.WebNativeMessagingExtensionAbility.d.ts |
| 新增API | NA | 类名：ConnectionInfo；  API声明：connectionId: number;  差异内容：connectionId: number; | api/@ohos.web.WebNativeMessagingExtensionAbility.d.ts |
| 新增API | NA | 类名：ConnectionInfo；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@ohos.web.WebNativeMessagingExtensionAbility.d.ts |
| 新增API | NA | 类名：ConnectionInfo；  API声明：extensionOrigin: string;  差异内容：extensionOrigin: string; | api/@ohos.web.WebNativeMessagingExtensionAbility.d.ts |
| 新增API | NA | 类名：ConnectionInfo；  API声明：fdRead: number;  差异内容：fdRead: number; | api/@ohos.web.WebNativeMessagingExtensionAbility.d.ts |
| 新增API | NA | 类名：ConnectionInfo；  API声明：fdWrite: number;  差异内容：fdWrite: number; | api/@ohos.web.WebNativeMessagingExtensionAbility.d.ts |
| 新增API | NA | 类名：global；  API声明：export default class WebNativeMessagingExtensionAbility  差异内容：export default class WebNativeMessagingExtensionAbility | api/@ohos.web.WebNativeMessagingExtensionAbility.d.ts |
| 新增API | NA | 类名：WebNativeMessagingExtensionAbility；  API声明：context: WebNativeMessagingExtensionContext;  差异内容：context: WebNativeMessagingExtensionContext; | api/@ohos.web.WebNativeMessagingExtensionAbility.d.ts |
| 新增API | NA | 类名：WebNativeMessagingExtensionAbility；  API声明：onConnectNative(info: ConnectionInfo): void;  差异内容：onConnectNative(info: ConnectionInfo): void; | api/@ohos.web.WebNativeMessagingExtensionAbility.d.ts |
| 新增API | NA | 类名：WebNativeMessagingExtensionAbility；  API声明：onDisconnectNative(info: ConnectionInfo): void;  差异内容：onDisconnectNative(info: ConnectionInfo): void; | api/@ohos.web.WebNativeMessagingExtensionAbility.d.ts |
| 新增API | NA | 类名：WebNativeMessagingExtensionAbility；  API声明：onDestroy(): void;  差异内容：onDestroy(): void; | api/@ohos.web.WebNativeMessagingExtensionAbility.d.ts |
| 新增API | NA | 类名：global；  API声明：export default class WebNativeMessagingExtensionContext  差异内容：export default class WebNativeMessagingExtensionContext | api/@ohos.web.WebNativeMessagingExtensionContext.d.ts |
| 新增API | NA | 类名：WebNativeMessagingExtensionContext；  API声明：startAbility(want: Want, options?: StartOptions): Promise<void>;  差异内容：startAbility(want: Want, options?: StartOptions): Promise<void>; | api/@ohos.web.WebNativeMessagingExtensionContext.d.ts |
| 新增API | NA | 类名：WebNativeMessagingExtensionContext；  API声明：terminateSelf(): Promise<void>;  差异内容：terminateSelf(): Promise<void>; | api/@ohos.web.WebNativeMessagingExtensionContext.d.ts |
| 新增API | NA | 类名：WebNativeMessagingExtensionContext；  API声明：stopNativeConnection(connectionId: number): Promise<void>;  差异内容：stopNativeConnection(connectionId: number): Promise<void>; | api/@ohos.web.WebNativeMessagingExtensionContext.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace webNativeMessagingExtensionManager  差异内容：declare namespace webNativeMessagingExtensionManager | api/@ohos.web.webNativeMessagingExtensionManager.d.ts |
| 新增API | NA | 类名：webNativeMessagingExtensionManager；  API声明：interface ConnectionNativeInfo  差异内容：interface ConnectionNativeInfo | api/@ohos.web.webNativeMessagingExtensionManager.d.ts |
| 新增API | NA | 类名：ConnectionNativeInfo；  API声明：connectionId: number;  差异内容：connectionId: number; | api/@ohos.web.webNativeMessagingExtensionManager.d.ts |
| 新增API | NA | 类名：ConnectionNativeInfo；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@ohos.web.webNativeMessagingExtensionManager.d.ts |
| 新增API | NA | 类名：ConnectionNativeInfo；  API声明：extensionOrigin: string;  差异内容：extensionOrigin: string; | api/@ohos.web.webNativeMessagingExtensionManager.d.ts |
| 新增API | NA | 类名：ConnectionNativeInfo；  API声明：extensionPid: number;  差异内容：extensionPid: number; | api/@ohos.web.webNativeMessagingExtensionManager.d.ts |
| 新增API | NA | 类名：webNativeMessagingExtensionManager；  API声明：export enum NmErrorCode  差异内容：export enum NmErrorCode | api/@ohos.web.webNativeMessagingExtensionManager.d.ts |
| 新增API | NA | 类名：NmErrorCode；  API声明：PERMISSION\_DENY = 17100203  差异内容：PERMISSION\_DENY = 17100203 | api/@ohos.web.webNativeMessagingExtensionManager.d.ts |
| 新增API | NA | 类名：NmErrorCode；  API声明：WANT\_CONTENT\_ERROR = 17100202  差异内容：WANT\_CONTENT\_ERROR = 17100202 | api/@ohos.web.webNativeMessagingExtensionManager.d.ts |
| 新增API | NA | 类名：NmErrorCode；  API声明：INNER\_ERROR = 17100201  差异内容：INNER\_ERROR = 17100201 | api/@ohos.web.webNativeMessagingExtensionManager.d.ts |
| 新增API | NA | 类名：webNativeMessagingExtensionManager；  API声明：interface WebExtensionConnectionCallback  差异内容：interface WebExtensionConnectionCallback | api/@ohos.web.webNativeMessagingExtensionManager.d.ts |
| 新增API | NA | 类名：WebExtensionConnectionCallback；  API声明：onConnect(connection: ConnectionNativeInfo): void;  差异内容：onConnect(connection: ConnectionNativeInfo): void; | api/@ohos.web.webNativeMessagingExtensionManager.d.ts |
| 新增API | NA | 类名：WebExtensionConnectionCallback；  API声明：onDisconnect(connection: ConnectionNativeInfo): void;  差异内容：onDisconnect(connection: ConnectionNativeInfo): void; | api/@ohos.web.webNativeMessagingExtensionManager.d.ts |
| 新增API | NA | 类名：WebExtensionConnectionCallback；  API声明：onFailed(code: NmErrorCode, errMsg: string): void;  差异内容：onFailed(code: NmErrorCode, errMsg: string): void; | api/@ohos.web.webNativeMessagingExtensionManager.d.ts |
| 新增API | NA | 类名：webNativeMessagingExtensionManager；  API声明：function connectNative(context: UIAbilityContext, want: Want, callback: WebExtensionConnectionCallback): number;  差异内容：function connectNative(context: UIAbilityContext, want: Want, callback: WebExtensionConnectionCallback): number; | api/@ohos.web.webNativeMessagingExtensionManager.d.ts |
| 新增API | NA | 类名：webNativeMessagingExtensionManager；  API声明：function disconnectNative(connectionId: number): Promise<void>;  差异内容：function disconnectNative(connectionId: number): Promise<void>; | api/@ohos.web.webNativeMessagingExtensionManager.d.ts |
| 新增API | NA | 类名：webview；  API声明：enum SiteIsolationMode  差异内容：enum SiteIsolationMode | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SiteIsolationMode；  API声明：PARTIAL = 0  差异内容：PARTIAL = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SiteIsolationMode；  API声明：STRICT = 1  差异内容：STRICT = 1 | api/@ohos.web.webview.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.web.WebNativeMessagingExtensionAbility.d.ts  差异内容：ArkWeb | api/@ohos.web.WebNativeMessagingExtensionAbility.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.web.WebNativeMessagingExtensionContext.d.ts  差异内容：ArkWeb | api/@ohos.web.WebNativeMessagingExtensionContext.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.web.webNativeMessagingExtensionManager.d.ts  差异内容：ArkWeb | api/@ohos.web.webNativeMessagingExtensionManager.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：static setAutoPreconnect(enabled: boolean): void;  差异内容：static setAutoPreconnect(enabled: boolean): void; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：static isAutoPreconnectEnabled(): boolean;  差异内容：static isAutoPreconnectEnabled(): boolean; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：static setSocketIdleTimeout(timeout: number): void;  差异内容：static setSocketIdleTimeout(timeout: number): void; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：static setSiteIsolationMode(mode: SiteIsolationMode): void;  差异内容：static setSiteIsolationMode(mode: SiteIsolationMode): void; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：static getSiteIsolationMode(): SiteIsolationMode;  差异内容：static getSiteIsolationMode(): SiteIsolationMode; | api/@ohos.web.webview.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：WebviewController；  API声明：static customizeSchemes(schemes: Array<WebCustomScheme>): void;  差异内容：static customizeSchemes(schemes: Array<WebCustomScheme>): void; | 类名：WebviewController；  API声明：static customizeSchemes(schemes: Array<WebCustomScheme>, lazyInitWebEngine: boolean): void;  差异内容：static customizeSchemes(schemes: Array<WebCustomScheme>, lazyInitWebEngine: boolean): void; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebAttribute；  API声明：onNativeEmbedObjectParamChange(callback: OnNativeEmbedObjectParamChangeCallback): WebAttribute;  差异内容：onNativeEmbedObjectParamChange(callback: OnNativeEmbedObjectParamChangeCallback): WebAttribute; | component/web.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebAttribute；  API声明：forceEnableZoom(enable: boolean): WebAttribute;  差异内容：forceEnableZoom(enable: boolean): WebAttribute; | component/web.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：SelectionMenuOptionsExt；  API声明：onMenuShow?: Callback<void>;  差异内容：onMenuShow?: Callback<void>; | component/web.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：SelectionMenuOptionsExt；  API声明：onMenuHide?: Callback<void>;  差异内容：onMenuHide?: Callback<void>; | component/web.d.ts |
