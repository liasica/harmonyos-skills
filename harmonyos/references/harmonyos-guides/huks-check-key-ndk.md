---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-check-key-ndk
title: 查询密钥是否存在(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 其他操作 > 查询密钥是否存在 > 查询密钥是否存在(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:df87642517a5ba766735b9bf79abadb9c23bc989303e1e5ea23c1a38cbfc15c9
---

HUKS提供了接口供应用查询指定密钥是否存在。

从API 23开始支持[群组密钥](huks-group-key-overview.md)特性。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

## 开发步骤

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集。用于查询时指定密钥的属性，查询单个密钥或者非群组密钥，可传空。
3. 调用接口[OH\_Huks\_IsKeyItemExist](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_iskeyitemexist)，查询密钥是否存在。

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <cstring>

6. OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
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

26. struct OH_Huks_Param g_testGenerateKeyParam[] = {{.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_ECC},
27. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
28. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_ECC_KEY_SIZE_256},
29. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};

31. /* 1.生成密钥 */
32. static OH_Huks_Result GenerateKeyHelper(const char *alias)
33. {
34. struct OH_Huks_Blob aliasBlob = {.size = (uint32_t)strlen(alias), .data = (uint8_t *)alias};
35. struct OH_Huks_ParamSet *testGenerateKeyParamSet = nullptr;
36. struct OH_Huks_Result ohResult;

38. do {
39. ohResult = InitParamSet(&testGenerateKeyParamSet, g_testGenerateKeyParam,
40. sizeof(g_testGenerateKeyParam) / sizeof(OH_Huks_Param));
41. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
42. break;
43. }

45. ohResult = OH_Huks_GenerateKeyItem(&aliasBlob, testGenerateKeyParamSet, nullptr);
46. } while (0);

48. OH_Huks_FreeParamSet(&testGenerateKeyParamSet);
49. return ohResult;
50. }

52. static napi_value IsKeyExist(napi_env env, napi_callback_info info)
53. {
54. const char *alias = "test_key";
55. struct OH_Huks_Blob keyAlias = {
56. (uint32_t)strlen(alias),
57. (uint8_t *)alias
58. };

60. /* 1.生成密钥 */
61. OH_Huks_Result genResult = GenerateKeyHelper(alias);
62. if (genResult.errorCode != OH_HUKS_SUCCESS) {
63. napi_value ret;
64. napi_create_int32(env, genResult.errorCode, &ret);
65. return ret;
66. }

68. /* 2.检查密钥是否存在 */
69. struct OH_Huks_Result ohResult = OH_Huks_IsKeyItemExist(&keyAlias, nullptr);

71. napi_value ret;
72. napi_create_int32(env, ohResult.errorCode, &ret);
73. return ret;
74. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/OtherOperations/CheckKeyExists/entry/src/main/cpp/napi_init.cpp#L15-L90)
