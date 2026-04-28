---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-window-direction
title: 窗口方向
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备窗口形态 > 窗口方向
category: best-practices
scraped_at: 2026-04-28T08:21:04+08:00
doc_updated_at: 2026-04-07
content_hash: sha256:46c739f464fbe261c03d218d39599c5359ff65070ee0cd9109717371f7fdc69f
---

## 概述

窗口方向适配旨在解决应用不同场景下窗口的朝向问题。以直板机上的视频类应用为例，应用首页通常竖屏显示；而全屏视频播放页通常横屏显示。其核心的策略在于动态调整应用窗口方向的显示策略（即window的[Orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)，以下简称“**窗口策略**”），确保在不同用户交互场景下提升用户体验。

本文主要内容如下：

* 前置约束与限制：介绍窗口方向的含义。明确指出在设备形态多样化的前提下，如何选择更合适的窗口旋转策略。
* 窗口策略枚举：介绍窗口策略的枚举值，并解析各值在不同设备形态下的行为映射，帮助开发者理解系统的底层适配逻辑。
* 实现原理：介绍配置页面窗口策略的技术实现机制与核心流程。

* 典型场景：
  + 应用首页案例：通用页面窗口策略。
  + 游戏应用案例：竖屏或横屏方向锁定的窗口策略。
  + 图库案例：四个方向自动旋转且受控制中心的旋转开关控制的窗口策略。
  + 个股详情页 & 股票K线图页：应用组合页面内根据场景不同切换的窗口策略。
  + 视频详情页 & 全屏播放页：相同页面内根据用户行为切换的窗口策略。

## 前置约束与限制

本文主要面向中高级开发者。开始之前，建议先了解[窗口管理](../harmonyos-guides/window-manager.md)、[窗口旋转](../harmonyos-guides/window-rotation.md)、[屏幕管理](../harmonyos-guides/display-manager.md)、[一次开发，多端部署](bpta-multi-device-overview.md)、[组件导航（Navigation）](../harmonyos-guides/arkts-navigation-navigation.md)等知识点。

横竖屏切换功能即实现应用内既支持竖屏显示也支持横屏显示的效果。对于应用内不同页面显示方向不同的情况，需要在应用逻辑中动态修改窗口方向来实现该效果。例如直板机上包含视频播放功能的应用，首页内容是采用竖屏方式，而全屏播放页则采用横屏方式展示。

随着设备形态越来越多，应用页面支持旋转已经从部分页面适配，变为全面支持，选择合适的旋转策略，对应用开发至关重要。

目前HarmonyOS系统中的窗口旋转形态有以下四种，对应真机实际状态如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/gLDP4RGBTsyvkyn4F3v7dw/zh-cn_image_0000002566756945.png?HW-CC-KV=V1&HW-CC-Date=20260428T002056Z&HW-CC-Expire=86400&HW-CC-Sign=1C7C595F053D3865FE56B581DDC7816A77DB906957378557AAD71AB760B7A169)

说明

以设备物理屏幕尺寸为判定依据，当设备屏幕高度大于宽度时，定义为设备竖屏状态；当设备屏幕高度小于宽度时，定义为设备横屏状态。

竖屏、横屏区分的标准：

* 按照用户默认使用状态一般为竖屏或横屏（即充电口朝下或朝右）
* display.rotation为0度即为横屏或竖屏

反向竖屏：横屏顺时针顺时针旋转90度

反向横屏区分的标准：反向竖屏顺时针旋转90度

## 了解窗口旋转策略

窗口旋转策略提供了18种旋转策略（即window的[Orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)），开发者可以通过预设旋转策略，进而控制应用在不同场景下窗口的方向。为了开发者能更快速的理解这些旋转策略，下文会分类说明18个枚举值的含义以及对应的效果。

### 固定方向策略

固定方向策略即应用首次加载或路由跳转时，窗口显示的初始方向且不支持旋转，包含以下五类：

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

自动旋转策略受窗口支持旋转的方向及控制中心的旋转开关控制影响。

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

说明

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
| AUTO\_ROTATION\_UNSPECIFIED | 12 | 跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定（如在直板机可以旋转到竖屏、横屏、反向横屏，无法旋转到反向竖屏；双折展开态、三折FG态、平板可以旋转到竖屏、反向竖屏、横屏及反向横屏）。 |

以三折叠G态（即三折叠设备完全展开时的三屏显示状态）为例，受控制中心控制的自动旋转策略效果图如下：

|  |  |  |
| --- | --- | --- |
| 自由旋转（竖屏/反向竖屏/横屏/反向横屏） | AUTO\_ROTATION\_RESTRICTED |  |
| 竖屏旋转（竖屏/反向竖屏） | AUTO\_ROTATION\_PORTRAIT\_RESTRICTED |  |
| 横屏旋转（横屏/反向横屏） | AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED |  |
| 保持当前窗口方向，在直板机可以旋转到竖屏、横屏、反向横屏，无法旋转到反向竖屏；双折展开态、三折FG态、平板可以旋转到竖屏、反向竖屏、横屏及反向横屏 | AUTO\_ROTATION\_UNSPECIFIED |  |

**带首选方向的自动旋转**

带首选方向的旋转策略是“**受控制中心控制”**且“**可旋转方向受系统判定”**，可以分为以下四类：

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER\_ROTATION\_PORTRAIT | 13 | 调用时临时旋转到竖屏，之后跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定。 |
| USER\_ROTATION\_LANDSCAPE | 14 | 调用时临时旋转到横屏，之后跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定。 |
| USER\_ROTATION\_PORTRAIT\_INVERTED | 15 | 调用时临时旋转到反向竖屏，之后跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定。 |
| USER\_ROTATION\_LANDSCAPE\_INVERTED | 16 | 调用时临时旋转到反向横屏，之后跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定。 |

说明

可旋转方向受系统判定：如在直板机可以旋转到竖屏、横屏、反向横屏三个方向，无法旋转到反向竖屏；双折展开态、三折FG态、平板可以旋转到竖屏、反向竖屏、横屏及反向横屏四个方向。

### 跟随桌面显示策略

因为不同的设备类型和形态的最佳体验，适合不同的旋转策略，多设备窗口策略的具体行为表现由系统根据当前设备的形态动态定义，开发者可以简单跟随桌面的最佳体验策略。实现参考下方”跟随桌面的旋转策略”章节。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FOLLOW\_DESKTOP | 17 | 表示跟随桌面的旋转模式，如果桌面可以旋转则可旋转，桌面不可旋转则不可旋转。 |

## 选择合适的窗口旋转策略

应用的不同页面在不同设备上需设置合适的窗口旋转策略，以提供最佳的用户体验。

关于如何通过是否支持自动旋转、支持旋转的方向及预设初始方向三个维度选择合适的窗口策略，可参考以下表格：

| 是否支持自动旋转 | 支持旋转的方向 | 预设初始方向 | 窗口策略 |
| --- | --- | --- | --- |
| 不可旋转 | NA | NA | LOCKED |
| 不可旋转 | NA | 竖屏 | PORTRAIT |
| 不可旋转 | NA | 横屏 | LANDSCAPE |
| 不可旋转 | NA | 反向竖屏 | PORTRAIT\_INVERTED |
| 不可旋转 | NA | 反向横屏 | LANDSCAPE\_INVERTED |
| 不受控旋转 | 四向可旋转 | NA | AUTO\_ROTATION |
| 不受控旋转 | 竖两向可旋转 | NA | AUTO\_ROTATION\_PORTRAIT |
| 不受控旋转 | 横两向可旋转 | NA | AUTO\_ROTATION\_LANDSCAPE |
| 不受控旋转 | 最多四向可旋转，但受系统判定 | NA | UNSPECIFIED |
| 受控旋转 | 竖两向可旋转 | NA | AUTO\_ROTATION\_PORTRAIT\_RESTRICTED |
| 受控旋转 | 横两向可旋转 | NA | AUTO\_ROTATION\_LANDSCAPE\_RESTRICTE |
| 受控旋转 | 四向可旋转 | NA | AUTO\_ROTATION\_RESTRICTED |
| 受控旋转 | 最多四向可旋转，但受系统判定 | NA | AUTO\_ROTATION\_UNSPECIFIED |
| 受控旋转 | 最多四向可旋转，但受系统判定 | 竖屏 | USER\_ROTATION\_PORTRAIT |
| 受控旋转 | 最多四向可旋转，但受系统判定 | 横屏 | USER\_ROTATION\_LANDSCAPE |
| 受控旋转 | 最多四向可旋转，但受系统判定 | 反向竖屏 | USER\_ROTATION\_PORTRAIT\_INVERTED |
| 受控旋转 | 最多四向可旋转，但受系统判定 | 反向横屏 | USER\_ROTATION\_LANDSCAPE\_INVERTED |
| 跟随桌面策略 | NA | NA | FOLLOW\_DESKTOP |

## 为应用配置旋转策略

为了满足灵活多变的UI交互需求，系统支持**应用级**、**窗口级**和**页面级**的窗口策略配置方案，并提供**子窗口**和**悬浮窗**旋转的窗口策略配置。

### 应用级配置

设置应用初始的窗口策略，通过在hap包的module.json5文件中配置orientation属性，会影响应用的启动方向。

此字段用于配置应用启动时的窗口显示状态。如果应用启动时需要以默认的横屏或竖屏方式显示，需要在此字段进行相应的配置。

其支持的参数可以参考module.json5配置项中[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)下orientation的[orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)枚举值。

```
1. {
2. "module": {
3. // ...
4. "abilities": [
5. {
6. "name": "EntryAbility",
7. // ...
8. "orientation": "unspecified",
9. // ...
10. }
11. ],
12. // ...
13. }
14. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/WindowOrientation/blob/master/products/default/src/main/module.json5#L2-L60)

应用可根据业务需求配置默认旋转策略：

* 如果应用是竖屏应用，建议配置PORTRAIT为默认旋转策略。
* 如果应用是横屏应用，例如MOBA类游戏应用，启动时默认为横屏，存在以下两种情况：
  + 仅支持横屏，建议配置LANDSCAPE为默认旋转策略。
  + 支持在横屏和反向横屏中切换，建议设置为AUTO\_ROTATION\_LANDSCAPE或者AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED（是否受控制中心的旋转开关控制）。
* 如果应用为可旋转应用，建议应用配置AUTO\_ROTATION\_RESTRICTED为默认旋转策略。
* 如果一个应用，在直板机和双折叠折叠态是竖屏应用，在平板和双折叠展开态默认是可旋转应用，推荐配置FOLLOW\_DESKTOP为默认旋转策略。

说明

对于需要通过控制中心进行旋转锁定控制的情况，可以选择字段后方带有RESTRICTED字段的旋转策略。

此字段表示旋转行为受到控制中心按钮控制：开关打开情况下，不随设备方向旋转，关闭情况下，则会发生跟随设备旋转。

以如下文件管理应用为例，在系统关闭了旋转锁定后，应用的页面都会随着手机旋转而发生展示上的切换，而打开时则不会发生旋转行为，此时就需要配置为AUTO\_ROTATION\_RESTRICTED。

应用随系统旋转切换横竖屏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/pi3cp7DuRUCOShIT8YuEyA/zh-cn_image_0000002535997144.png?HW-CC-KV=V1&HW-CC-Date=20260428T002056Z&HW-CC-Expire=86400&HW-CC-Sign=5C4B24A2C0131B6A72CA9B835AF3DAC0276DA4EAC4EEF840F47B9DD9B0DBEC48 "点击放大")

### 窗口级配置

它作用于整个应用组件窗口（window），定义该窗口的横竖屏旋转策略，并对基于Navigation组件和Router模块实现的路由跳转均生效。一旦配置，除非显式修改，否则对窗口内所有页面生效。

1. 在onWindowStageCreate()中调用window.setPreferredOrientation()方法即可设置整个应用窗口默认方向。页面跳转时，默认沿用上一个页面的窗口策略（即上一页面与应用级窗口策略不一致则优先使用上一页面的窗口策略）。如果整个应用页面的窗口策略一致，则无需执行步骤2。

```
1. setWindowOrientation(orientation: window.Orientation): void {
2. this.mainWindow.setPreferredOrientation(orientation)
3. .then(() => {
4. hilog.info(0x0000, 'testLog', `Succeeded in setting window orientation.`);
5. // Update window orientation.
6. this.mainWindowInfo.orientation = orientation;
7. })
8. .catch((err: BusinessError) => {
9. hilog.error(0x0000, 'testLog', `Failed to set window orientation. Code: ${err.code}, message: ${err.message}`);
10. });
11. }
```

2. 如果应用内页面的窗口策略不一致，则需要执行本步骤。在页面进入时（aboutToAppear），调用window.setPreferredOrientation()定义当前页面对应的窗口策略；在页面退出时（aboutToDisappear），调用window.setPreferredOrientation()恢复即将展示页面对应的窗口策略。

```
1. @StorageLink('mainWindow') mainWindow?: window.Window = undefined;
2. public lastOrientation?: window.Orientation;

4. aboutToAppear(): void {
5. if (this.mainWindow === undefined) {
6. return;
7. }
8. this.lastOrientation = this.mainWindow!.getPreferredOrientation();
9. this.mainWindow!.setPreferredOrientation(window.Orientation.LANDSCAPE);
10. }

12. aboutToDisappear(): void {
13. this.mainWindow!.setPreferredOrientation(this.lastOrientation)
14. }
```

典型场景如一些视频类应用、图片类应用等。

视频播窗横竖屏切换

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/2rugD-9JTteKZzy0shSuNw/zh-cn_image_0000002566916979.png?HW-CC-KV=V1&HW-CC-Date=20260428T002056Z&HW-CC-Expire=86400&HW-CC-Sign=5B5213A04B83FF83D89412022AE8593BFA4A825D76AA03795FEBC040DEB52828 "点击放大")

### 页面级配置

它作用于当前显示的具体页面（NavDestination组件），仅对基于Navigation组件实现的路由跳转生效。它允许根据业务需求动态调整不同页面的窗口策略。在页面路由跳转时，系统自动切换为下一个展示页面对应的窗口策略。

NavDestination组件提供[preferredOrientation](../harmonyos-references/ts-basic-components-navdestination.md#preferredorientation19)属性，支持每个页面独立配置窗口策略，互相不影响。页面跳转时，窗口策略自动更新为下一个页面对应的preferredOrientation。页面返回时，窗口策略也会自动更新为上一个页面对应的preferredOrientation。

### 方案对比

| 窗口策略配置方案 | 优势 | 劣势 | 推荐使用场景 |
| --- | --- | --- | --- |
| 应用级 | * 可设置应用启动的初始方向 * 应用所有页面窗口策略一致时仅需配置一次 | 应用内页面窗口策略不一致时，无法切换，需要配合窗口级或页面级窗口策略 | * 应用需要设置启动的初始方向。 * 应用所有页面窗口策略一致。 |
| 窗口级 | * 配置后所有页面生效 * 支持Navigation组件与Router模块实现的路由 * 版本兼容性高（API9+） | 页面窗口策略不一致时，需要在页面进入及退出时设置两次窗口策略。 | * 使用Router模块实现页面路由 * 应用基于API19之前的版本开发 |
| 页面级 | * 单独配置每个页面的窗口策略，页面跳转时窗口策略跟随自动更新 * 针对页面配置窗口策略，使用更简单、更灵活 | * 版本兼容性有限（API19+） * 仅支持Navigation组件实现的页面路由 | * 应用内页面的窗口策略多处不一致 * 基于Navigation模块实现页面路由 * 应用基于API19之后的版本开发 |

### 应用子窗口的旋转

在应用旋转场景中，应用主窗的尺寸由系统控制，而应用子窗的尺寸和位置由应用控制。因此，建议应用开发者在有应用子窗的旋转场景中，同步调整应用子窗的尺寸和位置，避免因旋转过程中应用子窗的尺寸和位置保持不变而导致如下图所示的应用子窗显示截断问题（直板机默认的旋转策略为UNSPECIFIED，旋转锁定按钮关闭的情况下不允许应用旋转，可以通过module.json5配置文件中abilities标签的"orientation"字段（参考[abilities对象的内部结构](../harmonyos-guides/module-structure.md#abilities对象的内部结构)）配置应用的旋转策略为AUTO\_ROTATION，使应用跟随设备方向旋转）。

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

```
1. import { window } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const SUB_WINDOW_LEFT_OFFSET: number = 50;
6. const SUB_WINDOW_TOP_OFFSET: number = 500;
7. const TAG: string = 'subWindowAdaptWhenRotate';
8. const DOMAIN: number = 0x0000;

10. @Entry
11. @Component
12. struct Index {
13. public mainWindow: window.Window | undefined = undefined;
14. public subWindow: window.Window | undefined = undefined;

16. aboutToAppear(): void {
17. // create subWindow
18. this.createSubWindow();

20. this.mainWindow = AppStorage.get('mainWindow');
21. if (!this.mainWindow) {
22. return;
23. }
24. this.mainWindow.on('windowSizeChange', () => {
25. this.adjustSubwindowSizeAndPosition();
26. })
27. }

29. private adjustSubwindowSizeAndPosition(): void {
30. if (!this.subWindow) {
31. hilog.error(DOMAIN, TAG, 'subWindow is null');
32. return;
33. }
34. let subwindowRect: window.Rect | null = null;
35. try {
36. subwindowRect = this.subWindow.getWindowProperties().windowRect;
37. } catch (error) {
38. hilog.warn(0x000, 'testTag', `getWindowProperties failed, code: ${error.code}, message: ${error.message}`);
39. }
40. let newWidth: number = subwindowRect!.height;
41. let newHeight: number = subwindowRect!.width;
42. let newX: number = subwindowRect!.top;
43. let newY: number = subwindowRect!.left;
44. this.subWindow.resize(newWidth, newHeight)
45. .then(() => {
46. hilog.info(DOMAIN, TAG, 'Succeeded in changing the window size')
47. }).catch((err: BusinessError) => {
48. hilog.error(DOMAIN, TAG, `Failed to change the window size. Cause code: ${err.code}, message: ${err.message}`);
49. });

51. this.subWindow.moveWindowTo(newX, newY)
52. .then(() => {
53. hilog.info(DOMAIN, TAG, 'Succeeded in moving the window');
54. }).catch((err: BusinessError) => {
55. hilog.error(DOMAIN, TAG, `Failed to move the window. Cause code: ${err.code}, message: ${err.message}`);
56. });

58. }

60. // ...
61. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/SubwindowAdaptWhenRotate/entry/src/main/ets/pages/Index.ets#L17-L134)

**实现效果**

根据示例代码为不同旋转方向设置不同的应用子窗尺寸和位置的实际效果如下图所示，应用子窗的尺寸和位置在竖屏显示和横屏显示下是不同的。

| 旋转前竖屏显示 | 旋转后横屏显示 |
| --- | --- |
|  |  |

### 悬浮窗的旋转

悬浮窗默认是竖向的，但是对于横向游戏和视频应用，横向的悬浮窗体验会更好。开发者可以通过在module.json5配置文件中abilities标签下的preferMultiWindowOrientation属性增加“landscape”或者“landscape\_auto”，配合API以声明应用支持横向悬浮窗或上下分屏模式。

```
1. {
2. "module": {
3. // ...
4. "abilities": [
5. {
6. "name": "EntryAbility",
7. // ...
8. "preferMultiWindowOrientation": "landscape_auto",
9. // ...
10. }
11. ],
12. // ...
13. }
14. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/ArkUI/orientationDevelopment/entry/src/main/configlandscapeauto/module.json5#L2-L63)

该场景下多窗布局动态可变为横向，需要配合API（[enableLandscapeMultiWindow()](../harmonyos-references/arkts-apis-window-window.md#enablelandscapemultiwindow12)/ [disableLandscapeMultiWindow()](../harmonyos-references/arkts-apis-window-window.md#disablelandscapemultiwindow12)）使用。

```
1. private windowClass = (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync()

3. aboutToAppear(): void {
4. this.windowClass.enableLandscapeMultiWindow();
5. }

7. aboutToDisappear(): void {
8. this.windowClass.disableLandscapeMultiWindow();
9. }
```

[ScreenRotationB.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/ArkUI/orientationDevelopment/entry/src/main/ets/pages/ScreenRotationB.ets#L6-L14)

例如：视频或者游戏类应用在横屏模式下开启悬浮窗后，页面没有适配横屏，导致内容显示不全或者观看体验不好。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/ul0JCkO6ROKqQS24Tj0I3Q/zh-cn_image_0000002566757003.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002056Z&HW-CC-Expire=86400&HW-CC-Sign=9B6F1A86301C02D77F261DF6543FCE6072AF8CCC92EC8DC663BF68A5A7F2C898 "点击放大")

优化后效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/rxc4pJqESrOzJOEUN237rg/zh-cn_image_0000002535837220.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002056Z&HW-CC-Expire=86400&HW-CC-Sign=DA3F49247FA29E1DD86D7D9615CC56173ABD85590CBDE3199C2187FCF043BA19 "点击放大")

## 为多设备配置旋转策略

随着设备的多样化，应用某些页面需要根据设备类型配置不同的窗口旋转策略以达到极致的用户体验，为了开发者能快速适配不同设备，我们提供了多设备的窗口旋转策略。

### 背景

1. 不同设备对旋转策略的使用约束不同

   下述特定场景下，由于产品定义与使用场景的不同，开发者自定义的窗口策略可能会显著降低用户体验，因此系统配置的窗口策略优先级会高于应用配置。此时，应用实际显示的窗口方向将由系统统一调度，开发者自定义的窗口策略将被覆盖而不生效。

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

| 产品类型 | 手机 | 阔折叠（Pura X） | 双折叠（Mate X系列） | 三折叠（Mate XT系列） | 平板 | 电脑 |
| --- | --- | --- | --- | --- | --- | --- |
| 是否支持横竖屏旋转 | 不支持 | 内屏：不支持  外屏：不支持 | 内屏：支持  外屏：不支持 | F态（单屏显示）：不支持  M态（双屏显示）：支持  G态（三屏显示）：支持 | 支持 | 应用无法配置窗口旋转策略 |

对于某些应用，在直板手机上默认采用竖屏显示策略，但在平板或折叠屏设备上，需支持自动旋转。若在Ability的生命周期中调用setPreferredOrientation，可能会导致应用启动时出现旋转动画。因此，可通过修改module.json5配置文件中的orientation属性，设置为FOLLOW\_DESKTOP，以跟随桌面的旋转模式。

### 实现响应式旋转策略

在设备切换形态时，有时应用对于相同页面希望采用不同的旋转策略，这时需要通过监听设备的窗口尺寸变化配合系统断点实现响应式旋转策略，至于断点与设备的映射关系，请先了解”[响应式布局](bpta-multi-device-responsive-layout.md)“。

1.在应用EntryAbility的onWindowStageCreate生命周期中，通过on('windowSizeChange')方法监听窗口尺寸变化，在其回调中通过getWindowWidthBreakpoint()及getWindowHeightBreakpoint()实时获取存储横竖断点变化信息，配合各个页面实现响应式旋转策略。

```
1. export default class EntryAbility extends UIAbility {
2. uiContext?: UIContext;
3. onWindowSizeChange: (windowSize: window.Size) => void = () => {
4. let widthBp: WidthBreakpoint = this.uiContext!.getWindowWidthBreakpoint();
5. AppStorage.setOrCreate(CommonConstants.WIDTH_BREAK_POINT, widthBp);
6. let heightBp: HeightBreakpoint = this.uiContext!.getWindowHeightBreakpoint();
7. AppStorage.setOrCreate(CommonConstants.HEIGHT_BREAK_POINT, heightBp);
8. }

10. // ...

12. onWindowStageCreate(windowStage: window.WindowStage): void {
13. // ...

15. windowStage.loadContent('pages/Index', (err) => {
16. // ...

18. windowStage.getMainWindow().then((data: window.Window) => {
19. try {
20. this.uiContext = data.getUIContext();
21. } catch (err) {
22. Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
23. }

25. let widthBp: WidthBreakpoint = this.uiContext!.getWindowWidthBreakpoint();
26. AppStorage.setOrCreate(CommonConstants.WIDTH_BREAK_POINT, widthBp);

28. let heightBp: HeightBreakpoint = this.uiContext!.getWindowHeightBreakpoint();
29. AppStorage.setOrCreate(CommonConstants.HEIGHT_BREAK_POINT, heightBp);

31. data.on('windowSizeChange', this.onWindowSizeChange);
32. }).catch((err: BusinessError) => {
33. hilog.error(0x0000, 'testTag', `Error occured, error code: ${err.code}, error message: ${err.message}`);
34. })

36. });
37. }

39. // ...
40. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/WindowOrientation/blob/master/products/default/src/main/ets/entryability/EntryAbility.ets#L25-L96)

2.在需要实现响应式旋转策略页面的aboutToAppear生命周期中，通过on('windowSizeChange')方法监听窗口尺寸变化，在其回调中实时获取设备的窗口尺寸变化信息。

```
1. @Component
2. export struct VideoDetail {
3. windowObj: window.Window | undefined = undefined;
4. // ...

6. aboutToAppear() {
7. try {
8. this.windowObj = (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync()
9. } catch (err) {
10. Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
11. }

13. // ...
14. this.windowObj?.on('windowSizeChange', this.onWindowSizeChange);

16. // ...
17. }
18. // ...
19. }
```

[VideoDetail.ets](https://gitcode.com/HarmonyOS_Samples/WindowOrientation/blob/master/features/video/src/main/ets/views/VideoDetail.ets#L38-L237)

并在aboutToDisappear中取消监听：

```
1. async aboutToDisappear() {
2. // ...
3. this.windowObj?.off('windowSizeChange')
4. }
```

[VideoDetail.ets](https://gitcode.com/HarmonyOS_Samples/WindowOrientation/blob/master/features/video/src/main/ets/views/VideoDetail.ets#L133-L144)

3.在页面windowSizeChange回调方法中，配合全局横竖断点变化，保证页面切换时不同设备上配置合适的窗口策略。

```
1. @Component
2. export struct VideoDetail {
3. // ...
4. @StorageLink(CommonConstants.WIDTH_BREAK_POINT) widthBp: WidthBreakpoint = WidthBreakpoint.WIDTH_SM;
5. @StorageLink(CommonConstants.HEIGHT_BREAK_POINT) heightBp: HeightBreakpoint = HeightBreakpoint.HEIGHT_SM;
6. // ...

8. // ...

10. private onWindowSizeChange: (windowSize: window.Size) => void = () => {
11. if (this.isClick) {
12. return;
13. }
14. if (this.widthBp === WidthBreakpoint.WIDTH_SM) {
15. this.isFullScreen = false
16. this.windowObj?.setPreferredOrientation(window.Orientation.AUTO_ROTATION_UNSPECIFIED)
17. .catch((err: BusinessError) => {
18. Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
19. });
20. }

22. if (this.widthBp === WidthBreakpoint.WIDTH_MD && this.heightBp === HeightBreakpoint.HEIGHT_SM) {
23. this.isFullScreen = true;
24. }
25. };

27. // ...

29. build() {
30. // ...
31. }
```

[VideoDetail.ets](https://gitcode.com/HarmonyOS_Samples/WindowOrientation/blob/master/features/video/src/main/ets/views/VideoDetail.ets#L39-L238)

在折叠屏设备上，通过display.on('foldStatusChange', callback())方法监听折叠的状态，并通过@StorageLink('isHalfFolded')保存并实时更新全局变量。

```
1. @Component
2. export struct VideoPlayer {
3. // ...
4. @StorageLink('isHalfFolded') isHalfFolded: boolean = false;
5. // ...
6. private onFoldStatusChange: Callback<display.FoldStatus> = (data: display.FoldStatus) => {
7. this.foldStatus = data;
8. if (canIUse('SystemCapability.Window.SessionManager')) {
9. if (data === display.FoldStatus.FOLD_STATUS_EXPANDED || data === display.FoldStatus.FOLD_STATUS_FOLDED ||
10. data === display.FoldStatus.FOLD_STATUS_EXPANDED_WITH_SECOND_EXPANDED ||
11. data === display.FoldStatus.FOLD_STATUS_FOLDED_WITH_SECOND_EXPANDED) {
12. let widthBp: WidthBreakpoint = this.getUIContext().getWindowWidthBreakpoint();
13. AppStorage.setOrCreate(CommonConstants.WIDTH_BREAK_POINT, widthBp);
14. let heightBp: HeightBreakpoint = this.getUIContext().getWindowHeightBreakpoint();
15. AppStorage.setOrCreate(CommonConstants.HEIGHT_BREAK_POINT, heightBp);
16. }
17. if (data === display.FoldStatus.FOLD_STATUS_FOLDED_WITH_SECOND_EXPANDED && this.isFullScreen) {
18. this.windowObj?.setPreferredOrientation(window.Orientation.AUTO_ROTATION_LANDSCAPE_RESTRICTED)
19. .catch((err: BusinessError) => {
20. Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
21. });
22. } else {
23. this.windowObj?.setPreferredOrientation(window.Orientation.AUTO_ROTATION_UNSPECIFIED)
24. .catch((err: BusinessError) => {
25. Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
26. });
27. }
28. }
29. };

31. aboutToAppear(): void {
32. // ...
33. if (canIUse('SystemCapability.Window.SessionManager')) {
34. try {
35. display.on('foldStatusChange', this.onFoldStatusChange);
36. } catch (error) {
37. let err = error as BusinessError;
38. Logger.error('VideoPlayer', `onFoldStatusChange failed, code = ${err.code}, message = ${err.message}`);
39. }
40. }
41. }
42. // ...

44. build() {
45. // ...
46. }
```

[VideoPlayer.ets](https://gitcode.com/HarmonyOS_Samples/WindowOrientation/blob/master/features/video/src/main/ets/components/VideoPlayer.ets#L23-L334)

## 优化横竖屏切换性能

在窗口旋转时，屏幕尺寸变化会导致界面重新布局。为提高横竖屏切换的流畅度，需进行性能优化。

**使用自定义组件冻结**

旋转时，由于整窗一起旋转，会导致页面重新布局，但是实际上需要展示的可能只有播放内容，对于其他的组件可以使用自定义组件冻结功能，避免由于旋转导致的UI更新操作。例如视频播放底下的详情内容，可能是单独的组件。

```
1. @Component({ freezeWhenInactive: true })
2. // Added custom component freezing function
3. struct VideoDetailView {
4. build() {
5. Scroll() {
6. // ...
7. }
8. }
9. }
```

[VideoPlayView.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitioninpage/VideoPlayView.ets#L297-L310)

**对图片使用autoResize**

如果当前旋转页面存在一些图片，未经合理的裁剪，图片过大，可以对图片设置autoResize属性，使图片裁剪到合适的大小进行绘制。该属性是将组件显示区域作为绘制的图源尺寸，以减少内存占用。例如原图是1920\*1080，但是显示区域是200\*100，则在解码时会降低采样编码到200\*100尺寸。

```
1. @Builder
2. function ImageItem(imageSrc: ResourceStr) {
3. Stack({}) {
4. Image(imageSrc)
5. .width('100%')
6. .height('100%')
7. .autoResize(true)// Use auto_resize attributes on images
8. .borderRadius(8)
9. .objectFit(ImageFit.Fill)
10. .backgroundColor('#1AFFFFFF')
11. }
12. }
```

[VideoPlayView.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitioninpage/VideoPlayView.ets#L314-L326)

**排查一些耗时操作**

排查当前页面是否存在冗余的OnAreaChange事件、blur模糊或linearGradient属性，这些属性较为耗时，应根据是否必须使用来决定是否进行优化。

## 典型场景

以窗口旋转策略实现的五个高频场景为载体，通过窗口级配置实现多设备的窗口方向变化。

### 应用首页案例

应用首页通常支持横屏与竖屏显示。但是在类直板机上横屏的用户体验不好，所以直板机始终竖屏显示；在非类直板机（如平板、双折叠展开态、三折叠M/G态）支持竖屏与横屏展示。体验标准如下：

| 体验标准 | 仅竖屏 | 支持自由旋转，受开关控制 |
| --- | --- | --- |
| 支持设备形态 | 直板机、双折叠折叠态、三折叠F态 | 双折叠展开态、三折叠M/G态、平板 |
| 效果图 |  |  |

对于市场上大多数应用的首页用户行为及体验，推荐使用FOLLOW\_DESKTOP策略，以满足应用在不同设备上的窗口策略需求。同时，FOLLOW\_DESKTOP支持在同设备的折叠状态切换时，窗口策略自动更新。例如，三折叠F态仅支持竖屏，切换至三折叠M态时，自动变为自由旋转，并受控制中心旋转开关的控制。

首先，需对应用启动时的旋转策略进行设置，具体可参考[配置module.json5文件中的orientation字段](bpta-landscape-and-portrait-development.md#section1188593118171)。以实现多开发为例，为满足直板机和平板设备的不同策略，设置为follow\_desktop，此字段主要解决不同设备上默认旋转策略差异的问题。

在具体需要实现横竖屏切换的页面上，采用window窗口提供的设置窗口方向的能力，通过[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)将窗口显示的方向修改为横屏或竖屏的状态。

具体如下：通过getContext获取对应的UIAbilityContext，并通过context获取对应的windowStage实例，然后通过windowStage.getMainWindowSync同步方法拿到对应的窗口实例win，然后调用[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)方法设置窗口方向。

```
1. @Component
2. export struct Home {
3. windowObj: window.Window | undefined = undefined;
4. // ...

6. aboutToAppear(): void {
7. this.tabBarsInfo.setTabList(TabBarsInfo);
8. try {
9. this.windowObj = (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync()
10. } catch (err) {
11. Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
12. }

14. this.windowObj?.setPreferredOrientation(window.Orientation.FOLLOW_DESKTOP)
15. .catch((err: BusinessError) => {
16. Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
17. });
18. // ...
19. }

21. // ...

23. build() {
24. // ...
25. }
26. }
```

[Home.ets](https://gitcode.com/HarmonyOS_Samples/WindowOrientation/blob/master/features/home/src/main/ets/views/Home.ets#L27-L186)

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

在个股详情页面上，在aboutToAppear生命周期中采用window窗口提供的设置窗口方向的能力，通过[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)设置窗口策略为FOLLOW\_DESKTOP，在aboutToDisappear中恢复上级页面的窗口策略。

```
1. @Component
2. export struct StockDetail {
3. windowObj: window.Window | undefined = undefined;
4. // ...

6. aboutToAppear(): void {
7. try {
8. this.windowObj = (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync()
9. } catch (err) {
10. Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
11. }

13. this.windowObj?.setPreferredOrientation(window.Orientation.FOLLOW_DESKTOP)
14. .catch((err: BusinessError) => {
15. Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
16. });
17. }

19. aboutToDisappear() {
20. this.windowObj?.setPreferredOrientation(window.Orientation.UNSPECIFIED)
21. .catch((err: BusinessError) => {
22. Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
23. });
24. }

26. build() {
27. // ...
28. }
29. }
```

[StockDetail.ets](https://gitcode.com/HarmonyOS_Samples/WindowOrientation/blob/master/features/stock/src/main/ets/views/StockDetail.ets#L31-L324)

股票K线图页通常仅横屏显示，支持横屏旋转，且受控制中心的旋转开关控制。体验标准如下：

| 体验标准 | 横屏旋转，受开关控制 |
| --- | --- |
| 支持设备形态 | 直板机、双折叠折叠态、三折叠F/M/G态、平板 |
| 效果图 |  |

**示例代码**

在K线图页的aboutToAppear()和aboutToDisappear()生命周期中调用window.setPreferredOrientation()，设置K线图页显示时窗口策略为AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED，K线图页返回时恢复窗口策略为FOLLOW\_DESKTOP。

```
1. aboutToAppear(): void {
2. try {
3. this.windowObj = (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync()
4. } catch (err) {
5. Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
6. }

8. this.windowObj?.setPreferredOrientation(window.Orientation.AUTO_ROTATION_LANDSCAPE_RESTRICTED)
9. .catch((err: BusinessError) => {
10. Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
11. });
12. }

14. aboutToDisappear(): void {
15. this.windowObj?.setPreferredOrientation(window.Orientation.FOLLOW_DESKTOP)
16. .catch((err: BusinessError) => {
17. Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
18. });
19. }
```

[ABAWindow.ets](https://gitcode.com/HarmonyOS_Samples/WindowOrientation/blob/master/features/stock/src/main/ets/views/ABAWindow.ets#L37-L55)

### 视频详情页 & 全屏播放页案例

视频详情页通常支持横屏与竖屏显示。但是在直板机上反向竖屏的用户体验不好，所以直板机只能旋转至竖屏、横屏、反向横屏三个方向，且横屏时自动显示全屏播放页，竖屏时自动显示视频详情页；在非类直板机（如平板、双折叠展开态、三折叠M/G态）保持当前窗口方向，支持自由旋转，且受开关控制。体验标准如下：

| 体验标准 | 三方向旋转（竖屏/横屏/反向横屏），受开关控制 | 自由旋转，受开关控制 |
| --- | --- | --- |
| 支持设备形态 | 直板机、双折叠折叠态、三折叠F态 | 双折叠展开态、三折叠M/G态、平板 |
| 效果图 |  |  |

全屏播放页通常仅横屏显示，支持横屏旋转，且受控制中心的旋转开关控制。在类直板机上，当用户点击全屏按钮进入全屏播放页只能旋转至横屏和反向横屏两个方向，而打开旋转开关旋转至横屏或反向横屏进入全屏播放页则需要支持旋转至竖屏时切换到视频详情页；在双折叠展开态（接近正方形）可以四个方向自由旋转，且受开关控制。体验标准如下：

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

要实现以上效果，可以使用窗口的能力设置orientation的枚举类型进行相应的旋转，为了提供临时设置方向的能力，当用户手动点击全屏按钮时，需要手动触发横竖屏切换。如果此时关闭了旋转锁定，窗口需要能够跟随传感器旋转。因此，荐视频详情页使用AUTO\_ROTATION\_UNSPECIFIED策略，三折叠展开态及平板的全屏播放页使用AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED策略，临时调用旋转，并让其后续支持跟随传感器。

在视频详情页中，设置窗口方向为AUTO\_ROTATION\_UNSPECIFIED：

```
1. @Component
2. export struct VideoDetail {
3. windowObj: window.Window | undefined = undefined;
4. // ...

6. aboutToAppear() {
7. try {
8. this.windowObj = (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync()
9. } catch (err) {
10. Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
11. }

13. // ...

15. this.windowObj?.setPreferredOrientation(window.Orientation.AUTO_ROTATION_UNSPECIFIED)
16. .catch((err: BusinessError) => {
17. Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
18. });
19. }
20. // ...

22. build() {
23. // ...
24. }
25. }
```

[VideoDetail.ets](https://gitcode.com/HarmonyOS_Samples/WindowOrientation/blob/master/features/video/src/main/ets/views/VideoDetail.ets#L37-L236)

在 aboutToAppear()`生命周期中添加窗口尺寸变化的监听方法 on('windowSizeChange', callback)，当窗口尺寸变化时，通过窗口断点判断当前设备的横竖屏状态，切换全屏状态或更新窗口策略；

监听视频详情页的全屏播放状态，在用户点击全屏播放按钮时，在回调方法 onFullScreenChange()`中判断当前设备的横竖屏状态，更新窗口策略，并在返回时恢复视频详情页的窗口策略。

```
1. @Component
2. export struct VideoDetail {
3. windowObj: window.Window | undefined = undefined;
4. @StorageLink('isFullScreen') @Watch('onFullScreenChange') isFullScreen: boolean = false;
5. // ...

7. aboutToAppear() {
8. // ...
9. this.windowObj?.on('windowSizeChange', this.onWindowSizeChange);

11. // ...
12. }
13. onFullScreenChange(): void {
14. if (this.isFullScreen) {
15. if (this.isClick) {
16. if (this.widthBp === WidthBreakpoint.WIDTH_SM || this.widthBp === WidthBreakpoint.WIDTH_LG ||
17. this.heightBp === HeightBreakpoint.HEIGHT_LG) {
18. this.windowObj?.setPreferredOrientation(window.Orientation.AUTO_ROTATION_LANDSCAPE_RESTRICTED)
19. .catch((err: BusinessError) => {
20. Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
21. });
22. }
23. }
24. } else {
25. this.windowObj?.setPreferredOrientation(window.Orientation.AUTO_ROTATION_UNSPECIFIED)
26. .catch((err: BusinessError) => {
27. Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
28. });
29. }
30. }

32. private onWindowSizeChange: (windowSize: window.Size) => void = () => {
33. if (this.isClick) {
34. return;
35. }
36. if (this.widthBp === WidthBreakpoint.WIDTH_SM) {
37. this.isFullScreen = false
38. this.windowObj?.setPreferredOrientation(window.Orientation.AUTO_ROTATION_UNSPECIFIED)
39. .catch((err: BusinessError) => {
40. Logger.error(`Invoke set preferred orientation failed, code is ${err.code}, message is ${err.message}`)
41. });
42. }

44. if (this.widthBp === WidthBreakpoint.WIDTH_MD && this.heightBp === HeightBreakpoint.HEIGHT_SM) {
45. this.isFullScreen = true;
46. }
47. };

49. // ...

51. build() {
52. // ...
53. }
54. }
```

[VideoDetail.ets](https://gitcode.com/HarmonyOS_Samples/WindowOrientation/blob/master/features/video/src/main/ets/views/VideoDetail.ets#L36-L235)

## 常见问题

### display与window的区别

* 屏幕（[@ohos.display (屏幕属性)](../harmonyos-references/js-apis-display.md)）指物理或逻辑的显示设备，是显示内容的整体区域。例如：
  + 物理屏幕：显示器、手机屏幕、投影仪等硬件设备。
  + 逻辑屏幕：操作系统虚拟的多屏幕环境（如扩展桌面）。
* 窗口（window）是运行在屏幕上的一个可交互的图形界面区域，属于软件层面。例如：
  + 应用程序窗口（如浏览器、文件夹窗口）。
  + 对话框、工具栏等子窗口。

### display.Orientation与window.Orientation的区别

* display的[Orientation](../harmonyos-references/js-apis-display.md#orientation10)表示屏幕当前横竖显示方向，屏幕的横竖显示方向只能获取，不能设置，客观体现了当前屏幕的显示状态。
* window.Orientation表示窗口旋转策略，窗口旋转策略可以由开发者设置，系统会根据开发者的预设策略进行相应的旋转。

对于开发者而言，控制应用的显示方向应该通过设置window.Orientation实现。

### display.rotation的定义

[Display](../harmonyos-references/js-apis-display.md#display)的属性rotation表示显示设备的屏幕顺时针旋转角度。使用场景：适用于和硬件设备角度强关联的场景，如相机预览角度补偿。

rotation的取值有4种，分别对应下图所示的4个方向（以直板机为例）。如果需要更精准的角度信息，则需要配合设备sensor获取。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/XAJXkSJYTx2DzXxHkk8WFg/zh-cn_image_0000002535837336.png?HW-CC-KV=V1&HW-CC-Date=20260428T002056Z&HW-CC-Expire=86400&HW-CC-Sign=F69D0E2241DCB2C6ED3147B5BE1C136DE436D1B0644BEF639BF769EEB2F5246A "点击放大")

| 值 | 含义 |
| --- | --- |
| 0 | 显示设备屏幕顺时针旋转为0°。 |
| 1 | 显示设备屏幕顺时针旋转为90°。 |
| 2 | 显示设备屏幕顺时针旋转为180°。 |
| 3 | 显示设备屏幕顺时针旋转为270°。 |

### window.getLastWindow的方式获取窗口出现延迟

1. 由于getLastWindow底层原因，需要经过查找获取实例，一定程度上会有性能损耗，可能会出现已经发生横屏或者竖屏切换的情况下，状态栏还没切换的情况。
2. 使用windowStage.getMainWindowSync的同步方法获取窗口实例。

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

### 竖屏时进入任务中心，进入横屏的应用，在onPageShow时获取的display信息不符合预期

目前display接口规则还不够清晰，建议使用window的getWindowProperties()接口处理。

### 如何获取屏幕的宽度、高度、分辨率和横竖屏等信息

引入屏幕属性模块，可以通过调用[display.getDefaultDisplaySync()](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)方法获取display对象后，从而获取到屏幕的宽度、高度、分辨率和横竖屏等信息。

### window.orientation与display.rotation的关系

窗口的orientation和屏幕rotation并没有直接关联关系，在使用上也不能相互替代，否则在多设备适配场景下可能会出现兼容性问题。以三折叠不同形态下的window.orientation与display.rotation映射关系为例说明。在rotation为0度的情况下，window.orientation可能是竖屏也可能是横屏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/7k-uFA8rRCK0vS8sDvfuog/zh-cn_image_0000002535997274.png?HW-CC-KV=V1&HW-CC-Date=20260428T002056Z&HW-CC-Expire=86400&HW-CC-Sign=2EB22C8434675460DDA6992607E89476B2699011C341D750DE7FB74E9895B6ED "点击放大")

## 示例代码

* [窗口方向](https://gitcode.com/HarmonyOS_Samples/WindowOrientation)
