---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1589
title: 云调试环境下无法监听折叠屏屏幕状态的改变
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 云调试环境下无法监听折叠屏屏幕状态的改变
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:98d6749f12b5d0d37c45e44b9894a0cb537e7af80bf17d56f0aa7c64beefa274
---

## 问题现象

在云调试环境下，使用display.on('foldStatusChange')方法无法监听折叠屏屏幕状态的变化。

## 背景知识

* [@ohos.display (屏幕属性)](../harmonyos-references/js-apis-display.md)提供管理显示设备的能力，包含获取屏幕的显示状态，监听设备的拔插行为等。
* [云调试](../AppGallery-connect-Guides/agc-clouddebug-introduction-0000001057034023.md)致力于为开发者提供高效的云端设备调试解决方案，解决开发者设备机型不足、设备管理困难及bug无法复现等问题，降低开发者的采购及管理成本。

## 解决方案

云调试中切换折叠状态的改变为虚拟变化，而[foldStatusChange](../harmonyos-references/js-apis-display.md#displayonfoldstatuschange10)是用于监听设备物理折叠状态的变化，从而导致无法正确地进行监听，可以使用[foldDisplayModeChange](../harmonyos-references/js-apis-display.md#displayonfolddisplaymodechange10)监听，该接口为监听设备屏幕显示模式的变化，可监听当前显示内容是显示在折叠设备的内屏还是外屏。

## 常见FAQ

Q：折叠屏模拟器怎么控制展开折叠？

A：折叠屏模拟器右侧工具栏可以控制折叠屏的展开折叠状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/uBNz2yZ1QNKrkyFxYFD-Hg/zh-cn_image_0000002658969527.png "点击放大")

Q：foldStatusChange和foldDisplayModeChange的区别？

A：foldStatusChange是用来监听物理设备折叠的状态，foldDisplayModeChange是监听折叠屏的屏幕显示模式。时序上物理折叠状态变化在前，底层会根据物理折叠状态匹配屏幕显示模式状态。
