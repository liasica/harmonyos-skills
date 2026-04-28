---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-6021
title: ArkUI
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > ArkUI
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:43+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:4ab75feacc16359c9f5e5f711f0b13fe5794f04102f589d7006429a5db1c61c1
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：global；  API声明：export declare class StepperItemModifier  差异内容：NA | 类名：global；  API声明：export declare class StepperItemModifier  差异内容：22 | api/arkui/StepperItemModifier.d.ts |
| API废弃版本变更 | 类名：StepperItemModifier；  API声明：applyNormalAttribute?(instance: StepperItemAttribute): void;  差异内容：NA | 类名：StepperItemModifier；  API声明：applyNormalAttribute?(instance: StepperItemAttribute): void;  差异内容：22 | api/arkui/StepperItemModifier.d.ts |
| API废弃版本变更 | 类名：global；  API声明：export declare class StepperModifier  差异内容：NA | 类名：global；  API声明：export declare class StepperModifier  差异内容：22 | api/arkui/StepperModifier.d.ts |
| API废弃版本变更 | 类名：StepperModifier；  API声明：applyNormalAttribute?(instance: StepperAttribute): void;  差异内容：NA | 类名：StepperModifier；  API声明：applyNormalAttribute?(instance: StepperAttribute): void;  差异内容：22 | api/arkui/StepperModifier.d.ts |
| API废弃版本变更 | 类名：global；  API声明：declare enum ItemState  差异内容：NA | 类名：global；  API声明：declare enum ItemState  差异内容：22 | component/stepper\_item.d.ts |
| API废弃版本变更 | 类名：ItemState；  API声明：Normal  差异内容：NA | 类名：ItemState；  API声明：Normal  差异内容：22 | component/stepper\_item.d.ts |
| API废弃版本变更 | 类名：ItemState；  API声明：Disabled  差异内容：NA | 类名：ItemState；  API声明：Disabled  差异内容：22 | component/stepper\_item.d.ts |
| API废弃版本变更 | 类名：ItemState；  API声明：Waiting  差异内容：NA | 类名：ItemState；  API声明：Waiting  差异内容：22 | component/stepper\_item.d.ts |
| API废弃版本变更 | 类名：ItemState；  API声明：Skip  差异内容：NA | 类名：ItemState；  API声明：Skip  差异内容：22 | component/stepper\_item.d.ts |
| API废弃版本变更 | 类名：global；  API声明：interface StepperItemInterface  差异内容：NA | 类名：global；  API声明：interface StepperItemInterface  差异内容：22 | component/stepper\_item.d.ts |
| API废弃版本变更 | 类名：global；  API声明：declare class StepperItemAttribute  差异内容：NA | 类名：global；  API声明：declare class StepperItemAttribute  差异内容：22 | component/stepper\_item.d.ts |
| API废弃版本变更 | 类名：StepperItemAttribute；  API声明：prevLabel(value: string): StepperItemAttribute;  差异内容：NA | 类名：StepperItemAttribute；  API声明：prevLabel(value: string): StepperItemAttribute;  差异内容：22 | component/stepper\_item.d.ts |
| API废弃版本变更 | 类名：StepperItemAttribute；  API声明：nextLabel(value: string): StepperItemAttribute;  差异内容：NA | 类名：StepperItemAttribute；  API声明：nextLabel(value: string): StepperItemAttribute;  差异内容：22 | component/stepper\_item.d.ts |
| API废弃版本变更 | 类名：StepperItemAttribute；  API声明：status(value?: ItemState): StepperItemAttribute;  差异内容：NA | 类名：StepperItemAttribute；  API声明：status(value?: ItemState): StepperItemAttribute;  差异内容：22 | component/stepper\_item.d.ts |
| API废弃版本变更 | 类名：global；  API声明：declare const StepperItemInstance: StepperItemAttribute;  差异内容：NA | 类名：global；  API声明：declare const StepperItemInstance: StepperItemAttribute;  差异内容：22 | component/stepper\_item.d.ts |
| API废弃版本变更 | 类名：global；  API声明：declare const StepperItem: StepperItemInterface;  差异内容：NA | 类名：global；  API声明：declare const StepperItem: StepperItemInterface;  差异内容：22 | component/stepper\_item.d.ts |
| API废弃版本变更 | 类名：global；  API声明：interface StepperInterface  差异内容：NA | 类名：global；  API声明：interface StepperInterface  差异内容：22 | component/stepper.d.ts |
| API废弃版本变更 | 类名：global；  API声明：declare class StepperAttribute  差异内容：NA | 类名：global；  API声明：declare class StepperAttribute  差异内容：22 | component/stepper.d.ts |
| API废弃版本变更 | 类名：StepperAttribute；  API声明：onFinish(callback: () => void): StepperAttribute;  差异内容：NA | 类名：StepperAttribute；  API声明：onFinish(callback: () => void): StepperAttribute;  差异内容：22 | component/stepper.d.ts |
| API废弃版本变更 | 类名：StepperAttribute；  API声明：onSkip(callback: () => void): StepperAttribute;  差异内容：NA | 类名：StepperAttribute；  API声明：onSkip(callback: () => void): StepperAttribute;  差异内容：22 | component/stepper.d.ts |
| API废弃版本变更 | 类名：StepperAttribute；  API声明：onChange(callback: (prevIndex: number, index: number) => void): StepperAttribute;  差异内容：NA | 类名：StepperAttribute；  API声明：onChange(callback: (prevIndex: number, index: number) => void): StepperAttribute;  差异内容：22 | component/stepper.d.ts |
| API废弃版本变更 | 类名：StepperAttribute；  API声明：onNext(callback: (index: number, pendingIndex: number) => void): StepperAttribute;  差异内容：NA | 类名：StepperAttribute；  API声明：onNext(callback: (index: number, pendingIndex: number) => void): StepperAttribute;  差异内容：22 | component/stepper.d.ts |
| API废弃版本变更 | 类名：StepperAttribute；  API声明：onPrevious(callback: (index: number, pendingIndex: number) => void): StepperAttribute;  差异内容：NA | 类名：StepperAttribute；  API声明：onPrevious(callback: (index: number, pendingIndex: number) => void): StepperAttribute;  差异内容：22 | component/stepper.d.ts |
| API废弃版本变更 | 类名：global；  API声明：declare const Stepper: StepperInterface;  差异内容：NA | 类名：global；  API声明：declare const Stepper: StepperInterface;  差异内容：22 | component/stepper.d.ts |
| API废弃版本变更 | 类名：global；  API声明：declare const StepperInstance: StepperAttribute;  差异内容：NA | 类名：global；  API声明：declare const StepperInstance: StepperAttribute;  差异内容：22 | component/stepper.d.ts |
| 新增错误码 | 类名：FrameNode；  API声明：appendChild(node: FrameNode): void;  差异内容：NA | 类名：FrameNode；  API声明：appendChild(node: FrameNode): void;  差异内容：100025 | api/arkui/FrameNode.d.ts |
| 新增错误码 | 类名：FrameNode；  API声明：insertChildAfter(child: FrameNode, sibling: FrameNode | null): void;  差异内容：NA | 类名：FrameNode；  API声明：insertChildAfter(child: FrameNode, sibling: FrameNode | null): void;  差异内容：100025 | api/arkui/FrameNode.d.ts |
| 新增错误码 | 类名：FrameNode；  API声明：moveTo(targetParent: FrameNode, index?: number): void;  差异内容：NA | 类名：FrameNode；  API声明：moveTo(targetParent: FrameNode, index?: number): void;  差异内容：100027 | api/arkui/FrameNode.d.ts |
| 新增错误码 | 类名：NodeContent；  API声明：addFrameNode(node: FrameNode): void;  差异内容：NA | 类名：NodeContent；  API声明：addFrameNode(node: FrameNode): void;  差异内容：100025 | api/arkui/NodeContent.d.ts |
| 新增错误码 | 类名：RenderNode；  API声明：appendChild(node: RenderNode): void;  差异内容：NA | 类名：RenderNode；  API声明：appendChild(node: RenderNode): void;  差异内容：100025 | api/arkui/RenderNode.d.ts |
| 新增错误码 | 类名：RenderNode；  API声明：insertChildAfter(child: RenderNode, sibling: RenderNode | null): void;  差异内容：NA | 类名：RenderNode；  API声明：insertChildAfter(child: RenderNode, sibling: RenderNode | null): void;  差异内容：100025 | api/arkui/RenderNode.d.ts |
| 删除错误码 | 类名：screenshot；  API声明：function capture(options?: CaptureOption): Promise<image.PixelMap>;  差异内容：401 | 类名：screenshot；  API声明：function capture(options?: CaptureOption): Promise<image.PixelMap>;  差异内容：NA | api/@ohos.screenshot.d.ts |
| 权限变更 | 类名：screenshot；  API声明：function capture(options?: CaptureOption): Promise<image.PixelMap>;  差异内容：ohos.permission.CUSTOM\_SCREEN\_CAPTURE | 类名：screenshot；  API声明：function capture(options?: CaptureOption): Promise<image.PixelMap>;  差异内容：ohos.permission.CUSTOM\_SCREEN\_CAPTURE or ohos.permission.CUSTOM\_SCREEN\_RECORDING | api/@ohos.screenshot.d.ts |
| 函数变更 | 类名：FrameNode；  API声明：addComponentContent<T>(content: ComponentContent<T>): void;  差异内容：content: ComponentContent<T> | 类名：FrameNode；  API声明：addComponentContent<T>(content: ComponentContent<T> | ReactiveComponentContent<T>): void;  差异内容：content: ComponentContent<T> | ReactiveComponentContent<T> | api/arkui/FrameNode.d.ts |
| 函数变更 | 类名：SearchAttribute；  API声明：customKeyboard(value: CustomBuilder, options?: KeyboardOptions): SearchAttribute;  差异内容：value: CustomBuilder | 类名：SearchAttribute；  API声明：customKeyboard(value: CustomBuilder | ComponentContent | undefined, options?: KeyboardOptions): SearchAttribute;  差异内容：value: CustomBuilder | ComponentContent | undefined | component/search.d.ts |
| 函数变更 | 类名：TextAreaAttribute；  API声明：customKeyboard(value: CustomBuilder, options?: KeyboardOptions): TextAreaAttribute;  差异内容：value: CustomBuilder | 类名：TextAreaAttribute；  API声明：customKeyboard(value: CustomBuilder | ComponentContent | undefined, options?: KeyboardOptions): TextAreaAttribute;  差异内容：value: CustomBuilder | ComponentContent | undefined | component/text\_area.d.ts |
| 函数变更 | 类名：TextInputAttribute；  API声明：customKeyboard(value: CustomBuilder, options?: KeyboardOptions): TextInputAttribute;  差异内容：value: CustomBuilder | 类名：TextInputAttribute；  API声明：customKeyboard(value: CustomBuilder | ComponentContent | undefined, options?: KeyboardOptions): TextInputAttribute;  差异内容：value: CustomBuilder | ComponentContent | undefined | component/text\_input.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare class UIPickerComponentModifier  差异内容：export declare class UIPickerComponentModifier | api/arkui/UIPickerComponentModifier.d.ts |
| 新增API | NA | 类名：UIPickerComponentModifier；  API声明：applyNormalAttribute?(instance: UIPickerComponentAttribute): void;  差异内容：applyNormalAttribute?(instance: UIPickerComponentAttribute): void; | api/arkui/UIPickerComponentModifier.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface UIPickerComponentOptions  差异内容：declare interface UIPickerComponentOptions | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：UIPickerComponentOptions；  API声明：selectedIndex?: number;  差异内容：selectedIndex?: number; | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：global；  API声明：interface UIPickerComponentInterface  差异内容：interface UIPickerComponentInterface | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type OnUIPickerComponentCallback = (selectedIndex: number) => void;  差异内容：declare type OnUIPickerComponentCallback = (selectedIndex: number) => void; | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum PickerIndicatorType  差异内容：declare enum PickerIndicatorType | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：PickerIndicatorType；  API声明：BACKGROUND = 0  差异内容：BACKGROUND = 0 | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：PickerIndicatorType；  API声明：DIVIDER = 1  差异内容：DIVIDER = 1 | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface PickerIndicatorStyle  差异内容：declare interface PickerIndicatorStyle | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：PickerIndicatorStyle；  API声明：type: PickerIndicatorType;  差异内容：type: PickerIndicatorType; | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：PickerIndicatorStyle；  API声明：strokeWidth?: LengthMetrics;  差异内容：strokeWidth?: LengthMetrics; | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：PickerIndicatorStyle；  API声明：dividerColor?: ResourceColor;  差异内容：dividerColor?: ResourceColor; | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：PickerIndicatorStyle；  API声明：startMargin?: LengthMetrics;  差异内容：startMargin?: LengthMetrics; | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：PickerIndicatorStyle；  API声明：endMargin?: LengthMetrics;  差异内容：endMargin?: LengthMetrics; | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：PickerIndicatorStyle；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：PickerIndicatorStyle；  API声明：borderRadius?: LengthMetrics | BorderRadiuses | LocalizedBorderRadiuses;  差异内容：borderRadius?: LengthMetrics | BorderRadiuses | LocalizedBorderRadiuses; | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class UIPickerComponentAttribute  差异内容：declare class UIPickerComponentAttribute | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：UIPickerComponentAttribute；  API声明：onChange(callback: Optional<OnUIPickerComponentCallback>): UIPickerComponentAttribute;  差异内容：onChange(callback: Optional<OnUIPickerComponentCallback>): UIPickerComponentAttribute; | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：UIPickerComponentAttribute；  API声明：onScrollStop(callback: Optional<OnUIPickerComponentCallback>): UIPickerComponentAttribute;  差异内容：onScrollStop(callback: Optional<OnUIPickerComponentCallback>): UIPickerComponentAttribute; | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：UIPickerComponentAttribute；  API声明：canLoop(isLoop: Optional<boolean>): UIPickerComponentAttribute;  差异内容：canLoop(isLoop: Optional<boolean>): UIPickerComponentAttribute; | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：UIPickerComponentAttribute；  API声明：enableHapticFeedback(enable: Optional<boolean>): UIPickerComponentAttribute;  差异内容：enableHapticFeedback(enable: Optional<boolean>): UIPickerComponentAttribute; | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：UIPickerComponentAttribute；  API声明：selectionIndicator(style: Optional<PickerIndicatorStyle>): UIPickerComponentAttribute;  差异内容：selectionIndicator(style: Optional<PickerIndicatorStyle>): UIPickerComponentAttribute; | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const UIPickerComponent: UIPickerComponentInterface;  差异内容：declare const UIPickerComponent: UIPickerComponentInterface; | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const UIPickerComponentInstance: UIPickerComponentAttribute;  差异内容：declare const UIPickerComponentInstance: UIPickerComponentAttribute; | component/ui\_picker\_component.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：on(type: 'tabChange', config: observer.ObserverOptions, callback: Callback<observer.TabContentInfo>): void;  差异内容：on(type: 'tabChange', config: observer.ObserverOptions, callback: Callback<observer.TabContentInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：on(type: 'tabChange', callback: Callback<observer.TabContentInfo>): void;  差异内容：on(type: 'tabChange', callback: Callback<observer.TabContentInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：off(type: 'tabChange', config: observer.ObserverOptions, callback?: Callback<observer.TabContentInfo>): void;  差异内容：off(type: 'tabChange', config: observer.ObserverOptions, callback?: Callback<observer.TabContentInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：off(type: 'tabChange', callback?: Callback<observer.TabContentInfo>): void;  差异内容：off(type: 'tabChange', callback?: Callback<observer.TabContentInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：on(type: 'windowSizeLayoutBreakpointChange', callback: Callback<observer.WindowSizeLayoutBreakpointInfo>): void;  差异内容：on(type: 'windowSizeLayoutBreakpointChange', callback: Callback<observer.WindowSizeLayoutBreakpointInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：off(type: 'windowSizeLayoutBreakpointChange', callback?: Callback<observer.WindowSizeLayoutBreakpointInfo>): void;  差异内容：off(type: 'windowSizeLayoutBreakpointChange', callback?: Callback<observer.WindowSizeLayoutBreakpointInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：on(type: 'textChange', callback: Callback<observer.TextChangeEventInfo>): void;  差异内容：on(type: 'textChange', callback: Callback<observer.TextChangeEventInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：on(type: 'textChange', identity: observer.ObserverOptions, callback: Callback<observer.TextChangeEventInfo>): void;  差异内容：on(type: 'textChange', identity: observer.ObserverOptions, callback: Callback<observer.TextChangeEventInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：off(type: 'textChange', callback?: Callback<observer.TextChangeEventInfo>): void;  差异内容：off(type: 'textChange', callback?: Callback<observer.TextChangeEventInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：off(type: 'textChange', identity: observer.ObserverOptions, callback?: Callback<observer.TextChangeEventInfo>): void;  差异内容：off(type: 'textChange', identity: observer.ObserverOptions, callback?: Callback<observer.TextChangeEventInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：onSwiperContentUpdate(callback: Callback<SwiperContentInfo>): void;  差异内容：onSwiperContentUpdate(callback: Callback<SwiperContentInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：onSwiperContentUpdate(config: observer.ObserverOptions, callback: Callback<SwiperContentInfo>): void;  差异内容：onSwiperContentUpdate(config: observer.ObserverOptions, callback: Callback<SwiperContentInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：offSwiperContentUpdate(callback?: Callback<SwiperContentInfo>): void;  差异内容：offSwiperContentUpdate(callback?: Callback<SwiperContentInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：offSwiperContentUpdate(config: observer.ObserverOptions, callback?: Callback<SwiperContentInfo>): void;  差异内容：offSwiperContentUpdate(config: observer.ObserverOptions, callback?: Callback<SwiperContentInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface SwiperContentInfo  差异内容：export interface SwiperContentInfo | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：SwiperContentInfo；  API声明：id: string;  差异内容：id: string; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：SwiperContentInfo；  API声明：uniqueId: number;  差异内容：uniqueId: number; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：SwiperContentInfo；  API声明：swiperItemInfos: Array<SwiperItemInfo>;  差异内容：swiperItemInfos: Array<SwiperItemInfo>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface SwiperItemInfo  差异内容：export interface SwiperItemInfo | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：SwiperItemInfo；  API声明：uniqueId: number;  差异内容：uniqueId: number; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：SwiperItemInfo；  API声明：index: number;  差异内容：index: number; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：export class Magnifier  差异内容：export class Magnifier | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Magnifier；  API声明：bind(id: string): void;  差异内容：bind(id: string): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Magnifier；  API声明：show(x: number, y: number): void;  差异内容：show(x: number, y: number): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Magnifier；  API声明：unbind(): void;  差异内容：unbind(): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：export const enum ResolveStrategy  差异内容：export const enum ResolveStrategy | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：ResolveStrategy；  API声明：CALLING\_SCOPE = 0  差异内容：CALLING\_SCOPE = 0 | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：ResolveStrategy；  API声明：LAST\_FOCUS = 1  差异内容：LAST\_FOCUS = 1 | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：ResolveStrategy；  API声明：MAX\_INSTANCE\_ID = 2  差异内容：MAX\_INSTANCE\_ID = 2 | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：ResolveStrategy；  API声明：UNIQUE = 3  差异内容：UNIQUE = 3 | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：ResolveStrategy；  API声明：LAST\_FOREGROUND = 4  差异内容：LAST\_FOREGROUND = 4 | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：ResolveStrategy；  API声明：UNDEFINED = 5  差异内容：UNDEFINED = 5 | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：export class ResolvedUIContext  差异内容：export class ResolvedUIContext | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：ResolvedUIContext；  API声明：strategy: ResolveStrategy;  差异内容：strategy: ResolveStrategy; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：static getCallingScopeUIContext(): UIContext | undefined;  差异内容：static getCallingScopeUIContext(): UIContext | undefined; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：static getLastFocusedUIContext(): UIContext | undefined;  差异内容：static getLastFocusedUIContext(): UIContext | undefined; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：static getLastForegroundUIContext(): UIContext | undefined;  差异内容：static getLastForegroundUIContext(): UIContext | undefined; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：static getAllUIContexts(): UIContext[];  差异内容：static getAllUIContexts(): UIContext[]; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：static resolveUIContext(): ResolvedUIContext;  差异内容：static resolveUIContext(): ResolvedUIContext; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getMagnifier(): Magnifier;  差异内容：getMagnifier(): Magnifier; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getId(): number;  差异内容：getId(): number; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：window；  API声明：enum PixelUnit  差异内容：enum PixelUnit | api/@ohos.window.d.ts |
| 新增API | NA | 类名：PixelUnit；  API声明：PX = 0  差异内容：PX = 0 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：PixelUnit；  API声明：VP = 1  差异内容：VP = 1 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：interface FrameMetrics  差异内容：interface FrameMetrics | api/@ohos.window.d.ts |
| 新增API | NA | 类名：FrameMetrics；  API声明：firstDrawFrame: boolean;  差异内容：firstDrawFrame: boolean; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：FrameMetrics；  API声明：inputHandlingDuration: number;  差异内容：inputHandlingDuration: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：FrameMetrics；  API声明：layoutMeasureDuration: number;  差异内容：layoutMeasureDuration: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：FrameMetrics；  API声明：vsyncTimestamp: number;  差异内容：vsyncTimestamp: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowLimits；  API声明：pixelUnit?: PixelUnit;  差异内容：pixelUnit?: PixelUnit; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：getWindowAvoidAreaIgnoringVisibility(type: AvoidAreaType): AvoidArea;  差异内容：getWindowAvoidAreaIgnoringVisibility(type: AvoidAreaType): AvoidArea; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：on(type: 'occlusionStateChanged', callback: Callback<OcclusionState>): void;  差异内容：on(type: 'occlusionStateChanged', callback: Callback<OcclusionState>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：off(type: 'occlusionStateChanged', callback?: Callback<OcclusionState>): void;  差异内容：off(type: 'occlusionStateChanged', callback?: Callback<OcclusionState>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：on(type: 'frameMetricsMeasured', callback: Callback<FrameMetrics>): void;  差异内容：on(type: 'frameMetricsMeasured', callback: Callback<FrameMetrics>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：off(type: 'frameMetricsMeasured', callback?: Callback<FrameMetrics>): void;  差异内容：off(type: 'frameMetricsMeasured', callback?: Callback<FrameMetrics>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：getWindowLimitsVP(): WindowLimits;  差异内容：getWindowLimitsVP(): WindowLimits; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：isInFreeWindowMode(): boolean;  差异内容：isInFreeWindowMode(): boolean; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：on(type: 'freeWindowModeChange', callback: Callback<boolean>): void;  差异内容：on(type: 'freeWindowModeChange', callback: Callback<boolean>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：off(type: 'freeWindowModeChange', callback?: Callback<boolean>): void;  差异内容：off(type: 'freeWindowModeChange', callback?: Callback<boolean>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：enum OcclusionState  差异内容：enum OcclusionState | api/@ohos.window.d.ts |
| 新增API | NA | 类名：OcclusionState；  API声明：NO\_OCCLUSION = 0  差异内容：NO\_OCCLUSION = 0 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：OcclusionState；  API声明：PARTIAL\_OCCLUSION = 1  差异内容：PARTIAL\_OCCLUSION = 1 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：OcclusionState；  API声明：FULL\_OCCLUSION = 2  差异内容：FULL\_OCCLUSION = 2 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：convertPosition(position: Position, targetNode: FrameNode): Position;  差异内容：convertPosition(position: Position, targetNode: FrameNode): Position; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：adoptChild(child: FrameNode): void;  差异内容：adoptChild(child: FrameNode): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：removeAdoptedChild(child: FrameNode): void;  差异内容：removeAdoptedChild(child: FrameNode): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：InputCounterOptions；  API声明：counterTextColor?: ColorMetrics;  差异内容：counterTextColor?: ColorMetrics; | component/common.d.ts |
| 新增API | NA | 类名：InputCounterOptions；  API声明：counterTextOverflowColor?: ColorMetrics;  差异内容：counterTextOverflowColor?: ColorMetrics; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type EnvDecorator = (value: SystemProperties) => PropertyDecorator;  差异内容：declare type EnvDecorator = (value: SystemProperties) => PropertyDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const Env: EnvDecorator;  差异内容：declare const Env: EnvDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum SystemProperties  差异内容：declare enum SystemProperties | component/common.d.ts |
| 新增API | NA | 类名：SystemProperties；  API声明：BREAK\_POINT = 'system.arkui.breakpoint'  差异内容：BREAK\_POINT = 'system.arkui.breakpoint' | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface ResponseRegion  差异内容：declare interface ResponseRegion | component/common.d.ts |
| 新增API | NA | 类名：ResponseRegion；  API声明：tool?: ResponseRegionSupportedTool;  差异内容：tool?: ResponseRegionSupportedTool; | component/common.d.ts |
| 新增API | NA | 类名：ResponseRegion；  API声明：x?: LengthMetrics;  差异内容：x?: LengthMetrics; | component/common.d.ts |
| 新增API | NA | 类名：ResponseRegion；  API声明：y?: LengthMetrics;  差异内容：y?: LengthMetrics; | component/common.d.ts |
| 新增API | NA | 类名：ResponseRegion；  API声明：width?: LengthMetrics | string;  差异内容：width?: LengthMetrics | string; | component/common.d.ts |
| 新增API | NA | 类名：ResponseRegion；  API声明：height?: LengthMetrics | string;  差异内容：height?: LengthMetrics | string; | component/common.d.ts |
| 新增API | NA | 类名：SourceType；  API声明：KEY = 4  差异内容：KEY = 4 | component/common.d.ts |
| 新增API | NA | 类名：SourceType；  API声明：JOYSTICK = 5  差异内容：JOYSTICK = 5 | component/common.d.ts |
| 新增API | NA | 类名：AxisEvent；  API声明：hasAxis(axisType: AxisType): boolean;  差异内容：hasAxis(axisType: AxisType): boolean; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：responseRegionList(regions: Array<ResponseRegion>): T;  差异内容：responseRegionList(regions: Array<ResponseRegion>): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback, measureFromViewport: boolean): T;  差异内容：onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback, measureFromViewport: boolean): T; | component/common.d.ts |
| 新增API | NA | 类名：TextContentControllerBase；  API声明：setStyledPlaceholder(styledString: StyledString): void;  差异内容：setStyledPlaceholder(styledString: StyledString): void; | component/common.d.ts |
| 新增API | NA | 类名：ScrollableCommonMethod；  API声明：contentStartOffset(offset: number | Resource): T;  差异内容：contentStartOffset(offset: number | Resource): T; | component/common.d.ts |
| 新增API | NA | 类名：ScrollableCommonMethod；  API声明：contentEndOffset(offset: number | Resource): T;  差异内容：contentEndOffset(offset: number | Resource): T; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type BuilderCallback = (...args: Args) => void;  差异内容：declare type BuilderCallback = (...args: Args) => void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare function mutableBuilder<Args extends Object[]>(builder: BuilderCallback): MutableBuilder<Args>;  差异内容：declare function mutableBuilder<Args extends Object[]>(builder: BuilderCallback): MutableBuilder<Args>; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class MutableBuilder  差异内容：declare class MutableBuilder | component/common.d.ts |
| 新增API | NA | 类名：VisibleAreaEventOptions；  API声明：measureFromViewport?: boolean;  差异内容：measureFromViewport?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum RenderStrategy  差异内容：declare enum RenderStrategy | component/enums.d.ts |
| 新增API | NA | 类名：RenderStrategy；  API声明：FAST = 0  差异内容：FAST = 0 | component/enums.d.ts |
| 新增API | NA | 类名：RenderStrategy；  API声明：OFFSCREEN = 1  差异内容：OFFSCREEN = 1 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum PresetFillType  差异内容：declare enum PresetFillType | component/enums.d.ts |
| 新增API | NA | 类名：PresetFillType；  API声明：BREAKPOINT\_DEFAULT = 0  差异内容：BREAKPOINT\_DEFAULT = 0 | component/enums.d.ts |
| 新增API | NA | 类名：PresetFillType；  API声明：BREAKPOINT\_SM1MD2LG3 = 1  差异内容：BREAKPOINT\_SM1MD2LG3 = 1 | component/enums.d.ts |
| 新增API | NA | 类名：PresetFillType；  API声明：BREAKPOINT\_SM2MD3LG5 = 2  差异内容：BREAKPOINT\_SM2MD3LG5 = 2 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum AxisType  差异内容：declare enum AxisType | component/enums.d.ts |
| 新增API | NA | 类名：AxisType；  API声明：VERTICAL\_AXIS = 0  差异内容：VERTICAL\_AXIS = 0 | component/enums.d.ts |
| 新增API | NA | 类名：AxisType；  API声明：HORIZONTAL\_AXIS = 1  差异内容：HORIZONTAL\_AXIS = 1 | component/enums.d.ts |
| 新增API | NA | 类名：AxisType；  API声明：PINCH\_AXIS = 2  差异内容：PINCH\_AXIS = 2 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum ResponseRegionSupportedTool  差异内容：declare enum ResponseRegionSupportedTool | component/enums.d.ts |
| 新增API | NA | 类名：ResponseRegionSupportedTool；  API声明：ALL = 0  差异内容：ALL = 0 | component/enums.d.ts |
| 新增API | NA | 类名：ResponseRegionSupportedTool；  API声明：FINGER = 1  差异内容：FINGER = 1 | component/enums.d.ts |
| 新增API | NA | 类名：ResponseRegionSupportedTool；  API声明：PEN = 2  差异内容：PEN = 2 | component/enums.d.ts |
| 新增API | NA | 类名：ResponseRegionSupportedTool；  API声明：MOUSE = 3  差异内容：MOUSE = 3 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface ImageAlt  差异内容：declare interface ImageAlt | component/image.d.ts |
| 新增API | NA | 类名：ImageAlt；  API声明：placeholder?: ResourceStr | PixelMap;  差异内容：placeholder?: ResourceStr | PixelMap; | component/image.d.ts |
| 新增API | NA | 类名：ImageAlt；  API声明：error?: ResourceStr | PixelMap;  差异内容：error?: ResourceStr | PixelMap; | component/image.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum ScrollSnapAnimationSpeed  差异内容：declare enum ScrollSnapAnimationSpeed | component/list.d.ts |
| 新增API | NA | 类名：ScrollSnapAnimationSpeed；  API声明：NORMAL = 0  差异内容：NORMAL = 0 | component/list.d.ts |
| 新增API | NA | 类名：ScrollSnapAnimationSpeed；  API声明：SLOW = 1  差异内容：SLOW = 1 | component/list.d.ts |
| 新增API | NA | 类名：ListAttribute；  API声明：scrollSnapAnimationSpeed(speed: ScrollSnapAnimationSpeed): ListAttribute;  差异内容：scrollSnapAnimationSpeed(speed: ScrollSnapAnimationSpeed): ListAttribute; | component/list.d.ts |
| 新增API | NA | 类名：Scroller；  API声明：contentSize(): SizeResult;  差异内容：contentSize(): SizeResult; | component/scroll.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：enableSelectedDataDetector(enable: boolean | undefined): SearchAttribute;  差异内容：enableSelectedDataDetector(enable: boolean | undefined): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type DrawableDescriptor = import('../api/@ohos.arkui.drawableDescriptor').DrawableDescriptor;  差异内容：declare type DrawableDescriptor = import('../api/@ohos.arkui.drawableDescriptor').DrawableDescriptor; | component/tab\_content.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface DrawableTabBarIndicator  差异内容：declare interface DrawableTabBarIndicator | component/tab\_content.d.ts |
| 新增API | NA | 类名：DrawableTabBarIndicator；  API声明：drawable?: DrawableDescriptor;  差异内容：drawable?: DrawableDescriptor; | component/tab\_content.d.ts |
| 新增API | NA | 类名：DrawableTabBarIndicator；  API声明：width?: Length;  差异内容：width?: Length; | component/tab\_content.d.ts |
| 新增API | NA | 类名：DrawableTabBarIndicator；  API声明：height?: Length;  差异内容：height?: Length; | component/tab\_content.d.ts |
| 新增API | NA | 类名：DrawableTabBarIndicator；  API声明：borderRadius?: Length;  差异内容：borderRadius?: Length; | component/tab\_content.d.ts |
| 新增API | NA | 类名：DrawableTabBarIndicator；  API声明：marginTop?: Length;  差异内容：marginTop?: Length; | component/tab\_content.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：scrollBarColor(thumbColor: ColorMetrics | undefined): TextAreaAttribute;  差异内容：scrollBarColor(thumbColor: ColorMetrics | undefined): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：enableSelectedDataDetector(enable: boolean | undefined): TextAreaAttribute;  差异内容：enableSelectedDataDetector(enable: boolean | undefined): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：onWillAttachIME(callback: Callback<IMEClient> | undefined): TextAreaAttribute;  差异内容：onWillAttachIME(callback: Callback<IMEClient> | undefined): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：enableSelectedDataDetector(enable: boolean | undefined): TextInputAttribute;  差异内容：enableSelectedDataDetector(enable: boolean | undefined): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TabContentInfo；  API声明：lastIndex?: number;  差异内容：lastIndex?: number; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export class WindowSizeLayoutBreakpointInfo  差异内容：export class WindowSizeLayoutBreakpointInfo | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：WindowSizeLayoutBreakpointInfo；  API声明：readonly widthBreakpoint: WidthBreakpoint;  差异内容：readonly widthBreakpoint: WidthBreakpoint; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：WindowSizeLayoutBreakpointInfo；  API声明：readonly heightBreakpoint: HeightBreakpoint;  差异内容：readonly heightBreakpoint: HeightBreakpoint; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export interface TextChangeEventInfo  差异内容：export interface TextChangeEventInfo | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：TextChangeEventInfo；  API声明：id: string;  差异内容：id: string; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：TextChangeEventInfo；  API声明：uniqueId: number;  差异内容：uniqueId: number; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：TextChangeEventInfo；  API声明：content: string;  差异内容：content: string; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：UIUtils；  API声明：static applySync<T>(task: TaskCallback): T;  差异内容：static applySync<T>(task: TaskCallback): T; | api/@ohos.arkui.StateManagement.d.ts |
| 新增API | NA | 类名：UIUtils；  API声明：static flushUpdates(): void;  差异内容：static flushUpdates(): void; | api/@ohos.arkui.StateManagement.d.ts |
| 新增API | NA | 类名：UIUtils；  API声明：static flushUIUpdates(): void;  差异内容：static flushUIUpdates(): void; | api/@ohos.arkui.StateManagement.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type TaskCallback = () => T;  差异内容：declare type TaskCallback = () => T; | api/@ohos.arkui.StateManagement.d.ts |
| 新增API | NA | 类名：display；  API声明：function getBrightnessInfo(displayId: number): BrightnessInfo;  差异内容：function getBrightnessInfo(displayId: number): BrightnessInfo; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明：type BrightnessCallback<T1, T2> = (data1: T1, data2: T2) => void;  差异内容：type BrightnessCallback<T1, T2> = (data1: T1, data2: T2) => void; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明：function on(type: 'brightnessInfoChange', callback: BrightnessCallback<number, BrightnessInfo>): void;  差异内容：function on(type: 'brightnessInfoChange', callback: BrightnessCallback<number, BrightnessInfo>): void; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明：function off(type: 'brightnessInfoChange', callback?: BrightnessCallback<number, BrightnessInfo>): void;  差异内容：function off(type: 'brightnessInfoChange', callback?: BrightnessCallback<number, BrightnessInfo>): void; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：VirtualScreenConfig；  API声明：supportsFocus?: boolean;  差异内容：supportsFocus?: boolean; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明：interface BrightnessInfo  差异内容：interface BrightnessInfo | api/@ohos.display.d.ts |
| 新增API | NA | 类名：BrightnessInfo；  API声明：readonly sdrNits: number;  差异内容：readonly sdrNits: number; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：BrightnessInfo；  API声明：readonly currentHeadroom: number;  差异内容：readonly currentHeadroom: number; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：BrightnessInfo；  API声明：readonly maxHeadroom: number;  差异内容：readonly maxHeadroom: number; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：PiPConfiguration；  API声明：handleId?: number;  差异内容：handleId?: number; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPConfiguration；  API声明：cornerAdsorptionEnabled?: boolean;  差异内容：cornerAdsorptionEnabled?: boolean; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPController；  API声明：on(type: 'activeStatusChange', callback: Callback<boolean>): void;  差异内容：on(type: 'activeStatusChange', callback: Callback<boolean>): void; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPController；  API声明：off(type: 'activeStatusChange', callback?: Callback<boolean>): void;  差异内容：off(type: 'activeStatusChange', callback?: Callback<boolean>): void; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：global；  API声明：export class ReactiveBuilderNode  差异内容：export class ReactiveBuilderNode | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：ReactiveBuilderNode；  API声明：build(builder: WrappedBuilder<Args>, config: BuildOptions, ...args: Args): void;  差异内容：build(builder: WrappedBuilder<Args>, config: BuildOptions, ...args: Args): void; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：ReactiveBuilderNode；  API声明：getFrameNode(): FrameNode | null;  差异内容：getFrameNode(): FrameNode | null; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：ReactiveBuilderNode；  API声明：postTouchEvent(event: TouchEvent): boolean;  差异内容：postTouchEvent(event: TouchEvent): boolean; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：ReactiveBuilderNode；  API声明：dispose(): void;  差异内容：dispose(): void; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：ReactiveBuilderNode；  API声明：reuse(param?: Object): void;  差异内容：reuse(param?: Object): void; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：ReactiveBuilderNode；  API声明：recycle(): void;  差异内容：recycle(): void; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：ReactiveBuilderNode；  API声明：updateConfiguration(): void;  差异内容：updateConfiguration(): void; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：ReactiveBuilderNode；  API声明：flushState(): void;  差异内容：flushState(): void; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：ReactiveBuilderNode；  API声明：postInputEvent(event: InputEventType): boolean;  差异内容：postInputEvent(event: InputEventType): boolean; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：ReactiveBuilderNode；  API声明：inheritFreezeOptions(enabled: boolean): void;  差异内容：inheritFreezeOptions(enabled: boolean): void; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：ReactiveBuilderNode；  API声明：isDisposed(): boolean;  差异内容：isDisposed(): boolean; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：global；  API声明：export class ReactiveComponentContent  差异内容：export class ReactiveComponentContent | api/arkui/ComponentContent.d.ts |
| 新增API | NA | 类名：ReactiveComponentContent；  API声明：reuse(param?: Object): void;  差异内容：reuse(param?: Object): void; | api/arkui/ComponentContent.d.ts |
| 新增API | NA | 类名：ReactiveComponentContent；  API声明：recycle(): void;  差异内容：recycle(): void; | api/arkui/ComponentContent.d.ts |
| 新增API | NA | 类名：ReactiveComponentContent；  API声明：dispose(): void;  差异内容：dispose(): void; | api/arkui/ComponentContent.d.ts |
| 新增API | NA | 类名：ReactiveComponentContent；  API声明：updateConfiguration(): void;  差异内容：updateConfiguration(): void; | api/arkui/ComponentContent.d.ts |
| 新增API | NA | 类名：ReactiveComponentContent；  API声明：flushState(): void;  差异内容：flushState(): void; | api/arkui/ComponentContent.d.ts |
| 新增API | NA | 类名：ReactiveComponentContent；  API声明：inheritFreezeOptions(enabled: boolean): void;  差异内容：inheritFreezeOptions(enabled: boolean): void; | api/arkui/ComponentContent.d.ts |
| 新增API | NA | 类名：ReactiveComponentContent；  API声明：isDisposed(): boolean;  差异内容：isDisposed(): boolean; | api/arkui/ComponentContent.d.ts |
| 新增API | NA | 类名：BadgeStyle；  API声明：outerBorderColor?: ResourceColor;  差异内容：outerBorderColor?: ResourceColor; | component/badge.d.ts |
| 新增API | NA | 类名：BadgeStyle；  API声明：outerBorderWidth?: LengthMetrics;  差异内容：outerBorderWidth?: LengthMetrics; | component/badge.d.ts |
| 新增API | NA | 类名：BadgeStyle；  API声明：enableAutoAvoidance?: boolean;  差异内容：enableAutoAvoidance?: boolean; | component/badge.d.ts |
| 新增API | NA | 类名：LongPressGestureHandlerOptions；  API声明：allowableMovement?: number;  差异内容：allowableMovement?: number; | component/gesture.d.ts |
| 新增API | NA | 类名：LongPressRecognizer；  API声明：getAllowableMovement(): number;  差异内容：getAllowableMovement(): number; | component/gesture.d.ts |
| 新增API | NA | 类名：ImageSpanAttribute；  API声明：supportSvg2(enable: Optional<boolean>): ImageSpanAttribute;  差异内容：supportSvg2(enable: Optional<boolean>): ImageSpanAttribute; | component/image\_span.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type InterceptionCallback = (from: NavPathInfo | NavBar, to: NavPathInfo | NavBar, pathStack: NavPathStack, operation: NavigationOperation, isAnimated: boolean) => void;  差异内容：declare type InterceptionCallback = (from: NavPathInfo | NavBar, to: NavPathInfo | NavBar, pathStack: NavPathStack, operation: NavigationOperation, isAnimated: boolean) => void; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationInterception；  API声明：interception?: InterceptionCallback;  差异内容：interception?: InterceptionCallback; | component/navigation.d.ts |
| 新增API | NA | 类名：NavDestinationContext；  API声明：mode?: NavDestinationMode;  差异内容：mode?: NavDestinationMode; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type Vector2T<T> = import('../api/arkui/Graphics').Vector2T<T>;  差异内容：declare type Vector2T<T> = import('../api/arkui/Graphics').Vector2T<T>; | component/particle.d.ts |
| 新增API | NA | 类名：ParticleAttribute；  API声明：rippleFields(fields: Array<RippleFieldOptions> | undefined): ParticleAttribute;  差异内容：rippleFields(fields: Array<RippleFieldOptions> | undefined): ParticleAttribute; | component/particle.d.ts |
| 新增API | NA | 类名：ParticleAttribute；  API声明：velocityFields(fields: Array<VelocityFieldOptions> | undefined): ParticleAttribute;  差异内容：velocityFields(fields: Array<VelocityFieldOptions> | undefined): ParticleAttribute; | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface FieldRegion  差异内容：declare interface FieldRegion | component/particle.d.ts |
| 新增API | NA | 类名：FieldRegion；  API声明：shape?: DisturbanceFieldShape;  差异内容：shape?: DisturbanceFieldShape; | component/particle.d.ts |
| 新增API | NA | 类名：FieldRegion；  API声明：position?: PositionT<number>;  差异内容：position?: PositionT<number>; | component/particle.d.ts |
| 新增API | NA | 类名：FieldRegion；  API声明：size?: SizeT<number>;  差异内容：size?: SizeT<number>; | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface RippleFieldOptions  差异内容：declare interface RippleFieldOptions | component/particle.d.ts |
| 新增API | NA | 类名：RippleFieldOptions；  API声明：amplitude?: number;  差异内容：amplitude?: number; | component/particle.d.ts |
| 新增API | NA | 类名：RippleFieldOptions；  API声明：wavelength?: number;  差异内容：wavelength?: number; | component/particle.d.ts |
| 新增API | NA | 类名：RippleFieldOptions；  API声明：waveSpeed?: number;  差异内容：waveSpeed?: number; | component/particle.d.ts |
| 新增API | NA | 类名：RippleFieldOptions；  API声明：attenuation?: number;  差异内容：attenuation?: number; | component/particle.d.ts |
| 新增API | NA | 类名：RippleFieldOptions；  API声明：center?: PositionT<number>;  差异内容：center?: PositionT<number>; | component/particle.d.ts |
| 新增API | NA | 类名：RippleFieldOptions；  API声明：region?: FieldRegion;  差异内容：region?: FieldRegion; | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface VelocityFieldOptions  差异内容：declare interface VelocityFieldOptions | component/particle.d.ts |
| 新增API | NA | 类名：VelocityFieldOptions；  API声明：velocity?: Vector2T<number>;  差异内容：velocity?: Vector2T<number>; | component/particle.d.ts |
| 新增API | NA | 类名：VelocityFieldOptions；  API声明：region?: FieldRegion;  差异内容：region?: FieldRegion; | component/particle.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：enableSelectedDataDetector(enable: boolean | undefined): RichEditorAttribute;  差异内容：enableSelectedDataDetector(enable: boolean | undefined): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：onWillAttachIME(callback: Callback<IMEClient> | undefined): RichEditorAttribute;  差异内容：onWillAttachIME(callback: Callback<IMEClient> | undefined): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：focusBox(style: FocusBoxStyle): T;  差异内容：focusBox(style: FocusBoxStyle): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：readonly leadingMarginSpan?: LeadingMarginSpan;  差异内容：readonly leadingMarginSpan?: LeadingMarginSpan; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ParagraphStyleInterface；  API声明：leadingMarginSpan?: LeadingMarginSpan;  差异内容：leadingMarginSpan?: LeadingMarginSpan; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ImageAttachment；  API声明：readonly supportSvg2?: boolean;  差异内容：readonly supportSvg2?: boolean; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ResourceImageAttachmentOptions；  API声明：supportSvg2?: boolean;  差异内容：supportSvg2?: boolean; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface LeadingMarginSpanDrawInfo  差异内容：declare interface LeadingMarginSpanDrawInfo | component/styled\_string.d.ts |
| 新增API | NA | 类名：LeadingMarginSpanDrawInfo；  API声明：x: number;  差异内容：x: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：LeadingMarginSpanDrawInfo；  API声明：top: number;  差异内容：top: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：LeadingMarginSpanDrawInfo；  API声明：bottom: number;  差异内容：bottom: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：LeadingMarginSpanDrawInfo；  API声明：baseline: number;  差异内容：baseline: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：LeadingMarginSpanDrawInfo；  API声明：direction: TextDirection;  差异内容：direction: TextDirection; | component/styled\_string.d.ts |
| 新增API | NA | 类名：LeadingMarginSpanDrawInfo；  API声明：start: number;  差异内容：start: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：LeadingMarginSpanDrawInfo；  API声明：end: number;  差异内容：end: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：LeadingMarginSpanDrawInfo；  API声明：first: boolean;  差异内容：first: boolean; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明：declare abstract class LeadingMarginSpan  差异内容：declare abstract class LeadingMarginSpan | component/styled\_string.d.ts |
| 新增API | NA | 类名：LeadingMarginSpan；  API声明：abstract onDraw(context: DrawContext, drawInfo: LeadingMarginSpanDrawInfo): void;  差异内容：abstract onDraw(context: DrawContext, drawInfo: LeadingMarginSpanDrawInfo): void; | component/styled\_string.d.ts |
| 新增API | NA | 类名：LeadingMarginSpan；  API声明：abstract getLeadingMargin(): LengthMetrics;  差异内容：abstract getLeadingMargin(): LengthMetrics; | component/styled\_string.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：minLineHeight(value: LengthMetrics | undefined): TextAttribute;  差异内容：minLineHeight(value: LengthMetrics | undefined): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：maxLineHeight(value: LengthMetrics | undefined): TextAttribute;  差异内容：maxLineHeight(value: LengthMetrics | undefined): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：lineHeightMultiple(value: number | undefined): TextAttribute;  差异内容：lineHeightMultiple(value: number | undefined): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：minLines(minLines: Optional<number>): TextAttribute;  差异内容：minLines(minLines: Optional<number>): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：enableSelectedDataDetector(enable: boolean | undefined): TextAttribute;  差异内容：enableSelectedDataDetector(enable: boolean | undefined): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type InputMethodExtraConfig = import('../api/@ohos.inputMethod.ExtraConfig').InputMethodExtraConfig;  差异内容：declare type InputMethodExtraConfig = import('../api/@ohos.inputMethod.ExtraConfig').InputMethodExtraConfig; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum TextDirection  差异内容：declare enum TextDirection | component/text\_common.d.ts |
| 新增API | NA | 类名：TextDirection；  API声明：LTR = 0  差异内容：LTR = 0 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextDirection；  API声明：RTL = 1  差异内容：RTL = 1 | component/text\_common.d.ts |
| 新增API | NA | 类名：IMEClient；  API声明：setExtraConfig(config: InputMethodExtraConfig): void;  差异内容：setExtraConfig(config: InputMethodExtraConfig): void; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface CacheCountInfo  差异内容：declare interface CacheCountInfo | component/units.d.ts |
| 新增API | NA | 类名：CacheCountInfo；  API声明：minCount: number;  差异内容：minCount: number; | component/units.d.ts |
| 新增API | NA | 类名：CacheCountInfo；  API声明：maxCount: number;  差异内容：maxCount: number; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type ResponsiveFillType = PresetFillType;  差异内容：declare type ResponsiveFillType = PresetFillType; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface ItemFillPolicy  差异内容：declare interface ItemFillPolicy | component/units.d.ts |
| 新增API | NA | 类名：ItemFillPolicy；  API声明：fillType?: ResponsiveFillType;  差异内容：fillType?: ResponsiveFillType; | component/units.d.ts |
| 新增API | NA | 类名：PlaybackSpeed；  API声明：SPEED\_FORWARD\_0\_50\_X = 5  差异内容：SPEED\_FORWARD\_0\_50\_X = 5 | component/video.d.ts |
| 新增API | NA | 类名：PlaybackSpeed；  API声明：SPEED\_FORWARD\_1\_50\_X = 6  差异内容：SPEED\_FORWARD\_1\_50\_X = 6 | component/video.d.ts |
| 新增API | NA | 类名：PlaybackSpeed；  API声明：SPEED\_FORWARD\_3\_00\_X = 7  差异内容：SPEED\_FORWARD\_3\_00\_X = 7 | component/video.d.ts |
| 新增API | NA | 类名：PlaybackSpeed；  API声明：SPEED\_FORWARD\_0\_25\_X = 8  差异内容：SPEED\_FORWARD\_0\_25\_X = 8 | component/video.d.ts |
| 新增API | NA | 类名：PlaybackSpeed；  API声明：SPEED\_FORWARD\_0\_125\_X = 9  差异内容：SPEED\_FORWARD\_0\_125\_X = 9 | component/video.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface SurfaceConfig  差异内容：declare interface SurfaceConfig | component/xcomponent.d.ts |
| 新增API | NA | 类名：SurfaceConfig；  API声明：isOpaque?: boolean;  差异内容：isOpaque?: boolean; | component/xcomponent.d.ts |
| 新增API | NA | 类名：XComponentController；  API声明：setXComponentSurfaceConfig(config: SurfaceConfig): void;  差异内容：setXComponentSurfaceConfig(config: SurfaceConfig): void; | component/xcomponent.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\arkui\PickerModifier.d.ts  差异内容：ArkUI | api/arkui/PickerModifier.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：component\picker.d.ts  差异内容：ArkUI | component/picker.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：CommonMethod；  API声明：borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses): T;  差异内容：borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses): T; | 类名：CommonMethod；  API声明：borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses, type?: RenderStrategy): T;  差异内容：borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses, type?: RenderStrategy): T; | component/common.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：ScrollableCommonMethod；  API声明：scrollBarColor(color: Color | number | string): T;  差异内容：scrollBarColor(color: Color | number | string): T; | 类名：ScrollableCommonMethod；  API声明：scrollBarColor(color: Color | number | string | Resource): T;  差异内容：scrollBarColor(color: Color | number | string | Resource): T; | component/common.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：GridAttribute；  API声明：columnsTemplate(value: string): GridAttribute;  差异内容：columnsTemplate(value: string): GridAttribute; | 类名：GridAttribute；  API声明：columnsTemplate(value: string | ItemFillPolicy): GridAttribute;  差异内容：columnsTemplate(value: string | ItemFillPolicy): GridAttribute; | component/grid.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：GridAttribute；  API声明：scrollBarColor(value: Color | number | string): GridAttribute;  差异内容：scrollBarColor(value: Color | number | string): GridAttribute; | 类名：GridAttribute；  API声明：scrollBarColor(color: Color | number | string | Resource): GridAttribute;  差异内容：scrollBarColor(color: Color | number | string | Resource): GridAttribute; | component/grid.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：ListAttribute；  API声明：lanes(value: number | LengthConstrain, gutter?: Dimension): ListAttribute;  差异内容：lanes(value: number | LengthConstrain, gutter?: Dimension): ListAttribute; | 类名：ListAttribute；  API声明：lanes(value: number | LengthConstrain | ItemFillPolicy, gutter?: Dimension): ListAttribute;  差异内容：lanes(value: number | LengthConstrain | ItemFillPolicy, gutter?: Dimension): ListAttribute; | component/list.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：ListAttribute；  API声明：contentStartOffset(value: number): ListAttribute;  差异内容：contentStartOffset(value: number): ListAttribute; | 类名：ListAttribute；  API声明：contentStartOffset(offset: number | Resource): ListAttribute;  差异内容：contentStartOffset(offset: number | Resource): ListAttribute; | component/list.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：ListAttribute；  API声明：contentEndOffset(value: number): ListAttribute;  差异内容：contentEndOffset(value: number): ListAttribute; | 类名：ListAttribute；  API声明：contentEndOffset(offset: number | Resource): ListAttribute;  差异内容：contentEndOffset(offset: number | Resource): ListAttribute; | component/list.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：ListAttribute；  API声明：cachedCount(count: number, show: boolean): ListAttribute;  差异内容：cachedCount(count: number, show: boolean): ListAttribute; | 类名：ListAttribute；  API声明：cachedCount(count: number | CacheCountInfo, show: boolean): ListAttribute;  差异内容：cachedCount(count: number | CacheCountInfo, show: boolean): ListAttribute; | component/list.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：ScrollAttribute；  API声明：scrollBarColor(color: Color | number | string): ScrollAttribute;  差异内容：scrollBarColor(color: Color | number | string): ScrollAttribute; | 类名：ScrollAttribute；  API声明：scrollBarColor(color: Color | number | string | Resource): ScrollAttribute;  差异内容：scrollBarColor(color: Color | number | string | Resource): ScrollAttribute; | component/scroll.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：SwiperAttribute；  API声明：displayCount(value: number | string | SwiperAutoFill, swipeByGroup?: boolean): SwiperAttribute;  差异内容：displayCount(value: number | string | SwiperAutoFill, swipeByGroup?: boolean): SwiperAttribute; | 类名：SwiperAttribute；  API声明：displayCount(value: number | string | SwiperAutoFill | ItemFillPolicy, swipeByGroup?: boolean): SwiperAttribute;  差异内容：displayCount(value: number | string | SwiperAutoFill | ItemFillPolicy, swipeByGroup?: boolean): SwiperAttribute; | component/swiper.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：SubTabBarStyle；  API声明：indicator(value: IndicatorStyle): SubTabBarStyle;  差异内容：indicator(value: IndicatorStyle): SubTabBarStyle; | 类名：SubTabBarStyle；  API声明：indicator(value: IndicatorStyle | DrawableTabBarIndicator): SubTabBarStyle;  差异内容：indicator(value: IndicatorStyle | DrawableTabBarIndicator): SubTabBarStyle; | component/tab\_content.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：WaterFlowAttribute；  API声明：columnsTemplate(value: string): WaterFlowAttribute;  差异内容：columnsTemplate(value: string): WaterFlowAttribute; | 类名：WaterFlowAttribute；  API声明：columnsTemplate(value: string | ItemFillPolicy): WaterFlowAttribute;  差异内容：columnsTemplate(value: string | ItemFillPolicy): WaterFlowAttribute; | component/water\_flow.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围不是包含关系 | 类名：ImageAttribute；  API声明：alt(value: string | Resource | PixelMap): ImageAttribute;  差异内容：alt(value: string | Resource | PixelMap): ImageAttribute; | 类名：ImageAttribute；  API声明：alt(src: ResourceStr | PixelMap | ImageAlt): ImageAttribute;  差异内容：alt(src: ResourceStr | PixelMap | ImageAlt): ImageAttribute; | component/image.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Window；  API声明：maximize(presentation?: MaximizePresentation): Promise<void>;  差异内容：maximize(presentation?: MaximizePresentation): Promise<void>; | 类名：Window；  API声明：maximize(presentation?: MaximizePresentation, acrossDisplay?: boolean): Promise<void>;  差异内容：maximize(presentation?: MaximizePresentation, acrossDisplay?: boolean): Promise<void>; | api/@ohos.window.d.ts |
| 新增导出符号 | 类名：global；  API声明：export const enum ResolveStrategy  差异内容：NA | 类名：global；  API声明：  差异内容：export const enum ResolveStrategy | api/@ohos.arkui.UIContext.d.ts |
| arkts演进版本整改兼容变化 | 类名：global；  API声明：export declare class FocusController  差异内容：NA | 类名：global；  API声明：export class FocusController  差异内容：NA | api/@ohos.arkui.UIContext.d.ts |
| arkts演进版本整改兼容变化 | 类名：global；  API声明：export declare class ComponentSnapshot  差异内容：NA | 类名：global；  API声明：export class ComponentSnapshot  差异内容：NA | api/@ohos.arkui.UIContext.d.ts |
