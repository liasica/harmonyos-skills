---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-withhold-query-sys-order
title: 通过sysTransOrderNo查询订单信息
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 直连商户 > 签约代扣 > 查询代扣订单 > 通过sysTransOrderNo查询订单信息
category: harmonyos-references
scraped_at: 2026-04-28T08:17:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e198ec5f3a1dc81cc8e88e67d80a7e15e80cc70764d4f43ee3eda5b327a2601b
---

## 功能介绍

开发者可以调用此接口来查询所有通过华为支付方式支付且已成功创建交易订单的订单详细信息。

说明

resultCode返回“000000”表示查询支付订单成功，不代表支付订单成功，订单状态需根据orderStatus字段判断。

## 场景描述

在产生交易订单前提下，商户可以通过该接口查看某笔订单的支付状态，也可以通过主动查询交易订单状态用以完成下一步的业务逻辑，常见的使用场景：

* 支付时由于网络、服务器等异常未收到支付回调通知。
* 调用支付接口返回未知支付状态时。

## 接口原型

* **承载协议：** HTTPS GET
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** https://petalpay-developer.cloud.huawei.com.cn/api/v2/aggr/transactions/orders/{sysTransOrderNo}
* **数据格式：**

  请求消息：Content-Type: application/json; charset=UTF-8

  响应消息：Content-Type: application/json; charset=UTF-8

## 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |
| PayMercAuth | 是 | String | 取值为：[PayMercAuth](payment-model.md#paymercauth)的JSON字符串 |

**Request Path**

| 参数 | 是否必填 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| sysTransOrderNo | 是 | String | 华为支付系统订单号。  用户支付成功后通过支付结果回调通知返回给商户或通过mercOrderNo查询订单信息接口查询获取。 |

## 请求示例

```
1. GET /api/v2/aggr/transactions/orders/{sysTransOrderNo} HTTP/1.1
2. Content-Type: application/json;charset=UTF-8
3. PayMercAuth:
4. {"callerId":"10132120***","traceId":"202305151047588466083","time":1684118878350,"authId":"120291744647139***","headerSign":"OaLyLiENHhYxXwZ+XhKKiYnzWsX/HJf+02A60A42fjh********************znmsDJOALXgvh/RKeReQBbc4lXZp5wnyZmdwTesmPGdszSNP/s=","bodySign":"kf9AZmVjBSGUI2MldsIFShO+Ak00qpPKaXgJo+K********************7gdghaJShhzAsNjt8DE9ulUIlQ0Q95/dZt2jEHcXyLfGNVzDNfFPhvF08NnnGM4="}
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
| mercNo | 否 | String | 商户号。 |
| appId | 否 | String | 应用ID。获取方式请参见[AppID管理及关联](../pay-docs/hwzf-appidguanli-0000001757041165.md)。 |
| sysTransOrderNo | 否 | String | 华为支付系统订单号。 |
| mercOrderNo | 是 | String | 商户订单号，由商户自己生成，商户需保证订单信息唯一性。最大长度46。 |
| orderStatus | 是 | String | 订单状态。  - TRX\_SUCCESS：交易成功  - TRX\_FAILED：交易失败  - TRX\_APPLY：交易处理中  - TRX\_PROC：交易处理中 |
| payload | 否 | String | 预留信息，如商户请求时传递该参数，此时会原样返回。 |
| currency | 是 | String | 交易币种单位，最大长度为3。  CNY （默认，当前仅支持该币种单位） |
| totalAmount | 是 | Long | 订单总金额，单位：分。 |
| payerAmount | 否 | Long | 买家实付金额，单位：分。 |
| promotionAmount | 否 | Long | 优惠金额，单位：分。 |
| finishTime | 否 | String | 支付完成时间，UTC时间格式（yyyy-MM-dd'T'HH:mm:ss.SSSZ）。 |
| paymentTools | 否 | String | 支付工具。  - WECHAT\_MICROPAY：微信小程序支付  - AGMT：快捷  - ACCT：账户余额  - HUAWEIPAY：华为pay |
| promotionDetail | 否 | List<[PromotionItem](payment-model.md#promotionitem)> | 营销信息。  **说明：** 当用户支付时参与过营销活动，此字段才会返回。 |
| payer | 否 | [PayerOut](payment-model.md#payerout) | 用户支付时客户端信息。 |

## 响应示例

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "000000",
5. "resultDesc": "Success.",
6. "sign": "MEUCIQCO8t5lbWmI+94L1DCah********************2XmM05x1SmFAIrepM9Pg=",
7. "currency": "CNY",
8. "finishTime": "2023-02-23T10:02:04.000+0800",
9. "mercOrderNo": "czl00120240705***",
10. "appId": "5765880207853***",
11. "mercNo": "10132120***",
12. "orderStatus": "TRX_SUCCESS",
13. "payerAmount": 10000,
14. "payload": "example-payload",
15. "paymentTools": "AGMT",
16. "promotionAmount": 0,
17. "sysTransOrderNo": "12407030857530004914518***",
18. "totalAmount": 10000
19. }
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
