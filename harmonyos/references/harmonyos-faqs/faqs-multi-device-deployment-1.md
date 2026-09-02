---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-multi-device-deployment-1
title: 应用未适配自由多窗，在平板设备上出现截断、挤压、堆叠等现象
breadcrumb: FAQ > 多设备场景 > 一次开发多端部署 > 常见问题 > 应用未适配自由多窗，在平板设备上出现截断、挤压、堆叠等现象
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:cf0829d9d15174df6464376cd751d45ceba7515b935afe2196e69bc80caada36
---

## 问题现象

在平板或PC等大屏设备上，在开启自由多窗的情况下，打开应用后，出现页面截断、图片挤压、组件堆叠等现象。

## 背景知识

* [module.json5](../harmonyos-guides/module-configuration-file.md)的[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)中supportWindowMode标识当前UIAbility组件所支持的窗口模式。
* [on('windowStatusChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowstatuschange11)方法可和[on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)方法实现对窗口是否进入悬浮窗模式及尺寸大小变化的监听。

## 问题定位

可以通过检查代码是否监听windowStatusChange事件或是否监听windowSizeChange事件，并且动态调整布局，来判断应用是否适配自由多窗模式。

## 分析结论

未适配自由多窗模式：未监听windowStatusChange事件或未监听windowSizeChange事件，并且动态调整布局。

## 修改建议

监听屏幕尺寸变化，并同步动态修改页面组件的布局及尺寸。

1. 开启窗口模式变化的监听，通过on('windowStatusChange')方法，根据窗口windowStatus发生变化时返回值对应为[WindowStatusType](../harmonyos-references/arkts-apis-window-e.md#windowstatustype11)来判断当前界面状态，WindowStatusType=4为悬浮窗模式。
2. 通过getWindowProperties方法返回值中的windowRect获取窗口尺寸，存入AppStorage。使用on('windowSizeChange')方法来监听窗口尺寸的变化。
3. UI侧通过@StorageLink绑定窗口尺寸后，AppStorage中属性key值对应的数据一旦改变，UI侧会同步修改。通过@StorageLink装饰的数据在窗口尺寸发生变化时会引起组件的重新渲染，可以根据最新的窗口尺寸动态调整应用布局。

具体详细示例可参考[应用布局适配智慧多窗的方案](../harmonyos-guides/multi-window-layout-adapt.md#应用布局适配智慧多窗的方案)。
