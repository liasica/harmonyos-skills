---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-purax-9
title: 应用在Pura X上打开时，组件存在遮挡
breadcrumb: FAQ > 多设备场景 > 手机 > Pura X常见问题 > 应用在Pura X上打开时，组件存在遮挡
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5fb17e4cb121dcdaadac85e5097ba0af33f03dbf46ed087c5dc6ea7005b92f16
---

## 问题现象

应用在Pura X阔折叠的内屏打开时，页面文字等组件布局重叠，导致部分内容无法看清。

## 背景知识

* [Pura X阔折叠](../best-practices/bpta-purax-guide.md)：Pura X配有一块16:10比例的矮胖内屏（展开态），较其他机型断点有所区别，横向断点sm，宽度范围320-600vp；纵向断点lg，高宽比大于1.2。
* [Text](../harmonyos-references/ts-basic-components-text.md)：用于一段文本的显示。可以通过设置fontSize和lineHeight等属性，调整文本的样式。

## 问题定位

1. 检查代码中是否使用getWindowWidthBreakpoint()与getWindowHeightBreakpoint()获取当前窗口断点，并存储在AppStorage中。
2. 检查代码中是否使用on('windowSizeChange')开启窗口尺寸变化的监听，并在监听的回调中重新获取断点，动态更新页面组件尺寸，布局。

## 分析结论

应用未使用getWindowWidthBreakpoint()与getWindowHeightBreakpoint()获取当前设备的断点，并根据不同断点进行组件的动态改变，导致在特殊机型Pura X内屏上显示时发生了重叠的现象。

## 修改建议

* 阔折叠与其他折叠屏屏幕尺寸差异较大，页面布局是不同的，如果使用display.isFoldable()等折叠机设备硬件相关接口做UX布局判断条件，将无法区分Pura X内屏与大折叠（或其他折叠设备）展开态。若以此为依据，使用相同的布局，可能导致页面留白、重叠等显示异常。
* 因此推荐采用响应式断点布局方案，确保在不同尺寸下都能提供完整的UI展示，具体可参考[官方示例](../best-practices/bpta-multi-device-responsive-layout.md#section1532120147301)。
