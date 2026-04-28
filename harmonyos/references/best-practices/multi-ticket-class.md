---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/multi-ticket-class
title: 多设备股票类界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备股票类界面
category: best-practices
scraped_at: 2026-04-28T08:21:13+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:105d79e46393d9e90ee4d58c7f821c5185b2bfa161640232dff4aa243ac5e3e6
---

## 概述

本文以目前流行的垂类市场中的股票类应用作为典型案例，详细介绍“一多”在实际开发中的应用，主要涵盖自选股和个股详情两个典型页面，展示其在直板机、双折叠、三折叠、阔折叠、平板五种产品形态上的“一次开发，多端部署”。下文将从[UX设计](multi-ticket-class.md#section18423159193410)、[工程管理](multi-ticket-class.md#section251720249266)、[窗口适配](multi-ticket-class.md#section824510452191)、[界面开发](multi-ticket-class.md#section1350915119215)四个角度，介绍“一多”股票类应用在开发过程中的最佳实践。

说明

阅读本文前，开发者需熟悉[ArkUI（方舟UI框架）](../harmonyos-guides/arkui.md)和页面开发的“一多”能力（参考[一次开发，多端部署概览](bpta-multi-device-overview.md)）。下文将详细介绍它们在“一多”开发实践中如何使用。

## UX设计

股票类应用的目的是让用户更加便捷地办理金融业务。常见的有银行理财、股票、基金等类型的应用和业务场景，核心场景有数据查看、股票交易等。

股票类应用有以下特点：

* 丰富的信息聚合。
* 图表数据高效展示。
* 便捷高效的交互方式。

此类型的应用在多端设备的使用过程中，不仅要保障用户在办理金融业务的过程中正常使用，还要尽可能提升大屏幕的交互效率。

以下是股票界面在直板机、阔折叠、双折叠设备及平板上的UX设计图。

说明

由于三折叠与平板的横向断点均为lg，在lg断点下仅展示平板的效果图。

**自选股页面**

页面主要包含：页面底部/侧边页签、标题、股票指数、股票列表-工具栏、股票列表。

| 横向(/纵向)断点 | sm/md | sm/lg | md | lg |
| --- | --- | --- | --- | --- |
| 自选股页面 |  |  |  |  |

**个股详情页**

页面主要包含：顶部标题、行情列表数据、分时Tab、曲线图和柱状图以及股票实时交易列表、讨论Tab、底部交易操作行。

| 横向(/纵向)断点 | sm/md | sm/lg | md | lg |
| --- | --- | --- | --- | --- |
| 个股详情页 |  |  |  |  |

**半模态-股票交易弹窗**

| 横向(/纵向)断点 | sm/md | sm/lg | md | lg |
| --- | --- | --- | --- | --- |
| 半模态-股票买入弹窗 |  |  |  |  |
| 半模态-确认买入股票弹窗 |  |  |  |  |

### 断点设计

股票类应用通常用于直板机、双折叠、三折叠、阔折叠和平板设备。以下为这些常用设备和屏幕尺寸（横向/纵向断点）的股票类应用适配策略：

1. 阔折叠外屏（sm/md）、直板机（sm/lg）

   基础视图。
2. 双折叠展开态、阔折叠横向展开（md）

   推荐做法：

   * 相较于直板机，双折叠在展开状态下，开发者可利用更大的屏幕空间扩展股票图表显示内容，以增强应用的沉浸感和信息显示，例如股票详情、股票K线图。
3. 平板、三折叠展开态（lg）

   推荐做法：
   * 相较于直板机，平板设备在横向模式下能够显示更多内容。默认为双栏显示，左侧栏主要用于显示股票列表，右侧栏则展示股票详情信息，例如股票K线图。当点击全屏按钮时，页面切换至单栏显示，页面主要展示股票详情信息，此时股票K线图会占据更大比例，显示内容更加丰富。

不同设备对应的断点区间，请参考[一多断点](bpta-multi-device-responsive-layout.md#section1532120147301)。

### 设计指南

金融理财类的多设备响应式设计指南，请参考[金融理财类](../design-guides/responsive-design-examples6-0000001793536905.md)。

## 工程管理

### 工程结构

在创建“一多”工程时，开发者会面临工程结构目录的划分问题。考虑到复用性和可维护性，本文以股票类应用为例，提供推荐的参考方案。

HarmonyOS的分层架构包括产品定制层、基础特性层和公共能力层，为开发者提供清晰、高效、可扩展的设计架构。详细请参见[分层架构设计](bpta-layered-architecture-design.md)。

股票类应用根据一多推荐的commons、features、products的“三层工程架构”划分目录。其中四个页面功能不同，互不依赖，根据页面划分为两个features（基础特性层）：首页-home、股票详情页-stockdetail。公共常量、媒体播放工具以及窗口管理工具等需要被不同页面依赖引用的内容，划分为一个commons（公共能力层）：基础能力-base。products（产品定制层）定制了程序标准启动流程和多场景协同场景的入口能力。

工程结构如下：

```
1. ├──commons
2. │  └──base/src/main/ets
3. │     ├──constants                        // 公共常量
4. │     └──utils                            // 公共工具
5. ├──features
6. │  ├──home/src/main
7. │  │  ├──ets
8. │  │  │  ├──models                        // 股票类数据
9. │  │  │  ├──pages                         // 应用首页内容
10. │  │  │  └──views                         // 首页视图组件
11. │  │  └──resources                        // 应用静态资源目录
12. │  └──stockdetail/src/main
13. │     ├──ets
14. │     │  ├──chartmodels                   // 图标组件
15. │     │  ├──models                        // 股票类数据
16. │     │  ├──pages                         // 股票详情页
17. │     │  └──views                         // 股票视图组件
18. │     └──resources                        // 应用静态资源目录
19. └──products
20. ├──phone/src/main/ets
21. │  ├──entryability                     // 程序入口
22. │  ├──entrybackupability
23. │  ├──pages                            // 首页
24. │  ├──splitScreenAbility               // 分屏入口
25. │  └──splitScreenBackupAbility
26. └──phone/src/main/resources            // 应用静态资源目录
```

## 窗口适配

### 窗口模式

[多设备股票类界面](https://gitcode.com/harmonyos_samples/multi-ticket-class)示例，根据适配的设备，涉及全屏模式、分屏模式、悬浮窗模式、自由窗口模式，可参考[窗口模式](bpta-multi-device-window-mode.md)。其中分屏模式与悬浮窗通常无特殊设计，可通过系统方式进入。应用监听窗口尺寸变化，[通过断点刷新UI](bpta-multi-device-responsive-layout.md#section175001836203617)，将自动适配全屏、分屏、悬浮窗、自由窗口模式下的布局。

使用系统UI组件进入全景多窗，实现一个应用多个窗口并行运行的体验，可参考[功能开发：应用多实例-多股比价](multi-ticket-class.md#section12800182173311)。

### 窗口方向

通过设置[window.setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)使应用跟随传感器自动旋转，可旋转至竖屏、横屏、反向竖屏、反向横屏四个方向。本示例使用[跟随桌面的旋转模式](../harmonyos-guides/window-rotation.md#其他方向类型)。

### 窗口沉浸式

根据UX设计，实现不同窗口模式（全屏、分屏、悬浮窗）下窗口的沉浸式，可参考[窗口沉浸式](bpta-multi-device-window-immersive.md)。全屏、分屏和悬浮窗的沉浸式均可通过[setWindowLayoutFullscreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)实现，并进行动态安全区避让。

## 界面开发

## 自选股页面

### 页面布局

* 将自选股页划分为四个部分，效果图如下：

  | 横向(/纵向)断点 | sm/md | sm/lg | md | lg |
  | --- | --- | --- | --- | --- |
  | 自选股页 |  |  |  |  |
* 对各个区域使用的多种能力进行分析，实现方案如下表：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 底部/侧边页签 | 借助[响应式组件](bpta-multi-device-responsive-layout.md#section1914110349546)Tabs实现。 |
  | 2 | 指数 | 最后一个组件固定，其他组件使用[List组件](../harmonyos-references/ts-container-list.md)实现延伸能力，随着设备宽度变大，页签间距变大，页面能够展示更多页签内容。 |
  | 3 | 股票列表-工具栏 | 文字和功能按钮中间增加[Blank组件](../harmonyos-references/ts-basic-components-blank.md)，实现拉伸能力。 |
  | 4 | 股票列表 | 通过使用[List组件](../harmonyos-references/ts-container-list.md)设置固定宽度和[Scroll组件](../harmonyos-references/ts-container-scroll.md)，可实现股票列表数据的上下或左右滑动。同时，支持对不同列设置不同的[justifyContent](../harmonyos-references/ts-container-column.md#justifycontent8)，以便实现各列的不同对齐方式。 |

* 整个页面使用的是[分栏布局](bpta-multi-device-page-layout.md#section631723412132)，在股票列表区域，点击某一股票时，平板上会分栏显示该股票的详细信息。

### 交互开发

页签切换、自选股查看和跳转等交互均为简单的点击事件，开发过程可参考[多设备交互](bpta-multi-interaction.md)。

## 股票详情页

### 页面布局

* 将个股详情页划分为六个部分，效果图如下：

  | 横向(/纵向)断点 | sm/md | sm/lg | md | lg |
  | --- | --- | --- | --- | --- |
  | 个股详情页 |  |  |  |  |
* 对各区域使用的能力进行分析，实现方案如表所示：

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 交易操作行 | 通过为“去交易”按钮设置[layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)布局权重，并使用Blank组件结合断点，实现该按钮的自适应拉伸。 |
  | 2 | 标题 | 居中显示，其他操作两端对齐，空白空间使用[Blank组件](../harmonyos-references/ts-basic-components-blank.md)实现自适应布局拉伸能力。 |
  | 3 | 行情列表数据 | 通过[栅格布局](bpta-multi-device-responsive-layout.md#section1061332817545)并结合断点，控制在不同断点下显示不同的列数，列表自适应两列变多列。 |
  | 4 | 中间Tab | 通过[List组件](../harmonyos-references/ts-container-list.md)的space属性并结合断点，控制在不同断点下ListItem之间的间距。 |
  | 5 | 曲线图和柱状图 | 使用layoutWeight属性实现拉伸能力。 |
  | 6 | 讨论的Tab | 通过[List组件](../harmonyos-references/ts-container-list.md)的space属性并结合断点，控制在不同断点下ListItem之间的间距。 |

### 交互开发

图表切换、股票交易等交互均为简单的点击事件，开发过程可参考[多设备交互](bpta-multi-interaction.md)。

### 功能开发：应用多实例-多股比价

应用通过系统提供的[MultiWindowEntryInAPP](../harmonyos-references/ui-design-multiwindowentryinapp-api.md)组件，配置需拉起的bundleName与UIAbility（仅限本应用，无法拉起其他应用），单击组件页面进入分屏（双股对比），在分屏状态下，在点击组件进入全景多窗（三股对比）。

下表以Mate X5设备为例，展示应用在分屏及全景多窗模式下的效果。

|  | 折叠屏分屏-双股**比价** | 折叠屏全景多窗-三股**比价** |
| --- | --- | --- |
| 个股详情页-多股比价 |  |  |

**约束条件**

[MultiWindowEntryInAPP](../harmonyos-references/ui-design-multiwindowentryinapp-api.md)组件依赖全景多窗特性，只有当前设备及屏幕状态支持全景多窗，才支持设置此功能。目前支持全景多窗的设备型态有：

* 双折叠：展开态。
* 三折叠：双屏态，三屏态的横屏态。
* 平板：横屏态。

对于不支持的设备型态，该组件不可交互，不响应点击事件。

说明

建议开发者在分屏副窗口左上角设置**关闭按钮**以直接关闭副窗口，本案例使用返回按钮，是股票比价场景需返回上级页面的特定需求。

**开发步骤**

应用使用[MultiWindowEntryInAPP](../harmonyos-references/ui-design-multiwindowentryinapp-api.md)组件主动分屏或进入全景多窗。具体开发步骤如下：

1. 导入模块。

   ```
   1. import { MultiWindowEntryInAPP, MultiWindowEntryInAPPAttribute} from '@kit.UIDesignKit';
   2. import { TextModifier } from '@kit.ArkUI';
   3. import { Want } from '@kit.AbilityKit';
   ```

   [MultiWindowEntryComponent.ets](https://gitcode.com/HarmonyOS_Samples/multi-ticket-class/blob/master/features/stockdetail/src/main/ets/views/MultiWindowEntryComponent.ets#L16-L18)
2. 使用MultiWindowEntryInAPP组件，并且设置组件参数。

   ```
   1. @Component
   2. export struct MultiWindowEntryComponent {
   3. @Link textModifier: TextModifier;
   4. @Link want: Want;
   5. @State isShowMultiWindowEntry: boolean = false;
   6. // ...

   8. build() {
   9. Row() {
   10. MultiWindowEntryInAPP({
   11. want: this.want,
   12. isShowSubtitle: false,
   13. multiWindowEntryInAPPStyle: {
   14. iconOptions: {
   15. iconSize: 24,
   16. iconColor: $r('sys.color.font_primary'),
   17. iconWeight: FontWeight.Normal,
   18. backgroundColor: $r('sys.color.comp_background_tertiary')
   19. },
   20. subtitleOptions: {
   21. modifier: this.textModifier.fontColor(Color.Black)
   22. }
   23. }
   24. })
   25. .id("MultiWindowEntryInAPP")
   26. }
   27. .visibility(this.isShowMultiWindowEntry ? Visibility.Visible : Visibility.None)
   28. }
   29. }
   ```

   [MultiWindowEntryComponent.ets](https://gitcode.com/HarmonyOS_Samples/multi-ticket-class/blob/master/features/stockdetail/src/main/ets/views/MultiWindowEntryComponent.ets#L23-L75)
3. 导入封装好的MultiWindowEntryComponent组件，并且设置组件参数。

   ```
   1. import { MultiWindowEntryComponent } from './MultiWindowEntryComponent';
   2. @Component
   3. export struct TopTitleBar {
   4. // ...
   5. @State textModifier: TextModifier = new TextModifier();
   6. @State splitScreenWant: Want = {
   7. // Modify the bundleName, moduleName and abilityName of the current application, and launch the UIAbility within the application.
   8. bundleName: 'com.example.multiticketclass',
   9. moduleName: 'phone',
   10. abilityName: 'SplitScreenAbility',
   11. };
   12. // ...
   13. build() {
   14. Row() {
   15. // ...
   16. // The area displayed by the icon on the right side
   17. Row({ space: 16 }) {
   18. // split screen
   19. Row() {
   20. MultiWindowEntryComponent({
   21. textModifier: this.textModifier,
   22. want: this.splitScreenWant
   23. })
   24. }
   25. // ...
   26. }
   27. }
   28. // ...
   29. }
   30. }
   ```

   [TopTitleBar.ets](https://gitcode.com/harmonyos_samples/multi-ticket-class/blob/master/features/stockdetail/src/main/ets/views/TopTitleBar.ets#L25-L157)

**应用内分屏高阶组件窗口路由方案**

建议开发者采用应用级多实例来实现分屏页面的路由管理。以下是页面级多实例与应用级多实例的主要区别，多股比价场景的分屏路由管理采用应用级多实例：

| 场景 | 路由栈特点 | 是否需要路由改造 | 核心方案 |
| --- | --- | --- | --- |
| 页面级多实例 | 每个UI Ability创建后，基于当前节点改造路由栈 | 需要 | 以当前路由节点生成路由表，开发者手动定义路由方案 |
| 应用级多实例（**推荐**） | 每个UI Ability创建独立的相同路由栈 | 不需要 | 每个窗口启动时创建独立路由栈（路由表相同） |

**应用内分屏高阶组件窗口路由退栈方案**

在多股比价场景中，当在应用内进行分屏操作时，新增窗口应保留当前浏览的股票信息，而主窗口则应回到股票列表。为实现这一功能，建议在新窗口的启动生命周期中触发事件，原窗口通过监听该事件并执行退栈操作。

1. 在分屏程序的入口SplitScreenAbility.ets中的onCreate()和onNewWant()生命周期中进行事件触发。

   ```
   1. let eventData: emitter.EventData = {
   2. data: {
   3. 'isStart': 1,
   4. 'id': 1
   5. }
   6. };
   7. let innerEvent: emitter.InnerEvent = {
   8. eventId: 1,
   9. priority: emitter.EventPriority.HIGH
   10. };

   12. export default class SplitScreenAbility extends UIAbility {
   13. // ...

   15. onCreate(): void {
   16. // ...
   17. emitter.emit(innerEvent, eventData);
   18. }

   20. onNewWant(): void {
   21. // ...
   22. emitter.emit(innerEvent, eventData);
   23. }
   24. // ...
   25. }
   ```

   [SplitScreenAbility.ets](https://gitcode.com/harmonyos_samples/multi-ticket-class/blob/master/products/phone/src/main/ets/splitScreenAbility/SplitScreenAbility.ets#L24-L145)
2. 在原窗口进行事件监听并做退栈处理。

   ```
   1. @Component
   2. export struct TopTitleBar {
   3. // ...
   4. private innerEvent: emitter.InnerEvent = { eventId: 1 };
   5. private callBack: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
   6. Logger.info(`eventData:${eventData}`);
   7. if (this.pageInfos?.pop) {
   8. this.pageInfos.pop();
   9. }
   10. };
   11. aboutToAppear(): void {
   12. if (this.context.abilityInfo.name === 'EntryAbility') {
   13. emitter.on(this.innerEvent, this.callBack);
   14. }
   15. }
   16. dispose(): void {
   17. emitter.off(this.innerEvent.eventId, this.callBack);
   18. }
   19. // ...
   20. }
   21. }
   ```

   [TopTitleBar.ets](https://gitcode.com/harmonyos_samples/multi-ticket-class/blob/master/features/stockdetail/src/main/ets/views/TopTitleBar.ets#L27-L156)

**应用内分屏高阶组件按钮显隐策略**

在应用内分屏高阶组件时，对不支持全景多窗的设备隐藏分屏按钮。方案的主要逻辑为：

1. 监听窗口尺寸变化。

   ```
   1. public onWindowSizeChange: (windowSize: window.Size) => void = (windowSize: window.Size) => {
   2. this.mainWindowInfo.windowSize = windowSize;
   3. this.mainWindowInfo.widthBp = this.uiContext!.getWindowWidthBreakpoint();
   4. this.mainWindowInfo.heightBp = this.uiContext!.getWindowHeightBreakpoint();
   5. };
   6. // ...
   7. updateWindowInfo(): void {
   8. try {
   9. // ...
   10. // Register for window size change monitoring, update window size and width/height breakpoint.
   11. this.mainWindow.on('windowSizeChange', this.onWindowSizeChange);
   12. // ...
   13. AppStorage.setOrCreate('mainWindowInfo', this.mainWindowInfo);
   14. } catch (error) {
   15. let err = error as BusinessError;
   16. hilog.error(0x0000, `TestLog`, `Failed to update window info. Code: ${err.code}, message: ${err.message}`);
   17. }
   18. }
   ```

   [WindowUtil.ets](https://gitcode.com/harmonyos_samples/multi-ticket-class/blob/master/commons/base/src/main/ets/utils/WindowUtil.ets#L39-L240)
2. 尺寸变化时获取按钮节点，查询其enabled属性。

   ```
   1. @StorageLink('mainWindowInfo') @Watch('watchWindow') mainWindowInfo: WindowInfo = new WindowInfo();
   2. aboutToAppear(): void {
   3. this.watchWindow();
   4. }

   6. private watchWindow(): void {
   7. setTimeout(()=> {
   8. let nodeStr = JSON.stringify(this.getUIContext()?.getFrameNodeById("MultiWindowEntryInAPP")?.getInspectorInfo());
   9. if (nodeStr?.search('"enabled":true') && nodeStr?.search('"enabled":true') !== -1) {
   10. this.isShowMultiWindowEntry = true;
   11. } else {
   12. this.isShowMultiWindowEntry = false;
   13. }
   14. })
   15. }
   ```

   [MultiWindowEntryComponent.ets](https://gitcode.com/harmonyos_samples/multi-ticket-class/blob/master/features/stockdetail/src/main/ets/views/MultiWindowEntryComponent.ets#L30-L44)
3. 根据enabled属性通过visibility控制组件的显隐。

   ```
   1. Row() {
   2. MultiWindowEntryInAPP({
   3. want: this.want,
   4. isShowSubtitle: false,
   5. multiWindowEntryInAPPStyle: {
   6. // ...
   7. }
   8. })
   9. .id("MultiWindowEntryInAPP")
   10. }
   11. .visibility(this.isShowMultiWindowEntry ? Visibility.Visible : Visibility.None)
   ```

   [MultiWindowEntryComponent.ets](https://gitcode.com/harmonyos_samples/multi-ticket-class/blob/master/features/stockdetail/src/main/ets/views/MultiWindowEntryComponent.ets#L51-L72)

## 示例代码

* [多设备股票类界面](https://gitcode.com/harmonyos_samples/multi-ticket-class)
