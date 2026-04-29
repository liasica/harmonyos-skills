---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ommon-promotion-service-merc-coup-coupbatch-update
title: 修改券批次信息
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 通用接口 > 运营工具 > 商家券 > 券批次 > 修改券批次信息
category: harmonyos-references
scraped_at: 2026-04-29T14:08:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c57cc711095bdeeba7462b3ec8d5933208aff6028faffbd771e4c791629ab1fa
---

## 功能介绍

商户可以通过该接口修改商家券基本信息。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** https://petalpay-developer.cloud.huawei.com.cn/api/merchantgrow/v1/merchantcoupon/couponbatch/update/baseinfo
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
| batchNo | 是 | String | 批次号，批次创建成功后返回。 |
| comment | 否 | String | 批次备注信息，用于自定义信息。字数上限为64个，一个中文汉字/英文字母/数字均占用一个字数。 |
| goodsName | 否 | String | 适用商品范围，用来描述批次在哪些商品可用，会显示在卡包中。字数上限为64个，一个中文汉字/英文字母/数字均占用一个字数。 |
| couponUseRule | 否 | [CouponUseRuleMod](payment-model.md#couponuserulemod) | 券核销相关规则。 |
| couponSendRule | 否 | [CouponSendRuleMod](payment-model.md#couponsendrulemod) | 券分发规则。 |
| displayInfo | 否 | [CouponDisplayInfoMod](payment-model.md#coupondisplayinfomod) | 优惠券展示信息。 |
| notifyConfig | 否 | [NotifyConfig](payment-model.md#notifyconfig) | 批次操作事件通知商户的appId和Url。  **说明**：华为平台（负一屏）发券时，该参数必传。 |

## 请求示例

```
1. POST /api/merchantgrow/v1/merchantcoupon/couponbatch/update/baseinfo HTTP/1.1
2. PayMercAuth: {"callerId":"10132120***","traceId":"202305151026422776499","time":1684117602555,"authId":"120291744647139***","headerSign":"u+H1Oe3fXV9mGCES89XA7tSjp8+TELYgG4bKyECwrVGwwExHtdWTnKc4WvEpfjLzpzKE2/+KYaq1*********************XSeR8r6X46b7491N1jKg/lOG7eAFfwjEWJu5JyvY5KunSeE6DiKs=","bodySign":"yWDtXOBqDoItPgHmF57L6U5G7F/LhsILChu8YSpVV0HwRQCzdGAz53wDkCRLiAEVGDDu6E6KxPAHE0TIkTxHMcUWx7N64*********************UIFeaszpiRT2aQDaqLGaxvta6J5UxIUmAp+wGdV/juGEvQ="}
3. Content-Type: application/json
4. {
5. "batchNo": "PV1202602041321081878538742919089***",
6. "requestNo": "10102320***",
7. "comment": "国内机票满XX元减XX元优惠券",
8. "goodsName": "机票",
9. "couponUseRule": {
10. "useMethod": [
11. "FASTAPP"
12. ],
13. "useAppId": [
14. "change1",
15. "change2"
16. ]
17. },
18. "couponSendRule": {
19. "preventApiAbuse": false
20. },
21. "displayInfo": {
22. "backgroundColor": "#483D8D",
23. "couponTitle": "8月1日活动券修改2",
24. "description": "xxxChange2",
25. "jumpUrl": "https://xxxChange2",
26. "nextJumpUrl": "https://xxxChange2",
27. "diversionName": "xxxChange2"
28. },
29. "notifyConfig": {
30. "notifyAppId": "wx23232232323Change3",
31. "notifyUrl": "https://www.123.comChange3"
32. }
33. }
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

## 响应示例

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "000000",
5. "resultDesc": "Success.",
6. "sign":"MEQCIEIWzdpziRyTi8vhwWHFuDdxfsiw********************jer0YAMabeCgTDG77e+2XJItvq/ZkIcCN5/B20pQ=="
7. }
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
