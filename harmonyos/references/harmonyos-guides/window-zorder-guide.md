---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-zorder-guide
title: 窗口层级
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口基础能力 > 窗口层级
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:22+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:fda7c3a6289062d833ca0049959f8342e39072e3620c2fb91184dade09a7ad6c
---

## 场景介绍

**窗口层级**是指多个窗口在屏幕上的堆叠顺序，决定窗口的前后显示关系，通常称为**Z序（ZOrder）**。

ZOrder值越大，窗口越靠前显示，能够覆盖ZOrder值较小的窗口；反之，ZOrder值较小的窗口则可能被其他窗口遮挡。

对于三方应用，无法直接修改窗口的ZOrder，但可以通过控制**zLevel**属性来间接影响子窗口的显示层级。

系统通过管理ZOrder和zLevel实现对用户界面可见性与交互优先级的控制。

本节将从基本概念、层级规则、父子窗口关系、TopMost窗口机制以及相关接口示例五个方面，系统化阐述窗口层级管理机制。

## 基本概念与层级规则

### ZOrder与zLevel

**ZOrder**表示系统内部维护的窗口堆叠顺序。数值越大，窗口越靠前。三方应用不可直接修改ZOrder。

**zLevel**表示三方应用可控制的应用内子窗口之间的相对层级，仅针对非模态子窗口有效。zLevel取值范围为[-10000, 10000]，默认值为0。zLevel越高，对应的ZOrder越大，窗口越靠前。

### 窗口zLevel层级规则

* **不同zLevel的子窗口**

  + zLevel高的窗口始终覆盖zLevel低的窗口，即使点击zLevel较低的窗口，也不会将其抬升至zLevel更高的窗口之上。
* **相同zLevel的子窗口**

  + 默认后创建的窗口层级更高。
  + 用户点击某个子窗口时，该窗口的ZOrder会被提升至同zLevel中的最高位置，实现“点击置顶”。
  + 若调用[setRaiseByClickEnabled()](../harmonyos-references/arkts-apis-window-window.md#setraisebyclickenabled14)接口传入false，则禁用点击抬升功能，点击时层级保持不变。

### 窗口类型层级规则

* **相同类型窗口的层级调整**

  同类型窗口（多个主窗口、多个普通子窗）之间可通过点击或快捷键（如Alt+Tab）调整层级。
* **应用内子窗口类型的默认层级**

  系统为不同类型的子窗口分配了默认层级。优先级由高到低如下所示：

  | 窗口类型 | 创建方式 |
  | --- | --- |
  | 模应用子窗 | 调用[createSubWindowWithOptions()](../harmonyos-references/arkts-apis-window-window.md#createsubwindowwithoptions12)接口，并设置子窗口参数[SubWindowOptions](../harmonyos-references/arkts-apis-window-i.md#subwindowoptions11)中的isModal为true，modalityType为APPLICATION\_MODALITY。 |
  | Toast子窗 | 调用[showToast()](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showtoast)接口，并设置showMode为TOP\_MOST。 |
  | 文本菜单子窗 | 调用[showActionMenu()](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showactionmenu)接口，并设置showInSubWindow为true。 |
  | Dialog子窗 | 调用[openCustomDialog()](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)传入dialogContent、options参数，并设置showInSubWindow为true。  调用[openCustomDialog()](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12-1)传入options参数，并设置showInSubWindow为true。  调用[openCustomDialogWithController()](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialogwithcontroller18)，并设置showInSubWindow为true。 |
  | 模态子窗 | 调用[createSubWindowWithOptions()](../harmonyos-references/arkts-apis-window-window.md#createsubwindowwithoptions12)接口，并设置子窗口参数[SubWindowOptions](../harmonyos-references/arkts-apis-window-i.md#subwindowoptions11)中的isModal为true，modalityType为WINDOW\_MODALITY。 |
  | 普通子窗 | 调用[createSubWindowWithOptions()](../harmonyos-references/arkts-apis-window-window.md#createsubwindowwithoptions12)接口创建的默认子窗。 |

  不同类型窗口之间不能通过点击或API调整跨越层级范围。

### 父子窗口层级规则

* 当父窗口被抬升时，其所有子窗口也会随之抬升；当子窗口被抬升时，其父窗口也会随之抬升。
* 子窗口的层级始终高于其父窗口。
* 窗口抬升可通过调用[raiseToAppTop()](../harmonyos-references/arkts-apis-window-window.md#raisetoapptop14)接口或点击窗口实现。

### TopMost置顶窗口层级规则

* 在[自由窗口](window-terminology.md#freeform-window自由窗口)状态下，应用主窗口可通过调用[setWindowTopmost()](../harmonyos-references/arkts-apis-window-window.md#setwindowtopmost14)接口传入true将自身置于其他应用窗口之上，以实现“不被遮挡”的常驻显示效果，需合理使用，避免影响用户体验。
* 使用该接口需要申请权限ohos.permission.WINDOW\_TOPMOST。

## 窗口层级控制机制汇总表

| 特性/操作 | 控制方式 | 生效范围 | 适用场景 |
| --- | --- | --- | --- |
| ZOrder | 系统管理 | 可跨应用生效 | 内部渲染顺序管理 |
| zLevel | setSubWindowZLevel()/创建窗口时设置 | 仅同应用内生效 | 子窗口层级管理 |
| 窗口置顶 | setWindowTopmost() | 可跨应用生效 | 视频、导航等常驻窗口 |
| 点击抬升 | setRaiseByClickEnabled() | 可跨应用生效 | 防误触、固定布局 |

## 层级相关开发场景

| 功能 | 典型场景 | 对应接口 |
| --- | --- | --- |
| 设置主窗口置顶 | 用于实现将窗口置于其他应用窗口之上不被遮挡。如视频通话、导航等场景。 | [setWindowTopmost()](../harmonyos-references/arkts-apis-window-window.md#setwindowtopmost14) |
| 提升子窗口到顶层 | 将子窗口提升至当前应用内同类型子窗口的最顶层，只在当前应用同一个父窗口下相同zLevel值的子窗范围内生效。  例如，视频会议中的悬浮工具栏，主窗口是视频画面，子窗口包括聊天框、共享控制栏等。点击聊天框时，可调用raiseToAppTop()将其提升到顶层，避免被其他子窗口遮挡。 | [raiseToAppTop()](../harmonyos-references/arkts-apis-window-window.md#raisetoapptop14) |
| 禁止/使能子窗点击抬升功能 | 可用于固定布局的工具面板，防止用户误操作导致层级混乱。 | [setRaiseByClickEnabled()](../harmonyos-references/arkts-apis-window-window.md#setraisebyclickenabled14) |
| 获取当前应用内层级最高的窗口 | 可判断当前最前显示的窗口（可能是主窗口或子窗口），用于日志记录或状态同步等场景。 | [getLastWindow()](../harmonyos-references/arkts-apis-window-f.md#windowgetlastwindow9-1) |

**说明** 

* 合理设置zLevel，避免层级冲突。
* TopMost功能谨慎使用，避免干扰系统多窗口体验。
* 对于需要高优先级显示的关键界面，可通过[raiseToAppTop()](../harmonyos-references/arkts-apis-window-window.md#raisetoapptop14)确保可见性，使用此接口前，需确保该窗口已调用showWindow()类接口（[showWindow()](../harmonyos-references/arkts-apis-window-window.md#showwindow9-1)/[showWindow(options: ShowWindowOptions)](../harmonyos-references/arkts-apis-window-window.md#showwindow20)）并执行完毕。
* [setWindowTopmost()](../harmonyos-references/arkts-apis-window-window.md#setwindowtopmost14)仅在[自由窗口](window-terminology.md#freeform-window自由窗口)状态下生效。开发者可通过[isInFreeWindowMode()](../harmonyos-references/arkts-apis-window-window.md#isinfreewindowmode22)查询当前窗口是否处于自由窗口，并结合[on('freeWindowModeChange')](../harmonyos-references/arkts-apis-window-window.md#onfreewindowmodechange22)事件监听器实时监听窗口模式的变化，从而准确判断何时可以安全调用[setWindowTopmost()](../harmonyos-references/arkts-apis-window-window.md#setwindowtopmost14)。
