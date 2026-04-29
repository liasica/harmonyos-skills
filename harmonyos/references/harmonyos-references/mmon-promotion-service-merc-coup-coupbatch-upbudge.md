---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/mmon-promotion-service-merc-coup-coupbatch-upbudge
title: 修改券批次预算
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 通用接口 > 运营工具 > 商家券 > 券批次 > 修改券批次预算
category: harmonyos-references
scraped_at: 2026-04-29T14:08:55+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:fe00e693c461be9135f6addb94e475d771db2045c23e7875b3a209bbd1af4fbf
---

## 功能介绍

商户可以通过该接口修改批次单天发放上限数量或者批次最大发放数量。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** https://petalpay-developer.cloud.huawei.com.cn/api/merchantgrow/v1/merchantcoupon/couponbatch/update/budget
* **数据格式：**

  请求消息：Content-Type: application/json

  响应消息：Content-Type: application/json

## 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |
| PayMercAuth | 是 | String | 取值为：[PayMercAuth](payment-model.md#paymercauth)的JSON字符串 |

**Request Body**

| 参数 | 是否必选 | 类型 | 说明 |
| --- | --- | --- | --- |
| requestNo | 是 | String | 请求号，由商户随机生成，不同请求要求唯一。最小长度为1，最大长度为64。  **说明**：用于保证幂等。对不同请求，requestNo的值要求不一样。对于相同请求，值要求一样，比如超时场景，可通过requestNo一样进行重试。 |
| batchNo | 是 | String | 批次号。 |
| targetMaxCoupons | 否 | Integer | 目标批次最大发放券个数。  **说明**：当couponCode = MERCHANT\_UPLOAD时，该值需要和导入的券Code数量保持一致。 |
| currentMaxCoupons | 否 | Integer | 当前批次最大发放券个数。 |
| targetMaxCouponsByDay | 否 | Integer | 目标单天发放券上限个数。 |
| currentMaxCouponsByDay | 否 | Integer | 当前单天发放券上限个数。 |

说明

以下几种情况会报错：

* currentMaxCoupons大于等于targetMaxCoupons。
* currentMaxCoupons、targetMaxCoupons、currentMaxCouponsByCoupons、targetMaxCouponsByCoupons都不存在。
* currentMaxCoupons、targetMaxCoupons一个为空，一个有值。
* currentMaxCouponsByDay、targetMaxCouponsByDay一个为空，一个有值。

## **请求示例**

```
1. POST /api/merchantgrow/v1/merchantcoupon/couponbatch/update/budget HTTP/1.1
2. PayMercAuth: {"callerId":"10132120***","traceId":"202305151026422776499","time":1684117602555,"authId":"120291744647139***","headerSign":"u+H1Oe3fXV9mGCES89XA7tSjp8+TELYgG4bKyECwrVGwwExHtdWTnKc4WvEpfjLzpzKE2/+KYaq1*********************8r6X46b7491N1jKg/lOG7eAFfwjEWJu5JyvY5KunSeE6DiKs=","bodySign":"yWDtXOBqDoItPgHmF57L6U5G7F/LhsILChu8YSpVV0HwRQCzdGAz53wDkCRLiAEVGDD*********************Pj10iUIFeaszpiRT2aQDaqLGaxvta6J5UxIUmAp+wGdV/juGEvQ="}
3. Content-Type: application/json
4. {
5. "batchNo": "PV1202602041321081878538742919089***",
6. "requestNo": "30000***",
7. "targetMaxCoupons": 3,
8. "currentMaxCoupons": 0
9. }
```

## 响应参数

**Response Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |

**Response Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| resultCode | 是 | String | 返回码，"000000"表示成功，其他表示见错误码。 |
| resultDesc | 是 | String | 结果描述。 |
| subCode | 否 | String | 业务错误码。 |
| subDesc | 否 | String | 业务错误描述信息。 |
| sign | 是 | String | 签名信息，除“sign”字段以外的其他字段参与签名。 |
| signType | 否 | String | 签名类型。华为支付生成签名字符串使用的算法，当前为SM2算法。 |
| certNo | 否 | String | 签名所使用的证书编号。 |
| maxCoupons | 是 | Integer | 更新后的批次最大发放个数。 |
| maxCouponsByDay | 否 | Integer | 更新后的单天发放上限个数。 |

## **响应示例**

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "000000",
5. "resultDesc": "Success.",
6. "sign":"MEQCIEIWzdpziRyTi8vhwWHFuDdxf********************jer0YAMabeCgTDG77e+2XJItvq/ZkIcCN5/B20pQ==",
7. "maxCoupons": 22,
8. "maxCouponsByDay": 16
9. }
```

## 错误码

**resultCode**非400000的错误码请看[公共错误码说明](payment-error-code-rest.md#公共错误码说明)。

| **返回码** | **错误码** | **错误描述** | **解决方案** |
| --- | --- | --- | --- |
| 400000 | UNKNOW\_ERROR | 服务暂不可用, 请稍后重试 | 稍候重试。 |
| 400000 | INVALID\_ARGUMENTS | 参数不合法 | 检查请求参数。 |
| 400000 | INVALID\_MERC\_NO | 无效商户号 | 检查入参商户号是否正确。 |
| 400000 | CHECK\_MERC\_STATUS | 商户状态校验失败 | 请检查商户状态是否正常。 |
| 400000 | COUPON\_BATCH\_NOT\_EXIST | 未找到待发券批次 | 请检查批次创建商户和归属商户是否有归属关系。 |
| 400000 | COUPON\_BATCH\_INVALID\_STATUS | 批次已过期或暂停 | 请检查回调地址是否为https协议地址。 |
| 400000 | COUPON\_BATCH\_UPDATING | 批次正在更新中，无法处理新的更新请求 | 确认批次更新状态，等待批次更新完成。 |
