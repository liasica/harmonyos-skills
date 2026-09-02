---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-30
title: 悬浮窗模式下，应用窗口放置在屏幕不同位置时，内部弹窗位置也随着变化
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 悬浮窗模式下，应用窗口放置在屏幕不同位置时，内部弹窗位置也随着变化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8d79a70d7c2f78d820b5762a88d7e526af1dca1fffd37ce90b5ab9d1388d4f4b
---

## 问题现象

应用切换到平板悬浮窗模式下时，拖动应用窗口在平板窗口上的位置后，点击按钮弹出弹窗，弹窗位置也随之改变。

## 背景知识

* [position](../harmonyos-references/ts-universal-attributes-location.md#position)：定位，确定子组件相对父组件内容区的位置。父组件内容区的大小为父组件大小减去border、padding、safeAreaPadding提供给子组件可布局的内容区域大小。
* [offset](../harmonyos-references/ts-universal-attributes-location.md#offset)：相对偏移，组件相对原本的布局位置进行偏移。
* [ClickEvent](../harmonyos-references/ts-universal-events-click.md#clickevent)：点击事件的回调函数。其中windowX参数表示点击位置相对于应用窗口左上角的X坐标；displayX参数表示点击位置相对于应用屏幕左上角的X坐标。

## 问题定位

1. 检查代码中是否使用position或者offset对弹窗组件进行位置偏移设置。
2. 检查偏移量设置值是否使用了点击事件中相对于应用屏幕左上角的X坐标displayX，使用该值进行组件偏移时，会导致在悬浮窗模式下displayX值一直在变化，从而出现弹窗位置也一直变化的现象。

## 分析结论

应用对弹窗组件使用了offset设置了相对偏移，设置值是通过click事件回调函数中获取到的相对于应用屏幕左上角的X坐标displayX。应用切换到悬浮窗模式后，在设备屏幕上移动后displayX的值也随之变化，导致应用内弹窗位置一直变化。

## 修改建议

使用click点击事件的回调中的相对于应用窗口左上角的X坐标windowX作为弹窗显示的偏移量。
