---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-5111
title: ArkUI
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > ArkUI
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:51+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:38c0544c5a819625431267fdbe5e740d1a3fbc80c58d9516eb3f7c1037a0a626
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：window；  API声明：function getAllWindowLayoutInfo(displayId: number): Promise<Array<WindowLayoutInfo>>;  差异内容：1300002 | 类名：window；  API声明：function getAllWindowLayoutInfo(displayId: number): Promise<Array<WindowLayoutInfo>>;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：Window；  API声明：setSystemAvoidAreaEnabled(enabled: boolean): Promise<void>;  差异内容：401 | 类名：Window；  API声明：setSystemAvoidAreaEnabled(enabled: boolean): Promise<void>;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：Window；  API声明：on(type: 'keyboardDidShow', callback: Callback<KeyboardInfo>): void;  差异内容：401 | 类名：Window；  API声明：on(type: 'keyboardDidShow', callback: Callback<KeyboardInfo>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：Window；  API声明：off(type: 'keyboardDidShow', callback?: Callback<KeyboardInfo>): void;  差异内容：401 | 类名：Window；  API声明：off(type: 'keyboardDidShow', callback?: Callback<KeyboardInfo>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：Window；  API声明：on(type: 'keyboardDidHide', callback: Callback<KeyboardInfo>): void;  差异内容：401 | 类名：Window；  API声明：on(type: 'keyboardDidHide', callback: Callback<KeyboardInfo>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：Window；  API声明：off(type: 'keyboardDidHide', callback?: Callback<KeyboardInfo>): void;  差异内容：401 | 类名：Window；  API声明：off(type: 'keyboardDidHide', callback?: Callback<KeyboardInfo>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 新增API | NA | 类名：global；  API声明：interface LazyVGridLayoutInterface  差异内容：interface LazyVGridLayoutInterface | component/lazy\_grid\_layout.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class LazyGridLayoutAttribute  差异内容：declare class LazyGridLayoutAttribute | component/lazy\_grid\_layout.d.ts |
| 新增API | NA | 类名：LazyGridLayoutAttribute；  API声明：rowsGap(value: LengthMetrics): T;  差异内容：rowsGap(value: LengthMetrics): T; | component/lazy\_grid\_layout.d.ts |
| 新增API | NA | 类名：LazyGridLayoutAttribute；  API声明：columnsGap(value: LengthMetrics): T;  差异内容：columnsGap(value: LengthMetrics): T; | component/lazy\_grid\_layout.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class LazyVGridLayoutAttribute  差异内容：declare class LazyVGridLayoutAttribute | component/lazy\_grid\_layout.d.ts |
| 新增API | NA | 类名：LazyVGridLayoutAttribute；  API声明：columnsTemplate(value: string): LazyVGridLayoutAttribute;  差异内容：columnsTemplate(value: string): LazyVGridLayoutAttribute; | component/lazy\_grid\_layout.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const LazyVGridLayout: LazyVGridLayoutInterface;  差异内容：declare const LazyVGridLayout: LazyVGridLayoutInterface; | component/lazy\_grid\_layout.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const LazyVGridLayoutInstance: LazyVGridLayoutAttribute;  差异内容：declare const LazyVGridLayoutInstance: LazyVGridLayoutAttribute; | component/lazy\_grid\_layout.d.ts |
| 新增API | NA | 类名：window；  API声明：enum RotationChangeType  差异内容：enum RotationChangeType | api/@ohos.window.d.ts |
| 新增API | NA | 类名：RotationChangeType；  API声明：WINDOW\_WILL\_ROTATE = 0  差异内容：WINDOW\_WILL\_ROTATE = 0 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：RotationChangeType；  API声明：WINDOW\_DID\_ROTATE = 1  差异内容：WINDOW\_DID\_ROTATE = 1 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：enum RectType  差异内容：enum RectType | api/@ohos.window.d.ts |
| 新增API | NA | 类名：RectType；  API声明：RELATIVE\_TO\_SCREEN = 0  差异内容：RELATIVE\_TO\_SCREEN = 0 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：RectType；  API声明：RELATIVE\_TO\_PARENT\_WINDOW = 1  差异内容：RELATIVE\_TO\_PARENT\_WINDOW = 1 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：interface RotationChangeInfo  差异内容：interface RotationChangeInfo | api/@ohos.window.d.ts |
| 新增API | NA | 类名：RotationChangeInfo；  API声明：type: RotationChangeType;  差异内容：type: RotationChangeType; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：RotationChangeInfo；  API声明：orientation: Orientation;  差异内容：orientation: Orientation; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：RotationChangeInfo；  API声明：displayId: number;  差异内容：displayId: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：RotationChangeInfo；  API声明：displayRect: Rect;  差异内容：displayRect: Rect; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：interface RotationChangeResult  差异内容：interface RotationChangeResult | api/@ohos.window.d.ts |
| 新增API | NA | 类名：RotationChangeResult；  API声明：rectType: RectType;  差异内容：rectType: RectType; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：RotationChangeResult；  API声明：windowRect: Rect;  差异内容：windowRect: Rect; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：interface RotationChangeCallback  差异内容：interface RotationChangeCallback | api/@ohos.window.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'XComponent', parameters: NativeXComponentParameters): XComponent;  差异内容：function createNode(context: UIContext, nodeType: 'XComponent', parameters: NativeXComponentParameters): XComponent; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface InteractionEventBindingInfo  差异内容：declare interface InteractionEventBindingInfo | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：InteractionEventBindingInfo；  API声明：baseEventRegistered: boolean;  差异内容：baseEventRegistered: boolean; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：InteractionEventBindingInfo；  API声明：nodeEventRegistered: boolean;  差异内容：nodeEventRegistered: boolean; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：InteractionEventBindingInfo；  API声明：nativeEventRegistered: boolean;  差异内容：nativeEventRegistered: boolean; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：InteractionEventBindingInfo；  API声明：builtInEventRegistered: boolean;  差异内容：builtInEventRegistered: boolean; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function getEvent(node: FrameNode, nodeType: 'Scroll'): UIScrollEvent | undefined;  差异内容：function getEvent(node: FrameNode, nodeType: 'Scroll'): UIScrollEvent | undefined; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function getEvent(node: FrameNode, nodeType: 'List'): UIListEvent | undefined;  差异内容：function getEvent(node: FrameNode, nodeType: 'List'): UIListEvent | undefined; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function getEvent(node: FrameNode, nodeType: 'WaterFlow'): UIWaterFlowEvent | undefined;  差异内容：function getEvent(node: FrameNode, nodeType: 'WaterFlow'): UIWaterFlowEvent | undefined; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function getEvent(node: FrameNode, nodeType: 'Grid'): UIGridEvent | undefined;  差异内容：function getEvent(node: FrameNode, nodeType: 'Grid'): UIGridEvent | undefined; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface SystemAdaptiveOptions  差异内容：declare interface SystemAdaptiveOptions | component/common.d.ts |
| 新增API | NA | 类名：SystemAdaptiveOptions；  API声明：disableSystemAdaptation?: boolean;  差异内容：disableSystemAdaptation?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface TipsOptions  差异内容：declare interface TipsOptions | component/common.d.ts |
| 新增API | NA | 类名：TipsOptions；  API声明：appearingTime?: number;  差异内容：appearingTime?: number; | component/common.d.ts |
| 新增API | NA | 类名：TipsOptions；  API声明：disappearingTime?: number;  差异内容：disappearingTime?: number; | component/common.d.ts |
| 新增API | NA | 类名：TipsOptions；  API声明：appearingTimeWithContinuousOperation?: number;  差异内容：appearingTimeWithContinuousOperation?: number; | component/common.d.ts |
| 新增API | NA | 类名：TipsOptions；  API声明：disappearingTimeWithContinuousOperation?: number;  差异内容：disappearingTimeWithContinuousOperation?: number; | component/common.d.ts |
| 新增API | NA | 类名：TipsOptions；  API声明：enableArrow?: boolean;  差异内容：enableArrow?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：TipsOptions；  API声明：arrowPointPosition?: ArrowPointPosition;  差异内容：arrowPointPosition?: ArrowPointPosition; | component/common.d.ts |
| 新增API | NA | 类名：TipsOptions；  API声明：arrowWidth?: Dimension;  差异内容：arrowWidth?: Dimension; | component/common.d.ts |
| 新增API | NA | 类名：TipsOptions；  API声明：arrowHeight?: Dimension;  差异内容：arrowHeight?: Dimension; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：type BorderRadiusType = Length | BorderRadiuses | LocalizedBorderRadiuses;  差异内容：type BorderRadiusType = Length | BorderRadiuses | LocalizedBorderRadiuses; | component/common.d.ts |
| 新增API | NA | 类名：DragPreviewMode；  API声明：ENABLE\_TOUCH\_POINT\_CALCULATION\_BASED\_ON\_FINAL\_PREVIEW = 7  差异内容：ENABLE\_TOUCH\_POINT\_CALCULATION\_BASED\_ON\_FINAL\_PREVIEW = 7 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum DraggingSizeChangeEffect  差异内容：declare enum DraggingSizeChangeEffect | component/common.d.ts |
| 新增API | NA | 类名：DraggingSizeChangeEffect；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | component/common.d.ts |
| 新增API | NA | 类名：DraggingSizeChangeEffect；  API声明：SIZE\_TRANSITION = 1  差异内容：SIZE\_TRANSITION = 1 | component/common.d.ts |
| 新增API | NA | 类名：DraggingSizeChangeEffect；  API声明：SIZE\_CONTENT\_TRANSITION = 2  差异内容：SIZE\_CONTENT\_TRANSITION = 2 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type TipsMessageType = ResourceStr | StyledString;  差异内容：declare type TipsMessageType = ResourceStr | StyledString; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface UIScrollableCommonEvent  差异内容：declare interface UIScrollableCommonEvent | component/common.d.ts |
| 新增API | NA | 类名：UIScrollableCommonEvent；  API声明：setOnReachStart(callback: Callback<void> | undefined): void;  差异内容：setOnReachStart(callback: Callback<void> | undefined): void; | component/common.d.ts |
| 新增API | NA | 类名：UIScrollableCommonEvent；  API声明：setOnReachEnd(callback: Callback<void> | undefined): void;  差异内容：setOnReachEnd(callback: Callback<void> | undefined): void; | component/common.d.ts |
| 新增API | NA | 类名：UIScrollableCommonEvent；  API声明：setOnScrollStart(callback: Callback<void> | undefined): void;  差异内容：setOnScrollStart(callback: Callback<void> | undefined): void; | component/common.d.ts |
| 新增API | NA | 类名：UIScrollableCommonEvent；  API声明：setOnScrollStop(callback: Callback<void> | undefined): void;  差异内容：setOnScrollStop(callback: Callback<void> | undefined): void; | component/common.d.ts |
| 新增API | NA | 类名：UIScrollableCommonEvent；  API声明：setOnScrollFrameBegin(callback: OnScrollFrameBeginCallback | undefined): void;  差异内容：setOnScrollFrameBegin(callback: OnScrollFrameBeginCallback | undefined): void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface DateRange  差异内容：declare interface DateRange | component/common.d.ts |
| 新增API | NA | 类名：DateRange；  API声明：start?: Date;  差异内容：start?: Date; | component/common.d.ts |
| 新增API | NA | 类名：DateRange；  API声明：end?: Date;  差异内容：end?: Date; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface NavigationMenuOptions  差异内容：declare interface NavigationMenuOptions | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationMenuOptions；  API声明：moreButtonOptions?: MoreButtonOptions;  差异内容：moreButtonOptions?: MoreButtonOptions; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface MoreButtonOptions  差异内容：declare interface MoreButtonOptions | component/navigation.d.ts |
| 新增API | NA | 类名：MoreButtonOptions；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | component/navigation.d.ts |
| 新增API | NA | 类名：MoreButtonOptions；  API声明：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions;  差异内容：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions; | component/navigation.d.ts |
| 新增API | NA | 类名：MoreButtonOptions；  API声明：backgroundEffect?: BackgroundEffectOptions;  差异内容：backgroundEffect?: BackgroundEffectOptions; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type Orientation = import('../api/@ohos.window').default.Orientation;  差异内容：declare type Orientation = import('../api/@ohos.window').default.Orientation; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum TabsCacheMode  差异内容：declare enum TabsCacheMode | component/tabs.d.ts |
| 新增API | NA | 类名：TabsCacheMode；  API声明：CACHE\_BOTH\_SIDE = 0  差异内容：CACHE\_BOTH\_SIDE = 0 | component/tabs.d.ts |
| 新增API | NA | 类名：TabsCacheMode；  API声明：CACHE\_LATEST\_SWITCHED = 1  差异内容：CACHE\_LATEST\_SWITCHED = 1 | component/tabs.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type PanListenerCallback = (event: GestureEvent, current: GestureRecognizer, node?: FrameNode) => void;  差异内容：declare type PanListenerCallback = (event: GestureEvent, current: GestureRecognizer, node?: FrameNode) => void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：display；  API声明：enum DisplaySourceMode  差异内容：enum DisplaySourceMode | api/@ohos.display.d.ts |
| 新增API | NA | 类名：DisplaySourceMode；  API声明：NONE = 0  差异内容：NONE = 0 | api/@ohos.display.d.ts |
| 新增API | NA | 类名：DisplaySourceMode；  API声明：MAIN = 1  差异内容：MAIN = 1 | api/@ohos.display.d.ts |
| 新增API | NA | 类名：DisplaySourceMode；  API声明：MIRROR = 2  差异内容：MIRROR = 2 | api/@ohos.display.d.ts |
| 新增API | NA | 类名：DisplaySourceMode；  API声明：EXTEND = 3  差异内容：EXTEND = 3 | api/@ohos.display.d.ts |
| 新增API | NA | 类名：DisplaySourceMode；  API声明：ALONE = 4  差异内容：ALONE = 4 | api/@ohos.display.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum FocusDrawLevel  差异内容：declare enum FocusDrawLevel | component/enums.d.ts |
| 新增API | NA | 类名：FocusDrawLevel；  API声明：SELF = 0  差异内容：SELF = 0 | component/enums.d.ts |
| 新增API | NA | 类名：FocusDrawLevel；  API声明：TOP = 1  差异内容：TOP = 1 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum DividerMode  差异内容：declare enum DividerMode | component/enums.d.ts |
| 新增API | NA | 类名：DividerMode；  API声明：FLOATING\_ABOVE\_MENU = 0  差异内容：FLOATING\_ABOVE\_MENU = 0 | component/enums.d.ts |
| 新增API | NA | 类名：DividerMode；  API声明：EMBEDDED\_IN\_MENU = 1  差异内容：EMBEDDED\_IN\_MENU = 1 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum EventQueryType  差异内容：declare enum EventQueryType | component/enums.d.ts |
| 新增API | NA | 类名：EventQueryType；  API声明：ON\_CLICK = 0  差异内容：ON\_CLICK = 0 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface UIGridEvent  差异内容：declare interface UIGridEvent | component/grid.d.ts |
| 新增API | NA | 类名：UIGridEvent；  API声明：setOnWillScroll(callback: OnWillScrollCallback | undefined): void;  差异内容：setOnWillScroll(callback: OnWillScrollCallback | undefined): void; | component/grid.d.ts |
| 新增API | NA | 类名：UIGridEvent；  API声明：setOnDidScroll(callback: OnScrollCallback | undefined): void;  差异内容：setOnDidScroll(callback: OnScrollCallback | undefined): void; | component/grid.d.ts |
| 新增API | NA | 类名：UIGridEvent；  API声明：setOnScrollIndex(callback: OnGridScrollIndexCallback | undefined): void;  差异内容：setOnScrollIndex(callback: OnGridScrollIndexCallback | undefined): void; | component/grid.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type OnGridScrollIndexCallback = (first: number, last: number) => void;  差异内容：declare type OnGridScrollIndexCallback = (first: number, last: number) => void; | component/grid.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface UIListEvent  差异内容：declare interface UIListEvent | component/list.d.ts |
| 新增API | NA | 类名：UIListEvent；  API声明：setOnWillScroll(callback: OnWillScrollCallback | undefined): void;  差异内容：setOnWillScroll(callback: OnWillScrollCallback | undefined): void; | component/list.d.ts |
| 新增API | NA | 类名：UIListEvent；  API声明：setOnDidScroll(callback: OnScrollCallback | undefined): void;  差异内容：setOnDidScroll(callback: OnScrollCallback | undefined): void; | component/list.d.ts |
| 新增API | NA | 类名：UIListEvent；  API声明：setOnScrollIndex(callback: OnListScrollIndexCallback | undefined): void;  差异内容：setOnScrollIndex(callback: OnListScrollIndexCallback | undefined): void; | component/list.d.ts |
| 新增API | NA | 类名：UIListEvent；  API声明：setOnScrollVisibleContentChange(callback: OnScrollVisibleContentChangeCallback | undefined): void;  差异内容：setOnScrollVisibleContentChange(callback: OnScrollVisibleContentChangeCallback | undefined): void; | component/list.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type OnListScrollIndexCallback = (start: number, end: number, center: number) => void;  差异内容：declare type OnListScrollIndexCallback = (start: number, end: number, center: number) => void; | component/list.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface RichEditorUrlStyle  差异内容：declare interface RichEditorUrlStyle | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorUrlStyle；  API声明：url?: ResourceStr;  差异内容：url?: ResourceStr; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface UIScrollEvent  差异内容：declare interface UIScrollEvent | component/scroll.d.ts |
| 新增API | NA | 类名：UIScrollEvent；  API声明：setOnWillScroll(callback: ScrollOnWillScrollCallback | undefined): void;  差异内容：setOnWillScroll(callback: ScrollOnWillScrollCallback | undefined): void; | component/scroll.d.ts |
| 新增API | NA | 类名：UIScrollEvent；  API声明：setOnDidScroll(callback: ScrollOnScrollCallback | undefined): void;  差异内容：setOnDidScroll(callback: ScrollOnScrollCallback | undefined): void; | component/scroll.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum AvoidanceMode  差异内容：declare enum AvoidanceMode | component/select.d.ts |
| 新增API | NA | 类名：AvoidanceMode；  API声明：COVER\_TARGET  差异内容：COVER\_TARGET | component/select.d.ts |
| 新增API | NA | 类名：AvoidanceMode；  API声明：AVOID\_AROUND\_TARGET  差异内容：AVOID\_AROUND\_TARGET | component/select.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface UIWaterFlowEvent  差异内容：declare interface UIWaterFlowEvent | component/water\_flow.d.ts |
| 新增API | NA | 类名：UIWaterFlowEvent；  API声明：setOnWillScroll(callback: OnWillScrollCallback | undefined): void;  差异内容：setOnWillScroll(callback: OnWillScrollCallback | undefined): void; | component/water\_flow.d.ts |
| 新增API | NA | 类名：UIWaterFlowEvent；  API声明：setOnDidScroll(callback: OnScrollCallback | undefined): void;  差异内容：setOnDidScroll(callback: OnScrollCallback | undefined): void; | component/water\_flow.d.ts |
| 新增API | NA | 类名：UIWaterFlowEvent；  API声明：setOnScrollIndex(callback: OnWaterFlowScrollIndexCallback | undefined): void;  差异内容：setOnScrollIndex(callback: OnWaterFlowScrollIndexCallback | undefined): void; | component/water\_flow.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type OnWaterFlowScrollIndexCallback = (first: number, last: number) => void;  差异内容：declare type OnWaterFlowScrollIndexCallback = (first: number, last: number) => void; | component/water\_flow.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface NativeXComponentParameters  差异内容：declare interface NativeXComponentParameters | component/xcomponent.d.ts |
| 新增API | NA | 类名：NativeXComponentParameters；  API声明：type: XComponentType;  差异内容：type: XComponentType; | component/xcomponent.d.ts |
| 新增API | NA | 类名：NativeXComponentParameters；  API声明：imageAIOptions?: ImageAIOptions;  差异内容：imageAIOptions?: ImageAIOptions; | component/xcomponent.d.ts |
| 属性变更 | 类名：RotationChangeInfo；  API声明：orientation: Orientation;  差异内容：Orientation | 类名：RotationChangeInfo；  API声明：orientation: number;  差异内容：number | api/@ohos.window.d.ts |
| 起始版本有变化 | 类名：TabsAttribute；  API声明：barBackgroundBlurStyle(style: BlurStyle, options: BackgroundBlurStyleOptions): TabsAttribute;  差异内容：15 | 类名：TabsAttribute；  API声明：barBackgroundBlurStyle(style: BlurStyle, options: BackgroundBlurStyleOptions): TabsAttribute;  差异内容：18 | component/tabs.d.ts |
| 起始版本有变化 | 类名：TabsAttribute；  API声明：barBackgroundEffect(options: BackgroundEffectOptions): TabsAttribute;  差异内容：15 | 类名：TabsAttribute；  API声明：barBackgroundEffect(options: BackgroundEffectOptions): TabsAttribute;  差异内容：18 | component/tabs.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：component\lazy\_grid\_layout.d.ts  差异内容：ArkUI | component/lazy\_grid\_layout.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：NavPathInfo；  API声明：navDestinationId?: string;  差异内容：navDestinationId?: string; | component/navigation.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：ParagraphStyle；  API声明：readonly paragraphSpacing?: number;  差异内容：readonly paragraphSpacing?: number; | component/styled\_string.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：FrameNode；  API声明：getInteractionEventBindingInfo(eventType: EventQueryType): InteractionEventBindingInfo | undefined;  差异内容：getInteractionEventBindingInfo(eventType: EventQueryType): InteractionEventBindingInfo | undefined; | api/arkui/FrameNode.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CommonMethod；  API声明：bindTips(message: TipsMessageType, options?: TipsOptions): T;  差异内容：bindTips(message: TipsMessageType, options?: TipsOptions): T; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CommonMethod；  API声明：accessibilityFocusDrawLevel(drawLevel: FocusDrawLevel): T;  差异内容：accessibilityFocusDrawLevel(drawLevel: FocusDrawLevel): T; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：BaseCustomComponent；  API声明：onNewParam?(param: ESObject): void;  差异内容：onNewParam?(param: ESObject): void; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：NavPathStack；  API声明：getPathStack(): Array<NavPathInfo>;  差异内容：getPathStack(): Array<NavPathInfo>; | component/navigation.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：NavPathStack；  API声明：setPathStack(pathStack: Array<NavPathInfo>, animated?: boolean): void;  差异内容：setPathStack(pathStack: Array<NavPathInfo>, animated?: boolean): void; | component/navigation.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：NavigationAttribute；  API声明：enableToolBarAdaptation(enable: Optional<boolean>): NavigationAttribute;  差异内容：enableToolBarAdaptation(enable: Optional<boolean>): NavigationAttribute; | component/navigation.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：NavDestinationAttribute；  API声明：onNewParam(callback: Optional<Callback<ESObject>>): NavDestinationAttribute;  差异内容：onNewParam(callback: Optional<Callback<ESObject>>): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：NavDestinationAttribute；  API声明：preferredOrientation(orientation: Optional<Orientation>): NavDestinationAttribute;  差异内容：preferredOrientation(orientation: Optional<Orientation>): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：NavDestinationAttribute；  API声明：enableStatusBar(enabled: Optional<boolean>, animated?: boolean): NavDestinationAttribute;  差异内容：enableStatusBar(enabled: Optional<boolean>, animated?: boolean): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：NavDestinationAttribute；  API声明：enableNavigationIndicator(enabled: Optional<boolean>): NavDestinationAttribute;  差异内容：enableNavigationIndicator(enabled: Optional<boolean>): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：DotIndicator；  API声明：space(space: LengthMetrics): DotIndicator;  差异内容：space(space: LengthMetrics): DotIndicator; | component/swiper.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TabsAttribute；  API声明：cachedMaxCount(count: number, mode: TabsCacheMode): TabsAttribute;  差异内容：cachedMaxCount(count: number, mode: TabsCacheMode): TabsAttribute; | component/tabs.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIUtils；  API声明：static makeV1Observed<T extends object>(source: T): T;  差异内容：static makeV1Observed<T extends object>(source: T): T; | api/@ohos.arkui.StateManagement.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIUtils；  API声明：static enableV2Compatibility<T extends object>(source: T): T;  差异内容：static enableV2Compatibility<T extends object>(source: T): T; | api/@ohos.arkui.StateManagement.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIObserver；  API声明：on(type: 'beforePanStart', callback: PanListenerCallback): void;  差异内容：on(type: 'beforePanStart', callback: PanListenerCallback): void; | api/@ohos.arkui.UIContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIObserver；  API声明：off(type: 'beforePanStart', callback?: PanListenerCallback): void;  差异内容：off(type: 'beforePanStart', callback?: PanListenerCallback): void; | api/@ohos.arkui.UIContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIObserver；  API声明：on(type: 'beforePanEnd', callback: PanListenerCallback): void;  差异内容：on(type: 'beforePanEnd', callback: PanListenerCallback): void; | api/@ohos.arkui.UIContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIObserver；  API声明：off(type: 'beforePanEnd', callback?: PanListenerCallback): void;  差异内容：off(type: 'beforePanEnd', callback?: PanListenerCallback): void; | api/@ohos.arkui.UIContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIObserver；  API声明：on(type: 'afterPanStart', callback: PanListenerCallback): void;  差异内容：on(type: 'afterPanStart', callback: PanListenerCallback): void; | api/@ohos.arkui.UIContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIObserver；  API声明：off(type: 'afterPanStart', callback?: PanListenerCallback): void;  差异内容：off(type: 'afterPanStart', callback?: PanListenerCallback): void; | api/@ohos.arkui.UIContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIObserver；  API声明：on(type: 'afterPanEnd', callback: PanListenerCallback): void;  差异内容：on(type: 'afterPanEnd', callback: PanListenerCallback): void; | api/@ohos.arkui.UIContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIObserver；  API声明：off(type: 'afterPanEnd', callback?: PanListenerCallback): void;  差异内容：off(type: 'afterPanEnd', callback?: PanListenerCallback): void; | api/@ohos.arkui.UIContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CalendarPickerAttribute；  API声明：markToday(enabled: boolean): CalendarPickerAttribute;  差异内容：markToday(enabled: boolean): CalendarPickerAttribute; | component/calendar\_picker.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：PanRecognizer；  API声明：getDirection(): PanDirection;  差异内容：getDirection(): PanDirection; | component/gesture.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：PanRecognizer；  API声明：getDistance(): number;  差异内容：getDistance(): number; | component/gesture.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：PanRecognizer；  API声明：getDistanceMap(): Map<SourceTool, number>;  差异内容：getDistanceMap(): Map<SourceTool, number>; | component/gesture.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：ListAttribute；  API声明：stackFromEnd(enabled: boolean): ListAttribute;  差异内容：stackFromEnd(enabled: boolean): ListAttribute; | component/list.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SelectAttribute；  API声明：dividerStyle(style: Optional<DividerStyleOptions>): SelectAttribute;  差异内容：dividerStyle(style: Optional<DividerStyleOptions>): SelectAttribute; | component/select.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SelectAttribute；  API声明：avoidance(mode: AvoidanceMode): SelectAttribute;  差异内容：avoidance(mode: AvoidanceMode): SelectAttribute; | component/select.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：CommonMethod；  API声明：backgroundBlurStyle(style: Optional<BlurStyle>, options?: BackgroundBlurStyleOptions): T;  差异内容：backgroundBlurStyle(style: Optional<BlurStyle>, options?: BackgroundBlurStyleOptions): T; | 类名：CommonMethod；  API声明：backgroundBlurStyle(style: Optional<BlurStyle>, options?: BackgroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): T;  差异内容：backgroundBlurStyle(style: Optional<BlurStyle>, options?: BackgroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): T; | component/common.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：CommonMethod；  API声明：backgroundEffect(options: Optional<BackgroundEffectOptions>): T;  差异内容：backgroundEffect(options: Optional<BackgroundEffectOptions>): T; | 类名：CommonMethod；  API声明：backgroundEffect(options: Optional<BackgroundEffectOptions>, sysOptions?: SystemAdaptiveOptions): T;  差异内容：backgroundEffect(options: Optional<BackgroundEffectOptions>, sysOptions?: SystemAdaptiveOptions): T; | component/common.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：CommonMethod；  API声明：foregroundBlurStyle(style: Optional<BlurStyle>, options?: ForegroundBlurStyleOptions): T;  差异内容：foregroundBlurStyle(style: Optional<BlurStyle>, options?: ForegroundBlurStyleOptions): T; | 类名：CommonMethod；  API声明：foregroundBlurStyle(style: Optional<BlurStyle>, options?: ForegroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): T;  差异内容：foregroundBlurStyle(style: Optional<BlurStyle>, options?: ForegroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): T; | component/common.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：CommonMethod；  API声明：blur(blurRadius: Optional<number>, options?: BlurOptions): T;  差异内容：blur(blurRadius: Optional<number>, options?: BlurOptions): T; | 类名：CommonMethod；  API声明：blur(blurRadius: Optional<number>, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): T;  差异内容：blur(blurRadius: Optional<number>, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): T; | component/common.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：CommonMethod；  API声明：backdropBlur(radius: Optional<number>, options?: BlurOptions): T;  差异内容：backdropBlur(radius: Optional<number>, options?: BlurOptions): T; | 类名：CommonMethod；  API声明：backdropBlur(radius: Optional<number>, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): T;  差异内容：backdropBlur(radius: Optional<number>, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): T; | component/common.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：NavigationAttribute；  API声明：backButtonIcon(value: string | PixelMap | Resource | SymbolGlyphModifier): NavigationAttribute;  差异内容：backButtonIcon(value: string | PixelMap | Resource | SymbolGlyphModifier): NavigationAttribute; | 类名：NavigationAttribute；  API声明：backButtonIcon(icon: string | PixelMap | Resource | SymbolGlyphModifier, accessibilityText?: ResourceStr): NavigationAttribute;  差异内容：backButtonIcon(icon: string | PixelMap | Resource | SymbolGlyphModifier, accessibilityText?: ResourceStr): NavigationAttribute; | component/navigation.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：NavigationAttribute；  API声明：menus(value: Array<NavigationMenuItem> | CustomBuilder): NavigationAttribute;  差异内容：menus(value: Array<NavigationMenuItem> | CustomBuilder): NavigationAttribute; | 类名：NavigationAttribute；  API声明：menus(items: Array<NavigationMenuItem> | CustomBuilder, options?: NavigationMenuOptions): NavigationAttribute;  差异内容：menus(items: Array<NavigationMenuItem> | CustomBuilder, options?: NavigationMenuOptions): NavigationAttribute; | component/navigation.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：NavDestinationAttribute；  API声明：backButtonIcon(value: ResourceStr | PixelMap | SymbolGlyphModifier): NavDestinationAttribute;  差异内容：backButtonIcon(value: ResourceStr | PixelMap | SymbolGlyphModifier): NavDestinationAttribute; | 类名：NavDestinationAttribute；  API声明：backButtonIcon(icon: ResourceStr | PixelMap | SymbolGlyphModifier, accessibilityText?: ResourceStr): NavDestinationAttribute;  差异内容：backButtonIcon(icon: ResourceStr | PixelMap | SymbolGlyphModifier, accessibilityText?: ResourceStr): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：NavDestinationAttribute；  API声明：menus(value: Array<NavigationMenuItem> | CustomBuilder): NavDestinationAttribute;  差异内容：menus(value: Array<NavigationMenuItem> | CustomBuilder): NavDestinationAttribute; | 类名：NavDestinationAttribute；  API声明：menus(items: Array<NavigationMenuItem> | CustomBuilder, options?: NavigationMenuOptions): NavDestinationAttribute;  差异内容：menus(items: Array<NavigationMenuItem> | CustomBuilder, options?: NavigationMenuOptions): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Indicator；  API声明：bottom(value: Length): T;  差异内容：bottom(value: Length): T; | 类名：Indicator；  API声明：bottom(bottom: LengthMetrics | Length, ignoreSize: boolean): T;  差异内容：bottom(bottom: LengthMetrics | Length, ignoreSize: boolean): T; | component/swiper.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：on(type: 'rotationChange', callback: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void;  差异内容：on(type: 'rotationChange', callback: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：off(type: 'rotationChange', callback?: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void;  差异内容：off(type: 'rotationChange', callback?: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：setParentWindow(windowId: number): Promise<void>;  差异内容：setParentWindow(windowId: number): Promise<void>; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：getParentWindow(): Window;  差异内容：getParentWindow(): Window; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：setWindowDelayRaiseOnDrag(isEnabled: boolean): void;  差异内容：setWindowDelayRaiseOnDrag(isEnabled: boolean): void; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：VirtualScrollOptions；  API声明：onLazyLoading?(index: number): void;  差异内容：onLazyLoading?(index: number): void; | component/repeat.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：VirtualScrollOptions；  API声明：onTotalCount?(): number;  差异内容：onTotalCount?(): number; | component/repeat.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：SubWindowOptions；  API声明：maximizeSupported?: boolean;  差异内容：maximizeSupported?: boolean; | api/@ohos.window.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：KeyEvent；  API声明：isNumLockOn?: boolean;  差异内容：isNumLockOn?: boolean; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：KeyEvent；  API声明：isCapsLockOn?: boolean;  差异内容：isCapsLockOn?: boolean; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：KeyEvent；  API声明：isScrollLockOn?: boolean;  差异内容：isScrollLockOn?: boolean; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：SheetOptions；  API声明：showInSubWindow?: boolean;  差异内容：showInSubWindow?: boolean; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ContextMenuOptions；  API声明：previewBorderRadius?: BorderRadiusType;  差异内容：previewBorderRadius?: BorderRadiusType; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：DragPreviewOptions；  API声明：sizeChangeEffect?: DraggingSizeChangeEffect;  差异内容：sizeChangeEffect?: DraggingSizeChangeEffect; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：KeyframeAnimateParam；  API声明：expectedFrameRateRange?: ExpectedFrameRateRange;  差异内容：expectedFrameRateRange?: ExpectedFrameRateRange; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：NavigationTitleOptions；  API声明：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions;  差异内容：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions; | component/navigation.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：NavigationTitleOptions；  API声明：backgroundEffect?: BackgroundEffectOptions;  差异内容：backgroundEffect?: BackgroundEffectOptions; | component/navigation.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：NavigationToolbarOptions；  API声明：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions;  差异内容：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions; | component/navigation.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：NavigationToolbarOptions；  API声明：backgroundEffect?: BackgroundEffectOptions;  差异内容：backgroundEffect?: BackgroundEffectOptions; | component/navigation.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：NavigationToolbarOptions；  API声明：moreButtonOptions?: MoreButtonOptions;  差异内容：moreButtonOptions?: MoreButtonOptions; | component/navigation.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：NavigationToolbarOptions；  API声明：hideItemValue?: boolean;  差异内容：hideItemValue?: boolean; | component/navigation.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：OverlayManagerOptions；  API声明：enableBackPressedEvent?: boolean;  差异内容：enableBackPressedEvent?: boolean; | api/@ohos.arkui.UIContext.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Display；  API声明：sourceMode?: DisplaySourceMode;  差异内容：sourceMode?: DisplaySourceMode; | api/@ohos.display.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Display；  API声明：x?: number;  差异内容：x?: number; | api/@ohos.display.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Display；  API声明：y?: number;  差异内容：y?: number; | api/@ohos.display.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：PiPConfiguration；  API声明：defaultWindowSizeType?: number;  差异内容：defaultWindowSizeType?: number; | api/@ohos.PiPWindow.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ShowDialogOptions；  API声明：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions;  差异内容：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions; | api/@ohos.promptAction.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ShowDialogOptions；  API声明：backgroundEffect?: BackgroundEffectOptions;  差异内容：backgroundEffect?: BackgroundEffectOptions; | api/@ohos.promptAction.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ShowDialogOptions；  API声明：onDidAppear?: Callback<void>;  差异内容：onDidAppear?: Callback<void>; | api/@ohos.promptAction.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ShowDialogOptions；  API声明：onDidDisappear?: Callback<void>;  差异内容：onDidDisappear?: Callback<void>; | api/@ohos.promptAction.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ShowDialogOptions；  API声明：onWillAppear?: Callback<void>;  差异内容：onWillAppear?: Callback<void>; | api/@ohos.promptAction.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ShowDialogOptions；  API声明：onWillDisappear?: Callback<void>;  差异内容：onWillDisappear?: Callback<void>; | api/@ohos.promptAction.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：BaseDialogOptions；  API声明：dialogTransition?: TransitionEffect;  差异内容：dialogTransition?: TransitionEffect; | api/@ohos.promptAction.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：BaseDialogOptions；  API声明：maskTransition?: TransitionEffect;  差异内容：maskTransition?: TransitionEffect; | api/@ohos.promptAction.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：BaseDialogOptions；  API声明：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions;  差异内容：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions; | api/@ohos.promptAction.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：BaseDialogOptions；  API声明：backgroundEffect?: BackgroundEffectOptions;  差异内容：backgroundEffect?: BackgroundEffectOptions; | api/@ohos.promptAction.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：BaseDialogOptions；  API声明：focusable?: boolean;  差异内容：focusable?: boolean; | api/@ohos.promptAction.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ActionSheetOptions；  API声明：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions;  差异内容：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions; | component/action\_sheet.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ActionSheetOptions；  API声明：backgroundEffect?: BackgroundEffectOptions;  差异内容：backgroundEffect?: BackgroundEffectOptions; | component/action\_sheet.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ActionSheetOptions；  API声明：onDidAppear?: Callback<void>;  差异内容：onDidAppear?: Callback<void>; | component/action\_sheet.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ActionSheetOptions；  API声明：onDidDisappear?: Callback<void>;  差异内容：onDidDisappear?: Callback<void>; | component/action\_sheet.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ActionSheetOptions；  API声明：onWillAppear?: Callback<void>;  差异内容：onWillAppear?: Callback<void>; | component/action\_sheet.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ActionSheetOptions；  API声明：onWillDisappear?: Callback<void>;  差异内容：onWillDisappear?: Callback<void>; | component/action\_sheet.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：AlertDialogParam；  API声明：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions;  差异内容：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions; | component/alert\_dialog.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：AlertDialogParam；  API声明：backgroundEffect?: BackgroundEffectOptions;  差异内容：backgroundEffect?: BackgroundEffectOptions; | component/alert\_dialog.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：AlertDialogParam；  API声明：onDidAppear?: Callback<void>;  差异内容：onDidAppear?: Callback<void>; | component/alert\_dialog.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：AlertDialogParam；  API声明：onDidDisappear?: Callback<void>;  差异内容：onDidDisappear?: Callback<void>; | component/alert\_dialog.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：AlertDialogParam；  API声明：onWillAppear?: Callback<void>;  差异内容：onWillAppear?: Callback<void>; | component/alert\_dialog.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：AlertDialogParam；  API声明：onWillDisappear?: Callback<void>;  差异内容：onWillDisappear?: Callback<void>; | component/alert\_dialog.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CalendarOptions；  API声明：disabledDateRange?: DateRange[];  差异内容：disabledDateRange?: DateRange[]; | component/calendar\_picker.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CalendarDialogOptions；  API声明：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions;  差异内容：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions; | component/calendar\_picker.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CalendarDialogOptions；  API声明：backgroundEffect?: BackgroundEffectOptions;  差异内容：backgroundEffect?: BackgroundEffectOptions; | component/calendar\_picker.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CalendarDialogOptions；  API声明：markToday?: boolean;  差异内容：markToday?: boolean; | component/calendar\_picker.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CustomDialogControllerOptions；  API声明：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions;  差异内容：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions; | component/custom\_dialog\_controller.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CustomDialogControllerOptions；  API声明：backgroundEffect?: BackgroundEffectOptions;  差异内容：backgroundEffect?: BackgroundEffectOptions; | component/custom\_dialog\_controller.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CustomDialogControllerOptions；  API声明：onDidAppear?: Callback<void>;  差异内容：onDidAppear?: Callback<void>; | component/custom\_dialog\_controller.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CustomDialogControllerOptions；  API声明：onDidDisappear?: Callback<void>;  差异内容：onDidDisappear?: Callback<void>; | component/custom\_dialog\_controller.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CustomDialogControllerOptions；  API声明：onWillAppear?: Callback<void>;  差异内容：onWillAppear?: Callback<void>; | component/custom\_dialog\_controller.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CustomDialogControllerOptions；  API声明：onWillDisappear?: Callback<void>;  差异内容：onWillDisappear?: Callback<void>; | component/custom\_dialog\_controller.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CustomDialogControllerOptions；  API声明：focusable?: boolean;  差异内容：focusable?: boolean; | component/custom\_dialog\_controller.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：DatePickerDialogOptions；  API声明：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions;  差异内容：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions; | component/date\_picker.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：DatePickerDialogOptions；  API声明：backgroundEffect?: BackgroundEffectOptions;  差异内容：backgroundEffect?: BackgroundEffectOptions; | component/date\_picker.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：PanGestureHandlerOptions；  API声明：distanceMap?: Map<SourceTool, number>;  差异内容：distanceMap?: Map<SourceTool, number>; | component/gesture.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：RichEditorParagraphStyle；  API声明：paragraphSpacing?: number;  差异内容：paragraphSpacing?: number; | component/rich\_editor.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：RichEditorTextSpanResult；  API声明：urlStyle?: RichEditorUrlStyle;  差异内容：urlStyle?: RichEditorUrlStyle; | component/rich\_editor.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：RichEditorTextSpanOptions；  API声明：urlStyle?: RichEditorUrlStyle;  差异内容：urlStyle?: RichEditorUrlStyle; | component/rich\_editor.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：RichEditorUpdateTextSpanStyleOptions；  API声明：urlStyle?: RichEditorUrlStyle;  差异内容：urlStyle?: RichEditorUrlStyle; | component/rich\_editor.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ParagraphStyleInterface；  API声明：paragraphSpacing?: LengthMetrics;  差异内容：paragraphSpacing?: LengthMetrics; | component/styled\_string.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：TextPickerDialogOptions；  API声明：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions;  差异内容：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions; | component/text\_picker.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：TextPickerDialogOptions；  API声明：backgroundEffect?: BackgroundEffectOptions;  差异内容：backgroundEffect?: BackgroundEffectOptions; | component/text\_picker.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：TimePickerDialogOptions；  API声明：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions;  差异内容：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions; | component/time\_picker.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：TimePickerDialogOptions；  API声明：backgroundEffect?: BackgroundEffectOptions;  差异内容：backgroundEffect?: BackgroundEffectOptions; | component/time\_picker.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：DividerStyleOptions；  API声明：mode?: DividerMode;  差异内容：mode?: DividerMode; | component/units.d.ts |
| 新增继承父类 | 类名：global；  API声明：declare class RepeatAttribute  差异内容：NA | 类名：global；  API声明：declare class RepeatAttribute  差异内容：declare class RepeatAttribute | component/repeat.d.ts |
