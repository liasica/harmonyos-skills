---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/allow-download-intermediate-cert
title: 证书链校验时下载缺失的中间CA证书
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书算法库框架 > 证书链校验时下载缺失的中间CA证书
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d709122da0056f80858af799159a682fe50cb6e83ac8a8ef1f595049d44ba925
---

从API 23开始，支持证书链校验时下载缺失的中间CA证书。

以创建X509证书链为例，完成证书链对象的创建，创建过程校验时允许下载缺失的中间证书。

## 开发步骤

1. 导入[证书算法库框架模块](../harmonyos-references/js-apis-cert.md)。

   ```
   1. import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 基于已有的证书数据，调用[cert.createX509Cert](../harmonyos-references/js-apis-cert.md#certcreatex509cert-1)创建X509证书对象，并返回结果。
3. 调用[cert.buildX509CertChain](../harmonyos-references/js-apis-cert.md#certbuildx509certchain12)创建X509证书链对象，将validationParameters的allowDownloadIntermediateCa参数设置为true，开启允许校验过程中从网络下载缺失的中间CA。

说明

本开发指导中提供的示例代码需要在配置网络的前提下执行。需要申请ohos.permission.INTERNET权限，配置方式请参见[声明权限](declare-permissions.md)。

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { util } from '@kit.ArkTS';

5. let rootCert = '-----BEGIN CERTIFICATE-----\n' +
6. 'MIIDjjCCAnagAwIBAgIQAzrx5qcRqaC7KGSxHQn65TANBgkqhkiG9w0BAQsFADBh\n' +
7. 'MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3\n' +
8. 'd3cuZGlnaWNlcnQuY29tMSAwHgYDVQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBH\n' +
9. 'MjAeFw0xMzA4MDExMjAwMDBaFw0zODAxMTUxMjAwMDBaMGExCzAJBgNVBAYTAlVT\n' +
10. 'MRUwEwYDVQQKEwxEaWdpQ2VydCBJbmMxGTAXBgNVBAsTEHd3dy5kaWdpY2VydC5j\n' +
11. 'b20xIDAeBgNVBAMTF0RpZ2lDZXJ0IEdsb2JhbCBSb290IEcyMIIBIjANBgkqhkiG\n' +
12. '9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuzfNNNx7a8myaJCtSnX/RrohCgiN9RlUyfuI\n' +
13. '2/Ou8jqJkTx65qsGGmvPrC3oXgkkRLpimn7Wo6h+4FR1IAWsULecYxpsMNzaHxmx\n' +
14. '1x7e/dfgy5SDN67sH0NO3Xss0r0upS/kqbitOtSZpLYl6ZtrAGCSYP9PIUkY92eQ\n' +
15. 'q2EGnI/yuum06ZIya7XzV+hdG82MHauVBJVJ8zUtluNJbd134/tJS7SsVQepj5Wz\n' +
16. 'tCO7TG1F8PapspUwtP1MVYwnSlcUfIKdzXOS0xZKBgyMUNGPHgm+F6HmIcr9g+UQ\n' +
17. 'vIOlCsRnKPZzFBQ9RnbDhxSJITRNrw9FDKZJobq7nMWxM4MphQIDAQABo0IwQDAP\n' +
18. 'BgNVHRMBAf8EBTADAQH/MA4GA1UdDwEB/wQEAwIBhjAdBgNVHQ4EFgQUTiJUIBiV\n' +
19. '5uNu5g/6+rkS7QYXjzkwDQYJKoZIhvcNAQELBQADggEBAGBnKJRvDkhj6zHd6mcY\n' +
20. '1Yl9PMWLSn/pvtsrF9+wX3N3KjITOYFnQoQj8kVnNeyIv/iPsGEMNKSuIEyExtv4\n' +
21. 'NeF22d+mQrvHRAiGfzZ0JFrabA0UWTW98kndth/Jsw1HKj2ZL7tcu7XUIOGZX1NG\n' +
22. 'Fdtom/DzMNU+MeKNhJ7jitralj41E6Vf8PlwUHBHQRFXGU7Aj64GxJUTFy8bJZ91\n' +
23. '8rGOmaFvE7FBcf6IKshPECBV1/MUReXgRPTqh5Uykw7+U0b6LJ3/iyK5S9kJRaTe\n' +
24. 'pLiaWN0bfVKfjllDiIGknibVb63dDcY3fe0Dkhvld1927jyNxF1WW6LZZm6zNTfl\n' +
25. 'MrY=\n' +
26. '-----END CERTIFICATE-----';

28. let leafCert = '-----BEGIN CERTIFICATE-----\n' +
29. 'MIIGIzCCBQugAwIBAgIQD8vHwz7g05mDl1F5X17HGzANBgkqhkiG9w0BAQsFADBg\n' +
30. 'MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3\n' +
31. 'd3cuZGlnaWNlcnQuY29tMR8wHQYDVQQDExZSYXBpZFNTTCBUTFMgUlNBIENBIEcx\n' +
32. 'MB4XDTI1MDMyNDAwMDAwMFoXDTI2MDMyMzIzNTk1OVowFzEVMBMGA1UEAwwMKi5k\n' +
33. 'b3ViYW8uY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAw6eEA/GD\n' +
34. 'ShJ0Rtlet3Lf+uYiYzzFJ6J1iJeT/JyvTwDOTKO2VgMjsFHgUcFJBG6QGZT6PXSv\n' +
35. 'vhkdzzIqqXzJwDsqqowwTwMk0YN/JUB0yr/9aFlmQakLZClu1W5og7uxp4ME+ep6\n' +
36. 'aJhoQ9MMCCn3/pvDnLoX1hG9z0pgbUsnIrM+1roLpH+D0FwC4jww7+tDr89/kjb4\n' +
37. '/+LMqjAbe1fLtXJRuxH5O+kAQNqLL/0ECvq+4KpC/r/0UxTlRTpGZY2M3MPUEXfp\n' +
38. 'RKMmkRoRSKwDMJ5u2DK0qanvV6mu7ORPoDsC/fTAiqonjh8rClm/zpj5GN9BQKfu\n' +
39. 'UoaeWIN/XMZSzQIDAQABo4IDIDCCAxwwHwYDVR0jBBgwFoAUDNtsgkkPSmcKuBTu\n' +
40. 'esRIUojrVjgwHQYDVR0OBBYEFCseEe+vZQ8BzqzkOju1EhGQwoCYMCMGA1UdEQQc\n' +
41. 'MBqCDCouZG91YmFvLmNvbYIKZG91YmFvLmNvbTA+BgNVHSAENzA1MDMGBmeBDAEC\n' +
42. 'ATApMCcGCCsGAQUFBwIBFhtodHRwOi8vd3d3LmRpZ2ljZXJ0LmNvbS9DUFMwDgYD\n' +
43. 'VR0PAQH/BAQDAgWgMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjA/BgNV\n' +
44. 'HR8EODA2MDSgMqAwhi5odHRwOi8vY2RwLnJhcGlkc3NsLmNvbS9SYXBpZFNTTFRM\n' +
45. 'U1JTQUNBRzEuY3JsMHYGCCsGAQUFBwEBBGowaDAmBggrBgEFBQcwAYYaaHR0cDov\n' +
46. 'L3N0YXR1cy5yYXBpZHNzbC5jb20wPgYIKwYBBQUHMAKGMmh0dHA6Ly9jYWNlcnRz\n' +
47. 'LnJhcGlkc3NsLmNvbS9SYXBpZFNTTFRMU1JTQUNBRzEuY3J0MAwGA1UdEwEB/wQC\n' +
48. 'MAAwggF9BgorBgEEAdZ5AgQCBIIBbQSCAWkBZwB2AA5XlLzzrqk+MxssmQez95Df\n' +
49. 'm8I9cTIl3SGpJaxhxU4hAAABlcjhhZsAAAQDAEcwRQIhAKfZw1gNPE4sWKi3WL0U\n' +
50. 'vO4EGn+MD1hScKPMNHex6Ty+AiBv0yYWRuEURh/8ywDMHC+1f3xFaj9kshfv389b\n' +
51. 'e09MhAB1AGQRxGykEuyniRyiAi4AvKtPKAfUHjUnq+r+1QPJfc3wAAABlcjhhcUA\n' +
52. 'AAQDAEYwRAIgClXL9SnQFh+6HEqsT/3aBM6jK9NmzG+hrmJGowOKVFYCIEsGPJda\n' +
53. 'TtsBnc/PrhZSjOHitpzrzKhW02hHOzkrtlR/AHYASZybad4dfOz8Nt7Nh2SmuFuv\n' +
54. 'CoeAGdFVUvvp6ynd+MMAAAGVyOGF3gAABAMARzBFAiBExgNNV8q5xfdSU+yL6NAJ\n' +
55. 'l1ze5IYXTetQf04caLUhKgIhALvTCHHHdvokmFbRKQvrY50ihwDoHd4pKbzRtyQ0\n' +
56. 'H16bMA0GCSqGSIb3DQEBCwUAA4IBAQAsjyQpYDf1JiYBsO4koUcFPeAdvTp9FbRL\n' +
57. 'yC0PN34rekPHwcjqsEU7mbuUaZ4EMklHqIqkniStPcKyIDCpSwBu17iezM57fwJA\n' +
58. 'tb9XfzjxZH1vWEFHImcvMEwR0BLRmwXUnnRt3qOeetTV/UpIwH4HGfHldtRNqSnj\n' +
59. 'xDiM1c2oRjv+4Qs5CTet70NHsaQBjkUWvioCgigE+vuCPnjwVNXJkfSHjC+DWWzf\n' +
60. 'Nc+rSFEOvO8Fe4d2rvboT7vXigvTciOeQdig9ySCJQCkWxOvB1AcvZc+kw0YhrpM\n' +
61. 'xUBhDd+DaUWOgmmVS3n6k3GfOqm2EU7iCp8KyfRu2DAsnlsO/YpH\n' +
62. '-----END CERTIFICATE-----';

64. // string转Uint8Array。
65. function stringToUint8Array(str: string): Uint8Array {
66. const encoder = new util.TextEncoder();
67. return encoder.encodeInto(str);
68. }

70. async function createX509Cert(certData: string): Promise<cert.X509Cert> {
71. // 证书二进制数据，需业务自行赋值。
72. let encodingBlob: cert.EncodingBlob = {
73. data: stringToUint8Array(certData),
74. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
75. encodingFormat: cert.EncodingFormat.FORMAT_PEM
76. };

78. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
79. try {
80. x509Cert = await cert.createX509Cert(encodingBlob);
81. } catch (error) {
82. let e: BusinessError = error as BusinessError;
83. console.error(`createX509Cert failed: errCode: ${e.code}, message: ${e.message}`);
84. }
85. return x509Cert;
86. }

88. async function buildX509CertChain() {
89. try {
90. const root = await createX509Cert(rootCert);
91. const leaf = await createX509Cert(leafCert);
92. let certCrlCollection = cert.createCertCRLCollection([leaf, root]);
93. let param: cert.CertChainBuildParameters = {
94. certMatchParameters: {},
95. validationParameters: {
96. certCRLs: [certCrlCollection],
97. allowDownloadIntermediateCa: true,
98. trustAnchors: [{ CACert: root }],
99. }
100. }
101. let data = await cert.buildX509CertChain(param);
102. console.info('buildX509CertChain result: success, certChainLength = ' + data.certChain.getCertList().length);
103. } catch (err) {
104. console.error(`buildX509CertChain failed: errCode: ${err.code}, message: ${err.message}`);
105. }
106. }
```

[AllowDownloadIntermediateCert.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateAlgorithmLibrary/entry/src/main/ets/pages/AllowDownloadIntermediateCert.ets#L16-L125)
