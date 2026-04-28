---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-6
title: 支付成功后没有收到回调？
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > Payment Kit常见问题 > 支付成功后没有收到回调？
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8a01b9307e4f72edf9d334aa56e9308965c4784d25a4fb5e62e52a7a170532ac
---

* 检查预下单传入的callbackUrl接口地址是否有效。
* 检查服务器是否有允许清单等网络限制。
* 加密套件不一致，目前华为支付支持的加密套件如下：

```
1. TLS_DHE_RSA_WITH_AES_128_GCM_SHA256
2. TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
3. TLS_DHE_DSS_WITH_AES_128_GCM_SHA256
4. TLS_DHE_DSS_WITH_AES_256_GCM_SHA384
5. TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
6. TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
7. TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
8. TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
9. TLS_AES_128_GCM_SHA256
```
