---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-server-notifications-record-query
title: 服务端通知记录查询
breadcrumb: API参考 > 应用服务 > IAP Kit（应用内支付服务） > REST API > 服务端通知记录查询
category: harmonyos-references
scraped_at: 2026-04-28T08:16:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5aec1c418dc502154b6223b1c989f910af90ff7695a65d89ecfce38ac759e24c
---

## 功能介绍

查询历史的服务端通知记录。

## 场景描述

开发者可以通过此接口查询历史的服务端通知记录，来确保不会漏处理服务端通知。

说明

1. 支持查询最近30天内的通知记录。
2. 不支持查询沙盒的通知记录。
3. 1秒只允许调用一次。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> IAP服务器
* **接口URL：** {rootUrl}/harmony/v1/application/notifications/query

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
| startTime | 是 | Long | 指定查询范围的开始时间，UTC时间戳，以毫秒为单位。  **说明：**  - startTime不能大于当前时间。  - 查询时间范围不超过最近30天。 |
| endTime | 是 | Long | 指定查询范围的结束时间，UTC时间戳，以毫秒为单位。  - endTime不能大于当前时间。  - 结束时间endTime必须大于开始时间startTime。 |
| notificationType | 否 | String | 通知主类型，不传查所有通知类型。通知主类型，具体请参见表[NotificationType](iap-key-event-notifications.md#notificationtype)说明 |
| sendResult | 否 | Integer | 通知发送结果，不传则查成功与失败的记录。  0：成功  1：失败 |
| purchaseOrderIdList | 否 | List<String> | 购买订单ID列表。 |
| continuationToken | 否 | String | 支持分页查询的数据定位标志。  初始请求时无需输入，当响应结果返回continuationToken时，下一次查询时需要输入上次查询返回的continuationToken才可以查询下一页数据。 |

## 请求示例

```
1. POST /harmony/v1/application/notifications/query
2. Content-Type: application/json;charset=UTF-8
3. Authorization: Bearer ***.***.***
4. Accept: application/json
5. {
6. "startTime": 1751299200000,
7. "endTime": 1751472000000
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
| responseCode | 是 | String | 返回码。  0：成功  失败，具体请参见[错误码](iap-server-error-code.md) |
| responseMessage | 否 | String | 响应描述。 |
| notificationHistory | 否 | List<Object> | 历史通知记录信息。具体请参见[NotificationHistory](iap-server-notifications-record-query.md#notificationhistory)说明。 |
| continuationToken | 否 | String | 支持分页查询的数据定位标志。如果返回，下一次查询请求时需要输入，以此查询下一页数据。 |

## NotificationHistory

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| jwsNotification | 是 | String | 通知内容信息，对通知内容NotificationPayload签名后的字符串。具体请参见表[NotificationPayload](iap-key-event-notifications.md#notificationpayload)。  需要参见[对返回结果验签](iap-verifying-signature.md)使用JWS签名方式对NotificationPayload消息体进行验签。 |
| sendResult | 是 | Integer | 通知发送结果。  0：成功  1：失败 |

## 响应示例

```
1. HTTP/1.2 200 OK
2. Content-Type: application/json;charset=UTF-8
3. {
4. "responseCode": "0",
5. "notificationHistory": [
6. {
7. "jwsNotification": "****",
8. "sendResult": 0
9. },
10. {
11. "jwsNotification": "****",
12. "sendResult": 1
13. }
14. ],
15. "continuationToken": "***"
16. }
```
