---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-augmentation-rag-overview
title: RAG概述
breadcrumb: 指南 > 应用框架 > Data Augmentation Kit（数据增强服务） > RAG > RAG概述
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a4b2d6a5a2f9bf16e90fedc6529fcbb9dab685b476fcfd4014cb838809d211e7
---

RAG（Retrieval-Augmented Generation，检索增强生成）融合了智能检索与知识库技术，通过知识库驱动内容生成，具备强大的可解释性和深度定制能力。应用可通过接入Data Augmentation Kit提供的[RAG](../harmonyos-references/dataaugmentation-rag-api.md)能力，快速实现知识问答、智慧助手等业务场景。本模块还支持通过模板灵活配置RAG运行的核心参数，实现全流程的深度定制。

其工作原理为：请求大语言模型解析用户问题，智能检索知识库内容，最终由大模型融合检索结果并生成自然流畅的回复。下文将以流式的知识问答场景为例，详细说明RAG的使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/PHeTSvbMQxGGsvhUTMkMVg/zh-cn_image_0000002712404344.png)
