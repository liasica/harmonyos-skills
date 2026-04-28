---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-102
title: 如何实现Sendable类型和JSON数据的转换
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何实现Sendable类型和JSON数据的转换
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7674f274b4e9cfee8b3e37f971e47787164a9c00a81e7a8d3c9d23275e41c337
---

可以通过从API version 12开始支持的，ArkTS新增的[ArkTSUtils.ASON](../harmonyos-references/arkts-apis-arkts-utils-ason.md)工具实现。

ASON支持解析JSON字符串并生成共享数据，用于跨并发域传输。ASON还支持将共享数据转换为JSON字符串。
