---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-visionkit-5111
title: Vision Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > Vision Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:56+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:50dc037ddbb999b5ab6a2f1adef2d72601175ab62819bb3452c59e6821fdf206
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：CardRecognition；  API声明：callback: Callback<CallbackParam>;  差异内容：NA | 类名：CardRecognition；  API声明：callback: Callback<CallbackParam>;  差异内容：19 | api/@hms.ai.CardRecognition.d.ets |
| API废弃版本变更 | 类名：global；  API声明：declare interface CallbackParam  差异内容：NA | 类名：global；  API声明：declare interface CallbackParam  差异内容：19 | api/@hms.ai.CardRecognition.d.ets |
| API废弃版本变更 | 类名：CallbackParam；  API声明：code: number;  差异内容：NA | 类名：CallbackParam；  API声明：code: number;  差异内容：19 | api/@hms.ai.CardRecognition.d.ets |
| API废弃版本变更 | 类名：CallbackParam；  API声明：cardType?: CardType;  差异内容：NA | 类名：CallbackParam；  API声明：cardType?: CardType;  差异内容：19 | api/@hms.ai.CardRecognition.d.ets |
| API废弃版本变更 | 类名：CallbackParam；  API声明：cardInfo?: Record<string, Record<string, string>>;  差异内容：NA | 类名：CallbackParam；  API声明：cardInfo?: Record<string, Record<string, string>>;  差异内容：19 | api/@hms.ai.CardRecognition.d.ets |
| 删除错误码 | 类名：VisionImageAnalyzerController；  API声明：on(type: 'cursorMoveInText', callback: Callback<void>): void;  差异内容：1013700002,401 | 类名：VisionImageAnalyzerController；  API声明：on(type: 'cursorMoveInText', callback: Callback<void>): void;  差异内容：NA | api/@hms.ai.visionImageAnalyzer.d.ets |
| 删除错误码 | 类名：VisionImageAnalyzerController；  API声明：off(type: 'cursorMoveInText', callback?: ErrorCallback): void;  差异内容：1013700002,401 | 类名：VisionImageAnalyzerController；  API声明：off(type: 'cursorMoveInText', callback?: Callback<void>): void;  差异内容：NA | api/@hms.ai.visionImageAnalyzer.d.ets |
| 删除错误码 | 类名：VisionImageAnalyzerController；  API声明：on(type: 'cursorMoveOutText', callback: Callback<void>): void;  差异内容：1013700002,401 | 类名：VisionImageAnalyzerController；  API声明：on(type: 'cursorMoveOutText', callback: Callback<void>): void;  差异内容：NA | api/@hms.ai.visionImageAnalyzer.d.ets |
| 删除错误码 | 类名：VisionImageAnalyzerController；  API声明：off(type: 'cursorMoveOutText', callback?: ErrorCallback): void;  差异内容：1013700002,401 | 类名：VisionImageAnalyzerController；  API声明：off(type: 'cursorMoveOutText', callback?: Callback<void>): void;  差异内容：NA | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：CardRecognition；  API声明：onResult: Callback<CardRecognitionResult>;  差异内容：onResult: Callback<CardRecognitionResult>; | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：global；  API声明：declare interface CardRecognitionResult  差异内容：declare interface CardRecognitionResult | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：CardRecognitionResult；  API声明：code: number;  差异内容：code: number; | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：CardRecognitionResult；  API声明：cardType?: CardType;  差异内容：cardType?: CardType; | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：CardRecognitionResult；  API声明：cardInfo?: Record<string, Record<string, string>>;  差异内容：cardInfo?: Record<string, Record<string, string>>; | api/@hms.ai.CardRecognition.d.ets |
| 函数变更 | 类名：VisionImageAnalyzerController；  API声明：off(type: 'cursorMoveInText', callback?: ErrorCallback): void;  差异内容：callback?: ErrorCallback | 类名：VisionImageAnalyzerController；  API声明：off(type: 'cursorMoveInText', callback?: Callback<void>): void;  差异内容：callback?: Callback<void> | api/@hms.ai.visionImageAnalyzer.d.ets |
| 函数变更 | 类名：VisionImageAnalyzerController；  API声明：off(type: 'cursorMoveOutText', callback?: ErrorCallback): void;  差异内容：callback?: ErrorCallback | 类名：VisionImageAnalyzerController；  API声明：off(type: 'cursorMoveOutText', callback?: Callback<void>): void;  差异内容：callback?: Callback<void> | api/@hms.ai.visionImageAnalyzer.d.ets |
