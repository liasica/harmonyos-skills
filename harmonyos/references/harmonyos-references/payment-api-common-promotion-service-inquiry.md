---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-promotion-service-inquiry
title: 查询用户可用平台券
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 通用接口 > 运营工具 > 查询用户可用平台券
category: harmonyos-references
scraped_at: 2026-04-28T08:18:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e7897af49257430e55a94aa7d9a42d4d6bb89f0afdc137be63472294026c0462
---

## 功能介绍

商户通过自定义使用券的匹配条件（如订单金额、AppID等），查询用户满足使用条件的平台券信息。

## 接口原型

## 接口原型

* **载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** https://petalpay-developer.cloud.huawei.com.cn/api/merchantgrow/v1/ecocoupon/coupon/query/usable
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
| appId | 是 | String | 当前调用接口商户号有绑定关系的AppID。 |
| openId | 是 | String | 用户的OpenId。 |
| sceneInfos | 是 | List<[RequestSceneInfo](payment-model.md#requestsceneinfo)> | 匹配券的场景条件列表，要求列表内的sceneId唯一。如果场景信息匹配上券，对应的sceneId会在响应参数matchedCoupon返回。 |

## 请求示例

以下请求示例中，匹配券的场景有2个，场景id（sceneId）分别为uuid1和uuid2。对于响应，如果场景id对应传递的sceneParams参数能匹配上券，券号信息（matchedCoupon）则会返回对应券号，否则不返回。

```
1. POST /api/merchantgrow/v1/ecocoupon/coupon/query/usable HTTP/1.1
2. PayMercAuth: {"callerId":"10132120***","traceId":"202305151026422776499","time":1684117602555,"authId":"120291744647139***","headerSign":"u+H1Oe3fXV9mGCES89XA7tSjp8+TELYgG4bKyECwrVGwwExHtdWTnKc4WvEpfjLzpzKE2/+K*********************/z0UcN9QrxXSeR8r6X46b7491N1jKg/lOG7eAFfwjEWJu5JyvY5KunSeE6DiKs=","bodySign":"yWDtXOBqDoItPgHmF57L6U5G7F/LhsILChu8YSpVV0HwRQCzdGAz53wDkCRLiAEVGDDu6E6KxPAHE0TIkTxH*********************iUIFeaszpiRT2aQDaqLGaxvta6J5UxIUmAp+wGdV/juGEvQ="}
3. Content-Type: application/json
4. {
5. "appId": "App00001",
6. "openId": "Open00001232",
7. "sceneInfos": [
8. {
9. "sceneId": "uuid1",
10. "sceneParams": {
11. "bundleName": "com.atomicservice.abcd",
12. "bundleType": "ATOMIC_SERVICE",
13. "deviceType": "phone",
14. "osType": "HMOS",
15. "productModel": "ALN-AL00",
16. "tradeOrderAmount": 200
17. }
18. },
19. {
20. "sceneId": "uuid2",
21. "sceneParams": {
22. "bundleName": "com.atomicservice.abcd",
23. "bundleType": "ATOMIC_SERVICE",
24. "deviceType": "phone",
25. "osType": "HMOS",
26. "productModel": "ALN-AL00",
27. "tradeOrderAmount": 300
28. }
29. }
30. ]
31. }
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
| coupons | 否 | List<[ServCouponInfo](payment-model.md#servcouponinfo)> | 场景条件匹配上的平台券信息列表。 |
| matchedCoupon | 否 | List<[SceneMatchedCouponNos](payment-model.md#scenematchedcouponnos)> | 各场景条件匹配到的券号信息。 |

## 响应示例

以下响应示例中，只有场景id（sceneId）为uuid1对应传递的sceneParams参数能匹配上券，sceneId为uuid2的场景没有匹配上任何券，所以券号信息（matchedCoupon）只返回sceneId为uuid1所匹配的券号。

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "000000",
5. "resultDesc": "Success.",
6. "sign":"MEQCIEIWzdpziRyTi8vhwWHFuDdxf********************CHljer0YAMabeCgTDG77e+2XJItvq/ZkIcCN5/B20pQ==",
7. "coupons": [
8. {
9. "couponCode": "couponCode001",
10. "batchNo": "batchNo001",
11. "couponType": "NORMAL",
12. "effectiveTime": 1753173740350,
13. "expireTime": 1753260140350,
14. "amount": 500,
15. "displayInfo": {
16. "couponDesc": "优惠券满20减5元",
17. "logoUrl": "https://www.logo.com/logourl"
18. }
19. }
20. ],
21. "matchedCoupon":[
22. {
23. "sceneId": "uuid1",
24. "couponNos":[
25. "couponCode001"
26. ]
27. }
28. ]
29. }
```

## 错误码

**resultCode**非400000的错误码请看[公共错误码说明](payment-error-code-rest.md#公共错误码说明)

| **返回码** | **错误码** | **错误描述** | **解决方案** |
| --- | --- | --- | --- |
| 400000 | UNKNOW\_ERROR | 服务暂不可用, 请稍后重试 | 稍后重试。 |
| 400000 | INVALID\_ARGUMENTS | 参数不合法 | 检查请求参数。 |
| 400000 | INVALID\_MERC\_NO | 无效商户号 | 检查入参商户号是否正确。 |
| 400000 | CHECK\_MERC\_STATUS | 商户状态校验失败 | 请检查商户状态是否正常。 |
| 400000 | INVALID\_APPID | AppId未和商户绑定 | 检查appId是否正确且已经绑定商户号。 |
| 400000 | INSUFFICIENT\_PERMISSION | 商户权限受限 | 在商户平台检查并配置该产品权限。 |
| 400000 | CUST\_NOT\_EXIST | 用户不存在或已销户 | 请确认操作的华为账号状态是否正常或已销户。 |
