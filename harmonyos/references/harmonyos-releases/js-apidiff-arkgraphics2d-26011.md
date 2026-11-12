---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics2d-26011
title: ArkGraphics 2D
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > ArkGraphics 2D
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:53+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:205d1538b7271bc400dd0b989f8c724cde2b525835da72a0a94601101c4ccc3e
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API卡片权限变更 | 类名：text；  API声明：interface FontVariation  差异内容：NA | 类名：text；  API声明：interface FontVariation  差异内容：form | api/@ohos.graphics.text.d.ts |
| API卡片权限变更 | 类名：FontVariation；  API声明：axis: string;  差异内容：NA | 类名：FontVariation；  API声明：axis: string;  差异内容：form | api/@ohos.graphics.text.d.ts |
| API卡片权限变更 | 类名：FontVariation；  API声明：value: number;  差异内容：NA | 类名：FontVariation；  API声明：value: number;  差异内容：form | api/@ohos.graphics.text.d.ts |
| API卡片权限变更 | 类名：FontVariation；  API声明：isNormalized?: boolean;  差异内容：NA | 类名：FontVariation；  API声明：isNormalized?: boolean;  差异内容：form | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：drawing；  API声明：interface RecordCmd  差异内容：interface RecordCmd | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明：class RecordCmdUtils  差异内容：class RecordCmdUtils | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：RecordCmdUtils；  API声明：beginRecording(width: number, height: number): Canvas;  差异内容：beginRecording(width: number, height: number): Canvas; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：RecordCmdUtils；  API声明：finishRecording(): RecordCmd;  差异内容：finishRecording(): RecordCmd; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：RecordCmdUtils；  API声明：getHeight(): number;  差异内容：getHeight(): number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：RecordCmdUtils；  API声明：getWidth(): number;  差异内容：getWidth(): number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawRecordCmd(recordCmd: RecordCmd): void;  差异内容：drawRecordCmd(recordCmd: RecordCmd): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：TextBlob；  API声明：static makeFromStringWithFallback(text: string, font: Font): Array<TextBlob>;  差异内容：static makeFromStringWithFallback(text: string, font: Font): Array<TextBlob>; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：TextBlob；  API声明：static makeFromPosTextWithFallback(text: string, len: number, points: common2D.Point[], font: Font): Array<TextBlob>;  差异内容：static makeFromPosTextWithFallback(text: string, len: number, points: common2D.Point[], font: Font): Array<TextBlob>; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明：interface TypefaceFallbackInfo  差异内容：interface TypefaceFallbackInfo | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：TypefaceFallbackInfo；  API声明：typeface: Typeface;  差异内容：typeface: Typeface; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：TypefaceFallbackInfo；  API声明：glyphIds: Array<number>;  差异内容：glyphIds: Array<number>; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：measureTextWithFallback(text: string, encoding: TextEncoding): number;  差异内容：measureTextWithFallback(text: string, encoding: TextEncoding): number; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Font；  API声明：textToGlyphsWithFallback(text: string, glyphCount?: number): Array<TypefaceFallbackInfo>;  差异内容：textToGlyphsWithFallback(text: string, glyphCount?: number): Array<TypefaceFallbackInfo>; | api/@ohos.graphics.drawing.d.ts |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：declare namespace displaySync  差异内容：NA | 类名：global；  API声明：declare namespace displaySync  差异内容：atomicservice | api/@ohos.graphics.displaySync.d.ts |
| API从不支持元服务到支持元服务 | 类名：displaySync；  API声明：interface IntervalInfo  差异内容：NA | 类名：displaySync；  API声明：interface IntervalInfo  差异内容：atomicservice | api/@ohos.graphics.displaySync.d.ts |
| API从不支持元服务到支持元服务 | 类名：IntervalInfo；  API声明：timestamp: number;  差异内容：NA | 类名：IntervalInfo；  API声明：timestamp: number;  差异内容：atomicservice | api/@ohos.graphics.displaySync.d.ts |
| API从不支持元服务到支持元服务 | 类名：IntervalInfo；  API声明：targetTimestamp: number;  差异内容：NA | 类名：IntervalInfo；  API声明：targetTimestamp: number;  差异内容：atomicservice | api/@ohos.graphics.displaySync.d.ts |
| API从不支持元服务到支持元服务 | 类名：displaySync；  API声明：interface DisplaySync  差异内容：NA | 类名：displaySync；  API声明：interface DisplaySync  差异内容：atomicservice | api/@ohos.graphics.displaySync.d.ts |
| API从不支持元服务到支持元服务 | 类名：DisplaySync；  API声明：setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange): void;  差异内容：NA | 类名：DisplaySync；  API声明：setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange): void;  差异内容：atomicservice | api/@ohos.graphics.displaySync.d.ts |
| API从不支持元服务到支持元服务 | 类名：DisplaySync；  API声明：on(type: 'frame', callback: Callback<IntervalInfo>): void;  差异内容：NA | 类名：DisplaySync；  API声明：on(type: 'frame', callback: Callback<IntervalInfo>): void;  差异内容：atomicservice | api/@ohos.graphics.displaySync.d.ts |
| API从不支持元服务到支持元服务 | 类名：DisplaySync；  API声明：off(type: 'frame', callback?: Callback<IntervalInfo>): void;  差异内容：NA | 类名：DisplaySync；  API声明：off(type: 'frame', callback?: Callback<IntervalInfo>): void;  差异内容：atomicservice | api/@ohos.graphics.displaySync.d.ts |
| API从不支持元服务到支持元服务 | 类名：DisplaySync；  API声明：start(): void;  差异内容：NA | 类名：DisplaySync；  API声明：start(): void;  差异内容：atomicservice | api/@ohos.graphics.displaySync.d.ts |
| API从不支持元服务到支持元服务 | 类名：DisplaySync；  API声明：stop(): void;  差异内容：NA | 类名：DisplaySync；  API声明：stop(): void;  差异内容：atomicservice | api/@ohos.graphics.displaySync.d.ts |
| API从不支持元服务到支持元服务 | 类名：displaySync；  API声明：function create(): DisplaySync;  差异内容：NA | 类名：displaySync；  API声明：function create(): DisplaySync;  差异内容：atomicservice | api/@ohos.graphics.displaySync.d.ts |
