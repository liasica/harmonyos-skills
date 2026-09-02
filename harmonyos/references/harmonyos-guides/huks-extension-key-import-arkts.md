---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-extension-key-import-arkts
title: 密钥导入(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > 密钥管理 > 密钥导入(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:04+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:1b85187da445369c7a222b90d5eae942e9ebb8cd9b5f191fac6bb5cbed35767b
---

从API版本26.0.0开始，在外部密钥管理扩展场景下，密钥导入能力支持将加密封装的密钥对导入到扩展设备中。密钥用途等参数传递给Extension后，由Extension实现方根据业务场景自行处理，HUKS不做额外校验。

具体的场景介绍请参考[密钥生成与导入导出介绍](huks-extension-key-generation-import-overview.md)。

## 开发步骤

1. 通过[openAuthorizeDialog](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取keyUri作为resourceId，或通过[getResourceId](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptogetresourceid)获取外部密钥管理扩展的资源ID。
2. 调用[openResource](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptoopenresource)打开资源。
3. 调用[importWrappedKeyItem](../harmonyos-references/js-apis-huks.md#huksimportwrappedkeyitem9)导入加密封装的密钥对，密钥参数中需指定[HUKS\_TAG\_KEY\_CLASS](../harmonyos-references/js-apis-huks.md#hukstag)为[HUKS\_KEY\_CLASS\_EXTENSION](../harmonyos-references/js-apis-huks.md#hukskeyclasstype22)，表示该密钥由外部密钥管理扩展管理。
4. 关闭资源。

## 开发案例

```ts
import { huks, huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function openResource(resourceId: string): Promise<void> {
  try {
    await huksExternalCrypto.openResource(resourceId)
      .then(() => {
        console.info('promise: openResource success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: openResource failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: openResource input arg invalid.');
  }
}

async function importWrappedKeyItem(
  keyAlias: string,
  wrappingKeyAlias: string,
  huksOptions: huks.HuksOptions
): Promise<void> {
  try {
    await huks.importWrappedKeyItem(keyAlias, wrappingKeyAlias, huksOptions)
      .then(() => {
        console.info('promise: importWrappedKeyItem success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: importWrappedKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: importWrappedKeyItem input arg invalid.');
  }
}

async function closeResource(resourceId: string): Promise<void> {
  try {
    await huksExternalCrypto.closeResource(resourceId)
      .then(() => {
        console.info('promise: closeResource success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: closeResource failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: closeResource input arg invalid.');
  }
}

async function extensionKeyImport(): Promise<void> {
  /* 1.准备资源ID（keyAlias和wrappingKeyAlias使用resourceId） */
  const resourceId = JSON.stringify({
    providerName: "testProviderName",
    bundleName: "com.example.cryptoapplication",
    abilityName: "CryptoExtension",
    index: {
      key: "testKey"
    } as ESObject
  });
  const keyAlias = resourceId;
  const wrappingKeyAlias = resourceId;

  const properties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_CLASS,
      value: huks.HuksKeyClass.HUKS_KEY_CLASS_EXTENSION
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_RSA
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
    }
  ];
  // 加密封装的密钥数据（由Extension实现方定义格式）
  const wrappedKeyData: Uint8Array = new Uint8Array([/* 封装密钥数据 */]);
  const huksOptions: huks.HuksOptions = {
    properties: properties,
    inData: wrappedKeyData
  };

  try {
    /* 2.打开资源 */
    await openResource(resourceId);
    
    /* 3.导入加密封装的密钥 */
    await importWrappedKeyItem(keyAlias, wrappingKeyAlias, huksOptions);
    
    /* 4.关闭资源 */
    await closeResource(resourceId);
    
    console.info('promise: extensionKeyImport completed successfully.');
  } catch (error) {
    console.error('promise: extensionKeyImport input arg invalid.');
  }
}
```
