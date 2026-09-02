---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-encryption-decryption-arkts
title: 加解密(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 加密/解密 > 加解密(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:31+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c172eedb6d033f7b766082dd96ad78892484840eae7b78104bd4ad4cda83c86d
---

以AES128、RSA2048、SM2和DES64为例，完成加解密。具体的场景介绍及支持的算法规格，请参考[加解密支持的算法](huks-encryption-decryption-overview.md#支持的算法)。

## 开发步骤

**生成密钥**

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集。
3. 调用[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)生成密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md)，导入已有的密钥。

**加密**

1. 获取密钥别名。
2. 获取待加密的数据。
3. 使用[HuksParam](../harmonyos-references/js-apis-huks.md#huksparam)设置加密算法参数配置。

   文档中提供多个示例，当使用不同算法时，请注意配置对应参数。

   * 使用AES算法加密，选取的分组模式为CBC、填充模式为PKCS7时，参数IV必选，请见开发案例：[AES/CBC/PKCS7](huks-encryption-decryption-arkts.md#aescbcpkcs7)。
   * 使用AES算法加密，选取的分组模式为GCM时，参数NONCE可选，AAD可选，请见开发案例：[AES/GCM/NoPadding](huks-encryption-decryption-arkts.md#aesgcmnopadding)。
   * 使用AES算法加密，选取的分组模式为CCM时，参数NONCE可选，AAD可选，请见开发案例：[AES/CCM/NoPadding](huks-encryption-decryption-arkts.md#aesccmnopadding)。
   * 使用RSA算法加密，需要选择相对应的分组模式、填充模式以及摘要算法DIGEST，请见开发案例：[RSA/ECB/PKCS1\_V1\_5](huks-encryption-decryption-arkts.md#rsaecbpkcs1_v1_5)和[RSA/ECB/OAEP/SHA256](huks-encryption-decryption-arkts.md#rsaecboaepsha256)。
   * 使用SM2算法加密，摘要算法DIGEST需要指定为SM3，请见开发案例：[SM2](huks-encryption-decryption-arkts.md#sm2)。

   详细规格请参考[加密/解密介绍及算法规格](huks-encryption-decryption-overview.md)。
4. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
5. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，获取加密后的密文。

**解密**

1. 获取密钥别名。
2. 获取待解密的密文。
3. 使用[HuksParam](../harmonyos-references/js-apis-huks.md#huksparam)设置解密算法参数配置。

   文档中提供多个示例，当使用不同算法时，请注意配置对应参数。

   * 使用AES算法解密，用例中选取的分组模式为GCM时，必须要填参数NONCE和参数AEAD，AAD可选，请见开发案例：[AES/GCM/NoPadding](huks-encryption-decryption-arkts.md#aesgcmnopadding)。
   * 其余示例参数与加密要求一致。

   详细规格请参考[加密/解密介绍及算法规格](huks-encryption-decryption-overview.md)。
4. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
5. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，获取解密后的数据。

**删除密钥**

当密钥废弃不用时，需要调用[deleteKeyItem](../harmonyos-references/js-apis-huks.md#huksdeletekeyitem9)删除密钥，具体请参考[密钥删除](huks-delete-key-arkts.md)。

## 开发案例

### AES/CBC/PKCS7

```typescript
/*
 * 以下以AES/CBC/PKCS7的Promise操作使用为例
 */
import { huks } from '@kit.UniversalKeystoreKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let aesKeyAlias = 'test_aesKeyAlias';
let handle: number;
let plainText = '123456';
let IV = cryptoFramework.createRandom().generateRandomSync(12).data;
let cipherData: Uint8Array;

function stringToUint8Array(str: string) {
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

function getAesGenerateProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  }];
  return properties;
}

function getAesEncryptProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_CBC
  }, {
    tag: huks.HuksTag.HUKS_TAG_IV,
    value: IV
  }];
  return properties;
}

function getAesDecryptProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_CBC
  }, {
    tag: huks.HuksTag.HUKS_TAG_IV,
    value: IV
  }];
  return properties;
}

async function generateAesKey() {
  /*
   * 模拟生成密钥场景
   */
  /*
   * 1. 获取生成密钥算法参数配置
   */
  let genProperties = getAesGenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  }
  /*
   * 2. 调用generateKeyItem
   */
  await huks.generateKeyItem(aesKeyAlias, options)
    .then(() => {
      console.info(`promise: generate AES Key success`);
    }).catch((error: BusinessError) => {
      console.error(`promise: generate AES Key failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function encryptData() {
  /*
   * 模拟加密场景
   */
  /*
   * 1. 获取加密算法参数配置
   */
  let encryptProperties = getAesEncryptProperties();
  let options: huks.HuksOptions = {
    properties: encryptProperties,
    inData: stringToUint8Array(plainText)
  }
  /*
   * 2. 调用initSession获取handle
   */
  await huks.initSession(aesKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(`promise: init EncryptData failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
  /*
   * 3. 调用finishSession获取加密后的密文
   */
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: encrypt data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      cipherData = data.outData as Uint8Array;
    }).catch((error: BusinessError) => {
      console.error(`promise: encrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function decryptData() {
  /*
   * 模拟解密场景
   * 1. 获取密钥别名
   */
  /*
   * 1. 获取解密算法参数配置
   */
  let decryptOptions = getAesDecryptProperties()
  let options: huks.HuksOptions = {
    properties: decryptOptions,
    inData: cipherData
  }
  /*
   * 2. 调用initSession获取handle
   */
  await huks.initSession(aesKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(`promise: init DecryptData failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
  /*
   * 3. 调用finishSession获取解密后的数据
   */
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: decrypt data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
    }).catch((error: BusinessError) => {
      console.error(`promise: decrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function deleteKey() {
  /*
   * 模拟删除密钥场景
   */
  let emptyOptions: huks.HuksOptions = {
    properties: []
  }
  /*
   * 1. 调用deleteKeyItem删除密钥
   */
  await huks.deleteKeyItem(aesKeyAlias, emptyOptions)
    .then(() => {
      console.info(`promise: delete data success`);
    }).catch((error: BusinessError) => {
      console.error(`promise: delete data failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}
```

### AES/GCM/NoPadding

```typescript
/*
 * 以下以AES/GCM/NoPadding的Promise操作使用为例
 */
import { huks } from '@kit.UniversalKeystoreKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let aesKeyAlias = 'test_aesKeyAlias';
let handle: number;
let plainText = '123456';
let cipherData: Uint8Array;
let AAD = '1234567890123456';
let NONCE = cryptoFramework.createRandom().generateRandomSync(12).data;

function stringToUint8Array(str: string) {
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

function getAesGenerateProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  }];
  return properties;
}

function getAesGcmEncryptProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_NONE
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_GCM
  }, {
    tag: huks.HuksTag.HUKS_TAG_NONCE,
    value: NONCE
  }, {
    tag: huks.HuksTag.HUKS_TAG_ASSOCIATED_DATA,
    value: stringToUint8Array(AAD)
  }];
  return properties;
}

function getAesGcmDecryptProperties(cipherData: Uint8Array) {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_NONE
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_GCM
  }, {
    tag: huks.HuksTag.HUKS_TAG_NONCE,
    value: NONCE
  }, {
    tag: huks.HuksTag.HUKS_TAG_ASSOCIATED_DATA,
    value: stringToUint8Array(AAD)
  }, {
    tag: huks.HuksTag.HUKS_TAG_AE_TAG,
    value: cipherData.slice(cipherData.length - 16)
  }];
  return properties;
}

async function generateAesKey() {
  /*
   * 模拟生成密钥场景
   */
  /*
   * 1. 获取生成密钥算法参数配置
   */
  let genProperties = getAesGenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  }
  /*
   * 2. 调用generateKeyItem
   */
  await huks.generateKeyItem(aesKeyAlias, options)
    .then(() => {
      console.info(`promise: generate AES Key success`);
    }).catch((error: BusinessError) => {
      console.error(`promise: generate AES Key failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function encryptData() {
  /*
   * 模拟加密场景
   */
  /*
   * 1. 获取加密算法参数配置
   */
  let encryptProperties = getAesGcmEncryptProperties();
  let options: huks.HuksOptions = {
    properties: encryptProperties,
    inData: stringToUint8Array(plainText)
  }
  /*
   * 2. 调用initSession获取handle
   */
  await huks.initSession(aesKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(`promise: init EncryptDataGcm failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
  /*
   * 3. 调用finishSession获取加密后的密文
   */
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: encrypt data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      cipherData = data.outData as Uint8Array;
    }).catch((error: BusinessError) => {
      console.error(`promise: encrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function decryptData() {
  /*
   * 模拟解密场景
   */
  /*
   * 1. 获取解密算法参数配置
   */
  let decryptOptions = getAesGcmDecryptProperties(cipherData)
  let options: huks.HuksOptions = {
    properties: decryptOptions,
    inData: cipherData.slice(0, cipherData.length - 16)
  }
  /*
   * 2. 调用initSession获取handle
   */
  await huks.initSession(aesKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(`promise: init DecryptDataGcm failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
  /*
   * 3. 调用finishSession获取解密后的数据
   */
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: decrypt data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
    }).catch((error: BusinessError) => {
      console.error(`promise: decrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function deleteKey() {
  /*
   * 模拟删除密钥场景
   */
  let emptyOptions: huks.HuksOptions = {
    properties: []
  }
  /*
   * 1. 调用deleteKeyItem删除密钥
   */
  await huks.deleteKeyItem(aesKeyAlias, emptyOptions)
    .then(() => {
      console.info(`promise: delete data success`);
    }).catch((error: BusinessError) => {
      console.error(`promise: delete data failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}
```

### AES/CCM/NoPadding

```ts
/*
 * 以下以AES/CCM/NoPadding的Promise操作使用为例
 */
import { huks } from '@kit.UniversalKeystoreKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from "@kit.BasicServicesKit";

let aesKeyAlias = 'test_aesCcmKeyAlias';
let handle: number;
let plainText = '123456';
let cipherData: Uint8Array;
let AAD = '1234567890123456';
let NONCE = cryptoFramework.createRandom().generateRandomSync(12).data;
let aeadTagLen = 14;

function StringToUint8Array(str: string) {
  let arr: number[] = new Array();
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function Uint8ArrayToString(fileData: Uint8Array) {
  let dataString = '';
  for (let i = 0; i < fileData.length; i++) {
    dataString += String.fromCharCode(fileData[i]);
  }
  return dataString;
}

function GetAesGenerateProperties() {
  let properties: Array<huks.HuksParam> = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  }];
  return properties;
}

function GetAesCcmEncryptProperties() {
  let properties: Array<huks.HuksParam> = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_NONE
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_CCM
  }, {
    tag: huks.HuksTag.HUKS_TAG_NONCE,
    value: NONCE
  }, {
    tag: huks.HuksTag.HUKS_TAG_ASSOCIATED_DATA,
    value: StringToUint8Array(AAD)
  }, {
    tag: huks.HuksTag.HUKS_TAG_AE_TAG_LEN,
    value: aeadTagLen
  }];
  return properties;
}

function GetAesCcmDecryptProperties(cipherData: Uint8Array) {
  let properties: Array<huks.HuksParam> = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_NONE
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_CCM
  }, {
    tag: huks.HuksTag.HUKS_TAG_NONCE,
    value: NONCE
  }, {
    tag: huks.HuksTag.HUKS_TAG_ASSOCIATED_DATA,
    value: StringToUint8Array(AAD)
  }, {
    tag: huks.HuksTag.HUKS_TAG_AE_TAG,
    value: cipherData.slice(cipherData.length - aeadTagLen)
  }, {
    tag: huks.HuksTag.HUKS_TAG_AE_TAG_LEN,
    value: aeadTagLen
  }];
  return properties;
}

async function GenerateAesKey() {
  /*
   * 模拟生成密钥场景
   * 1. 确定密钥别名
   */
  /*
   * 2. 获取生成密钥算法参数配置
   */
  let genProperties = GetAesGenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  }
  /*
   * 3. 调用generateKeyItem
   */
  await huks.generateKeyItem(aesKeyAlias, options)
    .then(() => {
      console.info(`promise: generate AES Key success`);
    }).catch((error: BusinessError) => {
      console.error(`promise: generate AES Key failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function EncryptData() {
  /*
   * 模拟加密场景
   * 1. 获取密钥别名
   */
  /*
   * 2. 获取待加密的数据
   */
  /*
   * 3. 获取加密算法参数配置
   */
  let encryptProperties = GetAesCcmEncryptProperties();
  let options: huks.HuksOptions = {
    properties: encryptProperties,
    inData: StringToUint8Array(plainText)
  }
  /*
   * 4. 调用initSession获取handle
   */
  await huks.initSession(aesKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(`promise: init EncryptDataCcm failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
  /*
   * 5. 调用finishSession获取加密后的密文
   */
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: encrypt data success, data is ` + Uint8ArrayToString(data.outData as Uint8Array));
      cipherData = data.outData as Uint8Array;
    }).catch((error: BusinessError) => {
      console.error(`promise: encrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function DecryptData() {
  /*
   * 模拟解密场景
   * 1. 获取密钥别名
   */
  /*
   * 2. 获取待解密的密文
   */
  /*
   * 3. 获取解密算法参数配置
   */
  let decryptOptions = GetAesCcmDecryptProperties(cipherData)
  let options: huks.HuksOptions = {
    properties: decryptOptions,
    inData: cipherData.slice(0, cipherData.length - aeadTagLen)
  }
  /*
   * 4. 调用initSession获取handle
   */
  await huks.initSession(aesKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(`promise: init DecryptDataCcm failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
  /*
   * 5. 调用finishSession获取解密后的数据
   */
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: decrypt data success, data is ` + Uint8ArrayToString(data.outData as Uint8Array));
    }).catch((error: BusinessError) => {
      console.error(`promise: decrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function DeleteKey() {
  /*
   * 模拟删除密钥场景
   * 1. 获取密钥别名
   */
  let emptyOptions: huks.HuksOptions = {
    properties: []
  }
  /*
   * 2. 调用deleteKeyItem删除密钥
   */
  await huks.deleteKeyItem(aesKeyAlias, emptyOptions)
    .then(() => {
      console.info(`promise: delete data success`);
    }).catch((error: BusinessError) => {
      console.error(`promise: delete data failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function TestEncryptDecrypt() {
  await GenerateAesKey();
  await EncryptData();
  await DecryptData();
  await DeleteKey();
}
```

### RSA/ECB/PKCS1\_V1\_5

```typescript
/*
 * 以下以RSA/ECB/PKCS1_V1_5模式的Promise操作使用为例
 */
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rsaKeyAlias = 'test_rsaKeyAlias';
let handle: number;
let plainText = '123456';
let cipherData: Uint8Array;

function stringToUint8Array(str: string) {
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

function getRsaGenerateProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  }];
  return properties;
}

function getRsaEncryptProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS1_V1_5
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_NONE
  }];
  return properties;
}

function getRsaDecryptProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS1_V1_5
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_NONE
  }];
  return properties;
}

async function generateRsaKey() {
  /*
   * 模拟生成密钥场景
   */
  /*
   * 1. 获取生成密钥算法参数配置
   */
  let genProperties = getRsaGenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  }
  /*
   * 2. 调用generateKeyItem
   */
  await huks.generateKeyItem(rsaKeyAlias, options)
    .then(() => {
      console.info(`promise: generate RSA Key success`);
    }).catch((error: BusinessError) => {
      console.error(`promise: generate RSA Key failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function encryptData() {
  /*
   * 模拟加密场景
   */
  /*
   * 1. 获取加密算法参数配置
   */
  let encryptProperties = getRsaEncryptProperties();
  let options: huks.HuksOptions = {
    properties: encryptProperties,
    inData: stringToUint8Array(plainText)
  }
  /*
   * 2. 调用initSession获取handle
   */
  await huks.initSession(rsaKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(`promise: init EncryptDataRsa failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
  /*
   * 3. 调用finishSession获取加密后的密文
   */
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: encrypt data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      cipherData = data.outData as Uint8Array;
    }).catch((error: BusinessError) => {
      console.error(`promise: encrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function decryptData() {
  /*
   * 模拟解密场景
   */
  /*
   * 1. 获取解密算法参数配置
   */
  let decryptOptions = getRsaDecryptProperties()
  let options: huks.HuksOptions = {
    properties: decryptOptions,
    inData: cipherData
  }
  /*
   * 2. 调用initSession获取handle
   */
  await huks.initSession(rsaKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(`promise: init DecryptDataRsa failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
  /*
   * 3. 调用finishSession获取解密后的数据
   */
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: decrypt data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
    }).catch((error: BusinessError) => {
      console.error(`promise: decrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function deleteKey() {
  /*
   * 模拟删除密钥场景
   */
  let emptyOptions: huks.HuksOptions = {
    properties: []
  }
  /*
   * 1. 调用deleteKeyItem删除密钥
   */
  await huks.deleteKeyItem(rsaKeyAlias, emptyOptions)
    .then(() => {
      console.info(`promise: delete data success`);
    }).catch((error: BusinessError) => {
      console.error(`promise: delete data failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}
```

### RSA/ECB/OAEP/SHA256

```typescript
/*
 * 以下以RSA/ECB/OAEP/SHA256模式的Promise操作使用为例
 */
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rsaKeyAlias = 'test_rsaKeyAlias';
let handle: number;
let plainText = '123456';
let cipherData: Uint8Array;

function stringToUint8Array(str: string) {
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

function getRsaGenerateProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  }];
  return properties;
}

function getRsaEncryptProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_OAEP
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }];
  return properties;
}

function getRsaDecryptProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_OAEP
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }];
  return properties;
}

async function generateRsaKey() {
  /*
   * 模拟生成密钥场景
   */
  /*
   * 1. 获取生成密钥算法参数配置
   */
  let genProperties = getRsaGenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  }
  /*
   * 2. 调用generateKeyItem
   */
  await huks.generateKeyItem(rsaKeyAlias, options)
    .then(() => {
      console.info(`promise: generate RSA Key success`);
    }).catch((error: BusinessError) => {
      console.error(`promise: generate RSA Key failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function encryptData() {
  /*
   * 模拟加密场景
   */
  /*
   * 1. 获取加密算法参数配置
   */
  let encryptProperties = getRsaEncryptProperties();
  let options: huks.HuksOptions = {
    properties: encryptProperties,
    inData: stringToUint8Array(plainText)
  }
  /*
   * 2. 调用initSession获取handle
   */
  await huks.initSession(rsaKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(`promise: init EncryptDataRsa failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
  /*
   * 3. 调用finishSession获取加密后的密文
   */
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: encrypt data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      cipherData = data.outData as Uint8Array;
    }).catch((error: BusinessError) => {
      console.error(`promise: encrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function decryptData() {
  /*
   * 模拟解密场景
   */
  /*
   * 1. 获取解密算法参数配置
   */
  let decryptOptions = getRsaDecryptProperties()
  let options: huks.HuksOptions = {
    properties: decryptOptions,
    inData: cipherData
  }
  /*
   * 2. 调用initSession获取handle
   */
  await huks.initSession(rsaKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(`promise: init DecryptDataRsa failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
  /*
   * 3. 调用finishSession获取解密后的数据
   */
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: decrypt data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
    }).catch((error: BusinessError) => {
      console.error(`promise: decrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function deleteKey() {
  /*
   * 模拟删除密钥场景
   */
  let emptyOptions: huks.HuksOptions = {
    properties: []
  }
  /*
   * 1. 调用deleteKeyItem删除密钥
   */
  await huks.deleteKeyItem(rsaKeyAlias, emptyOptions)
    .then((data) => {
      console.info(`promise: delete data success`);
    }).catch((error: BusinessError) => {
      console.error(`promise: delete data failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}
```

### SM2

```typescript
/*
 * 以下以SM2模式的Promise操作使用为例
 */
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

let sm2KeyAlias = 'test_sm2KeyAlias';
let handle: number;
let plainText = '123456';
let cipherData: Uint8Array;

function stringToUint8Array(str: string) {
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

function getSm2GenerateProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_SM2
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_SM2_KEY_SIZE_256
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  }];
  return properties;
}

function getSm2EncryptProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_SM2
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_SM2_KEY_SIZE_256
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SM3
  }];
  return properties;
}

function getSm2DecryptProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_SM2
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_SM2_KEY_SIZE_256
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SM3
  }];
  return properties;
}

async function generateSm2Key() {
  /*
   * 模拟生成密钥场景
   */
  /*
   * 1. 获取生成密钥算法参数配置
   */
  let genProperties = getSm2GenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  }
  /*
   * 2. 调用generateKeyItem
   */
  await huks.generateKeyItem(sm2KeyAlias, options)
    .then(() => {
      console.info(`promise: generate SM2 Key success`);
    }).catch((error: BusinessError) => {
      console.error(`promise: generate SM2 Key failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function encryptDataSm2() {
  /*
   * 模拟加密场景
   */
  /*
   * 1. 获取加密算法参数配置
   */
  let encryptProperties = getSm2EncryptProperties();
  let options: huks.HuksOptions = {
    properties: encryptProperties,
    inData: stringToUint8Array(plainText)
  }
  /*
   * 2. 调用initSession获取handle
   */
  await huks.initSession(sm2KeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(`promise: init EncryptDataSm2 failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
  /*
   * 3. 调用finishSession获取加密后的密文
   */
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: encrypt data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      cipherData = data.outData as Uint8Array;
    }).catch((error: BusinessError) => {
      console.error(`promise: encrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function decryptDataSm2() {
  /*
   * 模拟解密场景
   */
  /*
   * 1. 获取解密算法参数配置
   */
  let decryptOptions = getSm2DecryptProperties()
  let options: huks.HuksOptions = {
    properties: decryptOptions,
    inData: cipherData
  }
  /*
   * 2. 调用initSession获取handle
   */
  await huks.initSession(sm2KeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(`promise: init DecryptDataSm2 failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
  /*
   * 3. 调用finishSession获取解密后的数据
   */
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: decrypt data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
    }).catch((error: BusinessError) => {
      console.error(`promise: decrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function deleteKey() {
  /*
   * 模拟删除密钥场景
   */
  let emptyOptions: huks.HuksOptions = {
    properties: []
  }
  /*
   * 1. 调用deleteKeyItem删除密钥
   */
  await huks.deleteKeyItem(sm2KeyAlias, emptyOptions)
    .then(() => {
      console.info(`promise: delete data success`);
    }).catch((error: BusinessError) => {
      console.error(`promise: delete data failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}
```
