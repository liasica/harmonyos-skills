---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-extension-key-generation-import-export
title: 密钥生成与导入导出
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 密钥管理扩展 > 密钥管理扩展使用 > 密钥生成与导入导出
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:41+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f3b41d053b891023b8895f0d1c2ecacdefaa216bdddc7f0065e04de8a7357f0b
---

从API版本26.0.0开始，HUKS提供密钥生成、导入与导出能力。在密钥管理扩展场景下（如UKey物理设备），应用可通过HUKS标准接口在密钥管理扩展服务中生成密钥对、导入加密封装的密钥对或导出公钥。

调用方包括但不限于：三方应用、浏览器、内部模块（如证书管理）等。HUKS框架负责将接口调用转发到密钥管理扩展服务中完成实际操作，**调用方无需关心具体实现细节**。

## 功能概述

本节涵盖密钥生命周期的核心操作：

* 在密钥管理扩展场景下，keyAlias即为resourceId，即已执行过打开资源操作，且keyAlias中包含的providerName、abilityName、bundleName内容一致。
* 调用时均需指定[HUKS\_TAG\_KEY\_CLASS](../harmonyos-references/js-apis-huks.md#hukstag)为[HUKS\_KEY\_CLASS\_EXTENSION](../harmonyos-references/js-apis-huks.md#hukskeyclasstype22)，表示该密钥由密钥管理扩展服务实现方管理，密钥用途等参数由密钥管理扩展服务实现方根据业务场景自行处理，**HUKS不做额外校验**。

## 密钥生成（ArkTS）

在密钥管理扩展场景下，HUKS支持在密钥管理扩展服务中生成密钥对。生成的密钥存储在服务中，私钥不会离开服务提供方，公钥可通过导出接口获取。密钥用途等参数由密钥管理扩展服务提供方根据业务场景自行处理，HUKS不做额外校验。

应用通过调用HUKS的[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)接口发起密钥生成请求，请求被转发到CryptoExtensionAbility的[onGenerateKeyItem](../harmonyos-references/js-apis-cryptoextensionability.md#ongeneratekeyitem)接口完成密钥生成。

### 开发步骤

1. 通过[获取资源ID](huks-extension-ability-general-operation.md#获取资源id)操作，得到resourceId，并传入该resourceId进行打开资源，可参考[打开关闭资源](huks-extension-ability-general-operation.md#打开关闭资源)。
2. 调用[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)生成密钥对。建议传入算法类型、密钥长度、密钥用途等参数。密钥参数中需指定[HUKS\_TAG\_KEY\_CLASS](../harmonyos-references/js-apis-huks.md#hukstag)为[HUKS\_KEY\_CLASS\_EXTENSION](../harmonyos-references/js-apis-huks.md#hukskeyclasstype22)，表示该密钥由密钥管理扩展服务管理。
3. 操作执行完后，关闭资源，可参考[打开关闭资源](huks-extension-ability-general-operation.md#打开关闭资源)。

### 开发示例

```typescript
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

async function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions): Promise<void> {
  try {
    await huks.generateKeyItem(keyAlias, huksOptions)
      .then(() => {
        console.info('promise: generateKeyItem success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: generateKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: generateKeyItem input arg invalid.');
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

async function extensionKeyGeneration(): Promise<void> {
  /* 1.准备资源ID（keyAlias使用resourceId） */
  const resourceId = JSON.stringify({
    providerName: 'testProviderName',
    bundleName: 'com.example.cryptoapplication',
    abilityName: 'CryptoExtension',
    index: {
      key: 'testKey'
    } as ESObject
  });
  const keyAlias = resourceId;

  const properties: huks.HuksParam[] = [
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_CLASS,
      value: huks.HuksKeyClassType.HUKS_KEY_CLASS_EXTENSION
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
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
    }
  ];
  const huksOptions: huks.HuksOptions = {
    properties: properties,
    inData: new Uint8Array([])
  };

  try {
    /* 2.打开资源 */
    await openResource(resourceId);

    /* 3.生成密钥 */
    await generateKeyItem(keyAlias, huksOptions);

    /* 4.关闭资源 */
    await closeResource(resourceId);

    console.info('promise: extensionKeyGeneration completed successfully.');
  } catch (error) {
    console.error('promise: extensionKeyGeneration input arg invalid.');
  }
}
```

## 密钥导入（ArkTS）

在密钥管理扩展场景下，HUKS支持将加密封装的密钥对导入到密钥管理扩展服务中。封装密钥对通常由安全协商密钥加密，确保密钥在传输过程中不被泄露。密钥用途等参数由外部密钥管理服务提供方根据业务场景自行处理，HUKS不做额外校验。

* 接口入参中涉及的keyAlias和wrappingKeyAlias为resourceId，2个参数必须已通过打开资源接口在密钥管理扩展服务中成功打开。若任一resourceId未打开或已关闭，接口将返回资源不存在的错误。
* 当传入的keyAlias和wrappingKeyAlias不一致时，默认将证书导入到keyAlias所标识的资源中。

应用通过调用HUKS的[importWrappedKeyItem](../harmonyos-references/js-apis-huks.md#huksimportwrappedkeyitem9)接口发起密钥安全导入请求，请求被转发到CryptoExtensionAbility的[onImportWrappedKeyItem](../harmonyos-references/js-apis-cryptoextensionability.md#onimportwrappedkeyitem)接口完成密钥安全导入。

### 开发步骤

1. 通过[获取资源ID](huks-extension-ability-general-operation.md#获取资源id)操作，得到resourceId，并传入该resourceId进行打开资源，可参考[打开关闭资源](huks-extension-ability-general-operation.md#打开关闭资源)。
2. 调用[importWrappedKeyItem](../harmonyos-references/js-apis-huks.md#huksimportwrappedkeyitem9)导入加密封装的密钥对。密钥参数中需指定[HUKS\_TAG\_KEY\_CLASS](../harmonyos-references/js-apis-huks.md#hukstag)为[HUKS\_KEY\_CLASS\_EXTENSION](../harmonyos-references/js-apis-huks.md#hukskeyclasstype22)，表示该密钥由密钥管理扩展服务管理。
3. 操作执行完后，关闭资源，可参考[打开关闭资源](huks-extension-ability-general-operation.md#打开关闭资源)。

### 开发示例

```typescript
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
    providerName: 'testProviderName',
    bundleName: 'com.example.cryptoapplication',
    abilityName: 'CryptoExtension',
    index: {
      key: 'testKey'
    } as ESObject
  });
  const keyAlias = resourceId;
  const wrappingKeyAlias = resourceId;

  const properties: huks.HuksParam[] = [
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_CLASS,
      value: huks.HuksKeyClassType.HUKS_KEY_CLASS_EXTENSION
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

## 密钥导出（ArkTS）

在密钥管理扩展场景下，HUKS支持从密钥管理扩展服务中导出指定密钥的公钥。导出的公钥可用于证书申请、密钥协商、PIN加密等场景。

应用通过调用HUKS的[exportKeyItem](../harmonyos-references/js-apis-huks.md#huksexportkeyitem9)接口发起公钥导出请求，请求被转发到CryptoExtensionAbility的[onExportKeyItem](../harmonyos-references/js-apis-cryptoextensionability.md#onexportkeyitem)接口完成公钥导出。

### 开发步骤

1. 通过[获取资源ID](huks-extension-ability-general-operation.md#获取资源id)操作，得到resourceId，并传入该resourceId进行打开资源，可参考[打开关闭资源](huks-extension-ability-general-operation.md#打开关闭资源)。
2. 调用[exportKeyItem](../harmonyos-references/js-apis-huks.md#huksexportkeyitem9)导出公钥，密钥参数中需指定[HUKS\_TAG\_KEY\_CLASS](../harmonyos-references/js-apis-huks.md#hukstag)为[HUKS\_KEY\_CLASS\_EXTENSION](../harmonyos-references/js-apis-huks.md#hukskeyclasstype22)，表示该密钥由外部密钥管理扩展管理。
3. 操作执行完后，关闭资源，可参考[打开关闭资源](huks-extension-ability-general-operation.md#打开关闭资源)。

### 开发示例

```typescript
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

async function exportPublicKey(keyAlias: string): Promise<Uint8Array> {
  let publicKey: Uint8Array = new Uint8Array([]);
  try {
    const exportProperties: huks.HuksParam[] = [
      {
        tag: huks.HuksTag.HUKS_TAG_KEY_CLASS,
        value: huks.HuksKeyClassType.HUKS_KEY_CLASS_EXTENSION
      }
    ];
    const exportOptions: huks.HuksOptions = {
      properties: exportProperties
    };
    await huks.exportKeyItem(keyAlias, exportOptions)
      .then((data) => {
        publicKey = data.outData as Uint8Array;
        console.info('promise: exportKeyItem success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: exportKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: exportKeyItem input arg invalid.');
  }
  return publicKey;
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

async function extensionKeyExport(): Promise<Uint8Array> {
  /* 1.准备资源ID */
  const resourceId = 'your_resource_id';

  let publicKey: Uint8Array = new Uint8Array([]);
  try {
    /* 2.打开资源 */
    await openResource(resourceId);

    /* 3.导出公钥 */
    publicKey = await exportPublicKey(resourceId);
    console.info(`promise: public key length: ${publicKey.length}`);

    /* 4.关闭资源 */
    await closeResource(resourceId);

    console.info('promise: extensionKeyExport completed successfully.');
  } catch (error) {
    console.error('promise: extensionKeyExport input arg invalid.');
  }
  return publicKey;
}
```

## 规格差异说明

以上接口复用HUKS原有接口定义。在密钥管理扩展场景下，params中的参数为可选参数，由密钥管理扩展服务实现方定义支持范围。如未传入相应参数，密钥管理扩展服务将使用设置的默认行为。

* **密钥生成（generateKeyItem）**：推荐传入算法类型（HUKS\_TAG\_ALGORITHM）、密钥长度（HUKS\_TAG\_KEY\_SIZE）、密钥用途（HUKS\_TAG\_PURPOSE）等参数。如未传入，密钥管理扩展服务将使用默认值。keyAlias需传入有效的resourceId。
* **密钥安全导入（importWrappedKeyItem）**：推荐传入算法类型、密钥长度、密钥用途等参数。keyAlias和wrappingKeyAlias需传入有效的resourceId。wrappedKey为封装密钥数据，格式由密钥管理扩展服务实现方定义。
* **公钥导出（exportKeyItem）**：推荐传入密钥用途（HUKS\_TAG\_PURPOSE）参数，以便导出指定用途的公钥。如未传入，密钥管理扩展服务将使用默认值（通常默认签名用途）。keyAlias需传入有效的resourceId。
