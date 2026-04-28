---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics2d-6002
title: ArkGraphics 2D
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > ArkGraphics 2D
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:26+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:c677bf7fa065c3bbf6ae151ee1fe0dcd41a25c9b668f8c582deb60da913b73cd
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：common2D；  API声明：interface Color4f  差异内容：interface Color4f | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：Color4f；  API声明：alpha: number;  差异内容：alpha: number; | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：Color4f；  API声明：red: number;  差异内容：red: number; | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：Color4f；  API声明：green: number;  差异内容：green: number; | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：Color4f；  API声明：blue: number;  差异内容：blue: number; | api/@ohos.graphics.common2D.d.ts |
| 新增API | NA | 类名：text；  API声明：enum TextVerticalAlign  差异内容：enum TextVerticalAlign | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextVerticalAlign；  API声明：BASELINE = 0  差异内容：BASELINE = 0 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextVerticalAlign；  API声明：BOTTOM = 1  差异内容：BOTTOM = 1 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextVerticalAlign；  API声明：CENTER = 2  差异内容：CENTER = 2 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextVerticalAlign；  API声明：TOP = 3  差异内容：TOP = 3 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：PlaceholderAlignment；  API声明：FOLLOW\_PARAGRAPH  差异内容：FOLLOW\_PARAGRAPH | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明：enum TextUndefinedGlyphDisplay  差异内容：enum TextUndefinedGlyphDisplay | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextUndefinedGlyphDisplay；  API声明：USE\_DEFAULT  差异内容：USE\_DEFAULT | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextUndefinedGlyphDisplay；  API声明：USE\_TOFU  差异内容：USE\_TOFU | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明：function setTextUndefinedGlyphDisplay(noGlyphShow: TextUndefinedGlyphDisplay): void;  差异内容：function setTextUndefinedGlyphDisplay(noGlyphShow: TextUndefinedGlyphDisplay): void; | api/@ohos.graphics.text.d.ts |
| 删除API | 类名：uiEffect；  API声明：interface Color  差异内容：interface Color | NA | api/@ohos.graphics.uiEffect.d.ts |
| 删除API | 类名：Color；  API声明：red: number;  差异内容：red: number; | NA | api/@ohos.graphics.uiEffect.d.ts |
| 删除API | 类名：Color；  API声明：green: number;  差异内容：green: number; | NA | api/@ohos.graphics.uiEffect.d.ts |
| 删除API | 类名：Color；  API声明：blue: number;  差异内容：blue: number; | NA | api/@ohos.graphics.uiEffect.d.ts |
| 删除API | 类名：Color；  API声明：alpha: number;  差异内容：alpha: number; | NA | api/@ohos.graphics.uiEffect.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Path；  API声明：approximate(acceptableError: number): Array<number>;  差异内容：approximate(acceptableError: number): Array<number>; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Path；  API声明：interpolate(other: Path, weight: number, interpolatedPath: Path): boolean;  差异内容：interpolate(other: Path, weight: number, interpolatedPath: Path): boolean; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Path；  API声明：isInterpolate(other: Path): boolean;  差异内容：isInterpolate(other: Path): boolean; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Pen；  API声明：setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void;  差异内容：setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Pen；  API声明：getColor4f(): common2D.Color4f;  差异内容：getColor4f(): common2D.Color4f; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Brush；  API声明：setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void;  差异内容：setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Brush；  API声明：getColor4f(): common2D.Color4f;  差异内容：getColor4f(): common2D.Color4f; | api/@ohos.graphics.drawing.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：FontCollection；  API声明：unloadFontSync(name: string): void;  差异内容：unloadFontSync(name: string): void; | api/@ohos.graphics.text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：FontCollection；  API声明：unloadFont(name: string): Promise<void>;  差异内容：unloadFont(name: string): Promise<void>; | api/@ohos.graphics.text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Run；  API声明：getTextDirection(): TextDirection;  差异内容：getTextDirection(): TextDirection; | api/@ohos.graphics.text.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Run；  API声明：getAdvances(range: Range): Array<common2D.Point>;  差异内容：getAdvances(range: Range): Array<common2D.Point>; | api/@ohos.graphics.text.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ParagraphStyle；  API声明：verticalAlign?: TextVerticalAlign;  差异内容：verticalAlign?: TextVerticalAlign; | api/@ohos.graphics.text.d.ts |
