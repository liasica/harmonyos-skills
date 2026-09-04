---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-faqs-4
title: 如何处理OMG离线模型输出算子类型错误？
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > CANN Kit常见问题 > 如何处理OMG离线模型输出算子类型错误？
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:47a0f21c993d2460a4626b02af5871ea0dd8cb38a8bc05dbab5ab24c441d94c2
---

Caffe网络中具有相同类型名但计算功能不同的层。比如DetectionOutput层，需要使用算子映射指明为FSRDetectionOutput、SSDDetectionOutput等检测算子类型，否则OMG生成离线模型会执行失败。为了避免出现错误，以下两种方案二选一即可。

* 方案1：可以在OMG命令中加入--op\_name\_map参数，参考[OMG参数](cannkit-overall-parameter.md)中op\_name\_map参数设置。
* 方案2：可以在原始网络proto模型文件中将输出算子类型指定为SSDDetectionOutput等算子类型，如下图所示。

  **图1** 输出算子类型修改前（左）和修改后（右）

  ![](https://media:401788444070548638)
