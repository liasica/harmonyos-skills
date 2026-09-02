---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-rest-openid-configuration
title: 获取OpenID Connect配置公开信息
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > REST API > 扩展能力 > 获取OpenID Connect配置公开信息
category: harmonyos-references
scraped_at: 2026-09-02T15:02:50+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9461bd104c9a9e5ec456644d7c8082bf403677540bc86c1e32b4a32798e142fc
---

**注意** 

为了更安全的网络访问，请务必使用TLS1.2协议及规定内的加密套件。若使用协议是TLS1.0、TLS1.1或规定外的加密套件，可能无法正常访问华为账号服务。

关于TLS1.2协议及规定内加密套件的信息，可以点击这里进行详细了解：[TLS协议及加密套件](account-api-common.md#tls协议及加密套件)。

## 功能介绍

获取OpenID Connect配置公开信息。

## 场景描述

应用通过该API获取OAuth2服务的一些公开配置信息，如授权、获取Token、取消授权、JWT公钥信息等接入地址信息。

## 使用约束

需确保调用端网络正常。

## 接口原型

* **承载协议：** HTTPS POST/GET
* **接口方向：** 开发者服务器->华为账号服务器
* **接口URL：** https://oauth-login.cloud.huawei.com/.well-known/openid-configuration
* **数据格式：**

  响应消息：Content-Type: application/json

## 请求参数

无

## 请求示例

请通过POST方式调用，示例如下：

```http
POST /.well-known/openid-configuration HTTP/1.1
Host: oauth-login.cloud.huawei.com
```

请通过GET方式调用，示例如下：

```http
GET /.well-known/openid-configuration HTTP/1.1
Host: oauth-login.cloud.huawei.com
```

## 响应参数

### Response Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json。 |

### Response Body

| **参数** | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| issuer | 是 | String | 发行方。 |
| authorization\_endpoint | 是 | String | 授权接入地址。 |
| token\_endpoint | 是 | String | 获取Token接入地址。 |
| revocation\_endpoint | 是 | String | 取消授权接入地址。 |
| jwks\_uri | 是 | String | 获取JWT公钥信息接入地址。 |
| response\_modes\_supported | 是 | String[] | 获取身份验证的响应模式。  固定返回["form\_post"]，表示使用HTTP GET/POST表单提交方式返回授权码。 |
| response\_types\_supported | 是 | String[] | 支持的授权类型。固定返回["code"]，表示支持授权码模式。 |
| subject\_types\_supported | 是 | String[] | 支持的主题类型。  固定返回["pairwise"]，表示OP（OpenID Provider）会为每个RP（Relying Party）提供不同的sub值，从而在不同的RP（Relying Party）之间保护用户的唯一性。 |
| id\_token\_signing\_alg\_values\_supported | 是 | String[] | ID Token签名支持的算法。  - RS256  - PS256 |
| scopes\_supported | 是 | String[] | 支持的授权范围，当前支持的scope如下：  - openid  - email  - profile |
| token\_endpoint\_auth\_methods\_supported | 是 | String[] | 获取token接入地址支持的客户端身份验证方法列表。  固定返回["client\_secret\_post"]，表示使用HTTP POST方法将Client ID和Client Secret作为表单参数传递给授权服务器。 |
| claims\_supported | 是 | String[] | 支持的声明类型。  - aud：Client ID  - email：用户邮箱  - email\_verified：是否已邮箱验证  - exp：ID Token的过期时间  - family\_name：用户姓氏  - given\_name：用户名字（不包括姓氏）  - iat：ID Token的签发时间  - iss：ID Token的签发者  - locale：用户的首选语言和地区  - name：用户完整姓名  - picture：用户头像URL  - sub：用户的唯一标识（UnionID）  - display\_name：用户昵称 |
| code\_challenge\_methods\_supported | 是 | String[] | PKCE模式授权时，支持对code\_verifier进行编码的方法。固定["S256"]，表示使用SHA-256算法对码值进行加密。 |

## 响应示例

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
   "issuer": "https://accounts.huawei.com",
   "authorization_endpoint": "https://oauth-login.cloud.huawei.com/oauth2/v3/authorize",
   "token_endpoint": "https://oauth-login.cloud.huawei.com/oauth2/v3/token",
   "revocation_endpoint": "https://oauth-login.cloud.huawei.com/oauth2/v3/revoke",
   "jwks_uri": "https://oauth-login.cloud.huawei.com/oauth2/v3/certs",
   "response_modes_supported": [
      "form_post"
   ],
   "response_types_supported": [
      "code"
   ],
   "subject_types_supported": [
      "pairwise"
   ],
   "id_token_signing_alg_values_supported": [
      "RS256",
      "PS256"
   ],
   "scopes_supported": [
      "openid",
      "email",
      "profile"
   ],
   "token_endpoint_auth_methods_supported": [
      "client_secret_post"
   ],
   "claims_supported": [
       "aud",
       "email",
       "email_verified",
       "exp",
       "family_name",
       "given_name",
       "iat",
       "iss",
       "locale",
       "name",
       "picture",
       "sub",
       "display_name"
    ],
    "code_challenge_methods_supported": [
        "S256"
    ]
}
```

## 示例代码

Java示例代码如下，运行前需要进行[示例代码环境配置](account-api-common.md#示例代码环境配置)（请将此示例代码与工具类CallUtils放于同一路径下，如不在同一路径，请手动添加import）

```java
import com.alibaba.fastjson2.JSONArray;
import com.alibaba.fastjson2.JSONObject;
import org.apache.http.client.methods.HttpGet;
import java.io.IOException;

/**
 * 获取OpenID Connect配置公开信息
 */
public class GetOpenIdConnect {
    public static void main(String[] args) throws IOException {
        // 获取OpenID Connect配置公开信息的接口URL
        String url = "https://oauth-login.cloud.huawei.com/.well-known/openid-configuration";
        HttpGet httpGet = new HttpGet(url);
        JSONObject result = CallUtils.toJsonObject(CallUtils.remoteCallOAuth(httpGet));
        // 解析获取issuer
        String issuer = result.getString("issuer");
        // 解析获取authorization_endpoint
        String authorizationEndpoint = result.getString("authorization_endpoint");
        // 解析获取token_endpoint
        String tokenEndpoint = result.getString("token_endpoint");
        // 解析获取revocation_endpoint
        String revocationEndpoint = result.getString("revocation_endpoint");
        // 解析获取jwks_uri
        String jwksUri = result.getString("jwks_uri");
        // 解析获取response_modes_supported
        JSONArray responseModesSupported = result.getJSONArray("response_modes_supported");
        // 解析获取response_types_supported
        JSONArray responseTypesSupported = result.getJSONArray("response_types_supported");
        // 解析获取subject_types_supported
        JSONArray subjectTypesSupported = result.getJSONArray("subject_types_supported");
        // 解析获取id_token_signing_alg_values_supported
        JSONArray idTokenSigningAlgValuesSupported = result.getJSONArray("id_token_signing_alg_values_supported");
        // 解析获取scopes_supported
        JSONArray scopesSupported = result.getJSONArray("scopes_supported");
        // 解析获取token_endpoint_auth_methods_supported
        JSONArray tokenEndpointAuthMethodsSupported = result.getJSONArray("token_endpoint_auth_methods_supported");
        // 解析获取claims_supported
        JSONArray claimsSupported = result.getJSONArray("claims_supported");
        // 解析获取code_challenge_methods_supported
        JSONArray codeChallengeMethodsSupported = result.getJSONArray("code_challenge_methods_supported");
    }
}
```

## 错误码

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 成功。 | - |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的http请求method。 | 请检查http请求method是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 系统流控。 | 触发系统流控，请稍后重试。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 590 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
