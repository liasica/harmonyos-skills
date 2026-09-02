---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-group-key-ndk
title: 群组密钥(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 其他操作 > 群组密钥 > 群组密钥(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9bd2a31afd2189050c32eb33edc81f21d9bf7028ea6664761f93b385a4631bbc
---

从API 23开始，HUKS支持群组密钥功能。群组密钥支持的HUKS密钥操作及详细介绍参考[群组密钥介绍](huks-group-key-overview.md)，本文档以[AES/CBC/PKCS7加解密](huks-group-key-ndk.md#aescbcpkcs7加解密)、[X25519非对称密钥协商](huks-group-key-ndk.md#x25519非对称密钥协商)、[PBKDF2派生密钥](huks-group-key-ndk.md#pbkdf2派生密钥)为例展示群组密钥使用方法。

## 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

**配置文件**

使用群组密钥之前，需要在app.json5文件中配置群组信息，配置方法参考[配置文件示例](app-configuration-file.md#配置文件示例)中assetAccessGroups字段的配置方式。

## AES/CBC/PKCS7加解密

### 开发步骤

**生成密钥**

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集。需要添加群组密钥标签[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)、[OH\_HUKS\_TAG\_KEY\_OVERRIDE](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，避免密钥被覆盖。
3. 调用[OH\_Huks\_GenerateKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_generatekeyitem)生成密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md)，导入已有的密钥。

**加密**

1. 指定密钥别名。
2. 指定待加密的数据。
3. 调用[OH\_Huks\_InitParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_initparamset)指定算法参数配置。需要添加群组密钥标签[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)。
4. 调用[OH\_Huks\_InitSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_initsession)初始化密钥会话，并获取会话的句柄handle。
5. 调用[OH\_Huks\_FinishSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_finishsession)结束密钥会话，获取加密后的密文。

**解密**

1. 指定密钥别名。
2. 指定待解密的密文。
3. 调用[OH\_Huks\_InitParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_initparamset)指定算法参数配置。需要添加群组密钥标签[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)。
4. 调用[OH\_Huks\_InitSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_initsession)初始化密钥会话，并获取会话的句柄handle。
5. 调用[OH\_Huks\_FinishSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_finishsession)结束密钥会话，获取解密后的数据。

**删除密钥**

1. 指定密钥别名。
2. 调用[OH\_Huks\_InitParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_initparamset)指定算法参数配置。需要添加群组密钥标签[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)。
3. 调用[OH\_Huks\_DeleteKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_deletekeyitem)删除密钥，具体请参考[密钥删除](huks-delete-key-ndk.md)。

当密钥废弃不用时，需要调用OH\_Huks\_DeleteKeyItem删除密钥，具体请参考[密钥删除](huks-delete-key-ndk.md)。

### 开发示例

```
#include "huks/native_huks_api.h"
#include "huks/native_huks_param.h"
#include "napi/native_api.h"
#include <string.h>
#include "CryptoArchitectureKit/crypto_architecture_kit.h"

static OH_Crypto_ErrCode genRandomNumber(uint32_t randomLength, uint8_t *out)
{
    /* 创建随机数生成器 */
    OH_CryptoRand *rand = nullptr;
    OH_Crypto_ErrCode ret = OH_CryptoRand_Create(&rand);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }
    Crypto_DataBlob blob = {out, randomLength};
    /* 生成指定长度的随机数 */
    ret = OH_CryptoRand_GenerateRandom(rand, randomLength, &blob);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoRand_Destroy(rand);
        return ret;
    }
    OH_CryptoRand_Destroy(rand);

    return CRYPTO_SUCCESS;
}

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
uint32_t OH_HUKS_TAG_KEY_ACCESS_GROUP = 5 << 28 | 523;
static const uint32_t IV_SIZE = 16;
static uint8_t IV[IV_SIZE] = { 0 };
static OH_Crypto_ErrCode ret = genRandomNumber(IV_SIZE, IV);
/*
 * 需要在app.json5中配置assetAccessGroups字段新增分组信息
 */
static char group[] = "ohos.test.group";
static struct OH_Huks_Param g_genEncDecParams[] = {
    {
        .tag = OH_HUKS_TAG_ALGORITHM,
        .uint32Param = OH_HUKS_ALG_AES
    }, {
        .tag = OH_HUKS_TAG_PURPOSE,
        .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT | OH_HUKS_KEY_PURPOSE_DECRYPT
    }, {
        .tag = OH_HUKS_TAG_KEY_SIZE,
        .uint32Param = OH_HUKS_AES_KEY_SIZE_256
    }, {
        .tag = OH_HUKS_TAG_PADDING,
        .uint32Param = OH_HUKS_PADDING_PKCS7
    }, {
        .tag = OH_HUKS_TAG_BLOCK_MODE,
        .uint32Param = OH_HUKS_MODE_CBC
    }, {
        .tag = OH_HUKS_TAG_KEY_ACCESS_GROUP,
        .blob = {
            .size = (uint32_t)strlen(group),
            .data = (uint8_t *)group
        }
    }
};
static struct OH_Huks_Param g_encryptParams[] = {
    {
        .tag = OH_HUKS_TAG_ALGORITHM,
        .uint32Param = OH_HUKS_ALG_AES
    }, {
        .tag = OH_HUKS_TAG_PURPOSE,
        .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT
    }, {
        .tag = OH_HUKS_TAG_KEY_SIZE,
        .uint32Param = OH_HUKS_AES_KEY_SIZE_256
    }, {
        .tag = OH_HUKS_TAG_PADDING,
        .uint32Param = OH_HUKS_PADDING_PKCS7
    }, {
        .tag = OH_HUKS_TAG_BLOCK_MODE,
        .uint32Param = OH_HUKS_MODE_CBC
    }, {
        .tag = OH_HUKS_TAG_IV,
        .blob = {
            .size = IV_SIZE,
            .data = (uint8_t *)IV
        }
    }, {
        .tag = OH_HUKS_TAG_KEY_ACCESS_GROUP,
        .blob = {
            .size = (uint32_t)strlen(group),
            .data = (uint8_t *)group
        }
    }
};
static struct OH_Huks_Param g_decryptParams[] = {
    {
        .tag = OH_HUKS_TAG_ALGORITHM,
        .uint32Param = OH_HUKS_ALG_AES
    }, {
        .tag = OH_HUKS_TAG_PURPOSE,
        .uint32Param = OH_HUKS_KEY_PURPOSE_DECRYPT
    }, {
        .tag = OH_HUKS_TAG_KEY_SIZE,
        .uint32Param = OH_HUKS_AES_KEY_SIZE_256
    }, {
        .tag = OH_HUKS_TAG_PADDING,
        .uint32Param = OH_HUKS_PADDING_PKCS7
    }, {
        .tag = OH_HUKS_TAG_BLOCK_MODE,
        .uint32Param = OH_HUKS_MODE_CBC
    }, {
        .tag = OH_HUKS_TAG_IV,
        .blob = {
            .size = IV_SIZE,
            .data = (uint8_t *)IV
        }
    }, {
        .tag = OH_HUKS_TAG_KEY_ACCESS_GROUP,
        .blob = {
            .size = (uint32_t)strlen(group),
            .data = (uint8_t *)group
        }
    }
};
static const uint32_t AES_COMMON_SIZE = 1024;

OH_Huks_Result HksAesCipherTestEncrypt(
    const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *encryptParamSet,
    const struct OH_Huks_Blob *inData, struct OH_Huks_Blob *cipherText)
{
    uint8_t handleE[sizeof(uint64_t)] = {0};
    struct OH_Huks_Blob handleEncrypt = {sizeof(uint64_t), handleE};
    OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, encryptParamSet, &handleEncrypt, nullptr);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    ret = OH_Huks_FinishSession(&handleEncrypt, encryptParamSet, inData, cipherText);
    return ret;
}

OH_Huks_Result HksAesCipherTestDecrypt(const struct OH_Huks_Blob *keyAlias,
    const struct OH_Huks_ParamSet *decryptParamSet, const struct OH_Huks_Blob *cipherText,
    struct OH_Huks_Blob *plainText, const struct OH_Huks_Blob *inData)
{
    uint8_t handleD[sizeof(uint64_t)] = {0};
    struct OH_Huks_Blob handleDecrypt = {sizeof(uint64_t), handleD};
    OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, decryptParamSet, &handleDecrypt, nullptr);
    if (ret.errorCode != OH_HUKS_SUCCESS) {
        return ret;
    }
    ret = OH_Huks_FinishSession(&handleDecrypt, decryptParamSet, cipherText, plainText);
    return ret;
}

static napi_value EncDecKey(napi_env env, napi_callback_info info)
{
    char tmpKeyAlias[] = "test_enc_dec";
    struct OH_Huks_Blob keyAlias = { (uint32_t)strlen(tmpKeyAlias), (uint8_t *)tmpKeyAlias };
    struct OH_Huks_ParamSet *genParamSet = nullptr;
    struct OH_Huks_ParamSet *encryptParamSet = nullptr;
    struct OH_Huks_ParamSet *decryptParamSet = nullptr;
    OH_Huks_Result ohResult;
    do {
        /* 1. Generate Key */
        /*
         * 模拟生成密钥场景
         * 1.1. 确定密钥别名
         */
        /*
         * 1.2. 获取生成密钥算法参数配置
         */
        ohResult = InitParamSet(&genParamSet, g_genEncDecParams, sizeof(g_genEncDecParams) / sizeof(OH_Huks_Param));
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        /*
         * 1.3. 调用generateKeyItem
         */
        ohResult = OH_Huks_GenerateKeyItem(&keyAlias, genParamSet, nullptr);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        /* 2. Encrypt */
        /*
         * 模拟加密场景
         * 2.1. 获取密钥别名
         */
        /*
         * 2.2. 获取待加密的数据
         */
        /*
         * 2.3. 获取加密算法参数配置
         */
        ohResult = InitParamSet(&encryptParamSet, g_encryptParams, sizeof(g_encryptParams) / sizeof(OH_Huks_Param));
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        char tmpInData[] = "AES_ECB_INDATA_1";
        struct OH_Huks_Blob inData = { (uint32_t)strlen(tmpInData), (uint8_t *)tmpInData };
        uint8_t cipher[AES_COMMON_SIZE] = {0};
        struct OH_Huks_Blob cipherText = {AES_COMMON_SIZE, cipher};
        /*
         * 2.4. 调用initSession获取handle
         */
        /*
         * 2.5. 调用finishSession获取加密后的密文
         */
        ohResult = HksAesCipherTestEncrypt(&keyAlias, encryptParamSet, &inData, &cipherText);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        /* 3. Decrypt */
        /*
         * 模拟解密场景
         * 3.1. 获取密钥别名
         */
        /*
         * 3.2. 获取待解密的密文
         */
        /*
         * 3.3. 获取解密算法参数配置
         */
        ohResult = InitParamSet(&decryptParamSet, g_decryptParams, sizeof(g_decryptParams) / sizeof(OH_Huks_Param));
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        uint8_t plain[AES_COMMON_SIZE] = {0};
        struct OH_Huks_Blob plainText = {AES_COMMON_SIZE, plain};
        /*
         * 3.4. 调用initSession获取handle
         */
        /*
         * 3.5. 调用finishSession获取解密后的数据
         */
        ohResult = HksAesCipherTestDecrypt(&keyAlias, decryptParamSet, &cipherText, &plainText, &inData);
    } while (0);
    /* 4. Delete Key */
    /*
     * 模拟删除密钥场景
     * 4.1. 获取密钥别名
     */
    /*
     * 4.2. 调用deleteKeyItem删除密钥
     */
    (void)OH_Huks_DeleteKeyItem(&keyAlias, genParamSet);
        
    OH_Huks_FreeParamSet(&genParamSet);
    OH_Huks_FreeParamSet(&encryptParamSet);
    OH_Huks_FreeParamSet(&decryptParamSet);
    
    napi_value ret;
    napi_create_int32(env, ohResult.errorCode, &ret);
    return ret;
}
```

## X25519非对称密钥协商

### 开发步骤

**生成密钥**

设备A、设备B各自生成一个非对称密钥，具体请参考[密钥生成](huks-key-generation-overview.md)或[密钥导入](huks-key-import-overview.md)。

密钥生成时，指定参数[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，用于生成群组密钥。

**导出密钥**

设备A、B导出非对称密钥对的公钥材料，具体请参考[密钥导出](huks-export-key-ndk.md)。

导出密钥时，指定参数[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，用于导出群组密钥。

**密钥协商**

设备A、B分别基于本端私钥和对端设备的公钥，协商出共享密钥。

密钥协商时，指定参数[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，用于协商群组密钥。

**删除密钥**

当密钥废弃不用时，设备A、B均需要删除密钥，具体请参考[密钥删除](huks-delete-key-ndk.md)。

删除密钥时，指定参数[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，用于删除群组密钥。

### 开发示例

```
#include "huks/native_huks_api.h"
#include "huks/native_huks_param.h"
#include "napi/native_api.h"
#include <cstring>

static struct OH_Huks_Blob g_group = {(uint32_t)strlen("ohos.test.group"), (uint8_t *)"ohos.test.group"};
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
    {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE},
    {.tag = OH_HUKS_TAG_KEY_ACCESS_GROUP, .blob = g_group}
};
static struct OH_Huks_Param g_agreeParamsInit01[] = {
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_X25519},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_CURVE25519_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE},
    {.tag = OH_HUKS_TAG_KEY_ACCESS_GROUP, .blob = g_group}
};
static struct OH_Huks_Param g_agreeParamsFinish01[] = {
    {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_ONLY_USED_IN_HUKS},
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_keyAliasFinal1001},
    {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
    {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
    {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE},
    {.tag = OH_HUKS_TAG_KEY_ACCESS_GROUP, .blob = g_group}
};
static struct OH_Huks_Blob g_keyAliasFinal2001 = {(uint32_t)strlen("HksX25519AgreeKeyAliasTest001_2_final"),
                                                  (uint8_t *)"HksX25519AgreeKeyAliasTest001_2_final"};
static struct OH_Huks_Param g_agreeParamsInit02[] = {
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_X25519},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_CURVE25519_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE},
    {.tag = OH_HUKS_TAG_KEY_ACCESS_GROUP, .blob = g_group}
};
static struct OH_Huks_Param g_agreeParamsFinish02[] = {
    {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_ONLY_USED_IN_HUKS},
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
    {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_keyAliasFinal2001},
    {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
    {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
    {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE},
    {.tag = OH_HUKS_TAG_KEY_ACCESS_GROUP, .blob = g_group}
};
static const uint32_t X25519_COMMON_SIZE = 256;
static struct OH_Huks_Blob g_keyAlias01001 = {(uint32_t)strlen("HksX25519AgreeKeyAliasTest001_1"),
                                              (uint8_t *)"HksX25519AgreeKeyAliasTest001_1"};
static struct OH_Huks_Blob g_keyAlias02001 = {(uint32_t)strlen("HksX25519AgreeKeyAliasTest001_2"),
                                              (uint8_t *)"HksX25519AgreeKeyAliasTest001_2"};

static OH_Huks_Result MallocAndCheckBlobData(struct OH_Huks_Blob *blob, const uint32_t blobSize)
{
    struct OH_Huks_Result ret;
    ret.errorCode = OH_HUKS_SUCCESS;
    if (blobSize == 0 || blobSize > X25519_COMMON_SIZE) {
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
    OH_Huks_DeleteKeyItem(genKeyAliasFinal, genParamSet);
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

## PBKDF2派生密钥

### 开发步骤

**生成密钥**

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 密钥生成时，指定参数[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，用于生成群组密钥。
3. 调用[OH\_Huks\_GenerateKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_generatekeyitem)生成密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md)，导入已有的密钥。

**密钥派生**

1. 获取密钥别名，指定对应的属性参数HuksOptions，添加参数[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，用于派生群组密钥。
2. 调用[OH\_Huks\_InitParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_initparamset)指定算法参数配置。需要添加群组密钥标签[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)。
3. 调用[OH\_Huks\_InitSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_initsession)初始化密钥会话，并获取会话的句柄handle。
4. 调用[OH\_Huks\_UpdateSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_updatesession)更新密钥会话。
5. 调用[OH\_Huks\_FinishSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_finishsession)结束密钥会话，完成派生。

**删除密钥**

当密钥废弃不用时，需要调用[OH\_Huks\_DeleteKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_deletekeyitem)删除密钥，具体请参考[密钥删除](huks-delete-key-ndk.md)。

删除密钥时，指定参数[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，用于删除群组密钥。

### 开发示例

```
#include "huks/native_huks_api.h"
#include "huks/native_huks_param.h"
#include "napi/native_api.h"
#include <cstring>

OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
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
static const uint32_t DERIVE_KEY_SIZE_32 = 32;
static const uint32_t DERIVE_KEY_SIZE_256 = 256;
static const uint32_t DERIVE_KEY_ITERATION = 10000;
static const uint32_t SALT_SIZE = 8;
static const char DERIVE_KEY_SALT[SALT_SIZE] = "mysalt1";
static struct OH_Huks_Blob g_deriveKeyAlias = {(uint32_t)strlen("test_derive"), (uint8_t *)"test_derive"};
static struct OH_Huks_Blob g_group = {(uint32_t)strlen("ohos.test.group"), (uint8_t *)"ohos.test.group"};
static struct OH_Huks_Param g_genDeriveParams[] = {
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_DERIVE},
    {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_KEY_ACCESS_GROUP, .blob = g_group}
};
static struct OH_Huks_Param g_hkdfParams[] = {
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_PBKDF2},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_DERIVE},
    {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256},
    {.tag = OH_HUKS_TAG_DERIVE_KEY_SIZE, .uint32Param = DERIVE_KEY_SIZE_32},
    {.tag = OH_HUKS_TAG_ITERATION, .uint32Param = DERIVE_KEY_ITERATION},
    {.tag = OH_HUKS_TAG_SALT, .blob = {.size = SALT_SIZE, .data = (uint8_t *) DERIVE_KEY_SALT}},
    {.tag = OH_HUKS_TAG_KEY_ACCESS_GROUP, .blob = g_group}
};
static struct OH_Huks_Param g_hkdfFinishParams[] = {
    {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_ONLY_USED_IN_HUKS},
    {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_deriveKeyAlias},
    {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
    {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = DERIVE_KEY_SIZE_256},
    {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_DERIVE},
    {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE},
    {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
    {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
    {.tag = OH_HUKS_TAG_KEY_ACCESS_GROUP, .blob = g_group}
};
static const uint32_t COMMON_SIZE = 1024;
static const char *G_DERIVE_IN_DATA = "Hks_PBKDF2_Derive_Test_0_string";
static OH_Huks_Result PerformPbkdfDerivation(const struct OH_Huks_Blob *genAlias,
    struct OH_Huks_ParamSet *hkdfParamSet,
    struct OH_Huks_ParamSet *hkdfFinishParamSet,
    const struct OH_Huks_Blob &inData)
{
    OH_Huks_Result ohResult;
    /* Init */
    uint8_t handleD[sizeof(uint64_t)] = {0};
    struct OH_Huks_Blob handleDerive = {sizeof(uint64_t), handleD};
    ohResult = OH_Huks_InitSession(genAlias, hkdfParamSet, &handleDerive, nullptr);
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        return ohResult;
    }
    /* Update */
    uint8_t tmpOut[COMMON_SIZE] = {0};
    struct OH_Huks_Blob outData = {COMMON_SIZE, tmpOut};
    ohResult = OH_Huks_UpdateSession(&handleDerive, hkdfParamSet, &inData, &outData);
    if (ohResult.errorCode != OH_HUKS_SUCCESS) {
        return ohResult;
    }
    /* Finish */
    uint8_t outDataD[COMMON_SIZE] = {0};
    struct OH_Huks_Blob outDataDerive = {COMMON_SIZE, outDataD};
    ohResult = OH_Huks_FinishSession(&handleDerive, hkdfFinishParamSet, &inData, &outDataDerive);
    return ohResult;
}

napi_value PbkdfDeriveKey(napi_env env, napi_callback_info info)
{
    struct OH_Huks_Blob genAlias = {(uint32_t)strlen("test_signVerify"), (uint8_t *)"test_signVerify"};
    struct OH_Huks_Blob inData = {(uint32_t)strlen(G_DERIVE_IN_DATA), (uint8_t *)G_DERIVE_IN_DATA};
    struct OH_Huks_ParamSet *genParamSet = nullptr;
    struct OH_Huks_ParamSet *hkdfParamSet = nullptr;
    struct OH_Huks_ParamSet *hkdfFinishParamSet = nullptr;
    OH_Huks_Result ohResult;
    do {
        ohResult = InitParamSet(&genParamSet, g_genDeriveParams, sizeof(g_genDeriveParams) /
                     sizeof(OH_Huks_Param));
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        ohResult = InitParamSet(&hkdfParamSet, g_hkdfParams, sizeof(g_hkdfParams) /
                     sizeof(OH_Huks_Param));
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        ohResult =InitParamSet(&hkdfFinishParamSet, g_hkdfFinishParams, sizeof(g_hkdfFinishParams) /
              sizeof(OH_Huks_Param));
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        /* 1. 生成密钥 */
        ohResult = OH_Huks_GenerateKeyItem(&genAlias, genParamSet, nullptr);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        /* 2. 派生密钥 */
        ohResult = PerformPbkdfDerivation(&genAlias, hkdfParamSet, hkdfFinishParamSet, inData);
    } while (0);
    (void)OH_Huks_DeleteKeyItem(&genAlias, genParamSet);
    (void)OH_Huks_DeleteKeyItem(&g_deriveKeyAlias, genParamSet);
    OH_Huks_FreeParamSet(&genParamSet);
    OH_Huks_FreeParamSet(&hkdfParamSet);
    OH_Huks_FreeParamSet(&hkdfFinishParamSet);

    napi_value ret;
    napi_create_int32(env, ohResult.errorCode, &ret);
    return ret;
}
```
