---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-faqs-4
title: 如何处理OMG离线模型输出算子类型错误？
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dbdb5ec4f0c8f08c67cbbac3ca608f6f00ea84e1b0130e4234d658c444e2d1d4
---

Caffe网络中具有相同类型名但计算功能不同的层。比如DetectionOutput层，需要使用算子映射指明为FSRDetectionOutput、SSDDetectionOutput等检测算子类型，否则OMG生成离线模型会执行失败。为了避免出现错误，以下两种方案二选一即可。

* 方案1：可以在OMG命令中加入--op\_name\_map参数，参考[OMG参数](cannkit-overall-parameter.md)中op\_name\_map参数设置。
* 方案2：可以在原始网络proto模型文件中将输出算子类型指定为SSDDetectionOutput等算子类型，如下图所示。

  **图1** 输出算子类型修改前（左）和修改后（右）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/yk-AGJ-NTgejOl5yAlasAA/zh-cn_image_0000002552799644.png?HW-CC-KV=V1&HW-CC-Date=20260427T235322Z&HW-CC-Expire=86400&HW-CC-Sign=8B5B98E5CC4C5C8374CBF70D31CB42DBF47BBFB5C64362CF36B40708AB81B2C5)
