---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-verify-certchain-object
title: 证书链对象的创建和校验
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书算法库框架 > 证书链对象的创建和校验
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0532b59f8a4ca50ddd5cabbfad85ff1c05f524ad6074bd09a8cba4610d640244
---

以校验证书链为例，完成证书链对象的创建，获取证书链中的证书列表以及使用信任锚对证书链进行校验。

## 开发步骤

1. 导入[证书算法库框架模块](../harmonyos-references/js-apis-cert.md)。

   ```
   1. import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 基于已有的证书数据，调用[cert.createX509CertChain](../harmonyos-references/js-apis-cert.md#certcreatex509certchain11)创建X509证书链对象，并返回结果。
3. 调用[x509CertChain.getCertList](../harmonyos-references/js-apis-cert.md#getcertlist11)获取证书链中的X509证书列表。
4. 调用[x509CertChain.validate](../harmonyos-references/js-apis-cert.md#validate11)使用校验参数校验证书链并返回结果。

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { util } from '@kit.ArkTS';

5. let certChainData = '-----BEGIN CERTIFICATE-----\n' +
6. 'MIID6jCCAtKgAwIBAgIIIM2q/TmRoLcwDQYJKoZIhvcNAQELBQAwWjELMAkGA1UE\n' +
7. 'BhMCRU4xEDAOBgNVBAgTB0VuZ2xhbmQxDzANBgNVBAcTBkxvbmRvbjEMMAoGA1UE\n' +
8. 'ChMDdHMyMQwwCgYDVQQLEwN0czIxDDAKBgNVBAMTA3RzMjAeFw0yMzEyMDUwNzM5\n' +
9. 'MDBaFw0yNDEwMzEyMzU5MDBaMGExCzAJBgNVBAYTAkNOMRAwDgYDVQQIEwdKaWFu\n' +
10. 'Z3N1MRAwDgYDVQQHEwdOYW5qaW5nMQwwCgYDVQQKEwN0czMxDDAKBgNVBAsTA3Rz\n' +
11. 'MzESMBAGA1UEAxMJMTI3LjAuMC4xMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB\n' +
12. 'CgKCAQEAtt+2QxUevbolYLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLR\n' +
13. 'p26LFV/F8ebwPyo8YEBKSwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmc\n' +
14. 'rVvLBNMeVnxY86xHpo0MTNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0j\n' +
15. 'zT9GjeUP6JLdLFUZJKUPSTK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/U\n' +
16. 'T+p5ThAMH593zszlz330nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI3\n' +
17. '8MFQFJKvRHfgTAvVsvAvpBUM2DuBKwIDAQABo4GsMIGpMAkGA1UdEwQCMAAwHQYD\n' +
18. 'VR0OBBYEFDfsHTMZwoA6eaDFlBUyDpka+sYtMAsGA1UdDwQEAwID+DAnBgNVHSUE\n' +
19. 'IDAeBggrBgEFBQcDAQYIKwYBBQUHAwIGCCsGAQUFBwMEMBQGA1UdEQQNMAuCCTEy\n' +
20. 'Ny4wLjAuMTARBglghkgBhvhCAQEEBAMCBkAwHgYJYIZIAYb4QgENBBEWD3hjYSBj\n' +
21. 'ZXJ0aWZpY2F0ZTANBgkqhkiG9w0BAQsFAAOCAQEAp5vTvXrt8ZpgRJVtzv9ss0lJ\n' +
22. 'izp1fJf+ft5cDXrs7TSD5oHrSW2vk/ZieIMhexU4LFwhs4OE7jK6pgI48Dseqxx7\n' +
23. 'B/KktxhVMJUmVXd9Ayjp6f+BtZlIk0cArPuoXToXjsV8caTGBXHRdzxpAk/w9syc\n' +
24. 'GYrbH9TrdNMuTizOb+k268oKXUageZNxHmd7YvOXkcNgrd29jzwXKDYYiUa1DISz\n' +
25. 'DnYaJOgPt0B/5izhoWNK7GhJDy9KEuLURcTSWFysbbnljwO9INPT9MmlS83PdAgN\n' +
26. 'iS8VXF4pce1W9U5jH7d7k0JDVSXybebe1iPFphsZpYM/NE+jap+mPy1nTCbf9g==\n' +
27. '-----END CERTIFICATE-----\n' +
28. '-----BEGIN CERTIFICATE-----\n' +
29. 'MIIC0zCCAoWgAwIBAgIIXpLoPpQVWnkwBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
30. 'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
31. 'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDczNzAwWhcNMjQw\n' +
32. 'OTAxMjM1OTAwWjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
33. 'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czIxDDAKBgNVBAsTA3RzMjEMMAoGA1UE\n' +
34. 'AxMDdHMyMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtt+2QxUevbol\n' +
35. 'YLp51QGcUpageI4fwGLIqv4fj4aoVnHFOOBqVOVpfCLRp26LFV/F8ebwPyo8YEBK\n' +
36. 'SwXzMD1573rMSbaH9BalscH5lZYAbetXoio6YRvzlcmcrVvLBNMeVnxY86xHpo0M\n' +
37. 'TNyP7W024rZsxWO98xFQVdoiaBC+7+midlisx2Y+7u0jzT9GjeUP6JLdLFUZJKUP\n' +
38. 'STK3jVzw9v1eZQZKYoNfU6vFMd6ndtwW6qEnwpzmmX/UT+p5ThAMH593zszlz330\n' +
39. 'nTSXBjIsGkyvOz9gSB0Z0LAuJj06XUNhGL5xKJYKbdI38MFQFJKvRHfgTAvVsvAv\n' +
40. 'pBUM2DuBKwIDAQABo28wbTAMBgNVHRMEBTADAQH/MB0GA1UdDgQWBBQ37B0zGcKA\n' +
41. 'OnmgxZQVMg6ZGvrGLTALBgNVHQ8EBAMCAQYwEQYJYIZIAYb4QgEBBAQDAgAHMB4G\n' +
42. 'CWCGSAGG+EIBDQQRFg94Y2EgY2VydGlmaWNhdGUwBQYDK2VwA0EAuasLBe55YgvF\n' +
43. 'b4wmHeohylc9r8cFGS1LNQ5UcSn3sGqMYf6ehnef16NLuCW6upHCs8Sui4iAMvsP\n' +
44. 'uKPWR9dKBA==\n' +
45. '-----END CERTIFICATE-----\n' +
46. '-----BEGIN CERTIFICATE-----\n' +
47. 'MIIB3zCCAZGgAwIBAgIIWQvOEDl+ya4wBQYDK2VwMFoxCzAJBgNVBAYTAkVOMRAw\n' +
48. 'DgYDVQQIEwdFbmdsYW5kMQ8wDQYDVQQHEwZMb25kb24xDDAKBgNVBAoTA3RzMTEM\n' +
49. 'MAoGA1UECxMDdHMxMQwwCgYDVQQDEwN0czEwHhcNMjMxMjA1MDAwMDAwWhcNMjQx\n' +
50. 'MjA0MjM1OTU5WjBaMQswCQYDVQQGEwJFTjEQMA4GA1UECBMHRW5nbGFuZDEPMA0G\n' +
51. 'A1UEBxMGTG9uZG9uMQwwCgYDVQQKEwN0czExDDAKBgNVBAsTA3RzMTEMMAoGA1UE\n' +
52. 'AxMDdHMxMCowBQYDK2VwAyEAuxadj1ww0LqPN24zr28jcSOlSWAe0QdLyRF+ZgG6\n' +
53. 'klKjdTBzMBIGA1UdEwEB/wQIMAYBAf8CARQwHQYDVR0OBBYEFNSgpoQvfxR8A1Y4\n' +
54. 'St8NjOHkRpm4MAsGA1UdDwQEAwIBBjARBglghkgBhvhCAQEEBAMCAAcwHgYJYIZI\n' +
55. 'AYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTAFBgMrZXADQQAblBgoa72X/K13WOvc\n' +
56. 'KW0fqBgFKvLy85hWD6Ufi61k4ProQiZzMK+0+y9jReKelPx/zRdCCgSbQroAR2mV\n' +
57. 'xjoE\n' +
58. '-----END CERTIFICATE-----\n';

60. async function sample() {
61. let textEncoder = new util.TextEncoder();
62. // 证书链二进制数据，需业务自行赋值。
63. const encodingBlob: cert.EncodingBlob = {
64. data: textEncoder.encodeInto(certChainData),
65. // 根据encodingData的格式进行赋值，支持FORMAT_PEM、FORMAT_DER和FORMAT_PKCS7。
66. encodingFormat: cert.EncodingFormat.FORMAT_PEM
67. };
68. let x509CertChain: cert.X509CertChain = {} as cert.X509CertChain;
69. try {
70. x509CertChain = await cert.createX509CertChain(encodingBlob);
71. } catch (err) {
72. let e: BusinessError = err as BusinessError;
73. console.error(`createX509CertChain failed, errCode: ${e.code}, errMsg: ${e.message}`);
74. }

76. try {
77. let certList = x509CertChain.getCertList();
78. } catch (err) {
79. let e: BusinessError = err as BusinessError;
80. console.error(`X509CertChain getCertList failed, errCode: ${e.code}, errMsg: ${e.message}`);
81. }

83. // 证书链校验数据，需业务自行赋值。
84. const param: cert.CertChainValidationParameters = {
85. date: '20231212080000Z',
86. trustAnchors: [{
87. CAPubKey: new Uint8Array([0x30, 0x2a, 0x30, 0x05, 0x06, 0x03, 0x2b, 0x65, 0x70, 0x03, 0x21, 0x00, 0xbb, 0x16,
88. 0x9d, 0x8f, 0x5c, 0x30, 0xd0, 0xba, 0x8f, 0x37, 0x6e, 0x33, 0xaf, 0x6f, 0x23, 0x71, 0x23, 0xa5, 0x49, 0x60,
89. 0x1e, 0xd1, 0x07, 0x4b, 0xc9, 0x11, 0x7e, 0x66, 0x01, 0xba, 0x92, 0x52]),
90. CASubject: new Uint8Array([0x30, 0x5a, 0x31, 0x0b, 0x30, 0x09, 0x06, 0x03, 0x55, 0x04, 0x06, 0x13, 0x02, 0x45,
91. 0x4e, 0x31, 0x10, 0x30, 0x0e, 0x06, 0x03, 0x55, 0x04, 0x08, 0x13, 0x07, 0x45, 0x6e, 0x67, 0x6c, 0x61, 0x6e,
92. 0x64, 0x31, 0x0f, 0x30, 0x0d, 0x06, 0x03, 0x55, 0x04, 0x07, 0x13, 0x06, 0x4c, 0x6f, 0x6e, 0x64, 0x6f, 0x6e,
93. 0x31, 0x0c, 0x30, 0x0a, 0x06, 0x03, 0x55, 0x04, 0x0a, 0x13, 0x03, 0x74, 0x73, 0x31, 0x31, 0x0c, 0x30, 0x0a,
94. 0x06, 0x03, 0x55, 0x04, 0x0b, 0x13, 0x03, 0x74, 0x73, 0x31, 0x31, 0x0c, 0x30, 0x0a, 0x06, 0x03, 0x55, 0x04,
95. 0x03, 0x13, 0x03, 0x74, 0x73, 0x31]),
96. }]
97. };
98. try {
99. const validationRes = await x509CertChain.validate(param);
100. console.info('X509CertChain validate result: success.');
101. } catch (err) {
102. let e: BusinessError = err as BusinessError;
103. console.error(`X509CertChain validate failed, errCode: ${e.code}, errMsg: ${e.message}`);
104. }
105. }
```

[CreateVerifyCertchainObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateAlgorithmLibrary/entry/src/main/ets/pages/CreateVerifyCertchainObject.ets#L16-L125)
