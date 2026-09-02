---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-kem-arkts
title: 密钥封装(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 密钥封装 > 密钥封装(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:32+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:c063abfe8ecd674fe58574e4e96ab30c022b2132cb63935ccee062fe76678b8a
---

从API版本26.0.0开始，支持后量子封装解封装算法。以ML-KEM-768和ML-KEM-1024为例，在密钥由HUKS管理的情况下，完成密钥封装和解封装。具体的场景介绍及支持的算法规格，请参考[密钥封装支持的算法](huks-kem-overview.md#支持的算法)。

## 接口介绍

开发者可以查阅API文档，获取密钥封装接口的详细说明：[huks.encapsulate](../harmonyos-references/js-apis-huks.md#huksencapsulate)、[huks.decapsulate](../harmonyos-references/js-apis-huks.md#huksdecapsulate)。

### 封装接口参数

在密钥封装时，接口参数如下表所示：

**封装接口参数列表：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | ML-KEM公钥密钥别名，密钥需预先通过generateKeyItem生成并存储在HUKS。 |
| params | [HuksParam[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksparam) | 是 | 密钥封装操作参数集，详见下方params参数集。 |
| sharedKeyAlias | string | 否 | 共享密钥存储别名。为空表示不存储，共享密钥返回给调用方；非空表示存储到HUKS。 |
| sharedKeyParams | [HuksParam[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksparam) | 否（sharedKeyAlias非空时必填） | 共享密钥的属性参数集，详见下方sharedKeyParams参数集。 |

**params参数集：**

| 属性名称（Tag） | 属性内容（Value） | 必填 | 说明 |
| --- | --- | --- | --- |
| HUKS\_TAG\_ALGORITHM | 枚举值[HuksKeyAlg](../harmonyos-references/js-apis-huks.md#hukskeyalg)中的HUKS\_ALG\_ML\_KEM。 | 是 | 密钥封装算法。 |
| HUKS\_TAG\_AUTH\_STORAGE\_LEVEL | 枚举值[HuksAuthStorageLevel](../harmonyos-references/js-apis-huks.md#huksauthstoragelevel11)，取值为HUKS\_AUTH\_STORAGE\_LEVEL\_DE（开机后可访问）、HUKS\_AUTH\_STORAGE\_LEVEL\_CE（首次解锁后可访问）、HUKS\_AUTH\_STORAGE\_LEVEL\_ECE（解锁状态时可访问）。 | 否 | 密钥安全等级。 |

**sharedKeyParams参数集（sharedKeyAlias非空时必选）：**

| 属性名称（Tag） | 属性内容（Value） | 必填 | 说明 |
| --- | --- | --- | --- |
| HUKS\_TAG\_ALGORITHM | 枚举值[HuksKeyAlg](../harmonyos-references/js-apis-huks.md#hukskeyalg)，如HUKS\_ALG\_AES等。 | 是 | 共享密钥算法。 |
| HUKS\_TAG\_KEY\_SIZE | 枚举值[HuksKeySize](../harmonyos-references/js-apis-huks.md#hukskeysize)，如HUKS\_AES\_KEY\_SIZE\_256等。 | 是 | 共享密钥大小。 |
| HUKS\_TAG\_PURPOSE | 枚举值[HuksKeyPurpose](../harmonyos-references/js-apis-huks.md#hukskeypurpose)，如HUKS\_KEY\_PURPOSE\_ENCRYPT | HUKS\_KEY\_PURPOSE\_DECRYPT等。 | 是 | 共享密钥用途。 |
| HUKS\_TAG\_KEY\_OVERRIDE | 类型为boolean。 | 否 | 是否覆写同名密钥，默认值为false。 |
| HUKS\_TAG\_IS\_DEVICE\_PASSWORD\_SET | 类型为boolean。 | 否 | 是否仅在设置了锁屏密码的情况下，共享密钥才允许被访问。为true时，表示仅在用户设置了锁屏密码的情况下，共享密钥才允许被访问；为false时，表示无论用户是否设置锁屏密码，共享密钥均允许被访问。默认值为false。 |
| HUKS\_TAG\_USER\_AUTH\_TYPE | 枚举值[HuksUserAuthType](../harmonyos-references/js-apis-huks.md#huksuserauthtype9)，取值为HUKS\_USER\_AUTH\_TYPE\_FINGERPRINT、HUKS\_USER\_AUTH\_TYPE\_FACE、HUKS\_USER\_AUTH\_TYPE\_PIN等，支持多选。 | 否 | 共享密钥的用户认证类型。 |
| HUKS\_TAG\_KEY\_AUTH\_ACCESS\_TYPE | 枚举值[HuksAuthAccessType](../harmonyos-references/js-apis-huks.md#huksauthaccesstype9)，取值为HUKS\_AUTH\_ACCESS\_INVALID\_CLEAR\_PASSWORD、HUKS\_AUTH\_ACCESS\_INVALID\_NEW\_BIO\_ENROLL、HUKS\_AUTH\_ACCESS\_ALWAYS\_VALID等。 | 否 | 共享密钥的认证访问类型。 |
| HUKS\_TAG\_CHALLENGE\_TYPE | 枚举值[HuksChallengeType](../harmonyos-references/js-apis-huks.md#hukschallengetype9)，取值为HUKS\_CHALLENGE\_TYPE\_NORMAL、HUKS\_CHALLENGE\_TYPE\_CUSTOM、HUKS\_CHALLENGE\_TYPE\_NONE。 | 否 | challenge类型。 |
| HUKS\_TAG\_AUTH\_TIMEOUT | 类型为number，单位为秒。 | 否 | auth token单次有效期。 |

### 解封装接口参数

在密钥解封装时，接口参数如下表所示。

**解封装接口参数列表：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | ML-KEM私钥密钥别名，密钥需预先通过generateKeyItem生成并存储在HUKS。 |
| params | [HuksParam[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksparam) | 是 | 密钥解封装操作参数集，详见下方params参数集。 |
| encapData | Uint8Array | 是 | 封装密文数据，由封装接口的返回结果[HuksReturnResult](../harmonyos-references/js-apis-huks.md#huksreturnresult9)中的outData字段提供。 |
| sharedKeyAlias | string | 否 | 共享密钥存储别名。为空表示不存储，共享密钥返回给调用方；非空表示存储到HUKS。 |
| sharedKeyParams | [HuksParam[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksparam) | 否（sharedKeyAlias非空时必填） | 共享密钥的属性参数集，参数同封装接口的sharedKeyParams参数集。 |

**params参数集：**

| 属性名称（Tag） | 属性内容（Value） | 必填 | 说明 |
| --- | --- | --- | --- |
| HUKS\_TAG\_ALGORITHM | 枚举值[HuksKeyAlg](../harmonyos-references/js-apis-huks.md#hukskeyalg)中的HUKS\_ALG\_ML\_KEM。 | 是 | 密钥解封装算法。 |
| HUKS\_TAG\_AUTH\_STORAGE\_LEVEL | 枚举值[HuksAuthStorageLevel](../harmonyos-references/js-apis-huks.md#huksauthstoragelevel11)，取值为HUKS\_AUTH\_STORAGE\_LEVEL\_DE（开机后可访问）、HUKS\_AUTH\_STORAGE\_LEVEL\_CE（首次解锁后可访问）、HUKS\_AUTH\_STORAGE\_LEVEL\_ECE（解锁状态时可访问）。 | 否 | 密钥安全等级。 |

### 封装返回结果

封装接口返回[HuksReturnResult](../harmonyos-references/js-apis-huks.md#huksreturnresult9)，其字段如下表所示。

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| outData | Uint8Array | 封装后的密文数据。ML-KEM-768对应784字节密文，ML-KEM-1024对应912字节密文。 |
| sharedSecret | Uint8Array | 共享密钥，长度为32字节。若sharedKeyAlias非空（共享密钥存储到HUKS），此字段为空。 |

## 约束和限制

* 密钥封装和解封装使用的密钥用途必须为[HUKS\_KEY\_PURPOSE\_WRAP](../harmonyos-references/js-apis-huks.md#hukskeypurpose)（封装，公钥操作）和[HUKS\_KEY\_PURPOSE\_UNWRAP](../harmonyos-references/js-apis-huks.md#hukskeypurpose)（解封装，私钥操作）。
* ML-KEM生成的共享密钥长度固定为32字节。
* sharedKeyAlias非空时，sharedKeyParams必须提供且包含共享密钥的必要属性（算法、密钥大小、用途）。
* sharedKeyAlias非空时，若同名密钥已存在且未设置HUKS\_TAG\_KEY\_OVERRIDE为true，将返回错误。
* 使用现有共享密钥别名作为封装结果密钥别名会把现有密钥覆盖。

## 开发步骤

**生成密钥**

设备A、设备B各自生成一个ML-KEM密钥，具体请参考[密钥生成](huks-key-generation-arkts.md)或[密钥导入](huks-key-import-overview.md)。

密钥生成时，密钥用途需设置为HUKS\_KEY\_PURPOSE\_WRAP | HUKS\_KEY\_PURPOSE\_UNWRAP，算法设置为HUKS\_ALG\_ML\_KEM，密钥大小设置为768或1024。

**导出公钥**

设备B导出ML-KEM密钥的公钥，具体请参考[密钥导出](huks-export-key-arkts.md)。导出的公钥为X.509 DER格式。

**密钥封装**

设备A使用设备B的公钥进行密钥封装，生成密文和共享密钥。封装时可将共享密钥存储到HUKS（sharedKeyAlias非空）或返回给调用方（sharedKeyAlias为空）。

**密钥解封装**

设备B使用私钥对密文进行解封装，恢复共享密钥。解封装时可将共享密钥存储到HUKS（sharedKeyAlias非空）或返回给调用方（sharedKeyAlias为空）。

**删除密钥**

当密钥废弃不用时，设备A、B均需要删除密钥，具体请参考[密钥删除](huks-delete-key-arkts.md)。

## 代码示例

在进行密钥封装前，需确保已有ML-KEM密钥，可参考[密钥生成](huks-key-generation-arkts.md)生成密钥，参考[密钥导出](huks-export-key-arkts.md)导出公钥，参考[明文导入密钥](huks-import-key-in-plaintext-arkts.md)导入对端公钥。

### 共享密钥不托管到HUKS的示例

以ML-KEM-768为例，封装时不传入sharedKeyAlias和sharedKeyParams，共享密钥通过返回结果的sharedSecret字段获取。

```ts
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function encapsulateAndDecapsulate() {
  let encapParams: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_ML_KEM,
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_ML_KEM_KEY_PARAM_SET_768,
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_WRAP,
  }];

  let decapParams: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_ML_KEM,
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_ML_KEM_KEY_PARAM_SET_768,
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_UNWRAP,
  }];

  let encapsulatedData = new Uint8Array(0);
  let sharedSecret = new Uint8Array(0);

  /* 设备A：使用对端公钥别名进行封装，不传入sharedKeyAlias和sharedKeyParams */
  try {
    let encapResult = await huks.encapsulate('ml_kem_pub_key_b', encapParams);
    encapsulatedData = encapResult.outData as Uint8Array;
    sharedSecret = encapResult.sharedSecret as Uint8Array;
    console.info(`encapsulate success, encapsulatedData length: ${encapsulatedData.length}`);
  } catch (error) {
    console.error(`encapsulate failed, errCode : ${(error as BusinessError).code}, errMsg : ${(error as BusinessError).message}`);
  }

  /* 设备B：使用私钥别名进行解封装，不传入sharedKeyAlias和sharedKeyParams */
  try {
    let decapResult = await huks.decapsulate('ml_kem_key_b', decapParams, encapsulatedData);
    sharedSecret = decapResult.sharedSecret as Uint8Array;
    console.info(`decapsulate success, sharedSecret length: ${sharedSecret.length}`);
  } catch (error) {
    console.error(`decapsulate failed, errCode : ${(error as BusinessError).code}, errMsg : ${(error as BusinessError).message}`);
  }
}
```

### 共享密钥托管到HUKS的示例

以ML-KEM-768为例，封装和解封装时指定sharedKeyAlias和sharedKeyParams，共享密钥存储到HUKS管理，封装返回结果中sharedSecret为空。

```ts
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function encapsulateAndDecapsulateWithSharedKey() {
  let sharedKeyAliasA = 'ml_kem_shared_key_a';
  let sharedKeyAliasB = 'ml_kem_shared_key_b';

  let sharedKeyProperties: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES,
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256,
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
      huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT,
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_CBC,
  }];

  let encapParams: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_ML_KEM,
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_ML_KEM_KEY_PARAM_SET_768,
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_WRAP,
  }];

  let decapParams: huks.HuksParam[] = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_ML_KEM,
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_ML_KEM_KEY_PARAM_SET_768,
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_UNWRAP,
  }];

  let encapsulatedData = new Uint8Array(0);

  /* 设备A：封装并存储共享密钥到HUKS */
  try {
    let encapResult = await huks.encapsulate('ml_kem_pub_key_b', encapParams, sharedKeyAliasA, sharedKeyProperties);
    encapsulatedData = encapResult.outData as Uint8Array;
    console.info(`encapsulate success, encapsulatedData length: ${encapsulatedData.length}`);
  } catch (error) {
    console.error(`encapsulate failed, errCode : ${(error as BusinessError).code}, errMsg : ${(error as BusinessError).message}`);
  }

  /* 设备B：解封装并存储共享密钥到HUKS */
  try {
    await huks.decapsulate('ml_kem_key_b', decapParams, encapsulatedData, sharedKeyAliasB, sharedKeyProperties);
    console.info(`decapsulate success`);
  } catch (error) {
    console.error(`decapsulate failed, errCode : ${(error as BusinessError).code}, errMsg : ${(error as BusinessError).message}`);
  }
}
```
