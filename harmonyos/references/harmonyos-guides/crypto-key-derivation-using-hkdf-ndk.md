---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-hkdf-ndk
title: 使用HKDF进行密钥派生(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥派生 > 使用HKDF进行密钥派生(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:59cdc2e892a236bb95f9116123d1103d9ca0e8d3bbfeb1e098fc8f45731b3b63
---

对应算法规格请查看[密钥派生算法规格：HKDF](crypto-key-derivation-overview.md#hkdf算法)。

## 开发步骤

1. 调用[OH\_CryptoKdfParams\_Create](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdfparams_create)，指定字符串参数'HKDF'，创建密钥派生参数对象。
2. 调用[OH\_CryptoKdfParams\_SetParam](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdfparams_setparam)，设置HKDF所需的参数。示例如下：

   * CRYPTO\_KDF\_KEY\_DATABLOB：用于生成派生密钥的原始密钥材料。
   * CRYPTO\_KDF\_SALT\_DATABLOB：盐值。
   * CRYPTO\_KDF\_INFO\_DATABLOB：应用程序特定的信息（可选）。
3. 调用[OH\_CryptoKdf\_Create](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdf_create)，指定字符串参数'HKDF|SHA256|EXTRACT\_AND\_EXPAND'，创建密钥派生函数对象。
4. 调用[OH\_CryptoKdf\_Derive](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdf_derive)，指定目标密钥的字节长度，进行密钥派生。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"
2. #include <cstdio>
3. #include <cstring>
4. #include "file.h"

6. static OH_Crypto_ErrCode setParams(OH_CryptoKdfParams **params)
7. {
8. const char *keyData = "012345678901234567890123456789";
9. Crypto_DataBlob key = {
10. .data = reinterpret_cast<uint8_t *>(const_cast<char *>(keyData)),
11. .len = strlen(keyData)
12. };
13. OH_Crypto_ErrCode ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_KEY_DATABLOB, &key);
14. if (ret != CRYPTO_SUCCESS) {
15. goto end;
16. }

18. // 设置盐值。
19. const char *saltData = "saltstring";
20. Crypto_DataBlob salt = {
21. .data = reinterpret_cast<uint8_t *>(const_cast<char *>(saltData)),
22. .len = strlen(saltData)
23. };
24. ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_SALT_DATABLOB, &salt);
25. if (ret != CRYPTO_SUCCESS) {
26. goto end;
27. }

29. // 设置应用程序特定信息（可选）。
30. const char *infoData = "infostring";
31. Crypto_DataBlob info = {
32. .data = reinterpret_cast<uint8_t *>(const_cast<char *>(infoData)),
33. .len = strlen(infoData)
34. };
35. ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_INFO_DATABLOB, &info);
36. if (ret != CRYPTO_SUCCESS) {
37. goto end;
38. }
39. end:
40. OH_CryptoKdfParams_Destroy(*params);
41. *params = nullptr;
42. return ret;
43. }

45. OH_Crypto_ErrCode doTestHkdf()
46. {
47. // 创建HKDF参数对象。
48. OH_CryptoKdfParams *params = nullptr;
49. OH_Crypto_ErrCode ret = OH_CryptoKdfParams_Create("HKDF", &params);
50. if (ret != CRYPTO_SUCCESS) {
51. return ret;
52. }

54. ret = setParams(&params);
55. if (ret != CRYPTO_SUCCESS) {
56. return ret;
57. }

59. // 创建密钥派生函数对象。
60. OH_CryptoKdf *kdfCtx = nullptr;
61. ret = OH_CryptoKdf_Create("HKDF|SHA256|EXTRACT_AND_EXPAND", &kdfCtx);
62. if (ret != CRYPTO_SUCCESS) {
63. OH_CryptoKdfParams_Destroy(params);
64. return ret;
65. }

67. // 派生密钥。
68. Crypto_DataBlob out = {0};
69. uint32_t keyLength = 32; // 生成32字节的密钥。
70. ret = OH_CryptoKdf_Derive(kdfCtx, params, keyLength, &out);
71. if (ret != CRYPTO_SUCCESS) {
72. OH_CryptoKdf_Destroy(kdfCtx);
73. OH_CryptoKdfParams_Destroy(params);
74. return ret;
75. }

77. printf("Derived key length: %u\n", out.len);

79. // 清理资源。
80. OH_Crypto_FreeDataBlob(&out);
81. OH_CryptoKdf_Destroy(kdfCtx);
82. OH_CryptoKdfParams_Destroy(params);
83. return CRYPTO_SUCCESS;
84. }
```

[hkdf\_test.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyDerivation/HKDFDerivation/entry/src/main/cpp/types/project/hkdf_test.cpp#L16-L101)
