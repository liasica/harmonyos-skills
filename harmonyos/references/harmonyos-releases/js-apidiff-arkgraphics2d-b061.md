---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics2d-b061
title: ArkGraphics 2D
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta6引入的API > ArkGraphics 2D
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:23+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:ed7ad707e4117004efb7d47db81fc48063be13cfd849c2f79ec611d2a329648b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：common2D；  API声明： interface Point3d  差异内容： interface Point3d | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：Point3d；  API声明：z: number;  差异内容：z: number; | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum PathDirection  差异内容： enum PathDirection | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathDirection；  API声明：CLOCKWISE = 0  差异内容：CLOCKWISE = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathDirection；  API声明：COUNTER\_CLOCKWISE = 1  差异内容：COUNTER\_CLOCKWISE = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum PathFillType  差异内容： enum PathFillType | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathFillType；  API声明：WINDING = 0  差异内容：WINDING = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathFillType；  API声明：EVEN\_ODD = 1  差异内容：EVEN\_ODD = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathFillType；  API声明：INVERSE\_WINDING = 2  差异内容：INVERSE\_WINDING = 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathFillType；  API声明：INVERSE\_EVEN\_ODD = 3  差异内容：INVERSE\_EVEN\_ODD = 3 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum PathMeasureMatrixFlags  差异内容： enum PathMeasureMatrixFlags | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathMeasureMatrixFlags；  API声明：GET\_POSITION\_MATRIX = 0  差异内容：GET\_POSITION\_MATRIX = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathMeasureMatrixFlags；  API声明：GET\_TANGENT\_MATRIX = 1  差异内容：GET\_TANGENT\_MATRIX = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathMeasureMatrixFlags；  API声明：GET\_POSITION\_AND\_TANGENT\_MATRIX = 2  差异内容：GET\_POSITION\_AND\_TANGENT\_MATRIX = 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： class RoundRect  差异内容： class RoundRect | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：RoundRect；  API声明：setCorner(pos: CornerPos, x: number, y: number): void;  差异内容：setCorner(pos: CornerPos, x: number, y: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：RoundRect；  API声明：getCorner(pos: CornerPos): common2D.Point;  差异内容：getCorner(pos: CornerPos): common2D.Point; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：RoundRect；  API声明：offset(dx: number, dy: number): void;  差异内容：offset(dx: number, dy: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum PathOp  差异内容： enum PathOp | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathOp；  API声明：DIFFERENCE = 0  差异内容：DIFFERENCE = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathOp；  API声明：INTERSECT = 1  差异内容：INTERSECT = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathOp；  API声明：UNION = 2  差异内容：UNION = 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathOp；  API声明：XOR = 3  差异内容：XOR = 3 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PathOp；  API声明：REVERSE\_DIFFERENCE = 4  差异内容：REVERSE\_DIFFERENCE = 4 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：conicTo(ctrlX: number, ctrlY: number, endX: number, endY: number, weight: number): void;  差异内容：conicTo(ctrlX: number, ctrlY: number, endX: number, endY: number, weight: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：rMoveTo(dx: number, dy: number): void;  差异内容：rMoveTo(dx: number, dy: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：rLineTo(dx: number, dy: number): void;  差异内容：rLineTo(dx: number, dy: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：rQuadTo(dx1: number, dy1: number, dx2: number, dy2: number): void;  差异内容：rQuadTo(dx1: number, dy1: number, dx2: number, dy2: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：rConicTo(ctrlX: number, ctrlY: number, endX: number, endY: number, weight: number): void;  差异内容：rConicTo(ctrlX: number, ctrlY: number, endX: number, endY: number, weight: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：rCubicTo(ctrlX1: number, ctrlY1: number, ctrlX2: number, ctrlY2: number, endX: number, endY: number): void;  差异内容：rCubicTo(ctrlX1: number, ctrlY1: number, ctrlX2: number, ctrlY2: number, endX: number, endY: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：addPolygon(points: Array<common2D.Point>, close: boolean): void;  差异内容：addPolygon(points: Array<common2D.Point>, close: boolean): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：op(path: Path, pathOp: PathOp): boolean;  差异内容：op(path: Path, pathOp: PathOp): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：addArc(rect: common2D.Rect, startAngle: number, sweepAngle: number): void;  差异内容：addArc(rect: common2D.Rect, startAngle: number, sweepAngle: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：addCircle(x: number, y: number, radius: number, pathDirection?: PathDirection): void;  差异内容：addCircle(x: number, y: number, radius: number, pathDirection?: PathDirection): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：addOval(rect: common2D.Rect, start: number, pathDirection?: PathDirection): void;  差异内容：addOval(rect: common2D.Rect, start: number, pathDirection?: PathDirection): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：addRect(rect: common2D.Rect, pathDirection?: PathDirection): void;  差异内容：addRect(rect: common2D.Rect, pathDirection?: PathDirection): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：addRoundRect(roundRect: RoundRect, pathDirection?: PathDirection): void;  差异内容：addRoundRect(roundRect: RoundRect, pathDirection?: PathDirection): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：addPath(path: Path, matrix?: Matrix | null): void;  差异内容：addPath(path: Path, matrix?: Matrix | null): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：transform(matrix: Matrix): void;  差异内容：transform(matrix: Matrix): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：contains(x: number, y: number): boolean;  差异内容：contains(x: number, y: number): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：setFillType(pathFillType: PathFillType): void;  差异内容：setFillType(pathFillType: PathFillType): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：getBounds(): common2D.Rect;  差异内容：getBounds(): common2D.Rect; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：offset(dx: number, dy: number): Path;  差异内容：offset(dx: number, dy: number): Path; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：getPositionAndTangent(forceClosed: boolean, distance: number, position: common2D.Point, tangent: common2D.Point): boolean;  差异内容：getPositionAndTangent(forceClosed: boolean, distance: number, position: common2D.Point, tangent: common2D.Point): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：isClosed(): boolean;  差异内容：isClosed(): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：getMatrix(forceClosed: boolean, distance: number, matrix: Matrix, flags: PathMeasureMatrixFlags): boolean;  差异内容：getMatrix(forceClosed: boolean, distance: number, matrix: Matrix, flags: PathMeasureMatrixFlags): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：buildFromSvgString(str: string): boolean;  差异内容：buildFromSvgString(str: string): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum PointMode  差异内容： enum PointMode | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PointMode；  API声明：POINTS = 0  差异内容：POINTS = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PointMode；  API声明：LINES = 1  差异内容：LINES = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PointMode；  API声明：POLYGON = 2  差异内容：POLYGON = 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum ShadowFlag  差异内容： enum ShadowFlag | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ShadowFlag；  API声明：NONE = 0  差异内容：NONE = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ShadowFlag；  API声明：TRANSPARENT\_OCCLUDER = 1  差异内容：TRANSPARENT\_OCCLUDER = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ShadowFlag；  API声明：GEOMETRIC\_ONLY = 2  差异内容：GEOMETRIC\_ONLY = 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ShadowFlag；  API声明：ALL = 3  差异内容：ALL = 3 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawRoundRect(roundRect: RoundRect): void;  差异内容：drawRoundRect(roundRect: RoundRect): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawNestedRoundRect(outer: RoundRect, inner: RoundRect): void;  差异内容：drawNestedRoundRect(outer: RoundRect, inner: RoundRect): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawBackground(brush: Brush): void;  差异内容：drawBackground(brush: Brush): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawShadow(path: Path, planeParams: common2D.Point3d, devLightPos: common2D.Point3d, lightRadius: number, ambientColor: common2D.Color, spotColor: common2D.Color, flag: ShadowFlag): void;  差异内容：drawShadow(path: Path, planeParams: common2D.Point3d, devLightPos: common2D.Point3d, lightRadius: number, ambientColor: common2D.Color, spotColor: common2D.Color, flag: ShadowFlag): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawImageRect(pixelmap: image.PixelMap, dstRect: common2D.Rect, samplingOptions?: SamplingOptions): void;  差异内容：drawImageRect(pixelmap: image.PixelMap, dstRect: common2D.Rect, samplingOptions?: SamplingOptions): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawImageRectWithSrc(pixelmap: image.PixelMap, srcRect: common2D.Rect, dstRect: common2D.Rect, samplingOptions?: SamplingOptions, constraint?: SrcRectConstraint): void;  差异内容：drawImageRectWithSrc(pixelmap: image.PixelMap, srcRect: common2D.Rect, dstRect: common2D.Rect, samplingOptions?: SamplingOptions, constraint?: SrcRectConstraint): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawOval(oval: common2D.Rect): void;  差异内容：drawOval(oval: common2D.Rect): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawArc(arc: common2D.Rect, startAngle: number, sweepAngle: number): void;  差异内容：drawArc(arc: common2D.Rect, startAngle: number, sweepAngle: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawPoints(points: Array<common2D.Point>, mode?: PointMode): void;  差异内容：drawPoints(points: Array<common2D.Point>, mode?: PointMode): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawSingleCharacter(text: string, font: Font, x: number, y: number): void;  差异内容：drawSingleCharacter(text: string, font: Font, x: number, y: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：clear(color: common2D.Color): void;  差异内容：clear(color: common2D.Color): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：getWidth(): number;  差异内容：getWidth(): number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：getHeight(): number;  差异内容：getHeight(): number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：getLocalClipBounds(): common2D.Rect;  差异内容：getLocalClipBounds(): common2D.Rect; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：getTotalMatrix(): Matrix;  差异内容：getTotalMatrix(): Matrix; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：concatMatrix(matrix: Matrix): void;  差异内容：concatMatrix(matrix: Matrix): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：clipRegion(region: Region, clipOp?: ClipOp): void;  差异内容：clipRegion(region: Region, clipOp?: ClipOp): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：clipRoundRect(roundRect: RoundRect, clipOp?: ClipOp, doAntiAlias?: boolean): void;  差异内容：clipRoundRect(roundRect: RoundRect, clipOp?: ClipOp, doAntiAlias?: boolean): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：isClipEmpty(): boolean;  差异内容：isClipEmpty(): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：setMatrix(matrix: Matrix): void;  差异内容：setMatrix(matrix: Matrix): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：resetMatrix(): void;  差异内容：resetMatrix(): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：TextBlob；  API声明：static makeFromPosText(text: string, len: number, points: common2D.Point[], font: Font): TextBlob;  差异内容：static makeFromPosText(text: string, len: number, points: common2D.Point[], font: Font): TextBlob; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：TextBlob；  API声明：uniqueID(): number;  差异内容：uniqueID(): number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum FontEdging  差异内容： enum FontEdging | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontEdging；  API声明：ALIAS = 0  差异内容：ALIAS = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontEdging；  API声明：ANTI\_ALIAS = 1  差异内容：ANTI\_ALIAS = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontEdging；  API声明：SUBPIXEL\_ANTI\_ALIAS = 2  差异内容：SUBPIXEL\_ANTI\_ALIAS = 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum FontHinting  差异内容： enum FontHinting | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontHinting；  API声明：NONE = 0  差异内容：NONE = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontHinting；  API声明：SLIGHT = 1  差异内容：SLIGHT = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontHinting；  API声明：NORMAL = 2  差异内容：NORMAL = 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontHinting；  API声明：FULL = 3  差异内容：FULL = 3 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：measureSingleCharacter(text: string): number;  差异内容：measureSingleCharacter(text: string): number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：setEdging(edging: FontEdging): void;  差异内容：setEdging(edging: FontEdging): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：setHinting(hinting: FontHinting): void;  差异内容：setHinting(hinting: FontHinting): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：countText(text: string): number;  差异内容：countText(text: string): number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：setBaselineSnap(isBaselineSnap: boolean): void;  差异内容：setBaselineSnap(isBaselineSnap: boolean): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：isBaselineSnap(): boolean;  差异内容：isBaselineSnap(): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：setEmbeddedBitmaps(isEmbeddedBitmaps: boolean): void;  差异内容：setEmbeddedBitmaps(isEmbeddedBitmaps: boolean): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：isEmbeddedBitmaps(): boolean;  差异内容：isEmbeddedBitmaps(): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：setForceAutoHinting(isForceAutoHinting: boolean): void;  差异内容：setForceAutoHinting(isForceAutoHinting: boolean): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：isForceAutoHinting(): boolean;  差异内容：isForceAutoHinting(): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：getWidths(glyphs: Array<number>): Array<number>;  差异内容：getWidths(glyphs: Array<number>): Array<number>; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：textToGlyphs(text: string, glyphCount?: number): Array<number>;  差异内容：textToGlyphs(text: string, glyphCount?: number): Array<number>; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：isSubpixel(): boolean;  差异内容：isSubpixel(): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：isLinearMetrics(): boolean;  差异内容：isLinearMetrics(): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：getSkewX(): number;  差异内容：getSkewX(): number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：isEmbolden(): boolean;  差异内容：isEmbolden(): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：getScaleX(): number;  差异内容：getScaleX(): number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：getHinting(): FontHinting;  差异内容：getHinting(): FontHinting; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：getEdging(): FontEdging;  差异内容：getEdging(): FontEdging; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： class Lattice  差异内容： class Lattice | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Lattice；  API声明：static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number, fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<common2D.Color> | null): Lattice;  差异内容：static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number, fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<common2D.Color> | null): Lattice; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum RectType  差异内容： enum RectType | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：RectType；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：RectType；  API声明：TRANSPARENT = 1  差异内容：TRANSPARENT = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：RectType；  API声明：FIXEDCOLOR = 2  差异内容：FIXEDCOLOR = 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： class ShaderEffect  差异内容： class ShaderEffect | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ShaderEffect；  API声明：static createColorShader(color: number): ShaderEffect;  差异内容：static createColorShader(color: number): ShaderEffect; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ShaderEffect；  API声明：static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<number>, mode: TileMode, pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect;  差异内容：static createLinearGradient(startPt: common2D.Point, endPt: common2D.Point, colors: Array<number>, mode: TileMode, pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ShaderEffect；  API声明：static createRadialGradient(centerPt: common2D.Point, radius: number, colors: Array<number>, mode: TileMode, pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect;  差异内容：static createRadialGradient(centerPt: common2D.Point, radius: number, colors: Array<number>, mode: TileMode, pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ShaderEffect；  API声明：static createSweepGradient(centerPt: common2D.Point, colors: Array<number>, mode: TileMode, startAngle: number, endAngle: number, pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect;  差异内容：static createSweepGradient(centerPt: common2D.Point, colors: Array<number>, mode: TileMode, startAngle: number, endAngle: number, pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ShaderEffect；  API声明：static createConicalGradient(startPt: common2D.Point, startRadius: number, endPt: common2D.Point, endRadius: number, colors: Array<number>, mode: TileMode, pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect;  差异内容：static createConicalGradient(startPt: common2D.Point, startRadius: number, endPt: common2D.Point, endRadius: number, colors: Array<number>, mode: TileMode, pos?: Array<number> | null, matrix?: Matrix | null): ShaderEffect; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum TileMode  差异内容： enum TileMode | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：TileMode；  API声明：CLAMP = 0  差异内容：CLAMP = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：TileMode；  API声明：REPEAT = 1  差异内容：REPEAT = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：TileMode；  API声明：MIRROR = 2  差异内容：MIRROR = 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：TileMode；  API声明：DECAL = 3  差异内容：DECAL = 3 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ColorFilter；  API声明：static createMatrixColorFilter(matrix: Array<number>): ColorFilter;  差异内容：static createMatrixColorFilter(matrix: Array<number>): ColorFilter; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： class ImageFilter  差异内容： class ImageFilter | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ImageFilter；  API声明：static createBlurImageFilter(sigmaX: number, sigmaY: number, tileMode: TileMode, imageFilter?: ImageFilter | null): ImageFilter;  差异内容：static createBlurImageFilter(sigmaX: number, sigmaY: number, tileMode: TileMode, imageFilter?: ImageFilter | null): ImageFilter; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ImageFilter；  API声明：static createFromColorFilter(colorFilter: ColorFilter, imageFilter?: ImageFilter | null): ImageFilter;  差异内容：static createFromColorFilter(colorFilter: ColorFilter, imageFilter?: ImageFilter | null): ImageFilter; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：setMiterLimit(miter: number): void;  差异内容：setMiterLimit(miter: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：getMiterLimit(): number;  差异内容：getMiterLimit(): number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：setShaderEffect(shaderEffect: ShaderEffect): void;  差异内容：setShaderEffect(shaderEffect: ShaderEffect): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：getColor(): common2D.Color;  差异内容：getColor(): common2D.Color; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：getWidth(): number;  差异内容：getWidth(): number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：isAntiAlias(): boolean;  差异内容：isAntiAlias(): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：getAlpha(): number;  差异内容：getAlpha(): number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：getColorFilter(): ColorFilter;  差异内容：getColorFilter(): ColorFilter; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：setImageFilter(filter: ImageFilter | null): void;  差异内容：setImageFilter(filter: ImageFilter | null): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：reset(): void;  差异内容：reset(): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Pen；  API声明：getFillPath(src: Path, dst: Path): boolean;  差异内容：getFillPath(src: Path, dst: Path): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Brush；  API声明：getColor(): common2D.Color;  差异内容：getColor(): common2D.Color; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Brush；  API声明：isAntiAlias(): boolean;  差异内容：isAntiAlias(): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Brush；  API声明：getAlpha(): number;  差异内容：getAlpha(): number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Brush；  API声明：getColorFilter(): ColorFilter;  差异内容：getColorFilter(): ColorFilter; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Brush；  API声明：setImageFilter(filter: ImageFilter | null): void;  差异内容：setImageFilter(filter: ImageFilter | null): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Brush；  API声明：setShaderEffect(shaderEffect: ShaderEffect): void;  差异内容：setShaderEffect(shaderEffect: ShaderEffect): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Brush；  API声明：reset(): void;  差异内容：reset(): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： class Matrix  差异内容： class Matrix | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：setRotation(degree: number, px: number, py: number): void;  差异内容：setRotation(degree: number, px: number, py: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：setScale(sx: number, sy: number, px: number, py: number): void;  差异内容：setScale(sx: number, sy: number, px: number, py: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：setTranslation(dx: number, dy: number): void;  差异内容：setTranslation(dx: number, dy: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：setMatrix(values: Array<number>): void;  差异内容：setMatrix(values: Array<number>): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：preConcat(matrix: Matrix): void;  差异内容：preConcat(matrix: Matrix): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：isEqual(matrix: Matrix): Boolean;  差异内容：isEqual(matrix: Matrix): Boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：invert(matrix: Matrix): Boolean;  差异内容：invert(matrix: Matrix): Boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：isIdentity(): Boolean;  差异内容：isIdentity(): Boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：getValue(index: number): number;  差异内容：getValue(index: number): number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：postRotate(degree: number, px: number, py: number): void;  差异内容：postRotate(degree: number, px: number, py: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：postScale(sx: number, sy: number, px: number, py: number): void;  差异内容：postScale(sx: number, sy: number, px: number, py: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：postTranslate(dx: number, dy: number): void;  差异内容：postTranslate(dx: number, dy: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：preRotate(degree: number, px: number, py: number): void;  差异内容：preRotate(degree: number, px: number, py: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：preScale(sx: number, sy: number, px: number, py: number): void;  差异内容：preScale(sx: number, sy: number, px: number, py: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：preTranslate(dx: number, dy: number): void;  差异内容：preTranslate(dx: number, dy: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：reset(): void;  差异内容：reset(): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：mapPoints(src: Array<common2D.Point>): Array<common2D.Point>;  差异内容：mapPoints(src: Array<common2D.Point>): Array<common2D.Point>; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：getAll(): Array<number>;  差异内容：getAll(): Array<number>; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：mapRect(dst: common2D.Rect, src: common2D.Rect): boolean;  差异内容：mapRect(dst: common2D.Rect, src: common2D.Rect): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：setRectToRect(src: common2D.Rect, dst: common2D.Rect, scaleToFit: ScaleToFit): boolean;  差异内容：setRectToRect(src: common2D.Rect, dst: common2D.Rect, scaleToFit: ScaleToFit): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Matrix；  API声明：setPolyToPoly(src: Array<common2D.Point>, dst: Array<common2D.Point>, count: number): boolean;  差异内容：setPolyToPoly(src: Array<common2D.Point>, dst: Array<common2D.Point>, count: number): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum ScaleToFit  差异内容： enum ScaleToFit | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ScaleToFit；  API声明：FILL\_SCALE\_TO\_FIT = 0  差异内容：FILL\_SCALE\_TO\_FIT = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ScaleToFit；  API声明：START\_SCALE\_TO\_FIT = 1  差异内容：START\_SCALE\_TO\_FIT = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ScaleToFit；  API声明：CENTER\_SCALE\_TO\_FIT = 2  差异内容：CENTER\_SCALE\_TO\_FIT = 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：ScaleToFit；  API声明：END\_SCALE\_TO\_FIT = 3  差异内容：END\_SCALE\_TO\_FIT = 3 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum CornerPos  差异内容： enum CornerPos | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：CornerPos；  API声明：TOP\_LEFT\_POS = 0  差异内容：TOP\_LEFT\_POS = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：CornerPos；  API声明：TOP\_RIGHT\_POS = 1  差异内容：TOP\_RIGHT\_POS = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：CornerPos；  API声明：BOTTOM\_RIGHT\_POS = 2  差异内容：BOTTOM\_RIGHT\_POS = 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：CornerPos；  API声明：BOTTOM\_LEFT\_POS = 3  差异内容：BOTTOM\_LEFT\_POS = 3 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明： enum SrcRectConstraint  差异内容： enum SrcRectConstraint | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：SrcRectConstraint；  API声明：STRICT = 0  差异内容：STRICT = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：SrcRectConstraint；  API声明：FAST = 1  差异内容：FAST = 1 | api/@ohos.graphics.drawing.d.ts |
