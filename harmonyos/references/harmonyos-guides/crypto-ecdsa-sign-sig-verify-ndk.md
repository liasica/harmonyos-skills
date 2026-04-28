---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-ecdsa-sign-sig-verify-ndk
title: 使用ECDSA密钥对签名验签 (C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 签名验签 > 签名验签开发指导 > 使用ECDSA密钥对签名验签 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:34+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:3cd3d2a9dfec519f20fde3f269e2cf2e0a51b43cbaa40907a1730720761bd48b
---

对应的算法规格请查看[签名验签算法规格：ECDSA](crypto-sign-sig-verify-overview.md#ecdsa)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libohcrypto.so)
```

## 签名开发步骤

1. 调用[OH\_CryptoSign\_Create](../harmonyos-references/capi-crypto-signature-h.md#oh_cryptosign_create)，指定字符串参数'ECC256|SHA256'，创建非对称密钥类型为ECC256、摘要算法为SHA256的Sign实例，用于完成签名操作。
2. 调用[OH\_CryptoSign\_Init](../harmonyos-references/capi-crypto-signature-h.md#oh_cryptosign_init)，使用私钥[OH\_CryptoPrivKey](../harmonyos-references/capi-cryptoasymkeyapi-oh-cryptoprivkey.md)初始化Sign实例。
3. 调用[OH\_CryptoSign\_Update](../harmonyos-references/capi-crypto-signature-h.md#oh_cryptosign_update)，传入待签名的数据。当前单次update长度没有限制，开发者可以根据数据量判断如何调用update，如果数据量较小，可以直接调用OH\_CryptoSign\_Final接口一次性传入。
4. 调用[OH\_CryptoSign\_Final](../harmonyos-references/capi-crypto-signature-h.md#oh_cryptosign_final)，对数据进行签名。
5. 调用[OH\_CryptoSign\_Destroy](../harmonyos-references/capi-crypto-signature-h.md#oh_cryptosign_destroy)等释放内存。

```
1. #include "CryptoArchitectureKit/crypto_common.h"
2. #include "CryptoArchitectureKit/crypto_signature.h"
3. #include "CryptoArchitectureKit/crypto_asym_key.h"

5. static OH_Crypto_ErrCode doTestRsaPssSignSeg() {
6. OH_CryptoAsymKeyGenerator *keyCtx = nullptr;
7. OH_CryptoKeyPair *keyPair = nullptr;
8. OH_CryptoSign *sign = nullptr;
9. Crypto_DataBlob signData = {.data = nullptr, .len = 0};

11. uint8_t plainText[] = {
12. 0xe4, 0x2b, 0xcc, 0x08, 0x11, 0x79, 0x16, 0x1b, 0x35, 0x7f, 0xb3, 0xaf, 0x40, 0x3b, 0x3f, 0x7c
13. }; // 待签名数据，仅供参考。
14. Crypto_DataBlob msgBlob = {
15. .data = reinterpret_cast<uint8_t *>(plainText),
16. .len = sizeof(plainText)
17. };

19. OH_Crypto_ErrCode ret = OH_CryptoAsymKeyGenerator_Create((const char *)"ECC256", &keyCtx);
20. if (ret != CRYPTO_SUCCESS) {
21. return ret;
22. }
23. ret = OH_CryptoAsymKeyGenerator_Generate(keyCtx, &keyPair);
24. if (ret != CRYPTO_SUCCESS) {
25. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
26. return ret;
27. }

29. OH_CryptoPrivKey *privKey = OH_CryptoKeyPair_GetPrivKey(keyPair);
30. ret = OH_CryptoSign_Create((const char *)"ECC256|SHA256", &sign);
31. if (ret != CRYPTO_SUCCESS) {
32. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
33. OH_CryptoKeyPair_Destroy(keyPair);
34. return ret;
35. }

37. ret = OH_CryptoSign_Init(sign, privKey);
38. if (ret != CRYPTO_SUCCESS) {
39. OH_CryptoSign_Destroy(sign);
40. OH_CryptoKeyPair_Destroy(keyPair);
41. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
42. return ret;
43. }
44. ret = OH_CryptoSign_Update(sign, &msgBlob);
45. if (ret != CRYPTO_SUCCESS) {
46. OH_CryptoSign_Destroy(sign);
47. OH_CryptoKeyPair_Destroy(keyPair);
48. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
49. return ret;
50. }
51. ret = OH_CryptoSign_Final(sign, nullptr, &signData);
52. if (ret != CRYPTO_SUCCESS) {
53. OH_CryptoSign_Destroy(sign);
54. OH_CryptoKeyPair_Destroy(keyPair);
55. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
56. return ret;
57. }

59. OH_CryptoSign_Destroy(sign);
60. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
61. OH_CryptoKeyPair_Destroy(keyPair);
62. return CRYPTO_SUCCESS;
63. }
```

## 验签开发步骤

1. 调用[OH\_CryptoVerify\_Create](../harmonyos-references/capi-crypto-signature-h.md#oh_cryptoverify_create)，指定字符串参数'ECC256|SHA256'，创建非对称密钥类型为ECC256、摘要算法为SHA256的Verify实例，用于完成验签操作。
2. 调用[OH\_CryptoVerify\_Init](../harmonyos-references/capi-crypto-signature-h.md#oh_cryptoverify_init)，使用公钥（OH\_CryptoPubKey）初始化Verify实例。
3. 调用[OH\_CryptoVerify\_Update](../harmonyos-references/capi-crypto-signature-h.md#oh_cryptoverify_update)，传入待验证的数据。当前单次update长度没有限制，开发者可以根据数据量判断如何调用update，如果数据量较小，可以直接调用OH\_CryptoVerify\_Final接口一次性传入。
4. 调用[OH\_CryptoVerify\_Final](../harmonyos-references/capi-crypto-signature-h.md#oh_cryptoverify_final)，对数据进行验签。

```
1. #include "signing_signature_verification.h"

3. bool DoTestEcdsaSignature()
4. {
5. OH_CryptoAsymKeyGenerator *keyCtx = nullptr;
6. OH_CryptoKeyPair *keyPair = nullptr;
7. OH_CryptoVerify *verify = nullptr;

9. uint8_t plainText[] = {0xe4, 0x2b, 0xcc, 0x08, 0x11, 0x79, 0x16, 0x1b,
10. 0x35, 0x7f, 0xb3, 0xaf, 0x40, 0x3b, 0x3f, 0x7c};
11. Crypto_DataBlob msgBlob = {.data = reinterpret_cast<uint8_t *>(plainText), .len = sizeof(plainText)};

13. uint8_t pubKeyText[] = {0x30, 0x39, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08,
14. 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x22, 0x00, 0x03, 0x4d, 0xe4, 0xbb,
15. 0x11, 0x10, 0x1a, 0xd2, 0x05, 0x74, 0xf1, 0x0b, 0xb4, 0x75, 0x57, 0xf4, 0x3e, 0x55, 0x14,
16. 0x17, 0x05, 0x4a, 0xb2, 0xfb, 0x8c, 0x84, 0x64, 0x38, 0x02, 0xa0, 0x2a, 0xa6, 0xf0};

18. Crypto_DataBlob keyBlob = {.data = reinterpret_cast<uint8_t *>(pubKeyText), .len = sizeof(pubKeyText)};

20. uint8_t signText[] = {0x30, 0x44, 0x02, 0x20, 0x21, 0x89, 0x99, 0xb1, 0x56, 0x4e, 0x3a, 0x2c, 0x16, 0x08,
21. 0xb5, 0x8a, 0x06, 0x6f, 0x67, 0x47, 0x1b, 0x04, 0x18, 0x7d, 0x53, 0x2d, 0xba, 0x00,
22. 0x38, 0xd9, 0xe3, 0xe7, 0x8c, 0xcf, 0x76, 0x83, 0x02, 0x20, 0x13, 0x54, 0x84, 0x9d,
23. 0x73, 0x40, 0xc3, 0x92, 0x66, 0xdc, 0x3e, 0xc9, 0xf1, 0x4c, 0x33, 0x84, 0x2a, 0x76,
24. 0xaf, 0xc6, 0x61, 0x84, 0x5c, 0xae, 0x4b, 0x0d, 0x3c, 0xb0, 0xc8, 0x04, 0x89, 0x71};

26. Crypto_DataBlob signBlob = {.data = reinterpret_cast<uint8_t *>(signText), .len = sizeof(signText)};

28. OH_Crypto_ErrCode ret = CRYPTO_SUCCESS;
29. // keypair
30. ret = OH_CryptoAsymKeyGenerator_Create((const char *)"ECC256", &keyCtx);
31. if (ret != CRYPTO_SUCCESS) {
32. return false;
33. }
34. ret = OH_CryptoAsymKeyGenerator_Convert(keyCtx, CRYPTO_DER, &keyBlob, nullptr, &keyPair);
35. if (ret != CRYPTO_SUCCESS) {
36. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
37. return false;
38. }
39. OH_CryptoPubKey *pubKey = OH_CryptoKeyPair_GetPubKey(keyPair);
40. // verify
41. ret = OH_CryptoVerify_Create((const char *)"ECC256|SHA256", &verify);
42. if (ret != CRYPTO_SUCCESS) {
43. OH_CryptoVerify_Destroy(verify);
44. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
45. return false;
46. }
47. ret = OH_CryptoVerify_Init(verify, pubKey);
48. if (ret != CRYPTO_SUCCESS) {
49. OH_CryptoVerify_Destroy(verify);
50. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
51. return false;
52. }
53. bool res = OH_CryptoVerify_Final(verify, &msgBlob, &signBlob);
54. if (ret != true) {
55. OH_CryptoVerify_Destroy(verify);
56. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
57. return false;
58. }

60. OH_CryptoVerify_Destroy(verify);
61. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
62. OH_CryptoKeyPair_Destroy(keyPair);
63. return res;
64. }
```

[ecdsa\_signature\_verification.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/SignatureVerification/SigningSignatureVerification/entry/src/main/cpp/types/project/ecdsa_signature_verification.cpp#L15-L80)
