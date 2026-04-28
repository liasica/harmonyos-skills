---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/-convert-compressed-or-uncompressed-ecc-pubkey-ndk
title: 使用ECC压缩/非压缩公钥格式转换(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成和转换 > 密钥生成和转换开发指导 > 使用ECC压缩/非压缩公钥格式转换(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:19+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:94840181926c41d862523fb2dd3fa777e7a7abc30acb4c7d354df2d055a79bb9
---

可通过指定ECC公钥数据生成公钥对象（[PubKey](../harmonyos-references/capi-cryptoasymkeyapi-oh-cryptopubkey.md)），也可从公钥对象中获取ECC公钥数据。

当前仅支持满足X509规范的ECC算法的压缩或非压缩格式的完整公钥数据。此处的公钥数据应当是完整的X509公钥，对于仅使用点数据的情况，请参考[使用ECC压缩/非压缩点格式转换](rypto-convert-compressed-or-uncompressed-ecc-point.md)。

查看[非对称密钥生成和转换规格：ECC](crypto-asym-key-generation-conversion-spec.md#ecc)。

通过传入字符串参数，可指定需要获取的ECC公钥数据格式。如果需要获取满足X509规范的压缩格式数据，则指定参数为："X509|COMPRESSED"；需要获取非压缩格式，则指定参数为："X509|UNCOMPRESSED"。

## 指定非压缩公钥数据转换为压缩公钥数据

1. 指定uint8\_t类型的ECC非压缩公钥数据，封装成[Crypto\_DataBlob](../harmonyos-references/capi-cryptocommonapi-crypto-datablob.md)。

   公钥和私钥可单独传入，此处示例传入非压缩公钥。
2. 调用[OH\_CryptoAsymKeyGenerator\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_generate)，指定字符串参数'ECC\_BrainPoolP256r1'，创建密钥算法为ECC、密钥长度为256位的非对称密钥生成器（OH\_CryptoAsymKeyGenerator）。
3. 调用[OH\_CryptoAsymKeyGenerator\_Convert](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_convert)，传入封装后的[Crypto\_DataBlob](../harmonyos-references/capi-cryptocommonapi-crypto-datablob.md)，生成非对称密钥对象（OH\_CryptoKeyPair）。
4. 调用[OH\_CryptoPubKey\_Encode](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptopubkey_encode)，设置参数为'X509|COMPRESSED'，获取压缩公钥数据的字节流。

```
1. #include "CryptoArchitectureKit/crypto_common.h"
2. #include "CryptoArchitectureKit/crypto_asym_key.h"

4. OH_Crypto_ErrCode doTestEccDataCovert()
5. {
6. OH_CryptoAsymKeyGenerator *generator = nullptr;
7. OH_CryptoKeyPair *keyPair = nullptr;
8. Crypto_DataBlob returnBlob = { .data = nullptr, .len = 0 };
9. OH_Crypto_ErrCode ret = CRYPTO_INVALID_PARAMS;

11. ret = OH_CryptoAsymKeyGenerator_Create("ECC_BrainPoolP256r1", &generator);
12. if (ret != CRYPTO_SUCCESS) {
13. return ret;
14. }
15. uint8_t pubKeyBlobData[] = {
16. 48, 90, 48, 20, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 9, 43, 36, 3, 3, 2,
17. 8, 1, 1, 7, 3, 66, 0, 4, 143, 39, 57, 249, 145, 50, 63, 222, 35, 70, 178,
18. 121, 202, 154, 21, 146, 129, 75, 76, 63, 8, 195, 157, 111, 40, 217, 215,
19. 148, 120, 224, 205, 82, 83, 92, 185, 21, 211, 184, 5, 19, 114, 33, 86, 85,
20. 228, 123, 242, 206, 200, 98, 178, 184, 130, 35, 232, 45, 5, 202, 189, 11,
21. 46, 163, 156, 152
22. };
23. Crypto_DataBlob pubKeyUncompressedBlob = {
24. .data = pubKeyBlobData,
25. .len = sizeof(pubKeyBlobData),
26. };
27. ret = OH_CryptoAsymKeyGenerator_Convert(generator, CRYPTO_DER, &pubKeyUncompressedBlob, nullptr, &keyPair);
28. if (ret != CRYPTO_SUCCESS) {
29. OH_CryptoAsymKeyGenerator_Destroy(generator);
30. return ret;
31. }

33. OH_CryptoPubKey *pubKey = OH_CryptoKeyPair_GetPubKey(keyPair);
34. ret = OH_CryptoPubKey_Encode(pubKey, CRYPTO_DER, "X509|COMPRESSED", &returnBlob);
35. if (ret != CRYPTO_SUCCESS) {
36. OH_CryptoAsymKeyGenerator_Destroy(generator);
37. OH_CryptoKeyPair_Destroy(keyPair);
38. return ret;
39. }
40. OH_Crypto_FreeDataBlob(&returnBlob);
41. OH_CryptoAsymKeyGenerator_Destroy(generator);
42. OH_CryptoKeyPair_Destroy(keyPair);
43. return ret;
44. }
```

[specifyUncompressedPublicKey.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/ECCCompressPublicKeyFormatConversion/entry/src/main/cpp/types/project/specifyUncompressedPublicKey.cpp#L16-L60)
