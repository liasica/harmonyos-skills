---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-dh-ndk
title: 使用DH进行密钥协商(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥协商 > 密钥协商开发指导 > 使用DH进行密钥协商(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:063b1249beef80a52553e09bfde4d9f4a8d343f8fadbeb942954f4d59ef23dee
---

对应的算法规格请查看[密钥协商算法规格：DH](crypto-key-agreement-overview.md#dh)。

## 开发步骤

1. 调用[OH\_CryptoAsymKeyGenerator\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_create)、[OH\_CryptoAsymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_generate)生成密钥算法为DH\_modp1536的非对称密钥（keyPair）。

   如何生成DH非对称密钥，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：DH](crypto-asym-key-generation-conversion-spec.md#dh)和[随机生成非对称密钥对](crypto-generate-asym-key-pair-randomly-ndk.md)理解。参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[OH\_CryptoKeyAgreement\_Create](../harmonyos-references/capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_create)，指定字符串参数'DH\_modp1536'，创建密钥算法为DH\_modp1536的密钥协议生成器。
3. 调用[OH\_CryptoKeyAgreement\_GenerateSecret](../harmonyos-references/capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_generatesecret)，基于传入的私钥（keyPair.priKey）与公钥（keyPair.pubKey）进行密钥协商，返回共享密钥。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"
2. #include "CryptoArchitectureKit/crypto_key_agreement.h"
3. #include "file.h"
4. #include <cstdio>
5. #include <cstring>

7. static OH_Crypto_ErrCode GenerateSecret(OH_CryptoKeyAgreement *dhKeyAgreement, OH_CryptoKeyPair *keyPairA,
8. OH_CryptoKeyPair *keyPairB, Crypto_DataBlob *secret)
9. {
10. OH_CryptoPrivKey *privKey = OH_CryptoKeyPair_GetPrivKey(keyPairA);
11. OH_CryptoPubKey *pubKey = OH_CryptoKeyPair_GetPubKey(keyPairB);
12. return OH_CryptoKeyAgreement_GenerateSecret(dhKeyAgreement, privKey, pubKey, secret);
13. }

15. static OH_Crypto_ErrCode compareSecrets(const Crypto_DataBlob *secret1, const Crypto_DataBlob *secret2)
16. {
17. if ((secret1->len == secret2->len) &&
18. (memcmp(secret1->data, secret2->data, secret1->len) == 0)) {
19. return CRYPTO_SUCCESS;
20. }
21. return CRYPTO_OPERTION_ERROR;
22. }

24. OH_Crypto_ErrCode doTestDHKeyAgreement()
25. {
26. OH_CryptoAsymKeyGenerator *dhGen = nullptr;
27. OH_CryptoKeyPair *keyPairA = nullptr;
28. OH_CryptoKeyPair *keyPairB = nullptr;
29. OH_CryptoKeyAgreement *dhKeyAgreement = nullptr;
30. Crypto_DataBlob secret1 = { 0 };
31. Crypto_DataBlob secret2 = { 0 };
32. OH_Crypto_ErrCode ret = OH_CryptoAsymKeyGenerator_Create("DH_modp1536", &dhGen);
33. if (ret != CRYPTO_SUCCESS) {
34. return ret;
35. }

37. // 生成公私钥对A 和 B。
38. ret = OH_CryptoAsymKeyGenerator_Generate(dhGen, &keyPairA);
39. if (ret != CRYPTO_SUCCESS) {
40. goto goto_cleanup;
41. }

43. ret = OH_CryptoAsymKeyGenerator_Generate(dhGen, &keyPairB);
44. if (ret != CRYPTO_SUCCESS) {
45. goto goto_cleanup;
46. }

48. ret = OH_CryptoKeyAgreement_Create("DH_modp1536", &dhKeyAgreement);
49. if (ret != CRYPTO_SUCCESS) {
50. goto goto_cleanup;
51. }

53. // 使用A的公钥和B的私钥进行密钥协商。
54. ret = GenerateSecret(dhKeyAgreement, keyPairB, keyPairA, &secret1);
55. if (ret != CRYPTO_SUCCESS) {
56. goto goto_cleanup;
57. }

59. // 使用B的公钥和A的私钥进行密钥协商。
60. ret = GenerateSecret(dhKeyAgreement, keyPairA, keyPairB, &secret2);
61. if (ret != CRYPTO_SUCCESS) {
62. goto goto_cleanup;
63. }

65. // 比较两次协商的结果。
66. ret = compareSecrets(&secret1, &secret2);
67. if (ret != CRYPTO_SUCCESS) {
68. printf("dh result is not equal\n");
69. goto goto_cleanup;
70. }

72. goto_cleanup:
73. OH_Crypto_FreeDataBlob(&secret1);
74. OH_Crypto_FreeDataBlob(&secret2);
75. OH_CryptoKeyAgreement_Destroy(dhKeyAgreement);
76. OH_CryptoKeyPair_Destroy(keyPairA);
77. OH_CryptoKeyPair_Destroy(keyPairB);
78. OH_CryptoAsymKeyGenerator_Destroy(dhGen);
79. return ret;
80. }
```

[DH.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyNegotiationCpp/entry/src/main/cpp/types/project/DH.cpp#L16-L99)
