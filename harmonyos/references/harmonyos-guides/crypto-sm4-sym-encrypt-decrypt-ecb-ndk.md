---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-ecb-ndk
title: 使用SM4对称密钥（ECB模式）加解密(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用SM4对称密钥（ECB模式）加解密(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5b0a90a5904c5c84fdcdf2a11ebb7b6e2131a32e0ccf5269699151a71e08a5e7
---

对应的算法规格请查看[对称密钥加解密算法规格：SM4](crypto-sym-encrypt-decrypt-spec.md#sm4)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libohcrypto.so)
```

**加密**

1. 调用[OH\_CryptoSymKeyGenerator\_Create](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_create)、[OH\_CryptoSymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_generate)，生成密钥算法为SM4、密钥长度为128位的对称密钥（OH\_CryptoSymKey）。

   如何生成SM4对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：SM4](crypto-sym-key-generation-conversion-spec.md#sm4)和[随机生成对称密钥](crypto-generate-sym-key-randomly-ndk.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'SM4\_128|ECB|PKCS7'，创建对称密钥类型为SM4\_128、分组模式为ECB、填充模式为PKCS7的Cipher实例，用于完成加密操作。
3. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（OH\_CryptoSymKey），初始化加密Cipher实例。

   ECB模式无加密参数，直接传入null。
4. 调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，更新数据（明文）。

   * 当数据量较小时，可以在init完成后直接调用final。
   * 当数据量较大时，可以多次调用update，即分段加解密。
5. 调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，获取加密后的数据。

   * 由于已使用update传入数据，此处data传入null。
   * final输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。
6. 调用[OH\_CryptoSymKeyGenerator\_Destroy](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_destroy)、[OH\_CryptoSymCipher\_Destroy](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_destroy)、[OH\_CryptoSymCipherParams\_Destroy](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_destroy)销毁各对象。

**解密**

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'SM4\_128|ECB|PKCS7'，创建对称密钥类型为SM4\_128、分组模式为ECB、填充模式为PKCS7的Cipher实例，用于完成解密操作。
2. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（OH\_CryptoSymKey）初始化解密Cipher实例。ECB模式无加密参数，直接传入null。
3. 调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，更新数据（密文）。
4. 调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，获取解密后的数据。

```
1. #include "CryptoArchitectureKit/crypto_common.h"
2. #include "CryptoArchitectureKit/crypto_sym_cipher.h"
3. #include <cstring>
4. // ...

6. OH_Crypto_ErrCode doTestSm4Ecb()
7. {
8. OH_CryptoSymKeyGenerator *genCtx = nullptr;
9. OH_CryptoSymCipher *encCtx = nullptr;
10. OH_CryptoSymCipher *decCtx = nullptr;
11. OH_CryptoSymKey *keyCtx = nullptr;
12. OH_CryptoSymCipherParams *params = nullptr;
13. char *plainText = const_cast<char *>("this is test!");
14. Crypto_DataBlob input = {.data = (uint8_t *)(plainText), .len = strlen(plainText)};
15. Crypto_DataBlob outUpdate = {.data = nullptr, .len = 0};
16. Crypto_DataBlob decUpdate = {.data = nullptr, .len = 0};

18. // 随机生成对称密钥
19. OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create("SM4_128", &genCtx);
20. if (ret != CRYPTO_SUCCESS) {
21. goto end;
22. }
23. ret = OH_CryptoSymKeyGenerator_Generate(genCtx, &keyCtx);
24. if (ret != CRYPTO_SUCCESS) {
25. goto end;
26. }
27. // 创建参数
28. ret = OH_CryptoSymCipherParams_Create(&params);
29. if (ret != CRYPTO_SUCCESS) {
30. goto end;
31. }

33. // 加密操作
34. ret = OH_CryptoSymCipher_Create("SM4_128|ECB|PKCS7", &encCtx);
35. if (ret != CRYPTO_SUCCESS) {
36. goto end;
37. }
38. ret = OH_CryptoSymCipher_Init(encCtx, CRYPTO_ENCRYPT_MODE, keyCtx, params);
39. if (ret != CRYPTO_SUCCESS) {
40. goto end;
41. }
42. ret = OH_CryptoSymCipher_Final(encCtx, &input, &outUpdate);
43. if (ret != CRYPTO_SUCCESS) {
44. goto end;
45. }

47. // 解密操作
48. ret = OH_CryptoSymCipher_Create("SM4_128|ECB|PKCS7", &decCtx);
49. if (ret != CRYPTO_SUCCESS) {
50. goto end;
51. }
52. ret = OH_CryptoSymCipher_Init(decCtx, CRYPTO_DECRYPT_MODE, keyCtx, params);
53. if (ret != CRYPTO_SUCCESS) {
54. goto end;
55. }
56. ret = OH_CryptoSymCipher_Final(decCtx, &outUpdate, &decUpdate);
57. if (ret != CRYPTO_SUCCESS) {
58. goto end;
59. }
60. // 释放资源
61. end:
62. OH_CryptoSymCipherParams_Destroy(params);
63. OH_CryptoSymCipher_Destroy(encCtx);
64. OH_CryptoSymCipher_Destroy(decCtx);
65. OH_CryptoSymKeyGenerator_Destroy(genCtx);
66. OH_CryptoSymKey_Destroy(keyCtx);
67. OH_Crypto_FreeDataBlob(&outUpdate);
68. OH_Crypto_FreeDataBlob(&decUpdate);
69. return ret;
70. }
```

[sm4\_ecb\_encryption\_decryption.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceSM4/entry/src/main/cpp/types/project/sm4_ecb_encryption_decryption.cpp#L16-L89)
