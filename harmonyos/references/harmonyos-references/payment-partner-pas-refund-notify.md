---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-pas-refund-notify
title: 退款结果回调通知
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 平台类商户/服务商 > 支付并签约 > 退款结果回调通知
category: harmonyos-references
scraped_at: 2026-04-28T08:18:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b8e15fbdd700533989c9bcd2dfeb4aff6073aa4afdeeb3e8e64c86e79d397667
---

## 功能介绍

开发者完成退款申请成功后，华为支付服务器调用此接口向开发者的服务器发送退款关键事件通知。

说明

1. 为保证回调请求的可靠性，系统具备重试机制，可能会出现重发的通知。
2. 为保证信息合法性，开发者需要对返回的支付信息进行[SM2验签](payment-rest-overview.md#验签规则)，验签注意事项：

   * 需直接使用通知的完整内容进行验签。
   * 验签前需要对返回数据进行排序拼接，sign字段是签名值，排序拼接后的待验签内容需要排除sign字段。
   * 验签公钥使用[华为支付证书](../harmonyos-guides/payment-certificates-config.md#华为支付证书)。
3. 退款状态需根据refundOrderStatus字段判断。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** URL由开发者在请求申请退款接口时传递的callbackUrl参数决定
* **数据格式：**

  请求消息：Content-Type: application/json

  响应消息：Content-Type: application/json

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
| mercRefundNo | 是 | String | 商户退款订单号。 |
| sysRefundNo | 是 | String | 华为支付退款订单号。 |
| refundAmount | 是 | Long | 退款总金额。订单需要退款的金额，该金额不能大于订单金额，单位：分。  **说明：** 如果正向交易使用了营销，该退款金额包含营销金额，华为支付会按业务规则分配营销和买家自有资金分别退多少，默认按比例退款。如不填则默认payerRefundAmount。 |
| payerRefundAmount | 是 | Long | 退款给用户的金额，单位：分。 |
| promotionRefundAmount | 是 | Long | 营销退款金额，单位：分。 |
| currency | 是 | String | 交易币种单位，最大长度为3。  CNY （默认，当前仅支持该币种单位） |
| mercNo | 否 | String | 商户号。 |
| finishTime | 否 | String | 退款完成时间，UTC时间格式（yyyy-MM-dd'T'HH:mm:ss.SSSZ）。 |
| refundOrderStatus | 是 | String | 退款订单状态。  - REFUND\_SUCCESS：成功  - REFUND\_FAILED：失败 |
| payload | 否 | String | 预留信息，如商户请求时传递该参数，此时会原样返回。 |

## 请求示例

```
1. POST /hw/pay/callback HTTP/1.1
2. Content-Type: application/json;charset=UTF-8
3. {
4. "callbackId": "124070308575300049145189***",
5. "callbackTime": "2023-03-29 09:52:37",
6. "currency": "CNY",
7. "dataType": "plain",
8. "finishTime": "2023-02-23T10:05:17.000+0800",
9. "mercNo": "10132120***",
10. "mercRefundNo": "czl00120240705***",
11. "payerRefundAmount": 100,
12. "payload": "example-payload",
13. "promotionRefundAmount": 10,
14. "refundAmount": 100,
15. "refundOrderStatus": "REFUND_SUCCESS",
16. "sign": "MEYCIQD8RlHJ9tGmc2tass32B********************cZpBY1ffr21wgjQ2l",
17. "signType": "SM2",
18. "certNo": "120291744647139***",
19. "sysRefundNo": "1230223100511858780002***"
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
