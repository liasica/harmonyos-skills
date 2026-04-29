---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-server-refund-receive-notify
title: 接收退款申请事件通知
breadcrumb: API参考 > 应用服务 > IAP Kit（应用内支付服务） > REST API > 退款申请通知与处理 > 接收退款申请事件通知
category: harmonyos-references
scraped_at: 2026-04-29T14:07:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ed350c02abcc66972120558c771b27c274629e4030691fd31cebc70e24de6011
---

## 功能介绍

用户申请退款时，IAP服务器调用此接口向开发者服务器发送退款审核事件通知。

## 场景描述

如果开发者在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)申请支付服务时提前[配置通知接收地址](../harmonyos-guides/iap-set-necessary-parameters.md#配置订单订阅通知接收地址)，并且通知版本设置为v3，用户申请对已支付订单进行退款时，IAP服务器会调用此接口通知已配置的服务器。

若开发者服务器返回结果为非成功响应（请求返回的HTTP状态码不为200），IAP服务器将对本次关键事件的通知进行周期性重发。建议开发者服务端在收到通知后立即返回成功响应，避免通知消息堆积。

为保证可靠性，IAP服务端具备补偿机制，所以可能出现重发的通知比预期（成功回调1次）的多。

关键事件通知处理流程建议如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/m8KPG5RJTaCbngcpTgynqw/zh-cn_image_0000002558767426.png?HW-CC-KV=V1&HW-CC-Date=20260429T060742Z&HW-CC-Expire=86400&HW-CC-Sign=DF19D4EA1572A5EA7AE12E9825E12B930806779368BA5DF1F585C9C8E6774119)

1. IAP服务器发送退款请求关键事件通知。
2. 应用服务器收到通知请求后，从通知中获取用户申请的退款信息，决策该笔退款订单的处理方式。
3. 将退款审核结果通知给IAP服务器。
4. 若开发者审核结果为同意退款，则IAP服务器会发起退款，否则流程终止。
5. 退款成功后，IAP会将订单退款/撤销订阅事件通知到应用服务器。

## 接口约束

不建议开发者服务器设置IP允许清单用于限制华为侧的出口IP地址。IP允许清单本身并不能提高安全性且会给业务发展带来约束，IAP服务在消息层面已有更安全的JWS签名机制条件下，没有存在价值。不遵守该约定而导致的后果将由开发者自行承担。

如开发者需接收退款关键事件通知，需要在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中配置开发者服务器的回调地址，地址必须支持HTTPS协议且具有合法商用证书，出于安全考虑，cipher需要支持ECDHE-RSA-AES128-GCM-SHA256、ECDHE-ECDSA-AES128-GCM-SHA256、ECDHE-RSA-AES256-GCM-SHA384或ECDHE-ECDSA-AES256-GCM-SHA384中至少一种，否则无法正常接收通知消息。

说明

当前沙盒订单退款不支持退款申请事件通知，用户提交退款请求后，IAP服务会跳过退款审核流程，直接完成退款，同时给开发者服务器发送退款成功事件通知（NotificationSubtype：REFUND\_TRANSACTION）。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** IAP服务器 -> 开发者服务器
* **接口URL：** URL由开发者在申请支付服务时配置
* **数据格式：**

  请求消息：Content-Type: application/json; charset=UTF-8

  响应消息：Content-Type: application/json; charset=UTF-8

## 请求参数

### Request Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| jwsNotification | 是 | String | 通知内容信息，对通知内容NotificationPayload签名后的字符串。具体请参见表[NotificationPayload](iap-server-refund-receive-notify.md#notificationpayload)。  需要参见[对返回结果验签](iap-verifying-signature.md)使用JWS签名方式对NotificationPayload消息体进行验签。 |

### NotificationPayload

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| notificationType | 是 | String | 通知主类型。  REFUND\_REQUEST：退款审核事件通知。 |
| notificationRequestId | 是 | String | 通知唯一请求ID。 |
| notificationMetaData | 是 | Object | 通知元数据，具体请参见表[NotificationMetaData](iap-server-refund-receive-notify.md#notificationmetadata)说明。 |
| notificationVersion | 是 | String | 通知版本：v3。 |
| signedTime | 是 | Long | 通知签名时间，UTC时间戳，以毫秒为单位。 |

### NotificationMetaData

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| environment | 是 | String | 环境类型。  NORMAL：正式环境 |
| applicationId | 是 | String | 应用ID。 |
| packageName | 是 | String | 应用包名。 |
| refundRequestData | 是 | [RefundRequestData](iap-server-refund-receive-notify.md#refundrequestdata) | 具体退款申请信息。 |

### RefundRequestData

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| refundReason | 是 | String | 用户申请退款理由。  - LEGAL：未成年人未经允许购买  - UNINTENDED\_PURCHASE：无意购买或订阅  - UNSATISFIED\_WITH\_PURCHASE：购买的商品无法正常使用  - FULFILLMENT\_ISSUE：未收到商品  - OTHER：其他原因 |
| applyAmount | 是 | Long | 申请退款金额，单位：分。 |
| currency | 是 | String | 币种。  CNY：人民币 |
| applyType | 是 | Integer | 请求类型。  1：初次提交 |
| refundBatchNo | 是 | String | 退款批次号。 |
| refundOrders | 是 | List<[RefundOrder](iap-server-refund-receive-notify.md#refundorder)> | 退款申请工单下的订单号，当前仅游戏应用场景支持多笔订单。 |

### RefundOrder

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| purchaseOrderId | 是 | String | 具体一笔订单中对应的购买订单号。最大长度256。 |
| purchaseToken | 是 | String | 商品的购买Token。最大长度256。 |
| payAmount | 是 | Long | 该笔订单实付金额，单位分。 |

## 请求示例

```
1. POST /notify/address
2. Content-Type: application/json;charset=UTF-8
3. Accept: application/json
4. {
5. "jwsNotification": "***"
6. }
```

NotificationPayload样例（消耗型/非消耗型）

```
1. {
2. "notificationType": "REFUND_REQUEST",
3. "notificationRequestId": "7f67e39aa72d1a55f36293047f9769c0aa47a467ffb110eaeeeb888def9f9713",
4. "notificationMetaData": {
5. "environment": "NORMAL",
6. "applicationId": "***",
7. "packageName": "***",
8. "refundRequestData": {
9. "refundReason": "UNINTENDED_PURCHASE",
10. "applyAmount": 1,
11. "applyType": 1,
12. "refundBatchNo": "***",
13. "currency": "CNY",
14. "refundOrders": [
15. {
16. "purchaseOrderId": "***",
17. "purchaseToken": "***",
18. "payAmount": 1
19. }
20. ]
21. }
22. },
23. "notificationVersion": "v3",
24. "signedTime": 1741073978222
25. }
```

## 响应参数

通过HTTP状态码来标识IAP服务器通知开发者服务器是否发送成功：

* 如果通知发送成功，则发送HTTP 200，不需要返回响应体。
* 如果通知发送失败，则通过发送HTTP 40X或者HTTP 50X，告知IAP服务器进行重试，IAP服务器会在一段时间内重试多次。

## 响应示例

```
1. HTTP/1.2 200 OK
```
