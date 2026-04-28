---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corespeechkit-510
title: Core Speech Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Core Speech Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:07+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:05b1025171c837d08768aafd81e0d5dbf7271d7ef1cafd6f11a266104adc0233
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：speechRecognizer；  API声明：function createEngine(createEngineParams: CreateEngineParams, callback: AsyncCallback<SpeechRecognitionEngine>): void;  差异内容：NA | 类名：speechRecognizer；  API声明：function createEngine(createEngineParams: CreateEngineParams, callback: AsyncCallback<SpeechRecognitionEngine>): void;  差异内容：1002200009 | api/@hms.ai.speechRecognizer.d.ts |
| 新增错误码 | 类名：speechRecognizer；  API声明：function createEngine(createEngineParams: CreateEngineParams): Promise<SpeechRecognitionEngine>;  差异内容：NA | 类名：speechRecognizer；  API声明：function createEngine(createEngineParams: CreateEngineParams): Promise<SpeechRecognitionEngine>;  差异内容：1002200009 | api/@hms.ai.speechRecognizer.d.ts |
| 新增错误码 | 类名：SpeechRecognitionEngine；  API声明：listLanguages(params: LanguageQuery, callback: AsyncCallback<Array<string>>): void;  差异内容：NA | 类名：SpeechRecognitionEngine；  API声明：listLanguages(params: LanguageQuery, callback: AsyncCallback<Array<string>>): void;  差异内容：1002200009 | api/@hms.ai.speechRecognizer.d.ts |
| 新增错误码 | 类名：SpeechRecognitionEngine；  API声明：listLanguages(params: LanguageQuery): Promise<Array<string>>;  差异内容：NA | 类名：SpeechRecognitionEngine；  API声明：listLanguages(params: LanguageQuery): Promise<Array<string>>;  差异内容：1002200009 | api/@hms.ai.speechRecognizer.d.ts |
