---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-menu-overview
title: 菜单概述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 菜单 > 菜单概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:45+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:836c172405550c25228fb35bdd919763f1a23f8e58fd4636e84e7007bd48bcb1
---

菜单是一种用于给用户提供可执行的操作的弹窗，一般用于鼠标右键弹窗、点击弹窗等。

## 使用场景

| 接口 | 使用场景 |
| --- | --- |
| [菜单控制 (Menu)](arkts-popup-and-menu-components-menu.md) | 用于需要给指定的组件绑定用户可执行的操作时，例如长按图标展示操作选项等。 |
| [不依赖UI组件的全局菜单 (openMenu)](arkts-popup-and-menu-components-uicontext-menu.md) | 用于在无法直接访问UI组件的场景向用户提供可执行操作，例如在事件回调中展示操作选项等。 |

## 规格约束

* [bindMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindmenu11)通过调用isShow参数或[bindContextMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindcontextmenu12)调用isShown参数弹出时，需要等待页面全部构建完成才能展示。因此isShow或isShown不能在页面构建中设置为true，否则会导致menu弹窗显示位置及形状错误。
* openMenu的弹出需要传入有效的[TargetInfo](../harmonyos-references/arkts-apis-uicontext-i.md#targetinfo18)，否则无法弹出气泡。
* 其他规格约束，具体可参考[菜单控制](../harmonyos-references/ts-universal-attributes-menu.md)、[openMenu](../harmonyos-references/arkts-apis-uicontext-promptaction.md#openmenu18)说明。

## 生命周期

正常时序依次为：aboutToAppear>>onWillAppear>>onAppear>>onDidAppear>>aboutToDisappear>>onWillDisappear>>onDisappear>>onDidDisappear。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| aboutToAppear | () => void | 菜单显示动效前的事件回调。 |
| onAppear | () => void | 菜单弹出后的事件回调。 |
| aboutToDisappear | () => void | 菜单退出动效前的事件回调。 |
| onDisappear | () => void | 菜单消失后的事件回调。 |
| onWillAppear | [Callback<void>](../harmonyos-references/ts-types.md#callback12) | 菜单显示动效前的事件回调。  **说明：** aboutToAppear是初始化时触发调用，onWillAppear是在动画执行前触发调用，onWillAppear在aboutToAppear之后执行。 |
| onDidAppear | [Callback<void>](../harmonyos-references/ts-types.md#callback12) | 菜单弹出后的事件回调。  **说明：**  1. 快速点击按钮时，菜单会快速弹出、消失，此时onWillDisappear可能会在onDidAppear前生效。  2. 当菜单入场动效未完成时关闭菜单，该回调不会触发。  3. onAppear和onDidAppear触发时机相同，onDidAppear在onAppear后生效。 |
| onWillDisappear | [Callback<void>](../harmonyos-references/ts-types.md#callback12) | 菜单退出动效前的事件回调。  **说明：**  1. 快速点击按钮时，菜单会快速弹出、消失，此时onWillDisappear可能会在onDidAppear前生效。  2. aboutToDisappear和onWillDisappear触发时机相同，onWillDisappear在aboutToDisappear后生效。 |
| onDidDisappear | [Callback<void>](../harmonyos-references/ts-types.md#callback12) | 菜单消失后的事件回调。  **说明：** onDisappear和onDidDisappear触发时机相同，onDidDisappear在onDisappear后生效。 |
