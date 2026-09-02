---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-mode-overview
title: 窗口模式简介
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口模式 > 窗口模式简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:22+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:da159977a7b401468e6c87229fbd01e175febd12d0e063ef706af2d62d01ec5d
---

## 场景介绍

窗口模式指窗口在设备屏幕上的显示状态，包括全屏、最大化、最小化、自由悬浮窗口和分屏多种模式，是单个窗口的属性。

通过合理配置和使用窗口模式，应用可以更好地适配不同设备形态和用户交互场景，提供更优质的多窗口体验。

[智慧多窗](multi-window-intro.md)是一个多种窗口模式组合使用的实践范例，它允许用户在同一时间、同一屏幕上以悬浮窗、分屏或全景多窗的方式同时运行多个应用窗口，从而实现多任务处理。

窗口模式能力支持用户同时使用多个应用窗口，这种能力在[自由窗口](freeform-window-overview.md#自由窗口)状态和非[自由窗口](freeform-window-overview.md#自由窗口)状态下存在差异：

* 仅主窗及[自由窗口](freeform-window-overview.md#自由窗口)状态下的子窗支持配置窗口模式策略。
* 全局悬浮窗（即WindowType.TYPE\_FLOAT）、模态窗口（即WindowType.TYPE\_DIALOG）、非[自由窗口](freeform-window-overview.md#自由窗口)状态下的子窗以及系统窗口固定为自由悬浮窗口模式，不存在窗口模式切换。

可通过以下章节了解窗口模式基础能力、自由窗口适配等详细内容。

## 窗口模式WindowStatusType

窗口模式通过[WindowStatusType](../harmonyos-references/arkts-apis-window-e.md#windowstatustype11)枚举来描述，该枚举定义了应用窗口在不同场景下的显示状态。开发者可以根据应用需求选择合适的窗口模式，或动态监听窗口模式变化以进行相应的适配处理。下文将详细介绍各个窗口模式的特点、窗口模式变化的感知以及窗口模式策略的配置方式。

**说明** 

除了非[自由窗口](freeform-window-overview.md#自由窗口)状态下固定支持主窗口的FULL\_SCREEN模式外，其他各种窗口模式需提前配置相应的支持策略后才可触发。

### FULL\_SCREEN

全屏模式是指应用窗口铺满整个屏幕的显示状态。

**特点：**

* 窗口占据整个屏幕空间。
* 在[自由窗口](freeform-window-overview.md#自由窗口)状态下，窗口铺满整个屏幕，默认无dock栏、标题栏和状态栏显示。
* 在非[自由窗口](freeform-window-overview.md#自由窗口)状态下，窗口铺满整个屏幕，无标题栏和dock栏显示。

**适用场景：**

* 沉浸式体验的应用，如视频播放、游戏等。
* 需要最大化利用屏幕空间的应用场景。

**触发方式：**

* [自由窗口](freeform-window-overview.md#自由窗口)状态下：

  + 应用调用[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability-1)时，配置[StartOptions](../harmonyos-references/js-apis-app-ability-startoptions.md#startoptions)中的windowMode为AbilityConstant.WindowMode.WINDOW\_MODE\_FULLSCREEN。
  + 应用调用[maximize()](../harmonyos-references/arkts-apis-window-window.md#maximize12)接口，使用window.MaximizePresentation.ENTER\_IMMERSIVE或window.MaximizePresentation.ENTER\_IMMERSIVE\_DISABLE\_TITLE\_AND\_DOCK\_HOVER枚举入参。
  + 用户点击系统标题栏中的最大化按钮。
* 非[自由窗口](freeform-window-overview.md#自由窗口)状态下，应用主窗口启动时默认进入FULL\_SCREEN显示模式。

### MAXIMIZE

最大化模式是指应用窗口在[自由窗口](freeform-window-overview.md#自由窗口)状态下铺满整个屏幕，但保留dock栏、状态栏和标题栏的显示状态。

**特点：**

* 窗口占据整个屏幕空间，不需要hover就可以显示dock栏、状态栏和标题栏。
* 仅在[自由窗口](freeform-window-overview.md#自由窗口)状态下存在该模式。

**适用场景：**

[自由窗口](freeform-window-overview.md#自由窗口)状态下需要全屏显示但保持dock栏、状态栏和标题栏可见。

**触发方式：**

* [自由窗口](freeform-window-overview.md#自由窗口)状态下，应用在module.json5文件的metadata中将"ohos.ability.window.isMaximize"字段配置为true，应用主窗口启动将以MAXIMIZE模式启动。
* [自由窗口](freeform-window-overview.md#自由窗口)状态下，应用调用[maximize()](../harmonyos-references/arkts-apis-window-window.md#maximize12)接口，使用window.MaximizePresentation.EXIT\_IMMERSIVE枚举入参。

**说明** 

* 应用子窗口仅在[自由窗口](freeform-window-overview.md#自由窗口)状态下支持FULL\_SCREEN与MAXIMIZE模式，且需要在创建子窗时将maximizeSupported参数配置为true；或者通过[setSupportedWindowModes()](../harmonyos-references/arkts-apis-window-window.md#setsupportedwindowmodes)配置支持。
* FULL\_SCREEN与MAXIMIZE的主要差异：

  + FULL\_SCREEN：窗口铺满整个屏幕；在[自由窗口](freeform-window-overview.md#自由窗口)状态下，无dock栏、状态栏和标题栏显示；在非[自由窗口](freeform-window-overview.md#自由窗口)状态下，无dock栏和标题栏显示。
  + MAXIMIZE：窗口铺满整个屏幕，有dock栏、状态栏和标题栏显示。
  + MAXIMIZE模式仅在[自由窗口](freeform-window-overview.md#自由窗口)状态下生效。

### MINIMIZE

最小化模式是指应用窗口缩小到任务栏或dock栏，不在屏幕上显示内容的状态。

**特点：**

* 窗口内容不可见，窗口生命周期进入后台状态。
* 用户可以通过任务栏或dock栏重新激活窗口。

**适用场景：**

* 用户需要暂时隐藏窗口，但希望窗口可快速恢复之前的显示内容。
* 需要在后台继续处理某些业务逻辑的应用。

**触发方式：**

* 应用调用[minimize()](../harmonyos-references/arkts-apis-window-window.md#minimize11)接口。
* 用户点击系统标题栏中的最小化按钮。

### FLOATING

自由悬浮窗口模式是指应用窗口以自由悬浮窗口的形式显示，可以自由调整窗口的大小和位置。

在[自由窗口](freeform-window-overview.md#自由窗口)状态下和非[自由窗口](freeform-window-overview.md#自由窗口)状态下，自由悬浮窗口模式具有不同的特点和使用场景。

* **自由窗口状态下**

  自由窗口状态下，自由悬浮窗口在屏幕上可以按自由大小、位置显示，支持拖拽移动、拖拽缩放和分屏组合，从而实现多任务处理。

  **特点：**

  + 应用可通过[resize()](../harmonyos-references/arkts-apis-window-window.md#resize9)、[moveWindowTo()](../harmonyos-references/arkts-apis-window-window.md#movewindowto9-1)等接口改变自由悬浮窗口大小和位置。
  + 同一屏幕上可同时显示多个自由悬浮窗口。
  + [自由窗口](freeform-window-overview.md#自由窗口)状态下应用主窗口默认带有标题栏和三键控制按钮（最大化/还原、最小化、关闭），可以通过拖动窗口边缘调节窗口大小，通过拖动标题栏移动窗口位置。
  + 全局悬浮窗、模态窗口及系统窗口固定以自由悬浮窗口模式显示，无法切换窗口模式。

  **适用场景：**

  + 多任务并行处理的场景。
  + 需要同时查看多个应用内容的场景。

  **触发方式：**

  + [自由窗口](freeform-window-overview.md#自由窗口)状态下，窗口启动时默认进入FLOATING显示模式。
  + 当窗口在全屏、分屏模式时，应用调用[recover()](../harmonyos-references/arkts-apis-window-window.md#recover11)接口。
  + 当窗口在全屏、分屏模式时，用户点击系统标题栏中的还原按钮。
* **非自由窗口状态下**

  非自由窗口状态下的自由悬浮窗口在屏幕上可以按自由位置显示，但不同窗口类型在自由悬浮窗口模式下的能力存在差异。

  **特点：**

  + 对于应用主窗口：

    - 应用主窗口仅在进入智慧多窗悬浮窗或全景多窗后，窗口处于自由悬浮窗口模式，详见[智慧多窗简介](multi-window-intro.md)。
    - 不支持通过[resize()](../harmonyos-references/arkts-apis-window-window.md#resize9)、[moveWindowTo()](../harmonyos-references/arkts-apis-window-window.md#movewindowto9-1)等接口自由改变窗口大小和位置。
    - 同一屏幕上存在自由悬浮窗口的最大个数限制，超出限制时，打开新的自由悬浮窗口会替换最久未操作的自由悬浮窗口。最大个数限制在不同产品上存在差异，详见[智慧多窗简介](multi-window-intro.md)的“悬浮窗”及“全局多窗”章节。
    - 主窗在自由悬浮窗口模式下固定存在顶部横条，用户可通过拖拽顶部横条移动该窗口、切换窗口模式等。
    - 用户可通过拖拽窗口边缘对窗口进行缩放。
  + 对于应用子窗口、全局悬浮窗、模态窗口及系统窗口：

    - 固定以自由悬浮窗口模式显示，无法切换窗口模式。
    - 支持通过[resize()](../harmonyos-references/arkts-apis-window-window.md#resize9)、[moveWindowTo()](../harmonyos-references/arkts-apis-window-window.md#movewindowto9-1)等接口自由改变窗口大小和位置。
    - 无同时显示的最大个数限制，但受窗口最大数量限制（系统限制，当前单个应用进程中的窗口最大数量限制为256）。
    - 无顶部横条。

  **适用场景：**

  + 多任务并行处理的场景。
  + 需要同时查看多个应用内容的场景。

  **触发方式：**

  用户触发：包含通过悬浮窗手势触发、通知消息启动应用、侧边Dock启动应用、顶部横条切换等方式。详细内容可见[智慧多窗简介](multi-window-intro.md)中“悬浮窗的触发及恢复方式”章节。

  **说明** 

  更多关于智慧多窗悬浮窗的信息，请参考[智慧多窗简介](multi-window-intro.md)和[智慧多窗最佳实践](../best-practices/bpta-multi-window-practice.md)。

### SPLIT\_SCREEN

分屏模式是指应用窗口占据屏幕的某个部分，与另一个窗口同时显示的状态。当前支持应用内分屏及应用间分屏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/JrxhTWPxRDqjDme-k9lJDQ/zh-cn_image_0000002706674080.png)

**特点：**

* 分屏窗口按照左右或上下布局排列。
* 两个分屏窗口之间具有分界线。可通过拖拽分界线调整两个部分的窗口尺寸。
* 仅主窗支持分屏。
* 当前仅支持二分屏。

**适用场景：**

多个应用长时间并行使用的场景，如一边查看文档一边编写邮件、多应用商品比价等。

**触发方式：**

* 应用在前台调用[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability-1)时，配置[StartOptions](../harmonyos-references/js-apis-app-ability-startoptions.md#startoptions)中的windowMode为WINDOW\_MODE\_SPLIT\_PRIMARY或WINDOW\_MODE\_SPLIT\_SECONDARY（新拉起的应用主窗在[自由窗口](freeform-window-overview.md#自由窗口)下进入待分屏状态，在非[自由窗口](freeform-window-overview.md#自由窗口)下与调用方应用主窗形成分屏）。
* 用户触发：[自由窗口](freeform-window-overview.md#自由窗口)状态下，可通过点击窗口系统标题栏三键区域、拖拽窗口到分屏热区的方式触发。非[自由窗口](freeform-window-overview.md#自由窗口)状态下，可通过分屏手势、点击顶部横条切换的方式触发。

## 获取与监听窗口模式

应用可以通过查询窗口模式、监听窗口模式变化事件来感知当前窗口状态的改变，并据此进行相应的业务适配。

系统提供了以下相关查询和监听接口。

| 接口 | 功能描述 | 触发时机 | 适用场景 |
| --- | --- | --- | --- |
| [getWindowStatus()](../harmonyos-references/arkts-apis-window-window.md#getwindowstatus12) | 获取当前应用窗口的模式 | 应用主动调用 | 需要立即获取当前窗口模式进行判断的场景，如在执行某些窗口操作前，先判断当前窗口模式，避免在不支持的窗口模式下调用相关接口。 |
| [on('windowStatusChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowstatuschange11) | 开启窗口模式变化的监听 | 窗口模式变化时立即触发（此时窗口属性可能还没有更新） | 需要快速响应窗口模式变化，不依赖窗口属性的场景。 |
| [on('windowStatusDidChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowstatusdidchange20) | 开启窗口模式变化的监听 | 窗口模式变化且Rect属性更新完成后触发 | 需要在窗口模式变化后立即获取准确窗口大小和位置的场景。 |

## 定制窗口模式支持策略

应用可以通过多种方式配置窗口支持的模式，以满足不同设备和场景的需求。针对主窗、子窗窗口模式，提供了四种主要的配置方式，按优先级从高到低依次为：

| 优先级排序 | 配置方式 | 支持的窗口类型 | 生效范围 |
| --- | --- | --- | --- |
| 1 | [通过setSupportedWindowModes()接口配置](window-mode-overview.md#通过setsupportedwindowmodes接口配置) | 应用主窗口、应用子窗口 | 仅在自由窗口状态下生效 |
| 2 | [通过startAbility()接口配置](window-mode-overview.md#通过startability接口配置) | 应用主窗口 | 仅在自由窗口状态下生效 |
| 3 | [通过module.json5配置文件中abilities标签下的metadata标签配置](window-mode-overview.md#通过modulejson5配置文件中abilities标签下的metadata标签配置) | 应用主窗口 | 仅在自由窗口状态下生效 |
| 4 | [通过module.json5配置文件中abilities标签下的supportWindowMode属性配置](window-mode-overview.md#通过modulejson5配置文件中abilities标签下的supportwindowmode属性配置) | 应用主窗口 | 均生效 |

**说明** 

* 非[自由窗口](freeform-window-overview.md#自由窗口)状态下只能通过[module.json5配置文件](module-configuration-file.md)中[abilities标签](module-configuration-file.md#abilities标签)下的supportWindowMode属性配置窗口支持模式，其他配置方式均不生效。
* 非[自由窗口](freeform-window-overview.md#自由窗口)状态下，应用在[abilities标签](module-configuration-file.md#abilities标签)下配置的supportWindowMode属性中即使未包含FULL\_SCREEN，依然默认支持全屏模式显示。
* 在[自由窗口](freeform-window-overview.md#自由窗口)状态下，supportWindowMode中配置的FULL\_SCREEN模式，表示窗口支持windowStatusType.FULL\_SCREEN 和windowStatusType.MAXIMIZE两种显示模式。
* 多设备场景下不同窗口模式的开发与实现可以参考[窗口模式最佳实践](../best-practices/bpta-multi-device-window-mode.md)。

### 通过setSupportedWindowModes()接口配置

* 通过调用WindowStage.[setSupportedWindowModes()](../harmonyos-references/arkts-apis-window-windowstage.md#setsupportedwindowmodes15)传入supportedWindowModes或调用WindowStage.[setSupportedWindowModes()](../harmonyos-references/arkts-apis-window-windowstage.md#setsupportedwindowmodes20)接口传入supportedWindowModes和grayOutMaximizeButton，可以在运行时动态修改当前主窗口支持的窗口模式。
* 通过调用Window.[setSupportedWindowModes()](../harmonyos-references/arkts-apis-window-window.md#setsupportedwindowmodes)传入supportedWindowModes，可以在运行时动态修改当前主、子窗口支持的窗口模式。

支持配置的窗口模式如下所示：

| 配置值 | 模式 | 说明 |
| --- | --- | --- |
| SupportWindowMode.FULL\_SCREEN | 全屏模式 | 窗口支持全屏显示。 |
| SupportWindowMode.SPLIT | 分屏模式 | 主窗不支持仅配置SPLIT，需要配合FULL\_SCREEN和FLOATING一起使用，子窗不支持配置SPLIT。 |
| SupportWindowMode.FLOATING | 悬浮模式 | 窗口支持自由悬浮形式显示。 |

* 仅在[自由窗口](freeform-window-overview.md#自由窗口)状态下生效。
* 配置优先级最高，会覆盖其他配置方式。
* 适用于需要根据应用状态动态调整窗口模式的场景。

### 通过startAbility()接口配置

应用调用[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability-1)时可通过[StartOptions](../harmonyos-references/js-apis-app-ability-startoptions.md#startoptions)中的supportWindowMode参数，指定启动时窗口支持的模式。

**支持的模式值**（详见[bundleManager.SupportWindowMode](../harmonyos-references/js-apis-bundlemanager.md#supportwindowmode)）：

| 配置值 | 模式 | 说明 |
| --- | --- | --- |
| bundleManager.SupportWindowMode.FULL\_SCREEN | 全屏模式 | 窗口支持全屏显示。 |
| bundleManager.SupportWindowMode.SPLIT | 分屏模式 | 窗口支持分屏显示。 |
| bundleManager.SupportWindowMode.FLOATING | 自由悬浮窗口模式 | 窗口支持自由悬浮形式显示。 |

* 仅在[自由窗口](freeform-window-overview.md#自由窗口)状态下生效。
* 适用于主窗口启动时指定窗口模式。

### 通过module.json5配置文件中abilities标签下的metadata标签配置

通过[module.json5配置文件](module-configuration-file.md)中[abilities](module-configuration-file.md#abilities标签)标签下的[metadata标签](window-config-m.md#metadata标签)，可以设置窗口相关的元数据属性，包括自由多窗下的可支持窗口模式。

**配置项说明：**

| 配置项 | 说明 | 取值 |
| --- | --- | --- |
| name | 元数据名称 | "ohos.ability.window.supportWindowModeInFreeMultiWindow" |
| value | 支持的窗口模式 | 字符串，可配置多种模式，每个模式之间用逗号分隔，不区分顺序，不添加空格。支持配置的模式有：  - "fullscreen"：全屏模式，应用窗口铺满整个屏幕。  - "split"：分屏模式。应用窗口占据屏幕的某个部分，与另一个窗口同时显示。  - "floating"：自由悬浮窗口模式。应用窗口以悬浮窗口的形式显示。 |

* 仅在[自由窗口](freeform-window-overview.md#自由窗口)状态下生效。
* 适用于配置应用在自由窗口状态下默认的窗口模式支持范围。
* 可缺省，缺省值为"fullscreen, split, floating"。

### 通过module.json5配置文件中abilities标签下的supportWindowMode属性配置

通过[module.json5配置文件](module-configuration-file.md)中[abilities](module-configuration-file.md#abilities标签)标签下的supportWindowMode属性，可以指定应用支持的窗口模式。

**支持的模式值：**

| 配置值 | 模式 | 说明 |
| --- | --- | --- |
| "fullscreen" | 全屏模式 | 应用窗口铺满整个屏幕。 |
| "split" | 分屏模式 | 应用窗口占据屏幕的某个部分，与另一个窗口同时显示。 |
| "floating" | 悬浮窗模式 | 应用窗口以悬浮窗口的形式显示。 |

* 可缺省，缺省值为["fullscreen", "split", "floating"]。
* 在[自由窗口](freeform-window-overview.md#自由窗口)状态和非[自由窗口](freeform-window-overview.md#自由窗口)状态下均生效。
* 非[自由窗口](freeform-window-overview.md#自由窗口)状态下，仅支持该种配置方式。
* 在[自由窗口](freeform-window-overview.md#自由窗口)状态下，相对于上文其他几种配置方式，此配置方式优先级最低。
* 在[自由窗口](freeform-window-overview.md#自由窗口)状态下同时配置"fullscreen"和"split"时，如果应用的[targetAPIVersion](app-configuration-file.md#配置文件标签)小于15，窗口将以悬浮窗模式启动；如果应用的[targetAPIVersion](app-configuration-file.md#配置文件标签)大于等于15，窗口将以全屏模式启动。
