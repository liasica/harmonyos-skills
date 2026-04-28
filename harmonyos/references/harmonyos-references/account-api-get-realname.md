---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-realname
title: 获取实名信息
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > REST API > 实名认证 > 获取实名信息
category: harmonyos-references
scraped_at: 2026-04-28T08:16:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9e44ddbc6b966555af318e5b15b2b577f6827f4cc6d5be617c71c69227afdae6
---

注意

为了更安全的网络访问，请务必使用TLS1.2协议及规定内的加密套件。若使用协议是TLS1.0、TLS1.1或规定外的加密套件，可能无法正常访问华为账号服务。

关于TLS1.2协议及规定内加密套件的信息，可以点击这里进行详细了解：[TLS协议及加密套件](account-api-common.md#tls协议及加密套件)。

说明

该接口目前暂停开放。

## 功能介绍

应用服务端向华为账号服务器调用该接口获取华为账号实名信息（姓名，身份证号）。

## 场景描述

应用已经通过授权码（Authorization Code）获取到Access Token，并且已申请账号开放信息对应权限后，可以获取账号姓名，身份证号。

## 使用约束

该接口目前暂停开放。

## 接口原型

* **承载协议**：HTTPS POST
* **接口方向**：开发者服务器->华为账号服务器
* **接口URL**：https://openrealname.cloud.huawei.com/rest.php?nsp\_svc=OpenRealName.User.getDetailInfo
* **数据格式**：

  请求消息：Content-Type: application/x-www-form-urlencoded

  响应消息：Content-Type: application/json;charset=utf-8

## 请求参数

### Request Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/x-www-form-urlencoded。  **说明：**  Request Body传参，请务必遵循此请求头格式，否则可能导致请求失败，具体传参方式可参考[示例代码](account-api-get-realname.md#示例代码)。 |

### Request Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| access\_token | 是 | String | 通过[获取用户级凭证](account-api-obtain-user-token.md)获取的Access Token。 |
| queryRangeFlag | 是 | String | 实名信息查询范围标志：  固定传值："0001"。 |
| serviceAccountClientID | 是 | String | 服务账号，  到华为开发者联盟[API Console](https://developer.huawei.com/consumer/cn/console/overview)上，在“凭证”菜单中，选择创建服务账号密钥时会生成密钥文件，打开密钥文件中有sub\_account 信息，该参数为密钥文件中的sub\_account 的值。 |
| serviceAccountKeyID | 是 | String | 服务账号密钥ID：  打开创建服务账号密钥时生成的密钥文件，文件中有key\_id信息，该参数为密钥文件中的key\_id的值。 |

## 请求示例

请通过POST方式调用，示例如下：

```
1. POST /rest.php?nsp_svc=OpenRealName.User.getDetailInfo HTTP/1.1
2. Host: openrealname.cloud.huawei.com
3. Content-Type: application/x-www-form-urlencoded

5. access_token=<access_token>&queryRangeFlag=0001&serviceAccountClientID=<serviceAccountClientID>&serviceAccountKeyID=<serviceAccountKeyID>
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
| encryptedInfo | 否 | String | 加密后的姓名和证件号码  请使用Base64.decodeBase64方法解码后，使用请求传入的serviceAccountKeyID对应的私钥解密，解密算法为RSA/ECB/OAEPWithSHA-256AndMGF1Padding，解密后可获得明文姓名和证件号码，Json格式，如{realName:xxx, ctfCode:xxx\*\*xxx}。 |

调用失败时，响应消息体返回如下：

| 参数 | 参数位置 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| NSP\_STATUS | header | String | 错误码，详见本章节[错误码](account-api-get-realname.md#错误码)。 |
| error | body | String | 错误描述信息。 |

## 响应示例

### 请求成功时

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json;charset=utf-8

4. {
5. "encryptedInfo": "Uqk1s2m2Go-wN0bZIvgDawGUXjQb5i73pyhwQp******************ytyISICH0zSKP87zrw"
6. }
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
3. import org.apache.commons.codec.binary.Base64;
4. import org.apache.http.NameValuePair;
5. import org.apache.http.client.entity.UrlEncodedFormEntity;
6. import org.apache.http.client.methods.HttpPost;
7. import org.apache.http.message.BasicNameValuePair;
8. import javax.crypto.Cipher;
9. import javax.crypto.spec.OAEPParameterSpec;
10. import javax.crypto.spec.PSource;
11. import java.io.IOException;
12. import java.nio.charset.StandardCharsets;
13. import java.security.GeneralSecurityException;
14. import java.security.KeyFactory;
15. import java.security.PrivateKey;
16. import java.security.spec.MGF1ParameterSpec;
17. import java.security.spec.PKCS8EncodedKeySpec;
18. import java.util.ArrayList;
19. import java.util.List;

21. /**
22. * 获取实名信息
23. */
24. @Slf4j
25. public class GetDetailInfoDemo {

27. public static void main(String[] args) throws IOException {
28. // 获取实名信息的接口URL
29. String url = "https://openrealname.cloud.huawei.com/rest.php?nsp_svc=OpenRealName.User.getDetailInfo";
30. // 替换为获取到的Access Token
31. String accessToken = "<Access Token>";
32. // 替换为创建服务账号时生成的密钥文件中的sub_account值
33. String serviceAccountClientID = "<Service Account Client ID>";
34. // 替换为创建服务账号时生成的密钥文件中的key_id值
35. String serviceAccountKeyID = "<Service Account Key ID>";
36. // 解密接口响应结果所需的私钥，请替换为创建服务账号时分配的私钥（秘钥文件中private_key的值，不含前缀"-----BEGIN PRIVATE KEY-----\n"，不含后缀"\n-----END PRIVATE KEY-----\n"）
37. String privateKey = "<Private Key>";
38. JSONObject result = getDetailInfo(url, accessToken, serviceAccountClientID, serviceAccountKeyID);
39. // 解析获取encryptedInfo
40. String encryptedInfo = result.getString("encryptedInfo");
41. // 解密encryptedInfo
42. String plainData = null;
43. try {
44. plainData = decryptByPrivateKey(Base64.decodeBase64(encryptedInfo), privateKey);
45. } catch (GeneralSecurityException e) {
46. // 解密失败异常处理，如打印日志
47. log.error("decrypt encryptedInfo failed");
48. }
49. }

51. private static JSONObject getDetailInfo(String url, String accessToken, String serviceAccountClientID, String serviceAccountKeyID) throws IOException {
52. HttpPost httpPost = new HttpPost(url);
53. List<NameValuePair> request = new ArrayList<>();
54. request.add(new BasicNameValuePair("access_token", accessToken));
55. request.add(new BasicNameValuePair("serviceAccountClientID", serviceAccountClientID));
56. request.add(new BasicNameValuePair("serviceAccountKeyID", serviceAccountKeyID));
57. // 固定传0001
58. request.add(new BasicNameValuePair("queryRangeFlag", "0001"));
59. httpPost.setHeader("Content-Type", "application/x-www-form-urlencoded");
60. httpPost.setEntity(new UrlEncodedFormEntity(request));
61. // 使用默认异常处理逻辑，自定义异常处理请使用api CallUtils#remoteCall(HttpUriRequest, BiFunction<CloseableHttpResponse,String,E>)。
62. return CallUtils.toJsonObject(CallUtils.remoteCall(httpPost));
63. }

65. public static String decryptByPrivateKey(byte[] data, String privateKey) throws GeneralSecurityException {
66. String KEY_RSA = "RSA";
67. String KEY_RSA_OAEP = "RSA/ECB/OAEPWithSHA-256AndMGF1Padding";
68. byte[] bytes = Base64.decodeBase64(privateKey);
69. PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(bytes);
70. PrivateKey pk = KeyFactory.getInstance(KEY_RSA).generatePrivate(keySpec);
71. Cipher cipher = Cipher.getInstance(KEY_RSA_OAEP);
72. OAEPParameterSpec spec = new OAEPParameterSpec("SHA-256", "MGF1", MGF1ParameterSpec.SHA256,
73. PSource.PSpecified.DEFAULT);
74. cipher.init(Cipher.DECRYPT_MODE, pk, spec);
75. return new String(cipher.doFinal(data), StandardCharsets.UTF_8);
76. }
77. }
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
| 6 | 会话失效，session timeout。  可能原因:  - access\_token无效或已过期  - access\_token格式不正确 | - access\_token无效或已过期，请检查传参是否正确，如无问题请尝试重新获取。  - 未对access\_token进行URLEncode处理，可参考[示例代码](account-api-get-realname.md#示例代码)组装参数。 |
| 105 | 请求url中nsp\_svc参数错误。 | 请检查请求地址参数是否正确。 |
| 403 | 访问无权限。 | 请根据[使用约束](account-api-get-realname.md#使用约束)章节进行检查。 |
| 500 | 接口内部错误。 | 根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 接口流控。 | 业务调用频率过高，请稍后重试。 |
| 70001201 | 请求参数错误。 | 请根据错误描述信息确定错误参数并修正后重试。 |
| 70001401 | 服务内部错误。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 70009019 | 实名信息不存在 | 账号未实名，请先进行实名，或更换已实名账号，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
