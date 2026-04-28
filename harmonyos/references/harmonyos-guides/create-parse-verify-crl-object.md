---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-parse-verify-crl-object
title: 证书吊销列表对象的创建、解析和校验
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书算法库框架 > 证书吊销列表对象的创建、解析和校验
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9eefac927eb16596fa8aa8d7e52cb90205557bbc5fa6795a05684122c4f3a9fe
---

以校验证书是否已吊销为例，完成证书吊销列表对象的创建、解析和校验。若证书已被吊销，将打印被吊销日期。

## 开发步骤

1. 导入[证书算法库框架模块](../harmonyos-references/js-apis-cert.md)和[加解密算法库模块](../harmonyos-references/js-apis-cryptoframework.md)。

   ```
   1. import { cert } from '@kit.DeviceCertificateKit';
   2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
   ```
2. 基于已有的CRL数据，调用[cert.createX509CRL](../harmonyos-references/js-apis-cert.md#certcreatex509crl11)创建X509证书吊销列表的对象。
3. 解析证书吊销列表信息。

   此处以获取证书吊销列表版本、证书吊销列表类型、证书吊销列表颁发者名称、证书吊销列表对象的字符串类型数据为例，更多字段信息获取接口请查看[API参考文档](../harmonyos-references/js-apis-cert.md#x509crl11)。
4. 基于已有公钥信息，创建PublicKey公钥对象。

   具体可参考[加解密算法库框架-指定二进制数据生成非对称密钥对](../harmonyos-references/js-apis-cryptoframework.md#convertkey-3)。
5. 调用[X509CRL.verify](../harmonyos-references/js-apis-cert.md#verify11)校验签名合法性。
6. 基于已有的X509证书数据，调用[cert.createX509Cert](../harmonyos-references/js-apis-cert.md#certcreatex509cert)创建证书对象。
7. 调用[X509CRL.isRevoked](../harmonyos-references/js-apis-cert.md#isrevoked11)判断X509证书是否已被吊销。
8. 调用[X509CRL.getRevokedCert](../harmonyos-references/js-apis-cert.md#getrevokedcert11)获取被吊销证书对象。
9. 调用[X509CRLEntry.getRevocationDate](../harmonyos-references/js-apis-cert.md#getrevocationdate11)获取被吊销日期。

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { util } from '@kit.ArkTS';

6. // ...
7. // CRL示例
8. function crlSample(): void {
9. let textEncoder = new util.TextEncoder();
10. let encodingBlob: cert.EncodingBlob = {
11. // 将CRL数据从string转为Uint8Array。
12. data: textEncoder.encodeInto(crlData),
13. // CRL格式，仅支持PEM和DER格式。在这个例子中，CRL用的是PEM格式。
14. encodingFormat: cert.EncodingFormat.FORMAT_PEM
15. };

17. // 创建X509CRL实例。
18. cert.createX509CRL(encodingBlob, (err, x509Crl) => {
19. if (err != null) {
20. // 创建X509CRL实例失败。
21. console.error(`createX509Crl failed, errCode: ${err.code}, errMsg:${err.message} `);
22. return;
23. }
24. // 创建X509CRL实例成功。
25. console.info('createX509CRL result: success.');

27. // 获取CRL的版本。
28. let version = x509Crl.getVersion();
29. // 获取证书吊销列表类型。
30. let revokedType = x509Crl.getType();
31. console.info(`X509 CRL version: ${version}, type :${revokedType}`);

33. // 获取证书吊销列表颁发者名称。
34. let issuerName = x509Crl.getIssuerName(cert.EncodingType.ENCODING_UTF8);
35. console.info(`X509 CRL issuerName: ${issuerName}`);

37. // 获取证书吊销列表对象的字符串类型数据。
38. let crlString = x509Crl.toString(cert.EncodingType.ENCODING_UTF8);
39. console.info(`X509 CRL crlString: ${crlString}`);

42. // 公钥的二进制数据需要传入@ohos.security.cryptoFramework的convertKey()方法去获取公钥对象。
43. try {
44. let keyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024|PRIMES_3');
45. console.info('createAsyKeyGenerator result: success.');
46. let pubEncodingBlob: cryptoFramework.DataBlob = {
47. data: pubKeyData,
48. };
49. keyGenerator.convertKey(pubEncodingBlob, null, (e, keyPair) => {
50. if (e == null) {
51. console.info('convertKey result: success.');
52. x509Crl.verify(keyPair.pubKey, (err, data) => {
53. if (err == null) {
54. // 签名验证成功。
55. console.info('verify result: success.');
56. } else {
57. // 签名验证失败。
58. console.error(`verify failed, errCode: ${err.code}, errMsg: ${err.message}`);
59. }
60. });
61. } else {
62. console.error(`convert key failed, errCode: ${e.code}, errMsg: ${e.message}`);
63. }
64. })
65. } catch (error) {
66. let e: BusinessError = error as BusinessError;
67. console.error(`get pubKey failed, errCode: ${e.code}, errMsg: ${e.message}`);
68. }

70. // 使用certFramework的createX509Cert()方法创建一个X509Cert实例。
71. let certBlob: cert.EncodingBlob = {
72. data: textEncoder.encodeInto(certData),
73. encodingFormat: cert.EncodingFormat.FORMAT_PEM
74. };
75. let revokedFlag = true;
76. let serial: bigint = BigInt('0');
77. cert.createX509Cert(certBlob, (err, cert) => {
78. serial = cert.getCertSerialNumber();
79. if (err == null) {
80. try {
81. // 检查证书是否被吊销。
82. revokedFlag = x509Crl.isRevoked(cert);
83. console.info(`revokedFlag is: ${revokedFlag}`);
84. if (!revokedFlag) {
85. console.info('the given cert is not revoked.');
86. return;
87. }
88. // 根据序列号来获取被吊销的证书。
89. try {
90. let crlEntry = x509Crl.getRevokedCert(serial);
91. console.info('getRevokedCert result: success.');
92. let serialNumber = crlEntry.getSerialNumber();
93. console.info(`crlEntry serialNumber is: ${serialNumber}`);

95. // 获取被吊销证书的吊销日期。
96. let date = crlEntry.getRevocationDate();
97. console.info(`revocation date is: ${date}`);
98. } catch (error) {
99. let e: BusinessError = error as BusinessError;
100. console.error(`getRevokedCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
101. }
102. } catch (error) {
103. let e: BusinessError = error as BusinessError;
104. console.error(`isRevoked failed, errCode: ${e.code}, errMsg:${e.message}`);
105. }
106. } else {
107. console.error(`create x509 cert failed, errCode: ${err.code}, errMsg: ${err.message}`);
108. }
109. })

111. });
112. }
```

[CreateParseVerifyCrlObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateAlgorithmLibrary/entry/src/main/ets/pages/CreateParseVerifyCrlObject.ets#L16-L191)
