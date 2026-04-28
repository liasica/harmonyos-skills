---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-6001
title: ArkWeb
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > ArkWeb
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:35+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d16497d50a232d6ee42ca8a6192c9cff70b350bc5d56ad2dca0478521d9538de
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：WebAttribute；  API声明：selectionMenuOptions(expandedMenuOptions: Array<ExpandedMenuItemOptions>): WebAttribute;  差异内容：NA | 类名：WebAttribute；  API声明：selectionMenuOptions(expandedMenuOptions: Array<ExpandedMenuItemOptions>): WebAttribute;  差异内容：20 | component/web.d.ts |
| API废弃版本变更 | 类名：global；  API声明：declare interface ExpandedMenuItemOptions  差异内容：NA | 类名：global；  API声明：declare interface ExpandedMenuItemOptions  差异内容：20 | component/web.d.ts |
| API废弃版本变更 | 类名：ExpandedMenuItemOptions；  API声明：content: ResourceStr;  差异内容：NA | 类名：ExpandedMenuItemOptions；  API声明：content: ResourceStr;  差异内容：20 | component/web.d.ts |
| API废弃版本变更 | 类名：ExpandedMenuItemOptions；  API声明：startIcon?: ResourceStr;  差异内容：NA | 类名：ExpandedMenuItemOptions；  API声明：startIcon?: ResourceStr;  差异内容：20 | component/web.d.ts |
| API废弃版本变更 | 类名：ExpandedMenuItemOptions；  API声明：action: (selectedText: {  plainText: string;  }) => void;  差异内容：NA | 类名：ExpandedMenuItemOptions；  API声明：action: (selectedText: {  plainText: string;  }) => void;  差异内容：20 | component/web.d.ts |
| 新增API | NA | 类名：webview；  API声明：enum ControllerAttachState  差异内容：enum ControllerAttachState | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ControllerAttachState；  API声明：UNATTACHED = 0  差异内容：UNATTACHED = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ControllerAttachState；  API声明：ATTACHED = 1  差异内容：ATTACHED = 1 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface OnLoadStartedEvent  差异内容：declare interface OnLoadStartedEvent | component/web.d.ts |
| 新增API | NA | 类名：OnLoadStartedEvent；  API声明：url: string;  差异内容：url: string; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface OnLoadFinishedEvent  差异内容：declare interface OnLoadFinishedEvent | component/web.d.ts |
| 新增API | NA | 类名：OnLoadFinishedEvent；  API声明：url: string;  差异内容：url: string; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface PreviewMenuOptions  差异内容：declare interface PreviewMenuOptions | component/web.d.ts |
| 新增API | NA | 类名：PreviewMenuOptions；  API声明：hapticFeedbackMode?: HapticFeedbackMode;  差异内容：hapticFeedbackMode?: HapticFeedbackMode; | component/web.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：getAttachState(): ControllerAttachState;  差异内容：getAttachState(): ControllerAttachState; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：on(type: 'controllerAttachStateChange', callback: Callback<ControllerAttachState>): void;  差异内容：on(type: 'controllerAttachStateChange', callback: Callback<ControllerAttachState>): void; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：off(type: 'controllerAttachStateChange', callback?: Callback<ControllerAttachState>): void;  差异内容：off(type: 'controllerAttachStateChange', callback?: Callback<ControllerAttachState>): void; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：waitForAttached(timeout: number): Promise<ControllerAttachState>;  差异内容：waitForAttached(timeout: number): Promise<ControllerAttachState>; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：static setAppCustomUserAgent(userAgent: string): void;  差异内容：static setAppCustomUserAgent(userAgent: string): void; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：static setUserAgentForHosts(userAgent: string, hosts: Array<string>): void;  差异内容：static setUserAgentForHosts(userAgent: string, hosts: Array<string>): void; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebContextMenuResult；  API声明：redo(): void;  差异内容：redo(): void; | component/web.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebContextMenuResult；  API声明：undo(): void;  差异内容：undo(): void; | component/web.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebContextMenuResult；  API声明：pasteAndMatchStyle(): void;  差异内容：pasteAndMatchStyle(): void; | component/web.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebAttribute；  API声明：onLoadStarted(callback: Callback<OnLoadStartedEvent>): WebAttribute;  差异内容：onLoadStarted(callback: Callback<OnLoadStartedEvent>): WebAttribute; | component/web.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebAttribute；  API声明：onLoadFinished(callback: Callback<OnLoadFinishedEvent>): WebAttribute;  差异内容：onLoadFinished(callback: Callback<OnLoadFinishedEvent>): WebAttribute; | component/web.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebAttribute；  API声明：enableDataDetector(enable: boolean): WebAttribute;  差异内容：enableDataDetector(enable: boolean): WebAttribute; | component/web.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebAttribute；  API声明：dataDetectorConfig(config: TextDataDetectorConfig): WebAttribute;  差异内容：dataDetectorConfig(config: TextDataDetectorConfig): WebAttribute; | component/web.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebAttribute；  API声明：onActivateContent(callback: Callback<void>): WebAttribute;  差异内容：onActivateContent(callback: Callback<void>): WebAttribute; | component/web.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：WebviewController；  API声明：static setWebDebuggingAccess(webDebuggingAccess: boolean): void;  差异内容：static setWebDebuggingAccess(webDebuggingAccess: boolean): void; | 类名：WebviewController；  API声明：static setWebDebuggingAccess(webDebuggingAccess: boolean, port: number): void;  差异内容：static setWebDebuggingAccess(webDebuggingAccess: boolean, port: number): void; | api/@ohos.web.webview.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：OnBeforeUnloadEvent；  API声明：isReload?: boolean;  差异内容：isReload?: boolean; | component/web.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：SelectionMenuOptionsExt；  API声明：previewMenuOptions?: PreviewMenuOptions;  差异内容：previewMenuOptions?: PreviewMenuOptions; | component/web.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EmbedOptions；  API声明：supportCssDisplayChange?: boolean;  差异内容：supportCssDisplayChange?: boolean; | component/web.d.ts |
