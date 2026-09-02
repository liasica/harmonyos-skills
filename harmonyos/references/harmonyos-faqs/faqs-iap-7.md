---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-iap-7
title: 订阅退订之后获取到的商家订单号不是最新的
breadcrumb: FAQ > 应用服务开发 > 应用内支付服务（IAP Kit） > 订阅退订之后获取到的商家订单号不是最新的
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8fba4fe0bf6ca9873294a1bf8e528adf696dfbec1f17d6f538ae37a7bbca80ca
---

## 问题现象

沙箱环境，订阅→退订→订阅→退订流程（在该流程中，获取到的是首次订阅的商家订单号），且已经完成扣款，为什么最后一次退订获取到的商家订单号不是最新的？

## 解决方案

订阅后取消订阅然后再订阅，属于恢复订阅，

如：恢复订阅时未到扣款期，此时获取的订单号是第一次的；

如：恢复订阅时已到期且完成扣款，获取的订单号才会是新的。

该问题与扣款状态无关，关键在于订阅商品的生效期是否已超过。若重新订阅时未超过一个月的生效期，则保留首次订单号；若已超过，则生成新的订单号。
