---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-binary-data-to-sym-key-ndk
title: 指定二进制数据转换对称密钥(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成和转换 > 密钥生成和转换开发指导 > 指定二进制数据转换对称密钥(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:abe900e358d1113edfb2df69ee312c5a2b843d6f42dfe7b398fe2a5d0d3bdff6
---

以3DES和HMAC为例，根据指定的对称密钥二进制数据生成密钥（OH\_CryptoSymKey），将外部或存储的二进制数据转换为算法库的密钥对象，该对象可用于后续的加解密操作。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libohcrypto.so)
```

## 指定二进制数据转换3DES密钥

查看[对称密钥生成和转换规格：3DES](crypto-sym-key-generation-conversion-spec.md#section3des)。

1. 获取3DES二进制密钥数据，封装成[Crypto\_DataBlob](../harmonyos-references/capi-cryptocommonapi-crypto-datablob.md)。
2. 调用[OH\_CryptoSymKeyGenerator\_Create](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_create)，指定字符串参数'3DES192'，创建密钥算法为3DES、密钥长度为192位的对称密钥生成器（OH\_CryptoSymKeyGenerator）。
3. 调用[OH\_CryptoSymKeyGenerator\_Convert](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_convert)，根据指定的对称密钥二进制数据生成对称密钥对象（OH\_CryptoSymKey）。
4. 调用[OH\_CryptoSymKey\_GetKeyData](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkey_getkeydata)，获取密钥对象的二进制数据。

以下以生成3DES密钥为例：

```
1. #include "CryptoArchitectureKit/crypto_common.h"
2. #include "CryptoArchitectureKit/crypto_sym_key.h"
3. #include "file.h"

5. OH_Crypto_ErrCode doTestDataCovertSymKey()
6. {
7. const char *algName = "3DES192";
8. OH_CryptoSymKeyGenerator *ctx = nullptr;
9. OH_CryptoSymKey *convertKeyCtx = nullptr;
10. Crypto_DataBlob out = {.data = nullptr, .len = 0};
11. OH_Crypto_ErrCode ret;
12. uint8_t arr[] = {0xba, 0x3d, 0xc2, 0x71, 0x21, 0x1e, 0x30, 0x56, 0xad, 0x47, 0xfc, 0x5a,
13. 0x46, 0x39, 0xee, 0x7c, 0xba, 0x3b, 0xc2, 0x71, 0xab, 0xa0, 0x30, 0x72};
14. Crypto_DataBlob convertBlob = {.data = arr, .len = sizeof(arr)};
15. ret = OH_CryptoSymKeyGenerator_Create(algName, &ctx);
16. if (ret != CRYPTO_SUCCESS) {
17. return ret;
18. }
19. ret = OH_CryptoSymKeyGenerator_Convert(ctx, &convertBlob, &convertKeyCtx);
20. if (ret != CRYPTO_SUCCESS) {
21. OH_CryptoSymKeyGenerator_Destroy(ctx);
22. return ret;
23. }
24. ret = OH_CryptoSymKey_GetKeyData(convertKeyCtx, &out);
25. OH_CryptoSymKeyGenerator_Destroy(ctx);
26. OH_CryptoSymKey_Destroy(convertKeyCtx);
27. if (ret != CRYPTO_SUCCESS) {
28. return ret;
29. }
30. OH_Crypto_FreeDataBlob(&out);
31. return ret;
32. }
```

[3des.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/ConvertSymmetricKeyBinaryFormat/entry/src/main/cpp/types/project/3des.cpp#L16-L49)

## 指定二进制数据转换HMAC密钥

查看[对称密钥生成和转换规格：HMAC](crypto-sym-key-generation-conversion-spec.md#hmac)。

1. 获取HMAC二进制密钥，封装成[Crypto\_DataBlob](../harmonyos-references/capi-cryptocommonapi-crypto-datablob.md)。
2. 调用[OH\_CryptoSymKeyGenerator\_Create](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_create)，指定字符串参数'HMAC'，创建密钥算法为HMAC、密钥长度为[1, 32768]位的对称密钥生成器（OH\_CryptoSymKeyGenerator）。
3. 调用[OH\_CryptoSymKeyGenerator\_Convert](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_convert)，根据指定的对称密钥二进制数据生成对称密钥对象（OH\_CryptoSymKey）。
4. 调用[OH\_CryptoSymKey\_GetKeyData](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkey_getkeydata)，获取密钥对象的二进制数据。

以下以生成HMAC密钥为例：

```
1. #include "CryptoArchitectureKit/crypto_common.h"
2. #include "CryptoArchitectureKit/crypto_sym_key.h"
3. #include <cstring>
4. #include "file.h"

6. OH_Crypto_ErrCode testConvertHmacKey()
7. {
8. const char *algName = "HMAC";
9. OH_CryptoSymKeyGenerator *ctx = nullptr;
10. OH_CryptoSymKey *convertKeyCtx = nullptr;
11. Crypto_DataBlob out = {.data = nullptr, .len = 0};
12. OH_Crypto_ErrCode ret;

14. char *arr = const_cast<char *>("12345678abcdefgh12345678abcdefgh12345678abcdefgh12345678abcdefgh");
15. Crypto_DataBlob convertBlob = {.data = (uint8_t *)(arr), .len = strlen(arr)};
16. ret = OH_CryptoSymKeyGenerator_Create(algName, &ctx);
17. if (ret != CRYPTO_SUCCESS) {
18. return ret;
19. }
20. ret = OH_CryptoSymKeyGenerator_Convert(ctx, &convertBlob, &convertKeyCtx);
21. if (ret != CRYPTO_SUCCESS) {
22. OH_CryptoSymKeyGenerator_Destroy(ctx);
23. return ret;
24. }
25. ret = OH_CryptoSymKey_GetKeyData(convertKeyCtx, &out);
26. OH_CryptoSymKeyGenerator_Destroy(ctx);
27. OH_CryptoSymKey_Destroy(convertKeyCtx);
28. if (ret != CRYPTO_SUCCESS) {
29. return ret;
30. }
31. OH_Crypto_FreeDataBlob(&out);
32. return ret;
33. }
```

[hmac.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/ConvertSymmetricKeyBinaryFormat/entry/src/main/cpp/types/project/hmac.cpp#L16-L50)
