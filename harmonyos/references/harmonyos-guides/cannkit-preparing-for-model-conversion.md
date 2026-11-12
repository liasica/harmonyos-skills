---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-preparing-for-model-conversion
title: 模型转换前准备
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型转换 > 离线模型转换 > 模型转换前准备
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:40+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:2cc7797baea7f22a936616ee3df0c9b5a4dcc25f9175f39a37f4f5feec564462
---

CANN Kit当前仅支持Caffe、TensorFlow、ONNX和MindSpore模型转换为离线模型，其他格式的模型需要开发者自行转换为CANN Kit支持的模型格式。

1. 准备训练好的Caffe、TensorFlow、ONNX等模型。例如：[Caffe SqueezeNet V1.0](https://github.com/forresti/SqueezeNet)模型。
2. 参考[CANN工具包安装流程](cannkit-preparations.md#cann工具包安装流程)安装CANN工具包，使用CANN包中的ATC工具，将TensorFlow或Caffe模型转换为IR模型，使用方式请参见[模型转换示例](cannkit-model-conversion-example.md)。

**说明** 

若TensorFlow或Caffe模型过大，可以在ATC转换之前使用轻量化工具（tools\_dopt），使用方式请参见[模型轻量化](cannkit-lightweight-tool-overview.md)。
