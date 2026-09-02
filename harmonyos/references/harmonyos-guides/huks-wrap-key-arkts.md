---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-wrap-key-arkts
title: 加密导出导入密钥(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 其他操作 > 加密导出导入密钥 > 加密导出导入密钥(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:32+08:00
doc_updated_at: 2026-04-29
content_hash: sha256:c5e416ea0232c67267bcd6a40345279a22bb94b4e869f902624da833c703fa3d
---

从API 20开始，支持加密导出导入密钥。

当前指导提供以下加密导出导入密钥示例：

* [加密导出导入普通密钥](huks-wrap-key-arkts.md#加密导出导入普通密钥)
* [普通密钥导入为群组密钥](huks-wrap-key-arkts.md#普通密钥导入为群组密钥)

## 开发步骤

1. 初始化生成密钥属性集，需要设置[HUKS\_TAG\_IS\_ALLOWED\_WRAP](../harmonyos-references/js-apis-huks.md#hukstag)，指定密钥允许导出。
2. 调用[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)生成密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。
3. 调用[wrapKeyItem](../harmonyos-references/js-apis-huks.md#hukswrapkeyitem20)加密导出密钥。
4. 调用[unwrapKeyItem](../harmonyos-references/js-apis-huks.md#huksunwrapkeyitem20)加密导入密钥。如果是从普通密钥导入为群组密钥，需要传入TUI PIN类型的AuthToken，认证TUI PIN并获取AuthToken请参考[数字盾服务](devicesecurity-trustedauth-verifybypwd.md#开发步骤)。

## 开发案例

### 加密导出导入普通密钥

```ts
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = "testWrapKey";
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_NONE
  },
  {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_GCM
  },
  /* 生成密钥时指定允许加密导出 */
  {
    tag: huks.HuksTag.HUKS_TAG_IS_ALLOWED_WRAP,
    value: true
  }
];

let options: huks.HuksOptions = {
  properties: properties,
};

let wrapKeyProperties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_WRAP_TYPE,
    value: huks.HuksKeyWrapType.HUKS_KEY_WRAP_TYPE_HUK_BASED
  }
];

let wrapKeyOptions: huks.HuksOptions = {
  properties: wrapKeyProperties,
};

let wrappedKey: Uint8Array;

async function testGenerateKey() {
  await huks.generateKeyItem(keyAlias, options)
    .then((data) => {
      console.info(`promise: generateKeyItem success`);
    })
    .catch((error: Error) => {
      console.error(`promise: generateKeyItem failed`);
    });
}

async function testWrapKey(){
  await testGenerateKey();

  await huks.wrapKeyItem(keyAlias, wrapKeyOptions)
    .then((data) => {
      wrappedKey = data.outData as Uint8Array;
      console.info(`promise: wrapKeyItem success, data = ${JSON.stringify(data)}`);
    })
    .catch((error: Error) => {
      console.error(`promise: wrapKeyItem failed`);
    });

  await huks.unwrapKeyItem(keyAlias, wrapKeyOptions, wrappedKey)
    .then((data) => {
      console.info(`promise: unwrapKeyItem success`);
    })
    .catch((error: Error) => {
      console.error(`promise: unwrapKeyItem failed`);
    });
}
```

### 普通密钥导入为群组密钥

从API 23开始，支持从普通密钥导入为群组密钥。

```ts
import { huks } from '@kit.UniversalKeystoreKit';
import { trustedAuthentication } from '@kit.DeviceSecurityKit';

let keyAlias = "testWrapKey";
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_NONE
  },
  {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_GCM
  },
  /* 生成密钥时指定允许加密导出 */
  {
    tag: huks.HuksTag.HUKS_TAG_IS_ALLOWED_WRAP,
    value: true
  }
];

let options: huks.HuksOptions = {
  properties: properties,
};

let wrapKeyProperties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_WRAP_TYPE,
    value: huks.HuksKeyWrapType.HUKS_KEY_WRAP_TYPE_HUK_BASED
  }
];

let wrapKeyOptions: huks.HuksOptions = {
  properties: wrapKeyProperties,
};

let wrappedKey: Uint8Array;

async function testGenerateKey() {
  await huks.generateKeyItem(keyAlias, options)
    .then((data) => {
      console.info(`promise: generateKeyItem success`);
    })
    .catch((error: Error) => {
      console.error(`promise: generateKeyItem failed`);
    });
}

async function testWrapKey(){
  await testGenerateKey();

  await huks.wrapKeyItem(keyAlias, wrapKeyOptions)
    .then((data) => {
      wrappedKey = data.outData as Uint8Array;
      console.info(`promise: wrapKeyItem success, data = ${JSON.stringify(data)}`);
    })
    .catch((error: Error) => {
      console.error(`promise: wrapKeyItem failed`);
    });

  challenge = new Uint8Array(32);
  let label: trustedAuthentication.TUILable;
  let authID: bigint;
  /* 认证TUI PIN之前需要先创建数字盾，请参考数字盾服务，authID和label仅做示例 */
  let authToken = await trustedAuthentication.trustedAuthentication(challenge, authID, label);
  wrapKeyOptions.wrapKeyProperties.push({
    tag: huks.HuksTag.HUKS_TAG_AUTH_TOKEN,
    value: authToken.authToken
  })

  await huks.unwrapKeyItem(keyAlias, wrapKeyOptions, wrappedKey)
    .then((data) => {
      console.info(`promise: unwrapKeyItem success`);
    })
    .catch((error: Error) => {
      console.error(`promise: unwrapKeyItem failed`);
    });
}
```
