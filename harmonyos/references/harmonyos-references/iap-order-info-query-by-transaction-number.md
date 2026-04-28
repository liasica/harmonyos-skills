---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-order-info-query-by-transaction-number
title: 根据交易号查询订单状态信息
breadcrumb: API参考 > 应用服务 > IAP Kit（应用内支付服务） > REST API > 根据交易号查询订单状态信息
category: harmonyos-references
scraped_at: 2026-04-28T08:16:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:42861dc67ad6b7e1d4f4b1bfd7b47218e42bde6c6603126e55ffce8c91518405
---

## 功能介绍

此接口用于查询交易号对应的订单状态信息。

## 场景描述

当用户对订单存在疑问时，可以通过交易号向开发者寻求技术支持，开发者通过调用该接口查询对应的订单状态信息。

说明

该接口仅支持查询一年内的订单。

该接口不支持查询沙盒测试订单。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> IAP服务器
* **接口URL：** {rootUrl}/harmony/v1/application/order/lookup

  说明：rootUrl具体请参见[站点信息](iap-rest-common-statement.md#站点信息)。
* **数据格式：**

  请求消息：Content-Type: application/json; charset=UTF-8

  响应消息：Content-Type: application/json; charset=UTF-8

## 请求参数

### Request Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=UTF-8 |
| Authorization | 是 | String | 认证信息，使用JWT进行鉴权，具体请参见[Authorization说明](iap-jwt-description.md#authorization说明)。 |

### Request Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| orderNo | 是 | String | 具体一笔订单对应的交易号，交易号可在用户设备的"设置">"华为账号">"付款与账单">"购买记录"中对应订单详情中获取。 |

## 请求示例

```
1. POST /harmony/v1/application/order/lookup
2. Content-Type: application/json;charset=UTF-8
3. Authorization: Bearer ***.***.***
4. Accept: application/json
5. {
6. "orderNo": "******"
7. }
```

## 响应参数

### Response Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=UTF-8 |

### Response Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| responseCode | 是 | String | 返回码。  0：成功  其他：失败，具体请参见[错误码](iap-server-error-code.md) |
| responseMessage | 否 | String | 响应描述。 |
| orderStatus | 是 | Integer | 标识开发者在请求中提供的交易号是否有效。  1：交易号有效，且存在一笔订单状态信息  0：交易号无效 |
| jwsPurchaseOrder | 否 | String | 已购订单相关状态信息的JWS格式数据。  可参见[对返回结果验签](iap-verifying-signature.md)处理，验签通过后解码获取相关订单状态信息，具体请参见[PurchaseOrderPayload](iap-server-data-model.md#purchaseorderpayload)说明。 |

## 响应示例

```
1. HTTP/1.2 200 OK
2. Content-Type: application/json;charset=UTF-8
3. {
4. "responseCode": "0",
5. "responseMessage": "success",
6. "orderStatus": 1,
7. "jwsPurchaseOrder": "***"
8. }
```
