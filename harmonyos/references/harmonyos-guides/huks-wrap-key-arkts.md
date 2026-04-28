---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-wrap-key-arkts
title: 加密导出导入密钥(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 其他操作 > 加密导出导入密钥 > 加密导出导入密钥(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7c147bf752684b9f55b7e68937ced9cefdbf9441d88c6000070918736bc82193
---

从API 20开始，支持加密导出导入密钥。

当前指导提供以下加密导出导入密钥示例：

* [加密导出导入密钥(ArkTS)](huks-wrap-key-arkts.md#加密导出导入密钥arkts)
  + [开发步骤](huks-wrap-key-arkts.md#开发步骤)
  + [开发案例](huks-wrap-key-arkts.md#开发案例)
    - [加密导出导入普通密钥](huks-wrap-key-arkts.md#加密导出导入普通密钥)
    - [普通密钥导入为群组密钥](huks-wrap-key-arkts.md#普通密钥导入为群组密钥)

## 开发步骤

1. 初始化生成密钥属性集，需要设置[HUKS\_TAG\_IS\_ALLOWED\_WRAP](../harmonyos-references/js-apis-huks.md#hukstag)，指定密钥允许导出。
2. 调用[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)生成密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。
3. 调用[wrapKeyItem](../harmonyos-references/js-apis-huks.md#hukswrapkeyitem20)加密导出密钥。
4. 调用[unwrapKeyItem](../harmonyos-references/js-apis-huks.md#huksunwrapkeyitem20)加密导入密钥。如果是从普通密钥导入为群组密钥，需要传入TUI PIN类型的AuthToken，认证TUI PIN并获取AuthToken请参考[数字盾服务](../harmonyos-references/devicesecurity-trusted-auth-api.md#section6763105845111)

## 开发案例

### 加密导出导入普通密钥

```
1. import { huks } from '@kit.UniversalKeystoreKit';

3. let keyAlias = "testWrapKey";
4. let properties: Array<huks.HuksParam> = [
5. {
6. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
7. value: huks.HuksKeyAlg.HUKS_ALG_AES
8. },
9. {
10. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
11. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
12. },
13. {
14. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
15. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
16. },
17. {
18. tag: huks.HuksTag.HUKS_TAG_PADDING,
19. value: huks.HuksKeyPadding.HUKS_PADDING_NONE
20. },
21. {
22. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
23. value: huks.HuksCipherMode.HUKS_MODE_GCM
24. },
25. /* 生成密钥时指定允许加密导出 */
26. {
27. tag: huks.HuksTag.HUKS_TAG_IS_ALLOWED_WRAP,
28. value: true
29. }
30. ];

32. let options: huks.HuksOptions = {
33. properties: properties,
34. };

36. let wrapKeyProperties: Array<huks.HuksParam> = [
37. {
38. tag: huks.HuksTag.HUKS_TAG_KEY_WRAP_TYPE,
39. value: huks.HuksKeyWrapType.HUKS_KEY_WRAP_TYPE_HUK_BASED
40. }
41. ];

43. let wrapKeyOptions: huks.HuksOptions = {
44. properties: wrapKeyProperties,
45. };

47. let wrappedKey: Uint8Array;

49. async function testGenerateKey() {
50. await huks.generateKeyItem(keyAlias, options)
51. .then((data) => {
52. console.info(`promise: generateKeyItem success`);
53. })
54. .catch((error: Error) => {
55. console.error(`promise: generateKeyItem failed`);
56. });
57. }

59. async function testWrapKey(){
60. await testGenerateKey();

62. await huks.wrapKeyItem(keyAlias, wrapKeyOptions)
63. .then((data) => {
64. wrappedKey = data.outData as Uint8Array;
65. console.info(`promise: wrapKeyItem success, data = ${JSON.stringify(data)}`);
66. })
67. .catch((error: Error) => {
68. console.error(`promise: wrapKeyItem failed`);
69. });

71. await huks.unwrapKeyItem(keyAlias, wrapKeyOptions, wrappedKey)
72. .then((data) => {
73. console.info(`promise: unwrapKeyItem success`);
74. })
75. .catch((error: Error) => {
76. console.error(`promise: unwrapKeyItem failed`);
77. });
78. }
```

### 普通密钥导入为群组密钥

从API 23开始，支持从普通密钥导入为群组密钥。

```
1. import { huks } from '@kit.UniversalKeystoreKit';
2. import { trustedAuthentication } from '@kit.DeviceSecurityKit';

4. let keyAlias = "testWrapKey";
5. let properties: Array<huks.HuksParam> = [
6. {
7. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
8. value: huks.HuksKeyAlg.HUKS_ALG_AES
9. },
10. {
11. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
12. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
13. },
14. {
15. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
16. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
17. },
18. {
19. tag: huks.HuksTag.HUKS_TAG_PADDING,
20. value: huks.HuksKeyPadding.HUKS_PADDING_NONE
21. },
22. {
23. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
24. value: huks.HuksCipherMode.HUKS_MODE_GCM
25. },
26. /* 生成密钥时指定允许加密导出 */
27. {
28. tag: huks.HuksTag.HUKS_TAG_IS_ALLOWED_WRAP,
29. value: true
30. }
31. ];

33. let options: huks.HuksOptions = {
34. properties: properties,
35. };

37. let wrapKeyProperties: Array<huks.HuksParam> = [
38. {
39. tag: huks.HuksTag.HUKS_TAG_KEY_WRAP_TYPE,
40. value: huks.HuksKeyWrapType.HUKS_KEY_WRAP_TYPE_HUK_BASED
41. }
42. ];

44. let wrapKeyOptions: huks.HuksOptions = {
45. properties: wrapKeyProperties,
46. };

48. let wrappedKey: Uint8Array;

50. async function testGenerateKey() {
51. await huks.generateKeyItem(keyAlias, options)
52. .then((data) => {
53. console.info(`promise: generateKeyItem success`);
54. })
55. .catch((error: Error) => {
56. console.error(`promise: generateKeyItem failed`);
57. });
58. }

60. async function testWrapKey(){
61. await testGenerateKey();

63. await huks.wrapKeyItem(keyAlias, wrapKeyOptions)
64. .then((data) => {
65. wrappedKey = data.outData as Uint8Array;
66. console.info(`promise: wrapKeyItem success, data = ${JSON.stringify(data)}`);
67. })
68. .catch((error: Error) => {
69. console.error(`promise: wrapKeyItem failed`);
70. });

72. challenge = new Uint8Array(32);
73. let label: trustedAuthentication.TUILable;
74. let authID: bigint;
75. /* 认证TUI PIN之前需要先创建数字盾，请参考数字盾服务，authID和label仅做示例 */
76. let authToken = await trustedAuthentication.trustedAuthentication(challenge, authID, label);
77. wrapKeyOptions.wrapKeyProperties.push({
78. tag: huks.HuksTag.HUKS_TAG_AUTH_TOKEN,
79. value: authToken.authToken
80. })

82. await huks.unwrapKeyItem(keyAlias, wrapKeyOptions, wrappedKey)
83. .then((data) => {
84. console.info(`promise: unwrapKeyItem success`);
85. })
86. .catch((error: Error) => {
87. console.error(`promise: unwrapKeyItem failed`);
88. });
89. }
```
