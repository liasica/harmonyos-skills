---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics2d-6111
title: ArkGraphics 2D
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > ArkGraphics 2D
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:5a6a92594913f4372cc92780dd23cb2e6d85f3dacfe54f44122bb7277ec7f2b2
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：EllipsisMode；  API声明：MULTILINE\_START  差异内容：MULTILINE\_START | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：EllipsisMode；  API声明：MULTILINE\_MIDDLE  差异内容：MULTILINE\_MIDDLE | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontVariation；  API声明：isNormalized?: boolean;  差异内容：isNormalized?: boolean; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：fontEdging?: drawing.FontEdging;  差异内容：fontEdging?: drawing.FontEdging; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明：interface FontVariationAxis  差异内容：interface FontVariationAxis | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontVariationAxis；  API声明：key: string;  差异内容：key: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontVariationAxis；  API声明：minValue: number;  差异内容：minValue: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontVariationAxis；  API声明：maxValue: number;  差异内容：maxValue: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontVariationAxis；  API声明：defaultValue: number;  差异内容：defaultValue: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontVariationAxis；  API声明：flags: number;  差异内容：flags: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontVariationAxis；  API声明：name: string;  差异内容：name: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontVariationAxis；  API声明：localName: string;  差异内容：localName: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明：interface FontVariationInstance  差异内容：interface FontVariationInstance | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontVariationInstance；  API声明：name: string;  差异内容：name: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontVariationInstance；  API声明：localName: string;  差异内容：localName: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontVariationInstance；  API声明：coordinates: Array<FontVariation>;  差异内容：coordinates: Array<FontVariation>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：variationAxisRecords?: Array<FontVariationAxis>;  差异内容：variationAxisRecords?: Array<FontVariationAxis>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：variationInstanceRecords?: Array<FontVariationInstance>;  差异内容：variationInstanceRecords?: Array<FontVariationInstance>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：layoutWithConstraints(size: TextRectSize): TextLayoutResult;  差异内容：layoutWithConstraints(size: TextRectSize): TextLayoutResult; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getCharacterRangeForGlyphRange(glyphRange: Range, encoding: drawing.TextEncoding): Array<Range>;  差异内容：getCharacterRangeForGlyphRange(glyphRange: Range, encoding: drawing.TextEncoding): Array<Range>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getGlyphRangeForCharacterRange(characterRange: Range, encoding: drawing.TextEncoding): Array<Range>;  差异内容：getGlyphRangeForCharacterRange(characterRange: Range, encoding: drawing.TextEncoding): Array<Range>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：getCharacterPositionAtCoordinate(x: number, y: number, encoding: drawing.TextEncoding): PositionWithAffinity;  差异内容：getCharacterPositionAtCoordinate(x: number, y: number, encoding: drawing.TextEncoding): PositionWithAffinity; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明：interface TextRectSize  差异内容：interface TextRectSize | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextRectSize；  API声明：width: number;  差异内容：width: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextRectSize；  API声明：height: number;  差异内容：height: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明：interface TextLayoutResult  差异内容：interface TextLayoutResult | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextLayoutResult；  API声明：fitStrRange: Array<Range>;  差异内容：fitStrRange: Array<Range>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextLayoutResult；  API声明：correctRect: TextRectSize;  差异内容：correctRect: TextRectSize; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：HDRFormat；  API声明：VIDEO\_AIHDR = 8  差异内容：VIDEO\_AIHDR = 8 | api/@ohos.graphics.hdrCapability.d.ts |
| 新增API | NA | 类名：Filter；  API声明：hdrBrightnessRatio(ratio: number): Filter;  差异内容：hdrBrightnessRatio(ratio: number): Filter; | api/@ohos.graphics.uiEffect.d.ts |
