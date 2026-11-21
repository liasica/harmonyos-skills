---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-overview-of-ai-framework-operator
title: AI框架算子适配概述
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 自定义算子开发 > AscendC算子开发 > AscendC算子部署 > AI框架算子适配 > AI框架算子适配概述
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b638c9b408844465f65ee839f35519ca44ca18bc1a1ccf149fbc7004c92d6ca3
---

本章节内容介绍AI框架调用自定义算子的方法。如下图所示，PyTorch和TensorFlow仅支持图模式。

AI框架调用时，除了需要提供DDK框架调用时需要的代码实现文件，还需要对插件进行适配开发。下文仅展示通过ONNX框架进行算子适配，TensorFlow框架开发流程与ONNX框架开发流程一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/sBj1tVNhQFWrAf9G1IPv3A/zh-cn_image_0000002792878418.png?HW-CC-KV=V1&HW-CC-Date=20261121T011117Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C549E2E3441929AAF0AA189E62EDD1667341954A5D39DBBAE9DF89818D9D0B8)
