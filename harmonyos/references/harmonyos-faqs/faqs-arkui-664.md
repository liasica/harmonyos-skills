---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-664
title: 跳转页面后未避让状态栏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 跳转页面后未避让状态栏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:baaef1a6b2f40d56e9d1286982b8e9d4188c0ea6309d25aff82b8ad87ef40788
---

## 问题现象

多次跳转页面后，页面未避让状态栏，部分内容被状态栏遮挡，影响使用体验。

## 背景知识

* [getWindowAvoidArea](../harmonyos-references/js-apis-arkui-uiextension.md#getwindowavoidarea)：获取当前应用窗口内容规避的区域。如系统栏区域、刘海屏区域、手势区域、软键盘区域等与窗口内容重叠时，需要窗口内容避让的区域。
* [setWindowLayoutFullScreen](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)：设置主窗口或子窗口的布局是否为沉浸式布局。沉浸式布局生效时，布局不避让状态栏与三键导航栏，组件可能产生与其重叠的情况。非沉浸式布局生效时，布局避让状态栏与三键导航栏，组件不会与其重叠。
* [expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)：控制组件扩展其安全区域。

## 问题定位

* 排查应用代码中statusBarHeight关键字，在进入新页面后是否重新获取并更新statusBarHeight值。
* 排查应用代码中setWindowLayoutFullScreen关键字，检查是否只使用setWindowLayoutFullScreen(true)设置了沉浸式布局，没有动态重置避让区域。
* 排查expandSafeArea关键字，查看页面是否使用了expandSafeArea属性，如果使用了，按以下步骤排查。
  1. 排查页面是否开启剪切模式，部分容器组件（如Tabs、Swiper）默认开启剪切模式（clip(true)）。clip(true)会强制裁剪超出父容器的子组件内容，导致expandSafeArea无法扩展至安全区域。
  2. 排查Navigation页是否设置了margin/padding，如果设置了margin/padding属性,导致边界和安全区域无法重合，则expandSafeArea失效。
  3. 排查设置expandSafeArea的组件是否设置了固定宽高尺寸，如height(100)，这会覆盖安全区扩展逻辑，造成expandSafeArea失效。

## 分析结论

* 未在onPageShow生命周期中注册getWindowAvoidArea更新规避区域，导致页面切换时状态栏高度未重新获取。
* 使用setWindowLayoutFullScreen(true)全局开启沉浸式布局后，但没有在跳转后的二级、三级页面动态重置避让区域，会导致页面内容未避让状态栏。
* 页面设置的expandSafeArea失效，造成多次跳转页面后未避让状态栏。

## 修改建议

参考[开发应用沉浸式效果](../harmonyos-guides/arkts-develop-apply-immersive-effects.md)及[沉浸式页面实现](../best-practices/bpta-multi-device-window-immersive.md)，主要注意以下几点：

* 使用[Window.getWindowAvoidArea()](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)方法获取避让区域的高度，据此设置应用页面内容的上下padding实现避让状态栏和导航栏。
* 使用[getWindowAvoidArea()](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)接口获取当前布局遮挡区域。
* 在Ability中注册[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)全局系统区域变化监听，动态获取避让区域的实时数据。
* 确保设置的expandSafeArea属性生效，扩展安全区域。
  1. 设置了expandSafeArea属性的组件需关闭[clip](../harmonyos-references/ts-universal-attributes-sharp-clipping.md#clip12)剪切模式。
  2. 设置expandSafeArea属性的组件需与安全区域边界重合，动态调整margin/padding，使组件与安全区域边界重合。
  3. 设置expandSafeArea属性的组件不建议固定宽高尺寸，建议使用百分比或padding改变组件宽高。
