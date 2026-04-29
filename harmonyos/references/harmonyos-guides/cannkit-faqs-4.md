---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-faqs-4
title: 如何处理OMG离线模型输出算子类型错误？
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > CANN Kit常见问题 > 如何处理OMG离线模型输出算子类型错误？
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:39ee14f11c34f98125f85759dd83d43a18853b1e7c2352dc72fcf5d546d466ae
---

Caffe网络中具有相同类型名但计算功能不同的层。比如DetectionOutput层，需要使用算子映射指明为FSRDetectionOutput、SSDDetectionOutput等检测算子类型，否则OMG生成离线模型会执行失败。为了避免出现错误，以下两种方案二选一即可。

* 方案1：可以在OMG命令中加入--op\_name\_map参数，参考[OMG参数](cannkit-overall-parameter.md)中op\_name\_map参数设置。
* 方案2：可以在原始网络proto模型文件中将输出算子类型指定为SSDDetectionOutput等算子类型，如下图所示。

  **图1** 输出算子类型修改前（左）和修改后（右）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/4DN3VYHIQpKYeZVghTTqjw/zh-cn_image_0000002558606138.png?HW-CC-KV=V1&HW-CC-Date=20260429T054302Z&HW-CC-Expire=86400&HW-CC-Sign=92E70D1184D87948BA20071443D806D57ECE8BF73DDA0913858AB06F732525E2)
