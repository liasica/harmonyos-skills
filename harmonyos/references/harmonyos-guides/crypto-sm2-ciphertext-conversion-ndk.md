---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-ciphertext-conversion-ndk
title: 使用SM2密文格式转换(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用SM2密文格式转换(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a6d2080abe806b61ef8c53a5e4cc2af4c4935c2c5d2a9dc8cfccfb4c106ad290
---

当前支持的SM2密文格式为国密标准的ASN.1格式，其中各参数组合顺序为C1C3C2，具体参数含义请参考[转换SM2密文格式](crypto-asym-encrypt-decrypt-spec.md#转换sm2密文格式)。

开发者可指定SM2密文的参数，将其转换成符合国密标准的ASN.1格式密文。反之，也可以从国密标准的ASN.1格式密文中取出具体的SM2密文参数，便于开发者自行组合成其他格式的SM2密文。

**指定密文参数，生成标准ASN.1密文**

1. 调用[OH\_CryptoSm2CiphertextSpec\_Create](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptosm2ciphertextspec_create)，创建空的SM2密文规格对象。
2. 调用[OH\_CryptoSm2CiphertextSpec\_SetItem](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptosm2ciphertextspec_setitem)，设置密文的各个参数（C1.x、C1.y、C2、C3）。
3. 调用[OH\_CryptoSm2CiphertextSpec\_Encode](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptosm2ciphertextspec_encode)，生成ASN.1格式的密文（当前密文转换仅支持SM3，实现中只校验hash长度是否为32字节）。
4. 使用完毕后，调用[OH\_CryptoSm2CiphertextSpec\_Destroy](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptosm2ciphertextspec_destroy)销毁SM2密文规格对象。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"

3. OH_Crypto_ErrCode doTestGenCipherTextBySpec()
4. {
5. // 准备SM2密文参数。
6. uint8_t c1x[] = {45, 153, 88, 82, 104, 221, 226, 43, 174, 21, 122, 248, 5, 232, 105, 41, 92, 95, 102, 224,
7. 216, 149, 85, 236, 110, 6, 64, 188, 149, 70, 70, 183};
8. uint8_t c1y[] = {107, 93, 198, 247, 119, 18, 40, 110, 90, 156, 193, 158, 205, 113, 170, 128, 146, 109, 75,
9. 17, 181, 109, 110, 91, 149, 5, 110, 233, 209, 78, 229, 96};
10. uint8_t c2[] = {100, 227, 78, 195, 249, 179, 43, 70, 242, 69, 169, 10, 65, 123};
11. uint8_t c3[] = {87, 167, 167, 247, 88, 146, 203, 234, 83, 126, 117, 129, 52, 142, 82, 54, 152, 226, 201, 111,
12. 143, 115, 169, 125, 128, 42, 157, 31, 114, 198, 109, 244};

14. // 创建空的SM2密文规格对象。
15. OH_CryptoSm2CiphertextSpec *sm2CipherSpec = nullptr;
16. OH_Crypto_ErrCode ret = OH_CryptoSm2CiphertextSpec_Create(nullptr, &sm2CipherSpec);
17. if (ret != CRYPTO_SUCCESS) {
18. return ret;
19. }

21. // 设置各个参数。
22. Crypto_DataBlob c1xBlob = {c1x, sizeof(c1x)};
23. Crypto_DataBlob c1yBlob = {c1y, sizeof(c1y)};
24. Crypto_DataBlob c2Blob = {c2, sizeof(c2)};
25. Crypto_DataBlob c3Blob = {c3, sizeof(c3)};

27. ret = OH_CryptoSm2CiphertextSpec_SetItem(sm2CipherSpec, CRYPTO_SM2_CIPHERTEXT_C1_X, &c1xBlob);
28. if (ret != CRYPTO_SUCCESS) {
29. OH_CryptoSm2CiphertextSpec_Destroy(sm2CipherSpec);
30. return ret;
31. }
32. ret = OH_CryptoSm2CiphertextSpec_SetItem(sm2CipherSpec, CRYPTO_SM2_CIPHERTEXT_C1_Y, &c1yBlob);
33. if (ret != CRYPTO_SUCCESS) {
34. OH_CryptoSm2CiphertextSpec_Destroy(sm2CipherSpec);
35. return ret;
36. }
37. ret = OH_CryptoSm2CiphertextSpec_SetItem(sm2CipherSpec, CRYPTO_SM2_CIPHERTEXT_C2, &c2Blob);
38. if (ret != CRYPTO_SUCCESS) {
39. OH_CryptoSm2CiphertextSpec_Destroy(sm2CipherSpec);
40. return ret;
41. }
42. ret = OH_CryptoSm2CiphertextSpec_SetItem(sm2CipherSpec, CRYPTO_SM2_CIPHERTEXT_C3, &c3Blob);
43. if (ret != CRYPTO_SUCCESS) {
44. OH_CryptoSm2CiphertextSpec_Destroy(sm2CipherSpec);
45. return ret;
46. }

48. // 编码为ASN.1格式。
49. Crypto_DataBlob encoded = { 0 };
50. ret = OH_CryptoSm2CiphertextSpec_Encode(sm2CipherSpec, &encoded);
51. if (ret != CRYPTO_SUCCESS) {
52. OH_CryptoSm2CiphertextSpec_Destroy(sm2CipherSpec);
53. return ret;
54. }

56. // 清理资源。
57. OH_Crypto_FreeDataBlob(&encoded);
58. OH_CryptoSm2CiphertextSpec_Destroy(sm2CipherSpec);
59. return ret;
60. }
```

[CreateASN1Ciphertext.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceCpp/entry/src/main/cpp/types/project/sm2/CreateASN1Ciphertext.cpp#L16-L78)

**从标准ASN.1密文中获取密文参数**

1. 调用[OH\_CryptoSm2CiphertextSpec\_Create](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptosm2ciphertextspec_create)，从ASN.1格式密文创建SM2密文规格对象。
2. 调用[OH\_CryptoSm2CiphertextSpec\_GetItem](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptosm2ciphertextspec_getitem)，获取密文中的各个参数（C1.x、C1.y、C2、C3）。
3. 使用完毕后，调用[OH\_CryptoSm2CiphertextSpec\_Destroy](../harmonyos-references/capi-crypto-asym-cipher-h.md#oh_cryptosm2ciphertextspec_destroy)销毁SM2密文规格对象。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"

3. OH_Crypto_ErrCode doTestGetCipherTextSpec()
4. {
5. // 准备标准ASN.1格式密文。
6. uint8_t cipherTextArray[] = {
7. 48, 118, 2, 32, 45, 153, 88, 82, 104, 221, 226, 43, 174, 21, 122, 248, 5, 232, 105,
8. 41, 92, 95, 102, 224, 216, 149, 85, 236, 110, 6, 64, 188, 149, 70, 70, 183, 2, 32, 107,
9. 93, 198, 247, 119, 18, 40, 110, 90, 156, 193, 158, 205, 113, 170, 128, 146, 109, 75, 17,
10. 181, 109, 110, 91, 149, 5, 110, 233, 209, 78, 229, 96, 4, 32, 87, 167, 167, 247, 88, 146,
11. 203, 234, 83, 126, 117, 129, 52, 142, 82, 54, 152, 226, 201, 111, 143, 115, 169, 125, 128,
12. 42, 157, 31, 114, 198, 109, 244, 4, 14, 100, 227, 78, 195, 249, 179, 43, 70, 242, 69, 169,
13. 10, 65, 123
14. };
15. Crypto_DataBlob cipherText = {cipherTextArray, sizeof(cipherTextArray)};

17. // 从ASN.1格式密文创建SM2密文规格对象。
18. OH_CryptoSm2CiphertextSpec *sm2CipherSpec = nullptr;
19. OH_Crypto_ErrCode ret = OH_CryptoSm2CiphertextSpec_Create(&cipherText, &sm2CipherSpec);
20. if (ret != CRYPTO_SUCCESS) {
21. return ret;
22. }

24. // 获取各个参数。
25. Crypto_DataBlob c1x = { 0 };
26. Crypto_DataBlob c1y = { 0 };
27. Crypto_DataBlob c2 = { 0 };
28. Crypto_DataBlob c3 = { 0 };

30. ret = OH_CryptoSm2CiphertextSpec_GetItem(sm2CipherSpec, CRYPTO_SM2_CIPHERTEXT_C1_X, &c1x);
31. if (ret != CRYPTO_SUCCESS) {
32. goto EXIT;
33. }
34. ret = OH_CryptoSm2CiphertextSpec_GetItem(sm2CipherSpec, CRYPTO_SM2_CIPHERTEXT_C1_Y, &c1y);
35. if (ret != CRYPTO_SUCCESS) {
36. goto EXIT;
37. }
38. ret = OH_CryptoSm2CiphertextSpec_GetItem(sm2CipherSpec, CRYPTO_SM2_CIPHERTEXT_C2, &c2);
39. if (ret != CRYPTO_SUCCESS) {
40. goto EXIT;
41. }
42. ret = OH_CryptoSm2CiphertextSpec_GetItem(sm2CipherSpec, CRYPTO_SM2_CIPHERTEXT_C3, &c3);
43. if (ret != CRYPTO_SUCCESS) {
44. goto EXIT;
45. }

47. EXIT:
48. OH_Crypto_FreeDataBlob(&c1x);
49. OH_Crypto_FreeDataBlob(&c1y);
50. OH_Crypto_FreeDataBlob(&c2);
51. OH_Crypto_FreeDataBlob(&c3);
52. OH_CryptoSm2CiphertextSpec_Destroy(sm2CipherSpec);
53. return ret;
54. }
```

[ObtainCiphertext.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceCpp/entry/src/main/cpp/types/project/sm2/ObtainCiphertext.cpp#L16-L73)
