---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-1
title: 接入开发时，请求参数的签名、结果验签在什么场景使用？
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > Payment Kit常见问题 > 接入开发时，请求参数的签名、结果验签在什么场景使用？
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5e9b0e2cb9fac15d019dca3d5e8d0271c730db7d65f780f680bbcc66eb4a9cc2
---

1. 签名：商户服务器请求Payment Kit开放API时必须签名后再发起请求。
2. 验签：商户服务器请求Payment Kit服务器收到响应后或接收到回调通知请求时需要使用华为支付平台公钥验签。详细场景介绍参见[签名规则](../harmonyos-references/payment-rest-overview.md#签名规则)和[验签规则](../harmonyos-references/payment-rest-overview.md#验签规则)。
