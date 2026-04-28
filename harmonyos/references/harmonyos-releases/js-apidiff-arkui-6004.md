---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-6004
title: ArkUI
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta5引入的API > ArkUI
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:08+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:22691b4e377d3646fbe9de57ba7f7cab7280abe4dfe0ec8f8d2ec0398ac8a159
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API卡片权限变更 | 类名：global；  API声明：declare namespace curves  差异内容：NA | 类名：global；  API声明：declare namespace curves  差异内容：form | api/@ohos.curves.d.ts |
| API卡片权限变更 | 类名：curves；  API声明：enum Curve  差异内容：NA | 类名：curves；  API声明：export enum Curve  差异内容：form | api/@ohos.curves.d.ts |
| API卡片权限变更 | 类名：Curve；  API声明：Linear  差异内容：NA | 类名：Curve；  API声明：Linear  差异内容：form | api/@ohos.curves.d.ts |
| API卡片权限变更 | 类名：Curve；  API声明：Ease  差异内容：NA | 类名：Curve；  API声明：Ease  差异内容：form | api/@ohos.curves.d.ts |
| API卡片权限变更 | 类名：Curve；  API声明：EaseIn  差异内容：NA | 类名：Curve；  API声明：EaseIn  差异内容：form | api/@ohos.curves.d.ts |
| API卡片权限变更 | 类名：Curve；  API声明：EaseOut  差异内容：NA | 类名：Curve；  API声明：EaseOut  差异内容：form | api/@ohos.curves.d.ts |
| API卡片权限变更 | 类名：Curve；  API声明：EaseInOut  差异内容：NA | 类名：Curve；  API声明：EaseInOut  差异内容：form | api/@ohos.curves.d.ts |
| API卡片权限变更 | 类名：Curve；  API声明：FastOutSlowIn  差异内容：NA | 类名：Curve；  API声明：FastOutSlowIn  差异内容：form | api/@ohos.curves.d.ts |
| API卡片权限变更 | 类名：Curve；  API声明：LinearOutSlowIn  差异内容：NA | 类名：Curve；  API声明：LinearOutSlowIn  差异内容：form | api/@ohos.curves.d.ts |
| API卡片权限变更 | 类名：Curve；  API声明：FastOutLinearIn  差异内容：NA | 类名：Curve；  API声明：FastOutLinearIn  差异内容：form | api/@ohos.curves.d.ts |
| API卡片权限变更 | 类名：Curve；  API声明：ExtremeDeceleration  差异内容：NA | 类名：Curve；  API声明：ExtremeDeceleration  差异内容：form | api/@ohos.curves.d.ts |
| API卡片权限变更 | 类名：Curve；  API声明：Sharp  差异内容：NA | 类名：Curve；  API声明：Sharp  差异内容：form | api/@ohos.curves.d.ts |
| API卡片权限变更 | 类名：Curve；  API声明：Rhythm  差异内容：NA | 类名：Curve；  API声明：Rhythm  差异内容：form | api/@ohos.curves.d.ts |
| API卡片权限变更 | 类名：Curve；  API声明：Smooth  差异内容：NA | 类名：Curve；  API声明：Smooth  差异内容：form | api/@ohos.curves.d.ts |
| API卡片权限变更 | 类名：Curve；  API声明：Friction  差异内容：NA | 类名：Curve；  API声明：Friction  差异内容：form | api/@ohos.curves.d.ts |
| API卡片权限变更 | 类名：curves；  API声明：interface ICurve  差异内容：NA | 类名：curves；  API声明：export interface ICurve  差异内容：form | api/@ohos.curves.d.ts |
| API卡片权限变更 | 类名：ICurve；  API声明：interpolate(fraction: number): number;  差异内容：NA | 类名：ICurve；  API声明：interpolate(fraction: number): number;  差异内容：form | api/@ohos.curves.d.ts |
| 删除错误码 | 类名：uiAppearance；  API声明：function getDarkMode(): DarkMode;  差异内容：401 | 类名：uiAppearance；  API声明：function getDarkMode(): DarkMode;  差异内容：NA | api/@ohos.uiAppearance.d.ts |
| 删除错误码 | 类名：uiAppearance；  API声明：function getFontScale(): number;  差异内容：401 | 类名：uiAppearance；  API声明：function getFontScale(): number;  差异内容：NA | api/@ohos.uiAppearance.d.ts |
| 删除错误码 | 类名：uiAppearance；  API声明：function getFontWeightScale(): number;  差异内容：401 | 类名：uiAppearance；  API声明：function getFontWeightScale(): number;  差异内容：NA | api/@ohos.uiAppearance.d.ts |
| 删除错误码 | 类名：LengthMetrics；  API声明：static resource(value: Resource): LengthMetrics;  差异内容：180001,180002 | 类名：LengthMetrics；  API声明：static resource(value: Resource): LengthMetrics;  差异内容：NA | api/arkui/Graphics.d.ts |
| 函数变更 | 类名：SymbolGlyphAttribute；  API声明：shaderStyle(shaders: Array<ShaderStyle>): SymbolGlyphAttribute;  差异内容：shaders: Array<ShaderStyle> | 类名：SymbolGlyphAttribute；  API声明：shaderStyle(shader: Array<ShaderStyle | undefined> | ShaderStyle): SymbolGlyphAttribute;  差异内容：shader: Array<ShaderStyle | undefined> | ShaderStyle | component/symbolglyph.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum ReplaceEffectType  差异内容：declare enum ReplaceEffectType | component/symbolglyph.d.ts |
| 新增API | NA | 类名：ReplaceEffectType；  API声明：SEQUENTIAL = 0  差异内容：SEQUENTIAL = 0 | component/symbolglyph.d.ts |
| 新增API | NA | 类名：ReplaceEffectType；  API声明：CROSS\_FADE = 1  差异内容：CROSS\_FADE = 1 | component/symbolglyph.d.ts |
| 新增API | NA | 类名：ReplaceEffectType；  API声明：SLASH\_OVERLAY = 2  差异内容：SLASH\_OVERLAY = 2 | component/symbolglyph.d.ts |
| 新增API | NA | 类名：StickyStyle；  API声明：BOTH = 3  差异内容：BOTH = 3 | component/list.d.ts |
| 删除API | 类名：global；  API声明：declare class DisableSymbolEffect  差异内容：declare class DisableSymbolEffect | NA | component/symbolglyph.d.ts |
| 删除API | 类名：DisableSymbolEffect；  API声明：scope?: EffectScope;  差异内容：scope?: EffectScope; | NA | component/symbolglyph.d.ts |
| 删除API | 类名：global；  API声明：declare class QuickReplaceSymbolEffect  差异内容：declare class QuickReplaceSymbolEffect | NA | component/symbolglyph.d.ts |
| 删除API | 类名：QuickReplaceSymbolEffect；  API声明：scope?: EffectScope;  差异内容：scope?: EffectScope; | NA | component/symbolglyph.d.ts |
| 删除API | 类名：global；  API声明：declare enum TextChangeReason  差异内容：declare enum TextChangeReason | NA | component/text\_common.d.ts |
| 删除API | 类名：TextChangeReason；  API声明：UNKNOWN = 0  差异内容：UNKNOWN = 0 | NA | component/text\_common.d.ts |
| 删除API | 类名：TextChangeReason；  API声明：INPUT = 1  差异内容：INPUT = 1 | NA | component/text\_common.d.ts |
| 删除API | 类名：TextChangeReason；  API声明：PASTE = 2  差异内容：PASTE = 2 | NA | component/text\_common.d.ts |
| 删除API | 类名：TextChangeReason；  API声明：CUT = 3  差异内容：CUT = 3 | NA | component/text\_common.d.ts |
| 删除API | 类名：TextChangeReason；  API声明：DRAG = 4  差异内容：DRAG = 4 | NA | component/text\_common.d.ts |
| 删除API | 类名：TextChangeReason；  API声明：AUTO\_FILL = 5  差异内容：AUTO\_FILL = 5 | NA | component/text\_common.d.ts |
| 删除API | 类名：TextChangeReason；  API声明：AI\_WRITE = 6  差异内容：AI\_WRITE = 6 | NA | component/text\_common.d.ts |
| 删除API | 类名：TextChangeReason；  API声明：REDO = 7  差异内容：REDO = 7 | NA | component/text\_common.d.ts |
| 删除API | 类名：TextChangeReason；  API声明：UNDO = 8  差异内容：UNDO = 8 | NA | component/text\_common.d.ts |
| 删除API | 类名：TextChangeReason；  API声明：CONTROLLER = 9  差异内容：CONTROLLER = 9 | NA | component/text\_common.d.ts |
| 删除API | 类名：TextChangeReason；  API声明：ACCESSIBILITY = 10  差异内容：ACCESSIBILITY = 10 | NA | component/text\_common.d.ts |
| 删除API | 类名：TextChangeReason；  API声明：COLLABORATION = 11  差异内容：COLLABORATION = 11 | NA | component/text\_common.d.ts |
| 删除API | 类名：TextChangeReason；  API声明：STYLUS = 12  差异内容：STYLUS = 12 | NA | component/text\_common.d.ts |
| 函数变更 | 类名：TextDataDetectorConfig；  API声明：onDetectResultUpdate?: (result: string) => void;  差异内容：(result: string) => void | 类名：TextDataDetectorConfig；  API声明：onDetectResultUpdate?: Callback<string>;  差异内容：Callback<string> | component/text\_common.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：ReplaceSymbolEffect；  API声明：replaceType?: ReplaceEffectType;  差异内容：replaceType?: ReplaceEffectType; | component/symbolglyph.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Padding；  API声明：top?: Length;  差异内容：top?: Length; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Padding；  API声明：right?: Length;  差异内容：right?: Length; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Padding；  API声明：bottom?: Length;  差异内容：bottom?: Length; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Padding；  API声明：left?: Length;  差异内容：left?: Length; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EdgeWidths；  API声明：top?: Length;  差异内容：top?: Length; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EdgeWidths；  API声明：right?: Length;  差异内容：right?: Length; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EdgeWidths；  API声明：bottom?: Length;  差异内容：bottom?: Length; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EdgeWidths；  API声明：left?: Length;  差异内容：left?: Length; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EdgeOutlineWidths；  API声明：top?: Dimension;  差异内容：top?: Dimension; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EdgeOutlineWidths；  API声明：right?: Dimension;  差异内容：right?: Dimension; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EdgeOutlineWidths；  API声明：bottom?: Dimension;  差异内容：bottom?: Dimension; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EdgeOutlineWidths；  API声明：left?: Dimension;  差异内容：left?: Dimension; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：BorderRadiuses；  API声明：topLeft?: Length;  差异内容：topLeft?: Length; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：BorderRadiuses；  API声明：topRight?: Length;  差异内容：topRight?: Length; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：BorderRadiuses；  API声明：bottomLeft?: Length;  差异内容：bottomLeft?: Length; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：BorderRadiuses；  API声明：bottomRight?: Length;  差异内容：bottomRight?: Length; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：OutlineRadiuses；  API声明：topLeft?: Dimension;  差异内容：topLeft?: Dimension; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：OutlineRadiuses；  API声明：topRight?: Dimension;  差异内容：topRight?: Dimension; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：OutlineRadiuses；  API声明：bottomLeft?: Dimension;  差异内容：bottomLeft?: Dimension; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：OutlineRadiuses；  API声明：bottomRight?: Dimension;  差异内容：bottomRight?: Dimension; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EdgeColors；  API声明：top?: ResourceColor;  差异内容：top?: ResourceColor; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EdgeColors；  API声明：right?: ResourceColor;  差异内容：right?: ResourceColor; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EdgeColors；  API声明：bottom?: ResourceColor;  差异内容：bottom?: ResourceColor; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EdgeColors；  API声明：left?: ResourceColor;  差异内容：left?: ResourceColor; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EdgeStyles；  API声明：top?: BorderStyle;  差异内容：top?: BorderStyle; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EdgeStyles；  API声明：right?: BorderStyle;  差异内容：right?: BorderStyle; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EdgeStyles；  API声明：bottom?: BorderStyle;  差异内容：bottom?: BorderStyle; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EdgeStyles；  API声明：left?: BorderStyle;  差异内容：left?: BorderStyle; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EdgeOutlineStyles；  API声明：top?: OutlineStyle;  差异内容：top?: OutlineStyle; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EdgeOutlineStyles；  API声明：right?: OutlineStyle;  差异内容：right?: OutlineStyle; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EdgeOutlineStyles；  API声明：bottom?: OutlineStyle;  差异内容：bottom?: OutlineStyle; | component/units.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EdgeOutlineStyles；  API声明：left?: OutlineStyle;  差异内容：left?: OutlineStyle; | component/units.d.ts |
| 接口新增必选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Offset；  API声明：dx: Length;  差异内容：dx: Length; | component/units.d.ts |
| 接口新增必选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Offset；  API声明：dy: Length;  差异内容：dy: Length; | component/units.d.ts |
| 接口新增必选属性 | 类名：global；  API声明：  差异内容：NA | 类名：LengthConstrain；  API声明：minLength: Length;  差异内容：minLength: Length; | component/units.d.ts |
| 接口新增必选属性 | 类名：global；  API声明：  差异内容：NA | 类名：LengthConstrain；  API声明：maxLength: Length;  差异内容：maxLength: Length; | component/units.d.ts |
| 新增导出符号 | 类名：global；  API声明：export interface ShapeSize  差异内容：NA | 类名：global；  API声明：  差异内容：export interface ShapeSize | api/@ohos.arkui.shape.d.ts |
| 新增导出符号 | 类名：global；  API声明：export interface RectShapeOptions  差异内容：NA | 类名：global；  API声明：  差异内容：export interface RectShapeOptions | api/@ohos.arkui.shape.d.ts |
| 新增导出符号 | 类名：global；  API声明：export interface RoundRectShapeOptions  差异内容：NA | 类名：global；  API声明：  差异内容：export interface RoundRectShapeOptions | api/@ohos.arkui.shape.d.ts |
| 新增导出符号 | 类名：global；  API声明：export interface PathShapeOptions  差异内容：NA | 类名：global；  API声明：  差异内容：export interface PathShapeOptions | api/@ohos.arkui.shape.d.ts |
