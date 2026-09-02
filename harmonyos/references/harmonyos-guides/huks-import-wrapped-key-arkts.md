---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-import-wrapped-key-arkts
title: 安全导入密钥(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥生成/导入 > 密钥导入 > 安全导入密钥(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:03+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dcf5b13422a36b0c1a8f5b7d28844e32f44722776bf7c04260944fe8bed7f5e7
---

以安全导入ECDH密钥对为例，涉及业务侧加密密钥的[密钥生成](huks-key-generation-overview.md)、[协商](huks-key-agreement-overview.md)等操作不在本示例中体现。

具体的场景介绍及支持的算法规格，请参考[密钥导入支持的算法](huks-key-import-overview.md#支持的算法)。

## 开发步骤

1. 设备A（导入设备）将待导入密钥转换成[HUKS密钥材料格式](huks-concepts.md#密钥材料格式)To\_Import\_Key（仅针对非对称密钥，若待导入密钥是对称密钥则可省略此步骤）。
2. 设备B（被导入设备）生成一个安全导入用途的非对称密钥对Wrapping\_Key（公钥Wrapping\_Pk，私钥Wrapping\_Sk），导出Wrapping\_Key的公钥材料Wrapping\_Pk发送给设备A。
3. 设备A使用和设备B同样的算法，生成一个用于协商的非对称密钥对Caller\_Key（公钥Caller\_Pk，私钥Caller\_Sk），导出Caller\_Key的公钥材料Caller\_Pk并保存。
4. 设备A生成一个对称密钥Caller\_Kek，该密钥用于加密To\_Import\_Key生成To\_Import\_Key\_Enc。
5. 设备A基于Caller\_Key的私钥Caller\_Sk和设备B Wrapping\_Key的公钥Wrapping\_Pk，协商出Shared\_Key，使用Shared\_Key加密Caller\_Kek，生成Caller\_Kek\_Enc。
6. 设备A封装Caller\_Pk、Caller\_Kek\_Enc、To\_Import\_Key\_Enc等安全导入的密钥材料并发送给设备B，安全导入密钥材料格式见[安全导入密钥材料格式](huks-key-import-overview.md#安全导入密钥材料格式)。
7. 设备B导入封装的加密密钥材料。
8. 设备A、B删除用于安全导入的密钥。

## 开发案例

构造用于ECDH密钥协商、AES-GCM加密和包装密钥导入的参数集

```typescript
import { huks } from '@kit.UniversalKeystoreKit';

let IV = '0000000000000000';
let AAD = 'abababababababab';
let NONCE = 'hahahahahaha';
let TAG_SIZE = 16;
let FILED_LENGTH = 4;
let importedAes192PlainKey = 'The aes192 key to import';
let callerAes256Kek = 'The is kek to encrypt aes192 key';
let callerKeyAlias = 'test_caller_key_ecdh_aes192';
let callerKekAliasAes256 = 'test_caller_kek_ecdh_aes256';
let callerAgreeKeyAliasAes256 = 'test_caller_agree_key_ecdh_aes256';
let importedKeyAliasAes192 = 'test_import_key_ecdh_aes192';
let huksPubKey: Uint8Array;
let callerSelfPublicKey: Uint8Array;
let outSharedKey: Uint8Array;
let outPlainKeyEncData: Uint8Array;
let outKekEncData: Uint8Array;
let outKekEncTag: Uint8Array;
let outAgreeKeyEncTag: Uint8Array;
let mask = [0x000000FF, 0x0000FF00, 0x00FF0000, 0xFF000000];

function subUint8ArrayOf(arrayBuf: Uint8Array, start: number, end: number) {
  let arr: number[] = [];
  for (let i = start; i < end && i < arrayBuf.length; ++i) {
    arr.push(arrayBuf[i]);
  }
  return new Uint8Array(arr);
}

function stringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function assignLength(length: number, arrayBuf: Uint8Array, startIndex: number) {
  let index = startIndex;
  for (let i = 0; i < 4; i++) {
    arrayBuf[index++] = (length & mask[i]) >> (i * 8);
  }
  return 4;
}

function assignData(data: Uint8Array, arrayBuf: Uint8Array, startIndex: number) {
  let index = startIndex;
  for (let i = 0; i < data.length; i++) {
    arrayBuf[index++] = data[i];
  }
  return data.length;
}

let genWrappingKeyParams: huks.HuksOptions = {
  properties: [
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_ECC
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_UNWRAP
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_CURVE25519_KEY_SIZE_256
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PADDING,
      value: huks.HuksKeyPadding.HUKS_PADDING_NONE
    }
  ]
}

let genCallerEcdhParams: huks.HuksOptions = {
  properties: [
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_ECC
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_AGREE
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_CURVE25519_KEY_SIZE_256
    }
  ]
}

let importParamsCallerKek: huks.HuksOptions = {
  properties: [
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_AES
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PADDING,
      value: huks.HuksKeyPadding.HUKS_PADDING_NONE
    },
    {
      tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
      value: huks.HuksCipherMode.HUKS_MODE_GCM
    },
    {
      tag: huks.HuksTag.HUKS_TAG_DIGEST,
      value: huks.HuksKeyDigest.HUKS_DIGEST_NONE
    },
    {
      tag: huks.HuksTag.HUKS_TAG_IV,
      value: stringToUint8Array(IV)
    }
  ],
  inData: stringToUint8Array(callerAes256Kek)
}
```

构造用于生成ECC解包装密钥、ECDH协商密钥和导入AES-GCM密钥加密密钥的参数集

```typescript
let importParamsAgreeKey: huks.HuksOptions = {
  properties: [
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_AES
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PADDING,
      value: huks.HuksKeyPadding.HUKS_PADDING_NONE
    },
    {
      tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
      value: huks.HuksCipherMode.HUKS_MODE_GCM
    },
    {
      tag: huks.HuksTag.HUKS_TAG_DIGEST,
      value: huks.HuksKeyDigest.HUKS_DIGEST_NONE
    },
    {
      tag: huks.HuksTag.HUKS_TAG_IV,
      value: stringToUint8Array(IV)
    }
  ],
}

let callerAgreeParams: huks.HuksOptions = {
  properties: [
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_ECDH
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_AGREE
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_CURVE25519_KEY_SIZE_256
    }
  ]
}

let encryptKeyCommonParams: huks.HuksOptions = {
  properties: [
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_AES
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PADDING,
      value: huks.HuksKeyPadding.HUKS_PADDING_NONE
    },
    {
      tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
      value: huks.HuksCipherMode.HUKS_MODE_GCM
    },
    {
      tag: huks.HuksTag.HUKS_TAG_NONCE,
      value: stringToUint8Array(NONCE)
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ASSOCIATED_DATA,
      value: stringToUint8Array(AAD)
    }
  ],
}

let importWrappedAes192Params: huks.HuksOptions = {
  properties: [
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_AES
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
      huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_192
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PADDING,
      value: huks.HuksKeyPadding.HUKS_PADDING_NONE
    },
    {
      tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
      value: huks.HuksCipherMode.HUKS_MODE_CBC
    },
    {
      tag: huks.HuksTag.HUKS_TAG_DIGEST,
      value: huks.HuksKeyDigest.HUKS_DIGEST_NONE
    },
    {
      tag: huks.HuksTag.HUKS_TAG_UNWRAP_ALGORITHM_SUITE,
      value: huks.HuksUnwrapSuite.HUKS_UNWRAP_SUITE_ECDH_AES_256_GCM_NOPADDING
    },
    {
      tag: huks.HuksTag.HUKS_TAG_IV,
      value: stringToUint8Array(IV)
    }
  ]
}
```

生成密钥、导入密钥、删除密钥、导入包装密钥以及会话操作

```typescript
async function publicGenerateItemFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info(`enter promise generateKeyItem`);
  try {
    await huks.generateKeyItem(keyAlias, huksOptions)
      .then(data => {
        console.info(`promise: generateKeyItem success, data = ${JSON.stringify(data)}`);
      })
      .catch((err: Error) => {
        console.error(`promise: generateKeyItem failed, ${JSON.stringify(err)}`);
        throw (err as Error);
      })
  } catch (err) {
    console.error(`promise: generateKeyItem invalid, ${JSON.stringify(err)}`);
    throw (err as Error);
  }
}

async function publicImportKeyItemFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info(`enter promise importKeyItem`);
  try {
    await huks.importKeyItem(keyAlias, huksOptions)
      .then(data => {
        console.info(`promise: importKeyItem success, data = ${JSON.stringify(data)}`);
      }).catch((err: Error) => {
        console.error(`promise: importKeyItem failed, ${JSON.stringify(err)}`);
        throw (err as Error);
      })
  } catch (err) {
    console.error(`promise: importKeyItem input arg invalid, ${JSON.stringify(err)}`);
    throw (err as Error);
  }
}

async function publicDeleteKeyItemFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info(`enter promise deleteKeyItem`);
  try {
    await huks.deleteKeyItem(keyAlias, huksOptions)
      .then(data => {
        console.info(`promise: deleteKeyItem key success, data = ${JSON.stringify(data)}`);
      })
      .catch((err: Error) => {
        console.error(`promise: deleteKeyItem failed, ${JSON.stringify(err)}`);
        throw (err as Error);
      })
  } catch (err) {
    console.error(`promise: deleteKeyItem input arg invalid, ${JSON.stringify(err)}`);
    throw (err as Error);
  }
}

function importWrappedKeyItem(keyAlias: string, wrappingKeyAlias: string, huksOptions: huks.HuksOptions) {
  return new Promise<void>((resolve, reject) => {
    try {
      huks.importWrappedKeyItem(keyAlias, wrappingKeyAlias, huksOptions, (error, data) => {
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

async function publicImportWrappedKeyFunc(keyAlias: string, wrappingKeyAlias: string, huksOptions: huks.HuksOptions) {
  console.info(`enter promise importWrappedKeyItem`);
  for (let i = 0; i < huksOptions.inData!.length; i++) {
    console.error(`${i}: ${huksOptions.inData![i]}`);
  }
  try {
    await importWrappedKeyItem(keyAlias, wrappingKeyAlias, huksOptions)
      .then((data) => {
        console.info(`promise: importWrappedKeyItem success, data = ${JSON.stringify(data)}`);
      })
      .catch((error: Error) => {
        console.error(`promise: importWrappedKeyItem failed, ${JSON.stringify(error)}`);
        throw (error as Error);
      });
  } catch (error) {
    console.error(`promise: importWrappedKeyItem input arg invalid, ${JSON.stringify(error)}`);
    throw (error as Error);
  }
}

async function publicImportWrappedKeyPromise(keyAlias: string, wrappingKeyAlias: string,
  huksOptions: huks.HuksOptions) {
  console.info(`enter promise importWrappedKeyItem`);
  try {
    await huks.importWrappedKeyItem(keyAlias, wrappingKeyAlias, huksOptions)
      .then((data) => {
        console.info(`promise: importWrappedKeyItem success, data = ${JSON.stringify(data)}`);
      })
      .catch((error: Error) => {
        console.error(`promise: importWrappedKeyItem failed, ${JSON.stringify(error)}`);
        throw (error as Error);
      });
  } catch (error) {
    console.error(`promise: importWrappedKeyItem input arg invalid, ${JSON.stringify(error)}`);
    throw (error as Error);
  }
}

async function publicInitFunc(srcKeyAlias: string, huksOptions: huks.HuksOptions) {
  let handle: number = 0;
  console.info(`enter promise doInit`);
  try {
    await huks.initSession(srcKeyAlias, huksOptions)
      .then((data) => {
        console.info(`promise: doInit success, data = ${JSON.stringify(data)}`);
        handle = data.handle;
      })
      .catch((error: Error) => {
        console.error(`promise: doInit key failed, ${JSON.stringify(error)}`);
        throw (error as Error);
      });
  } catch (error) {
    console.error(`promise: doInit input arg invalid, ${JSON.stringify(error)}`);
    throw (error as Error);
  }
  return handle;
}

async function publicUpdateSessionFunction(handle: number, huksOptions: huks.HuksOptions) {
  const maxUpdateSize = 64;
  const inData = huksOptions.inData!;
  const lastInDataPosition = inData.length - 1;
  let inDataSegSize = maxUpdateSize;
  let inDataSegPosition = 0;
  let isFinished = false;
  let outData: number[] = [];

  while (inDataSegPosition <= lastInDataPosition) {
    if (inDataSegPosition + maxUpdateSize > lastInDataPosition) {
      isFinished = true;
      inDataSegSize = lastInDataPosition - inDataSegPosition + 1;
      console.info(`enter promise doUpdate`);
      break;
    }
    huksOptions.inData = new Uint8Array(
      Array.from(inData).slice(inDataSegPosition, inDataSegPosition + inDataSegSize)
    );
    console.info(`enter promise doUpdate`);
    try {
      await huks.updateSession(handle, huksOptions)
        .then((data) => {
          console.info(`promise: doUpdate success, data = ${JSON.stringify(data)}`);
          outData = outData.concat(Array.from(data.outData!));
        })
        .catch((error: Error) => {
          console.error(`promise: doUpdate failed, ${JSON.stringify(error)}`);
          throw (error as Error);
        });
    } catch (error) {
      console.error(`promise: doUpdate input arg invalid, ${JSON.stringify(error)}`);
      throw (error as Error);
    }
    if ((!isFinished) && (inDataSegPosition + maxUpdateSize > lastInDataPosition)) {
      console.error(`update size invalid isFinished = ${isFinished}`);
      console.error(`inDataSegPosition = ${inDataSegPosition}`);
      console.error(`lastInDataPosition = ${lastInDataPosition}`);
      return;
    }
    inDataSegPosition += maxUpdateSize;
  }
  return outData;
}

async function publicFinishSession(handle: number, huksOptions: huks.HuksOptions, inData: number[]) {
  let outData: number[] = [];
  console.info(`enter promise doFinish`);
  try {
    await huks.finishSession(handle, huksOptions)
      .then((data) => {
        console.info(`promise: doFinish success, data = ${JSON.stringify(data)}`);
        outData = inData.concat(Array.from(data.outData!));
      })
      .catch((error: Error) => {
        console.error(`promise: doFinish key failed, ${JSON.stringify(error)}`);
        throw (error as Error);
      });
  } catch (error) {
    console.error(`promise: doFinish input arg invalid, ${JSON.stringify(error)}`);
    throw (error as Error);
  }
  return new Uint8Array(outData);
}
```

密钥协商、加密、数据封装等核心功能函数实现

```typescript
async function cipherFunction(keyAlias: string, huksOptions: huks.HuksOptions) {
  let handle = await publicInitFunc(keyAlias, huksOptions);
  let tmpData = await publicUpdateSessionFunction(handle, huksOptions);
  let outData = await publicFinishSession(handle, huksOptions, tmpData!);
  return outData;
}

async function agreeFunction(keyAlias: string, huksOptions: huks.HuksOptions, huksPublicKey: Uint8Array) {
  let handle = await publicInitFunc(keyAlias, huksOptions);
  let outSharedKey: Uint8Array = new Uint8Array;
  huksOptions.inData = huksPublicKey;
  console.info(`enter promise doUpdate`);
  try {
    await huks.updateSession(handle, huksOptions)
      .then((data) => {
        console.error(`promise: doUpdate success, data = ${JSON.stringify(data)}`);
      })
      .catch((error: Error) => {
        console.error(`promise: doUpdate failed, ${JSON.stringify(error)}`);
        throw (error as Error);
      });
  } catch (error) {
    console.error(`promise: doUpdate input arg invalid, ${JSON.stringify(error)}`);
    throw (error as Error);
  }
  console.info(`enter promise doInit`);
  try {
    await huks.finishSession(handle, huksOptions)
      .then((data) => {
        console.info(`promise: doInit success, data = ${JSON.stringify(data)}`);
        outSharedKey = data.outData as Uint8Array;
      })
      .catch((error: Error) => {
        console.error(`promise: doInit key failed, ${JSON.stringify(error)}`);
        throw (error as Error);
      });
  } catch (error) {
    console.error(`promise: doInit input arg invalid, ${JSON.stringify(error)}`);
    throw (error as Error);
  }
  return outSharedKey;
}

async function importKekAndAgreeSharedSecret(callerKekAlias: string, importKekParams: huks.HuksOptions,
  callerKeyAlias: string, huksPublicKey: Uint8Array, agreeParams: huks.HuksOptions) {
  await publicImportKeyItemFunc(callerKekAlias, importKekParams);
  outSharedKey = await agreeFunction(callerKeyAlias, agreeParams, huksPublicKey);
  importParamsAgreeKey.inData = outSharedKey;
  await publicImportKeyItemFunc(callerAgreeKeyAliasAes256, importParamsAgreeKey);
}

async function generateAndExportPublicKey(keyAlias: string, huksOptions: huks.HuksOptions, caller: Boolean) {
  await publicGenerateItemFunc(keyAlias, huksOptions);
  try {
    await huks.exportKeyItem(keyAlias, huksOptions)
      .then((data) => {
        console.info(`promise: exportKeyItem success, data = ${JSON.stringify(data)}`);
        if (caller) {
          callerSelfPublicKey = data.outData as Uint8Array;
        } else {
          huksPubKey = data.outData as Uint8Array;
        }
      })
      .catch((error: Error) => {
        console.error(`promise: exportKeyItem failed, ${JSON.stringify(error)}`);
        throw (error as Error);
      });
  } catch (error) {
    console.error(`promise: generate pubKey failed, ${JSON.stringify(error)}`);
    throw (error as Error);
  }
}

async function encryptImportedPlainKeyAndKek(keyAlias: string) {
  encryptKeyCommonParams.inData = stringToUint8Array(keyAlias)
  let plainKeyEncData = await cipherFunction(callerKekAliasAes256, encryptKeyCommonParams);
  outKekEncTag = subUint8ArrayOf(plainKeyEncData, plainKeyEncData.length - TAG_SIZE, plainKeyEncData.length)
  outPlainKeyEncData = subUint8ArrayOf(plainKeyEncData, 0, plainKeyEncData.length - TAG_SIZE)
  encryptKeyCommonParams.inData = stringToUint8Array(callerAes256Kek)
  let kekEncData = await cipherFunction(callerAgreeKeyAliasAes256, encryptKeyCommonParams)
  outAgreeKeyEncTag = subUint8ArrayOf(kekEncData, kekEncData.length - TAG_SIZE, kekEncData.length)
  outKekEncData = subUint8ArrayOf(kekEncData, 0, kekEncData.length - TAG_SIZE)
}

async function buildWrappedDataAndImportWrappedKey(plainKey: string) {
  let plainKeySizeBuff = new Uint8Array(4);
  assignLength(plainKey.length, plainKeySizeBuff, 0);
  let wrappedData = new Uint8Array(
    FILED_LENGTH + huksPubKey.length +
      FILED_LENGTH + AAD.length +
      FILED_LENGTH + NONCE.length +
      FILED_LENGTH + TAG_SIZE +
      FILED_LENGTH + outKekEncData.length +
      FILED_LENGTH + AAD.length +
      FILED_LENGTH + NONCE.length +
      FILED_LENGTH + TAG_SIZE +
      FILED_LENGTH + plainKeySizeBuff.length +
      FILED_LENGTH + outPlainKeyEncData.length
  );
  let index = 0;
  let aadUint8Array = stringToUint8Array(AAD);
  let nonceArray = stringToUint8Array(NONCE);
  index += assignLength(callerSelfPublicKey.length, wrappedData, index); // 4
  index += assignData(callerSelfPublicKey, wrappedData, index); // 91
  index += assignLength(aadUint8Array.length, wrappedData, index); // 4
  index += assignData(aadUint8Array, wrappedData, index); // 16
  index += assignLength(nonceArray.length, wrappedData, index); // 4
  index += assignData(nonceArray, wrappedData, index); // 12
  index += assignLength(outAgreeKeyEncTag.length, wrappedData, index); // 4
  index += assignData(outAgreeKeyEncTag, wrappedData, index); // 16
  index += assignLength(outKekEncData.length, wrappedData, index); // 4
  index += assignData(outKekEncData, wrappedData, index); // 32
  index += assignLength(aadUint8Array.length, wrappedData, index); // 4
  index += assignData(aadUint8Array, wrappedData, index); // 16
  index += assignLength(nonceArray.length, wrappedData, index); // 4
  index += assignData(nonceArray, wrappedData, index); // 12
  index += assignLength(outKekEncTag.length, wrappedData, index); // 4
  index += assignData(outKekEncTag, wrappedData, index); // 16
  index += assignLength(plainKeySizeBuff.length, wrappedData, index); // 4
  index += assignData(plainKeySizeBuff, wrappedData, index); // 4
  index += assignLength(outPlainKeyEncData.length, wrappedData, index); // 4
  index += assignData(outPlainKeyEncData, wrappedData, index); // 24
  return wrappedData;
}
```

安全导入密钥的完整流程实现

```typescript
/* 模拟安全导入密钥场景，设备A为远端设备（导入设备），设备B为本端设备（被导入设备） */
async function ImportWrappedKey() {
  /**
   * 1. 设备A将待导入密钥转换成HUKS密钥材料格式To_Import_Key（仅针对非对称密钥，若待导入密钥是对称密钥则可省略此步骤），
   *   本示例使用importedAes256PlainKey（对称密钥）作为模拟
   */
  /**
   * 2. 设备B生成一个加密导入用途的、用于协商的非对称密钥对Wrapping_Key（公钥Wrapping_Pk，私钥Wrapping_Sk），
   * 导出Wrapping_Key公钥Wrapping_Pk存放在变量huksPubKey中
   */
  const srcKeyAliasWrap = 'HUKS_Basic_Capability_Import_0200';
  await generateAndExportPublicKey(srcKeyAliasWrap, genWrappingKeyParams, false);

  /**
   * 3. 设备A使用和设备B同样的算法，生成一个用于协商的非对称密钥对Caller_Key（公钥Caller_Pk，私钥Caller_Sk），
   * 导出Caller_Key公钥Caller_Pk存放在变量callerSelfPublicKey中
   */
  await generateAndExportPublicKey(callerKeyAlias, genCallerEcdhParams, true);

  /**
   * 4. 设备A生成一个对称密钥Caller_Kek，该密钥后续将用于加密To_Import_Key
   * 设备A基于Caller_Key的私钥Caller_Sk和设备B Wrapping_Key的公钥Wrapping_Pk，协商出Shared_Key
   */
  await importKekAndAgreeSharedSecret(callerKekAliasAes256, importParamsCallerKek, callerKeyAlias, huksPubKey,
    callerAgreeParams);

  /**
   * 5. 设备A使用Caller_Kek加密To_Import_Key，生成To_Import_Key_Enc
   * 设备A使用Shared_Key加密Caller_Kek，生成Caller_Kek_Enc
   */
  await encryptImportedPlainKeyAndKek(importedAes192PlainKey);

  /**
   * 6. 设备A封装Caller_Pk、To_Import_Key_Enc、Caller_Kek_Enc等安全导入的材料并发送给设备B。
   * 本示例作为变量存放在callerSelfPublicKey，PlainKeyEncData，KekEncData
   */
  let wrappedData = await buildWrappedDataAndImportWrappedKey(importedAes192PlainKey);
  importWrappedAes192Params.inData = wrappedData;

  /* 7. 设备B导入封装的加密密钥材料 */
  await publicImportWrappedKeyFunc(importedKeyAliasAes192, srcKeyAliasWrap, importWrappedAes192Params);

  /* 8. 设备A、B删除用于安全导入的密钥 */
  await publicDeleteKeyItemFunc(srcKeyAliasWrap, genWrappingKeyParams);
  await publicDeleteKeyItemFunc(callerKeyAlias, genCallerEcdhParams);
  await publicDeleteKeyItemFunc(importedKeyAliasAes192, importWrappedAes192Params);
  await publicDeleteKeyItemFunc(callerKekAliasAes256, callerAgreeParams);
}

/*
 * 确定密钥别名和封装密钥属性参数集
 */
let keyAlias = 'test_import_key_ecdh_aes192';
let isKeyExist: Boolean;
let keyProperties: huks.HuksParam[] = [{
  tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
  value: huks.HuksKeyAlg.HUKS_ALG_AES,
}];
let huksOptions: huks.HuksOptions = {
  properties: keyProperties, // 非空填充
  inData: new Uint8Array([]) // 非空填充
}

function Check() {
  try {
    huks.isKeyItemExist(keyAlias, huksOptions, (error, data) => {
      if (error) {
        console.error(`callback: isKeyItemExist failed, ${JSON.stringify(error)}`);
      } else {
        if (data !== null && data.valueOf() !== null) {
          isKeyExist = data.valueOf();
          console.info(`callback: isKeyItemExist success, isKeyExist = ${isKeyExist}`);
        }
      }
    });
  } catch (error) {
    console.error(`callback: isKeyItemExist input arg invalid, ${JSON.stringify(error)}`);
    throw (error as Error);
  }
}
```

## 调测验证

调用[huks.isKeyItemExist](../harmonyos-references/js-apis-huks.md#huksiskeyitemexist9)验证密钥是否存在，如密钥存在即表示密钥导入成功。

```ts
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from "@kit.BasicServicesKit";

/*
 * 确定密钥别名和封装密钥属性参数集
 */
let keyAlias = 'test_import_key_ecdh_aes192';
let isKeyExist: Boolean;
let keyProperties: Array<huks.HuksParam> = [{
  tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
  value: huks.HuksKeyAlg.HUKS_ALG_AES,
}];
let huksOptions: huks.HuksOptions = {
  properties: keyProperties, // 非空填充。
  inData: new Uint8Array(new Array()) // 非空填充。
}

async function isKeyItemExist(keyAlias: string, options: huks.HuksOptions): Promise<boolean> {
  console.info(`promise: enter isKeyItemExist`);
  let ret: boolean = false;
  try {
    await huks.isKeyItemExist(keyAlias, options)
      .then((data) => {
        console.info(`promise: isKeyItemExist success, data = ${data}`);
        ret = true;
      }).catch((error: BusinessError) => {
        console.error(`promise: isKeyItemExist failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: isKeyItemExist input arg invalid`);
  }
  return ret;
}

async function importWrappedKeyExistTest() {
  let retImp = await isKeyItemExist(keyAlias, huksOptions);
  if (retImp == false) {
    console.error("importWrappedKeyExistTest failed");
    return;
  }
  console.error("importWrappedKeyExistTest success");
}
```
