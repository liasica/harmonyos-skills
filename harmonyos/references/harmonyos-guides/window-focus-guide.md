---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-focus-guide
title: 窗口焦点
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口基础能力 > 窗口焦点
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:22+08:00
doc_updated_at: 2026-07-17
content_hash: sha256:5c409d82e74664e3d38c78ed1631467a83c8595556889be05cc7f8f9e977537b
---

## 场景介绍

**窗口焦点（Window Focus）** 是指在某一屏幕组内，当前能够接收键盘事件的窗口所具有的状态。系统通过焦点机制确保用户输入被正确路由到目标界面组件。

在一个屏幕组中，有且仅有一个窗口处于焦点状态，该窗口被称为**焦点窗口（Focused Window）** 。焦点窗口不仅能够响应键盘输入，还可在资源调度中享有更高优先级，例如在渲染、任务执行等方面获得系统倾斜。只有当窗口成功获取焦点后，系统方可拉起输入法进行输入。

## 基本概念和机制介绍

### 屏幕组

屏幕组是系统中一组逻辑上关联的显示区域，每个屏幕组独立维护其窗口栈和焦点状态。**每个屏幕组内有且仅有一个焦点窗口**，不同屏幕组之间的焦点互不影响。

### 窗口焦点状态

**窗口焦点状态（Focus State）** 表示当前窗口是否能接收用户输入事件（如点击、按键等）。

* 主要状态如下所示：

  + WINDOW\_ACTIVE：窗口已获焦，可响应用户操作。
  + WINDOW\_INACTIVE：窗口失焦，无法接收输入。
* 典型场景：应用启动后自动获焦；切换到其他应用时原窗口失焦。
* 可通过[on('windowEvent')](../harmonyos-references/arkts-apis-window-window.md#onwindowevent10)接口监听窗口焦点状态的变化。

### 窗口激活态管理

**窗口激活态（Highlight State）** 表示当前窗口是否处于“视觉高亮”状态，“视觉高亮”是一种UI反馈机制，通过改变窗口的外观（如标题栏颜色、边框样式、透明度、阴影等）来向用户传达：这个窗口当前是活跃的、可交互的，或者正在被系统强调。

* 窗口激活态支持应用窗口（包括主窗口和子窗口），不支持系统窗口。
* 窗口处于激活态不等于窗口获焦；但获焦窗口一定处于激活态。
* 具有独占激活和非独占激活两种模式。

  + 独占激活模式：仅一个窗口处于高亮，该应用的其他窗口自动失去高亮。
  + 非独占激活模式：应用内多个窗口（如父窗口和子窗口）同时高亮。
* 独占激活典型场景：多子窗应用中，仅当前操作的子窗标题栏处于高亮。
* 非独占激活典型场景：在专业设计工具中，用户同时操作主视图和参数设置面板，系统允许这两个窗口同时高亮，以表明它们都处于活跃交互状态。
* 可通过[on('windowHighlightChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowhighlightchange15)接口监听窗口激活态的变化。

## 焦点相关开发场景

| 功能 | 典型场景 | 对应接口 |
| --- | --- | --- |
| 监听窗口焦点变化 | 监听窗口焦点变化，以在窗口失焦时控制后台行为，如暂停动画、释放资源等。 | [on('windowEvent')](../harmonyos-references/arkts-apis-window-window.md#onwindowevent10) |
| 监听窗口激活态变化 | 监听窗口激活态变化，用于动态调整UI样式，如标题栏颜色、边框等。 | [on('windowHighlightChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowhighlightchange15) |
| 设置窗口是否可获焦 | 控制某个窗口是否参与焦点竞争。例如横幅消息通知，设置不可获焦，不打断用户输入法输入 | [setWindowFocusable()](../harmonyos-references/arkts-apis-window-window.md#setwindowfocusable9) |
| 在同应用内转移窗口焦点 | 进行应用内部多个窗口之间的焦点切换，确保流畅的焦点导航体验。例如，多窗口界面切换编辑窗口等。 | [shiftAppWindowFocus()](../harmonyos-references/arkts-apis-window-f.md#windowshiftappwindowfocus11) |
| 判断窗口是否获焦 | 进行窗口获焦状态的判断，可用于防止非活跃窗口执行敏感操作。 | [isFocused()](../harmonyos-references/arkts-apis-window-window.md#isfocused12) |
| 设置窗口是否独占激活 | 设置窗口为独占激活时，可用于聚焦窗口操作，提升用户注意力。  设置窗口为非独占激活时，可用于多标签页设计，支持多个窗口同时保持高亮。 | [setExclusivelyHighlighted()](../harmonyos-references/arkts-apis-window-window.md#setexclusivelyhighlighted15) |
| 查询窗口是否为激活态 | 判断当前窗口是否处于视觉高亮，可用于UI状态同步等场景。 | [isWindowHighlighted()](../harmonyos-references/arkts-apis-window-window.md#iswindowhighlighted18) |
| 显示当前窗口 | 可用于显示主窗口、子窗口、全局悬浮窗及系统窗口。  如果传入focusOnShow: false，窗口显示时不可获焦。 | [showWindow(options: ShowWindowOptions)](../harmonyos-references/arkts-apis-window-window.md#showwindow20) |

**说明** 

* 针对监听类接口：请使用对应的off()接口在页面销毁时移除相关监听，以避免内存泄漏。
* 页面加载优于显示：在调用showWindow()显示窗口等接口时，请确保已使用loadContent()或setUIContent等接口完成页面的加载。
* 合理使用窗口独占激活模式：避免滥用[setExclusivelyHighlighted()](../harmonyos-references/arkts-apis-window-window.md#setexclusivelyhighlighted15)导致用户体验割裂。
* 状态查询和监听接口的结合使用：首次进入页面可使用isWindowHighlighted()/isFocused()获取初始状态，再通过对应的on('windowHighlightChange')/on('windowEvent')接口监听后续变化以实现相关适配和操作。
