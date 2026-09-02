---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-api-msg-receipt
title: 消息回执
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > REST API > 消息回执
category: harmonyos-references
scraped_at: 2026-09-02T15:03:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:31f8d046189e958f617dcef3b20973ef60663203aa1cefe0bc01f2386139bf79
---

## 功能介绍

华为推送服务器调用此接口给您的服务器推送回执消息。

## 接口约束

您需要在AppGallery Connect上开通“消息回执”权益，如何开通请参见[开通回执权益](../harmonyos-guides/push-msg-receipt.md#开通回执权益)。

回执接口版本分为V1和V2，不同版本的回执消息请求头和响应参数相同，仅请求体不同。场景化消息推送仅支持V2版本回执。

## 接口原型

| 承载协议 | 接口方向 | 接口URL | 数据格式 |
| --- | --- | --- | --- |
| HTTPS POST | 华为Push服务器 -> 开发者回执消息接收服务器 | 您的回执接收服务器的地址，由您定义，同[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上配置的回执地址一致。 | 请求消息：Content-Type: application/json  响应消息：Content-Type: application/json |

## 请求参数

### Request Header

| 参数名 | 取值描述 | 样例 |
| --- | --- | --- |
| X-HUAWEI-CALLBACK-ID | 消息头鉴权参数，可选字段。当回执配置中回调用户名与回调秘钥均已配置时为必选参数。 | timestamp=1563\*\*\*\*\*1261; nonce=a07bfa17-6d82-4b53-a9a2-07c\*\*\*\*\*eef1; value=E4Ye\*\*\*\*\*HZ6592U8B9S37238E+Hwtjfrmpf8AQXF+c=  · timestamp为毫秒级时间戳  · nonce为UUID随机数  · value为待加密字符串（value示例中为了展示各字段，实际上是由timestamp、nonce、回调用户名拼接而成，不需要“+”），使用回调秘钥进行HmacSHA256加密后，经Base64编码后获得，具体请参见[示例代码](../harmonyos-guides/push-msg-receipt.md#配置回执参数) |

### Request Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| statuses | 是 | Array [[statuses](push-api-msg-receipt.md#statuses-v2版本) Object ] | 回执消息内容，包含最多100个[statuses](push-api-msg-receipt.md#statuses-v2版本)结构的数组，分为V1和V2版本。此处仅支持V2版本。 |

## statuses V2版本

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| token | 是 | String | 消息发送目标用户Token，携带给应用服务器。 |
| pushType | 是 | Integer | 消息类型，详情见[push-type](push-scenariozed-api-request-struct.md#request-header)。 |
| appPackageName | 是 | String | 消息发送方的应用包名。 |
| biTag | 否 | String | 您在发送消息时携带的biTag。如果下发推送消息未设置[biTag](push-scenariozed-api-request-param.md#pushoptions)字段，则该字段内容为空。 |
| requestId | 是 | String | 请求ID，在发送接口中返回的值。 |
| deliveryStatus | 否 | [deliveryStatus](push-api-msg-receipt.md#deliverystatus) Object | 消息的送达状态[deliveryStatus](push-api-msg-receipt.md#deliverystatus)结构体。非卡片刷新消息时回执。 |
| formStatus | 否 | [formStatus](push-api-msg-receipt.md#formstatus) Object | 卡片刷新消息的送达状态[formStatus](push-api-msg-receipt.md#formstatus)结构体，仅当消息类型为卡片刷新时回执。 |

## deliveryStatus

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| result | 是 | Integer | 消息到达的回执状态码，请参见[回执状态码](../harmonyos-guides/push-msg-receipt.md#回执状态码)。 |
| timestamp | 是 | Long | 消息成功到达客户端的时间戳（毫秒级时间戳），失败则为回执消息生成的时间戳。 |

## formStatus

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| formId | 是 | Long | 服务卡片的实例ID，当卡片[onAddForm](js-apis-app-form-formextensionability.md#formextensionabilityonaddform)（卡片使用方添加卡片至桌面）时获取。最大值为**231-1**。 |
| result | 是 | Integer | 消息到达的回执状态码，请参见[回执状态码](../harmonyos-guides/push-msg-receipt.md#回执状态码)。 |
| timestamp | 是 | Long | 消息成功到达客户端的时间戳（毫秒级时间戳），失败则为回执消息生成的时间戳。 |

## 请求示例

```json
{
  "statuses": [
    {
      "biTag": "131415",
      "pushType": 0,
      "appPackageName": "com.****",
      "token": "148896*******000001",
      "requestId": "1*******0",
      "deliveryStatus":{
        "result": 0,
        "timestamp": 1607832761768
      }
    }
  ]
}
```

## 响应参数

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| code | 是 | String | 应用服务器返回的处理结果状态。 |
| message | 是 | String | 应用服务器返回的处理结果描述信息。 |

## 响应示例

```json
{
  "code": "0",
  "message": "success"
}
```
