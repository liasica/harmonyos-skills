---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-face-verifactaion-result
title: 人脸核身实人验证结果查询
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > REST API > 通用接口 > 人脸核身实人验证 > 人脸核身实人验证结果查询
category: harmonyos-references
scraped_at: 2026-04-28T08:18:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5a40364dadead65e9ac743c91504c6f46a0962f21e039ec1da029823fe405041
---

## 功能介绍

开发者可以调用该接口查询用户实人身份信息验证结果。

## 场景描述

开发者需要验证用户的实人身份信息，在用户完成人脸核身实人验证操作后，调用该接口获取用户人脸核身实人验证结果。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> 华为支付服务器
* **接口URL：** https://petalpay-developer.cloud.huawei.com.cn/api/v1/realname/face-verification/result
* **数据格式：**

  请求消息：Content-Type: application/json; charset=UTF-8

  响应消息：Content-Type: application/json; charset=UTF-8

## 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=UTF-8 |
| PayDevAuth | 是 | String | 取值为：[PayDevAuth](payment-model.md#paydevauth)的JSON字符串 |

**Request Body**

| 参数 | 是否必选 | 类型 | 说明 |
| --- | --- | --- | --- |
| verifyResultId | 是 | String | 验证结果ID。[应用端接口](payment-realnameservice.md#realnameservicestartfaceverification)返回的验证结果ID。 |
| openId | 是 | String | 用户对外展示的ID（获取方式请参见[获取用户信息](account-api-get-user-info-overview.md)）。长度范围为1-512。 |

## 请求示例

```
1. POST /api/v1/realname/face-verification/result HTTP/1.1
2. Content-Type: application/json;charset=UTF-8
3. PayDevAuth: {"clientId":"10132120***","accessToken":"DQEBALZh0tlSKKiNDJ9lYYg0Du0EB3E6PvcGlFsyB*******************XR+k2EX8ry1IGdDUZG1PjfcWQ94xnK7w3ag==","traceId":"202305151026422776499","time":1684117602555, "developerSignKeyId":"76e5ee072756417a829201fa********************f9a292d23ca949202c3dac548120", "petalpaySignKeyId":"DEVELOPER_SIGN_EB48251AC36***", "headerSign":"u+H3F14Oe3fS34d32S9mGCES89XA7tSjp8+********************lOGS7eADFfw2E45WJu52vY5Ku4KGcSCnSeE6DiKs=", "bodySign":"y3DFDtDLXDBqDoItDgHmFJ343H57LKH6U5G7F/*******************asPj10iDUIFeHaszDFHpiHRT23LGHaxvHJKta6J5UxIUmApL+wGdV/juGEvQ="}
4. Accept: application/json
5. {
6. "verifyResultId": "12407091401520894056950***"
7. "openId": "88e9eae22447d7a138357cbf0af2d9a3a84819ec18419631c*******************2b9cc4e33ad29e2048318b47ec98be41cecdd4e153e6216a6bd60851"
8. }
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
| verifyResult | 是 | Boolean | 人脸核身实人验证结果。 |

## 响应示例

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "resultCode": "000000",
5. "resultDesc": "Success.",
6. "sign": "MEQCIEIWzdpziRyTi8vhwWHFu********************0YAMabeCgTDG77e+2XJItvq/ZkIcCN5/B20pQ==",
7. "verifyResult": true
8. }
```

## 错误码

**resultCode**非400000的错误码请查看[公共错误码说明](payment-error-code-rest.md#公共错误码说明)。

| **返回码** | **错误码** | **错误描述** | 解决方案 |
| --- | --- | --- | --- |
| 400000 | UNKNOW\_ERROR | 服务暂不可用，请稍后重试 | 稍后重试。 |
| 400000 | INVALID\_ARGUMENTS | 参数不合法 | 检查请求参数。 |
| 400000 | CLIENT\_ID\_PARAM\_ERROR | CLIENT\_ID错误 | 检查请求头参数clientId参数是否正确。 |
| 400000 | INVALID\_OPENID | OPEN\_ID错误 | 检查请求入参openId是否正确。 |
