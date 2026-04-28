---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-32
title: Extension类进程崩溃是否会导致主进程崩溃
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > Extension类进程崩溃是否会导致主进程崩溃
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:43+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:44183943c4c7e4f214e6946f92d553e032fa86e903ec0b7d5a05803a408691f0
---

子进程的崩溃不会直接导致主进程崩溃。只有当子进程的崩溃导致主进程在使用部分功能时抛出了未被应用捕获的异常，才会间接导致主进程崩溃。
