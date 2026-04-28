---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics2d-6021
title: ArkGraphics 2D
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > ArkGraphics 2D
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:43+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:2120f97532ab70ab84c8d0f94dfda71f32a5269c5e5eee7d73cfd6459c72cb67
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API卡片权限变更 | 类名：global；  API声明：declare namespace text  差异内容：NA | 类名：global；  API声明：declare namespace text  差异内容：form | api/@ohos.graphics.text.d.ts |
| API卡片权限变更 | 类名：text；  API声明：class FontCollection  差异内容：NA | 类名：text；  API声明：class FontCollection  差异内容：form | api/@ohos.graphics.text.d.ts |
| API卡片权限变更 | 类名：FontCollection；  API声明：loadFontSync(name: string, path: string | Resource): void;  差异内容：NA | 类名：FontCollection；  API声明：loadFontSync(name: string, path: string | Resource): void;  差异内容：form | api/@ohos.graphics.text.d.ts |
| API卡片权限变更 | 类名：FontCollection；  API声明：loadFont(name: string, path: string | Resource): Promise<void>;  差异内容：NA | 类名：FontCollection；  API声明：loadFont(name: string, path: string | Resource): Promise<void>;  差异内容：form | api/@ohos.graphics.text.d.ts |
| API卡片权限变更 | 类名：FontCollection；  API声明：unloadFontSync(name: string): void;  差异内容：NA | 类名：FontCollection；  API声明：unloadFontSync(name: string): void;  差异内容：form | api/@ohos.graphics.text.d.ts |
| API卡片权限变更 | 类名：FontCollection；  API声明：unloadFont(name: string): Promise<void>;  差异内容：NA | 类名：FontCollection；  API声明：unloadFont(name: string): Promise<void>;  差异内容：form | api/@ohos.graphics.text.d.ts |
| API卡片权限变更 | 类名：FontCollection；  API声明：clearCaches(): void;  差异内容：NA | 类名：FontCollection；  API声明：clearCaches(): void;  差异内容：form | api/@ohos.graphics.text.d.ts |
| API卡片权限变更 | 类名：global；  API声明：declare namespace uiEffect  差异内容：NA | 类名：global；  API声明：declare namespace uiEffect  差异内容：form | api/@ohos.graphics.uiEffect.d.ts |
| API卡片权限变更 | 类名：uiEffect；  API声明：interface VisualEffect  差异内容：NA | 类名：uiEffect；  API声明：interface VisualEffect  差异内容：form | api/@ohos.graphics.uiEffect.d.ts |
| 新增API | NA | 类名：FontCollection；  API声明：static getLocalInstance(): FontCollection;  差异内容：static getLocalInstance(): FontCollection; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明：function getFontDescriptorsFromPath(path: string | Resource): Promise<Array<FontDescriptor>>;  差异内容：function getFontDescriptorsFromPath(path: string | Resource): Promise<Array<FontDescriptor>>; | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：declare namespace common2D  差异内容：NA | 类名：global；  API声明：declare namespace common2D  差异内容：atomicservice | api/@ohos.graphics.common2D.d.ts |
| API从不支持元服务到支持元服务 | 类名：common2D；  API声明：interface Color  差异内容：NA | 类名：common2D；  API声明：interface Color  差异内容：atomicservice | api/@ohos.graphics.common2D.d.ts |
| API从不支持元服务到支持元服务 | 类名：Color；  API声明：alpha: number;  差异内容：NA | 类名：Color；  API声明：alpha: number;  差异内容：atomicservice | api/@ohos.graphics.common2D.d.ts |
| API从不支持元服务到支持元服务 | 类名：Color；  API声明：red: number;  差异内容：NA | 类名：Color；  API声明：red: number;  差异内容：atomicservice | api/@ohos.graphics.common2D.d.ts |
| API从不支持元服务到支持元服务 | 类名：Color；  API声明：green: number;  差异内容：NA | 类名：Color；  API声明：green: number;  差异内容：atomicservice | api/@ohos.graphics.common2D.d.ts |
| API从不支持元服务到支持元服务 | 类名：Color；  API声明：blue: number;  差异内容：NA | 类名：Color；  API声明：blue: number;  差异内容：atomicservice | api/@ohos.graphics.common2D.d.ts |
| API从不支持元服务到支持元服务 | 类名：common2D；  API声明：interface Rect  差异内容：NA | 类名：common2D；  API声明：interface Rect  差异内容：atomicservice | api/@ohos.graphics.common2D.d.ts |
| API从不支持元服务到支持元服务 | 类名：Rect；  API声明：left: number;  差异内容：NA | 类名：Rect；  API声明：left: number;  差异内容：atomicservice | api/@ohos.graphics.common2D.d.ts |
| API从不支持元服务到支持元服务 | 类名：Rect；  API声明：top: number;  差异内容：NA | 类名：Rect；  API声明：top: number;  差异内容：atomicservice | api/@ohos.graphics.common2D.d.ts |
| API从不支持元服务到支持元服务 | 类名：Rect；  API声明：right: number;  差异内容：NA | 类名：Rect；  API声明：right: number;  差异内容：atomicservice | api/@ohos.graphics.common2D.d.ts |
| API从不支持元服务到支持元服务 | 类名：Rect；  API声明：bottom: number;  差异内容：NA | 类名：Rect；  API声明：bottom: number;  差异内容：atomicservice | api/@ohos.graphics.common2D.d.ts |
| API从不支持元服务到支持元服务 | 类名：common2D；  API声明：interface Point  差异内容：NA | 类名：common2D；  API声明：interface Point  差异内容：atomicservice | api/@ohos.graphics.common2D.d.ts |
| API从不支持元服务到支持元服务 | 类名：Point；  API声明：x: number;  差异内容：NA | 类名：Point；  API声明：x: number;  差异内容：atomicservice | api/@ohos.graphics.common2D.d.ts |
| API从不支持元服务到支持元服务 | 类名：Point；  API声明：y: number;  差异内容：NA | 类名：Point；  API声明：y: number;  差异内容：atomicservice | api/@ohos.graphics.common2D.d.ts |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：declare namespace drawing  差异内容：NA | 类名：global；  API声明：declare namespace drawing  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：drawing；  API声明：class Path  差异内容：NA | 类名：drawing；  API声明：class Path  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Path；  API声明：set(src: Path): void;  差异内容：NA | 类名：Path；  API声明：set(src: Path): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Path；  API声明：moveTo(x: number, y: number): void;  差异内容：NA | 类名：Path；  API声明：moveTo(x: number, y: number): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Path；  API声明：lineTo(x: number, y: number): void;  差异内容：NA | 类名：Path；  API声明：lineTo(x: number, y: number): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Path；  API声明：arcTo(x1: number, y1: number, x2: number, y2: number, startDeg: number, sweepDeg: number): void;  差异内容：NA | 类名：Path；  API声明：arcTo(x1: number, y1: number, x2: number, y2: number, startDeg: number, sweepDeg: number): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Path；  API声明：quadTo(ctrlX: number, ctrlY: number, endX: number, endY: number): void;  差异内容：NA | 类名：Path；  API声明：quadTo(ctrlX: number, ctrlY: number, endX: number, endY: number): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Path；  API声明：conicTo(ctrlX: number, ctrlY: number, endX: number, endY: number, weight: number): void;  差异内容：NA | 类名：Path；  API声明：conicTo(ctrlX: number, ctrlY: number, endX: number, endY: number, weight: number): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Path；  API声明：cubicTo(ctrlX1: number, ctrlY1: number, ctrlX2: number, ctrlY2: number, endX: number, endY: number): void;  差异内容：NA | 类名：Path；  API声明：cubicTo(ctrlX1: number, ctrlY1: number, ctrlX2: number, ctrlY2: number, endX: number, endY: number): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Path；  API声明：rMoveTo(dx: number, dy: number): void;  差异内容：NA | 类名：Path；  API声明：rMoveTo(dx: number, dy: number): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Path；  API声明：rLineTo(dx: number, dy: number): void;  差异内容：NA | 类名：Path；  API声明：rLineTo(dx: number, dy: number): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Path；  API声明：rQuadTo(dx1: number, dy1: number, dx2: number, dy2: number): void;  差异内容：NA | 类名：Path；  API声明：rQuadTo(dx1: number, dy1: number, dx2: number, dy2: number): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Path；  API声明：rConicTo(ctrlX: number, ctrlY: number, endX: number, endY: number, weight: number): void;  差异内容：NA | 类名：Path；  API声明：rConicTo(ctrlX: number, ctrlY: number, endX: number, endY: number, weight: number): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Path；  API声明：rCubicTo(ctrlX1: number, ctrlY1: number, ctrlX2: number, ctrlY2: number, endX: number, endY: number): void;  差异内容：NA | 类名：Path；  API声明：rCubicTo(ctrlX1: number, ctrlY1: number, ctrlX2: number, ctrlY2: number, endX: number, endY: number): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：drawing；  API声明：interface FontFeature  差异内容：NA | 类名：drawing；  API声明：interface FontFeature  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontFeature；  API声明：name: string;  差异内容：NA | 类名：FontFeature；  API声明：name: string;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontFeature；  API声明：value: number;  差异内容：NA | 类名：FontFeature；  API声明：value: number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：drawing；  API声明：class Canvas  差异内容：NA | 类名：drawing；  API声明：class Canvas  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：drawing；  API声明：enum TextEncoding  差异内容：NA | 类名：drawing；  API声明：enum TextEncoding  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextEncoding；  API声明：TEXT\_ENCODING\_UTF8 = 0  差异内容：NA | 类名：TextEncoding；  API声明：TEXT\_ENCODING\_UTF8 = 0  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextEncoding；  API声明：TEXT\_ENCODING\_UTF16 = 1  差异内容：NA | 类名：TextEncoding；  API声明：TEXT\_ENCODING\_UTF16 = 1  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextEncoding；  API声明：TEXT\_ENCODING\_UTF32 = 2  差异内容：NA | 类名：TextEncoding；  API声明：TEXT\_ENCODING\_UTF32 = 2  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextEncoding；  API声明：TEXT\_ENCODING\_GLYPH\_ID = 3  差异内容：NA | 类名：TextEncoding；  API声明：TEXT\_ENCODING\_GLYPH\_ID = 3  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：drawing；  API声明：class TypefaceArguments  差异内容：NA | 类名：drawing；  API声明：class TypefaceArguments  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：TypefaceArguments；  API声明：addVariation(axis: string, value: number);  差异内容：NA | 类名：TypefaceArguments；  API声明：addVariation(axis: string, value: number);  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：drawing；  API声明：class Typeface  差异内容：NA | 类名：drawing；  API声明：class Typeface  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Typeface；  API声明：static makeFromFile(filePath: string): Typeface;  差异内容：NA | 类名：Typeface；  API声明：static makeFromFile(filePath: string): Typeface;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Typeface；  API声明：static makeFromRawFile(rawfile: Resource): Typeface;  差异内容：NA | 类名：Typeface；  API声明：static makeFromRawFile(rawfile: Resource): Typeface;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Typeface；  API声明：static makeFromFileWithArguments(filePath: string, typefaceArguments: TypefaceArguments): Typeface;  差异内容：NA | 类名：Typeface；  API声明：static makeFromFileWithArguments(filePath: string, typefaceArguments: TypefaceArguments): Typeface;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Typeface；  API声明：static makeFromRawFileWithArguments(rawfile: Resource, typefaceArguments: TypefaceArguments): Typeface;  差异内容：NA | 类名：Typeface；  API声明：static makeFromRawFileWithArguments(rawfile: Resource, typefaceArguments: TypefaceArguments): Typeface;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：drawing；  API声明：enum FontEdging  差异内容：NA | 类名：drawing；  API声明：enum FontEdging  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontEdging；  API声明：ALIAS = 0  差异内容：NA | 类名：FontEdging；  API声明：ALIAS = 0  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontEdging；  API声明：ANTI\_ALIAS = 1  差异内容：NA | 类名：FontEdging；  API声明：ANTI\_ALIAS = 1  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontEdging；  API声明：SUBPIXEL\_ANTI\_ALIAS = 2  差异内容：NA | 类名：FontEdging；  API声明：SUBPIXEL\_ANTI\_ALIAS = 2  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：drawing；  API声明：enum FontHinting  差异内容：NA | 类名：drawing；  API声明：enum FontHinting  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontHinting；  API声明：NONE = 0  差异内容：NA | 类名：FontHinting；  API声明：NONE = 0  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontHinting；  API声明：SLIGHT = 1  差异内容：NA | 类名：FontHinting；  API声明：SLIGHT = 1  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontHinting；  API声明：NORMAL = 2  差异内容：NA | 类名：FontHinting；  API声明：NORMAL = 2  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontHinting；  API声明：FULL = 3  差异内容：NA | 类名：FontHinting；  API声明：FULL = 3  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：drawing；  API声明：class Font  差异内容：NA | 类名：drawing；  API声明：class Font  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：enableSubpixel(isSubpixel: boolean): void;  差异内容：NA | 类名：Font；  API声明：enableSubpixel(isSubpixel: boolean): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：enableEmbolden(isEmbolden: boolean): void;  差异内容：NA | 类名：Font；  API声明：enableEmbolden(isEmbolden: boolean): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：enableLinearMetrics(isLinearMetrics: boolean): void;  差异内容：NA | 类名：Font；  API声明：enableLinearMetrics(isLinearMetrics: boolean): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：setSize(textSize: number): void;  差异内容：NA | 类名：Font；  API声明：setSize(textSize: number): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：getSize(): number;  差异内容：NA | 类名：Font；  API声明：getSize(): number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：setTypeface(typeface: Typeface): void;  差异内容：NA | 类名：Font；  API声明：setTypeface(typeface: Typeface): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：getTypeface(): Typeface;  差异内容：NA | 类名：Font；  API声明：getTypeface(): Typeface;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：getMetrics(): FontMetrics;  差异内容：NA | 类名：Font；  API声明：getMetrics(): FontMetrics;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：measureSingleCharacter(text: string): number;  差异内容：NA | 类名：Font；  API声明：measureSingleCharacter(text: string): number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：measureSingleCharacterWithFeatures(text: string, features: Array<FontFeature>): number;  差异内容：NA | 类名：Font；  API声明：measureSingleCharacterWithFeatures(text: string, features: Array<FontFeature>): number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：measureText(text: string, encoding: TextEncoding): number;  差异内容：NA | 类名：Font；  API声明：measureText(text: string, encoding: TextEncoding): number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：setScaleX(scaleX: number): void;  差异内容：NA | 类名：Font；  API声明：setScaleX(scaleX: number): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：setSkewX(skewX: number): void;  差异内容：NA | 类名：Font；  API声明：setSkewX(skewX: number): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：setEdging(edging: FontEdging): void;  差异内容：NA | 类名：Font；  API声明：setEdging(edging: FontEdging): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：setHinting(hinting: FontHinting): void;  差异内容：NA | 类名：Font；  API声明：setHinting(hinting: FontHinting): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：countText(text: string): number;  差异内容：NA | 类名：Font；  API声明：countText(text: string): number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：setBaselineSnap(isBaselineSnap: boolean): void;  差异内容：NA | 类名：Font；  API声明：setBaselineSnap(isBaselineSnap: boolean): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：isBaselineSnap(): boolean;  差异内容：NA | 类名：Font；  API声明：isBaselineSnap(): boolean;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：setEmbeddedBitmaps(isEmbeddedBitmaps: boolean): void;  差异内容：NA | 类名：Font；  API声明：setEmbeddedBitmaps(isEmbeddedBitmaps: boolean): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：isEmbeddedBitmaps(): boolean;  差异内容：NA | 类名：Font；  API声明：isEmbeddedBitmaps(): boolean;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：setForceAutoHinting(isForceAutoHinting: boolean): void;  差异内容：NA | 类名：Font；  API声明：setForceAutoHinting(isForceAutoHinting: boolean): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：isForceAutoHinting(): boolean;  差异内容：NA | 类名：Font；  API声明：isForceAutoHinting(): boolean;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：getWidths(glyphs: Array<number>): Array<number>;  差异内容：NA | 类名：Font；  API声明：getWidths(glyphs: Array<number>): Array<number>;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：textToGlyphs(text: string, glyphCount?: number): Array<number>;  差异内容：NA | 类名：Font；  API声明：textToGlyphs(text: string, glyphCount?: number): Array<number>;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：isSubpixel(): boolean;  差异内容：NA | 类名：Font；  API声明：isSubpixel(): boolean;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：isLinearMetrics(): boolean;  差异内容：NA | 类名：Font；  API声明：isLinearMetrics(): boolean;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：getSkewX(): number;  差异内容：NA | 类名：Font；  API声明：getSkewX(): number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：isEmbolden(): boolean;  差异内容：NA | 类名：Font；  API声明：isEmbolden(): boolean;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：getScaleX(): number;  差异内容：NA | 类名：Font；  API声明：getScaleX(): number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：getHinting(): FontHinting;  差异内容：NA | 类名：Font；  API声明：getHinting(): FontHinting;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：getEdging(): FontEdging;  差异内容：NA | 类名：Font；  API声明：getEdging(): FontEdging;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：createPathForGlyph(index: number): Path;  差异内容：NA | 类名：Font；  API声明：createPathForGlyph(index: number): Path;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：getBounds(glyphs: Array<number>): Array<common2D.Rect>;  差异内容：NA | 类名：Font；  API声明：getBounds(glyphs: Array<number>): Array<common2D.Rect>;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：getTextPath(text: string, byteLength: number, x: number, y: number): Path;  差异内容：NA | 类名：Font；  API声明：getTextPath(text: string, byteLength: number, x: number, y: number): Path;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：setThemeFontFollowed(followed: boolean): void;  差异内容：NA | 类名：Font；  API声明：setThemeFontFollowed(followed: boolean): void;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：Font；  API声明：isThemeFontFollowed(): boolean;  差异内容：NA | 类名：Font；  API声明：isThemeFontFollowed(): boolean;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：drawing；  API声明：enum FontMetricsFlags  差异内容：NA | 类名：drawing；  API声明：enum FontMetricsFlags  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetricsFlags；  API声明：UNDERLINE\_THICKNESS\_VALID = 1 << 0  差异内容：NA | 类名：FontMetricsFlags；  API声明：UNDERLINE\_THICKNESS\_VALID = 1 << 0  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetricsFlags；  API声明：UNDERLINE\_POSITION\_VALID = 1 << 1  差异内容：NA | 类名：FontMetricsFlags；  API声明：UNDERLINE\_POSITION\_VALID = 1 << 1  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetricsFlags；  API声明：STRIKETHROUGH\_THICKNESS\_VALID = 1 << 2  差异内容：NA | 类名：FontMetricsFlags；  API声明：STRIKETHROUGH\_THICKNESS\_VALID = 1 << 2  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetricsFlags；  API声明：STRIKETHROUGH\_POSITION\_VALID = 1 << 3  差异内容：NA | 类名：FontMetricsFlags；  API声明：STRIKETHROUGH\_POSITION\_VALID = 1 << 3  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetricsFlags；  API声明：BOUNDS\_INVALID = 1 << 4  差异内容：NA | 类名：FontMetricsFlags；  API声明：BOUNDS\_INVALID = 1 << 4  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：drawing；  API声明：interface FontMetrics  差异内容：NA | 类名：drawing；  API声明：interface FontMetrics  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetrics；  API声明：flags?: FontMetricsFlags;  差异内容：NA | 类名：FontMetrics；  API声明：flags?: FontMetricsFlags;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetrics；  API声明：top: number;  差异内容：NA | 类名：FontMetrics；  API声明：top: number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetrics；  API声明：ascent: number;  差异内容：NA | 类名：FontMetrics；  API声明：ascent: number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetrics；  API声明：descent: number;  差异内容：NA | 类名：FontMetrics；  API声明：descent: number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetrics；  API声明：bottom: number;  差异内容：NA | 类名：FontMetrics；  API声明：bottom: number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetrics；  API声明：leading: number;  差异内容：NA | 类名：FontMetrics；  API声明：leading: number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetrics；  API声明：avgCharWidth?: number;  差异内容：NA | 类名：FontMetrics；  API声明：avgCharWidth?: number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetrics；  API声明：maxCharWidth?: number;  差异内容：NA | 类名：FontMetrics；  API声明：maxCharWidth?: number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetrics；  API声明：xMin?: number;  差异内容：NA | 类名：FontMetrics；  API声明：xMin?: number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetrics；  API声明：xMax?: number;  差异内容：NA | 类名：FontMetrics；  API声明：xMax?: number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetrics；  API声明：xHeight?: number;  差异内容：NA | 类名：FontMetrics；  API声明：xHeight?: number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetrics；  API声明：capHeight?: number;  差异内容：NA | 类名：FontMetrics；  API声明：capHeight?: number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetrics；  API声明：underlineThickness?: number;  差异内容：NA | 类名：FontMetrics；  API声明：underlineThickness?: number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetrics；  API声明：underlinePosition?: number;  差异内容：NA | 类名：FontMetrics；  API声明：underlinePosition?: number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetrics；  API声明：strikethroughThickness?: number;  差异内容：NA | 类名：FontMetrics；  API声明：strikethroughThickness?: number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontMetrics；  API声明：strikethroughPosition?: number;  差异内容：NA | 类名：FontMetrics；  API声明：strikethroughPosition?: number;  差异内容：atomicservice | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：declare namespace text  差异内容：NA | 类名：global；  API声明：declare namespace text  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum TextAlign  差异内容：NA | 类名：text；  API声明：enum TextAlign  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextAlign；  API声明：LEFT = 0  差异内容：NA | 类名：TextAlign；  API声明：LEFT = 0  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextAlign；  API声明：RIGHT = 1  差异内容：NA | 类名：TextAlign；  API声明：RIGHT = 1  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextAlign；  API声明：CENTER = 2  差异内容：NA | 类名：TextAlign；  API声明：CENTER = 2  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextAlign；  API声明：JUSTIFY = 3  差异内容：NA | 类名：TextAlign；  API声明：JUSTIFY = 3  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextAlign；  API声明：START = 4  差异内容：NA | 类名：TextAlign；  API声明：START = 4  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextAlign；  API声明：END = 5  差异内容：NA | 类名：TextAlign；  API声明：END = 5  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum TextVerticalAlign  差异内容：NA | 类名：text；  API声明：enum TextVerticalAlign  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextVerticalAlign；  API声明：BASELINE = 0  差异内容：NA | 类名：TextVerticalAlign；  API声明：BASELINE = 0  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextVerticalAlign；  API声明：BOTTOM = 1  差异内容：NA | 类名：TextVerticalAlign；  API声明：BOTTOM = 1  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextVerticalAlign；  API声明：CENTER = 2  差异内容：NA | 类名：TextVerticalAlign；  API声明：CENTER = 2  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextVerticalAlign；  API声明：TOP = 3  差异内容：NA | 类名：TextVerticalAlign；  API声明：TOP = 3  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum TextDirection  差异内容：NA | 类名：text；  API声明：enum TextDirection  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextDirection；  API声明：RTL  差异内容：NA | 类名：TextDirection；  API声明：RTL  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextDirection；  API声明：LTR  差异内容：NA | 类名：TextDirection；  API声明：LTR  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum BreakStrategy  差异内容：NA | 类名：text；  API声明：enum BreakStrategy  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：BreakStrategy；  API声明：GREEDY  差异内容：NA | 类名：BreakStrategy；  API声明：GREEDY  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：BreakStrategy；  API声明：HIGH\_QUALITY  差异内容：NA | 类名：BreakStrategy；  API声明：HIGH\_QUALITY  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：BreakStrategy；  API声明：BALANCED  差异内容：NA | 类名：BreakStrategy；  API声明：BALANCED  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum WordBreak  差异内容：NA | 类名：text；  API声明：enum WordBreak  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：WordBreak；  API声明：NORMAL  差异内容：NA | 类名：WordBreak；  API声明：NORMAL  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：WordBreak；  API声明：BREAK\_ALL  差异内容：NA | 类名：WordBreak；  API声明：BREAK\_ALL  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：WordBreak；  API声明：BREAK\_WORD  差异内容：NA | 类名：WordBreak；  API声明：BREAK\_WORD  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：WordBreak；  API声明：BREAK\_HYPHEN  差异内容：NA | 类名：WordBreak；  API声明：BREAK\_HYPHEN  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：interface Decoration  差异内容：NA | 类名：text；  API声明：interface Decoration  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Decoration；  API声明：textDecoration?: TextDecorationType;  差异内容：NA | 类名：Decoration；  API声明：textDecoration?: TextDecorationType;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Decoration；  API声明：color?: common2D.Color;  差异内容：NA | 类名：Decoration；  API声明：color?: common2D.Color;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Decoration；  API声明：decorationStyle?: TextDecorationStyle;  差异内容：NA | 类名：Decoration；  API声明：decorationStyle?: TextDecorationStyle;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Decoration；  API声明：decorationThicknessScale?: number;  差异内容：NA | 类名：Decoration；  API声明：decorationThicknessScale?: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum TextDecorationType  差异内容：NA | 类名：text；  API声明：enum TextDecorationType  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextDecorationType；  API声明：NONE  差异内容：NA | 类名：TextDecorationType；  API声明：NONE  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextDecorationType；  API声明：UNDERLINE  差异内容：NA | 类名：TextDecorationType；  API声明：UNDERLINE  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextDecorationType；  API声明：OVERLINE  差异内容：NA | 类名：TextDecorationType；  API声明：OVERLINE  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextDecorationType；  API声明：LINE\_THROUGH  差异内容：NA | 类名：TextDecorationType；  API声明：LINE\_THROUGH  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum TextDecorationStyle  差异内容：NA | 类名：text；  API声明：enum TextDecorationStyle  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextDecorationStyle；  API声明：SOLID  差异内容：NA | 类名：TextDecorationStyle；  API声明：SOLID  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextDecorationStyle；  API声明：DOUBLE  差异内容：NA | 类名：TextDecorationStyle；  API声明：DOUBLE  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextDecorationStyle；  API声明：DOTTED  差异内容：NA | 类名：TextDecorationStyle；  API声明：DOTTED  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextDecorationStyle；  API声明：DASHED  差异内容：NA | 类名：TextDecorationStyle；  API声明：DASHED  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextDecorationStyle；  API声明：WAVY  差异内容：NA | 类名：TextDecorationStyle；  API声明：WAVY  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum FontWeight  差异内容：NA | 类名：text；  API声明：enum FontWeight  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontWeight；  API声明：W100  差异内容：NA | 类名：FontWeight；  API声明：W100  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontWeight；  API声明：W200  差异内容：NA | 类名：FontWeight；  API声明：W200  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontWeight；  API声明：W300  差异内容：NA | 类名：FontWeight；  API声明：W300  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontWeight；  API声明：W400  差异内容：NA | 类名：FontWeight；  API声明：W400  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontWeight；  API声明：W500  差异内容：NA | 类名：FontWeight；  API声明：W500  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontWeight；  API声明：W600  差异内容：NA | 类名：FontWeight；  API声明：W600  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontWeight；  API声明：W700  差异内容：NA | 类名：FontWeight；  API声明：W700  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontWeight；  API声明：W800  差异内容：NA | 类名：FontWeight；  API声明：W800  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontWeight；  API声明：W900  差异内容：NA | 类名：FontWeight；  API声明：W900  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum FontStyle  差异内容：NA | 类名：text；  API声明：enum FontStyle  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontStyle；  API声明：NORMAL  差异内容：NA | 类名：FontStyle；  API声明：NORMAL  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontStyle；  API声明：ITALIC  差异内容：NA | 类名：FontStyle；  API声明：ITALIC  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontStyle；  API声明：OBLIQUE  差异内容：NA | 类名：FontStyle；  API声明：OBLIQUE  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum FontWidth  差异内容：NA | 类名：text；  API声明：enum FontWidth  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontWidth；  API声明：ULTRA\_CONDENSED = 1  差异内容：NA | 类名：FontWidth；  API声明：ULTRA\_CONDENSED = 1  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontWidth；  API声明：EXTRA\_CONDENSED = 2  差异内容：NA | 类名：FontWidth；  API声明：EXTRA\_CONDENSED = 2  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontWidth；  API声明：CONDENSED = 3  差异内容：NA | 类名：FontWidth；  API声明：CONDENSED = 3  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontWidth；  API声明：SEMI\_CONDENSED = 4  差异内容：NA | 类名：FontWidth；  API声明：SEMI\_CONDENSED = 4  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontWidth；  API声明：NORMAL = 5  差异内容：NA | 类名：FontWidth；  API声明：NORMAL = 5  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontWidth；  API声明：SEMI\_EXPANDED = 6  差异内容：NA | 类名：FontWidth；  API声明：SEMI\_EXPANDED = 6  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontWidth；  API声明：EXPANDED = 7  差异内容：NA | 类名：FontWidth；  API声明：EXPANDED = 7  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontWidth；  API声明：EXTRA\_EXPANDED = 8  差异内容：NA | 类名：FontWidth；  API声明：EXTRA\_EXPANDED = 8  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontWidth；  API声明：ULTRA\_EXPANDED = 9  差异内容：NA | 类名：FontWidth；  API声明：ULTRA\_EXPANDED = 9  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum TextHeightBehavior  差异内容：NA | 类名：text；  API声明：enum TextHeightBehavior  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextHeightBehavior；  API声明：ALL = 0x0  差异内容：NA | 类名：TextHeightBehavior；  API声明：ALL = 0x0  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextHeightBehavior；  API声明：DISABLE\_FIRST\_ASCENT = 0x1  差异内容：NA | 类名：TextHeightBehavior；  API声明：DISABLE\_FIRST\_ASCENT = 0x1  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextHeightBehavior；  API声明：DISABLE\_LAST\_ASCENT = 0x2  差异内容：NA | 类名：TextHeightBehavior；  API声明：DISABLE\_LAST\_ASCENT = 0x2  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextHeightBehavior；  API声明：DISABLE\_ALL = 0x1 | 0x2  差异内容：NA | 类名：TextHeightBehavior；  API声明：DISABLE\_ALL = 0x1 | 0x2  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum TextBaseline  差异内容：NA | 类名：text；  API声明：enum TextBaseline  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextBaseline；  API声明：ALPHABETIC  差异内容：NA | 类名：TextBaseline；  API声明：ALPHABETIC  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextBaseline；  API声明：IDEOGRAPHIC  差异内容：NA | 类名：TextBaseline；  API声明：IDEOGRAPHIC  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum EllipsisMode  差异内容：NA | 类名：text；  API声明：enum EllipsisMode  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：EllipsisMode；  API声明：START  差异内容：NA | 类名：EllipsisMode；  API声明：START  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：EllipsisMode；  API声明：MIDDLE  差异内容：NA | 类名：EllipsisMode；  API声明：MIDDLE  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：EllipsisMode；  API声明：END  差异内容：NA | 类名：EllipsisMode；  API声明：END  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：interface TextShadow  差异内容：NA | 类名：text；  API声明：interface TextShadow  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextShadow；  API声明：color?: common2D.Color;  差异内容：NA | 类名：TextShadow；  API声明：color?: common2D.Color;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextShadow；  API声明：point?: common2D.Point;  差异内容：NA | 类名：TextShadow；  API声明：point?: common2D.Point;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextShadow；  API声明：blurRadius?: number;  差异内容：NA | 类名：TextShadow；  API声明：blurRadius?: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：interface RectStyle  差异内容：NA | 类名：text；  API声明：interface RectStyle  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：RectStyle；  API声明：color: common2D.Color;  差异内容：NA | 类名：RectStyle；  API声明：color: common2D.Color;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：RectStyle；  API声明：leftTopRadius: number;  差异内容：NA | 类名：RectStyle；  API声明：leftTopRadius: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：RectStyle；  API声明：rightTopRadius: number;  差异内容：NA | 类名：RectStyle；  API声明：rightTopRadius: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：RectStyle；  API声明：rightBottomRadius: number;  差异内容：NA | 类名：RectStyle；  API声明：rightBottomRadius: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：RectStyle；  API声明：leftBottomRadius: number;  差异内容：NA | 类名：RectStyle；  API声明：leftBottomRadius: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum LineHeightStyle  差异内容：NA | 类名：text；  API声明：enum LineHeightStyle  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：LineHeightStyle；  API声明：FONT\_SIZE = 0  差异内容：NA | 类名：LineHeightStyle；  API声明：FONT\_SIZE = 0  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：LineHeightStyle；  API声明：FONT\_HEIGHT = 1  差异内容：NA | 类名：LineHeightStyle；  API声明：FONT\_HEIGHT = 1  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：interface FontFeature  差异内容：NA | 类名：text；  API声明：interface FontFeature  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontFeature；  API声明：name: string;  差异内容：NA | 类名：FontFeature；  API声明：name: string;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontFeature；  API声明：value: number;  差异内容：NA | 类名：FontFeature；  API声明：value: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：interface FontVariation  差异内容：NA | 类名：text；  API声明：interface FontVariation  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontVariation；  API声明：axis: string;  差异内容：NA | 类名：FontVariation；  API声明：axis: string;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontVariation；  API声明：value: number;  差异内容：NA | 类名：FontVariation；  API声明：value: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum TextBadgeType  差异内容：NA | 类名：text；  API声明：enum TextBadgeType  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextBadgeType；  API声明：TEXT\_BADGE\_NONE  差异内容：NA | 类名：TextBadgeType；  API声明：TEXT\_BADGE\_NONE  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextBadgeType；  API声明：TEXT\_SUPERSCRIPT  差异内容：NA | 类名：TextBadgeType；  API声明：TEXT\_SUPERSCRIPT  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextBadgeType；  API声明：TEXT\_SUBSCRIPT  差异内容：NA | 类名：TextBadgeType；  API声明：TEXT\_SUBSCRIPT  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：interface TextStyle  差异内容：NA | 类名：text；  API声明：interface TextStyle  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：decoration?: Decoration;  差异内容：NA | 类名：TextStyle；  API声明：decoration?: Decoration;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：color?: common2D.Color;  差异内容：NA | 类名：TextStyle；  API声明：color?: common2D.Color;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：fontWeight?: FontWeight;  差异内容：NA | 类名：TextStyle；  API声明：fontWeight?: FontWeight;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：fontStyle?: FontStyle;  差异内容：NA | 类名：TextStyle；  API声明：fontStyle?: FontStyle;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：baseline?: TextBaseline;  差异内容：NA | 类名：TextStyle；  API声明：baseline?: TextBaseline;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：fontFamilies?: Array<string>;  差异内容：NA | 类名：TextStyle；  API声明：fontFamilies?: Array<string>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：fontSize?: number;  差异内容：NA | 类名：TextStyle；  API声明：fontSize?: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：letterSpacing?: number;  差异内容：NA | 类名：TextStyle；  API声明：letterSpacing?: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：wordSpacing?: number;  差异内容：NA | 类名：TextStyle；  API声明：wordSpacing?: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：lineHeightMaximum?: number;  差异内容：NA | 类名：TextStyle；  API声明：lineHeightMaximum?: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：lineHeightMinimum?: number;  差异内容：NA | 类名：TextStyle；  API声明：lineHeightMinimum?: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：lineHeightStyle?: LineHeightStyle;  差异内容：NA | 类名：TextStyle；  API声明：lineHeightStyle?: LineHeightStyle;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：heightScale?: number;  差异内容：NA | 类名：TextStyle；  API声明：heightScale?: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：halfLeading?: boolean;  差异内容：NA | 类名：TextStyle；  API声明：halfLeading?: boolean;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：heightOnly?: boolean;  差异内容：NA | 类名：TextStyle；  API声明：heightOnly?: boolean;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：ellipsis?: string;  差异内容：NA | 类名：TextStyle；  API声明：ellipsis?: string;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：ellipsisMode?: EllipsisMode;  差异内容：NA | 类名：TextStyle；  API声明：ellipsisMode?: EllipsisMode;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：locale?: string;  差异内容：NA | 类名：TextStyle；  API声明：locale?: string;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：baselineShift?: number;  差异内容：NA | 类名：TextStyle；  API声明：baselineShift?: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：fontFeatures?: Array<FontFeature>;  差异内容：NA | 类名：TextStyle；  API声明：fontFeatures?: Array<FontFeature>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：textShadows?: Array<TextShadow>;  差异内容：NA | 类名：TextStyle；  API声明：textShadows?: Array<TextShadow>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：backgroundRect?: RectStyle;  差异内容：NA | 类名：TextStyle；  API声明：backgroundRect?: RectStyle;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：fontVariations?: Array<FontVariation>;  差异内容：NA | 类名：TextStyle；  API声明：fontVariations?: Array<FontVariation>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：badgeType?: TextBadgeType;  差异内容：NA | 类名：TextStyle；  API声明：badgeType?: TextBadgeType;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextStyle；  API声明：fontWidth?: FontWidth;  差异内容：NA | 类名：TextStyle；  API声明：fontWidth?: FontWidth;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：class FontCollection  差异内容：NA | 类名：text；  API声明：class FontCollection  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontCollection；  API声明：static getGlobalInstance(): FontCollection;  差异内容：NA | 类名：FontCollection；  API声明：static getGlobalInstance(): FontCollection;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontCollection；  API声明：loadFontSync(name: string, path: string | Resource): void;  差异内容：NA | 类名：FontCollection；  API声明：loadFontSync(name: string, path: string | Resource): void;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontCollection；  API声明：loadFont(name: string, path: string | Resource): Promise<void>;  差异内容：NA | 类名：FontCollection；  API声明：loadFont(name: string, path: string | Resource): Promise<void>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontCollection；  API声明：unloadFontSync(name: string): void;  差异内容：NA | 类名：FontCollection；  API声明：unloadFontSync(name: string): void;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontCollection；  API声明：unloadFont(name: string): Promise<void>;  差异内容：NA | 类名：FontCollection；  API声明：unloadFont(name: string): Promise<void>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontCollection；  API声明：clearCaches(): void;  差异内容：NA | 类名：FontCollection；  API声明：clearCaches(): void;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：interface StrutStyle  差异内容：NA | 类名：text；  API声明：interface StrutStyle  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：StrutStyle；  API声明：fontFamilies?: Array<string>;  差异内容：NA | 类名：StrutStyle；  API声明：fontFamilies?: Array<string>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：StrutStyle；  API声明：fontStyle?: FontStyle;  差异内容：NA | 类名：StrutStyle；  API声明：fontStyle?: FontStyle;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：StrutStyle；  API声明：fontWidth?: FontWidth;  差异内容：NA | 类名：StrutStyle；  API声明：fontWidth?: FontWidth;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：StrutStyle；  API声明：fontWeight?: FontWeight;  差异内容：NA | 类名：StrutStyle；  API声明：fontWeight?: FontWeight;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：StrutStyle；  API声明：fontSize?: number;  差异内容：NA | 类名：StrutStyle；  API声明：fontSize?: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：StrutStyle；  API声明：height?: number;  差异内容：NA | 类名：StrutStyle；  API声明：height?: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：StrutStyle；  API声明：leading?: number;  差异内容：NA | 类名：StrutStyle；  API声明：leading?: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：StrutStyle；  API声明：forceHeight?: boolean;  差异内容：NA | 类名：StrutStyle；  API声明：forceHeight?: boolean;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：StrutStyle；  API声明：enabled?: boolean;  差异内容：NA | 类名：StrutStyle；  API声明：enabled?: boolean;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：StrutStyle；  API声明：heightOverride?: boolean;  差异内容：NA | 类名：StrutStyle；  API声明：heightOverride?: boolean;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：StrutStyle；  API声明：halfLeading?: boolean;  差异内容：NA | 类名：StrutStyle；  API声明：halfLeading?: boolean;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：interface ParagraphStyle  差异内容：NA | 类名：text；  API声明：interface ParagraphStyle  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：ParagraphStyle；  API声明：textStyle?: TextStyle;  差异内容：NA | 类名：ParagraphStyle；  API声明：textStyle?: TextStyle;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：ParagraphStyle；  API声明：textDirection?: TextDirection;  差异内容：NA | 类名：ParagraphStyle；  API声明：textDirection?: TextDirection;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：ParagraphStyle；  API声明：align?: TextAlign;  差异内容：NA | 类名：ParagraphStyle；  API声明：align?: TextAlign;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：ParagraphStyle；  API声明：wordBreak?: WordBreak;  差异内容：NA | 类名：ParagraphStyle；  API声明：wordBreak?: WordBreak;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：ParagraphStyle；  API声明：maxLines?: number;  差异内容：NA | 类名：ParagraphStyle；  API声明：maxLines?: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：ParagraphStyle；  API声明：breakStrategy?: BreakStrategy;  差异内容：NA | 类名：ParagraphStyle；  API声明：breakStrategy?: BreakStrategy;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：ParagraphStyle；  API声明：strutStyle?: StrutStyle;  差异内容：NA | 类名：ParagraphStyle；  API声明：strutStyle?: StrutStyle;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：ParagraphStyle；  API声明：textHeightBehavior?: TextHeightBehavior;  差异内容：NA | 类名：ParagraphStyle；  API声明：textHeightBehavior?: TextHeightBehavior;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：ParagraphStyle；  API声明：tab?: TextTab;  差异内容：NA | 类名：ParagraphStyle；  API声明：tab?: TextTab;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：ParagraphStyle；  API声明：trailingSpaceOptimized?: boolean;  差异内容：NA | 类名：ParagraphStyle；  API声明：trailingSpaceOptimized?: boolean;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：ParagraphStyle；  API声明：autoSpace?: boolean;  差异内容：NA | 类名：ParagraphStyle；  API声明：autoSpace?: boolean;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：ParagraphStyle；  API声明：verticalAlign?: TextVerticalAlign;  差异内容：NA | 类名：ParagraphStyle；  API声明：verticalAlign?: TextVerticalAlign;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：ParagraphStyle；  API声明：lineSpacing?: number;  差异内容：NA | 类名：ParagraphStyle；  API声明：lineSpacing?: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum PlaceholderAlignment  差异内容：NA | 类名：text；  API声明：enum PlaceholderAlignment  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：PlaceholderAlignment；  API声明：OFFSET\_AT\_BASELINE  差异内容：NA | 类名：PlaceholderAlignment；  API声明：OFFSET\_AT\_BASELINE  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：PlaceholderAlignment；  API声明：ABOVE\_BASELINE  差异内容：NA | 类名：PlaceholderAlignment；  API声明：ABOVE\_BASELINE  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：PlaceholderAlignment；  API声明：BELOW\_BASELINE  差异内容：NA | 类名：PlaceholderAlignment；  API声明：BELOW\_BASELINE  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：PlaceholderAlignment；  API声明：TOP\_OF\_ROW\_BOX  差异内容：NA | 类名：PlaceholderAlignment；  API声明：TOP\_OF\_ROW\_BOX  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：PlaceholderAlignment；  API声明：BOTTOM\_OF\_ROW\_BOX  差异内容：NA | 类名：PlaceholderAlignment；  API声明：BOTTOM\_OF\_ROW\_BOX  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：PlaceholderAlignment；  API声明：CENTER\_OF\_ROW\_BOX  差异内容：NA | 类名：PlaceholderAlignment；  API声明：CENTER\_OF\_ROW\_BOX  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：PlaceholderAlignment；  API声明：FOLLOW\_PARAGRAPH  差异内容：NA | 类名：PlaceholderAlignment；  API声明：FOLLOW\_PARAGRAPH  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：interface PlaceholderSpan  差异内容：NA | 类名：text；  API声明：interface PlaceholderSpan  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：PlaceholderSpan；  API声明：width: number;  差异内容：NA | 类名：PlaceholderSpan；  API声明：width: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：PlaceholderSpan；  API声明：height: number;  差异内容：NA | 类名：PlaceholderSpan；  API声明：height: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：PlaceholderSpan；  API声明：align: PlaceholderAlignment;  差异内容：NA | 类名：PlaceholderSpan；  API声明：align: PlaceholderAlignment;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：PlaceholderSpan；  API声明：baseline: TextBaseline;  差异内容：NA | 类名：PlaceholderSpan；  API声明：baseline: TextBaseline;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：PlaceholderSpan；  API声明：baselineOffset: number;  差异内容：NA | 类名：PlaceholderSpan；  API声明：baselineOffset: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：interface Range  差异内容：NA | 类名：text；  API声明：interface Range  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Range；  API声明：start: number;  差异内容：NA | 类名：Range；  API声明：start: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Range；  API声明：end: number;  差异内容：NA | 类名：Range；  API声明：end: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum SystemFontType  差异内容：NA | 类名：text；  API声明：enum SystemFontType  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：SystemFontType；  API声明：ALL = 1 << 0  差异内容：NA | 类名：SystemFontType；  API声明：ALL = 1 << 0  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：SystemFontType；  API声明：GENERIC = 1 << 1  差异内容：NA | 类名：SystemFontType；  API声明：GENERIC = 1 << 1  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：SystemFontType；  API声明：STYLISH = 1 << 2  差异内容：NA | 类名：SystemFontType；  API声明：STYLISH = 1 << 2  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：SystemFontType；  API声明：INSTALLED = 1 << 3  差异内容：NA | 类名：SystemFontType；  API声明：INSTALLED = 1 << 3  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：SystemFontType；  API声明：CUSTOMIZED = 1 << 4  差异内容：NA | 类名：SystemFontType；  API声明：CUSTOMIZED = 1 << 4  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：interface FontDescriptor  差异内容：NA | 类名：text；  API声明：interface FontDescriptor  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontDescriptor；  API声明：path?: string;  差异内容：NA | 类名：FontDescriptor；  API声明：path?: string;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontDescriptor；  API声明：postScriptName?: string;  差异内容：NA | 类名：FontDescriptor；  API声明：postScriptName?: string;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontDescriptor；  API声明：fullName?: string;  差异内容：NA | 类名：FontDescriptor；  API声明：fullName?: string;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontDescriptor；  API声明：fontFamily?: string;  差异内容：NA | 类名：FontDescriptor；  API声明：fontFamily?: string;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontDescriptor；  API声明：fontSubfamily?: string;  差异内容：NA | 类名：FontDescriptor；  API声明：fontSubfamily?: string;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontDescriptor；  API声明：weight?: FontWeight;  差异内容：NA | 类名：FontDescriptor；  API声明：weight?: FontWeight;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontDescriptor；  API声明：width?: number;  差异内容：NA | 类名：FontDescriptor；  API声明：width?: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontDescriptor；  API声明：italic?: number;  差异内容：NA | 类名：FontDescriptor；  API声明：italic?: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontDescriptor；  API声明：monoSpace?: boolean;  差异内容：NA | 类名：FontDescriptor；  API声明：monoSpace?: boolean;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：FontDescriptor；  API声明：symbolic?: boolean;  差异内容：NA | 类名：FontDescriptor；  API声明：symbolic?: boolean;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：class Paragraph  差异内容：NA | 类名：text；  API声明：class Paragraph  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：layoutSync(width: number): void;  差异内容：NA | 类名：Paragraph；  API声明：layoutSync(width: number): void;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：layout(width: number): Promise<void>;  差异内容：NA | 类名：Paragraph；  API声明：layout(width: number): Promise<void>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：paint(canvas: drawing.Canvas, x: number, y: number): void;  差异内容：NA | 类名：Paragraph；  API声明：paint(canvas: drawing.Canvas, x: number, y: number): void;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：paintOnPath(canvas: drawing.Canvas, path: drawing.Path, hOffset: number, vOffset: number): void;  差异内容：NA | 类名：Paragraph；  API声明：paintOnPath(canvas: drawing.Canvas, path: drawing.Path, hOffset: number, vOffset: number): void;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：getMaxWidth(): number;  差异内容：NA | 类名：Paragraph；  API声明：getMaxWidth(): number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：getHeight(): number;  差异内容：NA | 类名：Paragraph；  API声明：getHeight(): number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：getLongestLine(): number;  差异内容：NA | 类名：Paragraph；  API声明：getLongestLine(): number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：getLongestLineWithIndent(): number;  差异内容：NA | 类名：Paragraph；  API声明：getLongestLineWithIndent(): number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：getMinIntrinsicWidth(): number;  差异内容：NA | 类名：Paragraph；  API声明：getMinIntrinsicWidth(): number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：getMaxIntrinsicWidth(): number;  差异内容：NA | 类名：Paragraph；  API声明：getMaxIntrinsicWidth(): number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：getAlphabeticBaseline(): number;  差异内容：NA | 类名：Paragraph；  API声明：getAlphabeticBaseline(): number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：getIdeographicBaseline(): number;  差异内容：NA | 类名：Paragraph；  API声明：getIdeographicBaseline(): number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：getRectsForRange(range: Range, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>;  差异内容：NA | 类名：Paragraph；  API声明：getRectsForRange(range: Range, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：getRectsForPlaceholders(): Array<TextBox>;  差异内容：NA | 类名：Paragraph；  API声明：getRectsForPlaceholders(): Array<TextBox>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity;  差异内容：NA | 类名：Paragraph；  API声明：getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：getWordBoundary(offset: number): Range;  差异内容：NA | 类名：Paragraph；  API声明：getWordBoundary(offset: number): Range;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：getLineCount(): number;  差异内容：NA | 类名：Paragraph；  API声明：getLineCount(): number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：getLineHeight(line: number): number;  差异内容：NA | 类名：Paragraph；  API声明：getLineHeight(line: number): number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：getLineWidth(line: number): number;  差异内容：NA | 类名：Paragraph；  API声明：getLineWidth(line: number): number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：didExceedMaxLines(): boolean;  差异内容：NA | 类名：Paragraph；  API声明：didExceedMaxLines(): boolean;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：getTextLines(): Array<TextLine>;  差异内容：NA | 类名：Paragraph；  API声明：getTextLines(): Array<TextLine>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：getActualTextRange(lineNumber: number, includeSpaces: boolean): Range;  差异内容：NA | 类名：Paragraph；  API声明：getActualTextRange(lineNumber: number, includeSpaces: boolean): Range;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：getLineMetrics(): Array<LineMetrics>;  差异内容：NA | 类名：Paragraph；  API声明：getLineMetrics(): Array<LineMetrics>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：getLineMetrics(lineNumber: number): LineMetrics | undefined;  差异内容：NA | 类名：Paragraph；  API声明：getLineMetrics(lineNumber: number): LineMetrics | undefined;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：updateColor(color: common2D.Color): void;  差异内容：NA | 类名：Paragraph；  API声明：updateColor(color: common2D.Color): void;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Paragraph；  API声明：updateDecoration(decoration: Decoration): void;  差异内容：NA | 类名：Paragraph；  API声明：updateDecoration(decoration: Decoration): void;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：class LineTypeset  差异内容：NA | 类名：text；  API声明：class LineTypeset  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：LineTypeset；  API声明：getLineBreak(startIndex: number, width: number): number;  差异内容：NA | 类名：LineTypeset；  API声明：getLineBreak(startIndex: number, width: number): number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：LineTypeset；  API声明：createLine(startIndex: number, count: number): TextLine;  差异内容：NA | 类名：LineTypeset；  API声明：createLine(startIndex: number, count: number): TextLine;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：interface TextBox  差异内容：NA | 类名：text；  API声明：interface TextBox  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextBox；  API声明：rect: common2D.Rect;  差异内容：NA | 类名：TextBox；  API声明：rect: common2D.Rect;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextBox；  API声明：direction: TextDirection;  差异内容：NA | 类名：TextBox；  API声明：direction: TextDirection;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：interface PositionWithAffinity  差异内容：NA | 类名：text；  API声明：interface PositionWithAffinity  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：PositionWithAffinity；  API声明：position: number;  差异内容：NA | 类名：PositionWithAffinity；  API声明：position: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：PositionWithAffinity；  API声明：affinity: Affinity;  差异内容：NA | 类名：PositionWithAffinity；  API声明：affinity: Affinity;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum RectWidthStyle  差异内容：NA | 类名：text；  API声明：enum RectWidthStyle  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：RectWidthStyle；  API声明：TIGHT  差异内容：NA | 类名：RectWidthStyle；  API声明：TIGHT  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：RectWidthStyle；  API声明：MAX  差异内容：NA | 类名：RectWidthStyle；  API声明：MAX  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum RectHeightStyle  差异内容：NA | 类名：text；  API声明：enum RectHeightStyle  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：RectHeightStyle；  API声明：TIGHT  差异内容：NA | 类名：RectHeightStyle；  API声明：TIGHT  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：RectHeightStyle；  API声明：MAX  差异内容：NA | 类名：RectHeightStyle；  API声明：MAX  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：RectHeightStyle；  API声明：INCLUDE\_LINE\_SPACE\_MIDDLE  差异内容：NA | 类名：RectHeightStyle；  API声明：INCLUDE\_LINE\_SPACE\_MIDDLE  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：RectHeightStyle；  API声明：INCLUDE\_LINE\_SPACE\_TOP  差异内容：NA | 类名：RectHeightStyle；  API声明：INCLUDE\_LINE\_SPACE\_TOP  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：RectHeightStyle；  API声明：INCLUDE\_LINE\_SPACE\_BOTTOM  差异内容：NA | 类名：RectHeightStyle；  API声明：INCLUDE\_LINE\_SPACE\_BOTTOM  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：RectHeightStyle；  API声明：STRUT  差异内容：NA | 类名：RectHeightStyle；  API声明：STRUT  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum Affinity  差异内容：NA | 类名：text；  API声明：enum Affinity  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Affinity；  API声明：UPSTREAM  差异内容：NA | 类名：Affinity；  API声明：UPSTREAM  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Affinity；  API声明：DOWNSTREAM  差异内容：NA | 类名：Affinity；  API声明：DOWNSTREAM  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：class ParagraphBuilder  差异内容：NA | 类名：text；  API声明：class ParagraphBuilder  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：ParagraphBuilder；  API声明：pushStyle(textStyle: TextStyle): void;  差异内容：NA | 类名：ParagraphBuilder；  API声明：pushStyle(textStyle: TextStyle): void;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：ParagraphBuilder；  API声明：popStyle(): void;  差异内容：NA | 类名：ParagraphBuilder；  API声明：popStyle(): void;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：ParagraphBuilder；  API声明：addText(text: string): void;  差异内容：NA | 类名：ParagraphBuilder；  API声明：addText(text: string): void;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：ParagraphBuilder；  API声明：addPlaceholder(placeholderSpan: PlaceholderSpan): void;  差异内容：NA | 类名：ParagraphBuilder；  API声明：addPlaceholder(placeholderSpan: PlaceholderSpan): void;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：ParagraphBuilder；  API声明：build(): Paragraph;  差异内容：NA | 类名：ParagraphBuilder；  API声明：build(): Paragraph;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：ParagraphBuilder；  API声明：buildLineTypeset(): LineTypeset;  差异内容：NA | 类名：ParagraphBuilder；  API声明：buildLineTypeset(): LineTypeset;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：ParagraphBuilder；  API声明：addSymbol(symbolId: number): void;  差异内容：NA | 类名：ParagraphBuilder；  API声明：addSymbol(symbolId: number): void;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：interface TypographicBounds  差异内容：NA | 类名：text；  API声明：interface TypographicBounds  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TypographicBounds；  API声明：ascent: number;  差异内容：NA | 类名：TypographicBounds；  API声明：ascent: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TypographicBounds；  API声明：descent: number;  差异内容：NA | 类名：TypographicBounds；  API声明：descent: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TypographicBounds；  API声明：leading: number;  差异内容：NA | 类名：TypographicBounds；  API声明：leading: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TypographicBounds；  API声明：width: number;  差异内容：NA | 类名：TypographicBounds；  API声明：width: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：type CaretOffsetsCallback = (offset: number, index: number, leadingEdge: boolean) => boolean;  差异内容：NA | 类名：text；  API声明：type CaretOffsetsCallback = (offset: number, index: number, leadingEdge: boolean) => boolean;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：class TextLine  差异内容：NA | 类名：text；  API声明：class TextLine  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextLine；  API声明：getGlyphCount(): number;  差异内容：NA | 类名：TextLine；  API声明：getGlyphCount(): number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextLine；  API声明：getTextRange(): Range;  差异内容：NA | 类名：TextLine；  API声明：getTextRange(): Range;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextLine；  API声明：getGlyphRuns(): Array<Run>;  差异内容：NA | 类名：TextLine；  API声明：getGlyphRuns(): Array<Run>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextLine；  API声明：paint(canvas: drawing.Canvas, x: number, y: number): void;  差异内容：NA | 类名：TextLine；  API声明：paint(canvas: drawing.Canvas, x: number, y: number): void;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextLine；  API声明：createTruncatedLine(width: number, ellipsisMode: EllipsisMode, ellipsis: string): TextLine;  差异内容：NA | 类名：TextLine；  API声明：createTruncatedLine(width: number, ellipsisMode: EllipsisMode, ellipsis: string): TextLine;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextLine；  API声明：getTypographicBounds(): TypographicBounds;  差异内容：NA | 类名：TextLine；  API声明：getTypographicBounds(): TypographicBounds;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextLine；  API声明：getImageBounds(): common2D.Rect;  差异内容：NA | 类名：TextLine；  API声明：getImageBounds(): common2D.Rect;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextLine；  API声明：getTrailingSpaceWidth(): number;  差异内容：NA | 类名：TextLine；  API声明：getTrailingSpaceWidth(): number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextLine；  API声明：getStringIndexForPosition(point: common2D.Point): number;  差异内容：NA | 类名：TextLine；  API声明：getStringIndexForPosition(point: common2D.Point): number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextLine；  API声明：getOffsetForStringIndex(index: number): number;  差异内容：NA | 类名：TextLine；  API声明：getOffsetForStringIndex(index: number): number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextLine；  API声明：enumerateCaretOffsets(callback: CaretOffsetsCallback): void;  差异内容：NA | 类名：TextLine；  API声明：enumerateCaretOffsets(callback: CaretOffsetsCallback): void;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextLine；  API声明：getAlignmentOffset(alignmentFactor: number, alignmentWidth: number): number;  差异内容：NA | 类名：TextLine；  API声明：getAlignmentOffset(alignmentFactor: number, alignmentWidth: number): number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：class Run  差异内容：NA | 类名：text；  API声明：class Run  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Run；  API声明：getGlyphCount(): number;  差异内容：NA | 类名：Run；  API声明：getGlyphCount(): number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Run；  API声明：getGlyphs(): Array<number>;  差异内容：NA | 类名：Run；  API声明：getGlyphs(): Array<number>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Run；  API声明：getGlyphs(range: Range): Array<number>;  差异内容：NA | 类名：Run；  API声明：getGlyphs(range: Range): Array<number>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Run；  API声明：getPositions(): Array<common2D.Point>;  差异内容：NA | 类名：Run；  API声明：getPositions(): Array<common2D.Point>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Run；  API声明：getPositions(range: Range): Array<common2D.Point>;  差异内容：NA | 类名：Run；  API声明：getPositions(range: Range): Array<common2D.Point>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Run；  API声明：getOffsets(): Array<common2D.Point>;  差异内容：NA | 类名：Run；  API声明：getOffsets(): Array<common2D.Point>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Run；  API声明：getFont(): drawing.Font;  差异内容：NA | 类名：Run；  API声明：getFont(): drawing.Font;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Run；  API声明：paint(canvas: drawing.Canvas, x: number, y: number): void;  差异内容：NA | 类名：Run；  API声明：paint(canvas: drawing.Canvas, x: number, y: number): void;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Run；  API声明：getStringIndices(range?: Range): Array<number>;  差异内容：NA | 类名：Run；  API声明：getStringIndices(range?: Range): Array<number>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Run；  API声明：getStringRange(): Range;  差异内容：NA | 类名：Run；  API声明：getStringRange(): Range;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Run；  API声明：getTypographicBounds(): TypographicBounds;  差异内容：NA | 类名：Run；  API声明：getTypographicBounds(): TypographicBounds;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Run；  API声明：getImageBounds(): common2D.Rect;  差异内容：NA | 类名：Run；  API声明：getImageBounds(): common2D.Rect;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Run；  API声明：getTextDirection(): TextDirection;  差异内容：NA | 类名：Run；  API声明：getTextDirection(): TextDirection;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：Run；  API声明：getAdvances(range: Range): Array<common2D.Point>;  差异内容：NA | 类名：Run；  API声明：getAdvances(range: Range): Array<common2D.Point>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：interface RunMetrics  差异内容：NA | 类名：text；  API声明：interface RunMetrics  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：RunMetrics；  API声明：textStyle: TextStyle;  差异内容：NA | 类名：RunMetrics；  API声明：textStyle: TextStyle;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：RunMetrics；  API声明：fontMetrics: drawing.FontMetrics;  差异内容：NA | 类名：RunMetrics；  API声明：fontMetrics: drawing.FontMetrics;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：interface LineMetrics  差异内容：NA | 类名：text；  API声明：interface LineMetrics  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：LineMetrics；  API声明：startIndex: number;  差异内容：NA | 类名：LineMetrics；  API声明：startIndex: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：LineMetrics；  API声明：endIndex: number;  差异内容：NA | 类名：LineMetrics；  API声明：endIndex: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：LineMetrics；  API声明：ascent: number;  差异内容：NA | 类名：LineMetrics；  API声明：ascent: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：LineMetrics；  API声明：descent: number;  差异内容：NA | 类名：LineMetrics；  API声明：descent: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：LineMetrics；  API声明：height: number;  差异内容：NA | 类名：LineMetrics；  API声明：height: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：LineMetrics；  API声明：width: number;  差异内容：NA | 类名：LineMetrics；  API声明：width: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：LineMetrics；  API声明：left: number;  差异内容：NA | 类名：LineMetrics；  API声明：left: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：LineMetrics；  API声明：baseline: number;  差异内容：NA | 类名：LineMetrics；  API声明：baseline: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：LineMetrics；  API声明：lineNumber: number;  差异内容：NA | 类名：LineMetrics；  API声明：lineNumber: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：LineMetrics；  API声明：topHeight: number;  差异内容：NA | 类名：LineMetrics；  API声明：topHeight: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：LineMetrics；  API声明：runMetrics: Map<number, RunMetrics>;  差异内容：NA | 类名：LineMetrics；  API声明：runMetrics: Map<number, RunMetrics>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：function getSystemFontFullNamesByType(fontType: SystemFontType): Promise<Array<string>>;  差异内容：NA | 类名：text；  API声明：function getSystemFontFullNamesByType(fontType: SystemFontType): Promise<Array<string>>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：function getFontDescriptorByFullName(fullName: string, fontType: SystemFontType): Promise<FontDescriptor>;  差异内容：NA | 类名：text；  API声明：function getFontDescriptorByFullName(fullName: string, fontType: SystemFontType): Promise<FontDescriptor>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：function matchFontDescriptors(desc: FontDescriptor): Promise<Array<FontDescriptor>>;  差异内容：NA | 类名：text；  API声明：function matchFontDescriptors(desc: FontDescriptor): Promise<Array<FontDescriptor>>;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：interface TextTab  差异内容：NA | 类名：text；  API声明：interface TextTab  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextTab；  API声明：alignment: TextAlign;  差异内容：NA | 类名：TextTab；  API声明：alignment: TextAlign;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextTab；  API声明：location: number;  差异内容：NA | 类名：TextTab；  API声明：location: number;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum TextHighContrast  差异内容：NA | 类名：text；  API声明：enum TextHighContrast  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextHighContrast；  API声明：TEXT\_FOLLOW\_SYSTEM\_HIGH\_CONTRAST  差异内容：NA | 类名：TextHighContrast；  API声明：TEXT\_FOLLOW\_SYSTEM\_HIGH\_CONTRAST  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextHighContrast；  API声明：TEXT\_APP\_DISABLE\_HIGH\_CONTRAST  差异内容：NA | 类名：TextHighContrast；  API声明：TEXT\_APP\_DISABLE\_HIGH\_CONTRAST  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextHighContrast；  API声明：TEXT\_APP\_ENABLE\_HIGH\_CONTRAST  差异内容：NA | 类名：TextHighContrast；  API声明：TEXT\_APP\_ENABLE\_HIGH\_CONTRAST  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：function setTextHighContrast(action: TextHighContrast): void;  差异内容：NA | 类名：text；  API声明：function setTextHighContrast(action: TextHighContrast): void;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：enum TextUndefinedGlyphDisplay  差异内容：NA | 类名：text；  API声明：enum TextUndefinedGlyphDisplay  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextUndefinedGlyphDisplay；  API声明：USE\_DEFAULT  差异内容：NA | 类名：TextUndefinedGlyphDisplay；  API声明：USE\_DEFAULT  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextUndefinedGlyphDisplay；  API声明：USE\_TOFU  差异内容：NA | 类名：TextUndefinedGlyphDisplay；  API声明：USE\_TOFU  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
| API从不支持元服务到支持元服务 | 类名：text；  API声明：function setTextUndefinedGlyphDisplay(noGlyphShow: TextUndefinedGlyphDisplay): void;  差异内容：NA | 类名：text；  API声明：function setTextUndefinedGlyphDisplay(noGlyphShow: TextUndefinedGlyphDisplay): void;  差异内容：atomicservice | api/@ohos.graphics.text.d.ts |
