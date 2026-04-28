---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-string-data-to-asym-key-pair-ndk
title: 指定PEM格式字符串数据转换非对称密钥对(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成和转换 > 密钥生成和转换开发指导 > 指定PEM格式字符串数据转换非对称密钥对(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:454d0cfe175e46d8eeb73178d452e0c2ca0117f522e7551fc286455572f1fd17
---

以RSA为例，根据指定的非对称密钥字符串数据，生成非对称密钥对（OH\_CryptoKeyPair）。

说明

针对非对称密钥的convertPemKey操作：

* 公钥需满足X.509规范、PKCS#1规范、PEM编码格式。
* 私钥需满足PKCS#8规范、PKCS#1规范、PEM编码格式。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libohcrypto.so)
```

## 指定PEM格式字符串数据转换RSA密钥对

对应的算法规格请查看[非对称密钥生成和转换规格：RSA](crypto-asym-key-generation-conversion-spec.md#rsa)。

1. 调用[OH\_CryptoAsymKeyGenerator\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_create)，指定字符串参数'RSA1024'，创建RSA密钥类型为RSA1024、素数个数为2的非对称密钥生成器（OH\_CryptoAsymKeyGenerator）。

   生成RSA非对称密钥时，默认素数为2，此处省略了参数PRIMES\_2。
2. 调用[OH\_CryptoAsymKeyGenerator\_Convert](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_convert)，传入二进制密钥数据，生成非对称密钥对象（OH\_CryptoKeyPair）。
3. 调用[OH\_CryptoPubKey\_Encode](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptopubkey_encode)，将非对称密钥对象中的公钥转换成pkcs1或x509格式。

* 以下以生成RSA密钥对为例：

  ```
  1. #include "CryptoArchitectureKit/crypto_common.h"
  2. #include "CryptoArchitectureKit/crypto_asym_key.h"
  3. #include "file.h"

  5. OH_Crypto_ErrCode doTestPemDataCovertAsymKey()
  6. {
  7. OH_CryptoAsymKeyGenerator *ctx = nullptr;
  8. OH_Crypto_ErrCode ret;

  10. ret = OH_CryptoAsymKeyGenerator_Create("RSA1024", &ctx);
  11. if (ret != CRYPTO_SUCCESS) {
  12. return ret;
  13. }

  15. uint8_t sm2PubKeyBlobData[] = {
  16. 48,  129, 159, 48,  13,  6,   9,   42,  134, 72,  134, 247, 13,  1,   1,   1,   5,   0,   3,   129, 141,
  17. 0,   48,  129, 137, 2,   129, 129, 0,   235, 184, 151, 247, 130, 216, 140, 187, 64,  124, 219, 137, 140,
  18. 184, 53,  137, 216, 105, 156, 141, 137, 165, 30,  80,  232, 55,  96,  46,  23,  237, 197, 123, 121, 27,
  19. 240, 190, 14,  111, 237, 172, 67,  42,  47,  164, 226, 248, 211, 157, 213, 194, 131, 109, 181, 41,  173,
  20. 217, 127, 252, 121, 126, 26,  130, 55,  4,   134, 104, 73,  5,   132, 91,  214, 146, 232, 64,  99,  87,
  21. 33,  222, 155, 159, 9,   59,  212, 144, 46,  183, 83,  89,  220, 189, 148, 13,  176, 5,   139, 156, 230,
  22. 143, 16,  152, 79,  36,  8,   112, 40,  174, 35,  83,  82,  57,  137, 87,  123, 215, 99,  199, 66,  131,
  23. 150, 31,  143, 56,  252, 2,   73,  41,  70,  159, 2,   3,   1,   0,   1};

  25. OH_CryptoKeyPair *dupKeyPair = nullptr;
  26. Crypto_DataBlob pubBlob = {.data = sm2PubKeyBlobData, .len = sizeof(sm2PubKeyBlobData)};
  27. ret = OH_CryptoAsymKeyGenerator_Convert(ctx, CRYPTO_DER, &pubBlob, nullptr, &dupKeyPair);
  28. if (ret != CRYPTO_SUCCESS) {
  29. OH_CryptoAsymKeyGenerator_Destroy(ctx);
  30. return ret;
  31. }

  33. OH_CryptoPubKey *pubKey1 = OH_CryptoKeyPair_GetPubKey(dupKeyPair);
  34. Crypto_DataBlob retBlob = {.data = nullptr, .len = 0};
  35. ret = OH_CryptoPubKey_Encode(pubKey1, CRYPTO_PEM, "PKCS1", &retBlob);
  36. if (ret != CRYPTO_SUCCESS) {
  37. OH_CryptoAsymKeyGenerator_Destroy(ctx);
  38. OH_CryptoKeyPair_Destroy(dupKeyPair);
  39. return ret;
  40. }
  41. OH_Crypto_FreeDataBlob(&retBlob);
  42. OH_CryptoAsymKeyGenerator_Destroy(ctx);
  43. OH_CryptoKeyPair_Destroy(dupKeyPair);
  44. return ret;
  45. }
  ```

  [rsa.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/ConvertSpecifiedPEMAsymmetricKeyPair/entry/src/main/cpp/types/project/rsa.cpp#L16-L62)
