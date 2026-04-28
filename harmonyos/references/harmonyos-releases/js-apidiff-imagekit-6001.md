---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imagekit-6001
title: Image Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > Image Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:40+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:425019bfae30354b010600f738a5dcadb8039b9efb274fa36245a288df833f51
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：image；  API声明：function createPixelMapUsingAllocator(colors: ArrayBuffer, options: InitializationOptions, allocatorType?: AllocatorType): Promise<PixelMap>;  差异内容：function createPixelMapUsingAllocator(colors: ArrayBuffer, options: InitializationOptions, allocatorType?: AllocatorType): Promise<PixelMap>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：function createPixelMapUsingAllocatorSync(colors: ArrayBuffer, options: InitializationOptions, allocatorType?: AllocatorType): PixelMap;  差异内容：function createPixelMapUsingAllocatorSync(colors: ArrayBuffer, options: InitializationOptions, allocatorType?: AllocatorType): PixelMap; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：function createPixelMapUsingAllocatorSync(options: InitializationOptions, allocatorType?: AllocatorType): PixelMap;  差异内容：function createPixelMapUsingAllocatorSync(options: InitializationOptions, allocatorType?: AllocatorType): PixelMap; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：function getImageSourceSupportedFormats(): string[];  差异内容：function getImageSourceSupportedFormats(): string[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：function getImagePackerSupportedFormats(): string[];  差异内容：function getImagePackerSupportedFormats(): string[]; | api/@ohos.multimedia.image.d.ts |
