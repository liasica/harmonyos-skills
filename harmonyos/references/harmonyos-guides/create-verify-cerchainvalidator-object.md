---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-verify-cerchainvalidator-object
title: 证书链校验器对象的创建和校验
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书算法库框架 > 证书链校验器对象的创建和校验
category: harmonyos-guides
scraped_at: 2026-04-29T13:31:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:aeaafb284690b93c27e29e9102f5005fb88badcf5bd14d76e2c127cfb9c85dc2
---

证书链是由一组证书组成的证书集合，以图中样例证书文件为例，即可放在一个证书链中。

样例中可以看到GlobalSign自签名了证书，GlobalSign也签发了GlobalSign RSA OV SSL CA 2018的证书，GlobalSign RSA OV SSL CA 2018又签发了第三级证书。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/SAEB_kLTSheawmZKOMLaDQ/zh-cn_image_0000002558764878.png?HW-CC-KV=V1&HW-CC-Date=20260429T053123Z&HW-CC-Expire=86400&HW-CC-Sign=53C0780AFCC6FCA0CE9A967EF3C890A96F8C9BBE79C021C77E3635C8BE2D9829)

开发者可以参考示例将已有的多个证书构建出证书链数据。

## 开发步骤

1. 导入[证书算法库框架模块](../harmonyos-references/js-apis-cert.md)。

   ```
   1. import { cert } from '@kit.DeviceCertificateKit';
   ```
2. [cert.createCertChainValidator](../harmonyos-references/js-apis-cert.md#certcreatecertchainvalidator)创建证书链校验器对象。
3. 基于已有的证书数据，创建证书链数据对象[CertChainData](../harmonyos-references/js-apis-cert.md#certchaindata)。

   证书算法库框架提供了证书链校验器对象可用于校验证书链，以验证信任链根源，但待校验的证书链数据对象应符合证书链数据对象的数据结构定义[CertChainData](../harmonyos-references/js-apis-cert.md#certchaindata)。
4. 调用[CertChainValidator.validate](../harmonyos-references/js-apis-cert.md#validate)校验证书链数据。

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { util } from '@kit.ArkTS';

4. // CA数据，这只是一个示例，需要根据具体业务来赋值。
5. let caCertData = '-----BEGIN CERTIFICATE-----\n' +
6. 'MIIDgTCCAmmgAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMFcxCzAJBgNVBAYT\n' +
7. 'AkNOMQ8wDQYDVQQIDAbpmZXopb8xDzANBgNVBAcMBuilv+WuiTEPMA0GA1UECgwG\n' +
8. '5rWL6K+VMRUwEwYDVQQDDAzkuK3mlofmtYvor5UwHhcNMjUwMjIwMDI1NjMxWhcN\n' +
9. 'MzUwMjE4MDI1NjMxWjBXMQswCQYDVQQGEwJDTjEPMA0GA1UECAwG6ZmV6KW/MQ8w\n' +
10. 'DQYDVQQHDAbopb/lrokxDzANBgNVBAoMBua1i+ivlTEVMBMGA1UEAwwM5Lit5paH\n' +
11. '5rWL6K+VMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyY30ubE33Zmc\n' +
12. 'BBM4OIpD1UuDVKynC4xNBK4v79vnlc4ElmRZD4RjkS612DtpaUzt/yHMZXmJTdqg\n' +
13. '2jq7UG4sQc0G3uNGIXdUpRZpnUYGVftuZMxHaNOb+IgDkZzaO3Dk33piOpH/X/Ke\n' +
14. 'OosCbm7eBL+y+wRhUsLSCEasEsIvW3edHuYLrfz3MzwY/9AmnwqDGdRJ5rPayODD\n' +
15. 'HH0yw9JuRkdMacN8omVX8jBfJeI8KafcQW8MJz+Y0qyQyiZ6A81AQSVfT+6Sk2U3\n' +
16. 'UqeSTmtdIL1u29HfYLwYGHey+1Ro2wxqnMsFKIdKu2dDMDQZx61pER/dFtPYFlS7\n' +
17. '/uh3mi9HUQIDAQABo1MwUTAdBgNVHQ4EFgQUGDykmR825RPNFIEQaFzUqkr+CIow\n' +
18. 'HwYDVR0jBBgwFoAUGDykmR825RPNFIEQaFzUqkr+CIowDwYDVR0TAQH/BAUwAwEB\n' +
19. '/zANBgkqhkiG9w0BAQsFAAOCAQEAXjlmYKjBz1ajWywZNlN+LVRXNx7bS4TYtOc2\n' +
20. 'ME4N1ls6yjWSLtBe4DdkBqZ2HwrVW4dg5xZdAS/T0v/rRiGbX6iUFRV9WCTdtLZB\n' +
21. 'HKNh7vU39F7mgTaaWXQK/+6NeLKMzwJENRRaESI/sXeKE6irfJgYuq3NH8GGFd+w\n' +
22. 'HnvVBHRb6WSlY2s5Li7t6lj40UbwOljnqzRQvBeX57rOnzJgVKND3oY9pex/05Oe\n' +
23. '96x+qc2iqZbu54A6NYCTj/65EEKoj5rYxPXMV4FegV42ouaLJJoS+cEEY7w+ixcl\n' +
24. '04TjtjEdhTZiJCmI0RK50H2SWC0t9qkFewM3CCWTHY5ygPtMGA==\n' +
25. '-----END CERTIFICATE-----\n';

27. // 二级CA证书数据，这只是一个示例，需要根据具体业务来赋值。
28. let secondCaCertData = '-----BEGIN CERTIFICATE-----\n' +
29. 'MIIDgTCCAmmgAwIBAgIGAXKnJjrBMA0GCSqGSIb3DQEBCwUAMFcxCzAJBgNVBAYT\n' +
30. 'AkNOMQ8wDQYDVQQIDAbpmZXopb8xDzANBgNVBAcMBuilv+WuiTEPMA0GA1UECgwG\n' +
31. '5rWL6K+VMRUwEwYDVQQDDAzkuK3mlofmtYvor5UwHhcNMjUwMjIwMDI1NjU3WhcN\n' +
32. 'MzUwMjE4MDI1NjU3WjBXMQswCQYDVQQGEwJDTjEPMA0GA1UECAwG6ZmV6KW/MQ8w\n' +
33. 'DQYDVQQHDAbopb/lrokxDzANBgNVBAoMBua1i+ivlTEVMBMGA1UEAwwM5Lit5paH\n' +
34. '5rWL6K+VMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxSL5L7fwMaRF\n' +
35. 'RiT1l7kpzaAqZe33/3lgexoMfGiIFarIhYyYJsmOJKes2uLSnPeqEtscrXmFQiIG\n' +
36. '0srmwrriGgo3oxDp4/5i1FhCf3FqZUwD/RJhtVmkHT0HoYl4cpt/dJSF/e5vxt/J\n' +
37. '2Z1eRIQOj9DzyqET6+ONQmfVOyzEH6xlpXHZLvykSZ7ytPp25LxULPWjTmpDOPRq\n' +
38. 'vkSMaH4H3mPw/Z9r0MVKP7DgAZMl2yVudHp785AMTVD0L9zWGHf3sek25ek5nv2r\n' +
39. 'SlB21MTBpvd8GC/iGns4V3Bvf75WAMgpGghAkRRyADeqt5Hw+x9BIb9FcfE+h6n+\n' +
40. '6EF6FPa8GQIDAQABo1MwUTAdBgNVHQ4EFgQUjt2Crk/j6W8WCdHWyz4H+Q2/3PYw\n' +
41. 'HwYDVR0jBBgwFoAUGDykmR825RPNFIEQaFzUqkr+CIowDwYDVR0TAQH/BAUwAwEB\n' +
42. '/zANBgkqhkiG9w0BAQsFAAOCAQEAksPHMuVF9e2GMVlaSe1Ao9D1KrJvKNaFZPCI\n' +
43. 'lQe2CDsX+Qu7sQj4SML5vvWFLtcAp6ZovqUyEM0PtZWVSjPCRTMJ3ofBPwnXvQ2N\n' +
44. '7J7NCDA227MQabXeN3jMhkcAzlpdO5poTnobPF4xRqb39jM7otnNJsujvzdDab2l\n' +
45. 'LiP4eU5TrEaF2lwidBWJX0VoLrRpqzQhiWXGMpCBBugP5U+bFs20wezJBG19WYyc\n' +
46. '2xKKfvyIcxrpmvjLZl8HddS7Ot1CKXyc8U9QZBGAlPwOXu8juppcEtjJyl36EnvF\n' +
47. 'YAcwrXOAtCiNpX3UnLUbG8GtpOOWQWCt+x1gKmA6V0jbqQmqcw==\n' +
48. '-----END CERTIFICATE-----\n';

50. // 证书链校验器示例。在这个示例中，验证了一个二级证书链。
51. function certChainValidatorSample(): void {
52. let textEncoder = new util.TextEncoder();
53. // 证书链校验器算法。目前仅支持PKIX。
54. let algorithm = 'PKIX';

56. // 创建一个证书链校验器实例。
57. let validator = cert.createCertChainValidator(algorithm);

59. // CA证书数据。
60. let uint8ArrayOfCaCertData = textEncoder.encodeInto(caCertData);

62. // CA证书数据的长度。
63. let uint8ArrayOfCaCertDataLen = new Uint8Array(new Uint16Array([uint8ArrayOfCaCertData.byteLength]).buffer);

65. // 二级CA证书数据。
66. let uint8ArrayOf2ndCaCertData = textEncoder.encodeInto(secondCaCertData);

68. // 二级CA证书数据的长度。
69. let uint8ArrayOf2ndCaCertDataLen = new Uint8Array(new Uint16Array([uint8ArrayOf2ndCaCertData.byteLength]).buffer);

71. // 证书链二进制数据：二级CA证书数据长度+二级CA证书数据+CA证书数据长度+CA证书数据（L-V格式）。
72. let encodingData = new Uint8Array(uint8ArrayOf2ndCaCertDataLen.length + uint8ArrayOf2ndCaCertData.length +
73. uint8ArrayOfCaCertDataLen.length + uint8ArrayOfCaCertData.length);
74. for (let i = 0; i < uint8ArrayOf2ndCaCertDataLen.length; i++) {
75. encodingData[i] = uint8ArrayOf2ndCaCertDataLen[i];
76. }
77. for (let i = 0; i < uint8ArrayOf2ndCaCertData.length; i++) {
78. encodingData[uint8ArrayOf2ndCaCertDataLen.length + i] = uint8ArrayOf2ndCaCertData[i];
79. }
80. for (let i = 0; i < uint8ArrayOfCaCertDataLen.length; i++) {
81. encodingData[uint8ArrayOf2ndCaCertDataLen.length + uint8ArrayOf2ndCaCertData.length + i] =
82. uint8ArrayOfCaCertDataLen[i];
83. }
84. for (let i = 0; i < uint8ArrayOfCaCertData.length; i++) {
85. encodingData[uint8ArrayOf2ndCaCertDataLen.length + uint8ArrayOf2ndCaCertData.length +
86. uint8ArrayOfCaCertDataLen.length + i] = uint8ArrayOfCaCertData[i];
87. }

89. let certChainData: cert.CertChainData = {
90. // Uint8Array类型：L-V格式（证书数据长度-证书数据）。
91. data: encodingData,
92. // 证书的数量。本例中为2。
93. count: 2,
94. // 证书格式。仅支持 PEM 和 DER。在此示例中，证书为 PEM 格式。
95. encodingFormat: cert.EncodingFormat.FORMAT_PEM
96. };

98. // 验证证书链。
99. validator.validate(certChainData, (err, data) => {
100. if (err != null) {
101. // 校验失败。
102. console.error(`validate failed, errCode: ${err.code}, errMsg: ${err.message}`);
103. } else {
104. // 校验成功。
105. console.info('validate result: success.');
106. }
107. });
108. }
```

[CreateVerifyCerchainvalidatorObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateAlgorithmLibrary/entry/src/main/ets/pages/CreateVerifyCerchainvalidatorObject.ets#L18-L129)
