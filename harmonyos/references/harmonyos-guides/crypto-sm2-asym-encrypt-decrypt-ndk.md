---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-asym-encrypt-decrypt-ndk
title: 使用SM2非对称密钥加解密(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用SM2非对称密钥加解密(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:09fe3b2ec5b8abb4d9db9470b5d06fcf0a5cd8daff1b386d2db09b17c3821575
---

对应的算法规格请查看[非对称密钥加解密算法规格：SM2](crypto-asym-encrypt-decrypt-spec.md#sm2)。

**加密**

1. 调用[OH\_CryptoAsymKeyGenerator\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_create)、[OH\_CryptoAsymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_generate)，生成SM2密钥类型为SM2\_256的非对称密钥对（keyPair）。keyPair对象中包括公钥PubKey、私钥PriKey。

   如何生成SM2非对称密钥对，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：SM2](crypto-asym-key-generation-conversion-spec.md#sm2)和[随机生成非对称密钥对](crypto-generate-asym-key-pair-randomly-ndk.md)理解。参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[OH\_CryptoAsymCipher\_Create](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_create)，指定字符串参数'SM2\_256|SM3'，创建非对称密钥类型为SM2\_256、摘要算法为SM3的Cipher实例，用于完成加解密操作。
3. 调用[OH\_CryptoAsymCipher\_Init](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（keyPair），初始化加密Cipher实例。
4. 调用[OH\_CryptoAsymCipher\_Final](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_final)，传入明文，获取加密后的数据。

   OH\_CryptoAsymCipher\_Final输出结果可能为NULL，在访问具体数据前，需要先判断结果是否为NULL，避免产生异常。

**解密**

1. 由于SM2算法的Cipher实例不支持重复init操作，需要调用[OH\_CryptoAsymCipher\_Create](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_create)，重新生成Cipher实例。
2. 调用[OH\_CryptoAsymCipher\_Init](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（keyPair）初始化解密Cipher实例。
3. 调用[OH\_CryptoAsymCipher\_Final](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_final)，传入密文，获取解密后的数据。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"
2. #include <algorithm>
3. #include <vector>
4. #include <string>

6. static std::vector<uint8_t> doTestSm2Enc(OH_CryptoKeyPair *keyPair, std::vector<uint8_t> &plainText)
7. {
8. std::vector<uint8_t> cipherText;
9. OH_CryptoAsymCipher *cipher = nullptr;
10. OH_Crypto_ErrCode ret = OH_CryptoAsymCipher_Create("SM2_256|SM3", &cipher);
11. if (ret != CRYPTO_SUCCESS) {
12. return std::vector<uint8_t>{};
13. }

15. ret = OH_CryptoAsymCipher_Init(cipher, CRYPTO_ENCRYPT_MODE, keyPair);
16. if (ret != CRYPTO_SUCCESS) {
17. OH_CryptoAsymCipher_Destroy(cipher);
18. return std::vector<uint8_t>{};
19. }

21. Crypto_DataBlob in = {};
22. in.data = plainText.data();
23. in.len = plainText.size();
24. Crypto_DataBlob out = {};
25. ret = OH_CryptoAsymCipher_Final(cipher, &in, &out);
26. if (ret != CRYPTO_SUCCESS) {
27. OH_CryptoAsymCipher_Destroy(cipher);
28. return std::vector<uint8_t>{};
29. }
30. cipherText.insert(cipherText.end(), out.data, out.data + out.len);
31. OH_Crypto_FreeDataBlob(&out);

33. OH_CryptoAsymCipher_Destroy(cipher);
34. return cipherText;
35. }

37. static std::vector<uint8_t> doTestSm2Dec(OH_CryptoKeyPair *keyPair, std::vector<uint8_t> &encryptText)
38. {
39. std::vector<uint8_t> decryptText;
40. OH_CryptoAsymCipher *cipher = nullptr;
41. OH_Crypto_ErrCode ret = OH_CryptoAsymCipher_Create("SM2_256|SM3", &cipher);
42. if (ret != CRYPTO_SUCCESS) {
43. return std::vector<uint8_t>{};
44. }

46. ret = OH_CryptoAsymCipher_Init(cipher, CRYPTO_DECRYPT_MODE, keyPair);
47. if (ret != CRYPTO_SUCCESS) {
48. OH_CryptoAsymCipher_Destroy(cipher);
49. return std::vector<uint8_t>{};
50. }

52. Crypto_DataBlob in = {};
53. in.data = encryptText.data();
54. in.len = encryptText.size();
55. Crypto_DataBlob out = {};
56. ret = OH_CryptoAsymCipher_Final(cipher, &in, &out);
57. if (ret != CRYPTO_SUCCESS) {
58. OH_CryptoAsymCipher_Destroy(cipher);
59. return std::vector<uint8_t>{};
60. }
61. decryptText.insert(decryptText.end(), out.data, out.data + out.len);
62. OH_Crypto_FreeDataBlob(&out);

64. OH_CryptoAsymCipher_Destroy(cipher);
65. return decryptText;
66. }

68. OH_Crypto_ErrCode doTestSm2EncMessage()
69. {
70. OH_CryptoAsymKeyGenerator *keyGen = nullptr;
71. OH_Crypto_ErrCode ret = OH_CryptoAsymKeyGenerator_Create("SM2_256", &keyGen);
72. if (ret != CRYPTO_SUCCESS) {
73. return ret;
74. }
75. OH_CryptoKeyPair *keyPair = nullptr;
76. ret = OH_CryptoAsymKeyGenerator_Generate(keyGen, &keyPair);
77. if (ret != CRYPTO_SUCCESS) {
78. OH_CryptoAsymKeyGenerator_Destroy(keyGen);
79. return ret;
80. }

82. std::string message = "This is a test";
83. std::vector<uint8_t> plainText(message.begin(), message.end());
84. std::vector<uint8_t> cipherText = doTestSm2Enc(keyPair, plainText);
85. std::vector<uint8_t> decryptText = doTestSm2Dec(keyPair, cipherText);

87. if ((plainText.size() != decryptText.size()) ||
88. (!std::equal(plainText.begin(), plainText.end(), decryptText.begin()))) {
89. OH_CryptoKeyPair_Destroy(keyPair);
90. OH_CryptoAsymKeyGenerator_Destroy(keyGen);
91. return CRYPTO_OPERTION_ERROR;
92. }

94. OH_CryptoKeyPair_Destroy(keyPair);
95. OH_CryptoAsymKeyGenerator_Destroy(keyGen);
96. return CRYPTO_SUCCESS;
97. }
```

[SM2EncryptionDecryption.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceCpp/entry/src/main/cpp/types/project/sm2/SM2EncryptionDecryption.cpp#L16-L116)
