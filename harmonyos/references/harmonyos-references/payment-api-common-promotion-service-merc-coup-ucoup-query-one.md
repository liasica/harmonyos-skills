---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-promotion-service-merc-coup-ucoup-query-one
title: 查询用户单张优惠券详情
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 通用接口 > 运营工具 > 商家券 > 用户券 > 查询用户单张优惠券详情
category: harmonyos-references
scraped_at: 2026-09-02T14:53:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2d4568de19e8fd187138d5df3c5e0882cab21d4dec638a6249ce1ad35f218095
---

## 功能介绍

商户可通过该接口查询用户卡包中某一张商家券的详情信息。

## 接口原型

* **承载协议：** HTTPS GET
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** https://petalpay-developer.cloud.huawei.com.cn/api/merchantgrow/v1/merchantcoupon/coupondetail/query/appid/{appId}/user/{openId}/batchno/{batchNo}/coupon/{couponCode}
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
| appId | 是 | String | 与当前调用接口商户号有绑定关系的AppID。最小长度为1，最大长度为32。 |
| openId | 是 | String | 用户OpenID。最小长度为1，最大长度为256。 |
| batchNo | 是 | String | 批次号。最小长度为1，最大长度为40。 |
| couponCode | 是 | String | 待查询的券Code。最小长度为1，最大长度为32。 |

## **请求示例**

```json
GET /api/merchantgrow/v1/merchantcoupon/coupondetail/query/appid/{appId}/user/{openId}/batchno/{batchNo}/coupon/{couponCode}  HTTP/1.1
PayMercAuth: {"callerId":"10132120***","traceId":"202305151026422776499","time":1684117602555,"authId":"120291744647139***","headerSign":"u+H1Oe3fXV9mGCES89XA7tSjp8+TELYgG4bKyECwrVGwwExHtdWTnKc4WvEpfjLzpzKE2/+KYaq1j*********************XSeR8r6X46b7491N1jKg/lOG7eAFfwjEWJu5JyvY5KunSeE6DiKs=","bodySign":"yWDtXOBqDoItPgHmF57L6U5G7F/LhsILChu8YSpVV0HwRQCzdGAz53wDkCRLiAEVGDDu6E6KxPAHE0TIkTxHMcUWx*********************szpiRT2aQDaqLGaxvta6J5UxIUmAp+wGdV/juGEvQ="}
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
| subDesc | 否 | String | 业务错误描述信息。 |
| sign | 是 | String | 签名信息，除“sign”字段以外的其他字段参与签名。 |
| signType | 否 | String | 签名类型。华为支付生成签名字符串使用的算法，当前为SM2算法。 |
| certNo | 否 | String | 签名所使用的证书编号。 |
| couponInfo | 否 | [CouponInfo](payment-model.md#couponinfo) | 给用户呈现的优惠券信息。 |

## **响应示例**

```json
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
{
  "couponInfo": {
    "couponCode": "AADFWERWEQRWER",
    "batchNo": "PV1202404110850271397151413900974***",
    "batchName": "国庆活动券14",
    "belongMerchant": "101631000***",
    "comment": "活动使用",
    "goodsName": "商品1,商品2,商品3",
    "couponType": "EXCHANGE",
    "couponState": "SENDED",
    "displayInfo": {
      "backgroundColor": "#483D8B",
      "couponTitle": "国庆活动券14",
      "description": "国庆活动",
      "jumpUrl": "https://www.232.com",
      "diversionName": "example-phoneName",
      "merchantLogoUrl": "https://xxxxxx",
      "merchantName": "滴答出行2"
    },
    "couponUseRule": {
      "useMethod": [
        "FASTAPP"
      ],
      "useAppId": [
        "change1"
      ],
      "exchangeCoupon": {
        "exchangePrice": 100,
        "transactionMinimum": 100
      },
      "availableTime": {
        "beginTime": "2024-03-28T09:10:00.000+0800",
        "endTime": "2024-10-18T20:10:00.000+0800",
        "dayAfterReceive": 3,
        "availableWeek": {
          "weekDay": [
            1
          ],
          "dayTime": [
            {
              "beginTime": 3600,
              "endTime": 86394
            }
          ]
        },
        "irregularyTime": [
          {
            "beginTime": "2024-03-28T08:10:00.000+0800",
            "endTime": "2024-10-18T14:10:00.000+0800"
          },
          {
            "beginTime": "2024-03-29T08:10:00.000+0800",
            "endTime": "2024-10-19T01:10:00.000+0800"
          }
        ]
      },
      "fixedNormalCoupon": {
        "discountAmount": 5,
        "transactionMinimum": 100
      },
      "discountCoupon": {
        "discountPercent": 88,
        "transactionMinimum": 100
      }
    },
    "availableStartTime": "2024-04-11T17:23:38.900+0800",
    "expireTime": "2024-04-13T23:59:59.999+0800",
    "receiveTime": "2024-04-11T17:23:38.866+0800",
    "distributeRequestNo": "czl00120240411112***"
  },
  "resultCode": "000000",
  "sign": "MEQCIFWeGBD8KMhkqtNso2m72rKQKzdU********************rWbBQGKt8LWnqvEappqvZ7TxEkZPqRyhBNXA==",
  "resultDesc": "Success."
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
| 400000 | CUST\_NOT\_EXIST | 用户不存在或已销户 | 请确认操作的华为账号状态是否正常或已销户。 |
| 400000 | COUPON\_NOT\_EXIST | 未找到相关优惠券 | 查询用户优惠券信息，确认是否存在优惠券。 |
