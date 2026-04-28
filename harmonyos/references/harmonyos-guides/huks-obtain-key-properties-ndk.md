---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-obtain-key-properties-ndk
title: 获取密钥属性(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 其他操作 > 获取密钥属性 > 获取密钥属性(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f20c9cf803a05e058aa48211feb8c90e791b5e8f8c29a4410e869b2ee9eb4845
---

HUKS提供了接口供业务获取指定密钥的相关属性。在获取指定密钥属性前，需要确保已在HUKS中生成或导入持久化存储的密钥。

说明

轻量级智能穿戴不支持获取密钥属性功能。

从API 23开始支持[群组密钥](huks-group-key-overview.md)特性。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

## 开发步骤

1. 构造对应参数。

   * keyAlias：密钥别名，封装成[OH\_Huks\_Blob](../harmonyos-references/capi-hukstypeapi-oh-huks-blob.md)结构，密钥别名最大长度为128字节。
   * paramSetIn：预留参数，暂不需要处理，传空即可。
   * paramSetOut：用于放置获取到的参数集结果，为[OH\_Huks\_ParamSet](../harmonyos-references/capi-hukstypeapi-oh-huks-paramset.md)类型对象，需要业务提前申请好内存，需申请足够容纳获取到的密钥属性集的内存大小。
2. 调用接口[OH\_Huks\_GetKeyItemParamSet](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_getkeyitemparamset)，传入上述参数。
3. 返回值为成功码/错误码，获取成功后，从参数集中读取需要的参数。

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

31. static OH_Huks_Result GenerateKeyHelper(const char *alias)
32. {
33. struct OH_Huks_Blob aliasBlob = {.size = (uint32_t)strlen(alias), .data = (uint8_t *)alias};
34. struct OH_Huks_ParamSet *testGenerateKeyParamSet = nullptr;
35. struct OH_Huks_Result ohResult;
36. do {
37. /* 1.初始化密钥属性集 */
38. ohResult = InitParamSet(&testGenerateKeyParamSet, g_testGenerateKeyParam,
39. sizeof(g_testGenerateKeyParam) / sizeof(OH_Huks_Param));
40. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
41. break;
42. }
43. /* 1.生成密钥 */
44. ohResult = OH_Huks_GenerateKeyItem(&aliasBlob, testGenerateKeyParamSet, nullptr);
45. } while (0);
46. OH_Huks_FreeParamSet(&testGenerateKeyParamSet);
47. return ohResult;
48. }

50. static napi_value GetKeyParamSet(napi_env env, napi_callback_info info)
51. {
52. /* 1. 参数构造：确定密钥别名 */
53. const char *alias = "test_key";
54. struct OH_Huks_Blob aliasBlob = { .size = (uint32_t)strlen(alias), .data = (uint8_t *)alias };
55. /* 生成密钥 */
56. OH_Huks_Result genResult = GenerateKeyHelper(alias);
57. if (genResult.errorCode != OH_HUKS_SUCCESS) {
58. napi_value ret;
59. napi_create_int32(env, genResult.errorCode, &ret);
60. return ret;
61. }
62. const size_t paramSetSize = 512;
63. /* 构造参数：为参数集申请内存
64. * 请业务按实际情况评估大小进行申请
65. */
66. struct OH_Huks_ParamSet *outParamSet = static_cast<struct OH_Huks_ParamSet *>(malloc(paramSetSize));
67. if (outParamSet == nullptr) {
68. return nullptr;
69. }
70. outParamSet->paramSetSize = paramSetSize;
71. struct OH_Huks_Result ohResult;
72. do {
73. /* 2. 获取密钥属性集 */
74. ohResult = OH_Huks_GetKeyItemParamSet(&aliasBlob, nullptr, outParamSet);
75. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
76. break;
77. }
78. /* 3. 从参数集中读取参数，以OH_HUKS_TAG_PURPOSE为例 */
79. OH_Huks_Param *purposeParam = nullptr; // 无需申请内存，获取后指针指向该参数在参数集中所处内存地址
80. ohResult = OH_Huks_GetParam(outParamSet, OH_HUKS_TAG_PURPOSE, &purposeParam);
81. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
82. break;
83. }
84. } while (0);
85. OH_Huks_FreeParamSet(&outParamSet);
86. napi_value ret;
87. napi_create_int32(env, ohResult.errorCode, &ret);
88. return ret;
89. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/OtherOperations/GetKeyAttributes/entry/src/main/cpp/napi_init.cpp#L15-L106)
