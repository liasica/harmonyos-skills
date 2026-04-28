---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-5
title: 如何主动退出当前应用
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何主动退出当前应用
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:40+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:76bfdde07c7c09dd779e55a2441b0729dc71e69218c88ed6861ec024ce473929
---

可以通过ApplicationContext的killAllProcesses()方法退出当前应用。

调用killAllProcesses()方法后，会逐个终止应用中的所有进程。
