---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/multi-communication-app
title: 多设备即时通讯界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备即时通讯界面
category: best-practices
scraped_at: 2026-09-02T15:03:19+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:a9be8e00e71285e7d3b4573ddd0734a2a58d475dd48aae8d75f521cfeeb31934
---

## 概述

本文从当前常见的多设备应用场景中，选取即时通讯行业应用作为典型案例，详细介绍”一多”在实际开发中的应用。

即时通讯应用的核心功能是用户交互，主要功能模块包含对话聊天、通讯录和社交圈等交互功能。开发者在开发”一多”应用时，经常面临多端适配问题。本文针对即时通讯应用的常见多端适配问题，提供解决方案。

应用当前已适配的设备包括：直板机、双折叠（Mate X系列）、三折叠、阔折叠、平板和电脑。

**说明** 

阅读本文前，开发者需熟悉[ArkUI（方舟UI框架）](../harmonyos-guides/arkui.md)和[一次开发，多端部署概览](bpta-multi-device-overview.md)相关知识。

下文将从UX设计、工程管理、页面开发三个角度，介绍即时通讯应用在多设备开发中的最佳实践。

* [UX设计](multi-communication-app.md#section18771832172516)：介绍即时通讯应用的交互逻辑和通用设计要点，对于类似的设计要点，开发者可以直接参考。
* [工程管理](multi-communication-app.md#section73711812196)：推荐“一多”项目采用分层架构，明确各层逻辑。同时，介绍即时通讯应用适用的三层架构配置。
* [移动端页面](multi-communication-app.md#section202931220101020)和[电脑端页面](multi-communication-app.md#section5748352172710)：遵循实际应用开发流程，以页面为基本单元，逐项讲解各页面在窗口适配、页面开发的设计思路与实现方法。

## UX设计

即时通讯应用的UX设计可参考社交通讯类多设备响应式设计指南的[社交通讯类](../design-guides/responsive-design-examples2-0000001793536901.md)章节，设计参考图如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/Ins5WeZDTIi-u9fzlKzQSA/zh-cn_image_0000002579689282.png "点击放大")

## 工程管理

考虑到“一多”工程代码的复用性和可维护性，推荐开发者使用分层架构组织代码工程。分层架构将项目工程划分为产品定制层（products）、基础特性层（features）和公共能力层（common）三个层级，各层级权责明确且功能独立，为开发者提供了一套清晰、高效且可扩展的设计架构。关于分层架构的具体设计细节，可参考[分层架构设计](bpta-layered-architecture-design.md)。

### 创建工程

建议开发者参考[多设备工程部署与发布](bpta-multi-device-ide.md)相关内容，掌握分层架构工程的创建与配置方法后，创建出模板项目工程。然后根据即时通讯应用的开发需求进行针对性修改，确保工程架构贴合实际业务需求。

### 工程结构

即时通讯应用根据推荐的分层架构按照products、features、common三个层级组织代码工程。每个层级的设计如下：

* products层：即时通讯应用需要适配的设备包括直板机、双折叠（Mate X系列）、三折叠、阔折叠、平板和电脑。由于电脑设备的界面布局与其他设备差异较大，因此在products层单独创建名称为“pc”的HAP包作为电脑端的应用入口；而直板机、双折叠（Mate X系列）、三折叠、阔折叠和平板设备上的界面布局整体相似，部分差异可以通过“一多”的[自适应布局](bpta-multi-device-adaptive-layout.md)和[响应式布局](bpta-multi-device-responsive-layout.md)进行适配，因此在products层创建一个名称为“default”的HAP包作为这些设备的应用入口。
* features层：即时通讯应用主要包含三个核心业务模块，分别是消息（message）、社交（social）和用户详情（user）。在features层为三个业务模块分别创建对应的HAR包，供products层按需引用。三个业务模块相对独立，互不依赖，便于后续维护与迭代。
* common层：为实现代码复用、减少冗余，在common层集中存放公共常量、路由跳转工具以及窗口管理工具等需要被多个模块共用的基础能力，供其他模块统一调用。

工程结构如下：

```screen
├──common
│  └──commonmultidevicecommunication                                     
│     └──src/main
│        ├──ets
│        │  ├──constants                      // 公共常量定义
│        │  ├──model                          // 公共model定义
│        │  ├──utils                          // 工具类
│        │  └──view                           // feature公共业务组件
│        └──resources                         // 公共资源
├──features                                   
│  ├──commonui                                // products公共业务组件模块
│  │  └──src/main
│  │     ├──ets
│  │     │  └──view                           // products公共业务组件
│  │     └──resources                         // 静态路由表资源
│  ├──message                                 // 消息模块
│  │  └──src/main
│  │     ├──ets
│  │     │  ├──model                          // 消息模块数据模型
│  │     │  ├──view                           // 消息模块组件
│  │     │  └──viewmodel                      // 消息模块视图模型
│  │     └──resources                         // 消息模块资源
│  ├──social                                  // 社交模块
│  │  └──src/main
│  │     ├──ets
│  │     │  ├──model                          // 社交模块数据模型
│  │     │  ├──view                           // 社交模块组件
│  │     │  └──viewmodel                      // 社交模块视图模型
│  │     └──resources                         // 社交模块资源
│  └──user                                    // 个人主页模块
│     └──src/main
│        ├──ets
│        │  ├──model                          // 个人主页模块数据模型
│        │  ├──view                           // 个人主页模块组件
│        │  └──viewmodel                      // 个人主页模块视图模型
│        └──resources                         // 个人主页模块资源
└──products                                    
  ├──default                                  // 手机/平板设备
  │  └──src/main
  │     ├──ets
  │     │  ├──entryability                    // 入口类
  │     │  ├──entrybackupability              // 应用数据备份恢复自定义拓展类
  │     │  └──pages                           // 入口页面
  │     └──resources                          // 资源文件
  └──pc                                       // PC设备
    └──src/main
       ├──ets
       │  ├──pages                           // 入口页面
       │  ├──pcability                       // 入口类
       │  └──pcbackupability                 // 应用数据备份恢复自定义拓展类
       └──resources                          // 资源文件
```

## 移动端页面

本章介绍如何针对直板机、双折叠（Mate X系列）、三折叠、阔折叠和平板设备上的即时通讯应用，使用“一多”布局能力，实现页面层级“一套代码、多端适配”的目标。同时，介绍这些设备上的窗口适配方案。

### 窗口适配

* 窗口模式

  适配设备支持全屏、分屏、悬浮窗和自由窗口模式，具体参见[窗口模式](bpta-multi-device-window-mode.md)。其中，分屏模式与悬浮窗通常无特殊设计，可通过系统方式进入。应用内监听窗口尺寸变化，[通过断点刷新UI](bpta-multi-device-responsive-layout.md#section175001836203617)，即可自动适配全屏、分屏、悬浮窗、自由窗口模式下的布局。
* 窗口方向

  可以通过[window.setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)设置窗口方向显示类型。窗口方向包含四种类型，分别是竖屏、横屏、反向竖屏和反向横屏。相关内容可参考[窗口方向](bpta-multi-device-window-direction.md)。在即时通讯应用中，通过module.json5配置文件，建议设置为FOLLOW\_DESKTOP。
* 窗口沉浸式

  根据UX设计，需要实现不同窗口模式（全屏、分屏、悬浮窗、自由窗口）下的沉浸式效果，可参考[窗口沉浸式](bpta-multi-device-window-immersive.md)。推荐开发者使用组件级的沉浸方案[实现沉浸效果](bpta-multi-device-window-immersive.md#section180431120426)，同时需要进行动态安全区避让，确保沉浸式显示效果。自由窗口模式下使用[window.setWindowDecorVisible(false)](../harmonyos-references/arkts-apis-window-window.md#setwindowdecorvisible11)设置隐藏标题栏，仅保留右上角三键。此时，应用页面拓展至标题栏区域，实现沉浸式显示效果。

### 消息页

即时通讯应用消息页主要用于展示消息列表、消息详情，满足用户聊天需求。根据功能设计，将消息页相关内容划分为5个区域，效果如下：

| 横向断点 | sm | md | lg |
| --- | --- | --- | --- |
| 消息页 |  |  |  |

**界面开发**

具体介绍及实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 顶部标题栏 | 使用响应式组件[HdsNavDestination](../harmonyos-references/ui-design-hdsnavdestination.md)设置[titleBar](../harmonyos-references/ui-design-hdsnavigation.md#titlebar)属性实现。在不同的设备宽度下组件自适应占满一屏。 |
| 2 | 消息列表 | 使用响应式组件[List](../harmonyos-references/ts-container-list.md)实现。通过[响应式环境变量](../harmonyos-references/responsive-env-system-property.md)监听窗口尺寸布局断点（[windowsizelayoutbreakpointinfo](../harmonyos-references/js-apis-arkui-observer.md#windowsizelayoutbreakpointinfo22)）变化，动态调整列表边距。 |
| 3 | 底部导航栏 | 使用响应式组件[HdsTabs](../harmonyos-references/ui-design-hdstabs.md)实现。通过[barFloatingStyle](../harmonyos-references/ui-design-hdstabs.md#barfloatingstyle)属性设置页签悬浮样式。 |
| 4 | 消息详情 | 使用响应式组件[Scroll](../harmonyos-references/ts-container-scroll.md)实现。通过设置[layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)属性，当设备高度小于内容高度时，可滑动查看消息信息。 |
| 5 | 消息输入区域 | 使用沿水平方向布局容器组件[Row](../harmonyos-references/ts-container-row.md)嵌套媒体组件[image](../atomic-ascf/components-image.md)实现。通过设置[layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)属性，消息输入框在不同断点下自适应拉伸。 |
| 6 | PC设备左侧导航栏 | 使用侧边栏容器[SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md)实现。通过设置[showSideBar](../harmonyos-references/ts-container-sidebarcontainer.md#showsidebar)属性，确保侧边栏固定显示。 |

### 通讯录页

即时通讯应用通讯录页主要用于展示通讯录列表、联系人主页，满足查看联系人需求。根据功能设计，将通讯录页相关内容划分为5个区域，效果如下：

| 横向断点 | sm | md | lg |
| --- | --- | --- | --- |
| 通讯录页 |  |  |  |

**界面开发**

具体介绍及实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 顶部标题栏 | 使用响应式组件[HdsNavDestination](../harmonyos-references/ui-design-hdsnavdestination.md)设置[titleBar](../harmonyos-references/ui-design-hdsnavigation.md#titlebar)属性实现。在不同的设备宽度下组件自适应占满一屏。 |
| 2 | 搜索栏 | 使用沿水平方向布局容器组件[Row](../harmonyos-references/ts-container-row.md)实现。通过设置[layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)属性，搜索框在不同断点下自适应拉伸。通过监听断点变化，实现响应式排列。 |
| 3 | 通讯录列表 | 使用堆叠容器[Stack](../harmonyos-references/ts-container-stack.md)嵌套响应式组件[List](../harmonyos-references/ts-container-list.md)和[AlphabetIndexer](../harmonyos-references/ts-container-alphabet-indexer.md)实现。通过监听断点变化，动态调整列表边距。 |
| 4 | 底部导航栏 | 使用响应式组件[HdsTabs](../harmonyos-references/ui-design-hdstabs.md)实现。通过[barFloatingStyle](../harmonyos-references/ui-design-hdstabs.md#barfloatingstyle)属性设置页签悬浮样式。 |
| 5 | 联系人主页 | 使用响应式组件[Scroll](../harmonyos-references/ts-container-scroll.md)嵌套网格容器[Grid](../harmonyos-references/ts-container-grid.md)实现。通过Grid的[aspectRatio](../harmonyos-references/ts-universal-attributes-layout-constraints.md#aspectratio)约束和设置image组件[objectFit](../harmonyos-references/ts-basic-components-image.md#objectfit)，使得Grid保持3列并横向自适应一屏。 |

### 朋友圈页

即时通讯应用朋友圈页主要用于展示朋友圈列表，满足查看朋友动态分享的需求。根据功能设计，将朋友圈页相关内容划分为4个区域，效果如下：

| 横向断点 | sm | md | lg |
| --- | --- | --- | --- |
| 朋友圈页 |  |  |  |

**界面开发**

具体介绍及实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 顶部标题栏 | 使用响应式组件[HdsNavDestination](../harmonyos-references/ui-design-hdsnavdestination.md)设置[titleBar](../harmonyos-references/ui-design-hdsnavigation.md#titlebar)属性实现。在不同的设备宽度下组件自适应占满一屏。 |
| 2 | 朋友圈列表 | 使用响应式组件[List](../harmonyos-references/ts-container-list.md)嵌套网格容器[Grid](../harmonyos-references/ts-container-grid.md)实现。通过Grid的[aspectRatio](../harmonyos-references/ts-universal-attributes-layout-constraints.md#aspectratio)约束和设置image组件[objectFit](../harmonyos-references/ts-basic-components-image.md#objectfit)，使得Grid保持3列并横向自适应一屏。 |
| 3 | 底部导航栏 | 使用响应式组件[HdsTabs](../harmonyos-references/ui-design-hdstabs.md)实现。通过[barFloatingStyle](../harmonyos-references/ui-design-hdstabs.md#barfloatingstyle)属性设置页签悬浮样式。 |

## 电脑端页面

本章介绍如何基于现有移动端界面开发方案，实现布局复用，高效完成电脑设备上即时通讯应用的界面开发。

### 消息页

即时通讯应用消息页主要用于展示消息列表、消息详情，满足用户聊天需求。根据功能设计，将消息页相关内容划分为5个区域，效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/3JsRa9lJQHmycJKMpl_N9g/zh-cn_image_0000002610129075.png "点击放大")

**界面开发**

具体介绍及实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 顶部标题栏 | 复用移动端设备布局方案，同移动端[消息页](multi-communication-app.md#section6120145294418)对应区域的布局实现方案一致。 |
| 2 | 消息列表 |
| 3 | 消息详情 |
| 4 | 消息输入区域 |
| 5 | PC设备左侧导航栏 | 使用侧边栏容器[SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md)实现。通过设置[showSidebar](../harmonyos-references/ts-container-sidebarcontainer.md#showsidebar)属性，确保侧边栏固定显示。 |

### 通讯录页

即时通讯应用通讯录页主要用于展示通讯录列表、联系人主页，满足查看联系人需求。根据功能设计，将通讯录页相关内容划分为5个区域，效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/A8LKYgf0SouY6sbag1Y-cA/zh-cn_image_0000002610209169.png "点击放大")

**界面开发**

具体介绍及实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 顶部标题栏 | 复用移动端设备布局方案，同移动端[通讯录页](multi-communication-app.md#section36831643877)对应区域的布局实现方案一致。 |
| 2 | 搜索栏 |
| 3 | 通讯录列表 |
| 4 | 联系人主页 |
| 5 | PC设备左侧导航栏 | 使用侧边栏容器[SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md)实现。通过设置[showSideBar](../harmonyos-references/ts-container-sidebarcontainer.md#showsidebar)属性，确保侧边栏固定显示。 |

### 朋友圈页

即时通讯应用朋友圈页主要用于展示朋友圈列表，满足查看朋友动态分享的需求。根据功能设计，将朋友圈页相关内容划分为4个区域，效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/AuIt6n4PQOamNQ2bz1ASrg/zh-cn_image_0000002579689290.png "点击放大")

**界面开发**

具体介绍及实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | PC设备左侧导航栏 | 使用侧边栏容器[SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md)实现。通过设置[showSidebar](../harmonyos-references/ts-container-sidebarcontainer.md#showsidebar)属性，确保侧边栏固定显示。 |
| 2 | 系统自由多窗操作栏 | 使用[window.setWindowDecorVisible(false)](../harmonyos-references/arkts-apis-window-window.md#setwindowdecorvisible11)设置隐藏标题栏，仅保留右上角三键。 |
| 3 | 朋友圈列表 | 复用移动端设备布局方案，同移动端[朋友圈页](multi-communication-app.md#section0352342123618)对应朋友圈列表布局实现方案一致。 |

## 示例代码

* [多设备即时通讯界面](https://gitcode.com/HarmonyOS_Samples/MultiDeviceCommunication)
