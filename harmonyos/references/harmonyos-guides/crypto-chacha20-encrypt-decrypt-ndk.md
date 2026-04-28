---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-chacha20-encrypt-decrypt-ndk
title: 使用ChaCha20对称密钥加解密(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用ChaCha20对称密钥加解密(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3898fbd4c103e54b2d9ab66b4296d2af9546cd7b51a6768848b7b45ae67f6324
---

从API22开始，算法库支持该算法。

对应的算法规格请查看[对称密钥加解密算法规格：ChaCha20](crypto-sym-encrypt-decrypt-spec.md#chacha20)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libohcrypto.so)
```

## 开发步骤

**创建对象**

调用[OH\_CryptoSymKeyGenerator\_Create](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_create)、[OH\_CryptoSymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_generate)，生成密钥算法为ChaCha20的对称密钥（OH\_CryptoSymKey）。

如何生成ChaCha20对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：ChaCha20](crypto-sym-key-generation-conversion-spec.md#chacha20)和[随机生成对称密钥](crypto-generate-sym-key-randomly-ndk.md)理解。参考文档与示例可能存在入参差异，请注意区分。

**加密**

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'ChaCha20'，创建对称密钥类型为ChaCha20的Cipher实例，用于完成加密操作。
2. 调用[OH\_CryptoSymCipherParams\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_create)创建参数对象，调用[OH\_CryptoSymCipherParams\_SetParam](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_setparam)设置对应的加密参数。
3. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（OH\_CryptoSymKey）和对应的加密参数（OH\_CryptoSymCipherParams），初始化加密Cipher实例。
4. 调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，更新数据（明文）。
5. 调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，获取加密后的数据。

   说明

   由于已使用update传入数据，此处data传入null。

   doFinal输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。
6. 调用[OH\_CryptoSymKeyGenerator\_Destroy](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_destroy)、[OH\_CryptoSymCipher\_Destroy](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_destroy)、[OH\_CryptoSymCipherParams\_Destroy](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_destroy)销毁各对象。

**解密**

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'ChaCha20'，创建对称密钥类型为ChaCha20的Cipher实例，用于完成解密操作。
2. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（OH\_CryptoSymKey）和对应的解密参数（OH\_CryptoSymCipherParams），初始化解密Cipher实例。
3. 调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，更新数据（密文）。
4. 调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，获取解密后的数据。

```
1. #include "CryptoArchitectureKit/crypto_common.h"
2. #include "CryptoArchitectureKit/crypto_sym_cipher.h"
3. #include <cstring>
4. #include "file.h"

6. // 参数赋值函数
7. static OH_Crypto_ErrCode doChaCha20SetParams(Crypto_DataBlob *ivBlob, OH_CryptoSymCipherParams **params)
8. {
9. OH_Crypto_ErrCode ret = OH_CryptoSymCipherParams_Create(params);
10. if (ret != CRYPTO_SUCCESS) {
11. return ret;
12. }
13. ret = OH_CryptoSymCipherParams_SetParam(*params, CRYPTO_IV_DATABLOB, ivBlob);
14. if (ret != CRYPTO_SUCCESS) {
15. OH_CryptoSymCipherParams_Destroy(*params);
16. *params = nullptr;
17. return ret;
18. }
19. return ret;
20. }

22. // 加密函数
23. static OH_Crypto_ErrCode doChaCha20Encrypt(OH_CryptoSymKey *keyCtx, OH_CryptoSymCipherParams *params,
24. Crypto_DataBlob *msgBlob, Crypto_DataBlob *encData)
25. {
26. OH_CryptoSymCipher *encCtx = nullptr;
27. OH_Crypto_ErrCode ret = OH_CryptoSymCipher_Create("ChaCha20", &encCtx);
28. if (ret != CRYPTO_SUCCESS) {
29. goto end;
30. }
31. ret = OH_CryptoSymCipher_Init(encCtx, CRYPTO_ENCRYPT_MODE, keyCtx, params);
32. if (ret != CRYPTO_SUCCESS) {
33. goto end;
34. }
35. ret = OH_CryptoSymCipher_Final(encCtx, msgBlob, encData);
36. if (ret != CRYPTO_SUCCESS) {
37. goto end;
38. }

40. end:
41. OH_CryptoSymCipher_Destroy(encCtx);
42. return ret;
43. }

45. // 解密函数
46. static OH_Crypto_ErrCode doChaCha20Decrypt(OH_CryptoSymKey *keyCtx, OH_CryptoSymCipherParams *params,
47. Crypto_DataBlob *encData, Crypto_DataBlob *decData)
48. {
49. OH_CryptoSymCipher *decCtx = nullptr;
50. OH_Crypto_ErrCode ret = OH_CryptoSymCipher_Create("ChaCha20", &decCtx);
51. if (ret != CRYPTO_SUCCESS) {
52. goto end;
53. }
54. ret = OH_CryptoSymCipher_Init(decCtx, CRYPTO_DECRYPT_MODE, keyCtx, params); // 解密使用的params与加密时相同。
55. if (ret != CRYPTO_SUCCESS) {
56. goto end;
57. }
58. ret = OH_CryptoSymCipher_Final(decCtx, encData, decData);
59. if (ret != CRYPTO_SUCCESS) {
60. goto end;
61. }

63. end:
64. OH_CryptoSymCipher_Destroy(decCtx);
65. return ret;
66. }

68. OH_Crypto_ErrCode doTestChaCha20()
69. {
70. OH_CryptoSymKeyGenerator *genCtx = nullptr;
71. OH_CryptoSymKey *keyCtx = nullptr;
72. OH_CryptoSymCipherParams *params = nullptr;
73. Crypto_DataBlob encData = {.data = nullptr, .len = 0};
74. Crypto_DataBlob decData = {.data = nullptr, .len = 0};
75. char *plainText = const_cast<char *>("this is test!");
76. Crypto_DataBlob msgBlob = {.data = (uint8_t *)(plainText), .len = strlen(plainText)};
77. uint8_t iv[16] = {1, 2, 4, 12, 3, 4, 2, 3, 3, 2, 0, 4, 3, 1, 0, 10}; // 示例代码iv值，开发者可使用安全随机数生成。
78. Crypto_DataBlob ivBlob = {.data = iv, .len = sizeof(iv)};
79. // 生成对称密钥。
80. OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create("ChaCha20", &genCtx);
81. if (ret != CRYPTO_SUCCESS) {
82. goto end;
83. }
84. ret = OH_CryptoSymKeyGenerator_Generate(genCtx, &keyCtx);
85. if (ret != CRYPTO_SUCCESS) {
86. goto end;
87. }

89. // 参数赋值。
90. ret = doChaCha20SetParams(&ivBlob, &params);
91. if (ret != CRYPTO_SUCCESS) {
92. goto end;
93. }

95. // 加密。
96. ret = doChaCha20Encrypt(keyCtx, params, &msgBlob, &encData);
97. if (ret != CRYPTO_SUCCESS) {
98. goto end;
99. }

101. // 解密。
102. ret = doChaCha20Decrypt(keyCtx, params, &encData, &decData);
103. if (ret != CRYPTO_SUCCESS) {
104. goto end;
105. }

107. end:
108. OH_CryptoSymCipherParams_Destroy(params);
109. OH_CryptoSymKeyGenerator_Destroy(genCtx);
110. OH_CryptoSymKey_Destroy(keyCtx);
111. OH_Crypto_FreeDataBlob(&encData);
112. OH_Crypto_FreeDataBlob(&decData);
113. return ret;
114. }
```

[chacha20\_encryption\_decryption.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceChaCha20/entry/src/main/cpp/types/project/chacha20_encryption_decryption.cpp#L16-L131)
