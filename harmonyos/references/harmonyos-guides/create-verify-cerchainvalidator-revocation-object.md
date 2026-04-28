---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-verify-cerchainvalidator-revocation-object
title: 证书链在线校验证书吊销状态
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书算法库框架 > 证书链在线校验证书吊销状态
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e76bca99b703d990d778d951678bbdfdc4878bf16c5a335808d9fbe2f50e9d11
---

## 本地证书链吊销状态校验时仅校验终端实体证书

API 22开始支持本地证书链吊销状态校验时仅校验终端实体证书。

### 开发步骤

1. 导入[证书算法库框架模块](../harmonyos-references/js-apis-cert.md)。

   ```
   1. import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 调用[cert.createX509CertChain](../harmonyos-references/js-apis-cert.md#certcreatex509certchain11)创建证书链对象。
3. 调用[cert.createX509Cert](../harmonyos-references/js-apis-cert.md#certcreatex509cert)创建X509证书对象。
4. 调用[cert.createX509CRL](../harmonyos-references/js-apis-cert.md#certcreatex509crl11)创建X509证书吊销列表对象。
5. 构造[cert.CertChainValidationParameters](../harmonyos-references/js-apis-cert.md#certchainvalidationparameters11)证书链校验参数对象。
6. 调用[cert.validate](../harmonyos-references/js-apis-cert.md#validate11)，传入证书链校验参数，进行证书链校验。

本地仅校验终端实体证书的吊销状态示例：

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: number[] = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. async function createCertChain(certData: string): Promise<cert.X509CertChain> {
13. // 证书二进制数据，需业务自行赋值。
14. let encodingBlob: cert.EncodingBlob = {
15. data: stringToUint8Array(certData),
16. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
17. encodingFormat: cert.EncodingFormat.FORMAT_PEM
18. };

20. let x509CertChain: cert.X509CertChain = {} as cert.X509CertChain;
21. try {
22. x509CertChain = await cert.createX509CertChain(encodingBlob);
23. } catch (err) {
24. console.error(`createCertChain failed: errCode: ${err.code}, message: ${err.message}`);
25. }
26. return x509CertChain;
27. }

29. async function createCert(certData: string): Promise<cert.X509Cert> {
30. // 证书二进制数据，需业务自行赋值。
31. let encodingBlob: cert.EncodingBlob = {
32. data: stringToUint8Array(certData),
33. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
34. encodingFormat: cert.EncodingFormat.FORMAT_PEM
35. };

37. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
38. try {
39. x509Cert = await cert.createX509Cert(encodingBlob);
40. } catch (err) {
41. console.error(`createCert failed: errCode: ${err.code}, message: ${err.message}`);
42. }
43. return x509Cert;
44. }

46. export async function createCRL(crmPem: string): Promise<cert.CertCRLCollection> {
47. try {
48. let crlEncodingBlob: cert.EncodingBlob = {
49. data: stringToUint8Array(crmPem),
50. encodingFormat: cert.EncodingFormat.FORMAT_PEM
51. }
52. let crl: cert.X509CRL = await cert.createX509CRL(crlEncodingBlob);
53. let collection: cert.CertCRLCollection = cert.createCertCRLCollection([], [crl]);
54. return collection;
55. } catch (error) {
56. throw error as Error;
57. }
58. }
59. // ...
60. async function doTestLeafCertCrlCheck() {
61. try {
62. let x509CertChain: cert.X509CertChain = await createCertChain(certChainData);
63. let x509Cert: cert.X509Cert = await createCert(trustRootCertPem);
64. let caCollection: cert.CertCRLCollection = await createCRL(crl);
65. const param: cert.CertChainValidationParameters = {
66. date: '20250926080000Z',
67. trustAnchors: [{
68. CACert: x509Cert
69. }],
70. certCRLs: [caCollection],
71. revocationCheckParam: {
72. options: [
73. cert.RevocationCheckOptions.REVOCATION_CHECK_OPTION_LOCAL_CRL_ONLY_CHECK_END_ENTITY_CERT
74. ],
75. }
76. };
77. await x509CertChain.validate(param);
78. console.info(`validate result: success.`);
79. } catch (error) {
80. console.error(`x509CertChain validate failed: errCode: ${error.code}, message: ${error.message}`);
81. }
82. }
```

[CreateOnlyCheckLeafCertRevocateObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateAlgorithmLibrary/entry/src/main/ets/pages/CreateOnlyCheckLeafCertRevocateObject.ets#L16-L184)

## 在线校验证书链中的中间CA证书的吊销状态

从API 22开始，支持在线校验证书链中的中间CA证书的吊销状态。

### 开发步骤

1. 导入[证书算法库框架模块](../harmonyos-references/js-apis-cert.md)。

   ```
   1. import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 调用[cert.createX509CertChain](../harmonyos-references/js-apis-cert.md#certcreatex509certchain11)创建证书链对象。
3. 调用[cert.createX509Cert](../harmonyos-references/js-apis-cert.md#certcreatex509cert)创建X509证书对象。
4. 构造[cert.CertChainValidationParameters](../harmonyos-references/js-apis-cert.md#certchainvalidationparameters11)证书链校验参数。
5. 调用[cert.validate](../harmonyos-references/js-apis-cert.md#validate11)，传入证书链校验参数，进行证书链校验。

说明

本开发指导中提供的示例代码需要在配置网络的前提下执行。

在线校验中间证书的吊销状态示例：

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: number[] = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. async function createCertChain(certData: string): Promise<cert.X509CertChain> {
13. // 证书二进制数据，需业务自行赋值。
14. let encodingBlob: cert.EncodingBlob = {
15. data: stringToUint8Array(certData),
16. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
17. encodingFormat: cert.EncodingFormat.FORMAT_PEM
18. };

20. let x509CertChain: cert.X509CertChain = {} as cert.X509CertChain;
21. try {
22. x509CertChain = await cert.createX509CertChain(encodingBlob);
23. } catch (err) {
24. console.error(`createCertChain failed: errCode: ${err.code}, message: ${err.message}`);
25. }
26. return x509CertChain;
27. }

29. async function createCert(certData: string): Promise<cert.X509Cert> {
30. // 证书二进制数据，需业务自行赋值。
31. let encodingBlob: cert.EncodingBlob = {
32. data: stringToUint8Array(certData),
33. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
34. encodingFormat: cert.EncodingFormat.FORMAT_PEM
35. };

37. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
38. try {
39. x509Cert = await cert.createX509Cert(encodingBlob);
40. } catch (err) {
41. console.error(`createCert failed: errCode: ${err.code}, message: ${err.message}`);
42. }
43. return x509Cert;
44. }

46. // ...
47. async function doTestCaCheck() {
48. try {
49. let x509CertChain: cert.X509CertChain = await createCertChain(caChain);
50. let x509Cert: cert.X509Cert = await createCert(caTrustCert);
51. const param: cert.CertChainValidationParameters = {
52. trustAnchors: [{
53. CACert: x509Cert
54. }],
55. revocationCheckParam: {
56. options: [
57. cert.RevocationCheckOptions.REVOCATION_CHECK_OPTION_ACCESS_NETWORK,
58. cert.RevocationCheckOptions.REVOCATION_CHECK_OPTION_CHECK_INTERMEDIATE_CA_ONLINE
59. ],
60. }
61. };
62. await x509CertChain.validate(param);
63. console.info(`validate result: success.`);
64. } catch (error) {
65. console.error(`x509CertChain validate failed: errCode: ${error.code}, message: ${error.message}`);
66. }
67. }
```

[CreateOnlineCheckIntermediateCertificateonlyObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateAlgorithmLibrary/entry/src/main/ets/pages/CreateOnlineCheckIntermediateCertificateonlyObject.ets#L16-L159)

## 证书链校验时忽略在线证书吊销检查的网络不可达异常

从API 23开始，支持证书链校验时忽略网络不可达的在线证书吊销检查异常。

### 开发步骤

1. 导入[证书算法库框架模块](../harmonyos-references/js-apis-cert.md)。

   ```
   1. import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 调用[cert.createX509CertChain](../harmonyos-references/js-apis-cert.md#certcreatex509certchain11-2)创建证书链对象。
3. 调用[cert.createX509Cert](../harmonyos-references/js-apis-cert.md#certcreatex509cert)创建X509证书对象。构造 cert.CertChainValidationParameters 证书链校验参数，配置 revocationCheckParam 为 RevocationCheckOptions.REVOCATION\_CHECK\_OPTION\_IGNORE\_NETWORK\_ERROR，以忽略网络不可达的情况。
4. 调用[cert.validate](../harmonyos-references/js-apis-cert.md#validate11)，传入证书链校验参数，进行证书链校验。

在线CRL检查忽略网络不可达异常示例：

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { util } from '@kit.ArkTS';

5. // string转Uint8Array。
6. function stringToUint8Array(str: string): Uint8Array {
7. const encoder = new util.TextEncoder();
8. return encoder.encodeInto(str);
9. }
10. // ...
11. async function createX509Cert(certData: string): Promise<cert.X509Cert> {
12. // 证书二进制数据，需业务自行赋值。
13. let encodingBlob: cert.EncodingBlob = {
14. data: stringToUint8Array(certData),
15. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
16. encodingFormat: cert.EncodingFormat.FORMAT_PEM
17. };

19. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
20. try {
21. x509Cert = await cert.createX509Cert(encodingBlob);
22. } catch (error) {
23. let e: BusinessError = error as BusinessError;
24. console.error(`createX509Cert failed: errCode: ${e.code}, message: ${e.message}`);
25. }
26. return x509Cert;
27. }

29. async function createX509CertChain(): Promise<cert.X509CertChain> {
30. const root = await createX509Cert(rootCert);
31. const intermediate = await createX509Cert(intermediateCert);
32. const leaf = await createX509Cert(leafCert);
33. let x509CertChain: cert.X509CertChain = {} as cert.X509CertChain;
34. try {
35. x509CertChain = cert.createX509CertChain([leaf, intermediate, root]);
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`createX509CertChain failed: errCode: ${e.code}, message: ${e.message}`);
39. }
40. return x509CertChain;
41. }

43. async function validateCRL() {
44. const certChain = await createX509CertChain();
45. console.info('createX509CertChain result: success.');
46. const root = await createX509Cert(rootCert);
47. // 证书链校验数据，需业务自行赋值。
48. const param: cert.CertChainValidationParameters = {
49. trustAnchors: [{ CACert: root }],
50. revocationCheckParam: {
51. options: [
52. cert.RevocationCheckOptions.REVOCATION_CHECK_OPTION_IGNORE_NETWORK_ERROR,
53. cert.RevocationCheckOptions.REVOCATION_CHECK_OPTION_ACCESS_NETWORK
54. ],
55. }
56. }
57. try {
58. await certChain.validate(param);
59. console.info('validateCRL result: success.');
60. } catch (err) {
61. console.error(`X509CertChain validate failed: errCode: ${err.code}, message: ${err.message}`);
62. }
63. }
```

[IgnoreNetworkUnreachable.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateAlgorithmLibrary/entry/src/main/ets/pages/IgnoreNetworkUnreachable.ets#L16-L168)
