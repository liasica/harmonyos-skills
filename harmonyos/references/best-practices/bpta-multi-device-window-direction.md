---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-window-direction
title: 窗口方向
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备窗口形态 > 窗口方向
category: best-practices
scraped_at: 2026-09-02T15:03:18+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:69112f0f0418e18d61437c7579a6502feba8e30438f2d55e957d017f3487305f
---

## 概述

窗口方向适配旨在解决应用不同场景下窗口的朝向问题。以直板机上的视频类应用为例，应用首页通常竖屏显示；而全屏视频播放页通常横屏显示。其核心的策略在于动态调整应用窗口方向的显示策略（即window的[Orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)，以下简称“**窗口旋转策略**”），确保在不同用户交互场景下提升用户体验。

本文主要内容如下：

* 前置约束与限制：介绍窗口方向的含义。明确指出在设备形态多样化的前提下，如何选择更合适的窗口旋转策略。
* 窗口旋转策略枚举：介绍窗口旋转策略的枚举值，并解析各值在不同设备形态下的行为映射，帮助开发者理解系统的底层适配逻辑。
* 实现原理：介绍配置页面窗口旋转策略的技术实现机制与核心流程。

* 典型场景：
  + 应用首页案例：通用页面窗口旋转策略。
  + 游戏应用案例：竖屏或横屏方向锁定的窗口旋转策略。
  + 图库案例：四个方向自动旋转且受控制中心的旋转开关控制的窗口旋转策略。
  + 个股详情页 & 股票K线图页：应用组合页面内根据场景不同切换的窗口旋转策略。
  + 视频详情页 & 全屏播放页：相同页面内根据用户行为切换的窗口旋转策略。

## 前置约束与限制

在阅读本文前，建议开发者先了解[窗口管理](../harmonyos-guides/window-manager.md)、[窗口旋转](../harmonyos-guides/window-rotation.md)、[屏幕管理](../harmonyos-guides/display-manager.md)、[一次开发，多端部署](bpta-multi-device-overview.md)、[组件导航（Navigation）](../harmonyos-guides/arkts-navigation-navigation.md)等相关知识。

横竖屏切换功能可实现应用内既支持竖屏显示也支持横屏显示的效果。对于应用内不同页面显示方向不同的情况，需在应用逻辑中动态修改窗口方向以实现该效果。例如，在直板机上具备视频播放功能的应用中，首页内容是采用竖屏方式，而全屏播放页则采用横屏方式展示。

随着设备形态日益丰富，应用页面支持旋转已从部分页面适配发展为全面支持。因此，选择合适的旋转策略，对应用开发至关重要。

目前HarmonyOS系统中设备的显示方向有以下四种，对应真机实际状态如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/ECO3wCttSHG5k6veSB1K5w/zh-cn_image_0000002566756945.png)

**基本定义：**

以设备物理屏幕尺寸为判定依据，设备的显示方向定义如下：

* 竖屏（PORTRAIT）：屏幕高度大于宽度，用户正向握持设备时充电口朝下（默认竖屏状态）。
* 反向竖屏（PORTRAIT\_INVERTED）：屏幕高度大于宽度，但设备倒置，即充电口朝上。
* 横屏（LANDSCAPE）：屏幕宽度大于高度，用户正向握持设备时充电口朝右（默认横屏状态）。
* 反向横屏（LANDSCAPE\_INVERTED）：屏幕宽度大于高度，但设备倒置，即充电口朝左。

**区分方法**：

系统提供了@ohos.display模块来获取屏幕的当前方向（[Orientation](../harmonyos-references/js-apis-display.md#orientation10)）和旋转角度（即[Display](../harmonyos-references/js-apis-display.md#display)的rotation）。屏幕方向直接对应上述四种方向枚举值，而旋转角度表示屏幕相对于默认方向的顺时针旋转度数，其对应关系如下表（以常见直板机为例）：

| 屏幕旋转角度返回值 (rotation) | 对应度数 | 屏幕方向 (Orientation) |
| --- | --- | --- |
| 0 | 0° | 竖屏 (PORTRAIT) |
| 1 | 90° | 反向横屏 (LANDSCAPE\_INVERTED) |
| 2 | 180° | 反向竖屏 (PORTRAIT\_INVERTED) |
| 3 | 270° | 横屏 (LANDSCAPE) |

## 了解窗口旋转策略

窗口旋转策略提供了18种窗口旋转策略（即window的[Orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)），开发者可通过预设相关窗口旋转策略控制应用在不同场景下的窗口显示方向。为帮助开发者能更快速的理解这些策略，下文会分类说明18个枚举值的含义及对应效果。

### 固定方向策略

固定方向旋转策略是指应用窗口在启动或页面跳转时被锁定在特定显示方向（如竖屏、横屏等），且不随设备物理方向改变而自动旋转，包含以下五类：

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PORTRAIT | 1 | 表示竖屏显示模式。 |
| LANDSCAPE | 2 | 表示横屏显示模式。 |
| PORTRAIT\_INVERTED | 3 | 表示反向竖屏显示模式。 |
| LANDSCAPE\_INVERTED | 4 | 表示反向横屏显示模式。 |
| LOCKED | 11 | 表示锁定模式，窗口显示方向与屏幕当前方向（参考[Orientation](../harmonyos-references/js-apis-display.md#orientation10)）一致。 |

以三折叠G态为例，窗口初始方向的效果图如下：

| 初始方向 | 枚举值 | 设备竖屏时，应用启动效果图 | 设备横屏时，应用启动效果图 |
| --- | --- | --- | --- |
| 竖屏 | PORTRAIT |  |  |
| 反向竖屏 | PORTRAIT\_INVERTED |  |  |
| 横屏 | LANDSCAPE |  |  |
| 反向横屏 | LANDSCAPE\_INVERTED |  |  |
| 锁定模式 | LOCKED |  |  |

### 自动旋转策略

自动旋转策略是指应用窗口能够根据设备物理方向（即重力传感器）的变化自动调整显示方向，且可能受系统控制中心“旋转锁定”开关的影响。

**说明** 

控制中心的旋转开关用于控制屏幕是否可以旋转。当“旋转锁定”高亮时，表示已锁定，无法旋转；当“旋转锁定”为灰色时，表示已解锁，可以旋转。

例如，若要实现跟随控制中心的自动旋转，包括横屏、竖屏、反向横屏、反向竖屏，则可设置为AUTO\_ROTATION\_RESTRICTED。

若不希望跟随控制中心的旋转控制，只需设置为AUTO\_ROTATION，此时应用的旋转不受控制中心锁定的影响。其他旋转方式亦然。

**不受控制中心控制的自动旋转**

不受控制中心控制的自动旋转策略包含以下三类：

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO\_ROTATION | 5 | 跟随传感器自动旋转，可以旋转到竖屏、横屏、反向竖屏、反向横屏四个方向，且不受控制中心的旋转开关控制。 |
| AUTO\_ROTATION\_PORTRAIT | 6 | 跟随传感器自动竖向旋转，可以旋转到竖屏、反向竖屏，无法旋转到横屏、反向横屏，且不受控制中心的旋转开关控制。 |
| AUTO\_ROTATION\_LANDSCAPE | 7 | 跟随传感器自动横向旋转，可以旋转到横屏、反向横屏，无法旋转到竖屏、反向竖屏，且不受控制中心的旋转开关控制。 |

以三折叠G态为例，不受控制中心控制的自动旋转策略效果图如下：

|  | 不受开关控制枚举值 | 不受开关控制效果图 |
| --- | --- | --- |
| 自由旋转（竖屏/反向竖屏/横屏/反向横屏） | AUTO\_ROTATION |  |
| 竖屏旋转（竖屏/反向竖屏） | AUTO\_ROTATION\_PORTRAIT |  |
| 横屏旋转（横屏/反向横屏） | AUTO\_ROTATION\_LANDSCAPE |  |

**说明** 

控制中心的旋转开关用于控制屏幕是否可以旋转。当“旋转锁定”高亮时，表示已锁定，无法旋转；当“旋转锁定”为灰色时，表示已解锁，可以旋转。

例如，若要实现跟随控制中心的自动旋转，包括横屏、竖屏、反向横屏、反向竖屏，则可设置为AUTO\_ROTATION\_RESTRICTED。

若不希望跟随控制中心的旋转控制，只需设置为AUTO\_ROTATION，此时应用的旋转不受控制中心锁定的影响。其他旋转方式亦然。

**受控制中心控制的自动旋转**

受控制中心控制的自动旋转策略包含以下四类：

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO\_ROTATION\_RESTRICTED | 8 | 跟随传感器自动旋转，可以旋转到竖屏、横屏、反向竖屏、反向横屏四个方向，且受控制中心的旋转开关控制。 |
| AUTO\_ROTATION\_PORTRAIT\_RESTRICTED | 9 | 跟随传感器自动竖向旋转，可以旋转到竖屏、反向竖屏，无法旋转到横屏、反向横屏，且受控制中心的旋转开关控制。 |
| AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED | 10 | 跟随传感器自动横向旋转，可以旋转到横屏、反向横屏，无法旋转到竖屏、反向竖屏，且受控制中心的旋转开关控制。 |
| AUTO\_ROTATION\_UNSPECIFIED | 12 | 跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定。 |

以三折叠G态（即三折叠设备完全展开时的三屏显示状态）为例，受控制中心控制的自动旋转策略效果图如下：

|  |  |  |
| --- | --- | --- |
| 自由旋转（竖屏/反向竖屏/横屏/反向横屏） | AUTO\_ROTATION\_RESTRICTED |  |
| 竖屏旋转（竖屏/反向竖屏） | AUTO\_ROTATION\_PORTRAIT\_RESTRICTED |  |
| 横屏旋转（横屏/反向横屏） | AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED |  |
| 跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定。 | AUTO\_ROTATION\_UNSPECIFIED |  |

**带首选方向的自动旋转**

带首选方向的旋转策略允许应用在启动时或调用接口时临时切换到指定方向（如竖屏、横屏等），之后跟随设备传感器自动旋转，且该自动旋转受控制中心“旋转锁定”开关控制，同时可旋转方向受系统对当前设备形态判定的影响，具体可分为以下四类：

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER\_ROTATION\_PORTRAIT | 13 | 调用时临时旋转到竖屏，之后跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定。 |
| USER\_ROTATION\_LANDSCAPE | 14 | 调用时临时旋转到横屏，之后跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定。 |
| USER\_ROTATION\_PORTRAIT\_INVERTED | 15 | 调用时临时旋转到反向竖屏，之后跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定。 |
| USER\_ROTATION\_LANDSCAPE\_INVERTED | 16 | 调用时临时旋转到反向横屏，之后跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定。 |

**说明** 

可旋转方向受系统判定：在自动旋转开关开启的状态下，窗口可旋转至的具体方向（如竖屏、横屏、反向横屏等）由系统根据当前设备的形态（如直板机、折叠屏展开态、平板等）自动决定，以提供最佳体验。在具体设备上会禁用不适合用户使用的方向，例如在直板机上可以旋转到竖屏、横屏、反向横屏三个方向，无法旋转到反向竖屏。

### 跟随桌面显示策略

跟随桌面显示策略适用于适配多种设备形态（如手机、平板、折叠屏）的应用，使应用自动继承系统桌面的旋转策略，从而在不同设备上提供一致且符合用户预期的旋转体验。例如，在同时适配手机和平板的应用中，若希望应用在平板上随桌面横竖屏旋转，而在手机上保持竖屏锁定，可采用此策略，无需为不同设备单独编写复杂的旋转逻辑。

该策略简化了多设备适配的复杂度，开发者无需针对每种设备形态单独配置旋转行为，系统会自动根据桌面状态管理应用窗口的方向。具体实现可参考“[跟随桌面的旋转策略](bpta-multi-device-window-direction.md#section3434202623320)”章节。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FOLLOW\_DESKTOP | 17 | 表示跟随桌面的旋转模式，如果桌面可以旋转则可旋转，桌面不可旋转则不可旋转。 |

## 选择合适的窗口旋转策略

应用在不同业务界面需设置合适的窗口旋转策略，以提供最佳用户体验。

为正确选择旋转策略枚举，开发者可通过通过是否支持自动旋转、支持旋转的方向及预设初始方向三个维度进行匹配，具体参考如下表：

| 是否支持自动旋转 | 支持旋转的方向 | 预设初始方向 | 窗口旋转策略 |
| --- | --- | --- | --- |
| 固定方向 | NA | 竖屏 | PORTRAIT |
| NA | 横屏 | LANDSCAPE |
| NA | 反向竖屏 | PORTRAIT\_INVERTED |
| NA | 反向横屏 | LANDSCAPE\_INVERTED |
| 受控自动旋转 | 竖两向可旋转 | NA | AUTO\_ROTATION\_PORTRAIT\_RESTRICTED |
| 横两向可旋转 | NA | AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED |
| 最多四向可旋转，但受系统判定 | NA | AUTO\_ROTATION\_UNSPECIFIED |
| 竖屏 | USER\_ROTATION\_PORTRAIT |
| 横屏 | USER\_ROTATION\_LANDSCAPE |
| 反向竖屏 | USER\_ROTATION\_PORTRAIT\_INVERTED |
| 反向横屏 | USER\_ROTATION\_LANDSCAPE\_INVERTED |
| 跟随桌面策略 | NA | NA | FOLLOW\_DESKTOP |

上述表格也可以抽象为如下的决策逻辑，如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/i9KCg2oQRguMoMP3AvfieA/zh-cn_image_0000002572763022.png "点击放大")

**说明** 

不推荐使用不受控制中心限制的自动旋转策略，故未将其列入表格。如特定场景需要，可直接使用[自动旋转策略](bpta-multi-device-window-direction.md#section180611396137)中的该策略。

**窗户策略工具类**

为提升开发者窗口旋转策略选择的易用性，结合上述策略决策逻辑图，我们提供了一套窗口旋转策略选择工具类，支持三种使用形式。

1. 通过链式属性访问直接获取策略值

   若开发者需要在代码的中硬编码策略值，可通过工具类中的OrientationPresets常量，采用三层递进的链式调用获取旋转策略枚举，示例如下：

   ```typescript
   @Component
   export struct Home {
     windowObj: window.Window | undefined = undefined;
     // ...

     aboutToAppear(): void {
       this.tabBarsInfo.setTabList(TabBarsInfo);
       try {
         this.windowObj = (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync()
       } catch (err) {
         Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
       }

       // Use the WindowOrientationHelper tool to directly obtain the rotation strategy enumeration through chained calls.
       this.windowObj?.setPreferredOrientation(WindowOrientationHelper.presets.FOLLOW_DESKTOP)
         .catch((err: BusinessError) => {
           Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
         });
       // ...
     }

     aboutToDisappear() {
       // Use the WindowOrientationHelper tool to directly obtain the rotation strategy enumeration through chained calls.
       this.windowObj?.setPreferredOrientation(WindowOrientationHelper.presets.FIXED.UNSPECIFIED)
         .catch((err: BusinessError) => {
           Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
         });
     }

     // ...

     build() {
       // ...
     }
   }
   ```
2. 通过函数式选择器动态选择

   若开发者在特定界面场景下已确定主行为模式，仅需根据条件细化策略，则可采用该方法，示例如下：

   ```typescript
   @Component
   export struct PortraitModeGame {
     windowObj: window.Window | undefined = undefined;
     // ...

     aboutToAppear(): void {
       try {
         this.windowObj = (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync()
       } catch (err) {
         Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
       }

       // Obtain the PORTRAIT rotation strategy enumeration through the function selector.
       this.windowObj?.setPreferredOrientation(WindowOrientationHelper.fixed('PORTRAIT'))
         .catch((err: BusinessError) => {
           Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
         });
       // ...
     }

     // ...
     build() {
       // ...
     }
   }
   ```
3. 通过通用选择器动态选择

   若开发者在特定界面场景下所有旋转参数均需动态确定，可通过select方法，利用联合参数定义策略选择器入参实现，示例如下：

   ```typescript
   @Component
   export struct VideoDetail {
     windowObj: window.Window | undefined = undefined;
     // ...

     aboutToAppear() {
       // ...

       // Dynamically select an appropriate rotation strategy through a selector.
       this.windowObj?.setPreferredOrientation(WindowOrientationHelper.select({
         mode: 'autoRotate',
         range: 'ALL_ORIENTATIONS',
         preferred: 'UNSPECIFIED'
       }))
         .catch((err: BusinessError) => {
           Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
         });
     }

     onFullScreenChange(): void {
       if (this.isFullScreen) {
         if (this.isClick) {
           if (this.widthBp === WidthBreakpoint.WIDTH_SM || this.widthBp === WidthBreakpoint.WIDTH_LG ||
             this.heightBp === HeightBreakpoint.HEIGHT_LG) {
             // Dynamically select an appropriate rotation strategy through a selector.
             this.windowObj?.setPreferredOrientation(WindowOrientationHelper.select({
               mode: 'autoRotate',
               range: 'LANDSCAPE_ONLY'
             }))
               .catch((err: BusinessError) => {
                 Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
               });
           }
         }
       } else {
         // Dynamically select an appropriate rotation strategy through a selector.
         this.windowObj?.setPreferredOrientation(WindowOrientationHelper.select({
           mode: 'autoRotate',
           range: 'ALL_ORIENTATIONS',
           preferred: 'UNSPECIFIED'
         }))
           .catch((err: BusinessError) => {
             Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
           });
       }
     }

     private onWindowSizeChange: (windowSize: window.Size) => void = () => {
       if (this.isClick) {
         return;
       }
       if (this.widthBp === WidthBreakpoint.WIDTH_SM) {
         this.isFullScreen = false
         // Dynamically select an appropriate rotation strategy through a selector.
         this.windowObj?.setPreferredOrientation(WindowOrientationHelper.select({
           mode: 'autoRotate',
           range: 'ALL_ORIENTATIONS',
           preferred: 'UNSPECIFIED'
         }))
           .catch((err: BusinessError) => {
             Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
           });
       }

       if (this.widthBp === WidthBreakpoint.WIDTH_MD && this.heightBp === HeightBreakpoint.HEIGHT_SM) {
         this.isFullScreen = true;
       }
     };

     async aboutToDisappear() {
       // ...
       // Dynamically select an appropriate rotation strategy through a selector.
       this.windowObj?.setPreferredOrientation(WindowOrientationHelper.select({
         mode: 'autoRotate',
         range: 'ALL_ORIENTATIONS',
         preferred: 'UNSPECIFIED'
       }))
         .catch((err: BusinessError) => {
           Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
         });
       // ...
     }

     build() {
       // ...
     }

   }
   ```

   在工具类中，select方法的入参类型为OrientationConfig，根据逻辑选型分为三种子类型：自动旋转AutoRotateConfig、跟随桌面FollowDesktopConfig及固定方向FixedConfig。例如自动旋转分支，采用三层抽象的维度，需在配置中继续添加旋转范围range字段及首选方向preferred字段，以确定符合场景的窗口旋转策略。OrientationConfig类型定义如下：

   ```typescript
   /**
    * Orientation Type (used uniformly for fixed orientation and preferred orientation of auto rotation)
    */
   export type WindowOrientationType =
     | 'UNSPECIFIED' // Unspecified (lock current orientation for fixed mode, no preferred orientation for auto rotation)
       | 'PORTRAIT'
       | 'LANDSCAPE'
       | 'PORTRAIT_INVERTED'
       | 'LANDSCAPE_INVERTED';

   /**
    * Auto Rotation Range
    */
   export type AutoRotateRange =
     | 'LANDSCAPE_ONLY' // Landscape only (including forward and reverse landscape)
       | 'PORTRAIT_ONLY' // Portrait only (including forward and reverse portrait)
       | 'ALL_ORIENTATIONS'; // All orientations (support all directions)

   // ...
   /**
    * Fixed Orientation Configuration
    */
   export interface FixedConfig {
     mode: 'fixed';
     orientation?: WindowOrientationType; // Omitted or 'UNSPECIFIED' means lock current orientation
   }

   /**
    * Auto Rotation Configuration
    */
   export interface AutoRotateConfig {
     mode: 'autoRotate';
     range: AutoRotateRange; // Rotation range
     preferred?: WindowOrientationType; // Preferred orientation (valid only when range = 'ALL_ORIENTATIONS')
   }

   /**
    * Follow Desktop Configuration
    */
   export interface FollowDesktopConfig {
     mode: 'followDesktop';
   }

   /**
    * Union type of window rotation strategy configuration
    */
   export type OrientationConfig = FixedConfig | AutoRotateConfig | FollowDesktopConfig;
   ```

   上述工具类的使用示例可参考本文典型场景中的各类案例。

## 为应用配置旋转策略

为了满足灵活多变的UI交互需求，系统支持**应用级**、**窗口级**和**页面级**的窗口旋转策略配置方案，并提供**子窗口**和**悬浮窗**旋转的窗口旋转策略配置。

### 应用级配置

通过在hap包的module.json5文件中配置orientation属性，可设置应用的初始窗口旋转策略，会影响整个应用的启动方向。

该字段用于配置应用启动时的窗口显示状态。若应用需以默认的横屏或竖屏方式启动，应在字段中进行相应配置。

其支持的参数可以参考module.json5配置项中[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)下orientation的orientation枚举值。

```json
{
  "module": {
    // ...
    "abilities": [
      {
        "name": "EntryAbility",
        // ...
        "orientation": "unspecified",
        // ...
      }
    ],
    // ...
  }
}
```

应用可根据业务需求配置默认旋转策略：

* 若应用在直板机和双折叠折叠态是竖屏应用，平板和双折叠展开态是可旋转应用，推荐配置FOLLOW\_DESKTOP为默认旋转策略。
* 若应用为竖屏应用，建议配置PORTRAIT为默认旋转策略。
* 若应用为横屏应用（如MOBA类游戏），启动时默认为横屏，存在以下两种情况：
  + 仅支持横屏时，建议配置LANDSCAPE为默认旋转策略；
  + 支持横屏和反向横屏切换时，建议配置AUTO\_ROTATION\_LANDSCAPE或AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED（是否受控制中心旋转开关控制）。
* 若应用为可旋转应用，建议配置AUTO\_ROTATION\_RESTRICTED为默认旋转策略。

**说明** 

对于需要通过控制中心进行旋转锁定控制的情况，可选择字段后方带有RESTRICTED字段的旋转策略。

该字段表示旋转行为受到控制中心按钮控制：开关打开时，不随设备方向旋转；关闭时，则跟随设备旋转。

以备忘录应用为例，当系统关闭旋转锁定后，应用页面会随手机旋转自动切换横竖屏；打开旋转锁定时，则不会发生旋转行为，此时需配置为AUTO\_ROTATION\_RESTRICTED。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/wE8V4u3bQgaV142vUVb-dw/zh-cn_image_0000002693704626.png "点击放大")

### 窗口级配置

它作用于整个应用窗口（window），定义该窗口的横竖屏旋转策略，并对基于Navigation组件和Router模块实现的路由跳转均生效。一旦配置，除非显式修改，否则对窗口内所有页面生效。

1. 在onWindowStageCreate()中调用window.setPreferredOrientation()方法即可设置整个应用窗口默认方向。

```typescript
setWindowOrientation(orientation: window.Orientation): void {
  this.mainWindow.setPreferredOrientation(orientation)
    .then(() => {
      hilog.info(0x0000, 'testLog', `Succeeded in setting window orientation.`);
      // Update window orientation.
      this.mainWindowInfo.orientation = orientation;
    })
    .catch((err: BusinessError) => {
      hilog.error(0x0000, 'testLog', `Failed to set window orientation. Code: ${err.code}, message: ${err.message}`);
    });
}
```

2. 如果应用内页面的窗口旋转策略不一致，则需要执行本步骤。在页面进入时（aboutToAppear），调用window.setPreferredOrientation()定义当前页面对应的窗口旋转策略；在页面退出时（aboutToDisappear），调用window.setPreferredOrientation()恢复即将展示页面对应的窗口旋转策略。

```typescript
@StorageLink('mainWindow') mainWindow?: window.Window = undefined;
public lastOrientation?: window.Orientation;

aboutToAppear(): void {
  if (this.mainWindow === undefined) {
    return;
  }
  this.lastOrientation = this.mainWindow!.getPreferredOrientation();
  this.mainWindow!.setPreferredOrientation(window.Orientation.LANDSCAPE);
}

aboutToDisappear(): void {
  this.mainWindow!.setPreferredOrientation(this.lastOrientation)
}
```

典型场景如一些视频类应用、图片类应用等。

视频播窗横竖屏切换

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/l-ars_0UTF-kbByA_8dsdg/zh-cn_image_0000002566916979.png "点击放大")

### 页面级配置

它作用于当前显示的具体页面（NavDestination组件），仅对基于Navigation组件实现的路由跳转生效。它允许根据业务需求动态调整不同页面的窗口旋转策略。在页面路由跳转时，系统自动切换为下一个展示页面对应的窗口旋转策略。

NavDestination组件提供[preferredOrientation](../harmonyos-references/ts-basic-components-navdestination.md#preferredorientation19)属性，支持每个页面独立配置窗口旋转策略，互相不影响。页面跳转时，窗口旋转策略自动更新为下一个页面对应的preferredOrientation。页面返回时，窗口旋转策略也会自动更新为上一个页面对应的preferredOrientation。

### 方案对比

| 窗口旋转策略配置方案 | 优势 | 劣势 | 推荐使用场景 |
| --- | --- | --- | --- |
| 应用级 | * 可设置应用启动的初始方向 * 应用所有页面窗口旋转策略一致时仅需配置一次 | 应用内页面窗口旋转策略不一致时，无法切换，需要配合窗口级或页面级窗口旋转策略 | * 应用需要设置启动的初始方向。 * 应用所有页面窗口旋转策略一致。 |
| 窗口级 | * 配置后同一窗口内所有页面生效 * 支持Navigation组件与Router模块实现的路由 * 版本兼容性高（API9+） | 页面窗口旋转策略不一致时，需要在页面进入及退出时设置两次窗口旋转策略。 | * 使用Router模块实现页面路由 * 应用基于API19之前的版本开发 |
| 页面级 | * 单独配置每个页面的窗口旋转策略，页面跳转时窗口旋转策略跟随自动更新 * 针对页面配置窗口旋转策略，使用更简单、更灵活 | * 版本兼容性有限（API19+） * 仅支持Navigation组件实现的页面路由 | * 应用内页面的窗口旋转策略多处不一致 * 基于Navigation模块实现页面路由 * 应用基于API19之后的版本开发 |

### 应用子窗口的旋转

在应用旋转场景中，应用主窗的尺寸由系统控制，而应用子窗的尺寸和位置由应用控制。因此，建议应用开发者在有应用子窗的旋转场景中，同步调整应用子窗的尺寸和位置，避免因旋转过程中应用子窗的尺寸和位置保持不变而导致如下图所示的应用子窗显示截断问题（直板机默认的旋转策略为UNSPECIFIED，旋转锁定按钮关闭的情况下不允许应用旋转，可以通过module.json5配置文件中abilities标签的"orientation"字段配置应用的旋转策略为AUTO\_ROTATION，使应用跟随设备方向旋转）。

| 旋转前竖屏显示 | 旋转后横屏显示（调整前） |
| --- | --- |
|  |  |

**实现方案**

系统为设备窗口尺寸变化监听、设置应用子窗尺寸和位置提供了如下接口：

1. [on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)接口用于开启窗口尺寸变化的监听，当窗口发生旋转后，会触发其中的回调。
2. [resize()](../harmonyos-references/arkts-apis-window-window.md#resize9)接口用于改变当前窗口的大小，可以在窗口发生旋转后及时调整子窗的宽高。
3. [moveWindowTo()](../harmonyos-references/arkts-apis-window-window.md#movewindowto9)接口用于移动窗口位置，可以在窗口发生旋转后及时调整子窗的位置。

为实现根据应用旋转方向设置应用子窗尺寸，开发者可使用on('windowSizeChange')接口监听窗口尺寸的变化，并在回调函数中通过resize()接口和moveWindowTo()接口分别调整应用子窗的尺寸和位置。

需要指出的是，开发者可以使用[setFollowParentWindowLayoutEnabled()](../harmonyos-references/arkts-apis-window-window.md#setfollowparentwindowlayoutenabled17)接口设置子窗或模态窗口的布局信息是否跟随主窗，如果设置为跟随主窗，那么子窗的旋转便不再需要额外适配。

```typescript
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const SUB_WINDOW_LEFT_OFFSET: number = 50;
const SUB_WINDOW_TOP_OFFSET: number = 500;
const TAG: string = 'subWindowAdaptWhenRotate';
const DOMAIN: number = 0x0000;

@Entry
@Component
struct Index {
  public mainWindow: window.Window | undefined = undefined;
  public subWindow: window.Window | undefined = undefined;

  aboutToAppear(): void {
    // create subWindow
    this.createSubWindow();

    this.mainWindow = AppStorage.get('mainWindow');
    if (!this.mainWindow) {
      return;
    }
    this.mainWindow.on('windowSizeChange', () => {
      this.adjustSubwindowSizeAndPosition();
    })
  }

  private adjustSubwindowSizeAndPosition(): void {
    if (!this.subWindow) {
      hilog.error(DOMAIN, TAG, 'subWindow is null');
      return;
    }
    let subwindowRect: window.Rect | null = null;
    try {
      subwindowRect = this.subWindow.getWindowProperties().windowRect;
    } catch (error) {
      hilog.warn(0x000, 'testTag', `getWindowProperties failed, code: ${error.code}, message: ${error.message}`);
    }
    let newWidth: number = subwindowRect!.height;
    let newHeight: number = subwindowRect!.width;
    let newX: number = subwindowRect!.top;
    let newY: number = subwindowRect!.left;
    this.subWindow.resize(newWidth, newHeight)
      .then(() => {
        hilog.info(DOMAIN, TAG, 'Succeeded in changing the window size')
      }).catch((err: BusinessError) => {
      hilog.error(DOMAIN, TAG, `Failed to change the window size. Cause code: ${err.code}, message: ${err.message}`);
    });

    this.subWindow.moveWindowTo(newX, newY)
      .then(() => {
        hilog.info(DOMAIN, TAG, 'Succeeded in moving the window');
      }).catch((err: BusinessError) => {
      hilog.error(DOMAIN, TAG, `Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
    });

  }

  // ...
}
```

**实现效果**

根据示例代码为不同旋转方向设置不同的应用子窗尺寸和位置的实际效果如下图所示，应用子窗的尺寸和位置在竖屏显示和横屏显示下是不同的。

| 旋转前竖屏显示 | 旋转后横屏显示 |
| --- | --- |
|  |  |

### 悬浮窗的旋转

悬浮窗默认是竖向的，但是对于横向游戏和视频应用，横向的悬浮窗体验会更好。开发者可以通过在module.json5配置文件中abilities标签下的preferMultiWindowOrientation属性增加“landscape”或者“landscape\_auto”，配合API以声明应用支持横向悬浮窗或上下分屏模式。

```json
{
  "module": {
    // ...
    "abilities": [
      {
        "name": "EntryAbility",
        // ...
        "preferMultiWindowOrientation": "landscape_auto",
        // ...
      }
    ],
    // ...
  }
}
```

该场景下多窗布局动态可变为横向，需要配合API（[enableLandscapeMultiWindow()](../harmonyos-references/arkts-apis-window-window.md#enablelandscapemultiwindow12)/ [disableLandscapeMultiWindow()](../harmonyos-references/arkts-apis-window-window.md#disablelandscapemultiwindow12)）使用。

```typescript
private windowClass = (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync()

aboutToAppear(): void {
  this.windowClass.enableLandscapeMultiWindow();
}

aboutToDisappear(): void {
  this.windowClass.disableLandscapeMultiWindow();
}
```

例如：视频或者游戏类应用在横屏模式下开启悬浮窗后，页面没有适配横屏，导致内容显示不全或者观看体验不好。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/9e9d6RpeQ5O_rWh7EymfqA/zh-cn_image_0000002566757003.gif "点击放大")

优化后效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/DXLcx6pvSzOAv9t0f__YSg/zh-cn_image_0000002535837220.gif "点击放大")

## 为多设备配置旋转策略

随着设备的多样化，应用某些页面需要根据设备类型配置不同的窗口旋转策略以达到较好的用户体验，为了开发者能快速适配不同设备，我们提供了多设备的窗口旋转策略。

### 背景

1. 不同设备对旋转策略的使用约束不同

   下述特定场景下，由于产品定义与使用场景的不同，开发者自定义的窗口旋转策略可能会显著降低用户体验，因此系统配置的窗口旋转策略优先级会高于应用配置。此时，应用实际显示的窗口方向将由系统统一调度，开发者自定义的窗口旋转策略将被覆盖而不生效。

   | 设备场景 | Pura X折叠态 | 电脑 | 智慧屏 | 智能穿戴 |
   | --- | --- | --- | --- | --- |
   | 特定显示方向 | 跟随屏幕方向显示 | | | |
   | 效果图 |  |  |  |  |
2. 不同交互场景对旋转策略的使用约束不同

   例如下述场景中，自由多窗不支持竖屏模式，悬浮窗默认是竖向的，但是但是对于横向游戏和视频应用，横向的悬浮窗体验会更好。

   | 使用场景 | 分屏 | 全景多窗 | 自由多窗 | 全局批注 | 任务列表视图 |
   | --- | --- | --- | --- | --- | --- |
   | 特定显示方向 | 跟随传感器自动旋转，可以旋转到竖屏、横屏、反向竖屏、反向横屏四个方向，且受控制中心的旋转开关控制 | | 跟随屏幕方向显示 | 手写笔点击全局批注后，锁定当前窗口方向 | 锁定当前窗口方向 |
   | 效果图 |  |  |  |  |  |
3. 相同的页面，开发者希望在不同的设备上，应用不同的旋转策略。例如：视频详情页应用在直板机上默认只能竖向，而在折叠屏展开态则希望能四个方向自由旋转。
4. 由于设备的形态差异，应用在不同的设备上也希望有不同的启动方向。

### 跟随桌面的旋转策略

当前HarmonyOS主流设备桌面的横竖屏旋转策略如下表所示：

| 产品类型 | 手机 | 阔折（Pura X系列） | 大阔折（Pura X MAX系列） | 双折叠（Mate X系列） | 三折叠（Mate XT系列） | 平板 | 电脑 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 是否支持横竖屏旋转 | 不支持 | 内屏：不支持  外屏：不支持 | 内屏：支持  外屏：不支持 | 内屏：支持  外屏：不支持 | F态（单屏显示）：不支持  M态（双屏显示）：支持  G态（三屏显示）：支持 | 支持 | 应用无法配置窗口旋转策略 |

对于某些应用，在直板手机上默认采用竖屏显示策略，但在平板或折叠屏设备上，需支持自动旋转。若在Ability的生命周期中调用setPreferredOrientation，可能会导致应用启动时出现旋转动画。因此，可通过修改module.json5配置文件中的orientation属性，设置为FOLLOW\_DESKTOP，以跟随桌面的旋转模式。

### 实现响应式旋转策略

在设备切换形态时，有时应用对于相同页面希望采用不同的旋转策略，这时需要通过监听设备的窗口尺寸变化配合系统断点实现响应式旋转策略，至于断点与设备的映射关系，请先了解[响应式布局](bpta-multi-device-responsive-layout.md)。

1.在应用EntryAbility的onWindowStageCreate生命周期中，通过on('windowSizeChange')方法监听窗口尺寸变化，在其回调中通过getWindowWidthBreakpoint()及getWindowHeightBreakpoint()实时获取并存储横竖断点变化信息，配合各个页面实现响应式旋转策略。

```typescript
export default class EntryAbility extends UIAbility {
  uiContext?: UIContext;
  onWindowSizeChange: (windowSize: window.Size) => void = () => {
    let widthBp: WidthBreakpoint = this.uiContext!.getWindowWidthBreakpoint();
    AppStorage.setOrCreate(CommonConstants.WIDTH_BREAK_POINT, widthBp);
    let heightBp: HeightBreakpoint = this.uiContext!.getWindowHeightBreakpoint();
    AppStorage.setOrCreate(CommonConstants.HEIGHT_BREAK_POINT, heightBp);
  }

  // ...

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // ...

    windowStage.loadContent('pages/Index', (err) => {
      // ...

      windowStage.getMainWindow().then((data: window.Window) => {
        try {
          this.uiContext = data.getUIContext();
        } catch (err) {
          Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
        }

        let widthBp: WidthBreakpoint = this.uiContext!.getWindowWidthBreakpoint();
        AppStorage.setOrCreate(CommonConstants.WIDTH_BREAK_POINT, widthBp);

        let heightBp: HeightBreakpoint = this.uiContext!.getWindowHeightBreakpoint();
        AppStorage.setOrCreate(CommonConstants.HEIGHT_BREAK_POINT, heightBp);

        data.on('windowSizeChange', this.onWindowSizeChange);
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', `Error occured, error code: ${err.code}, error message: ${err.message}`);
      })

    });
  }

  // ...
}
```

2.在需要实现响应式旋转策略页面的aboutToAppear生命周期中，通过on('windowSizeChange')方法监听窗口尺寸变化，在其回调中实时获取设备的窗口尺寸变化信息。

```typescript
@Component
export struct VideoDetail {
  windowObj: window.Window | undefined = undefined;
  // ...

  aboutToAppear() {
    try {
      this.windowObj = (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync()
    } catch (err) {
      Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
    }

    // ...
    this.windowObj?.on('windowSizeChange', this.onWindowSizeChange);

    // ...
  }
  // ...
}
```

并在aboutToDisappear中取消监听：

```typescript
async aboutToDisappear() {
  // ...
  this.windowObj?.off('windowSizeChange')
}
```

3.在页面windowSizeChange回调方法中，配合全局横竖断点变化，保证页面切换时不同设备上配置合适的窗口旋转策略。

```typescript
@Component
export struct VideoDetail {
  // ...
  @StorageLink(CommonConstants.WIDTH_BREAK_POINT) widthBp: WidthBreakpoint = WidthBreakpoint.WIDTH_SM;
  @StorageLink(CommonConstants.HEIGHT_BREAK_POINT) heightBp: HeightBreakpoint = HeightBreakpoint.HEIGHT_SM;
  // ...

  // ...

  private onWindowSizeChange: (windowSize: window.Size) => void = () => {
    if (this.isClick) {
      return;
    }
    if (this.widthBp === WidthBreakpoint.WIDTH_SM) {
      this.isFullScreen = false
      // Dynamically select an appropriate rotation strategy through a selector.
      this.windowObj?.setPreferredOrientation(WindowOrientationHelper.select({
        mode: 'autoRotate',
        range: 'ALL_ORIENTATIONS',
        preferred: 'UNSPECIFIED'
      }))
        .catch((err: BusinessError) => {
          Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
        });
    }

    if (this.widthBp === WidthBreakpoint.WIDTH_MD && this.heightBp === HeightBreakpoint.HEIGHT_SM) {
      this.isFullScreen = true;
    }
  };

  // ...

  build() {
    // ...
}
```

在折叠屏设备上，通过display.on('foldStatusChange', callback())方法监听折叠的状态，并通过@StorageLink('isHalfFolded')保存并实时更新全局变量。

```typescript
@Component
export struct VideoPlayer {
  // ...
  @StorageLink('isHalfFolded') isHalfFolded: boolean = false;
  // ...
  private onFoldStatusChange: Callback<display.FoldStatus> = (data: display.FoldStatus) => {
    this.foldStatus = data;
    if (canIUse('SystemCapability.Window.SessionManager')) {
      if (data === display.FoldStatus.FOLD_STATUS_EXPANDED || data === display.FoldStatus.FOLD_STATUS_FOLDED ||
        data === display.FoldStatus.FOLD_STATUS_EXPANDED_WITH_SECOND_EXPANDED ||
        data === display.FoldStatus.FOLD_STATUS_FOLDED_WITH_SECOND_EXPANDED) {
        let widthBp: WidthBreakpoint = this.getUIContext().getWindowWidthBreakpoint();
        AppStorage.setOrCreate(CommonConstants.WIDTH_BREAK_POINT, widthBp);
        let heightBp: HeightBreakpoint = this.getUIContext().getWindowHeightBreakpoint();
        AppStorage.setOrCreate(CommonConstants.HEIGHT_BREAK_POINT, heightBp);
      }
      if (data === display.FoldStatus.FOLD_STATUS_FOLDED_WITH_SECOND_EXPANDED && this.isFullScreen) {
        this.windowObj?.setPreferredOrientation(window.Orientation.AUTO_ROTATION_LANDSCAPE_RESTRICTED)
          .catch((err: BusinessError) => {
            Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
          });
      } else {
        this.windowObj?.setPreferredOrientation(window.Orientation.AUTO_ROTATION_UNSPECIFIED)
          .catch((err: BusinessError) => {
            Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
          });
      }
    }
  };

  aboutToAppear(): void {
    // ...
    if (canIUse('SystemCapability.Window.SessionManager')) {
      try {
        display.on('foldStatusChange', this.onFoldStatusChange);
      } catch (error) {
        let err = error as BusinessError;
        Logger.error('VideoPlayer', `onFoldStatusChange failed, code = ${err.code}, message = ${err.message}`);
      }
    }
  }
  // ...

  build() {
    // ...
}
```

## 优化横竖屏切换性能

在窗口旋转时，屏幕尺寸变化会导致界面重新布局。为提高横竖屏切换的流畅度，需进行性能优化。

**使用自定义组件冻结**

旋转时，由于整窗一起旋转，会导致页面重新布局，但是实际上需要展示的可能只有播放内容，对于其他的组件可以使用自定义组件冻结功能，避免由于旋转导致的UI更新操作。例如视频播放底下的详情内容，可能是单独的组件。

```typescript
@Component({ freezeWhenInactive: true })
  // Added custom component freezing function
struct VideoDetailView {
  build() {
    Scroll() {
      // ...
    }
  }
}
```

**对图片使用autoResize**

如果当前旋转页面存在一些图片，未经合理的裁剪，图片过大，可以对图片设置autoResize属性，使图片裁剪到合适的大小进行绘制。该属性是将组件显示区域作为绘制的图源尺寸，以减少内存占用。例如原图是1920px\*1080px，但是显示区域是200vp\*100vp，则在解码时会降低采样编码到200vp\*100vp尺寸。

```typescript
@Builder
function ImageItem(imageSrc: ResourceStr) {
  Stack({}) {
    Image(imageSrc)
      .width('100%')
      .height('100%')
      .autoResize(true)// Use auto_resize attributes on images
      .borderRadius(8)
      .objectFit(ImageFit.Fill)
      .backgroundColor('#1AFFFFFF')
  }
}
```

**排查一些耗时操作**

排查当前页面是否存在冗余的OnAreaChange事件、blur模糊属性或linearGradient属性，这些属性较为耗时，应根据是否必须使用来决定是否进行优化。

## 使用多设备工具模块设置窗口旋转策略

### 模块简介

在 HarmonyOS 应用开发中，系统提供了多种窗口旋转策略（详情请参考[了解窗口旋转策略](bpta-multi-device-window-direction.md#section7778165616124)），涵盖了固定方向、自动旋转、跟随桌面等多种模式。策略枚举数量多且分类复杂，开发者在不同业务场景下需反复查阅文档进行选型；在多设备（直板机、折叠屏、平板等）适配时，需针对各设备使用场景单独实现适配逻辑，缺乏统一的封装与动态适配能力，导致代码复杂度高、难以维护与复用。

多设备工具模块的设计初衷是为了解决上述痛点。它内置了20种常见页面类型的预设窗口策略配置，将复杂的代码逻辑判断抽象为简洁的配置声明，开发者仅需传入对应的页面类型，即可利用模块完成窗口策略的解析与应用。同时，模块提供了响应式规则引擎，支持根据设备形态动态匹配窗口策略配置，实现一次配置、多设备自适应。

下图展示了应用层、多设备工具模块与系统层之间的整体协作流程：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/SBrTj0YCQA2btRlW1IeQcA/zh-cn_image_0000002693534420.png "点击放大")

**响应式规则引擎**（responsiverule目录模块）

响应式规则引擎模块的核心是通过内部的一系列规则动态匹配窗口旋转策略。

**窗口策略控制**（orientation目录模块）

窗口策略控制模块负责将解析后的方向配置应用到系统窗口。其中，OrientationStrategy提供从抽象配置到系统枚举的映射逻辑，支持fixed，autoRotate、followDesktop三种模式；presets提供了开箱即用的20种常见页面类型预设方向配置。

**协作关系**

窗口策略控制中的预设或自定义配置提供选择内容，规则引擎决定匹配方式，窗口策略控制中的OrientationStrategy负责应用生效。开发者只需将设备上下文及预设或自定义配置传给响应式规则引擎，响应式规则引擎会根据窗口形态、设备形态、折叠状态等变化动态匹配返回一个窗口策略配置值，OrientationStrategy模块将此返回值映射为对应的系统窗口旋转策略。

### 响应式规则引擎

在多设备适配场景中，同一个页面在不同设备形态下往往需要采用不同的窗口旋转策略。传统做法需要在每个页面中手动实现条件判断逻辑，根据设备尺寸和宽高比进行窗口旋转策略适配，代码分散且难以维护。响应式规则引擎将这类条件判断抽象为声明式的规则配置——开发者只需描述"在什么条件下使用什么策略"，引擎在运行时根据实际的设备上下文自动求值并返回匹配的配置，消除了手写条件分支的繁琐工作。

**规则结构**

规则引擎的核心数据结构由三层组成：

| 层级 | 类型 | 说明 |
| --- | --- | --- |
| 条件 | Condition | 由字段名 field、运算符 operator、比较值 value 组成，一个完整的Condition如：  { field: 'windowWidthVp', operator: EQUAL, value: 600 }，代表的条件为“窗口宽度的vp值是否等于600”。 |
| 规则 | Rule<T> | 一组条件的 AND 组合（conditions: Condition[]），全部满足时命中，返回对应的 value: T，一个完整的Rule<number>如：{conditions: [{ field: 'windowWidthVp', operator: GREATER\_THAN\_OR\_EQUAL, value: 600 },{ field: 'windowWidthVp', operator: LESS\_THAN, value: 840 }],value: 2}，代表的条件为“当窗口宽度的vp值大于等于600且小于840时，返回数值2”。 |
| 响应式值 | ConditionResponsiveValue<T> | 顶层容器，包含规则列表 rules: Rule<T>[] 和兜底默认值 defaultValue: T。 |

**运算符**

引擎内置多种operator运算符，按使用场景可分为以下四类：

* 数值比较：

| 运算符 | 含义 |
| --- | --- |
| EQUAL | 等于 |
| NOT\_EQUAL | 不等于 |
| GREATER\_THAN | 大于 |
| GREATER\_THAN\_OR\_EQUAL | 大于等于 |
| LESS\_THAN | 小于 |
| LESS\_THAN\_OR\_EQUAL | 小于等于 |

* 区间判断：

| 运算符 | 含义 |
| --- | --- |
| BETWEEN | 闭区间 |
| BETWEEN\_LEFT\_OPEN | 左开区间 |
| BETWEEN\_RIGHT\_OPEN | 右开区间 |
| BETWEEN\_OPEN | 开区间 |
| NOT\_BETWEEN | 不在区间内 |

* 字符串匹配**：**

| 运算符 | 含义 |
| --- | --- |
| CONTAINS | 包含子串 |
| NOT\_CONTAINS | 不包含子串 |
| STARTS\_WITH | 以...开头 |
| ENDS\_WITH | 以...结尾 |
| MATCHES | 正则匹配（条件值为正则表达式字符串） |

* 集合运算：

| 运算符 | 含义 |
| --- | --- |
| IN | 在集合中 |
| NOT\_IN | 不在集合中（同上取反） |

**求值流程**

ResponsiveValueResolver.getValue(context: Object | undefined, responsiveValue: ResponsiveValue<T>) 是引擎的求值入口，其内部流程可总结为如下四点：

1. 短路匹配：规则按 Rules 数组顺序求值，首条全部条件命中的规则立即返回，后续规则不再执行。
2. AND 语义：同一条规则内的多个条件必须全部满足，任一条件失败则整条规则跳过。
3. 类型安全：引擎在求值前进行运行时类型检查，类型不匹配时输出警告并回退到defaultValue，而非静默失败。
4. 兜底保障：无论context是否完整、规则是否匹配，始终有defaultValue作为最终结果返回，保证不中断业务流程。

```typescript
export class ResponsiveValueResolver {
  // Evaluate rules against the developer-defined Context.
  // Returns the first matching rule's value, or defaultValue when none match.
  // Context is typed as Object so the developer can pass their own context class.
  static getValue<T>(context: Object | undefined, responsiveValue: ResponsiveValue<T>): T | undefined {
    if (!responsiveValue) {
      return undefined;
    }

    if (!context) {
      return responsiveValue.defaultValue;
    }

    const ctxRecord: Record<string, ConditionValue> = context as Object as Record<string, ConditionValue>;

    for (let i = 0; i < responsiveValue.rules.length; i++) {
      const rule: Rule<T> = responsiveValue.rules[i];
      let allMatch = true;
      for (let j = 0; j < rule.conditions.length; j++) {
        const condition: Condition = rule.conditions[j];
        const ctxValue: ConditionValue | undefined = ctxRecord[condition.field];

        if (ctxValue === undefined) {
          Logger.warn(
            `[ResponsiveValueResolver] field '${condition.field}' not in context, rule will fall back to defaultValue`);
          allMatch = false;
          break;
        }

        if (!ResponsiveValueResolver.isConditionValue(ctxValue as Object)) {
          Logger.warn(
            `[ResponsiveValueResolver] field '${condition.field}' value is not a valid ConditionValue ` +
            `(string|number|boolean|array of them), rule will fall back to defaultValue`);
          allMatch = false;
          break;
        }

        const predicate: Predicate = OPERATOR_PREDICATES[condition.operator];
        if (!predicate) {
          Logger.warn(`[ResponsiveValueResolver] Unknown operator: ${condition.operator}`);
          allMatch = false;
          break;
        }
        if (!ResponsiveValueResolver.areTypesCompatible(condition.operator, ctxValue, condition.value)) {
          Logger.warn(
            `[ResponsiveValueResolver] type mismatch for field '${condition.field}':` +
            ` operator '${condition.operator}' is incompatible with context value and condition value types,` +
            ` rule will fall back to defaultValue`);
          allMatch = false;
          break;
        }
        if (!predicate(ctxValue, condition.value)) {
          allMatch = false;
          break;
        }
      }

      if (allMatch) {
        return rule.value;
      }
    }

    return responsiveValue.defaultValue;
  }

  // Validate that a context field value conforms to ConditionValue at runtime,
  // guarding against unsafe casts when a developer passes a custom context object.
  private static isConditionValue(value: Object): boolean {
    // ...
  }

  // Ensure the runtime types of ctxValue and condValue are compatible with the
  // operator before invoking the predicate, so mismatches are reported instead
  // of silently making a rule fail to match.
  private static areTypesCompatible(operator: Operator, ctxValue: ConditionValue, condValue: ConditionValue): boolean {
    // ...
  }
}
```

**横向视频全屏播放场景的窗口策略规则代码示例**

长视频应用的横向视频全屏视频播放页配置了完整的条件规则，是理解规则引擎的最佳切入点。横向视频在全屏播放时，不同设备形态需要不同的旋转策略，对应的预设配置定义如下：

```typescript
export class ResponsiveOrientationConfig {
  // ...
  private static getLandscapeVideoFullscreenConfigData(): ConditionResponsiveValue<OrientationConfig> {
    return {
      rules: [
        {
          conditions: [
            { field: 'displayLongEdgeVp', operator: Operator.GREATER_THAN_OR_EQUAL,
              value: LANDSCAPE_FULLSCREEN_LONG_EDGE_MIN },
            { field: 'displayLongEdgeVp', operator: Operator.LESS_THAN,
              value: LANDSCAPE_FULLSCREEN_LONG_EDGE_MID },
            { field: 'displayLongShortRatio', operator: Operator.GREATER_THAN_OR_EQUAL,
              value: LANDSCAPE_FULLSCREEN_RATIO_BAND_1 }
          ],
          value: { mode: 'autoRotate', range: AutoRotateRange.LANDSCAPE_ONLY }
        },
        {
          conditions: [
            { field: 'displayLongEdgeVp', operator: Operator.GREATER_THAN_OR_EQUAL,
              value: LANDSCAPE_FULLSCREEN_LONG_EDGE_MID },
            { field: 'displayLongEdgeVp', operator: Operator.LESS_THAN,
              value: LANDSCAPE_FULLSCREEN_LONG_EDGE_MAX },
            { field: 'displayLongShortRatio', operator: Operator.GREATER_THAN_OR_EQUAL,
              value: LANDSCAPE_FULLSCREEN_RATIO_BAND_2 }
          ],
          value: { mode: 'autoRotate', range: AutoRotateRange.LANDSCAPE_ONLY }
        }
      ],
      defaultValue: { mode: 'autoRotate', range: AutoRotateRange.ALL_ORIENTATIONS }
    };
  }
}
```

不同设备下的匹配结果：

| 设备形态 | 设备长边 (vp) | 设备长宽比 | 命中规则 | 最终策略 |
| --- | --- | --- | --- | --- |
| 直板机 | 600~840 | 1.25 | 规则1 | 仅横屏旋转 |
| 窄长直板机（以Pocket2为例） | 861 | 2.36 | 规则2 | 仅横屏旋转 |
| 双折叠折叠态（以Mate X5为例） | 801 | 2.32 | 规则1 | 仅横屏旋转 |
| 双折叠展开态（以Mate X5为例） | 798 | 1.12 | 无命中规则 | 全方向自由旋转 |
| Pura X Max折叠态 | 672 | 1.46 | 规则1 | 仅横屏旋转 |
| Pura X Max展开态 | 939 | 1.41 | 无命中规则 | 全方向自由旋转 |
| 三折叠G态（以Mate XT为例） | 1107 | 1.42 | 无命中默认 | 全方向自由旋转 |
| 平板 | 1600 | 1.6 | 无命中默认 | 全方向自由旋转 |

当前工具模块对部分高频场景进行了预设配置，开发者调用ResponsiveOrientationConfig.getConfig()并传入PageType的场景枚举后获取响应式方向配置OrientationConfig，再调用OrientationStrategy.resolveResponsive()方法（方法实现参考下方章节）并传入OrientationConfig后，引擎自动完成求值，从而提升选型效率，使用方式如下：

```typescript
aboutToAppear() {
  // ...

  const config: ConditionResponsiveValue<OrientationConfig> =
    ResponsiveOrientationConfig.getConfig(PageType.LONG_VIDEO);
  try {
    this.windowObj?.setPreferredOrientation(
      OrientationStrategy.resolveResponsive(globalThis.context, config));
  } catch (err) {
    const error = err as BusinessError;
    Logger.error('VideoDetail', `setPreferredOrientation failed, code: ${error.code}, message: ${error.message}`);
  }
}
```

### Orientation窗口策略控制

Orientation窗口策略控制将开发者声明的抽象配置映射为系统 window.Orientation 枚举值。开发者只需关注三种模式的配置方式与适用场景，无需记忆底层所有的系统枚举。

**方向配置类型**

在了解策略映射之前，先看模块定义的三种方向配置类型。它们构成了一个联合类型，通过 mode 字段区分：

```typescript
// Physical orientation, used for fixed orientation and auto-rotate preferred.
export enum OrientationType {
  UNSPECIFIED = 'UNSPECIFIED',
  PORTRAIT = 'PORTRAIT',
  LANDSCAPE = 'LANDSCAPE',
  PORTRAIT_INVERTED = 'PORTRAIT_INVERTED',
  LANDSCAPE_INVERTED = 'LANDSCAPE_INVERTED',
}

// Allowed auto-rotation range.
export enum AutoRotateRange {
  LANDSCAPE_ONLY = 'LANDSCAPE_ONLY',
  PORTRAIT_ONLY = 'PORTRAIT_ONLY',
  ALL_ORIENTATIONS = 'ALL_ORIENTATIONS',
}

export interface FixedConfig {
  mode: 'fixed';
  orientation?: OrientationType;
}

export interface AutoRotateConfig {
  mode: 'autoRotate';
  range: AutoRotateRange;
  preferred?: OrientationType;
}

export interface FollowDesktopConfig {
  mode: 'followDesktop';
}

export type OrientationConfig = FixedConfig | AutoRotateConfig | FollowDesktopConfig;
```

**OrientationStrategy：策略映射**

OrientationStrategy 是窗口策略控制的核心，提供了一系列静态方法将响应式规则引擎返回的OrientationConfig转换为系统的window.Orientation，通过调用setPreferredOrientation()方法将匹配的窗口旋转策略应用到当前窗口。

OrientationStrategy的三种模式如下：

1. fixed（固定方向策略**）**：

   固定方向策略将窗口锁定在指定方向，不随设备物理旋转而改变。

   | 配置 orientation 参数 | 映射到 window.Orientation | 行为说明 |
   | --- | --- | --- |
   | UNSPECIFIED | LOCKED | 锁定当前屏幕方向，不跟随传感器旋转 |
   | PORTRAIT | PORTRAIT | 锁定竖屏 |
   | LANDSCAPE | LANDSCAPE | 锁定横屏 |
   | PORTRAIT\_INVERTED | PORTRAIT\_INVERTED | 锁定反向竖屏 |
   | LANDSCAPE\_INVERTED | LANDSCAPE\_INVERTED | 锁定反向横屏 |

   适用场景：

   * 需要保持进入页面时方向的场景，使用 fixed() 锁定当前方向。
   * 自定义响应式规则引擎时，直板机场景使用fixed(OrientationType.PORTRAIT)锁定仅竖屏。
2. autoRotate（自动旋转策略）

   自动旋转策略允许窗口跟随设备物理方向自动旋转，并受控制中心"旋转锁定"开关控制。通过 range 参数限定可旋转的方向范围，通过可选的 preferred 参数指定首次应用时的首选方向。

   | 配置 | 映射到 window.Orientation | 行为说明 |
   | --- | --- | --- |
   | range: LANDSCAPE\_ONLY | AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED | 仅横屏和反向横屏之间旋转，受开关控制 |
   | range: PORTRAIT\_ONLY | AUTO\_ROTATION\_PORTRAIT\_RESTRICTED | 仅竖屏和反向竖屏之间旋转，受开关控制 |
   | range: ALL\_ORIENTATIONS 无首选 | AUTO\_ROTATION\_UNSPECIFIED | 全方向旋转，可旋转方向由系统根据设备形态判定，受开关控制 |
   | range: ALL\_ORIENTATIONS + preferred: PORTRAIT | USER\_ROTATION\_PORTRAIT | 调用时临时切换到竖屏，之后全方向跟随传感器旋转，受开关控制 |
   | range: ALL\_ORIENTATIONS + preferred: LANDSCAPE | USER\_ROTATION\_LANDSCAPE | 调用时临时切换到横屏，之后全方向跟随传感器旋转，受开关控制 |
   | range: ALL\_ORIENTATIONS + preferred: PORTRAIT\_INVERTED | USER\_ROTATION\_PORTRAIT\_INVERTED | 调用时临时切换到反向竖屏，之后全方向跟随传感器旋转 |
   | range: ALL\_ORIENTATIONS + preferred: LANDSCAPE\_INVERTED | USER\_ROTATION\_LANDSCAPE\_INVERTED | 调用时临时切换到反向横屏，之后全方向跟随传感器旋转 |

   适用场景：

   * 长视频详情页 / 图库应用：autoRotate(AutoRotationRange.ALL\_ORIENTATIONS)，全方向自由旋转。
   * 竖屏游戏（也支持反向竖屏）：autoRotate(AutoRotationRange.PORTRAIT\_ONLY)，仅竖向旋转。
3. followDesktop（跟随桌面策略）

   跟随桌面策略将旋转行为完全委托给系统桌面，应用窗口的方向随桌面方向自动变化。

   | 配置 | 映射到 window.Orientation |
   | --- | --- |
   | followDesktop | FOLLOW\_DESKTOP |

   适用场景：

   * 应用首页，需要在不同设备上有差异化旋转行为。
   * 社交、购物、阅读等以竖屏为主但在大屏设备上允许旋转的通用页面。
   * 希望一次配置自动适配所有设备旋转策略的场景。

OrientationStrategy的核心静态方法resolveResponsive如下：

```typescript
export class OrientationStrategy {
  // ...

  private static resolveUserRotation(preferred?: OrientationType): window.Orientation {
    if (!preferred || preferred === OrientationType.UNSPECIFIED) {
      return window.Orientation.AUTO_ROTATION_UNSPECIFIED;
    }
    switch (preferred) {
      case OrientationType.PORTRAIT:
        return window.Orientation.USER_ROTATION_PORTRAIT;
      case OrientationType.LANDSCAPE:
        return window.Orientation.USER_ROTATION_LANDSCAPE;
      case OrientationType.PORTRAIT_INVERTED:
        return window.Orientation.USER_ROTATION_PORTRAIT_INVERTED;
      case OrientationType.LANDSCAPE_INVERTED:
        return window.Orientation.USER_ROTATION_LANDSCAPE_INVERTED;
      default:
        return window.Orientation.AUTO_ROTATION_UNSPECIFIED;
    }
  }

  static resolve(config: OrientationConfig): window.Orientation {
    switch (config.mode) {
      case 'followDesktop':
        return OrientationStrategy.followDesktop();
      case 'fixed':
        return OrientationStrategy.fixed(config.orientation);
      case 'autoRotate':
        return OrientationStrategy.autoRotate(config.range, config.preferred);
      default:
        return window.Orientation.AUTO_ROTATION_UNSPECIFIED;
    }
  }

  static resolveResponsive(
    context: Object | undefined,
    responsiveValue: ResponsiveValue<OrientationConfig>
  ): window.Orientation {
    const config: OrientationConfig | undefined =
      ResponsiveValueResolver.getValue<OrientationConfig>(context, responsiveValue);
    if (!config) {
      return window.Orientation.UNSPECIFIED;
    }
    return OrientationStrategy.resolve(config);
  }
}
```

### 工具模块的使用

前面三章分别介绍了模块的整体架构、响应式规则引擎和窗口策略控制。本章将这三部分串联起来，完整展示从添加依赖、初始化上下文、到页面中应用窗口旋转策略的完整开发流程。

**添加依赖**

在模块的 oh-package.json5 中添加对 multidevicelibrary 的依赖：

```json
{
  "name": "default",
  "version": "1.0.0",
  "description": "Please describe the basic information.",
  "main": "",
  "author": "",
  "license": "",
  "dependencies": {
    "base": "file:../../commons/base",
    "multidevicelibrary": "file:../../commons/multidevicelibrary",
    "home": "file:../../features/home",
    "portrait": "file:../../features/portrait",
    "landscape": "file:../../features/landscape",
    "photos": "file:../../features/photos",
    "stock": "file:../../features/stock",
    "longvideo": "file:../../features/longvideo",
    "shortvideo": "file:../../features/shortvideo",
    "hovervideo": "file:../../features/hovervideo"
  }
}
```

**定义响应式上下文**

在使用工具模块之前，需要先定义设备上下文类，用于承载运行时设备状态。该类将作为规则引擎的条件匹配数据源，ResponsiveContext 的字段也可根据业务需要灵活增减：

```typescript
// Developer-defined context for scene orientation resolution.
// Maintained by EntryAbility and passed to OrientationController as Object.
// The library's resolver accesses fields generically via Record<string, ConditionValue>.
@Observed
export class ResponsiveContext {
  public displayLongEdgeVp: number;
  public displayShortEdgeVp: number;
  public displayLongShortRatio: number;
  public widthBreakpoint: WidthBreakpoint;
  public heightBreakpoint: HeightBreakpoint;

  constructor(
    displayLongEdgeVp: number = 0,
    displayShortEdgeVp: number = 0,
    displayLongShortRatio: number = 1,
    widthBreakpoint: WidthBreakpoint = WidthBreakpoint.WIDTH_SM,
    heightBreakpoint: HeightBreakpoint = HeightBreakpoint.HEIGHT_SM
  ) {
    this.displayLongEdgeVp = displayLongEdgeVp;
    this.displayShortEdgeVp = displayShortEdgeVp;
    this.displayLongShortRatio = displayLongShortRatio;
    this.widthBreakpoint = widthBreakpoint;
    this.heightBreakpoint = heightBreakpoint;
  }
}
```

**存入 AppStorage 供业务页面使用**

初始化流程的核心目标是将ResponsiveContext存入 AppStorage，使所有业务页面能够通过统一的 Key 获取上下文实例并调用ResponsiveValueResolver.getValue()。具体在 EntryAbility.onWindowStageCreate() 中完成以下三步：

```typescript
export default class EntryAbility extends UIAbility {
  // ...
  private responsiveContext?: ResponsiveContext;
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // ...

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        Logger.error(`Failed to load the content. Cause: ${JSON.stringify(err)}`);
        return;
      }
      Logger.info('Succeeded in loading the content.');

      windowStage.getMainWindow().then((data: window.Window) => {
        try {
          this.uiContext = data.getUIContext();
        } catch (err) {
          Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`);
        }

        const abilityRegi: AbilityRegister = new AbilityRegister(data);
        AppStorage.setOrCreate('multidevicelibrary.abilities', abilityRegi.registerContext('defaults'));

        // Maintain the ResponsiveContext for scene orientation resolution and store it in AppStorage.
        this.responsiveContext = new ResponsiveContext();
        this.updateResponsiveContext();
        AppStorage.setOrCreate('multidevicelibrary.context', this.responsiveContext);

        // ...
      }).catch((err: BusinessError) => {
        Logger.error(`Error occured, error code: ${err.code}, error message: ${err.message}`);
      });
    });
  }

  // ...
}
```

**监听设备状态变化****和屏幕属性变化**：

设备状态（屏幕尺寸、折叠态、分辨率）可能在运行时发生变化。为保证规则引擎始终基于最新的设备上下文求值，需要在 EntryAbility 中注册两个关键监听，并在回调中刷新 ResponsiveContext。为了保证拿到的设备状态和屏幕属性是变化后的最终值，建议在屏幕属性变化后也更新一下相关的属性值。

```typescript
export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // ...

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        Logger.error(`Failed to load the content. Cause: ${JSON.stringify(err)}`);
        return;
      }
      Logger.info('Succeeded in loading the content.');

      windowStage.getMainWindow().then((data: window.Window) => {
        // ...
        data.on('windowSizeChange', this.onWindowSizeChange);
        this.registerDisplayListener();
      }).catch((err: BusinessError) => {
        Logger.error(`Error occured, error code: ${err.code}, error message: ${err.message}`);
      });
    });
  }

  // ...

  private onWindowSizeChange: (windowSize: window.Size) => void = (windowSize: window.Size) => {
    if (!this.uiContext) {
      Logger.error('[EntryAbility] uiContext is undefined in onWindowSizeChange.');
      return;
    }
    let widthBp: WidthBreakpoint = this.uiContext.getWindowWidthBreakpoint();
    AppStorage.setOrCreate(CommonConstants.WIDTH_BREAK_POINT, widthBp);
    let heightBp: HeightBreakpoint = this.uiContext.getWindowHeightBreakpoint();
    AppStorage.setOrCreate(CommonConstants.HEIGHT_BREAK_POINT, heightBp);
    let windowSizeVp: window.Size = {
      width: this.uiContext.px2vp(windowSize.width),
      height: this.uiContext.px2vp(windowSize.height)
    };
    AppStorage.setOrCreate(CommonConstants.WINDOW_SIZE_VP, windowSizeVp);
    this.updateResponsiveContext();
    this.scene?.recompute();
  }
  // ...
  private registerDisplayListener(): void {
    try {
      display.on('change', () => {
        this.updateResponsiveContext();
        this.scene?.recompute();
      });
    } catch (e) {
      Logger.error(`[EntryAbility] display.on('change') unavailable: ${JSON.stringify(e)}`);
    }
  }
}
```

updateResponsiveContext() 实现从 defaultDisplay 实时计算屏幕参数：

```typescript
private updateResponsiveContext(): void {
  if (!this.responsiveContext) {
    return;
  }
  try {
    const defaultDisplay: display.Display = display.getDefaultDisplaySync();
    const longEdgePx: number =
      defaultDisplay.width >= defaultDisplay.height ? defaultDisplay.width : defaultDisplay.height;
    const shortEdgePx: number =
      defaultDisplay.width >= defaultDisplay.height ? defaultDisplay.height : defaultDisplay.width;
    const longShortRatio: number = shortEdgePx > 0 ? longEdgePx / shortEdgePx : 1;
    const densityPixels: number = defaultDisplay.densityPixels;
    this.responsiveContext.displayLongEdgeVp = longEdgePx / densityPixels;
    this.responsiveContext.displayShortEdgeVp = shortEdgePx / densityPixels;
    this.responsiveContext.displayLongShortRatio = longShortRatio;
    if (this.uiContext) {
      this.responsiveContext.widthBreakpoint = this.uiContext.getWindowWidthBreakpoint();
      this.responsiveContext.heightBreakpoint = this.uiContext.getWindowHeightBreakpoint();
    }
    AppStorage.setOrCreate(CommonConstants.DISPLAY_SHORT_EDGE_VP, this.responsiveContext.displayShortEdgeVp);
    AppStorage.setOrCreate(CommonConstants.DISPLAY_LONG_SHORT_RATIO, this.responsiveContext.displayLongShortRatio);
  } catch (error) {
    Logger.error(`[EntryAbility] updateResponsiveContext failed: ${JSON.stringify(error)}`);
  }
}
```

**业务页面标准用法**

业务页面使用工具模块遵循统一的标准模式：

```typescript
aboutToAppear() {
  // ...

  const config: ConditionResponsiveValue<OrientationConfig> =
    ResponsiveOrientationConfig.getConfig(PageType.LONG_VIDEO);
  try {
    this.windowObj?.setPreferredOrientation(
      OrientationStrategy.resolveResponsive(globalThis.context, config));
  } catch (err) {
    const error = err as BusinessError;
    Logger.error('VideoDetail', `setPreferredOrientation failed, code: ${error.code}, message: ${error.message}`);
  }
}
```

### 方案对比

页面数量少、适配设备单一、窗口策略固定不变的场景，推荐直接使用系统原生 API 开发；页面数量多、需适配多设备、窗口策略支持动态调整适配的场景，优先采用多设备工具模块，降低跨设备适配成本。原生API与多设备工具模块的对比表格如下，开发者可根据应用的场景选择合适的方案：

| 对比维度 | 原生 API | 多设备工具模块 |
| --- | --- | --- |
| 使用方式 | 直接调用 window.setPreferredOrientation(枚举值) | 声明式配置，调用ResponsiveValueResolver.getValue() |
| 枚举选择 | 需从所有系统枚举中手动筛选 | 通过 PageType 预设或自定义 OrientationConfig，无需记忆枚举 |
| 多设备适配 | 手写 if-else 判断设备尺寸/宽高比/折叠态 | 响应式规则引擎自动匹配 |
| 代码复用 | 每个页面重复编写 setPreferredOrientation 逻辑 | 预设配置一次定义多处复用，自定义配置可跨页面共享 |
| 维护成本 | 策略调整需逐一修改各页面代码 | 集中修改配置常量即可全局生效 |

## 典型场景

以窗口旋转策略实现的五个高频场景为载体，通过窗口级配置实现多设备的窗口方向变化。

### 应用首页案例

应用首页通常支持横屏与竖屏显示。但是在类直板机上横屏的用户体验不好，所以直板机始终竖屏显示；在非类直板机（如平板、双折叠展开态、三折叠M/G态）支持竖屏与横屏展示。体验标准如下：

| 体验标准 | 仅竖屏 | 支持自由旋转，受开关控制 |
| --- | --- | --- |
| 支持设备形态 | 直板机、双折叠折叠态、三折叠F态 | 双折叠展开态、三折叠M/G态、平板 |
| 效果图 |  |  |

对于市场上大多数应用的首页用户行为及体验，推荐使用FOLLOW\_DESKTOP策略，以满足应用在不同设备上的窗口旋转策略需求。同时，FOLLOW\_DESKTOP支持在同设备的折叠状态切换时，窗口旋转策略自动更新。例如，三折叠F态仅支持竖屏，切换至三折叠M态时，自动变为自由旋转，并受控制中心旋转开关的控制。

首先，需对应用启动时的旋转策略进行设置，具体可参考[配置module.json5文件中的orientation字段](bpta-landscape-and-portrait-development.md#section1188593118171)。以实现多开发为例，为满足直板机和平板设备的不同策略，设置为follow\_desktop，此字段主要解决不同设备上默认旋转策略差异的问题。

在具体需要实现横竖屏切换的页面上，采用window窗口提供的设置窗口方向的能力，通过[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)将窗口显示的方向修改为横屏或竖屏的状态。

具体如下：通过getContext获取对应的UIAbilityContext，并通过context获取对应的windowStage实例，然后通过windowStage.getMainWindowSync同步方法拿到对应的窗口实例win，然后调用[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)方法设置窗口方向。

```typescript
@Component
export struct Home {
  windowObj: window.Window | undefined = undefined;
  // ...

  aboutToAppear(): void {
    this.tabBarsInfo.setTabList(TabBarsInfo);
    try {
      this.windowObj = (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync()
    } catch (err) {
      Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
    }

    // Use the WindowOrientationHelper tool to directly obtain the rotation strategy enumeration through chained calls.
    this.windowObj?.setPreferredOrientation(WindowOrientationHelper.presets.FOLLOW_DESKTOP)
      .catch((err: BusinessError) => {
        Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
      });
    // ...
  }

  // ...

  build() {
    // ...
  }
}
```

### 游戏应用案例

游戏应用通常仅支持竖屏或横屏显示。例如消除类游戏仅支持竖屏显示；MOBA类游戏仅支持横屏显示。体验标准如下：

| 体验标准 | 竖屏游戏仅支持竖屏 | 横屏游戏支持横屏旋转，受开关控制 |
| --- | --- | --- |
| 支持设备形态 | 直板机、双折叠折叠态、三折叠F/M/G态、平板 | 直板机、双折叠折叠态、三折叠F/M/G态、平板 |
| 效果图 |  |  |

对于游戏类应用，无论横竖屏游戏，均为固定方式或仅支持一个方向（例竖屏及反向竖屏）的旋转切换，此类应用均不需要在应用内进行开关控制，所以只需要在module.json5配置文件中进行相应的配置即可。一般有以下几种情况：

**默认竖屏方向**

如果该应用默认为仅竖屏状态，那么则需要在module.json5中的“orientation”字段进行配置为portrait。如果希望游戏同时支持反向竖屏显示，推荐设置为auto\_rotation\_portrait\_restricted。

**默认横屏方向**

推荐横屏游戏使用auto\_rotation\_landscape\_restricted策略，所有设备上初始窗口方向为横屏或反向横屏，支持横屏旋转，且受控制中心的旋转开关控制。同时，在同一设备切换折叠状态时，保持横屏或反向横屏显示。

### 图库应用案例

图库应用通常在所有设备上支持竖屏或横屏显示。但是在直板机上反向竖屏的用户体验不好，所以直板机只能旋转至竖屏、横屏、反向横屏三个方向，受开关控制；在非类直板机（如平板、双折叠展开态、三折叠M/G态）保持当前窗口方向，支持自由旋转，且受开关控制。体验标准如下：

| 体验标准 | 三向旋转（竖屏/横屏/反向横屏），受开关控制 | 自由旋转，受开关控制 |
| --- | --- | --- |
| 支持设备形态 | 直板机、双折叠折叠态、三折叠F态 | 双折叠展开态、三折叠M/G态、平板 |
| 效果图 |  |  |

推荐图库应用案例在module.json5中的“orientation”字段或页面中通过[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)使用AUTO\_ROTATION\_UNSPECIFIED策略。

### 个股详情页 & 股票K线图页案例

个股详情页通常支持横屏与竖屏显示。但是在类直板机上横屏的用户体验不好，所以直板机始终竖屏显示，不支持旋转；在非类直板机（如平板、双折叠展开态、三折叠M/G态）保持当前窗口方向，支持自由旋转，且受控制中心的旋转开关控制。体验标准如下：

| 体验标准 | 仅竖屏 | 支持自由旋转，受开关控制 |
| --- | --- | --- |
| 支持设备形态 | 直板机、双折叠折叠态、三折叠F态 | 双折叠展开态、三折叠M/G态、平板 |
| 效果图 |  |  |

在个股详情页面上，在aboutToAppear生命周期中采用window窗口提供的设置窗口方向的能力，通过[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)设置窗口旋转策略为FOLLOW\_DESKTOP，在aboutToDisappear中恢复上级页面的窗口旋转策略。

```typescript
@Component
export struct StockDetail {
  windowObj: window.Window | undefined = undefined;
  // ...

  aboutToAppear(): void {
    try {
      this.windowObj = (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync()
    } catch (err) {
      Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
    }

    this.windowObj?.setPreferredOrientation(window.Orientation.FOLLOW_DESKTOP)
      .catch((err: BusinessError) => {
        Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
      });
  }

  aboutToDisappear() {
    this.windowObj?.setPreferredOrientation(window.Orientation.UNSPECIFIED)
      .catch((err: BusinessError) => {
        Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
      });
  }

  build() {
    // ...
  }
}
```

股票K线图页通常仅横屏显示，支持横屏旋转，且受控制中心的旋转开关控制。体验标准如下：

| 体验标准 | 横屏旋转，受开关控制 |
| --- | --- |
| 支持设备形态 | 直板机、双折叠折叠态、三折叠F/M/G态、平板 |
| 效果图 |  |

**示例代码**

在K线图页的aboutToAppear()和aboutToDisappear()生命周期中调用window.setPreferredOrientation()，设置K线图页显示时窗口旋转策略为AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED，K线图页返回时恢复窗口旋转策略为FOLLOW\_DESKTOP。

```typescript
aboutToAppear(): void {
  try {
    this.windowObj = (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync()
  } catch (err) {
    Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
  }

  this.windowObj?.setPreferredOrientation(WindowOrientationHelper.autoRotate("LANDSCAPE_ONLY"))
    .catch((err: BusinessError) => {
      Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
    });
}

aboutToDisappear(): void {
  this.windowObj?.setPreferredOrientation(WindowOrientationHelper.followDesktop())
    .catch((err: BusinessError) => {
      Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
    });
}
```

### 视频详情页 & 全屏播放页案例

视频详情页通常支持横屏与竖屏显示。但是在直板机上反向竖屏的用户体验不好，所以直板机只能旋转至竖屏、横屏、反向横屏三个方向，且横屏时自动显示全屏播放页，竖屏时自动显示视频详情页；在非类直板机（如平板、双折叠展开态、三折叠M/G态）保持当前窗口方向，支持自由旋转，且受开关控制。体验标准如下：

| 体验标准 | 三方向旋转（竖屏/横屏/反向横屏），受开关控制 | 自由旋转，受开关控制 |
| --- | --- | --- |
| 支持设备形态 | 直板机、双折叠折叠态、三折叠F态 | 双折叠展开态、三折叠M/G态、平板 |
| 效果图 |  |  |

全屏播放页仅横屏显示，支持横屏旋转，并受控制中心旋转开关控制。在类直板机上，用户点击全屏按钮进入全屏播放页时，仅能旋转至横屏和反向横屏两个方向；若开启旋转开关，从横屏或反向横屏进入全屏播放页时，支持旋转至竖屏、横屏、反向横屏三个方向，并在旋转至竖屏时切换至视频详情页。在双折叠展开态（接近正方形）下，可自由旋转至四个方向，且受开关控制。体验标准如下：

| 体验标准 | 横屏旋转，受开关控制 | 自由旋转，受开关控制 | 横屏旋转，受开关控制 |
| --- | --- | --- | --- |
| 支持设备形态 | 类直板机 | 双折叠展开态、三折叠M | 三折叠G态、平板 |
| 效果图 |  |  |  |

对于视频类应用，在具体需要实现横竖屏切换的页面上，例如视频播放页面支持横屏，但是首页的内容是支持仅竖屏的，那么就需要在进入对应的页面时，采用window窗口提供的设置窗口方向的能力，通过[setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)将窗口显示的方向修改为横屏、竖屏的状态。应用的默认旋转策略和如何通过[setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)方法设置窗口方向可参考首页案例代码。

以视频播放为例，不仅可以通过系统控制横竖屏，也支持用户在系统锁定旋转的情况下，手动设置横屏状态，即需要满足以下条件：

1. **应用跟随传感器旋转。**
2. **受到控制中心的旋转锁定按钮控制。**
3. **支持用户在应用页面中临时调用设置方向的能力，例如点击全屏按钮进行切换。**

要实现上述效果，可通过窗口的 orientation 属性设置枚举类型来实现旋转功能。为支持临时方向设置，当用户点击全屏按钮时需手动触发横竖屏切换。若旋转锁定已关闭，窗口应跟随传感器旋转。因此推荐视频详情页采用 AUTO\_ROTATION\_UNSPECIFIED 策略，三折叠展开态及平板全屏播放页采用 AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED 策略，以实现临时调用旋转并支持后续传感器跟随。

在视频详情页中，设置窗口方向为AUTO\_ROTATION\_UNSPECIFIED：

```typescript
@Component
export struct VideoDetail {
  windowObj: window.Window | undefined = undefined;
  // ...

  aboutToAppear() {
    try {
      this.windowObj = (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync()
    } catch (err) {
      Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
    }

    // ...

    // Dynamically select an appropriate rotation strategy through a selector.
    this.windowObj?.setPreferredOrientation(WindowOrientationHelper.select({
      mode: 'autoRotate',
      range: 'ALL_ORIENTATIONS',
      preferred: 'UNSPECIFIED'
    }))
      .catch((err: BusinessError) => {
        Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
      });
  }

  // ...

  build() {
    // ...
  }

}
```

在aboutToAppear()生命周期中添加窗口尺寸变化的监听方法on('windowSizeChange', callback)，当窗口尺寸变化时，通过窗口断点判断当前设备的横竖屏状态，切换全屏状态或更新窗口旋转策略；

监听视频详情页的全屏播放状态，在用户点击全屏播放按钮时，在回调方法onFullScreenChange()中判断当前设备的横竖屏状态，更新窗口旋转策略，并在用户返回视频详情页时恢复视频详情页的窗口旋转策略。

```typescript
@Component
export struct VideoDetail {
  windowObj: window.Window | undefined = undefined;
  @StorageLink('isFullScreen') @Watch('onFullScreenChange') isFullScreen: boolean = false;
  // ...

  aboutToAppear() {
    // ...
    this.windowObj?.on('windowSizeChange', this.onWindowSizeChange);

    // ...
  }

  onFullScreenChange(): void {
    if (this.isFullScreen) {
      if (this.isClick) {
        if (this.widthBp === WidthBreakpoint.WIDTH_SM || this.widthBp === WidthBreakpoint.WIDTH_LG ||
          this.heightBp === HeightBreakpoint.HEIGHT_LG) {
          // Dynamically select an appropriate rotation strategy through a selector.
          this.windowObj?.setPreferredOrientation(WindowOrientationHelper.select({
            mode: 'autoRotate',
            range: 'LANDSCAPE_ONLY'
          }))
            .catch((err: BusinessError) => {
              Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
            });
        }
      }
    } else {
      // Dynamically select an appropriate rotation strategy through a selector.
      this.windowObj?.setPreferredOrientation(WindowOrientationHelper.select({
        mode: 'autoRotate',
        range: 'ALL_ORIENTATIONS',
        preferred: 'UNSPECIFIED'
      }))
        .catch((err: BusinessError) => {
          Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
        });
    }
  }

  private onWindowSizeChange: (windowSize: window.Size) => void = () => {
    if (this.isClick) {
      return;
    }
    if (this.widthBp === WidthBreakpoint.WIDTH_SM) {
      this.isFullScreen = false
      // Dynamically select an appropriate rotation strategy through a selector.
      this.windowObj?.setPreferredOrientation(WindowOrientationHelper.select({
        mode: 'autoRotate',
        range: 'ALL_ORIENTATIONS',
        preferred: 'UNSPECIFIED'
      }))
        .catch((err: BusinessError) => {
          Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
        });
    }

    if (this.widthBp === WidthBreakpoint.WIDTH_MD && this.heightBp === HeightBreakpoint.HEIGHT_SM) {
      this.isFullScreen = true;
    }
  };

  // ...

  build() {
    // ...
  }

}
```

## 常见问题

### display与window的区别

* 屏幕（[@ohos.display (屏幕属性)](../harmonyos-references/js-apis-display.md)）指物理或逻辑的显示设备，是显示内容的整体区域。例如：
  + 物理屏幕：显示器、手机屏幕、投影仪等硬件设备。
  + 逻辑屏幕：操作系统虚拟的多屏幕环境（如扩展桌面）。
* 窗口（window）是运行在屏幕上的一个可交互的图形界面区域，属于软件层面。例如：
  + 应用程序窗口（如浏览器、文件夹窗口）。
  + 对话框、工具栏等子窗口。

### display.rotation的定义

[Display](../harmonyos-references/js-apis-display.md#display)的属性rotation表示显示设备的屏幕顺时针旋转角度。使用场景：适用于和硬件设备角度强关联的场景，如相机预览角度补偿。

rotation的取值有4种，分别对应下图所示的4个方向（以直板机为例）。如果需要更精准的角度信息，则需要配合设备sensor获取。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/jGV91_teSy2OTT45Ls3PSQ/zh-cn_image_0000002535837336.png "点击放大")

| 值 | 含义 |
| --- | --- |
| 0 | 显示设备屏幕顺时针旋转为0°。 |
| 1 | 显示设备屏幕顺时针旋转为90°。 |
| 2 | 显示设备屏幕顺时针旋转为180°。 |
| 3 | 显示设备屏幕顺时针旋转为270°。 |

### display.Orientation与window.Orientation的区别

* display的[Orientation](../harmonyos-references/js-apis-display.md#orientation10)表示屏幕当前横竖显示方向，屏幕的横竖显示方向只能获取，不能设置，客观体现了当前屏幕的显示状态。
* window.Orientation表示窗口旋转策略，窗口旋转策略可以由开发者设置，系统会根据开发者的预设策略进行相应的旋转。

对于开发者而言，控制应用的显示方向应该通过设置window.Orientation实现，详情请参考[了解窗口旋转策略](bpta-multi-device-window-direction.md#section7778165616124)。

### display.Orientation与display.rotation的关系

display.Orientation 为屏幕当前的朝向状态，display.rotation 为屏幕相对自然方向的物理旋转角度。display.Orientation 为和 display.rotation 均为只读属性，且用于描述屏幕当前旋转状态，但二者定义逻辑不同，在各类设备形态下不存在固定对应关系，开发过程中不可相互替代。若混用接口，在折叠屏等多形态设备适配场景中极易引发兼容性问题。以三折叠设备为例：当 display.rotation 取值为 0° 时，display.Orientation 既可能为竖屏状态，也可能为反向横屏状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/vshkw4T0TuuEDRGczTwM6A/zh-cn_image_0000002622960129.jpg "点击放大")

### window.getLastWindow的方式获取窗口出现延迟

1. 由于getLastWindow底层原因，需要经过查找获取实例，一定程度上会有性能损耗，可能会出现已经发生横屏或者竖屏切换的情况下，状态栏还没切换的情况。
2. 使用windowStage.getMainWindowSync的同步方法获取窗口实例。

```typescript
onWindowStageCreate(windowStage: window.WindowStage): void {
  // ...
  try {
    this.windowUtil = new WindowUtil(windowStage.getMainWindowSync());
  } catch (error) {
    let err = error as BusinessError;
    hilog.error(0x0000, 'TestLog', `Failed to get main window. Code: ${err.code}, message: ${err.message}`);
  }
  AppStorage.setOrCreate('windowUtil', this.windowUtil);

  windowStage.loadContent('pages/Index', (err) => {
    // ...
    this.windowUtil!.setUIContext();
    this.windowUtil!.setImmersiveType(ImmersiveType.IMMERSIVE);
    this.windowUtil!.updateWindowInfo();
  });
}
```

### 竖屏时进入任务中心，进入横屏的应用，在onPageShow时获取的display信息不符合预期

目前display接口规则还不够清晰，建议使用window的getWindowProperties()接口处理。

### 如何获取屏幕的宽度、高度、分辨率和横竖屏等信息

引入屏幕属性模块，可以通过调用[display.getDefaultDisplaySync()](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)方法获取display对象后，从而获取到屏幕的宽度、高度、分辨率和横竖屏等信息。

### 如何通过日志查看应用当前设置的窗口旋转策略

在多模块多团队共同开发过程中，页面窗口旋转策略的设置可能导致预期之外的窗口旋转问题。开发者需通过查询日志的方式自行排查是否设定了非预期的窗口旋转策略。查询方法如下：

1. 连接并推包到当前设备。
2. 打开Log页面，依次在筛选框中选择“当前的连接设备”、“No filters”、“当前的调试应用”、“Debug”或“Info”，最后在关键字栏填写“SetRequestedOrientation”。
3. 操作问题页面后，在日志中查看系统日志，找到应用包名一行的日志，lastReqOrientation表示应用最后的窗口旋转策略，target表示目标窗口旋转策略，后面的数字可参考下方对照表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/EkSrjhKTQSe81Md3MNRvlQ/zh-cn_image_0000002593796295.png)

日志中查看窗口方向对照表

| window.orientation | target |
| --- | --- |
| UNSPECIFIED | 0 |
| PORTRAIT | 1 |
| LANDSCAPE | 2 |
| PORTRAIT\_INVERTED | 3 |
| LANDSCAPE\_INVERTED | 4 |
| AUTO\_ROTATION | 5 |
| AUTO\_ROTATION\_PORTRAIT | 6 |
| AUTO\_ROTATION\_LANDSCAPE | 7 |
| AUTO\_ROTATION\_RESTRICTED | 8 |
| AUTO\_ROTATION\_PORTRAIT\_RESTRICTED | 9 |
| AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED | 10 |
| LOCKED | 11 |
| FOLLOW\_RECENT | 12 |
| AUTO\_ROTATION\_UNSPECIFIED | 13 |
| USER\_ROTATION\_PORTRAIT | 14 |
| USER\_ROTATION\_LANDSCAPE | 15 |
| USER\_ROTATION\_PORTRAIT\_INVERTED | 16 |
| USER\_ROTATION\_LANDSCAPE\_INVERTED | 17 |
| FOLLOW\_DESKTOP | 18 |

## 示例代码

* [窗口方向](https://gitcode.com/HarmonyOS_Samples/WindowOrientation)
