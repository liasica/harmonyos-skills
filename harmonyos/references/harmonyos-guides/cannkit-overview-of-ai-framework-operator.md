---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-overview-of-ai-framework-operator
title: AI框架算子适配概述
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 自定义算子开发 > AscendC算子开发 > AscendC算子部署 > AI框架算子适配 > AI框架算子适配概述
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:759162dd01895baf3b4da9d97437df99ad4f64262a7b6edbc538fb15510b4214
---

本章节内容介绍AI框架调用自定义算子的方法。如下图所示，PyTorch和TensorFlow仅支持图模式。

AI框架调用时，除了需要提供DDK框架调用时需要的代码实现文件，还需要对插件进行适配开发。下文仅展示通过ONNX框架进行算子适配，TensorFlow框架开发流程与ONNX框架开发流程一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/fHWYazoTRvWWAu322j_AMw/zh-cn_image_0000002791566764.png?HW-CC-KV=V1&HW-CC-Date=20261119T014918Z&HW-CC-Expire=31536000000&HW-CC-Sign=6C03CC630B76A535489E6D3530C13A8856C587626851EB4CC1DB6887AFA100FB)
