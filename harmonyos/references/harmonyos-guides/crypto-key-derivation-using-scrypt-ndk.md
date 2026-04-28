---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-scrypt-ndk
title: 使用SCRYPT进行密钥派生(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥派生 > 使用SCRYPT进行密钥派生(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b3c4bf0bc38726f017259fac25fc623bfeb49b7437b02a38c4aaea69987ee81a
---

对应的算法规格请查看[密钥派生算法规格：SCRYPT](crypto-key-derivation-overview.md#scrypt算法)。

## 开发步骤

1. 调用[OH\_CryptoKdfParams\_Create](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdfparams_create)，指定字符串参数'SCRYPT'，创建密钥派生参数对象。
2. 调用[OH\_CryptoKdfParams\_SetParam](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdfparams_setparam)，设置Scrypt所需的参数。

   密钥派生失败原因：下列参数未设置。

   * CRYPTO\_KDF\_KEY\_DATABLOB：用于生成派生密钥的原始密码。
   * CRYPTO\_KDF\_SALT\_DATABLOB：盐值。
   * CRYPTO\_KDF\_SCRYPT\_N\_UINT64：CPU/内存开销参数，必须是2的幂次方。
   * CRYPTO\_KDF\_SCRYPT\_R\_UINT64：块大小参数，影响并行度。
   * CRYPTO\_KDF\_SCRYPT\_P\_UINT64：并行化参数。
   * CRYPTO\_KDF\_SCRYPT\_MAX\_MEM\_UINT64：最大内存限制（字节）。
3. 调用[OH\_CryptoKdf\_Create](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdf_create)，指定字符串参数'SCRYPT'，创建密钥派生函数对象。
4. 调用[OH\_CryptoKdf\_Derive](../harmonyos-references/capi-crypto-kdf-h.md#oh_cryptokdf_derive)，指定目标密钥的字节长度，进行密钥派生。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"
2. #include "CryptoArchitectureKit/crypto_kdf.h"
3. #include <cstdio>
4. #include <cstring>
5. #include "file.h"

7. static OH_Crypto_ErrCode doSetSaltAndPassword(OH_CryptoKdfParams **params)
8. {
9. const char *password = "123456";
10. const char *salt = "saltstring";
11. Crypto_DataBlob saltBlob = {
12. .data = reinterpret_cast<uint8_t *>(const_cast<char *>(salt)),
13. .len = strlen(salt)
14. };
15. Crypto_DataBlob passwordBlob = {
16. .data = reinterpret_cast<uint8_t *>(const_cast<char *>(password)),
17. .len = strlen(password)
18. };
19. OH_Crypto_ErrCode ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_KEY_DATABLOB, &passwordBlob);
20. if (ret != CRYPTO_SUCCESS) {
21. return ret;
22. }

24. ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_SALT_DATABLOB, &saltBlob);
25. if (ret != CRYPTO_SUCCESS) {
26. return ret;
27. }
28. return CRYPTO_SUCCESS;
29. }

31. // 设置参数函数
32. static OH_Crypto_ErrCode doScryptSetParams(OH_CryptoKdfParams **params)
33. {
34. OH_Crypto_ErrCode ret = OH_CryptoKdfParams_Create("SCRYPT", params);
35. if (ret != CRYPTO_SUCCESS) {
36. return ret;
37. }

39. uint64_t n = 1024;  // CPU/内存开销参数。
40. uint64_t r = 8;     // 块大小参数。
41. uint64_t p = 16;    // 并行化参数。
42. uint64_t maxMem = 1067008;  // 最大内存限制（字节）。

44. Crypto_DataBlob nData = { .data = reinterpret_cast<uint8_t *>(&n), .len = sizeof(uint64_t) };
45. Crypto_DataBlob rData = { .data = reinterpret_cast<uint8_t *>(&r), .len = sizeof(uint64_t) };
46. Crypto_DataBlob pData = { .data = reinterpret_cast<uint8_t *>(&p), .len = sizeof(uint64_t) };
47. Crypto_DataBlob maxMemData = { .data = reinterpret_cast<uint8_t *>(&maxMem), .len = sizeof(uint64_t) };

49. ret = doSetSaltAndPassword(params);
50. if (ret != CRYPTO_SUCCESS) {
51. goto end;
52. }

54. ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_SCRYPT_N_UINT64, &nData);
55. if (ret != CRYPTO_SUCCESS) {
56. goto end;
57. }
58. ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_SCRYPT_R_UINT64, &rData);
59. if (ret != CRYPTO_SUCCESS) {
60. goto end;
61. }
62. ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_SCRYPT_P_UINT64, &pData);
63. if (ret != CRYPTO_SUCCESS) {
64. goto end;
65. }
66. ret = OH_CryptoKdfParams_SetParam(*params, CRYPTO_KDF_SCRYPT_MAX_MEM_UINT64, &maxMemData);
67. if (ret != CRYPTO_SUCCESS) {
68. goto end;
69. }
70. return ret;

72. end:
73. OH_CryptoKdfParams_Destroy(*params);
74. *params = nullptr;
75. return ret;
76. }

78. static OH_Crypto_ErrCode doScryptDerive(OH_CryptoKdfParams *params, uint32_t keyLength, Crypto_DataBlob *out)
79. {
80. // 创建密钥派生函数对象。
81. OH_CryptoKdf *kdfCtx = nullptr;
82. OH_Crypto_ErrCode ret = OH_CryptoKdf_Create("SCRYPT", &kdfCtx);
83. if (ret != CRYPTO_SUCCESS) {
84. return ret;
85. }

87. // 派生密钥。
88. ret = OH_CryptoKdf_Derive(kdfCtx, params, keyLength, out);
89. if (ret != CRYPTO_SUCCESS) {
90. OH_CryptoKdf_Destroy(kdfCtx);
91. return ret;
92. }

94. printf("Derived key length: %u\n", out->len);

96. OH_CryptoKdf_Destroy(kdfCtx);
97. return ret;
98. }

100. OH_Crypto_ErrCode doTestScrypt()
101. {
102. OH_CryptoKdfParams *params = nullptr;
103. Crypto_DataBlob out = {0};
104. uint32_t keyLength = 32; // 生成32字节的密钥。

106. // 设置参数。
107. OH_Crypto_ErrCode ret = doScryptSetParams(&params);
108. if (ret != CRYPTO_SUCCESS) {
109. return ret;
110. }

112. // 派生密钥。
113. ret = doScryptDerive(params, keyLength, &out);
114. if (ret != CRYPTO_SUCCESS) {
115. OH_CryptoKdfParams_Destroy(params);
116. return ret;
117. }

119. // 清理资源。
120. OH_Crypto_FreeDataBlob(&out);
121. OH_CryptoKdfParams_Destroy(params);
122. return CRYPTO_SUCCESS;
123. }
```

[scrypt\_test.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyDerivation/SCRYPTDerivation/entry/src/main/cpp/types/project/scrypt_test.cpp#L16-L140)
