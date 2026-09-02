---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-add-new-ability
title: 添加Ability
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 添加Ability
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:140fc38a43eebf961f0543678d6502aa121a1f68aac1d1ae82b9ac31604e33a4
---

Ability是应用/元服务所具备的能力的抽象，应用的一个Module可以包含一个或多个Ability，元服务仅包含一个Ability。应用/元服务先后提供了两种应用模型：

* FA（Feature Ability）模型： API 7开始支持的模型，已经不再主推。
* Stage模型：HarmonyOS 3.1 Developer Preview版本开始新增的模型，是目前主推且会长期演进的模型。在该模型中，由于提供了AbilityStage、WindowStage等类作为应用组件和Windows窗口的“舞台”，因此称这种应用模型为Stage模型。

  Stage模型包含两种Ability组件类型：

  + UIAbility组件：包含UI界面，提供展示UI的能力，主要用于和用户交互。详细介绍请参见[UIAbility组件概述](uiability-overview.md)。
  + ExtensionAbility组件：提供特定场景的扩展能力，满足更多的使用场景。详细介绍请参见[ExtensionAbility概述](extensionability-overview.md)。元服务暂不支持使用ExtensionAbility组件。

## Stage模型添加Ability

### 在模块中添加UIAbility

1. 选中对应的模块，单击鼠标右键，选择**New > Ability**。
2. 设置Ability名称，选择是否在设备主屏幕上显示该功能的启动图标，单击**Finish**完成Ability创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/6hO8b_gsSs2_zsx6df18qw/zh-cn_image_0000002731383137.png)

### 在模块中添加Extension Ability

从DevEco Studio 6.1.0 Beta2版本开始，支持在API 23及以上Car设备工程的模块中添加RemoteNotificationAbility。

从26.0.0版本开始，支持在API 26.0.0及以上工程的模块中添加Agent、AgentUI。

1. 在工程中选中对应的模块，单击鼠标右键，选择**New > Extension Ability**，选择不同的场景类型 。当前仅Application工程支持创建Extension Ability。
   * 若创建的模块类型为HAP，支持创建如下Extension Ability：
     + **EmbeddedUIExtensionAbility**：用于提供[跨进程界面嵌入](embeddeduiextensionability.md)的能力。
     + **Backup****Ability**：用于提供[备份及恢复应用数据](app-file-backup-overview.md)的能力。
     + **WorkScheduler**：用于提供[延迟任务](work-scheduler.md)的相关能力。
     + **RemoteNotificationAbility**：用于提供获取场景化消息数据和生命周期销毁的回调的通知能力，当前仅支持在Phone、Tablet、2in1、Car设备中使用。
     + **Driver**：用于提供[驱动相关扩展框架](driverextensionability.md)。仅在当前工程的设备类型只含有2in1设备时，支持创建该类型。
     + **Agent：**用于提供[智能体扩展](agent-extension-ability.md)的能力。
     + **A****gentUI****：**用于提供[接入端侧Agent UI界面显示](../harmonyos-references/js-apis-agent-agentuiextensionability.md)的能力。
   * 若创建的模块类型为HAR或HSP，支持创建以下两种Extension Ability：
     + **EmbeddedUIExtensionAbility**：用于提供[跨进程界面嵌入](embeddeduiextensionability.md)的能力。
     + **WorkScheduler**：用于提供[延迟任务](work-scheduler.md)的相关能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/UqdFGbmcTt-o-v9vFi4ncA/zh-cn_image_0000002731543109.png)
2. 设置Ability名称，单击Finish完成Extension Ability创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/AhpSYS0CQUav7wmpZ_t6KA/zh-cn_image_0000002731383135.png)

## FA模型添加Ability

### 创建Particle Ability

1. 选中对应的模块，单击鼠标右键，选择**New > Ability** ，然后选择对应的Data Ability/Service Ability模板。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/XTpQ_1ADTw2kUyUQRfHqcg/zh-cn_image_0000002701823836.png)
2. 根据选择的Ability模板，设置Ability的基本信息。
   * **Ability name**：Ability类名称，由大小写字母、数字和下划线组成。
   * **Language**：该Ability使用的开发语言。
3. 单击**Finish**完成Ability的创建，可以在工程目录对应的模块中查看和编辑Ability。

### 创建Feature Ability

1. 选中对应的模块，单击鼠标右键，选择**New > Ability** ，然后选择对应的Page Ability模板。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/yt151sLZTjKrkg0JR9TqlQ/zh-cn_image_0000002701663910.png)
2. 根据选择的Ability模板，设置Ability的基本信息。
   * **Ability name**：Ability类名称，由大小写字母、数字和下划线组成。
   * **Launcher ability**：表示该Ability在终端桌面上是否有启动图标，一个HAP可以有多个启动图标，来启动不同的FA。
   * **Language**：该Ability使用的开发语言。
3. 单击**Finish**完成Ability的创建，可以在工程目录对应的模块中查看和编辑Ability。
