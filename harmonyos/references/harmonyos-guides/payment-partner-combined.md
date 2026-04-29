---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-partner-combined
title: 平台类商户合单支付场景
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 平台类商户合单支付场景
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:31+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:c367cbc7b782dcafd418b025cc9b9727e66f07d1713e76d565395c37ede6d6d9
---

## 场景介绍

从4.1.0(11)版本开始，新增支持平台类商户合单支付场景。

用户在商户开发的APP应用/元服务上购买了一个旅行套餐，包含机票、保险、酒店等这几个不同的产品对应不同的收单商户，但用户是一次支付。平台类商户通过接入合单支付将多个不同商户的订单合到同一订单下发起支付。

支持商户模型：平台类商户

华为支付收银台合单支付展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/UUHz-cefSqqNc-_QszBp0Q/zh-cn_image_0000002589245395.png?HW-CC-KV=V1&HW-CC-Date=20260429T053930Z&HW-CC-Expire=86400&HW-CC-Sign=004BFAADEEE86CB06FE861B213E362F14552971FB3B20CF4F390259B13F72B2F)

## 业务流程

开发者通过接入Payment Kit合单支付，可以将多个子订单合并到同一个主订单里完成支付。具体接入流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/3SvoqSHYRFiVnHnJyqOsRw/zh-cn_image_0000002558765588.png?HW-CC-KV=V1&HW-CC-Date=20260429T053930Z&HW-CC-Expire=86400&HW-CC-Sign=F6D34EB808ED75F551C973A0FCFF7477457174A9C1518B573E81DA21227CD1E7)

1. 商户客户端请求商户服务端创建合单支付订单。
2. 商户服务器通过调用Payment Kit服务端[平台类商户合单支付预下单](../harmonyos-references/payment-partner-combined-app-prepay.md)接口。
3. Payment Kit服务端返回预支付ID（prepayId）给商户服务端。
4. 商户服务端组建订单信息参数[orderStr](../harmonyos-references/payment-model.md#orderstr)返回给客户端。
5. 商户客户端使用orderStr作为入参调用[requestPayment](../harmonyos-references/payment-paymentservice.md#requestpayment)接口拉起Payment Kit支付收银台。
6. Payment Kit客户端展示支付收银台，通过支付收银台可查看多个订单详情信息。
7. 用户在Payment Kit客户端收银台完成支付操作后。
8. Payment Kit服务端受理支付，异步处理支付订单。
9. Payment Kit服务端同步返回支付结果信息给Payment Kit客户端。
10. Payment Kit客户端展示支付结果页。
11. 用户关闭支付结果页后Payment Kit客户端会返回支付状态给商户客户端。
12. Payment Kit服务端异步处理支付完成后，会调用商户预下单时通过callbackUrl传递的回调接口返回支付结果信息给商户服务器。
13. 商户服务器收到支付结果回调响应后，使用[SM2验签方式](../harmonyos-references/payment-rest-overview.md#验签规则)对支付结果进行验签。

## 接口说明

接口返回值有两种返回形式：Promise和AsyncCallback。Promise和AsyncCallback只是返回方式不一样，功能相同。具体API说明详见[接口文档](../harmonyos-references/payment-paymentservice.md)。

| 接口名 | 描述 |
| --- | --- |
| requestPayment(context:common.UIAbilityContext, orderStr: string): Promise<void>; | 拉起Payment Kit支付收银台。 |
| requestPayment(context:common.UIAbilityContext, orderStr: string, callback: AsyncCallback<void>): void; | 拉起Payment Kit支付收银台。 |

## 开发步骤

### 预下单（服务器开发）

1. 开发者按照商户模型调用[平台类商户合单支付预下单](../harmonyos-references/payment-partner-combined-app-prepay.md)接口获取预支付ID（prepayId）。

   为保证支付订单的安全性和可靠性需要对请求body和请求头PayMercAuth对象内的入参排序拼接进行签名，可参考[签名规则](../harmonyos-references/payment-rest-overview.md#签名规则)。
2. 构建合单订单信息参数[orderStr](../harmonyos-references/payment-model.md#orderstr)并返回给客户端。业务接口请求示例代码可参考[业务接口请求](payment-server-connect.md#业务接口请求)。

### 拉起华为支付收银台（端侧开发）

使用服务端返回的[orderStr](../harmonyos-references/payment-model.md#orderstr)调用[requestPayment](../harmonyos-references/payment-paymentservice.md#requestpayment)接口拉起Payment Kit支付收银台。合单支付拉起支付收银台与商户基础支付场景处理逻辑一致，可参见[这里](payment-payment-process.md#拉起华为支付收银台端侧开发)。

### 支付结果回调通知（服务器开发）

支付成功后华为支付服务器会调用开发者提供回调接口，将支付信息返回给开发者的服务器，回调详细信息按商户模式请参见[平台类商户合单支付结果回调通知](../harmonyos-references/payment-partner-combined-notify.md)。

为保证信息合法性，商户服务器需要对返回的支付信息进行[SM2验签](../harmonyos-references/payment-rest-overview.md#验签规则)，验签注意事项：

1. 需直接使用通知的完整内容进行验签。
2. 验签前需要对返回数据进行排序拼接，sign字段是签名值，排序拼接后的待验签内容需要排除sign字段。
3. 验签公钥使用[华为支付证书](payment-certificates-config.md#华为支付证书)。

## 延伸和拓展

当开发者完成上述能力之后，可以调用以下API接口完成订单其他相关操作。

### 平台类商户

[查询合单支付订单](../harmonyos-references/payment-partner-combined-merc-query-order.md)、[申请退款](../harmonyos-references/payment-partner-combined-refund.md)、[查询退款订单](../harmonyos-references/payment-partner-combined-merc-query-refund.md)、[查询对账单](../harmonyos-references/payment-partner-agent-query-trade-bill.md)、[查询结算账单](../harmonyos-references/payment-partner-agent-query-settle-bill.md)。
