---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-hmac-arkts
title: HMAC(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > HMAC > HMAC(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8cf0f39be0fbe738f58233f436573c5ef681ada2bc70a17b8a18cfe0739b8b87
---

HMAC是密钥相关的哈希运算消息认证码（Hash-based Message Authentication Code）。具体的场景介绍及支持的算法规格，请参考[HMAC介绍及算法规格](huks-hmac-overview.md)。

## 开发步骤

**生成密钥**

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集。
3. 调用[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)生成密钥，HMAC支持的规格请参考[密钥生成支持的算法](huks-key-generation-overview.md#支持的算法)。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md#支持的算法)的规格介绍，导入已有的密钥。

**执行HMAC**

1. 获取密钥别名。
2. 获取待运算的数据。
3. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
4. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，获取哈希后的数据。

```
1. /*
2. * 以下以HMAC密钥的Promise操作使用为例
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';

6. let hmacKeyAlias = 'test_HMAC';
7. let handle: number;
8. let plainText = '123456';
9. let hashData: Uint8Array;

11. function stringToUint8Array(str: String) {
12. let arr: number[] = [];
13. for (let i = 0, j = str.length; i < j; ++i) {
14. arr.push(str.charCodeAt(i));
15. }
16. return new Uint8Array(arr);
17. }

19. function uint8ArrayToString(fileData: Uint8Array) {
20. let dataString = '';
21. for (let i = 0; i < fileData.length; i++) {
22. dataString += String.fromCharCode(fileData[i]);
23. }
24. return dataString;
25. }

27. function getHMACProperties() {
28. const properties: huks.HuksParam[] = [{
29. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
30. value: huks.HuksKeyAlg.HUKS_ALG_HMAC
31. }, {
32. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
33. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
34. }, {
35. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
36. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_MAC
37. }, {
38. tag: huks.HuksTag.HUKS_TAG_DIGEST,
39. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA384,
40. }];
41. return properties;
42. }

44. /* 1.生成 HMAC 密钥 */
45. async function generateHMACKey() {
46. let options: huks.HuksOptions = {
47. properties: getHMACProperties()
48. };

50. await huks.generateKeyItem(hmacKeyAlias, options)
51. .then((data) => {
52. console.info(`promise: generate HMAC Key success`);
53. }).catch((error: Error) => {
54. console.error(`promise: generate HMAC Key failed, ${JSON.stringify(error)}`);
55. throw (error as Error);
56. })
57. }
58. /* 2.执行 HMAC 计算 */
59. async function hMACData() {
60. let options: huks.HuksOptions = {
61. properties: getHMACProperties(),
62. inData: stringToUint8Array(plainText)
63. }

65. await huks.initSession(hmacKeyAlias, options)
66. .then((data) => {
67. handle = data.handle;
68. }).catch((error: Error) => {
69. console.error(`promise: init session failed, ${JSON.stringify(error)}`);
70. throw (error as Error);
71. })

73. await huks.finishSession(handle, options)
74. .then((data) => {
75. console.info(`promise: HMAC data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
76. hashData = data.outData as Uint8Array;
77. }).catch((error: Error) => {
78. console.error(`promise: HMAC data failed, ${JSON.stringify(error)}`);
79. throw (error as Error);
80. })
81. }

83. async function executeHMAC() {
84. await generateHMACKey();
85. await hMACData();
86. }
```

[HMAC.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/HMAC/entry/src/main/ets/pages/HMAC.ets#L16-L103)
