---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-compressed-or-uncompressed-ecc-point-ndk
title: 使用ECC压缩/非压缩点格式转换(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成与转换 > 使用ECC压缩/非压缩点格式转换(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:00+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:da547f70dccbdba78e4bca9d2d33e540faf9ae23efd2ba65ff057b1341cb0e14
---

支持将压缩/非压缩的点数据，转换为Point对象，用于密钥对象生成；也支持将Point对象转换为压缩/非压缩的点数据。

ECC的算法规格请查看[非对称密钥生成和转换规格：ECC](crypto-key-generation-conversion.md#ecc)。

通过传入字符串参数format，可指定获取的点数据格式。如果获取压缩格式，则指定format为："COMPRESSED"；获取非压缩格式，则指定format为："UNCOMPRESSED"。

## 指定非压缩点数据转换为压缩点数据

1. 指定uint8\_t类型的ECC非压缩点数据，调用[OH\_CryptoEcPoint\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoecpoint_create)，构造[OH\_CryptoEcPoint](../harmonyos-references/capi-cryptoasymkeyapi-oh-cryptoecpoint.md)对象，用于生成点数据。
2. 调用[OH\_CryptoEcPoint\_Encode](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoecpoint_encode)，获取压缩点数据。

```
#include "CryptoArchitectureKit/crypto_architecture_kit.h"

OH_Crypto_ErrCode doTestEccPointUncompressedToCompressed()
{
    uint8_t pk[] = {
        4, 143, 39, 57, 249, 145, 50, 63, 222, 35, 70, 178, 121, 202, 154, 21, 146, 129, 75, 76, 63, 8, 195, 157, 111,
        40, 217, 215, 148, 120, 224, 205, 82, 83, 92, 185, 21, 211, 184, 5, 19, 114, 33, 86, 85, 228, 123, 242, 206,
        200, 98, 178, 184, 130, 35, 232, 45, 5, 202, 189, 11, 46, 163, 156, 152
    };
    Crypto_DataBlob pkData = {pk, sizeof(pk)};
    OH_CryptoEcPoint *point = nullptr;
    OH_Crypto_ErrCode ret = OH_CryptoEcPoint_Create("NID_brainpoolP256r1", &pkData, &point);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }
    Crypto_DataBlob returnPointBlobData = {0};
    ret = OH_CryptoEcPoint_Encode(point, "COMPRESSED", &returnPointBlobData);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoEcPoint_Destroy(point);
        return ret;
    }
    OH_Crypto_FreeDataBlob(&returnPointBlobData);
    OH_CryptoEcPoint_Destroy(point);
    return ret;
}
```

## 指定压缩点数据获取密钥对象

1. 指定uint8\_t类型的ECC压缩点数据，调用[OH\_CryptoEcPoint\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoecpoint_create)，构造[OH\_CryptoEcPoint](../harmonyos-references/capi-cryptoasymkeyapi-oh-cryptoecpoint.md)对象，用于生成点数据。
2. 调用[OH\_CryptoEcPoint\_Encode](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoecpoint_encode)，获取非压缩点数据。

```
#include "CryptoArchitectureKit/crypto_architecture_kit.h"

OH_Crypto_ErrCode doTestEccPointCompressedToPoint()
{
    uint8_t pk[] = {
        2, 143, 39, 57, 249, 145, 50, 63, 222, 35, 70, 178, 121, 202, 154, 21, 146, 129, 75, 76, 63, 8, 195, 157, 111,
        40, 217, 215, 148, 120, 224, 205, 82
    };
    Crypto_DataBlob pkData = {pk, sizeof(pk)};
    OH_CryptoEcPoint *point = nullptr;
    OH_Crypto_ErrCode ret = OH_CryptoEcPoint_Create("NID_brainpoolP256r1", &pkData, &point);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }
    Crypto_DataBlob returnPointBlobData = {0};
    ret = OH_CryptoEcPoint_Encode(point, "UNCOMPRESSED", &returnPointBlobData);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoEcPoint_Destroy(point);
        return ret;
    }
    OH_Crypto_FreeDataBlob(&returnPointBlobData);
    OH_CryptoEcPoint_Destroy(point);
    return ret;
}
```
