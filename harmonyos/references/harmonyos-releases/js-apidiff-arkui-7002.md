---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-7002
title: ArkUI
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > ArkUI
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:03+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:eb9a648b1e83c6056988a23413f412de1a7cd4ed5abb5aa19c05ddebc00e1b43
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API卡片权限变更 | 类名：CommonMethod；  API声明：hitTestBehavior(value: HitTestMode): T;  差异内容：NA | 类名：CommonMethod；  API声明：hitTestBehavior(value: HitTestMode): T;  差异内容：form | component/common.d.ts |
| API卡片权限变更 | 类名：global；  API声明：declare enum HitTestMode  差异内容：NA | 类名：global；  API声明：declare enum HitTestMode  差异内容：form | component/enums.d.ts |
| API卡片权限变更 | 类名：HitTestMode；  API声明：Default  差异内容：NA | 类名：HitTestMode；  API声明：Default  差异内容：form | component/enums.d.ts |
| API卡片权限变更 | 类名：HitTestMode；  API声明：Block  差异内容：NA | 类名：HitTestMode；  API声明：Block  差异内容：form | component/enums.d.ts |
| API卡片权限变更 | 类名：HitTestMode；  API声明：Transparent  差异内容：NA | 类名：HitTestMode；  API声明：Transparent  差异内容：form | component/enums.d.ts |
| API卡片权限变更 | 类名：HitTestMode；  API声明：None  差异内容：NA | 类名：HitTestMode；  API声明：None  差异内容：form | component/enums.d.ts |
| API卡片权限变更 | 类名：HitTestMode；  API声明：BLOCK\_HIERARCHY  差异内容：NA | 类名：HitTestMode；  API声明：BLOCK\_HIERARCHY  差异内容：form | component/enums.d.ts |
| API卡片权限变更 | 类名：HitTestMode；  API声明：BLOCK\_DESCENDANTS  差异内容：NA | 类名：HitTestMode；  API声明：BLOCK\_DESCENDANTS  差异内容：form | component/enums.d.ts |
| API卡片权限变更 | 类名：SwiperAttribute；  API声明：customContentTransition(transition: SwiperContentAnimatedTransition): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：customContentTransition(transition: SwiperContentAnimatedTransition): SwiperAttribute;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：global；  API声明：declare interface SwiperContentAnimatedTransition  差异内容：NA | 类名：global；  API声明：declare interface SwiperContentAnimatedTransition  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperContentAnimatedTransition；  API声明：timeout?: number;  差异内容：NA | 类名：SwiperContentAnimatedTransition；  API声明：timeout?: number;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperContentAnimatedTransition；  API声明：transition: Callback<SwiperContentTransitionProxy>;  差异内容：NA | 类名：SwiperContentAnimatedTransition；  API声明：transition: Callback<SwiperContentTransitionProxy>;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：global；  API声明：declare interface SwiperContentTransitionProxy  差异内容：NA | 类名：global；  API声明：declare interface SwiperContentTransitionProxy  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperContentTransitionProxy；  API声明：selectedIndex: number;  差异内容：NA | 类名：SwiperContentTransitionProxy；  API声明：selectedIndex: number;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperContentTransitionProxy；  API声明：index: number;  差异内容：NA | 类名：SwiperContentTransitionProxy；  API声明：index: number;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperContentTransitionProxy；  API声明：position: number;  差异内容：NA | 类名：SwiperContentTransitionProxy；  API声明：position: number;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperContentTransitionProxy；  API声明：mainAxisLength: number;  差异内容：NA | 类名：SwiperContentTransitionProxy；  API声明：mainAxisLength: number;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperContentTransitionProxy；  API声明：finishTransition(): void;  差异内容：NA | 类名：SwiperContentTransitionProxy；  API声明：finishTransition(): void;  差异内容：form | component/swiper.d.ts |
| 新增错误码 | 类名：DrawableDescriptor；  API声明：getPixelMap(): image.PixelMap;  差异内容：NA | 类名：DrawableDescriptor；  API声明：getPixelMap(): image.PixelMap;  差异内容：111002 | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增错误码 | 类名：DrawableDescriptor；  API声明：loadSync(): DrawableDescriptorLoadedResult;  差异内容：NA | 类名：DrawableDescriptor；  API声明：loadSync(): DrawableDescriptorLoadedResult;  差异内容：111002 | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增错误码 | 类名：DrawableDescriptor；  API声明：load(): Promise<DrawableDescriptorLoadedResult>;  差异内容：NA | 类名：DrawableDescriptor；  API声明：load(): Promise<DrawableDescriptorLoadedResult>;  差异内容：111002 | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增错误码 | 类名：LayeredDrawableDescriptor；  API声明：getForeground(): DrawableDescriptor;  差异内容：NA | 类名：LayeredDrawableDescriptor；  API声明：getForeground(): DrawableDescriptor;  差异内容：111002 | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增错误码 | 类名：LayeredDrawableDescriptor；  API声明：getBackground(): DrawableDescriptor;  差异内容：NA | 类名：LayeredDrawableDescriptor；  API声明：getBackground(): DrawableDescriptor;  差异内容：111002 | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增错误码 | 类名：LayeredDrawableDescriptor；  API声明：getMask(): DrawableDescriptor;  差异内容：NA | 类名：LayeredDrawableDescriptor；  API声明：getMask(): DrawableDescriptor;  差异内容：111002 | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增错误码 | 类名：window；  API声明：function createWindow(config: Configuration, callback: AsyncCallback<Window>): void;  差异内容：NA | 类名：window；  API声明：function createWindow(config: Configuration, callback: AsyncCallback<Window>): void;  差异内容：1300008 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：window；  API声明：function createWindow(config: Configuration): Promise<Window>;  差异内容：NA | 类名：window；  API声明：function createWindow(config: Configuration): Promise<Window>;  差异内容：1300008 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：window；  API声明：function getAllWindowLayoutInfo(displayId: number): Promise<Array<WindowLayoutInfo>>;  差异内容：NA | 类名：window；  API声明：function getAllWindowLayoutInfo(displayId: number): Promise<Array<WindowLayoutInfo>>;  差异内容：1300002 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：Window；  API声明：destroyWindow(callback: AsyncCallback<void>): void;  差异内容：NA | 类名：Window；  API声明：destroyWindow(callback: AsyncCallback<void>): void;  差异内容：1300003 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：Window；  API声明：destroyWindow(): Promise<void>;  差异内容：NA | 类名：Window；  API声明：destroyWindow(): Promise<void>;  差异内容：1300003 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：Window；  API声明：loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：Window；  API声明：loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void;  差异内容：1300003 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：Window；  API声明：loadContent(path: string, storage: LocalStorage): Promise<void>;  差异内容：NA | 类名：Window；  API声明：loadContent(path: string, storage: LocalStorage): Promise<void>;  差异内容：1300003 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：Window；  API声明：setUIContent(path: string, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：Window；  API声明：setUIContent(path: string, callback: AsyncCallback<void>): void;  差异内容：1300003 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：Window；  API声明：setUIContent(path: string): Promise<void>;  差异内容：NA | 类名：Window；  API声明：setUIContent(path: string): Promise<void>;  差异内容：1300003 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：Window；  API声明：maximize(presentation?: MaximizePresentation): Promise<void>;  差异内容：NA | 类名：Window；  API声明：maximize(presentation?: MaximizePresentation): Promise<void>;  差异内容：1300005 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：Window；  API声明：setWindowDecorVisible(isVisible: boolean): void;  差异内容：NA | 类名：Window；  API声明：setWindowDecorVisible(isVisible: boolean): void;  差异内容：1300004 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：WindowStage；  API声明：createSubWindow(name: string): Promise<Window>;  差异内容：NA | 类名：WindowStage；  API声明：createSubWindow(name: string): Promise<Window>;  差异内容：1300005 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：WindowStage；  API声明：createSubWindow(name: string, callback: AsyncCallback<Window>): void;  差异内容：NA | 类名：WindowStage；  API声明：createSubWindow(name: string, callback: AsyncCallback<Window>): void;  差异内容：1300005 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：WindowStage；  API声明：getSubWindow(): Promise<Array<Window>>;  差异内容：NA | 类名：WindowStage；  API声明：getSubWindow(): Promise<Array<Window>>;  差异内容：1300005 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：WindowStage；  API声明：getSubWindow(callback: AsyncCallback<Array<Window>>): void;  差异内容：NA | 类名：WindowStage；  API声明：getSubWindow(callback: AsyncCallback<Array<Window>>): void;  差异内容：1300005 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：WindowStage；  API声明：loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：WindowStage；  API声明：loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void;  差异内容：1300005 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：WindowStage；  API声明：loadContent(path: string, storage?: LocalStorage): Promise<void>;  差异内容：NA | 类名：WindowStage；  API声明：loadContent(path: string, storage?: LocalStorage): Promise<void>;  差异内容：1300005 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：WindowStage；  API声明：loadContent(path: string, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：WindowStage；  API声明：loadContent(path: string, callback: AsyncCallback<void>): void;  差异内容：1300005 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：typeNode；  API声明：function bindController(node: FrameNode, controller: Scroller, nodeType: 'Scroll'): void;  差异内容：NA | 类名：typeNode；  API声明：function bindController(node: FrameNode, controller: Scroller, nodeType: 'Scroll'): void;  差异内容：100021 | api/arkui/FrameNode.d.ts |
| 删除错误码 | 类名：Display；  API声明：on(type: 'availableAreaChange', callback: Callback<Rect>): void;  差异内容：801 | 类名：Display；  API声明：on(type: 'availableAreaChange', callback: Callback<Rect>): void;  差异内容：NA | api/@ohos.display.d.ts |
| 删除错误码 | 类名：Display；  API声明：off(type: 'availableAreaChange', callback?: Callback<Rect>): void;  差异内容：801 | 类名：Display；  API声明：off(type: 'availableAreaChange', callback?: Callback<Rect>): void;  差异内容：NA | api/@ohos.display.d.ts |
| 权限变更 | 类名：screenshot；  API声明：function capture(options?: CaptureOption): Promise<image.PixelMap>;  差异内容：ohos.permission.CUSTOM\_SCREEN\_CAPTURE or ohos.permission.CUSTOM\_SCREEN\_RECORDING | 类名：screenshot；  API声明：function capture(options?: CaptureOption): Promise<image.PixelMap>;  差异内容：ohos.permission.CUSTOM\_SCREEN\_CAPTURE or ohos.permission.CUSTOM\_SCREEN\_RECORDING [since 22] | api/@ohos.screenshot.d.ts |
| 权限变更 | 类名：window；  API声明：function createWindow(config: Configuration, callback: AsyncCallback<Window>): void;  差异内容：ohos.permission.SYSTEM\_FLOAT\_WINDOW | 类名：window；  API声明：function createWindow(config: Configuration, callback: AsyncCallback<Window>): void;  差异内容：ohos.permission.SYSTEM\_FLOAT\_WINDOW [since 12] | api/@ohos.window.d.ts |
| 权限变更 | 类名：window；  API声明：function createWindow(config: Configuration): Promise<Window>;  差异内容：ohos.permission.SYSTEM\_FLOAT\_WINDOW | 类名：window；  API声明：function createWindow(config: Configuration): Promise<Window>;  差异内容：ohos.permission.SYSTEM\_FLOAT\_WINDOW [since 12] | api/@ohos.window.d.ts |
| 函数变更 | 类名：CircleAttribute；  API声明：stroke(value: ResourceColor | ColorMetrics): T;  差异内容：T | 类名：CircleAttribute；  API声明：stroke(value: ResourceColor | ColorMetrics): CircleAttribute;  差异内容：CircleAttribute | component/circle.d.ts |
| 函数变更 | 类名：CircleAttribute；  API声明：fill(value: ResourceColor | ColorMetrics): T;  差异内容：T | 类名：CircleAttribute；  API声明：fill(value: ResourceColor | ColorMetrics): CircleAttribute;  差异内容：CircleAttribute | component/circle.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface ChipGroupV2ItemConfig  差异内容：export interface ChipGroupV2ItemConfig | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemConfig；  API声明：prefixIcon?: ChipV2PrefixImageIconConfig;  差异内容：prefixIcon?: ChipV2PrefixImageIconConfig; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemConfig；  API声明：prefixSymbolIcon?: ChipV2PrefixSymbolIconConfig;  差异内容：prefixSymbolIcon?: ChipV2PrefixSymbolIconConfig; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemConfig；  API声明：label: ChipV2LabelConfig;  差异内容：label: ChipV2LabelConfig; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemConfig；  API声明：suffixIcon?: ChipV2SuffixImageIconConfig;  差异内容：suffixIcon?: ChipV2SuffixImageIconConfig; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemConfig；  API声明：suffixSymbolIcon?: ChipV2SuffixSymbolIconConfig;  差异内容：suffixSymbolIcon?: ChipV2SuffixSymbolIconConfig; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemConfig；  API声明：allowClose?: boolean;  差异内容：allowClose?: boolean; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemConfig；  API声明：closeIcon?: ChipV2CloseConfig;  差异内容：closeIcon?: ChipV2CloseConfig; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemConfig；  API声明：accessibilityDescription?: ResourceStr;  差异内容：accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemConfig；  API声明：accessibilityLevel?: string;  差异内容：accessibilityLevel?: string; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class ChipGroupV2Item  差异内容：export declare class ChipGroupV2Item | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2Item；  API声明：@Trace  public prefixIcon?: ChipV2PrefixImageIcon;  差异内容：@Trace  public prefixIcon?: ChipV2PrefixImageIcon; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2Item；  API声明：@Trace  public prefixSymbolIcon?: ChipV2PrefixSymbolIcon;  差异内容：@Trace  public prefixSymbolIcon?: ChipV2PrefixSymbolIcon; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2Item；  API声明：@Trace  public label: ChipV2Label;  差异内容：@Trace  public label: ChipV2Label; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2Item；  API声明：@Trace  public suffixIcon?: ChipV2SuffixImageIcon;  差异内容：@Trace  public suffixIcon?: ChipV2SuffixImageIcon; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2Item；  API声明：@Trace  public suffixSymbolIcon?: ChipV2SuffixSymbolIcon;  差异内容：@Trace  public suffixSymbolIcon?: ChipV2SuffixSymbolIcon; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2Item；  API声明：@Trace  public allowClose?: boolean;  差异内容：@Trace  public allowClose?: boolean; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2Item；  API声明：@Trace  public closeIcon?: ChipV2CloseConfig;  差异内容：@Trace  public closeIcon?: ChipV2CloseConfig; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2Item；  API声明：@Trace  public accessibilityDescription?: ResourceStr;  差异内容：@Trace  public accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2Item；  API声明：@Trace  public accessibilityLevel?: string;  差异内容：@Trace  public accessibilityLevel?: string; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class ChipGroupV2Items  差异内容：export declare class ChipGroupV2Items | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface ChipGroupV2ItemStyleConfig  差异内容：export interface ChipGroupV2ItemStyleConfig | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemStyleConfig；  API声明：size?: ChipV2Size | SizeT<LengthMetrics>;  差异内容：size?: ChipV2Size | SizeT<LengthMetrics>; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemStyleConfig；  API声明：backgroundColor?: ColorMetrics;  差异内容：backgroundColor?: ColorMetrics; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemStyleConfig；  API声明：fontColor?: ColorMetrics;  差异内容：fontColor?: ColorMetrics; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemStyleConfig；  API声明：selectedFontColor?: ColorMetrics;  差异内容：selectedFontColor?: ColorMetrics; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemStyleConfig；  API声明：selectedBackgroundColor?: ColorMetrics;  差异内容：selectedBackgroundColor?: ColorMetrics; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemStyleConfig；  API声明：backgroundSystemMaterial?: uiMaterial.Material;  差异内容：backgroundSystemMaterial?: uiMaterial.Material; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemStyleConfig；  API声明：selectedBackgroundSystemMaterial?: uiMaterial.Material;  差异内容：selectedBackgroundSystemMaterial?: uiMaterial.Material; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class ChipGroupV2ItemStyle  差异内容：export declare class ChipGroupV2ItemStyle | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemStyle；  API声明：@Trace  public size?: ChipV2Size | SizeT<LengthMetrics>;  差异内容：@Trace  public size?: ChipV2Size | SizeT<LengthMetrics>; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemStyle；  API声明：@Trace  public backgroundColor?: ColorMetrics;  差异内容：@Trace  public backgroundColor?: ColorMetrics; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemStyle；  API声明：@Trace  public fontColor?: ColorMetrics;  差异内容：@Trace  public fontColor?: ColorMetrics; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemStyle；  API声明：@Trace  public selectedFontColor?: ColorMetrics;  差异内容：@Trace  public selectedFontColor?: ColorMetrics; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemStyle；  API声明：@Trace  public selectedBackgroundColor?: ColorMetrics;  差异内容：@Trace  public selectedBackgroundColor?: ColorMetrics; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemStyle；  API声明：@Trace  public backgroundSystemMaterial?: uiMaterial.Material;  差异内容：@Trace  public backgroundSystemMaterial?: uiMaterial.Material; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2ItemStyle；  API声明：@Trace  public selectedBackgroundSystemMaterial?: uiMaterial.Material;  差异内容：@Trace  public selectedBackgroundSystemMaterial?: uiMaterial.Material; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface ChipGroupV2SpaceConfig  差异内容：export interface ChipGroupV2SpaceConfig | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2SpaceConfig；  API声明：itemSpace?: string | number;  差异内容：itemSpace?: string | number; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2SpaceConfig；  API声明：startSpace?: Length;  差异内容：startSpace?: Length; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2SpaceConfig；  API声明：endSpace?: Length;  差异内容：endSpace?: Length; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class ChipGroupV2Space  差异内容：export declare class ChipGroupV2Space | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2Space；  API声明：@Trace  public itemSpace?: string | number;  差异内容：@Trace  public itemSpace?: string | number; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2Space；  API声明：@Trace  public startSpace?: Length;  差异内容：@Trace  public startSpace?: Length; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2Space；  API声明：@Trace  public endSpace?: Length;  差异内容：@Trace  public endSpace?: Length; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface ChipGroupV2IconItemConfig  差异内容：export interface ChipGroupV2IconItemConfig | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2IconItemConfig；  API声明：icon: ChipV2ImageIconConfig;  差异内容：icon: ChipV2ImageIconConfig; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2IconItemConfig；  API声明：action: Callback<void>;  差异内容：action: Callback<void>; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2IconItemConfig；  API声明：accessibilityText?: ResourceStr;  差异内容：accessibilityText?: ResourceStr; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2IconItemConfig；  API声明：accessibilityDescription?: ResourceStr;  差异内容：accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2IconItemConfig；  API声明：accessibilityLevel?: string;  差异内容：accessibilityLevel?: string; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface ChipGroupV2SymbolItemConfig  差异内容：export interface ChipGroupV2SymbolItemConfig | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2SymbolItemConfig；  API声明：symbol: SymbolGlyphModifier;  差异内容：symbol: SymbolGlyphModifier; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2SymbolItemConfig；  API声明：action: VoidCallback;  差异内容：action: VoidCallback; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2SymbolItemConfig；  API声明：accessibilityText?: ResourceStr;  差异内容：accessibilityText?: ResourceStr; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2SymbolItemConfig；  API声明：accessibilityDescription?: ResourceStr;  差异内容：accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2SymbolItemConfig；  API声明：accessibilityLevel?: string;  差异内容：accessibilityLevel?: string; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface ChipGroupV2PaddingConfig  差异内容：export interface ChipGroupV2PaddingConfig | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2PaddingConfig；  API声明：top: Length;  差异内容：top: Length; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2PaddingConfig；  API声明：bottom: Length;  差异内容：bottom: Length; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class ChipGroupV2Padding  差异内容：export declare class ChipGroupV2Padding | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2Padding；  API声明：@Trace  public top: Length;  差异内容：@Trace  public top: Length; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2Padding；  API声明：@Trace  public bottom: Length;  差异内容：@Trace  public bottom: Length; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare struct ChipGroupV2IconGroupSuffix  差异内容：export declare struct ChipGroupV2IconGroupSuffix | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2IconGroupSuffix；  API声明：@Require  @Param  items: Array<ChipGroupV2IconItemConfig | SymbolGlyphModifier | ChipGroupV2SymbolItemConfig>;  差异内容：@Require  @Param  items: Array<ChipGroupV2IconItemConfig | SymbolGlyphModifier | ChipGroupV2SymbolItemConfig>; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2IconGroupSuffix；  API声明：@Param  iconBackgroundSystemMaterial?: uiMaterial.Material;  差异内容：@Param  iconBackgroundSystemMaterial?: uiMaterial.Material; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2IconGroupSuffix；  API声明：build(): void;  差异内容：build(): void; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare struct ChipGroupV2  差异内容：export declare struct ChipGroupV2 | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2；  API声明：@Require  @Param  items: ChipGroupV2Items;  差异内容：@Require  @Param  items: ChipGroupV2Items; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2；  API声明：@Event  $items?: Callback<ChipGroupV2Items>;  差异内容：@Event  $items?: Callback<ChipGroupV2Items>; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2；  API声明：@Param  itemStyle?: ChipGroupV2ItemStyle;  差异内容：@Param  itemStyle?: ChipGroupV2ItemStyle; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2；  API声明：@Param  selectedIndexes?: Array<number>;  差异内容：@Param  selectedIndexes?: Array<number>; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2；  API声明：@Event  $selectedIndexes?: Callback<Array<number>>;  差异内容：@Event  $selectedIndexes?: Callback<Array<number>>; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2；  API声明：@Param  multiple?: boolean;  差异内容：@Param  multiple?: boolean; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2；  API声明：@Param  chipGroupSpace?: ChipGroupV2Space;  差异内容：@Param  chipGroupSpace?: ChipGroupV2Space; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2；  API声明：@Param  chipGroupPadding?: ChipGroupV2Padding;  差异内容：@Param  chipGroupPadding?: ChipGroupV2Padding; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2；  API声明：@Event  onChange?: Callback<Array<number>>;  差异内容：@Event  onChange?: Callback<Array<number>>; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2；  API声明：@BuilderParam  suffix?: Callback<void>;  差异内容：@BuilderParam  suffix?: Callback<void>; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：ChipGroupV2；  API声明：build(): void;  差异内容：build(): void; | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare enum ChipV2Size  差异内容：export declare enum ChipV2Size | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Size；  API声明：NORMAL = 'NORMAL'  差异内容：NORMAL = 'NORMAL' | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Size；  API声明：SMALL = 'SMALL'  差异内容：SMALL = 'SMALL' | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare enum ChipV2AccessibilitySelectedType  差异内容：export declare enum ChipV2AccessibilitySelectedType | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2AccessibilitySelectedType；  API声明：CLICKED = 0  差异内容：CLICKED = 0 | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2AccessibilitySelectedType；  API声明：CHECKED = 1  差异内容：CHECKED = 1 | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2AccessibilitySelectedType；  API声明：SELECTED = 2  差异内容：SELECTED = 2 | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface ChipV2ImageIconConfig  差异内容：export interface ChipV2ImageIconConfig | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2ImageIconConfig；  API声明：src: ResourceStr;  差异内容：src: ResourceStr; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2ImageIconConfig；  API声明：size?: SizeT<LengthMetrics>;  差异内容：size?: SizeT<LengthMetrics>; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2ImageIconConfig；  API声明：fillColor?: ColorMetrics;  差异内容：fillColor?: ColorMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2ImageIconConfig；  API声明：activatedFillColor?: ColorMetrics;  差异内容：activatedFillColor?: ColorMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2ImageIconConfig；  API声明：modifier?: ImageModifier;  差异内容：modifier?: ImageModifier; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export abstract class ChipV2ImageIcon  差异内容：export abstract class ChipV2ImageIcon | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2ImageIcon；  API声明：@Trace  public src: ResourceStr;  差异内容：@Trace  public src: ResourceStr; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2ImageIcon；  API声明：@Trace  public size?: SizeT<LengthMetrics>;  差异内容：@Trace  public size?: SizeT<LengthMetrics>; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2ImageIcon；  API声明：@Trace  public fillColor?: ColorMetrics;  差异内容：@Trace  public fillColor?: ColorMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2ImageIcon；  API声明：@Trace  public activatedFillColor?: ColorMetrics;  差异内容：@Trace  public activatedFillColor?: ColorMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2ImageIcon；  API声明：@Trace  public modifier?: ImageModifier;  差异内容：@Trace  public modifier?: ImageModifier; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface ChipV2SuffixImageIconConfig  差异内容：export interface ChipV2SuffixImageIconConfig | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2SuffixImageIconConfig；  API声明：action?: VoidCallback;  差异内容：action?: VoidCallback; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class ChipV2SuffixImageIcon  差异内容：export declare class ChipV2SuffixImageIcon | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2SuffixImageIcon；  API声明：@Trace  public accessibilityLevel?: string;  差异内容：@Trace  public accessibilityLevel?: string; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2SuffixImageIcon；  API声明：@Trace  public accessibilityText?: ResourceStr;  差异内容：@Trace  public accessibilityText?: ResourceStr; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2SuffixImageIcon；  API声明：@Trace  public accessibilityDescription?: ResourceStr;  差异内容：@Trace  public accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2SuffixImageIcon；  API声明：@Trace  public action?: VoidCallback;  差异内容：@Trace  public action?: VoidCallback; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export abstract class ChipV2Icon  差异内容：export abstract class ChipV2Icon | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface ChipV2PrefixImageIconConfig  差异内容：export interface ChipV2PrefixImageIconConfig | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class ChipV2PrefixImageIcon  差异内容：export declare class ChipV2PrefixImageIcon | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface ChipV2AccessibilityConfig  差异内容：export interface ChipV2AccessibilityConfig | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2AccessibilityConfig；  API声明：accessibilityLevel?: string;  差异内容：accessibilityLevel?: string; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2AccessibilityConfig；  API声明：accessibilityText?: ResourceStr;  差异内容：accessibilityText?: ResourceStr; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2AccessibilityConfig；  API声明：accessibilityDescription?: ResourceStr;  差异内容：accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class ChipV2Accessibility  差异内容：export declare class ChipV2Accessibility | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Accessibility；  API声明：@Trace  public accessibilityLevel?: string;  差异内容：@Trace  public accessibilityLevel?: string; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Accessibility；  API声明：@Trace  public accessibilityText?: ResourceStr;  差异内容：@Trace  public accessibilityText?: ResourceStr; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Accessibility；  API声明：@Trace  public accessibilityDescription?: ResourceStr;  差异内容：@Trace  public accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface ChipV2CloseConfig  差异内容：export interface ChipV2CloseConfig | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2CloseConfig；  API声明：fontSize?: LengthMetrics;  差异内容：fontSize?: LengthMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class ChipV2CloseIcon  差异内容：export declare class ChipV2CloseIcon | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2CloseIcon；  API声明：@Trace  public fontSize?: LengthMetrics;  差异内容：@Trace  public fontSize?: LengthMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface ChipV2SymbolIconConfig  差异内容：export interface ChipV2SymbolIconConfig | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2SymbolIconConfig；  API声明：normal?: SymbolGlyphModifier;  差异内容：normal?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2SymbolIconConfig；  API声明：activated?: SymbolGlyphModifier;  差异内容：activated?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export abstract class ChipV2SymbolIcon  差异内容：export abstract class ChipV2SymbolIcon | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2SymbolIcon；  API声明：@Trace  public normal?: SymbolGlyphModifier;  差异内容：@Trace  public normal?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2SymbolIcon；  API声明：@Trace  public activated?: SymbolGlyphModifier;  差异内容：@Trace  public activated?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface ChipV2PrefixSymbolIconConfig  差异内容：export interface ChipV2PrefixSymbolIconConfig | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class ChipV2PrefixSymbolIcon  差异内容：export declare class ChipV2PrefixSymbolIcon | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface ChipV2SuffixSymbolIconConfig  差异内容：export interface ChipV2SuffixSymbolIconConfig | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2SuffixSymbolIconConfig；  API声明：normalAccessibility?: ChipV2AccessibilityConfig;  差异内容：normalAccessibility?: ChipV2AccessibilityConfig; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2SuffixSymbolIconConfig；  API声明：activatedAccessibility?: ChipV2AccessibilityConfig;  差异内容：activatedAccessibility?: ChipV2AccessibilityConfig; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2SuffixSymbolIconConfig；  API声明：action?: VoidCallback;  差异内容：action?: VoidCallback; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class ChipV2SuffixSymbolIcon  差异内容：export declare class ChipV2SuffixSymbolIcon | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2SuffixSymbolIcon；  API声明：@Trace  public normalAccessibility?: ChipV2Accessibility;  差异内容：@Trace  public normalAccessibility?: ChipV2Accessibility; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2SuffixSymbolIcon；  API声明：@Trace  public activatedAccessibility?: ChipV2Accessibility;  差异内容：@Trace  public activatedAccessibility?: ChipV2Accessibility; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2SuffixSymbolIcon；  API声明：@Trace  public action?: VoidCallback;  差异内容：@Trace  public action?: VoidCallback; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface ChipV2LabelMarginConfig  差异内容：export interface ChipV2LabelMarginConfig | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2LabelMarginConfig；  API声明：left?: LengthMetrics;  差异内容：left?: LengthMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2LabelMarginConfig；  API声明：right?: LengthMetrics;  差异内容：right?: LengthMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface ChipV2LocalizedLabelMarginConfig  差异内容：export interface ChipV2LocalizedLabelMarginConfig | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2LocalizedLabelMarginConfig；  API声明：start?: LengthMetrics;  差异内容：start?: LengthMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2LocalizedLabelMarginConfig；  API声明：end?: LengthMetrics;  差异内容：end?: LengthMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface ChipV2LabelConfig  差异内容：export interface ChipV2LabelConfig | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2LabelConfig；  API声明：text: string;  差异内容：text: string; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2LabelConfig；  API声明：fontSize?: LengthMetrics;  差异内容：fontSize?: LengthMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2LabelConfig；  API声明：fontColor?: ColorMetrics;  差异内容：fontColor?: ColorMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2LabelConfig；  API声明：activatedFontColor?: ColorMetrics;  差异内容：activatedFontColor?: ColorMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2LabelConfig；  API声明：fontFamily?: string;  差异内容：fontFamily?: string; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2LabelConfig；  API声明：labelMargin?: ChipV2LabelMarginConfig;  差异内容：labelMargin?: ChipV2LabelMarginConfig; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2LabelConfig；  API声明：localizedLabelMargin?: ChipV2LocalizedLabelMarginConfig;  差异内容：localizedLabelMargin?: ChipV2LocalizedLabelMarginConfig; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2LabelConfig；  API声明：modifier?: TextModifier;  差异内容：modifier?: TextModifier; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class ChipV2Label  差异内容：export declare class ChipV2Label | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Label；  API声明：@Trace  public text: string;  差异内容：@Trace  public text: string; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Label；  API声明：@Trace  public fontSize?: LengthMetrics;  差异内容：@Trace  public fontSize?: LengthMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Label；  API声明：@Trace  public fontColor?: ColorMetrics;  差异内容：@Trace  public fontColor?: ColorMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Label；  API声明：@Trace  public activatedFontColor?: ColorMetrics;  差异内容：@Trace  public activatedFontColor?: ColorMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Label；  API声明：@Trace  public fontFamily?: string;  差异内容：@Trace  public fontFamily?: string; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Label；  API声明：@Trace  public labelMargin?: ChipV2LabelMarginConfig;  差异内容：@Trace  public labelMargin?: ChipV2LabelMarginConfig; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Label；  API声明：@Trace  public localizedLabelMargin?: ChipV2LocalizedLabelMarginConfig;  差异内容：@Trace  public localizedLabelMargin?: ChipV2LocalizedLabelMarginConfig; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Label；  API声明：@Trace  public modifier?: TextModifier;  差异内容：@Trace  public modifier?: TextModifier; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface IChipV2OptionsConfig  差异内容：export interface IChipV2OptionsConfig | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：label: ChipV2Label;  差异内容：label: ChipV2Label; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：prefixIcon?: ChipV2Icon;  差异内容：prefixIcon?: ChipV2Icon; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：suffixIcon?: ChipV2Icon;  差异内容：suffixIcon?: ChipV2Icon; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：allowClose?: boolean;  差异内容：allowClose?: boolean; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：closeIcon?: ChipV2CloseIcon;  差异内容：closeIcon?: ChipV2CloseIcon; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：enabled?: boolean;  差异内容：enabled?: boolean; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：activated?: boolean;  差异内容：activated?: boolean; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：backgroundColor?: ColorMetrics;  差异内容：backgroundColor?: ColorMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：activatedBackgroundColor?: ColorMetrics;  差异内容：activatedBackgroundColor?: ColorMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：borderRadius?: LengthMetrics;  差异内容：borderRadius?: LengthMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：size?: ChipV2Size | SizeT<LengthMetrics>;  差异内容：size?: ChipV2Size | SizeT<LengthMetrics>; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：direction?: Direction;  差异内容：direction?: Direction; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：accessibilityDescription?: ResourceStr;  差异内容：accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：accessibilityLevel?: string;  差异内容：accessibilityLevel?: string; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：accessibilitySelectedType?: ChipV2AccessibilitySelectedType;  差异内容：accessibilitySelectedType?: ChipV2AccessibilitySelectedType; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：maxFontScale?: number | Resource;  差异内容：maxFontScale?: number | Resource; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：minFontScale?: number | Resource;  差异内容：minFontScale?: number | Resource; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：padding?: LocalizedPadding;  差异内容：padding?: LocalizedPadding; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：fontSize?: LengthMetrics;  差异内容：fontSize?: LengthMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：backgroundSystemMaterial?: uiMaterial.Material;  差异内容：backgroundSystemMaterial?: uiMaterial.Material; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：activatedBackgroundSystemMaterial?: uiMaterial.Material;  差异内容：activatedBackgroundSystemMaterial?: uiMaterial.Material; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：onClose?: VoidCallback;  差异内容：onClose?: VoidCallback; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：IChipV2OptionsConfig；  API声明：onClicked?: Callback<void>;  差异内容：onClicked?: Callback<void>; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export class ChipV2Options  差异内容：export class ChipV2Options | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public label: ChipV2Label;  差异内容：@Trace  public label: ChipV2Label; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public prefixIcon?: ChipV2Icon;  差异内容：@Trace  public prefixIcon?: ChipV2Icon; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public suffixIcon?: ChipV2Icon;  差异内容：@Trace  public suffixIcon?: ChipV2Icon; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public allowClose?: boolean;  差异内容：@Trace  public allowClose?: boolean; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public closeIcon?: ChipV2CloseIcon;  差异内容：@Trace  public closeIcon?: ChipV2CloseIcon; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public enabled?: boolean;  差异内容：@Trace  public enabled?: boolean; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public activated?: boolean;  差异内容：@Trace  public activated?: boolean; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public backgroundColor?: ColorMetrics;  差异内容：@Trace  public backgroundColor?: ColorMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public activatedBackgroundColor?: ColorMetrics;  差异内容：@Trace  public activatedBackgroundColor?: ColorMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public borderRadius?: LengthMetrics;  差异内容：@Trace  public borderRadius?: LengthMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public size?: ChipV2Size | SizeT<LengthMetrics>;  差异内容：@Trace  public size?: ChipV2Size | SizeT<LengthMetrics>; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public direction?: Direction;  差异内容：@Trace  public direction?: Direction; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public accessibilityDescription?: ResourceStr;  差异内容：@Trace  public accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public accessibilityLevel?: string;  差异内容：@Trace  public accessibilityLevel?: string; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public accessibilitySelectedType?: ChipV2AccessibilitySelectedType;  差异内容：@Trace  public accessibilitySelectedType?: ChipV2AccessibilitySelectedType; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public maxFontScale?: number | Resource;  差异内容：@Trace  public maxFontScale?: number | Resource; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public minFontScale?: number | Resource;  差异内容：@Trace  public minFontScale?: number | Resource; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public padding?: LocalizedPadding;  差异内容：@Trace  public padding?: LocalizedPadding; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public fontSize?: LengthMetrics;  差异内容：@Trace  public fontSize?: LengthMetrics; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public backgroundSystemMaterial?: uiMaterial.Material;  差异内容：@Trace  public backgroundSystemMaterial?: uiMaterial.Material; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：@Trace  public activatedBackgroundSystemMaterial?: uiMaterial.Material;  差异内容：@Trace  public activatedBackgroundSystemMaterial?: uiMaterial.Material; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：public onClose?: VoidCallback;  差异内容：public onClose?: VoidCallback; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2Options；  API声明：public onClicked?: Callback<void>;  差异内容：public onClicked?: Callback<void>; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare struct ChipV2  差异内容：export declare struct ChipV2 | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2；  API声明：@Require  @Param  readonly chipV2Options: ChipV2Options;  差异内容：@Require  @Param  readonly chipV2Options: ChipV2Options; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：ChipV2；  API声明：build(): void;  差异内容：build(): void; | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare enum IconTypeV2  差异内容：export declare enum IconTypeV2 | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：IconTypeV2；  API声明：BADGE = 1  差异内容：BADGE = 1 | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：IconTypeV2；  API声明：NORMAL\_ICON = 2  差异内容：NORMAL\_ICON = 2 | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：IconTypeV2；  API声明：SYSTEM\_ICON = 3  差异内容：SYSTEM\_ICON = 3 | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：IconTypeV2；  API声明：HEAD\_SCULPTURE = 4  差异内容：HEAD\_SCULPTURE = 4 | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：IconTypeV2；  API声明：APP\_ICON = 5  差异内容：APP\_ICON = 5 | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：IconTypeV2；  API声明：PREVIEW = 6  差异内容：PREVIEW = 6 | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：IconTypeV2；  API声明：LONGITUDINAL = 7  差异内容：LONGITUDINAL = 7 | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：IconTypeV2；  API声明：VERTICAL = 8  差异内容：VERTICAL = 8 | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：global；  API声明：declare type OnActionCallback = () => void;  差异内容：declare type OnActionCallback = () => void; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：global；  API声明：declare type OnChangeCallback = (value: boolean) => void;  差异内容：declare type OnChangeCallback = (value: boolean) => void; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface OperateIconV2Options  差异内容：export interface OperateIconV2Options | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateIconV2Options；  API声明：value?: ResourceStr;  差异内容：value?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateIconV2Options；  API声明：symbolStyle?: SymbolGlyphModifier;  差异内容：symbolStyle?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateIconV2Options；  API声明：action?: OnActionCallback;  差异内容：action?: OnActionCallback; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateIconV2Options；  API声明：accessibilityText?: ResourceStr;  差异内容：accessibilityText?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateIconV2Options；  API声明：accessibilityDescription?: ResourceStr;  差异内容：accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateIconV2Options；  API声明：accessibilityLevel?: string;  差异内容：accessibilityLevel?: string; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class OperateIconV2  差异内容：export declare class OperateIconV2 | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateIconV2；  API声明：@Trace  public value: ResourceStr;  差异内容：@Trace  public value: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateIconV2；  API声明：@Trace  public symbolStyle?: SymbolGlyphModifier;  差异内容：@Trace  public symbolStyle?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateIconV2；  API声明：@Trace  public action?: OnActionCallback;  差异内容：@Trace  public action?: OnActionCallback; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateIconV2；  API声明：@Trace  public accessibilityText?: ResourceStr;  差异内容：@Trace  public accessibilityText?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateIconV2；  API声明：@Trace  public accessibilityDescription?: ResourceStr;  差异内容：@Trace  public accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateIconV2；  API声明：@Trace  public accessibilityLevel?: string;  差异内容：@Trace  public accessibilityLevel?: string; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface OperateCheckV2Options  差异内容：export interface OperateCheckV2Options | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateCheckV2Options；  API声明：isCheck?: boolean;  差异内容：isCheck?: boolean; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateCheckV2Options；  API声明：onChange?: OnChangeCallback;  差异内容：onChange?: OnChangeCallback; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateCheckV2Options；  API声明：accessibilityText?: ResourceStr;  差异内容：accessibilityText?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateCheckV2Options；  API声明：accessibilityDescription?: ResourceStr;  差异内容：accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateCheckV2Options；  API声明：accessibilityLevel?: string;  差异内容：accessibilityLevel?: string; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class OperateCheckV2  差异内容：export declare class OperateCheckV2 | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateCheckV2；  API声明：@Trace  public isCheck?: boolean;  差异内容：@Trace  public isCheck?: boolean; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateCheckV2；  API声明：@Trace  public onChange?: OnChangeCallback;  差异内容：@Trace  public onChange?: OnChangeCallback; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateCheckV2；  API声明：@Trace  public accessibilityText?: ResourceStr;  差异内容：@Trace  public accessibilityText?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateCheckV2；  API声明：@Trace  public accessibilityDescription?: ResourceStr;  差异内容：@Trace  public accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateCheckV2；  API声明：@Trace  public accessibilityLevel?: string;  差异内容：@Trace  public accessibilityLevel?: string; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface OperateButtonV2Options  差异内容：export interface OperateButtonV2Options | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateButtonV2Options；  API声明：text?: ResourceStr;  差异内容：text?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateButtonV2Options；  API声明：accessibilityText?: ResourceStr;  差异内容：accessibilityText?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateButtonV2Options；  API声明：accessibilityDescription?: ResourceStr;  差异内容：accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateButtonV2Options；  API声明：accessibilityLevel?: string;  差异内容：accessibilityLevel?: string; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class OperateButtonV2  差异内容：export declare class OperateButtonV2 | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateButtonV2；  API声明：@Trace  public text?: ResourceStr;  差异内容：@Trace  public text?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateButtonV2；  API声明：@Trace  public accessibilityText?: ResourceStr;  差异内容：@Trace  public accessibilityText?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateButtonV2；  API声明：@Trace  public accessibilityDescription?: ResourceStr;  差异内容：@Trace  public accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateButtonV2；  API声明：@Trace  public accessibilityLevel?: string;  差异内容：@Trace  public accessibilityLevel?: string; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface ContentItemV2Options  差异内容：export interface ContentItemV2Options | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：ContentItemV2Options；  API声明：iconStyle?: IconTypeV2;  差异内容：iconStyle?: IconTypeV2; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：ContentItemV2Options；  API声明：icon?: ResourceStr;  差异内容：icon?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：ContentItemV2Options；  API声明：symbolStyle?: SymbolGlyphModifier;  差异内容：symbolStyle?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：ContentItemV2Options；  API声明：primaryText?: ResourceStr;  差异内容：primaryText?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：ContentItemV2Options；  API声明：secondaryText?: ResourceStr;  差异内容：secondaryText?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：ContentItemV2Options；  API声明：description?: ResourceStr;  差异内容：description?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class ContentItemV2  差异内容：export declare class ContentItemV2 | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：ContentItemV2；  API声明：@Trace  public iconStyle?: IconTypeV2;  差异内容：@Trace  public iconStyle?: IconTypeV2; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：ContentItemV2；  API声明：@Trace  public icon?: ResourceStr;  差异内容：@Trace  public icon?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：ContentItemV2；  API声明：@Trace  public symbolStyle?: SymbolGlyphModifier;  差异内容：@Trace  public symbolStyle?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：ContentItemV2；  API声明：@Trace  public primaryText?: ResourceStr;  差异内容：@Trace  public primaryText?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：ContentItemV2；  API声明：@Trace  public secondaryText?: ResourceStr;  差异内容：@Trace  public secondaryText?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：ContentItemV2；  API声明：@Trace  public description?: ResourceStr;  差异内容：@Trace  public description?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface OperateItemV2Options  差异内容：export interface OperateItemV2Options | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateItemV2Options；  API声明：icon?: OperateIconV2;  差异内容：icon?: OperateIconV2; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateItemV2Options；  API声明：subIcon?: OperateIconV2;  差异内容：subIcon?: OperateIconV2; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateItemV2Options；  API声明：button?: OperateButtonV2;  差异内容：button?: OperateButtonV2; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateItemV2Options；  API声明：toggle?: OperateCheckV2;  差异内容：toggle?: OperateCheckV2; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateItemV2Options；  API声明：checkbox?: OperateCheckV2;  差异内容：checkbox?: OperateCheckV2; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateItemV2Options；  API声明：radio?: OperateCheckV2;  差异内容：radio?: OperateCheckV2; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateItemV2Options；  API声明：image?: ResourceStr;  差异内容：image?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateItemV2Options；  API声明：symbolStyle?: SymbolGlyphModifier;  差异内容：symbolStyle?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateItemV2Options；  API声明：text?: ResourceStr;  差异内容：text?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateItemV2Options；  API声明：arrow?: OperateIconV2;  差异内容：arrow?: OperateIconV2; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class OperateItemV2  差异内容：export declare class OperateItemV2 | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateItemV2；  API声明：@Trace  public icon?: OperateIconV2;  差异内容：@Trace  public icon?: OperateIconV2; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateItemV2；  API声明：@Trace  public subIcon?: OperateIconV2;  差异内容：@Trace  public subIcon?: OperateIconV2; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateItemV2；  API声明：@Trace  public button?: OperateButtonV2;  差异内容：@Trace  public button?: OperateButtonV2; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateItemV2；  API声明：@Trace  public toggle?: OperateCheckV2;  差异内容：@Trace  public toggle?: OperateCheckV2; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateItemV2；  API声明：@Trace  public checkbox?: OperateCheckV2;  差异内容：@Trace  public checkbox?: OperateCheckV2; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateItemV2；  API声明：@Trace  public radio?: OperateCheckV2;  差异内容：@Trace  public radio?: OperateCheckV2; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateItemV2；  API声明：@Trace  public image?: ResourceStr;  差异内容：@Trace  public image?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateItemV2；  API声明：@Trace  public symbolStyle?: SymbolGlyphModifier;  差异内容：@Trace  public symbolStyle?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateItemV2；  API声明：@Trace  public text?: ResourceStr;  差异内容：@Trace  public text?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：OperateItemV2；  API声明：@Trace  public arrow?: OperateIconV2;  差异内容：@Trace  public arrow?: OperateIconV2; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare struct ComposeListItemV2  差异内容：export declare struct ComposeListItemV2 | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：ComposeListItemV2；  API声明：@Param  contentItemV2?: ContentItemV2;  差异内容：@Param  contentItemV2?: ContentItemV2; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：ComposeListItemV2；  API声明：@Param  operateItemV2?: OperateItemV2;  差异内容：@Param  operateItemV2?: OperateItemV2; | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增API | NA | 类名：global；  API声明：declare type OnActionCallback = () => void;  差异内容：declare type OnActionCallback = () => void; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface ComposeTitleBarV2MenuItemParams  差异内容：export interface ComposeTitleBarV2MenuItemParams | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：ComposeTitleBarV2MenuItemParams；  API声明：value: ResourceStr;  差异内容：value: ResourceStr; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：ComposeTitleBarV2MenuItemParams；  API声明：symbolStyle?: SymbolGlyphModifier;  差异内容：symbolStyle?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：ComposeTitleBarV2MenuItemParams；  API声明：isEnabled?: boolean;  差异内容：isEnabled?: boolean; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：ComposeTitleBarV2MenuItemParams；  API声明：action?: OnActionCallback;  差异内容：action?: OnActionCallback; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：ComposeTitleBarV2MenuItemParams；  API声明：label?: ResourceStr;  差异内容：label?: ResourceStr; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：ComposeTitleBarV2MenuItemParams；  API声明：accessibilityText?: ResourceStr;  差异内容：accessibilityText?: ResourceStr; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：ComposeTitleBarV2MenuItemParams；  API声明：accessibilityLevel?: string;  差异内容：accessibilityLevel?: string; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：ComposeTitleBarV2MenuItemParams；  API声明：accessibilityDescription?: ResourceStr;  差异内容：accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class ComposeTitleBarV2MenuItem  差异内容：export declare class ComposeTitleBarV2MenuItem | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：ComposeTitleBarV2MenuItem；  API声明：@Trace  value: ResourceStr;  差异内容：@Trace  value: ResourceStr; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：ComposeTitleBarV2MenuItem；  API声明：@Trace  symbolStyle?: SymbolGlyphModifier;  差异内容：@Trace  symbolStyle?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：ComposeTitleBarV2MenuItem；  API声明：@Trace  isEnabled?: boolean;  差异内容：@Trace  isEnabled?: boolean; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：ComposeTitleBarV2MenuItem；  API声明：@Trace  action?: OnActionCallback;  差异内容：@Trace  action?: OnActionCallback; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：ComposeTitleBarV2MenuItem；  API声明：@Trace  label?: ResourceStr;  差异内容：@Trace  label?: ResourceStr; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：ComposeTitleBarV2MenuItem；  API声明：@Trace  accessibilityText?: ResourceStr;  差异内容：@Trace  accessibilityText?: ResourceStr; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：ComposeTitleBarV2MenuItem；  API声明：@Trace  accessibilityLevel?: string;  差异内容：@Trace  accessibilityLevel?: string; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：ComposeTitleBarV2MenuItem；  API声明：@Trace  accessibilityDescription?: ResourceStr;  差异内容：@Trace  accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare struct ComposeTitleBarV2  差异内容：export declare struct ComposeTitleBarV2 | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：ComposeTitleBarV2；  API声明：@Param  item?: ComposeTitleBarV2MenuItem;  差异内容：@Param  item?: ComposeTitleBarV2MenuItem; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：ComposeTitleBarV2；  API声明：@Param  title: ResourceStr;  差异内容：@Param  title: ResourceStr; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：ComposeTitleBarV2；  API声明：@Param  subtitle?: ResourceStr;  差异内容：@Param  subtitle?: ResourceStr; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：ComposeTitleBarV2；  API声明：@Param  menuItems?: Array<ComposeTitleBarV2MenuItem>;  差异内容：@Param  menuItems?: Array<ComposeTitleBarV2MenuItem>; | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增API | NA | 类名：global；  API声明：declare enum CounterV2Type  差异内容：declare enum CounterV2Type | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2Type；  API声明：LIST = 0  差异内容：LIST = 0 | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2Type；  API声明：COMPACT = 1  差异内容：COMPACT = 1 | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2Type；  API声明：INLINE = 2  差异内容：INLINE = 2 | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2Type；  API声明：INLINE\_DATE = 3  差异内容：INLINE\_DATE = 3 | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export type OnCounterV2HoverCallback = (isHover: boolean) => void;  差异内容：export type OnCounterV2HoverCallback = (isHover: boolean) => void; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：global；  API声明：declare class CounterV2CommonOptions  差异内容：declare class CounterV2CommonOptions | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2CommonOptions；  API声明：focusable?: boolean;  差异内容：focusable?: boolean; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2CommonOptions；  API声明：step?: number;  差异内容：step?: number; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2CommonOptions；  API声明：onHoverIncrease?: OnCounterV2HoverCallback;  差异内容：onHoverIncrease?: OnCounterV2HoverCallback; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2CommonOptions；  API声明：onHoverDecrease?: OnCounterV2HoverCallback;  差异内容：onHoverDecrease?: OnCounterV2HoverCallback; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export type OnInlineCounterV2Change = (value: number) => void;  差异内容：export type OnInlineCounterV2Change = (value: number) => void; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：global；  API声明：declare class CounterV2InlineStyleOptions  差异内容：declare class CounterV2InlineStyleOptions | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2InlineStyleOptions；  API声明：value?: number;  差异内容：value?: number; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2InlineStyleOptions；  API声明：min?: number;  差异内容：min?: number; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2InlineStyleOptions；  API声明：max?: number;  差异内容：max?: number; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2InlineStyleOptions；  API声明：textWidth?: number;  差异内容：textWidth?: number; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2InlineStyleOptions；  API声明：onChange?: OnInlineCounterV2Change;  差异内容：onChange?: OnInlineCounterV2Change; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：global；  API声明：declare class CounterV2NumberStyleOptions  差异内容：declare class CounterV2NumberStyleOptions | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2NumberStyleOptions；  API声明：label?: ResourceStr;  差异内容：label?: ResourceStr; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2NumberStyleOptions；  API声明：onFocusIncrease?: VoidCallback;  差异内容：onFocusIncrease?: VoidCallback; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2NumberStyleOptions；  API声明：onFocusDecrease?: VoidCallback;  差异内容：onFocusDecrease?: VoidCallback; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2NumberStyleOptions；  API声明：onBlurIncrease?: VoidCallback;  差异内容：onBlurIncrease?: VoidCallback; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2NumberStyleOptions；  API声明：onBlurDecrease?: VoidCallback;  差异内容：onBlurDecrease?: VoidCallback; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：global；  API声明：declare class CounterV2DateData  差异内容：declare class CounterV2DateData | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2DateData；  API声明：year: number;  差异内容：year: number; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2DateData；  API声明：month: number;  差异内容：month: number; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2DateData；  API声明：day: number;  差异内容：day: number; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2DateData；  API声明：toString(): string;  差异内容：toString(): string; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export type OnDateCounterV2ChangeCallback = (date: CounterV2DateData) => void;  差异内容：export type OnDateCounterV2ChangeCallback = (date: CounterV2DateData) => void; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：global；  API声明：declare class CounterV2DateStyleOptions  差异内容：declare class CounterV2DateStyleOptions | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2DateStyleOptions；  API声明：year?: number;  差异内容：year?: number; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2DateStyleOptions；  API声明：month?: number;  差异内容：month?: number; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2DateStyleOptions；  API声明：day?: number;  差异内容：day?: number; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2DateStyleOptions；  API声明：onDateChange?: OnDateCounterV2ChangeCallback;  差异内容：onDateChange?: OnDateCounterV2ChangeCallback; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：global；  API声明：declare class CounterV2Options  差异内容：declare class CounterV2Options | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2Options；  API声明：type: CounterV2Type;  差异内容：type: CounterV2Type; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2Options；  API声明：numberOptions?: CounterV2NumberStyleOptions;  差异内容：numberOptions?: CounterV2NumberStyleOptions; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2Options；  API声明：inlineOptions?: CounterV2InlineStyleOptions;  差异内容：inlineOptions?: CounterV2InlineStyleOptions; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2Options；  API声明：dateOptions?: CounterV2DateStyleOptions;  差异内容：dateOptions?: CounterV2DateStyleOptions; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2Options；  API声明：direction?: Direction;  差异内容：direction?: Direction; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：global；  API声明：declare struct CounterV2Component  差异内容：declare struct CounterV2Component | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：CounterV2Component；  API声明：@Param  options: CounterV2Options;  差异内容：@Param  options: CounterV2Options; | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare enum DateMode  差异内容：export declare enum DateMode | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：DateMode；  API声明：DATE = 0  差异内容：DATE = 0 | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：DateMode；  API声明：YEAR\_AND\_MONTH = 1  差异内容：YEAR\_AND\_MONTH = 1 | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：DateMode；  API声明：MONTH\_AND\_DAY = 2  差异内容：MONTH\_AND\_DAY = 2 | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare enum DisplayMode  差异内容：export declare enum DisplayMode | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：DisplayMode；  API声明：DATE = 0  差异内容：DATE = 0 | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：DisplayMode；  API声明：TIME = 1  差异内容：TIME = 1 | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：DisplayMode；  API声明：DATE\_TIME = 2  差异内容：DATE\_TIME = 2 | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class DatePickerComponentResult  差异内容：export declare class DatePickerComponentResult | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：DatePickerComponentResult；  API声明：year?: number;  差异内容：year?: number; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：DatePickerComponentResult；  API声明：month?: number;  差异内容：month?: number; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：DatePickerComponentResult；  API声明：day?: number;  差异内容：day?: number; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：DatePickerComponentResult；  API声明：hour?: number;  差异内容：hour?: number; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：DatePickerComponentResult；  API声明：minute?: number;  差异内容：minute?: number; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：DatePickerComponentResult；  API声明：second?: number;  差异内容：second?: number; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare enum TimeFormat  差异内容：export declare enum TimeFormat | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：TimeFormat；  API声明：HOUR\_MINUTE = 0  差异内容：HOUR\_MINUTE = 0 | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：TimeFormat；  API声明：HOUR\_MINUTE\_SECOND = 1  差异内容：HOUR\_MINUTE\_SECOND = 1 | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class CommonOptions  差异内容：export declare class CommonOptions | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：CommonOptions；  API声明：start?: Date;  差异内容：start?: Date; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：CommonOptions；  API声明：end?: Date;  差异内容：end?: Date; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：CommonOptions；  API声明：selected?: Date;  差异内容：selected?: Date; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：CommonOptions；  API声明：loop?: boolean;  差异内容：loop?: boolean; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：CommonOptions；  API声明：onChange?: Callback<DatePickerComponentResult>;  差异内容：onChange?: Callback<DatePickerComponentResult>; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：CommonOptions；  API声明：onScrollStop?: Callback<DatePickerComponentResult>;  差异内容：onScrollStop?: Callback<DatePickerComponentResult>; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：CommonOptions；  API声明：enableHapticFeedback?: boolean;  差异内容：enableHapticFeedback?: boolean; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class DateOptions  差异内容：export declare class DateOptions | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：DateOptions；  API声明：mode?: DateMode;  差异内容：mode?: DateMode; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：DateOptions；  API声明：lunar?: boolean;  差异内容：lunar?: boolean; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class TimeOptions  差异内容：export declare class TimeOptions | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：TimeOptions；  API声明：format?: TimeFormat;  差异内容：format?: TimeFormat; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：TimeOptions；  API声明：useMilitaryTime?: boolean;  差异内容：useMilitaryTime?: boolean; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class DatePickerComponentOptions  差异内容：export declare class DatePickerComponentOptions | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：DatePickerComponentOptions；  API声明：displayMode?: DisplayMode;  差异内容：displayMode?: DisplayMode; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：DatePickerComponentOptions；  API声明：dateOptions?: DateOptions;  差异内容：dateOptions?: DateOptions; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：DatePickerComponentOptions；  API声明：timeOptions?: TimeOptions;  差异内容：timeOptions?: TimeOptions; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare struct DatePickerComponent  差异内容：export declare struct DatePickerComponent | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：DatePickerComponent；  API声明：@Prop  options: DatePickerComponentOptions;  差异内容：@Prop  options: DatePickerComponentOptions; | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：declare type OnActionCallback = () => void;  差异内容：declare type OnActionCallback = () => void; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare enum EditableLeftIconTypeV2  差异内容：export declare enum EditableLeftIconTypeV2 | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableLeftIconTypeV2；  API声明：Back = 0  差异内容：Back = 0 | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableLeftIconTypeV2；  API声明：Cancel = 1  差异内容：Cancel = 1 | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface EditableLeftIconV2Options  差异内容：export declare interface EditableLeftIconV2Options | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableLeftIconV2Options；  API声明：iconType?: EditableLeftIconTypeV2;  差异内容：iconType?: EditableLeftIconTypeV2; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableLeftIconV2Options；  API声明：defaultFocus?: boolean;  差异内容：defaultFocus?: boolean; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableLeftIconV2Options；  API声明：onAction?: OnActionCallback;  差异内容：onAction?: OnActionCallback; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class EditableLeftIconV2  差异内容：export declare class EditableLeftIconV2 | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableLeftIconV2；  API声明：@Trace  public iconType: EditableLeftIconTypeV2;  差异内容：@Trace  public iconType: EditableLeftIconTypeV2; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableLeftIconV2；  API声明：@Trace  public defaultFocus: boolean;  差异内容：@Trace  public defaultFocus: boolean; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableLeftIconV2；  API声明：@Trace  public onAction?: OnActionCallback;  差异内容：@Trace  public onAction?: OnActionCallback; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface EditableTitleV2Options  差异内容：export declare interface EditableTitleV2Options | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleV2Options；  API声明：mainTitle?: ResourceStr;  差异内容：mainTitle?: ResourceStr; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleV2Options；  API声明：subTitle?: ResourceStr;  差异内容：subTitle?: ResourceStr; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class EditableTitleV2  差异内容：export declare class EditableTitleV2 | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleV2；  API声明：@Trace  public mainTitle: ResourceStr;  差异内容：@Trace  public mainTitle: ResourceStr; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleV2；  API声明：@Trace  public subTitle?: ResourceStr;  差异内容：@Trace  public subTitle?: ResourceStr; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface EditableTitleBarMenuItemV2Options  差异内容：export declare interface EditableTitleBarMenuItemV2Options | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItemV2Options；  API声明：value?: ResourceStr;  差异内容：value?: ResourceStr; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItemV2Options；  API声明：symbolStyle?: SymbolGlyphModifier;  差异内容：symbolStyle?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItemV2Options；  API声明：isEnabled?: boolean;  差异内容：isEnabled?: boolean; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItemV2Options；  API声明：label?: ResourceStr;  差异内容：label?: ResourceStr; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItemV2Options；  API声明：action?: OnActionCallback;  差异内容：action?: OnActionCallback; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItemV2Options；  API声明：accessibilityLevel?: string;  差异内容：accessibilityLevel?: string; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItemV2Options；  API声明：accessibilityText?: ResourceStr;  差异内容：accessibilityText?: ResourceStr; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItemV2Options；  API声明：accessibilityDescription?: ResourceStr;  差异内容：accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItemV2Options；  API声明：defaultFocus?: boolean;  差异内容：defaultFocus?: boolean; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class EditableTitleBarMenuItemV2  差异内容：export declare class EditableTitleBarMenuItemV2 | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItemV2；  API声明：@Trace  public value: ResourceStr;  差异内容：@Trace  public value: ResourceStr; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItemV2；  API声明：@Trace  public symbolStyle?: SymbolGlyphModifier;  差异内容：@Trace  public symbolStyle?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItemV2；  API声明：@Trace  public isEnabled: boolean;  差异内容：@Trace  public isEnabled: boolean; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItemV2；  API声明：@Trace  public label?: ResourceStr;  差异内容：@Trace  public label?: ResourceStr; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItemV2；  API声明：@Trace  public action?: OnActionCallback;  差异内容：@Trace  public action?: OnActionCallback; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItemV2；  API声明：@Trace  public accessibilityLevel: string;  差异内容：@Trace  public accessibilityLevel: string; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItemV2；  API声明：@Trace  public accessibilityText?: ResourceStr;  差异内容：@Trace  public accessibilityText?: ResourceStr; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItemV2；  API声明：@Trace  public accessibilityDescription?: ResourceStr;  差异内容：@Trace  public accessibilityDescription?: ResourceStr; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItemV2；  API声明：@Trace  public defaultFocus: boolean;  差异内容：@Trace  public defaultFocus: boolean; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export type EditableTitleBarItemV2 = EditableTitleBarMenuItemV2;  差异内容：export type EditableTitleBarItemV2 = EditableTitleBarMenuItemV2; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export type EditableTitleBarItemV2Options = EditableTitleBarMenuItemV2Options;  差异内容：export type EditableTitleBarItemV2Options = EditableTitleBarMenuItemV2Options; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface EditableSaveButtonV2Options  差异内容：export declare interface EditableSaveButtonV2Options | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableSaveButtonV2Options；  API声明：isRequired?: boolean;  差异内容：isRequired?: boolean; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableSaveButtonV2Options；  API声明：defaultFocus?: boolean;  差异内容：defaultFocus?: boolean; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableSaveButtonV2Options；  API声明：onAction?: OnActionCallback;  差异内容：onAction?: OnActionCallback; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class EditableSaveButtonV2  差异内容：export declare class EditableSaveButtonV2 | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableSaveButtonV2；  API声明：@Trace  public isRequired: boolean;  差异内容：@Trace  public isRequired: boolean; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableSaveButtonV2；  API声明：@Trace  public defaultFocus: boolean;  差异内容：@Trace  public defaultFocus: boolean; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableSaveButtonV2；  API声明：@Trace  public onAction?: OnActionCallback;  差异内容：@Trace  public onAction?: OnActionCallback; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface EditableTitleBarStyleV2Options  差异内容：export declare interface EditableTitleBarStyleV2Options | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarStyleV2Options；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarStyleV2Options；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarStyleV2Options；  API声明：safeAreaTypes?: Array<SafeAreaType>;  差异内容：safeAreaTypes?: Array<SafeAreaType>; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarStyleV2Options；  API声明：safeAreaEdges?: Array<SafeAreaEdge>;  差异内容：safeAreaEdges?: Array<SafeAreaEdge>; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarStyleV2Options；  API声明：contentMargin?: LocalizedMargin;  差异内容：contentMargin?: LocalizedMargin; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class EditableTitleBarStyleV2  差异内容：export declare class EditableTitleBarStyleV2 | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarStyleV2；  API声明：@Trace  public backgroundColor?: ResourceColor;  差异内容：@Trace  public backgroundColor?: ResourceColor; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarStyleV2；  API声明：@Trace  public backgroundBlurStyle?: BlurStyle;  差异内容：@Trace  public backgroundBlurStyle?: BlurStyle; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarStyleV2；  API声明：@Trace  public safeAreaTypes?: Array<SafeAreaType>;  差异内容：@Trace  public safeAreaTypes?: Array<SafeAreaType>; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarStyleV2；  API声明：@Trace  public safeAreaEdges?: Array<SafeAreaEdge>;  差异内容：@Trace  public safeAreaEdges?: Array<SafeAreaEdge>; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarStyleV2；  API声明：@Trace  public contentMargin?: LocalizedMargin;  差异内容：@Trace  public contentMargin?: LocalizedMargin; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare struct EditableTitleBarV2  差异内容：export declare struct EditableTitleBarV2 | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarV2；  API声明：@Param  leftIcon?: EditableLeftIconV2;  差异内容：@Param  leftIcon?: EditableLeftIconV2; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarV2；  API声明：@Param  title: ResourceStr | EditableTitleV2;  差异内容：@Param  title: ResourceStr | EditableTitleV2; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarV2；  API声明：@Param  imageItem?: EditableTitleBarItemV2;  差异内容：@Param  imageItem?: EditableTitleBarItemV2; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarV2；  API声明：@Param  menuItems?: Array<EditableTitleBarMenuItemV2>;  差异内容：@Param  menuItems?: Array<EditableTitleBarMenuItemV2>; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarV2；  API声明：@Param  saveButton?: EditableSaveButtonV2;  差异内容：@Param  saveButton?: EditableSaveButtonV2; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：EditableTitleBarV2；  API声明：@Param  options: EditableTitleBarStyleV2;  差异内容：@Param  options: EditableTitleBarStyleV2; | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare enum MarginTypeV2  差异内容：export declare enum MarginTypeV2 | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：MarginTypeV2；  API声明：DEFAULT\_MARGIN = 0  差异内容：DEFAULT\_MARGIN = 0 | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：MarginTypeV2；  API声明：FIT\_MARGIN = 1  差异内容：FIT\_MARGIN = 1 | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface PromptOptionsV2Config  差异内容：export interface PromptOptionsV2Config | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：PromptOptionsV2Config；  API声明：marginType: MarginTypeV2;  差异内容：marginType: MarginTypeV2; | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：PromptOptionsV2Config；  API声明：marginTop: Dimension;  差异内容：marginTop: Dimension; | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：PromptOptionsV2Config；  API声明：icon?: ResourceStr;  差异内容：icon?: ResourceStr; | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：PromptOptionsV2Config；  API声明：symbolStyle?: SymbolGlyphModifier;  差异内容：symbolStyle?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：PromptOptionsV2Config；  API声明：tip?: ResourceStr;  差异内容：tip?: ResourceStr; | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：PromptOptionsV2Config；  API声明：actionText?: ResourceStr;  差异内容：actionText?: ResourceStr; | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：PromptOptionsV2Config；  API声明：isShown?: boolean;  差异内容：isShown?: boolean; | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class PromptOptionsV2  差异内容：export declare class PromptOptionsV2 | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：PromptOptionsV2；  API声明：@Trace  icon?: ResourceStr;  差异内容：@Trace  icon?: ResourceStr; | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：PromptOptionsV2；  API声明：@Trace  symbolStyle?: SymbolGlyphModifier;  差异内容：@Trace  symbolStyle?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：PromptOptionsV2；  API声明：@Trace  tip?: ResourceStr;  差异内容：@Trace  tip?: ResourceStr; | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：PromptOptionsV2；  API声明：@Trace  marginType: MarginTypeV2;  差异内容：@Trace  marginType: MarginTypeV2; | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：PromptOptionsV2；  API声明：@Trace  actionText?: ResourceStr;  差异内容：@Trace  actionText?: ResourceStr; | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：PromptOptionsV2；  API声明：@Trace  marginTop: Dimension;  差异内容：@Trace  marginTop: Dimension; | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：PromptOptionsV2；  API声明：@Trace  isShown?: boolean;  差异内容：@Trace  isShown?: boolean; | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：global；  API声明：declare type OnTipClickCallback = () => void;  差异内容：declare type OnTipClickCallback = () => void; | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：global；  API声明：declare type OnActionTextClickCallback = () => void;  差异内容：declare type OnActionTextClickCallback = () => void; | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare struct ExceptionPromptV2  差异内容：export declare struct ExceptionPromptV2 | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：ExceptionPromptV2；  API声明：@Param  options: PromptOptionsV2;  差异内容：@Param  options: PromptOptionsV2; | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：ExceptionPromptV2；  API声明：@Event  onTipClick?: OnTipClickCallback;  差异内容：@Event  onTipClick?: OnTipClickCallback; | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：ExceptionPromptV2；  API声明：@Event  onActionTextClick?: OnActionTextClickCallback;  差异内容：@Event  onActionTextClick?: OnActionTextClickCallback; | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare struct SwipeRefresherV2  差异内容：export declare struct SwipeRefresherV2 | api/@ohos.arkui.advanced.SwipeRefresherV2.d.ets |
| 新增API | NA | 类名：SwipeRefresherV2；  API声明：@Param  content?: string;  差异内容：@Param  content?: string; | api/@ohos.arkui.advanced.SwipeRefresherV2.d.ets |
| 新增API | NA | 类名：SwipeRefresherV2；  API声明：@Require  @Param  isLoading: boolean;  差异内容：@Require  @Param  isLoading: boolean; | api/@ohos.arkui.advanced.SwipeRefresherV2.d.ets |
| 新增API | NA | 类名：global；  API声明：declare type OnChangedCallback = (callbackParam: CallbackParamV2) => void;  差异内容：declare type OnChangedCallback = (callbackParam: CallbackParamV2) => void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class TreeListenerV2  差异内容：export declare class TreeListenerV2 | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeListenerV2；  API声明：onNodeClick(callback: OnChangedCallback): void;  差异内容：onNodeClick(callback: OnChangedCallback): void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeListenerV2；  API声明：onceNodeClick(callback: OnChangedCallback): void;  差异内容：onceNodeClick(callback: OnChangedCallback): void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeListenerV2；  API声明：offNodeClick(callback?: OnChangedCallback): void;  差异内容：offNodeClick(callback?: OnChangedCallback): void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeListenerV2；  API声明：onNodeAdd(callback: OnChangedCallback): void;  差异内容：onNodeAdd(callback: OnChangedCallback): void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeListenerV2；  API声明：onceNodeAdd(callback: OnChangedCallback): void;  差异内容：onceNodeAdd(callback: OnChangedCallback): void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeListenerV2；  API声明：offNodeAdd(callback?: OnChangedCallback): void;  差异内容：offNodeAdd(callback?: OnChangedCallback): void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeListenerV2；  API声明：onNodeDelete(callback: OnChangedCallback): void;  差异内容：onNodeDelete(callback: OnChangedCallback): void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeListenerV2；  API声明：onceNodeDelete(callback: OnChangedCallback): void;  差异内容：onceNodeDelete(callback: OnChangedCallback): void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeListenerV2；  API声明：offNodeDelete(callback?: OnChangedCallback): void;  差异内容：offNodeDelete(callback?: OnChangedCallback): void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeListenerV2；  API声明：onNodeModify(callback: OnChangedCallback): void;  差异内容：onNodeModify(callback: OnChangedCallback): void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeListenerV2；  API声明：onceNodeModify(callback: OnChangedCallback): void;  差异内容：onceNodeModify(callback: OnChangedCallback): void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeListenerV2；  API声明：offNodeModify(callback?: OnChangedCallback): void;  差异内容：offNodeModify(callback?: OnChangedCallback): void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeListenerV2；  API声明：onNodeMove(callback: OnChangedCallback): void;  差异内容：onNodeMove(callback: OnChangedCallback): void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeListenerV2；  API声明：onceNodeMove(callback: OnChangedCallback): void;  差异内容：onceNodeMove(callback: OnChangedCallback): void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeListenerV2；  API声明：offNodeMove(callback?: OnChangedCallback): void;  差异内容：offNodeMove(callback?: OnChangedCallback): void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class TreeListenerManagerV2  差异内容：export declare class TreeListenerManagerV2 | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeListenerManagerV2；  API声明：static getInstance(): TreeListenerManagerV2;  差异内容：static getInstance(): TreeListenerManagerV2; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeListenerManagerV2；  API声明：getTreeListener(): TreeListenerV2;  差异内容：getTreeListener(): TreeListenerV2; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare struct TreeViewV2  差异内容：export declare struct TreeViewV2 | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeViewV2；  API声明：@Param  treeControllerV2: TreeControllerV2;  差异内容：@Param  treeControllerV2: TreeControllerV2; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface CallbackParamV2  差异内容：export interface CallbackParamV2 | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：CallbackParamV2；  API声明：currentNodeId: number;  差异内容：currentNodeId: number; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：CallbackParamV2；  API声明：parentNodeId?: number;  差异内容：parentNodeId?: number; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：CallbackParamV2；  API声明：childIndex?: number;  差异内容：childIndex?: number; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：global；  API声明：declare type OnContainerCallback = () => void;  差异内容：declare type OnContainerCallback = () => void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface NodeParamV2  差异内容：export interface NodeParamV2 | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：NodeParamV2；  API声明：parentNodeId?: number;  差异内容：parentNodeId?: number; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：NodeParamV2；  API声明：currentNodeId?: number;  差异内容：currentNodeId?: number; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：NodeParamV2；  API声明：isFolder?: boolean;  差异内容：isFolder?: boolean; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：NodeParamV2；  API声明：icon?: ResourceStr;  差异内容：icon?: ResourceStr; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：NodeParamV2；  API声明：symbolIconStyle?: SymbolGlyphModifier;  差异内容：symbolIconStyle?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：NodeParamV2；  API声明：selectedIcon?: ResourceStr;  差异内容：selectedIcon?: ResourceStr; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：NodeParamV2；  API声明：symbolSelectedIconStyle?: SymbolGlyphModifier;  差异内容：symbolSelectedIconStyle?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：NodeParamV2；  API声明：editIcon?: ResourceStr;  差异内容：editIcon?: ResourceStr; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：NodeParamV2；  API声明：symbolEditIconStyle?: SymbolGlyphModifier;  差异内容：symbolEditIconStyle?: SymbolGlyphModifier; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：NodeParamV2；  API声明：primaryTitle?: ResourceStr;  差异内容：primaryTitle?: ResourceStr; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：NodeParamV2；  API声明：secondaryTitle?: ResourceStr;  差异内容：secondaryTitle?: ResourceStr; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：NodeParamV2；  API声明：container?: OnContainerCallback;  差异内容：container?: OnContainerCallback; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class TreeControllerV2  差异内容：export declare class TreeControllerV2 | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeControllerV2；  API声明：removeNode(): void;  差异内容：removeNode(): void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeControllerV2；  API声明：modifyNode(): void;  差异内容：modifyNode(): void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeControllerV2；  API声明：addNode(nodeParam?: NodeParamV2): TreeControllerV2;  差异内容：addNode(nodeParam?: NodeParamV2): TreeControllerV2; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeControllerV2；  API声明：refreshNode(parentId: number, parentSubTitle: ResourceStr, currentSubtitle: ResourceStr): void;  差异内容：refreshNode(parentId: number, parentSubTitle: ResourceStr, currentSubtitle: ResourceStr): void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：TreeControllerV2；  API声明：buildDone(): void;  差异内容：buildDone(): void; | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface LazyColumnLayoutInterface  差异内容：export interface LazyColumnLayoutInterface | api/@ohos.arkui.components.ArkLazyColumnLayout.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare class LazyColumnLayoutAttribute  差异内容：export declare class LazyColumnLayoutAttribute | api/@ohos.arkui.components.ArkLazyColumnLayout.d.ts |
| 新增API | NA | 类名：LazyColumnLayoutAttribute；  API声明：space(space: LengthMetrics | undefined): LazyColumnLayoutAttribute;  差异内容：space(space: LengthMetrics | undefined): LazyColumnLayoutAttribute; | api/@ohos.arkui.components.ArkLazyColumnLayout.d.ts |
| 新增API | NA | 类名：LazyColumnLayoutAttribute；  API声明：alignItems(value: HorizontalAlign | undefined): LazyColumnLayoutAttribute;  差异内容：alignItems(value: HorizontalAlign | undefined): LazyColumnLayoutAttribute; | api/@ohos.arkui.components.ArkLazyColumnLayout.d.ts |
| 新增API | NA | 类名：LazyColumnLayoutAttribute；  API声明：header(builder: CustomBuilder | undefined): LazyColumnLayoutAttribute;  差异内容：header(builder: CustomBuilder | undefined): LazyColumnLayoutAttribute; | api/@ohos.arkui.components.ArkLazyColumnLayout.d.ts |
| 新增API | NA | 类名：LazyColumnLayoutAttribute；  API声明：footer(builder: CustomBuilder | undefined): LazyColumnLayoutAttribute;  差异内容：footer(builder: CustomBuilder | undefined): LazyColumnLayoutAttribute; | api/@ohos.arkui.components.ArkLazyColumnLayout.d.ts |
| 新增API | NA | 类名：LazyColumnLayoutAttribute；  API声明：sticky(sticky: StickyStyle | undefined): LazyColumnLayoutAttribute;  差异内容：sticky(sticky: StickyStyle | undefined): LazyColumnLayoutAttribute; | api/@ohos.arkui.components.ArkLazyColumnLayout.d.ts |
| 新增API | NA | 类名：LazyColumnLayoutAttribute；  API声明：onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): LazyColumnLayoutAttribute;  差异内容：onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): LazyColumnLayoutAttribute; | api/@ohos.arkui.components.ArkLazyColumnLayout.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare const LazyColumnLayout: LazyColumnLayoutInterface;  差异内容：export declare const LazyColumnLayout: LazyColumnLayoutInterface; | api/@ohos.arkui.components.ArkLazyColumnLayout.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare const LazyColumnLayoutInstance: LazyColumnLayoutAttribute;  差异内容：export declare const LazyColumnLayoutInstance: LazyColumnLayoutAttribute; | api/@ohos.arkui.components.ArkLazyColumnLayout.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare class LazyDynamicLayoutAttribute  差异内容：export declare class LazyDynamicLayoutAttribute | api/@ohos.arkui.components.ArkLazyDynamicLayout.d.ts |
| 新增API | NA | 类名：LazyDynamicLayoutAttribute；  API声明：onVisibleIndexesChange(callback: Callback<number[]> | undefined): LazyDynamicLayoutAttribute;  差异内容：onVisibleIndexesChange(callback: Callback<number[]> | undefined): LazyDynamicLayoutAttribute; | api/@ohos.arkui.components.ArkLazyDynamicLayout.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare function LazyDynamicLayout(algorithm: LazyLayoutAlgorithm): LazyDynamicLayoutAttribute;  差异内容：export declare function LazyDynamicLayout(algorithm: LazyLayoutAlgorithm): LazyDynamicLayoutAttribute; | api/@ohos.arkui.components.ArkLazyDynamicLayout.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare const LazyDynamicLayoutInstance: LazyDynamicLayoutAttribute;  差异内容：export declare const LazyDynamicLayoutInstance: LazyDynamicLayoutAttribute; | api/@ohos.arkui.components.ArkLazyDynamicLayout.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare enum SelectionContainerTextJoinStyle  差异内容：export declare enum SelectionContainerTextJoinStyle | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerTextJoinStyle；  API声明：NEWLINE = 0  差异内容：NEWLINE = 0 | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerTextJoinStyle；  API声明：DIRECT = 1  差异内容：DIRECT = 1 | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface SelectionContainerMenuOptions  差异内容：export interface SelectionContainerMenuOptions | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerMenuOptions；  API声明：onAppear?: Callback<string>;  差异内容：onAppear?: Callback<string>; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerMenuOptions；  API声明：onDisappear?: Callback<void>;  差异内容：onDisappear?: Callback<void>; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerMenuOptions；  API声明：onMenuShow?: Callback<string>;  差异内容：onMenuShow?: Callback<string>; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerMenuOptions；  API声明：onMenuHide?: Callback<string>;  差异内容：onMenuHide?: Callback<string>; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：global；  API声明：export type OnMenuItemClickWithTextCallback = (menuItem: TextMenuItem, value: string) => boolean;  差异内容：export type OnMenuItemClickWithTextCallback = (menuItem: TextMenuItem, value: string) => boolean; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface SelectionContainerEditMenuOptions  差异内容：export interface SelectionContainerEditMenuOptions | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerEditMenuOptions；  API声明：onCreateMenu?: OnCreateMenuCallback;  差异内容：onCreateMenu?: OnCreateMenuCallback; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerEditMenuOptions；  API声明：onMenuItemClick?: OnMenuItemClickWithTextCallback;  差异内容：onMenuItemClick?: OnMenuItemClickWithTextCallback; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerEditMenuOptions；  API声明：onPrepareMenu?: OnPrepareMenuCallback;  差异内容：onPrepareMenu?: OnPrepareMenuCallback; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface SelectionContainerInterface  差异内容：export interface SelectionContainerInterface | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare class SelectionContainerAttribute  差异内容：export declare class SelectionContainerAttribute | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerAttribute；  API声明：copyOption(value: Optional<CopyOptions>): SelectionContainerAttribute;  差异内容：copyOption(value: Optional<CopyOptions>): SelectionContainerAttribute; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerAttribute；  API声明：caretColor(color: Optional<ResourceColor>): SelectionContainerAttribute;  差异内容：caretColor(color: Optional<ResourceColor>): SelectionContainerAttribute; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerAttribute；  API声明：selectedBackgroundColor(color: Optional<ResourceColor>): SelectionContainerAttribute;  差异内容：selectedBackgroundColor(color: Optional<ResourceColor>): SelectionContainerAttribute; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerAttribute；  API声明：enableHapticFeedback(isEnabled: Optional<boolean>): SelectionContainerAttribute;  差异内容：enableHapticFeedback(isEnabled: Optional<boolean>): SelectionContainerAttribute; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerAttribute；  API声明：textJoinStyle(style: Optional<SelectionContainerTextJoinStyle>): SelectionContainerAttribute;  差异内容：textJoinStyle(style: Optional<SelectionContainerTextJoinStyle>): SelectionContainerAttribute; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerAttribute；  API声明：bindSelectionMenu(spanType: Optional<TextSpanType>, content: Optional<CustomBuilder>, responseType: Optional<TextResponseType>, options?: Optional<SelectionContainerMenuOptions>): SelectionContainerAttribute;  差异内容：bindSelectionMenu(spanType: Optional<TextSpanType>, content: Optional<CustomBuilder>, responseType: Optional<TextResponseType>, options?: Optional<SelectionContainerMenuOptions>): SelectionContainerAttribute; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerAttribute；  API声明：editMenuOptions(editMenu: Optional<SelectionContainerEditMenuOptions>): SelectionContainerAttribute;  差异内容：editMenuOptions(editMenu: Optional<SelectionContainerEditMenuOptions>): SelectionContainerAttribute; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerAttribute；  API声明：onTextSelectionChange(callback: Optional<Callback<Array<string>>>): SelectionContainerAttribute;  差异内容：onTextSelectionChange(callback: Optional<Callback<Array<string>>>): SelectionContainerAttribute; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerAttribute；  API声明：onWillCopy(callback: Optional<Callback<string, boolean>>): SelectionContainerAttribute;  差异内容：onWillCopy(callback: Optional<Callback<string, boolean>>): SelectionContainerAttribute; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerAttribute；  API声明：onCopy(callback: Optional<Callback<string>>): SelectionContainerAttribute;  差异内容：onCopy(callback: Optional<Callback<string>>): SelectionContainerAttribute; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare const SelectionContainer: SelectionContainerInterface;  差异内容：export declare const SelectionContainer: SelectionContainerInterface; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare const SelectionContainerInstance: SelectionContainerAttribute;  差异内容：export declare const SelectionContainerInstance: SelectionContainerAttribute; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare class WithEnvAttribute  差异内容：export declare class WithEnvAttribute | api/@ohos.arkui.WithEnv.d.ts |
| 新增API | NA | 类名：WithEnvAttribute；  API声明：env<T>(key: WritableSystemEnvKey<T>, value: T): WithEnvAttribute;  差异内容：env<T>(key: WritableSystemEnvKey<T>, value: T): WithEnvAttribute; | api/@ohos.arkui.WithEnv.d.ts |
| 新增API | NA | 类名：WithEnvAttribute；  API声明：customEnv<T>(key: CustomEnvKey<T>, value: T): WithEnvAttribute;  差异内容：customEnv<T>(key: CustomEnvKey<T>, value: T): WithEnvAttribute; | api/@ohos.arkui.WithEnv.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare type WithEnvInterface = () => WithEnvAttribute;  差异内容：export declare type WithEnvInterface = () => WithEnvAttribute; | api/@ohos.arkui.WithEnv.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare const WithEnv: WithEnvInterface;  差异内容：export declare const WithEnv: WithEnvInterface; | api/@ohos.arkui.WithEnv.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare const WithEnvInstance: WithEnvAttribute;  差异内容：export declare const WithEnvInstance: WithEnvAttribute; | api/@ohos.arkui.WithEnv.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare class ContainerReaderModifier  差异内容：export declare class ContainerReaderModifier | api/arkui/ContainerReaderModifier.d.ts |
| 新增API | NA | 类名：ContainerReaderModifier；  API声明：applyNormalAttribute?(instance: ContainerReaderAttribute): void;  差异内容：applyNormalAttribute?(instance: ContainerReaderAttribute): void; | api/arkui/ContainerReaderModifier.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface LazyLayoutAlgorithm  差异内容：export interface LazyLayoutAlgorithm | api/arkui/LazyLayoutAlgorithm.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum LazyLayoutDirection  差异内容：export enum LazyLayoutDirection | api/arkui/LazyLayoutAlgorithm.d.ts |
| 新增API | NA | 类名：LazyLayoutDirection；  API声明：FORWARD = 0  差异内容：FORWARD = 0 | api/arkui/LazyLayoutAlgorithm.d.ts |
| 新增API | NA | 类名：LazyLayoutDirection；  API声明：BACKWARD = 1  差异内容：BACKWARD = 1 | api/arkui/LazyLayoutAlgorithm.d.ts |
| 新增API | NA | 类名：global；  API声明：export class LazyLayoutHelper  差异内容：export class LazyLayoutHelper | api/arkui/LazyLayoutAlgorithm.d.ts |
| 新增API | NA | 类名：LazyLayoutHelper；  API声明：getViewStart(): number;  差异内容：getViewStart(): number; | api/arkui/LazyLayoutAlgorithm.d.ts |
| 新增API | NA | 类名：LazyLayoutHelper；  API声明：getViewEnd(): number;  差异内容：getViewEnd(): number; | api/arkui/LazyLayoutAlgorithm.d.ts |
| 新增API | NA | 类名：LazyLayoutHelper；  API声明：getLazyLayoutDirection(): LazyLayoutDirection;  差异内容：getLazyLayoutDirection(): LazyLayoutDirection; | api/arkui/LazyLayoutAlgorithm.d.ts |
| 新增API | NA | 类名：LazyLayoutHelper；  API声明：setAdjustedOffset(offset: number): void;  差异内容：setAdjustedOffset(offset: number): void; | api/arkui/LazyLayoutAlgorithm.d.ts |
| 新增API | NA | 类名：LazyLayoutHelper；  API声明：setChildrenInactive(children: number[]): void;  差异内容：setChildrenInactive(children: number[]): void; | api/arkui/LazyLayoutAlgorithm.d.ts |
| 新增API | NA | 类名：global；  API声明：interface LazyCustomLayoutAlgorithmOptions  差异内容：interface LazyCustomLayoutAlgorithmOptions | api/arkui/LazyLayoutAlgorithm.d.ts |
| 新增API | NA | 类名：LazyCustomLayoutAlgorithmOptions；  API声明：axis?: Axis;  差异内容：axis?: Axis; | api/arkui/LazyLayoutAlgorithm.d.ts |
| 新增API | NA | 类名：global；  API声明：export class LazyCustomLayoutAlgorithm  差异内容：export class LazyCustomLayoutAlgorithm | api/arkui/LazyLayoutAlgorithm.d.ts |
| 新增API | NA | 类名：LazyCustomLayoutAlgorithm；  API声明：onMeasure(self: FrameNode, constraint: LayoutConstraint, helper?: LazyLayoutHelper): void;  差异内容：onMeasure(self: FrameNode, constraint: LayoutConstraint, helper?: LazyLayoutHelper): void; | api/arkui/LazyLayoutAlgorithm.d.ts |
| 新增API | NA | 类名：LazyCustomLayoutAlgorithm；  API声明：onLayout(self: FrameNode, position: Position): void;  差异内容：onLayout(self: FrameNode, position: Position): void; | api/arkui/LazyLayoutAlgorithm.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare class SelectionContainerModifier  差异内容：export declare class SelectionContainerModifier | api/arkui/SelectionContainerModifier.d.ts |
| 新增API | NA | 类名：SelectionContainerModifier；  API声明：applyNormalAttribute?(instance: SelectionContainerAttribute): void;  差异内容：applyNormalAttribute?(instance: SelectionContainerAttribute): void; | api/arkui/SelectionContainerModifier.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface OrderOverlayOptions  差异内容：export interface OrderOverlayOptions | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：OrderOverlayOptions；  API声明：levelOrder?: LevelOrder;  差异内容：levelOrder?: LevelOrder; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：OrderOverlayOptions；  API声明：levelMode?: LevelMode;  差异内容：levelMode?: LevelMode; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：OrderOverlayOptions；  API声明：levelUniqueId?: number;  差异内容：levelUniqueId?: number; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：OverlayManager；  API声明：openOrderOverlay(content: ComponentContent, options?: OrderOverlayOptions): Promise<void>;  差异内容：openOrderOverlay(content: ComponentContent, options?: OrderOverlayOptions): Promise<void>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：export abstract class BaseGestureHandlingProposal  差异内容：export abstract class BaseGestureHandlingProposal | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：BaseGestureHandlingProposal；  API声明：action: SmartGestureAction;  差异内容：action: SmartGestureAction; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：BaseGestureHandlingProposal；  API声明：operateIntention: OperateIntention;  差异内容：operateIntention: OperateIntention; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：export abstract class TargetedGestureProposal  差异内容：export abstract class TargetedGestureProposal | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：TargetedGestureProposal；  API声明：node: FrameNode;  差异内容：node: FrameNode; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：export class ClickActionProposal  差异内容：export class ClickActionProposal | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：export class SelectActionProposal  差异内容：export class SelectActionProposal | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：export class NoneActionProposal  差异内容：export class NoneActionProposal | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：export class BackPressActionProposal  差异内容：export class BackPressActionProposal | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：export class PageSwitchActionProposal  差异内容：export class PageSwitchActionProposal | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：PageSwitchActionProposal；  API声明：pageCount: number;  差异内容：pageCount: number; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：export class ScrollActionProposal  差异内容：export class ScrollActionProposal | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：ScrollActionProposal；  API声明：distance?: number;  差异内容：distance?: number; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：export class GestureHandlingResolution  差异内容：export class GestureHandlingResolution | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：GestureHandlingResolution；  API声明：isConsumed: boolean;  差异内容：isConsumed: boolean; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：GestureHandlingResolution；  API声明：selectedProposal?: BaseGestureHandlingProposal;  差异内容：selectedProposal?: BaseGestureHandlingProposal; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：export class SmartGestureController  差异内容：export class SmartGestureController | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：SmartGestureController；  API声明：enableSmartTapAndSlideGestures(enabled: boolean): void;  差异内容：enableSmartTapAndSlideGestures(enabled: boolean): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：SmartGestureController；  API声明：registerMonitor(monitorCallback: Callback<BaseGestureHandlingProposal, GestureHandlingResolution>): void;  差异内容：registerMonitor(monitorCallback: Callback<BaseGestureHandlingProposal, GestureHandlingResolution>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：SmartGestureController；  API声明：unregisterMonitor(monitorCallback: Callback<BaseGestureHandlingProposal, GestureHandlingResolution>): void;  差异内容：unregisterMonitor(monitorCallback: Callback<BaseGestureHandlingProposal, GestureHandlingResolution>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：SmartGestureController；  API声明：clearMonitors(): void;  差异内容：clearMonitors(): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：SmartGestureController；  API声明：requestSelected(id: string): void;  差异内容：requestSelected(id: string): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：SmartGestureController；  API声明：clearSelected(): void;  差异内容：clearSelected(): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getSmartGestureController(): SmartGestureController;  差异内容：getSmartGestureController(): SmartGestureController; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：DrawableDescriptor；  API声明：release(): void;  差异内容：release(): void; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：DrawableDescriptor；  API声明：isReleased(): boolean;  差异内容：isReleased(): boolean; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：DrawableDescriptor；  API声明：invalidate(): void;  差异内容：invalidate(): void; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface HdrCompositionConfig  差异内容：declare interface HdrCompositionConfig | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：HdrCompositionConfig；  API声明：rect: Rectangle;  差异内容：rect: Rectangle; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：global；  API声明：export class PictureDrawableDescriptor  差异内容：export class PictureDrawableDescriptor | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：PictureDrawableDescriptor；  API声明：setHdrComposition(config: HdrCompositionConfig): void;  差异内容：setHdrComposition(config: HdrCompositionConfig): void; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：BrightnessInfo；  API声明：readonly brightnessPosition?: number;  差异内容：readonly brightnessPosition?: number; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：BaseDialogOptions；  API声明：displayModeInSubWindow?: DialogDisplayMode;  差异内容：displayModeInSubWindow?: DialogDisplayMode; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：window；  API声明：enum AcrossDisplayPresentation  差异内容：enum AcrossDisplayPresentation | api/@ohos.window.d.ts |
| 新增API | NA | 类名：AcrossDisplayPresentation；  API声明：FOLLOW\_ACROSS\_DISPLAY\_SETTING = 0  差异内容：FOLLOW\_ACROSS\_DISPLAY\_SETTING = 0 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：AcrossDisplayPresentation；  API声明：ENTER\_ACROSS\_DISPLAY\_MODE = 1  差异内容：ENTER\_ACROSS\_DISPLAY\_MODE = 1 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：AcrossDisplayPresentation；  API声明：EXIT\_ACROSS\_DISPLAY\_MODE = 2  差异内容：EXIT\_ACROSS\_DISPLAY\_MODE = 2 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：interface MaximizeOptions  差异内容：interface MaximizeOptions | api/@ohos.window.d.ts |
| 新增API | NA | 类名：MaximizeOptions；  API声明：maximizePresentation?: MaximizePresentation;  差异内容：maximizePresentation?: MaximizePresentation; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：MaximizeOptions；  API声明：acrossDisplayPresentation?: AcrossDisplayPresentation;  差异内容：acrossDisplayPresentation?: AcrossDisplayPresentation; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：MaximizeOptions；  API声明：snapshotAnimationConfig?: WindowSnapshotAnimationConfig;  差异内容：snapshotAnimationConfig?: WindowSnapshotAnimationConfig; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：interface WindowSnapshotAnimationConfig  差异内容：interface WindowSnapshotAnimationConfig | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowSnapshotAnimationConfig；  API声明：duration?: number;  差异内容：duration?: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowSnapshotAnimationConfig；  API声明：delay?: number;  差异内容：delay?: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：maximizeWithOptions(maximizeOptions?: MaximizeOptions): Promise<void>;  差异内容：maximizeWithOptions(maximizeOptions?: MaximizeOptions): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：setSupportedWindowModes(supportedWindowModes: Array<bundleManager.SupportWindowMode>): Promise<void>;  差异内容：setSupportedWindowModes(supportedWindowModes: Array<bundleManager.SupportWindowMode>): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：ExpandMode；  API声明：LAZY\_NOT\_EXPAND = 3  差异内容：LAZY\_NOT\_EXPAND = 3 | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum ChildrenCountMode  差异内容：export enum ChildrenCountMode | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：ChildrenCountMode；  API声明：ALL\_EXPAND = 0  差异内容：ALL\_EXPAND = 0 | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：ChildrenCountMode；  API声明：ONLY\_EXPANDED = 1  差异内容：ONLY\_EXPANDED = 1 | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：ChildrenCountMode；  API声明：ALL\_NOT\_EXPAND = 2  差异内容：ALL\_NOT\_EXPAND = 2 | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：UIState；  API声明：HOVERED = 1 << 4  差异内容：HOVERED = 1 << 4 | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：global；  API声明：type window = import('../api/@ohos.window').default;  差异内容：type window = import('../api/@ohos.window').default; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class SystemEnvKey  差异内容：declare class SystemEnvKey | component/common.d.ts |
| 新增API | NA | 类名：SystemEnvKey；  API声明：private type?: T;  差异内容：private type?: T; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class WritableSystemEnvKey  差异内容：declare class WritableSystemEnvKey | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class ReadonlySystemEnvKey  差异内容：declare class ReadonlySystemEnvKey | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class CustomEnvKey  差异内容：declare class CustomEnvKey | component/common.d.ts |
| 新增API | NA | 类名：CustomEnvKey；  API声明：private type?: S;  差异内容：private type?: S; | component/common.d.ts |
| 新增API | NA | 类名：CustomEnvKey；  API声明：static create<T>(): CustomEnvKey<T>;  差异内容：static create<T>(): CustomEnvKey<T>; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class WritableEnvKey  差异内容：declare class WritableEnvKey | component/common.d.ts |
| 新增API | NA | 类名：WritableEnvKey；  API声明：static readonly DIRECTION: WritableSystemEnvKey<Direction>;  差异内容：static readonly DIRECTION: WritableSystemEnvKey<Direction>; | component/common.d.ts |
| 新增API | NA | 类名：WritableEnvKey；  API声明：static readonly FONT\_SCALE: WritableSystemEnvKey<number>;  差异内容：static readonly FONT\_SCALE: WritableSystemEnvKey<number>; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class ReadonlyEnvKey  差异内容：declare class ReadonlyEnvKey | component/common.d.ts |
| 新增API | NA | 类名：ReadonlyEnvKey；  API声明：static readonly WINDOW\_AVOID\_AREA: ReadonlySystemEnvKey<window.UIEnvWindowAvoidAreaInfoVP>;  差异内容：static readonly WINDOW\_AVOID\_AREA: ReadonlySystemEnvKey<window.UIEnvWindowAvoidAreaInfoVP>; | component/common.d.ts |
| 新增API | NA | 类名：ReadonlyEnvKey；  API声明：static readonly WINDOW\_AVOID\_AREA\_PX: ReadonlySystemEnvKey<window.UIEnvWindowAvoidAreaInfoPX>;  差异内容：static readonly WINDOW\_AVOID\_AREA\_PX: ReadonlySystemEnvKey<window.UIEnvWindowAvoidAreaInfoPX>; | component/common.d.ts |
| 新增API | NA | 类名：ReadonlyEnvKey；  API声明：static readonly WINDOW\_SIZE: ReadonlySystemEnvKey<window.SizeInVP>;  差异内容：static readonly WINDOW\_SIZE: ReadonlySystemEnvKey<window.SizeInVP>; | component/common.d.ts |
| 新增API | NA | 类名：ReadonlyEnvKey；  API声明：static readonly WINDOW\_SIZE\_PX: ReadonlySystemEnvKey<window.Size>;  差异内容：static readonly WINDOW\_SIZE\_PX: ReadonlySystemEnvKey<window.Size>; | component/common.d.ts |
| 新增API | NA | 类名：ReadonlyEnvKey；  API声明：static readonly WINDOW\_DISPLAY\_ID: ReadonlySystemEnvKey<number>;  差异内容：static readonly WINDOW\_DISPLAY\_ID: ReadonlySystemEnvKey<number>; | component/common.d.ts |
| 新增API | NA | 类名：ReadonlyEnvKey；  API声明：static readonly WINDOW\_SYSTEM\_DENSITY: ReadonlySystemEnvKey<number>;  差异内容：static readonly WINDOW\_SYSTEM\_DENSITY: ReadonlySystemEnvKey<number>; | component/common.d.ts |
| 新增API | NA | 类名：ReadonlyEnvKey；  API声明：static readonly WINDOW\_IS\_FOCUSED: ReadonlySystemEnvKey<boolean>;  差异内容：static readonly WINDOW\_IS\_FOCUSED: ReadonlySystemEnvKey<boolean>; | component/common.d.ts |
| 新增API | NA | 类名：ReadonlyEnvKey；  API声明：static readonly WINDOW\_IS\_HIGHLIGHTED: ReadonlySystemEnvKey<boolean>;  差异内容：static readonly WINDOW\_IS\_HIGHLIGHTED: ReadonlySystemEnvKey<boolean>; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare function CustomEnv<T>(key: CustomEnvKey<T>): PropertyDecorator;  差异内容：declare function CustomEnv<T>(key: CustomEnvKey<T>): PropertyDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare function Env<T>(key: SystemEnvKey<T> | SystemProperties): PropertyDecorator;  差异内容：declare function Env<T>(key: SystemEnvKey<T> | SystemProperties): PropertyDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type ShouldRecognizerParallelWithCallback = (current: GestureRecognizer, others: Array<GestureRecognizer>) => GestureRecognizer;  差异内容：declare type ShouldRecognizerParallelWithCallback = (current: GestureRecognizer, others: Array<GestureRecognizer>) => GestureRecognizer; | component/common.d.ts |
| 新增API | NA | 类名：StateStyles；  API声明：hovered?: object;  差异内容：hovered?: object; | component/common.d.ts |
| 新增API | NA | 类名：PopupCommonOptions；  API声明：levelMode?: LevelMode;  差异内容：levelMode?: LevelMode; | component/common.d.ts |
| 新增API | NA | 类名：PopupCommonOptions；  API声明：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions;  差异内容：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions; | component/common.d.ts |
| 新增API | NA | 类名：PopupCommonOptions；  API声明：backgroundEffect?: BackgroundEffectOptions;  差异内容：backgroundEffect?: BackgroundEffectOptions; | component/common.d.ts |
| 新增API | NA | 类名：PopupOptions；  API声明：levelMode?: LevelMode;  差异内容：levelMode?: LevelMode; | component/common.d.ts |
| 新增API | NA | 类名：PopupOptions；  API声明：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions;  差异内容：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions; | component/common.d.ts |
| 新增API | NA | 类名：PopupOptions；  API声明：backgroundEffect?: BackgroundEffectOptions;  差异内容：backgroundEffect?: BackgroundEffectOptions; | component/common.d.ts |
| 新增API | NA | 类名：CustomPopupOptions；  API声明：levelMode?: LevelMode;  差异内容：levelMode?: LevelMode; | component/common.d.ts |
| 新增API | NA | 类名：CustomPopupOptions；  API声明：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions;  差异内容：backgroundBlurStyleOptions?: BackgroundBlurStyleOptions; | component/common.d.ts |
| 新增API | NA | 类名：CustomPopupOptions；  API声明：backgroundEffect?: BackgroundEffectOptions;  差异内容：backgroundEffect?: BackgroundEffectOptions; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum MenuGridPosition  差异内容：declare enum MenuGridPosition | component/common.d.ts |
| 新增API | NA | 类名：MenuGridPosition；  API声明：TOP = 0  差异内容：TOP = 0 | component/common.d.ts |
| 新增API | NA | 类名：MenuGridPosition；  API声明：BOTTOM = 1  差异内容：BOTTOM = 1 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface MenuGridStyleOptions  差异内容：declare interface MenuGridStyleOptions | component/common.d.ts |
| 新增API | NA | 类名：MenuGridStyleOptions；  API声明：count?: number;  差异内容：count?: number; | component/common.d.ts |
| 新增API | NA | 类名：MenuGridStyleOptions；  API声明：horizontalSize?: number;  差异内容：horizontalSize?: number; | component/common.d.ts |
| 新增API | NA | 类名：MenuGridStyleOptions；  API声明：position?: MenuGridPosition;  差异内容：position?: MenuGridPosition; | component/common.d.ts |
| 新增API | NA | 类名：ContextMenuOptions；  API声明：targetSpace?: LengthMetrics;  差异内容：targetSpace?: LengthMetrics; | component/common.d.ts |
| 新增API | NA | 类名：ContextMenuOptions；  API声明：gridStyle?: MenuGridStyleOptions;  差异内容：gridStyle?: MenuGridStyleOptions; | component/common.d.ts |
| 新增API | NA | 类名：AttributeModifier；  API声明：applyHoveredAttribute?(instance: T): void;  差异内容：applyHoveredAttribute?(instance: T): void; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：bindContextMenuByResponseType(content: CustomBuilder | Array<MenuElement>, responseType: ResponseType, options?: ContextMenuOptions): T;  差异内容：bindContextMenuByResponseType(content: CustomBuilder | Array<MenuElement>, responseType: ResponseType, options?: ContextMenuOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：bindContextMenuByIsShow(isShow: boolean, content: CustomBuilder | Array<MenuElement>, options?: ContextMenuOptions): T;  差异内容：bindContextMenuByIsShow(isShow: boolean, content: CustomBuilder | Array<MenuElement>, options?: ContextMenuOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：shouldRecognizerParallelWith(callback: ShouldRecognizerParallelWithCallback): T;  差异内容：shouldRecognizerParallelWith(callback: ShouldRecognizerParallelWithCallback): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：accessibilityCustomActions(actions: Array<AccessibilityCustomAction> | undefined): T;  差异内容：accessibilityCustomActions(actions: Array<AccessibilityCustomAction> | undefined): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：smartGestureShortcut(options?: SmartGestureShortcutOptions): T;  差异内容：smartGestureShortcut(options?: SmartGestureShortcutOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：inspectorLabel(label: string | undefined): T;  差异内容：inspectorLabel(label: string | undefined): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：doubleSided(value: Optional<boolean>): T;  差异内容：doubleSided(value: Optional<boolean>): T; | component/common.d.ts |
| 新增API | NA | 类名：ScrollableCommonMethod；  API声明：scrollBarHeight(height: LengthMetrics | undefined): T;  差异内容：scrollBarHeight(height: LengthMetrics | undefined): T; | component/common.d.ts |
| 新增API | NA | 类名：EditModeOptions；  API声明：useDefaultMultiSelectStyle?: boolean;  差异内容：useDefaultMultiSelectStyle?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：EditModeOptions；  API声明：enableTwoFingerMultiSelect?: boolean;  差异内容：enableTwoFingerMultiSelect?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface SmartGestureShortcutOptions  差异内容：declare interface SmartGestureShortcutOptions | component/common.d.ts |
| 新增API | NA | 类名：SmartGestureShortcutOptions；  API声明：action?: GestureShortcut;  差异内容：action?: GestureShortcut; | component/common.d.ts |
| 新增API | NA | 类名：SmartGestureShortcutOptions；  API声明：enabled?: boolean;  差异内容：enabled?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：SmartGestureShortcutOptions；  API声明：selectable?: boolean;  差异内容：selectable?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：CustomDialogControllerOptions；  API声明：displayModeInSubWindow?: DialogDisplayMode;  差异内容：displayModeInSubWindow?: DialogDisplayMode; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：systemMaterial?: SystemUiMaterial;  差异内容：systemMaterial?: SystemUiMaterial; | component/date\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum DialogDisplayMode  差异内容：declare enum DialogDisplayMode | component/enums.d.ts |
| 新增API | NA | 类名：DialogDisplayMode；  API声明：SCREEN\_BASED = 0  差异内容：SCREEN\_BASED = 0 | component/enums.d.ts |
| 新增API | NA | 类名：DialogDisplayMode；  API声明：WINDOW\_BASED = 1  差异内容：WINDOW\_BASED = 1 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum GestureShortcut  差异内容：declare enum GestureShortcut | component/enums.d.ts |
| 新增API | NA | 类名：GestureShortcut；  API声明：PRIMARY = 0  差异内容：PRIMARY = 0 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum SmartGestureAction  差异内容：declare enum SmartGestureAction | component/enums.d.ts |
| 新增API | NA | 类名：SmartGestureAction；  API声明：NONE = 0  差异内容：NONE = 0 | component/enums.d.ts |
| 新增API | NA | 类名：SmartGestureAction；  API声明：PAGE\_FORWARD = 1  差异内容：PAGE\_FORWARD = 1 | component/enums.d.ts |
| 新增API | NA | 类名：SmartGestureAction；  API声明：SCROLL\_FORWARD = 2  差异内容：SCROLL\_FORWARD = 2 | component/enums.d.ts |
| 新增API | NA | 类名：SmartGestureAction；  API声明：SELECT = 3  差异内容：SELECT = 3 | component/enums.d.ts |
| 新增API | NA | 类名：SmartGestureAction；  API声明：CLICK = 4  差异内容：CLICK = 4 | component/enums.d.ts |
| 新增API | NA | 类名：SmartGestureAction；  API声明：BACK\_PRESS = 5  差异内容：BACK\_PRESS = 5 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum OperateIntention  差异内容：declare enum OperateIntention | component/enums.d.ts |
| 新增API | NA | 类名：OperateIntention；  API声明：TAP = 0  差异内容：TAP = 0 | component/enums.d.ts |
| 新增API | NA | 类名：OperateIntention；  API声明：SLIDE\_FORWARD = 1  差异内容：SLIDE\_FORWARD = 1 | component/enums.d.ts |
| 新增API | NA | 类名：OperateIntention；  API声明：BACK\_PRESS = 2  差异内容：BACK\_PRESS = 2 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type Material = import('../api/@ohos.arkui.uiMaterial').default.Material;  差异内容：declare type Material = import('../api/@ohos.arkui.uiMaterial').default.Material; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum ScrollEffectType  差异内容：declare enum ScrollEffectType | component/navigation.d.ts |
| 新增API | NA | 类名：ScrollEffectType；  API声明：COMMON\_BLUR = 0  差异内容：COMMON\_BLUR = 0 | component/navigation.d.ts |
| 新增API | NA | 类名：ScrollEffectType；  API声明：GRADUAL\_BLUR = 1  差异内容：GRADUAL\_BLUR = 1 | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface ScrollEffectOptions  差异内容：declare interface ScrollEffectOptions | component/navigation.d.ts |
| 新增API | NA | 类名：ScrollEffectOptions；  API声明：scrollEffectType?: ScrollEffectType;  差异内容：scrollEffectType?: ScrollEffectType; | component/navigation.d.ts |
| 新增API | NA | 类名：ScrollEffectOptions；  API声明：blurEffectiveStartOffset?: LengthMetrics;  差异内容：blurEffectiveStartOffset?: LengthMetrics; | component/navigation.d.ts |
| 新增API | NA | 类名：ScrollEffectOptions；  API声明：blurEffectiveEndOffset?: LengthMetrics;  差异内容：blurEffectiveEndOffset?: LengthMetrics; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationTitleOptions；  API声明：scrollEffectOptions?: ScrollEffectOptions;  差异内容：scrollEffectOptions?: ScrollEffectOptions; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationTitleOptions；  API声明：systemMaterial?: Material;  差异内容：systemMaterial?: Material; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface NavigationConfiguration  差异内容：declare interface NavigationConfiguration | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationConfiguration；  API声明：stackSizeLimit?: number;  差异内容：stackSizeLimit?: number; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationAttribute；  API声明：configuration(config: NavigationConfiguration): NavigationAttribute;  差异内容：configuration(config: NavigationConfiguration): NavigationAttribute; | component/navigation.d.ts |
| 新增API | NA | 类名：NavDestinationAttribute；  API声明：onSaveState(callback: Optional<SaveStateCallback>): NavDestinationAttribute;  差异内容：onSaveState(callback: Optional<SaveStateCallback>): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationAttribute；  API声明：onRestoreState(callback: Optional<RestoreStateCallback>): NavDestinationAttribute;  差异内容：onRestoreState(callback: Optional<RestoreStateCallback>): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type SaveStateCallback = () => Record<string, Object> | null;  差异内容：declare type SaveStateCallback = () => Record<string, Object> | null; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type RestoreStateCallback = (savedState: Record<string, Object> | null) => void;  差异内容：declare type RestoreStateCallback = (savedState: Record<string, Object> | null) => void; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：RichEditorTextStyle；  API声明：strokeJoinStyle?: StrokeJoinStyle;  差异内容：strokeJoinStyle?: StrokeJoinStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorParagraphStyle；  API声明：shaderStyle?: ShaderStyle;  差异内容：shaderStyle?: ShaderStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextStyleResult；  API声明：strokeJoinStyle?: StrokeJoinStyle;  差异内容：strokeJoinStyle?: StrokeJoinStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorBaseController；  API声明：scrollToVisible(range?: TextRange): void;  差异内容：scrollToVisible(range?: TextRange): void; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：punctuationOverflow(enabled: Optional<boolean>): RichEditorAttribute;  差异内容：punctuationOverflow(enabled: Optional<boolean>): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：DotIndicator；  API声明：indicatorIcon(iconList: Array<IndicatorIconInfo>): DotIndicator;  差异内容：indicatorIcon(iconList: Array<IndicatorIconInfo>): DotIndicator; | component/swiper.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface IndicatorIconInfo  差异内容：declare interface IndicatorIconInfo | component/swiper.d.ts |
| 新增API | NA | 类名：IndicatorIconInfo；  API声明：index: number;  差异内容：index: number; | component/swiper.d.ts |
| 新增API | NA | 类名：IndicatorIconInfo；  API声明：icon: ResourceStr | SymbolGlyphModifier;  差异内容：icon: ResourceStr | SymbolGlyphModifier; | component/swiper.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：strokeJoinStyle(strokeJoinStyle: StrokeJoinStyle | undefined): TextAreaAttribute;  差异内容：strokeJoinStyle(strokeJoinStyle: StrokeJoinStyle | undefined): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：shaderStyle(shader: ShaderStyle | undefined): TextAreaAttribute;  差异内容：shaderStyle(shader: ShaderStyle | undefined): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：punctuationOverflow(enabled: Optional<boolean>): TextAreaAttribute;  差异内容：punctuationOverflow(enabled: Optional<boolean>): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：strokeJoinStyle(strokeJoinStyle: StrokeJoinStyle | undefined): TextInputAttribute;  差异内容：strokeJoinStyle(strokeJoinStyle: StrokeJoinStyle | undefined): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：shaderStyle(shader: ShaderStyle | undefined): TextInputAttribute;  差异内容：shaderStyle(shader: ShaderStyle | undefined): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：punctuationOverflow(enabled: Optional<boolean>): TextInputAttribute;  差异内容：punctuationOverflow(enabled: Optional<boolean>): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextPickerDialogOptionsExt；  API声明：systemMaterial?: SystemUiMaterial;  差异内容：systemMaterial?: SystemUiMaterial; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TimePickerDialogOptions；  API声明：systemMaterial?: SystemUiMaterial;  差异内容：systemMaterial?: SystemUiMaterial; | component/time\_picker.d.ts |
| 新增API | NA | 类名：UIPickerComponentAttribute；  API声明：itemHeight(height: Optional<LengthMetrics>): UIPickerComponentAttribute;  差异内容：itemHeight(height: Optional<LengthMetrics>): UIPickerComponentAttribute; | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：UIPickerComponentAttribute；  API声明：displayedItemCount(count: Optional<number>): UIPickerComponentAttribute;  差异内容：displayedItemCount(count: Optional<number>): UIPickerComponentAttribute; | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：VideoOptions；  API声明：controllerAsync?: VideoControllerAsync;  差异内容：controllerAsync?: VideoControllerAsync; | component/video.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class VideoControllerAsync  差异内容：declare class VideoControllerAsync | component/video.d.ts |
| 新增API | NA | 类名：VideoControllerAsync；  API声明：start(): Promise<void>;  差异内容：start(): Promise<void>; | component/video.d.ts |
| 新增API | NA | 类名：VideoControllerAsync；  API声明：pause(): Promise<void>;  差异内容：pause(): Promise<void>; | component/video.d.ts |
| 新增API | NA | 类名：VideoControllerAsync；  API声明：stop(): Promise<void>;  差异内容：stop(): Promise<void>; | component/video.d.ts |
| 新增API | NA | 类名：VideoControllerAsync；  API声明：requestFullscreen(value: boolean);  差异内容：requestFullscreen(value: boolean); | component/video.d.ts |
| 新增API | NA | 类名：VideoControllerAsync；  API声明：exitFullscreen();  差异内容：exitFullscreen(); | component/video.d.ts |
| 新增API | NA | 类名：VideoControllerAsync；  API声明：setCurrentTime(value: number, seekMode?: SeekMode);  差异内容：setCurrentTime(value: number, seekMode?: SeekMode); | component/video.d.ts |
| 新增API | NA | 类名：VideoControllerAsync；  API声明：reset(): Promise<void>;  差异内容：reset(): Promise<void>; | component/video.d.ts |
| 新增API | NA | 类名：IconGroupSuffix；  API声明：@Prop  iconBackgroundSystemMaterial?: uiMaterial.Material;  差异内容：@Prop  iconBackgroundSystemMaterial?: uiMaterial.Material; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroup；  API声明：@Prop  backgroundSystemMaterial?: uiMaterial.Material;  差异内容：@Prop  backgroundSystemMaterial?: uiMaterial.Material; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroup；  API声明：@Prop  selectedBackgroundSystemMaterial?: uiMaterial.Material;  差异内容：@Prop  selectedBackgroundSystemMaterial?: uiMaterial.Material; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface PopupV2Button  差异内容：export interface PopupV2Button | api/@ohos.arkui.advanced.PopupV2.d.ets |
| 新增API | NA | 类名：PopupV2Button；  API声明：text: ResourceStr;  差异内容：text: ResourceStr; | api/@ohos.arkui.advanced.PopupV2.d.ets |
| 新增API | NA | 类名：PopupV2Button；  API声明：buttonTextModifier?: TextModifier;  差异内容：buttonTextModifier?: TextModifier; | api/@ohos.arkui.advanced.PopupV2.d.ets |
| 新增API | NA | 类名：PopupV2Button；  API声明：action?: Callback<void>;  差异内容：action?: Callback<void>; | api/@ohos.arkui.advanced.PopupV2.d.ets |
| 新增API | NA | 类名：SelectionMenuOptions；  API声明：backgroundSystemMaterial?: uiMaterial.Material;  差异内容：backgroundSystemMaterial?: uiMaterial.Material; | api/@ohos.arkui.advanced.SelectionMenu.d.ets |
| 新增API | NA | 类名：LazyWaterFlowLayoutAttribute；  API声明：header(builder: CustomBuilder | undefined): T;  差异内容：header(builder: CustomBuilder | undefined): T; | api/@ohos.arkui.components.ArkLazyWaterFlowLayout.d.ts |
| 新增API | NA | 类名：LazyWaterFlowLayoutAttribute；  API声明：footer(builder: CustomBuilder | undefined): T;  差异内容：footer(builder: CustomBuilder | undefined): T; | api/@ohos.arkui.components.ArkLazyWaterFlowLayout.d.ts |
| 新增API | NA | 类名：LazyWaterFlowLayoutAttribute；  API声明：sticky(sticky: StickyStyle | undefined): T;  差异内容：sticky(sticky: StickyStyle | undefined): T; | api/@ohos.arkui.components.ArkLazyWaterFlowLayout.d.ts |
| 新增API | NA | 类名：Colors；  API声明：primary?: ResourceColor;  差异内容：primary?: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：onPrimary?: ResourceColor;  差异内容：onPrimary?: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：container?: ResourceColor;  差异内容：container?: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：FloatingBallController；  API声明：onDestroy(callback: Callback<string>): void;  差异内容：onDestroy(callback: Callback<string>): void; | api/@ohos.window.floatingBall.d.ts |
| 新增API | NA | 类名：FloatingBallController；  API声明：offDestroy(callback?: Callback<string>): void;  差异内容：offDestroy(callback?: Callback<string>): void; | api/@ohos.window.floatingBall.d.ts |
| 新增API | NA | 类名：FloatingBallParams；  API声明：titleColor?: string;  差异内容：titleColor?: string; | api/@ohos.window.floatingBall.d.ts |
| 新增API | NA | 类名：FloatingBallParams；  API声明：contentColor?: string;  差异内容：contentColor?: string; | api/@ohos.window.floatingBall.d.ts |
| 新增API | NA | 类名：FloatViewConfiguration；  API声明：isConfirmOnClose?: boolean;  差异内容：isConfirmOnClose?: boolean; | api/@ohos.window.floatView.d.ts |
| 新增API | NA | 类名：floatView；  API声明：interface TemplateProperty  差异内容：interface TemplateProperty | api/@ohos.window.floatView.d.ts |
| 新增API | NA | 类名：TemplateProperty；  API声明：templateType: FloatViewTemplateType;  差异内容：templateType: FloatViewTemplateType; | api/@ohos.window.floatView.d.ts |
| 新增API | NA | 类名：TemplateProperty；  API声明：size: window.Size;  差异内容：size: window.Size; | api/@ohos.window.floatView.d.ts |
| 新增API | NA | 类名：FloatViewController；  API声明：switchTemplate(templateProperty: TemplateProperty): Promise<void>;  差异内容：switchTemplate(templateProperty: TemplateProperty): Promise<void>; | api/@ohos.window.floatView.d.ts |
| 新增API | NA | 类名：FloatViewTemplateType；  API声明：HORIZONTAL\_BAR = 1  差异内容：HORIZONTAL\_BAR = 1 | api/@ohos.window.floatView.d.ts |
| 新增API | NA | 类名：LengthMetrics；  API声明：autoRefresh?(value: boolean): LengthMetrics;  差异内容：autoRefresh?(value: boolean): LengthMetrics; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ColorMetrics；  API声明：autoRefresh?(value: boolean): ColorMetrics;  差异内容：autoRefresh?(value: boolean): ColorMetrics; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ColorMetrics；  API声明：autoRefresh?(value: boolean): ColorMetrics;  差异内容：autoRefresh?(value: boolean): ColorMetrics; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface BackgroundBlur  差异内容：export interface BackgroundBlur | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：BackgroundBlur；  API声明：radius: number;  差异内容：radius: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：BackgroundBlur；  API声明：grayscale?: [  number,  number  ];  差异内容：grayscale?: [  number,  number  ]; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface ContentBlur  差异内容：export interface ContentBlur | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ContentBlur；  API声明：radius: number;  差异内容：radius: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ContentBlur；  API声明：grayscale?: [  number,  number  ];  差异内容：grayscale?: [  number,  number  ]; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface ForegroundBlur  差异内容：export interface ForegroundBlur | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ForegroundBlur；  API声明：radius: number;  差异内容：radius: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：CalendarDialogOptions；  API声明：systemMaterial?: SystemUiMaterial;  差异内容：systemMaterial?: SystemUiMaterial; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum EmbeddedDpiFollowStrategy  差异内容：declare enum EmbeddedDpiFollowStrategy | component/embedded\_component.d.ts |
| 新增API | NA | 类名：EmbeddedDpiFollowStrategy；  API声明：FOLLOW\_HOST\_DPI = 0  差异内容：FOLLOW\_HOST\_DPI = 0 | component/embedded\_component.d.ts |
| 新增API | NA | 类名：EmbeddedDpiFollowStrategy；  API声明：FOLLOW\_UI\_EXTENSION\_ABILITY\_DPI = 1  差异内容：FOLLOW\_UI\_EXTENSION\_ABILITY\_DPI = 1 | component/embedded\_component.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum EmbeddedWindowModeFollowStrategy  差异内容：declare enum EmbeddedWindowModeFollowStrategy | component/embedded\_component.d.ts |
| 新增API | NA | 类名：EmbeddedWindowModeFollowStrategy；  API声明：FOLLOW\_HOST\_WINDOW\_MODE = 0  差异内容：FOLLOW\_HOST\_WINDOW\_MODE = 0 | component/embedded\_component.d.ts |
| 新增API | NA | 类名：EmbeddedWindowModeFollowStrategy；  API声明：FOLLOW\_UI\_EXTENSION\_ABILITY\_WINDOW\_MODE = 1  差异内容：FOLLOW\_UI\_EXTENSION\_ABILITY\_WINDOW\_MODE = 1 | component/embedded\_component.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface EmbeddedOptions  差异内容：declare interface EmbeddedOptions | component/embedded\_component.d.ts |
| 新增API | NA | 类名：EmbeddedOptions；  API声明：placeholder?: ComponentContent;  差异内容：placeholder?: ComponentContent; | component/embedded\_component.d.ts |
| 新增API | NA | 类名：EmbeddedOptions；  API声明：areaChangePlaceholder?: Record<string, ComponentContent>;  差异内容：areaChangePlaceholder?: Record<string, ComponentContent>; | component/embedded\_component.d.ts |
| 新增API | NA | 类名：EmbeddedOptions；  API声明：dpiFollowStrategy?: EmbeddedDpiFollowStrategy;  差异内容：dpiFollowStrategy?: EmbeddedDpiFollowStrategy; | component/embedded\_component.d.ts |
| 新增API | NA | 类名：EmbeddedOptions；  API声明：windowModeFollowStrategy?: EmbeddedWindowModeFollowStrategy;  差异内容：windowModeFollowStrategy?: EmbeddedWindowModeFollowStrategy; | component/embedded\_component.d.ts |
| 新增API | NA | 类名：EmbeddedComponentAttribute；  API声明：onDrawReady(callback: Callback<void>): EmbeddedComponentAttribute;  差异内容：onDrawReady(callback: Callback<void>): EmbeddedComponentAttribute; | component/embedded\_component.d.ts |
| 新增API | NA | 类名：GridAttribute；  API声明：enableEditMode(enabled: boolean | undefined): GridAttribute;  差异内容：enableEditMode(enabled: boolean | undefined): GridAttribute; | component/grid.d.ts |
| 新增API | NA | 类名：GridAttribute；  API声明：onEditModeChange(callback: Callback<boolean> | undefined): GridAttribute;  差异内容：onEditModeChange(callback: Callback<boolean> | undefined): GridAttribute; | component/grid.d.ts |
| 新增API | NA | 类名：LazyGridLayoutAttribute；  API声明：header(builder: CustomBuilder | undefined): T;  差异内容：header(builder: CustomBuilder | undefined): T; | component/lazy\_grid\_layout.d.ts |
| 新增API | NA | 类名：LazyGridLayoutAttribute；  API声明：footer(builder: CustomBuilder | undefined): T;  差异内容：footer(builder: CustomBuilder | undefined): T; | component/lazy\_grid\_layout.d.ts |
| 新增API | NA | 类名：LazyGridLayoutAttribute；  API声明：sticky(sticky: StickyStyle | undefined): T;  差异内容：sticky(sticky: StickyStyle | undefined): T; | component/lazy\_grid\_layout.d.ts |
| 新增API | NA | 类名：ListAttribute；  API声明：enableEditMode(enabled: boolean | undefined): ListAttribute;  差异内容：enableEditMode(enabled: boolean | undefined): ListAttribute; | component/list.d.ts |
| 新增API | NA | 类名：ListAttribute；  API声明：onEditModeChange(callback: Callback<boolean> | undefined): ListAttribute;  差异内容：onEditModeChange(callback: Callback<boolean> | undefined): ListAttribute; | component/list.d.ts |
| 新增API | NA | 类名：MenuItemAttribute；  API声明：subMenuBuilder(builder: CustomBuilder): MenuItemAttribute;  差异内容：subMenuBuilder(builder: CustomBuilder): MenuItemAttribute; | component/menu\_item.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：strokeJoinStyle(strokeJoinStyle: StrokeJoinStyle | undefined): SearchAttribute;  差异内容：strokeJoinStyle(strokeJoinStyle: StrokeJoinStyle | undefined): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：shaderStyle(shader: ShaderStyle | undefined): SearchAttribute;  差异内容：shaderStyle(shader: ShaderStyle | undefined): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum SecurityComponentRoleType  差异内容：declare enum SecurityComponentRoleType | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentRoleType；  API声明：ROLE\_NONE = 0  差异内容：ROLE\_NONE = 0 | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentRoleType；  API声明：BUTTON = 1  差异内容：BUTTON = 1 | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：fallbackLineSpacing(enabled: boolean): T;  差异内容：fallbackLineSpacing(enabled: boolean): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：accessibilityNextFocusId(nextId: string): T;  差异内容：accessibilityNextFocusId(nextId: string): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：accessibilityDefaultFocus(focus: boolean): T;  差异内容：accessibilityDefaultFocus(focus: boolean): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：accessibilityRole(role: SecurityComponentRoleType): T;  差异内容：accessibilityRole(role: SecurityComponentRoleType): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：accessibilityDescription(description: string | Resource): T;  差异内容：accessibilityDescription(description: string | Resource): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SelectAttribute；  API声明：menuBackgroundBlurStyleOptions(blurStyle: Optional<BackgroundBlurStyleOptions>): SelectAttribute;  差异内容：menuBackgroundBlurStyleOptions(blurStyle: Optional<BackgroundBlurStyleOptions>): SelectAttribute; | component/select.d.ts |
| 新增API | NA | 类名：SelectAttribute；  API声明：menuBackgroundEffect(effect: Optional<BackgroundEffectOptions>): SelectAttribute;  差异内容：menuBackgroundEffect(effect: Optional<BackgroundEffectOptions>): SelectAttribute; | component/select.d.ts |
| 新增API | NA | 类名：SideBarContainerType；  API声明：DISPLACE = 3  差异内容：DISPLACE = 3 | component/sidebar.d.ts |
| 新增API | NA | 类名：SideBarContainerAttribute；  API声明：showSideBarWithGesture(value: boolean): SideBarContainerAttribute;  差异内容：showSideBarWithGesture(value: boolean): SideBarContainerAttribute; | component/sidebar.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：readonly strokeJoinStyle?: StrokeJoinStyle;  差异内容：readonly strokeJoinStyle?: StrokeJoinStyle; | component/styled\_string.d.ts |
| 新增API | NA | 类名：TextStyleInterface；  API声明：strokeJoinStyle?: StrokeJoinStyle;  差异内容：strokeJoinStyle?: StrokeJoinStyle; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：readonly shaderStyle?: ShaderStyle;  差异内容：readonly shaderStyle?: ShaderStyle; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：readonly tailIndents?: Array<number>;  差异内容：readonly tailIndents?: Array<number>; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ParagraphStyleInterface；  API声明：shaderStyle?: ShaderStyle;  差异内容：shaderStyle?: ShaderStyle; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ParagraphStyleInterface；  API声明：tailIndents?: LengthMetrics | Array<LengthMetrics>;  差异内容：tailIndents?: LengthMetrics | Array<LengthMetrics>; | component/styled\_string.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：tailIndents(value: Optional<LengthMetrics | Array<LengthMetrics>>): TextAttribute;  差异内容：tailIndents(value: Optional<LengthMetrics | Array<LengthMetrics>>): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：incrementalUpdatePolicy(policy: IncrementalUpdatePolicy | undefined): TextAttribute;  差异内容：incrementalUpdatePolicy(policy: IncrementalUpdatePolicy | undefined): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：punctuationOverflow(enabled: Optional<boolean>): TextAttribute;  差异内容：punctuationOverflow(enabled: Optional<boolean>): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：global；  API声明：type OnCreateMenuCallback = (menuItems: Array<TextMenuItem>) => Array<TextMenuItem>;  差异内容：type OnCreateMenuCallback = (menuItems: Array<TextMenuItem>) => Array<TextMenuItem>; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum StrokeJoinStyle  差异内容：declare enum StrokeJoinStyle | component/text\_common.d.ts |
| 新增API | NA | 类名：StrokeJoinStyle；  API声明：MITER\_JOIN = 0  差异内容：MITER\_JOIN = 0 | component/text\_common.d.ts |
| 新增API | NA | 类名：StrokeJoinStyle；  API声明：ROUND\_JOIN = 1  差异内容：ROUND\_JOIN = 1 | component/text\_common.d.ts |
| 新增API | NA | 类名：StrokeJoinStyle；  API声明：BEVEL\_JOIN = 2  差异内容：BEVEL\_JOIN = 2 | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum IncrementalUpdatePolicy  差异内容：declare enum IncrementalUpdatePolicy | component/text\_common.d.ts |
| 新增API | NA | 类名：IncrementalUpdatePolicy；  API声明：NONE = 0  差异内容：NONE = 0 | component/text\_common.d.ts |
| 新增API | NA | 类名：IncrementalUpdatePolicy；  API声明：PARAGRAPH\_CACHE = 1  差异内容：PARAGRAPH\_CACHE = 1 | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface AccessibilityNextFocusParams  差异内容：declare interface AccessibilityNextFocusParams | component/units.d.ts |
| 新增API | NA | 类名：AccessibilityNextFocusParams；  API声明：isConsiderDescendants?: boolean;  差异内容：isConsiderDescendants?: boolean; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface AccessibilityCustomAction  差异内容：declare interface AccessibilityCustomAction | component/units.d.ts |
| 新增API | NA | 类名：AccessibilityCustomAction；  API声明：name: ResourceStr;  差异内容：name: ResourceStr; | component/units.d.ts |
| 新增API | NA | 类名：AccessibilityCustomAction；  API声明：onAction: VoidCallback;  差异内容：onAction: VoidCallback; | component/units.d.ts |
| 删除API | 类名：global；  API声明：declare const Env: EnvDecorator;  差异内容：declare const Env: EnvDecorator; | NA | component/common.d.ts |
| 删除API | 类名：HdrType；  API声明：EDR = 2  差异内容：EDR = 2 | NA | component/xcomponent.d.ts |
| 起始版本有变化 | 类名：EllipseOptions；  API声明：width?: Length;  差异内容：7 | 类名：EllipseOptions；  API声明：width?: Length;  差异内容：18 | component/ellipse.d.ts |
| 起始版本有变化 | 类名：EllipseOptions；  API声明：height?: Length;  差异内容：7 | 类名：EllipseOptions；  API声明：height?: Length;  差异内容：18 | component/ellipse.d.ts |
| 起始版本有变化 | 类名：LineOptions；  API声明：width?: Length;  差异内容：7 | 类名：LineOptions；  API声明：width?: Length;  差异内容：18 | component/line.d.ts |
| 起始版本有变化 | 类名：LineOptions；  API声明：height?: Length;  差异内容：7 | 类名：LineOptions；  API声明：height?: Length;  差异内容：18 | component/line.d.ts |
| 起始版本有变化 | 类名：PathOptions；  API声明：width?: Length;  差异内容：7 | 类名：PathOptions；  API声明：width?: Length;  差异内容：18 | component/path.d.ts |
| 起始版本有变化 | 类名：PathOptions；  API声明：height?: Length;  差异内容：7 | 类名：PathOptions；  API声明：height?: Length;  差异内容：18 | component/path.d.ts |
| 起始版本有变化 | 类名：PathOptions；  API声明：commands?: ResourceStr;  差异内容：7 | 类名：PathOptions；  API声明：commands?: ResourceStr;  差异内容：18 | component/path.d.ts |
| 起始版本有变化 | 类名：PolygonOptions；  API声明：width?: Length;  差异内容：7 | 类名：PolygonOptions；  API声明：width?: Length;  差异内容：18 | component/polygon.d.ts |
| 起始版本有变化 | 类名：PolygonOptions；  API声明：height?: Length;  差异内容：7 | 类名：PolygonOptions；  API声明：height?: Length;  差异内容：18 | component/polygon.d.ts |
| 起始版本有变化 | 类名：PolylineOptions；  API声明：width?: Length;  差异内容：7 | 类名：PolylineOptions；  API声明：width?: Length;  差异内容：18 | component/polyline.d.ts |
| 起始版本有变化 | 类名：PolylineOptions；  API声明：height?: Length;  差异内容：7 | 类名：PolylineOptions；  API声明：height?: Length;  差异内容：18 | component/polyline.d.ts |
| 起始版本有变化 | 类名：RectOptions；  API声明：width?: Length;  差异内容：7 | 类名：RectOptions；  API声明：width?: Length;  差异内容：18 | component/rect.d.ts |
| 起始版本有变化 | 类名：RectOptions；  API声明：height?: Length;  差异内容：7 | 类名：RectOptions；  API声明：height?: Length;  差异内容：18 | component/rect.d.ts |
| 起始版本有变化 | 类名：RectOptions；  API声明：radius?: Length | Array<any>;  差异内容：7 | 类名：RectOptions；  API声明：radius?: Length | Array<any>;  差异内容：18 | component/rect.d.ts |
| 起始版本有变化 | 类名：RoundedRectOptions；  API声明：width?: Length;  差异内容：7 | 类名：RoundedRectOptions；  API声明：width?: Length;  差异内容：18 | component/rect.d.ts |
| 起始版本有变化 | 类名：RoundedRectOptions；  API声明：height?: Length;  差异内容：7 | 类名：RoundedRectOptions；  API声明：height?: Length;  差异内容：18 | component/rect.d.ts |
| 起始版本有变化 | 类名：RoundedRectOptions；  API声明：radiusWidth?: Length;  差异内容：7 | 类名：RoundedRectOptions；  API声明：radiusWidth?: Length;  差异内容：18 | component/rect.d.ts |
| 起始版本有变化 | 类名：RoundedRectOptions；  API声明：radiusHeight?: Length;  差异内容：7 | 类名：RoundedRectOptions；  API声明：radiusHeight?: Length;  差异内容：18 | component/rect.d.ts |
| 起始版本有变化 | 类名：ViewportRect；  API声明：x?: Length;  差异内容：7 | 类名：ViewportRect；  API声明：x?: Length;  差异内容：18 | component/shape.d.ts |
| 起始版本有变化 | 类名：ViewportRect；  API声明：y?: Length;  差异内容：7 | 类名：ViewportRect；  API声明：y?: Length;  差异内容：18 | component/shape.d.ts |
| 起始版本有变化 | 类名：ViewportRect；  API声明：width?: Length;  差异内容：7 | 类名：ViewportRect；  API声明：width?: Length;  差异内容：18 | component/shape.d.ts |
| 起始版本有变化 | 类名：ViewportRect；  API声明：height?: Length;  差异内容：7 | 类名：ViewportRect；  API声明：height?: Length;  差异内容：18 | component/shape.d.ts |
| 起始版本有变化 | 类名：VideoAttribute；  API声明：loop(value: boolean): VideoAttribute;  差异内容：6 | 类名：VideoAttribute；  API声明：loop(value: boolean): VideoAttribute;  差异内容：7 | component/video.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.arkui.advanced.ChipGroupV2.d.ets  差异内容：ArkUI | api/@ohos.arkui.advanced.ChipGroupV2.d.ets |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.arkui.advanced.ChipV2.d.ets  差异内容：ArkUI | api/@ohos.arkui.advanced.ChipV2.d.ets |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.arkui.advanced.ComposeListItemV2.d.ets  差异内容：ArkUI | api/@ohos.arkui.advanced.ComposeListItemV2.d.ets |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.arkui.advanced.ComposeTitleBarV2.d.ets  差异内容：ArkUI | api/@ohos.arkui.advanced.ComposeTitleBarV2.d.ets |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.arkui.advanced.CounterV2.d.ets  差异内容：ArkUI | api/@ohos.arkui.advanced.CounterV2.d.ets |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.arkui.advanced.DatePickerComponent.d.ets  差异内容：ArkUI | api/@ohos.arkui.advanced.DatePickerComponent.d.ets |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.arkui.advanced.EditableTitleBarV2.d.ets  差异内容：ArkUI | api/@ohos.arkui.advanced.EditableTitleBarV2.d.ets |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.arkui.advanced.ExceptionPromptV2.d.ets  差异内容：ArkUI | api/@ohos.arkui.advanced.ExceptionPromptV2.d.ets |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.arkui.advanced.SwipeRefresherV2.d.ets  差异内容：ArkUI | api/@ohos.arkui.advanced.SwipeRefresherV2.d.ets |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.arkui.advanced.TreeViewV2.d.ets  差异内容：ArkUI | api/@ohos.arkui.advanced.TreeViewV2.d.ets |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.arkui.components.ArkLazyColumnLayout.d.ts  差异内容：ArkUI | api/@ohos.arkui.components.ArkLazyColumnLayout.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.arkui.components.ArkLazyDynamicLayout.d.ts  差异内容：ArkUI | api/@ohos.arkui.components.ArkLazyDynamicLayout.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.arkui.components.SelectionContainer.d.ts  差异内容：ArkUI | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.arkui.lazyLayoutAlgorithm.d.ts  差异内容：ArkUI | api/@ohos.arkui.lazyLayoutAlgorithm.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.arkui.WithEnv.d.ts  差异内容：ArkUI | api/@ohos.arkui.WithEnv.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\arkui\ContainerReaderModifier.d.ts  差异内容：ArkUI | api/arkui/ContainerReaderModifier.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\arkui\LazyLayoutAlgorithm.d.ts  差异内容：ArkUI | api/arkui/LazyLayoutAlgorithm.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\arkui\SelectionContainerModifier.d.ts  差异内容：ArkUI | api/arkui/SelectionContainerModifier.d.ts |
| API从不支持元服务到支持元服务 | 类名：SystemProperties；  API声明：WINDOW\_AVOID\_AREA = 'system.window.avoidarea'  差异内容：NA | 类名：SystemProperties；  API声明：WINDOW\_AVOID\_AREA = 'system.window.avoidarea'  差异内容：atomicservice | component/common.d.ts |
| API从不支持元服务到支持元服务 | 类名：SystemProperties；  API声明：WINDOW\_AVOID\_AREA\_PX = 'system.window.avoidarea.px'  差异内容：NA | 类名：SystemProperties；  API声明：WINDOW\_AVOID\_AREA\_PX = 'system.window.avoidarea.px'  差异内容：atomicservice | component/common.d.ts |
| API从不支持元服务到支持元服务 | 类名：SystemProperties；  API声明：WINDOW\_SIZE = 'system.window.size'  差异内容：NA | 类名：SystemProperties；  API声明：WINDOW\_SIZE = 'system.window.size'  差异内容：atomicservice | component/common.d.ts |
| API从不支持元服务到支持元服务 | 类名：SystemProperties；  API声明：WINDOW\_SIZE\_PX = 'system.window.size.px'  差异内容：NA | 类名：SystemProperties；  API声明：WINDOW\_SIZE\_PX = 'system.window.size.px'  差异内容：atomicservice | component/common.d.ts |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：interface RichTextInterface  差异内容：NA | 类名：global；  API声明：interface RichTextInterface  差异内容：atomicservice | component/rich\_text.d.ts |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：declare class RichTextAttribute  差异内容：NA | 类名：global；  API声明：declare class RichTextAttribute  差异内容：atomicservice | component/rich\_text.d.ts |
| API从不支持元服务到支持元服务 | 类名：RichTextAttribute；  API声明：onStart(callback: () => void): RichTextAttribute;  差异内容：NA | 类名：RichTextAttribute；  API声明：onStart(callback: () => void): RichTextAttribute;  差异内容：atomicservice | component/rich\_text.d.ts |
| API从不支持元服务到支持元服务 | 类名：RichTextAttribute；  API声明：onComplete(callback: () => void): RichTextAttribute;  差异内容：NA | 类名：RichTextAttribute；  API声明：onComplete(callback: () => void): RichTextAttribute;  差异内容：atomicservice | component/rich\_text.d.ts |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：declare const RichText: RichTextInterface;  差异内容：NA | 类名：global；  API声明：declare const RichText: RichTextInterface;  差异内容：atomicservice | component/rich\_text.d.ts |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：declare const RichTextInstance: RichTextAttribute;  差异内容：NA | 类名：global；  API声明：declare const RichTextInstance: RichTextAttribute;  差异内容：atomicservice | component/rich\_text.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：FrameNode；  API声明：getChildrenCount(): number;  差异内容：getChildrenCount(): number; | 类名：FrameNode；  API声明：getChildrenCount(countMode?: ChildrenCountMode): number;  差异内容：getChildrenCount(countMode?: ChildrenCountMode): number; | api/arkui/FrameNode.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：CommonMethod；  API声明：bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | undefined, options?: ContextMenuOptions): T;  差异内容：bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | undefined, options?: ContextMenuOptions): T; | 类名：CommonMethod；  API声明：bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | Array<MenuElement> | undefined, options?: ContextMenuOptions): T;  差异内容：bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | Array<MenuElement> | undefined, options?: ContextMenuOptions): T; | component/common.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：CommonMethod；  API声明：accessibilityNextFocusId(nextId: string): T;  差异内容：accessibilityNextFocusId(nextId: string): T; | 类名：CommonMethod；  API声明：accessibilityNextFocusId(nextId: string, nextFocusParams: AccessibilityNextFocusParams | undefined): T;  差异内容：accessibilityNextFocusId(nextId: string, nextFocusParams: AccessibilityNextFocusParams | undefined): T; | component/common.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：ImageAttribute；  API声明：colorFilter(value: ColorFilter | DrawingColorFilter): ImageAttribute;  差异内容：colorFilter(value: ColorFilter | DrawingColorFilter): ImageAttribute; | 类名：ImageAttribute；  API声明：colorFilter(value: ColorFilter | DrawingColorFilter | ResourceColor): ImageAttribute;  差异内容：colorFilter(value: ColorFilter | DrawingColorFilter | ResourceColor): ImageAttribute; | component/image.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围不是包含关系 | 类名：SymbolGlyphAttribute；  API声明：fontWeight(value: number | FontWeight | string): SymbolGlyphAttribute;  差异内容：fontWeight(value: number | FontWeight | string): SymbolGlyphAttribute; | 类名：SymbolGlyphAttribute；  API声明：fontWeight(value: number | FontWeight | ResourceStr, fontWeightConfigs?: FontWeightConfigs): SymbolGlyphAttribute;  差异内容：fontWeight(value: number | FontWeight | ResourceStr, fontWeightConfigs?: FontWeightConfigs): SymbolGlyphAttribute; | component/symbolglyph.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围不是包含关系 | 类名：SymbolSpanAttribute；  API声明：fontWeight(value: number | FontWeight | string): SymbolSpanAttribute;  差异内容：fontWeight(value: number | FontWeight | string): SymbolSpanAttribute; | 类名：SymbolSpanAttribute；  API声明：fontWeight(value: number | FontWeight | ResourceStr, fontWeightConfigs?: FontWeightConfigs): SymbolSpanAttribute;  差异内容：fontWeight(value: number | FontWeight | ResourceStr, fontWeightConfigs?: FontWeightConfigs): SymbolSpanAttribute; | component/symbol\_span.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Window；  API声明：recover(): Promise<void>;  差异内容：recover(): Promise<void>; | 类名：Window；  API声明：recover(snapshotAnimationConfig: WindowSnapshotAnimationConfig): Promise<void>;  差异内容：recover(snapshotAnimationConfig: WindowSnapshotAnimationConfig): Promise<void>; | api/@ohos.window.d.ts |
