---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-process
title: ArkTS卡片进程模型
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片进程模型
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bf27b392b16e94dadc6fcbbed834e90b8fe0ada4626d540530670beddcb8377c
---

本文主要介绍，卡片从创建到显示整个过程中各个进程的含义。具体请参考卡片进程模型。

**图1** 卡片进程模型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/3FVupHvYRXuL7mzixYdOdA/zh-cn_image_0000002589324657.png)

* 卡片使用方进程：显示卡片的宿主进程，例如桌面进程。
* 卡片渲染服务进程：系统内统一加载渲染卡片UI的进程，所有卡片渲染在同一个进程内，不同的应用卡片通过虚拟机隔离。
* 卡片管理服务进程：系统内统一卡片生命周期的系统[SA](serviceability-overview.md)服务。
* 卡片提供方进程：提供卡片的应用进程，包括应用自身UIAbility运行的主进程，以及卡片单独的[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)进程。两个进程之间内存隔离，但是共享相同的文件沙箱。
