---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-x25519-ndk
title: 使用X25519进行密钥协商(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥协商 > 密钥协商开发指导 > 使用X25519进行密钥协商(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:605e7c7e643c134ac1122017b3c3c52d40a749a18ea22d816ed4cae69fa072f3
---

对应的算法规格请查看[密钥协商算法规格：X25519](crypto-key-agreement-overview.md#x25519)。

## 开发步骤

1. 调用[OH\_CryptoAsymKeyGenerator\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_create)、[OH\_CryptoAsymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_generate)、[OH\_CryptoAsymKeyGenerator\_Convert](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_convert)生成密钥算法为X25519的非对称密钥（keyPair）。

   如何生成X25519非对称密钥，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：X25519](crypto-asym-key-generation-conversion-spec.md#x25519)和[随机生成非对称密钥对](crypto-generate-asym-key-pair-randomly-ndk.md)理解。参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[OH\_CryptoKeyAgreement\_Create](../harmonyos-references/capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_create)，指定字符串参数'X25519'，创建密钥算法为X25519的密钥协议生成器。
3. 调用[OH\_CryptoKeyAgreement\_GenerateSecret](../harmonyos-references/capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_generatesecret)，基于传入的私钥（keyPair.priKey）与公钥（keyPair.pubKey）进行密钥协商，返回共享密钥。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"
2. #include "CryptoArchitectureKit/crypto_key_agreement.h"
3. #include "file.h"
4. #include <cstdio>
5. #include <cstring>

8. static OH_Crypto_ErrCode GenerateSecret(OH_CryptoKeyAgreement *x25519KeyAgreement, OH_CryptoKeyPair *keyPairA,
9. OH_CryptoKeyPair *keyPairB, Crypto_DataBlob *secret)
10. {
11. OH_CryptoPrivKey *privKey = OH_CryptoKeyPair_GetPrivKey(keyPairA);
12. OH_CryptoPubKey *pubKey = OH_CryptoKeyPair_GetPubKey(keyPairB);
13. return OH_CryptoKeyAgreement_GenerateSecret(x25519KeyAgreement, privKey, pubKey, secret);
14. }

16. static OH_Crypto_ErrCode CompareSecrets(Crypto_DataBlob secret1, Crypto_DataBlob secret2)
17. {
18. if ((secret1.len == secret2.len) &&
19. (memcmp(secret1.data, secret2.data, secret1.len) == 0)) {
20. return CRYPTO_SUCCESS;
21. }
22. return CRYPTO_OPERTION_ERROR;
23. }

25. static OH_Crypto_ErrCode CovertKeyPairByBlob(OH_CryptoAsymKeyGenerator *x25519Gen, OH_CryptoKeyPair **keyPair)
26. {
27. uint8_t pubKeyArray[] = {48, 42, 48, 5, 6, 3, 43, 101, 110, 3, 33, 0, 36, 98, 216, 106, 74, 99, 179, 203, 81, 145,
28. 147, 101, 139, 57, 74, 225, 119, 196, 207, 0, 50, 232, 93, 147, 188, 21, 225, 228, 54, 251,
29. 230, 52};
30. uint8_t priKeyArray[] = {48, 46, 2, 1, 0, 48, 5, 6, 3, 43, 101, 110, 4, 34, 4, 32, 112, 65, 156, 73, 65, 89, 183,
31. 39, 119, 229, 110, 12, 192, 237, 186, 153, 21, 122, 28, 176, 248, 108, 22, 242, 239, 179,
32. 106, 175, 85, 65, 214, 90};
33. Crypto_DataBlob pubKeyBlob = {pubKeyArray, sizeof(pubKeyArray)};
34. Crypto_DataBlob priKeyBlob = {priKeyArray, sizeof(priKeyArray)};
35. return OH_CryptoAsymKeyGenerator_Convert(x25519Gen, CRYPTO_DER, &pubKeyBlob, &priKeyBlob, keyPair);
36. }

38. OH_Crypto_ErrCode doTestX25519KeyAgreement()
39. {
40. OH_CryptoAsymKeyGenerator *x25519Gen = nullptr;
41. OH_CryptoKeyPair *keyPairA = nullptr;
42. OH_CryptoKeyPair *keyPairB = nullptr;
43. OH_CryptoKeyAgreement *x25519KeyAgreement = nullptr;
44. Crypto_DataBlob secret1 = {0};
45. Crypto_DataBlob secret2 = {0};
46. OH_Crypto_ErrCode ret = OH_CryptoAsymKeyGenerator_Create("X25519", &x25519Gen);
47. if (ret != CRYPTO_SUCCESS) {
48. return ret;
49. }

51. ret = CovertKeyPairByBlob(x25519Gen, &keyPairA);
52. if (ret != CRYPTO_SUCCESS) {
53. goto goto_cleanup;
54. }

56. ret = OH_CryptoAsymKeyGenerator_Generate(x25519Gen, &keyPairB);
57. if (ret != CRYPTO_SUCCESS) {
58. goto goto_cleanup;
59. }

61. ret = OH_CryptoKeyAgreement_Create("X25519", &x25519KeyAgreement);
62. if (ret != CRYPTO_SUCCESS) {
63. goto goto_cleanup;
64. }

66. // 使用A的公钥和B的私钥进行密钥协商。
67. ret = GenerateSecret(x25519KeyAgreement, keyPairB, keyPairA, &secret1);
68. if (ret != CRYPTO_SUCCESS) {
69. goto goto_cleanup;
70. }

72. // 使用A的私钥和B的公钥进行密钥协商。
73. ret = GenerateSecret(x25519KeyAgreement, keyPairA, keyPairB, &secret2);
74. if (ret != CRYPTO_SUCCESS) {
75. goto goto_cleanup;
76. }

78. ret = CompareSecrets(secret1, secret2);
79. if (ret != CRYPTO_SUCCESS) {
80. printf("x25519 result is not equal\n");
81. goto goto_cleanup;
82. }

84. goto_cleanup:
85. OH_Crypto_FreeDataBlob(&secret1);
86. OH_Crypto_FreeDataBlob(&secret2);
87. OH_CryptoKeyAgreement_Destroy(x25519KeyAgreement);
88. OH_CryptoKeyPair_Destroy(keyPairA);
89. OH_CryptoKeyPair_Destroy(keyPairB);
90. OH_CryptoAsymKeyGenerator_Destroy(x25519Gen);
91. return CRYPTO_SUCCESS;
92. }
```

[X25519.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyNegotiationCpp/entry/src/main/cpp/types/project/X25519.cpp#L16-L111)
