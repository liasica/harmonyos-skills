---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-pas-withhold-unsign-notify
title: 解约结果回调通知
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 直连商户 > 支付并签约 > 解约结果回调通知
category: harmonyos-references
scraped_at: 2026-04-28T08:17:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3a08a0b185f6df801ffd0b33e8287ad38c5178ddb9992170d40127d2b0796cf1
---

开发者完成解约申请成功后，华为支付服务器调用此接口向开发者服务器发送解约关键事件通知。

说明

为保证回调请求的可靠性，系统具备重试机制，所以可能出现重发的通知。

## 场景描述

一笔签约关系解除成功后，华为支付服务器会调用开发者的应用/元服务在签约模板中配置的回调接口（callbackUrl）传递给开发者解约订单的具体信息。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** URL为开发者在请求申请解约接口时传入的callbackUrl
* **数据格式：**

  请求消息：Content-Type: application/json; charset=UTF-8

  响应消息：Content-Type: application/json; charset=UTF-8

## 请求参数

**Request Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| callbackId | 是 | String | 回调通知的唯一ID。 |
| callbackTime | 是 | String | 回调通知时间。格式为yyyy-MM-dd HH:mm:ss。 |
| dataType | 否 | String | 数据加密类型标识。  - encrypt：加密  - plain：未加密 |
| sign | 是 | String | 回调通知结果签名，除“sign”字段以外的其他字段参与签名。  开发者可参考[验签规则](payment-rest-overview.md#验签规则)对回调报文进行验签处理。 |
| signType | 是 | String | 签名类型。华为支付生成签名字符串使用的算法，当前为SM2算法。 |
| certNo | 否 | String | 签名所使用的证书编号。 |
| planId | 否 | String | 协议模板ID。该模板ID是商户在向华为支付[提交代扣权限申请](../harmonyos-guides/payment-password-free-pay-overview.md)时由华为支付生成。 |
| mercContractCode | 否 | String | 商户签约协议号。商户侧自己生成。 |
| contractId | 是 | String | 委托代扣协议ID。 |
| mercNo | 否 | String | 商户号。 |
| appId | 否 | String | 应用ID。获取方式请参见[AppID管理及关联](../pay-docs/hwzf-appidguanli-0000001757041165.md)。 |
| changeMode | 否 | String | 解约方式。  - USER\_UNSIGN：用户解约  - MERC\_API\_UNSIGN：商户解约  - PLATFORM\_UNSIGN：平台解约 |
| expireDate | 否 | String | 签约过期时间，格式：yyyy-MM-dd。 |
| operateTime | 否 | String | 操作时间，如：2023-09-01 09:01:25。 |

## 请求示例

```
1. POST /hw/pay/callback HTTP/1.1
2. Content-Type: application/json;charset=UTF-8
3. {
4. "callbackId": "124070308575300049145189***",
5. "callbackTime": "2023-08-29 09:29:14",
6. "dataType": "plain",
7. "mercContractCode": "2024020316555432***",
8. "mercNo": "10132120***",
9. "operateTime": "2023-09-01 09:01:25",
10. "sign": "MEYCIQDXutp78nEN87jF***********lWyjA6p210xOqI2InX9w2SIYRx",
11. "signType": "SM2",
12. "contractId":"2024070914615843071097***",
13. "certNo": "120291744647139***"
14. }
```

## 响应参数

**Response Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |

**Response Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| resultCode | 是 | String | 响应码。华为支付侧解析application/json类型响应。 “000000”表示成功，其他值表示失败，如返回值格式不匹配或非“000000”将视为回调失败。 |
| resultDesc | 是 | String | 结果描述。 |

## 响应示例

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "000000",
5. "resultDesc": "Success."
6. }
```
