---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/attestation-signature-verification-servers
title: 服务器端开发
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 应用真实性证明 > 签名验签识别真实请求 > 服务器端开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c1c6eeeb6461f6e2ff46a2d0418ecf18edea913d523be955baac488484b84fd1
---

## 使用前提

使用应用公钥对业务请求进行验签的前提是服务器已经完成对密钥证明证书链进行校验和保存应用公钥，相关开发指南请参考：

* [对密钥证明证书链进行校验](device-attestation-servers.md#校验密钥证明证书链)
* [保存应用公钥](device-attestation-servers.md#保存应用公钥)

## 使用应用公钥对业务请求进行验签

应用服务器首先校验挑战值Challenge，然后根据应用公钥ID查找应用公钥。

说明

安全建议：如果应用服务器在保存应用公钥时关联了用户ID，在使用应用公钥对业务请求进行验签时，应该根据应用公钥ID+当前登录的用户ID查找应用公钥。

应用服务器再使用应用公钥对请求中的签名进行验签。

**示例：**

```
1. import org.bouncycastle.jce.provider.BouncyCastleProvider;

3. import java.io.ByteArrayOutputStream;
4. import java.io.FileInputStream;
5. import java.io.FileOutputStream;
6. import java.security.InvalidKeyException;
7. import java.security.KeyFactory;
8. import java.security.NoSuchAlgorithmException;
9. import java.security.NoSuchProviderException;
10. import java.security.PublicKey;
11. import java.security.Security;
12. import java.security.Signature;
13. import java.security.SignatureException;
14. import java.security.spec.X509EncodedKeySpec;
15. import java.util.Base64;

17. public class VerifySignature {
18. static {
19. Security.addProvider(new BouncyCastleProvider());
20. }

22. //保存HarmonyOS Hap应用生成的证书公钥的文件名
23. static String g_publicKeyFileName = "d:\\attestPublicKey.pem";
24. //HarmonyOS Hap应用使用私钥生成的签名数据，base64编码。
25. static String g_signedData = "MEUCIQDtlrQa7HQccprCkR0nWTL7N6HEKY9PKN3DTk3aeN0/fQIgeqTrQ+7exiJhwTY3LwT7XhRHV1emOfTYho5qxyektho=";
26. //待签名的数据
27. static String g_plaintext = "123456";
28. //签名算法，与应用端采用的算法保持一致，取值样例：SM3WITHSM2，SHA256withECDSA。
29. static String g_signAlg = "SHA256withECDSA";

31. public static void main(String[] args) {
32. VerifySignature verifySignature = new VerifySignature();
33. verifySignature.verifySignature(g_publicKeyFileName, g_plaintext, g_signedData, g_signAlg);
34. }

36. void verifySignature(String publicKeyFile, String plainText, String signedData, String signAlg) {
37. try {
38. PublicKey publicKey = readAttestPublicKey(publicKeyFile);
39. byte[] signedDataByte = Base64.getDecoder().decode(signedData);
40. System.out.println("signedDataByte len=" + signedDataByte.length);
41. printBytes(signedDataByte);
42. byte[] plainTextBytes = plainText.getBytes();
43. System.out.println("plainTextBytes len=" + plainTextBytes.length);
44. printBytes(plainTextBytes);
45. boolean result = doVerify(publicKey, plainTextBytes, signedDataByte, signAlg);
46. System.out.println("Verify signature result: " + result);
47. } catch (Exception e) {
48. System.out.println(e);
49. }
50. }

52. PublicKey readAttestPublicKey(String publicKeyFileName) throws Exception {
53. //todo: 从服务器读取应用公钥
54. KeyFactory keyFactory = KeyFactory.getInstance("EC", "BC");
55. X509EncodedKeySpec spec = new X509EncodedKeySpec(readFromFile(publicKeyFileName));
56. PublicKey publicKey = keyFactory.generatePublic(spec);
57. System.out.println("the app public key: \n" + publicKey);
58. return publicKey;
59. }

61. byte[] readFromFile(String fn) throws Exception {
62. FileInputStream inputStream = new FileInputStream(fn);
63. ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
64. byte[] bytes = new byte[1024];
65. int len;
66. do {
67. len = inputStream.read(bytes);
68. outputStream.write(bytes, 0, len);
69. } while (bytes.length == len);
70. inputStream.close();
71. return outputStream.toByteArray();
72. }

74. boolean doVerify(PublicKey publickey, byte[] unsignedData, byte[] signedData, String signAlg) {
75. boolean verifyResult = false;
76. try {
77. Signature signature = Signature.getInstance(signAlg, "BC");
78. signature.initVerify(publickey);
79. signature.update(unsignedData);
80. verifyResult = signature.verify(signedData);
81. return verifyResult;
82. } catch (NoSuchAlgorithmException | NoSuchProviderException | InvalidKeyException | SignatureException e) {
83. e.printStackTrace();
84. }
85. return verifyResult;
86. }

88. void printBytes(byte[] byteArray) {
89. for (int i = 0; i < byteArray.length; i++) {
90. System.out.printf("%02X ", byteArray[i]);
91. }
92. System.out.println();
93. }
94. }
```
