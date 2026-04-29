---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-zero-memory-copy
title: 内存零拷贝
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 端侧部署 > 内存零拷贝
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1168d6e44500c75e70eece3e1f2d1591fb7c0ec2f6cab5aeb2927dd52e7dc51c
---

## 概述

对于GPU的纹理数据或模型的输入数据等已经存在于ION内存中的场景，就可以使用“内存零拷贝方式”，即将存放数据的ION内存封装为输入输出张量，直接进行推理，不需要进行输入张量和输出张量的数据拷贝，以便节省内存以及推理时间。

## 使用说明

对于零拷贝使用场景，在模型加载完成后，使用[OH\_NNTensor\_CreateWithFd](../harmonyos-references/capi-neural-network-core-h.md#oh_nntensor_createwithfd)，将ION内存封装为输入张量“input\_tensor”，输出张量"output\_tensor"，执行推理。

说明

若size为模型输出大小，对于输出张量，建议开发者申请ION内存的大小为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/L_Uvuox9ROaeI52fa_4ckw/zh-cn_image_0000002558606066.png?HW-CC-KV=V1&HW-CC-Date=20260429T054058Z&HW-CC-Expire=86400&HW-CC-Sign=F2DB0A8B55D13F90156D6BFC8AF9EA8EE87D43F8B37C350CC27DB31A58B7829D)。
