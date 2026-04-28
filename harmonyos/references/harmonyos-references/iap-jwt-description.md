---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-jwt-description
title: 生成服务端请求的token
breadcrumb: API参考 > 应用服务 > IAP Kit（应用内支付服务） > REST API > 生成服务端请求的token
category: harmonyos-references
scraped_at: 2026-04-28T08:16:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1359213a01dce8677b6ab5a08445f52040c0736e33c52d4fbf67fba99401f218
---

服务端API请求的Authorization标头中必须包含JWT格式的token用于鉴权。JSON Web Token（JWT）是一个开放标准（RFC 7519），定义了一种安全传输信息的方法，具体请参见[jwt.io](https://jwt.io/)。可以使用从[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)下载的私钥签名生成JWT。密钥的生成和下载请参见[配置密钥](../harmonyos-guides/iap-set-necessary-parameters.md#配置密钥)。创建JWT格式的token需要以下几步：

1. 创建JWT Header
2. 创建JWT Payload
3. 创建JWT格式的token

## 创建JWT Header

Header参数如下：

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| alg | 是 | String | 算法类型，固定为ES256。 |
| typ | 是 | String | Token类型，固定为JWT。 |
| kid | 是 | String | 密钥ID，获取方式请参见[配置密钥](../harmonyos-guides/iap-set-necessary-parameters.md#配置密钥)。如果有多个密钥，请使用对JWT进行签名的同一私钥的密钥ID。 |

## 创建JWT Payload

JWT负载包含访问服务端API的一些关键信息，例如密钥颁发者ID、JWT签发时间和JWT到期时间等。JWT负载参数如下：

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| iss | 是 | String | 标识密钥颁发者ID（Issuer ID），获取方式请参见[配置密钥](../harmonyos-guides/iap-set-necessary-parameters.md#配置密钥)的说明。 |
| aud | 是 | String | JWT的预期接收者，固定为iap-v1。 |
| iat | 是 | Long | JWT签发时间，UTC时间戳，以秒为单位。 |
| exp | 是 | Long | JWT到期时间，UTC时间戳，以秒为单位。  （exp-iat）即为JWT的有效期，有效期不能超过1小时。 |
| aid | 是 | String | APP ID，获取方式参见[配置应用身份信息](../harmonyos-guides/iap-config-app-identity-info.md)。 |
| digest | 是 | String | Request Body（json字符串）的hash值，用于验证Request Body的完整性，算法为SHA-256。  **说明：** 如果Request Body为空，则传空字符串""的hash值。 |

## 创建JWT格式的token

使用Header中指定的算法（ES256）以及密钥ID关联的私钥进行签名生成JWT，可以使用各种开源库来创建JWT格式的token，具体请参见[jwt.io](https://jwt.io/)。

### 代码示例

说明

以下示例代码仅以Java语言为例，Python、PHP、JS、Golang语言示例代码可通过在[IAP Kit-Sample-ServerDemo](https://gitcode.com/HarmonyOS_Samples/iapkit-sample-serverdemo)中切换代码分支查看。

```
1. import com.auth0.jwt.JWT;
2. import com.auth0.jwt.algorithms.Algorithm;
3. import java.nio.charset.StandardCharsets;
4. import java.nio.file.Files;
5. import java.nio.file.Path;
6. import java.nio.file.Paths;
7. import java.security.KeyFactory;
8. import java.security.interfaces.ECPrivateKey;
9. import java.security.spec.PKCS8EncodedKeySpec;
10. import java.time.Duration;
11. import java.util.Base64;
12. import java.util.HashMap;
13. import java.util.Map;
14. import org.apache.commons.codec.digest.DigestUtils;

16. public class JWTGenerator {
17. /**
18. * Private key file path.
19. * For key generation and download, please refer to Configuring Keys.
20. */
21. private static final String JWT_PRI_KEY_PATH = "/path/to/key/priKey.p8"; // TODO: Need to replace it with the actual value.

23. /**
24. * JWT validity period, which is a UTC timestamp in seconds. The validity period cannot exceed 1 hour.
25. */
26. private static final long ACTIVE_TIME_SECOND = 3600;  // TODO: Need to replace it with the actual value.

28. private static final Map<String, Object> JWT_HEADER = new HashMap<>();

30. private static final Map<String, Object> JWT_PAYLOAD = new HashMap<>();

32. static {
33. // Algorithm type. The value is always ES256.
34. JWT_HEADER.put("alg", "ES256");
35. // Token type. The value is always JWT.
36. JWT_HEADER.put("typ", "JWT");
37. // Key ID.
38. JWT_HEADER.put("kid", "Key ID");  // TODO: Need to replace it with the actual value.

40. // Key issuer ID.
41. JWT_PAYLOAD.put("iss", "Issuer ID");  // TODO: Need to replace it with the actual value.
42. // Expected receiver of the JWT. The value is fixed at iap-v1.
43. JWT_PAYLOAD.put("aud", "iap-v1");
44. // Time when the JWT is issued. The value is a UTC timestamp, in seconds.
45. // Re-put the value in the genJwt method.
46. JWT_PAYLOAD.put("iat", 0);
47. // Time when the JWT expires. The value is a UTC timestamp, in seconds. exp-iat indicates the validity period of the JWT, which cannot exceed one hour.
48. // Re-put the value in the genJwt method.
49. JWT_PAYLOAD.put("exp", 0);
50. // App ID.
51. JWT_PAYLOAD.put("aid", "App ID");  // TODO: Need to replace it with the actual value.
52. // Hash value of the request body (JSON character string), which is used to verify the integrity of the body. The algorithm is SHA-256.
53. JWT_PAYLOAD.put("digest", "");
54. }

56. public static String genJwt(String bodyStr) throws Exception {
57. try {
58. // Fetch the Private Key Content in PEM format.
59. Path filePath = Paths.get(JWT_PRI_KEY_PATH);
60. String fileString = new String(Files.readAllBytes(filePath), StandardCharsets.UTF_8);
61. String privateKey = fileString.replace("-----BEGIN PRIVATE KEY-----", "")
62. .replaceAll("\\R+", "")
63. .replace("-----END PRIVATE KEY-----", "");
64. KeyFactory keyFactory = KeyFactory.getInstance("EC");
65. byte[] privateKeyBytes = Base64.getDecoder().decode(privateKey);
66. PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(privateKeyBytes);
67. ECPrivateKey ecPrivateKey = (ECPrivateKey) keyFactory.generatePrivate(keySpec);
68. Map<String, Object> jwtPayload = new HashMap<>(JWT_PAYLOAD);
69. long signTime = System.currentTimeMillis() / Duration.ofSeconds(1).toMillis();
70. String digest = DigestUtils.sha256Hex(bodyStr);
71. jwtPayload.put("iat", signTime);
72. jwtPayload.put("exp", signTime + ACTIVE_TIME_SECOND);
73. jwtPayload.put("digest", digest);
74. return JWT.create().withHeader(JWT_HEADER).withPayload(jwtPayload).sign(Algorithm.ECDSA256(ecPrivateKey));
75. } catch (Exception e) {
76. // TODO: Need to replace it with the actual business logic.
77. throw new Exception(e);
78. }
79. }
80. }
```

pom文件

```
1. <dependency>
2. <groupId>com.auth0</groupId>
3. <artifactId>java-jwt</artifactId>
4. <version>4.4.0</version>
5. </dependency>
```

## Authorization说明

调用服务端API请求时，请求Header使用 Authorization: Bearer <JWT格式的token>传递鉴权信息，样例如下：

```
1. Authorization: Bearer eyJhbGciOi---xxx.eyJpc3MiOm---xxx.WFquGEx5gf---xxx
```
