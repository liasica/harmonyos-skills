---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-token
title: 基于服务账号生成鉴权令牌
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 开发准备 > 基于服务账号生成鉴权令牌
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8b5d6ed14ac401f0fd7308c078d1b854fe01fc99fbff127f5115a0574f91204c
---

注意

只有使用应用设备状态检测服务时才需要配置此章节。

## 概述

服务账号（Service Account）是一种可实现服务器与服务器之间接口鉴权的账号，在华为开发者联盟的[API Console](https://developer.huawei.com/consumer/cn/console/overview)上创建服务账号，您可根据返回的公私钥在业务应用中生成鉴权令牌，调用支持此类鉴权的华为公开API。

服务账号令牌为JWT（JSON Web Token）格式字符串，JWT数据格式包括三个部分：

* Header（头部）
* Payload（负载）
* Signature（签名）

这三个部分通过“.”进行连接，其中Signature为通过SHA256withRSA算法对Header与Payload拼接的字符串签名生成的字符串。

**示例**

```
1. eyJra*****JjNjBjMXXX.
2. eyJhd*****JodHRXXX.
3. BRNss*****7az5oU7-Zp5g9X2WJVXXX
```

更多JWT的相关知识请参见[Introduction to JSON Web Tokens](https://jwt.io/introduction/)。

## 开发步骤

1. 创建服务账号密钥文件。

   开发者需要在华为开发者联盟的[API Console](https://developer.huawei.com/consumer/cn/console/overview)上创建并下载服务账号的密钥文件，相关创建步骤请参见[API Console操作指南-服务账号密钥](../start/api-0000001062522591.md#section91275725415)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/rs1eAJrYQ0uUtS6DeJvvVw/zh-cn_image_0000002552958384.png?HW-CC-KV=V1&HW-CC-Date=20260427T234252Z&HW-CC-Expire=86400&HW-CC-Sign=C92727BC6DB2EC454F9D3426F3A9BE829296F74D85AEFE14034F0B009AB403CF)

   说明

   您在开发者联盟需要申请开发者级的服务账号凭证。

   服务账号密钥样例文件形式可参考：

   ```
   1. {
   2. "project_id": "*****",
   3. "key_id": "*****",
   4. "private_key": "-----BEGIN PRIVATE KEY-----\nMIIJQgIBADANBgkqhkiG9w0BAQEFAASCCSwwggkoAgEAAoICAQCKw6kJKtCh7qmMvp1u1dI27z2TKZrPOzHbQaXO/Eez0AWZ2EN+ouF496R3pfo7fQXC1XOT/YTbVC4DNZwWSMA54fu3/AOCY9Zzyi46OK*****==\n-----END PRIVATE KEY-----\n",
   5. "sub_account": "*****",
   6. "auth_uri": "https://oauth-login.cloud.huawei.com/oauth2/v3/authorize",
   7. "token_uri": "https://oauth-login.cloud.huawei.com/oauth2/v3/token",
   8. "auth_provider_cert_uri": "https://oauth-login.cloud.huawei.com/oauth2/v3/certs",
   9. "client_cert_uri": "https://oauth-login.cloud.huawei.com/oauth2/v3/x509?client_id=*****"
   10. }
   ```
2. 生成JWT Header数据。

   根据服务账号密钥文件中的key\_id字段拼接以下JSON体，对JSON体进行BASE64编码。

   ```
   1. {
   2. "kid": "*****",
   3. "typ": "JWT",
   4. "alg": "PS256"
   5. }
   ```

   | 字段名 | 描述 |
   | --- | --- |
   | kid | 服务账号密钥文件中key\_id字段。 |
   | typ | 数据类型，固定为：JWT。 |
   | alg | 算法类型，固定为：PS256。 |
3. 生成JWT Payload数据。

   根据服务账号密钥文件中的sub\_account字段拼接以下JSON体，对JSON体进行BASE64编码。

   ```
   1. {
   2. "aud": "https://oauth-login.cloud.huawei.com/oauth2/v3/token",
   3. "iss": "*****",
   4. "exp": 1581410664,
   5. "iat": 1581407064
   6. }
   ```

   | 字段名 | 描述 |
   | --- | --- |
   | aud | 固定为：https://oauth-login.cloud.huawei.com/oauth2/v3/token。 |
   | iss | 服务账号密钥文件中sub\_account字段，标识数据生成者。 |
   | exp | JWT到期UTC时间戳，建议比“iat”晚3600秒。 |
   | iat | JWT签发UTC时间戳，为自UTC时间1970年1月1日00:00:00的秒数（应用服务器时间需要校准为标准时间）。 |
4. 生成JWT Token数据。

   将完成BASE64编码后的Header字符串与Payload字符串，通过“.”进行连接，并在开发者的应用中，通过服务账号密钥文件中的private\_key（华为不进行存储，请您妥善保管），使用SHA256withRSA/PSS算法对拼接的字符串签名，最后将Header，Payload以及字符串签名通过“.”进行连接，即可得到Token数据。

## 示例代码

为了方便您生成服务账号鉴权令牌，我们提供了Java语言的示例代码，请按照说明替换参数运行。

如果您使用其他开发语言，请选择对应的[JWT开源组件](https://www.jwt.io/libraries)进行开发。

```
1. import com.alibaba.fastjson.JSONObject;
2. import org.apache.commons.codec.binary.Base64;
3. import org.bouncycastle.jce.provider.BouncyCastleProvider;

5. import java.nio.charset.StandardCharsets;
6. import java.security.*;
7. import java.security.spec.InvalidKeySpecException;
8. import java.security.spec.PKCS8EncodedKeySpec;
9. import java.util.Objects;

11. public class JWTGenerateDemo_test {
12. // please replace it with the private_key in your json file
13. // this is the plain text in this demo, please encrypt the private key in your code, only get the string between
14. // '-----BEGIN PRIVATE KEY-----\n' and '\n-----END PRIVATE KEY-----\n'
15. private static final String PRIVATE_KEY = "xxxx";

17. // please replace it with the sub_account in your json file
18. private static final String ISS = "xxx";

20. // please replace it with the key_id in your json file
21. private static final String KID = "xxx";

23. private static final String AUD = "https://oauth-login.cloud.huawei.com/oauth2/v3/token";

25. private static final String ALG_PS256 = "PS256";

27. private static final String DOT = ".";

29. private static PrivateKey getPrivateKey(String key) throws NoSuchAlgorithmException, InvalidKeySpecException {
30. PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(decodeBase64(key));
31. KeyFactory keyFactory = KeyFactory.getInstance("RSA");
32. return keyFactory.generatePrivate(keySpec);
33. }

35. private static byte[] decodeBase64(String Base64Str) {
36. return Base64.decodeBase64(Base64Str.getBytes(StandardCharsets.UTF_8));
37. }

39. private String createJwt()
40. throws NoSuchAlgorithmException, InvalidKeySpecException, InvalidKeyException, SignatureException {
41. long iat = System.currentTimeMillis() / 1000;
42. long exp = iat + 3600;//JWT有效期3600s

44. // jwt header
45. JSONObject header = new JSONObject();
46. header.put("alg", ALG_PS256);
47. header.put("kid", KID);
48. header.put("typ", "JWT");

50. // jwt payload
51. JSONObject payload = new JSONObject();
52. payload.put("aud", AUD);
53. payload.put("iss", ISS);
54. payload.put("exp", exp);
55. payload.put("iat", iat);

57. // jwt signature
58. byte[] encodeHeaderBytes = Base64.encodeBase64URLSafe(header.toString().getBytes(StandardCharsets.UTF_8));
59. byte[] encodePayloadBytes = Base64.encodeBase64URLSafe(payload.toString().getBytes(StandardCharsets.UTF_8));
60. String encodeHeader = new String(encodeHeaderBytes, StandardCharsets.UTF_8);
61. String encodePayload = new String(encodePayloadBytes, StandardCharsets.UTF_8);
62. String jwtHeaderAndPayload = encodeHeader + DOT + encodePayload;
63. Signature signatureInstance = Signature.getInstance("SHA256withRSA/PSS", new BouncyCastleProvider());
64. signatureInstance.initSign(getPrivateKey(PRIVATE_KEY));
65. signatureInstance.update(jwtHeaderAndPayload.getBytes(StandardCharsets.UTF_8));
66. String signature =
67. new String(Objects.requireNonNull(Base64.encodeBase64URLSafe(signatureInstance.sign())), StandardCharsets.UTF_8);

69. return jwtHeaderAndPayload + DOT + signature;
70. }

72. public static void main(String args[])
73. throws InvalidKeySpecException, NoSuchAlgorithmException, SignatureException, InvalidKeyException {
74. JWTGenerateDemo_test JWTGenerateDemo = new JWTGenerateDemo_test();
75. JWTGenerateDemo.createJwt();//获取鉴权令牌
76. }
77. }
```

执行main()函数即可。

推荐的java版本为java8，maven依赖如下：

```
1. <dependency>
2. <groupId>com.alibaba</groupId>
3. <artifactId>fastjson</artifactId>
4. <version>1.2.83</version>
5. </dependency>
6. <dependency>
7. <groupId>org.bouncycastle</groupId>
8. <artifactId>bcprov-jdk18on</artifactId>
9. <version>1.74</version>
10. </dependency>
11. <dependency>
12. <groupId>commons-codec</groupId>
13. <artifactId>commons-codec</artifactId>
14. <version>1.15</version>
15. </dependency>
```
