---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-combined-notify
title: 合单支付结果回调通知
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 平台类商户/服务商 > 合单支付（仅支持平台类商户） > 合单支付结果回调通知
category: harmonyos-references
scraped_at: 2026-04-28T08:18:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ec563a80484c072727c255b33234c8d29f0afded436bb93b792977caf6f120b5
---

## 功能介绍

用户支付完成后，华为支付服务器调用此接口向商户服务器发送支付关键事件通知。

说明

1. 为保证回调请求的可靠性，系统具备重试机制，所以可能出现重发的通知。
2. 订单状态需根据orderStatus字段判断。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** URL由开发者在请求预下单接口时传递的callbackUrl
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
| combinedMercNo | 否 | String | 商户号。 |
| combinedAppId | 否 | String | 商户申请并关联的应用id。 |
| combinedSysTransOrderNo | 是 | String | 华为支付合单支付主订单号。 |
| combinedMercOrderNo | 是 | String | 商户合单支付主订单号。由商户生成。 |
| orderStatus | 否 | String | 订单状态：  - TRX\_SUCCESS：交易成功  - TRX\_FAILED：交易失败 |
| payload | 是 | String | 预留信息，如商户请求时传递该参数，此时会原样返回。 |
| subOrders | 是 | List<[SubOrderResult](payment-model.md#suborderresult)> | 子单交易结果详情。 |
| payer | 否 | [PayerOut](payment-model.md#payerout) | 用户支付时客户端信息。 |

## 请求示例

```
1. POST /hw/pay/callback HTTP/1.1
2. Content-Type: application/json;charset=UTF-8
3. {
4. "callbackId": "124070308575300049145189***",
5. "callbackTime": "2023-08-29 10:29:14",
6. "dataType": "plain",
7. "resultCode": "000000",
8. "resultDesc": "Success.",
9. "sign": "MEYCIQDOsSJ5gL9mcYKi9usz4********************hAOd2P+Gu77jclylTWJOTThPxOdJs+2zsDv3sg38UY/Wy",
10. "signType": "SM2",
11. "combinedSysTransOrderNo": "123112802273686342***",
12. "payload": "example-payload",
13. "combinedMercOrderNo": "czl00120240705***",
14. "orderStatus": "TRX_SUCCESS",
15. "subOrders": [
16. {
17. "sysTransOrderNo": "1231171178343***",
18. "mercOrderNo": "czl00120240705***",
19. "orderStatus": "TRX_SUCCESS",
20. "payload": "example-payload",
21. "currency": "CNY",
22. "totalAmount": 40,
23. "payerAmount": 1,
24. "paymentTools": "AGMT"
25. }
26. ]
27. }
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
