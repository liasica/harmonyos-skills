---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-pay-and-sign
title: 支付并签约场景
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 免密支付接入 > 支付并签约场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:337d6fd347eb8e60d5f3589c2e6d97f7f77639b1e2583bb2ae369afdeee3a53f
---

## 场景介绍

从4.1.0(11)版本开始，新增支持支付并签约场景。

用户在商户APP应用/元服务选购完不同的商品确认订单后，跳转至用户支付并签约确认页面，用户完成支付并签约后，后续再次购买商品时，商户可以直接发起代扣，减少用户拉起收银台、输入支付密码等相关操作。

支持商户模型：直连商户、服务商

华为支付支付并签约页面展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/132lSIj3T5WxAas1d7-S4A/zh-cn_image_0000002552799438.png?HW-CC-KV=V1&HW-CC-Date=20260427T235007Z&HW-CC-Expire=86400&HW-CC-Sign=56A27818A6B7E82FD3D60C8E21AF4ADD7D0B414E6C8ED3CEF9CACE65D6BA1A07)

## 业务流程

开发者通过接入Payment Kit 提供的支付并签约能力，可以让用户在支付完成后快速与商户建立签约代扣的关系。具体接入流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/jRrZCBUsQLKwHMVHILagzw/zh-cn_image_0000002583439133.png?HW-CC-KV=V1&HW-CC-Date=20260427T235007Z&HW-CC-Expire=86400&HW-CC-Sign=791037A2161156B1965239D23368C639D3009E021211609500A3D191EEA117F6)

1. 商户客户端请求商户服务端创建商品订单。
2. 商户服务端调用Payment Kit服务端[直连商户预下单](../harmonyos-references/payment-pas-prepay.md)或[服务商预下单](../harmonyos-references/payment-partner-pas-prepay.md)接口。
3. Payment Kit服务端返回预支付ID（prepayId）给商户服务端。
4. 商户服务端组建订单信息参数[orderStr](../harmonyos-references/payment-model.md#orderstr)返回给商户客户端。
5. 商户客户端使用orderStr调用[requestPayment](../harmonyos-references/payment-paymentservice.md#paymentservicerequestpayment)接口拉起Payment Kit支付收银台。
6. Payment Kit客户端展示支付收银台。
7. 用户通过收银台完成支付并签约。
8. Payment Kit服务端处理支付并同步返回支付受理成功结果给Payment Kit客户端。
9. Payment Kit异步处理支付完成并回调支付结果给商户服务端（支付失败场景不会有支付结果回调通知）。商户服务端需要使用[SM2验签方式](../harmonyos-references/payment-rest-overview.md#验签规则)对支付结果进行验签。
10. Payment Kit服务端处理签约并同步返回签约受理成功结果给Payment Kit客户端。
11. Payment Kit服务端异步处理签约完成后回调签约结果给商户服务端（取消签约和签约失败场景不会有回调结果通知）。商户服务端需要使用[SM2验签方式](../harmonyos-references/payment-rest-overview.md#验签规则)对签约结果进行验签。
12. Payment Kit客户端展示结果页。
13. 用户关闭结果页后Payment Kit客户端会返回支付状态给商户客户端。
14. 商户客户端进行后续处理操作。

## 接口说明

接口返回值有两种返回形式：Promise和AsyncCallback。Promise和AsyncCallback只是返回方式不一样，功能相同。具体API说明详见[接口文档](../harmonyos-references/payment-paymentservice.md)。

| 接口名 | 描述 |
| --- | --- |
| requestPayment(context:common.UIAbilityContext, orderStr: string): Promise<void>; | 拉起Payment Kit支付收银台。 |
| requestPayment(context:common.UIAbilityContext, orderStr: string, callback: AsyncCallback<void>): void; | 拉起Payment Kit支付收银台。 |

## 开发步骤

### 预下单（服务器开发）

1. 按照商户模型调用[直连商户预下单](../harmonyos-references/payment-pas-prepay.md)或[服务商预下单](../harmonyos-references/payment-partner-pas-prepay.md)接口获取预支付ID（prepayId）。

   为保证支付订单的安全性和可靠性需要对请求body和请求头PayMercAuth对象内的入参排序拼接进行签名，可参考[签名规则](../harmonyos-references/payment-rest-overview.md#签名规则)。
2. 构建订单信息参数[orderStr](../harmonyos-references/payment-model.md#orderstr)返回给客户端，业务接口请求示例代码可参考[业务接口请求](payment-server-connect.md#业务接口请求)。

### 拉起华为支付收银台（端侧开发）

使用[orderStr](../harmonyos-references/payment-model.md#orderstr)调用[requestPayment](../harmonyos-references/payment-paymentservice.md#paymentservicerequestpayment)接口拉起Payment Kit支付收银台。

支付并签约拉起支付收银台与商户基础支付场景处理逻辑一致，可参见[这里](payment-payment-process.md#拉起华为支付收银台端侧开发)。

### 支付并签约结果处理（服务器开发）

商户在构建[直连商户预下单](../harmonyos-references/payment-pas-prepay.md)或[服务商预下单](../harmonyos-references/payment-partner-pas-prepay.md)请求参数时，传入一个callbackUrl。在完成支付并签约后，华为支付服务器将以POST方式调用callbackUrl，将支付并签约的结果返回给商户服务器。

说明

* 如果用户没有提前登录，系统会自动拉起华为账号登录页面让用户登录。
* 支付并签约接口请求成功不代表支付或签约成功，建议不要以客户端签约收银台返回作为用户支付并签约的最终结果，需以服务器接收到的结果通知或者查询API返回为准。

为保证信息合法性，商户服务器需要对返回的支付信息进行[SM2验签](../harmonyos-references/payment-rest-overview.md#验签规则)，验签注意事项：

1. 需直接使用通知的完整内容进行验签。
2. 验签前需要对返回数据进行排序拼接，sign字段是签名值，排序拼接后的待验签内容需要排除sign字段。
3. 验签公钥使用[华为支付证书](payment-certificates-config.md#华为支付证书)。

## 延伸和拓展

当开发者完成上述支付并签约接入操作之后还可以调用以下API接口完成订单相关操作。

### 直连商户

[查询支付订单](../harmonyos-references/payment-pas-merc-query-order.md)、[申请退款](../harmonyos-references/payment-pas--refund.md)、[查询退款订单](../harmonyos-references/payment-pas-merc-query-refund.md)、[查询签约订单](../harmonyos-references/payment-withhold-query-contractcode.md)、[申请解约](../harmonyos-references/payment-pas-withhold-unsign.md)、[查询对账单](../harmonyos-references/payment-query-trade-bill.md)、[查询结算账单](../harmonyos-references/payment-query-settle-bill.md)。

### 服务商

[查询支付订单](../harmonyos-references/payment-partner-pas-merc-query-order.md)、[申请退款](../harmonyos-references/payment-partner-pas-refund.md)、[查询退款订单](../harmonyos-references/payment-partner-pas-merc-query-refund.md)、[查询签约订单](../harmonyos-references/payment-partner-withhold-query-contractcode.md)、[申请解约](../harmonyos-references/payment-partner-pas-unsign.md)、[查询对账单](../harmonyos-references/payment-partner-agent-query-trade-bill.md)、[查询结算账单](../harmonyos-references/payment-partner-agent-query-settle-bill.md)。
