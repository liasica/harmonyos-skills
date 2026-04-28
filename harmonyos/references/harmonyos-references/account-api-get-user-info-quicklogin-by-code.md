---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-user-info-quicklogin-by-code
title: 一键登录获取华为账号绑定号码和UnionID/OpenID
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > REST API > 获取用户信息 > 一键登录获取华为账号绑定号码和UnionID/OpenID
category: harmonyos-references
scraped_at: 2026-04-28T08:16:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5b5109a2045baa0fe087336fbefb7d8dc45adfc6b2a03dab6e807b3f6155efae
---

注意

为了更安全的网络访问，请务必使用TLS1.2协议及规定内的加密套件。若使用协议是TLS1.0、TLS1.1或规定外的加密套件，可能无法正常访问华为账号服务。

关于TLS1.2协议及规定内加密套件的信息，可以点击这里进行详细了解：[TLS协议及加密套件](account-api-common.md#tls协议及加密套件)。

## 功能介绍

通过一键登录场景的Authorization Code获取UnionID，OpenID，华为账号绑定的手机号码及其相关信息。

## 场景描述

[华为账号一键登录（获取手机号和UnionID/OpenID）](../harmonyos-guides/account-phone-unionid-login.md)场景，应用服务端向华为账号服务器调用该接口获取UnionID，OpenID，华为账号绑定的手机号码及其相关信息。该服务仅对中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）用户提供。

## 使用约束

* 需确保调用端网络正常。
* 华为账号一键登录服务仅对中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）用户提供；且应用服务端获取华为账号绑定的手机号码时，该服务器必须部署在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。
* 应用使用华为账号一键登录功能之前，需要完成华为账号一键登录权限申请，详见[申请账号权限](../harmonyos-guides/account-config-permissions.md)。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器->华为账号服务器
* **接口URL：** https://account-api.cloud.huawei.com/oauth2/v6/quickLogin/getPhoneNumber
* **数据格式：**

  请求消息：Content-Type: application/json

  响应消息：Content-Type: application/json

## 请求参数

### Request Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json。  **说明：**  Request Body传参，请务必遵循此请求头格式，否则可能导致请求失败，具体传参方式可参考[示例代码](account-api-get-user-info-quicklogin-by-code.md#示例代码)。 |

### Request Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| code | 是 | String | 通过[华为账号一键登录（获取手机号和UnionID/OpenID）](../harmonyos-guides/account-phone-unionid-login.md)场景获取的Authorization Code，详情可参考一键登录[客户端开发](../harmonyos-guides/account-phone-unionid-login.md#客户端开发)。 |
| clientId | 是 | String | 在创建应用后，由AppGallery Connect（简称AGC）为应用分配的唯一标识。参数取值详见[查看应用基本信息](../app/agc-help-appinfo-0000001100014694.md)中的**OAuth 2.0客户端ID（凭据）-Client ID**参数。  **说明：**  该参数与获取code参数时的Client ID必须一致，否则会报错（响应消息中resultCode=60180003），如出现此报错，请参考[配置Client ID](../harmonyos-guides/account-client-id.md)排查处理。 |
| clientSecret | 是 | String | 在创建应用后，由AppGallery Connect（简称AGC）为应用分配的密钥（Client Secret）。参数取值详见[查看应用基本信息](../app/agc-help-appinfo-0000001100014694.md)中的**OAuth 2.0客户端ID（凭据）-Client Secret**参数。 |

## 请求示例

请通过POST方式调用，示例如下：

```
1. POST /oauth2/v6/quickLogin/getPhoneNumber HTTP/1.1
2. Host: account-api.cloud.huawei.com
3. Content-Type: application/json

5. {"code":"<code>","clientId": "<clientId>","clientSecret": "<clientSecret>"}
```

## 响应参数

### Response Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json。 |

### Response Body

调用成功时，响应消息返回如下：

| **参数** | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| openId | 是 | String | 用户OpenID。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |
| unionId | 是 | String | 用户UnionID。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |
| phoneNumber | 是 | String | 华为账号绑定号码（含国家码），使用该手机号完成一键登录的功能，详见[华为账号一键登录（获取手机号和UnionID/OpenID）](../harmonyos-guides/account-phone-unionid-login.md)。 |
| phoneNumberValid | 是 | Integer | 通过一键登录功能获取的华为账号绑定号码的实时有效性。  若发起一键登录时[LoginPanelParams](account-api-component-manager.md#loginpanelparams)的verifyPhoneNumber参数值传递为true，表示华为代为验证手机号有效性，开发者无需关注此返回值；  若verifyPhoneNumber参数值传递为false, 需要根据返回的状态值进行处理。  0：在过去90天内，无法证明当前手机号码可以触达用户， 需要进行验证。  1：在过去90天内，当前手机号码被证明可以触达用户，可以直接使用。 |
| purePhoneNumber | 是 | String | 不带国家码的手机号，此处为phoneNumber去除国际冠码与国际电话区号的形式。 |
| phoneCountryCode | 是 | String | purePhoneNumber的国际冠码(00)+国际电话区号。 |

调用失败时，响应消息返回如下：

| 参数 | 参数类型 | 描述 |
| --- | --- | --- |
| resultCode | int | 错误码，详见本章节[错误码](account-api-get-user-info-quicklogin-by-code.md#错误码)。 |
| resultDesc | String | 错误描述信息。 |

## 响应示例

### 请求成功时

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json

4. {
5. "openId": "AQAxrBzThFv*****lv9tV_4rMCc",
6. "unionId": "AQAxrB1HNA*****n-IfWRSUVq2M7xU",
7. // 华为账号绑定号码，使用该手机号完成一键登录(返回数据实际为明文)
8. "phoneNumber": "0086191******08",
9. // 通过一键登录功能获取的华为账号绑定号码的实时有效性, 0表示需要进一步验证有效性， 1表示可以直接使用
10. "phoneNumberValid": 1,
11. // 不带国际冠码与国际电话区号的形式(返回数据实际为明文)
12. "purePhoneNumber": "191******08",
13. "phoneCountryCode": "0086"
14. }
```

### 请求失败时

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json

4. {
5. "resultCode": 60180008,
6. "resultDesc": "user or phone number not exist"
7. }
```

## 示例代码

Java示例代码如下，运行前需要进行[示例代码环境配置](account-api-common.md#示例代码环境配置)（请将此示例代码与工具类CallUtils放于同一路径下，如不在同一路径，请手动添加import）

```
1. import com.alibaba.fastjson2.JSONObject;
2. import org.apache.http.client.methods.HttpPost;
3. import java.io.IOException;
4. import java.util.HashMap;
5. import java.util.Map;

7. /**
8. * 一键登录获取华为账号绑定号码和OpenID/UnionID
9. */
10. public class GetQuickLoginMobilePhoneByCodeDemo {
11. public static void main(String[] args) throws IOException {
12. // 一键登录获取华为账号绑定号码和OpenID/UnionID的接口URL
13. String url = "https://account-api.cloud.huawei.com/oauth2/v6/quickLogin/getPhoneNumber";
14. // 替换为一键登录场景获取到的Authorization Code
15. String authorizationCode = "<Authorization Code>";
16. // 替换为一键登录场景获取Authorization Code时使用的Client ID
17. String clientId = "<Client ID>";
18. // 替换为Client ID对应的Client Secret
19. String clientSecret = "<Client Secret>";
20. JSONObject result = getQuickLoginMobile(url, authorizationCode, clientId, clientSecret);
21. // 解析获取openId
22. String openId = result.getString("openId");
23. // 解析获取unionId
24. String unionId = result.getString("unionId");
25. // 解析获取phoneNumber
26. String phoneNumber = result.getString("phoneNumber");
27. // 解析获取phoneNumberValid
28. Integer phoneNumberValid = result.getInteger("phoneNumberValid");
29. // 解析获取purePhoneNumber
30. String purePhoneNumber = result.getString("purePhoneNumber");
31. // 解析获取phoneCountryCode
32. String phoneCountryCode = result.getString("phoneCountryCode");
33. }

35. private static JSONObject getQuickLoginMobile(
36. String url, String authorizationCode, String clientId, String clientSecret) throws IOException {
37. HttpPost httpPost = new HttpPost(url);
38. Map<String, Object> reqBody = new HashMap<>();
39. reqBody.put("code", authorizationCode);
40. reqBody.put("clientId", clientId);
41. reqBody.put("clientSecret", clientSecret);
42. httpPost.setHeader("Content-Type", "application/json");
43. httpPost.setEntity(CallUtils.wrapJsonEntity(reqBody));
44. // 如需要自定义异常处理请使用api CallUtils#remoteCall(HttpUriRequest, BiFunction<CloseableHttpResponse,String,E>)
45. return CallUtils.toJsonObject(CallUtils.remoteCallAccountApi(httpPost));
46. }
47. }
```

## 错误码

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 仅表示本次接口调用成功，实际业务处理结果需要通过**Response Body**中的**resultCode（错误码）** 进行判断。 | - |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的http请求method。 | 请检查http请求method是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 系统流控。 | 触发系统流控，请稍后重试。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 590 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |

| 错误码 | 描述 | 解决方法 |
| --- | --- | --- |
| 60010002 | 参数不合法。 | 请按照错误描述及接口[Request Body](account-api-get-user-info-quicklogin-by-code.md#request-body)参数说明检查入参。 |
| 60010012 | code参数不正确。 | code参数传值不正确，可能原因：伪造的无效code或code被篡改。 |
| 60010013 | clientSecret参数不正确。 | clientSecret参数传值不正确，参数取值详见[查看应用基本信息](../app/agc-help-appinfo-0000001100014694.md)中的**OAuth 2.0客户端ID（凭据）-Client Secret**参数。 |
| 60180003 | code中的client\_id和入参不一致。 | code参数获取时的clientId与当前接口参数clientId不一致导致，请检查入参client\_id是否与[配置Client ID](../harmonyos-guides/account-client-id.md)中的值一致。 |
| 60180004 | code过期，code只有5分钟有效期，超过有效期后将无法继续使用。 | 请引导用户重新授权，获取新的code再重试。 |
| 60180005 | code已经被使用过。 | code只能用一次，请重新获取code再重试。 |
| 60180006 | code已失效。正常code有效期为5分钟，但是由于用户的行为（如更改密码、取消应用的授权等行为），导致华为服务器提前失效已颁发的code。 | 请引导用户重新授权，获取新的code再重试。 |
| 60180007 | code未授权华为账号一键登录权限。 | code未授权华为账号一键登录权限，可能原因如下：  - 应用使用华为账号一键登录功能之前，需要完成华为账号一键登录权限申请，详见[申请账号权限](../harmonyos-guides/account-config-permissions.md)。  - code不是通过调用华为账号的一键登录组件获取到的，请参考[客户端开发](../harmonyos-guides/account-phone-unionid-login.md#客户端开发)的展示一键登录页面并获取Authorization Code，获取华为账号一键登录场景所需的code参数。 |
| 60180008 | 用户无手机号。 | 用户华为账号未绑定手机号，该异常场景应用需要展示其他登录方式。 |
| 60180009 | 手机号信息获取受限。 | - 华为账号一键登录服务仅对中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）用户提供。  - 应用服务端获取华为账号绑定号码时，该服务器必须部署在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 60010001 | 系统内部错误。 | 请稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
