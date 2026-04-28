---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-obtain-refresh-token
title: 刷新用户级凭证
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > REST API > 开放接口调用凭证 > 刷新用户级凭证
category: harmonyos-references
scraped_at: 2026-04-28T08:16:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fc85b17bd19ba5c43a82be2be0d4ade11740fd8f847b554495a2316d08a9c51f
---

注意

为了更安全的网络访问，请务必使用TLS1.2协议及规定内的加密套件。若使用协议是TLS1.0、TLS1.1或规定外的加密套件，可能无法正常访问华为账号服务。

关于TLS1.2协议及规定内加密套件的信息，可以点击这里进行详细了解：[TLS协议及加密套件](account-api-common.md#tls协议及加密套件)。

## 功能介绍

应用服务端使用Refresh Token来获取新的Access Token。

## 场景描述

当Access Token即将过期或已经过期时，使用Refresh Token获取新的Access Token。

## 使用约束

* 需确保调用端网络正常。
* Refresh Token有效期为180天。

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
| Content-Type | 是 | String | 取值为：application/x-www-form-urlencoded。  **说明：**  Request Body传参，请务必遵循此请求头格式，否则可能导致请求失败，具体传参方式可参考[示例代码](account-api-obtain-refresh-token.md#示例代码)。 |

### Request Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| grant\_type | 是 | String | 授权模式，固定传“refresh\_token”。 |
| client\_id | 是 | String | 在创建应用后，由AppGallery Connect（简称AGC）为应用分配的唯一标识。参数取值详见[查看应用基本信息](../app/agc-help-appinfo-0000001100014694.md)中的**OAuth 2.0客户端ID（凭据）-Client ID**参数。  **说明：**  该参数与获取refresh\_token参数时的Client ID必须一致，否则会报错（sub\_error=20154），如出现此报错，请参考[配置Client ID](../harmonyos-guides/account-client-id.md)排查处理。 |
| client\_secret | 是 | String | 在创建应用后，由AppGallery Connect（简称AGC）为应用分配的密钥（Client Secret）。参数取值详见[查看应用基本信息](../app/agc-help-appinfo-0000001100014694.md)中的**OAuth 2.0客户端ID（凭据）-Client Secret**参数。 |
| refresh\_token | 是 | String | 通过[获取用户级凭证](account-api-obtain-user-token.md)获取的Refresh Token，用于刷新Access Token。 |
| scope | 否 | String | 该参数用于指定获取Access Token中的scope范围，需要是Refresh Token中包含的scope的子集，多个scope以空格分隔，当前最大支持同时传入150个scope。  - 如果没有传scope参数，则生成的Access Token包含的scope和Refresh Token中的scope相同。  - 如果传了scope参数，则Access Token所包含的scope是Refresh Token中的scope和入参scope取交集。 |
| supportAlg | 否 | String | 生成ID Token的算法，当前支持的算法如下：  - PS256（推荐使用）  - RS256  如果未指定该参数或指定的算法不在支持的范围内，则默认使用RS256。 |

## 请求示例

```
1. POST /oauth2/v3/token HTTP/1.1
2. Host: oauth-login.cloud.huawei.com
3. Content-Type: application/x-www-form-urlencoded

5. grant_type=refresh_token&client_id=<client_id>&client_secret=<client_secret>&refresh_token=<refresh_token>
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
| scope | 否 | String | Access Token中的scope，当Access Token不包含任何scope时，该字段不返回。详见入参scope字段说明。 |
| expires\_in | 是 | Integer | Access Token的过期时间，以秒为单位。有效期为3600秒。 |
| id\_token | 否 | String | 当响应参数的scope中包含openid时，则会返回此参数（JWT格式）。ID Token的描述信息请参见[验证ID Token有效性](account-api-verify-id-token.md)中ID Token描述。 |

调用失败时，响应消息体返回如下：

| 参数 | 参数类型 | 描述 |
| --- | --- | --- |
| error | int | 业务响应主错误码，详见[错误码](account-api-obtain-refresh-token.md#错误码)。 |
| sub\_error | int | 业务响应子错误码，详见[错误码](account-api-obtain-refresh-token.md#错误码)。 |
| error\_description | String | 错误描述信息。 |

## 响应示例

### 请求成功时

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json;charset=utf-8

4. {
5. "access_token": "DgEAAN7qd*****U0TvQ/eXpE4x+gvhoYh5/UuzL",
6. "id_token": "eyJraW*****ifQ.eyJhdF9oYX*****Q2fQ.TT05lFYe*****vDwb_Gj1ccR59yyB2Ig",
7. "expires_in": 3600,
8. "scope": "openid profile email",
9. "token_type": "Bearer"
10. }
```

### 请求失败时

```
1. HTTP/1.1 400 Bad Request
2. Content-Type: application/json

4. {
5. "sub_error": 12304,
6. "error_description": "invalid client_secret",
7. "error": 1203
8. }
```

## 示例代码

Java示例代码如下，运行前需要进行[示例代码环境配置](account-api-common.md#示例代码环境配置)（请将此示例代码与工具类CallUtils放于同一路径下，如不在同一路径，请手动添加import）

```
1. import com.alibaba.fastjson2.JSONObject;
2. import org.apache.http.NameValuePair;
3. import org.apache.http.client.entity.UrlEncodedFormEntity;
4. import org.apache.http.client.methods.HttpPost;
5. import org.apache.http.message.BasicNameValuePair;
6. import java.io.IOException;
7. import java.util.ArrayList;
8. import java.util.List;

10. /**
11. * 刷新用户级凭证
12. */
13. public class RefreshTokenAPIDemo {
14. public static void main(String[] args) throws IOException {
15. // 刷新用户级凭证的接口URL
16. String url = "https://oauth-login.cloud.huawei.com/oauth2/v3/token";
17. // 授权模式，固定传"refresh_token"
18. String grantType = "refresh_token";
19. // 替换为实际的Client ID
20. String clientId = "<Client ID>";
21. // 替换为Client ID对应的Client Secret
22. String clientSecret = "<Client Secret>";
23. // 替换为Client ID获取的Refresh Token
24. String refreshToken = "<Refresh Token>";
25. JSONObject result = refreshToken(url, refreshToken, clientSecret, clientId, grantType);
26. // 解析获取scope
27. String scope = result.getString("scope");
28. // 解析获取token_type
29. String tokenType = result.getString("token_type");
30. // 解析获取access_token
31. String accessToken = result.getString("access_token");
32. // 解析获取expires_in
33. Integer expiresIn = result.getInteger("expires_in");
34. // 解析获取id_token
35. String idToken = result.getString("id_token");
36. }

38. private static JSONObject refreshToken(String url, String refreshToken, String clientSecret,
39. String clientId, String grantType) throws IOException {
40. HttpPost httpPost = new HttpPost(url);
41. List<NameValuePair> request = new ArrayList<>();
42. request.add(new BasicNameValuePair("client_secret", clientSecret));
43. request.add(new BasicNameValuePair("refresh_token", refreshToken));
44. request.add(new BasicNameValuePair("client_id", clientId));
45. request.add(new BasicNameValuePair("grant_type", grantType));
46. request.add(new BasicNameValuePair("supportAlg", "PS256"));
47. httpPost.setHeader("Content-Type", "application/x-www-form-urlencoded");
48. httpPost.setEntity(new UrlEncodedFormEntity(request));
49. // 如需要自定义异常处理请使用api CallUtils#remoteCall(HttpUriRequest, BiFunction<CloseableHttpResponse,String,E>)
50. return CallUtils.toJsonObject(CallUtils.remoteCallOAuth(httpPost));
51. }
52. }
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
| 1101 | 20002 | client\_id格式不正确。 | 检查client\_id是否满足正则：^[0-9]{1,64}$。 |
| 1101 | 20003 | client\_id格式不正确或系统不存在。 | - 检查client\_id是否满足正则：^[0-9]{1,64}$。  - 请前往AppGallery Connect（简称AGC）确认client\_id是否存在。 |
| 1101 | 20041 | scope格式不正确或数量超过150个。 | - 检查scope参数是否满足正则：^[0-9a-zA-Z:/\\.\u0020]+$。  - 检查scope数量是否超过150个。 |
| 1101 | 20042 | 无效的scope。 | 入参scope存在伪造值，请参照参数说明，传入正确的参数。 |
| 1101 | 20154 | refresh\_token中的client\_id和入参不一致。 | 检查入参client\_id是否与[配置Client ID](../harmonyos-guides/account-client-id.md)中的值一致。 |
| 1101 | 20171 | client\_secret为空。 | 请按照接口参数的要求，传入正确的client\_secret参数。 |
| 1101 | 20172 | client\_secret格式不正确。 | 检查client\_secret格式是否满足正则：^[0-9a-zA-Z=/\\+]+$。 |
| 1101 | 20182 | grant\_type值不正确。 | grant\_type可选值如下：  - “authorization\_code”：该场景用于[获取用户级凭证](account-api-obtain-user-token.md)。  - “refresh\_token”： 该场景用于[刷新用户级凭证](account-api-obtain-refresh-token.md)。  - “client\_credentials”：该场景用于[获取应用级凭证](account-api-obtain-app-token.md)。 |
| 1101 | 20192 | refresh\_token格式不正确。 | refresh\_token参数格式需要满足正则：^[0-9a-zA-Z=/\\+]+$。 |
| 1102 | 20001 | client\_id为空。 | 请按照接口参数的要求，传入正确的client\_id参数。 |
| 1102 | 20181 | grant\_type为空。 | grant\_type可选值如下：  - “authorization\_code”：该场景用于[获取用户级凭证](account-api-obtain-user-token.md)。  - “refresh\_token”： 该场景用于[刷新用户级凭证](account-api-obtain-refresh-token.md)。  - “client\_credentials”：该场景用于[获取应用级凭证](account-api-obtain-app-token.md)。 |
| 1102 | 20191 | refresh\_token为空。 | 请按照接口参数的要求，传入正确的refresh\_token参数。 |
| 1203 | 11205 | refresh\_token已过期。refresh\_token的有效期为180天，超过有效期后将无法继续使用。 | 请引导用户重新授权，获取新的refresh\_token。 |
| 1203 | 12303 | client\_id在系统不存在。 | 请前往AppGallery Connect（简称AGC）确认client\_id是否存在。 |
| 1203 | 12304 | 无效的client\_secret。 | 入参client\_id和client\_secret不匹配导致，请检查参数。 |
| 1203 | 31202 | refresh\_token解析失败。 | refresh\_token不是一个正确有效的数据，请检查refresh\_token参数。 |
| 1203 | 31204 | refresh\_token已失效。正常refresh\_token有效期为180天，但是由于用户的行为（如更改密码、取消应用的授权等行为），导致华为服务器提前使已颁发的refresh\_token失效。 | 请引导用户重新授权，获取新的refresh\_token。 |
| 1203 | 31218 | refresh\_token非法。 | refresh\_token格式需要满足正则：^[0-9a-zA-Z=\/\+]+$。 |
| 1203 | 500 | 系统内部错误。 | 系统内部处理错误，建议业务打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
