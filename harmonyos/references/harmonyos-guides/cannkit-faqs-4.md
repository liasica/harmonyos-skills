---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-faqs-4
title: 如何处理ATC离线模型输出算子类型错误？
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > CANN Kit常见问题 > 如何处理ATC离线模型输出算子类型错误？
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:46+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:af99875a8eeb0fe64f6a61081e1217273c2d8bb5bcc5113c7e3e35c9d1b56d37
---

Caffe网络中具有相同类型名但计算功能不同的层。比如DetectionOutput层，需要使用算子映射指明为FSRDetectionOutput、SSDDetectionOutput等检测算子类型，否则ATC生成离线模型会执行失败。为了避免出现错误，以下两种方案二选一即可。

* 方案1：可以在ATC命令中加入--op\_name\_map参数，参考[ATC参数](cannkit-overall-parameter.md)中op\_name\_map参数设置。
* 方案2：可以在原始网络proto模型文件中将输出算子类型指定为SSDDetectionOutput等算子类型，如下图所示。

  **图1** 输出算子类型修改前（左）和修改后（右）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/53OP-0pdQdW2tanFUoHoXA/zh-cn_image_0000002793038394.png?HW-CC-KV=V1&HW-CC-Date=20261121T011246Z&HW-CC-Expire=31536000000&HW-CC-Sign=5945A128208F5ED145F4A10B071937FB589CA95D7DE5F30752C076EDECAC63CE)
