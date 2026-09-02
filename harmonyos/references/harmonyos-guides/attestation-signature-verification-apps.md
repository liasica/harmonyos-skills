---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/attestation-signature-verification-apps
title: 应用端开发
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 应用真实性证明 > 签名验签识别真实请求 > 应用端开发
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:32+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:68af1407b00010e92f2aad045eca69c68abbbdb943b68c42f4ab7de26bf43d2d
---

## 接口说明

接口能力由[Universal Keystore Kit](huks-overview.md)提供，涉及的功能指导请参考：

* [Universal Keystore Kit简介](huks-overview.md)
* [查询密钥是否存在(ArkTS)](huks-check-key-arkts.md)
* [查询密钥是否存在(C/C++)](huks-check-key-ndk.md)
* [生成密钥(ArkTS)](huks-key-generation-arkts.md)
* [生成密钥(C/C++)](huks-key-generation-ndk.md)
* [在线匿名密钥证明(ArkTS)](huks-key-anon-attestation-arkts.md)
* [在线匿名密钥证明(C/C++)](huks-key-anon-attestation-ndk.md)
* [离线匿名密钥证明(ArkTS)](huks-offline-anon-attestation-arkts.md)
* [签名/验签(ArkTS)](huks-signing-signature-verification-arkts.md)
* [签名/验签(C/C++)](huks-signing-signature-verification-ndk.md)

## 使用前提

使用应用的私钥对业务请求进行签名的前提是已经创建应用公私钥和在服务器保存了应用公钥，相关开发指南请参考：

* [查询应用公私钥对是否存在](device-attestation-apps.md#查询应用公私钥对是否存在)
* [创建应用公私钥对](device-attestation-apps.md#创建应用公私钥对)
* [对应用公钥和应用ID进行证明](device-attestation-apps.md#对应用公钥和应用id进行证明)

## 使用应用私钥对业务请求进行签名

在密钥证明流程处理成功后，您的应用在进行一些安全敏感的端云业务时，可以使用已验证的密钥对业务请求进行安全保护。

应用可以调用Universal Keystore Kit的签名接口，使用应用私钥对业务请求数据（如HTTP请求的Body）进行签名，然后把签名结果数据添加到请求消息中（如HTTP的Header字段）。为了方便应用服务器查找应用公钥用于验签，应用应该在业务请求中携带应用公钥ID。

**说明** 

安全建议：为了在发送业务请求时能够防重放攻击，建议应用先从应用服务器获取一次性的挑战值Challenge。应用服务器采用安全随机数生成挑战值Challenge，并缓存到服务器中。

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let keyAlias = 'serviceKey_user01'; // 业务密钥别名
let handle: number;
let plaintext = '123456'; // 待签名的明文数据，建议包含服务器端返回的Challenge。
let signature: Uint8Array; // 存储签名结果数据的变量

function StringToUint8Array(str: String) {
  let arr: number[] = new Array();
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function GetSignProperties() {
  let properties: Array<huks.HuksParam> = new Array();
  let index = 0;
  properties[index++] = {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_ECC
  };
  properties[index++] = {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  };
  properties[index++] = {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
  };
  properties[index++] = {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }
  return properties;
}

async function Sign(keyAlias: string, plaintext: string) {
  let signProperties = GetSignProperties();
  let options: huks.HuksOptions = {
    properties: signProperties,
    inData: StringToUint8Array(plaintext)
  }
  await huks.initSession(keyAlias, options)
    .then((data) => {
      handle = data.handle;
    }).catch((err: BusinessError) => {
      console.error(`promise: init sign failed, error: ` + err.message);
    })
  await huks.finishSession(handle, options)
    .then((data) => {
      signature = data.outData as Uint8Array;
  
      let base64 = new util.Base64Helper();
      let signatureBase64 = base64.encodeToStringSync(signature);
      // todo：把签名结果的Base64编码（signatureBase64变量）发送到云侧的服务器。如下示例代码把签名结果打印到日志中，供调测使用，商用代码不需要打印。
      console.info(`sign success, result:` + signatureBase64);
  
    }).catch((err: BusinessError) => {
      console.error(`promise: sign failed, error: ` + err.message);
    })
}
```
