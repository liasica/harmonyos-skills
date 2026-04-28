---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-chacha20-encrypt-decrypt-poly1305-ndk
title: 使用ChaCha20对称密钥（Poly1305模式）加解密(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用ChaCha20对称密钥（Poly1305模式）加解密(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6259e165e7fa6a5114effdd9becb04bc9f397f69b7a5e039d8c289ff37f12b4f
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

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'ChaCha20|Poly1305'，创建对称密钥类型为ChaCha20、模式为Poly1305的Cipher实例，用于完成加密操作。
2. 调用[OH\_CryptoSymCipherParams\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_create)创建参数对象，调用[OH\_CryptoSymCipherParams\_SetParam](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_setparam)设置对应的加密参数。
3. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（OH\_CryptoSymKey）和Poly1305模式对应的加密参数（OH\_CryptoSymCipherParams），初始化加密Cipher实例。
4. 调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，更新数据（明文）。
5. 调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，获取加密后的数据。

   说明

   由于已使用update传入数据，此处data传入null。

   doFinal输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。
6. 使用[OH\_CryptoSymCipherParams\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_create)创建Params，使用[OH\_CryptoSymCipherParams\_SetParam](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_setparam)设置authTag，作为解密的认证信息。在Poly1305模式下，需要从加密后的数据中取出末尾16字节，作为解密时初始化的认证信息。
7. 调用[OH\_CryptoSymKeyGenerator\_Destroy](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_destroy)、[OH\_CryptoSymCipher\_Destroy](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_destroy)、[OH\_CryptoSymCipherParams\_Destroy](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_destroy)销毁各对象。

**解密**

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'ChaCha20|Poly1305'，创建对称密钥类型为ChaCha20、模式为Poly1305的Cipher实例，用于完成解密操作。
2. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（OH\_CryptoSymKey）和Poly1305模式对应的解密参数（OH\_CryptoSymCipherParams），初始化解密Cipher实例。
3. 调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，更新数据（密文）。
4. 调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，获取解密后的数据。

```
1. #include "CryptoArchitectureKit/crypto_common.h"
2. #include "CryptoArchitectureKit/crypto_sym_cipher.h"
3. #include <cstring>
4. #include "file.h"

6. // 参数赋值函数
7. static OH_Crypto_ErrCode doChaCha20Poly1305SetParams(Crypto_DataBlob *ivData, Crypto_DataBlob *aadData,
8. Crypto_DataBlob *tagData, OH_CryptoSymCipherParams **params)
9. {
10. OH_Crypto_ErrCode ret = OH_CryptoSymCipherParams_Create(params);
11. if (ret != CRYPTO_SUCCESS) {
12. return ret;
13. }
14. ret = OH_CryptoSymCipherParams_SetParam(*params, CRYPTO_IV_DATABLOB, ivData);
15. if (ret != CRYPTO_SUCCESS) {
16. goto end;
17. }
18. ret = OH_CryptoSymCipherParams_SetParam(*params, CRYPTO_AAD_DATABLOB, aadData);
19. if (ret != CRYPTO_SUCCESS) {
20. goto end;
21. }
22. ret = OH_CryptoSymCipherParams_SetParam(*params, CRYPTO_TAG_DATABLOB, tagData);
23. if (ret != CRYPTO_SUCCESS) {
24. goto end;
25. }
26. return ret;

28. end:
29. OH_CryptoSymCipherParams_Destroy(*params);
30. *params = nullptr;
31. return ret;
32. }

34. // 加密函数
35. static OH_Crypto_ErrCode doChaCha20Poly1305Encrypt(OH_CryptoSymKey *keyCtx, OH_CryptoSymCipherParams *params,
36. Crypto_DataBlob *msgBlob, Crypto_DataBlob *outUpdate, Crypto_DataBlob *tagOutPut)
37. {
38. OH_CryptoSymCipher *encCtx = nullptr;
39. OH_Crypto_ErrCode ret = OH_CryptoSymCipher_Create("ChaCha20|Poly1305", &encCtx);
40. if (ret != CRYPTO_SUCCESS) {
41. goto end;
42. }
43. ret = OH_CryptoSymCipher_Init(encCtx, CRYPTO_ENCRYPT_MODE, keyCtx, params);
44. if (ret != CRYPTO_SUCCESS) {
45. goto end;
46. }
47. ret = OH_CryptoSymCipher_Update(encCtx, msgBlob, outUpdate);
48. if (ret != CRYPTO_SUCCESS) {
49. goto end;
50. }
51. ret = OH_CryptoSymCipher_Final(encCtx, nullptr, tagOutPut);
52. if (ret != CRYPTO_SUCCESS) {
53. goto end;
54. }

56. end:
57. OH_CryptoSymCipher_Destroy(encCtx);
58. return ret;
59. }

61. // 解密函数
62. static OH_Crypto_ErrCode doChaCha20Poly1305Decrypt(OH_CryptoSymKey *keyCtx, OH_CryptoSymCipherParams *params,
63. Crypto_DataBlob *tagOutPut, Crypto_DataBlob *outUpdate, Crypto_DataBlob *decUpdate)
64. {
65. OH_CryptoSymCipher *decCtx = nullptr;
66. OH_Crypto_ErrCode ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_TAG_DATABLOB, tagOutPut);
67. if (ret != CRYPTO_SUCCESS) {
68. return ret;
69. }
70. ret = OH_CryptoSymCipher_Create("ChaCha20|Poly1305", &decCtx);
71. if (ret != CRYPTO_SUCCESS) {
72. goto end;
73. }
74. ret = OH_CryptoSymCipher_Init(decCtx, CRYPTO_DECRYPT_MODE, keyCtx, params);
75. if (ret != CRYPTO_SUCCESS) {
76. goto end;
77. }
78. ret = OH_CryptoSymCipher_Final(decCtx, outUpdate, decUpdate);
79. if (ret != CRYPTO_SUCCESS) {
80. goto end;
81. }

83. end:
84. OH_CryptoSymCipher_Destroy(decCtx);
85. return ret;
86. }

88. OH_Crypto_ErrCode doTestChaCha20Poly1305()
89. {
90. OH_CryptoSymKeyGenerator *genCtx = nullptr;
91. OH_CryptoSymKey *keyCtx = nullptr;
92. OH_CryptoSymCipherParams *params = nullptr;

94. Crypto_DataBlob outUpdate = {.data = nullptr, .len = 0};
95. Crypto_DataBlob decUpdate = {.data = nullptr, .len = 0};

97. uint8_t aad[8] = {1, 2, 3, 4, 5, 6, 7, 8};
98. uint8_t tag[16] = {0};
99. uint8_t iv[12] = {1, 2, 4, 12, 3, 4, 2, 3, 3, 2, 0, 4}; // iv使用安全随机数生成。
100. Crypto_DataBlob ivData = {.data = iv, .len = sizeof(iv)};
101. Crypto_DataBlob aadData = {.data = aad, .len = sizeof(aad)};
102. Crypto_DataBlob tagData = {.data = tag, .len = sizeof(tag)};
103. Crypto_DataBlob tagOutPut = {.data = nullptr, .len = 0};
104. char *plainText = const_cast<char *>("this is test!");
105. Crypto_DataBlob msgBlob = {.data = (uint8_t *)(plainText), .len = strlen(plainText)};
106. OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create("ChaCha20", &genCtx);
107. if (ret != CRYPTO_SUCCESS) {
108. goto end;
109. }
110. ret = OH_CryptoSymKeyGenerator_Generate(genCtx, &keyCtx);
111. if (ret != CRYPTO_SUCCESS) {
112. goto end;
113. }

115. // 参数赋值。
116. ret = doChaCha20Poly1305SetParams(&ivData, &aadData, &tagData, &params);
117. if (ret != CRYPTO_SUCCESS) {
118. goto end;
119. }

121. // 加密。
122. ret = doChaCha20Poly1305Encrypt(keyCtx, params, &msgBlob, &outUpdate, &tagOutPut);
123. if (ret != CRYPTO_SUCCESS) {
124. goto end;
125. }

127. // 解密。
128. ret = doChaCha20Poly1305Decrypt(keyCtx, params, &tagOutPut, &outUpdate, &decUpdate);
129. if (ret != CRYPTO_SUCCESS) {
130. goto end;
131. }

133. // 释放资源。
134. end:
135. OH_CryptoSymCipherParams_Destroy(params);
136. OH_CryptoSymKeyGenerator_Destroy(genCtx);
137. OH_CryptoSymKey_Destroy(keyCtx);
138. OH_Crypto_FreeDataBlob(&outUpdate);
139. OH_Crypto_FreeDataBlob(&decUpdate);
140. OH_Crypto_FreeDataBlob(&tagOutPut);
141. return ret;
142. }
```

[chacha20\_poly1305\_encryption\_decryption.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceChaCha20/entry/src/main/cpp/types/project/chacha20_poly1305_encryption_decryption.cpp#L16-L159)
