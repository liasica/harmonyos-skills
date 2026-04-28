---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-overview-of-ai-framework-operator
title: AI框架算子适配概述
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子部署 > AI框架算子适配 > AI框架算子适配概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c4d535b0279dcaaa430948bd3628fb908ab6b4ed9cebc461758ac7a40a354f73
---

本章节内容介绍AI框架调用自定义算子的方法。如下图所示，PyTorch和TensorFlow仅支持图模式。

AI框架调用时，除了需要提供DDK框架调用时需要的代码实现文件，还需要对插件进行适配开发。下文仅展示通过ONNX框架进行算子适配，TensorFlow框架开发流程与ONNX框架开发流程一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/oDVtFMn1T_aPs1vsX8lbsw/zh-cn_image_0000002583439297.png?HW-CC-KV=V1&HW-CC-Date=20260427T235132Z&HW-CC-Expire=86400&HW-CC-Sign=D49969CC32EA2D1E175793CEC849536CBBEFD63CA4559637F5E2B06B6E6D4F5D)
