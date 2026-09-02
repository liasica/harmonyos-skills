---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-extension-registration-and-unregistration-arkts
title: 注册/注销Provider(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > Provider管理 > 注册/注销Provider(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:32+08:00
doc_updated_at: 2026-08-03
content_hash: sha256:b7265679dfe605ccfa992c94151595e56575ce91bec3ffb57b60796f146ba011
---

从API 22开始，huksExternalCrypto提供Provider注册和注销功能接口。

## 注册Provider

### 开发步骤

1. 构造注册参数，需要传入[HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_NAME](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)。
2. 调用注册接口[registerProvider](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptoregisterprovider)。

### 开发案例

```ts
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

function StringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function registerProvider(): Promise<void> {
  try {
    /* 1.构造注册参数 */
    const providerName = "testProvider";
    const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [
      {
        tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_NAME,
        value: StringToUint8Array("CryptoExtension")
      }
    ];

    /* 2.调用registerProvider */
    await huksExternalCrypto.registerProvider(providerName, extProperties)
      .then(() => {
        console.info('promise: registerProvider success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: registerProvider failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: registerProvider input arg invalid.');
  }
}

async function TestRegisterProvider() {
  await registerProvider();
}
```

## 注册Provider并注册UIExtensionAbility

### 开发步骤

1. 构造注册参数，需要传入[HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_NAME](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)。
2. 构造UI注册参数，需要传入[HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_INFO](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)，该值为JSON字符串，包含abilityName和index两个字段，其中abilityName为该UIExtensionAbility中module.json5中的name字段，其长度不得大于128字节，index值的长度不得大于512字节，其值应是resourceId，1个CryptoExtension最多注册10个UIExtensionAbility。
3. 调用注册接口[registerProvider](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptoregisterprovider)。

### 开发案例

```ts
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

function StringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function registerProvider(): Promise<void> {
  try {
    /* 1.构造注册参数 ability name */
    const providerName = "testProvider";
    /* 2.构造 ability info */
    const abilityInfo = '[' +
      '{"abilityName":"UiAbility1","index":""},' +
      '{"abilityName":"UiAbility2","index":"string2"}]';
    const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [
      {
        tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_NAME,
        value: StringToUint8Array("CryptoExtension")
      }, {
        tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_INFO,
        value: StringToUint8Array(abilityInfo)
      }
    ];

    /* 3.调用registerProvider */
    await huksExternalCrypto.registerProvider(providerName, extProperties)
      .then(() => {
        console.info('promise: registerProvider success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: registerProvider failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: registerProvider input arg invalid.');
  }
}

async function TestRegisterProvider() {
  await registerProvider();
}
```

## 注销Provider

### 开发步骤

1. 构造注销参数，注销单个ability需要传入[HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_NAME](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数。批量注销不需要传入[HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_NAME](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数。
2. 调用注销接口[unregisterProvider](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptounregisterprovider)。

**注销单个ability**

```ts
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

function StringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function unregisterProvider(): Promise<void> {
  try {
    /* 1.构造注销参数 */
    const providerName = "testProvider";
    const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [
      {
        tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_NAME,
        value: StringToUint8Array("CryptoExtension")
      }
    ];

    /* 2.调用unregisterProvider */
    await huksExternalCrypto.unregisterProvider(providerName, extProperties)
      .then(() => {
        console.info('promise: unregisterProvider success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: unregisterProvider failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: unregisterProvider input arg invalid.');
  }
}

async function TestRegisterProvider() {
  await unregisterProvider();
}
```

**批量注销**

```ts
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function unregisterProvider(): Promise<void> {
  try {
    /* 1.构造注销参数 */
    const providerName = "testProvider";
    const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];

    /* 2.调用unregisterProvider */
    await huksExternalCrypto.unregisterProvider(providerName, extProperties)
      .then(() => {
        console.info('promise: unregisterProvider success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: unregisterProvider failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: unregisterProvider input arg invalid.');
  }
}

async function TestRegisterProvider() {
  await unregisterProvider();
}
```
