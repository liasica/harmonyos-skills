---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/device-attestation-servers
title: 服务器端开发
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 应用真实性证明 > 创建密钥确立可信凭证 > 服务器端开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a21990aa7710689947252e57cf6d24297d3c98c05b9ba3720bc930809f69af64
---

## 校验密钥证明证书链

您的应用服务器接收到来自应用的请求，其中包含的密钥证明证书链采用X509标准格式，证书链（证书数组）中的第一本证书为**密钥证明证书**，最后一本证书为根CA证书，中间的为子CA证书。

应用服务器对密钥证明证书链的校验步骤如下：

1. 使用官网提供的可信的根CA证书对证书链合法性进行校验。（[根CA证书下载地址](https://pki.consumer.huawei.com/ca/cer/Huawei_CBG_ECC_Device_Attestation_Root_CA.cer)）

   说明

   请勿在应用服务器中使用子CA证书对密钥证明证书链进行校验，子CA证书可能会因为有效期结束、证书被吊销等发生变化。
2. 解析**密钥证明证书**获取应用公钥、挑战值Challenge、应用ID、密钥管理部件ID。

   其中应用公钥直接从密钥证明证书的subjectPublicKeyInfo字段获取；其他字段从密钥证明证书的扩展域段（Extensions）中获取，扩展域段的OID为1.3.6.1.4.1.2011.2.376.1.3（密钥证明扩展域段）。
3. 校验挑战值Challenge是否与“创建密钥确立可信凭证流程”步骤3中应用服务器缓存的挑战值Challenge一致。
4. 校验应用ID是否与预期的取值一致。根据应用ID判断请求是否来自预期的HarmonyOS应用。
5. 校验密钥来源是否与预期的取值一致。

**密钥证明证书格式说明：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/lyJu21HFT_GuP36HLYSTvw/zh-cn_image_0000002583438459.png?HW-CC-KV=V1&HW-CC-Date=20260427T234324Z&HW-CC-Expire=86400&HW-CC-Sign=FD920FBD91FFF92AA2C5EEC3C9B1A40F04A72FA1F355A6D2D04BDA6F51797E6E)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/hEVqkkwfQhKrSwoimpxCsg/zh-cn_image_0000002552958414.png?HW-CC-KV=V1&HW-CC-Date=20260427T234324Z&HW-CC-Expire=86400&HW-CC-Sign=93589753233F431A7A8EF38C9B701316BFAB299F6723E7AE127FF79BD2CD84C9)

密钥证明扩展域段为Asn.1 DER标准编码格式，数据结构定义如下：

```
1. HuaweiAttestation ::= SEQUENCE {
2. version             AttestationVersion DEFAULT v1,
3. claim1             AttestationClaim,
4. claim2             AttestationClaim,
5. claim3             AttestationClaim,
6. ... ...
7. }

9. AttestationVersion ::= INTEGER { v1(0) }

11. AttestationClaim ::= SEQUENCE {
12. securityLevel       SecurityLevel,
13. type             AttestationType,
14. value            AttestationValue
15. }

17. SecurityLevel ::= INTEGER
18. AttestationType ::= OBJECT IDENTIFIER
19. AttestationValue ::= ANY -- DEFINED BY AttestationType

21. ApplicationIDType ::= SEQUENCE {
22. type                         OBJECT IDENTIFIER,
23. value                        OCT_STR
24. }
```

**AttestationClaim类型取值说明：**

| 序号 | type（OID）取值 | value的数据类型 | securityLevel | Claim说明 |
| --- | --- | --- | --- | --- |
| 1 | 1.3.6.1.4.1.2011.2.376.2.1.4 | OCT\_STR | 保留字段，暂不使用 | 应用输入的挑战值Challenge。 |
| 2 | 1.3.6.1.4.1.2011.2.376.2.1.3 | ApplicationIDType | 保留字段，暂不使用 | 应用ID。 |
| 3 | 1.3.6.1.4.1.2011.2.376.2.2.2.6 | OCT\_STR | 保留字段，暂不使用 | 密钥管理部件ID。取值固定为：0x28c4fb4944afec11b9090242ac120002（Universal Keystore Kit的部件ID）。 |
| 4 | 1.3.6.1.4.1.2011.2.376.2.2.4.8 | UTF8String | 2 | 设备产品型号，从API version 20开始支持。设备产品型号一般应用在设备风控场景，识别黑灰产设备的行为，请勿使用该字段对设备身份进行认证。 |

**securityLevel类型取值说明：**

| securityLevel | 说明 |
| --- | --- |
| 2 | REE（Rich Execution Environment），数据来源于HarmonyOS系统层。 |
| 3 | TEE（Trusted Execution Environment），数据通过TEE进行保护。 |

**ApplicationIDType类型取值说明：**

| type（OID）取值 | value取值说明 |
| --- | --- |
| 1.3.6.1.4.1.2011.2.376.2.1.3.1 | HarmonyOS Hap应用信息，包含如下字段：  1. appId：包含Hap应用的bundleName和签名证书公钥的hash；  2. bundleName：Hap应用的包名；  3. appIdentifier：AppGallery Connect网站上为Hap应用分配的统一APP ID字段，从API version 20开始支持；  4. appMode：Hap应用的状态，取值：debug或release，从API version 20开始支持。  value为json字符串，样例如下：  {  "appId":"com.example.attesthcts\_BDmjsOezxRmguzlYRVhQavW22Eswi5sX61wOAysWPOGS8TZ5tY1u1A9EcvarzyrfOEj5zT8BCGkfFkVjn0m5wzo=",  "bundleName":"com.example.attesthcts",  "appIdentifier":"5765880207853009781",  "appMode":"release"  } |
| 1.3.6.1.4.1.2011.2.376.2.1.3.2 | 系统服务（Service Ability）的ID，样例：  {processName: "huawei\_share"} |

**示例：**

```
1. import org.bouncycastle.asn1.*;
2. import org.bouncycastle.jce.provider.BouncyCastleProvider;

4. import java.io.ByteArrayInputStream;
5. import java.io.FileOutputStream;
6. import java.security.PublicKey;
7. import java.security.Security;
8. import java.security.cert.CertPath;
9. import java.security.cert.CertPathValidator;
10. import java.security.cert.CertificateFactory;
11. import java.security.cert.PKIXCertPathValidatorResult;
12. import java.security.cert.PKIXParameters;
13. import java.security.cert.TrustAnchor;
14. import java.security.cert.X509Certificate;
15. import java.util.ArrayList;
16. import java.util.Date;
17. import java.util.HashSet;
18. import java.util.List;

20. import com.alibaba.fastjson.JSON;

22. public class ParseAttestation {
23. static {
24. Security.addProvider(new BouncyCastleProvider());
25. }

27. //HarmonyOS Hap应用通过anonAttestKeyItem接口获取到的 “密钥证明证书链”数据
28. static String[] g_attestCertStr = new String[]{"-----BEGIN CERTIFICATE-----\nMIIEUDCCA/WgAwIBAgIOCfv5Xf9hjA2u32gjpG8wCgYIKoZIzj0EAwIwXTE5MDcGA1UEAwwwSHVhd2VpIENCRyBFQ0MgRGV2aWNlIEFub255bW91cyBBdHRlc3RhdGlvbiBDQSAxMRMwEQYDVQQKDApIdWF3ZWkgQ0JHMQswCQYDVQQGEwJDTjAeFw0yNTA1MTMwNjI3NDlaFw0yNTA1MjAwNjI3NDlaMCwxKjAoBgNVBAMMIURldmljZSBDZXJ0aWZpY2F0ZSBNYW5hZ2VtZW50IEtleTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALd0wgFgvDF5uPq2hh69LdRHnIX3+mzdAzf10L9Jk6bWPZqqTvz88ZX7e12Su1Myf5iyT3TMKjZ+Y2SnsWpHG/7Dpx990u7/CxeeRY0qziIqMTEbrLFaSHY++///9SxmEiM7a3z2Ged2FzDSvOTj1JVmm2hk+bUcceTVuHAmRwidFIQrL5h/lxaO3uPFqbTdiW6ocz06pEbi8mg6LAafik1pfsO30a3yIGiH1f4uZhCEFjHQxQdSFsRPh04Ehclx6lQ196tO0d3RHR8dxL7ghGNxs9rB1Sq/0TH2mK1vKAY/YgvBs5nypOnDY+0MXN7j5NucvJ32wssGI7CbmMxVeZMCAwEAAaOCAf0wggH5MB0GA1UdDgQWBBQA6HLpfdJvtiqPqQXenry8b6qjYzAMBgNVHRMBAf8EAjAAMAkGA1UdOAQCBQAwHwYDVR0jBBgwFoAU4yzL/3aHOxL7QyI/P/sCBoHfJ6cwggGcBgwrBgEEAY9bAoJ4AQMEggGKMIIBhgIBADCB/AIBAgYNKwYBBAGPWwKCeAIBAzCB5wYOKwYBBAGPWwKCeAIBAwEEgdR7ImFwcElkIjoiY29tLmV4YW1wbGUubXlhcHBsaWNhdGlvbl9CS3BOWWR2UU0yYkNLYklwRERuWmdkdGNYdEtnZUg5M2FwVm1aOWdpcTFoeUt2elNzVVNFZTFsT3VsK3N2bXhZS2ltb0dNWnF0U0o3eGxpRkVZd2NRK0E9IiwiYnVuZGxlTmFtZSI6ImNvbS5leGFtcGxlLm15YXBwbGljYXRpb24iLCJhcHBJZGVudGlmaWVyIjoiMTU3MzU0NjgiLCJhcHBNb2RlIjoiZGVidWcifTAiAgEABg0rBgEEAY9bAoJ4AgEEBA5jaGFsbGVuZ2VfZGF0YTAYAgEDBg0rBgEEAY9bAoJ4AgEFBAQCAAAAMB0CAQIGDisGAQQBj1sCgngCAgQIDAhDTFMtQUwwMDAlAgEDBg4rBgEEAY9bAoJ4AgICBgQQKMT7SUSv7BG5CQJCrBIAAjAKBggqhkjOPQQDAgNJADBGAiEAko1y6sf7Fg48oWZC8FoP5WtmzKiVk5AOOvuhwaK0CQcCIQD8HymOzkzmOOjUuz/rdVrTM4191dpGr3jfU1u5rBpNIw==\n-----END CERTIFICATE-----", "-----BEGIN CERTIFICATE-----\nMIICyjCCAlCgAwIBAgIREj5jzbLehL8yzkDm5uwcSJUwCgYIKoZIzj0EAwMwSzETMBEGA1UEChMKSHVhd2VpIENCRzE0MDIGA1UEAxMrSHVhd2VpIENCRyBFQ0MgRGV2aWNlIEF0dGVzdGF0aW9uIFJvb3QgQ0EgMTAeFw0yMzEyMDUwMzE4MDRaFw0zMzEyMDUwMzE4MDRaMF0xOTA3BgNVBAMMMEh1YXdlaSBDQkcgRUNDIERldmljZSBBbm9ueW1vdXMgQXR0ZXN0YXRpb24gQ0EgMTETMBEGA1UECgwKSHVhd2VpIENCRzELMAkGA1UEBhMCQ04wWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATYjeQrfijuZ/9HJPLlsfJ4/wnXbQXaxy5f5fEcMN+pTZ5RekpY7PnDp2zEdibvkSzjv1MuRs8JzORyGatSOrYFo4IBATCB/jAfBgNVHSMEGDAWgBTaRGLD5yvof1E6XEuPQ3w5JMPOrDAdBgNVHQ4EFgQU4yzL/3aHOxL7QyI/P/sCBoHfJ6cwRgYDVR0gBD8wPTA7BgRVHSAAMDMwMQYIKwYBBQUHAgEWJWh0dHA6Ly9wa2kuY29uc3VtZXIuaHVhd2VpLmNvbS9jYS9jcHMwEgYDVR0TAQH/BAgwBgEB/wIBATAOBgNVHQ8BAf8EBAMCAQYwUAYDVR0fBEkwRzBFoEOgQYY/aHR0cDovL3BraS5jb25zdW1lci5odWF3ZWkuY29tL2NhL2NybC9yb290X2RldmljZUF0dGVzdF9jcmwuY3JsMAoGCCqGSM49BAMDA2gAMGUCMQCE9qqNREq3AvCuznKeBl8biwC5GpV/Z1B0rsU4RqeTqNJ0Gvyz3g8Noaf4SpWzsLUCMBm5nr39UEOq89kx7QQjgYWLEWKcuSsgw2/6MckKP/6zrxjVld2SMtqiphKnrv1EkA==\n-----END CERTIFICATE-----","-----BEGIN CERTIFICATE-----\nMIICCTCCAY6gAwIBAgIDVxAsMAoGCCqGSM49BAMDMEsxEzARBgNVBAoTCkh1YXdlaSBDQkcxNDAyBgNVBAMTK0h1YXdlaSBDQkcgRUNDIERldmljZSBBdHRlc3RhdGlvbiBSb290IENBIDEwIBcNMjMxMTMwMDIwNjU1WhgPMjA3MzExMzAwMjA2NTVaMEsxEzARBgNVBAoTCkh1YXdlaSBDQkcxNDAyBgNVBAMTK0h1YXdlaSBDQkcgRUNDIERldmljZSBBdHRlc3RhdGlvbiBSb290IENBIDEwdjAQBgcqhkjOPQIBBgUrgQQAIgNiAATDJzRdruaBeMoQBbdqCe51ezvkQn3OPYBoRmpL5KPktdFtD0b97FRp8jGLiUhPKyo8M15fxW5Ams4s80E8I1BSXoovDnkKllFfUadD8URgwEfOk5qttYNKzJcULavOhbijQjBAMA4GA1UdDwEB/wQEAwIBBjAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBTaRGLD5yvof1E6XEuPQ3w5JMPOrDAKBggqhkjOPQQDAwNpADBmAjEA2zDQREvORPqcZyjwKDltu0T9zN8Cd3/hi4DQZvuRJdJOY57yIIO/LKxezzEcGiMMAjEAkX7r0U4Mcaw4uURMh+7tLMyvyxnlW8yJqBEOnZfqS8I8t0bQIY2r/5TQAPC0JhBm\n-----END CERTIFICATE-----"};

30. //从HarmonyOS官网下载的根CA证书
31. static String g_rootCertStr = "-----BEGIN CERTIFICATE-----\n" +
32. "MIICCTCCAY6gAwIBAgIDVxAsMAoGCCqGSM49BAMDMEsxEzARBgNVBAoTCkh1YXdl\n" +
33. "aSBDQkcxNDAyBgNVBAMTK0h1YXdlaSBDQkcgRUNDIERldmljZSBBdHRlc3RhdGlv\n" +
34. "biBSb290IENBIDEwIBcNMjMxMTMwMDIwNjU1WhgPMjA3MzExMzAwMjA2NTVaMEsx\n" +
35. "EzARBgNVBAoTCkh1YXdlaSBDQkcxNDAyBgNVBAMTK0h1YXdlaSBDQkcgRUNDIERl\n" +
36. "dmljZSBBdHRlc3RhdGlvbiBSb290IENBIDEwdjAQBgcqhkjOPQIBBgUrgQQAIgNi\n" +
37. "AATDJzRdruaBeMoQBbdqCe51ezvkQn3OPYBoRmpL5KPktdFtD0b97FRp8jGLiUhP\n" +
38. "Kyo8M15fxW5Ams4s80E8I1BSXoovDnkKllFfUadD8URgwEfOk5qttYNKzJcULavO\n" +
39. "hbijQjBAMA4GA1UdDwEB/wQEAwIBBjAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQW\n" +
40. "BBTaRGLD5yvof1E6XEuPQ3w5JMPOrDAKBggqhkjOPQQDAwNpADBmAjEA2zDQREvO\n" +
41. "RPqcZyjwKDltu0T9zN8Cd3/hi4DQZvuRJdJOY57yIIO/LKxezzEcGiMMAjEAkX7r\n" +
42. "0U4Mcaw4uURMh+7tLMyvyxnlW8yJqBEOnZfqS8I8t0bQIY2r/5TQAPC0JhBm\n" +
43. "-----END CERTIFICATE-----\n";

45. //保存HarmonyOS Hap应用生成的应用公钥的文件名
46. static String g_publicKeyFileName = "d:\\attestPublicKey.pem";

48. public static void main(String[] args) {
49. ParseAttestation parseAttestation = new ParseAttestation();
50. parseAttestation.parseAndValidateAttestCertChain(g_attestCertStr, g_rootCertStr, g_publicKeyFileName);
51. }

53. void parseAndValidateAttestCertChain(String[] attestCertStr, String rootCertStr, String publicKeyFileName) {
54. try {
55. //解析密钥证明证书链
56. List<X509Certificate> attestCerts = parseAttestationCerts(attestCertStr);
57. //校验密钥证明证书链
58. Date curDate = new Date();
59. validateAttestationCertChain(attestCerts, rootCertStr, curDate);
60. //解析密钥证明证书
61. AttestationInfo attestInfo = extractAttestaionField(attestCerts.get(0));
62. //校验密钥证明信息是否正确
63. if (!checkAttestInfo(attestInfo)) {
64. //todo： 进行异常处理
65. }
66. //保存HarmonyOS Hap应用生成的应用公钥
67. saveAttestPublicKey(attestInfo.publicKey, publicKeyFileName);
68. } catch (Exception e) {
69. System.out.println(e);
70. }
71. }

73. List<X509Certificate> parseAttestationCerts(String[] certStr) throws Exception {
74. List<X509Certificate> certificateList = new ArrayList<>(certStr.length);
75. CertificateFactory certificateFactory = CertificateFactory.getInstance("X.509", "BC");
76. for (int i = 0; i < certStr.length; i++) {
77. certificateList.add((X509Certificate) certificateFactory.generateCertificate(
78. new ByteArrayInputStream(certStr[i].getBytes())));
79. }
80. return certificateList;
81. }

83. void validateAttestationCertChain(List<X509Certificate> certs, String trustCAStr, Date date) throws Exception {
84. //构造证书链
85. CertificateFactory factory = CertificateFactory.getInstance("X.509", "BC");
86. CertPath certPath = factory.generateCertPath(certs);

88. //读取信任根证书和构建trustAnchor对象
89. X509Certificate trustCA = (X509Certificate) factory.generateCertificate(
90. new ByteArrayInputStream(trustCAStr.getBytes()));

92. TrustAnchor trustAnchor = new TrustAnchor(trustCA, null);
93. HashSet trustAnchorSet = new HashSet<TrustAnchor>();
94. trustAnchorSet.add(trustAnchor);

96. //构建validator和对应的参数
97. PKIXParameters params = new PKIXParameters(trustAnchorSet);
98. params.setDate(date);
99. //密钥证明证书有效期比较短，不需要进行证书的吊销验证。
100. params.setRevocationEnabled(false);

102. CertPathValidator validator = CertPathValidator.getInstance("PKIX", "BC");
103. try {
104. PKIXCertPathValidatorResult result = (PKIXCertPathValidatorResult) validator.validate(certPath, params);
105. System.out.println("Cert Chain validate success!");
106. } catch (Exception e) {
107. System.out.println("Cert Chain validate fail!" + e.getMessage());
108. }
109. }

111. int getInteger(ASN1Encodable value) {
112. if (value instanceof ASN1Integer) {
113. return ((ASN1Integer) value).getValue().intValue();
114. } else if (value instanceof ASN1Enumerated) {
115. return ((ASN1Enumerated) value).getValue().intValue();
116. } else {
117. throw new IllegalArgumentException(
118. "expected Integer value ; found " + value.getClass().getName() + " instead.");
119. }
120. }

122. byte[] getOctetString(ASN1Encodable value) {
123. if (value instanceof ASN1OctetString) {
124. return ((ASN1OctetString) value).getOctets();
125. } else {
126. throw new RuntimeException(
127. "expected OctetString value ; found " + value.getClass().getName() + " instead.");
128. }
129. }

131. void printBytes(byte[] byteArray) {
132. if (byteArray == null) {
133. System.out.println("null");
134. }
135. for (int i = 0; i < byteArray.length; i++) {
136. System.out.printf("%02X ", byteArray[i]);
137. }
138. System.out.println();
139. }

141. AttestationInfo extractAttestaionField(X509Certificate certificate) {
142. AttestationInfo attestInfo = new AttestationInfo();
143. //获取应用公钥
144. attestInfo.publicKey = certificate.getPublicKey();
145. //从密钥证明证书中获取 “密钥证明扩展域段”
146. byte[] attestationValue = certificate.getExtensionValue("1.3.6.1.4.1.2011.2.376.1.3");
147. if (attestationValue == null || attestationValue.length == 0) {
148. throw new IllegalArgumentException("Can't found the attestation extension!");
149. }
150. ASN1Sequence attestSequence = ASN1Sequence.getInstance(
151. ASN1OctetString.getInstance(attestationValue).getOctets());

153. //获取Attestation Version
154. attestInfo.version = getInteger(attestSequence.getObjectAt(0));

156. for (int i = 1; i < attestSequence.size(); i++) {
157. ASN1Sequence attestClaim = ASN1Sequence.getInstance(attestSequence.getObjectAt(i));
158. //获取Claim的oid
159. ASN1ObjectIdentifier attestClaimOid = (ASN1ObjectIdentifier) attestClaim.getObjectAt(1);
160. if ("1.3.6.1.4.1.2011.2.376.2.1.4".equalsIgnoreCase(attestClaimOid.getId())) {
161. //读取Challenge
162. attestInfo.challenge = getOctetString(attestClaim.getObjectAt(2));
163. } else if ("1.3.6.1.4.1.2011.2.376.2.1.3".equalsIgnoreCase(attestClaimOid.getId())) {
164. //读取appInfo
165. ASN1Sequence appInfoAsn1 = (ASN1Sequence) attestClaim.getObjectAt(2);
166. //获取appInfo的oid
167. ASN1ObjectIdentifier appidOid = (ASN1ObjectIdentifier) appInfoAsn1.getObjectAt(0);
168. if (!"1.3.6.1.4.1.2011.2.376.2.1.3.1".equalsIgnoreCase(appidOid.getId())) {
169. continue;
170. }
171. //读取hap应用信息
172. String appInfo = new String(getOctetString(appInfoAsn1.getObjectAt(1)));
173. System.out.println("appInfo is:\n" + appInfo);
174. attestInfo.appInfo = JSON.parseObject(appInfo, AppInfo.class);
175. } else if ("1.3.6.1.4.1.2011.2.376.2.2.2.6".equalsIgnoreCase(attestClaimOid.getId())) {
176. //读取密钥管理部件id，应该取值为0x28c4fb4944afec11b9090242ac120002
177. attestInfo.keyManagerId = getOctetString(attestClaim.getObjectAt(2));
178. } else if ("1.3.6.1.4.1.2011.2.376.2.2.4.8".equalsIgnoreCase(attestClaimOid.getId())) {
179. //读取设备产品型号
180. attestInfo.model = attestClaim.getObjectAt(2).toString();
181. }
182. }
183. return attestInfo;
184. }

186. boolean checkAttestInfo(AttestationInfo attestInfo) {
187. //todo: 校验Challenge
188. System.out.println("challenge is:");
189. printBytes(attestInfo.challenge);

191. //todo: 校验appInfo中的字段信息
192. System.out.println("appInfo.appId is:\n" + attestInfo.appInfo.appId);
193. System.out.println("appInfo.bundleName is:\n" + attestInfo.appInfo.bundleName);
194. System.out.println("appInfo.appIdentifier is:\n" + attestInfo.appInfo.appIdentifier);
195. System.out.println("appInfo.appMode is:\n" + attestInfo.appInfo.appMode);

197. //todo: 校验keyManagerId，固定为：0x28c4fb4944afec11b9090242ac120002。
198. System.out.println("key manager id is:");
199. printBytes(attestInfo.keyManagerId);

201. return true;
202. }

204. void saveAttestPublicKey(PublicKey publicKey, String publicKeyFileName) throws Exception {
205. //todo: 把attestInfo.publicKey.getEncoded()获取到的应用公钥保存到服务器
206. FileOutputStream file = new FileOutputStream(publicKeyFileName);
207. file.write(publicKey.getEncoded());
208. file.close();
209. System.out.println("the app public key: \n" + publicKey);
210. }

212. class AttestationInfo {
213. public PublicKey publicKey;
214. public int version;
215. public byte[] challenge;
216. public AppInfo appInfo;
217. public byte[] keyManagerId;
218. public String model;
219. }

221. static class AppInfo {
222. public String appId;
223. public String bundleName;
224. public String appIdentifier;
225. public String appMode;
226. }
227. }
```

## 保存应用公钥

您的应用服务器对密钥证明证书链校验通过后，把密钥证明证书中的应用公钥保存到服务器中（“对密钥证明证书链进行校验”的样例代码中已包含公钥保存的示例代码），以便对后续的业务请求进行验证。在保存应用公钥前应确保公钥的唯一性，应用服务器中不应该存在多个相同的应用公钥。

说明

安全建议：为了提高安全性，建议为终端设备中登录的每个用户生成唯一的密钥对，并在应用服务器对用户与应用公钥进行关联。

**实现提示：** 对业务请求进行签名验签时需要先查找到应用公钥，建议为应用公钥生成一个唯一的应用公钥ID（如：对应用公钥计算Hash），并保存应用公钥ID与应用公钥的关系，通过应用公钥ID来查找应用公钥。

同时，应用服务器应该返回应用公钥ID给应用，并由应用存储应用ID。
