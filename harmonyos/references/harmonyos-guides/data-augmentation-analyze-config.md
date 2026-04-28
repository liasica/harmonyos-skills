---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-augmentation-analyze-config
title: 配置分析过程模板
breadcrumb: 指南 > 应用框架 > Data Augmentation Kit（数据增强服务） > RAG > RAG配置 > 配置分析过程模板
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2a34ceb4856220cb149d721f7969e0a2ad778cb1b0c2e438fe72ee4f59fc13bf
---

## 功能介绍

分析过程模板用于在RAG运行时，通过流式输出向用户实时呈现结构化的中间结果。该模板包含预设文本和动态占位符，可将大模型的输出或RAG执行中的关键信息组织为连贯文本。开发者可以通过在指定应用[资源目录](resource-categories-and-access.md#资源目录)放置thought\_template.json配置文件，自定义分析过程模板。

可供配置的8个分析过程模板如下：

* {text}是核心内容占位符，用于动态替换RAG执行过程中的文本信息。
* 仅有thoughtStart、thoughtFinishCoreference、thoughtFinishExtraction三个参数对应模板可使用占位符，且只有第一个占位符会动态替换文本。
* 支持占位符的模板可选择不放占位符，即不会进行内容替换。

| 模板参数名 | 参数名含义 | 占位符 | 占位符替换内容 | 模板文本（含占位符）长度限制 |
| --- | --- | --- | --- | --- |
| thoughtStart | 思考过程开始 | {text} | 输出用户问题 | 600字节 |
| thoughtStartCoreference | 指代消除开始 | 不支持占位符 | 不涉及 | 600字节 |
| thoughtFinishCoreference | 指代消除结束 | {text} | 输出指代消除结果 | 600字节 |
| thoughtStartExtraction | 实体提取开始 | 不支持占位符 | 不涉及 | 600字节 |
| thoughtFinishExtraction | 实体提取结束 | {text} | 输出实体提取结果 | 600字节 |
| thoughtStartRetrieval | 知识检索开始 | 不支持占位符 | 不涉及 | 600字节 |
| thoughtFinishRetrieval | 知识检索结束 | 不支持占位符 | 不涉及 | 600字节 |
| thoughtFinish | 思考过程结束 | 不支持占位符 | 不涉及 | 600字节 |

## 约束限制

1. 配置文件中的模板参数名称必须和给定的名称严格一致才能生效，对应值必须为字符串格式，使用UTF-8编码，使用其他编码可能会导致流式输出乱码。未配置或配置失败的超参使用默认值代替。
2. 模板文字不得超过600字节，约200个汉字。否则对应模板会配置失败。
3. 只用thoughtStart模板值配置为空字符串时，会配置失败。其余模板可配置为空字符串，即不会输出对应内容。

## 开发步骤

在应用[资源目录](resource-categories-and-access.md#资源目录)的rawfile/arkdata/rag下创建thought\_template.json文件，若工程中无目标目录则递归创建。

分析过程模板文件thought\_template.json默认如下，实际文件内容请根据业务需要进行配置。

```
1. {
2. "thoughtStart": "开始分析用户的问题，原始问题是: \n{text}\n\n\n解析用户需求流程包括：对问题进行改写分析、提取问题中的关键信息、寻找知识库中的关联信息、总结相关内容生成答复。\n",
3. "thoughtStartCoreference": "\n开始对用户的问题进行改写分析...\n",
4. "thoughtFinishCoreference": "\n问题改写结果为: \n{text}\n",
5. "thoughtStartExtraction": "\n\n接下来对用户问题中的关键信息进行提取和分析...",
6. "thoughtFinishExtraction": "\n用户问题中的关键信息提取结果如下: \n{text}\n信息提取完成...\n",
7. "thoughtStartRetrieval": "\n现在根据提取到的信息对知识库进行检索......",
8. "thoughtFinishRetrieval": "\n\n相关内容检索完成，",
9. "thoughtFinish": "为你总结并生成回复中"
10. }
```
