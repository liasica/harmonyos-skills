---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-cmac-native
title: CMAC(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > CMAC > CMAC(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5743f3d98f0beef8cd8eb1a17ad761c990aff749658bdb2d250453c7026967d8
---

CMAC是基于对称密钥分组加密算法的消息认证码（Cipher-based Message Authentication Code），目前支持3DES加密算法的消息认证方法。

**说明** 

仅支持在智能穿戴设备（Wearable）使用。

## 开发步骤

**生成密钥**

1. 获取生成密钥算法参数配置。
2. 调用[OH\_Huks\_GenerateKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_generatekeyitem)生成密钥，支持的规格是128比特长度的密钥。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md#支持的算法)的规格介绍，导入已有的密钥。

**执行CMAC**

1. 调用[OH\_Huks\_InitParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_initparamset)获取算法参数配置。
2. 调用[OH\_Huks\_InitSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_initsession)和[OH\_Huks\_FinishSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_finishsession)计算MAC值。

```
#include "huks/native_huks_api.h"
#include "huks/native_huks_param.h"
#include "huks/native_huks_type.h"
#include "napi/native_api.h"
#include <string.h>

static const uint32_t CMAC_COMMON_SIZE = 8;
static const uint32_t IV_SIZE = 8;
static uint8_t IV[IV_SIZE] = { 0 };

OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params, uint32_t paramCount)
{
    OH_Huks_Result ret = OH_Huks_InitParamSet(paramSet);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    ret = OH_Huks_AddParams(*paramSet, params, paramCount);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        OH_Huks_FreeParamSet(paramSet);
        return ret;
    }
    ret = OH_Huks_BuildParamSet(paramSet);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        OH_Huks_FreeParamSet(paramSet);
        return ret;
    }
    return ret;
}

static struct OH_Huks_Param g_genParams[] = {
    {
        .tag = OH_HUKS_TAG_ALGORITHM,
        .uint32Param = OH_HUKS_ALG_3DES
    }, {
        .tag = OH_HUKS_TAG_KEY_SIZE,
        .uint32Param = OH_HUKS_3DES_KEY_SIZE_128
    }, {
        .tag = OH_HUKS_TAG_PURPOSE,
        .uint32Param = OH_HUKS_KEY_PURPOSE_MAC
    }
};

static struct OH_Huks_Param g_cmacParams[] = {
    {
        .tag = OH_HUKS_TAG_ALGORITHM,
        .uint32Param = OH_HUKS_ALG_CMAC
    }, {
        .tag = OH_HUKS_TAG_KEY_SIZE,
        .uint32Param = OH_HUKS_3DES_KEY_SIZE_128
    }, {
        .tag = OH_HUKS_TAG_PURPOSE,
        .uint32Param = OH_HUKS_KEY_PURPOSE_MAC
    }, {
        .tag = OH_HUKS_TAG_BLOCK_MODE,
        .uint32Param = OH_HUKS_MODE_CBC
    }, {
        .tag = OH_HUKS_TAG_PADDING,
        .uint32Param = OH_HUKS_PADDING_ISO_IEC_9797_1
    }, {
        .tag = OH_HUKS_TAG_IV,
        .blob = {
            .size = IV_SIZE,
            .data = (uint8_t *)IV
        }
    }
};

OH_Huks_Result HksCmacTest(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *cmacParamSet,
    const struct OH_Huks_Blob *inData, struct OH_Huks_Blob *outData)
{
    uint8_t handleE[sizeof(uint64_t)] = {0};
    struct OH_Huks_Blob handle = {sizeof(uint64_t), handleE};
    OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, cmacParamSet, &handle, nullptr);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    ret = OH_Huks_FinishSession(&handle, cmacParamSet, inData, outData);
    return ret;
}

static napi_value CmacKey(napi_env env, napi_callback_info info)
{
    char tmpKeyAlias[] = "test_cmac";
    struct OH_Huks_Blob keyAlias = { (uint32_t)strlen(tmpKeyAlias), (uint8_t *)tmpKeyAlias };
    struct OH_Huks_ParamSet *genParamSet = nullptr;
    struct OH_Huks_ParamSet *cmacParamSet = nullptr;
    OH_Huks_Result ohResult;
    do {
      /*       * 1.1 获取生成密钥算法参数配置       */
        ohResult = InitParamSet(&genParamSet, g_genParams, sizeof(g_genParams) / sizeof(OH_Huks_Param));
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
       /*               * 1.2 调用OH_Huks_GenerateKeyItem        */
        ohResult = OH_Huks_GenerateKeyItem(&keyAlias, genParamSet, nullptr);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
       /*        * 2.1. 获取CMAC算法参数配置        */
        char tmpInData[] = "CMAC_INDATA";
        struct OH_Huks_Blob inData = { (uint32_t)strlen(tmpInData), (uint8_t *)tmpInData };
        uint8_t mac[CMAC_COMMON_SIZE] = { 0 };
        struct OH_Huks_Blob macData= {CMAC_COMMON_SIZE, mac};
        ohResult = InitParamSet(&cmacParamSet, g_cmacParams, sizeof(g_cmacParams) / sizeof(OH_Huks_Param));
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
       /*        * 2.2 调用initSession和finishSession计算MAC        */
        ohResult = HksCmacTest(&keyAlias, cmacParamSet, &inData, &macData);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
    } while (0);
    OH_Huks_FreeParamSet(&genParamSet);
    OH_Huks_FreeParamSet(&cmacParamSet);
    
    napi_value ret;
    napi_create_int32(env, ohResult.errorCode, &ret);
    return ret;
}
```
