---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-3
title: GET请求的bodySign是对谁签名得到的？
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > Payment Kit常见问题 > GET请求的bodySign是对谁签名得到的？
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:14+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:08f65a9df62de8cad3858c6806c2ef987677b21174b8e96d55701df1e5434424
---

GET请求需要对path url进行签名，例如[查询支付订单](../harmonyos-references/payment-sys-query-order.md)的待签名内容是：“/api/v2/aggr/transactions/orders/{sysTransOrderNo}”。
