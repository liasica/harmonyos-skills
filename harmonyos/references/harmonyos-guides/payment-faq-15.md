---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-15
title: 同一次支付请求接收到多次回调通知，怎么解决？
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > Payment Kit常见问题 > 同一次支付请求接收到多次回调通知，怎么解决？
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:30+08:00
doc_updated_at: 2026-05-19
content_hash: sha256:ae9e3c4217115ad10f05b2377cd2b15eda1c02e4c207173af038cb67443a0550
---

* 当开发者返回的响应格式不符合要求（如请求响应格式不是application/json、响应的报文不是 {"resultCode":"000000","resultDesc":"Success."}等），具体可参考[通知回调接口说明](../harmonyos-references/payment-rest-overview.md#通知回调接口说明)。
* 检查自验证回调接口是否可正常接收响应，如Payment Kit服务器请求响应连接超时也会触发重试回调。
