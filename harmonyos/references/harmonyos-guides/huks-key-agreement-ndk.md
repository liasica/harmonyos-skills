---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-agreement-ndk
title: 密钥协商(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 密钥协商 > 密钥协商(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:023a9a7f90d301962800a9df7659f2ac8d1a5ec93278d3bfcb326677894ab2d7
---

以X25519、DH和ECDH协商密钥类型为例，在密钥由HUKS管理的情况下，完成密钥协商。具体的场景介绍及支持的算法规格，请参考[密钥协商支持的算法](huks-key-agreement-overview.md#支持的算法)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

## 开发步骤

**生成密钥**

设备A、设备B各自生成一个非对称密钥，具体请参考[密钥生成](huks-key-generation-overview.md)或[密钥导入](huks-key-import-overview.md)。

密钥生成时，可指定参数，OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG（可选），用于标识此步骤生成的密钥是否由HUKS管理。

**导出密钥**

设备A、B导出非对称密钥对的公钥材料，具体请参考[密钥导出](huks-export-key-arkts.md)。

**密钥协商**

设备A、B分别基于本端私钥和对端设备的公钥，协商出共享密钥。

密钥协商时，可指定参数OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG（可选），用于标识协商得到的密钥是否由HUKS管理。

* 当TAG设置为OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS时，表示基于该密钥协商出的密钥，由HUKS管理，可保证协商密钥全生命周期不出安全环境。
* 当TAG设置为OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED时，表示基于该密钥协商出的密钥，返回给调用方管理，由业务自行保证密钥安全。
* 若业务未设置TAG的具体值，表示基于该密钥协商出的密钥，既可由HUKS管理，也可返回给调用方管理，业务可在后续协商时再选择使用何种方式保护密钥。

| 生成 | 协商 | 规格 |
| --- | --- | --- |
| OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | 密钥由HUKS管理 |
| OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | 密钥返回给调用方管理 |
| 未指定TAG具体值 | OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | 密钥由HUKS管理 |
| 未指定TAG具体值 | OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | 密钥返回给调用方管理 |
| 未指定TAG具体值 | 未指定TAG具体值 | 密钥返回给调用方管理 |

注：协商时指定的TAG值，不可与生成时指定的TAG值冲突。表格中仅列举有效的指定方式。

**删除密钥**

当密钥废弃不用时，设备A、B均需要删除密钥，具体请参考[密钥删除](huks-delete-key-ndk.md)。

## 开发案例

下面分别以X25519、DH和ECDH密钥为例，进行协商。

### X25519非对称密钥协商用例

准备X25519密钥协商材料：

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <cstring>
5. #include "file.h"

7. /* 初始化参数 */
8. static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
9. uint32_t paramCount)
10. {
11. OH_Huks_Result ret = OH_Huks_InitParamSet(paramSet);
12. if (ret.errorCode != OH_HUKS_SUCCESS) {
13. return ret;
14. }
15. ret = OH_Huks_AddParams(*paramSet, params, paramCount);
16. if (ret.errorCode != OH_HUKS_SUCCESS) {
17. OH_Huks_FreeParamSet(paramSet);
18. return ret;
19. }
20. ret = OH_Huks_BuildParamSet(paramSet);
21. if (ret.errorCode != OH_HUKS_SUCCESS) {
22. OH_Huks_FreeParamSet(paramSet);
23. return ret;
24. }
25. return ret;
26. }
27. static struct OH_Huks_Blob g_keyAliasFinal1001 = {(uint32_t)strlen("HksECDHAgreeKeyAliasTest001_1_final"),
28. (uint8_t *)"HksECDHAgreeKeyAliasTest001_1_final"};
29. /* 集成密钥参数集 */
30. static struct OH_Huks_Param g_genAgreeParams[] = {
31. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_X25519},
32. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
33. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_CURVE25519_KEY_SIZE_256},
34. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};
35. static struct OH_Huks_Param g_agreeParamsInit01[] = {
36. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_X25519},
37. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
38. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_CURVE25519_KEY_SIZE_256},
39. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};
40. static struct OH_Huks_Param g_agreeParamsFinish01[] = {
41. {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_ONLY_USED_IN_HUKS},
42. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
43. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
44. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
45. {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_keyAliasFinal1001},
46. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
47. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
48. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};
49. static struct OH_Huks_Blob g_keyAliasFinal2001 = {(uint32_t)strlen("HksX25519AgreeKeyAliasTest001_2_final"),
50. (uint8_t *)"HksX25519AgreeKeyAliasTest001_2_final"};
51. static struct OH_Huks_Param g_agreeParamsInit02[] = {
52. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_X25519},
53. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
54. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_CURVE25519_KEY_SIZE_256},
55. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};
56. static struct OH_Huks_Param g_agreeParamsFinish02[] = {
57. {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_ONLY_USED_IN_HUKS},
58. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
59. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
60. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
61. {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_keyAliasFinal2001},
62. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
63. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
64. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};
65. static const uint32_t X25519_COMMON_SIZE = 256;
66. static struct OH_Huks_Blob g_keyAlias01001 = {(uint32_t)strlen("HksX25519AgreeKeyAliasTest001_1"),
67. (uint8_t *)"HksX25519AgreeKeyAliasTest001_1"};
68. static struct OH_Huks_Blob g_keyAlias02001 = {(uint32_t)strlen("HksX25519AgreeKeyAliasTest001_2"),
69. (uint8_t *)"HksX25519AgreeKeyAliasTest001_2"};
```

[napi\_X25519.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/KeyExchange/entry/src/main/cpp/types/projects/napi_X25519.cpp#L15-L86)

执行密钥协商：

```
1. /* 导出密钥 */
2. OH_Huks_Result HksX25519AgreeExport(const struct OH_Huks_Blob *keyAlias1, const struct OH_Huks_Blob *keyAlias2,
3. struct OH_Huks_Blob *publicKey1, struct OH_Huks_Blob *publicKey2,
4. const struct OH_Huks_ParamSet *genParamSet)
5. {
6. OH_Huks_Result ret = OH_Huks_ExportPublicKeyItem(keyAlias1, genParamSet, publicKey1);
7. if (ret.errorCode != OH_HUKS_SUCCESS) {
8. return ret;
9. }
10. ret = OH_Huks_ExportPublicKeyItem(keyAlias2, genParamSet, publicKey2);
11. if (ret.errorCode != OH_HUKS_SUCCESS) {
12. return ret;
13. }
14. return ret;
15. }
16. static const char *IN_DATA = "Hks_X25519_Agree_Test";
17. /* 协商密钥操作 */
18. OH_Huks_Result HksX25519AgreeFinish(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_Blob *publicKey,
19. const struct OH_Huks_ParamSet *initParamSet,
20. const struct OH_Huks_ParamSet *finishParamSet, struct OH_Huks_Blob *outData)
21. {
22. struct OH_Huks_Blob inData = {(uint32_t)strlen(IN_DATA), (uint8_t *)IN_DATA};
23. uint8_t handleU[sizeof(uint64_t)] = {0};
24. struct OH_Huks_Blob handle = {sizeof(uint64_t), handleU};
25. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, initParamSet, &handle, nullptr);
26. if (ret.errorCode != OH_HUKS_SUCCESS) {
27. return ret;
28. }
29. uint8_t outDataU[X25519_COMMON_SIZE] = {0};
30. struct OH_Huks_Blob outDataUpdate = {X25519_COMMON_SIZE, outDataU};
31. ret = OH_Huks_UpdateSession(&handle, initParamSet, publicKey, &outDataUpdate);
32. if (ret.errorCode != OH_HUKS_SUCCESS) {
33. return ret;
34. }
35. ret = OH_Huks_FinishSession(&handle, finishParamSet, &inData, outData);
36. if (ret.errorCode != OH_HUKS_SUCCESS) {
37. return ret;
38. }
39. return ret;
40. }

42. static OH_Huks_Result InitializeAgreeParamSets(struct OH_Huks_ParamSet **genParamSet,
43. struct OH_Huks_ParamSet **initParamSet01,
44. struct OH_Huks_ParamSet **finishParamSet01,
45. struct OH_Huks_ParamSet **initParamSet02,
46. struct OH_Huks_ParamSet **finishParamSet02)
47. {
48. OH_Huks_Result ohResult;

50. ohResult = InitParamSet(genParamSet, g_genAgreeParams,
51. sizeof(g_genAgreeParams) / sizeof(OH_Huks_Param));
52. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
53. return ohResult;
54. }
55. ohResult = InitParamSet(initParamSet01, g_agreeParamsInit01,
56. sizeof(g_agreeParamsInit01) / sizeof(OH_Huks_Param));
57. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
58. return ohResult;
59. }
60. ohResult = InitParamSet(finishParamSet01, g_agreeParamsFinish01,
61. sizeof(g_agreeParamsFinish01) / sizeof(OH_Huks_Param));
62. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
63. return ohResult;
64. }
65. ohResult = InitParamSet(initParamSet02, g_agreeParamsInit02,
66. sizeof(g_agreeParamsInit02) / sizeof(OH_Huks_Param));
67. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
68. return ohResult;
69. }
70. ohResult = InitParamSet(finishParamSet02, g_agreeParamsFinish02,
71. sizeof(g_agreeParamsFinish02) / sizeof(OH_Huks_Param));
72. return ohResult;
73. }

75. static OH_Huks_Result GenerateKeyPair(struct OH_Huks_ParamSet *genParamSet)
76. {
77. OH_Huks_Result ohResult;

79. /* 设备A生成密钥 */
80. ohResult = OH_Huks_GenerateKeyItem(&g_keyAlias01001, genParamSet, nullptr);
81. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
82. return ohResult;
83. }

85. /* 设备B生成密钥 */
86. ohResult = OH_Huks_GenerateKeyItem(&g_keyAlias02001, genParamSet, nullptr);
87. return ohResult;
88. }

90. static OH_Huks_Result KeyAgreement(struct OH_Huks_Blob *g_keyAlias,
91. struct OH_Huks_Blob *publicKey,
92. struct OH_Huks_Blob *outData,
93. struct OH_Huks_ParamSet *initParamSet,
94. struct OH_Huks_ParamSet *finishParamSet)
95. {
96. OH_Huks_Result ohResult;

98. ohResult = MallocAndCheckBlobData(outData, outData->size);
99. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
100. return ohResult;
101. }
102. /* 协商密钥 */
103. ohResult = HksX25519AgreeFinish(g_keyAlias, publicKey, initParamSet, finishParamSet, outData);
104. return ohResult;
105. }

107. static void CleanKey(struct OH_Huks_Blob *genKeyAlias,
108. struct OH_Huks_Blob *genKeyAliasFinal,
109. struct OH_Huks_ParamSet *genParamSet,
110. struct OH_Huks_ParamSet **initParamSet,
111. struct OH_Huks_ParamSet **finishParamSet)
112. {
113. OH_Huks_DeleteKeyItem(genKeyAlias, genParamSet);
114. OH_Huks_DeleteKeyItem(genKeyAliasFinal, NULL);
115. OH_Huks_FreeParamSet(initParamSet);
116. OH_Huks_FreeParamSet(finishParamSet);
117. }

119. /* 协商密钥整体流程 */
120. napi_value X25519AgreeKey(napi_env env, napi_callback_info info)
121. {
122. struct OH_Huks_ParamSet *genParamSet = nullptr;
123. struct OH_Huks_ParamSet *initParamSet01 = nullptr;
124. struct OH_Huks_ParamSet *finishParamSet01 = nullptr;
125. struct OH_Huks_ParamSet *initParamSet02 = nullptr;
126. struct OH_Huks_ParamSet *finishParamSet02 = nullptr;
127. struct OH_Huks_Blob publicKey01 = {.size = OH_HUKS_AES_KEY_SIZE_256, .data = nullptr};
128. struct OH_Huks_Blob publicKey02 = {.size = OH_HUKS_AES_KEY_SIZE_256, .data = nullptr};
129. struct OH_Huks_Blob outData01 = {.size = X25519_COMMON_SIZE, .data = nullptr};
130. struct OH_Huks_Blob outData02 = {.size = X25519_COMMON_SIZE, .data = nullptr};
131. OH_Huks_Result ohResult;
132. do {
133. /* 1.确定密钥别名集成密钥参数集 */
134. ohResult = InitializeAgreeParamSets(&genParamSet, &initParamSet01, &finishParamSet01,
135. &initParamSet02, &finishParamSet02);
136. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
137. break;
138. }
139. /* 2.设备A和设备B生成密钥 */
140. ohResult = GenerateKeyPair(genParamSet);
141. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
142. break;
143. }
144. ohResult = MallocAndCheckBlobData(&publicKey01, publicKey01.size);
145. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
146. break;
147. }
148. ohResult = MallocAndCheckBlobData(&publicKey02, publicKey02.size);
149. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
150. break;
151. }
152. /* 3.设备A、B导出公钥 */
153. ohResult = HksX25519AgreeExport(&g_keyAlias01001, &g_keyAlias02001, &publicKey01, &publicKey02, genParamSet);
154. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
155. break;
156. }
157. /* 4.设备A、B执行密钥协商 */
158. ohResult = KeyAgreement(&g_keyAlias01001, &publicKey02, &outData01, initParamSet01, finishParamSet01);
159. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
160. break;
161. }
162. ohResult = KeyAgreement(&g_keyAlias02001, &publicKey01, &outData02, initParamSet02, finishParamSet02);
163. } while (0);
164. free(publicKey01.data);
165. free(publicKey02.data);
166. free(outData01.data);
167. free(outData02.data);
168. /* 5.设备A、B删除密钥 */
169. CleanKey(&g_keyAlias01001, &g_keyAliasFinal1001, genParamSet, &initParamSet01, &finishParamSet01);
170. CleanKey(&g_keyAlias02001, &g_keyAliasFinal2001, genParamSet, &initParamSet02, &finishParamSet02);
171. OH_Huks_FreeParamSet(&genParamSet);

173. napi_value ret;
174. napi_create_int32(env, ohResult.errorCode, &ret);
175. return ret;
176. }
```

[napi\_X25519.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/KeyExchange/entry/src/main/cpp/types/projects/napi_X25519.cpp#L102-L280)

### DH密钥协商用例

准备DH密钥协商材料：

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <cstring>
5. #include "file.h"

7. /* 初始化参数 */
8. static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
9. uint32_t paramCount)
10. {
11. OH_Huks_Result ret = OH_Huks_InitParamSet(paramSet);
12. if (ret.errorCode != OH_HUKS_SUCCESS) {
13. return ret;
14. }
15. ret = OH_Huks_AddParams(*paramSet, params, paramCount);
16. if (ret.errorCode != OH_HUKS_SUCCESS) {
17. OH_Huks_FreeParamSet(paramSet);
18. return ret;
19. }
20. ret = OH_Huks_BuildParamSet(paramSet);
21. if (ret.errorCode != OH_HUKS_SUCCESS) {
22. OH_Huks_FreeParamSet(paramSet);
23. return ret;
24. }
25. return ret;
26. }
27. static struct OH_Huks_Blob g_keyAliasFinal1001 = {(uint32_t)strlen("HksDHAgreeKeyAliasTest001_1_final"),
28. (uint8_t *)"HksDHAgreeKeyAliasTest001_1_final"};
29. /* 集成密钥参数集 */
30. static struct OH_Huks_Param g_genAgreeParams[] = {
31. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_DH},
32. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
33. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_DH_KEY_SIZE_2048}};
34. static struct OH_Huks_Param g_agreeParamsInit01[] = {
35. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_DH},
36. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
37. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_DH_KEY_SIZE_2048}};
38. static struct OH_Huks_Param g_agreeParamsFinish01[] = {
39. {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_KEY_EXPORT_ALLOWED},
40. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
41. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
42. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
43. {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_keyAliasFinal1001},
44. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
45. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
46. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};
47. static struct OH_Huks_Param g_agreeParamsFinish01_2[] = {
48. {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_ONLY_USED_IN_HUKS},
49. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
50. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
51. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
52. {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_keyAliasFinal1001},
53. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
54. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
55. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};
56. static struct OH_Huks_Blob g_keyAliasFinal2001 = {(uint32_t)strlen("HksDHAgreeKeyAliasTest001_2_final"),
57. (uint8_t *)"HksDHAgreeKeyAliasTest001_2_final"};
58. static struct OH_Huks_Param g_agreeParamsInit02[] = {
59. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_DH},
60. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
61. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_DH_KEY_SIZE_2048}};
62. static struct OH_Huks_Param g_agreeParamsFinish02[] = {
63. {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_KEY_EXPORT_ALLOWED},
64. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
65. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
66. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
67. {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_keyAliasFinal2001},
68. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
69. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
70. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};
71. static struct OH_Huks_Param g_agreeParamsFinish02_2[] = {
72. {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_ONLY_USED_IN_HUKS},
73. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
74. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
75. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
76. {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_keyAliasFinal2001},
77. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
78. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
79. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};
80. static const uint32_t DH_COMMON_SIZE = 2048;
81. static struct OH_Huks_Blob g_keyAlias01001 = {(uint32_t)strlen("HksDHAgreeKeyAliasTest001_1"),
82. (uint8_t *)"HksDHAgreeKeyAliasTest001_1"};
83. static struct OH_Huks_Blob g_keyAlias02001 = {(uint32_t)strlen("HksDHAgreeKeyAliasTest001_2"),
84. (uint8_t *)"HksDHAgreeKeyAliasTest001_2"};
```

[napi\_DH.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/KeyExchange/entry/src/main/cpp/types/projects/napi_DH.cpp#L15-L100)

执行密钥协商：

```
1. static OH_Huks_Result MallocAndCheckBlobData(struct OH_Huks_Blob *blob, const uint32_t blobSize)
2. {
3. struct OH_Huks_Result ret;
4. ret.errorCode = OH_HUKS_SUCCESS;
5. if (blobSize == 0 || blobSize > DH_COMMON_SIZE) {
6. ret.errorCode = OH_HUKS_ERR_CODE_INTERNAL_ERROR;
7. return ret;
8. }
9. blob->data = (uint8_t *)malloc(blobSize);
10. if (blob->data == NULL) {
11. ret.errorCode = OH_HUKS_ERR_CODE_INTERNAL_ERROR;
12. }
13. return ret;
14. }
15. /* 导出密钥 */
16. OH_Huks_Result HksDHAgreeExport(const struct OH_Huks_Blob *keyAlias1, const struct OH_Huks_Blob *keyAlias2,
17. struct OH_Huks_Blob *publicKey1, struct OH_Huks_Blob *publicKey2,
18. const struct OH_Huks_ParamSet *genParamSet)
19. {
20. OH_Huks_Result ret = OH_Huks_ExportPublicKeyItem(keyAlias1, genParamSet, publicKey1);
21. if (ret.errorCode != OH_HUKS_SUCCESS) {
22. return ret;
23. }
24. ret = OH_Huks_ExportPublicKeyItem(keyAlias2, genParamSet, publicKey2);
25. if (ret.errorCode != OH_HUKS_SUCCESS) {
26. return ret;
27. }
28. return ret;
29. }
30. static const char *IN_DATA = "Hks_DH_Agree_Test";
31. /* 协商密钥操作 */
32. OH_Huks_Result HksDHAgreeFinish(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_Blob *publicKey,
33. const struct OH_Huks_ParamSet *initParamSet,
34. const struct OH_Huks_ParamSet *finishParamSet, struct OH_Huks_Blob *outData)
35. {
36. struct OH_Huks_Blob inData = {(uint32_t)strlen(IN_DATA), (uint8_t *)IN_DATA};
37. uint8_t handleU[sizeof(uint64_t)] = {0};
38. struct OH_Huks_Blob handle = {sizeof(uint64_t), handleU};
39. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, initParamSet, &handle, nullptr);
40. if (ret.errorCode != OH_HUKS_SUCCESS) {
41. return ret;
42. }
43. uint8_t outDataU[DH_COMMON_SIZE] = {0};
44. struct OH_Huks_Blob outDataUpdate = {DH_COMMON_SIZE, outDataU};
45. ret = OH_Huks_UpdateSession(&handle, initParamSet, publicKey, &outDataUpdate);
46. if (ret.errorCode != OH_HUKS_SUCCESS) {
47. return ret;
48. }
49. ret = OH_Huks_FinishSession(&handle, finishParamSet, &inData, outData);
50. if (ret.errorCode != OH_HUKS_SUCCESS) {
51. return ret;
52. }
53. return ret;
54. }

56. static OH_Huks_Result InitializeAgreeParamSets(struct OH_Huks_ParamSet **genParamSet,
57. struct OH_Huks_ParamSet **initParamSet01,
58. struct OH_Huks_ParamSet **finishParamSet01,
59. struct OH_Huks_ParamSet **initParamSet02,
60. struct OH_Huks_ParamSet **finishParamSet02)
61. {
62. OH_Huks_Result ohResult;

64. ohResult = InitParamSet(genParamSet, g_genAgreeParams,
65. sizeof(g_genAgreeParams) / sizeof(OH_Huks_Param));
66. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
67. return ohResult;
68. }
69. ohResult = InitParamSet(initParamSet01, g_agreeParamsInit01,
70. sizeof(g_agreeParamsInit01) / sizeof(OH_Huks_Param));
71. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
72. return ohResult;
73. }
74. ohResult = InitParamSet(finishParamSet01, g_agreeParamsFinish01,
75. sizeof(g_agreeParamsFinish01) / sizeof(OH_Huks_Param));
76. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
77. return ohResult;
78. }
79. ohResult = InitParamSet(initParamSet02, g_agreeParamsInit02,
80. sizeof(g_agreeParamsInit02) / sizeof(OH_Huks_Param));
81. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
82. return ohResult;
83. }
84. ohResult = InitParamSet(finishParamSet02, g_agreeParamsFinish02,
85. sizeof(g_agreeParamsFinish02) / sizeof(OH_Huks_Param));
86. return ohResult;
87. }

89. static OH_Huks_Result GenerateKeyPair(struct OH_Huks_ParamSet *genParamSet)
90. {
91. OH_Huks_Result ohResult;

93. /* 设备A生成密钥 */
94. ohResult = OH_Huks_GenerateKeyItem(&g_keyAlias01001, genParamSet, nullptr);
95. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
96. return ohResult;
97. }

99. /* 设备B生成密钥 */
100. ohResult = OH_Huks_GenerateKeyItem(&g_keyAlias02001, genParamSet, nullptr);
101. return ohResult;
102. }

104. static OH_Huks_Result KeyAgreement(struct OH_Huks_Blob *g_keyAlias,
105. struct OH_Huks_Blob *publicKey,
106. struct OH_Huks_Blob *outData,
107. struct OH_Huks_ParamSet *initParamSet,
108. struct OH_Huks_ParamSet *finishParamSet)
109. {
110. OH_Huks_Result ohResult;

112. ohResult = MallocAndCheckBlobData(outData, outData->size);
113. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
114. return ohResult;
115. }
116. /* 协商密钥 */
117. ohResult = HksDHAgreeFinish(g_keyAlias, publicKey, initParamSet, finishParamSet, outData);
118. return ohResult;
119. }

121. static void CleanKey(struct OH_Huks_Blob *genKeyAlias,
122. struct OH_Huks_Blob *genKeyAliasFinal,
123. struct OH_Huks_ParamSet *genParamSet,
124. struct OH_Huks_ParamSet **initParamSet,
125. struct OH_Huks_ParamSet **finishParamSet)
126. {
127. OH_Huks_DeleteKeyItem(genKeyAlias, genParamSet);
128. OH_Huks_DeleteKeyItem(genKeyAliasFinal, NULL);
129. OH_Huks_FreeParamSet(initParamSet);
130. OH_Huks_FreeParamSet(finishParamSet);
131. }

133. /* 协商密钥整体流程 */
134. napi_value DhAgreeKey(napi_env env, napi_callback_info info)
135. {
136. struct OH_Huks_ParamSet *genParamSet = nullptr;
137. struct OH_Huks_ParamSet *initParamSet01 = nullptr;
138. struct OH_Huks_ParamSet *finishParamSet01 = nullptr;
139. struct OH_Huks_ParamSet *initParamSet02 = nullptr;
140. struct OH_Huks_ParamSet *finishParamSet02 = nullptr;
141. struct OH_Huks_Blob publicKey01 = {.size = DH_COMMON_SIZE, .data = nullptr};
142. struct OH_Huks_Blob publicKey02 = {.size = DH_COMMON_SIZE, .data = nullptr};
143. struct OH_Huks_Blob outData01 = {.size = DH_COMMON_SIZE, .data = nullptr};
144. struct OH_Huks_Blob outData02 = {.size = DH_COMMON_SIZE, .data = nullptr};

146. OH_Huks_Result ohResult;
147. do {
148. /* 1.确定密钥别名集成密钥参数集 */
149. ohResult = InitializeAgreeParamSets(&genParamSet, &initParamSet01, &finishParamSet01,
150. &initParamSet02, &finishParamSet02);
151. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
152. break;
153. }
154. /* 2.设备A和设备B生成密钥 */
155. ohResult = GenerateKeyPair(genParamSet);
156. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
157. break;
158. }
159. ohResult = MallocAndCheckBlobData(&publicKey01, publicKey01.size);
160. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
161. break;
162. }
163. ohResult = MallocAndCheckBlobData(&publicKey02, publicKey02.size);
164. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
165. break;
166. }
167. /* 3.设备A、B导出公钥 */
168. ohResult = HksDHAgreeExport(&g_keyAlias01001, &g_keyAlias02001, &publicKey01, &publicKey02, genParamSet);
169. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
170. break;
171. }
172. /* 4.设备A、B执行密钥协商 */
173. ohResult = KeyAgreement(&g_keyAlias01001, &publicKey02, &outData01, initParamSet01, finishParamSet01);
174. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
175. break;
176. }
177. ohResult = KeyAgreement(&g_keyAlias02001, &publicKey01, &outData02, initParamSet02, finishParamSet02);
178. } while (0);
179. free(publicKey01.data);
180. free(publicKey02.data);
181. free(outData01.data);
182. free(outData02.data);
183. /* 5.设备A、B删除密钥 */
184. CleanKey(&g_keyAlias01001, &g_keyAliasFinal1001, genParamSet, &initParamSet01, &finishParamSet01);
185. CleanKey(&g_keyAlias02001, &g_keyAliasFinal2001, genParamSet, &initParamSet02, &finishParamSet02);
186. OH_Huks_FreeParamSet(&genParamSet);

188. napi_value ret;
189. napi_create_int32(env, ohResult.errorCode, &ret);
190. return ret;
191. }
```

[napi\_DH.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/KeyExchange/entry/src/main/cpp/types/projects/napi_DH.cpp#L102-L294)

### ECDH密钥协商用例

准备ECDH密钥协商材料：

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <cstring>
5. #include "file.h"

7. /* 初始化参数 */
8. static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
9. uint32_t paramCount)
10. {
11. OH_Huks_Result ret = OH_Huks_InitParamSet(paramSet);
12. if (ret.errorCode != OH_HUKS_SUCCESS) {
13. return ret;
14. }
15. ret = OH_Huks_AddParams(*paramSet, params, paramCount);
16. if (ret.errorCode != OH_HUKS_SUCCESS) {
17. OH_Huks_FreeParamSet(paramSet);
18. return ret;
19. }
20. ret = OH_Huks_BuildParamSet(paramSet);
21. if (ret.errorCode != OH_HUKS_SUCCESS) {
22. OH_Huks_FreeParamSet(paramSet);
23. return ret;
24. }
25. return ret;
26. }
27. static const uint32_t IV_SIZE = 16;
28. static uint8_t IV[IV_SIZE] = {0}; // this is a test value, for real use the iv should be different every time
29. static struct OH_Huks_Blob g_keyAliasFinal1001 = {(uint32_t)strlen("HksECDHAgreeKeyAliasTest001_1_final"),
30. (uint8_t *)"HksECDHAgreeKeyAliasTest001_1_final"};
31. /* 集成密钥参数集 */
32. static struct OH_Huks_Param g_genAgreeParams[] = {
33. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_ECC},
34. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
35. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_ECC_KEY_SIZE_256},
36. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};
37. static struct OH_Huks_Param g_agreeParamsInit01[] = {
38. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_ECDH},
39. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
40. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_ECC_KEY_SIZE_256}};
41. static struct OH_Huks_Param g_agreeParamsFinish01[] = {
42. {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_ONLY_USED_IN_HUKS},
43. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
44. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
45. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
46. {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_keyAliasFinal1001},
47. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
48. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_CBC}};
49. static struct OH_Huks_Blob g_keyAliasFinal2001 = {(uint32_t)strlen("HksECDHAgreeKeyAliasTest001_2_final"),
50. (uint8_t *)"HksECDHAgreeKeyAliasTest001_2_final"};
51. static struct OH_Huks_Param g_agreeParamsInit02[] = {
52. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_ECDH},
53. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
54. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_ECC_KEY_SIZE_256}};
55. static struct OH_Huks_Param g_agreeParamsFinish02[] = {
56. {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_ONLY_USED_IN_HUKS},
57. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
58. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
59. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
60. {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_keyAliasFinal2001},
61. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
62. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_CBC}};
63. static const uint32_t ECDH_COMMON_SIZE = 1024;
64. static struct OH_Huks_Blob g_keyAlias01001 = {(uint32_t)strlen("HksECDHAgreeKeyAliasTest001_1"),
65. (uint8_t *)"HksECDHAgreeKeyAliasTest001_1"};
66. static struct OH_Huks_Blob g_keyAlias02001 = {(uint32_t)strlen("HksECDHAgreeKeyAliasTest001_2"),
67. (uint8_t *)"HksECDHAgreeKeyAliasTest001_2"};
```

[napi\_ECDH.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/KeyExchange/entry/src/main/cpp/types/projects/napi_ECDH.cpp#L15-L83)

ECDH密钥协商的功能函数实现，包括内存分配、参数初始化、密钥生成、和资源清理等：

```
1. static OH_Huks_Result MallocAndCheckBlobData(struct OH_Huks_Blob *blob, const uint32_t blobSize)
2. {
3. struct OH_Huks_Result ret;
4. ret.errorCode = OH_HUKS_SUCCESS;
5. if (blobSize == 0 || blobSize > ECDH_COMMON_SIZE) {
6. ret.errorCode = OH_HUKS_ERR_CODE_INTERNAL_ERROR;
7. return ret;
8. }
9. blob->data = (uint8_t *)malloc(blobSize);
10. if (blob->data == NULL) {
11. ret.errorCode = OH_HUKS_ERR_CODE_INTERNAL_ERROR;
12. }
13. return ret;
14. }

16. /* 导出密钥 */
17. OH_Huks_Result HksEcdhAgreeExport(const struct OH_Huks_Blob *keyAlias1, const struct OH_Huks_Blob *keyAlias2,
18. struct OH_Huks_Blob *publicKey1, struct OH_Huks_Blob *publicKey2,
19. const struct OH_Huks_ParamSet *genParamSet)
20. {
21. OH_Huks_Result ret = OH_Huks_ExportPublicKeyItem(keyAlias1, genParamSet, publicKey1);
22. if (ret.errorCode != OH_HUKS_SUCCESS) {
23. return ret;
24. }
25. ret = OH_Huks_ExportPublicKeyItem(keyAlias2, genParamSet, publicKey2);
26. if (ret.errorCode != OH_HUKS_SUCCESS) {
27. return ret;
28. }
29. return ret;
30. }
31. static const char *IN_DATA = "Hks_ECDH_Agree_Test_000000000000000000000000000000000000000000000000000000000000"
32. "00000000000000000000000000000000000000000000000000000000000000000000000000000000"
33. "0000000000000000000000000000000000000000000000000000000000000000000000000_string";
34. /* 协商密钥操作 */
35. OH_Huks_Result HksEcdhAgreeFinish(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_Blob *publicKey,
36. const struct OH_Huks_ParamSet *initParamSet,
37. const struct OH_Huks_ParamSet *finishParamSet, struct OH_Huks_Blob *outData)
38. {
39. struct OH_Huks_Blob inData = {(uint32_t)strlen(IN_DATA), (uint8_t *)IN_DATA};
40. uint8_t handleU[sizeof(uint64_t)] = {0};
41. struct OH_Huks_Blob handle = {sizeof(uint64_t), handleU};
42. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, initParamSet, &handle, nullptr);
43. if (ret.errorCode != OH_HUKS_SUCCESS) {
44. return ret;
45. }
46. uint8_t outDataU[ECDH_COMMON_SIZE] = {0};
47. struct OH_Huks_Blob outDataUpdate = {ECDH_COMMON_SIZE, outDataU};
48. ret = OH_Huks_UpdateSession(&handle, initParamSet, publicKey, &outDataUpdate);
49. if (ret.errorCode != OH_HUKS_SUCCESS) {
50. return ret;
51. }
52. ret = OH_Huks_FinishSession(&handle, finishParamSet, &inData, outData);
53. if (ret.errorCode != OH_HUKS_SUCCESS) {
54. return ret;
55. }
56. return ret;
57. }

60. static OH_Huks_Result InitializeAgreeParamSets(struct OH_Huks_ParamSet **genParamSet,
61. struct OH_Huks_ParamSet **initParamSet01,
62. struct OH_Huks_ParamSet **finishParamSet01,
63. struct OH_Huks_ParamSet **initParamSet02,
64. struct OH_Huks_ParamSet **finishParamSet02)
65. {
66. OH_Huks_Result ohResult;

68. ohResult = InitParamSet(genParamSet, g_genAgreeParams,
69. sizeof(g_genAgreeParams) / sizeof(OH_Huks_Param));
70. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
71. return ohResult;
72. }
73. ohResult = InitParamSet(initParamSet01, g_agreeParamsInit01,
74. sizeof(g_agreeParamsInit01) / sizeof(OH_Huks_Param));
75. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
76. return ohResult;
77. }
78. ohResult = InitParamSet(finishParamSet01, g_agreeParamsFinish01,
79. sizeof(g_agreeParamsFinish01) / sizeof(OH_Huks_Param));
80. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
81. return ohResult;
82. }
83. ohResult = InitParamSet(initParamSet02, g_agreeParamsInit02,
84. sizeof(g_agreeParamsInit02) / sizeof(OH_Huks_Param));
85. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
86. return ohResult;
87. }
88. ohResult = InitParamSet(finishParamSet02, g_agreeParamsFinish02,
89. sizeof(g_agreeParamsFinish02) / sizeof(OH_Huks_Param));
90. return ohResult;
91. }

93. static OH_Huks_Result GenerateKeyPair(struct OH_Huks_ParamSet *genParamSet)
94. {
95. OH_Huks_Result ohResult;

97. /* 设备A生成密钥 */
98. ohResult = OH_Huks_GenerateKeyItem(&g_keyAlias01001, genParamSet, nullptr);
99. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
100. return ohResult;
101. }

103. /* 设备B生成密钥 */
104. ohResult = OH_Huks_GenerateKeyItem(&g_keyAlias02001, genParamSet, nullptr);
105. return ohResult;
106. }

108. static OH_Huks_Result KeyAgreement(struct OH_Huks_Blob *g_keyAlias,
109. struct OH_Huks_Blob *publicKey,
110. struct OH_Huks_Blob *outData,
111. struct OH_Huks_ParamSet *initParamSet,
112. struct OH_Huks_ParamSet *finishParamSet)
113. {
114. OH_Huks_Result ohResult;

116. ohResult = MallocAndCheckBlobData(outData, outData->size);
117. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
118. return ohResult;
119. }
120. /* 协商密钥 */
121. ohResult = HksEcdhAgreeFinish(g_keyAlias, publicKey, initParamSet, finishParamSet, outData);
122. return ohResult;
123. }

125. static void CleanKey(struct OH_Huks_Blob *genKeyAlias,
126. struct OH_Huks_Blob *genKeyAliasFinal,
127. struct OH_Huks_ParamSet *genParamSet,
128. struct OH_Huks_ParamSet **initParamSet,
129. struct OH_Huks_ParamSet **finishParamSet)
130. {
131. OH_Huks_DeleteKeyItem(genKeyAlias, genParamSet);
132. OH_Huks_DeleteKeyItem(genKeyAliasFinal, NULL);
133. OH_Huks_FreeParamSet(initParamSet);
134. OH_Huks_FreeParamSet(finishParamSet);
135. }
```

[napi\_ECDH.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/KeyExchange/entry/src/main/cpp/types/projects/napi_ECDH.cpp#L85-L221)

ECDH密钥协商的完整流程实现：

```
1. /* 协商密钥整体流程 */
2. napi_value EcdhAgreeKey(napi_env env, napi_callback_info info)
3. {
4. struct OH_Huks_ParamSet *genParamSet = nullptr;
5. struct OH_Huks_ParamSet *initParamSet01 = nullptr;
6. struct OH_Huks_ParamSet *finishParamSet01 = nullptr;
7. struct OH_Huks_ParamSet *initParamSet02 = nullptr;
8. struct OH_Huks_ParamSet *finishParamSet02 = nullptr;
9. struct OH_Huks_Blob publicKey01 = {.size = OH_HUKS_ECC_KEY_SIZE_256, .data = nullptr};
10. struct OH_Huks_Blob publicKey02 = {.size = OH_HUKS_ECC_KEY_SIZE_256, .data = nullptr};
11. struct OH_Huks_Blob outData01 = {.size = ECDH_COMMON_SIZE, .data = nullptr};
12. struct OH_Huks_Blob outData02 = {.size = ECDH_COMMON_SIZE, .data = nullptr};
13. OH_Huks_Result ohResult;
14. do {
15. /* 1.确定密钥别名集成密钥参数集 */
16. ohResult = InitializeAgreeParamSets(&genParamSet, &initParamSet01, &finishParamSet01,
17. &initParamSet02, &finishParamSet02);
18. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
19. break;
20. }
21. /* 2.设备A和设备B生成密钥 */
22. ohResult = GenerateKeyPair(genParamSet);
23. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
24. break;
25. }
26. ohResult = MallocAndCheckBlobData(&publicKey01, publicKey01.size);
27. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
28. break;
29. }
30. ohResult = MallocAndCheckBlobData(&publicKey02, publicKey02.size);
31. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
32. break;
33. }
34. /* 3.设备A、B导出公钥 */
35. ohResult = HksEcdhAgreeExport(&g_keyAlias01001, &g_keyAlias02001, &publicKey01, &publicKey02, genParamSet);
36. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
37. break;
38. }
39. /* 4.设备A、B执行密钥协商 */
40. ohResult = KeyAgreement(&g_keyAlias01001, &publicKey02, &outData01, initParamSet01, finishParamSet01);
41. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
42. break;
43. }
44. ohResult = KeyAgreement(&g_keyAlias02001, &publicKey01, &outData02, initParamSet02, finishParamSet02);
45. } while (0);
46. free(publicKey01.data);
47. free(publicKey02.data);
48. free(outData01.data);
49. free(outData02.data);
50. /* 5.设备A、B删除密钥 */
51. CleanKey(&g_keyAlias01001, &g_keyAliasFinal1001, genParamSet, &initParamSet01, &finishParamSet01);
52. CleanKey(&g_keyAlias02001, &g_keyAliasFinal2001, genParamSet, &initParamSet02, &finishParamSet02);
53. OH_Huks_FreeParamSet(&genParamSet);

55. napi_value ret;
56. napi_create_int32(env, ohResult.errorCode, &ret);
57. return ret;
58. }
```

[napi\_ECDH.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/KeyExchange/entry/src/main/cpp/types/projects/napi_ECDH.cpp#L223-L282)
