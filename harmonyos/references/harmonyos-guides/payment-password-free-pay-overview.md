---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-password-free-pay-overview
title: 免密代扣说明
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 免密支付接入 > 免密代扣说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c45d33b20686f09a3db1fa0a70891e504391350ab7eec018d09b337a09cd0857
---

免密代扣包括支付并签约以及签约代扣场景。

开发者接入免密支付前需先申请开通签约代扣产品（即申请**配置免密代扣模板**和获取**协议模板ID**），产品开通参见[产品开通操作](payment-product-configuration.md#场景一产品开通操作)。

华为支付以模板维度管理每个代扣扣费服务，主要组成要素如下：

| 字段含义 | 开发者对接字段 | 说明 |
| --- | --- | --- |
| 协议模板ID | planId | 由华为支付分配的唯一模板ID，开发对接免密支付的必选参数之一。 |
| 商户签约协议号 | mercContractCode | 即商户签约标识。开发者请求签约时传入的签约协议号，商户侧生成，商户需保证唯一性。 |
| 委托代扣协议ID | contractId | 即华为签约标识。商户与用户签约成功后从华为支付签约回调通知中返回给商户或通过[直连商户查询签约信息](../harmonyos-references/payment-withhold-query-contractcode.md)或[服务商查询签约信息](../harmonyos-references/payment-partner-withhold-query-contractcode.md)接口查询获取。 |

接入免密支付时需注意以下事项：

1. 不允许多个应用共同使用同一个免密代扣模板，发布的商品必须和免密代扣模板是一对一的关系。
2. 同一用户在同一商户同一模板下的多次签约，需要使用新的商户签约协议号，生成的华为支付侧委托代扣协议ID不变,且与最新商户签约协议号关联。
3. 商户在多个应用中使用同一委托代扣协议ID发起免密代扣时，需要统一传递用户签约的应用ID。
