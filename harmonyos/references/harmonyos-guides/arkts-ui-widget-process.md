---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-process
title: ArkTS卡片进程模型
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片进程模型
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:18+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:33b2189cedb5955f6ee4ab53024659d663f5a4bb1269df6153a7d14623b48f68
---

本文主要介绍，卡片从创建到显示整个过程中各个进程的含义。具体请参考卡片进程模型。

**图1** 卡片进程模型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/Z4Q3ErmFQFKf6WTh5_n7Zw/zh-cn_image_0000002817506689.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=B58AEAA4410CA56106C5851AADFF6B8360B5A952DBAC9A6329128BD2B4A1EE20)

* 卡片使用方进程：显示卡片的宿主进程，例如桌面进程。
* 卡片渲染服务进程：系统内统一加载渲染卡片UI的进程，所有卡片渲染在同一个进程内，不同的应用卡片通过虚拟机隔离。
* 卡片管理服务进程：系统内统一卡片生命周期的系统[SA](../lite-wearable-guides/serviceability-overview.md)服务。
* 卡片提供方进程：提供卡片的应用进程，包括应用自身UIAbility运行的主进程，以及卡片单独的[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)进程。两个进程之间内存隔离，但是共享相同的文件沙箱。
