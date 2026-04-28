---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-combined-merc-query-order
title: 通过combinedMercOrderNo查询订单信息
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 平台类商户/服务商 > 合单支付（仅支持平台类商户） > 查询合单支付订单 > 通过combinedMercOrderNo查询订单信息
category: harmonyos-references
scraped_at: 2026-04-28T08:18:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c3747b4b9cec6a722f6d16612df94223032c3081e202c8c456bf06c9f2a60dd0
---

## 功能介绍

开发者可以调用此接口查询已经在华为支付创建成功的合单支付订单详细信息。

说明

resultCode返回“000000”表示查询支付订单成功，不代表支付订单成功，订单状态需根据orderStatus字段判断。

## 场景描述

用户已完成合单支付，开发者调此接口获取合单支付订单信息。

## 接口原型

* **承载协议：** HTTPS GET
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** https://petalpay-developer.cloud.huawei.com.cn/api/v2/partner/combined/transactions/merc-orders/{combinedMercOrderNo}
* **数据格式：**

  请求消息：Content-Type: application/json

  响应消息：Content-Type: application/json

## 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |
| PayMercAuth | 是 | String | 取值为：[PayMercAuth](payment-model.md#paymercauth)的JSON字符串 |

**request path**

| 参数 | 是否必填 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| combinedMercOrderNo | 是 | String | 商户合单支付主单订单号。 |

## 请求示例

```
1. GET /api/v2/partner/combined/transactions/merc-orders/{combinedMercOrderNo} HTTP/1.1
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
| resultCode | 是 | String | 结果码，"000000"表示成功，其他表示失败。 |
| resultDesc | 是 | String | 结果描述。 |
| subCode | 否 | String | 业务错误码。 |
| subDesc | 否 | String | 业务错误描述信息。 |
| sign | 是 | String | 签名值。用于开发者对响应报文进行防篡改验证。 |
| combinedSysTransOrderNo | 否 | String | 华为支付合单支付交易订单号。 |
| combinedMercOrderNo | 否 | String | 商户生成的合单支付主订单号。 |
| combinedAppId | 否 | String | 商户申请并关联的应用id。 |
| orderStatus | 是 | String | 订单状态。  - TRX\_SUCCESS：交易成功  - TRX\_FAILED：交易失败  - TRX\_APPLY：交易处理中  - TRX\_PROC：交易处理中 |
| payload | 否 | String | 合单商户下单时传入的预留字段，原样返回。 |
| subOrders | 否 | [SubOrderResult](payment-model.md#suborderresult) | 合单支付子订单信息。 |
| payer | 否 | [PayerOut](payment-model.md#payerout) | 用户支付时客户端信息。 |

## 响应示例

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "000000",
5. "resultDesc": "Success.",
6. "sign": "MEYCIQDOsSJ5gL9mcYKi9usz4I/u********************77jclylTWJOTThPxOdJs+2zsDv3sg38UY/Wy",
7. "combinedSysTransOrderNo": "12407030857530004914518***",
8. "payload": "example-payload",
9. "combinedMercOrderNo": "czl00120240705***",
10. "orderStatus": "TRX_SUCCESS",
11. "subOrders": [
12. {
13. "sysTransOrderNo": "12407030857530004914518***",
14. "mercOrderNo": "czl00120240705***",
15. "orderStatus": "TRX_SUCCESS",
16. "payload": "example-payload",
17. "currency": "CNY",
18. "totalAmount": 40,
19. "payerAmount": 1,
20. "paymentTools": "AGMT"
21. }
22. ]
23. }
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
