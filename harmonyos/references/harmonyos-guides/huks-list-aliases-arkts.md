---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-list-aliases-arkts
title: 查询密钥别名集(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 其他操作 > 查询密钥别名集 > 查询密钥别名集(ArkTS)
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:41+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:2051f21b5b1f92ef28fdd83c63a250599ae7584616dcd9b4a1806a118953daa6
---

HUKS提供了接口供应用查询密钥别名集。

**说明** 

轻量级智能穿戴不支持查询密钥别名集功能。

从API 23开始支持[群组密钥](huks-group-key-overview.md)特性。

## 开发步骤

1. 初始化密钥属性集，用于查询指定密钥别名集TAG。TAG仅支持[HUKS\_TAG\_AUTH\_STORAGE\_LEVEL](../harmonyos-references/js-apis-huks.md#hukstag)。
2. 调用接口[listAliases](../harmonyos-references/js-apis-huks.md#hukslistaliases12)，查询密钥别名集。

```typescript
/*
 * 以下查询密钥别名集Promise操作使用为例
 */
import { huks } from '@kit.UniversalKeystoreKit';

async function testListAliases() {
  /* 1.初始化密钥属性集 */
  let queryProperties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_AUTH_STORAGE_LEVEL,
      value: huks.HuksAuthStorageLevel.HUKS_AUTH_STORAGE_LEVEL_DE
    }
  ];
  let queryOptions: huks.HuksOptions = {
    properties: queryProperties
  };

  try {
    /* 2.查询密钥别名集 */
    let result: huks.HuksListAliasesReturnResult = await huks.listAliases(queryOptions);
    console.info(`promise: listAliases success, result = ${JSON.stringify(result)}`);
  } catch (error) {
    console.error(`promise: listAliases fail`);
    throw (error as Error);
  }
}
```
