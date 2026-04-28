---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-user-info-get-phone
title: 获取华为账号用户信息-获取手机号
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > REST API > 获取用户信息 > 获取华为账号用户信息-获取手机号
category: harmonyos-references
scraped_at: 2026-04-28T08:16:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1388b9177dfc8ac42fd73a833defb53a71c1aef08973d43de9356a907706a6fc
---

注意

为了更安全的网络访问，请务必使用TLS1.2协议及规定内的加密套件。若使用协议是TLS1.0、TLS1.1或规定外的加密套件，可能无法正常访问华为账号服务。

关于TLS1.2协议及规定内加密套件的信息，可以点击这里进行详细了解：[TLS协议及加密套件](account-api-common.md#tls协议及加密套件)。

## 功能介绍

[获取手机号](../harmonyos-guides/account-get-phone-overview.md)场景，应用服务端向华为账号服务器调用该接口获取UnionID，OpenID，用户授权开放的手机号码及其相关信息。

## 场景描述

应用已经通过授权码（Authorization Code）获取到Access Token后，获取UnionID，OpenID，用户授权开放的手机号码及其相关信息。一般用于元服务和游戏应用。

## 使用约束

* 需确保调用端网络正常。
* 应用获取手机号之前，需要完成phone（获取您的手机号）的scope权限申请，在获取Authorization Code时携带phone（获取您的手机号）scope，详见[业务流程](../atomic-guides/account-guide-atomic-get-phonenumber.md#section168761120115)。

说明

应用未申请phone（获取您的手机号）的scope权限，或获取Authorization Code时未携带phone（获取您的手机号）scope，调用成功后响应中将不包含手机号。

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
| Content-Type | 是 | String | 取值为：application/x-www-form-urlencoded。  **说明：**  Request Body传参，请务必遵循此请求头格式，否则可能导致请求失败，具体传参方式可参考[示例代码](account-api-get-user-info-get-phone.md#示例代码)。 |

### Request Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| access\_token | 是 | String | 通过[获取用户级凭证](account-api-obtain-user-token.md)获取的Access Token。获取凭证时Authorization Code需包含phone scope的授权。 |

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
| mobileNumber | 否 | String | 用户选择授权给应用的手机号（华为账号绑定号码或用户选择的其他手机号），详见[获取手机号](../harmonyos-guides/account-get-phone-overview.md)。  以下场景mobileNumber不返回:  - 用户未绑定手机号。  - 用户授权提供的手机号与华为账号的关联已被删除。  - 应用未申请phone的scope权限。  - 获取Authorization Code时不携带phone scope。 |
| purePhoneNumber | 否 | String | 不带国家码的手机号，此处为去除国际冠码与国际电话区号的手机号形式。  当不返回 mobileNumber 时，也不进行返回。 |
| phoneCountryCode | 否 | String | purePhoneNumber的国际冠码(00)+国际电话区号。  当不返回 mobileNumber 时，也不进行返回。 |

说明

如字段无特殊说明，华为账号服务器返回的手机号码格式如下：

* 当账号注册地为中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）且绑定手机号为中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）手机号码时，省略国际冠码与国际电话区号，直接返回手机号码，如: 11136000008。
* 其它情况则遵循格式：国际冠码(统一使用00) + 国际电话区号 + 手机号码，如：0085261234567 (香港特别行政区)、 0079871234560 (俄罗斯)。

调用失败时，响应消息返回如下：

| 参数 | 参数位置 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| NSP\_STATUS | header | String | 错误码，详见本章节[错误码](account-api-get-user-info-get-phone.md#错误码)。 |
| error | body | String | 错误描述信息。 |

## 响应示例

### 请求成功时

* 注册地中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）且绑定手机号为中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）手机号码：

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json;charset=utf-8

4. {
5. "openID": "AQAxrBzThFv*****lv9tV_4rMCc",
6. "unionID": "AQAxrB1HNA*****n-IfWRSUVq2M7xU",
7. // 用户授权开放的手机号码(返回数据实际为明文)
8. "mobileNumber": "191******08",
9. // 不带国际冠码与国际电话区号的手机号码(返回数据实际为明文)
10. "purePhoneNumber": "191******08",
11. "phoneCountryCode": "0086"
12. }
```

* 其他情况：

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json;charset=utf-8

4. {
5. "openID": "AQAxrBzThFv*****lv9tV_4rMCc",
6. "unionID": "AQAxrB1HNA*****n-IfWRSUVq2M7xU",
7. // 用户授权开放的手机号码(返回数据实际为明文)
8. "mobileNumber": "00790******43",
9. // 不带国际冠码与国际电话区号的手机号码(返回数据实际为明文)
10. "purePhoneNumber": "90******43",
11. "phoneCountryCode": "007"
12. }
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

10. /**
11. * 获取华为账号用户信息-获取手机号
12. */
13. public class GetUserMobileDemo {
14. public static void main(String[] args) throws IOException {
15. // 获取华为账号用户信息-获取手机号的接口URL
16. String url = "https://account.cloud.huawei.com/rest.php?nsp_svc=GOpen.User.getInfo";
17. // 替换为实际获取到的用户级凭证Access Token
18. String accessToken = "<Access Token>";
19. JSONObject result = getInfo(url, accessToken);
20. // 解析获取openID
21. String openID = result.getString("openID");
22. // 解析获取unionID
23. String unionID = result.getString("unionID");
24. // 解析获取mobileNumber
25. String mobileNumber = result.getString("mobileNumber");
26. // 解析获取purePhoneNumber
27. String purePhoneNumber = result.getString("purePhoneNumber");
28. // 解析获取phoneCountryCode
29. String phoneCountryCode = result.getString("phoneCountryCode");
30. }

32. private static JSONObject getInfo(String url, String accessToken) throws IOException {
33. HttpPost httpPost = new HttpPost(url);
34. List<NameValuePair> request = new ArrayList<>();
35. request.add(new BasicNameValuePair("access_token", accessToken));
36. httpPost.setHeader("Content-Type", "application/x-www-form-urlencoded");
37. httpPost.setEntity(new UrlEncodedFormEntity(request));
38. // 使用默认异常处理逻辑，自定义异常处理请使用api CallUtils#remoteCall(HttpUriRequest, BiFunction<CloseableHttpResponse,String,E>)
39. return CallUtils.toJsonObject(CallUtils.remoteCall(httpPost));
40. }
41. }
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
| 6 | 会话失效，session timeout。  可能原因:  - access\_token无效或已过期  - access\_token格式不正确  - 其他内部原因 | - 请检查传参是否正确，如无问题请尝试重新获取。  - 未对access\_token进行URLEncode处理，可参考[示例代码](account-api-get-user-info-get-phone.md#示例代码)组装参数。  - 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 105 | 参数错误 | 参考API文档的说明，调整参数传值。 |
| 403 | 访问无权限。 | 请前往AppGallery Connect（简称AGC）为应用申请开放权限，详见[申请账号权限](../harmonyos-guides/account-config-permissions.md)。 |
| 500 | 接口内部错误。 | 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 触发系统流控。 | 请稍后重试。 |
| 70001402 | 系统鉴权错误。 | 鉴权系统异常，若重试无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 70020002 | 内部网络错误。 | 内部网络错误，若重试无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 70001401 | 系统内部错误。 | 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
