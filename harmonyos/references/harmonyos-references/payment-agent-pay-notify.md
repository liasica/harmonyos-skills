---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-agent-pay-notify
title: 支付结果回调通知
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 平台类商户/服务商 > 基础支付 > 支付结果回调通知
category: harmonyos-references
scraped_at: 2026-04-28T08:17:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:71898249cadbdfc970c67b71c1eedec1aa0bd110a91f8969f81460917f3c6040
---

## 功能介绍

用户支付完成后，华为支付服务器调用此接口向开发者的服务器发送支付关键事件通知。

说明

1. 为保证回调请求的可靠性，系统具备重试机制，所以可能出现重发的通知。
2. 订单状态需根据orderStatus字段判断。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** URL由开发者在请求预下单接口时传递的callbackUrl
* **数据格式：**

  请求消息：Content-Type: application/json; charset=UTF-8

  响应消息：Content-Type: application/json; charset=UTF-8

## 请求参数

**Request Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| callbackId | 是 | String | 回调通知的唯一ID。 |
| callbackTime | 是 | String | 回调通知时间。格式为yyyy-MM-dd HH:mm:ss。 |
| dataType | 是 | String | 数据加密类型标识。  - encrypt：加密  - plain：未加密 |
| sign | 是 | String | 回调通知结果签名，除“sign”字段以外的其他字段参与签名。  开发者可参考[验签规则](payment-rest-overview.md#验签规则)对回调报文进行验签处理。 |
| signType | 是 | String | 签名类型。华为支付生成签名字符串使用的算法，当前为SM2算法。 |
| certNo | 否 | String | 签名所使用的证书编号。 |
| spMercNo | 否 | String | 合作伙伴父商户号。最大长度12。 |
| subMercNo | 否 | String | 合作伙伴子商户号。最大长度12。 |
| spAppId | 否 | String | 合作伙伴父商户关联的应用ID。 |
| sysTransOrderNo | 是 | String | 华为支付系统订单号。 |
| mercOrderNo | 是 | String | 商户订单号，由商户自己生成，商户需保证订单信息唯一性。最大长度46。 |
| orderStatus | 是 | String | 订单状态。  - TRX\_SUCCESS:交易成功  - TRX\_FAILED:交易失败 |
| payload | 否 | String | 预留信息，如商户请求时传递该参数，此时会原样返回。 |
| currency | 是 | String | 交易币种单位，最大长度为3。  CNY （默认，当前仅支持该币种单位） |
| totalAmount | 是 | Long | 订单总金额，单位：分。 |
| payerAmount | 是 | Long | 买家实付金额，单位：分。 |
| promotionAmount | 是 | Long | 优惠金额，单位：分。 |
| finishTime | 否 | String | 支付完成时间，UTC时间格式（yyyy-MM-dd'T'HH:mm:ss.SSSZ）。 |
| paymentTools | 否 | String | 支付工具。  - WECHAT\_MICROPAY：微信小程序支付  - AGMT：快捷  - ACCT：账户余额  - HUAWEIPAY：华为pay |
| promotionDetail | 否 | List<[PromotionItem](payment-model.md#promotionitem)> | 营销活动信息。 |
| payer | 否 | [PayerOut](payment-model.md#payerout) | 用户支付时客户端信息。 |

## 请求示例

```
1. POST /hw/pay/callback HTTP/1.1
2. Content-Type: application/json;charset=UTF-8
3. {
4. "callbackId": "124070308575300049145189***",
5. "callbackTime": "2023-03-29 09:29:14",
6. "currency": "CNY",
7. "dataType": "plain",
8. "finishTime": "2023-02-23T10:02:04.000+0800",
9. "mercOrderNo": "czl00120240705***",
10. "orderStatus": "TRX_SUCCESS",
11. "payerAmount": 10000,
12. "payload": "example-payload",
13. "paymentTools": "AGMT",
14. "promotionAmount": 0,
15. "sign": "MEYCIQDXutp78*******************VlWyjA6p210xOqI2InX9w2SIYRx",
16. "signType": "SM2",
17. "certNo": "120291744647139***",
18. "sysTransOrderNo": "12407030857530004914518***",
19. "totalAmount": 10000
20. }
```

## 响应参数

**Response Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |

**Response Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| resultCode | 是 | String | 响应码。华为支付侧解析application/json类型响应。 “000000”表示成功，其他值表示失败，如返回值格式不匹配或非“000000”将视为回调失败。 |
| resultDesc | 是 | String | 结果描述。 |

## 响应示例

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "000000",
5. "resultDesc": "Success."
6. }
```
