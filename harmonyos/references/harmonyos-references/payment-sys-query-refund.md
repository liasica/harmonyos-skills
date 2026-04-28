---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-sys-query-refund
title: 通过sysRefundOrderNo查询退款订单信息
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 直连商户 > 基础支付 > 查询退款订单 > 通过sysRefundOrderNo查询退款订单信息
category: harmonyos-references
scraped_at: 2026-04-28T08:17:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:44076090094784bda1915845538c45e40d80b1a42b15a71a434ccee4ba1c5965
---

## 功能介绍

开发者可以调用该接口查询某笔退款订单详细信息。

说明

resultCode返回“000000”表示查询退款订单成功，不代表退款成功，退款状态需根据refundOrderStatus字段判断。

退款订单状态：

* REFUND\_CHL\_PROC：处理中
* REFUND\_SUCCESS：成功
* REFUND\_FAILED：失败

## 场景描述

该接口支持所有的华为支付退款订单查询，若开发者已有申请退款的订单，可以通过该接口查看具体退款订单的退款状态。

## 接口原型

* **承载协议：** HTTPS GET
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** https://petalpay-developer.cloud.huawei.com.cn/api/v1/aggr/transactions/refunds/orders/{sysRefundOrderNo}
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
| sysRefundOrderNo | 是 | String | 华为支付退款订单号。 |

## 请求示例

```
1. GET /api/v1/aggr/transactions/refunds/orders/{sysRefundOrderNo} HTTP/1.1
2. Content-Type: application/json;charset=UTF-8
3. PayMercAuth: {"callerId":"10132120***","traceId":"202305151501075707669","time":1684134067480,"authId":"120291744647139***","headerSign":"p9e6EvvWnVW/Q********************o6Run7iCj1mWYBYJIPB75/UrhP0aBflpW1J8Sf8VUt6orCWk=","bodySign":"haZnDZSsB/ed+BBnXhv5lPKR********************H8JJ+7uNwoEYO3lps="}
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
| sysRefundOrderNo | 否 | String | 华为支付退款订单号。 |
| mercRefundOrderNo | 否 | String | 商户退款订单号。 |
| refundOrderStatus | 是 | String | 退款订单状态：  - REFUND\_CHL\_PROC：处理中  - REFUND\_SUCCESS：成功  - REFUND\_FAILED：失败 |
| finishTime | 否 | String | 退款完成时间，UTC时间格式（yyyy-MM-dd'T'HH:mm:ss.SSSZ）。 |
| promotionRefundAmount | 否 | Long | 营销退款金额，单位：分。 |
| refundAmount | 否 | Long | 退款总金额。订单需要退款的金额，该金额不能大于订单金额，单位：分。  **说明：** 如果正向交易使用了营销，该退款金额包含营销金额，华为支付会按业务规则分配营销和买家自有资金分别退多少，默认按比例退款。如不填则默认全额退款。 |
| payerRefundAmount | 否 | Long | 退款给用户的金额，单位：分。 |
| currency | 否 | String | 交易币种单位，最大长度为3。  CNY （默认，当前仅支持该币种单位） |
| payload | 否 | String | 预留信息，如商户请求时传递该参数，此时会原样返回。 |

## 响应示例

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "000000",
5. "resultDesc": "Success.",
6. "sign": "MEUCIQCEA/HVCjAFReiy59wGUp0zQ********************IxmlIIv2zaKH3e6YfxkL94=",
7. "sysRefundOrderNo": "12407030900270084914518***",
8. "mercRefundOrderNo": "czl0012024070914***",
9. "refundOrderStatus": "REFUND_SUCCESS",
10. "finishTime": "2023-05-15T14:42:09.000+0800",
11. "promotionRefundAmount": 0,
12. "refundAmount": 2,
13. "payerRefundAmount": 2,
14. "currency": "CNY",
15. "payload": "example-payload"
16. }
```

## 错误码

**resultCode**非400000的错误码请查看[公共错误码说明](payment-error-code-rest.md#公共错误码说明)。

| 返回码 | 错误码 | **错误描述** | 解决方案 |
| --- | --- | --- | --- |
| 400000 | UNKNOW\_ERROR | 服务暂不可用，请稍后重试 | 稍后重试。 |
| 400000 | INVALID\_ARGUMENTS | 参数不合法 | 检查请求参数。 |
| 400000 | PAY\_ORDER\_NOT\_EXIST | 支付订单号不存在 | 检查入参订单号是否正确。 |
| 400000 | MERC\_ORDER\_NOT\_EXIST | 商户订单号不存在 | 检查入参订单号是否正确。 |
| 400000 | INVALID\_MERCNO | 无效商户号 | 检查入参商户号是否正确。 |
| 400000 | CHECK\_ORDER\_STATUS | 订单状态异常 | 请检查是否使用相同订单重复下单。 |
