---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-payment-4
title: 华为支付预下单接口报错提示无效的商户号
breadcrumb: FAQ > 应用服务开发 > 鸿蒙支付服务（Payment Kit） > 华为支付预下单接口报错提示无效的商户号
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:e7a4c418475ad62efe5830d664f9f283a3fc68baeec1b0bccbc31d566e1e7ea0
---

## 问题现象

接入华为支付服务，调用预下单接口返回“40000-INVALID\_MERCNO-无效的商户号”，如何解决？

## 解决方案

出现该问题通常是因为开发者的商户是平台类商户或者服务商商户，而在应用服务端预下单接口调用时是按照直连商户的方式去接入造成的，可以按照如下两个步骤进行排查：

1. 商户类型分为三种：直连商户、平台类商户和服务商商户：
   * 直连商户：直接与华为支付对接，使用华为支付服务的经营主体，直接向用户提供商品或服务。
   * 平台类商户：面向为商品交易或服务提供线上撮合与管理平台的商户，华为支付为其提供的支付与结算解决方案，平台接入华为支付后，平台上的商家（称为“子商户”）可入驻华为支付，然后提供商品或服务。
   * 服务商商户：作为华为支付与商户之间的连接桥梁，由其推荐入网的商户称为“特约商户”不可直接发起交易，需关联特约商户的商户号。

     商户类型在申请商户号时由开发者自行选择，开发者若不清楚商户类型可登录[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)，进入【账户中心】->【账户设置】->【商户主体信息】->【商户号设置】页面查看商户号信息。具体可看参考：[申请接入时如何选择合作身份](../pay-docs/hwzf-hezuoshenfen-0000001725918617.md)和[华为支付商户号信息查询](../pay-docs/hwzf-shanghuhao-0000001725982508.md)。

     商户类型确认后如何绑定具体可参考文档：[直连商户/平台类商户绑定](../harmonyos-guides/payment-binding-appid-to-merc.md#直连商户平台类商户绑定)和[服务商绑定](../harmonyos-guides/payment-binding-appid-to-merc.md#服务商绑定)。
2. 直连商户预下单调用时[请求参数](../harmonyos-references/payment-agent-prepay.md#请求参数)的Request Body传入是mercNo（商户号）参数即可。平台类商户或者服务商预下单调用时[请求参数](../harmonyos-references/payment-agent-prepay.md#请求参数)的Request Body传入的则是spMercNo（合作伙伴父商户号）和subMercNo（合作伙伴子商户号）。

   应用服务端预下单接口参考文档：[直连商户预下单](../harmonyos-references/payment-prepay.md)和[平台类商户/服务商预下单](../harmonyos-references/payment-agent-prepay.md)。
