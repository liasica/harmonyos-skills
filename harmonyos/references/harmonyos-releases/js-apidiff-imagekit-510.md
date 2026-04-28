---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imagekit-510
title: Image Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Image Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:09+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a7584667fd7c414c0d20c005b9d1a0ddacc8fe4d3bd76f732c4e56c05400a291
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace videoProcessingEngine  差异内容：declare namespace videoProcessingEngine | api/@ohos.multimedia.videoProcessingEngine.d.ts |
| 新增API | NA | 类名：videoProcessingEngine；  API声明：enum QualityLevel  差异内容：enum QualityLevel | api/@ohos.multimedia.videoProcessingEngine.d.ts |
| 新增API | NA | 类名：QualityLevel；  API声明：NONE = 0  差异内容：NONE = 0 | api/@ohos.multimedia.videoProcessingEngine.d.ts |
| 新增API | NA | 类名：QualityLevel；  API声明：LOW = 1  差异内容：LOW = 1 | api/@ohos.multimedia.videoProcessingEngine.d.ts |
| 新增API | NA | 类名：QualityLevel；  API声明：MEDIUM = 2  差异内容：MEDIUM = 2 | api/@ohos.multimedia.videoProcessingEngine.d.ts |
| 新增API | NA | 类名：QualityLevel；  API声明：HIGH = 3  差异内容：HIGH = 3 | api/@ohos.multimedia.videoProcessingEngine.d.ts |
| 新增API | NA | 类名：videoProcessingEngine；  API声明：interface ImageProcessor  差异内容：interface ImageProcessor | api/@ohos.multimedia.videoProcessingEngine.d.ts |
| 新增API | NA | 类名：ImageProcessor；  API声明：enhanceDetail(sourceImage: image.PixelMap, width: number, height: number, level?: QualityLevel): Promise<image.PixelMap>;  差异内容：enhanceDetail(sourceImage: image.PixelMap, width: number, height: number, level?: QualityLevel): Promise<image.PixelMap>; | api/@ohos.multimedia.videoProcessingEngine.d.ts |
| 新增API | NA | 类名：ImageProcessor；  API声明：enhanceDetail(sourceImage: image.PixelMap, scale: number, level?: QualityLevel): Promise<image.PixelMap>;  差异内容：enhanceDetail(sourceImage: image.PixelMap, scale: number, level?: QualityLevel): Promise<image.PixelMap>; | api/@ohos.multimedia.videoProcessingEngine.d.ts |
| 新增API | NA | 类名：ImageProcessor；  API声明：enhanceDetailSync(sourceImage: image.PixelMap, width: number, height: number, level?: QualityLevel): image.PixelMap;  差异内容：enhanceDetailSync(sourceImage: image.PixelMap, width: number, height: number, level?: QualityLevel): image.PixelMap; | api/@ohos.multimedia.videoProcessingEngine.d.ts |
| 新增API | NA | 类名：ImageProcessor；  API声明：enhanceDetailSync(sourceImage: image.PixelMap, scale: number, level?: QualityLevel): image.PixelMap;  差异内容：enhanceDetailSync(sourceImage: image.PixelMap, scale: number, level?: QualityLevel): image.PixelMap; | api/@ohos.multimedia.videoProcessingEngine.d.ts |
| 新增API | NA | 类名：videoProcessingEngine；  API声明：function initializeEnvironment(): Promise<void>;  差异内容：function initializeEnvironment(): Promise<void>; | api/@ohos.multimedia.videoProcessingEngine.d.ts |
| 新增API | NA | 类名：videoProcessingEngine；  API声明：function deinitializeEnvironment(): Promise<void>;  差异内容：function deinitializeEnvironment(): Promise<void>; | api/@ohos.multimedia.videoProcessingEngine.d.ts |
| 新增API | NA | 类名：videoProcessingEngine；  API声明：function create(): ImageProcessor;  差异内容：function create(): ImageProcessor; | api/@ohos.multimedia.videoProcessingEngine.d.ts |
| 新增API | NA | 类名：PixelMapFormat；  API声明：ARGB\_8888 = 1  差异内容：ARGB\_8888 = 1 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMapFormat；  API声明：ASTC\_4x4 = 102  差异内容：ASTC\_4x4 = 102 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：enum CropAndScaleStrategy  差异内容：enum CropAndScaleStrategy | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：CropAndScaleStrategy；  API声明：SCALE\_FIRST = 1  差异内容：SCALE\_FIRST = 1 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：CropAndScaleStrategy；  API声明：CROP\_FIRST = 2  差异内容：CROP\_FIRST = 2 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：interface PackingOptionsForSequence  差异内容：interface PackingOptionsForSequence | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PackingOptionsForSequence；  API声明：frameCount: number;  差异内容：frameCount: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PackingOptionsForSequence；  API声明：delayTimeList: Array<number>;  差异内容：delayTimeList: Array<number>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PackingOptionsForSequence；  API声明：disposalTypes?: Array<number>;  差异内容：disposalTypes?: Array<number>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PackingOptionsForSequence；  API声明：loopCount?: number;  差异内容：loopCount?: number; | api/@ohos.multimedia.image.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.multimedia.videoProcessingEngine.d.ts  差异内容：ImageKit | api/@ohos.multimedia.videoProcessingEngine.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：PixelMap；  API声明：createScaledPixelMap(x: number, y: number, level?: AntiAliasingLevel): Promise<PixelMap>;  差异内容：createScaledPixelMap(x: number, y: number, level?: AntiAliasingLevel): Promise<PixelMap>; | api/@ohos.multimedia.image.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：PixelMap；  API声明：createScaledPixelMapSync(x: number, y: number, level?: AntiAliasingLevel): PixelMap;  差异内容：createScaledPixelMapSync(x: number, y: number, level?: AntiAliasingLevel): PixelMap; | api/@ohos.multimedia.image.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：PixelMap；  API声明：cloneSync(): PixelMap;  差异内容：cloneSync(): PixelMap; | api/@ohos.multimedia.image.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：PixelMap；  API声明：clone(): Promise<PixelMap>;  差异内容：clone(): Promise<PixelMap>; | api/@ohos.multimedia.image.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：ImagePacker；  API声明：packToDataFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>;  差异内容：packToDataFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>; | api/@ohos.multimedia.image.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：ImagePacker；  API声明：packToFileFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, fd: number, options: PackingOptionsForSequence): Promise<void>;  差异内容：packToFileFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, fd: number, options: PackingOptionsForSequence): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：DecodingOptions；  API声明：cropAndScaleStrategy?: CropAndScaleStrategy;  差异内容：cropAndScaleStrategy?: CropAndScaleStrategy; | api/@ohos.multimedia.image.d.ts |
