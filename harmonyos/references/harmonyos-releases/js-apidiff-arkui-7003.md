---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-7003
title: ArkUI
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Release引入的API > ArkUI
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:41396e21cd8958468017465ba8affdd95a72c4c385fd1901d4448b97b5ba05e0
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：display；  API声明：function setVirtualScreenSurface(screenId: number, surfaceId: string): Promise<void>;  差异内容：801 | 类名：display；  API声明：function setVirtualScreenSurface(screenId: number, surfaceId: string): Promise<void>;  差异内容：NA | api/@ohos.display.d.ts |
| 属性变更 | 类名：SwipeRefresherV2；  API声明：@Param  content?: string;  差异内容：string | 类名：SwipeRefresherV2；  API声明：@Param  content?: ResourceStr;  差异内容：ResourceStr | api/@ohos.arkui.advanced.SwipeRefresherV2.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare type OnOverlayBackPressCallback = () => boolean;  差异内容：export declare type OnOverlayBackPressCallback = () => boolean; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：OverlayManagerOptions；  API声明：onBackPress?: OnOverlayBackPressCallback;  差异内容：onBackPress?: OnOverlayBackPressCallback; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Window；  API声明：isInWindowPostureMode(mode: WindowPostureMode): boolean;  差异内容：isInWindowPostureMode(mode: WindowPostureMode): boolean; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：onWindowPostureModeChange(mode: WindowPostureMode, callback: Callback<boolean>): void;  差异内容：onWindowPostureModeChange(mode: WindowPostureMode, callback: Callback<boolean>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：offWindowPostureModeChange(mode: WindowPostureMode, callback?: Callback<boolean>): void;  差异内容：offWindowPostureModeChange(mode: WindowPostureMode, callback?: Callback<boolean>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：enum WindowPostureMode  差异内容：enum WindowPostureMode | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowPostureMode；  API声明：DESKTOP\_MODE = 0  差异内容：DESKTOP\_MODE = 0 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum TextEncoding  差异内容：declare enum TextEncoding | component/text\_common.d.ts |
| 新增API | NA | 类名：TextEncoding；  API声明：TEXT\_ENCODING\_UTF8 = 0  差异内容：TEXT\_ENCODING\_UTF8 = 0 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextEncoding；  API声明：TEXT\_ENCODING\_UTF16 = 1  差异内容：TEXT\_ENCODING\_UTF16 = 1 | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface SelectionContainerOptions  差异内容：export interface SelectionContainerOptions | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerOptions；  API声明：controller: SelectionContainerController;  差异内容：controller: SelectionContainerController; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare class SelectionContainerController  差异内容：export declare class SelectionContainerController | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerController；  API声明：closeSelectionMenu(): void;  差异内容：closeSelectionMenu(): void; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：SelectionContainerController；  API声明：clearTextSelection(): void;  差异内容：clearTextSelection(): void; | api/@ohos.arkui.components.SelectionContainer.d.ts |
| 新增API | NA | 类名：uiMaterial；  API声明：enum MaterialLevel  差异内容：enum MaterialLevel | api/@ohos.arkui.uiMaterial.d.ts |
| 新增API | NA | 类名：MaterialLevel；  API声明：EXQUISITE = 0  差异内容：EXQUISITE = 0 | api/@ohos.arkui.uiMaterial.d.ts |
| 新增API | NA | 类名：MaterialLevel；  API声明：GENTLE = 1  差异内容：GENTLE = 1 | api/@ohos.arkui.uiMaterial.d.ts |
| 新增API | NA | 类名：MaterialLevel；  API声明：SMOOTH = 2  差异内容：SMOOTH = 2 | api/@ohos.arkui.uiMaterial.d.ts |
| 新增API | NA | 类名：uiMaterial；  API声明：function getGlobalMaterialLevel(): MaterialLevel;  差异内容：function getGlobalMaterialLevel(): MaterialLevel; | api/@ohos.arkui.uiMaterial.d.ts |
| 新增API | NA | 类名：uiMaterial；  API声明：function isImmersiveMaterialSupported(): boolean;  差异内容：function isImmersiveMaterialSupported(): boolean; | api/@ohos.arkui.uiMaterial.d.ts |
| 起始版本有变化 | 类名：EllipseOptions；  API声明：width?: Length;  差异内容：18 | 类名：EllipseOptions；  API声明：width?: Length;  差异内容：7 | component/ellipse.d.ts |
| 起始版本有变化 | 类名：EllipseOptions；  API声明：height?: Length;  差异内容：18 | 类名：EllipseOptions；  API声明：height?: Length;  差异内容：7 | component/ellipse.d.ts |
| 起始版本有变化 | 类名：LineOptions；  API声明：width?: Length;  差异内容：18 | 类名：LineOptions；  API声明：width?: Length;  差异内容：7 | component/line.d.ts |
| 起始版本有变化 | 类名：LineOptions；  API声明：height?: Length;  差异内容：18 | 类名：LineOptions；  API声明：height?: Length;  差异内容：7 | component/line.d.ts |
| 起始版本有变化 | 类名：PathOptions；  API声明：width?: Length;  差异内容：18 | 类名：PathOptions；  API声明：width?: Length;  差异内容：7 | component/path.d.ts |
| 起始版本有变化 | 类名：PathOptions；  API声明：height?: Length;  差异内容：18 | 类名：PathOptions；  API声明：height?: Length;  差异内容：7 | component/path.d.ts |
| 起始版本有变化 | 类名：PathOptions；  API声明：commands?: ResourceStr;  差异内容：18 | 类名：PathOptions；  API声明：commands?: ResourceStr;  差异内容：7 | component/path.d.ts |
| 起始版本有变化 | 类名：PolygonOptions；  API声明：width?: Length;  差异内容：18 | 类名：PolygonOptions；  API声明：width?: Length;  差异内容：7 | component/polygon.d.ts |
| 起始版本有变化 | 类名：PolygonOptions；  API声明：height?: Length;  差异内容：18 | 类名：PolygonOptions；  API声明：height?: Length;  差异内容：7 | component/polygon.d.ts |
| 起始版本有变化 | 类名：PolylineOptions；  API声明：width?: Length;  差异内容：18 | 类名：PolylineOptions；  API声明：width?: Length;  差异内容：7 | component/polyline.d.ts |
| 起始版本有变化 | 类名：PolylineOptions；  API声明：height?: Length;  差异内容：18 | 类名：PolylineOptions；  API声明：height?: Length;  差异内容：7 | component/polyline.d.ts |
| 起始版本有变化 | 类名：RectOptions；  API声明：width?: Length;  差异内容：18 | 类名：RectOptions；  API声明：width?: Length;  差异内容：7 | component/rect.d.ts |
| 起始版本有变化 | 类名：RectOptions；  API声明：height?: Length;  差异内容：18 | 类名：RectOptions；  API声明：height?: Length;  差异内容：7 | component/rect.d.ts |
| 起始版本有变化 | 类名：RectOptions；  API声明：radius?: Length | Array<any>;  差异内容：18 | 类名：RectOptions；  API声明：radius?: Length | Array<any>;  差异内容：7 | component/rect.d.ts |
| 起始版本有变化 | 类名：RoundedRectOptions；  API声明：width?: Length;  差异内容：18 | 类名：RoundedRectOptions；  API声明：width?: Length;  差异内容：7 | component/rect.d.ts |
| 起始版本有变化 | 类名：RoundedRectOptions；  API声明：height?: Length;  差异内容：18 | 类名：RoundedRectOptions；  API声明：height?: Length;  差异内容：7 | component/rect.d.ts |
| 起始版本有变化 | 类名：RoundedRectOptions；  API声明：radiusWidth?: Length;  差异内容：18 | 类名：RoundedRectOptions；  API声明：radiusWidth?: Length;  差异内容：7 | component/rect.d.ts |
| 起始版本有变化 | 类名：RoundedRectOptions；  API声明：radiusHeight?: Length;  差异内容：18 | 类名：RoundedRectOptions；  API声明：radiusHeight?: Length;  差异内容：7 | component/rect.d.ts |
| 起始版本有变化 | 类名：ViewportRect；  API声明：x?: Length;  差异内容：18 | 类名：ViewportRect；  API声明：x?: Length;  差异内容：7 | component/shape.d.ts |
| 起始版本有变化 | 类名：ViewportRect；  API声明：y?: Length;  差异内容：18 | 类名：ViewportRect；  API声明：y?: Length;  差异内容：7 | component/shape.d.ts |
| 起始版本有变化 | 类名：ViewportRect；  API声明：width?: Length;  差异内容：18 | 类名：ViewportRect；  API声明：width?: Length;  差异内容：7 | component/shape.d.ts |
| 起始版本有变化 | 类名：ViewportRect；  API声明：height?: Length;  差异内容：18 | 类名：ViewportRect；  API声明：height?: Length;  差异内容：7 | component/shape.d.ts |
| 新增kit | 类名：global；  API声明：api\arkui\RenderNode.d.ts  差异内容：NA | 类名：global；  API声明：api\arkui\RenderNode.d.ts  差异内容：ArkUI | api/arkui/RenderNode.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：LayoutManager；  API声明：getCharacterPositionAtCoordinate(x: number, y: number): PositionWithAffinity | undefined;  差异内容：getCharacterPositionAtCoordinate(x: number, y: number): PositionWithAffinity | undefined; | 类名：LayoutManager；  API声明：getCharacterPositionAtCoordinate(x: number, y: number, encoding?: TextEncoding): PositionWithAffinity | undefined;  差异内容：getCharacterPositionAtCoordinate(x: number, y: number, encoding?: TextEncoding): PositionWithAffinity | undefined; | component/text\_common.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：LayoutManager；  API声明：getGlyphRangeForCharacterRange(charRange: TextRange): Array<TextRange> | undefined;  差异内容：getGlyphRangeForCharacterRange(charRange: TextRange): Array<TextRange> | undefined; | 类名：LayoutManager；  API声明：getGlyphRangeForCharacterRange(charRange: TextRange, encoding?: TextEncoding): Array<TextRange> | undefined;  差异内容：getGlyphRangeForCharacterRange(charRange: TextRange, encoding?: TextEncoding): Array<TextRange> | undefined; | component/text\_common.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：LayoutManager；  API声明：getCharacterRangeForGlyphRange(glyphRange: TextRange): Array<TextRange> | undefined;  差异内容：getCharacterRangeForGlyphRange(glyphRange: TextRange): Array<TextRange> | undefined; | 类名：LayoutManager；  API声明：getCharacterRangeForGlyphRange(glyphRange: TextRange, encoding?: TextEncoding): Array<TextRange> | undefined;  差异内容：getCharacterRangeForGlyphRange(glyphRange: TextRange, encoding?: TextEncoding): Array<TextRange> | undefined; | component/text\_common.d.ts |
