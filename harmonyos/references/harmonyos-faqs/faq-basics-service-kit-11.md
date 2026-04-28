---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-11
title: 如何获取系统时间，并且在切换时区时，时间戳一直保持北京时间
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 如何获取系统时间，并且在切换时区时，时间戳一直保持北京时间
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:adbbd0c6bfc64933468b49a1e93237c515c06e62fc9ba58e4eb8c5054377a679
---

使用[systemDateTime.getTime()](../harmonyos-references/js-apis-date-time.md#systemdatetimegettime10)可以获取自Unix纪元以来经过的时间。getTime获取的是Unix时间戳，Unix时间戳和时区无关，在任何时区返回的值都是一致的。
