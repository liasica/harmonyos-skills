---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-pkcs1-ndk
title: 使用RSA非对称密钥（PKCS1模式）加解密(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用RSA非对称密钥（PKCS1模式）加解密(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6f13a2c99b7b248a3fefc8dd4ee226ad268bbcc8d2aea63853b027d750c5f8f2
---

对应的算法规格请查看[非对称密钥加解密算法规格：RSA](crypto-asym-encrypt-decrypt-spec.md#rsa)。

**加密**

1. 调用[OH\_CryptoAsymKeyGenerator\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_create)、[OH\_CryptoAsymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_generate)，生成RSA密钥类型为RSA1024、素数个数为2的非对称密钥对（keyPair）。keyPair对象中包括公钥PubKey、私钥PriKey。

   如何生成RSA非对称密钥对，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：RSA](crypto-asym-key-generation-conversion-spec.md#rsa)和[随机生成非对称密钥对](crypto-generate-asym-key-pair-randomly.md)理解。参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[OH\_CryptoAsymCipher\_Create](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_create)，指定字符串参数'RSA1024|PKCS1'，创建非对称密钥类型为RSA1024、填充模式为PKCS1的Cipher实例，用于完成加解密操作。
3. 调用[OH\_CryptoAsymCipher\_Init](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（keyPair），初始化加密Cipher实例。
4. 调用[OH\_CryptoAsymCipher\_Final](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_final)，传入明文，获取加密后的数据。

   * OH\_CryptoAsymCipher\_Final输出结果可能为NULL，在访问具体数据前，需要先判断结果是否为NULL，避免产生异常。
   * 当数据量较大时，可以多次调用OH\_CryptoAsymCipher\_Final，即[分段加解密](crypto-rsa-asym-encrypt-decrypt-by-segment-ndk.md)。

**解密**

1. 由于RSA算法的Cipher实例不支持重复init操作，需要调用[OH\_CryptoAsymCipher\_Create](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_create)，重新生成Cipher实例。
2. 调用[OH\_CryptoAsymCipher\_Init](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（keyPair）初始化解密Cipher实例。
3. 调用[OH\_CryptoAsymCipher\_Final](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_final)，传入密文，获取解密后的数据。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"
2. #include <cstring>

4. static OH_Crypto_ErrCode doRsaEncrypt(const Crypto_DataBlob *plainData, OH_CryptoKeyPair **keyPair,
5. OH_CryptoAsymKeyGenerator **keyGen, Crypto_DataBlob *encryptedData)
6. {
7. OH_Crypto_ErrCode ret = OH_CryptoAsymKeyGenerator_Create("RSA1024", keyGen);
8. if (ret != CRYPTO_SUCCESS) {
9. return ret;
10. }

12. ret = OH_CryptoAsymKeyGenerator_Generate(*keyGen, keyPair);
13. if (ret != CRYPTO_SUCCESS) {
14. OH_CryptoAsymKeyGenerator_Destroy(*keyGen);
15. return ret;
16. }

18. OH_CryptoAsymCipher *cipher = nullptr;
19. ret = OH_CryptoAsymCipher_Create("RSA1024|PKCS1", &cipher);
20. if (ret != CRYPTO_SUCCESS) {
21. OH_CryptoKeyPair_Destroy(*keyPair);
22. OH_CryptoAsymKeyGenerator_Destroy(*keyGen);
23. return ret;
24. }

26. ret = OH_CryptoAsymCipher_Init(cipher, CRYPTO_ENCRYPT_MODE, *keyPair);
27. if (ret != CRYPTO_SUCCESS) {
28. OH_CryptoAsymCipher_Destroy(cipher);
29. OH_CryptoKeyPair_Destroy(*keyPair);
30. OH_CryptoAsymKeyGenerator_Destroy(*keyGen);
31. return ret;
32. }

34. ret = OH_CryptoAsymCipher_Final(cipher, plainData, encryptedData);
35. OH_CryptoAsymCipher_Destroy(cipher);
36. if (ret != CRYPTO_SUCCESS) {
37. OH_CryptoKeyPair_Destroy(*keyPair);
38. OH_CryptoAsymKeyGenerator_Destroy(*keyGen);
39. return ret;
40. }

42. return ret;
43. }

45. static OH_Crypto_ErrCode doRsaDecrypt(const Crypto_DataBlob *encryptedData, OH_CryptoKeyPair *keyPair,
46. const Crypto_DataBlob *expectedPlainData)
47. {
48. OH_CryptoAsymCipher *cipher = nullptr;
49. OH_Crypto_ErrCode ret = OH_CryptoAsymCipher_Create("RSA1024|PKCS1", &cipher);
50. if (ret != CRYPTO_SUCCESS) {
51. return ret;
52. }

54. ret = OH_CryptoAsymCipher_Init(cipher, CRYPTO_DECRYPT_MODE, keyPair);
55. if (ret != CRYPTO_SUCCESS) {
56. OH_CryptoAsymCipher_Destroy(cipher);
57. return ret;
58. }

60. Crypto_DataBlob decrypted = { 0 };
61. ret = OH_CryptoAsymCipher_Final(cipher, encryptedData, &decrypted);
62. OH_CryptoAsymCipher_Destroy(cipher);
63. if (ret != CRYPTO_SUCCESS) {
64. return ret;
65. }

67. if ((decrypted.len != expectedPlainData->len) ||
68. (memcmp(decrypted.data, expectedPlainData->data, decrypted.len) != 0)) {
69. OH_Crypto_FreeDataBlob(&decrypted);
70. return CRYPTO_OPERTION_ERROR;
71. }

73. OH_Crypto_FreeDataBlob(&decrypted);
74. return ret;
75. }

77. OH_Crypto_ErrCode doTestRsaEncDec()
78. {
79. const char *testData = "Hello, RSA!";
80. Crypto_DataBlob plainData = {
81. .data = (uint8_t *)testData,
82. .len = strlen(testData)
83. };

85. OH_CryptoKeyPair *keyPair = nullptr;
86. OH_CryptoAsymKeyGenerator *keyGen = nullptr;
87. Crypto_DataBlob encryptedData = { 0 };

89. OH_Crypto_ErrCode ret = doRsaEncrypt(&plainData, &keyPair, &keyGen, &encryptedData);
90. if (ret != CRYPTO_SUCCESS) {
91. return ret;
92. }

94. ret = doRsaDecrypt(&encryptedData, keyPair, &plainData);
95. OH_Crypto_FreeDataBlob(&encryptedData);
96. OH_CryptoKeyPair_Destroy(keyPair);
97. OH_CryptoAsymKeyGenerator_Destroy(keyGen);
98. return ret;
99. }
```

[PKCS1\_RSA.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceCpp/entry/src/main/cpp/types/project/rsa/PKCS1_RSA.cpp#L16-L118)
