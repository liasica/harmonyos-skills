---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-foldable-guide
title: 双折叠应用开发
breadcrumb: 最佳实践 > 多端设备体验提升 > 手机 > 双折叠应用开发
category: best-practices
scraped_at: 2026-04-29T14:12:56+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:02bde97154a22d9fc0ba6157d5356b675703b70dac65637e9908faeccf8a766b
---

## 概述

### 设备特点

相对于直板机，双折叠有以下明显特点：

* 设备屏幕尺寸可变，具有不同大小和形态的UX界面。
* 具有特殊的折叠状态和交互事件。包含三种状态：折叠态，展开态和悬停态。
  + 展开态：双折叠完全展开后的形态。有更大的屏幕尺寸，可充分显示应用内容。
  + 折叠态：双折叠折叠后的形态。折叠后屏幕尺寸变小。
  + 悬停态：双折叠处于完全展开和折叠的中间状态，可平稳放置。
* 不同折叠状态下，可用的相机，相机的位置会发生变化。

### 主要型号

双折叠目前主要的产品为Mate X双折叠系列，示意图如下。

| 产品名称 | 示意图 |
| --- | --- |
| Mate X系列 |  |

## 硬件说明

本章将介绍双折叠的屏幕方向、屏幕尺寸以及相机硬件参数等信息。

### 屏幕规格信息

以下是双折叠在折叠和展开状态下的硬件参数。

**折叠态屏幕规格信息**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [屏幕旋转角度（rotation）](../harmonyos-references/js-apis-display.md#属性) | 0(0度) | 1(90度) | 2(180度) | 3(270度) |
| 折叠态示意图 |  |  |  |  |
| [屏幕方向Orientation](../harmonyos-references/js-apis-display.md#orientation10) | 竖屏PORTRAIT | 横屏LANDSCAPE | 反向竖屏PORTRAIT\_INVERTED | 反向横屏LANDSCAPE\_INVERTED |
| 屏幕ID | 0 | 0 | 0 | 0 |
| 分辨率(vp) (向下取整) | 345 \* 801 | 801 \* 345 | 345 \* 801 | 801 \* 345 |
| 分辨率(px) | 1080 \* 2504 | 2504 \* 1080 | 1080 \* 2504 | 2504 \* 1080 |
| 横纵断点 | 横向断点sm，纵向断点lg | 横向断点md，纵向断点sm | 横向断点sm，纵向断点lg | 横向断点md，纵向断点sm |

**展开态屏幕规格信息**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [屏幕旋转角度（rotation）](../harmonyos-references/js-apis-display.md#属性) | 0(0度) | 1(90度) | 2(180度) | 3(270度) |
| 展开态示意图 |  |  |  |  |
| [屏幕方向Orientation](../harmonyos-references/js-apis-display.md#orientation10) | 竖屏PORTRAIT | 横屏LANDSCAPE | 反向竖屏PORTRAIT\_INVERTED | 反向横屏LANDSCAPE\_INVERTED |
| 屏幕ID | 0 | 0 | 0 | 0 |
| 分辨率(vp) (向下取整) | 711 \* 798 (Mate X5) | 798 \* 711 (Mate X5) | 711 \* 798 (Mate X5) | 798 \* 711 (Mate X5) |
| 分辨率(px) | 2224 \* 2496 (Mate X5) | 2496 \* 2224 (Mate X5) | 2224 \* 2496 (Mate X5) | 2496 \* 2224 (Mate X5) |
| 横纵断点 | 横向断点md，纵向断点md | 横向断点md，纵向断点md | 横向断点md，纵向断点md | 横向断点md，纵向断点md |

说明

* 上述Mate X系列屏幕尺寸参数以Mate X5为例展示属性，系列其它产品可通过[display](../harmonyos-references/js-apis-display.md)的[getDefaultDisplaySync()](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)方法获取设备屏幕分辨率(px)，通过[px2vp()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#px2vp12)方法得到分辨率的vp值。
* 悬停态在不同旋转角度下的硬件参数和展开态一致，适配悬停态可参考[折叠屏悬停态](bpta-folded-hover.md)。
* 设备屏幕和窗口方向详细信息可参考[窗口方向](bpta-multi-device-window-direction.md)。

### 其他硬件信息

**相机硬件信息**

相机有默认的[相机镜头安装角度](../harmonyos-guides/camera-rotation-term.md#相机镜头安装角度)，在使用时需要考虑镜头角度和设备的旋转角度，具体定义可参考[预览旋转角度](../harmonyos-guides/camera-rotation-term.md#预览旋转角度)。双折叠相机前置和后置镜头角度以及需要设置的预览流旋转角度如下，折叠态和展开态下的相机参数一致。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [屏幕旋转角度（rotation）](../harmonyos-references/js-apis-display.md#属性) | 0(0度) | 1(90度) | 2(180度) | 3(270度) |
| 示意图 |  |  |  |  |
| 后置相机镜头角度 | 90度 | 90度 | 90度 | 90度 |
| 后置相机拍摄预览流旋转角度 | 90度 | 180度 | 270度 | 0度 |
| 前置相机镜头角度 | 270度 | 270度 | 270度 | 270度 |
| 前置相机拍摄预览流旋转角度 | 270度 | 0度 | 90度 | 180度 |

说明

* 双折叠后置相机安装角度为90°，前置相机安装角度为270°，和折叠状态无关。可通过[CameraDevice](../harmonyos-references/arkts-apis-camera-i.md#cameradevice)接口获取相机安装角度cameraOrientation。
* 更多相机硬件差异和开发详情可参考[相机硬件差异](bpta-multi-device-camera.md)。

### 设备特有能力

双折叠设备有着独特的折叠能力，在不同的折叠状态下有着不同的折叠属性，Mate X系列产品折叠状态和属性如下。

|  | 折叠态 | 悬停态 | 展开态 |
| --- | --- | --- | --- |
| 效果图 |  |  |  |
| [isFoldable](../harmonyos-references/js-apis-display.md#displayisfoldable10) | true | | |
| [FoldStatus](../harmonyos-references/js-apis-display.md#foldstatus10) | FOLD\_STATUS\_FOLDED | FOLD\_STATUS\_HALF\_FOLDED | FOLD\_STATUS\_EXPANDED |
| [FoldDisplayMode](../harmonyos-references/js-apis-display.md#folddisplaymode10) | FOLD\_DISPLAY\_MODE\_MAIN | FOLD\_DISPLAY\_MODE\_FULL | FOLD\_DISPLAY\_MODE\_FULL |

## 体验标准

应用体验建议分为功能与兼容性、稳定性、性能、功耗、安全和UX六个部分，详细信息如下所示。

| 名称 | 简介 |
| --- | --- |
| [应用基础功能和兼容性体验建议](../harmonyos-guides/experience-suggestions-compatibility.md) | 应用与OS兼容、应用与设备兼容、应用升级兼容、功能体验相关等 |
| [应用稳定性体验建议](../harmonyos-guides/experience-suggestions-stability.md) | 长时间运行故障率（崩溃、冻屏等）、长时间运行内存资源异常 |
| [应用性能体验建议](../harmonyos-guides/performance-experience-suggestions.md) | 时延、帧率流畅体验和内存占用、CPU占用、线程数等资源占用约束 |
| [应用功耗体验建议](../harmonyos-guides/app-power-experience-standards.md) | 后台任务使用、后台硬件器件资源/软件系统资源占用管控，分布式资源占用等 |
| [应用安全隐私体验建议](../harmonyos-guides/security-privacy-experience-standards.md) | 基础安全、恶意软件、应用安全、隐私合规等 |
| [应用UX体验建议](../harmonyos-guides/experience-suggestions-ux.md) | 设计规范、设计约束的符合性，UX精致体验要求等 |

双折叠设备主要在UX上有着特殊的适配体验和建议，下文主要介绍双折叠的UX体验建议。

### UX体验建议

**体验设计标准**

双折叠设备的三种形态分别为折叠态、展开态和悬停态。折叠态便于随身携带和单手操作，适合移动场景下的便捷使用；展开态能够充分展示应用内容，适合多任务处理和沉浸式体验；悬停态可稳定放置，让用户解放双手。详细的UX设计标准可参考[双折叠设计指南](../design-guides/foldable-0000002352875141.md)和[折叠屏应用UX体验标准](../design-guides/ux-guidelines-foldable-screen-0000001807866557.md)。双折叠的主要体验标准如下：

* 响应式布局：随着屏幕状态的变化，界面中应用内容进行适配变化，常见的响应式布局的表现形式为：相对拉伸、相对缩放、延伸布局、挪移布局、重复布局、瀑布布局等。
* 多窗口交互：双折叠设备因其大屏特性，具备多窗口适配的优势，例如分屏和悬浮窗。
* 开合连续性：应用在设备折叠/展开后不应出现操作步骤增加，操作更复杂等体验下降的情况。例如：页面切换到其他页面、页面滚动位置发生偏移、输入内容丢失、图片模糊、播放进度变化。
* 开合流畅：设备在折叠/展开时，变化过程有连续动效，而不是硬切换。
* 悬停态适配：长视频、短视频、直播、通话、会议、拍摄类应用需针对双折叠的悬停态进行单独适配。下半屏区域内可放置交互操作，上半屏区域内进行信息显示，呈现浏览型内容。交互型控件，例如弹出框、半模态，在下半屏显示；跟随上下文的控件，例如菜单，跟随触发元素所在侧的屏幕显示。
* 折痕避让：悬停态时，中间弯折区域难以操作且显示内容会变形。长视频、短视频、直播、通话、会议、拍摄类应用需针对折痕区域进行避让适配。

说明

不同尺寸屏幕下的页面布局应通过[断点](bpta-multi-device-responsive-layout.md#section1532120147301)进行划分和设计实现，页面布局的判断条件不推荐使用[deviceType](../harmonyos-references/js-apis-resource-manager.md#devicetype)、[isFoldable](../harmonyos-references/js-apis-display.md#displayisfoldable10)、[foldStatus](../harmonyos-references/js-apis-display.md#foldstatus10)接口，否则会导致不同屏幕尺寸双折叠下的布局混乱问题。

**体验设计差异点**

双折叠设备主要设计差异点体现在折叠状态变化上，主要为开合连续和悬停态适配以及页面的响应式布局。开合连续需要确保应用状态在开合前后状态一致，可参考[适配应用界面开合连续](bpta-foldable-guide.md#section186893019118)章节。悬停态需对上下半屏进行合理的布局和折痕避让，可参考[适配设备悬停态](bpta-foldable-guide.md#section1223242181220)章节。双折叠设备的显示尺寸会随着设备的开合而变化，应用能够响应这些变化自动调整布局，可参考[响应式布局](bpta-multi-device-responsive-layout.md)。

**应用设计最佳实践**

根据上述UX体验标准和设计差异点，各垂域应用可根据功能和场景特点进行双折叠UX设计，例如影音娱乐类应用主要体验为沉浸式视频播放和互动，需要考虑不同折叠状态的沉浸式视频播放布局和交互设计。更多垂域设计信息和方案可参考[应用设计最佳实践](../design-guides/practices-overview-0000001746498066.md)。

## 工程管理

在双折叠设备上运行的应用，需要在module.json5配置文件的module字段中包含"phone"，新建工程默认包含该字段。更多详情可参考[deviceTypes标签](../harmonyos-guides/module-configuration-file.md#devicetypes标签)。

## 窗口适配

### 适配设备窗口模式

当前双折叠设备支持的窗口模式有全屏窗口模式、分屏窗口模式以及悬浮窗口模式，各模式的详细信息见[窗口模式](bpta-multi-device-window-mode.md)。

说明

分屏、悬浮窗窗口模式均默认已配置，开发者可以调整在module.json5配置文件中[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)下的supportWindowMode属性，设置需要的窗口能力。

双折叠支持分屏窗口模式和悬浮窗口模式。分屏一般用于两个应用长时间并行使用的场景，例如边看购物攻略边购物的场景；应用也可以主动实现应用内分屏。双折叠支持上下分屏和左右分屏，双折叠分屏窗口参数如下（以Mate X5为例）。具体适配方案和代码可见[分屏窗口模式适配](bpta-multi-device-window-mode.md#section579413164399)。

**折叠态分屏窗口参数**

| 分屏方式 | 分屏比例 | 旋转状态 | 分屏窗口尺寸(vp) | 分屏窗口断点 |
| --- | --- | --- | --- | --- |
| 左右分屏 | 1:1 | 横屏 | 378 \* 345 | 横向断点sm，纵向断点md |
| 上下分屏 | 1:1 | 竖屏 | 345 \* 378 | 横向断点sm，纵向断点md |
| 2:1 | 345 \* 504 | 横向断点sm，纵向断点lg |
| 1:2 | 345 \* 252 | 横向断点sm，纵向断点sm |

**展开态分屏窗口参数**

| 分屏方式 | 分屏比例 | 旋转状态 | 分屏窗口尺寸(vp) | 分屏窗口断点 |
| --- | --- | --- | --- | --- |
| 左右分屏 | 1:1 | 竖屏 | 352 \* 798 | 横向断点sm，纵向断点lg |
| 横屏 | 395 \* 711 | 横向断点sm，纵向断点lg |
| 上下分屏 | 1:1 | 竖屏 | 711 \* 376 | 横向断点md，纵向断点sm |
| 横屏 | 798 \* 333 | 横向断点md，纵向断点sm |

说明

* 折叠态下，左右分屏仅支持横屏，上下分屏仅支持竖屏。左右分屏仅支持1:1分屏。
* 展开态下，设备仅支持1:1分屏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/7a_Yzm_LQ8WTSkTGVRvOZg/zh-cn_image_0000002419627141.png?HW-CC-KV=V1&HW-CC-Date=20260429T061251Z&HW-CC-Expire=86400&HW-CC-Sign=5D423142BE747FD0C06D4147DD8A779D6940F9E47373FBF173FDBF66FD468D61 "点击放大")

悬浮窗一般用于阅读新闻资讯、购物等场景，应用可根据需要在双折叠上实现竖向悬浮窗和横向悬浮窗，双折叠悬浮窗口参数如下（以Mate X5为例）。应用界面适配悬浮窗可参考[悬浮窗口模式适配](bpta-multi-device-window-mode.md#section8433735123611)。

**折叠态悬浮窗参数**

| 悬浮窗类型 | 悬浮窗口尺寸(vp) | 悬浮窗口断点 |
| --- | --- | --- |
| 纵向悬浮窗 | 345 \* 567 | 横向断点sm，纵向断点lg |
| 横向悬浮窗 | 345 \* 194 | 横向断点sm，纵向断点sm |

**展开态悬浮窗参数**

| 悬浮窗类型 | 悬浮窗口尺寸(vp) | 悬浮窗口断点 |
| --- | --- | --- |
| 纵向悬浮窗 | 345 \* 648 | 横向断点sm，纵向断点lg |
| 横向悬浮窗 | 345 \* 194 | 横向断点sm，纵向断点sm |

说明

设备在不同旋转状态下悬浮窗参数一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/mOxj_kr2SDiPefLmft4kDQ/zh-cn_image_0000002386067908.png?HW-CC-KV=V1&HW-CC-Date=20260429T061251Z&HW-CC-Expire=86400&HW-CC-Sign=3CBCDA53B842E0187231A8D37EA2A835ECBF5AA9D2B5CF66C0D6751AA70A3E4E "点击放大")

### 适配设备显示方向

可以通过设置窗口旋转策略（[orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)）的方式控制应用的显示方向。窗口旋转策略（orientation）与屏幕旋转角度的关系请参考[window.orientation与display.rotation的关系](bpta-multi-device-window-direction.md#section20201743171811)。双折叠开发的横竖屏旋转策略以及适配方案可参考[窗口方向](bpta-multi-device-window-direction.md)。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [屏幕旋转角度（rotation）](../harmonyos-references/js-apis-display.md#属性) | 0(0度) | 1(90度) | 2(180度) | 3(270度) |
| 旋转状态 |  |  |  |  |
| 默认窗口旋转策略(Orientation) | UNSPECIFIED  未定义方向模式，由系统判定。 | | | |
| 表现形式 | PORTRAIT  竖屏显示 | | | |

说明

* 表格中的参数表示[屏幕属性](../harmonyos-references/js-apis-display.md#属性)中顺时针旋转角度（rotation）对应的窗口旋转策略。

建议双折叠展开态界面支持横竖屏旋转，展开态界面有足够的空间来适应变化前后的横竖屏布局，无论横屏还是竖屏，窗口均有足够的显示区域，具体适配逻辑可参考[为应用配置旋转策略](bpta-multi-device-window-direction.md#section714419371037)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/8ZliRNyARIKgN0H9-M47Nw/zh-cn_image_0000002419746985.png?HW-CC-KV=V1&HW-CC-Date=20260429T061251Z&HW-CC-Expire=86400&HW-CC-Sign=E26588CBEFDE87653F3D4BE84217D5656D09FB0EA78DC23735C7E22F8995D61A "点击放大")

双折叠推荐的旋转逻辑如下。

| 折叠状态 | 窗口全屏时尺寸（vp） | 是否支持横竖屏旋转（以348vp为阈值） | 系统是否默认支持横竖屏旋转 |
| --- | --- | --- | --- |
| 折叠态 | 345 \* 801 | 否 | 否 |
| 展开态 | 711 \* 798 | 是 | 否 |

### 适配设备沉浸式

不同窗口模式和窗口方向下的沉浸式实现，参考窗口沉浸式的[实现沉浸式效果](bpta-multi-device-window-immersive.md#section180431120426)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/MWYs9J9cQmm324roiEf8Vw/zh-cn_image_0000002386227816.png?HW-CC-KV=V1&HW-CC-Date=20260429T061251Z&HW-CC-Expire=86400&HW-CC-Sign=20D3BD1C4B4F80310A090FD48E5426FE261E41117BCD48D0FAD3C442A43BC335 "点击放大")

## 界面开发

### 典型布局场景

双折叠上典型的响应式布局方式有分栏布局、重复布局、挪移布局和缩进布局。应用可以利用不同的UI组件和断点来实现多样的布局，从而打造丰富的布局场景。典型布局场景的实现方式可参考[页面布局场景](bpta-multi-device-page-layout.md)。复杂的分栏布局，例如单双栏形态变化时的路由跳转，可参考[分栏布局](bpta-multi-device-page-layout.md#section11897247142110)。

### 大方形屏适配建议

双折叠展开态纵向断点为md，屏幕比例近似1:1，呈现出对称且均衡的视觉效果，横向分辨率超过600vp，是典型的大方形屏。大方形屏非常适合多任务处理、内容分屏展示以及创作类应用，能够显著提升用户的操作效率与交互体验。大方形屏的布局设计与实现可参考[大方形屏](bpta-multi-device-screen-layout.md#section12921201325714)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/VlE-e4WeRZqAgf6QR1v1og/zh-cn_image_0000002386227852.png?HW-CC-KV=V1&HW-CC-Date=20260429T061251Z&HW-CC-Expire=86400&HW-CC-Sign=F41F9F054C5E7B937977E0D23A251324EFAE19532DB766B0E8D1E8EFC3BC7A93 "点击放大")

### 适配设备悬停态

双折叠的悬停态可以在桌面平稳放置，实现免手持体验，常用于视频通话、播放视频、拍照和听歌等不需要频繁交互的场景。这种状态下，应用需要对中间折痕区域进行避让，并且对上下两个界面进行悬停适配，重新布局。悬停态的实现方案可参考[折叠屏悬停态](bpta-folded-hover.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/yjlSyXOQQrmnAnRkWCO6Zg/zh-cn_image_0000002419627209.png?HW-CC-KV=V1&HW-CC-Date=20260429T061251Z&HW-CC-Expire=86400&HW-CC-Sign=DBD07E1ABC49A970E223D7B5E9F7BE155D866AC75607C8FFA988E1C1439706B8 "点击放大")

### 适配应用界面开合连续

开合连续指应用在各种屏幕和窗口状态间切换时页面内容连续，切换之前的任务和相关状态能保存、延续，或能够快速恢复，给用户提供连续的体验。主要标准有页面不发生改变和焦点不发生偏移，具体可参考[开合接续](../design-guides/foldable-0000002352875141.md#section5560057912)。应用页面和功能相关的开合连续能力建议使用断点实现，并通过[window.on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)接口监听。

display提供了折叠状态监听的接口，这些接口建议使用在某些应用功能的适配上，比如[适配设备悬停态](bpta-foldable-guide.md#section1223242181220)、[设置多设备上相机预览画面比例](bpta-multi-device-camera.md#section882216138497)，但不能用于页面布局的开合连续适配。

说明

* **不推荐使用折叠状态监听接口实现页面布局的响应式布局和接续，避免在窗口变化但折叠状态未改变的场景下布局未能及时调整，出现页面异常。**
* 在双折叠开合过程中，各种监听回调的触发时序如下。
  + 展开态->折叠态：foldStatusChange(悬停态) -> foldStatusChange(折叠态) -> foldDisplayModeChange -> windowSizeChange
  + 折叠态->展开态：foldStatusChange(悬停态) -> foldDisplayModeChange -> windowSizeChange -> foldStatusChange(展开态)

常见的接口汇总如下。

| API | 说明 |
| --- | --- |
| [getWindowWidthBreakpoint](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getwindowwidthbreakpoint13) | 获取当前实例所在窗口的宽度断点 |
| [getWindowHeightBreakpoint](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getwindowheightbreakpoint13) | 获取当前实例所在窗口的高度断点 |
| [window.on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7) | 开启窗口尺寸变化的监听 |
| [window.off('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#offwindowsizechange7) | 关闭窗口尺寸变化的监听 |
| [display.isFoldable](../harmonyos-references/js-apis-display.md#displayisfoldable10) | 检查设备是否可折叠 |
| [display.getCurrentFoldCreaseRegion](../harmonyos-references/js-apis-display.md#displaygetcurrentfoldcreaseregion10) | 在当前模式下获取折叠折痕区域 |
| [display.getFoldStatus](../harmonyos-references/js-apis-display.md#displaygetfoldstatus10) | 获取可折叠设备的当前折叠状态 |
| [display.getFoldDisplayMode](../harmonyos-references/js-apis-display.md#displaygetfolddisplaymode10) | 获取可折叠设备的显示模式 |
| [display.on('foldStatusChange')](../harmonyos-references/js-apis-display.md#displayonfoldstatuschange10) | 开启折叠设备折叠状态变化的监听 |
| [display.off('foldStatusChange')](../harmonyos-references/js-apis-display.md#displayofffoldstatuschange10) | 关闭折叠设备折叠状态变化的监听 |
| [display.on('foldDisplayModeChange')](../harmonyos-references/js-apis-display.md#displayonfolddisplaymodechange10) | 开启折叠设备屏幕显示模式变化的监听 |
| [display.off('foldDisplayModeChange')](../harmonyos-references/js-apis-display.md#displayofffolddisplaymodechange10) | 关闭折叠设备屏幕显示模式变化的监听 |

**开合页面后刷新UI布局效果**

双折叠开合状态变化时会伴随着窗口尺寸的变化，可通过注册on('windowSizeChange')事件监听器来捕获窗口尺寸变化，在回调函数中重新计算当前断点，通过断点变化更新UI布局，确保界面始终与当前窗口尺寸保持同步。这一机制能够有效处理设备展开/折叠、分屏模式切换以及屏幕旋转等多种场景下的界面适配需求，为用户提供流畅的双折叠使用体验。

```
1. private onWindowSizeChange: (windowSize: window.Size) => void = (windowSize: window.Size) => {
2. AppStorage.setOrCreate('currentWidthBreakpoint', this.uiContext!.getWindowWidthBreakpoint());
3. AppStorage.setOrCreate('currentHeightBreakpoint', this.uiContext!.getWindowHeightBreakpoint());
4. };
```

[EntryAbility.ets](https://gitcode.com/harmonyos_samples/SmallWindowScene/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L37-L40)

触发断点变化回调后，需要通过断点更新UI布局实现双折叠开合前后布局连续，具体可参考[通过断点刷新UI](bpta-multi-device-responsive-layout.md#section175001836203617)。

**可滑动组件的阅读焦点不偏移**

对于双折叠开合连续使用场景，应用在完成折叠状态切换操作后，需确保[List](../harmonyos-references/ts-container-list.md)组件、[WaterFlow](../harmonyos-references/ts-container-waterflow.md)组件以及 [Scroll](../harmonyos-references/ts-container-scroll.md)组件等可滑动组件的阅读焦点不发生偏移。目前，这些组件依据折叠状态改变前的滑动偏移量来维持阅读焦点位置，然而，由于折叠状态切换前后，组件内部高度可能发生变化，即便滑动相同的偏移量，也难以达成阅读焦点不偏移的目标。因此，有必要针对上述可滑动组件采取特殊处理措施。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/bmGx1myPTv6cw73AMvk_wA/zh-cn_image_0000002386067952.png?HW-CC-KV=V1&HW-CC-Date=20260429T061251Z&HW-CC-Expire=86400&HW-CC-Sign=BD770F84891EAEBBC64D0A22B18D31103724AD5CDE72003FD4ECC2C2AB0A0809 "点击放大")

* List组件

  List组件可以通过[onScrollIndex()](../harmonyos-references/ts-container-list.md#onscrollindex)来监听子组件划入或划出List显示区域，可以获取到当前处于List显示区域头部的索引值。获取到头部索引值后，在监听双折叠状态变化的回调中，利用Scroller控制器提供的[scrollToIndex()](../harmonyos-references/ts-container-scroll.md#scrolltoindex)方法，使列表滑动到指定索引值的位置，从而保证阅读焦点不偏移，示例如下。

  在aboutToAppear中注册监听索引值变化的回调，触发刷新。

  ```
  1. aboutToAppear(): void {
  2. let callback: Callback<display.FoldStatus> = (data: display.FoldStatus) => {
  3. if (data === display.FoldStatus.FOLD_STATUS_EXPANDED) {
  4. this.barOpacity = 1;
  5. this.listScroller.scrollToIndex(this.currentIndex);
  6. } else if (data === display.FoldStatus.FOLD_STATUS_FOLDED) {
  7. this.listScroller.scrollToIndex(this.currentIndex);
  8. }
  9. hilog.info(0x0000, TAG, 'Listening enabled. Data: ' + JSON.stringify(data));
  10. };
  11. try {
  12. display.on('foldStatusChange', callback);
  13. } catch (error) {
  14. let err = error as BusinessError;
  15. hilog.error(0x0000, 'TestLog', `Failed to update fold status. Code: ${err.code}, message: ${err.message}`);
  16. }
  17. }
  ```

  [Index.ets](https://gitcode.com/harmonyos_samples/SmallWindowScene/blob/master/entry/src/main/ets/pages/Index.ets#L52-L69)

  在List组件scrollToIndex()方法中更新索引值。

  ```
  1. List({
  2. space: CommonConstants.LIST_SPACE[0],
  3. scroller: this.listScroller,
  4. }) {
  5. // ...
  6. }
  7. .onScrollIndex((start: number) => {
  8. this.currentIndex = start;
  9. })
  ```

  [Index.ets](https://gitcode.com/harmonyos_samples/SmallWindowScene/blob/master/entry/src/main/ets/pages/Index.ets#L152-L200)
* WaterFlow组件

  WaterFlow组件需要根据场景进行特殊的判断，若双折叠状态改变前后，WaterFlow未改变展示列数，则系统默认使用改变前的滑动偏移量，以确保阅读焦点不发生偏移；若双折叠状态改变前后，WaterFlow改变了列数，则需要将[WaterFlowLayoutMode](../harmonyos-references/ts-container-waterflow.md#waterflowlayoutmode12枚举说明)改为SLIDING\_WINDOW。修改后，系统将根据WaterFlow可展示区域的最小索引值，自动调整以确保阅读焦点不偏移。

  ```
  1. WaterFlow({ layoutMode: WaterFlowLayoutMode.SLIDING_WINDOW }) {
  2. LazyForEach(this.dataSource, (item: number) => {
  3. FlowItem() {
  4. Column() {
  5. Text('Num' + item).fontSize(12).height('16')
  6. }
  7. }
  8. .onAppear(() => {
  9. if (item + 20 == this.dataSource.totalCount()) {
  10. for (let i = 0; i < 100; i++) {
  11. this.dataSource.addLastItem();
  12. }
  13. }
  14. })
  15. .width('100%')
  16. .height(this.itemHeightArray[item % 100])
  17. .backgroundColor(this.colors[item % 5])
  18. }, (item: string) => item)
  19. }
  20. .columnsTemplate(this.waterFlowColumnsTemplate)
  ```

  [WaterFlowView.ets](https://gitcode.com/harmonyos_samples/SmallWindowScene/blob/master/entry/src/main/ets/views/WaterFlowView.ets#L82-L101)
* Scroll组件

  Scroll组件会根据折叠前的滑动偏移量来保证阅读焦点不偏移，但Scroll组件无法做到List组件一样，根据列表项索引来保证阅读焦点不偏移。Scroll组件提供了[scrollBy()](../harmonyos-references/ts-container-scroll.md#scrollby9)方法，以实现滑动指定距离。开发者需要根据具体的业务场景，计算出需要滑动的距离，再通过scrollBy()方法，自行适配Scroll组件的阅读焦点不偏移。

## 交互适配

双折叠的交互方式为触控屏，常见的操作有点击、双击、长按、拖拽、滑动等，应用可根据这些操作进行功能适配，详情可参考[多设备交互](bpta-multi-interaction.md)。

## 功能开发

### 相机开发

对于需要实现相机页面和功能的应用，在双折叠上需要对不同的折叠状态、屏幕尺寸，相机镜头进行适配。双折叠相机开发详情请参考[相机硬件差异](bpta-multi-device-camera.md)，主要考虑的有以下几点。

* 相机页面布局：通过横向断点区分和实现不同形态屏幕的页面布局，可参考[通过断点实现多套页面布局](bpta-multi-device-camera.md#section181143569262)。
* 相机设备选择：根据相机的状态和位置，选择当前形态下可用的相机，可参考[选择相机设备](bpta-multi-device-camera.md#section13854163154917)。
* 相机预览流配置：配置预览流分辨率，避免出现压缩、拉伸、异常旋转的问题，可参考[设置多设备上相机预览画面比例](bpta-multi-device-camera.md#section882216138497)。
* 拍照旋转适配：在横竖屏拍照场景下，正确获取并设置旋转角度，需确保图片始终正向显示，可参考[设置拍照旋转角度](bpta-multi-device-camera.md#section0752024124911)。
* 悬停态相机页面：对悬停态进行UI重布局和折痕避让，可参考[实现悬停态相机页面](bpta-multi-device-camera.md#section50639679)。

| 设备形态 | 折叠态 | 悬停态 | 展开态（竖向） | 展开态（横向） |
| --- | --- | --- | --- | --- |
| 效果图 |  |  |  |  |

双折叠上开发相机功能的一些常见问题和解决方案可参考文章相机硬件差异的[常见问题](bpta-multi-device-camera.md#section1684283074912)。

## 典型业务案例

### 购物比价

购物比价类应用可以在双折叠上展示更丰富的信息，例如可以使用分屏能力同时浏览两个商品的内容，方便用户进行对比。详细开发方案可参考[多设备购物比价界面](multi-shopping-price-comparison.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/nICOMkjISrq1mOThbFDsBA/zh-cn_image_0000002419747037.png?HW-CC-KV=V1&HW-CC-Date=20260429T061251Z&HW-CC-Expire=86400&HW-CC-Sign=852C8835E130B291C1CD8FEE2DA284E2D692B3AE19F3E6EB309C35C2BFB22D80 "点击放大")

更多垂域案例可参考[多设备界面开发案例](bpta-multi-device-ui-development.md)。

## 小折叠应用开发

### 概述

相对于直板机，小折叠有以下特点：

* 具有特殊的折叠状态和交互事件。包含三种状态：折叠态，展开态和悬停态。
  + 展开态：小折叠完全展开后的形态。形态为直板机。
  + 折叠态：小折叠折叠后的形态。折叠后屏幕尺寸很小，有一定的交互空间。
  + 悬停态：小折叠处于完全展开和折叠的中间状态，可平稳放置。

小折叠目前共有两款产品，Pocket系列和Nova Flip系列，示意图如下。

| 产品名称 | 示意图 |
| --- | --- |
| Pocket系列 |  |
| Nova Flip系列 |  |

### 差异化适配要点

**折叠属性**

以Pocket系列产品为例，小折叠状态属性如下。

|  | 折叠态 | 悬停态 | 展开态 |
| --- | --- | --- | --- |
| 效果图 |  |  |  |
| [isFoldable](../harmonyos-references/js-apis-display.md#displayisfoldable10) | false | | |
| [FoldStatus](../harmonyos-references/js-apis-display.md#foldstatus10) | FOLD\_STATUS\_FOLDED | FOLD\_STATUS\_HALF\_FOLDED | FOLD\_STATUS\_EXPANDED |
| [FoldDisplayMode](../harmonyos-references/js-apis-display.md#folddisplaymode10) | FOLD\_DISPLAY\_MODE\_SUB | FOLD\_DISPLAY\_MODE\_MAIN | FOLD\_DISPLAY\_MODE\_MAIN |

**界面开发**

小折叠在展开态下呈现直板机形态，其基础布局设计与直板机保持一致，竖屏时注重单手操作与内容垂直浏览，横屏时则充分利用宽屏优势，通过分栏或左右布局提升信息密度与交互效率：

* 竖屏：布局设计以单手操作便捷性与内容垂直浏览为核心。界面通常采用单栏布局，内容按优先级自上而下垂直堆叠；导航栏建议置于屏幕底部（底部页签栏），以符合用户单手拇指的操作热区；图文组合多采用上下结构，确保信息流的连贯性与沉浸感。
* 横屏：布局设计侧重于利用宽屏空间提升信息密度与交互效率。界面推荐采用分栏布局（如左右双栏）或重复布局（多列网格），充分利用横向视野展示更多内容；图文组合建议采用挪移布局（左右排列），将图片与文字并排展示，避免横向空间的浪费，从而提供更高效的生产力体验或更沉浸的影音视野。

具体的布局设计和实现，可参考[直板机竖屏](bpta-multi-device-screen-layout.md#section1919517165814)和[直板机横屏](bpta-multi-device-screen-layout.md#section8373105265815)。

说明

小折叠折叠态外屏屏幕较小，外屏的开发与ArtTS卡片开发一致，实现可参考[ArkTS卡片开发](../harmonyos-guides/arkts-ui.md)，注意需要把form\_config.json配置文件中的supportShapes字段设置为“circle”。卡片的设计标准可参考[服务卡片](../design-guides/system-features-service-widget-0000002087671904.md)。

## 常见问题

### 展开态下应用启动页面未铺满屏幕或出现异常布局

**问题现象**

在双折叠展开态启动应用时，应用的启动页面未铺满整个屏幕，出现白屏区域或者启动页面被截断。

**可能原因**

应用未配置增强启动页。

**解决方案**

应用需要[配置增强启动页](../harmonyos-guides/launch-page-config.md#配置增强启动页)，配置后启动页面中的背景、图片和图标等资源能根据窗口大小自适应填充，保证启动页面在不同设备形态上正常显示，配置中各标签的说明可参考[startWindow标签](../harmonyos-guides/module-configuration-file.md#startwindow标签)。

### 如何判断不同类型的双折叠

**问题现象**

咨询如何判断不同型号的双折叠。

**解决方案**

禁止通过判断具体设备类型实现应用页面布局和功能，页面布局在不同设备上的适配推荐使用[断点](bpta-multi-device-responsive-layout.md#section1532120147301)和[window.on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)实现，具体见[如何实现不同折叠状态下的页面布局](bpta-foldable-guide.md#section241814335915)；一些特殊的功能例如悬停态、相机等使用折叠状态监听来实现，但不能用于页面布局的适配。

### 如何实现不同折叠状态下的页面布局

**问题现象**

应用页面布局在不同折叠状态下不知道如何适配或适配有问题。

**解决方案**

推荐使用断点进行页面布局的适配，根据不同断点下页面布局的UX设计，开发不同断点下的页面布局，通过[window.on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)监听页面的断点变化，即可实现不同折叠状态下的页面布局适配，详细开发方案参考[断点](bpta-multi-device-responsive-layout.md#section1532120147301)的开发案例。
