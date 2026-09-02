---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-x963kdf-ndk
title: 使用X963KDF进行密钥派生(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥派生介绍及算法规格 > 使用X963KDF进行密钥派生(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e0dd3278e9ef9d6180d1b41514dddcf006cb384808d19144d8187be156f99d9b
---

从API版本22开始，算法库支持使用该算法进行密钥派生操作。

对应算法规格请查看[密钥派生算法规格：X963KDF](crypto-key-derivation-overview.md#x963kdf算法)。

## 开发步骤

1. 调用[OH\_CryptoKdfParams\_Create](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdfparams_create)，指定字符串参数'X963KDF'，创建密钥派生参数对象。
2. 调用[OH\_CryptoKdfParams\_SetParam](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdfparams_setparam)，设置X963KDF所需的参数。示例如下：

   * CRYPTO\_KDF\_KEY\_DATABLOB：用于生成派生密钥的原始密钥材料。
   * CRYPTO\_KDF\_INFO\_DATABLOB：应用程序特定的信息（可选）。
3. 调用[OH\_CryptoKdf\_Create](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdf_create)，指定字符串参数'X963KDF|SHA256'，创建密钥派生函数对象。
4. 调用[OH\_CryptoKdf\_Derive](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdf_derive)，指定目标密钥的字节长度，进行密钥派生。

```
#include "CryptoArchitectureKit/crypto_architecture_kit.h"
#include <cstdio>
#include <cstring>
#include "file.h"

OH_Crypto_ErrCode doTestX963Kdf()
{
    // 创建X963KDF参数对象。
    OH_CryptoKdfParams *params = nullptr;
    OH_Crypto_ErrCode ret = OH_CryptoKdfParams_Create("X963KDF", &params);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }

    // 设置原始密钥材料。
    const char *keyData = "012345678901234567890123456789";
    Crypto_DataBlob key = {
        .data = reinterpret_cast<uint8_t *>(const_cast<char *>(keyData)),
        .len = strlen(keyData)
    };
    ret = OH_CryptoKdfParams_SetParam(params, CRYPTO_KDF_KEY_DATABLOB, &key);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoKdfParams_Destroy(params);
        return ret;
    }

    // 设置应用程序特定信息。
    const char *infoData = "infostring";
    Crypto_DataBlob info = {
        .data = reinterpret_cast<uint8_t *>(const_cast<char *>(infoData)),
        .len = strlen(infoData)
    };
    ret = OH_CryptoKdfParams_SetParam(params, CRYPTO_KDF_INFO_DATABLOB, &info);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoKdfParams_Destroy(params);
        return ret;
    }

    // 创建密钥派生函数对象。
    OH_CryptoKdf *kdfCtx = nullptr;
    ret = OH_CryptoKdf_Create("X963KDF|SHA256", &kdfCtx);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoKdfParams_Destroy(params);
        return ret;
    }

    // 派生密钥。
    Crypto_DataBlob out = {0};
    uint32_t keyLength = 32; // 生成32字节的密钥。
    ret = OH_CryptoKdf_Derive(kdfCtx, params, keyLength, &out);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoKdf_Destroy(kdfCtx);
        OH_CryptoKdfParams_Destroy(params);
        return ret;
    }

    printf("Derived key length: %u\n", out.len);

    // 清理资源。
    OH_Crypto_FreeDataBlob(&out);
    OH_CryptoKdf_Destroy(kdfCtx);
    OH_CryptoKdfParams_Destroy(params);
    return CRYPTO_SUCCESS;
}
```
