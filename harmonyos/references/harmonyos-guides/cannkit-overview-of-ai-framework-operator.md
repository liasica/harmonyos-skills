---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-overview-of-ai-framework-operator
title: AI框架算子适配概述
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 自定义算子开发 > AscendC算子开发 > AscendC算子部署 > AI框架算子适配 > AI框架算子适配概述
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:34d8e98801f9dbee1039dcc12f608d99a19f69f4060ddaa21efbbdb94ba94c3a
---

本章节内容介绍AI框架调用自定义算子的方法。如下图所示，PyTorch和TensorFlow仅支持图模式。

AI框架调用时，除了需要提供DDK框架调用时需要的代码实现文件，还需要对插件进行适配开发。下文仅展示通过ONNX框架进行算子适配，TensorFlow框架开发流程与ONNX框架开发流程一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/kDLwEwyrTW6_z2ZCSeChhQ/zh-cn_image_0000002786520630.png?HW-CC-KV=V1&HW-CC-Date=20261112T233225Z&HW-CC-Expire=31536000000&HW-CC-Sign=A686A25315D502D878237BD0E0CE7D6A8F46B25F4082D2C7C696D079A40AAEA4)
