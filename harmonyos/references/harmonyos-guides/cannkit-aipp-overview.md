---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-aipp-overview
title: 概述
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型转换 > AIPP > 概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5f437e052d252342c4ff3f826b3343c2923f2ea97ef822577a28e83bbec40f6d
---

AIPP(AI Pre-Process)是针对AI推理的输入数据进行预处理的模块。CANN模型推理一般需要标准化输入数据格式，而一般模型推理场景数据是一张图片，在格式上存在多样性，AIPP可实现不同格式图片数据到NPU标准输入数据格式的转换。对已训练好的模型，不用重新训练匹配推理计算平台需要的数据格式，而只通过AIPP参数配置或者在软件上调用AIPP接口即可完成适配。由于AIPP硬件专用，可以获得较好的推理性能收益，又可以称为“硬件图像预处理”。
