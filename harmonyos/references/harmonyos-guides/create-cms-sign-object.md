---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-cms-sign-object
title: 证书CMS签名
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书算法库框架 > 证书CMS签名
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:90d61ee95855407071716a062264eb99c2f88484b0754bb970e7d66bc99d5c98
---

从API 18开始，支持证书CMS签名。

从API 22开始，支持证书CMS封装。

PKCS#7是用于存储签名或加密数据的标准语法。CMS作为PKCS#7的扩展，支持的数据类型包括数据、签名数据、封装数据、签名和封装数据、摘要数据以及加密数据。该标准常用于保护数据的完整性和机密性。

目前仅支持CMS签名数据和封装数据。

## 开发步骤

1. 导入[证书算法库框架模块](../harmonyos-references/js-apis-cert.md)。

   ```
   1. import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 调用[cert.createCmsGenerator](../harmonyos-references/js-apis-cert.md#certcreatecmsgenerator18)创建cmsGenerator对象。
3. 调用[cmsGenerator.addSigner](../harmonyos-references/js-apis-cert.md#addsigner18)添加签名者信息。
4. 调用[cmsGenerator.addCert](../harmonyos-references/js-apis-cert.md#addcert18)添加证书。
5. 调用[cmsGenerator.doFinal](../harmonyos-references/js-apis-cert.md#dofinal18)获取Cms最终签名数据。

* 异步方法示例：

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let certData = '-----BEGIN CERTIFICATE-----\n' +
5. 'MIICXjCCAcegAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMEgxCzAJBgNVBAYT\n' +
6. 'AkNOMQwwCgYDVQQIDANzaGExDTALBgNVBAcMBHhpYW4xDTALBgNVBAoMBHRlc3Qx\n' +
7. 'DTALBgNVBAMMBHRlc3QwHhcNMjQxMTIyMDkwNTIyWhcNMzQxMTIwMDkwNTIyWjBI\n' +
8. 'MQswCQYDVQQGEwJDTjEMMAoGA1UECAwDc2hhMQ0wCwYDVQQHDAR4aWFuMQ0wCwYD\n' +
9. 'VQQKDAR0ZXN0MQ0wCwYDVQQDDAR0ZXN0MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB\n' +
10. 'iQKBgQC6nCZTM16Rk2c4P/hwfVm++jqe6GCA/PXXGe4YL218q1dTKMHBGEw8kXi0\n' +
11. 'XLDcyyC2yUn8ywN2QSyly6ke9EE6PGfZywStLp4g2PTTWB04sS3aXT2y+fToiTXQ\n' +
12. '3AxfFYRpB+EgSdSCkJs6jKXVwbzu54kEtQTfs8UdBQ9nVKaJLwIDAQABo1MwUTAd\n' +
13. 'BgNVHQ4EFgQU6QXnt1smb2HRSO/2zuRQnz/SDxowHwYDVR0jBBgwFoAU6QXnt1sm\n' +
14. 'b2HRSO/2zuRQnz/SDxowDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOB\n' +
15. 'gQBPR/+5xzFG1XlTdgwWVvqVxvhGUkbMTGW0IviJ+jbKsi57vnVsOtFzEA6y+bYx\n' +
16. 'xG/kEOcwLtzeVHOQA+ZU5SVcc+qc0dfFiWjL2PSAG4bpqSTjujpuUk+g8ugixbG1\n' +
17. 'a26pkDJhNeB/E3eBIbeydSY0A/dIGb6vbGo6BSq2KvnWAA==\n' +
18. '-----END CERTIFICATE-----\n';

20. let rsaStr1024: string =
21. '-----BEGIN RSA PRIVATE KEY-----\n' +
22. 'Proc-Type: 4,ENCRYPTED\n' +
23. 'DEK-Info: DES-EDE3-CBC,DB0AC6E3BEE16420\n\n' +
24. '1N5xykdckthZnswMV7blxXm2RCqe/OByBfMwFI7JoXR8STtMiStd4xA3W405k1Ma\n' +
25. 'ExpsHgWwZaS23x+sQ1sL1dsqIPMrw1Vr+KrL20vQcCVjXPpGKauafVbtcWQ1r2PZ\n' +
26. 'QJ4KWP6FhUp+sGt2ItODW3dK+1GdqL22ZtANrgFzS42Wh8FSn0UMCf6RG62DK62J\n' +
27. 'z2jtf4XaorrGSjdTeY+fyyGfSyKidIMMBe+IXwlhCgAe7aHSaqXtMsv+BibB7PJ3\n' +
28. 'XmEp1D/0ptL3r46txyYcuy8jSNCkW8er93KKnlRN6KbuYZPvPNncWkzZBzV17t5d\n' +
29. 'QgtvVh32AKgqk5jm8YVnspOFiPrbrK9UN3IW15juFkfnhriM3IrKap4/kW+tfawZ\n' +
30. 'DmHkSyl8xqFK413Rv0UvYBTjOcGbs2BSJYEvp8CIjtA17SvLmNw70K2nXWuQYutY\n' +
31. '+HyucPtHfEqUPQRzWTAMMntTru77u7dxo2WMMMxOtMJO5h7MAnZH9bAFiuO3ewcY\n' +
32. 'eEePg10d8Owcfh9G6kc0HIGT9MMLMi0mTXhpoQTuWPYuSx6uUZL1fsp1x2fuM0qn\n' +
33. 'bdf3+UnATYUu4tgvBHrMV7405Y6Y3PnqOFxVMeAHeOTo6UThtJ10mfeCPXGcUaHo\n' +
34. 'P5enw7h4145cha3+S4hNrUwj3skrtavld7tY74p4DvgZSlCMF3JAm3DhpnEMVcYP\n' +
35. 'Y6TkSevvxOpBvEHE41Y4VBCBwd9clcixI6cSBJKPUU4A/sc/kkNdGFcbzLQCg/zR\n' +
36. '1m7YmBROb2qy4w3lv/uwVnPGLg/YV465irRaN3hgz7/1lm8STKQhmQ==\n' +
37. '-----END RSA PRIVATE KEY-----\n';

39. // string转Uint8Array。
40. function stringToUint8Array(str: string): Uint8Array {
41. let arr: number[] = [];
42. for (let i = 0, j = str.length; i < j; i++) {
43. arr.push(str.charCodeAt(i));
44. }
45. return new Uint8Array(arr);
46. }

48. async function testPkcs7SignByPromise() {
49. let certEncodingBlob: cert.EncodingBlob = {
50. data: stringToUint8Array(certData),
51. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
52. encodingFormat: cert.EncodingFormat.FORMAT_PEM
53. };
54. cert.createX509Cert(certEncodingBlob, (error, x509Cert) => {
55. if (error) {
56. console.error(`createX509Cert failed: errCode: ${error.code}, message: ${error.message}`);
57. } else {
58. try {
59. let cmsContentType = cert.CmsContentType.SIGNED_DATA;
60. let cmsGenerator = cert.createCmsGenerator(cmsContentType);
61. console.info('testPkcs7SignByPromise createCmsGenerator result: success.');
62. let privateKeyInfo: cert.PrivateKeyInfo = {
63. key: rsaStr1024,
64. password: '123456'
65. };
66. // addCert设置为true时，第二次addSigner或者addCert增加相同的证书，会报错。
67. let config: cert.CmsSignerConfig = {
68. mdName: 'SHA256',
69. addCert: false,
70. addAttr: true,
71. addSmimeCapAttr: true
72. }
73. cmsGenerator.addSigner(x509Cert, privateKeyInfo, config);
74. console.info('testPkcs7SignByPromise addSigner result: success.');
75. cmsGenerator.addCert(x509Cert);
76. console.info('testPkcs7SignByPromise addCert result: success.');
77. let content = new Uint8Array([1, 2, 3, 4]);
78. let optionsFinal: cert.CmsGeneratorOptions = {
79. contentDataFormat: cert.CmsContentDataFormat.BINARY,
80. outFormat: cert.CmsFormat.PEM,
81. isDetached: true
82. };
83. cmsGenerator.doFinal(content, optionsFinal).then(result => {
84. console.info('testPkcs7SignByPromise doFinal result: success, result = %s', result);
85. }).catch((error: BusinessError) => {
86. console.error(`testPkcs7SignByPromise failed: errCode: ${error.code}, message: ${error.message}`);
87. });
88. } catch (err) {
89. let e: BusinessError = err as BusinessError;
90. console.error(`testPkcs7SignByPromise failed: errCode: ${e.code}, message: ${e.message}`);
91. }
92. }
93. });
94. }
```

[CreateCmsSignObjectAsync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateAlgorithmLibrary/entry/src/main/ets/pages/CreateCmsSignObjectAsync.ets#L16-L114)

* 同步方法示例：

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let certData = '-----BEGIN CERTIFICATE-----\n' +
5. 'MIICXjCCAcegAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMEgxCzAJBgNVBAYT\n' +
6. 'AkNOMQwwCgYDVQQIDANzaGExDTALBgNVBAcMBHhpYW4xDTALBgNVBAoMBHRlc3Qx\n' +
7. 'DTALBgNVBAMMBHRlc3QwHhcNMjQxMTIyMDkwNTIyWhcNMzQxMTIwMDkwNTIyWjBI\n' +
8. 'MQswCQYDVQQGEwJDTjEMMAoGA1UECAwDc2hhMQ0wCwYDVQQHDAR4aWFuMQ0wCwYD\n' +
9. 'VQQKDAR0ZXN0MQ0wCwYDVQQDDAR0ZXN0MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB\n' +
10. 'iQKBgQC6nCZTM16Rk2c4P/hwfVm++jqe6GCA/PXXGe4YL218q1dTKMHBGEw8kXi0\n' +
11. 'XLDcyyC2yUn8ywN2QSyly6ke9EE6PGfZywStLp4g2PTTWB04sS3aXT2y+fToiTXQ\n' +
12. '3AxfFYRpB+EgSdSCkJs6jKXVwbzu54kEtQTfs8UdBQ9nVKaJLwIDAQABo1MwUTAd\n' +
13. 'BgNVHQ4EFgQU6QXnt1smb2HRSO/2zuRQnz/SDxowHwYDVR0jBBgwFoAU6QXnt1sm\n' +
14. 'b2HRSO/2zuRQnz/SDxowDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOB\n' +
15. 'gQBPR/+5xzFG1XlTdgwWVvqVxvhGUkbMTGW0IviJ+jbKsi57vnVsOtFzEA6y+bYx\n' +
16. 'xG/kEOcwLtzeVHOQA+ZU5SVcc+qc0dfFiWjL2PSAG4bpqSTjujpuUk+g8ugixbG1\n' +
17. 'a26pkDJhNeB/E3eBIbeydSY0A/dIGb6vbGo6BSq2KvnWAA==\n' +
18. '-----END CERTIFICATE-----\n';

20. let rsaStr1024: string  =
21. '-----BEGIN RSA PRIVATE KEY-----\n' +
22. 'Proc-Type: 4,ENCRYPTED\n' +
23. 'DEK-Info: DES-EDE3-CBC,DB0AC6E3BEE16420\n\n' +
24. '1N5xykdckthZnswMV7blxXm2RCqe/OByBfMwFI7JoXR8STtMiStd4xA3W405k1Ma\n' +
25. 'ExpsHgWwZaS23x+sQ1sL1dsqIPMrw1Vr+KrL20vQcCVjXPpGKauafVbtcWQ1r2PZ\n' +
26. 'QJ4KWP6FhUp+sGt2ItODW3dK+1GdqL22ZtANrgFzS42Wh8FSn0UMCf6RG62DK62J\n' +
27. 'z2jtf4XaorrGSjdTeY+fyyGfSyKidIMMBe+IXwlhCgAe7aHSaqXtMsv+BibB7PJ3\n' +
28. 'XmEp1D/0ptL3r46txyYcuy8jSNCkW8er93KKnlRN6KbuYZPvPNncWkzZBzV17t5d\n' +
29. 'QgtvVh32AKgqk5jm8YVnspOFiPrbrK9UN3IW15juFkfnhriM3IrKap4/kW+tfawZ\n' +
30. 'DmHkSyl8xqFK413Rv0UvYBTjOcGbs2BSJYEvp8CIjtA17SvLmNw70K2nXWuQYutY\n' +
31. '+HyucPtHfEqUPQRzWTAMMntTru77u7dxo2WMMMxOtMJO5h7MAnZH9bAFiuO3ewcY\n' +
32. 'eEePg10d8Owcfh9G6kc0HIGT9MMLMi0mTXhpoQTuWPYuSx6uUZL1fsp1x2fuM0qn\n' +
33. 'bdf3+UnATYUu4tgvBHrMV7405Y6Y3PnqOFxVMeAHeOTo6UThtJ10mfeCPXGcUaHo\n' +
34. 'P5enw7h4145cha3+S4hNrUwj3skrtavld7tY74p4DvgZSlCMF3JAm3DhpnEMVcYP\n' +
35. 'Y6TkSevvxOpBvEHE41Y4VBCBwd9clcixI6cSBJKPUU4A/sc/kkNdGFcbzLQCg/zR\n' +
36. '1m7YmBROb2qy4w3lv/uwVnPGLg/YV465irRaN3hgz7/1lm8STKQhmQ==\n' +
37. '-----END RSA PRIVATE KEY-----\n';

39. // string转Uint8Array。
40. function stringToUint8Array(str: string): Uint8Array {
41. let arr: number[] = [];
42. for (let i = 0, j = str.length; i < j; i++) {
43. arr.push(str.charCodeAt(i));
44. }
45. return new Uint8Array(arr);
46. }

48. function testPkcs7SignBySync() {
49. let certEncodingBlob: cert.EncodingBlob = {
50. data: stringToUint8Array(certData),
51. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
52. encodingFormat: cert.EncodingFormat.FORMAT_PEM
53. };
54. cert.createX509Cert(certEncodingBlob, (error, x509Cert) => {
55. if (error) {
56. console.error(`createX509Cert failed: errCode: ${error.code}, message: ${error.message}`);
57. } else {
58. try {
59. let cmsContentType = cert.CmsContentType.SIGNED_DATA;
60. let cmsGenerator = cert.createCmsGenerator(cmsContentType);
61. console.info('testPkcs7SignBySync createCmsGenerator success.');
62. let privateKeyInfo: cert.PrivateKeyInfo = {
63. key: rsaStr1024,
64. password: '123456'
65. };
66. // addCert设置为true时，第二次addSigner或者addCert增加相同的证书，会报错。
67. let config: cert.CmsSignerConfig = {
68. mdName:'SHA256',
69. addCert:false,
70. addAttr:false,
71. addSmimeCapAttr:false
72. }
73. cmsGenerator.addSigner(x509Cert, privateKeyInfo, config);
74. console.info('testPkcs7SignBySync addSigner result: success.');
75. cmsGenerator.addCert(x509Cert);
76. console.info('testPkcs7SignBySync addCert result: success.');
77. let content = new Uint8Array([1,2,3,4]);
78. let optionsFinal: cert.CmsGeneratorOptions = {
79. contentDataFormat : cert.CmsContentDataFormat.BINARY,
80. outFormat : cert.CmsFormat.DER,
81. isDetached : false
82. };
83. let output = cmsGenerator.doFinalSync(content, optionsFinal);
84. console.info('testPkcs7SignBySync doFinalSync result: success, output = %s.', output);
85. } catch (err) {
86. let e: BusinessError = err as BusinessError;
87. console.error(`testPkcs7SignBySync failed: errCode: ${e.code}, message: ${e.message}`);
88. }
89. }
90. });
91. }
```

[CreateCmsSignObjectSync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateAlgorithmLibrary/entry/src/main/ets/pages/CreateCmsSignObjectSync.ets#L16-L110)
