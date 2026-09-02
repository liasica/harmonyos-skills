---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-anon-attestation-arkts
title: 匿名密钥证明(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥证明 > 匿名密钥证明(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:03+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b166488da3f9cc4d0c1c3f8f3f08518b1854bfe967958e1ccdb77559f709b3dd
---

在使用本功能时，需确保网络通畅。

## 开发步骤

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化参数集。

   [HuksOptions](../harmonyos-references/js-apis-huks.md#huksoptions)中的properties字段中的参数必须包含[HUKS\_TAG\_ATTESTATION\_CHALLENGE](../harmonyos-references/js-apis-huks.md#hukstag)属性，可选参数包含[HUKS\_TAG\_ATTESTATION\_ID\_VERSION\_INFO](../harmonyos-references/js-apis-huks.md#hukstag)，[HUKS\_TAG\_ATTESTATION\_ID\_ALIAS](../harmonyos-references/js-apis-huks.md#hukstag)属性。
3. 生成非对称密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。
4. 将密钥别名与参数集作为参数传入[anonAttestKeyItem](../harmonyos-references/js-apis-huks.md#huksanonattestkeyitem11)方法中，即可证明密钥。

## 开发案例

```typescript
/*
 * 以下以anonAttestKey的Promise接口操作验证为例
 */
import { huks } from '@kit.UniversalKeystoreKit';

/* 1.确定密钥别名 */
let keyAliasString = 'key anon attest';
let aliasString = keyAliasString;
let aliasUint8 = stringToUint8Array(keyAliasString);
let securityLevel = stringToUint8Array('sec_level');
let challenge = stringToUint8Array('challenge_data');
let versionInfo = stringToUint8Array('version_info');
let anonAttestCertChain: string[];

class ThrowObject {
  public isThrow: boolean = false;
}

/* 封装生成时的密钥参数集 */
let genKeyProperties: huks.HuksParam[] = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  },
  {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PSS
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_GENERATE_TYPE,
    value: huks.HuksKeyGenerateType.HUKS_KEY_GENERATE_TYPE_DEFAULT
  },
  {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB
  }
]
let genOptions: huks.HuksOptions = {
  properties: genKeyProperties
};

/* 2.封装证明密钥的参数集 */
let anonAttestKeyProperties: huks.HuksParam[] = [
  {
    tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_SEC_LEVEL_INFO,
    value: securityLevel
  },
  {
    tag: huks.HuksTag.HUKS_TAG_ATTESTATION_CHALLENGE,
    value: challenge
  },
  {
    tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_VERSION_INFO,
    value: versionInfo
  },
  {
    tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_ALIAS,
    value: aliasUint8
  }
]
let huksOptions: huks.HuksOptions = {
  properties: anonAttestKeyProperties
};

function stringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
  return new Promise<void>((resolve, reject) => {
    try {
      huks.generateKeyItem(keyAlias, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throwObject.isThrow = true;
      throw (error as Error);
    }
  });
}

/* 3.生成密钥 */
async function publicGenKeyFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
  console.info(`enter promise generateKeyItem`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await generateKeyItem(keyAlias, huksOptions, throwObject)
      .then((data) => {
        console.info(`promise: generateKeyItem success, data = ${JSON.stringify(data)}`);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(`promise: generateKeyItem failed, ${JSON.stringify(error)}`);
        }
      });
  } catch (error) {
    console.error(`promise: generateKeyItem input arg invalid, ${JSON.stringify(error)}`);
  }
}

/* 4.证明密钥 */
function anonAttestKeyItem(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
  return new Promise<huks.HuksReturnResult>((resolve, reject) => {
    try {
      huks.anonAttestKeyItem(keyAlias, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throwObject.isThrow = true;
      throw (error as Error);
    }
  });
}

async function publicAnonAttestKey(keyAlias: string, huksOptions: huks.HuksOptions): Promise<string> {
  console.info(`enter promise anonAttestKeyItem`);
  let throwObject: ThrowObject = { isThrow: false };
  try {
    await anonAttestKeyItem(keyAlias, huksOptions, throwObject)
      .then((data) => {
        console.info(`promise: anonAttestKeyItem success, data = ${JSON.stringify(data)}`);
        if (data !== null && data.certChains !== null) {
          anonAttestCertChain = data.certChains as string[];
        }
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          throw (error as Error);
        } else {
          console.error(`promise: anonAttestKeyItem failed, ${JSON.stringify(error)}`);
        }
      });
    return 'Success';
  } catch (error) {
    console.error(`promise: anonAttestKeyItem input arg invalid, ${JSON.stringify(error)}`);
    return 'Failed';
  }
}

async function anonAttestKeyTest(): Promise<string> {
  await publicGenKeyFunc(aliasString, genOptions);
  let ret = await publicAnonAttestKey(aliasString, huksOptions);
  console.info('anon attest certChain data: ' + anonAttestCertChain)
  return ret;
}
```
