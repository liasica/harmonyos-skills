---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-dataaugmentationkit-6003
title: Data Augmentation Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:16+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:351e401b59f71210b07539a7865717d21aee57671a32368e6a82e6a07ef8e582
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace localChatModel  差异内容：declare namespace localChatModel | api/@hms.data.localChatModel.d.ts |
| 新增API | NA | 类名：localChatModel；  API声明：interface Config  差异内容：interface Config | api/@hms.data.localChatModel.d.ts |
| 新增API | NA | 类名：Config；  API声明：isStream: boolean;  差异内容：isStream: boolean; | api/@hms.data.localChatModel.d.ts |
| 新增API | NA | 类名：localChatModel；  API声明：interface QuestionInfo  差异内容：interface QuestionInfo | api/@hms.data.localChatModel.d.ts |
| 新增API | NA | 类名：QuestionInfo；  API声明：questionId: number;  差异内容：questionId: number; | api/@hms.data.localChatModel.d.ts |
| 新增API | NA | 类名：QuestionInfo；  API声明：content: string;  差异内容：content: string; | api/@hms.data.localChatModel.d.ts |
| 新增API | NA | 类名：localChatModel；  API声明：interface Answer  差异内容：interface Answer | api/@hms.data.localChatModel.d.ts |
| 新增API | NA | 类名：Answer；  API声明：questionId: number;  差异内容：questionId: number; | api/@hms.data.localChatModel.d.ts |
| 新增API | NA | 类名：Answer；  API声明：content: string;  差异内容：content: string; | api/@hms.data.localChatModel.d.ts |
| 新增API | NA | 类名：Answer；  API声明：isFinished: boolean;  差异内容：isFinished: boolean; | api/@hms.data.localChatModel.d.ts |
| 新增API | NA | 类名：localChatModel；  API声明：function init(): Promise<boolean>;  差异内容：function init(): Promise<boolean>; | api/@hms.data.localChatModel.d.ts |
| 新增API | NA | 类名：localChatModel；  API声明：function chat(info: QuestionInfo, config: Config, callback: AsyncCallback<Answer>): Promise<void>;  差异内容：function chat(info: QuestionInfo, config: Config, callback: AsyncCallback<Answer>): Promise<void>; | api/@hms.data.localChatModel.d.ts |
| 新增API | NA | 类名：retrieval；  API声明：interface ExplanationConfig  差异内容：interface ExplanationConfig | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：ExplanationConfig；  API声明：groundTruths: Array<string>;  差异内容：groundTruths: Array<string>; | api/@hms.data.retrieval.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.data.localChatModel.d.ts  差异内容：DataAugmentationKit | api/@hms.data.localChatModel.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：ChatLLM；  API声明：abstract cancel(chatId: number): void;  差异内容：abstract cancel(chatId: number): void; | api/@hms.data.rag.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：RagSession；  API声明：cancel(runId: number): Promise<void>;  差异内容：cancel(runId: number): Promise<void>; | api/@hms.data.rag.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：RetrievalCondition；  API声明：explanation?: ExplanationConfig;  差异内容：explanation?: ExplanationConfig; | api/@hms.data.retrieval.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：RdbRecords；  API声明：missedGroundTruths?: Array<ItemInfo>;  差异内容：missedGroundTruths?: Array<ItemInfo>; | api/@hms.data.retrieval.d.ts |
