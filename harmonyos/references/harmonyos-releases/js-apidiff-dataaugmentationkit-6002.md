---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-dataaugmentationkit-6002
title: Data Augmentation Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > Data Augmentation Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:28+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:68df54c6aa4581af44afe0a653c78ca23af6ea1f6554ae25027df295ee9732e8
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：Retriever；  API声明：retrieveRdb(query: string, condition: RetrievalCondition): Promise<RdbRecords>;  差异内容：NA | 类名：Retriever；  API声明：retrieveRdb(query: string, condition: RetrievalCondition): Promise<RdbRecords>;  差异内容：1021200012 | api/@hms.data.retrieval.d.ts |
| 属性变更 | 类名：VectorQuery；  API声明：value: Float32Array;  差异内容：value: Float32Array; | 类名：VectorQuery；  API声明：value?: Float32Array;  差异内容：value?: Float32Array; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace knowledgeProcessor  差异内容：declare namespace knowledgeProcessor | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：knowledgeProcessor；  API声明：function getKnowledgeProcessor(context: common.BaseContext, config: KnowledgeProcessorConfig): Promise<KnowledgeProcessor>;  差异内容：function getKnowledgeProcessor(context: common.BaseContext, config: KnowledgeProcessorConfig): Promise<KnowledgeProcessor>; | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：knowledgeProcessor；  API声明：interface KnowledgeProcessorConfig  差异内容：interface KnowledgeProcessorConfig | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：KnowledgeProcessorConfig；  API声明：sourceConfig: KnowledgeSourceConfig;  差异内容：sourceConfig: KnowledgeSourceConfig; | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：knowledgeProcessor；  API声明：interface KnowledgeSourceConfig  差异内容：interface KnowledgeSourceConfig | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：KnowledgeSourceConfig；  API声明：rdbSource?: relationalStore.StoreConfig;  差异内容：rdbSource?: relationalStore.StoreConfig; | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：knowledgeProcessor；  API声明：enum ProcessorStatus  差异内容：enum ProcessorStatus | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：ProcessorStatus；  API声明：DATA\_REMAINING\_TO\_PROCESS = 0  差异内容：DATA\_REMAINING\_TO\_PROCESS = 0 | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：ProcessorStatus；  API声明：DATA\_PROCESSING\_IN\_PROGRESS = 1  差异内容：DATA\_PROCESSING\_IN\_PROGRESS = 1 | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：ProcessorStatus；  API声明：DATA\_PROCESSING\_COMPLETE = 2  差异内容：DATA\_PROCESSING\_COMPLETE = 2 | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：knowledgeProcessor；  API声明：interface KnowledgeProcessor  差异内容：interface KnowledgeProcessor | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：KnowledgeProcessor；  API声明：getStatus(): Promise<ProcessorStatus>;  差异内容：getStatus(): Promise<ProcessorStatus>; | api/@hms.data.knowledgeProcessor.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.data.knowledgeProcessor.d.ts  差异内容：DataAugmentationKit | api/@hms.data.knowledgeProcessor.d.ts |
