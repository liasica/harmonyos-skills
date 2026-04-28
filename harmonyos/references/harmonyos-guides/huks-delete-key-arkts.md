---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-delete-key-arkts
title: 密钥删除(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥删除 > 密钥删除(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:527f44c55d89bfaf021ec9b824e4ffe8124a9726e8100ef16e0d3af4e67c2172
---

为保证数据安全性，当不需要使用该密钥时，应该删除密钥。

从API 23开始支持[群组密钥](huks-group-key-overview.md)特性。

## 开发步骤

以删除DH密钥为例。

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集。用于删除时指定密钥的属性，删除单个密钥或者非群组密钥，可传空。
3. 调用接口[deleteKeyItem](../harmonyos-references/js-apis-huks.md#huksdeletekeyitem9)，删除密钥。

```
1. /*
2. * 以下以DH密钥的Promise操作使用为例
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';

6. let keyAlias = 'test_Key';

8. let generateProperties: huks.HuksParam[] = [
9. {
10. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
11. value: huks.HuksKeyAlg.HUKS_ALG_DH
12. },
13. {
14. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
15. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_AGREE
16. },
17. {
18. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
19. value: huks.HuksKeySize.HUKS_DH_KEY_SIZE_2048
20. }
21. ];

23. let generateHuksOptions: huks.HuksOptions = {
24. properties: generateProperties,
25. inData: new Uint8Array([])
26. }

28. /* 1.生成密钥 */
29. function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
30. return new Promise<void>((resolve, reject) => {
31. try {
32. huks.generateKeyItem(keyAlias, huksOptions, (error, data) => {
33. if (error) {
34. reject(error);
35. } else {
36. resolve(data);
37. }
38. });
39. } catch (error) {
40. throw (error as Error);
41. }
42. });
43. }

45. async function generateKey(keyAlias: string, huksOptions: huks.HuksOptions): Promise<void> {
46. console.info(`enter promise generateKeyItem`);
47. try {
48. await generateKeyItem(keyAlias, huksOptions);
49. console.info(`promise: generateKeyItem success`);
50. } catch (error) {
51. console.error(`promise: generateKeyItem failed, ${JSON.stringify(error)}`);
52. }
53. }

55. /* 2.删除密钥 */
56. let deleteHuksOptions: huks.HuksOptions = {
57. properties: []
58. }

60. function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
61. return new Promise<void>((resolve, reject) => {
62. try {
63. huks.deleteKeyItem(keyAlias, huksOptions, (error, data) => {
64. if (error) {
65. reject(error);
66. } else {
67. resolve(data);
68. }
69. });
70. } catch (error) {
71. throw (error as Error);
72. }
73. });
74. }

76. async function deleteKey(keyAlias: string, huksOptions: huks.HuksOptions): Promise<void> {
77. console.info(`enter promise deleteKeyItem`);
78. try {
79. await deleteKeyItem(keyAlias, huksOptions);
80. console.info(`promise: deleteKeyItem success`);
81. } catch (error) {
82. console.error(`promise: deleteKeyItem failed, ${JSON.stringify(error)}`);
83. }
84. }

86. async function executeKeyLifecycle(): Promise<string> {
87. try {
88. /* 1.生成密钥 */
89. console.info('start generateKey...');
90. await generateKey(keyAlias, generateHuksOptions);
91. console.info('end generateKey...');

93. /* 2.删除密钥 */
94. console.info('start deleteKey...');
95. await deleteKey(keyAlias, deleteHuksOptions);
96. console.info('end deleteKey...');

98. console.info('Key lifecycle completed successfully');
99. return 'Success';
100. } catch (error) {
101. console.error(`Key lifecycle failed: ${JSON.stringify(error)}`);
102. return 'Failed';
103. }
104. }
```

[KeyDeletion.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyDeletion/entry/src/main/ets/pages/KeyDeletion.ets#L16-L121)
