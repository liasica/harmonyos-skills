---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-b065
title: ArkUI
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > ArkUI
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:15+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:7a8505de3bd1298b56286666539a8fd98559c89b0a170578235505cedbc42dc9
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API卡片权限变更 | 类名：global；  API声明： declare class ScrollableCommonMethod  差异内容：NA | 类名：global；  API声明： declare class ScrollableCommonMethod  差异内容：form | component/common.d.ts |
| API卡片权限变更 | 类名：ScrollableCommonMethod；  API声明：onDidScroll(handler: OnScrollCallback): T;  差异内容：NA | 类名：ScrollableCommonMethod；  API声明：onDidScroll(handler: OnScrollCallback): T;  差异内容：form | component/common.d.ts |
| API卡片权限变更 | 类名：global；  API声明：declare type OnScrollCallback = (scrollOffset: number, scrollState: ScrollState) => void;  差异内容：NA | 类名：global；  API声明：declare type OnScrollCallback = (scrollOffset: number, scrollState: ScrollState) => void;  差异内容：form | component/common.d.ts |
| API废弃版本变更 | 类名：ScrollableCommonMethod；  API声明：onScroll(event: (scrollOffset: number, scrollState: ScrollState) => void): T;  差异内容：NA | 类名：ScrollableCommonMethod；  API声明：onScroll(event: (scrollOffset: number, scrollState: ScrollState) => void): T;  差异内容：12 | component/common.d.ts |
| 错误码变更 | 类名：componentSnapshot；  API声明：function createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>, delay?: number, checkImageStatus?: boolean, options?: SnapshotOptions): void;  差异内容：100001,401 | 类名：componentSnapshot；  API声明：function createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>, delay?: number, checkImageStatus?: boolean, options?: SnapshotOptions): void;  差异内容：100001,160001,401 | api/@ohos.arkui.componentSnapshot.d.ts |
| 错误码变更 | 类名：componentSnapshot；  API声明：function createFromBuilder(builder: CustomBuilder, delay?: number, checkImageStatus?: boolean, options?: SnapshotOptions): Promise<image.PixelMap>;  差异内容：100001,401 | 类名：componentSnapshot；  API声明：function createFromBuilder(builder: CustomBuilder, delay?: number, checkImageStatus?: boolean, options?: SnapshotOptions): Promise<image.PixelMap>;  差异内容：100001,160001,401 | api/@ohos.arkui.componentSnapshot.d.ts |
| 错误码变更 | 类名：ComponentSnapshot；  API声明：createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>, delay?: number, checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): void;  差异内容：100001,401 | 类名：ComponentSnapshot；  API声明：createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>, delay?: number, checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): void;  差异内容：100001,160001,401 | api/@ohos.arkui.UIContext.d.ts |
| 错误码变更 | 类名：ComponentSnapshot；  API声明：createFromBuilder(builder: CustomBuilder, delay?: number, checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>;  差异内容：100001,401 | 类名：ComponentSnapshot；  API声明：createFromBuilder(builder: CustomBuilder, delay?: number, checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>;  差异内容：100001,160001,401 | api/@ohos.arkui.UIContext.d.ts |
| 函数变更 | 类名：Component3DAttribute；  API声明：environment(uri: Resource): Component3DAttribute;  差异内容：uri: Resource | 类名：Component3DAttribute；  API声明：environment(uri: ResourceStr): Component3DAttribute;  差异内容：uri: ResourceStr | component/component3d.d.ts |
| 函数变更 | 类名：Component3DAttribute；  API声明：customRender(uri: Resource, selfRenderUpdate: boolean): Component3DAttribute;  差异内容：uri: Resource | 类名：Component3DAttribute；  API声明：customRender(uri: ResourceStr, selfRenderUpdate: boolean): Component3DAttribute;  差异内容：uri: ResourceStr | component/component3d.d.ts |
| 函数变更 | 类名：Component3DAttribute；  API声明：shader(uri: Resource): Component3DAttribute;  差异内容：uri: Resource | 类名：Component3DAttribute；  API声明：shader(uri: ResourceStr): Component3DAttribute;  差异内容：uri: ResourceStr | component/component3d.d.ts |
| 函数变更 | 类名：Component3DAttribute；  API声明：shaderImageTexture(uri: Resource): Component3DAttribute;  差异内容：uri: Resource | 类名：Component3DAttribute；  API声明：shaderImageTexture(uri: ResourceStr): Component3DAttribute;  差异内容：uri: ResourceStr | component/component3d.d.ts |
| 属性变更 | 类名：SceneOptions；  API声明：scene?: Resource | Scene;  差异内容：Resource,Scene | 类名：SceneOptions；  API声明：scene?: ResourceStr | Scene;  差异内容：ResourceStr,Scene | component/component3d.d.ts |
| 属性变更 | 类名：ContextMenuOptions；  API声明：borderRadius?: Length | BorderRadiuses;  差异内容：Length,BorderRadiuses | 类名：ContextMenuOptions；  API声明：borderRadius?: Length | BorderRadiuses | LocalizedBorderRadiuses;  差异内容：Length,BorderRadiuses,LocalizedBorderRadiuses | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class NavPushPathHelper  差异内容： export declare class NavPushPathHelper | api/@ohos.atomicservice.NavPushPathHelper.d.ets |
| 新增API | NA | 类名：NavPushPathHelper；  API声明：pushPath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>;  差异内容：pushPath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>; | api/@ohos.atomicservice.NavPushPathHelper.d.ets |
| 新增API | NA | 类名：NavPushPathHelper；  API声明：pushPath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>;  差异内容：pushPath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>; | api/@ohos.atomicservice.NavPushPathHelper.d.ets |
| 新增API | NA | 类名：NavPushPathHelper；  API声明：pushDestination(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>;  差异内容：pushDestination(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>; | api/@ohos.atomicservice.NavPushPathHelper.d.ets |
| 新增API | NA | 类名：NavPushPathHelper；  API声明：pushDestination(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>;  差异内容：pushDestination(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>; | api/@ohos.atomicservice.NavPushPathHelper.d.ets |
| 新增API | NA | 类名：NavPushPathHelper；  API声明：pushPathByName(moduleName: string, name: string, param: unknown, animated?: boolean): Promise<void>;  差异内容：pushPathByName(moduleName: string, name: string, param: unknown, animated?: boolean): Promise<void>; | api/@ohos.atomicservice.NavPushPathHelper.d.ets |
| 新增API | NA | 类名：NavPushPathHelper；  API声明：pushPathByName(moduleName: string, name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): Promise<void>;  差异内容：pushPathByName(moduleName: string, name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): Promise<void>; | api/@ohos.atomicservice.NavPushPathHelper.d.ets |
| 新增API | NA | 类名：NavPushPathHelper；  API声明：pushDestinationByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>;  差异内容：pushDestinationByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>; | api/@ohos.atomicservice.NavPushPathHelper.d.ets |
| 新增API | NA | 类名：NavPushPathHelper；  API声明：pushDestinationByName(moduleName: string, name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): Promise<void>;  差异内容：pushDestinationByName(moduleName: string, name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): Promise<void>; | api/@ohos.atomicservice.NavPushPathHelper.d.ets |
| 新增API | NA | 类名：NavPushPathHelper；  API声明：replacePath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>;  差异内容：replacePath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>; | api/@ohos.atomicservice.NavPushPathHelper.d.ets |
| 新增API | NA | 类名：NavPushPathHelper；  API声明：replacePath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>;  差异内容：replacePath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>; | api/@ohos.atomicservice.NavPushPathHelper.d.ets |
| 新增API | NA | 类名：NavPushPathHelper；  API声明：replacePathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>;  差异内容：replacePathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>; | api/@ohos.atomicservice.NavPushPathHelper.d.ets |
| 新增API | NA | 类名：componentSnapshot；  API声明：function getSync(id: string, options?: SnapshotOptions): image.PixelMap;  差异内容：function getSync(id: string, options?: SnapshotOptions): image.PixelMap; | api/@ohos.arkui.componentSnapshot.d.ts |
| 新增API | NA | 类名：FrameCallback；  API声明：onIdle(timeLeftInNano: number): void;  差异内容：onIdle(timeLeftInNano: number): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：ComponentSnapshot；  API声明：getSync(id: string, options?: componentSnapshot.SnapshotOptions): image.PixelMap;  差异内容：getSync(id: string, options?: componentSnapshot.SnapshotOptions): image.PixelMap; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明：function create(config: PiPConfiguration, contentNode: typeNode.XComponent): Promise<PiPController>;  差异内容：function create(config: PiPConfiguration, contentNode: typeNode.XComponent): Promise<PiPController>; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'XComponent', options: XComponentOptions): XComponent;  差异内容：function createNode(context: UIContext, nodeType: 'XComponent', options: XComponentOptions): XComponent; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：onClick(event: Callback<ClickEvent>, distanceThreshold: number): T;  差异内容：onClick(event: Callback<ClickEvent>, distanceThreshold: number): T; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum KeyboardAvoidMode  差异内容： declare enum KeyboardAvoidMode | component/common.d.ts |
| 新增API | NA | 类名：KeyboardAvoidMode；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | component/common.d.ts |
| 新增API | NA | 类名：KeyboardAvoidMode；  API声明：NONE = 1  差异内容：NONE = 1 | component/common.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：font(fontValue: Font, options?: FontSettingOptions): TextAttribute;  差异内容：font(fontValue: Font, options?: FontSettingOptions): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：fontWeight(weight: number | FontWeight | string, options?: FontSettingOptions): TextAttribute;  差异内容：fontWeight(weight: number | FontWeight | string, options?: FontSettingOptions): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：halfLeading(halfLeading: boolean): TextAttribute;  差异内容：halfLeading(halfLeading: boolean): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TipsDialog；  API声明：themeColorMode?: ThemeColorMode;  差异内容：themeColorMode?: ThemeColorMode; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：SelectDialog；  API声明：themeColorMode?: ThemeColorMode;  差异内容：themeColorMode?: ThemeColorMode; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：ConfirmDialog；  API声明：themeColorMode?: ThemeColorMode;  差异内容：themeColorMode?: ThemeColorMode; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：AlertDialog；  API声明：themeColorMode?: ThemeColorMode;  差异内容：themeColorMode?: ThemeColorMode; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：LoadingDialog；  API声明：themeColorMode?: ThemeColorMode;  差异内容：themeColorMode?: ThemeColorMode; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：CustomContentDialog；  API声明：themeColorMode?: ThemeColorMode;  差异内容：themeColorMode?: ThemeColorMode; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：UIUtils；  API声明：static makeObserved<T extends object>(source: T): T;  差异内容：static makeObserved<T extends object>(source: T): T; | api/@ohos.arkui.StateManagement.d.ts |
| 新增API | NA | 类名：AtomicServiceWeb；  API声明：@ObjectLink  controller: AtomicServiceWebController;  差异内容：@ObjectLink  controller: AtomicServiceWebController; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWeb；  API声明：@Prop  mixedMode?: MixedMode;  差异内容：@Prop  mixedMode?: MixedMode; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWeb；  API声明：@Prop  darkMode?: WebDarkMode;  差异内容：@Prop  darkMode?: WebDarkMode; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWeb；  API声明：@Prop  forceDarkAccess?: boolean;  差异内容：@Prop  forceDarkAccess?: boolean; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWeb；  API声明：onControllerAttached?: Callback<void>;  差异内容：onControllerAttached?: Callback<void>; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWeb；  API声明：onLoadIntercept?: OnLoadInterceptCallback;  差异内容：onLoadIntercept?: OnLoadInterceptCallback; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWeb；  API声明：onProgressChange?: Callback<OnProgressChangeEvent>;  差异内容：onProgressChange?: Callback<OnProgressChangeEvent>; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare interface OnLoadInterceptEvent  差异内容： export declare interface OnLoadInterceptEvent | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：OnLoadInterceptEvent；  API声明：data: WebResourceRequest;  差异内容：data: WebResourceRequest; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare interface OnProgressChangeEvent  差异内容： export declare interface OnProgressChangeEvent | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：OnProgressChangeEvent；  API声明：newProgress: number;  差异内容：newProgress: number; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class AtomicServiceWebController  差异内容： export declare class AtomicServiceWebController | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWebController；  API声明：getUserAgent(): string;  差异内容：getUserAgent(): string; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWebController；  API声明：getCustomUserAgent(): string;  差异内容：getCustomUserAgent(): string; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWebController；  API声明：setCustomUserAgent(userAgent: string): void;  差异内容：setCustomUserAgent(userAgent: string): void; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWebController；  API声明：refresh(): void;  差异内容：refresh(): void; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWebController；  API声明：forward(): void;  差异内容：forward(): void; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWebController；  API声明：backward(): void;  差异内容：backward(): void; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWebController；  API声明：accessForward(): boolean;  差异内容：accessForward(): boolean; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWebController；  API声明：accessBackward(): boolean;  差异内容：accessBackward(): boolean; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWebController；  API声明：accessStep(step: number): boolean;  差异内容：accessStep(step: number): boolean; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：AtomicServiceWebController；  API声明：loadUrl(url: string | Resource, headers?: Array<WebHeader>): void;  差异内容：loadUrl(url: string | Resource, headers?: Array<WebHeader>): void; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare interface WebHeader  差异内容： export declare interface WebHeader | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：WebHeader；  API声明：headerKey: string;  差异内容：headerKey: string; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：WebHeader；  API声明：headerValue: string;  差异内容：headerValue: string; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：global；  API声明：export type OnLoadInterceptCallback = (event: OnLoadInterceptEvent) => boolean;  差异内容：export type OnLoadInterceptCallback = (event: OnLoadInterceptEvent) => boolean; | api/@ohos.atomicservice.AtomicServiceWeb.d.ets |
| 新增API | NA | 类名：ShowToastOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：ShowToastOptions；  API声明：textColor?: ResourceColor;  差异内容：textColor?: ResourceColor; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：ShowToastOptions；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：ShowToastOptions；  API声明：shadow?: ShadowOptions | ShadowStyle;  差异内容：shadow?: ShadowOptions | ShadowStyle; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：BaseDialogOptions；  API声明：keyboardAvoidMode?: KeyboardAvoidMode;  差异内容：keyboardAvoidMode?: KeyboardAvoidMode; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：Window；  API声明：getWindowStatus(): WindowStatusType;  差异内容：getWindowStatus(): WindowStatusType; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：isFocused(): boolean;  差异内容：isFocused(): boolean; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：createSubWindowWithOptions(name: string, options: SubWindowOptions): Promise<Window>;  差异内容：createSubWindowWithOptions(name: string, options: SubWindowOptions): Promise<Window>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：ColumnAttribute；  API声明：reverse(isReversed: Optional<boolean>): ColumnAttribute;  差异内容：reverse(isReversed: Optional<boolean>): ColumnAttribute; | component/column.d.ts |
| 新增API | NA | 类名：CustomDialogControllerOptions；  API声明：keyboardAvoidMode?: KeyboardAvoidMode;  差异内容：keyboardAvoidMode?: KeyboardAvoidMode; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TapGestureParameters  差异内容： declare interface TapGestureParameters | component/gesture.d.ts |
| 新增API | NA | 类名：TapGestureParameters；  API声明：count?: number;  差异内容：count?: number; | component/gesture.d.ts |
| 新增API | NA | 类名：TapGestureParameters；  API声明：fingers?: number;  差异内容：fingers?: number; | component/gesture.d.ts |
| 新增API | NA | 类名：TapGestureParameters；  API声明：distanceThreshold?: number;  差异内容：distanceThreshold?: number; | component/gesture.d.ts |
| 新增API | NA | 类名：GestureRecognizer；  API声明：isValid(): boolean;  差异内容：isValid(): boolean; | component/gesture.d.ts |
| 新增API | NA | 类名：ListAttribute；  API声明：maintainVisibleContentPosition(enabled: boolean): ListAttribute;  差异内容：maintainVisibleContentPosition(enabled: boolean): ListAttribute; | component/list.d.ts |
| 新增API | NA | 类名：NavPathInfo；  API声明：isEntry?: boolean;  差异内容：isEntry?: boolean; | component/navigation.d.ts |
| 新增API | NA | 类名：RichEditorTextStyleResult；  API声明：textShadow?: Array<ShadowOptions>;  差异内容：textShadow?: Array<ShadowOptions>; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：enableKeyboardOnFocus(isEnabled: boolean): RichEditorAttribute;  差异内容：enableKeyboardOnFocus(isEnabled: boolean): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RowAttribute；  API声明：reverse(isReversed: Optional<boolean>): RowAttribute;  差异内容：reverse(isReversed: Optional<boolean>): RowAttribute; | component/row.d.ts |
| 新增API | NA | 类名：SaveDescription；  API声明：EXPORT\_TO\_GALLERY = 9  差异内容：EXPORT\_TO\_GALLERY = 9 | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveDescription；  API声明：QUICK\_SAVE\_TO\_GALLERY = 10  差异内容：QUICK\_SAVE\_TO\_GALLERY = 10 | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveDescription；  API声明：RESAVE\_TO\_GALLERY = 11  差异内容：RESAVE\_TO\_GALLERY = 11 | component/save\_button.d.ts |
| 新增API | NA | 类名：TextDataDetectorConfig；  API声明：color?: ResourceColor;  差异内容：color?: ResourceColor; | component/text\_common.d.ts |
| 新增API | NA | 类名：TextDataDetectorConfig；  API声明：decoration?: DecorationStyleInterface;  差异内容：decoration?: DecorationStyleInterface; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface FontSettingOptions  差异内容： declare interface FontSettingOptions | component/text\_common.d.ts |
| 新增API | NA | 类名：FontSettingOptions；  API声明：enableVariableFontWeight?: boolean;  差异内容：enableVariableFontWeight?: boolean; | component/text\_common.d.ts |
| 删除API | 类名：global；  API声明： export declare class FormComponentModifier  差异内容： export declare class FormComponentModifier | NA | api/arkui/FormComponentModifier.d.ts |
| 删除API | 类名：FormComponentModifier；  API声明：applyNormalAttribute?(instance: FormComponentAttribute): void;  差异内容：applyNormalAttribute?(instance: FormComponentAttribute): void; | NA | api/arkui/FormComponentModifier.d.ts |
