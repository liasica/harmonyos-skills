---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-107
title: A持有B，B引用A的场景会不会导致内存泄漏
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > A持有B，B引用A的场景会不会导致内存泄漏
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:12+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a5b14cdfc0d4b0faa77b43f1e1e641c6051775dc2fee3f4a78e04663cf98ecba
---

方舟虚拟机的内存管理和GC使用根可达算法，该算法能解决循环引用问题，避免A引用B、B引用A的内存泄漏。
