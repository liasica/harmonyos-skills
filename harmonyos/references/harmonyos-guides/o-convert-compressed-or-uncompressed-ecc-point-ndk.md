---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/o-convert-compressed-or-uncompressed-ecc-point-ndk
title: 使用ECC压缩/非压缩点格式转换(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成和转换 > 密钥生成和转换开发指导 > 使用ECC压缩/非压缩点格式转换(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6637f6907469d70a455a7354b793141746cdcd7952cf7db182ca82e7460d6855
---

支持将压缩/非压缩的点数据，转换为Point对象，用于密钥对象生成；也支持将Point对象转换为压缩/非压缩的点数据。

ECC的算法规格请查看[非对称密钥生成和转换规格：ECC](crypto-asym-key-generation-conversion-spec.md#ecc)。

通过传入字符串参数format，可指定获取的点数据格式。如果获取压缩格式，则指定format为："COMPRESSED"；获取非压缩格式，则指定format为："UNCOMPRESSED"。

## 指定非压缩点数据转换为压缩点数据

1. 指定uint8\_t类型的ECC非压缩点数据，调用[OH\_CryptoEcPoint\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoecpoint_create)，构造[OH\_CryptoEcPoint](../harmonyos-references/capi-cryptoasymkeyapi-oh-cryptoecpoint.md)对象，用于生成点数据。
2. 调用[OH\_CryptoEcPoint\_Encode](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoecpoint_encode)，获取压缩点数据。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"

3. OH_Crypto_ErrCode doTestEccPointUncompressedToCompressed()
4. {
5. uint8_t pk[] = {
6. 4, 143, 39, 57, 249, 145, 50, 63, 222, 35, 70, 178, 121, 202, 154, 21, 146, 129, 75, 76, 63, 8, 195, 157, 111,
7. 40, 217, 215, 148, 120, 224, 205, 82, 83, 92, 185, 21, 211, 184, 5, 19, 114, 33, 86, 85, 228, 123, 242, 206,
8. 200, 98, 178, 184, 130, 35, 232, 45, 5, 202, 189, 11, 46, 163, 156, 152
9. };
10. Crypto_DataBlob pkData = {pk, sizeof(pk)};
11. OH_CryptoEcPoint *point = nullptr;
12. OH_Crypto_ErrCode ret = OH_CryptoEcPoint_Create("NID_brainpoolP256r1", &pkData, &point);
13. if (ret != CRYPTO_SUCCESS) {
14. return ret;
15. }
16. Crypto_DataBlob returnPointBlobData = {0};
17. ret = OH_CryptoEcPoint_Encode(point, "COMPRESSED", &returnPointBlobData);
18. if (ret != CRYPTO_SUCCESS) {
19. OH_CryptoEcPoint_Destroy(point);
20. return ret;
21. }
22. OH_Crypto_FreeDataBlob(&returnPointBlobData);
23. OH_CryptoEcPoint_Destroy(point);
24. return ret;
25. }
```

[compressedPointData.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/ECCCompressPublicKeyFormatConversion/entry/src/main/cpp/types/project/compressedPointData.cpp#L16-L42)

## 指定压缩点数据获取密钥对象

1. 指定uint8\_t类型的ECC压缩点数据，调用[OH\_CryptoEcPoint\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoecpoint_create)，构造[OH\_CryptoEcPoint](../harmonyos-references/capi-cryptoasymkeyapi-oh-cryptoecpoint.md)对象，用于生成点数据。
2. 调用[OH\_CryptoEcPoint\_Encode](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoecpoint_encode)，获取非压缩点数据。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"

3. OH_Crypto_ErrCode doTestEccPointCompressedToPoint()
4. {
5. uint8_t pk[] = {
6. 2, 143, 39, 57, 249, 145, 50, 63, 222, 35, 70, 178, 121, 202, 154, 21, 146, 129, 75, 76, 63, 8, 195, 157, 111,
7. 40, 217, 215, 148, 120, 224, 205, 82
8. };
9. Crypto_DataBlob pkData = {pk, sizeof(pk)};
10. OH_CryptoEcPoint *point = nullptr;
11. OH_Crypto_ErrCode ret = OH_CryptoEcPoint_Create("NID_brainpoolP256r1", &pkData, &point);
12. if (ret != CRYPTO_SUCCESS) {
13. return ret;
14. }
15. Crypto_DataBlob returnPointBlobData = {0};
16. ret = OH_CryptoEcPoint_Encode(point, "UNCOMPRESSED", &returnPointBlobData);
17. if (ret != CRYPTO_SUCCESS) {
18. OH_CryptoEcPoint_Destroy(point);
19. return ret;
20. }
21. OH_Crypto_FreeDataBlob(&returnPointBlobData);
22. OH_CryptoEcPoint_Destroy(point);
23. return ret;
24. }
```

[getKeyObject.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/ECCCompressPublicKeyFormatConversion/entry/src/main/cpp/types/project/getKeyObject.cpp#L16-L41)
