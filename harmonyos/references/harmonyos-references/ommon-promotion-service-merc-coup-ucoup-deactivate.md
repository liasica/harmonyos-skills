---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ommon-promotion-service-merc-coup-ucoup-deactivate
title: 使券失效
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 通用接口 > 运营工具 > 商家券 > 用户券 > 使券失效
category: harmonyos-references
scraped_at: 2026-04-28T08:18:17+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:5675b18f183112b1b42729bb57cdf196b7b186fb218222d6b9b263fd00fa5eac
---

## 功能介绍

失效一张券，券失效后无法再被核销。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** https://petalpay-developer.cloud.huawei.com.cn/api/merchantgrow/v1/merchantcoupon/coupon/deactivate
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
| requestNo | 是 | String | 请求号，由商户随机生成，不同请求要求唯一。最小长度为1，最大长度为64。  说明：用于保证幂等。对不同请求，requestNo的值要求不一样。对于相同请求，值要求一样，比如超时场景，可通过requestNo一样进行重试。 |
| couponCode | 是 | String | 券号。最小长度为1，最大长度为32。 |
| batchNo | 是 | String | 券归属批次号。最小长度为1，最大长度为40。 |
| deactivateReason | 是 | String | 商户失效券的原因。最小长度为1，最大长度为64。 |

## **请求示例**

```
1. POST /api/merchantgrow/v1/merchantcoupon/coupon/deactivate HTTP/1.1
2. PayMercAuth: {"callerId":"10132120***","traceId":"202305151026422776499","time":1684117602555,"authId":"120291744647139***","headerSign":"u+H1Oe3fXV9mGCES89XA7tSjp8+TELYgG4bKyECwrVGwwExHtdWTnKc4WvEpfjLzpzKE2/+KYaq1jD*********************cN9QrxXSeR8r6X46b7491N1jKg/lOG7eAFfwjEWJu5JyvY5KunSeE6DiKs=","bodySign":"yWDtXOBqDoItPgHmF57L6U5G7F/LhsILChu8YSpVV0HwRQCzdGAz53wDkCRLiAEVGDDu6E6KxPAHE0TIkTx*********************j10iUIFeaszpiRT2aQDaqLGaxvta6J5UxIUmAp+wGdV/juGEvQ="}
3. Content-Type: application/json
4. {
5. "requestNo": "REQ000032",
6. "batchNo": "PV1202602051023491879174270605609***",
7. "couponCode": "C2",
8. "deactivateReason":"******XXX"
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
| deactivateTime | 是 | String | 系统券成功失效的时间，格式为yyyy-MM-dd'T'HH:mm:ss.SSSZ，yyyy-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.SSS表示时分秒，Z为对应的时区。例如：2023-03-28T17:50:12.000+0800表示，北京时间2023年3月28日 17点50分12秒。注意：要使用必须传准确的UTC时间。 |

## **响应示例**

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "000000",
5. "resultDesc": "Success.",
6. "sign":"MEQCIEIWzdpziRyTi8vhwWHFuDdxfsi********************YAMabeCgTDG77e+2XJItvq/ZkIcCN5/B20pQ==",
7. "deactivateTime": "2024-03-23T16:42:12.000+0800"
8. }
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
| 400000 | COUPON\_NOT\_EXIST | 未找到相关优惠券 | 查询用户优惠券信息，确认是否存在优惠券。 |
| 400000 | COUPON\_INVALID\_STATUS | 优惠券状态不正确 | 查询用户优惠券状态，确认是否正常。 |
