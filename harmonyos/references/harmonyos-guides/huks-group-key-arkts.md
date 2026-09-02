---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-group-key-arkts
title: 群组密钥(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 其他操作 > 群组密钥 > 群组密钥(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:efd84ea215874e6e05c12792eaaed84ba89f4a4b10adb9bdc70c6eefe438ba13
---

从API 23开始，HUKS支持群组密钥功能。群组密钥支持的HUKS密钥操作及详细介绍参考[群组密钥介绍](huks-group-key-overview.md)，本文档以[AES/CBC/PKCS7加解密](huks-group-key-arkts.md#aescbcpkcs7加解密)、[X25519非对称密钥协商](huks-group-key-arkts.md#x25519非对称密钥协商)、[PBKDF2派生密钥](huks-group-key-arkts.md#pbkdf2派生密钥)为例展示群组密钥使用方法。

**配置文件**

使用群组密钥之前，需要在app.json5文件中配置群组信息，配置方法参考[配置文件示例](app-configuration-file.md#配置文件示例)中assetAccessGroups字段的配置方式。

## AES/CBC/PKCS7加解密

### 开发步骤

**生成密钥**

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集。需要添加群组密钥标签[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)，推荐使用[HUKS\_TAG\_KEY\_OVERRIDE](../harmonyos-references/js-apis-huks.md#hukstag)，避免密钥被覆盖。
3. 调用[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)生成密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md)，导入已有的密钥。

**加密**

1. 指定密钥别名。
2. 指定待加密的数据。
3. 使用[HuksParam](../harmonyos-references/js-apis-huks.md#huksparam)设置加密算法参数配置。需要添加群组密钥标签[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)。
4. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
5. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，获取加密后的密文。

**解密**

1. 指定密钥别名。
2. 指定待解密的密文。
3. 使用[HuksParam](../harmonyos-references/js-apis-huks.md#huksparam)设置解密算法参数配置。需要添加群组密钥标签[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)。
4. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
5. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，获取解密后的数据。

**删除密钥**

1. 指定密钥别名。
2. 使用[HuksParam](../harmonyos-references/js-apis-huks.md#huksparam)设置密钥删除算法参数配置。需要添加群组密钥标签[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)。
3. 调用[deleteKeyItem](../harmonyos-references/js-apis-huks.md#huksdeletekeyitem9)删除密钥，具体请参考[密钥删除](huks-delete-key-arkts.md)。

### 开发示例

```ts
/*
 * 以下以AES/CBC/PKCS7的Promise操作使用为例
 */
import { huks } from '@kit.UniversalKeystoreKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from "@kit.BasicServicesKit";

let aesKeyAlias = 'groupKeyTestAesKeyAlias';
let handle: number;
let plainText = '123456';
let IV = cryptoFramework.createRandom().generateRandomSync(12).data;
let cipherData: Uint8Array;
/*
 * 需要在app.json5中配置assetAccessGroups字段新增群组信息
 */
let group = 'ohos.test.groupKey';

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
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_ACCESS_GROUP,
    value: StringToUint8Array(group)
  }];
  return properties;
}

function GetAesEncryptProperties() {
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
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_CBC
  }, {
    tag: huks.HuksTag.HUKS_TAG_IV,
    value: IV
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_ACCESS_GROUP,
    value: StringToUint8Array(group)
  }];
  return properties;
}

function GetAesDecryptProperties() {
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
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_CBC
  }, {
    tag: huks.HuksTag.HUKS_TAG_IV,
    value: IV
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_ACCESS_GROUP,
    value: StringToUint8Array(group)
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
      console.error(`promise: generate AES Key failed, errCode: ${error.code}, errMsg: ${error.message}`);
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
  let encryptProperties = GetAesEncryptProperties();
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
      console.error(`promise: init EncryptData failed, errCode: ${error.code}, errMsg: ${error.message}`);
    })
  /*
   * 5. 调用finishSession获取加密后的密文
   */
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: encrypt data success, data is ` + Uint8ArrayToString(data.outData as Uint8Array));
      cipherData = data.outData as Uint8Array;
    }).catch((error: BusinessError) => {
      console.error(`promise: encrypt data failed, errCode: ${error.code}, errMsg: ${error.message}`);
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
  let decryptOptions = GetAesDecryptProperties()
  let options: huks.HuksOptions = {
    properties: decryptOptions,
    inData: cipherData
  }
  /*
   * 4. 调用initSession获取handle
   */
  await huks.initSession(aesKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(`promise: init DecryptData failed, errCode: ${error.code}, errMsg: ${error.message}`);
    })
  /*
   * 5. 调用finishSession获取解密后的数据
   */
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: decrypt data success, data is ` + Uint8ArrayToString(data.outData as Uint8Array));
    }).catch((error: BusinessError) => {
      console.error(`promise: decrypt data failed, errCode: ${error.code}, errMsg: ${error.message}`);
    })
}

async function DeleteKey() {
  /*
   * 模拟删除密钥场景
   * 1. 获取密钥别名
   */
  let deleteProperties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_ACCESS_GROUP,
      value: StringToUint8Array(group)
    }
  ]
  let deleteOptions: huks.HuksOptions = {
    properties: deleteProperties
  }
  /*
   * 2. 调用deleteKeyItem删除密钥
   */
  await huks.deleteKeyItem(aesKeyAlias, deleteOptions)
    .then(() => {
      console.info(`promise: delete data success`);
    }).catch((error: BusinessError) => {
      console.error(`promise: delete data failed, errCode: ${error.code}, errMsg: ${error.message}`);
    })
}

async function TestGroupKeyEncryptDecrypt() {
  await GenerateAesKey();
  await EncryptData();
  await DecryptData();
  await DeleteKey();
}
```

## X25519非对称密钥协商

### 开发步骤

**生成密钥**

设备A、设备B各自生成一个非对称密钥，具体请参考[密钥生成](huks-key-generation-overview.md)或[密钥导入](huks-key-import-overview.md)。

密钥生成时，指定参数[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)，用于生成群组密钥。

**导出密钥**

设备A、B导出非对称密钥对的公钥材料，具体请参考[密钥导出](huks-export-key-arkts.md)。

导出密钥时，指定参数[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)，用于导出群组密钥。

**密钥协商**

设备A、B分别基于本端私钥和对端设备的公钥，协商出共享密钥。

密钥协商时，指定参数[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)，用于协商群组密钥。

**删除密钥**

当密钥废弃不用时，设备A、B均需要删除密钥，具体请参考[密钥删除](huks-delete-key-arkts.md)。

删除密钥时，指定参数[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)，用于删除群组密钥。

### 开发示例

```ts
/*
 * 以下以X25519密钥的Promise操作使用为例
 * 通过群组密钥协商群组密钥
 */
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from "@kit.BasicServicesKit";

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

/*
 * 确定密钥别名和封装密钥属性参数集
 */
let srcKeyAliasFirst = "AgreeX25519KeyFirstAlias";
let srcKeyAliasSecond = "AgreeX25519KeySecondAlias";
let agreeX25519InData = 'AgreeX25519TestIndata';
let finishOutData: Uint8Array;
let handle: number;
let exportKey: Uint8Array;
let exportKeyFirst: Uint8Array;
let exportKeySecond: Uint8Array;
/*
 * 需要在app.json5中配置assetAccessGroups字段新增群组信息
 */
let group = 'ohos.test.groupKey';
/* 集成生成密钥参数集 */
let properties: Array<huks.HuksParam> = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_X25519,
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_AGREE,
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_CURVE25519_KEY_SIZE_256,
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_NONE,
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_CBC,
  }, {
    tag: huks.HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
    value: huks.HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_ACCESS_GROUP,
    value: StringToUint8Array(group)
  }
];
let HuksOptions: huks.HuksOptions = {
  properties: properties,
  inData: new Uint8Array(new Array())
}
const finishProperties: Array<huks.HuksParam> = [{
    tag: huks.HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
    value: huks.HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
  }, {
    tag: huks.HuksTag.HUKS_TAG_IS_KEY_ALIAS,
    value: true
  }, {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES,
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256,
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value:
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT,
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_NONE,
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB,
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_ACCESS_GROUP,
    value: StringToUint8Array(group)
  }
];
/* 集成第一个协商参数集 */
let finishOptionsFirst: huks.HuksOptions = {
  properties: [
    ...finishProperties, {
    tag: huks.HuksTag.HUKS_TAG_KEY_ALIAS,
    value: StringToUint8Array(srcKeyAliasFirst + 'final'),
  }],
  inData: StringToUint8Array(agreeX25519InData)
}
/* 集成第二个协商参数集 */
let finishOptionsSecond: huks.HuksOptions = {
  properties: [
    ...finishProperties, {
    tag: huks.HuksTag.HUKS_TAG_KEY_ALIAS,
    value: StringToUint8Array(srcKeyAliasSecond + 'final'),
  }],
  inData: StringToUint8Array(agreeX25519InData)
}

/* 生成密钥 */
async function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info("promise: enter generateKeyItem");
  try {
    await huks.generateKeyItem(keyAlias, huksOptions)
      .then(() => {
        console.info(`promise: generateKeyItem success`);
      }).catch((error: BusinessError) => {
        console.error(`promise: generateKeyItem failed, errCode: ${error.code}, errMsg: ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: generateKeyItem input arg invalid`);
  }
}

/* 初始化密钥会话接口，并获取一个句柄（必选）和挑战值（可选） */
async function initSession(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info("promise: enter initSession");
  try {
    await huks.initSession(keyAlias, huksOptions)
      .then((data) => {
        handle = data.handle;
        console.info(`promise: initSession success`);
      }).catch((error: BusinessError) => {
        console.error(`promise: initSession failed, errCode: ${error.code}, errMsg: ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: initSession input arg invalid`);
  }
}

/* 分段添加密钥操作的数据并进行相应的密钥操作，输出处理数据 */
async function updateSession(handle: number, huksOptions: huks.HuksOptions) {
  console.info("promise: enter updateSession");
  try {
    await huks.updateSession(handle, huksOptions)
      .then((data) => {
        console.info(`promise: updateSession success, data is ` + Uint8ArrayToString(data.outData as Uint8Array));
      }).catch((error: BusinessError) => {
        console.error(`promise: updateSession failed, errCode: ${error.code}, errMsg: ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: updateSession input arg invalid`);
  }
}

/* 结束密钥会话并进行相应的密钥操作，输出处理数据 */
async function finishSession(handle: number, huksOptions: huks.HuksOptions) {
  console.info("promise: enter finishSession");
  try {
    await huks.finishSession(handle, huksOptions)
      .then((data) => {
        finishOutData = data.outData as Uint8Array;
        console.info(`promise: finishSession success, data is ` + Uint8ArrayToString(data.outData as Uint8Array));
      }).catch((error: BusinessError) => {
        console.error(`promise: finishSession failed, errCode: ${error.code}, errMsg: ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: finishSession input arg invalid`);
  }
}

/* 导出密钥 */
async function exportKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info("promise: enter exportKeyItem");
  try {
    await huks.exportKeyItem(keyAlias, huksOptions)
      .then((data) => {
        exportKey = data.outData as Uint8Array;
        console.info(`promise: exportKey success, data is ` + Uint8ArrayToString(data.outData as Uint8Array));
      }).catch((error: BusinessError) => {
        console.error(`promise: exportKeyItem failed, errCode: ${error.code}, errMsg: ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: exportKeyItem input arg invalid`);
  }
}

/* 删除密钥操作 */
async function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info("promise: enter deleteKeyItem");
  try {
    await huks.deleteKeyItem(keyAlias, huksOptions)
      .then(() => {
        console.info(`promise: deleteKeyItem success`);
      }).catch((error: BusinessError) => {
        console.error(`promise: deleteKeyItem failed, errCode: ${error.code}, errMsg: ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: deleteKeyItem input arg invalid`);
  }
}

async function testAgree() {
  /* 1.确定密钥别名并集成要参数集。A设备：srcKeyAliasFirst；B设备：srcKeyAliasSecond */
  /* 2.设备A生成密钥 */
  await generateKeyItem(srcKeyAliasFirst, HuksOptions);
  /* 3.设备B生成密钥 */
  await generateKeyItem(srcKeyAliasSecond, HuksOptions);
  /* 4.设备A、B导出非对称密钥的公钥 */
  await exportKeyItem(srcKeyAliasFirst, HuksOptions);
  exportKeyFirst = exportKey;
  await exportKeyItem(srcKeyAliasSecond, HuksOptions);
  exportKeySecond = exportKey;
  /* 5.对第一个密钥进行协商（三段式） */
  await initSession(srcKeyAliasFirst, HuksOptions);
  HuksOptions.inData = exportKeySecond;
  await updateSession(handle, HuksOptions);
  await finishSession(handle, finishOptionsFirst);
  /* 6.对第二个密钥进行协商（三段式） */
  await initSession(srcKeyAliasSecond, HuksOptions);
  HuksOptions.inData = exportKeyFirst;
  await updateSession(handle, HuksOptions);
  await finishSession(handle, finishOptionsSecond);
  /* 7.设备A、B删除密钥 */
  await deleteKeyItem(srcKeyAliasFirst, HuksOptions);
  await deleteKeyItem(srcKeyAliasSecond, HuksOptions);
}
```

## PBKDF2派生密钥

### 开发步骤

**生成密钥**

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 密钥生成时，指定参数[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)，用于生成群组密钥。
3. 调用[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)生成密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md)，导入已有的密钥。

**密钥派生**

1. 获取密钥别名，指定对应的属性参数HuksOptions，添加参数[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)，用于派生群组密钥。
2. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
3. 调用[updateSession](../harmonyos-references/js-apis-huks.md#huksupdatesession9)更新密钥会话。
4. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，完成派生。

**删除密钥**

当密钥废弃不用时，需要调用[deleteKeyItem](../harmonyos-references/js-apis-huks.md#huksdeletekeyitem9)删除密钥，具体请参考[密钥删除](huks-delete-key-arkts.md)。

删除密钥时，指定参数[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)，用于删除群组密钥。

### 开发示例

```ts
/*
 * 以下以PBKDF2密钥的Promise操作使用为例
 * 使用群组密钥派生群组密钥
 */
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from "@kit.BasicServicesKit";

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

/*
 * 确定密钥别名和封装密钥属性参数集
 */
let srcKeyAlias = "pbkdf2Key";
let salt = "mySalt";
let iterationCount = 10000;
let derivedKeySize = 32;
let handle: number;
let finishOutData: Uint8Array;
/*
 * 需要在app.json5中配置assetAccessGroups字段新增群组信息
 */
let group = 'ohos.test.groupKey';

/* 集成生成密钥参数集 */
let properties: Array<huks.HuksParam> = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES,
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DERIVE,
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256,
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256,
  }, {
    tag: huks.HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
    value: huks.HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_ACCESS_GROUP,
    value: StringToUint8Array(group)
  }
];

let huksOptions: huks.HuksOptions = {
  properties: properties,
  inData: new Uint8Array(new Array())
}

/* 集成init时密钥参数集 */
let initProperties: Array<huks.HuksParam> = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_PBKDF2,
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DERIVE,
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256,
  }, {
    tag: huks.HuksTag.HUKS_TAG_DERIVE_KEY_SIZE,
    value: derivedKeySize,
  }, {
    tag: huks.HuksTag.HUKS_TAG_ITERATION,
    value: iterationCount,
  }, {
    tag: huks.HuksTag.HUKS_TAG_SALT,
    value: StringToUint8Array(salt),
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_ACCESS_GROUP,
    value: StringToUint8Array(group)
  }
];

let initOptions: huks.HuksOptions = {
  properties: initProperties,
  inData: new Uint8Array(new Array())
}

/* 集成finish时密钥参数集 */
let finishProperties: Array<huks.HuksParam> = [{
    tag: huks.HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
    value: huks.HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
  }, {
    tag: huks.HuksTag.HUKS_TAG_IS_KEY_ALIAS,
    value: true,
  }, {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES,
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256,
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT,
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_NONE,
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_ALIAS,
    value: StringToUint8Array(srcKeyAlias),
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB,
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_ACCESS_GROUP,
    value: StringToUint8Array(group)
  }
];

let finishOptions: huks.HuksOptions = {
  properties: finishProperties,
  inData: new Uint8Array(new Array())
}

async function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info(`promise: enter generateKeyItem`);
  try {
    await huks.generateKeyItem(keyAlias, huksOptions)
      .then(() => {
        console.info(`promise: generateKeyItem success`);
      }).catch((error: BusinessError) => {
        console.error(`promise: generateKeyItem failed, errCode: ${error.code}, errMsg: ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: generateKeyItem input arg invalid`);
  }
}

async function initSession(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info(`promise: enter initSession`);
  try {
    await huks.initSession(keyAlias, huksOptions)
      .then((data) => {
        handle = data.handle;
        console.info(`promise: initSession success`);
      }).catch((error: BusinessError) => {
        console.error(`promise: initSession failed, errCode: ${error.code}, errMsg: ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: initSession input arg invalid`);
  }
}

async function updateSession(handle: number, huksOptions: huks.HuksOptions) {
  console.info(`promise: enter updateSession`);
  try {
    await huks.updateSession(handle, huksOptions)
      .then((data) => {
        let outData = data.outData as Uint8Array;
        console.info(`promise: updateSession success, data = ${Uint8ArrayToString(outData)}`);
      }).catch((error: BusinessError) => {
        console.error(`promise: updateSession failed, errCode: ${error.code}, errMsg: ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: updateSession input arg invalid`);
  }
}

async function finishSession(handle: number, huksOptions: huks.HuksOptions) {
  console.info(`promise: enter finishSession`);
  try {
    await huks.finishSession(handle, huksOptions)
      .then((data) => {
        let outData = data.outData as Uint8Array;
        console.info(`promise: finishSession success, data = ${Uint8ArrayToString(outData)}`);
      }).catch((error: BusinessError) => {
        console.error(`promise: finishSession failed, errCode: ${error.code}, errMsg: ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: finishSession input arg invalid`);
  }
}

async function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info(`promise: enter deleteKeyItem`);
  try {
    await huks.deleteKeyItem(keyAlias, huksOptions)
      .then(() => {
        console.info(`promise: deleteKeyItem success`);
      }).catch((error: BusinessError) => {
        console.error(`promise: deleteKeyItem failed, errCode: ${error.code}, errMsg: ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: deleteKeyItem input arg invalid`);
  }
}
async function testDerive() {
  /* 生成密钥 */
  await generateKeyItem(srcKeyAlias, huksOptions);
  /* 进行派生操作 */
  await initSession(srcKeyAlias, initOptions);
  await updateSession(handle, initOptions);
  await finishSession(handle, finishOptions);
  await deleteKeyItem(srcKeyAlias, huksOptions);
}
```
