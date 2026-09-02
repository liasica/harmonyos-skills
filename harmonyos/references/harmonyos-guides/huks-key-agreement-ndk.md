---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-agreement-ndk
title: 密钥协商(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 密钥协商 > 密钥协商(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:904e0d803403442783db780f7d051ab4865cd104174d5970e604af8f369abd5f
---

以X25519、DH和ECDH协商密钥类型为例，在密钥由HUKS管理的情况下，完成密钥协商。具体的场景介绍及支持的算法规格，请参考[密钥协商支持的算法](huks-key-agreement-overview.md#支持的算法)。

## 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

## 开发步骤

**生成密钥**

设备A、设备B各自生成一个非对称密钥，具体请参考[密钥生成](huks-key-generation-overview.md)或[密钥导入](huks-key-import-overview.md)。

密钥生成时，可指定参数，OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG（可选），用于标识此步骤生成的密钥是否由HUKS管理。

**导出密钥**

设备A、B导出非对称密钥对的公钥材料，具体请参考[密钥导出](huks-export-key-arkts.md)。

**密钥协商**

设备A、B分别基于本端私钥和对端设备的公钥，协商出共享密钥。

密钥协商时，可指定参数OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG（可选），用于标识协商得到的密钥是否由HUKS管理。

* 当TAG设置为OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS时，表示基于该密钥协商出的密钥，由HUKS管理，可保证协商密钥全生命周期不出安全环境。
* 当TAG设置为OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED时，表示基于该密钥协商出的密钥，返回给调用方管理，由业务自行保证密钥安全。
* 若业务未设置TAG的具体值，表示基于该密钥协商出的密钥，既可由HUKS管理，也可返回给调用方管理，业务可在后续协商时再选择使用何种方式保护密钥。

| 生成 | 协商 | 规格 |
| --- | --- | --- |
| OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | 密钥由HUKS管理 |
| OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | 密钥返回给调用方管理 |
| 未指定TAG具体值 | OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | 密钥由HUKS管理 |
| 未指定TAG具体值 | OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | 密钥返回给调用方管理 |
| 未指定TAG具体值 | 未指定TAG具体值 | 密钥返回给调用方管理 |

注：协商时指定的TAG值，不可与生成时指定的TAG值冲突。表格中仅列举有效的指定方式。

**删除密钥**

当密钥废弃不用时，设备A、B均需要删除密钥，具体请参考[密钥删除](huks-delete-key-ndk.md)。

## 开发案例

下面分别以X25519、DH和ECDH密钥为例，进行协商。

### X25519非对称密钥协商用例

准备X25519密钥协商材料：

```
#include "huks/native_huks_api.h"
#include "huks/native_huks_param.h"
#include "napi/native_api.h"
#include <cstring>
#include "file.h"

/* 初始化参数 */
static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
    uint32_t paramCount)
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
static struct OH_Huks_Blob g_keyAliasFinal1001 = {(uint32_t)strlen("HksECDHAgreeKeyAliasTest001_1_final"),
                                                  (uint8_t *)"HksECDHAgreeKeyAliasTest001_1_final"};
/* 集成密钥参数集 */
static struct OH_Huks_Param g_genAgreeParams[] = {
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_X25519},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_CURVE25519_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};
static struct OH_Huks_Param g_agreeParamsInit01[] = {
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_X25519},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_CURVE25519_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};
static struct OH_Huks_Param g_agreeParamsFinish01[] = {
    {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_ONLY_USED_IN_HUKS},
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_keyAliasFinal1001},
    {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
    {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
    {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};
static struct OH_Huks_Blob g_keyAliasFinal2001 = {(uint32_t)strlen("HksX25519AgreeKeyAliasTest001_2_final"),
                                                  (uint8_t *)"HksX25519AgreeKeyAliasTest001_2_final"};
static struct OH_Huks_Param g_agreeParamsInit02[] = {
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_X25519},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_CURVE25519_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};
static struct OH_Huks_Param g_agreeParamsFinish02[] = {
    {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_ONLY_USED_IN_HUKS},
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_keyAliasFinal2001},
    {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
    {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
    {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};
static const uint32_t X25519_COMMON_SIZE = 256;
static struct OH_Huks_Blob g_keyAlias01001 = {(uint32_t)strlen("HksX25519AgreeKeyAliasTest001_1"),
                                              (uint8_t *)"HksX25519AgreeKeyAliasTest001_1"};
static struct OH_Huks_Blob g_keyAlias02001 = {(uint32_t)strlen("HksX25519AgreeKeyAliasTest001_2"),
                                              (uint8_t *)"HksX25519AgreeKeyAliasTest001_2"};
```

执行密钥协商：

```
/* 导出密钥 */
OH_Huks_Result HksX25519AgreeExport(const struct OH_Huks_Blob *keyAlias1, const struct OH_Huks_Blob *keyAlias2,
    struct OH_Huks_Blob *publicKey1, struct OH_Huks_Blob *publicKey2,
    const struct OH_Huks_ParamSet *genParamSet)
{
    OH_Huks_Result ret = OH_Huks_ExportPublicKeyItem(keyAlias1, genParamSet, publicKey1);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    ret = OH_Huks_ExportPublicKeyItem(keyAlias2, genParamSet, publicKey2);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    return ret;
}
static const char *IN_DATA = "Hks_X25519_Agree_Test";
/* 协商密钥操作 */
OH_Huks_Result HksX25519AgreeFinish(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_Blob *publicKey,
    const struct OH_Huks_ParamSet *initParamSet,
    const struct OH_Huks_ParamSet *finishParamSet, struct OH_Huks_Blob *outData)
{
    struct OH_Huks_Blob inData = {(uint32_t)strlen(IN_DATA), (uint8_t *)IN_DATA};
    uint8_t handleU[sizeof(uint64_t)] = {0};
    struct OH_Huks_Blob handle = {sizeof(uint64_t), handleU};
    OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, initParamSet, &handle, nullptr);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    uint8_t outDataU[X25519_COMMON_SIZE] = {0};
    struct OH_Huks_Blob outDataUpdate = {X25519_COMMON_SIZE, outDataU};
    ret = OH_Huks_UpdateSession(&handle, initParamSet, publicKey, &outDataUpdate);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    ret = OH_Huks_FinishSession(&handle, finishParamSet, &inData, outData);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    return ret;
}

static OH_Huks_Result InitializeAgreeParamSets(struct OH_Huks_ParamSet **genParamSet,
    struct OH_Huks_ParamSet **initParamSet01,
    struct OH_Huks_ParamSet **finishParamSet01,
    struct OH_Huks_ParamSet **initParamSet02,
    struct OH_Huks_ParamSet **finishParamSet02)
{
    OH_Huks_Result ohResult;
    
    ohResult = InitParamSet(genParamSet, g_genAgreeParams,
                            sizeof(g_genAgreeParams) / sizeof(OH_Huks_Param));
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(initParamSet01, g_agreeParamsInit01,
                            sizeof(g_agreeParamsInit01) / sizeof(OH_Huks_Param));
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(finishParamSet01, g_agreeParamsFinish01,
                            sizeof(g_agreeParamsFinish01) / sizeof(OH_Huks_Param));
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(initParamSet02, g_agreeParamsInit02,
                            sizeof(g_agreeParamsInit02) / sizeof(OH_Huks_Param));
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(finishParamSet02, g_agreeParamsFinish02,
                            sizeof(g_agreeParamsFinish02) / sizeof(OH_Huks_Param));
    return ohResult;
}

static OH_Huks_Result GenerateKeyPair(struct OH_Huks_ParamSet *genParamSet)
{
    OH_Huks_Result ohResult;
    
    /* 设备A生成密钥 */
    ohResult = OH_Huks_GenerateKeyItem(&g_keyAlias01001, genParamSet, nullptr);
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        return ohResult;
    }
    
    /* 设备B生成密钥 */
    ohResult = OH_Huks_GenerateKeyItem(&g_keyAlias02001, genParamSet, nullptr);
    return ohResult;
}

static OH_Huks_Result KeyAgreement(struct OH_Huks_Blob *g_keyAlias,
    struct OH_Huks_Blob *publicKey,
    struct OH_Huks_Blob *outData,
    struct OH_Huks_ParamSet *initParamSet,
    struct OH_Huks_ParamSet *finishParamSet)
{
    OH_Huks_Result ohResult;
    
    ohResult = MallocAndCheckBlobData(outData, outData->size);
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        return ohResult;
    }
    /* 协商密钥 */
    ohResult = HksX25519AgreeFinish(g_keyAlias, publicKey, initParamSet, finishParamSet, outData);
    return ohResult;
}

static void CleanKey(struct OH_Huks_Blob *genKeyAlias,
    struct OH_Huks_Blob *genKeyAliasFinal,
    struct OH_Huks_ParamSet *genParamSet,
    struct OH_Huks_ParamSet **initParamSet,
    struct OH_Huks_ParamSet **finishParamSet)
{
    OH_Huks_DeleteKeyItem(genKeyAlias, genParamSet);
    OH_Huks_DeleteKeyItem(genKeyAliasFinal, NULL);
    OH_Huks_FreeParamSet(initParamSet);
    OH_Huks_FreeParamSet(finishParamSet);
}

/* 协商密钥整体流程 */
napi_value X25519AgreeKey(napi_env env, napi_callback_info info)
{
    struct OH_Huks_ParamSet *genParamSet = nullptr;
    struct OH_Huks_ParamSet *initParamSet01 = nullptr;
    struct OH_Huks_ParamSet *finishParamSet01 = nullptr;
    struct OH_Huks_ParamSet *initParamSet02 = nullptr;
    struct OH_Huks_ParamSet *finishParamSet02 = nullptr;
    struct OH_Huks_Blob publicKey01 = {.size = OH_HUKS_AES_KEY_SIZE_256, .data = nullptr};
    struct OH_Huks_Blob publicKey02 = {.size = OH_HUKS_AES_KEY_SIZE_256, .data = nullptr};
    struct OH_Huks_Blob outData01 = {.size = X25519_COMMON_SIZE, .data = nullptr};
    struct OH_Huks_Blob outData02 = {.size = X25519_COMMON_SIZE, .data = nullptr};
    OH_Huks_Result ohResult;
    do {
        /* 1.确定密钥别名集成密钥参数集 */
        ohResult = InitializeAgreeParamSets(&genParamSet, &initParamSet01, &finishParamSet01,
                                            &initParamSet02, &finishParamSet02);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        /* 2.设备A和设备B生成密钥 */
        ohResult = GenerateKeyPair(genParamSet);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        ohResult = MallocAndCheckBlobData(&publicKey01, publicKey01.size);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        ohResult = MallocAndCheckBlobData(&publicKey02, publicKey02.size);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        /* 3.设备A、B导出公钥 */
        ohResult = HksX25519AgreeExport(&g_keyAlias01001, &g_keyAlias02001, &publicKey01, &publicKey02, genParamSet);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        /* 4.设备A、B执行密钥协商 */
        ohResult = KeyAgreement(&g_keyAlias01001, &publicKey02, &outData01, initParamSet01, finishParamSet01);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        ohResult = KeyAgreement(&g_keyAlias02001, &publicKey01, &outData02, initParamSet02, finishParamSet02);
    } while (0);
    free(publicKey01.data);
    free(publicKey02.data);
    free(outData01.data);
    free(outData02.data);
    /* 5.设备A、B删除密钥 */
    CleanKey(&g_keyAlias01001, &g_keyAliasFinal1001, genParamSet, &initParamSet01, &finishParamSet01);
    CleanKey(&g_keyAlias02001, &g_keyAliasFinal2001, genParamSet, &initParamSet02, &finishParamSet02);
    OH_Huks_FreeParamSet(&genParamSet);

    napi_value ret;
    napi_create_int32(env, ohResult.errorCode, &ret);
    return ret;
}
```

### DH密钥协商用例

准备DH密钥协商材料：

```
#include "huks/native_huks_api.h"
#include "huks/native_huks_param.h"
#include "napi/native_api.h"
#include <cstring>
#include "file.h"

/* 初始化参数 */
static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
    uint32_t paramCount)
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
static struct OH_Huks_Blob g_keyAliasFinal1001 = {(uint32_t)strlen("HksDHAgreeKeyAliasTest001_1_final"),
                                                  (uint8_t *)"HksDHAgreeKeyAliasTest001_1_final"};
/* 集成密钥参数集 */
static struct OH_Huks_Param g_genAgreeParams[] = {
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_DH},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_DH_KEY_SIZE_2048}};
static struct OH_Huks_Param g_agreeParamsInit01[] = {
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_DH},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_DH_KEY_SIZE_2048}};
static struct OH_Huks_Param g_agreeParamsFinish01[] = {
    {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_KEY_EXPORT_ALLOWED},
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_keyAliasFinal1001},
    {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
    {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
    {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};
static struct OH_Huks_Param g_agreeParamsFinish01_2[] = {
    {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_ONLY_USED_IN_HUKS},
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_keyAliasFinal1001},
    {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
    {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
    {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};
static struct OH_Huks_Blob g_keyAliasFinal2001 = {(uint32_t)strlen("HksDHAgreeKeyAliasTest001_2_final"),
                                                  (uint8_t *)"HksDHAgreeKeyAliasTest001_2_final"};
static struct OH_Huks_Param g_agreeParamsInit02[] = {
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_DH},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_DH_KEY_SIZE_2048}};
static struct OH_Huks_Param g_agreeParamsFinish02[] = {
    {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_KEY_EXPORT_ALLOWED},
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_keyAliasFinal2001},
    {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
    {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
    {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};
static struct OH_Huks_Param g_agreeParamsFinish02_2[] = {
    {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_ONLY_USED_IN_HUKS},
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_keyAliasFinal2001},
    {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
    {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
    {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};
static const uint32_t DH_COMMON_SIZE = 2048;
static struct OH_Huks_Blob g_keyAlias01001 = {(uint32_t)strlen("HksDHAgreeKeyAliasTest001_1"),
                                              (uint8_t *)"HksDHAgreeKeyAliasTest001_1"};
static struct OH_Huks_Blob g_keyAlias02001 = {(uint32_t)strlen("HksDHAgreeKeyAliasTest001_2"),
                                              (uint8_t *)"HksDHAgreeKeyAliasTest001_2"};
```

执行密钥协商：

```
static OH_Huks_Result MallocAndCheckBlobData(struct OH_Huks_Blob *blob, const uint32_t blobSize)
{
    struct OH_Huks_Result ret;
    ret.errorCode = OH_HUKS_SUCCESS;
    if (blobSize == 0 || blobSize > DH_COMMON_SIZE) {
        ret.errorCode = OH_HUKS_ERR_CODE_INTERNAL_ERROR;
        return ret;
    }
    blob->data = (uint8_t *)malloc(blobSize);
    if (blob->data == NULL) {
        ret.errorCode = OH_HUKS_ERR_CODE_INTERNAL_ERROR;
    }
    return ret;
}
/* 导出密钥 */
OH_Huks_Result HksDHAgreeExport(const struct OH_Huks_Blob *keyAlias1, const struct OH_Huks_Blob *keyAlias2,
    struct OH_Huks_Blob *publicKey1, struct OH_Huks_Blob *publicKey2,
    const struct OH_Huks_ParamSet *genParamSet)
{
    OH_Huks_Result ret = OH_Huks_ExportPublicKeyItem(keyAlias1, genParamSet, publicKey1);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    ret = OH_Huks_ExportPublicKeyItem(keyAlias2, genParamSet, publicKey2);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    return ret;
}
static const char *IN_DATA = "Hks_DH_Agree_Test";
/* 协商密钥操作 */
OH_Huks_Result HksDHAgreeFinish(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_Blob *publicKey,
    const struct OH_Huks_ParamSet *initParamSet,
    const struct OH_Huks_ParamSet *finishParamSet, struct OH_Huks_Blob *outData)
{
    struct OH_Huks_Blob inData = {(uint32_t)strlen(IN_DATA), (uint8_t *)IN_DATA};
    uint8_t handleU[sizeof(uint64_t)] = {0};
    struct OH_Huks_Blob handle = {sizeof(uint64_t), handleU};
    OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, initParamSet, &handle, nullptr);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    uint8_t outDataU[DH_COMMON_SIZE] = {0};
    struct OH_Huks_Blob outDataUpdate = {DH_COMMON_SIZE, outDataU};
    ret = OH_Huks_UpdateSession(&handle, initParamSet, publicKey, &outDataUpdate);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    ret = OH_Huks_FinishSession(&handle, finishParamSet, &inData, outData);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    return ret;
}

static OH_Huks_Result InitializeAgreeParamSets(struct OH_Huks_ParamSet **genParamSet,
    struct OH_Huks_ParamSet **initParamSet01,
    struct OH_Huks_ParamSet **finishParamSet01,
    struct OH_Huks_ParamSet **initParamSet02,
    struct OH_Huks_ParamSet **finishParamSet02)
{
    OH_Huks_Result ohResult;
    
    ohResult = InitParamSet(genParamSet, g_genAgreeParams,
                            sizeof(g_genAgreeParams) / sizeof(OH_Huks_Param));
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(initParamSet01, g_agreeParamsInit01,
                            sizeof(g_agreeParamsInit01) / sizeof(OH_Huks_Param));
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(finishParamSet01, g_agreeParamsFinish01,
                            sizeof(g_agreeParamsFinish01) / sizeof(OH_Huks_Param));
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(initParamSet02, g_agreeParamsInit02,
                            sizeof(g_agreeParamsInit02) / sizeof(OH_Huks_Param));
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(finishParamSet02, g_agreeParamsFinish02,
                            sizeof(g_agreeParamsFinish02) / sizeof(OH_Huks_Param));
    return ohResult;
}

static OH_Huks_Result GenerateKeyPair(struct OH_Huks_ParamSet *genParamSet)
{
    OH_Huks_Result ohResult;
    
    /* 设备A生成密钥 */
    ohResult = OH_Huks_GenerateKeyItem(&g_keyAlias01001, genParamSet, nullptr);
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        return ohResult;
    }
    
    /* 设备B生成密钥 */
    ohResult = OH_Huks_GenerateKeyItem(&g_keyAlias02001, genParamSet, nullptr);
    return ohResult;
}

static OH_Huks_Result KeyAgreement(struct OH_Huks_Blob *g_keyAlias,
    struct OH_Huks_Blob *publicKey,
    struct OH_Huks_Blob *outData,
    struct OH_Huks_ParamSet *initParamSet,
    struct OH_Huks_ParamSet *finishParamSet)
{
    OH_Huks_Result ohResult;
    
    ohResult = MallocAndCheckBlobData(outData, outData->size);
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        return ohResult;
    }
    /* 协商密钥 */
    ohResult = HksDHAgreeFinish(g_keyAlias, publicKey, initParamSet, finishParamSet, outData);
    return ohResult;
}

static void CleanKey(struct OH_Huks_Blob *genKeyAlias,
    struct OH_Huks_Blob *genKeyAliasFinal,
    struct OH_Huks_ParamSet *genParamSet,
    struct OH_Huks_ParamSet **initParamSet,
    struct OH_Huks_ParamSet **finishParamSet)
{
    OH_Huks_DeleteKeyItem(genKeyAlias, genParamSet);
    OH_Huks_DeleteKeyItem(genKeyAliasFinal, NULL);
    OH_Huks_FreeParamSet(initParamSet);
    OH_Huks_FreeParamSet(finishParamSet);
}

/* 协商密钥整体流程 */
napi_value DhAgreeKey(napi_env env, napi_callback_info info)
{
    struct OH_Huks_ParamSet *genParamSet = nullptr;
    struct OH_Huks_ParamSet *initParamSet01 = nullptr;
    struct OH_Huks_ParamSet *finishParamSet01 = nullptr;
    struct OH_Huks_ParamSet *initParamSet02 = nullptr;
    struct OH_Huks_ParamSet *finishParamSet02 = nullptr;
    struct OH_Huks_Blob publicKey01 = {.size = DH_COMMON_SIZE, .data = nullptr};
    struct OH_Huks_Blob publicKey02 = {.size = DH_COMMON_SIZE, .data = nullptr};
    struct OH_Huks_Blob outData01 = {.size = DH_COMMON_SIZE, .data = nullptr};
    struct OH_Huks_Blob outData02 = {.size = DH_COMMON_SIZE, .data = nullptr};

    OH_Huks_Result ohResult;
    do {
        /* 1.确定密钥别名集成密钥参数集 */
        ohResult = InitializeAgreeParamSets(&genParamSet, &initParamSet01, &finishParamSet01,
                                            &initParamSet02, &finishParamSet02);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        /* 2.设备A和设备B生成密钥 */
        ohResult = GenerateKeyPair(genParamSet);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        ohResult = MallocAndCheckBlobData(&publicKey01, publicKey01.size);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        ohResult = MallocAndCheckBlobData(&publicKey02, publicKey02.size);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        /* 3.设备A、B导出公钥 */
        ohResult = HksDHAgreeExport(&g_keyAlias01001, &g_keyAlias02001, &publicKey01, &publicKey02, genParamSet);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        /* 4.设备A、B执行密钥协商 */
        ohResult = KeyAgreement(&g_keyAlias01001, &publicKey02, &outData01, initParamSet01, finishParamSet01);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        ohResult = KeyAgreement(&g_keyAlias02001, &publicKey01, &outData02, initParamSet02, finishParamSet02);
    } while (0);
    free(publicKey01.data);
    free(publicKey02.data);
    free(outData01.data);
    free(outData02.data);
    /* 5.设备A、B删除密钥 */
    CleanKey(&g_keyAlias01001, &g_keyAliasFinal1001, genParamSet, &initParamSet01, &finishParamSet01);
    CleanKey(&g_keyAlias02001, &g_keyAliasFinal2001, genParamSet, &initParamSet02, &finishParamSet02);
    OH_Huks_FreeParamSet(&genParamSet);

    napi_value ret;
    napi_create_int32(env, ohResult.errorCode, &ret);
    return ret;
}
```

### ECDH密钥协商用例

准备ECDH密钥协商材料：

```
#include "huks/native_huks_api.h"
#include "huks/native_huks_param.h"
#include "napi/native_api.h"
#include <cstring>
#include "file.h"

/* 初始化参数 */
static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
    uint32_t paramCount)
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
static const uint32_t IV_SIZE = 16;
static uint8_t IV[IV_SIZE] = {0}; // this is a test value, for real use the iv should be different every time
static struct OH_Huks_Blob g_keyAliasFinal1001 = {(uint32_t)strlen("HksECDHAgreeKeyAliasTest001_1_final"),
                                                  (uint8_t *)"HksECDHAgreeKeyAliasTest001_1_final"};
/* 集成密钥参数集 */
static struct OH_Huks_Param g_genAgreeParams[] = {
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_ECC},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_ECC_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};
static struct OH_Huks_Param g_agreeParamsInit01[] = {
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_ECDH},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_ECC_KEY_SIZE_256}};
static struct OH_Huks_Param g_agreeParamsFinish01[] = {
    {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_ONLY_USED_IN_HUKS},
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_keyAliasFinal1001},
    {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
    {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_CBC}};
static struct OH_Huks_Blob g_keyAliasFinal2001 = {(uint32_t)strlen("HksECDHAgreeKeyAliasTest001_2_final"),
                                                  (uint8_t *)"HksECDHAgreeKeyAliasTest001_2_final"};
static struct OH_Huks_Param g_agreeParamsInit02[] = {
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_ECDH},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_ECC_KEY_SIZE_256}};
static struct OH_Huks_Param g_agreeParamsFinish02[] = {
    {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_ONLY_USED_IN_HUKS},
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_keyAliasFinal2001},
    {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
    {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_CBC}};
static const uint32_t ECDH_COMMON_SIZE = 1024;
static struct OH_Huks_Blob g_keyAlias01001 = {(uint32_t)strlen("HksECDHAgreeKeyAliasTest001_1"),
                                              (uint8_t *)"HksECDHAgreeKeyAliasTest001_1"};
static struct OH_Huks_Blob g_keyAlias02001 = {(uint32_t)strlen("HksECDHAgreeKeyAliasTest001_2"),
                                              (uint8_t *)"HksECDHAgreeKeyAliasTest001_2"};
```

ECDH密钥协商的功能函数实现，包括内存分配、参数初始化、密钥生成、和资源清理等：

```
static OH_Huks_Result MallocAndCheckBlobData(struct OH_Huks_Blob *blob, const uint32_t blobSize)
{
    struct OH_Huks_Result ret;
    ret.errorCode = OH_HUKS_SUCCESS;
    if (blobSize == 0 || blobSize > ECDH_COMMON_SIZE) {
        ret.errorCode = OH_HUKS_ERR_CODE_INTERNAL_ERROR;
        return ret;
    }
    blob->data = (uint8_t *)malloc(blobSize);
    if (blob->data == NULL) {
        ret.errorCode = OH_HUKS_ERR_CODE_INTERNAL_ERROR;
    }
    return ret;
}

/* 导出密钥 */
OH_Huks_Result HksEcdhAgreeExport(const struct OH_Huks_Blob *keyAlias1, const struct OH_Huks_Blob *keyAlias2,
                                  struct OH_Huks_Blob *publicKey1, struct OH_Huks_Blob *publicKey2,
                                  const struct OH_Huks_ParamSet *genParamSet)
{
    OH_Huks_Result ret = OH_Huks_ExportPublicKeyItem(keyAlias1, genParamSet, publicKey1);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    ret = OH_Huks_ExportPublicKeyItem(keyAlias2, genParamSet, publicKey2);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    return ret;
}
static const char *IN_DATA = "Hks_ECDH_Agree_Test_000000000000000000000000000000000000000000000000000000000000"
                              "00000000000000000000000000000000000000000000000000000000000000000000000000000000"
                              "0000000000000000000000000000000000000000000000000000000000000000000000000_string";
/* 协商密钥操作 */
OH_Huks_Result HksEcdhAgreeFinish(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_Blob *publicKey,
                                  const struct OH_Huks_ParamSet *initParamSet,
                                  const struct OH_Huks_ParamSet *finishParamSet, struct OH_Huks_Blob *outData)
{
    struct OH_Huks_Blob inData = {(uint32_t)strlen(IN_DATA), (uint8_t *)IN_DATA};
    uint8_t handleU[sizeof(uint64_t)] = {0};
    struct OH_Huks_Blob handle = {sizeof(uint64_t), handleU};
    OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, initParamSet, &handle, nullptr);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    uint8_t outDataU[ECDH_COMMON_SIZE] = {0};
    struct OH_Huks_Blob outDataUpdate = {ECDH_COMMON_SIZE, outDataU};
    ret = OH_Huks_UpdateSession(&handle, initParamSet, publicKey, &outDataUpdate);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    ret = OH_Huks_FinishSession(&handle, finishParamSet, &inData, outData);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    return ret;
}

static OH_Huks_Result InitializeAgreeParamSets(struct OH_Huks_ParamSet **genParamSet,
    struct OH_Huks_ParamSet **initParamSet01,
    struct OH_Huks_ParamSet **finishParamSet01,
    struct OH_Huks_ParamSet **initParamSet02,
    struct OH_Huks_ParamSet **finishParamSet02)
{
    OH_Huks_Result ohResult;
    
    ohResult = InitParamSet(genParamSet, g_genAgreeParams,
                            sizeof(g_genAgreeParams) / sizeof(OH_Huks_Param));
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(initParamSet01, g_agreeParamsInit01,
                            sizeof(g_agreeParamsInit01) / sizeof(OH_Huks_Param));
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(finishParamSet01, g_agreeParamsFinish01,
                            sizeof(g_agreeParamsFinish01) / sizeof(OH_Huks_Param));
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(initParamSet02, g_agreeParamsInit02,
                            sizeof(g_agreeParamsInit02) / sizeof(OH_Huks_Param));
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(finishParamSet02, g_agreeParamsFinish02,
                            sizeof(g_agreeParamsFinish02) / sizeof(OH_Huks_Param));
    return ohResult;
}

static OH_Huks_Result GenerateKeyPair(struct OH_Huks_ParamSet *genParamSet)
{
    OH_Huks_Result ohResult;
    
    /* 设备A生成密钥 */
    ohResult = OH_Huks_GenerateKeyItem(&g_keyAlias01001, genParamSet, nullptr);
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        return ohResult;
    }
    
    /* 设备B生成密钥 */
    ohResult = OH_Huks_GenerateKeyItem(&g_keyAlias02001, genParamSet, nullptr);
    return ohResult;
}

static OH_Huks_Result KeyAgreement(struct OH_Huks_Blob *g_keyAlias,
    struct OH_Huks_Blob *publicKey,
    struct OH_Huks_Blob *outData,
    struct OH_Huks_ParamSet *initParamSet,
    struct OH_Huks_ParamSet *finishParamSet)
{
    OH_Huks_Result ohResult;
    
    ohResult = MallocAndCheckBlobData(outData, outData->size);
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        return ohResult;
    }
    /* 协商密钥 */
    ohResult = HksEcdhAgreeFinish(g_keyAlias, publicKey, initParamSet, finishParamSet, outData);
    return ohResult;
}

static void CleanKey(struct OH_Huks_Blob *genKeyAlias,
    struct OH_Huks_Blob *genKeyAliasFinal,
    struct OH_Huks_ParamSet *genParamSet,
    struct OH_Huks_ParamSet **initParamSet,
    struct OH_Huks_ParamSet **finishParamSet)
{
    OH_Huks_DeleteKeyItem(genKeyAlias, genParamSet);
    OH_Huks_DeleteKeyItem(genKeyAliasFinal, NULL);
    OH_Huks_FreeParamSet(initParamSet);
    OH_Huks_FreeParamSet(finishParamSet);
}
```

ECDH密钥协商的完整流程实现：

```
/* 协商密钥整体流程 */
napi_value EcdhAgreeKey(napi_env env, napi_callback_info info)
{
    struct OH_Huks_ParamSet *genParamSet = nullptr;
    struct OH_Huks_ParamSet *initParamSet01 = nullptr;
    struct OH_Huks_ParamSet *finishParamSet01 = nullptr;
    struct OH_Huks_ParamSet *initParamSet02 = nullptr;
    struct OH_Huks_ParamSet *finishParamSet02 = nullptr;
    struct OH_Huks_Blob publicKey01 = {.size = OH_HUKS_ECC_KEY_SIZE_256, .data = nullptr};
    struct OH_Huks_Blob publicKey02 = {.size = OH_HUKS_ECC_KEY_SIZE_256, .data = nullptr};
    struct OH_Huks_Blob outData01 = {.size = ECDH_COMMON_SIZE, .data = nullptr};
    struct OH_Huks_Blob outData02 = {.size = ECDH_COMMON_SIZE, .data = nullptr};
    OH_Huks_Result ohResult;
    do {
        /* 1.确定密钥别名集成密钥参数集 */
        ohResult = InitializeAgreeParamSets(&genParamSet, &initParamSet01, &finishParamSet01,
                                            &initParamSet02, &finishParamSet02);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        /* 2.设备A和设备B生成密钥 */
        ohResult = GenerateKeyPair(genParamSet);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        ohResult = MallocAndCheckBlobData(&publicKey01, publicKey01.size);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        ohResult = MallocAndCheckBlobData(&publicKey02, publicKey02.size);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        /* 3.设备A、B导出公钥 */
        ohResult = HksEcdhAgreeExport(&g_keyAlias01001, &g_keyAlias02001, &publicKey01, &publicKey02, genParamSet);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        /* 4.设备A、B执行密钥协商 */
        ohResult = KeyAgreement(&g_keyAlias01001, &publicKey02, &outData01, initParamSet01, finishParamSet01);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        ohResult = KeyAgreement(&g_keyAlias02001, &publicKey01, &outData02, initParamSet02, finishParamSet02);
    } while (0);
    free(publicKey01.data);
    free(publicKey02.data);
    free(outData01.data);
    free(outData02.data);
    /* 5.设备A、B删除密钥 */
    CleanKey(&g_keyAlias01001, &g_keyAliasFinal1001, genParamSet, &initParamSet01, &finishParamSet01);
    CleanKey(&g_keyAlias02001, &g_keyAliasFinal2001, genParamSet, &initParamSet02, &finishParamSet02);
    OH_Huks_FreeParamSet(&genParamSet);

    napi_value ret;
    napi_create_int32(env, ohResult.errorCode, &ret);
    return ret;
}
```
