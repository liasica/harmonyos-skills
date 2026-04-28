---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-agent-merc-query-order
title: 通过mercOrderNo查询订单信息
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 平台类商户/服务商 > 基础支付 > 查询支付订单 > 通过mercOrderNo查询订单信息
category: harmonyos-references
scraped_at: 2026-04-28T08:17:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a5d50c5c6c170f54f880c73e860e2ae8c23111358426c885f1feebacdaad44fe
---

## 功能介绍

开发者可以调用此接口来查询所有通过华为支付方式支付且已成功创建交易订单的订单详细信息。

说明

resultCode返回“000000”表示查询支付订单成功，不代表支付订单成功，订单状态需根据orderStatus字段判断。

## 场景描述

该接口支持所有的华为支付系统交易订单的查询，若商户已完成Payment Kit单次支付能力的集成，并且有产生交易订单，可以通过该接口查看某笔订单的支付状态。开发者也可通过主动查询交易订单状态用以完成下一步的业务逻辑。

需要调用该接口的场景：

* 支付时由于网络、服务器等异常未收到支付回调通知。
* 调用支付接口返回未知支付状态时。

## 接口原型

* **承载协议：** HTTPS GET
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** https://petalpay-developer.cloud.huawei.com.cn/api/v2/partner/aggr/transactions/merc-orders/{mercOrderNo}
* **数据格式：**

  请求消息：Content-Type: application/json; charset=UTF-8

  响应消息：Content-Type: application/json; charset=UTF-8

## 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |
| PayMercAuth | 是 | String | 取值为：[PayMercAuth](payment-model.md#paymercauth)的JSON字符串 |

**request path**

| 参数 | 是否必填 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| mercOrderNo | 是 | String | 商户订单号，由商户自己生成，商户需保证订单号唯一性。最大长度46。 |

## 请求示例

```
1. GET /api/v2/partner/aggr/transactions/merc-orders/{mercOrderNo} HTTP/1.1
2. Content-Type: application/json;charset=UTF-8
3. PayMercAuth: {"callerId":"10132120***","traceId":"202305151047578634337","time":1684118877557,"authId":"120291744647139***","headerSign":"FB0vzUONHsvsurnKHZhc4*******************sZ3oJYeLt/4Da5n3DLXlSKYFmE=","bodySign":"DDRuPlG/QFb3OQTNHLIOaNFKnQ********************kvvni+9cVmsqHir0bRFLANqqh2zyzv4="}
```

## 响应参数

**Response Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |

**Response Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| resultCode | 是 | String | 结果码，“000000”表示成功，其他表示失败。 |
| resultDesc | 是 | String | 结果描述。 |
| subCode | 否 | String | 业务错误码。 |
| subDesc | 否 | String | 业务错误描述信息。 |
| sign | 是 | String | 签名值。用于开发者对响应报文进行防篡改验证。 |
| sysTransOrderNo | 否 | String | 华为支付系统订单号。 |
| mercOrderNo | 是 | String | 商户订单号，由商户自己生成，商户需保证订单号唯一性。最大长度46。 |
| orderStatus | 是 | String | 订单状态。  - TRX\_SUCCESS:交易成功  - TRX\_FAILED:交易失败  - TRX\_APPLY：交易处理中  - TRX\_PROC：交易处理中 |
| payload | 否 | String | 预留信息，如商户请求时传递该参数，此时会原样返回。 |
| currency | 是 | String | 交易币种单位，最大长度为3。  CNY （默认，当前仅支持该币种单位） |
| totalAmount | 是 | Long | 订单总金额，单位：分。 |
| payerAmount | 否 | Long | 买家实付金额，单位：分。 |
| promotionAmount | 否 | Long | 优惠金额，单位：分。 |
| finishTime | 否 | String | 支付完成时间，UTC时间格式（yyyy-MM-dd'T'HH:mm:ss.SSSZ）。 |
| paymentTools | 否 | String | 支付工具。  - WECHAT\_MICROPAY：微信小程序支付  - AGMT：快捷  - ACCT：账户余额  - HUAWEIPAY：华为pay |
| promotionDetail | 否 | List<[PromotionItem](payment-model.md#promotionitem)> | 营销信息，订单参与营销活动时才会返回。 |
| spMercNo | 否 | String | 合作伙伴父商户号。最大长度12。 |
| subMercNo | 否 | String | 合作伙伴子商户号。最大长度12。 |
| spAppId | 否 | String | 合作伙伴父商户关联的应用ID。 |
| subAppId | 否 | String | 合作伙伴子商户关联的应用ID。  **说明：** 平台子商户当前不支持绑定AppID，平台类商户请求传递该入参可能导致校验异常。 |
| payer | 否 | [PayerOut](payment-model.md#payerout) | 用户支付时客户端信息。 |

## 响应示例

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "000000",
5. "resultDesc": "Success.",
6. "sign": "MEQCIH5/3J3onT8qdEQhPZcI2eHH08eo********************eAOjIYtSAMtvDH1hRbA4MY861dug==",
7. "sysTransOrderNo": "12407030857530004914518***",
8. "mercOrderNo": "czl00120240705***",
9. "orderStatus": "TRX_SUCCESS",
10. "payload": "example-payload",
11. "currency": "CNY",
12. "totalAmount": 100000,
13. "payerAmount": 80000,
14. "promotionAmount": 20000,
15. "finishTime": "2023-11-28T10:09:01.276+0800",
16. "paymentTools": "AGMT"
17. }
```

## 错误码

**resultCode**非400000的错误码请查看[公共错误码说明](payment-error-code-rest.md#公共错误码说明)。

| **返回码** | **错误码** | **错误描述** | 解决方案 |
| --- | --- | --- | --- |
| 400000 | UNKNOW\_ERROR | 服务暂不可用，请稍后重试 | 稍后重试。 |
| 400000 | INVALID\_ARGUMENTS | 参数不合法 | 检查请求参数。 |
| 400000 | PAY\_ORDER\_NOT\_EXIST | 支付订单号不存在 | 检查入参订单号是否正确。 |
| 400000 | MERC\_ORDER\_NOT\_EXIST | 商户订单号不存在 | 检查入参订单号是否正确。 |
| 400000 | INVALID\_MERCNO | 无效商户号 | 检查入参商户号是否正确。 |
| 400000 | CHECK\_ORDER\_STATUS | 订单状态异常 | 请检查是否使用相同订单重复下单。 |
