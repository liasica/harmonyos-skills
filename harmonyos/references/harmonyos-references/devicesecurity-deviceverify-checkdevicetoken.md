---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-deviceverify-checkdevicetoken
title: 验证deviceToken
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > REST API > 验证deviceToken
category: harmonyos-references
scraped_at: 2026-04-28T08:07:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:45f81ac622377ce87a988918905d1d05713fda5aacf289e52afa7b750860256b
---

## 功能介绍

开发者应用的服务端可调用本接口验证deviceToken合法性，确认设备为真实的华为设备。

## 场景描述

开发者获取到device token后可调用本接口验证deviceToken合法性，确认设备为真实的华为设备。

与设备真实性证明能力的区别：

| 开放能力 | 能力说明 |
| --- | --- |
| 验证deviceToken | 验证设备真实性的一个轻量化实现，对开发者集成的要求相对简单。  不支持防重放，且每次校验都需要与Device Security服务器交互，对业务的处理时延有一定的影响。 |
| [设备真实性证明](../harmonyos-guides/device-attestation-intro.md) | 是通过在设备侧的TEE中创建一对公私钥，并对该密钥进行证明后把公钥保存在应用服务器，需要开发者在应用服务器中保存证明后的公钥，并维护公钥的生命周期，对开发者的集成要求相对较高。  支持防重放，后续的业务请求无需与设备真实性证明服务器交互，对业务的处理时延无明显的影响。 |

建议开发者根据实际的安全诉求和业务场景，选择合适的能力。

## 使用约束

无

## 接口原型

* **承载协议** HTTPS POST
* **接口方向** 开发者服务器->Device Security服务器
* **接口URL** https://connect-api.cloud.huawei.com/api/rms/v1/deviceVerify/checkDeviceToken
* **数据格式** 请求消息头：Content-Type: application/json;charset=utf-8

  响应消息：Content-Type: application/json;charset=utf-8

## 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 否 | String | 取值为：application/json;charset=utf-8。 |
| Authorization | 是 | String | 服务账号令牌 |
| bundleName | 是 | String | 开发者APP包名 |

说明

Authorization格式：Bearer后面拼接空格，再拼接获取的鉴权信息。令牌生成[示例代码](../harmonyos-guides/devicesecurity-deviceverify-token.md#示例代码)。

**Request Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| deviceToken | 是 | String | 客户端调用[getDeviceToken](devicesecurity-deviceverify-api.md#getdevicetoken)获取的设备临时标识。 |
| transactionId | 否 | String | 应用服务的唯一事务标识，关联业务上下文消息。 |
| timestamp | 是 | Long | 应用服务器上的UTC时间。单位，毫秒。 |

说明

开发者在构造消息体时，消息体需要在外层包一层data结构，详情参考如下调用示例。

## 请求示例

```
1. post /api/rms/v1/deviceVerify/checkDeviceToken HTTP/1.1
2. Host: xxx
3. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
4. bundleName: com.huawei.xxx
5. Content-Type: application/json;charset=utf-8

7. {"data":{ "deviceToken":"xxx", "transactionId":"xxx", "timestamp":1704038400}}
```

## 响应参数

**Response Body**

| **参数** | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| bundleName | 否 | String | 从token中获取的bundleName，供开发者校验。 |
| errorCodes | 是 | String | 错误码。 |

## 响应示例

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json;charset=utf-8

4. {"bundleName":"xxx","errorCodes":"OK"}
```

## 错误码

以下错误码的详细介绍请参见[REST API错误码](devicesecurity-restapi-errcode.md)。

| **错误码** | **描述** |
| --- | --- |
| OK | 请求处理成功。 |
| InvalidDeviceToken | deviceToken缺失或不合法。 |
| DeviceTokenExpired | deviceToken过期。 |
| InvalidTimeStamp | timeStamp缺失或不合法。 |
| InternalServerError | 服务器内部错误。 |
| InvalidBundleName | bundleName缺失或不合法。 |
