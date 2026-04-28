---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-arkts
title: 生成密钥(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥生成/导入 > 密钥生成 > 生成密钥(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0a715ad6e06e067da31db90b8598e4884ab0ec4ba40669156905b5361a42d92e
---

以DH算法为例，生成随机密钥。具体的场景介绍及支持的算法规格，请参考[密钥生成支持的算法](huks-key-generation-overview.md#支持的算法)。

注意

密钥别名中禁止包含个人数据等敏感信息。

## 开发步骤

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集。

   * 通过[HuksParam](../harmonyos-references/js-apis-huks.md#huksparam)封装密钥属性，搭配Array组成密钥属性集，并赋值给[HuksOptions](../harmonyos-references/js-apis-huks.md#huksoptions)中的properties字段。
   * 密钥属性集中必须包含[HuksKeyAlg](../harmonyos-references/js-apis-huks.md#hukskeyalg)、[HuksKeySize](../harmonyos-references/js-apis-huks.md#hukskeysize)、[HuksKeyPurpose](../harmonyos-references/js-apis-huks.md#hukskeypurpose)属性，即必传TAG：HUKS\_TAG\_ALGORITHM、HUKS\_TAG\_PURPOSE、HUKS\_TAG\_KEY\_SIZE。

   注意

   一个密钥只能有一类PURPOSE，并且生成密钥时指定的用途要与使用时的方式一致，否则会导致异常。
3. 调用[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)，传入密钥别名和密钥属性集，生成密钥。

说明

如果业务再次使用相同别名调用HUKS生成密钥，HUKS将生成新密钥并直接覆盖历史的密钥文件。

```
1. import { huks } from '@kit.UniversalKeystoreKit';

3. /* 1.确定密钥别名 */
4. let keyAlias = 'dh_key';
5. /* 2.初始化密钥属性集 */
6. let properties1: huks.HuksParam[] = [
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

21. let huksOptions: huks.HuksOptions = {
22. properties: properties1,
23. inData: new Uint8Array([])
24. }

26. /* 3.生成密钥 */
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

43. async function publicGenKeyFunc(keyAlias: string, huksOptions: huks.HuksOptions): Promise<string> {
44. console.info(`enter promise generateKeyItem`);
45. try {
46. await generateKeyItem(keyAlias, huksOptions)
47. .then((data) => {
48. console.info(`promise: generateKeyItem success, data = ${JSON.stringify(data)}`);
49. })
50. .catch((error: Error) => {
51. console.error(`promise: generateKeyItem failed, ${JSON.stringify(error)}`);
52. });
53. return 'Success';
54. } catch (error) {
55. console.error(`promise: generateKeyItem input arg invalid, ` + JSON.stringify(error));
56. return 'Failed';
57. }
58. }

60. async function testGenKey(): Promise<string> {
61. let ret = await publicGenKeyFunc(keyAlias, huksOptions);
62. return ret;
63. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/GenerateKey/entry/src/main/ets/pages/Index.ets#L18-L84)
