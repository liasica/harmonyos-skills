---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-sandbox-test
title: 沙盒环境验证
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 沙盒环境验证
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:35+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:d1dd22175d1d576d36a3bf96efd4c906a2a55d7844a30480009b40f44be4c5c1
---

华为支付提供沙盒环境，开发者无需真实完成商户入网即可开始调试华为支付接入，模拟真实环境下华为支付交易过程，提前介入方案设计和开发联调，提升接入效率。

说明

* 沙盒环境当前仅支持部分能力及接口调试，具体可参见[沙盒环境接口请求及支持维度说明](payment-sandbox-test.md#沙盒环境接口请求及支持维度说明)。
* 使用沙盒环境验证支付场景，支付成功不会产生真实扣款。
* 当前沙盒环境创建的订单与真实环境订单暂无明确的沙盒验证相关标识，开发者应自行将沙盒验证订单与真实订单做区分（如在商户订单号中添加沙盒标识、预下单通过payload字段添加标识等）。
* 沙盒环境支付订单暂不支持分账，生成、查询及下载账单数据。

## 沙盒环境调试配置

### 获取沙盒环境配置

在沙盒验证前，需要生成沙盒环境配置信息（如商户号、证书ID、用户账号、支付密码等）进行调试，生成沙盒环境配置暂不支持开发者生成，请联系华为工程师获取，相关咨询可[点击此处](payment-service-support.md)或者通过[在线工单系统](https://developer.huawei.com/consumer/cn/support/feedback/#/add/13?level2=111)与我们联系。

生成沙盒环境配置信息需提供如下信息：

| 配置项 | 是否必选 | 说明 |
| --- | --- | --- |
| 商户模式  (mercNo) | 是 | 沙盒验证使用的商户模式。  - DIRECT：直连（普通）  - AGENT：服务商  - PLAT\_AGENT：平台商户 |
| 应用ID  (appId) | 是 | 应用的AppID（在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站点击“开发与服务”，在项目列表中找到项目，在“项目设置 > 常规”页面的“应用”区域获取“APP ID”的值）。  生成的沙盒验证配置需要与开发者应用关联。 |
| 华为账号  (hwAccount) | 是 | 开发者华为账号。用于生成测试用账号及支付密码等测试信息。 |
| 邮箱地址 | 是 | 开发者邮箱地址。用于后续配置或其他信息邮件答复。 |
| 业务说明 | 是 | 应用业务简介（可附应用页面截图）。 |

### 构建debug签名应用

说明

开发者应用为debug模式，应用相关测试场景才能正常进入沙盒环境。

构建debug签名应用步骤如下：

1. 参见[手动签名方式调试HarmonyOS应用/元服务](../app/agc-help-cert-0000002270829389.md)，申请应用调试证书->注册调试设备->申请调试Profile。
2. 参见[配置签名信息](ide-signing.md#section1240072619462)，在DevEco Studio侧配置签名信息。
3. 在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中[配置应用签名证书指纹](../app/agc-help-cert-fingerprint-0000002278002933.md)。

## 沙盒环境接口请求及支持维度说明

REST API请求说明：

1. 沙盒环境调试开放API接口请使用以下站点：https://petalpay-developer-sandbox.cloud.huawei.com.cn
2. 沙盒环境REST API 接口请求与真实环境请求方式一致，仅使用的配置不同（参见[沙盒环境调试配置](payment-sandbox-test.md#沙盒环境调试配置)），API接口调用请参见REST API[公共说明](../harmonyos-references/payment-rest-overview.md)以及对应的API接口说明。

沙盒调试支持调试的能力维度如下：

| 操作层面 | 能力维度描述 |
| --- | --- |
| 用户 | **用户登录**：支持用户在支付过程中使用华为账号进行登录操作。  **银行卡支付**：支持用户在华为支付收银台选择银行卡支付（测试配置默认绑定测试银行卡，暂不支持用户主动绑卡）。  **余额支付**：支持用户在华为支付收银台选择余额支付（预置余额，暂不支持充值，支付后不会产生扣费）。  **密码支付**：支持用户在华为支付收银台通过输入密码完成支付（不支持修改用户支付密码）。 |
| 商户（开发者） | **拉起支付收银台：** 支持商户应用/元服务通过预下单接口获取预支付ID（prepayId）构建[orderStr](../harmonyos-references/payment-model.md#orderstr)参数调用[requestPayment](../harmonyos-references/payment-paymentservice.md#requestpayment)接口拉起华为支付收银台。  **调用REST API接口查询订单、退款等操作：**  - **直连商户：**  - [预下单](../harmonyos-references/payment-prepay.md)：商户可以通过本接口提交华为支付订单信息，同时获取华为支付预交易订单号。  - [支付结果回调通知](../harmonyos-references/payment-pay-notify.md)：用户支付完成后，华为支付服务器通过开发者请求预下单接口时入参传递的回调通知URL（callbackUrl）向开发者的服务器发送支付关键事件通知。  - [查询支付订单](../harmonyos-references/payment-merc-query-order.md)：商户可以通过本接口查询某笔交易订单状态。  - [申请退款](../harmonyos-references/payment-service--refund.md)：商户可以调用此接口将订单金额退还给用户。  - [退款结果通知](../harmonyos-references/payment-refund-notify.md)：用户支付完成后，华为支付服务器通过开发者请求申请退款接口时入参传递的回调通知URL（callbackUrl）向开发者的服务器发送支付关键事件通知。  - [查询退款订单](../harmonyos-references/payment-merc-query-refund.md)：商户调用退款申请成功后，商户可以调用此接口查询退款订单状态。  - **平台类商户/服务商：**  - [预下单](../harmonyos-references/payment-agent-prepay.md)：平台类商户/服务商可通过本接口提交华为支付订单信息，同时获取华为支付预交易订单号。  - [支付结果回调通知](../harmonyos-references/payment-agent-pay-notify.md)：用户支付完成后，华为支付服务器通过开发者请求预下单接口时入参传递的回调通知URL（callbackUrl）向开发者的服务器发送支付关键事件通知。  - [查询支付订单](../harmonyos-references/payment-agent-merc-query-order.md)：平台类商户/服务商可通过本接口查询某笔交易订单状态。  - [申请退款](../harmonyos-references/payment-agent-refund.md)：平台类商户/服务商可调用此接口将订单金额退还给用户。  - [退款结果通知](../harmonyos-references/payment-agent-refund-notify.md)：用户支付完成后，华为支付服务器通过开发者请求申请退款接口时入参传递的回调通知URL（callbackUrl）向开发者的服务器发送支付关键事件通知。  - [查询退款订单](../harmonyos-references/payment-agent-merc-query-refund.md)：调用退款申请成功后，平台类商户/服务商可调用此接口查询退款订单状态。 |

## 验证商户基础支付场景

**支持商户模型：** 直连商户、平台类商户、服务商

1. 在满足沙盒验证条件（已获取[沙盒环境调试配置](payment-sandbox-test.md#沙盒环境调试配置)）下，开发者可以使用沙盒环境配置调用[直连商户预下单](../harmonyos-references/payment-prepay.md)/[平台类商户/服务商预下单](../harmonyos-references/payment-agent-prepay.md)获取预支付ID（prepayId）构建[orderStr](../harmonyos-references/payment-model.md#orderstr)请求[requestPayment](../harmonyos-references/payment-paymentservice.md#requestpayment)接口拉起Payment Kit支付收银台（开发步骤可参见[商户基础支付场景](payment-payment-process.md#开发步骤)）。

   说明

   * 沙盒环境下的支付流程与正式环境的支付流程一致，相关配置信息（如mercNo、authId等）需要替换为沙盒环境的站点及配置。
   * 使用沙盒环境时，构建的[orderStr](../harmonyos-references/payment-model.md#orderstr)中需要传递沙盒环境标识sandbox\_flag。示例如下：

     ```
     1. {"app_id":"101831***","merc_no":"101610000***","prepay_id":"12507011723580897591704***","timestamp":"1751361838042","noncestr":"6f18060eee669126b98e474407cc0682","sign":"OeS+xINxcEoClk+WlsLdnZqL0aIJ5qV734StxULDIgnwz8********************qURxBMzdT2NqdwNefGfrcB5kWVic0RuLz8wqrUPoQBrcl83VVzw59jmgrupitpHMD9sHDpja92H4AMP2SBOdFR2a58qexJves26iTO2f2hsSKFSUEUlHYEW/bgZmVv83GOTo4wIaIbN94gBjkou0kBInTqP2Ht0R9gzVCdB0pYLK+PM4nCY72TkeglyuYHjzD6GlqKMO3UZmuUoqYi8=","auth_id":"101610000031***","reserved":"{\"sandbox_flag\": true}"}
     ```
   * 如果用户没有提前登录，系统会拉起华为账号登录页面让用户登录，请使用沙盒环境用户账户进行登录。
2. 用户按照正常流程完成支付（实际不会产生真实扣费）后，开发者可以收到回调通知，需要完成回调事件处理。开发者也可以主动请求订单查询、申请退款等接口，以完成订单查询、退款等整个支付流程的闭环。

   沙盒环境拉起支付收银台完成订单支付与正常环境支付流程体验一致，页面示例参见[商户基础支付场景](payment-payment-process.md#场景介绍)所示。
