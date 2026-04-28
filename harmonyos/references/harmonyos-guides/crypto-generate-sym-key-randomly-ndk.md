---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-sym-key-randomly-ndk
title: 随机生成对称密钥(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成和转换 > 密钥生成和转换开发指导 > 随机生成对称密钥(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8afa6a5acd75fd3d5600bdbedc4d29861bb095764b3d0eb77e74b01f29f72f52
---

以AES和SM4为例，随机生成对称密钥（OH\_CryptoSymKey）。

对称密钥对象可用于后续加解密操作，二进制数据可用于存储或传输。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libohcrypto.so)
```

## 随机生成AES密钥

对应的算法规格请查看[对称密钥生成和转换规格：AES](crypto-sym-key-generation-conversion-spec.md#aes)。

1. 调用[OH\_CryptoSymKeyGenerator\_Create](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_create)，指定字符串参数'AES256'，创建密钥算法为AES、密钥长度为256位的对称密钥生成器（OH\_CryptoSymKeyGenerator）。
2. 调用[OH\_CryptoSymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_generate)，随机生成对称密钥对象（OH\_CryptoSymKey）。
3. 调用[OH\_CryptoSymKey\_GetKeyData](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkey_getkeydata)，获取密钥对象的二进制数据。

```
1. #include "CryptoArchitectureKit/crypto_common.h"
2. #include "CryptoArchitectureKit/crypto_sym_key.h"
3. #include "file.h"

5. OH_Crypto_ErrCode testGenerateSymKey()
6. {
7. OH_CryptoSymKeyGenerator *ctx = nullptr;
8. OH_CryptoSymKey *keyCtx = nullptr;
9. Crypto_DataBlob out = {.data = nullptr, .len = 0};
10. OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create("AES256", &ctx);
11. if (ret != CRYPTO_SUCCESS) {
12. return ret;
13. }
14. ret = OH_CryptoSymKeyGenerator_Generate(ctx, &keyCtx);
15. if (ret != CRYPTO_SUCCESS) {
16. OH_CryptoSymKeyGenerator_Destroy(ctx);
17. return ret;
18. }
19. ret = OH_CryptoSymKey_GetKeyData(keyCtx, &out);
20. OH_CryptoSymKeyGenerator_Destroy(ctx);
21. OH_CryptoSymKey_Destroy(keyCtx);
22. if (ret != CRYPTO_SUCCESS) {
23. return ret;
24. }
25. OH_Crypto_FreeDataBlob(&out);
26. return ret;
27. }
```

## 随机生成SM4密钥

对应的算法规格请查看[对称密钥生成和转换规格：SM4](crypto-sym-key-generation-conversion-spec.md#sm4)。

1. 调用[OH\_CryptoSymKeyGenerator\_Create](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_create)，指定字符串参数'SM4\_128'，创建密钥算法为SM4、密钥长度为128位的对称密钥生成器（OH\_CryptoSymKeyGenerator）。
2. 调用[OH\_CryptoSymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_generate)，随机生成对称密钥对象（OH\_CryptoSymKey）。
3. 调用[OH\_CryptoSymKey\_GetKeyData](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkey_getkeydata)，获取密钥对象的二进制数据。

```
1. #include "CryptoArchitectureKit/crypto_common.h"
2. #include "CryptoArchitectureKit/crypto_sym_key.h"
3. #include "file.h"

5. OH_Crypto_ErrCode testGenerateSM4Key()
6. {
7. OH_CryptoSymKeyGenerator *ctx = nullptr;
8. OH_CryptoSymKey *keyCtx = nullptr;
9. Crypto_DataBlob out = {.data = nullptr, .len = 0};
10. OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create("SM4_128", &ctx);
11. if (ret != CRYPTO_SUCCESS) {
12. return ret;
13. }
14. ret = OH_CryptoSymKeyGenerator_Generate(ctx, &keyCtx);
15. if (ret != CRYPTO_SUCCESS) {
16. OH_CryptoSymKeyGenerator_Destroy(ctx);
17. return ret;
18. }
19. ret = OH_CryptoSymKey_GetKeyData(keyCtx, &out);
20. OH_CryptoSymKeyGenerator_Destroy(ctx);
21. OH_CryptoSymKey_Destroy(keyCtx);
22. if (ret != CRYPTO_SUCCESS) {
23. return ret;
24. }
25. OH_Crypto_FreeDataBlob(&out);
26. return ret;
27. }
```

[sm4.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/RandomlyGenerateSymmetricKey/entry/src/main/cpp/types/project/sm4.cpp#L16-L44)
