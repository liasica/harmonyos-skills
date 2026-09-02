---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-settings-application-page
title: 多设备设置界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备设置界面
category: best-practices
scraped_at: 2026-09-02T15:03:19+08:00
doc_updated_at: 2026-05-22
content_hash: sha256:e8b97291b8ed06da4d9a65190dfd0893cc41758cad82a295c4fd2d72942b28b3
---

## 概述

本文从当前常见的多设备应用场景中选取设置应用作为典型案例，详细阐述“一多”理念在实际开发中的应用。设置应用主要展示导航页列表及内容页在不同设备上的呈现方式，并介绍路由跳转功能。

当前应用已适配的设备包括：直板机、双折叠（Mate X系列）、三折叠、阔折叠、平板和电脑。

下文将从UX设计、工程管理、移动端页面和电脑端页面四个角度，介绍“一多”设置应用在开发过程中的最佳实践。

**说明** 

阅读本文前，建议开发者先了解[ArkUI（方舟UI框架）](../harmonyos-guides/arkui.md)和[一次开发，多端部署概览](bpta-multi-device-overview.md)相关知识。

* [UX设计](bpta-multi-settings-application-page.md#section99762271515)：介绍设置应用的交互逻辑与通用设计要点，开发者可直接参考。
* [工程管理](bpta-multi-settings-application-page.md#section719020851716)：介绍“一多”工程所需配置，并推荐采用结构更清晰的三层架构。
* [移动端页面](bpta-multi-settings-application-page.md#section202931220101020)和[电脑端页面](bpta-multi-settings-application-page.md#section5748352172710)：遵循实际应用开发流程，以页面为基本单元，依次讲解窗口适配、页面开发及功能开发的设计思路与实现方式。

## UX设计

设计参考图如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/SXmQ3C9ES2GvK8qEoU_3Qg/zh-cn_image_0000002579408634.png "点击放大")

## 工程管理

为确保“一多”工程代码的复用性与可维护性，推荐开发者采用分层架构组织代码工程。该架构将项目划分为产品定制层（products）、基础特性层（features）和公共能力层（common）三个层级，各层级权责明确且功能独立，为开发者提供了清晰、高效且可扩展的设计方案。关于分层架构的具体设计细节，可参考[分层架构设计](bpta-layered-architecture-design.md)。

### 创建工程

建议开发者参考[多设备工程部署与发布](bpta-multi-device-ide.md)相关内容，掌握分层架构工程的创建与配置方法后，创建模板项目工程。根据设置应用的开发需求进行针对性修改，确保工程架构贴合实际业务需求。

### 工程结构

应用采用推荐的分层架构，将代码工程按products、features、common三个层级组织代码工程。各层级设计如下：

* products层：应用需适配的设备包括直板机、双折叠（Mate X系列）、三折叠、阔折叠、平板及电脑。由于电脑界面布局与其他设备差异较大，因此单独创建名为“pc”的包作为电脑设备的应用入口；直板机、双折叠（Mate X系列）、三折叠、阔折叠及平板设备的界面布局整体相似，部分差异可通过“一多”[自适应布局](bpta-multi-device-adaptive-layout.md)和[响应式布局](bpta-multi-device-responsive-layout.md)适配，为此创建名为“default”的包作为这些设备的应用入口。
* features层：包含一个核心业务模块——网络连接（multisettinglink）。模块对应创建HAR包，供products层按需引用。
* common层：为实现代码复用并减少冗余，集中存放公共常量、日志工具类及窗口管理工具等基础能力，供其他模块统一调用。

工程结构如下：

```screen
├──common                                          // 公共模块层
│  └──multisettingbase                             // 公共能力模块
│     ├──src/main/ets                              // 代码区
│     │  ├──model                                  // 数据模型
│     │  ├──utils                                  // 工具类
│     │  └──view                                   // 公共视图组件
│     └──src/main/resources                        // 资源目录
├──features                                         // 功能模块层
│  └──multisettinglink                             // 网络连接功能模块
│     ├──src/main/ets                              // 代码区
│     │  ├──model                                  // 数据模型
│     │  ├──view                                   // 视图组件
│     │  └──viewmodel                              // 视图模型
│     └──src/main/resources                        // 资源目录
└──products                                        // 产品层
   ├──default                                      // 手机/平板设备入口
   │  ├──src/main/ets                              // 代码区
   │  │  ├──common                                 // 公共常量
   │  │  ├──entryability                           // 应用入口能力
   │  │  ├──entrybackupability                     // 备份能力
   │  │  ├──pages                                  // 页面
   │  │  ├──view                                   // 视图组件
   │  │  └──viewmodel                              // 视图模型
   │  └──src/main/resources                        // 资源目录
   └──pc                                           // 电脑设备入口
      ├──src/main/ets                              // 代码区
      │  ├──common                                 // 公共常量
      │  ├──pages                                  // 页面
      │  ├──pcability                              // 电脑应用入口能力
      │  ├──pcbackupability                        // 电脑备份能力
      │  ├──view                                   // 视图组件
      │  └──viewmodel                              // 视图模型
      └──src/main/resources                        // 资源目录
```

## 移动端页面

本章介绍如何针对直板机、双折叠（Mate X系列）、三折叠、阔折叠、平板设备上的设置应用，利用“一多”布局能力，实现页面层级“一套代码、多端适配”的目标。同时，阐述这些设备上的窗口适配方案。

### 窗口适配

* 窗口模式

  适配设备支持全屏、分屏、悬浮窗和自由窗口模式，具体参见[窗口模式](bpta-multi-device-window-mode.md)。其中，分屏模式与悬浮窗无需特殊设计，可通过系统方式进入。应用内监听窗口尺寸变化，[通过断点刷新UI](bpta-multi-device-responsive-layout.md#section175001836203617)，自动适配全屏、分屏、悬浮窗和自由窗口模式下的布局。
* 窗口方向

  通过[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)，将[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)的orientation属性设置为跟随桌面的旋转模式（follow\_desktop）。
* 窗口沉浸式

  根据UX设计，需实现不同窗口模式（全屏、分屏、悬浮窗、自由窗口）下的沉浸式效果，可参考[窗口沉浸式](bpta-multi-device-window-immersive.md)。推荐开发者使用组件级沉浸方案（组件设置页面沉浸）[实现沉浸式效果](bpta-multi-device-window-immersive.md#section180431120426)，同时需进行动态安全区避让，确保沉浸式显示效果。自由窗口模式下，使用[window.setWindowDecorVisible(false)](../harmonyos-references/arkts-apis-window-window.md#setwindowdecorvisible11)隐藏标题栏，仅保留右上角三键，使应用页面延伸至标题栏区域，实现沉浸式显示效果。

### 导航与详情页

设置应用导航与详情页主要展示列表按钮以及对应详情页，点击导航按钮实现详情页跳转。根据功能设计，应用首页相关内容划分为6个区域，效果图如下：

| 横向断点 | sm | md | lg、xl |
| --- | --- | --- | --- |
| 首页 |  |  |  |

**界面开发**

具体介绍及实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 导航页标题栏 | 使用[HdsNavigation](../harmonyos-references/ui-design-hdsnavigation.md)实现，通过[titleMode](../harmonyos-references/ui-design-hdsnavigation.md#titlemode)属性设置为小标题模式，并设置[titleBar](../harmonyos-references/ui-design-hdsnavigation.md#titlebar)实现模糊样式及沉浸光感样式。 |
| 2 | 搜索栏 | 使用[Search](../harmonyos-references/ts-basic-components-search.md)组件实现，支持文本输入功能。 |
| 3 | 导航按钮列表 | 列表基于[List](../harmonyos-references/ts-container-list.md)组件实现，自定义单个按钮组件，支持传入不同参数展示不同样式，并通过系统路由表实现点击跳转至对应目标页。 |
| 4 | 内容页标题栏 | 使用[HdsNavDestination](../harmonyos-references/ui-design-hdsnavdestination.md)实现，通过[titleMode](../harmonyos-references/ui-design-hdsnavigation.md#titlemode)属性设置为小标题模式，并设置[titleBar](../harmonyos-references/ui-design-hdsnavigation.md#titlebar)实现模糊样式、沉浸光感样式及标题栏按钮。 |
| 5 | WLAN页设置按钮列表 | 列表基于[List](../harmonyos-references/ts-container-list.md)组件实现，自定义单个按钮组件，支持传入不同参数展示不同样式，开关按钮使用[Toggle](../harmonyos-references/ts-basic-components-toggle.md)实现。 |
| 6 | WLAN列表 | 列表基于[List](../harmonyos-references/ts-container-list.md)组件实现，自定义WLAN组件显示WLAN信息及图标。 |

**路由跳转**

通过[HdsNavigation](../harmonyos-references/ui-design-hdsnavigation.md)组件、[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)对象、[HdsNavDestination](../harmonyos-references/ui-design-hdsnavdestination.md)组件及系统路由表实现页面路由跳转。

* HdsNavigation组件用于展示导航按钮列表，按钮通过点击事件调用NavPathStack对象的[pushPathByName](../harmonyos-references/ts-basic-components-navigation.md#pushpathbyname10)方法跳转至指定页面。
* HdsNavDestination组件用于构建HdsNavigation组件的子页面，组件中需声明@Builder对外实例化方法，用于注册系统路由表。
* 在系统路由表中注册子页面实例化方法、源码所在路径及唯一标识符，系统路由表文件路径为entry/src/main/resources/base/profile/router\_map.json。

更多内容参考[Navigation页面路由](../harmonyos-guides/arkts-navigation-jump.md)。

## 电脑端页面

本章介绍如何基于现有移动端界面开发方案，实现代码逻辑与布局复用，高效完成电脑设备上设置应用的界面开发。

### 导航与详情页

设置应用导航与详情页主要展示列表按钮及对应详情页，点击导航按钮实现详情页跳转。根据功能设计，应用首页相关内容划分为6个区域，效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/-0NxaBh8QyuOaO0PZczl-A/zh-cn_image_0000002579408636.png "点击放大")

**界面开发**

具体介绍及实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 导航页标题栏 | 使用[window.setWindowDecorVisible(false)](../harmonyos-references/arkts-apis-window-window.md#setwindowdecorvisible11)隐藏标题栏，并通过自定义组件实现标题功能。 |
| 2 | 搜索栏 | 复用移动端导航与详情页对应区域的布局实现方案。 |
| 3 | 导航按钮列表 |
| 4 | 内容页标题栏 |
| 5 | WLAN页设置按钮列表 |
| 6 | WLAN列表 |

**路由跳转**

同移动端页面-[导航与详情页](bpta-multi-settings-application-page.md#section16469195751520)-路由跳转。

## 示例代码

[多设备设置界面](https://gitcode.com/HarmonyOS_Samples/NavigationSettings)
