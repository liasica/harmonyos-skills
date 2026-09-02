---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-computer-4
title: 应用在PC设备上页面文字显示过大或过小
breadcrumb: FAQ > 多设备场景 > 电脑 > 常见问题 > 应用在PC设备上页面文字显示过大或过小
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:2beec92ff43c57beb7a83c372fb8936d2212dbe92d83d9bb1dc8774e5f159a60
---

## 问题现象

在PC设备上打开应用，应用界面显示的文字过大或过小。

## 背景知识

1. 数值相同情况下，使用不同像素单位时，文字显示大小也会不一致。详细参考：[组件支持的参数类型及参数单位类型](faqs-arkui-45.md)。
2. 响应式布局：通常使用窗口监听（[如何监听窗口大小的变化](faqs-arkui-1040.md)）配合[断点](../best-practices/bpta-multi-device-responsive-layout.md#section1532120147301)动态调整字体与布局。

## 问题定位

1. 当窗口变化时若未对组件进行相应的动态适配可能造成字体显示异常。检查是否使用响应式布局，如动态监听窗口变化，使用百分比布局或字体相对单位。
2. 字体大小单位设置不一致也会导致字体显示异常，检查是否混合使用fp和px单位。

## 分析结论

1. 未动态适配窗口变化。
2. 字体单位不一致。

## 修改建议

1. 避免混用绝对单位(px)与相对单位(fp/vp)。
2. 窗口监听配合断点实现动态调整字体大小，参考[横向断点的使用案例](../best-practices/bpta-multi-device-responsive-layout.md#section565041813314)。
