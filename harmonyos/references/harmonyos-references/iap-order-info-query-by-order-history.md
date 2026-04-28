---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-order-info-query-by-order-history
title: 查询用户的历史购买记录
breadcrumb: API参考 > 应用服务 > IAP Kit（应用内支付服务） > REST API > 查询用户的历史购买记录
category: harmonyos-references
scraped_at: 2026-04-28T08:16:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ca3590c931ee9e726c49198f23ada85c303504d340ac55ccead798a988921f2a
---

## 功能介绍

此接口用于查询用户的历史购买记录。

## 场景描述

开发者可以通过此接口查询用户的历史购买记录，来判断是否给用户展示促销价格、是否已完成权益发放等场景。

说明

1. 支持查询七年内的历史购买记录。
2. 不支持查询沙盒历史购买记录。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> IAP服务器
* **接口URL：** {rootUrl}/harmony/v1/application/user/orders/query

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
| purchaseOrderId | 是 | String | 待查询用户的具体一笔订单中对应的购买订单号。最大长度256。 |
| productType | 否 | Integer | 用于查询指定商品类型的历史购买记录。取值如下：  0：消耗型商品  1：非消耗型商品  2：自动续期订阅商品  3：非续期订阅商品 |
| startTime | 否 | Long | 查询开始时间，UTC时间戳，以毫秒为单位。若startTime未指定，取值如下：  - 指定endTime，startTime取值为：endTime - 365天。  - 未指定endTime，startTime取值为：当前时间 - 365天。 |
| endTime | 否 | Long | 查询结束时间，UTC时间戳，以毫秒为单位。若endTime未指定，取值如下：  - 指定startTime，endTime取值为：startTime + 365天，但不会早于当前时刻。  - 未指定startTime，endTime取值为：当前时间。  **说明：** 查询时间范围不超过365天。 |
| productIdList | 否 | List<String> | 用于查询指定商品ID的历史购买记录，可以指定最多10个商品ID。 |
| subGroupIdList | 否 | List<String> | 用于查询指定订阅组ID的历史购买记录，可以指定最多10个订阅组ID。 |
| refunded | 否 | Boolean | 用于查询是否退款的历史购买记录。取值如下：  - true：仅查询退款的历史购买记录。  - false：仅查询未退款的历史购买记录。 |
| sort | 否 | String | 用于指定用户历史购买记录的返回顺序，取值如下：  - ASCENDING（默认）：按购买时间升序排列，最早记录优先返回。  - DESCENDING：按购买时间降序排列，最新记录优先返回。 |
| continuationToken | 否 | String | 支持分页查询的数据定位标志，分页查询时每一页最多包含10条历史购买记录。  - 初始请求时无需输入，当响应结果返回continuationToken时，下一次查询时需要输入上次查询返回的continuationToken才可以查询下一页数据。 |

## 请求示例

```
1. POST /harmony/v1/application/user/orders/query
2. Content-Type: application/json;charset=UTF-8
3. Authorization: Bearer ***.***.***
4. Accept: application/json
5. {
6. "purchaseOrderId": "******"
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
| jwsPurchaseOrderList | 否 | List<String> | 已购订单相关状态信息的JWS格式数据的数组。  可参见[返回结果验签](iap-verifying-signature.md)处理，验签通过后解码获取相关订单状态信息，具体请参见[PurchaseOrderPayload](iap-server-data-model.md#purchaseorderpayload)说明。 |
| continuationToken | 否 | String | 支持分页查询的数据定位标志。如果返回，下一次查询请求时需要输入，以此查询下一页数据。 |

## 响应示例

```
1. HTTP/1.2 200 OK
2. Content-Type: application/json;charset=UTF-8
3. {
4. "responseCode": "0",
5. "jwsPurchaseOrderList": ["****","****","****","****"],
6. "continuationToken": "***"
7. }
```
