---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-dh-ndk
title: 使用DH进行密钥协商(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥协商介绍及算法规格 > 使用DH进行密钥协商(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:524f47445b20bd93f77e00e0a492a3818f2092194d537cf5207341b5bc5ada2f
---

对应的算法规格请查看[密钥协商算法规格：DH](crypto-key-agreement-overview.md#dh)。

## 开发步骤

1. 调用[OH\_CryptoAsymKeyGenerator\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_create)、[OH\_CryptoAsymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_generate)生成密钥算法为DH\_modp1536的非对称密钥（keyPair）。

   如何生成DH非对称密钥，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：DH](crypto-key-generation-conversion.md#dh)和[随机生成非对称密钥对](crypto-generate-asym-key-pair-randomly-ndk.md)理解。参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[OH\_CryptoKeyAgreement\_Create](../harmonyos-references/capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_create)，指定字符串参数'DH\_modp1536'，创建密钥算法为DH\_modp1536的密钥协商生成器。
3. 调用[OH\_CryptoKeyAgreement\_GenerateSecret](../harmonyos-references/capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_generatesecret)，基于传入的私钥（keyPair.priKey）与公钥（keyPair.pubKey）进行密钥协商，返回共享密钥。

```
#include "CryptoArchitectureKit/crypto_architecture_kit.h"
#include "CryptoArchitectureKit/crypto_key_agreement.h"
#include "file.h"
#include <cstdio>
#include <cstring>

static OH_Crypto_ErrCode GenerateSecret(OH_CryptoKeyAgreement *dhKeyAgreement, OH_CryptoKeyPair *keyPairA,
    OH_CryptoKeyPair *keyPairB, Crypto_DataBlob *secret)
{
    OH_CryptoPrivKey *privKey = OH_CryptoKeyPair_GetPrivKey(keyPairA);
    OH_CryptoPubKey *pubKey = OH_CryptoKeyPair_GetPubKey(keyPairB);
    return OH_CryptoKeyAgreement_GenerateSecret(dhKeyAgreement, privKey, pubKey, secret);
}

static OH_Crypto_ErrCode compareSecrets(const Crypto_DataBlob *secret1, const Crypto_DataBlob *secret2)
{
    if ((secret1->len == secret2->len) &&
        (memcmp(secret1->data, secret2->data, secret1->len) == 0)) {
        return CRYPTO_SUCCESS;
    }
    return CRYPTO_OPERTION_ERROR;
}

OH_Crypto_ErrCode doTestDHKeyAgreement()
{
    OH_CryptoAsymKeyGenerator *dhGen = nullptr;
    OH_CryptoKeyPair *keyPairA = nullptr;
    OH_CryptoKeyPair *keyPairB = nullptr;
    OH_CryptoKeyAgreement *dhKeyAgreement = nullptr;
    Crypto_DataBlob secret1 = { 0 };
    Crypto_DataBlob secret2 = { 0 };
    OH_Crypto_ErrCode ret = OH_CryptoAsymKeyGenerator_Create("DH_modp1536", &dhGen);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }

    // 生成公私钥对A 和 B。
    ret = OH_CryptoAsymKeyGenerator_Generate(dhGen, &keyPairA);
    if (ret != CRYPTO_SUCCESS) {
        goto goto_cleanup;
    }

    ret = OH_CryptoAsymKeyGenerator_Generate(dhGen, &keyPairB);
    if (ret != CRYPTO_SUCCESS) {
        goto goto_cleanup;
    }

    ret = OH_CryptoKeyAgreement_Create("DH_modp1536", &dhKeyAgreement);
    if (ret != CRYPTO_SUCCESS) {
        goto goto_cleanup;
    }

    // 使用A的公钥和B的私钥进行密钥协商。
    ret = GenerateSecret(dhKeyAgreement, keyPairB, keyPairA, &secret1);
    if (ret != CRYPTO_SUCCESS) {
        goto goto_cleanup;
    }

    // 使用B的公钥和A的私钥进行密钥协商。
    ret = GenerateSecret(dhKeyAgreement, keyPairA, keyPairB, &secret2);
    if (ret != CRYPTO_SUCCESS) {
        goto goto_cleanup;
    }

    // 比较两次协商的结果。
    ret = compareSecrets(&secret1, &secret2);
    if (ret != CRYPTO_SUCCESS) {
        printf("dh result is not equal\n");
        goto goto_cleanup;
    }

goto_cleanup:
    OH_Crypto_FreeDataBlob(&secret1);
    OH_Crypto_FreeDataBlob(&secret2);
    OH_CryptoKeyAgreement_Destroy(dhKeyAgreement);
    OH_CryptoKeyPair_Destroy(keyPairA);
    OH_CryptoKeyPair_Destroy(keyPairB);
    OH_CryptoAsymKeyGenerator_Destroy(dhGen);
    return ret;
}
```
