---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-faq-20
title: subGroupId（订阅组ID）、subGroupGenerationId（订阅组的代ID）和subscriptionId（订阅ID）说明
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > IAP Kit常见问题 > subGroupId（订阅组ID）、subGroupGenerationId（订阅组的代ID）和subscriptionId（订阅ID）说明
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:45+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:a1ff5fc0c57683dcad66edb9f4b88a5733f29ad62a5b5326bd47c79fc46a0224
---

* subGroupId(订阅组ID)标识一个订阅组，一个订阅组下存在多个自动续期订阅商品。
* subGroupGenerationId(订阅组的代ID)是标识用户在同一订阅组下连续订阅的唯一ID。用户首次订阅时生成，在同一订阅组内切换其它订阅商品该ID不会改变，在订阅失效且超出[保留期](iap-subscription-functions.md#保留期)后，用户重新购买商品时改变。
* subscriptionId(订阅ID)标识用户对订阅组中的一个商品存在订阅关系。
