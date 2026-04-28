---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-visionkit-b123sp18
title: Vision Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > API变更清单 > Vision Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:54+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:4060ab5f2b6194e040198be173ec483b63c5d6617526441004ba69ad94ebc637
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：CardContentConfig；  API声明：idCard?: IdCardConfig;  差异内容：idCard?: IdCardConfig; | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：global；  API声明： declare interface IdCardConfig  差异内容： declare interface IdCardConfig | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：IdCardConfig；  API声明：isPhotoNeeded?: boolean;  差异内容：isPhotoNeeded?: boolean; | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：IdCardConfig；  API声明：isQualityDetectionNeeded?: boolean;  差异内容：isQualityDetectionNeeded?: boolean; | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController；  API声明：getImageAnalyzerUIStatus(): Promise<ImageAnalyzerUIStatus>;  差异内容：getImageAnalyzerUIStatus(): Promise<ImageAnalyzerUIStatus>; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：visionImageAnalyzer；  API声明： enum ImageAnalyzerUIStatus  差异内容： enum ImageAnalyzerUIStatus | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：ImageAnalyzerUIStatus；  API声明：INITIAL = 0  差异内容：INITIAL = 0 | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：ImageAnalyzerUIStatus；  API声明：AI\_BUTTON\_SELECTED = 1  差异内容：AI\_BUTTON\_SELECTED = 1 | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：ImageAnalyzerUIStatus；  API声明：TEXT\_SELECTED = 2  差异内容：TEXT\_SELECTED = 2 | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：ImageAnalyzerUIStatus；  API声明：SUBJECT\_SELECTED = 3  差异内容：SUBJECT\_SELECTED = 3 | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：ImageAnalyzerUIStatus；  API声明：OBJECT\_SEARCH = 4  差异内容：OBJECT\_SEARCH = 4 | api/@hms.ai.visionImageAnalyzer.d.ets |
