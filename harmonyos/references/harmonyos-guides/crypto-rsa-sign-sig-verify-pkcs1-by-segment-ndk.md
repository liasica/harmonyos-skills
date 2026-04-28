---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1-by-segment-ndk
title: 使用RSA密钥对分段签名验签 (PKCS1模式)(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 签名验签 > 签名验签开发指导 > 使用RSA密钥对分段签名验签 (PKCS1模式)(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e53faf841c37e97f734bb04f9be889074822e86769d3f900386b3d8584648c68
---

对应的算法规格请查看[签名验签算法规格：RSA](crypto-sign-sig-verify-overview.md#rsa)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libohcrypto.so)
```

## 签名开发步骤

1. 调用[OH\_CryptoSign\_Create](../harmonyos-references/capi-crypto-signature-h.md#oh_cryptosign_create)，指定字符串参数'RSA1024|PKCS1|SHA256'，创建Sign实例，用于完成签名操作。
2. 调用[OH\_CryptoSign\_Init](../harmonyos-references/capi-crypto-signature-h.md#oh_cryptosign_init)，使用私钥（OH\_CryptoPrivKey）初始化Sign实例。
3. 调用[OH\_CryptoSign\_Update](../harmonyos-references/capi-crypto-signature-h.md#oh_cryptosign_update)，传入待签名的数据。当前单次update长度没有限制，开发者可以根据数据量判断如何调用update。如果数据量较小，可以直接调用OH\_CryptoSign\_Final接口一次性传入。
4. 调用[OH\_CryptoSign\_Final](../harmonyos-references/capi-crypto-signature-h.md#oh_cryptosign_final)，获取签名后的数据。
5. 调用[OH\_CryptoSign\_Destroy](../harmonyos-references/capi-crypto-signature-h.md#oh_cryptosign_destroy)等释放内存。

```
1. #include "CryptoArchitectureKit/crypto_common.h"
2. #include "CryptoArchitectureKit/crypto_asym_key.h"
3. #include "CryptoArchitectureKit/crypto_signature.h"

5. static OH_Crypto_ErrCode doTestRsaSignSeg() {
6. OH_CryptoAsymKeyGenerator *keyCtx = nullptr;
7. OH_CryptoKeyPair *keyPair = nullptr;
8. OH_CryptoSign *sign = nullptr;
9. Crypto_DataBlob signData = {.data = nullptr, .len = 0};

11. uint8_t plainText[] = {
12. 0x43, 0x31, 0x7d, 0xb5, 0x85, 0x2e, 0xd4, 0xef, 0x08, 0x7a, 0x17, 0x96, 0xbc, 0x7c, 0x8f, 0x80,
13. 0x8c, 0xa7, 0x63, 0x7f, 0x26, 0x89, 0x8f, 0xf0, 0xfa, 0xa7, 0x51, 0xbd, 0x9c, 0x69, 0x17, 0xf3,
14. 0xd1, 0xb5, 0xc7, 0x12, 0xbf, 0xcf, 0x91, 0x25, 0x82, 0x23, 0x6b, 0xd6, 0x64, 0x52, 0x77, 0x93,
15. 0x01, 0x9d, 0x70, 0xa3, 0xf4, 0x92, 0x16, 0xec, 0x3f, 0xa7, 0x3c, 0x83, 0x8d, 0x40, 0x41, 0xfc,
16. };
17. Crypto_DataBlob msgBlob = {
18. .data = reinterpret_cast<uint8_t *>(plainText),
19. .len = sizeof(plainText)
20. };

22. OH_Crypto_ErrCode ret = OH_CryptoAsymKeyGenerator_Create((const char *)"RSA2048", &keyCtx);
23. if (ret != CRYPTO_SUCCESS) {
24. return ret;
25. }
26. ret = OH_CryptoAsymKeyGenerator_Generate(keyCtx, &keyPair);
27. if (ret != CRYPTO_SUCCESS) {
28. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
29. return ret;
30. }

32. OH_CryptoPrivKey *privKey = OH_CryptoKeyPair_GetPrivKey(keyPair);
33. ret = OH_CryptoSign_Create((const char *)"RSA1024|PKCS1|SHA256", &sign);
34. if (ret != CRYPTO_SUCCESS) {
35. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
36. OH_CryptoKeyPair_Destroy(keyPair);
37. return ret;
38. }

40. int blockSize = 20;
41. int cnt_s = 64 / blockSize;
42. int rem_s = 64 % blockSize;
43. ret = OH_CryptoSign_Init(sign, privKey);
44. if (ret != CRYPTO_SUCCESS) {
45. OH_CryptoSign_Destroy(sign);
46. OH_CryptoKeyPair_Destroy(keyPair);
47. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
48. return ret;
49. }
50. for (int i = 0; i < cnt_s; i++) {
51. msgBlob.len = blockSize;
52. ret = OH_CryptoSign_Update(sign, &msgBlob);
53. if (ret != CRYPTO_SUCCESS) {
54. OH_CryptoSign_Destroy(sign);
55. OH_CryptoKeyPair_Destroy(keyPair);
56. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
57. return ret;
58. }
59. msgBlob.data += blockSize;
60. }
61. if (rem_s > 0) {
62. msgBlob.len = rem_s;
63. ret = OH_CryptoSign_Final(sign, &msgBlob, &signData);
64. if (ret != CRYPTO_SUCCESS) {
65. OH_CryptoSign_Destroy(sign);
66. OH_CryptoKeyPair_Destroy(keyPair);
67. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
68. return ret;
69. }
70. }

72. msgBlob.data -=  64 - rem_s;
73. msgBlob.len = 64;
74. OH_CryptoSign_Destroy(sign);
75. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
76. OH_CryptoKeyPair_Destroy(keyPair);
77. return CRYPTO_SUCCESS;
78. }
```

## 验签开发步骤

1. 调用[OH\_CryptoVerify\_Create](../harmonyos-references/capi-crypto-signature-h.md#oh_cryptoverify_create)，指定字符串参数'RSA1024|PKCS1|SHA256'，与签名的Sign实例保持一致。创建Verify实例，用于完成验签操作。
2. 调用[OH\_CryptoVerify\_Init](../harmonyos-references/capi-crypto-signature-h.md#oh_cryptoverify_init)，使用公钥（OH\_CryptoPubKey）初始化Verify实例。
3. 调用[OH\_CryptoVerify\_Update](../harmonyos-references/capi-crypto-signature-h.md#oh_cryptoverify_update)，传入待验证的数据。当前单次update长度没有限制，开发者可以根据数据量判断如何调用update，如果数据量较小，可以直接调用OH\_CryptoVerify\_Final接口一次性传入。
4. 调用[OH\_CryptoVerify\_Final](../harmonyos-references/capi-crypto-signature-h.md#oh_cryptoverify_final)，对数据进行验签。

```
1. #include "signing_signature_verification.h"

3. static constexpr int INT_64 = 64;
4. bool DoTestRsaSignatureSeg()
5. {
6. OH_CryptoAsymKeyGenerator *keyCtx = nullptr;
7. OH_CryptoKeyPair *keyPair = nullptr;
8. OH_CryptoVerify *verify = nullptr;

10. uint8_t plainText[] = {
11. 0x43, 0x31, 0x7d, 0xb5, 0x85, 0x2e, 0xd4, 0xef, 0x08, 0x7a, 0x17, 0x96, 0xbc, 0x7c, 0x8f, 0x80,
12. 0x8c, 0xa7, 0x63, 0x7f, 0x26, 0x89, 0x8f, 0xf0, 0xfa, 0xa7, 0x51, 0xbd, 0x9c, 0x69, 0x17, 0xf3,
13. 0xd1, 0xb5, 0xc7, 0x12, 0xbf, 0xcf, 0x91, 0x25, 0x82, 0x23, 0x6b, 0xd6, 0x64, 0x52, 0x77, 0x93,
14. 0x01, 0x9d, 0x70, 0xa3, 0xf4, 0x92, 0x16, 0xec, 0x3f, 0xa7, 0x3c, 0x83, 0x8d, 0x40, 0x41, 0xfc,
15. };
16. Crypto_DataBlob msgBlob = {.data = reinterpret_cast<uint8_t *>(plainText), .len = sizeof(plainText)};

18. uint8_t pubKeyText[] = {
19. 0x2d, 0x2d, 0x2d, 0x2d, 0x2d, 0x42, 0x45, 0x47, 0x49, 0x4e, 0x20, 0x52, 0x53, 0x41, 0x20, 0x50, 0x55, 0x42,
20. 0x4c, 0x49, 0x43, 0x20, 0x4b, 0x45, 0x59, 0x2d, 0x2d, 0x2d, 0x2d, 0x2d, 0x0a, 0x4d, 0x49, 0x47, 0x4a, 0x41,
21. 0x6f, 0x47, 0x42, 0x41, 0x4d, 0x78, 0x63, 0x44, 0x4d, 0x6f, 0x61, 0x59, 0x52, 0x58, 0x6f, 0x78, 0x65, 0x69,
22. 0x33, 0x49, 0x6d, 0x33, 0x33, 0x78, 0x4a, 0x76, 0x61, 0x73, 0x63, 0x43, 0x62, 0x77, 0x31, 0x6f, 0x73, 0x63,
23. 0x32, 0x56, 0x56, 0x69, 0x47, 0x6a, 0x56, 0x47, 0x47, 0x4a, 0x37, 0x6c, 0x75, 0x4e, 0x41, 0x58, 0x6b, 0x6a,
24. 0x73, 0x56, 0x46, 0x64, 0x35, 0x0a, 0x58, 0x37, 0x4c, 0x4d, 0x6c, 0x46, 0x34, 0x63, 0x35, 0x5a, 0x75, 0x59,
25. 0x2f, 0x61, 0x69, 0x57, 0x77, 0x70, 0x54, 0x69, 0x63, 0x62, 0x67, 0x49, 0x33, 0x43, 0x66, 0x50, 0x6f, 0x32,
26. 0x6a, 0x6c, 0x52, 0x74, 0x67, 0x41, 0x46, 0x6b, 0x44, 0x71, 0x7a, 0x4b, 0x53, 0x46, 0x62, 0x46, 0x47, 0x51,
27. 0x6b, 0x43, 0x6e, 0x64, 0x63, 0x2b, 0x54, 0x59, 0x6b, 0x5a, 0x42, 0x32, 0x70, 0x45, 0x6f, 0x72, 0x0a, 0x7a,
28. 0x73, 0x61, 0x56, 0x58, 0x77, 0x5a, 0x47, 0x45, 0x34, 0x41, 0x43, 0x70, 0x59, 0x35, 0x79, 0x65, 0x66, 0x49,
29. 0x44, 0x6c, 0x45, 0x57, 0x49, 0x51, 0x4f, 0x6a, 0x59, 0x4b, 0x2f, 0x6c, 0x58, 0x71, 0x7a, 0x48, 0x47, 0x69,
30. 0x4f, 0x69, 0x32, 0x75, 0x4a, 0x45, 0x75, 0x44, 0x43, 0x50, 0x6a, 0x51, 0x64, 0x6a, 0x54, 0x41, 0x67, 0x4d,
31. 0x42, 0x41, 0x41, 0x45, 0x3d, 0x0a, 0x2d, 0x2d, 0x2d, 0x2d, 0x2d, 0x45, 0x4e, 0x44, 0x20, 0x52, 0x53, 0x41,
32. 0x20, 0x50, 0x55, 0x42, 0x4c, 0x49, 0x43, 0x20, 0x4b, 0x45, 0x59, 0x2d, 0x2d, 0x2d, 0x2d, 0x2d, 0x0a,
33. };

35. Crypto_DataBlob keyBlob = {.data = reinterpret_cast<uint8_t *>(pubKeyText), .len = sizeof(pubKeyText)};

37. uint8_t signText[] = {
38. 0x68, 0x2f, 0x3b, 0xe6, 0xa6, 0x5c, 0xb8, 0x60, 0xd4, 0xe1, 0x64, 0xa7, 0xd8, 0x0c, 0x9c, 0x89,
39. 0x39, 0xb4, 0xf0, 0xb7, 0xad, 0xb5, 0x8a, 0x71, 0x04, 0xf1, 0xa5, 0x63, 0xdd, 0x32, 0x6a, 0x44,
40. 0xeb, 0xff, 0xb7, 0xe6, 0x85, 0xe5, 0xa5, 0x55, 0x5d, 0x5b, 0x28, 0x53, 0x63, 0xe4, 0xb3, 0xb9,
41. 0xa8, 0x70, 0xc8, 0x8f, 0xcd, 0x21, 0x8d, 0xe6, 0x1f, 0xe5, 0x78, 0x34, 0xd3, 0x45, 0x0c, 0x9c,
42. 0x7a, 0x22, 0x1b, 0x63, 0x55, 0xca, 0x14, 0xa5, 0x0c, 0x7a, 0x40, 0x8e, 0xa1, 0x14, 0x78, 0xa1,
43. 0xf1, 0x36, 0x78, 0xbd, 0xba, 0x37, 0x3b, 0x5b, 0xb0, 0x8e, 0xb3, 0x4a, 0x9b, 0x1b, 0x0c, 0xfa,
44. 0xfa, 0xc7, 0x9f, 0xb1, 0x35, 0x48, 0x82, 0x73, 0xf8, 0x6b, 0xd4, 0x76, 0x33, 0x5c, 0xed, 0x9c,
45. 0xd8, 0x4b, 0xc9, 0x92, 0xa0, 0x3f, 0x6e, 0xba, 0x78, 0x2e, 0x80, 0x78, 0x1e, 0x74, 0xa0, 0x47,
46. };

48. Crypto_DataBlob signBlob = {.data = reinterpret_cast<uint8_t *>(signText), .len = sizeof(signText)};

50. // keypair
51. OH_Crypto_ErrCode ret = CRYPTO_SUCCESS;
52. ret = OH_CryptoAsymKeyGenerator_Create((const char *)"RSA2048", &keyCtx);
53. if (ret != CRYPTO_SUCCESS) {
54. return false;
55. }
56. ret = OH_CryptoAsymKeyGenerator_Convert(keyCtx, CRYPTO_PEM, &keyBlob, nullptr, &keyPair);
57. if (ret != CRYPTO_SUCCESS) {
58. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
59. return false;
60. }
61. OH_CryptoPubKey *pubKey = OH_CryptoKeyPair_GetPubKey(keyPair);
62. // verify
63. ret = OH_CryptoVerify_Create((const char *)"RSA1024|PKCS1|SHA256", &verify);
64. if (ret != CRYPTO_SUCCESS) {
65. OH_CryptoVerify_Destroy(verify);
66. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
67. return false;
68. }
69. int blockSize = 20;
70. int cntS = INT_64 / blockSize;
71. int remS = INT_64 % blockSize;
72. ret = OH_CryptoVerify_Init(verify, pubKey);
73. if (ret != CRYPTO_SUCCESS) {
74. OH_CryptoVerify_Destroy(verify);
75. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
76. return false;
77. }
78. for (int i = 0; i < cntS; i++) {
79. msgBlob.len = blockSize;
80. ret = OH_CryptoVerify_Update(verify, (Crypto_DataBlob *)&msgBlob);
81. if (ret != CRYPTO_SUCCESS) {
82. OH_CryptoVerify_Destroy(verify);
83. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
84. return false;
85. }
86. msgBlob.data += blockSize;
87. }
88. bool res = false;
89. if (remS > 0) {
90. msgBlob.len = remS;
91. res = OH_CryptoVerify_Final(verify, (Crypto_DataBlob *)&msgBlob, (Crypto_DataBlob *)&signBlob);
92. if (res != true) {
93. OH_CryptoVerify_Destroy(verify);
94. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
95. return false;
96. }
97. }

99. msgBlob.data -= INT_64 - remS;
100. msgBlob.len = INT_64;

102. OH_CryptoVerify_Destroy(verify);
103. OH_CryptoAsymKeyGenerator_Destroy(keyCtx);
104. OH_CryptoKeyPair_Destroy(keyPair);
105. return res;
106. }
```

[rsa\_pkcs1\_segment\_signature.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/SignatureVerification/SigningSignatureVerification/entry/src/main/cpp/types/project/rsa_pkcs1_segment_signature.cpp#L16-L123)
