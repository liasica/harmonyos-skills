---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics2d-b031
title: ArkGraphics 2D
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > ArkGraphics 2D
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:35+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:7c0570a00ff944aba22ebd61d15378fdebe7916387789feb851c28bb8684f155
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：Canvas；  API声明：drawRect(left: number, top: number, right: number, bottom: number): void;  差异内容：drawRect(left: number, top: number, right: number, bottom: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawColor(alpha: number, red: number, green: number, blue: number, blendMode?: BlendMode): void;  差异内容：drawColor(alpha: number, red: number, green: number, blue: number, blendMode?: BlendMode): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：setColor(alpha: number, red: number, green: number, blue: number): void;  差异内容：setColor(alpha: number, red: number, green: number, blue: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Brush；  API声明：setColor(alpha: number, red: number, green: number, blue: number): void;  差异内容：setColor(alpha: number, red: number, green: number, blue: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawRegion(region: Region): void;  差异内容：drawRegion(region: Region): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：saveLayer(rect?: common2D.Rect | null, brush?: Brush | null): number;  差异内容：saveLayer(rect?: common2D.Rect | null, brush?: Brush | null): number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Typeface；  API声明：static makeFromFile(filePath: string): Typeface;  差异内容：static makeFromFile(filePath: string): Typeface; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：setScaleX(scaleX: number): void;  差异内容：setScaleX(scaleX: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：setSkewX(skewX: number): void;  差异内容：setSkewX(skewX: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum FontMetricsFlags  差异内容： enum FontMetricsFlags | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetricsFlags；  API声明：UNDERLINE\_THICKNESS\_VALID = 1 << 0  差异内容：UNDERLINE\_THICKNESS\_VALID = 1 << 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetricsFlags；  API声明：UNDERLINE\_POSITION\_VALID = 1 << 1  差异内容：UNDERLINE\_POSITION\_VALID = 1 << 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetricsFlags；  API声明：STRIKETHROUGH\_THICKNESS\_VALID = 1 << 2  差异内容：STRIKETHROUGH\_THICKNESS\_VALID = 1 << 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetricsFlags；  API声明：STRIKETHROUGH\_POSITION\_VALID = 1 << 3  差异内容：STRIKETHROUGH\_POSITION\_VALID = 1 << 3 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetricsFlags；  API声明：BOUNDS\_INVALID = 1 << 4  差异内容：BOUNDS\_INVALID = 1 << 4 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetrics；  API声明：flags?: FontMetricsFlags;  差异内容：flags?: FontMetricsFlags; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetrics；  API声明：avgCharWidth?: number;  差异内容：avgCharWidth?: number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetrics；  API声明：maxCharWidth?: number;  差异内容：maxCharWidth?: number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetrics；  API声明：xMin?: number;  差异内容：xMin?: number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetrics；  API声明：xMax?: number;  差异内容：xMax?: number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetrics；  API声明：xHeight?: number;  差异内容：xHeight?: number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetrics；  API声明：capHeight?: number;  差异内容：capHeight?: number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetrics；  API声明：underlineThickness?: number;  差异内容：underlineThickness?: number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetrics；  API声明：underlinePosition?: number;  差异内容：underlinePosition?: number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetrics；  API声明：strikethroughThickness?: number;  差异内容：strikethroughThickness?: number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetrics；  API声明：strikethroughPosition?: number;  差异内容：strikethroughPosition?: number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathEffect；  API声明：static createCornerPathEffect(radius: number): PathEffect;  差异内容：static createCornerPathEffect(radius: number): PathEffect; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： class Region  差异内容： class Region | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Region；  API声明：isPointContained(x: number, y: number): boolean;  差异内容：isPointContained(x: number, y: number): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Region；  API声明：isRegionContained(other: Region): boolean;  差异内容：isRegionContained(other: Region): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Region；  API声明：op(region: Region, regionOp: RegionOp): boolean;  差异内容：op(region: Region, regionOp: RegionOp): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Region；  API声明：quickReject(left: number, top: number, right: number, bottom: number): boolean;  差异内容：quickReject(left: number, top: number, right: number, bottom: number): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Region；  API声明：setPath(path: Path, clip: Region): boolean;  差异内容：setPath(path: Path, clip: Region): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Region；  API声明：setRect(left: number, top: number, right: number, bottom: number): boolean;  差异内容：setRect(left: number, top: number, right: number, bottom: number): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum RegionOp  差异内容： enum RegionOp | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：RegionOp；  API声明：DIFFERENCE = 0  差异内容：DIFFERENCE = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：RegionOp；  API声明：INTERSECT = 1  差异内容：INTERSECT = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：RegionOp；  API声明：UNION = 2  差异内容：UNION = 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：RegionOp；  API声明：XOR = 3  差异内容：XOR = 3 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：RegionOp；  API声明：REVERSE\_DIFFERENCE = 4  差异内容：REVERSE\_DIFFERENCE = 4 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：RegionOp；  API声明：REPLACE = 5  差异内容：REPLACE = 5 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：text；  API声明： enum FontWidth  差异内容： enum FontWidth | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontWidth；  API声明：ULTRA\_CONDENSED = 1  差异内容：ULTRA\_CONDENSED = 1 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontWidth；  API声明：EXTRA\_CONDENSED = 2  差异内容：EXTRA\_CONDENSED = 2 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontWidth；  API声明：CONDENSED = 3  差异内容：CONDENSED = 3 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontWidth；  API声明：SEMI\_CONDENSED = 4  差异内容：SEMI\_CONDENSED = 4 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontWidth；  API声明：NORMAL = 5  差异内容：NORMAL = 5 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontWidth；  API声明：SEMI\_EXPANDED = 6  差异内容：SEMI\_EXPANDED = 6 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontWidth；  API声明：EXPANDED = 7  差异内容：EXPANDED = 7 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontWidth；  API声明：EXTRA\_EXPANDED = 8  差异内容：EXTRA\_EXPANDED = 8 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontWidth；  API声明：ULTRA\_EXPANDED = 9  差异内容：ULTRA\_EXPANDED = 9 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： enum TextHeightBehavior  差异内容： enum TextHeightBehavior | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextHeightBehavior；  API声明：ALL = 0x0  差异内容：ALL = 0x0 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextHeightBehavior；  API声明：DISABLE\_FIRST\_ASCENT = 0x1  差异内容：DISABLE\_FIRST\_ASCENT = 0x1 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextHeightBehavior；  API声明：DISABLE\_LAST\_ASCENT = 0x2  差异内容：DISABLE\_LAST\_ASCENT = 0x2 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextHeightBehavior；  API声明：DISABLE\_ALL = 0x1 | 0x2  差异内容：DISABLE\_ALL = 0x1 | 0x2 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： interface TextShadow  差异内容： interface TextShadow | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextShadow；  API声明：color?: common2D.Color;  差异内容：color?: common2D.Color; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextShadow；  API声明：point?: common2D.Point;  差异内容：point?: common2D.Point; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextShadow；  API声明：blurRadius?: number;  差异内容：blurRadius?: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： interface RectStyle  差异内容： interface RectStyle | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：RectStyle；  API声明：color: common2D.Color;  差异内容：color: common2D.Color; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：RectStyle；  API声明：leftTopRadius: number;  差异内容：leftTopRadius: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：RectStyle；  API声明：rightTopRadius: number;  差异内容：rightTopRadius: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：RectStyle；  API声明：rightBottomRadius: number;  差异内容：rightBottomRadius: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：RectStyle；  API声明：leftBottomRadius: number;  差异内容：leftBottomRadius: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： interface FontFeature  差异内容： interface FontFeature | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontFeature；  API声明：name: string;  差异内容：name: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontFeature；  API声明：value: number;  差异内容：value: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： interface FontVariation  差异内容： interface FontVariation | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontVariation；  API声明：axis: string;  差异内容：axis: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontVariation；  API声明：value: number;  差异内容：value: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：baselineShift?: number;  差异内容：baselineShift?: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：fontFeatures?: Array<FontFeature>;  差异内容：fontFeatures?: Array<FontFeature>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：textShadows?: Array<TextShadow>;  差异内容：textShadows?: Array<TextShadow>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：backgroundRect?: RectStyle;  差异内容：backgroundRect?: RectStyle; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：fontVariations?: Array<FontVariation>;  差异内容：fontVariations?: Array<FontVariation>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： interface StrutStyle  差异内容： interface StrutStyle | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：StrutStyle；  API声明：fontFamilies?: Array<string>;  差异内容：fontFamilies?: Array<string>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：StrutStyle；  API声明：fontStyle?: FontStyle;  差异内容：fontStyle?: FontStyle; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：StrutStyle；  API声明：fontWidth?: FontWidth;  差异内容：fontWidth?: FontWidth; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：StrutStyle；  API声明：fontWeight?: FontWeight;  差异内容：fontWeight?: FontWeight; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：StrutStyle；  API声明：fontSize?: number;  差异内容：fontSize?: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：StrutStyle；  API声明：height?: number;  差异内容：height?: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：StrutStyle；  API声明：leading?: number;  差异内容：leading?: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：StrutStyle；  API声明：forceHeight?: boolean;  差异内容：forceHeight?: boolean; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：StrutStyle；  API声明：enabled?: boolean;  差异内容：enabled?: boolean; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：StrutStyle；  API声明：heightOverride?: boolean;  差异内容：heightOverride?: boolean; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：StrutStyle；  API声明：halfLeading?: boolean;  差异内容：halfLeading?: boolean; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：strutStyle?: StrutStyle;  差异内容：strutStyle?: StrutStyle; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：textHeightBehavior?: TextHeightBehavior;  差异内容：textHeightBehavior?: TextHeightBehavior; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getActualTextRange(lineNumber: number, includeSpaces: boolean): Range;  差异内容：getActualTextRange(lineNumber: number, includeSpaces: boolean): Range; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getLineMetrics(): Array<LineMetrics>;  差异内容：getLineMetrics(): Array<LineMetrics>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getLineMetrics(lineNumber: number): LineMetrics | undefined;  差异内容：getLineMetrics(lineNumber: number): LineMetrics | undefined; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphBuilder；  API声明：addSymbol(symbolId: number): void;  差异内容：addSymbol(symbolId: number): void; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： interface RunMetrics  差异内容： interface RunMetrics | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：RunMetrics；  API声明：textStyle: TextStyle;  差异内容：textStyle: TextStyle; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：RunMetrics；  API声明：fontMetrics: drawing.FontMetrics;  差异内容：fontMetrics: drawing.FontMetrics; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： interface LineMetrics  差异内容： interface LineMetrics | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：LineMetrics；  API声明：startIndex: number;  差异内容：startIndex: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：LineMetrics；  API声明：endIndex: number;  差异内容：endIndex: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：LineMetrics；  API声明：ascent: number;  差异内容：ascent: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：LineMetrics；  API声明：descent: number;  差异内容：descent: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：LineMetrics；  API声明：height: number;  差异内容：height: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：LineMetrics；  API声明：width: number;  差异内容：width: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：LineMetrics；  API声明：left: number;  差异内容：left: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：LineMetrics；  API声明：baseline: number;  差异内容：baseline: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：LineMetrics；  API声明：lineNumber: number;  差异内容：lineNumber: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：LineMetrics；  API声明：topHeight: number;  差异内容：topHeight: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：LineMetrics；  API声明：runMetrics: Map<number, RunMetrics>;  差异内容：runMetrics: Map<number, RunMetrics>; | api/@ohos.graphics.text.d.ts |
