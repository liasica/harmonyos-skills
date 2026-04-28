---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-unionid
title: 通过OpenID获取UnionID
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > REST API > 扩展能力 > 通过OpenID获取UnionID
category: harmonyos-references
scraped_at: 2026-04-28T08:16:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1d3b36b31ba3896cff5dfeb2c9ff82a8e84183a13c849e4e3a1f2a02256e5651
---

注意

为了更安全的网络访问，请务必使用TLS1.2协议及规定内的加密套件。若使用协议是TLS1.0、TLS1.1或规定外的加密套件，可能无法正常访问华为账号服务。

关于TLS1.2协议及规定内加密套件的信息，可以点击这里进行详细了解：[TLS协议及加密套件](account-api-common.md#tls协议及加密套件)。

## 功能介绍

应用服务端向华为账号服务器调用该接口，通过用户的OpenID获取UnionID信息。

## 场景描述

在开发HarmonyOS应用时，您需要考虑同一用户在非HarmonyOS应用和HarmonyOS应用的用户数据是否互通。如果您之前使用OpenID来关联用户数据，我们建议将用户数据关系切换成UnionID，以确保用户使用HarmonyOS应用后可以继承老版本的用户数据。

## 使用约束

* 需确保调用端网络正常。
* 仅能获取自身应用的用户OpenID对应的UnionID。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器->华为账号服务器
* **接口URL：** https://oauth-login.cloud.huawei.com/rest.php?nsp\_svc=huawei.oauth2.app.openIdToUnionId
* **数据格式：**

  请求消息：Content-Type: application/x-www-form-urlencoded

  响应消息：Content-Type: text/plain;charset=utf-8

## 请求参数

### Request Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/x-www-form-urlencoded。  **说明：**  Request Body传参，请务必遵循此请求头格式，否则可能导致请求失败，具体传参方式可参考[示例代码](account-api-get-unionid.md#示例代码)。 |

### Request Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| access\_token | 是 | String | 通过[获取应用级凭证](account-api-obtain-app-token.md)获取的Access Token。  **说明：**  通过OpenID获取UnionID时，Access Token必须由OpenID所属应用的Client ID获取。 |
| open\_id | 是 | String | 用户OpenID。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |

## 请求示例

请通过POST方式调用，示例如下：

```
1. POST /rest.php?nsp_svc=huawei.oauth2.app.openIdToUnionId HTTP/1.1
2. Host: oauth-login.cloud.huawei.com
3. Content-Type: application/x-www-form-urlencoded

5. open_id=<open_id>&access_token=<access_token>
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
| union\_id | 是 | String | 用户的UnionID，由用户账号和应用开发者账号签名而成。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |

调用失败时，响应消息体返回如下：

| 参数 | 参数位置 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| NSP\_STATUS | header | String | 错误码，详见本章节[错误码](account-api-get-unionid.md#错误码)。 |
| error | body | String | 错误描述信息。 |

## 响应示例

### 请求成功时

```
1. HTTP/1.1 200 OK
2. Content-Type: text/plain;charset=utf-8

4. {"union_id":"AQAxrB1HNA*****n-IfWRSUVq2M7xU"}
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
11. * 通过OpenID获取UnionID
12. */
13. public class OpenIdToUnionIdDemo {
14. public static void main(String[] args) throws IOException {
15. // 通过OpenID获取UnionID的接口URL
16. String url = "https://oauth-login.cloud.huawei.com/rest.php?nsp_svc=huawei.oauth2.app.openIdToUnionId";
17. // 替换为实际获取到的应用级凭证Access Token
18. String accessToken = "<Access Token>";
19. // 替换为获取到的OpenID
20. String openId = "<OpenID>";
21. JSONObject result = openIdToUnionId(url, accessToken, openId);
22. // 解析获取union_id
23. String unionId = result.getString("union_id");
24. }

26. private static JSONObject openIdToUnionId(String url, String accessToken, String openId) throws IOException {
27. HttpPost httpPost = new HttpPost(url);
28. List<NameValuePair> request = new ArrayList<>();
29. request.add(new BasicNameValuePair("access_token", accessToken));
30. request.add(new BasicNameValuePair("open_id", openId));
31. httpPost.setHeader("Content-Type", "application/x-www-form-urlencoded");
32. httpPost.setEntity(new UrlEncodedFormEntity(request));
33. // 使用默认异常处理逻辑，自定义异常处理请使用api CallUtils#remoteCall(HttpUriRequest, BiFunction<CloseableHttpResponse,String,E>)
34. return CallUtils.toJsonObject(CallUtils.remoteCall(httpPost));
35. }
36. }
```

## 错误码

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 仅表示本次接口调用成功，实际业务处理结果需要通过**Response Header**中的**NSP\_STATUS**进行判断。 | - |
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
| 6 | access\_token已过期。access\_token有效期为3600秒，超过有效期后将无法继续使用。 | 请通过[获取应用级凭证](account-api-obtain-app-token.md)重新获取新的access\_token。 |
| 102 | 无效的access\_token。 | access\_token参数无效，可能原因：请求头的Content-Type为application/x-www-form-urlencoded，但实际代码调用时，未对请求body参数进行URLEncode处理，可参考[示例代码](account-api-get-unionid.md#示例代码)组装参数。 |
| 403 | 无权限访问。 | 入参access\_token请通过[获取应用级凭证](account-api-obtain-app-token.md)获取，其他方式获取的access\_token不允许调用该接口。 |
| 500 | 接口内部错误。 | 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 501 | 服务分发异常。 | - 检查请求URL中nsp\_svc是否正确  - 若确认请求URL与文档一致，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 1302 | 接口流控。 | 业务调用频率过高，单应用调用并发请低于100TPS。 |
| 31204 | access\_token已失效。 | 通过[获取应用级凭证](account-api-obtain-app-token.md)获取的access\_token不会出现此错误。请严格按照接口入参要求，使用[获取应用级凭证](account-api-obtain-app-token.md)方式获取access\_token并重试。 |
| 150028 | open\_id参数为空或超长。 | 请检查open\_id是否为空或者超过256的字符长度。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md) |
