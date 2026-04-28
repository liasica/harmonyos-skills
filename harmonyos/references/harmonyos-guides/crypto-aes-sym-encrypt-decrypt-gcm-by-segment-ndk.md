---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm-by-segment-ndk
title: 使用AES对称密钥（GCM模式）分段加解密(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用AES对称密钥（GCM模式）分段加解密(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:24+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:e9e94d4c6f4d06065a21c5f8398cc7a5deed713c9948248d395552967f417d12
---

对应的算法规格请查看[对称密钥加解密算法规格：AES](crypto-sym-encrypt-decrypt-spec.md#aes)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libohcrypto.so)
```

## 开发步骤

**创建对象**

调用[OH\_CryptoSymKeyGenerator\_Create](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_create)和[OH\_CryptoSymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_generate)，生成密钥算法为AES、密钥长度为128位的对称密钥（OH\_CryptoSymKey）。

如何生成AES对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：AES](crypto-sym-key-generation-conversion-spec.md#aes)和[随机生成对称密钥](crypto-generate-sym-key-randomly-ndk.md)文档进行理解。参考文档与当前示例可能存在入参差异，请注意区分。

**加密**

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'AES128|GCM|PKCS7'，创建对称密钥算法为AES128、分组模式为GCM、填充模式为PKCS7的Cipher实例，用于完成加密操作。
2. 调用[OH\_CryptoSymCipherParams\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_create)创建参数对象，调用[OH\_CryptoSymCipherParams\_SetParam](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_setparam)设置对应的加密参数。
3. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定对称密钥（OH\_CryptoSymKey）和GCM模式的加密参数（OH\_CryptoSymCipherParams），以初始化加密 Cipher 实例。
4. 将一次传入数据量设置为20字节，多次调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，更新数据（明文）。

   * 当前单次update没有长度限制，开发者可根据数据量判断如何调用update。
   * 建议开发者对每次update的结果都判断是否为null，并在结果不为null时取出其中的密文进行拼接，形成完整的密文。因为在不同的模式下，update的结果可能会受到不同影响。

     1）例如ECB和CBC模式，始终以分组为基本单位进行加密，并输出本次更新产生的加密分组结果。即当本次更新操作凑满一个分组时，输出密文；若未凑满，则本次更新输出null，将未加密的数据与下次输入的数据拼接后，再进行分组输出。最后进行doFinal操作时，将未加密的数据根据指定的填充模式进行填充，再输出剩余加密结果。解密过程中的update操作同理。

     2）对于流加密模式（比如CTR和OFB模式），通常密文长度和明文长度相等。
5. 调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，获取密文。

   * 由于已使用update传入数据，此处传入null。
   * final输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，以避免产生异常。

     注意

     在GCM模式下，final会返回authTag，作为解密操作时初始化的认证信息，需要保存。

     在GCM模式下，算法库当前只支持16字节的authTag，作为解密操作时初始化的认证信息。示例中authTag恰好为16字节。

**解密**

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定参数'AES128|GCM|PKCS7'，创建对称密钥类型为AES128、分组模式为GCM、填充模式为PKCS7的Cipher实例，完成解密操作。
2. 调用[OH\_CryptoSymCipherParams\_SetParam](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_setparam)设置authTag作为解密的认证信息。

   在GCM模式下，从加密后的数据中取出末尾16字节，作为解密时初始化的认证信息。示例中authTag恰好为16字节。
3. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（OH\_CryptoSymKey）和GCM模式对应的解密参数（OH\_CryptoSymCipherParams），初始化解密Cipher实例。
4. 将一次传入数据量设置为20字节，多次调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，更新数据（密文）。
5. 调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)获取解密数据。

**销毁对象**

调用[OH\_CryptoSymKeyGenerator\_Destroy](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_destroy)、[OH\_CryptoSymCipher\_Destroy](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_destroy)和[OH\_CryptoSymCipherParams\_Destroy](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_destroy)销毁各对象。

```
1. #include <cstring>
2. #include "CryptoArchitectureKit/crypto_common.h"
3. #include "CryptoArchitectureKit/crypto_sym_cipher.h"
4. #include "file.h"

6. #define OH_CRYPTO_GCM_TAG_LEN 16
7. #define OH_CRYPTO_MAX_TEST_DATA_LEN 128
8. OH_Crypto_ErrCode doTestAesGcmSeg()
9. {
10. OH_CryptoSymKeyGenerator *genCtx = nullptr;
11. OH_CryptoSymCipher *encCtx = nullptr;
12. OH_CryptoSymCipher *decCtx = nullptr;
13. OH_CryptoSymKey *keyCtx = nullptr;
14. OH_CryptoSymCipherParams *params = nullptr;

16. char *plainText = const_cast<char *>("aaaaa.....bbbbb.....ccccc.....ddddd.....eee");
17. Crypto_DataBlob msgBlob = {.data = (uint8_t *)(plainText), .len = strlen(plainText)};

19. uint8_t aad[8] = {1, 2, 3, 4, 5, 6, 7, 8};
20. uint8_t tagArr[16] = {0};
21. uint8_t iv[12] = {1, 2, 4, 12, 3, 4, 2, 3, 3, 2, 0, 4}; // iv使用安全随机数生成
22. Crypto_DataBlob tag = {.data = nullptr, .len = 0};
23. Crypto_DataBlob ivBlob = {.data = iv, .len = sizeof(iv)};
24. Crypto_DataBlob aadBlob = {.data = aad, .len = sizeof(aad)};
25. Crypto_DataBlob outUpdate = {.data = nullptr, .len = 0};
26. Crypto_DataBlob decUpdate = {.data = nullptr, .len = 0};
27. Crypto_DataBlob tagInit = {.data = tagArr, .len = sizeof(tagArr)};
28. int32_t cipherLen = 0;
29. int blockSize = 20;
30. int32_t randomLen = strlen(plainText);
31. int cnt = randomLen / blockSize;
32. int rem = randomLen % blockSize;
33. uint8_t cipherText[OH_CRYPTO_MAX_TEST_DATA_LEN] = {0};
34. Crypto_DataBlob cipherBlob;

36. // 生成密钥
37. OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create("AES128", &genCtx);
38. if (ret != CRYPTO_SUCCESS) {
39. goto end;
40. }
41. ret = OH_CryptoSymKeyGenerator_Generate(genCtx, &keyCtx);
42. if (ret != CRYPTO_SUCCESS) {
43. goto end;
44. }

46. // 设置参数
47. ret = OH_CryptoSymCipherParams_Create(&params);
48. if (ret != CRYPTO_SUCCESS) {
49. goto end;
50. }
51. ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_IV_DATABLOB, &ivBlob);
52. if (ret != CRYPTO_SUCCESS) {
53. goto end;
54. }
55. ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_AAD_DATABLOB, &aadBlob);
56. if (ret != CRYPTO_SUCCESS) {
57. goto end;
58. }
59. ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_TAG_DATABLOB, &tagInit);
60. if (ret != CRYPTO_SUCCESS) {
61. goto end;
62. }

64. // 加密
65. ret = OH_CryptoSymCipher_Create("AES128|GCM|PKCS7", &encCtx);
66. if (ret != CRYPTO_SUCCESS) {
67. goto end;
68. }
69. ret = OH_CryptoSymCipher_Init(encCtx, CRYPTO_ENCRYPT_MODE, keyCtx, params);
70. if (ret != CRYPTO_SUCCESS) {
71. goto end;
72. }

74. for (int i = 0; i < cnt; i++) {
75. msgBlob.len = blockSize;
76. ret = OH_CryptoSymCipher_Update(encCtx, &msgBlob, &outUpdate);
77. if (ret != CRYPTO_SUCCESS) {
78. goto end;
79. }
80. msgBlob.data += blockSize;
81. memcpy(&cipherText[cipherLen], outUpdate.data, outUpdate.len);
82. cipherLen += outUpdate.len;
83. OH_Crypto_FreeDataBlob(&outUpdate);
84. }
85. if (rem > 0) {
86. msgBlob.len = rem;
87. ret = OH_CryptoSymCipher_Update(encCtx, (Crypto_DataBlob *)&msgBlob, &outUpdate);
88. if (ret != CRYPTO_SUCCESS) {
89. goto end;
90. }
91. memcpy(&cipherText[cipherLen], outUpdate.data, outUpdate.len);
92. cipherLen += outUpdate.len;
93. OH_Crypto_FreeDataBlob(&outUpdate);
94. }
95. ret = OH_CryptoSymCipher_Final(encCtx, nullptr, &tag);
96. if (ret != CRYPTO_SUCCESS) {
97. goto end;
98. }

100. // 解密
101. cipherBlob = {.data = reinterpret_cast<uint8_t *>(cipherText), .len = (size_t)cipherLen};
102. msgBlob.data -= strlen(plainText) - rem;
103. msgBlob.len = strlen(plainText);
104. ret = OH_CryptoSymCipher_Create("AES128|GCM|PKCS7", &decCtx);
105. if (ret != CRYPTO_SUCCESS) {
106. goto end;
107. }
108. ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_TAG_DATABLOB, &tag);
109. if (ret != CRYPTO_SUCCESS) {
110. goto end;
111. }
112. ret = OH_CryptoSymCipher_Init(decCtx, CRYPTO_DECRYPT_MODE, keyCtx, params);
113. if (ret != CRYPTO_SUCCESS) {
114. goto end;
115. }
116. ret = OH_CryptoSymCipher_Final(decCtx, &cipherBlob, &decUpdate);
117. if (ret != CRYPTO_SUCCESS) {
118. goto end;
119. }

121. end:
122. OH_CryptoSymCipherParams_Destroy(params);
123. OH_CryptoSymCipher_Destroy(encCtx);
124. OH_CryptoSymCipher_Destroy(decCtx);
125. OH_CryptoSymKeyGenerator_Destroy(genCtx);
126. OH_CryptoSymKey_Destroy(keyCtx);
127. OH_Crypto_FreeDataBlob(&outUpdate);
128. OH_Crypto_FreeDataBlob(&tag);
129. OH_Crypto_FreeDataBlob(&decUpdate);
130. return ret;
131. }
```

[aes\_gcm\_segment\_encryption\_decryption.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceAes/entry/src/main/cpp/types/project/aes_gcm_segment_encryption_decryption.cpp#L16-L148)
