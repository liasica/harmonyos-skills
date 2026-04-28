---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-faq-1
title: 通过加载内存镜像启动的游戏会全屏显示来电提醒，应该如何避免？
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏启动加速服务 > 通过加载内存镜像启动的游戏会全屏显示来电提醒，应该如何避免？
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:48+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:688fe31cd0dbe02ebedaed2b778a46adfea35582c77373aefb1ac9d8af3b4946
---

没有通过加载内存镜像启动的游戏，用户在游戏期间来电，来电提醒悬浮在手机正上方。

通过加载内存镜像启动的游戏，用户在游戏期间来电，游戏画面会被切至后台，当前来电提醒会被全屏显示，这影响了用户的游戏体验。

开发者应在onWindowStageCreate生命周期中调用[setWindowSystemBarEnable](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarenable9)，隐藏状态栏和导航栏，确保快速启动的游戏在来电提醒时悬浮在手机正上方。
