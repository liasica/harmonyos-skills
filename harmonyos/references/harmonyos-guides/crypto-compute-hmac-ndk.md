---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-hmac-ndk
title: 消息认证码计算HMAC(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 消息认证码 > 消息认证码计算HMAC(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d422b5303a4e5631404dc361142e51801aa02065196e0e28b1ebf14e98e06266
---

HMAC通过指定摘要算法，以通信双方共享密钥与消息作为输入，生成消息认证码用于检验传递报文的完整性。HMAC在消息摘要算法的基础上增加了密钥的输入，确保了信息的正确性。生成的消息认证码为固定长度。

## 开发步骤

在调用update接口传入数据时，可以[一次性传入](crypto-compute-hmac-ndk.md#hmac一次性传入)，也可以把数据人工[分段传入](crypto-compute-hmac-ndk.md#hmac分段传入)。对于同一段数据而言，是否分段，计算结果没有差异。对于数据量较大的数据，开发者可以根据实际需求选择是否分段传入。

下面分别提供两种方式的示例代码。

### HMAC（一次性传入）

1. 调用[OH\_CryptoSymKeyGenerator\_Create](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_create)、[OH\_CryptoSymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_generate)生成密钥算法为HMAC的对称密钥（symKey）。
2. 调用[OH\_CryptoMac\_Create](../harmonyos-references/capi-crypto-mac-h.md#oh_cryptomac_create)，指定字符串参数'HMAC'，创建MAC算法为HMAC的MAC生成器。
3. 调用[OH\_CryptoMac\_SetParam](../harmonyos-references/capi-crypto-mac-h.md#oh_cryptomac_setparam)，指定参数CRYPTO\_MAC\_DIGEST\_NAME\_STR，设置摘要算法名称。
4. 调用[OH\_CryptoMac\_Init](../harmonyos-references/capi-crypto-mac-h.md#oh_cryptomac_init)，指定共享对称密钥（symKey），初始化MAC对象。
5. 调用[OH\_CryptoMac\_Update](../harmonyos-references/capi-crypto-mac-h.md#oh_cryptomac_update)，传入自定义消息，进行消息认证码计算。
6. 调用[OH\_CryptoMac\_Final](../harmonyos-references/capi-crypto-mac-h.md#oh_cryptomac_final)，获取MAC计算结果。
7. 调用[OH\_CryptoMac\_GetLength](../harmonyos-references/capi-crypto-mac-h.md#oh_cryptomac_getlength)，获取MAC消息认证码的长度，单位为字节。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"
2. #include <cstdio>
3. #include <cstring>

5. static OH_CryptoSymKey *GenerateHmacKey(const char *algoName)
6. {
7. OH_CryptoSymKeyGenerator *keyGen = nullptr;
8. OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create(algoName, &keyGen);
9. if (ret != CRYPTO_SUCCESS) {
10. return nullptr;
11. }
12. OH_CryptoSymKey *keyCtx = nullptr;
13. ret = OH_CryptoSymKeyGenerator_Generate(keyGen, &keyCtx);
14. OH_CryptoSymKeyGenerator_Destroy(keyGen);
15. if (ret != CRYPTO_SUCCESS) {
16. return nullptr;
17. }
18. return keyCtx;
19. }

21. static OH_Crypto_ErrCode CreateHmacContext(OH_CryptoSymKey *keyCtx, OH_CryptoMac **ctx)
22. {
23. OH_Crypto_ErrCode ret = OH_CryptoMac_Create("HMAC", ctx);
24. if (ret != CRYPTO_SUCCESS) {
25. return ret;
26. }

28. // 设置摘要算法名称为SM3。
29. const char *digestName = "SM3";
30. Crypto_DataBlob digestNameData = {
31. .data = reinterpret_cast<uint8_t *>(const_cast<char *>(digestName)),
32. .len = strlen(digestName)
33. };
34. ret = OH_CryptoMac_SetParam(*ctx, CRYPTO_MAC_DIGEST_NAME_STR, &digestNameData);
35. if (ret != CRYPTO_SUCCESS) {
36. OH_CryptoMac_Destroy(*ctx);
37. return ret;
38. }

40. // 初始化HMAC计算。
41. ret = OH_CryptoMac_Init(*ctx, keyCtx);
42. if (ret != CRYPTO_SUCCESS) {
43. OH_CryptoMac_Destroy(*ctx);
44. return ret;
45. }

47. return CRYPTO_SUCCESS;
48. }

50. static OH_Crypto_ErrCode UpdateHmacData(OH_CryptoMac *ctx)
51. {
52. // 一次性传入所有数据。
53. const char *message = "hmacTestMessage";
54. Crypto_DataBlob input = {
55. .data = reinterpret_cast<uint8_t *>(const_cast<char *>(message)),
56. .len = strlen(message)
57. };
58. OH_Crypto_ErrCode ret = OH_CryptoMac_Update(ctx, &input);
59. if (ret != CRYPTO_SUCCESS) {
60. return ret;
61. }

63. return CRYPTO_SUCCESS;
64. }

66. static OH_Crypto_ErrCode FinalizeHmac(OH_CryptoMac *ctx, Crypto_DataBlob *out, uint32_t *macLen)
67. {
68. // 完成HMAC计算并获取结果。
69. OH_Crypto_ErrCode ret = OH_CryptoMac_Final(ctx, out);
70. if (ret != CRYPTO_SUCCESS) {
71. return ret;
72. }

74. // 获取HMAC值的长度。
75. ret = OH_CryptoMac_GetLength(ctx, macLen);
76. if (ret != CRYPTO_SUCCESS) {
77. OH_Crypto_FreeDataBlob(out);
78. return ret;
79. }

81. return CRYPTO_SUCCESS;
82. }

84. OH_Crypto_ErrCode doTestHmacOnce()
85. {
86. OH_CryptoSymKey *keyCtx = nullptr;
87. OH_CryptoMac *ctx = nullptr;
88. Crypto_DataBlob out = {0};
89. OH_Crypto_ErrCode ret = CRYPTO_SUCCESS;
90. uint32_t macLen = 0;

92. // 生成HMAC密钥，使用SM3作为摘要算法。
93. keyCtx = GenerateHmacKey("HMAC|SM3");
94. if (keyCtx == nullptr) {
95. ret = CRYPTO_OPERTION_ERROR;
96. goto cleanup;
97. }

99. // 创建HMAC上下文。
100. ret = CreateHmacContext(keyCtx, &ctx);
101. if (ret != CRYPTO_SUCCESS) {
102. goto cleanup;
103. }

105. // 一次性传入所有数据。
106. ret = UpdateHmacData(ctx);
107. if (ret != CRYPTO_SUCCESS) {
108. goto cleanup;
109. }

111. // 完成HMAC计算。
112. ret = FinalizeHmac(ctx, &out, &macLen);
113. if (ret != CRYPTO_SUCCESS) {
114. goto cleanup;
115. }

117. printf("HMAC calculation success, length: %u\n", macLen);

119. cleanup:
120. // 清理资源。
121. OH_Crypto_FreeDataBlob(&out);
122. OH_CryptoMac_Destroy(ctx);
123. OH_CryptoSymKey_Destroy(keyCtx);
124. return ret;
125. }
```

[singleTime.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/MessageAuthenticationCode/entry/src/main/cpp/types/project/hmac/singleTime.cpp#L16-L144)

### HMAC（分段传入）

与一次性传入的步骤基本相同，区别在于多次调用[OH\_CryptoMac\_Update](../harmonyos-references/capi-crypto-mac-h.md#oh_cryptomac_update)来处理分段数据。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"
2. #include <cstdio>
3. #include <cstring>

5. static OH_CryptoSymKey *GenerateHmacKey(const char *algoName)
6. {
7. OH_CryptoSymKeyGenerator *keyGen = nullptr;
8. OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create(algoName, &keyGen);
9. if (ret != CRYPTO_SUCCESS) {
10. return nullptr;
11. }
12. OH_CryptoSymKey *keyCtx = nullptr;
13. ret = OH_CryptoSymKeyGenerator_Generate(keyGen, &keyCtx);
14. OH_CryptoSymKeyGenerator_Destroy(keyGen);
15. if (ret != CRYPTO_SUCCESS) {
16. return nullptr;
17. }
18. return keyCtx;
19. }

21. static OH_Crypto_ErrCode CreateHmacContext(OH_CryptoSymKey *keyCtx, OH_CryptoMac **ctx)
22. {
23. OH_Crypto_ErrCode ret = OH_CryptoMac_Create("HMAC", ctx);
24. if (ret != CRYPTO_SUCCESS) {
25. return ret;
26. }

28. // 设置摘要算法名称为SM3。
29. const char *digestName = "SM3";
30. Crypto_DataBlob digestNameData = {
31. .data = reinterpret_cast<uint8_t *>(const_cast<char *>(digestName)),
32. .len = strlen(digestName)
33. };
34. ret = OH_CryptoMac_SetParam(*ctx, CRYPTO_MAC_DIGEST_NAME_STR, &digestNameData);
35. if (ret != CRYPTO_SUCCESS) {
36. OH_CryptoMac_Destroy(*ctx);
37. return ret;
38. }

40. // 初始化HMAC计算。
41. ret = OH_CryptoMac_Init(*ctx, keyCtx);
42. if (ret != CRYPTO_SUCCESS) {
43. OH_CryptoMac_Destroy(*ctx);
44. return ret;
45. }

47. return CRYPTO_SUCCESS;
48. }

50. static OH_Crypto_ErrCode ProcessHmacSegments(OH_CryptoMac *ctx)
51. {
52. // 分段传入数据。
53. const char *message = "aaaaa.....bbbbb.....ccccc.....ddddd.....eee";
54. size_t messageLen = strlen(message);
55. size_t segmentSize = 20; // 每段20字节。

57. for (size_t i = 0; i < messageLen; i += segmentSize) {
58. size_t currentSize = (i + segmentSize <= messageLen) ? segmentSize : (messageLen - i);
59. Crypto_DataBlob segment = {
60. .data = reinterpret_cast<uint8_t *>(const_cast<char *>(message + i)),
61. .len = currentSize
62. };
63. OH_Crypto_ErrCode ret = OH_CryptoMac_Update(ctx, &segment);
64. if (ret != CRYPTO_SUCCESS) {
65. return ret;
66. }
67. }

69. return CRYPTO_SUCCESS;
70. }

72. static OH_Crypto_ErrCode FinalizeHmac(OH_CryptoMac *ctx, Crypto_DataBlob *out, uint32_t *macLen)
73. {
74. // 完成HMAC计算并获取结果。
75. OH_Crypto_ErrCode ret = OH_CryptoMac_Final(ctx, out);
76. if (ret != CRYPTO_SUCCESS) {
77. return ret;
78. }

80. // 获取HMAC值的长度。
81. ret = OH_CryptoMac_GetLength(ctx, macLen);
82. if (ret != CRYPTO_SUCCESS) {
83. OH_Crypto_FreeDataBlob(out);
84. return ret;
85. }

87. return CRYPTO_SUCCESS;
88. }

90. OH_Crypto_ErrCode doTestHmacBySegments()
91. {
92. OH_CryptoSymKey *keyCtx = nullptr;
93. OH_CryptoMac *ctx = nullptr;
94. Crypto_DataBlob out = {0};
95. OH_Crypto_ErrCode ret = CRYPTO_SUCCESS;
96. uint32_t macLen = 0;

98. // 生成HMAC密钥，使用SM3作为摘要算法。
99. keyCtx = GenerateHmacKey("HMAC|SM3");
100. if (keyCtx == nullptr) {
101. ret = CRYPTO_OPERTION_ERROR;
102. goto cleanup;
103. }

105. // 创建HMAC上下文。
106. ret = CreateHmacContext(keyCtx, &ctx);
107. if (ret != CRYPTO_SUCCESS) {
108. goto cleanup;
109. }

111. // 分段处理数据。
112. ret = ProcessHmacSegments(ctx);
113. if (ret != CRYPTO_SUCCESS) {
114. goto cleanup;
115. }

117. // 完成HMAC计算。
118. ret = FinalizeHmac(ctx, &out, &macLen);
119. if (ret != CRYPTO_SUCCESS) {
120. goto cleanup;
121. }

123. printf("HMAC calculation success, length: %u\n", macLen);

125. cleanup:
126. // 清理资源。
127. OH_Crypto_FreeDataBlob(&out);
128. OH_CryptoMac_Destroy(ctx);
129. OH_CryptoSymKey_Destroy(keyCtx);
130. return ret;
131. }
```

[segmentation.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/MessageAuthenticationCode/entry/src/main/cpp/types/project/hmac/segmentation.cpp#L16-L150)
