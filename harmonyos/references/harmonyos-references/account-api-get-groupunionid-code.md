---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-groupunionid-code
title: 通过Authorization Code获取GroupUnionID
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > REST API > 扩展能力 > 通过Authorization Code获取GroupUnionID
category: harmonyos-references
scraped_at: 2026-04-28T08:16:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1b4a8896d0912ab0c4da2e03ee25ba0f5eeb1c8b3f462fa17a394549dd678b05
---

注意

为了更安全的网络访问，请务必使用TLS1.2协议及规定内的加密套件。若使用协议是TLS1.0、TLS1.1或规定外的加密套件，可能无法正常访问华为账号服务。

关于TLS1.2协议及规定内加密套件的信息，可以点击这里进行详细了解：[TLS协议及加密套件](account-api-common.md#tls协议及加密套件)。

## 功能介绍

应用服务端通过获取到的Authorization Code调用此接口，获取GroupUnionID、用户级Access Token、Refresh Token、ID Token等信息。

## 场景描述

针对用户登录需要获取GroupUnionID场景时，可以在[华为账号一键登录（获取手机号和UnionID/OpenID）](../harmonyos-guides/account-phone-unionid-login.md)、[华为账号登录（获取UnionID/OpenID）](../harmonyos-guides/account-unionid-login-button.md)、[静默登录](../harmonyos-guides/account-silent-login.md)等场景获取到Authorization Code后，调用该接口获取GroupUnionID、Access Token、Refresh Token、ID Token等信息。

## 使用约束

* 需确保调用端网络正常。
* 仅对企业开发者开放。
* 开发者账号必须加入关联主体账号组。具体可通过[创建账号组](../start/cag-0000001265390541.md)创建关联主体账号组，然后在关联主体账号组中[添加账号组成员](../start/aai-0000001265430513.md)。
* Authorization Code仅能使用一次，且具有5分钟的有效期，过期后需重新授权获取。

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
| Content-Type | 是 | String | 取值为：application/x-www-form-urlencoded。  **说明：**  Request Body传参，请务必遵循此请求头格式，否则可能导致请求失败，具体传参方式可参考[示例代码](account-api-get-groupunionid-code.md#示例代码)。 |

### Request Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| grant\_type | 是 | String | 授权模式，固定传“authorization\_code”。 |
| client\_id | 是 | String | 在创建应用后，由AppGallery Connect（简称AGC）为应用分配的唯一标识。参数取值详见[查看应用基本信息](../app/agc-help-appinfo-0000001100014694.md)中的**OAuth 2.0客户端ID（凭据）-Client ID**参数。  **说明：**  该参数与获取code参数时的Client ID必须一致，否则会报错（sub\_error=20154），如出现此报错，请参考[配置Client ID](../harmonyos-guides/account-client-id.md)排查处理。 |
| client\_secret | 是 | String | 在创建应用后，由AppGallery Connect（简称AGC）为应用分配的密钥（Client Secret）。参数取值详见[查看应用基本信息](../app/agc-help-appinfo-0000001100014694.md)中的**OAuth 2.0客户端ID（凭据）-Client Secret**参数。 |
| code | 是 | String | Authorization Code可通过[华为账号一键登录（获取手机号和UnionID/OpenID）](../harmonyos-guides/account-phone-unionid-login.md)、[华为账号登录（获取UnionID/OpenID）](../harmonyos-guides/account-unionid-login-button.md)、[静默登录](../harmonyos-guides/account-silent-login.md)等场景获取。 |
| supportAlg | 否 | String | 生成ID Token的算法，当前支持的算法如下：  - PS256（推荐使用）  - RS256  如果未指定该参数或指定的算法不在支持的范围内，则默认使用RS256。 |
| need\_group\_union\_id | 否 | Boolean | 是否需要获取GroupUnionID，传值如下：  - true  - false  如果未指定该参数，则响应结果中不会返回group\_union\_id字段。  GroupUnionID使用场景详见[不同开发者的应用之间如何实现用户数据互通](../harmonyos-guides/account-faq-19.md)。 |

## 请求示例

```
1. POST /oauth2/v3/token HTTP/1.1
2. Host: oauth-login.cloud.huawei.com
3. Content-Type: application/x-www-form-urlencoded

5. grant_type=authorization_code&code=<code>&client_id=<client_id>&client_secret=<client_secret>&need_group_union_id=<need_group_union_id>
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
| scope | 是 | String | Access Token中的scope，以空格分隔，最大不会超过150个。 |
| expires\_in | 是 | Integer | Access Token的过期时间，以秒为单位。有效期为3600秒。 |
| refresh\_token | 是 | String | Refresh Token，用于刷新Access Token。Refresh Token有效期为180天，长度详见[Access Token和Refresh Token长度限制要求](../harmonyos-guides/account-faq-11.md)。 |
| id\_token | 是 | String | ID Token（JWT格式），详细信息请参见[验证ID Token有效性](account-api-verify-id-token.md)中ID Token描述。 |
| group\_union\_id | 否 | String | GroupUnionID是用户在关联主体账号组内的统一身份标识，使用场景详见[不同开发者的应用之间如何实现用户数据互通](../harmonyos-guides/account-faq-19.md)。当请求参数need\_group\_union\_id不传或者为false时，该字段不返回。 |

调用失败时，响应消息体返回如下：

| 参数 | 参数类型 | 描述 |
| --- | --- | --- |
| error | int | 业务响应主错误码，详见[错误码](account-api-get-groupunionid-code.md#错误码)。 |
| sub\_error | int | 业务响应子错误码，详见[错误码](account-api-get-groupunionid-code.md#错误码)。 |
| error\_description | String | 错误描述信息。 |

## 响应示例

### 请求成功时

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json;charset=utf-8

4. {
5. "access_token": "DgEAAN7qd*****U0TvQ/eXpE4x+gvhoYh5/UuzL",
6. "refresh_token": "DgECAL++vCn******NQ/UOL8+wm0jJi+o4NI793H",
7. "expires_in": 3600,
8. "id_token": "eyJraW*****ifQ.eyJhdF9oYX*****Q2fQ.TT05lFYe*****vDwb_Gj1ccR59yyB2Ig",
9. "scope": "openid profile",
10. "token_type": "Bearer",
11. "group_union_id": "AgAsmsA25yiLl*****8Gr-uQyoKU8rSfMEwFJiqOA"
12. }
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
11. * 通过Authorization Code获取GroupUnionID
12. */
13. public class GetGroupUnionIDByCodeDemo {
14. public static void main(String[] args) throws IOException {
15. // 通过Authorization Code获取GroupUnionID的接口URL
16. String url = "https://oauth-login.cloud.huawei.com/oauth2/v3/token";
17. // 授权模式，这里使用授权码模式（authorization_code）获取Access Token
18. String grantType = "authorization_code";
19. // 替换为实际的Client ID
20. String clientId = "<Client ID>";
21. // 替换为Client ID对应的Client Secret
22. String clientSecret = "<Client Secret>";
23. // 替换为获取到的授权码（Authorization Code）
24. String code = "<Authorization Code>";
25. JSONObject result = getGroupUnionIDByCode(url, code, clientSecret, clientId, grantType);
26. // 解析获取group_union_id
27. String groupUnionId = result.getString("group_union_id");
28. // 解析获取scope
29. String scope = result.getString("scope");
30. // 解析获取access_token
31. String accessToken = result.getString("access_token");
32. // 解析获取refresh_token
33. String refreshToken = result.getString("refresh_token");
34. // 解析获取token_type
35. String tokenType = result.getString("token_type");
36. // 解析获取expires_in
37. Integer expiresIn = result.getInteger("expires_in");
38. // 解析获取id_token
39. String idToken = result.getString("id_token");
40. }

42. private static JSONObject getGroupUnionIDByCode(String url, String code, String clientSecret,
43. String clientId, String grantType) throws IOException {
44. HttpPost httpPost = new HttpPost(url);
45. List<NameValuePair> request = new ArrayList<>();
46. request.add(new BasicNameValuePair("code", code));
47. request.add(new BasicNameValuePair("client_secret", clientSecret));
48. request.add(new BasicNameValuePair("client_id", clientId));
49. request.add(new BasicNameValuePair("grant_type", grantType));
50. request.add(new BasicNameValuePair("supportAlg", "PS256"));
51. request.add(new BasicNameValuePair("need_group_union_id", "true"));
52. httpPost.setHeader("Content-Type", "application/x-www-form-urlencoded");
53. httpPost.setEntity(new UrlEncodedFormEntity(request));
54. // 如需要自定义异常处理请使用api CallUtils#remoteCall(HttpUriRequest, BiFunction<CloseableHttpResponse,String,E>)
55. return CallUtils.toJsonObject(CallUtils.remoteCallOAuth(httpPost));
56. }
57. }
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
| 1101 | 20003 | client\_id格式不正确或系统不存在。 | - 检查client\_id是否满足正则：^[0-9]{1,64}$。  - 请前往AppGallery Connect（简称AGC）确认client\_id是否存在。 |
| 1101 | 20085 | client\_secret为空。 | 请按照接口参数的要求，传入正确的client\_secret参数。 |
| 1101 | 20152 | code格式不正确。 | 检查code格式是否满足正则：^[0-9a-zA-Z=/\\+]+$。  该错误码出现可能场景：  - code参数被篡改，导致格式不符。  - 请求头的Content-Type为application/x-www-form-urlencoded，但实际代码调用时，未对请求body体进行URLEncode处理，可参考[示例代码](account-api-get-groupunionid-code.md#示例代码)组装参数。 |
| 1101 | 20154 | code中的client\_id和入参不一致。 | 检查入参client\_id是否与[配置Client ID](../harmonyos-guides/account-client-id.md)中的值一致。 |
| 1101 | 20155 | code过期，code只有5分钟有效期，超过有效期后将无法继续使用。 | 请引导用户重新授权，获取新的code再重试。 |
| 1101 | 20156 | code已经被使用过。 | code只能用一次，请重新获取code再重试。 |
| 1101 | 20158 | code已失效。正常code有效期为5分钟，但是由于用户的行为（如更改密码、取消应用的授权等行为），导致华为服务器提前失效已颁发的code。 | 请引导用户重新授权，获取新的code再重试。 |
| 1101 | 20171 | client\_secret为空。 | 请按照接口参数的要求，传入正确的client\_secret参数。 |
| 1101 | 20172 | client\_secret格式不正确。 | 检查client\_secret格式是否满足正则：^[0-9a-zA-Z=/\\+]+$。 |
| 1101 | 20182 | grant\_type值不正确。 | grant\_type可选值如下：  - “authorization\_code”：该场景用于[获取用户级凭证](account-api-obtain-user-token.md)。  - “refresh\_token”： 该场景用于[刷新用户级凭证](account-api-obtain-refresh-token.md)。  - “client\_credentials”：该场景用于[获取应用级凭证](account-api-obtain-app-token.md)。 |
| 1102 | 20001 | client\_id为空。 | 请按照接口参数的要求，传入正确的client\_id参数。 |
| 1102 | 20151 | code为空。 | 请按照接口参数的要求，传入正确的code参数。 |
| 1102 | 20181 | grant\_type为空。 | grant\_type可选值如下：  - “authorization\_code”：该场景用于[获取用户级凭证](account-api-obtain-user-token.md)。  - “refresh\_token”： 该场景用于[刷新用户级凭证](account-api-obtain-refresh-token.md)。  - “client\_credentials”：该场景用于[获取应用级凭证](account-api-obtain-app-token.md)。 |
| 1103 | 20153 | 无效的code。 | code被篡改或伪造的code导致，请排查code参数是否与获取到的code一致。 |
| 1203 | 12303 | client\_id在系统不存在。 | 请前往AppGallery Connect（简称AGC）确认client\_id是否存在。 |
| 1203 | 12304 | 无效的client\_secret。 | 入参client\_id和client\_secret不匹配导致，请检查参数。 |
| 1203 | 500 | 系统内部错误。 | 系统内部处理错误，建议业务打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1203 | 100300 | 系统处理异常。 | 请重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1203 | 100502 | 开发者账号的关联主体账号组未查询到。 | 请参考[添加账号组成员](../start/aai-0000001265430513.md)，将应用的开发者账号加入关联主体账号组后重试。 |
