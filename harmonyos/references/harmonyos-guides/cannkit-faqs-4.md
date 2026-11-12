---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-faqs-4
title: 如何处理ATC离线模型输出算子类型错误？
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > CANN Kit常见问题 > 如何处理ATC离线模型输出算子类型错误？
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:05c2c70eac9e0477d33953a410e5918d7416341e710139b231a66591f6aba391
---

Caffe网络中具有相同类型名但计算功能不同的层。比如DetectionOutput层，需要使用算子映射指明为FSRDetectionOutput、SSDDetectionOutput等检测算子类型，否则ATC生成离线模型会执行失败。为了避免出现错误，以下两种方案二选一即可。

* 方案1：可以在ATC命令中加入--op\_name\_map参数，参考[ATC参数](cannkit-overall-parameter.md)中op\_name\_map参数设置。
* 方案2：可以在原始网络proto模型文件中将输出算子类型指定为SSDDetectionOutput等算子类型，如下图所示。

  **图1** 输出算子类型修改前（左）和修改后（右）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/k8Ie2kGZQ-C4mROB7OPK_g/zh-cn_image_0000002815400211.png?HW-CC-KV=V1&HW-CC-Date=20261112T233224Z&HW-CC-Expire=31536000000&HW-CC-Sign=82916757245218CEB9DD40918E30C80F032B0A3DCF6083209CCA0E94BFB276A2)
