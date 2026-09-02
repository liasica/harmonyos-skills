---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/device-attestation-apps
title: 应用端开发
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 应用真实性证明 > 创建密钥确立可信凭证 > 应用端开发
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:32+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:a3a6094d1118b6ae478500acde7f33d78ace573150f6e0cad5edf143d7dacb9e
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

## 查询应用公私钥对是否存在

查询应用公私钥对是否存在，如果已存在，则不需要重复创建。

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = 'serviceKey_user01';  // 业务密钥别名
let isKeyExist: Boolean;
 
let huksOptions: huks.HuksOptions = {
  properties: []
}
try {
  huks.hasKeyItem(keyAlias, huksOptions, (error, data) => {
    if (error) {
      console.error(`callback: hasKeyItem failed, ` + JSON.stringify(error));
    } else {
      if (data !== null && data.valueOf() !== null) {
        isKeyExist = data.valueOf();
        console.info(`callback: hasKeyItem success, isKeyExist = ${isKeyExist}`);
      }
    }
  });
} catch (error) {
  console.error(`callback: hasKeyItem input arg invalid, ` + JSON.stringify(error));
}
```

## 创建应用公私钥对

创建一个用于验证应用请求真实性的非对称算法密钥对，称为应用公私钥对（包含应用公钥和应用私钥），比如RSA、ECC算法的密钥对。通过Universal Keystore Kit创建的密钥对基于硬件的安全环境进行生成和安全存储。

**说明** 

实现建议：在免密登录/支付应用等场景，需要为应用中的每个登录用户生成唯一的密钥对。

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyAlias = 'serviceKey_user01'; // 业务密钥别名

function GetGenerateProperties() {
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
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN |
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  };
  properties[index++] = {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }
  return properties;
}

async function GenerateKey(keyAlias: string) {
  let genProperties = GetGenerateProperties();
  let options: huks.HuksOptions = {
    properties: genProperties
  }
  await huks.generateKeyItem(keyAlias, options)
    .then(() => {
      console.info(`promise: generate Key success.`);
    }).catch((err: BusinessError) => {
      console.error(`promise: generate Key failed, error: ` + err.message);
    })
}
```

## 对应用公钥和应用ID进行证明

您的应用调用Universal Keystore Kit的离线密钥证明接口（推荐）或在线密钥证明接口（不推荐）对生成的应用公钥和调用的应用身份进行证明，Universal Keystore Kit返回密钥证明证书链给应用，证书链采用X509标准格式。其中在线密钥证明接口返回的证书链包含3本证书，离线密钥证明接口返回的证书链包含4本证书。

**说明** 

安全建议：为了在发送密钥证明证书链给应用服务器时能够防重放攻击，建议应用先从应用服务器获取一次性的挑战值Challenge，并在调用密钥证明接口时输入挑战值Challenge。应用服务器采用安全随机数生成挑战值Challenge，并缓存到服务器中。

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';
import { deviceInfo } from '@kit.BasicServicesKit';

class HuksProperties {
  tag: huks.HuksTag = huks.HuksTag.HUKS_TAG_ALGORITHM;
  value: huks.HuksKeyAlg | huks.HuksKeySize | huks.HuksKeyPurpose | huks.HuksKeyDigest |
    huks.HuksKeyStorageType | huks.HuksKeyPadding | huks.HuksKeyGenerateType |
    huks.HuksCipherMode | Uint8Array = huks.HuksKeyAlg.HUKS_ALG_ECC;
}

let challenge = stringToUint8Array('challenge_data'); // 从服务器获取的挑战值Challenge
let keyAlias = 'serviceKey_user01'; // 业务密钥别名

function stringToUint8Array(str: string): Uint8Array {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  let tmpUint8Array = new Uint8Array(arr);
  return tmpUint8Array;
}

async function anonAttestKey(): Promise<void> {
  let aliasString = keyAlias;

  let properties: HuksProperties[] = [
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_CHALLENGE,
      value: challenge
    }
  ];

  let options: huks.HuksOptions = {
    properties: properties
  };

  let g_secInfo :Uint8Array = stringToUint8Array("hi_security_level_info");
  let g_challenge : Uint8Array = stringToUint8Array("hi_challenge_data");
  let g_version : Uint8Array = stringToUint8Array("hi_os_version_data");
  let g_keyAlias : Uint8Array = stringToUint8Array("testKey");

  let gCommonParam: Array<huks.HuksParam> = [
    { tag : huks.HuksTag.HUKS_TAG_ATTESTATION_ID_SEC_LEVEL_INFO, value : g_secInfo },
    { tag : huks.HuksTag.HUKS_TAG_ATTESTATION_CHALLENGE, value : g_challenge },
    { tag : huks.HuksTag.HUKS_TAG_ATTESTATION_ID_VERSION_INFO, value : g_version },
    { tag : huks.HuksTag.HUKS_TAG_ATTESTATION_ID_ALIAS, value : g_keyAlias },
  ];

  try {
    let sdkApiVersionInfo: number = deviceInfo.sdkApiVersion;
    if (sdkApiVersionInfo<26) {
      let data = await huks.anonAttestKeyItem(aliasString, options);
      console.info(`anonAttestKeyItem success`);
      data.certChains?.forEach(cert => {
          console.info(cert);
      });
    } else {
      let data = await huks.anonAttestKeyItemOffline(aliasString, gCommonParam);
      // todo：把证书链信息（data变量）发送到云侧的服务器。如下示例代码把证书链打印到日志中，供调测使用，商用代码不需要打印。
      console.info(`anonAttestKeyItem success`);
      data.certChains?.forEach(cert => {
        console.info(cert);
      });
    }
  } catch (error) {
    console.error(`promise: anonAttestKeyItem fail`);
  }
}
```
