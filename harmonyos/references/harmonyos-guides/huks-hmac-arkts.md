---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-hmac-arkts
title: HMAC(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > HMAC > HMAC(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:03+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:278e5313e93e96b57fc0a6525d086702eb05d0ee10f551cb0a3674abe785e679
---

HMAC是密钥相关的哈希运算消息认证码（Hash-based Message Authentication Code）。具体的场景介绍及支持的算法规格，请参考[HMAC介绍及算法规格](huks-hmac-overview.md)。

## 开发步骤

**生成密钥**

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集。
3. 调用[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)生成密钥，HMAC支持的规格请参考[密钥生成支持的算法](huks-key-generation-overview.md#支持的算法)。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md#支持的算法)的规格介绍，导入已有的密钥。

**执行HMAC**

1. 获取密钥别名。
2. 获取待运算的数据。
3. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
4. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，获取哈希后的数据。

```typescript
/*
 * 以下以HMAC密钥的Promise操作使用为例
 */
import { huks } from '@kit.UniversalKeystoreKit';

let hmacKeyAlias = 'test_HMAC';
let handle: number;
let plainText = '123456';
let hashData: Uint8Array;

function stringToUint8Array(str: String) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function uint8ArrayToString(fileData: Uint8Array) {
  let dataString = '';
  for (let i = 0; i < fileData.length; i++) {
    dataString += String.fromCharCode(fileData[i]);
  }
  return dataString;
}

function getHMACProperties() {
  const properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_HMAC
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_MAC
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA384,
  }];
  return properties;
}

/* 1.生成 HMAC 密钥 */
async function generateHMACKey() {
  let options: huks.HuksOptions = {
    properties: getHMACProperties()
  };

  await huks.generateKeyItem(hmacKeyAlias, options)
    .then((data) => {
      console.info(`promise: generate HMAC Key success`);
    }).catch((error: Error) => {
      console.error(`promise: generate HMAC Key failed, ${JSON.stringify(error)}`);
      throw (error as Error);
    })
}
/* 2.执行 HMAC 计算 */
async function hMACData() {
  let options: huks.HuksOptions = {
    properties: getHMACProperties(),
    inData: stringToUint8Array(plainText)
  }

  await huks.initSession(hmacKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: Error) => {
      console.error(`promise: init session failed, ${JSON.stringify(error)}`);
      throw (error as Error);
    })

  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: HMAC data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      hashData = data.outData as Uint8Array;
    }).catch((error: Error) => {
      console.error(`promise: HMAC data failed, ${JSON.stringify(error)}`);
      throw (error as Error);
    })
}

async function executeHMAC() {
  await generateHMACKey();
  await hMACData();
}
```
