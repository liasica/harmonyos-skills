---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics2d-5111
title: ArkGraphics 2D
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > ArkGraphics 2D
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:50+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d58dddb9b5d5f31bd10766c6af5eb7a70f60a3f64dbb85362d87a2ad73abdbb1
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：Path；  API声明：getSegment(forceClosed: boolean, start: number, stop: number, startWithMoveTo: boolean, dst: Path): boolean;  差异内容：401 | 类名：Path；  API声明：getSegment(forceClosed: boolean, start: number, stop: number, startWithMoveTo: boolean, dst: Path): boolean;  差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：Canvas；  API声明：drawArcWithCenter(arc: common2D.Rect, startAngle: number, sweepAngle: number, useCenter: boolean): void;  差异内容：401 | 类名：Canvas；  API声明：drawArcWithCenter(arc: common2D.Rect, startAngle: number, sweepAngle: number, useCenter: boolean): void;  差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：Canvas；  API声明：clear(color: common2D.Color | number): void;  差异内容：401 | 类名：Canvas；  API声明：clear(color: common2D.Color | number): void;  差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：Canvas；  API声明：quickRejectPath(path: Path): boolean;  差异内容：401 | 类名：Canvas；  API声明：quickRejectPath(path: Path): boolean;  差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：Canvas；  API声明：quickRejectRect(rect: common2D.Rect): boolean;  差异内容：401 | 类名：Canvas；  API声明：quickRejectRect(rect: common2D.Rect): boolean;  差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：Typeface；  API声明：static makeFromRawFile(rawfile: Resource): Typeface;  差异内容：401 | 类名：Typeface；  API声明：static makeFromRawFile(rawfile: Resource): Typeface;  差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：Font；  API声明：createPathForGlyph(index: number): Path;  差异内容：401 | 类名：Font；  API声明：createPathForGlyph(index: number): Path;  差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：Font；  API声明：getBounds(glyphs: Array<number>): Array<common2D.Rect>;  差异内容：401 | 类名：Font；  API声明：getBounds(glyphs: Array<number>): Array<common2D.Rect>;  差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：PathEffect；  API声明：static createDiscretePathEffect(segLength: number, dev: number, seedAssist?: number): PathEffect;  差异内容：401 | 类名：PathEffect；  API声明：static createDiscretePathEffect(segLength: number, dev: number, seedAssist?: number): PathEffect;  差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：PathEffect；  API声明：static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect;  差异内容：401 | 类名：PathEffect；  API声明：static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect;  差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：PathEffect；  API声明：static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect;  差异内容：401 | 类名：PathEffect；  API声明：static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect;  差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：Pen；  API声明：setColor(color: number): void;  差异内容：401 | 类名：Pen；  API声明：setColor(color: number): void;  差异内容：NA | api/@ohos.graphics.drawing.d.ts |
| 删除错误码 | 类名：TextLine；  API声明：createTruncatedLine(width: number, ellipsisMode: EllipsisMode, ellipsis: string): TextLine;  差异内容：401 | 类名：TextLine；  API声明：createTruncatedLine(width: number, ellipsisMode: EllipsisMode, ellipsis: string): TextLine;  差异内容：NA | api/@ohos.graphics.text.d.ts |
| 删除错误码 | 类名：TextLine；  API声明：getStringIndexForPosition(point: common2D.Point): number;  差异内容：401 | 类名：TextLine；  API声明：getStringIndexForPosition(point: common2D.Point): number;  差异内容：NA | api/@ohos.graphics.text.d.ts |
| 删除错误码 | 类名：TextLine；  API声明：getOffsetForStringIndex(index: number): number;  差异内容：401 | 类名：TextLine；  API声明：getOffsetForStringIndex(index: number): number;  差异内容：NA | api/@ohos.graphics.text.d.ts |
| 删除错误码 | 类名：TextLine；  API声明：enumerateCaretOffsets(callback: CaretOffsetsCallback): void;  差异内容：401 | 类名：TextLine；  API声明：enumerateCaretOffsets(callback: CaretOffsetsCallback): void;  差异内容：NA | api/@ohos.graphics.text.d.ts |
| 删除错误码 | 类名：TextLine；  API声明：getAlignmentOffset(alignmentFactor: number, alignmentWidth: number): number;  差异内容：401 | 类名：TextLine；  API声明：getAlignmentOffset(alignmentFactor: number, alignmentWidth: number): number;  差异内容：NA | api/@ohos.graphics.text.d.ts |
| 删除错误码 | 类名：Run；  API声明：getGlyphs(range: Range): Array<number>;  差异内容：401 | 类名：Run；  API声明：getGlyphs(range: Range): Array<number>;  差异内容：NA | api/@ohos.graphics.text.d.ts |
| 删除错误码 | 类名：Run；  API声明：getPositions(range: Range): Array<common2D.Point>;  差异内容：401 | 类名：Run；  API声明：getPositions(range: Range): Array<common2D.Point>;  差异内容：NA | api/@ohos.graphics.text.d.ts |
| 删除错误码 | 类名：Run；  API声明：getStringIndices(range?: Range): Array<number>;  差异内容：401 | 类名：Run；  API声明：getStringIndices(range?: Range): Array<number>;  差异内容：NA | api/@ohos.graphics.text.d.ts |
