---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-faq-4
title: 游戏资源加速ExtensionAbility方法中使用static静态变量为什么不生效？
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏资源加速服务 > 游戏资源加速ExtensionAbility方法中使用static静态变量为什么不生效？
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:46+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0b33c25d80fac446358428096e66227eb453ff242bc2411344c95be311157113
---

资源加速ExtensionAbility的进程可能会切换，避免在ExtensionAbility方法使用应用自身的上下文变量，例如类成员变量、全局static静态变量。

若想在资源加速ExtensionAbility方法中共享变量，应使用[数据持久化技术](app-data-persistence-overview.md)，在不同方法中共享变量。
