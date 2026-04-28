---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-list-aliases-arkts
title: 查询密钥别名集(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 其他操作 > 查询密钥别名集 > 查询密钥别名集(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a3a811e8231ac2ec7c43fa2be8d51e42dfb689f7a11ffb12e4d8d6a847e5c9b9
---

HUKS提供了接口供应用查询密钥别名集。

说明

轻量级智能穿戴不支持查询密钥别名集功能。

从API 23开始支持[群组密钥](huks-group-key-overview.md)特性。

## 开发步骤

1. 初始化密钥属性集，用于查询指定密钥别名集TAG。TAG仅支持[HUKS\_TAG\_AUTH\_STORAGE\_LEVEL](../harmonyos-references/js-apis-huks.md#hukstag)。
2. 调用接口[listAliases](../harmonyos-references/js-apis-huks.md#hukslistaliases12)，查询密钥别名集。

```
1. /*
2. * 以下查询密钥别名集Promise操作使用为例
3. */
4. import { huks } from '@kit.UniversalKeystoreKit'

6. async function testListAliases() {
7. /* 1.初始化密钥属性集 */
8. let queryProperties: Array<huks.HuksParam> = [
9. {
10. tag: huks.HuksTag.HUKS_TAG_AUTH_STORAGE_LEVEL,
11. value: huks.HuksAuthStorageLevel.HUKS_AUTH_STORAGE_LEVEL_DE
12. }
13. ];
14. let queryOptions: huks.HuksOptions = {
15. properties: queryProperties
16. };

18. try {
19. /* 2.查询密钥别名集 */
20. let result: huks.HuksListAliasesReturnResult = await huks.listAliases(queryOptions);
21. console.info(`promise: listAliases success`);
22. } catch (error) {
23. console.error(`promise: listAliases fail`);
24. throw (error as Error);
25. }
26. }
```

[QueryKeyAliasSet.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/OtherOperations/QueryKeyAliasSet/entry/src/main/ets/pages/QueryKeyAliasSet.ets#L16-L43)
