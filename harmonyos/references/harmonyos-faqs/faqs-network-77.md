---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-77
title: 为什么在设置自定义DNS后，HTTP请求还是会走本地DNS缓存
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 为什么在设置自定义DNS后，HTTP请求还是会走本地DNS缓存
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d8f94c4ab878afa8c481951284bebc2f3a3e9ccd7ddb20a7a2f7f1d0171d5f2a
---

HTTP请求存在连接复用，而连接复用基于域名匹配，如果已经有指向相同域名的连接可以复用，那么请求会直接复用已有连接，导致自定义规则不生效。
