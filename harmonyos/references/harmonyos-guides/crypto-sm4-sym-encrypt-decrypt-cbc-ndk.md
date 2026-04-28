---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-cbc-ndk
title: 使用SM4对称密钥（CBC模式）加解密(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用SM4对称密钥（CBC模式）加解密(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f7dfaa332501bbfb9f4a78851260984559665d670457c99b2b87c0e3a3884d34
---

对应的算法规格请查看[对称密钥加解密算法规格：SM4](crypto-sym-encrypt-decrypt-spec.md#sm4)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libohcrypto.so)
```

**加密**

1. 调用[OH\_CryptoSymKeyGenerator\_Create](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_create)、[OH\_CryptoSymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_generate)，生成密钥算法为SM4、密钥长度为128位的对称密钥（OH\_CryptoSymKey）。

   如何生成SM4对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：SM4](crypto-sym-key-generation-conversion-spec.md#sm4)和[随机生成对称密钥](crypto-generate-sym-key-randomly-ndk.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'SM4\_128|CBC|PKCS7'，创建对称密钥类型为SM4\_128、分组模式为CBC、填充模式为PKCS7的Cipher实例，用于完成加密操作。
3. 调用[OH\_CryptoSymCipherParams\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_create)创建参数对象，调用[OH\_CryptoSymCipherParams\_SetParam](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_setparam)设置对应的加密参数。
4. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（OH\_CryptoSymKey）和CBC模式对应的加密参数（OH\_CryptoSymCipherParams），初始化加密Cipher实例。
5. 调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，更新数据（明文）。

   * 当数据量较小时，可以在init完成后直接调用final。
   * 当数据量较大时，可以多次调用update，即分段加解密。
6. 调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，获取加密后的数据。

   * 由于已使用update传入数据，此处data传入null。
   * final输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。
7. 调用[OH\_CryptoSymKeyGenerator\_Destroy](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_destroy)、[OH\_CryptoSymCipher\_Destroy](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_destroy)、[OH\_CryptoSymCipherParams\_Destroy](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_destroy)销毁各对象。

**解密**

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'SM4\_128|CBC|PKCS7'，创建对称密钥类型为SM4\_128、分组模式为CBC、填充模式为PKCS7的Cipher实例，用于完成解密操作。
2. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（OH\_CryptoSymKey）和CBC模式对应的解密参数（OH\_CryptoSymCipherParams），初始化解密Cipher实例。
3. 调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，更新数据（密文）。
4. 调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，获取解密后的数据。

```
1. #include "CryptoArchitectureKit/crypto_common.h"
2. #include "CryptoArchitectureKit/crypto_sym_cipher.h"
3. #include <cstring>
4. // ...

6. OH_Crypto_ErrCode doTestSm4Cbc()
7. {
8. OH_CryptoSymKeyGenerator *genCtx = nullptr;
9. OH_CryptoSymCipher *encCtx = nullptr;
10. OH_CryptoSymCipher *decCtx = nullptr;
11. OH_CryptoSymKey *keyCtx = nullptr;
12. OH_CryptoSymCipherParams *params = nullptr;
13. Crypto_DataBlob outUpdate = {.data = nullptr, .len = 0};
14. Crypto_DataBlob decUpdate = {.data = nullptr, .len = 0};

16. char *plainText = const_cast<char *>("this is test!");
17. Crypto_DataBlob msgBlob = {.data = (uint8_t *)(plainText), .len = strlen(plainText)};
18. uint8_t iv[16] = {1, 2, 4, 12, 3, 4, 2, 3, 3, 2, 0, 4, 3, 1, 0, 10}; // iv使用安全随机数生成
19. Crypto_DataBlob ivBlob = {.data = iv, .len = sizeof(iv)};
20. // 生成对称密钥
21. OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create("SM4_128", &genCtx);
22. if (ret != CRYPTO_SUCCESS) {
23. goto end;
24. }
25. ret = OH_CryptoSymKeyGenerator_Generate(genCtx, &keyCtx);
26. if (ret != CRYPTO_SUCCESS) {
27. goto end;
28. }

30. // 设置参数
31. ret = OH_CryptoSymCipherParams_Create(&params);
32. if (ret != CRYPTO_SUCCESS) {
33. goto end;
34. }
35. ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_IV_DATABLOB, &ivBlob);
36. if (ret != CRYPTO_SUCCESS) {
37. goto end;
38. }

40. // 加密
41. ret = OH_CryptoSymCipher_Create("SM4_128|CBC|PKCS7", &encCtx);
42. if (ret != CRYPTO_SUCCESS) {
43. goto end;
44. }
45. ret = OH_CryptoSymCipher_Init(encCtx, CRYPTO_ENCRYPT_MODE, keyCtx, params);
46. if (ret != CRYPTO_SUCCESS) {
47. goto end;
48. }
49. ret = OH_CryptoSymCipher_Final(encCtx, &msgBlob, &outUpdate);
50. if (ret != CRYPTO_SUCCESS) {
51. goto end;
52. }

54. // 解密
55. ret = OH_CryptoSymCipher_Create("SM4_128|CBC|PKCS7", &decCtx);
56. if (ret != CRYPTO_SUCCESS) {
57. goto end;
58. }
59. ret = OH_CryptoSymCipher_Init(decCtx, CRYPTO_DECRYPT_MODE, keyCtx, params);
60. if (ret != CRYPTO_SUCCESS) {
61. goto end;
62. }
63. ret = OH_CryptoSymCipher_Final(decCtx, &outUpdate, &decUpdate);
64. if (ret != CRYPTO_SUCCESS) {
65. goto end;
66. }

68. // 资源释放
69. end:
70. OH_CryptoSymCipherParams_Destroy(params);
71. OH_CryptoSymCipher_Destroy(encCtx);
72. OH_CryptoSymCipher_Destroy(decCtx);
73. OH_CryptoSymKeyGenerator_Destroy(genCtx);
74. OH_CryptoSymKey_Destroy(keyCtx);
75. OH_Crypto_FreeDataBlob(&outUpdate);
76. OH_Crypto_FreeDataBlob(&decUpdate);
77. return ret;
78. }
```

[sm4\_cbc\_encryption\_decryption.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceSM4/entry/src/main/cpp/types/project/sm4_cbc_encryption_decryption.cpp#L16-L97)
