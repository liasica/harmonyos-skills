---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-6002
title: ArkUI
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > ArkUI
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:26+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:440ddb96f2973321f7927e11d6b3669b04f5bc113eb6905349043857f128fa37
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：XComponentType；  API声明：NODE  差异内容：NA | 类名：XComponentType；  API声明：NODE  差异内容：20 | component/enums.d.ts |
| 函数变更 | 类名：SecurityComponentMethod；  API声明：fontWeight(value: number | FontWeight | string): T;  差异内容：value: number | FontWeight | string | 类名：SecurityComponentMethod；  API声明：fontWeight(value: number | FontWeight | string | Resource): T;  差异内容：value: number | FontWeight | string | Resource | component/security\_component.d.ts |
| 函数变更 | 类名：SecurityComponentMethod；  API声明：maxLines(line: number): T;  差异内容：line: number | 类名：SecurityComponentMethod；  API声明：maxLines(line: number | Resource): T;  差异内容：line: number | Resource | component/security\_component.d.ts |
| 自定义类型变更 | 类名：global；  API声明：declare type GestureRecognizerJudgeBeginCallback = (event: BaseGestureEvent, current: GestureRecognizer, recognizers: Array<GestureRecognizer>) => GestureJudgeResult;  差异内容：NA | 类名：global；  API声明：declare type GestureRecognizerJudgeBeginCallback = (event: BaseGestureEvent, current: GestureRecognizer, recognizers: Array<GestureRecognizer>, touchRecognizers?: Array<TouchRecognizer>) => GestureJudgeResult;  差异内容：touchRecognizers?: Array<TouchRecognizer> | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace uiAppearance  差异内容：declare namespace uiAppearance | api/@ohos.uiAppearance.d.ts |
| 新增API | NA | 类名：uiAppearance；  API声明：enum DarkMode  差异内容：enum DarkMode | api/@ohos.uiAppearance.d.ts |
| 新增API | NA | 类名：DarkMode；  API声明：ALWAYS\_DARK = 0  差异内容：ALWAYS\_DARK = 0 | api/@ohos.uiAppearance.d.ts |
| 新增API | NA | 类名：DarkMode；  API声明：ALWAYS\_LIGHT = 1  差异内容：ALWAYS\_LIGHT = 1 | api/@ohos.uiAppearance.d.ts |
| 新增API | NA | 类名：uiAppearance；  API声明：function getDarkMode(): DarkMode;  差异内容：function getDarkMode(): DarkMode; | api/@ohos.uiAppearance.d.ts |
| 新增API | NA | 类名：uiAppearance；  API声明：function getFontScale(): number;  差异内容：function getFontScale(): number; | api/@ohos.uiAppearance.d.ts |
| 新增API | NA | 类名：uiAppearance；  API声明：function getFontWeightScale(): number;  差异内容：function getFontWeightScale(): number; | api/@ohos.uiAppearance.d.ts |
| 新增API | NA | 类名：window；  API声明：function shiftAppWindowTouchEvent(sourceWindowId: number, targetWindowId: number, fingerId: number): Promise<void>;  差异内容：function shiftAppWindowTouchEvent(sourceWindowId: number, targetWindowId: number, fingerId: number): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：enum ScreenshotEventType  差异内容：enum ScreenshotEventType | api/@ohos.window.d.ts |
| 新增API | NA | 类名：ScreenshotEventType；  API声明：SYSTEM\_SCREENSHOT = 0  差异内容：SYSTEM\_SCREENSHOT = 0 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：ScreenshotEventType；  API声明：SYSTEM\_SCREENSHOT\_ABORT = 1  差异内容：SYSTEM\_SCREENSHOT\_ABORT = 1 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：ScreenshotEventType；  API声明：SCROLL\_SHOT\_START = 2  差异内容：SCROLL\_SHOT\_START = 2 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：ScreenshotEventType；  API声明：SCROLL\_SHOT\_END = 3  差异内容：SCROLL\_SHOT\_END = 3 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：ScreenshotEventType；  API声明：SCROLL\_SHOT\_ABORT = 4  差异内容：SCROLL\_SHOT\_ABORT = 4 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type SpringLoadingContext = import('../api/@ohos.arkui.dragController').default.SpringLoadingContext;  差异内容：declare type SpringLoadingContext = import('../api/@ohos.arkui.dragController').default.SpringLoadingContext; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type DragSpringLoadingConfiguration = import('../api/@ohos.arkui.dragController').default.DragSpringLoadingConfiguration;  差异内容：declare type DragSpringLoadingConfiguration = import('../api/@ohos.arkui.dragController').default.DragSpringLoadingConfiguration; | component/common.d.ts |
| 新增API | NA | 类名：LayoutSafeAreaEdge；  API声明：START = 2  差异内容：START = 2 | component/common.d.ts |
| 新增API | NA | 类名：LayoutSafeAreaEdge；  API声明：END = 3  差异内容：END = 3 | component/common.d.ts |
| 新增API | NA | 类名：LayoutSafeAreaEdge；  API声明：VERTICAL = 4  差异内容：VERTICAL = 4 | component/common.d.ts |
| 新增API | NA | 类名：LayoutSafeAreaEdge；  API声明：HORIZONTAL = 5  差异内容：HORIZONTAL = 5 | component/common.d.ts |
| 新增API | NA | 类名：LayoutSafeAreaEdge；  API声明：ALL = 6  差异内容：ALL = 6 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type TouchTestDoneCallback = (event: BaseGestureEvent, recognizers: Array<GestureRecognizer>) => void;  差异内容：declare type TouchTestDoneCallback = (event: BaseGestureEvent, recognizers: Array<GestureRecognizer>) => void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type DataLoadParams = import('../api/@ohos.data.unifiedDataChannel').default.DataLoadParams;  差异内容：declare type DataLoadParams = import('../api/@ohos.data.unifiedDataChannel').default.DataLoadParams; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum ModalMode  差异内容：declare enum ModalMode | component/common.d.ts |
| 新增API | NA | 类名：ModalMode；  API声明：AUTO = 0  差异内容：AUTO = 0 | component/common.d.ts |
| 新增API | NA | 类名：ModalMode；  API声明：NONE = 1  差异内容：NONE = 1 | component/common.d.ts |
| 新增API | NA | 类名：ModalMode；  API声明：TARGET\_WINDOW = 2  差异内容：TARGET\_WINDOW = 2 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type Matrix4Transit = import('../api/@ohos.matrix4').default.Matrix4Transit;  差异内容：declare type Matrix4Transit = import('../api/@ohos.matrix4').default.Matrix4Transit; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface BackgroundOptions  差异内容：declare interface BackgroundOptions | component/common.d.ts |
| 新增API | NA | 类名：BackgroundOptions；  API声明：align?: Alignment;  差异内容：align?: Alignment; | component/common.d.ts |
| 新增API | NA | 类名：BackgroundOptions；  API声明：ignoresLayoutSafeAreaEdges?: Array<LayoutSafeAreaEdge>;  差异内容：ignoresLayoutSafeAreaEdges?: Array<LayoutSafeAreaEdge>; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type OnWillStopDraggingCallback = (velocity: number) => void;  差异内容：declare type OnWillStopDraggingCallback = (velocity: number) => void; | component/common.d.ts |
| 新增API | NA | 类名：ImageSpanAlignment；  API声明：FOLLOW\_PARAGRAPH  差异内容：FOLLOW\_PARAGRAPH | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum FocusWrapMode  差异内容：declare enum FocusWrapMode | component/enums.d.ts |
| 新增API | NA | 类名：FocusWrapMode；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | component/enums.d.ts |
| 新增API | NA | 类名：FocusWrapMode；  API声明：WRAP\_WITH\_ARROW = 1  差异内容：WRAP\_WITH\_ARROW = 1 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum TipsAnchorType  差异内容：declare enum TipsAnchorType | component/enums.d.ts |
| 新增API | NA | 类名：TipsAnchorType；  API声明：TARGET  差异内容：TARGET | component/enums.d.ts |
| 新增API | NA | 类名：TipsAnchorType；  API声明：CURSOR  差异内容：CURSOR | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum ColorSpace  差异内容：declare enum ColorSpace | component/enums.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：SRGB = 0  差异内容：SRGB = 0 | component/enums.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：DISPLAY\_P3 = 1  差异内容：DISPLAY\_P3 = 1 | component/enums.d.ts |
| 新增API | NA | 类名：ImageRotateOrientation；  API声明：UP\_MIRRORED = 5  差异内容：UP\_MIRRORED = 5 | component/image.d.ts |
| 新增API | NA | 类名：ImageRotateOrientation；  API声明：RIGHT\_MIRRORED = 6  差异内容：RIGHT\_MIRRORED = 6 | component/image.d.ts |
| 新增API | NA | 类名：ImageRotateOrientation；  API声明：DOWN\_MIRRORED = 7  差异内容：DOWN\_MIRRORED = 7 | component/image.d.ts |
| 新增API | NA | 类名：ImageRotateOrientation；  API声明：LEFT\_MIRRORED = 8  差异内容：LEFT\_MIRRORED = 8 | component/image.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum BorderRadiusMode  差异内容：declare enum BorderRadiusMode | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：BorderRadiusMode；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：BorderRadiusMode；  API声明：CUSTOM = 1  差异内容：CUSTOM = 1 | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：dragController；  API声明：const enum DragSpringLoadingState  差异内容：const enum DragSpringLoadingState | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragSpringLoadingState；  API声明：BEGIN  差异内容：BEGIN | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragSpringLoadingState；  API声明：UPDATE  差异内容：UPDATE | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragSpringLoadingState；  API声明：END  差异内容：END | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragSpringLoadingState；  API声明：CANCEL  差异内容：CANCEL | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：dragController；  API声明：interface DragSpringLoadingConfiguration  差异内容：interface DragSpringLoadingConfiguration | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragSpringLoadingConfiguration；  API声明：stillTimeLimit?: number;  差异内容：stillTimeLimit?: number; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragSpringLoadingConfiguration；  API声明：updateInterval?: number;  差异内容：updateInterval?: number; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragSpringLoadingConfiguration；  API声明：updateNotifyCount?: number;  差异内容：updateNotifyCount?: number; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragSpringLoadingConfiguration；  API声明：updateToFinishInterval?: number;  差异内容：updateToFinishInterval?: number; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：dragController；  API声明：interface SpringLoadingDragInfos  差异内容：interface SpringLoadingDragInfos | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：SpringLoadingDragInfos；  API声明：dataSummary?: unifiedDataChannel.Summary;  差异内容：dataSummary?: unifiedDataChannel.Summary; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：SpringLoadingDragInfos；  API声明：extraInfos?: string;  差异内容：extraInfos?: string; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：dragController；  API声明：class SpringLoadingContext  差异内容：class SpringLoadingContext | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：SpringLoadingContext；  API声明：state: DragSpringLoadingState;  差异内容：state: DragSpringLoadingState; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：SpringLoadingContext；  API声明：currentNotifySequence: number;  差异内容：currentNotifySequence: number; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：SpringLoadingContext；  API声明：dragInfos?: SpringLoadingDragInfos;  差异内容：dragInfos?: SpringLoadingDragInfos; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：SpringLoadingContext；  API声明：currentConfig?: DragSpringLoadingConfiguration;  差异内容：currentConfig?: DragSpringLoadingConfiguration; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：SpringLoadingContext；  API声明：abort(): void;  差异内容：abort(): void; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：SpringLoadingContext；  API声明：updateConfiguration(config: DragSpringLoadingConfiguration): void;  差异内容：updateConfiguration(config: DragSpringLoadingConfiguration): void; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：HalfScreenLaunchComponent；  API声明：onReceive?: Callback<Record<string, Object>>;  差异内容：onReceive?: Callback<Record<string, Object>>; | api/@ohos.atomicservice.HalfScreenLaunchComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：declare class TouchRecognizer  差异内容：declare class TouchRecognizer | component/gesture.d.ts |
| 新增API | NA | 类名：TouchRecognizer；  API声明：getEventTargetInfo(): EventTargetInfo;  差异内容：getEventTargetInfo(): EventTargetInfo; | component/gesture.d.ts |
| 新增API | NA | 类名：TouchRecognizer；  API声明：cancelTouch(): void;  差异内容：cancelTouch(): void; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明：type OnPrepareMenuCallback = (menuItems: Array<TextMenuItem>) => Array<TextMenuItem>;  差异内容：type OnPrepareMenuCallback = (menuItems: Array<TextMenuItem>) => Array<TextMenuItem>; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class ShaderStyle  差异内容：declare class ShaderStyle | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class LinearGradientStyle  差异内容：declare class LinearGradientStyle | component/text\_common.d.ts |
| 新增API | NA | 类名：LinearGradientStyle；  API声明：options: LinearGradientOptions;  差异内容：options: LinearGradientOptions; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class RadialGradientStyle  差异内容：declare class RadialGradientStyle | component/text\_common.d.ts |
| 新增API | NA | 类名：RadialGradientStyle；  API声明：options: RadialGradientOptions;  差异内容：options: RadialGradientOptions; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class ColorShaderStyle  差异内容：declare class ColorShaderStyle | component/text\_common.d.ts |
| 新增API | NA | 类名：ColorShaderStyle；  API声明：color: ResourceColor;  差异内容：color: ResourceColor; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum TextChangeReason  差异内容：declare enum TextChangeReason | component/text\_common.d.ts |
| 新增API | NA | 类名：TextChangeReason；  API声明：UNKNOWN = 0  差异内容：UNKNOWN = 0 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextChangeReason；  API声明：INPUT = 1  差异内容：INPUT = 1 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextChangeReason；  API声明：PASTE = 2  差异内容：PASTE = 2 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextChangeReason；  API声明：CUT = 3  差异内容：CUT = 3 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextChangeReason；  API声明：DRAG = 4  差异内容：DRAG = 4 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextChangeReason；  API声明：AUTO\_FILL = 5  差异内容：AUTO\_FILL = 5 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextChangeReason；  API声明：AI\_WRITE = 6  差异内容：AI\_WRITE = 6 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextChangeReason；  API声明：REDO = 7  差异内容：REDO = 7 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextChangeReason；  API声明：UNDO = 8  差异内容：UNDO = 8 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextChangeReason；  API声明：CONTROLLER = 9  差异内容：CONTROLLER = 9 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextChangeReason；  API声明：ACCESSIBILITY = 10  差异内容：ACCESSIBILITY = 10 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextChangeReason；  API声明：COLLABORATION = 11  差异内容：COLLABORATION = 11 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextChangeReason；  API声明：STYLUS = 12  差异内容：STYLUS = 12 | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum TextVerticalAlign  差异内容：declare enum TextVerticalAlign | component/text\_common.d.ts |
| 新增API | NA | 类名：TextVerticalAlign；  API声明：BASELINE = 0  差异内容：BASELINE = 0 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextVerticalAlign；  API声明：BOTTOM = 1  差异内容：BOTTOM = 1 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextVerticalAlign；  API声明：CENTER = 2  差异内容：CENTER = 2 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextVerticalAlign；  API声明：TOP = 3  差异内容：TOP = 3 | component/text\_common.d.ts |
| 删除API | 类名：global；  API声明：declare enum LocationIconStyle  差异内容：declare enum LocationIconStyle | NA | component/location\_button.d.ts |
| 删除API | 类名：LocationIconStyle；  API声明：FULL\_FILLED = 0  差异内容：FULL\_FILLED = 0 | NA | component/location\_button.d.ts |
| 删除API | 类名：LocationIconStyle；  API声明：LINES = 1  差异内容：LINES = 1 | NA | component/location\_button.d.ts |
| 删除API | 类名：global；  API声明：declare enum LocationDescription  差异内容：declare enum LocationDescription | NA | component/location\_button.d.ts |
| 删除API | 类名：LocationDescription；  API声明：CURRENT\_LOCATION = 0  差异内容：CURRENT\_LOCATION = 0 | NA | component/location\_button.d.ts |
| 删除API | 类名：LocationDescription；  API声明：ADD\_LOCATION = 1  差异内容：ADD\_LOCATION = 1 | NA | component/location\_button.d.ts |
| 删除API | 类名：LocationDescription；  API声明：SELECT\_LOCATION = 2  差异内容：SELECT\_LOCATION = 2 | NA | component/location\_button.d.ts |
| 删除API | 类名：LocationDescription；  API声明：SHARE\_LOCATION = 3  差异内容：SHARE\_LOCATION = 3 | NA | component/location\_button.d.ts |
| 删除API | 类名：LocationDescription；  API声明：SEND\_LOCATION = 4  差异内容：SEND\_LOCATION = 4 | NA | component/location\_button.d.ts |
| 删除API | 类名：LocationDescription；  API声明：LOCATING = 5  差异内容：LOCATING = 5 | NA | component/location\_button.d.ts |
| 删除API | 类名：LocationDescription；  API声明：LOCATION = 6  差异内容：LOCATION = 6 | NA | component/location\_button.d.ts |
| 删除API | 类名：LocationDescription；  API声明：SEND\_CURRENT\_LOCATION = 7  差异内容：SEND\_CURRENT\_LOCATION = 7 | NA | component/location\_button.d.ts |
| 删除API | 类名：LocationDescription；  API声明：RELOCATION = 8  差异内容：RELOCATION = 8 | NA | component/location\_button.d.ts |
| 删除API | 类名：LocationDescription；  API声明：PUNCH\_IN = 9  差异内容：PUNCH\_IN = 9 | NA | component/location\_button.d.ts |
| 删除API | 类名：LocationDescription；  API声明：CURRENT\_POSITION = 10  差异内容：CURRENT\_POSITION = 10 | NA | component/location\_button.d.ts |
| 删除API | 类名：global；  API声明：declare interface LocationButtonOptions  差异内容：declare interface LocationButtonOptions | NA | component/location\_button.d.ts |
| 删除API | 类名：LocationButtonOptions；  API声明：icon?: LocationIconStyle;  差异内容：icon?: LocationIconStyle; | NA | component/location\_button.d.ts |
| 删除API | 类名：LocationButtonOptions；  API声明：text?: LocationDescription;  差异内容：text?: LocationDescription; | NA | component/location\_button.d.ts |
| 删除API | 类名：LocationButtonOptions；  API声明：buttonType?: ButtonType;  差异内容：buttonType?: ButtonType; | NA | component/location\_button.d.ts |
| 删除API | 类名：global；  API声明：declare enum LocationButtonOnClickResult  差异内容：declare enum LocationButtonOnClickResult | NA | component/location\_button.d.ts |
| 删除API | 类名：LocationButtonOnClickResult；  API声明：SUCCESS = 0  差异内容：SUCCESS = 0 | NA | component/location\_button.d.ts |
| 删除API | 类名：LocationButtonOnClickResult；  API声明：TEMPORARY\_AUTHORIZATION\_FAILED = 1  差异内容：TEMPORARY\_AUTHORIZATION\_FAILED = 1 | NA | component/location\_button.d.ts |
| 删除API | 类名：global；  API声明：interface LocationButtonInterface  差异内容：interface LocationButtonInterface | NA | component/location\_button.d.ts |
| 删除API | 类名：global；  API声明：type LocationButtonCallback = (event: ClickEvent, result: LocationButtonOnClickResult, error?: BusinessError<void>) => void;  差异内容：type LocationButtonCallback = (event: ClickEvent, result: LocationButtonOnClickResult, error?: BusinessError<void>) => void; | NA | component/location\_button.d.ts |
| 删除API | 类名：global；  API声明：declare class LocationButtonAttribute  差异内容：declare class LocationButtonAttribute | NA | component/location\_button.d.ts |
| 删除API | 类名：LocationButtonAttribute；  API声明：onClick(event: LocationButtonCallback): LocationButtonAttribute;  差异内容：onClick(event: LocationButtonCallback): LocationButtonAttribute; | NA | component/location\_button.d.ts |
| 删除API | 类名：global；  API声明：declare const LocationButton: LocationButtonInterface;  差异内容：declare const LocationButton: LocationButtonInterface; | NA | component/location\_button.d.ts |
| 删除API | 类名：global；  API声明：declare const LocationButtonInstance: LocationButtonAttribute;  差异内容：declare const LocationButtonInstance: LocationButtonAttribute; | NA | component/location\_button.d.ts |
| 删除API | 类名：global；  API声明：export declare function isApiVersionGreaterOrEqual(apiVersion: string): boolean;  差异内容：export declare function isApiVersionGreaterOrEqual(apiVersion: string): boolean; | NA | api/@internal/full/global.d.ts |
| 删除API | 类名：SaveButtonAttribute；  API声明：tipPosition(position: SaveButtonTipPosition): SaveButtonAttribute;  差异内容：tipPosition(position: SaveButtonTipPosition): SaveButtonAttribute; | NA | component/save\_button.d.ts |
| 删除API | 类名：global；  API声明：declare enum SaveButtonTipPosition  差异内容：declare enum SaveButtonTipPosition | NA | component/save\_button.d.ts |
| 删除API | 类名：SaveButtonTipPosition；  API声明：ABOVE\_BOTTOM = 0  差异内容：ABOVE\_BOTTOM = 0 | NA | component/save\_button.d.ts |
| 删除API | 类名：SaveButtonTipPosition；  API声明：BELOW\_TOP = 1  差异内容：BELOW\_TOP = 1 | NA | component/save\_button.d.ts |
| 删除kit | 类名：global；  API声明：component\location\_button.d.ts  差异内容：ArkUI | 类名：global；  API声明：  差异内容：NA | component/location\_button.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.uiAppearance.d.ts  差异内容：ArkUI | api/@ohos.uiAppearance.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：SegmentButtonOptions；  API声明：borderRadiusMode?: BorderRadiusMode;  差异内容：borderRadiusMode?: BorderRadiusMode; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：SegmentButtonOptions；  API声明：backgroundBorderRadius?: LengthMetrics;  差异内容：backgroundBorderRadius?: LengthMetrics; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：SegmentButtonOptions；  API声明：itemBorderRadius?: LengthMetrics;  差异内容：itemBorderRadius?: LengthMetrics; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：ParagraphStyle；  API声明：readonly textVerticalAlign?: TextVerticalAlign;  差异内容：readonly textVerticalAlign?: TextVerticalAlign; | component/styled\_string.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：DrawModifier；  API声明：drawForeground?(drawContext: DrawContext): void;  差异内容：drawForeground?(drawContext: DrawContext): void; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CommonMethod；  API声明：ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>): T;  差异内容：ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>): T; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CommonMethod；  API声明：transform3D(transform: Optional<Matrix4Transit>): T;  差异内容：transform3D(transform: Optional<Matrix4Transit>): T; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CommonMethod；  API声明：onTouchTestDone(callback: TouchTestDoneCallback): T;  差异内容：onTouchTestDone(callback: TouchTestDoneCallback): T; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CommonMethod；  API声明：onDragSpringLoading(callback: Callback<SpringLoadingContext> | null, configuration?: DragSpringLoadingConfiguration): T;  差异内容：onDragSpringLoading(callback: Callback<SpringLoadingContext> | null, configuration?: DragSpringLoadingConfiguration): T; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：ScrollableCommonMethod；  API声明：onWillStopDragging(handler: OnWillStopDraggingCallback): T;  差异内容：onWillStopDragging(handler: OnWillStopDraggingCallback): T; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：RichEditorBaseController；  API声明：setTypingParagraphStyle(style: RichEditorParagraphStyle): void;  差异内容：setTypingParagraphStyle(style: RichEditorParagraphStyle): void; | component/rich\_editor.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：RichEditorAttribute；  API声明：enableAutoSpacing(enable: Optional<boolean>): RichEditorAttribute;  差异内容：enableAutoSpacing(enable: Optional<boolean>): RichEditorAttribute; | component/rich\_editor.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SearchAttribute；  API声明：enableAutoSpacing(enabled: Optional<boolean>): SearchAttribute;  差异内容：enableAutoSpacing(enabled: Optional<boolean>): SearchAttribute; | component/search.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextAttribute；  API声明：textVerticalAlign(textVerticalAlign: Optional<TextVerticalAlign>): TextAttribute;  差异内容：textVerticalAlign(textVerticalAlign: Optional<TextVerticalAlign>): TextAttribute; | component/text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextAttribute；  API声明：shaderStyle(shader: ShaderStyle): TextAttribute;  差异内容：shaderStyle(shader: ShaderStyle): TextAttribute; | component/text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextAttribute；  API声明：enableAutoSpacing(enabled: Optional<boolean>): TextAttribute;  差异内容：enableAutoSpacing(enabled: Optional<boolean>): TextAttribute; | component/text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextAreaAttribute；  API声明：enableAutoSpacing(enabled: Optional<boolean>): TextAreaAttribute;  差异内容：enableAutoSpacing(enabled: Optional<boolean>): TextAreaAttribute; | component/text\_area.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextInputAttribute；  API声明：enableAutoSpacing(enabled: Optional<boolean>): TextInputAttribute;  差异内容：enableAutoSpacing(enabled: Optional<boolean>): TextInputAttribute; | component/text\_input.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：BuilderNode；  API声明：inheritFreezeOptions(enabled: boolean): void;  差异内容：inheritFreezeOptions(enabled: boolean): void; | api/arkui/BuilderNode.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：ComponentContent；  API声明：inheritFreezeOptions(enabled: boolean): void;  差异内容：inheritFreezeOptions(enabled: boolean): void; | api/arkui/ComponentContent.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：ColorMetrics；  API声明：static colorWithSpace(colorSpace: ColorSpace, red: number, green: number, blue: number, alpha?: number): ColorMetrics;  差异内容：static colorWithSpace(colorSpace: ColorSpace, red: number, green: number, blue: number, alpha?: number): ColorMetrics; | api/arkui/Graphics.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：DatePickerAttribute；  API声明：canLoop(isLoop: Optional<boolean>): DatePickerAttribute;  差异内容：canLoop(isLoop: Optional<boolean>): DatePickerAttribute; | component/date\_picker.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：GestureRecognizer；  API声明：preventBegin(): void;  差异内容：preventBegin(): void; | component/gesture.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：GridAttribute；  API声明：focusWrapMode(mode: Optional<FocusWrapMode>): GridAttribute;  差异内容：focusWrapMode(mode: Optional<FocusWrapMode>): GridAttribute; | component/grid.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：ListAttribute；  API声明：focusWrapMode(mode: Optional<FocusWrapMode>): ListAttribute;  差异内容：focusWrapMode(mode: Optional<FocusWrapMode>): ListAttribute; | component/list.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：CanvasGradient；  API声明：addColorStop(offset: number, color: string): void;  差异内容：addColorStop(offset: number, color: string): void; | 类名：CanvasGradient；  API声明：addColorStop(offset: number, color: string | ColorMetrics): void;  差异内容：addColorStop(offset: number, color: string | ColorMetrics): void; | component/canvas.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：CommonMethod；  API声明：background(builder: CustomBuilder, options?: {  align?: Alignment;  }): T;  差异内容：background(builder: CustomBuilder, options?: {  align?: Alignment;  }): T; | 类名：CommonMethod；  API声明：background(content: CustomBuilder | ResourceColor, options?: BackgroundOptions): T;  差异内容：background(content: CustomBuilder | ResourceColor, options?: BackgroundOptions): T; | component/common.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：CommonMethod；  API声明：backgroundColor(color: Optional<ResourceColor>): T;  差异内容：backgroundColor(color: Optional<ResourceColor>): T; | 类名：CommonMethod；  API声明：backgroundColor(color: Optional<ResourceColor | ColorMetrics>): T;  差异内容：backgroundColor(color: Optional<ResourceColor | ColorMetrics>): T; | component/common.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：ImageAttribute；  API声明：fillColor(color: ResourceColor | ColorContent): ImageAttribute;  差异内容：fillColor(color: ResourceColor | ColorContent): ImageAttribute; | 类名：ImageAttribute；  API声明：fillColor(color: ResourceColor | ColorContent | ColorMetrics): ImageAttribute;  差异内容：fillColor(color: ResourceColor | ColorContent | ColorMetrics): ImageAttribute; | component/image.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：on(type: 'screenshotAppEvent', callback: Callback<ScreenshotEventType>): void;  差异内容：on(type: 'screenshotAppEvent', callback: Callback<ScreenshotEventType>): void; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：off(type: 'screenshotAppEvent', callback?: Callback<ScreenshotEventType>): void;  差异内容：off(type: 'screenshotAppEvent', callback?: Callback<ScreenshotEventType>): void; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：snapshotSync(): image.PixelMap;  差异内容：snapshotSync(): image.PixelMap; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：on(eventType: 'uiExtensionSecureLimitChange', callback: Callback<boolean>): void;  差异内容：on(eventType: 'uiExtensionSecureLimitChange', callback: Callback<boolean>): void; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：off(eventType: 'uiExtensionSecureLimitChange', callback?: Callback<boolean>): void;  差异内容：off(eventType: 'uiExtensionSecureLimitChange', callback?: Callback<boolean>): void; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：isImmersiveLayout(): boolean;  差异内容：isImmersiveLayout(): boolean; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：DragEvent；  API声明：getDragSource(): string;  差异内容：getDragSource(): string; | component/common.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：DragEvent；  API声明：isRemote(): boolean;  差异内容：isRemote(): boolean; | component/common.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：DragEvent；  API声明：setDataLoadParams(dataLoadParams: DataLoadParams): void;  差异内容：setDataLoadParams(dataLoadParams: DataLoadParams): void; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：SweepGradientOptions；  API声明：metricsColors?: Array<[  ColorMetrics,  number  ]>;  差异内容：metricsColors?: Array<[  ColorMetrics,  number  ]>; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ContentCoverOptions；  API声明：enableSafeArea?: boolean;  差异内容：enableSafeArea?: boolean; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：SheetOptions；  API声明：enableFloatingDragBar?: boolean;  差异内容：enableFloatingDragBar?: boolean; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：PopupCommonOptions；  API声明：avoidTarget?: AvoidanceMode;  差异内容：avoidTarget?: AvoidanceMode; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：TipsOptions；  API声明：showAtAnchor?: TipsAnchorType;  差异内容：showAtAnchor?: TipsAnchorType; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：PopupOptions；  API声明：avoidTarget?: AvoidanceMode;  差异内容：avoidTarget?: AvoidanceMode; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CustomPopupOptions；  API声明：avoidTarget?: AvoidanceMode;  差异内容：avoidTarget?: AvoidanceMode; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ContextMenuAnimationOptions；  API声明：hoverScaleInterruption?: boolean;  差异内容：hoverScaleInterruption?: boolean; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ContextMenuOptions；  API声明：modalMode?: ModalMode;  差异内容：modalMode?: ModalMode; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ContextMenuOptions；  API声明：onDidAppear?: Callback<void>;  差异内容：onDidAppear?: Callback<void>; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ContextMenuOptions；  API声明：onDidDisappear?: Callback<void>;  差异内容：onDidDisappear?: Callback<void>; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ContextMenuOptions；  API声明：onWillAppear?: Callback<void>;  差异内容：onWillAppear?: Callback<void>; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ContextMenuOptions；  API声明：onWillDisappear?: Callback<void>;  差异内容：onWillDisappear?: Callback<void>; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：RichEditorParagraphStyle；  API声明：textVerticalAlign?: TextVerticalAlign;  差异内容：textVerticalAlign?: TextVerticalAlign; | component/rich\_editor.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CommonSegmentButtonOptions；  API声明：borderRadiusMode?: BorderRadiusMode;  差异内容：borderRadiusMode?: BorderRadiusMode; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CommonSegmentButtonOptions；  API声明：backgroundBorderRadius?: LengthMetrics;  差异内容：backgroundBorderRadius?: LengthMetrics; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CommonSegmentButtonOptions；  API声明：itemBorderRadius?: LengthMetrics;  差异内容：itemBorderRadius?: LengthMetrics; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：DragInfo；  API声明：dataLoadParams?: unifiedDataChannel.DataLoadParams;  差异内容：dataLoadParams?: unifiedDataChannel.DataLoadParams; | api/@ohos.arkui.dragController.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ScrollEventInfo；  API声明：axis?: Axis;  差异内容：axis?: Axis; | api/@ohos.arkui.observer.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Display；  API声明：supportedRefreshRates?: Array<number>;  差异内容：supportedRefreshRates?: Array<number>; | api/@ohos.display.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ActionMenuOptions；  API声明：onDidAppear?: Callback<void>;  差异内容：onDidAppear?: Callback<void>; | api/@ohos.promptAction.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ActionMenuOptions；  API声明：onDidDisappear?: Callback<void>;  差异内容：onDidDisappear?: Callback<void>; | api/@ohos.promptAction.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ActionMenuOptions；  API声明：onWillAppear?: Callback<void>;  差异内容：onWillAppear?: Callback<void>; | api/@ohos.promptAction.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ActionMenuOptions；  API声明：onWillDisappear?: Callback<void>;  差异内容：onWillDisappear?: Callback<void>; | api/@ohos.promptAction.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：DatePickerDialogOptions；  API声明：canLoop?: boolean;  差异内容：canLoop?: boolean; | component/date\_picker.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ParagraphStyleInterface；  API声明：textVerticalAlign?: TextVerticalAlign;  差异内容：textVerticalAlign?: TextVerticalAlign; | component/styled\_string.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：TextDataDetectorConfig；  API声明：enablePreviewMenu?: boolean;  差异内容：enablePreviewMenu?: boolean; | component/text\_common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EditMenuOptions；  API声明：onPrepareMenu?: OnPrepareMenuCallback;  差异内容：onPrepareMenu?: OnPrepareMenuCallback; | component/text\_common.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：WindowStage；  API声明：setSupportedWindowModes(supportedWindowModes: Array<bundleManager.SupportWindowMode>): Promise<void>;  差异内容：setSupportedWindowModes(supportedWindowModes: Array<bundleManager.SupportWindowMode>): Promise<void>; | 类名：WindowStage；  API声明：setSupportedWindowModes(supportedWindowModes: Array<bundleManager.SupportWindowMode>, grayOutMaximizeButton: boolean): Promise<void>;  差异内容：setSupportedWindowModes(supportedWindowModes: Array<bundleManager.SupportWindowMode>, grayOutMaximizeButton: boolean): Promise<void>; | api/@ohos.window.d.ts |
| 删除导出符号 | 类名：global；  API声明：export declare function isApiVersionGreaterOrEqual(apiVersion: string): boolean;  差异内容：export declare function isApiVersionGreaterOrEqual(apiVersion: string): boolean; | 类名：global；  API声明：  差异内容：NA | api/@internal/full/global.d.ts |
