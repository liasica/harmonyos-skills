---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-check-key-arkts
title: 查询密钥是否存在(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 其他操作 > 查询密钥是否存在 > 查询密钥是否存在(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bef1f939caa3959c831292a4ee6eb875ac545ec723dbb4cb9f1d475affe49458
---

HUKS提供了接口供应用查询指定密钥是否存在。

从API 23开始支持[群组密钥](huks-group-key-overview.md)特性。

## 开发步骤

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集。用于查询时指定密钥的属性，查询单个密钥或者非群组密钥，可传空。
3. 调用接口[hasKeyItem](../harmonyos-references/js-apis-huks.md#hukshaskeyitem11)，查询密钥是否存在。

```
1. import { huks } from '@kit.UniversalKeystoreKit';

3. let keyAlias = 'test_key';
4. let isKeyExist: Boolean;

6. let generateProperties: huks.HuksParam[] = [
7. {
8. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
9. value: huks.HuksKeyAlg.HUKS_ALG_DH
10. },
11. {
12. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
13. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_AGREE
14. },
15. {
16. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
17. value: huks.HuksKeySize.HUKS_DH_KEY_SIZE_2048
18. }
19. ];

21. let generateHuksOptions: huks.HuksOptions = {
22. properties: generateProperties,
23. inData: new Uint8Array([])
24. }

26. /* 1.生成密钥 */
27. function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
28. return new Promise<void>((resolve, reject) => {
29. try {
30. huks.generateKeyItem(keyAlias, huksOptions, (error, data) => {
31. if (error) {
32. reject(error);
33. } else {
34. resolve(data);
35. }
36. });
37. } catch (error) {
38. throw (error as Error);
39. }
40. });
41. }

43. async function generateKey(keyAlias: string, huksOptions: huks.HuksOptions): Promise<void> {
44. console.info(`enter promise generateKeyItem`);
45. await generateKeyItem(keyAlias, huksOptions);
46. console.info(`promise: generateKeyItem success`);
47. }

49. /* 2.检查密钥是否存在 */
50. let huksOptions: huks.HuksOptions = {
51. properties: []
52. }

54. function hasKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
55. return new Promise<boolean>((resolve, reject) => {
56. try {
57. huks.hasKeyItem(keyAlias, huksOptions, (error, data) => {
58. if (error) {
59. reject(error);
60. } else {
61. resolve(data.valueOf());
62. }
63. });
64. } catch (error) {
65. throw (error as Error);
66. }
67. });
68. }

70. async function checkKeyExistence(keyAlias: string, huksOptions: huks.HuksOptions): Promise<boolean> {
71. console.info(`enter promise hasKeyItem`);
72. const exists = await hasKeyItem(keyAlias, huksOptions);
73. console.info(`promise: hasKeyItem success, isKeyExist = ${exists}`);
74. return exists;
75. }

77. async function executeCheckKey(): Promise<string> {
78. try {
79. /* 1.生成密钥 */
80. await generateKey(keyAlias, generateHuksOptions);

82. /* 2.检查密钥是否存在 */
83. isKeyExist = await checkKeyExistence(keyAlias, huksOptions);

85. console.info(`Key check completed, isKeyExist = ${isKeyExist}`);
86. return 'Success';
87. } catch (error) {
88. console.error(`Key check failed: ${JSON.stringify(error)}`);
89. return 'Failed';
90. }
91. }
```

[CheckKeyExists.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/OtherOperations/CheckKeyExists/entry/src/main/ets/pages/CheckKeyExists.ets#L17-L109)
