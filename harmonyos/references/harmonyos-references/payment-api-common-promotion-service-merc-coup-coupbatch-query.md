---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-promotion-service-merc-coup-coupbatch-query
title: 查询券批次详情
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 通用接口 > 运营工具 > 商家券 > 券批次 > 查询券批次详情
category: harmonyos-references
scraped_at: 2026-09-02T14:53:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:25f4fd8e16e9cfacf36d058301530aa930a3bca3724dd384d166b6d7189c0aab
---

## 功能介绍

商户可通过该接口查询已创建的商家券批次详情信息。

## 接口原型

* **承载协议：** HTTPS GET
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** https://petalpay-developer.cloud.huawei.com.cn/api/merchantgrow/v1/merchantcoupon/couponbatch/querydetail/{batchNo}
* **数据格式：**

  请求消息：Content-Type: application/json

  响应消息：Content-Type: application/json

## 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |
| PayMercAuth | 是 | String | 取值为：[PayMercAuth](payment-model.md#paymercauth)的JSON字符串 |

**Request Path**

| 参数 | 是否必选 | 类型 | 说明 |
| --- | --- | --- | --- |
| batchNo | 是 | String | 批次号。 |

## **请求示例**

```json
GET /api/merchantgrow/v1/merchantcoupon/couponbatch/querydetail/PV1202602041321081878538742919089024 HTTP/1.1
PayMercAuth: {"callerId":"10132120***","traceId":"202305151026422776499","time":1684117602555,"authId":"120291744647139***","headerSign":"u+H1Oe3fXV9mGCES89XA7tSjp8+TELYgG4bKyECwrVGwwExHtdWTnKc4WvEpfjLzpzKE2/+*********************cN9QrxXSeR8r6X46b7491N1jKg/lOG7eAFfwjEWJu5JyvY5KunSeE6DiKs=","bodySign":"yWDtXOBqDoItPgHmF57L6U5G7F/LhsILChu8YSpVV0HwRQCzdGAz53wDkCRLiAEVGDDu6E6KxPAHE0TIkTxH*********************sPj10iUIFeaszpiRT2aQDaqLGaxvta6J5UxIUmAp+wGdV/juGEvQ="}
Content-Type: application/json
```

## 响应参数

**Response Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |

**Response Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| resultCode | 是 | String | 返回码，"000000"表示成功，其他表示异常，请参见[错误码](payment-error-code-rest.md#公共错误码说明)。 |
| resultDesc | 是 | String | 结果描述。 |
| subCode | 否 | String | 业务错误码。 |
| subDesc | 否 | String | 业务错误描述信息 |
| sign | 是 | String | 签名信息，除“sign”字段以外的其他字段参与签名。 |
| signType | 否 | String | 签名类型。华为支付生成签名字符串使用的算法，当前为SM2算法。 |
| batchInfo | 否 | [CouponBatchDetailExtInfo](payment-model.md#couponbatchdetailextinfo) | 券批次查询响应。 |

## **响应示例**

```json
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
{
    "resultCode": "000000",
    "resultDesc": "Success.",
    "batchInfo": {
        "batchName": "国内机票XX元优惠券",
        "belongMerchant": "101631000030",
        "comment": "国内机票满XX元减XX元优惠券",
        "goodsName": "机票",
        "couponType": "NORMAL",
        "couponUseRule": {
            "useMethod": [
                "FASTAPP"
            ],
            "useAppId": [
                "change1",
                "change2"
            ],
            "exchangeCoupon": {
                "exchangePrice": 100,
                "transactionMinimum": 100
            },
            "availableTime": {
                "beginTime": "2026-02-04T17:50:12.000+0800",
                "endTime": "2026-05-28T17:50:12.000+0800",
                "dayAfterReceive": 10,
                "irregularyTime": []
            },
            "fixedNormalCoupon": {
                "discountAmount": 100,
                "transactionMinimum": 100
            },
            "discountCoupon": {
                "discountPercent": 86,
                "transactionMinimum": 100
            }
        },
        "couponSendRule": {
            "preventApiAbuse": false,
            "maxCoupons": 0,
            "sendEntrance": "PLATFORM_PUSH",
            "maxCouponsPerUser": 2,
            "naturalPersonLimit": false
        },
        "displayInfo": {
            "backgroundColor": "#483D8D",
            "couponTitle": "8月1日活动券修改2",
            "description": "xxxChange2",
            "jumpUrl": "https://xxxChange2",
            "nextJumpUrl": "https://xxxChange2",
            "diversionName": "xxxChange2",
            "merchantLogoUrl": "https://XXX/ab3OXLUtwRO.png",
            "merchantName": "XX公司"
        },
        "couponCodeMode": "MERCHANT_UPLOAD",
        "notifyConfig": {
            "notifyAppId": "wx23232232323Change3",
            "notifyUrl": "https://www.123.comChange3"
        },
        "batchStatus": "DEACTIVATED",
        "batchNo": "PV1202602041321081878538742919089***",
        "couponCodeCount": {
            "totalCount": 0,
            "availableCount": 0
        },
        "sendCountInfo": {
            "totalSendNum": 0,
            "totalSendAmount": 0,
            "todaySendNum": 0,
            "todaySendAmount": 0
        }
    }
}
```

## 错误码

**resultCode**非400000的错误码请看[公共错误码说明](payment-error-code-rest.md#公共错误码说明)。

| **返回码** | **错误码** | **错误描述** | **解决方案** |
| --- | --- | --- | --- |
| 400000 | UNKNOW\_ERROR | 服务暂不可用, 请稍后重试 | 稍候重试。 |
| 400000 | INVALID\_ARGUMENTS | 参数不合法 | 检查请求参数。 |
| 400000 | INVALID\_MERC\_NO | 无效商户号 | 检查入参商户号是否正确。 |
| 400000 | CHECK\_MERC\_STATUS | 商户状态校验失败 | 请检查商户状态是否正常。 |
| 400000 | INVALID\_APPID | AppId未和商户绑定 | 检查appId是否正确且已经绑定商户号。 |
| 400000 | INSUFFICIENT\_PERMISSION | 商户权限受限 | 在商户平台检查并配置该产品权限。 |
| 400000 | COUPON\_INCORRECT\_MERCHANT\_RELATION | 批次创建商户和归属商户无归属关系 | 请检查批次创建商户和归属商户是否有归属关系。 |
| 400000 | COUPON\_INVALID\_NOTIFY\_URL | 回调地址仅支持https协议地址 | 请检查回调地址是否为https协议地址。 |
