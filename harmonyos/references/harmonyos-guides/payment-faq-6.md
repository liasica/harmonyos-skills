---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-6
title: 支付成功后没有收到回调？
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > Payment Kit常见问题 > 支付成功后没有收到回调？
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:724a71e465ef8084ce0e3f8e253da649eb87c361e592311e4338c10267aee28f
---

* 检查预下单传入的callbackUrl接口地址是否有效。
* 检查服务器是否有允许清单等网络限制。
* 加密套件不一致，目前华为支付支持的加密套件如下：

```html
TLS_DHE_RSA_WITH_AES_128_GCM_SHA256
TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
TLS_DHE_DSS_WITH_AES_128_GCM_SHA256
TLS_DHE_DSS_WITH_AES_256_GCM_SHA384
TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
TLS_AES_128_GCM_SHA256
```
