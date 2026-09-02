---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-487
title: 鸿蒙电脑拖拽悬浮窗至扩展显示器时，如何保证悬浮窗布局不出现异常
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 鸿蒙电脑拖拽悬浮窗至扩展显示器时，如何保证悬浮窗布局不出现异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:36897ec840b82f25778eb4c0d64aafea9708cce219e814593702e88f49338b2d
---

**问题原理**

vp与px转换公式：px = vp \* 显示设备逻辑像素的密度。

ArkTS页面组件的尺寸单位通常会使用vp，当拖拽悬浮窗至扩展显示器时，组件的实际显示大小px会因为显示设备逻辑像素密度的改变而变化，此时如果不同步调整窗口大小，会导致悬浮窗布局出现异常。

**解决措施**

使用[on('densityUpdate')](../harmonyos-references/arkts-apis-uicontext-uiobserver.md#ondensityupdate12)监听悬浮窗所处屏幕逻辑像素密度的变化，当其改变时，根据窗口原有vp，通过[resize](../harmonyos-references/arkts-apis-window-window.md#resize9)接口调整悬浮窗实际大小（px），确保悬浮窗布局不出现异常。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/uIVTlao0TL6uYmgeWQFVCw/zh-cn_image_0000002624635848.png "点击放大")
