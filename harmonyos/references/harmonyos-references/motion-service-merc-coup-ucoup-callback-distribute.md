---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/motion-service-merc-coup-ucoup-callback-distribute
title: 发券事件回调通知
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 通用接口 > 运营工具 > 商家券 > 用户券 > 发券事件回调通知
category: harmonyos-references
scraped_at: 2026-04-28T08:18:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ecd545351e88a5e73f8d3cbe1d083070031bf1b5a899ecc345aef5043eab3b9d
---

## 功能介绍

发券后，华为支付服务器调用此接口向开发者服务器发送发券事件通知。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** URL由开发者调用创建券批次接口时通过传入
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
| callbackId | 是 | String | 回调通知的唯一ID。 |
| callbackTime | 是 | String | 回调通知创建的时间，遵循rfc3339标准格式，格式为yyyy-MM-DDTHH:mm:ss+TIMEZONE，yyyy-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss表示时分秒，TIMEZONE表示时区（+08:00表示东八区时间，领先UTC 8小时，即北京时间）。例如：2015-05-20T13:29:35+08:00表示，北京时间2015年5月20日13点29分35秒。 |
| dataType | 是 | String | 数据加密类型标识。  - encrypt：加密  - plain：未加密 |
| sign | 是 | String | 回调通知结果签名，除“sign”字段以外的其他字段参与签名。 |
| signType | 是 | String | 签名类型。华为支付生成签名字符串使用的算法，当前为SM2算法。 |
| certNo | 否 | String | 签名所使用的证书编号。 |
| eventType | 是 | String | 通知消息对应的事件类型，发券通知为：COUPON.SEND。 |
| openId | 否 | String | 用户的唯一标识。 |
| unionId | 否 | String | 用户在同一个开放平台账号下的唯一标识。当开发者账号失效时，此字段会为空。 |
| sendEntrance | 是 | String | 投放商家券的位置。  - PLATFORM\_PUSH：平台推广  - MERC\_SELF\_CHANNEL：商家自运营渠道（应用/元服务） |
| senderMerchant | 是 | String | 发券商户号。 |
| coupons | 是 | List<[CouponNotice](payment-model.md#couponnotice)> | 通知消息的附加信息，Json格式。 |

## **请求示例**

```
1. POST /opengw/merc/v1/transactions/result HTTP/1.1
2. Content-Type: application/json;charset=UTF-8
3. {
4. "callbackId": "f2eff0509b864125bc3ea54852608***",
5. "callbackTime": "2023-03-29 09:52:37",
6. "dataType": "plain",
7. "sign": "MEYCIQD8RlHJ9tGmc2tass32BgGgRbV5m********************2KxxldbJA2GYpU7nDIJCYHcZpBY1ffr21wgjQ2l",
8. "signType": "SM2",
9. "certNo": "10132120***",
10. "eventType": "1230223100516008511858780***",
11. "openId": "SM2",
12. "sendEntrance": "",
13. "senderMerchant": "516008511***",
14. "coupons": [
15. {
16. "batchNo": "1230223100516008511858780***",
17. "couponCodes": ["4b60ab60c777432296e787000***"],
18. "receiveTime": "2024-03-28T17:50:12.000+0800"
19. }
20. ]
21. }
```

## 响应参数

**Response Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |

**Response Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| resultCode | 否 | String | 华为支付侧解析application/json类型响应，“000000”表示成功，其他值失败，如返回值格式不匹配或非“000000”将视为失败。 |
| resultDesc | 否 | String | 结果描述。 |

## **响应示例**

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "000000",
5. "resultDesc": "Success."
6. }
```
