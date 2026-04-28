---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-pbkdf2-ndk
title: 使用PBKDF2进行密钥派生(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥派生 > 使用PBKDF2进行密钥派生(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:41404d03ab9ab555d734c8984451ed4bd1156d541697712f34ded58546b75eea
---

对应的算法规格请查看[密钥派生算法规格：PBKDF2](crypto-key-derivation-overview.md#pbkdf2算法)。

## 开发步骤

1. 调用[OH\_CryptoKdfParams\_Create](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdfparams_create)，指定字符串参数'PBKDF2'，创建密钥派生参数对象。
2. 调用[OH\_CryptoKdfParams\_SetParam](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdfparams_setparam)，设置PBKDF2所需的参数。示例如下：

   * CRYPTO\_KDF\_KEY\_DATABLOB：用于生成派生密钥的原始密码。
   * CRYPTO\_KDF\_SALT\_DATABLOB：盐值。
   * CRYPTO\_KDF\_ITER\_COUNT\_INT：重复运算的次数，需要为正整数。
3. 调用[OH\_CryptoKdf\_Create](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdf_create)，指定字符串参数'PBKDF2|SHA256'，创建密钥派生函数对象。
4. 调用[OH\_CryptoKdf\_Derive](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdf_derive)，指定目标密钥的字节长度，进行密钥派生。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"
2. #include <cstdio>
3. #include <cstring>
4. #include "file.h"

6. static OH_Crypto_ErrCode setParams(OH_CryptoKdfParams **params)
7. {
8. // 设置密码。
9. const char *password = "123456";
10. Crypto_DataBlob passwordBlob = {
11. .data = reinterpret_cast<uint8_t *>(const_cast<char *>(password)),
12. .len = strlen(password)
13. };
14. OH_Crypto_ErrCode ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_KEY_DATABLOB, &passwordBlob);
15. if (ret != CRYPTO_SUCCESS) {
16. goto end;
17. }

19. // 设置盐值。
20. const char *salt = "saltstring";
21. Crypto_DataBlob saltBlob = {
22. .data = reinterpret_cast<uint8_t *>(const_cast<char *>(salt)),
23. .len = strlen(salt)
24. };
25. ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_SALT_DATABLOB, &saltBlob);
26. if (ret != CRYPTO_SUCCESS) {
27. goto end;
28. }

30. // 设置迭代次数。
31. int iterations = 10000;
32. Crypto_DataBlob iterationsBlob = {
33. .data = reinterpret_cast<uint8_t *>(&iterations),
34. .len = sizeof(int)
35. };
36. ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_ITER_COUNT_INT, &iterationsBlob);
37. if (ret != CRYPTO_SUCCESS) {
38. goto end;
39. }
40. end:
41. OH_CryptoKdfParams_Destroy(*params);
42. *params = nullptr;
43. return ret;
44. }

46. OH_Crypto_ErrCode doTestPbkdf2()
47. {
48. // 创建PBKDF2参数对象。
49. OH_CryptoKdfParams *params = nullptr;
50. OH_Crypto_ErrCode ret = OH_CryptoKdfParams_Create("PBKDF2", &params);
51. if (ret != CRYPTO_SUCCESS) {
52. return ret;
53. }

55. ret = setParams(&params);
56. if (ret != CRYPTO_SUCCESS) {
57. return ret;
58. }

60. // 创建密钥派生函数对象。
61. OH_CryptoKdf *kdfCtx = nullptr;
62. ret = OH_CryptoKdf_Create("PBKDF2|SHA256", &kdfCtx);
63. if (ret != CRYPTO_SUCCESS) {
64. OH_CryptoKdfParams_Destroy(params);
65. return ret;
66. }

68. // 派生密钥。
69. Crypto_DataBlob out = {0};
70. uint32_t keyLength = 32; // 生成32字节的密钥。
71. ret = OH_CryptoKdf_Derive(kdfCtx, params, keyLength, &out);
72. if (ret != CRYPTO_SUCCESS) {
73. OH_CryptoKdf_Destroy(kdfCtx);
74. OH_CryptoKdfParams_Destroy(params);
75. return ret;
76. }

78. printf("Derived key length: %u\n", out.len);

80. // 清理资源。
81. OH_Crypto_FreeDataBlob(&out);
82. OH_CryptoKdf_Destroy(kdfCtx);
83. OH_CryptoKdfParams_Destroy(params);
84. return CRYPTO_SUCCESS;
85. }
```

[pbkdf2\_test.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyDerivation/PBKDF2Derivation/entry/src/main/cpp/types/project/pbkdf2_test.cpp#L16-L102)
