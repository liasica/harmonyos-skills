---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-scrypt-ndk
title: 使用SCRYPT进行密钥派生(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥派生介绍及算法规格 > 使用SCRYPT进行密钥派生(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:89a3d7afc3e6257afb5d09600fc79d3c56b08fa099db87ab76832da11ebae7a4
---

对应的算法规格请查看[密钥派生算法规格：SCRYPT](crypto-key-derivation-overview.md#scrypt算法)。

## 开发步骤

1. 调用[OH\_CryptoKdfParams\_Create](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdfparams_create)，指定字符串参数'SCRYPT'，创建密钥派生参数对象。
2. 调用[OH\_CryptoKdfParams\_SetParam](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdfparams_setparam)，设置Scrypt所需的参数。

   密钥派生失败原因：下列参数未设置。

   * CRYPTO\_KDF\_KEY\_DATABLOB：用于生成派生密钥的原始密码。
   * CRYPTO\_KDF\_SALT\_DATABLOB：盐值。
   * CRYPTO\_KDF\_SCRYPT\_N\_UINT64：CPU/内存开销参数，必须是2的幂次方。
   * CRYPTO\_KDF\_SCRYPT\_R\_UINT64：块大小参数，影响并行度。
   * CRYPTO\_KDF\_SCRYPT\_P\_UINT64：并行化参数。
   * CRYPTO\_KDF\_SCRYPT\_MAX\_MEM\_UINT64：最大内存限制（字节）。
3. 调用[OH\_CryptoKdf\_Create](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdf_create)，指定字符串参数'SCRYPT'，创建密钥派生函数对象。
4. 调用[OH\_CryptoKdf\_Derive](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdf_derive)，指定目标密钥的字节长度，进行密钥派生。

```
#include "CryptoArchitectureKit/crypto_architecture_kit.h"
#include "CryptoArchitectureKit/crypto_kdf.h"
#include <cstdio>
#include <cstring>
#include "file.h"

static OH_Crypto_ErrCode doSetSaltAndPassword(OH_CryptoKdfParams **params)
{
    const char *password = "123456";
    const char *salt = "saltstring";
    Crypto_DataBlob saltBlob = {
        .data = reinterpret_cast<uint8_t *>(const_cast<char *>(salt)),
        .len = strlen(salt)
    };
    Crypto_DataBlob passwordBlob = {
        .data = reinterpret_cast<uint8_t *>(const_cast<char *>(password)),
        .len = strlen(password)
    };
    OH_Crypto_ErrCode ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_KEY_DATABLOB, &passwordBlob);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }

    ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_SALT_DATABLOB, &saltBlob);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }
    return CRYPTO_SUCCESS;
}

// 设置参数函数
static OH_Crypto_ErrCode doScryptSetParams(OH_CryptoKdfParams **params)
{
    OH_Crypto_ErrCode ret = OH_CryptoKdfParams_Create("SCRYPT", params);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }

    uint64_t n = 1024;  // CPU/内存开销参数。
    uint64_t r = 8;     // 块大小参数。
    uint64_t p = 16;    // 并行化参数。
    uint64_t maxMem = 1067008;  // 最大内存限制（字节）。

    Crypto_DataBlob nData = { .data = reinterpret_cast<uint8_t *>(&n), .len = sizeof(uint64_t) };
    Crypto_DataBlob rData = { .data = reinterpret_cast<uint8_t *>(&r), .len = sizeof(uint64_t) };
    Crypto_DataBlob pData = { .data = reinterpret_cast<uint8_t *>(&p), .len = sizeof(uint64_t) };
    Crypto_DataBlob maxMemData = { .data = reinterpret_cast<uint8_t *>(&maxMem), .len = sizeof(uint64_t) };

    ret = doSetSaltAndPassword(params);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }

    ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_SCRYPT_N_UINT64, &nData);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }
    ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_SCRYPT_R_UINT64, &rData);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }
    ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_SCRYPT_P_UINT64, &pData);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }
    ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_SCRYPT_MAX_MEM_UINT64, &maxMemData);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }
    return ret;

end:
    OH_CryptoKdfParams_Destroy(*params);
    *params = nullptr;
    return ret;
}

static OH_Crypto_ErrCode doScryptDerive(OH_CryptoKdfParams *params, uint32_t keyLength, Crypto_DataBlob *out)
{
    // 创建密钥派生函数对象。
    OH_CryptoKdf *kdfCtx = nullptr;
    OH_Crypto_ErrCode ret = OH_CryptoKdf_Create("SCRYPT", &kdfCtx);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }

    // 派生密钥。
    ret = OH_CryptoKdf_Derive(kdfCtx, params, keyLength, out);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoKdf_Destroy(kdfCtx);
        return ret;
    }

    printf("Derived key length: %u\n", out->len);

    OH_CryptoKdf_Destroy(kdfCtx);
    return ret;
}

OH_Crypto_ErrCode doTestScrypt()
{
    OH_CryptoKdfParams *params = nullptr;
    Crypto_DataBlob out = {0};
    uint32_t keyLength = 32; // 生成32字节的密钥。

    // 设置参数。
    OH_Crypto_ErrCode ret = doScryptSetParams(&params);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }

    // 派生密钥。
    ret = doScryptDerive(params, keyLength, &out);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoKdfParams_Destroy(params);
        return ret;
    }

    // 清理资源。
    OH_Crypto_FreeDataBlob(&out);
    OH_CryptoKdfParams_Destroy(params);
    return CRYPTO_SUCCESS;
}
```
