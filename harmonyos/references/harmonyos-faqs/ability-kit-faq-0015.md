---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/ability-kit-faq-0015
title: Extension类进程崩溃是否会导致主进程崩溃
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 常见问题 > Extension类进程崩溃是否会导致主进程崩溃
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:47+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:1e00d2e6241e0906d0970ba2584338b61e8843f07a533576f6a91750aeec102c
---

**Q：Extension类进程崩溃是否会导致主进程崩溃？**

**A**：子进程的崩溃不会直接导致主进程崩溃。只有当子进程的崩溃导致主进程在使用部分功能时抛出了未被应用捕获的异常，才会间接导致主进程崩溃。
