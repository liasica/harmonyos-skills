---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/multi-news-read
title: 多设备新闻阅读界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备新闻阅读界面
category: best-practices
scraped_at: 2026-09-02T15:03:19+08:00
doc_updated_at: 2026-09-02
content_hash: sha256:7f4ab78488091cd43973097916cf2da6138231df01d4ea572b8d3bf438a710c6
---

## 概述

本文以新闻阅读应用为例，介绍如何基于三层架构、断点监听和自适应布局，实现一套代码在直板机、折叠屏、平板和电脑上的多端部署。目前该应用已适配设备包括：直板机、阔折叠、双折叠、三折叠、平板和电脑。

**说明** 

在阅读本文前，建议开发者先了解[ArkUI（方舟UI框架）](../harmonyos-guides/arkui.md)和[一次开发，多端部署概览](bpta-multi-device-overview.md)相关知识。

下文将从UX设计、工程管理、移动端页面和电脑端页面四个方面，系统介绍新闻阅读应用在实际开发中的最佳实践，为开发者提供可借鉴的实现思路。

* [UX设计](multi-news-read.md#section73614881015)：介绍新闻阅读应用的响应式设计要点和多设备效果预览。
* [工程管理](multi-news-read.md#section1220019261104)：基于分层架构搭建“一多”应用代码工程，以清晰的目录结构明确各层逻辑，同时封装窗口断点监听等公共能力。
* [移动端页面](multi-news-read.md#section141711741141)和[电脑端页面](multi-news-read.md#section65701625122313)：按照实际应用开发流程，以页面为基本单元，分别讲解不同设备端页面在窗口适配、页面开发及交互开发等环节的设计思路与具体实现方法。

## UX设计

新闻阅读应用的UX设计可参考[新闻阅读类](../design-guides/responsive-design-examples4-0000001746657290.md)设计指南。应用在直板机上采用单列纵向布局，在折叠屏和平板上以双列栅格展示，在电脑上采用侧边栏加内容区的分栏布局。多设备新闻阅读界面在不同设备形态下的效果如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/QA_fTh01QYCyuvzYmX4FMg/zh-cn_image_0000002693047956.png "点击放大")

## 工程管理

考虑到“一多”工程代码的复用性和可维护性，推荐开发者使用分层架构组织代码工程。分层架构将项目工程划分为产品定制层（products）、基础特性层（features）和公共能力层（common）三个层级，各层级权责清晰、各司其职，为开发者提供了一套清晰、高效且可扩展的设计架构。关于分层架构的具体设计细节，可参考[分层架构设计](bpta-layered-architecture-design.md)。

### 创建工程

建议开发者参考[多设备工程部署与发布](bpta-multi-device-ide.md)相关内容，掌握分层架构工程的创建与配置方法后，创建出模板项目工程。然后根据新闻阅读应用的开发需求进行针对性修改，确保工程架构贴合实际业务需求。

### 工程结构

在创建“一多”工程时，开发者会面临工程结构目录的划分问题。考虑到复用性和可维护性，本文以新闻阅读应用为例，提供推荐的参考方案。

HarmonyOS的分层架构主要包括三个层次：产品定制层、基础特性层和公共能力层，为开发者构建了一个清晰、高效、可扩展的设计架构。更多详情请参考[分层架构设计](bpta-layered-architecture-design.md)的逻辑设计。

新闻阅读应用根据一多推荐的common、features、products的“三层工程架构”划分目录。各层级设计如下：

* products层：新闻阅读应用需要适配的设备包括直板机、阔折叠、双折叠、三折叠、平板、电脑。由于电脑的界面布局与其他设备差异较大，因此在products层创建名称为"pc"的HAP包，作为电脑的应用入口。直板机、阔折叠、双折叠和平板的界面整体布局相似，部分差异可以通过“一多”的[自适应布局](bpta-multi-device-adaptive-layout.md)和[响应式布局](bpta-multi-device-responsive-layout.md)进行适配，因此在products层创建名称为"default"的HAP包作为这类设备统一的应用入口。

* features层：新闻阅读应用主要包含首页推荐页（recommendation）和新闻详情（newsdetail）两个核心业务模块。在features层为两个业务模块分别创建对应的HAR包，供products层按需引用。各业务模块相对独立，互不依赖，便于后续工程的维护与迭代。
* common层：为实现代码复用、减少冗余，在common层创建一个基础能力HAR包，统一封装公共常量、窗口管理工具、断点取值器等多模块共用的基础能力，便于上层模块直接调用。

工程结构如下：

```screen
├──common                          // 公共能力层 
│  └──src/main/ets
│     ├──components                // 公共 UI 组件（NewsCard 等）
│     ├──constants                 // 公共常量（断点等）
│     ├──types                     // 数据契约接口
│     └──utils                     // 窗口、断点、日志等工具
├──features                        // 基础特性层
│  ├──recommendation               // 首页推荐
│  │  └──src/main/ets
│  │     ├──constants              // 推荐常量
│  │     ├──model                  // 推荐数据
│  │     ├──page                   // 推荐首页
│  │     ├──view                   // 首页 UI 组件
│  │     └──viewmodel              // 首页状态
│  └──newsdetail                   // 新闻详情
│     └──src/main/ets
│        ├──constants              // 详情常量
│        ├──model                  // 详情数据
│        ├──view                   // 详情页 UI 组件
│        └──viewmodel              // 详情页状态
└──products                        // 产品定制层
   ├──default                      // 默认（直板机/折叠屏/平板）产品
   │  └──src/main/ets
   │     ├──defaultability         // 默认入口 Ability
   │     └──pages                  // 页面（首页、详情等）
   └──pc                           // 电脑端产品
      └──src/main/ets
         ├──pages                  // 电脑页面
         ├──pcability              // 电脑入口 Ability
         ├──view                   // 电脑标题栏组件
         ├──viewmodel              // 电脑视图模型
         └──window                 // 电脑窗口管理
```

## 移动端页面

本章介绍如何针对直板机、阔折叠、双折叠、三折叠和平板设备，使用“一多”布局能力，实现新闻阅读应用页面层级“一套代码、多端适配”。同时，介绍上述设备的窗口适配方案，以及各页面的交互开发和功能开发方案。

### 窗口适配

* 窗口模式

  多设备新闻阅读示例，根据适配的设备，涉及全屏模式、分屏模式、悬浮窗模式、自由窗口模式，可参考[窗口模式](bpta-multi-device-window-mode.md)。其中分屏模式与悬浮窗通常无特殊设计，可通过系统方式进入。应用监听窗口尺寸变化，[通过断点刷新UI](bpta-multi-device-responsive-layout.md#section175001836203617)，将自动适配全屏、分屏、悬浮窗、自由窗口模式下的布局。

* 窗口方向

  通过设置[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)设置应用窗口方向，在新闻阅读应用中，[Orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)参数设置为FOLLOW\_DESKTOP，使应用跟随桌面的旋转策略。在该旋转策略下，在直板机上推荐仅竖屏显示，在双折叠展开态、三折叠展开态、平板等大屏幕场景下推荐四方向旋转并受控制中心的旋转开关控制。具体说明可参考[为应用配置旋转策略](bpta-multi-device-window-direction.md#section714419371037)。

* 窗口沉浸式

  为了更好的视觉观感，新闻阅读应用通常将顶部状态栏设置为全局沉浸。根据UX设计，需要实现不同窗口模式（全屏、分屏、悬浮窗）下窗口的沉浸式，可参考[窗口沉浸式](bpta-multi-device-window-immersive.md)。全屏、分屏和悬浮窗的沉浸式均可通过[setWindowLayoutFullscreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)实现，并进行动态安全区避让。

### 首页推荐页

首页推荐页包含热点要闻、大图轮播、上文下图卡片和新闻列表等多个内容区块。在直板机上这些区块纵向单列排列，在折叠屏展开态和平板上需要以双列栅格展示并控制摘要内容的显隐，同时顶部搜索栏和子Tab栏的排列方式也需随横向断点切换。

设备效果图如下：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **横向（/纵向）断点** | **sm/md** | **sm/lg** | **md** | **lg、xl** |
| 首页推荐页 |  |  |  |  |

**界面开发**

移动端首页推荐页页各区域介绍及实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 顶部页签及搜索框 | 使用[GridRow](../harmonyos-references/ts-container-gridrow.md)栅格组件实现，在不同横向断点下，通过设置GridCol的span和order，实现搜索框和页签的上下或左右布局：直板机设备搜索框占满整行在上、页签在下；puraX外屏或横向断点为md及以上时页签居左、搜索框居右。 |
| 2 | 热点要闻 | 使用[List](../harmonyos-references/ts-container-list.md)组件实现，通过lanes属性按断点分栏：横向断点为sm时1列、md时2列、lg/xl时3列。 |
| 3 | 大图轮播 | 使用[Swiper](../harmonyos-references/ts-container-swiper.md)组件实现，通过displayCount按断点切换显示数量（横向断点下sm为1，md为2，lg/xl为3）。 |
| 4 | 上文下图卡片 | 使用Column纵向排布标题和多张图片实现上文下图卡片。横向断点为sm/md时展示1条，lg/xl断点下通过Row并排展示2条。 |
| 5 | 新闻列表 | 横向断点为sm时单列展示，md及以上断点使用[GridRow](../harmonyos-references/ts-container-gridrow.md)双列栅格展示。 |
| 6 | 底部/侧边页签 | 使用[HdsTabs](../harmonyos-references/ui-design-hdstabs.md)组件实现，配置[barFloatingStyle](../harmonyos-references/ui-design-hdstabs.md#barfloatingstyle)悬浮样式和沉浸光感材质，不支持该材质的设备自动降级。 |

### 新闻详情页

新闻详情页包含文章正文和评论区两部分。在直板机设备上，正文与评论区需纵向排列；在大屏设备上，二者并排展示，评论区作为侧栏可独立滚动。底部悬浮工具栏在API 26及以上设备使用[沉浸光感](bpta-spatiality-immersive.md)，低版本降级为背景模糊。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **横向（/纵向）断点** | **sm/md** | **sm/lg** | **md** | **lg、xl** |
| 新闻详情页 |  |  |  |  |

**界面开发**

移动端新闻详情页各区域介绍及实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 新闻标题和作者区 | 使用Column纵向排布新闻标题和作者行，作者行使用Row横排头像、名称、发布时间和关注按钮，内边距按断点调整。 |
| 2 | 内容区 | 正文图文使用[Scroll](../harmonyos-references/ts-container-scroll.md)承载滚动展示。小屏下与标题、评论区纵向堆叠统一滚动。 |
| 3 | 评论区 | 使用List展示评论列表。横向断点为md及以上时置于[SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md)右侧侧栏独立滚动；横向断点为sm时堆叠于正文下方。 |
| 4 | 底部悬浮工具栏 | 使用Stack悬浮于内容上方。API 26及以上通过[systemMaterial()](../harmonyos-references/ts-universal-attributes-image-effect.md#systemmaterial)应用沉浸光感材质，低版本使用[backgroundBlurStyle()](../harmonyos-references/ts-universal-attributes-background.md#backgroundblurstyle9)背景模糊降级。 |

## 电脑端页面

本章介绍如何基于现有移动端界面开发方案，实现代码逻辑与布局复用，高效完成新闻阅读应用在电脑设备上的界面开发。电脑端的新闻阅读应用大部分交互逻辑与移动端应用类似，本章只展示两者的差异。

### 窗口适配

* 窗口模式

  新闻阅读应用在电脑端上支持全屏和自由窗口两种模式，具体实现可参考[窗口模式](bpta-multi-device-window-mode.md)。应用内使用响应式组件，即可根据窗口大小，自动适配全屏和自由窗口模式下的布局。
* 窗口沉浸式

  根据UX设计规范，需要实现全屏和自由窗口下的沉浸式效果，具体实现可参考[窗口沉浸式](bpta-multi-device-window-immersive.md)。全屏模式下，通过[window.setWindowLayoutFullscreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)实现沉浸式。自由窗口模式下，通过[window.setWindowDecorVisible()](../harmonyos-references/arkts-apis-window-window.md#setwindowdecorvisible11)隐藏标题栏，仅保留右上角三键，使页面内容延伸至标题栏区域，实现沉浸式显示效果。

### 首页推荐页

电脑端首页推荐页的页签栏展示在左侧，右侧承载内容区。效果图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/SIdhM2nGQQKu960jzEZvWQ/zh-cn_image_0000002722887399.png "点击放大")

**界面开发**

电脑端首页推荐页与移动端大屏布局基本一致，主要包含以下区域：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 沉浸式标题栏 | 通过[window.setWindowLayoutFullscreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)让内容占据标题栏区域，[window.setWindowDecorVisible()](../harmonyos-references/arkts-apis-window-window.md#setwindowdecorvisible11)隐藏默认装饰。使用Stack布局实现。左侧展示应用图标和名称，右侧依次放置顶部页签、加号按钮和搜索框，同时避让三键区。 |
| 2 | 左侧tab栏 | 左侧[HdsTabs](../harmonyos-references/ui-design-hdstabs.md)设置vertical(true)使页签栏竖向展示。 |
| 3 | 内容区 | 与xl断点下的移动端布局一致，实现方案可参考移动端[首页推荐页](multi-news-read.md#section197614546219)。 |

### 新闻详情页

电脑端新闻详情页左侧为新闻内容、右侧展示评论区，底部嵌入工具栏。运行效果如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/ss_gmOBZT4iXUD4_sTjRNg/zh-cn_image_0000002693207824.png "点击放大")

**界面开发**

电脑端新闻详情页与移动端大屏布局基本一致，主要包含以下区域：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 内容区 | 左侧部分，和xl断点下的移动端布局一致，实现方案可参考移动端[新闻详情页](multi-news-read.md#section1813183410226)。 |
| 2 | 底部功能区 | 将功能按钮横排在内容区底部，作为内嵌工具栏参与正常布局，不再悬浮遮挡内容。 |
| 3 | 评论区 | 右侧部分，和xl断点下的移动端布局一致，实现方案可参考移动端[新闻详情页](multi-news-read.md#section1813183410226)。 |

## 示例代码

[多设备新闻阅读界面](https://gitcode.com/HarmonyOS_Samples/multi-news-read)
