---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/attestation-signature-verification-apps
title: 应用端开发
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 应用真实性证明 > 签名验签识别真实请求 > 应用端开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:10bb262730547a81f73accf4785929ce4b0a4ea21d0c59565e6181d3c206c4eb
---

## 接口说明

接口能力由[Universal Keystore Kit](huks-overview.md)提供，涉及的功能指导请参考：

* [Universal Keystore Kit简介](huks-overview.md)
* [查询密钥是否存在(ArkTS)](huks-check-key-arkts.md)
* [查询密钥是否存在(C/C++)](huks-check-key-ndk.md)
* [生成密钥(ArkTS)](huks-key-generation-arkts.md)
* [生成密钥(C/C++)](huks-key-generation-ndk.md)
* [匿名密钥证明(ArkTS)](huks-key-anon-attestation-arkts.md)
* [匿名密钥证明(C/C++)](huks-key-anon-attestation-ndk.md)
* [签名/验签(ArkTS)](huks-signing-signature-verification-arkts.md)
* [签名/验签(C/C++)](huks-signing-signature-verification-ndk.md)

## 使用前提

使用应用的私钥对业务请求进行签名的前提是已经创建应用公私钥和在服务器保存了应用公钥，相关开发指南请参考：

* [查询应用公私钥对是否存在](device-attestation-apps.md#查询应用公私钥对是否存在)
* [创建应用公私钥对](device-attestation-apps.md#创建应用公私钥对)
* [对应用公钥和应用ID进行证明](device-attestation-apps.md#对应用公钥和应用id进行证明)

## 使用应用私钥对业务请求进行签名

在密钥证明流程处理成功后，您的应用在进行一些安全敏感的端云业务时，可以使用已验证的密钥对业务请求进行安全保护。

应用可以调用Universal Keystore Kit的签名接口，使用应用私钥对业务请求数据（如HTTP请求的Body）进行签名，然后把签名结果数据添加到请求消息中（如HTTP的Header字段）。为了方便应用服务器查找应用公钥用于验签，应用应该在业务请求中携带应用公钥ID。

说明

安全建议：为了在发送业务请求时能够防重放攻击，建议应用先从应用服务器获取一次性的挑战值Challenge。应用服务器采用安全随机数生成挑战值Challenge，并缓存到服务器中。

**示例：**

```
1. import { huks } from '@kit.UniversalKeystoreKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { util } from '@kit.ArkTS';

5. let keyAlias = 'serviceKey_user01'; //业务密钥别名
6. let handle: number;
7. let plaintext = '123456'; //待签名的明文数据，建议包含服务器端返回的Challenge。
8. let signature: Uint8Array; //存储签名结果数据的变量

10. function StringToUint8Array(str: String) {
11. let arr: number[] = new Array();
12. for (let i = 0, j = str.length; i < j; ++i) {
13. arr.push(str.charCodeAt(i));
14. }
15. return new Uint8Array(arr);
16. }

18. function GetSignProperties() {
19. let properties: Array<huks.HuksParam> = new Array();
20. let index = 0;
21. properties[index++] = {
22. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
23. value: huks.HuksKeyAlg.HUKS_ALG_ECC
24. };
25. properties[index++] = {
26. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
27. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
28. };
29. properties[index++] = {
30. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
31. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
32. };
33. properties[index++] = {
34. tag: huks.HuksTag.HUKS_TAG_DIGEST,
35. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
36. }
37. return properties;
38. }

40. async function Sign(keyAlias: string, plaintext: string) {
41. let signProperties = GetSignProperties();
42. let options: huks.HuksOptions = {
43. properties: signProperties,
44. inData: StringToUint8Array(plaintext)
45. }
46. await huks.initSession(keyAlias, options)
47. .then((data) => {
48. handle = data.handle;
49. }).catch((err: BusinessError) => {
50. console.error(`promise: init sign failed, error: ` + err.message);
51. })
52. await huks.finishSession(handle, options)
53. .then((data) => {
54. signature = data.outData as Uint8Array;

56. let base64 = new util.Base64Helper();
57. let signatureBase64 = base64.encodeToStringSync(signature);
58. //todo：把签名结果的Base64编码（signatureBase64变量）发送到云侧的服务器。如下示例代码把签名结果打印到日志中，供调测使用，商用代码不需要打印。
59. console.info(`sign success, result:` + signatureBase64);

61. }).catch((err: BusinessError) => {
62. console.error(`promise: sign failed, error: ` + err.message);
63. })
64. }
```
