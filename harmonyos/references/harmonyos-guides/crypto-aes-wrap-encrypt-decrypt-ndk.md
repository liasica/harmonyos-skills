---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-wrap-encrypt-decrypt-ndk
title: 使用AES-WRAP算法对对称密钥加解密(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用AES-WRAP算法对对称密钥加解密(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c8a716d0d4f73cba22d636e21141a4840be7ea154ac61d325f0f06365b1a3c8a
---

从API version 22开始，算法库支持使用该算法进行加密和解密操作。

请查看[AES-WRAP加解密算法规格](crypto-sym-encrypt-decrypt-spec.md#aes-wrap)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libohcrypto.so)
```

## 开发步骤

**创建对象**

调用[OH\_CryptoSymKeyGenerator\_Create](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_create)和[OH\_CryptoSymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_generate)，生成密钥算法为AES、密钥长度为128位的对称密钥（OH\_CryptoSymKey）。

如何生成AES对称密钥，请参考以下示例，并结合[对称密钥生成和转换规格：AES](crypto-sym-key-generation-conversion-spec.md#aes)和[随机生成对称密钥](crypto-generate-sym-key-randomly-ndk.md)理解，参考文档与当前示例可能存在入参差异，请注意区分。

**加密**

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'AES128-WRAP'，创建对称密钥类型为AES128-WRAP的Cipher实例，用于加密操作。
2. 调用[OH\_CryptoSymCipherParams\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_create)创建参数对象，并调用[OH\_CryptoSymCipherParams\_SetParam](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_setparam)设置加密参数。
3. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（OH\_CryptoSymKey）和对应的加密参数（OH\_CryptoSymCipherParams），初始化加密Cipher实例。
4. 加密内容较短时，可以直接调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，无需调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，获取加密后的数据。

**解密**

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'AES128-WRAP'，创建对称密钥类型为AES128-WRAP的Cipher实例，用于解密操作。
2. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（OH\_CryptoSymKey）和对应的解密参数（OH\_CryptoSymCipherParams），初始化解密Cipher实例。
3. 解密内容较短时，可直接调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，无需调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，获取解密后的数据。

**销毁对象**

调用[OH\_CryptoSymKeyGenerator\_Destroy](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_destroy)、[OH\_CryptoSymCipher\_Destroy](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_destroy)、[OH\_CryptoSymKey\_Destroy](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkey_destroy)、[OH\_Crypto\_FreeDataBlob](../harmonyos-references/capi-crypto-common-h.md#oh_crypto_freedatablob)释放申请的内存，销毁对象。

```
1. #include "CryptoArchitectureKit/crypto_common.h"
2. #include "CryptoArchitectureKit/crypto_sym_cipher.h"
3. #include <cstring>
4. #include "file.h"

6. // 加密函数
7. static OH_Crypto_ErrCode doAesWrapEncrypt(OH_CryptoSymKey *keyCtx, OH_CryptoSymCipherParams *params,
8. Crypto_DataBlob *msgBlob, Crypto_DataBlob *encData)
9. {
10. OH_CryptoSymCipher *encCtx = nullptr;
11. OH_Crypto_ErrCode ret = OH_CryptoSymCipher_Create("AES128-WRAP", &encCtx);
12. if (ret != CRYPTO_SUCCESS) {
13. goto end;
14. }
15. ret = OH_CryptoSymCipher_Init(encCtx, CRYPTO_ENCRYPT_MODE, keyCtx, params);
16. if (ret != CRYPTO_SUCCESS) {
17. goto end;
18. }
19. ret = OH_CryptoSymCipher_Final(encCtx, msgBlob, encData);
20. if (ret != CRYPTO_SUCCESS) {
21. goto end;
22. }

24. end:
25. OH_CryptoSymCipher_Destroy(encCtx);
26. return ret;
27. }

29. // 解密函数
30. static OH_Crypto_ErrCode doAesWrapDecrypt(OH_CryptoSymKey *keyCtx, OH_CryptoSymCipherParams *params,
31. Crypto_DataBlob *encData, Crypto_DataBlob *decData)
32. {
33. OH_CryptoSymCipher *decCtx = nullptr;
34. OH_Crypto_ErrCode ret = OH_CryptoSymCipher_Create("AES128-WRAP", &decCtx);
35. if (ret != CRYPTO_SUCCESS) {
36. goto end;
37. }
38. ret = OH_CryptoSymCipher_Init(decCtx, CRYPTO_DECRYPT_MODE, keyCtx, params); // 解密使用的params与加密时相同。
39. if (ret != CRYPTO_SUCCESS) {
40. goto end;
41. }
42. ret = OH_CryptoSymCipher_Final(decCtx, encData, decData);
43. if (ret != CRYPTO_SUCCESS) {
44. goto end;
45. }

47. end:
48. OH_CryptoSymCipher_Destroy(decCtx);
49. return ret;
50. }

52. OH_Crypto_ErrCode doTestAesWrap()
53. {
54. OH_CryptoSymKeyGenerator *genCtx = nullptr;
55. OH_CryptoSymKey *keyCtx = nullptr;
56. OH_CryptoSymCipherParams *params = nullptr;
57. Crypto_DataBlob encData = {.data = nullptr, .len = 0};
58. Crypto_DataBlob decData = {.data = nullptr, .len = 0};
59. uint8_t keyData[] = {0xb7, 0x21, 0x3d, 0x4f, 0x63, 0x57, 0x9b, 0x97,
60. 0x09, 0xd9, 0x80, 0x6f, 0x9f, 0x3a, 0x6f, 0x64};
61. Crypto_DataBlob msgBlob = {.data = keyData, .len = sizeof(keyData)};
62. uint8_t iv[8] = {1, 2, 4, 12, 3, 4, 2, 3}; // 示例代码iv值，开发者可使用安全随机数生成。
63. Crypto_DataBlob ivBlob = {.data = iv, .len = sizeof(iv)};
64. // 生成对称密钥。
65. OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create("AES128", &genCtx);
66. if (ret != CRYPTO_SUCCESS) {
67. goto end;
68. }
69. ret = OH_CryptoSymKeyGenerator_Generate(genCtx, &keyCtx);
70. if (ret != CRYPTO_SUCCESS) {
71. goto end;
72. }

74. // 创建参数对象。
75. ret = OH_CryptoSymCipherParams_Create(&params);
76. if (ret != CRYPTO_SUCCESS) {
77. goto end;
78. }
79. // 设置参数。
80. ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_IV_DATABLOB, &ivBlob); // aes-wrap只需要设置iv。
81. if (ret != CRYPTO_SUCCESS) {
82. goto end;
83. }

85. // 加密。
86. ret = doAesWrapEncrypt(keyCtx, params, &msgBlob, &encData);
87. if (ret != CRYPTO_SUCCESS) {
88. goto end;
89. }

91. // 解密。
92. ret = doAesWrapDecrypt(keyCtx, params, &encData, &decData);
93. if (ret != CRYPTO_SUCCESS) {
94. goto end;
95. }

97. end:
98. OH_CryptoSymCipherParams_Destroy(params);
99. OH_CryptoSymKeyGenerator_Destroy(genCtx);
100. OH_CryptoSymKey_Destroy(keyCtx);
101. OH_Crypto_FreeDataBlob(&encData);
102. OH_Crypto_FreeDataBlob(&decData);
103. return ret;
104. }
```

[aes\_wrap\_encryption\_decryption.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceAesWrap/entry/src/main/cpp/project/aes_wrap_encryption_decryption.cpp#L16-L121)
