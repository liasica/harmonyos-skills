---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-verify-realname
title: 实名信息校验
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > REST API > 实名认证 > 实名信息校验
category: harmonyos-references
scraped_at: 2026-04-28T08:16:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a2d117c4ab603bd723ad44bf9ab24c08e7f00643d6ecf50efb2bd0b93140ef70
---

注意

为了更安全的网络访问，请务必使用TLS1.2协议及规定内的加密套件。若使用协议是TLS1.0、TLS1.1或规定外的加密套件，可能无法正常访问华为账号服务。

关于TLS1.2协议及规定内加密套件的信息，可以点击这里进行详细了解：[TLS协议及加密套件](account-api-common.md#tls协议及加密套件)。

说明

该接口目前暂停开放。

## 功能介绍

应用服务端向华为账号服务器调用该接口，用于校验用户提供的实名信息和华为账号实名信息是否一致。

## 场景描述

应用已经通过授权码（Authorization Code）获取到Access Token，并且已申请账号开放信息对应权限后，将用户填写的实名信息与华为账号实名信息进行校验，并获取用户实名信息校验结果。

## 使用约束

该接口目前暂停开放。

## 接口原型

* **承载协议：** HTTPS POST
* **接口方向：** 开发者服务器->华为账号服务器
* **接口URL：** https://openrealname.cloud.huawei.com/rest.php?nsp\_svc=OpenRealName.User.verifyRealName
* **数据格式：**

  请求消息：Content-Type: application/x-www-form-urlencoded

  响应消息：Content-Type: application/json;charset=utf-8

## 请求参数

### Request Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/x-www-form-urlencoded。  **说明：**  Request Body传参，请务必遵循此请求头格式，否则可能导致请求失败，具体传参方式可参考[示例代码](account-api-verify-realname.md#示例代码)。 |

### Request Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| access\_token | 是 | String | 通过[获取用户级凭证](account-api-obtain-user-token.md)获取的Access Token。  **说明：**  本场景下Access Token只能使用一次，再次使用会报“access forbidden”错误。 |
| sceneID | 是 | Integer | 调用场景  0：使用华为账号实名信息验证姓名、证件类型、证件号场景  1：使用华为账号实名信息验证姓名、证件类型、证件号、人脸场景  2：使用华为账号实名信息验证人脸场景 |
| idType | 是 | Integer | ID类型枚举对象  1：UserID类型  2：OpenID类型  3：UnionID类型 |
| idValue | 是 | String | ID实际值，值类型通过idType属性定义，如传用户的UnionID、OpenID值。 |
| ctfType | 否 | Integer | 证件类型  1：身份证（sceneID调用场景为0或1时需传） |
| realName | 否 | String | 待校验实名信息中的姓名，需使用SHA-512算法进行HASH后传入（sceneID调用场景为0或1时需传） |
| ctfCode | 否 | String | 待校验实名信息中的身份证号（若尾号为x，需统一转成大写X后校验），需使用SHA-512算法进行HASH后传入（sceneID调用场景为0或1时需传） |
| supportAlg | 是 | String | 指定返回的verifyToken的签名算法类型。  - RS256  - PS256  - ES256 |

## 请求示例

请通过POST方式调用，示例如下：

```
1. POST /rest.php?nsp_svc=OpenRealName.User.verifyRealName HTTP/1.1
2. Host: openrealname.cloud.huawei.com
3. Content-Type: application/x-www-form-urlencoded

5. access_token=<access_token>&sceneID=1&ctfType=1&realName=<realName>&ctfCode=<ctfCode>&idType=2&idValue=<idValue>&supportAlg=RS256
```

## 响应参数

### Response Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=utf-8。 |

### Response Body

调用成功时，响应消息体返回如下：

| **参数** | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| state | 是 | Integer | 实名状态  0：未认证  1：已认证  2： 认证中 |
| realNameLevel | 否 | Integer | 实名认证等级  0：未实名  10：未送权威渠道验证  20：已验证填写的姓名证件号实名  30：已验证证件照片实名  35：已验证过银行卡实名  40：已验证人脸实名 |
| verifyResult | 否 | Integer | 实名一致性校验结果  0：校验一致  1：姓名不匹配  2：姓名与证件号码不匹配 |
| verifyToken | 否 | String | 验证通过后返回的Token，JWT格式的数据 |

调用失败时，响应消息体返回如下：

| 参数 | 参数位置 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| NSP\_STATUS | header | String | 错误码，详见本章节[错误码](account-api-verify-realname.md#错误码)。 |
| error | body | String | 错误描述信息。 |

## 响应示例

### 请求成功时

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json;charset=utf-8

4. {
5. "state": 1,
6. "verifyResult": 0,
7. "realNameLevel": 20,
8. "verifyToken": "eyJraWQ****Aad-dw"
9. }
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
2. import lombok.extern.slf4j.Slf4j;
3. import org.apache.http.NameValuePair;
4. import org.apache.http.client.entity.UrlEncodedFormEntity;
5. import org.apache.http.client.methods.HttpPost;
6. import org.apache.http.message.BasicNameValuePair;
7. import javax.xml.bind.annotation.adapters.HexBinaryAdapter;
8. import java.io.IOException;
9. import java.nio.charset.StandardCharsets;
10. import java.security.MessageDigest;
11. import java.security.NoSuchAlgorithmException;
12. import java.util.ArrayList;
13. import java.util.List;
14. import java.util.Locale;

16. /**
17. * 实名信息校验
18. */
19. @Slf4j
20. public class VerifyRealNameDemo {

22. public static void main(String[] args) throws IOException {
23. // 实名信息校验的接口URL
24. String url = "https://openrealname.cloud.huawei.com/rest.php?nsp_svc=OpenRealName.User.verifyRealName";
25. // 替换为获取的Access Token
26. String accessToken = "<Access Token>";
27. // 替换为需要的调用场景
28. Integer sceneID = 1;
29. // 待校验姓名，当sceneID值为0或1时，该参数必传（此处无需进行SHA-512，后面调用逻辑中已具备SHA-512处理能力）
30. String realName = "<realName>";
31. // 替换为需要校验的实名信息中的身份证号，此处无需进行SHA-512，后面调用逻辑中已具备SHA-512处理能力
32. String ctfCode = "<ctfCode>";
33. // 证件类型，当sceneID值为0或1时，该参数必传，并且固定传1；否则传null
34. Integer ctfType = 1;
35. // 请替换为实际场景的idType(1：UserID类型 2：OpenID类型 3：UnionID类型)
36. Integer idType = 2;
37. // 请替换为实际场景的idValue(根据idType属性定义，传对应用户的身份标识，如UserID值、OpenID值、UnionID值)
38. String idValue = "<idValue>";

40. JSONObject result = verifyRealName(url, accessToken, sceneID, realName, ctfCode, ctfType, idType, idValue);

42. // 解析获取state
43. Integer state = result.getInteger("state");
44. // 解析获取realNameLevel
45. Integer realNameLevel = result.getInteger("realNameLevel");
46. // 解析获取verifyResult
47. Integer verifyResult = result.getInteger("verifyResult");
48. // 解析获取verifyToken
49. String verifyToken = result.getString("verifyToken");
50. }

52. /**
53. * 调用华为账号服务，进行实名信息校验
54. *
55. * @param url 实名信息校验的接口URL
56. * @param accessToken Access Token
57. * @param sceneID 调用场景 0：使用华为账号实名信息验证姓名、证件类型、证件号场景 1：使用华为账号实名信息验证姓名、证件类型、证件号、人脸场景 2：使用华为账号实名信息验证人脸场景
58. * @param realName 待校验姓名，当sceneID值为0或1时，该参数必传（此处无需进行SHA-512，后面调用逻辑中已具备SHA-512处理能力）；否则传null
59. * @param ctfCode 待校验身份证号，当sceneID值为0或1时，该参数必传（此处无需进行SHA-512，后面调用逻辑中已具备SHA-512处理能力）；否则传null
60. * @param ctfType 证件类型，当sceneID值为0或1时，该参数必传，并且固定传1；否则传null
61. * @param idType ID类型枚举对象 1：UserID类型 2：OpenID类型 3：UnionID类型
62. * @param idValue 根据idType参数值，传入对应用户的身份标识，如UserID值、UnionID值、OpenID值
63. * @return JSONObject 服务响应数据
64. * @throws IOException 调用异常
65. */
66. private static JSONObject verifyRealName (
67. String url, String accessToken, Integer sceneID,
68. String realName, String ctfCode, Integer ctfType,
69. Integer idType, String idValue
70. ) throws IOException {
71. HttpPost httpPost = new HttpPost(url);
72. List<NameValuePair> request = new ArrayList<>();
73. request.add(new BasicNameValuePair("access_token", accessToken));
74. request.add(new BasicNameValuePair("sceneID", String.valueOf(sceneID)));
75. request.add(new BasicNameValuePair("realName", encryptBySHA512(realName)));
76. request.add(new BasicNameValuePair("ctfCode", encryptBySHA512(ctfCode.toLowerCase(Locale.US))));
77. if (ctfType != null) {
78. request.add(new BasicNameValuePair("ctfType", String.valueOf(ctfType)));
79. }
80. request.add(new BasicNameValuePair("idType", String.valueOf(idType)));
81. request.add(new BasicNameValuePair("idValue", idValue));
82. // 请根据实际情况调整supportAlg的值
83. request.add(new BasicNameValuePair("supportAlg", "PS256"));
84. httpPost.setHeader("Content-Type", "application/x-www-form-urlencoded");
85. httpPost.setEntity(new UrlEncodedFormEntity(request));
86. // 使用默认异常处理逻辑，自定义异常处理请使用api CallUtils#remoteCall(HttpUriRequest, BiFunction<CloseableHttpResponse,String,E>)
87. return CallUtils.toJsonObject(CallUtils.remoteCall(httpPost));
88. }

90. private static String encryptBySHA512(String str) {
91. try {
92. MessageDigest md = MessageDigest.getInstance("SHA-512");
93. return new HexBinaryAdapter().marshal(md.digest(str.getBytes(StandardCharsets.UTF_8)))
94. .toLowerCase(Locale.US);
95. } catch (NoSuchAlgorithmException e) {
96. log.error("no such alg", e);
97. }
98. return null;
99. }
100. }
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
| 6 | 会话失效，session timeout。  可能原因:  - access\_token无效或已过期  - access\_token格式不正确 | - access\_token无效或已过期，请检查传参是否正确，如无问题请尝试重新获取。  - 未对access\_token进行URLEncode处理，可参考[示例代码](account-api-verify-realname.md#示例代码)组装参数。 |
| 105 | 请求url中nsp\_svc参数错误。 | 请检查请求地址参数是否正确。 |
| 403 | 访问无权限。 | 请根据[使用约束](account-api-verify-realname.md#使用约束)章节进行检查。 |
| 500 | 接口内部错误。 | 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 接口流控。 | 业务调用频率过高，请稍后重试。 |
| 70001201 | 请求参数错误。 | 请根据错误描述信息确定错误参数并修正后重试。 |
| 70001401 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 70009019 | 实名信息不存在 | 账号未实名，请先进行实名，或更换已实名账号，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
