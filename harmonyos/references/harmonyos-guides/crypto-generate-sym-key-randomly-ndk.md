---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-sym-key-randomly-ndk
title: 随机生成对称密钥(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成与转换 > 随机生成对称密钥(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3d68639dde1e40e9aca34a39f4dac1443edc6cb9180c89310b3e53cd13807d72
---

以AES和SM4为例，随机生成对称密钥（OH\_CryptoSymKey）。

对称密钥对象可用于后续加解密操作，二进制数据可用于存储或传输。

## 在CMake脚本中链接相关动态库

```txt
target_link_libraries(entry PUBLIC libohcrypto.so)
```

## 随机生成AES密钥

对应的算法规格请查看[对称密钥生成和转换规格：AES](crypto-key-generation-conversion.md#aes)。

1. 调用[OH\_CryptoSymKeyGenerator\_Create](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_create)，指定字符串参数'AES256'，创建密钥算法为AES、密钥长度为256位的对称密钥生成器（OH\_CryptoSymKeyGenerator）。
2. 调用[OH\_CryptoSymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_generate)，随机生成对称密钥对象（OH\_CryptoSymKey）。
3. 调用[OH\_CryptoSymKey\_GetKeyData](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkey_getkeydata)，获取密钥对象的二进制数据。

```
#include "CryptoArchitectureKit/crypto_common.h"
#include "CryptoArchitectureKit/crypto_sym_key.h"
#include "file.h"

OH_Crypto_ErrCode testGenerateSymKey()
{
    OH_CryptoSymKeyGenerator *ctx = nullptr;
    OH_CryptoSymKey *keyCtx = nullptr;
    Crypto_DataBlob out = {.data = nullptr, .len = 0};
    OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create("AES256", &ctx);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }
    ret = OH_CryptoSymKeyGenerator_Generate(ctx, &keyCtx);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoSymKeyGenerator_Destroy(ctx);
        return ret;
    }
    ret = OH_CryptoSymKey_GetKeyData(keyCtx, &out);
    OH_CryptoSymKeyGenerator_Destroy(ctx);
    OH_CryptoSymKey_Destroy(keyCtx);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }
    OH_Crypto_FreeDataBlob(&out);
    return ret;
}
```

## 随机生成SM4密钥

对应的算法规格请查看[对称密钥生成和转换规格：SM4](crypto-key-generation-conversion.md#sm4)。

1. 调用[OH\_CryptoSymKeyGenerator\_Create](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_create)，指定字符串参数'SM4\_128'，创建密钥算法为SM4、密钥长度为128位的对称密钥生成器（OH\_CryptoSymKeyGenerator）。
2. 调用[OH\_CryptoSymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_generate)，随机生成对称密钥对象（OH\_CryptoSymKey）。
3. 调用[OH\_CryptoSymKey\_GetKeyData](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkey_getkeydata)，获取密钥对象的二进制数据。

```
#include "CryptoArchitectureKit/crypto_common.h"
#include "CryptoArchitectureKit/crypto_sym_key.h"
#include "file.h"

OH_Crypto_ErrCode testGenerateSM4Key()
{
    OH_CryptoSymKeyGenerator *ctx = nullptr;
    OH_CryptoSymKey *keyCtx = nullptr;
    Crypto_DataBlob out = {.data = nullptr, .len = 0};
    OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create("SM4_128", &ctx);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }
    ret = OH_CryptoSymKeyGenerator_Generate(ctx, &keyCtx);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoSymKeyGenerator_Destroy(ctx);
        return ret;
    }
    ret = OH_CryptoSymKey_GetKeyData(keyCtx, &out);
    OH_CryptoSymKeyGenerator_Destroy(ctx);
    OH_CryptoSymKey_Destroy(keyCtx);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }
    OH_Crypto_FreeDataBlob(&out);
    return ret;
}
```
