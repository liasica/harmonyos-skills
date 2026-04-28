---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-ccm-ndk
title: 使用AES对称密钥（CCM模式）加解密(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用AES对称密钥（CCM模式）加解密(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:817878f396f7bb22d9e4690b48328f637cb37d3e00bbb6204ecb09532bb9dd4d
---

请查看[对称密钥加解密算法规格：AES](crypto-sym-encrypt-decrypt-spec.md#aes)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libohcrypto.so)
```

## 开发步骤

**创建对象**

调用[OH\_CryptoSymKeyGenerator\_Create](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_create)、[OH\_CryptoSymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_generate)，生成密钥算法为AES、密钥长度为128位的对称密钥（OH\_CryptoSymKey）。

如何生成AES对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：AES](crypto-sym-key-generation-conversion-spec.md#aes)和[随机生成对称密钥](crypto-generate-sym-key-randomly-ndk.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。

**加密**

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'AES128|CCM'，创建对称密钥类型为AES128、分组模式为CCM的Cipher实例，用于完成加密操作。
2. 调用[OH\_CryptoSymCipherParams\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_create)创建参数对象，调用[OH\_CryptoSymCipherParams\_SetParam](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_setparam)设置对应的加密参数。
3. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（OH\_CryptoSymKey）和CCM模式对应的加密参数（OH\_CryptoSymCipherParams），初始化加密Cipher实例。
4. 调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，更新数据（明文）。

   当前单次update没有长度限制，根据明文长度判断单次调用update输入的数据长度。

   说明

   CCM模式不支持分段加解密。
5. 调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，获取加密后的数据。

   * 已使用update传入数据，此处data传入null。
   * final输出结果可能为null，访问数据前需先判断结果是否为null。

     注意

     在CCM模式下，final设置authTag作为解密时的初始化认证信息，需要保存。
6. 使用[OH\_CryptoSymCipherParams\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_create)创建Params，使用[OH\_CryptoSymCipherParams\_SetParam](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_setparam)设置authTag，作为解密的认证信息。

   在CCM模式下，算法库支持12字节的authTag，用于解密时的初始化认证。示例中authTag为12字节。

**解密**

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定参数 'AES128|CCM'，创建对称密钥类型为AES128、分组模式为CCM的Cipher实例，用于解密操作。
2. 解密时需使用[OH\_CryptoSymCipherParams\_SetParam](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_setparam)设置authTag，作为初始化的认证信息。
3. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为解密，指定解密密钥和CCM模式的解密参数，初始化解密Cipher实例。
4. 调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，更新数据（密文）。

   当前单次update长度没有限制，开发者可以根据密文长度判断单次调用update输入的数据长度。

   说明

   CCM模式不支持分段加解密。
5. 调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，获取解密后的数据。

   * 已使用update传入数据，此处data传入null。
   * 在访问final输出结果的具体数据前，需要先判断结果是否为null，以避免异常。

**销毁对象**

调用[OH\_CryptoSymKeyGenerator\_Destroy](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_destroy)、[OH\_CryptoSymCipher\_Destroy](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_destroy)、[OH\_CryptoSymKey\_Destroy](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkey_destroy)、[OH\_Crypto\_FreeDataBlob](../harmonyos-references/capi-crypto-common-h.md#oh_crypto_freedatablob)释放申请的内存，销毁对称密钥、Cipher实例和Params。

* AES CCM模式加解密示例如下：

```
1. #include "CryptoArchitectureKit/crypto_common.h"
2. #include "CryptoArchitectureKit/crypto_sym_cipher.h"
3. #include <cstring>
4. #include "file.h"

6. OH_Crypto_ErrCode doTestAesCcm()
7. {
8. OH_CryptoSymKeyGenerator *genCtx = nullptr;
9. OH_CryptoSymCipher *encCtx = nullptr;
10. OH_CryptoSymCipher *decCtx = nullptr;
11. OH_CryptoSymKey *keyCtx = nullptr;
12. OH_CryptoSymCipherParams *params = nullptr;

14. Crypto_DataBlob outUpdate = {.data = nullptr, .len = 0};
15. Crypto_DataBlob decUpdate = {.data = nullptr, .len = 0};

17. uint8_t aad[8] = {1, 2, 3, 4, 5, 6, 7, 8};
18. uint8_t tag[12] = {0};
19. uint8_t iv[7] = {1, 2, 4, 12, 3, 4, 2}; // iv使用安全随机数生成
20. Crypto_DataBlob ivData = {.data = iv, .len = sizeof(iv)};
21. Crypto_DataBlob aadData = {.data = aad, .len = sizeof(aad)};
22. Crypto_DataBlob tagData = {.data = tag, .len = sizeof(tag)};
23. Crypto_DataBlob tagOutPut = {.data = nullptr, .len = 0};
24. char *plainText = const_cast<char *>("this is test!");
25. Crypto_DataBlob msgBlob = {.data = (uint8_t *)(plainText), .len = strlen(plainText)};
26. // 生成对称密钥
27. OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create("AES128", &genCtx);
28. if (ret != CRYPTO_SUCCESS) {
29. goto end;
30. }
31. ret = OH_CryptoSymKeyGenerator_Generate(genCtx, &keyCtx);
32. if (ret != CRYPTO_SUCCESS) {
33. goto end;
34. }

36. // 设置参数
37. ret = OH_CryptoSymCipherParams_Create(&params);
38. if (ret != CRYPTO_SUCCESS) {
39. goto end;
40. }
41. ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_IV_DATABLOB, &ivData);
42. if (ret != CRYPTO_SUCCESS) {
43. goto end;
44. }
45. ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_AAD_DATABLOB, &aadData);
46. if (ret != CRYPTO_SUCCESS) {
47. goto end;
48. }
49. ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_TAG_DATABLOB, &tagData);
50. if (ret != CRYPTO_SUCCESS) {
51. goto end;
52. }

54. // 加密
55. ret = OH_CryptoSymCipher_Create("AES128|CCM", &encCtx);
56. if (ret != CRYPTO_SUCCESS) {
57. goto end;
58. }
59. ret = OH_CryptoSymCipher_Init(encCtx, CRYPTO_ENCRYPT_MODE, keyCtx, params);
60. if (ret != CRYPTO_SUCCESS) {
61. goto end;
62. }
63. ret = OH_CryptoSymCipher_Update(encCtx, &msgBlob, &outUpdate);
64. if (ret != CRYPTO_SUCCESS) {
65. goto end;
66. }
67. ret = OH_CryptoSymCipher_Final(encCtx, nullptr, &tagOutPut);
68. if (ret != CRYPTO_SUCCESS) {
69. goto end;
70. }

72. // 解密
73. ret = OH_CryptoSymCipher_Create("AES128|CCM", &decCtx);
74. if (ret != CRYPTO_SUCCESS) {
75. goto end;
76. }
77. ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_TAG_DATABLOB, &tagOutPut);
78. if (ret != CRYPTO_SUCCESS) {
79. goto end;
80. }
81. ret = OH_CryptoSymCipher_Init(decCtx, CRYPTO_DECRYPT_MODE, keyCtx, params);
82. if (ret != CRYPTO_SUCCESS) {
83. goto end;
84. }
85. ret = OH_CryptoSymCipher_Final(decCtx, &outUpdate, &decUpdate);
86. if (ret != CRYPTO_SUCCESS) {
87. goto end;
88. }

90. end:
91. OH_CryptoSymCipherParams_Destroy(params);
92. OH_CryptoSymCipher_Destroy(encCtx);
93. OH_CryptoSymCipher_Destroy(decCtx);
94. OH_CryptoSymKeyGenerator_Destroy(genCtx);
95. OH_CryptoSymKey_Destroy(keyCtx);
96. OH_Crypto_FreeDataBlob(&outUpdate);
97. OH_Crypto_FreeDataBlob(&decUpdate);
98. OH_Crypto_FreeDataBlob(&tagOutPut);
99. return ret;
100. }
```

[aes\_ccm\_encryption\_decryption.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceAes/entry/src/main/cpp/types/project/aes_ccm_encryption_decryption.cpp#L16-L117)
