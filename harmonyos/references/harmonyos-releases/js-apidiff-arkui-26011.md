---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-26011
title: ArkUI
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > ArkUI
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:52+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:583e7e32680ab1b3be831c392fb060613036cd5d399799f91cad5794110c1c0a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API模型切换 | 类名：global；  API声明：declare type ResourceStr = string | Resource;  差异内容：NA | 类名：global；  API声明：declare type ResourceStr = string | Resource;  差异内容：stagemodelonly | component/units.d.ts |
| API卡片权限变更 | 类名：SpanAttribute；  API声明：fontVariations(fontVariations: Array<FontVariation>): SpanAttribute;  差异内容：NA | 类名：SpanAttribute；  API声明：fontVariations(fontVariations: Array<FontVariation>): SpanAttribute;  差异内容：form | component/span.d.ts |
| API卡片权限变更 | 类名：TextAttribute；  API声明：fontVariations(fontVariations: Array<FontVariation>): TextAttribute;  差异内容：NA | 类名：TextAttribute；  API声明：fontVariations(fontVariations: Array<FontVariation>): TextAttribute;  差异内容：form | component/text.d.ts |
| API卡片权限变更 | 类名：global；  API声明：declare type FontVariation = import('../api/@ohos.graphics.text').default.FontVariation;  差异内容：NA | 类名：global；  API声明：declare type FontVariation = import('../api/@ohos.graphics.text').default.FontVariation;  差异内容：form | component/text\_common.d.ts |
| API跨平台权限变更 | 类名：WindowType；  API声明：TYPE\_DIALOG = 16  差异内容：NA | 类名：WindowType；  API声明：TYPE\_DIALOG = 16  差异内容：crossplatform | api/@ohos.window.d.ts |
| API跨平台权限变更 | 类名：SubWindowOptions；  API声明：modalityType?: ModalityType;  差异内容：NA | 类名：SubWindowOptions；  API声明：modalityType?: ModalityType;  差异内容：crossplatform | api/@ohos.window.d.ts |
| API跨平台权限变更 | 类名：Window；  API声明：setWindowFocusable(isFocusable: boolean): Promise<void>;  差异内容：crossplatform | 类名：Window；  API声明：setWindowFocusable(isFocusable: boolean): Promise<void>;  差异内容：NA | api/@ohos.window.d.ts |
| API跨平台权限变更 | 类名：Window；  API声明：setWindowFocusable(isFocusable: boolean, callback: AsyncCallback<void>): void;  差异内容：crossplatform | 类名：Window；  API声明：setWindowFocusable(isFocusable: boolean, callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace dialog  差异内容：declare namespace dialog | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：dialog；  API声明：declare interface DialogTextStyleOptions  差异内容：declare interface DialogTextStyleOptions | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogTextStyleOptions；  API声明：wordBreak?: WordBreak;  差异内容：wordBreak?: WordBreak; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：dialog；  API声明：declare interface DialogButton  差异内容：declare interface DialogButton | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogButton；  API声明：value: ResourceStr;  差异内容：value: ResourceStr; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogButton；  API声明：fontColor?: ResourceColor;  差异内容：fontColor?: ResourceColor; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogButton；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogButton；  API声明：enabled?: boolean;  差异内容：enabled?: boolean; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogButton；  API声明：primary?: boolean;  差异内容：primary?: boolean; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogButton；  API声明：style?: DialogButtonStyle;  差异内容：style?: DialogButtonStyle; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogButton；  API声明：action: VoidCallback;  差异内容：action: VoidCallback; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：dialog；  API声明：declare interface DialogSheet  差异内容：declare interface DialogSheet | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogSheet；  API声明：title: ResourceStr;  差异内容：title: ResourceStr; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogSheet；  API声明：icon?: ResourceStr;  差异内容：icon?: ResourceStr; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogSheet；  API声明：action: VoidCallback;  差异内容：action: VoidCallback; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：dialog；  API声明：declare interface DialogBaseOptions  差异内容：declare interface DialogBaseOptions | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：controller?: DialogBaseController;  差异内容：controller?: DialogBaseController; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：width?: Dimension;  差异内容：width?: Dimension; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：height?: Dimension;  差异内容：height?: Dimension; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions;  差异内容：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：backgroundEffect?: BackgroundEffectOptions;  差异内容：backgroundEffect?: BackgroundEffectOptions; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：borderRadius?: Dimension | BorderRadiuses | LocalizedBorderRadiuses;  差异内容：borderRadius?: Dimension | BorderRadiuses | LocalizedBorderRadiuses; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：borderWidth?: Dimension | EdgeWidths | LocalizedEdgeWidths;  差异内容：borderWidth?: Dimension | EdgeWidths | LocalizedEdgeWidths; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：borderColor?: ResourceColor | EdgeColors | LocalizedEdgeColors;  差异内容：borderColor?: ResourceColor | EdgeColors | LocalizedEdgeColors; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：borderStyle?: BorderStyle | EdgeStyles;  差异内容：borderStyle?: BorderStyle | EdgeStyles; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：shadow?: ShadowOptions | ShadowStyle;  差异内容：shadow?: ShadowOptions | ShadowStyle; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：alignment?: DialogBaseAlignment;  差异内容：alignment?: DialogBaseAlignment; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：offset?: Offset;  差异内容：offset?: Offset; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：maskRect?: Rectangle;  差异内容：maskRect?: Rectangle; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：maskColor?: ResourceColor;  差异内容：maskColor?: ResourceColor; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：isModal?: boolean;  差异内容：isModal?: boolean; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：showInSubWindow?: boolean;  差异内容：showInSubWindow?: boolean; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：displayModeInSubWindow?: DialogDisplayMode;  差异内容：displayModeInSubWindow?: DialogDisplayMode; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：autoCancel?: boolean;  差异内容：autoCancel?: boolean; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：focusable?: boolean;  差异内容：focusable?: boolean; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：dialogTransition?: TransitionEffect;  差异内容：dialogTransition?: TransitionEffect; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：maskTransition?: TransitionEffect;  差异内容：maskTransition?: TransitionEffect; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：keyboardAvoidMode?: KeyboardAvoidMode;  差异内容：keyboardAvoidMode?: KeyboardAvoidMode; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：keyboardAvoidDistance?: LengthMetrics;  差异内容：keyboardAvoidDistance?: LengthMetrics; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：onWillAppear?: VoidCallback;  差异内容：onWillAppear?: VoidCallback; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：onDidAppear?: VoidCallback;  差异内容：onDidAppear?: VoidCallback; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：onWillDisappear?: VoidCallback;  差异内容：onWillDisappear?: VoidCallback; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：onDidDisappear?: VoidCallback;  差异内容：onDidDisappear?: VoidCallback; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：onWillDismiss?: Callback<DialogDismissal>;  差异内容：onWillDismiss?: Callback<DialogDismissal>; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：enableHoverMode?: boolean;  差异内容：enableHoverMode?: boolean; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：hoverModeArea?: HoverModeAreaType;  差异内容：hoverModeArea?: HoverModeAreaType; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：levelMode?: LevelMode;  差异内容：levelMode?: LevelMode; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：levelUniqueId?: number;  差异内容：levelUniqueId?: number; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：immersiveMode?: ImmersiveMode;  差异内容：immersiveMode?: ImmersiveMode; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：levelOrder?: LevelOrder;  差异内容：levelOrder?: LevelOrder; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseOptions；  API声明：systemMaterial?: SystemUiMaterial;  差异内容：systemMaterial?: SystemUiMaterial; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：dialog；  API声明：declare interface DialogMessage  差异内容：declare interface DialogMessage | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogMessage；  API声明：content: ResourceStr;  差异内容：content: ResourceStr; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：dialog；  API声明：declare interface DialogStyleOptions  差异内容：declare interface DialogStyleOptions | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogStyleOptions；  API声明：title?: ResourceStr;  差异内容：title?: ResourceStr; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogStyleOptions；  API声明：subtitle?: ResourceStr;  差异内容：subtitle?: ResourceStr; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogStyleOptions；  API声明：message?: DialogMessage;  差异内容：message?: DialogMessage; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogStyleOptions；  API声明：buttons?: Array<DialogButton>;  差异内容：buttons?: Array<DialogButton>; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogStyleOptions；  API声明：buttonDirection?: DialogButtonOrientation;  差异内容：buttonDirection?: DialogButtonOrientation; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogStyleOptions；  API声明：sheets?: Array<DialogSheet>;  差异内容：sheets?: Array<DialogSheet>; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogStyleOptions；  API声明：gridCount?: number;  差异内容：gridCount?: number; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：dialog；  API声明：declare interface DialogCustomOptions  差异内容：declare interface DialogCustomOptions | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogCustomOptions；  API声明：customStyle?: boolean;  差异内容：customStyle?: boolean; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：global；  API声明：export class DialogBaseController  差异内容：export class DialogBaseController | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseController；  API声明：close(): void;  差异内容：close(): void; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseController；  API声明：getState(): DialogState;  差异内容：getState(): DialogState; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum DialogBaseAlignment  差异内容：export enum DialogBaseAlignment | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseAlignment；  API声明：TOP = 0  差异内容：TOP = 0 | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseAlignment；  API声明：CENTER = 1  差异内容：CENTER = 1 | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseAlignment；  API声明：BOTTOM = 2  差异内容：BOTTOM = 2 | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseAlignment；  API声明：DEFAULT = 3  差异内容：DEFAULT = 3 | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseAlignment；  API声明：TOP\_START = 4  差异内容：TOP\_START = 4 | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseAlignment；  API声明：TOP\_END = 5  差异内容：TOP\_END = 5 | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseAlignment；  API声明：CENTER\_START = 6  差异内容：CENTER\_START = 6 | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseAlignment；  API声明：CENTER\_END = 7  差异内容：CENTER\_END = 7 | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseAlignment；  API声明：BOTTOM\_START = 8  差异内容：BOTTOM\_START = 8 | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogBaseAlignment；  API声明：BOTTOM\_END = 9  差异内容：BOTTOM\_END = 9 | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum DialogButtonOrientation  差异内容：export enum DialogButtonOrientation | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogButtonOrientation；  API声明：AUTO = 0  差异内容：AUTO = 0 | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogButtonOrientation；  API声明：HORIZONTAL = 1  差异内容：HORIZONTAL = 1 | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogButtonOrientation；  API声明：VERTICAL = 2  差异内容：VERTICAL = 2 | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum DialogState  差异内容：export enum DialogState | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogState；  API声明：UNINITIALIZED = 0  差异内容：UNINITIALIZED = 0 | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogState；  API声明：INITIALIZED = 1  差异内容：INITIALIZED = 1 | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogState；  API声明：APPEARING = 2  差异内容：APPEARING = 2 | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogState；  API声明：APPEARED = 3  差异内容：APPEARED = 3 | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogState；  API声明：DISAPPEARING = 4  差异内容：DISAPPEARING = 4 | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogState；  API声明：DISAPPEARED = 5  差异内容：DISAPPEARED = 5 | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface DialogResult  差异内容：export interface DialogResult | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogResult；  API声明：dialogId: number;  差异内容：dialogId: number; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface DialogDismissal  差异内容：export interface DialogDismissal | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogDismissal；  API声明：dismiss: VoidCallback;  差异内容：dismiss: VoidCallback; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：DialogDismissal；  API声明：reason: DismissReason;  差异内容：reason: DismissReason; | api/@ohos.arkui.dialog.d.ts |
| 新增API | NA | 类名：window；  API声明：enum FocusChangeReason  差异内容：enum FocusChangeReason | api/@ohos.window.d.ts |
| 新增API | NA | 类名：FocusChangeReason；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：FocusChangeReason；  API声明：CLICK = 1  差异内容：CLICK = 1 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：interface WindowFocusState  差异内容：interface WindowFocusState | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowFocusState；  API声明：isFocused: boolean;  差异内容：isFocused: boolean; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowFocusState；  API声明：focusChangeReason: FocusChangeReason;  差异内容：focusChangeReason: FocusChangeReason; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowFocusState；  API声明：nextFocusedWindowId?: number;  差异内容：nextFocusedWindowId?: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowFocusState；  API声明：prevFocusedWindowId?: number;  差异内容：prevFocusedWindowId?: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：enum WindowPosition  差异内容：enum WindowPosition | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowPosition；  API声明：NOT\_TOPMOST = -3  差异内容：NOT\_TOPMOST = -3 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowPosition；  API声明：TOPMOST = -2  差异内容：TOPMOST = -2 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowPosition；  API声明：BOTTOM = -1  差异内容：BOTTOM = -1 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowPosition；  API声明：TOP = 0  差异内容：TOP = 0 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：interface WindowPositionParams  差异内容：interface WindowPositionParams | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowPositionParams；  API声明：windowId: number;  差异内容：windowId: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowPositionParams；  API声明：insertAfter: number;  差异内容：insertAfter: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：function setWindowPosition(list: Array<WindowPositionParams>): Promise<void>;  差异内容：function setWindowPosition(list: Array<WindowPositionParams>): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowCreateParams；  API声明：minimizeOnStart?: boolean;  差异内容：minimizeOnStart?: boolean; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowCreateParams；  API声明：excludeFromDock?: boolean;  差异内容：excludeFromDock?: boolean; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowCreateParams；  API声明：excludeFromRecent?: boolean;  差异内容：excludeFromRecent?: boolean; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：onWindowFocusStateChange(callback: Callback<WindowFocusState>): void;  差异内容：onWindowFocusStateChange(callback: Callback<WindowFocusState>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：offWindowFocusStateChange(callback?: Callback<WindowFocusState>): void;  差异内容：offWindowFocusStateChange(callback?: Callback<WindowFocusState>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：DataReloadOperation；  API声明：reuseImmediately?: boolean;  差异内容：reuseImmediately?: boolean; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：RichEditorImageSpanStyle；  API声明：resizable?: ResizableOptions;  差异内容：resizable?: ResizableOptions; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorImageSpanStyleResult；  API声明：resizable?: ResizableOptions;  差异内容：resizable?: ResizableOptions; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：SubHeader；  API声明：@Prop  endIcon?: ResourceStr;  差异内容：@Prop  endIcon?: ResourceStr; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SubHeader；  API声明：endIconSymbolOptions?: SymbolOptions;  差异内容：endIconSymbolOptions?: SymbolOptions; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SubHeaderV2；  API声明：@Param  readonly endIcon?: SubHeaderV2IconType;  差异内容：@Param  readonly endIcon?: SubHeaderV2IconType; | api/@ohos.arkui.advanced.SubHeaderV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export class DialogPresenter  差异内容：export class DialogPresenter | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：DialogPresenter；  API声明：present(options?: dialog.DialogStyleOptions): Promise<DialogResult>;  差异内容：present(options?: dialog.DialogStyleOptions): Promise<DialogResult>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：DialogPresenter；  API声明：present(content: CustomBuilder | CustomBuilderWithId | ComponentContent<Object>, options?: dialog.DialogCustomOptions): Promise<DialogResult>;  差异内容：present(content: CustomBuilder | CustomBuilderWithId | ComponentContent<Object>, options?: dialog.DialogCustomOptions): Promise<DialogResult>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：DialogPresenter；  API声明：update(content: ComponentContent<Object>, options?: dialog.DialogBaseOptions): Promise<void>;  差异内容：update(content: ComponentContent<Object>, options?: dialog.DialogBaseOptions): Promise<void>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：DialogPresenter；  API声明：dismiss(target: number | ComponentContent<Object>): Promise<void>;  差异内容：dismiss(target: number | ComponentContent<Object>): Promise<void>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getDialogPresenter(): DialogPresenter;  差异内容：getDialogPresenter(): DialogPresenter; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：titleBarHoverMode?: SheetTitleBarHoverMode;  差异内容：titleBarHoverMode?: SheetTitleBarHoverMode; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：scrollBarState?: BarState;  差异内容：scrollBarState?: BarState; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum SheetTitleBarHoverMode  差异内容：declare enum SheetTitleBarHoverMode | component/common.d.ts |
| 新增API | NA | 类名：SheetTitleBarHoverMode；  API声明：STANDARD = 0  差异内容：STANDARD = 0 | component/common.d.ts |
| 新增API | NA | 类名：SheetTitleBarHoverMode；  API声明：STACK = 1  差异内容：STACK = 1 | component/common.d.ts |
| 新增API | NA | 类名：ImageAnimatorAttribute；  API声明：interpolation(value: ImageInterpolation): ImageAnimatorAttribute;  差异内容：interpolation(value: ImageInterpolation): ImageAnimatorAttribute; | component/image\_animator.d.ts |
| 新增API | NA | 类名：ImageSpanAttribute；  API声明：resizable(value: ResizableOptions): ImageSpanAttribute;  差异内容：resizable(value: ResizableOptions): ImageSpanAttribute; | component/image\_span.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface PreloadOptions  差异内容：declare interface PreloadOptions | component/navigation.d.ts |
| 新增API | NA | 类名：PreloadOptions；  API声明：onDestroy?: Callback<void>;  差异内容：onDestroy?: Callback<void>; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：preloadPath(info: NavPathInfo, options?: PreloadOptions): Promise<void>;  差异内容：preloadPath(info: NavPathInfo, options?: PreloadOptions): Promise<void>; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationConfiguration；  API声明：clearContentStackOnPrimaryNavigation?: boolean;  差异内容：clearContentStackOnPrimaryNavigation?: boolean; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationConfiguration；  API声明：recyclePagesOnLowMemory?: boolean;  差异内容：recyclePagesOnLowMemory?: boolean; | component/navigation.d.ts |
| 新增API | NA | 类名：ImageAttachment；  API声明：readonly resizable?: ResizableOptions;  差异内容：readonly resizable?: ResizableOptions; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ResourceImageAttachmentOptions；  API声明：resizable?: ResizableOptions;  差异内容：resizable?: ResizableOptions; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ImageAttachmentInterface；  API声明：resizable?: ResizableOptions;  差异内容：resizable?: ResizableOptions; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum TabsSidebarDisplayStyle  差异内容：declare enum TabsSidebarDisplayStyle | component/tabs.d.ts |
| 新增API | NA | 类名：TabsSidebarDisplayStyle；  API声明：EMBED = 0  差异内容：EMBED = 0 | component/tabs.d.ts |
| 新增API | NA | 类名：TabsSidebarDisplayStyle；  API声明：DISPLACE = 1  差异内容：DISPLACE = 1 | component/tabs.d.ts |
| 新增API | NA | 类名：TabsController；  API声明：getBarDisplayMode(): TabBarDisplayMode;  差异内容：getBarDisplayMode(): TabBarDisplayMode; | component/tabs.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum TabBarStyle  差异内容：declare enum TabBarStyle | component/tabs.d.ts |
| 新增API | NA | 类名：TabBarStyle；  API声明：BOTTOM = 0  差异内容：BOTTOM = 0 | component/tabs.d.ts |
| 新增API | NA | 类名：TabBarStyle；  API声明：SIDEBAR = 1  差异内容：SIDEBAR = 1 | component/tabs.d.ts |
| 新增API | NA | 类名：TabBarStyle；  API声明：SIDEBAR\_ADAPTABLE = 2  差异内容：SIDEBAR\_ADAPTABLE = 2 | component/tabs.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type TabsSidebarSearchFilterCallback = (tabIndex: number, text: string) => boolean;  差异内容：declare type TabsSidebarSearchFilterCallback = (tabIndex: number, text: string) => boolean; | component/tabs.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface TabsSidebarSearchableOptions  差异内容：declare interface TabsSidebarSearchableOptions | component/tabs.d.ts |
| 新增API | NA | 类名：TabsSidebarSearchableOptions；  API声明：searchText?: ResourceStr;  差异内容：searchText?: ResourceStr; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsSidebarSearchableOptions；  API声明：placeholder?: ResourceStr;  差异内容：placeholder?: ResourceStr; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsSidebarSearchableOptions；  API声明：searchCallback?: (text: string) => void;  差异内容：searchCallback?: (text: string) => void; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsSidebarSearchableOptions；  API声明：searchFilter?: TabsSidebarSearchFilterCallback;  差异内容：searchFilter?: TabsSidebarSearchFilterCallback; | component/tabs.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum TabBarDisplayMode  差异内容：declare enum TabBarDisplayMode | component/tabs.d.ts |
| 新增API | NA | 类名：TabBarDisplayMode；  API声明：BOTTOM\_TABBAR = 0  差异内容：BOTTOM\_TABBAR = 0 | component/tabs.d.ts |
| 新增API | NA | 类名：TabBarDisplayMode；  API声明：SIDEBAR = 1  差异内容：SIDEBAR = 1 | component/tabs.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface TabsBreakpointType  差异内容：declare interface TabsBreakpointType | component/tabs.d.ts |
| 新增API | NA | 类名：TabsBreakpointType；  API声明：sm?: T;  差异内容：sm?: T; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsBreakpointType；  API声明：md?: T;  差异内容：md?: T; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsBreakpointType；  API声明：lg?: T;  差异内容：lg?: T; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：barStyle(style: Optional<TabBarStyle>): TabsAttribute;  差异内容：barStyle(style: Optional<TabBarStyle>): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：sidebarPosition(position: Optional<BarPosition>): TabsAttribute;  差异内容：sidebarPosition(position: Optional<BarPosition>): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：sidebarHeader(header: Optional<ComponentContent>): TabsAttribute;  差异内容：sidebarHeader(header: Optional<ComponentContent>): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：sidebarSearchable(searchOptions?: TabsSidebarSearchableOptions): TabsAttribute;  差异内容：sidebarSearchable(searchOptions?: TabsSidebarSearchableOptions): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：barDisplayModeBreakpoint(style: Optional<TabsBreakpointType<TabBarDisplayMode>>): TabsAttribute;  差异内容：barDisplayModeBreakpoint(style: Optional<TabsBreakpointType<TabBarDisplayMode>>): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：onBarDisplayModeChange(callback: Optional<Callback<TabBarDisplayMode>>): TabsAttribute;  差异内容：onBarDisplayModeChange(callback: Optional<Callback<TabBarDisplayMode>>): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：sidebarSelectedIconColor(value: Optional<ResourceColor>): TabsAttribute;  差异内容：sidebarSelectedIconColor(value: Optional<ResourceColor>): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：sidebarSelectedTextColor(value: Optional<ResourceColor>): TabsAttribute;  差异内容：sidebarSelectedTextColor(value: Optional<ResourceColor>): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：sidebarUnselectedIconColor(value: Optional<ResourceColor>): TabsAttribute;  差异内容：sidebarUnselectedIconColor(value: Optional<ResourceColor>): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：sidebarUnselectedTextColor(value: Optional<ResourceColor>): TabsAttribute;  差异内容：sidebarUnselectedTextColor(value: Optional<ResourceColor>): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：sidebarSelectedBoardColor(value: Optional<ResourceColor>): TabsAttribute;  差异内容：sidebarSelectedBoardColor(value: Optional<ResourceColor>): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：sidebarWidth(value: Optional<Length>): TabsAttribute;  差异内容：sidebarWidth(value: Optional<Length>): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：minSidebarWidth(value: Optional<Length>): TabsAttribute;  差异内容：minSidebarWidth(value: Optional<Length>): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：maxSidebarWidth(value: Optional<Length>): TabsAttribute;  差异内容：maxSidebarWidth(value: Optional<Length>): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：minContentWidth(value: Optional<Length>): TabsAttribute;  差异内容：minContentWidth(value: Optional<Length>): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：sidebarBackgroundColor(value: Optional<ResourceColor>): TabsAttribute;  差异内容：sidebarBackgroundColor(value: Optional<ResourceColor>): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：sidebarBackgroundBlurStyle(value: Optional<BlurStyle>): TabsAttribute;  差异内容：sidebarBackgroundBlurStyle(value: Optional<BlurStyle>): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：sidebarDivider(value: Optional<DividerStyle>): TabsAttribute;  差异内容：sidebarDivider(value: Optional<DividerStyle>): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：sidebarDisplayStyle(style: Optional<TabsSidebarDisplayStyle>): TabsAttribute;  差异内容：sidebarDisplayStyle(style: Optional<TabsSidebarDisplayStyle>): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum TabVisibility  差异内容：declare enum TabVisibility | component/tab\_content.d.ts |
| 新增API | NA | 类名：TabVisibility；  API声明：VISIBLE = 0  差异内容：VISIBLE = 0 | component/tab\_content.d.ts |
| 新增API | NA | 类名：TabVisibility；  API声明：HIDDEN = 1  差异内容：HIDDEN = 1 | component/tab\_content.d.ts |
| 新增API | NA | 类名：TabContentAttribute；  API声明：tabBarVisibility(visibility: TabVisibility, displayMode?: TabBarDisplayMode): TabContentAttribute;  差异内容：tabBarVisibility(visibility: TabVisibility, displayMode?: TabBarDisplayMode): TabContentAttribute; | component/tab\_content.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.arkui.dialog.d.ts  差异内容：ArkUI | api/@ohos.arkui.dialog.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：DataChangeListener；  API声明：onDataReloaded(): void;  差异内容：onDataReloaded(): void; | 类名：DataChangeListener；  API声明：onDataReloaded(reuseImmediately: boolean): void;  差异内容：onDataReloaded(reuseImmediately: boolean): void; | component/lazy\_for\_each.d.ts |
