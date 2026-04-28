---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-server-notifications-test
title: 测试服务端通知
breadcrumb: API参考 > 应用服务 > IAP Kit（应用内支付服务） > REST API > 测试服务端通知
category: harmonyos-references
scraped_at: 2026-04-28T08:16:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:22c97d01df1a7f710a01b119dbf8689c8a22b4f502d77a7bedf9905fe495fcb7
---

## 功能介绍

此接口用于测试服务端通知。

## 场景描述

开发者调用此接口，IAP服务器向开发者服务器发送测试通知。

说明

1. 5分钟内只允许调用一次，在开发者服务器收到测试通知后，不建议再次调用此接口。
2. 测试通知只支持开发者的生产环境通知地址。
3. 测试通知主类型为TEST，无通知子类型，具体请参见[NotificationType](iap-key-event-notifications.md#notificationtype)说明。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> IAP服务器
* **接口URL：** {rootUrl}/harmony/v1/application/notifications/test

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

## 请求示例

```
1. POST /harmony/v1/application/notifications/test
2. Content-Type: application/json;charset=UTF-8
3. Authorization: Bearer ***.***.***
4. Accept: application/json
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
| testNotificationId | 是 | String | 测试通知ID。 |

## 响应示例

```
1. HTTP/1.2 200 OK
2. Content-Type: application/json;charset=UTF-8
3. {
4. "responseCode": "0",
5. "testNotificationId": "***"
6. }
```

## 测试服务端通知样例

```
1. {
2. "notificationType": "TEST", // 固定为TEST
3. "notificationRequestId": "xxx",
4. "notificationMetaData": {
5. "environment": "NORMAL", // 固定为NORMAL
6. "applicationId": "xxx", // 应用ID
7. "packageName": "testPackageName", // 固定为testPackageName
8. "type": 0, // 固定为0
9. "purchaseToken": "xxx", // 前缀固定为testPurchaseToken，后面为应用ID
10. "purchaseOrderId": "xxx" // 前缀固定为testPurchaseOrderId，后面为应用ID
11. },
12. "notificationVersion": "v3", // 固定为v3
13. "signedTime": 1747445946282
14. }
```
