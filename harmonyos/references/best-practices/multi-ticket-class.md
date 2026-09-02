---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/multi-ticket-class
title: 多设备股票类界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备股票类界面
category: best-practices
scraped_at: 2026-09-02T15:03:18+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:eb2160b60b9f7f3c9b55acf15d34eecb70e1c15e450a409eec4a215903d6898a
---

## 概述

本文以当前流行的垂类市场中的股票类应用为典型案例，详细介绍“一多”在实际开发中的应用，主要涵盖自选股和个股详情两个典型页面，展示其在直板机、双折叠、三折叠、阔折叠、平板和电脑六种产品形态上的“一次开发，多端部署”。下文将从UX设计、工程管理、移动端页面、电脑端页面四个角度，介绍“一多”股票类应用在开发过程中的最佳实践。

**说明** 

阅读本文前，建议开发者先了解[ArkUI（方舟UI框架）](../harmonyos-guides/arkui.md)和[一次开发，多端部署概览](bpta-multi-device-overview.md)相关知识。

下文将从UX设计、工程管理、页面开发三个角度，介绍股票类应用在多设备开发中的最佳实践。

* [UX设计](multi-ticket-class.md#section18423159193410)：介绍股票类应用的交互逻辑和通用设计要点，对于类似的设计要点，开发者可以直接参考。
* [工程管理](multi-ticket-class.md#section251720249266)：推荐“一多”项目采用分层架构，明确各层逻辑。同时，介绍股票类应用适用的三层架构配置。
* [移动端页面](multi-ticket-class.md#section824510452191)、[电脑端页面](multi-ticket-class.md#section2092619161616)：遵循实际应用开发流程，以页面为基本单元，分别讲解移动端、电脑端页面在窗口适配、页面开发和功能开发的设计思路与实现方法。

## UX设计

股票类应用的目的是让用户更便捷地办理金融业务。常见类型包括理财、股票、基金等应用及业务场景，核心场景有数据查看和股票交易等。

股票类应用有以下特点：

* 丰富的信息聚合。
* 图表数据高效展示。
* 便捷高效的交互方式。

此类型的应用在多端设备的使用过程中，要保障用户办理金融业务时的基本体验与功能可用性，也需着力优化大屏幕设备上的交互效率。

股票类应用的UX设计可参考金融理财类多设备响应式设计指南的[自选股](../design-guides/responsive-design-examples6-0000001793536905.md#section0732192812391)章节，设计参考图如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/2FGrU7ktQRCEZr4_Vf4c6g/zh-cn_image_0000002579631774.png "点击放大")

## 工程管理

### 创建工程

建议开发者参考[多设备工程部署与发布](bpta-multi-device-ide.md)相关内容，掌握分层架构工程的创建与配置方法后，创建出模板项目工程。然后根据股票类应用的开发需求进行针对性修改，确保工程架构贴合实际业务需求。

### 工程结构

在创建“一多”工程时，开发者会面临工程结构目录的划分问题。考虑到复用性和可维护性，本文以股票类应用为例，提供推荐的参考方案。

HarmonyOS的分层架构包括产品定制层、基础特性层和公共能力层，为开发者提供清晰、高效、可扩展的设计架构。详细请参见[分层架构设计](bpta-layered-architecture-design.md)。

股票类应用根据一多推荐的commons、features、products的"三层工程架构"划分目录。其中，features（基础特性层）按业务功能划分为三个独立模块：股票交易-stockdeal（包含买入弹窗、K线图表、交易详情等组件）、股票详情-stockdetail（包含股票详情页、多窗口入口、信息表格等）以及股票市场-stockmarket（包含市场列表组件）。公共常量、媒体播放工具以及窗口管理工具等需要被不同页面依赖引用的内容，划分为一个commons（公共能力层）：基础能力-base。products（产品定制层）包含default和pc两个模块定制了程序标准启动流程和多场景协同场景的入口能力。

工程结构如下（目录层级）：

```screen
├──commons
│  └──base/src/main
│     └──ets
│        ├──baseviews                     // 公共视图组件
│        ├──models                        // 公共数据模型
│        └──utils                         // 公共工具类
├──features
│  ├──stockdeal/src/main
│  │  └──ets
│  │     ├──chartmodels                   // 图表组件
│  │     ├──models                        // 股票交易数据模型
│  │     ├──viewmodels                    // 股票交易视图模型
│  │     └──views                         // 股票交易视图组件
│  ├──stockdetail/src/main
│  │  ├──ets
│  │  │  ├──models                        // 股票详情数据模型
│  │  │  ├──viewmodels                    // 股票详情视图模型
│  │  │  ├──pages                         // 股票详情页
│  │  │  └──views                         // 股票详情视图组件
│  └──stockmarket/src/main
│     └──ets
│        ├──models                        // 股票市场数据模型
│        ├──viewmodels                    // 股票市场视图模型
│        └──views                         // 股票市场视图组件
└──products
   ├──default/src/main
   │  ├──ets
   │  │  ├──entryability                  // 移动端程序入口
   │  │  ├──entrybackupability            // 程序备份入口
   │  │  ├──pages                         // 移动端首页
   │  │  ├──splitScreenAbility            // 分屏能力
   │  │  └──splitScreenBackupAbility      // 分屏备份能力
   │  └──resources                        // 应用静态资源目录
   └──pc/src/main
      ├──ets
      │  ├──pages                         // PC端页面
      │  ├──pcability                     // PC端程序入口
      │  └──pcbackupability               // PC程序备份入口
      └──resources                        // 应用静态资源目录
```

## 移动端页面

### 窗口适配

**窗口模式**

[多设备股票类界面](https://gitcode.com/harmonyos_samples/multi-ticket-class)示例，根据适配的设备，涉及全屏模式、分屏模式、悬浮窗模式、自由窗口模式，可参考[窗口模式](bpta-multi-device-window-mode.md)。其中分屏模式与悬浮窗通常无特殊设计，可通过系统方式进入。应用监听窗口尺寸变化，[通过断点刷新UI](bpta-multi-device-responsive-layout.md#section175001836203617)，将自动适配全屏、分屏、悬浮窗、自由窗口模式下的布局。

使用系统UI组件进入全景多窗，实现一个应用多个窗口并行运行的体验，可参考[股票详情页](multi-ticket-class.md#section46312514204)——功能开发：应用多实例-多股比价部分。

**窗口方向**

通过设置[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)使应用跟随传感器自动旋转。在类直板机上推荐仅竖屏显示，在双折叠展开态、三折叠G态、平板等大屏幕场景下推荐四方向旋转并受控制中心的旋转开关控制。在股票应用中，通过module.json5配置文件，建议设置为FOLLOW\_DESKTOP，具体说明可参考[窗口方向](bpta-multi-device-window-direction.md)。

**窗口沉浸式**

根据UX设计，实现不同窗口模式（全屏、分屏、悬浮窗）下窗口的沉浸式，可参考[窗口沉浸式](bpta-multi-device-window-immersive.md)。全屏、分屏和悬浮窗的沉浸式均可通过[setWindowLayoutFullscreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)实现，并进行动态安全区避让。

### 自选股页面

自选股页主要用于响应用户输入、展示指数、自选股票信息以及跳转股票详情页。按照功能设计，将自选股页相关内容划分为4个区域，效果图如下所示：

| 横向(/纵向)断点 | sm/md | sm/lg | md | lg |
| --- | --- | --- | --- | --- |
| 自选股页 |  |  |  |  |

**界面开发**

对各个区域使用的多种能力进行分析，实现方案如下表：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 底部/侧边页签 | 借助[响应式组件](bpta-multi-device-responsive-layout.md#section1914110349546)HdsTabs实现。同时在api版本低的设备上降级使用Tabs组件。 |
| 2 | 指数 | 最后一个组件固定，其他组件使用[List](../harmonyos-references/ts-container-list.md)实现延伸能力，随着设备宽度变大，页签间距变大，页面能够展示更多页签内容。 |
| 3 | 股票列表-工具栏 | 文字和功能按钮中间增加[Blank](../harmonyos-references/ts-basic-components-blank.md)，实现拉伸能力。 |
| 4 | 股票列表 | 通过使用[List](../harmonyos-references/ts-container-list.md)设置固定宽度和[Scroll](../harmonyos-references/ts-container-scroll.md)，可实现股票列表数据的上下或左右滑动。同时，支持对不同列设置不同的[justifyContent](../harmonyos-references/ts-container-column.md#justifycontent8)，以便实现各列的不同对齐方式。 |

* 整个页面使用的是[分栏布局](bpta-multi-device-page-layout.md#section11897247142110)，在股票列表区域，点击某一股票时，平板上会分栏显示该股票的详细信息。

### 股票详情页

股票详情页主要用于响应用户输入、展示具体股票详细信息以及查看讨论信息等内容。按照功能设计，将自选股页相关内容划分为6个区域，效果图如下所示：

| 横向(/纵向)断点 | sm/md | sm/lg | md | lg、xl |
| --- | --- | --- | --- | --- |
| 个股详情页 |  |  |  |  |

**界面开发**

对各区域使用的能力进行分析，实现方案如表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 交易操作行 | 通过为“去交易”按钮设置[layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)布局权重，并使用Blank组件结合断点，实现该按钮的自适应拉伸。 |
| 2 | 标题 | 居中显示，其他操作两端对齐，空白空间使用[Blank](../harmonyos-references/ts-basic-components-blank.md)实现自适应布局拉伸能力。 |
| 3 | 行情列表数据 | 通过[栅格](bpta-multi-device-responsive-layout.md#section1061332817545)并结合断点，控制在不同断点下显示不同的列数，列表自适应两列变多列。 |
| 4 | 中间Tab | 通过[List](../harmonyos-references/ts-container-list.md)的space属性并结合断点，控制在不同断点下ListItem之间的间距。 |
| 5 | 曲线图和柱状图 | 使用layoutWeight属性实现拉伸能力。 |
| 6 | 讨论Tab | 通过[List](../harmonyos-references/ts-container-list.md)的space属性并结合断点，控制在不同断点下ListItem之间的间距。 |

**功能开发：应用多实例-多股比价**

应用通过系统提供的[MultiWindowEntryInAPP](../harmonyos-references/ui-design-multiwindowentryinapp-api.md)组件，配置需拉起的bundleName与UIAbility（仅限本应用，无法拉起其他应用），单击组件页面进入分屏（双股对比），在分屏状态下，再点击组件进入全景多窗（三股对比）。

下表以Mate X5设备为例，展示应用在分屏及全景多窗模式下的效果。

| - | 折叠屏分屏-双股**比价** | 折叠屏全景多窗-三股**比价** |
| --- | --- | --- |
| 个股详情页-多股比价 |  |  |

**约束条件**

[MultiWindowEntryInAPP](../harmonyos-references/ui-design-multiwindowentryinapp-api.md)组件依赖全景多窗特性，只有当前设备及屏幕状态支持全景多窗，才支持设置此功能。目前支持全景多窗的设备型态有：

* 双折叠：展开态。
* 三折叠：双屏态，三屏态的横屏态。
* 平板：横屏态。

对于不支持的设备型态，该组件不可交互，不响应点击事件。

**说明** 

建议开发者在分屏副窗口左上角设置**关闭按钮**以直接关闭副窗口，本案例使用返回按钮，是股票比价场景需返回上级页面的特定需求。

**开发步骤**

应用使用[MultiWindowEntryInAPP](../harmonyos-references/ui-design-multiwindowentryinapp-api.md)组件主动分屏或进入全景多窗。具体开发步骤如下：

1. 导入模块。

   ```typescript
   import { MultiWindowEntryInAPP } from '@kit.UIDesignKit';
   import { TextModifier } from '@kit.ArkUI';
   import { Want } from '@kit.AbilityKit';
   ```
2. 使用MultiWindowEntryInAPP组件，并且设置组件参数。

   ```typescript
   @Component
   export struct MultiWindowEntryComponent {
     @Link textModifier: TextModifier;
     @Link want: Want;
     @State isShowMultiWindowEntry: boolean = false;
     // ...

     build() {
       Row() {
         MultiWindowEntryInAPP({
           want: this.want,
           isShowSubtitle: false,
           multiWindowEntryInAPPStyle: {
             iconOptions: {
               iconSize: 24,
               iconColor: $r('sys.color.font_primary'),
               iconWeight: FontWeight.Normal,
               backgroundColor: $r('sys.color.comp_background_tertiary')
             },
             subtitleOptions: {
               modifier: this.textModifier.fontColor($r('app.color.text_primary_color'))
             }
           }
         })
           .id('MultiWindowEntryInAPP')
       }
       .visibility(this.isShowMultiWindowEntry ? Visibility.Visible : Visibility.None)
     }
   }
   ```
3. 导入封装好的MultiWindowEntryComponent组件，并且设置组件参数。

   ```typescript
   import { MultiWindowEntryComponent } from './MultiWindowEntryComponent';

   @Component
   export struct TopTitleBar {
     // ...
     @State textModifier: TextModifier = new TextModifier();
     @State splitScreenWant: Want = {
       // Modify the bundleName, moduleName and abilityName of the current application,
       // and launch the UIAbility within the application.
       bundleName: 'com.example.multiticketclass',
       moduleName: 'multiticketclassdefaultsample',
       abilityName: 'SplitScreenAbility',
     };
     // ...
     build() {
       Row() {
         // ...
         // The area displayed by the icon on the right side
         Row({ space: 16 }) {
           // split screen
           Row() {
             MultiWindowEntryComponent({
               textModifier: this.textModifier,
               want: this.splitScreenWant
             })
           }
           .visibility(this.getMultiWindowVisibility())
         }
       }
       // ...
     }
   }
   ```

**应用内分屏高阶组件窗口路由方案**

建议开发者采用应用级多实例来实现分屏页面的路由管理。以下是页面级多实例与应用级多实例的主要区别，多股比价场景的分屏路由管理采用应用级多实例：

| 场景 | 路由栈特点 | 是否需要路由改造 | 核心方案 |
| --- | --- | --- | --- |
| 页面级多实例 | 每个UI Ability创建后，基于当前节点改造路由栈 | 需要 | 以当前路由节点生成路由表，开发者手动定义路由方案 |
| 应用级多实例（**推荐**） | 每个UI Ability创建独立的相同路由栈 | 不需要 | 每个窗口启动时创建独立路由栈（路由表相同） |

**应用内分屏高阶组件窗口路由退栈方案**

在多股比价场景中，当在应用内进行分屏操作时，新增窗口应保留当前浏览的股票信息，而主窗口则应回到股票列表。为实现这一功能，建议在新窗口的启动生命周期中触发事件，原窗口通过监听该事件并执行退栈操作。

1. 在分屏程序的入口SplitScreenAbility.ets中的onCreate()和onNewWant()生命周期中进行事件触发。

   ```typescript
   let eventData: emitter.EventData = {
     data: {
       'isStart': 1,
       'id': 1
     }
   };
   let innerEvent: emitter.InnerEvent = {
     eventId: 1,
     priority: emitter.EventPriority.HIGH
   };

   export default class SplitScreenAbility extends UIAbility {
     // ...

     onCreate(): void {
       // ...
       emitter.emit(innerEvent, eventData);
     }

     onNewWant(): void {
       // ...
       emitter.emit(innerEvent, eventData);
     }

     // ...
   }
   ```
2. 在原窗口进行事件监听并做退栈处理。

   ```typescript
   @Component
   export struct TopTitleBar {
     // ...
     private innerEvent: emitter.InnerEvent = { eventId: 1 };
     private callBack: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
       Logger.info(`eventData:${eventData}`);
       if (this.pageInfos?.pop) {
         this.pageInfos.pop();
       }
     };

     aboutToAppear(): void {
       this.viewModel.loadData();
       if (this.context.abilityInfo.name === 'MultiticketclassdefaultAbility') {
         emitter.on(this.innerEvent, this.callBack);
       }
     }

     aboutToDisappear(): void {
       emitter.off(this.innerEvent.eventId, this.callBack);
     }

     // ...
     }
   }
   ```

**应用内分屏高阶组件按钮显隐策略**

在应用内分屏高阶组件时，对不支持全景多窗的设备隐藏分屏按钮。方案的主要逻辑为：

1. 监听窗口尺寸变化。

   ```typescript
   public onWindowSizeChange: (windowSize: window.Size) => void = (windowSize: window.Size) => {
     this.mainWindowInfo.windowSize = windowSize;
     if (this.uiContext) {
       this.mainWindowInfo.widthBp = this.uiContext.getWindowWidthBreakpoint();
       this.mainWindowInfo.heightBp = this.uiContext.getWindowHeightBreakpoint();
     }
   };
   // ...
   updateWindowInfo(): void {
     try {
       // ...
       // Register for window size change monitoring, update window size and width/height breakpoint.
       this.mainWindow.on('windowSizeChange', this.onWindowSizeChange);
       // ...
       AppStorage.setOrCreate(KEY_MAIN_WINDOW_INFO, this.mainWindowInfo);
     } catch (error) {
       let err = error as BusinessError;
       Logger.error(`Failed to update window info. Code: ${err.code}, message: ${err.message}`);
     }
   }
   ```
2. 尺寸变化时获取按钮节点，查询其enabled属性。

   ```typescript
   private timerId: number = -1;

   aboutToAppear(): void {
     this.checkMultiWindowEnabled();
   }

   aboutToDisappear(): void {
     if (this.timerId !== -1) {
       clearTimeout(this.timerId);
     }
   }

   private checkMultiWindowEnabled(): void {
     this.timerId = setTimeout(() => {
       const frameNode = this.getUIContext()?.getFrameNodeById('MultiWindowEntryInAPP');
       const inspectorInfo = JSON.stringify(frameNode?.getInspectorInfo() as InspectorInfo);
       if (inspectorInfo?.search('"enabled":true') && inspectorInfo?.search('"enabled":true') !== -1) {
         this.isShowMultiWindowEntry = true;
       } else {
         this.isShowMultiWindowEntry = false;
       }
     }) as number;
   }
   ```
3. 根据enabled属性通过visibility控制组件的显隐。

   ```typescript
   Row() {
     MultiWindowEntryInAPP({
       want: this.want,
       isShowSubtitle: false,
       multiWindowEntryInAPPStyle: {
         // ...
       }
     })
       .id('MultiWindowEntryInAPP')
   }
   .visibility(this.isShowMultiWindowEntry ? Visibility.Visible : Visibility.None)
   ```

## 电脑端页面

本章介绍如何基于现有移动端界面开发方案，实现代码逻辑与布局复用，高效完成股票类应用在电脑设备上的界面开发。

### 窗口适配

* 窗口模式

  长视频应用在电脑端上支持全屏和自由窗口两种模式，具体实现可参考[窗口模式](bpta-multi-device-window-mode.md)。应用内监听窗口尺寸变化，[通过断点刷新UI](bpta-multi-device-responsive-layout.md#section175001836203617)，即可自动适配全屏和自由窗口模式下的布局。
* 窗口沉浸式

  根据UX设计规范，需要实现全屏和自由窗口下的沉浸式效果，具体实现可参考[窗口沉浸式](bpta-multi-device-window-immersive.md)。全屏模式下，通过[window.setWindowLayoutFullscreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)实现沉浸式。自由窗口模式下，通过[window.setWindowDecorVisible(false)](../harmonyos-references/arkts-apis-window-window.md#setwindowdecorvisible11)隐藏标题栏，仅保留右上角三键，使页面内容延伸至标题栏区域，实现沉浸式显示效果。

### 自选股页面

**页面布局**

* 将电脑端自选股页划分为四个部分，效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/L0Uoz_afQjujimdA-kobjQ/zh-cn_image_0000002610071557.png "点击放大")

* 对各个区域使用的多种能力进行分析，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 侧边页签 | 同移动端[自选股页面](multi-ticket-class.md#section2034582411817)对应区域的布局实现方案一致。 |
  | 2 | 指数 |
  | 3 | 股票列表-工具栏 |
  | 4 | 股票列表 |

### 股票详情页

**页面布局**

* 将电脑端股票详情页划分为五个部分，效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/JhyBARp0QYOYNhjV6FYNag/zh-cn_image_0000002579631780.png "点击放大")

* 对各区域使用的能力进行分析，实现方案如表所示：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 交易操作行 | 同移动端[股票详情页](multi-ticket-class.md#section46312514204)对应区域的布局实现方案一致。 |
  | 2 | 标题 |
  | 3 | 行情列表数据 |
  | 4 | 中间Tab |
  | 5 | 曲线图和柱状图 |

## 示例代码

* [多设备股票类界面](https://gitcode.com/harmonyos_samples/multi-ticket-class)
