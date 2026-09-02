---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-wrap-encrypt-decrypt-ndk
title: 使用AES-WRAP算法对对称密钥加解密(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密介绍 > 使用AES-WRAP算法对对称密钥加解密(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:00+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:83e682dfdf4a547b4b7a50905b9679f65e17866c16e74c35d24cdb86033b4576
---

从API版本22开始，算法库支持使用该算法进行加密和解密操作。

请查看[AES-WRAP加解密算法规格](crypto-encryption-decryption.md#aes-wrap)。

## 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libohcrypto.so)
```

## 开发步骤

**创建对象**

调用[OH\_CryptoSymKeyGenerator\_Create](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_create)和[OH\_CryptoSymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_generate)，生成密钥算法为AES、密钥长度为128位的对称密钥（OH\_CryptoSymKey）。

如何生成AES对称密钥，请参考以下示例，并结合[对称密钥生成和转换规格：AES](crypto-key-generation-conversion.md#aes)和[随机生成对称密钥](crypto-generate-sym-key-randomly-ndk.md)理解，参考文档与当前示例可能存在入参差异，请注意区分。

**加密**

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'AES128-WRAP'，创建对称密钥类型为AES128-WRAP的Cipher实例，用于加密操作。
2. 调用[OH\_CryptoSymCipherParams\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_create)创建参数对象，并调用[OH\_CryptoSymCipherParams\_SetParam](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_setparam)设置加密参数。
3. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（OH\_CryptoSymKey）和对应的加密参数（OH\_CryptoSymCipherParams），初始化加密Cipher实例。
4. 加密内容较短时，可以直接调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，无需调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，获取加密后的数据。

**解密**

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'AES128-WRAP'，创建对称密钥类型为AES128-WRAP的Cipher实例，用于解密操作。
2. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（OH\_CryptoSymKey）和对应的解密参数（OH\_CryptoSymCipherParams），初始化解密Cipher实例。
3. 解密内容较短时，可直接调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，无需调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，获取解密后的数据。

**销毁对象**

调用[OH\_CryptoSymKeyGenerator\_Destroy](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_destroy)、[OH\_CryptoSymCipher\_Destroy](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_destroy)、[OH\_CryptoSymKey\_Destroy](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkey_destroy)、[OH\_Crypto\_FreeDataBlob](../harmonyos-references/capi-crypto-common-h.md#oh_crypto_freedatablob)释放申请的内存，销毁对象。

```
#include "CryptoArchitectureKit/crypto_common.h"
#include "CryptoArchitectureKit/crypto_sym_cipher.h"
#include <cstring>
#include "file.h"

// 加密函数
static OH_Crypto_ErrCode doAesWrapEncrypt(OH_CryptoSymKey *keyCtx, OH_CryptoSymCipherParams *params,
    Crypto_DataBlob *msgBlob, Crypto_DataBlob *encData)
{
    OH_CryptoSymCipher *encCtx = nullptr;
    OH_Crypto_ErrCode ret = OH_CryptoSymCipher_Create("AES128-WRAP", &encCtx);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }
    ret = OH_CryptoSymCipher_Init(encCtx, CRYPTO_ENCRYPT_MODE, keyCtx, params);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }
    ret = OH_CryptoSymCipher_Final(encCtx, msgBlob, encData);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }

end:
    OH_CryptoSymCipher_Destroy(encCtx);
    return ret;
}

// 解密函数
static OH_Crypto_ErrCode doAesWrapDecrypt(OH_CryptoSymKey *keyCtx, OH_CryptoSymCipherParams *params,
    Crypto_DataBlob *encData, Crypto_DataBlob *decData)
{
    OH_CryptoSymCipher *decCtx = nullptr;
    OH_Crypto_ErrCode ret = OH_CryptoSymCipher_Create("AES128-WRAP", &decCtx);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }
    ret = OH_CryptoSymCipher_Init(decCtx, CRYPTO_DECRYPT_MODE, keyCtx, params); // 解密使用的params与加密时相同。
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }
    ret = OH_CryptoSymCipher_Final(decCtx, encData, decData);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }

end:
    OH_CryptoSymCipher_Destroy(decCtx);
    return ret;
}

OH_Crypto_ErrCode doTestAesWrap()
{
    OH_CryptoSymKeyGenerator *genCtx = nullptr;
    OH_CryptoSymKey *keyCtx = nullptr;
    OH_CryptoSymCipherParams *params = nullptr;
    Crypto_DataBlob encData = {.data = nullptr, .len = 0};
    Crypto_DataBlob decData = {.data = nullptr, .len = 0};
    uint8_t keyData[] = {0xb7, 0x21, 0x3d, 0x4f, 0x63, 0x57, 0x9b, 0x97,
        0x09, 0xd9, 0x80, 0x6f, 0x9f, 0x3a, 0x6f, 0x64};
    Crypto_DataBlob msgBlob = {.data = keyData, .len = sizeof(keyData)};
    uint8_t iv[8] = {1, 2, 4, 12, 3, 4, 2, 3}; // 示例代码iv值，开发者可使用安全随机数生成。
    Crypto_DataBlob ivBlob = {.data = iv, .len = sizeof(iv)};
    // 生成对称密钥。
    OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create("AES128", &genCtx);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }
    ret = OH_CryptoSymKeyGenerator_Generate(genCtx, &keyCtx);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }

    // 创建参数对象。
    ret = OH_CryptoSymCipherParams_Create(&params);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }
    // 设置参数。
    ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_IV_DATABLOB, &ivBlob); // aes-wrap只需要设置iv。
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }

    // 加密。
    ret = doAesWrapEncrypt(keyCtx, params, &msgBlob, &encData);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }

    // 解密。
    ret = doAesWrapDecrypt(keyCtx, params, &encData, &decData);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }

end:
    OH_CryptoSymCipherParams_Destroy(params);
    OH_CryptoSymKeyGenerator_Destroy(genCtx);
    OH_CryptoSymKey_Destroy(keyCtx);
    OH_Crypto_FreeDataBlob(&encData);
    OH_Crypto_FreeDataBlob(&decData);
    return ret;
}
```
