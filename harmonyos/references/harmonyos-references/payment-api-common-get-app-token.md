---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-get-app-token
title: 获取应用级凭证
category: harmonyos-references
scraped_at: 2026-04-28T08:18:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9fd1e56c856cdacb073b228db6233e2f09b8a8be3ed431f76f770ae1d130c140
---

此接口用于获取访问token，该token相当于一个访问许可，部分接口请求时华为支付服务器会对其进行校验。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器 -> 华为云服务器
* **接口URL：** https://oauth-login.cloud.huawei.com/oauth2/v3/token
* **数据格式：**

  请求消息：Content-Type: application/x-www-form-urlencoded

  响应消息：Content-Type: application/json;charset=UTF-8

## 请求参数

**Request Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/x-www-form-urlencoded |

**Request Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| grant\_type | 是 | String | 填写为“client\_credentials”，表示为客户端模式。 |
| client\_id | 是 | String | 应用的OAuth 2.0客户端ID（在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站点击“我的项目”，在项目列表中找到项目，在“项目设置 > 常规”页面的“应用”区域获取“OAuth 2.0客户端ID（凭据）：Client ID”的值） |
| client\_secret | 是 | String | 应用的OAuth 2.0客户端ID分配的密钥（在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站点击“我的项目”，在项目列表中找到项目，在“项目设置 > 常规”页面的“应用”区域获取“OAuth 2.0客户端ID（凭据）：Client Secret”的值） |

## 请求示例

```
1. POST /oauth2/v3/token?grant_type=client_credentials&client_id=<客户端ID>&client_secret=<客户端密钥> HTTP/1.1
2. Content-Type: application/x-www-form-urlencoded
```

## 响应参数

**Response Header**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=UTF-8 |

**Response Body**

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| token\_type | 是 | String | 固定字符串“Bearer”。 |
| access\_token | 是 | String | Access Token。应用凭据。 |
| expires\_in | 否 | Long | Access Token的过期时间，以秒为单位。默认60分钟过期。 |

## 响应示例

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json; charset=UTF-8
3. {
4. "access_token": "<返回的Access Token>",
5. "expires_in": 3600,
6. "token_type": "Bearer"
7. }
```
