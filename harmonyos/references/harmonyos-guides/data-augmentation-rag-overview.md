---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-augmentation-rag-overview
title: RAG概述
breadcrumb: 指南 > 应用框架 > Data Augmentation Kit（数据增强服务） > RAG > RAG概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1d62734920c9ac5c8b6cba6c9057930c861bcb73e1de12cd5e76b5fd5ef4b593
---

RAG（Retrieval-Augmented Generation，检索增强生成）融合了智能检索与知识库技术，通过知识库驱动内容生成，具备强大的可解释性和深度定制能力。应用可通过接入Data Augmentation Kit提供的[RAG](../harmonyos-references/dataaugmentation-rag-api.md)能力，快速实现知识问答、智慧助手等业务场景。本模块还支持通过模板灵活配置RAG运行的核心参数，实现全流程的深度定制。

其工作原理为：请求大语言模型解析用户问题，智能检索知识库内容，最终由大模型融合检索结果并生成自然流畅的回复。下文将以流式的知识问答场景为例，详细说明RAG的使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/ae2i5j6FT06X5fNH__FbCw/zh-cn_image_0000002558764780.png?HW-CC-KV=V1&HW-CC-Date=20260429T052948Z&HW-CC-Expire=86400&HW-CC-Sign=6EB1A3B72080E727333FA692C0FFCFBC0060851BAFD5A372763A2999DBA2FDFE)
