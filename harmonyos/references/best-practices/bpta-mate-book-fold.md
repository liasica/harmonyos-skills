---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-mate-book-fold
title: MateBook Fold折叠电脑应用开发
breadcrumb: 最佳实践 > 多端设备体验提升 > 电脑 > MateBook Fold折叠电脑应用开发
category: best-practices
scraped_at: 2026-04-29T14:13:01+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:9e39dcff7ae4a8cf2d7d99498d4b825fcdc73c8a7587ef0ac5199e92f2ebd7f8
---

## 概述

HarmonyOS折叠电脑MateBook Fold，凭借其独特的折叠设计、全屏触控和[虚拟键盘](../design-guides/foldable-pc-0000002322600098.md#虚拟键盘)的交互方式，融合了一体机、笔记本和平板三种设备的使用体验，在形态创新与交互体验方面有所提升。除了具备传统电脑的功能特性外，这款折叠电脑还具备以下核心亮点：

1. 设备形态：支持五种使用形态：半折叠态（唤起全尺寸键盘）、半折叠态（关闭全尺寸键盘）、横向展开态、竖向展开态、外接显示器。
2. 交互设计：在半折叠态下，上下两块屏幕均可独立操作。用户可以通过点击桌面右下角的键盘图标或使用多指（八指及以上）轻触屏幕来唤起全尺寸键盘，从而实现传统电脑的操作体验。
3. 屏幕显示方向：在半折叠态下，屏幕仅支持一种显示方向，不支持旋转。而在展开态下，屏幕支持三种显示方向（[display.Orientation](../harmonyos-references/js-apis-display.md#orientation10)）：横屏（1-LANDSCAPE）、反向横屏（3-LANDSCAPE\_INVERTED）和竖屏（0-PORTRAIT），并且始终支持旋转功能，无法关闭。

说明

当磁吸键盘贴附在下屏时，设备进入半折叠态（唤起全尺寸键盘），此时下屏无法使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/V5onPisXQp-oXMPSljdLqw/zh-cn_image_0000002419750993.png?HW-CC-KV=V1&HW-CC-Date=20260429T061258Z&HW-CC-Expire=86400&HW-CC-Sign=B78BA05B6042F12BE973FD9EEEFFC7F1C7411CE8AE9C0B399067DF9347F0DCA6 "点击放大")

## 硬件说明

### 屏幕规格信息

折叠电脑在不同折叠状态下具有不同的分辨率、屏幕宽度等属性：

* 在半折叠态（关闭全尺寸键盘）下，设备拥有上下两个屏幕，其中上屏的displayId为0，下屏的displayId为999。而在半折叠态（唤起全尺寸键盘）和展开态下，仅显示displayId为0的屏幕。
* 折叠电脑底部工具栏高度固定为118px，但在不同折叠电脑形态下，工具栏占用的宽度和位置不同，屏幕可用宽高（[availableWidth/availableHeight](../harmonyos-references/js-apis-display.md#属性)）也会有所不同。
* 折叠电脑外接显示器时，会自动进入横向展开态布局，且屏幕方向为反向横屏，此时折叠电脑默认作为主显示器（displayId为0），外接屏幕作为副显示器（displayId与接入的端口有关）。可使用[getWindowProperties()](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)方法获取当前窗口的属性[WindowProperties](../harmonyos-references/arkts-apis-window-i.md#windowproperties)，其中displayId为当前窗口所在屏幕的ID，从而可判断当前窗口所在的显示器。

**半折叠态屏幕规格信息**

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| [屏幕旋转角度（rotation）](../harmonyos-references/js-apis-display.md#属性) | 0(0度) | | | 1(90度) | 2(180度) | 3(270度) |
| 设备形态 | 半折叠态（唤起全尺寸键盘） | 半折叠态（关闭全尺寸键盘） | | NA | NA | NA |
| 半折叠态效果图 |  |  | | NA | NA | NA |
| [屏幕方向Orientation](../harmonyos-references/js-apis-display.md#orientation10) | 竖屏PORTRAIT | | | NA | NA | NA |
| 屏幕ID | displayId：0 | displayId：0 | displayId：999 | NA | NA | NA |
| 分辨率（px） | 2472\*1608 | 2472\*1608 | 2472\*1606 | NA | NA | NA |
| 分辨率（vp）向下取整 | 1373\*893 | 1373\*893 | 1373\*892 | NA | NA | NA |
| 屏幕可用宽高（px） | 2472\*1490（底部工具栏高度118px） | 2472\*1608 | 2472\*1488（底部工具栏高度118px） | NA | NA | NA |
| 屏幕可用宽高（vp）向下取整 | 1373\*827 | 1373\*893 | 1373\*826 | NA | NA | NA |
| [横纵断点](bpta-multi-device-responsive-layout.md#section1532120147301) | 横向断点lg，纵向断点sm | 横向断点lg，纵向断点sm | 横向断点lg，纵向断点sm | NA | NA | NA |

**展开态屏幕规格信息**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| [屏幕旋转角度（rotation）](../harmonyos-references/js-apis-display.md#属性) | 0(0度) | 1(90度) | 2(180度) | 3(270度) | |
| 设备形态 | 竖向展开态 | 横向展开态 | NA | 横向展开态 | 外接显示器 |
| 展开态效果图 |  |  | NA |  |  |
| [屏幕方向Orientation](../harmonyos-references/js-apis-display.md#orientation10) | 竖屏PORTRAIT | 横屏LANDSCAPE | NA | 反向横屏LANDSCAPE\_INVERTED | |
| 屏幕ID | displayId：0 | displayId：0 | NA | displayId：0 | 主显示器：displayId为0  外接显示器：displayId与接入的端口有关 |
| 分辨率（px） | 2472\*3296 | 3296\*2472 | NA | 3296\*2472 | 3296\*2472 |
| 分辨率（vp）向下取整 | 1373\*1831 | 1831\*1373 | NA | 1831\*1373 | 1831\*1373 |
| 屏幕可用宽高（px） | 2472\*3178（底部工具栏高度118px） | 3296\*2354（底部工具栏高度118px） | NA | 3296\*2354（底部工具栏高度118px） | 3296\*2354（底部工具栏高度118px） |
| 屏幕可用宽高（vp）向下取整 | 1373\*1765 | 1831\*1307 | NA | 1831\*1307 | 1831\*1307 |
| [横纵断点](bpta-multi-device-responsive-layout.md#section1532120147301) | 横向断点lg，纵向断点lg | 横向断点xl，纵向断点sm | NA | 横向断点xl，纵向断点sm | 横向断点xl，纵向断点sm |

**常用接口**

* 获取屏幕对象相关接口

  [Display](../harmonyos-references/js-apis-display.md#display)对象中包含屏幕宽高，屏幕可用区域宽高等重要信息，对应的Display区域如下图所示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/CYgn_IvhQQKhtYGscT9ZnA/zh-cn_image_0000002386071972.png?HW-CC-KV=V1&HW-CC-Date=20260429T061258Z&HW-CC-Expire=86400&HW-CC-Sign=27CD85143286D1116C352832194CA8532EC460A562BDDBCEC9E2FFBE5BC1C47F "点击放大")

  | API | 说明 |
  | --- | --- |
  | [display.getAllDisplays()](../harmonyos-references/js-apis-display.md#displaygetalldisplays9) | 获取所有的Display对象。不同设备形态下对应的Display区域如上图所示。 |
  | [display.getDisplayByIdSync()](../harmonyos-references/js-apis-display.md#displaygetdisplaybyidsync12) | 根据displayId获取对应的Display对象。具体的displayId可参考[屏幕规格信息](bpta-mate-book-fold.md#section05491630111312)表格中屏幕ID行。  除半折叠态（关闭全尺寸键盘）分为上下两屏，上屏displayId为0，下屏displayId为999，其余状态折叠电脑屏幕的displayId均为0。 |
  | [display.getDefaultDisplaySync()](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9) | 获取当前默认的Display对象。除半折叠态（关闭全尺寸键盘）获取的Display对象为displayId为0的上屏，其余设备形态下获取的Display区域如上图所示。 |
  | [display.getPrimaryDisplaySync()](../harmonyos-references/js-apis-display.md#displaygetprimarydisplaysync14) | 获取主屏信息。对于折叠电脑，当外接屏幕时，获取的是当前主屏幕的Display对象；当没有外接屏幕时，获取的是设备自带屏幕中displayId为0的Display对象。 |
  | [display.on('add'|'remove'|'change')](../harmonyos-references/js-apis-display.md#displayonaddremovechange) | 开启显示设备新增、移除、变化的监听。 |

  说明

  + display.on('add'|'remove'|'change')触发场景如下：
    - display.on('add')触发场景：半折叠态（唤起全尺寸键盘）->半折叠态（关闭全尺寸键盘）、外接显示器。
    - display.on('change')触发场景：涉及Display变化时，包括折叠状态、屏幕方向，可用区域变化等。
    - display.on('remove')触发场景：半折叠态（关闭全尺寸键盘）->半折叠态（唤起全尺寸键盘）、展开态、取消外接显示器。

### 其他硬件信息

折叠电脑相机预设了默认的[镜头安装角度](../harmonyos-guides/camera-rotation-term.md#相机镜头安装角度)。使用时，需考虑镜头角度与设备的旋转角度，具体定义可参考[预览旋转角度](../harmonyos-guides/camera-rotation-term.md#预览旋转角度)。当屏幕方向一致时，前置镜头角度与需设置的预览流旋转角度如下，不同设备状态下的相机参数保持一致。

|  |  |  |  |
| --- | --- | --- | --- |
| 屏幕旋转角度（rotation） | 0(0度) | 1(90度) | 3(270度) |
| 示意图 |  |  |  |
| 前置相机镜头角度 | 270° | 270° | 270° |
| 预览旋转角度 | 270°+0°=270° | 270°+90° = 0° | 270°+270° = 180° |
| 后置相机镜头角度 | 无后置相机 | | |

### 设备特有能力

折叠电脑具备独特的折叠功能，在不同折叠状态下展现出不同的特性，具体如下：

1. 折叠时，折叠电脑进入睡眠状态，应用无法获取当前的折叠状态（[display.FoldStatus](../harmonyos-references/js-apis-display.md#foldstatus10)）；半折叠时，折叠状态为FOLD\_STATUS\_HALF\_FOLDED；展开时，折叠状态为FOLD\_STATUS\_EXPANDED。
2. 通过接口[display.isFoldable()](../harmonyos-references/js-apis-display.md#displayisfoldable10)可判断设备是否支持折叠，若支持则返回true。然而，获取可折叠设备显示模式的接口[display.getFoldDisplayMode()](../harmonyos-references/js-apis-display.md#displaygetfolddisplaymode10)不适用于电脑，其返回结果为FOLD\_DISPLAY\_MODE\_UNKNOWN。

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 设备形态 | 半折叠态（唤起全尺寸键盘） | 半折叠态（关闭全尺寸键盘） | | 横向展开态 | 竖向展开态 |
| 效果图 |  |  | |  |  |
| isFoldable | true | | | | |
| FoldStatus | FOLD\_STATUS\_HALF\_FOLDED | | | FOLD\_STATUS\_EXPANDED | |
| FoldDisplayMode | FOLD\_DISPLAY\_MODE\_UNKNOWN | | | | |
| [FoldCreaseRegion](../harmonyos-references/js-apis-display.md#foldcreaseregion10) | {"left":0,"top":1608,"width":2472,"height":82} | | | | |

**常用接口**

* 获取设备折叠状态相关接口

  | API | 说明 |
  | --- | --- |
  | [display.getFoldStatus()](../harmonyos-references/js-apis-display.md#displaygetfoldstatus10) | 主动获取可折叠设备的当前折叠状态。具体折叠状态可参考上表中的FoldStatus行。 |
  | [display.on('foldStatusChange')](../harmonyos-references/js-apis-display.md#displayonfoldstatuschange10) | 开启折叠设备折叠状态变化的监听。当前设备物理折叠状态FoldStatus变化时，触发回调函数，返回折叠设备当前折叠状态。 |
* 获取可用区域相关接口

  | API | 说明 |
  | --- | --- |
  | [getAvailableArea()](../harmonyos-references/js-apis-display.md#getavailablearea12) | 获取当前设备屏幕的可用区域，使用Promise异步回调，仅支持电脑设备。 |
  | [on('availableAreaChange')](../harmonyos-references/js-apis-display.md#onavailableareachange12) | 开启当前设备屏幕的可用区域监听。当前设备屏幕有可用区域变化时，触发回调函数，返回可用区域，仅支持电脑设备。 |
  | [display.getDisplayByIdSync()](../harmonyos-references/js-apis-display.md#displaygetdisplaybyidsync12) | 返回displayId对应的display对象。其中包含电脑设备上屏幕的可用区域宽度availableWidth和高度availableHeight。display对应的区域可参考[屏幕规格信息](bpta-mate-book-fold.md#section05491630111312)中的常用接口部分。 |
* 获取折痕区域相关接口

  | API | 说明 |
  | --- | --- |
  | [display.getCurrentFoldCreaseRegion()](../harmonyos-references/js-apis-display.md#displaygetcurrentfoldcreaseregion10) | 在当前显示模式下获取折叠折痕区域。返回[FoldCreaseRegion](../harmonyos-references/js-apis-display.md#foldcreaseregion10)对象，即设备在当前显示模式下的折叠折痕区域。具体返回数据可参考[设备特有能力](bpta-mate-book-fold.md#section1792714518428)表中的FoldCreaseRegion行。 |

## 体验标准

应用体验建议分为功能与兼容性、稳定性、性能、功耗、安全和UX六个部分，详细信息如下所示。

| 名称 | 简介 |
| --- | --- |
| [应用基础功能和兼容性体验建议](../harmonyos-guides/experience-suggestions-compatibility.md) | 应用与OS兼容、应用与设备兼容、应用升级兼容、功能体验相关等。 |
| [应用稳定性体验建议](../harmonyos-guides/experience-suggestions-stability.md) | 长时间运行故障率（崩溃、冻屏等）、长时间运行内存资源异常。 |
| [应用性能体验建议](../harmonyos-guides/performance-experience-suggestions.md) | 时延、帧率流畅体验和内存占用、CPU占用、线程数等资源占用约束。 |
| [应用功耗体验建议](../harmonyos-guides/app-power-experience-standards.md) | 后台任务使用、后台硬件器件资源/软件系统资源占用管控，分布式资源占用等。 |
| [应用安全隐私体验建议](../harmonyos-guides/security-privacy-experience-standards.md) | 基础安全、恶意软件、应用安全、隐私合规等。 |
| [应用UX体验建议](../harmonyos-guides/experience-suggestions-ux.md) | 设计规范、设计约束的符合性，UX精致体验要求等。 |

折叠电脑设备主要在UX上有着特殊的适配体验和建议，下文主要介绍折叠电脑的UX体验建议。

### UX体验建议

**体验设计标准**

折叠电脑以“沉浸无界、灵动流畅、直觉自然”为核心设计理念，深度融合折叠屏的硬件特性与多模态交互需求，针对系统架构和桌面应用在多形态变换、应用适配、交互输入、系统动效表现等方面，为相关设计师和开发人员提供UX设计指南和规范，确保用户在任何场景下均能获得连贯高效的使用体验。UX设计指南可参考[电脑](../design-guides/2in1-0000001777531700.md)和[折叠电脑](../design-guides/foldable-pc-0000002322600098.md)。

**体验设计差异点**

折叠电脑具备折叠状态和展开状态等五种页面布局。在开发应用时，建议采用[响应式布局](bpta-multi-device-responsive-layout.md)，以根据屏幕尺寸自动调整布局，实时响应窗口尺寸变化，确保内容以最优布局展示。响应式布局中最常用的特征是窗口宽度和窗口高宽比，可以将这些参数划分为不同的范围。应用需通过横纵断点来决定不同状态下的页面布局，关于断点的原理和使用示例，可参考[断点](bpta-multi-device-responsive-layout.md#section1532120147301)。

折叠电脑涵盖了从xs到xl的所有横向断点，应用可根据需求设计不同断点对应的页面布局，以实现自适应和响应式布局。在适配折叠电脑页面布局时，为避免出现过多空白区域或内容过于拥挤，影响用户体验，开发者可[设置自由窗口宽度最小值](bpta-multi-device-window-mode.md#section6754152523715)，从而避免xs断点的适配。

页面布局主要实现流程为：

1. 调用[on('windowSizeChange')](../harmonyos-references/js-apis-arkui-uiextension.md#onwindowsizechange)监听自由窗口尺寸的变化。
2. 通过[getWindowWidthBreakpoint()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getwindowwidthbreakpoint13)与[getWindowHeightBreakpoint()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getwindowheightbreakpoint13)获取当前窗口横向断点与纵向断点。
3. 通过状态变量将横纵断点绑定为组件的属性值，当横纵断点变化时组件自动变化，或通过横纵断点变化控制自定义组件的显隐，展示不同断点对应的页面布局。

**应用设计最佳实践**

根据上述UX体验标准和设计差异点，各垂域应用可根据功能和场景特点进行折叠电脑的UX设计；更多垂域设计信息和方案可参考[典型应用案例](../design-guides/foldable-pc-0000002322600098.md#section1124084104516)。

## 工程管理

在折叠电脑设备上运行的应用，需要在module.json5配置文件的module字段中增加支持的deviceTypes工程配置，即需增设"2in1"。更多详情可参考[deviceTypes标签](../harmonyos-guides/module-configuration-file.md#devicetypes标签)。

## 窗口适配

本章节主要介绍折叠电脑在窗口适配上需要适配的内容。

### 适配设备窗口模式

折叠电脑支持全屏、分屏、自由窗口三种窗口模式。

**全屏**

折叠电脑的窗口模式与传统电脑上一致，应用启动时默认应为自由窗口模式，用户可以通过[setWindowLayoutFullScreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)接口，实现界面元素延伸至状态栏和导航区域，从而进入全屏模式，具体适配信息请参考[窗口沉浸式](bpta-multi-device-window-immersive.md)。

**分屏**

折叠电脑支持分屏窗口模式，一般用于两个应用长时间并行使用的场景，例如边看购物攻略边购物的场景；应用也可以主动实现应用内分屏。折叠电脑默认支持上下分屏和左右分屏，分屏窗口参数如下，具体适配信息请参考[分屏窗口模式适配](bpta-multi-device-window-mode.md#section579413164399)。

| 分屏方式 | 默认分屏比例 | 设备形态 | 旋转状态 | 分屏窗口尺寸(px) | 分屏窗口尺寸(vp)向下取整 | 分屏窗口断点 |
| --- | --- | --- | --- | --- | --- | --- |
| 左右分屏 | 1:1 | 半折叠态（唤起全尺寸键盘） | 竖屏 | 1225\*1490 | 680 \* 827 | 横向断点md，纵向断点lg |
| 半折叠态（关闭全尺寸键盘） | 竖屏 | 1225\*1608 | 680 \* 893 | 横向断点md，纵向断点lg |
| 横向展开态 | 横屏/反向横屏 | 1637\*2354 | 909 \* 1307 | 横向断点lg，纵向断点lg |
| 上下分屏 | 1:1 | 竖向展开态 | 竖屏 | 2472\*1578 | 1373 \* 876 | 横向断点lg，纵向断点sm |

说明

折叠电脑在半折叠状态下，只能在上屏使用左右分屏，下屏无法触发分屏模式。

**自由窗口**

折叠电脑的窗口模式与传统电脑上一致，应用启动时默认应为自由窗口模式，而非全屏模式，具体适配信息请参考[自由窗口模式适配](bpta-multi-device-window-mode.md#section151195853214)。

* 跨屏幕移动

  折叠电脑在半折叠状态（关闭全尺寸键盘）下，如果应用位于下屏，开发者可以使用[moveWindowToGlobal()](../harmonyos-references/arkts-apis-window-window.md#movewindowtoglobal15)接口将应用跨屏移动到上屏，从而实现从下屏到上屏的窗口移动。

  ```
  1. let mainWindow =
  2. (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync();
  3. let moveConfiguration: window.MoveConfiguration = {
  4. displayId: 0
  5. };
  6. await mainWindow.moveWindowToGlobal(0, 0, moveConfiguration);
  ```

  [Index.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/HpDemo/entry/src/main/ets/pages/Index.ets#L45-L50)
* 窗口跨屏展示

  在半折叠状态（关闭全尺寸键盘）下，折叠电脑的全屏模式仅支持单屏最大化显示。如果应用内容过多，单屏显示无法完全呈现所有信息。此时，通过跨两个屏幕展示内容，可以更方便地查看所有信息。在这种情况下，可以长按最大化按键，在弹出的菜单中选择进入瀑布流模式，从而实现窗口的跨屏展示。

### 适配窗口显示方向

电脑上的窗口显示方向[Orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)效果始终跟随屏幕显示方向[Orientation](../harmonyos-references/js-apis-display.md#orientation10)的效果，屏幕显示方向由具体产品定义（MateBook Pro只支持横屏，MateBook Fold支持三个方向），具体信息可参考[硬件说明](bpta-mate-book-fold.md#section7335104513501)。

说明

由于[window.setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)设置窗口方向不生效，所以不建议调用[window.setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)设置电脑的窗口方向，也不建议调用[getPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#getpreferredorientation12)获取窗口的显示方向。

### 适配窗口沉浸式

不同设备的定制沉浸式策略，推荐通过窗口模式进行区分，而非依赖设备类型判断。可通过动态识别当前窗口模式（如全屏、分屏、悬浮窗、自由窗口等），针对不同窗口形态实施定制化的沉浸式策略。适配窗口沉浸式请参考[窗口沉浸式](bpta-multi-device-window-immersive.md)。

## 界面开发

折叠电脑的响应式布局符合电脑的标准，详情可参考[电脑布局设计](bpta-pc-guide.md#section583511558587)。

## 交互体验

折叠电脑的交互体验符合电脑的标准，详情可参考[电脑交互体验](bpta-pc-guide.md#section1634505165912)。

说明

需要注意的是，折叠电脑与传统电脑的差异点在于，折叠电脑触屏点击应用内输入框会自动拉起[悬浮键盘](../design-guides/foldable-pc-0000002322600098.md#虚拟键盘)，鼠标点击应用内输入框不会自动拉起虚拟键盘。

## 功能开发

### 适配相机的旋转角度

当折叠电脑处于不同的设备状态时，屏幕的状态也会有所不同。在这种情况下，相机应用预览输出的原始图像需要旋转不同的角度，以确保图像在正确的方向上显示。（预览旋转角度 = 镜头安装角度 + 屏幕显示补偿角度，屏幕显示补偿角度的值与屏幕旋转角度相同。若要自行获取镜头安装角度，可以参考：[getSupportedCameras()](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedcameras)）

在预览时，预览旋转角度与屏幕显示旋转角度（[Display](../harmonyos-references/js-apis-display.md#属性).rotation）相关。若要适配相机的旋转角度，则需要在session调用[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)完成配流后，配置输出流：

1. 通过[display.getDefaultDisplaySync()](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)接口获取[Display](../harmonyos-references/js-apis-display.md#属性)对象并读取其rotation属性值，获得显示设备的屏幕旋转角度。
2. 并根据[相机镜头安装角度](../harmonyos-guides/camera-rotation-term.md#相机镜头安装角度)+[屏幕显示旋转角度](../harmonyos-guides/camera-rotation-term.md#屏幕旋转角度)的值计算[预览旋转角度](../harmonyos-guides/camera-rotation-term.md#预览旋转角度)，可参考[相机硬件信息](bpta-mate-book-fold.md#section1848513375424)查看对应预览旋转角度。
3. 再调用[setPreviewRotation()](../harmonyos-references/arkts-apis-camera-previewoutput.md#getpreviewrotation12)接口，设置图像的预览旋转角度。

具体开发指导可参考[适配相机旋转角度-预览](../harmonyos-guides/camera-rotation-angle-adaptation.md#预览)。

**应用对接预览流二次处理场景下的问题**

若三方应用接口对接的是预览流二次处理，导致系统无法将镜头安装角度补充到预览旋转角度中，导致不能使用系统现有的能力，因此向应用提供两种方案：

* 若应用不需要非镜像成像，建议应用在预览流二次处理后，直接套用系统现有的角度计算方法，应用补偿相机镜头安装角度进行适配。
* 若应用需要非镜像成像，建议应用在预览流二次处理后，自行开发一套角度计算公式，应用自行适配。（非镜像成像场景下，自行适配的性能大大优于补偿相机镜头安装角度的方法）

## 常见问题

### 如何区分MateBook Fold和MateBook Pro

* 页面布局类问题：

  页面布局由窗口形态、宽度和高宽比属性决定，不应区分产品型号或设备类型。例如MateBook Fold的横向展开态布局应该和MateBook Pro布局保持一致，MateBook Fold的其他状态对应横向断点lg的页面布局，应与平板布局保持一致。所以，布局类问题只需判断断点，开发响应式布局即可。详情可参考[断点](bpta-multi-device-responsive-layout.md#section1532120147301)的使用。
* 非页面布局或功能类问题：

  由于MateBook Fold和MateBook Pro的设备类型[deviceType](../harmonyos-references/js-apis-device-info.md#常量)均为2in1，因此，可以通过[isFoldable()](../harmonyos-references/js-apis-display.md#displayisfoldable10)判断是否为可折叠设备，MateBook Fold返回为true，MateBook Pro返回为false。

### 折叠状态变化导致的页面异常

**问题现象**

当折叠电脑的折叠状态发生变化时，可能会导致应用的页面布局出现异常。

**可能原因**

当折叠电脑的折叠状态发生变化时，窗口的大小及横纵断点也会同步发生变化，若应用感知到可用区域的变化，但未对不同断点下的页面布局做处理，可能会导致应用的页面布局不符合需求场景，或出现异常。

**解决措施**

使用获取可用区域的相关接口主动获取可用区域的尺寸或调用[on('windowSizeChange')](../harmonyos-references/js-apis-arkui-uiextension.md#onwindowsizechange)监听自由窗口尺寸的变更，根据获取到的可用区域尺寸判断所属[断点](bpta-multi-device-responsive-layout.md#section1532120147301)，当断点改变时同步调整页面布局，实现页面的[响应式布局](bpta-multi-device-responsive-layout.md)。具体方案可参考[UX体验建议](bpta-mate-book-fold.md#section1756114301170)章节。

### 如何实现跨屏幕移动窗口

**问题现象**

折叠电脑在半折叠状态（关闭全尺寸键盘）下，上下两块屏幕均可独立操作，如果应用位于下屏，开发者想将应用跨屏移动到上屏，应该如何操作？

**解决措施**

可使用[moveWindowToGlobal()](../harmonyos-references/arkts-apis-window-window.md#movewindowtoglobal15)接口实现跨屏幕移动窗口，将窗口从下屏移动至上屏。详情可参考[窗口模式](bpta-mate-book-fold.md#section8155133712178)章节。

### 应用感知可用区域变化不及时

**问题现象**

应用未感知可用区域变化或者感知可用区域变化不及时，但调用moveTo()和resize()调整窗口大小或位置，导致窗口大小或位置异常。

**解决措施**

使用以下三种方法均可解决该问题：

* 使用[display.getDisplayByIdSync()](../harmonyos-references/js-apis-display.md#displaygetdisplaybyidsync12)根据displayId主动获取对应可用区域的[display](../harmonyos-references/js-apis-display.md#display)对象。
* 使用[getAvailableArea()](../harmonyos-references/js-apis-display.md#getavailablearea12)主动获取当前设备屏幕的可用区域。
* 使用[on('availableAreaChange')](../harmonyos-references/js-apis-display.md#onavailableareachange12)开启当前设备屏幕的可用区域监听。

### 相机预览画面旋转异常

**问题现象**

折叠电脑在屏幕旋转后，相机生成的预览画面出现异常。

**可能原因**

折叠电脑在屏幕旋转后，相机预览流未适配旋转后的预览角度，造成预览画面未更新。

**解决措施**

在session调用[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)完成配流后调用，通过[display.getDefaultDisplaySync()](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)获得显示设备的屏幕旋转角度displayRotation，并通过[setPreviewRotation()](../harmonyos-references/arkts-apis-camera-previewoutput.md#getpreviewrotation12)，设置图像的预览旋转角度。具体可参考[功能开发](bpta-mate-book-fold.md#section1110071416153)章节。
