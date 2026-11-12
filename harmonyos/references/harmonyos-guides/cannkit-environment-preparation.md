---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-environment-preparation
title: 环境准备
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 自定义算子开发 > AscendC算子开发 > 环境准备
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:41+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b4c008b8f471cb7a6f4c8c4cacc6368b7c33bdc20aa269156753b29775590164
---

进行环境准备前，你需要了解如下基本概念，以便更好的理解后续操作。

* 开发环境：指编译开发代码的环境。
* 运行环境：指运行算子、推理程序等的Linux环境。运行环境必须连接上带有Kirin AI处理器的设备，如手机、平板等。
* 开发环境与运行环境合设场景：开发环境和运行环境在同一台机器上，开发者使用连接上Kirin AI处理器的机器作为运行环境，同时在该环境上进行代码开发与编译。
* 开发环境与运行环境分设场景：开发环境和运行环境不在同一台机器上，开发者使用连接上Kirin AI处理器的机器作为运行环境；使用其他独立机器进行代码开发与编译，作为开发环境。

  **说明** 

  开发运行环境需要满足以下要求：

  + ubuntu版本不低于22.04，ubuntu架构为x86\_64， python版本不低于3.7，gcc/g++版本不低于7.3.0。
  + 设备连接与调试参考[hdc](hdc.md)。

进行自定义算子开发前，请参考完成[环境准备](https://gitcode.com/cann/cann-recipes-harmony-infer/blob/master/docs/quick_install.md)。
