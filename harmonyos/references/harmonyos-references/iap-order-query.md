---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-order-query
title: 应用购买记录相关支付订单查询
breadcrumb: API参考 > 应用服务 > IAP Kit（应用内支付服务） > REST API > 应用购买记录相关支付订单查询
category: harmonyos-references
scraped_at: 2026-04-28T08:16:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8cd17bac85084f72d02d5ef5e449a8b476b38e0155d5757a7f66b88460196fe2
---

## 功能介绍

此接口用于查询指定时间范围内的付款和退款订单。

## 场景描述

例如：当开发者需要查看前一天的付款和退款订单时，可以将开始时间设为前一天的零点，结束时间设为当天的零点，然后调用此接口查询相关的订单记录。

说明

* 由于当天的订单信息可能还会发生变动，因此不建议使用此接口查询当天的实时订单数据，建议延迟一天查询。
* 当前仅支持查询180天内的订单数据。
* 当前不支持查询沙盒订单和0元订单。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> IAP服务器
* **接口URL：** {rootUrl}/order/harmony/v1/application/trade/orders/query

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
| startTime | 是 | Long | 指定查询范围的开始时间，UTC时间戳，以毫秒为单位。  startTime不能大于当前时间。 |
| endTime | 是 | Long | 指定查询范围的结束时间，UTC时间戳，以毫秒为单位。  - 结束时间endTime与开始时间startTime的时间差为48小时或者48小时内。  - 结束时间endTime必须大于开始时间startTime。 |
| continuationToken | 否 | String | 支持分页查询的数据定位标志。  - 初始请求时无需输入，当响应结果返回continuationToken时，下一次查询时需要输入上次查询返回的continuationToken才可以查询下一页数据。 |

## 请求示例

```
1. POST /order/harmony/v1/application/trade/orders/query
2. Content-Type: application/json; charset=UTF-8
3. Authorization: Bearer ***.***.***
4. Accept: application/json
5. {
6. "startTime": 1739548800000,
7. "endTime": 1739721600000
8. }
```

## 响应参数

### Response Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=UTF-8 |

### Response Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| responseCode | 是 | String | 返回码。  0：成功。  其他：失败，具体请参见[错误码](iap-server-error-code.md)。 |
| responseMessage | 否 | String | 响应描述。 |
| orderInfoList | 否 | List<Object> | 订单信息列表，其中每个JSONObject表示一个订单信息，订单信息格式参见[OrderInfo](iap-order-query.md#orderinfo)。 |
| continuationToken | 否 | String | 支持分页查询的数据定位标志。如果返回，下一次查询请求时需要输入，以此查询下一页数据。 |

## 响应示例

```
1. HTTP/1.2 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "responseCode": "0",
5. "orderInfoList": [
6. {
7. "requestId": "***",
8. "country": "CN",
9. "merchantId": "***",
10. "applicationId": "***",
11. "orderTime": 1739602800000,
12. "tradeTime": 1739602800000,
13. "productId": "***",
14. "productName": "test",
15. "payMoney": "10.00",
16. "couponAmt": "0.10",
17. "currency": "CNY",
18. "tradeState": 0,
19. "tradeType": "REFUND",
20. "refundTime": 1739620800000,
21. "refundMoney": "0.02"
22. },
23. {
24. "requestId": "***",
25. "country": "CN",
26. "merchantId": "***",
27. "applicationId": "***",
28. "orderTime": 1739602800000,
29. "tradeTime": 1739602800000,
30. "productId": "***",
31. "productName": "测试商品",
32. "payMoney": "0.01",
33. "currency": "CNY",
34. "tradeState": 0,
35. "tradeType": "PURCHASE"
36. },
37. ],
38. "continuationToken": "***"
39. }
```

### OrderInfo

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| requestId | 是 | String | 具体一笔订单中对应的购买订单号ID，同purchaseOrderId。最大长度256。 |
| country | 是 | String | 国家/地区码，用于区分国家/地区信息，请参见[ISO 3166](https://www.iso.org/iso-3166-country-codes.html)标准。 |
| merchantId | 是 | String | 商户ID。 |
| applicationId | 是 | String | 应用ID。 |
| orderTime | 是 | Long | 下单时间，UTC时间戳，以毫秒为单位。 |
| tradeTime | 是 | Long | 支付时间，UTC时间戳，以毫秒为单位。  **说明：** 支付时间（tradeTime）在[startTime,endTime)范围内的订单将被查询出来。 |
| productId | 是 | String | 商品ID。 |
| productName | 是 | String | 商品名称。 |
| payMoney | 是 | String | 支付金额，单位为元。 |
| couponAmt | 否 | String | 优惠券金额，单位为元。 |
| currency | 是 | String | 币种。 |
| tradeState | 是 | Integer | 订单状态。  0：成功。 |
| tradeType | 是 | String | 交易类型。  - PURCHASE：支付。  - REFUND：退款。 |
| refundTime | 否 | Long | 退款时间，UTC时间戳，以毫秒为单位。 |
| refundMoney | 否 | String | 退款金额，单位为元。 |
