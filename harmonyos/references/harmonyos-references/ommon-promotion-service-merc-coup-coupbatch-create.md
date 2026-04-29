---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ommon-promotion-service-merc-coup-coupbatch-create
title: 创建券批次
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 通用接口 > 运营工具 > 商家券 > 券批次 > 创建券批次
category: harmonyos-references
scraped_at: 2026-04-29T14:08:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4f0c9b5d550ddef82aa246aef617dc1abdff80680921e528ab2d329e8234c002
---

## 功能介绍

商户可以通过该接口创建商家券。创建成功后返回商家券批次号给到商户，商户可调用发券接口发放该批次商家券。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** https://petalpay-developer.cloud.huawei.com.cn/api/merchantgrow/v1/merchantcoupon/couponbatch/create
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
| requestNo | 是 | String | 商户请求单号。由商户随机生成，不同请求要求唯一。最小长度为1，最大长度为64。  **说明**：用于保证幂等。对不同请求，requestNo的值要求不一样。对于相同请求，值要求一样，比如超时场景，可通过requestNo一样进行重试。 |
| batchName | 是 | String | 批次名称。最小长度为1，最大长度为64。 |
| belongMerchant | 是 | String | 批次归属商户号。最小长度为1，最大长度为64。  **说明**：  - 普通直连模式，该参数为直连商户号。  - 服务商模式，该参数为特约商户号。  - 平台商户模式，该参数为平台子商户号。 |
| comment | 否 | String | 批次描述信息。最大长度为64。 |
| goodsName | 是 | String | 适用商品范围，用来描述批次在哪些商品可用。最小长度为1，最大长度为64。 |
| couponType | 是 | String | 优惠券类型，支持以下枚举：  - NORMAL：满减券  - DISCOUNT：折扣券  - EXCHANGE：换购券 |
| couponUseRule | 是 | [CouponUseRule](payment-model.md#couponuserule) | 券核销相关规则。 |
| couponSendRule | 是 | [CouponSendRule](payment-model.md#couponsendrule) | 券分发规则。 |
| displayInfo | 是 | [CouponDisplayInfo](payment-model.md#coupondisplayinfo) | 优惠券展示信息。 |
| couponCodeMode | 否 | String | 券码模式，支持以下枚举：  - MERCHANT\_UPLOAD：导入Code模式，需要[上传券预存Code](ommon-promotion-service-merc-coup-coupbatch-upload.md)。发券时，随机选择一个券码。  - HWPAY\_MODE：自动分配券code，商户不需要预存code  - MERCHANT\_API：调用发券接口时需指定券code |
| notifyConfig | 否 | [NotifyConfig](payment-model.md#notifyconfig) | 批次操作事件通知商户的appId和Url。当sendEntrance为华为平台发券时，该参数必传。 |

## 请求示例

```
1. POST /api/merchantgrow/v1/merchantcoupon/couponbatch/create HTTP/1.1
2. Content-Type: application/json;charset=UTF-8
3. PayMercAuth: {"callerId":"10132120***","traceId":"202305151026422776499","time":1684117602555,"authId":"120291744647139***","headerSign":"u+H1Oe3fXV9mGCES89XA7tSjp8+TELYgG4bKyECwrVGwwExHtdWTnKc4WvEpfjLzpzKE2/+*********************0UcN9QrxXSeR8r6X46b7491N1jKg/lOG7eAFfwjEWJu5JyvY5KunSeE6DiKs=","bodySign":"yWDtXOBqDoItPgHmF57L6U5G7F/LhsILChu8YSpVV0HwRQCzdGAz53wDkCRLiAEVGDDu6E6KxPAHE0TIkT*********************Pj10iUIFeaszpiRT2aQDaqLGaxvta6J5UxIUmAp+wGdV/juGEvQ="}
4. Content-Type: application/json
5. {
6. "requestNo": "REQ00203141232***",
7. "batchName": "国内机票XX元优惠券",
8. "belongMerchant": "101631000***",
9. "comment": "国内机票满XX元减XX元优惠券",
10. "goodsName": "机票",
11. "couponType": "NORMAL",
12. "couponUseRule": {
13. "availableTime": {
14. "beginTime": "2026-02-04T17:50:12.000+0800",
15. "dayAfterReceive": 10,
16. "endTime": "2026-05-28T17:50:12.000+0800"
17. },
18. "fixedNormalCoupon": {
19. "discountAmount": 100,
20. "transactionMinimum": 100
21. },
22. "discountCoupon": {
23. "discountPercent": 86,
24. "transactionMinimum": 100
25. },
26. "exchangeCoupon": {
27. "exchangePrice": 100,
28. "transactionMinimum": 100
29. },
30. "useAppId": [
31. "appid1"
32. ],
33. "useMethod": [
34. "FASTAPP"
35. ]
36. },
37. "couponSendRule": {
38. "maxCoupons": 0,
39. "maxCouponsPerUser": 2,
40. "naturalPersonLimit": false,
41. "preventApiAbuse": false,
42. "sendEntrance": "PLATFORM_PUSH"
43. },
44. "displayInfo": {
45. "backgroundColor": "#DF674F",
46. "couponTitle": "XX元满减券",
47. "description": "XX元满减券",
48. "diversionName": "XX元满减券",
49. "nextJumpUrl": "https://hoas.drcn.agconnect.link/abcd",
50. "merchantLogoUrl": "https://XXX/ab3OXLUtwRO.png",
51. "merchantName": "XX公司"
52. },
53. "couponCodeMode": "MERCHANT_UPLOAD",
54. "notifyConfig": {
55. "notifyAppId": "appid1",
56. "notifyUrl": "https://xxx/callback/merc/coupon"
57. }
58. }
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
| batchNo | 是 | String | 批次号。 |
| createTime | 是 | String | 创建时间（UTC时间），格式为yyyy-MM-dd'T'HH:mm:ss.SSSZ，yyyy-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.SSS表示时分秒，Z为对应的时区。例如：2023-03-28T17:50:12.000+0800表示，北京时间2023年3月28日 17点50分12秒。 |

## 响应示例

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "000000",
5. "resultDesc": "Success",
6. "sign": "MEQCIEIWzdpziRyTi8vhwWHFuDdx********************CHljer0YAMabeCgTDG77e+2XJItvq/ZkIcCN5/B20pQ==",
7. "batchNo": "PV1202602041321081878538742919089***",
8. "createTime": "2024-03-28T17:50:12.000+0800"
9. }
```

## 错误码

**resultCode**非400000的错误码请查看[公共错误码说明](payment-error-code-rest.md#公共错误码说明)。

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
