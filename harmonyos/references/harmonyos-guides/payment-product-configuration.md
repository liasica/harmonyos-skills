---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-product-configuration
title: （可选）特定场景配置操作
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 开发准备 > （可选）特定场景配置操作
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f616a21aaf907be74d083fc56c07c3ae499a30755cb8f19782a96f302b0cca90
---

如涉及以下场景，需提前完成相关产品的开通或配置操作。如不涉及，请直接跳转[下一章节](payment-config-agc.md)。

## 场景一：产品开通操作

部分支付场景接入涉及产品开通，未开通产品直接接入，商户请求华为支付开放的API接口时可能会导致“商户未找到对应的产品示例”、“不支持的操作”等异常响应。开通产品需商户侧与华为支付侧沟通（合作咨询可[点击此处](payment-service-support.md)）后申请开通对应产品。

涉及产品开通的支付场景如下：

* [平台类商户合单支付场景](payment-partner-combined.md)
* [支付并签约场景](payment-pay-and-sign.md)
* [签约代扣场景](payment-withhold-process.md)
* [通用收银台支付相关场景](payment-common-pay-introduction.md)

涉及商户：直连商户、服务商、平台类商户

处理人：商户产品、商户BD等

## 场景二：涉及结算账单下载

如需要生成及下载账单，需商户在[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)入网时设置的管理员先在“[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/) > 商户中心 > 产品功能 > 功能设置”中开启“账单接口获取开关”，开启后**次日开始生成**前一日的账单。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/PqvNJ-Q2QvuutAZJT97eZQ/zh-cn_image_0000002558765576.png?HW-CC-KV=V1&HW-CC-Date=20260429T053929Z&HW-CC-Expire=86400&HW-CC-Sign=62474319D9937AC041BAD7D278E61B1199744877F71E37C46150A2B7615D5623)

涉及商户：直连商户、服务商、平台类商户

处理人：商户在[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)设置的超级管理员

## 场景三：服务商代特约商户发起退款

服务商商户模型接入，特约商户需要发起退款，涉及**服务商代特约商户发起退款**，需要服务商在[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)上[申请API退款授权](../pay-docs/hwzf-apituikuan-0000002371871965.md)完成特约商户退款授权操作。

涉及商户：服务商

处理人：商户在[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)设置的超级管理员

## 场景四：设置支付账户留存金额

商户交易款项会结算到卡，商户可[设置支付账户留存金额阈值](../pay-docs/hwzf-zhanghuyue-0000002344207501.md#section1946479152718)并充值留存一定的余额在支付账户，以此保证退款功能正常可用。

涉及商户：直连商户、服务商、平台类商户

处理人：商户在[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)设置的超级管理员

## 场景五：涉及账单分账

商户如需对订单进行分账操作，可通过[直连商户预下单](../harmonyos-references/payment-prepay.md)或[平台类商户/服务商预下单](../harmonyos-references/payment-agent-prepay.md)接口中allocationType字段实现，使用该字段前需商户侧与华为支付侧沟通（合作咨询可[点击此处](payment-service-support.md)）后申请开通并配置分账能力。

分账相关操作参见[分账交易管理](../pay-docs/hwzf-fenzhangjiaoyi-0000001723142294.md)。

涉及商户：直连商户、服务商、平台类商户

处理人：商户在[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)设置的超级管理员
