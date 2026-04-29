---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-responsive-layout
title: 响应式布局
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 界面布局响应式变化 > 响应式布局
category: best-practices
scraped_at: 2026-04-29T14:11:55+08:00
doc_updated_at: 2026-04-07
content_hash: sha256:ded7fcfc5d00f45633264712b4ae04e2409dc316a18756823b2c624b590909a9
---

## 概述

响应式设计（Responsive Web Design，简称RWD）在Web网站设计领域是一种网页设计方法论，旨在让网站在不同设备和屏幕尺寸上都能提供良好的阅读和交互体验，而无需为每一个新设备或屏幕尺寸创建单独的版本。这种设计方法的核心在于页面布局和内容可以根据用户所使用的设备特性（如屏幕尺寸、分辨率、方向等）进行灵活调整。

响应式设计在HarmonyOS中的应用主要体现在UI开发上，目的是确保应用能够在搭载HarmonyOS的多种设备上，包括不同屏幕尺寸和分辨率的设备，提供一致且优秀的用户体验。HarmonyOS为此提供了一系列的响应式布局能力和工具，用来实现多端布局。

响应式布局是基于响应式设计方法论进行布局的方法，核心思想是页面根据不同屏幕尺寸自动调整布局，提供更舒适的界面和更好的用户体验。响应式布局页面的效果图如下：

**图1** 响应式布局示意图1  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/LGSQIbx9QpiIDFyzcNqG-w/zh-cn_image_0000002355146009.png?HW-CC-KV=V1&HW-CC-Date=20260429T061153Z&HW-CC-Expire=86400&HW-CC-Sign=7F5FA312EB79CB2E20916726060CA8DB2B56783C0A0AC98E2EFCEFBACB2C4E48 "点击放大")

**图2** 响应式布局示意图2  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/MzJbKbdCSH-TJuRA0znzLw/zh-cn_image_0000002321147306.png?HW-CC-KV=V1&HW-CC-Date=20260429T061153Z&HW-CC-Expire=86400&HW-CC-Sign=4C6BD1A001D49BBA8FD7E3710EC1BA2456B07D71B5BE0463442EF0257F350E98 "点击放大")

本文将详细介绍实现响应式布局的四种响应式布局能力，帮助开发者实现响应式布局效果。

| 响应式布局能力 | 简介 |
| --- | --- |
| [断点](bpta-multi-device-responsive-layout.md#section1532120147301) | 将窗口宽度划分为不同的范围（即断点），监听窗口尺寸变化，当断点改变时同步调整页面布局。 |
| [媒体查询](bpta-multi-device-responsive-layout.md#section1950102518311) | 媒体查询支持监听窗口宽度、横竖屏、深浅色、设备类型等多种媒体特征，当媒体特征发生改变时同步调整页面布局。 |
| [栅格](bpta-multi-device-responsive-layout.md#section1061332817545) | 栅格组件将其所在的区域划分为有规律的多列，通过调整不同断点下的栅格组件的参数以及其子组件占据的列数等，实现不同的布局效果。 |
| [响应式组件](bpta-multi-device-responsive-layout.md#section1914110349546) | HarmonyOS提供的一些组件支持响应式布局，例如： Tabs、Swiper、Grid、List、GridRow，通过断点设置可以实现不同的展示效果。 |

## 断点

响应式布局是指页面内的元素可以根据特定的特征（如窗口宽度、屏幕方向等）自动变化以适应外部容器变化的布局能力。响应式布局中最常使用的特征是窗口宽度及窗口高宽比，可以将窗口宽度及窗口高宽比划分为不同的范围，称之为“断点”。当窗口宽度及窗口高宽比从一个断点变化到另一个断点时，改变页面布局（如将页面内容从单列排布调整为双列排布甚至三列排布等）以获得更好的显示效果。

本章节将通过详细介绍断点的设计原理、定义以及使用，帮助开发者掌握通过断点实现响应式布局。

### 断点的设计原理

提升全场景体验，需考虑多设备连续性。应用页面布局设计时推荐遵循以下原则：

* 原则一：两个宽度相近的窗口，页面布局相同，断点归一。
* 原则二：高度相对宽度较小的窗口，呈现横向窗口或类方形窗口时，页面布局进行差异化设计，增加断点。

因此，系统设计了横向和纵向断点分别代表窗口的不同特征，作为判断页面布局和交互体验的条件：

* 横向断点以窗口宽度值区分，代表窗口宽度。
* 纵向断点以窗口高宽比区分，代表窗口相对高度，表示横向、方形或纵向窗口。

下文[横向断点的使用案例](bpta-multi-device-responsive-layout.md#section565041813314)章节将介绍如何使用横向断点实现原则一，[纵向断点的使用案例](bpta-multi-device-responsive-layout.md#section8955133118444)章节将介绍如何结合横向和纵向断点实现原则二。

### 断点的定义

横向断点以应用窗口宽度为判断条件，建议划分为如下几个区间：

| 断点名称 | 窗口宽度（vp） |
| --- | --- |
| xs | (0, 320） |
| sm | [320, 600) |
| md | [600, 840) |
| lg | [840, 1440) |
| xl | [1440, +∞) |

纵向断点根据应用窗口的高宽比进行判断，建议划分为如下几个区间：

| 断点名称 | 高宽比 |
| --- | --- |
| sm | (0, 0.8) |
| md | [0.8, 1.2) |
| lg | [1.2, +∞) |

下图为HarmonyOS常用设备断点区间表：

**图3** HarmonyOS常用设备断点区间表

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/5KeJBRs5SACnEEtSmVykfw/zh-cn_image_0000002321553558.png?HW-CC-KV=V1&HW-CC-Date=20260429T061153Z&HW-CC-Expire=86400&HW-CC-Sign=38725654BC69B300668BAA2311126E6B47305AEEB10F8ED25320E43151207DBE "点击放大")

说明

1. 断点面向窗口而非设备类型，相同断点区间的窗口展示相同的页面布局。同一设备上的不同窗口形态（例如全屏显示、分屏显示、自由窗口等）可能落入不同的断点区间，展示不同布局。
2. 部分手机、小折叠屏机型横屏/反向横屏时横向断点会落入lg，包括Pura70 Pro和Pocket2。
3. 开发者可以根据实际使用场景决定适配哪些断点。如xs断点对应的一般是智能穿戴类设备，如果确定某页面不会在智能穿戴设备上显示，则可以不适配xs断点。
4. 可以根据实际业务场景需要在lg断点后面新增xl、xxl等断点。

当前HarmonyOS主流设备窗口全屏时尺寸和横纵断点区间如下表所示。

| 产品类型 | 常见产品型号 | 窗口全屏时尺寸（以产品型号第一款举例，单位为vp） | 横向断点 | 纵向断点 |
| --- | --- | --- | --- | --- |
| 手机（竖屏/反向竖屏） | Mate60、Mate60 Pro、Mate70、Mate70 Pro、Pura60、Pura60 Pro、Pura70、Pura70 Pro | 827 \* 374 | sm | lg |
| 阔折叠 | Pura X | 内屏（竖屏/反向竖屏）：707 \* 440 | 内屏：sm | 内屏：lg |
| 外屏（反向横屏）：326 \* 326 | 外屏：sm | 外屏：md |
| 小折叠 | Pocket 2 | 内屏（竖屏/反向竖屏）：860 \* 364 | 内屏：sm | 内屏：lg |
| 外屏：/ | 外屏：/ | 外屏：/ |
| 双折叠 | Mate X5、Mate X6 | 内屏（竖屏/反向竖屏）：798 \* 711 | 内屏：md | 内屏：md |
| 外屏（竖屏/反向竖屏）：801 \* 345 | 外屏：sm | 外屏：lg |
| 三折叠 | Mate XT | F态（单屏显示，竖屏/反向竖屏）：776 \* 350 | F态（单屏显示）：sm | F态（单屏显示）：lg |
| M态（双屏显示，竖屏/反向竖屏）：776 \* 712 | M态（双屏显示）：md | M态（双屏显示）：md |
| G态（三屏显示，横屏/反向横屏）：1107 \* 776 | G态（三屏显示）：lg | G态（三屏显示）：sm |
| 平板（横屏/反向横屏） | MatePad、MatePad Pro | 1137 \* 711 | lg | sm |
| 电脑 | MateBook Pro（横屏） | 1642 \* 1094 | xl | sm |
| MateBook Fold（展开态横屏） | 1831 \* 1307 | xl | sm |
| 智慧屏 | Mate TV | 1280 \* 720 | lg | sm |

### 通过断点刷新UI

**通过断点环境变量****刷新UI**

从API version 22起，开发者可利用响应式系统环境变量装饰器@Env读取断点信息。当组件所在窗口尺寸发生变化时，@Env装饰的断点环境变量将更新，并触发与该断点环境变量关联的组件刷新，从而实现界面内容的同步更新。装饰变量声明如下，更多场景请参考[@Env：环境变量](../harmonyos-guides/arkts-env-system-property.md)。

获取@Component/@ComponentV2所在窗口的环境变量信息后，当窗口尺寸变化时，断点环境变量将根据新的窗口尺寸更新，并触发相关UI组件的刷新。常见场景包括：

* 通过BuilderNode切换窗口后，触发断点环境变量重新获取断点信息。
* 横竖屏或折叠状态切换时，窗口的横纵向断点刷新，断点环境变量将同步更新。

断点环境变量具体使用方式请参考@Env：环境变量[使用场景](../harmonyos-guides/arkts-env-system-property.md#使用场景)。环境变量初始化流程请参考[@Env初始化流程](../harmonyos-guides/arkts-env-system-property.md#env初始化流程)。

**通过主动监听断点变化刷新UI**

1. 使用自定义窗口信息类WindowInfo保存窗口断点信息。

   ```
   1. @Observed
   2. export class WindowInfo {
   3. // ...
   4. // Width/height breakpoint.
   5. public widthBp: WidthBreakpoint = WidthBreakpoint.WIDTH_XS;
   6. public heightBp: HeightBreakpoint = HeightBreakpoint.HEIGHT_SM;
   7. // ...
   8. }
   ```

   [WindowUtil.ets](https://gitcode.com/HarmonyOS_Samples/ResponsiveLayout/blob/master/entry/src/main/ets/utils/WindowUtil.ets#L362-L385)
2. WindowUtil类中创建窗口信息类对象，使用[getWindowWidthBreakpoint()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getwindowwidthbreakpoint13)与[getWindowHeightBreakpoint()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getwindowheightbreakpoint13)获取当前窗口横向断点与纵向断点。通过[on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)开启窗口尺寸变化的监听，并在监听回调中重新获取断点。

   ```
   1. export class WindowUtil {
   2. // ...
   3. public mainWindowInfo: WindowInfo = new WindowInfo();
   4. // ...
   5. public onWindowSizeChange: (windowSize: window.Size) => void = (windowSize: window.Size) => {
   6. this.mainWindowInfo.windowSize = windowSize;
   7. this.mainWindowInfo.widthBp = this.uiContext!.getWindowWidthBreakpoint();
   8. this.mainWindowInfo.heightBp = this.uiContext!.getWindowHeightBreakpoint();
   9. };
   10. // ...
   11. updateWindowInfo(): void {
   12. try {
   13. // ...
   14. // First time get width/height breakpoint.
   15. this.mainWindowInfo.widthBp = this.uiContext!.getWindowWidthBreakpoint();
   16. this.mainWindowInfo.heightBp = this.uiContext!.getWindowHeightBreakpoint();
   17. // Register for window size change monitoring, update window size and width/height breakpoint.
   18. this.mainWindow.on('windowSizeChange', this.onWindowSizeChange);
   19. // ...
   20. } catch (error) {
   21. let err = error as BusinessError;
   22. hilog.error(0x0000, `TestLog`, `Failed to update window info. Code: ${err.code}, message: ${err.message}`);
   23. }
   24. }
   25. // ...
   26. }
   ```

   [WindowUtil.ets](https://gitcode.com/HarmonyOS_Samples/ResponsiveLayout/blob/master/entry/src/main/ets/utils/WindowUtil.ets#L31-L358)
3. 在EntryAbility的onWindowStageCreate()生命周期中，获取应用窗口实例，对WindowUtil进行初始化操作，并保存至AppStorage中。在loadContent加载完页面后，完成断点监听注册、断点更新等操作。完成上述步骤后，当窗口尺寸发生变化时，更新横纵断点。

   ```
   1. onWindowStageCreate(windowStage: window.WindowStage): void {
   2. // ...
   3. try {
   4. this.windowUtil = new WindowUtil(windowStage.getMainWindowSync());
   5. } catch (error) {
   6. let err = error as BusinessError;
   7. hilog.error(0x0000, 'TestLog', `Failed to get main window. Code: ${err.code}, message: ${err.message}`);
   8. }
   9. AppStorage.setOrCreate('windowUtil', this.windowUtil);

   11. windowStage.loadContent('pages/Index', (err) => {
   12. // ...
   13. this.windowUtil!.setUIContext();
   14. this.windowUtil!.setImmersiveType(ImmersiveType.IMMERSIVE);
   15. this.windowUtil!.updateWindowInfo();
   16. });
   17. }
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/ResponsiveLayout/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L42-L72)
4. 使用@StorageLink装饰器获取窗口管理类WindowUtil对象，子组件初始化时传递窗口信息类对象，使子组件可以获取当前窗口的断点信息。

   ```
   1. @Component
   2. export struct GridLayout {
   3. @StorageLink('windowUtil') windowUtil: WindowUtil | undefined = undefined;
   4. pageInfos: NavPathStack = new NavPathStack();

   6. build() {
   7. NavDestination() {
   8. GridView({
   9. mainWindowInfo: this.windowUtil?.mainWindowInfo,
   10. pageInfos: this.pageInfos
   11. })
   12. }
   13. // ...
   14. }
   15. }
   ```

   [GridLayout.ets](https://gitcode.com/HarmonyOS_Samples/ResponsiveLayout/blob/master/entry/src/main/ets/pages/GridLayout.ets#L25-L46)
5. 使用@ObjectLink装饰器接收窗口信息类对象，根据获取的窗口信息，对不同断点区间进行针对性布局。如下示例代码完成了在不同断点下，Grid组件显示不同数量列的功能。

   ```
   1. @Component
   2. export struct GridView {
   3. @ObjectLink mainWindowInfo: WindowInfo;
   4. // ...

   6. build() {
   7. Scroll() {
   8. Column() {
   9. // ...
   10. Grid() {
   11. // ...
   12. }
   13. .width('100%')
   14. .columnsTemplate(`repeat(${new WidthBreakpointType(2, 3, 4, 4).getValue(this.mainWindowInfo.widthBp)}, 1fr)`)
   15. .columnsGap(12)
   16. .rowsGap(12)
   17. }
   18. // ...
   19. }
   20. // ...
   21. }
   22. }
   ```

   [GridView.ets](https://gitcode.com/HarmonyOS_Samples/ResponsiveLayout/blob/master/entry/src/main/ets/views/GridView.ets#L21-L92)

### 横向断点的使用案例

针对布局拉通（两个宽度相近的窗口，页面布局应保持一致），本章节介绍实际开发中横向断点的使用。

实现多设备应用时，首先根据不同设备类型对应的横向断点集合，规划多种设计方案。例如，应用需要支持手机、双折叠（Mate X系列）和平板，需要考虑的三个横向断点分别是sm、md和lg，并设计相应页面布局。设计效果图如下：

| sm | md | lg |
| --- | --- | --- |
|  |  |  |

在实际应用开发中，可能不会涉及到全部的横向断点。开发者可以根据应用的实际需求，灵活选用并整理工具类，为响应式布局的属性赋值。例如，如果应用仅需适配手机、双折叠和平板设备，可以设计工具类 “WidthBreakpointType”，覆盖三个横向断点下的成员变量，从而实现具体的响应式布局。

```
1. export class WidthBreakpointType<T> {
2. sm: T;
3. md: T;
4. lg: T;
5. xl: T;

7. constructor(sm: T, md: T, lg: T, xl: T) {
8. this.sm = sm;
9. this.md = md;
10. this.lg = lg;
11. this.xl = xl
12. }

14. getValue(widthBp: WidthBreakpoint): T {
15. if (widthBp === WidthBreakpoint.WIDTH_XS || widthBp === WidthBreakpoint.WIDTH_SM) {
16. return this.sm;
17. }
18. if (widthBp === WidthBreakpoint.WIDTH_MD) {
19. return this.md;
20. }
21. if (widthBp === WidthBreakpoint.WIDTH_LG) {
22. return this.lg;
23. } else {
24. return this.xl;
25. }
26. }
27. }
```

[WidthBreakpointType.ets](https://gitcode.com/harmonyos_samples/ResponsiveLayout/blob/master/entry/src/main/ets/utils/WidthBreakpointType.ets#L17-L43)

在实际开发中，设置不同断点下的字体大小。例如，在sm、md、lg横向断点下，字体大小分别为14fp、16fp、18fp，通过工具类BreakpointType为属性赋值。

```
1. Text('Test')
2. .fontSize(new BreakpointType('14fp', '16fp', '18fp').getValue(this.currentWidthBreakpoint))
```

[VideoExample.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/ResponsiveLayout/entry/src/main/ets/pages/VideoExample.ets#L87-L88)

在sm和md横向断点下，字体大小为14fp；在lg断点下，字体大小为16fp。使用三元表达式结合横向断点为属性赋值。

```
1. Text('Test')
2. .fontSize(this.currentWidthBreakpoint === WidthBreakpoint.WIDTH_LG ? '16fp' : '14fp')
```

[UpdateWidthExample.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/ResponsiveLayout/entry/src/main/ets/pages/UpdateWidthExample.ets#L23-L24)

### 纵向断点的使用案例

针对高度相对宽度较小的窗口（如横向窗口或类方形窗口），本章节将介绍如何在实际开发中结合使用横向断点和纵向断点进行特殊布局设计。

系统推荐以下方式判断横向窗口或类方形窗口，并展示特殊页面布局。

| 窗口类型 | 横向窗口 | 类方形窗口 |
| --- | --- | --- |
| 效果图 |  |  |
| 判断条件 | 纵向断点为sm或窗口高宽比小于0.8 | 纵向断点为md或窗口高宽比在[0.8, 1.2)之间 |

```
1. // Judgment of the horizontal window. (The actual application may need to be combined with other conditions, for example, determine the horizontal breakpoint)
2. if (this.currentHeightBreakpoint === HeightBreakpoint.HEIGHT_SM &&
3. this.currentWidthBreakpoint === WidthBreakpoint.WIDTH_MD) {
4. // Horizontal window page layout.
5. }
6. // Judgment of the square window. (The actual use may need to be combined with other conditions, such as determining horizontal breakpoints)
7. if (this.currentHeightBreakpoint === HeightBreakpoint.HEIGHT_MD &&
8. this.currentWidthBreakpoint === WidthBreakpoint.WIDTH_SM) {
9. // Square-like window page layout.
10. }
```

[VideoExample.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/ResponsiveLayout/entry/src/main/ets/pages/VideoExample.ets#L39-L48)

**独特的小窗口布局**

为了提供独特的用户体验，类方形小窗口设计为独特布局。常见场景为手机上下1:1分屏或Pura X外屏，可使用横向断点为sm，纵向断点为md进行区分，示意图如下。更多详情和示例代码请参考[Pura X阔折叠应用开发](bpta-purax-guide.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/EW7Y5wnJTHmOggycGJO74A/zh-cn_image_0000002355146073.png?HW-CC-KV=V1&HW-CC-Date=20260429T061153Z&HW-CC-Expire=86400&HW-CC-Sign=341CDC6E47CBDE3AC73AF7D484119C187CB386B40CD748F291288DAB43FD12AC)

**类方屏旋转方案**

在Mate X5内屏等类方屏窗口场景中，设计应用窗口支持旋转，以满足不同用户的体验需求。

判断纵向断点为md时，通过[window.setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9-1)设置窗口支持旋转。

```
1. let currentHeightBreakpoint: HeightBreakpoint | undefined = AppStorage.get('currentHeightBreakpoint');
2. if (currentHeightBreakpoint === HeightBreakpoint.HEIGHT_MD) {
3. this.mainWindowClass?.setPreferredOrientation(window.Orientation.AUTO_ROTATION_RESTRICTED).catch((error: BusinessError) => {
4. hilog.error(0x0000, 'VideoExample',
5. `setPreferredOrientation failed. code=${error.code}, message = ${error.message}`);
6. });
7. }
```

[VideoExample.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/ResponsiveLayout/entry/src/main/ets/pages/VideoExample.ets#L52-L58)

说明

* 应用设置窗口旋转方案需要结合多种条件一起判断，详情可参考[为多设备配置旋转策略](bpta-multi-device-window-direction.md#section189311691213)。
* Pura X外屏默认不支持窗口旋转。

**其他特殊场景**

除了独特的小窗口布局和类方屏旋转方案外，在开发过程中存在特殊场景，仅使用横向断点无法区分，需要结合横向断点和纵向断点进行判断。

本章节以视频类应用的全屏播放页为例。在手机横屏时，不支持旋转；在双折叠展开态和平板竖屏时，支持旋转。由于这三种场景的横向断点都在md范围内，无法区分，因此需要结合横向断点和纵向断点进行区分，以兼容多种设备的全屏播放窗口旋转方案。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/niUEvoplQkSKKdm3hbPPFA/zh-cn_image_0000002321147370.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061153Z&HW-CC-Expire=86400&HW-CC-Sign=D156C67BC66B084284EAA51AB10CBEC5520F0C1107A9D5B934CBC338FD29E025 "点击放大")

1. 确保已完成[通过断点刷新UI](bpta-multi-device-responsive-layout.md#section175001836203617)中步骤5和步骤6的初始化操作。
2. 使用@Watch装饰器监听状态变量isFullScreen的变化，以判断视频是否全屏播放，并在显示或隐藏时同步修改窗口方向。全屏播放时，未使用断点的窗口设置逻辑如下：需要将窗口设置为AUTO\_ROTATION\_LANDSCAPE属性的情况包括手机、双折叠屏（X 系列）的折叠态与半折态。

   **图4** **手机效果图**  
   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/mLNfJIeiSUihssd9JP435Q/zh-cn_image_0000002355265933.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061153Z&HW-CC-Expire=86400&HW-CC-Sign=D617495ED788E8DA36B745146A4139B57B8F304C9BF7CCD017359ABD6AA176E1 "点击放大")

   **图5** **双折叠屏（X系列）半折态**  
   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/ZtWxUVVSQjOrgYHwQSo0yQ/zh-cn_image_0000002321307226.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061153Z&HW-CC-Expire=86400&HW-CC-Sign=4B5F80261662097197F240CAC6BBCC71B1509DFC7DE6CA221FCA1FD24996D45A "点击放大")

   **反例：**

   ```
   1. if (this.isFullScreen) {
   2. if (deviceInfo.deviceType !== '2in1') {
   3. this.windowUtil!.disableWindowSystemBar();
   4. }
   5. try {
   6. if ((!display.isFoldable() && deviceInfo.deviceType === 'phone') ||
   7. display.getFoldStatus() === display.FoldStatus.FOLD_STATUS_FOLDED) {
   8. this.windowUtil!.setMainWindowOrientation(window.Orientation.AUTO_ROTATION_LANDSCAPE);
   9. }
   10. if (display.isFoldable()) {
   11. if (this.isHalfFolded) {
   12. this.windowUtil!.setMainWindowOrientation(window.Orientation.AUTO_ROTATION_LANDSCAPE);
   13. }
   14. }
   15. } catch (error) {
   16. let err = error as BusinessError
   17. hilog.error(0x0000, 'VideoExample',
   18. `setMainWindowOrientation failed. code=${err.code}, message = ${err.message}`);
   19. }
   20. }
   ```

   [VideoExample.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/ResponsiveLayout/entry/src/main/ets/pages/VideoExample.ets#L61-L80)

   在进入全屏页时，通过isFoldable、deviceType和getFoldStatus三个值共同判断，这种方式可读性和维护性较差。随着鸿蒙生态的拓展，不同设备上可能会出现各种异常情况。

   **正例：**

   * 双折叠屏（X系列）展开态与平板，支持旋转。双折叠屏（X系列）的横向断点为md，纵向断点为md；平板横向持握时横向断点为lg，竖向持握时横向断点为md，纵向断点为lg。将窗口显示方向设置为AUTO\_ROTATION\_RESTRICTED。
   * 手机与双折叠屏（X系列）折叠态竖屏时的横向断点为sm，纵向断点为lg，全屏播放时支持横向旋转。将窗口显示方向设置为AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED。
   * 手机与双折叠屏（X系列）折叠态横屏时的横向断点为md，纵向断点为sm，此时如果退出全屏播放，则竖屏展示布局。将窗口显示方向设置为PORTRAIT。

     说明

     本案例未覆盖部分手机（如Pocket 2、Pura 70Pro）横屏时横向断点落入lg的情况。

     ```
     1. // entry/src/main/ets/page/VideoExample.ets
     2. private onFullScreenChange(): void {
     3. // Large folding screen (X series) in unfolded state and tablet state, supporting rotation && large folding screen (X series) in hover state requires landscape display and does not support rotation.
     4. if (((this.currentWidthBreakpoint === WidthBreakpoint.WIDTH_MD && this.currentHeightBreakpoint !==
     5. HeightBreakpoint.HEIGHT_SM) || this.currentWidthBreakpoint === WidthBreakpoint.WIDTH_LG) &&
     6. !this.isHalfFolded) {
     7. this.windowUtil?.setMainWindowOrientation(window.Orientation.AUTO_ROTATION_RESTRICTED);
     8. }
     9. // Phone and large folding screen (X series) in portrait mode.
     10. else if (this.currentWidthBreakpoint === WidthBreakpoint.WIDTH_SM && this.currentHeightBreakpoint ===
     11. HeightBreakpoint.HEIGHT_LG) {
     12. // In full-screen mode, the layout is displayed in landscape mode. Otherwise, the layout is displayed in portrait mode.
     13. if (this.isFullScreen) {
     14. this.windowUtil?.setMainWindowOrientation(window.Orientation.AUTO_ROTATION_LANDSCAPE_RESTRICTED);
     15. } else {
     16. this.windowUtil?.setMainWindowOrientation(window.Orientation.PORTRAIT);
     17. }
     18. }
     19. // When the mobile phone and large folding screen (X series) are folded in landscape mode and the playback is not in full screen mode, the vertical display layout is displayed.
     20. else if (this.currentWidthBreakpoint === WidthBreakpoint.WIDTH_MD && this.currentHeightBreakpoint ===
     21. HeightBreakpoint.HEIGHT_SM && !this.isFullScreen) {
     22. this.windowUtil?.setMainWindowOrientation(window.Orientation.PORTRAIT);
     23. }
     24. // The navigation bar is not hidden on a 2in1 device.
     25. if (deviceInfo.deviceType !== '2in1') {
     26. // The navigation bar is hidden in full-screen playback. Otherwise, the navigation bar is displayed.
     27. if (this.isFullScreen) {
     28. this.windowUtil!.disableWindowSystemBar();
     29. } else {
     30. this.windowUtil!.enableWindowSystemBar();
     31. }
     32. }
     33. }
     34. }
     ```

     [VideoExample.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/ResponsiveLayout/entry/src/main/ets/pages/VideoExample.ets#L120-L156)

通过纵向和横向断点替换之前的逻辑，开发者只需维护一套方案。这实现了“全屏播放”页在多设备上的兼容。在实际开发中，多设备兼容均可采用此方案进行适配。

## 媒体查询

在实际应用开发过程中，开发者常常需要针对不同类型设备或同一类型设备的不同状态来修改应用的样式。媒体查询提供了丰富的媒体特征监听能力，可以监听应用显示区域变化、横竖屏、深浅色、设备类型等，因此在应用开发过程中使用的非常广泛。

本小节主要介绍媒体查询跟断点的结合，即如何借助媒体查询能力，监听断点的变化，关于媒体查询的相关介绍请参见[媒体查询](../harmonyos-guides/arkts-layout-development-media-query.md)。

**示例：**

通过媒体查询，监听应用窗口宽度变化，获取当前应用所处的断点值。

| sm | md | lg |
| --- | --- | --- |
|  |  |  |

1. 对通过媒体查询监听[断点](bpta-multi-device-responsive-layout.md#section1532120147301)的功能做简单的封装，方便后续使用。

   ```
   1. import { mediaquery } from '@kit.ArkUI';

   3. export type BreakpointType = 'xs' | 'sm' | 'md' | 'lg' | 'xl' | 'xxl';

   5. export interface Breakpoint {
   6. name: BreakpointType
   7. size: number
   8. mediaQueryListener?: mediaquery.MediaQueryListener
   9. }

   11. export class BreakpointSystem {
   12. private static instance: BreakpointSystem;
   13. private readonly breakpoints: Breakpoint[] = [
   14. { name: 'xs', size: 0 },
   15. { name: 'sm', size: 320 },
   16. { name: 'md', size: 600 },
   17. { name: 'lg', size: 840 }
   18. ]
   19. private states: Set<BreakpointState<Object>>;

   21. private constructor() {
   22. this.states = new Set();
   23. }

   25. public static getInstance(): BreakpointSystem {
   26. if (!BreakpointSystem.instance) {
   27. BreakpointSystem.instance = new BreakpointSystem();
   28. }
   29. return BreakpointSystem.instance;
   30. }

   32. public attach(state: BreakpointState<Object>): void {
   33. this.states.add(state);
   34. }

   36. public detach(state: BreakpointState<Object>): void {
   37. this.states.delete(state);
   38. }

   40. public start() {
   41. this.breakpoints.forEach((breakpoint: Breakpoint, index) => {
   42. let condition: string;
   43. if (index === this.breakpoints.length - 1) {
   44. condition = `(${breakpoint.size}vp<=width)`;
   45. } else {
   46. condition = `(${breakpoint.size}vp<=width<${this.breakpoints[index + 1].size}vp)`;
   47. }
   48. let uiContext = AppStorage.get('uiContext') as UIContext;
   49. breakpoint.mediaQueryListener = uiContext.getMediaQuery().matchMediaSync(condition);
   50. if (breakpoint.mediaQueryListener.matches) {
   51. this.updateAllState(breakpoint.name);
   52. }
   53. breakpoint.mediaQueryListener.on('change', (mediaQueryResult) => {
   54. if (mediaQueryResult.matches) {
   55. this.updateAllState(breakpoint.name);
   56. }
   57. });
   58. })
   59. }

   61. private updateAllState(type: BreakpointType): void {
   62. this.states.forEach(state => state.update(type));
   63. }

   65. public stop() {
   66. this.breakpoints.forEach((breakpoint: Breakpoint) => {
   67. if (breakpoint.mediaQueryListener) {
   68. breakpoint.mediaQueryListener.off('change');
   69. }
   70. })
   71. this.states.clear();
   72. }
   73. }

   75. export interface BreakpointOptions<T> {
   76. xs?: T;
   77. sm?: T;
   78. md?: T;
   79. lg?: T;
   80. xl?: T;
   81. xxl?: T;
   82. }

   84. export class BreakpointState<T extends Object> {
   85. public value: T | undefined = undefined;
   86. private options: BreakpointOptions<T>;

   88. constructor(options: BreakpointOptions<T>) {
   89. this.options = options;
   90. }

   92. static of<T extends Object>(options: BreakpointOptions<T>): BreakpointState<T> {
   93. return new BreakpointState(options);
   94. }

   96. public update(type: BreakpointType): void {
   97. if (type === 'xs') {
   98. this.value = this.options.xs;
   99. } else if (type === 'sm') {
   100. this.value = this.options.sm;
   101. } else if (type === 'md') {
   102. this.value = this.options.md;
   103. } else if (type === 'lg') {
   104. this.value = this.options.lg;
   105. } else if (type === 'xl') {
   106. this.value = this.options.xl;
   107. } else if (type === 'xxl') {
   108. this.value = this.options.xxl;
   109. } else {
   110. this.value = undefined;
   111. }
   112. }
   113. }
   ```

   [Breakpoint.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/responsiveLayout/breakpoint/Breakpoint.ets#L17-L129)
2. 在页面中，通过媒体查询，监听应用窗口宽度变化，获取当前应用所处的断点值。

   ```
   1. import { BreakpointSystem, BreakpointState } from './Breakpoint';

   3. @Entry
   4. @Component
   5. struct BreakpointSample {
   6. @State compStr: BreakpointState<string> = BreakpointState.of({ sm: 'sm', md: 'md', lg: 'lg' })
   7. @State compImg: BreakpointState<Resource> = BreakpointState.of({
   8. sm: $r('app.media.sm_new'),
   9. md: $r('app.media.md_new'),
   10. lg: $r('app.media.lg_new')
   11. });

   13. aboutToAppear() {
   14. BreakpointSystem.getInstance().attach(this.compStr);
   15. BreakpointSystem.getInstance().attach(this.compImg);
   16. BreakpointSystem.getInstance().start();
   17. }

   19. aboutToDisappear() {
   20. BreakpointSystem.getInstance().detach(this.compStr);
   21. BreakpointSystem.getInstance().detach(this.compImg);
   22. BreakpointSystem.getInstance().stop();
   23. }

   25. build() {
   26. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
   27. Column()
   28. .height(100)
   29. .width(100)
   30. .backgroundImage(this.compImg.value)
   31. .backgroundImagePosition(Alignment.Center)
   32. .backgroundImageSize(ImageSize.Contain)

   34. Text(this.compStr.value)
   35. .fontSize(24)
   36. .margin(10)
   37. }
   38. .width('100%')
   39. .height('100%')
   40. }
   41. }
   ```

   [BreakpointSample.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/responsiveLayout/breakpoint/BreakpointSample.ets#L17-L57)

## 栅格

栅格系统是一种用于页面布局的二维网格结构，多设备场景下通用的辅助定位工具。它将页面水平方向划分为等宽的列，通过设置内容占据的列数来实现灵活的布局。

栅格可以显著降低适配不同屏幕尺寸的设计及开发成本，使得整体设计和开发流程更有秩序和节奏感，同时也保证多设备上应用显示的协调性和一致性，提升用户体验。

HarmonyOS的栅格系统采用了12列设计，因为12可以被2、3、4、6整除，提供了更灵活的布局可能性。栅格布局主要优势包括：

1. 提供可循的规律：栅格布局可以为布局提供规律性的结构，解决多尺寸多设备的动态布局问题。通过将页面划分为等宽的列数和行数，可以方便地对页面元素进行定位和排版。
2. 统一的定位标注：栅格布局可以为系统提供一种统一的定位标注，保证不同设备上各个模块的布局一致性。这可以减少设计和开发的复杂度，提高工作效率。
3. 灵活的间距调整方法：栅格布局可以提供一种灵活的间距调整方法，满足特殊场景布局调整的需求。通过调整列与列之间和行与行之间的间距，可以控制整个页面的排版效果。
4. 自动换行和自适应：栅格布局可以完成一对多布局的自动换行和自适应。当页面元素的数量超出了一行或一列的容量时，他们会自动换到下一行或下一列，并且在不同的设备上自适应排版，使得页面布局更加灵活和适应性强。

**图6** 栅格示意图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/30WhVdaWQLC2cBXDFQTF_w/zh-cn_image_0000002461092273.png?HW-CC-KV=V1&HW-CC-Date=20260429T061153Z&HW-CC-Expire=86400&HW-CC-Sign=3CEE046EEFFEEC722F19448B6DB95B4C8172662934F47A2AC391C5E39A014368 "点击放大")

栅格的样式由Margin、Gutter、Columns三个属性决定。

* Margin是相对应用窗口、父容器的左右边缘的距离，决定了内容可展示的整体宽度。
* Gutter是相邻的两个Column之间的距离，决定内容间的紧密程度。
* Columns是栅格中的列数，其数值决定了内容的布局复杂度。

单个Column的宽度是系统结合Margin、Gutter和Columns自动计算的，不需要也不允许开发者手动配置。

以竖屏手机的栅格宽度计算为例：

屏幕宽度：360vp

Margin： 24vp

Gutter： 24vp

栅格数： 4个（含3个Gutter）

计算公式如下：

1个栅格的宽度 = (屏幕宽度 - Margin x 2 - Gutter x 3)/4 = (360 - 24 x 2 - 24 x 3)/4 = 60(vp)

2个栅格的宽度 = 1个栅格的宽度 + Gutter + 1个栅格的宽度 = 60 + 24 + 60 = 144(vp)

3个栅格的宽度 = 2个栅格的宽度 + Gutter + 1个栅格的宽度 = 144 + 24 + 60 = 228(vp)

4个栅格的宽度 = 3个栅格的宽度 + Gutter + 1个栅格的宽度 = 228 + 24 + 60 = 312(vp)

综合权衡各类设备的屏幕特征，基于8vp为网格的基本单位可以对界面上元素的大小、位置、对齐方式进行更好的规划，构建更有层次感、秩序感，以及多设备上一致的布局效果。一些更小的控件（例如图标）大小也可以对齐4vp的网格大小。栅格化布局中的Margin和Gutter的值参考8vp/4vp网格系统设置。如，手机设备上的栅格化设计，基础栅格Margin为24vp，等于3个8vp的宽度；卡片栅格Margin为12vp，等于一个8vp加上一个4vp的宽度。

各类设备的栅格数、Margin、Gutter的参数，如下表所示：

| 参数项 | 手机 | 折叠屏 | 平板 | 车机 | 智慧屏 |
| --- | --- | --- | --- | --- | --- |
| 竖屏栅格数（个） | 4 | 8 | 8 | - | - |
| 横屏栅格数（个） | 8 | 8 | 12 | 12 | 12 |
| 基础栅格Margin（vp） | 24 | 24 | 24 | 24 | 48 |
| 基础栅格Gutter（vp） | 24 | 24 | 24 | 24 | 24 |
| 卡片栅格Margin（vp） | 12 | 12 | 12 | 12 | 48 |
| 卡片栅格Gutter（vp） | 12 | 12 | 12 | 12 | 24 |

栅格布局就是栅格结合了断点，实现栅格布局能力的组件叫栅格组件。在实际使用场景中，可以根据需要配置不同断点下栅格组件中元素占据的列数，同时也可以调整Margin、Gutter、Columns的取值，从而实现不同的布局效果。

| sm断点 | md断点 |
| --- | --- |
|  |  |

说明

* ArkUI在API version 9对栅格组件做了重构，推出了新的栅格组件[GridRow](../harmonyos-references/ts-container-gridrow.md)和[GridCol](../harmonyos-references/ts-container-gridcol.md)，同时原有的[GridContainer组件](../harmonyos-references/ts-container-gridcontainer.md)及[栅格设置](../harmonyos-references/ts-universal-attributes-grid.md)已经废弃。
* 本文中提到的栅格组件，如无特别说明，都是指GridRow和GridCol组件。

### 栅格组件的断点

栅格组件提供了丰富的断点定制能力。

**（一）开发者可以修改断点的取值范围，支持启用最多6个断点。**

* 基于本文断点小节介绍的推荐值，栅格组件默认提供xs、sm、md、lg四个断点。
* 栅格组件支持开发者修改断点的取值范围，除了默认的四个断点，还支持开发者启用xl和xxl两个额外的断点。

  说明

  断点并非越多越好，通常每个断点都需要开发者“精心适配”以达到最佳显示效果。

**示例1：**

修改默认的断点范围，同时启用xl和xxl断点。

图片左下角显示了当前设备屏幕的尺寸（即应用窗口尺寸），可以看到随着窗口尺寸发生变化，栅格的断点也相应发生了改变（为了便于理解，下图中将设备的DPI设置为160，此时1vp=1px）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/mXEV2SEZSRCuxTUNSXQSUw/zh-cn_image_0000002355265993.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061153Z&HW-CC-Expire=86400&HW-CC-Sign=A93F20C236C394333CCF5FDF9BD70720A25F717EB2963A9CCB48FCD1EA36E764 "点击放大")

```
1. @Entry
2. @Preview
3. @Component
4. struct GridRowSample1 {
5. @State currentBreakpoint: string = 'md';

7. build() {
8. GridRow({ breakpoints: { value: ['320vp', '600vp', '840vp', '1440vp'] } }) {
9. GridCol({
10. span: {
11. xs: 12,
12. sm: 12,
13. md: 12,
14. lg: 12,
15. xl: 12
16. }
17. }) {
18. Row() {
19. Text(this.currentBreakpoint)
20. .fontSize(100)
21. .fontWeight(FontWeight.Bolder)
22. }
23. .width('100%')
24. .height('100%')
25. .alignItems(VerticalAlign.Center)
26. .justifyContent(FlexAlign.Center)
27. }
28. }
29. .onBreakpointChange((breakPoint: string) => {
30. this.currentBreakpoint = breakPoint;
31. })
32. }
33. }
```

[GridRowSample1.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/gridRow/gridRow/GridRowSample1.ets#L17-L49)

**（二）栅格断点默认以窗口宽度为参照物，同时还允许开发者配置为以栅格组件本身的宽度为参照物。**

栅格既可以用于页面整体布局的场景，也可以用于页面局部布局的场景。考虑到在实际场景中，存在应用窗口尺寸不变但是局部区域尺寸发生了变化的情况，栅格组件支持以自身宽度为参照物响应断点变化具有更大的灵活性。

**示例2：**

以栅格组件宽度为参考物响应断点变化。满足窗口尺寸不变，而部分内容区需要做响应式变化的场景。

为了便于理解，可将自定义预览器的设备屏幕宽度设置为650vp。示例代码中将侧边栏的变化范围控制在[100vp, 600vp]，那么右侧的栅格组件宽度相对应在[550vp, 50vp]之间变化。根据代码中对栅格断点的配置，栅格组件宽度发生变化时，其断点相应的发生改变。

```
1. @Entry
2. @Component
3. struct GridRowSample2 {
4. @State currentBreakpoint: string = 'md';

6. build() {
7. // Users can adjust the width of the sidebar and content area by dragging the divider in the sidebar component.
8. SideBarContainer(SideBarContainerType.Embed) {
9. // Sidebar, with a resizable range of [100vp, 600vp].
10. Column() {
11. }
12. .width('100%')
13. .backgroundColor($r('sys.color.comp_background_secondary'))

15. // Content area.
16. GridRow({
17. breakpoints: {
18. value: ['320vp', '600vp', '840vp', '1440vp'],
19. reference: BreakpointsReference.ComponentSize
20. }
21. }) {
22. GridCol({
23. span: {
24. xs: 12,
25. sm: 12,
26. md: 12,
27. lg: 12,
28. xl: 12
29. }
30. }) {
31. Row() {
32. Text(this.currentBreakpoint)
33. .fontSize(50)
34. .fontWeight(FontWeight.Bolder)
35. }
36. .width('100%')
37. .height('100%')
38. .justifyContent(FlexAlign.Center)
39. .alignItems(VerticalAlign.Center)
40. }
41. }
42. .onBreakpointChange((currentBreakpoint: string) => {
43. this.currentBreakpoint = currentBreakpoint;
44. })
45. .width('100%')
46. }
47. // The sidebar does not auto-hide when dragged to its minimum width.
48. .autoHide(false)
49. .sideBarWidth(100)
50. // Minimum width of the sidebar.
51. .minSideBarWidth(100)
52. // Maximum width of the sidebar.
53. .maxSideBarWidth(600)
54. }
55. }
```

[GridRowSample2.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/gridRow/gridRow/GridRowSample2.ets#L17-L71)

**（三）栅格组件的断点发生变化时，会通过onBreakPointChange事件通知开发者。**

在之前的两个例子中，已经演示了onBreakpointChange事件的用法，此处不再赘述。

### 栅格组件的columns、gutter和margin

栅格组件columns默认为12列，gutter默认为0，同时支持开发者根据实际需要定义不同断点下的columns数量以及gutter长度。特别的，在栅格组件实际使用过程中，常常会发生多个元素占据的列数相加超过总列数而折行的场景。栅格组件还允许开发者分别定义水平方向的gutter（相邻两列之间的间距）和垂直方向的gutter（折行时相邻两行之间的间距）。

考虑到[组件通用属性](../harmonyos-references/ts-component-general-attributes.md)中已经有margin和padding，栅格组件不再单独提供额外的margin属性，直接使用通用属性即可。借助margin或者padding属性，均可以控制栅格组件与父容器左右边缘的距离，但是二者也存在一些差异：

* margin区域在栅格组件的边界外，padding区域在栅格组件的边界内。
* 栅格组件的backgroundColor会影响padding区域，但不会影响margin区域。

总的来讲，margin在组件外而padding在组件内，开发者可以根据实际需要进行选择及实现目标效果。

**示例3：**

不同断点下，定义不同的columns和gutter。

| sm | md | lg |
| --- | --- | --- |
|  |  |  |

```
1. @Entry
2. @Component
3. struct GridRowSample3 {
4. private bgColors: ResourceColor[] = [
5. $r('sys.color.ohos_id_color_palette_aux1'),
6. $r('sys.color.ohos_id_color_palette_aux2'),
7. $r('sys.color.ohos_id_color_palette_aux3'),
8. $r('sys.color.ohos_id_color_palette_aux4'),
9. $r('sys.color.ohos_id_color_palette_aux5'),
10. $r('sys.color.ohos_id_color_palette_aux6')
11. ];

13. build() {
14. // Config the values of columns and gutter at different breakpoints.
15. GridRow({
16. columns: { sm: 4, md: 8, lg: 12 },
17. gutter: {
18. x: { sm: 8, md: 16, lg: 24 },
19. y: { sm: 8, md: 16, lg: 24 }
20. }
21. }) {
22. ForEach(this.bgColors, (bgColor: ResourceColor) => {
23. GridCol({ span: { sm: 2, md: 2, lg: 2 } }) {
24. Row()
25. .width('100%')
26. .backgroundColor(bgColor)
27. .height(30)
28. }
29. }, (bgColor: ResourceColor) => bgColor.toString())
30. }
31. }
32. }
```

[GridRowSample3.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/gridRow/gridRow/GridRowSample3.ets#L17-L48)

**示例4：**

通过通用属性margin或者padding，均可以控制栅格组件与其父容器左右两侧的距离，但padding区域计算在栅格组件内而margin区域计算在栅格组件外。此外，借助onBreakpointChange事件，还可以改变不同断点下margin或padding值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/5_uFwIiLS8emRBOSc-W9CQ/zh-cn_image_0000002355266017.png?HW-CC-KV=V1&HW-CC-Date=20260429T061153Z&HW-CC-Expire=86400&HW-CC-Sign=A37BF916197BF987450B3B27365BF6B538766F825E68DB615A32001021A0B5A7 "点击放大")

```
1. @Entry
2. @Component
3. struct GridRowSample4 {
4. @State gridMargin: number = 0;

6. build() {
7. Column() {
8. Row()
9. .width('100%')
10. .height(30)

12. // Control the left and right spacing of the grid using padding.
13. GridRow() {
14. GridCol({ span: { sm: 12, md: 12, lg: 12 } }) {
15. Row() {
16. Text('padding')
17. .fontSize(24)
18. .fontWeight(FontWeight.Medium)
19. }
20. .width('100%')
21. .height('100%')
22. .alignItems(VerticalAlign.Center)
23. .justifyContent(FlexAlign.Center)
24. .backgroundColor($r('sys.color.comp_background_secondary'))
25. }
26. }
27. .height(50)
28. .borderWidth(2)
29. .borderColor('#F1CCB8')
30. .padding({
31. left: this.gridMargin,
32. right: this.gridMargin
33. })
34. // Configure the left and right spacing values of grid components at different breakpoints using breakpoint change events.
35. .onBreakpointChange((currentBreakpoint: string) => {
36. if (currentBreakpoint === 'xs' || currentBreakpoint === 'sm') {
37. this.gridMargin = 12;
38. } else {
39. this.gridMargin = 24;
40. }
41. })

43. Row()
44. .width('100%')
45. .height(30)

47. // Control the left and right spacing of the grid using margin.
48. GridRow() {
49. GridCol({ span: { sm: 12, md: 12, lg: 12 } }) {
50. Row() {
51. Text('margin')
52. .fontSize(24)
53. .fontWeight(FontWeight.Medium)
54. }
55. .width('100%')
56. .height('100%')
57. .alignItems(VerticalAlign.Center)
58. .justifyContent(FlexAlign.Center)
59. .backgroundColor($r('sys.color.comp_background_secondary'))
60. }
61. }
62. .height(50)
63. .borderWidth(2)
64. .borderColor('#F1CCB8')
65. .margin({
66. left: this.gridMargin,
67. right: this.gridMargin
68. })
69. }
70. }
71. }
```

[GridRowSample4.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/gridRow/gridRow/GridRowSample4.ets#L17-L87)

### 栅格组件的span、offset和order

栅格组件（GridRow）的直接孩子节点只可以是栅格子组件（GridCol），GridCol组件支持配置span、offset和order三个参数。这三个参数的取值按照"xs -> sm -> md -> lg -> xl -> xxl"的向后方向具有继承性（不支持向前方向的继承性），例如将sm断点下span的值配置为3，不配置md断点下span的值，则md断点下span的取值也是3。

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| span | {xs?: number, sm?: number, md?: number, lg?: number, xl?: number, xxl?:number} | 是 | - | 在栅格中占据的列数。span为0，意味着该元素既不参与布局计算，也不会被渲染。 |
| offset | {xs?: number, sm?: number, md?: number, lg?: number, xl?: number, xxl?:number} | 否 | 0 | 相对于前一个栅格子组件偏移的列数。 |
| order | {xs?: number, sm?: number, md?: number, lg?: number, xl?: number, xxl?:number} | 否 | 0 | 元素的序号，根据栅格子组件的序号，从小到大对栅格子组件做排序。 |

**示例5：**

通过span参数配置GridCol在不同断点下占据不同的列数。特别的，将md断点下3和6的span配置为0，这样在md断点下3和6不会渲染和显示。

| sm | md | lg |
| --- | --- | --- |
|  |  |  |

```
1. @Entry
2. @Component
3. struct GridRowSample5 {
4. private elements: ColorArr[] = [
5. { index: 1, color: $r('sys.color.ohos_id_color_palette_aux1') },
6. { index: 2, color: $r('sys.color.ohos_id_color_palette_aux2') },
7. { index: 3, color: $r('sys.color.ohos_id_color_palette_aux3') },
8. { index: 4, color: $r('sys.color.ohos_id_color_palette_aux4') },
9. { index: 5, color: $r('sys.color.ohos_id_color_palette_aux5') },
10. { index: 6, color: $r('sys.color.ohos_id_color_palette_aux6') }
11. ];

13. build() {
14. GridRow({ columns: { sm: 12, md: 12, lg: 12 } }) {
15. ForEach(this.elements, (item: ColorArr) => {
16. GridCol({ span: { sm: 6, md: item.index % 3 === 0 ? 0 : 4, lg: 3 } }) {
17. Row() {
18. Text(`${item.index}`)
19. .fontSize(24)
20. }
21. .justifyContent(FlexAlign.Center)
22. .backgroundColor(item.color)
23. .height(30)
24. .width('100%')
25. }
26. }, (item: ColorArr, index: number) => (item.index + index).toString())
27. }
28. }
29. }
```

[GridRowSample5.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/gridRow/gridRow/GridRowSample5.ets#L19-L47)

**示例6：**

通过offset参数，配置GridCol相对其前一个兄弟间隔的列数。

| sm | md | lg |
| --- | --- | --- |
|  |  |  |

```
1. @Entry
2. @Component
3. struct GridRowSample6 {
4. private elements: ColorArr[] = [
5. { index: 1, color: $r('sys.color.ohos_id_color_palette_aux1') },
6. { index: 2, color: $r('sys.color.ohos_id_color_palette_aux2') },
7. { index: 3, color: $r('sys.color.ohos_id_color_palette_aux3') },
8. { index: 4, color: $r('sys.color.ohos_id_color_palette_aux4') },
9. { index: 5, color: $r('sys.color.ohos_id_color_palette_aux5') },
10. { index: 6, color: $r('sys.color.ohos_id_color_palette_aux6') }
11. ];

13. build() {
14. GridRow({ columns: { sm: 12, md: 12, lg: 12 } }) {
15. ForEach(this.elements, (item: ColorArr) => {
16. GridCol({
17. span: { sm: 6, md: 4, lg: 3 },
18. offset: { sm: 0, md: 2, lg: 1 }
19. }) {
20. Row() {
21. Text(`${item.index}`)
22. .fontSize(24)
23. }
24. .justifyContent(FlexAlign.Center)
25. .backgroundColor(item.color)
26. .height(30)
27. .width('100%')
28. }
29. }, (item: ColorArr, index: number) => (item.index + index).toString())
30. }
31. }
32. }
```

[GridRowSample6.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/gridRow/gridRow/GridRowSample6.ets#L19-L50)

**示例7：**

通过order属性，控制GridCol的顺序。在sm和md断点下，按照1至6的顺序排列显示；在lg断点下，按照6至1的顺序排列显示。

| sm | md | lg |
| --- | --- | --- |
|  |  |  |

```
1. @Entry
2. @Component
3. struct GridRowSample7 {
4. private elements: ColorArr[] = [
5. { index: 1, color: $r('sys.color.ohos_id_color_palette_aux1') },
6. { index: 2, color: $r('sys.color.ohos_id_color_palette_aux2') },
7. { index: 3, color: $r('sys.color.ohos_id_color_palette_aux3') },
8. { index: 4, color: $r('sys.color.ohos_id_color_palette_aux4') },
9. { index: 5, color: $r('sys.color.ohos_id_color_palette_aux5') },
10. { index: 6, color: $r('sys.color.ohos_id_color_palette_aux6') }
11. ];

13. build() {
14. GridRow({ columns: { sm: 12, md: 12, lg: 12 } }) {
15. ForEach(this.elements, (item: ColorArr) => {
16. GridCol({
17. span: { sm: 6, md: 4, lg: 3 },
18. order: { lg: (6 - item.index) }
19. }) {
20. Row() {
21. Text(`${item.index}`)
22. .fontSize(24)
23. }
24. .justifyContent(FlexAlign.Center)
25. .backgroundColor(item.color)
26. .height(30)
27. .width('100%')
28. }
29. }, (item: ColorArr, index: number) => (item.index + index).toString())
30. }
31. }
32. }
```

[GridRowSample7.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/gridRow/gridRow/GridRowSample7.ets#L19-L50)

**示例8：**

仅配置sm和lg断点下span、offset和order参数的值，则md断点下这三个参数的取值与sm断点相同（按照“sm->md->lg”的向后方向继承）。

| sm | md | lg |
| --- | --- | --- |
|  |  |  |

```
1. @Entry
2. @Component
3. struct GridRowSample8 {
4. private elements: ColorArr[] = [
5. { index: 1, color: $r('sys.color.ohos_id_color_palette_aux1') },
6. { index: 2, color: $r('sys.color.ohos_id_color_palette_aux2') },
7. { index: 3, color: $r('sys.color.ohos_id_color_palette_aux3') },
8. { index: 4, color: $r('sys.color.ohos_id_color_palette_aux4') },
9. { index: 5, color: $r('sys.color.ohos_id_color_palette_aux5') },
10. { index: 6, color: $r('sys.color.ohos_id_color_palette_aux6') }
11. ];

13. build() {
14. GridRow({ columns: { sm: 12, md: 12, lg: 12 } }) {
15. ForEach(this.elements, (item: ColorArr) => {
16. // If the values of the three parameters are not configured at the md breakpoint, they will inherit the values from the sm breakpoint.
17. GridCol({
18. span: { sm: 4, lg: 3 },
19. offset: { sm: 2, lg: 1 },
20. order: { sm: (6 - item.index), lg: item.index }
21. }) {
22. Row() {
23. Text(`${item.index}`)
24. .fontSize(24)
25. }
26. .justifyContent(FlexAlign.Center)
27. .backgroundColor(item.color)
28. .height(30)
29. .width('100%')
30. }
31. }, (item: ColorArr, index: number) => (item.index + index).toString())
32. }
33. }
34. }
```

[GridRowSample8.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/gridRow/gridRow/GridRowSample8.ets#L19-L52)

### 栅格组件的嵌套使用

栅格组件可以嵌套使用以满足复杂场景的需要。

**示例9：**

| sm | md | lg |
| --- | --- | --- |
|  |  |  |

```
1. @Entry
2. @Component
3. struct GridRowSample9 {
4. private elements: ColorArr[] = [
5. { index: 1, color: $r('sys.color.ohos_id_color_palette_aux1') },
6. { index: 2, color: $r('sys.color.ohos_id_color_palette_aux2') },
7. { index: 3, color: $r('sys.color.ohos_id_color_palette_aux3') },
8. { index: 4, color: $r('sys.color.ohos_id_color_palette_aux4') },
9. { index: 5, color: $r('sys.color.ohos_id_color_palette_aux5') },
10. { index: 6, color: $r('sys.color.ohos_id_color_palette_aux6') }
11. ];

13. build() {
14. GridRow({ columns: { sm: 12, md: 12, lg: 12 } }) {
15. GridCol({
16. span: { sm: 12, md: 10, lg: 8 },
17. offset: { sm: 0, md: 1, lg: 2 }
18. }) {
19. GridRow({ columns: { sm: 12, md: 12, lg: 12 } }) {
20. ForEach(this.elements, (item: ColorArr) => {
21. GridCol({ span: { sm: 6, md: 4, lg: 3 } }) {
22. Row() {
23. Text(`${item.index}`)
24. .fontSize(24)
25. }
26. .justifyContent(FlexAlign.Center)
27. .backgroundColor(item.color)
28. .height(30)
29. .width('100%')
30. }
31. }, (item: ColorArr, index: number) => JSON.stringify(item) + index)
32. }
33. .backgroundColor($r('sys.color.comp_background_secondary'))
34. .height('100%')
35. }
36. }
37. }
38. }
```

[GridRowSample9.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/gridRow/gridRow/GridRowSample9.ets#L19-L56)

## 响应式组件

HarmonyOS提供的一些组件支持响应式布局，例如： Tabs、Swiper、Grid、List、GridRow，通过断点设置可以实现不同的展示效果。

说明

响应式组件的实现原理与开发步骤，可参考[组件布局场景](bpta-multi-device-component-layout.md)。

## 响应式布局样式

当基本的自适应布局无法满足多终端上屏幕的体验要求时，我们需要针对不同终端的屏幕特点进行响应式的布局。常见的响应式布局样式有：分栏布局、重复布局、挪移布局和缩进布局。

### 分栏布局

利用屏幕的宽度优势，将导航栏与内容区同屏左右显示，如设置首页及设置详情页。

当横向vp大于等于600vp时，显示分栏布局。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/SOLxg0aSS8-xoCnsggWENg/zh-cn_image_0000002427564766.png?HW-CC-KV=V1&HW-CC-Date=20260429T061153Z&HW-CC-Expire=86400&HW-CC-Sign=2BA92B793D51738628437D115137DD129CE7B284BEA4E609BF3C3C4E908BB9C8 "点击放大")

### 重复布局

利用屏幕的宽度优势，将相同属性的组件横向并列排布。

重复布局适用于对宽高比敏感的图片和组合内容，当内容放大以后导致原图放大超过150%的场景。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/UVMRW7QKRACUD1Wq7zPgYg/zh-cn_image_0000002460966061.png?HW-CC-KV=V1&HW-CC-Date=20260429T061153Z&HW-CC-Expire=86400&HW-CC-Sign=11F265BDD31836A6F3BB758BA7001FDED8539AADC9D996FFC4930743B9C2F3AA "点击放大")

### 挪移布局

利用屏幕的宽度优势，将原先的上下布局切换成左右布局。

挪移布局适用于横竖屏切换，以及类似的宽高比明显变化 (大于 200%) ，同时希望保证内容完整的场景。

例如上下布局的插画和文字，横屏后左右布局。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/vK2tplw3TZCkTBgf_m6_rw/zh-cn_image_0000002427408746.png?HW-CC-KV=V1&HW-CC-Date=20260429T061153Z&HW-CC-Expire=86400&HW-CC-Sign=A73BA9184239222B0E42C135EFD5CED4735197B1C920527C385E73DB707D7CAB "点击放大")

### 缩进布局

为了在宽屏上内容显示有更好的效果，在不同宽度的设备上进行不同缩进效果。

缩进布局适用于纯段落文本/上图下段落文本/卡片的布局结构的场景，在其对应的栅格规格下，缩进的规则占用栅格数量进行布局。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/u_6ej50MRJSfm1JZZLX4HA/zh-cn_image_0000002321147530.png?HW-CC-KV=V1&HW-CC-Date=20260429T061153Z&HW-CC-Expire=86400&HW-CC-Sign=659889F533AD6101F24C63EFCB73F0CC435CD2174D4B5C42A6D46AB2F1548808 "点击放大")

当栅格为8 columns或12 columns时可以使用6 columns和8 columns的缩进布局。

说明

关于响应式布局样式的UX设计，可参考[响应式布局方法](../design-guides/design-responsive-layout-method-0000001795698449.md)。

关于响应式布局样式的开发实现，可参考[页面布局场景](bpta-multi-device-page-layout.md)。

## 常见问题

### 常见的触发断点变化的场景有哪些？

**问题现象**

什么场景会触发断点变化？

**解决方案**

常见的触发断点变化的场景包括以下几点：

* 设备旋转
* 折叠屏开合
* 窗口模式改变
* 自由窗口模式调节窗口大小

### 显示缩放对断点的影响

**问题现象**

系统修改显示缩放会影响页面布局

**可能原因**

vp具体计算公式为：vp= px/（DPI/160）

在用户变更缩放比例后dpi会随之变化，从而导致vp会发生变化，需要考虑vp变化后对断点区间的影响。

以Mate60手机为例，设置显示缩放后，dpi变化以及vp变化如下表所示：

| 显示缩放模式 | dpi | vp（宽度） |
| --- | --- | --- |
| 小 | 2.7625 | 440 |
| 默认 | 3.25 | 374 |
| 大 | 3.8 | 319 |

因此，可能会出现显示缩放改变导致断点前后不一致的情况。

**解决方案**

若开发者需要应用随dpi改变刷新布局，可使用[on('densityUpdate')](../harmonyos-references/arkts-apis-uicontext-uiobserver.md#ondensityupdate12)监听屏幕像素密度变化，并在监听回调中重新获取断点并刷新UI。

若开发者不希望应用受显示缩放影响布局，可以使用[setDefaultDensityEnabled()](../harmonyos-references/arkts-apis-window-windowstage.md#setdefaultdensityenabled12)设置应用是否使用系统默认Density，true表示使用系统默认Density，窗口不跟随系统显示大小变化重新布局；false表示不使用系统默认Density，窗口跟随系统显示大小变化重新布局。

### 像素转换

**问题现象**

应用开发中，像素之间的转换是非常常见的场景，需要常见像素的转换方案。

**解决方案**

应用开发中，像素之间的转换是非常常见的场景，常见的像素单位如下：

[PX](../harmonyos-references/ts-types.md#px10)（屏幕像素单位）：px，屏幕上的实际像素：1px代表手机屏幕上的一个像素点。

[VP](../harmonyos-references/ts-types.md#vp10)（虚拟像素单位）：vp，屏幕密度相关像素，根据屏幕像素密度转换为屏幕物理像素，当数值不带单位时，默认单位vp。vp与px的比例与屏幕像素密度有关。

[FP](../harmonyos-references/ts-types.md#fp10)（字体像素单位）：fp，字体像素大小默认情况下与vp相同，即默认情况下1fp = 1vp。如果用户在设置中选择了更大的字体，字体的实际显示大小就会在vp的基础上乘以scale系数，即 1fp = 1vp \* scale。

常见像素单位之间的转化请参考[vp2px](../harmonyos-references/arkts-apis-uicontext-uicontext.md#vp2px12)/[px2vp](../harmonyos-references/arkts-apis-uicontext-uicontext.md#px2vp12)/[fp2px](../harmonyos-references/arkts-apis-uicontext-uicontext.md#fp2px12)/[px2fp](../harmonyos-references/arkts-apis-uicontext-uicontext.md#px2fp12)/[lpx2px](../harmonyos-references/arkts-apis-uicontext-uicontext.md#lpx2px12)/[px2lpx](../harmonyos-references/arkts-apis-uicontext-uicontext.md#px2lpx12)等接口。

### 如何区分手机/折叠屏/平板/电脑/智慧屏/智能穿戴

**解决方案**

* 手机/折叠屏/平板/电脑设备，可参考[断点的定义](bpta-multi-device-responsive-layout.md#section186821126131515)中HarmonyOS常用设备断点区间表进行区分。

* 智慧屏设备，可参考[如何判断当前设备是智慧屏](bpta-matetv-guide.md#section6168122172416)进行区分。

* 智能穿戴设备，可参考[一多应用中如何区分智能穿戴设备](bpta-smartwatch.md#section1748314426272)进行区分。
