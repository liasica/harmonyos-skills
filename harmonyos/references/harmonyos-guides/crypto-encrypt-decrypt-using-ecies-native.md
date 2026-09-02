---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-encrypt-decrypt-using-ecies-native
title: 使用ECIES混合加解密(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密介绍 > 使用ECIES混合加解密(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e3dbe5ea748949df2438bc22930c2316f880aa866d238b6c0032e83147fa8852
---

从API版本26.0.0开始，支持ECIES算法，ECIES是一种基于椭圆曲线密码学的加密算法。

**约束条件：**

* 密钥协商算法支持ECC256、ECC384、ECC521。
* 密钥派生算法仅支持X963KDF，摘要算法支持SHA1、SHA256、SHA384、SHA512。
* 对称加密算法支持AES128、AES192、AES256。
* 分组模式仅支持GCM。

## 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libohcrypto.so)
```

## 开发步骤

### 加密

1. 调用[OH\_CryptoAsymKeyGenerator\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_create)和[OH\_CryptoAsymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_generate)，使用ECC算法生成密钥对。
2. 调用[OH\_CryptoKeyAgreement\_Create](../harmonyos-references/capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_create)和[OH\_CryptoKeyAgreement\_GenerateSecret](../harmonyos-references/capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_generatesecret)，基于本端的私钥（KeyPair.priKey）与对端的公钥（KeyPair.pubKey）进行密钥协商，返回共享密钥。
3. X963KDF密钥派生，调用[OH\_CryptoKdf\_Create](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdf_create)和[OH\_CryptoKdf\_Derive](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdf_derive)，基于协商的共享密钥（Secret）进行密钥派生，返回派生后的密钥。
4. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'AES128|GCM'，创建对称密钥类型为AES128、分组模式为GCM的Cipher实例，用于完成加密操作。
5. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（OH\_CryptoSymKey），初始化加密Cipher实例。
6. 调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，更新数据（明文），获取加密后的数据。
7. 调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，获取authTag。

   **说明** 

   在GCM模式下，一次加密流程中，将每次update和最后final的结果拼接起来，会得到“密文 + authTag”，authTag为末尾的16字节。其余部分均为密文。如果final的data参数传入null，则final的结果就是authTag。

### 解密

1. 调用[OH\_CryptoAsymKeyGenerator\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_create)和[OH\_CryptoAsymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_generate)，使用ECC算法生成密钥对。
2. 调用[OH\_CryptoKeyAgreement\_Create](../harmonyos-references/capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_create)和[OH\_CryptoKeyAgreement\_GenerateSecret](../harmonyos-references/capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_generatesecret)，基于本端的私钥（KeyPair.priKey）与对端的公钥（KeyPair.pubKey）进行密钥协商，返回共享密钥。
3. X963KDF密钥派生，调用[OH\_CryptoKdf\_Create](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdf_create)和[OH\_CryptoKdf\_Derive](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdf_derive)，基于协商的共享密钥（Secret）进行密钥派生，返回派生后的密钥。
4. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'AES128|GCM'，创建对称密钥类型为AES128、分组模式为GCM的Cipher实例，用于完成解密操作。
5. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（OH\_CryptoSymKey），初始化解密Cipher实例。
6. 调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，更新数据（密文）。
7. 调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，获取解密数据。

### 示例代码

```
#include <cstring>
#include <hilog/log.h>
#include "CryptoArchitectureKit/crypto_architecture_kit.h"
#include "native_test.h"

namespace ECIES {
uint8_t aad[] = { 0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07 };
uint8_t tag[] = { 0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F };
const uint8_t ivSize = 16;
const uint8_t keySize = 16;

struct CryptoContext {
    OH_CryptoKeyPair *keyPair;
    OH_CryptoSymKey *symKey;
    Crypto_DataBlob secret;
    Crypto_DataBlob ivData; // secret的前16字节作为IV，浅拷贝
};

OH_Crypto_ErrCode GenerateKeyPair(OH_CryptoKeyPair **keyPair)
{
    OH_CryptoAsymKeyGenerator *asyKeyGenerator = nullptr;
    OH_Crypto_ErrCode ret = OH_CryptoAsymKeyGenerator_Create("ECC256", &asyKeyGenerator);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }
    ret = OH_CryptoAsymKeyGenerator_Generate(asyKeyGenerator, keyPair);
    OH_CryptoAsymKeyGenerator_Destroy(asyKeyGenerator);
    return ret;
}

OH_Crypto_ErrCode GenerateSecret(OH_CryptoPrivKey *privKey, OH_CryptoPubKey *pubKey, Crypto_DataBlob *secret)
{
    // EC密钥协商
    OH_CryptoKeyAgreement *keyAgreement = nullptr;
    OH_Crypto_ErrCode ret = OH_CryptoKeyAgreement_Create("ECC256", &keyAgreement);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }
    ret = OH_CryptoKeyAgreement_GenerateSecret(keyAgreement, privKey, pubKey, secret);
    OH_CryptoKeyAgreement_Destroy(keyAgreement);
    return ret;
}

OH_Crypto_ErrCode KdfDeriveSecret(OH_CryptoPrivKey *privKey, OH_CryptoPubKey *pubKey, Crypto_DataBlob *secret)
{
    // 使用X963KDF进行密钥派生
    OH_CryptoKdfParams *params = nullptr;
    OH_Crypto_ErrCode ret = OH_CryptoKdfParams_Create("X963KDF", &params);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }
    Crypto_DataBlob keyData = {};
    ret = GenerateSecret(privKey, pubKey, &keyData);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoKdfParams_Destroy(params);
        return ret;
    }
    ret = OH_CryptoKdfParams_SetParam(params, CRYPTO_KDF_KEY_DATABLOB, &keyData);
    OH_Crypto_FreeDataBlob(&keyData);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoKdfParams_Destroy(params);
        return ret;
    }
    const char *info = "infostring";
    Crypto_DataBlob infoData = { .data = (uint8_t *)info, .len = strlen(info) };
    ret = OH_CryptoKdfParams_SetParam(params, CRYPTO_KDF_INFO_DATABLOB, &infoData);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoKdfParams_Destroy(params);
        return ret;
    }
    OH_CryptoKdf *x963Kdf = nullptr;
    ret = OH_CryptoKdf_Create("X963KDF|SHA256", &x963Kdf);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoKdfParams_Destroy(params);
        return ret;
    }
    ret = OH_CryptoKdf_Derive(x963Kdf, params, ivSize + keySize, secret);
    OH_CryptoKdf_Destroy(x963Kdf);
    OH_CryptoKdfParams_Destroy(params);
    return ret;
}

OH_Crypto_ErrCode GenerateSymKey(const Crypto_DataBlob *secret, OH_CryptoSymKey **symKey)
{
    OH_CryptoSymKeyGenerator *symKeyGenerator = nullptr;
    OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create("AES128", &symKeyGenerator);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }
    Crypto_DataBlob keyData = { .data = secret->data + ivSize, .len = keySize };
    ret = OH_CryptoSymKeyGenerator_Convert(symKeyGenerator, &keyData, symKey);
    OH_CryptoSymKeyGenerator_Destroy(symKeyGenerator);
    return ret;
}

void SetCipherIvData(CryptoContext *ctx, Crypto_DataBlob *secret)
{
    ctx->ivData.data = secret->data;
    ctx->ivData.len = ivSize;
}

OH_Crypto_ErrCode SetCipherParams(OH_CryptoSymCipherParams *params, Crypto_DataBlob *ivBlob, Crypto_DataBlob *tagBlob)
{
    Crypto_DataBlob aadBlob = { .data = aad, .len = sizeof(aad) };
    OH_Crypto_ErrCode ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_AAD_DATABLOB, &aadBlob);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }
    ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_IV_DATABLOB, ivBlob);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }
    ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_TAG_DATABLOB, tagBlob);
    return ret;
}

OH_Crypto_ErrCode Encrypt(CryptoContext *ctx, Crypto_DataBlob *plainText, Crypto_DataBlob *cipherText,
    Crypto_DataBlob *tagBlob)
{
    // AES-GCM对称加密
    OH_CryptoSymCipherParams *params = nullptr;
    OH_Crypto_ErrCode ret = OH_CryptoSymCipherParams_Create(&params);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }
    Crypto_DataBlob tagInit = { .data = tag, .len = sizeof(tag) };
    ret = SetCipherParams(params, &ctx->ivData, &tagInit);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoSymCipherParams_Destroy(params);
        return ret;
    }
    OH_CryptoSymCipher *encCtx = nullptr;
    ret = OH_CryptoSymCipher_Create("AES128|GCM", &encCtx);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoSymCipherParams_Destroy(params);
        return ret;
    }
    ret = OH_CryptoSymCipher_Init(encCtx, CRYPTO_ENCRYPT_MODE, ctx->symKey, params);
    OH_CryptoSymCipherParams_Destroy(params);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoSymCipher_Destroy(encCtx);
        return ret;
    }
    ret = OH_CryptoSymCipher_Update(encCtx, plainText, cipherText);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoSymCipher_Destroy(encCtx);
        return ret;
    }
    ret = OH_CryptoSymCipher_Final(encCtx, nullptr, tagBlob);
    OH_CryptoSymCipher_Destroy(encCtx);
    return ret;
}

OH_Crypto_ErrCode Decrypt(CryptoContext *ctx, Crypto_DataBlob *cipherText, Crypto_DataBlob *plainText,
    Crypto_DataBlob *tagBlob)
{
    // AES-GCM对称解密
    OH_CryptoSymCipherParams *params = nullptr;
    OH_Crypto_ErrCode ret = OH_CryptoSymCipherParams_Create(&params);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }
    ret = SetCipherParams(params, &ctx->ivData, tagBlob);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoSymCipherParams_Destroy(params);
        return ret;
    }
    OH_CryptoSymCipher *decCtx = nullptr;
    ret = OH_CryptoSymCipher_Create("AES128|GCM", &decCtx);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoSymCipherParams_Destroy(params);
        return ret;
    }
    ret = OH_CryptoSymCipher_Init(decCtx, CRYPTO_DECRYPT_MODE, ctx->symKey, params);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoSymCipher_Destroy(decCtx);
        OH_CryptoSymCipherParams_Destroy(params);
        return ret;
    }
    ret = OH_CryptoSymCipher_Final(decCtx, cipherText, plainText);
    OH_CryptoSymCipher_Destroy(decCtx);
    OH_CryptoSymCipherParams_Destroy(params);
    return ret;
}

void CleanupDataBlob(Crypto_DataBlob *plainData, Crypto_DataBlob *cipherData, Crypto_DataBlob *tagBlob)
{
    OH_Crypto_FreeDataBlob(plainData);
    OH_Crypto_FreeDataBlob(cipherData);
    OH_Crypto_FreeDataBlob(tagBlob);
}

void CleanupContext(CryptoContext *ctx)
{
    OH_Crypto_FreeDataBlob(&ctx->secret);
    OH_CryptoSymKey_Destroy(ctx->symKey);
    OH_CryptoKeyPair_Destroy(ctx->keyPair);
}
} // namespace ECIES

OH_Crypto_ErrCode doNativeTest()
{
    ECIES::CryptoContext ctxA = {};
    ECIES::CryptoContext ctxB = {};
    Crypto_DataBlob plainData = {};
    Crypto_DataBlob cipherData = {};
    Crypto_DataBlob tagBlob = {};
    OH_Crypto_ErrCode ret = CRYPTO_INVALID_PARAMS;
    do {
        ret = ECIES::GenerateKeyPair(&ctxA.keyPair);
        if (ret != CRYPTO_SUCCESS) {
            break;
        }
        ret = ECIES::GenerateKeyPair(&ctxB.keyPair);
        if (ret != CRYPTO_SUCCESS) {
            break;
        }

        // A端密钥协商：A端的私钥 + B端的公钥
        ret = ECIES::KdfDeriveSecret(OH_CryptoKeyPair_GetPrivKey(ctxA.keyPair),
            OH_CryptoKeyPair_GetPubKey(ctxB.keyPair), &ctxA.secret);
        if (ret != CRYPTO_SUCCESS) {
            break;
        }
        ret = ECIES::GenerateSymKey(&ctxA.secret, &ctxA.symKey);
        if (ret != CRYPTO_SUCCESS) {
            break;
        }
        // 使用A端派生密钥的前16字节作为加解密端的IV
        ECIES::SetCipherIvData(&ctxA, &ctxA.secret);
        ECIES::SetCipherIvData(&ctxB, &ctxA.secret);
        // A端加密
        uint8_t message[] = { 0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B };
        Crypto_DataBlob plainText = { .data = message, .len = sizeof(message) };
        ret = ECIES::Encrypt(&ctxA, &plainText, &cipherData, &tagBlob);
        if (ret != CRYPTO_SUCCESS) {
            break;
        }

        // B端密钥协商：B端的私钥 + A端的公钥
        ret = ECIES::KdfDeriveSecret(OH_CryptoKeyPair_GetPrivKey(ctxB.keyPair),
            OH_CryptoKeyPair_GetPubKey(ctxA.keyPair), &ctxB.secret);
        if (ret != CRYPTO_SUCCESS) {
            break;
        }
        ret = ECIES::GenerateSymKey(&ctxB.secret, &ctxB.symKey);
        if (ret != CRYPTO_SUCCESS) {
            break;
        }
        // B端解密
        ret = ECIES::Decrypt(&ctxB, &cipherData, &plainData, &tagBlob);
    } while (0);

    ECIES::CleanupDataBlob(&plainData, &cipherData, &tagBlob);
    ECIES::CleanupContext(&ctxA);
    ECIES::CleanupContext(&ctxB);
    OH_LOG_INFO(LOG_APP, "doNativeTest result: %{public}s", (ret == 0 ? "Success" : "Failed"));
    return ret;
}
```
