---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-add-new-ability
title: 在模块中添加Ability
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 在模块中添加Ability
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f5433f9b9b3a5b165a90cd4c64c85ea9869ee049d8f087df1d328d12730eeb1e
---

Ability是应用/元服务所具备的能力的抽象，应用的一个Module可以包含一个或多个Ability，元服务仅包含一个Ability。应用/元服务先后提供了两种应用模型：

* FA（Feature Ability）模型： API 7开始支持的模型，已经不再主推。
* Stage模型：HarmonyOS 3.1 Developer Preview版本开始新增的模型，是目前主推且会长期演进的模型。在该模型中，由于提供了AbilityStage、WindowStage等类作为应用组件和Windows窗口的“舞台”，因此称这种应用模型为Stage模型。

  Stage模型包含两种Ability组件类型：

  + UIAbility组件：包含UI界面，提供展示UI的能力，主要用于和用户交互。详细介绍请参见[UIAbility组件概述](uiability-overview.md)。
  + ExtensionAbility组件：提供特定场景的扩展能力，满足更多的使用场景。详细介绍请参见[ExtensionAbility概述](extensionability-overview.md)。元服务暂不支持使用ExtensionAbility组件。

从DevEco Studio 6.1.0 Beta2版本开始，在API 23及以上工程，支持Car设备添加RemoteNotificationAbility。

## Stage模型添加Ability

### 在模块中添加UIAbility

1. 选中对应的模块，单击鼠标右键，选择**New > Ability**。
2. 设置Ability名称，选择是否在设备主屏幕上显示该功能的启动图标，单击**Finish**完成Ability创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/PxcGZJ5ERsGdXaQns4n9jg/zh-cn_image_0000002561753721.png?HW-CC-KV=V1&HW-CC-Date=20260427T235455Z&HW-CC-Expire=86400&HW-CC-Sign=D0031C875ABBE39025479EC7EEBC7D40E3E792ABB5A9528731CCB13110FB0CCC)

### 在模块中添加Extension Ability

1. 在工程中选中对应的模块，单击鼠标右键，选择**New > Extension Ability**，选择不同的场景类型 。当前仅Application工程支持创建Extension Ability。
   * 若创建的模块类型为entry或feature，支持创建以下五种Extension Ability：
     + **EmbeddedUIExtensionAbility**：用于提供[跨进程界面嵌入](embeddeduiextensionability.md)的能力。
     + **Backup****Ability**：用于提供[备份及恢复应用数据](app-file-backup-overview.md)的能力。
     + **WorkScheduler**：用于提供[延迟任务](work-scheduler.md)的相关能力。
     + **RemoteNotificationAbility**：用于提供获取场景化消息数据和生命周期销毁的回调的通知能力，当前仅支持在Phone、Tablet、2in1、Car设备中使用。
     + **Driver**：用于提供[驱动相关扩展框架](driverextensionability.md)。仅在当前工程的设备类型只含有2in1设备时，支持创建该类型。
   * 若创建的模块类型为HAR或HSP，支持创建以下两种Extension Ability：
     + **EmbeddedUIExtensionAbility**：用于提供[跨进程界面嵌入](embeddeduiextensionability.md)的能力。
     + **WorkScheduler**：用于提供[延迟任务](work-scheduler.md)的相关能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/GUH-L9IoSgqbAr4jpZm0MQ/zh-cn_image_0000002561833697.png?HW-CC-KV=V1&HW-CC-Date=20260427T235455Z&HW-CC-Expire=86400&HW-CC-Sign=9C5A8744413AC58EC79FB56D01027F18CD4CEB72BF59C0958A113C6DAF7BFC73)
2. 设置Ability名称，单击Finish完成Extension Ability创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/p9Icw9OQRim_acjWu8vs3Q/zh-cn_image_0000002530913772.png?HW-CC-KV=V1&HW-CC-Date=20260427T235455Z&HW-CC-Expire=86400&HW-CC-Sign=953AC8892E96684EBC05B9D6E58875CBC56DEBA6FC6FC8F380295B09CF249AB8)

## FA模型添加Ability

ArkTS工程与JS工程在FA模型中添加Ability的操作方式一致，本节内容以ArkTS工程为例介绍在模块中添加Ability。

### 创建Particle Ability

1. 选中对应的模块，单击鼠标右键，选择**New > Ability** ，然后选择对应的Data Ability/Service Ability模板。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/YjmOKSD1R_6_qHoSm9a4qg/zh-cn_image_0000002530913774.png?HW-CC-KV=V1&HW-CC-Date=20260427T235455Z&HW-CC-Expire=86400&HW-CC-Sign=7363DBFA92E7065DEDA75245C417E6257EF7A530D9346158A2E2EA7777AB97A2)
2. 根据选择的Ability模板，设置Ability的基本信息。
   * **Ability name**：Ability类名称，由大小写字母、数字和下划线组成。
   * **Language**：该Ability使用的开发语言。
3. 单击**Finish**完成Ability的创建，可以在工程目录对应的模块中查看和编辑Ability。

### 创建Feature Ability

1. 选中对应的模块，单击鼠标右键，选择**New > Ability** ，然后选择对应的Page Ability模板。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/5bKsiMB0QE6jqZnkceQzpQ/zh-cn_image_0000002561833701.png?HW-CC-KV=V1&HW-CC-Date=20260427T235455Z&HW-CC-Expire=86400&HW-CC-Sign=D0725CD528CAA2BE703FCC76CC76AFE1F976F00A6FB388D6D83C65A35524B45F)
2. 根据选择的Ability模板，设置Ability的基本信息。
   * **Ability name**：Ability类名称，由大小写字母、数字和下划线组成。
   * **Launcher ability**：表示该Ability在终端桌面上是否有启动图标，一个HAP可以有多个启动图标，来启动不同的FA。
   * **Language**：该Ability使用的开发语言。
3. 单击**Finish**完成Ability的创建，可以在工程目录对应的模块中查看和编辑Ability。
