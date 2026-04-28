---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-ecdh-ndk
title: 使用ECDH进行密钥协商(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥协商 > 密钥协商开发指导 > 使用ECDH进行密钥协商(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bc76ebee2ad18630721903e52f9b9aef161751d083db0f341a9fd0d3a5fbc550
---

对应的算法规格请查看[密钥协商算法规格：ECDH](crypto-key-agreement-overview.md#ecdh)。

## 开发步骤

1. 调用[OH\_CryptoAsymKeyGenerator\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_create)、[OH\_CryptoAsymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_generate)、[OH\_CryptoAsymKeyGenerator\_Convert](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_convert)生成密钥算法为ECC、密钥长度为256位的非对称密钥（keyPair）。

   如何生成ECC非对称密钥，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：ECC](crypto-asym-key-generation-conversion-spec.md#ecc)和[随机生成非对称密钥对](crypto-generate-asym-key-pair-randomly-ndk.md)理解。参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[OH\_CryptoKeyAgreement\_Create](../harmonyos-references/capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_create)，指定字符串参数'ECC256'，创建密钥算法为ECC、密钥长度为256位的密钥协议生成器。
3. 调用[OH\_CryptoKeyAgreement\_GenerateSecret](../harmonyos-references/capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_generatesecret)，基于传入的私钥（keyPair.priKey）与公钥（keyPair.pubKey）进行密钥协商，返回共享密钥。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"
2. #include "CryptoArchitectureKit/crypto_key_agreement.h"
3. #include "file.h"
4. #include <cstdio>
5. #include <cstring>

7. static OH_Crypto_ErrCode GenerateSecret(OH_CryptoKeyAgreement *eccKeyAgreement, OH_CryptoKeyPair *keyPairA,
8. OH_CryptoKeyPair *keyPairB, Crypto_DataBlob *secret)
9. {
10. OH_CryptoPrivKey *privKey = OH_CryptoKeyPair_GetPrivKey(keyPairA);
11. OH_CryptoPubKey *pubKey = OH_CryptoKeyPair_GetPubKey(keyPairB);
12. return OH_CryptoKeyAgreement_GenerateSecret(eccKeyAgreement, privKey, pubKey, secret);
13. }

15. static OH_Crypto_ErrCode compareSecrets(const Crypto_DataBlob *secret1, const Crypto_DataBlob *secret2)
16. {
17. if ((secret1->len == secret2->len) &&
18. (memcmp(secret1->data, secret2->data, secret1->len) == 0)) {
19. return CRYPTO_SUCCESS;
20. }
21. return CRYPTO_OPERTION_ERROR;
22. }

24. static OH_Crypto_ErrCode CovertKeyPairByBlob(OH_CryptoAsymKeyGenerator *eccGen, OH_CryptoKeyPair **keyPair)
25. {
26. uint8_t pubKeyArray[] = {48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7,
27. 3, 66, 0, 4, 83, 96, 142, 9, 86, 214, 126, 106, 247, 233, 92, 125, 4, 128, 138, 105, 246,
28. 162, 215, 71, 81, 58, 202, 121, 26, 105, 211, 55, 130, 45, 236, 143, 55, 16, 248, 75, 167,
29. 160, 167, 106, 2, 152, 243, 44, 68, 66, 0, 167, 99, 92, 235, 215, 159, 239, 28, 106, 124,
30. 171, 34, 145, 124, 174, 57, 92};
31. uint8_t priKeyArray[] = {48, 49, 2, 1, 1, 4, 32, 115, 56, 137, 35, 207, 0, 60, 191, 90, 61, 136, 105, 210, 16,
32. 27, 4, 171, 57, 10, 61, 123, 40, 189, 28, 34, 207, 236, 22, 45, 223, 10, 189, 160, 10, 6,
33. 8, 42, 134, 72, 206, 61, 3, 1, 7};
34. Crypto_DataBlob pubKeyBlob = {pubKeyArray, sizeof(pubKeyArray)};
35. Crypto_DataBlob priKeyBlob = {priKeyArray, sizeof(priKeyArray)};
36. return OH_CryptoAsymKeyGenerator_Convert(eccGen, CRYPTO_DER, &pubKeyBlob, &priKeyBlob, keyPair);
37. }

39. OH_Crypto_ErrCode doTestEcdhKeyAgreement()
40. {
41. OH_CryptoAsymKeyGenerator *eccGen = nullptr;
42. OH_CryptoKeyPair *keyPairA = nullptr;
43. OH_CryptoKeyPair *keyPairB = nullptr;
44. OH_CryptoKeyAgreement *eccKeyAgreement = nullptr;
45. Crypto_DataBlob secret1 = { 0 };
46. Crypto_DataBlob secret2 = { 0 };

48. OH_Crypto_ErrCode ret = OH_CryptoAsymKeyGenerator_Create("ECC256", &eccGen);
49. if (ret != CRYPTO_SUCCESS) {
50. return ret;
51. }

53. ret = CovertKeyPairByBlob(eccGen, &keyPairA);
54. if (ret != CRYPTO_SUCCESS) {
55. goto goto_cleanup;
56. }

58. ret = OH_CryptoAsymKeyGenerator_Generate(eccGen, &keyPairB);
59. if (ret != CRYPTO_SUCCESS) {
60. goto goto_cleanup;
61. }

63. ret = OH_CryptoKeyAgreement_Create("ECC256", &eccKeyAgreement);
64. if (ret != CRYPTO_SUCCESS) {
65. goto goto_cleanup;
66. }

68. // 使用A的公钥和B的私钥进行密钥协商。
69. ret = GenerateSecret(eccKeyAgreement, keyPairB, keyPairA, &secret1);
70. if (ret != CRYPTO_SUCCESS) {
71. goto goto_cleanup;
72. }

74. // 使用A的私钥和B的公钥进行密钥协商。
75. ret = GenerateSecret(eccKeyAgreement, keyPairA, keyPairB, &secret2);
76. if (ret != CRYPTO_SUCCESS) {
77. goto goto_cleanup;
78. }

80. // 比较两次协商的结果。
81. ret = compareSecrets(&secret1, &secret2);
82. if (ret != CRYPTO_SUCCESS) {
83. printf("ecdh result is not equal\n");
84. goto goto_cleanup;
85. }

87. goto_cleanup:
88. OH_Crypto_FreeDataBlob(&secret1);
89. OH_Crypto_FreeDataBlob(&secret2);
90. OH_CryptoKeyAgreement_Destroy(eccKeyAgreement);
91. OH_CryptoKeyPair_Destroy(keyPairA);
92. OH_CryptoKeyPair_Destroy(keyPairB);
93. OH_CryptoAsymKeyGenerator_Destroy(eccGen);
94. return ret;
95. }
```

[ECDH.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyNegotiationCpp/entry/src/main/cpp/types/project/ECDH.cpp#L16-L114)
