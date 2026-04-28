---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-ux-5032
title: UX样式或效果的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > OS平台行为变更说明 > HarmonyOS 5.0.3(15) Beta2引入的行为变更 > UX样式或效果的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:30+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:509446e7662bda81b1bb5ddbb6178336157d3a021d8a8873c00a64a3281802c9
---

## 动态照片自动播放效果变更

**变更原因**

动态照片自动播放时会放大至1.1倍；动态照片左右滑动自动播放时，闪烁和晃动效果明显。为改善用户界面使用体验，动态照片设置autoPlay自动播放时不放大。

**变更影响**

此变更无需应用适配。

@ohos.multimedia.medialibrary模块中的autoPlay接口ux默认行为规范变更。

变更前行为：动态照片设置autoPlay自动播放时放大至1.1倍。

变更后行为：动态照片设置autoPlay自动播放时不放大。

**起始API Level**

13

**变更的接口/组件**

@ohos.multimedia.medialibrary模块中的autoPlay接口。

**适配指导**

默认行为变更，无需适配。

## NavDestination标题栏工具栏支持跟手滑动隐藏后，超过2秒未操作，不恢复显示

**变更原因**

UX规范变更。

**变更影响**

此变更不涉及应用适配。

* 变更前：NavDestination组件的标题栏工具栏上滑隐藏，下滑显示，2s不操作后自动显示。
* 变更后：NavDestination组件的标题栏工具栏上滑隐藏，下滑显示，2s不操作后不会自动显示。

**起始API Level**

14

**变更的接口/组件**

NavDestination.bindToScrollable, NavDestination.bindToNestedScrollable

**适配指导**

默认行为变更，无需适配。

## Tabs组件TabBar的显示和隐藏动效变更

**变更原因**

UX规范变更。

**变更影响**

此变更不涉及应用适配。

* 变更前：Tabs组件的TabBar上滑隐藏，下滑消失，2s不操作后自动显示。
* 变更后：Tabs组件的TabBar上滑隐藏，下滑消失，2s不操作后不会自动显示。

**起始API Level**

13

**变更的接口/组件**

UIContext的bindTabsToScrollable、bindTabsToNestedScrollable接口

**适配指导**

默认行为变更，无需适配。
