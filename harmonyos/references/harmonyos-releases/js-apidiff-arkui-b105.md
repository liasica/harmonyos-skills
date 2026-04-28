---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-b105
title: ArkUI
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > OS平台能力 > API变更清单 > HarmonyOS 5.0.1(13) Beta3引入的API > ArkUI
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:02+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:356c2132613a8e65a28dcb036d6daea28f05ca8b9781f8cf0b9dd4ded73d0dab
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API卡片权限变更 | 类名：TextAttribute；  API声明：fontFeature(value: string): TextAttribute;  差异内容：NA | 类名：TextAttribute；  API声明：fontFeature(value: string): TextAttribute;  差异内容：form | component/text.d.ts |
| API废弃版本变更 | 类名：ToastShowMode；  API声明：TOP\_MOST = 1  差异内容：NA | 类名：ToastShowMode；  API声明：TOP\_MOST = 1  差异内容：12 | api/@ohos.promptAction.d.ts |
| API废弃版本变更 | 类名：global；  API声明： declare enum NavigationType  差异内容：NA | 类名：global；  API声明： declare enum NavigationType  差异内容：13 | component/navigator.d.ts |
| API废弃版本变更 | 类名：NavigationType；  API声明：Push  差异内容：NA | 类名：NavigationType；  API声明：Push  差异内容：13 | component/navigator.d.ts |
| API废弃版本变更 | 类名：NavigationType；  API声明：Back  差异内容：NA | 类名：NavigationType；  API声明：Back  差异内容：13 | component/navigator.d.ts |
| API废弃版本变更 | 类名：NavigationType；  API声明：Replace  差异内容：NA | 类名：NavigationType；  API声明：Replace  差异内容：13 | component/navigator.d.ts |
| API废弃版本变更 | 类名：global；  API声明： interface NavigatorInterface  差异内容：NA | 类名：global；  API声明： interface NavigatorInterface  差异内容：13 | component/navigator.d.ts |
| API废弃版本变更 | 类名：global；  API声明： declare class NavigatorAttribute  差异内容：NA | 类名：global；  API声明： declare class NavigatorAttribute  差异内容：13 | component/navigator.d.ts |
| API废弃版本变更 | 类名：NavigatorAttribute；  API声明：active(value: boolean): NavigatorAttribute;  差异内容：NA | 类名：NavigatorAttribute；  API声明：active(value: boolean): NavigatorAttribute;  差异内容：13 | component/navigator.d.ts |
| API废弃版本变更 | 类名：NavigatorAttribute；  API声明：type(value: NavigationType): NavigatorAttribute;  差异内容：NA | 类名：NavigatorAttribute；  API声明：type(value: NavigationType): NavigatorAttribute;  差异内容：13 | component/navigator.d.ts |
| API废弃版本变更 | 类名：NavigatorAttribute；  API声明：target(value: string): NavigatorAttribute;  差异内容：NA | 类名：NavigatorAttribute；  API声明：target(value: string): NavigatorAttribute;  差异内容：13 | component/navigator.d.ts |
| API废弃版本变更 | 类名：NavigatorAttribute；  API声明：params(value: object): NavigatorAttribute;  差异内容：NA | 类名：NavigatorAttribute；  API声明：params(value: object): NavigatorAttribute;  差异内容：13 | component/navigator.d.ts |
| API废弃版本变更 | 类名：global；  API声明：declare const Navigator: NavigatorInterface;  差异内容：NA | 类名：global；  API声明：declare const Navigator: NavigatorInterface;  差异内容：13 | component/navigator.d.ts |
| API废弃版本变更 | 类名：global；  API声明：declare const NavigatorInstance: NavigatorAttribute;  差异内容：NA | 类名：global；  API声明：declare const NavigatorInstance: NavigatorAttribute;  差异内容：13 | component/navigator.d.ts |
| API废弃版本变更 | 类名：global；  API声明： declare interface RouteInfo  差异内容：NA | 类名：global；  API声明： declare interface RouteInfo  差异内容：13 | component/nav\_router.d.ts |
| API废弃版本变更 | 类名：RouteInfo；  API声明：name: string;  差异内容：NA | 类名：RouteInfo；  API声明：name: string;  差异内容：13 | component/nav\_router.d.ts |
| API废弃版本变更 | 类名：RouteInfo；  API声明：param?: unknown;  差异内容：NA | 类名：RouteInfo；  API声明：param?: unknown;  差异内容：13 | component/nav\_router.d.ts |
| API废弃版本变更 | 类名：global；  API声明： declare interface NavRouterInterface  差异内容：NA | 类名：global；  API声明： declare interface NavRouterInterface  差异内容：13 | component/nav\_router.d.ts |
| API废弃版本变更 | 类名：global；  API声明： declare enum NavRouteMode  差异内容：NA | 类名：global；  API声明： declare enum NavRouteMode  差异内容：13 | component/nav\_router.d.ts |
| API废弃版本变更 | 类名：NavRouteMode；  API声明：PUSH\_WITH\_RECREATE  差异内容：NA | 类名：NavRouteMode；  API声明：PUSH\_WITH\_RECREATE  差异内容：13 | component/nav\_router.d.ts |
| API废弃版本变更 | 类名：NavRouteMode；  API声明：PUSH  差异内容：NA | 类名：NavRouteMode；  API声明：PUSH  差异内容：13 | component/nav\_router.d.ts |
| API废弃版本变更 | 类名：NavRouteMode；  API声明：REPLACE  差异内容：NA | 类名：NavRouteMode；  API声明：REPLACE  差异内容：13 | component/nav\_router.d.ts |
| API废弃版本变更 | 类名：global；  API声明： declare class NavRouterAttribute  差异内容：NA | 类名：global；  API声明： declare class NavRouterAttribute  差异内容：13 | component/nav\_router.d.ts |
| API废弃版本变更 | 类名：NavRouterAttribute；  API声明：onStateChange(callback: (isActivated: boolean) => void): NavRouterAttribute;  差异内容：NA | 类名：NavRouterAttribute；  API声明：onStateChange(callback: (isActivated: boolean) => void): NavRouterAttribute;  差异内容：13 | component/nav\_router.d.ts |
| API废弃版本变更 | 类名：NavRouterAttribute；  API声明：mode(mode: NavRouteMode): NavRouterAttribute;  差异内容：NA | 类名：NavRouterAttribute；  API声明：mode(mode: NavRouteMode): NavRouterAttribute;  差异内容：13 | component/nav\_router.d.ts |
| API废弃版本变更 | 类名：global；  API声明：declare const NavRouter: NavRouterInterface;  差异内容：NA | 类名：global；  API声明：declare const NavRouter: NavRouterInterface;  差异内容：13 | component/nav\_router.d.ts |
| API废弃版本变更 | 类名：global；  API声明：declare const NavRouterInstance: NavRouterAttribute;  差异内容：NA | 类名：global；  API声明：declare const NavRouterInstance: NavRouterAttribute;  差异内容：13 | component/nav\_router.d.ts |
| 错误码变更 | 类名：componentUtils；  API声明：function getRectangleById(id: string): ComponentInfo;  差异内容：NA | 类名：componentUtils；  API声明：function getRectangleById(id: string): ComponentInfo;  差异内容：100001 | api/@ohos.arkui.componentUtils.d.ts |
| 错误码变更 | 类名：ComponentUtils；  API声明：getRectangleById(id: string): componentUtils.ComponentInfo;  差异内容：NA | 类名：ComponentUtils；  API声明：getRectangleById(id: string): componentUtils.ComponentInfo;  差异内容：100001 | api/@ohos.arkui.UIContext.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：onVisibleAreaChange(ratios: Array<number>, event: (isVisible: boolean, currentRatio: number) => void): T;  差异内容：event: (isVisible: boolean, currentRatio: number) => void | 类名：CommonMethod；  API声明：onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback): T;  差异内容：event: VisibleAreaChangeCallback | component/common.d.ts |
| 自定义类型变更 | 类名：global；  API声明：declare type VisibleAreaChangeCallback = (isVisible: boolean, currentRatio: number) => void;  差异内容：isVisible: boolean, currentRatio: number | 类名：global；  API声明：declare type VisibleAreaChangeCallback = (isExpanding: boolean, currentRatio: number) => void;  差异内容：isExpanding: boolean, currentRatio: number | component/common.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getWindowWidthBreakpoint(): WidthBreakpoint;  差异内容：getWindowWidthBreakpoint(): WidthBreakpoint; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getWindowHeightBreakpoint(): HeightBreakpoint;  差异内容：getWindowHeightBreakpoint(): HeightBreakpoint; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：isFollowingSystemFontScale(): boolean;  差异内容：isFollowingSystemFontScale(): boolean; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getMaxFontScale(): number;  差异内容：getMaxFontScale(): number; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum SheetKeyboardAvoidMode  差异内容： declare enum SheetKeyboardAvoidMode | component/common.d.ts |
| 新增API | NA | 类名：SheetKeyboardAvoidMode；  API声明：NONE = 0  差异内容：NONE = 0 | component/common.d.ts |
| 新增API | NA | 类名：SheetKeyboardAvoidMode；  API声明：TRANSLATE\_AND\_RESIZE = 1  差异内容：TRANSLATE\_AND\_RESIZE = 1 | component/common.d.ts |
| 新增API | NA | 类名：SheetKeyboardAvoidMode；  API声明：RESIZE\_ONLY = 2  差异内容：RESIZE\_ONLY = 2 | component/common.d.ts |
| 新增API | NA | 类名：SheetKeyboardAvoidMode；  API声明：TRANSLATE\_AND\_SCROLL = 3  差异内容：TRANSLATE\_AND\_SCROLL = 3 | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：keyboardAvoidMode?: SheetKeyboardAvoidMode;  差异内容：keyboardAvoidMode?: SheetKeyboardAvoidMode; | component/common.d.ts |
| 新增API | NA | 类名：ContextMenuOptions；  API声明：layoutRegionMargin?: Margin;  差异内容：layoutRegionMargin?: Margin; | component/common.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：enableHapticFeedback(isEnabled: boolean): TextAttribute;  差异内容：enableHapticFeedback(isEnabled: boolean): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：ComposeTitleBarMenuItem；  API声明：label?: ResourceStr;  差异内容：label?: ResourceStr; | api/@ohos.arkui.advanced.ComposeTitleBar.d.ets |
| 新增API | NA | 类名：SegmentButton；  API声明：onItemClicked?: Callback<number>;  差异内容：onItemClicked?: Callback<number>; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SelectTitleBarMenuItem；  API声明：label?: ResourceStr;  差异内容：label?: ResourceStr; | api/@ohos.arkui.advanced.SelectTitleBar.d.ets |
| 新增API | NA | 类名：TabTitleBarMenuItem；  API声明：label?: ResourceStr;  差异内容：label?: ResourceStr; | api/@ohos.arkui.advanced.TabTitleBar.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface ToolBarSymbolGlyphOptions  差异内容： export interface ToolBarSymbolGlyphOptions | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ToolBarSymbolGlyphOptions；  API声明：normal?: SymbolGlyphModifier;  差异内容：normal?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ToolBarSymbolGlyphOptions；  API声明：activated?: SymbolGlyphModifier;  差异内容：activated?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ToolBarOption；  API声明：textColor?: ResourceColor;  差异内容：textColor?: ResourceColor; | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ToolBarOption；  API声明：activatedTextColor?: ResourceColor;  差异内容：activatedTextColor?: ResourceColor; | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ToolBarOption；  API声明：iconColor?: ResourceColor;  差异内容：iconColor?: ResourceColor; | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ToolBarOption；  API声明：activatedIconColor?: ResourceColor;  差异内容：activatedIconColor?: ResourceColor; | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ToolBarOption；  API声明：toolBarSymbolOptions?: ToolBarSymbolGlyphOptions;  差异内容：toolBarSymbolOptions?: ToolBarSymbolGlyphOptions; | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class ToolBarModifier  差异内容： export declare class ToolBarModifier | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ToolBarModifier；  API声明：height(height: LengthMetrics): ToolBarModifier;  差异内容：height(height: LengthMetrics): ToolBarModifier; | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ToolBarModifier；  API声明：backgroundColor(backgroundColor: ResourceColor): ToolBarModifier;  差异内容：backgroundColor(backgroundColor: ResourceColor): ToolBarModifier; | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ToolBarModifier；  API声明：padding(padding: LengthMetrics): ToolBarModifier;  差异内容：padding(padding: LengthMetrics): ToolBarModifier; | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ToolBarModifier；  API声明：stateEffect(stateEffect: boolean): ToolBarModifier;  差异内容：stateEffect(stateEffect: boolean): ToolBarModifier; | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ToolBar；  API声明：@Prop  dividerModifier?: DividerModifier;  差异内容：@Prop  dividerModifier?: DividerModifier; | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ToolBar；  API声明：@Prop  toolBarModifier?: ToolBarModifier;  差异内容：@Prop  toolBarModifier?: ToolBarModifier; | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：global；  API声明：declare type FrameNode = import('../api/arkui/FrameNode').FrameNode;  差异内容：declare type FrameNode = import('../api/arkui/FrameNode').FrameNode; | component/canvas.d.ts |
| 新增API | NA | 类名：CanvasRenderingContext2D；  API声明：readonly canvas: FrameNode;  差异内容：readonly canvas: FrameNode; | component/canvas.d.ts |
| 新增API | NA | 类名：CanvasRenderingContext2D；  API声明：on(type: 'onAttach', callback: Callback<void>): void;  差异内容：on(type: 'onAttach', callback: Callback<void>): void; | component/canvas.d.ts |
| 新增API | NA | 类名：CanvasRenderingContext2D；  API声明：off(type: 'onAttach', callback?: Callback<void>): void;  差异内容：off(type: 'onAttach', callback?: Callback<void>): void; | component/canvas.d.ts |
| 新增API | NA | 类名：CanvasRenderingContext2D；  API声明：on(type: 'onDetach', callback: Callback<void>): void;  差异内容：on(type: 'onDetach', callback: Callback<void>): void; | component/canvas.d.ts |
| 新增API | NA | 类名：CanvasRenderingContext2D；  API声明：off(type: 'onDetach', callback?: Callback<void>): void;  差异内容：off(type: 'onDetach', callback?: Callback<void>): void; | component/canvas.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum WidthBreakpoint  差异内容： declare enum WidthBreakpoint | component/enums.d.ts |
| 新增API | NA | 类名：WidthBreakpoint；  API声明：WIDTH\_XS = 0  差异内容：WIDTH\_XS = 0 | component/enums.d.ts |
| 新增API | NA | 类名：WidthBreakpoint；  API声明：WIDTH\_SM = 1  差异内容：WIDTH\_SM = 1 | component/enums.d.ts |
| 新增API | NA | 类名：WidthBreakpoint；  API声明：WIDTH\_MD = 2  差异内容：WIDTH\_MD = 2 | component/enums.d.ts |
| 新增API | NA | 类名：WidthBreakpoint；  API声明：WIDTH\_LG = 3  差异内容：WIDTH\_LG = 3 | component/enums.d.ts |
| 新增API | NA | 类名：WidthBreakpoint；  API声明：WIDTH\_XL = 4  差异内容：WIDTH\_XL = 4 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum HeightBreakpoint  差异内容： declare enum HeightBreakpoint | component/enums.d.ts |
| 新增API | NA | 类名：HeightBreakpoint；  API声明：HEIGHT\_SM = 0  差异内容：HEIGHT\_SM = 0 | component/enums.d.ts |
| 新增API | NA | 类名：HeightBreakpoint；  API声明：HEIGHT\_MD = 1  差异内容：HEIGHT\_MD = 1 | component/enums.d.ts |
| 新增API | NA | 类名：HeightBreakpoint；  API声明：HEIGHT\_LG = 2  差异内容：HEIGHT\_LG = 2 | component/enums.d.ts |
| 新增API | NA | 类名：NavigationTitleOptions；  API声明：mainTitleModifier?: TextModifier;  差异内容：mainTitleModifier?: TextModifier; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationTitleOptions；  API声明：subTitleModifier?: TextModifier;  差异内容：subTitleModifier?: TextModifier; | component/navigation.d.ts |
| 新增API | NA | 类名：SelectionMenuOptions；  API声明：menuType?: MenuType;  差异内容：menuType?: MenuType; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：enableHapticFeedback(isEnabled: boolean): RichEditorAttribute;  差异内容：enableHapticFeedback(isEnabled: boolean): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：barState(state: BarState): RichEditorAttribute;  差异内容：barState(state: BarState): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：enableHapticFeedback(isEnabled: boolean): SearchAttribute;  差异内容：enableHapticFeedback(isEnabled: boolean): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：CustomSpan；  API声明：invalidate(): void;  差异内容：invalidate(): void; | component/styled\_string.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：enableHapticFeedback(isEnabled: boolean): TextAreaAttribute;  差异内容：enableHapticFeedback(isEnabled: boolean): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum MenuType  差异内容： declare enum MenuType | component/text\_common.d.ts |
| 新增API | NA | 类名：MenuType；  API声明：SELECTION\_MENU = 0  差异内容：SELECTION\_MENU = 0 | component/text\_common.d.ts |
| 新增API | NA | 类名：MenuType；  API声明：PREVIEW\_MENU = 1  差异内容：PREVIEW\_MENU = 1 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextMenuItemId；  API声明：static readonly AI\_WRITER: TextMenuItemId;  差异内容：static readonly AI\_WRITER: TextMenuItemId; | component/text\_common.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：enableHapticFeedback(isEnabled: boolean): TextInputAttribute;  差异内容：enableHapticFeedback(isEnabled: boolean): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：XComponentAttribute；  API声明：enableSecure(isSecure: boolean): XComponentAttribute;  差异内容：enableSecure(isSecure: boolean): XComponentAttribute; | component/xcomponent.d.ts |
