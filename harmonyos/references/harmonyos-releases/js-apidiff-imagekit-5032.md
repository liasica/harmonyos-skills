---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imagekit-5032
title: Image Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta2引入的API > Image Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:35+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:e2e504937e5cee3dc6ea175d7aa2e841ea0a259f0053dd563c101dd13f3cb6a5
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：image；  API声明： enum AllocatorType  差异内容： enum AllocatorType | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AllocatorType；  API声明：AUTO = 0  差异内容：AUTO = 0 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AllocatorType；  API声明：DMA = 1  差异内容：DMA = 1 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AllocatorType；  API声明：SHARE\_MEMORY = 2  差异内容：SHARE\_MEMORY = 2 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageSource；  API声明：createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType): Promise<PixelMap>;  差异内容：createPixelMapUsingAllocator(options?: DecodingOptions, allocatorType?: AllocatorType): Promise<PixelMap>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageSource；  API声明：createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType): PixelMap;  差异内容：createPixelMapUsingAllocatorSync(options?: DecodingOptions, allocatorType?: AllocatorType): PixelMap; | api/@ohos.multimedia.image.d.ts |
