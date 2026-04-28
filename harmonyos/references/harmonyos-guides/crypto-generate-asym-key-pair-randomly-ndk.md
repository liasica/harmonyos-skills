---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-randomly-ndk
title: 随机生成非对称密钥对(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成和转换 > 密钥生成和转换开发指导 > 随机生成非对称密钥对(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:17+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:0d7be829d4c72b65a73aa87633d870de7fbc1c397185ef0686c2f0306fd4bfca
---

以RSA和SM2为例，随机生成非对称密钥对（OH\_CryptoKeyPair），并获得二进制数据。

非对称密钥对可用于后续加解密等操作，二进制数据可用于存储或传输。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libohcrypto.so)
```

## 随机生成RSA密钥对

对应的算法规格请查看[非对称密钥生成和转换规格：RSA](crypto-asym-key-generation-conversion-spec.md#rsa)。

1. 调用[OH\_CryptoAsymKeyGenerator\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_create)，指定字符串参数'RSA1024|PRIMES\_2'，创建RSA密钥类型为RSA1024、素数个数为2的非对称密钥生成器（OH\_CryptoAsymKeyGenerator）。
2. 调用[OH\_CryptoAsymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_generate)，随机生成非对称密钥对象（OH\_CryptoKeyPair）。
3. 调用[OH\_CryptoPubKey\_Encode](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptopubkey_encode)获取公钥密钥对象的二进制数据。

```
1. #include "CryptoArchitectureKit/crypto_common.h"
2. #include "CryptoArchitectureKit/crypto_asym_key.h"
3. #include "file.h"

5. OH_Crypto_ErrCode generateRSAKey()
6. {
7. OH_CryptoAsymKeyGenerator *ctx = nullptr;
8. OH_CryptoKeyPair *keyPair = nullptr;
9. OH_Crypto_ErrCode ret;

11. ret = OH_CryptoAsymKeyGenerator_Create("RSA1024|PRIMES_2", &ctx);
12. if (ret != CRYPTO_SUCCESS) {
13. OH_CryptoAsymKeyGenerator_Destroy(ctx);
14. return ret;
15. }

17. ret = OH_CryptoAsymKeyGenerator_Generate(ctx, &keyPair);
18. if (ret != CRYPTO_SUCCESS) {
19. OH_CryptoAsymKeyGenerator_Destroy(ctx);
20. OH_CryptoKeyPair_Destroy(keyPair);
21. return ret;
22. }

24. OH_CryptoPubKey *pubKey = OH_CryptoKeyPair_GetPubKey(keyPair);
25. Crypto_DataBlob retBlob = {.data = nullptr, .len = 0};
26. ret = OH_CryptoPubKey_Encode(pubKey, CRYPTO_PEM, "PKCS1", &retBlob);
27. if (ret != CRYPTO_SUCCESS) {
28. OH_CryptoAsymKeyGenerator_Destroy(ctx);
29. OH_CryptoKeyPair_Destroy(keyPair);
30. return ret;
31. }

33. OH_Crypto_FreeDataBlob(&retBlob);

35. OH_CryptoAsymKeyGenerator_Destroy(ctx);
36. OH_CryptoKeyPair_Destroy(keyPair);
37. return ret;
38. }
```

[rsa.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/RandomlyGenerateAsymmetricKeyPair/entry/src/main/cpp/types/project/rsa.cpp#L16-L55)

## 随机生成SM2密钥对

对应的算法规格请查看[非对称密钥生成和转换规格：SM2](crypto-asym-key-generation-conversion-spec.md#sm2)。

1. 调用[OH\_CryptoAsymKeyGenerator\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_create)，指定字符串参数'SM2\_256'，创建密钥算法为SM2、密钥长度为256位的非对称密钥生成器（OH\_CryptoAsymKeyGenerator）。
2. 调用[OH\_CryptoAsymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_generate)，随机生成非对称密钥对象（OH\_CryptoKeyPair）。
3. 调用[OH\_CryptoPubKey\_Encode](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptopubkey_encode)获取公钥密钥对象的二进制数据。

```
1. #include "CryptoArchitectureKit/crypto_common.h"
2. #include "CryptoArchitectureKit/crypto_asym_key.h"
3. #include "file.h"

5. OH_Crypto_ErrCode generateSM2Key()
6. {
7. OH_CryptoAsymKeyGenerator *ctx = nullptr;
8. OH_CryptoKeyPair *dupKeyPair = nullptr;
9. OH_Crypto_ErrCode ret;

11. ret = OH_CryptoAsymKeyGenerator_Create("SM2_256", &ctx);
12. if (ret != CRYPTO_SUCCESS) {
13. OH_CryptoAsymKeyGenerator_Destroy(ctx);
14. return ret;
15. }

17. ret = OH_CryptoAsymKeyGenerator_Generate(ctx, &dupKeyPair);
18. if (ret != CRYPTO_SUCCESS) {
19. OH_CryptoAsymKeyGenerator_Destroy(ctx);
20. OH_CryptoKeyPair_Destroy(dupKeyPair);
21. return ret;
22. }

24. OH_CryptoPubKey *pubKey = OH_CryptoKeyPair_GetPubKey(dupKeyPair);
25. Crypto_DataBlob retBlob = { .data = nullptr, .len = 0 };
26. ret = OH_CryptoPubKey_Encode(pubKey, CRYPTO_DER, nullptr, &retBlob);
27. if (ret != CRYPTO_SUCCESS) {
28. OH_CryptoAsymKeyGenerator_Destroy(ctx);
29. OH_CryptoKeyPair_Destroy(dupKeyPair);
30. return ret;
31. }

33. OH_Crypto_FreeDataBlob(&retBlob);
34. OH_CryptoAsymKeyGenerator_Destroy(ctx);
35. OH_CryptoKeyPair_Destroy(dupKeyPair);
36. return ret;
37. }
```

[sm2.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/RandomlyGenerateAsymmetricKeyPair/entry/src/main/cpp/types/project/sm2.cpp#L16-L53)
