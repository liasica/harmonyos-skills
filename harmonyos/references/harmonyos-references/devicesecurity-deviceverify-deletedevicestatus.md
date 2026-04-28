---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-deviceverify-deletedevicestatus
title: 删除设备标记状态
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > REST API > 删除设备标记状态
category: harmonyos-references
scraped_at: 2026-04-28T08:07:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2f9f48e55e995cfa9ee484ec630021d0d9f0bb3bbea4a42dc6d6418a2b43d6fd
---

## 功能介绍

开发者应用的服务端可调用本接口删除设备标记状态。

## 场景描述

开发者应用的服务端可调用本接口删除设备标记状态，删除后标记在云端失效。

## 使用约束

无

## 接口原型

* **承载协议** HTTPS POST
* **接口方向** 开发者服务器->Device Security服务器
* **接口URL** https://connect-api.cloud.huawei.com/api/rms/v1/deviceVerify/delDeviceStatus
* **数据格式** 请求消息头：Content-Type：application/json;charset=utf-8

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
| mode | 是 | Int | 设备标记状态的粒度。取值：  1 ：应用级  2 ：开发者级 |
| deviceToken | 是 | String | 客户端调用[getDeviceToken](devicesecurity-deviceverify-api.md#getdevicetoken)获取的设备临时标识。 |
| transactionId | 否 | String | 应用服务的唯一事务标识，关联业务上下文消息。 |
| timestamp | 是 | Long | 应用服务器上的UTC时间。单位，毫秒。 |

说明

开发者在构造消息体时，消息体需要在外层包一层data结构，详情参考如下调用示例。

## 请求示例

```
1. POST /api/rms/v1/deviceVerify/delDeviceStatus HTTP/1.1
2. Host: xxx
3. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
4. bundleName: com.huawei.xxx
5. Content-Type: application/json;charset=utf-8

7. {"data":{ "mode":1, "deviceToken":"xxx", "transactionId":"ddc740b9-45bb-424a-bc50-64e8a813acab", "timestamp":1711072205525}}
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
| NotFound | 未找到设备的标记记录（设备身份验证成功，该设备未被标记过）。 |
| InvalidBundleName | bundleName缺失或不合法。 |
| InvalidDeviceToken | deviceToken缺失或不合法。 |
| DeviceTokenExpired | deviceToken过期。 |
| InvalidMode | Mode缺失或者非法。 |
| InvalidTimeStamp | timeStamp缺失或不合法。 |
| InternalServerError | 内部服务器错误。 |
