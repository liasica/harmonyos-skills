---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-cms-verify-object
title: 证书CMS验签
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书算法库框架 > 证书CMS验签
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:13f744ec06ab2446a60d6168f1002d81d869c66ef4892d672c42267e600273c2
---

从API 22开始，支持证书CMS验签。

PKCS#7是用于存储签名或加密数据的标准语法。CMS作为PKCS#7的扩展，支持的数据类型包括数据、签名数据、封装数据、签名和封装数据、摘要数据以及加密数据。该标准常用于保护数据的完整性和机密性。

目前仅支持CMS签名数据和封装数据。

## 开发步骤

1. 导入[证书算法库框架模块](../harmonyos-references/js-apis-cert.md)。

   ```
   1. import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 签名的开发步骤查看[CMS签名](create-cms-sign-object.md)。
3. 调用[cert.createCmsParser](../harmonyos-references/js-apis-cert.md#certcreatecmsparser22)创建CmsParser对象。
4. 调用[cmsParser.setRawData](../harmonyos-references/js-apis-cert.md#setrawdata22)设置CMS数据。
5. 调用[cmsParser.verifySignedData](../harmonyos-references/js-apis-cert.md#verifysigneddata22)进行验签。

验签示例：

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. let ECC_256_PUB_ENTRY_CERT: string =
4. '-----BEGIN CERTIFICATE-----\n' +
5. 'MIICejCCAiCgAwIBAgIUGE371/LcCW79mzMm6UiJdyC4khcwCgYIKoZIzj0EAwIw\n' +
6. 'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
7. 'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
8. 'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTAeFw0yNTA5MjgxMDU0MDVa\n' +
9. 'Fw0zNTA5MjYxMDU0MDVaMHUxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\n' +
10. 'MRAwDgYDVQQHDAdCZWlqaW5nMRswGQYDVQQKDBJFQ0RTQSBFeGFtcGxlIENvcnAx\n' +
11. 'CzAJBgNVBAsMAklUMRgwFgYDVQQDDA93d3cuZXhhbXBsZS5jb20wWTATBgcqhkjO\n' +
12. 'PQIBBggqhkjOPQMBBwNCAAQNKO5YXAsmdm/ShEU5VyQlQSdnV6hNQIofHhQ/GyeK\n' +
13. '1W7t3KnMie4cv/wnA4Qmor2KeBBXUFUnYJqqWOHsivIuo4GEMIGBMAkGA1UdEwQC\n' +
14. 'MAAwCwYDVR0PBAQDAgK0MCcGA1UdEQQgMB6CD3d3dy5leGFtcGxlLmNvbYILZXhh\n' +
15. 'bXBsZS5jb20wHQYDVR0OBBYEFD7RUSUimy0SWShmPIus91tDS0u9MB8GA1UdIwQY\n' +
16. 'MBaAFFjgVG0DwmSwxzJWELNvxGtm3mxUMAoGCCqGSM49BAMCA0gAMEUCIQCTw7sx\n' +
17. 'X0tt1xiNvIQ9LD4bECzdgzIuBaU97GgYDusIUgIgTkc0wYZ3EUg0COHPly4cVsTj\n' +
18. '1Cyy/+qufhBUJw5om7E=\n' +
19. '-----END CERTIFICATE-----';

21. let ECC_256_PUB_INTER_CERT: string =
22. '-----BEGIN CERTIFICATE-----\n' +
23. 'MIICTDCCAfGgAwIBAgIUc1x0keEiLIcS1oKtSpeEiPoaepkwCgYIKoZIzj0EAwIw\n' +
24. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
25. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
26. 'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTM0OVoXDTMwMDkyNzEwNTM0OVow\n' +
27. 'fjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
28. 'bmcxHjAcBgNVBAoMFUVDRFNBIEludGVybWVkaWF0ZSBDQTELMAkGA1UECwwCSVQx\n' +
29. 'HjAcBgNVBAMMFUVDRFNBIEludGVybWVkaWF0ZSBDQTBZMBMGByqGSM49AgEGCCqG\n' +
30. 'SM49AwEHA0IABGoCqpHBV/glJeezsp693/hhflYOKpHvaNszVBLkTurkqrbhbaMo\n' +
31. 'hw1oO2Zro54rhZ8tom2UAGn1rzNmRVBCxTajXTBbMAwGA1UdEwQFMAMBAf8wCwYD\n' +
32. 'VR0PBAQDAgEGMB0GA1UdDgQWBBRY4FRtA8JksMcyVhCzb8RrZt5sVDAfBgNVHSME\n' +
33. 'GDAWgBTmNm24RfPnLf1HMNCocS90CGalJjAKBggqhkjOPQQDAgNJADBGAiEAstMv\n' +
34. 'puHi/dgAlvycicL3VQ5iITvUSG2fo286LYc01CQCIQCyw4+94ovyRtaT/WWoZh3u\n' +
35. 'ia4tt478nYeQgMChg+xtSw==\n' +
36. '-----END CERTIFICATE-----';

38. let ECC_256_PUB_ROOT_CERT: string =
39. '-----BEGIN CERTIFICATE-----\n' +
40. 'MIICUzCCAfqgAwIBAgIUPma0DkC+ck+t/3eykmsKsy5D0egwCgYIKoZIzj0EAwIw\n' +
41. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
42. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
43. 'DA1FQ0RTQSBSb290IENBMB4XDTI1MDkyODEwNTMyN1oXDTM1MDkyNjEwNTMyN1ow\n' +
44. 'bjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAOBgNVBAcMB0JlaWpp\n' +
45. 'bmcxFjAUBgNVBAoMDUVDRFNBIFJvb3QgQ0ExCzAJBgNVBAsMAklUMRYwFAYDVQQD\n' +
46. 'DA1FQ0RTQSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEA3KYWepl\n' +
47. 'wjHe/Htx2cAhrjaZpWPJOUyL6siUFRayVebaqOQejuUPypbj+u4ZHodsviUe12E1\n' +
48. '50Q+R9Uayes+WKN2MHQwHQYDVR0OBBYEFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMB8G\n' +
49. 'A1UdIwQYMBaAFOY2bbhF8+ct/Ucw0KhxL3QIZqUmMAsGA1UdDwQEAwIBBjAJBgNV\n' +
50. 'HREEAjAAMAkGA1UdEgQCMAAwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNH\n' +
51. 'ADBEAiAjo+sFDtGVhyc+NqdwxhepqSXOjRI5As6TSz3OYTvERwIgayLgfBn2uABH\n' +
52. 'wYQI60CEJkDF9Pn2fxsGuNEyyn0ks28=\n' +
53. '-----END CERTIFICATE-----';
54. let ECC_256_PRI_ENTRY_KEY: string =
55. '-----BEGIN EC PRIVATE KEY-----\n' +
56. 'MHcCAQEEII8+yfaMTjUyWtjIopGgNxHUMPKhAYTnIVYbiTOVB4x5oAoGCCqGSM49\n' +
57. 'AwEHoUQDQgAEDSjuWFwLJnZv0oRFOVckJUEnZ1e oTUCKHx4UPxsnitVu7dypzInu\n' +
58. 'HL/8JwOEJqK9ingQV1BVJ2Caqljh7IryLg==\n' +
59. '-----END EC PRIVATE KEY-----';

61. // string转Uint8Array。
62. function stringToUint8Array(str: string): Uint8Array {
63. let arr: number[] = [];
64. for (let i = 0, j = str.length; i < j; i++) {
65. arr.push(str.charCodeAt(i));
66. };
67. return new Uint8Array(arr);
68. }

70. async function createX509Cert(inStream: string): Promise<cert.X509Cert> {
71. let encodingBlob: cert.EncodingBlob = {
72. data: stringToUint8Array(inStream),
73. encodingFormat: cert.EncodingFormat.FORMAT_PEM

75. };
76. let x509Cert: cert.X509Cert = await cert.createX509Cert(encodingBlob);

78. return x509Cert;
79. }

81. async function testCmsVerifyTest() {
82. try {
83. let plainText: Uint8Array = new Uint8Array([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]);
84. let x509CertEntry: cert.X509Cert = await createX509Cert(ECC_256_PUB_ENTRY_CERT);
85. let x509CertInter: cert.X509Cert = await createX509Cert(ECC_256_PUB_INTER_CERT);
86. let x509CertRoot: cert.X509Cert = await createX509Cert(ECC_256_PUB_ROOT_CERT);
87. let cms: cert.CmsGenerator = cert.createCmsGenerator(cert.CmsContentType.SIGNED_DATA);
88. let signerConfig: cert.CmsSignerConfig = {
89. mdName: 'SHA256',
90. };
91. let keyInfo: cert.PrivateKeyInfo = {
92. key: ECC_256_PRI_ENTRY_KEY
93. };
94. let option: cert.CmsGeneratorOptions = {
95. outFormat: cert.CmsFormat.PEM
96. };
97. cms.addSigner(x509CertEntry, keyInfo, signerConfig);
98. let signData = cms.doFinalSync(plainText, option);
99. let config: cert.CmsVerificationConfig = {
100. trustCerts: [x509CertRoot, x509CertInter],
101. };
102. let verify: cert.CmsParser = cert.createCmsParser();
103. await verify.setRawData(signData, cert.CmsFormat.PEM);
104. await verify.verifySignedData(config);
105. console.info(`verifySignedData result: success.`);
106. } catch (error) {
107. console.error(`verifySignedData failed: errCode: ${error.code}, message: ${error.message}`);
108. }
109. }
```

[CreateCmsVerifyObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateAlgorithmLibrary/entry/src/main/ets/pages/CreateCmsVerifyObject.ets#L16-L128)
