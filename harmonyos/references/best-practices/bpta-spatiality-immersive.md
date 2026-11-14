---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-spatiality-immersive
title: 沉浸光感
breadcrumb: 最佳实践 > 技术创新 > 空间化 > 沉浸光感
category: best-practices
scraped_at: 2026-11-14T08:54:04+08:00
doc_updated_at: 2026-11-10
content_hash: sha256:41909c784e8c8d6f45685b6b83e19b701577bf4baedfc3794130a0542e1c317a
---

## 概述

空间化（Spatial UI）是HarmonyOS系统在视觉体验层面的一次重要升级。它通过沉浸光感材质与悬浮组件两大核心能力，让应用界面呈现出精致、通透、有层次的视觉效果，同时配合[智感握姿](bpta-smart-reach.md)等智能交互，提升UX的精致程度。

[沉浸光感](../harmonyos-guides/arkts-immersive-light-sense.md)是空间化视觉的基石，为组件（标题栏、导航栏、工具栏等）提供三种视觉效果：内容相关的毛玻璃模糊、按压状态的弹性光效反馈、以及滑动过程的透明度渐变。悬浮组件则是空间化的交互载体，底部导航栏从传统的贴底色块变为悬浮圆角胶囊，配合MiniBar折叠展开、智感握姿左右跟随等能力，让交互更加自然流畅。空间化的效果如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/sQFNfUDxSS2q45aqAV9_3w/zh-cn_image_0000002594475428.png?HW-CC-KV=V1&HW-CC-Date=20261114T005402Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E6D90DA2253A10B55870F6FCF4BC814CB817F6BA9D4684165E88F861E8CB2E6 "点击放大")

本文将从沉浸光感的基础概念切入，重点围绕首眼沉浸光感、自适应悬浮导航与智感握姿智能交互三大应用场景，系统介绍如何在HarmonyOS应用中快速接入沉浸光感能力。

## 沉浸光感介绍

### 什么是沉浸光感

沉浸光感是一套高品质视觉与动效体系。通过模拟真实物理光照模型，在UI组件内部产生细腻的光晕、反射和折射效果，从而打造出通透玻璃质感，提升应用的视觉沉浸感和交互反馈的真实度。它赋予组件以下视觉特性：

| **特性** | **说明** |
| --- | --- |
| **通透材质** | 组件背景呈现毛玻璃效果，内容可透过组件隐约可见，营造层次感与通透感。 |
| **渐变模糊** | 标题栏随页面滑动产生渐变模糊效果，从透明到模糊平滑过渡。 |
| **按压弹性反馈** | 用户按压组件时产生弹性缩放动画，提供触觉层面的反馈。 |
| **按压点光源** | 按压时在触点位置产生光晕扩散效果，增强交互的视觉反馈。 |
| **材质流光** | 组件表面呈现微妙的流光效果，随视角和状态变化，提升精致感。 |
| **智能反色** | 当底层内容颜色与组件前景色接近时，自动调整前景色以保证可读性。 |

沉浸光感视觉示意图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/wMwY_9OzSsaU_IiD6GVzsQ/zh-cn_image_0000002594053198.png?HW-CC-KV=V1&HW-CC-Date=20261114T005402Z&HW-CC-Expire=31536000000&HW-CC-Sign=535E66FC06600420138E0CBF1B14E209B7E4AB3BCC96054C88A0BA8E6E1108E3 "点击放大")

### 沉浸光感的档位

为应对不同设备的性能差异，沉浸光感提供了多个档位供开发者选择：

| **档位** | **[MaterialLevel](../harmonyos-references/ui-design-hdsmaterial.md#materiallevel)枚举** | **说明** |
| --- | --- | --- |
| **强** | EXQUISITE | 完整的沉浸光感效果，包含所有视觉特性，适合高性能设备。 |
| **均衡（默认）** | GENTLE | 适度的沉浸光感效果，在视觉效果与性能之间取得平衡。 |
| **弱** | SMOOTH | 轻量级沉浸光感效果，仅保留核心视觉特性，适合低性能设备。 |
| **系统自适应** | ADAPTIVE | 由系统根据设备性能自动选择合适的档位，推荐大多数场景使用。 |

**说明** 

* 推荐使用默认值ADAPTIVE档位。该模式下，系统会根据当前设备的算力动态调整组件的材质效果，兼顾性能与显示效果。
* 若未采用系统自适应能力，请先调用[getSystemMaterialTypes()](https://link.gitcode.com/?target=https://developer.huawei.com/consumer/cn/doc/doccenter-references/api/ui-design-hdsmaterial#getsystemmaterialtypes&from=https://gitcode.com/self_dev/BestPractice/blob/dev/zh_CN/innovation-feature-development/technical-innovation/bpta-spatiality-immersive.md&lang=zh&theme=white)接口查询当前设备支持的材质能力，再根据查询结果选用相应的材质效果枚举：
  + 如果查询结果显示当前设备支持IMMERSIVE材质类型，可选用EXQUISITE或GENTLE效果。
  + 如果查询结果显示当前设备不支持IMMERSIVE材质类型，则建议使用SMOOTH效果，以降低卡顿和发热风险，保障用户体验。

沉浸光感效果由材质滤镜、折射、高光、阴影等多层效果叠加而成，渲染时需要消耗GPU资源，不合理使用会显著增加功耗。在实际应用中，总体原则是将沉浸光感效果作为一种"稀缺"视觉资源使用，具体参考[沉浸光感功耗优化](https://link.gitcode.com/?target=https://developer.huawei.com/consumer/cn/doc/doccenter-capabilities/arkts-immersive-light-sense-constraints&from=https://gitcode.com/self_dev/BestPractice/blob/dev/zh_CN/innovation-feature-development/technical-innovation/bpta-spatiality-immersive.md&lang=zh&theme=white)。

## 沉浸光感适配方案

沉浸光感的适配要从框架层面整体规划，核心策略是：

* 采用HDS系列组件替代传统组件以直接获得沉浸效果，具体请参考[UI Design Kit（UI设计套件）](../harmonyos-guides/ui-design-kit-guide.md)下的[沉浸光感](../harmonyos-guides/ui-design-hds-component-material.md)。
* 普通ArkUI组件通过应用级开启或者组件级开启方式[开启沉浸光感](../harmonyos-guides/arkts-immersive-light-sense-enable.md)，具体请参考[UI开发（ArkTS声明式开发范式）](../harmonyos-guides/arkts-ui-development.md)下的[沉浸光感](../harmonyos-guides/arkts-immersive-light-sense.md)。

为有效实现沉浸光感效果，应遵循“从整体到局部”的适配原则：首先通过整体框架适配确立应用的基础视觉规范，为后续工作奠定基础；在此基础上，针对标题栏、底部导航及内容区域组件进行针对性调整，以确保视觉风格统一与交互体验连贯。

### 整体框架适配

1. 采用HDS系列组件

   应用需要将传统的Navigation、Tabs等组件替换为HDS系列组件：

   * **HDS导航（[HdsNavigation](../harmonyos-references/ui-design-hdsnavigation.md)/[HdsNavDestination](../harmonyos-references/ui-design-hdsnavdestination.md)）**：通过设置[TitleBarStyleOptions](../harmonyos-references/ui-design-hdsnavigation.md#titlebarstyleoptions)的systemMaterialEffect参数，可为标题栏按钮设置沉浸光感视效。
   * **HDS底部页签（[HdsTabs](../harmonyos-references/ui-design-hdstabs.md)）**：通过设置[HdsTabsFloatingStyle](../harmonyos-references/ui-design-hdstabs.md#hdstabsfloatingstyle)的systemMaterialEffect参数，可为底部页签设置沉浸光感视效。

   已采用HDS系列组件的应用，即可通过systemMaterialEffect属性配置沉浸光感效果，且始终跟随最新规范，大大减少了适配工作量。
2. 普通组件开启沉浸光感

   组件开启沉浸光感可以查看[组件适配沉浸光感](../harmonyos-guides/arkts-immersive-light-sense-component-adaptation.md)，系统介绍各组件如何通过应用级开关与组件级配置开启沉浸光感，涵盖沉浸光感的视觉效果、设置方法及适配要点，帮助开发者快速完成沉浸光感的组件适配。

   本文通过组件级开启方式设置沉浸式系统材质，设置方式分三种方式开启：

   * 通过通用属性设置

     通过设置组件的[systemMaterial](../harmonyos-references/ts-universal-attributes-image-effect.md#systemmaterial)属性来开启新材质效果。该属性本身是一个开关：

     1. **开启效果**：.systemMaterial(new uiMaterial.ImmersiveMaterial())或者.systemMaterial(undefined)
     2. **关闭效果**：.systemMaterial(uiMaterial.Material.empty)
   * 通过组件专属接口设置

     当前支持设置的组件包括：Select下拉菜单的[menuSystemMaterial](../harmonyos-references/ts-basic-components-select.md#menusystemmaterial)、Navigation标题栏的[systemMaterial](../harmonyos-references/ts-basic-components-navigation.md#navigationtitleoptions11)。
   * 弹窗类组件通过options参数中的systemMaterial字段设置。

   **说明** 

   * 开启沉浸光感，要确保应用的[targetAPIVersion](../harmonyos-guides/app-configuration-file.md)不低于26.0.0。如果低版本适配，适配指导请参考[ArkTS API兼容性保护](../harmonyos-releases/arkts-api-compatibility-warning-elim.md)。
   * 沉浸光感开启后，除了弹窗类组件或方法、Slider、Toggle，其他组件仅在以下区域中生效：Navigation/NavDestination标题栏，或横向Tabs中barPosition为BarPosition.End的底部TabBar中。

     弹窗类组件或方法包括：Popup、Tips、Menu、BindSheet、showActionMenu、AlertDialog、CustomDialog、ActionSheet、CalendarPickerDialog、DatePickerDialog、TextPickerDialog、TimePickerDialog、Toast、Select、AlphabetIndexer气泡弹窗、Text设置copyOption后长按或双击触发的文本菜单、SelectionMenu（结合bindSelectionMenu一起使用）。
   * 沉浸光感开启后，需要大量GPU资源，具体的使用指导请参考[沉浸光感功耗优化](../harmonyos-guides/arkts-immersive-light-sense-constraints.md)，其余开启后的常见问题请参考[沉浸光感常见问题](../harmonyos-guides/arkts-immersive-light-sense-faq.md)。

### 标题栏适配

标题栏是沉浸光感最直观的体现。沉浸光感标题栏示意图如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/XmQw6MxkRDSxE_fcydi8tg/zh-cn_image_0000002624492723.gif?HW-CC-KV=V1&HW-CC-Date=20261114T005402Z&HW-CC-Expire=31536000000&HW-CC-Sign=78DCFD2F9D998DC591DAE13E74E043936E7324E6505EDA6ADF17D0A4FDC57DA4 "点击放大")

* 标题栏使用材质

  通过HdsNavigation或HdsNavDestination的[titleBar](../harmonyos-references/ui-design-hdsnavigation.md#titlebar)属性，可以配置标题栏的滚动效果与材质效果。

  关键属性值说明：

  | **属性** | **说明** |
  | --- | --- |
  | [ScrollEffectType](../harmonyos-references/ui-design-hdsnavigation.md#scrolleffecttype) | 渐变模糊效果，标题栏随滑动从透明渐变为模糊。 |
  | [MaterialType](../harmonyos-references/ui-design-hdsmaterial.md#materialtype) | 自适应材质类型，系统根据场景自动选择材质风格。 |
  | [MaterialLevel](../harmonyos-references/ui-design-hdsmaterial.md#materiallevel) | 自适应材质强度，系统根据设备性能自动选择档位。 |

  **说明** 

  渐变模糊效果对比：

  + IMMERSIVE\_GRADIENT\_BLUR（沉浸光感渐变模糊）：标题栏从完全透明渐变到模糊，模糊区域更大，过渡更自然，沉浸感更强。配合材质效果，呈现通透的视觉体验。
  + GRADIENT\_BLUR（渐变模糊）：标题栏从半透明渐变到模糊，过渡相对克制。配合材质效果，在通透与信息密度之间取得平衡。

  两种效果都需要配合systemMaterialEffect材质属性使用，才能呈现完整的沉浸光感效果.
* 标题栏和状态栏适配滑动显隐

  在沉浸光感页面中，标题栏和状态栏支持滑动隐藏，具体可参考[标题栏动态显隐](../harmonyos-guides/ui-design-navigation-dynamic-display-and-hiding.md)。具体实现方案如下：

  1. 通过[dynamicHideTitleBar](../harmonyos-references/ui-design-hdsnavigation.md#dynamichidetitlebar)属性的hideTitleArea和hideStatusBar分别启动标题栏、状态栏的动态显隐功能。
  2. 通过[dynamicHideTitleBar](../harmonyos-references/ui-design-hdsnavigation.md#dynamichidetitlebar)属性的mode设置动态显隐模式，[HideMode](../harmonyos-references/ui-design-hdsnavigation.md#hidemode)支持三种模糊模式（SCROLL\_UP\_TO、SCROLL\_UP、SCROLL\_DOWN）以及混合模式（SCROLL\_UP\_TO\_BLEND\_SCROLL\_UP）。
  3. 调用[bindToScrollable](../harmonyos-references/ui-design-hdsnavigation.md#bindtoscrollable)接口绑定内容区滚动组件，实现标题栏和状态栏模糊度与透明度的同步变化。

### 底部导航适配

* 设置悬浮导航

  设置[barOverlap](../harmonyos-references/ui-design-hdstabs.md#baroverlap)(true)以启用悬浮模糊背景，通过[barFloatingStyle](../harmonyos-references/ui-design-hdstabs.md#barfloatingstyle)配置悬浮样式，可将HdsTabs切换为悬浮胶囊形态，并通过barBottomMargin调整与内容区域的间距，增强视觉轻盈感。

  悬浮导航示意图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/4p4GVFfbSFumgnI4I3e_GQ/zh-cn_image_0000002594213114.png?HW-CC-KV=V1&HW-CC-Date=20261114T005402Z&HW-CC-Expire=31536000000&HW-CC-Sign=FA92C1718DFE349FA60FCF165ECA7CF49AD5902718CDB6F8D9AFD4F2E9260695 "点击放大")
* 设置沉浸光感效果

  悬浮导航栏的沉浸光感效果可通过barFloatingStyle中的systemMaterialEffect属性进行配置，其中materialType用于定义材质风格，materialLevel则控制材质强度。

  沉浸光感示意图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/DKReEEehQTe7oFzmxXxGWw/zh-cn_image_0000002624612573.png?HW-CC-KV=V1&HW-CC-Date=20261114T005402Z&HW-CC-Expire=31536000000&HW-CC-Sign=07C6686AB375C72A9AEDC75CE0D412ABC3511BEFB99AAE8DFD4E0C81158FDF51 "点击放大")
* 沉浸式MiniBar

  针对悬浮导航的多功能场景，例如音乐播放等需同时展示底部导航和播放控制的场景，HdsTabs提供了MiniBar能力，即在底部导航栏中嵌入一个可折叠展开的[迷你栏](../harmonyos-guides/ui-design-hds-tabs-bar-floating.md#迷你栏)。

  1. 设置HdsTabs布局位置[barPosition](../harmonyos-references/ui-design-hdstabs.md#barposition)和层级叠加[barOverlap](../harmonyos-references/ui-design-hdstabs.md#baroverlap)之后，通过[barFloatingStyle](../harmonyos-references/ui-design-hdstabs.md#barfloatingstyle)方法的miniBar属性允许开发者自定义一个悬浮于屏幕底部的迷你控制中心。
  2. miniBarBuilder的配置通过[@Builder装饰器：自定义构建函数](../harmonyos-guides/arkts-builder.md)来创建自定义的迷你栏。

  MiniBar示意图如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/jbcinbcJQO-OVInJmyW2Mg/zh-cn_image_0000002594053200.gif?HW-CC-KV=V1&HW-CC-Date=20261114T005402Z&HW-CC-Expire=31536000000&HW-CC-Sign=C39C61455F298447DC6C2C91BD79741BCC99F9CF92130F031D7EE8D18B236203)

### 内容区域组件适配

对于内容区域中的普通组件，可通过设置其[systemMaterial](../harmonyos-references/ts-universal-attributes-image-effect.md#systemmaterial)属性为ImmersiveMaterial实例来启用新材质效果。支持三个关键参数配置：

* **style**: 用于定义材质视觉样式，可选值详见[ImmersiveStyle](../harmonyos-references/arkts-apis-uimaterial.md#immersivestyle)枚举。
* **interactive**：控制是否启用交互形变效果。
* **lightEffect**：用于配置光感交互反馈效果。

**说明** 

沉浸光感开启后，除了弹窗类组件或方法、Slider、Toggle，其他组件仅在以下区域中生效：Navigation/NavDestination标题栏，或横向Tabs中barPosition为BarPosition.End的底部TabBar中。

效果示意图如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/3bfeeqsGRzSXrUiTItbtCw/zh-cn_image_0000002624492725.gif?HW-CC-KV=V1&HW-CC-Date=20261114T005402Z&HW-CC-Expire=31536000000&HW-CC-Sign=15A55D1B4D834E18B68ABC72F5ACCE448F225986E99D1AC713A7C43276E46B82)

## 场景一：应用首眼沉浸光感

应用首眼是用户打开应用的第一印象，沉浸光感能让首眼效果焕然一新。基于HDS提供的HdsNavigation与HdsTabs组件，通过配置沉浸光感材质，即可打造精致的首眼视觉效果。

| **首眼沉浸效果-强** | **首眼沉浸效果-均衡** | **首眼沉浸效果-弱** |
| --- | --- | --- |
|  |  |  |

### 列表标题栏适配光感

* 标题栏使用材质

  沉浸光感标题栏的实现通过设置titleBar.style.systemMaterialEffect以启用材质效果，设置titleBar.style.scrollEffectOpts以配置标题栏的滚动效果。

  ```typescript
  import {
    hdsMaterial,
    HdsNavigation,
    HdsNavigationMenuContentOptions,
    HdsNavigationTitleMode,
    HideMode,
    ScrollEffectType,
    TextStyleMode,
  } from '@kit.UIDesignKit';
  // ...
      HdsNavigation() {
        // ...
      }
      // ...
      .titleBar({
        // ...
        style: {
          scrollEffectOpts: {
            enableScrollEffect: true,
            scrollEffectType: ScrollEffectType.GRADIENT_BLUR,
            // ...
          },
          systemMaterialEffect: {
            materialType: hdsMaterial.MaterialType.ADAPTIVE,
            materialLevel: this.customMaterialLevel.level,
          },
        },
        // ...
      })
      // ...
  ```

  **说明** 

  [MaterialLevel](../harmonyos-references/ui-design-hdsmaterial.md#materiallevel)使用了this.customMaterialLevel.level，这意味着用户可以通过菜单动态切换沉浸光感的强度档位。
* 标题栏和状态栏适配滑动隐藏

  实现方案如下：

  1. 通过[dynamicHideTitleBar](../harmonyos-references/ui-design-hdsnavigation.md#dynamichidetitlebar)属性的hideTitleArea和hideStatusBar分别设置为true，以启动标题栏、状态栏的动态显隐功能。
  2. 通过[dynamicHideTitleBar](../harmonyos-references/ui-design-hdsnavigation.md#dynamichidetitlebar)属性的mode设置为HideMode.SCROLL\_UP\_TO，上滑到固定位置隐藏，下滑到固定位置显示。
  3. 调用[bindToScrollable](../harmonyos-references/ui-design-hdsnavigation.md#bindtoscrollable)接口绑定内容区滚动组件，实现标题栏和状态栏模糊度与透明度的同步变化。

  ```typescript
  .hideBackButton(false)
  .titleMode(HdsNavigationTitleMode.MINI)
  .dynamicHideTitleBar({
    hideTitleArea: true,
    hideStatusBar: true,
    mode: HideMode.SCROLL_UP_TO,
  })
  // ...
  .bindToScrollable([this.scroller])
  ```

### 首页底部导航适配

1. 使用悬浮导航

   首页底部导航可通过HdsTabs悬浮模式实现，配置[barFloatingStyle](../harmonyos-references/ui-design-hdstabs.md#barfloatingstyle)属性可自定义悬浮栏样式，包括圆角、背景色及位置偏移等参数，适配多设备布局需求。

   ```typescript
   HdsTabs({ controller: this.controller }) {
     // ...
   }
   .scrollable(false)
   .barOverlap(true)
   .vertical(false)
   .barPosition(BarPosition.End)
   .onAttach(() => {
     try {
       this.controller.preloadItems([0, 1, 2, 3, 4]);
     } catch (error) {
       Logger.error(TAG, `OnAttach preloadItems failed`);
     }
   })
   .barFloatingStyle({
     barBottomMargin: this.globalInfoModel.naviIndicatorHeight > 0 ? this.globalInfoModel.naviIndicatorHeight :
       $r('sys.float.padding_level8'),
     adaptToHandedness: true,
     systemMaterialEffect: {
       materialType: hdsMaterial.MaterialType.ADAPTIVE,
       materialLevel: this.customMaterialLevel.level,
     }
   })
   ```

   **说明** 

   [MaterialLevel](../harmonyos-references/ui-design-hdsmaterial.md#materiallevel)使用了this.customMaterialLevel.level，这意味着用户可以通过菜单动态切换沉浸光感的强度档位。
2. 适配新材质

   悬浮导航栏的材质效果通过统一配置systemMaterialEffect的参数[SystemMaterialParams](../harmonyos-references/ui-design-hdstabs.md#systemmaterialparams)，让标题栏与悬浮导航栏呈现出协调一致的光感视觉风格。

   ```typescript
   HdsNavigation() {
     // ...
   }
   // ...
   .titleBar({
     // ...
     style: {
       // ...
       systemMaterialEffect: {
         materialType: hdsMaterial.MaterialType.ADAPTIVE,
         materialLevel: this.customMaterialLevel.level,
       },
     },
     // ...
   })
   // ...
   ```

### 菜单栏适配沉浸光感

菜单栏沉浸光感适配的核心是通过封装版本兼容的材质工具类，实现API级别的平滑过渡。菜单栏沉浸光感效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/6bqrMBcpQYa6plODS0ebtA/zh-cn_image_0000002624951609.gif?HW-CC-KV=V1&HW-CC-Date=20261114T005402Z&HW-CC-Expire=31536000000&HW-CC-Sign=6AAEC86A14D8013B2F5E083D40934493316C4AC171035230A8C0BEBB31669402 "点击放大")

* 材质工具类封装

  ```typescript
  import { uiMaterial } from '@kit.ArkUI';
  import { deviceInfo } from '@kit.BasicServicesKit';
  import { hdsMaterial } from '@kit.UIDesignKit';

  export class MaterialUtil {
    // ...

    public static getMaterialOptions<T>(option: T): MaterialOptions<T> | T {
      if (deviceInfo.apiAvailable('26.0.0') && hdsMaterial.getSystemMaterialTypes().length > 0) {
        const materialOptions = option as MaterialOptions<T>;
        materialOptions.systemMaterial = new uiMaterial.ImmersiveMaterial({
          style: uiMaterial.ImmersiveStyle.THICK,
          interactive: true,
          lightEffect: { color: undefined }
        });
        return materialOptions;
      }
      return option;
    }
  }

  interface MaterialOptions<T> extends ThisType<T> {
    systemMaterial?: SystemUiMaterial;
  }
  ```

* 菜单栏具体实现

  ```typescript
  private menuId: string = 'MaterialLevelMenu' + this.currentIndex;
  private menus: HdsNavigationMenuContentOptions = {
    value: [
      {
        content: {
          label: $r('app.string.level'),
          icon: $r('sys.symbol.house_fill'),
          type: TextStyleMode.NORMAL,
          componentId: this.menuId,
          action: () => {
            try {
              const uiContext = this.getUIContext();
              const promptAction = this.getUIContext().getPromptAction();
              const contentNode = new ComponentContent(uiContext, wrapBuilder(materialLevelMenu))
              promptAction.openMenu(contentNode, { id: this.menuId }, MaterialUtil.getMaterialOptions<MenuOptions>(
                { mask: false, backgroundBlurStyle: BlurStyle.COMPONENT_THICK }) as MenuOptions)
                .catch((error: BusinessError) => {
                  Logger.error(TAG, `Show menu failed. cause code: ${error.code}, msg: ${error.message}`);
                });
            } catch (error) {
              Logger.error(TAG, `Show menu failed. cause msg: ${error.message}`);
            }
          }
        }
      }
    ],
  };
  ```

## 场景二：自适应悬浮导航

自适应悬浮导航作为空间化核心交互能力，可通过HdsTabs的悬浮模式和MiniBar配置快速实现多设备适配，提升用户操作效率。效果示意如下图：

| **自适应悬浮-展开** | **自适应悬浮-折叠1** | **自适应悬浮-折叠2** |
| --- | --- | --- |
|  |  |  |

### 沉浸式迷你栏

在音乐播放场景中，采用主HdsTabs与可折叠MiniBar的组合方案。MiniBar作为嵌入HdsTabs的迷你控制栏，可灵活切换折叠/展开状态。示例效果折叠时呈现紧凑播放控制条，展开时展示完整播放信息与控制按钮，实现空间高效利用与操作便捷性的统一。

1. 设置悬浮导航布局位置与层级叠加
   * 设置[barPosition](../harmonyos-references/ui-design-hdstabs.md#barposition)为BarPosition.End且[vertical](../harmonyos-references/ui-design-hdstabs.md#vertical)为false，使页签栏置于容器底部。
   * 设置[barOverlap](../harmonyos-references/ui-design-hdstabs.md#baroverlap)为true，使页签栏悬浮于内容之上。
2. 设置沉浸光感

   设置[barFloatingStyle](../harmonyos-references/ui-design-hdstabs.md#barfloatingstyle)的materialType材质效果与materialLevel材质等级均为自适应（ADAPTIVE）模式。
3. 设置迷你栏

   通过[barFloatingStyle](../harmonyos-references/ui-design-hdstabs.md#barfloatingstyle)方法的miniBar属性自定义迷你栏。

```typescript
import {
  HdsBarStyle,
  hdsMaterial,
  HdsNavDestination,
  HdsTabs,
  HdsTabsController,
  ScrollEffectType,
} from '@kit.UIDesignKit';
// ...
  private controller: HdsTabsController = new HdsTabsController();
  @Local globalInfoModel: GlobalInfoModel =
    AppStorageV2.connect(GlobalInfoModel, StorageKey.GLOBAL_INFO) ?? new GlobalInfoModel();
  @Local isMiniBar: boolean = true;

  @Builder
  miniBarBuilder() {
    Row() {
      // ...
    }
  }
  // ...
      HdsTabs({ controller: this.controller }) {
        // ...
      }
      .barOverlap(true)
      .vertical(false)
      .barPosition(BarPosition.End)
      .barFloatingStyle({
        barBottomMargin: this.globalInfoModel.naviIndicatorHeight > 0 ? this.globalInfoModel.naviIndicatorHeight :
          $r('sys.float.padding_level8'),
        systemMaterialEffect: {
          materialType: hdsMaterial.MaterialType.IMMERSIVE,
          materialLevel: hdsMaterial.MaterialLevel.ADAPTIVE
        },
        miniBar: {
          miniBarBuilder: () => this.miniBarBuilder(),
          onBarStyleChange: (miniBarStyle: HdsBarStyle) => {
            this.isMiniBar = miniBarStyle === HdsBarStyle.COLLAPSE
          }
        }
      })
      // ...
```

### 多设备左右栏适配

MiniBar可根据设备宽度自动适配展开/折叠状态：宽屏设备（如平板）默认展开，窄屏设备（如手机）默认折叠，无需开发者手动干预。

## 场景三：智感握姿，智能交互

智感握姿是空间化在交互层面的核心能力。在宽屏设备上，基于智能感知用户握持，底部悬浮导航栏会自动跟随握持手左右切换位置，提供智能化交互体验。具体开发者请查看[智感握姿](bpta-smart-reach.md)。

## 示例代码

* [沉浸光感开发案例](https://gitcode.com/HarmonyOS_Samples/Spatialization)
