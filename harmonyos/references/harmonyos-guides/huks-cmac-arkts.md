---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-cmac-arkts
title: CMAC(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > CMAC > CMAC(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ea9ce5acd49fcbf296b7b5aad036dd2ce03af27800fb4170137f16925284865d
---

CMAC是基于对称密钥分组加密算法的消息认证码（Cipher-based Message Authentication Code），目前支持3DES加密算法的消息认证方法。

说明

仅支持在智能穿戴设备（Wearable）使用。

## 开发步骤

**生成密钥**

1. 获取生成密钥算法参数配置。
2. 调用[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)生成密钥，支持的规格是128比特长度的密钥。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md#支持的算法)的规格介绍，导入已有的密钥。

**执行CMAC**

1. 获取CMAC算法参数配置。
2. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
3. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，获取MAC数据。

```
1. /*
2. * 以下以CMAC密钥的Promise操作使用为例。
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';
5. import { BusinessError } from "@kit.BasicServicesKit";
6. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

8. let keyAlias = 'test_cmac';
9. let handle: number;
10. let plainText = '123456';
11. let IV = cryptoFramework.createRandom().generateRandomSync(8).data;
12. let macData: Uint8Array;

14. function StringToUint8Array(str: String) {
15. let arr: number[] = new Array();
16. for (let i = 0, j = str.length; i < j; ++i) {
17. arr.push(str.charCodeAt(i));
18. }
19. return new Uint8Array(arr);
20. }

22. function Uint8ArrayToString(fileData: Uint8Array) {
23. let dataString = '';
24. for (let i = 0; i < fileData.length; i++) {
25. dataString += String.fromCharCode(fileData[i]);
26. }
27. return dataString;
28. }

30. function GenerateKeyProperties() {
31. const properties: Array<huks.HuksParam> = [{
32. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
33. value: huks.HuksKeyAlg.HUKS_ALG_3DES
34. }, {
35. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
36. value: huks.HuksKeySize.HUKS_3DES_KEY_SIZE_128
37. }, {
38. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
39. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_MAC
40. }];
41. return properties;
42. }

44. function GetCmacProperties() {
45. const properties: Array<huks.HuksParam> = [{
46. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
47. value: huks.HuksKeyAlg.HUKS_ALG_CMAC
48. }, {
49. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
50. value: huks.HuksKeySize.HUKS_3DES_KEY_SIZE_128
51. }, {
52. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
53. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_MAC
54. }, {
55. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
56. value: huks.HuksCipherMode.HUKS_MODE_CBC
57. }, {
58. tag: huks.HuksTag.HUKS_TAG_PADDING,
59. value: huks.HuksKeyPadding.HUKS_PADDING_ISO_IEC_9797_1
60. }, {
61. tag: huks.HuksTag.HUKS_TAG_IV,
62. value: IV
63. }];
64. return properties;
65. }

67. async function GenerateCmacKey() {
68. /*
69. * 1.1 获取生成密钥算法参数配置
70. */
71. let genProperties = GenerateKeyProperties();
72. let options: huks.HuksOptions = {
73. properties: genProperties
74. }
75. /*
76. * 1.2 调用generateKeyItem
77. */
78. await huks.generateKeyItem(keyAlias, options)
79. .then(() => {
80. console.info(`promise: generate cmac key success`);
81. }).catch((error: BusinessError) => {
82. console.error(`promise: generate cmac key failed, errCode : ${error.code}, errMsg : ${error.message}`);
83. })
84. }

86. async function CmacData() {
87. /*
88. * 2.1 获取CMAC算法参数配置
89. */
90. let cmacProperties = GetCmacProperties();
91. let options: huks.HuksOptions = {
92. properties: cmacProperties,
93. inData: StringToUint8Array(plainText)
94. }
95. /*
96. * 2.2 调用initSession获取handle
97. */
98. await huks.initSession(keyAlias, options)
99. .then((data) => {
100. handle = data.handle;
101. }).catch((error: BusinessError) => {
102. console.error(`promise: init EncryptData failed, errCode : ${error.code}, errMsg : ${error.message}`);
103. })
104. /*
105. * 2.3 调用finishSession获取CMAC的结果
106. */
107. await huks.finishSession(handle, options)
108. .then((data) => {
109. macData = data.outData as Uint8Array;
110. console.info(`promise: cmac data success, data is ${Uint8ArrayToString(macData)}`);
111. }).catch((error: BusinessError) => {
112. console.error(`promise: cmac data failed, errCode : ${error.code}, errMsg : ${error.message}`);
113. })
114. }

116. async function testCMAC() {
117. await GenerateCmacKey();
118. await CmacData();
119. }
```
