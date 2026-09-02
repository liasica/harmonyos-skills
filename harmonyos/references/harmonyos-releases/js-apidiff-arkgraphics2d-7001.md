---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics2d-7001
title: ArkGraphics 2D
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > ArkGraphics 2D
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:05+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:912d333def5e846a7e783dcfc80b4434a3c154f136d6f8d7b53fbb92d7cb70f7
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：ColorSpaceManager；  API声明：getColorSpaceName(): ColorSpace;  差异内容：NA | 类名：ColorSpaceManager；  API声明：getColorSpaceName(): ColorSpace;  差异内容：18600001 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增错误码 | 类名：ColorSpaceManager；  API声明：getWhitePoint(): Array<number>;  差异内容：NA | 类名：ColorSpaceManager；  API声明：getWhitePoint(): Array<number>;  差异内容：18600001 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增错误码 | 类名：ColorSpaceManager；  API声明：getGamma(): number;  差异内容：NA | 类名：ColorSpaceManager；  API声明：getGamma(): number;  差异内容：18600001 | api/@ohos.graphics.colorSpaceManager.d.ts |
| 新增错误码 | 类名：ColorSpaceManager；  API声明：getColorSpaceName(): colorSpaceManager.ColorSpace;  差异内容：NA | 类名：ColorSpaceManager；  API声明：getColorSpaceName(): colorSpaceManager.ColorSpace;  差异内容：18600001 | api/@ohos.graphics.sendableColorSpaceManager.d.ets |
| 新增错误码 | 类名：ColorSpaceManager；  API声明：getWhitePoint(): collections.Array<number>;  差异内容：NA | 类名：ColorSpaceManager；  API声明：getWhitePoint(): collections.Array<number>;  差异内容：18600001 | api/@ohos.graphics.sendableColorSpaceManager.d.ets |
| 新增错误码 | 类名：ColorSpaceManager；  API声明：getGamma(): number;  差异内容：NA | 类名：ColorSpaceManager；  API声明：getGamma(): number;  差异内容：18600001 | api/@ohos.graphics.sendableColorSpaceManager.d.ets |
| 新增API | NA | 类名：Path；  API声明：convertToSvgString(): string;  差异内容：convertToSvgString(): string; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：getPointData(): Array<common2D.Point>;  差异内容：getPointData(): Array<common2D.Point>; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：getVerbData(): Array<PathIteratorVerb>;  差异内容：getVerbData(): Array<PathIteratorVerb>; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：getConicWeightData(): Array<number>;  差异内容：getConicWeightData(): Array<number>; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：getLastPoint(): common2D.Point;  差异内容：getLastPoint(): common2D.Point; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：isEqual(path: Path): boolean;  差异内容：isEqual(path: Path): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawGlyphs(glyphIds: Array<number>, glyphIdOffset: number, positions: Array<common2D.Point>, positionOffset: number, glyphCount: number, font: Font): void;  差异内容：drawGlyphs(glyphIds: Array<number>, glyphIdOffset: number, positions: Array<common2D.Point>, positionOffset: number, glyphCount: number, font: Font): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：isOpaque(): boolean;  差异内容：isOpaque(): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：resetClip(): void;  差异内容：resetClip(): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明：class PointUtils  差异内容：class PointUtils | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PointUtils；  API声明：static negate(point: common2D.Point): void;  差异内容：static negate(point: common2D.Point): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：PointUtils；  API声明：static offset(point: common2D.Point, dx: number, dy: number): void;  差异内容：static offset(point: common2D.Point, dx: number, dy: number): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontCollection；  API声明：setParagraphCachesEnabled(enable: boolean): void;  差异内容：setParagraphCachesEnabled(enable: boolean): void; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：firstLineHeadIndent?: number;  差异内容：firstLineHeadIndent?: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：tailIndents?: Array<number>;  差异内容：tailIndents?: Array<number>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：headIndents?: Array<number>;  差异内容：headIndents?: Array<number>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：orphanCharOptimization?: boolean;  差异内容：orphanCharOptimization?: boolean; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getProcessState(): TextProcessState;  差异内容：getProcessState(): TextProcessState; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getTextDisplayState(): TextDisplayState;  差异内容：getTextDisplayState(): TextDisplayState; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getParagraphStyle(): ParagraphStyle;  差异内容：getParagraphStyle(): ParagraphStyle; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getVisibleTextRanges(): Array<Range>;  差异内容：getVisibleTextRanges(): Array<Range>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明：enum TextProcessState  差异内容：enum TextProcessState | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextProcessState；  API声明：INIT = 0  差异内容：INIT = 0 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextProcessState；  API声明：INDEXED = 1  差异内容：INDEXED = 1 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextProcessState；  API声明：SHAPED = 2  差异内容：SHAPED = 2 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextProcessState；  API声明：LINE\_BROKEN = 3  差异内容：LINE\_BROKEN = 3 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextProcessState；  API声明：FORMATTED = 4  差异内容：FORMATTED = 4 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextProcessState；  API声明：PAINT = 5  差异内容：PAINT = 5 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextProcessState；  API声明：UPDATE\_ATTRIBUTE = 6  差异内容：UPDATE\_ATTRIBUTE = 6 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明：enum TextDisplayState  差异内容：enum TextDisplayState | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextDisplayState；  API声明：UNKNOWN = 0  差异内容：UNKNOWN = 0 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextDisplayState；  API声明：ALL = 1  差异内容：ALL = 1 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextDisplayState；  API声明：CLIP = 2  差异内容：CLIP = 2 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextDisplayState；  API声明：OMITTED = 3  差异内容：OMITTED = 3 | api/@ohos.graphics.text.d.ts |
