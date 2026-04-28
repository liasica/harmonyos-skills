---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-random-number-ndk
title: 安全随机数生成(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 随机数 > 安全随机数生成(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d1e9cda6911eed3c262e603260539eb50d44c068956663d7e445c0ca42178f52
---

说明

从API version 12开始，轻量级智能穿戴设备支持获取随机数相关操作。

随机数主要用于临时会话密钥生成和非对称加密算法密钥生成等场景。在加解密场景中，安全随机数生成器需要具备随机性、不可预测性与不可重现性。当前系统生成的随机数满足密码学安全伪随机性要求。

开发者可以调用接口，完成以下功能：

* 生成指定长度的安全随机数，并将其用于生成对应的密钥。
* 指定随机种子，生成一系列的随机序列。

在开发前，开发者应该先对加解密基础知识有一定了解，并熟知以下随机数相关的基本概念：

* **内部状态**

  代表随机数生成器内存中的数值，当内部状态相同时，随机数生成器会生成固定的随机数序列。
* **随机种子**

  一个用来对伪随机数的内部状态进行初始化的数据，随机数生成器通过种子来生成一系列的随机序列。

  当前OpenSSL实现方式，随机数生成器内部状态是不断变化的，即使设置相同的种子，生成的随机数序列也不会相同。

## 支持的算法与规格

随机数生成算法使用OpenSSL的RAND\_priv\_bytes接口生成安全随机数。

| 算法 | 长度（Byte） |
| --- | --- |
| CTR\_DRBG | [1, INT\_MAX] |

## 开发步骤

1. 调用[OH\_CryptoRand\_Create](../harmonyos-references/capi-crypto-rand-h.md#oh_cryptorand_create)，创建随机数生成器。
2. （可选）调用[OH\_CryptoRand\_SetSeed](../harmonyos-references/capi-crypto-rand-h.md#oh_cryptorand_setseed)，为随机数生成器设置种子。
3. 调用[OH\_CryptoRand\_GenerateRandom](../harmonyos-references/capi-crypto-rand-h.md#oh_cryptorand_generaterandom)，生成指定长度的安全随机数。指定字节长度范围为1~INT\_MAX。
4. 调用[OH\_CryptoRand\_GetAlgoName](../harmonyos-references/capi-crypto-rand-h.md#oh_cryptorand_getalgoname)，获取随机数生成器使用的算法名称。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"
2. #include <cstdio>
3. #include "file.h"

5. OH_Crypto_ErrCode doTestRandomNumber()
6. {
7. // 创建随机数生成器。
8. OH_CryptoRand *rand = nullptr;
9. OH_Crypto_ErrCode ret = OH_CryptoRand_Create(&rand);
10. if (ret != CRYPTO_SUCCESS) {
11. return ret;
12. }

14. // 设置随机种子（可选）。
15. uint8_t seedData[12] = {0x25, 0x65, 0x58, 0x89, 0x85, 0x55, 0x66, 0x77, 0x88, 0x99, 0x11, 0x22};
16. Crypto_DataBlob seed = {
17. .data = seedData,
18. .len = sizeof(seedData)
19. };
20. ret = OH_CryptoRand_SetSeed(rand, &seed);
21. if (ret != CRYPTO_SUCCESS) {
22. OH_CryptoRand_Destroy(rand);
23. return ret;
24. }

26. // 生成指定长度的随机数。
27. Crypto_DataBlob out = {0};
28. uint32_t randomLength = 24; // 生成24字节的随机数。
29. ret = OH_CryptoRand_GenerateRandom(rand, randomLength, &out);
30. if (ret != CRYPTO_SUCCESS) {
31. OH_CryptoRand_Destroy(rand);
32. return ret;
33. }

35. // 获取并打印随机数生成器的算法名称。
36. const char *algoName = OH_CryptoRand_GetAlgoName(rand);
37. if (algoName != nullptr) {
38. printf("Random number generator algorithm: %s\n", algoName);
39. }

41. printf("Generated random number length: %u\n", out.len);

43. // 清理资源。
44. OH_Crypto_FreeDataBlob(&out);
45. OH_CryptoRand_Destroy(rand);
46. return CRYPTO_SUCCESS;
47. }
```

[rand\_test.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/SecureRandomNumberGeneration/entry/src/main/cpp/types/project/rand_test.cpp#L16-L64)
