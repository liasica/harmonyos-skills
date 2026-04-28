---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-cms-enveloped-object
title: 证书CMS封装
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书算法库框架 > 证书CMS封装
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9b874196268843a9c8e80de5ae8836b24743b38b4f78d7a16f8bc992287e2a35
---

从API 22开始，支持证书CMS封装。

PKCS#7是用于存储签名或加密数据的标准语法。CMS作为PKCS#7的扩展，支持的数据类型包括数据、签名数据、封装数据、签名和封装数据、摘要数据以及加密数据。该标准常用于保护数据的完整性和机密性。

目前仅支持CMS签名数据和封装数据。

## 开发步骤

1. 导入[证书算法库框架模块](../harmonyos-references/js-apis-cert.md)。

   ```
   1. import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 调用[cert.createCmsGenerator](../harmonyos-references/js-apis-cert.md#certcreatecmsgenerator18)创建cmsGenerator对象。
3. 调用[cmsGenerator.setRecipientEncryptionAlgorithm](../harmonyos-references/js-apis-cert.md#setrecipientencryptionalgorithm22)设置加密算法。
4. 调用[cmsGenerator.addRecipientInfo](../harmonyos-references/js-apis-cert.md#addrecipientinfo22)添加接收者信息。
5. 调用[cmsGenerator.doFinal](../harmonyos-references/js-apis-cert.md#dofinal18)获取CMS最终封装数据。
6. 调用[cmsGenerator.getEncryptedContentData](../harmonyos-references/js-apis-cert.md#getencryptedcontentdata22)获取CMS封装密文数据。

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. let eccCertData = '-----BEGIN CERTIFICATE-----\n' +
4. 'MIICOjCCAd+gAwIBAgIGAXKnJjrAMAoGCCqGSM49BAMCMHkxCzAJBgNVBAYTAmNo\n' +
5. 'MQ8wDQYDVQQIDAZodWF3ZWkxDTALBgNVBAcMBHhpYW4xDzANBgNVBAoMBmh1YXdl\n' +
6. 'aTENMAsGA1UECwwEdGVzdDENMAsGA1UEAwwEYW5uZTEbMBkGCSqGSIb3DQEJARYM\n' +
7. 'dGVzdEAxMjMuY29tMB4XDTI0MTEyNzAzMjQ1MFoXDTM0MTEyNTAzMjQ1MFoweTEL\n' +
8. 'MAkGA1UEBhMCY2gxDzANBgNVBAgMBmh1YXdlaTENMAsGA1UEBwwEeGlhbjEPMA0G\n' +
9. 'A1UECgwGaHVhd2VpMQ0wCwYDVQQLDAR0ZXN0MQ0wCwYDVQQDDARhbm5lMRswGQYJ\n' +
10. 'KoZIhvcNAQkBFgx0ZXN0QDEyMy5jb20wWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC\n' +
11. 'AARzg16D6tsNHZa7w0tLHFprXg5kUQgXv/vv3KIM21hY+WDYMz1OST4tmTeQWQF8\n' +
12. 'kARtjjbHBxtOPufWxMfxf51Wo1MwUTAdBgNVHQ4EFgQUU/P31GCBwyrj3yXkoNaX\n' +
13. 'xvPp8uIwHwYDVR0jBBgwFoAUU/P31GCBwyrj3yXkoNaXxvPp8uIwDwYDVR0TAQH/\n' +
14. 'BAUwAwEB/zAKBggqhkjOPQQDAgNJADBGAiEA/wCfbTorAWEEZcgd0CgfXI+EzXu2\n' +
15. 'Y88BmDD5LFlj3N0CIQDB34h77Li0CSpYpS4+7Mug237zbkFjHR3Q4/VWOT1G1A==\n' +
16. '-----END CERTIFICATE-----\n';

18. let rsaCertData = '-----BEGIN CERTIFICATE-----\n' +
19. 'MIICXjCCAcegAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMEgxCzAJBgNVBAYT\n' +
20. 'AkNOMQwwCgYDVQQIDANzaGExDTALBgNVBAcMBHhpYW4xDTALBgNVBAoMBHRlc3Qx\n' +
21. 'DTALBgNVBAMMBHRlc3QwHhcNMjQxMTIyMDkwNTIyWhcNMzQxMTIwMDkwNTIyWjBI\n' +
22. 'MQswCQYDVQQGEwJDTjEMMAoGA1UECAwDc2hhMQ0wCwYDVQQHDAR4aWFuMQ0wCwYD\n' +
23. 'VQQKDAR0ZXN0MQ0wCwYDVQQDDAR0ZXN0MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB\n' +
24. 'iQKBgQC6nCZTM16Rk2c4P/hwfVm++jqe6GCA/PXXGe4YL218q1dTKMHBGEw8kXi0\n' +
25. 'XLDcyyC2yUn8ywN2QSyly6ke9EE6PGfZywStLp4g2PTTWB04sS3aXT2y+fToiTXQ\n' +
26. '3AxfFYRpB+EgSdSCkJs6jKXVwbzu54kEtQTfs8UdBQ9nVKaJLwIDAQABo1MwUTAd\n' +
27. 'BgNVHQ4EFgQU6QXnt1smb2HRSO/2zuRQnz/SDxowHwYDVR0jBBgwFoAU6QXnt1sm\n' +
28. 'b2HRSO/2zuRQnz/SDxowDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOB\n' +
29. 'gQBPR/+5xzFG1XlTdgwWVvqVxvhGUkbMTGW0IviJ+jbKsi57vnVsOtFzEA6y+bYx\n' +
30. 'xG/kEOcwLtzeVHOQA+ZU5SVcc+qc0dfFiWjL2PSAG4bpqSTjujpuUk+g8ugixbG1\n' +
31. 'a26pkDJhNeB/E3eBIbeydSY0A/dIGb6vbGo6BSq2KvnWAA==\n' +
32. '-----END CERTIFICATE-----\n';

34. // string转Uint8Array。
35. function stringToUint8Array(str: string): Uint8Array {
36. let arr: number[] = [];
37. for (let i = 0, j = str.length; i < j; i++) {
38. arr.push(str.charCodeAt(i));
39. }
40. return new Uint8Array(arr);
41. }

43. async function testGetEncryptedContentData() {
44. try {
45. let ecccertEncodingBlob: cert.EncodingBlob = {
46. data: stringToUint8Array(eccCertData),
47. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
48. encodingFormat: cert.EncodingFormat.FORMAT_PEM
49. };

51. let rsacertEncodingBlob: cert.EncodingBlob = {
52. data: stringToUint8Array(rsaCertData),
53. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
54. encodingFormat: cert.EncodingFormat.FORMAT_PEM
55. };

57. let eccx509Certcert = await cert.createX509Cert(ecccertEncodingBlob);
58. let rsax509Certcert = await cert.createX509Cert(rsacertEncodingBlob);

60. let cmsContentType = cert.CmsContentType.ENVELOPED_DATA;
61. let cmsGenerator = cert.createCmsGenerator(cmsContentType);
62. console.info(`createCmsGenerator result: success.`);
63. let algorithm = cert.CmsRecipientEncryptionAlgorithm.AES_256_GCM;
64. cmsGenerator.setRecipientEncryptionAlgorithm(algorithm);
65. console.info(`setRecipientEncryptionAlgorithm result: success.`);
66. let eccCert: cert.CmsKeyAgreeRecipientInfo = {
67. cert: eccx509Certcert,
68. digestAlgorithm: cert.CmsKeyAgreeRecipientDigestAlgorithm.SHA256,
69. };
70. let rsaCert: cert.CmsKeyTransRecipientInfo = {
71. cert: rsax509Certcert,
72. };
73. let recipientInfo: cert.CmsRecipientInfo = {
74. keyTransInfo: rsaCert,
75. keyAgreeInfo: eccCert,
76. };
77. await cmsGenerator.addRecipientInfo(recipientInfo);
78. console.info(`addRecipientInfo result: success.`);
79. let content = new Uint8Array([1, 2, 3, 4]);
80. let optionsFinal: cert.CmsGeneratorOptions = {
81. contentDataFormat: cert.CmsContentDataFormat.BINARY,
82. outFormat: cert.CmsFormat.PEM,
83. isDetached: true
84. };
85. let cms = await cmsGenerator.doFinal(content, optionsFinal);
86. console.info(`doFinal result: success, cms = %s`, cms);
87. let data = await cmsGenerator.getEncryptedContentData();
88. console.info(`getEncryptedContentData result: success, data = %s`, data);
89. } catch (err) {
90. console.error(`testGetEncryptedContentData failed: errCode: ${err.code}, message: ${err.message}`);
91. }
92. }
```

[CreateCmsEnvelopedObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateAlgorithmLibrary/entry/src/main/ets/pages/CreateCmsEnvelopedObject.ets#L16-L111)
