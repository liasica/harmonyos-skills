---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-b123sp18
title: ArkUI
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > API变更清单 > ArkUI
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:46+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:0e3a2b32f2ef855b59182f5b85b3334ed5ec56cbb81d06611b688ac1716ede09
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API卡片权限变更 | 类名：RichEditorAttribute；  API声明：copyOptions(value: CopyOptions): RichEditorAttribute;  差异内容：form | 类名：RichEditorAttribute；  API声明：copyOptions(value: CopyOptions): RichEditorAttribute;  差异内容：NA | component/rich\_editor.d.ts |
| API废弃版本变更 | 类名：ChipGroupItemOptions；  API声明：suffixIcon?: IconOptions;  差异内容：NA | 类名：ChipGroupItemOptions；  API声明：suffixIcon?: IconOptions;  差异内容：14 | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| API废弃版本变更 | 类名：CommonMethod；  API声明：gridSpan(value: number): T;  差异内容：NA | 类名：CommonMethod；  API声明：gridSpan(value: number): T;  差异内容：14 | component/common.d.ts |
| API废弃版本变更 | 类名：CommonMethod；  API声明：gridOffset(value: number): T;  差异内容：NA | 类名：CommonMethod；  API声明：gridOffset(value: number): T;  差异内容：14 | component/common.d.ts |
| 函数变更 | 类名：Scroller；  API声明：scrollPage(value: {  next: boolean;  });  差异内容：value: {  next: boolean;  } | 类名：Scroller；  API声明：scrollPage(value: ScrollPageOptions);  差异内容：value: ScrollPageOptions | component/scroll.d.ts |
| 函数变更 | 类名：NavDestinationAttribute；  API声明：title(value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle, options?: NavigationTitleOptions): NavDestinationAttribute;  差异内容：value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle | 类名：NavDestinationAttribute；  API声明：title(value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle | Resource, options?: NavigationTitleOptions): NavDestinationAttribute;  差异内容：value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle | Resource | component/nav\_destination.d.ts |
| 属性变更 | 类名：IconGroupSuffix；  API声明：@Require  @Prop  items: Array<IconItemOptions | SymbolGlyphModifier>;  差异内容：Array<IconItemOptions | SymbolGlyphModifier> | 类名：IconGroupSuffix；  API声明：@Require  @Prop  items: Array<IconItemOptions | SymbolGlyphModifier | SymbolItemOptions>;  差异内容：Array<IconItemOptions | SymbolGlyphModifier | SymbolItemOptions> | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 属性变更 | 类名：NavigationCommonTitle；  API声明：main: string;  差异内容：string | 类名：NavigationCommonTitle；  API声明：main: string | Resource;  差异内容：string,Resource | component/navigation.d.ts |
| 属性变更 | 类名：NavigationCommonTitle；  API声明：sub: string;  差异内容：string | 类名：NavigationCommonTitle；  API声明：sub: string | Resource;  差异内容：string,Resource | component/navigation.d.ts |
| 属性变更 | 类名：NavigationMenuItem；  API声明：value: string;  差异内容：string | 类名：NavigationMenuItem；  API声明：value: string | Resource;  差异内容：string,Resource | component/navigation.d.ts |
| 属性变更 | 类名：NavigationMenuItem；  API声明：icon?: string;  差异内容：string | 类名：NavigationMenuItem；  API声明：icon?: string | Resource;  差异内容：string,Resource | component/navigation.d.ts |
| 属性变更 | 类名：NavDestinationCommonTitle；  API声明：main: string;  差异内容：string | 类名：NavDestinationCommonTitle；  API声明：main: string | Resource;  差异内容：string,Resource | component/nav\_destination.d.ts |
| 属性变更 | 类名：NavDestinationCommonTitle；  API声明：sub: string;  差异内容：string | 类名：NavDestinationCommonTitle；  API声明：sub: string | Resource;  差异内容：string,Resource | component/nav\_destination.d.ts |
| 自定义类型变更 | 类名：global；  API声明：declare type StyledStringValue = TextStyle | DecorationStyle | BaselineOffsetStyle | LetterSpacingStyle | TextShadowStyle | GestureStyle | ImageAttachment | ParagraphStyle | LineHeightStyle | CustomSpan | UserDataSpan;  差异内容：TextStyle | DecorationStyle | BaselineOffsetStyle | LetterSpacingStyle | TextShadowStyle | GestureStyle | ImageAttachment | ParagraphStyle | LineHeightStyle | CustomSpan | UserDataSpan | 类名：global；  API声明：declare type StyledStringValue = TextStyle | DecorationStyle | BaselineOffsetStyle | LetterSpacingStyle | TextShadowStyle | GestureStyle | ImageAttachment | ParagraphStyle | LineHeightStyle | UrlStyle | CustomSpan | UserDataSpan | BackgroundColorStyle;  差异内容：TextStyle | DecorationStyle | BaselineOffsetStyle | LetterSpacingStyle | TextShadowStyle | GestureStyle | ImageAttachment | ParagraphStyle | LineHeightStyle | UrlStyle | CustomSpan | UserDataSpan | BackgroundColorStyle | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare enum SplitPolicy  差异内容： export declare enum SplitPolicy | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：SplitPolicy；  API声明：HOME\_PAGE = 0  差异内容：HOME\_PAGE = 0 | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：SplitPolicy；  API声明：DETAIL\_PAGE = 1  差异内容：DETAIL\_PAGE = 1 | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：SplitPolicy；  API声明：FULL\_PAGE = 2  差异内容：FULL\_PAGE = 2 | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct MultiNavigation  差异内容： export declare struct MultiNavigation | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavigation；  API声明：@State  multiStack: MultiNavPathStack;  差异内容：@State  multiStack: MultiNavPathStack; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavigation；  API声明：@BuilderParam  navDestination: NavDestinationBuildFunction;  差异内容：@BuilderParam  navDestination: NavDestinationBuildFunction; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavigation；  API声明：onNavigationModeChange?: OnNavigationModeChangeCallback;  差异内容：onNavigationModeChange?: OnNavigationModeChangeCallback; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavigation；  API声明：onHomeShowOnTop?: OnHomeShowOnTopCallback;  差异内容：onHomeShowOnTop?: OnHomeShowOnTopCallback; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class MultiNavPathStack  差异内容： export declare class MultiNavPathStack | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：pushPath(info: NavPathInfo, animated?: boolean, policy?: SplitPolicy): void;  差异内容：pushPath(info: NavPathInfo, animated?: boolean, policy?: SplitPolicy): void; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：pushPath(info: NavPathInfo, options?: NavigationOptions, policy?: SplitPolicy): void;  差异内容：pushPath(info: NavPathInfo, options?: NavigationOptions, policy?: SplitPolicy): void; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：pushPathByName(name: string, param: Object, animated?: boolean, policy?: SplitPolicy): void;  差异内容：pushPathByName(name: string, param: Object, animated?: boolean, policy?: SplitPolicy): void; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：pushPathByName(name: string, param: Object, onPop?: base.Callback<PopInfo>, animated?: boolean, policy?: SplitPolicy): void;  差异内容：pushPathByName(name: string, param: Object, onPop?: base.Callback<PopInfo>, animated?: boolean, policy?: SplitPolicy): void; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：replacePath(info: NavPathInfo, animated?: boolean): void;  差异内容：replacePath(info: NavPathInfo, animated?: boolean): void; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：replacePath(info: NavPathInfo, options?: NavigationOptions): void;  差异内容：replacePath(info: NavPathInfo, options?: NavigationOptions): void; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：replacePathByName(name: string, param: Object, animated?: boolean): void;  差异内容：replacePathByName(name: string, param: Object, animated?: boolean): void; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：removeByIndexes(indexes: Array<number>): number;  差异内容：removeByIndexes(indexes: Array<number>): number; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：removeByName(name: string): number;  差异内容：removeByName(name: string): number; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：pop(animated?: boolean): NavPathInfo | undefined;  差异内容：pop(animated?: boolean): NavPathInfo | undefined; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：pop(result?: Object, animated?: boolean): NavPathInfo | undefined;  差异内容：pop(result?: Object, animated?: boolean): NavPathInfo | undefined; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：popToName(name: string, animated?: boolean): number;  差异内容：popToName(name: string, animated?: boolean): number; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：popToName(name: string, result: Object, animated?: boolean): number;  差异内容：popToName(name: string, result: Object, animated?: boolean): number; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：popToIndex(index: number, animated?: boolean): void;  差异内容：popToIndex(index: number, animated?: boolean): void; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：popToIndex(index: number, result: Object, animated?: boolean): void;  差异内容：popToIndex(index: number, result: Object, animated?: boolean): void; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：moveToTop(name: string, animated?: boolean): number;  差异内容：moveToTop(name: string, animated?: boolean): number; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：moveIndexToTop(index: number, animated?: boolean): void;  差异内容：moveIndexToTop(index: number, animated?: boolean): void; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：clear(animated?: boolean): void;  差异内容：clear(animated?: boolean): void; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：getAllPathName(): Array<string>;  差异内容：getAllPathName(): Array<string>; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：getParamByIndex(index: number): Object | undefined;  差异内容：getParamByIndex(index: number): Object | undefined; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：getParamByName(name: string): Array<Object>;  差异内容：getParamByName(name: string): Array<Object>; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：getIndexByName(name: string): Array<number>;  差异内容：getIndexByName(name: string): Array<number>; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：size(): number;  差异内容：size(): number; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：disableAnimation(disable: boolean): void;  差异内容：disableAnimation(disable: boolean): void; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：switchFullScreenState(isFullScreen?: boolean): boolean;  差异内容：switchFullScreenState(isFullScreen?: boolean): boolean; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：setHomeWidthRange(minPercent: number, maxPercent: number): void;  差异内容：setHomeWidthRange(minPercent: number, maxPercent: number): void; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：keepBottomPage(keepBottom: boolean): void;  差异内容：keepBottomPage(keepBottom: boolean): void; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：MultiNavPathStack；  API声明：setPlaceholderPage(info: NavPathInfo): void;  差异内容：setPlaceholderPage(info: NavPathInfo): void; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：global；  API声明：declare type NavDestinationBuildFunction = (name: string, param?: object) => void;  差异内容：declare type NavDestinationBuildFunction = (name: string, param?: object) => void; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：global；  API声明：declare type OnNavigationModeChangeCallback = (mode: NavigationMode) => void;  差异内容：declare type OnNavigationModeChangeCallback = (mode: NavigationMode) => void; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：global；  API声明：declare type OnHomeShowOnTopCallback = (name: string) => void;  差异内容：declare type OnHomeShowOnTopCallback = (name: string) => void; | api/@ohos.arkui.advanced.MultiNavigation.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface SuffixImageIconOptions  差异内容： export interface SuffixImageIconOptions | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：SuffixImageIconOptions；  API声明：action?: VoidCallback;  差异内容：action?: VoidCallback; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：SuffixImageIconOptions；  API声明：accessibilityText?: ResourceStr;  差异内容：accessibilityText?: ResourceStr; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：SuffixImageIconOptions；  API声明：accessibilityDescription?: ResourceStr;  差异内容：accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：SuffixImageIconOptions；  API声明：accessibilityLevel?: string;  差异内容：accessibilityLevel?: string; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroupItemOptions；  API声明：suffixImageIcon?: SuffixImageIconOptions;  差异内容：suffixImageIcon?: SuffixImageIconOptions; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroupItemOptions；  API声明：suffixSymbolOptions?: ChipSuffixSymbolGlyphOptions;  差异内容：suffixSymbolOptions?: ChipSuffixSymbolGlyphOptions; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroupItemOptions；  API声明：closeOptions?: CloseOptions;  差异内容：closeOptions?: CloseOptions; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroupItemOptions；  API声明：accessibilityDescription?: ResourceStr;  差异内容：accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroupItemOptions；  API声明：accessibilityLevel?: string;  差异内容：accessibilityLevel?: string; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：IconItemOptions；  API声明：accessibilityText?: ResourceStr;  差异内容：accessibilityText?: ResourceStr; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：IconItemOptions；  API声明：accessibilityDescription?: ResourceStr;  差异内容：accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：IconItemOptions；  API声明：accessibilityLevel?: string;  差异内容：accessibilityLevel?: string; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface SymbolItemOptions  差异内容： export interface SymbolItemOptions | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：SymbolItemOptions；  API声明：symbol: SymbolGlyphModifier;  差异内容：symbol: SymbolGlyphModifier; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：SymbolItemOptions；  API声明：action: VoidCallback;  差异内容：action: VoidCallback; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：SymbolItemOptions；  API声明：accessibilityText?: ResourceStr;  差异内容：accessibilityText?: ResourceStr; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：SymbolItemOptions；  API声明：accessibilityDescription?: ResourceStr;  差异内容：accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：SymbolItemOptions；  API声明：accessibilityLevel?: string;  差异内容：accessibilityLevel?: string; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：Window；  API声明：setSubWindowModal(isModal: boolean, modalityType: ModalityType): Promise<void>;  差异内容：setSubWindowModal(isModal: boolean, modalityType: ModalityType): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明： interface DecorButtonStyle  差异内容： interface DecorButtonStyle | api/@ohos.window.d.ts |
| 新增API | NA | 类名：DecorButtonStyle；  API声明：colorMode?: ConfigurationConstant.ColorMode;  差异内容：colorMode?: ConfigurationConstant.ColorMode; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：DecorButtonStyle；  API声明：buttonBackgroundSize?: number;  差异内容：buttonBackgroundSize?: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：DecorButtonStyle；  API声明：spacingBetweenButtons?: number;  差异内容：spacingBetweenButtons?: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：DecorButtonStyle；  API声明：closeButtonRightMargin?: number;  差异内容：closeButtonRightMargin?: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：function getWindowsByCoordinate(displayId: number, windowNumber?: number, x?: number, y?: number): Promise<Array<Window>>;  差异内容：function getWindowsByCoordinate(displayId: number, windowNumber?: number, x?: number, y?: number): Promise<Array<Window>>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：MaximizePresentation；  API声明：ENTER\_IMMERSIVE\_DISABLE\_TITLE\_AND\_DOCK\_HOVER = 3  差异内容：ENTER\_IMMERSIVE\_DISABLE\_TITLE\_AND\_DOCK\_HOVER = 3 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：on(type: 'displayIdChange', callback: Callback<number>): void;  差异内容：on(type: 'displayIdChange', callback: Callback<number>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：off(type: 'displayIdChange', callback?: Callback<number>): void;  差异内容：off(type: 'displayIdChange', callback?: Callback<number>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：setWindowTopmost(isWindowTopmost: boolean): Promise<void>;  差异内容：setWindowTopmost(isWindowTopmost: boolean): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：raiseToAppTop(): Promise<void>;  差异内容：raiseToAppTop(): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：setRaiseByClickEnabled(enable: boolean): Promise<void>;  差异内容：setRaiseByClickEnabled(enable: boolean): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：setResizeByDragEnabled(enable: boolean, callback: AsyncCallback<void>): void;  差异内容：setResizeByDragEnabled(enable: boolean, callback: AsyncCallback<void>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：setResizeByDragEnabled(enable: boolean): Promise<void>;  差异内容：setResizeByDragEnabled(enable: boolean): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：restore(): Promise<void>;  差异内容：restore(): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：setWindowTitleMoveEnabled(enabled: boolean): void;  差异内容：setWindowTitleMoveEnabled(enabled: boolean): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：setDecorButtonStyle(dectorStyle: DecorButtonStyle): void;  差异内容：setDecorButtonStyle(dectorStyle: DecorButtonStyle): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：getDecorButtonStyle(): DecorButtonStyle;  差异内容：getDecorButtonStyle(): DecorButtonStyle; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：setWindowTitleButtonVisible(isMaximizeButtonVisible: boolean, isMinimizeButtonVisible: boolean, isCloseButtonVisible?: boolean): void;  差异内容：setWindowTitleButtonVisible(isMaximizeButtonVisible: boolean, isMinimizeButtonVisible: boolean, isCloseButtonVisible?: boolean): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：startMoving(): Promise<void>;  差异内容：startMoving(): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：setTitleAndDockHoverShown(isTitleHoverShown?: boolean, isDockHoverShown?: boolean): Promise<void>;  差异内容：setTitleAndDockHoverShown(isTitleHoverShown?: boolean, isDockHoverShown?: boolean): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明： enum ModalityType  差异内容： enum ModalityType | api/@ohos.window.d.ts |
| 新增API | NA | 类名：ModalityType；  API声明：WINDOW\_MODALITY = 0  差异内容：WINDOW\_MODALITY = 0 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：ModalityType；  API声明：APPLICATION\_MODALITY = 1  差异内容：APPLICATION\_MODALITY = 1 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：SubWindowOptions；  API声明：modalityType?: ModalityType;  差异内容：modalityType?: ModalityType; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStage；  API声明：on(eventType: 'windowStageClose', callback: Callback<void>): void;  差异内容：on(eventType: 'windowStageClose', callback: Callback<void>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStage；  API声明：off(eventType: 'windowStageClose', callback?: Callback<void>): void;  差异内容：off(eventType: 'windowStageClose', callback?: Callback<void>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStage；  API声明：removeStartingWindow(): Promise<void>;  差异内容：removeStartingWindow(): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStage；  API声明：setWindowModal(isModal: boolean): Promise<void>;  差异内容：setWindowModal(isModal: boolean): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStage；  API声明：setWindowRectAutoSave(enabled: boolean): Promise<void>;  差异内容：setWindowRectAutoSave(enabled: boolean): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStage；  API声明：isWindowRectAutoSave(): Promise<boolean>;  差异内容：isWindowRectAutoSave(): Promise<boolean>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'Marquee'): Marquee;  差异内容：function createNode(context: UIContext, nodeType: 'Marquee'): Marquee; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'TextArea'): TextArea;  差异内容：function createNode(context: UIContext, nodeType: 'TextArea'): TextArea; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'SymbolGlyph'): SymbolGlyph;  差异内容：function createNode(context: UIContext, nodeType: 'SymbolGlyph'): SymbolGlyph; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'QRCode'): QRCode;  差异内容：function createNode(context: UIContext, nodeType: 'QRCode'): QRCode; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'Badge'): Badge;  差异内容：function createNode(context: UIContext, nodeType: 'Badge'): Badge; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'TextClock'): TextClock;  差异内容：function createNode(context: UIContext, nodeType: 'TextClock'): TextClock; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'TextTimer'): TextTimer;  差异内容：function createNode(context: UIContext, nodeType: 'TextTimer'): TextTimer; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'Grid'): Grid;  差异内容：function createNode(context: UIContext, nodeType: 'Grid'): Grid; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'GridItem'): GridItem;  差异内容：function createNode(context: UIContext, nodeType: 'GridItem'): GridItem; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type Marquee = TypedFrameNode<MarqueeInterface, MarqueeAttribute>;  差异内容：type Marquee = TypedFrameNode<MarqueeInterface, MarqueeAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type TextArea = TypedFrameNode<TextAreaInterface, TextAreaAttribute>;  差异内容：type TextArea = TypedFrameNode<TextAreaInterface, TextAreaAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type SymbolGlyph = TypedFrameNode<SymbolGlyphInterface, SymbolGlyphAttribute>;  差异内容：type SymbolGlyph = TypedFrameNode<SymbolGlyphInterface, SymbolGlyphAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type QRCode = TypedFrameNode<QRCodeInterface, QRCodeAttribute>;  差异内容：type QRCode = TypedFrameNode<QRCodeInterface, QRCodeAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type Badge = TypedFrameNode<BadgeInterface, BadgeAttribute>;  差异内容：type Badge = TypedFrameNode<BadgeInterface, BadgeAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type TextClock = TypedFrameNode<TextClockInterface, TextClockAttribute>;  差异内容：type TextClock = TypedFrameNode<TextClockInterface, TextClockAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type TextTimer = TypedFrameNode<TextTimerInterface, TextTimerAttribute>;  差异内容：type TextTimer = TypedFrameNode<TextTimerInterface, TextTimerAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type Grid = TypedFrameNode<GridInterface, GridAttribute>;  差异内容：type Grid = TypedFrameNode<GridInterface, GridAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type GridItem = TypedFrameNode<GridItemInterface, GridItemAttribute>;  差异内容：type GridItem = TypedFrameNode<GridItemInterface, GridItemAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：focusScopeId(id: string, isGroup?: boolean, arrowStepOut?: boolean): T;  差异内容：focusScopeId(id: string, isGroup?: boolean, arrowStepOut?: boolean): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：useEffect(useEffect: boolean, effectType: EffectType): T;  差异内容：useEffect(useEffect: boolean, effectType: EffectType): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：accessibilityGroup(isGroup: boolean, accessibilityOptions: AccessibilityOptions): T;  差异内容：accessibilityGroup(isGroup: boolean, accessibilityOptions: AccessibilityOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum EffectType  差异内容： declare enum EffectType | component/common.d.ts |
| 新增API | NA | 类名：EffectType；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | component/common.d.ts |
| 新增API | NA | 类名：EffectType；  API声明：WINDOW\_EFFECT = 1  差异内容：WINDOW\_EFFECT = 1 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum BlurStyleActivePolicy  差异内容： declare enum BlurStyleActivePolicy | component/common.d.ts |
| 新增API | NA | 类名：BlurStyleActivePolicy；  API声明：FOLLOWS\_WINDOW\_ACTIVE\_STATE = 0  差异内容：FOLLOWS\_WINDOW\_ACTIVE\_STATE = 0 | component/common.d.ts |
| 新增API | NA | 类名：BlurStyleActivePolicy；  API声明：ALWAYS\_ACTIVE = 1  差异内容：ALWAYS\_ACTIVE = 1 | component/common.d.ts |
| 新增API | NA | 类名：BlurStyleActivePolicy；  API声明：ALWAYS\_INACTIVE = 2  差异内容：ALWAYS\_INACTIVE = 2 | component/common.d.ts |
| 新增API | NA | 类名：BackgroundBlurStyleOptions；  API声明：policy?: BlurStyleActivePolicy;  差异内容：policy?: BlurStyleActivePolicy; | component/common.d.ts |
| 新增API | NA | 类名：BackgroundBlurStyleOptions；  API声明：inactiveColor?: ResourceColor;  差异内容：inactiveColor?: ResourceColor; | component/common.d.ts |
| 新增API | NA | 类名：BackgroundEffectOptions；  API声明：policy?: BlurStyleActivePolicy;  差异内容：policy?: BlurStyleActivePolicy; | component/common.d.ts |
| 新增API | NA | 类名：BackgroundEffectOptions；  API声明：inactiveColor?: ResourceColor;  差异内容：inactiveColor?: ResourceColor; | component/common.d.ts |
| 新增API | NA | 类名：KeyEvent；  API声明：unicode?: number;  差异内容：unicode?: number; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：enableHoverMode?: boolean;  差异内容：enableHoverMode?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：hoverModeArea?: HoverModeAreaType;  差异内容：hoverModeArea?: HoverModeAreaType; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface FadingEdgeOptions  差异内容： declare interface FadingEdgeOptions | component/common.d.ts |
| 新增API | NA | 类名：FadingEdgeOptions；  API声明：fadingEdgeLength?: LengthMetrics;  差异内容：fadingEdgeLength?: LengthMetrics; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：chainWeight(chainWeight: ChainWeightOptions): T;  差异内容：chainWeight(chainWeight: ChainWeightOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：safeAreaPadding(paddingValue: Padding | LengthMetrics | LocalizedPadding): T;  差异内容：safeAreaPadding(paddingValue: Padding | LengthMetrics | LocalizedPadding): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：tabStop(isTabStop: boolean): T;  差异内容：tabStop(isTabStop: boolean): T; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ContentClipMode  差异内容： declare enum ContentClipMode | component/common.d.ts |
| 新增API | NA | 类名：ContentClipMode；  API声明：CONTENT\_ONLY = 0  差异内容：CONTENT\_ONLY = 0 | component/common.d.ts |
| 新增API | NA | 类名：ContentClipMode；  API声明：BOUNDARY = 1  差异内容：BOUNDARY = 1 | component/common.d.ts |
| 新增API | NA | 类名：ContentClipMode；  API声明：SAFE\_AREA = 2  差异内容：SAFE\_AREA = 2 | component/common.d.ts |
| 新增API | NA | 类名：ScrollableCommonMethod；  API声明：fadingEdge(enabled: Optional<boolean>, options?: FadingEdgeOptions): T;  差异内容：fadingEdge(enabled: Optional<boolean>, options?: FadingEdgeOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：ScrollableCommonMethod；  API声明：clipContent(clip: ContentClipMode | RectShape): T;  差异内容：clipContent(clip: ContentClipMode | RectShape): T; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum HoverModeAreaType  差异内容： declare enum HoverModeAreaType | component/common.d.ts |
| 新增API | NA | 类名：HoverModeAreaType；  API声明：TOP\_SCREEN = 0  差异内容：TOP\_SCREEN = 0 | component/common.d.ts |
| 新增API | NA | 类名：HoverModeAreaType；  API声明：BOTTOM\_SCREEN = 1  差异内容：BOTTOM\_SCREEN = 1 | component/common.d.ts |
| 新增API | NA | 类名：GridAttribute；  API声明：cachedCount(count: number, show: boolean): GridAttribute;  差异内容：cachedCount(count: number, show: boolean): GridAttribute; | component/grid.d.ts |
| 新增API | NA | 类名：ListAttribute；  API声明：cachedCount(count: number, show: boolean): ListAttribute;  差异内容：cachedCount(count: number, show: boolean): ListAttribute; | component/list.d.ts |
| 新增API | NA | 类名：ListScroller；  API声明：getVisibleListContentInfo(x: number, y: number): VisibleListContentInfo;  差异内容：getVisibleListContentInfo(x: number, y: number): VisibleListContentInfo; | component/list.d.ts |
| 新增API | NA | 类名：BarStyle；  API声明：SAFE\_AREA\_PADDING = 2  差异内容：SAFE\_AREA\_PADDING = 2 | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationToolbarOptions；  API声明：barStyle?: BarStyle;  差异内容：barStyle?: BarStyle; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationAttribute；  API声明：recoverable(recoverable: Optional<boolean>): NavigationAttribute;  差异内容：recoverable(recoverable: Optional<boolean>): NavigationAttribute; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationAttribute；  API声明：enableDragBar(isEnabled: Optional<boolean>): NavigationAttribute;  差异内容：enableDragBar(isEnabled: Optional<boolean>): NavigationAttribute; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum NavigationSystemTransitionType  差异内容： declare enum NavigationSystemTransitionType | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavigationSystemTransitionType；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavigationSystemTransitionType；  API声明：NONE = 1  差异内容：NONE = 1 | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavigationSystemTransitionType；  API声明：TITLE = 2  差异内容：TITLE = 2 | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavigationSystemTransitionType；  API声明：CONTENT = 3  差异内容：CONTENT = 3 | component/nav\_destination.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface NestedScrollInfo  差异内容： declare interface NestedScrollInfo | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NestedScrollInfo；  API声明：parent: Scroller;  差异内容：parent: Scroller; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NestedScrollInfo；  API声明：child: Scroller;  差异内容：child: Scroller; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationAttribute；  API声明：systemTransition(type: NavigationSystemTransitionType): NavDestinationAttribute;  差异内容：systemTransition(type: NavigationSystemTransitionType): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationAttribute；  API声明：recoverable(recoverable: Optional<boolean>): NavDestinationAttribute;  差异内容：recoverable(recoverable: Optional<boolean>): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationAttribute；  API声明：bindToScrollable(scrollers: Array<Scroller>): NavDestinationAttribute;  差异内容：bindToScrollable(scrollers: Array<Scroller>): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationAttribute；  API声明：bindToNestedScrollable(scrollInfos: Array<NestedScrollInfo>): NavDestinationAttribute;  差异内容：bindToNestedScrollable(scrollInfos: Array<NestedScrollInfo>): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：RichEditorImageSpanOptions；  API声明：onHover?: OnHoverCallback;  差异内容：onHover?: OnHoverCallback; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type OnHoverCallback = (status: boolean, event: HoverEvent) => void;  差异内容：declare type OnHoverCallback = (status: boolean, event: HoverEvent) => void; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：Scroller；  API声明：getItemIndex(x: number, y: number): number;  差异内容：getItemIndex(x: number, y: number): number; | component/scroll.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ScrollPageOptions  差异内容： declare interface ScrollPageOptions | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollPageOptions；  API声明：next: boolean;  差异内容：next: boolean; | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollPageOptions；  API声明：animation?: boolean;  差异内容：animation?: boolean; | component/scroll.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：onSubmit(callback: SearchSubmitCallback): SearchAttribute;  差异内容：onSubmit(callback: SearchSubmitCallback): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type SearchSubmitCallback = (searchContent: string, event?: SubmitEvent) => void;  差异内容：declare type SearchSubmitCallback = (searchContent: string, event?: SubmitEvent) => void; | component/search.d.ts |
| 新增API | NA | 类名：StyledString；  API声明：static toHtml(styledString: StyledString): string;  差异内容：static toHtml(styledString: StyledString): string; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class BackgroundColorStyle  差异内容： declare class BackgroundColorStyle | component/styled\_string.d.ts |
| 新增API | NA | 类名：BackgroundColorStyle；  API声明：readonly textBackgroundStyle: TextBackgroundStyle;  差异内容：readonly textBackgroundStyle: TextBackgroundStyle; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class UrlStyle  差异内容： declare class UrlStyle | component/styled\_string.d.ts |
| 新增API | NA | 类名：UrlStyle；  API声明：readonly url: string;  差异内容：readonly url: string; | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyledStringKey；  API声明：BACKGROUND\_COLOR = 6  差异内容：BACKGROUND\_COLOR = 6 | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyledStringKey；  API声明：URL = 7  差异内容：URL = 7 | component/styled\_string.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：onSubmit(callback: TextAreaSubmitCallback): TextAreaAttribute;  差异内容：onSubmit(callback: TextAreaSubmitCallback): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type TextAreaSubmitCallback = (enterKeyType: EnterKeyType, event?: SubmitEvent) => void;  差异内容：declare type TextAreaSubmitCallback = (enterKeyType: EnterKeyType, event?: SubmitEvent) => void; | component/text\_area.d.ts |
| 新增API | NA | 类名：WaterFlowAttribute；  API声明：cachedCount(count: number, show: boolean): WaterFlowAttribute;  差异内容：cachedCount(count: number, show: boolean): WaterFlowAttribute; | component/water\_flow.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare enum AccessibilitySelectedType  差异内容： export declare enum AccessibilitySelectedType | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：AccessibilitySelectedType；  API声明：CLICKED = 0  差异内容：CLICKED = 0 | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：AccessibilitySelectedType；  API声明：CHECKED = 1  差异内容：CHECKED = 1 | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：AccessibilitySelectedType；  API声明：SELECTED = 2  差异内容：SELECTED = 2 | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：SuffixIconOptions；  API声明：accessibilityText?: ResourceStr;  差异内容：accessibilityText?: ResourceStr; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：SuffixIconOptions；  API声明：accessibilityDescription?: ResourceStr;  差异内容：accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：SuffixIconOptions；  API声明：accessibilityLevel?: string;  差异内容：accessibilityLevel?: string; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface AccessibilityOptions  差异内容： export interface AccessibilityOptions | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：AccessibilityOptions；  API声明：accessibilityLevel?: string;  差异内容：accessibilityLevel?: string; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：AccessibilityOptions；  API声明：accessibilityText?: ResourceStr;  差异内容：accessibilityText?: ResourceStr; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：AccessibilityOptions；  API声明：accessibilityDescription?: ResourceStr;  差异内容：accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface CloseOptions  差异内容： export interface CloseOptions | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface ChipSuffixSymbolGlyphOptions  差异内容： export interface ChipSuffixSymbolGlyphOptions | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipSuffixSymbolGlyphOptions；  API声明：normalAccessibility?: AccessibilityOptions;  差异内容：normalAccessibility?: AccessibilityOptions; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipSuffixSymbolGlyphOptions；  API声明：activatedAccessibility?: AccessibilityOptions;  差异内容：activatedAccessibility?: AccessibilityOptions; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipSuffixSymbolGlyphOptions；  API声明：action?: VoidCallback;  差异内容：action?: VoidCallback; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipOptions；  API声明：suffixSymbolOptions?: ChipSuffixSymbolGlyphOptions;  差异内容：suffixSymbolOptions?: ChipSuffixSymbolGlyphOptions; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipOptions；  API声明：closeOptions?: CloseOptions;  差异内容：closeOptions?: CloseOptions; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipOptions；  API声明：accessibilityDescription?: ResourceStr;  差异内容：accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipOptions；  API声明：accessibilityLevel?: string;  差异内容：accessibilityLevel?: string; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipOptions；  API声明：accessibilitySelectedType?: AccessibilitySelectedType;  差异内容：accessibilitySelectedType?: AccessibilitySelectedType; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct PopoverDialog  差异内容： export declare struct PopoverDialog | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：PopoverDialog；  API声明：@Link  visible: boolean;  差异内容：@Link  visible: boolean; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：PopoverDialog；  API声明：@Require  @Prop  popover: PopoverOptions;  差异内容：@Require  @Prop  popover: PopoverOptions; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：PopoverDialog；  API声明：@Require  @BuilderParam  targetBuilder: Callback<void>;  差异内容：@Require  @BuilderParam  targetBuilder: Callback<void>; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare interface PopoverOptions  差异内容： export declare interface PopoverOptions | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：SegmentButton；  API声明：@Prop  maxFontScale: number | Resource;  差异内容：@Prop  maxFontScale: number | Resource; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：global；  API声明： export class MarqueeDynamicSyncScene  差异内容： export class MarqueeDynamicSyncScene | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：MarqueeDynamicSyncScene；  API声明：readonly type: MarqueeDynamicSyncSceneType;  差异内容：readonly type: MarqueeDynamicSyncSceneType; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：FocusController；  API声明：setAutoFocusTransfer(isAutoFocusTransfer: boolean): void;  差异内容：setAutoFocusTransfer(isAutoFocusTransfer: boolean): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：FocusController；  API声明：activate(isActive: boolean, autoInactive?: boolean): void;  差异内容：activate(isActive: boolean, autoInactive?: boolean): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：KeyboardAvoidMode；  API声明：OFFSET\_WITH\_CARET = 2  差异内容：OFFSET\_WITH\_CARET = 2 | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：KeyboardAvoidMode；  API声明：RESIZE\_WITH\_CARET = 3  差异内容：RESIZE\_WITH\_CARET = 3 | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：KeyboardAvoidMode；  API声明：NONE = 4  差异内容：NONE = 4 | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export const enum MarqueeDynamicSyncSceneType  差异内容： export const enum MarqueeDynamicSyncSceneType | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：MarqueeDynamicSyncSceneType；  API声明：ANIMATION = 1  差异内容：ANIMATION = 1 | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：WindowProxy；  API声明：on(type: 'rectChange', reasons: number, callback: Callback<RectChangeOptions>): void;  差异内容：on(type: 'rectChange', reasons: number, callback: Callback<RectChangeOptions>): void; | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：WindowProxy；  API声明：off(type: 'rectChange', callback?: Callback<RectChangeOptions>): void;  差异内容：off(type: 'rectChange', callback?: Callback<RectChangeOptions>): void; | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：WindowProxy；  API声明：properties: WindowProxyProperties;  差异内容：properties: WindowProxyProperties; | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：uiExtension；  API声明： interface WindowProxyProperties  差异内容： interface WindowProxyProperties | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：WindowProxyProperties；  API声明：uiExtensionHostWindowProxyRect: window.Rect;  差异内容：uiExtensionHostWindowProxyRect: window.Rect; | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：uiExtension；  API声明： enum RectChangeReason  差异内容： enum RectChangeReason | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：RectChangeReason；  API声明：HOST\_WINDOW\_RECT\_CHANGE = 0x0001  差异内容：HOST\_WINDOW\_RECT\_CHANGE = 0x0001 | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：uiExtension；  API声明： interface RectChangeOptions  差异内容： interface RectChangeOptions | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：RectChangeOptions；  API声明：rect: window.Rect;  差异内容：rect: window.Rect; | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：RectChangeOptions；  API声明：reason: RectChangeReason;  差异内容：reason: RectChangeReason; | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：display；  API声明：function getPrimaryDisplaySync(): Display;  差异内容：function getPrimaryDisplaySync(): Display; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：ShowToastOptions；  API声明：enableHoverMode?: boolean;  差异内容：enableHoverMode?: boolean; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：ShowToastOptions；  API声明：hoverModeArea?: HoverModeAreaType;  差异内容：hoverModeArea?: HoverModeAreaType; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：ShowDialogOptions；  API声明：enableHoverMode?: boolean;  差异内容：enableHoverMode?: boolean; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：ShowDialogOptions；  API声明：hoverModeArea?: HoverModeAreaType;  差异内容：hoverModeArea?: HoverModeAreaType; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：BaseDialogOptions；  API声明：enableHoverMode?: boolean;  差异内容：enableHoverMode?: boolean; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：BaseDialogOptions；  API声明：hoverModeArea?: HoverModeAreaType;  差异内容：hoverModeArea?: HoverModeAreaType; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：RouterOptions；  API声明：recoverable?: boolean;  差异内容：recoverable?: boolean; | api/@ohos.router.d.ts |
| 新增API | NA | 类名：NamedRouterOptions；  API声明：recoverable?: boolean;  差异内容：recoverable?: boolean; | api/@ohos.router.d.ts |
| 新增API | NA | 类名：screenshot；  API声明：function capture(options?: CaptureOption): Promise<image.PixelMap>;  差异内容：function capture(options?: CaptureOption): Promise<image.PixelMap>; | api/@ohos.screenshot.d.ts |
| 新增API | NA | 类名：screenshot；  API声明： interface CaptureOption  差异内容： interface CaptureOption | api/@ohos.screenshot.d.ts |
| 新增API | NA | 类名：CaptureOption；  API声明：displayId?: number;  差异内容：displayId?: number; | api/@ohos.screenshot.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：enableHoverMode?: boolean;  差异内容：enableHoverMode?: boolean; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：hoverModeArea?: HoverModeAreaType;  差异内容：hoverModeArea?: HoverModeAreaType; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：AlertDialogParam；  API声明：enableHoverMode?: boolean;  差异内容：enableHoverMode?: boolean; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogParam；  API声明：hoverModeArea?: HoverModeAreaType;  差异内容：hoverModeArea?: HoverModeAreaType; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：CalendarDialogOptions；  API声明：enableHoverMode?: boolean;  差异内容：enableHoverMode?: boolean; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarDialogOptions；  API声明：hoverModeArea?: HoverModeAreaType;  差异内容：hoverModeArea?: HoverModeAreaType; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CustomDialogControllerOptions；  API声明：enableHoverMode?: boolean;  差异内容：enableHoverMode?: boolean; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：CustomDialogControllerOptions；  API声明：hoverModeArea?: HoverModeAreaType;  差异内容：hoverModeArea?: HoverModeAreaType; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface LunarSwitchStyle  差异内容： declare interface LunarSwitchStyle | component/date\_picker.d.ts |
| 新增API | NA | 类名：LunarSwitchStyle；  API声明：selectedColor?: ResourceColor;  差异内容：selectedColor?: ResourceColor; | component/date\_picker.d.ts |
| 新增API | NA | 类名：LunarSwitchStyle；  API声明：unselectedColor?: ResourceColor;  差异内容：unselectedColor?: ResourceColor; | component/date\_picker.d.ts |
| 新增API | NA | 类名：LunarSwitchStyle；  API声明：strokeColor?: ResourceColor;  差异内容：strokeColor?: ResourceColor; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：lunarSwitchStyle?: LunarSwitchStyle;  差异内容：lunarSwitchStyle?: LunarSwitchStyle; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：enableHoverMode?: boolean;  差异内容：enableHoverMode?: boolean; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：hoverModeArea?: HoverModeAreaType;  差异内容：hoverModeArea?: HoverModeAreaType; | component/date\_picker.d.ts |
| 新增API | NA | 类名：GestureInterface；  API声明：allowedTypes(types: Array<SourceTool>): T;  差异内容：allowedTypes(types: Array<SourceTool>): T; | component/gesture.d.ts |
| 新增API | NA | 类名：GestureHandler；  API声明：allowedTypes(types: Array<SourceTool>): T;  差异内容：allowedTypes(types: Array<SourceTool>): T; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ImageRotateOrientation  差异内容： declare enum ImageRotateOrientation | component/image.d.ts |
| 新增API | NA | 类名：ImageRotateOrientation；  API声明：AUTO = 0  差异内容：AUTO = 0 | component/image.d.ts |
| 新增API | NA | 类名：ImageRotateOrientation；  API声明：UP = 1  差异内容：UP = 1 | component/image.d.ts |
| 新增API | NA | 类名：ImageRotateOrientation；  API声明：RIGHT = 2  差异内容：RIGHT = 2 | component/image.d.ts |
| 新增API | NA | 类名：ImageRotateOrientation；  API声明：DOWN = 3  差异内容：DOWN = 3 | component/image.d.ts |
| 新增API | NA | 类名：ImageRotateOrientation；  API声明：LEFT = 4  差异内容：LEFT = 4 | component/image.d.ts |
| 新增API | NA | 类名：ImageAttribute；  API声明：orientation(orientation: ImageRotateOrientation): ImageAttribute;  差异内容：orientation(orientation: ImageRotateOrientation): ImageAttribute; | component/image.d.ts |
| 新增API | NA | 类名：ImageSpanAttribute；  API声明：colorFilter(filter: ColorFilter | DrawingColorFilter): ImageSpanAttribute;  差异内容：colorFilter(filter: ColorFilter | DrawingColorFilter): ImageSpanAttribute; | component/image\_span.d.ts |
| 新增API | NA | 类名：ScrollBarAttribute；  API声明：enableNestedScroll(enabled: Optional<boolean>): ScrollBarAttribute;  差异内容：enableNestedScroll(enabled: Optional<boolean>): ScrollBarAttribute; | component/scroll\_bar.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：caretColor(color: ResourceColor): TextAttribute;  差异内容：caretColor(color: ResourceColor): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：selectedBackgroundColor(color: ResourceColor): TextAttribute;  差异内容：selectedBackgroundColor(color: ResourceColor): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：LayoutManager；  API声明：getRectsForRange(range: TextRange, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>;  差异内容：getRectsForRange(range: TextRange, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type RectWidthStyle = import('../api/@ohos.graphics.text').default.RectWidthStyle;  差异内容：declare type RectWidthStyle = import('../api/@ohos.graphics.text').default.RectWidthStyle; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type RectHeightStyle = import('../api/@ohos.graphics.text').default.RectHeightStyle;  差异内容：declare type RectHeightStyle = import('../api/@ohos.graphics.text').default.RectHeightStyle; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type TextBox = import('../api/@ohos.graphics.text').default.TextBox;  差异内容：declare type TextBox = import('../api/@ohos.graphics.text').default.TextBox; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type TextPickerScrollStopCallback = (value: string | string[], index: number | number[]) => void;  差异内容：declare type TextPickerScrollStopCallback = (value: string | string[], index: number | number[]) => void; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerAttribute；  API声明：onScrollStop(callback: TextPickerScrollStopCallback): TextPickerAttribute;  差异内容：onScrollStop(callback: TextPickerScrollStopCallback): TextPickerAttribute; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerDialogOptions；  API声明：onScrollStop?: Callback<TextPickerResult>;  差异内容：onScrollStop?: Callback<TextPickerResult>; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerDialogOptions；  API声明：enableHoverMode?: boolean;  差异内容：enableHoverMode?: boolean; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerDialogOptions；  API声明：hoverModeArea?: HoverModeAreaType;  差异内容：hoverModeArea?: HoverModeAreaType; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TimePickerDialogOptions；  API声明：enableHoverMode?: boolean;  差异内容：enableHoverMode?: boolean; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerDialogOptions；  API声明：hoverModeArea?: HoverModeAreaType;  差异内容：hoverModeArea?: HoverModeAreaType; | component/time\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ChainWeightOptions  差异内容： declare interface ChainWeightOptions | component/units.d.ts |
| 新增API | NA | 类名：ChainWeightOptions；  API声明：horizontal?: number;  差异内容：horizontal?: number; | component/units.d.ts |
| 新增API | NA | 类名：ChainWeightOptions；  API声明：vertical?: number;  差异内容：vertical?: number; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface AccessibilityOptions  差异内容： declare interface AccessibilityOptions | component/units.d.ts |
| 新增API | NA | 类名：AccessibilityOptions；  API声明：accessibilityPreferred?: boolean;  差异内容：accessibilityPreferred?: boolean; | component/units.d.ts |
