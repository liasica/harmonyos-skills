---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics2d-510
title: ArkGraphics 2D
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > ArkGraphics 2D
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:02+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:b18495600f8c46b2406d557ced45c9b1344875f52683b36c44130c21779377fc
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：drawing；  API声明：enum PathIteratorVerb  差异内容：enum PathIteratorVerb | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathIteratorVerb；  API声明：MOVE = 0  差异内容：MOVE = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathIteratorVerb；  API声明：LINE = 1  差异内容：LINE = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathIteratorVerb；  API声明：QUAD = 2  差异内容：QUAD = 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathIteratorVerb；  API声明：CONIC = 3  差异内容：CONIC = 3 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathIteratorVerb；  API声明：CUBIC = 4  差异内容：CUBIC = 4 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathIteratorVerb；  API声明：CLOSE = 5  差异内容：CLOSE = 5 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathIteratorVerb；  API声明：DONE = CLOSE + 1  差异内容：DONE = CLOSE + 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明：class PathIterator  差异内容：class PathIterator | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathIterator；  API声明：next(points: Array<common2D.Point>, offset?: number): PathIteratorVerb;  差异内容：next(points: Array<common2D.Point>, offset?: number): PathIteratorVerb; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathIterator；  API声明：peek(): PathIteratorVerb;  差异内容：peek(): PathIteratorVerb; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathIterator；  API声明：hasNext(): boolean;  差异内容：hasNext(): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明：enum PathDashStyle  差异内容：enum PathDashStyle | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathDashStyle；  API声明：TRANSLATE = 0  差异内容：TRANSLATE = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathDashStyle；  API声明：ROTATE = 1  差异内容：ROTATE = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathDashStyle；  API声明：MORPH = 2  差异内容：MORPH = 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：WordBreak；  API声明：BREAK\_HYPHEN  差异内容：BREAK\_HYPHEN | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：SystemFontType；  API声明：CUSTOMIZED = 1 << 4  差异内容：CUSTOMIZED = 1 << 4 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明：class LineTypeset  差异内容：class LineTypeset | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：LineTypeset；  API声明：getLineBreak(startIndex: number, width: number): number;  差异内容：getLineBreak(startIndex: number, width: number): number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：LineTypeset；  API声明：createLine(startIndex: number, count: number): TextLine;  差异内容：createLine(startIndex: number, count: number): TextLine; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明：interface TypographicBounds  差异内容：interface TypographicBounds | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TypographicBounds；  API声明：ascent: number;  差异内容：ascent: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TypographicBounds；  API声明：descent: number;  差异内容：descent: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TypographicBounds；  API声明：leading: number;  差异内容：leading: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TypographicBounds；  API声明：width: number;  差异内容：width: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明：type CaretOffsetsCallback = (offset: number, index: number, leadingEdge: boolean) => boolean;  差异内容：type CaretOffsetsCallback = (offset: number, index: number, leadingEdge: boolean) => boolean; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明：function matchFontDescriptors(desc: FontDescriptor): Promise<Array<FontDescriptor>>;  差异内容：function matchFontDescriptors(desc: FontDescriptor): Promise<Array<FontDescriptor>>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明：interface TextTab  差异内容：interface TextTab | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextTab；  API声明：alignment: TextAlign;  差异内容：alignment: TextAlign; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextTab；  API声明：location: number;  差异内容：location: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ColorSpace；  API声明：H\_LOG = 26  差异内容：H\_LOG = 26 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Path；  API声明：getSegment(forceClosed: boolean, start: number, stop: number, startWithMoveTo: boolean, dst: Path): boolean;  差异内容：getSegment(forceClosed: boolean, start: number, stop: number, startWithMoveTo: boolean, dst: Path): boolean; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Path；  API声明：getPathIterator(): PathIterator;  差异内容：getPathIterator(): PathIterator; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Canvas；  API声明：drawImageLattice(pixelmap: image.PixelMap, lattice: Lattice, dstRect: common2D.Rect, filterMode: FilterMode): void;  差异内容：drawImageLattice(pixelmap: image.PixelMap, lattice: Lattice, dstRect: common2D.Rect, filterMode: FilterMode): void; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Canvas；  API声明：drawImageNine(pixelmap: image.PixelMap, center: common2D.Rect, dstRect: common2D.Rect, filterMode: FilterMode): void;  差异内容：drawImageNine(pixelmap: image.PixelMap, center: common2D.Rect, dstRect: common2D.Rect, filterMode: FilterMode): void; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Canvas；  API声明：drawArcWithCenter(arc: common2D.Rect, startAngle: number, sweepAngle: number, useCenter: boolean): void;  差异内容：drawArcWithCenter(arc: common2D.Rect, startAngle: number, sweepAngle: number, useCenter: boolean): void; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Canvas；  API声明：quickRejectPath(path: Path): boolean;  差异内容：quickRejectPath(path: Path): boolean; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Canvas；  API声明：quickRejectRect(rect: common2D.Rect): boolean;  差异内容：quickRejectRect(rect: common2D.Rect): boolean; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Typeface；  API声明：static makeFromRawFile(rawfile: Resource): Typeface;  差异内容：static makeFromRawFile(rawfile: Resource): Typeface; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Font；  API声明：createPathForGlyph(index: number): Path;  差异内容：createPathForGlyph(index: number): Path; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Font；  API声明：getBounds(glyphs: Array<number>): Array<common2D.Rect>;  差异内容：getBounds(glyphs: Array<number>): Array<common2D.Rect>; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Font；  API声明：getTextPath(text: string, byteLength: number, x: number, y: number): Path;  差异内容：getTextPath(text: string, byteLength: number, x: number, y: number): Path; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：PathEffect；  API声明：static createDiscretePathEffect(segLength: number, dev: number, seedAssist?: number): PathEffect;  差异内容：static createDiscretePathEffect(segLength: number, dev: number, seedAssist?: number): PathEffect; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：PathEffect；  API声明：static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect;  差异内容：static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：PathEffect；  API声明：static createPathDashEffect(path: Path, advance: number, phase: number, style: PathDashStyle): PathEffect;  差异内容：static createPathDashEffect(path: Path, advance: number, phase: number, style: PathDashStyle): PathEffect; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：PathEffect；  API声明：static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect;  差异内容：static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Pen；  API声明：getHexColor(): number;  差异内容：getHexColor(): number; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Brush；  API声明：getHexColor(): number;  差异内容：getHexColor(): number; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：FontCollection；  API声明：loadFont(name: string, path: string | Resource): Promise<void>;  差异内容：loadFont(name: string, path: string | Resource): Promise<void>; | api/@ohos.graphics.text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Paragraph；  API声明：layout(width: number): Promise<void>;  差异内容：layout(width: number): Promise<void>; | api/@ohos.graphics.text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：ParagraphBuilder；  API声明：buildLineTypeset(): LineTypeset;  差异内容：buildLineTypeset(): LineTypeset; | api/@ohos.graphics.text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextLine；  API声明：createTruncatedLine(width: number, ellipsisMode: EllipsisMode, ellipsis: string): TextLine;  差异内容：createTruncatedLine(width: number, ellipsisMode: EllipsisMode, ellipsis: string): TextLine; | api/@ohos.graphics.text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextLine；  API声明：getTypographicBounds(): TypographicBounds;  差异内容：getTypographicBounds(): TypographicBounds; | api/@ohos.graphics.text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextLine；  API声明：getImageBounds(): common2D.Rect;  差异内容：getImageBounds(): common2D.Rect; | api/@ohos.graphics.text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextLine；  API声明：getTrailingSpaceWidth(): number;  差异内容：getTrailingSpaceWidth(): number; | api/@ohos.graphics.text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextLine；  API声明：getStringIndexForPosition(point: common2D.Point): number;  差异内容：getStringIndexForPosition(point: common2D.Point): number; | api/@ohos.graphics.text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextLine；  API声明：getOffsetForStringIndex(index: number): number;  差异内容：getOffsetForStringIndex(index: number): number; | api/@ohos.graphics.text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextLine；  API声明：enumerateCaretOffsets(callback: CaretOffsetsCallback): void;  差异内容：enumerateCaretOffsets(callback: CaretOffsetsCallback): void; | api/@ohos.graphics.text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：TextLine；  API声明：getAlignmentOffset(alignmentFactor: number, alignmentWidth: number): number;  差异内容：getAlignmentOffset(alignmentFactor: number, alignmentWidth: number): number; | api/@ohos.graphics.text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Run；  API声明：getStringIndices(range?: Range): Array<number>;  差异内容：getStringIndices(range?: Range): Array<number>; | api/@ohos.graphics.text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Run；  API声明：getStringRange(): Range;  差异内容：getStringRange(): Range; | api/@ohos.graphics.text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Run；  API声明：getTypographicBounds(): TypographicBounds;  差异内容：getTypographicBounds(): TypographicBounds; | api/@ohos.graphics.text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Run；  API声明：getImageBounds(): common2D.Rect;  差异内容：getImageBounds(): common2D.Rect; | api/@ohos.graphics.text.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Canvas；  API声明：drawShadow(path: Path, planeParams: common2D.Point3d, devLightPos: common2D.Point3d, lightRadius: number, ambientColor: common2D.Color, spotColor: common2D.Color, flag: ShadowFlag): void;  差异内容：drawShadow(path: Path, planeParams: common2D.Point3d, devLightPos: common2D.Point3d, lightRadius: number, ambientColor: common2D.Color, spotColor: common2D.Color, flag: ShadowFlag): void; | 类名：Canvas；  API声明：drawShadow(path: Path, planeParams: common2D.Point3d, devLightPos: common2D.Point3d, lightRadius: number, ambientColor: common2D.Color | number, spotColor: common2D.Color | number, flag: ShadowFlag): void;  差异内容：drawShadow(path: Path, planeParams: common2D.Point3d, devLightPos: common2D.Point3d, lightRadius: number, ambientColor: common2D.Color | number, spotColor: common2D.Color | number, flag: ShadowFlag): void; | api/@ohos.graphics.drawing.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Canvas；  API声明：clear(color: common2D.Color): void;  差异内容：clear(color: common2D.Color): void; | 类名：Canvas；  API声明：clear(color: common2D.Color | number): void;  差异内容：clear(color: common2D.Color | number): void; | api/@ohos.graphics.drawing.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Lattice；  API声明：static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number, fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<common2D.Color> | null): Lattice;  差异内容：static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number, fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<common2D.Color> | null): Lattice; | 类名：Lattice；  API声明：static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number, fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<number> | null): Lattice;  差异内容：static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number, fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<number> | null): Lattice; | api/@ohos.graphics.drawing.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：ShadowLayer；  API声明：static create(blurRadius: number, x: number, y: number, color: common2D.Color): ShadowLayer;  差异内容：static create(blurRadius: number, x: number, y: number, color: common2D.Color): ShadowLayer; | 类名：ShadowLayer；  API声明：static create(blurRadius: number, x: number, y: number, color: common2D.Color | number): ShadowLayer;  差异内容：static create(blurRadius: number, x: number, y: number, color: common2D.Color | number): ShadowLayer; | api/@ohos.graphics.drawing.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：ColorFilter；  API声明：static createBlendModeColorFilter(color: common2D.Color, mode: BlendMode): ColorFilter;  差异内容：static createBlendModeColorFilter(color: common2D.Color, mode: BlendMode): ColorFilter; | 类名：ColorFilter；  API声明：static createBlendModeColorFilter(color: common2D.Color | number, mode: BlendMode): ColorFilter;  差异内容：static createBlendModeColorFilter(color: common2D.Color | number, mode: BlendMode): ColorFilter; | api/@ohos.graphics.drawing.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Pen；  API声明：setColor(alpha: number, red: number, green: number, blue: number): void;  差异内容：setColor(alpha: number, red: number, green: number, blue: number): void; | 类名：Pen；  API声明：setColor(color: number): void;  差异内容：setColor(color: number): void; | api/@ohos.graphics.drawing.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Brush；  API声明：setColor(alpha: number, red: number, green: number, blue: number): void;  差异内容：setColor(alpha: number, red: number, green: number, blue: number): void; | 类名：Brush；  API声明：setColor(color: number): void;  差异内容：setColor(color: number): void; | api/@ohos.graphics.drawing.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Run；  API声明：getGlyphs(): Array<number>;  差异内容：getGlyphs(): Array<number>; | 类名：Run；  API声明：getGlyphs(range: Range): Array<number>;  差异内容：getGlyphs(range: Range): Array<number>; | api/@ohos.graphics.text.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Run；  API声明：getPositions(): Array<common2D.Point>;  差异内容：getPositions(): Array<common2D.Point>; | 类名：Run；  API声明：getPositions(range: Range): Array<common2D.Point>;  差异内容：getPositions(range: Range): Array<common2D.Point>; | api/@ohos.graphics.text.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围不是包含关系 | 类名：Canvas；  API声明：drawColor(alpha: number, red: number, green: number, blue: number, blendMode?: BlendMode): void;  差异内容：drawColor(alpha: number, red: number, green: number, blue: number, blendMode?: BlendMode): void; | 类名：Canvas；  API声明：drawColor(color: number, blendMode?: BlendMode): void;  差异内容：drawColor(color: number, blendMode?: BlendMode): void; | api/@ohos.graphics.drawing.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ParagraphStyle；  API声明：tab?: TextTab;  差异内容：tab?: TextTab; | api/@ohos.graphics.text.d.ts |
