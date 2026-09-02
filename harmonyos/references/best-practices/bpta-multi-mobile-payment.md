---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-mobile-payment
title: 多设备移动支付界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备移动支付界面
category: best-practices
scraped_at: 2026-09-02T15:03:19+08:00
doc_updated_at: 2026-08-10
content_hash: sha256:050e925db7c1eda265eecf9d33ae85a6c68ee6e43244db0e0f868598d0850380
---

## 概述

本文从当前常见的多设备应用场景中，选择移动支付应用作为典型案例，详细介绍“一多”在实际开发中的应用。

移动支付应用的核心是为用户提供便捷的金融支付服务，主要功能涵盖扫码支付、出示收付款二维码、投资理财等。本文围绕上述核心功能，选取推荐页、扫一扫页、收付款页作为典型页面进行开发实践。开发过程遵循多设备开发的“差异性”、“一致性”、“灵活性”和“兼容性”原则，助力开发者快速掌握 “一多” 开发能力，高效实现移动支付应用相关功能。

目前该应用已适配设备包括：直板机、双折叠（Mate X系列）、三折叠、阔折叠、平板、电脑和智能穿戴。

**说明** 

阅读本文前，建议开发者先了解[ArkUI（方舟UI框架）](../harmonyos-guides/arkui.md)和[一次开发，多端部署概览](bpta-multi-device-overview.md)相关知识。

下文将从UX设计、工程管理、页面开发三个方面，系统介绍移动支付应用在实际开发中的最佳实践，为开发者提供可借鉴的实现思路。

* [UX设计](bpta-multi-mobile-payment.md#section329281918912)：介绍移动支付应用的交互逻辑和通用设计要点，可供同类移动支付应用开发者直接参考复用。
* [工程管理](bpta-multi-mobile-payment.md#section197441250917)：基于分层架构搭建 “一多” 应用代码工程，以清晰的目录结构明确各层逻辑，同时针对移动支付业务场景提供适配的工程配置方案。
* [移动端页面](bpta-multi-mobile-payment.md#section189941330999)、[电脑端页面](bpta-multi-mobile-payment.md#section188167341083)和[智能穿戴端页面](bpta-multi-mobile-payment.md#section188882391398)：按照实际应用开发流程，以页面为基本单元，分别讲解移动端、电脑端、智能穿戴端页面在窗口适配、页面开发、功能开发等环节的设计思路与具体实现方法。

## UX设计

移动支付应用的UX设计可参考[移动支付类](../design-guides/mobile-payment-0000001957421613.md)多设备响应式设计指南，设计参考图如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/Upv1YdphShyVYl_Hnvr5jA/zh-cn_image_0000002583509660.png "点击放大")

## 工程管理

为提升“一多”工程代码的复用性和可维护性，推荐开发者使用分层架构组织代码工程。分层架构将项目工程划分为产品定制层（products）、基础特性层（features）和公共能力层（common），各层级权责明确且功能独立，为开发者提供了一套清晰、高效且可扩展的设计架构。关于分层架构的具体设计细节，可参考[分层架构设计](bpta-layered-architecture-design.md)。

### 创建工程

开发者可先参考[多设备工程部署与发布](bpta-multi-device-ide.md)相关内容，掌握分层架构工程的创建与配置方法，并完成分层架构模板工程的搭建。后续再结合移动支付应用的实际开发需求进行针对性调整，使工程架构与业务场景保持一致。

### 工程结构

移动支付应用基于推荐的分层架构，按products、features、common三个层级组织代码工程。各层级设计如下：

* products层：移动支付应用需要适配的设备包括直板机、双折叠（Mate X系列）、三折叠、阔折叠、平板、电脑和智能穿戴。由于电脑和智能穿戴的界面布局与其他设备差异较大，因此在products层分别创建名称为“pc”和“watch”的HAP包，作为电脑和智能穿戴的应用入口。直板机、双折叠（Mate X系列）、三折叠、阔折叠和平板上的界面整体布局相似，部分差异可以通过“一多”的[自适应布局](bpta-multi-device-adaptive-layout.md)和[响应式布局](bpta-multi-device-responsive-layout.md)进行适配，因此在products层创建名称为“default”的HAP包作为这类设备统一的应用入口。
* features层：移动支付应用主要包含推荐页（multimobilepaymentrecommend）、扫一扫（multimobilepaymentscan）和收付款（multimobilepaymentpay）三个核心业务模块。在features层为三个业务模块分别创建对应的HAR包，供products层按需引用。各业务模块相对独立，互不依赖，便于后续工程的维护与迭代。
* common层：为实现代码复用、减少冗余，在common层创建一个基础（multimobilepaymentbase）能力HAR包。统一封装公共常量、断点工具以及窗口管理工具等多模块共用的基础能力，便于上层模块直接调用。

工程结构如下：

```screen
├──common                                        // 公共能力层
│  └──multimobilepaymentbase/src/main
│     ├──ets
│     │  ├──components
│     │  ├──data                    
│     │  ├──db                                 
│     │  └──utils   
│     └──resources                                // 应用资源       
├──features                                       // 基础特性层
│  ├──multimobilepaymentpay/src/main              // 收付款模块
│  │  ├──ets
│  │  │  ├──view
│  │  │  └──viewmodel
│  │  └──resources                                // 应用资源
│  ├──multimobilepaymentrecommend/src/main        // 推荐模块
│  │  ├──ets
│  │  │  ├──model
│  │  │  ├──view
│  │  │  └──viewmodel
│  │  └──resources                                // 应用资源
│  └──multimobilepaymentscan/src/main             // 扫码模块
│     ├──ets
│     │  ├──model
│     │  ├──view
│     │  └──viewmodel
│     └──resources
└──products                                       // 产品定制层
   ├──default/src/main                            // 手机、平板
   │  ├──ets
   │  │  ├──entryability
   │  │  ├──entrybackupability
   │  │  ├──model
   │  │  ├──pages
   │  │  ├──view
   │  │  └──viewmodel
   │  └──resources                                // 应用资源
   ├──pc/src/main                                 // 电脑
   │  ├──ets
   │  │  ├──model
   │  │  ├──pages
   │  │  ├──pcability
   │  │  ├──pcbackupability
   │  │  └──viewmodel
   │  └──resources                                
   └──watch/src/main                              // 手表
      ├──ets
      │  ├──model
      │  ├──pages
      │  ├──view
      │  ├──viewmodel
      │  ├──wearableability
      │  └──wearablebackupability
      └──resources
```

## 移动端页面

本章介绍如何针对直板机、双折叠（Mate X系列）、三折叠、阔折叠和平板设备，使用“一多”布局能力，实现移动支付应用页面层级“一套代码、多端适配”。同时，介绍上述设备的窗口适配方案。

### 窗口适配

* 窗口模式

  适配设备支持全屏、分屏和悬浮窗模式，具体参见[窗口模式](bpta-multi-device-window-mode.md)。其中，分屏模式与悬浮窗通常无特殊设计，可通过系统方式进入。应用内监听窗口尺寸变化，[通过断点刷新UI](bpta-multi-device-responsive-layout.md#section175001836203617)，即可自动适配全屏、分屏、悬浮窗模式下的布局。
* 窗口方向

  窗口显示方向通过在HAP包的module.json5文件中[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)下配置orientation属性为follow\_desktop实现，[跟随桌面的旋转模式](../harmonyos-guides/window-rotation.md#其他方向类型)。

* 窗口沉浸式

  根据UX设计规范，需要实现沉浸式效果，具体实现可参考[窗口沉浸式](bpta-multi-device-window-immersive.md)。在推荐页中，可通过window.[setWindowLayoutFullscreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)实现沉浸式，并配合动态安全区避让，确保显示效果完整。

  **说明** 

  由于扫一扫页面和收付款页面通过半模态转场实现，无法通过setWindowLayoutFullscreen()达到沉浸式的目的，需要针对性进行沉浸式处理：

  在扫一扫页面中，可以通过[ignoreLayoutSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#ignorelayoutsafearea20)，扩展相机预览时的安全区域。

  在收付款页面中，可以通过[background](../harmonyos-references/ts-universal-attributes-background.md#background10)属性，在设置背景色的同时向父组件的安全区扩展，实现沉浸式显示效果。

### 推荐页

推荐页主要展示常用功能入口与推荐产品，满足用户快速浏览信息、便捷使用的需求。按照功能设计，将推荐页相关内容划分为6个区域，效果图如下：

| 示意图 | sm | md | lg/xl |
| --- | --- | --- | --- |
| 效果图 |  |  |  |

**界面开发**

推荐页借助“一多”自适应布局的拉伸能力、占比能力和响应式组件，实现不同断点下的布局效果。

具体介绍及实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 底部页签 | 使用[HdsTabs](../harmonyos-references/ui-design-hdstabs.md)组件实现，通过[HdsTabsFloatingStyle](../harmonyos-references/ui-design-hdstabs.md#hdstabsfloatingstyle)属性设置页签栏的悬浮样式。 |
| 2 | 城市及搜索框 | 通过[Blank](../harmonyos-references/ts-basic-components-blank.md)组件填充中间空白区域，实现[拉伸能力](../harmonyos-guides-V5/adaptive-layout-V5.md#拉伸能力)。 |
| 3 | 金刚区 | 通过监听[断点](bpta-multi-device-responsive-layout.md#section1532120147301)变化改变快捷功能的形态，在横向断点为sm时呈现上下布局，大于sm时呈现左右布局。同时结合[占比能力](../harmonyos-guides-V5/adaptive-layout-V5.md#占比能力)，使其在左右布局时随着窗口的宽度变化而变化。 |
| 4 | 功能入口合集 | 采用[重复布局](bpta-multi-device-page-layout.md#section381193213517)结合断点监听，在横向断点为sm，功能呈现为2行4列；横向断点为md时，呈现为2行6列；横向断点为lg或xl时，呈现为2行8列。 |
| 5 | 服务卡片 | 采用重复布局结合断点监听，在横向断点为sm，视窗内显示1个元素；横向断点为md时，视窗内显示2个元素；横向断点为lg或xl时，显示4个元素。 |
| 6 | 财富精选 | 和服务卡片实现相同，采用重复布局结合断点监听的方式实现。 |

在实际开发中，区域1为外层页签，区域2-6为并列的推荐页内容，所以对应的开发顺序为区域1和区域2-6。

在本示例中，点击扫一扫/收付款，在不同断点下呈现效果不同：在横向断点为sm时，拉起一个独立页面；横向断点大于sm时，拉起一个弹窗。此处采用[半模态转场](../harmonyos-references/ts-universal-attributes-sheet-transition.md)实现，sm断点时设置半模态样式[sheetType](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheettype11枚举说明)为CONTENT\_COVER，即全屏弹窗；大于sm断点时设置样式为CENTER，即居中弹窗。具体实现可查看[示例代码](bpta-multi-mobile-payment.md#section22034418521)。

### 扫一扫页

扫一扫页主要功能为拉起相机进行扫码，同时提供其他相关功能入口。按照功能设计，将扫一扫页相关内容划分为4个区域，效果图如下：

| 示意图 | sm | md | lg/xl |
| --- | --- | --- | --- |
| 效果图 |  |  |  |

**界面开发**

扫一扫页借助“一多”自适应布局的均分能力，实现不同断点下的布局效果。

具体介绍及实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 画面预览区 | 使用[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件实现，具体实现逻辑可查看[示例代码](bpta-multi-mobile-payment.md#section22034418521)。 |
| 2 | 顶部按钮区 | 通过[Row](../harmonyos-references/ts-container-row.md)组件和[Button](../harmonyos-references/ts-basic-components-button.md)组件实现。若当前的半模态样式为全屏则显示，若半模态样式为居中弹窗，不显示本区域。 |
| 3 | 功能区 | 通过Row组件的[justifyContent](../harmonyos-references/ts-container-row.md#justifycontent8)属性实现[均分能力](bpta-multi-device-adaptive-layout.md#均分能力)，将其设置为SpaceEvenly，使相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距均相同。 |
| 4 | 扫描模式区 | 与功能区类似，通过Row组件的justifyContent属性实现均分能力。 |

在实际开发中，区域1为底层画面，区域2-4为并列的扫一扫页内容，所以对应的开发顺序为区域1和区域2-4。

**功能开发**

扫一扫功能通过[Scan Kit（统一扫码服务）](../harmonyos-references/scan-api.md)的能力实现。多设备开发时，某些设备可能不支持扫码功能，需要使用[canIUse](../harmonyos-references/js-apis-syscap.md#caniuse)接口查询系统能力，若支持扫码，[向用户申请授权](../harmonyos-guides/request-user-authorization.md)，调用相机，打开扫码弹窗。

在本示例中，仅实现拉起相机预览流并保存扫码数据信息，在实际开发时，需要根据业务逻辑进一步处理扫码数据。具体实现逻辑可查看[示例代码](bpta-multi-mobile-payment.md#section22034418521)。

### 收付款页

收付款页主要功能为展示收付款二维码，同时提供其他相关功能入口。按照功能设计，将收付款页相关内容划分为4个区域，效果图如下：

| 示意图 | sm | md | lg/xl |
| --- | --- | --- | --- |
| 效果图 |  |  |  |

**界面开发**

收付款页借助“一多”自适应布局的拉伸能力，实现不同断点下的布局效果。

具体介绍及实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 标题区 | 通过[Blank](../harmonyos-references/ts-basic-components-blank.md)组件填充中间空白区域，实现[拉伸能力](../harmonyos-guides-V5/adaptive-layout-V5.md#拉伸能力)。结合断点能力控制其显隐，在横向断点为sm时显示，大于sm时隐藏。 |
| 2 | 二维码区 | 通过Blank组件纵向填充空白区域，实现拉伸能力，提升视觉体验。 |
| 3 | 收款记录 | 通过断点判断其应处于二维码区域内/外，通过[visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)属性控制其显隐状态。 |
| 4 | 功能区 | 通过Blank组件填充中间空白区域实现拉伸能力，使内容始终位于容器两端。 |

在实际开发中，区域1、2、4为并列内容，3需要判断位于哪个容器中，所以对应的开发顺序为区域1、2、4和区域3。

**功能开发**

二维码通过[generateBarcode (码图生成)](../harmonyos-references/scan-generatebarcode.md)能力实现，需要设备具备码图生成能力，所以在开发时，需要通过[canIUse](../harmonyos-references/js-apis-syscap.md#caniuse)接口进行判断，防止因设备不兼容导致功能异常或崩溃。

## 电脑端页面

本章介绍如何基于现有移动端界面开发方案，实现代码逻辑与布局复用，高效完成电脑设备上移动支付应用的界面开发。

### 窗口适配

* 窗口模式

  适配设备支持自由窗口模式，具体参见[窗口模式](bpta-multi-device-window-mode.md)。应用内监听窗口尺寸变化，[通过断点刷新UI](bpta-multi-device-responsive-layout.md#section175001836203617)，即可自动适配自由窗口模式下的布局。
* 窗口沉浸式

  自由窗口模式下使用window.[setWindowDecorVisible(false)](../harmonyos-references/arkts-apis-window-window.md#setwindowdecorvisible11)设置隐藏标题栏，仅保留右上角三键。此时，应用页面拓展至标题栏区域，实现沉浸式显示效果。

### 推荐页

电脑端推荐页与移动端推荐页内容基本一致，差异点在于，移动端使用底部页签进行内容视图切换，电脑端使用侧边栏进行切换。按照模块，将推荐页相关内容划分为2个区域，效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/Qi47WKhjSDWoQT_XsCtMWg/zh-cn_image_0000002614029343.png "点击放大")

**界面开发**

推荐页定义独立的侧边栏，并复用已有的移动端页面代码即可实现。

具体介绍及实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 侧边栏 | 通过[SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md)组件，单独定义侧边栏内容。 |
| 2 | 内容区 | 复用[移动端页面](bpta-multi-mobile-payment.md#section189941330999)内容。 |

在实际开发中， 区域1为外层容器，所以对应的开发顺序为先区域1后区域2。

## 智能穿戴端页面

本章介绍如何完成智能穿戴设备上的移动支付应用开发，同时，阐述功能开发的实现方案。

### 推荐页

智能穿戴设备推荐页仅展示金刚区核心功能，并且，由于智能穿戴没有摄像头，不支持扫一扫能力，仅提供收付款、出行和卡包功能。效果图如下：

| 示意图 | xs |
| --- | --- |
| 效果图 |  |

**界面开发**

推荐页使用弧形列表[ArcList](../harmonyos-references/ts-container-arclist.md)组件实现，它支持自定义标题栏样式及子组件样式，常用于穿戴设备的开发场景。

### 收付款页

收付款页仅展示二维码，效果图如下：

| 示意图 | xs |
| --- | --- |
| 效果图 |  |

**界面开发**

页面跳转通过[Navigation](../harmonyos-references/ts-basic-components-navigation.md)和[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)组件实现，并隐藏标题栏。

**功能开发**

二维码通过[generateBarcode (码图生成)](../harmonyos-references/scan-generatebarcode.md)能力实现，需要设备具备码图生成能力，所以在开发时，需要通过[canIUse](../harmonyos-references/js-apis-syscap.md#caniuse)接口进行判断，防止因设备不兼容导致功能异常或崩溃。

## 示例代码

* [多设备移动支付界面](https://gitcode.com/HarmonyOS_Samples/multi-mobile-payment)
