---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/multi-video-app
title: 多设备长视频界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备长视频界面
category: best-practices
scraped_at: 2026-09-02T15:03:19+08:00
doc_updated_at: 2026-08-10
content_hash: sha256:8fe614dd8762736e1a569902b7576f354686cbe220f3ccf2322f543a0dbd547b
---

## 概述

本文从当前常见的多设备应用场景中，选取长视频应用作为典型案例，详细介绍“一多”在实际开发中的应用。

长视频应用的核心是沉浸式播放与用户交互，主要功能涵盖视频推荐、视频搜索、视频详情、评论互动、全屏播放等。本文围绕上述核心功能，选取推荐页、搜索页及视频详情页作为典型页面进行开发实践。开发过程遵循多设备开发的“差异性”、“一致性”、“灵活性”和“兼容性”原则，助力开发者快速掌握“一多”开发能力，高效实现长视频应用相关功能。

目前该应用已适配设备包括：直板机、双折叠（Mate X系列）、三折叠、阔折叠、平板、电脑和智慧屏。

**说明** 

阅读本文前，建议开发者先了解[ArkUI（方舟UI框架）](../harmonyos-guides/arkui.md)和[一次开发，多端部署概览](bpta-multi-device-overview.md)相关知识。

下文将从UX设计、工程管理、页面开发三个方面，系统介绍长视频应用在实际开发中的最佳实践，为开发者提供可借鉴的实现思路。

* [UX设计](multi-video-app.md#zh-cn_topic_0000001744653537_section17797105112306)：介绍长视频应用的交互逻辑和通用设计要点，可供同类长视频应用开发者直接参考复用。
* [工程管理](multi-video-app.md#zh-cn_topic_0000001744653537_section189781175313)：基于分层架构搭建“一多”应用代码工程，以清晰的目录结构明确各层逻辑，同时针对长视频业务场景提供适配的工程配置方案。
* [移动端页面](multi-video-app.md#zh-cn_topic_0000001744653537_section7318163817529)、[电脑端页面](multi-video-app.md#section6171185373615)和[智慧屏端页面](multi-video-app.md#section67231377369)：按照实际应用开发流程，以页面为基本单元，分别讲解移动端、电脑端、智慧屏端页面在窗口适配、页面开发、交互开发及功能开发等环节的设计思路与具体实现方法。

## UX设计

长视频应用的UX设计可参考影音娱乐类多设备响应式设计指南的[长视频](../design-guides/responsive-design-examples1-0000001957369849.md#section10309114311327)章节，设计参考图如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/-AiKXKG6T3OAcDiargq06Q/zh-cn_image_0000002579786808.png "点击放大")

## 工程管理

为提升“一多”工程代码的复用性和可维护性，推荐开发者使用分层架构组织代码工程。分层架构将项目工程划分为产品定制层（products）、基础特性层（features）和公共能力层（common），各层级权责明确且功能独立，为开发者提供了一套清晰、高效且可扩展的设计架构。关于分层架构的具体设计细节，可参考[分层架构设计](bpta-layered-architecture-design.md)。

### 创建工程

开发者可先参考[多设备工程部署与发布](bpta-multi-device-ide.md)相关内容，掌握分层架构工程的创建与配置方法，并完成分层架构模板工程的搭建。后续再结合长视频应用的实际开发需求进行针对性调整，使工程架构与业务场景保持一致。

### 工程结构

长视频应用基于推荐的分层架构，按products、features、common三个层级组织代码工程。各层级设计如下：

* products层：长视频应用需要适配的设备包括直板机、双折叠（Mate X系列）、三折叠、阔折叠、平板、电脑和智慧屏。由于智慧屏和电脑的界面布局与其他设备差异较大，因此在products层分别创建名称为“tv”和“pc”的HAP包，作为智慧屏和电脑的应用入口。直板机、双折叠（Mate X系列）、三折叠、阔折叠和平板的界面整体布局相似，部分差异可以通过“一多”的[自适应布局](bpta-multi-device-adaptive-layout.md)和[响应式布局](bpta-multi-device-responsive-layout.md)进行适配，因此在products层创建名称为“default”的HAP包作为这类设备统一的应用入口。
* features层：长视频应用主要包含推荐（multivideorecommended）、搜索（multivideosearch）和视频详情（multivideodetail）三个核心业务模块。在features层为三个业务模块分别创建对应的HAR包，供products层按需引用。各业务模块相对独立，互不依赖，便于后续工程的维护与迭代。
* common层：为实现代码复用、减少冗余，在common层创建一个基础（multivideobase）能力HAR包，统一封装公共常量、媒体播放工具以及窗口管理工具等多模块共用的基础能力，便于上层模块直接调用。

工程结构如下：

```screen
├──common                                         // 基础特性层
│  ├──multivideobase/src/main/ets                 // 基础公共能力ArkTS源码
│  │  ├──constants
│  │  └──utils
│  └──base/Index.ets                              // 基础公共能力对外导出接口
├──features                                       // 公共能力层
│  ├──multivideorecommended/src/main/ets          // 推荐模块ArkTS源码
│  │  ├──constants
│  │  ├──model
│  │  ├──utils
│  │  ├──view
│  │  └──viewmodel
│  ├──multivideorecommended/src/main/resources    // 推荐模块资源文件
│  ├──multivideorecommended/Index.ets             // 推荐模块对外导出接口
│  ├──multivideosearch/src/main/ets               // 搜索模块ArkTS源码
│  │  ├──constants
│  │  ├──model
│  │  ├──view
│  │  └──viewmodel
│  ├──multivideosearch/src/main/resources         // 搜索模块资源文件
│  ├──multivideosearch/Index.ets                  // 搜索模块对外导出接口
│  ├──multivideodetail/src/main/ets               // 视频详情模块ArkTS源码
│  │  ├──constants
│  │  ├──model
│  │  ├──utils
│  │  ├──view
│  │  └──viewmodel
│  ├──multivideovideodetail/src/main/resources    // 视频详情模块资源文件
│  └──multivideodetail/Index.ets                  // 视频详情模块对外导出接口
└──products                                       // 产品定制层
   ├──default/src/main/ets                        // 直板机、双折叠（Mate X系列）、三折叠、阔折叠产品ArkTS源码
   │  ├──constants
   │  ├──defaultability
   │  ├──model
   │  ├──pages
   │  ├──view
   │  └──viewmodel
   ├──default/src/main/resources                 // 直板机、双折叠（Mate X系列）、三折叠、阔折叠产品资源文件
   ├──pc/src/main/ets                            // 电脑产品ArkTS源码
   │  ├──constants
   │  ├──model
   │  ├──pages
   │  ├──pcability
   │  ├──view
   │  └──viewmodel
   ├──pc/src/main/resources                      // 电脑产品资源文件
   ├──tv/src/main/ets                            // 智慧屏产品ArkTS源码
   │  ├──constants
   │  ├──tvability
   │  ├──pages
   │  └──view
   └──tv/src/main/resources                      // 智慧屏产品资源文件
```

## 移动端页面

本章介绍如何针对直板机、双折叠（Mate X系列）、三折叠、阔折叠和平板设备，使用“一多”布局能力，实现长视频应用页面层级“一套代码、多端适配”。同时，介绍上述设备的窗口适配方案，以及各页面的交互开发和功能开发方案。

### 窗口适配

* 窗口模式

  长视频应用在移动端设备上支持全屏、分屏、悬浮窗和自由窗口四种模式，具体实现可参考[窗口模式](bpta-multi-device-window-mode.md)。其中，分屏与悬浮窗模式无需特殊设计，可直接通过系统能力进入。应用内监听窗口尺寸变化，[通过断点刷新UI](bpta-multi-device-responsive-layout.md#section175001836203617)，即可自动适配各类窗口模式下的布局。
* 窗口方向

  应用内可通过[window.setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)设置窗口显示方向，具体说明可参考[窗口方向](bpta-multi-device-window-direction.md)。在长视频应用中，仅在视频详情页进行全屏播放切换时，执行特定的窗口方向设置，相关实现逻辑可参考[视频详情页 & 全屏播放页案例](bpta-multi-device-window-direction.md#section0224819173914)。除该场景外，应用统一采用[跟随桌面的旋转模式](../harmonyos-guides/window-rotation.md#其他方向类型)，建议在HAP包的module.json5文件中[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)下配置orientation属性为follow\_desktop。
* 窗口沉浸式

  根据UX设计规范，需要在多种窗口模式（全屏、分屏、悬浮窗）下实现沉浸式效果，具体实现可参考[窗口沉浸式](bpta-multi-device-window-immersive.md)。在全屏、分屏和悬浮窗模式下，均可通过[window.setWindowLayoutFullscreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)实现沉浸式，并配合动态安全区避让，确保显示效果完整。

### 推荐页

推荐页主要用于推荐精选内容，满足用户观看需求。按照功能设计，将应用推荐页相关内容划分为6个区域，效果图如下所示。

| 横向（/纵向）断点 | sm/md | sm/lg | md | lg、xl |
| --- | --- | --- | --- | --- |
| 推荐页-精选页Tab |  |  |  |  |

**界面开发**

推荐页借助“一多”自适应布局的延伸能力、缩放能力和响应式布局的栅格系统，实现不同断点下的布局效果。具体介绍及实现方案如下表所示。

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | Banner图 | 使用响应式组件[Swiper](../harmonyos-references/ts-container-swiper.md)实现。通过[displayCount](../harmonyos-references/ts-container-swiper.md#displaycount8)属性，控制视窗内显示元素数量。在横向断点为sm或md时，视窗内显示1个元素；在横向断点为lg或xl时，视窗内显示2个元素。结合[aspectRatio](../harmonyos-references/ts-universal-attributes-layout-constraints.md#aspectratio)属性，实现Banner图在不同断点下的自适应缩放。 |
| 2 | 图标列表 | 使用响应式组件[List](../harmonyos-references/ts-container-list.md)实现。通过监听断点变化，动态调整图标间距。 |
| 3 | 热播视频 | 使用网格容器[Grid](../harmonyos-references/ts-container-grid.md)实现。通过[columnsTemplate](../harmonyos-references/ts-container-grid.md#columnstemplate)属性，动态调整不同断点下的显示列数。结合[aspectRatio](../harmonyos-references/ts-universal-attributes-layout-constraints.md#aspectratio)属性，实现视频预览图在不同断点下的自适应缩放。 |
| 4 | 新片发布 |
| 5 | 每日佳片 | 使用响应式布局的栅格系统实现。通过挪移布局，实现不同断点下“上下布局”与“左右布局”之间的自适应切换。结合[aspectRatio](../harmonyos-references/ts-universal-attributes-layout-constraints.md#aspectratio)属性，实现视频预览图在不同断点下的自适应缩放。 |
| 6 | 往期回顾 |

在实际开发中，区域1-6为并列的推荐页内容，开发顺序为区域1-6。为进一步提升用户体验，推荐页实现了[社区页签沉浸式设计](multi-video-app.md#li12646116102317)和[Banner图创新排版](multi-video-app.md#li1330641852313)，效果图如下所示。

* 社区页签沉浸式设计

  | 横向（/纵向）断点 | sm/md | sm/lg | md | lg、xl |
  | --- | --- | --- | --- | --- |
  | 推荐页-社区页Tab |  |  |  |  |
* Banner图创新排版

  | 横向（/纵向）断点 | sm/md | sm/lg | md | lg、xl |
  | --- | --- | --- | --- | --- |
  | 推荐页-视频页Tab |  |  |  |  |

**交互开发**

为提升长视频应用推荐页的用户浏览体验，需结合用户潜在使用场景进行交互开发。用户在浏览过程中，通常会有快速预览视频内容、动态调整热播视频数量的需求。因此，在满足[多设备交互](bpta-multi-interaction.md)开发基础操作适配的基础上，额外实现了两项交互功能：[热播视频区域长按预览](multi-video-app.md#li202846476502)和[热播视频区域缩放控制](multi-video-app.md#li16567125118)。

* 热播视频区域长按预览

  视频应用移动端实现了手机和平板设备的适配，支持的输入设备包括触控屏、手写笔和鼠标。

  上述输入设备的长按预览操作，统一在热播视频区域首张图片的[LongPressGesture()](../harmonyos-references/ts-basic-gestures-longpressgesture.md)回调中实现，通过弹出[自定义弹窗 (CustomDialog)](../harmonyos-references/ts-methods-custom-dialog-box.md)播放视频完成交互。效果图如下所示。

  | 横向（/纵向）断点 | sm/lg | md | lg、xl |
  | --- | --- | --- | --- |
  | 推荐页-热播视频长按预览 |  |  |  |
* 热播视频区域缩放控制

  长视频应用移动端实现了手机和平板设备的适配，支持的输入设备包括触控屏、鼠标和键盘。缩放控制可以通过触摸屏上的双指操作触发，也可以通过键盘Ctrl键+鼠标滚轮的组合方式触发。

  上述输入设备的缩放操作，统一在热播视频区域的[PinchGesture()](../harmonyos-references/ts-basic-gestures-pinchgesture.md)回调中实现，通过修改网格布局的[columnsTemplate](../harmonyos-references/ts-container-grid.md#columnstemplate)属性动态调整布局效果。效果图如下所示。

  | 横向断点 | md | lg、xl |
  | --- | --- | --- |
  | 推荐页-热播视频区域缩放 |  |  |

### 搜索页

搜索页主要用于响应用户输入、展示搜索建议及搜索结果。按照功能设计，将应用搜索页相关内容划分为5个区域，效果图如下所示。

| 横向（/纵向）断点 | sm/md | sm/lg | md | lg、xl |
| --- | --- | --- | --- | --- |
| 搜索页 |  |  |  |  |
| 搜索页-智能提示 |  |  |  |  |
| 搜索页-搜索结果 |  |  |  |  |

**界面开发**

搜索页借助“一多”自适应布局的延伸能力和响应式布局的栅格系统，实现不同断点下的布局效果。具体介绍及实现方案如下表所示。

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 搜索框 | 使用[TextInput](../harmonyos-references/ts-basic-components-textinput.md)组件实现。通过[layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)属性实现自适应拉伸，确保在不同断点下均横向铺满屏幕。 |
| 2 | 搜索发现 | 使用响应式组件[List](../harmonyos-references/ts-container-list.md)实现。通过[lanes](../harmonyos-references/ts-container-list.md#lanes9)属性控制列数：在sm和md横向断点下2列显示；在lg和xl横向断点下3列显示。标题栏的空白区域使用[Blank](../harmonyos-references/ts-basic-components-blank.md)组件实现拉伸效果。 |
| 3 | 热搜 | 使用响应式组件[List](../harmonyos-references/ts-container-list.md)实现。通过[lanes](../harmonyos-references/ts-container-list.md#lanes9)属性控制列数：在sm横向断点下1列显示；在md横向断点下2列显示；在lg和xl横向断点下3列显示。随断点变化自适应调整顶部页签的间距。 |
| 4 | “华”搜索智能提示 | 使用响应式组件[List](../harmonyos-references/ts-container-list.md)实现。通过[lanes](../harmonyos-references/ts-container-list.md#lanes9)属性控制列数：在sm和md横向断点下1列显示；在lg和xl横向断点下2列显示。 |
| 5 | 搜索结果 | 使用响应式栅格系统实现。通过挪移布局实现“上下布局”与“左右布局”切换。同时，结合[aspectRatio](../harmonyos-references/ts-universal-attributes-layout-constraints.md#aspectratio)属性，实现视频预览图的自适应缩放。 |

在实际开发中，区域1为导航栏，区域2、3、4和5为并列的搜索页内容，开发顺序为区域1，区域2-5。为提升搜索页使用体验，页面会根据用户在搜索框的输入动态切换展示内容。本示例中，默认状态下显示搜索发现和热搜内容。当用户输入“华”时，显示智能提示列表。当用户输入“华为发布会”或在智能提示中选择“华为发布会”时，显示搜索结果。开发者可根据需求自定义搜索发现、热搜、智能提示及搜索结果的触发条件与展示样式。

### 视频详情页

视频详情页主要用于视频播放、评论互动及相关信息展示。根据页面的功能差异，将其划分为[边看边评页](multi-video-app.md#li790319142255)和[全屏播放页](multi-video-app.md#li3446284253)两部分。

* 边看边评页

边看边评页主要用于展示视频详细信息，并为用户提供评论互动功能。按照功能设计，将边看边评页相关内容划分为5个区域，效果图如下所示。

| 横向（/纵向）断点 | sm/md | sm/lg | md | lg、xl |
| --- | --- | --- | --- | --- |
| 视频详情页-边看边评 |  |  |  |  |

**界面开发**

边看边评页借助“一多”自适应布局的延伸和缩放能力，结合不同断点下部分组件的显隐控制，实现多断点的布局适配。具体介绍及实现方案如下表所示。

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 视频播放 | 使用[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)和[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)等视频播放相关组件实现。具体实现逻辑可查看[示例代码](multi-video-app.md#section18854194463114)。 |
| 2 | 相关列表 | 标题栏的空白区域通过[Blank](../harmonyos-references/ts-basic-components-blank.md)组件实现拉伸能力。视频列表区域通过[List](../harmonyos-references/ts-container-list.md)组件实现延伸能力，横向显示视频相关列表。 |
| 3 | 全部评论 | 在sm和md横向断点下，该区域底部显示；在lg和xl横向断点下，该区域侧边显示。同时结合[aspectRatio](../harmonyos-references/ts-universal-attributes-layout-constraints.md#aspectratio)属性，实现评论区图片在不同断点下的自适应缩放。 |
| 4 | 写评论 | 使用[TextInput](../harmonyos-references/ts-basic-components-textinput.md)组件实现。通过[layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)属性实现自适应拉伸，实现输入框在不同断点下均横向占满容器的剩余空间。 |
| 5 | 视频简介 | 视频简介区域的图标使用[Row](../harmonyos-references/ts-container-row.md)组件实现。通过将[justifyContent](../harmonyos-references/ts-container-row.md#justifycontent8)属性设置为FlexAlign.SpaceBetween实现图标均分排列。选集列表和周边视频区域通过[List](../harmonyos-references/ts-container-list.md)组件实现延伸能力，横向显示相关内容。在sm和md横向断点下，隐藏该区域；在lg和xl断点下，显示该区域。 |

实际开发中，在sm和md断点下，区域5不显示，区域1-4均显示在视频下方。区域1-3和区域4为并列的边看边评页内容，开发顺序为区域4，区域1-3；在lg和xl断点下，页面分为侧边栏和主内容区两部分，主内容区包含区域1、2、5，侧边栏包括区域3、4，两部分为并列的边看边评页内容，开发顺序为区域3、4，区域1、2、5。

* 全屏播放页

全屏播放页主要为用户提供沉浸式观看体验，并支持选集功能。按照功能设计，将全屏播放页相关内容划分为3个区域，效果图如下所示。

| 横向（/纵向）断点 | sm/md | sm/lg | md | lg、xl |
| --- | --- | --- | --- | --- |
| 视频详情页-全屏播放 |  |  |  |  |
| 视频详情页-选集 |  |  |  |  |

**界面开发**

全屏播放页借助“一多”自适应布局的占比能力，实现不同断点下布局效果的自适应调整。具体介绍及实现方案如下表所示。

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 全屏视频播放 | 使用[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)和[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)等视频播放相关组件实现，具体实现逻辑可查看[示例代码](multi-video-app.md#section18854194463114)。 |
| 2 | 进度条及工具栏 | 进度条使用[Slider](../harmonyos-references/ts-basic-components-slider.md)组件实现。通过[layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)属性，控制进度条在不同断点下均横向占满父组件剩余空间。 |
| 3 | 选集列表 | 使用响应式组件[List](../harmonyos-references/ts-container-list.md)实现。通过[lanes](../harmonyos-references/ts-container-list.md#lanes9)属性控制选集列表的列数在不同断点下自适应变化。在不同断点下，该区域切换为侧边显示或底部显示。断点变化时，该区域尺寸支持两种配置方式：设置为固定大小，或通过[layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)属性实现与区域1、区域2按固定占比分配空间。 |

实际开发中，区域1、2和区域3是并列的全屏播放页内容，开发顺序为区域1、2，区域3。全屏播放页的窗口适配可参考[窗口方向](multi-video-app.md#li672514218397)。为进一步提升用户体验，全屏播放页针对折叠屏半折叠状态，实现了[视频悬停播放功能](multi-video-app.md#li4648122318619)。

* 视频悬停播放功能

  1. 悬停态触发条件：在双折叠/三折叠设备上浏览边看边评页或全屏播放页时，将设备旋转至横屏并切换为半折叠状态，即可自动进入悬停播放模式，获得沉浸式视频观看体验。

  2. 悬停态页面布局：视频画面移至屏幕上半部分显示；屏幕中间设置为折叠屏折痕避让区；进度条及其他可操作组件统一排布在屏幕下半部分。效果图如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/azbc1ZOkQQSsabaP77pPOQ/zh-cn_image_0000002610146917.png "点击放大")

**说明** 

更多悬停态页面的开发方式，请参考[折叠屏悬停态](bpta-folded-hover.md)。

**交互开发**

长视频应用的全屏播放页面，主要为用户提供沉浸式视频观看体验。因此，在满足[多设备交互](bpta-multi-interaction.md)开发基础操作适配的基础上，实现了[视频播放控制](multi-video-app.md#li12864112272313)的交互开发。

* 视频播放控制

  长视频应用移动端实现了手机和平板设备的适配，支持的输入设备包括触控屏、手写笔、鼠标和键盘。需根据上述输入设备的不同交互方式，适配相应事件处理机制。

  以实现播放/暂停控制为例，对于触控屏、手写笔和鼠标，统一在视频播放区域的播放/暂停控件上监听[onClick()](../harmonyos-references/ts-universal-events-click.md#onclick12)点击事件，实现播放和暂停控制。对于键盘，则通过监听空格键的[onKeyEvent](../harmonyos-references/ts-universal-events-key.md#onkeyevent)事件，实现播放和暂停控制。视频播放控制的具体交互逻辑，可查看[示例代码](multi-video-app.md#section18854194463114)。

## 电脑端页面

本章介绍如何基于现有移动端界面开发方案，实现代码逻辑与布局复用，高效完成长视频应用在电脑设备上的界面开发。同时，详细阐述各页面的交互开发实现方案。

### 窗口适配

* 窗口模式

  长视频应用在电脑端上支持全屏和自由窗口两种模式，具体实现可参考[窗口模式](bpta-multi-device-window-mode.md)。应用内监听窗口尺寸变化，[通过断点刷新UI](bpta-multi-device-responsive-layout.md#section175001836203617)，即可自动适配全屏和自由窗口模式下的布局。
* 窗口沉浸式

  根据UX设计规范，需要实现全屏和自由窗口下的沉浸式效果，具体实现可参考[窗口沉浸式](bpta-multi-device-window-immersive.md)。全屏模式下，通过[window.setWindowLayoutFullscreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)实现沉浸式。自由窗口模式下，通过[window.setWindowDecorVisible(false)](../harmonyos-references/arkts-apis-window-window.md#setwindowdecorvisible11)隐藏标题栏，仅保留右上角三键，使页面内容延伸至标题栏区域，实现沉浸式显示效果。

### 推荐页

电脑端推荐页与移动端功能定位一致，按照功能设计划分为6个区域，效果图如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/FTxCbCUvRJKrZUlMqwVwew/zh-cn_image_0000002579627030.png "点击放大")

**界面开发**

推荐页借助“一多”自适应布局的延伸能力、缩放能力和响应式布局的栅格系统，实现不同断点下的布局效果。

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | Banner图 | 与移动端[推荐页](multi-video-app.md#section109591922155720)区域1-6复用布局实现方案。 |
| 2 | 图标列表 |
| 3 | 热播视频 |
| 4 | 新片发布 |
| 5 | 每日佳片 |
| 6 | 往期回顾 |

实际开发中，电脑端各区域的开发顺序与移动端[推荐页](multi-video-app.md#section109591922155720)保持一致。同时，为确保与移动端一致的用户体验，电脑端推荐页也适配了[社区页签沉浸式设计](multi-video-app.md#li143831112164610)和[Banner图创新排版](multi-video-app.md#li638321294617)。效果图如下所示。

* 社区页签沉浸式设计

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/HlY1JNwpR5Sd8wDTnoeStA/zh-cn_image_0000002579786936.png "点击放大")
* Banner图创新排版

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/GFlWPmPWR7qUl3vij7NPgA/zh-cn_image_0000002610066823.png "点击放大")

**交互开发**

为确保长视频应用电脑端推荐页与移动端保持一致的交互体验，电脑端推荐页同步实现了热播视频区域长按预览和热播视频区域缩放控制两项交互功能。

长视频应用电脑端需支持的输入设备包括触控屏、鼠标、键盘和触控板。长按和缩放操作控制复用移动端实现方案，效果图如下。

**表1**

| 交互功能 | 效果图 |
| --- | --- |
| 热播视频区域长按预览 |  |
| 热播视频区域缩放控制 |  |

### 搜索页

电脑端搜索页与移动端功能定位一致，按照功能设计划分为5个区域，效果图如下所示。

|  |  |
| --- | --- |
| 搜索页 |  |
| 搜索页-智能提示 |  |
| 搜索页-搜索结果 |  |

**界面开发**

搜索页借助“一多”自适应布局的延伸能力和响应式布局的栅格系统，实现不同断点下的布局效果。

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 搜索框 | 与移动端[搜索页](multi-video-app.md#section1733591819510)区域1-5复用布局实现方案。 |
| 2 | 搜索发现 |
| 3 | 热搜 |
| 4 | “华”搜索智能提示 |
| 5 | 搜索结果 |

实际开发中，电脑端各区域的开发顺序与移动端[搜索页](multi-video-app.md#section1733591819510)保持一致。

### 视频详情页

电脑端视频详情页与移动端功能定位一致，可分为[边看边评页](multi-video-app.md#li9736151011198)和[全屏播放页](multi-video-app.md#li19738151011916)两部分。

* 边看边评页

边看边评页按照功能设计划分为5个区域，效果图如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/9kHagbLtQEqbr--L6swOgQ/zh-cn_image_0000002579627036.png "点击放大")

**界面开发**

边看边评页借助“一多”自适应布局的延伸和缩放能力，结合不同断点下部分组件的显隐控制，实现多断点的布局适配。

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 视频播放 | 与移动端[边看边评页](multi-video-app.md#li790319142255)区域1-5复用布局实现方案。 |
| 2 | 相关列表 |
| 3 | 全部评论 |
| 4 | 写评论 |
| 5 | 视频简介 |

实际开发中，电脑端各区域的开发顺序与移动端[边看边评页](multi-video-app.md#li790319142255)保持一致。

* 全屏播放页

全屏播放页按照功能设计划分为3个区域，效果图如下所示。

|  |  |
| --- | --- |
| 视频详情页-全屏播放 |  |
| 视频详情页-选集 |  |

**界面开发**

全屏播放页借助“一多”自适应布局的占比能力，实现不同断点下布局效果的自适应调整。

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 全屏视频播放 | 与移动端[全屏播放页](multi-video-app.md#li3446284253)区域1-3复用布局实现方案。 |
| 2 | 进度条及工具栏 |
| 3 | 选集列表 |

实际开发中，电脑端各区域的开发顺序与移动端[全屏播放页](multi-video-app.md#li3446284253)保持一致。

**交互开发**

为确保长视频应用电脑端全屏播放页与移动端保持一致的交互体验，电脑端全屏播放页同步实现了[视频播放控制](multi-video-app.md#li8739110151918)交互功能。

* 视频播放控制

  长视频应用适配了电脑设备，需支持的输入设备包括触控屏、鼠标、触控板和键盘。需根据不同输入设备的交互方式，适配相应事件处理机制。

  以实现播放/暂停控制为例，对于触控屏、鼠标和触摸板，统一在视频播放区域的播放/暂停控件上监听[onClick()](../harmonyos-references/ts-universal-events-click.md#onclick12)点击事件来进行播放和暂停控制。对于键盘，则监听空格键的[onKeyEvent](../harmonyos-references/ts-universal-events-key.md#onkeyevent)事件来进行播放和暂停控制。视频播放控制的具体交互逻辑，可查看[示例代码](multi-video-app.md#section18854194463114)。

## 智慧屏端页面

本章介绍如何基于现有移动端界面开发方案，实现代码逻辑与布局复用，高效完成长视频应用在智慧屏设备上的界面开发。同时，详细阐述各页面的交互开发实现方案。

### 推荐页

智慧屏端推荐页与移动端功能定位一致，按照功能设计划分为6个区域，效果图如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/8LBcEU6_STSLt8ASP8K5PA/zh-cn_image_0000002610146927.png "点击放大")

**界面开发**

推荐页各区域具体介绍及实现方案如下表所示。

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | Banner图 | 使用响应式组件[Swiper](../harmonyos-references/ts-container-swiper.md)实现。通过[displayCount](../harmonyos-references/ts-container-swiper.md#displaycount8)属性控制视窗内同时显示5个元素，当视窗内元素发生位置变换时，呈现不同的布局效果，提升视觉交互体验。 |
| 2 | 顶部页签 | 使用响应式组件[List](../harmonyos-references/ts-container-list.md)实现。通过index变化实现下方区域显示内容的切换。 |
| 3 | 热播视频 | 与移动端设备复用布局方案，同移动端[推荐页](multi-video-app.md#section109591922155720)区域3、4的布局实现方案。 |
| 4 | 新片发布 |
| 5 | 每日佳片 | 与移动端设备复用布局方案，同移动端[推荐页](multi-video-app.md#section109591922155720)区域5、6的布局实现方案。 |
| 6 | 往期回顾 |

在实际开发中，区域1-6为并列的推荐页内容，开发顺序为区域1-6。

### 搜索页

智慧屏端搜索页与移动端功能定位一致，按照功能设计划分为5个区域，效果图如下所示。

|  |  |
| --- | --- |
| 搜索页 |  |
| 搜索页-搜索结果 |  |

**界面开发**

搜索页具体介绍及实现方案如下表所示。

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 搜索框 | 使用[TextInput](../harmonyos-references/ts-basic-components-textinput.md)组件实现。设置为固定宽度，并在窗口水平方向居中显示。 |
| 2 | 自定义键盘 | 使用栅格组件[Grid](../harmonyos-references/ts-container-grid.md)分别实现字母输入和数字输入两个自定义键盘。 |
| 3 | 搜索智能提示 | 使用响应式组件[List](../harmonyos-references/ts-container-list.md)实现。 |
| 4 | 搜索推荐 | 上方标题栏使用[Text](../harmonyos-references/ts-basic-components-text.md)或响应式组件[List](../harmonyos-references/ts-container-list.md)实现，下方视频区域使用响应式组件[List](../harmonyos-references/ts-container-list.md)实现，在相同布局区域进行复用。 |
| 5 | 搜索结果 |

实际开发中，区域1、2为键盘输入操作区域，区域3-5为并列的搜索页内容，开发顺序为区域1、2，区域3-5。为提升搜索页使用体验，页面会根据用户在搜索框的输入动态切换展示内容。本示例中，默认状态下显示大家都在搜和热搜内容。当用户输入“H”时，显示搜索结果。开发者可根据需求自定义大家都在搜、热搜及搜索结果的触发条件与展示样式。

### 视频详情页

智慧屏端视频详情页主要用于视频播放和相关信息的展示。按照功能设计，将视频详情页相关内容划分为6个区域，效果图如下所示。

|  |  |
| --- | --- |
| 视频详情页 |  |
| 视频详情页-全屏播放 |  |
| 视频详情页-选集 |  |

**界面开发**

视频详情页具体介绍及实现方案如下表所示。

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 视频播放 | 使用[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)和[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)等视频播放相关组件实现。具体实现逻辑可查看[示例代码](multi-video-app.md#section18854194463114)。 |
| 2 | 标题栏 | 在父组件[Row](../harmonyos-references/ts-container-row.md)中分别实现标题和选集两个功能区。通过[Stack](../harmonyos-references/ts-container-stack.md)组件控制视频详情页组件层级，确保标题栏始终显示在视频详情页最上层。 |
| 3 | 视频简介 | 使用[Text](../harmonyos-references/ts-basic-components-text.md)组件实现。进入视频详情页时默认显示该区域，视频播放时隐藏该区域。 |
| 4 | 选集列表 | 使用响应式组件[List](../harmonyos-references/ts-container-list.md)实现。进入视频详情页时默认显示该区域，视频播放时自动隐藏该区域；用户执行选集操作时，重新显示该区域。 |
| 5 | 进度条 | 使用[Slider](../harmonyos-references/ts-basic-components-slider.md)组件实现。进入视频详情页时默认隐藏该区域，视频播放时自动显示该区域；用户执行选集操作时，重新隐藏该区域。 |
| 6 | 视频推荐 | 上方标题栏使用[Text](../harmonyos-references/ts-basic-components-text.md)组件实现，下方视频区域使用响应式组件[List](../harmonyos-references/ts-container-list.md)实现。进入视频详情页时默认显示该区域，视频播放时自动隐藏该区域；用户退出视频播放时，重新显示该区域。 |

实际开发中，区域1为视频播放主体内容、区域2-5为视频相关信息、区域6为视频推荐内容。三个区域均为视频详情页的并列展示模块，开发顺序为区域1，区域2-5，区域6。

**交互开发**

为确保长视频应用智慧屏端全屏播放页与移动端保持一致的交互体验，智慧屏端全屏播放页同步实现了[视频播放控制](multi-video-app.md#li98341811145013)交互功能。

* 视频播放控制

  长视频应用适配了智慧屏设备，需支持的输入设备包括灵犀指向遥控、灵犀悬浮触控、键盘和鼠标。需根据不同输入设备的交互方式，适配相应事件处理机制。

  以实现播放/暂停控制为例，对于灵犀指向遥控、灵犀悬浮触控和鼠标，统一在视频播放区域监听[onClick()](../harmonyos-references/ts-universal-events-click.md#onclick12)点击事件来进行播放和暂停控制。对于灵犀指向遥控，监听确定键的[onKeyEvent](../harmonyos-references/ts-universal-events-key.md#onkeyevent)事件来进行播放和暂停控制。对于键盘，则监听空格键的[onKeyEvent](../harmonyos-references/ts-universal-events-key.md#onkeyevent)事件来进行播放和暂停控制。视频播放控制的具体交互逻辑，可查看[示例代码](multi-video-app.md#section18854194463114)。

## 示例代码

* [多设备长视频界面](https://gitcode.com/harmonyos_samples/MultiVideoApplication)
