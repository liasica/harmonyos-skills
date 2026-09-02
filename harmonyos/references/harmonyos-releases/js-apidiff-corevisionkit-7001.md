---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corevisionkit-7001
title: Core Vision Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Core Vision Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:05+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:c2193834106bc1c7a34da597f30c3d32d6f92a5b4f72e330572329244da6e08f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace imageSuperResolution  差异内容：declare namespace imageSuperResolution | api/@hms.ai.vision.imageSuperResolution.d.ts |
| 新增API | NA | 类名：imageSuperResolution；  API声明：export class ISPResponse  差异内容：export class ISPResponse | api/@hms.ai.vision.imageSuperResolution.d.ts |
| 新增API | NA | 类名：ISPResponse；  API声明：pixelMap: image.PixelMap;  差异内容：pixelMap: image.PixelMap; | api/@hms.ai.vision.imageSuperResolution.d.ts |
| 新增API | NA | 类名：imageSuperResolution；  API声明：class ImageSRAnalyzer  差异内容：class ImageSRAnalyzer | api/@hms.ai.vision.imageSuperResolution.d.ts |
| 新增API | NA | 类名：ImageSRAnalyzer；  API声明：public static create(): Promise<ImageSRAnalyzer>;  差异内容：public static create(): Promise<ImageSRAnalyzer>; | api/@hms.ai.vision.imageSuperResolution.d.ts |
| 新增API | NA | 类名：ImageSRAnalyzer；  API声明：process(request: visionBase.Request): Promise<ISPResponse>;  差异内容：process(request: visionBase.Request): Promise<ISPResponse>; | api/@hms.ai.vision.imageSuperResolution.d.ts |
| 新增API | NA | 类名：ImageSRAnalyzer；  API声明：destroy(): Promise<void>;  差异内容：destroy(): Promise<void>; | api/@hms.ai.vision.imageSuperResolution.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace textSearchImage  差异内容：declare namespace textSearchImage | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增API | NA | 类名：textSearchImage；  API声明：class ImageObject  差异内容：class ImageObject | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增API | NA | 类名：ImageObject；  API声明：imagePath: string;  差异内容：imagePath: string; | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增API | NA | 类名：ImageObject；  API声明：scope: string;  差异内容：scope: string; | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增API | NA | 类名：ImageObject；  API声明：similarity: number;  差异内容：similarity: number; | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增API | NA | 类名：textSearchImage；  API声明：function init(): Promise<boolean>;  差异内容：function init(): Promise<boolean>; | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增API | NA | 类名：textSearchImage；  API声明：function insertImage(imagePath: string, scope: string): Promise<boolean>;  差异内容：function insertImage(imagePath: string, scope: string): Promise<boolean>; | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增API | NA | 类名：textSearchImage；  API声明：function search(query: string, scope: string, topKey?: number): Promise<ImageObject[]>;  差异内容：function search(query: string, scope: string, topKey?: number): Promise<ImageObject[]>; | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增API | NA | 类名：textSearchImage；  API声明：function deleteImage(imagePath: string, scope: string): Promise<boolean>;  差异内容：function deleteImage(imagePath: string, scope: string): Promise<boolean>; | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增API | NA | 类名：textSearchImage；  API声明：function clearData(): Promise<boolean>;  差异内容：function clearData(): Promise<boolean>; | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增API | NA | 类名：textSearchImage；  API声明：function release(): Promise<boolean>;  差异内容：function release(): Promise<boolean>; | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.ai.vision.imageSuperResolution.d.ts  差异内容：CoreVisionKit | api/@hms.ai.vision.imageSuperResolution.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.ai.vision.textSearchImage.d.ts  差异内容：CoreVisionKit | api/@hms.ai.vision.textSearchImage.d.ts |
