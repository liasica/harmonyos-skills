---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-obtain-app-token
title: 获取应用级凭证
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > REST API > 开放接口调用凭证 > 获取应用级凭证
category: harmonyos-references
scraped_at: 2026-09-02T15:02:50+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:61a9daffa7aa0716afbe09702f4df02d8d4e97b86633fe95d8ebdadab81b89f6
---

**注意** 

为了更安全的网络访问，请务必使用TLS1.2协议及规定内的加密套件。若使用协议是TLS1.0、TLS1.1或规定外的加密套件，可能无法正常访问华为账号服务。

关于TLS1.2协议及规定内加密套件的信息，可以点击这里进行详细了解：[TLS协议及加密套件](account-api-common.md#tls协议及加密套件)。

## 功能介绍

应用服务端调用此接口获取应用级凭证Access Token。

## 场景描述

获取应用级凭证，访问被应用级权限管控的资源，例如[通过OpenID获取UnionID](account-api-get-unionid.md)。

## 使用约束

* 需确保调用端网络正常。
* 应用级Access Token有效期为3600秒，为避免不必要的网络开销，在有效期内建议应用服务器复用此Access Token。单个Client ID获取应用级Access Token频率限制为1000次/5分钟，超出此限制可能会触发流控导致请求失败。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器->华为账号服务器
* **接口URL：** https://oauth-login.cloud.huawei.com/oauth2/v3/token
* **数据格式：**

  请求消息：Content-Type: application/x-www-form-urlencoded

  响应消息：Content-Type: application/json;charset=utf-8

## 请求参数

### Request Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/x-www-form-urlencoded。  **说明：**  Request Body传参，请务必遵循此请求头格式，否则可能导致请求失败，具体传参方式可参考[示例代码](account-api-obtain-app-token.md#示例代码)。 |

### Request Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| grant\_type | 是 | String | 授权模式，本场景固定传值“client\_credentials”。 |
| client\_id | 是 | String | 在创建应用后，由AppGallery Connect（简称AGC）为应用分配的唯一标识。参数取值详见[查看应用基本信息](../app/agc-help-appinfo-0000001100014694.md)中的**OAuth 2.0客户端ID（凭据）-Client ID**参数。 |
| client\_secret | 是 | String | 在创建应用后，由AppGallery Connect（简称AGC）为应用分配的密钥（Client Secret）。参数取值详见[查看应用基本信息](../app/agc-help-appinfo-0000001100014694.md)中的**OAuth 2.0客户端ID（凭据）-Client Secret**参数。 |

## 请求示例

```http
POST /oauth2/v3/token HTTP/1.1
Host: oauth-login.cloud.huawei.com
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials&client_id=<client_id>&client_secret=<client_secret>
```

## 响应参数

### Response Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=utf-8。 |

### Response Body

调用成功时，响应消息体返回如下：

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| token\_type | 是 | String | 固定字符串“Bearer”。 |
| access\_token | 是 | String | Access Token，访问被权限管控资源的凭证。Access Token长度详见[Access Token和Refresh Token长度限制要求](../harmonyos-guides/account-faq-11.md)。 |
| expires\_in | 是 | Integer | Access Token的过期时间，单位：s。默认有效期为3600s。 |

调用失败时，响应消息体返回如下：

| 参数 | 参数类型 | 描述 |
| --- | --- | --- |
| error | int | 业务响应主错误码，详见[错误码](account-api-obtain-app-token.md#错误码)。 |
| sub\_error | int | 业务响应子错误码，详见[错误码](account-api-obtain-app-token.md#错误码)。 |
| error\_description | String | 错误描述信息。 |

## 响应示例

### 请求成功时

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
    "access_token": "DgEAAN7qd*****U0TvQ/eXpE4x+gvhoYh5/UuzL",
    "expires_in": 3600,
    "token_type": "Bearer"
}
```

### 请求失败时

```json
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
    "sub_error": 12304,
    "error_description": "invalid client_secret",
    "error": 1101
}
```

## 示例代码

Java示例代码如下，运行前需要进行[示例代码环境配置](account-api-common.md#示例代码环境配置)（请将此示例代码与工具类CallUtils放于同一路径下，如不在同一路径，请手动添加import）

```java
import com.alibaba.fastjson2.JSONObject;
import org.apache.http.NameValuePair;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.message.BasicNameValuePair;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * 获取应用级凭证
 */
public class AppTokenAPIDemo {
    public static void main(String[] args) throws IOException {
        // 获取应用级凭证的接口URL
        String url = "https://oauth-login.cloud.huawei.com/oauth2/v3/token";
        // 授权模式，固定传"client_credentials"
        String grantType = "client_credentials";
        // 替换为实际的Client ID
        String clientId = "<Client ID>";
        // 替换为Client ID对应的Client Secret
        String clientSecret = "<Client Secret>";
        JSONObject result = getAppToken(url, clientSecret, clientId, grantType);
        // 解析获取access_token
        String accessToken = result.getString("access_token");
        // 解析获取token_type
        String tokenType = result.getString("token_type");
        // 解析获取expires_in
        Integer expiresIn = result.getInteger("expires_in");
    }

    private static JSONObject getAppToken(String url, String clientSecret,
                                          String clientId, String grantType) throws IOException {
        HttpPost httpPost = new HttpPost(url);
        List<NameValuePair> request = new ArrayList<>();
        request.add(new BasicNameValuePair("client_secret", clientSecret));
        request.add(new BasicNameValuePair("client_id", clientId));
        request.add(new BasicNameValuePair("grant_type", grantType));
        httpPost.setHeader("Content-Type", "application/x-www-form-urlencoded");
        httpPost.setEntity(new UrlEncodedFormEntity(request));
        // 如需要自定义异常处理请使用api CallUtils#remoteCall(HttpUriRequest, BiFunction<CloseableHttpResponse,String,E>)
        return CallUtils.toJsonObject(CallUtils.remoteCallOAuth(httpPost));
    }
}
```

## 错误码

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 成功。 | - |
| 400 | 参数错误。 | 请根据**业务响应主错误码**以及**业务响应子错误码**进一步排查问题。 |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的http请求method。 | 请检查http请求method是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 系统流控。 | 触发系统流控，请稍后重试。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 590 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

| 业务响应主错误码 | 业务响应子错误码 | 描述 | 解决方法 |
| --- | --- | --- | --- |
| 1101 | 12304 | client\_secret不正确。 | 请前往AppGallery Connect（简称AGC）确认client\_secret是否正确。 |
| 1101 | 20002 | client\_id格式不正确。 | 检查client\_id是否满足正则：^[0-9]{1,64}$。 |
| 1101 | 20003 | client\_id在系统不存在。 | 请前往AppGallery Connect（简称AGC）确认client\_id是否存在。 |
| 1101 | 20171 | client\_secret为空。 | 请按照接口参数的要求，传入正确的client\_secret参数。 |
| 1101 | 20172 | client\_secret格式不正确。 | 检查client\_secret格式是否满足正则：^[0-9a-zA-Z=/\\+]+$。 |
| 1101 | 20182 | grant\_type值不正确。 | grant\_type可选值如下：  - “authorization\_code”：该场景用于[获取用户级凭证](account-api-obtain-user-token.md)。  - “device\_code”：该场景用于[扫码授权登录-获取用户级凭证](account-api-obtain-user-token-for-qrcode.md)。  - “refresh\_token”： 该场景用于[刷新用户级凭证](account-api-obtain-refresh-token.md)。  - “client\_credentials”：该场景用于[获取应用级凭证](account-api-obtain-app-token.md)。  当前场景请固定传”client\_credentials“。 |
| 1102 | 20001 | client\_id为空。 | 请按照接口参数的要求，传入正确的client\_id参数。 |
| 1102 | 20181 | grant\_type为空。 | grant\_type可选值如下：  - “authorization\_code”：该场景用于[获取用户级凭证](account-api-obtain-user-token.md)。  - “device\_code”：该场景用于[扫码授权登录-获取用户级凭证](account-api-obtain-user-token-for-qrcode.md)。  - “refresh\_token”： 该场景用于[刷新用户级凭证](account-api-obtain-refresh-token.md)。  - “client\_credentials”：该场景用于[获取应用级凭证](account-api-obtain-app-token.md)。  当前场景请固定传”client\_credentials“。 |
| 1203 | 500 | 系统内部错误。 | 系统内部处理错误，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1203 | 1203 | 系统未知异常。 | 系统未知异常，建议打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
