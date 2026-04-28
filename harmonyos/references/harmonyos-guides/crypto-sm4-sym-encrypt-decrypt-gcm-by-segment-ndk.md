---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-gcm-by-segment-ndk
title: 使用SM4对称密钥（GCM模式）分段加解密(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用SM4对称密钥（GCM模式）分段加解密(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:27+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:95a414e8815034329ad92055e3bef3ff1be1f8fd6946e0a64c39efd07a355722
---

对应的算法规格请查看[对称密钥加解密算法规格：SM4](crypto-sym-encrypt-decrypt-spec.md#sm4)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libohcrypto.so)
```

**加密**

1. 调用[OH\_CryptoSymKeyGenerator\_Create](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_create)、[OH\_CryptoSymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_generate)，生成密钥算法为SM4、密钥长度为128位的对称密钥（OH\_CryptoSymKey）。

   如何生成SM4对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：SM4](crypto-sym-key-generation-conversion-spec.md#sm4)和[随机生成对称密钥](crypto-generate-sym-key-randomly-ndk.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'SM4\_128|GCM|PKCS7'，创建对称密钥类型为SM4\_128、分组模式为GCM、填充模式为PKCS7的Cipher实例，用于完成加密操作。
3. 调用[OH\_CryptoSymCipherParams\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_create)创建参数对象，调用[OH\_CryptoSymCipherParams\_SetParam](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_setparam)设置对应的加密参数。
4. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（OH\_CryptoSymKey）和GCM模式对应的加密参数（OH\_CryptoSymCipherParams），初始化加密Cipher实例。
5. 将一次传入数据量设置为20字节，多次调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，更新数据（明文）。

   * 当前单次update长度没有限制，开发者可以根据数据量判断如何调用update。
   * 建议开发者对每次update的结果都判断是否为null，并在结果不为null时取出其中的数据进行拼接，形成完整的密文。因为在不同的模式下，update的结果可能会受到不同影响。

     1）比如ECB和CBC模式，始终以分组作为基本单位来加密，并输出本次update产生的加密分组结果。即当本次update操作凑满一个分组就输出密文，没有凑满则此次update输出null，将未加密的数据与下次输入的数据拼接凑分组再输出。等到最后doFinal的时候，将未加密的数据，根据指定的填充模式进行填充，再输出剩余加密结果。解密过程中的update同理。

     2）对于流加密模式（比如CTR和OFB模式），通常密文长度和明文长度相等。
6. 调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，获取加密后的数据。

   * 由于已使用update传入数据，此处data传入null。
   * doFinal输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。
7. 使用[OH\_CryptoSymCipherParams\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_create)创建Params，使用[OH\_CryptoSymCipherParams\_SetParam](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_setparam)设置authTag，作为解密的认证信息。

   在GCM模式下，需要从加密后的数据中取出末尾16字节，作为解密时初始化的认证信息。示例中authTag恰好为16字节。
8. 调用[OH\_CryptoSymKeyGenerator\_Destroy](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_destroy)、[OH\_CryptoSymCipher\_Destroy](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_destroy)、[OH\_CryptoSymCipherParams\_Destroy](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_destroy)销毁各对象。

**解密**

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'SM4\_128|GCM|PKCS7'，创建对称密钥类型为SM4\_128、分组模式为GCM、填充模式为PKCS7的Cipher实例，用于完成解密操作。
2. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（OH\_CryptoSymKey）和GCM模式对应的解密参数（OH\_CryptoSymCipherParams），初始化解密Cipher实例。
3. 将一次传入数据量设置为20字节，多次调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，更新数据（密文）。
4. 调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，获取解密后的数据。

```
1. #include <cstring>
2. #include "CryptoArchitectureKit/crypto_common.h"
3. #include "CryptoArchitectureKit/crypto_sym_cipher.h"

5. #define OH_CRYPTO_GCM_TAG_LEN 16
6. #define OH_CRYPTO_MAX_TEST_DATA_LEN 128

8. OH_Crypto_ErrCode doTestSm4GcmSeg()
9. {
10. OH_CryptoSymKeyGenerator *genCtx = nullptr;
11. OH_CryptoSymCipher *encCtx = nullptr;
12. OH_CryptoSymCipher *decCtx = nullptr;
13. OH_CryptoSymKey *keyCtx = nullptr;
14. OH_CryptoSymCipherParams *params = nullptr;

16. char *plainText = const_cast<char *>("aaaaa.....bbbbb.....ccccc.....ddddd.....eee");
17. Crypto_DataBlob msgBlob = {.data = (uint8_t *)(plainText), .len = strlen(plainText)};
18. uint8_t aad[8] = {1, 2, 3, 4, 5, 6, 7, 8};
19. uint8_t tagArr[16] = {0};
20. uint8_t iv[12] = {1, 2, 4, 12, 3, 4, 2, 3, 3, 2, 0, 4}; // iv使用安全随机数生成
21. Crypto_DataBlob tag = {.data = nullptr, .len = 0};
22. Crypto_DataBlob ivBlob = {.data = iv, .len = sizeof(iv)};
23. Crypto_DataBlob aadBlob = {.data = aad, .len = sizeof(aad)};
24. Crypto_DataBlob outUpdate = {.data = nullptr, .len = 0};
25. Crypto_DataBlob decUpdate = {.data = nullptr, .len = 0};
26. Crypto_DataBlob tagInit = {.data = tagArr, .len = sizeof(tagArr)};
27. int32_t cipherLen = 0;
28. int blockSize = 20;
29. int32_t randomLen = strlen(plainText);
30. int cnt = randomLen / blockSize;
31. int rem = randomLen % blockSize;
32. uint8_t cipherText[OH_CRYPTO_MAX_TEST_DATA_LEN] = {0};
33. Crypto_DataBlob cipherBlob;

35. // 生成密钥
36. OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create("SM4_128", &genCtx);
37. if (ret != CRYPTO_SUCCESS) {
38. goto end;
39. }
40. ret = OH_CryptoSymKeyGenerator_Generate(genCtx, &keyCtx);
41. if (ret != CRYPTO_SUCCESS) {
42. goto end;
43. }

45. // 设置参数
46. ret = OH_CryptoSymCipherParams_Create(&params);
47. if (ret != CRYPTO_SUCCESS) {
48. goto end;
49. }
50. ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_IV_DATABLOB, &ivBlob);
51. if (ret != CRYPTO_SUCCESS) {
52. goto end;
53. }
54. ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_AAD_DATABLOB, &aadBlob);
55. if (ret != CRYPTO_SUCCESS) {
56. goto end;
57. }
58. ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_TAG_DATABLOB, &tagInit);
59. if (ret != CRYPTO_SUCCESS) {
60. goto end;
61. }

63. // 加密
64. ret = OH_CryptoSymCipher_Create("SM4_128|GCM|PKCS7", &encCtx);
65. if (ret != CRYPTO_SUCCESS) {
66. goto end;
67. }
68. ret = OH_CryptoSymCipher_Init(encCtx, CRYPTO_ENCRYPT_MODE, keyCtx, params);
69. if (ret != CRYPTO_SUCCESS) {
70. goto end;
71. }

73. for (int i = 0; i < cnt; i++) {
74. msgBlob.len = blockSize;
75. ret = OH_CryptoSymCipher_Update(encCtx, &msgBlob, &outUpdate);
76. if (ret != CRYPTO_SUCCESS) {
77. goto end;
78. }
79. msgBlob.data += blockSize;
80. memcpy(&cipherText[cipherLen], outUpdate.data, outUpdate.len);
81. cipherLen += outUpdate.len;
82. OH_Crypto_FreeDataBlob(&outUpdate);
83. }
84. if (rem > 0) {
85. msgBlob.len = rem;
86. ret = OH_CryptoSymCipher_Update(encCtx, (Crypto_DataBlob *)&msgBlob, &outUpdate);
87. if (ret != CRYPTO_SUCCESS) {
88. goto end;
89. }
90. memcpy(&cipherText[cipherLen], outUpdate.data, outUpdate.len);
91. cipherLen += outUpdate.len;
92. OH_Crypto_FreeDataBlob(&outUpdate);
93. }
94. ret = OH_CryptoSymCipher_Final(encCtx, nullptr, &tag);
95. if (ret != CRYPTO_SUCCESS) {
96. goto end;
97. }

99. // 解密
100. cipherBlob = {.data = reinterpret_cast<uint8_t *>(cipherText), .len = (size_t)cipherLen};
101. msgBlob.data -= strlen(plainText) - rem;
102. msgBlob.len = strlen(plainText);
103. ret = OH_CryptoSymCipher_Create("SM4_128|GCM|PKCS7", &decCtx);
104. if (ret != CRYPTO_SUCCESS) {
105. goto end;
106. }
107. ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_TAG_DATABLOB, &tag);
108. if (ret != CRYPTO_SUCCESS) {
109. goto end;
110. }
111. ret = OH_CryptoSymCipher_Init(decCtx, CRYPTO_DECRYPT_MODE, keyCtx, params);
112. if (ret != CRYPTO_SUCCESS) {
113. goto end;
114. }
115. ret = OH_CryptoSymCipher_Final(decCtx, &cipherBlob, &decUpdate);
116. if (ret != CRYPTO_SUCCESS) {
117. goto end;
118. }
119. end:
120. OH_CryptoSymCipherParams_Destroy(params);
121. OH_CryptoSymCipher_Destroy(encCtx);
122. OH_CryptoSymCipher_Destroy(decCtx);
123. OH_CryptoSymKeyGenerator_Destroy(genCtx);
124. OH_CryptoSymKey_Destroy(keyCtx);
125. OH_Crypto_FreeDataBlob(&outUpdate);
126. OH_Crypto_FreeDataBlob(&tag);
127. OH_Crypto_FreeDataBlob(&decUpdate);
128. return ret;
129. }
```

[sm4\_gcm\_seg\_encryption\_decryption.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceSM4/entry/src/main/cpp/types/project/sm4_gcm_seg_encryption_decryption.cpp#L16-L146)
