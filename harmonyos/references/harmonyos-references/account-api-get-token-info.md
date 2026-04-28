---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-token-info
title: 解析凭证
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > REST API > 开放接口调用凭证 > 解析凭证
category: harmonyos-references
scraped_at: 2026-04-28T08:16:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3695b8bc7e156442224ecb8f775f9d6131156b744e6b123a5f9cd8491dd48782
---

注意

为了更安全的网络访问，请务必使用TLS1.2协议及规定内的加密套件。若使用协议是TLS1.0、TLS1.1或规定外的加密套件，可能无法正常访问华为账号服务。

关于TLS1.2协议及规定内加密套件的信息，可以点击这里进行详细了解：[TLS协议及加密套件](account-api-common.md#tls协议及加密套件)。

## 功能介绍

* 对已经获得的Access Token进行鉴权。
* 通过华为服务器解析Access Token，获取Client ID、UnionID、OpenID、scope等信息。

## 场景描述

应用已经获取到Access Token，要对其进行解析并获取Access Token中包含的Client ID、UnionID、OpenID、scope等信息。

## 使用约束

需确保调用端网络正常。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器->华为账号服务器
* **接口URL：** https://oauth-api.cloud.huawei.com/rest.php?nsp\_fmt=JSON&nsp\_svc=huawei.oauth2.user.getTokenInfo
* **数据格式：**

  请求消息：Content-Type: application/x-www-form-urlencoded

  响应消息：Content-Type: text/plain;charset=utf-8

## 请求参数

### Request Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/x-www-form-urlencoded。  **说明：**  Request Body传参，请务必遵循此请求头格式，否则可能导致请求失败，具体传参方式可参考[示例代码](account-api-get-token-info.md#示例代码)。 |

### Request Body

| **参数** | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| access\_token | 是 | String | 通过[获取用户级凭证](account-api-obtain-user-token.md)/[刷新用户级凭证](account-api-obtain-refresh-token.md)/[获取应用级凭证](account-api-obtain-app-token.md)获取到的access\_token值。 |
| open\_id | 否 | String | 需要解析用户级凭证并期望拿到OpenID时，请填写该参数，填写固定值字符串“OPENID”。 |

## 请求示例

请通过POST方式调用，示例如下：

```
1. POST /rest.php?nsp_fmt=JSON&nsp_svc=huawei.oauth2.user.getTokenInfo HTTP/1.1
2. Host: oauth-api.cloud.huawei.com
3. Content-Type: application/x-www-form-urlencoded

5. open_id=OPENID&access_token=<access_token>
```

## 响应参数

### Response Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：text/plain;charset=utf-8。 |

### Response Body

调用成功时，响应消息体返回如下：

| **参数** | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| client\_id | 是 | String | 在创建应用后，由AppGallery Connect（简称AGC）为应用分配的唯一标识。参数取值详见[查看应用基本信息](../app/agc-help-appinfo-0000001100014694.md)中的**OAuth 2.0客户端ID（凭据）-Client ID**参数。 |
| expire\_in | 是 | Integer | Access Token的过期时间，单位为秒。 |
| union\_id | 否 | String | 用户的UnionID，由用户账号和应用开发者账号签名而成。当Access Token为用户级时才返回。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |
| open\_id | 否 | String | 用户的OpenID，由用户账号和Client ID签名而成，当Access Token为用户级，且入参open\_id为OPENID时才返回。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |
| scope | 否 | String | 用户授权scope列表，通过空格分隔，当Access Token为用户级且用户授权的scope不为空时才返回。 |
| project\_id | 是 | String | 项目ID，项目的唯一标识。 |
| type | 是 | Integer | 凭证类型。  0：通过[获取用户级凭证](account-api-obtain-user-token.md)获取的Access Token。  1：通过[获取应用级凭证](account-api-obtain-app-token.md)获取的Access Token。 |

调用失败时，响应消息体返回如下：

| 参数 | 参数位置 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| NSP\_STATUS | header | String | 错误码，详见本章节[错误码](account-api-get-token-info.md#错误码)。 |
| error | body | String | 错误描述信息。 |

## 响应示例

### 请求成功时

```
1. HTTP/1.1 200 OK
2. Content-Type: text/plain;charset=utf-8

4. {
5. "union_id": "AQAxrB1HNA*****n-IfWRSUVq2M7xU",
6. "scope": "openid profile",
7. "open_id": "AQAxrBzThFv*****lv9tV_4rMCc",
8. "expire_in": 1123,
9. "client_id": "12*****61",
10. "project_id": "123*****789",
11. "type": 0
12. }
```

### 请求失败时

```
1. HTTP/1.1 200 OK
2. Content-Type: text/plain;charset=utf-8
3. NSP_STATUS: 102

5. {
6. "error": "invalid session"
7. }
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
11. * 解析凭证
12. */
13. public class GetTokenInfoAPIDemo {
14. public static void main(String[] args) throws IOException {
15. // 解析凭证的接口URL
16. String url
17. = "https://oauth-api.cloud.huawei.com/rest.php?nsp_fmt=JSON&nsp_svc=huawei.oauth2.user.getTokenInfo";
18. // 替换为实际获取到的用户级凭证Access Token或应用级凭证Access Token
19. String accessToken = "<Access Token>";
20. JSONObject result = getClientTokenInfo(accessToken, url);
21. // 解析获取type
22. Integer type = result.getInteger("type");
23. // 解析获取scope
24. String scope = result.getString("scope");
25. // 解析获取client_id
26. String clientId = result.getString("client_id");
27. // 解析获取expire_in
28. Integer expireIn = result.getInteger("expire_in");
29. // 解析获取project_id
30. String projectId = result.getString("project_id");
31. // 解析获取open_id
32. String openId = result.getString("open_id");
33. // 解析获取union_id
34. String unionId = result.getString("union_id");
35. }

37. private static JSONObject getClientTokenInfo(String accessToken, String url) throws IOException {
38. HttpPost httpPost = new HttpPost(url);
39. List<NameValuePair> request = new ArrayList<>();
40. request.add(new BasicNameValuePair("access_token", accessToken));
41. request.add(new BasicNameValuePair("openid", "OPENID"));
42. httpPost.setHeader("Content-Type", "application/x-www-form-urlencoded");
43. httpPost.setEntity(new UrlEncodedFormEntity(request));
44. // 如需要自定义异常处理请使用api CallUtils#remoteCall(HttpUriRequest, BiFunction<CloseableHttpResponse,String,E>)
45. return CallUtils.toJsonObject(CallUtils.remoteCall(httpPost));
46. }
47. }
```

## 错误码

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 仅代表接口调用成功，实际业务处理结果需要通过**Response Header**中的**NSP\_STATUS**进行判断。 | - |
| 400 | 参数错误。 | 请根据文档排查请求参数是否符合规范。 |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的http请求method。 | 请检查http请求method是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 系统流控。 | 触发系统流控，请稍后重试。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 590 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

说明

Response Header中的NSP\_STATUS字段，在处理成功时不会返回。

| NSP\_STATUS | 描述 | 解决方法 |
| --- | --- | --- |
| 6 | access\_token已过期。access\_token的有效期为3600秒，超过有效期后将无法继续使用。 | 请引导用户重新授权，获取新的access\_token。 |
| 102 | 无效的access\_token。 | access\_token参数无效，可能原因：请求头的Content-Type为application/x-www-form-urlencoded，但实际代码调用时，未对请求body参数进行URLEncode处理，可参考[示例代码](account-api-get-token-info.md#示例代码)组装参数。 |
| 500 | 接口内部错误。 | 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 501 | 服务分发异常。 | - 检查请求URL中nsp\_svc是否正确  - 若确认请求URL与文档一致，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 31204 | access\_token已失效。正常access\_token有效期为3600秒，但是由于用户的行为（如更改密码、取消应用的授权等行为），导致华为服务器提前失效已颁发的access\_token。 | 请引导用户重新授权，获取新的access\_token。 |
