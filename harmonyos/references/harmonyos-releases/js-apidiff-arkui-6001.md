---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-6001
title: ArkUI
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > ArkUI
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:36+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:e5f86eaef725fea3f57181ebd1c0b3b914d02fd6a3999667324594f434b2ec7c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：global；  API声明：export declare class NavigatorModifier  差异内容：NA | 类名：global；  API声明：export declare class NavigatorModifier  差异内容：20 | api/arkui/NavigatorModifier.d.ts |
| API废弃版本变更 | 类名：NavigatorModifier；  API声明：applyNormalAttribute?(instance: NavigatorAttribute): void;  差异内容：NA | 类名：NavigatorModifier；  API声明：applyNormalAttribute?(instance: NavigatorAttribute): void;  差异内容：20 | api/arkui/NavigatorModifier.d.ts |
| API废弃版本变更 | 类名：global；  API声明：export declare class NavRouterModifier  差异内容：NA | 类名：global；  API声明：export declare class NavRouterModifier  差异内容：20 | api/arkui/NavRouterModifier.d.ts |
| API废弃版本变更 | 类名：NavRouterModifier；  API声明：applyNormalAttribute?(instance: NavRouterAttribute): void;  差异内容：NA | 类名：NavRouterModifier；  API声明：applyNormalAttribute?(instance: NavRouterAttribute): void;  差异内容：20 | api/arkui/NavRouterModifier.d.ts |
| API废弃版本变更 | 类名：global；  API声明：export declare class PanelModifier  差异内容：NA | 类名：global；  API声明：export declare class PanelModifier  差异内容：20 | api/arkui/PanelModifier.d.ts |
| API废弃版本变更 | 类名：PanelModifier；  API声明：applyNormalAttribute?(instance: PanelAttribute): void;  差异内容：NA | 类名：PanelModifier；  API声明：applyNormalAttribute?(instance: PanelAttribute): void;  差异内容：20 | api/arkui/PanelModifier.d.ts |
| 新增错误码 | 类名：ClickEvent；  API声明：preventDefault: () => void;  差异内容：NA | 类名：ClickEvent；  API声明：preventDefault: () => void;  差异内容：100017 | component/common.d.ts |
| 新增错误码 | 类名：TouchEvent；  API声明：preventDefault: () => void;  差异内容：NA | 类名：TouchEvent；  API声明：preventDefault: () => void;  差异内容：100017 | component/common.d.ts |
| 新增错误码 | 类名：PromptAction；  API声明：closeToast(toastId: number): void;  差异内容：NA | 类名：PromptAction；  API声明：closeToast(toastId: number): void;  差异内容：103401 | api/@ohos.arkui.UIContext.d.ts |
| 新增错误码 | 类名：promptAction；  API声明：function closeToast(toastId: number): void;  差异内容：NA | 类名：promptAction；  API声明：function closeToast(toastId: number): void;  差异内容：103401 | api/@ohos.promptAction.d.ts |
| 新增错误码 | 类名：Window；  API声明：setSubWindowModal(isModal: boolean): Promise<void>;  差异内容：NA | 类名：Window；  API声明：setSubWindowModal(isModal: boolean): Promise<void>;  差异内容：1300003 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：Window；  API声明：setSubWindowModal(isModal: boolean, modalityType: ModalityType): Promise<void>;  差异内容：NA | 类名：Window；  API声明：setSubWindowModal(isModal: boolean, modalityType: ModalityType): Promise<void>;  差异内容：1300003 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：WindowStage；  API声明：setWindowModal(isModal: boolean): Promise<void>;  差异内容：NA | 类名：WindowStage；  API声明：setWindowModal(isModal: boolean): Promise<void>;  差异内容：1300005 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：WindowStage；  API声明：isWindowRectAutoSave(): Promise<boolean>;  差异内容：NA | 类名：WindowStage；  API声明：isWindowRectAutoSave(): Promise<boolean>;  差异内容：1300003 | api/@ohos.window.d.ts |
| 新增错误码 | 类名：CanvasRenderingContext2D；  API声明：startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>;  差异内容：NA | 类名：CanvasRenderingContext2D；  API声明：startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>;  差异内容：110003 | component/canvas.d.ts |
| 新增错误码 | 类名：StyledString；  API声明：static fromHtml(html: string): Promise<StyledString>;  差异内容：NA | 类名：StyledString；  API声明：static fromHtml(html: string): Promise<StyledString>;  差异内容：170001 | component/styled\_string.d.ts |
| 删除错误码 | 类名：Window；  API声明：destroyWindow(callback: AsyncCallback<void>): void;  差异内容：1300003 | 类名：Window；  API声明：destroyWindow(callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：Window；  API声明：destroyWindow(): Promise<void>;  差异内容：1300003 | 类名：Window；  API声明：destroyWindow(): Promise<void>;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：Window；  API声明：loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void;  差异内容：1300003 | 类名：Window；  API声明：loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：Window；  API声明：loadContent(path: string, storage: LocalStorage): Promise<void>;  差异内容：1300003 | 类名：Window；  API声明：loadContent(path: string, storage: LocalStorage): Promise<void>;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：Window；  API声明：setUIContent(path: string, callback: AsyncCallback<void>): void;  差异内容：1300003 | 类名：Window；  API声明：setUIContent(path: string, callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：Window；  API声明：setUIContent(path: string): Promise<void>;  差异内容：1300003 | 类名：Window；  API声明：setUIContent(path: string): Promise<void>;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：Window；  API声明：maximize(presentation?: MaximizePresentation): Promise<void>;  差异内容：1300005 | 类名：Window；  API声明：maximize(presentation?: MaximizePresentation): Promise<void>;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：Window；  API声明：setWindowDecorVisible(isVisible: boolean): void;  差异内容：1300004 | 类名：Window；  API声明：setWindowDecorVisible(isVisible: boolean): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：Window；  API声明：setTitleAndDockHoverShown(isTitleHoverShown?: boolean, isDockHoverShown?: boolean): Promise<void>;  差异内容：401 | 类名：Window；  API声明：setTitleAndDockHoverShown(isTitleHoverShown?: boolean, isDockHoverShown?: boolean): Promise<void>;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：WindowStage；  API声明：createSubWindow(name: string): Promise<Window>;  差异内容：1300005 | 类名：WindowStage；  API声明：createSubWindow(name: string): Promise<Window>;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：WindowStage；  API声明：createSubWindow(name: string, callback: AsyncCallback<Window>): void;  差异内容：1300005 | 类名：WindowStage；  API声明：createSubWindow(name: string, callback: AsyncCallback<Window>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：WindowStage；  API声明：loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void;  差异内容：1300005 | 类名：WindowStage；  API声明：loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：WindowStage；  API声明：loadContent(path: string, storage?: LocalStorage): Promise<void>;  差异内容：1300005 | 类名：WindowStage；  API声明：loadContent(path: string, storage?: LocalStorage): Promise<void>;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：WindowStage；  API声明：loadContent(path: string, callback: AsyncCallback<void>): void;  差异内容：1300005 | 类名：WindowStage；  API声明：loadContent(path: string, callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：WindowStage；  API声明：loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void;  差异内容：1300003 | 类名：WindowStage；  API声明：loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：WindowStage；  API声明：loadContentByName(name: string, callback: AsyncCallback<void>): void;  差异内容：1300003 | 类名：WindowStage；  API声明：loadContentByName(name: string, callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.window.d.ts |
| 删除错误码 | 类名：WindowStage；  API声明：loadContentByName(name: string, storage?: LocalStorage): Promise<void>;  差异内容：1300003 | 类名：WindowStage；  API声明：loadContentByName(name: string, storage?: LocalStorage): Promise<void>;  差异内容：NA | api/@ohos.window.d.ts |
| 错误码变更 | 类名：WindowStage；  API声明：getSubWindow(): Promise<Array<Window>>;  差异内容：1300005 | 类名：WindowStage；  API声明：getSubWindow(): Promise<Array<Window>>;  差异内容：1300002 | api/@ohos.window.d.ts |
| 错误码变更 | 类名：WindowStage；  API声明：getSubWindow(callback: AsyncCallback<Array<Window>>): void;  差异内容：1300005 | 类名：WindowStage；  API声明：getSubWindow(callback: AsyncCallback<Array<Window>>): void;  差异内容：1300002 | api/@ohos.window.d.ts |
| 函数变更 | 类名：PathAttribute；  API声明：commands(value: string): PathAttribute;  差异内容：value: string | 类名：PathAttribute；  API声明：commands(value: ResourceStr): PathAttribute;  差异内容：value: ResourceStr | component/path.d.ts |
| 函数变更 | 类名：RectAttribute；  API声明：radiusWidth(value: number | string): RectAttribute;  差异内容：value: number | string | 类名：RectAttribute；  API声明：radiusWidth(value: Length): RectAttribute;  差异内容：value: Length | component/rect.d.ts |
| 函数变更 | 类名：RectAttribute；  API声明：radiusHeight(value: number | string): RectAttribute;  差异内容：value: number | string | 类名：RectAttribute；  API声明：radiusHeight(value: Length): RectAttribute;  差异内容：value: Length | component/rect.d.ts |
| 函数变更 | 类名：RectAttribute；  API声明：radius(value: number | string | Array<any>): RectAttribute;  差异内容：value: number | string | Array<any> | 类名：RectAttribute；  API声明：radius(value: Length | Array<any>): RectAttribute;  差异内容：value: Length | Array<any> | component/rect.d.ts |
| 函数变更 | 类名：SearchAttribute；  API声明：searchButton(value: string, option?: SearchButtonOptions): SearchAttribute;  差异内容：value: string | 类名：SearchAttribute；  API声明：searchButton(value: ResourceStr, option?: SearchButtonOptions): SearchAttribute;  差异内容：value: ResourceStr | component/search.d.ts |
| 函数变更 | 类名：ShapeAttribute；  API声明：strokeDashOffset(value: number | string): ShapeAttribute;  差异内容：value: number | string | 类名：ShapeAttribute；  API声明：strokeDashOffset(value: Length): ShapeAttribute;  差异内容：value: Length | component/shape.d.ts |
| 函数变更 | 类名：ShapeAttribute；  API声明：strokeMiterLimit(value: number | string): ShapeAttribute;  差异内容：value: number | string | 类名：ShapeAttribute；  API声明：strokeMiterLimit(value: Length): ShapeAttribute;  差异内容：value: Length | component/shape.d.ts |
| 函数变更 | 类名：ShapeAttribute；  API声明：strokeWidth(value: number | string): ShapeAttribute;  差异内容：value: number | string | 类名：ShapeAttribute；  API声明：strokeWidth(value: Length): ShapeAttribute;  差异内容：value: Length | component/shape.d.ts |
| 函数变更 | 类名：SpanAttribute；  API声明：fontWeight(value: number | FontWeight | string): SpanAttribute;  差异内容：value: number | FontWeight | string | 类名：SpanAttribute；  API声明：fontWeight(value: number | FontWeight | ResourceStr): SpanAttribute;  差异内容：value: number | FontWeight | ResourceStr | component/span.d.ts |
| 函数变更 | 类名：SpanAttribute；  API声明：letterSpacing(value: number | string): SpanAttribute;  差异内容：value: number | string | 类名：SpanAttribute；  API声明：letterSpacing(value: number | ResourceStr): SpanAttribute;  差异内容：value: number | ResourceStr | component/span.d.ts |
| 函数变更 | 类名：TextAttribute；  API声明：fontWeight(value: number | FontWeight | string): TextAttribute;  差异内容：value: number | FontWeight | string | 类名：TextAttribute；  API声明：fontWeight(value: number | FontWeight | ResourceStr): TextAttribute;  差异内容：value: number | FontWeight | ResourceStr | component/text.d.ts |
| 函数变更 | 类名：TextAttribute；  API声明：fontWeight(weight: number | FontWeight | string, options?: FontSettingOptions): TextAttribute;  差异内容：weight: number | FontWeight | string | 类名：TextAttribute；  API声明：fontWeight(weight: number | FontWeight | ResourceStr, options?: FontSettingOptions): TextAttribute;  差异内容：weight: number | FontWeight | ResourceStr | component/text.d.ts |
| 函数变更 | 类名：TextAttribute；  API声明：letterSpacing(value: number | string): TextAttribute;  差异内容：value: number | string | 类名：TextAttribute；  API声明：letterSpacing(value: number | ResourceStr): TextAttribute;  差异内容：value: number | ResourceStr | component/text.d.ts |
| 函数变更 | 类名：TextAttribute；  API声明：baselineOffset(value: number | string): TextAttribute;  差异内容：value: number | string | 类名：TextAttribute；  API声明：baselineOffset(value: number | ResourceStr): TextAttribute;  差异内容：value: number | ResourceStr | component/text.d.ts |
| 函数变更 | 类名：TextAreaAttribute；  API声明：fontWeight(value: number | FontWeight | string): TextAreaAttribute;  差异内容：value: number | FontWeight | string | 类名：TextAreaAttribute；  API声明：fontWeight(value: number | FontWeight | ResourceStr): TextAreaAttribute;  差异内容：value: number | FontWeight | ResourceStr | component/text\_area.d.ts |
| 函数变更 | 类名：TextClockAttribute；  API声明：format(value: string): TextClockAttribute;  差异内容：value: string | 类名：TextClockAttribute；  API声明：format(value: ResourceStr): TextClockAttribute;  差异内容：value: ResourceStr | component/text\_clock.d.ts |
| 函数变更 | 类名：TextInputAttribute；  API声明：fontWeight(value: number | FontWeight | string): TextInputAttribute;  差异内容：value: number | FontWeight | string | 类名：TextInputAttribute；  API声明：fontWeight(value: number | FontWeight | ResourceStr): TextInputAttribute;  差异内容：value: number | FontWeight | ResourceStr | component/text\_input.d.ts |
| 函数变更 | 类名：TextTimerAttribute；  API声明：fontWeight(value: number | FontWeight | string): TextTimerAttribute;  差异内容：value: number | FontWeight | string | 类名：TextTimerAttribute；  API声明：fontWeight(value: number | FontWeight | ResourceStr): TextTimerAttribute;  差异内容：value: number | FontWeight | ResourceStr | component/text\_timer.d.ts |
| 函数变更 | 类名：VideoAttribute；  API声明：onError(event: () => void): VideoAttribute;  差异内容：event: () => void | 类名：VideoAttribute；  API声明：onError(event: VoidCallback | import('../api/@ohos.base').ErrorCallback): VideoAttribute;  差异内容：event: VoidCallback | import('../api/@ohos.base').ErrorCallback | component/video.d.ts |
| 函数变更 | 类名：RichEditorController；  API声明：addTextSpan(value: string, options?: RichEditorTextSpanOptions): number;  差异内容：value: string, options?: RichEditorTextSpanOptions | 类名：RichEditorController；  API声明：addTextSpan(content: ResourceStr, options?: RichEditorTextSpanOptions): number;  差异内容：content: ResourceStr, options?: RichEditorTextSpanOptions | component/rich\_editor.d.ts |
| 属性变更 | 类名：ProgressButton；  API声明：@Prop  content: string;  差异内容：string | 类名：ProgressButton；  API声明：@Prop  content: ResourceStr;  差异内容：ResourceStr | api/@ohos.arkui.advanced.ProgressButton.d.ets |
| 属性变更 | 类名：SelectOptions；  API声明：value?: string;  差异内容：string | 类名：SelectOptions；  API声明：value?: ResourceStr;  差异内容：ResourceStr | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 属性变更 | 类名：SubHeaderV2SelectOptions；  API声明：selectedContent?: string;  差异内容：string | 类名：SubHeaderV2SelectOptions；  API声明：selectedContent?: ResourceStr;  差异内容：ResourceStr | api/@ohos.arkui.advanced.SubHeaderV2.d.ets |
| 属性变更 | 类名：SubHeaderV2Select；  API声明：@Trace  selectedContent?: string;  差异内容：string | 类名：SubHeaderV2Select；  API声明：@Trace  selectedContent?: ResourceStr;  差异内容：ResourceStr | api/@ohos.arkui.advanced.SubHeaderV2.d.ets |
| 属性变更 | 类名：SwipeRefresher；  API声明：@Prop  content?: string;  差异内容：string | 类名：SwipeRefresher；  API声明：@Prop  content?: ResourceStr;  差异内容：ResourceStr | api/@ohos.arkui.advanced.SwipeRefresher.d.ets |
|  |  |  |  |
| 属性变更 | 类名：BadgeStyle；  API声明：fontSize?: number | string;  差异内容：number,string | 类名：BadgeStyle；  API声明：fontSize?: number | ResourceStr;  差异内容：number,ResourceStr | component/badge.d.ts |
| 属性变更 | 类名：BadgeStyle；  API声明：badgeSize?: number | string;  差异内容：number,string | 类名：BadgeStyle；  API声明：badgeSize?: number | ResourceStr;  差异内容：number,ResourceStr | component/badge.d.ts |
| 属性变更 | 类名：BadgeStyle；  API声明：fontWeight?: number | FontWeight | string;  差异内容：number,FontWeight,string | 类名：BadgeStyle；  API声明：fontWeight?: number | FontWeight | ResourceStr;  差异内容：number,FontWeight,ResourceStr | component/badge.d.ts |
| 属性变更 | 类名：BadgeParamWithString；  API声明：value: string;  差异内容：string | 类名：BadgeParamWithString；  API声明：value: ResourceStr;  差异内容：ResourceStr | component/badge.d.ts |
| 属性变更 | 类名：CircleOptions；  API声明：width?: string | number;  差异内容：string,number | 类名：CircleOptions；  API声明：width?: Length;  差异内容：Length | component/circle.d.ts |
| 属性变更 | 类名：CircleOptions；  API声明：height?: string | number;  差异内容：string,number | 类名：CircleOptions；  API声明：height?: Length;  差异内容：Length | component/circle.d.ts |
| 属性变更 | 类名：EllipseOptions；  API声明：width?: string | number;  差异内容：string,number | 类名：EllipseOptions；  API声明：width?: Length;  差异内容：Length | component/ellipse.d.ts |
| 属性变更 | 类名：EllipseOptions；  API声明：height?: string | number;  差异内容：string,number | 类名：EllipseOptions；  API声明：height?: Length;  差异内容：Length | component/ellipse.d.ts |
| 属性变更 | 类名：LineOptions；  API声明：width?: string | number;  差异内容：string,number | 类名：LineOptions；  API声明：width?: Length;  差异内容：Length | component/line.d.ts |
| 属性变更 | 类名：LineOptions；  API声明：height?: string | number;  差异内容：string,number | 类名：LineOptions；  API声明：height?: Length;  差异内容：Length | component/line.d.ts |
| 属性变更 | 类名：PathOptions；  API声明：width?: number | string;  差异内容：number,string | 类名：PathOptions；  API声明：width?: Length;  差异内容：Length | component/path.d.ts |
| 属性变更 | 类名：PathOptions；  API声明：height?: number | string;  差异内容：number,string | 类名：PathOptions；  API声明：height?: Length;  差异内容：Length | component/path.d.ts |
| 属性变更 | 类名：PathOptions；  API声明：commands?: string;  差异内容：string | 类名：PathOptions；  API声明：commands?: ResourceStr;  差异内容：ResourceStr | component/path.d.ts |
| 属性变更 | 类名：PolygonOptions；  API声明：width?: string | number;  差异内容：string,number | 类名：PolygonOptions；  API声明：width?: Length;  差异内容：Length | component/polygon.d.ts |
| 属性变更 | 类名：PolygonOptions；  API声明：height?: string | number;  差异内容：string,number | 类名：PolygonOptions；  API声明：height?: Length;  差异内容：Length | component/polygon.d.ts |
| 属性变更 | 类名：PolylineOptions；  API声明：width?: string | number;  差异内容：string,number | 类名：PolylineOptions；  API声明：width?: Length;  差异内容：Length | component/polyline.d.ts |
| 属性变更 | 类名：PolylineOptions；  API声明：height?: string | number;  差异内容：string,number | 类名：PolylineOptions；  API声明：height?: Length;  差异内容：Length | component/polyline.d.ts |
| 属性变更 | 类名：CapsuleStyleOptions；  API声明：content?: string;  差异内容：string | 类名：CapsuleStyleOptions；  API声明：content?: ResourceStr;  差异内容：ResourceStr | component/progress.d.ts |
| 属性变更 | 类名：StarStyleOptions；  API声明：backgroundUri: string;  差异内容：string | 类名：StarStyleOptions；  API声明：backgroundUri: ResourceStr;  差异内容：ResourceStr | component/rating.d.ts |
| 属性变更 | 类名：StarStyleOptions；  API声明：foregroundUri: string;  差异内容：string | 类名：StarStyleOptions；  API声明：foregroundUri: ResourceStr;  差异内容：ResourceStr | component/rating.d.ts |
| 属性变更 | 类名：StarStyleOptions；  API声明：secondaryUri?: string;  差异内容：string | 类名：StarStyleOptions；  API声明：secondaryUri?: ResourceStr;  差异内容：ResourceStr | component/rating.d.ts |
| 属性变更 | 类名：RectOptions；  API声明：width?: number | string;  差异内容：number,string | 类名：RectOptions；  API声明：width?: Length;  差异内容：Length | component/rect.d.ts |
| 属性变更 | 类名：RectOptions；  API声明：height?: number | string;  差异内容：number,string | 类名：RectOptions；  API声明：height?: Length;  差异内容：Length | component/rect.d.ts |
| 属性变更 | 类名：RectOptions；  API声明：radius?: number | string | Array<any>;  差异内容：number,string,Array<any> | 类名：RectOptions；  API声明：radius?: Length | Array<any>;  差异内容：Length,Array<any> | component/rect.d.ts |
| 属性变更 | 类名：RoundedRectOptions；  API声明：width?: number | string;  差异内容：number,string | 类名：RoundedRectOptions；  API声明：width?: Length;  差异内容：Length | component/rect.d.ts |
| 属性变更 | 类名：RoundedRectOptions；  API声明：height?: number | string;  差异内容：number,string | 类名：RoundedRectOptions；  API声明：height?: Length;  差异内容：Length | component/rect.d.ts |
| 属性变更 | 类名：RoundedRectOptions；  API声明：radiusWidth?: number | string;  差异内容：number,string | 类名：RoundedRectOptions；  API声明：radiusWidth?: Length;  差异内容：Length | component/rect.d.ts |
| 属性变更 | 类名：RoundedRectOptions；  API声明：radiusHeight?: number | string;  差异内容：number,string | 类名：RoundedRectOptions；  API声明：radiusHeight?: Length;  差异内容：Length | component/rect.d.ts |
| 属性变更 | 类名：SearchOptions；  API声明：value?: string;  差异内容：string | 类名：SearchOptions；  API声明：value?: ResourceStr;  差异内容：ResourceStr | component/search.d.ts |
| 属性变更 | 类名：ViewportRect；  API声明：x?: number | string;  差异内容：number,string | 类名：ViewportRect；  API声明：x?: Length;  差异内容：Length | component/shape.d.ts |
| 属性变更 | 类名：ViewportRect；  API声明：y?: number | string;  差异内容：number,string | 类名：ViewportRect；  API声明：y?: Length;  差异内容：Length | component/shape.d.ts |
| 属性变更 | 类名：ViewportRect；  API声明：width?: number | string;  差异内容：number,string | 类名：ViewportRect；  API声明：width?: Length;  差异内容：Length | component/shape.d.ts |
| 属性变更 | 类名：ViewportRect；  API声明：height?: number | string;  差异内容：number,string | 类名：ViewportRect；  API声明：height?: Length;  差异内容：Length | component/shape.d.ts |
| 属性变更 | 类名：TextPickerOptions；  API声明：value?: string | string[];  差异内容：string,string[] | 类名：TextPickerOptions；  API声明：value?: ResourceStr | ResourceStr[];  差异内容：ResourceStr,ResourceStr[] | component/text\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare class StepperModifier  差异内容：export declare class StepperModifier | api/arkui/StepperModifier.d.ts |
| 新增API | NA | 类名：StepperModifier；  API声明：applyNormalAttribute?(instance: StepperAttribute): void;  差异内容：applyNormalAttribute?(instance: StepperAttribute): void; | api/arkui/StepperModifier.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum ToolBarItemPlacement  差异内容：declare enum ToolBarItemPlacement | component/toolbar.d.ts |
| 新增API | NA | 类名：ToolBarItemPlacement；  API声明：TOP\_BAR\_LEADING = 0  差异内容：TOP\_BAR\_LEADING = 0 | component/toolbar.d.ts |
| 新增API | NA | 类名：ToolBarItemPlacement；  API声明：TOP\_BAR\_TRAILING = 1  差异内容：TOP\_BAR\_TRAILING = 1 | component/toolbar.d.ts |
| 新增API | NA | 类名：global；  API声明：interface ToolBarItemOptions  差异内容：interface ToolBarItemOptions | component/toolbar.d.ts |
| 新增API | NA | 类名：ToolBarItemOptions；  API声明：placement?: ToolBarItemPlacement;  差异内容：placement?: ToolBarItemPlacement; | component/toolbar.d.ts |
| 新增API | NA | 类名：global；  API声明：interface ToolBarItemInterface  差异内容：interface ToolBarItemInterface | component/toolbar.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class ToolBarItemAttribute  差异内容：declare class ToolBarItemAttribute | component/toolbar.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const ToolBarItem: ToolBarItemInterface;  差异内容：declare const ToolBarItem: ToolBarItemInterface; | component/toolbar.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const ToolBarItemInstance: ToolBarItemAttribute;  差异内容：declare const ToolBarItemInstance: ToolBarItemAttribute; | component/toolbar.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare function isApiVersionGreaterOrEqual(apiVersion: string): boolean;  差异内容：export declare function isApiVersionGreaterOrEqual(apiVersion: string): boolean; | api/@internal/full/global.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type NodeIdentity = string | number;  差异内容：declare type NodeIdentity = string | number; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type NodeRenderStateChangeCallback = (state: NodeRenderState, node?: FrameNode) => void;  差异内容：declare type NodeRenderStateChangeCallback = (state: NodeRenderState, node?: FrameNode) => void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：export const enum NodeRenderState  差异内容：export const enum NodeRenderState | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：NodeRenderState；  API声明：ABOUT\_TO\_RENDER\_IN = 0  差异内容：ABOUT\_TO\_RENDER\_IN = 0 | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：NodeRenderState；  API声明：ABOUT\_TO\_RENDER\_OUT = 1  差异内容：ABOUT\_TO\_RENDER\_OUT = 1 | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：promptAction；  API声明：enum CommonState  差异内容：enum CommonState | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：CommonState；  API声明：UNINITIALIZED = 0  差异内容：UNINITIALIZED = 0 | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：CommonState；  API声明：INITIALIZED = 1  差异内容：INITIALIZED = 1 | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：CommonState；  API声明：APPEARING = 2  差异内容：APPEARING = 2 | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：CommonState；  API声明：APPEARED = 3  差异内容：APPEARED = 3 | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：CommonState；  API声明：DISAPPEARING = 4  差异内容：DISAPPEARING = 4 | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：CommonState；  API声明：DISAPPEARED = 5  差异内容：DISAPPEARED = 5 | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type WindowAnimationCurveParam = Array<number>;  差异内容：declare type WindowAnimationCurveParam = Array<number>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：function getGlobalWindowMode(displayId?: number): Promise<number>;  差异内容：function getGlobalWindowMode(displayId?: number): Promise<number>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：function setStartWindowBackgroundColor(moduleName: string, abilityName: string, color: ColorMetrics): Promise<void>;  差异内容：function setStartWindowBackgroundColor(moduleName: string, abilityName: string, color: ColorMetrics): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：enum WindowTransitionType  差异内容：enum WindowTransitionType | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowTransitionType；  API声明：DESTROY = 0  差异内容：DESTROY = 0 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：enum WindowAnimationCurve  差异内容：enum WindowAnimationCurve | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowAnimationCurve；  API声明：LINEAR = 0  差异内容：LINEAR = 0 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowAnimationCurve；  API声明：INTERPOLATION\_SPRING = 1  差异内容：INTERPOLATION\_SPRING = 1 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：interface WindowAnimationConfig  差异内容：interface WindowAnimationConfig | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowAnimationConfig；  API声明：curve: WindowAnimationCurve;  差异内容：curve: WindowAnimationCurve; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowAnimationConfig；  API声明：duration?: number;  差异内容：duration?: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowAnimationConfig；  API声明：param?: WindowAnimationCurveParam;  差异内容：param?: WindowAnimationCurveParam; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：interface TransitionAnimation  差异内容：interface TransitionAnimation | api/@ohos.window.d.ts |
| 新增API | NA | 类名：TransitionAnimation；  API声明：config: WindowAnimationConfig;  差异内容：config: WindowAnimationConfig; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：TransitionAnimation；  API声明：opacity?: number;  差异内容：opacity?: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：interface ShowWindowOptions  差异内容：interface ShowWindowOptions | api/@ohos.window.d.ts |
| 新增API | NA | 类名：ShowWindowOptions；  API声明：focusOnShow?: boolean;  差异内容：focusOnShow?: boolean; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：enum GlobalWindowMode  差异内容：enum GlobalWindowMode | api/@ohos.window.d.ts |
| 新增API | NA | 类名：GlobalWindowMode；  API声明：FULLSCREEN = 1  差异内容：FULLSCREEN = 1 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：GlobalWindowMode；  API声明：SPLIT = 1 << 1  差异内容：SPLIT = 1 << 1 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：GlobalWindowMode；  API声明：FLOAT = 1 << 2  差异内容：FLOAT = 1 << 2 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：GlobalWindowMode；  API声明：PIP = 1 << 3  差异内容：PIP = 1 << 3 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum AccessibilityAction  差异内容：declare enum AccessibilityAction | component/common.d.ts |
| 新增API | NA | 类名：AccessibilityAction；  API声明：UNDEFINED\_ACTION = 0  差异内容：UNDEFINED\_ACTION = 0 | component/common.d.ts |
| 新增API | NA | 类名：AccessibilityAction；  API声明：ACCESSIBILITY\_CLICK = 1  差异内容：ACCESSIBILITY\_CLICK = 1 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum AccessibilityActionInterceptResult  差异内容：declare enum AccessibilityActionInterceptResult | component/common.d.ts |
| 新增API | NA | 类名：AccessibilityActionInterceptResult；  API声明：ACTION\_INTERCEPT = 0  差异内容：ACTION\_INTERCEPT = 0 | component/common.d.ts |
| 新增API | NA | 类名：AccessibilityActionInterceptResult；  API声明：ACTION\_CONTINUE = 1  差异内容：ACTION\_CONTINUE = 1 | component/common.d.ts |
| 新增API | NA | 类名：AccessibilityActionInterceptResult；  API声明：ACTION\_RISE = 2  差异内容：ACTION\_RISE = 2 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type AccessibilityActionInterceptCallback = (action: AccessibilityAction) => AccessibilityActionInterceptResult;  差异内容：declare type AccessibilityActionInterceptCallback = (action: AccessibilityAction) => AccessibilityActionInterceptResult; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface RotateAngleOptions  差异内容：declare interface RotateAngleOptions | component/common.d.ts |
| 新增API | NA | 类名：RotateAngleOptions；  API声明：angleX?: number | string;  差异内容：angleX?: number | string; | component/common.d.ts |
| 新增API | NA | 类名：RotateAngleOptions；  API声明：angleY?: number | string;  差异内容：angleY?: number | string; | component/common.d.ts |
| 新增API | NA | 类名：RotateAngleOptions；  API声明：angleZ?: number | string;  差异内容：angleZ?: number | string; | component/common.d.ts |
| 新增API | NA | 类名：RotateAngleOptions；  API声明：centerX?: number | string;  差异内容：centerX?: number | string; | component/common.d.ts |
| 新增API | NA | 类名：RotateAngleOptions；  API声明：centerY?: number | string;  差异内容：centerY?: number | string; | component/common.d.ts |
| 新增API | NA | 类名：RotateAngleOptions；  API声明：centerZ?: number;  差异内容：centerZ?: number; | component/common.d.ts |
| 新增API | NA | 类名：RotateAngleOptions；  API声明：perspective?: number;  差异内容：perspective?: number; | component/common.d.ts |
| 新增API | NA | 类名：SheetType；  API声明：SIDE = 3  差异内容：SIDE = 3 | component/common.d.ts |
| 新增API | NA | 类名：DismissReason；  API声明：SLIDE = 4  差异内容：SLIDE = 4 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface PopupBorderLinearGradient  差异内容：declare interface PopupBorderLinearGradient | component/common.d.ts |
| 新增API | NA | 类名：PopupBorderLinearGradient；  API声明：direction?: GradientDirection;  差异内容：direction?: GradientDirection; | component/common.d.ts |
| 新增API | NA | 类名：PopupBorderLinearGradient；  API声明：colors: Array<[  ResourceColor,  number  ]>;  差异内容：colors: Array<[  ResourceColor,  number  ]>; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface MenuMaskType  差异内容：declare interface MenuMaskType | component/common.d.ts |
| 新增API | NA | 类名：MenuMaskType；  API声明：color?: ResourceColor;  差异内容：color?: ResourceColor; | component/common.d.ts |
| 新增API | NA | 类名：MenuMaskType；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface ItemDragEventHandler  差异内容：declare interface ItemDragEventHandler | component/common.d.ts |
| 新增API | NA | 类名：ItemDragEventHandler；  API声明：onLongPress?: Callback<number>;  差异内容：onLongPress?: Callback<number>; | component/common.d.ts |
| 新增API | NA | 类名：ItemDragEventHandler；  API声明：onDragStart?: Callback<number>;  差异内容：onDragStart?: Callback<number>; | component/common.d.ts |
| 新增API | NA | 类名：ItemDragEventHandler；  API声明：onMoveThrough?: OnMoveHandler;  差异内容：onMoveThrough?: OnMoveHandler; | component/common.d.ts |
| 新增API | NA | 类名：ItemDragEventHandler；  API声明：onDrop?: Callback<number>;  差异内容：onDrop?: Callback<number>; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type AccessibilityTransparentCallback = (event: TouchEvent) => void;  差异内容：declare type AccessibilityTransparentCallback = (event: TouchEvent) => void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum UndoStyle  差异内容：declare enum UndoStyle | component/rich\_editor.d.ts |
| 新增API | NA | 类名：UndoStyle；  API声明：CLEAR\_STYLE = 0  差异内容：CLEAR\_STYLE = 0 | component/rich\_editor.d.ts |
| 新增API | NA | 类名：UndoStyle；  API声明：KEEP\_STYLE = 1  差异内容：KEEP\_STYLE = 1 | component/rich\_editor.d.ts |
| 新增API | NA | 类名：SearchType；  API声明：ONE\_TIME\_CODE = 14  差异内容：ONE\_TIME\_CODE = 14 | component/search.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface DecorationOptions  差异内容：declare interface DecorationOptions | component/styled\_string.d.ts |
| 新增API | NA | 类名：DecorationOptions；  API声明：enableMultiType?: boolean;  差异内容：enableMultiType?: boolean; | component/styled\_string.d.ts |
| 新增API | NA | 类名：TextAreaType；  API声明：ONE\_TIME\_CODE = 14  差异内容：ONE\_TIME\_CODE = 14 | component/text\_area.d.ts |
| 新增API | NA | 类名：InputType；  API声明：ONE\_TIME\_CODE = 14  差异内容：ONE\_TIME\_CODE = 14 | component/text\_input.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface PickerBackgroundStyle  差异内容：declare interface PickerBackgroundStyle | component/text\_picker.d.ts |
| 新增API | NA | 类名：PickerBackgroundStyle；  API声明：color?: ResourceColor;  差异内容：color?: ResourceColor; | component/text\_picker.d.ts |
| 新增API | NA | 类名：PickerBackgroundStyle；  API声明：borderRadius?: LengthMetrics | BorderRadiuses | LocalizedBorderRadiuses;  差异内容：borderRadius?: LengthMetrics | BorderRadiuses | LocalizedBorderRadiuses; | component/text\_picker.d.ts |
| 新增API | NA | 类名：FullScreenLaunchComponent；  API声明：onReceive?: Callback<Record<string, Object>>;  差异内容：onReceive?: Callback<Record<string, Object>>; | api/@ohos.arkui.advanced.FullScreenLaunchComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：declare type InputEventType = TouchEvent | MouseEvent | AxisEvent;  差异内容：declare type InputEventType = TouchEvent | MouseEvent | AxisEvent; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：global；  API声明：export enum UIState  差异内容：export enum UIState | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：UIState；  API声明：NORMAL = 0  差异内容：NORMAL = 0 | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：UIState；  API声明：PRESSED = 1 << 0  差异内容：PRESSED = 1 << 0 | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：UIState；  API声明：FOCUSED = 1 << 1  差异内容：FOCUSED = 1 << 1 | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：UIState；  API声明：DISABLED = 1 << 2  差异内容：DISABLED = 1 << 2 | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：UIState；  API声明：SELECTED = 1 << 3  差异内容：SELECTED = 1 << 3 | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type UIStatesChangeHandler = (node: FrameNode, currentUIStates: number) => void;  差异内容：declare type UIStatesChangeHandler = (node: FrameNode, currentUIStates: number) => void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type PromptActionCommonState = import('../api/@ohos.promptAction').promptAction.CommonState;  差异内容：declare type PromptActionCommonState = import('../api/@ohos.promptAction').promptAction.CommonState; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：TouchType；  API声明：HOVER\_ENTER = 9  差异内容：HOVER\_ENTER = 9 | component/enums.d.ts |
| 新增API | NA | 类名：TouchType；  API声明：HOVER\_MOVE = 10  差异内容：HOVER\_MOVE = 10 | component/enums.d.ts |
| 新增API | NA | 类名：TouchType；  API声明：HOVER\_EXIT = 11  差异内容：HOVER\_EXIT = 11 | component/enums.d.ts |
| 新增API | NA | 类名：TouchType；  API声明：HOVER\_CANCEL = 12  差异内容：HOVER\_CANCEL = 12 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum LocalizedAlignment  差异内容：declare enum LocalizedAlignment | component/enums.d.ts |
| 新增API | NA | 类名：LocalizedAlignment；  API声明：TOP\_START = "top\_start"  差异内容：TOP\_START = "top\_start" | component/enums.d.ts |
| 新增API | NA | 类名：LocalizedAlignment；  API声明：TOP = "top"  差异内容：TOP = "top" | component/enums.d.ts |
| 新增API | NA | 类名：LocalizedAlignment；  API声明：TOP\_END = "top\_end"  差异内容：TOP\_END = "top\_end" | component/enums.d.ts |
| 新增API | NA | 类名：LocalizedAlignment；  API声明：START = "start"  差异内容：START = "start" | component/enums.d.ts |
| 新增API | NA | 类名：LocalizedAlignment；  API声明：CENTER = "center"  差异内容：CENTER = "center" | component/enums.d.ts |
| 新增API | NA | 类名：LocalizedAlignment；  API声明：END = "end"  差异内容：END = "end" | component/enums.d.ts |
| 新增API | NA | 类名：LocalizedAlignment；  API声明：BOTTOM\_START = "bottom\_start"  差异内容：BOTTOM\_START = "bottom\_start" | component/enums.d.ts |
| 新增API | NA | 类名：LocalizedAlignment；  API声明：BOTTOM = "bottom"  差异内容：BOTTOM = "bottom" | component/enums.d.ts |
| 新增API | NA | 类名：LocalizedAlignment；  API声明：BOTTOM\_END = "bottom\_end"  差异内容：BOTTOM\_END = "bottom\_end" | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum AnimationPropertyType  差异内容：declare enum AnimationPropertyType | component/enums.d.ts |
| 新增API | NA | 类名：AnimationPropertyType；  API声明：ROTATION = 0  差异内容：ROTATION = 0 | component/enums.d.ts |
| 新增API | NA | 类名：AnimationPropertyType；  API声明：TRANSLATION = 1  差异内容：TRANSLATION = 1 | component/enums.d.ts |
| 新增API | NA | 类名：AnimationPropertyType；  API声明：SCALE = 2  差异内容：SCALE = 2 | component/enums.d.ts |
| 新增API | NA | 类名：AnimationPropertyType；  API声明：OPACITY = 3  差异内容：OPACITY = 3 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface EventLocationInfo  差异内容：declare interface EventLocationInfo | component/gesture.d.ts |
| 新增API | NA | 类名：EventLocationInfo；  API声明：x: number;  差异内容：x: number; | component/gesture.d.ts |
| 新增API | NA | 类名：EventLocationInfo；  API声明：y: number;  差异内容：y: number; | component/gesture.d.ts |
| 新增API | NA | 类名：EventLocationInfo；  API声明：windowX: number;  差异内容：windowX: number; | component/gesture.d.ts |
| 新增API | NA | 类名：EventLocationInfo；  API声明：windowY: number;  差异内容：windowY: number; | component/gesture.d.ts |
| 新增API | NA | 类名：EventLocationInfo；  API声明：displayX: number;  差异内容：displayX: number; | component/gesture.d.ts |
| 新增API | NA | 类名：EventLocationInfo；  API声明：displayY: number;  差异内容：displayY: number; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type BusinessError<T> = import('../api/@ohos.base').BusinessError<T>;  差异内容：declare type BusinessError<T> = import('../api/@ohos.base').BusinessError<T>; | component/image.d.ts |
| 新增API | NA | 类名：ParticleEmitterShape；  API声明：ANNULUS = 'annulus'  差异内容：ANNULUS = 'annulus' | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface ParticleAnnulusRegion  差异内容：declare interface ParticleAnnulusRegion | component/particle.d.ts |
| 新增API | NA | 类名：ParticleAnnulusRegion；  API声明：center?: PositionT<LengthMetrics>;  差异内容：center?: PositionT<LengthMetrics>; | component/particle.d.ts |
| 新增API | NA | 类名：ParticleAnnulusRegion；  API声明：outerRadius: LengthMetrics;  差异内容：outerRadius: LengthMetrics; | component/particle.d.ts |
| 新增API | NA | 类名：ParticleAnnulusRegion；  API声明：innerRadius: LengthMetrics;  差异内容：innerRadius: LengthMetrics; | component/particle.d.ts |
| 新增API | NA | 类名：ParticleAnnulusRegion；  API声明：startAngle?: number;  差异内容：startAngle?: number; | component/particle.d.ts |
| 新增API | NA | 类名：ParticleAnnulusRegion；  API声明：endAngle?: number;  差异内容：endAngle?: number; | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum SaveButtonTipPosition  差异内容：declare enum SaveButtonTipPosition | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveButtonTipPosition；  API声明：ABOVE\_BOTTOM = 0  差异内容：ABOVE\_BOTTOM = 0 | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveButtonTipPosition；  API声明：BELOW\_TOP = 1  差异内容：BELOW\_TOP = 1 | component/save\_button.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface MenuOutlineOptions  差异内容：declare interface MenuOutlineOptions | component/select.d.ts |
| 新增API | NA | 类名：MenuOutlineOptions；  API声明：width?: Dimension | EdgeOutlineWidths;  差异内容：width?: Dimension | EdgeOutlineWidths; | component/select.d.ts |
| 新增API | NA | 类名：MenuOutlineOptions；  API声明：color?: ResourceColor | EdgeColors;  差异内容：color?: ResourceColor | EdgeColors; | component/select.d.ts |
| 新增API | NA | 类名：global；  API声明：interface SliderCustomContentOptions  差异内容：interface SliderCustomContentOptions | component/slider.d.ts |
| 新增API | NA | 类名：SliderCustomContentOptions；  API声明：accessibilityText?: ResourceStr;  差异内容：accessibilityText?: ResourceStr; | component/slider.d.ts |
| 新增API | NA | 类名：SliderCustomContentOptions；  API声明：accessibilityDescription?: ResourceStr;  差异内容：accessibilityDescription?: ResourceStr; | component/slider.d.ts |
| 新增API | NA | 类名：SliderCustomContentOptions；  API声明：accessibilityLevel?: string;  差异内容：accessibilityLevel?: string; | component/slider.d.ts |
| 新增API | NA | 类名：SliderCustomContentOptions；  API声明：accessibilityGroup?: boolean;  差异内容：accessibilityGroup?: boolean; | component/slider.d.ts |
| 新增API | NA | 类名：global；  API声明：interface SliderPrefixOptions  差异内容：interface SliderPrefixOptions | component/slider.d.ts |
| 新增API | NA | 类名：global；  API声明：interface SliderSuffixOptions  差异内容：interface SliderSuffixOptions | component/slider.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum SuperscriptStyle  差异内容：declare enum SuperscriptStyle | component/text\_common.d.ts |
| 新增API | NA | 类名：SuperscriptStyle；  API声明：NORMAL = 0  差异内容：NORMAL = 0 | component/text\_common.d.ts |
| 新增API | NA | 类名：SuperscriptStyle；  API声明：SUPERSCRIPT = 1  差异内容：SUPERSCRIPT = 1 | component/text\_common.d.ts |
| 新增API | NA | 类名：SuperscriptStyle；  API声明：SUBSCRIPT = 2  差异内容：SUBSCRIPT = 2 | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum AutoCapitalizationMode  差异内容：declare enum AutoCapitalizationMode | component/text\_common.d.ts |
| 新增API | NA | 类名：AutoCapitalizationMode；  API声明：NONE = 0  差异内容：NONE = 0 | component/text\_common.d.ts |
| 新增API | NA | 类名：AutoCapitalizationMode；  API声明：WORDS = 1  差异内容：WORDS = 1 | component/text\_common.d.ts |
| 新增API | NA | 类名：AutoCapitalizationMode；  API声明：SENTENCES = 2  差异内容：SENTENCES = 2 | component/text\_common.d.ts |
| 新增API | NA | 类名：AutoCapitalizationMode；  API声明：ALL\_CHARACTERS = 3  差异内容：ALL\_CHARACTERS = 3 | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface LineSpacingOptions  差异内容：declare interface LineSpacingOptions | component/text\_common.d.ts |
| 新增API | NA | 类名：LineSpacingOptions；  API声明：onlyBetweenLines?: boolean;  差异内容：onlyBetweenLines?: boolean; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface MaxLinesOptions  差异内容：declare interface MaxLinesOptions | component/text\_common.d.ts |
| 新增API | NA | 类名：MaxLinesOptions；  API声明：overflowMode?: MaxLinesMode;  差异内容：overflowMode?: MaxLinesMode; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum MaxLinesMode  差异内容：declare enum MaxLinesMode | component/text\_common.d.ts |
| 新增API | NA | 类名：MaxLinesMode；  API声明：CLIP = 0  差异内容：CLIP = 0 | component/text\_common.d.ts |
| 新增API | NA | 类名：MaxLinesMode；  API声明：SCROLL = 1  差异内容：SCROLL = 1 | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface IMEClient  差异内容：declare interface IMEClient | component/text\_common.d.ts |
| 新增API | NA | 类名：IMEClient；  API声明：nodeId: number;  差异内容：nodeId: number; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface ScrollBarMargin  差异内容：declare interface ScrollBarMargin | component/units.d.ts |
| 新增API | NA | 类名：ScrollBarMargin；  API声明：start?: LengthMetrics;  差异内容：start?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：ScrollBarMargin；  API声明：end?: LengthMetrics;  差异内容：end?: LengthMetrics; | component/units.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\arkui\StepperModifier.d.ts  差异内容：ArkUI | api/arkui/StepperModifier.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：component\toolbar.d.ts  差异内容：ArkUI | component/toolbar.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：TextStyle；  API声明：readonly strokeWidth?: number;  差异内容：readonly strokeWidth?: number; | component/styled\_string.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：TextStyle；  API声明：readonly strokeColor?: ResourceColor;  差异内容：readonly strokeColor?: ResourceColor; | component/styled\_string.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：TextStyle；  API声明：readonly superscript?: SuperscriptStyle;  差异内容：readonly superscript?: SuperscriptStyle; | component/styled\_string.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：DecorationStyle；  API声明：readonly thicknessScale?: number;  差异内容：readonly thicknessScale?: number; | component/styled\_string.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：DecorationStyle；  API声明：readonly options?: DecorationOptions;  差异内容：readonly options?: DecorationOptions; | component/styled\_string.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIObserver；  API声明：on(type: 'navDestinationUpdateByUniqueId', navigationUniqueId: number, callback: Callback<observer.NavDestinationInfo>): void;  差异内容：on(type: 'navDestinationUpdateByUniqueId', navigationUniqueId: number, callback: Callback<observer.NavDestinationInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIObserver；  API声明：off(type: 'navDestinationUpdateByUniqueId', navigationUniqueId: number, callback?: Callback<observer.NavDestinationInfo>): void;  差异内容：off(type: 'navDestinationUpdateByUniqueId', navigationUniqueId: number, callback?: Callback<observer.NavDestinationInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIObserver；  API声明：on(type: 'nodeRenderState', nodeIdentity: NodeIdentity, callback: NodeRenderStateChangeCallback): void;  差异内容：on(type: 'nodeRenderState', nodeIdentity: NodeIdentity, callback: NodeRenderStateChangeCallback): void; | api/@ohos.arkui.UIContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIObserver；  API声明：off(type: 'nodeRenderState', nodeIdentity: NodeIdentity, callback?: NodeRenderStateChangeCallback): void;  差异内容：off(type: 'nodeRenderState', nodeIdentity: NodeIdentity, callback?: NodeRenderStateChangeCallback): void; | api/@ohos.arkui.UIContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：DragController；  API声明：enableDropDisallowedBadge(enabled: boolean): void;  差异内容：enableDropDisallowedBadge(enabled: boolean): void; | api/@ohos.arkui.UIContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：FocusController；  API声明：isActive(): boolean;  差异内容：isActive(): boolean; | api/@ohos.arkui.UIContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UIContext；  API声明：isAvailable(): boolean;  差异内容：isAvailable(): boolean; | api/@ohos.arkui.UIContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextMenuController；  API声明：static disableSystemServiceMenuItems(disable: boolean): void;  差异内容：static disableSystemServiceMenuItems(disable: boolean): void; | api/@ohos.arkui.UIContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextMenuController；  API声明：static disableMenuItems(items: Array<TextMenuItemId>): void;  差异内容：static disableMenuItems(items: Array<TextMenuItemId>): void; | api/@ohos.arkui.UIContext.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CommonController；  API声明：getState(): CommonState;  差异内容：getState(): CommonState; | api/@ohos.promptAction.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CanvasPath；  API声明：roundRect(x: number, y: number, w: number, h: number, radii?: number | Array<number>): void;  差异内容：roundRect(x: number, y: number, w: number, h: number, radii?: number | Array<number>): void; | component/canvas.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：LayoutPolicy；  API声明：static readonly wrapContent: LayoutPolicy;  差异内容：static readonly wrapContent: LayoutPolicy; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：LayoutPolicy；  API声明：static readonly fixAtIdealSize: LayoutPolicy;  差异内容：static readonly fixAtIdealSize: LayoutPolicy; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CommonMethod；  API声明：onAccessibilityHoverTransparent(callback: AccessibilityTransparentCallback): T;  差异内容：onAccessibilityHoverTransparent(callback: AccessibilityTransparentCallback): T; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CommonMethod；  API声明：layoutGravity(alignment: LocalizedAlignment): T;  差异内容：layoutGravity(alignment: LocalizedAlignment): T; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CommonMethod；  API声明：toolbar(value: CustomBuilder): T;  差异内容：toolbar(value: CustomBuilder): T; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CommonMethod；  API声明：onAccessibilityActionIntercept(callback: AccessibilityActionInterceptCallback): T;  差异内容：onAccessibilityActionIntercept(callback: AccessibilityActionInterceptCallback): T; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：ScrollableCommonMethod；  API声明：scrollBarMargin(margin: ScrollBarMargin): T;  差异内容：scrollBarMargin(margin: ScrollBarMargin): T; | component/common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：RichEditorAttribute；  API声明：undoStyle(style: Optional<UndoStyle>): RichEditorAttribute;  差异内容：undoStyle(style: Optional<UndoStyle>): RichEditorAttribute; | component/rich\_editor.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SearchAttribute；  API声明：onWillAttachIME(callback: Callback<IMEClient>): SearchAttribute;  差异内容：onWillAttachIME(callback: Callback<IMEClient>): SearchAttribute; | component/search.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SearchAttribute；  API声明：autoCapitalizationMode(mode: AutoCapitalizationMode): SearchAttribute;  差异内容：autoCapitalizationMode(mode: AutoCapitalizationMode): SearchAttribute; | component/search.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SearchAttribute；  API声明：strokeWidth(width: Optional<LengthMetrics>): SearchAttribute;  差异内容：strokeWidth(width: Optional<LengthMetrics>): SearchAttribute; | component/search.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SearchAttribute；  API声明：strokeColor(color: Optional<ResourceColor>): SearchAttribute;  差异内容：strokeColor(color: Optional<ResourceColor>): SearchAttribute; | component/search.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TabsAttribute；  API声明：animationCurve(curve: Curve | ICurve): TabsAttribute;  差异内容：animationCurve(curve: Curve | ICurve): TabsAttribute; | component/tabs.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextAttribute；  API声明：optimizeTrailingSpace(optimize: Optional<boolean>): TextAttribute;  差异内容：optimizeTrailingSpace(optimize: Optional<boolean>): TextAttribute; | component/text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextAreaAttribute；  API声明：minLines(lines: Optional<number>): TextAreaAttribute;  差异内容：minLines(lines: Optional<number>): TextAreaAttribute; | component/text\_area.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextAreaAttribute；  API声明：autoCapitalizationMode(mode: AutoCapitalizationMode): TextAreaAttribute;  差异内容：autoCapitalizationMode(mode: AutoCapitalizationMode): TextAreaAttribute; | component/text\_area.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextAreaAttribute；  API声明：strokeWidth(width: Optional<LengthMetrics>): TextAreaAttribute;  差异内容：strokeWidth(width: Optional<LengthMetrics>): TextAreaAttribute; | component/text\_area.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextAreaAttribute；  API声明：strokeColor(color: Optional<ResourceColor>): TextAreaAttribute;  差异内容：strokeColor(color: Optional<ResourceColor>): TextAreaAttribute; | component/text\_area.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextInputAttribute；  API声明：onWillAttachIME(callback: Callback<IMEClient>): TextInputAttribute;  差异内容：onWillAttachIME(callback: Callback<IMEClient>): TextInputAttribute; | component/text\_input.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextInputAttribute；  API声明：autoCapitalizationMode(mode: AutoCapitalizationMode): TextInputAttribute;  差异内容：autoCapitalizationMode(mode: AutoCapitalizationMode): TextInputAttribute; | component/text\_input.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextInputAttribute；  API声明：strokeWidth(width: Optional<LengthMetrics>): TextInputAttribute;  差异内容：strokeWidth(width: Optional<LengthMetrics>): TextInputAttribute; | component/text\_input.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextInputAttribute；  API声明：strokeColor(color: Optional<ResourceColor>): TextInputAttribute;  差异内容：strokeColor(color: Optional<ResourceColor>): TextInputAttribute; | component/text\_input.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextInputAttribute；  API声明：enableAutoFillAnimation(enabled: Optional<boolean>): TextInputAttribute;  差异内容：enableAutoFillAnimation(enabled: Optional<boolean>): TextInputAttribute; | component/text\_input.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextPickerAttribute；  API声明：selectedBackgroundStyle(style: Optional<PickerBackgroundStyle>): TextPickerAttribute;  差异内容：selectedBackgroundStyle(style: Optional<PickerBackgroundStyle>): TextPickerAttribute; | component/text\_picker.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：XComponentController；  API声明：lockCanvas(): DrawingCanvas | null;  差异内容：lockCanvas(): DrawingCanvas | null; | component/xcomponent.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：XComponentController；  API声明：unlockCanvasAndPost(canvas: DrawingCanvas): void;  差异内容：unlockCanvasAndPost(canvas: DrawingCanvas): void; | component/xcomponent.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：XComponentAttribute；  API声明：hdrBrightness(brightness: number): XComponentAttribute;  差异内容：hdrBrightness(brightness: number): XComponentAttribute; | component/xcomponent.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：BuilderNode；  API声明：postInputEvent(event: InputEventType): boolean;  差异内容：postInputEvent(event: InputEventType): boolean; | api/arkui/BuilderNode.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：BuilderNode；  API声明：isDisposed(): boolean;  差异内容：isDisposed(): boolean; | api/arkui/BuilderNode.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：ComponentContent；  API声明：isDisposed(): boolean;  差异内容：isDisposed(): boolean; | api/arkui/ComponentContent.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：FrameNode；  API声明：isDisposed(): boolean;  差异内容：isDisposed(): boolean; | api/arkui/FrameNode.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：FrameNode；  API声明：addSupportedUIStates(uiStates: number, statesChangeHandler: UIStatesChangeHandler, excludeInner?: boolean): void;  差异内容：addSupportedUIStates(uiStates: number, statesChangeHandler: UIStatesChangeHandler, excludeInner?: boolean): void; | api/arkui/FrameNode.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：FrameNode；  API声明：removeSupportedUIStates(uiStates: number): void;  差异内容：removeSupportedUIStates(uiStates: number): void; | api/arkui/FrameNode.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：FrameNode；  API声明：createAnimation(property: AnimationPropertyType, startValue: Optional<number[]>, endValue: number[], param: AnimateParam): boolean;  差异内容：createAnimation(property: AnimationPropertyType, startValue: Optional<number[]>, endValue: number[], param: AnimateParam): boolean; | api/arkui/FrameNode.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：FrameNode；  API声明：cancelAnimations(properties: AnimationPropertyType[]): boolean;  差异内容：cancelAnimations(properties: AnimationPropertyType[]): boolean; | api/arkui/FrameNode.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：FrameNode；  API声明：getNodePropertyValue(property: AnimationPropertyType): number[];  差异内容：getNodePropertyValue(property: AnimationPropertyType): number[]; | api/arkui/FrameNode.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：NodeAdapter；  API声明：isDisposed(): boolean;  差异内容：isDisposed(): boolean; | api/arkui/FrameNode.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：RenderNode；  API声明：isDisposed(): boolean;  差异内容：isDisposed(): boolean; | api/arkui/RenderNode.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：CustomDialogController；  API声明：getState(): PromptActionCommonState;  差异内容：getState(): PromptActionCommonState; | component/custom\_dialog\_controller.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：MenuAttribute；  API声明：subMenuExpandSymbol(symbol: SymbolGlyphModifier): MenuAttribute;  差异内容：subMenuExpandSymbol(symbol: SymbolGlyphModifier): MenuAttribute; | component/menu.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：NavigationAttribute；  API声明：splitPlaceholder(placeholder: ComponentContent): NavigationAttribute;  差异内容：splitPlaceholder(placeholder: ComponentContent): NavigationAttribute; | component/navigation.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：RefreshAttribute；  API声明：maxPullDownDistance(distance: Optional<number>): RefreshAttribute;  差异内容：maxPullDownDistance(distance: Optional<number>): RefreshAttribute; | component/refresh.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SaveButtonAttribute；  API声明：setIcon(icon: Resource): SaveButtonAttribute;  差异内容：setIcon(icon: Resource): SaveButtonAttribute; | component/save\_button.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SaveButtonAttribute；  API声明：setText(text: string | Resource): SaveButtonAttribute;  差异内容：setText(text: string | Resource): SaveButtonAttribute; | component/save\_button.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SaveButtonAttribute；  API声明：iconSize(size: Dimension | SizeOptions): SaveButtonAttribute;  差异内容：iconSize(size: Dimension | SizeOptions): SaveButtonAttribute; | component/save\_button.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SaveButtonAttribute；  API声明：iconBorderRadius(radius: Dimension | BorderRadiuses): SaveButtonAttribute;  差异内容：iconBorderRadius(radius: Dimension | BorderRadiuses): SaveButtonAttribute; | component/save\_button.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SaveButtonAttribute；  API声明：stateEffect(enabled: boolean): SaveButtonAttribute;  差异内容：stateEffect(enabled: boolean): SaveButtonAttribute; | component/save\_button.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SaveButtonAttribute；  API声明：tipPosition(position: SaveButtonTipPosition): SaveButtonAttribute;  差异内容：tipPosition(position: SaveButtonTipPosition): SaveButtonAttribute; | component/save\_button.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：ScrollBarAttribute；  API声明：scrollBarColor(color: Optional<ColorMetrics>): ScrollBarAttribute;  差异内容：scrollBarColor(color: Optional<ColorMetrics>): ScrollBarAttribute; | component/scroll\_bar.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SelectAttribute；  API声明：textModifier(modifier: Optional<TextModifier>): SelectAttribute;  差异内容：textModifier(modifier: Optional<TextModifier>): SelectAttribute; | component/select.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SelectAttribute；  API声明：arrowModifier(modifier: Optional<SymbolGlyphModifier>): SelectAttribute;  差异内容：arrowModifier(modifier: Optional<SymbolGlyphModifier>): SelectAttribute; | component/select.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SelectAttribute；  API声明：optionTextModifier(modifier: Optional<TextModifier>): SelectAttribute;  差异内容：optionTextModifier(modifier: Optional<TextModifier>): SelectAttribute; | component/select.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SelectAttribute；  API声明：selectedOptionTextModifier(modifier: Optional<TextModifier>): SelectAttribute;  差异内容：selectedOptionTextModifier(modifier: Optional<TextModifier>): SelectAttribute; | component/select.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SelectAttribute；  API声明：menuOutline(outline: MenuOutlineOptions): SelectAttribute;  差异内容：menuOutline(outline: MenuOutlineOptions): SelectAttribute; | component/select.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SelectAttribute；  API声明：showInSubWindow(showInSubWindow: Optional<boolean>): SelectAttribute;  差异内容：showInSubWindow(showInSubWindow: Optional<boolean>): SelectAttribute; | component/select.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SelectAttribute；  API声明：showDefaultSelectedIcon(show: boolean): SelectAttribute;  差异内容：showDefaultSelectedIcon(show: boolean): SelectAttribute; | component/select.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SliderAttribute；  API声明：prefix(content: ComponentContent, options?: SliderPrefixOptions): SliderAttribute;  差异内容：prefix(content: ComponentContent, options?: SliderPrefixOptions): SliderAttribute; | component/slider.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SliderAttribute；  API声明：suffix(content: ComponentContent, options?: SliderSuffixOptions): SliderAttribute;  差异内容：suffix(content: ComponentContent, options?: SliderSuffixOptions): SliderAttribute; | component/slider.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：SwiperAttribute；  API声明：maintainVisibleContentPosition(enabled: boolean): SwiperAttribute;  差异内容：maintainVisibleContentPosition(enabled: boolean): SwiperAttribute; | component/swiper.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextMenuItemId；  API声明：static readonly url: TextMenuItemId;  差异内容：static readonly url: TextMenuItemId; | component/text\_common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextMenuItemId；  API声明：static readonly email: TextMenuItemId;  差异内容：static readonly email: TextMenuItemId; | component/text\_common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextMenuItemId；  API声明：static readonly phoneNumber: TextMenuItemId;  差异内容：static readonly phoneNumber: TextMenuItemId; | component/text\_common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextMenuItemId；  API声明：static readonly address: TextMenuItemId;  差异内容：static readonly address: TextMenuItemId; | component/text\_common.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextMenuItemId；  API声明：static readonly dateTime: TextMenuItemId;  差异内容：static readonly dateTime: TextMenuItemId; | component/text\_common.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：CommonMethod；  API声明：rotate(options: Optional<RotateOptions>): T;  差异内容：rotate(options: Optional<RotateOptions>): T; | 类名：CommonMethod；  API声明：rotate(options: Optional<RotateOptions | RotateAngleOptions>): T;  差异内容：rotate(options: Optional<RotateOptions | RotateAngleOptions>): T; | component/common.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：CommonMethod；  API声明：align(value: Alignment): T;  差异内容：align(value: Alignment): T; | 类名：CommonMethod；  API声明：align(alignment: Alignment | LocalizedAlignment): T;  差异内容：align(alignment: Alignment | LocalizedAlignment): T; | component/common.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：DynamicNode；  API声明：onMove(handler: Optional<OnMoveHandler>): T;  差异内容：onMove(handler: Optional<OnMoveHandler>): T; | 类名：DynamicNode；  API声明：onMove(handler: Optional<OnMoveHandler>, eventHandler: ItemDragEventHandler): T;  差异内容：onMove(handler: Optional<OnMoveHandler>, eventHandler: ItemDragEventHandler): T; | component/common.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：TabsAttribute；  API声明：barHeight(value: Length): TabsAttribute;  差异内容：barHeight(value: Length): TabsAttribute; | 类名：TabsAttribute；  API声明：barHeight(height: Length, noMinHeightLimit: boolean): TabsAttribute;  差异内容：barHeight(height: Length, noMinHeightLimit: boolean): TabsAttribute; | component/tabs.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：TextAttribute；  API声明：lineSpacing(value: LengthMetrics): TextAttribute;  差异内容：lineSpacing(value: LengthMetrics): TextAttribute; | 类名：TextAttribute；  API声明：lineSpacing(value: LengthMetrics, options?: LineSpacingOptions): TextAttribute;  差异内容：lineSpacing(value: LengthMetrics, options?: LineSpacingOptions): TextAttribute; | component/text.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：TextAreaAttribute；  API声明：maxLines(value: number): TextAreaAttribute;  差异内容：maxLines(value: number): TextAreaAttribute; | 类名：TextAreaAttribute；  API声明：maxLines(lines: number, options: MaxLinesOptions): TextAreaAttribute;  差异内容：maxLines(lines: number, options: MaxLinesOptions): TextAreaAttribute; | component/text\_area.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：TextAreaAttribute；  API声明：lineSpacing(value: LengthMetrics): TextAreaAttribute;  差异内容：lineSpacing(value: LengthMetrics): TextAreaAttribute; | 类名：TextAreaAttribute；  API声明：lineSpacing(value: LengthMetrics, options?: LineSpacingOptions): TextAreaAttribute;  差异内容：lineSpacing(value: LengthMetrics, options?: LineSpacingOptions): TextAreaAttribute; | component/text\_area.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：on(type: 'keyboardWillShow', callback: Callback<KeyboardInfo>): void;  差异内容：on(type: 'keyboardWillShow', callback: Callback<KeyboardInfo>): void; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：off(type: 'keyboardWillShow', callback?: Callback<KeyboardInfo>): void;  差异内容：off(type: 'keyboardWillShow', callback?: Callback<KeyboardInfo>): void; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：on(type: 'keyboardWillHide', callback: Callback<KeyboardInfo>): void;  差异内容：on(type: 'keyboardWillHide', callback: Callback<KeyboardInfo>): void; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：off(type: 'keyboardWillHide', callback?: Callback<KeyboardInfo>): void;  差异内容：off(type: 'keyboardWillHide', callback?: Callback<KeyboardInfo>): void; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：on(type: 'windowStatusDidChange', callback: Callback<WindowStatusType>): void;  差异内容：on(type: 'windowStatusDidChange', callback: Callback<WindowStatusType>): void; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：off(type: 'windowStatusDidChange', callback?: Callback<WindowStatusType>): void;  差异内容：off(type: 'windowStatusDidChange', callback?: Callback<WindowStatusType>): void; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：enableDrag(enable: boolean): Promise<void>;  差异内容：enableDrag(enable: boolean): Promise<void>; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：setWindowTransitionAnimation(transitionType: WindowTransitionType, animation: TransitionAnimation): Promise<void>;  差异内容：setWindowTransitionAnimation(transitionType: WindowTransitionType, animation: TransitionAnimation): Promise<void>; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Window；  API声明：getWindowTransitionAnimation(transitionType: WindowTransitionType): TransitionAnimation | undefined;  差异内容：getWindowTransitionAnimation(transitionType: WindowTransitionType): TransitionAnimation | undefined; | api/@ohos.window.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：DragEvent；  API声明：getDisplayId(): number;  差异内容：getDisplayId(): number; | component/common.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：ComponentObserver；  API声明：on(type: 'drawChildren', callback: Callback<void>): void;  差异内容：on(type: 'drawChildren', callback: Callback<void>): void; | api/@ohos.arkui.inspector.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：ComponentObserver；  API声明：off(type: 'drawChildren', callback?: Callback<void>): void;  差异内容：off(type: 'drawChildren', callback?: Callback<void>): void; | api/@ohos.arkui.inspector.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：DecorButtonStyle；  API声明：buttonIconSize?: number;  差异内容：buttonIconSize?: number; | api/@ohos.window.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：DecorButtonStyle；  API声明：buttonBackgroundCornerRadius?: number;  差异内容：buttonBackgroundCornerRadius?: number; | api/@ohos.window.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：KeyboardInfo；  API声明：animated?: boolean;  差异内容：animated?: boolean; | api/@ohos.window.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：KeyboardInfo；  API声明：config?: WindowAnimationConfig;  差异内容：config?: WindowAnimationConfig; | api/@ohos.window.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：SubWindowOptions；  API声明：outlineEnabled?: boolean;  差异内容：outlineEnabled?: boolean; | api/@ohos.window.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：PopupCommonOptions；  API声明：outlineWidth?: Dimension;  差异内容：outlineWidth?: Dimension; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：PopupCommonOptions；  API声明：borderWidth?: Dimension;  差异内容：borderWidth?: Dimension; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：PopupCommonOptions；  API声明：outlineLinearGradient?: PopupBorderLinearGradient;  差异内容：outlineLinearGradient?: PopupBorderLinearGradient; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：PopupCommonOptions；  API声明：borderLinearGradient?: PopupBorderLinearGradient;  差异内容：borderLinearGradient?: PopupBorderLinearGradient; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：PopupOptions；  API声明：outlineWidth?: Dimension;  差异内容：outlineWidth?: Dimension; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：PopupOptions；  API声明：borderWidth?: Dimension;  差异内容：borderWidth?: Dimension; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：PopupOptions；  API声明：outlineLinearGradient?: PopupBorderLinearGradient;  差异内容：outlineLinearGradient?: PopupBorderLinearGradient; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：PopupOptions；  API声明：borderLinearGradient?: PopupBorderLinearGradient;  差异内容：borderLinearGradient?: PopupBorderLinearGradient; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CustomPopupOptions；  API声明：outlineWidth?: Dimension;  差异内容：outlineWidth?: Dimension; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CustomPopupOptions；  API声明：borderWidth?: Dimension;  差异内容：borderWidth?: Dimension; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CustomPopupOptions；  API声明：outlineLinearGradient?: PopupBorderLinearGradient;  差异内容：outlineLinearGradient?: PopupBorderLinearGradient; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：CustomPopupOptions；  API声明：borderLinearGradient?: PopupBorderLinearGradient;  差异内容：borderLinearGradient?: PopupBorderLinearGradient; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ContextMenuOptions；  API声明：outlineColor?: ResourceColor | EdgeColors;  差异内容：outlineColor?: ResourceColor | EdgeColors; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ContextMenuOptions；  API声明：outlineWidth?: Dimension | EdgeOutlineWidths;  差异内容：outlineWidth?: Dimension | EdgeOutlineWidths; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ContextMenuOptions；  API声明：mask?: boolean | MenuMaskType;  差异内容：mask?: boolean | MenuMaskType; | component/common.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：TextStyleInterface；  API声明：strokeWidth?: LengthMetrics;  差异内容：strokeWidth?: LengthMetrics; | component/styled\_string.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：TextStyleInterface；  API声明：strokeColor?: ResourceColor;  差异内容：strokeColor?: ResourceColor; | component/styled\_string.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：TextStyleInterface；  API声明：superscript?: SuperscriptStyle;  差异内容：superscript?: SuperscriptStyle; | component/styled\_string.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：DecorationStyleInterface；  API声明：thicknessScale?: number;  差异内容：thicknessScale?: number; | component/styled\_string.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：GestureStyleInterface；  API声明：onTouch?: Callback<TouchEvent>;  差异内容：onTouch?: Callback<TouchEvent>; | component/styled\_string.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：TextPickerDialogOptions；  API声明：selectedBackgroundStyle?: PickerBackgroundStyle;  差异内容：selectedBackgroundStyle?: PickerBackgroundStyle; | component/text\_picker.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：NavigationInfo；  API声明：uniqueId?: number;  差异内容：uniqueId?: number; | api/@ohos.arkui.observer.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：BuildOptions；  API声明：localStorage?: LocalStorage;  差异内容：localStorage?: LocalStorage; | api/arkui/BuilderNode.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：BaseGestureEvent；  API声明：fingerInfos?: FingerInfo[];  差异内容：fingerInfos?: FingerInfo[]; | component/gesture.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：TapGestureEvent；  API声明：tapLocation?: EventLocationInfo;  差异内容：tapLocation?: EventLocationInfo; | component/gesture.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：GestureEvent；  API声明：fingerInfos?: FingerInfo[];  差异内容：fingerInfos?: FingerInfo[]; | component/gesture.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：GestureEvent；  API声明：tapLocation?: EventLocationInfo;  差异内容：tapLocation?: EventLocationInfo; | component/gesture.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ImageError；  API声明：error?: BusinessError<void>;  差异内容：error?: BusinessError<void>; | component/image.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EmitterProperty；  API声明：annulusRegion?: ParticleAnnulusRegion;  差异内容：annulusRegion?: ParticleAnnulusRegion; | component/particle.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EmitterOptions；  API声明：annulusRegion?: ParticleAnnulusRegion;  差异内容：annulusRegion?: ParticleAnnulusRegion; | component/particle.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ScrollOptions；  API声明：canOverScroll?: boolean;  差异内容：canOverScroll?: boolean; | component/scroll.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：DecorationStyleResult；  API声明：thicknessScale?: number;  差异内容：thicknessScale?: number; | component/text\_common.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Window；  API声明：showWindow(): Promise<void>;  差异内容：showWindow(): Promise<void>; | 类名：Window；  API声明：showWindow(options: ShowWindowOptions): Promise<void>;  差异内容：showWindow(options: ShowWindowOptions): Promise<void>; | api/@ohos.window.d.ts |
| 新增导出符号 | 类名：global；  API声明：export declare function isApiVersionGreaterOrEqual(apiVersion: string): boolean;  差异内容：NA | 类名：global；  API声明：  差异内容：export declare function isApiVersionGreaterOrEqual(apiVersion: string): boolean; | api/@internal/full/global.d.ts |
| 新增导出符号 | 类名：global；  API声明：export const enum NodeRenderState  差异内容：NA | 类名：global；  API声明：  差异内容：export const enum NodeRenderState | api/@ohos.arkui.UIContext.d.ts |
