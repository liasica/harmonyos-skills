---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-6011
title: ArkUI
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Beta1引入的API > ArkUI
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:56+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:25bb00d1d160388e25d18ed324ef50141eebf45ee494e461da097fdf1020595b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：Window；  API声明：setRelativePositionToParentWindowEnabled(enabled: boolean, anchor?: WindowAnchor, offsetX?: number, offsetY?: number): Promise<void>;  差异内容：1300016 | 类名：Window；  API声明：setRelativePositionToParentWindowEnabled(enabled: boolean, anchor?: WindowAnchor, offsetX?: number, offsetY?: number): Promise<void>;  差异内容：NA | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：interface MainWindowInfo  差异内容：interface MainWindowInfo | api/@ohos.window.d.ts |
| 新增API | NA | 类名：MainWindowInfo；  API声明：displayId: number;  差异内容：displayId: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：MainWindowInfo；  API声明：windowId: number;  差异内容：windowId: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：MainWindowInfo；  API声明：showing: boolean;  差异内容：showing: boolean; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：MainWindowInfo；  API声明：label: string;  差异内容：label: string; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：interface WindowSnapshotConfiguration  差异内容：interface WindowSnapshotConfiguration | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowSnapshotConfiguration；  API声明：useCache?: boolean;  差异内容：useCache?: boolean; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：function setWatermarkImageForAppWindows(pixelMap: image.PixelMap | undefined): Promise<void>;  差异内容：function setWatermarkImageForAppWindows(pixelMap: image.PixelMap | undefined): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：function getAllMainWindowInfo(): Promise<Array<MainWindowInfo>>;  差异内容：function getAllMainWindowInfo(): Promise<Array<MainWindowInfo>>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：function getMainWindowSnapshot(windowId: Array<number>, config: WindowSnapshotConfiguration): Promise<Array<image.PixelMap | undefined>>;  差异内容：function getMainWindowSnapshot(windowId: Array<number>, config: WindowSnapshotConfiguration): Promise<Array<image.PixelMap | undefined>>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum VisibilityChangeReason  差异内容：declare enum VisibilityChangeReason | component/nav\_destination.d.ts |
| 新增API | NA | 类名：VisibilityChangeReason；  API声明：TRANSITION = 0  差异内容：TRANSITION = 0 | component/nav\_destination.d.ts |
| 新增API | NA | 类名：VisibilityChangeReason；  API声明：CONTENT\_COVER = 1  差异内容：CONTENT\_COVER = 1 | component/nav\_destination.d.ts |
| 新增API | NA | 类名：VisibilityChangeReason；  API声明：APP\_STATE = 2  差异内容：APP\_STATE = 2 | component/nav\_destination.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface DrawableDescriptorLoadedResult  差异内容：export interface DrawableDescriptorLoadedResult | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：DrawableDescriptorLoadedResult；  API声明：imageWidth: number;  差异内容：imageWidth: number; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：DrawableDescriptorLoadedResult；  API声明：imageHeight: number;  差异内容：imageHeight: number; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface AnimationController  差异内容：export interface AnimationController | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：AnimationController；  API声明：start(): void;  差异内容：start(): void; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：AnimationController；  API声明：stop(): void;  差异内容：stop(): void; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：AnimationController；  API声明：pause(): void;  差异内容：pause(): void; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：AnimationController；  API声明：resume(): void;  差异内容：resume(): void; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：AnimationController；  API声明：getStatus(): AnimationStatus;  差异内容：getStatus(): AnimationStatus; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface CheckBoxGroupConfiguration  差异内容：declare interface CheckBoxGroupConfiguration | component/checkboxgroup.d.ts |
| 新增API | NA | 类名：CheckBoxGroupConfiguration；  API声明：name: string;  差异内容：name: string; | component/checkboxgroup.d.ts |
| 新增API | NA | 类名：CheckBoxGroupConfiguration；  API声明：status: SelectStatus;  差异内容：status: SelectStatus; | component/checkboxgroup.d.ts |
| 新增API | NA | 类名：CheckBoxGroupConfiguration；  API声明：triggerChange: Callback<boolean>;  差异内容：triggerChange: Callback<boolean>; | component/checkboxgroup.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type OnDidStopDraggingCallback = (willFling: boolean) => void;  差异内容：declare type OnDidStopDraggingCallback = (willFling: boolean) => void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum ListItemSwipeActionDirection  差异内容：declare enum ListItemSwipeActionDirection | component/list\_item.d.ts |
| 新增API | NA | 类名：ListItemSwipeActionDirection；  API声明：START = 0  差异内容：START = 0 | component/list\_item.d.ts |
| 新增API | NA | 类名：ListItemSwipeActionDirection；  API声明：END = 1  差异内容：END = 1 | component/list\_item.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class ListItemSwipeActionManager  差异内容：declare class ListItemSwipeActionManager | component/list\_item.d.ts |
| 新增API | NA | 类名：ListItemSwipeActionManager；  API声明：static expand(node: FrameNode, direction: ListItemSwipeActionDirection): void;  差异内容：static expand(node: FrameNode, direction: ListItemSwipeActionDirection): void; | component/list\_item.d.ts |
| 新增API | NA | 类名：ListItemSwipeActionManager；  API声明：static collapse(node: FrameNode): void;  差异内容：static collapse(node: FrameNode): void; | component/list\_item.d.ts |
| 新增API | NA | 类名：SaveButtonOnClickResult；  API声明：CANCELED\_BY\_USER = 2  差异内容：CANCELED\_BY\_USER = 2 | component/save\_button.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum TextContentAlign  差异内容：declare enum TextContentAlign | component/text\_common.d.ts |
| 新增API | NA | 类名：TextContentAlign；  API声明：TOP = 0  差异内容：TOP = 0 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextContentAlign；  API声明：CENTER = 1  差异内容：CENTER = 1 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextContentAlign；  API声明：BOTTOM = 2  差异内容：BOTTOM = 2 | component/text\_common.d.ts |
| 函数变更 | 类名：NavDestinationAttribute；  API声明：onShown(callback: () => void): NavDestinationAttribute;  差异内容：callback: () => void | 类名：NavDestinationAttribute；  API声明：onShown(callback: Callback<VisibilityChangeReason>): NavDestinationAttribute;  差异内容：callback: Callback<VisibilityChangeReason> | component/nav\_destination.d.ts |
| 函数变更 | 类名：NavDestinationAttribute；  API声明：onHidden(callback: () => void): NavDestinationAttribute;  差异内容：callback: () => void | 类名：NavDestinationAttribute；  API声明：onHidden(callback: Callback<VisibilityChangeReason>): NavDestinationAttribute;  差异内容：callback: Callback<VisibilityChangeReason> | component/nav\_destination.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：ImageAttachment；  API声明：readonly sizeInVp?: SizeOptions;  差异内容：readonly sizeInVp?: SizeOptions; | component/styled\_string.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：DrawableDescriptor；  API声明：loadSync(): DrawableDescriptorLoadedResult;  差异内容：loadSync(): DrawableDescriptorLoadedResult; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：DrawableDescriptor；  API声明：load(): Promise<DrawableDescriptorLoadedResult>;  差异内容：load(): Promise<DrawableDescriptorLoadedResult>; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：AnimatedDrawableDescriptor；  API声明：getAnimationController(id?: string): AnimationController | undefined;  差异内容：getAnimationController(id?: string): AnimationController | undefined; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIContext；  API声明：static setResourceManagerCacheMaxCountForHSP(count: number): void;  差异内容：static setResourceManagerCacheMaxCountForHSP(count: number): void; | api/@ohos.arkui.UIContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：FrameNode；  API声明：invalidateAttributes(): void;  差异内容：invalidateAttributes(): void; | api/arkui/FrameNode.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CheckboxGroupAttribute；  API声明：contentModifier(modifier: Optional<ContentModifier<CheckBoxGroupConfiguration>>): CheckboxGroupAttribute;  差异内容：contentModifier(modifier: Optional<ContentModifier<CheckBoxGroupConfiguration>>): CheckboxGroupAttribute; | component/checkboxgroup.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CommonMethod；  API声明：allowForceDark(value: boolean): T;  差异内容：allowForceDark(value: boolean): T; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：ScrollableCommonMethod；  API声明：onWillStartDragging(handler: VoidCallback): T;  差异内容：onWillStartDragging(handler: VoidCallback): T; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：ScrollableCommonMethod；  API声明：onDidStopDragging(handler: OnDidStopDraggingCallback): T;  差异内容：onDidStopDragging(handler: OnDidStopDraggingCallback): T; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：ScrollableCommonMethod；  API声明：onWillStartFling(handler: VoidCallback): T;  差异内容：onWillStartFling(handler: VoidCallback): T; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：ScrollableCommonMethod；  API声明：onDidStopFling(handler: VoidCallback): T;  差异内容：onDidStopFling(handler: VoidCallback): T; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：ImageAttribute；  API声明：supportSvg2(enable: boolean): ImageAttribute;  差异内容：supportSvg2(enable: boolean): ImageAttribute; | component/image.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：NavigationAttribute；  API声明：enableVisibilityLifecycleWithContentCover(isEnabled: Optional<boolean>): NavigationAttribute;  差异内容：enableVisibilityLifecycleWithContentCover(isEnabled: Optional<boolean>): NavigationAttribute; | component/navigation.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：RichEditorAttribute；  API声明：scrollBarColor(color: Optional<ColorMetrics>): RichEditorAttribute;  差异内容：scrollBarColor(color: Optional<ColorMetrics>): RichEditorAttribute; | component/rich\_editor.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SaveButtonAttribute；  API声明：userCancelEvent(enabled: boolean): SaveButtonAttribute;  差异内容：userCancelEvent(enabled: boolean): SaveButtonAttribute; | component/save\_button.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextAttribute；  API声明：textContentAlign(textContentAlign: Optional<TextContentAlign>): TextAttribute;  差异内容：textContentAlign(textContentAlign: Optional<TextContentAlign>): TextAttribute; | component/text.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：SliderAttribute；  API声明：blockColor(value: ResourceColor): SliderAttribute;  差异内容：blockColor(value: ResourceColor): SliderAttribute; | 类名：SliderAttribute；  API声明：blockColor(value: ResourceColor | LinearGradient): SliderAttribute;  差异内容：blockColor(value: ResourceColor | LinearGradient): SliderAttribute; | component/slider.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：setContentAspectRatio(ratio: number, isPersistent?: boolean, needUpdateRect?: boolean): Promise<void>;  差异内容：setContentAspectRatio(ratio: number, isPersistent?: boolean, needUpdateRect?: boolean): Promise<void>; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AxisEvent；  API声明：getPinchAxisScaleValue(): number;  差异内容：getPinchAxisScaleValue(): number; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：AnimationOptions；  API声明：frameDurations?: Array<number>;  差异内容：frameDurations?: Array<number>; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：AnimationOptions；  API声明：autoPlay?: boolean;  差异内容：autoPlay?: boolean; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CaptureOption；  API声明：blackWindowIds?: Array<number>;  差异内容：blackWindowIds?: Array<number>; | api/@ohos.screenshot.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：BaseEvent；  API声明：axisPinch?: number;  差异内容：axisPinch?: number; | component/common.d.ts |
