---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-augmentation-config-prompt-template
title: 配置提示词模板
breadcrumb: 指南 > 应用框架 > Data Augmentation Kit（数据增强服务） > RAG > RAG配置 > 配置提示词模板
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d2cbeaf0b7581263c352c3019dda9404bc76253494bc280e1f76c89b1ec30959
---

## 功能介绍

提示词模板采用结构化的固定格式，将“角色、任务、输入和输出要求”等要素清晰组织起来，使开发者只需填充关键信息，即可稳定、高效地引导模型生成预期结果。开发者可以通过在指定应用[资源目录](resource-categories-and-access.md#资源目录)放置prompt\_template.json配置文件，导入自定义提示词模板。

RAG每组提示词模板包含：系统提示词（system）和用户提示词（user），格式为：

```
1. "提示词模板组名称": {
2. "system": "XXX"，
3. "user": "XXX"
4. }
```

RAG支持三个自定义提示词模板组，并提供占位符，用于替换对应内容。同一个占位符可以在模板中使用多次，每个占位符均会进行内容替换。

| 提示词模板组名称 | 提示词模板组描述 | 占位符 | 占位符替换内容 |
| --- | --- | --- | --- |
| coreferencePrompt | 指代消除提示词模板组 | {history} | 指代消除阶段用于指导指代消除的历史问答记录信息 |
| coreferencePrompt | 指代消除提示词模板组 | {input} | 指代消除阶段用户的输入 |
| extractionPrompt | 关键词提取提示词模板组 | {question} | 关键词处理阶段用户的输入 |
| answerPrompt | 总结提示词模板组 | {history} | 总结阶段用户的历史问答记录信息 |
| answerPrompt | 总结提示词模板组 | {time} | 总结阶段的时间信息 |
| answerPrompt | 总结提示词模板组 | {query} | 总结阶段用户的输入 |
| answerPrompt | 总结提示词模板组 | {retrieval} | 总结阶段用于支持总结的检索结果信息 |

## 约束限制

1. 配置文件中的超参名称必须和给定的名称严格一致才能生效，即模板组的key必须为：coreferencePrompt、extractionPrompt、answerPrompt之一。每个提示词模板组必须同时包含系统提示词（system）和用户提示词（user）两项。
2. 提示词模板的数据类型必须为字符串格式，否则可能导致模板载入失败。
3. 提示词模板的长度建议符合实际使用的大模型配置。

## 开发步骤

在应用[资源目录](resource-categories-and-access.md#资源目录)的rawfile/arkdata/rag下创建prompt\_template.json文件，若工程中无目标目录则递归创建。

提示词模板文件prompt\_template.json示例如下，实际文件内容请根据业务需要进行配置。

```
1. {
2. "coreferencePrompt": {
3. "system": "This is a coreference system prompt."，
4. "user": " This is a coreference user prompt.\nPrompt history: {history}; Prompt input: {input}."
5. },
6. "extractionPrompt": {
7. "system": "This is extraction system prompt.",
8. "user": " This is extraction user prompt.\nPrompt question: {question}. "
9. },
10. "answerPrompt": {
11. "system": "This is answer system prompt.",
12. "user": " This is answer user prompt.\nPrompt history: {history};Prompt time: {time};Prompt query: {query};Prompt retrieval: {retrieval}."
13. }
14. }
```
