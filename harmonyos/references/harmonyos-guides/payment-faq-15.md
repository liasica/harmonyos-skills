---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-15
title: 同一次支付请求接收到多次回调通知，怎么解决？
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > Payment Kit常见问题 > 同一次支付请求接收到多次回调通知，怎么解决？
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:621fabcc5825db97c41a884878b7908f3324e6a33774d7395275cc3cd082ccd0
---

1. 同一次支付请求接收到多次回调是开发者返回的响应报错，导致重试。请检查返回的响应格式是不是application/json以及响应的报文是不是 {"resultCode":"000000","resultDesc":"Success."} ，具体可参考[通知回调接口说明](../harmonyos-references/payment-rest-overview.md#通知回调接口说明)。
2. 自验证回调接口是否可正常接收响应，如Payment Kit服务器请求响应连接超时也会触发重试回调。
