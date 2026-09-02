---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-ukey-signing-signature-verification-arkts
title: 签名/验签(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > 签名/验签 > 签名/验签(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:33+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:897fe6ada3b316b8f2c72730752ac68fe86b9c15bfd4266e8d10390ac8a2ce8a
---

当前指导提供以下示例，供开发者参考完成签名、验签开发：

* [密钥算法为RSA、摘要算法为SHA256、填充模式为PSS](huks-ukey-signing-signature-verification-arkts.md#rsasha256pss)

具体的场景介绍及支持的算法规格，请参考[签名/验签介绍及算法规格](huks-ukey-signing-signature-verification-overview.md)。

## 开发步骤

**签名**

1. 通过证书管理系统能力提供的[openAuthorizeDialog](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取[keyUri](../harmonyos-references/js-apis-certmanagerdialog.md#certreference22)作为resourceId，并作为密钥别名，[打开资源](huks-open-close-resource-ndk.md#打开资源)后完成PIN码认证。
2. 指定待签名的明文数据。
3. 获取属性参数[HuksOptions](../harmonyos-references/js-apis-huks.md#huksoptions)，包括两个字段properties和inData。inData传入明文数据，properties传入算法参数配置。
4. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
5. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，获取签名signature。

**验签**

1. 通过证书管理系统能力提供的[openAuthorizeDialog](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取[keyUri](../harmonyos-references/js-apis-certmanagerdialog.md#certreference22)作为resourceId，并作为密钥别名，然后[打开资源](huks-open-close-resource-ndk.md#打开资源)。
2. 获取待验证的签名。
3. 获取属性参数[HuksOptions](../harmonyos-references/js-apis-huks.md#huksoptions)，包括两个字段properties和inData。inData传入签名signature，properties传入算法参数配置。
4. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
5. 调用[updateSession](../harmonyos-references/js-apis-huks.md#huksupdatesession9)更新密钥会话。
6. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，验证签名。

## 开发案例

### RSA/SHA256/PSS

```ts
/*
 * 密钥算法为RSA，摘要算法为SHA256，填充模式为PSS
 */
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

let handle: number;
let plaintext = '123456';
let signature: Uint8Array;

function StringToUint8Array(str: string) {
  let arr: number[] = [];
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

function GetRsaSignProperties() {
  let properties: Array<huks.HuksParam> = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PSS
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_CLASS,
    value: huks.HuksKeyClassType.HUKS_KEY_CLASS_EXTENSION
  }];
  return properties;
}

function GetRsaVerifyProperties() {
  let properties: Array<huks.HuksParam> = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PSS
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_CLASS,
    value: huks.HuksKeyClassType.HUKS_KEY_CLASS_EXTENSION
  }];
  return properties;
}

async function initSession(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info('promise: enter initSession.');
  try {
    await huks.initSession(keyAlias, huksOptions)
      .then((data) => {
        handle = data.handle;
        console.info('promise: initSession success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: initSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error('promise: initSession input arg invalid.');
  }
}

async function updateSession(handle: number, huksOptions: huks.HuksOptions) {
  console.info('promise: enter updateSession.');
  try {
    await huks.updateSession(handle, huksOptions)
      .then((data) => {
        let outData = data.outData as Uint8Array;
        console.info(`promise: updateSession success, data = ${Uint8ArrayToString(outData)}`);
      }).catch((error: BusinessError) => {
        console.error(`promise: updateSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error('promise: updateSession input arg invalid.');
  }
}

async function finishSession(handle: number, huksOptions: huks.HuksOptions) {
  console.info('promise: enter finishSession.');
  try {
    await huks.finishSession(handle, huksOptions)
      .then((data) => {
        signature = data.outData as Uint8Array;
        console.info(`promise: finishSession success, data = ${Uint8ArrayToString(signature)}`);
      }).catch((error: BusinessError) => {
        console.error(`promise: finishSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error('promise: finishSession input arg invalid.');
  }
}

async function Sign(keyAlias: string, plaintext: string) {
  console.info('enter Sign.');
  let signProperties = GetRsaSignProperties();
  let options: huks.HuksOptions = {
    properties: signProperties,
  }
  await initSession(keyAlias, options);

  if (handle !== undefined) {
    options.inData = StringToUint8Array(plaintext);
    await finishSession(handle, options);
  }
}

async function Verify(keyAlias: string, plaintext: string, signature: Uint8Array) {
  console.info('enter Verify.');
  let verifyProperties = GetRsaVerifyProperties();
  let options: huks.HuksOptions = {
    properties: verifyProperties,
  }

  await initSession(keyAlias, options);

  if (handle !== undefined) {
    options.inData = StringToUint8Array(plaintext);
    await updateSession(handle, options);
    options.inData = signature;
    await finishSession(handle, options);
  }
}

async function testSignVerify() {
  // 假设keyAlias是已获取的resourceId
  let keyAlias = JSON.stringify({
    providerName: "testProviderName",
    bundleName: "com.example.cryptoapplication",
    abilityName: "CryptoExtension",
    index: {
      key: "testKey"
    } as ESObject
  });
  await Sign(keyAlias, plaintext);
  await Verify(keyAlias, plaintext, signature);
}
```
