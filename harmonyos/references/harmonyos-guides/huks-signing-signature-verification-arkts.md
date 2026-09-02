---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-signing-signature-verification-arkts
title: 签名/验签(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 签名/验签 > 签名/验签(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:31+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:930b723dde5e9a64727c328bc80242c3a47787a41ca080a834ff1dd268f995e9
---

当前指导提供以下示例，供开发者参考完成签名、验签开发：

* 密钥算法为ECC256、摘要算法为SHA256，请见开发案例：[ECC256/SHA256](huks-signing-signature-verification-arkts.md#ecc256sha256)
* 密钥算法为SM2、摘要算法为SM3，请见开发案例：[SM2/SM3](huks-signing-signature-verification-arkts.md#sm2sm3)
* 密钥算法为SM2、摘要算法为NoDigest，请见开发案例：[SM2/NoDigest](huks-signing-signature-verification-arkts.md#sm2nodigest)
* 密钥算法为RSA、摘要算法为SHA256、填充模式为PSS，请见开发案例：[RSA/SHA256/PSS](huks-signing-signature-verification-arkts.md#rsasha256pss)
* 密钥算法为RSA、摘要算法为SHA256、填充模式为PKCS1\_V1\_5，请见开发案例：[RSA/SHA256/PKCS1\_V1\_5](huks-signing-signature-verification-arkts.md#rsasha256pkcs1_v1_5)
* 密钥算法为RSA、摘要算法为SHA384、填充模式为PSS，请见开发案例：[RSA2048/SHA384/PSS](huks-signing-signature-verification-arkts.md#rsa2048sha384pss)
* [签名/验签(ArkTS)](huks-signing-signature-verification-arkts.md#签名验签arkts)
  + [ECC/SHA256/携带认证信息的签名类型](huks-signing-signature-verification-arkts.md#eccsha256携带认证信息的签名类型)

具体的场景介绍及支持的算法规格，请参考[签名/验签支持的算法](huks-signing-signature-verification-overview.md#支持的算法)。

## 开发步骤

**生成密钥**

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集。
3. 调用[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)生成密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md)，导入已有的密钥。

**签名**

1. 获取密钥别名。
2. 指定待签名的明文数据。
3. 获取属性参数[HuksOptions](../harmonyos-references/js-apis-huks.md#huksoptions)，包括两个字段properties和inData。inData传入明文数据，properties使用[HuksParam](../harmonyos-references/js-apis-huks.md#huksparam)设置算法参数配置。
4. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
5. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，获取签名signature。

**验签**

1. 获取密钥别名。
2. 获取待验证的签名signature。
3. 获取属性参数[HuksOptions](../harmonyos-references/js-apis-huks.md#huksoptions)，包括两个字段properties和inData。inData传入签名signature，properties使用[HuksParam](../harmonyos-references/js-apis-huks.md#huksparam)设置算法参数配置。
4. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
5. 调用[updateSession](../harmonyos-references/js-apis-huks.md#huksupdatesession9)更新密钥会话。
6. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，验证签名。

**删除密钥**

当密钥废弃不用时，需要调用[deleteKeyItem](../harmonyos-references/js-apis-huks.md#huksdeletekeyitem9)删除密钥，具体请参考[密钥删除](huks-delete-key-arkts.md)。

## 开发案例

### ECC256/SHA256

```typescript
/*
 * 密钥算法为ECC256、摘要算法为SHA256
 */
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = 'test_eccKeyAlias';
let handle: number;
let plaintext = '123456';
let signature: Uint8Array;

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

function getEccGenerateProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_ECC
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN |
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }];
  return properties;
}

function getEccSignProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_ECC
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }];
  return properties;
}

function getEccVerifyProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_ECC
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }];
  return properties;
}

async function generateEccKey(keyAlias: string) {
  let genProperties = getEccGenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  }
  await huks.generateKeyItem(keyAlias, options)
    .then((data) => {
      console.info(`promise: generate ECC Key success, data = ${JSON.stringify(data)}`);
    }).catch((err: Error) => {
      console.error(`promise: generate ECC Key failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
}

async function sign(keyAlias: string, plaintext: string) {
  let signProperties = getEccSignProperties();
  let options: huks.HuksOptions = {
    properties: signProperties,
    inData: stringToUint8Array(plaintext)
  }
  await huks.initSession(keyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((err: Error) => {
      console.error(`promise: init sign failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: sign success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      signature = data.outData as Uint8Array;
    }).catch((err: Error) => {
      console.error(`promise: sign failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
}

async function verify(keyAlias: string, plaintext: string, signature: Uint8Array) {
  let verifyProperties = getEccVerifyProperties()
  let options: huks.HuksOptions = {
    properties: verifyProperties,
    inData: stringToUint8Array(plaintext)
  }
  await huks.initSession(keyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((err: Error) => {
      console.error(`promise: init verify failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
  await huks.updateSession(handle, options)
    .then((data) => {
      console.info(`promise: update verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
    }).catch((err: Error) => {
      console.error(`promise: update verify failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
  options.inData = signature;
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
    }).catch((err: Error) => {
      console.error(`promise: verify failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
}

async function deleteEccKey(keyAlias: string) {
  let emptyOptions: huks.HuksOptions = {
    properties: []
  }
  await huks.deleteKeyItem(keyAlias, emptyOptions)
    .then((data) => {
      console.info(`promise: delete data success`);
    }).catch((err: Error) => {
      console.error(`promise: delete data failed`);
      throw (err as Error);
    })
}

async function testSignVerify() {
  await generateEccKey(keyAlias);
  await sign(keyAlias, plaintext);
  await verify(keyAlias, plaintext, signature);
  await deleteEccKey(keyAlias);
}
```

### SM2/SM3

```typescript
/*
 * 密钥算法为SM2、摘要算法为SM3
 */
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = 'test_sm2KeyAlias';
let handle: number;
let plaintext = '123456';
let signature: Uint8Array;

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

function getSm2GenerateProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_SM2
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN |
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SM3
  }];
  return properties;
}

function getSm2SignProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_SM2
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SM3
  }];
  return properties;
}

function getSm2VerifyProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_SM2
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SM3
  }];
  return properties;
}

async function generateSm2Key(keyAlias: string) {
  let genProperties = getSm2GenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  }
  await huks.generateKeyItem(keyAlias, options)
    .then((data) => {
      console.info(`promise: generate Sm2 Key success, data = ${JSON.stringify(data)}`);
    }).catch((err: Error) => {
      console.error(`promise: generate Sm2 Key failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
}

async function sign(keyAlias: string, plaintext: string) {
  let signProperties = getSm2SignProperties();
  let options: huks.HuksOptions = {
    properties: signProperties,
    inData: stringToUint8Array(plaintext)
  }
  await huks.initSession(keyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((err: Error) => {
      console.error(`promise: init sign failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: sign success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      signature = data.outData as Uint8Array;
    }).catch((err: Error) => {
      console.error(`promise: sign failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
}

async function verify(keyAlias: string, plaintext: string, signature: Uint8Array) {
  let verifyProperties = getSm2VerifyProperties()
  let options: huks.HuksOptions = {
    properties: verifyProperties,
    inData: stringToUint8Array(plaintext)
  }
  await huks.initSession(keyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((err: Error) => {
      console.error(`promise: init verify failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
  await huks.updateSession(handle, options)
    .then((data) => {
      console.info(`promise: update verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
    }).catch((err: Error) => {
      console.error(`promise: update verify failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
  options.inData = signature;
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
    }).catch((err: Error) => {
      console.error(`promise: verify failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
}

async function deleteSm2Key(keyAlias: string) {
  let emptyOptions: huks.HuksOptions = {
    properties: []
  }
  await huks.deleteKeyItem(keyAlias, emptyOptions)
    .then((data) => {
      console.info(`promise: delete data success`);
    }).catch((err: Error) => {
      console.error(`promise: delete data failed`);
      throw (err as Error);
    })
}

export async function testSignVerify() {
  await generateSm2Key(keyAlias);
  await sign(keyAlias, plaintext);
  await verify(keyAlias, plaintext, signature);
  await deleteSm2Key(keyAlias);
}
```

### SM2/NoDigest

```typescript
/*
 * 密钥算法为SM2、摘要算法为NoDigest，由业务自己做SM3摘要
 */
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyAlias = 'test_sm2KeyAlias';
let handle: number;
let hash = '12345678901234567890123456789012';
let signature: Uint8Array;

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
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN |
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_NONE
  }];
  return properties;
}

function getSm2SignProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_SM2
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_SM2_KEY_SIZE_256
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_NONE
  }];
  return properties;
}

function getSm2VerifyProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_SM2
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_SM2_KEY_SIZE_256
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_NONE
  }];
  return properties;
}

async function generateSm2Key(keyAlias: string) {
  console.info(`enter generateSm2Key`);
  let genProperties = getSm2GenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  };
  await huks.generateKeyItem(keyAlias, options)
    .then(() => {
      console.info(`promise: generateSm2Key success`);
    }).catch((error: BusinessError) => {
      console.error(`promise: generateSm2Key failed, errCode : ${error.code}, errMsg : ${error.message}`);
      throw (error as Error);
    })
}

async function sign(keyAlias: string, plaintext: string) {
  let signProperties = getSm2SignProperties();
  let options: huks.HuksOptions = {
    properties: signProperties,
    inData: stringToUint8Array(plaintext)
  };
  await huks.initSession(keyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(`promise: init sign failed, error: ` + JSON.stringify(error));
      throw (error as Error);
    })
  await huks.finishSession(handle, options)
    .then((data) => {
      signature = data.outData as Uint8Array;
      console.info(`promise: sign success, data is ` + uint8ArrayToString(signature));
    }).catch((error: BusinessError) => {
      console.error(`promise: sign failed, error: ` + JSON.stringify(error));
      throw (error as Error);
    })
}

async function verify(keyAlias: string, plaintext: string, signature: Uint8Array) {
  let verifyProperties = getSm2VerifyProperties();
  let options: huks.HuksOptions = {
    properties: verifyProperties,
    inData: stringToUint8Array(plaintext)
  };
  await huks.initSession(keyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(`promise: init verify failed, error: ` + JSON.stringify(error));
      throw (error as Error);
    })
  await huks.updateSession(handle, options)
    .then((data) => {
      console.info(`promise: update verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
    }).catch((error: BusinessError) => {
      console.error(`promise: update verify failed, error: ` + JSON.stringify(error));
      throw (error as Error);
    })
  options.inData = signature;
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
    }).catch((error: BusinessError) => {
      console.error(`promise: verify failed, error: ` + JSON.stringify(error));
      throw (error as Error);
    })
}

async function deleteSm2Key(keyAlias: string) {
  console.info(`enter deleteSm2Key`);
  let emptyOptions: huks.HuksOptions = {
    properties: []
  };
  await huks.deleteKeyItem(keyAlias, emptyOptions)
    .then((data) => {
      console.info(`promise: delete data success`);
    }).catch((error: Error) => {
      console.error(`promise: delete data failed`);
      throw (error as Error);
    })
}

async function testSignVerify() {
  await generateSm2Key(keyAlias);
  await sign(keyAlias, hash);
  await verify(keyAlias, hash, signature);
  await deleteSm2Key(keyAlias);
}
```

### RSA/SHA256/PSS

```typescript
/*
 * 密钥算法为RSA，摘要算法为SHA256，填充模式为PSS
 */
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = 'test_rsaKeyAlias';
let handle: number;
let plaintext = '123456';
let signature: Uint8Array;

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
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN |
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PSS
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }];
  return properties;
}

function getRsaSignProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PSS
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
  }];
  return properties;
}

function getRsaVerifyProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PSS
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  }];
  return properties;
}

async function generateRsaKey(keyAlias: string) {
  let genProperties = getRsaGenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  };
  await huks.generateKeyItem(keyAlias, options)
    .then((data) => {
      console.info(`promise: generate RSA Key success, data = ${JSON.stringify(data)}`);
    }).catch((err: Error) => {
      console.error(`promise: generate RSA Key failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    });
}

async function sign(keyAlias: string, plaintext: string) {
  let signProperties = getRsaSignProperties();
  let options: huks.HuksOptions = {
    properties: signProperties,
    inData: stringToUint8Array(plaintext)
  }
  await huks.initSession(keyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((err: Error) => {
      console.error(`promise: init sign failed, error: ` + JSON.stringify(err));
      return;
    });

  if (handle !== undefined) {
    await huks.finishSession(handle, options)
      .then((data) => {
        console.info(`promise: sign success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
        signature = data.outData as Uint8Array;
      }).catch((err: Error) => {
        console.error(`promise: sign failed, error: ` + JSON.stringify(err));
        throw (err as Error);
      });
  }
}

async function verify(keyAlias: string, plaintext: string, signature: Uint8Array) {
  let verifyProperties = getRsaVerifyProperties();
  let options: huks.HuksOptions = {
    properties: verifyProperties,
    inData: stringToUint8Array(plaintext)
  }
  await huks.initSession(keyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((err: Error) => {
      console.error(`promise: init verify failed, error: ` + JSON.stringify(err));
      return;
    });

  if (handle !== undefined) {
    await huks.updateSession(handle, options)
      .then((data) => {
        console.info(`promise: update verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      }).catch((err: Error) => {
        console.error(`promise: update verify failed, error: ` + JSON.stringify(err));
        throw (err as Error);
      });

    options.inData = signature;
    await huks.finishSession(handle, options)
      .then((data) => {
        console.info(`promise: verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      }).catch((err: Error) => {
        console.error(`promise: verify failed, error: ` + JSON.stringify(err));
        throw (err as Error);
      });
  }
}

async function deleteRsaKey(keyAlias: string) {
  let emptyOptions: huks.HuksOptions = {
    properties: []
  }
  await huks.deleteKeyItem(keyAlias, emptyOptions)
    .then((data) => {
      console.info(`promise: delete data success`);
    }).catch((err: Error) => {
      console.error(`promise: delete data failed`);
      throw (err as Error);
    });
}

export async function testSignVerify() {
  await generateRsaKey(keyAlias);
  await sign(keyAlias, plaintext);
  await verify(keyAlias, plaintext, signature);
  await deleteRsaKey(keyAlias);
}
```

### RSA/SHA256/PKCS1\_V1\_5

```typescript
/*
 * 密钥算法为RSA，摘要算法为SHA256，填充模式为PKCS1_V1_5
 */
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = 'test_rsaKeyAlias';
let handle: number;
let plaintext = '123456';
let signature: Uint8Array;

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

function getRsaGenerateProperties() {
  let properties: huks.HuksParam[] = [
    { tag: huks.HuksTag.HUKS_TAG_ALGORITHM, value: huks.HuksKeyAlg.HUKS_ALG_RSA },
    { tag: huks.HuksTag.HUKS_TAG_KEY_SIZE, value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048 },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
    },
    { tag: huks.HuksTag.HUKS_TAG_PADDING, value: huks.HuksKeyPadding.HUKS_PADDING_PKCS1_V1_5 },
    { tag: huks.HuksTag.HUKS_TAG_DIGEST, value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256 }
  ];
  return properties;
}

function getRsaSignProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS1_V1_5
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }];
  return properties;
}

function getRsaVerifyProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS1_V1_5
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }];
  return properties;
}

async function generateRsaKey(keyAlias: string) {
  let genProperties = getRsaGenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  }
  await huks.generateKeyItem(keyAlias, options)
    .then((data) => {
      console.info(`promise: generate RSA Key success, data = ${JSON.stringify(data)}`);
    }).catch((err: Error) => {
      console.error(`promise: generate RSA Key failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
}

async function sign(keyAlias: string, plaintext: string) {
  let signProperties = getRsaSignProperties();
  let options: huks.HuksOptions = {
    properties: signProperties,
    inData: stringToUint8Array(plaintext)
  }
  await huks.initSession(keyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((err: Error) => {
      console.error(`promise: init sign failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: sign success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      signature = data.outData as Uint8Array;
    }).catch((err: Error) => {
      console.error(`promise: sign failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
}

async function verify(keyAlias: string, plaintext: string, signature: Uint8Array) {
  let verifyProperties = getRsaVerifyProperties()
  let options: huks.HuksOptions = {
    properties: verifyProperties,
    inData: stringToUint8Array(plaintext)
  }
  await huks.initSession(keyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((err: Error) => {
      console.error(`promise: init verify failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
  await huks.updateSession(handle, options)
    .then((data) => {
      console.info(`promise: update verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
    }).catch((err: Error) => {
      console.error(`promise: update verify failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
  options.inData = signature;
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
    }).catch((err: Error) => {
      console.error(`promise: verify failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
}

async function deleteRsaKey(keyAlias: string) {
  let emptyOptions: huks.HuksOptions = {
    properties: []
  }
  await huks.deleteKeyItem(keyAlias, emptyOptions)
    .then((data) => {
      console.info(`promise: delete data success`);
    }).catch((err: Error) => {
      console.error(`promise: delete data failed`);
      throw (err as Error);
    })
}

export async function testSignVerify() {
  await generateRsaKey(keyAlias);
  await sign(keyAlias, plaintext);
  await verify(keyAlias, plaintext, signature);
  await deleteRsaKey(keyAlias);
}
```

### RSA2048/SHA384/PSS

```typescript
/*
 * 密钥算法为RSA2048、摘要算法为SHA384、填充模式为PSS
 */
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = 'test_rsaSha384PssKeyAlias';
let handle: number;
let plaintext = '123456';
let signature: Uint8Array;

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

function getRsaGenerateProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN |
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PSS
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA384
  }];
  return properties;
}

function getRsaSignProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PSS
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA384
  }];
  return properties;
}

function getRsaVerifyProperties() {
  let properties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PSS
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA384
  }];
  return properties;
}

async function generateRsaKey(keyAlias: string) {
  let genProperties = getRsaGenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  }
  await huks.generateKeyItem(keyAlias, options)
    .then((data) => {
      console.info(`promise: generate RSA Key success, data = ${JSON.stringify(data)}`);
    }).catch((err: Error) => {
      console.error(`promise: generate RSA Key failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
}

async function sign(keyAlias: string, plaintext: string) {
  let signProperties = getRsaSignProperties();
  let options: huks.HuksOptions = {
    properties: signProperties,
    inData: stringToUint8Array(plaintext)
  };
  await huks.initSession(keyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((err: Error) => {
      console.error(`promise: init sign failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: sign success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      signature = data.outData as Uint8Array;
    }).catch((err: Error) => {
      console.error(`promise: sign failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
}

async function verify(keyAlias: string, plaintext: string, signature: Uint8Array) {
  let verifyProperties = getRsaVerifyProperties()
  let options: huks.HuksOptions = {
    properties: verifyProperties,
    inData: stringToUint8Array(plaintext)
  };
  await huks.initSession(keyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((err: Error) => {
      console.error(`promise: init verify failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
  await huks.updateSession(handle, options)
    .then((data) => {
      console.info(`promise: update verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
    }).catch((err: Error) => {
      console.error(`promise: update verify failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
  options.inData = signature;
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
    }).catch((err: Error) => {
      console.error(`promise: verify failed, error: ` + JSON.stringify(err));
      throw (err as Error);
    })
}

async function deleteRsaKey(keyAlias: string) {
  let emptyOptions: huks.HuksOptions = {
    properties: []
  };
  await huks.deleteKeyItem(keyAlias, emptyOptions)
    .then((data) => {
      console.info(`promise: delete data success`);
    }).catch((err: Error) => {
      console.error(`promise: delete data failed`);
      throw (err as Error);
    })
}

async function testSignVerify() {
  await generateRsaKey(keyAlias);
  await sign(keyAlias, plaintext);
  await verify(keyAlias, plaintext, signature);
  await deleteRsaKey(keyAlias);
}
```

### ECC/SHA256/携带认证信息的签名类型

前提条件：此功能的示例代码依赖数字盾服务的设置数字盾密码和验证数字盾密码，请参考[数字盾服务](devicesecurity-trustedauth-service.md)的数字盾密码管理和交易信息密码认证。

```ts
/*
 * 密钥算法为ECC，摘要算法为SHA256，用户认证类型包含TUI PIN，携带认证信息的签名类型
 * 在签名参数中加上HUKS_TAG_KEY_SECURE_SIGN_TYPE，值为HUKS_SECURE_SIGN_WITH_AUTHINFO即可使用携带认证信息的签名类型
 * 在验签时，把携带认证信息的签名的前41位数据拆出来，剩下的是签名，然后把携带的认证信息拼在原数据的前面。
 * 设置数字盾密码和验证数字盾密码请参考数字盾服务
 */
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = 'test_eccKeyAlias';
let handle: number;
let challenge: Uint8Array;
let plaintext = '123456';
let signature: Uint8Array;

function stringToUint8Array(str: String) {
  let arr: number[] = new Array();
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

function GetEccGenerateProperties() {
  let properties: Array<huks.HuksParam> = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_ECC
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256,
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
  }, {
    tag: huks.HuksTag.HUKS_TAG_USER_AUTH_TYPE,
    value: huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_TUI_PIN | huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_FINGERPRINT | huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_FACE
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_ACCESS_TYPE,
    value: huks.HuksAuthAccessType.HUKS_AUTH_ACCESS_ALWAYS_VALID
  }, {
    tag: huks.HuksTag.HUKS_TAG_CHALLENGE_TYPE,
    value: huks.HuksChallengeType.HUKS_CHALLENGE_TYPE_NORMAL
  }];

  return properties;
}

function GetEccSignProperties() {
  let properties: Array<huks.HuksParam> = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_ECC
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SECURE_SIGN_TYPE,
    value: huks.HuksSecureSignType.HUKS_SECURE_SIGN_WITH_AUTHINFO
  }];
  return properties;
}

function GetEccVerifyProperties() {
  let properties: Array<huks.HuksParam> = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_ECC
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }];
  return properties;
}

async function GenerateEccKey(keyAlias: string) {
  let genProperties = GetEccGenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  }
  await huks.generateKeyItem(keyAlias, options)
    .then((data) => {
      console.info(`promise: generate ECC Key success, data = ${JSON.stringify(data)}`);
    }).catch((err: Error) => {
      console.error(`promise: generate ECC Key failed, error: ` + JSON.stringify(err));
    })
}

async function sign(keyAlias: string, plaintext: string) {
  let signProperties = GetEccSignProperties();
  let options: huks.HuksOptions = {
    properties: signProperties,
    inData: stringToUint8Array(plaintext)
  }
  await huks.initSession(keyAlias, options)
    .then((data) => {
      handle = data.handle;
      challenge = data.challenge as Uint8Array;
    }).catch((err: Error) => {
      console.error(`promise: init sign failed, error: ` + JSON.stringify(err));
    })

  let TuiAuthToken :trustedAuthentication.AuthToken;
  // 验证TUI PIN并获取Authtoken请参考数字盾服务

  await huks.finishSession(handle, options, TuiAuthToken.authToken)
    .then((data) => {
      console.info(`promise: sign success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
      signature = data.outData as Uint8Array;
    }).catch((err: Error) => {
      console.error(`promise: sign failed, error: ` + JSON.stringify(err));
    })
}

async function verify(keyAlias: string, plaintext: string, signature: Uint8Array) {
  let verifyProperties = GetEccVerifyProperties();
  // 在验签时，把携带认证信息的签名的前41位数据拆出来，剩下的是签名，然后把携带的认证信息拼在原数据的前面。
  let appendInfo = signature.subarray(0, 41);
  let newSignature = signature.subarray(41);
  let newIndata = new Uint8Array(appendInfo.length + indataArray.length);
  newIndata.set(appendInfo, 0);
  newIndata.set(stringToUint8Array(plaintext), appendInfo.length);
  let options: huks.HuksOptions = {
    properties: verifyProperties,
    inData: newIndata
  }
  await huks.initSession(keyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((err: Error) => {
      console.error(`promise: init verify failed, error: ` + JSON.stringify(err));
    })
  await huks.updateSession(handle, options)
    .then((data) => {
      console.info(`promise: update verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
    }).catch((err: Error) => {
      console.error(`promise: update verify failed, error: ` + JSON.stringify(err));
    })
  options.inData = newSignature;
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
    }).catch((err: Error) => {
      console.error(`promise: verify failed, error: ` + JSON.stringify(err));
    })
}

async function DeleteEccKey(keyAlias: string) {
  let emptyOptions: huks.HuksOptions = {
    properties: []
  }
  await huks.deleteKeyItem(keyAlias, emptyOptions)
    .then((data) => {
      console.info(`promise: delete data success`);
    }).catch((err: Error) => {
      console.error(`promise: delete data failed`);
    })
}

async function testSignVerify() {
  await GenerateEccKey(keyAlias);
  await sign(keyAlias, plaintext);
  await verify(keyAlias, plaintext, signature);
  await DeleteEccKey(keyAlias);
}
```
