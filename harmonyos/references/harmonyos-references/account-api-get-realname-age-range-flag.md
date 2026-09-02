---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-realname-age-range-flag
title: 获取用户实名年龄段
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > REST API > 实名认证 > 获取用户实名年龄段
category: harmonyos-references
scraped_at: 2026-09-02T15:02:50+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ec5efb478e36f14b5046378157cdf464a231f109befbf2f17e4f5929c6287584
---

**注意** 

为了更安全的网络访问，请务必使用TLS1.2协议及规定内的加密套件。若使用协议是TLS1.0、TLS1.1或规定外的加密套件，可能无法正常访问华为账号服务。

关于TLS1.2协议及规定内加密套件的信息，可以点击这里进行详细了解：[TLS协议及加密套件](account-api-common.md#tls协议及加密套件)。

## 功能介绍

应用服务端向华为账号服务器调用该接口获取华为账号实名信息（年龄段）。

## 场景描述

应用通过授权码（Authorization Code）获取到Access Token后，可以获取账号信息（年龄段）。用于游戏应用，具体业务流程请参见[获取用户实名年龄段](../harmonyos-guides/account-get-realname-age.md)。

## 使用约束

* 需确保调用端网络正常。
* 需要完成[realNameAgeRange（获取您的年龄段）scope权限申请](../harmonyos-guides/account-config-permissions.md)，确保在获取Authorization Code时携带realNameAgeRange scope权限。

## 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：开发者服务器->华为账号服务器
* **接口URL**：https://account-realname-api.cloud.huawei.com/openrealname/v6/realname-info/get
* **数据格式**：

  请求消息：Content-Type: application/json;charset=utf-8

  响应消息：Content-Type: application/json;charset=utf-8

## 请求参数

### Request Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=utf-8。  **说明：**  Request Body传参，请务必遵循此请求头格式，否则可能导致请求失败，具体传参方式可参考[示例代码](account-api-get-realname-age-range-flag.md#示例代码)。 |
| Authorization | 是 | String | 通过[获取用户级凭证](account-api-obtain-user-token.md)获取的Access Token。获取凭证时Authorization Code需包含realNameAgeRange scope的授权。  传参格式：Bearer ${Access Token}  样例：Bearer DgEEn\*\*\*\*\*\*Y+Aj== |

### Request Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| clientId | 是 | String | 在创建应用后，由AppGallery Connect（简称AGC）为应用分配的唯一标识。参数取值详见[查看应用基本信息](../app/agc-help-appinfo-0000001100014694.md)中的**OAuth 2.0客户端ID(凭据)-Client ID**参数。  **说明：**  该参数与获取Access Token时的Client ID必须一致，否则会报错（resultCode=61110003）。 |

## 请求示例

请通过POST方式调用，示例如下：

```http
POST /openrealname/v6/realname-info/get HTTP/1.1
Host: account-realname-api.cloud.huawei.com
Content-Type: application/json;charset=utf-8
Authorization: Bearer <Access Token>
 
{
    "clientId": "123456789"
}
```

## 响应参数

### Response Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=utf-8。 |

### Response Body

调用成功时，响应消息返回如下：

| **参数** | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| ageRangeFlag | 否 | Integer | 用户的年龄段标识。  1：未知（未实名）  2：儿童（0~14岁）  3：未成年人（14~18岁）  4：成年人（18岁以上）  以下场景ageRangeFlag不返回：  - 应用未申请realNameAgeRange权限。  - 获取Authorization Code时没有携带realNameAgeRange scope。 |

调用失败时，响应消息返回如下：

| 参数 | 参数位置 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| resultCode | body | Int | 错误码，详见本章节[错误码](account-api-get-realname-age-range-flag.md#错误码)。 |
| resultDesc | body | String | 错误描述信息。 |

## 响应示例

### 请求成功时

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
    "ageRangeFlag": 4
}
```

### 请求失败时

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
    "resultCode": 60010014,
    "resultDesc": "Invalid accessToken."
}
```

## 示例代码

Java示例代码如下，运行前需要进行[示例代码环境配置](account-api-common.md#示例代码环境配置)（请将此示例代码与工具类CallUtils放于同一路径下，如不在同一路径，请按需import）

```java
import com.alibaba.fastjson2.JSONObject;

import org.apache.http.client.methods.HttpPost;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class GetDetailInfoDemo {
    public static void main(String[] args) throws IOException {
        // 替换为实际的Client ID
        String clientId = "<Client ID>";
        // 替换为实际获取到的Access Token
        String accessToken = "Bearer <Access Token>";
        // 获取实名信息的接口URL
        String url = "https://account-realname-api.cloud.huawei.com/openrealname/v6/realname-info/get";
        HttpPost httpPost = new HttpPost(url);
        httpPost.setHeader("Content-Type", "application/json;charset=utf-8");
        httpPost.setHeader("Authorization", accessToken);
        Map<String, Object> reqBody = new HashMap<>();
        reqBody.put("clientId", clientId);
        httpPost.setEntity(CallUtils.wrapJsonEntity(reqBody));
        JSONObject result = CallUtils.toJsonObject(CallUtils.remoteCallAccountApi(httpPost));
    }
}
```

## 错误码

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 仅表示本次接口调用成功（接口调用成功不等于业务处理成功，如**Response Body**中返回了**resultCode**字段，说明业务处理报错，需要判断报错原因）。 | - |
| 400 | 参数错误。 | 请根据文档排查请求参数是否符合规范。 |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的HTTP请求method。 | 请检查HTTP请求method是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 590 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

**说明** 

Response Body中的resultCode字段，在处理成功时不会返回。

| resultCode | 描述 | 解决方法 |
| --- | --- | --- |
| 60010002 | 参数不合法。 | 请按照错误描述及接口[Request Body](account-api-get-realname-age-range-flag.md#request-body)参数说明检查入参。 |
| 60010003 | 鉴权信息不合法。 | 请检查Header中Authorization参数传值，可能是未传值或传值不正确。 |
| 60010014 | 会话失效。  可能原因:  - Access Token格式不正确  - Access Token无效或已过期 | 请检查Header中Authorization参数传值，确保获取凭证时Authorization Code包含realNameAgeRange scope的授权，详见[获取用户级凭证](account-api-obtain-user-token.md)。 |
| 61110001 | 触发系统流控。 | 请稍后重试。 |
| 61110002 | Access Token中的scope权限不满足。  可能原因:  - 应用未申请realNameAgeRange scope权限。  - 获取Authorization Code时没有携带realNameAgeRange scope。 | - 申请realNameAgeRange scope权限，详见[申请账号权限](../harmonyos-guides/account-config-permissions.md)  - 请检查Header中Authorization参数传值，确保获取凭证时Authorization Code包含realNameAgeRange scope的授权，详见[获取用户级凭证](account-api-obtain-user-token.md)。 |
| 61110003 | Access Token中的Client ID和入参clientId不一致。 | 请检查获取凭证时Authorization Code时携带的Client ID是否和body入参中的clientId保持一致。 |
| 60010001 | 系统内部错误。 | 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
