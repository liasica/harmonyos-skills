---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/common-promotion-service-merc-coup-coupbatch-query
title: 查询券批次详情
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 通用接口 > 运营工具 > 商家券 > 券批次 > 查询券批次详情
category: harmonyos-references
scraped_at: 2026-04-29T14:08:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c30fb857b929deef11c3207bd1642db6591952498fd2bf4cc435fa249993b66c
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

```
1. GET /api/merchantgrow/v1/merchantcoupon/couponbatch/querydetail/PV1202602041321081878538742919089024 HTTP/1.1
2. PayMercAuth: {"callerId":"10132120***","traceId":"202305151026422776499","time":1684117602555,"authId":"120291744647139***","headerSign":"u+H1Oe3fXV9mGCES89XA7tSjp8+TELYgG4bKyECwrVGwwExHtdWTnKc4WvEpfjLzpzKE2/+*********************cN9QrxXSeR8r6X46b7491N1jKg/lOG7eAFfwjEWJu5JyvY5KunSeE6DiKs=","bodySign":"yWDtXOBqDoItPgHmF57L6U5G7F/LhsILChu8YSpVV0HwRQCzdGAz53wDkCRLiAEVGDDu6E6KxPAHE0TIkTxH*********************sPj10iUIFeaszpiRT2aQDaqLGaxvta6J5UxIUmAp+wGdV/juGEvQ="}
3. Content-Type: application/json
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
| subDesc | 否 | String | 业务错误描述信息 |
| sign | 是 | String | 签名信息，除“sign”字段以外的其他字段参与签名。 |
| signType | 否 | String | 签名类型。华为支付生成签名字符串使用的算法，当前为SM2算法。 |
| batchInfo | 否 | [CouponBatchDetailExtInfo](payment-model.md#couponbatchdetailextinfo) | 券批次查询响应。 |

## **响应示例**

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "000000",
5. "resultDesc": "Success.",
6. "batchInfo": {
7. "batchName": "国内机票XX元优惠券",
8. "belongMerchant": "101631000030",
9. "comment": "国内机票满XX元减XX元优惠券",
10. "goodsName": "机票",
11. "couponType": "NORMAL",
12. "couponUseRule": {
13. "useMethod": [
14. "FASTAPP"
15. ],
16. "useAppId": [
17. "change1",
18. "change2"
19. ],
20. "exchangeCoupon": {
21. "exchangePrice": 100,
22. "transactionMinimum": 100
23. },
24. "availableTime": {
25. "beginTime": "2026-02-04T17:50:12.000+0800",
26. "endTime": "2026-05-28T17:50:12.000+0800",
27. "dayAfterReceive": 10,
28. "irregularyTime": []
29. },
30. "fixedNormalCoupon": {
31. "discountAmount": 100,
32. "transactionMinimum": 100
33. },
34. "discountCoupon": {
35. "discountPercent": 86,
36. "transactionMinimum": 100
37. }
38. },
39. "couponSendRule": {
40. "preventApiAbuse": false,
41. "maxCoupons": 0,
42. "sendEntrance": "PLATFORM_PUSH",
43. "maxCouponsPerUser": 2,
44. "naturalPersonLimit": false
45. },
46. "displayInfo": {
47. "backgroundColor": "#483D8D",
48. "couponTitle": "8月1日活动券修改2",
49. "description": "xxxChange2",
50. "jumpUrl": "https://xxxChange2",
51. "nextJumpUrl": "https://xxxChange2",
52. "diversionName": "xxxChange2",
53. "merchantLogoUrl": "https://XXX/ab3OXLUtwRO.png",
54. "merchantName": "XX公司"
55. },
56. "couponCodeMode": "MERCHANT_UPLOAD",
57. "notifyConfig": {
58. "notifyAppId": "wx23232232323Change3",
59. "notifyUrl": "https://www.123.comChange3"
60. },
61. "batchStatus": "DEACTIVATED",
62. "batchNo": "PV1202602041321081878538742919089***",
63. "couponCodeCount": {
64. "totalCount": 0,
65. "availableCount": 0
66. },
67. "sendCountInfo": {
68. "totalSendNum": 0,
69. "totalSendAmount": 0,
70. "todaySendNum": 0,
71. "todaySendAmount": 0
72. }
73. }
74. }
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
