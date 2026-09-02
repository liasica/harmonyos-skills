---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-6111
title: ArkUI
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > ArkUI
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:feefa51d9009be9f99a8caca2d1a06b10316e1dead3fa3f03254ef7c1879bca4
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：CrownAction；  API声明：BEGIN = 0  差异内容：NA | 类名：CrownAction；  API声明：BEGIN = 0  差异内容：24 dynamic | component/enums.d.ts |
| 新增错误码 | 类名：WindowProxy；  API声明：createSubWindowWithOptions(name: string, subWindowOptions: window.SubWindowOptions): Promise<window.Window>;  差异内容：NA | 类名：WindowProxy；  API声明：createSubWindowWithOptions(name: string, subWindowOptions: window.SubWindowOptions): Promise<window.Window>;  差异内容：1300035 | api/@ohos.arkui.uiExtension.d.ts |
| 新增错误码 | 类名：WindowProxy；  API声明：createSubWindowWithOptions(name: string, subWindowConfig: window.SubWindowOptions, followCreatorLifecycle: boolean): Promise<window.Window>;  差异内容：NA | 类名：WindowProxy；  API声明：createSubWindowWithOptions(name: string, subWindowConfig: window.SubWindowOptions, followCreatorLifecycle: boolean): Promise<window.Window>;  差异内容：1300035 | api/@ohos.arkui.uiExtension.d.ts |
| 函数变更 | 类名：SecurityComponentMethod；  API声明：id(description: string): T;  差异内容：description: string | 类名：SecurityComponentMethod；  API声明：id(id: string): T;  差异内容：id: string | component/security\_component.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface DynamicLayoutInterface  差异内容：export interface DynamicLayoutInterface | api/@ohos.arkui.components.ArkDynamicLayout.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare class DynamicLayoutAttribute  差异内容：export declare class DynamicLayoutAttribute | api/@ohos.arkui.components.ArkDynamicLayout.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare const DynamicLayout: DynamicLayoutInterface;  差异内容：export declare const DynamicLayout: DynamicLayoutInterface; | api/@ohos.arkui.components.ArkDynamicLayout.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare const DynamicLayoutInstance: DynamicLayoutAttribute;  差异内容：export declare const DynamicLayoutInstance: DynamicLayoutAttribute; | api/@ohos.arkui.components.ArkDynamicLayout.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface LayoutAlgorithm  差异内容：export interface LayoutAlgorithm | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：global；  API声明：export class CustomLayoutAlgorithm  差异内容：export class CustomLayoutAlgorithm | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：CustomLayoutAlgorithm；  API声明：onMeasure(self: FrameNode, constraint: LayoutConstraint): void;  差异内容：onMeasure(self: FrameNode, constraint: LayoutConstraint): void; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：CustomLayoutAlgorithm；  API声明：onLayout(self: FrameNode, position: Position): void;  差异内容：onLayout(self: FrameNode, position: Position): void; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：global；  API声明：interface ColumnLayoutAlgorithmOptions  差异内容：interface ColumnLayoutAlgorithmOptions | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：ColumnLayoutAlgorithmOptions；  API声明：space?: LengthMetrics;  差异内容：space?: LengthMetrics; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：ColumnLayoutAlgorithmOptions；  API声明：alignItems?: HorizontalAlign;  差异内容：alignItems?: HorizontalAlign; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：ColumnLayoutAlgorithmOptions；  API声明：justifyContent?: FlexAlign;  差异内容：justifyContent?: FlexAlign; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：ColumnLayoutAlgorithmOptions；  API声明：isReverse?: boolean;  差异内容：isReverse?: boolean; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：global；  API声明：export class ColumnLayoutAlgorithm  差异内容：export class ColumnLayoutAlgorithm | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：ColumnLayoutAlgorithm；  API声明：@Trace  public space?: LengthMetrics;  差异内容：@Trace  public space?: LengthMetrics; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：ColumnLayoutAlgorithm；  API声明：@Trace  public alignItems?: HorizontalAlign;  差异内容：@Trace  public alignItems?: HorizontalAlign; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：ColumnLayoutAlgorithm；  API声明：@Trace  public justifyContent?: FlexAlign;  差异内容：@Trace  public justifyContent?: FlexAlign; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：ColumnLayoutAlgorithm；  API声明：@Trace  public isReverse?: boolean;  差异内容：@Trace  public isReverse?: boolean; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：global；  API声明：interface RowLayoutAlgorithmOptions  差异内容：interface RowLayoutAlgorithmOptions | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：RowLayoutAlgorithmOptions；  API声明：space?: LengthMetrics;  差异内容：space?: LengthMetrics; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：RowLayoutAlgorithmOptions；  API声明：alignItems?: VerticalAlign;  差异内容：alignItems?: VerticalAlign; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：RowLayoutAlgorithmOptions；  API声明：justifyContent?: FlexAlign;  差异内容：justifyContent?: FlexAlign; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：RowLayoutAlgorithmOptions；  API声明：isReverse?: boolean;  差异内容：isReverse?: boolean; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：global；  API声明：export class RowLayoutAlgorithm  差异内容：export class RowLayoutAlgorithm | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：RowLayoutAlgorithm；  API声明：@Trace  public space?: LengthMetrics;  差异内容：@Trace  public space?: LengthMetrics; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：RowLayoutAlgorithm；  API声明：@Trace  public alignItems?: VerticalAlign;  差异内容：@Trace  public alignItems?: VerticalAlign; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：RowLayoutAlgorithm；  API声明：@Trace  public justifyContent?: FlexAlign;  差异内容：@Trace  public justifyContent?: FlexAlign; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：RowLayoutAlgorithm；  API声明：@Trace  public isReverse?: boolean;  差异内容：@Trace  public isReverse?: boolean; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：global；  API声明：interface StackLayoutAlgorithmOptions  差异内容：interface StackLayoutAlgorithmOptions | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：StackLayoutAlgorithmOptions；  API声明：alignContent?: LocalizedAlignment;  差异内容：alignContent?: LocalizedAlignment; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：global；  API声明：export class StackLayoutAlgorithm  差异内容：export class StackLayoutAlgorithm | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：StackLayoutAlgorithm；  API声明：@Trace  public alignContent?: LocalizedAlignment;  差异内容：@Trace  public alignContent?: LocalizedAlignment; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：global；  API声明：interface GridLayoutAlgorithmOptions  差异内容：interface GridLayoutAlgorithmOptions | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：GridLayoutAlgorithmOptions；  API声明：columnsTemplate?: string | ItemFillPolicy;  差异内容：columnsTemplate?: string | ItemFillPolicy; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：GridLayoutAlgorithmOptions；  API声明：columnsGap?: LengthMetrics;  差异内容：columnsGap?: LengthMetrics; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：GridLayoutAlgorithmOptions；  API声明：rowsGap?: LengthMetrics;  差异内容：rowsGap?: LengthMetrics; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：global；  API声明：export class GridLayoutAlgorithm  差异内容：export class GridLayoutAlgorithm | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：GridLayoutAlgorithm；  API声明：@Trace  public columnsTemplate?: string | ItemFillPolicy;  差异内容：@Trace  public columnsTemplate?: string | ItemFillPolicy; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：GridLayoutAlgorithm；  API声明：@Trace  public columnsGap?: LengthMetrics;  差异内容：@Trace  public columnsGap?: LengthMetrics; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：GridLayoutAlgorithm；  API声明：@Trace  public rowsGap?: LengthMetrics;  差异内容：@Trace  public rowsGap?: LengthMetrics; | api/arkui/LayoutAlgorithm.d.ts |
| 新增API | NA | 类名：EllipsisMode；  API声明：MULTILINE\_START = 3  差异内容：MULTILINE\_START = 3 | component/enums.d.ts |
| 新增API | NA | 类名：EllipsisMode；  API声明：MULTILINE\_CENTER = 4  差异内容：MULTILINE\_CENTER = 4 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum CompetitionStrategy  差异内容：declare enum CompetitionStrategy | component/enums.d.ts |
| 新增API | NA | 类名：CompetitionStrategy；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | component/enums.d.ts |
| 新增API | NA | 类名：CompetitionStrategy；  API声明：COMPETITION = 1  差异内容：COMPETITION = 1 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum HdrType  差异内容：declare enum HdrType | component/xcomponent.d.ts |
| 新增API | NA | 类名：HdrType；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | component/xcomponent.d.ts |
| 新增API | NA | 类名：HdrType；  API声明：AIHDR = 1  差异内容：AIHDR = 1 | component/xcomponent.d.ts |
| 新增API | NA | 类名：ButtonOptions；  API声明：textAlign?: TextAlign;  差异内容：textAlign?: TextAlign; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：AdvancedDialogV2Button；  API声明：@Trace  textAlign?: TextAlign;  差异内容：@Trace  textAlign?: TextAlign; | api/@ohos.arkui.advanced.DialogV2.d.ets |
| 新增API | NA | 类名：AdvancedDialogV2ButtonOptions；  API声明：textAlign?: TextAlign;  差异内容：textAlign?: TextAlign; | api/@ohos.arkui.advanced.DialogV2.d.ets |
| 新增API | NA | 类名：SegmentButton；  API声明：@Prop  enableStateAnimation: boolean;  差异内容：@Prop  enableStateAnimation: boolean; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：TabSegmentButtonV2；  API声明：@Param  readonly enableStateAnimation?: boolean;  差异内容：@Param  readonly enableStateAnimation?: boolean; | api/@ohos.arkui.advanced.SegmentButtonV2.d.ets |
| 新增API | NA | 类名：CapsuleSegmentButtonV2；  API声明：@Param  readonly enableStateAnimation?: boolean;  差异内容：@Param  readonly enableStateAnimation?: boolean; | api/@ohos.arkui.advanced.SegmentButtonV2.d.ets |
| 新增API | NA | 类名：OperationOption；  API声明：id?: string;  差异内容：id?: string; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SelectOptions；  API声明：id?: string;  差异内容：id?: string; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SubHeader；  API声明：@Prop  titleId?: string;  差异内容：@Prop  titleId?: string; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SubHeaderV2TitleOptions；  API声明：id?: string;  差异内容：id?: string; | api/@ohos.arkui.advanced.SubHeaderV2.d.ets |
| 新增API | NA | 类名：SubHeaderV2Title；  API声明：@Trace  id?: string;  差异内容：@Trace  id?: string; | api/@ohos.arkui.advanced.SubHeaderV2.d.ets |
| 新增API | NA | 类名：SubHeaderV2SelectOptions；  API声明：id?: string;  差异内容：id?: string; | api/@ohos.arkui.advanced.SubHeaderV2.d.ets |
| 新增API | NA | 类名：SubHeaderV2Select；  API声明：@Trace  id?: string;  差异内容：@Trace  id?: string; | api/@ohos.arkui.advanced.SubHeaderV2.d.ets |
| 新增API | NA | 类名：SubHeaderV2OperationItemOptions；  API声明：id?: string;  差异内容：id?: string; | api/@ohos.arkui.advanced.SubHeaderV2.d.ets |
| 新增API | NA | 类名：SubHeaderV2OperationItem；  API声明：@Trace  id?: string;  差异内容：@Trace  id?: string; | api/@ohos.arkui.advanced.SubHeaderV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export enum AnimationStopMode  差异内容：export enum AnimationStopMode | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：AnimationStopMode；  API声明：FIRST\_FRAME = 0  差异内容：FIRST\_FRAME = 0 | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：AnimationStopMode；  API声明：LAST\_FRAME = 1  差异内容：LAST\_FRAME = 1 | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：AnimationOptions；  API声明：stopMode?: AnimationStopMode;  差异内容：stopMode?: AnimationStopMode; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：ComponentObserver；  API声明：onDrawChildren(callback: Callback<number[]>): void;  差异内容：onDrawChildren(callback: Callback<number[]>): void; | api/@ohos.arkui.inspector.d.ts |
| 新增API | NA | 类名：ComponentObserver；  API声明：offDrawChildren(callback?: Callback<number[]>): void;  差异内容：offDrawChildren(callback?: Callback<number[]>): void; | api/@ohos.arkui.inspector.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：isEasySplit(): boolean;  差异内容：isEasySplit(): boolean; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getPageRootNode(): FrameNode | null;  差异内容：getPageRootNode(): FrameNode | null; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Window；  API声明：clearWindowMask(): Promise<void>;  差异内容：clearWindowMask(): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStage；  API声明：releaseUIContent(): Promise<void>;  差异内容：releaseUIContent(): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：FloatingBallController；  API声明：setFloatingBallVisibilityInApp(isVisible: boolean): Promise<void>;  差异内容：setFloatingBallVisibilityInApp(isVisible: boolean): Promise<void>; | api/@ohos.window.floatingBall.d.ts |
| 新增API | NA | 类名：BuilderNode；  API声明：postInputEventWithStrategy(event: InputEventType, competitionStrategy?: CompetitionStrategy): boolean;  差异内容：postInputEventWithStrategy(event: InputEventType, competitionStrategy?: CompetitionStrategy): boolean; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：ReactiveBuilderNode；  API声明：postInputEventWithStrategy(event: InputEventType, competitionStrategy?: CompetitionStrategy): boolean;  差异内容：postInputEventWithStrategy(event: InputEventType, competitionStrategy?: CompetitionStrategy): boolean; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：CanvasRenderer；  API声明：antialias: boolean | undefined;  差异内容：antialias: boolean | undefined; | component/canvas.d.ts |
| 新增API | NA | 类名：MouseEvent；  API声明：eventHandleId?: number;  差异内容：eventHandleId?: number; | component/common.d.ts |
| 新增API | NA | 类名：TouchEvent；  API声明：eventHandleId?: number;  差异内容：eventHandleId?: number; | component/common.d.ts |
| 新增API | NA | 类名：AxisEvent；  API声明：eventHandleId?: number;  差异内容：eventHandleId?: number; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type OnNeedSoftkeyboardCallback = () => boolean;  差异内容：declare type OnNeedSoftkeyboardCallback = () => boolean; | component/common.d.ts |
| 新增API | NA | 类名：DragResult；  API声明：UNKNOWN = -1  差异内容：UNKNOWN = -1 | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：enableClickSoundEffect(enabled: boolean | undefined): T;  差异内容：enableClickSoundEffect(enabled: boolean | undefined): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：onNeedSoftkeyboard(onNeedSoftkeyboardCallback: OnNeedSoftkeyboardCallback | undefined): T;  差异内容：onNeedSoftkeyboard(onNeedSoftkeyboardCallback: OnNeedSoftkeyboardCallback | undefined): T; | component/common.d.ts |
| 新增API | NA | 类名：NavigationMode；  API声明：AUTO\_WITH\_ASPECT\_RATIO  差异内容：AUTO\_WITH\_ASPECT\_RATIO | component/navigation.d.ts |
| 新增API | NA | 类名：RichEditorBaseController；  API声明：setStyledPlaceholder(styledString: StyledString): void;  差异内容：setStyledPlaceholder(styledString: StyledString): void; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：readonly fontConfigs?: FontConfigs;  差异内容：readonly fontConfigs?: FontConfigs; | component/styled\_string.d.ts |
| 新增API | NA | 类名：TextStyleInterface；  API声明：fontConfigs?: FontConfigs;  差异内容：fontConfigs?: FontConfigs; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum TabsNestedScrollMode  差异内容：declare enum TabsNestedScrollMode | component/tabs.d.ts |
| 新增API | NA | 类名：TabsNestedScrollMode；  API声明：SELF\_ONLY = 0  差异内容：SELF\_ONLY = 0 | component/tabs.d.ts |
| 新增API | NA | 类名：TabsNestedScrollMode；  API声明：SELF\_FIRST = 1  差异内容：SELF\_FIRST = 1 | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：nestedScroll(value: TabsNestedScrollMode | undefined): TabsAttribute;  差异内容：nestedScroll(value: TabsNestedScrollMode | undefined): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：horizontalScrolling(enabled: Optional<boolean>): TextAreaAttribute;  差异内容：horizontalScrolling(enabled: Optional<boolean>): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：LayoutManager；  API声明：getCharacterPositionAtCoordinate(x: number, y: number): PositionWithAffinity | undefined;  差异内容：getCharacterPositionAtCoordinate(x: number, y: number): PositionWithAffinity | undefined; | component/text\_common.d.ts |
| 新增API | NA | 类名：LayoutManager；  API声明：getGlyphRangeForCharacterRange(charRange: TextRange): Array<TextRange> | undefined;  差异内容：getGlyphRangeForCharacterRange(charRange: TextRange): Array<TextRange> | undefined; | component/text\_common.d.ts |
| 新增API | NA | 类名：LayoutManager；  API声明：getCharacterRangeForGlyphRange(glyphRange: TextRange): Array<TextRange> | undefined;  差异内容：getCharacterRangeForGlyphRange(glyphRange: TextRange): Array<TextRange> | undefined; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface FontConfigs  差异内容：declare interface FontConfigs | component/text\_common.d.ts |
| 新增API | NA | 类名：FontConfigs；  API声明：fontWeightConfigs?: FontWeightConfigs;  差异内容：fontWeightConfigs?: FontWeightConfigs; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface FontWeightConfigs  差异内容：declare interface FontWeightConfigs | component/text\_common.d.ts |
| 新增API | NA | 类名：FontWeightConfigs；  API声明：enableVariableFontWeight?: boolean;  差异内容：enableVariableFontWeight?: boolean; | component/text\_common.d.ts |
| 新增API | NA | 类名：FontWeightConfigs；  API声明：enableDeviceFontWeightCategory?: boolean;  差异内容：enableDeviceFontWeightCategory?: boolean; | component/text\_common.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.arkui.components.ArkDynamicLayout.d.ts  差异内容：ArkUI | api/@ohos.arkui.components.ArkDynamicLayout.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.arkui.layoutAlgorithm.d.ts  差异内容：ArkUI | api/@ohos.arkui.layoutAlgorithm.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\arkui\LayoutAlgorithm.d.ts  差异内容：ArkUI | api/arkui/LayoutAlgorithm.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：SpanAttribute；  API声明：font(value: Font): SpanAttribute;  差异内容：font(value: Font): SpanAttribute; | 类名：SpanAttribute；  API声明：font(value: Font, fontConfigs?: FontConfigs): SpanAttribute;  差异内容：font(value: Font, fontConfigs?: FontConfigs): SpanAttribute; | component/span.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：SpanAttribute；  API声明：fontWeight(value: number | FontWeight | ResourceStr): SpanAttribute;  差异内容：fontWeight(value: number | FontWeight | ResourceStr): SpanAttribute; | 类名：SpanAttribute；  API声明：fontWeight(weight: number | FontWeight | ResourceStr, fontWeightConfigs?: FontWeightConfigs): SpanAttribute;  差异内容：fontWeight(weight: number | FontWeight | ResourceStr, fontWeightConfigs?: FontWeightConfigs): SpanAttribute; | component/span.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：XComponentAttribute；  API声明：hdrBrightness(brightness: number): XComponentAttribute;  差异内容：hdrBrightness(brightness: number): XComponentAttribute; | 类名：XComponentAttribute；  API声明：hdrBrightness(brightness: number, type?: HdrType): XComponentAttribute;  差异内容：hdrBrightness(brightness: number, type?: HdrType): XComponentAttribute; | component/xcomponent.d.ts |
