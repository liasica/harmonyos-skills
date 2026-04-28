---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics2d-b123sp18
title: ArkGraphics 2D
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > API变更清单 > ArkGraphics 2D
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:46+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:48a25cc7d991131f16c74ddb9963c96e971e548d725feb3c409b89d38318b541
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：Filter；  API声明：blur(radius: number, tileMode: TileMode): Filter;  差异内容：blur(radius: number, tileMode: TileMode): Filter; | api/@ohos.effectKit.d.ts |
| 新增API | NA | 类名：effectKit；  API声明： enum TileMode  差异内容： enum TileMode | api/@ohos.effectKit.d.ts |
| 新增API | NA | 类名：TileMode；  API声明：CLAMP = 0  差异内容：CLAMP = 0 | api/@ohos.effectKit.d.ts |
| 新增API | NA | 类名：TileMode；  API声明：REPEAT = 1  差异内容：REPEAT = 1 | api/@ohos.effectKit.d.ts |
| 新增API | NA | 类名：TileMode；  API声明：MIRROR = 2  差异内容：MIRROR = 2 | api/@ohos.effectKit.d.ts |
| 新增API | NA | 类名：TileMode；  API声明：DECAL = 3  差异内容：DECAL = 3 | api/@ohos.effectKit.d.ts |
| 新增API | NA | 类名：text；  API声明： enum SystemFontType  差异内容： enum SystemFontType | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：SystemFontType；  API声明：ALL = 1 << 0  差异内容：ALL = 1 << 0 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：SystemFontType；  API声明：GENERIC = 1 << 1  差异内容：GENERIC = 1 << 1 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：SystemFontType；  API声明：STYLISH = 1 << 2  差异内容：STYLISH = 1 << 2 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：SystemFontType；  API声明：INSTALLED = 1 << 3  差异内容：INSTALLED = 1 << 3 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明： interface FontDescriptor  差异内容： interface FontDescriptor | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：path?: string;  差异内容：path?: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：postScriptName?: string;  差异内容：postScriptName?: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：fullName?: string;  差异内容：fullName?: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：fontFamily?: string;  差异内容：fontFamily?: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：fontSubfamily?: string;  差异内容：fontSubfamily?: string; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：weight?: FontWeight;  差异内容：weight?: FontWeight; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：width?: number;  差异内容：width?: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：italic?: number;  差异内容：italic?: number; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：monoSpace?: boolean;  差异内容：monoSpace?: boolean; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：symbolic?: boolean;  差异内容：symbolic?: boolean; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明：function getSystemFontFullNamesByType(fontType: SystemFontType): Promise<Array<string>>;  差异内容：function getSystemFontFullNamesByType(fontType: SystemFontType): Promise<Array<string>>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：text；  API声明：function getFontDescriptorByFullName(fullName: string, fontType: SystemFontType): Promise<FontDescriptor>;  差异内容：function getFontDescriptorByFullName(fullName: string, fontType: SystemFontType): Promise<FontDescriptor>; | api/@ohos.graphics.text.d.ts |
