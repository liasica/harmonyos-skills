---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-real-name-preparations
title: （可选）用户身份验证服务接入准备
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 开发准备 > （可选）用户身份验证服务接入准备
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e6ad8e1aa1fbbde41e22a60ac21ab75df9116038a1d3abeb734f1bfda7bff85f
---

如不涉及身份验证服务接入，可跳过该章节。

## 开启用户身份验证服务权限开关

开发者可登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“项目设置 > 开放能力管理”的“鸿蒙支付服务”中开启身份验证服务相关权限开关。

说明

开启身份验证服务相关权限开关时，开发者需签署一份“开发者协议”，开发者同意协议并提交申请资料后需要等待审核（审核周期一般在1-3个工作日）通过后才能使用相关服务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/9DE0PWRzSS2eFMQZhxRuhw/zh-cn_image_0000002589325455.png?HW-CC-KV=V1&HW-CC-Date=20260429T053929Z&HW-CC-Expire=86400&HW-CC-Sign=651FBDD96F668A0A3222780F15BC33916504FF9C4B6B25B89702F84393020291)

## 上传开发者公钥及下载华为公钥

开发者可登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“鸿蒙支付服务 > 身份验证服务”菜单中的“公钥管理”页签下完成开发者证书的上传以及华为公钥证书下载。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/qC3KSw9TTKC7EI-7_oMZvg/zh-cn_image_0000002589245393.png?HW-CC-KV=V1&HW-CC-Date=20260429T053929Z&HW-CC-Expire=86400&HW-CC-Sign=93A7A4B15B1D8688D3F91677A204BF10E9EAD4216BD2FB5D5CE984B5A29DD618)

证书使用如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/0dEgChByQxe0Xv3rE5ToGg/zh-cn_image_0000002558765586.png?HW-CC-KV=V1&HW-CC-Date=20260429T053929Z&HW-CC-Expire=86400&HW-CC-Sign=A51697A6579D790EE3D747F0267C6CD8E146E97EA4C2D3E5E3532FB1BD96F044)

证书说明如下：

| 证书 | 获取方式 | 内容说明及使用场景 |
| --- | --- | --- |
| **华为加密公钥** | [AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)的“鸿蒙支付服务>身份验证服务>公钥管理”下载 | 华为支付服务器使用SM2加密算法生成的证书公钥。  **使用场景：** 开发者可用对应的公钥证书对请求开放API接口的隐私字段进行加密，华为支付服务器使用配对的私钥证书对隐私字段进行解密。 |
| **华为签名公钥** | [AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)的“鸿蒙支付服务>身份验证服务>公钥管理”下载 | 华为支付服务器使用SM2加密算法生成的证书公钥。  **使用场景：** 华为支付服务器使用配对的私钥证书对响应报文进行加签， 开发者用于对开放API接口响应报文验签使用，具体验签方式请参见[验签规则](../harmonyos-references/payment-rest-overview.md#验签规则)。 |
| **开发者公钥**（**加密**） | 开发者生成 | 开发者使用SM2加密算法生成的证书公钥。需登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“鸿蒙支付服务>身份验证服务>公钥管理”上传（公钥类型为加密）。  **使用场景：** 开发者上传后生成证书Id（developerEncKeyId），开发者请求开放API接口时可通过[PayDevAuth](../harmonyos-references/payment-model.md#paydevauth)请求头传递，指定给华为支付服务器用于对开放API接口响应的隐私字段加密。 |
| **开发者公钥（签名）** | 开发者生成 | 开发者使用SM2加密算法生成的证书公钥。需登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“鸿蒙支付服务>身份验证服务>公钥管理”上传（公钥类型为签名）。  **使用场景：** 开发者上传后生成证书Id（developerSignKeyId），开发者请求开放API接口时可通过[PayDevAuth](../harmonyos-references/payment-model.md#paydevauth)请求头传递，指定给华为支付服务器用于对开放API接口请求报文进行验签。 |

### SM2公私钥对生成示例代码参考

注意

* 只支持ASN.1格式的SM2公私钥对（以下示例代码为服务端生成示例）。如需在应用端生成ASN.1格式SM2公私钥对（公钥91字节，私钥51字节）可参考：

1. [随机生成非对称密钥对(ArkTS)](crypto-generate-asym-key-pair-randomly.md)（应用端生成的公私钥对可能无法在服务端使用）。
2. 参考[数据编码格式差异](../best-practices/bpta-cross-platform-compatibility.md#section1152116421582)将生成的秘钥对转成16进制hex格式。

* 生成的SM2公私钥对，还请先自测验证加解密是否正常，正常后再正式对外使用，避免生成错误的公私钥对，阻塞后续业务进度。

```
1. import org.bouncycastle.jce.provider.BouncyCastleProvider;
2. import org.bouncycastle.util.encoders.Hex;
3. import org.junit.Test;

5. import java.security.KeyPair;
6. import java.security.KeyPairGenerator;
7. import java.security.SecureRandom;
8. import java.security.spec.ECGenParameterSpec;
9. import java.util.HashMap;

11. public class GenerateSm2KeyPairTest2 {
12. public static void main(String[] args) {
13. try {
14. // 获取sm2公私钥
15. String jsonObject = getSm2SecretKey();
16. // 可打印生成公私钥信息，例如：log.info(jsonObject);
17. } catch (Exception e) {
18. e.printStackTrace();
19. }
20. }

22. /**
23. * 生成SM2的ASN.1格式的公私钥
24. *
25. * @return SM2的ASN.1格式的公私钥
26. */
27. public static String getSm2SecretKey() {
28. try {
29. KeyPair keyPair = generateSm2KeyPair();
30. String privateKeyStr = Hex.toHexString(keyPair.getPrivate().getEncoded());
31. String publicKeyStr = Hex.toHexString(keyPair.getPublic().getEncoded());
32. HashMap<String, String> result = new HashMap<>();
33. result.put("Sm2PrivateKey", privateKeyStr);
34. result.put("Sm2PublicKey", publicKeyStr);
35. return result.toString();
36. } catch (Exception e) {
37. return null;
38. }
39. }

41. /**
42. * SM2算法生成ASN.1格式的公私钥对
43. *
44. * @return 密钥对信息
45. */
46. public static KeyPair generateSm2KeyPair() throws Exception {
47. try {
48. final ECGenParameterSpec sm2Spec = new ECGenParameterSpec("sm2p256v1");
49. // 获取一个椭圆曲线类型的密钥对生成器
50. final KeyPairGenerator kpg = KeyPairGenerator.getInstance("EC", new BouncyCastleProvider());
51. SecureRandom random = new SecureRandom();
52. // 使用SM2的算法区域初始化密钥生成器
53. kpg.initialize(sm2Spec, random);
54. // 获取密钥对
55. KeyPair keyPair = kpg.generateKeyPair();
56. return keyPair;
57. } catch (Exception e) {
58. throw new SecurityException("generateSm2KeyPair failed.");
59. }
60. }
61. }
```

### SM2加密示例代码参考

```
1. import org.bouncycastle.asn1.ASN1ObjectIdentifier;
2. import org.bouncycastle.asn1.gm.GMNamedCurves;
3. import org.bouncycastle.asn1.x509.AlgorithmIdentifier;
4. import org.bouncycastle.asn1.x509.SubjectPublicKeyInfo;
5. import org.bouncycastle.asn1.x9.X9ECParameters;
6. import org.bouncycastle.asn1.x9.X9ObjectIdentifiers;
7. import org.bouncycastle.crypto.engines.SM2Engine;
8. import org.bouncycastle.crypto.params.ECDomainParameters;
9. import org.bouncycastle.crypto.params.ECPublicKeyParameters;
10. import org.bouncycastle.crypto.params.ParametersWithRandom;
11. import org.bouncycastle.math.ec.ECPoint;
12. import org.bouncycastle.util.encoders.Hex;

14. import java.nio.charset.StandardCharsets;
15. import java.security.SecureRandom;

17. public class SM2EncTest {
18. public static void main(String[] args) {
19. encrypt("16进制编码的SM2公钥", "待加密数据");
20. }

22. public static String encrypt(String pubKey, String data) {
23. SM2Engine sm2Engine = new SM2Engine(SM2Engine.Mode.C1C3C2);
24. if (data == null || data.isEmpty()) {
25. return data;
26. }
27. byte[] in = data.getBytes(StandardCharsets.UTF_8);
28. return Hex.toHexString(encrypt(pubKey, in, sm2Engine));
29. }

31. private static byte[] encrypt(String pubKey, byte[] in, SM2Engine sm2Engine) {
32. try {
33. byte[] bPubKey = Hex.decode(pubKey);
34. byte[] coding = getCoding(bPubKey);
35. X9ECParameters x9ECParameters = GMNamedCurves.getByName("sm2p256v1");
36. ECDomainParameters ecDomainParameters = new ECDomainParameters(x9ECParameters.getCurve(),
37. x9ECParameters.getG(), x9ECParameters.getN());
38. ECPoint pukPoint = x9ECParameters.getCurve().decodePoint(coding);
39. ECPublicKeyParameters publicKeyParameters = new ECPublicKeyParameters(pukPoint, ecDomainParameters);
40. sm2Engine.init(true, new ParametersWithRandom(publicKeyParameters, new SecureRandom()));
41. return sm2Engine.processBlock(in, 0, in.length);
42. } catch (Exception var7) {
43. throw new SecurityException(var7);
44. }
45. }

47. private static byte[] getCoding(byte[] publicKey) {
48. if (publicKey.length != 64 && publicKey.length != 65) {
49. AlgorithmIdentifier aid = new AlgorithmIdentifier(
50. X9ObjectIdentifiers.id_ecPublicKey, new ASN1ObjectIdentifier("1.2.156.10197.1.301"));
51. SubjectPublicKeyInfo info = SubjectPublicKeyInfo.getInstance(publicKey);
52. if (!aid.equals(info.getAlgorithm())) {
53. throw new SecurityException("encoded not valid");
54. } else {
55. byte[] coding = info.getPublicKeyData().getBytes();
56. if (coding.length != 65) {
57. throw new SecurityException("encoded not valid");
58. } else {
59. return coding;
60. }
61. }
62. } else {
63. if (publicKey.length == 64) {
64. byte[] bytes = new byte[65];
65. bytes[0] = 4;
66. System.arraycopy(publicKey, 0, bytes, 1, 64);
67. publicKey = bytes;
68. }
69. return (byte[]) publicKey.clone();
70. }
71. }
72. }
```

### SM2解密示例代码参考

```
1. import org.bouncycastle.asn1.ASN1Integer;
2. import org.bouncycastle.asn1.ASN1OctetString;
3. import org.bouncycastle.asn1.ASN1Primitive;
4. import org.bouncycastle.asn1.ASN1Sequence;
5. import org.bouncycastle.asn1.ASN1Set;
6. import org.bouncycastle.asn1.ASN1TaggedObject;
7. import org.bouncycastle.asn1.gm.GMNamedCurves;
8. import org.bouncycastle.asn1.sec.ECPrivateKey;
9. import org.bouncycastle.asn1.x509.AlgorithmIdentifier;
10. import org.bouncycastle.asn1.x9.X9ECParameters;
11. import org.bouncycastle.crypto.engines.SM2Engine;
12. import org.bouncycastle.crypto.params.ECDomainParameters;
13. import org.bouncycastle.crypto.params.ECPrivateKeyParameters;
14. import org.bouncycastle.util.encoders.Hex;

16. import java.io.IOException;
17. import java.math.BigInteger;
18. import java.nio.charset.StandardCharsets;
19. import java.util.Enumeration;

21. public class SM2DecTest {
22. public static void main(String[] args) {
23. String data = decrypt("16进制编码解密私钥", "密文");
24. System.out.println(data);
25. }

27. private static String decrypt(String priKey, String cipherData) {
28. SM2Engine sm2Engine = new SM2Engine(SM2Engine.Mode.C1C3C2);
29. if (cipherData == null || cipherData.isEmpty()) {
30. throw new SecurityException("cipher data is empty when decrypt data");
31. }
32. if (priKey == null || priKey.isEmpty()) {
33. throw new SecurityException("pri key is empty when decrypt data");
34. }
35. try {
36. X9ECParameters x9ECParameters = GMNamedCurves.getByName("sm2p256v1");
37. ECDomainParameters ecDomainParameters = new ECDomainParameters(x9ECParameters.getCurve(),
38. x9ECParameters.getG(), x9ECParameters.getN());
39. byte[] bPriKey = Hex.decode(priKey);
40. byte[] enContent = Hex.decode(cipherData);
41. BigInteger privateKeyD;
42. if (bPriKey.length != 32 && bPriKey.length != 33) {
43. privateKeyD = getDInt(bPriKey);
44. } else {
45. privateKeyD = new BigInteger(bPriKey);
46. }
47. ECPrivateKeyParameters privateKeyParameters = new ECPrivateKeyParameters(privateKeyD, ecDomainParameters);
48. sm2Engine.init(false, privateKeyParameters);
49. return new String(sm2Engine.processBlock(enContent, 0, enContent.length), StandardCharsets.UTF_8);
50. } catch (Exception var7) {
51. throw new SecurityException(var7);
52. }
53. }

55. private static BigInteger getDInt(byte[] bytesKey) throws IOException {
56. ASN1Sequence sequence = ASN1Sequence.getInstance(bytesKey);
57. Enumeration e = sequence.getObjects();
58. BigInteger version = ((ASN1Integer) e.nextElement()).getValue();
59. if (version.intValue() != 0) {
60. throw new IllegalArgumentException("wrong version for private key info");
61. }
62. AlgorithmIdentifier algId = AlgorithmIdentifier.getInstance(e.nextElement());
63. ASN1OctetString privKey = ASN1OctetString.getInstance(e.nextElement());
64. ASN1Set attributes;
65. if (e.hasMoreElements()) {
66. attributes = ASN1Set.getInstance((ASN1TaggedObject) e.nextElement(), false);
67. }
68. ASN1Primitive primitive = ASN1Primitive.fromByteArray(privKey.getOctets());
69. ECPrivateKey privateKey = ECPrivateKey.getInstance(primitive);
70. return privateKey.getKey();
71. }
72. }
```
