---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-import-key-in-plaintext-arkts
title: 明文导入密钥(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥生成/导入 > 密钥导入 > 明文导入密钥(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8a2dd538bd82484f5655b56bf0050eeec2b0b776d05969bcbdf0308e12a41972
---

分别以导入AES256、RSA2048和X25519密钥为例。具体的场景介绍及支持的算法规格，请参考[密钥导入支持的算法](huks-key-import-overview.md#支持的算法)。

## 开发步骤

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 封装密钥属性集和密钥材料。

   * 密钥属性集同样与密钥生成中指定的密钥属性一致，须包含[HuksKeyAlg](../harmonyos-references/js-apis-huks.md#hukskeyalg)、[HuksKeySize](../harmonyos-references/js-apis-huks.md#hukskeysize)、[HuksKeyPurpose](../harmonyos-references/js-apis-huks.md#hukskeypurpose)属性。
   * 密钥材料须符合[HUKS密钥材料格式](huks-concepts.md#密钥材料格式)，并以Uint8Array形式赋值给[HuksOptions](../harmonyos-references/js-apis-huks.md#huksoptions)的inData字段。
3. 调用[huks.importKeyItem](../harmonyos-references/js-apis-huks.md#huksimportkeyitem9)，传入密钥别名和密钥属性集，即可导入密钥。

   HuksParam和HuksOptions的含义参考：[HuksParam](../harmonyos-references/js-apis-huks.md#huksparam) 和 [HuksOptions](../harmonyos-references/js-apis-huks.md#huksoptions)

### 导入AES256密钥

```
1. /* 以下以导入AES256密钥的Callback操作使用为例。 */
2. import { huks } from '@kit.UniversalKeystoreKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. /* 密钥材料。 */
6. let plainTextSize32 = new Uint8Array([
7. 0xfb, 0x8b, 0x9f, 0x12, 0xa0, 0x83, 0x19, 0xbe, 0x6a, 0x6f, 0x63, 0x2a, 0x7c, 0x86, 0xba, 0xca,
8. 0x64, 0x0b, 0x88, 0x96, 0xe2, 0xfa, 0x77, 0xbc, 0x71, 0xe3, 0x0f, 0x0f, 0x9e, 0x3c, 0xe5, 0xf9
9. ]);
10. /* 1.确定密钥别名。 */
11. let keyAlias = 'AES256Alias_sample';

13. /* 2.封装密钥属性集和密钥材料。 */
14. let properties: huks.HuksParam[] = [{
15. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
16. value: huks.HuksKeyAlg.HUKS_ALG_AES
17. }, {
18. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
19. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
20. }, {
21. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
22. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
23. },
24. ]
25. let options: huks.HuksOptions = {
26. properties: properties,
27. inData: plainTextSize32
28. };

30. /* 3.明文导入密钥。 */
31. async function importKeyItem(keyAlias: string, huksOptions: huks.HuksOptions): Promise<boolean> {
32. console.info('promise: enter importKeyItem');
33. let ret: boolean = false;
34. try {
35. await huks.importKeyItem(keyAlias, huksOptions)
36. .then(() => {
37. console.info(`promise: importKeyItem success`);
38. ret = true;
39. }).catch((error: BusinessError) => {
40. console.error(`promise: importKeyItem failed errCode : ${error.code}, errMsg : ${error.message}`);
41. })
42. } catch (error) {
43. console.error(`promise: importKeyItem input arg invalid`);
44. }
45. return ret;
46. }

48. async function testImport() {
49. let retImp = await importKeyItem(keyAlias, options);
50. if (retImp == false) {
51. console.error(`testImport failed`);
52. return;
53. }
54. console.info(`testImport success`);
55. }
```

[AES256.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/ImportKeyPlainText/entry/src/main/ets/pages/AES256.ets#L16-L74)

### 导入RSA2048密钥对

```
1. /* 以下以导入RSA2048密钥的Callback操作使用为例。 */
2. import { huks } from '@kit.UniversalKeystoreKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let rsa2048KeyPairMaterial = new Uint8Array([
6. 0x01, 0x00, 0x00, 0x00, // 密钥算法(小端表示)huks.HuksKeyAlg.HUKS_ALG_RSA = 1。
7. 0x00, 0x08, 0x00, 0x00, // 密钥大小（比特）：2048。
8. 0x00, 0x01, 0x00, 0x00, // 模数n长度（字节）：256。
9. 0x03, 0x00, 0x00, 0x00, // 公钥指数e长度（字节）：3。
10. 0x00, 0x01, 0x00, 0x00, // 私钥指数d长度（字节）：256。
11. // 模数n。
12. 0xc5, 0x35, 0x62, 0x48, 0xc4, 0x92, 0x87, 0x73, 0x0d, 0x42, 0x96, 0xfc, 0x7b, 0x11, 0x05, 0x06,
13. 0x0f, 0x8d, 0x66, 0xc1, 0x0e, 0xad, 0x37, 0x44, 0x92, 0x95, 0x2f, 0x6a, 0x55, 0xba, 0xec, 0x1d,
14. 0x54, 0x62, 0x0a, 0x4b, 0xd3, 0xc7, 0x05, 0xe4, 0x07, 0x40, 0xd9, 0xb7, 0xc2, 0x12, 0xcb, 0x9a,
15. 0x90, 0xad, 0xe3, 0x24, 0xe8, 0x5e, 0xa6, 0xf8, 0xd0, 0x6e, 0xbc, 0xd1, 0x69, 0x7f, 0x6b, 0xe4,
16. 0x2b, 0x4e, 0x1a, 0x65, 0xbb, 0x73, 0x88, 0x6b, 0x7c, 0xaf, 0x7e, 0xd0, 0x47, 0x26, 0xeb, 0xa5,
17. 0xbe, 0xd6, 0xe8, 0xee, 0x9c, 0xa5, 0x66, 0xa5, 0xc9, 0xd3, 0x25, 0x13, 0xc4, 0x0e, 0x6c, 0xab,
18. 0x50, 0xb6, 0x50, 0xc9, 0xce, 0x8f, 0x0a, 0x0b, 0xc6, 0x28, 0x69, 0xe9, 0x83, 0x69, 0xde, 0x42,
19. 0x56, 0x79, 0x7f, 0xde, 0x86, 0x24, 0xca, 0xfc, 0xaa, 0xc0, 0xf3, 0xf3, 0x7f, 0x92, 0x8e, 0x8a,
20. 0x12, 0x52, 0xfe, 0x50, 0xb1, 0x5e, 0x8c, 0x01, 0xce, 0xfc, 0x7e, 0xf2, 0x4f, 0x5f, 0x03, 0xfe,
21. 0xa7, 0xcd, 0xa1, 0xfc, 0x94, 0x52, 0x00, 0x8b, 0x9b, 0x7f, 0x09, 0xab, 0xa8, 0xa4, 0xf5, 0xb4,
22. 0xa5, 0xaa, 0xfc, 0x72, 0xeb, 0x17, 0x40, 0xa9, 0xee, 0xbe, 0x8f, 0xc2, 0xd1, 0x80, 0xc2, 0x0d,
23. 0x44, 0xa9, 0x59, 0x44, 0x59, 0x81, 0x3b, 0x5d, 0x4a, 0xde, 0xfb, 0xae, 0x24, 0xfc, 0xa3, 0xd9,
24. 0xbc, 0x57, 0x55, 0xc2, 0x26, 0xbc, 0x19, 0xa7, 0x9a, 0xc5, 0x59, 0xa3, 0xee, 0x5a, 0xef, 0x41,
25. 0x80, 0x7d, 0xf8, 0x5e, 0xc1, 0x1d, 0x32, 0x38, 0x41, 0x5b, 0xb6, 0x92, 0xb8, 0xb7, 0x03, 0x0d,
26. 0x3e, 0x59, 0x0f, 0x1c, 0xb3, 0xe1, 0x2a, 0x95, 0x1a, 0x3b, 0x50, 0x4f, 0xc4, 0x1d, 0xcf, 0x73,
27. 0x7c, 0x14, 0xca, 0xe3, 0x0b, 0xa7, 0xc7, 0x1a, 0x41, 0x4a, 0xee, 0xbe, 0x1f, 0x43, 0xdd, 0xf9,
28. // 公钥指数e。
29. 0x01, 0x00, 0x01,
30. // 私钥指数d。
31. 0x88, 0x4b, 0x82, 0xe7, 0xe3, 0xe3, 0x99, 0x75, 0x6c, 0x9e, 0xaf, 0x17, 0x44, 0x3e, 0xd9, 0x07,
32. 0xfd, 0x4b, 0xae, 0xce, 0x92, 0xc4, 0x28, 0x44, 0x5e, 0x42, 0x79, 0x08, 0xb6, 0xc3, 0x7f, 0x58,
33. 0x2d, 0xef, 0xac, 0x4a, 0x07, 0xcd, 0xaf, 0x46, 0x8f, 0xb4, 0xc4, 0x43, 0xf9, 0xff, 0x5f, 0x74,
34. 0x2d, 0xb5, 0xe0, 0x1c, 0xab, 0xf4, 0x6e, 0xd5, 0xdb, 0xc8, 0x0c, 0xfb, 0x76, 0x3c, 0x38, 0x66,
35. 0xf3, 0x7f, 0x01, 0x43, 0x7a, 0x30, 0x39, 0x02, 0x80, 0xa4, 0x11, 0xb3, 0x04, 0xd9, 0xe3, 0x57,
36. 0x23, 0xf4, 0x07, 0xfc, 0x91, 0x8a, 0xc6, 0xcc, 0xa2, 0x16, 0x29, 0xb3, 0xe5, 0x76, 0x4a, 0xa8,
37. 0x84, 0x19, 0xdc, 0xef, 0xfc, 0xb0, 0x63, 0x33, 0x0b, 0xfa, 0xf6, 0x68, 0x0b, 0x08, 0xea, 0x31,
38. 0x52, 0xee, 0x99, 0xef, 0x43, 0x2a, 0xbe, 0x97, 0xad, 0xb3, 0xb9, 0x66, 0x7a, 0xae, 0xe1, 0x8f,
39. 0x57, 0x86, 0xe5, 0xfe, 0x14, 0x3c, 0x81, 0xd0, 0x64, 0xf8, 0x86, 0x1a, 0x0b, 0x40, 0x58, 0xc9,
40. 0x33, 0x49, 0xb8, 0x99, 0xc6, 0x2e, 0x94, 0x70, 0xee, 0x09, 0x88, 0xe1, 0x5c, 0x4e, 0x6c, 0x22,
41. 0x72, 0xa7, 0x2a, 0x21, 0xdd, 0xd7, 0x1d, 0xfc, 0x63, 0x15, 0x0b, 0xde, 0x06, 0x9c, 0xf3, 0x28,
42. 0xf3, 0xac, 0x4a, 0xa8, 0xb5, 0x50, 0xca, 0x9b, 0xcc, 0x0a, 0x04, 0xfe, 0x3f, 0x98, 0x68, 0x81,
43. 0xac, 0x24, 0x53, 0xea, 0x1f, 0x1c, 0x6e, 0x5e, 0xca, 0xe8, 0x31, 0x0d, 0x08, 0x12, 0xf3, 0x26,
44. 0xf8, 0x5e, 0xeb, 0x10, 0x27, 0xae, 0xaa, 0xc3, 0xad, 0x6c, 0xc1, 0x89, 0xdb, 0x7d, 0x5a, 0x12,
45. 0x55, 0xad, 0x11, 0x19, 0xa1, 0xa9, 0x8f, 0x0b, 0x6d, 0x78, 0x8d, 0x1c, 0xdf, 0xe5, 0x63, 0x82,
46. 0x0b, 0x7d, 0x23, 0x04, 0xb4, 0x75, 0x8c, 0xed, 0x77, 0xfc, 0x1a, 0x85, 0x29, 0x11, 0xe0, 0x61,
47. ]);

49. /* 1.确定密钥别名。 */
50. let keyAlias = 'RSA_sample';
51. /* 2.封装密钥属性集和密钥材料。 */
52. let properties: huks.HuksParam[] = [{
53. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
54. value: huks.HuksKeyAlg.HUKS_ALG_RSA
55. }, {
56. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
57. value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
58. }, {
59. // 此tag表示密钥导入后的用途，导入后将不可更改。
60. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
61. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
62. }, {
63. // 此tag表示需导入的密钥类型。
64. tag: huks.HuksTag.HUKS_TAG_IMPORT_KEY_TYPE,
65. // 此value表示导入密钥对，若改为HUKS_KEY_TYPE_PUBLIC_KEY时表示仅导入公钥。
66. value: huks.HuksImportKeyType.HUKS_KEY_TYPE_KEY_PAIR
67. }
68. ]
69. let options: huks.HuksOptions = {
70. properties: properties,
71. inData: rsa2048KeyPairMaterial
72. };

74. /* 3.明文导入密钥。 */
75. async function importKeyItem(keyAlias: string, huksOptions: huks.HuksOptions): Promise<boolean> {
76. console.info('promise: enter importKeyItem');
77. let ret: boolean = false;
78. try {
79. await huks.importKeyItem(keyAlias, huksOptions)
80. .then(() => {
81. console.info(`promise: importKeyItem success`);
82. ret = true;
83. }).catch((error: BusinessError) => {
84. console.error(`promise: importKeyItem failed errCode : ${error.code}, errMsg : ${error.message}`);
85. })
86. } catch (error) {
87. console.error(`promise: importKeyItem input arg invalid`);
88. }
89. return ret;
90. }

92. async function testImport() {
93. let retImp = await importKeyItem(keyAlias, options);
94. if (retImp == false) {
95. console.error(`testImport failed`);
96. return;
97. }
98. console.info(`testImport success`);
99. }
```

[RSA2048.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/ImportKeyPlainText/entry/src/main/ets/pages/RSA2048.ets#L16-L117)

### 导入X25519密钥公钥

```
1. /* 以下以导入X25519密钥的Callback操作使用为例。 */
2. import { huks } from '@kit.UniversalKeystoreKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // X25519的公钥数据。X25519密钥对中的私钥和公钥都是32字节（256位），关于算法原理请自行参考相关密码学资料。
6. let x25519KeyPubMaterial = new Uint8Array([
7. 0x30, 0x2A, 0x30, 0x05, 0x06, 0x03, 0x2B, 0x65, 0x6E, 0x03, 0x21, 0x00, 0xD2, 0x36, 0x9E, 0xCF,
8. 0xF0, 0x61, 0x5B, 0x73, 0xCE, 0x4F, 0xF0, 0x40, 0x2B, 0x89, 0x18, 0x3E, 0x06, 0x33, 0x60, 0xC6
9. ]);

11. /* 1.确定密钥别名。 */
12. let keyAlias = 'X25519_Pub_import_sample';
13. /* 2.封装密钥属性集和密钥材料。 */
14. let properties: huks.HuksParam[] = [{
15. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
16. value: huks.HuksKeyAlg.HUKS_ALG_X25519
17. }, {
18. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
19. value: huks.HuksKeySize.HUKS_CURVE25519_KEY_SIZE_256
20. }, {
21. // 此tag表示密钥导入后的用途，导入后将不可更改。
22. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
23. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
24. }, {
25. // 此tag表示需导入的密钥类型。
26. tag: huks.HuksTag.HUKS_TAG_IMPORT_KEY_TYPE,
27. // 此value表示导入密钥的公钥，若改为HUKS_KEY_TYPE_KEY_PAIR时表示导入密钥对。
28. value: huks.HuksImportKeyType.HUKS_KEY_TYPE_PUBLIC_KEY
29. },
30. ]
31. let options: huks.HuksOptions = {
32. properties: properties,
33. inData: x25519KeyPubMaterial
34. };

36. /* 3.明文导入密钥。 */
37. async function importKeyItem(keyAlias: string, huksOptions: huks.HuksOptions): Promise<boolean> {
38. console.info('promise: enter importKeyItem');
39. let ret: boolean = false;
40. try {
41. await huks.importKeyItem(keyAlias, huksOptions)
42. .then(() => {
43. console.info(`promise: importKeyItem success`);
44. ret = true;
45. }).catch((error: BusinessError) => {
46. console.error(`promise: importKeyItem failed errCode : ${error.code}, errMsg : ${error.message}`);
47. })
48. } catch (error) {
49. console.error(`promise: importKeyItem input arg invalid`);
50. }
51. return ret;
52. }

54. async function testImport() {
55. let retImp = await importKeyItem(keyAlias, options);
56. if (retImp == false) {
57. console.error(`testImport failed`);
58. return;
59. }
60. console.info(`testImport success`);
61. }
```

[X25519.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/ImportKeyPlainText/entry/src/main/ets/pages/X25519.ets#L15-L78)

## 调测验证

调用[huks.isKeyItemExist](../harmonyos-references/js-apis-huks.md#huksiskeyitemexist9)验证密钥是否存在，如密钥存在即表示密钥导入成功。

```
1. import { huks } from '@kit.UniversalKeystoreKit';
2. import { BusinessError } from "@kit.BasicServicesKit";

4. let keyAlias = 'AES256Alias_sample';
5. let keyProperties: Array<huks.HuksParam> = [{
6. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
7. value: huks.HuksKeyAlg.HUKS_ALG_AES
8. }
9. ]
10. let huksOptions: huks.HuksOptions = {
11. properties: keyProperties, // 非空填充。
12. inData: new Uint8Array(new Array()) // 非空填充。
13. }

15. async function isKeyItemExist(keyAlias: string, options: huks.HuksOptions): Promise<boolean> {
16. console.info(`promise: enter isKeyItemExist success`);
17. let ret: boolean = false;
18. try {
19. await huks.isKeyItemExist(keyAlias, options)
20. .then((data) => {
21. console.info(`promise: isKeyItemExist success, data = ${data}`);
22. ret = true;
23. }).catch((error: BusinessError) => {
24. console.error(`promise: isKeyItemExist success, errCode : ${error.code}, errMsg : ${error.message}`);
25. })
26. } catch (error) {
27. console.error(`promise: isKeyItemExist input arg invalid`);
28. }
29. return ret;
30. }

32. async function testImportKeyExist() {
33. let retExist = await isKeyItemExist(keyAlias, huksOptions);
34. if (retExist == false) {
35. console.error(`testImportKeyExist failed`);
36. return;
37. }
38. console.info(`testImportKeyExist success`);
39. }
```
