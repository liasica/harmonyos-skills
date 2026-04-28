---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-29
title: http请求结束后是否需要进行销毁
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > http请求结束后是否需要进行销毁
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b056b5ed80de3f2cd8016b0c4297796293258b32dd9e67cc655bb59036337bc0
---

http请求对象，在请求成功或者失败后，都需要调用destroy()接口进行销毁，以节省资源消耗。详细请参见[使用HTTP访问网络](../harmonyos-guides/http-request.md)。
