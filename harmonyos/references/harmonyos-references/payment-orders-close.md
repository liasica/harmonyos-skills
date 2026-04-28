---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-orders-close
title: 关闭订单
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 直连商户 > 基础支付 > 关闭订单
category: harmonyos-references
scraped_at: 2026-04-28T08:17:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c05aa18305b88a41897f6d276ba6bef88b8961cbe92028e6c8c6faf0bc4d01e7
---

## 功能介绍

开发者可以调用该接口关闭已创建的订单。

## 场景描述

用户在开发者的应用中创建订单时，开发者服务器同步在华为支付创建订单完成。用户需要取消订单重新创建，开发者服务器在取消订单前可调用该接口关闭华为支付的订单，避免极端场景下用户重复支付。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** https://petalpay-developer.cloud.huawei.com.cn/api/v1/aggr/transactions/orders/close

  说明：元服务预下单接口请使用以下URL为https://petalpay-developer.cloud.huawei.com.cn/api/v1/aggr/transactions/orders/close
* **数据格式：**

  请求消息：Content-Type: application/json; charset=UTF-8

  响应消息：Content-Type: application/json; charset=UTF-8

## 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |
| PayMercAuth | 是 | String | 取值为：[PayMercAuth](payment-model.md#paymercauth)的JSON字符串 |

**Request Body**

| 参数 | 是否必选 | 类型 | 说明 |
| --- | --- | --- | --- |
| mercOrderNo | 是 | String | 商户订单号，由商户在预下单时生成，商户需保证订单信息唯一性。最大长度46。 |

## 请求示例

```
1. POST /api/v1/aggr/transactions/orders/close HTTP/1.1
2. Content-Type: application/json;charset=UTF-8
3. PayMercAuth: {"callerId":"10132120***","traceId":"202305151026422776499","time":1684117602555,"authId":"120291744647139***","headerSign":"u+H1Oe3fXV9mGCES89XA7tSjp8+********************lOG7eAFfwjEWJu5JyvY5KunSeE6DiKs=","bodySign":"yWDtXOBqDoItPgHmF57L6U5G7F/*******************asPj10iUIFeaszpiRT2aQDaqLGaxvta6J5UxIUmAp+wGdV/juGEvQ="}
4. Accept: application/json
5. {
6. "mercOrderNo": "czl00120240705***"
7. }
```

## 响应参数

**Response Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |

**Response Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| resultCode | 是 | String | 返回码，“000000”表示成功，其他表示异常，请参见[错误码](payment-error-code-rest.md#公共错误码说明)。 |
| resultDesc | 是 | String | 结果描述。 |
| subCode | 否 | String | 业务错误码。 |
| subDesc | 否 | String | 业务错误描述信息。 |
| sign | 是 | String | 签名值。用于开发者对响应报文进行防篡改验证。 |

## 响应示例

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "000000",
5. "resultDesc": "Success.",
6. "sign": "MEQCIEIWzdpziRyTi8vhwWHFu********************0YAMabeCgTDG77e+2XJItvq/ZkIcCN5/B20pQ=="
7. }
```

## 错误码

**resultCode**非400000的错误码请查看[公共错误码说明](payment-error-code-rest.md#公共错误码说明)。

| **返回码** | **错误码** | **错误描述** | 解决方案 |
| --- | --- | --- | --- |
| 400000 | UNKNOW\_ERROR | 服务暂不可用，请稍后重试 | 稍后重试。 |
| 400000 | INVALID\_ARGUMENTS | 参数不合法 | 检查请求参数。 |
| 400000 | INVALID\_MERCNO | 无效商户号 | 检查入参商户号是否正确。 |
| 400000 | MERC\_ORDER\_NOT\_EXIST | 商户订单号不存在 | 检查入参订单号是否正确。 |
