---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-cms-decapsulation-object
title: 证书CMS解封装
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书算法库框架 > 证书CMS解封装
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9f4a536abc4038bf14c21aa9ad5a49a74dd94dcca3825128ee98a8389edc8e5f
---

从API 22开始，支持证书CMS解封装。

PKCS#7是用于存储签名或加密数据的标准语法。CMS作为PKCS#7的扩展，支持的数据类型包括数据、签名数据、封装数据、签名和封装数据、摘要数据以及加密数据。该标准常用于保护数据的完整性和机密性。

目前仅支持CMS签名数据和封装数据。

## 开发步骤

1. 导入[证书算法库框架模块](../harmonyos-references/js-apis-cert.md)。

   ```
   1. import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 调用[证书CMS封装](create-cms-enveloped-object.md)进行CMS数据封装。
3. 调用[cert.createCmsParser](../harmonyos-references/js-apis-cert.md#certcreatecmsparser22)创建CmsParser对象。
4. 调用[cmsParser.setRawData](../harmonyos-references/js-apis-cert.md#setrawdata22)设置CMS数据。
5. 调用[cmsParser.decryptEnvelopedData](../harmonyos-references/js-apis-cert.md#decryptenvelopeddata22)解密封装数据。

解封装示例：

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. let ECC_256_PUBKEY: string =
4. '-----BEGIN CERTIFICATE-----\n' +
5. 'MIICGDCCAb6gAwIBAgIGAXKnJjrAMAoGCCqGSM49BAMCMFcxCzAJBgNVBAYTAkNO\n' +
6. 'MQ8wDQYDVQQIDAbpmZXopb8xDzANBgNVBAcMBuilv+WuiTEPMA0GA1UECgwG5rWL\n' +
7. '6K+VMRUwEwYDVQQDDAzkuK3mlofmtYvor5UwHhcNMjUwOTE2MDY0MTMwWhcNMzUw\n' +
8. 'OTE0MDY0MTMwWjBXMQswCQYDVQQGEwJDTjEPMA0GA1UECAwG6ZmV6KW/MQ8wDQYD\n' +
9. 'VQQHDAbopb/lrokxDzANBgNVBAoMBua1i+ivlTEVMBMGA1UEAwwM5Lit5paH5rWL\n' +
10. '6K+VMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEB06h4SzOryi3d7PW9yN2wACC\n' +
11. 'VxlduBQjVLWZlDKhFKkdZjve8mUyytSSbBj/rrzR2XmzUzofuNkUbAtje3DDJqN2\n' +
12. 'MHQwHQYDVR0OBBYEFNtUldgBESf31bwTnYtApIctaSdtMB8GA1UdIwQYMBaAFNtU\n' +
13. 'ldgBESf31bwTnYtApIctaSdtMAsGA1UdDwQEAwIBBjAJBgNVHREEAjAAMAkGA1Ud\n' +
14. 'EgQCMAAwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNIADBFAiEAzxzaG2vR\n' +
15. 'zUnFFL3X3lRQ0IOJrb6cvkSZuaFd4bW2lgUCIHW6QGGnECDFMbDNz7Og9kjkt+3k\n' +
16. 'FmEJWqEMYudBH3Ul\n' +
17. '-----END CERTIFICATE-----';
18. let ECC_256_PRIVATE: string =
19. '-----BEGIN PRIVATE KEY-----\n' +
20. 'MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgOYwEyIw3ZNIAL4xO\n' +
21. 'pP6eVcQYcrL2sfnt6vB0z9tKmMmhRANCAAQHTqHhLM6vKLd3s9b3I3bAAIJXGV24\n' +
22. 'FCNUtZmUMqEUqR1mO97yZTLK1JJsGP+uvNHZebNTOh+42RRsC2N7cMMm\n' +
23. '-----END PRIVATE KEY-----';

25. // string转Uint8Array。
26. function stringToUint8Array(str: string): Uint8Array {
27. let arr: number[] = [];
28. for (let i = 0, j = str.length; i < j; i++) {
29. arr.push(str.charCodeAt(i));
30. };
31. return new Uint8Array(arr);
32. }

34. async function createX509Cert(inStream: string): Promise<cert.X509Cert> {
35. let encodingBlob: cert.EncodingBlob = {
36. data: stringToUint8Array(inStream),
37. encodingFormat: cert.EncodingFormat.FORMAT_PEM
38. };
39. let x509Cert: cert.X509Cert = await cert.createX509Cert(encodingBlob);
40. return x509Cert;
41. }

43. async function testCmsDecryptTest() {
44. try {
45. let plainText: Uint8Array = new Uint8Array([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]);
46. let x509CertEc: cert.X509Cert = await createX509Cert(ECC_256_PUBKEY);
47. let cms: cert.CmsGenerator = cert.createCmsGenerator(cert.CmsContentType.ENVELOPED_DATA);
48. let option: cert.CmsGeneratorOptions = {
49. outFormat: cert.CmsFormat.PEM
50. };
51. cms.setRecipientEncryptionAlgorithm(cert.CmsRecipientEncryptionAlgorithm.AES_128_GCM);
52. let recipientInfo: cert.CmsRecipientInfo = {
53. keyAgreeInfo: {
54. cert: x509CertEc,
55. digestAlgorithm: cert.CmsKeyAgreeRecipientDigestAlgorithm.SHA256
56. }
57. };
58. await cms.addRecipientInfo(recipientInfo);
59. console.info('add recipient result: success, digestAlgorithm = ' + recipientInfo.keyAgreeInfo?.digestAlgorithm);
60. let envelopeData = await cms.doFinal(plainText, option);
61. console.info('doFinal result: success, envelopeData = ' + envelopeData);
62. let cipherText = await cms.getEncryptedContentData();
63. console.info('getEncryptedContentData result: success, cipherText = ' + cipherText);
64. let config: cert.CmsEnvelopedDecryptionConfig = {
65. keyInfo: {
66. key: ECC_256_PRIVATE
67. },
68. };
69. let cmsDecrypt: cert.CmsParser = cert.createCmsParser();
70. await cmsDecrypt.setRawData(envelopeData, cert.CmsFormat.PEM);
71. let decPlainText: Uint8Array = await cmsDecrypt.decryptEnvelopedData(config);
72. console.info('[XTS] decryptEnvelopedData result: success, decPlainText = ' + decPlainText);
73. console.info('decryptEnvelopedData result: success.');
74. } catch (error) {
75. console.error(`verifySignedData failed: errCode: ${error.code}, message: ${error.message}`);
76. }
77. }
```

[CreateCmsDecapsulationObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateAlgorithmLibrary/entry/src/main/ets/pages/CreateCmsDecapsulationObject.ets#L16-L96)
