---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-payment-2
title: 华为支付服务元服务支付鉴权报错
breadcrumb: FAQ > 应用服务开发 > 鸿蒙支付服务（Payment Kit） > 华为支付服务元服务支付鉴权报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:615fd78cafcf6825560159aed45b61ce9dbcf5cde8c7a4d1a62ae1ea2c306355
---

## 问题现象

元服务接入华为支付服务，进行支付鉴权时出现报错，响应HTTP状态码:200，响应内容:{"resultCode":"200002","resultDesc":"签名错误","subCode":"INVALID\_SIGNATURE","subDesc":"无效签名"}，如何解决？

## 解决方案

该报错一般是由于开发者订单信息中的sign用的是预下单返回的sign，而orderStr.sign需要重新加签后才能使用。具体可参考[orderStr](../harmonyos-references/payment-model.md#orderstr)和[签名规则](../harmonyos-references/payment-rest-overview.md#签名规则)。
