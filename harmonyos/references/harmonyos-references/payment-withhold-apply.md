---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-withhold-apply
title: 申请免密代扣
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 直连商户 > 签约代扣 > 申请免密代扣
category: harmonyos-references
scraped_at: 2026-04-28T08:17:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ea122b0e1677298e6083934367e707692b3c354803071ac8715789b9f4494c8f
---

## 功能介绍

开发者可以调用此接口进行免密支付。

## 场景描述

在完成Payment Kit的签约后，开发者可以调用该接口直接进行免密扣款。

## 使用约束

换单重试，视为新的业务订单，需开发者自行将新的业务订单关联业务原订单。接口重入规则说明如下（供参考）：

| 重入判定字段 | 支持原单重入场景 | 建议换单重试场景 |
| --- | --- | --- |
| 商户订单号  （mercOrderNo） | 1. 代扣请求接口失败，根据错误码排查后，支持原商户订单号重试。  2. 代扣请求接口成功，原商户订单号重入，接口幂等返回。该笔订单状态以异步结果通知或同步查询接口里为准。 | 代扣请求成功，代扣订单查询或代扣回调通知扣款状态为TRX\_FAILED，则订单进入失败终态。如需重新扣款时，需要换单重试。 |

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** https://petalpay-developer.cloud.huawei.com.cn/api/v1/aggr/transactions/withhold
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
| allocationType | 否 | String | 分账类型。  - NO\_ALLOCATION：不分账（默认）  - DELAY\_ORDER\_ALLOCATION：延时分账  **说明：** 使用该字段需联系开发者的商户对接人协助申请开通分账能力。分账相关操作参见[分账交易管理](../pay-docs/hwzf-dongjiefenzhang-0000001200646822.md)。 |
| callbackUrl | 是 | String | 回调通知地址，通知URL必须为外网环境可直接访问的URL，要求为https地址。具体要求参考[通知回调接口说明](payment-rest-overview.md#通知回调接口说明)。最大长度为512。 |
| payload | 否 | String | 商户预留信息，在查询和回调通知时会原样返回。最大长度255。 |
| expireTime | 否 | String | 交易过期时间。此时间必须为准确的UTC时间。  格式要求："yyyy-MM-dd'T'HH:mm:ss.SSSZ" 。  **说明：**  - 下单过期时间，不传默认2个小时，如果传递则最小值无限制，最大180天，超过180天系统会报错。  - 传已过时间可能会导致订单因过期、超时等原因异常关闭。  - 开发者可以参考[获取对应的UTC过期时间示例](payment-appendix.md#获取对应的utc过期时间示例)来获取对应的UTC过期时间。 |
| contractId | 是 | String | 委托代扣协议ID。签约成功后回调接口中返回，最大长度64。 |
| payer | 否 | [PayerIn](payment-model.md#payerin) | 支付者信息。 |

## 请求示例

```
1. POST /api/v1/aggr/transactions/withhold HTTP/1.1
2. Content-Type: application/json;charset=UTF-8
3. PayMercAuth: {"callerId":"10132120***","traceId":"202305151026422776499","time":1684117602555,"authId":"120291744647139***","headerSign":"u+H1Oe3fXV9mGCES89XA7tSjp8+TELYgG*******************4WvEpfjLzpzKE2/+KYaq1jDH/+VmefC29ZXpK54c5DwKJH7rMv6SBj/z0UcN9Qr*******************AFfwjEWJu5JyvY5KunSeE6DiKs=","bodySign":"yWDtXOBqDoItPgHmF57L6U5G7F/L*******************Du6E6KxPAHE0TIkTxHMcUWx7N6405QrcBimTcTN7pBpFA7pvFe*******************vta6J5UxIUmAp+wGdV/juGEvQ="}
4. Accept: application/json
5. {
6. "appId": "5765880207853***",
7. "contractId": "2024070914615843071097***",
8. "mercNo": "10132120***",
9. "mercOrderNo": "czl00120240705***",
10. "allocationType": "DELAY_ORDER_ALLOCATION",
11. "callbackUrl": "https://www.xxxxxx.com/hw/pay/callback",
12. "currency": "CNY",
13. "totalAmount": 2,
14. "tradeSummary": "xx服务-杂志报刊"
15. }
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
| sign | 是 | String | 签名值。用于开发者对响应报文进行防篡改验证。 |
| sysTransOrderNo | 是 | String | 华为支付系统订单号。 |

**响应示例**

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "000000",
5. "resultDesc": "Success.",
6. "sign": "MEQCIEIWzdpziRyTi8vhwWHFuDdx********************beCgTDG77e+2XJItvq/ZkIcCN5/B20pQ==",
7. "sysTransOrderNo": "12407030857530004914518***"
8. }
```

## 错误码

**resultCode**非400000的错误码请看[公共错误码说明](payment-error-code-rest.md#公共错误码说明)。

| **返回码** | **错误码** | **错误描述** | 解决方案 |
| --- | --- | --- | --- |
| 400000 | CUST\_NOT\_EXIST | 用户不存在或已销户 | 请替换签约号重试。 |
| 400000 | INVALID\_ARGUMENTS | 参数不合法 | 请检查参数是否正确。 |
| 400000 | INVALID\_MERC\_NO | 无效商户号 | 请更换有效的商户号。 |
| 400000 | UNKNOW\_ERROR | 服务暂不可用，请稍后重试 | 稍后重试。 |
| 400000 | CHECK\_TRANSACTION\_ORDER\_STATUS | 交易订单状态异常 | 请查看订单是否正确或换单重试。 |
| 400000 | CHECK\_MERC\_STATUS | 商户状态异常 | 请检查商户状态是否正常。 |
| 400000 | MERC\_NOT\_SUPPORT\_ALLOCATION | 商户不支持分账 | 请更换allocationType入参。 |
| 400000 | CHECK\_ACCOUNT\_STATUS | 用户状态异常 | 请检查签约用户状态是否正常。 |
| 400000 | INVALID\_PAYMENT\_TYPE | 用户无有效支付方式 | 请检查签约用户支付方式。 |
| 400000 | WITHHOLD\_OVER\_TIMES | 代扣次数超限。 | 请间隔四小时后再重试。 |
| 400000 | INVALID\_APPID | appId不匹配。 | 请检查appId是否正确且已经绑定商户号。 |
