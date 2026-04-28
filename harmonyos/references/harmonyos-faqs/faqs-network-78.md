---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-78
title: HTTP已有连接复用，如何使自定义DNS立即生效
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > HTTP已有连接复用，如何使自定义DNS立即生效
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:17+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:4e611fa2755d5985a058b92d988ca82c0106b21411bffbc0cc198166d4cd6404
---

本地DNS缓存默认超时时间为10分钟，对于HTTP1.1协议，可以通过发起一个超时时间为1ms的请求，当请求超时后会结束所复用的TCP流，再发起的请求将使用自定义DNS规则。
