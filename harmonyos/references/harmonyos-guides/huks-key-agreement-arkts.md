---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-agreement-arkts
title: 密钥协商(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 密钥协商 > 密钥协商(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8dd85e9d7bcd8d61a957fd6f6fd4e733c4651c823819717de7ba21a7d983cc70
---

以X25519，DH和ECDH三个协商密钥类型为例，在密钥由HUKS管理的情况下，完成密钥协商。具体的场景介绍及支持的算法规格，请参考[密钥协商支持的算法](huks-key-agreement-overview.md#支持的算法)。

## 开发步骤

**生成密钥**

设备A、设备B各自生成一个非对称密钥，具体请参考[密钥生成](huks-key-generation-overview.md)或[密钥导入](huks-key-import-overview.md)。

密钥生成时，可指定参数[HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG](../harmonyos-references/js-apis-huks.md#hukstag)（可选），用于标识基于该密钥协商出的密钥是否由HUKS管理。

* 当TAG设置为[HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS](../harmonyos-references/js-apis-huks.md#hukskeystoragetype)时，表示基于该密钥协商出的密钥，由HUKS管理，可保证协商密钥全生命周期不出安全环境。
* 当TAG设置为[HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED](../harmonyos-references/js-apis-huks.md#hukskeystoragetype)时，表示基于该密钥协商出的密钥，返回给调用方管理，由业务自行保证密钥安全。
* 若业务未设置TAG的具体值，表示基于该密钥协商出的密钥，可由HUKS管理，也可返回给调用方管理，业务可在后续协商时再选择使用何种方式保护密钥。

**导出密钥**

设备A、B导出非对称密钥对的公钥材料，具体请参考[密钥导出](huks-export-key-arkts.md)。

**密钥协商**

设备A、B分别基于本端私钥和对端设备的公钥，协商出共享密钥。

密钥协商时，可指定参数HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG（可选），用于标识协商得到的密钥是否由HUKS管理。

| 生成 | 协商 | 规格 |
| --- | --- | --- |
| HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | 密钥由HUKS管理 |
| HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | 密钥返回给调用方管理 |
| 未指定TAG具体值 | HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | 密钥由HUKS管理 |
| 未指定TAG具体值 | HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | 密钥返回给调用方管理 |
| 未指定TAG具体值 | 未指定TAG具体值 | 密钥返回给调用方管理 |

注：协商时指定的TAG值，不可与生成时指定的TAG值冲突。表格中仅列举有效的指定方式。

**删除密钥**

当密钥废弃不用时，设备A、B均需要删除密钥，具体请参考[密钥删除](huks-delete-key-arkts.md)。

## 开发案例

下面分别以X25519、DH和ECDH密钥为例，进行协商。

### X25519非对称密钥协商用例

准备X25519密钥协商材料：

```typescript
/*
 * 以下以X25519密钥的Promise操作使用为例
 */
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

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

/*
 * 确定密钥别名和封装密钥属性参数集
 */
let srcKeyAliasFirst = 'AgreeX25519KeyFirstAlias';
let srcKeyAliasSecond = 'AgreeX25519KeySecondAlias';
let agreeX25519InData = 'AgreeX25519TestIndata';
let finishOutData: Uint8Array;
let handle: number;
let exportKey: Uint8Array;
let exportKeyFirst: Uint8Array;
let exportKeySecond: Uint8Array;
/* 集成生成密钥参数集 */
let properties: huks.HuksParam[] = [{
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
}
];
let huksOptions: huks.HuksOptions = {
  properties: properties,
  inData: new Uint8Array([])
}
/* 集成第一个协商参数集 */
const finishProperties: huks.HuksParam[] = [{
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
}
];
let finishOptionsFirst: huks.HuksOptions = {
  properties: [
    ...finishProperties, {
    tag: huks.HuksTag.HUKS_TAG_KEY_ALIAS,
    value: stringToUint8Array(srcKeyAliasFirst + 'final'),
  }],
  inData: stringToUint8Array(agreeX25519InData)
}
/* 集成第二个协商参数集 */
let finishOptionsSecond: huks.HuksOptions = {
  properties: [
    ...finishProperties, {
    tag: huks.HuksTag.HUKS_TAG_KEY_ALIAS,
    value: stringToUint8Array(srcKeyAliasSecond + 'final'),
  }],
  inData: stringToUint8Array(agreeX25519InData)
}
```

执行密钥协商：

```typescript
/* 生成密钥 */
async function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter generateKeyItem');
  try {
    await huks.generateKeyItem(keyAlias, huksOptions)
      .then(() => {
        console.info(`promise: generateKeyItem success`);
      }).catch((error: BusinessError) => {
        console.error(`promise: generateKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: generateKeyItem input arg invalid`);
  }
}

/* 初始化密钥会话接口，并获取一个句柄（必选）和挑战值（可选） */
async function initSession(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter initSession');
  try {
    await huks.initSession(keyAlias, huksOptions)
      .then((data) => {
        handle = data.handle;
        console.info(`promise: initSession success`);
      }).catch((error: BusinessError) => {
        console.error(`promise: initSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: initSession input arg invalid`);
  }
}

/* 分段添加密钥操作的数据并进行相应的密钥操作，输出处理数据 */
async function updateSession(handle: number, huksOptions: huks.HuksOptions) {
  console.info('promise: enter updateSession');
  try {
    await huks.updateSession(handle, huksOptions)
      .then((data) => {
        console.info(`promise: updateSession success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      }).catch((error: BusinessError) => {
        console.error(`promise: updateSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: updateSession input arg invalid`);
  }
}

/* 结束密钥会话并进行相应的密钥操作，输出处理数据 */
async function finishSession(handle: number, huksOptions: huks.HuksOptions) {
  console.info('promise: enter finishSession');
  try {
    await huks.finishSession(handle, huksOptions)
      .then((data) => {
        finishOutData = data.outData as Uint8Array;
        console.info(`promise: finishSession success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      }).catch((error: BusinessError) => {
        console.error(`promise: finishSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: finishSession input arg invalid`);
  }
}

/* 导出密钥 */
async function exportKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter exportKeyItem');
  try {
    await huks.exportKeyItem(keyAlias, huksOptions)
      .then((data) => {
        exportKey = data.outData as Uint8Array;
        console.info(`promise: exportKey success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      }).catch((error: BusinessError) => {
        console.error(`promise: exportKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: exportKeyItem input arg invalid`);
  }
}

/* 删除密钥操作 */
async function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter deleteKeyItem');
  try {
    await huks.deleteKeyItem(keyAlias, huksOptions)
      .then(() => {
        console.info(`promise: deleteKeyItem success`);
      }).catch((error: BusinessError) => {
        console.error(`promise: deleteKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: deleteKeyItem input arg invalid`);
  }
}

async function testAgree() {
  /* 1.确定密钥别名并集成要参数集。A设备：srcKeyAliasFirst；B设备：srcKeyAliasSecond */
  /* 2.设备A生成密钥 */
  await generateKeyItem(srcKeyAliasFirst, huksOptions);
  /* 3.设备B生成密钥 */
  await generateKeyItem(srcKeyAliasSecond, huksOptions);
  /* 4.设备A、B导出非对称密钥的公钥 */
  await exportKeyItem(srcKeyAliasFirst, huksOptions);
  exportKeyFirst = exportKey;
  await exportKeyItem(srcKeyAliasSecond, huksOptions);
  exportKeySecond = exportKey;
  /* 5.对第一个密钥进行协商（三段式） */
  await initSession(srcKeyAliasFirst, huksOptions);
  huksOptions.inData = exportKeySecond;
  await updateSession(handle, huksOptions);
  await finishSession(handle, finishOptionsFirst);
  /* 6.对第二个密钥进行协商（三段式） */
  await initSession(srcKeyAliasSecond, huksOptions);
  huksOptions.inData = exportKeyFirst;
  await updateSession(handle, huksOptions);
  await finishSession(handle, finishOptionsSecond);
  /* 7.设备A、B删除密钥 */
  await deleteKeyItem(srcKeyAliasFirst, huksOptions);
  await deleteKeyItem(srcKeyAliasSecond, huksOptions);
}
```

### DH密钥协商用例

```typescript
/*
 * 下面以DH密钥的Promise操作使用为例
 */
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

function stringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function uint8ArrayToBigInt(arr: Uint8Array): bigint {
  let i = 0;
  const byteMax: bigint = BigInt('0x100');
  let result: bigint = BigInt('0');
  while (i < arr.length) {
    result = result * byteMax;
    result = result + BigInt(arr[i]);
    i += 1;
  }
  return result;
}

function uint8ArrayToString(fileData: Uint8Array) {
  let dataString = '';
  for (let i = 0; i < fileData.length; i++) {
    dataString += String.fromCharCode(fileData[i]);
  }
  return dataString;
}

let handle: number;
let finishOutData: Uint8Array;
let exportKey: Uint8Array;
const dhAgree: huks.HuksParam[] = [{
  tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
  value: huks.HuksKeyAlg.HUKS_ALG_DH,
}, {
  tag: huks.HuksTag.HUKS_TAG_PURPOSE,
  value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_AGREE,
}];
const dh2048Agree: huks.HuksParam[] = [
  ...dhAgree, {
  tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
  value: huks.HuksKeySize.HUKS_DH_KEY_SIZE_2048,
}];
const dhGenOptions: huks.HuksOptions = {
  properties: dh2048Agree,
  inData: new Uint8Array([])
};
const emptyOptions: huks.HuksOptions = {
  properties: [],
  inData: new Uint8Array([])
};

/* 生成密钥 */
async function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter generateKeyItem');
  try {
    await huks.generateKeyItem(keyAlias, huksOptions)
      .then(() => {
        console.info(`promise: generateKeyItem success`);
      }).catch((error: BusinessError) => {
        console.error(`promise: generateKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: generateKeyItem input arg invalid`);
  }
}

/* 初始化密钥会话接口，并获取一个句柄（必选）和挑战值（可选） */
async function initSession(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter initSession');
  try {
    await huks.initSession(keyAlias, huksOptions)
      .then((data) => {
        handle = data.handle;
        console.info(`promise: initSession success`);
      }).catch((error: BusinessError) => {
        console.error(`promise: initSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: initSession input arg invalid`);
  }
}

/* 分段添加密钥操作的数据并进行相应的密钥操作，输出处理数据 */
async function updateSession(handle: number, huksOptions: huks.HuksOptions) {
  console.info('promise: enter updateSession');
  try {
    await huks.updateSession(handle, huksOptions)
      .then((data) => {
        console.info(`promise: updateSession success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      }).catch((error: BusinessError) => {
        console.error(`promise: updateSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: updateSession input arg invalid`);
  }
}

/* 查询密钥是否存在 */
async function isKeyItemExist(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter isKeyItemExist');
  try {
    await huks.isKeyItemExist(keyAlias, huksOptions)
      .then((data) => {
        console.info(`isKeyItemExist success`);
      }).catch((error: BusinessError) => {
        console.error(`isKeyItemExist failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`isKeyItemExist input arg invalid`);
  }
}

/* 结束密钥会话并进行相应的密钥操作，输出处理数据 */
async function finishSession(handle: number, huksOptions: huks.HuksOptions) {
  console.info('promise: enter finishSession');
  try {
    await huks.finishSession(handle, huksOptions)
      .then((data) => {
        finishOutData = data.outData as Uint8Array;
        console.info(`promise: finishSession success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      }).catch((error: BusinessError) => {
        console.error(`promise: finishSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: finishSession input arg invalid`);
  }
}

/* 导出密钥 */
async function exportKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter exportKeyItem');
  try {
    await huks.exportKeyItem(keyAlias, huksOptions)
      .then((data) => {
        exportKey = data.outData as Uint8Array;
        console.info(`promise: exportKey success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      }).catch((error: BusinessError) => {
        console.error(`promise: exportKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: exportKeyItem input arg invalid`);
  }
}

/* 删除密钥操作 */
async function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter deleteKeyItem');
  try {
    await huks.deleteKeyItem(keyAlias, huksOptions)
      .then(() => {
        console.info(`promise: deleteKeyItem success`);
      }).catch((error: BusinessError) => {
        console.error(`promise: deleteKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: deleteKeyItem input arg invalid`);
  }
}

async function huksDhAgreeExportKey(keyAlias: string,
  peerPubKey: Uint8Array) {
  await initSession(keyAlias, dhGenOptions);
  const dhAgreeUpdateBobPubKey: huks.HuksOptions = {
    properties: [
      ...dh2048Agree, {
      tag: huks.HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
      value: huks.HuksKeyStorageType.HUKS_STORAGE_KEY_EXPORT_ALLOWED,
    }],
    inData: peerPubKey
  };
  await updateSession(handle, dhAgreeUpdateBobPubKey);
  await finishSession(handle, emptyOptions);
}

async function huksDhAgreeInHuks(keyAlias: string, peerPubKey: Uint8Array,
  aliasAgreedKey: string) {
  const onlyUsedInHuks: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_KEY_STORAGE_FLAG,
    value: huks.HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
  }, {
    tag: huks.HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
    value: huks.HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
  }];
  const dhAgreeInit: huks.HuksOptions = {
    properties: [
      ...dhAgree,
      { tag: huks.HuksTag.HUKS_TAG_KEY_SIZE, value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256, },
      ...onlyUsedInHuks],
    inData: new Uint8Array([])
  };
  const dhAgreeFinishParams: huks.HuksParam[] = [
    ...onlyUsedInHuks,
    { tag: huks.HuksTag.HUKS_TAG_IS_KEY_ALIAS, value: true },
    { tag: huks.HuksTag.HUKS_TAG_ALGORITHM, value: huks.HuksKeyAlg.HUKS_ALG_AES },
    { tag: huks.HuksTag.HUKS_TAG_KEY_SIZE, value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256 },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
    }
  ];

  await initSession(keyAlias, dhAgreeInit);
  const dhAgreeUpdatePubKey: huks.HuksOptions = {
    properties: [...dhAgree, ...onlyUsedInHuks],
    inData: peerPubKey
  };
  await updateSession(handle, dhAgreeUpdatePubKey);
  const dhAgreeAliceFinish: huks.HuksOptions = {
    properties: [...dhAgreeFinishParams, {
      tag: huks.HuksTag.HUKS_TAG_KEY_ALIAS, value: stringToUint8Array(aliasAgreedKey)
    }], inData: new Uint8Array([])
  };
  await finishSession(handle, dhAgreeAliceFinish);
}

async function huksDhAgreeInHuksTest(
  aliasA: string, aliasB: string,
  pubKeyA: Uint8Array, pubKeyB: Uint8Array,
  aliasAgreedKeyFromA: string, aliasAgreedKeyFromB: string) {

  await huksDhAgreeInHuks(aliasA, pubKeyB, aliasAgreedKeyFromA);
  const aliceAgreedExist = await isKeyItemExist(aliasAgreedKeyFromA, emptyOptions);
  console.info(`ok! aliceAgreedExist in huks is ${aliceAgreedExist}`);

  await huksDhAgreeInHuks(aliasB, pubKeyA, aliasAgreedKeyFromB);
  const bobAgreedExist = await isKeyItemExist(aliasAgreedKeyFromB, emptyOptions);
  console.info(`ok! bobAgreedExist in huks is ${bobAgreedExist}`);

  await deleteKeyItem(aliasAgreedKeyFromA, emptyOptions);
  await deleteKeyItem(aliasAgreedKeyFromB, emptyOptions);
}

async function huksDhAgreeTest() {
  const aliasAlice = 'alice';
  const aliasBob = 'bob';

  /* 调用generateKeyItem生成别名为alice与bob的两个密钥 */
  await generateKeyItem(aliasAlice, dhGenOptions);
  await generateKeyItem(aliasBob, dhGenOptions);

  /* 导出非对称密钥alice与bob的公钥 */
  await exportKeyItem(aliasAlice, emptyOptions);
  const pubKeyAlice = exportKey;
  await exportKeyItem(aliasBob, emptyOptions);
  const pubKeyBob = exportKey;

  /* 开始协商，协商生成的密钥返回给业务管理 */
  await huksDhAgreeExportKey(aliasAlice, pubKeyBob);
  await huksDhAgreeExportKey(aliasBob, pubKeyAlice);

  /* 开始协商，协商生成的密钥由HUKS管理 */
  await huksDhAgreeInHuksTest(aliasAlice, aliasBob, pubKeyAlice, pubKeyBob, 'agreedKeyFromAlice', 'agreedKeyFromBob');
  /* 设备A、B删除密钥 */
  await deleteKeyItem(aliasAlice, emptyOptions);
  await deleteKeyItem(aliasBob, emptyOptions);
}
```

### ECDH密钥协商用例

准备ECDH密钥协商材料：

```typescript
/*
 * 以下以ECDH密钥的Promise操作使用为例
 */
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

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

/*
 * 确定密钥别名和封装密钥属性参数集
 */
let srcKeyAliasFirst = 'AgreeECDHKeyFirstAlias';
let srcKeyAliasSecond = 'AgreeECDHKeySecondAlias';
let agreeECDHInData = 'AgreeECDHTestIndata';
let finishOutData: Uint8Array;
let handle: number;
let exportKey: Uint8Array;
let exportKeyFirst: Uint8Array;
let exportKeySecond: Uint8Array;
/* 集成生成密钥参数集 */
let genProperties: huks.HuksParam[] = [{
  tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
  value: huks.HuksKeyAlg.HUKS_ALG_ECC,
}, {
  tag: huks.HuksTag.HUKS_TAG_PURPOSE,
  value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_AGREE,
}, {
  tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
  value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256,
}, {
  tag: huks.HuksTag.HUKS_TAG_DIGEST,
  value: huks.HuksKeyDigest.HUKS_DIGEST_NONE,
}, {
  tag: huks.HuksTag.HUKS_TAG_PADDING,
  value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
}, {
  tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
  value: huks.HuksCipherMode.HUKS_MODE_CBC,
}
]
let genHuksOptions: huks.HuksOptions = {
  properties: genProperties,
  inData: new Uint8Array([])
}

let properties: huks.HuksParam[] = [{
  tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
  value: huks.HuksKeyAlg.HUKS_ALG_ECDH,
}, {
  tag: huks.HuksTag.HUKS_TAG_PURPOSE,
  value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_AGREE,
}, {
  tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
  value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256,
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
}
]
let huksOptions: huks.HuksOptions = {
  properties: properties,
  inData: new Uint8Array([])
}
/* 集成第一个协商参数集 */
const finishProperties: huks.HuksParam[] = [{
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
  value: huks.HuksCipherMode.HUKS_MODE_CBC,
}
];
let finishOptionsFirst: huks.HuksOptions = {
  properties: [
    ...finishProperties, {
    tag: huks.HuksTag.HUKS_TAG_KEY_ALIAS,
    value: stringToUint8Array(srcKeyAliasFirst + 'final'),
  }],
  inData: stringToUint8Array(agreeECDHInData)
}
/* 集成第二个协商参数集 */
let finishOptionsSecond: huks.HuksOptions = {
  properties: [
    ...finishProperties, {
    tag: huks.HuksTag.HUKS_TAG_KEY_ALIAS,
    value: stringToUint8Array(srcKeyAliasSecond + 'final'),
  }],
  inData: stringToUint8Array(agreeECDHInData)
}
```

执行密钥协商：

```typescript
/* 生成密钥 */
async function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter generateKeyItem');
  try {
    await huks.generateKeyItem(keyAlias, huksOptions)
      .then(() => {
        console.info(`promise: generateKeyItem success`);
      }).catch((error: BusinessError) => {
        console.error(`promise: generateKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: generateKeyItem input arg invalid`);
  }
}

/* 初始化密钥会话接口，并获取一个句柄（必选）和挑战值（可选） */
async function initSession(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter initSession');
  try {
    await huks.initSession(keyAlias, huksOptions)
      .then((data) => {
        handle = data.handle;
        console.info(`promise: initSession success`);
      }).catch((error: BusinessError) => {
        console.error(`promise: initSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: initSession input arg invalid`);
  }
}

/* 分段添加密钥操作的数据并进行相应的密钥操作，输出处理数据 */
async function updateSession(handle: number, huksOptions: huks.HuksOptions) {
  console.info('promise: enter updateSession');
  try {
    await huks.updateSession(handle, huksOptions)
      .then((data) => {
        console.info(`promise: updateSession success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      }).catch((error: BusinessError) => {
        console.error(`promise: updateSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: updateSession input arg invalid`);
  }
}

/* 结束密钥会话并进行相应的密钥操作，输出处理数据 */
async function finishSession(handle: number, huksOptions: huks.HuksOptions) {
  console.info('promise: enter finishSession');
  try {
    await huks.finishSession(handle, huksOptions)
      .then((data) => {
        finishOutData = data.outData as Uint8Array;
        console.info(`promise: finishSession success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      }).catch((error: BusinessError) => {
        console.error(`promise: finishSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: finishSession input arg invalid`);
  }
}

/* 导出密钥 */
async function exportKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter exportKeyItem');
  try {
    await huks.exportKeyItem(keyAlias, huksOptions)
      .then((data) => {
        exportKey = data.outData as Uint8Array;
        console.info(`promise: exportKey success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      }).catch((error: BusinessError) => {
        console.error(`promise: exportKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: exportKeyItem input arg invalid`);
  }
}

/* 删除密钥操作 */
async function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter deleteKeyItem');
  try {
    await huks.deleteKeyItem(keyAlias, huksOptions)
      .then(() => {
        console.info(`promise: deleteKeyItem success`);
      }).catch((error: BusinessError) => {
        console.error(`promise: deleteKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: deleteKeyItem input arg invalid`);
  }
}

async function testAgree() {
  /* 1.确定密钥别名并集成要参数集。A设备：srcKeyAliasFirst；B设备：srcKeyAliasSecond */
  /* 2.设备A生成密钥 */
  await generateKeyItem(srcKeyAliasFirst, genHuksOptions);
  /* 3.设备B生成密钥 */
  await generateKeyItem(srcKeyAliasSecond, genHuksOptions);
  /* 4.设备A、B导出非对称密钥的公钥 */
  await exportKeyItem(srcKeyAliasFirst, genHuksOptions);
  exportKeyFirst = exportKey;
  await exportKeyItem(srcKeyAliasSecond, genHuksOptions);
  exportKeySecond = exportKey;
  /* 5.对第一个密钥进行协商（三段式） */
  await initSession(srcKeyAliasFirst, huksOptions);
  huksOptions.inData = exportKeySecond;
  await updateSession(handle, huksOptions);
  await finishSession(handle, finishOptionsFirst);
  /* 6.对第二个密钥进行协商（三段式） */
  await initSession(srcKeyAliasSecond, huksOptions);
  huksOptions.inData = exportKeyFirst;
  await updateSession(handle, huksOptions);
  await finishSession(handle, finishOptionsSecond);
  /* 7.设备A、B删除密钥 */
  await deleteKeyItem(srcKeyAliasFirst, huksOptions);
  await deleteKeyItem(srcKeyAliasSecond, huksOptions);
}
```
