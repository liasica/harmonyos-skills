---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-rest-jwt-public-key
title: 获取验证ID Token的JWT公钥信息
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > REST API > 扩展能力 > 获取验证ID Token的JWT公钥信息
category: harmonyos-references
scraped_at: 2026-04-28T08:16:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cdd89740c533e0c05512d9d40adb30f899538978faa9af0d3e44e638518792dd
---

注意

为了更安全的网络访问，请务必使用TLS1.2协议及规定内的加密套件。若使用协议是TLS1.0、TLS1.1或规定外的加密套件，可能无法正常访问华为账号服务。

关于TLS1.2协议及规定内加密套件的信息，可以点击这里进行详细了解：[TLS协议及加密套件](account-api-common.md#tls协议及加密套件)。

## 功能介绍

获取ID Token解析与验证所需的JWT公钥信息。该接口会返回当天及前一天的JWT公钥信息，应用服务端可根据ID Token中的kid与此接口返回的kid进行比对，拿到对应的公钥信息。

## 场景描述

应用在获取到ID Token后，需要对其进行解析与验证，解析后可获取用户数据，并验证签名。

说明

* JWT公钥信息每天0点进行刷新。
* PS256与RS256算法的JWT公钥信息一致。具体如何通过JWT公钥解析验证ID Token，详见[服务端解析与验证](../harmonyos-guides/account-faq-12.md#服务端解析与验证) 。

## 使用约束

需确保调用端网络正常。

## 接口原型

* **承载协议：** HTTPS POST/GET
* **接口方向：** 开发者服务器->华为账号服务器
* **接口URL：** https://oauth-login.cloud.huawei.com/oauth2/v3/certs
* **数据格式：**

  响应消息：Content-Type: application/json;charset=utf-8

## 请求参数

无

## 请求示例

请通过POST方式调用，示例如下：

```
1. POST /oauth2/v3/certs HTTP/1.1
2. Host: oauth-login.cloud.huawei.com
```

请通过GET方式调用，示例如下：

```
1. GET /oauth2/v3/certs HTTP/1.1
2. Host: oauth-login.cloud.huawei.com
```

## 响应参数

### Response Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=utf-8。 |

### Response Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| keys | 是 | JSONArray | JWT公钥信息数组 |

keys数组每个元素中包含字段信息如下：

| **参数** | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| kty | 是 | String | JWK type，固定"RSA"。 |
| e | 是 | String | RSA算法e值。 |
| use | 是 | String | 标识密钥的预期用途：  sig：签名。 |
| kid | 是 | String | JWK唯一标识。 |
| alg | 是 | String | 算法类型，当前该字段值固定为"RS256"。 |
| n | 是 | String | RSA算法n值。 |

## 响应示例

```
1. HTTP/1.1 200 OK
2. Content-Type: application/json;charset=utf-8

4. {
5. "keys": [
6. {
7. "kty": "RSA",
8. "e": "AQAB",
9. "use": "sig",
10. "kid": "046fad4b211a9cbfbdc75debb4044901e029ba857c9d84f26f2839ba8aad22e8",
11. "alg": "RS256",
12. "n": "h_6JivtuClNwkUxMg******ZJKo239SANnkAfIgU6ECY5fxEZdIMBf7RJigO******uMuK064QfT0Dw"
13. },
14. {
15. "kty": "RSA",
16. "e": "AQAB",
17. "use": "sig",
18. "kid": "65f642e667650cc0db5bad81c6781c1f20b00c0ec977e89aaca964e9beafd5d2",
19. "alg": "RS256",
20. "n": "m8-SeDRLSd-Y02u******BbxzizQfSkEDLRjvksb74S2Bw2qQ82Er58******yoc0j2yujCRZTpiF9-w"
21. }
22. ]
23. }
```

## 示例代码

Java示例代码如下，运行前需要进行[示例代码环境配置](account-api-common.md#示例代码环境配置)（请将此示例代码与工具类CallUtils放于同一路径下，如不在同一路径，请手动添加import）

```
1. import com.alibaba.fastjson2.JSONArray;
2. import com.alibaba.fastjson2.JSONObject;
3. import org.apache.http.client.methods.HttpGet;
4. import java.io.IOException;

6. /**
7. * 获取验证ID Token的JWT公钥信息
8. */
9. public class GetIdTokenCerts {
10. public static void main(String[] args) throws IOException {
11. // 获取验证ID Token的JWT公钥信息的接口URL
12. String url = "https://oauth-login.cloud.huawei.com/oauth2/v3/certs";
13. JSONObject result = CallUtils.toJsonObject(CallUtils.remoteCallOAuth(new HttpGet(url)));
14. // 解析获取响应参数keys列表
15. JSONArray keys = result.getJSONArray("keys");
16. for (Object keyInfo : keys) {
17. // 获取keys中每个元素对象中的字段信息
18. JSONObject jsonObj = (JSONObject) keyInfo;
19. // 解析获取kty
20. String kty = jsonObj.getString("kty");
21. // 解析获取e
22. String e = jsonObj.getString("e");
23. // 解析获取use
24. String use = jsonObj.getString("use");
25. // 解析获取kid
26. String kid = jsonObj.getString("kid");
27. // 解析获取alg
28. String alg = jsonObj.getString("alg");
29. // 解析获取n
30. String n = jsonObj.getString("n");
31. }
32. }
33. }
```

## 错误码

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 成功。 | - |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的http请求method。 | 请检查http请求method是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 503 | 系统流控。 | 触发系统流控，请稍后重试。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 590 | 服务内部错误。 | 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
