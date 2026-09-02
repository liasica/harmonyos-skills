---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-confirm-purchase-for-sub
title: 订阅确认发货
breadcrumb: API参考 > 应用服务 > IAP Kit（应用内支付服务） > REST API > 订阅确认发货
category: harmonyos-references
scraped_at: 2026-09-02T15:02:56+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:c4e9d18906c784481c09be34944d2b876b8b275e5be920509f8355ebf8a07c15
---

## 功能介绍

此接口用于通知IAP服务器，开发者服务器已经向用户发放权益。

## 场景描述

开发者服务器收到IAP服务器关键事件通知后，调用订阅状态查询接口获取订阅的最新状态，再根据订阅状态发放权益，具体请参见[确保权益发放](../harmonyos-guides/iap-delivering-subscriptions.md#确保权益发放)。

**说明** 

一个购买订单号ID（purchaseOrderId）只可以发货一次，请勿重复发货。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> IAP服务器
* **接口URL：** {rootUrl}/subscription/harmony/v1/application/purchase/shipped/confirm

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
| purchaseOrderId | 是 | String | 具体一笔订单中对应的购买订单号ID。最大长度256。 |
| purchaseToken | 是 | String | 商品的购买Token，发起购买和查询订单信息均会返回。最大长度256。 |

## 请求示例

更多语言及详细的代码示例，请参考[IAP Kit-Sample-ServerDemo](https://gitcode.com/HarmonyOS_Samples/iapkit-sample-serverdemo)。

```javascript
POST /subscription/harmony/v1/application/purchase/shipped/confirm
Content-Type: application/json;charset=UTF-8
Authorization: Bearer ***.***.***
Accept: application/json
{
  "purchaseToken": "***.*.***",
  "purchaseOrderId": "****.*.***"
}
```

## 响应参数

### Response Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=UTF-8 |

### Response Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| responseCode | 是 | String | 返回码。  0：成功。  失败，具体请参见[错误码](iap-server-error-code.md)。 |
| responseMessage | 否 | String | 响应描述。 |

## 响应示例

```javascript
HTTP/1.2 200 OK
Content-Type: application/json;charset=UTF-8
{
  "responseCode": "0"
}
```
