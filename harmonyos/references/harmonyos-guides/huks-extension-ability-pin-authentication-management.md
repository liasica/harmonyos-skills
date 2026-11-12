---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-extension-ability-pin-authentication-management
title: PIN码访问控制
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 密钥管理扩展 > 密钥管理扩展使用 > PIN码访问控制
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:41+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:2498473d40cdf1cc9ce67ecfe542a3f665b8a1b56e0f4aa28693bd95304bdb57
---

PIN（Personal Identification Number）码是密钥管理扩展服务中的安全访问凭证，服务实现方可以采用“凭证+PIN码”的双因子认证模式：用户必须同时拥有有效的凭证（如物理设备、虚拟服务会话等）和正确的PIN码，才能访问服务内的密钥材料。

PIN码作用如下：

1. 防暴力破解：连续错误输入达到一定次数（与密钥管理扩展服务实现相关）后自动锁定，通过[onAuthUkeyPin](../harmonyos-references/js-apis-cryptoextensionability.md#onauthukeypin)返回值中的retryCount字段查询剩余重试次数。
2. 硬件级安全：PIN码验证在密钥管理扩展服务内完成，敏感信息不离开服务。

密钥管理扩展服务使用resourceId标识资源，生态应用打开资源之后，如需要操作resourceId对应的私钥执行签名操作，则需要先验证PIN码。

## PIN码认证状态管理

HUKS提供以下PIN码认证状态管理能力：

* **查询认证状态**：从API版本22开始，可通过[getUkeyPinAuthState](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptogetukeypinauthstate)查询当前PIN码认证状态。
* **清除认证状态**：从API版本26.0.0开始，可通过[clearUkeyPinAuthState](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptoclearukeypinauthstate)清除指定资源的PIN码认证状态。

**说明** 

HUKS提供PIN码认证能力和认证状态查询能力。应用PIN码认证之前，可以先查询认证状态。如果需要PIN码认证，则需要拉起[证书管理应用](certmanager-overview.md)，完成PIN码认证。

## 查询认证状态

应用可以通过对应接口查询PIN码是否认证通过。

### 开发步骤

**ArkTS接口**

1. 通过[获取资源ID](huks-extension-ability-general-operation.md#获取资源id)操作，得到resourceId，并传入该resourceId进行打开资源，可参考[打开关闭资源](huks-extension-ability-general-operation.md#打开关闭资源)。
2. 调用查询认证状态接口[getUkeyPinAuthState](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptogetukeypinauthstate)验证PIN码。
3. 操作执行完后，关闭资源，可参考[打开关闭资源](huks-extension-ability-general-operation.md#打开关闭资源)。

**C++接口**

1. 在CMake脚本中链接相关动态库：

   ```txt
   target_link_libraries(entry PUBLIC libhuks_ndk.z.so libhuks_external_crypto.z.so)
   ```
2. 通过[获取资源ID](huks-extension-ability-general-operation.md#获取资源id)中的证书管理途径获取resourceId，并传入该resourceId进行打开资源，可参考[打开关闭资源](huks-extension-ability-general-operation.md#打开关闭资源)。
3. 调用[OH\_Huks\_InitExternalCryptoParamSet](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_initexternalcryptoparamset)指定参数配置。
4. 调用[OH\_Huks\_GetUkeyPinAuthState](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_getukeypinauthstate)获取PIN码认证状态。
5. 操作执行完后，关闭资源，可参考[打开关闭资源](huks-extension-ability-general-operation.md#打开关闭资源)。

### 开发示例

**ArkTS接口**

```typescript
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function getUkeyPinAuthState(): Promise<huksExternalCrypto.HuksExternalPinAuthState> {
  let ret: huksExternalCrypto.HuksExternalPinAuthState =
    huksExternalCrypto.HuksExternalPinAuthState.HUKS_EXT_CRYPTO_PIN_NO_AUTH;
  try {
    /* 1.构造查询PIN码状态参数 */
    const testResourceId = JSON.stringify({
      providerName: 'testProviderName',
      bundleName: 'com.example.cryptoapplication',
      abilityName: 'CryptoExtension',
      index: {
        key: 'testKey'
      } as ESObject
    });
    const extProperties: huksExternalCrypto.HuksExternalCryptoParam[] = [];

    /* 2.调用getUkeyPinAuthState */
    await huksExternalCrypto.getUkeyPinAuthState(testResourceId, extProperties)
      .then((data) => {
        console.info(`promise: getUkeyPinAuthState success , data : ${data}`);
      }).catch((error: BusinessError) => {
        console.error(`promise: getUkeyPinAuthState failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: getUkeyPinAuthState input arg invalid.');
  }
  return ret;
}

async function testGetUkeyPinAuthState() {
  let ret: huksExternalCrypto.HuksExternalPinAuthState = await getUkeyPinAuthState();
  if (ret != huksExternalCrypto.HuksExternalPinAuthState.HUKS_EXT_CRYPTO_PIN_AUTH_SUCCEEDED) {
    console.error('getUkeyPinAuthState failed.');
    return;
  }

  console.info('getUkeyPinAuthState success.');
}
```

**C++接口**

```
static const char *QUERY_RESOURCE_ID =
    "{\"providerName\":\"testProviderName\","
    "\"abilityName\":\"CryptoExtension\","
    "\"bundleName\":\"com.example.cryptoapplication\","
    "\"index\":{\"key\":\"testKey\"}}";

static struct OH_Huks_ExternalCryptoParam g_getPinStateParamsTest[] = {};

static napi_value GetUkeyPinAuthState(napi_env env, napi_callback_info info)
{
    struct OH_Huks_Blob g_resourceId = {
        (uint32_t)strlen(QUERY_RESOURCE_ID),
        (uint8_t *)QUERY_RESOURCE_ID
    };
    struct OH_Huks_ExternalCryptoParamSet *pinStateParamSet = nullptr;
    OH_Huks_ExternalPinAuthState authState = OH_HUKS_EXT_CRYPTO_PIN_NO_AUTH;
    OH_Huks_Result ohResult;
    do {
        ohResult = InitParamSet(&pinStateParamSet, g_getPinStateParamsTest,
            sizeof(g_getPinStateParamsTest) / sizeof(OH_Huks_ExternalCryptoParam));
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        ohResult = OH_Huks_GetUkeyPinAuthState(&g_resourceId, pinStateParamSet, &authState);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
    } while (0);
    OH_Huks_FreeExternalCryptoParamSet(&pinStateParamSet);

    napi_value ret;
    napi_create_int32(env, ohResult.errorCode, &ret);
    return ret;
}
```

## 清除认证状态

应用在密钥操作完成后或需要重置认证状态时，可以调用对应接口清除指定资源的PIN码认证状态。

### 使用场景

以下场景可能需要清除PIN码认证状态：

* 密钥操作完成后，主动清除认证状态，避免认证状态残留。
* 应用退出或切换用户时，清除认证状态。
* 认证状态异常时，重置认证状态。

### 开发步骤

1. 通过[获取资源ID](huks-extension-ability-general-operation.md#获取资源id)操作，得到resourceId，并传入该resourceId进行打开资源，可参考[打开关闭资源](huks-extension-ability-general-operation.md#打开关闭资源)。
2. 调用[clearUkeyPinAuthState](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptoclearukeypinauthstate)清除PIN码认证状态。
3. 操作执行完后，关闭资源，可参考[打开关闭资源](huks-extension-ability-general-operation.md#打开关闭资源)。

### 开发示例

```typescript
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 清除PIN码认证状态
async function clearUkeyPinAuthState(resourceId: string): Promise<void> {
  try {
    await huksExternalCrypto.clearUkeyPinAuthState(resourceId)
      .then(() => {
        console.info('promise: clearUkeyPinAuthState success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: clearUkeyPinAuthState failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: clearUkeyPinAuthState input arg invalid.');
  }
}
```
