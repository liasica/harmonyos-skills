---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-pas-prepay
title: 预下单
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 直连商户 > 支付并签约 > 预下单
category: harmonyos-references
scraped_at: 2026-04-28T08:17:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:25333a082bff0ff8bd287d1ca1c7c2091e38b28991f4cff25a05595cb69980e3
---

## 功能介绍

开发者可以调用该接口获取预支付ID（prepayId）。

## 场景描述

在接入Payment Kit的支付并签约前，开发者需要调用该接口获取到预支付ID（prepayId），用prepayId构建[orderStr](payment-model.md#orderstr)参数返回给客户端调用支付接口拉起华为支付收银台。

## 接口原型

* **载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** https://petalpay-developer.cloud.huawei.com.cn/api/v1/aggr/pay-and-sign/preorder/create/app

  说明：元服务预下单接口请使用<https://petalpay-developer.cloud.huawei.com.cn/api/v1/aggr/pay-and-sign/preorder/create/fa>
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
| mercOrderNo | 是 | String | 商户订单号，由商户自己生成，商户需保证订单信息唯一性。最大长度46。 |
| mercNo | 是 | String | 商户号。最大长度12。 |
| tradeSummary | 是 | String | 交易的摘要。格式建议：“商户应用名称-商品描述”。最大长度128。 |
| totalAmount | 是 | Long | 订单金额，必须为大于0的整数值，单位：分。 |
| currency | 否 | String | 交易币种单位，最大长度为3。  CNY （默认，当前仅支持该币种单位） |
| goodsDetail | 否 | List<[GoodDetail](payment-model.md#gooddetail)> | 订单详细信息列表。 |
| allocationType | 否 | String | 分账类型。  - NO\_ALLOCATION：不分账（默认）  - DELAY\_ORDER\_ALLOCATION：延时分账  **说明：** 使用该字段需联系开发者的商户对接人协助申请开通分账能力。分账相关操作参见[分账交易管理](../pay-docs/hwzf-dongjiefenzhang-0000001200646822.md)。 |
| callbackUrl | 是 | String | 回调通知地址，通知URL必须为外网环境可直接访问的URL，要求为https地址。具体要求参考[通知回调接口说明](payment-rest-overview.md#通知回调接口说明)。最大长度为512。 |
| payload | 否 | String | 商户预留信息，在查询和回调通知时会原样返回。最大长度255。 |
| expireTime | 否 | String | 交易过期时间。此时间必须为准确的UTC时间。  格式要求："yyyy-MM-dd'T'HH:mm:ss.SSSZ" 。  **说明：**  - 下单过期时间，不传默认2个小时，如果传递则最小值无限制，最大180天，超过180天系统会报错。  - 传已过时间可能会导致订单因过期、超时等原因异常关闭。  - 开发者可以参考[获取对应的UTC过期时间示例](payment-appendix.md#获取对应的utc过期时间示例)来获取对应的UTC过期时间。 |
| contractInfo | 是 | [ContractInfo](payment-model.md#contractinfo) | 签约信息。 |
| payer | 否 | [PayerIn](payment-model.md#payerin) | 支付者信息。 |

## 请求示例

```
1. POST /api/v1/aggr/pay-and-sign/preorder/create/app HTTP/1.1
2. Content-Type: application/json;charset=UTF-8
3. PayMercAuth: {"callerId":"10132120***","traceId":"202305151026422776499","time":1684117602555,"authId":"120291744647139***","headerSign":"u+H1Oe3fXV9mGCES89XA7tSjp8+********************lOG7eAFfwjEWJu5JyvY5KunSeE6DiKs=","bodySign":"yWDtXOBqDoItPgHmF57L6U5G7F/*******************asPj10iUIFeaszpiRT2aQDaqLGaxvta6J5UxIUmAp+wGdV/juGEvQ="}
4. Accept: application/json
5. {
6. "appId": "5765880207853***",
7. "mercOrderNo": "czl00120240705***",
8. "mercNo": "10132120***",
9. "tradeSummary": "xx商城-手机",
10. "totalAmount": 2,
11. "currency": "CNY",
12. "callbackUrl": "https://www.xxxxxx.com/hw/pay/callback",
13. "payload": "example-payload",
14. "expireTime": "2023-03-28T17:50:12.000+0800",
15. "contractInfo": {
16. "planId": "1***",
17. "mercContractCode": "2024020316555432***",
18. "callbackUrl": "https://www.xxxxxx.com/hw/sign/callback"
19. }
20. }
```

## 响应参数

**Response Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |

**Response Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| resultCode | 是 | String | 返回码，“000000”表示成功，其他表示异常，请参见[错误码](payment-error-code-rest.md#公共错误码说明)。 |
| resultDesc | 是 | String | 结果描述。 |
| subCode | 否 | String | 业务错误码。 |
| subDesc | 否 | String | 业务错误描述信息。 |
| sign | 是 | String | 签名值。用于开发者对响应报文进行防篡改验证。 |
| prepayId | 是 | String | 预支付ID。有效期10分钟。 |
| mercOrderNo | 否 | String | 商户订单号，由商户自己生成，商户需保证订单信息唯一性。最大长度46。 |

## 响应示例

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "000000",
5. "resultDesc": "Success.",
6. "sign": "MEQCIEIWzdpziRyTi8vhwWHFuDdx********************MabeCgTDG77e+2XJItvq/ZkIcCN5/B20pQ==",
7. "prepayId": "12407091401520894056950***",
8. "mercOrderNo": "czl00120240705***"
9. }
```

## 错误码

**resultCode**非400000的错误码请查看[公共错误码说明](payment-error-code-rest.md#公共错误码说明)。

| **返回码** | **错误码** | **错误描述** | 解决方案 |
| --- | --- | --- | --- |
| 400000 | UNKNOW\_ERROR | 服务暂不可用，请稍后重试 | 稍后重试。 |
| 400000 | INVALID\_ARGUMENTS | 参数不合法 | 检查请求参数。 |
| 400000 | INVALID\_MERCNO | 无效商户号 | 检查入参商户号是否正确。 |
| 400000 | REJECTED\_BY\_RISK\_CONTROL | 风控拒绝 | 咨询华为支付团队，[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。 |
| 400000 | NO\_MATCH\_MATCHING\_PRODUCT | 未匹配到商户产品 | 检查商户产品是否配置正确。 |
| 400000 | CHECK\_ORDER\_STATUS | 订单状态异常 | 请检查是否使用相同订单重复下单。 |
| 400000 | BANK\_CARD\_NOT\_SUPPORT | 银行卡不支持 | 更换其他银行卡重试。 |
| 400000 | INVALID\_APPID | appId不匹配 | 检查appId是否正确且已经绑定商户号。 |
