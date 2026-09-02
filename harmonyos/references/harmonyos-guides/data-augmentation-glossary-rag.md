---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-augmentation-glossary-rag
title: RAG术语
breadcrumb: 指南 > 应用框架 > Data Augmentation Kit（数据增强服务） > Data Augmentation Kit术语 > RAG术语
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:25+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:34bfb55e207a63c7217f90934cd70fa2c00c1f102677b0b83b459a8cfebe0f98
---

本术语收录Data Augmentation Kit中RAG模块涉及的核心术语，按英文首字母排序。

## C

### Config；RAG配置

RAG会话的配置项，包含大模型（Large Language Model，简称LLM）、检索配置（retrievalConfig）和检索条件（retrievalCondition）三个核心属性。

## K

### Knowledge Base；知识库

经知识加工处理后形成的结构化数据存储。包含向量数据库和倒排索引数据库，为RAG提供检索内容支持。

## R

### RunConfig；运行配置

流式问答的配置项。通过[StreamType](../harmonyos-references/dataaugmentation-rag-api.md#streamtype)指定流式输出的数据类型（如思考过程、引用来源、最终答案）。

### runId；运行ID

会话内特定流式问答的唯一标识符。用于取消特定的问答任务。

### RetrievalConfig；检索配置

RAG中配置知识库连接信息的对象。包含向量数据库和倒排索引数据库的通道配置（channelConfigs），决定了检索数据源。

### RetrievalCondition；检索条件

RAG中配置检索查询和排序策略的对象。包括检索目标表（fromClause）、召回字段（responseColumns）、向量查询条件（vectorQuery）及重排方法（rerankMethod）等。

## S

### Score；评分

用户对RAG返回答案的满意度评级。取值范围：[1, 5]，用于反馈和模型优化。

### StreamType；流类型

流式问答输出数据的类型枚举。包含THOUGHT（对应取值为0）思考过程、REFERENCE（对应取值为1）引用来源、ANSWER（对应取值为2）最终答案。
