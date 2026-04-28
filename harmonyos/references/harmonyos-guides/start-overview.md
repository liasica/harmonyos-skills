---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-overview
title: 开发准备
breadcrumb: 指南 > 基础入门 > 快速入门 > 开发准备
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8121225e770d211ddacdc7c88aff5cd34bfb6f9709ff9ef33f2388cf0ae06434
---

本文档适用于HarmonyOS应用开发的初学者。通过构建一个简单的具有页面跳转/返回功能的应用（如下图所示），快速了解工程目录的主要文件，熟悉HarmonyOS应用开发流程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/tpn7m8m7RQy5yTPtaNRzjw/zh-cn_image_0000002552957468.png?HW-CC-KV=V1&HW-CC-Date=20260427T233723Z&HW-CC-Expire=86400&HW-CC-Sign=DBFBAEC76D13A5A20A2AB75C7D6C96935E95742DF4D5A9DD3B8497886C8F36E4)

在开始之前，您需要了解有关HarmonyOS应用的一些基本概念：UI框架的简单说明、应用模型的基本概念。

## 基本概念

### UI框架

HarmonyOS提供了一套UI开发框架，即方舟开发框架（ArkUI框架）。方舟开发框架可为开发者提供应用UI开发所必需的能力，比如多种组件、布局计算、动画能力、UI交互、绘制等。

方舟开发框架针对不同目的和技术背景的开发者提供了两种开发范式，分别是基于ArkTS的声明式开发范式（简称“声明式开发范式”）和兼容JS的类Web开发范式（简称“类Web开发范式”）。以下是两种开发范式的简单对比。

| **开发范式名称** | **语言生态** | **UI更新方式** | **适用场景** | **适用人群** |
| --- | --- | --- | --- | --- |
| 声明式开发范式 | ArkTS语言 | 数据驱动更新 | 复杂度较大、团队合作度较高的程序 | 移动系统应用开发人员、系统应用开发人员 |
| 类Web开发范式 | JS语言 | 数据驱动更新 | 界面较为简单的程序应用和卡片 | Web前端开发人员 |

更多UI框架的开发内容及指导，详见[UI开发](arkui-overview.md)。

### 应用模型

应用模型是HarmonyOS为开发者提供的应用程序所需能力的抽象提炼，它提供了应用程序必备的组件和运行机制。有了应用模型，开发者可以基于一套统一的模型进行应用开发，使应用开发更简单、高效。

随着系统的演进发展，HarmonyOS先后提供了两种应用模型：

* **FA（Feature Ability）模型：** HarmonyOS API 7开始支持的模型，已经不再主推。FA模型开发可见[FA模型开发概述](fa-model-development-overview.md)。**快速入门章节不再详细说明此模型**。
* **Stage模型：** HarmonyOS API 9开始新增的模型，是目前主推且会长期演进的模型。在该模型中，由于提供了AbilityStage、WindowStage等类作为应用组件和Window窗口的“舞台”，因此称这种应用模型为Stage模型。Stage模型开发可见[Stage模型开发概述](stage-model-development-overview.md)。**快速入门以此为例提供开发指导。**

FA模型和Stage模型的整体架构和设计思想等更多区别，请见[应用模型](application-models.md)。

快速入门提供了一个含有两个页面的开发实例，并基于Stage模型构建第一个ArkTS应用，以便开发者理解以上基本概念及应用开发流程。

## 工具准备

请下载并安装[最新版DevEco Studio](https://developer.huawei.com/consumer/cn/download/)，具体可参照[下载与安装DevEco Studio](ide-software-install.md)，更多工具使用指导可见[工具概述](ide-tools-overview.md)。

完成上述操作及基本概念的理解后，可参照[构建第一个HarmonyOS应用（ArkTS）](start-with-ets-stage.md)进行下一步体验和学习。
