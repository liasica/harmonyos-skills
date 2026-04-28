---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-parse-verify-cert-object
title: 证书对象的创建、解析和校验
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书算法库框架 > 证书对象的创建、解析和校验
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7db8660ed8e8c28efdfc36444c86313efab536b3b580d64d88479f4b54dccd8d
---

以校验证书有效性为例，完成证书对象的创建、解析和校验。

## 开发步骤

1. 导入[证书算法库框架模块](../harmonyos-references/js-apis-cert.md)。

   ```
   1. import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 基于已有的X509证书数据，调用[cert.createX509Cert](../harmonyos-references/js-apis-cert.md#certcreatex509cert)创建证书对象。
3. 解析证书的字段信息。

   此处以获取证书版本、证书序列号、证书颁发者名称、证书主体名称、证书对象的字符串类型数据为例，更多字段信息获取接口请查看[API参考文档](../harmonyos-references/js-apis-cert.md#x509cert)。
4. 调用[X509Cert.getPublicKey](../harmonyos-references/js-apis-cert.md#getpublickey)获取证书中的公钥，并调用[X509Cert.verify](../harmonyos-references/js-apis-cert.md#verify)校验签名。示例为自验签场景，因此获取的是本证书中的公钥。应用须结合自身场景获取用于验签的公钥。
5. 调用[X509Cert.checkValidityWithDate](../harmonyos-references/js-apis-cert.md#checkvaliditywithdate)校验证书有效期。入参date用于确认此日期是否在X509证书有效期内。

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { util } from '@kit.ArkTS';

5. // 此处仅为示例的证书二进制数据，需根据业务的不同对证书数据进行赋值。
6. let certData = '-----BEGIN CERTIFICATE-----\n' +
7. 'MIIBLzCB1QIUO/QDVJwZLIpeJyPjyTvE43xvE5cwCgYIKoZIzj0EAwIwGjEYMBYG\n' +
8. 'A1UEAwwPRXhhbXBsZSBSb290IENBMB4XDTIzMDkwNDExMjAxOVoXDTI2MDUzMDEx\n' +
9. 'MjAxOVowGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYI\n' +
10. 'KoZIzj0DAQcDQgAEHjG74yMIueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTa\n' +
11. 'tUsU0i/sePnrKglj2H8Abbx9PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEA\n' +
12. '0ce/fvA4tckNZeB865aOApKXKlBjiRlaiuq5mEEqvNACIQDPD9WyC21MXqPBuRUf\n' +
13. 'BetUokslUfjT6+s/X4ByaxycAA==\n' +
14. '-----END CERTIFICATE-----\n';

16. // 证书示例
17. function certSample(): void {
18. let textEncoder = new util.TextEncoder();
19. let encodingBlob: cert.EncodingBlob = {
20. // 将证书数据从string类型转换成Uint8Array。
21. data: textEncoder.encodeInto(certData),
22. // 证书格式，仅支持PEM和DER。在此示例中，证书为PEM格式。
23. encodingFormat: cert.EncodingFormat.FORMAT_PEM
24. };

26. // 创建X509Cert实例。
27. cert.createX509Cert(encodingBlob, (err, x509Cert) => {
28. if (err != null) {
29. // 创建X509Cert实例失败。
30. console.error(`createX509Cert failed, errCode:${err.code}, errMsg:${err.message}`);
31. return;
32. }
33. // X509Cert实例创建成功。
34. console.info('createX509Cert result: success.');

36. // 获取证书版本。
37. let version = x509Cert.getVersion();
38. // 获取证书序列号。
39. let serial = x509Cert.getCertSerialNumber();
40. console.info(`X509 version: ${version} , X509 serial:${serial}`);

42. // 获取证书颁发者名称。
43. let issuerName = x509Cert.getIssuerName(cert.EncodingType.ENCODING_UTF8);
44. console.info(`X509 issuerName: ${issuerName}`);

46. // 获取证书主体名称。
47. let subjectNameBin = x509Cert.getSubjectName(cert.EncodingType.ENCODING_UTF8);
48. let encoder = util.TextDecoder.create();
49. let subjectName = encoder.decodeToString(subjectNameBin.data);
50. console.info(`X509 subjectName: ${subjectName}`);

52. // 获取证书对象的字符串类型数据。
53. let certString = x509Cert.toString(cert.EncodingType.ENCODING_UTF8);
54. console.info(`X509 certString: ${certString}`);

56. // 使用上级证书对象的getPublicKey()方法或本（自签名）证书对象获取公钥对象。
57. try {
58. let pubKey = x509Cert.getPublicKey();
59. // 验证证书签名。
60. x509Cert.verify(pubKey, (err, data) => {
61. if (err == null) {
62. // 签名验证成功。
63. console.info('verify result: success.');
64. } else {
65. // 签名验证失败。
66. console.error(`verify failed, errCode: ${err.code} , errMsg:${err.message}`);
67. }
68. });
69. } catch (error) {
70. let e: BusinessError = error as BusinessError;
71. console.error(`getPublicKey failed, errCode: ${e.code} , errMsg:${e.message}`);
72. }

74. // 用一个字符串代表时间。
75. let date = '20230930000001Z';

77. // 验证证书的有效期。
78. try {
79. x509Cert.checkValidityWithDate(date);
80. } catch (error) {
81. let e: BusinessError = error as BusinessError;
82. console.error(`checkValidityWithDate failed, errCode: ${e.code}, errMsg:${e.message}`);
83. }
84. });
85. }
```

[CreateParseVerifyCertObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateAlgorithmLibrary/entry/src/main/ets/pages/CreateParseVerifyCertObject.ets#L16-L105)
