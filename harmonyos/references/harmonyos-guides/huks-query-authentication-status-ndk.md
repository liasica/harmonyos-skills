---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-query-authentication-status-ndk
title: 查询认证状态(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > UKeyPIN码认证管理 > 查询认证状态(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:c198240a6ec6c66dece0ceabee61d2b0bf061c087cd0baa2edfc19c2ff331e7e
---

从API 22开始，huksExternalCrypto提供PIN码认证状态查询功能接口。应用可以通过该接口查询PIN码是否认证通过。具体的场景介绍及规格，请参考[UKey PIN码认证介绍及规格](huks-ukey-pin-authentication-management-overview.md)。

## 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libhuks_ndk.z.so libhuks_external_crypto.z.so)
```

## 开发步骤

1. 通过证书管理系统能力提供的[openAuthorizeDialog](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取[keyUri](../harmonyos-references/js-apis-certmanagerdialog.md#certreference22)，并将其作为resourceId。
2. 调用[OH\_Huks\_InitExternalCryptoParamSet](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_initexternalcryptoparamset)指定参数配置。
3. 调用[OH\_Huks\_GetUkeyPinAuthState](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_getukeypinauthstate)获取PIN码认证状态。

## 开发案例

```
#include "huks/native_huks_external_crypto_api.h"
#include "huks/native_huks_param.h"
#include "napi/native_api.h"
#include <string.h>

OH_Huks_Result InitParamSet(
    struct OH_Huks_ExternalCryptoParamSet **paramSet,
    const struct OH_Huks_ExternalCryptoParam *params,
    uint32_t paramCount)
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

static const char *resourceId = "{\"providerName\":\"testProviderName\",\"abilityName\":\"CryptoExtension\",\"bundleName\":\"com.example.cryptoapplication\",\"index\":{\"key\":\"testKey\"}}";

static struct OH_Huks_ExternalCryptoParam g_getPinStateParamsTest[] = {};

static napi_value GetUkeyPinAuthState(napi_env env, napi_callback_info info)
{
    struct OH_Huks_Blob g_resourceId = {
        (uint32_t)strlen(resourceId),
        (uint8_t *)resourceId
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
