---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/multi-travel-navigation
title: 多设备地图导航界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备地图导航界面
category: best-practices
scraped_at: 2026-09-02T15:03:19+08:00
doc_updated_at: 2026-08-10
content_hash: sha256:6366e0a2ca75ef235395775604d3a9e1777a699ffa7f537a09872ced689bf0d6
---

## 概述

本文从当前常见的多设备应用场景中，选取地图导航应用作为典型案例，详细介绍“一多”在实际开发中的应用。

地图导航应用的核心，是实现地图画布、地点搜索、路线规划与导航状态这四大模块间的流畅切换与稳定协同。既要保障用户在不同设备上打开应用时，获得连续一致的搜索与导航体验，避免搜索面板遮挡地图Logo、定位按钮和路线信息，同时也要充分利用折叠屏、平板和电脑的大窗口能力，获得更好的视觉观感与交互体验。

当前应用已适配的设备包括：直板机、双折叠（Mate X系列）、三折叠、阔折叠、平板和电脑。

**说明** 

开发者在开发地图导航应用前，需要进行前置开发准备：

* 申请位置权限，可参考[申请位置权限开发指导](../harmonyos-guides/location-permission-guidelines.md)；
* 开通地图服务，可参考Map Kit指南中的[开发准备](../harmonyos-guides/map-config-agc.md)；
* 若需体验实况窗功能，可参考Live View Kit（实况窗服务）中的[开发准备](../harmonyos-guides/liveview-preparations.md)。

在阅读本文前，建议开发者先了解[ArkUI（方舟UI框架）](../harmonyos-guides/arkui.md)和[一次开发，多端部署概览](bpta-multi-device-overview.md)相关知识。

下文将从UX设计、工程管理、页面开发三个角度，详细介绍地图导航应用在多设备开发中的最佳实践，为开发者提供可参考的落地思路。

* [UX设计](multi-travel-navigation.md#section73614881015)：介绍地图导航应用在不同设备上的交互逻辑和通用设计要点，可供同类地图导航应用开发者直接参考复用。
* [工程管理](multi-travel-navigation.md#section1220019261104)：推荐“一多”应用采用分层架构，通过清晰的目录结构组织地图容器、地点探索、实况窗和产品入口。
* [移动端页面](multi-travel-navigation.md#section141711741141)、[电脑端页面](multi-travel-navigation.md#section65701625122313)：按照实际应用开发流程，以页面为基本单元，分别讲解移动端、电脑端页面在窗口适配、页面开发、交互开发及功能开发等环节的设计思路与具体实现方法。

## UX设计

出行导航类场景通常包含查询地点信息、路线建议、导航、打车等核心功能，用户可以通过悬浮面板体验到面板与底层地图间的交互，围绕此核心场景，此类应用有如下特点：

* 手机使用底部半模态面板，其他设备上使用侧边半模态面板。
* 面板支持多档位高度滑动调节。
* 面板默认高度，需要依据屏幕尺寸的不同而有所区分，充分发挥屏幕尺寸优势。
* 折叠屏&平板上侧边的半模态面板支持用户自行拖拽至左侧或右侧位置。
* 建议折叠屏和平板等宽屏设备上，Tab放置在半模态面板内。

地图导航应用的UX设计可参考[出行导航类](../design-guides/travel-and-navigation-0000001957391017.md)多设备响应式设计指南，设计参考图如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/G1Qz6F8sRhGKs5_M7f0K9Q/zh-cn_image_0000002584589316.png "点击放大")

## 工程管理

考虑到“一多”工程代码的复用性和可维护性，推荐开发者使用分层架构组织代码工程。分层架构将项目工程划分为产品定制层（products）、基础特性层（features）和公共能力层（commons）三个层级，各层级权责清晰、各司其职，为开发者提供了一套清晰、高效且可扩展的设计架构。关于分层架构的具体设计细节，可参考[分层架构设计](bpta-layered-architecture-design.md)。

### 创建工程

建议开发者参考[多设备工程部署与发布](bpta-multi-device-ide.md)相关内容，掌握分层架构工程的创建与配置方法后，创建出模板项目工程。然后根据地图导航应用的开发需求进行针对性修改，确保工程架构贴合实际业务需求。

### 工程结构

在创建“一多”工程时，开发者会面临工程结构目录的划分问题。考虑到复用性和可维护性，本文以地图导航应用为例，提供推荐的参考方案。

HarmonyOS的分层架构主要包括三个层次：产品定制层、基础特性层和公共能力层，为开发者构建了一个清晰、高效、可扩展的设计架构。更多详情请参考[分层架构设计](bpta-layered-architecture-design.md)的逻辑设计。

地图导航应用根据一多推荐的commons、features、products的“三层工程架构”划分目录。各层级设计如下：

* commons层：集中存放窗口管理、断点工具、定位状态、地图状态和公共常量等需要被不同页面依赖引用的内容，实现代码复用并减少冗余。

* features层：地图容器、地点探索和实况窗能力相互独立，根据业务职责划分为三个业务模块：地图容器（mapcontainer）、地点探索（poiexplore）和实况窗（maplive）。
* products层：多设备地图导航应用需要适配的设备包括直板机、双折叠（Mate X系列）、三折叠、阔折叠、平板和电脑。由于电脑界面布局与其他设备有一定差异。因此单独创建“pc”的HAP包作为电脑设备应用入口；直板机、双折叠（Mate X系列）、三折叠、阔折叠、平板界面布局整体相似，部分差异可以通过“一多”的[自适应布局](bpta-multi-device-adaptive-layout.md)和[响应式布局](bpta-multi-device-responsive-layout.md)进行适配，为此创建名为“default”的HAP包作为这些设备的应用入口。

工程结构如下：

```screen
├──commons                                // 公共能力层
│  └──multitravelbase                     // 公共基础模块
│     └──src
│        └──main
│           ├──ets
│           │  ├──constants               // 公共常量
│           │  ├──model                   // 跨模块共享状态和数据模型
│           │  └──utils                   // 日志、位置、窗口、地图场景、资源文本等公共工具
│           └──resources                  // 公共资源
├──features                               // 基础特性层
│  ├──mapcontainer                        // 地图容器模块
│  │  └──src
│  │     └──main
│  │        ├──ets
│  │        │  ├──model                   // 地图视口、边距等地图容器模型
│  │        │  ├──pages                   // 地图主界面页面入口
│  │        │  ├──view                    // 地图画布、面板容器、PC装饰工具栏等视图
│  │        │  └──viewmodel               // 地图主界面状态管理
│  │        └──resources                  // 地图容器资源
│  ├──maplive                             // 实况窗模块
│  │  └──src
│  │     └──main
│  │        ├──ets
│  │        │  ├──constants               // 实况窗常量
│  │        │  └──viewmodel               // 实况窗控制逻辑
│  │        └──resources                  // 实况窗资源
│  └──poiexplore                          // 兴趣点探索模块
│     └──src
│        └──main
│           ├──ets
│           │  ├──constants               // 兴趣点探索常量
│           │  ├──model                   // 首页展示、地点详情、搜索和路线规划数据模型
│           │  ├──view                    // 首页、搜索、详情、路线规划等视图
│           │  └──viewmodel               // 搜索、地点详情和路线规划视图模型
│           └──resources                  // 兴趣点探索资源
└──products                               // 产品定制层
   ├──default                             // 默认（手机/平板）产品
   │  └──src
   │     └──main
   │        ├──ets
   │        │  ├──defaultability          // 默认产品入口
   │        │  └──pages                   // 默认产品页面
   │        └──resources                  // 默认产品资源
   └──pc                                  // 电脑产品
      └──src
         └──main
            ├──ets
            │  ├──pages                   // 电脑产品页面
            │  └──pcability               // 电脑产品入口
            └──resources                  // 电脑产品资源
```

## 移动端页面

本章将介绍如何针对直板机、双折叠（Mate X系列）、三折叠、阔折叠和平板设备，使用“一多”的布局能力，实现地图导航应用页面层级“一套代码、多端适配”。同时，介绍上述移动设备的窗口适配方案，以及各页面的交互开发和功能开发。

### 窗口适配

* 窗口模式

  多设备地图导航示例，根据适配的设备，涉及全屏模式、分屏模式、悬浮窗模式、自由窗口模式，可参考[窗口模式](bpta-multi-device-window-mode.md)。其中分屏模式与悬浮窗通常无特殊设计，可通过系统方式进入。应用监听窗口尺寸变化，[通过断点刷新UI](bpta-multi-device-responsive-layout.md#section175001836203617)，将自动适配全屏、分屏、悬浮窗、自由窗口模式下的布局。

* 窗口方向

  通过设置[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)设置应用窗口方向，在地图导航应用中，[Orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)参数设置为FOLLOW\_DESKTOP，使应用跟随桌面的旋转策略。在该旋转策略下，在类直板机上推荐仅竖屏显示，在双折叠展开态、三折叠展开态、平板等大屏幕场景下推荐四方向旋转并受控制中心的旋转开关控制。具体说明可参考[为应用配置旋转策略](bpta-multi-device-window-direction.md#section714419371037)。

* 窗口沉浸式

  为了更好的视觉观感，地图导航应用通常将底部的地图画布设置为全局沉浸。根据UX设计，需要实现不同窗口模式（全屏、分屏、悬浮窗）下窗口的沉浸式，可参考[窗口沉浸式](bpta-multi-device-window-immersive.md)。全屏、分屏和悬浮窗的沉浸式均可通过[setWindowLayoutFullscreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)实现，并进行动态安全区避让。

### 地图容器页

地图容器页是地图导航应用的基础页面，负责承载地图画布、操作按钮和业务内容面板。多设备效果图如下：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **横向（/纵向）断点** | **sm/md** | **sm/lg** | **md** | **lg、xl** |
| 地图容器 |  |  |  |  |

**界面开发**

在移动端的地图容器页，信息面板覆盖在地图画布上，主要包含以下区域：

|  |  |  |
| --- | --- | --- |
| **区域编号** | **简介** | **实现方案** |
| 1 | 地图画布 | 使用[Map Kit（地图服务）](../harmonyos-guides/map-kit-guide.md)的[MapComponent](../harmonyos-references/map-mapcomponent.md#mapcomponent)创建地图，并通过[MapComponentController](../harmonyos-references/map-map-mapcomponentcontroller.md)更新定位、标记和路线。 |
| 2 | 信息面板 | 自定义信息面板承载业务内容，使用[Stack](../harmonyos-references/ts-container-stack.md)组件覆盖在地图上展示。 |

在不同设备形态下，可以将设备类型和断点映射为地图面板不同布局，屏蔽业务对断点的直接感知。覆盖式布局再根据断点细分为底部面板、底部Mini面板和悬浮面板。

|  |  |  |  |
| --- | --- | --- | --- |
| **设备或窗口场景** | **横向（/纵向）断点** | **内容面板形态** | **设计说明** |
| 直板机、Pura X内屏 | sm/lg | 底部面板 | 三档高度，地图横向空间有限，面板从底部展开，保留地图主要信息。 |
| Pura X外屏 | sm/md | 底部Mini面板 | 两档高度，小方形屏需减少面板遮挡，优先展示核心信息。 |
| 双折叠、三折叠、平板 | md、lg、xl | 悬浮面板 | 面板悬浮在地图侧边，可同时查看信息面板与地图点位。 |

**交互开发**

地图容器页主要处理容器级交互，不承载具体业务页面的交互逻辑，包含以下交互：

* 面板档位/位置切换：底部面板支持上下拖动切换高度档位，悬浮面板除了支持高度档位切换外，还支持左右拖动切换吸附位置。面板交互完成后，地图容器根据面板高度、侧边位置和可见状态重新计算地图可视区域，使地图Logo、定位控件和路线内容避开面板区域。

底部面板通过[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)监听上下拖动，悬浮面板通过PanGesture监听上下和左右拖动；面板高度或位置变化后，地图容器重新计算地图Padding，并调用Map Kit的[MapController.setPadding()](../harmonyos-references/map-map-mapcomponentcontroller.md#setpadding)更新地图可视区域。

面板档位/位置切换示意图如下所示（以首页为例）：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **横向（/纵向）断点** | **sm/md** | **sm/lg** | **md** | **lg、xl** |
| 低档位 | / |  |  |  |
| 中档位 |  |  |  |  |
| 高档位 |  |  |  |  |
| 位置切换 | / | / |  |  |

**功能开发**

地图容器页负责地图实例和地图基础能力的初始化，同时统一维护地图与业务面板之间的状态联动。首页、地点搜索、地点详情和路线规划等业务页面只更新业务状态，地图容器根据当前状态统一刷新地图内容，避免地图标记、选中地点和路线绘制分散在各个业务页面中处理。

地图容器页功能开发流程如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/akjo0ePgSnyAeoXJEoKxPA/zh-cn_image_0000002614909169.png "点击放大")

地图容器页主要包含以下功能：

* 创建地图组件：使用[Map Kit（地图服务）](../harmonyos-guides/map-kit-guide.md)的[MapComponent](../harmonyos-references/map-mapcomponent.md#mapcomponent)创建地图实例，并通过回调获取[MapComponentController](../harmonyos-references/map-map-mapcomponentcontroller.md)，为后续定位、标记、路线绘制和地图避让提供控制入口。获取MapComponentController后，开启我的位置、复位按钮、实时路况和建筑物显示等地图基础能力；其中，复位按钮用于快速回到当前位置，底部面板场景下可隐藏缩放控件，避免控件与面板重叠。
* 设置当前位置：定位成功后，地图容器通过[MapController.setMyLocation()](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocation)设置当前位置，并在坐标转换后通过[MapController.animateCamera()](../harmonyos-references/map-map-mapcomponentcontroller.md#animatecamera)移动地图镜头，保证用户进入页面后能快速看到当前位置附近的地图内容。
* 更新业务状态：业务页面更新当前地图状态、选中地点、搜索结果和路线数据，地图容器监听状态变化，并统一触发地图内容刷新。
* 刷新地图内容：地图容器根据当前业务场景区分首页、搜索结果、地点详情和路线规划等场景。

### 首页

首页是用户进入应用后的默认业务面板，主要承载搜索入口、常用出行功能、地点推荐和快捷操作。该页面的目标是让用户快速发起搜索或选择目的地，同时尽量不破坏地图浏览体验。多设备效果图如下：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **横向（/纵向）断点** | **sm/md** | **sm/lg** | **md** | **lg、xl** |
| 面板类型 | 底部Mini面板 | 底部面板 | 悬浮面板 | 悬浮面板 |
| 首页 |  |  |  |  |

**界面开发**

在直板机和Pura X内屏上，首页内容放在底部面板中，低档位优先露出搜索入口和核心功能，高档位展示更多推荐内容。在Pura X外屏上，Mini面板减少内容密度，只保留搜索和关键操作。在双折叠、三折叠和平板上，首页面板以悬浮方式展示在地图侧边，用户可以一边浏览推荐地点，一边观察地图点位。

首页主要包含以下区域：

|  |  |  |
| --- | --- | --- |
| **区域编号** | **简介** | **实现方案** |
| 1 | 搜索入口 | 使用[TextInput](../harmonyos-references/ts-basic-components-textinput.md)组件实现搜索框，结合搜索图标、清除图标和提交事件完成地点搜索入口。 |
| 2 | 出行功能区 | 使用网格容器[Grid](../harmonyos-references/ts-container-grid.md)实现，展示出行功能入口，通过[columnsTemplate](../harmonyos-references/ts-container-grid.md#columnstemplate)设置宫格列数。同时，根据面板的档位切换缩略展示或者全部展示。 |
| 3 | 常用地点区 | 使用响应式组件Column组件实现，以卡片形式展示。 |
| 4 | 景点推荐区 | 使用响应式组件[List](../harmonyos-references/ts-container-list.md)展示推荐地点，并通过属性[listDirection](../harmonyos-references/ts-container-list.md#listdirection)实现横向浏览。 |
| 5 | 底部Tab栏 | 使用[HdsTabs](../harmonyos-references/ui-design-hdstabs.md)组件实现透明材质的底部页签。 |

**交互开发**

首页主要包含以下交互：

* 搜索入口交互：用户点击搜索框时，通过点击事件触发回调自动将面板提升到高档位；以直板机为例，点击搜索框面板自动升高示意图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/ZG4AixvXRUOhWuYegXbESQ/zh-cn_image_0000002584429394.gif "点击放大")

### 地点搜索页

地点搜索页用于承接用户输入关键字后的结果展示。地图导航应用中，搜索结果列表和地图标记须保持一致：列表展示的地点需要同步显示在地图上，用户选择列表项后，地图也应聚焦到对应位置。效果图如下所示：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **横向（/纵向）断点** | **sm/md** | **sm/lg** | **md** | **lg、xl** |
| 面板类型 | 底部Mini面板 | 底部面板 | 悬浮面板 | 悬浮面板 |
| 默认面板 |  |  |  |  |

**界面开发**

在底部面板场景中，搜索结果随面板档位展开：中档位下展示主要结果，高档位展示更完整的列表。在Mini面板场景中，结果信息应简化，避免类方屏上地图被过度遮挡。在悬浮面板场景中，搜索结果列表固定在地图侧边，用户可以同时查看列表和标记点。地点搜索页主要包含以下区域：

|  |  |  |
| --- | --- | --- |
| **区域编号** | **简介** | **实现方案** |
| 1 | 搜索输入区 | 复用搜索栏中的[TextInput](../harmonyos-references/ts-basic-components-textinput.md)展示搜索词，并通过提交事件重新发起地点搜索。 |
| 2 | 结果列表 | 使用List组件展示搜索结果，高档位中支持纵向滚动浏览。 |
| 3 | 地图标记 | 使用[MapController.addMarker()](../harmonyos-references/map-map-mapcomponentcontroller.md#addmarker)添加搜索结果标记，并通过[MarkerOptions](../harmonyos-references/map-common.md#markeroptions)配置标记的图标、位置和标题。 |

### 地点详情页

地点详情页连接地点搜索和路线规划，是用户确认目的地、查看地址信息并发起导航的中间页面。该页面应在有限空间中优先展示地点名称、地址和导航入口，在宽屏空间中补充更多详情信息。多设备效果图如下：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **横向（/纵向）断点** | **sm/md** | **sm/lg** | **md** | **lg、xl** |
| 面板类型 | 底部Mini面板 | 底部面板 | 悬浮面板 | 悬浮面板 |
| 地点详情页（含长截图） |  |  |  |  |

**界面开发**

在直板机和Pura X内屏上，详情页通过底部面板展示，低档位保留地点名称和路线按钮，高档位展示完整详情。在Pura X外屏上，详情内容需要控制层级，避免占用过多地图区域。在双折叠、三折叠和平板上，详情面板浮在地图侧边，用户可以同时确认地点详情和地图位置。

地点详情页主要包含以下区域：

|  |  |  |
| --- | --- | --- |
| **区域编号** | **简介** | **实现方案** |
| 1 | 地点基础信息区 | 将地点名称、营业状态、距离、地址、入口标签和地点图片组织在详情内容顶部，通过固定内边距、固定行高和[maxLines](../harmonyos-references/ts-basic-components-text.md#maxlines)控制首屏信息密度，保证底部面板、悬浮面板和侧栏中都能优先展示核心地点信息。 |
| 2 | 扩展内容区 | 将门票推荐、问答和推荐地点等内容放在同一个[Scroll](../harmonyos-references/ts-container-scroll.md)容器中；当面板为高档位或电脑端侧栏时允许纵向滚动，非高档位时关闭内容滚动，将上下拖动优先交给面板档位切换。 |
| 3 | 底部操作区 | 将收藏、分享、路线和导航操作固定在页面底部，详情内容区通过[layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)占据剩余高度，底部操作区保持固定高度并结合安全区避让，保证关键操作始终可触达。 |

### 路线规划页

路线规划页是地图导航应用的核心业务页面。用户选择目的地后，页面需要展示起终点、出行方式、路线方案列表，并在地图上同步绘制路线。该页面既要保障路线信息清晰，也要保留足够地图空间观察路线走向。多设备效果图如下：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **横向（/纵向）断点** | **sm/md** | **sm/lg** | **md** | **lg、xl** |
| 面板类型 | 底部Mini面板 | 底部面板 | 悬浮面板 | 悬浮面板 |
| 路线规划页 |  |  |  |  |

**界面开发**

在底部面板场景中，路线规划页中档位优先展示起终点、当前路线摘要和路线列表。在Mini面板场景中，路线信息需要聚焦起终点，减少多方案列表对地图的遮挡。在悬浮面板场景中，路线页面板位于地图侧边，用户可以同时查看路线摘要和地图走向。

路线规划页的具体信息和实现方案如下表所示：

|  |  |  |
| --- | --- | --- |
| **区域编号** | **简介** | **实现方案** |
| 1 | 地图路线区 | 调用[MapController.addPolyline()](../harmonyos-references/map-map-mapcomponentcontroller.md#addpolyline)绘制路线折线，并通过MapController.animateCamera()将地图镜头聚焦于路线图。 |
| 2 | 起终点信息 | 使用[TextInput](../harmonyos-references/ts-basic-components-textinput.md)组件展示起点和终点，其中终点回显当前选中的地点名称。 |
| 3 | 出行方式区 | 使用[Scroll](../harmonyos-references/ts-container-scroll.md)容器横向展示出行方式入口，并通过选中态区分当前出行方式。 |
| 4 | 路线方案列表 | 面板处于高档位时使用List组件纵向展示路线方案，面板处于中档位或Mini面板时使用横向卡片展示前3条路线。 |
| 5 | 底部交互按钮区 | 将收藏、分享和开始导航按钮固定在页面底部，底部操作区保持固定高度并结合安全区避让，保证关键操作始终可触达。 |
| 6 | 返回按钮 | 使用[Stack](../harmonyos-references/ts-container-stack.md)组件，将返回按钮叠放在地图画布上方，使得地图容器聚焦于路线信息。 |

**交互开发**

路线规划页主要包含以下交互：

* 返回地点详情：用户点击返回按钮时，页面通过按钮点击事件触发返回逻辑，调用路线清理回调并将地图状态恢复为地点详情状态，同时通过页面路由退栈[NavPathStack.pop()](../harmonyos-references/ts-basic-components-navigation.md#pop11)返回上一页。路线清理后，地图侧重新展示当前地点标记，避免路线折线继续停留在详情场景中。

  以直板机为例，返回清除路线并恢复地点标记的示意图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/ZdMlSUFcS2qAuZ4djCQf4w/zh-cn_image_0000002584589344.gif "点击放大")

**功能开发**

路线规划页主要负责路线请求、路线结果处理和地图路线同步：

* 路线请求：页面进入时将地图状态切换为路线规划状态，并清理旧路线；随后优先使用当前定位作为起点，如果当前定位尚未就绪，则等待定位结果。起点坐标会通过[map.convertCoordinateSync()](../harmonyos-references/map-map-functions.md#convertcoordinatesync)完成坐标系转换，再使用Map Kit的[navi.getDrivingRoutes()](../harmonyos-references/map-navi-api.md#getdrivingroutes)发起驾车路线规划，通过[DrivingRouteParams](../harmonyos-references/map-navi-api.md#drivingrouteparams)传入起点origins、终点destination等参数。
* 路线结果处理：路线规划成功后，页面保存路径[RouteResult.routes](../harmonyos-references/map-navi-api.md#routeresult)，并从首条路线的信息steps中提取[RouteRoad](../harmonyos-references/map-navi-api.md#routeroad)数据，用于地图侧绘制路线；同时通过路线步骤中的duration和distance汇总总耗时与总距离，并在路线列表中展示不同路线方案。
* 路线地图同步：路线道路数据准备完成后，页面通过路线就绪回调将RouteRoad传递给地图容器。地图容器将[RouteRoad.polyline](../harmonyos-references/map-navi-api.md#routeroad)转换为路线点位集合，调用[MapComponentController.addPolyline()](../harmonyos-references/map-map-mapcomponentcontroller.md#addpolyline)接口绘制路线折线，并通过[MapPolylineOptions](../harmonyos-references/map-common.md#mappolylineoptions)配置折线样式和箭头纹理；随后根据路线点位计算东北角和西南角边界，传入[map.newLatLngBounds()](../harmonyos-references/map-map-functions.md#newlatlngbounds)生成镜头更新对象，并调用[MapComponentController.animateCamera()](../harmonyos-references/map-map-mapcomponentcontroller.md#animatecamera)将路线完整展示在当前地图可视区域内。

### 实况窗

导航类应用退到后台后，用户仍希望查看距离、车辆信息或导航状态。实况窗可以在通知中心和胶囊区域展示关键状态，减少用户频繁回到应用的操作。

**说明** 

阅读本章节前，开发者需熟悉[Live View Kit简介](../harmonyos-guides/liveview-introduction.md)及[实况窗支持对接的场景](../harmonyos-guides/liveview-introduction.md#实况窗支持对接的场景)，并进行[开发准备](../harmonyos-guides/liveview-preparations.md)。下面将详细介绍实况窗在“一多”开发中的实践。

**界面开发**

实况窗页支持卡片和胶囊两种形态，卡片形态的实况窗展示在通知中心，状态栏的实况窗表现为胶囊形态。点击实况胶囊后，可展示实况卡片。在直板机和折叠屏上，可以进行以下设计：

|  |  |  |
| --- | --- | --- |
| 场景 | 实况卡片 | 实况胶囊 |
| 效果图 |  |  |

实况窗各场景的具体信息和实现方案如下表所示：

|  |  |  |
| --- | --- | --- |
| 区域编号 | 简介 | 实现方案 |
| 1 | 卡片形态 | 实况窗默认支持多端效果，本应用实现效果为[导航模板](../harmonyos-guides/liveview-create-locally.md#导航模板)，实况窗拉起时展示在通知中心，点击实况胶囊后展示在状态栏。 |
| 2 | 胶囊形态 | 实况胶囊默认支持多端效果，本应用实现效果为文本胶囊[TextCapsule](../harmonyos-references/liveview-liveviewmanager.md#textcapsule)。 |

## 电脑端页面

本章介绍如何基于现有移动端界面开发方案，实现代码逻辑与布局复用，高效完成地图导航应用在电脑设备上的界面开发。电脑端的地图导航应用大部分交互逻辑与移动端应用类似，本章只展示两者的差异。

### 窗口适配

* 窗口模式

  地图导航应用在电脑端上支持全屏和自由窗口两种模式，具体实现可参考[窗口模式](bpta-multi-device-window-mode.md)。应用内使用响应式组件，即可根据窗口大小，自动适配全屏和自由窗口模式下的布局
* 窗口沉浸式

  据UX设计规范，需要实现全屏和自由窗口下的沉浸式效果，具体实现可参考[窗口沉浸式](bpta-multi-device-window-immersive.md)。全屏模式下，通过[window.setWindowLayoutFullscreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)实现沉浸式。自由窗口模式下，通过[window.setWindowDecorVisible(false)](../harmonyos-references/arkts-apis-window-window.md#setwindowdecorvisible11)隐藏标题栏，仅保留右上角三键，使页面内容延伸至标题栏区域，实现沉浸式显示效果。

### 地图容器页

电脑端地图容器页移动端功能定位一致，信息面板固定在侧边栏，面板右侧承载地图画布和电脑端装饰工具栏。效果图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/T2n6MlMRTRWkhXZwX-J-Ww/zh-cn_image_0000002584429408.png "点击放大")

**界面开发**

电脑端地图容器页使用嵌入式布局组织侧边栏、地图画布和工具栏，主要包含以下区域：

|  |  |  |
| --- | --- | --- |
| **区域编号** | **简介** | **实现方案** |
| 1 | 固定侧栏 | 使用[SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md)容器固定侧边栏宽度，容器内部复用信息面板承载业务页面。 |
| 2 | 地图画布 | 同[地图容器页](multi-travel-navigation.md#section1728173982316)地图画布区域的布局实现方案一致。 |
| 3 | 地图操作区 | 使用[Stack](../harmonyos-references/ts-container-stack.md)组件，在地图主区域叠加工具栏区域。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/Dr85ItTYRMCubTVvMEnbrQ/zh-cn_image_0000002584589348.png "点击放大")

### 首页

电脑端首页固定展示在侧栏中，地图主区域保持完整可浏览状态。运行效果如下所示：

**界面开发**

电脑端首页固定展示在侧栏中，主要包含以下区域：

|  |  |  |
| --- | --- | --- |
| **区域编号** | **简介** | **实现方案** |
| 1 | 搜索入口 | 同[移动端首页](multi-travel-navigation.md#section1813183410226)的布局实现方案一致。 |
| 2 | 出行功能区 |
| 3 | 地点推荐区 |

### 地点搜索页

电脑端地点搜索页在侧栏中展示搜索结果列表，在地图主区域同步展示搜索结果标记。运行效果如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/tI5ub9DISPCYqmJNhiAilg/zh-cn_image_0000002614789083.png "点击放大")

**界面开发**

|  |  |  |
| --- | --- | --- |
| **区域编号** | **简介** | **实现方案** |
| 1 | 搜索输入区 | 同[移动端地点搜索页](multi-travel-navigation.md#section12545345162216)的布局实现方案一致。 |
| 2 | 结果列表 |
| 3 | 地图标记 |

### 地点详情页

电脑端地点详情页固定在侧栏中，用户可以在确认地点信息的同时查看地图中的目的地位置。运行效果如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/A9U1ideCSHGVTzkvmfJo7Q/zh-cn_image_0000002614909193.png "点击放大")

**界面开发**

电脑端地点详情页主要包含以下区域：

|  |  |  |
| --- | --- | --- |
| **区域编号** | **简介** | **实现方案** |
| 1 | 地点基础信息区 | 同[移动端地点详情页](multi-travel-navigation.md#section6685652152210)的布局实现方案一致。 |
| 2 | 扩展内容区 |
| 3 | 底部操作区 |

### 路线规划页

电脑端路线规划页在侧栏中展示起终点和路线方案，在地图主区域展示完整路线走向。运行效果如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/TijtKc0ITFSm2M2TjVJg5Q/zh-cn_image_0000002584429410.png "点击放大")

**界面开发**

电脑端路线规划页主要包含以下区域：

|  |  |  |
| --- | --- | --- |
| **区域编号** | **简介** | **实现方案** |
| 1 | 起终点信息 | 除返回按钮的位置，同[移动端路线规划页](multi-travel-navigation.md#section35318452315)的布局实现方案一致。 |
| 2 | 出行方式区 |
| 3 | 路线方案列表 | 使用纵向List列表展示路线方案，展示路线策略、总距离和总耗时。 |
| 4 | 地图路线区 | 同[移动端路线规划页](multi-travel-navigation.md#section35318452315)的布局实现方案一致。 |

## 示例代码

[多设备地图导航界面](https://gitcode.com/HarmonyOS_Samples/multi-travel-navigation)
