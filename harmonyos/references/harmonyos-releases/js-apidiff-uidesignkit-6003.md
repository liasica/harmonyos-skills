---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-uidesignkit-6003
title: UI Design Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > UI Design Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:22+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:14d23d39575183c3db6213771076671bebba1590f8f7cf45aa8bc502b27036cd
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 自定义类型变更 | 类名：global；  API声明：export declare type IconType = ResourceStr | SymbolGlyphModifier;  差异内容：ResourceStr | SymbolGlyphModifier | 类名：global；  API声明：export declare type IconType = ResourceStr | SymbolGlyphModifier | PixelMap;  差异内容：ResourceStr | SymbolGlyphModifier | PixelMap | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare enum BlurStrategy  差异内容：export declare enum BlurStrategy | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：BlurStrategy；  API声明：ENABLE = 0  差异内容：ENABLE = 0 | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：BlurStrategy；  API声明：DISABLE = 1  差异内容：DISABLE = 1 | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：BlurStrategy；  API声明：ADAPTIVE = 2  差异内容：ADAPTIVE = 2 | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface MultiWindowEntryInAPPMenuParams  差异内容：export declare interface MultiWindowEntryInAPPMenuParams | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：MultiWindowEntryInAPPMenuParams；  API声明：want: Want;  差异内容：want: Want; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface SuffixArrowIconOptions  差异内容：export declare interface SuffixArrowIconOptions | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：SuffixArrowIconOptions；  API声明：arrowColor?: ResourceColor;  差异内容：arrowColor?: ResourceColor; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：SuffixArrowIconOptions；  API声明：onClick?: OnClickCallback;  差异内容：onClick?: OnClickCallback; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：SuffixArrowIconOptions；  API声明：arrowId?: string;  差异内容：arrowId?: string; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：SuffixArrowIconOptions；  API声明：enable?: boolean;  差异内容：enable?: boolean; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：SuffixArrowIconOptions；  API声明：accessibilityOptions?: AccessibilityOptions;  差异内容：accessibilityOptions?: AccessibilityOptions; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface SuffixArrowIconTextOptions  差异内容：export declare interface SuffixArrowIconTextOptions | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：SuffixArrowIconTextOptions；  API声明：startArrow?: SuffixArrowIconOptions;  差异内容：startArrow?: SuffixArrowIconOptions; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：SuffixArrowIconTextOptions；  API声明：text?: TextOptions;  差异内容：text?: TextOptions; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：SuffixArrowIconTextOptions；  API声明：endArrow?: SuffixArrowIconOptions;  差异内容：endArrow?: SuffixArrowIconOptions; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class SuffixArrowIconText  差异内容：export declare class SuffixArrowIconText | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：SuffixArrowIconText；  API声明：options?: SuffixArrowIconTextOptions;  差异内容：options?: SuffixArrowIconTextOptions; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface MultiWindowEntryInAPPIconOptions  差异内容：export declare interface MultiWindowEntryInAPPIconOptions | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：MultiWindowEntryInAPPIconOptions；  API声明：iconColor?: ResourceColor;  差异内容：iconColor?: ResourceColor; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：MultiWindowEntryInAPPIconOptions；  API声明：iconWeight?: number | FontWeight | string;  差异内容：iconWeight?: number | FontWeight | string; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：MultiWindowEntryInAPPIconOptions；  API声明：iconSize?: number | string | Resource;  差异内容：iconSize?: number | string | Resource; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：MultiWindowEntryInAPPIconOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface MultiWindowEntryInAPPSubtitleOptions  差异内容：export declare interface MultiWindowEntryInAPPSubtitleOptions | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：MultiWindowEntryInAPPSubtitleOptions；  API声明：modifier?: TextModifier;  差异内容：modifier?: TextModifier; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface MultiWindowEntryInAPPStyle  差异内容：export declare interface MultiWindowEntryInAPPStyle | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：MultiWindowEntryInAPPStyle；  API声明：iconOptions?: MultiWindowEntryInAPPIconOptions;  差异内容：iconOptions?: MultiWindowEntryInAPPIconOptions; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：MultiWindowEntryInAPPStyle；  API声明：subtitleOptions?: MultiWindowEntryInAPPSubtitleOptions;  差异内容：subtitleOptions?: MultiWindowEntryInAPPSubtitleOptions; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class MultiWindowEntryInAPPAttribute  差异内容：export declare class MultiWindowEntryInAPPAttribute | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface MultiWindowEntryInAPPParams  差异内容：export declare interface MultiWindowEntryInAPPParams | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：MultiWindowEntryInAPPParams；  API声明：want: Want;  差异内容：want: Want; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：MultiWindowEntryInAPPParams；  API声明：isShowSubtitle?: boolean;  差异内容：isShowSubtitle?: boolean; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：MultiWindowEntryInAPPParams；  API声明：multiWindowEntryInAPPStyle?: MultiWindowEntryInAPPStyle;  差异内容：multiWindowEntryInAPPStyle?: MultiWindowEntryInAPPStyle; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare type MultiWindowEntryInAPPInterface = (params: MultiWindowEntryInAPPParams) => MultiWindowEntryInAPPAttribute;  差异内容：export declare type MultiWindowEntryInAPPInterface = (params: MultiWindowEntryInAPPParams) => MultiWindowEntryInAPPAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare const MultiWindowEntryInAPP: MultiWindowEntryInAPPInterface;  差异内容：export declare const MultiWindowEntryInAPP: MultiWindowEntryInAPPInterface; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：declare const MultiWindowEntryInAPPInstance: MultiWindowEntryInAPPAttribute;  差异内容：declare const MultiWindowEntryInAPPInstance: MultiWindowEntryInAPPAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsActionBar；  API声明：@Param  blurStrategy?: BlurStrategy;  差异内容：@Param  blurStrategy?: BlurStrategy; | api/@hms.hds.HdsActionBar.d.ets |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：ActionBarButton；  API声明：@Trace  buttonModifier?: ButtonModifier;  差异内容：@Trace  buttonModifier?: ButtonModifier; | api/@hms.hds.HdsActionBar.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：HdsTabsAttribute；  API声明：blurStrategy(value: BlurStrategy): HdsTabsAttribute;  差异内容：blurStrategy(value: BlurStrategy): HdsTabsAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：HdsSideMenuMainItem；  API声明：updateBadge(badge?: HdsSideMenuBadgeParam): HdsSideMenuMainItem;  差异内容：updateBadge(badge?: HdsSideMenuBadgeParam): HdsSideMenuMainItem; | api/@hms.hds.HdsSideMenu.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：TitleBarStyleOptions；  API声明：blurStrategy?: BlurStrategy;  差异内容：blurStrategy?: BlurStrategy; | api/@hms.hds.hdsBaseComponent.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：HdsNavigationMenuContentOptions；  API声明：multiWindowEntryInAPPMenu?: MultiWindowEntryInAPPMenuParams;  差异内容：multiWindowEntryInAPPMenu?: MultiWindowEntryInAPPMenuParams; | api/@hms.hds.hdsBaseComponent.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：HdsNavigationTitleBarOptions；  API声明：enableComponentSafeArea?: boolean;  差异内容：enableComponentSafeArea?: boolean; | api/@hms.hds.hdsBaseComponent.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：DynamicHideParams；  API声明：hideRatio?: number;  差异内容：hideRatio?: number; | api/@hms.hds.hdsBaseComponent.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：SelectStyle；  API声明：showDefaultSelectedIcon?: boolean;  差异内容：showDefaultSelectedIcon?: boolean; | api/@hms.hds.hdsBaseComponent.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ActionBarButtonOptions；  API声明：buttonModifier?: ButtonModifier;  差异内容：buttonModifier?: ButtonModifier; | api/@hms.hds.HdsActionBar.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：HdsSideMenuMainItemParam；  API声明：badge?: HdsSideMenuBadgeParam;  差异内容：badge?: HdsSideMenuBadgeParam; | api/@hms.hds.HdsSideMenu.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：SnackBarStyleOptions；  API声明：blurStrategy?: BlurStrategy;  差异内容：blurStrategy?: BlurStrategy; | api/@hms.hds.HdsSnackBar.d.ets |
| 新增导出符号 | 类名：global；  API声明：export declare interface MultiWindowEntryInAPPStyle  差异内容：NA | 类名：global；  API声明：  差异内容：export declare interface MultiWindowEntryInAPPStyle | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增导出符号 | 类名：global；  API声明：export declare type MultiWindowEntryInAPPInterface = (params: MultiWindowEntryInAPPParams) => MultiWindowEntryInAPPAttribute;  差异内容：NA | 类名：global；  API声明：  差异内容：export declare type MultiWindowEntryInAPPInterface = (params: MultiWindowEntryInAPPParams) => MultiWindowEntryInAPPAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
