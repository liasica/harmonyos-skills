---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-delete-key-arkts
title: 密钥删除(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥删除 > 密钥删除(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:03+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0511e0b3a48467c8bb7e83ae76e84b3ddb696da79014a09e5b1f18a42681937a
---

为保证数据安全性，当不需要使用该密钥时，应该删除密钥。

从API 23开始支持[群组密钥](huks-group-key-overview.md)特性。

## 开发步骤

以删除DH密钥为例。

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集。用于删除时指定密钥的属性，删除单个密钥或者非群组密钥，可传空。
3. 调用接口[deleteKeyItem](../harmonyos-references/js-apis-huks.md#huksdeletekeyitem9)，删除密钥。

```typescript
/*
 * 以下以DH密钥的Promise操作使用为例
 */
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = 'test_Key';

let generateProperties: huks.HuksParam[] = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_DH
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_AGREE
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_DH_KEY_SIZE_2048
  }
];

let generateHuksOptions: huks.HuksOptions = {
  properties: generateProperties,
  inData: new Uint8Array([])
}

/* 1.生成密钥 */
function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  return new Promise<void>((resolve, reject) => {
    try {
      huks.generateKeyItem(keyAlias, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throw (error as Error);
    }
  });
}

async function generateKey(keyAlias: string, huksOptions: huks.HuksOptions): Promise<void> {
  console.info(`enter promise generateKeyItem`);
  try {
    await generateKeyItem(keyAlias, huksOptions);
    console.info(`promise: generateKeyItem success`);
  } catch (error) {
    console.error(`promise: generateKeyItem failed, ${JSON.stringify(error)}`);
  }
}

/* 2.删除密钥 */
let deleteHuksOptions: huks.HuksOptions = {
  properties: []
}

function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  return new Promise<void>((resolve, reject) => {
    try {
      huks.deleteKeyItem(keyAlias, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throw (error as Error);
    }
  });
}

async function deleteKey(keyAlias: string, huksOptions: huks.HuksOptions): Promise<void> {
  console.info(`enter promise deleteKeyItem`);
  try {
    await deleteKeyItem(keyAlias, huksOptions);
    console.info(`promise: deleteKeyItem success`);
  } catch (error) {
    console.error(`promise: deleteKeyItem failed, ${JSON.stringify(error)}`);
  }
}

async function executeKeyLifecycle(): Promise<string> {
  try {
    /* 1.生成密钥 */
    console.info('start generateKey...');
    await generateKey(keyAlias, generateHuksOptions);
    console.info('end generateKey...');

    /* 2.删除密钥 */
    console.info('start deleteKey...');
    await deleteKey(keyAlias, deleteHuksOptions);
    console.info('end deleteKey...');

    console.info('Key lifecycle completed successfully');
    return 'Success';
  } catch (error) {
    console.error(`Key lifecycle failed: ${JSON.stringify(error)}`);
    return 'Failed';
  }
}
```
