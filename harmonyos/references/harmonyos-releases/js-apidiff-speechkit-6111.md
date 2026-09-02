---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-speechkit-6111
title: Speech Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > Speech Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:08+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:c6352082e90df79142cb6687ddfe3d9dcbf1b2d72ce5c10f4efa4758d31b9bb2
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：AICaptionOptions；  API声明：onError: ErrorCallback;  差异内容：NA | 类名：AICaptionOptions；  API声明：onError: ErrorCallback;  差异内容：1012900013 | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare enum AICaptionFontSize  差异内容：export declare enum AICaptionFontSize | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AICaptionFontSize；  API声明：SMALL = 1  差异内容：SMALL = 1 | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AICaptionFontSize；  API声明：NORMAL = 2  差异内容：NORMAL = 2 | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AICaptionFontSize；  API声明：BIG = 3  差异内容：BIG = 3 | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AICaptionFontSize；  API声明：LARGE = 4  差异内容：LARGE = 4 | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AICaptionOptions；  API声明：sourceLanguage?: string;  差异内容：sourceLanguage?: string; | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AICaptionOptions；  API声明：targetLanguage?: string;  差异内容：targetLanguage?: string; | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AICaptionOptions；  API声明：fontSize?: AICaptionFontSize;  差异内容：fontSize?: AICaptionFontSize; | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：AICaptionOptions；  API声明：fontColor?: ResourceColor;  差异内容：fontColor?: ResourceColor; | api/@hms.ai.AICaption.d.ets |
| 新增API | NA | 类名：global；  API声明：export type UpReadState = (readState: ReadStateCode) => void;  差异内容：export type UpReadState = (readState: ReadStateCode) => void; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：global；  API声明：export struct TextReaderIconV2  差异内容：export struct TextReaderIconV2 | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReaderIconV2；  API声明：@Param  readState: ReadStateCode;  差异内容：@Param  readState: ReadStateCode; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReaderIconV2；  API声明：@Event  upReadState: UpReadState;  差异内容：@Event  upReadState: UpReadState; | api/@hms.ai.textReader.d.ets |
| 新增API | NA | 类名：TextReaderIconV2；  API声明：build(): void;  差异内容：build(): void; | api/@hms.ai.textReader.d.ets |
