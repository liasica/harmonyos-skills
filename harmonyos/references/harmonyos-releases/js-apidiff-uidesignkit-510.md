---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-uidesignkit-510
title: UI Design Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > UI Design Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:16+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:1368000329ac49bbcd400455037f197da21d08d628d3e9759e46fa5700ee9f81
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：export declare type HdsNavigationInterface = (pathInfos?: NavPathStack) => HdsNavigationAttribute;  差异内容：export declare type HdsNavigationInterface = (pathInfos?: NavPathStack) => HdsNavigationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare type NavDestinationBuilder = (name: string, pageInfos: Object) => void;  差异内容：export declare type NavDestinationBuilder = (name: string, pageInfos: Object) => void; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare enum ScrollEffectType  差异内容：export declare enum ScrollEffectType | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：ScrollEffectType；  API声明：COMMON\_BLUR = 0  差异内容：COMMON\_BLUR = 0 | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare enum HdsNavigationTitleMode  差异内容：export declare enum HdsNavigationTitleMode | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationTitleMode；  API声明：FREE = 0  差异内容：FREE = 0 | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationTitleMode；  API声明：FULL = 1  差异内容：FULL = 1 | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationTitleMode；  API声明：MINI = 2  差异内容：MINI = 2 | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare type IconType = ResourceStr | SymbolGlyphModifier;  差异内容：export declare type IconType = ResourceStr | SymbolGlyphModifier; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare type HdsNavigationMenuItemOptions = HdsNavigationBadgeIconOptions;  差异内容：export declare type HdsNavigationMenuItemOptions = HdsNavigationBadgeIconOptions; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare type HdsNavigationBackButtonItemOptions = HdsNavigationIconOptions;  差异内容：export declare type HdsNavigationBackButtonItemOptions = HdsNavigationIconOptions; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface HdsNavigationBackgroundStyle  差异内容：export declare interface HdsNavigationBackgroundStyle | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationBackgroundStyle；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface HdsNavigationTitleStyle  差异内容：export declare interface HdsNavigationTitleStyle | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationTitleStyle；  API声明：mainTitleColor?: ResourceColor;  差异内容：mainTitleColor?: ResourceColor; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationTitleStyle；  API声明：subTitleColor?: ResourceColor;  差异内容：subTitleColor?: ResourceColor; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface HdsNavigationIconItemStyle  差异内容：export declare interface HdsNavigationIconItemStyle | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationIconItemStyle；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationIconItemStyle；  API声明：iconColor?: ResourceColor;  差异内容：iconColor?: ResourceColor; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface HdsTitleBarContentStyle  差异内容：export declare interface HdsTitleBarContentStyle | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsTitleBarContentStyle；  API声明：titleStyle?: HdsNavigationTitleStyle;  差异内容：titleStyle?: HdsNavigationTitleStyle; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsTitleBarContentStyle；  API声明：menuStyle?: HdsNavigationIconItemStyle;  差异内容：menuStyle?: HdsNavigationIconItemStyle; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsTitleBarContentStyle；  API声明：backIconStyle?: HdsNavigationIconItemStyle;  差异内容：backIconStyle?: HdsNavigationIconItemStyle; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface HdsNavigationTitleBarStyle  差异内容：export declare interface HdsNavigationTitleBarStyle | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationTitleBarStyle；  API声明：backgroundStyle?: HdsNavigationBackgroundStyle;  差异内容：backgroundStyle?: HdsNavigationBackgroundStyle; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationTitleBarStyle；  API声明：contentStyle?: HdsTitleBarContentStyle;  差异内容：contentStyle?: HdsTitleBarContentStyle; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface ScrollEffectOptions  差异内容：export declare interface ScrollEffectOptions | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：ScrollEffectOptions；  API声明：enableScrollEffect?: boolean;  差异内容：enableScrollEffect?: boolean; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：ScrollEffectOptions；  API声明：scrollEffectType?: ScrollEffectType;  差异内容：scrollEffectType?: ScrollEffectType; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：ScrollEffectOptions；  API声明：blurEffectiveStartOffset?: LengthMetrics;  差异内容：blurEffectiveStartOffset?: LengthMetrics; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：ScrollEffectOptions；  API声明：blurEffectiveEndOffset?: LengthMetrics;  差异内容：blurEffectiveEndOffset?: LengthMetrics; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface TitleBarStyleOptions  差异内容：export declare interface TitleBarStyleOptions | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：TitleBarStyleOptions；  API声明：scrollEffectOpts?: ScrollEffectOptions;  差异内容：scrollEffectOpts?: ScrollEffectOptions; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：TitleBarStyleOptions；  API声明：originalStyle?: HdsNavigationTitleBarStyle;  差异内容：originalStyle?: HdsNavigationTitleBarStyle; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：TitleBarStyleOptions；  API声明：scrollEffectStyle?: HdsNavigationTitleBarStyle;  差异内容：scrollEffectStyle?: HdsNavigationTitleBarStyle; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface HdsNavigationBadgeOptions  差异内容：export declare interface HdsNavigationBadgeOptions | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationBadgeOptions；  API声明：count?: number;  差异内容：count?: number; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationBadgeOptions；  API声明：value?: string;  差异内容：value?: string; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface HdsNavigationIconOptions  差异内容：export declare interface HdsNavigationIconOptions | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationIconOptions；  API声明：icon?: IconType;  差异内容：icon?: IconType; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationIconOptions；  API声明：label?: ResourceStr;  差异内容：label?: ResourceStr; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationIconOptions；  API声明：isEnabled?: boolean;  差异内容：isEnabled?: boolean; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationIconOptions；  API声明：action?: Callback<void>;  差异内容：action?: Callback<void>; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface HdsNavigationBadgeIconOptions  差异内容：export declare interface HdsNavigationBadgeIconOptions | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationBadgeIconOptions；  API声明：content?: HdsNavigationIconOptions;  差异内容：content?: HdsNavigationIconOptions; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationBadgeIconOptions；  API声明：badge?: HdsNavigationBadgeOptions;  差异内容：badge?: HdsNavigationBadgeOptions; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface HdsNavigationMenuContentOptions  差异内容：export declare interface HdsNavigationMenuContentOptions | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationMenuContentOptions；  API声明：value?: Array<HdsNavigationMenuItemOptions>;  差异内容：value?: Array<HdsNavigationMenuItemOptions>; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationMenuContentOptions；  API声明：maxCount?: number;  差异内容：maxCount?: number; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface HdsNavigationTitle  差异内容：export declare interface HdsNavigationTitle | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationTitle；  API声明：mainTitle: ResourceStr;  差异内容：mainTitle: ResourceStr; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationTitle；  API声明：subTitle?: ResourceStr;  差异内容：subTitle?: ResourceStr; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface TitleBarContentOptions  差异内容：export declare interface TitleBarContentOptions | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：TitleBarContentOptions；  API声明：title?: HdsNavigationTitle;  差异内容：title?: HdsNavigationTitle; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：TitleBarContentOptions；  API声明：menu?: HdsNavigationMenuContentOptions;  差异内容：menu?: HdsNavigationMenuContentOptions; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：TitleBarContentOptions；  API声明：backIcon?: HdsNavigationBackButtonItemOptions;  差异内容：backIcon?: HdsNavigationBackButtonItemOptions; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface PaddingOptions  差异内容：export declare interface PaddingOptions | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：PaddingOptions；  API声明：start?: LengthMetrics;  差异内容：start?: LengthMetrics; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：PaddingOptions；  API声明：end?: LengthMetrics;  差异内容：end?: LengthMetrics; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface HdsNavigationTitleBarOptions  差异内容：export declare interface HdsNavigationTitleBarOptions | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationTitleBarOptions；  API声明：padding?: PaddingOptions;  差异内容：padding?: PaddingOptions; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationTitleBarOptions；  API声明：style?: TitleBarStyleOptions;  差异内容：style?: TitleBarStyleOptions; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationTitleBarOptions；  API声明：content?: TitleBarContentOptions;  差异内容：content?: TitleBarContentOptions; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface NavBarWidthRangeOptions  差异内容：export declare interface NavBarWidthRangeOptions | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：NavBarWidthRangeOptions；  API声明：minWidth?: Dimension;  差异内容：minWidth?: Dimension; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：NavBarWidthRangeOptions；  API声明：maxWidth?: Dimension;  差异内容：maxWidth?: Dimension; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：declare class HdsNavigationAttribute  差异内容：declare class HdsNavigationAttribute | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationAttribute；  API声明：titleBar(options?: HdsNavigationTitleBarOptions): HdsNavigationAttribute;  差异内容：titleBar(options?: HdsNavigationTitleBarOptions): HdsNavigationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationAttribute；  API声明：titleMode(value: HdsNavigationTitleMode): HdsNavigationAttribute;  差异内容：titleMode(value: HdsNavigationTitleMode): HdsNavigationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationAttribute；  API声明：toolbarConfiguration(value: Array<ToolbarItem> | CustomBuilder, options?: NavigationToolbarOptions): HdsNavigationAttribute;  差异内容：toolbarConfiguration(value: Array<ToolbarItem> | CustomBuilder, options?: NavigationToolbarOptions): HdsNavigationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationAttribute；  API声明：hideToolBar(hide: boolean, animated?: boolean): HdsNavigationAttribute;  差异内容：hideToolBar(hide: boolean, animated?: boolean): HdsNavigationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationAttribute；  API声明：hideTitleBar(hide: boolean, animated?: boolean): HdsNavigationAttribute;  差异内容：hideTitleBar(hide: boolean, animated?: boolean): HdsNavigationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationAttribute；  API声明：hideBackButton(value: boolean): HdsNavigationAttribute;  差异内容：hideBackButton(value: boolean): HdsNavigationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationAttribute；  API声明：navBarWidth(value: Length): HdsNavigationAttribute;  差异内容：navBarWidth(value: Length): HdsNavigationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationAttribute；  API声明：navBarPosition(value: NavBarPosition): HdsNavigationAttribute;  差异内容：navBarPosition(value: NavBarPosition): HdsNavigationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationAttribute；  API声明：mode(value: NavigationMode): HdsNavigationAttribute;  差异内容：mode(value: NavigationMode): HdsNavigationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationAttribute；  API声明：hideNavBar(value: boolean): HdsNavigationAttribute;  差异内容：hideNavBar(value: boolean): HdsNavigationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationAttribute；  API声明：navDestination(builder: NavDestinationBuilder): HdsNavigationAttribute;  差异内容：navDestination(builder: NavDestinationBuilder): HdsNavigationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationAttribute；  API声明：navBarWidthRange(value: NavBarWidthRangeOptions): HdsNavigationAttribute;  差异内容：navBarWidthRange(value: NavBarWidthRangeOptions): HdsNavigationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationAttribute；  API声明：minContentWidth(value: Dimension): HdsNavigationAttribute;  差异内容：minContentWidth(value: Dimension): HdsNavigationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationAttribute；  API声明：ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>): HdsNavigationAttribute;  差异内容：ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>): HdsNavigationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationAttribute；  API声明：systemBarStyle(originalStyle: Optional<SystemBarStyle>, scrollEffectStyle: Optional<SystemBarStyle>): HdsNavigationAttribute;  差异内容：systemBarStyle(originalStyle: Optional<SystemBarStyle>, scrollEffectStyle: Optional<SystemBarStyle>): HdsNavigationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationAttribute；  API声明：recoverable(recoverable: Optional<boolean>): HdsNavigationAttribute;  差异内容：recoverable(recoverable: Optional<boolean>): HdsNavigationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationAttribute；  API声明：onNavBarStateChange(callback: Callback<boolean>): HdsNavigationAttribute;  差异内容：onNavBarStateChange(callback: Callback<boolean>): HdsNavigationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavigationAttribute；  API声明：onNavigationModeChange(callback: Callback<NavigationMode>): HdsNavigationAttribute;  差异内容：onNavigationModeChange(callback: Callback<NavigationMode>): HdsNavigationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare const HdsNavigation: HdsNavigationInterface;  差异内容：export declare const HdsNavigation: HdsNavigationInterface; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare const HdsNavigationInstance: HdsNavigationAttribute;  差异内容：export declare const HdsNavigationInstance: HdsNavigationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare type HdsNavDestinationInterface = () => HdsNavDestinationAttribute;  差异内容：export declare type HdsNavDestinationInterface = () => HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：declare class HdsNavDestinationAttribute  差异内容：declare class HdsNavDestinationAttribute | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavDestinationAttribute；  API声明：titleBar(options?: HdsNavigationTitleBarOptions): HdsNavDestinationAttribute;  差异内容：titleBar(options?: HdsNavigationTitleBarOptions): HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavDestinationAttribute；  API声明：hideTitleBar(hide: boolean, animated?: boolean): HdsNavDestinationAttribute;  差异内容：hideTitleBar(hide: boolean, animated?: boolean): HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavDestinationAttribute；  API声明：hideBackButton(value: boolean): HdsNavDestinationAttribute;  差异内容：hideBackButton(value: boolean): HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavDestinationAttribute；  API声明：mode(value: NavDestinationMode): HdsNavDestinationAttribute;  差异内容：mode(value: NavDestinationMode): HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavDestinationAttribute；  API声明：toolbarConfiguration(toolbarParam: Array<ToolbarItem> | CustomBuilder, options?: NavigationToolbarOptions): HdsNavDestinationAttribute;  差异内容：toolbarConfiguration(toolbarParam: Array<ToolbarItem> | CustomBuilder, options?: NavigationToolbarOptions): HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavDestinationAttribute；  API声明：hideToolBar(hide: boolean, animated?: boolean): HdsNavDestinationAttribute;  差异内容：hideToolBar(hide: boolean, animated?: boolean): HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavDestinationAttribute；  API声明：onShown(callback: Callback<void>): HdsNavDestinationAttribute;  差异内容：onShown(callback: Callback<void>): HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavDestinationAttribute；  API声明：onHidden(callback: Callback<void>): HdsNavDestinationAttribute;  差异内容：onHidden(callback: Callback<void>): HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavDestinationAttribute；  API声明：onReady(callback: Callback<NavDestinationContext>): HdsNavDestinationAttribute;  差异内容：onReady(callback: Callback<NavDestinationContext>): HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavDestinationAttribute；  API声明：onWillAppear(callback: Callback<void>): HdsNavDestinationAttribute;  差异内容：onWillAppear(callback: Callback<void>): HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavDestinationAttribute；  API声明：onWillDisappear(callback: Callback<void>): HdsNavDestinationAttribute;  差异内容：onWillDisappear(callback: Callback<void>): HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavDestinationAttribute；  API声明：onWillShow(callback: Callback<void>): HdsNavDestinationAttribute;  差异内容：onWillShow(callback: Callback<void>): HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavDestinationAttribute；  API声明：onWillHide(callback: Callback<void>): HdsNavDestinationAttribute;  差异内容：onWillHide(callback: Callback<void>): HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavDestinationAttribute；  API声明：ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>): HdsNavDestinationAttribute;  差异内容：ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>): HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavDestinationAttribute；  API声明：systemBarStyle(originalStyle: Optional<SystemBarStyle>, scrollEffectStyle: Optional<SystemBarStyle>): HdsNavDestinationAttribute;  差异内容：systemBarStyle(originalStyle: Optional<SystemBarStyle>, scrollEffectStyle: Optional<SystemBarStyle>): HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavDestinationAttribute；  API声明：recoverable(recoverable: Optional<boolean>): HdsNavDestinationAttribute;  差异内容：recoverable(recoverable: Optional<boolean>): HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare const HdsNavDestination: HdsNavDestinationInterface;  差异内容：export declare const HdsNavDestination: HdsNavDestinationInterface; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare const HdsNavDestinationInstance: HdsNavDestinationAttribute;  差异内容：export declare const HdsNavDestinationInstance: HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.hds.hdsBaseComponent.d.ets  差异内容：UIDesignKit | api/@hms.hds.hdsBaseComponent.d.ets |
