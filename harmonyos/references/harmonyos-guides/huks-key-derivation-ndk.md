---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-derivation-ndk
title: 密钥派生(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 密钥派生 > 密钥派生(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5bff2c089b6faa3a5acd1467d95a4d1db3ab21a492e5f046c7e54016bd753967
---

以HKDF256和PBKDF2密钥为例，完成密钥派生。具体的场景介绍及支持的算法规格，请参考[密钥派生支持的算法](huks-key-derivation-overview.md#支持的算法)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

## 开发步骤

**生成密钥**

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集，可指定参数，OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG（可选），用于标识基于该密钥派生出的密钥是否由HUKS管理。

   * 当TAG设置为OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS时，表示基于该密钥派生出的密钥，由HUKS管理，可保证派生密钥全生命周期不出安全环境。
   * 当TAG设置为OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED时，表示基于该密钥派生出的密钥，返回给调用方管理，由业务自行保证密钥安全。
   * 若业务未设置TAG的具体值，表示基于该密钥派生出的密钥，即可由HUKS管理，也可返回给调用方管理，业务可在后续派生时再选择使用何种方式保护密钥。
3. 调用[OH\_Huks\_GenerateKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_generatekeyitem)生成密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md)，导入已有的密钥。

**密钥派生**

1. 获取密钥别名，指定对应的属性参数HuksOptions。

   可指定参数OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG（可选），用于标识派生得到的密钥是否由HUKS管理。

   | 生成 | 派生 | 规格 |
   | --- | --- | --- |
   | OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | 密钥由HUKS管理 |
   | OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | 密钥返回给调用方管理 |
   | 未指定TAG具体值 | OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | 密钥由HUKS管理 |
   | 未指定TAG具体值 | OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | 密钥返回给调用方管理 |
   | 未指定TAG具体值 | 未指定TAG具体值 | 密钥返回给调用方管理 |

   注：派生时指定的TAG值，不可与生成时指定的TAG值冲突。表格中仅列举有效的指定方式。
2. 调用[OH\_Huks\_InitSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_initsession)初始化密钥会话，并获取会话的句柄handle。
3. 调用[OH\_Huks\_UpdateSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_updatesession)更新密钥会话。
4. 调用[OH\_Huks\_FinishSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_finishsession)结束密钥会话，完成派生。

**删除密钥**

当密钥废弃不用时，需要调用OH\_Huks\_DeleteKeyItem删除密钥，具体请参考[密钥删除](huks-delete-key-ndk.md)。

## 开发案例

### HKDF

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

26. static const uint32_t DERIVE_KEY_SIZE_32 = 32;
27. static const uint32_t DERIVE_KEY_SIZE_256 = 256;
28. static struct OH_Huks_Blob g_deriveKeyAlias = {(uint32_t)strlen("test_derive"), (uint8_t *)"test_derive"};
29. static struct OH_Huks_Param g_genDeriveParams[] = {
30. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
31. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_DERIVE},
32. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256},
33. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256}};
34. static struct OH_Huks_Param g_hkdfParams[] = {{.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_HKDF},
35. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_DERIVE},
36. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256},
37. {.tag = OH_HUKS_TAG_DERIVE_KEY_SIZE, .uint32Param = DERIVE_KEY_SIZE_32}};
38. static struct OH_Huks_Param g_hkdfFinishParams[] = {
39. {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_ONLY_USED_IN_HUKS},
40. {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_deriveKeyAlias},
41. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
42. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = DERIVE_KEY_SIZE_256},
43. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_DERIVE},
44. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256}};
45. static const uint32_t COMMON_SIZE = 2048;
46. static const char *G_DERIVE_IN_DATA = "Hks_HKDF_Derive_Test_0_string";
47. static OH_Huks_Result PerformHkdfDerivation(const struct OH_Huks_Blob *genAlias,
48. struct OH_Huks_ParamSet *hkdfParamSet,
49. struct OH_Huks_ParamSet *hkdfFinishParamSet,
50. const struct OH_Huks_Blob &inData)
51. {
52. OH_Huks_Result ohResult;
53. // Init
54. uint8_t handleD[sizeof(uint64_t)] = {0};
55. struct OH_Huks_Blob handleDerive = {sizeof(uint64_t), handleD};
56. ohResult = OH_Huks_InitSession(genAlias, hkdfParamSet, &handleDerive, nullptr);
57. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
58. return ohResult;
59. }
60. // Update
61. uint8_t tmpOut[COMMON_SIZE] = {0};
62. struct OH_Huks_Blob outData = {COMMON_SIZE, tmpOut};
63. ohResult = OH_Huks_UpdateSession(&handleDerive, hkdfParamSet, &inData, &outData);
64. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
65. return ohResult;
66. }
67. // Finish
68. uint8_t outDataD[COMMON_SIZE] = {0};
69. struct OH_Huks_Blob outDataDerive = {COMMON_SIZE, outDataD};
70. ohResult = OH_Huks_FinishSession(&handleDerive, hkdfFinishParamSet, &inData, &outDataDerive);
71. return ohResult;
72. }

74. napi_value HkdfDeriveKey(napi_env env, napi_callback_info info)
75. {
76. struct OH_Huks_Blob genAlias = {(uint32_t)strlen("test_signVerify"), (uint8_t *)"test_signVerify"};
77. struct OH_Huks_Blob inData = {(uint32_t)strlen(G_DERIVE_IN_DATA), (uint8_t *)G_DERIVE_IN_DATA};
78. struct OH_Huks_ParamSet *genParamSet = nullptr;
79. struct OH_Huks_ParamSet *hkdfParamSet = nullptr;
80. struct OH_Huks_ParamSet *hkdfFinishParamSet = nullptr;
81. OH_Huks_Result ohResult;
82. do {
83. ohResult = InitParamSet(&genParamSet, g_genDeriveParams, sizeof(g_genDeriveParams) /
84. sizeof(OH_Huks_Param));
85. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
86. break;
87. }

89. ohResult = InitParamSet(&hkdfParamSet, g_hkdfParams, sizeof(g_hkdfParams) /
90. sizeof(OH_Huks_Param));
91. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
92. break;
93. }
94. // finish paramset
95. ohResult =
96. InitParamSet(&hkdfFinishParamSet, g_hkdfFinishParams, sizeof(g_hkdfFinishParams) /
97. sizeof(OH_Huks_Param));
98. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
99. break;
100. }
101. /* 1. 生成密钥 */
102. ohResult = OH_Huks_GenerateKeyItem(&genAlias, genParamSet, nullptr);
103. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
104. break;
105. }
106. /* 2. 派生密钥 */
107. ohResult = PerformHkdfDerivation(&genAlias, hkdfParamSet, hkdfFinishParamSet, inData);
108. } while (0);
109. (void)OH_Huks_DeleteKeyItem(&genAlias, nullptr);
110. (void)OH_Huks_DeleteKeyItem(&g_deriveKeyAlias, nullptr);
111. OH_Huks_FreeParamSet(&genParamSet);
112. OH_Huks_FreeParamSet(&hkdfParamSet);
113. OH_Huks_FreeParamSet(&hkdfFinishParamSet);

115. napi_value ret;
116. napi_create_int32(env, ohResult.errorCode, &ret);
117. return ret;
118. }
```

[napi\_hkdf256.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/KeyDerivation/entry/src/main/cpp/types/projects/napi_hkdf256.cpp#L15-L134)

### PBKDF2

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <cstring>
5. #include "file.h"

7. OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
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
26. static const uint32_t DERIVE_KEY_SIZE_32 = 32;
27. static const uint32_t DERIVE_KEY_SIZE_256 = 256;
28. static const uint32_t DERIVE_KEY_ITERATION = 10000;
29. static const uint32_t SALT_SIZE = 8;
30. static const char DERIVE_KEY_SALT[SALT_SIZE] = "mysalt1";
31. static struct OH_Huks_Blob g_deriveKeyAlias = {(uint32_t)strlen("test_derive"), (uint8_t *)"test_derive"};
32. static struct OH_Huks_Param g_genDeriveParams[] = {
33. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
34. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_DERIVE},
35. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256},
36. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256}};
37. static struct OH_Huks_Param g_hkdfParams[] = {{.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_PBKDF2},
38. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_DERIVE},
39. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256},
40. {.tag = OH_HUKS_TAG_DERIVE_KEY_SIZE, .uint32Param = DERIVE_KEY_SIZE_32},
41. {.tag = OH_HUKS_TAG_ITERATION, .uint32Param = DERIVE_KEY_ITERATION},
42. {.tag = OH_HUKS_TAG_SALT,
43. .blob = {
44. .size = SALT_SIZE,
45. .data = (uint8_t *) DERIVE_KEY_SALT
46. }}};
47. static struct OH_Huks_Param g_hkdfFinishParams[] = {
48. {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_ONLY_USED_IN_HUKS},
49. {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_deriveKeyAlias},
50. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
51. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = DERIVE_KEY_SIZE_256},
52. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_DERIVE},
53. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE},
54. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
55. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB}};
56. static const uint32_t COMMON_SIZE = 1024;
57. static const char *G_DERIVE_IN_DATA = "Hks_PBKDF2_Derive_Test_0_string";
58. static OH_Huks_Result PerformPbkdfDerivation(const struct OH_Huks_Blob *genAlias,
59. struct OH_Huks_ParamSet *hkdfParamSet,
60. struct OH_Huks_ParamSet *hkdfFinishParamSet,
61. const struct OH_Huks_Blob &inData)
62. {
63. OH_Huks_Result ohResult;
64. // Init
65. uint8_t handleD[sizeof(uint64_t)] = {0};
66. struct OH_Huks_Blob handleDerive = {sizeof(uint64_t), handleD};
67. ohResult = OH_Huks_InitSession(genAlias, hkdfParamSet, &handleDerive, nullptr);
68. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
69. return ohResult;
70. }
71. // Update
72. uint8_t tmpOut[COMMON_SIZE] = {0};
73. struct OH_Huks_Blob outData = {COMMON_SIZE, tmpOut};
74. ohResult = OH_Huks_UpdateSession(&handleDerive, hkdfParamSet, &inData, &outData);
75. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
76. return ohResult;
77. }
78. // Finish
79. uint8_t outDataD[COMMON_SIZE] = {0};
80. struct OH_Huks_Blob outDataDerive = {COMMON_SIZE, outDataD};
81. ohResult = OH_Huks_FinishSession(&handleDerive, hkdfFinishParamSet, &inData, &outDataDerive);
82. return ohResult;
83. }

85. napi_value PbkdfDeriveKey(napi_env env, napi_callback_info info)
86. {
87. struct OH_Huks_Blob genAlias = {(uint32_t)strlen("test_signVerify"), (uint8_t *)"test_signVerify"};
88. struct OH_Huks_Blob inData = {(uint32_t)strlen(G_DERIVE_IN_DATA), (uint8_t *)G_DERIVE_IN_DATA};
89. struct OH_Huks_ParamSet *genParamSet = nullptr;
90. struct OH_Huks_ParamSet *hkdfParamSet = nullptr;
91. struct OH_Huks_ParamSet *hkdfFinishParamSet = nullptr;
92. OH_Huks_Result ohResult;
93. do {
94. ohResult = InitParamSet(&genParamSet, g_genDeriveParams, sizeof(g_genDeriveParams) /
95. sizeof(OH_Huks_Param));
96. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
97. break;
98. }
99. ohResult = InitParamSet(&hkdfParamSet, g_hkdfParams, sizeof(g_hkdfParams) /
100. sizeof(OH_Huks_Param));
101. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
102. break;
103. }
104. ohResult =InitParamSet(&hkdfFinishParamSet, g_hkdfFinishParams, sizeof(g_hkdfFinishParams) /
105. sizeof(OH_Huks_Param));
106. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
107. break;
108. }
109. /* 1. 生成密钥 */
110. ohResult = OH_Huks_GenerateKeyItem(&genAlias, genParamSet, nullptr);
111. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
112. break;
113. }
114. /* 2. 派生密钥 */
115. ohResult = PerformPbkdfDerivation(&genAlias, hkdfParamSet, hkdfFinishParamSet, inData);
116. } while (0);
117. (void)OH_Huks_DeleteKeyItem(&genAlias, nullptr);
118. (void)OH_Huks_DeleteKeyItem(&g_deriveKeyAlias, nullptr);
119. OH_Huks_FreeParamSet(&genParamSet);
120. OH_Huks_FreeParamSet(&hkdfParamSet);
121. OH_Huks_FreeParamSet(&hkdfFinishParamSet);

123. napi_value ret;
124. napi_create_int32(env, ohResult.errorCode, &ret);
125. return ret;
126. }
```

[napi\_pbkdf2.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/KeyDerivation/entry/src/main/cpp/types/projects/napi_pbkdf2.cpp#L15-L142)
