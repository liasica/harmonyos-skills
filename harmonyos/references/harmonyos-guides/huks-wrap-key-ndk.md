---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-wrap-key-ndk
title: 加密导出导入密钥(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 其他操作 > 加密导出导入密钥 > 加密导出导入密钥(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0eba3ce7a46b2435c898f9a5fbdebc5f7be1fa8dd096dce8b92ab41f2e95e11a
---

从API 20开始，支持加密导出导入密钥。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

## 开发步骤

1. 初始化生成密钥属性集，需要设置[OH\_HUKS\_TAG\_IS\_ALLOWED\_WRAP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，指定密钥允许导出。
2. 调用[OH\_Huks\_GenerateKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_generatekeyitem)生成密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。
3. 调用[OH\_Huks\_WrapKey](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_wrapkey)加密导出密钥。
4. 调用[OH\_Huks\_UnwrapKey](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_unwrapkey)加密导入密钥。

## 开发案例

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <string.h>

6. OH_Huks_Result InitParamSet(
7. struct OH_Huks_ParamSet **paramSet,
8. const struct OH_Huks_Param *params,
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

28. struct OH_Huks_Param g_testGenerateKeyParam[] = {
29. {
30. .tag = OH_HUKS_TAG_ALGORITHM,
31. .uint32Param = OH_HUKS_ALG_ECC
32. }, {
33. .tag = OH_HUKS_TAG_PURPOSE,
34. .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE
35. }, {
36. .tag = OH_HUKS_TAG_KEY_SIZE,
37. .uint32Param = OH_HUKS_ECC_KEY_SIZE_256
38. }, {
39. .tag = OH_HUKS_TAG_DIGEST,
40. .uint32Param = OH_HUKS_DIGEST_NONE
41. }, {
42. .tag = OH_HUKS_TAG_IS_ALLOWED_WRAP,
43. .boolParam = true
44. }
45. };

47. struct OH_Huks_Param g_wrapKeyParam[] = {
48. {
49. .tag = OH_HUKS_TAG_KEY_WRAP_TYPE,
50. .uint32Param = OH_HUKS_KEY_WRAP_TYPE_HUK_BASED
51. }
52. };

54. static napi_value GenerateKey(napi_env env, napi_callback_info info)
55. {
56. /* 1.确定密钥别名 */
57. const char *alias = "test_generate";
58. struct OH_Huks_Blob aliasBlob = { .size = (uint32_t)strlen(alias), .data = (uint8_t *)alias };
59. struct OH_Huks_ParamSet *testGenerateKeyParamSet = nullptr;
60. struct OH_Huks_ParamSet *wrapKeyParamSet = nullptr;
61. struct OH_Huks_Result ohResult;
62. do {
63. /* 2.初始化密钥属性集 */
64. ohResult = InitParamSet(&testGenerateKeyParamSet, g_testGenerateKeyParam,
65. sizeof(g_testGenerateKeyParam) / sizeof(OH_Huks_Param));
66. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
67. break;
68. }

70. /* 3.生成密钥 */
71. ohResult = OH_Huks_GenerateKeyItem(&aliasBlob, testGenerateKeyParamSet, nullptr);
72. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
73. break;
74. }

76. /* 4.初始化加密导出导入密钥属性集 */
77. ohResult = InitParamSet(&wrapKeyParamSet, g_wrapKeyParam,
78. sizeof(g_wrapKeyParam) / sizeof(OH_Huks_Param));
79. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
80. break;
81. }

83. /* 5.加密导出密钥 */
84. uint8_t WrappedData[2048] = {0};
85. struct OH_Huks_Blob wrappedKey = {2048, WrappedData};
86. ohResult = OH_Huks_WrapKey(&aliasBlob, wrapKeyParamSet, &wrappedKey);
87. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
88. break;
89. }

91. /* 6.加密导入密钥 */
92. ohResult = OH_Huks_UnwrapKey(&aliasBlob, wrapKeyParamSet, &wrappedKey);
93. } while (0);
94. OH_Huks_FreeParamSet(&testGenerateKeyParamSet);
95. OH_Huks_FreeParamSet(&wrapKeyParamSet);
96. napi_value ret;
97. napi_create_int32(env, ohResult.errorCode, &ret);
98. return ret;
99. }
```
