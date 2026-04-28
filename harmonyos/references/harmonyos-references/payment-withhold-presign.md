---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-withhold-presign
title: 预签约
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 直连商户 > 签约代扣 > 预签约
category: harmonyos-references
scraped_at: 2026-04-28T08:17:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:04ae4cbb3aaa31819390ca20bb34885a9b59040ad0a56ada468caeb8c38c8814
---

## 功能介绍

开发者可以调用此接口获取预签约号（preSignNo）。

## 场景描述

接入Payment Kit的签约能力时，开发者需要先调用该接口获取到preSignNo，然后将preSignNo传递给客户端调用签约接口拉起华为支付签约收银台。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** https://petalpay-developer.cloud.huawei.com.cn/api/v2/contract/presign/app

  说明：元服务预签约接口请使用<https://petalpay-developer.cloud.huawei.com.cn/api/v2/contract/presign/fa>
* **数据格式：**

  请求消息：Content-Type: application/json; charset=UTF-8

  响应消息：Content-Type: application/json; charset=UTF-8

## 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |
| PayMercAuth | 是 | String | 取值为：[PayMercAuth](payment-model.md#paymercauth)的JSON字符串 |

**Request Body**

| 参数 | 是否必选 | 类型 | 说明 |
| --- | --- | --- | --- |
| appId | 是 | String | 应用ID。获取方式请参见[AppID管理及关联](../pay-docs/hwzf-appidguanli-0000001757041165.md)。 |
| planId | 是 | String | 协议模板ID。该模板ID是商户在向华为支付[提交代扣权限申请](../harmonyos-guides/payment-password-free-pay-overview.md)时由华为支付生成。 |
| mercContractCode | 是 | String | 商户签约协议号。开发者请求签约时传入的签约协议号，商户侧自己生成，商户需保证字段唯一性。最大长度64。 |
| mercNo | 是 | String | 商户号。 |
| callbackUrl | 是 | String | 回调通知地址，通知URL必须为外网环境可直接访问的URL，要求为https地址。具体要求参考[通知回调接口说明](payment-rest-overview.md#通知回调接口说明)。最大长度为512。 |
| expireTime | 否 | String | 交易过期时间。此时间必须为准确的UTC时间。  格式要求："yyyy-MM-dd'T'HH:mm:ss.SSSZ" 。  **说明：**  - 下单过期时间，不传默认2个小时，如果传递则最小值无限制，最大180天，超过180天系统会报错。  - 传已过时间可能会导致订单因过期、超时等原因异常关闭。  - 开发者可以参考[获取对应的UTC过期时间示例](payment-appendix.md#获取对应的utc过期时间示例)来获取对应的UTC过期时间。 |
| payer | 否 | [PayerIn](payment-model.md#payerin) | 支付者信息。 |

## 请求示例

```
1. POST /api/v2/contract/presign/app HTTP/1.1
2. Content-Type: application/json;charset=UTF-8
3. PayMercAuth: {"callerId":"10132120***","traceId":"202305151026422776499","time":1684117602555,"authId":"120291744647139***","headerSign":"u+H1Oe3fXV9mGCES89XA7tSjp8+********************lOG7eAFfwjEWJu5JyvY5KunSeE6DiKs=","bodySign":"yWDtXOBqDoItPgHmF57L6U5G7F/*******************asPj10iUIFeaszpiRT2aQDaqLGaxvta6J5UxIUmAp+wGdV/juGEvQ="}
4. Accept: application/json
5. {
6. "appId": "5765880207853***",
7. "callbackUrl": "https://www.xxxxxx.com/hw/pay/callback",
8. "mercContractCode": "2024020316555432***",
9. "mercNo": "10132120***",
10. "planId": "1***"
11. }
```

## 响应参数

**Response Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |

**Response Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| resultCode | 是 | String | 返回码，"000000"表示成功，其他表示见[错误码](payment-error-code-rest.md#公共错误码说明)。 |
| resultDesc | 是 | String | 结果描述。 |
| subCode | 否 | String | 业务错误码。 |
| subDesc | 否 | String | 业务错误描述信息。 |
| sign | 是 | String | 签名值。用于开发者对响应报文进行防篡改验证。 |
| preSignNo | 是 | String | 预签约号。有效期10分钟。 |

## 响应示例

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "000000",
5. "resultDesc": "Success.",
6. "sign": "MEQCIEIWzdpzi************XJItvq/ZkIcCN5/B20pQ==",
7. "preSignNo": "27713875*****"
8. }
```

## 错误码

**resultCode**非400000的错误码请查看[公共错误码说明](payment-error-code-rest.md#公共错误码说明)。

| **返回码** | **错误码** | **错误描述** | 解决方案 |
| --- | --- | --- | --- |
| 400000 | NO\_MATCH\_MATCHING\_PRODUCT | 未匹配到商户产品 | 检查商户产品是否配置正确。 |
| 400000 | INVALID\_ARGUMENTS | 参数不合法 | 检查参数是否正确。 |
| 400000 | INVALID\_APPID | appId不匹配 | 检查appId是否正确且已经绑定商户号。 |
