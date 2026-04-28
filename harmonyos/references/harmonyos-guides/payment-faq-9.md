---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-9
title: 关于支付回调的验签，为什么预下单请求验签的时候使用SHA256，回调验签却使用SM2？只能使用SM2进行验签吗？
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > Payment Kit常见问题 > 关于支付回调的验签，为什么预下单请求验签的时候使用SHA256，回调验签却使用SM2？只能使用SM2进行验签吗？
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:99335a4577e32c50b450460daaaf35a5028d85966e04801960d60f573fbe09a5
---

1. 商户预下单请求加签，华为支付提供了SHA256WithRSA/PSS和SM2两种签名方式，由商户自行选择使用哪一种签名方式进行签名。
2. 对于支付业务，应监管要求，需要支持国密算法。回调通知华为支付统一使用SM2进行加签，所以目前只能使用SM2进行回调验签，无法由商户选择。
