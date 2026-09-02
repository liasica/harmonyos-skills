---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-universal-keystore-15
title: HUKS如何分段加解密
breadcrumb: FAQ > 系统开发 > 安全 > 密钥管理（Universal Keystore） > HUKS如何分段加解密
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:530c26db1337c58a941612efc40f94ee6bc82f86de68599f5c5d6dd851c9232a
---

## 问题现象

如何使用密钥管理服务进行分段加解密？

## 背景知识

[加解密(ArkTS)](../harmonyos-guides/huks-encryption-decryption-arkts.md)：以AES128、RSA2048和SM2为例，完成加解密。

[huks.updateSession](../harmonyos-references/js-apis-huks.md#huksupdatesession9)：[huks.initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9-1)，[huks.updateSession](../harmonyos-references/js-apis-huks.md#huksupdatesession9)，[huks.finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9-2)为三段式接口，分段加解密时，传入finishSession的inData要设置为空。

## 解决方案

分段加解密可通过将明文进行指定长度多段拆分的形式传入，以1024为例，实现AES/CBC/PKCS7分段加解密。完整代码如下：

```ts
import { hilog } from '@kit.PerformanceAnalysisKit';
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';

const MAX_UPDATE_SESSION_LENGTH = 1024;

let aesKeyAlias = 'test_aesKeyAlias';
let handle: number;
let plainText = '1234567890';
let result = '';
let IV = '001122334455';
let cipherData: Uint8Array;

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('测试加解密')
        .width('100%')
        .onClick(async () => {
          generatorData();
          await GenerateAesKey();
          await EncryptData();
          await DecryptData();
          check();
        });
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center);
  }
}

function StringToUint8Array(data: string): Uint8Array {
  return new Uint8Array(buffer.from(data, 'utf-8').buffer);
}

function Uint8ArrayToString(input: Uint8Array): string {
  let bufferStr = buffer.from(input).toString('utf-8');
  return bufferStr;
}

function generatorData() {
  let i = 0;
  plainText = '1234567890';
  while (i <= 10) {
    i++;
    plainText = plainText + plainText;
  }
  console.info('造数据成功');
}

// 生成密钥
async function GenerateAesKey() {
  let genProperties = GetAesGenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  };

  await huks.generateKeyItem(aesKeyAlias, options)
    .then(() => {
      hilog.info(0x0000, 'AppDataSecurity', `promise: generate AES Key success`);
    }).catch((error: Error) => {
      console.error(`promise: generate AES Key failed, ${error.message}`);
    });
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
    value: StringToUint8Array(IV)
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
    value: StringToUint8Array(IV)
  }];
  return properties;
}

// 分段加密
async function EncryptData() {
  let encryptProperties = GetAesEncryptProperties();
  let options: huks.HuksOptions = {
    properties: encryptProperties,
    inData: new Uint8Array(0)
  };

  await huks.initSession(aesKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: Error) => {
      console.error(`promise: init EncryptData failed, ${error.message}`);
    });

  let resultTemp = new Uint8Array(0);
  let contentTemp = plainText;
  while (contentTemp.length > 0) {
    // 超过长度会取最长
    const contentCurr = contentTemp.substring(0, MAX_UPDATE_SESSION_LENGTH);
    // 起始点大于长度会返回""
    contentTemp = contentTemp.substring(MAX_UPDATE_SESSION_LENGTH, contentTemp.length);
    options.inData = StringToUint8Array(contentCurr);
    await huks.updateSession(handle, options).then((data) => {
      const mergeText = new Uint8Array(resultTemp.length + data.outData!.length);
      mergeText.set(resultTemp);
      mergeText.set(data.outData!, resultTemp.length);
      resultTemp = mergeText;
    }).catch(async (error: BusinessError) => {
      console.error(`promise: encrypt updateSession failed, ${error.message}`);
    });
  }

  // 分段加解密时，传入finishSession的inData要设置为空的
  options.inData = new Uint8Array(0);
  await huks.finishSession(handle, options).then((data) => {
    cipherData = new Uint8Array(resultTemp.length + data.outData!.length);
    cipherData.set(resultTemp);
    cipherData.set(data.outData!, resultTemp.length);
  }).catch((error: Error) => {
    console.error(`promise: encrypt data failed, ${error.message}`);
  });
}

// 分段解密
async function DecryptData() {
  let decryptOptions = GetAesDecryptProperties();
  let options: huks.HuksOptions = {
    properties: decryptOptions,
    inData: cipherData
  };

  await huks.initSession(aesKeyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((error: Error) => {
      console.error(`promise: init DecryptData failed, ${error.message}`);
    });

  let resultTemp = new Uint8Array(0);
  let contentTemp = cipherData;
  while (contentTemp.length > 0) {
    const contentCurr = contentTemp.slice(0, MAX_UPDATE_SESSION_LENGTH); // 超过长度会取最长
    contentTemp = contentTemp.slice(MAX_UPDATE_SESSION_LENGTH, contentTemp.length);
    options.inData = contentCurr;
    await huks.updateSession(handle, options).then((data) => {
      const mergeText = new Uint8Array(resultTemp.length + data.outData!.length);
      mergeText.set(resultTemp);
      mergeText.set(data.outData!, resultTemp.length);
      resultTemp = mergeText;
    }).catch((error: Error) => {
      console.error(`promise: decrypt updateSession failed, ${error.message}`);
    });
  }

  options.inData = new Uint8Array(0);
  await huks.finishSession(handle, options).then(() => {
    result = Uint8ArrayToString(resultTemp);
  }).catch((error: Error) => {
    console.error(`promise: decrypt data failed, ${error.message}`);
  });
}

// 验证
function check() {
  console.info('批量加解密结果：', result === plainText);
}
```
