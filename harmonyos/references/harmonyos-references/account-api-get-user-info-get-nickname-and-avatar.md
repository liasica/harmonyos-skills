---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-user-info-get-nickname-and-avatar
title: 获取华为账号用户信息-获取头像昵称
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > REST API > 获取用户信息 > 获取华为账号用户信息-获取头像昵称
category: harmonyos-references
scraped_at: 2026-04-28T08:16:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:95eb87cce241a55ccb467c5cf4d515cf0926988243f6a716dce0e0b62378c6b1
---

注意

为了更安全的网络访问，请务必使用TLS1.2协议及规定内的加密套件。若使用协议是TLS1.0、TLS1.1或规定外的加密套件，可能无法正常访问华为账号服务。

关于TLS1.2协议及规定内加密套件的信息，可以点击这里进行详细了解：[TLS协议及加密套件](account-api-common.md#tls协议及加密套件)。

## 功能介绍

[获取头像昵称](../harmonyos-guides/account-get-avatar-nickname.md)场景，应用服务端向华为账号服务器调用该接口获取头像昵称及其相关信息和UnionID/OpenID。

## 场景描述

应用已经通过授权码（Authorization Code）获取到Access Token后，获取头像昵称及其相关信息和UnionID/OpenID。

## 使用约束

* 需确保调用端网络正常。
* 应用获取华为账号头像昵称之前需要在获取Authorization Code时携带profile（昵称和头像）scope，详见[业务流程](../harmonyos-guides/account-get-avatar-nickname.md#业务流程)。

说明

获取Authorization Code时不携带profile（昵称和头像）scope，调用成功后响应中将不包含昵称和头像。

## 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：开发者服务器->华为账号服务器
* **接口URL**：https://account.cloud.huawei.com/rest.php?nsp\_svc=GOpen.User.getInfo
* **数据格式**：

  请求消息：Content-Type: application/x-www-form-urlencoded

  响应消息：Content-Type: application/json;charset=utf-8

## 请求参数

### Request Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/x-www-form-urlencoded。  **说明：**  Request Body传参，请务必遵循此请求头格式，否则可能导致请求失败，具体传参方式可参考[示例代码](account-api-get-user-info-get-nickname-and-avatar.md#示例代码)。 |

### Request Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| access\_token | 是 | String | 通过[获取用户级凭证](account-api-obtain-user-token.md)获取的Access Token。获取凭证时Authorization Code需包含profile scope的授权。 |
| getNickName | 否 | int | 控制返回昵称的类型，默认为0。  0：返回匿名化账号。  1：返回华为账号昵称，没有昵称时返回匿名化账号。 |

## 请求示例

请通过POST方式调用，示例如下：

```
1. POST /rest.php?nsp_svc=GOpen.User.getInfo HTTP/1.1
2. Host: account.cloud.huawei.com
3. Content-Type: application/x-www-form-urlencoded

5. access_token=<Access Token>
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
| openID | 是 | String | 用户OpenID。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |
| unionID | 是 | String | 用户UnionID。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |
| displayName | 否 | String | 用户昵称，该字段返回场景详见[获取头像昵称](../harmonyos-guides/account-get-avatar-nickname.md)。  - 请求参数“getNickName”为0或不传时，返回匿名化账号。  - 请求参数“getNickName”为1时，返回昵称，没有昵称时返回匿名化账号。  **说明：**  调用成功后响应中若不包含用户昵称displayName，请确认获取的Authorization Code是否携带了profile（昵称和头像）scope。参考[客户端开发](../harmonyos-guides/account-get-avatar-nickname.md#客户端开发) |
| displayNameFlag | 否 | int | 返回的昵称类型 。  0：昵称。  1：匿名账号。  **说明：**  调用成功后响应中若不包含昵称类型displayNameFlag，请确认获取的Authorization Code是否携带了profile（昵称和头像）scope。参考[客户端开发](../harmonyos-guides/account-get-avatar-nickname.md#客户端开发) |
| headPictureURL | 否 | String | 用户头像，该字段返回场景详见[获取头像昵称](../harmonyos-guides/account-get-avatar-nickname.md)。用户未设置头像时不返回。 |

调用失败时，响应消息返回如下：

| 参数 | 参数位置 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| NSP\_STATUS | header | String | 错误码，详见本章节[错误码](account-api-get-user-info-get-nickname-and-avatar.md#错误码)。 |
| error | body | String | 错误描述信息。 |

## 响应示例

### 请求成功时

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json;charset=utf-8

4. {
5. "displayName": "182******74",
6. "displayNameFlag": 1,
7. "openID": "AQAxrBzThFv*****lv9tV_4rMCc",
8. "unionID": "AQAxrB1HNA*****n-IfWRSUVq2M7xU",
9. "headPictureURL": "https://upfile-*****.jpg"
10. }
```

### 请求失败时

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json;charset=utf-8
3. NSP_STATUS: 6

5. {
6. "error": "session timeout"
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
9. import java.util.Objects;

11. /**
12. * 获取华为账号用户信息-获取头像昵称
13. */
14. public class GetUserAvatarAndNickNameDemo {
15. public static void main(String[] args) throws IOException {
16. // 获取华为账号用户信息-获取头像昵称的接口URL
17. String url = "https://account.cloud.huawei.com/rest.php?nsp_svc=GOpen.User.getInfo";
18. // 替换为实际获取到的用户级凭证Access Token
19. String accessToken = "<Access Token>";
20. JSONObject result = getUserAvatarAndNickName(url, accessToken, 1);
21. // 解析获取openID
22. String openID = result.getString("openID");
23. // 解析获取unionID
24. String unionID = result.getString("unionID");
25. // 解析获取displayName
26. String displayName = result.getString("displayName");
27. // 解析获取displayNameFlag
28. Integer displayNameFlag = result.getInteger("displayNameFlag");
29. // 解析获取headPictureURL
30. String headPictureURL = result.getString("headPictureURL");
31. }

33. private static JSONObject getUserAvatarAndNickName(String url, String access_token, Integer getNickName) throws IOException {
34. HttpPost httpPost = new HttpPost(url);
35. List<NameValuePair> request = new ArrayList<>();
36. request.add(new BasicNameValuePair("access_token", access_token));
37. request.add(new BasicNameValuePair("getNickName", Objects.isNull(getNickName) ? null : String.valueOf(getNickName)));
38. httpPost.setHeader("Content-Type", "application/x-www-form-urlencoded");
39. httpPost.setEntity(new UrlEncodedFormEntity(request));
40. // 使用默认异常处理逻辑，自定义异常处理请使用api CallUtils#remoteCall(HttpUriRequest, BiFunction<CloseableHttpResponse,String,E>)
41. return CallUtils.toJsonObject(CallUtils.remoteCall(httpPost));
42. }
43. }
```

## 错误码

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 仅表示本次接口调用成功（接口调用成功不等于业务处理成功，如**Response Header**中返回了**NSP\_STATUS**字段，说明业务处理报错，需要判断报错原因）。 | - |
| 400 | 参数错误。 | 请根据文档排查请求参数是否符合规范。 |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的http请求method。 | 请检查http请求method是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 590 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

说明

Response Header中的NSP\_STATUS字段，在处理成功时不会返回。

| NSP\_STATUS | 描述 | 解决方法 |
| --- | --- | --- |
| 6 | 会话失效，session timeout。  可能原因:  - access\_token无效或已过期  - access\_token格式不正确  - 其他内部原因 | - 请检查传参是否正确，如无问题请尝试重新获取。  - 未对access\_token进行URLEncode处理，可参考[示例代码](account-api-get-user-info-get-nickname-and-avatar.md#示例代码)组装参数。  - 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 105 | 参数错误 | 参考API文档的说明，调整参数传值。 |
| 403 | 访问无权限。 | 请前往AppGallery Connect（简称AGC）为应用申请开放权限，详见[申请账号权限](../harmonyos-guides/account-config-permissions.md)。 |
| 500 | 接口内部错误。 | 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 触发系统流控。 | 请稍后重试。 |
| 70001201 | 参数不合法 | 参考API文档的说明，调整参数传值。 |
| 70001402 | 系统鉴权错误。 | 鉴权系统异常，若重试无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 70020002 | 内部网络错误。 | 内部网络错误，若重试无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 70001401 | 系统内部错误。 | 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
