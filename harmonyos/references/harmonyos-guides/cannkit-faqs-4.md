---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-faqs-4
title: 如何处理ATC离线模型输出算子类型错误？
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > CANN Kit常见问题 > 如何处理ATC离线模型输出算子类型错误？
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:39+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:df3e28bb17195e03d6774dc353c685ef2a9512cd4603456755bd49a535f0fd48
---

Caffe网络中具有相同类型名但计算功能不同的层。比如DetectionOutput层，需要使用算子映射指明为FSRDetectionOutput、SSDDetectionOutput等检测算子类型，否则ATC生成离线模型会执行失败。为了避免出现错误，以下两种方案二选一即可。

* 方案1：可以在ATC命令中加入--op\_name\_map参数，参考[ATC参数](cannkit-overall-parameter.md)中op\_name\_map参数设置。
* 方案2：可以在原始网络proto模型文件中将输出算子类型指定为SSDDetectionOutput等算子类型，如下图所示。

  **图1** 输出算子类型修改前（左）和修改后（右）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/qRsEx2yVTBO-kD96f6T5gA/zh-cn_image_0000002817427803.png?HW-CC-KV=V1&HW-CC-Date=20261114T004838Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1DAD12036F35B243F274FD3821016EF1D9F321AB0B8B1EA2CEB725D6802774D)
