---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-dataaugmentationkit-6101
title: Data Augmentation Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Data Augmentation Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:20df55113b0679791fac57bcaabbd339faec3b02db339ed4261dad4b3a34ba88
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：knowledgeProcessor；  API声明：interface KnowledgeProcessConfig  差异内容：interface KnowledgeProcessConfig | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：KnowledgeProcessConfig；  API声明：mode: KnowledgeProcessMode;  差异内容：mode: KnowledgeProcessMode; | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：knowledgeProcessor；  API声明：enum KnowledgeProcessMode  差异内容：enum KnowledgeProcessMode | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：KnowledgeProcessMode；  API声明：INVERTED\_INDEX = 1  差异内容：INVERTED\_INDEX = 1 | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：KnowledgeProcessMode；  API声明：INVERTED\_INDEX\_VECTORIZATION = 3  差异内容：INVERTED\_INDEX\_VECTORIZATION = 3 | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：KnowledgeProcessor；  API声明：startProcess(config: KnowledgeProcessConfig): Promise<void>;  差异内容：startProcess(config: KnowledgeProcessConfig): Promise<void>; | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：KnowledgeProcessor；  API声明：stopProcess(): Promise<void>;  差异内容：stopProcess(): Promise<void>; | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：knowledgeProcessor；  API声明：function cleanKnowledgeData(context: common.Context, config: KnowledgeProcessorConfig): Promise<void>;  差异内容：function cleanKnowledgeData(context: common.Context, config: KnowledgeProcessorConfig): Promise<void>; | api/@hms.data.knowledgeProcessor.d.ts |
