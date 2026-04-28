---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-cbc-ndk
title: 使用AES对称密钥（CBC模式）加解密(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用AES对称密钥（CBC模式）加解密(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:140921f71f6db19289b6575d1b4547dcb860509218c7ef9be4927e4392934b31
---

请查看[对称密钥加解密算法规格：AES](crypto-sym-encrypt-decrypt-spec.md#aes)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libohcrypto.so)
```

## 开发步骤

**创建对象**

调用[OH\_CryptoSymKeyGenerator\_Create](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_create)和[OH\_CryptoSymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_generate)，生成密钥算法为AES、密钥长度为128位的对称密钥（OH\_CryptoSymKey）。

如何生成AES对称密钥，请参考以下示例，并结合[对称密钥生成和转换规格：AES](crypto-sym-key-generation-conversion-spec.md#aes)和[随机生成对称密钥](crypto-generate-sym-key-randomly-ndk.md)理解，参考文档与当前示例可能存在入参差异，请注意区分。

**加密**

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'AES128|CBC|PKCS7'，创建对称密钥类型为AES128、分组模式为CBC、填充模式为PKCS7的Cipher实例，用于加密操作。
2. 调用[OH\_CryptoSymCipherParams\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_create)创建参数对象，并调用[OH\_CryptoSymCipherParams\_SetParam](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_setparam)设置加密参数。
3. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（OH\_CryptoSymKey）和CBC模式对应的加密参数（OH\_CryptoSymCipherParams），初始化加密Cipher实例。
4. 加密内容较短时，可以直接调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，无需调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，获取加密后的数据。

**解密**

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'AES128|CBC|PKCS7'，创建对称密钥类型为AES128、分组模式为CBC、填充模式为PKCS7的Cipher实例，用于解密操作。
2. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（OH\_CryptoSymKey）和CBC模式对应的解密参数（OH\_CryptoSymCipherParams），初始化解密Cipher实例。
3. 解密内容较短时，可直接调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，无需调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，获取解密后的数据。

**销毁对象**

调用[OH\_CryptoSymKeyGenerator\_Destroy](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_destroy)、[OH\_CryptoSymCipher\_Destroy](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_destroy)、[OH\_CryptoSymKey\_Destroy](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkey_destroy)、[OH\_Crypto\_FreeDataBlob](../harmonyos-references/capi-crypto-common-h.md#oh_crypto_freedatablob)释放申请的内存，销毁对象。

```
1. #include "CryptoArchitectureKit/crypto_common.h"
2. #include "CryptoArchitectureKit/crypto_sym_cipher.h"
3. #include <cstring>
4. #include "file.h"

6. OH_Crypto_ErrCode doTestAesCbc()
7. {
8. OH_CryptoSymKeyGenerator *genCtx = nullptr;
9. OH_CryptoSymCipher *encCtx = nullptr;
10. OH_CryptoSymCipher *decCtx = nullptr;
11. OH_CryptoSymKey *keyCtx = nullptr;
12. OH_CryptoSymCipherParams *params = nullptr;
13. Crypto_DataBlob outUpdate = {.data = nullptr, .len = 0};
14. Crypto_DataBlob decUpdate = {.data = nullptr, .len = 0};
15. char *plainText = const_cast<char *>("this is test!");
16. Crypto_DataBlob msgBlob = {.data = (uint8_t *)(plainText), .len = strlen(plainText)};
17. uint8_t iv[16] = {1, 2, 4, 12, 3, 4, 2, 3, 3, 2, 0, 4, 3, 1, 0, 10}; // iv使用安全随机数生成
18. Crypto_DataBlob ivBlob = {.data = iv, .len = sizeof(iv)};
19. // 生成对称密钥
20. OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create("AES128", &genCtx);
21. if (ret != CRYPTO_SUCCESS) {
22. goto end;
23. }
24. ret = OH_CryptoSymKeyGenerator_Generate(genCtx, &keyCtx);
25. if (ret != CRYPTO_SUCCESS) {
26. goto end;
27. }

29. // 设置参数
30. ret = OH_CryptoSymCipherParams_Create(&params);
31. if (ret != CRYPTO_SUCCESS) {
32. goto end;
33. }
34. ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_IV_DATABLOB, &ivBlob);
35. if (ret != CRYPTO_SUCCESS) {
36. goto end;
37. }

39. // 加密
40. ret = OH_CryptoSymCipher_Create("AES128|CBC|PKCS7", &encCtx);
41. if (ret != CRYPTO_SUCCESS) {
42. goto end;
43. }
44. ret = OH_CryptoSymCipher_Init(encCtx, CRYPTO_ENCRYPT_MODE, keyCtx, params);
45. if (ret != CRYPTO_SUCCESS) {
46. goto end;
47. }
48. ret = OH_CryptoSymCipher_Final(encCtx, &msgBlob, &outUpdate);
49. if (ret != CRYPTO_SUCCESS) {
50. goto end;
51. }

53. // 解密
54. ret = OH_CryptoSymCipher_Create("AES128|CBC|PKCS7", &decCtx);
55. if (ret != CRYPTO_SUCCESS) {
56. goto end;
57. }
58. ret = OH_CryptoSymCipher_Init(decCtx, CRYPTO_DECRYPT_MODE, keyCtx, params);
59. if (ret != CRYPTO_SUCCESS) {
60. goto end;
61. }
62. ret = OH_CryptoSymCipher_Final(decCtx, &outUpdate, &decUpdate);
63. if (ret != CRYPTO_SUCCESS) {
64. goto end;
65. }

67. end:
68. OH_CryptoSymCipherParams_Destroy(params);
69. OH_CryptoSymCipher_Destroy(encCtx);
70. OH_CryptoSymCipher_Destroy(decCtx);
71. OH_CryptoSymKeyGenerator_Destroy(genCtx);
72. OH_CryptoSymKey_Destroy(keyCtx);
73. OH_Crypto_FreeDataBlob(&outUpdate);
74. OH_Crypto_FreeDataBlob(&decUpdate);
75. return ret;
76. }
```

[aes\_cbc\_encryption\_decryption.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceAes/entry/src/main/cpp/types/project/aes_cbc_encryption_decryption.cpp#L16-L93)
