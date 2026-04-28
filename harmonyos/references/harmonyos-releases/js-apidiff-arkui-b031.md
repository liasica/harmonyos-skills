---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-b031
title: ArkUI
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > ArkUI
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:36+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:2721edc8f5c8fdfd30a3956c767c855558240e93bb45e16bc07a4c7b5774d3c6
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API卡片权限变更 | 类名：CommonMethod；  API声明：accessibilityGroup(value: boolean): T;  差异内容：NA | 类名：CommonMethod；  API声明：accessibilityGroup(value: boolean): T;  差异内容：form | component/common.d.ts |
| API卡片权限变更 | 类名：CommonMethod；  API声明：accessibilityText(value: string): T;  差异内容：NA | 类名：CommonMethod；  API声明：accessibilityText(value: string): T;  差异内容：form | component/common.d.ts |
| API卡片权限变更 | 类名：CommonMethod；  API声明：accessibilityTextHint(value: string): T;  差异内容：NA | 类名：CommonMethod；  API声明：accessibilityTextHint(value: string): T;  差异内容：form | component/common.d.ts |
| API卡片权限变更 | 类名：CommonMethod；  API声明：accessibilityDescription(value: string): T;  差异内容：NA | 类名：CommonMethod；  API声明：accessibilityDescription(value: string): T;  差异内容：form | component/common.d.ts |
| API卡片权限变更 | 类名：CommonMethod；  API声明：accessibilityLevel(value: string): T;  差异内容：NA | 类名：CommonMethod；  API声明：accessibilityLevel(value: string): T;  差异内容：form | component/common.d.ts |
| API卡片权限变更 | 类名：CommonMethod；  API声明：accessibilityVirtualNode(builder: CustomBuilder): T;  差异内容：NA | 类名：CommonMethod；  API声明：accessibilityVirtualNode(builder: CustomBuilder): T;  差异内容：form | component/common.d.ts |
| API废弃版本变更 | 类名：global；  API声明： export declare class XComponentNode  差异内容：NA | 类名：global；  API声明： export declare class XComponentNode  差异内容：12 | api/arkui/XComponentNode.d.ts |
| API废弃版本变更 | 类名：XComponentNode；  API声明：onCreate(event?: Object): void;  差异内容：NA | 类名：XComponentNode；  API声明：onCreate(event?: Object): void;  差异内容：12 | api/arkui/XComponentNode.d.ts |
| API废弃版本变更 | 类名：XComponentNode；  API声明：onDestroy(): void;  差异内容：NA | 类名：XComponentNode；  API声明：onDestroy(): void;  差异内容：12 | api/arkui/XComponentNode.d.ts |
| API废弃版本变更 | 类名：XComponentNode；  API声明：changeRenderType(type: NodeRenderType): boolean;  差异内容：NA | 类名：XComponentNode；  API声明：changeRenderType(type: NodeRenderType): boolean;  差异内容：12 | api/arkui/XComponentNode.d.ts |
| API废弃版本变更 | 类名：XComponentType；  API声明：COMPONENT  差异内容：NA | 类名：XComponentType；  API声明：COMPONENT  差异内容：12 | component/enums.d.ts |
| 函数变更 | 类名：dragController；  API声明：function executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: DragInfo): Promise<{  event: DragEvent;  extraParams: string;  }>;  差异内容：Promise<{event:DragEvent;extraParams:string;}> | 类名：dragController；  API声明：function executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: DragInfo): Promise<DragEventParam>;  差异内容：Promise<DragEventParam> | api/@ohos.arkui.dragController.d.ts |
| 函数变更 | 类名：DragController；  API声明：executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: dragController.DragInfo): Promise<{  event: DragEvent;  extraParams: string;  }>;  差异内容：Promise<{event:DragEvent;extraParams:string;}> | 类名：DragController；  API声明：executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: dragController.DragInfo): Promise<dragController.DragEventParam>;  差异内容：Promise<dragController.DragEventParam> | api/@ohos.arkui.UIContext.d.ts |
| 函数变更 | 类名：SwiperAttribute；  API声明：prevMargin(value: Length): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：prevMargin(value: Length, ignoreBlank?: boolean): SwiperAttribute;  差异内容：ignoreBlank?: boolean | component/swiper.d.ts |
| 函数变更 | 类名：SwiperAttribute；  API声明：nextMargin(value: Length): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：nextMargin(value: Length, ignoreBlank?: boolean): SwiperAttribute;  差异内容：ignoreBlank?: boolean | component/swiper.d.ts |
| 函数变更 | 类名：dragController；  API声明：function executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: DragInfo, callback: AsyncCallback<{  event: DragEvent;  extraParams: string;  }>): void;  差异内容：callback: AsyncCallback<{  event: DragEvent;  extraParams: string;  }> | 类名：dragController；  API声明：function executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: DragInfo, callback: AsyncCallback<DragEventParam>): void;  差异内容：callback: AsyncCallback<DragEventParam> | api/@ohos.arkui.dragController.d.ts |
| 函数变更 | 类名：DragController；  API声明：executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: dragController.DragInfo, callback: AsyncCallback<{  event: DragEvent;  extraParams: string;  }>): void;  差异内容：callback: AsyncCallback<{  event: DragEvent;  extraParams: string;  }> | 类名：DragController；  API声明：executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: dragController.DragInfo, callback: AsyncCallback<dragController.DragEventParam>): void;  差异内容：callback: AsyncCallback<dragController.DragEventParam> | api/@ohos.arkui.UIContext.d.ts |
| 函数变更 | 类名：SearchAttribute；  API声明：onChange(callback: (value: string) => void): SearchAttribute;  差异内容：callback: (value: string) => void | 类名：SearchAttribute；  API声明：onChange(callback: EditableTextOnChangeCallback): SearchAttribute;  差异内容：callback: EditableTextOnChangeCallback | component/search.d.ts |
| 函数变更 | 类名：TextAreaAttribute；  API声明：onChange(callback: (value: string) => void): TextAreaAttribute;  差异内容：callback: (value: string) => void | 类名：TextAreaAttribute；  API声明：onChange(callback: EditableTextOnChangeCallback): TextAreaAttribute;  差异内容：callback: EditableTextOnChangeCallback | component/text\_area.d.ts |
| 函数变更 | 类名：TextInputAttribute；  API声明：onChange(callback: (value: string) => void): TextInputAttribute;  差异内容：callback: (value: string) => void | 类名：TextInputAttribute；  API声明：onChange(callback: EditableTextOnChangeCallback): TextInputAttribute;  差异内容：callback: EditableTextOnChangeCallback | component/text\_input.d.ts |
| 函数变更 | 类名：TextInputAttribute；  API声明：showError(value?: string | undefined): TextInputAttribute;  差异内容：value?: string | undefined | 类名：TextInputAttribute；  API声明：showError(value?: ResourceStr | undefined): TextInputAttribute;  差异内容：value?: ResourceStr | undefined | component/text\_input.d.ts |
| 函数变更 | 类名：MenuItemAttribute；  API声明：selectIcon(value: boolean | ResourceStr): MenuItemAttribute;  差异内容：value: boolean | ResourceStr | 类名：MenuItemAttribute；  API声明：selectIcon(value: boolean | ResourceStr | SymbolGlyphModifier): MenuItemAttribute;  差异内容：value: boolean | ResourceStr | SymbolGlyphModifier | component/menu\_item.d.ts |
| 函数变更 | 类名：NavigationAttribute；  API声明：backButtonIcon(value: string | PixelMap | Resource): NavigationAttribute;  差异内容：value: string | PixelMap | Resource | 类名：NavigationAttribute；  API声明：backButtonIcon(value: string | PixelMap | Resource | SymbolGlyphModifier): NavigationAttribute;  差异内容：value: string | PixelMap | Resource | SymbolGlyphModifier | component/navigation.d.ts |
| 函数变更 | 类名：NavDestinationAttribute；  API声明：backButtonIcon(value: ResourceStr | PixelMap): NavDestinationAttribute;  差异内容：value: ResourceStr | PixelMap | 类名：NavDestinationAttribute；  API声明：backButtonIcon(value: ResourceStr | PixelMap | SymbolGlyphModifier): NavDestinationAttribute;  差异内容：value: ResourceStr | PixelMap | SymbolGlyphModifier | component/nav\_destination.d.ts |
| 函数变更 | 类名：SecurityComponentMethod；  API声明：offset(value: Position): T;  差异内容：value: Position | 类名：SecurityComponentMethod；  API声明：offset(value: Position | Edges | LocalizedEdges): T;  差异内容：value: Position | Edges | LocalizedEdges | component/security\_component.d.ts |
| 函数变更 | 类名：BottomTabBarStyle；  API声明：padding(value: Padding | Dimension): BottomTabBarStyle;  差异内容：value: Padding | Dimension | 类名：BottomTabBarStyle；  API声明：padding(value: Padding | Dimension | LocalizedPadding): BottomTabBarStyle;  差异内容：value: Padding | Dimension | LocalizedPadding | component/tab\_content.d.ts |
| 属性变更 | 类名：IconGroupSuffix；  API声明：@Prop  items: Array<IconItemOptions>;  差异内容：Array<IconItemOptions> | 类名：IconGroupSuffix；  API声明：@Require  @Prop  items: Array<IconItemOptions | SymbolGlyphModifier>;  差异内容：Array<IconItemOptions | SymbolGlyphModifier> | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 属性变更 | 类名：global；  API声明：declare const ComponentV2: ClassDecorator;  差异内容：ClassDecorator | 类名：global；  API声明：declare const ComponentV2: ClassDecorator & ((options: ComponentOptions) => ClassDecorator);  差异内容：ClassDecorator & ((options: ComponentOptions) => ClassDecorator) | component/common.d.ts |
| 属性变更 | 类名：TipsDialog；  API声明：imageRes: Resource;  差异内容：Resource | 类名：TipsDialog；  API声明：imageRes: ResourceStr | PixelMap;  差异内容：ResourceStr,PixelMap | api/@ohos.arkui.advanced.Dialog.d.ets |
| 属性变更 | 类名：ActionSheetOptions；  API声明：cornerRadius?: Dimension | BorderRadiuses;  差异内容：Dimension,BorderRadiuses | 类名：ActionSheetOptions；  API声明：cornerRadius?: Dimension | BorderRadiuses | LocalizedBorderRadiuses;  差异内容：Dimension,BorderRadiuses,LocalizedBorderRadiuses | component/action\_sheet.d.ts |
| 属性变更 | 类名：ActionSheetOptions；  API声明：borderWidth?: Dimension | EdgeWidths;  差异内容：Dimension,EdgeWidths | 类名：ActionSheetOptions；  API声明：borderWidth?: Dimension | EdgeWidths | LocalizedEdgeWidths;  差异内容：Dimension,EdgeWidths,LocalizedEdgeWidths | component/action\_sheet.d.ts |
| 属性变更 | 类名：ActionSheetOptions；  API声明：borderColor?: ResourceColor | EdgeColors;  差异内容：ResourceColor,EdgeColors | 类名：ActionSheetOptions；  API声明：borderColor?: ResourceColor | EdgeColors | LocalizedEdgeColors;  差异内容：ResourceColor,EdgeColors,LocalizedEdgeColors | component/action\_sheet.d.ts |
| 属性变更 | 类名：AlertDialogParam；  API声明：cornerRadius?: Dimension | BorderRadiuses;  差异内容：Dimension,BorderRadiuses | 类名：AlertDialogParam；  API声明：cornerRadius?: Dimension | BorderRadiuses | LocalizedBorderRadiuses;  差异内容：Dimension,BorderRadiuses,LocalizedBorderRadiuses | component/alert\_dialog.d.ts |
| 属性变更 | 类名：AlertDialogParam；  API声明：borderWidth?: Dimension | EdgeWidths;  差异内容：Dimension,EdgeWidths | 类名：AlertDialogParam；  API声明：borderWidth?: Dimension | EdgeWidths | LocalizedEdgeWidths;  差异内容：Dimension,EdgeWidths,LocalizedEdgeWidths | component/alert\_dialog.d.ts |
| 属性变更 | 类名：AlertDialogParam；  API声明：borderColor?: ResourceColor | EdgeColors;  差异内容：ResourceColor,EdgeColors | 类名：AlertDialogParam；  API声明：borderColor?: ResourceColor | EdgeColors | LocalizedEdgeColors;  差异内容：ResourceColor,EdgeColors,LocalizedEdgeColors | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare enum ExtraRegionPosition  差异内容： export declare enum ExtraRegionPosition | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：ExtraRegionPosition；  API声明：TOP = 1  差异内容：TOP = 1 | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：ExtraRegionPosition；  API声明：BOTTOM = 2  差异内容：BOTTOM = 2 | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface ExpandedRegionLayoutOptions  差异内容： export interface ExpandedRegionLayoutOptions | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：ExpandedRegionLayoutOptions；  API声明：horizontalSplitRatio?: number;  差异内容：horizontalSplitRatio?: number; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：ExpandedRegionLayoutOptions；  API声明：verticalSplitRatio?: number;  差异内容：verticalSplitRatio?: number; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：ExpandedRegionLayoutOptions；  API声明：isExtraRegionPerpendicular?: boolean;  差异内容：isExtraRegionPerpendicular?: boolean; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：ExpandedRegionLayoutOptions；  API声明：extraRegionPosition?: ExtraRegionPosition;  差异内容：extraRegionPosition?: ExtraRegionPosition; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface HoverModeRegionLayoutOptions  差异内容： export interface HoverModeRegionLayoutOptions | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：HoverModeRegionLayoutOptions；  API声明：horizontalSplitRatio?: number;  差异内容：horizontalSplitRatio?: number; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：HoverModeRegionLayoutOptions；  API声明：showExtraRegion?: boolean;  差异内容：showExtraRegion?: boolean; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：HoverModeRegionLayoutOptions；  API声明：extraRegionPosition?: ExtraRegionPosition;  差异内容：extraRegionPosition?: ExtraRegionPosition; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface FoldedRegionLayoutOptions  差异内容： export interface FoldedRegionLayoutOptions | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：FoldedRegionLayoutOptions；  API声明：verticalSplitRatio?: number;  差异内容：verticalSplitRatio?: number; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum PresetSplitRatio  差异内容： export declare enum PresetSplitRatio | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：PresetSplitRatio；  API声明：LAYOUT\_1V1 = 1  差异内容：LAYOUT\_1V1 = 1 | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：PresetSplitRatio；  API声明：LAYOUT\_2V3 = 0.6666666666666666  差异内容：LAYOUT\_2V3 = 0.6666666666666666 | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：PresetSplitRatio；  API声明：LAYOUT\_3V2 = 1.5  差异内容：LAYOUT\_3V2 = 1.5 | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface HoverModeStatus  差异内容： export interface HoverModeStatus | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：HoverModeStatus；  API声明：foldStatus: display.FoldStatus;  差异内容：foldStatus: display.FoldStatus; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：HoverModeStatus；  API声明：isHoverMode: boolean;  差异内容：isHoverMode: boolean; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：HoverModeStatus；  API声明：appRotation: number;  差异内容：appRotation: number; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：HoverModeStatus；  API声明：windowStatusType: window.WindowStatusType;  差异内容：windowStatusType: window.WindowStatusType; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：global；  API声明：export type OnHoverStatusChangeHandler = (status: HoverModeStatus) => void;  差异内容：export type OnHoverStatusChangeHandler = (status: HoverModeStatus) => void; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct FoldSplitContainer  差异内容： export declare struct FoldSplitContainer | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：FoldSplitContainer；  API声明：@BuilderParam  primary: Callback<void>;  差异内容：@BuilderParam  primary: Callback<void>; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：FoldSplitContainer；  API声明：@BuilderParam  secondary: Callback<void>;  差异内容：@BuilderParam  secondary: Callback<void>; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：FoldSplitContainer；  API声明：@BuilderParam  extra?: Callback<void>;  差异内容：@BuilderParam  extra?: Callback<void>; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：FoldSplitContainer；  API声明：@Prop  expandedLayoutOptions: ExpandedRegionLayoutOptions;  差异内容：@Prop  expandedLayoutOptions: ExpandedRegionLayoutOptions; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：FoldSplitContainer；  API声明：@Prop  hoverModeLayoutOptions: HoverModeRegionLayoutOptions;  差异内容：@Prop  hoverModeLayoutOptions: HoverModeRegionLayoutOptions; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：FoldSplitContainer；  API声明：@Prop  foldedLayoutOptions: FoldedRegionLayoutOptions;  差异内容：@Prop  foldedLayoutOptions: FoldedRegionLayoutOptions; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：FoldSplitContainer；  API声明：@Prop  animationOptions?: AnimateParam | null;  差异内容：@Prop  animationOptions?: AnimateParam | null; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：FoldSplitContainer；  API声明：onHoverStatusChange?: OnHoverStatusChangeHandler;  差异内容：onHoverStatusChange?: OnHoverStatusChangeHandler; | api/@ohos.arkui.advanced.FoldSplitContainer.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare type StorageDefaultCreator<T> = () => T;  差异内容：export declare type StorageDefaultCreator<T> = () => T; | api/@ohos.arkui.StateManagement.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface TypeConstructorWithArgs  差异内容： export interface TypeConstructorWithArgs | api/@ohos.arkui.StateManagement.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class AppStorageV2  差异内容： export declare class AppStorageV2 | api/@ohos.arkui.StateManagement.d.ts |
| 新增API | NA | 类名：AppStorageV2；  API声明：static connect<T extends object>(type: TypeConstructorWithArgs<T>, keyOrDefaultCreator?: string | StorageDefaultCreator<T>, defaultCreator?: StorageDefaultCreator<T>): T | undefined;  差异内容：static connect<T extends object>(type: TypeConstructorWithArgs<T>, keyOrDefaultCreator?: string | StorageDefaultCreator<T>, defaultCreator?: StorageDefaultCreator<T>): T | undefined; | api/@ohos.arkui.StateManagement.d.ts |
| 新增API | NA | 类名：AppStorageV2；  API声明：static remove<T>(keyOrType: string | TypeConstructorWithArgs<T>): void;  差异内容：static remove<T>(keyOrType: string | TypeConstructorWithArgs<T>): void; | api/@ohos.arkui.StateManagement.d.ts |
| 新增API | NA | 类名：AppStorageV2；  API声明：static keys(): Array<string>;  差异内容：static keys(): Array<string>; | api/@ohos.arkui.StateManagement.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare type PersistenceErrorCallback = (key: string, reason: 'quota' | 'serialization' | 'unknown', message: string) => void;  差异内容：export declare type PersistenceErrorCallback = (key: string, reason: 'quota' | 'serialization' | 'unknown', message: string) => void; | api/@ohos.arkui.StateManagement.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class PersistenceV2  差异内容： export declare class PersistenceV2 | api/@ohos.arkui.StateManagement.d.ts |
| 新增API | NA | 类名：PersistenceV2；  API声明：static save<T>(keyOrType: string | TypeConstructorWithArgs<T>): void;  差异内容：static save<T>(keyOrType: string | TypeConstructorWithArgs<T>): void; | api/@ohos.arkui.StateManagement.d.ts |
| 新增API | NA | 类名：PersistenceV2；  API声明：static notifyOnError(callback: PersistenceErrorCallback | undefined): void;  差异内容：static notifyOnError(callback: PersistenceErrorCallback | undefined): void; | api/@ohos.arkui.StateManagement.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface TypeConstructor  差异内容： export interface TypeConstructor | api/@ohos.arkui.StateManagement.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare type TypeDecorator = <T>(type: TypeConstructor<T>) => PropertyDecorator;  差异内容：export declare type TypeDecorator = <T>(type: TypeConstructor<T>) => PropertyDecorator; | api/@ohos.arkui.StateManagement.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare const Type: TypeDecorator;  差异内容：export declare const Type: TypeDecorator; | api/@ohos.arkui.StateManagement.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class ContainerSpanModifier  差异内容： export declare class ContainerSpanModifier | api/arkui/ContainerSpanModifier.d.ts |
| 新增API | NA | 类名：ContainerSpanModifier；  API声明：applyNormalAttribute?(containerSpanAttribute: ContainerSpanAttribute): void;  差异内容：applyNormalAttribute?(containerSpanAttribute: ContainerSpanAttribute): void; | api/arkui/ContainerSpanModifier.d.ts |
| 新增API | NA | 类名：ChipGroupItemOptions；  API声明：prefixSymbol?: ChipSymbolGlyphOptions;  差异内容：prefixSymbol?: ChipSymbolGlyphOptions; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroupItemOptions；  API声明：suffixSymbol?: ChipSymbolGlyphOptions;  差异内容：suffixSymbol?: ChipSymbolGlyphOptions; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface ChipGroupPaddingOptions  差异内容： export interface ChipGroupPaddingOptions | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroupPaddingOptions；  API声明：top: Length;  差异内容：top: Length; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroupPaddingOptions；  API声明：bottom: Length;  差异内容：bottom: Length; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroup；  API声明：@Prop  chipGroupPadding?: ChipGroupPaddingOptions;  差异内容：@Prop  chipGroupPadding?: ChipGroupPaddingOptions; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：TipsDialog；  API声明：onCheckedChange?: Callback<boolean>;  差异内容：onCheckedChange?: Callback<boolean>; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：ConfirmDialog；  API声明：onCheckedChange?: Callback<boolean>;  差异内容：onCheckedChange?: Callback<boolean>; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：SubHeader；  API声明：primaryTitleModifier?: TextModifier;  差异内容：primaryTitleModifier?: TextModifier; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SubHeader；  API声明：secondaryTitleModifier?: TextModifier;  差异内容：secondaryTitleModifier?: TextModifier; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SubHeader；  API声明：@BuilderParam  titleBuilder?: () => void;  差异内容：@BuilderParam  titleBuilder?: () => void; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SubHeader；  API声明：@Prop  contentMargin?: LocalizedMargin;  差异内容：@Prop  contentMargin?: LocalizedMargin; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SubHeader；  API声明：@Prop  contentPadding?: LocalizedPadding;  差异内容：@Prop  contentPadding?: LocalizedPadding; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：dragController；  API声明： interface DragEventParam  差异内容： interface DragEventParam | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragEventParam；  API声明：event: DragEvent;  差异内容：event: DragEvent; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragEventParam；  API声明：extraParams: string;  差异内容：extraParams: string; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface PageInfo  差异内容： export interface PageInfo | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：PageInfo；  API声明：routerPageInfo?: observer.RouterPageInfo;  差异内容：routerPageInfo?: observer.RouterPageInfo; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：PageInfo；  API声明：navDestinationInfo?: observer.NavDestinationInfo;  差异内容：navDestinationInfo?: observer.NavDestinationInfo; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export class DynamicSyncScene  差异内容： export class DynamicSyncScene | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：DynamicSyncScene；  API声明：setFrameRateRange(range: ExpectedFrameRateRange): void;  差异内容：setFrameRateRange(range: ExpectedFrameRateRange): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：DynamicSyncScene；  API声明：getFrameRateRange(): ExpectedFrameRateRange;  差异内容：getFrameRateRange(): ExpectedFrameRateRange; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export class SwiperDynamicSyncScene  差异内容： export class SwiperDynamicSyncScene | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：SwiperDynamicSyncScene；  API声明：readonly type: SwiperDynamicSyncSceneType;  差异内容：readonly type: SwiperDynamicSyncSceneType; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export abstract class FrameCallback  差异内容： export abstract class FrameCallback | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：FrameCallback；  API声明：abstract onFrame(frameTimeInNano: number): void;  差异内容：abstract onFrame(frameTimeInNano: number): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getPageInfoByUniqueId(id: number): PageInfo;  差异内容：getPageInfoByUniqueId(id: number): PageInfo; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getNavigationInfoByUniqueId(id: number): observer.NavigationInfo | undefined;  差异内容：getNavigationInfoByUniqueId(id: number): observer.NavigationInfo | undefined; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：postFrameCallback(frameCallback: FrameCallback): void;  差异内容：postFrameCallback(frameCallback: FrameCallback): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：postDelayedFrameCallback(frameCallback: FrameCallback, delayTime: number): void;  差异内容：postDelayedFrameCallback(frameCallback: FrameCallback, delayTime: number): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：requireDynamicSyncScene(id: string): Array<DynamicSyncScene>;  差异内容：requireDynamicSyncScene(id: string): Array<DynamicSyncScene>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export const enum SwiperDynamicSyncSceneType  差异内容： export const enum SwiperDynamicSyncSceneType | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：SwiperDynamicSyncSceneType；  API声明：GESTURE = 0  差异内容：GESTURE = 0 | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：SwiperDynamicSyncSceneType；  API声明：ANIMATION = 1  差异内容：ANIMATION = 1 | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'TextInput'): TextInput;  差异内容：function createNode(context: UIContext, nodeType: 'TextInput'): TextInput; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'Button'): Button;  差异内容：function createNode(context: UIContext, nodeType: 'Button'): Button; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type TextInput = TypedFrameNode<TextInputInterface, TextInputAttribute>;  差异内容：type TextInput = TypedFrameNode<TextInputInterface, TextInputAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type Button = TypedFrameNode<ButtonInterface, ButtonAttribute>;  差异内容：type Button = TypedFrameNode<ButtonInterface, ButtonAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TextStyle  差异内容： declare interface TextStyle | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：wordBreak?: WordBreak;  差异内容：wordBreak?: WordBreak; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogParam；  API声明：textStyle?: TextStyle;  差异内容：textStyle?: TextStyle; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：alignRules(alignRule: LocalizedAlignRuleOptions): T;  差异内容：alignRules(alignRule: LocalizedAlignRuleOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface LocalizedHorizontalAlignParam  差异内容： declare interface LocalizedHorizontalAlignParam | component/common.d.ts |
| 新增API | NA | 类名：LocalizedHorizontalAlignParam；  API声明：anchor: string;  差异内容：anchor: string; | component/common.d.ts |
| 新增API | NA | 类名：LocalizedHorizontalAlignParam；  API声明：align: HorizontalAlign;  差异内容：align: HorizontalAlign; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface LocalizedVerticalAlignParam  差异内容： declare interface LocalizedVerticalAlignParam | component/common.d.ts |
| 新增API | NA | 类名：LocalizedVerticalAlignParam；  API声明：anchor: string;  差异内容：anchor: string; | component/common.d.ts |
| 新增API | NA | 类名：LocalizedVerticalAlignParam；  API声明：align: VerticalAlign;  差异内容：align: VerticalAlign; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface LocalizedAlignRuleOptions  差异内容： declare interface LocalizedAlignRuleOptions | component/common.d.ts |
| 新增API | NA | 类名：LocalizedAlignRuleOptions；  API声明：start?: LocalizedHorizontalAlignParam;  差异内容：start?: LocalizedHorizontalAlignParam; | component/common.d.ts |
| 新增API | NA | 类名：LocalizedAlignRuleOptions；  API声明：end?: LocalizedHorizontalAlignParam;  差异内容：end?: LocalizedHorizontalAlignParam; | component/common.d.ts |
| 新增API | NA | 类名：LocalizedAlignRuleOptions；  API声明：middle?: LocalizedHorizontalAlignParam;  差异内容：middle?: LocalizedHorizontalAlignParam; | component/common.d.ts |
| 新增API | NA | 类名：LocalizedAlignRuleOptions；  API声明：top?: LocalizedVerticalAlignParam;  差异内容：top?: LocalizedVerticalAlignParam; | component/common.d.ts |
| 新增API | NA | 类名：LocalizedAlignRuleOptions；  API声明：bottom?: LocalizedVerticalAlignParam;  差异内容：bottom?: LocalizedVerticalAlignParam; | component/common.d.ts |
| 新增API | NA | 类名：LocalizedAlignRuleOptions；  API声明：center?: LocalizedVerticalAlignParam;  差异内容：center?: LocalizedVerticalAlignParam; | component/common.d.ts |
| 新增API | NA | 类名：LocalizedAlignRuleOptions；  API声明：bias?: Bias;  差异内容：bias?: Bias; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum BlurStyleActivePolicy  差异内容： declare enum BlurStyleActivePolicy | component/common.d.ts |
| 新增API | NA | 类名：BlurStyleActivePolicy；  API声明：FOLLOWS\_WINDOW\_ACTIVE\_STATE = 0  差异内容：FOLLOWS\_WINDOW\_ACTIVE\_STATE = 0 | component/common.d.ts |
| 新增API | NA | 类名：BlurStyleActivePolicy；  API声明：ALWAYS\_ACTIVE = 1  差异内容：ALWAYS\_ACTIVE = 1 | component/common.d.ts |
| 新增API | NA | 类名：BlurStyleActivePolicy；  API声明：ALWAYS\_INACTIVE = 2  差异内容：ALWAYS\_INACTIVE = 2 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum BlurType  差异内容： declare enum BlurType | component/common.d.ts |
| 新增API | NA | 类名：BlurType；  API声明：WITHIN\_WINDOW = 0  差异内容：WITHIN\_WINDOW = 0 | component/common.d.ts |
| 新增API | NA | 类名：BlurType；  API声明：BEHIND\_WINDOW = 1  差异内容：BEHIND\_WINDOW = 1 | component/common.d.ts |
| 新增API | NA | 类名：BackgroundBlurStyleOptions；  API声明：policy?: BlurStyleActivePolicy;  差异内容：policy?: BlurStyleActivePolicy; | component/common.d.ts |
| 新增API | NA | 类名：BackgroundBlurStyleOptions；  API声明：inactiveColor?: ResourceColor;  差异内容：inactiveColor?: ResourceColor; | component/common.d.ts |
| 新增API | NA | 类名：BackgroundBlurStyleOptions；  API声明：type?: BlurType;  差异内容：type?: BlurType; | component/common.d.ts |
| 新增API | NA | 类名：BackgroundEffectOptions；  API声明：policy?: BlurStyleActivePolicy;  差异内容：policy?: BlurStyleActivePolicy; | component/common.d.ts |
| 新增API | NA | 类名：BackgroundEffectOptions；  API声明：inactiveColor?: ResourceColor;  差异内容：inactiveColor?: ResourceColor; | component/common.d.ts |
| 新增API | NA | 类名：BackgroundEffectOptions；  API声明：type?: BlurType;  差异内容：type?: BlurType; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum LayoutSafeAreaType  差异内容： declare enum LayoutSafeAreaType | component/common.d.ts |
| 新增API | NA | 类名：LayoutSafeAreaType；  API声明：SYSTEM = 0  差异内容：SYSTEM = 0 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum LayoutSafeAreaEdge  差异内容： declare enum LayoutSafeAreaEdge | component/common.d.ts |
| 新增API | NA | 类名：LayoutSafeAreaEdge；  API声明：TOP = 0  差异内容：TOP = 0 | component/common.d.ts |
| 新增API | NA | 类名：LayoutSafeAreaEdge；  API声明：BOTTOM = 1  差异内容：BOTTOM = 1 | component/common.d.ts |
| 新增API | NA | 类名：ContextMenuAnimationOptions；  API声明：hoverScale?: AnimationRange<number>;  差异内容：hoverScale?: AnimationRange<number>; | component/common.d.ts |
| 新增API | NA | 类名：MenuElement；  API声明：symbolIcon?: SymbolGlyphModifier;  差异内容：symbolIcon?: SymbolGlyphModifier; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：focusScopeId(id: string, isGroup?: boolean): T;  差异内容：focusScopeId(id: string, isGroup?: boolean): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：focusScopePriority(scopeId: string, priority?: FocusPriority): T;  差异内容：focusScopePriority(scopeId: string, priority?: FocusPriority): T; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type OnMoveHandler = (from: number, to: number) => void;  差异内容：declare type OnMoveHandler = (from: number, to: number) => void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class DynamicNode  差异内容： declare class DynamicNode | component/common.d.ts |
| 新增API | NA | 类名：DynamicNode；  API声明：onMove(handler: Optional<OnMoveHandler>): T;  差异内容：onMove(handler: Optional<OnMoveHandler>): T; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum TextSelectableMode  差异内容： declare enum TextSelectableMode | component/enums.d.ts |
| 新增API | NA | 类名：TextSelectableMode；  API声明：SELECTABLE\_UNFOCUSABLE = 0  差异内容：SELECTABLE\_UNFOCUSABLE = 0 | component/enums.d.ts |
| 新增API | NA | 类名：TextSelectableMode；  API声明：SELECTABLE\_FOCUSABLE = 1  差异内容：SELECTABLE\_FOCUSABLE = 1 | component/enums.d.ts |
| 新增API | NA | 类名：TextSelectableMode；  API声明：UNSELECTABLE = 2  差异内容：UNSELECTABLE = 2 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type WindowStatusType = import('../api/@ohos.window').default.WindowStatusType;  差异内容：declare type WindowStatusType = import('../api/@ohos.window').default.WindowStatusType; | component/folder\_stack.d.ts |
| 新增API | NA | 类名：HoverEventParam；  API声明：windowStatusType: WindowStatusType;  差异内容：windowStatusType: WindowStatusType; | component/folder\_stack.d.ts |
| 新增API | NA | 类名：MenuItemOptions；  API声明：symbolStartIcon?: SymbolGlyphModifier;  差异内容：symbolStartIcon?: SymbolGlyphModifier; | component/menu\_item.d.ts |
| 新增API | NA | 类名：MenuItemOptions；  API声明：symbolEndIcon?: SymbolGlyphModifier;  差异内容：symbolEndIcon?: SymbolGlyphModifier; | component/menu\_item.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：pushPath(info: NavPathInfo, options?: NavigationOptions): void;  差异内容：pushPath(info: NavPathInfo, options?: NavigationOptions): void; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：pushDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>;  差异内容：pushDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：replacePath(info: NavPathInfo, options?: NavigationOptions): void;  差异内容：replacePath(info: NavPathInfo, options?: NavigationOptions): void; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type SystemBarStyle = import('../api/@ohos.window').default.SystemBarStyle;  差异内容：declare type SystemBarStyle = import('../api/@ohos.window').default.SystemBarStyle; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationMenuItem；  API声明：symbolIcon?: SymbolGlyphModifier;  差异内容：symbolIcon?: SymbolGlyphModifier; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum LaunchMode  差异内容： declare enum LaunchMode | component/navigation.d.ts |
| 新增API | NA | 类名：LaunchMode；  API声明：STANDARD = 0  差异内容：STANDARD = 0 | component/navigation.d.ts |
| 新增API | NA | 类名：LaunchMode；  API声明：MOVE\_TO\_TOP\_SINGLETON = 1  差异内容：MOVE\_TO\_TOP\_SINGLETON = 1 | component/navigation.d.ts |
| 新增API | NA | 类名：LaunchMode；  API声明：POP\_TO\_SINGLETON = 2  差异内容：POP\_TO\_SINGLETON = 2 | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface NavigationOptions  差异内容： declare interface NavigationOptions | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationOptions；  API声明：launchMode?: LaunchMode;  差异内容：launchMode?: LaunchMode; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationOptions；  API声明：animated?: boolean;  差异内容：animated?: boolean; | component/navigation.d.ts |
| 新增API | NA | 类名：ToolbarItem；  API声明：symbolIcon?: SymbolGlyphModifier;  差异内容：symbolIcon?: SymbolGlyphModifier; | component/navigation.d.ts |
| 新增API | NA | 类名：ToolbarItem；  API声明：activeSymbolIcon?: SymbolGlyphModifier;  差异内容：activeSymbolIcon?: SymbolGlyphModifier; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationTitleOptions；  API声明：paddingStart?: LengthMetrics;  差异内容：paddingStart?: LengthMetrics; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationTitleOptions；  API声明：paddingEnd?: LengthMetrics;  差异内容：paddingEnd?: LengthMetrics; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationAttribute；  API声明：ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>): NavigationAttribute;  差异内容：ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>): NavigationAttribute; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationAttribute；  API声明：systemBarStyle(style: Optional<SystemBarStyle>): NavigationAttribute;  差异内容：systemBarStyle(style: Optional<SystemBarStyle>): NavigationAttribute; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationAnimatedTransition；  API声明：isInteractive?: boolean;  差异内容：isInteractive?: boolean; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationTransitionProxy；  API声明：isInteractive?: boolean;  差异内容：isInteractive?: boolean; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationTransitionProxy；  API声明：cancelTransition?(): void;  差异内容：cancelTransition?(): void; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationTransitionProxy；  API声明：updateTransition?(progress: number): void;  差异内容：updateTransition?(progress: number): void; | component/navigation.d.ts |
| 新增API | NA | 类名：NavContentInfo；  API声明：param?: Object;  差异内容：param?: Object; | component/navigation.d.ts |
| 新增API | NA | 类名：NavContentInfo；  API声明：navDestinationId?: string;  差异内容：navDestinationId?: string; | component/navigation.d.ts |
| 新增API | NA | 类名：NavDestinationAttribute；  API声明：ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>): NavDestinationAttribute;  差异内容：ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationAttribute；  API声明：systemBarStyle(style: Optional<SystemBarStyle>): NavDestinationAttribute;  差异内容：systemBarStyle(style: Optional<SystemBarStyle>): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：RelativeContainerAttribute；  API声明：barrier(barrierStyle: Array<LocalizedBarrierStyle>): RelativeContainerAttribute;  差异内容：barrier(barrierStyle: Array<LocalizedBarrierStyle>): RelativeContainerAttribute; | component/relative\_container.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum LocalizedBarrierDirection  差异内容： declare enum LocalizedBarrierDirection | component/relative\_container.d.ts |
| 新增API | NA | 类名：LocalizedBarrierDirection；  API声明：START = 0  差异内容：START = 0 | component/relative\_container.d.ts |
| 新增API | NA | 类名：LocalizedBarrierDirection；  API声明：END = 1  差异内容：END = 1 | component/relative\_container.d.ts |
| 新增API | NA | 类名：LocalizedBarrierDirection；  API声明：TOP = 2  差异内容：TOP = 2 | component/relative\_container.d.ts |
| 新增API | NA | 类名：LocalizedBarrierDirection；  API声明：BOTTOM = 3  差异内容：BOTTOM = 3 | component/relative\_container.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface LocalizedBarrierStyle  差异内容： declare interface LocalizedBarrierStyle | component/relative\_container.d.ts |
| 新增API | NA | 类名：LocalizedBarrierStyle；  API声明：id: string;  差异内容：id: string; | component/relative\_container.d.ts |
| 新增API | NA | 类名：LocalizedBarrierStyle；  API声明：localizedDirection: LocalizedBarrierDirection;  差异内容：localizedDirection: LocalizedBarrierDirection; | component/relative\_container.d.ts |
| 新增API | NA | 类名：LocalizedBarrierStyle；  API声明：referencedId: Array<string>;  差异内容：referencedId: Array<string>; | component/relative\_container.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：onWillInsert(callback: Callback<InsertValue, boolean>): SearchAttribute;  差异内容：onWillInsert(callback: Callback<InsertValue, boolean>): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：onDidInsert(callback: Callback<InsertValue>): SearchAttribute;  差异内容：onDidInsert(callback: Callback<InsertValue>): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：onWillDelete(callback: Callback<DeleteValue, boolean>): SearchAttribute;  差异内容：onWillDelete(callback: Callback<DeleteValue, boolean>): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：onDidDelete(callback: Callback<DeleteValue>): SearchAttribute;  差异内容：onDidDelete(callback: Callback<DeleteValue>): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：enablePreviewText(enable: boolean): SearchAttribute;  差异内容：enablePreviewText(enable: boolean): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：Indicator；  API声明：start(value: LengthMetrics): T;  差异内容：start(value: LengthMetrics): T; | component/swiper.d.ts |
| 新增API | NA | 类名：Indicator；  API声明：end(value: LengthMetrics): T;  差异内容：end(value: LengthMetrics): T; | component/swiper.d.ts |
| 新增API | NA | 类名：DotIndicator；  API声明：maxDisplayCount(maxDisplayCount: number): DotIndicator;  差异内容：maxDisplayCount(maxDisplayCount: number): DotIndicator; | component/swiper.d.ts |
| 新增API | NA | 类名：SubTabBarStyle；  API声明：padding(padding: LocalizedPadding): SubTabBarStyle;  差异内容：padding(padding: LocalizedPadding): SubTabBarStyle; | component/tab\_content.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：onWillInsert(callback: Callback<InsertValue, boolean>): TextAreaAttribute;  差异内容：onWillInsert(callback: Callback<InsertValue, boolean>): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：onDidInsert(callback: Callback<InsertValue>): TextAreaAttribute;  差异内容：onDidInsert(callback: Callback<InsertValue>): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：onWillDelete(callback: Callback<DeleteValue, boolean>): TextAreaAttribute;  差异内容：onWillDelete(callback: Callback<DeleteValue, boolean>): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：onDidDelete(callback: Callback<DeleteValue>): TextAreaAttribute;  差异内容：onDidDelete(callback: Callback<DeleteValue>): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：enablePreviewText(enable: boolean): TextAreaAttribute;  差异内容：enablePreviewText(enable: boolean): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：onWillInsert(callback: Callback<InsertValue, boolean>): TextInputAttribute;  差异内容：onWillInsert(callback: Callback<InsertValue, boolean>): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：onDidInsert(callback: Callback<InsertValue>): TextInputAttribute;  差异内容：onDidInsert(callback: Callback<InsertValue>): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：onWillDelete(callback: Callback<DeleteValue, boolean>): TextInputAttribute;  差异内容：onWillDelete(callback: Callback<DeleteValue, boolean>): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：onDidDelete(callback: Callback<DeleteValue>): TextInputAttribute;  差异内容：onDidDelete(callback: Callback<DeleteValue>): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：enablePreviewText(enable: boolean): TextInputAttribute;  差异内容：enablePreviewText(enable: boolean): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface ChipSymbolGlyphOptions  差异内容： export interface ChipSymbolGlyphOptions | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipSymbolGlyphOptions；  API声明：normal?: SymbolGlyphModifier;  差异内容：normal?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipSymbolGlyphOptions；  API声明：activated?: SymbolGlyphModifier;  差异内容：activated?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface LocalizedLabelMarginOptions  差异内容： export interface LocalizedLabelMarginOptions | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：LocalizedLabelMarginOptions；  API声明：start?: LengthMetrics;  差异内容：start?: LengthMetrics; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：LocalizedLabelMarginOptions；  API声明：end?: LengthMetrics;  差异内容：end?: LengthMetrics; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：LabelOptions；  API声明：localizedLabelMargin?: LocalizedLabelMarginOptions;  差异内容：localizedLabelMargin?: LocalizedLabelMarginOptions; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipOptions；  API声明：prefixSymbol?: ChipSymbolGlyphOptions;  差异内容：prefixSymbol?: ChipSymbolGlyphOptions; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipOptions；  API声明：suffixSymbol?: ChipSymbolGlyphOptions;  差异内容：suffixSymbol?: ChipSymbolGlyphOptions; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipOptions；  API声明：direction?: Direction;  差异内容：direction?: Direction; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：CounterOptions；  API声明：direction?: Direction;  差异内容：direction?: Direction; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItem；  API声明：label?: ResourceStr;  差异内容：label?: ResourceStr; | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：EditableTitleBar；  API声明：@Prop  contentMargin?: LocalizedMargin;  差异内容：@Prop  contentMargin?: LocalizedMargin; | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：PopupOptions；  API声明：direction?: Direction;  差异内容：direction?: Direction; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：CommonSegmentButtonOptions；  API声明：localizedButtonPadding?: LocalizedPadding;  差异内容：localizedButtonPadding?: LocalizedPadding; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：CommonSegmentButtonOptions；  API声明：localizedTextPadding?: LocalizedPadding;  差异内容：localizedTextPadding?: LocalizedPadding; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：CommonSegmentButtonOptions；  API声明：direction?: Direction;  差异内容：direction?: Direction; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonOptions；  API声明：localizedButtonPadding?: LocalizedPadding;  差异内容：localizedButtonPadding?: LocalizedPadding; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonOptions；  API声明：localizedTextPadding?: LocalizedPadding;  差异内容：localizedTextPadding?: LocalizedPadding; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonOptions；  API声明：direction?: Direction;  差异内容：direction?: Direction; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：window；  API声明： interface SystemBarStyle  差异内容： interface SystemBarStyle | api/@ohos.window.d.ts |
| 新增API | NA | 类名：SystemBarStyle；  API声明：statusBarContentColor?: string;  差异内容：statusBarContentColor?: string; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：on(type: 'subWindowClose', callback: Callback<void>): void;  差异内容：on(type: 'subWindowClose', callback: Callback<void>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：off(type: 'subWindowClose', callback?: Callback<void>): void;  差异内容：off(type: 'subWindowClose', callback?: Callback<void>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：ComponentContent；  API声明：dispose(): void;  差异内容：dispose(): void; | api/arkui/ComponentContent.d.ts |
| 新增API | NA | 类名：LengthMetrics；  API声明：static resource(value: Resource): LengthMetrics;  差异内容：static resource(value: Resource): LengthMetrics; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：IndexerAlign；  API声明：START  差异内容：START | component/alphabet\_indexer.d.ts |
| 新增API | NA | 类名：IndexerAlign；  API声明：END  差异内容：END | component/alphabet\_indexer.d.ts |
| 新增API | NA | 类名：AlphabetIndexerAttribute；  API声明：enableHapticFeedback(value: boolean): AlphabetIndexerAttribute;  差异内容：enableHapticFeedback(value: boolean): AlphabetIndexerAttribute; | component/alphabet\_indexer.d.ts |
| 新增API | NA | 类名：ContainerSpanAttribute；  API声明：attributeModifier(modifier: AttributeModifier<ContainerSpanAttribute>): ContainerSpanAttribute;  差异内容：attributeModifier(modifier: AttributeModifier<ContainerSpanAttribute>): ContainerSpanAttribute; | component/container\_span.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：dateTimeOptions?: DateTimeOptions;  差异内容：dateTimeOptions?: DateTimeOptions; | component/date\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class ForEachAttribute  差异内容： declare class ForEachAttribute | component/for\_each.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class LazyForEachAttribute  差异内容： declare class LazyForEachAttribute | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum SubMenuExpandingMode  差异内容： declare enum SubMenuExpandingMode | component/menu.d.ts |
| 新增API | NA | 类名：SubMenuExpandingMode；  API声明：SIDE\_EXPAND = 0  差异内容：SIDE\_EXPAND = 0 | component/menu.d.ts |
| 新增API | NA | 类名：SubMenuExpandingMode；  API声明：EMBEDDED\_EXPAND = 1  差异内容：EMBEDDED\_EXPAND = 1 | component/menu.d.ts |
| 新增API | NA | 类名：SubMenuExpandingMode；  API声明：STACK\_EXPAND = 2  差异内容：STACK\_EXPAND = 2 | component/menu.d.ts |
| 新增API | NA | 类名：MenuAttribute；  API声明：menuItemDivider(options: DividerStyleOptions | undefined): MenuAttribute;  差异内容：menuItemDivider(options: DividerStyleOptions | undefined): MenuAttribute; | component/menu.d.ts |
| 新增API | NA | 类名：MenuAttribute；  API声明：menuItemGroupDivider(options: DividerStyleOptions | undefined): MenuAttribute;  差异内容：menuItemGroupDivider(options: DividerStyleOptions | undefined): MenuAttribute; | component/menu.d.ts |
| 新增API | NA | 类名：MenuAttribute；  API声明：subMenuExpandingMode(mode: SubMenuExpandingMode): MenuAttribute;  差异内容：subMenuExpandingMode(mode: SubMenuExpandingMode): MenuAttribute; | component/menu.d.ts |
| 新增API | NA | 类名：SlideEffect；  API声明：START = 5  差异内容：START = 5 | component/page\_transition.d.ts |
| 新增API | NA | 类名：SlideEffect；  API声明：END = 6  差异内容：END = 6 | component/page\_transition.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface CircleStyleOptions  差异内容： declare interface CircleStyleOptions | component/pattern\_lock.d.ts |
| 新增API | NA | 类名：CircleStyleOptions；  API声明：color?: ResourceColor;  差异内容：color?: ResourceColor; | component/pattern\_lock.d.ts |
| 新增API | NA | 类名：CircleStyleOptions；  API声明：radius?: LengthMetrics;  差异内容：radius?: LengthMetrics; | component/pattern\_lock.d.ts |
| 新增API | NA | 类名：CircleStyleOptions；  API声明：enableWaveEffect?: boolean;  差异内容：enableWaveEffect?: boolean; | component/pattern\_lock.d.ts |
| 新增API | NA | 类名：PatternLockAttribute；  API声明：activateCircleStyle(options: Optional<CircleStyleOptions>): PatternLockAttribute;  差异内容：activateCircleStyle(options: Optional<CircleStyleOptions>): PatternLockAttribute; | component/pattern\_lock.d.ts |
| 新增API | NA | 类名：RefreshAttribute；  API声明：pullDownRatio(ratio: Optional<number>): RefreshAttribute;  差异内容：pullDownRatio(ratio: Optional<number>): RefreshAttribute; | component/refresh.d.ts |
| 新增API | NA | 类名：RichEditorSpanType；  API声明：BUILDER = 3  差异内容：BUILDER = 3 | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorBaseController；  API声明：getLayoutManager(): LayoutManager;  差异内容：getLayoutManager(): LayoutManager; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorController；  API声明：fromStyledString(value: StyledString): Array<RichEditorSpan>;  差异内容：fromStyledString(value: StyledString): Array<RichEditorSpan>; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorController；  API声明：toStyledString(value: RichEditorRange): StyledString;  差异内容：toStyledString(value: RichEditorRange): StyledString; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type RichEditorSpan = RichEditorImageSpanResult | RichEditorTextSpanResult;  差异内容：declare type RichEditorSpan = RichEditorImageSpanResult | RichEditorTextSpanResult; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：SelectOption；  API声明：symbolIcon?: SymbolGlyphModifier;  差异内容：symbolIcon?: SymbolGlyphModifier; | component/select.d.ts |
| 新增API | NA | 类名：SelectAttribute；  API声明：divider(options: Optional<DividerOptions> | null): SelectAttribute;  差异内容：divider(options: Optional<DividerOptions> | null): SelectAttribute; | component/select.d.ts |
| 新增API | NA | 类名：MenuItemConfiguration；  API声明：symbolIcon?: SymbolGlyphModifier;  差异内容：symbolIcon?: SymbolGlyphModifier; | component/select.d.ts |
| 新增API | NA | 类名：SliderInteraction；  API声明：SLIDE\_AND\_CLICK\_UP = 2  差异内容：SLIDE\_AND\_CLICK\_UP = 2 | component/slider.d.ts |
| 新增API | NA | 类名：TabsController；  API声明：preloadItems(indices: Optional<Array<number>>): Promise<void>;  差异内容：preloadItems(indices: Optional<Array<number>>): Promise<void>; | component/tabs.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：textSelectable(mode: TextSelectableMode): TextAttribute;  差异内容：textSelectable(mode: TextSelectableMode): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextController；  API声明：getLayoutManager(): LayoutManager;  差异内容：getLayoutManager(): LayoutManager; | component/text.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface InsertValue  差异内容： declare interface InsertValue | component/text\_common.d.ts |
| 新增API | NA | 类名：InsertValue；  API声明：insertOffset: number;  差异内容：insertOffset: number; | component/text\_common.d.ts |
| 新增API | NA | 类名：InsertValue；  API声明：insertValue: string;  差异内容：insertValue: string; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum TextDeleteDirection  差异内容： declare enum TextDeleteDirection | component/text\_common.d.ts |
| 新增API | NA | 类名：TextDeleteDirection；  API声明：BACKWARD = 0  差异内容：BACKWARD = 0 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextDeleteDirection；  API声明：FORWARD = 1  差异内容：FORWARD = 1 | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface DeleteValue  差异内容： declare interface DeleteValue | component/text\_common.d.ts |
| 新增API | NA | 类名：DeleteValue；  API声明：deleteOffset: number;  差异内容：deleteOffset: number; | component/text\_common.d.ts |
| 新增API | NA | 类名：DeleteValue；  API声明：direction: TextDeleteDirection;  差异内容：direction: TextDeleteDirection; | component/text\_common.d.ts |
| 新增API | NA | 类名：DeleteValue；  API声明：deleteValue: string;  差异内容：deleteValue: string; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type EditableTextOnChangeCallback = (value: string, previewRange?: TextRange) => void;  差异内容：declare type EditableTextOnChangeCallback = (value: string, previewRange?: TextRange) => void; | component/text\_common.d.ts |
| 新增API | NA | 类名：TextBaseController；  API声明：getLayoutManager(): LayoutManager;  差异内容：getLayoutManager(): LayoutManager; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface LayoutManager  差异内容： declare interface LayoutManager | component/text\_common.d.ts |
| 新增API | NA | 类名：LayoutManager；  API声明：getLineCount(): number;  差异内容：getLineCount(): number; | component/text\_common.d.ts |
| 新增API | NA | 类名：LayoutManager；  API声明：getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity;  差异内容：getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity; | component/text\_common.d.ts |
| 新增API | NA | 类名：LayoutManager；  API声明：getLineMetrics(lineNumber: number): LineMetrics;  差异内容：getLineMetrics(lineNumber: number): LineMetrics; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： interface PositionWithAffinity  差异内容： interface PositionWithAffinity | component/text\_common.d.ts |
| 新增API | NA | 类名：PositionWithAffinity；  API声明：position: number;  差异内容：position: number; | component/text\_common.d.ts |
| 新增API | NA | 类名：PositionWithAffinity；  API声明：affinity: Affinity;  差异内容：affinity: Affinity; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type Affinity = import('../api/@ohos.graphics.text').default.Affinity;  差异内容：declare type Affinity = import('../api/@ohos.graphics.text').default.Affinity; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type LineMetrics = import('../api/@ohos.graphics.text').default.LineMetrics;  差异内容：declare type LineMetrics = import('../api/@ohos.graphics.text').default.LineMetrics; | component/text\_common.d.ts |
| 新增API | NA | 类名：TimePickerDialogOptions；  API声明：dateTimeOptions?: DateTimeOptions;  差异内容：dateTimeOptions?: DateTimeOptions; | component/time\_picker.d.ts |
| 新增API | NA | 类名：BorderOptions；  API声明：dashGap?: EdgeWidths | LengthMetrics | LocalizedEdgeWidths;  差异内容：dashGap?: EdgeWidths | LengthMetrics | LocalizedEdgeWidths; | component/units.d.ts |
| 新增API | NA | 类名：BorderOptions；  API声明：dashWidth?: EdgeWidths | LengthMetrics | LocalizedEdgeWidths;  差异内容：dashWidth?: EdgeWidths | LengthMetrics | LocalizedEdgeWidths; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface DividerStyleOptions  差异内容： declare interface DividerStyleOptions | component/units.d.ts |
| 新增API | NA | 类名：DividerStyleOptions；  API声明：strokeWidth?: LengthMetrics;  差异内容：strokeWidth?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：DividerStyleOptions；  API声明：color?: ResourceColor;  差异内容：color?: ResourceColor; | component/units.d.ts |
| 新增API | NA | 类名：DividerStyleOptions；  API声明：startMargin?: LengthMetrics;  差异内容：startMargin?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：DividerStyleOptions；  API声明：endMargin?: LengthMetrics;  差异内容：endMargin?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：VideoOptions；  API声明：imageAIOptions?: ImageAIOptions;  差异内容：imageAIOptions?: ImageAIOptions; | component/video.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum WaterFlowLayoutMode  差异内容： declare enum WaterFlowLayoutMode | component/water\_flow.d.ts |
| 新增API | NA | 类名：WaterFlowLayoutMode；  API声明：ALWAYS\_TOP\_DOWN = 0  差异内容：ALWAYS\_TOP\_DOWN = 0 | component/water\_flow.d.ts |
| 新增API | NA | 类名：WaterFlowLayoutMode；  API声明：SLIDING\_WINDOW = 1  差异内容：SLIDING\_WINDOW = 1 | component/water\_flow.d.ts |
| 新增API | NA | 类名：WaterFlowOptions；  API声明：layoutMode?: WaterFlowLayoutMode;  差异内容：layoutMode?: WaterFlowLayoutMode; | component/water\_flow.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum FocusPriority  差异内容： declare enum FocusPriority | component/focus.d.ts |
| 新增API | NA | 类名：FocusPriority；  API声明：AUTO = 0  差异内容：AUTO = 0 | component/focus.d.ts |
| 新增API | NA | 类名：FocusPriority；  API声明：PRIOR = 2000  差异内容：PRIOR = 2000 | component/focus.d.ts |
| 新增API | NA | 类名：FocusPriority；  API声明：PREVIOUS = 3000  差异内容：PREVIOUS = 3000 | component/focus.d.ts |
| 新增API | NA | 类名：global；  API声明： interface VirtualScrollOptions  差异内容： interface VirtualScrollOptions | component/repeat.d.ts |
| 新增API | NA | 类名：VirtualScrollOptions；  API声明：totalCount?: number;  差异内容：totalCount?: number; | component/repeat.d.ts |
| 新增API | NA | 类名：global；  API声明： interface TemplateOptions  差异内容： interface TemplateOptions | component/repeat.d.ts |
| 新增API | NA | 类名：TemplateOptions；  API声明：cachedCount?: number;  差异内容：cachedCount?: number; | component/repeat.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type TemplateTypedFunc<T> = (item: T, index: number) => string;  差异内容：declare type TemplateTypedFunc<T> = (item: T, index: number) => string; | component/repeat.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type RepeatItemBuilder<T> = (repeatItem: RepeatItem<T>) => void;  差异内容：declare type RepeatItemBuilder<T> = (repeatItem: RepeatItem<T>) => void; | component/repeat.d.ts |
| 新增API | NA | 类名：RepeatAttribute；  API声明：virtualScroll(virtualScrollOptions?: VirtualScrollOptions): RepeatAttribute<T>;  差异内容：virtualScroll(virtualScrollOptions?: VirtualScrollOptions): RepeatAttribute<T>; | component/repeat.d.ts |
| 新增API | NA | 类名：RepeatAttribute；  API声明：template(type: string, itemBuilder: RepeatItemBuilder<T>, templateOptions?: TemplateOptions): RepeatAttribute<T>;  差异内容：template(type: string, itemBuilder: RepeatItemBuilder<T>, templateOptions?: TemplateOptions): RepeatAttribute<T>; | component/repeat.d.ts |
| 新增API | NA | 类名：RepeatAttribute；  API声明：templateId(typedFunc: TemplateTypedFunc<T>): RepeatAttribute<T>;  差异内容：templateId(typedFunc: TemplateTypedFunc<T>): RepeatAttribute<T>; | component/repeat.d.ts |
| 删除API | 类名：global；  API声明： declare enum SymbolRenderingStrategy  差异内容： declare enum SymbolRenderingStrategy | NA | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 删除API | 类名：SymbolRenderingStrategy；  API声明：SINGLE = 0  差异内容：SINGLE = 0 | NA | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 删除API | 类名：SymbolRenderingStrategy；  API声明：MULTIPLE\_COLOR = 1  差异内容：MULTIPLE\_COLOR = 1 | NA | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 删除API | 类名：SymbolRenderingStrategy；  API声明：MULTIPLE\_OPACITY = 2  差异内容：MULTIPLE\_OPACITY = 2 | NA | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 删除API | 类名：global；  API声明： declare enum SymbolEffectStrategy  差异内容： declare enum SymbolEffectStrategy | NA | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 删除API | 类名：SymbolEffectStrategy；  API声明：NONE = 0  差异内容：NONE = 0 | NA | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 删除API | 类名：SymbolEffectStrategy；  API声明：SCALE = 1  差异内容：SCALE = 1 | NA | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 删除API | 类名：SymbolEffectStrategy；  API声明：HIERARCHICAL = 2  差异内容：HIERARCHICAL = 2 | NA | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 删除API | 类名：global；  API声明：declare type WindowMode = import('../api/@ohos.window').WindowMode;  差异内容：declare type WindowMode = import('../api/@ohos.window').WindowMode; | NA | component/folder\_stack.d.ts |
| 删除API | 类名：HoverEventParam；  API声明：windowMode: WindowMode;  差异内容：windowMode: WindowMode; | NA | component/folder\_stack.d.ts |
| 新增装饰器 | 类名：IconGroupSuffix；  API声明：@Prop  items: Array<IconItemOptions>;  差异内容：NA | 类名：IconGroupSuffix；  API声明：@Require  @Prop  items: Array<IconItemOptions | SymbolGlyphModifier>;  差异内容：Require | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增装饰器 | 类名：ChipGroup；  API声明：@Prop  items: ChipGroupItemOptions[];  差异内容：NA | 类名：ChipGroup；  API声明：@Require  @Prop  items: ChipGroupItemOptions[];  差异内容：Require | api/@ohos.arkui.advanced.ChipGroup.d.ets |
