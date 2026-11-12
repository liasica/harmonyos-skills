---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-extension-registration-and-unregistration-arkts-ndk
title: CryptoExtensionAbility注册与注销
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 密钥管理扩展 > CryptoExtensionAbility适配 > CryptoExtensionAbility注册与注销
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:41+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:db505231dd110d1d522238a2ca6174c4565f1746b391c8470e78390746cbd89a
---

从API版本22开始，huksExternalCrypto提供Provider注册和注销功能接口，包括ArkTS接口和C++接口。开发者需先实现CryptoExtensionAbility，再通过注册接口接入HUKS后方可使用能力，使用完毕后注销即可断开连接。

## 注册CryptoExtensionAbility

密钥管理扩展应用检测到密钥管理设备或服务可用时，向系统注册CryptoExtensionAbility。具体的可用性检测方式因接入的设备/服务形态而异，例如UKey物理设备监听USB插拔事件。详细规格见[接入能力](huks-extension-ability-support-overview.md#接入能力)。

### 配置CryptoExtensionAbility

在注册CryptoExtensionAbility前，需先在module.json5的[extensionAbilities](module-configuration-file.md#extensionabilities标签)中配置CryptoExtensionAbility。

* name：Ability名称，需与后续注册Provider时传入的[HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_NAME](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)保持一致，最大长度为127字节。
* srcEntry：CryptoExtensionAbility实现类的代码路径。
* type：固定为crypto。
* exported：建议设为false，表示不允许三方应用直接调用。

```json5
// entry/src/main/module.json5
{
  "module": {
    // ...
    "extensionAbilities": [
      {
        "name": "yourCryptoExtensionAbilityName", // 自定义CryptoExtensionAbility名字
        "srcEntry": "./ets/yourAbilitySourcePath",
        "type": "crypto",
        "exported": false
      }
    ],
  }
}
```

**ArkTS接口**

1. 构造注册参数，包含[HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_NAME](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)字段，值为Ability名称的UTF-8字节流，长度为1-128字节。
2. 调用[registerProvider](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptoregisterprovider)接口，需捕获BusinessError处理失败。

**C++接口**

1. 在CMake脚本中链接相关动态库：

   ```txt
   target_link_libraries(entry PUBLIC libhuks_ndk.z.so libhuks_external_crypto.z.so)
   ```
2. 构造注册参数，需要传入[OH\_HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_NAME](../harmonyos-references/capi-native-huks-external-crypto-type-h.md#oh_huks_externalcryptotag)。
3. 调用注册接口[OH\_Huks\_RegisterProvider](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_registerprovider)。

### 开发示例

**ArkTS接口**

```typescript
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

function stringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function registerProvider(): Promise<void> {
  try {
    /* 1.构造注册参数 */
    const providerName = 'testProvider';
    const extProperties: huksExternalCrypto.HuksExternalCryptoParam[] = [
      {
        tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_NAME,
        value: stringToUint8Array('CryptoExtension')
      }
    ];

    /* 2.调用registerProvider */
    await huksExternalCrypto.registerProvider(providerName, extProperties)
      .then(() => {
        console.info('promise: registerProvider success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: registerProvider failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: registerProvider input arg invalid.');
  }
}

async function testRegisterProvider() {
  await registerProvider();
}
```

**C++接口**

以下工具函数被所有示例共用，建议在实际项目中放置于公共源文件：

```
#include "napi/native_api.h"
#include "huks/native_huks_api.h"
#include "huks/native_huks_type.h"
#include "huks/native_huks_param.h"
#include "huks/native_huks_external_crypto_api.h"
#include "huks/native_huks_external_crypto_type.h"
#include <string>

// 初始化参数集
OH_Huks_Result InitParamSet(struct OH_Huks_ExternalCryptoParamSet **paramSet,
    const struct OH_Huks_ExternalCryptoParam *params, uint32_t paramCount)
{
    OH_Huks_Result ret = OH_Huks_InitExternalCryptoParamSet(paramSet);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    ret = OH_Huks_AddExternalCryptoParams(*paramSet, params, paramCount);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        OH_Huks_FreeExternalCryptoParamSet(paramSet);
        return ret;
    }
    ret = OH_Huks_BuildExternalCryptoParamSet(paramSet);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        OH_Huks_FreeExternalCryptoParamSet(paramSet);
        return ret;
    }
    return ret;
}

// 字符串 → Blob
struct OH_Huks_Blob StringToBlob(const std::string &str)
{
    return { (uint32_t)str.size(), (uint8_t *)str.c_str() };
}
```

注册CryptoExtensionAbility：

```
static struct OH_Huks_Blob g_abilityName = {
    (uint32_t)strlen("testAbility"),
    (uint8_t *)"testAbility"
};

static struct OH_Huks_Blob g_providerName = {
    (uint32_t)strlen("testProviderName"),
    (uint8_t *)"testProviderName"
};

static struct OH_Huks_ExternalCryptoParam g_abilityParams[] = {
    {
        .tag = OH_HUKS_EXT_CRYPTO_TAG_ABILITY_NAME,
        .blob = g_abilityName
    },
};

static napi_value registerProvider(napi_env env, napi_callback_info info)
{
    struct OH_Huks_ExternalCryptoParamSet *providerParamSet = nullptr;
    OH_Huks_Result ohResult;
    do {
        ohResult = InitParamSet(&providerParamSet, g_abilityParams,
            sizeof(g_abilityParams) / sizeof(OH_Huks_ExternalCryptoParam));
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        ohResult = OH_Huks_RegisterProvider(&g_providerName, providerParamSet);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
    } while (0);
    OH_Huks_FreeExternalCryptoParamSet(&providerParamSet);

    napi_value ret;
    napi_create_int32(env, ohResult.errorCode, &ret);
    return ret;
}
```

## 注册CryptoExtensionAbility与定制化认证UI

从API版本26.0.0开始，支持同步注册UIAbility到系统中，仅在ArkTS接口下支持。UIAbility由开发者自行实现UI布局与交互逻辑。

从API版本26.0.1开始，新增支持注册[UkeyAuthExtensionAbility](../harmonyos-references/js-apis-ukeyauthextensionability.md#ukeyauthextensionability)，开发者可继承后自行实现UI布局与交互逻辑。注册时通过abilityType字段区分类型：0表示UIAbility类型（不传时默认），1表示UkeyAuthExtensionAbility类型。

两种方式的差异可参考[定制化认证UI](huks-extension-ability-support-overview.md#定制化认证ui)中的对比表。

### 配置定制化认证UI

在注册UIAbility或UkeyAuthExtensionAbility前，需先在module.json5中进行配置。两种Ability的配置位置不同：UIAbility配置在[abilities标签](module-configuration-file.md#abilities标签)中，UkeyAuthExtensionAbility配置在[extensionAbilities标签](module-configuration-file.md#extensionabilities标签)中。

**配置UIAbility**

在abilities标签中配置：

* name：Ability名称，需与注册时[HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_INFO](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)中的abilityName字段保持一致，最大长度为127字节。
* srcEntry：UIAbility实现类的代码路径。
* exported：建议设为true，允许证书管理服务拉起。

```json5
// entry/src/main/module.json5
{
  "module": {
    // ...
    "abilities": [
      {
        "name": "yourUIAbility", // 自定义UIAbility名字
        "srcEntry": "./ets/yourUIAbilitySourcePath",
        "exported": true
      },
    ],
  }
}
```

**配置UkeyAuthExtensionAbility**

在extensionAbilities标签中配置，type固定为ukeyAuth：

* name：Ability名称，需与注册时[HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_INFO](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)中的abilityName字段保持一致，最大长度为127字节。
* srcEntry：UkeyAuthExtensionAbility实现类的代码路径。
* type：固定为ukeyAuth。
* exported：建议设为true，允许证书管理服务拉起。

```json5
// entry/src/main/module.json5
{
  "module": {
    // ...
    "extensionAbilities": [
      {
        "name": "yourUKeyAuthExtensionAbility", // 自定义UkeyAuthExtensionAbility名字
        "srcEntry": "./ets/yourUkeyAuthAbilitySourcePath",
        "type": "ukeyAuth",
        "exported": true
      },
    ],
  }
}
```

### 开发步骤

1. 构造注册参数，包含[HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_NAME](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)字段，值为Ability名称的UTF-8字节流。
2. 构造定制化认证UI注册参数，包含[HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_INFO](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)字段。
3. 调用[registerProvider](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptoregisterprovider)接口，需捕获BusinessError处理失败。

### 开发示例

```typescript
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

interface AbilityInfo {
  abilityName: string;
  index: string;
}

function stringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function registerProvider(): Promise<void> {
  try {
    /* 1.构造注册参数 ability name */
    const providerName = 'testProvider';
    /* 2.构造 ability info */
    const abilityInfoList: AbilityInfo[] = [
      { abilityName: 'UiAbility1', index: '' },
      { abilityName: 'UiAbility2', index: 'string2' },
    ];
    const abilityInfo = JSON.stringify(abilityInfoList);
    const extProperties: huksExternalCrypto.HuksExternalCryptoParam[] = [
      {
        tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_NAME,
        value: stringToUint8Array('CryptoExtension')
      }, {
        tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_INFO,
        value: stringToUint8Array(abilityInfo)
      }
    ];

    /* 3.调用registerProvider */
    await huksExternalCrypto.registerProvider(providerName, extProperties)
      .then(() => {
        console.info('promise: registerProvider success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: registerProvider failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: registerProvider input arg invalid.');
  }
}

async function testRegisterProvider() {
  await registerProvider();
}
```

**注册UkeyAuthExtensionAbility（定制化认证UI）**

从API版本26.0.1开始，开发者可注册UkeyAuthExtensionAbility，使用自行实现的UI布局。注册时abilityType字段需设置为1。

```typescript
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError, deviceInfo } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

// 字符串 → UTF-8字节流
function stringToUint8Array(str: string): Uint8Array {
  return new util.TextEncoder().encodeInto(str);
}

// 定制化认证UI信息
interface AbilityInfo {
  abilityName: string;
  index: string;
  abilityType?: number; // 从API版本26.0.1开始：0=UIAbility, 1=UkeyAuthExtensionAbility，不传则默认0
}

// 注册Provider并注册UkeyAuthExtensionAbility（定制化认证UI）
async function registerProviderWithUkeyAuthExtension(): Promise<void> {
  const providerName = "testProvider";
  const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [
    {
      tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_NAME,
      value: stringToUint8Array("CryptoExtension")
    }
  ];

  // API版本26.0.1开始，支持注册UkeyAuthExtensionAbility
  if (deviceInfo.sdkApiVersion > 26 ||
    (deviceInfo.sdkApiVersion === 26 && deviceInfo.sdkPatchApiVersion >= 1)) {
    const abilityInfoList: AbilityInfo[] = [
      // abilityType=1 表示UkeyAuthExtensionAbility类型
      { abilityName: 'UkeyAuthExtensionAbility1', index: '', abilityType: 1 },
    ];

    extProperties.push({
      tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_INFO,
      value: stringToUint8Array(JSON.stringify(abilityInfoList)),
    });
  }

  try {
    await huksExternalCrypto.registerProvider(providerName, extProperties);
    console.info('promise: registerProvider with UkeyAuthExtensionAbility success.');
  } catch (error) {
    const e = error as BusinessError;
    console.error(`promise: registerProvider failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
}

async function testRegisterProviderWithUkeyAuthExtension(): Promise<void> {
  await registerProviderWithUkeyAuthExtension();
}
```

## 注销CryptoExtensionAbility

密钥管理扩展应用检测到密钥管理设备或服务不可用时，从系统注销CryptoExtensionAbility。具体的可用性检测方式因接入的设备/服务形态而异，例如UKey物理设备监听USB插拔事件、数字盾（虚拟智能卡）在应用退出时检测。详细规格见[接入能力](huks-extension-ability-support-overview.md#接入能力)。

### 开发步骤

**ArkTS接口**

1. 构造注销参数，注销单个ability需要传入[HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_NAME](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数。批量注销不需要传入[HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_NAME](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数。
2. 调用注销接口[unregisterProvider](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptounregisterprovider)。

**C++接口**

1. 在CMake脚本中链接相关动态库：

   ```txt
   target_link_libraries(entry PUBLIC libhuks_ndk.z.so libhuks_external_crypto.z.so)
   ```
2. 构造注销参数，注销单个ability需要传入[OH\_HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_NAME](../harmonyos-references/capi-native-huks-external-crypto-type-h.md#oh_huks_externalcryptotag)。批量注销不需要传入[OH\_HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_NAME](../harmonyos-references/capi-native-huks-external-crypto-type-h.md#oh_huks_externalcryptotag)。
3. 调用注销接口[OH\_Huks\_UnregisterProvider](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_unregisterprovider)。

### 开发示例

**ArkTS接口**

**注销单个ability**

```typescript
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

function stringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function unregisterProvider(): Promise<void> {
  try {
    /* 1.构造注销参数 */
    const providerName = 'testProvider';
    const extProperties: huksExternalCrypto.HuksExternalCryptoParam[] = [
      {
        tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_NAME,
        value: stringToUint8Array('CryptoExtension')
      }
    ];

    /* 2.调用unregisterProvider */
    await huksExternalCrypto.unregisterProvider(providerName, extProperties)
      .then(() => {
        console.info('promise: unregisterProvider success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: unregisterProvider failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: unregisterProvider input arg invalid.');
  }
}

async function testRegisterProvider() {
  await unregisterProvider();
}
```

**批量注销**

```typescript
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function unregisterProvider(): Promise<void> {
  try {
    /* 1.构造注销参数 */
    const providerName = 'testProvider';
    const extProperties: huksExternalCrypto.HuksExternalCryptoParam[] = [];

    /* 2.调用unregisterProvider */
    await huksExternalCrypto.unregisterProvider(providerName, extProperties)
      .then(() => {
        console.info('promise: unregisterProvider success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: unregisterProvider failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: unregisterProvider input arg invalid.');
  }
}

async function testRegisterProvider() {
  await unregisterProvider();
}
```

**C++接口**

以下工具函数被所有示例共用，建议在实际项目中放置于公共源文件：

```
#include "napi/native_api.h"
#include "huks/native_huks_api.h"
#include "huks/native_huks_type.h"
#include "huks/native_huks_param.h"
#include "huks/native_huks_external_crypto_api.h"
#include "huks/native_huks_external_crypto_type.h"
#include <string>

// 初始化参数集
OH_Huks_Result InitParamSet(struct OH_Huks_ExternalCryptoParamSet **paramSet, const struct OH_Huks_ExternalCryptoParam *params, uint32_t paramCount)
{
    OH_Huks_Result ret = OH_Huks_InitExternalCryptoParamSet(paramSet);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    ret = OH_Huks_AddExternalCryptoParams(*paramSet, params, paramCount);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        OH_Huks_FreeExternalCryptoParamSet(paramSet);
        return ret;
    }
    ret = OH_Huks_BuildExternalCryptoParamSet(paramSet);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        OH_Huks_FreeExternalCryptoParamSet(paramSet);
        return ret;
    }
    return ret;
}

// 字符串 → Blob
struct OH_Huks_Blob StringToBlob(const std::string &str)
{
    return { (uint32_t)str.size(), (uint8_t *)str.c_str() };
}
```

**注销单个ability：**

```
static napi_value unregisterSingleProvider(napi_env env, napi_callback_info info)
{
    struct OH_Huks_ExternalCryptoParamSet *providerParamSet = nullptr;
    OH_Huks_Result ohResult;
    do {
        ohResult = InitParamSet(&providerParamSet, g_abilityParams,
            sizeof(g_abilityParams) / sizeof(OH_Huks_ExternalCryptoParam));
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        ohResult = OH_Huks_UnregisterProvider(&g_providerName, providerParamSet);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
    } while (0);
    OH_Huks_FreeExternalCryptoParamSet(&providerParamSet);

    napi_value ret;
    napi_create_int32(env, ohResult.errorCode, &ret);
    return ret;
}
```

**批量注销：**

```
static struct OH_Huks_ExternalCryptoParam g_emptyAbilityParams[] = {};

static napi_value unregisterAllProvider(napi_env env, napi_callback_info info)
{
    struct OH_Huks_ExternalCryptoParamSet *providerParamSet = nullptr;
    OH_Huks_Result ohResult;
    do {
        ohResult = InitParamSet(&providerParamSet, g_emptyAbilityParams,
            sizeof(g_emptyAbilityParams) / sizeof(OH_Huks_ExternalCryptoParam));
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        ohResult = OH_Huks_UnregisterProvider(&g_providerName, providerParamSet);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
    } while (0);
    OH_Huks_FreeExternalCryptoParamSet(&providerParamSet);

    napi_value ret;
    napi_create_int32(env, ohResult.errorCode, &ret);
    return ret;
}
```
