---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-arkts
title: 生成密钥(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥生成/导入 > 密钥生成 > 生成密钥(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:31+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:16d2e1049ce0b34887249af1eecb63dc303088900a16beb1258d7e640298f2c1
---

以DH算法为例，生成随机密钥。具体的场景介绍及支持的算法规格，请参考[密钥生成支持的算法](huks-key-generation-overview.md#支持的算法)。

**注意** 

密钥别名中禁止包含个人数据等敏感信息。

## 开发步骤

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集。

   * 通过[HuksParam](../harmonyos-references/js-apis-huks.md#huksparam)封装密钥属性，搭配Array组成密钥属性集，并赋值给[HuksOptions](../harmonyos-references/js-apis-huks.md#huksoptions)中的properties字段。
   * 密钥属性集中必须包含[HuksKeyAlg](../harmonyos-references/js-apis-huks.md#hukskeyalg)、[HuksKeySize](../harmonyos-references/js-apis-huks.md#hukskeysize)、[HuksKeyPurpose](../harmonyos-references/js-apis-huks.md#hukskeypurpose)属性，即必传TAG：HUKS\_TAG\_ALGORITHM、HUKS\_TAG\_PURPOSE、HUKS\_TAG\_KEY\_SIZE。

   **注意** 

   一个密钥只能有一类PURPOSE，并且生成密钥时指定的用途要与使用时的方式一致，否则会导致异常。
3. 调用[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)，传入密钥别名和密钥属性集，生成密钥。

**说明** 

如果业务再次使用相同别名调用HUKS生成密钥，HUKS将生成新密钥并直接覆盖历史的密钥文件。

```typescript
import { huks } from '@kit.UniversalKeystoreKit';

/* 1.确定密钥别名 */
let keyAlias = 'dh_key';
/* 2.初始化密钥属性集 */
let properties1: huks.HuksParam[] = [
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

let huksOptions: huks.HuksOptions = {
  properties: properties1,
  inData: new Uint8Array([])
}

/* 3.生成密钥 */
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

async function publicGenKeyFunc(keyAlias: string, huksOptions: huks.HuksOptions): Promise<string> {
  console.info(`enter promise generateKeyItem`);
  try {
    await generateKeyItem(keyAlias, huksOptions)
      .then((data) => {
        console.info(`promise: generateKeyItem success, data = ${JSON.stringify(data)}`);
      })
      .catch((error: Error) => {
        console.error(`promise: generateKeyItem failed, ${JSON.stringify(error)}`);
      });
    return 'Success';
  } catch (error) {
    console.error(`promise: generateKeyItem input arg invalid, ` + JSON.stringify(error));
    return 'Failed';
  }
}

async function testGenKey(): Promise<string> {
  let ret = await publicGenKeyFunc(keyAlias, huksOptions);
  return ret;
}
```
