---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-verify-id-token
title: 验证ID Token有效性
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > REST API > 扩展能力 > 验证ID Token有效性
category: harmonyos-references
scraped_at: 2026-04-28T08:16:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1e138d59bf914315b4f5dd9e5e8be2fa7bd09f9ef320b5fe9df9c6949651cf53
---

注意

为了更安全的网络访问，请务必使用TLS1.2协议及规定内的加密套件。若使用协议是TLS1.0、TLS1.1或规定外的加密套件，可能无法正常访问华为账号服务。

关于TLS1.2协议及规定内加密套件的信息，可以点击这里进行详细了解：[TLS协议及加密套件](account-api-common.md#tls协议及加密套件)。

## 功能介绍

应用服务端向华为账号服务器，调用该接口验证ID Token的有效性，并解析ID Token中的信息，只用于调试目的。

## 场景描述

* 第三方应用通过ID Token方式进行华为账号登录授权，要解析出用户的ID Token，需要先对ID Token的有效性进行验证，如果本地验证失败，可调用此接口向华为服务器发送验证请求进行调试，验证ID Token的有效性。
* 如果ID Token是直接调用[获取用户级凭证](account-api-obtain-user-token.md)的接口获取的，则不需要验证ID Token的有效性。

## 使用约束

* 需确保调用端网络正常。
* 由于调用此接口耗时，并且易受网络状况的影响，所以该接口只能用于调试目的。在商用环境需采用本地验证的方式，详见[解析与验证](../harmonyos-guides/account-faq-12.md#解析与验证)。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器->华为账号服务器
* **接口URL：** https://oauth-login.cloud.huawei.com/oauth2/v3/tokeninfo
* **数据格式：**

  请求消息：Content-Type: application/x-www-form-urlencoded

  响应消息：Content-Type: application/json

## 请求参数

### Request Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/x-www-form-urlencoded。  **说明：**  Request Body传参，请务必遵循此请求头格式，否则可能导致请求失败，具体传参方式可参考[示例代码](account-api-verify-id-token.md#示例代码)。 |

### Request Body

| **参数** | 是否必选 | **参数类型** | 描述 |
| --- | --- | --- | --- |
| id\_token | 是 | String | 应用获取到的ID Token。 |

## 请求示例

请通过POST方式调用，示例如下：

```
1. POST /oauth2/v3/tokeninfo HTTP/1.1
2. Host:oauth-login.cloud.huawei.com
3. Content-Type: application/x-www-form-urlencoded

5. id_token=<id_token>
```

## 响应参数

### Response Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json。 |

### Response Body

调用成功时，响应消息体返回如下：

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| typ | 是 | String | ID Token的格式，固定“JWT”。 |
| alg | 是 | String | ID Token的签名算法。  - PS256  - RS256 |
| kid | 是 | String | 验证签名所用公私密钥对的id，长度最大256。 |

调用失败时，响应消息体返回如下：

| 参数 | 参数类型 | 描述 |
| --- | --- | --- |
| error | int | 业务响应主错误码，详见[错误码](account-api-verify-id-token.md#错误码)。 |
| sub\_error | int | 业务响应子错误码，详见[错误码](account-api-verify-id-token.md#错误码)。 |
| error\_description | String | 错误描述信息。 |

## ID Token字段解析

其中部分字段与生成id\_token的scope有关，如下为各scope对应字段说明：

scope包含权限项openid时，解析的字段映射表如下：

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| iss | 是 | String | 固定值：https://accounts.huawei.com。 |
| sub | 是 | String | 用户的UnionID。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |
| aud | 是 | String | 接收ID Token的Client ID。 |
| exp | 是 | Long | ID Token的过期时间戳（10位）。 |
| iat | 是 | Long | ID Token的生成时间戳（10位）。 |
| at\_hash | 是 | String | Access Token的哈希值。 |
| azp | 是 | String | 生成ID Token的Client ID。 |
| openid | 是 | String | 用户OpenID。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |
| nonce | 否 | String | 防重放攻击随机值。详情请参考[LoginWithHuaweiIDRequest](account-api-authentication.md#loginwithhuaweiidrequest)或[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)的nonce字段说明。 |

scope包含权限项profile时，解析的字段映射表如下：

| **参数** | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| picture | 否 | String | 用户头像图片链接。 |
| display\_name | 否 | String | 华为账号对应的昵称，没有昵称则取匿名化的邮箱或手机号。 |
| nickname | 否 | String | 华为账号对应的昵称。 |

scope包含权限项quickLoginAnonymousPhone时，解析的字段映射表如下：

| **参数** | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| anonymized\_login\_mobile\_number | 否 | String | 匿名化的华为账号绑定手机号码，详见[华为账号一键登录（获取手机号和UnionID/OpenID）](../harmonyos-guides/account-phone-unionid-login.md)。 |

scope包含权限项email时，解析的字段映射表如下：

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| email\_verified | 否 | Boolean | 用户邮箱是否已验证。  - true：是  - false：否  由于Email不是华为账号的必填项，响应中可能没有这个属性。 |
| email | 否 | String | 用户邮箱地址，由于Email不是华为账号的必填项，响应中可能没有这个属性。 |

## 响应示例

### 请求成功时

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json

4. {
5. "at_hash": "Dx5WUwU*****L-SKuAvWUg",
6. "sub": "AQAxrB1HNA*****n-IfWRSUVq2M7xU",
7. "kid": "6a2880c5d6a88c*****88eb680e05197d5bebd*****7b71757fc1b9530809ca",
8. "iss": "https://accounts.huawei.com",
9. "typ": "JWT",
10. "display_name": "Jack",
11. "nickname": "Jack",
12. "aud": "30*****33",
13. "azp": "30*****33",
14. "exp": 1563823909,
15. "iat": 1563820309,
16. "alg": "PS256",
17. "nonce": "default",
18. "openid": "AQAxrBzThFv*****lv9tV_4rMCc"
19. }
```

### 请求失败时

```
1. HTTP/1.1 400 Bad Request
2. Content-Type: application/json

4. {
5. "sub_error": 14004,
6. "error_description": "jwk not found error",
7. "error": 1400
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
11. * 验证ID Token有效性
12. */
13. public class IDTokenAPIDemo {
14. public static void main(String[] args) throws IOException {
15. // 验证ID Token有效性的接口URL
16. String url = "https://oauth-login.cloud.huawei.com/oauth2/v3/tokeninfo";
17. // 替换为获取到的ID Token
18. String idToken = "<ID Token>";
19. JSONObject result = getDetailByIDToken(url, idToken);
20. // 解析获取kid
21. String kid = result.getString("kid");
22. // 解析获取typ
23. String typ = result.getString("typ");
24. // 解析获取alg
25. String alg = result.getString("alg");
26. // 解析获取iss
27. String iss = result.getString("iss");
28. // 解析获取sub
29. String sub = result.getString("sub");
30. // 解析获取aud
31. String aud = result.getString("aud");
32. // 解析获取exp
33. Long exp = result.getLong("exp");
34. // 解析获取iat
35. Long iat = result.getLong("iat");
36. // 解析获取at_hash
37. String atHash = result.getString("at_hash");
38. // 解析获取azp
39. String azp = result.getString("azp");
40. // 解析获取openid
41. String openid = result.getString("openid");
42. // 解析获取nonce
43. String nonce = result.getString("nonce");
44. }

46. private static JSONObject getDetailByIDToken(String url, String idToken) throws IOException {
47. HttpPost httpPost = new HttpPost(url);
48. List<NameValuePair> request = new ArrayList<>();
49. request.add(new BasicNameValuePair("id_token", idToken));
50. httpPost.setHeader("Content-Type", "application/x-www-form-urlencoded");
51. httpPost.setEntity(new UrlEncodedFormEntity(request));
52. return CallUtils.toJsonObject(CallUtils.remoteCallOAuth(httpPost));
53. }
54. }
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
| 1203 | 100305 | id\_token的header解析失败。 | id\_token格式错误或者伪造的id\_token。  - 检查id\_token值是否JWT格式。  - 检查是否为华为账号返回的原始值。 |
| 1203 | 100306 | id\_token的payload解析失败。 | id\_token格式错误或者伪造的id\_token。  - 检查id\_token值是否JWT格式。  - 检查是否为华为账号返回的原始值。 |
| 1203 | 150021 | id\_token解析失败。 | id\_token格式错误或者伪造的id\_token。  - 检查id\_token值是否JWT格式。  - 检查是否为华为账号返回的原始值。 |
| 1203 | 150023 | id\_token的signature解析失败。 | id\_token格式错误或者伪造的id\_token。  - 检查id\_token值是否JWT格式。  - 检查是否为华为账号返回的原始值。 |
| 1203 | 500 | 系统内部错误。 | 系统内部处理错误，建议业务打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1400 | 14004 | 无法通过其kid找到对应的JWT公钥相关信息。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1500 | 15003 | 无效的id\_token。 | id\_token格式错误或者伪造的id\_token。  - 检查id\_token值是否JWT格式。  - 检查是否为华为账号返回的原始值。 |
| 1500 | 15004 | id\_token验证失败。 | 检查验证时使用的公钥、算法是否正确。 |
| 1500 | 15005 | id\_token的issuer验证失败。 | 请排查id\_token是否被篡改。 |
| 1500 | 15006 | id\_token已过期。 | 请重新获取新的id\_token。 |
| 1500 | 15007 | id\_token为空。 | 请按照接口参数的要求，传入正确的id\_token参数。 |
| 1500 | 15008 | id\_token格式不正确。 | 检查id\_token的格式是否满足正则：^[0-9a-zA-Z\_\-\.]+$。 |
