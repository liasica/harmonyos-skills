---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-verifying-signature
title: 对返回结果验签
breadcrumb: API参考 > 应用服务 > IAP Kit（应用内支付服务） > REST API > 对返回结果验签
category: harmonyos-references
scraped_at: 2026-04-28T08:16:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:61ace9862de2d6e8df17e6fd8b381e749cda1dccb4840e5785ffcc6a18759237
---

## 功能介绍

IAP服务器API返回结果以及服务端关键事件通知返回的是JSON Web Signature （JWS）格式的数据。JWS的主要目的是保证了数据在传输过程中不被修改，验证数据的完整性。

## JWS结构

JWS由三部分组成：

1. Header（头部）
2. Payload（负载）
3. Signature（签名）

在传输的时候，将JWS的三部分分别进行Base64编码。

解码后的Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| alg | 是 | String | 算法类型，固定为ES256。 |
| typ | 是 | String | 固定为JWT。 |
| x5c | 是 | String | X.509 证书链，顺序为叶子证书、中间证书、根证书。 |

## JWS解码和验签

1. 解析JWS，获取Header、 Payload和Signature。
2. 从header的x5c中获取证书链（依次是叶子证书、中间证书、根证书），使用[Huawei CBG Root CA G2](https://pki.consumer.huawei.com/ca/cer/RootCaG2Ecdsa.cer)证书对证书链进行验证。
3. 校验叶子证书的OID：1.3.6.1.4.1.2011.2.415.1.1。
4. 证书校验通过则从叶子证书获取到PublicKey。
5. 通过Header指定的算法和PublicKey进行JWT验签，可以使用各种开源库来验签，具体请参见[jwt.io](https://jwt.io/)。

## JWS解码和验签示例

说明

以下示例代码仅以Java语言为例，Python、PHP、JS、Golang语言示例代码可通过在 **[IAP Kit-Sample-ServerDemo](https://gitcode.com/HarmonyOS_Samples/iapkit-sample-serverdemo)** 中切换代码分支查看。

```
1. import com.auth0.jwt.JWT;
2. import com.auth0.jwt.JWTVerifier;
3. import com.auth0.jwt.algorithms.Algorithm;
4. import com.auth0.jwt.interfaces.DecodedJWT;
5. import java.io.ByteArrayInputStream;
6. import java.io.InputStream;
7. import java.nio.charset.StandardCharsets;
8. import java.nio.file.Files;
9. import java.nio.file.Paths;
10. import java.security.PublicKey;
11. import java.security.cert.CertPath;
12. import java.security.cert.CertPathValidator;
13. import java.security.cert.CertPathValidatorException;
14. import java.security.cert.Certificate;
15. import java.security.cert.CertificateFactory;
16. import java.security.cert.PKIXCertPathValidatorResult;
17. import java.security.cert.PKIXParameters;
18. import java.security.cert.TrustAnchor;
19. import java.security.cert.X509Certificate;
20. import java.security.interfaces.ECPublicKey;
21. import java.util.Base64;
22. import java.util.HashSet;
23. import java.util.LinkedList;
24. import java.util.List;
25. import java.util.Set;

27. public class JWSChecker {
28. private static final String CA_CERT_FILE_PATH = "/path/to/cer/RootCaG2Ecdsa.cer";// TODO: Need to replace it with the actual value, please refer to Huawei CBG Root CA G2.

30. /**
31. * JWS HEADER PARAM X5C: Indicates the X.509 certificate chain. The sequence is leaf certificate, intermediate certificate, and root certificate.
32. */
33. private static final String HEADER_PARAM_X5C = "x5c";

35. private static final int X5C_CHAIN_LENGTH = 3;

37. /**
38. * JWS HEADER PARAM ALG: Algorithm type. The value is always ES256.
39. */
40. private static final String HEADER_PARAM_ALG_ES256 = "ES256";

42. private static final String LEAF_CERT_OID = "1.3.6.1.4.1.2011.2.415.1.1";

44. /**
45. * Used to verify JWS and decode the payload.
46. * @param jwsStr JWS string
47. * @return payload string
48. * @throws Exception exception
49. */
50. public static String checkAndDecodeJWS(String jwsStr) throws Exception {
51. if (jwsStr == null || jwsStr.isEmpty()) {
52. // TODO: Need to replace it with the actual business logic.
53. throw new Exception("jwsStr was null");
54. }
55. DecodedJWT decodedJWT = JWT.decode(jwsStr);
56. if (!HEADER_PARAM_ALG_ES256.equals(decodedJWT.getAlgorithm())) {
57. // TODO: Need to replace it with the actual business logic.
58. throw new Exception("alg must be ES256");
59. }
60. String[] x5cChain = decodedJWT.getHeaderClaim(HEADER_PARAM_X5C).asArray(String.class);
61. if (x5cChain == null) {
62. // TODO: Need to replace it with the actual business logic.
63. throw new Exception("x5c chain was null");
64. }
65. // Verify the x5c certificate chain and obtain the public key.
66. PublicKey publicKey = verifyChainAndGetPubKey(x5cChain);
67. // Use the public key to verify the signature of the jws.
68. JWTVerifier jwtVerifier = JWT.require(Algorithm.ECDSA256((ECPublicKey) publicKey)).build();
69. jwtVerifier.verify(decodedJWT);
70. // Decode and return the payload.
71. return new String(Base64.getUrlDecoder().decode(decodedJWT.getPayload()), StandardCharsets.UTF_8);
72. }
73. private static PublicKey verifyChainAndGetPubKey(String[] certificates) throws Exception {
74. CertificateFactory certificateFactory = CertificateFactory.getInstance("X.509");
75. List<Certificate> certificateList = new LinkedList<>();
76. for (String certificate : certificates) {
77. InputStream inputStream = new ByteArrayInputStream(Base64.getDecoder().decode(certificate));
78. certificateList.add(certificateFactory.generateCertificate(inputStream));
79. }
80. if (certificateList.size() != X5C_CHAIN_LENGTH) {
81. // TODO: Need to replace it with the actual business logic.
82. throw new Exception("invalid cert chain length");
83. }
84. PKIXCertPathValidatorResult certPathValidatorResult;
85. try {
86. PKIXParameters parameters = loadRootCAAndPKIX();
87. CertPathValidator validator = CertPathValidator.getInstance("PKIX");

89. // TODO: Need to do crl check if not ignore CRL
90. parameters.setRevocationEnabled(false);
91. CertPath certPath = certificateFactory.generateCertPath(certificateList.subList(0, X5C_CHAIN_LENGTH - 1));
92. certPathValidatorResult = (PKIXCertPathValidatorResult) validator.validate(certPath, parameters);
93. } catch (Exception e) {
94. // TODO: Need to replace it with the actual business logic.
95. throw new Exception(e);
96. }
97. Certificate iapCert = certificateList.get(0);
98. if (!(iapCert instanceof X509Certificate)) {
99. // TODO: Need to replace it with the actual business logic.
100. throw new Exception("leaf certificate must be X509 format");
101. }
102. X509Certificate x509Certificate = (X509Certificate) iapCert;
103. if (x509Certificate.getNonCriticalExtensionOIDs() == null ||
104. !x509Certificate.getNonCriticalExtensionOIDs().contains(LEAF_CERT_OID)) {
105. // TODO: Need to replace it with the actual business logic.
106. throw new CertPathValidatorException("OID not found");
107. }
108. return certPathValidatorResult.getPublicKey();
109. }
110. private static PKIXParameters loadRootCAAndPKIX() throws Exception {
111. PKIXParameters parameters;
112. // TODO: Under Java 8, Need to close the resource in the finally block.
113. try (InputStream fis = Files.newInputStream(Paths.get(CA_CERT_FILE_PATH))) {
114. CertificateFactory certificateFactory = CertificateFactory.getInstance("X.509");
115. Certificate trustCert = certificateFactory.generateCertificate(fis);
116. if (!(trustCert instanceof X509Certificate)) {
117. // TODO: Need to replace it with the actual business logic.
118. throw new RuntimeException("root certificate must be X509 format");
119. }
120. Set<TrustAnchor> trustAnchors = new HashSet<>();
121. trustAnchors.add(new TrustAnchor((X509Certificate) trustCert, null));
122. parameters = new PKIXParameters(trustAnchors);
123. }
124. return parameters;
125. }
126. }
```

pom文件

```
1. <dependency>
2. <groupId>com.auth0</groupId>
3. <artifactId>java-jwt</artifactId>
4. <version>4.4.0</version>
5. </dependency>
```
