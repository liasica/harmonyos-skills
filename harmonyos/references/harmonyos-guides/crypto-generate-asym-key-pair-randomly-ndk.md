---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-randomly-ndk
title: 随机生成非对称密钥对(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成与转换 > 随机生成非对称密钥对(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:00+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cd96392c2a0b2455e5620d9e45e2fd0debe991fb7687a0ebb44f9b1da7342ed1
---

以RSA和SM2为例，随机生成非对称密钥对（OH\_CryptoKeyPair），并获得二进制数据。

非对称密钥对可用于后续加解密等操作，二进制数据可用于存储或传输。

## 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libohcrypto.so)
```

## 随机生成RSA密钥对

对应的算法规格请查看[非对称密钥生成和转换规格：RSA](crypto-key-generation-conversion.md#rsa)。

1. 调用[OH\_CryptoAsymKeyGenerator\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_create)，指定字符串参数'RSA1024|PRIMES\_2'，创建RSA密钥类型为RSA1024、素数个数为2的非对称密钥生成器（OH\_CryptoAsymKeyGenerator）。
2. 调用[OH\_CryptoAsymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_generate)，随机生成非对称密钥对象（OH\_CryptoKeyPair）。
3. 调用[OH\_CryptoPubKey\_Encode](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptopubkey_encode)获取公钥密钥对象的二进制数据。

```
#include "CryptoArchitectureKit/crypto_common.h"
#include "CryptoArchitectureKit/crypto_asym_key.h"
#include "file.h"

OH_Crypto_ErrCode generateRSAKey()
{
    OH_CryptoAsymKeyGenerator *ctx = nullptr;
    OH_CryptoKeyPair *keyPair = nullptr;
    OH_Crypto_ErrCode ret;

    ret = OH_CryptoAsymKeyGenerator_Create("RSA1024|PRIMES_2", &ctx);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymKeyGenerator_Destroy(ctx);
        return ret;
    }
    
    ret = OH_CryptoAsymKeyGenerator_Generate(ctx, &keyPair);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymKeyGenerator_Destroy(ctx);
        OH_CryptoKeyPair_Destroy(keyPair);
        return ret;
    }

    OH_CryptoPubKey *pubKey = OH_CryptoKeyPair_GetPubKey(keyPair);
    Crypto_DataBlob retBlob = {.data = nullptr, .len = 0};
    ret = OH_CryptoPubKey_Encode(pubKey, CRYPTO_PEM, "PKCS1", &retBlob);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymKeyGenerator_Destroy(ctx);
        OH_CryptoKeyPair_Destroy(keyPair);
        return ret;
    }

    OH_Crypto_FreeDataBlob(&retBlob);

    OH_CryptoAsymKeyGenerator_Destroy(ctx);
    OH_CryptoKeyPair_Destroy(keyPair);
    return ret;
}
```

## 随机生成SM2密钥对

对应的算法规格请查看[非对称密钥生成和转换规格：SM2](crypto-key-generation-conversion.md#sm2)。

1. 调用[OH\_CryptoAsymKeyGenerator\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_create)，指定字符串参数'SM2\_256'，创建密钥算法为SM2、密钥长度为256位的非对称密钥生成器（OH\_CryptoAsymKeyGenerator）。
2. 调用[OH\_CryptoAsymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_generate)，随机生成非对称密钥对象（OH\_CryptoKeyPair）。
3. 调用[OH\_CryptoPubKey\_Encode](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptopubkey_encode)获取公钥密钥对象的二进制数据。

```
#include "CryptoArchitectureKit/crypto_common.h"
#include "CryptoArchitectureKit/crypto_asym_key.h"
#include "file.h"

OH_Crypto_ErrCode generateSM2Key()
{
    OH_CryptoAsymKeyGenerator *ctx = nullptr;
    OH_CryptoKeyPair *dupKeyPair = nullptr;
    OH_Crypto_ErrCode ret;

    ret = OH_CryptoAsymKeyGenerator_Create("SM2_256", &ctx);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymKeyGenerator_Destroy(ctx);
        return ret;
    }

    ret = OH_CryptoAsymKeyGenerator_Generate(ctx, &dupKeyPair);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymKeyGenerator_Destroy(ctx);
        OH_CryptoKeyPair_Destroy(dupKeyPair);
        return ret;
    }

    OH_CryptoPubKey *pubKey = OH_CryptoKeyPair_GetPubKey(dupKeyPair);
    Crypto_DataBlob retBlob = { .data = nullptr, .len = 0 };
    ret = OH_CryptoPubKey_Encode(pubKey, CRYPTO_DER, nullptr, &retBlob);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymKeyGenerator_Destroy(ctx);
        OH_CryptoKeyPair_Destroy(dupKeyPair);
        return ret;
    }

    OH_Crypto_FreeDataBlob(&retBlob);
    OH_CryptoAsymKeyGenerator_Destroy(ctx);
    OH_CryptoKeyPair_Destroy(dupKeyPair);
    return ret;
}
```
