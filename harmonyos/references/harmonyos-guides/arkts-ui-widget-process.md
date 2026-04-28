---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-process
title: ArkTS卡片进程模型
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片进程模型
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:01dbefd470fa12ed1fed696573244548fb559993bf34d8d27254db8f4bb636a5
---

本文主要介绍，卡片从创建到显示整个过程中各个进程的含义。具体请参考卡片进程模型。

**图1** 卡片进程模型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/Hd5cr3E8ROi14flAg1kMfg/zh-cn_image_0000002552958290.png?HW-CC-KV=V1&HW-CC-Date=20260427T234125Z&HW-CC-Expire=86400&HW-CC-Sign=258EF582C8D27F5DD3AA79AD799884057207B3C0A7302A95FBEAF694465433D5)

* 卡片使用方进程：显示卡片的宿主进程，例如桌面进程。
* 卡片渲染服务进程：系统内统一加载渲染卡片UI的进程，所有卡片渲染在同一个进程内，不同的应用卡片通过虚拟机隔离。
* 卡片管理服务进程：系统内统一卡片生命周期的系统[SA](serviceability-overview.md)服务。
* 卡片提供方进程：提供卡片的应用进程，包括应用自身UIAbility运行的主进程，以及卡片单独的[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)进程。两个进程之间内存隔离，但是共享相同的文件沙箱。
