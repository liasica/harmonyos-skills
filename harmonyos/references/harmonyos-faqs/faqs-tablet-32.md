---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-32
title: 平板设备上，应用页面横屏状态下不显示内容
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 平板设备上，应用页面横屏状态下不显示内容
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e35b4c74b8a35cbe6da3b9d63022f88c4a89ab9885186bb0226201cea0857320
---

## 问题现象

在平板横屏模式下打开应用，首页中选择内容播放，平板横屏时播放界面显示白屏，切换为竖屏才显示具体内容。

## 背景知识

* [Orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)：窗口显示方向类型枚举。
* [visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)：控制组件的显示或隐藏。当未设置visibility时，组件默认为显示。

## 问题定位

1. 应用启动后，从日志发现有setVisibility相关日志，在平板横屏时日志打印setVisibility：false，在竖屏时日志打印setVisibility：true。

   ```shell
   10-11 11:37:33.721 I A00000 /com.xxx.xx: setVisibility true
   10-11 11:37:33.721 I A00000 /com.xxx.xx: setVisibility false
   ```
2. 建议检查代码中详情页组件的visibility属性显示与隐藏设置是否合理，当窗口显示横屏时，设置组件Visibility.None，页面会隐藏并且不参与布局，不进行占位，就会导致一片空白的现象。

## 分析结论

应用在切换Orientation窗口显示方向为LANDSCAPE横屏时，设置了整体页面父组件显示模式为Visibility.None，将整体页面隐藏了，导致横屏不显示内容，竖屏才显示。

## 修改建议

正确设置横竖屏状态下，页面组件的显示模式，调整为Visibility.Visible正常显示。具体示例可见[visibility示例](../harmonyos-references/ts-universal-attributes-visibility.md#示例)。
