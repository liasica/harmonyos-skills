---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm-ndk
title: 使用AES对称密钥（GCM模式）加解密(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用AES对称密钥（GCM模式）加解密(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0c3f9b67c1e700fa9ff523c0c7820523d95e52418649fcb635c542da0feffeb6
---

对应的算法规格请查看[对称密钥加解密算法规格：AES](crypto-sym-encrypt-decrypt-spec.md#aes)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libohcrypto.so)
```

## 开发步骤

**创建对象**

调用[OH\_CryptoSymKeyGenerator\_Create](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_create)和[OH\_CryptoSymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_generate)，生成密钥算法为AES、密钥长度为128位的对称密钥（OH\_CryptoSymKey）。

生成AES对称密钥，参考以下示例，并结合[对称密钥生成和转换规格：AES](crypto-sym-key-generation-conversion-spec.md#aes)和[随机生成对称密钥](crypto-generate-sym-key-randomly-ndk.md)理解。注意，参考文档与示例可能有入参差异

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'AES128|GCM|PKCS7'，创建对称密钥类型为AES128、分组模式为GCM、填充模式为PKCS7的Cipher实例，用于完成加密操作。
2. 调用[OH\_CryptoSymCipherParams\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_create)创建参数对象，调用[OH\_CryptoSymCipherParams\_SetParam](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_setparam)设置对应的加密参数。
3. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定对称密钥（OH\_CryptoSymKey）和GCM模式对应的加密参数（OH\_CryptoSymCipherParams），以初始化加密Cipher实例。
4. 调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，更新数据（明文）。

   当前单次update长度没有限制，开发者可以根据数据量判断如何调用update。

   * 当数据量较小时，可以在init完成后直接调用final。
   * 当数据量较大时，可以多次调用update，即[分段加解密](crypto-aes-sym-encrypt-decrypt-gcm-by-segment-ndk.md)。
5. 调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，获取加密后的数据。

   * 由于已使用update传入数据，此处data传入null。
   * final输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。

   注意

   在GCM模式下，final会返回authTag，作为解密时初始化的认证信息，需要保存。GCM模式下，算法库当前只支持16字节的authTag。示例中authTag为16字节。

**解密**

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'AES128|GCM|PKCS7'，创建对称密钥类型为AES128、分组模式为GCM、填充模式为PKCS7的Cipher实例，用于完成解密操作。
2. 使用[OH\_CryptoSymCipherParams\_SetParam](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_setparam)设置authTag，作为解密的认证信息。
3. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（OH\_CryptoSymKey）和GCM模式对应的解密参数（OH\_CryptoSymCipherParams），初始化解密Cipher实例。
4. 调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，更新数据（密文）。
5. 调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，获取解密数据。

**销毁对象**

调用[OH\_CryptoSymKeyGenerator\_Destroy](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_destroy)、[OH\_CryptoSymCipher\_Destroy](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_destroy)、[OH\_CryptoSymCipherParams\_Destroy](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_destroy)销毁对象。

* AES GCM模式加解密示例如下：

```
1. #include "CryptoArchitectureKit/crypto_common.h"
2. #include "CryptoArchitectureKit/crypto_sym_cipher.h"
3. #include <cstring>
4. #include "file.h"

6. OH_Crypto_ErrCode doTestAesGcm()
7. {
8. OH_CryptoSymKeyGenerator *genCtx = nullptr;
9. OH_CryptoSymCipher *encCtx = nullptr;
10. OH_CryptoSymCipher *decCtx = nullptr;
11. OH_CryptoSymKey *keyCtx = nullptr;
12. OH_CryptoSymCipherParams *params = nullptr;

14. Crypto_DataBlob outUpdate = {.data = nullptr, .len = 0};
15. Crypto_DataBlob decUpdate = {.data = nullptr, .len = 0};

17. uint8_t aad[8] = {1, 2, 3, 4, 5, 6, 7, 8};
18. uint8_t tag[16] = {0};
19. uint8_t iv[12] = {1, 2, 4, 12, 3, 4, 2, 3, 3, 2, 0, 4}; // iv使用安全随机数生成
20. Crypto_DataBlob ivData = {.data = iv, .len = sizeof(iv)};
21. Crypto_DataBlob aadData = {.data = aad, .len = sizeof(aad)};
22. Crypto_DataBlob tagData = {.data = tag, .len = sizeof(tag)};
23. Crypto_DataBlob tagOutPut = {.data = nullptr, .len = 0};
24. char *plainText = const_cast<char *>("this is test!");
25. Crypto_DataBlob msgBlob = {.data = (uint8_t *)(plainText), .len = strlen(plainText)};

27. // 生成对称密钥
28. OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create("AES128", &genCtx);
29. if (ret != CRYPTO_SUCCESS) {
30. goto end;
31. }
32. ret = OH_CryptoSymKeyGenerator_Generate(genCtx, &keyCtx);
33. if (ret != CRYPTO_SUCCESS) {
34. goto end;
35. }

37. // 设置参数
38. ret = OH_CryptoSymCipherParams_Create(&params);
39. if (ret != CRYPTO_SUCCESS) {
40. goto end;
41. }
42. ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_IV_DATABLOB, &ivData);
43. if (ret != CRYPTO_SUCCESS) {
44. goto end;
45. }
46. ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_AAD_DATABLOB, &aadData);
47. if (ret != CRYPTO_SUCCESS) {
48. goto end;
49. }
50. ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_TAG_DATABLOB, &tagData);
51. if (ret != CRYPTO_SUCCESS) {
52. goto end;
53. }

55. // 加密
56. ret = OH_CryptoSymCipher_Create("AES128|GCM|PKCS7", &encCtx);
57. if (ret != CRYPTO_SUCCESS) {
58. goto end;
59. }
60. ret = OH_CryptoSymCipher_Init(encCtx, CRYPTO_ENCRYPT_MODE, keyCtx, params);
61. if (ret != CRYPTO_SUCCESS) {
62. goto end;
63. }
64. ret = OH_CryptoSymCipher_Update(encCtx, &msgBlob, &outUpdate);
65. if (ret != CRYPTO_SUCCESS) {
66. goto end;
67. }
68. ret = OH_CryptoSymCipher_Final(encCtx, nullptr, &tagOutPut);
69. if (ret != CRYPTO_SUCCESS) {
70. goto end;
71. }

73. // 解密
74. ret = OH_CryptoSymCipher_Create("AES128|GCM|PKCS7", &decCtx);
75. if (ret != CRYPTO_SUCCESS) {
76. goto end;
77. }
78. ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_TAG_DATABLOB, &tagOutPut);
79. if (ret != CRYPTO_SUCCESS) {
80. goto end;
81. }
82. ret = OH_CryptoSymCipher_Init(decCtx, CRYPTO_DECRYPT_MODE, keyCtx, params);
83. if (ret != CRYPTO_SUCCESS) {
84. goto end;
85. }
86. ret = OH_CryptoSymCipher_Final(decCtx, &outUpdate, &decUpdate);
87. if (ret != CRYPTO_SUCCESS) {
88. goto end;
89. }

91. end:
92. OH_CryptoSymCipherParams_Destroy(params);
93. OH_CryptoSymCipher_Destroy(encCtx);
94. OH_CryptoSymCipher_Destroy(decCtx);
95. OH_CryptoSymKeyGenerator_Destroy(genCtx);
96. OH_CryptoSymKey_Destroy(keyCtx);
97. OH_Crypto_FreeDataBlob(&outUpdate);
98. OH_Crypto_FreeDataBlob(&decUpdate);
99. OH_Crypto_FreeDataBlob(&tagOutPut);
100. return ret;
101. }
```

[aes\_gcm\_encryption\_decryption.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceAes/entry/src/main/cpp/types/project/aes_gcm_encryption_decryption.cpp#L16-L118)
