---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-34
title: 多个UIAbility是运行在一个进程还是多个进程中？三方应用是否支持应用运行在多个进程下？主进程结束了，会影响子进程的运行吗
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 多个UIAbility是运行在一个进程还是多个进程中？三方应用是否支持应用运行在多个进程下？主进程结束了，会影响子进程的运行吗
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:43+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f1bf41d83e91cff043682bf43bea55816a7ad1bce13e30bc312e449b0deb1e95
---

**PC/2in1设备**

* 不同模块的UIAbility运行在不同的进程中。
* 多个进程相互独立，其他进程的退出不会影响当前进程。

**其他设备**

* 多个UIAbility运行在同一个进程中。
* 三方应用的UIAbility不支持多进程运行，而Extension则运行在独立的进程中。
* 手机设备上的UIAbility均运行在单个进程中，不包含子进程。

**参考链接**

[进程模型](../harmonyos-guides/process-model-stage.md)
