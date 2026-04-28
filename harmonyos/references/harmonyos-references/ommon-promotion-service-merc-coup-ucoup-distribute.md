---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ommon-promotion-service-merc-coup-ucoup-distribute
title: 发放优惠券
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 通用接口 > 运营工具 > 商家券 > 用户券 > 发放优惠券
category: harmonyos-references
scraped_at: 2026-04-28T08:18:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8a653f63f0b5f0ff11655b161c01ce94e0476f9c87a3fb8de451dd74928facc3
---

## 功能介绍

发放商家券，支持一个请求最大发放10张券，可以是一个批次下的多张，也可以是多个批次下的券，多个批次一起发放时一个批次发放失败，不影响其它批次的处理。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** https://petalpay-developer.cloud.huawei.com.cn/api/merchantgrow/v1/merchantcoupon/couponbatch/distribute
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
| requestNo | 是 | String | 请求号，由商户随机生成，不同请求要求唯一。最小长度为1，最大长度为64。  **说明**：用于保证幂等。对不同请求，requestNo的值要求不一样；对于相同请求，值要求一样，比如超时场景，可通过requestNo一样进行重试。 |
| appId | 是 | String | 当前调用接口商户号有绑定关系的AppID。最小长度为1，最大长度为32。 |
| openId | 是 | String | 用户的OpenId。最小长度为1，最大长度为256。 |
| coupons | 是 | List<[SendCouponInfo](payment-model.md#sendcouponinfo)> | 待发券的批次信息和券码。列表最小长度为1，最大长度为10。 |
| deviceInfo | 否 | [DeviceInfo](payment-model.md#deviceinfo) | 用户的设备信息，风控时使用，提升风控的准确度。 |

## **请求示例**

```
1. POST /api/merchantgrow/v1/merchantcoupon/couponbatch/create HTTP/1.1
2. PayMercAuth: {"callerId":"10132120***","traceId":"202305151026422776***","time":1684117602555,"authId":"120291744647139***","headerSign":"u+H1Oe3fXV9mGCES89XA7tSjp8+TELYgG4bKyECwrVGwwExHtdWTnKc4WvEpfjLzpzKE2/+K*********************/z0UcN9QrxXSeR8r6X46b7491N1jKg/lOG7eAFfwjEWJu5JyvY5KunSeE6DiKs=","bodySign":"yWDtXOBqDoItPgHmF57L6U5G7F/LhsILChu8YSpVV0HwRQCzdGAz53wDkCRLiAEVGDDu6E6KxPAHE0TIkTxH*********************iUIFeaszpiRT2aQDaqLGaxvta6J5UxIUmAp+wGdV/juGEvQ="}
3. Content-Type: application/json
4. {
5. "requestNo": "REQ000003",
6. "appId": "App00001",
7. "openId": "Open00001***",
8. "coupons": [
9. {
10. "batchNo": "PV1202602041321081878538742919089***",
11. "sendNum": 1
12. }
13. ],
14. "deviceInfo": {
15. "deviceId": "DEV002***",
16. "deviceIdType": "UDID",
17. "deviceModel": "MODEL00***",
18. "riskToken": "TOKEN0000231***",
19. "clientIp": "10.10.10.10",
20. "clientVersion": "V100100100",
21. "packageName": "com.huawei.coupon"
22. }
23. }
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
| distributeTime | 否 | String | 系统成功发券的时间，格式为yyyy-MM-dd'T'HH:mm:ss.SSSZ，yyyy-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.SSS表示时分秒，Z为对应的时区。例如：2023-03-28T17:50:12.000+0800表示，北京时间2023年3月28日 17点50分12秒。注意：要使用必须传准确的UTC时间。 |
| succResults | 否 | List<[BatchCoupons](payment-model.md#batchcoupons)> | 成功发券的结果信息。 |
| failResults | 否 | List<[FailResult](payment-model.md#failresult)> | 失败发券的结果信息。 |

## **响应示例**

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "000000",
5. "resultDesc": "Success.",
6. "sign":"MEQCIEIWzdpziRyTi8vhwWHFuDdxf********************CHljer0YAMabeCgTDG77e+2XJItvq/ZkIcCN5/B20pQ==",
7. "batchNo": "PV1202403211136181382014597367613***",
8. "openId": "OPEN_02032411234***",
9. "distributeTime": "2024-03-23T16:42:12.000+0800",
10. "succResults": [
11. {
12. "batchNo": "PV1202403211136181382014597367613***",
13. "couponCodes": ["C1"]
14. }
15. ]
16. }
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
| 400000 | COUPON\_BATCH\_NOT\_EXIST | 未找到待发券批次 | 确认券批次是否已创建，券批次号传递是否正确。 |
| 400000 | COUPON\_BATCH\_INVALID\_STATUS | 批次已过期或暂停 | 确认券批次状态或重新创建券批次。 |
| 400000 | COUPON\_NOT\_MATCH\_SEND\_RULE | 不满足发券条件 | 请确认用户是否满足发券条件（如用户已注销等）。 |
| 400000 | COUPON\_EXCEED\_SEND\_LIMIT\_PER\_REQUEST | 超过单个请求发放上限 | 请确认单个请求发放上限。 |
