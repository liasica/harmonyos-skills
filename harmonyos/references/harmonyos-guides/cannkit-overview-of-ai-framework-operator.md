---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-overview-of-ai-framework-operator
title: AI框架算子适配概述
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 自定义算子开发 > AscendC算子开发 > AscendC算子部署 > AI框架算子适配 > AI框架算子适配概述
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dc15d2e2345321d0004b6b8edb132cfab36f638e5f07907ce41000a7579d404f
---

本章节内容介绍AI框架调用自定义算子的方法。如下图所示，PyTorch和TensorFlow仅支持图模式。

AI框架调用时，除了需要提供DDK框架调用时需要的代码实现文件，还需要对插件进行适配开发。下文仅展示通过ONNX框架进行算子适配，TensorFlow框架开发流程与ONNX框架开发流程一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/FjYI-L7sRHGKpTYOWalFUA/zh-cn_image_0000002788468378.png?HW-CC-KV=V1&HW-CC-Date=20261114T004838Z&HW-CC-Expire=31536000000&HW-CC-Sign=409FE7ACB328BB712B8BA417CB8BFCE39AC43999387765A8201E94BA1350684D)
