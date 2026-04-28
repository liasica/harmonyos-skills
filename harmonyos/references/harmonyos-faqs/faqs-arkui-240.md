---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-240
title: 创建subwindow默认是否铺满全屏，铺满全屏时如何隐藏状态栏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 创建subwindow默认是否铺满全屏，铺满全屏时如何隐藏状态栏
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:01+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:31b491321bd717de0d948ca0bfa42f5c7521e3e230c064507fa09e0a075a9e52
---

子窗口默认不铺满全屏。要设置窗口全屏模式时状态栏的可见模式，需调用setWindowSystemBarEnable方法，此方法必须由主窗口调用。

**参考链接**

[setWindowSystemBarEnable](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarenable9)
