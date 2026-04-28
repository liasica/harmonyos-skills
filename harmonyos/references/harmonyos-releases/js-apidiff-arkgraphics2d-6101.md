---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics2d-6101
title: ArkGraphics 2D
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > ArkGraphics 2D
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:38abffa146d4f40bdc807babcf9339e7d91d4becc48c08d73b293986f5946c7b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：ColorSpaceManager；  API声明：getColorSpaceName(): ColorSpace;  差异内容：18600001 | 类名：ColorSpaceManager；  API声明：getColorSpaceName(): ColorSpace;  差异内容：NA | api/@ohos.graphics.colorSpaceManager.d.ts |
| 删除错误码 | 类名：ColorSpaceManager；  API声明：getWhitePoint(): Array<number>;  差异内容：18600001 | 类名：ColorSpaceManager；  API声明：getWhitePoint(): Array<number>;  差异内容：NA | api/@ohos.graphics.colorSpaceManager.d.ts |
| 删除错误码 | 类名：ColorSpaceManager；  API声明：getGamma(): number;  差异内容：18600001 | 类名：ColorSpaceManager；  API声明：getGamma(): number;  差异内容：NA | api/@ohos.graphics.colorSpaceManager.d.ts |
| 删除错误码 | 类名：ColorSpaceManager；  API声明：getColorSpaceName(): colorSpaceManager.ColorSpace;  差异内容：18600001 | 类名：ColorSpaceManager；  API声明：getColorSpaceName(): colorSpaceManager.ColorSpace;  差异内容：NA | api/@ohos.graphics.sendableColorSpaceManager.d.ets |
| 删除错误码 | 类名：ColorSpaceManager；  API声明：getWhitePoint(): collections.Array<number>;  差异内容：18600001 | 类名：ColorSpaceManager；  API声明：getWhitePoint(): collections.Array<number>;  差异内容：NA | api/@ohos.graphics.sendableColorSpaceManager.d.ets |
| 删除错误码 | 类名：ColorSpaceManager；  API声明：getGamma(): number;  差异内容：18600001 | 类名：ColorSpaceManager；  API声明：getGamma(): number;  差异内容：NA | api/@ohos.graphics.sendableColorSpaceManager.d.ets |
| 函数变更 | 类名：Pen；  API声明：setShaderEffect(shaderEffect: ShaderEffect): void;  差异内容：shaderEffect: ShaderEffect | 类名：Pen；  API声明：setShaderEffect(shaderEffect: ShaderEffect | null): void;  差异内容：shaderEffect: ShaderEffect | null | api/@ohos.graphics.drawing.d.ts |
| 函数变更 | 类名：Pen；  API声明：setColorFilter(filter: ColorFilter): void;  差异内容：filter: ColorFilter | 类名：Pen；  API声明：setColorFilter(filter: ColorFilter | null): void;  差异内容：filter: ColorFilter | null | api/@ohos.graphics.drawing.d.ts |
| 函数变更 | 类名：Pen；  API声明：setMaskFilter(filter: MaskFilter): void;  差异内容：filter: MaskFilter | 类名：Pen；  API声明：setMaskFilter(filter: MaskFilter | null): void;  差异内容：filter: MaskFilter | null | api/@ohos.graphics.drawing.d.ts |
| 函数变更 | 类名：Pen；  API声明：setPathEffect(effect: PathEffect): void;  差异内容：effect: PathEffect | 类名：Pen；  API声明：setPathEffect(effect: PathEffect | null): void;  差异内容：effect: PathEffect | null | api/@ohos.graphics.drawing.d.ts |
| 函数变更 | 类名：Pen；  API声明：setShadowLayer(shadowLayer: ShadowLayer): void;  差异内容：shadowLayer: ShadowLayer | 类名：Pen；  API声明：setShadowLayer(shadowLayer: ShadowLayer | null): void;  差异内容：shadowLayer: ShadowLayer | null | api/@ohos.graphics.drawing.d.ts |
| 函数变更 | 类名：Brush；  API声明：setColorFilter(filter: ColorFilter): void;  差异内容：filter: ColorFilter | 类名：Brush；  API声明：setColorFilter(filter: ColorFilter | null): void;  差异内容：filter: ColorFilter | null | api/@ohos.graphics.drawing.d.ts |
| 函数变更 | 类名：Brush；  API声明：setMaskFilter(filter: MaskFilter): void;  差异内容：filter: MaskFilter | 类名：Brush；  API声明：setMaskFilter(filter: MaskFilter | null): void;  差异内容：filter: MaskFilter | null | api/@ohos.graphics.drawing.d.ts |
| 函数变更 | 类名：Brush；  API声明：setShadowLayer(shadowLayer: ShadowLayer): void;  差异内容：shadowLayer: ShadowLayer | 类名：Brush；  API声明：setShadowLayer(shadowLayer: ShadowLayer | null): void;  差异内容：shadowLayer: ShadowLayer | null | api/@ohos.graphics.drawing.d.ts |
| 函数变更 | 类名：Brush；  API声明：setShaderEffect(shaderEffect: ShaderEffect): void;  差异内容：shaderEffect: ShaderEffect | 类名：Brush；  API声明：setShaderEffect(shaderEffect: ShaderEffect | null): void;  差异内容：shaderEffect: ShaderEffect | null | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：drawing；  API声明：enum VertexMode  差异内容：enum VertexMode | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：VertexMode；  API声明：TRIANGLES\_VERTEXMODE = 0  差异内容：TRIANGLES\_VERTEXMODE = 0 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：VertexMode；  API声明：TRIANGLESSTRIP\_VERTEXMODE = 1  差异内容：TRIANGLESSTRIP\_VERTEXMODE = 1 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：VertexMode；  API声明：TRIANGLESFAN\_VERTEXMODE = 2  差异内容：TRIANGLESFAN\_VERTEXMODE = 2 | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：isInverseFillType(): boolean;  差异内容：isInverseFillType(): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Path；  API声明：toggleInverseFillType(): void;  差异内容：toggleInverseFillType(): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Canvas；  API声明：drawVertices(vertexMode: VertexMode, vertexCount: number, positions: Array<common2D.Point>, texs: Array<common2D.Point> | null, colors: Array<number> | null, indexCount: number, indices: Array<number> | null, mode: BlendMode): void;  差异内容：drawVertices(vertexMode: VertexMode, vertexCount: number, positions: Array<common2D.Point>, texs: Array<common2D.Point> | null, colors: Array<number> | null, indexCount: number, indices: Array<number> | null, mode: BlendMode): void; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Typeface；  API声明：isBold(): boolean;  差异内容：isBold(): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Typeface；  API声明：isItalic(): boolean;  差异内容：isItalic(): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Region；  API声明：isRect(): boolean;  差异内容：isRect(): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：Region；  API声明：quickContains(left: number, top: number, right: number, bottom: number): boolean;  差异内容：quickContains(left: number, top: number, right: number, bottom: number): boolean; | api/@ohos.graphics.drawing.d.ts |
| 新增API | NA | 类名：FontCollection；  API声明：loadFontSyncWithCheck(name: string, path: string | Resource, index?: number): void;  差异内容：loadFontSyncWithCheck(name: string, path: string | Resource, index?: number): void; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontCollection；  API声明：loadFontWithCheck(name: string, path: string | Resource, index?: number): Promise<void>;  差异内容：loadFontWithCheck(name: string, path: string | Resource, index?: number): Promise<void>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：compressHeadPunctuation?: boolean;  差异内容：compressHeadPunctuation?: boolean; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：includeFontPadding?: boolean;  差异内容：includeFontPadding?: boolean; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：fallbackLineSpacing?: boolean;  差异内容：fallbackLineSpacing?: boolean; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：localPostscriptName?: string;  差异内容：localPostscriptName?: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：localFullName?: string;  差异内容：localFullName?: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：localFamilyName?: string;  差异内容：localFamilyName?: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：localSubFamilyName?: string;  差异内容：localSubFamilyName?: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：version?: string;  差异内容：version?: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：manufacture?: string;  差异内容：manufacture?: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：copyright?: string;  差异内容：copyright?: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：trademark?: string;  差异内容：trademark?: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：license?: string;  差异内容：license?: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：index?: number;  差异内容：index?: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明：function isFontSupported(fontURL: string | Resource): boolean;  差异内容：function isFontSupported(fontURL: string | Resource): boolean; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明：function getFontUnicodeSet(path: string | Resource, index: number): Promise<Array<number>>;  差异内容：function getFontUnicodeSet(path: string | Resource, index: number): Promise<Array<number>>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明：function getFontCount(path: string | Resource): number;  差异内容：function getFontCount(path: string | Resource): number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明：function getFontPathsByType(fontType: SystemFontType): Array<string>;  差异内容：function getFontPathsByType(fontType: SystemFontType): Array<string>; | api/@ohos.graphics.text.d.ts |
