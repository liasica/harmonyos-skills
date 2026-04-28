---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-server-subscribe-offer-sign
title: 生成优惠签名购买参数
breadcrumb: API参考 > 应用服务 > IAP Kit（应用内支付服务） > REST API > 生成优惠签名购买参数
category: harmonyos-references
scraped_at: 2026-04-28T08:16:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:599209c0d82ba330a028e6ec2d4c67a38db60e2148d8de99ec5c31e0214c138e
---

开发者在促销优惠场景下需要传入JWT格式的jwsRepresentation参数，该参数包含购买订单涉及的优惠及商品信息。JSON Web Token（JWT）是一个开放标准（RFC 7519），定义了一种安全传输信息的方法，具体请参见[jwt.io](https://jwt.io/)。开发者可以使用从[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)下载的私钥签名生成JWT。密钥生成和下载请参见[配置密钥](../harmonyos-guides/iap-set-necessary-parameters.md#配置密钥)。创建JWT格式的签名购买参数需要以下几步：

1. 创建JWT Header
2. 创建JWT Payload
3. 创建JWT格式的signature

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
| aud | 是 | String | JWT的预期接收者，确保JWT是针对其自身的，固定为iap-v1。 |
| iat | 是 | Long | JWT签发时间，UTC时间戳，以秒为单位。 |
| exp | 是 | Long | JWT到期时间，UTC时间戳，以秒为单位。  （exp-iat）即为JWT的有效期，有效期不能超过1小时。 |
| aid | 是 | String | APP ID，获取方式参见[配置应用身份信息](../harmonyos-guides/iap-config-app-identity-info.md)。 |
| data | 是 | String | 优惠信息扩展信息，为[PurchaseReservedInfo](iap-server-data-model.md#purchasereservedinfo)结构的Json字符串。 |

## 创建JWT格式的signature

使用Header中指定的算法（ES256）以及密钥ID关联的私钥进行签名生成JWT，可以使用各种开源库来创建JWT格式的token，具体请参见[jwt.io](https://jwt.io/)。

### 代码示例

```
1. import com.auth0.jwt.JWT;
2. import com.auth0.jwt.algorithms.Algorithm;

4. import java.security.KeyFactory;
5. import java.security.NoSuchAlgorithmException;
6. import java.security.interfaces.ECPrivateKey;
7. import java.security.spec.InvalidKeySpecException;
8. import java.security.spec.PKCS8EncodedKeySpec;
9. import java.util.Base64;
10. import java.util.Map;

12. public class JwsRepresentationGenerator {
13. public static String createJwsRepresentation(String signingKey, Map<String, Object> jwtHeader,
14. Map<String, Object> jwtPayload) {
15. try {
16. // Configure a key and download the private key file in AppGallery Connect.
17. byte[] derEncodedSigningKey = Base64.getDecoder().decode(signingKey);
18. KeyFactory keyFactory = KeyFactory.getInstance("EC");
19. PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(derEncodedSigningKey);
20. ECPrivateKey ecPrivateKey = (ECPrivateKey) keyFactory.generatePrivate(keySpec);
21. return JWT.create().withHeader(jwtHeader).withPayload(jwtPayload).sign(Algorithm.ECDSA256(ecPrivateKey));
22. } catch (NoSuchAlgorithmException | InvalidKeySpecException e) {
23. // TODO: Need to replace it with the actual business logic.
24. throw new RuntimeException(e);
25. }
26. }
27. }
```
