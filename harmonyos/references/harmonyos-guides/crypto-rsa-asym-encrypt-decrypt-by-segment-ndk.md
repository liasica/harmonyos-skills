---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-by-segment-ndk
title: 使用RSA非对称密钥分段加解密(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用RSA非对称密钥分段加解密(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:30+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:ea81687f0915e09a15a4497975009a24318aa2ed4e176dbd4fa6ee68b127e2e1
---

对应的算法规格请查看[非对称密钥加解密算法规格：RSA](crypto-asym-encrypt-decrypt-spec.md#rsa)。

**加密**

1. 调用[OH\_CryptoAsymKeyGenerator\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_create)、[OH\_CryptoAsymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_generate)，生成RSA密钥类型为RSA1024、素数个数为2的非对称密钥对（keyPair）。keyPair对象中包括公钥PubKey、私钥PriKey。

   如何生成RSA非对称密钥对，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：RSA](crypto-asym-key-generation-conversion-spec.md#rsa)和[随机生成非对称密钥对](crypto-generate-asym-key-pair-randomly.md)理解。参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[OH\_CryptoAsymCipher\_Create](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_create)，指定字符串参数'RSA1024|PKCS1'，创建非对称密钥类型为RSA1024、填充模式为PKCS1的Cipher实例，用于完成加解密操作。
3. 调用[OH\_CryptoAsymCipher\_Init](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（keyPair），初始化加密Cipher实例。
4. 多次调用[OH\_CryptoAsymCipher\_Final](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_final)，传入明文，获取加密后的数据。

   * OH\_CryptoAsymCipher\_Final输出结果可能为NULL，在访问具体数据前，需要先判断结果是否为NULL，避免产生异常。
   * 此处将明文按64个字节一组拆分，多次加密。使用1024位密钥，每次将生成128字节密文。

     说明

     非对称密钥的分段加解密是指当明文大于单次加解密支持的数据长度时，需要将待加解密数据分为合适长度的数据段，并对每个数据段执行加解密操作。详细介绍可见[非对称分段加解密介绍](crypto-encrypt-decrypt-by-segment.md#非对称加解密)。

**解密**

1. 由于RSA算法的Cipher实例不支持重复init操作，需要调用[OH\_CryptoAsymCipher\_Create](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_create)，重新生成Cipher实例。
2. 调用[OH\_CryptoAsymCipher\_Init](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（keyPair）初始化解密Cipher实例。
3. 多次调用[OH\_CryptoAsymCipher\_Final](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_final)，传入密文，获取解密后的数据。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"
2. #include <algorithm>
3. #include <vector>
4. #include <string>

6. static std::vector<uint8_t> doTestRsaEnc(OH_CryptoKeyPair *keyPair, std::vector<uint8_t> &plainText)
7. {
8. std::vector<uint8_t> cipherText;
9. OH_CryptoAsymCipher *cipher = nullptr;
10. OH_Crypto_ErrCode ret = OH_CryptoAsymCipher_Create("RSA1024|PKCS1", &cipher);
11. if (ret != CRYPTO_SUCCESS) {
12. return std::vector<uint8_t>{};
13. }

15. ret = OH_CryptoAsymCipher_Init(cipher, CRYPTO_ENCRYPT_MODE, keyPair);
16. if (ret != CRYPTO_SUCCESS) {
17. OH_CryptoAsymCipher_Destroy(cipher);
18. return std::vector<uint8_t>{};
19. }

21. size_t plainTextSplitLen = 64;
22. for (size_t i = 0; i < plainText.size(); i += plainTextSplitLen) {
23. Crypto_DataBlob in = {};
24. in.data = plainText.data() + i;
25. if (i + plainTextSplitLen > plainText.size()) {
26. in.len = plainText.size() - i;
27. } else {
28. in.len = plainTextSplitLen;
29. }
30. Crypto_DataBlob out = {};
31. ret = OH_CryptoAsymCipher_Final(cipher, &in, &out);
32. if (ret != CRYPTO_SUCCESS) {
33. OH_CryptoAsymCipher_Destroy(cipher);
34. return std::vector<uint8_t>{};
35. }
36. cipherText.insert(cipherText.end(), out.data, out.data + out.len);
37. OH_Crypto_FreeDataBlob(&out);
38. }

40. OH_CryptoAsymCipher_Destroy(cipher);
41. return cipherText;
42. }

44. static std::vector<uint8_t> doTestRsaDec(OH_CryptoKeyPair *keyPair, std::vector<uint8_t> &encryptText)
45. {
46. std::vector<uint8_t> decryptText;
47. OH_CryptoAsymCipher *cipher = nullptr;
48. OH_Crypto_ErrCode ret = OH_CryptoAsymCipher_Create("RSA1024|PKCS1", &cipher);
49. if (ret != CRYPTO_SUCCESS) {
50. return std::vector<uint8_t>{};
51. }

53. ret = OH_CryptoAsymCipher_Init(cipher, CRYPTO_DECRYPT_MODE, keyPair);
54. if (ret != CRYPTO_SUCCESS) {
55. OH_CryptoAsymCipher_Destroy(cipher);
56. return std::vector<uint8_t>{};
57. }

59. size_t cipherTextSplitLen = 128; // RSA密钥每次加密生成的密文字节长度计算方式：密钥位数/8。
60. for (size_t i = 0; i < encryptText.size(); i += cipherTextSplitLen) {
61. Crypto_DataBlob in = {};
62. in.data = encryptText.data() + i;
63. if (i + cipherTextSplitLen > encryptText.size()) {
64. in.len = encryptText.size() - i;
65. } else {
66. in.len = cipherTextSplitLen;
67. }
68. Crypto_DataBlob out = {};
69. ret = OH_CryptoAsymCipher_Final(cipher, &in, &out);
70. if (ret != CRYPTO_SUCCESS) {
71. OH_CryptoAsymCipher_Destroy(cipher);
72. return std::vector<uint8_t>{};
73. }
74. decryptText.insert(decryptText.end(), out.data, out.data + out.len);
75. OH_Crypto_FreeDataBlob(&out);
76. }

78. OH_CryptoAsymCipher_Destroy(cipher);
79. return decryptText;
80. }

82. OH_Crypto_ErrCode doTestRsaEncLongMessage()
83. {
84. OH_CryptoAsymKeyGenerator *keyGen = nullptr;
85. OH_Crypto_ErrCode ret = OH_CryptoAsymKeyGenerator_Create("RSA1024", &keyGen);
86. if (ret != CRYPTO_SUCCESS) {
87. return ret;
88. }
89. OH_CryptoKeyPair *keyPair = nullptr;
90. ret = OH_CryptoAsymKeyGenerator_Generate(keyGen, &keyPair);
91. if (ret != CRYPTO_SUCCESS) {
92. OH_CryptoAsymKeyGenerator_Destroy(keyGen);
93. return ret;
94. }

96. std::string message =
97. "This is a long plainText! This is a long plainText! This is a long plainText!"
98. "This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!"
99. "This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!"
100. "This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!"
101. "This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!"
102. "This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!"
103. "This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!"
104. "This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!";

106. std::vector<uint8_t> plainText(message.begin(), message.end());
107. std::vector<uint8_t> cipherText = doTestRsaEnc(keyPair, plainText);
108. std::vector<uint8_t> decryptText = doTestRsaDec(keyPair, cipherText);

110. if ((plainText.size() != decryptText.size()) ||
111. (!std::equal(plainText.begin(), plainText.end(), decryptText.begin()))) {
112. OH_CryptoKeyPair_Destroy(keyPair);
113. OH_CryptoAsymKeyGenerator_Destroy(keyGen);
114. return CRYPTO_OPERTION_ERROR;
115. }

117. OH_CryptoKeyPair_Destroy(keyPair);
118. OH_CryptoAsymKeyGenerator_Destroy(keyGen);
119. return CRYPTO_SUCCESS;
120. }
```

[RSAEncryptDecrypt.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceCpp/entry/src/main/cpp/types/project/rsa/RSAEncryptDecrypt.cpp#L16-L138)
