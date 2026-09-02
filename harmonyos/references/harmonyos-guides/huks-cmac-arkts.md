---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-cmac-arkts
title: CMAC(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > CMAC > CMAC(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1dfaca06ed9db735c1c8d866147ff14a51d8b1b8905ca64061a2680b7b2c11ff
---

CMAC是基于对称密钥分组加密算法的消息认证码（Cipher-based Message Authentication Code），目前支持3DES加密算法的消息认证方法。

**说明** 

仅支持在智能穿戴设备（Wearable）使用。

## 开发步骤

**生成密钥**

1. 获取生成密钥算法参数配置。
2. 调用[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)生成密钥，支持的规格是128比特长度的密钥。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md#支持的算法)的规格介绍，导入已有的密钥。

**执行CMAC**

1. 获取CMAC算法参数配置。
2. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
3. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，获取MAC数据。

```ts
/*
 * 以下以CMAC密钥的Promise操作使用为例。
 */
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from "@kit.BasicServicesKit";
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let keyAlias = 'test_cmac';
let handle: number;
let plainText = '123456';
let IV = cryptoFramework.createRandom().generateRandomSync(8).data;
let macData: Uint8Array;

function StringToUint8Array(str: String) {
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

function GenerateKeyProperties() {
  const properties: Array<huks.HuksParam> = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_3DES
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_3DES_KEY_SIZE_128
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_MAC
  }];
  return properties;
}

function GetCmacProperties() {
  const properties: Array<huks.HuksParam> = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_CMAC
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_3DES_KEY_SIZE_128
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_MAC
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_CBC
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_ISO_IEC_9797_1
  }, {
    tag: huks.HuksTag.HUKS_TAG_IV,
    value: IV
  }];
  return properties;
}

async function GenerateCmacKey() {
  /*
   * 1.1 获取生成密钥算法参数配置
   */
  let genProperties = GenerateKeyProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  }
  /*
   * 1.2 调用generateKeyItem
   */
  await huks.generateKeyItem(keyAlias, options)
    .then(() => {
      console.info(`promise: generate cmac key success`);
    }).catch((error: BusinessError) => {
      console.error(`promise: generate cmac key failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function CmacData() {
  /*
   * 2.1 获取CMAC算法参数配置
   */
  let cmacProperties = GetCmacProperties();
  let options: huks.HuksOptions = {
    properties: cmacProperties,
    inData: StringToUint8Array(plainText)
  }
  /*
   * 2.2 调用initSession获取handle
   */
  await huks.initSession(keyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: BusinessError) => {
      console.error(`promise: init EncryptData failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
  /*
   * 2.3 调用finishSession获取CMAC的结果
   */
  await huks.finishSession(handle, options)
    .then((data) => {
      macData = data.outData as Uint8Array;
      console.info(`promise: cmac data success, data is ${Uint8ArrayToString(macData)}`);
    }).catch((error: BusinessError) => {
      console.error(`promise: cmac data failed, errCode : ${error.code}, errMsg : ${error.message}`);
    })
}

async function testCMAC() {
  await GenerateCmacKey();
  await CmacData();
}
```
