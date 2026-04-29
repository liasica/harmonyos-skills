---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-487
title: 鸿蒙电脑拖拽悬浮窗至扩展显示器时，如何保证悬浮窗布局不出现异常
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 鸿蒙电脑拖拽悬浮窗至扩展显示器时，如何保证悬浮窗布局不出现异常
category: harmonyos-faqs
scraped_at: 2026-04-29T14:18:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:eceb9f3c787cd74363510c1b2f33eda54de0409917e8a9d7904ad972da3747b5
---

**问题原理**

vp与px转换公式：px = vp \* 显示设备逻辑像素的密度。

ArkTS页面组件的尺寸单位通常会使用vp，当拖拽悬浮窗至扩展显示器时，组件的实际显示大小px会因为显示设备逻辑像素密度的改变而变化，此时如果不同步调整窗口大小，会导致悬浮窗布局出现异常。

**解决措施**

使用[on('densityUpdate')](../harmonyos-references/arkts-apis-uicontext-uiobserver.md#ondensityupdate12)监听悬浮窗所处屏幕逻辑像素密度的变化，当其改变时，根据窗口原有vp，通过[resize](../harmonyos-references/arkts-apis-window-window.md#resize9)接口调整悬浮窗实际大小（px），确保悬浮窗布局不出现异常。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/HyoDlvGBTsuZlsyItvumnw/zh-cn_image_0000002533911659.png?HW-CC-KV=V1&HW-CC-Date=20260429T061805Z&HW-CC-Expire=86400&HW-CC-Sign=4C2CC768A7A463BB94D2283D28F6B0E19CB797E8C2DC1C1D2E1153D7FC621265 "点击放大")
