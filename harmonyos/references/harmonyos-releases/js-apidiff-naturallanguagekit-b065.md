---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-naturallanguagekit-b065
title: Natural Language Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > Natural Language Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:19+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:77ffbaaec0b2b478f22229ba8ab37b9811d9e18f085b096b2729d85ddd259e6d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：textProcessing；  API声明：function init(): Promise<boolean>;  差异内容：1011200001,1011200002 | 类名：textProcessing；  API声明：function init(): Promise<boolean>;  差异内容：1011200001,1011200002,200,401 | api/@hms.ai.nlp.textProcessing.d.ts |
| 错误码变更 | 类名：textProcessing；  API声明：function release(): Promise<boolean>;  差异内容：1011200001,1011200002 | 类名：textProcessing；  API声明：function release(): Promise<boolean>;  差异内容：1011200001,1011200002,200,401 | api/@hms.ai.nlp.textProcessing.d.ts |
| 错误码变更 | 类名：textProcessing；  API声明：function getWordSegment(text: string): Promise<Array<WordSegment>>;  差异内容：1011200001,1011200002,401 | 类名：textProcessing；  API声明：function getWordSegment(text: string): Promise<Array<WordSegment>>;  差异内容：1011200001,1011200002,200,401 | api/@hms.ai.nlp.textProcessing.d.ts |
| 错误码变更 | 类名：textProcessing；  API声明：function getEntity(text: string, entityConfig?: EntityConfig): Promise<Array<Entity>>;  差异内容：1011200001,1011200002,401 | 类名：textProcessing；  API声明：function getEntity(text: string, entityConfig?: EntityConfig): Promise<Array<Entity>>;  差异内容：1011200001,1011200002,200,401 | api/@hms.ai.nlp.textProcessing.d.ts |
