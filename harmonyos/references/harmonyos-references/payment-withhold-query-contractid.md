---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-withhold-query-contractid
title: 通过contractId查询签约订单信息
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 直连商户 > 签约代扣 > 查询签约订单 > 通过contractId查询签约订单信息
category: harmonyos-references
scraped_at: 2026-04-29T14:08:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9da64ad33166161fd6e8e3a45b8acc156bd5ff4a390631403d3b4cb05820cd02
---

## 功能介绍

开发者可以调用此接口来查询所有通过华为支付签约成功的订单的详细信息。

## 场景描述

存在签约关系前提下，开发者可以通过该接口查看某笔签约订单的信息，也可以通过主动查询签约订单状态用以完成下一步的业务逻辑，常见的使用场景：

* 支付时由于网络、服务器等异常未收到签约回调通知。
* 调用签约接口返回未知签约状态时。

## 接口原型

* **承载协议：** HTTPS GET
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** https://petalpay-developer.cloud.huawei.com.cn/api/v2/contract/sign/contracts/{contractId
* **数据格式：**

  请求消息：Content-Type: application/json; charset=UTF-8

  响应消息：Content-Type: application/json; charset=UTF-8

## 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |
| PayMercAuth | 是 | String | 取值为：[PayMercAuth](payment-model.md#paymercauth)的JSON字符串 |

**Request Path**

| 参数 | 是否必填 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| contractId | 是 | String | 委托代扣协议ID，签约成功后回调接口中返回。 |

## 请求示例

```
1. GET /api/v2/contract/sign/contracts/{contractId} HTTP/1.1
2. Content-Type: application/json;charset=UTF-8
3. PayMercAuth:
4. {"callerId":"10132120***","traceId":"202305151047588466083","time":1684118878350,"authId":"120291744647139***","headerSign":"4Xb1tDGRC4f/B58ANI********************znmsDJOALXgvh/RKeReQBbc4lXZp5wnyZmdwTesmPGdszSNP/s=","bodySign":"kf9AZmVjBSGUI2MldsIFShO+Ak00qpPKaXgJo+K********************7gdghaJShhzAsNjt8DE9ulUIlQ0Q95/dZt2jEHcXyLfGNVzDNfFPhvF08NnnGM4="}
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
| mercNo | 否 | String | 签约商户号。 |
| appId | 否 | String | 应用ID。获取方式请参见[AppID管理及关联](../pay-docs/hwzf-appidguanli-0000001757041165.md)。 |
| contractId | 否 | String | 委托代扣协议ID。 |
| mercContractCode | 否 | String | 商户签约协议号。 |
| planId | 否 | String | 协议模板ID。该模板ID是商户在向华为支付[提交代扣权限申请](../harmonyos-guides/payment-password-free-pay-overview.md)时由华为支付生成。 |
| signedTime | 否 | String | 签约时间，格式：yyyy-MM-dd hh:mm:ss。 |
| expireDate | 否 | String | 签约过期时间，格式：yyyy-MM-dd。 |
| signStatus | 否 | String | 签约状态。  1：已签约  9：已解约 |
| payer | 否 | [PayerOut](payment-model.md#payerout) | 用户支付时客户端信息。 |

## 响应示例

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "mercContractCode": "2024020316555432***",
5. "signedTime": "2023-09-01 09:01:25",
6. "resultCode": "000000",
7. "sign": "MEUCIQDQ206irxpkVWGQPN*************Dvy1CaNnXaKU+uZBnrJmdhm5aG4JM=",
8. "contractId": "2024070914615843071097***",
9. "planId": "1***",
10. "resultDesc": "success",
11. "mercNo": "10132120***"
12. }
```

## 错误码

**resultCode**非400000的错误码请查看[公共错误码说明](payment-error-code-rest.md#公共错误码说明)。

| **返回码** | **错误码** | **错误描述** | 解决方案 |
| --- | --- | --- | --- |
| 400000 | UNKNOW\_ERROR | 服务暂不可用，请稍后重试 | 稍后重试。 |
| 400000 | CUST\_NOT\_EXIST | 用户不存在或已销户 | 请更换签约号重试。 |
| 400000 | CHECK\_CONTRACT\_STATUS | 签约号无效 | 1. 请确认是否存在签约关系。  2. 检查签约号输入是否正确。 |
