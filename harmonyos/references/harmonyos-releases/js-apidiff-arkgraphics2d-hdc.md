---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics2d-hdc
title: ArkGraphics 2D
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta1引入的API > ArkGraphics 2D
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:50+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d88df366b2c8d88493aa16bdac4ddc6421f79510c196a83dd28a4a16dc266eff
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API卡片权限变更 | 类名：global；  API声明： declare namespace effectKit  差异内容：NA | 类名：global；  API声明： declare namespace effectKit  差异内容：form | api/@ohos.effectKit.d.ts |
| API卡片权限变更 | 类名：effectKit；  API声明： interface Filter  差异内容：NA | 类名：effectKit；  API声明： interface Filter  差异内容：form | api/@ohos.effectKit.d.ts |
| API卡片权限变更 | 类名：Filter；  API声明：blur(radius: number): Filter;  差异内容：NA | 类名：Filter；  API声明：blur(radius: number): Filter;  差异内容：form | api/@ohos.effectKit.d.ts |
| API卡片权限变更 | 类名：Filter；  API声明：brightness(bright: number): Filter;  差异内容：NA | 类名：Filter；  API声明：brightness(bright: number): Filter;  差异内容：form | api/@ohos.effectKit.d.ts |
| API卡片权限变更 | 类名：Filter；  API声明：grayscale(): Filter;  差异内容：NA | 类名：Filter；  API声明：grayscale(): Filter;  差异内容：form | api/@ohos.effectKit.d.ts |
| API卡片权限变更 | 类名：effectKit；  API声明： interface ColorPicker  差异内容：NA | 类名：effectKit；  API声明： interface ColorPicker  差异内容：form | api/@ohos.effectKit.d.ts |
| API卡片权限变更 | 类名：ColorPicker；  API声明：getMainColor(): Promise<Color>;  差异内容：NA | 类名：ColorPicker；  API声明：getMainColor(): Promise<Color>;  差异内容：form | api/@ohos.effectKit.d.ts |
| API卡片权限变更 | 类名：ColorPicker；  API声明：getMainColorSync(): Color;  差异内容：NA | 类名：ColorPicker；  API声明：getMainColorSync(): Color;  差异内容：form | api/@ohos.effectKit.d.ts |
| API卡片权限变更 | 类名：effectKit；  API声明： interface Color  差异内容：NA | 类名：effectKit；  API声明： interface Color  差异内容：form | api/@ohos.effectKit.d.ts |
| API卡片权限变更 | 类名：Color；  API声明：red: number;  差异内容：NA | 类名：Color；  API声明：red: number;  差异内容：form | api/@ohos.effectKit.d.ts |
| API卡片权限变更 | 类名：Color；  API声明：green: number;  差异内容：NA | 类名：Color；  API声明：green: number;  差异内容：form | api/@ohos.effectKit.d.ts |
| API卡片权限变更 | 类名：Color；  API声明：blue: number;  差异内容：NA | 类名：Color；  API声明：blue: number;  差异内容：form | api/@ohos.effectKit.d.ts |
| API卡片权限变更 | 类名：Color；  API声明：alpha: number;  差异内容：NA | 类名：Color；  API声明：alpha: number;  差异内容：form | api/@ohos.effectKit.d.ts |
| API卡片权限变更 | 类名：effectKit；  API声明：function createEffect(source: image.PixelMap): Filter;  差异内容：NA | 类名：effectKit；  API声明：function createEffect(source: image.PixelMap): Filter;  差异内容：form | api/@ohos.effectKit.d.ts |
| API卡片权限变更 | 类名：effectKit；  API声明：function createColorPicker(source: image.PixelMap): Promise<ColorPicker>;  差异内容：NA | 类名：effectKit；  API声明：function createColorPicker(source: image.PixelMap): Promise<ColorPicker>;  差异内容：form | api/@ohos.effectKit.d.ts |
| API卡片权限变更 | 类名：effectKit；  API声明：function createColorPicker(source: image.PixelMap, callback: AsyncCallback<ColorPicker>): void;  差异内容：NA | 类名：effectKit；  API声明：function createColorPicker(source: image.PixelMap, callback: AsyncCallback<ColorPicker>): void;  差异内容：form | api/@ohos.effectKit.d.ts |
| API废弃版本变更 | 类名：Filter；  API声明：getPixelMap(): image.PixelMap;  差异内容：NA | 类名：Filter；  API声明：getPixelMap(): image.PixelMap;  差异内容：11 | api/@ohos.effectKit.d.ts |
| 错误码变更 | 类名：effectKit；  API声明：function createColorPicker(source: image.PixelMap): Promise<ColorPicker>;  差异内容：NA | 类名：effectKit；  API声明：function createColorPicker(source: image.PixelMap): Promise<ColorPicker>;  差异内容：401 | api/@ohos.effectKit.d.ts |
| 错误码变更 | 类名：effectKit；  API声明：function createColorPicker(source: image.PixelMap, callback: AsyncCallback<ColorPicker>): void;  差异内容：NA | 类名：effectKit；  API声明：function createColorPicker(source: image.PixelMap, callback: AsyncCallback<ColorPicker>): void;  差异内容：401 | api/@ohos.effectKit.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace drawing  差异内容： declare namespace drawing | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum BlendMode  差异内容： enum BlendMode | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：CLEAR = 0  差异内容：CLEAR = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：SRC = 1  差异内容：SRC = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：DST = 2  差异内容：DST = 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：SRC\_OVER = 3  差异内容：SRC\_OVER = 3 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：DST\_OVER = 4  差异内容：DST\_OVER = 4 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：SRC\_IN = 5  差异内容：SRC\_IN = 5 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：DST\_IN = 6  差异内容：DST\_IN = 6 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：SRC\_OUT = 7  差异内容：SRC\_OUT = 7 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：DST\_OUT = 8  差异内容：DST\_OUT = 8 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：SRC\_ATOP = 9  差异内容：SRC\_ATOP = 9 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：DST\_ATOP = 10  差异内容：DST\_ATOP = 10 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：XOR = 11  差异内容：XOR = 11 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：PLUS = 12  差异内容：PLUS = 12 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：MODULATE = 13  差异内容：MODULATE = 13 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：SCREEN = 14  差异内容：SCREEN = 14 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：OVERLAY = 15  差异内容：OVERLAY = 15 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：DARKEN = 16  差异内容：DARKEN = 16 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：LIGHTEN = 17  差异内容：LIGHTEN = 17 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：COLOR\_DODGE = 18  差异内容：COLOR\_DODGE = 18 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：COLOR\_BURN = 19  差异内容：COLOR\_BURN = 19 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：HARD\_LIGHT = 20  差异内容：HARD\_LIGHT = 20 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：SOFT\_LIGHT = 21  差异内容：SOFT\_LIGHT = 21 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：DIFFERENCE = 22  差异内容：DIFFERENCE = 22 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：EXCLUSION = 23  差异内容：EXCLUSION = 23 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：MULTIPLY = 24  差异内容：MULTIPLY = 24 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：HUE = 25  差异内容：HUE = 25 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：SATURATION = 26  差异内容：SATURATION = 26 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：COLOR = 27  差异内容：COLOR = 27 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：LUMINOSITY = 28  差异内容：LUMINOSITY = 28 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： class Path  差异内容： class Path | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：moveTo(x: number, y: number): void;  差异内容：moveTo(x: number, y: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：lineTo(x: number, y: number): void;  差异内容：lineTo(x: number, y: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：arcTo(x1: number, y1: number, x2: number, y2: number, startDeg: number, sweepDeg: number): void;  差异内容：arcTo(x1: number, y1: number, x2: number, y2: number, startDeg: number, sweepDeg: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：quadTo(ctrlX: number, ctrlY: number, endX: number, endY: number): void;  差异内容：quadTo(ctrlX: number, ctrlY: number, endX: number, endY: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：cubicTo(ctrlX1: number, ctrlY1: number, ctrlX2: number, ctrlY2: number, endX: number, endY: number): void;  差异内容：cubicTo(ctrlX1: number, ctrlY1: number, ctrlX2: number, ctrlY2: number, endX: number, endY: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：close(): void;  差异内容：close(): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：reset(): void;  差异内容：reset(): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum FilterMode  差异内容： enum FilterMode | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FilterMode；  API声明：FILTER\_MODE\_NEAREST = 0  差异内容：FILTER\_MODE\_NEAREST = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FilterMode；  API声明：FILTER\_MODE\_LINEAR = 1  差异内容：FILTER\_MODE\_LINEAR = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： class SamplingOptions  差异内容： class SamplingOptions | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： class Canvas  差异内容： class Canvas | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawRect(rect: common2D.Rect): void;  差异内容：drawRect(rect: common2D.Rect): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawCircle(x: number, y: number, radius: number): void;  差异内容：drawCircle(x: number, y: number, radius: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawImage(pixelmap: image.PixelMap, left: number, top: number, samplingOptions?: SamplingOptions): void;  差异内容：drawImage(pixelmap: image.PixelMap, left: number, top: number, samplingOptions?: SamplingOptions): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawColor(color: common2D.Color, blendMode?: BlendMode): void;  差异内容：drawColor(color: common2D.Color, blendMode?: BlendMode): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawPoint(x: number, y: number): void;  差异内容：drawPoint(x: number, y: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawPath(path: Path): void;  差异内容：drawPath(path: Path): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawLine(x0: number, y0: number, x1: number, y1: number): void;  差异内容：drawLine(x0: number, y0: number, x1: number, y1: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawTextBlob(blob: TextBlob, x: number, y: number): void;  差异内容：drawTextBlob(blob: TextBlob, x: number, y: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawPixelMapMesh(pixelmap: image.PixelMap, meshWidth: number, meshHeight: number, vertices: Array<number>, vertOffset: number, colors: Array<number>, colorOffset: number): void;  差异内容：drawPixelMapMesh(pixelmap: image.PixelMap, meshWidth: number, meshHeight: number, vertices: Array<number>, vertOffset: number, colors: Array<number>, colorOffset: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：attachPen(pen: Pen): void;  差异内容：attachPen(pen: Pen): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：attachBrush(brush: Brush): void;  差异内容：attachBrush(brush: Brush): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：detachPen(): void;  差异内容：detachPen(): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：detachBrush(): void;  差异内容：detachBrush(): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：save(): number;  差异内容：save(): number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：restore(): void;  差异内容：restore(): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：restoreToCount(count: number): void;  差异内容：restoreToCount(count: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：getSaveCount(): number;  差异内容：getSaveCount(): number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：scale(sx: number, sy: number): void;  差异内容：scale(sx: number, sy: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：skew(sx: number, sy: number): void;  差异内容：skew(sx: number, sy: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：rotate(degrees: number, sx: number, sy: number): void;  差异内容：rotate(degrees: number, sx: number, sy: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：translate(dx: number, dy: number): void;  差异内容：translate(dx: number, dy: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：clipPath(path: Path, clipOp?: ClipOp, doAntiAlias?: boolean): void;  差异内容：clipPath(path: Path, clipOp?: ClipOp, doAntiAlias?: boolean): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：clipRect(rect: common2D.Rect, clipOp?: ClipOp, doAntiAlias?: boolean): void;  差异内容：clipRect(rect: common2D.Rect, clipOp?: ClipOp, doAntiAlias?: boolean): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum ClipOp  差异内容： enum ClipOp | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ClipOp；  API声明：DIFFERENCE = 0  差异内容：DIFFERENCE = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ClipOp；  API声明：INTERSECT = 1  差异内容：INTERSECT = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： interface TextBlobRunBuffer  差异内容： interface TextBlobRunBuffer | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：TextBlobRunBuffer；  API声明：glyph: number;  差异内容：glyph: number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：TextBlobRunBuffer；  API声明：positionX: number;  差异内容：positionX: number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：TextBlobRunBuffer；  API声明：positionY: number;  差异内容：positionY: number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum TextEncoding  差异内容： enum TextEncoding | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：TextEncoding；  API声明：TEXT\_ENCODING\_UTF8 = 0  差异内容：TEXT\_ENCODING\_UTF8 = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：TextEncoding；  API声明：TEXT\_ENCODING\_UTF16 = 1  差异内容：TEXT\_ENCODING\_UTF16 = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：TextEncoding；  API声明：TEXT\_ENCODING\_UTF32 = 2  差异内容：TEXT\_ENCODING\_UTF32 = 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：TextEncoding；  API声明：TEXT\_ENCODING\_GLYPH\_ID = 3  差异内容：TEXT\_ENCODING\_GLYPH\_ID = 3 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： class TextBlob  差异内容： class TextBlob | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：TextBlob；  API声明：static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob;  差异内容：static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：TextBlob；  API声明：static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob;  差异内容：static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：TextBlob；  API声明：bounds(): common2D.Rect;  差异内容：bounds(): common2D.Rect; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： class Typeface  差异内容： class Typeface | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Typeface；  API声明：getFamilyName(): string;  差异内容：getFamilyName(): string; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： class Font  差异内容： class Font | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：enableSubpixel(isSubpixel: boolean): void;  差异内容：enableSubpixel(isSubpixel: boolean): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：enableEmbolden(isEmbolden: boolean): void;  差异内容：enableEmbolden(isEmbolden: boolean): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：enableLinearMetrics(isLinearMetrics: boolean): void;  差异内容：enableLinearMetrics(isLinearMetrics: boolean): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：setSize(textSize: number): void;  差异内容：setSize(textSize: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：getSize(): number;  差异内容：getSize(): number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：setTypeface(typeface: Typeface): void;  差异内容：setTypeface(typeface: Typeface): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：getTypeface(): Typeface;  差异内容：getTypeface(): Typeface; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：getMetrics(): FontMetrics;  差异内容：getMetrics(): FontMetrics; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：measureText(text: string, encoding: TextEncoding): number;  差异内容：measureText(text: string, encoding: TextEncoding): number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： interface FontMetrics  差异内容： interface FontMetrics | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetrics；  API声明：top: number;  差异内容：top: number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetrics；  API声明：ascent: number;  差异内容：ascent: number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetrics；  API声明：descent: number;  差异内容：descent: number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetrics；  API声明：bottom: number;  差异内容：bottom: number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontMetrics；  API声明：leading: number;  差异内容：leading: number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： class MaskFilter  差异内容： class MaskFilter | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：MaskFilter；  API声明：static createBlurMaskFilter(blurType: BlurType, sigma: number): MaskFilter;  差异内容：static createBlurMaskFilter(blurType: BlurType, sigma: number): MaskFilter; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： class PathEffect  差异内容： class PathEffect | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathEffect；  API声明：static createDashPathEffect(intervals: Array<number>, phase: number): PathEffect;  差异内容：static createDashPathEffect(intervals: Array<number>, phase: number): PathEffect; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： class ShadowLayer  差异内容： class ShadowLayer | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ShadowLayer；  API声明：static create(blurRadius: number, x: number, y: number, color: common2D.Color): ShadowLayer;  差异内容：static create(blurRadius: number, x: number, y: number, color: common2D.Color): ShadowLayer; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： class ColorFilter  差异内容： class ColorFilter | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ColorFilter；  API声明：static createBlendModeColorFilter(color: common2D.Color, mode: BlendMode): ColorFilter;  差异内容：static createBlendModeColorFilter(color: common2D.Color, mode: BlendMode): ColorFilter; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ColorFilter；  API声明：static createComposeColorFilter(outer: ColorFilter, inner: ColorFilter): ColorFilter;  差异内容：static createComposeColorFilter(outer: ColorFilter, inner: ColorFilter): ColorFilter; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ColorFilter；  API声明：static createLinearToSRGBGamma(): ColorFilter;  差异内容：static createLinearToSRGBGamma(): ColorFilter; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ColorFilter；  API声明：static createSRGBGammaToLinear(): ColorFilter;  差异内容：static createSRGBGammaToLinear(): ColorFilter; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ColorFilter；  API声明：static createLumaColorFilter(): ColorFilter;  差异内容：static createLumaColorFilter(): ColorFilter; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum JoinStyle  差异内容： enum JoinStyle | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：JoinStyle；  API声明：MITER\_JOIN = 0  差异内容：MITER\_JOIN = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：JoinStyle；  API声明：ROUND\_JOIN = 1  差异内容：ROUND\_JOIN = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：JoinStyle；  API声明：BEVEL\_JOIN = 2  差异内容：BEVEL\_JOIN = 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum CapStyle  差异内容： enum CapStyle | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：CapStyle；  API声明：FLAT\_CAP = 0  差异内容：FLAT\_CAP = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：CapStyle；  API声明：SQUARE\_CAP = 1  差异内容：SQUARE\_CAP = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：CapStyle；  API声明：ROUND\_CAP = 2  差异内容：ROUND\_CAP = 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum BlurType  差异内容： enum BlurType | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlurType；  API声明：NORMAL = 0  差异内容：NORMAL = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlurType；  API声明：SOLID = 1  差异内容：SOLID = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlurType；  API声明：OUTER = 2  差异内容：OUTER = 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：BlurType；  API声明：INNER = 3  差异内容：INNER = 3 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： class Pen  差异内容： class Pen | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：setColor(color: common2D.Color): void;  差异内容：setColor(color: common2D.Color): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：setStrokeWidth(width: number): void;  差异内容：setStrokeWidth(width: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：setAntiAlias(aa: boolean): void;  差异内容：setAntiAlias(aa: boolean): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：setAlpha(alpha: number): void;  差异内容：setAlpha(alpha: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：setColorFilter(filter: ColorFilter): void;  差异内容：setColorFilter(filter: ColorFilter): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：setMaskFilter(filter: MaskFilter): void;  差异内容：setMaskFilter(filter: MaskFilter): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：setPathEffect(effect: PathEffect): void;  差异内容：setPathEffect(effect: PathEffect): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：setShadowLayer(shadowLayer: ShadowLayer): void;  差异内容：setShadowLayer(shadowLayer: ShadowLayer): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：setBlendMode(mode: BlendMode): void;  差异内容：setBlendMode(mode: BlendMode): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：setDither(dither: boolean): void;  差异内容：setDither(dither: boolean): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：setJoinStyle(style: JoinStyle): void;  差异内容：setJoinStyle(style: JoinStyle): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：getJoinStyle(): JoinStyle;  差异内容：getJoinStyle(): JoinStyle; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：setCapStyle(style: CapStyle): void;  差异内容：setCapStyle(style: CapStyle): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：getCapStyle(): CapStyle;  差异内容：getCapStyle(): CapStyle; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： class Brush  差异内容： class Brush | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Brush；  API声明：setColor(color: common2D.Color): void;  差异内容：setColor(color: common2D.Color): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Brush；  API声明：setAntiAlias(aa: boolean): void;  差异内容：setAntiAlias(aa: boolean): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Brush；  API声明：setAlpha(alpha: number): void;  差异内容：setAlpha(alpha: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Brush；  API声明：setColorFilter(filter: ColorFilter): void;  差异内容：setColorFilter(filter: ColorFilter): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Brush；  API声明：setMaskFilter(filter: MaskFilter): void;  差异内容：setMaskFilter(filter: MaskFilter): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Brush；  API声明：setShadowLayer(shadowLayer: ShadowLayer): void;  差异内容：setShadowLayer(shadowLayer: ShadowLayer): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Brush；  API声明：setBlendMode(mode: BlendMode): void;  差异内容：setBlendMode(mode: BlendMode): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：effectKit；  API声明：function createColorPicker(source: image.PixelMap, region: Array<number>): Promise<ColorPicker>;  差异内容：function createColorPicker(source: image.PixelMap, region: Array<number>): Promise<ColorPicker>; | api/@ohos.effectKit.d.ts |
| 新增API | NA | 类名：effectKit；  API声明：function createColorPicker(source: image.PixelMap, region: Array<number>, callback: AsyncCallback<ColorPicker>): void;  差异内容：function createColorPicker(source: image.PixelMap, region: Array<number>, callback: AsyncCallback<ColorPicker>): void; | api/@ohos.effectKit.d.ts |
| 新增API | NA | 类名：Filter；  API声明：invert(): Filter;  差异内容：invert(): Filter; | api/@ohos.effectKit.d.ts |
| 新增API | NA | 类名：Filter；  API声明：setColorMatrix(colorMatrix: Array<number>): Filter;  差异内容：setColorMatrix(colorMatrix: Array<number>): Filter; | api/@ohos.effectKit.d.ts |
| 新增API | NA | 类名：Filter；  API声明：getEffectPixelMap(): Promise<image.PixelMap>;  差异内容：getEffectPixelMap(): Promise<image.PixelMap>; | api/@ohos.effectKit.d.ts |
| 新增API | NA | 类名：ColorPicker；  API声明：getLargestProportionColor(): Color;  差异内容：getLargestProportionColor(): Color; | api/@ohos.effectKit.d.ts |
| 新增API | NA | 类名：ColorPicker；  API声明：getTopProportionColors(colorCount: number): Array<Color | null>;  差异内容：getTopProportionColors(colorCount: number): Array<Color | null>; | api/@ohos.effectKit.d.ts |
| 新增API | NA | 类名：ColorPicker；  API声明：getHighestSaturationColor(): Color;  差异内容：getHighestSaturationColor(): Color; | api/@ohos.effectKit.d.ts |
| 新增API | NA | 类名：ColorPicker；  API声明：getAverageColor(): Color;  差异内容：getAverageColor(): Color; | api/@ohos.effectKit.d.ts |
| 新增API | NA | 类名：ColorPicker；  API声明：isBlackOrWhiteOrGrayColor(color: number): boolean;  差异内容：isBlackOrWhiteOrGrayColor(color: number): boolean; | api/@ohos.effectKit.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：BT709 = 6  差异内容：BT709 = 6 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：BT601\_EBU = 7  差异内容：BT601\_EBU = 7 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：BT601\_SMPTE\_C = 8  差异内容：BT601\_SMPTE\_C = 8 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：BT2020\_HLG = 9  差异内容：BT2020\_HLG = 9 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：BT2020\_PQ = 10  差异内容：BT2020\_PQ = 10 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：P3\_HLG = 11  差异内容：P3\_HLG = 11 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：P3\_PQ = 12  差异内容：P3\_PQ = 12 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：ADOBE\_RGB\_1998\_LIMIT = 13  差异内容：ADOBE\_RGB\_1998\_LIMIT = 13 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：DISPLAY\_P3\_LIMIT = 14  差异内容：DISPLAY\_P3\_LIMIT = 14 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：SRGB\_LIMIT = 15  差异内容：SRGB\_LIMIT = 15 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：BT709\_LIMIT = 16  差异内容：BT709\_LIMIT = 16 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：BT601\_EBU\_LIMIT = 17  差异内容：BT601\_EBU\_LIMIT = 17 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：BT601\_SMPTE\_C\_LIMIT = 18  差异内容：BT601\_SMPTE\_C\_LIMIT = 18 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：BT2020\_HLG\_LIMIT = 19  差异内容：BT2020\_HLG\_LIMIT = 19 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：BT2020\_PQ\_LIMIT = 20  差异内容：BT2020\_PQ\_LIMIT = 20 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：P3\_HLG\_LIMIT = 21  差异内容：P3\_HLG\_LIMIT = 21 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：P3\_PQ\_LIMIT = 22  差异内容：P3\_PQ\_LIMIT = 22 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：LINEAR\_P3 = 23  差异内容：LINEAR\_P3 = 23 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：LINEAR\_SRGB = 24  差异内容：LINEAR\_SRGB = 24 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：LINEAR\_BT709 = LINEAR\_SRGB  差异内容：LINEAR\_BT709 = LINEAR\_SRGB | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：LINEAR\_BT2020 = 25  差异内容：LINEAR\_BT2020 = 25 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：DISPLAY\_SRGB = SRGB  差异内容：DISPLAY\_SRGB = SRGB | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：DISPLAY\_P3\_SRGB = DISPLAY\_P3  差异内容：DISPLAY\_P3\_SRGB = DISPLAY\_P3 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：DISPLAY\_P3\_HLG = P3\_HLG  差异内容：DISPLAY\_P3\_HLG = P3\_HLG | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：DISPLAY\_P3\_PQ = P3\_PQ  差异内容：DISPLAY\_P3\_PQ = P3\_PQ | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace common2D  差异内容： declare namespace common2D | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：common2D；  API声明： interface Color  差异内容： interface Color | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：Color；  API声明：alpha: number;  差异内容：alpha: number; | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：Color；  API声明：red: number;  差异内容：red: number; | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：Color；  API声明：green: number;  差异内容：green: number; | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：Color；  API声明：blue: number;  差异内容：blue: number; | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：common2D；  API声明： interface Rect  差异内容： interface Rect | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：Rect；  API声明：left: number;  差异内容：left: number; | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：Rect；  API声明：top: number;  差异内容：top: number; | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：Rect；  API声明：right: number;  差异内容：right: number; | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：Rect；  API声明：bottom: number;  差异内容：bottom: number; | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：common2D；  API声明： interface Point  差异内容： interface Point | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：Point；  API声明：x: number;  差异内容：x: number; | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：Point；  API声明：y: number;  差异内容：y: number; | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace displaySync  差异内容： declare namespace displaySync | api/@ohos.graphics.displaySync.d.ts |
| 新增API | NA | 类名：displaySync；  API声明： interface IntervalInfo  差异内容： interface IntervalInfo | api/@ohos.graphics.displaySync.d.ts |
| 新增API | NA | 类名：IntervalInfo；  API声明：timestamp: number;  差异内容：timestamp: number; | api/@ohos.graphics.displaySync.d.ts |
| 新增API | NA | 类名：IntervalInfo；  API声明：targetTimestamp: number;  差异内容：targetTimestamp: number; | api/@ohos.graphics.displaySync.d.ts |
| 新增API | NA | 类名：displaySync；  API声明： interface DisplaySync  差异内容： interface DisplaySync | api/@ohos.graphics.displaySync.d.ts |
| 新增API | NA | 类名：DisplaySync；  API声明：setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange): void;  差异内容：setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange): void; | api/@ohos.graphics.displaySync.d.ts |
| 新增API | NA | 类名：DisplaySync；  API声明：on(type: 'frame', callback: Callback<IntervalInfo>): void;  差异内容：on(type: 'frame', callback: Callback<IntervalInfo>): void; | api/@ohos.graphics.displaySync.d.ts |
| 新增API | NA | 类名：DisplaySync；  API声明：off(type: 'frame', callback?: Callback<IntervalInfo>): void;  差异内容：off(type: 'frame', callback?: Callback<IntervalInfo>): void; | api/@ohos.graphics.displaySync.d.ts |
| 新增API | NA | 类名：DisplaySync；  API声明：start(): void;  差异内容：start(): void; | api/@ohos.graphics.displaySync.d.ts |
| 新增API | NA | 类名：DisplaySync；  API声明：stop(): void;  差异内容：stop(): void; | api/@ohos.graphics.displaySync.d.ts |
| 新增API | NA | 类名：displaySync；  API声明：function create(): DisplaySync;  差异内容：function create(): DisplaySync; | api/@ohos.graphics.displaySync.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace hdrCapability  差异内容： declare namespace hdrCapability | api/@ohos.graphics.hdrCapability.d.ts |
| 新增API | NA | 类名：hdrCapability；  API声明： enum HDRFormat  差异内容： enum HDRFormat | api/@ohos.graphics.hdrCapability.d.ts |
| 新增API | NA | 类名：HDRFormat；  API声明：NONE = 0  差异内容：NONE = 0 | api/@ohos.graphics.hdrCapability.d.ts |
| 新增API | NA | 类名：HDRFormat；  API声明：VIDEO\_HLG = 1  差异内容：VIDEO\_HLG = 1 | api/@ohos.graphics.hdrCapability.d.ts |
| 新增API | NA | 类名：HDRFormat；  API声明：VIDEO\_HDR10 = 2  差异内容：VIDEO\_HDR10 = 2 | api/@ohos.graphics.hdrCapability.d.ts |
| 新增API | NA | 类名：HDRFormat；  API声明：VIDEO\_HDR\_VIVID = 3  差异内容：VIDEO\_HDR\_VIVID = 3 | api/@ohos.graphics.hdrCapability.d.ts |
| 新增API | NA | 类名：HDRFormat；  API声明：IMAGE\_HDR\_VIVID\_DUAL = 4  差异内容：IMAGE\_HDR\_VIVID\_DUAL = 4 | api/@ohos.graphics.hdrCapability.d.ts |
| 新增API | NA | 类名：HDRFormat；  API声明：IMAGE\_HDR\_VIVID\_SINGLE = 5  差异内容：IMAGE\_HDR\_VIVID\_SINGLE = 5 | api/@ohos.graphics.hdrCapability.d.ts |
| 新增API | NA | 类名：HDRFormat；  API声明：IMAGE\_HDR\_ISO\_DUAL = 6  差异内容：IMAGE\_HDR\_ISO\_DUAL = 6 | api/@ohos.graphics.hdrCapability.d.ts |
| 新增API | NA | 类名：HDRFormat；  API声明：IMAGE\_HDR\_ISO\_SINGLE = 7  差异内容：IMAGE\_HDR\_ISO\_SINGLE = 7 | api/@ohos.graphics.hdrCapability.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace sendableColorSpaceManager  差异内容： declare namespace sendableColorSpaceManager | api/@ohos.graphics.sendableColorSpaceManager.d.ets |
| 新增API | NA | 类名：sendableColorSpaceManager；  API声明：type ISendable = lang.ISendable;  差异内容：type ISendable = lang.ISendable; | api/@ohos.graphics.sendableColorSpaceManager.d.ets |
| 新增API | NA | 类名：sendableColorSpaceManager；  API声明： interface ColorSpaceManager  差异内容： interface ColorSpaceManager | api/@ohos.graphics.sendableColorSpaceManager.d.ets |
| 新增API | NA | 类名：ColorSpaceManager；  API声明：getColorSpaceName(): colorSpaceManager.ColorSpace;  差异内容：getColorSpaceName(): colorSpaceManager.ColorSpace; | api/@ohos.graphics.sendableColorSpaceManager.d.ets |
| 新增API | NA | 类名：ColorSpaceManager；  API声明：getWhitePoint(): collections.Array<number>;  差异内容：getWhitePoint(): collections.Array<number>; | api/@ohos.graphics.sendableColorSpaceManager.d.ets |
| 新增API | NA | 类名：ColorSpaceManager；  API声明：getGamma(): number;  差异内容：getGamma(): number; | api/@ohos.graphics.sendableColorSpaceManager.d.ets |
| 新增API | NA | 类名：sendableColorSpaceManager；  API声明：function create(colorSpaceName: colorSpaceManager.ColorSpace): ColorSpaceManager;  差异内容：function create(colorSpaceName: colorSpaceManager.ColorSpace): ColorSpaceManager; | api/@ohos.graphics.sendableColorSpaceManager.d.ets |
| 新增API | NA | 类名：sendableColorSpaceManager；  API声明：function create(primaries: colorSpaceManager.ColorSpacePrimaries, gamma: number): ColorSpaceManager;  差异内容：function create(primaries: colorSpaceManager.ColorSpacePrimaries, gamma: number): ColorSpaceManager; | api/@ohos.graphics.sendableColorSpaceManager.d.ets |
| 新增API | NA | 类名：global；  API声明： declare namespace text  差异内容： declare namespace text | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： enum TextAlign  差异内容： enum TextAlign | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextAlign；  API声明：LEFT = 0  差异内容：LEFT = 0 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextAlign；  API声明：RIGHT = 1  差异内容：RIGHT = 1 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextAlign；  API声明：CENTER = 2  差异内容：CENTER = 2 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextAlign；  API声明：JUSTIFY = 3  差异内容：JUSTIFY = 3 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextAlign；  API声明：START = 4  差异内容：START = 4 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextAlign；  API声明：END = 5  差异内容：END = 5 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： enum TextDirection  差异内容： enum TextDirection | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextDirection；  API声明：RTL  差异内容：RTL | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextDirection；  API声明：LTR  差异内容：LTR | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： enum BreakStrategy  差异内容： enum BreakStrategy | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：BreakStrategy；  API声明：GREEDY  差异内容：GREEDY | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：BreakStrategy；  API声明：HIGH\_QUALITY  差异内容：HIGH\_QUALITY | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：BreakStrategy；  API声明：BALANCED  差异内容：BALANCED | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： enum WordBreak  差异内容： enum WordBreak | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：WordBreak；  API声明：NORMAL  差异内容：NORMAL | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：WordBreak；  API声明：BREAK\_ALL  差异内容：BREAK\_ALL | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：WordBreak；  API声明：BREAK\_WORD  差异内容：BREAK\_WORD | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： interface Decoration  差异内容： interface Decoration | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Decoration；  API声明：textDecoration?: TextDecorationType;  差异内容：textDecoration?: TextDecorationType; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Decoration；  API声明：color?: common2D.Color;  差异内容：color?: common2D.Color; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Decoration；  API声明：decorationStyle?: TextDecorationStyle;  差异内容：decorationStyle?: TextDecorationStyle; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Decoration；  API声明：decorationThicknessScale?: number;  差异内容：decorationThicknessScale?: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： enum TextDecorationType  差异内容： enum TextDecorationType | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextDecorationType；  API声明：NONE  差异内容：NONE | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextDecorationType；  API声明：UNDERLINE  差异内容：UNDERLINE | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextDecorationType；  API声明：OVERLINE  差异内容：OVERLINE | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextDecorationType；  API声明：LINE\_THROUGH  差异内容：LINE\_THROUGH | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： enum TextDecorationStyle  差异内容： enum TextDecorationStyle | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextDecorationStyle；  API声明：SOLID  差异内容：SOLID | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextDecorationStyle；  API声明：DOUBLE  差异内容：DOUBLE | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextDecorationStyle；  API声明：DOTTED  差异内容：DOTTED | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextDecorationStyle；  API声明：DASHED  差异内容：DASHED | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextDecorationStyle；  API声明：WAVY  差异内容：WAVY | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： enum FontWeight  差异内容： enum FontWeight | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontWeight；  API声明：W100  差异内容：W100 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontWeight；  API声明：W200  差异内容：W200 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontWeight；  API声明：W300  差异内容：W300 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontWeight；  API声明：W400  差异内容：W400 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontWeight；  API声明：W500  差异内容：W500 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontWeight；  API声明：W600  差异内容：W600 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontWeight；  API声明：W700  差异内容：W700 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontWeight；  API声明：W800  差异内容：W800 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontWeight；  API声明：W900  差异内容：W900 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： enum FontStyle  差异内容： enum FontStyle | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontStyle；  API声明：NORMAL  差异内容：NORMAL | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontStyle；  API声明：ITALIC  差异内容：ITALIC | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontStyle；  API声明：OBLIQUE  差异内容：OBLIQUE | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： enum TextBaseline  差异内容： enum TextBaseline | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextBaseline；  API声明：ALPHABETIC  差异内容：ALPHABETIC | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextBaseline；  API声明：IDEOGRAPHIC  差异内容：IDEOGRAPHIC | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： enum EllipsisMode  差异内容： enum EllipsisMode | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：EllipsisMode；  API声明：START  差异内容：START | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：EllipsisMode；  API声明：MIDDLE  差异内容：MIDDLE | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：EllipsisMode；  API声明：END  差异内容：END | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： interface TextStyle  差异内容： interface TextStyle | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：decoration?: Decoration;  差异内容：decoration?: Decoration; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：color?: common2D.Color;  差异内容：color?: common2D.Color; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：fontWeight?: FontWeight;  差异内容：fontWeight?: FontWeight; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：fontStyle?: FontStyle;  差异内容：fontStyle?: FontStyle; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：baseline?: TextBaseline;  差异内容：baseline?: TextBaseline; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：fontFamilies?: Array<string>;  差异内容：fontFamilies?: Array<string>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：fontSize?: number;  差异内容：fontSize?: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：letterSpacing?: number;  差异内容：letterSpacing?: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：wordSpacing?: number;  差异内容：wordSpacing?: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：heightScale?: number;  差异内容：heightScale?: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：halfLeading?: boolean;  差异内容：halfLeading?: boolean; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：heightOnly?: boolean;  差异内容：heightOnly?: boolean; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：ellipsis?: string;  差异内容：ellipsis?: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：ellipsisMode?: EllipsisMode;  差异内容：ellipsisMode?: EllipsisMode; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：locale?: string;  差异内容：locale?: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： class FontCollection  差异内容： class FontCollection | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontCollection；  API声明：static getGlobalInstance(): FontCollection;  差异内容：static getGlobalInstance(): FontCollection; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontCollection；  API声明：loadFontSync(name: string, path: string | Resource): void;  差异内容：loadFontSync(name: string, path: string | Resource): void; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： interface ParagraphStyle  差异内容： interface ParagraphStyle | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：textStyle?: TextStyle;  差异内容：textStyle?: TextStyle; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：textDirection?: TextDirection;  差异内容：textDirection?: TextDirection; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：align?: TextAlign;  差异内容：align?: TextAlign; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：wordBreak?: WordBreak;  差异内容：wordBreak?: WordBreak; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：maxLines?: number;  差异内容：maxLines?: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：breakStrategy?: BreakStrategy;  差异内容：breakStrategy?: BreakStrategy; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： enum PlaceholderAlignment  差异内容： enum PlaceholderAlignment | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：PlaceholderAlignment；  API声明：OFFSET\_AT\_BASELINE  差异内容：OFFSET\_AT\_BASELINE | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：PlaceholderAlignment；  API声明：ABOVE\_BASELINE  差异内容：ABOVE\_BASELINE | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：PlaceholderAlignment；  API声明：BELOW\_BASELINE  差异内容：BELOW\_BASELINE | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：PlaceholderAlignment；  API声明：TOP\_OF\_ROW\_BOX  差异内容：TOP\_OF\_ROW\_BOX | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：PlaceholderAlignment；  API声明：BOTTOM\_OF\_ROW\_BOX  差异内容：BOTTOM\_OF\_ROW\_BOX | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：PlaceholderAlignment；  API声明：CENTER\_OF\_ROW\_BOX  差异内容：CENTER\_OF\_ROW\_BOX | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： interface PlaceholderSpan  差异内容： interface PlaceholderSpan | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：PlaceholderSpan；  API声明：width: number;  差异内容：width: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：PlaceholderSpan；  API声明：height: number;  差异内容：height: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：PlaceholderSpan；  API声明：align: PlaceholderAlignment;  差异内容：align: PlaceholderAlignment; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：PlaceholderSpan；  API声明：baseline: TextBaseline;  差异内容：baseline: TextBaseline; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：PlaceholderSpan；  API声明：baselineOffset: number;  差异内容：baselineOffset: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： interface Range  差异内容： interface Range | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Range；  API声明：start: number;  差异内容：start: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Range；  API声明：end: number;  差异内容：end: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： class Paragraph  差异内容： class Paragraph | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：layoutSync(width: number): void;  差异内容：layoutSync(width: number): void; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：paint(canvas: drawing.Canvas, x: number, y: number): void;  差异内容：paint(canvas: drawing.Canvas, x: number, y: number): void; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getMaxWidth(): number;  差异内容：getMaxWidth(): number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getHeight(): number;  差异内容：getHeight(): number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getLongestLine(): number;  差异内容：getLongestLine(): number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getMinIntrinsicWidth(): number;  差异内容：getMinIntrinsicWidth(): number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getMaxIntrinsicWidth(): number;  差异内容：getMaxIntrinsicWidth(): number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getAlphabeticBaseline(): number;  差异内容：getAlphabeticBaseline(): number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getIdeographicBaseline(): number;  差异内容：getIdeographicBaseline(): number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getRectsForRange(range: Range, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>;  差异内容：getRectsForRange(range: Range, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getRectsForPlaceholders(): Array<TextBox>;  差异内容：getRectsForPlaceholders(): Array<TextBox>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity;  差异内容：getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getWordBoundary(offset: number): Range;  差异内容：getWordBoundary(offset: number): Range; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getLineCount(): number;  差异内容：getLineCount(): number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getLineHeight(line: number): number;  差异内容：getLineHeight(line: number): number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getLineWidth(line: number): number;  差异内容：getLineWidth(line: number): number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：didExceedMaxLines(): boolean;  差异内容：didExceedMaxLines(): boolean; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getTextLines(): Array<TextLine>;  差异内容：getTextLines(): Array<TextLine>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： interface TextBox  差异内容： interface TextBox | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextBox；  API声明：rect: common2D.Rect;  差异内容：rect: common2D.Rect; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextBox；  API声明：direction: TextDirection;  差异内容：direction: TextDirection; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： interface PositionWithAffinity  差异内容： interface PositionWithAffinity | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：PositionWithAffinity；  API声明：position: number;  差异内容：position: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：PositionWithAffinity；  API声明：affinity: Affinity;  差异内容：affinity: Affinity; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： enum RectWidthStyle  差异内容： enum RectWidthStyle | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：RectWidthStyle；  API声明：TIGHT  差异内容：TIGHT | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：RectWidthStyle；  API声明：MAX  差异内容：MAX | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： enum RectHeightStyle  差异内容： enum RectHeightStyle | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：RectHeightStyle；  API声明：TIGHT  差异内容：TIGHT | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：RectHeightStyle；  API声明：MAX  差异内容：MAX | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：RectHeightStyle；  API声明：INCLUDE\_LINE\_SPACE\_MIDDLE  差异内容：INCLUDE\_LINE\_SPACE\_MIDDLE | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：RectHeightStyle；  API声明：INCLUDE\_LINE\_SPACE\_TOP  差异内容：INCLUDE\_LINE\_SPACE\_TOP | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：RectHeightStyle；  API声明：INCLUDE\_LINE\_SPACE\_BOTTOM  差异内容：INCLUDE\_LINE\_SPACE\_BOTTOM | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：RectHeightStyle；  API声明：STRUT  差异内容：STRUT | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： enum Affinity  差异内容： enum Affinity | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Affinity；  API声明：UPSTREAM  差异内容：UPSTREAM | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Affinity；  API声明：DOWNSTREAM  差异内容：DOWNSTREAM | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： class ParagraphBuilder  差异内容： class ParagraphBuilder | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphBuilder；  API声明：pushStyle(textStyle: TextStyle): void;  差异内容：pushStyle(textStyle: TextStyle): void; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphBuilder；  API声明：popStyle(): void;  差异内容：popStyle(): void; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphBuilder；  API声明：addText(text: string): void;  差异内容：addText(text: string): void; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphBuilder；  API声明：addPlaceholder(placeholderSpan: PlaceholderSpan): void;  差异内容：addPlaceholder(placeholderSpan: PlaceholderSpan): void; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphBuilder；  API声明：build(): Paragraph;  差异内容：build(): Paragraph; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： class TextLine  差异内容： class TextLine | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextLine；  API声明：getGlyphCount(): number;  差异内容：getGlyphCount(): number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextLine；  API声明：getTextRange(): Range;  差异内容：getTextRange(): Range; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextLine；  API声明：getGlyphRuns(): Array<Run>;  差异内容：getGlyphRuns(): Array<Run>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextLine；  API声明：paint(canvas: drawing.Canvas, x: number, y: number): void;  差异内容：paint(canvas: drawing.Canvas, x: number, y: number): void; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： class Run  差异内容： class Run | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Run；  API声明：getGlyphCount(): number;  差异内容：getGlyphCount(): number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Run；  API声明：getGlyphs(): Array<number>;  差异内容：getGlyphs(): Array<number>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Run；  API声明：getPositions(): Array<common2D.Point>;  差异内容：getPositions(): Array<common2D.Point>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Run；  API声明：getOffsets(): Array<common2D.Point>;  差异内容：getOffsets(): Array<common2D.Point>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Run；  API声明：getFont(): drawing.Font;  差异内容：getFont(): drawing.Font; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Run；  API声明：paint(canvas: drawing.Canvas, x: number, y: number): void;  差异内容：paint(canvas: drawing.Canvas, x: number, y: number): void; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace uiEffect  差异内容： declare namespace uiEffect | api/@ohos.graphics.uiEffect.d.ts |
| 新增API | NA | 类名：uiEffect；  API声明： interface Filter  差异内容： interface Filter | api/@ohos.graphics.uiEffect.d.ts |
| 新增API | NA | 类名：Filter；  API声明：blur(blurRadius: number): Filter;  差异内容：blur(blurRadius: number): Filter; | api/@ohos.graphics.uiEffect.d.ts |
| 新增API | NA | 类名：uiEffect；  API声明： interface VisualEffect  差异内容： interface VisualEffect | api/@ohos.graphics.uiEffect.d.ts |
| 新增API | NA | 类名：uiEffect；  API声明：function createFilter(): Filter;  差异内容：function createFilter(): Filter; | api/@ohos.graphics.uiEffect.d.ts |
| 新增API | NA | 类名：uiEffect；  API声明：function createEffect(): VisualEffect;  差异内容：function createEffect(): VisualEffect; | api/@ohos.graphics.uiEffect.d.ts |
