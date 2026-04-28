---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-encryption-decryption-ndk
title: 加解密(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 加密/解密 > 加解密(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dad83ad945bacf6a4531aab1e4c9c6dbb4dcbcf3758f36260f396e55e3a9f639
---

以AES256、RSA1024、SM2和DES64为例，完成加解密。具体的场景介绍及支持的算法规格，请参考[加解密支持的算法](huks-encryption-decryption-overview.md#支持的算法)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

## 开发步骤

**生成密钥**

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集。
3. 调用[OH\_Huks\_GenerateKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_generatekeyitem)生成密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md)，导入已有的密钥。

**加密**

1. 获取密钥别名。
2. 获取待加密的数据。
3. 调用[OH\_Huks\_InitParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_initparamset)指定算法参数配置。

   文档中提供多个示例，当使用不同算法时，请注意配置对应参数。

   * 使用AES算法加密，选取的分组模式为CBC、填充模式为PKCS7时，参数IV必选，请见开发案例：[AES/CBC/PKCS7](huks-encryption-decryption-ndk.md#aescbcpkcs7)。
   * 使用AES算法加密，选取的分组模式为GCM时，参数NONCE可选，AAD可选，请见开发案例：[AES/GCM/NoPadding](huks-encryption-decryption-ndk.md#aesgcmnopadding)。
   * 使用AES算法加密，选取的分组模式为CCM时，参数NONCE可选，AAD可选，请见开发案例：[AES/CCM/NoPadding](huks-encryption-decryption-ndk.md#aesccmnopadding)。
   * 使用RSA算法加密，需要选择相对应的分组模式、填充模式以及摘要算法DIGEST，请见开发案例：[RSA/ECB/PKCS1\_V1\_5](huks-encryption-decryption-ndk.md#rsaecbpkcs1_v1_5)和[RSA/ECB/OAEP/SHA256](huks-encryption-decryption-ndk.md#rsaecboaepsha256)。
   * 使用SM2算法加密，摘要算法DIGEST需要指定为SM3，请见开发案例：[SM2](huks-encryption-decryption-ndk.md#sm2)。

   详细规格请参考[加密/解密介绍及算法规格](huks-encryption-decryption-overview.md)。
4. 调用[OH\_Huks\_InitSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_initsession)初始化密钥会话，并获取会话的句柄handle。
5. 调用[OH\_Huks\_FinishSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_finishsession)结束密钥会话，获取加密后的密文。

**解密**

1. 获取密钥别名。
2. 获取待解密的密文。
3. 调用[OH\_Huks\_InitParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_initparamset)指定算法参数配置。

   文档中提供多个示例，当使用不同算法时，请注意配置对应参数。

   * 使用AES算法解密，用例中选取的分组模式为GCM时，必须要填参数NONCE和参数AEAD，AAD可选，请见开发案例：[AES/GCM/NoPadding](huks-encryption-decryption-ndk.md#aesgcmnopadding)。
   * 其余示例参数与加密要求一致。

   详细规格请参考[加密/解密介绍及算法规格](huks-encryption-decryption-overview.md)。
4. 调用[OH\_Huks\_InitSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_initsession)初始化密钥会话，并获取会话的句柄handle。
5. 调用[OH\_Huks\_FinishSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_finishsession)结束密钥会话，获取解密后的数据。

**删除密钥**

当密钥废弃不用时，需要调用OH\_Huks\_DeleteKeyItem删除密钥，具体请参考[密钥删除](huks-delete-key-ndk.md)。

## 开发案例

### AES/CBC/PKCS7

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <cstring>
5. #include "CryptoArchitectureKit/crypto_architecture_kit.h"

7. static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
8. uint32_t paramCount)
9. {
10. OH_Huks_Result ret = OH_Huks_InitParamSet(paramSet);
11. if (ret.errorCode != OH_HUKS_SUCCESS) {
12. return ret;
13. }
14. ret = OH_Huks_AddParams(*paramSet, params, paramCount);
15. if (ret.errorCode != OH_HUKS_SUCCESS) {
16. OH_Huks_FreeParamSet(paramSet);
17. return ret;
18. }
19. ret = OH_Huks_BuildParamSet(paramSet);
20. if (ret.errorCode != OH_HUKS_SUCCESS) {
21. OH_Huks_FreeParamSet(paramSet);
22. return ret;
23. }
24. return ret;
25. }

27. static OH_Crypto_ErrCode genRandomNumber(uint32_t randomLength, uint8_t *out)
28. {
29. // 创建随机数生成器。
30. OH_CryptoRand *rand = nullptr;
31. OH_Crypto_ErrCode ret = OH_CryptoRand_Create(&rand);
32. if (ret != CRYPTO_SUCCESS) {
33. return ret;
34. }
35. Crypto_DataBlob blob = {out, randomLength};
36. // 生成指定长度的随机数。
37. ret = OH_CryptoRand_GenerateRandom(rand, randomLength, &blob);
38. if (ret != CRYPTO_SUCCESS) {
39. OH_CryptoRand_Destroy(rand);
40. return ret;
41. }
42. OH_CryptoRand_Destroy(rand);

44. return CRYPTO_SUCCESS;
45. }

47. static const uint32_t IV_SIZE = 16;
48. static uint8_t IV[IV_SIZE] = {0};
49. static OH_Crypto_ErrCode ret = genRandomNumber(IV_SIZE, IV);
50. static struct OH_Huks_Param g_genEncDecParams[] = {
51. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
52. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT | OH_HUKS_KEY_PURPOSE_DECRYPT},
53. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
54. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
55. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_CBC}};

57. static struct OH_Huks_Param g_encryptParams[] = {
58. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
59. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT},
60. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
61. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
62. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_CBC},
63. {.tag = OH_HUKS_TAG_IV,
64. .blob = {
65. .size = IV_SIZE,
66. .data = (uint8_t *)IV
67. }}};

69. static struct OH_Huks_Param g_decryptParams[] = {
70. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
71. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_DECRYPT},
72. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
73. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
74. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_CBC},
75. {.tag = OH_HUKS_TAG_IV,
76. .blob = {
77. .size = IV_SIZE,
78. .data = (uint8_t *)IV
79. }}};

81. static const uint32_t AES_COMMON_SIZE = 1024;
82. OH_Huks_Result HksAesCipherTestEncrypt(const struct OH_Huks_Blob *keyAlias,
83. const struct OH_Huks_ParamSet *encryptParamSet,
84. const struct OH_Huks_Blob *inData, struct OH_Huks_Blob *cipherText)
85. {
86. uint8_t handleE[sizeof(uint64_t)] = {0};
87. struct OH_Huks_Blob handleEncrypt = {sizeof(uint64_t), handleE};
88. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, encryptParamSet, &handleEncrypt, nullptr);
89. if (ret.errorCode != OH_HUKS_SUCCESS) {
90. return ret;
91. }
92. ret = OH_Huks_FinishSession(&handleEncrypt, encryptParamSet, inData, cipherText);
93. return ret;
94. }

96. OH_Huks_Result HksAesCipherTestDecrypt(const struct OH_Huks_Blob *keyAlias,
97. const struct OH_Huks_ParamSet *decryptParamSet,
98. const struct OH_Huks_Blob *cipherText, struct OH_Huks_Blob *plainText,
99. const struct OH_Huks_Blob *inData)
100. {
101. uint8_t handleD[sizeof(uint64_t)] = {0};
102. struct OH_Huks_Blob handleDecrypt = {sizeof(uint64_t), handleD};
103. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, decryptParamSet, &handleDecrypt, nullptr);
104. if (ret.errorCode != OH_HUKS_SUCCESS) {
105. return ret;
106. }
107. ret = OH_Huks_FinishSession(&handleDecrypt, decryptParamSet, cipherText, plainText);
108. return ret;
109. }

111. napi_value TestAesCbc(napi_env env, napi_callback_info info)
112. {
113. char tmpKeyAlias[] = "test_enc_dec";
114. struct OH_Huks_Blob keyAlias = {(uint32_t)strlen(tmpKeyAlias), (uint8_t *)tmpKeyAlias};
115. struct OH_Huks_ParamSet *genParamSet = nullptr;
116. struct OH_Huks_ParamSet *encryptParamSet = nullptr;
117. struct OH_Huks_ParamSet *decryptParamSet = nullptr;
118. OH_Huks_Result ohResult;
119. do {
120. /* 1. 模拟生成密钥场景 */
121. /*
122. * 1.1. 获取生成密钥算法参数配置
123. */
124. ohResult = InitParamSet(&genParamSet, g_genEncDecParams, sizeof(g_genEncDecParams) / sizeof(OH_Huks_Param));
125. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
126. break;
127. }
128. /*
129. * 1.2. 调用generateKeyItem
130. */
131. ohResult = OH_Huks_GenerateKeyItem(&keyAlias, genParamSet, nullptr);
132. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
133. break;
134. }
135. /* 2. 模拟加密场景 */
136. /*
137. * 2.1. 获取加密算法参数配置
138. */
139. ohResult = InitParamSet(&encryptParamSet, g_encryptParams, sizeof(g_encryptParams) / sizeof(OH_Huks_Param));
140. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
141. break;
142. }
143. char tmpInData[] = "AES_ECB_INDATA_1";
144. struct OH_Huks_Blob inData = {(uint32_t)strlen(tmpInData), (uint8_t *)tmpInData};
145. uint8_t cipher[AES_COMMON_SIZE] = {0};
146. struct OH_Huks_Blob cipherText = {AES_COMMON_SIZE, cipher};
147. /*
148. * 2.2. 调用HksAesCipherTestEncrypt获取加密后的密文
149. */
150. ohResult = HksAesCipherTestEncrypt(&keyAlias, encryptParamSet, &inData, &cipherText);
151. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
152. break;
153. }
154. /* 3. 模拟解密场景 */
155. /*
156. * 3.1. 获取解密算法参数配置
157. */
158. ohResult = InitParamSet(&decryptParamSet, g_decryptParams, sizeof(g_decryptParams) / sizeof(OH_Huks_Param));
159. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
160. break;
161. }
162. uint8_t plain[AES_COMMON_SIZE] = {0};
163. struct OH_Huks_Blob plainText = {AES_COMMON_SIZE, plain};
164. /*
165. * 3.2. 调用HksAesCipherTestDecrypt获取解密后的数据
166. */
167. ohResult = HksAesCipherTestDecrypt(&keyAlias, decryptParamSet, &cipherText, &plainText, &inData);
168. } while (0);
169. /* 4. 模拟删除密钥场景 */
170. /*
171. * 4.1. 调用deleteKeyItem删除密钥
172. */
173. (void)OH_Huks_DeleteKeyItem(&keyAlias, genParamSet);

175. OH_Huks_FreeParamSet(&genParamSet);
176. OH_Huks_FreeParamSet(&encryptParamSet);
177. OH_Huks_FreeParamSet(&decryptParamSet);

179. napi_value ret;
180. napi_create_int32(env, ohResult.errorCode, &ret);
181. return ret;
182. }
```

[napi\_aescbcpkcs7.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/EncryptionDecryption/entry/src/main/cpp/types/projects/napi_aescbcpkcs7.cpp#L16-L199)

### AES/GCM/NoPadding

准备加解密密钥材料：

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <cstring>
5. #include "CryptoArchitectureKit/crypto_architecture_kit.h"

7. static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
8. uint32_t paramCount)
9. {
10. OH_Huks_Result ret = OH_Huks_InitParamSet(paramSet);
11. if (ret.errorCode != OH_HUKS_SUCCESS) {
12. return ret;
13. }
14. ret = OH_Huks_AddParams(*paramSet, params, paramCount);
15. if (ret.errorCode != OH_HUKS_SUCCESS) {
16. OH_Huks_FreeParamSet(paramSet);
17. return ret;
18. }
19. ret = OH_Huks_BuildParamSet(paramSet);
20. if (ret.errorCode != OH_HUKS_SUCCESS) {
21. OH_Huks_FreeParamSet(paramSet);
22. return ret;
23. }
24. return ret;
25. }

27. static OH_Crypto_ErrCode genRandomNumber(uint32_t randomLength, uint8_t *out)
28. {
29. // 创建随机数生成器。
30. OH_CryptoRand *rand = nullptr;
31. OH_Crypto_ErrCode ret = OH_CryptoRand_Create(&rand);
32. if (ret != CRYPTO_SUCCESS) {
33. return ret;
34. }
35. Crypto_DataBlob blob = {out, randomLength};
36. // 生成指定长度的随机数。
37. ret = OH_CryptoRand_GenerateRandom(rand, randomLength, &blob);
38. if (ret != CRYPTO_SUCCESS) {
39. OH_CryptoRand_Destroy(rand);
40. return ret;
41. }
42. OH_CryptoRand_Destroy(rand);

44. return CRYPTO_SUCCESS;
45. }

47. static const uint32_t NONCE_SIZE = 12;
48. static const uint32_t AAD_SIZE = 16;
49. static const uint32_t AE_TAG_SIZE = 16;
50. static char AEAD[AE_TAG_SIZE] = {0};
51. static char AAD[AAD_SIZE] = "cdcdcdcdcdcdcdc"; // this is a test value, for real use it should be different every time
52. static uint8_t NONCE[NONCE_SIZE] = {0};
53. static OH_Crypto_ErrCode ret = genRandomNumber(NONCE_SIZE, NONCE);
54. static struct OH_Huks_Param g_genEncDecParams[] = {
55. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
56. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT | OH_HUKS_KEY_PURPOSE_DECRYPT},
57. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
58. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
59. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_GCM}};

61. static struct OH_Huks_Param g_encryptParams[] = {
62. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
63. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT},
64. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
65. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
66. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_GCM},
67. {.tag = OH_HUKS_TAG_NONCE,
68. .blob = {
69. .size = NONCE_SIZE,
70. .data = (uint8_t *)NONCE // this is a test value, for real use the iv should be different every time
71. }},
72. {.tag = OH_HUKS_TAG_ASSOCIATED_DATA,
73. .blob = {
74. .size = AAD_SIZE,
75. .data = (uint8_t *)AAD // this is a test value, for real use the iv should be different every time
76. }}};

78. static struct OH_Huks_Param g_decryptParams[] = {
79. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
80. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_DECRYPT},
81. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
82. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
83. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_GCM},
84. {.tag = OH_HUKS_TAG_NONCE,
85. .blob = {
86. .size = NONCE_SIZE,
87. .data = (uint8_t *)NONCE // this is a test value, for real use the iv should be different every time
88. }},
89. {.tag = OH_HUKS_TAG_ASSOCIATED_DATA,
90. .blob = {
91. .size = AAD_SIZE,
92. .data = (uint8_t *)AAD // this is a test value, for real use the iv should be different every time
93. }},
94. {.tag = OH_HUKS_TAG_AE_TAG,
95. .blob = {
96. .size = AE_TAG_SIZE,
97. .data = (uint8_t *)AEAD // this is a test value, for real use the iv should be different every time
98. }}};

100. static const uint32_t AES_GCM_SIZE = 1024;
101. OH_Huks_Result HksAesGcmTestEncrypt(const struct OH_Huks_Blob *keyAlias,
102. const struct OH_Huks_ParamSet *encryptParamSet,
103. const struct OH_Huks_Blob *inData, struct OH_Huks_Blob *cipherText)
104. {
105. uint8_t handleE[sizeof(uint64_t)] = {0};
106. struct OH_Huks_Blob handleEncrypt = {sizeof(uint64_t), handleE};
107. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, encryptParamSet, &handleEncrypt, nullptr);
108. if (ret.errorCode != OH_HUKS_SUCCESS) {
109. return ret;
110. }
111. ret = OH_Huks_FinishSession(&handleEncrypt, encryptParamSet, inData, cipherText);
112. return ret;
113. }

115. OH_Huks_Result HksAesGcmTestDecrypt(const struct OH_Huks_Blob *keyAlias,
116. const struct OH_Huks_ParamSet *decryptParamSet,
117. const struct OH_Huks_Blob *cipherText, struct OH_Huks_Blob *plainText,
118. const struct OH_Huks_Blob *inData)
119. {
120. uint8_t handleD[sizeof(uint64_t)] = {0};
121. struct OH_Huks_Blob handleDecrypt = {sizeof(uint64_t), handleD};
122. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, decryptParamSet, &handleDecrypt, nullptr);
123. if (ret.errorCode != OH_HUKS_SUCCESS) {
124. return ret;
125. }
126. ret = OH_Huks_FinishSession(&handleDecrypt, decryptParamSet, cipherText, plainText);
127. return ret;
128. }
```

[napi\_aesgcmnopadding.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/EncryptionDecryption/entry/src/main/cpp/types/projects/napi_aesgcmnopadding.cpp#L16-L145)

执行加解密流程：

```
1. napi_value TestAesGcm(napi_env env, napi_callback_info info)
2. {
3. char tmpKeyAlias[] = "test_enc_dec";
4. struct OH_Huks_Blob keyAlias = {(uint32_t)strlen(tmpKeyAlias), (uint8_t *)tmpKeyAlias};
5. struct OH_Huks_ParamSet *genParamSet = nullptr;
6. struct OH_Huks_ParamSet *encryptParamSet = nullptr;
7. struct OH_Huks_ParamSet *decryptParamSet = nullptr;
8. OH_Huks_Result ohResult;
9. do {
10. /* 1. 模拟生成密钥场景 */
11. /*
12. * 1.1. 获取生成密钥算法参数配置
13. */
14. ohResult = InitParamSet(&genParamSet, g_genEncDecParams, sizeof(g_genEncDecParams) / sizeof(OH_Huks_Param));
15. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
16. break;
17. }
18. /*
19. * 1.2. 调用generateKeyItem
20. */
21. ohResult = OH_Huks_GenerateKeyItem(&keyAlias, genParamSet, nullptr);
22. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
23. break;
24. }
25. /* 2. 模拟加密场景 */
26. /*
27. * 2.1. 获取加密算法参数配置
28. */
29. ohResult = InitParamSet(&encryptParamSet, g_encryptParams, sizeof(g_encryptParams) / sizeof(OH_Huks_Param));
30. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
31. break;
32. }
33. char tmpInData[] = "AES_GCM_INDATA_1";
34. struct OH_Huks_Blob inData = {(uint32_t)strlen(tmpInData), (uint8_t *)tmpInData};
35. uint8_t cipher[AES_GCM_SIZE] = {0};
36. struct OH_Huks_Blob cipherText = {AES_GCM_SIZE, cipher};
37. /*
38. * 2.2. 调用HksAesGcmTestEncrypt获取加密后的密文
39. */
40. ohResult = HksAesGcmTestEncrypt(&keyAlias, encryptParamSet, &inData, &cipherText);
41. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
42. break;
43. }
44. /* 3. 模拟解密场景 */
45. /*
46. * 3.1. 获取解密算法参数配置
47. */
48. strncpy(AEAD, (char *)cipherText.data + strlen(tmpInData), AE_TAG_SIZE);
49. cipherText.data[strlen(tmpInData)] = '\0';
50. cipherText.size -= AE_TAG_SIZE;
51. ohResult = InitParamSet(&decryptParamSet, g_decryptParams, sizeof(g_decryptParams) / sizeof(OH_Huks_Param));
52. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
53. break;
54. }
55. /*
56. * 3.2. 调用HksAesGcmTestDecrypt获取解密后的数据
57. */
58. uint8_t plainBuffer[AES_GCM_SIZE] = {0};
59. struct OH_Huks_Blob plainText = {AES_GCM_SIZE, plainBuffer};
60. ohResult = HksAesGcmTestDecrypt(&keyAlias, decryptParamSet, &cipherText, &plainText, &inData);
61. } while (0);
62. /* 4. 模拟删除密钥场景 */
63. /*
64. * 4.1. 调用deleteKeyItem删除密钥
65. */
66. (void)OH_Huks_DeleteKeyItem(&keyAlias, genParamSet);

68. OH_Huks_FreeParamSet(&genParamSet);
69. OH_Huks_FreeParamSet(&encryptParamSet);
70. OH_Huks_FreeParamSet(&decryptParamSet);

72. napi_value ret;
73. napi_create_int32(env, ohResult.errorCode, &ret);
74. return ret;
75. }
```

[napi\_aesgcmnopadding.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/EncryptionDecryption/entry/src/main/cpp/types/projects/napi_aesgcmnopadding.cpp#L147-L223)

### AES/CCM/NoPadding

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <string.h>

6. static const uint32_t IV_SIZE = 16;
7. static const uint32_t AEAD_TAG_LEN = 14;
8. static char IV[IV_SIZE] = { 0 }; // this is a test value, for real use the iv should be different every time.
9. static char AEAD[AEAD_TAG_LEN] = { 0 };
10. static char NONCE[OH_HUKS_AE_NONCE_LEN] = { 0 };
11. static struct OH_Huks_Param g_genEncDecParams[] = {
12. {
13. .tag = OH_HUKS_TAG_ALGORITHM,
14. .uint32Param = OH_HUKS_ALG_AES
15. }, {
16. .tag = OH_HUKS_TAG_PURPOSE,
17. .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT | OH_HUKS_KEY_PURPOSE_DECRYPT
18. }, {
19. .tag = OH_HUKS_TAG_KEY_SIZE,
20. .uint32Param = OH_HUKS_AES_KEY_SIZE_256
21. }, {
22. .tag = OH_HUKS_TAG_PADDING,
23. .uint32Param = OH_HUKS_PADDING_NONE
24. }, {
25. .tag = OH_HUKS_TAG_BLOCK_MODE,
26. .uint32Param = OH_HUKS_MODE_CCM
27. }
28. };
29. static struct OH_Huks_Param g_encryptParams[] = {
30. {
31. .tag = OH_HUKS_TAG_ALGORITHM,
32. .uint32Param = OH_HUKS_ALG_AES
33. }, {
34. .tag = OH_HUKS_TAG_PURPOSE,
35. .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT
36. }, {
37. .tag = OH_HUKS_TAG_KEY_SIZE,
38. .uint32Param = OH_HUKS_AES_KEY_SIZE_256
39. }, {
40. .tag = OH_HUKS_TAG_PADDING,
41. .uint32Param = OH_HUKS_PADDING_NONE
42. }, {
43. .tag = OH_HUKS_TAG_BLOCK_MODE,
44. .uint32Param = OH_HUKS_MODE_CCM
45. }, {
46. .tag = OH_HUKS_TAG_IV,
47. .blob = {
48. .size = IV_SIZE,
49. .data = (uint8_t *)IV // this is a test value, for real use the iv should be different every time.
50. }
51. }, {
52. .tag = OH_HUKS_TAG_NONCE,
53. .blob = {
54. .size = OH_HUKS_AE_NONCE_LEN,
55. .data = (uint8_t *)NONCE
56. }
57. }, {
58. .tag = OH_HUKS_TAG_AE_TAG_LEN,
59. .uint32Param = AEAD_TAG_LEN
60. }
61. };
62. static struct OH_Huks_Param g_decryptParams[] = {
63. {
64. .tag = OH_HUKS_TAG_ALGORITHM,
65. .uint32Param = OH_HUKS_ALG_AES
66. }, {
67. .tag = OH_HUKS_TAG_PURPOSE,
68. .uint32Param = OH_HUKS_KEY_PURPOSE_DECRYPT
69. }, {
70. .tag = OH_HUKS_TAG_KEY_SIZE,
71. .uint32Param = OH_HUKS_AES_KEY_SIZE_256
72. }, {
73. .tag = OH_HUKS_TAG_PADDING,
74. .uint32Param = OH_HUKS_PADDING_NONE
75. }, {
76. .tag = OH_HUKS_TAG_BLOCK_MODE,
77. .uint32Param = OH_HUKS_MODE_CCM
78. }, {
79. .tag = OH_HUKS_TAG_IV,
80. .blob = {
81. .size = IV_SIZE,
82. .data = (uint8_t *)IV // this is a test value, for real use the iv should be different every time.
83. }
84. }, {
85. .tag = OH_HUKS_TAG_NONCE,
86. .blob = {
87. .size = OH_HUKS_AE_NONCE_LEN,
88. .data = (uint8_t *)NONCE
89. }
90. }, {
91. .tag = OH_HUKS_TAG_AE_TAG,
92. .blob = {
93. .size = AEAD_TAG_LEN,
94. .data = (uint8_t *)AEAD
95. }
96. }, {
97. .tag = OH_HUKS_TAG_AE_TAG_LEN,
98. .uint32Param = AEAD_TAG_LEN
99. }
100. };
101. static const uint32_t AES_COMMON_SIZE = 1024;

103. OH_Huks_Result InitParamSet(
104. struct OH_Huks_ParamSet **paramSet,
105. const struct OH_Huks_Param *params,
106. uint32_t paramCount)
107. {
108. OH_Huks_Result ret = OH_Huks_InitParamSet(paramSet);
109. if (ret.errorCode != OH_HUKS_SUCCESS) {
110. return ret;
111. }
112. ret = OH_Huks_AddParams(*paramSet, params, paramCount);
113. if (ret.errorCode != OH_HUKS_SUCCESS) {
114. OH_Huks_FreeParamSet(paramSet);
115. return ret;
116. }
117. ret = OH_Huks_BuildParamSet(paramSet);
118. if (ret.errorCode != OH_HUKS_SUCCESS) {
119. OH_Huks_FreeParamSet(paramSet);
120. return ret;
121. }
122. return ret;
123. }

125. OH_Huks_Result HksAesCipherTestEncrypt(
126. const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *encryptParamSet,
127. const struct OH_Huks_Blob *inData, struct OH_Huks_Blob *cipherText)
128. {
129. uint8_t handleE[sizeof(uint64_t)] = {0};
130. struct OH_Huks_Blob handleEncrypt = {sizeof(uint64_t), handleE};
131. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, encryptParamSet, &handleEncrypt, nullptr);
132. if (ret.errorCode != OH_HUKS_SUCCESS) {
133. return ret;
134. }
135. ret = OH_Huks_FinishSession(&handleEncrypt, encryptParamSet, inData, cipherText);
136. return ret;
137. }

139. OH_Huks_Result HksAesCipherTestDecrypt(const struct OH_Huks_Blob *keyAlias,
140. const struct OH_Huks_ParamSet *decryptParamSet, const struct OH_Huks_Blob *cipherText,
141. struct OH_Huks_Blob *plainText)
142. {
143. uint8_t handleD[sizeof(uint64_t)] = {0};
144. struct OH_Huks_Blob handleDecrypt = {sizeof(uint64_t), handleD};
145. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, decryptParamSet, &handleDecrypt, nullptr);
146. if (ret.errorCode != OH_HUKS_SUCCESS) {
147. return ret;
148. }
149. ret = OH_Huks_FinishSession(&handleDecrypt, decryptParamSet, cipherText, plainText);
150. return ret;
151. }

153. static napi_value EncDecKey(napi_env env, napi_callback_info info)
154. {
155. char tmpKeyAlias[] = "test_aes_ccm_enc_dec";
156. struct OH_Huks_Blob keyAlias = { (uint32_t)strlen(tmpKeyAlias), (uint8_t *)tmpKeyAlias };
157. struct OH_Huks_ParamSet *genParamSet = nullptr;
158. struct OH_Huks_ParamSet *encryptParamSet = nullptr;
159. struct OH_Huks_ParamSet *decryptParamSet = nullptr;
160. OH_Huks_Result ohResult;
161. do {
162. /* 1. Generate Key */
163. /*
164. * 模拟生成密钥场景
165. * 1.1. 确定密钥别名
166. */
167. /*
168. * 1.2. 获取生成密钥算法参数配置
169. */
170. ohResult = InitParamSet(&genParamSet, g_genEncDecParams, sizeof(g_genEncDecParams) / sizeof(OH_Huks_Param));
171. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
172. break;
173. }
174. /*
175. * 1.3. 调用generateKeyItem
176. */
177. ohResult = OH_Huks_GenerateKeyItem(&keyAlias, genParamSet, nullptr);
178. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
179. break;
180. }
181. /* 2. Encrypt */
182. /*
183. * 模拟加密场景
184. * 2.1. 获取密钥别名
185. */
186. /*
187. * 2.2. 获取待加密的数据
188. */
189. /*
190. * 2.3. 获取加密算法参数配置
191. */
192. ohResult = InitParamSet(&encryptParamSet, g_encryptParams, sizeof(g_encryptParams) / sizeof(OH_Huks_Param));
193. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
194. break;
195. }
196. char tmpInData[] = "AES_CCM_INDATA_1";
197. uint32_t dataLen = (uint32_t)strlen(tmpInData);
198. struct OH_Huks_Blob inData = { dataLen, (uint8_t *)tmpInData };
199. uint8_t cipher[AES_COMMON_SIZE] = {0};
200. struct OH_Huks_Blob cipherText = {AES_COMMON_SIZE, cipher};
201. /*
202. * 2.4. 调用initSession获取handle
203. */
204. /*
205. * 2.5. 调用finishSession获取加密后的密文
206. */
207. ohResult = HksAesCipherTestEncrypt(&keyAlias, encryptParamSet, &inData, &cipherText);
208. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
209. break;
210. }
211. strncpy(AEAD, (char *)cipherText.data + dataLen, AEAD_TAG_LEN);
212. cipherText.data[dataLen] = '\0';
213. cipherText.size -= AEAD_TAG_LEN;
214. /* 3. Decrypt */
215. /*
216. * 模拟解密场景
217. * 3.1. 获取密钥别名
218. */
219. /*
220. * 3.2. 获取待解密的密文
221. */
222. /*
223. * 3.3. 获取解密算法参数配置
224. */
225. ohResult = InitParamSet(&decryptParamSet, g_decryptParams, sizeof(g_decryptParams) / sizeof(OH_Huks_Param));
226. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
227. break;
228. }
229. uint8_t plain[AES_COMMON_SIZE] = {0};
230. struct OH_Huks_Blob plainText = {AES_COMMON_SIZE, plain};
231. /*
232. * 3.4. 调用initSession获取handle
233. */
234. /*
235. * 3.5. 调用finishSession获取解密后的数据
236. */
237. ohResult = HksAesCipherTestDecrypt(&keyAlias, decryptParamSet, &cipherText, &plainText);
238. } while (0);
239. /* 4. Delete Key */
240. /*
241. * 模拟删除密钥场景
242. * 4.1. 获取密钥别名
243. */
244. /*
245. * 4.2. 调用deleteKeyItem删除密钥
246. */
247. (void)OH_Huks_DeleteKeyItem(&keyAlias, genParamSet);

249. OH_Huks_FreeParamSet(&genParamSet);
250. OH_Huks_FreeParamSet(&encryptParamSet);
251. OH_Huks_FreeParamSet(&decryptParamSet);

253. napi_value ret;
254. napi_create_int32(env, ohResult.errorCode, &ret);
255. return ret;
256. }
```

### RSA/ECB/PKCS1\_V1\_5

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <cstring>

6. static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
7. uint32_t paramCount)
8. {
9. OH_Huks_Result ret = OH_Huks_InitParamSet(paramSet);
10. if (ret.errorCode != OH_HUKS_SUCCESS) {
11. return ret;
12. }
13. ret = OH_Huks_AddParams(*paramSet, params, paramCount);
14. if (ret.errorCode != OH_HUKS_SUCCESS) {
15. OH_Huks_FreeParamSet(paramSet);
16. return ret;
17. }
18. ret = OH_Huks_BuildParamSet(paramSet);
19. if (ret.errorCode != OH_HUKS_SUCCESS) {
20. OH_Huks_FreeParamSet(paramSet);
21. return ret;
22. }
23. return ret;
24. }

26. static struct OH_Huks_Param g_genEncDecParams[] = {
27. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_RSA},
28. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT | OH_HUKS_KEY_PURPOSE_DECRYPT},
29. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_RSA_KEY_SIZE_1024},
30. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
31. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_PKCS1_V1_5},
32. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};

34. static struct OH_Huks_Param g_encryptParams[] = {
35. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_RSA},
36. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT},
37. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_RSA_KEY_SIZE_1024},
38. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_PKCS1_V1_5},
39. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
40. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};

42. static struct OH_Huks_Param g_decryptParams[] = {
43. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_RSA},
44. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_DECRYPT},
45. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_RSA_KEY_SIZE_1024},
46. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_PKCS1_V1_5},
47. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
48. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};

50. static const uint32_t RSA_COMMON_SIZE = 1024;
51. OH_Huks_Result HksRsaPkcsTestEncrypt(const struct OH_Huks_Blob *keyAlias,
52. const struct OH_Huks_ParamSet *encryptParamSet,
53. const struct OH_Huks_Blob *inData, struct OH_Huks_Blob *cipherText)
54. {
55. uint8_t handleE[sizeof(uint64_t)] = {0};
56. struct OH_Huks_Blob handleEncrypt = {sizeof(uint64_t), handleE};
57. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, encryptParamSet, &handleEncrypt, nullptr);
58. if (ret.errorCode != OH_HUKS_SUCCESS) {
59. return ret;
60. }
61. ret = OH_Huks_FinishSession(&handleEncrypt, encryptParamSet, inData, cipherText);
62. return ret;
63. }

65. OH_Huks_Result HksRsaPkcsTestDecrypt(const struct OH_Huks_Blob *keyAlias,
66. const struct OH_Huks_ParamSet *decryptParamSet,
67. const struct OH_Huks_Blob *cipherText, struct OH_Huks_Blob *plainText,
68. const struct OH_Huks_Blob *inData)
69. {
70. uint8_t handleD[sizeof(uint64_t)] = {0};
71. struct OH_Huks_Blob handleDecrypt = {sizeof(uint64_t), handleD};
72. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, decryptParamSet, &handleDecrypt, nullptr);
73. if (ret.errorCode != OH_HUKS_SUCCESS) {
74. return ret;
75. }
76. ret = OH_Huks_FinishSession(&handleDecrypt, decryptParamSet, cipherText, plainText);
77. return ret;
78. }

80. napi_value TestRsaEcbPkcs(napi_env env, napi_callback_info info)
81. {
82. char tmpKeyAlias[] = "test_enc_dec";
83. struct OH_Huks_Blob keyAlias = {(uint32_t)strlen(tmpKeyAlias), (uint8_t *)tmpKeyAlias};
84. struct OH_Huks_ParamSet *genParamSet = nullptr;
85. struct OH_Huks_ParamSet *encryptParamSet = nullptr;
86. struct OH_Huks_ParamSet *decryptParamSet = nullptr;
87. OH_Huks_Result ohResult;
88. do {
89. /* 1. 模拟生成密钥场景 */
90. /*
91. * 1.1. 获取生成密钥算法参数配置
92. */
93. ohResult = InitParamSet(&genParamSet, g_genEncDecParams, sizeof(g_genEncDecParams) / sizeof(OH_Huks_Param));
94. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
95. break;
96. }
97. /*
98. * 1.2. 调用generateKeyItem
99. */
100. ohResult = OH_Huks_GenerateKeyItem(&keyAlias, genParamSet, nullptr);
101. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
102. break;
103. }
104. /* 2. 模拟加密场景 */
105. /*
106. * 2.1. 获取加密算法参数配置
107. */
108. ohResult = InitParamSet(&encryptParamSet, g_encryptParams, sizeof(g_encryptParams) / sizeof(OH_Huks_Param));
109. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
110. break;
111. }
112. char tmpInData[] = "RSA_ECB_OAEP_IN";
113. struct OH_Huks_Blob inData = {(uint32_t)strlen(tmpInData), (uint8_t *)tmpInData};
114. uint8_t cipher[RSA_COMMON_SIZE] = {0};
115. struct OH_Huks_Blob cipherText = {RSA_COMMON_SIZE, cipher};
116. /*
117. * 2.2. 调用HksRsaPkcsTestEncrypt获取加密后的密文
118. */
119. ohResult = HksRsaPkcsTestEncrypt(&keyAlias, encryptParamSet, &inData, &cipherText);
120. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
121. break;
122. }
123. /* 3. 模拟解密场景 */
124. /*
125. * 3.1. 获取解密算法参数配置
126. */
127. ohResult = InitParamSet(&decryptParamSet, g_decryptParams, sizeof(g_decryptParams) / sizeof(OH_Huks_Param));
128. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
129. break;
130. }
131. uint8_t plain[RSA_COMMON_SIZE] = {0};
132. struct OH_Huks_Blob plainText = {RSA_COMMON_SIZE, plain};
133. /*
134. * 3.2. 调用HksRsaPkcsTestDecrypt获取解密后的数据
135. */
136. ohResult = HksRsaPkcsTestDecrypt(&keyAlias, decryptParamSet, &cipherText, &plainText, &inData);
137. } while (0);
138. /* 4. 模拟删除密钥场景 */
139. /*
140. * 4.1. 调用deleteKeyItem删除密钥
141. */
142. (void)OH_Huks_DeleteKeyItem(&keyAlias, genParamSet);

144. OH_Huks_FreeParamSet(&genParamSet);
145. OH_Huks_FreeParamSet(&encryptParamSet);
146. OH_Huks_FreeParamSet(&decryptParamSet);

148. napi_value ret;
149. napi_create_int32(env, ohResult.errorCode, &ret);
150. return ret;
151. }
```

[napi\_rsaecbpkcs1\_v1\_5.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/EncryptionDecryption/entry/src/main/cpp/types/projects/napi_rsaecbpkcs1_v1_5.cpp#L17-L169)

### RSA/ECB/OAEP/SHA256

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <cstring>

6. static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
7. uint32_t paramCount)
8. {
9. OH_Huks_Result ret = OH_Huks_InitParamSet(paramSet);
10. if (ret.errorCode != OH_HUKS_SUCCESS) {
11. return ret;
12. }
13. ret = OH_Huks_AddParams(*paramSet, params, paramCount);
14. if (ret.errorCode != OH_HUKS_SUCCESS) {
15. OH_Huks_FreeParamSet(paramSet);
16. return ret;
17. }
18. ret = OH_Huks_BuildParamSet(paramSet);
19. if (ret.errorCode != OH_HUKS_SUCCESS) {
20. OH_Huks_FreeParamSet(paramSet);
21. return ret;
22. }
23. return ret;
24. }

26. static struct OH_Huks_Param g_genEncDecParams[] = {
27. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_RSA},
28. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT | OH_HUKS_KEY_PURPOSE_DECRYPT},
29. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_RSA_KEY_SIZE_1024},
30. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_OAEP},
31. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
32. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256}};

34. static struct OH_Huks_Param g_encryptParams[] = {
35. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_RSA},
36. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT},
37. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_RSA_KEY_SIZE_1024},
38. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_OAEP},
39. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
40. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256}};

42. static struct OH_Huks_Param g_decryptParams[] = {
43. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_RSA},
44. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_DECRYPT},
45. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_RSA_KEY_SIZE_1024},
46. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_OAEP},
47. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
48. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256}};

50. static const uint32_t RSA_COMMON_SIZE = 1024;
51. OH_Huks_Result HksRsaOaepTestEncrypt(const struct OH_Huks_Blob *keyAlias,
52. const struct OH_Huks_ParamSet *encryptParamSet,
53. const struct OH_Huks_Blob *inData, struct OH_Huks_Blob *cipherText)
54. {
55. uint8_t handleE[sizeof(uint64_t)] = {0};
56. struct OH_Huks_Blob handleEncrypt = {sizeof(uint64_t), handleE};
57. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, encryptParamSet, &handleEncrypt, nullptr);
58. if (ret.errorCode != OH_HUKS_SUCCESS) {
59. return ret;
60. }
61. ret = OH_Huks_FinishSession(&handleEncrypt, encryptParamSet, inData, cipherText);
62. return ret;
63. }

65. OH_Huks_Result HksRsaOaepTestDecrypt(const struct OH_Huks_Blob *keyAlias,
66. const struct OH_Huks_ParamSet *decryptParamSet,
67. const struct OH_Huks_Blob *cipherText, struct OH_Huks_Blob *plainText,
68. const struct OH_Huks_Blob *inData)
69. {
70. uint8_t handleD[sizeof(uint64_t)] = {0};
71. struct OH_Huks_Blob handleDecrypt = {sizeof(uint64_t), handleD};
72. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, decryptParamSet, &handleDecrypt, nullptr);
73. if (ret.errorCode != OH_HUKS_SUCCESS) {
74. return ret;
75. }
76. ret = OH_Huks_FinishSession(&handleDecrypt, decryptParamSet, cipherText, plainText);
77. return ret;
78. }

80. napi_value TestRsaEcbOaep(napi_env env, napi_callback_info info)
81. {
82. char tmpKeyAlias[] = "test_enc_dec";
83. struct OH_Huks_Blob keyAlias = {(uint32_t)strlen(tmpKeyAlias), (uint8_t *)tmpKeyAlias};
84. struct OH_Huks_ParamSet *genParamSet = nullptr;
85. struct OH_Huks_ParamSet *encryptParamSet = nullptr;
86. struct OH_Huks_ParamSet *decryptParamSet = nullptr;
87. OH_Huks_Result ohResult;
88. do {
89. /* 1. 模拟生成密钥场景 */
90. /*
91. * 1.1. 获取生成密钥算法参数配置
92. */
93. ohResult = InitParamSet(&genParamSet, g_genEncDecParams, sizeof(g_genEncDecParams) / sizeof(OH_Huks_Param));
94. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
95. break;
96. }
97. /*
98. * 1.2. 调用generateKeyItem
99. */
100. ohResult = OH_Huks_GenerateKeyItem(&keyAlias, genParamSet, nullptr);
101. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
102. break;
103. }
104. /* 2. 模拟加密场景 */
105. /*
106. * 2.1. 获取加密算法参数配置
107. */
108. ohResult = InitParamSet(&encryptParamSet, g_encryptParams, sizeof(g_encryptParams) / sizeof(OH_Huks_Param));
109. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
110. break;
111. }
112. char tmpInData[] = "RSA_ECB_OAEP_IN";
113. struct OH_Huks_Blob inData = {(uint32_t)strlen(tmpInData), (uint8_t *)tmpInData};
114. uint8_t cipher[RSA_COMMON_SIZE] = {0};
115. struct OH_Huks_Blob cipherText = {RSA_COMMON_SIZE, cipher};
116. /*
117. * 2.2. 调用HksRsaOaepTestEncrypt获取加密后的密文
118. */
119. ohResult = HksRsaOaepTestEncrypt(&keyAlias, encryptParamSet, &inData, &cipherText);
120. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
121. break;
122. }
123. /* 3. 模拟解密场景 */
124. /*
125. * 3.1. 获取解密算法参数配置
126. */
127. ohResult = InitParamSet(&decryptParamSet, g_decryptParams, sizeof(g_decryptParams) / sizeof(OH_Huks_Param));
128. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
129. break;
130. }
131. uint8_t plain[RSA_COMMON_SIZE] = {0};
132. struct OH_Huks_Blob plainText = {RSA_COMMON_SIZE, plain};
133. /*
134. * 3.2. 调用HksRsaOaepTestDecrypt获取解密后的数据
135. */
136. ohResult = HksRsaOaepTestDecrypt(&keyAlias, decryptParamSet, &cipherText, &plainText, &inData);
137. } while (0);
138. /* 4. 模拟删除密钥场景 */
139. /*
140. * 4.1. 调用deleteKeyItem删除密钥
141. */
142. (void)OH_Huks_DeleteKeyItem(&keyAlias, genParamSet);

144. OH_Huks_FreeParamSet(&genParamSet);
145. OH_Huks_FreeParamSet(&encryptParamSet);
146. OH_Huks_FreeParamSet(&decryptParamSet);

148. napi_value ret;
149. napi_create_int32(env, ohResult.errorCode, &ret);
150. return ret;
151. }
```

[napi\_rsaecboaepsha256.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/EncryptionDecryption/entry/src/main/cpp/types/projects/napi_rsaecboaepsha256.cpp#L16-L168)

### SM2

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <cstring>

6. static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
7. uint32_t paramCount)
8. {
9. OH_Huks_Result ret = OH_Huks_InitParamSet(paramSet);
10. if (ret.errorCode != OH_HUKS_SUCCESS) {
11. return ret;
12. }
13. ret = OH_Huks_AddParams(*paramSet, params, paramCount);
14. if (ret.errorCode != OH_HUKS_SUCCESS) {
15. OH_Huks_FreeParamSet(paramSet);
16. return ret;
17. }
18. ret = OH_Huks_BuildParamSet(paramSet);
19. if (ret.errorCode != OH_HUKS_SUCCESS) {
20. OH_Huks_FreeParamSet(paramSet);
21. return ret;
22. }
23. return ret;
24. }

26. static struct OH_Huks_Param g_genEncDecParams[] = {
27. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_SM2},
28. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT | OH_HUKS_KEY_PURPOSE_DECRYPT},
29. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_SM2_KEY_SIZE_256},
30. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SM3}};

32. static struct OH_Huks_Param g_encryptParams[] = {
33. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_SM2},
34. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT},
35. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_SM2_KEY_SIZE_256},
36. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SM3}};

38. static struct OH_Huks_Param g_decryptParams[] = {
39. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_SM2},
40. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_DECRYPT},
41. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_SM2_KEY_SIZE_256},
42. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SM3}};

44. static const uint32_t SM2_SIZE = 1024;
45. OH_Huks_Result HksSm2TestEncrypt(const struct OH_Huks_Blob *keyAlias,
46. const struct OH_Huks_ParamSet *encryptParamSet,
47. const struct OH_Huks_Blob *inData, struct OH_Huks_Blob *cipherText)
48. {
49. uint8_t handleE[sizeof(uint64_t)] = {0};
50. struct OH_Huks_Blob handleEncrypt = {sizeof(uint64_t), handleE};
51. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, encryptParamSet, &handleEncrypt, nullptr);
52. if (ret.errorCode != OH_HUKS_SUCCESS) {
53. return ret;
54. }
55. ret = OH_Huks_FinishSession(&handleEncrypt, encryptParamSet, inData, cipherText);
56. return ret;
57. }

59. OH_Huks_Result HksSm2TestDecrypt(const struct OH_Huks_Blob *keyAlias,
60. const struct OH_Huks_ParamSet *decryptParamSet,
61. const struct OH_Huks_Blob *cipherText, struct OH_Huks_Blob *plainText,
62. const struct OH_Huks_Blob *inData)
63. {
64. uint8_t handleD[sizeof(uint64_t)] = {0};
65. struct OH_Huks_Blob handleDecrypt = {sizeof(uint64_t), handleD};
66. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, decryptParamSet, &handleDecrypt, nullptr);
67. if (ret.errorCode != OH_HUKS_SUCCESS) {
68. return ret;
69. }
70. ret = OH_Huks_FinishSession(&handleDecrypt, decryptParamSet, cipherText, plainText);
71. return ret;
72. }

74. napi_value TestSm2(napi_env env, napi_callback_info info)
75. {
76. char tmpKeyAlias[] = "test_sm2key";
77. struct OH_Huks_Blob keyAlias = {(uint32_t)strlen(tmpKeyAlias), (uint8_t *)tmpKeyAlias};
78. struct OH_Huks_ParamSet *genParamSet = nullptr;
79. struct OH_Huks_ParamSet *encryptParamSet = nullptr;
80. struct OH_Huks_ParamSet *decryptParamSet = nullptr;
81. OH_Huks_Result ohResult;
82. do {
83. /* 1. 模拟生成密钥场景 */
84. /*
85. * 1.1. 获取生成密钥算法参数配置
86. */
87. ohResult = InitParamSet(&genParamSet, g_genEncDecParams, sizeof(g_genEncDecParams) / sizeof(OH_Huks_Param));
88. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
89. break;
90. }
91. /*
92. * 1.2. 调用generateKeyItem
93. */
94. ohResult = OH_Huks_GenerateKeyItem(&keyAlias, genParamSet, nullptr);
95. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
96. break;
97. }
98. /* 2. 模拟加密场景 */
99. /*
100. * 2.1. 获取加密算法参数配置
101. */
102. ohResult = InitParamSet(&encryptParamSet, g_encryptParams, sizeof(g_encryptParams) / sizeof(OH_Huks_Param));
103. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
104. break;
105. }
106. char tmpInData[] = "AES_ECB_INDATA_1";
107. struct OH_Huks_Blob inData = {(uint32_t)strlen(tmpInData), (uint8_t *)tmpInData};
108. uint8_t cipher[SM2_SIZE] = {0};
109. struct OH_Huks_Blob cipherText = {SM2_SIZE, cipher};
110. /*
111. * 2.2. 调用HksSm2TestEncrypt获取加密后的密文
112. */
113. ohResult = HksSm2TestEncrypt(&keyAlias, encryptParamSet, &inData, &cipherText);
114. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
115. break;
116. }
117. /* 3. 模拟解密场景 */
118. /*
119. * 3.1. 获取解密算法参数配置
120. */
121. ohResult = InitParamSet(&decryptParamSet, g_decryptParams, sizeof(g_decryptParams) / sizeof(OH_Huks_Param));
122. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
123. break;
124. }
125. uint8_t plain[SM2_SIZE] = {0};
126. struct OH_Huks_Blob plainText = {SM2_SIZE, plain};
127. /*
128. * 3.2. 调用HksSm2TestDecrypt获取解密后的数据
129. */
130. ohResult = HksSm2TestDecrypt(&keyAlias, decryptParamSet, &cipherText, &plainText, &inData);
131. } while (0);
132. /* 4. 模拟删除密钥场景 */
133. /*
134. * 4.1. 调用deleteKeyItem删除密钥
135. */
136. (void)OH_Huks_DeleteKeyItem(&keyAlias, genParamSet);

138. OH_Huks_FreeParamSet(&genParamSet);
139. OH_Huks_FreeParamSet(&encryptParamSet);
140. OH_Huks_FreeParamSet(&decryptParamSet);

142. napi_value ret;
143. napi_create_int32(env, ohResult.errorCode, &ret);
144. return ret;
145. }
```

[napi\_sm2.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/EncryptionDecryption/entry/src/main/cpp/types/projects/napi_sm2.cpp#L16-L162)
