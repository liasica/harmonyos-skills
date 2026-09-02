---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-query-subscription-status
title: 订阅状态查询
breadcrumb: API参考 > 应用服务 > IAP Kit（应用内支付服务） > REST API > 订阅状态查询
category: harmonyos-references
scraped_at: 2026-09-02T15:02:56+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:9d9669191b91da2f202e1a48f849937ff5af47a5aca3864c24fadf6766218d35
---

## 功能介绍

此接口用于查询自动续期订阅商品的最新状态。

## 场景描述

开发者服务器收到IAP服务端关键事件通知后，调用该接口获取订阅最新状态。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> IAP服务器
* **接口URL：** {rootUrl}/subscription/harmony/v1/application/subscription/status/query

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

```json
POST /subscription/harmony/v1/application/subscription/status/query
Content-Type: application/json;charset=UTF-8
Authorization: Bearer ***.***.***
Accept: application/json
{
  "purchaseToken": "***.*.***",
  "purchaseOrderId": "***.*.***"
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
| responseCode | 是 | String | 返回码。  0：成功。  其他：失败，具体请参见[错误码](iap-server-error-code.md)。 |
| responseMessage | 否 | String | 响应描述。 |
| jwsSubGroupStatus | 是 | String | 包含已购订阅相关状态信息的JWS格式数据。可参见[对返回结果验签](iap-verifying-signature.md)解码验签获取相关订阅状态信息的JSON字符串，其包含的参数请参见[SubGroupStatusPayload](iap-query-subscription-status.md#subgroupstatuspayload)。 |

### SubGroupStatusPayload

| 参数 | 是否必选 | 类型 | 说明 |
| --- | --- | --- | --- |
| environment | 是 | String | 环境类型。  - NORMAL：生产环境  - SANDBOX：沙盒环境 |
| applicationId | 是 | String | 应用ID。 |
| packageName | 是 | String | 应用包名。 |
| subGroupId | 是 | String | 订阅组ID。 |
| lastSubscriptionStatus | 否 | Object | 订阅组中最后生效的订阅状态[SubscriptionStatus](iap-query-subscription-status.md#subscriptionstatus)，比如A切换B，B切换C，此处是C的订阅状态。 |
| historySubscriptionStatusList | 否 | List<Object> | 订阅组最近生效的历史订阅状态[SubscriptionStatus](iap-query-subscription-status.md#subscriptionstatus)的列表，按订阅切换时间升序 ，最多包含10条有效订阅状态信息的记录 。  比如A切换B，B切换C，这里包含A，B，C三个订阅状态信息。 |

### SubscriptionStatus

| 参数 | 是否必选 | 类型 | 说明 |
| --- | --- | --- | --- |
| subGroupGenerationId | 是 | String | 订阅组的代ID。  - 用户切换订阅商品时，此ID不会改变。  - 订阅失效且超出[保留期](../harmonyos-guides/iap-subscription-functions.md#保留期)后，用户重新购买商品时，此ID会改变。 |
| subscriptionId | 是 | String | 商品的订阅ID。以下场景，此ID会发生改变：  - 用户切换订阅商品时。  - 订阅失效且超出[保留期](../harmonyos-guides/iap-subscription-functions.md#保留期)后，用户重新购买商品时。 |
| purchaseToken | 是 | String | 购买token，在购买消耗型/非消耗型/非续期订阅商品场景中与具体购买订单一一对应，在订阅型商品场景中与订阅ID一一对应。最大长度256。 |
| status | 是 | String | 订阅状态。  1：生效中  2：已到期  3：尝试扣费  5：撤销 |
| expiresTime | 是 | Long | 自动续期订阅商品的过期时间，UTC时间戳，以毫秒为单位。 |
| lastPurchaseOrder | 否 | Object | 当前订阅最新的一笔购买订单。包含的参数请参见[PurchaseOrderPayload](iap-server-data-model.md#purchaseorderpayload)。 |
| recentPurchaseOrderList | 否 | List<Object> | 当前订阅最新的购买订单列表，包含续期、折算、延期等产生的购买订单。购买订单包含的参数请参见[PurchaseOrderPayload](iap-server-data-model.md#purchaseorderpayload)。 |
| renewalInfo | 否 | Object | 当前订阅最新的未来扣费计划，包含的参数请参见[SubRenewalInfo](iap-query-subscription-status.md#subrenewalinfo)。 |

### SubRenewalInfo

| 参数 | 是否必选 | 类型 | 说明 |
| --- | --- | --- | --- |
| environment | 是 | String | 环境类型。  - NORMAL：生产环境  - SANDBOX：沙盒环境 |
| subGroupGenerationId | 是 | String | 订阅组的代ID。  - 用户切换订阅商品时，此ID不会改变。  - 订阅失效且超出[保留期](../harmonyos-guides/iap-subscription-functions.md#保留期)后，用户重新购买商品时，此ID会改变。 |
| nextRenewPeriodProductId | 否 | String | 下一个计费周期续订的商品ID。 |
| productId | 是 | String | 当前生效的商品ID。 |
| autoRenewStatusCode | 是 | String | 自动续期状态。  0：关闭  1：打开 |
| hasInBillingRetryPeriod | 是 | Boolean | 系统是否还在尝试扣费。  - true：是  - false：否 |
| priceIncreaseStatusCode | 否 | String | 目前涨价状态码。  1：用户暂未同意涨价  2：用户已同意涨价 |
| offerTypeCode | 否 | String | 优惠类型。  1：推介促销  2：优惠促销  4：挽留促销 |
| offerId | 否 | String | 优惠ID。 |
| renewalPrice | 否 | Long | 下期续费价格，单位：分，取消订阅场景下不返回。 |
| currency | 否 | String | 币种，请参见[ISO 4217](https://www.iso.org/iso-4217-currency-codes.html)标准。例如CNY、USD、MYR。 |
| renewalTime | 否 | Long | 续期时间，UTC时间戳，以毫秒为单位。 |
| expirationIntent | 否 | String | 订阅续期失败的原因。  1：用户取消  2：商品无效  3：签约无效  4：扣费异常  5：用户不同意涨价  6：未知  7：存在未发货的订阅 |
| nextRenewPeriodPayload | 否 | String | 商户侧保留信息，由开发者在调用[支付接口](iap-iap.md#iapcreatepurchase)时传入。 |

## 响应示例

```json
HTTP/1.2 200 OK
Content-Type: application/json;charset=UTF-8
{
  "responseCode": "0",
  "jwsSubGroupStatus": "***"
}
```

[SubGroupStatusPayload](iap-query-subscription-status.md#subgroupstatuspayload)结构体示例：

```javascript
{
    "environment": "NORMAL",
    "applicationId": "10***58",
    "packageName": "demoApp",
    "subGroupId": "demoSubGroup",
    "lastSubscriptionStatus": {
        "subGroupGenerationId": "c0e5f80732852b92f7111b8b9ed4fbb************c842ea854dfa2da67ab9e",
        "subscriptionId": "*************.********.****",
        "purchaseToken": "***.*.***",
        "status": "5",
        "expiresTime": 1721716039363,
        "lastPurchaseOrder": {
            "subGroupGenerationId": "c0e5f80732852b92f7111b8b9ed4fbb************c842ea854dfa2da67ab9e",
            "purchaseOrderId": "*************.********.****",
            "subscriptionId": "*************.********.****",
            "purchaseToken": "***.*.***",
            "applicationId": "10***58",
            "productId": "demoProduct",
            "subGroupId": "demoSubGroup",
            "purchaseTime": 1721082441000,
            "duration": "P1W",
            "durationTypeCode": "0",
            "productType": "2",
            "developerPayload": "demoPayload",
            "signedTime": 1721111398533,
            "purchaseOrderRevocationReasonCode": "1",
            "revocationTime": 1721111240720,
            "offerTypeCode": "1",
            "offerId": "12**56",
            "environment": "NORMAL",
            "countryCode": "CN",
            "price": 880,
            "currency": "SGD",
            "finishStatus": "1"
        },
        "recentPurchaseOrderList": [
            {
                "subGroupGenerationId": "c0e5f80732852b92f7111b8b9ed4fbb************c842ea854dfa2da67ab9e",
                "purchaseOrderId": "*************.********.****",
                "subscriptionId": "*************.********.****",
                "purchaseToken": "***.*.***",
                "applicationId": "10***58",
                "productId": "demoProduct",
                "subGroupId": "demoSubGroup",
                "purchaseTime": 1721082441000,
                "duration": "P1W",
                "durationTypeCode": "0",
                "productType": "2",
                "developerPayload": "demoPayload",
                "signedTime": 1721111398533,
                "purchaseOrderRevocationReasonCode": "1",
                "revocationTime": 1721111240720,
                "offerTypeCode": "1",
                "offerId": "12**56",
                "environment": "NORMAL",
                "countryCode": "CN",
                "price": 880,
                "currency": "SGD",
                "finishStatus": "1"
            }
        ],
        "renewalInfo": {
            "subGroupGenerationId": "c0e5f80732852b92f7111b8b9ed4fbb************c842ea854dfa2da67ab9e",
            "productId": "demoProduct",
            "autoRenewStatusCode": "0",
            "hasInBillingRetryPeriod": false,
            "environment": "NORMAL"
        }
    },
    "historySubscriptionStatusList": [
        {
            "subGroupGenerationId": "c0e5f80732852b92f7111b8b9ed4fbb************c842ea854dfa2da67ab9e",
            "subscriptionId": "*************.********.****",
            "purchaseToken": "***.*.***",
            "status": "5",
            "expiresTime": 1721716039363,
            "lastPurchaseOrder": {
                "subGroupGenerationId": "c0e5f80732852b92f7111b8b9ed4fbb************c842ea854dfa2da67ab9e",
                "purchaseOrderId": "*************.********.****",
                "subscriptionId": "*************.********.****",
                "purchaseToken": "***.*.***",
                "applicationId": "10***58",
                "productId": "demoProduct",
                "subGroupId": "demoSubGroup",
                "purchaseTime": 1721082441000,
                "duration": "P1W",
                "durationTypeCode": "0",
                "productType": "2",
                "developerPayload": "demoPayload",
                "signedTime": 1721111398533,
                "purchaseOrderRevocationReasonCode": "1",
                "revocationTime": 1721111240720,
                "offerTypeCode": "1",
                "offerId": "12**56",
                "environment": "NORMAL",
                "countryCode": "CN",
                "price": 880,
                "currency": "SGD",
                "finishStatus": "1"
            },
            "recentPurchaseOrderList": [
                {
                    "subGroupGenerationId": "c0e5f80732852b92f7111b8b9ed4fbb************c842ea854dfa2da67ab9e",
                    "purchaseOrderId": "*************.********.****",
                    "subscriptionId": "*************.********.****",
                    "purchaseToken": "***.*.***",
                    "applicationId": "10***58",
                    "productId": "demoProduct",
                    "subGroupId": "demoSubGroup",
                    "purchaseTime": 1721082441000,
                    "duration": "P1W",
                    "durationTypeCode": "0",
                    "productType": "2",
                    "developerPayload": "demoPayload",
                    "signedTime": 1721111398533,
                    "purchaseOrderRevocationReasonCode": "1",
                    "revocationTime": 1721111240720,
                    "offerTypeCode": "1",
                    "offerId": "12**56",
                    "environment": "NORMAL",
                    "countryCode": "CN",
                    "price": 880,
                    "currency": "SGD",
                    "finishStatus": "1"
                }
            ],
            "renewalInfo": {
                "subGroupGenerationId": "c0e5f80732852b92f7111b8b9ed4fbb************c842ea854dfa2da67ab9e",
                "productId": "demoProduct",
                "autoRenewStatusCode": "0",
                "hasInBillingRetryPeriod": false,
                "environment": "NORMAL"
            }
        }
    ]
}
```
